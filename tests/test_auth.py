from __future__ import annotations

from pathlib import Path

import pytest

from montecarlo import UsersApi, __version__
from montecarlo.auth import CredentialsError, Options, new_client
from tests.conftest import FakeApi

HTTPS = "https://api.example.com"


@pytest.mark.parametrize(
    ("options", "want"),
    [
        (Options(token="t"), "endpoint is required"),
        (Options(endpoint=HTTPS), "no credentials"),
        (Options(endpoint=HTTPS, client_id="id"), "client id and client secret are both required"),
        (Options(endpoint=HTTPS, client_id="id", client_secret="s"), "instance is required"),
        (Options(endpoint=HTTPS, token_id="id"), "token id and token secret are both required"),
        (
            Options(endpoint=HTTPS, client_id="id", client_secret="s", instance="us 1"),
            "instance id",
        ),
    ],
)
def test_validate_rejects_an_incomplete_mechanism(options: Options, want: str) -> None:
    with pytest.raises(CredentialsError, match=want):
        options.validate()


@pytest.mark.parametrize(
    "options",
    [
        Options(endpoint=HTTPS, token_id="id", token_secret="secret"),
        Options(endpoint=HTTPS, client_id="id", client_secret="secret", instance="us1"),
        Options(endpoint=HTTPS, token="access-token"),
    ],
)
def test_validate_accepts_each_complete_mechanism(options: Options) -> None:
    options.validate()


def test_api_token_becomes_a_colon_joined_bearer() -> None:
    """The gateway parses an API token from `Bearer <id>:<secret>`."""
    options = Options(endpoint=HTTPS, token_id="key-id", token_secret="s3cret")
    assert options.bearer() == "key-id:s3cret"


def test_oauth_takes_precedence_and_carries_no_static_bearer(
    isolate: Path, fake_api: FakeApi
) -> None:
    """Proven on the header that goes out, not on which mechanism reports itself in use."""
    options = Options(
        endpoint=fake_api.url,
        client_id="id",
        client_secret="secret",
        instance="us1",
        token_id="key-id",
        token_secret="s3cret",
        token="access-token",
        config_dir=isolate,
    )
    assert options.uses_oauth()
    assert options.bearer(), "a static bearer must also be available, to prove OAuth wins"

    UsersApi(new_client(options)).get_current_user()

    (request,) = fake_api.api_requests()
    authorization = [v for k, v in request.headers if k.lower() == "authorization"]
    assert authorization == ["Bearer oauth-access-token"]


def test_token_url_defaults_under_the_endpoint() -> None:
    options = Options(endpoint="https://api.example.com/")
    assert options.resolved_token_url() == "https://api.example.com/oauth2/token"

    options.token_url = "https://login.example.com/token"
    assert options.resolved_token_url() == options.token_url


def test_new_client_sets_the_endpoint_with_the_trailing_slash_trimmed(isolate: Path) -> None:
    """The generated configuration has no usable default host, so it has to be set."""
    client = new_client(
        Options(endpoint=HTTPS + "/", token_id="id", token_secret="secret", config_dir=isolate)
    )
    assert client.configuration.host == HTTPS


def test_new_client_rejects_missing_credentials(isolate: Path) -> None:
    with pytest.raises(CredentialsError, match="no credentials"):
        new_client(Options(endpoint=HTTPS, config_dir=isolate))


def test_new_client_rejects_a_missing_endpoint(isolate: Path) -> None:
    """Without this the client would silently send every request to a relative URL."""
    with pytest.raises(CredentialsError, match="endpoint is required"):
        new_client(Options(token_id="id", token_secret="secret", config_dir=isolate))


@pytest.mark.parametrize(
    ("endpoint", "accepted"),
    [
        ("http://collector.attacker.example", False),
        ("api.getmontecarlo.com", False),
        ("https://api.getmontecarlo.com", True),
        ("http://127.0.0.1:8080", True),
        ("http://localhost:8080", True),
    ],
)
def test_validate_requires_an_https_endpoint_except_loopback(endpoint: str, accepted: bool) -> None:
    options = Options(endpoint=endpoint, token_id="id", token_secret="secret")
    if accepted:
        options.validate()
    else:
        with pytest.raises(CredentialsError, match="must"):
            options.validate()


def test_validate_requires_an_https_token_url() -> None:
    """The token exchange can leak client credentials as easily as the API endpoint can."""
    options = Options(
        endpoint=HTTPS,
        client_id="id",
        client_secret="secret",
        instance="us1",
        token_url="http://attacker.example/oauth2/token",
    )
    with pytest.raises(CredentialsError, match="token url must use https"):
        options.validate()


def test_user_agent_identifies_the_sdk_unless_overridden(isolate: Path) -> None:
    options = Options(endpoint=HTTPS, token_id="id", token_secret="secret", config_dir=isolate)
    assert new_client(options).user_agent.startswith(f"mc-sdk-python/{__version__} (python/")

    options.user_agent = "my-tool/1.0"
    assert new_client(options).user_agent == "my-tool/1.0"


def test_options_repr_hides_secrets() -> None:
    rendered = repr(
        Options(
            endpoint=HTTPS,
            token_id="key-id",
            token_secret="token-secret",
            token="bearer-secret",
            client_id="client-id",
            client_secret="client-secret",
        )
    )
    assert "key-id" in rendered
    assert "client-id" in rendered
    for secret in ("token-secret", "bearer-secret", "client-secret"):
        assert secret not in rendered
