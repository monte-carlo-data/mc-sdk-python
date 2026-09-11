from __future__ import annotations

from pathlib import Path

import pytest

from montecarlo.auth import CredentialsError, Options
from montecarlo.profile import PROFILE_FILE_NAME, load_profile, parse_ini

# The file is written by the CLI and read by every Monte Carlo tool, so this is the layout it
# produces, including keys this SDK does not use.
SAMPLE_PROFILES = """
[default]
mcd_id = default-id
mcd_token = default-secret
mcd_api_endpoint = https://api.example.com
aws_profile = something-this-sdk-ignores

; a comment
[oauth-profile]
mcd_oauth_client_id = client-id
mcd_oauth_client_secret = client-secret
mcd_instance_id = eu1
mcd_id = ignored-when-oauth-is-present
mcd_token = also-ignored

[both-endpoints]
mcd_id = id
mcd_token = secret
mcd_api_endpoint = https://api.example.com
mcd_token_endpoint = https://login.example.com/token
"""


def write_profiles(directory: Path, contents: str = SAMPLE_PROFILES) -> Path:
    path = directory / PROFILE_FILE_NAME
    path.write_text(contents)
    return path


def test_load_profile_reads_the_default_section(isolate: Path) -> None:
    write_profiles(isolate)
    profile = load_profile("", isolate)
    assert (profile.token_id, profile.token_secret) == ("default-id", "default-secret")
    assert profile.endpoint == "https://api.example.com"


def test_load_profile_prefers_oauth_within_a_profile(isolate: Path) -> None:
    write_profiles(isolate)
    profile = load_profile("oauth-profile", isolate)
    assert (profile.client_id, profile.client_secret) == ("client-id", "client-secret")
    assert (profile.token_id, profile.token_secret) == ("", "")
    assert profile.instance == "eu1"


def test_load_profile_reads_the_token_endpoint(isolate: Path) -> None:
    write_profiles(isolate)
    assert load_profile("both-endpoints", isolate).token_url == "https://login.example.com/token"


def test_load_profile_fails_on_an_unknown_name(isolate: Path) -> None:
    """Silently getting different credentials would be worse than failing."""
    write_profiles(isolate)
    with pytest.raises(CredentialsError, match="profile 'nope' not found"):
        load_profile("nope", isolate)


@pytest.mark.parametrize(
    ("contents", "present", "missing"),
    [
        ("[default]\nmcd_oauth_client_id = x\n", "mcd_oauth_client_id", "mcd_oauth_client_secret"),
        (
            "[default]\nmcd_oauth_client_secret = x\n",
            "mcd_oauth_client_secret",
            "mcd_oauth_client_id",
        ),
        ("[default]\nmcd_id = x\n", "mcd_id", "mcd_token"),
        ("[default]\nmcd_token = x\n", "mcd_token", "mcd_id"),
    ],
)
def test_half_a_credential_pair_is_a_configuration_error(
    isolate: Path, contents: str, present: str, missing: str
) -> None:
    write_profiles(isolate, contents)
    with pytest.raises(CredentialsError, match=f"has {present} but not {missing}"):
        load_profile("", isolate)


def test_mcd_default_profile_selects_the_section(
    isolate: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    write_profiles(isolate)
    monkeypatch.setenv("MCD_DEFAULT_PROFILE", "oauth-profile")
    assert load_profile("", isolate).client_id == "client-id"


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


def test_load_profile_strips_the_graphql_suffix_from_the_api_endpoint(isolate: Path) -> None:
    """Every other Monte Carlo tool stores the GraphQL URL under mcd_api_endpoint."""
    write_profiles(isolate, "[default]\nmcd_api_endpoint = https://api.example.com/graphql\n")
    profile = load_profile("", isolate)
    assert profile.endpoint == "https://api.example.com"
    assert Options(endpoint=profile.endpoint).resolved_token_url() == (
        "https://api.example.com/oauth2/token"
    )


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


def test_parse_errors_do_not_echo_the_offending_line(tmp_path: Path) -> None:
    """Callers render these errors verbatim into unredacted surfaces."""
    secret = "not-a-real-token-only-a-fixture"
    path = write_profiles(tmp_path, f"mcd_token = {secret}\n")
    with pytest.raises(CredentialsError) as info:
        parse_ini(path)
    assert secret not in str(info.value)
    assert info.value.__cause__ is None and info.value.__suppress_context__
