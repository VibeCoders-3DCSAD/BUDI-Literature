# Suggestions to Improve Literature Review Matrix

> **Status: implemented 2026-09-30.** The advice below was taken. Deviations are
> listed under [What was actually built](#what-was-actually-built); everything
> else here is the original proposal, kept for rationale.
>
> | Original suggestion | What exists now |
> | --- | --- |
> | `refs.bib` as canonical metadata | `literature/conversions/metadata.json` — page-1 verified, already the corpus sidecar |
> | `data/papers.csv` | `docs/literature-review-matrix.md`, 17 columns, **generated** |
> | `data/quotes.csv` | `scores/quotes.json` (34 records) |
> | `data/effects.csv` | `scores/effects.json` (44 records) |
> | `notes/*.md` per paper | `{stem}_summarized.json` — the pipeline's existing summary format, extended |
> | `scripts/build_matrix.py` | `scripts/build_matrix.py` + `--check` validator |
> | Separate `lit-review/` tree | Rejected: duplicates `literature/conversions/`, splits the citation authority, and breaks the naming convention |
> | `data/themes.csv` | Deferred; the matrix emits a per-module theme count for now |
> | CSV + pandas | JSON + stdlib `json`; the repo already gitignores `*.csv` and pandas is not a dependency |
> | Zotero / Obsidian / Airtable | Rejected: the corpus is agent-driven, and a closed format needs a generator to stay consistent |
>
> Column definitions and every validation rule: `docs/standards/matrix-format.md`.

Don’t scale the 56-column Markdown table as-is. At 94 papers, it will become a huge sparse table: hard to read, hard to diff, hard to query, and full of duplicated metadata. You don’t need to abandon the matrix — make it a **lean generated view** over a few normalized sources.

## Recommended structure

Use the matrix as an index, not the database:

```text
lit-review/
  refs.bib                     # canonical bibliographic metadata
  data/
    papers.csv                 # core matrix: 10–20 columns
    screening.csv              # include/exclude + reason
    extraction.csv             # optional moderate extraction
    quotes.csv                 # one row per quote
    effects.csv                # one row per statistical result/effect size
    themes.csv                 # synthesis by theme
  notes/
    abdullahi2025.md
    aldrees2025.md
  synthesis/
    themes.md
    methods.md
    gaps.md
  scripts/
    build_matrix.py
  literature-review-matrix.md  # generated/index file
```

The key idea: keep **bibliographic metadata** in `refs.bib`, **short core data** in `papers.csv`, and **long details** in per-paper notes or long tables.

## Keep the core matrix lean

Aim for something like 15–20 columns max:

| paper_id | citekey | author_year | title | type | venue | year | doi | tags | design | sample | key_finding | gap | relevance | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Move these out of the matrix:

- `Full_Citation`, `All_Authors`, `DOI`, `URL`, `ISBN_ISSN` → `refs.bib`
- `Direct_Citations_Statements` → `quotes.csv`
- `Statistical_Evidence`, `Effect_Sizes` → `effects.csv`
- `Methodology`, `Data_Collection`, `Sampling_Strategy`, `Limitations`, `Implications`, `Future_Research` → per-paper note
- `Topics`, `Themes`, `Keywords` → tags, not long lists
- `Hypotheses`, `Theoretical_Framework`, `Conceptual_Model` → note only if present

Many of your current columns are often “Not reported” or “Not applicable.” If a column is mostly empty, it doesn’t belong in the matrix.

## Use per-paper notes

One file per paper is much easier to maintain than one giant row. Example:

```yaml
---
paper_id: abdullahi2025
citekey: abdullahi2025systematic
authors: [Abdullahi, M., Alhussian, H., Aziz, N., ...]
year: 2025
title: A Systematic Literature Review of Concept Drift Mitigation in Time-Series Applications
type: journal-article
venue: IEEE Access
doi: 10.1109/ACCESS.2025.3587231
tags: [theme/concept-drift, method/SLR, context/time-series, method/ensemble]
status: included
---
## Summary
...

## Method
...

## Key findings
- SVM reported as most effective...
- Regression under-studied...

## Limitations/gaps
- Search limited to 2013–2024...
- Benchmark datasets may not reflect real-world data...

## Quotes
> “The findings show that Support Vector Machines...”

## Relevance to BUDGIE
...
```

Then link to it from the matrix with `[[abdullahi2025]]`.

## Use long tables for quotes and effects

Instead of cramming many quotes into one cell:

`quotes.csv`

| paper_id | page | quote | theme |
|---|---|---|---|
| abdullahi2025 | Abstract | “SVM is the most effective...” | methods/algorithm |

`effects.csv`

| paper_id | outcome | metric | value | CI | p | effect_size |
|---|---|---|---|---|---|---|
| aldrees2025 | risk detection | accuracy | 95.21% | ±2.1% | <0.05 | — |

This makes synthesis much easier and avoids giant Markdown cells.

## Use tags and controlled vocabulary

Instead of free-text topics/themes, use tags like:

- `theme/concept-drift`
- `theme/credit-risk`
- `method/SLR`
- `method/federated-learning`
- `context/micro-lending`
- `method/ensemble`

Create a `tags.md` data dictionary. For 94 papers, consistency matters more than detail.

→ Shipped as the four controlled namespaces in `docs/standards/matrix-format.md`:
`theme/<module_id>`, `method/<slug>`, `context/<slug>`, `quality/<slug>`. The matrix
shows the top five `theme/` tags per paper and appends `theme/+Nmore`; `method/` is
constrained to a fixed vocabulary with `method/other` as the escape hatch. The
builder rejects an unknown `type` and a tag outside those namespaces.

## Use the right tools

- **Zotero + Better BibTeX** — canonical citations, PDFs, annotations, citekeys.
- **Obsidian + Dataview** — per-paper notes with YAML frontmatter; generate the matrix automatically.
- **Airtable / Notion / SQLite** — if you want linked records: Papers, Authors, Findings, Quotes, Themes.
- **Python/Pandas** — validate DOIs, years, duplicates; generate `literature-review-matrix.md` from CSV/YAML.

Example Dataview query in Obsidian:

```dataview
TABLE year, venue, tags, status
FROM "notes"
WHERE status = "included"
SORT year DESC
```

## Migration plan

1. Freeze the current matrix. → done, `d7aeee5`
2. Create `refs.bib` from Zotero/DOIs. → superseded: `metadata.json` already exists and is verified
3. Define a 15–20 column core schema. → done, 17 columns
4. Create one note per paper. → done for 2 of 93 (`A--Abdullahi-2025`, `A--Aldrees-2025`); the other 91 are still 0 bytes
5. Move quotes to `quotes.csv`. → done, `scores/quotes.json`
6. Move statistics/effect sizes to `effects.csv`. → done, `scores/effects.json`
7. Generate the matrix from notes/CSV. → done, `scripts/build_matrix.py`
8. Build a separate thematic synthesis table for writing. → deferred

## What was actually built

The proposal was right about the diagnosis and mostly right about the shape, with
four substantive changes.

**The parallel tree was dropped.** A separate `lit-review/` directory would have
meant two places to look for a paper, a second bibliographic authority that could
drift from `metadata.json`, and stems that no longer follow
`docs/standards/rrl-naming-conventions.md`. Everything landed in the existing
`literature/conversions/` and `scores/` trees instead, so `scripts/common.py` and
the scoring pipeline keep working unchanged.

**Per-paper notes became summary JSON.** Markdown notes with YAML frontmatter are
pleasant to write by hand, but this repo already has a `_summarized.json` contract
that the pipeline reads. Adding a second per-paper format would mean the agent
writes one thing and the scorer reads another. The summary schema was extended
additively with `study_design`, `sample`, `context`, `software`, `quotes[]`, and
`effects[]`; existing summaries stay valid.

**Long tables are JSON, not CSV.** The repository `.gitignore`s `*.csv`, and adding
pandas for a 17-column projection is not worth it. `build_matrix.py` uses stdlib
`json`, plus the PyYAML the rest of the pipeline already depends on.

**A validator ships with the generator.** The proposal predicted that structured
data with validation would catch the DOI with a space and the abstract/conclusion
percentage mismatch. It does. `build_matrix.py --check` exits 1 on any error and
reports informational gaps separately, so the 42 missing DOIs and the 5 unverified
venues are visible without failing the build. It is wired into the workflow docs
as a required step after every extraction.

The result: 93 papers in 17 columns, 34 quotes and 44 effects in the long tables,
2 papers fully extracted, and 91 marked `not extracted` rather than absent — so the
coverage gap is legible in the matrix itself instead of being a set of empty files.


## If you must stay in pure Markdown

Then split it:

- `matrix-bibliographic.md`
- `matrix-methods.md`
- `matrix-findings.md`
- `matrix-limitations.md`

Each with `paper_id` and fewer columns. But even then, long text should live in notes, not table cells.

## Bottom line

You don’t need a 56-column table. Use a **tiered system**:

1. `refs.bib` for citation metadata.
2. `papers.csv` for a lean core matrix.
3. `notes/*.md` for detailed extraction.
4. `quotes.csv`, `effects.csv` for long/quantitative evidence.
5. `themes.csv` or `synthesis.md` for writing.

This scales to 94+ papers and keeps the matrix readable. I also noticed a couple of inconsistencies in your sample rows — e.g., a DOI with a space and abstract vs conclusion percentages differing. A structured system with validation would catch those automatically.

Both were caught. The DOI with a space is a validator error; the percentage
mismatch in `A--Aldrees-2025` is preserved rather than resolved, because the paper
genuinely reports 14.03%/13.28% in its abstract and 14.82%/13.63% in its
conclusion. The validator flags the conflict, and `limitations` records it. Choosing
one pair would have made the matrix tidier and the literature wrong.