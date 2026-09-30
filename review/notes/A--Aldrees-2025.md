---
paper_id: A--Aldrees-2025
first_author: "Aldrees"
year: 2025
title: "Behavioral Patterns in Micro-lending: Enhancing Credit Risk Assessment with Collaborative Filtering and Federated Learning"
venue: "International Journal of Computing and Intelligent Systems"
doi: "10.1007/s44196-025-00776-w"
type: Not reported
designation: algorithm
section: "Not reported"
modules: []
status: extracted
generated-by: scripts/build_matrix.py
---

# Behavioral Patterns in Micro-lending: Enhancing Credit Risk Assessment with Collaborative Filtering and Federated Learning

`A--Aldrees-2025` — Aldrees (2025), *International Journal of Computing and Intelligent Systems*

## Summary

A privacy-preserving credit risk method for micro-lending, CFM-LPA, combines collaborative filtering over lending patterns with federated learning, updating a behaviour factor each repayment period to filter new credit risks without sharing borrower data.

## Problem and Motivation

Micro-lending platforms struggle to assess credit risk because borrower data are scarce, borrower variety is high, and centralized credit scoring exposes sensitive financial data. Return rate and customer history behave differently at low-interest scales, where delayed or failed returns across increasing tenures shift credit risk in ways conventional methods do not capture. Existing machine learning and ensemble approaches depend on centralized data sources and rarely include privacy-preserving behavioural analysis.

## Method

**Design.** Computational method-development study with comparative benchmark evaluation against three published models; the authors state no formal design label.
**Sample.** n = 32,581 loan records (public Kaggle credit-risk dataset by user laotse, 12 features, one record per loan application)
**Context.** geography: Not reported (no country stated; the dataset is a public international loan dataset); population: Micro-lending borrowers aged 20-45 with incomes of 4K-2039K, employment tenure of 1-31 years, loan grades A-D and loan amounts of 0.5K-35K; setting: Virtual/computational: offline simulation of micro-lending credit risk assessment on an NVIDIA A100 with WEKA and Python 3.9; no live lending platform was involved
- Use the public Kaggle credit-risk dataset (32,581 records, 12 features) and split it into an initial input block (return + response) and a behaviour pattern block.
- Derive a behaviour factor from return rate, prompt return, credit limit, credit history, default rate, liability and economic conditions, then update it at every repayment period.
- Apply collaborative filtering over lending patterns, matching new borrowers to similar borrowers through user- and item-based filtering to generate risk ratings from repayment history.
- Wrap the filtering in federated learning so that multiple lenders train collaboratively, exchanging model updates rather than raw borrower records.
- Filter risk with Arisk, contrasting maximum and minimum credit periods, then detect new risk with riskdetect(t) conditioned on the filtered factor of the previous return period.
- Bound the behaviour factor with a credit-period threshold rule, assigning Cperiod to its maximum or minimum branch when the credit-score-to-history ratio crosses the threshold.
- Benchmark against SMOTE-ENN (Aruleba and Sun), LightGBM-GAN (Zhuang and Wei) and FEEM-VO (Yang and Xiao) over tenure, interest rate, amount and limit-category variants.
- Run experiments in WEKA and Python 3.9 on an NVIDIA A100 (80 GB VRAM) with a 64-core AMD EPYC 7742, 128 GB RAM and 10 Gbps Ethernet.
- State reliability procedures: 95% confidence intervals, a paired t-test, a Wilcoxon signed-rank test, and fivefold cross-validated Bayesian optimisation of XGBoost hyperparameters.
- Discuss mitigations for model drift, poisoning and inference attacks, plus group bias, using FedAvg/FedProx, Krum, differential privacy, AIF360 and Fairlearn.

## Software

- WEKA (version not reported)
- Python 3.9
- AIF360 (version not reported)
- Fairlearn (version not reported)
- XGBoost, Bayesian-optimised: 500 boosting rounds, learning rate 0.05, max depth 6, subsample 0.8, feature fraction 0.7, L2 lambda 1.2
- SMOTE-ENN (baseline implementation, version not reported)
- LightGBM-GAN (baseline implementation, version not reported)
- FEEM-VO (baseline implementation, version not reported)
- FedAvg / FedProx federated aggregation (version not reported)

