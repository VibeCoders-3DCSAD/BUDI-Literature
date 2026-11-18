# review/

The review surface for the RRL corpus. Two halves, and the difference matters:
most of this directory is **generated**, and only two places are **authored**.

## Generated — never hand-edit

Rebuild with `python3 scripts/build_matrix.py` and
`python3 scripts/build_summary_tables.py`.

| File | Contents |
| :--- | :--- |
| `literature-review-matrix.md` | 15-column index over the corpus |
| `validation.md` | Errors and informational gaps from the last build |
| `data/papers.csv` | One row per paper, the matrix columns plus `tags` |
| `data/screening.csv` | Intake triage: status, module count, metadata completeness |
| `data/quotes.csv` | One row per extracted quotation |
| `data/effects.csv` | One row per statistical result |
| `data/themes.csv` | Per-module coverage tally |
| `summary/related-literature.md` | Chapter 2 table of contextual works |
| `summary/related-studies.md` | Chapter 2 table of primary studies |

## Authored — the builder never overwrites these

| Path | Contents |
| :--- | :--- |
| `notes/{paper_id}.md` | One extraction note per paper. The note is the source of truth for modules, quotes, and results; the builder writes a stub only when a note is missing. |
| `synthesis/` | Cross-paper synthesis |

## Authored analysis

| File | Contents |
| :--- | :--- |
| `references-reconciliation.md` | How the corpus lines up with `Base/references/references.md`, and what is still unsourced |
| `citation-substantiation-ch2.md` | Citation checks behind the Chapter 2 claims |
| `bucket-triage.md`, `thin-note-triage.md` | Intake and extraction triage records |

## Verifying

```bash
python3 scripts/build_matrix.py --check   # exit 1 on any error
```

Gaps are informational: a module with no papers is a gap in the corpus, and a
paper with no module is an unfinished extraction. Only errors mean the corpus
contradicts itself.
