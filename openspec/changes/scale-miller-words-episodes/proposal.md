## Why

Miller Words is currently presented as one Thing with Story 001's HTML and PDF links embedded directly in prose. As more vocabulary stories are produced, that shape will become repetitive and make each HTML/PDF pair harder to discover and maintain.

## What Changes

- Model Miller Words stories as an ordered set of episodes in the personal-site content data.
- Present each episode as one grouped entry with its HTML view and PDF download actions together.
- Move Story 001's hard-coded links into the structured episode set.
- Organize future episode assets under self-contained episode folders while preserving each generated HTML file's image links.
- Keep the shared Things page reusable for other Things that do not have episodes.

## Capabilities

### New Capabilities

- `personal-site-miller-words-episodes`: Manage and present multiple Miller Words episodes as grouped HTML/PDF resource pairs.

### Modified Capabilities

## Impact

- Astro content schema and the shared Thing detail page under `personal-site/src/`.
- Miller Words content metadata under `personal-site/src/content/things/miller-words.md`.
- Public Miller Words assets under `personal-site/public/things/miller-words/`.
- No new dependency, runtime service, API, or publishing action is required.
