## Purpose

Give Miller Words one durable, aggregate view of vocabulary progress so individual story episodes can stay focused on reading and recall while the overall practice history grows across future sessions.

## ADDED Requirements

### Requirement: Story episodes stay focused on story practice

Individual Miller Words episode HTML SHALL present its story, scenes, illustrations, and recall activities without carrying the overall word-count dashboard.

#### Scenario: Story 001 no longer owns aggregate statistics

- **WHEN** a visitor opens the Story 001 HTML experience
- **THEN** the daily word-count chart and overall entry/unique-word counters are absent from the story practice area

#### Scenario: Story practice remains available

- **WHEN** a visitor opens Story 001 after the statistics are moved
- **THEN** the story scenes, illustrations, word labels, and memory-matching practice remain usable

### Requirement: Miller Words has an overall statistics report

The Miller Words site SHALL provide a stable overall report that presents aggregate vocabulary statistics across all recorded sessions and episodes.

#### Scenario: Current aggregate statistics are visible

- **WHEN** a visitor opens the overall report for the current word bank
- **THEN** the report shows 140 recorded entries, 139 distinct practice word/phrase forms, all 30 recorded daily counts, and five weekly summaries

#### Scenario: Daily history is understandable

- **WHEN** a visitor reviews the daily statistics
- **THEN** each recorded day has a clearly labeled count and the report distinguishes entries from unique words

#### Scenario: Weekly history is understandable

- **WHEN** a visitor reviews the weekly statistics
- **THEN** each week shows its Day range, entry count, and distinct form count, with inferred weeks explicitly identified and Day distinguished from a calendar date

#### Scenario: The report serves as the word-notebook entry

- **WHEN** a visitor opens the overall report
- **THEN** they can open any of Stories 001–005, search the full word list, and view word entries in week, Day, and original daily-ordinal order
- **AND** only available printable PDFs are linked

#### Scenario: The report is discoverable from Miller Words

- **WHEN** a visitor opens the Miller Words Thing entry
- **THEN** they can follow a clearly labeled overall-report link that is separate from the individual episode HTML/PDF actions

### Requirement: Overall statistics are extensible and accessible

The overall report SHALL consume structured aggregate data that can include future sessions without changing individual episode templates, and every visual statistic SHALL have an equivalent text representation.

#### Scenario: A future session is added

- **WHEN** a new session record is added to the report data
- **THEN** the overall totals and daily/session history can be updated without adding statistics markup to a story episode

#### Scenario: A visitor uses a narrow viewport or assistive technology

- **WHEN** a visitor views the report on mobile or with a screen reader
- **THEN** the statistics remain readable, and chart values are available through semantic text or a table
