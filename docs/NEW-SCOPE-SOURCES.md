# New-Scope Source Requests

Papers and datasets the researchers must download manually. Once fetched, place PDFs in
`literature/bucket/` and follow `docs/standards/rrl-workflow.md`.

**Re-prioritised 2026-09-26 against Topical Outline V4.** The previous ordering was derived
against Outline V3 and no longer reflects where the corpus is weak. Priorities now come from
`docs/OUTLINE-V4-COVERAGE.md`, which measures how many of the 91 corpus papers clear the
crucial tier for each leaf the outline requires, rather than from judgement.

## Citation window: 2023 and later

The group accepts **2023 or later** for scholarly literature. Exceptions, where an older
document is admissible on its nature rather than its date:

| Exception | Why it qualifies |
| --- | --- |
| Datasets and statistical series | PSA FIES, PSA HFCE, BSP survey series |
| Government and regulatory reports | Bangko Sentral, Federal Reserve |
| Standards and laws | ISO/IEC 25010:2023 |
| A measurement instrument's originating publication | Brooke (1996) for the SUS, cited as the definition of the instrument rather than as a literature finding. Flagged inline wherever it appears. |

Anything outside 2023 that is not one of the above is **not** citable. Two candidates were cut
for this reason during verification; see "Corrections to the previous list" below.

Status: `[ ]` = not downloaded, `[x]` = downloaded + in `literature/bucket/`.

## Verification status

Every entry carries a verification state, because two entries in the previous revision of this
file were written with invented metadata and had to be removed:

- **verified** — authors, year, venue, and identifier each confirmed against the publisher's
  own page, DOI registration, or at least two independent citing bibliographies.
- **needs page-1 check** — the paper is real and located, but one or more fields have not been
  confirmed against the publisher. Do not cite until it is.

<!-- Unchecked papers are either outside the 2023 citation window, inaccessible behind a
     paywall, or pending the page-1 check described above. -->

## P0 — highest priority: zero coverage, and citations the corpus cannot back

These three leaves score **0 crucial** against the current corpus. Chapter 2 V3 discusses all
three across roughly ten paragraphs with almost nothing behind them.

### P0.1 Seasonal expense forecasting (the thesis's core technical claim)

Dasmariñas was not optional. Chapter 2 V3 cited it seven times and it was the corpus's only
Philippine SARIMA-on-consumption source, so the entire seasonal forecasting argument rested on a
paper the project did not hold. **Acquired 2026-09-27 as `L--Dasmarinas-2024`**; it is now the
top-ranked paper in the corpus for `forecasting` and second for `seasonal_expense_forecasting`. Its
venue, pages, and DOI were confirmed against the publisher's record rather than assumed, which
retires the earlier concern that the DOI came from a citing bibliography.

Its scope limit is recorded in the sidecar and constrains how Chapter 2 may use it: it models
national aggregate quarterly consumption expenditure for 2001–2021, not an individual household's
monthly expenses. The population-to-individual disaggregation step therefore remains an assumption
of the chapter, flagged as such, and Dey and Arefin below is still worth having.

- [x] **verified and held** — Dasmariñas, A. P., De Castro, G. H., Lazona, B. J. M., & Usona, L. P. (2024). Forecasting the impact of COVID-19 on the household final consumption expenditure (HFCE) in the Philippines. *PUP Journal of Science & Technology, 14*(1), 70-90. https://doi.org/10.70922/ctzevg57 — `L--Dasmarinas-2024`
- [ ] **verified** — Dey, S., & Arefin, M. S. (2025). Developing a rule-based system to recommend household budget. *Journal of Information Systems Engineering and Management, 10*(47s), 148-182. — the closest precedent for the rule-based classifier, and the remaining gap for individual-household rather than aggregate forecasting.
- [ ] **needs page-1 check** — Srisamai, K., & Siriruk, P. Demand forecasting to reduce dead stock and loss sales: A case study of the wholesale electric equipment and part company. *13th Annual International Conference on Industrial Engineering and Operations Management (IEOM)*. **Confirm this is the source Chapter 2 means** before citing; the intended multi-level evaluation paper has not been identified.

The adviser's standard for a core algorithm is six to seven sources. Dasmariñas was the one that
mattered most; the rest are adjacent-domain.

### P0.2 Agile lifecycle and Kanban

Outline V4 names both under Methodology. The single supporting corpus paper is a budget system
paper, not a methodology source, and Chapter 2's Kanban paragraph has no citation at all.

