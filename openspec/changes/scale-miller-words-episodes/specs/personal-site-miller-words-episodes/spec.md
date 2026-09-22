## Purpose

Provide a maintainable episode set for Miller Words so every vocabulary story exposes its browser HTML and printable PDF together, while future stories can be added through content data rather than page markup changes.

## ADDED Requirements

### Requirement: Miller Words episodes are represented as grouped resource pairs

The personal-site content model SHALL support an ordered set of Miller Words episodes, and each episode SHALL contain a stable identity, a display title, one browser-viewable HTML URL, and one downloadable PDF URL.

#### Scenario: Story 001 is represented as an episode

- **WHEN** the Miller Words content is loaded
- **THEN** Story 001 appears as one episode with its HTML and PDF resources associated with the same episode entry

#### Scenario: A future episode is added through content data

- **WHEN** an author adds another valid episode object to the Miller Words content
- **THEN** the site can render that episode without adding another hard-coded link block to the page template

#### Scenario: Invalid episode resources are rejected

- **WHEN** an episode is missing its identity, title, HTML URL, or PDF URL
- **THEN** the content validation reports an error rather than generating an incomplete episode entry

### Requirement: The Thing page presents episodes as a reusable set

The Miller Words Thing page SHALL render an episode section when episode data exists, with each episode's title and its HTML/PDF actions visually and semantically grouped together. Things without episode data SHALL retain their existing presentation.

#### Scenario: Multiple episodes are displayed as separate entries

- **WHEN** Miller Words contains two or more episodes
- **THEN** the page renders one distinct episode entry per episode in content order

#### Scenario: HTML and PDF actions remain paired

- **WHEN** a visitor views an episode entry
- **THEN** the browser-view HTML action and PDF-download action are adjacent within that episode's group and identify their formats

#### Scenario: A visitor uses keyboard navigation

- **WHEN** a visitor tabs through the episode set
- **THEN** each HTML and PDF action receives a visible focus state and can be activated without a pointer

### Requirement: Episode assets use self-contained public paths

Each published episode SHALL keep its generated HTML, PDF, and any episode-specific illustrations under a self-contained public asset directory, and the generated HTML SHALL load its illustrations from valid site-relative paths.

#### Scenario: Story 001 assets are isolated from future episodes

- **WHEN** the Story 001 assets are published
- **THEN** their HTML, PDF, and illustrations are stored under the Story 001 episode directory without relying on another episode's files

#### Scenario: Generated HTML illustration links resolve

- **WHEN** a visitor opens an episode's generated HTML
- **THEN** every illustration referenced by that HTML loads successfully from the personal site
