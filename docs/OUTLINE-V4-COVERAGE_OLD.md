> **Deprecated.** This document is superseded by `review/data/themes.csv` and the
> coverage table in `review/literature-review-matrix.md`.
> Retained for historical reference only.
>
> The per-leaf counts below were computed by scoring the corpus against
> `config/modules.yaml` (22 modules, weights, crucial/supporting tiers). Both the
> module namespace and the scoring stage are retired. Coverage is now a count of
> the `modules[]` assignments made during extraction, and `themes.csv` regenerates
> that view on every build, so this file could only ever be stale. The counts
> below describe the corpus as of 2026-09-30 under the old taxonomy.

# Outline V4 Coverage Analysis

Originally generated 2026-09-26 by re-scoring the corpus against
`config/modules.yaml` after it was realigned to Topical Outline V4
(`GROUP4 - TOPICAL OUTLINE - V4 - 09.26.26.docx`). **Refreshed 2026-09-30**
against the 93-paper corpus, which now includes `L--Dasmarinas-2024` and
`A--DeyArefin-2025`.

Thresholds: crucial >= 0.45, supporting >= 0.30.

How many corpus papers clear each threshold for each required leaf. This is the first
measurement of whether the corpus can actually support the current outline, rather than a
judgement about it.

| Module | Outline V4 leaf | Crucial | Supporting | Best match |
|---|---|---:|---:|---|
| `agile_methodology` | Agile lifecycle + Kanban **0** | 0 | 1 | `L--Santiago-2025` (0.401) |
| `system_evaluation` | System Evaluation (SUS + ISO/IEC 25010) **0** | 0 | 1 | `L--Santiago-2025` (0.358) |
| `seasonal_expense_forecasting` | Seasonal Expense Forecasting **0** | 0 | 11 | `I--Ganong-2025` (0.429) |
| `forecasting` | SARIMA forecasting | 4 | 23 | `L--Dasmarinas-2024` (0.494) |
| `budget_recommendation` | Budget Creation / constraint optimization | 4 | 24 | `A--DeyArefin-2025` (0.491) |
| `financial_profile_classification` | Saver/Borrower Profile Classification | 3 | 65 | `L--Francisco-2026` (0.486) |
| `filipino_context` | Philippine financial problems in planning | 4 | 23 | `L--BangkoSentral-2023b` (0.493) |
| `pfms_systems` | Personal Financial Management Application | 6 | 40 | `I--Yadav-2026` (0.524) |
| `performance_indicators` | Performance Analysis indicators | 6 | 56 | `I--Yadav-2026` (0.495) |
| `anomaly_detection` | Unusual Expense Detection | 7 | 28 | `A--Zhong-2025` (0.535) |
| `financial_planning` | Financial Planning (now the central concept) | 7 | 50 | `I--Yeo-2023` (0.553) |
| `ml_algorithms` | Models and algorithms (general) | 15 | 51 | `A--Sireesha-2026` (0.540) |

## Leaves the corpus cannot support at all

3 of 12 required leaves have **zero** papers at crucial tier:

- **Agile lifecycle + Kanban** (`agile_methodology`) — 1 supporting, best match `L--Santiago-2025` at 0.401, below the 0.45 floor.
- **System Evaluation (SUS + ISO/IEC 25010)** (`system_evaluation`) — 1 supporting, best match `L--Santiago-2025` at 0.358, below the 0.45 floor.
- **Seasonal Expense Forecasting** (`seasonal_expense_forecasting`) — 11 supporting, best match `I--Ganong-2025` at 0.429, below the 0.45 floor.

Three of these are hard requirements of the outline, and the gaps are not academic:

| Gap | Why it is a problem |
|---|---|
| **Seasonal Expense Forecasting** | This is the thesis's core technical claim. The chapter leans on Dasmariñas et al. (2024) for it seven times. That paper joined the corpus on 2026-09-27 and is now its strongest match — but at 0.494 on `forecasting` and below the floor on `seasonal_expense_forecasting`, because the module keywords reward generic forecasting vocabulary over monthly-seasonal decomposition. One supporting paper is not the adviser's six to seven, and the leaf the outline names by that exact phrase is the one the paper does not hit. |
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


## Known corpus limitations (recorded 2026-09-27, refreshed 2026-09-30)

These are properties of the corpus itself rather than of any outline leaf, and they bound how far
the coverage numbers above can be trusted. The corpus is 93 papers after
`L--Dasmarinas-2024` was added on 2026-09-27 and `A--DeyArefin-2025` on
2026-09-30.

