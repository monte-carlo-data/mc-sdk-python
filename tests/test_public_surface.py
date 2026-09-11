"""Compiles the public surface the way a consumer does: one import, one name.

A rename of `new_client`, `Options` or `CredentialsError`, or a generator upgrade that drops
the `__init__` override re-exporting them, fails here rather than in a downstream repository.
"""

from __future__ import annotations

from pathlib import Path

import montecarlo


def test_the_package_exports_client_construction_beside_the_generated_surface(
    isolate: Path,
) -> None:
    assert "Options" in montecarlo.__all__
    assert "new_client" in montecarlo.__all__
    assert "CredentialsError" in montecarlo.__all__
    assert montecarlo.CredentialsError is montecarlo.auth.CredentialsError
    assert "UsersApi" in montecarlo.__all__
    assert "CurrentUserOut" in montecarlo.__all__

    client = montecarlo.new_client(
        montecarlo.Options(
            endpoint="https://api.getmontecarlo.com",
            token_id="id",
            token_secret="secret",
            config_dir=isolate,
        )
    )
    assert isinstance(client, montecarlo.ApiClient)
    assert isinstance(montecarlo.UsersApi(client), montecarlo.UsersApi)


def test_the_generated_configuration_alone_points_nowhere_useful() -> None:
    """Why `new_client` exists: the spec declares no server, so the generated host is empty."""
    assert montecarlo.Configuration().host == ""
