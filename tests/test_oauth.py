from __future__ import annotations

import threading
from pathlib import Path

import pytest

from pycarlo2 import UsersApi
from pycarlo2.auth import CredentialsError, Options, new_client
from pycarlo2.oauth import TokenSource, scopes_for_instance, validate_instance_id
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


def test_token_is_cached_until_shortly_before_expiry(fake_api: FakeApi) -> None:
    now = [1_000.0]
    fake_api.token_responses = [
        (200, {"access_token": "first", "expires_in": 300}),
        (200, {"access_token": "second", "expires_in": 300}),
    ]
    source = TokenSource(
        "id", "secret", "us1", fake_api.url + "/oauth2/token", clock=lambda: now[0]
    )

    assert source.token() == "first"
    assert source.token() == "first"
    assert len(fake_api.token_requests()) == 1

    # 300s lifetime, renewed 60s early: still cached at +239s, renewed at +240s.
    now[0] += 239
    assert source.token() == "first"
    assert len(fake_api.token_requests()) == 1
    now[0] += 1
    assert source.token() == "second"
    assert len(fake_api.token_requests()) == 2


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


@pytest.mark.parametrize("expires_in", ["soon", None])
def test_an_unparseable_expires_in_falls_back_to_an_hour(
    fake_api: FakeApi, expires_in: str | None
) -> None:
    now = [0.0]
    fake_api.token_responses = [
        (200, {"access_token": "first", "expires_in": expires_in}),
        (200, {"access_token": "second", "expires_in": expires_in}),
    ]
    source = TokenSource(
        "id", "secret", "us1", fake_api.url + "/oauth2/token", clock=lambda: now[0]
    )

    assert source.token() == "first"
    assert len(fake_api.token_requests()) == 1

    now[0] += 3600 - 60 - 1
    assert source.token() == "first"
    assert len(fake_api.token_requests()) == 1

    now[0] += 1
    assert source.token() == "second"
    assert len(fake_api.token_requests()) == 2


def test_a_short_lived_token_is_still_cached_for_half_its_life(fake_api: FakeApi) -> None:
    now = [0.0]
    fake_api.token_responses = [
        (200, {"access_token": "first", "expires_in": 30}),
        (200, {"access_token": "second", "expires_in": 30}),
    ]
    source = TokenSource(
        "id", "secret", "us1", fake_api.url + "/oauth2/token", clock=lambda: now[0]
    )

    assert source.token() == "first"

    now[0] += 14
    assert source.token() == "first"
    assert len(fake_api.token_requests()) == 1

    now[0] += 1
    assert source.token() == "second"
    assert len(fake_api.token_requests()) == 2


def test_token_source_validates_its_inputs() -> None:
    with pytest.raises(CredentialsError, match="instance id"):
        TokenSource("id", "secret", "us 1", "https://x/oauth2/token")
    with pytest.raises(CredentialsError, match="token url must use https"):
        TokenSource("id", "secret", "us1", "http://attacker.example/oauth2/token")


def test_concurrent_callers_share_one_token_request(fake_api: FakeApi) -> None:
    fake_api.token_responses = [(200, {"access_token": "shared", "expires_in": 3600})]
    source = TokenSource("id", "secret", "us1", fake_api.url + "/oauth2/token")
    barrier = threading.Barrier(8)
    lock = threading.Lock()
    tokens: list[str] = []

    def call() -> None:
        barrier.wait()
        token = source.token()
        with lock:
            tokens.append(token)

    threads = [threading.Thread(target=call) for _ in range(8)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    assert tokens == ["shared"] * 8
    assert len(fake_api.token_requests()) == 1


@pytest.mark.parametrize("instance", ["a", "us1", "US-1", "a" * 63])
def test_validate_instance_id_accepts_a_dns_safe_identifier(instance: str) -> None:
    validate_instance_id(instance)


@pytest.mark.parametrize("instance", ["", "us_1", "us 1", "us.1", "a" * 64, "us1/../other"])
def test_validate_instance_id_rejects_anything_else(instance: str) -> None:
    with pytest.raises(CredentialsError, match="invalid instance id"):
        validate_instance_id(instance)


def test_token_request_does_not_follow_a_redirect_with_the_client_secret(
    fake_api: FakeApi,
) -> None:
    """`_request` builds its `urllib3.Retry` without `redirect=0`, so a 302 from the token
    endpoint is followed and the form body, client_secret included, is re-POSTed to wherever
    the redirect points."""
    fake_api.token_responses = [(302, {"Location": fake_api.url + "/collector"})]
    source = TokenSource("id", "secret", "us1", fake_api.url + "/oauth2/token")
    with pytest.raises(CredentialsError):
        source.token()
    assert fake_api.requests_for("/collector") == []
    assert len(fake_api.token_requests()) == 1


@pytest.mark.parametrize(
    ("body", "match"),
    [
        ("<html>login</html>", "not JSON"),
        ([], "JSON object"),
    ],
)
def test_a_non_json_token_response_is_a_credentials_error(
    fake_api: FakeApi, body: str | list, match: str
) -> None:
    """`_request` calls `json.loads(response.data)` unguarded, so a non-JSON body or a JSON
    body that is not an object surfaces as a bare `json.JSONDecodeError` or `AttributeError`
    instead of a `CredentialsError`."""
    fake_api.token_responses = [(200, body)]
    source = TokenSource("id", "secret", "us1", fake_api.url + "/oauth2/token")
    with pytest.raises(CredentialsError, match=match):
        source.token()
