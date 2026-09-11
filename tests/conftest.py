"""Fixtures shared by the hand-written surface's tests.

`isolate` keeps a test from reading the developer's real credentials. `fake_api` is the
loopback HTTP server that stands in for the API and its token endpoint; the boundaries of the
hand-written code are the filesystem and HTTP, so both are exercised for real rather than
mocked.
"""

from __future__ import annotations

import json
import threading
from collections.abc import Iterator
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs

import pytest

from montecarlo.profile import ENVIRONMENT_KEYS, PROFILE_FILE_NAME

CURRENT_USER = {
    "account_frozen": False,
    "account_id": "00000000-0000-4000-8000-000000000001",
    "email": "user@example.com",
    "identity_type": "user",
    "user_id": "u1",
}

DEPLOYMENT = {
    "aws_external_id": None,
    "created_time": None,
    "enabled": True,
    "id": "00000000-0000-4000-8000-000000000002",
    "last_updated_time": None,
    "name": "prod",
    "runtime_platform": "AWS",
    "type": "COLLECTION_AGENT",
}

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


@pytest.fixture
def isolate(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> Path:
    """Clear every environment variable resolution consults and return a config directory.

    Pass the directory as `Options.config_dir`; that is what makes a test's file-backed
    lookups land here rather than in the real ~/.mcd. As a backstop for a call site that
    forgets, HOME is pointed at the same directory with an empty `.mcd` under it.
    """
    for key in ENVIRONMENT_KEYS:
        monkeypatch.delenv(key, raising=False)
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("USERPROFILE", str(tmp_path))
    (tmp_path / ".mcd").mkdir()
    return tmp_path


@dataclass
class Request:
    method: str
    path: str
    headers: list[tuple[str, str]]
    form: dict[str, list[str]]
    body: str


@dataclass
class FakeApi:
    """A loopback server. `/oauth2/token` answers with the next `token_responses` entry (or a
    fresh token); every other path answers 200 with `api_response`, `CURRENT_USER` by default.
    Every request is recorded, body included.

    `token_responses` is consumed one per token request as `(status, body)`; when it runs
    out, the server answers with a fresh `oauth-access-token`. `body` is usually a dict or
    list, sent as JSON; a `(301|302|307|308, {"Location": url})` pair sends that status with a
    `Location` header and an empty body instead, and a `str` body is sent verbatim with a
    `text/html` content type, to exercise a redirect or a non-JSON response.

    When `redirect_api_to` is set, every API path other than `/collector` answers 307 with
    that Location; `/collector` answers 200 with `api_response`, so a test can assert whether
    the client followed the redirect there.
    """

    url: str
    requests: list[Request] = field(default_factory=list)
    token_responses: list[tuple[int, dict | list | str]] = field(default_factory=list)
    api_response: dict | list = field(default_factory=lambda: CURRENT_USER)
    redirect_api_to: str = ""

    def token_requests(self) -> list[Request]:
        return [r for r in self.requests if r.path == "/oauth2/token"]

    def api_requests(self) -> list[Request]:
        return [r for r in self.requests if r.path != "/oauth2/token"]

    def requests_for(self, path: str) -> list[Request]:
        return [r for r in self.requests if r.path == path]


@pytest.fixture
def fake_api() -> Iterator[FakeApi]:
    state = FakeApi(url="")

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, format: str, *args: object) -> None:
            pass

        def _record(self) -> Request:
            length = int(self.headers.get("Content-Length") or 0)
            body = self.rfile.read(length).decode() if length else ""
            request = Request(
                method=self.command,
                path=self.path,
                headers=[(k, v) for k, v in self.headers.items()],
                form=parse_qs(body),
                body=body,
            )
            state.requests.append(request)
            return request

        def _reply(self, status: int, payload: dict | list) -> None:
            data = json.dumps(payload).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def _redirect(self, status: int, location: str) -> None:
            self.send_response(status)
            self.send_header("Location", location)
            self.send_header("Content-Length", "0")
            self.end_headers()

        def _reply_raw(self, status: int, text: str) -> None:
            data = text.encode()
            self.send_response(status)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def _reply_token(self) -> None:
            if state.token_responses:
                status, payload = state.token_responses.pop(0)
            else:
                status, payload = 200, {"access_token": "oauth-access-token", "expires_in": 3600}
            if isinstance(payload, str):
                self._reply_raw(status, payload)
            elif (
                isinstance(payload, dict)
                and "Location" in payload
                and status
                in (
                    301,
                    302,
                    307,
                    308,
                )
            ):
                self._redirect(status, payload["Location"])
            else:
                self._reply(status, payload)

        def do_GET(self) -> None:
            self._record()
            if state.redirect_api_to and self.path != "/collector":
                self._redirect(307, state.redirect_api_to)
            else:
                self._reply(200, state.api_response)

        def do_POST(self) -> None:
            request = self._record()
            if request.path == "/oauth2/token":
                self._reply_token()
            elif state.redirect_api_to and self.path != "/collector":
                self._redirect(307, state.redirect_api_to)
            else:
                self._reply(200, state.api_response)

        def do_PATCH(self) -> None:
            self._record()
            if state.redirect_api_to and self.path != "/collector":
                self._redirect(307, state.redirect_api_to)
            else:
                self._reply(200, state.api_response)

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    state.url = f"http://127.0.0.1:{server.server_port}"
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield state
    finally:
        server.shutdown()
        server.server_close()
