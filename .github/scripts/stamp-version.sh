#!/usr/bin/env bash
# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0
#
# Writes a release's version over the 0.0.0 the tree carries on main, in pyproject.toml and the
# three places the generator stamps it, before the release builds. The tree is never committed
# after this.
#
#   .github/scripts/stamp-version.sh 0.1.4
set -euo pipefail

version=$1
[[ $version =~ ^[0-9]+\.[0-9]+\.[0-9]+(\.dev[0-9]+)?$ ]] || { echo "not a release version: '$version'" >&2; exit 1; }

# stamp <file> <text holding 0.0.0>: replace that text, which must appear exactly once.
stamp() {
  local file=$1 from=$2
  [ "$(grep -cF -- "$from" "$file")" = 1 ] || { echo "$file should hold '$from' once" >&2; exit 1; }
  FROM=$from TO=${from/0.0.0/$version} perl -pi -e 's/\Q$ENV{FROM}\E/$ENV{TO}/' "$file"
}

stamp pyproject.toml 'version = "0.0.0"'
stamp pycarlo2/__init__.py '__version__ = "0.0.0"'
stamp pycarlo2/api_client.py 'OpenAPI-Generator/0.0.0/python'
stamp pycarlo2/configuration.py 'SDK Package Version: 0.0.0'
echo "Stamped $version."
