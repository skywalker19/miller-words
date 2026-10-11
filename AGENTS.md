# Miller Words agent instructions

After editing canonical words, stories, or story illustrations, finish by running
`bash scripts/sync_personal_site.sh` so the sibling personal-site receives and
validates the generated static content. The generator alone only prepares local
outputs. Preserve the site-owned `MillerWordsEntry.astro` presentation; do not
generate or overwrite it from this repository.

Run `bash scripts/publish_repos.sh` only when the user explicitly asks to
publish. That command performs Git commits and pushes only; it does not generate,
sync, build, or deploy. Server deployment is a separate user-requested action.
