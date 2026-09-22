## Why

Story 001 currently carries the word-count dashboard even though those numbers describe Miller Words as a whole, not one story. As more episodes are added, the statistics need a single home that can grow across all vocabulary sessions while keeping each story focused on reading and recall practice.

## What Changes

- Remove the word-statistics dashboard from the Story 001 child-facing story HTML.
- Add an overall Miller Words report that presents the aggregate word-learning statistics in one place.
- Link to the overall report from the Miller Words Thing entry, separately from the episode set.
- Define a data shape that can incorporate future word sessions and episodes without duplicating chart markup in each story.
- Keep episode HTML focused on its story, scenes, and practice activities.

## Capabilities

### New Capabilities

- `miller-words-overall-report`: Present aggregate vocabulary statistics for the complete Miller Words practice, independent of individual story episodes.

### Modified Capabilities

## Impact

- The generated Story 001 HTML asset under `personal-site/public/`.
- A new static report page or asset and a report link in the Miller Words Thing entry.
- Public-safe aggregation data derived from the canonical Miller Words word list and future session records.
- No runtime service or new dependency is required.
