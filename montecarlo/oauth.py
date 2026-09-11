# Hand-written, not generator output.
"""OAuth 2.0 client credentials: scopes, the token exchange, and a self-refreshing token."""

from __future__ import annotations

import json
import re
import threading
import time

import urllib3

from montecarlo.profile import CredentialsError

# Granted to every machine-to-machine client.
ACCESS_SCOPE = "https://api.getmontecarlo.com/access"
# Joined with an instance id, the scope the gateway routes on.
INSTANCE_SCOPE_PREFIX = "https://instance.getmontecarlo.com/"

# Instance ids are short DNS-safe identifiers such as `us1`; this is the gateway's own rule, so
# the SDK never requests a scope the gateway would reject.
INSTANCE_ID_PATTERN = re.compile(r"^[A-Za-z0-9-]{1,63}$")

# A token is renewed this long before its stated expiry, so one never expires mid-request.
TOKEN_EXPIRY_SKEW_SECONDS = 60.0
TOKEN_REQUEST_TIMEOUT_SECONDS = 10.0
DEFAULT_EXPIRES_IN_SECONDS = 3600


def scopes_for_instance(instance: str) -> list[str]:
    """The OAuth scopes for an instance id such as `us1`: the access scope, then the instance's."""
    return [ACCESS_SCOPE, INSTANCE_SCOPE_PREFIX + instance]


def validate_instance_id(instance: str) -> None:
    if not INSTANCE_ID_PATTERN.fullmatch(instance):
        raise CredentialsError(f"invalid instance id {instance!r}; expected an identifier like us1")


class TokenSource:
    """Exchanges client credentials for an access token and renews it as needed.

    `token()` returns a cached token until shortly before it expires, then fetches a new one.
    It is safe to call from several threads. The token request is retried on connection
    failures and 5xx responses, never on 4xx: a rejected credential does not improve with
    retrying.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        instance: str,
        token_url: str,
        http: urllib3.PoolManager | None = None,
    ) -> None:
        self._client_id = client_id
        self._client_secret = client_secret
        self._scope = " ".join(scopes_for_instance(instance))
        self._token_url = token_url
        self._http = http or urllib3.PoolManager()
        self._lock = threading.Lock()
        self._token = ""
        self._expires_at = 0.0

    def token(self) -> str:
        with self._lock:
            if not self._token or time.monotonic() >= self._expires_at:
                self._token, self._expires_at = self._request()
            return self._token

    def _request(self) -> tuple[str, float]:
        retries = urllib3.Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=(500, 502, 503, 504),
            allowed_methods=frozenset({"POST"}),
            raise_on_status=False,
        )
        try:
            response = self._http.request(
                "POST",
                self._token_url,
                fields={
                    "grant_type": "client_credentials",
                    "client_id": self._client_id,
                    "client_secret": self._client_secret,
                    "scope": self._scope,
                },
                encode_multipart=False,
                headers={"Accept": "application/json"},
                timeout=TOKEN_REQUEST_TIMEOUT_SECONDS,
                retries=retries,
            )
        except urllib3.exceptions.HTTPError as exc:
            raise CredentialsError(f"token request to {self._token_url} failed: {exc}") from exc
        if response.status != 200:
            body = response.data.decode(errors="replace")[:200]
            raise CredentialsError(
                f"token request to {self._token_url} failed with status {response.status}: {body}"
            )

        payload = json.loads(response.data)
        access_token = payload.get("access_token")
        if not isinstance(access_token, str) or not access_token:
            raise CredentialsError(f"token response from {self._token_url} carries no access_token")
        try:
            expires_in = int(payload.get("expires_in", DEFAULT_EXPIRES_IN_SECONDS))
        except (TypeError, ValueError):
            expires_in = DEFAULT_EXPIRES_IN_SECONDS
        expires_at = time.monotonic() + max(0.0, expires_in - TOKEN_EXPIRY_SKEW_SECONDS)
        return access_token, expires_at
