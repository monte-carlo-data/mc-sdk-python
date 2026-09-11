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

from montecarlo.profile import ENVIRONMENT_KEYS

CURRENT_USER = {
    "account_frozen": False,
    "account_id": "00000000-0000-4000-8000-000000000001",
    "email": "user@example.com",
    "identity_type": "user",
    "user_id": "u1",
}


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


@dataclass
class FakeApi:
    """A loopback server answering `GET /api/v2/users/me` and `POST /oauth2/token`.

    `token_responses` is consumed one per token request as `(status, body)`; when it runs
    out, the server answers with a fresh `oauth-access-token`.
    """

    url: str
    requests: list[Request] = field(default_factory=list)
    token_responses: list[tuple[int, dict]] = field(default_factory=list)

    def token_requests(self) -> list[Request]:
        return [r for r in self.requests if r.path == "/oauth2/token"]

    def api_requests(self) -> list[Request]:
        return [r for r in self.requests if r.path != "/oauth2/token"]


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
            )
            state.requests.append(request)
            return request

        def _reply(self, status: int, payload: dict) -> None:
            data = json.dumps(payload).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self) -> None:
            self._record()
            self._reply(200, CURRENT_USER)

        def do_POST(self) -> None:
            self._record()
            if state.token_responses:
                status, payload = state.token_responses.pop(0)
            else:
                status, payload = 200, {"access_token": "oauth-access-token", "expires_in": 3600}
            self._reply(status, payload)

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    state.url = f"http://127.0.0.1:{server.server_port}"
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield state
    finally:
        server.shutdown()
        server.server_close()
