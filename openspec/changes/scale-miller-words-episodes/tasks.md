## 1. Content model

- [x] 1.1 Extend the Things schema with an optional validated `episodes` array containing `slug`, title, HTML URL, and PDF URL fields; verify existing Things still pass content validation
- [x] 1.2 Convert Story 001's two standalone links into one structured episode object and remove the hard-coded link block from the Markdown body; verify the content contains one paired episode

## 2. Episode presentation

- [x] 2.1 Add a reusable episode-set presentation to the shared Thing detail route, rendering one grouped entry per episode and nothing for Things without episodes; verify Story 001 appears as one grouped entry
- [x] 2.2 Add accessible HTML-view and PDF-download actions with responsive layout and visible keyboard focus; verify both actions are reachable and clearly identify their formats

## 3. Asset migration

- [x] 3.1 Move Story 001 HTML, PDF, and four illustrations into a self-contained episode directory under `public/things/miller-words/episodes/story-001/`; verify generated HTML illustration references resolve within that bundle
- [x] 3.2 Update Story 001 episode URLs to the migrated paths and verify the HTML, PDF, and all four illustrations are present with non-zero sizes

## 4. Verification

- [x] 4.1 Run `npm run build` in `personal-site/` and verify Astro check and static generation complete without errors
- [x] 4.2 Inspect the built Thing page and run local HTTP checks for the episode page, HTML, four illustrations, and PDF; verify mobile styles prevent ordinary horizontal overflow and the download response is `application/pdf`
