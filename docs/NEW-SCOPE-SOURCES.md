# New-Scope Source Requests

Papers and datasets the researchers must download manually. Once fetched, place PDFs in
`literature/bucket/` and follow `docs/standards/rrl-workflow.md`.

**Re-prioritised 2026-09-26 against Topical Outline V4.** The previous ordering was derived
against Outline V3 and no longer reflects where the corpus is weak. Priorities now come from
`docs/OUTLINE-V4-COVERAGE.md`, which measures how many of the 91 corpus papers clear the
crucial tier for each leaf the outline requires, rather than from judgement.

Status: `[ ]` = not downloaded, `[x]` = downloaded + in `literature/bucket/`.

<!-- Unchecked papers are either under minimum year limit (i.e., more than 3 years ago) or inaccessible (i.e., locked behind paywall). -->

## P0 — zero corpus coverage, named explicitly by Outline V4

These three leaves score **0 crucial** against the current corpus. Chapter 2 V3 discusses all
three across roughly ten paragraphs with almost nothing behind them.

### P0.1 Seasonal expense forecasting (the thesis's core technical claim)

Dasmariñas is not optional. Chapter 2 V3 cites it seven times and it is the corpus's only
Philippine SARIMA-on-consumption source, so the entire seasonal forecasting argument currently
rests on a paper the project does not hold.

- [ ] Dasmariñas, A. P., De Castro, G., Lazona, B. J., & Usona, L. (2024). Forecasting the impact of COVID-19 on the household final consumption expenditure (HFCE) in the Philippines. *PUP Journal of Science & Technology, 14*(1), 70–90. https://doi.org/10.70922/ctzevg57
- [ ] Dey, S., & Arefin, M. S. (2025). Developing a rule-based system to recommend household budget. *Journal of Information Systems Engineering and Management, 10*(47s), 148–182. https://jisem-journal.com/index.php/journal/article/view/9230 — also closes a 3-citation gap in Chapter 2.
- [ ] Srisamai, K., & Siriruk, P. Demand forecasting to reduce dead stock and loss sales: A case study of the wholesale electric equipment and part company. *13th Annual International Conference on Industrial Engineering and Operations Management (IEOM)*. **Confirm this is the source Chapter 2 means** before citing; the intended multi-level evaluation paper has not been identified.

The adviser's standard for a core algorithm is six to seven sources. Dasmariñas alone is one.

### P0.2 Agile lifecycle and Kanban

Outline V4 names both under Methodology. The single supporting corpus paper is a budget system
paper, not a methodology source, and Chapter 2's Kanban paragraph has no citation at all.

- [ ] Lei, H., Ganjeizadeh, F., & Jayachandran, P. (2024). A statistical analysis of the effects of Scrum and Kanban on software development projects. *Journal of Systems and Software, 198*, 111–125. https://doi.org/10.1016/j.jss.2023.111756
- [ ] Alqudah, M., & Razali, R. (2024). Key factors for adopting Kanban in software development: An empirical study. *International Journal of Agile Systems and Management, 17*(2), 201–220. https://doi.org/10.1504/IJASM.2024.137890
- [ ] An empirical study on impact of project management constraints in Agile software development: Multigroup analysis between Scrum and Kanban (2023). *Brazilian Journal of Operations & Production Management*. https://bjopm.org.br/bjopm/article/view/1796
- [ ] Ozkan, N., Bal, S., Erdoğan, T. G., & Gök, M. Ş. (2022). Scrum, Kanban or a mix of both? A systematic literature review. *International Journal of Agile Systems and Management, 15*(4), 512–532. https://doi.org/10.1504/IJASM.2022.125678 — 2022, just outside the 3-year window, but it is the systematic review of the two methods and is the strongest single citation for a Kanban methodology section.

### P0.3 System evaluation: ISO/IEC 25010:2023 and SUS

Outline V4 names both explicitly. One supporting corpus paper, and it is not about either.

- [ ] Quality evaluation of ticketing management system using ISO/IEC 25010:2023 standards and AHP method (2024). *Intechno Journal: Information Technology Journal*. https://jurnal.amikom.ac.id/index.php/intechno/article/view/1870 — applies the **2023** edition specifically, with questionnaire and black-box testing.
- [ ] ISO/IEC 25010-based quality evaluation of three mobile applications for reproductive health services in Morocco (2024). *Clinical and Experimental Obstetrics & Gynecology*. — mobile applications, checklist method, and explicit KPI guidance for integrating quality dimensions through development.
- [ ] Lianto, M. E., Primasari, C. H., Marsella, E., Wibisono, Y. P., & Cininta, M. (2023). Evaluasi functional suitability, performance efficiency, usability, dan portability berdasarkan ISO 25010 pada aplikasi VR. *KONSTELASI: Konvergensi Teknologi dan Sistem Informasi, 3*(1), 24–36. — covers exactly the four characteristics in dispute between Chapter 1, Chapter 2, and the fielded instrument, so it is precedent for one side of that argument.
- [ ] The ISO/IEC 25010:2023 standard itself is **not a paper** and must be cited as the standard, not folded into this list.

**On the SUS:** the instrument is Brooke (1996) and there is no recent replacement. Chapter 2
should cite Brooke directly and accept that it falls outside the 3-year window, rather than cite a
secondary paper that merely reprints the ten items. The instrument's own bibliography in the
group's field copy should be checked before the citation is written.

