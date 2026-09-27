# Outline V4 Coverage Analysis

Generated 2026-09-26 by re-scoring the 91-paper corpus against `config/modules.yaml`
after it was realigned to Topical Outline V4 (`GROUP4 - TOPICAL OUTLINE - V4 - 09.26.26.docx`).

Thresholds: crucial >= 0.45, supporting >= 0.30.

How many corpus papers clear each threshold for each required leaf. This is the first
measurement of whether the corpus can actually support the current outline, rather than a
judgement about it.

| Module | Outline V4 leaf | Crucial | Supporting | Best match |
|---|---|---:|---:|---|
| `agile_methodology` | Agile lifecycle + Kanban **0** | 0 | 1 | `L--Santiago-2025` (0.401) |
| `system_evaluation` | System Evaluation (SUS + ISO/IEC 25010) **0** | 0 | 1 | `L--Santiago-2025` (0.358) |
| `seasonal_expense_forecasting` | Seasonal Expense Forecasting **0** | 0 | 9 | `I--Ganong-2025` (0.429) |
| `forecasting` | SARIMA forecasting | 3 | 19 | `A--SinghU-2025` (0.492) |
| `budget_recommendation` | Budget Creation / constraint optimization | 3 | 20 | `A--Gulbakyt-2025` (0.493) |
| `financial_profile_classification` | Saver/Borrower Profile Classification | 3 | 61 | `L--Francisco-2026` (0.487) |
| `filipino_context` | Philippine financial problems in planning | 4 | 19 | `L--Atento-2025` (0.493) |
| `pfms_systems` | Personal Financial Management Application | 6 | 33 | `I--Yadav-2026` (0.524) |
| `performance_indicators` | Performance Analysis indicators | 6 | 49 | `I--Yadav-2026` (0.495) |
| `anomaly_detection` | Unusual Expense Detection | 7 | 21 | `A--Zhong-2025` (0.534) |
| `financial_planning` | Financial Planning (now the central concept) | 7 | 42 | `I--Yeo-2023` (0.554) |
| `ml_algorithms` | Models and algorithms (general) | 14 | 36 | `A--Sireesha-2026` (0.539) |

## Leaves the corpus cannot support at all

3 of 12 required leaves have **zero** papers at crucial tier:

- **Agile lifecycle + Kanban** (`agile_methodology`) — 1 supporting, best match `L--Santiago-2025` at 0.401, below the 0.45 floor.
- **System Evaluation (SUS + ISO/IEC 25010)** (`system_evaluation`) — 1 supporting, best match `L--Santiago-2025` at 0.358, below the 0.45 floor.
- **Seasonal Expense Forecasting** (`seasonal_expense_forecasting`) — 9 supporting, best match `I--Ganong-2025` at 0.429, below the 0.45 floor.

Three of these are hard requirements of the outline, and the gaps are not academic:

| Gap | Why it is a problem |
|---|---|
| **Seasonal Expense Forecasting** | This is the thesis's core technical claim. The chapter leans on Dasmariñas et al. (2024) for it seven times, and that paper is not in the corpus at all. The adviser's standard for a core algorithm is six to seven sources. |
| **Agile lifecycle and Kanban** | Outline V4 names both explicitly under Methodology. The single supporting paper is a budget system paper, not a methodology source. The chapter's Kanban paragraph currently has no citation at all. |
| **System Evaluation (SUS, ISO/IEC 25010)** | Outline V4 names both explicitly. One supporting paper. The chapter discusses the ISO quality model and the SUS instrument across four paragraphs with no methodology source behind either. |

## Consequences for the intake list

The intake list agreed on 2026-09-21 (Tjostheim, Rafiei, Hovakimyan & Bravo, Schwartz, BSP
CFIS 2025, Khashadourian & Harrison, Fenig & Petersen, Asebedo 2025) was derived against
Outline V3. Outline V4 removed the savings and debt product subtypes, TAM/UTAUT, and the SVM
classifier, so several of those eight now serve a leaf the outline no longer contains. They are
re-ranked in `docs/NEW-SCOPE-SOURCES.md`.

Reordering the intake by this analysis puts the three zero-coverage leaves first, ahead of the
topic gaps those eight were chosen for.


## Known corpus limitations (recorded 2026-09-27)

