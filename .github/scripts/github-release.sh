#!/usr/bin/env bash
# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0
#
# Creates the GitHub release for <tag> from the files in <dist>, unless one is published. Marks it
# latest only when it is the highest plain version tag. Replaces a draft an interrupted run of this
# job left, and refuses to touch anyone else's.
#
#   GITHUB_REPOSITORY=owner/repo .github/scripts/github-release.sh v0.1.4 0.1.4 dist
set -euo pipefail

tag=$1 version=$2 dist=$3
repo=$GITHUB_REPOSITORY
bot='github-actions[bot]' # what this job's GITHUB_TOKEN creates

# Listed rather than fetched by tag: the by-tag lookup never returns a draft.
releases=$(gh api "repos/$repo/releases" --paginate \
  --jq ".[] | select(.tag_name == \"$tag\") | \"\(.id) \(.draft) \(.author.login)\"")

# A draft left behind comes from a run interrupted mid-upload: gh deletes its own draft when an
# upload fails. Nothing is deleted until every match has been checked.
drafts=()
while read -r id draft author; do
  [ -n "$id" ] || continue
  if [ "$draft" = false ]; then
    echo "$tag already has a release."
    exit 0
  fi
  drafts+=("$id $author")
done <<<"$releases"

for d in ${drafts[@]+"${drafts[@]}"}; do
  author=${d#* }
  if [ "$author" != "$bot" ]; then
    echo "::error::$tag has a draft release by $author; delete or publish it, then re-run." >&2
    exit 1
  fi
done
for d in ${drafts[@]+"${drafts[@]}"}; do
  gh api -X DELETE "repos/$repo/releases/${d%% *}"
  echo "Deleted the draft $tag release an interrupted run left."
done

refs=$(gh api "repos/$repo/git/matching-refs/tags/v" --jq '.[].ref')
highest=$(printf '%s\n' "$refs" | sed 's#^refs/tags/##' |
  { grep -E '^v[0-9]+\.[0-9]+\.[0-9]+$' || true; } | sort -V | tail -1)
latest=false
if [ "$highest" = "$tag" ]; then latest=true; fi

notes="Published to PyPI as [pycarlo2 $version](https://pypi.org/project/pycarlo2/$version/):"
# shellcheck disable=SC2016 # the backticks are a Markdown code fence
notes=$(printf '%s\n\n```bash\npip install pycarlo2==%s\n```\n' "$notes" "$version")

gh release create "$tag" "$dist"/pycarlo2-* --repo "$repo" --verify-tag \
  --title "$tag" --notes "$notes" --latest="$latest"
