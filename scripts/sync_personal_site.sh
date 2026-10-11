#!/usr/bin/env bash
set -euo pipefail

MILLER_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SITE_ROOT="$(cd "$MILLER_ROOT/../personal-site" && pwd)"

python3 "$MILLER_ROOT/scripts/make_overall_report.py"
python3 "$MILLER_ROOT/scripts/sync_personal_site_report.py"

cd "$SITE_ROOT"
npm run check:sensitive
npm run build
npm run check:sensitive -- --path dist

printf '\nMiller Words static files are synced and the personal-site build passed. Nothing was committed or published.\n'