## Key Findings

- num: Table 3 reports 95.21% new risk detection for CFM-LPA, against 90.32% for FEEM-VO, 86.45% for LightGBM-GAN and 80.12% for SMOTE-ENN.
- num: The abstract claims 14.03% better risk detection accuracy and 13.28% better return rate analysis across financed amounts, while Sect. 6 claims 14.82% and 13.63% for different interest rates.
- num: Table 3 return rate analysis values rise from 0.81 (SMOTE-ENN) to 0.88 (LightGBM-GAN), 0.92 (FEEM-VO) and 0.97 (CFM-LPA).
- num: Evaluation uses 32,581 loan records described by 12 features, with ages 20–45, loan amounts 0.5K–35K, interest rates 5.42–23.22 and credit histories of 2–30 years.
- num: Table 3 limit-category accuracy for CFM-LPA is A: 90, B: 93, C: 95, D: 96, against A: 78, B: 80, C: 82, D: 84 for SMOTE-ENN.
- num: Sect. 5 states 95% confidence intervals (± 2.1% for accuracy) and a paired t-test at p < 0.05, with fivefold cross-validated Bayesian optimisation of an XGBoost setup.
- num: The dataset's Group A (majority) has an average credit score of 720, an 85% loan acceptance rate and a 5% default rate; Group B has 680, 65% and 7%.
- num: Comparative X-variants span tenure 2–20 yrs, interest rate 5–23, amount 5–35K and limit categories A to D.
- The behaviour factor is recomputed each repayment period, so the previous period's factor conditions credit risk for the next period.
- The authors acknowledge that federated learning needs heavy computation and robust synchronisation across lenders, which may not scale.

## Key Figures and Tables

- Fig. 1 (p. 6): Data used for evaluation — 32,581 records across 12 features → the behaviour factor is computed from return rate, prompt return and credit limit.
- Fig. 2 (p. 8): Return rate and credit limit relation — if Rrate = Econ × t then BrC = good → a high return rate with a high score marks good behaviour patterns and low risk.
- Fig. 3 (p. 9): Credit risk analysis — Crisk(t + 1) tracks borrowers whose risk grows over tenure → high debt with consistent payment still yields a high risk score.
- Fig. 4 (p. 11): Lending pattern analysis — stable monthly repayment yields smooth patterns, irregular repayment yields abnormal ones → repayment consistency is the risk signal.
- Fig. 5 (p. 14): Behaviour factor estimation using federated learning — Lenpat(t) enters each period → lending patterns propagate across lenders without moving raw data.
- Fig. 6 (p. 15): Behaviour factor analysis under Bfact variants → a low behaviour factor marks missed payments and irregular financial activity.
- Fig. 7 (p. 17): Filtering ratio analysis — Arisk contrasts maximum and minimum credit periods → a high filtering ratio means more risk being detected and filtered.
- Fig. 8 (p. 19): New risk detection over time by borrower specification → stable borrowers show low occurrence of new risk, so the method surfaces fewer new risks.
- Fig. 9 (p. 20): Return rate analysis — CFM-LPA holds return rate above the baselines → continuous federated updates stabilise repayment under economic fluctuation.
- Table 1 (p. 5): Summary of existing models (partially garbled character-level extraction) → prior work is dominated by centralized ML, ensemble and oversampling approaches.
- Table 2 (p. 21): Experimental setup — A100 80 GB, 64-core EPYC 7742, 128 GB RAM, Windows 11, Python 3.9, AIF360/Fairlearn, learning rate 0.01, max depth 10, 500 estimators → hardware is specified, but the XGBoost-style settings do not belong to the proposed CFM-LPA method.
- Table 3 (p. 21): Comparative analysis — CFM-LPA 95.21% new risk detection and 0.97 return rate analysis against SMOTE-ENN 80.12%/0.81 → best reported value on both metrics.

## Limitations and Gaps

