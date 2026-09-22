## Context

The first Miller Words integration stores Story 001 at `personal-site/public/things/miller-words/output/` with illustrations in a shared `cartoon/` directory. The Thing content currently places two standalone anchors in Markdown, while the shared Thing detail route renders arbitrary Markdown and a generic `links` sidebar. See `proposal.md` and `specs/personal-site-miller-words-episodes/spec.md` for the scope and behavior contract.

## Goals / Non-Goals

**Goals:**

- Represent episode metadata in frontmatter as an ordered array of grouped resources.
- Keep the episode UI reusable from the shared Thing detail route and inert for other Things.
- Make each episode asset bundle independently portable and preserve the generated HTML experience.
- Keep local asset URLs explicit and validated as site-relative paths.
- Make adding Story 002 a content-and-assets operation rather than a template edit.

**Non-Goals:**

- Do not turn all Thing links into episode records.
- Do not rebuild the generated vocabulary HTML, quiz, or PDF in Astro.
- Do not add a client-side episode router, database, CMS, or upload workflow.
- Do not change the existing generated Miller Words source files.

## Decisions

1. **Add an optional `episodes` array to the Things schema.** Each record uses `slug`, `title`, `htmlUrl`, and `pdfUrl`, with site-relative URL validation. The field defaults to an empty array so existing Things remain unchanged. An explicit array is preferable to parsing Markdown links because it gives the build a validated, inspectable contract.

2. **Render episodes in the shared Thing detail route.** A small local component or route section will render the set after the Thing prose when `episodes.length > 0`; the sidebar's existing `links` behavior remains available for unrelated external links. This avoids a Miller Words-only page fork while keeping the component's data model focused.

3. **Use per-episode asset bundles.** Migrate Story 001 to `public/things/miller-words/episodes/story-001/` with the generated HTML/PDF and an internal illustration directory. Preserve the generated HTML's relative directory shape, or make the smallest path adjustment necessary, so its references remain self-contained. Future episodes follow the same convention.

4. **Keep resources paired in one card.** The episode title is the primary label; actions are clearly named “View HTML” and “Download PDF”. The PDF link keeps the `download` attribute, while the HTML link may open in a new tab because it is a complete standalone practice page.

5. **Keep the content body narrative-focused.** Remove the current Story 001 link block from prose after the structured episode set is rendering. The prose can continue explaining the practice; resource navigation belongs to the reusable episode UI.

## Risks / Trade-offs

- [Risk] Moving Story 001 changes existing asset URLs → update the episode metadata and verify old links are not referenced by the site; no redirect is needed for an unpublished local path.
- [Risk] Generic schema growth could make the Thing model noisy → keep `episodes` optional with a default empty array and render nothing when absent.
- [Risk] A generated HTML file may assume a specific relative folder shape → copy its asset subtree to match the expected paths and test every referenced illustration after the build.
- [Risk] Long episode titles or action labels could compress on mobile → use a stacked responsive card layout and keyboard-visible focus styles.

## Migration Plan

1. Extend the Things schema and add the reusable episode renderer.
2. Move Story 001 public assets into its episode bundle and update the content metadata.
3. Remove the old hard-coded Markdown links.
4. Run `npm run build`, then serve `dist/` locally and verify the Thing page, each HTML asset, each illustration, and each PDF response.

Rollback consists of restoring the prior asset paths and Markdown links, removing the optional schema/rendering code, and rebuilding; no external migration is involved.
