## Context

Story 001 currently contains a two-panel dashboard: a word-trail chart with aggregate counters and a memory-matching exam. The word-trail data describes the current Miller Words word bank, while the exam belongs to the story's practice experience. The site already has a structured Miller Words episode set and static Astro routes. See `proposal.md` and `specs/miller-words-overall-report/spec.md` for the scope and behavior contract.

## Goals / Non-Goals

**Goals:**

- Remove only the overall word-statistics panel from Story 001; preserve the memory exam and story practice.
- Add a stable overall report page linked from the Miller Words Thing entry.
- Give the report a structured data source with aggregate totals and daily/session rows that can grow over time.
- Provide both visual summaries and accessible text/table equivalents.
- Keep all output static and public-safe.

**Non-Goals:**

- Do not change the meaning of the existing word list or silently correct its source data.
- Do not remove the memory meter or matching exam from individual stories.
- Do not add user accounts, live progress synchronization, analytics, or a database.
- Do not make individual story pages dynamically aggregate all report data at runtime.

## Decisions

1. **Use a dedicated Astro overall-report route.** A native route such as `/things/miller-words/report/` can share the site's layout and accessibility conventions, while the generated episode HTML remains an independent child-facing artifact. This is preferable to embedding the report in Story 001 or maintaining a second standalone HTML dashboard.

2. **Store report data separately from episode content.** Add a small public-safe structured data module under `personal-site/src/data/` containing total entries, unique words, session/day records, and any future aggregate fields. The report page renders from this data; episode Markdown only needs a report link and episode resources.

3. **Extract the word-trail panel, not the memory exam.** Remove the chart/statistics panel from the copied Story 001 HTML, update the remaining practice layout for one panel, and put the chart plus aggregate counters on the report page. Keep Story 001's word bank and memory-exam behavior intact.

4. **Add an optional report link object to the Things schema.** A site-relative report URL and label will allow the shared Thing page to show the overall report only when configured, keeping other Things unchanged and avoiding misuse of the external-only `links` field.

5. **Include a semantic table or text summary alongside charts.** CSS/visual bars can communicate the trend at a glance, but the report must expose day labels and counts as ordinary text so it remains useful without visual interpretation or JavaScript.

## Risks / Trade-offs

- [Risk] Removing a large HTML panel from a generated one-line file may leave stale CSS or layout assumptions → verify the remaining memory exam renders independently and remove only unused statistics markup/styles where safe.
- [Risk] Aggregate data can drift from `miller-words/words.md` → record the source and update procedure in the report data module; preserve exact verified counts and flag future unverified values rather than guessing.
- [Risk] A report link may be overlooked if mixed with episode actions → render it as a distinct “Overall report” section before or beside the episode set, with a different visual hierarchy.
- [Risk] Future sessions may have different dimensions than daily counts → model rows as labeled sessions with explicit entry counts and leave derived metrics extensible rather than hard-coding eight bars.

## Migration Plan

1. Add the optional report metadata field and current report data.
2. Create the overall report route and link it from Miller Words.
3. Remove the word-trail panel from Story 001 and verify its memory exam remains.
4. Run the personal-site build and inspect report/story routes at desktop and mobile widths.

Rollback restores the previous Story 001 HTML asset and removes the report route/data/link; no external migration is involved.
