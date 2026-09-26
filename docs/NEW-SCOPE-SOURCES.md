# New-Scope Source Requests

Papers and datasets the researchers must download manually for the new-scope BUDI
methodologies. Once fetched, place PDFs in `literature/bucket/` and follow
`docs/standards/rrl-workflow.md`.

Adopted methodology contracts: `../BUDI-ML/training/docs/model-methodologies/`
(`financial-classification-v2-methodology.md`, `anomaly-alerts-v2-methodology.md`,
`budget-optimizer-methodology.md`). Forecast methodology (pooled SARIMA) is
unchanged from the approved technical specification in `../BUDI-Base/`.

Status: `[ ]` = not downloaded, `[x]` = downloaded + in `literature/bucket/`.

<!-- Unchecked papers are either under minimum year limit (i.e., more than 3 years ago) or inaccessible (i.e., locked behind paywall). -->

## Financial classification (rule-based, v2)

- [ ] Bhutta, N., Blair, J., & Dettling, L. J. (2023). The smart money is in cash? Financial literacy and liquid savings among U.S. families. *Journal of Accounting and Public Policy, 42*(2), 107000. https://doi.org/10.1016/j.jaccpubpol.2022.107000
- [ ] He, L., & Zhou, S. (2022). Household financial vulnerability to income and medical expenditure shocks: Measurement and determinants. *International Journal of Environmental Research and Public Health, 19*(8), 4480. https://doi.org/10.3390/ijerph19084480
- [ ] Adams, R. M., Bord, V. M., & Katcher, B. (2022). Credit card profitability. *FEDS Notes*. https://doi.org/10.17016/2380-7172.3100
- [X] Bangko Sentral ng Pilipinas. (2025). *2025 consumer finance and inclusion survey*. https://www.bsp.gov.ph/Inclusive%20Finance/Financial%20Inclusion%20Reports%20and%20Publications/2025/2025CFISreport.pdf
- [X] Board of Governors of the Federal Reserve System. (2024). *Report on the economic well-being of U.S. households in 2023*. https://www.federalreserve.gov/publications/2024-economic-well-being-of-us-households-in-2023.htm
- [X] Guo, X., Okamura, H., & Dohi, T. (2024). Optimal test case generation for boundary value analysis. *Software Quality Journal, 32*, 543–566. https://doi.org/10.1007/s11219-023-09659-9
- [X] Hernandez, M., Epelde, G., Alberdi, A., Cilla, R., & Rankin, D. (2023). Synthetic tabular data evaluation in the health domain. *Methods of Information in Medicine, 62*(S01), e19–e38. https://doi.org/10.1055/s-0042-1760247

## Anomaly alerts (dual-channel IQR, v2)

- [ ] Chandola, V., Banerjee, A., & Kumar, V. (2009). Anomaly detection: A survey. *ACM Computing Surveys, 41*(3), Article 15. https://doi.org/10.1145/1541880.1541882
- [ ] Fisch, A. T. M., Eckley, I. A., & Fearnhead, P. (2022). A linear time method for the detection of collective and point anomalies. *Statistical Analysis and Data Mining*. https://doi.org/10.1002/sam.11586
- [X] Mashiko, S., Kawamata, Y., Nakayama, T., Sakurai, T., & Okada, Y. (2025). Anomaly detection in double-entry bookkeeping data by federated learning system. *Scientific Reports, 15*, Article 42208. https://doi.org/10.1038/s41598-025-26120-y
- [X] Azamuke, D., Katarahweire, M., & Bainomugisha, E. (2025). A labeled synthetic mobile money transaction dataset. *Data in Brief, 60*, Article 111534. https://doi.org/10.1016/j.dib.2025.111534

## Budget optimization (hierarchical LP, v2)

- [X] Fenig, G., & Petersen, L. (2024). *Dynamic optimization meets budgeting: Unraveling financial complexities* (Working Paper No. 32821). National Bureau of Economic Research. https://doi.org/10.3386/w32821
- [ ] Pulina, G. (2024). Credit card debt puzzle: Evidence from the euro area. *Economics Letters, 236*, Article 111586. https://doi.org/10.1016/j.econlet.2024.111586

## Notes

- BSP CFIS 2025 is cited in both classification and budget methodologies.
- `SciPy linprog` (budget) is software, not a download candidate.
- Forecaster references (pooled SARIMA) should come from the BUDI-Base technical specification's bibliography; confirm against Google Drive before citing.

## Researcher's Notes

- Unchecked papers are either under minimum year limit (i.e., more than 3 years ago) or inaccessible (i.e., locked behind paywall).