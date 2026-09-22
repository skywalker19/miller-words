## Context

The source project already generates a self-contained Story 001 HTML file and a print-ready PDF, with four scene images stored alongside the source output. The destination is a static Astro site with a Things content collection and a shared archive layout. See `proposal.md` and `specs/personal-site-miller-words/spec.md` for the motivation and externally visible contract.

## Goals / Non-Goals

**Goals:**

- Add Miller Words as a normal published Thing using the site's existing archive and detail-page conventions.
- Preserve the supplied generated HTML as the canonical screen practice experience rather than reimplementing its story or quiz in Astro.
- Make the HTML's relative illustration links resolve after copying the public-safe generated assets into the site's static asset tree.
- Provide a concise landing/detail page with clear view and PDF-download actions.
- Keep the site build static, dependency-free, responsive, and accessible.

**Non-Goals:**

- Do not modify or regenerate the Miller Words source outputs.
- Do not expose the handwriting source photo or private workspace paths.
- Do not add server-side storage, analytics, authentication, or a new content system.
- Do not publish or deploy the site as part of this change.

## Decisions

1. **Use the existing Things collection and detail route.** This keeps Miller Words discoverable alongside the site's other small projects and avoids a parallel archive. Add a published Markdown entry with the required frontmatter and a short description plus the two public actions.

2. **Copy, do not link across repositories.** Static deployment cannot safely depend on `/miller-words/` at runtime. Copy the generated HTML and PDF plus the four approved cartoon derivatives into a descriptive `public/things/miller-words/` tree. Keep the HTML in a matching relative directory layout so its existing `../../cartoon/...` links continue to work.

3. **Offer both a site detail page and the full generated HTML.** The Thing detail page explains the practice and provides a view-story link to the generated HTML in a new browser tab, plus a PDF download link. This preserves the generated interaction and avoids fragile iframe height behavior while still making the HTML directly viewable from the site.

4. **Use descriptive labels and links.** The view action names “Story 001 HTML” and the download action names “Story 001 PDF” so their destination and format are clear to keyboard and assistive-technology users.

## Risks / Trade-offs

- [Risk] The generated HTML references relative cartoon paths → preserve its source-relative folder shape and verify all four image URLs resolve in the built output.
- [Risk] The copied HTML has its own visual language → keep the surrounding Astro detail page quiet and minimal, and let the generated story remain visually self-contained.
- [Risk] Future Miller Words stories could become stale on the site → document the copied asset locations and validate that the displayed story title and PDF remain aligned during future updates.

## Migration Plan

Copy the approved generated artifacts into `personal-site/public/`, add the published Thing content, run the production build, and inspect the resulting static paths. Rollback is deleting the new Thing entry and Miller Words asset directory; no existing data migration is required.
