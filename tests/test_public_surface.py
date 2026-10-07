# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0

"""Compiles the public surface the way a consumer does: one import, one name.

A rename of `new_client`, `Options` or `CredentialsError`, or a generator upgrade that drops
the `__init__` override re-exporting them, fails here rather than in a downstream repository.
"""

from __future__ import annotations

from pathlib import Path

import pycarlo2
from pycarlo2 import auth


def test_the_package_exports_client_construction_beside_the_generated_surface(
    isolate: Path,
) -> None:
    assert "Options" in pycarlo2.__all__
    assert "new_client" in pycarlo2.__all__
    assert "CredentialsError" in pycarlo2.__all__
    assert pycarlo2.CredentialsError is auth.CredentialsError
    assert "UsersApi" in pycarlo2.__all__
    assert "CurrentUserOut" in pycarlo2.__all__

    client = pycarlo2.new_client(
        pycarlo2.Options(
            endpoint="https://api.getmontecarlo.com",
            token_id="id",
            token_secret="secret",
            config_dir=isolate,
        )
    )
    assert isinstance(client, pycarlo2.ApiClient)
    assert isinstance(pycarlo2.UsersApi(client), pycarlo2.UsersApi)


def test_the_generated_configuration_alone_points_nowhere_useful() -> None:
    """Why `new_client` exists: the spec declares no server, so the generated host is empty."""
    assert pycarlo2.Configuration().host == ""