- Headline results are internally inconsistent and not reproducible: the Abstract reports 14.03% better risk detection accuracy and 13.28% better return rate analysis across financed amounts, while Sect. 6 (Conclusion, p. 21) reports 14.82% and 13.63% for different interest rates; neither matches the 95.21% vs 80.12% gap in Table 3.
- The authors acknowledge that reliance on collaborative filtering may introduce biases when lending data are sparse or imbalanced, producing inaccurate risk predictions for new or underrepresented borrowers (Sect. 6, p. 22).
- Federated learning requires significant computational resources and robust synchronization across multiple lending institutions, which may pose scalability challenges (Sect. 6, p. 22).
- Future studies are still needed on scalability through efficient federated communication protocols, reduced computational overhead, and real-time financial indicators or alternative credit data such as social and transactional behaviour (Sect. 6, p. 22).
- [unacknowledged] The study is an offline simulation on a single public Kaggle dataset with no live lending platform, no human participants and no Philippine data, so external validity is untested.
- [unacknowledged] Table 2's learning rate, max depth, 500 estimators and Bayesian-optimised XGBoost settings belong to a baseline-style configuration rather than the proposed CFM-LPA, leaving the reported setup unreproducible.
- [unacknowledged] No precision, recall, F1, per-fold variance or per-class result is reported, and the Table 1 and Table 3 column alignment is ambiguous, so the comparison cannot be fully reconstructed.

## Definitions

- **CFM-LPA** — Collaborative Filtering Method using Lending Pattern Analysis, the paper's proposed credit risk assessment method.
- **Behaviour factor (Bfact)** — Borrower behavioural factor derived from credit period, liability and pattern, normalised and recomputed each repayment period.
- **Return rate (Rrate)** — Share of the lent amount returned by the borrower, adjusted by credit limit and micro-lending risk.
- **Credit limit (Clm)** — Limit extended to the borrower over time; a high limit is treated as a signal of financial risk.
- **Lenpat / Lenfed** — The lending pattern term and its federated-learning counterpart that generalises patterns across lenders.
- **Arisk** — Filtered risk factor built from the difference between maximum and minimum credit periods.
- **FEEM-VO** — Feature Enhanced Ensemble Modeling with Voting Optimization, a Yang and Xiao baseline used for comparison.
- **Kaggle credit-risk dataset** — Public dataset by Kaggle user laotse supplying the 32,581 records and 12 features used in all experiments.

## Key Equations

