# RRL Naming Conventions

Naming rules for the curated corpus. A paper has three artefacts, each named
differently:

| Artefact | Name | Lives in |
|----------|------|----------|
| stem (stable id) | `{Prefix}--{AuthorLastName}-{Year}{LetterSuffix}` | `paper_id`; the note filename |
| PDF | first author and year, e.g. `Bunyi, 2024.pdf` | `literature/pdfs/` (fetched, gitignored) |
| conversion | the PDF name plus `_marked.md` | `literature/mds/` |

The stem is **not** derivable from the PDF or conversion filename. The binding
between a stem and its files is recorded in `literature/mds/metadata.json`
(`source_pdf`, `source_pdf_path`, `conversion_md`); resolve a stem through that
sidecar, never by guessing a filename.

## Source Prefixes

The prefix is part of the stem and marks geographic/institutional origin.

| Prefix | Meaning | Example stem |
|--------|---------|--------------|
| `L--` | Local (Philippine) | `L--Cuevas-2023` |
| `I--` | International | `I--Smith-2024` |
| `A--` | Algorithm/system focus | `A--Lu-2025` |
| `AI--` | Algorithm + international | `AI--Transformer-Anomaly` |
| `IA--` | International + algorithm (legacy) | `IA--Gradient-Boosting` |
| `AL--` | Algorithm + local (legacy) | `AL--RF-Profiling` |
| `LA--` | Local + algorithm (legacy) | `LA--Isolation-Forest` |

**Convention**: use `L--`, `I--`, or `A--` for new papers. The compound prefixes
exist in legacy files only; their order is inconsistent across older entries.

## Stem Format

```
{Prefix}--{AuthorLastName}-{Year}{LetterSuffix}
```

Examples:
- `L--Cuevas-2023` — Philippine paper by Cuevas, 2023
- `I--Yang-2024b` — international paper by Yang, 2024, second of multiple
- `A--Lu-2025` — algorithm-focused paper by Lu, 2025

The `LetterSuffix` (a, b, c...) separates papers that share an author and year.
The stem names the note; it is also the note's `paper_id`, and it must end in the
paper's year (the builder checks this against the sidecar).

## PDFs

Fetched into `literature/pdfs/` (gitignored), flat. A PDF is named for its first
author and year, which keeps it recognisable without the sidecar:

- one author: `Bunyi, 2024.pdf`
- two authors: `Claro & Noval, 2025.pdf`
- three or more: `DSouza et al., 2026.pdf`
- corporate author: `Bangko Sentral ng Pilipinas, 2026a.pdf`

Fresh downloads land in `bucket/` at the repo root and are triaged into
`literature/pdfs/` (see `docs/standards/rrl-workflow.md`).

## Conversions

`scripts/prepare_pdf.py` converts a PDF to `{pdf-name}_marked.md` with a
frontmatter block recording the source PDF's SHA-256 and page count. Conversions
live flat in `literature/mds/`, and their names are recorded per stem in the
sidecar. Do not rename a conversion without updating `metadata.json`.

## Authored Extraction Note Naming

A note takes the stem as its filename, in `review/notes/`:

```
review/notes/{stem}.md
```

Example: `review/notes/A--Lu-2025.md`. Calling scripts locate a note from the
stem, so it is the note — not the conversion — that carries the stable id.

The note grammar is specified in `docs/standards/note-format.md`.

## Legacy Suffixes

The following suffixes are retired and must not be produced for new files:

| Suffix | Legacy meaning |
|--------|---------------|
| `_summarized.json` | Structured JSON summary, retired 2026-10-01 in favour of the note |
| `_summarized.yaml` | YAML summary (pre-v6.0) |
| `_summarized.md` | Markdown summary (pre-v6.0) |