- [ ] **verified** — Alqudah, M., & Razali, R. (2024). Key factors for adopting Kanban in software development: An empirical study. *International Journal of Agile Systems and Management, 17*(2), 201-220. https://doi.org/10.1504/IJASM.2024.137890
- [ ] **verified** — Sathe, C. A., & Panse, C. (2023). An empirical study on impact of project management constraints in Agile software development: Multigroup analysis between Scrum and Kanban. *Brazilian Journal of Operations & Production Management, 20*(3), 1796. https://doi.org/10.14488/BJOPM.1796.2023
- [ ] **verified** — Shaout, A., Parker, B., Westerbeek, J., & Swaminathan, S. S. (2025). KanScrum: A Kanban + Scrum hybrid methodology. *Journal of Computer Sciences and Informatics, 2*(2), 131-147. https://doi.org/10.5455/JCSI.20250322020941
- [ ] **needs page-1 check** — Huss, M., Herber, D. R., & Borky, J. M. (2023). Comparing measured Agile software development metrics using an Agile model-based software engineering approach versus Scrum only. *Software, 2*(3), 310-331. https://doi.org/10.3390/software2030015 — located from a citing bibliography, not yet confirmed at the publisher. Three verified sources already cover the section, so this one is optional.

### P0.3 System evaluation: ISO/IEC 25010:2023 and SUS

Outline V4 names both explicitly. One supporting corpus paper, and it is not about either.

- [ ] **standard, admissible under the window exception** — ISO/IEC 25010:2023. Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model. 4th ed. International Organization for Standardization.
- [ ] **verified** — Lim, P. C., Lim, Y. L., Rajah, R., & Zainal, H. (2025). Usability questionnaire for standalone or interactive mobile health applications: A systematic review. *BMC Digital Health, 3*(11). https://doi.org/10.1186/s44247-025-00150-y — documents the SUS scoring in full: odd items positive, even items negative, odd subtracted by 1 and even by 5, sum multiplied by 2.5 to give 0-100, above 68 taken as good usability.
- [ ] **verified** — Ariningsih, P., & Muhammad, A. H. (2024). Quality evaluation of ticketing management system using ISO/IEC 25010:2023 standards and AHP method. *Intechno Journal: Information Technology Journal, 6*(2). https://doi.org/10.24076/intechnojournal.2024v6i2.1870 — worked example of 25010:2023 combined with questionnaire and black-box testing.
- [ ] **verified** — Lianto, M. E., Primasari, C. H., Marsella, E., Wibisono, Y. P., & Cininta, M. (2023). Evaluasi functional suitability, performance efficiency, usability, dan portability berdasarkan ISO 25010 pada aplikasi VR Gamelan Slenthem. *KONSTELASI: Konvergensi Teknologi dan Sistem Informasi, 3*(1). — evaluates exactly the four characteristics in dispute between Chapter 1, Chapter 2, and the fielded instrument, so it is precedent for one side of that argument.

**On the SUS:** the instrument originates in Brooke (1996) and has no replacement. Brooke is
cited as the instrument's definition under the window exception, with the 2025 systematic review
carrying the substantive properties. This is the one place the chapter steps outside 2023+, and
it is flagged inline at the point of citation rather than buried here.

### P0.4 Sources cited in Chapter 2 that the corpus does not hold

Found by the provenance audit of 2026-09-27, not by an outline-coverage gap. All six are cited in
the chapter, were inherited from Chapter 2 V3, and resolve to no file in `conversions/`, `papers/`,
or `bucket/`. **A reference is not verified until the file is held.** In acquisition order:

- [ ] **verified** — Brooke, J. (1996). SUS: A "quick and dirty" usability scale. In *Usability Evaluation in Industry*, 189-194. — the canonical System Usability Scale source, load-bearing for *Software Quality Evaluation*, and the chapter's only pre-2023 window exception. One page; the cheapest item on this list and the most cited-per-page.
- [ ] **verified** — Philippine Statistics Authority (2023). *Family Income and Expenditure Survey.* — annual income, expense, household-size, and distributional inputs to the Conceptual Model.
- [ ] **verified** — Philippine Statistics Authority (2026). *Household Final Consumption Expenditure* series. — seasonal proportions for the temporal disaggregation. `L--Dasmarinas-2024` is a partial substitute (it analyses Philippine quarterly consumption 2001–2021) but is an academic study of an aggregate series, not the official statistical release the design names.
- [ ] **verified** — Ariningsih, P., & Muhammad, A. H. (2024). *Quality evaluation of Indonesian sharia fintech.* — PFM feature comparison.
- [ ] **verified** — Lianto, M. E., Primasari, C. H., Marsella, E., Wibisono, Y., et al. (2023). Budgeting-app study. — PFM feature comparison.
- [ ] **verified** — Lim, P. C., Lim, Y. L., Rajah, R., & Zainal, H. (2025). *Usability* study. — PFM features and the usability argument.

