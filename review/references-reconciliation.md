# Corpus coverage against the canonical reference list

**Checked:** 2026-11-18
**Reference list:** `Base/references/references.md` (63 entries)
**Corpus:** `literature/mds/` + `review/notes/` (53 papers)
**Builder:** `scripts/build_matrix.py --check` — 0 errors, 12 informational gaps

This file records how the Literature corpus lines up with the reference list the
chapters cite, and what the last repair changed. It is authored, not generated;
regenerate the numbers with `scripts/build_matrix.py --check` if the corpus moves.

---

## State after the repair

| Measure | Value |
| :--- | :--- |
| Papers in `metadata.json` | 53 |
| Conversions in `literature/mds/` | 53 |
| Authored notes in `review/notes/` | 53 |
| Notes the builder recognised before the repair | 7 |
| Notes it recognises now | 53 |
| Papers extracted | 51 |
| Taxonomy modules covered | 19 of 19 |
| Builder errors | 0 |

The repair was a filename fix, not a content change. A previous pass renamed the
notes to citation style (`Adams et al., 2022.md`), but the builder resolves a note
as `review/notes/{paper_id}.md`, so 46 of the 53 notes were invisible and the
matrix reported 7 extracted papers and 14 of 19 modules. Every note already
carried its `paper_id` in frontmatter, so the 46 files were renamed back to
`{paper_id}.md` and nothing else in them changed. The matrix, the five CSVs, and
the two Chapter 2 summary tables were rebuilt from the corrected corpus.

Conversion files are named by author and year, which is the documented convention:
each is mapped back to its stem through the sidecar's `conversion_md` field, so
their names are independent of the note names and were left alone.

---

## References with no corpus source

Ten entries are cited in Chapters 1 to 3 but have no PDF, conversion, or note.
They arrived with the pass that sourced the SARIMA and IQR thresholds, and they
are the definitional citations behind the error metrics and the directional test.

| Reference | Cite as | Used for |
| :--- | :--- | :--- |
| Arumugam & Natarajan (2023) | Arumugam & Natarajan, 2023 | Theil's U2 applied to SARIMA |
| Bürgi (2025) | Bürgi, 2025 | directional-accuracy testing |
| Dobos et al. (2023) | Dobos et al., 2023 | IQR compared with other detectors |
| Hewamalage et al. (2023) | Hewamalage et al., 2023 | naive and seasonal-naive baselines, MASE |
| Hyndman & Koehler (2006) | Hyndman & Koehler, 2006 | MASE definition |
| Lewis (1982) | Lewis, 1982 | SMAPE interpretation bands |
| Pesaran & Timmermann (1992) | Pesaran & Timmermann, 1992 | directional-accuracy significance |
| Powers (2011) | Powers, 2011 | precision, recall, F1 definitions |
| Pradipta et al. (2024) | Pradipta et al., 2024 | Lewis bands in a recent SARIMA study |
| Theil (1966) | Theil, 1966 | Theil's U2 statistic |

All ten are marked `[verified]` in the reference list, so their metadata is
already settled; what is missing is the source document and therefore the note.
Adding them would give the corpus a `model_performance_evaluation` source for
every metric the chapters use, which is the weakest part of the current coverage.

## The Bangko Sentral lettering — settled

The Chapter 3 reference list is the authority, and the corpus stems already
match it. No rename is needed.

| Note | Document | Label |
| :--- | :--- | :--- |
| `L--BangkoSentral-2025` | 2025 Consumer Finance and Inclusion Survey | BSP (2025) |
| `L--BangkoSentral-2026a` | Consumer Expectations Survey, Q2 2026 | BSP (2026a) |
| `L--BangkoSentral-2026b` | Q1 2026 Report on Economic and Financial Developments | BSP (2026b) |

The suffixes follow publication year, and alphabetical title order within 2026.
The 2025 survey takes no letter. `Base/references/references.md` and
`Base/references/citation-map.csv` were corrected to this scheme on 2026-11-18;
the retired labels are recorded in `Base/references/bsp-mapping.md`.

The builder still reports a duplicate-year gap on `L--BangkoSentral-2026a` /
`2026b`, which is expected: both carry `year: 2026` because the disambiguating
letter lives in the stem, not the year field.

## Remaining gaps in the corpus itself

| Gap | Count | Detail |
| :--- | :--- | :--- |
| Papers with no module assignment | 2 | `I--Bangor-2008`, `I--Hnatkowska-2022` |
| Entries with no DOI in `metadata.json` | 29 | Reports, theses, and book chapters without one |
| Papers whose note records a self-contradiction | 8 | Reported as informational; the extractor keeps both figures with locators |

None of these is an error. The two unassigned papers are cited in Chapter 3 for
the SUS benchmark and for rule-compatibility checking, so they belong in the
corpus even before they carry modules; assigning `model_performance_evaluation`
to both would be defensible, but the module is a claim about where the paper sits
in the outline, so it is left to the extraction pass that reads them.

## What this means for sourcing

The corpus matches the reference list exactly except for the ten metric sources
above. It does not need pruning: all 53 papers map to a cited work, and all three
BSP reports are cited in Chapters 1 and 2.
