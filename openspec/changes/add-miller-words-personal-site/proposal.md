## Why

Miller's vocabulary practice already produces a rich, interactive HTML story and a print-ready PDF, but those outputs are not discoverable from the personal site. Adding a small public-facing entry gives the family a stable place to read the practice story and download its printable version.

## What Changes

- Add a published Miller Words entry to the personal site's Things archive.
- Make the Story 001 HTML output viewable from the site in a visitor-friendly page or embedded presentation.
- Make the matching Story 001 PDF available as an explicit download.
- Preserve the existing Miller Words story content and illustrations while adapting paths and presentation for the Astro site's static build.
- Keep the integration accessible and responsive on desktop and mobile.

## Capabilities

### New Capabilities

- `personal-site-miller-words`: Publicly present Miller's vocabulary practice story with a viewable HTML experience and downloadable PDF.

### Modified Capabilities

## Impact

- Astro pages, content, navigation, and public static assets under `personal-site/`.
- Existing generated artifacts under `miller-words/output/` and its cartoon images are read-only source material.
- No runtime service, API, or new dependency is required; the result remains a static site feature.
