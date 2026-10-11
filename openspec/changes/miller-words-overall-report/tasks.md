## 1. Report data and content model

- [x] 1.1 Add structured overall-report data for current totals and daily counts, preserving the verified 45-entry/44-unique/8-day figures; verify the data is public-safe and type-checkable
- [x] 1.2 Extend the Things schema with an optional site-relative report link and configure Miller Words to point to the overall report; verify other Things remain valid without report metadata

## 2. Overall report

- [x] 2.1 Create the stable Miller Words overall-report route using the shared site layout and report data; verify it renders aggregate totals and the labeled daily/session history
- [x] 2.2 Add accessible text/table equivalents and responsive styling for the report statistics; verify the report remains readable without relying on chart graphics or horizontal scrolling

## 3. Story 001 migration

- [x] 3.1 Remove the word-trail chart and aggregate counters from the Story 001 HTML asset while preserving the memory meter, matching exam, scenes, and illustrations; verify no word-trail dashboard markup remains
- [x] 3.2 Update the remaining Story 001 layout/styles as needed and verify the HTML still loads all four cartoon illustrations and its practice interactions

## 4. Verification

- [x] 4.1 Run `npm run build` in `personal-site/` and verify Astro check and static generation complete without errors
- [x] 4.2 Run local HTTP checks for the Miller Words Thing page, overall report, Story 001 HTML, four illustrations, and PDF; verify report link separation and expected successful content types

## 5. Complete word-notebook entry — 2026-10-11

- [x] 5.1 Generate report data from the canonical word table: 140 records, 139 distinct forms, 30 Days, five weeks, five stories and 22 scenes; preserve week provenance and daily ordinals
- [x] 5.2 Add daily and weekly statistics, semantic detail tables, a searchable full word bank, and links to every story in the overall report; generate a local entry page and the personal-site report from the same data and renderer
- [x] 5.3 Generate browser pages and copy existing illustrations for Stories 002–005; allow absent PDF resources so only available print versions are linked
- [x] 5.4 Update README and the personal-site Miller Words entry, synchronize the prepared site files, and compile the Astro site successfully (zero errors, warnings or hints); leave publishing to a separate request