## P1 — topic gaps in well-covered leaves

Retained from the previous list. Each serves an Outline V4 leaf that the corpus supports only
partially (3–6 crucial papers against a target of 5+ per subtopic).

### Financial classification (rule-based saver/borrower)

- [ ] Bhutta, N., Blair, J., & Dettling, L. J. (2023). The smart money is in cash? Financial literacy and liquid savings among U.S. families. *Journal of Accounting and Public Policy, 42*(2), 107000. https://doi.org/10.1016/j.jaccpubpol.2022.107000
- [ ] He, L., & Zhou, S. (2022). Household financial vulnerability to income and medical expenditure shocks: Measurement and determinants. *International Journal of Environmental Research and Public Health, 19*(8), 4480. https://doi.org/10.3390/ijerph19084480
- [ ] Adams, R. M., Bord, V. M., & Katcher, B. (2022). Credit card profitability. *FEDS Notes*. https://doi.org/10.17016/2380-7172.3100
- [x] Bangko Sentral ng Pilipinas. (2025). *2025 consumer finance and inclusion survey*. https://www.bsp.gov.ph/Inclusive%20Finance/Financial%20Inclusion%20Reports%20and%20Publications/2025/2025CFISreport.pdf
- [x] Board of Governors of the Federal Reserve System. (2024). *Report on the economic well-being of U.S. households in 2023*. https://www.federalreserve.gov/publications/2024-economic-well-being-of-us-households-in-2023.htm
- [x] Guo, X., Okamura, H., & Dohi, T. (2024). Optimal test case generation for boundary value analysis. *Software Quality Journal, 32*, 543–566. https://doi.org/10.1007/s11219-023-09659-9
- [x] Hernandez, M., Epelde, G., Alberdi, A., Cilla, R., & Rankin, D. (2023). Synthetic tabular data evaluation in the health domain. *Methods of Information in Medicine, 62*(S01), e19–e38. https://doi.org/10.1055/s-0042-1760247

### Anomaly detection (IQR, unusual expense)

- [ ] Chandola, V., Banerjee, A., & Kumar, V. (2009). Anomaly detection: A survey. *ACM Computing Surveys, 41*(3), Article 15. https://doi.org/10.1145/1541880.1541882 — 2009, outside the window, kept as the canonical survey for the IQR/box-plot basis.
- [ ] Fisch, A. T. M., Eckley, I. A., & Fearnhead, P. (2022). A linear time method for the detection of collective and point anomalies. *Statistical Analysis and Data Mining*. https://doi.org/10.1002/sam.11586
- [x] Mashiko, S., Kawamata, Y., Nakayama, T., Sakurai, T., & Okada, Y. (2025). Anomaly detection in double-entry bookkeeping data by federated learning system. *Scientific Reports, 15*, Article 42208. https://doi.org/10.1038/s41598-025-26120-y
- [x] Azamuke, D., Katarahweire, M., & Bainomugisha, E. (2025). A labeled synthetic mobile money transaction dataset. *Data in Brief, 60*, Article 111534. https://doi.org/10.1016/j.dib.2025.111534

### Budget optimization (constraint optimization, LP)

- [x] Fenig, G., & Petersen, L. (2024). *Dynamic optimization meets budgeting: Unraveling financial complexities* (Working Paper No. 32821). National Bureau of Economic Research. https://doi.org/10.3386/w32821
- [ ] Pulina, G. (2024). Credit card debt puzzle: Evidence from the euro area. *Economics Letters, 236*, Article 111586. https://doi.org/10.1016/j.econlet.2024.111586

### Financial planning process (the thesis's central concept)

Now a first-class leaf under V4 rather than a subtopic. The corpus supports it best of any
module (7 crucial), so this is the lowest-urgency group, but it is the concept the title is built
on.

- [x] Asebedo, 2025 — present in `literature/bucket/`, not yet converted. Personal financial planning scoping review; directly serves Definition, Importance, and Process.
- [x] Khashadourian & Harrison, 2024 — present in `literature/bucket/`, not yet converted.
- [ ] Schwartz — present in `literature/bucket/temp/`, not yet triaged.

## P2 — dropped from the previous list

Listed so the change is auditable. These were prioritised under Outline V3, which contained
leaves that V4 removed.

| Paper | Why it dropped |
|---|---|
| Hovakimyan & Bravo | Serves the savings/debt product subtypes, a V3 leaf. V4 replaced these with a single rule-based saver/borrower classifier. Revisit only if Chapter 1's Scope section survives unchanged, which it should not. |
| Tjostheim | Forecasting-adjacent, but P0.1 needs Philippine consumption seasonality specifically, and Dasmariñas is the paper Chapter 2 already cites. |
| Rafiei | Method-selection framing that Chapter 2 does not use. |

## Notes

- BSP CFIS 2025 is cited in both classification and budget methodologies.
- `HiGHS` (budget solver) is software, not a download candidate.
- The 91 `_summarized.json` files in the corpus are still empty placeholders, so
  `scores/validation.md` reports 0/91 annotated and its correlations are `nan`. Threshold
  calibration is blocked on summarising the corpus; see `scores/validation.md`.

## Researcher's Notes

- Unchecked papers are either under minimum year limit (i.e., more than 3 years ago) or inaccessible (i.e., locked behind paywall).
