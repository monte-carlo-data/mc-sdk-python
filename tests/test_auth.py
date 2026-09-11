from __future__ import annotations

import json
from pathlib import Path
from uuid import UUID

import pytest

from montecarlo import DeploymentsApi, UsersApi, __version__
from montecarlo.auth import CredentialsError, Options, new_client
from montecarlo.models.deployment_patch import DeploymentPatch
from montecarlo.profile import PROFILE_FILE_NAME, config_dir
from tests.conftest import DEPLOYMENT, FakeApi, write_profiles

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
    "kwargs",
    [
        {"token_id": "id", "token_secret": "secret"},
        {"client_id": "id", "client_secret": "secret", "instance": "us1"},
        {"token": "access-token"},
    ],
    ids=["api token", "oauth client credentials", "pre-obtained bearer"],
)
def test_validate_accepts_each_complete_mechanism(kwargs: dict[str, str]) -> None:
    Options(endpoint=HTTPS, **kwargs).validate()


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


@pytest.mark.parametrize(
    ("kwargs", "want"),
    [
        ({"token_id": "key-id", "token_secret": "s3cret"}, "Bearer key-id:s3cret"),
        ({"token": "pre-obtained"}, "Bearer pre-obtained"),
        (
            {"token_id": "key-id", "token_secret": "s3cret", "token": "pre-obtained"},
            "Bearer key-id:s3cret",
        ),
    ],
    ids=["api token", "pre-obtained bearer", "api token wins over pre-obtained bearer"],
)
def test_a_static_credential_goes_out_as_the_bearer_and_asks_for_no_token(
    isolate: Path, fake_api: FakeApi, kwargs: dict[str, str], want: str
) -> None:
    client = new_client(Options(endpoint=fake_api.url, config_dir=isolate, **kwargs))
    UsersApi(client).get_current_user()

    (request,) = fake_api.api_requests()
    authorization = [v for k, v in request.headers if k.lower() == "authorization"]
    assert authorization == [want]
    assert fake_api.token_requests() == []
    assert request.path == "/api/v2/users/me"


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
    """Without this the first call dies inside urllib3 with "No host specified", not here."""
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
        ("http://[::1]:1", True),
        ("http://127.0.0.2:1", True),
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
    authorization = [v for k, v in request.headers if k.lower() == "authorization"]
    assert authorization == ["Bearer delegated-token"]


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
        client = new_client(options)
        configuration = client.configuration
        assert configuration.access_token is None
        # `default_headers` is where the generated client keeps per-request headers, the place
        # Go's `DefaultHeader` bug lived; a credential must not be there either.
        rendered = (
            repr(vars(configuration))
            + configuration.to_debug_report()
            + repr(client.default_headers)
        )
        assert "leaked" not in rendered