- `ML(t) = (Clm + BrC × ((Irate × Econ + Bfact) / (1 + Bfact(t + 1)))) × Crisk` — Micro-lending risk at time t from limit, score, rate and behaviour factor.
- `Rrate = (Ramt−tot / amt) + exp(Clm × BrC / ML(t))` — Return rate: amount returned over amount lent, adjusted by risk.
- `Lenadjust = log((amt × Crisk / (1 − (1 + Irate)^t)) × (Rrate × Clm / (BrC × Chist))) + (1 − Dri) + Hres(t)` — Adjusted lending pattern from risk, return rate and default rate.
- `Crisk(t + 1) = (1 / (1 + Lenpat + Econ)) × (amt × Crisk / (1 − (1 + Irate)^t))` — Next-period credit risk from lending pattern and economic condition.
- `Lenfed(t) = Lenpat × Crisk(t + 1) × (1 / (1 + Σ (Cstable/Urepay) + BrC/(1 + Irate) + 1/(1 + Dri × Econ)))` — Federated lending pattern weighting credit stability and default.
- `Ftbh(t) = Lenfed(t) × Ftbh−in × (1 / (1 + Econ)) ∀Urepay` — Behaviour pattern over time across all repayment tenures.
- `Bfact(t) = Cperiod × Ftbh(t) × (Σ Oi / (1 + Irate)) × (BrC − Dri)` — Behaviour factor from credit period, pattern and liability.
- `Arisk = Σ (Crisk × Cstable)/(Irate − maxt Cperiod) − (Crisk × Urepay)/(Irate − mint Cperiod) + Rrate × Clm + Dri × Econ` — Risk filter contrasting maximum and minimum credit periods.
- `riskdetect(t) = (BrC + Chist + Clm) × (1 / Arisk) × (Bfact − Cperiod + Econ)` — Detected risk; exceeding Arisk indicates a high-risk borrower.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Risk detection accuracy improvement of the proposed CFM-LPA across financed amounts | accuracy improvement | 14.03% | — | — | Abstract, p. 1 |
| Return rate analysis improvement of the proposed CFM-LPA across financed amounts | return rate improvement | 13.28% | — | — | Abstract, p. 1 |
| Risk detection analysis improvement of the proposed CFM-LPA for the different interest rates | accuracy improvement | 14.82% | — | — | Sec. 6 Conclusion, p. 21 |
| Return rate analysis improvement of the proposed CFM-LPA for the different interest rates | return rate improvement | 13.63% | — | — | Sec. 6 Conclusion, p. 21 |
| New risk detection, proposed CFM-LPA | accuracy | 95.21% | — | — | Table 3, p. 21 |
| New risk detection, FEEM-VO baseline | accuracy | 90.32% | — | — | Table 3, p. 21 |
| New risk detection, LightGBM-GAN baseline | accuracy | 86.45% | — | — | Table 3, p. 21 |
| New risk detection, SMOTE-ENN baseline | accuracy | 80.12% | — | — | Table 3, p. 21 |
| Return rate analysis, proposed CFM-LPA | return rate | 0.97 | — | — | Table 3, p. 21 |
| Return rate analysis, FEEM-VO baseline | return rate | 0.92 | — | — | Table 3, p. 21 |
| Return rate analysis, LightGBM-GAN baseline | return rate | 0.88 | — | — | Table 3, p. 21 |
| Return rate analysis, SMOTE-ENN baseline | return rate | 0.81 | — | — | Table 3, p. 21 |
| New risk detection by limit category, proposed CFM-LPA | accuracy by loan grade | A: 90, B: 93, C: 95, D: 96 | — | — | Table 3, p. 21 |
| New risk detection by limit category, FEEM-VO baseline | accuracy by loan grade | A: 86, B: 89, C: 91, D: 93 | — | — | Table 3, p. 21 |
| New risk detection by limit category, LightGBM-GAN baseline | accuracy by loan grade | A: 82, B: 85, C: 88, D: 90 | — | — | Table 3, p. 21 |
| New risk detection by limit category, SMOTE-ENN baseline | accuracy by loan grade | A: 78, B: 80, C: 82, D: 84 | — | — | Table 3, p. 21 |
| Reliability procedure reported for the accuracy estimates | 95% confidence interval half-width for accuracy | ± 2.1% | ± 2.1% | — | Sec. 5 Results and Discussion, p. 19 |
| Significance testing reported for the comparative results | paired t-test p-value | p < 0.05 | — | <0.05 | Sec. 5 Results and Discussion, p. 19 |
| Group A (majority) average credit score in the dataset | credit score | 720 | — | — | Sec. 5 Results and Discussion, p. 19 |
| Group A (majority) loan acceptance rate in the dataset | acceptance rate | 85% | — | — | Sec. 5 Results and Discussion, p. 19 |
| Group A (majority) default rate in the dataset | default rate | 5% | — | — | Sec. 5 Results and Discussion, p. 19 |
| Group B (minority) average credit score in the dataset | credit score | 680 | — | — | Sec. 5 Results and Discussion, p. 19 |
| Group B (minority) loan approval rate in the dataset | approval rate | 65% | — | — | Sec. 5 Results and Discussion, p. 19 |
| Group B (minority) default rate in the dataset | default rate | 7% | — | — | Sec. 5 Results and Discussion, p. 19 |
| Evaluation sample size | records | 32,581 | — | — | Sec. 3 Data Description, p. 6 |

## Quotes

> "This article introduces a Collaborative Filtering Method using Lending Pattern Analysis (CFM-LPA)."
>
> — Abstract, p. 1 — `ml_algorithms`

> "The proposed method enhances risk detection accuracy by 14.03% and improves return rate analysis by 13.28% across financed amounts."
>
> — Abstract, p. 1 — `ml_algorithms`

> "The proposed method improves the risk detection analysis by 14.82% and return rate analysis by 13.63% for the different interest rates."
>
> — Sec. 6 Conclusion, p. 21 — `ml_algorithms`

> "Data shortage, borrower variety, and privacy issues contribute to micro-lending platforms’ ongoing struggles with proper credit risk assessment."
>
> — Sec. 1.1 Research Gap, p. 2 — `debt_management`