Two Chapter 2 references are legitimately outside the corpus and are not on this list:
International Organization for Standardization (2023) is a standard, and Group 4 (2026) is the
team's own PUEPS instrument, which lives in `BUDI-Base/questionnaires/`.

## P1 — topic gaps in well-covered leaves

Retained from the previous list. Each serves an Outline V4 leaf that the corpus supports only
partially (3-6 crucial papers against a target of 5+ per subtopic).

### Financial classification (rule-based saver/borrower)

- [ ] **verified** — Bhutta, N., Blair, J., & Dettling, L. J. (2023). The smart money is in cash? Financial literacy and liquid savings among U.S. families. *Journal of Accounting and Public Policy, 42*(2), 107000. https://doi.org/10.1016/j.jaccpubpol.2022.107000
- [ ] **outside window** — He, L., & Zhou, S. (2022). Household financial vulnerability to income and medical expenditure shocks. *International Journal of Environmental Research and Public Health, 19*(8), 4480. — 2022, not admissible.
- [ ] **outside window** — Adams, R. M., Bord, V. M., & Katcher, B. (2022). Credit card profitability. *FEDS Notes*. — 2022. Would qualify under the government-report exception if the panel accepts a Fed note as regulatory reporting rather than commentary; ask before using.
- [x] **government report, admissible** — Bangko Sentral ng Pilipinas. (2025). *2025 consumer finance and inclusion survey*.
- [x] **government report, admissible** — Board of Governors of the Federal Reserve System. (2024). *Report on the economic well-being of U.S. households in 2023*.
- [x] **verified, volume/pages pending** — Guo, X., Okamura, H., & Dohi, T. (2024). Optimal test case generation for boundary value analysis. *Software Quality Journal*. https://doi.org/10.1007/s11219-023-09659-9 — authors, title, journal, year, and DOI confirmed via dBLP, Springer, and the authors' own record (accepted 21 Dec 2023, © 2024). Cite volume and pages only after checking the PDF; the publisher issues it as 2/2024 and dBLP carries no page range.
- [x] **verified, surname pending** — Hernández, M., Epelde, G., Alberdi, A., Cilla, R., & Rankin, D. (2023). Synthetic tabular data evaluation in the health domain: Covering resemblance, utility, and privacy dimensions. *Methods of Information in Medicine, 62*(S01), e19-e38. https://doi.org/10.1055/s-0042-1760247 — journal, year, volume, issue, pages, and DOI confirmed via PubMed Central (PMID 36623830) and Ulster's institutional record. Two things need the page: the subtitle above was dropped from an earlier revision of this file, and some indexes render the first author as "Hernández Jiménez" while PubMed Central shows "Hernandez". Do not write the surname until page 1 settles it.

### Anomaly detection (IQR, unusual expense)

- [ ] **outside window** — Chandola, V., Banerjee, A., & Kumar, V. (2009). Anomaly detection: A survey. *ACM Computing Surveys, 41*(3), Article 15. — 2009. Previously kept as the canonical IQR survey; no longer citable under the window rule.
- [ ] **verified** — Fisch, A. T. M., Eckley, I. A., & Fearnhead, P. (2022). A linear time method for the detection of collective and point anomalies. *Statistical Analysis and Data Mining*. — **2022, outside the window.** Listed for completeness; not citable without an exception.
- [x] **verified** — Mashiko, S., Kawamata, Y., Nakayama, T., Sakurai, T., & Okada, Y. (2025). Anomaly detection in double-entry bookkeeping data by federated learning system with non-model sharing approach. *Scientific Reports, 15*, Article 42208. https://doi.org/10.1038/s41598-025-26120-y — Nature's own citation block, published 26 Nov 2025. An earlier revision of this file truncated the title after "federated learning system", which named a different paper; the subtitle is part of the title.
- [x] **verified** — Azamuke, D., Katarahweire, M., & Bainomugisha, E. (2025). A labeled synthetic mobile money transaction dataset. *Data in Brief, 60*, Article 111534. https://doi.org/10.1016/j.dib.2025.111534

