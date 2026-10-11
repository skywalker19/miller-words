#!/usr/bin/env bash
set -euo pipefail

MILLER_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SITE_ROOT="$(cd "$MILLER_ROOT/../personal-site" && pwd)"
SOURCE_MESSAGE="${1:-Update Miller Words content}"
SITE_MESSAGE="${2:-Update Miller Words on personal-site}"
INCLUDE_SHARED_ROUTE="${INCLUDE_SHARED_ROUTE:-0}"
PUBLISH_IMPLEMENTATION_DOCS="${PUBLISH_IMPLEMENTATION_DOCS:-0}"

preflight_repo() {
  local repo="$1"
  local label="$2"
  local branch upstream staged
  branch="$(git -C "$repo" branch --show-current)"
  upstream="$(git -C "$repo" rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>/dev/null || true)"
  if [[ "$branch" != main || "$upstream" != origin/main ]]; then
    printf '%s must be on main tracking origin/main (branch=%s, upstream=%s).\n' "$label" "$branch" "${upstream:-none}" >&2
    return 1
  fi
  staged="$(git -C "$repo" diff --cached --name-only)"
  if [[ -n "$staged" ]]; then
    printf 'Refusing to publish %s because its index already has staged changes:\n%s\n' "$label" "$staged" >&2
    return 1
  fi
  git -C "$repo" fetch --quiet origin main
  if ! git -C "$repo" merge-base --is-ancestor origin/main HEAD; then
    printf '%s is behind or diverged from origin/main; sync it before publishing.\n' "$label" >&2
    return 1
  fi
}

publish_repo() {
  local repo="$1"
  local label="$2"
  local paths="$3"
  local -a allowed
  IFS=$'\t' read -r -a allowed <<< "$paths"
  local -a existing=()
  local path
  for path in "${allowed[@]}"; do
    if [[ -e "$repo/$path" ]] || git -C "$repo" ls-files --error-unmatch -- "$path" >/dev/null 2>&1; then
      existing+=("$path")
    fi
  done
  if ((${#existing[@]})); then git -C "$repo" add -A -- "${existing[@]}"; fi
  if ! git -C "$repo" diff --cached --quiet; then
    printf '\n%s files selected for %s:\n' "$label" "$label"
    git -C "$repo" diff --cached --name-status
    git -C "$repo" commit -m "$label"
  else
    printf '%s has no selected changes; skipping its commit.\n' "$label"
  fi
  if ! git -C "$repo" push origin main; then
    printf '\nPush failed for %s. Any earlier repository push may already be complete; check each main branch before retrying.\n' "$label" >&2
    return 1
  fi
}

preflight_repo "$MILLER_ROOT" "Miller Words"
preflight_repo "$SITE_ROOT" "personal-site"
publish_repo "$MILLER_ROOT" "$SOURCE_MESSAGE" $'.gitignore\tAGENTS.md\tREADME.md\twords.md\tprompts.md\tpractice\tcartoon\toutput/data\toutput/html\toutput/pdf\toutput/site-staging\tscripts/make_overall_report.py\tscripts/sync_personal_site_report.py\tscripts/sync_personal_site.sh\tscripts/publish_repos.sh\tscripts/report'
SITE_PATHS=$'src/content/things/miller-words.md\tsrc/data/miller-words-overall-report.json\tsrc/data/miller-words-overall-report.ts\tsrc/pages/things/miller-words/report\tsrc/components/MillerWordsEntry.astro\tsrc/styles/miller-words-report.css\tsrc/utils/render-miller-words-report.mjs\tpublic/things/miller-words'
if [[ "$INCLUDE_SHARED_ROUTE" == 1 ]]; then SITE_PATHS+=$'\tsrc/pages/things/[...id].astro'; fi
if [[ "$PUBLISH_IMPLEMENTATION_DOCS" == 1 ]]; then SITE_PATHS+=$'\tREADME.md\tdeploy/SETUP.md'; fi
publish_repo "$SITE_ROOT" "$SITE_MESSAGE" "$SITE_PATHS"

printf '\nGit publication finished. This command does not generate or sync content, run a build, or deploy the server.\n'
