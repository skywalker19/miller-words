# Miller Words

A small, repeatable vocabulary practice for words Miller discovers while reading.

## 单词本入口

打开 [Miller 的单词本总报告](output/html/miller-words-report.html)：Story 001–005、Day 1–30 的每日统计、五个周次的统计，以及可搜索的完整词表都在这里。当前 140 条词条记录、139 个不同词形、22 个故事场景。

[Memory Exam · 单词配对](output/html/miller-words-report.html#memory-exam) 是总览中的独立板块，涵盖全部 139 个不同词形。可选择全部故事、一篇故事或某个 Day，每轮最多 8 对，优先练习未配对正确的词。答对记录只保存在当前浏览器，沿用同一浏览器内原 Story 001 的记录；“重置本范围记录”仅清除当前范围的词。配对正确不等同于已经掌握，还应读出单词、复述故事或造句。

也可以直接打开项目根目录的 [index.html](index.html)。

更新 `words.md` 和故事后，运行 `python3 scripts/make_overall_report.py`，即可重建报告、四篇新故事网页和网站同步文件。报告数据保存在 `output/data/miller-words-report.json`。网站文件在 `output/site-staging/` 准备完成后，用 `python3 scripts/sync_personal_site_report.py` 同步到个人网站工作区；该操作不发布网站。

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
    ├── html/miller-words-report.html # Stories, daily/weekly counts, shared Memory Exam
    ├── html/story-001.html    # Story and link to matching practice
    └── pdf/story-001.pdf      # Print version, two scenes per page
├── scripts/
│   └── make_story_pdf.py      # Rebuilds the printable PDF
├── openspec/                  # Spec-driven change planning
└── .agents/skills/            # OpenSpec skills for Codex
```

## Workflow for each reading session

当前练习入口：[单词本总报告](output/html/miller-words-report.html) · [故事目录](practice/README.md) · [Day 9–30 图片总览](output/html/story-002-005-images.html)。

1. Miller writes down unfamiliar words while reading.
2. Take one clear photo and save it in `raw/`, using a date in the filename for future sessions.
3. Add a clean transcription to the first section of `words.md`. Preserve the original spelling and day number; do not silently guess a meaning.
4. Resolve ambiguous meanings with the sentence from the book when possible.
5. Add a short story using the words in natural English. Use several short sentences rather than one long sentence that merely forces every word in.
6. Generate one picture per scene. Use pictures as recall cues, then practice once without labels.
7. Ask Miller to recall and say the sentences aloud. Correct gently, then revisit the same words after 1, 3, 7, and 14 days.
8. Open a story for screen practice, then use the overall report's Memory Exam to match words from any story or Day. Correct matches are remembered in that browser. Story 001 also has a printable PDF with two scenes per page.

## Design principles

- The goal is not only recognition. Miller should be able to understand, say, and use each word.
- Keep a daily new-word load small: about 5–8 words, with older words mixed in.
- Prefer phrases and collocations: **hide-and-seek**, **fish tank**, **a ray of light**, **take a bow**, **by myself**.
- Keep Chinese support available, but hide it during recall. English first, translation as a check.
- Generated pictures should make the scene memorable, not replace reading. Remove labels for the final recall round.