These are properties of the corpus itself rather than of any outline leaf, and they bound how far
the coverage numbers above can be trusted. The corpus is 92 papers after
`L--Dasmarinas-2024` was added on 2026-09-27.

### Metadata is verified for 26 of 92 entries

| `metadata_source` | Entries |
| --- | --- |
| `verified from PDF page 1 on 2026-09-26` | 23 |
| `verified from PDF page 1 on 2026-09-27` | 3 |
| `unverified (frontmatter only)` | 66 |

"Verified" means the title, authors, year, and venue were read off page 1 of the source PDF. The
remaining 66 carry conversion frontmatter only, so their venue and author block are whatever the
converter emitted. **Cite those on the strength of the source filename and nothing else.** This repo
has already retracted one false verification claim (`docs/NEW-SCOPE-SOURCES.md`, commit `75d4cbe`)
that asserted every DOI had been checked when two had been invented, so the bar is: a reference is
verified when the file is held and page 1 has been read, not when a string looks plausible.

83 of 92 entries have no DOI at all. Adding DOIs and completing page-1 verification is the single
largest outstanding metadata task.

Count the entries with `metadata.json` under `["entries"]`, not at the top level — the file wraps
everything in that key, and a flat count over it silently returns 1.

### 5 entries record an affiliation where a journal belongs

`A--DSouza-2026`, `I--Zhao-2025`, `L--Atento-2025`, `I--RSingh-2025`, and `I--Yoganandham-2025`
all carry `venue_unverified: true` in the sidecar. In the first three the recorded "venue" is an
institutional affiliation, so the publication outlet is unidentifiable and the paper is probably a
preprint or submission draft. `I--Yoganandham-2025` gives a journal name with no volume, issue, or
pages. `I--RSingh-2025` is worse: no authors, no title, no DOI, and an ambiguous byline, so it is
unusable until the PDF is re-read. None of these should count toward a leaf's source quota.

### Summarisation has not been done, so the scores are uncalibrated

**All 92 `_summarized.json` files are 0 bytes.** No paper has been summarised. The consequence is
visible in `scores/validation.md`: annotated-relevant counts are 0 of 92, both point-biserial
correlations are `nan`, and specificity is 0.022. Those are not broken numbers, they are the
arithmetic result of validating against an empty baseline.

`scores/index.json` ranks papers by TF-IDF, BM25, and MiniLM embedding similarity against
`config/modules.yaml` keywords. None of that is wrong, but it is unvalidated: the thresholds
(`crucial >= 0.45`, `supporting >= 0.30`) have never been checked against human judgement, and the
per-module rankings that drive every source-assignment decision in Chapter 2 rest on them.
Summarisation is deferred to a separate session; until then, treat a module's top-ranked paper as a
lead to verify rather than a settled answer.

This is also why the corpus is not self-consistent about titles: `scores/index.json` reports
`title: null` for all 92 entries because `score.py` reads the `_marked.md` frontmatter and not the
`metadata.json` sidecar. The sidecar is the citation authority.

### Sources cited in Chapter 2 that this corpus does not hold

Audited 2026-09-27 against the chapter's 30 references. Six resolve to nothing in `conversions/`,
`papers/`, or `bucket/`, and were inherited from Chapter 2 V3, which did not hold them either:

| Cited as | Needed for |
| --- | --- |
| Brooke (1996) | System Usability Scale; the canonical source, and the chapter's only pre-2023 exception |
| Philippine Statistics Authority (2023) | FIES annual inputs to the Conceptual Model |
| Philippine Statistics Authority (2026) | HFCE seasonal proportions for temporal disaggregation |
| Ariningsih & Muhammad (2024) | PFM feature comparison |
| Lianto et al. (2023) | PFM feature comparison |
| Lim et al. (2025) | PFM features, usability |

`L--Dasmarinas-2024` was the seventh and is now held. The full audit is in
`BUDI-Base/thesis/paper/chapter-2-evidence-map.md`.

## Standing rule: verify against the corpus, not the chapter

A citation that is well-formed and internally consistent can still point at a paper the project does
not have. Six of Chapter 2's references did, for three chapters, because every check that had been
run compared the reference list against the body rather than against the corpus. Any reference
integrity check must resolve each entry to a file.
