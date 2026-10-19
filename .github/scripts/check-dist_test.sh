#!/usr/bin/env bash
# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0
#
# Tests check-dist.sh against hand-made distributions.
set -euo pipefail

script=$(cd "$(dirname "$0")" && pwd)/check-dist.sh
ignore=$(cd "$(dirname "$0")/../.." && pwd)/.openapi-generator-ignore
failures=0
root=$(mktemp -d)
trap 'rm -rf "$root"' EXIT

version=
wheel=

# make_sdist : (re)build the sdist from sd/, as a list of files so no directory entries appear.
make_sdist() {
  (cd sd && find "pycarlo2-$version" -type f | tar czf "../dist/pycarlo2-$version.tar.gz" -T -)
}

# fixture <version> : a fresh directory, now the cwd, holding a complete build of <version>.
fixture() {
  local dir f
  version=$1
  dir=$(mktemp -d "$root/XXXXXX")
  cd "$dir"
  cp "$ignore" .openapi-generator-ignore
  mkdir dist stage "sd"
  : > dist/.gitignore

  mkdir -p stage/pycarlo2 "stage/pycarlo2-$version.dist-info"
  printf '__version__ = "%s"\n' "$version" > stage/pycarlo2/__init__.py
  : > stage/pycarlo2/py.typed
  : > "stage/pycarlo2-$version.dist-info/METADATA"
  while read -r f; do
    : > "stage/$f"
  done < <(grep -E '^pycarlo2/' .openapi-generator-ignore)
  wheel="$PWD/dist/pycarlo2-$version-py3-none-any.whl"
  (cd stage && zip -qrD "$wheel" .)

  mkdir -p "sd/pycarlo2-$version/pycarlo2"
  : > "sd/pycarlo2-$version/pycarlo2/__init__.py"
  for f in pyproject.toml README.md LICENSE PKG-INFO .gitignore; do
    : > "sd/pycarlo2-$version/$f"
  done
  make_sdist
}

# expect_pass|expect_fail <name> [version] : run the script on dist in the cwd.
check() {
  local want=$1 name=$2 got=fail
  if "$script" dist "${3:-$version}" >/dev/null 2>&1; then got=pass; fi
  if [[ $got == "$want" ]]; then
    echo "ok   $name"
  else
    echo "FAIL $name: want $want, got $got"
    failures=$((failures + 1))
  fi
}
expect_pass() { check pass "$@"; }
expect_fail() { check fail "$@"; }

fixture 0.1.0
expect_pass "a complete build passes"

fixture 0.1.0.dev123
expect_pass "a .dev version passes"

fixture 0.1.0
expect_fail "a version other than the built one is rejected" 0.1.1

fixture 0.1.0
zip -qd "$wheel" pycarlo2/paging.py
expect_fail "a hand-written module missing from the wheel is rejected"

fixture 0.1.0
mkdir stage/tests
: > stage/tests/test_x.py
(cd stage && zip -q "$wheel" tests/test_x.py)
expect_fail "tests in the wheel are rejected"

fixture 0.1.0
printf '__version__ = "0.1.1"\n' > stage/pycarlo2/__init__.py
(cd stage && zip -q "$wheel" pycarlo2/__init__.py)
expect_fail "a __version__ that differs from the version is rejected"

fixture 0.1.0
zip -qd "$wheel" pycarlo2/py.typed
expect_fail "a wheel without py.typed is rejected"

fixture 0.1.0
mkdir sd/pycarlo2-0.1.0/.work
: > sd/pycarlo2-0.1.0/.work/notes.md
make_sdist
expect_fail "an extra file in the sdist is rejected"

fixture 0.1.0
: > dist/extra.whl
expect_fail "a third file in dist is rejected"

fixture 0.1.0
rm dist/pycarlo2-0.1.0.tar.gz
expect_fail "a build without an sdist is rejected"

exit $((failures > 0))
