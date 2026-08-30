# Miller Words

A small, repeatable vocabulary practice for words Miller discovers while reading.

## Folder layout

```text
miller-words/
├── README.md                  # Workflow and design principles
├── prompts.md                # Copy-ready prompts for the three-step workflow
├── words.md                   # Canonical word list; list is always section 1
├── raw/                       # Unedited photos of Miller's handwriting
├── cartoon/                   # Memory pictures generated from the practice story
├── practice/
    ├── story-001.md           # Natural sentences and picture-based activities
    └── review-log.md           # Lightweight retrieval-practice record
├── output/
    ├── html/story-001.html    # Browser-friendly version
    └── pdf/story-001.pdf      # Print version, two scenes per page
└── scripts/
    └── make_story_pdf.py      # Rebuilds the printable PDF
```

## Workflow for each reading session

1. Miller writes down unfamiliar words while reading.
2. Take one clear photo and save it in `raw/`, using a date in the filename for future sessions.
3. Add a clean transcription to the first section of `words.md`. Preserve the original spelling and day number; do not silently guess a meaning.
4. Resolve ambiguous meanings with the sentence from the book when possible.
5. Add a short story using the words in natural English. Use several short sentences rather than one long sentence that merely forces every word in.
6. Generate one picture per scene. Use pictures as recall cues, then practice once without labels.
7. Ask Miller to recall and say the sentences aloud. Correct gently, then revisit the same words after 1, 3, 7, and 14 days.
8. Open the HTML for screen practice or print the PDF. The PDF uses two scenes per page.

## Design principles

- The goal is not only recognition. Miller should be able to understand, say, and use each word.
- Keep a daily new-word load small: about 5–8 words, with older words mixed in.
- Prefer phrases and collocations: **hide-and-seek**, **fish tank**, **a ray of light**, **take a bow**, **by myself**.
- Keep Chinese support available, but hide it during recall. English first, translation as a check.
- Generated pictures should make the scene memorable, not replace reading. Remove labels for the final recall round.
# miller-words