> "Due to security concerns and a lack of flexibility for changing financial patterns, traditional credit scoring algorithms often depend on centralized data collecting."
>
> — Sec. 1.1 Research Gap, p. 2 — `privacy_security`

> "The above data are provided for 32,581 record sets as collected from the dataset."
>
> — Sec. 3 Data Description, p. 6 — `ml_algorithms`

> "Research on the combination of federated learning with collaborative filtering for customized credit risk prediction is still in its early stages, but it provides a privacy-preserving option."
>
> — Sec. 2 Related Works, p. 6 — `privacy_security`

> "CFM enhances lending decisions through federated learning without exchanging borrower-specific data directly to maintain privacy."
>
> — Sec. 4.1 Collaborative Filtering, p. 10 — `privacy_security`

> "A borrower with irregular repayment and behaviour patterns leads to abnormal patterns and indicates a potential risk during lending."
>
> — Sec. 4.1 Collaborative Filtering, p. 12 — `behavioral_insights`

> "One possible source of bias in the dataset is the difference between Group A (the majority) and Group B (the minority)."
>
> — Sec. 5 Results and Discussion, p. 19 — `ml_algorithms`

> "A borrower with predictable and stable financial behaviour will have a low occurrence of new risk"
>
> — Sec. 5 Results and Discussion, p. 20 — `anomaly_detection`

> "As data distributions vary over time, a phenomenon known as model drift occurs, and the prediction performance continues to decline."
>
> — Sec. 5 Results and Discussion, p. 20 — `ml_algorithms`

> "However, the model’s reliance on collaborative filtering may introduce biases if the available lending data is sparse or imbalanced, potentially leading to inaccurate risk predictions for new or underrepresented borrowers."
>
> — Sec. 6 Conclusion, pp. 21-22 — `ml_algorithms`

> "Federated learning ensures data privacy; it requires significant computational resources and robust synchronization across multiple lending institutions, which may pose scalability challenges."
>
> — Sec. 6 Conclusion, p. 22 — `privacy_security`

## Relevance to BUDGIE

- `ml_algorithms` — high: Supplies the core algorithm, a collaborative filtering plus federated learning risk model benchmarked against SMOTE-ENN, LightGBM-GAN and FEEM-VO, with accuracy reported in Table 3.
- `debt_management` — high: Micro-lending, repayment behaviour, default rate, credit limit and credit risk are the paper's entire subject, expressed through return rate and credit stability terms.
- `behavioral_insights` — high: The behaviour factor is built from repayment consistency, peer influence, financial adaptability and loan purpose, making borrower psychology the model's signal.
- `privacy_security` — high: Decentralized federated training is proposed explicitly as the remedy for centralized data collection, with poisoning, inference attacks and differential privacy discussed.
- `anomaly_detection` — medium: New-risk detection, filtering ratio and abnormal repayment patterns are operationalised through Arisk and riskdetect(t) rather than classical outlier methods.
- `synthetic_data_mlops` — medium: GAN and SMOTE based synthetic oversampling appear in the baselines, and the paper discusses drift-aware aggregation, model upgrades and serving concerns.
- `financial_wellbeing` — low: Credit stability and repayment consistency are treated as financial stability indicators of borrowers, but no well-being instrument or measure is used.
- `forecasting` — low: Period-to-period updating and drift monitoring (FedProx, ADWIN, Kolmogorov–Smirnov) are discussed, but no time series forecast or seasonality is modelled.
- `pfms_systems` — low: Lending-platform credit scoring is adjacent to finance applications, but no personal finance app, dashboard or interface is built or evaluated.
- `filipino_context` — low: No Philippine institution, data source or population appears; the study is international and uses a public non-Filipino loan dataset.

The paper packages credit risk scoring for micro-lending as a privacy problem rather than purely a predictive one, proposing that lenders share federated model updates instead of borrower records. It shows how a behaviour factor derived from return rate, credit limit, credit history and economic conditions can be refreshed every repayment period and filtered to isolate newly emerging risks. Empirically, the proposed CFM-LPA reports the best values among three published baselines on a 32,581-record public loan dataset. The contribution is therefore conceptual and architectural; the reported gains are large but rest on a single offline dataset with internally inconsistent headline numbers, which limits how far the result generalises.