def test_resolve_prefers_explicit_options_over_everything(
    isolate: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    write_profiles(isolate)
    monkeypatch.setenv("MCD_DEFAULT_API_ID", "env-id")
    monkeypatch.setenv("MCD_DEFAULT_API_TOKEN", "env-secret")

    resolved = Options(
        endpoint="https://explicit.example.com",
        token_id="explicit-id",
        token_secret="explicit-secret",
        config_dir=isolate,
    ).resolve()

    assert resolved.token_id == "explicit-id"
    assert resolved.endpoint == "https://explicit.example.com"


def test_resolve_prefers_environment_over_profile(
    isolate: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The endpoint still comes from the profile: MCD_API_ENDPOINT is deliberately not read,
    since in the CLI and pycarlo it carries the GraphQL endpoint, not the REST base URL."""
    write_profiles(isolate)
    monkeypatch.setenv("MCD_DEFAULT_API_ID", "env-id")
    monkeypatch.setenv("MCD_DEFAULT_API_TOKEN", "env-secret")
    monkeypatch.setenv("MCD_API_ENDPOINT", "https://ignored.example.com/graphql")

    resolved = Options(config_dir=isolate).resolve()

    assert resolved.token_id == "env-id"
    assert resolved.endpoint == "https://api.example.com"


def test_resolve_reads_oauth_client_credentials_and_the_instance_from_the_environment(
    isolate: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("MCD_DEFAULT_OAUTH_CLIENT_ID", "env-client-id")
    monkeypatch.setenv("MCD_DEFAULT_OAUTH_CLIENT_SECRET", "env-client-secret")
    monkeypatch.setenv("MCD_DEFAULT_INSTANCE_ID", "eu1")

    resolved = Options(endpoint=HTTPS, config_dir=isolate).resolve()
    resolved.validate()

    assert resolved.uses_oauth()
    assert resolved.client_id == "env-client-id"
    assert resolved.instance == "eu1"


def test_resolve_falls_back_to_the_profile(isolate: Path) -> None:
    write_profiles(isolate)
    resolved = Options(config_dir=isolate).resolve()
    assert (resolved.token_id, resolved.endpoint) == ("default-id", "https://api.example.com")


def test_resolve_tolerates_a_missing_file(isolate: Path) -> None:
    """A caller passing its own credentials should not need a credentials file to exist."""
    resolved = Options(
        endpoint="https://api.example.com", token_id="id", token_secret="secret", config_dir=isolate
    ).resolve()
    assert resolved.token_id == "id"


def test_resolve_fails_when_a_named_profile_is_missing(isolate: Path) -> None:
    """A profile asked for by name has to exist, even when the file does not."""
    with pytest.raises(CredentialsError, match="profile 'nope' not found"):
        Options(profile="nope", config_dir=isolate).resolve()


def test_an_ambient_oauth_environment_does_not_displace_an_explicit_api_token(
    isolate: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Resolution is mechanism-wise: a complete explicit mechanism is never layered over."""
    monkeypatch.setenv("MCD_DEFAULT_OAUTH_CLIENT_ID", "env-client-id")
    monkeypatch.setenv("MCD_DEFAULT_OAUTH_CLIENT_SECRET", "env-client-secret")
    monkeypatch.setenv("MCD_DEFAULT_INSTANCE_ID", "us1")

    resolved = Options(
        endpoint="https://api.example.com",
        token_id="explicit-id",
        token_secret="explicit-secret",
        config_dir=isolate,
    ).resolve()

    assert not resolved.uses_oauth()
    assert resolved.bearer() == "explicit-id:explicit-secret"
    assert resolved.instance == "us1"


def test_a_partial_ambient_oauth_environment_does_not_break_an_explicit_api_token(
    isolate: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("MCD_DEFAULT_OAUTH_CLIENT_ID", "env-client-id")

    resolved = Options(
        endpoint="https://api.example.com",
        token_id="explicit-id",
        token_secret="explicit-secret",
        config_dir=isolate,
    ).resolve()
    resolved.validate()


def test_resolve_surfaces_a_malformed_profiles_file_rather_than_swallowing_it(
    isolate: Path,
) -> None:
    """A real file this SDK cannot read is a different failure from no file at all."""
    write_profiles(isolate, "not an ini file\n[unclosed\n")
    with pytest.raises(CredentialsError, match="profiles.ini"):
        Options(endpoint="https://api.example.com", config_dir=isolate).resolve()


def test_an_ambient_default_profile_does_not_break_a_complete_explicit_configuration(
    isolate: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """MCD_DEFAULT_PROFILE selects a section; it does not by itself make a missing file fatal."""
    monkeypatch.setenv("MCD_DEFAULT_PROFILE", "default")

    resolved = Options(
        endpoint="https://api.example.com", token_id="id", token_secret="secret", config_dir=isolate
    ).resolve()

    assert (resolved.token_id, resolved.token_secret) == ("id", "secret")
    assert resolved.endpoint == "https://api.example.com"


def test_a_profile_supplies_the_instance_and_token_url_only_for_oauth(isolate: Path) -> None:
    write_profiles(
        isolate,
        "[default]\nmcd_oauth_client_id = c\nmcd_oauth_client_secret = s\n"
        "mcd_instance_id = eu1\nmcd_token_endpoint = https://login.example.com/token\n",
    )
    resolved = Options(endpoint="https://api.example.com", config_dir=isolate).resolve()
    assert (resolved.instance, resolved.token_url) == ("eu1", "https://login.example.com/token")

    resolved = Options(
        endpoint="https://api.example.com", token="explicit", config_dir=isolate, profile="default"
    ).resolve()
    assert (resolved.instance, resolved.token_url) == ("", "")


@pytest.mark.parametrize(
    ("profile_contents", "explicit", "match"),
    [
        (
            "[default]\nmcd_oauth_client_id = c\nmcd_oauth_client_secret = s\n"
            "mcd_instance_id = us1\n",
            {"token_id": "explicit-id"},
            "token id and token secret are both required",
        ),
        (
            "[default]\nmcd_id = id\nmcd_token = secret\n",
            {"client_id": "explicit"},
            "client id and client secret are both required",
        ),
    ],
)
def test_half_an_explicit_credential_pair_is_not_replaced_by_the_profile(
    isolate: Path, profile_contents: str, explicit: dict[str, str], match: str
) -> None:
    """`resolve` must treat a half-set explicit pair as a mechanism already chosen, not as
    `has_credentials() is False`; today it is silently overwritten by the profile instead."""
    write_profiles(isolate, profile_contents)
    with pytest.raises(CredentialsError, match=match):
        Options(endpoint="https://api.example.com", config_dir=isolate, **explicit).resolve()


def test_an_unreadable_profiles_file_is_a_credentials_error(isolate: Path) -> None:
    """`parse_ini` only wraps `configparser.Error`; a directory at the profiles path raises
    `IsADirectoryError`, an `OSError` that `resolve` does not catch alongside
    `FileNotFoundError`."""
    (isolate / PROFILE_FILE_NAME).mkdir()
    with pytest.raises(CredentialsError, match="profiles.ini"):
        Options(endpoint="https://api.example.com", config_dir=isolate).resolve()


def test_a_profile_under_the_default_home_directory_authenticates_a_client(
    isolate: Path, fake_api: FakeApi
) -> None:
    (isolate / ".mcd" / PROFILE_FILE_NAME).write_text(
        "[default]\nmcd_id = profile-id\nmcd_token = profile-secret\n"
    )
    assert config_dir() == isolate / ".mcd"

    UsersApi(new_client(Options(endpoint=fake_api.url))).get_current_user()

    (request,) = fake_api.api_requests()
    authorization = [v for k, v in request.headers if k.lower() == "authorization"]
    assert authorization == ["Bearer profile-id:profile-secret"]


def test_an_empty_string_config_dir_means_the_default_directory(isolate: Path) -> None:
    """An empty string means ~/.mcd; `Path("")` would be `Path(".")` by pathlib's rules and is
    not special-cased."""
    (isolate / ".mcd" / PROFILE_FILE_NAME).write_text(
        "[default]\nmcd_id = profile-id\nmcd_token = profile-secret\n"
    )
    resolved = Options(endpoint=HTTPS, config_dir="").resolve()
    assert (resolved.token_id, resolved.token_secret) == ("profile-id", "profile-secret")


def test_a_body_carrying_request_is_forwarded_intact(isolate: Path, fake_api: FakeApi) -> None:
    fake_api.api_response = DEPLOYMENT
    client = new_client(
        Options(endpoint=fake_api.url, token_id="id", token_secret="secret", config_dir=isolate)
    )
    DeploymentsApi(client).update_deployment(
        UUID("00000000-0000-4000-8000-000000000002"), DeploymentPatch(name="renamed")
    )

    (request,) = fake_api.requests_for("/api/v2/deployments/00000000-0000-4000-8000-000000000002")
    assert request.method == "PATCH"
    assert json.loads(request.body) == {"name": "renamed"}
    authorization = [v for k, v in request.headers if k.lower() == "authorization"]
    assert len(authorization) == 1
