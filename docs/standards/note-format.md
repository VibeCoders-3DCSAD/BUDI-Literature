# Literature Note Format

A **note** is the extraction record for one paper. Notes are **authored** by the
extraction agent and live at `review/notes/{stem}.md`. They are the single
source of truth for everything the matrix reports about a paper except its
bibliographic record.

`scripts/build_matrix.py` reads notes. It never writes a note that already
exists; it only creates a stub for a paper that has none.

## The two-source rule

| Field group | Authority |
| :--- | :--- |
| `paper_id`, `title`, `authors`, `year`, `venue`, `doi` | `literature/conversions/metadata.json` — page-1 verified |
| designation | the stem prefix |
| everything else | the note |

Bibliographic values in a note's frontmatter are for the reader's convenience.
If they ever disagree with `metadata.json`, **the sidecar wins** and the
disagreement is a validation error. Never re-derive a title or a DOI from the
PDF, and never re-introduce the space in a line-broken DOI.

## Grammar

```markdown
---
paper_id: A--Aldrees-2025
first_author: Aldrees
year: 2025
title: "Behavioral Patterns in Micro-lending: ..."
venue: "International Journal of Computing and Intelligent Systems"
doi: 10.1007/s44196-025-00776-w
type: journal-article
designation: algorithm
status: extracted
modules: [rule_based_classification, model_performance_evaluation]
module_rationale:
  rule_based_classification: "Sect. 3 defines a five-branch threshold rule ..."
  model_performance_evaluation: "Sect. 4.1 reports holdout accuracy ..."
---

# Behavioral Patterns in Micro-lending: ...

`A--Aldrees-2025` — Aldrees (2025), *International Journal of Computing...*

## Summary
One or two sentences. Feeds the matrix `key_finding` column.

## Problem and Motivation
At most three sentences. No methodology.

## Method
**Design.** The paper's own design label, plus a note if it states none.
**Sample.** N and unit together.
**Context.** geography: ...; population: ...; setting: ...
- One approach step per bullet, in the order the paper presents them.

## Software
- Named tool (version, if printed)

## Key Findings
- num: A quantitative finding, with the number exactly as printed.

## Key Figures and Tables
- Figure 3: description → takeaway

## Limitations and Gaps
- The paper's single most significant limitation. This bullet alone feeds the
  matrix `gap` column; it is not a summary of the ones below it.
- Every other limitation, authors' own first where they acknowledge it.

## Definitions
- **Term** — the paper's definition

## Key Equations
- `equation` — explanation in at most 15 words

## Statistical Evidence
| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| New risk detection, proposed CFM-LPA | accuracy | 95.21% | — | — | Table 3, p. 21 |

## Quotes
| Text | Locator | Module |
| :--- | :--- | :--- |
| "verbatim quotation, at most 40 words" | Abstract, p. 1 | rule_based_classification |

## Remember This
- At most 20 words each, 3 to 5 items.

## Cited Works
- Author (year) (role) — the claim attributed to them [locator]

---
Conversion: [`A--Aldrees-2025_marked.md`](../../literature/conversions/A--Aldrees-2025_marked.md)
```

## Frontmatter

| Key | Rule |
| :--- | :--- |
| `paper_id` | Required. Must equal the file's stem. |
| `status` | Required. `extracted` or `not extracted`. |
| `modules[]` | Required when `status: extracted`. Ids copied verbatim from `config/taxonomy.yaml`. May be `[]` only with a stated reason. |
| `module_rationale` | Required when `status: extracted`. Exactly one clause per id in `modules[]`, no id absent from `modules[]`. |
| `type` | Optional. A controlled label; `metadata.json` `publication_type` takes precedence. |
| `first_author`, `year`, `title`, `venue`, `doi`, `designation` | Optional, informational. The sidecar wins on any disagreement. |

## What the builder reads, and from where

| Matrix column / table | Source in the note |
| :--- | :--- |
| `modules` | frontmatter `modules[]` |
| `section` | derived from `modules[]` via the taxonomy |
| `design` | the `**Design.**` line in `## Method` |
| `sample` | the `**Sample.**` line in `## Method` |
| `key_finding` | the first paragraph of `## Summary` |
| `gap` | the first bullet of `## Limitations and Gaps` |
| `data/quotes.csv` | the `## Quotes` table |
| `data/effects.csv` | the `## Statistical Evidence` table |
| `status` | frontmatter `status` |

