## Purpose

Give Miller's vocabulary practice a stable, public-facing home in the personal site while preserving the generated story as a useful screen experience and printable activity.

## ADDED Requirements

### Requirement: Visitors can discover Miller Words from the Things archive

The personal site SHALL expose a published Miller Words entry in the Things archive with a stable, navigable URL.

#### Scenario: Miller Words appears in the Things archive

- **WHEN** a visitor opens the published Things archive
- **THEN** they can identify and follow a Miller Words entry without knowing the underlying asset filename

#### Scenario: Direct Miller Words URL loads

- **WHEN** a visitor navigates directly to the Miller Words entry URL
- **THEN** the page loads successfully as part of the static site

### Requirement: Visitors can view the Miller Words HTML story

The Miller Words entry SHALL provide a clear link to a browser-viewable Story 001 HTML experience containing the supplied story content, word-practice activity, and scene illustrations.

#### Scenario: Visitor opens the HTML story

- **WHEN** a visitor selects the view-story action
- **THEN** Story 001 opens as HTML in the browser with readable story sections and its included illustrations

#### Scenario: HTML story works on a narrow viewport

- **WHEN** a visitor opens the HTML story on a mobile-sized viewport
- **THEN** the story remains readable and usable without requiring horizontal scrolling for ordinary content

### Requirement: Visitors can download the Miller Words PDF

The Miller Words entry SHALL provide an explicit, accessible download action for the supplied Story 001 PDF.

#### Scenario: Visitor downloads the print version

- **WHEN** a visitor selects the PDF download action
- **THEN** the browser receives the Story 001 PDF rather than an HTML error page

#### Scenario: Download action identifies its format

- **WHEN** assistive technology or a keyboard user encounters the PDF action
- **THEN** the link has an accessible name that identifies it as a PDF download
