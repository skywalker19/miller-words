## 1. Public source assets

- [x] 1.1 Copy the approved Story 001 HTML and four cartoon derivatives into the site's `public/things/miller-words/` tree, preserving relative links, and verify each referenced image returns successfully from the built static output
- [x] 1.2 Copy the approved Story 001 PDF into the site's public Miller Words asset tree and verify it is recognized as a PDF and has non-zero size

## 2. Site integration

- [x] 2.1 Add a published Miller Words Thing entry using the existing content schema and verify it appears in the Things archive with a stable detail URL
- [x] 2.2 Add clear view-HTML and download-PDF actions to the Thing content and verify their labels identify the destination formats and work from the rendered page

## 3. Verification

- [x] 3.1 Run the personal-site production build and verify Astro check and static generation complete without errors
- [x] 3.2 Inspect the generated HTML, asset paths, and PDF response in a local preview and verify the page is usable at mobile width without ordinary horizontal overflow
