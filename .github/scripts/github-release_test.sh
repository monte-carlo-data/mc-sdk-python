#!/usr/bin/env bash
# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0
#
# Tests github-release.sh against a fake gh that logs its calls and serves canned releases and tags.
# shellcheck disable=SC2329 # the helpers run through check, by name
set -euo pipefail

script=$(cd "$(dirname "$0")" && pwd)/github-release.sh
failures=0
root=$(mktemp -d)
trap 'rm -rf "$root"' EXIT
calls=$root/calls
export CALLS=$calls

mkdir "$root/bin" "$root/dist"
touch "$root/dist/pycarlo2-0.1.1-py3-none-any.whl" "$root/dist/pycarlo2-0.1.1.tar.gz"
cat > "$root/bin/gh" <<'EOF'
#!/usr/bin/env bash
echo "${*//$'\n'/ }" >> "$CALLS"
filter=
prev=
for a in "$@"; do
  if [ "$prev" = --jq ]; then filter=$a; fi
  prev=$a
done
case "$*" in
  "api repos/o/r/releases --paginate"*) printf '%s' "${STUB_RELEASES:-[]}" | jq -r "$filter" ;;
  "api repos/o/r/git/matching-refs/"*)
    if [ -n "${STUB_REFS_FAIL:-}" ]; then echo "gh: HTTP 500" >&2; exit 1; fi
    printf '%s\n' "${STUB_REFS:-}" ;;
  "api -X DELETE "* | "release create "*) ;;
  *) echo "unexpected gh call: $*" >&2; exit 2 ;;
esac
EOF
chmod +x "$root/bin/gh"
export PATH="$root/bin:$PATH"

status=0
reset() {
  : > "$calls"
  unset STUB_REFS_FAIL
  STUB_RELEASES='[]'
  STUB_REFS=$'refs/tags/v0.1.0\nrefs/tags/v0.1.1'
  export STUB_RELEASES STUB_REFS
}

# release <tag> <version> : run the script and record its exit status.
release() {
  status=0
  GITHUB_REPOSITORY=o/r "$script" "$1" "$2" "$root/dist" > "$root/out" 2>&1 || status=$?
}

called() { grep -qF -- "$1" "$calls"; }

# check <name> <command...> : passes when the command succeeds.
check() {
  local name=$1
  shift
  if "$@"; then
    echo "ok   $name"
  else
    echo "FAIL $name"
    failures=$((failures + 1))
  fi
}

created() { [ "$(grep -c '^release create v0.1.1 ' "$calls" || true)" = 1 ]; }
no_create() { ! called 'release create'; }
no_delete() { ! called 'DELETE'; }
succeeded() { [ "$status" = 0 ]; }
failed() { [ "$status" != 0 ]; }

reset
release v0.1.1 0.1.1
check "the highest tag is created and marked latest" created
check "the create call verifies the tag" called '--verify-tag'
check "the create call marks it latest" called '--latest=true'
check "the create call attaches every dist file" \
  called "$root/dist/pycarlo2-0.1.1-py3-none-any.whl $root/dist/pycarlo2-0.1.1.tar.gz"
check "a clean run exits 0" succeeded
check "a clean run deletes nothing" no_delete
check "the notes name the PyPI release" \
  called 'Published to PyPI as [pycarlo2 0.1.1](https://pypi.org/project/pycarlo2/0.1.1/):'
check "the notes carry the install command" called 'pip install pycarlo2==0.1.1'

reset
STUB_REFS=$'refs/tags/v0.1.1\nrefs/tags/v0.1.10'
release v0.1.1 0.1.1
check "a higher tag compared as numbers keeps latest off" called '--latest=false'

reset
STUB_REFS=$'refs/tags/v0.1.0\nrefs/tags/v0.1.1\nrefs/tags/v0.2.0-rc1'
release v0.1.1 0.1.1
check "a non-plain tag does not take latest" called '--latest=true'

reset
STUB_RELEASES='[{"id":11,"tag_name":"v0.1.1","draft":false,"author":{"login":"someone"}}]'
release v0.1.1 0.1.1
check "a published release is left alone" succeeded
check "a published release is not recreated" no_create
check "a published release is not deleted" no_delete

reset
STUB_RELEASES='[{"id":10,"tag_name":"v0.1.0","draft":false,"author":{"login":"someone"}},
{"id":11,"tag_name":"v0.1.1","draft":true,"author":{"login":"github-actions[bot]"}}]'
release v0.1.1 0.1.1
check "a bot draft is deleted by id" called 'api -X DELETE repos/o/r/releases/11'
check "a bot draft is replaced" created
check "a replaced draft exits 0" succeeded

reset
STUB_RELEASES='[{"id":11,"tag_name":"v0.1.1","draft":true,"author":{"login":"someone"}}]'
release v0.1.1 0.1.1
check "another author's draft fails the run" failed
check "another author's draft is not deleted" no_delete
check "another author's draft is not replaced" no_create

reset
STUB_RELEASES='[{"id":11,"tag_name":"v0.1.1","draft":true,"author":{"login":"github-actions[bot]"}},
{"id":12,"tag_name":"v0.1.1","draft":false,"author":{"login":"someone"}}]'
release v0.1.1 0.1.1
check "a published release after a bot draft wins" succeeded
check "a published release after a bot draft deletes nothing" no_delete
check "a published release after a bot draft creates nothing" no_create

reset
STUB_RELEASES='[{"id":11,"tag_name":"v0.1.1","draft":true,"author":{"login":"github-actions[bot]"}},
{"id":12,"tag_name":"v0.1.1","draft":true,"author":{"login":"someone"}}]'
release v0.1.1 0.1.1
check "a mixed set of drafts fails the run" failed
check "a mixed set of drafts deletes nothing" no_delete

reset
STUB_REFS_FAIL=1
export STUB_REFS_FAIL
release v0.1.1 0.1.1
check "a failing tag listing fails the run" failed
check "a failing tag listing creates nothing" no_create

exit $((failures > 0))
