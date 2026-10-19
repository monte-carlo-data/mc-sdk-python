# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0
"""Imports the installed pycarlo2 and builds a client, checking that it is the given version.

Run it with the interpreter it should check, outside the checkout or with -I, so the source tree
can't shadow the installed package:  python -I .github/scripts/smoke.py 0.1.4
"""

import sys
import tempfile

import pycarlo2


def main(version: str) -> None:
    assert pycarlo2.__version__ == version, pycarlo2.__version__
    with tempfile.TemporaryDirectory() as config_dir:
        client = pycarlo2.new_client(
            pycarlo2.Options(token_id="smoke", token_secret="smoke", config_dir=config_dir)
        )
    assert client.user_agent.startswith(f"mc-sdk-python/{version} "), client.user_agent
    print(f"pycarlo2 {version} installs and builds a client.")


if __name__ == "__main__":
    main(sys.argv[1])
