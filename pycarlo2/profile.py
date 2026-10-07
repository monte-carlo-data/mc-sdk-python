# Hand-written, not generator output.
# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0
"""The credentials file every Monte Carlo tool shares, and the environment variable names that
can stand in for it.

This module owns the credentials file and the names of the environment variables; the
three-tier resolution itself — options, then environment, then this file — is `Options.resolve`
in `auth.py`. `~/.mcd/profiles.ini` is written by the Monte Carlo CLI and read by pycarlo and
mc-sdk-go, so this module reads the same file, the same section names and the same keys. Most
keys mean the same thing here; `mcd_api_endpoint` is reinterpreted, see `strip_graphql_path`.
"""

from __future__ import annotations

import configparser
import os
from dataclasses import dataclass, field
from pathlib import Path

PROFILE_FILE_NAME = "profiles.ini"
DEFAULT_PROFILE_NAME = "default"
CONFIG_DIR_NAME = ".mcd"

# Keys as the CLI writes them, and as pycarlo reads them.
KEY_ID = "mcd_id"
KEY_TOKEN = "mcd_token"
KEY_API_ENDPOINT = "mcd_api_endpoint"
KEY_OAUTH_CLIENT_ID = "mcd_oauth_client_id"
KEY_OAUTH_CLIENT_SECRET = "mcd_oauth_client_secret"
KEY_TOKEN_ENDPOINT = "mcd_token_endpoint"
KEY_INSTANCE_ID = "mcd_instance_id"

# Environment variables this package reads, named as every other Monte Carlo tool names them.
ENV_PROFILE = "MCD_DEFAULT_PROFILE"
ENV_TOKEN_ID = "MCD_DEFAULT_API_ID"
ENV_TOKEN_SECRET = "MCD_DEFAULT_API_TOKEN"
ENV_CLIENT_ID = "MCD_DEFAULT_OAUTH_CLIENT_ID"
ENV_CLIENT_SECRET = "MCD_DEFAULT_OAUTH_CLIENT_SECRET"
ENV_INSTANCE = "MCD_DEFAULT_INSTANCE_ID"

# Every name above, so a test can isolate itself from the developer's environment by ranging
# over this rather than restating the list. A variable added above must be added here.
ENVIRONMENT_KEYS = (
    ENV_PROFILE,
    ENV_TOKEN_ID,
    ENV_TOKEN_SECRET,
    ENV_CLIENT_ID,
    ENV_CLIENT_SECRET,
    ENV_INSTANCE,
)


class CredentialsError(Exception):
    """Credentials could not be resolved, read or validated.

    Raised at construction rather than as a 401 on the first call. The message never carries a
    credential or a line of the credentials file.
    """


@dataclass
class Profile:
    """One section of the credentials file, with the keys this SDK reads."""

    endpoint: str = ""
    token_url: str = ""
    instance: str = ""
    token_id: str = ""
    token_secret: str = field(default="", repr=False)
    client_id: str = ""
    client_secret: str = field(default="", repr=False)


def config_dir() -> Path:
    """The default directory holding the credentials file, `~/.mcd`."""
    try:
        home = Path.home()
    except RuntimeError:
        raise CredentialsError("no home directory to look for .mcd under") from None
    return home / CONFIG_DIR_NAME


def strip_graphql_path(endpoint: str) -> str:
    """Derive the REST base URL from a `mcd_api_endpoint` value.

    That key holds the GraphQL URL in every other Monte Carlo tool, while REST operations live
    under `/api/v2/...` on the bare host, so a trailing `/graphql` is removed.
    """
    endpoint = endpoint.rstrip("/")
    return endpoint.removesuffix("/graphql")


def parse_ini(path: Path) -> dict[str, dict[str, str]]:
    """Read the credentials file into `{section: {key: value}}`, keys lower-cased.

    A missing file propagates as `FileNotFoundError` so a caller can tell absence from damage;
    any other read failure, or an unparseable file, is a `CredentialsError` naming the path and
    nothing else.
    """
    try:
        text = path.read_text()
    except FileNotFoundError:
        raise
    except (OSError, UnicodeDecodeError):
        # `from None`: the chained message could carry the path's internals or a line of the file.
        raise CredentialsError(f"{path}: cannot be read") from None
    parser = configparser.ConfigParser(interpolation=None)
    try:
        parser.read_string(text, source=str(path))
    except configparser.Error:
        # `from None`: the chained exception's message would echo the offending line.
        raise CredentialsError(f"{path}: not a valid profiles file") from None
    return {name: dict(parser[name]) for name in parser.sections()}


def load_profile(name: str = "", directory: str | os.PathLike[str] | None = None) -> Profile:
    """Read one profile's credentials.

    An empty name resolves to `MCD_DEFAULT_PROFILE`, then to `default`. A `None` or empty-string
    directory resolves to `~/.mcd`. A named profile missing from the file is an error: a caller
    that asked for specific credentials should hear that they are missing rather than silently get
    someone else's.

    Within a profile, OAuth client credentials take precedence over an API token, as in pycarlo.
    Half of either pair is a configuration error, not a fall-through to the other mechanism.
    """
    name = name or os.environ.get(ENV_PROFILE, "") or DEFAULT_PROFILE_NAME
    if directory is None or os.fspath(directory) == "":
        path = config_dir() / PROFILE_FILE_NAME
    else:
        path = Path(directory) / PROFILE_FILE_NAME
    sections = parse_ini(path)
    values = sections.get(name)
    if values is None:
        raise CredentialsError(f"profile {name!r} not found in {path}")

    profile = Profile(
        endpoint=strip_graphql_path(values.get(KEY_API_ENDPOINT, "")),
        token_url=values.get(KEY_TOKEN_ENDPOINT, ""),
        instance=values.get(KEY_INSTANCE_ID, ""),
    )
    client_id = values.get(KEY_OAUTH_CLIENT_ID, "")
    client_secret = values.get(KEY_OAUTH_CLIENT_SECRET, "")
    token_id = values.get(KEY_ID, "")
    token_secret = values.get(KEY_TOKEN, "")

    def half_set(present: str, missing: str) -> CredentialsError:
        return CredentialsError(f"profile {name!r} in {path} has {present} but not {missing}")

    if client_id and client_secret:
        profile.client_id, profile.client_secret = client_id, client_secret
    elif client_id:
        raise half_set(KEY_OAUTH_CLIENT_ID, KEY_OAUTH_CLIENT_SECRET)
    elif client_secret:
        raise half_set(KEY_OAUTH_CLIENT_SECRET, KEY_OAUTH_CLIENT_ID)
    elif token_id and token_secret:
        profile.token_id, profile.token_secret = token_id, token_secret
    elif token_id:
        raise half_set(KEY_ID, KEY_TOKEN)
    elif token_secret:
        raise half_set(KEY_TOKEN, KEY_ID)
    return profile
