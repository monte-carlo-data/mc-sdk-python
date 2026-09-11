# Hand-written, not generator output.
"""OAuth 2.0 client credentials: scopes, the token exchange, and a self-refreshing token.

`TokenSource` validates its own inputs at construction, so a caller that builds one directly
gets the same checks `Options.validate()` runs. The token request follows no redirects: a 3xx
is reported as a failed status rather than resent, since a redirect would carry the client
secret to whatever host the `Location` header names. A `token()` call can block for the retry
policy's worst case (about 45 seconds) while it holds the internal lock, so other threads
calling `token()` concurrently wait that long too.
"""

from __future__ import annotations

import ipaddress
import json
import re
import threading
import time
from collections.abc import Callable
from urllib.parse import urlparse

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
DEFAULT_EXPIRES_IN_SECONDS = 3600

# Every attempt is bounded as a whole, not just per phase, so the lock in TokenSource.token
# is never held longer than TOKEN_REQUEST_ATTEMPTS * TOKEN_REQUEST_TIMEOUT_SECONDS plus
# backoff (about 45 seconds worst case) while other threads wait for a token.
TOKEN_REQUEST_TIMEOUT_SECONDS = 10.0
TOKEN_REQUEST_TIMEOUT = urllib3.Timeout(
    connect=5.0, read=TOKEN_REQUEST_TIMEOUT_SECONDS, total=TOKEN_REQUEST_TIMEOUT_SECONDS
)
# Retried on connection failures and 5xx, never on 4xx: a rejected credential does not
# improve with retrying. redirect=0: a redirect would re-send the client secret in the form
# body to whatever host the Location header names, which the https check on token_url
# cannot see; a 3xx is reported as a failed status instead.
TOKEN_REQUEST_RETRIES = urllib3.Retry(
    total=3,
    redirect=0,
    raise_on_redirect=False,
    backoff_factor=0.5,
    status_forcelist=(500, 502, 503, 504),
    allowed_methods=frozenset({"POST"}),
    raise_on_status=False,
)


def scopes_for_instance(instance: str) -> list[str]:
    """The OAuth scopes for an instance id such as `us1`: the access scope, then the instance's."""
    return [ACCESS_SCOPE, INSTANCE_SCOPE_PREFIX + instance]


def validate_instance_id(instance: str) -> None:
    if not INSTANCE_ID_PATTERN.fullmatch(instance):
        raise CredentialsError(f"invalid instance id {instance!r}; expected an identifier like us1")


def validate_url(raw: str, name: str) -> None:
    """Require an absolute https URL; http is allowed only for a loopback host, for tests."""
    parsed = urlparse(raw)
    if not parsed.scheme or not parsed.netloc:
        raise CredentialsError(f"{name} must be an absolute URL: {raw!r}")
    if parsed.scheme == "https":
        return
    if parsed.scheme == "http" and _is_loopback(parsed.hostname):
        return
    raise CredentialsError(
        f"{name} must use https (http is allowed only for a loopback host): {raw!r}"
    )


def _is_loopback(host: str | None) -> bool:
    """True for `localhost` or any loopback IP literal (`127.0.0.1`, `::1`, ...)."""
    if host == "localhost":
        return True
    if host is None:
        return False
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


class TokenSource:
    """Exchanges client credentials for an access token and renews it as needed.

    `token()` returns a cached token until shortly before it expires, then fetches a new one.
    It is safe to call from several threads. The token request is retried on connection
    failures and 5xx responses, never on 4xx: a rejected credential does not improve with
    retrying, and it never follows redirects.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        instance: str,
        token_url: str,
        *,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        """Validate `instance` and `token_url`, the same checks `Options.validate()` runs.

        A `TokenSource` built directly, without going through `Options`, therefore still
        rejects a bad instance id or an insecure token URL at construction.

        `clock` is the monotonic clock expiry is measured against; tests inject a fake.
        """
        validate_instance_id(instance)
        validate_url(token_url, "token url")
        self._client_id = client_id
        self._client_secret = client_secret
        self._scope = " ".join(scopes_for_instance(instance))
        self._token_url = token_url
        self._http = urllib3.PoolManager()
        self._clock = clock
        self._lock = threading.Lock()
        self._token = ""
        self._expires_at = 0.0

    def token(self) -> str:
        with self._lock:
            if not self._token or self._clock() >= self._expires_at:
                self._token, self._expires_at = self._request()
            return self._token

    def _request(self) -> tuple[str, float]:
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
                timeout=TOKEN_REQUEST_TIMEOUT,
                retries=TOKEN_REQUEST_RETRIES,
            )
        except urllib3.exceptions.HTTPError as exc:
            raise CredentialsError(f"token request to {self._token_url} failed: {exc}") from exc
        if response.status != 200:
            body = response.data.decode(errors="replace")[:200]
            raise CredentialsError(
                f"token request to {self._token_url} failed with status {response.status}: {body}"
            )

        try:
            payload = json.loads(response.data)
        except ValueError:
            raise CredentialsError(f"token response from {self._token_url} is not JSON") from None
        if not isinstance(payload, dict):
            raise CredentialsError(f"token response from {self._token_url} is not a JSON object")
        access_token = payload.get("access_token")
        if not isinstance(access_token, str) or not access_token:
            raise CredentialsError(f"token response from {self._token_url} carries no access_token")
        try:
            expires_in = int(payload.get("expires_in", DEFAULT_EXPIRES_IN_SECONDS))
        except (TypeError, ValueError):
            expires_in = DEFAULT_EXPIRES_IN_SECONDS
        # A token shorter than twice the skew is still cached for half its life instead of
        # being refetched on every call.
        skew = min(TOKEN_EXPIRY_SKEW_SECONDS, expires_in / 2)
        expires_at = self._clock() + max(0.0, expires_in - skew)
        return access_token, expires_at
