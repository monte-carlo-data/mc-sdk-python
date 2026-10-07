# Hand-written, not generator output.
# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0
"""Client construction and credentials.

Build a client with `new_client`. Credentials resolve from the `Options` passed in, then from
the environment, then from the credentials file the Monte Carlo CLI writes, so a caller with
the CLI already configured can often pass an endpoint alone and get a working client. Do not
build one from the generated `ApiClient` or `Configuration` directly: the spec declares no
server, so their default host is empty and the first call fails inside urllib3 with
`No host specified` rather than reaching the API.

The API accepts exactly one credential mechanism per request, as an Authorization bearer
header: an OAuth 2.0 client-credentials access token, or a Monte Carlo API token. Neither the
API client nor the token exchange follows a redirect.
"""

from __future__ import annotations

import dataclasses
import os
import platform
from collections.abc import Callable
from dataclasses import dataclass, field

import urllib3

from pycarlo2 import profile as profiles
from pycarlo2.api_client import ApiClient
from pycarlo2.configuration import Configuration
from pycarlo2.oauth import TokenSource, validate_instance_id, validate_url
from pycarlo2.profile import CredentialsError

__all__ = ["CredentialsError", "Options", "new_client"]

# The API has one host, so a redirect is returned as the response rather than followed: the
# credential is attached to every request, and a 307 or 308 would carry it and the body to
# whatever host the Location header names. total=3 keeps urllib3's default connection retries.
API_REQUEST_RETRIES = urllib3.Retry(total=3, redirect=0, raise_on_redirect=False)


@dataclass
class Options:
    """The inputs for building an authenticated client.

    `endpoint` is always required, though it can come from a profile rather than the caller.
    Exactly one credential mechanism is expected. When more than one is supplied directly, OAuth
    client credentials win, then an API token, then a pre-obtained bearer; `resolve` documents
    how a mechanism supplied through the environment or a profile is chosen instead.

    Secrets are excluded from `repr` so an `Options` can be logged.
    """

    # The API base URL, e.g. https://api.getmontecarlo.com.
    endpoint: str = ""

    # The two halves of a Monte Carlo API token. They are supplied separately and combined into
    # the bearer credential here, so a caller never has to know the wire format.
    token_id: str = ""
    token_secret: str = field(default="", repr=False)

    # A bearer credential the caller already holds: an access token obtained elsewhere.
    token: str = field(default="", repr=False)

    # OAuth 2.0 client credentials. `instance` selects the deployment the gateway routes to and
    # is required with them.
    client_id: str = ""
    client_secret: str = field(default="", repr=False)
    instance: str = ""

    # Where client credentials are exchanged. Empty means `endpoint` + /oauth2/token.
    token_url: str = ""

    # A section of the credentials file the Monte Carlo CLI writes. Empty means
    # MCD_DEFAULT_PROFILE, then "default".
    profile: str = ""

    # The directory holding that file. Empty means ~/.mcd.
    config_dir: str | os.PathLike[str] | None = None

    # The User-Agent sent with every request. Empty means one identifying this SDK and the
    # Python it runs on.
    user_agent: str = ""

    def uses_oauth(self) -> bool:
        return bool(self.client_id and self.client_secret)

    def uses_api_token(self) -> bool:
        return bool(self.token_id and self.token_secret)

    def has_credentials(self) -> bool:
        return self.uses_oauth() or self.uses_api_token() or bool(self.token)

    def _check_pairs(self) -> None:
        """A half-set credential pair is a configuration error, never a fall-through."""
        if bool(self.client_id) != bool(self.client_secret):
            raise CredentialsError("client id and client secret are both required for OAuth")
        if bool(self.token_id) != bool(self.token_secret):
            raise CredentialsError("token id and token secret are both required for an API token")

    def validate(self) -> None:
        """Enforce each mechanism's contract, so a misconfiguration fails at construction."""
        if not self.endpoint:
            raise CredentialsError("endpoint is required")
        validate_url(self.endpoint, "endpoint")
        if self.token_url:
            validate_url(self.token_url, "token url")
        self._check_pairs()
        if self.uses_oauth():
            if not self.instance:
                raise CredentialsError(
                    "instance is required with OAuth client credentials, e.g. us1"
                )
            validate_instance_id(self.instance)
        if not self.has_credentials():
            raise CredentialsError(
                "no credentials: set client id and secret, token id and secret, or a token"
            )

    def base_url(self) -> str:
        return self.endpoint.rstrip("/")

    def resolved_token_url(self) -> str:
        return self.token_url or self.base_url() + "/oauth2/token"

    def bearer(self) -> str:
        """The static credential to send, for the mechanisms that produce one up front.

        Ignores OAuth entirely: `new_client` consults this only when there is no token source,
        so a stale static header can never ride along an OAuth-authenticated request.
        """
        if self.uses_api_token():
            return f"{self.token_id}:{self.token_secret}"
        return self.token

    def resolve(self) -> Options:
        """Fill in whatever is empty, from the environment and then from a profile.

        Resolution is per credential mechanism, not per field: a mechanism supplied completely
        here is used as-is, and the environment, then the profile, is consulted only to pick a
        mechanism when none is supplied. An ambient MCD_DEFAULT_OAUTH_* trio therefore cannot
        displace an explicit API token, and a half-set ambient variable cannot break a mechanism
        the caller never asked for. `instance` is filled from the environment unconditionally:
        it is a routing hint, not a credential.

        A half-set pair supplied here is an error before the environment or a profile is
        consulted; neither ever completes one.

        A profile is consulted when one is named, when no mechanism was found by then, or when
        the endpoint is still empty. `MCD_DEFAULT_PROFILE`, if set, only selects which section a
        consulted profile reads from; it does not by itself make a missing file an error. A
        profile named explicitly has to exist; otherwise a missing file means whatever was
        supplied stands on its own. A file that exists but cannot be read is always an error. A
        profile supplies `instance` and `token_url` only when OAuth is the selected mechanism.
        """
        self._check_pairs()
        out = dataclasses.replace(self)

        if not out.has_credentials():
            client_id = os.environ.get(profiles.ENV_CLIENT_ID, "")
            client_secret = os.environ.get(profiles.ENV_CLIENT_SECRET, "")
            token_id = os.environ.get(profiles.ENV_TOKEN_ID, "")
            token_secret = os.environ.get(profiles.ENV_TOKEN_SECRET, "")
            if client_id and client_secret:
                out.client_id, out.client_secret = client_id, client_secret
            elif token_id and token_secret:
                out.token_id, out.token_secret = token_id, token_secret
        out.instance = out.instance or os.environ.get(profiles.ENV_INSTANCE, "")

        named = bool(out.profile)
        has_credentials = out.has_credentials()
        if not named and has_credentials and out.endpoint:
            return out

        try:
            loaded = profiles.load_profile(out.profile, out.config_dir)
        except FileNotFoundError as exc:
            if named:
                raise CredentialsError(
                    f"profile {out.profile!r} not found: no profiles file at {exc.filename}"
                ) from None
            return out

        out.endpoint = out.endpoint or loaded.endpoint
        if not has_credentials:
            out.token_id, out.token_secret = loaded.token_id, loaded.token_secret
            out.client_id, out.client_secret = loaded.client_id, loaded.client_secret
        if out.uses_oauth():
            out.token_url = out.token_url or loaded.token_url
            out.instance = out.instance or loaded.instance
        return out