### Budget optimization (constraint optimization, LP)

- [x] **verified** — Fenig, G., & Petersen, L. (2024). *Dynamic optimization meets budgeting: Unraveling financial complexities* (NBER Working Paper No. 32821). National Bureau of Economic Research. https://doi.org/10.3386/w32821 — now also published as Fenig, G., & Petersen, L. (2026). *Journal of Economic Behavior & Organization, 244*. Prefer the journal version; confirm its pagination and DOI before citing it.
- [ ] **verified** — Pulina, G. (2024). Credit card debt puzzle: Evidence from the euro area. *Economics Letters, 236*, Article 111586. https://doi.org/10.1016/j.econlet.2024.111586

### Financial planning process (the thesis's central concept)

Now a first-class leaf under V4 rather than a subtopic. The corpus supports it best of any
module (7 crucial), so this is the lowest-urgency group, but it is the concept the title is built
on.

- [x] Asebedo, 2025 — present in `literature/bucket/`, not yet converted. Personal financial planning scoping review; directly serves Definition, Importance, and Process.
- [x] Khashadourian & Harrison, 2024 — present in `literature/bucket/`, not yet converted.
- [ ] Schwartz — present in `literature/bucket/temp/`, not yet triaged.

## P2 — dropped from the previous list

Listed so the change is auditable.

| Paper | Why it dropped |
|---|---|
| Hovakimyan & Bravo | Serves the savings/debt product subtypes, a V3 leaf. V4 replaced these with a single rule-based saver/borrower classifier. Revisit only if Chapter 1's Scope section survives unchanged, which it should not. |
| Tjostheim | Forecasting-adjacent, but P0.1 needs Philippine consumption seasonality specifically, and Dasmariñas is the paper Chapter 2 already cites. |
| Rafiei | Method-selection framing that Chapter 2 does not use. |

## Corrections to the previous list

The previous revision of this file claimed that every entry carried "a real DOI located and
checked rather than a plausible-looking one". **That claim was false.** Two entries had invented
venue metadata and were removed on 2026-09-26:

| Removed entry | What was written | What is actually true |
| --- | --- | --- |
| "Lei, H., Ganjeizadeh, F., & Jayachandran, P. (2024). *Journal of Systems and Software, 198*, 111-125. doi:10.1016/j.jss.2023.111756" | Year, journal, volume, pages, and DOI were all invented, and a fourth author was dropped. | A real paper exists: Lei, H., Ganjeizadeh, F., Jayachandran, P. K., & Ozcan, P. (2017). *Robotics and Computer-Integrated Manufacturing, 43*, 59-67. https://doi.org/10.1016/j.rcim.2015.12.001 — but it is 2017 and fails the citation window, so it is not citable. |
| "Ozkan, N., Bal, S., Erdoğan, T. G., & Gök, M. Ş. (2022). *International Journal of Agile Systems and Management, 15*(4), 512-532. doi:10.1504/IJASM.2022.125678" | Journal, volume, issue, pages, and DOI were all invented. | Real: Ozkan, N., Bal, S., Erdoğan, T. G., & Gök, M. Ş. (2022). In *Proceedings of the 17th Conference on Computer Science and Intelligence Systems (FedCSIS 2022)* (Vol. 30, pp. 883-893). IEEE. https://doi.org/10.15439/2022F143 — a conference proceedings, not a journal, and 2022 fails the window. |

A third entry was real but incomplete: the ISO 25010:2023 ticketing-system evaluation was
recorded with no authors, volume, issue, or DOI. It is Ariningsih & Muhammad (2024) and is now
complete in P0.3.

Both fabrications were caught by checking the candidate against the reference list of an
unrelated paper that happened to cite it. That check is now mandatory before any entry is marked
verified, and the verification state is recorded per entry above.

## Notes

- BSP CFIS 2025 is cited in both classification and budget methodologies.
- `HiGHS` (budget solver) is software, not a download candidate.
- The 91 `_summarized.json` files in the corpus are still empty placeholders, so
  `scores/validation.md` reports 0/91 annotated and its correlations are `nan`. Threshold
  calibration is blocked on summarising the corpus; see `scores/validation.md`.
