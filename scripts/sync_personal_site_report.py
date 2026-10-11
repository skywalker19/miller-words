#!/usr/bin/env python3
"""Apply the prepared report files without overwriting concurrent site changes."""
import hashlib
import json
import shutil
from pathlib import Path

root = Path(__file__).resolve().parents[1]
stage = root / 'output/site-staging'
site = root.parent / 'personal-site'
baseline = json.loads((stage / 'baseline.json').read_text())
for relative, expected in baseline.items():
    target = site / relative
    actual = hashlib.sha256(target.read_bytes()).hexdigest() if target.exists() else None
    if actual != expected:
        raise SystemExit(f'Site file changed after preparation: {relative}; regenerate staging before applying.')
for relative in baseline:
    target = site / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(stage / relative, target)
print(f'Applied {len(baseline)} prepared report/story files to personal-site. Nothing published.')