# pycarlo's header names.
_HEADER_TELEMETRY_REASON = "x-mcd-telemetry-reason"
_HEADER_TELEMETRY_SERVICE = "x-mcd-telemetry-service"


def default_user_agent() -> str:
    # Deferred: pycarlo2/__init__.py imports this module, so a module-level import would be a cycle.
    from pycarlo2 import __version__

    return f"mc-sdk-python/{__version__} (python/{platform.python_version()})"


class _AuthenticatedClient(ApiClient):
    """The generated client with a credential attached to every request.

    The credential is added as the request goes out rather than stored on the configuration,
    so an OAuth token is fetched and renewed on its own schedule, and a credential never
    reaches `Configuration`, which anything can log. A request that already carries an
    Authorization header, set through an operation's `_request_auth`, keeps it: a per-request
    credential wins cleanly instead of stacking into a second header.
    """

    def __init__(self, configuration: Configuration, credential: Callable[[], str]) -> None:
        super().__init__(configuration)
        self._credential = credential

    def call_api(self, method, url, header_params=None, *args, **kwargs):
        # The generated operations pass `param_serialize`'s tuple positionally; only the header
        # dict is touched here, so a changed tuple shape past it is forwarded unchanged.
        headers = dict(header_params or {})
        if not any(name.lower() == "authorization" for name in headers):
            headers["Authorization"] = f"Bearer {self._credential()}"
        return super().call_api(method, url, headers, *args, **kwargs)


def new_client(options: Options | None = None) -> ApiClient:
    """Build a client that authenticates every request.

    Anything `options` leaves empty is filled in from the environment and the credentials
    file; `Options.resolve` documents that order. Pass the result to any generated `*Api`
    class: `UsersApi(new_client(Options(endpoint=...)))`.
    """
    resolved = (options or Options()).resolve()
    resolved.validate()

    if resolved.uses_oauth():
        credential: Callable[[], str] = TokenSource(
            resolved.client_id,
            resolved.client_secret,
            resolved.instance,
            resolved.resolved_token_url(),
        ).token
    else:
        bearer = resolved.bearer()
        credential = lambda: bearer  # noqa: E731

    configuration = Configuration(host=resolved.base_url(), retries=API_REQUEST_RETRIES)
    client = _AuthenticatedClient(configuration, credential)
    client.user_agent = resolved.user_agent or default_user_agent()
    # The gateway drops User-Agent, so these are the only client identity usage telemetry sees.
    # A tool built on the SDK overrides them with `set_default_header`.
    client.set_default_header(_HEADER_TELEMETRY_REASON, "user")  # pycarlo's RequestReason.USER
    client.set_default_header(_HEADER_TELEMETRY_SERVICE, "mc-sdk-python")
    return client
