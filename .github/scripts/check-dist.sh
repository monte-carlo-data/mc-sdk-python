#!/usr/bin/env bash
# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0
#
# Checks what `uv build` wrote to <dist> before it is published: one wheel and one sdist of
# <version>, holding the package and nothing else, with py.typed, every hand-written module and
# a __version__ that matches.
#
#   .github/scripts/check-dist.sh dist 0.1.0
set -euo pipefail

dist=$1
version=$2
fail() { echo "$*" >&2; exit 1; }

wheel="$dist/pycarlo2-$version-py3-none-any.whl"
sdist="$dist/pycarlo2-$version.tar.gz"
[ "$(find "$dist" -maxdepth 1 -type f ! -name '.*' | wc -l)" -eq 2 ] || fail "$dist should hold exactly one wheel and one sdist"
[ -f "$wheel" ] || fail "no $wheel"
[ -f "$sdist" ] || fail "no $sdist"

wheel_files=$(unzip -Z1 "$wheel")
outside=$(grep -vE "^(pycarlo2/|pycarlo2-$version\.dist-info/)" <<<"$wheel_files" || true)
[ -z "$outside" ] || fail "the wheel holds files outside the package: $outside"

# The hand-written modules are the package entries in .openapi-generator-ignore, which test.yml
# keeps in step with the modules marked hand-written.
for f in pycarlo2/__init__.py pycarlo2/py.typed $(grep -E '^pycarlo2/' .openapi-generator-ignore); do
  grep -qxF "$f" <<<"$wheel_files" || fail "the wheel lacks $f"
done

unzip -p "$wheel" pycarlo2/__init__.py | grep -qxF "__version__ = \"$version\"" \
  || fail "pycarlo2.__version__ is not $version; was the tree stamped?"

outside=$(tar tzf "$sdist" | grep -vE "^pycarlo2-$version/(pycarlo2/|pyproject\.toml$|README\.md$|LICENSE$|PKG-INFO$|\.gitignore$)" || true)
[ -z "$outside" ] || fail "the sdist holds files outside the package: $outside"

echo "$wheel and $sdist hold the package and nothing else."
