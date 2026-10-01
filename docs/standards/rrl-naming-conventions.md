# RRL Naming Conventions

File naming rules for the curated corpus in `literature/conversions/`.

## Source Prefixes

Every curated paper file uses a prefix to indicate geographic/institutional origin.

| Prefix | Meaning | Example |
|--------|---------|---------|
| `L--` | Local (Philippine) | `L--Cuevas-2023.pdf` |
| `I--` | International | `I--Smith-2024.pdf` |
| `A--` | Algorithm/system focus | `A--LSTM-Spending-Forecast.pdf` |
| `AI--` | Algorithm + international | `AI--Transformer-Anomaly.pdf` |
| `IA--` | International + algorithm (legacy) | `IA--Gradient-Boosting.pdf` |
| `AL--` | Algorithm + local (legacy) | `AL--RF-Profiling.pdf` |
| `LA--` | Local + algorithm (legacy) | `LA--Isolation-Forest.pdf` |

**Convention**: Use `L--`, `I--`, or `A--` for new papers. The compound prefixes (`AI--`, `IA--`, `AL--`, `LA--`) exist in legacy files only; prefix order is inconsistent across older entries.

## Processing Suffixes

Each paper has up to three files, distinguished by suffix:

| Suffix | Meaning | Location |
|--------|---------|----------|
| `.pdf` | Source paper PDF | `literature/papers/` (fetched, gitignored) |
| `_marked.md` | Markdown conversion with YAML frontmatter | `literature/conversions/` |
| `.md` (no suffix) | Authored extraction note | `review/notes/` (same `{stem}` as the conversion) |

### Legacy Suffixes

The following suffixes are retired and should not be produced for new files:

| Suffix | Legacy Meaning |
|--------|---------------|
| `_summarized.json` | Structured JSON summary, retired 2026-10-01 in favour of the note |
| `_summarized.yaml` | YAML summary (pre-v6.0) |
| `_summarized.md` | Markdown summary (pre-v6.0) |

## File Stem Format

```
{Prefix}--{AuthorLastName}-{Year}{LetterSuffix}
```

Examples:
- `L--Cuevas-2023.pdf` — Philippine paper by Cuevas, 2023
- `I--Smith-2024a.pdf` — International paper by Smith, 2024, first of multiple
- `A--LSTM-Spending-Forecast.pdf` — Algorithm-focused paper (no author-based stem)

The `LetterSuffix` (a, b, c...) is used when multiple papers share the same author and year.

## Extraction Note Naming

A note takes the same stem as the conversion, with a plain `.md` extension in a
different directory:

```
literature/conversions/{stem}_marked.md   ->   review/notes/{stem}.md
```

Example: `review/notes/A--Cuevas-2023.md`

The note grammar is specified in `docs/standards/note-format.md`.
