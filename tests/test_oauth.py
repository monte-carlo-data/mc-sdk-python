from __future__ import annotations

from pathlib import Path

import pytest

from montecarlo import UsersApi
from montecarlo import oauth as oauth_module
from montecarlo.auth import CredentialsError, Options, new_client
from montecarlo.oauth import TokenSource, scopes_for_instance
from tests.conftest import FakeApi


def _authorization_headers(request) -> list[str]:
    return [v for k, v in request.headers if k.lower() == "authorization"]


@pytest.mark.parametrize(
    ("instance", "want"),
    [
        ("us1", ["https://api.getmontecarlo.com/access", "https://instance.getmontecarlo.com/us1"]),
        ("", ["https://api.getmontecarlo.com/access", "https://instance.getmontecarlo.com/"]),
    ],
)
def test_scopes_for_instance_appends_the_instance_scope_after_access(
    instance: str, want: list[str]
) -> None:
    """The access scope is spelled out literally, so a typo in the constant fails here."""
    assert scopes_for_instance(instance) == want


def test_client_credentials_go_in_the_form_body_with_both_scopes(
    isolate: Path, fake_api: FakeApi
) -> None:
    options = Options(
        endpoint=fake_api.url,
        client_id="client-id",
        client_secret="client-secret",
        instance="eu1",
        config_dir=isolate,
    )
    UsersApi(new_client(options)).get_current_user()

    (token_request,) = fake_api.token_requests()
    assert token_request.form == {
        "grant_type": ["client_credentials"],
        "client_id": ["client-id"],
        "client_secret": ["client-secret"],
        "scope": ["https://api.getmontecarlo.com/access https://instance.getmontecarlo.com/eu1"],
    }
    assert not _authorization_headers(token_request)


def test_new_client_sends_only_one_authorization_header_with_a_delegated_token(
    isolate: Path, fake_api: FakeApi
) -> None:
    """A per-request credential set through `_request_auth` wins; nothing stacks a second one."""
    client = new_client(
        Options(
            endpoint=fake_api.url,
            token_id="static-id",
            token_secret="static-secret",
            config_dir=isolate,
        )
    )
    UsersApi(client).get_current_user(
        _request_auth={
            "type": "bearer",
            "in": "header",
            "key": "Authorization",
            "value": "Bearer delegated-token",
        }
    )

    (request,) = fake_api.api_requests()
    assert _authorization_headers(request) == ["Bearer delegated-token"]


def test_credentials_never_reach_the_configuration(isolate: Path) -> None:
    """Anything can log the configuration; `to_debug_report` and `access_token` are public."""
    for options in (
        Options(
            endpoint="https://api.example.com", token_id="leaked-id", token_secret="leaked-secret"
        ),
        Options(
            endpoint="https://api.example.com",
            client_id="leaked-client",
            client_secret="leaked-client-secret",
            instance="us1",
        ),
    ):
        options.config_dir = isolate
        configuration = new_client(options).configuration
        assert configuration.access_token is None
        rendered = repr(vars(configuration)) + configuration.to_debug_report()
        assert "leaked" not in rendered


def test_token_is_cached_until_shortly_before_expiry(
    isolate: Path, fake_api: FakeApi, monkeypatch: pytest.MonkeyPatch
) -> None:
    now = [1_000.0]
    monkeypatch.setattr(oauth_module.time, "monotonic", lambda: now[0])
    fake_api.token_responses = [
        (200, {"access_token": "first", "expires_in": 300}),
        (200, {"access_token": "second", "expires_in": 300}),
    ]
    api = UsersApi(
        new_client(
            Options(
                endpoint=fake_api.url,
                client_id="id",
                client_secret="secret",
                instance="us1",
                config_dir=isolate,
            )
        )
    )

    api.get_current_user()
    api.get_current_user()
    assert len(fake_api.token_requests()) == 1

    # 300s lifetime, renewed 60s early: still cached at +239s, renewed at +240s.
    now[0] += 239
    api.get_current_user()
    assert len(fake_api.token_requests()) == 1
    now[0] += 1
    api.get_current_user()
    assert len(fake_api.token_requests()) == 2
    assert _authorization_headers(fake_api.api_requests()[-1]) == ["Bearer second"]


def test_token_request_retries_a_5xx_but_not_a_4xx(fake_api: FakeApi) -> None:
    fake_api.token_responses = [(503, {}), (200, {"access_token": "after-retry"})]
    source = TokenSource("id", "secret", "us1", fake_api.url + "/oauth2/token")
    assert source.token() == "after-retry"
    assert len(fake_api.token_requests()) == 2

    fake_api.requests.clear()
    fake_api.token_responses = [(401, {"error": "invalid_client"})]
    source = TokenSource("id", "wrong", "us1", fake_api.url + "/oauth2/token")
    with pytest.raises(CredentialsError, match="status 401"):
        source.token()
    assert len(fake_api.token_requests()) == 1


def test_token_response_without_an_access_token_is_an_error(fake_api: FakeApi) -> None:
    fake_api.token_responses = [(200, {"token_type": "Bearer"})]
    source = TokenSource("id", "secret", "us1", fake_api.url + "/oauth2/token")
    with pytest.raises(CredentialsError, match="no access_token"):
        source.token()


def test_an_unparseable_expires_in_falls_back_to_an_hour(
    fake_api: FakeApi, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(oauth_module.time, "monotonic", lambda: 0.0)
    fake_api.token_responses = [(200, {"access_token": "t", "expires_in": "soon"})]
    source = TokenSource("id", "secret", "us1", fake_api.url + "/oauth2/token")
    source.token()
    assert source._expires_at == 3600 - 60