Everything else in the note — problem, method steps, software, findings,
figures, definitions, equations, remembered points, cited works — exists for the
reader. The builder ignores it. That asymmetry is deliberate: the note is a
document first, a data source second.

## Required sections

`## Summary`, `## Method` (with both a `**Design.**` and a `**Sample.**` line),
`## Limitations and Gaps` (at least one bullet), `## Statistical Evidence`, and
`## Quotes` must all be present for a note with `status: extracted`.

`## Statistical Evidence` and `## Quotes` must state absence explicitly rather
than being dropped. A paper that reports no statistics, or that offers no
quotation worth keeping, writes the single line `Not reported.` under the
heading. Omitting the heading silently and letting the builder infer emptiness
is a validation error, because a missing section and an empty one are different
claims.

Optional, omit when the paper says nothing: `## Problem and Motivation`,
`## Software`, `## Key Findings`, `## Key Figures and Tables`, `## Definitions`,
`## Key Equations`, `## Remember This`, `## Cited Works`.

## Tables

Both tables have a fixed header. A note whose table header does not match
exactly is a validation error, not a best-effort parse.

- `## Statistical Evidence` — `Outcome`, `Metric`, `Value`, `CI`, `p`, `Locator`
- `## Quotes` — `Text`, `Locator`, `Module`

Cell rules:

1. **Never a raw `|`.** Write `\|`. Statistical notation produces pipes often
   enough that this is not hypothetical.
2. **No newlines inside a cell.** One record per row, always.
3. **Empty or `—`** for a CI or p-value the paper does not print. Never guess
   one, and never write `0`.
4. **Numbers exactly as printed.** No rounding, no unit conversion, no
   recomputation.
5. **`Outcome` must distinguish rows.** A comparison table legitimately reports
   `accuracy` four times, once per model. Write
   `"New risk detection, proposed CFM-LPA"`, not `"New risk detection"`.
6. **`Text` is verbatim**, in straight double quotes, at most 40 words. The
   outer quotes are added by the format and stripped on parse.
7. **`Module` is a taxonomy id**, so quotes and paper assignments stay
   comparable. A quote may be filed under a module the paper as a whole is not
   assigned to, when the quote is what establishes the fit.

## Contradictory figures

When a paper reports the same measurement twice with different numbers, keep
**both** rows with their distinct locators, and describe the contradiction in
`## Limitations and Gaps`. Never reconcile silently and never pick a winner.

`A--Aldrees-2025` is the worked example: 14.03% in the abstract against 14.82%
in the conclusion, both genuine, both kept.

## Missing values

| Situation | Value |
| :--- | :--- |
| Paper does not report it | `Not reported` |
| Does not apply to this design | `Not applicable` |
| Present but genuinely ambiguous | `Unclear: <one-clause reason>` |
| Known unreliable in the source | `Unverified: <reason>` |

Never blank, never `N/A`, never `unknown`, never `-`.

## Stubs

`build_matrix.py` writes a stub for any paper with no note file. A stub carries
`status: not extracted` and says so in the body. It is a generated placeholder:
once you extract the paper, **replace the whole file** with a full note. The
builder will not overwrite a note you wrote, and it does not distinguish a stub
from an authored note beyond `status` — so do not edit a stub in place, write
the note as a new file.

## Validation

Errors, per note:

- frontmatter missing, unparseable, or without `paper_id` and `status`
- `paper_id` disagrees with the file stem
- a module id absent from `config/taxonomy.yaml`
- `module_rationale` and `modules[]` do not correspond exactly
- a required section missing
- a table header that does not match exactly
- a row with the wrong number of cells
- an unknown `status` value
- `status: extracted` with no `## Summary` paragraph, no `**Design.**` line, no
  `**Sample.**` line, or no limitations bullet

Gaps, informational: a module with no papers, a paper with no module, a missing
DOI, an unverified venue, an absent publication type, fill-rate verdicts
suppressed while fewer than 10 papers are extracted.

## Superseded

`summary-format.md` specified the retired `_summarized.json` extraction schema
and is kept as `summary-format_OLD.md`. The JSON files are gone; this document
replaces them.