- Justifies: Privacy-preserving credit scoring can be achieved by exchanging federated model updates across lenders instead of raw borrower records.

- Justifies: Recomputing a behaviour factor every repayment period lets a model filter new credit risks that centralised batch scoring misses.

- Justifies: CFM-LPA reported 95.21% new risk detection on 32,581 public loan records, above SMOTE-ENN, LightGBM-GAN and FEEM-VO.

- Justifies: Collaborative filtering over lending patterns generalises risk ratings to new borrowers with sparse individual repayment history.

## Remember This

- CFM-LPA pairs collaborative filtering with federated learning for privacy-preserving micro-lending credit risk assessment.
- Evaluation uses 32,581 public Kaggle loan records against SMOTE-ENN, LightGBM-GAN and FEEM-VO baselines.
- Table 3 gives CFM-LPA 95.21% new risk detection, the highest of the four compared models.
- Abstract and conclusion disagree: 14.03% versus 14.82% risk detection, 13.28% versus 13.63% return rate.
- The behaviour factor is recomputed each repayment period and conditions the next period's credit risk.

## Cited Works

- Zhuang, Y.; Wei, H. (2024) (baseline) — GAN-LightGBM model uses generative adversarial networks for data imbalance and LightGBM to estimate credit risk in fintech. [3 1]
- Aruleba, I.; Sun, Y. (2024) (baseline) — Ensemble of Random Forest, adaptive boosting and XGBoost with SMOTE-ENN plus SHAP improves interpretability and class balance. [3 2]
- Yang, D.; Xiao, B. (2024) (baseline) — Multi-stage ensemble model combines behavioural and non-financial data with bagging-based oversampling for SME credit risk. [3 3]
- Gamba-Santamaria, S.; Melo-Velandia, L. F.; Orozco-Vanegas, C. (2023) (context) — Intrinsic estimators with penalized regression split loan risk into payment capacity and risk-taking components, handling multicollinearity. [3 4]
- Wang, F.; Ding, L.; Yu, H.; Zhao, Y. (2020) (methodology) — Nonlinear least squares SVM builds an index system for credit risk classification in online supply chains. [4 1]
- Rao, C.; Liu, Y.; Goh, M. (2023) (methodology) — Particle swarm optimisation tunes XGBoost hyperparameters for auto loan credit risk while lowering computational cost. [4 2]
- Shetabi, M. (2024) (context) — Evolutionary ensemble feature selection adapts to changing risk factors in FinTech lending. [4 3]
- Xia, H.; Liu, J.; Zhang, Z. J. (2024) (context) — Machine learning classification over platform Q&A text identifies harmful behaviour on online loan platforms. [4 3]
- Sinkey, J. F., Jr.; Greenawalt, M. B. (1991) (context) — Statistical analysis of loan-loss experience and risk-taking at large commercial banks informs lending strategy. [4 4]
- Li, Z.; Liang, S.; Pan, X.; Pang, M. (2024) (context) — Loan profit forecast combining financial and non-financial information improves SME credit risk prediction. [4 4]
- Wang, Y.; Zhang, Y.; Liang, M.; Yuan, R.; Feng, J.; Wu, J. (2023) (baseline) — Heterogeneous ensemble learning with SHAP corrects class imbalance for national student loan default prediction. [4 5]
- Zhang, R.; Lin, C.; Tong, Z. (2021) (context) — Visual early warning system analyses danger indicators in real time for college net loan credit risk. [4 5]
- Liu, P.; Shao, Y. (2013) (context) — Loan securitization and risk-sharing systems reduce revenue volatility for small enterprises. [4 6]
- laotse (Kaggle) () (methodology) — Public Kaggle credit-risk dataset supplies the 32,581 records and 12 features used for all experiments. [6 1]
- Aiello, M. A.; Angelico, C. (2023) (context) — Carbon tax exposure affects business loan default rates at Italian banks, motivating risk-factor based credit assessment. [2 1]

---

Conversion: [`A--Aldrees-2025_marked.md`](../../literature/conversions/A--Aldrees-2025_marked.md) · Summary: [`A--Aldrees-2025_summarized.json`](../../literature/conversions/A--Aldrees-2025_summarized.json)
