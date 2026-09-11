from __future__ import annotations

from pathlib import Path

import pytest

from montecarlo import profile as profile_module
from montecarlo.auth import CredentialsError, Options
from montecarlo.profile import config_dir, load_profile, parse_ini
from tests.conftest import write_profiles


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


def test_load_profile_strips_the_graphql_suffix_from_the_api_endpoint(isolate: Path) -> None:
    """Every other Monte Carlo tool stores the GraphQL URL under mcd_api_endpoint."""
    write_profiles(isolate, "[default]\nmcd_api_endpoint = https://api.example.com/graphql\n")
    profile = load_profile("", isolate)
    assert profile.endpoint == "https://api.example.com"
    assert Options(endpoint=profile.endpoint).resolved_token_url() == (
        "https://api.example.com/oauth2/token"
    )


def test_parse_errors_do_not_echo_the_offending_line(tmp_path: Path) -> None:
    """Callers render these errors verbatim into unredacted surfaces."""
    secret = "not-a-real-token-only-a-fixture"
    path = write_profiles(tmp_path, f"mcd_token = {secret}\n")
    with pytest.raises(CredentialsError) as info:
        parse_ini(path)
    assert secret not in str(info.value)
    assert info.value.__cause__ is None and info.value.__suppress_context__


def _no_home() -> None:
    raise RuntimeError("no home")


def test_a_missing_home_directory_is_a_credentials_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(profile_module.Path, "home", classmethod(lambda cls: _no_home()))
    with pytest.raises(CredentialsError, match="home directory"):
        config_dir()
