#!/usr/bin/env bash
# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0
#
# Tests stamp-version.sh against copies of the files it edits.
set -euo pipefail

script=$(cd "$(dirname "$0")" && pwd)/stamp-version.sh
repo=$(cd "$(dirname "$0")/../.." && pwd)
failures=0
root=$(mktemp -d)
trap 'rm -rf "$root"' EXIT

files=(pyproject.toml pycarlo2/__init__.py pycarlo2/api_client.py pycarlo2/configuration.py)

# tree : a fresh directory, now the cwd, holding copies of the files the script edits.
tree() {
  local dir f
  dir=$(mktemp -d "$root/XXXXXX")
  mkdir "$dir/pycarlo2"
  for f in "${files[@]}"; do cp "$repo/$f" "$dir/$f"; done
  cd "$dir"
}

# count <file> <text> : how many lines of <file> hold <text>.
count() { grep -cF -- "$2" "$1" || true; }

report() {
  local name=$1 ok=$2
  if [[ $ok == 1 ]]; then
    echo "ok   $name"
  else
    echo "FAIL $name"
    failures=$((failures + 1))
  fi
}

expect_pass() {
  local name=$1 version=$2 ok=0
  "$script" "$version" >/dev/null 2>&1 && ok=1
  report "$name" "$ok"
}

expect_fail() {
  local name=$1 version=$2 ok=1
  "$script" "$version" >/dev/null 2>&1 && ok=0
  report "$name" "$ok"
}

tree
expect_pass "a release version stamps" 0.1.4
ok=1
stamped=('version = "0.1.4"' '__version__ = "0.1.4"' 'OpenAPI-Generator/0.1.4/python' 'SDK Package Version: 0.1.4')
stale=('version = "0.0.0"' '__version__ = "0.0.0"' 'OpenAPI-Generator/0.0.0/python' 'SDK Package Version: 0.0.0')
for i in 0 1 2 3; do
  [[ $(count "${files[$i]}" "${stamped[$i]}") == 1 ]] || ok=0
  [[ $(count "${files[$i]}" "${stale[$i]}") == 0 ]] || ok=0
done
report "each file holds its stamped text once and no 0.0.0 stamp" "$ok"

tree
expect_pass "a dev version stamps" 0.1.4.dev99

for bad in 0.1 v0.1.0 0.1.0rc1 ""; do
  tree
  expect_fail "version '$bad' is rejected" "$bad"
done

tree
"$script" 0.1.4 >/dev/null 2>&1
expect_fail "stamping twice is rejected" 0.1.5

tree
printf '__version__ = "0.0.0"\n' >> pycarlo2/__init__.py
expect_fail "a stamped text that appears twice is rejected" 0.1.4

tree
perl -pi -e 's{OpenAPI-Generator/0\.0\.0/python}{OpenAPI-Generator/python}' pycarlo2/api_client.py
expect_fail "a stamped text that is missing is rejected" 0.1.4

exit $((failures > 0))
