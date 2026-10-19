#!/usr/bin/env bash
# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0
#
# Builds the wheel and sdist into a clean dist/ the way the release does, stamped with <version>
# when one is given, and checks them. Then installs the wheel into a clean venv and builds a
# client, so a broken package fails before anything is published.
#
#   .github/scripts/build-dist.sh 0.1.4
set -euo pipefail

if [ $# -gt 0 ]; then
  .github/scripts/stamp-version.sh "$1"
fi
version=$(python3 -c 'import tomllib; print(tomllib.load(open("pyproject.toml", "rb"))["project"]["version"])')

rm -rf dist
uv build
.github/scripts/check-dist.sh dist "$version"
# Frozen: the lock records the project as 0.0.0 even when the build is stamped.
uv run --frozen --no-dev --group release twine check --strict dist/*

venv=$(mktemp -d)
trap 'rm -rf "$venv"' EXIT
uv venv --quiet "$venv"
uv pip install --quiet --python "$venv/bin/python" "dist/pycarlo2-$version-py3-none-any.whl"
"$venv/bin/python" -I .github/scripts/smoke.py "$version"