### Metadata is page-1 verified for all 93 entries

As of 2026-09-30 every entry in `metadata.json` records
`verified from PDF page 1`: 18 on 2026-09-26, 3 on 2026-09-27, and 72 on
2026-09-29. The earlier state of this document (26 of 92 verified, 66 carrying
conversion frontmatter only) is stale.

Verification means the title, authors, year, and venue were read off page 1 of the
source PDF. This repo has already retracted one false verification claim
(`docs/NEW-SCOPE-SOURCES.md`, commit `75d4cbe`) that asserted every DOI had been
checked when two had been invented, so the bar is: a reference is verified when
the file is held and page 1 has been read, not when a string looks plausible.

**51 of 93 entries still have no DOI.** Adding DOIs remains the single largest
outstanding metadata task; `scores/matrix-validation.md` reports the count on
every build.

Count the entries with `metadata.json` under `["entries"]`, not at the top level —
the file wraps everything in that key, and a flat count over it silently returns 1.

### 14 entries record an unverified venue

14 of 93 entries carry `venue_unverified: true` in the sidecar. They fall into two
groups, and neither should count toward a leaf's source quota.

**Nine have no venue at all**: `A--Begum-2025`, `A--Chahar-2026`,
`A--ChenTan-2025`, `A--John-2025`, `A--Olabintan-2026`, `A--Sappa-2024`,
`A--Sireesha-2026`, `I--Dheepiga-2025`, and `L--Salvador-2024`. Flagged during the
2026-09-29 verification pass; each still needs its outlet read off the PDF.

**Five name something that is not a publication outlet**:

| Stem | Recorded venue | Problem |
| --- | --- | --- |
| `A--DSouza-2026` | P.E.S Modern College of Engineering, Pune | An affiliation, not a journal. Preprint or submission draft. |
| `I--Yoganandham-2025` | Degres Journal, ISSN 0376-8163 | Journal name with no volume, issue, or pages. |
| `L--Abila-2026` | International Journal of Health and Business Analysis | Health-analytics journal on a Philippine personal-finance paper. Verify the outlet. |
| `L--Atento-2025` | International Journal of Health and Business Analysis | Same journal, same year, different paper. Plausible venue; authorship must be checked. |
| `L--Francisco-2026` | International Journal of Multidisciplinary Education… | Education journal on a saver/borrower classification study. Verify the outlet. |

Earlier revisions of this document also flagged `I--Zhao-2025` and
`I--RSingh-2025` here. Both were resolved by the 2026-09-29 pass: `I--Zhao-2025`
now carries a venue, and `I--RSingh-2025` — which had no authors, title, or DOI —
was renamed and re-read. They are no longer in the unverified set.

`build_matrix.py` renders an unverified venue with an `(Unverified)` suffix, prints
`Not reported` when there is no venue to render, and tags the paper
`quality/metadata-partial`. `scores/matrix-validation.md` lists the five renderable
cases on every build.

### Summarisation has barely started, so the scores are uncalibrated

**2 of 93 `_summarized.json` files are populated** (`A--Abdullahi-2025` and
`A--Aldrees-2025`, extracted 2026-09-30). The other 91 are still 0 bytes, so the
per-column fill-rate check in `scores/matrix-validation.md` stays suppressed until
10 papers are extracted. The consequence is still visible in
`scores/validation.md`: annotated-relevant counts are 0 of 93, both point-biserial
correlations are `nan`, and specificity is 0.022. Those are not broken numbers,
they are the arithmetic result of validating against a near-empty baseline.

`scores/index.json` ranks papers by TF-IDF, BM25, and MiniLM embedding similarity
against `config/modules.yaml` keywords. None of that is wrong, but it is
unvalidated: the thresholds (`crucial >= 0.45`, `supporting >= 0.30`) have never
been checked against human judgement, and the per-module rankings that drive every
source-assignment decision in Chapter 2 rest on them. Treat a module's top-ranked
paper as a lead to verify rather than a settled answer.

This is also why the corpus is not self-consistent about titles: `scores/index.json`
reports `title: null` for every entry because `score.py` reads the `_marked.md`
frontmatter and not the `metadata.json` sidecar. The sidecar is the citation
authority, and `build_matrix.py` reads it — which is why the generated matrix shows
real titles while `scores/report.md` shows stems.

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
