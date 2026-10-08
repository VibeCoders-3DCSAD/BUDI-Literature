---
paper_id: A--John-2025
first_author: John
year: 2025
title: "Fair and Explainable Credit-Scoring under Concept Drift: Adaptive Explanation Frameworks for Evolving Populations"
venue: "Not reported"
doi: Not reported
designation: algorithm
status: extracted
modules: [model_algorithm_integration, model_development, model_performance_evaluation]
module_rationale:
  model_algorithm_integration: "Sect. 3.5 (p. 7) builds an Adaptive Explanation Framework that couples XGBoost to three modified SHAP pipelines (Methods A–C), and Fig. 11 (p. 13) compares their final-year feature importance against the static baseline."
  model_development: "Sect. 3.2 (pp. 5–6) specifies the training workflow — XGBoost under a time-aware expanding-window validation scheme in which each yearly model is trained on all prior years and evaluated on the next."
  model_performance_evaluation: "Sect. 3.6 (p. 8) and Sects. 4.2–4.6 (pp. 9–14) report AUC, F1, cosine similarity, Kendall tau, Jaccard overlap, DPD, EOD and counterfactual perturbation response for the baseline and the adaptive explanation methods."
---

# Fair and Explainable Credit-Scoring under Concept Drift: Adaptive Explanation Frameworks for Evolving Populations

## Summary

John (2025) argues that explainability techniques used in credit scoring — principally SHAP — are built on the assumption that the data distribution is static, and that this assumption fails once concept drift reshapes the borrower population. The stated consequence is not only a loss of predictive power but a loss of interpretive and fairness reliability: explanations that were once stable become volatile, and features that once looked neutral can become correlated with protected attributes. The paper's response is an "Adaptive Explanation Framework" of three SHAP variants. Method A (Drift-Weighted SHAP Adjustment) reweights SHAP values by feature-level distribution shift measured with the Population Stability Index or Jensen–Shannon divergence; Method B (Sliding Background Sampling) replaces the fixed SHAP background dataset with a sliding window of recent observations; Method C (Surrogate Ridge Recalibration) fits a Ridge regression surrogate that approximates and smooths SHAP attributions over time. These are benchmarked against static SHAP on a multi-year lending dataset covering 2015–2024, with XGBoost as the predictive model under time-aware expanding-window validation, alongside Logistic Regression and Random Forest. Evaluation covers predictive performance (AUC, F1), explanation stability (cosine similarity, Kendall tau, Jaccard overlap), fairness (Demographic Parity Difference, Equal Opportunity Difference, Equalized Odds Difference) and robustness (background sensitivity, counterfactual perturbation, proxy-variable detection).

The reported pattern is that predictive accuracy holds roughly steady (test AUC 0.63–0.66) while explanation stability and fairness degrade under drift, and that the adaptive variants — Method B most consistently — recover stability and reduce demographic disparity without a loss of accuracy. The paper claims a mean DPD reduction of approximately −0.026 against baseline (95% CI = (−0.035, −0.016), p < 0.05) with AUC unchanged, and reports final-year explanation stability of cosine ≈ 0.995 and Kendall τ ≈ 0.89 for the adaptive framework. Method A is described as producing "mixed results". The contribution the paper claims is conceptual as much as empirical: that adaptability belongs in the explanation layer, not only in the predictive model, so that credit decisions remain auditable as populations change.

## Problem and Motivation

The paper's framing of the problem is that modern credit scoring depends on machine learning models that are deliberately adaptive, while the tools used to explain those models are not. As borrower behaviour, inflation, financial products and post-pandemic spending patterns shift, "the model's understanding of what matters also changes" (Sect. 1.1, p. 1). Widmer and Kubat's (1996) concept drift is invoked as the description of this phenomenon, and Gama et al. (2014) are cited for the observation that the research community has concentrated on detecting and correcting drift to restore accuracy while doing far less to preserve interpretability as data shifts.

Two motivations are pressed. The first is regulatory: under frameworks influenced by the EU's GDPR and the U.S. Equal Credit Opportunity Act, financial institutions must demonstrate that automated decisions are fair, transparent and compliant, and the paper argues that fairness cannot be separated from the environment in which a model operates. If explanations drift, compliance and trust are both undermined. The second is technical: LIME and SHAP were "created with the assumption that data remain relatively stable", relying on static samples or reference points, so in a credit environment where everything from borrower behaviour to market signals changes constantly "those assumptions fall apart" (Sect. 1.1, p. 2).

The paper gives the instability a concrete form: the same borrower might receive a different explanation for an identical outcome six months later. It also connects explanation drift to fairness drift — as borrower profiles shift, features once considered neutral can acquire unintended correlations with sensitive traits such as race or gender — and notes that fairness auditing is not a one-time activity. A third strand is that adaptive learning research refreshes models but leaves "their interpretive logic … frozen in the past" (Sect. 1.2, p. 2). SHAP's dependence on a static background dataset is named as the specific mechanism by which this happens.

## Method

**Design.** The paper states no formal design label; it is an empirical computational study that trains yearly credit-default models over a 2015–2024 lending dataset and benchmarks three adaptive SHAP variants against static SHAP on predictive, stability, fairness and robustness measures.
**Sample.** N Not reported (no record count, no per-year sample size, and no train/test split size is printed anywhere in the paper); the unit of analysis is the individual borrower record within each annual slice of the multi-year lending dataset (Sect. 3.1, p. 4; Sect. 4.1, p. 8).
**Context.** geography: Not reported — no country, region, lender or institution is named; the only institutional marker printed is the author email `5507.students.ku.ac.ke` (p. 1). population: Borrowers in a multi-year lending dataset spanning 2015–2024, described by demographic, financial and socioeconomic variables including income, credit score, age, employment status, debt-to-income ratio and loan amount, with the binary outcome `default`. setting: Computational/offline — XGBoost models retrained annually on accumulated historical data and evaluated on the following year, with SHAP computed on a representative sample of applicants from each year; no live lending platform, no bank and no human participants are involved.

Methodologically the paper proceeds in seven stages. First, dataset construction (Sect. 3.1): a multi-year lending dataset spanning 2015 through 2024, combining demographic, financial and socioeconomic variables, with `default` as the outcome of interest. The paper states that each year's data "has its own personality" and that the setup permits both cross-sectional analysis within a year and trend analysis across years, mirroring what happens inside real banks where models trained on historical data are applied to new borrowers.

Second, drift detection (Sect. 3.2, p. 5) using four statistical tools: the Population Stability Index (PSI) for numerical features, with 2015 as the baseline year and any PSI above 0.25 treated as meaningful drift; the Kolmogorov–Smirnov (KS) test for distribution shape and spread; Jensen–Shannon (JS) divergence for categorical variables; and the Chi-square test for category frequencies. The stated purpose is to distinguish covariate drift (changing feature distributions) from label drift (changing default rate), and to identify which features shift most so that the adaptive explanation methods can target them.

Third, baseline modelling (Sect. 3.2 "Baseline Modeling", pp. 5–6): XGBoost is the primary model, chosen for its handling of nonlinear interactions and heterogeneous data, with Logistic Regression and Random Forest employed alongside it. Training uses a time-aware expanding-window validation strategy in which each yearly model is trained on all prior years and evaluated on the subsequent year, mimicking periodic retraining in a financial institution. Evaluation uses AUC, F1, precision and recall. The paper states that the baseline stage provides the foundation for evaluating predictive drift, explanation drift and fairness drift.

Fourth, fairness analysis over time (Sect. 3.3, p. 6): three metrics — Demographic Parity Difference (DPD), Equal Opportunity Difference (EOD) and Equalized Odds Difference (EODs) — computed per year from cross-tabulated model predictions across sensitive attributes including race, gender, region, age, income group and employment status, and visualised as a temporal series to detect bias drift. SHAP values are integrated into the fairness audit to identify which features most influence outputs for each group, and where significant fairness drift is found, decomposition analysis is used to attribute it to population-level change (data drift) or model-level learning bias (explanation drift).

Fifth, explainability analysis (Sect. 3.4, p. 7): SHAP values computed for each yearly model on a representative sample of that year's applicants, with mean absolute SHAP values averaged into feature importance rankings. The analysis is split into a per-slice view (yearly SHAP summary plots and bar charts) and a longitudinal view (cosine similarity, Kendall tau and Jaccard similarity between consecutive years' importance vectors).

Sixth, the Adaptive Explanation Framework itself (Sect. 3.5, pp. 7–8). Method A, Drift-Weighted SHAP Adjustment, adjusts SHAP weights according to feature distribution changes between training and testing periods, measured with PSI or JS divergence, so that heavily drifted features do not distort interpretation. Method B, Sliding Background Sampling, replaces the fixed SHAP background dataset with a sliding-window background such as "the last 6 months", composed of recent observations, so SHAP values adapt continuously to current data characteristics while transient fluctuations are smoothed. Method C, Surrogate Ridge Recalibration, keeps a small Ridge regression surrogate that learns to approximate SHAP feature attributions over time, monitors the relationship between features and SHAP outputs, and recalibrates attributions when they deviate significantly from past explanatory patterns, acting as a stability smoother.

Seventh, evaluation and statistical testing (Sects. 3.6–3.7, p. 8): four metric families — predictive performance (AUC, F1), explanation stability (cosine, Kendall tau, Jaccard), fairness (group-level disparity measures and group recalibration) and robustness (background sensitivity, counterfactual perturbations, proxy-variable detection). Inference uses paired bootstrap confidence intervals at 95 percent, paired t-tests or Wilcoxon signed-rank tests depending on normality, and temporal correlation coefficients between consecutive years.

## Key Findings

- **Drift is present across numeric, categorical and target variables.** PSI for `annual_income` and `credit_score` rose steadily, reaching approximately 0.16 and 0.017 by 2019 with further increases later; KS tests rejected identical distributions for most numeric variables between consecutive years (p < 0.05); JS divergence for `employment_status` exceeded 0.1 in the 2020–2021 recessionary years, when unemployment reportedly spiked from roughly 5% to over 15%; default rates rose from ~15% in 2015 to over 23% in 2024 (Sect. 4.1, p. 8).
- **Demographic composition was comparatively stable.** Race and gender showed JS divergence values below 0.0002, although Chi-square tests still signalled significant frequency differences in later years (p < 0.05) (Sect. 4.1, p. 8).
- **Predictive accuracy held; calibration did not.** XGBoost maintained test AUC between 0.63 and 0.66 across test years, but F1 remained generally below 0.07 because of class imbalance and the fixed 0.5 threshold; thresholds that balanced precision and recall varied yearly, which the paper reads as degraded calibration stability despite persistent ranking ability (Sect. 4.2, p. 9).
- **Fairness moved with drift.** For race, DPD ranged from approximately 0.01 to 0.03 and EOD from 0.01 to 0.08, with the largest shifts in 2020–2021 when employment-related variables gained predictive influence. The paper concludes that changing input distributions affect fairness behaviour even when model architecture is held constant (Sect. 4.3, p. 10).
- **Method B reduced disparity without cost to AUC.** Mean DPD difference fell by approximately −0.026 against baseline (95% CI = (−0.035, −0.016), p < 0.05) while AUC was unchanged (Sect. 4.3, p. 10).
- **Model reasoning drifted, not just inputs.** Top predictors were consistently `loan_amount`, `dti` and `credit_score`, but their magnitudes and rankings moved; during downturns, income and employment status became more influential and credit score importance declined. By 2024 the top three by mean absolute SHAP value were `loan_amount` (0.055), `dti` (0.034) and `credit_score` (0.023) (Sect. 4.4, p. 11).
- **Baseline explanations were directionally stable but rank-unstable.** Cosine 0.991–0.998, Kendall tau 0.758–0.912, Jaccard top-10 overlap 0.818–1.0 (Sect. 4.4, p. 11).
- **Method B outperformed the other two adaptive variants.** Method A produced "mixed results, that is, modest stability gains in some years, regressions in others"; Method B achieved the highest cosine and Kendall stability scores year-over-year; Method C reached comparable stability but at slightly higher computational cost from continuous surrogate retraining. Methods B and C both produced better top-10 Jaccard overlaps than baseline (Sect. 4.5, pp. 12–13).
- **Counterfactual responses were monotonic.** Decreasing `credit_score` by 10% raised default probability by approximately 0.05; increasing it by 10% lowered it by about 0.035 (Sect. 4.6, p. 14).
- **Proxy variables were detected and then damped.** `loan_amount`, `credit_score` and `annual_income` were statistically associated with race (p < 0.01; η² = 0.017–0.045); adaptive recalibration reduced the frequency and prominence of these proxy features (Sect. 4.6, p. 14).
- **Conclusion-level summary values.** Explanation stability stayed high (cosine ≈ 0.995, Kendall τ ≈ 0.89) and demographic parity difference fell by about 0.026 (p < 0.05); the paper does not state in the conclusion whether the cosine and Kendall figures refer to the baseline or to the adaptive methods (Conclusion, p. 17).

## Key Figures and Tables

The paper contains no numbered tables. Its results are carried by fourteen numbered figures, whose plotted values are not reproduced in the conversion; the numeric values below are those printed in the running text that references each figure.

- **Fig. 1 (p. 5): Loan default rate by year** — referenced by the drift-detection section; the text reports the default rate rising from ~15% in 2015 to over 23% in 2024 (Sect. 4.1, p. 8).
- **Fig. 2 (p. 9): PSI for annual_income and credit_score** — text reports PSI values reaching approximately 0.16 and 0.017 by 2019, with further increases in later years (Sect. 4.1, p. 8).
- **Fig. 3 (p. 9): JS divergence for race and gender** — text reports values below 0.0002 for both attributes, with Chi-square tests still significant in later years (Sect. 4.1, p. 8).
- **Fig. 4 (p. 10): Model test AUC over test years** — text reports test AUC between 0.63 and 0.66 (Sect. 4.2, p. 9).
- **Fig. 5 (p. 10): DPD over time by model for race** — text reports DPD ranging from approximately 0.01 to 0.03 (Sect. 4.3, p. 10).
- **Fig. 6 (p. 11): EOD over time by model for race** — text reports EOD variability of 0.01 to 0.08 (Sect. 4.3, p. 10).
- **Fig. 7 (p. 11): DPD before and after method B recalibration** — text reports a mean DPD difference of approximately −0.026 (95% CI = (−0.035, −0.016), p < 0.05) with AUC unchanged (Sect. 4.3, p. 10).
- **Fig. 8 (p. 12): Explainability stability over time** — text reports baseline cosine 0.991–0.998, Kendall 0.758–0.912 and Jaccard 0.818–1.0 (Sect. 4.4, p. 11).
- **Fig. 9 (p. 12): Top features by the final test year (2024)** — text reports `loan_amount` (0.055), `dti` (0.034), `credit_score` (0.023) (Sect. 4.4, p. 11).
- **Fig. 10 (p. 13): Kendall tau and Cosine similarity over test years for the adaptive methods** — no accompanying numeric values are printed in the text.
- **Fig. 11 (p. 13): Final year feature importance for the baseline and adaptive explainability methods** — no accompanying numeric values are printed in the text.
- **Fig. 12 (p. 13): Number of harmful features detected by each explainability method (baseline and adaptive) using race as the attribute** — no accompanying numeric values are printed in the text, and the term "harmful features" is not defined numerically anywhere in the paper.
- **Fig. 13 (p. 14): Mean probability change from counterfactual perturbations** — text reports a +0.05 change for a 10% decrease and a −0.035 change for a 10% increase in `credit_score` (Sect. 4.6, p. 14).
- **Fig. 14 (p. 15): SHAP background size sensitivity test** — the text reports that baseline SHAP explanations were highly sensitive to background sample size while adaptive methods, especially Method B, showed improved consistency as sample size varied; no numeric sensitivity values are printed (Sect. 4.6, p. 14).

## Limitations and Gaps

Acknowledged by the authors:

- SHAP analysis, while powerful, "can be computationally heavy, especially when applied repeatedly across large datasets or time windows", which the authors state can affect scalability and real-time use (Sect. 5.4, p. 16).
- The fairness assessment "focuses mainly on single attributes like race or gender, while real-world fairness often involves multiple, intersecting factors"; the authors state that future research will need to explore these more complex forms of bias (Sect. 5.4, p. 16).
- Recalibration in this study "was done manually at intervals" rather than continuously; the authors propose integrating statistical drift detectors such as PSI, Kullback-Leibler divergence or KS tests to trigger automatic retraining or explanation updates (Sect. 6, p. 16).
- The study has not been applied to real banking data or live credit-scoring systems; the authors note that real financial data brings missing information, delayed updates, regulatory limits and evolving credit products, and propose collaboration with banks or fintech firms (Sect. 6, p. 16).
- Method C "incurred slightly higher computational cost due to continuous surrogate retraining" (Sect. 4.5, p. 13).

Not acknowledged by the authors:

- [unacknowledged] The sample size is never printed. No total record count, no per-year N, no train/test split size and no number of applicants sampled for SHAP appears anywhere in the paper, so no reported proportion can be converted into a count and no precision of the estimates can be checked.
- [unacknowledged] The dataset is never sourced. Sect. 3.1 describes a "multi-year lending dataset" spanning 2015–2024 but names no provider, no collection instrument, no access route and no licence, and the References contain no data citation. The provenance and therefore the reproducibility of every drift, fairness and stability result is unverifiable from the paper.
- [unacknowledged] The figures carry the results and their data are not recoverable from the text. Fourteen figures are referenced, several (Figs. 10, 11, 12, 14) are discussed without a single numeric value in the running text, and no figure data table is supplied. Ranges such as "0.63 to 0.66" or "0.991–0.998" give the span but never the per-year values, so no reader can reconstruct the time series that the paper's central claim about temporal stability depends on.
- [unacknowledged] Method A is reported without numbers. The paper states that Method A "produced mixed results, that is, modest stability gains in some years, regressions in others" (Sect. 4.5, p. 12) but prints no cosine, Kendall or Jaccard value for it in any year, so the negative result cannot be assessed.
- [unacknowledged] Method C is reported without cost numbers. The claim of "slightly higher computational cost" (Sect. 4.5, p. 13) is not accompanied by any runtime, memory or training-cost measurement.
- [unacknowledged] Fairness results are printed only for race. Sect. 3.3 states that fairness was audited across race, gender, region, age, income group and employment status, but every printed DPD and EOD value in Sect. 4.3 and every fairness figure (Figs. 5–7) concerns race alone. The other five attributes are asserted to have been audited and are never reported.
- [unacknowledged] No confidence interval or p-value is printed for any explanation-stability metric. The only inferential statistics in the paper are attached to the DPD result (95% CI = (−0.035, −0.016), p < 0.05), the KS and Chi-square tests in drift detection, and the proxy-variable association (p < 0.01). Cosine, Kendall tau and Jaccard values are reported as bare ranges.
- [unacknowledged] The reported PSI values fall below the paper's own drift threshold. Sect. 3.2 (p. 5) states that "any PSI above 0.25 was treated as a sign of meaningful drift", yet Sect. 4.1 (p. 8) reports PSI values of approximately 0.16 and 0.017 by 2019 and describes them as "indicating ongoing population drift". The paper does not print the later PSI values that would resolve whether the threshold was eventually crossed, and it does not reconcile the two statements.
- [unacknowledged] The Conclusion restates the DPD improvement without its sign. Sect. 4.3 prints "approximately -0.026"; the Conclusion prints "reduced by about 0.026" (p. 17). The two are consistent in magnitude but the Conclusion does not carry the sign or the confidence interval. Both are recorded below with their distinct locators.
- [unacknowledged] The Conclusion's stability figures are unattributed. "Explanation stability stayed high (cosine ≈ 0.995, Kendall τ ≈ 0.89)" (Conclusion, p. 17) does not say whether these refer to the baseline, to Method B, to Method C, or to an average, and they cannot be matched to the baseline ranges printed in Sect. 4.4 (0.991–0.998 and 0.758–0.912), which overlap them.
- [unacknowledged] The in-text citation numbers do not match the reference list. Numbering restarts by section and does not correspond to the final list: Sect. 1.1 cites "Barocas et al. (2023) … [1]" while reference [1] is Alvarez-Melis and Jaakkola (2018); Sect. 2.1 cites "Bussmann et al. (2021) … [1]" while reference [1] is again Alvarez-Melis and Jaakkola; Sect. 5.1 cites "Miller (2019) … [1]" while Miller is reference [15]. Two references (Barocas, Hardt and Narayanan 2019 and 2023) are listed separately as [3] and [4]. The citation apparatus cannot be resolved by a reader without manual matching.
- [unacknowledged] Sections are numbered inconsistently: "3.2 Drift Detection" (p. 5) and "3.2 Baseline Modeling" (p. 5) carry the same number, so cross-references to Sect. 3.2 are ambiguous.
- [unacknowledged] The "harmful features" quantity plotted in Fig. 12 is never defined. The paper does not state how a feature is classified as harmful, what threshold or test is used, or what the counts were for any method, so the figure cannot be interpreted from the text.
- [unacknowledged] No per-year AUC, F1, precision or recall is printed. Only a range (0.63–0.66) and an upper bound ("generally below 0.07") are given, so the claim that predictive accuracy was maintained across the full period rests on an interval rather than on the yearly values the expanding-window design produces.
- [unacknowledged] No code, artefact or data availability statement is provided, and the paper names no software, library version or computational environment, so the pipeline cannot be reproduced.
- [unacknowledged] The fairness recalibration embedded in Method B is described as adjusting thresholds or reweighting features for different demographic groups (Sect. 3.3, p. 6), but no threshold value, group weight or recalibration rule is printed, so the mechanism by which the reported −0.026 DPD reduction was achieved cannot be inspected.

## Definitions

- **Concept drift** — the situation in which relationships learned from past data stop holding once the underlying patterns move in a different direction (Widmer and Kubat 1996, cited in Sect. 1.1, p. 1).
- **Covariate drift** — drift in which input distributions shift; distinguished in Sect. 2.2 (p. 3) from **prior drift**, in which class proportions change, and **concept drift**, in which the link between inputs and outputs itself evolves.
- **Population Stability Index (PSI)** — the measure used to quantify how much numerical features such as income, credit score or debt-to-income ratio shift over time, with 2015 as baseline and 0.25 as the meaningful-drift threshold (Sect. 3.2, p. 5).
- **Kolmogorov–Smirnov (KS) test** — used to compare the shapes of distributions and detect significant change in range or spread for features such as loan amount or annual income (Sect. 3.2, p. 5).
- **Jensen–Shannon (JS) divergence** — an information-theoretic measure of how much two probability distributions differ, applied in this study to categorical variables (Sect. 3.2, p. 5).
- **SHAP (SHapley Additive exPlanations)** — a game-theory-based method that breaks a model's prediction into individual feature contributions (Sect. 3.4, p. 7); introduced by Lundberg and Lee (2017) and described as mathematically grounded but dependent on a static background dataset (Sect. 1.2, p. 2).
- **Method A — Drift-Weighted SHAP Adjustment** — recalibrates SHAP values by adjusting their weights according to feature distribution changes between training and testing periods, using PSI or JS divergence as the adjustment signal (Sect. 3.5, p. 7).
- **Method B — Sliding Background Sampling** — replaces the static SHAP reference dataset with a sliding-window background of recent observations, allowing SHAP values to adapt to the most recent data characteristics (Sect. 3.5, p. 7).
- **Method C — Surrogate Ridge Recalibration** — a Ridge regression surrogate that approximates SHAP feature attributions over time and recalibrates them when they deviate significantly from past explanatory patterns (Sect. 3.5, p. 7).
- **Demographic Parity Difference (DPD)** — evaluates whether the rate of positive predictions, such as loan approvals, is consistent across protected groups (Sect. 3.3, p. 6).
- **Equal Opportunity Difference (EOD)** — assesses whether groups have equal true positive rates, meaning whether qualified applicants from all groups have an equal chance of receiving approval (Sect. 3.3, p. 6).
- **Equalized Odds Difference (EODs)** — extends EOD by considering both true positive and false positive rates, ensuring fairness in both acceptance and rejection patterns (Sect. 3.3, p. 6).
- **Bias drift** — the year-to-year change in disparity magnitude, detected by visualising each fairness metric as a temporal series (Sect. 3.3, p. 6).
- **Cosine similarity** — measures how aligned the direction of feature importance vectors is between consecutive years (Sect. 3.4, p. 7).
- **Kendall tau** — measures how well the ranking of features stays consistent across years (Sect. 3.4, p. 7).
- **Jaccard similarity** — measures whether the same key features continue to appear among the top-ranked drivers of model decisions (Sect. 3.4, p. 7).
- **Time-aware expanding-window validation** — each yearly model is trained using all prior years' data and evaluated on the subsequent year, mimicking periodic retraining as new borrower data accumulates (Sect. 3.2 "Baseline Modeling", p. 6).
- **Proxy variable** — a non-sensitive feature that may secretly act as a stand-in for a protected attribute; tested in this study by checking non-sensitive features for statistical association with race (Sect. 3.6, p. 8).
- **Harmful features** — a term appearing only in the caption of Fig. 12 (p. 13); the paper does not define it, state how harmfulness is determined, or report the counts.
- **Group recalibration** — the mechanism, embedded particularly in Method B, that adjusts thresholds or reweights features for demographic groups to reduce observed disparities while maintaining predictive consistency (Sect. 3.3, p. 6).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Population drift in annual_income | Population Stability Index (PSI) by 2019 | 0.16 | — | — | Sect. 4.1, p. 8 |
| Population drift in credit_score | Population Stability Index (PSI) by 2019 | 0.017 | — | — | Sect. 4.1, p. 8 |
| Distributional shift in most numeric variables between consecutive years | Kolmogorov–Smirnov test p-value | p < 0.05 | — | <0.05 | Sect. 4.1, p. 8 |
| Composition change in employment_status, recessionary years (2020–2021) | Jensen–Shannon divergence | exceeding 0.1 | — | — | Sect. 4.1, p. 8 |
| Unemployment rate, recessionary years (2020–2021) | unemployment rate | from roughly 5% to over 15% | — | — | Sect. 4.1, p. 8 |
| Composition change in race | Jensen–Shannon divergence | below 0.0002 | — | — | Sect. 4.1, p. 8 |
| Composition change in gender | Jensen–Shannon divergence | below 0.0002 | — | — | Sect. 4.1, p. 8 |
| Frequency differences in demographic variables, later years | Chi-square test p-value | p < 0.05 | — | <0.05 | Sect. 4.1, p. 8 |
| Default rate, 2015 | default rate | ~15% | — | — | Sect. 4.1, p. 8 |
| Default rate, 2024 | default rate | over 23% | — | — | Sect. 4.1, p. 8 |
| Baseline XGBoost discrimination across test years | test AUC | 0.63 to 0.66 | — | — | Sect. 4.2, p. 9 |
| Baseline XGBoost classification balance across test years | F1 score | below 0.07 | — | — | Sect. 4.2, p. 9 |
| Fairness drift for race | Demographic Parity Difference (DPD) | 0.01 to 0.03 | — | — | Sect. 4.3, p. 10 |
| Fairness drift for race | Equal Opportunity Difference (EOD) | 0.01 to 0.08 | — | — | Sect. 4.3, p. 10 |
| Fairness improvement after Method B recalibration | mean DPD difference vs baseline | -0.026 | (-0.035, -0.016) | <0.05 | Sect. 4.3, p. 10 |
| Predictive performance after Method B recalibration | AUC | unchanged | — | — | Sect. 4.3, p. 10 |
| Top feature by mean absolute SHAP value, final test year 2024 | loan_amount mean absolute SHAP | 0.055 | — | — | Sect. 4.4, p. 11 |
| Second feature by mean absolute SHAP value, final test year 2024 | dti mean absolute SHAP | 0.034 | — | — | Sect. 4.4, p. 11 |
| Third feature by mean absolute SHAP value, final test year 2024 | credit_score mean absolute SHAP | 0.023 | — | — | Sect. 4.4, p. 11 |
| Baseline SHAP directional stability across years | cosine similarity | 0.991–0.998 | — | — | Sect. 4.4, p. 11 |
| Baseline SHAP rank stability across years | Kendall tau | 0.758–0.912 | — | — | Sect. 4.4, p. 11 |
| Baseline SHAP top-10 feature overlap across years | Jaccard overlap | 0.818–1.0 | — | — | Sect. 4.4, p. 11 |
| Counterfactual perturbation, credit_score decreased by 10% | change in default probability | +0.05 | — | — | Sect. 4.6, p. 14 |
| Counterfactual perturbation, credit_score increased by 10% | change in default probability | -0.035 | — | — | Sect. 4.6, p. 14 |
| Proxy-variable association of loan_amount, credit_score and annual_income with race | p-value | p < 0.01 | — | <0.01 | Sect. 4.6, p. 14 |
| Proxy-variable association with race | eta-squared | 0.017–0.045 | — | — | Sect. 4.6, p. 14 |
| Explanation stability of the adaptive framework (restated in conclusion) | cosine similarity | ≈ 0.995 | — | — | Conclusion, p. 17 |
| Explanation stability of the adaptive framework (restated in conclusion) | Kendall tau | ≈ 0.89 | — | — | Conclusion, p. 17 |
| Fairness improvement restated in the conclusion | demographic parity difference reduction | about 0.026 | — | <0.05 | Conclusion, p. 17 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "Evolving borrower behaviors, shifting economic conditions, and changing regulatory landscapes continuously reshape the data distributions underlying modern credit-scoring systems." | Abstract, p. 1 | model_algorithm_integration |
| "Conventional explainability techniques, such as SHAP, assume static data and fixed background distributions, making their explanations unstable and potentially unfair when concept drift occurs." | Abstract, p. 1 | model_algorithm_integration |
| "Results show that adaptive methods, particularly rebaselined and surrogate-based explanations, substantially improve temporal stability and reduce disparate impact across demographic groups without degrading predictive accuracy." | Abstract, p. 1 | model_algorithm_integration |
| "The same borrower might get a different explanation for an identical outcome six months later." | Sect. 1.1, p. 2 | model_algorithm_integration |
| "Models are refreshed, but their interpretive logic remains frozen in the past." | Sect. 1.2, p. 2 | model_algorithm_integration |
| "The tension between adaptability and explainability is at the center of this research." | Sect. 1.1, p. 2 | model_algorithm_integration |
| "The year 2015 served as the baseline, and any PSI above 0.25 was treated as a sign of meaningful drift" | Sect. 3.2, p. 5 | model_development |
| "each yearly model is trained using all prior years' data and evaluated on the subsequent year" | Sect. 3.2 Baseline Modeling, p. 6 | model_development |
| "The goal here isn't only to measure accuracy but to understand how the model's reasoning, feature importance, and fairness shift as the world around it changes." | Sect. 3.1, p. 4 | model_development |
| "the models maintained moderate but stable discrimination power, with test AUC values between 0.63 and 0.66" | Sect. 4.2, p. 9 | model_performance_evaluation |
| "F1 scores remained low (generally below 0.07) due to class imbalance and the fixed 0.5 threshold used for binary classification" | Sect. 4.2, p. 9 | model_performance_evaluation |
| "The correlation between drift and fairness imbalance confirms that changing input distributions directly affects fairness behavior, even when the model architecture remains constant." | Sect. 4.3, p. 10 | model_performance_evaluation |
| "Method A, which reweights SHAP values according to feature distribution changes, produced mixed results, that is, modest stability gains in some years, regressions in others." | Sect. 4.5, p. 12 | model_algorithm_integration |
| "Method B delivered the most consistent improvements, achieving the highest cosine and Kendall stability scores year-over-year." | Sect. 4.5, p. 12 | model_algorithm_integration |
| "Background sensitivity tests revealed that baseline SHAP explanations were highly sensitive to background sample size" | Sect. 4.6, p. 14 | model_performance_evaluation |
| "SHAP explanations, while clear in short snapshots, became less consistent when examined across multiple years." | Conclusion, p. 17 | model_performance_evaluation |
| "SHAP analysis, while powerful, can be computationally heavy, especially when applied repeatedly across large datasets or time windows." | Sect. 5.4, p. 16 | model_algorithm_integration |
| "the fairness assessment focuses mainly on single attributes like race or gender, while real-world fairness often involves multiple, intersecting factors" | Sect. 5.4, p. 16 | model_performance_evaluation |

## Remember This

- The paper's claim is that adaptability belongs in the explanation layer, not only in the predictive model; it proposes three modified SHAP pipelines (Methods A, B, C) and benchmarks them against static SHAP on a 2015–2024 lending dataset.
- Test AUC held at 0.63–0.66 while explanation rankings moved (baseline Kendall tau 0.758–0.912), which the paper reads as predictive stability masking interpretive instability.
- Method B (sliding background sampling) is the best-performing variant; Method A is described as "mixed" and Method C as comparable but costlier — neither A nor C is given any numeric result.
- The only inferential statistics printed for the headline fairness claim are the DPD figures: −0.026 mean difference, 95% CI (−0.035, −0.016), p < 0.05.
- No sample size, no dataset source, and no per-year values are printed anywhere; the results live in fourteen figures whose plotted data are not tabulated.

## Cited Works

Reference-list numbers are given as printed in the paper's final list. The paper's in-text citation numbers do not correspond to these and restart by section (see Limitations).

- [1] Alvarez-Melis, D.; Jaakkola, T. S. (2018) — cited for the finding that small data changes can cause large swings in explanation outputs and that interpretability methods lack stability mechanisms. [Sect. 2.4]
- [2] Baena-García, M.; del Campo-Ávila, J.; Fidalgo, R.; Bifet, A.; Gavalda, R.; Morales-Bueno, R. (2006) — early drift detection method (EDDM) monitoring model error rates to signal retraining; criticised in the paper for tracking accuracy only. [Sect. 2.2]
- [3] Barocas, S.; Hardt, M.; Narayanan, A. (2019) — conceptual foundation for assessing and mitigating bias; fairness must be evaluated in context. [Sect. 2.3]
- [4] Barocas, S.; Hardt, M.; Narayanan, A. (2023) — fairness in AI cannot be separated from the environments in which models operate; fairness requires continuous attention. [Sect. 1.1, 1.2]
- [5] Bracke, P.; Datta, A.; Jung, C.; Sen, S. (2019) — Bank of England working paper using LIME and SHAP to trace how income, employment history and credit utilisation affect default predictions. [Sect. 2.1]
- [6] Bussmann, N.; Giudici, P.; Marinelli, D.; Papenbrock, J. (2021) — explainable machine learning supports regulatory compliance and operational accountability in credit risk management. [Sect. 2.1]
- [7] Doshi-Velez, F.; Kim, B. (2017) — interpretability should rest on consistent, scientific reasoning rather than heuristics or visual tricks. [Sect. 1.2]
- [8] Gama, J.; Žliobaitė, I.; Bifet, A.; Pechenizkiy, M.; Bouchachia, A. (2014) — survey on concept drift adaptation; used to argue that drift research focuses on accuracy and neglects interpretability. [Sect. 1.1, 1.2, 2.2]
- [9] Hardt, M.; Price, E.; Srebro, N. (2016) — equality of opportunity: people with the same qualifications should have equal chances across groups. [Sect. 2.3]
- [10] Kamiran, F.; Calders, T. (2012) — data preprocessing techniques that remove or reweight biased samples before training. [Sect. 2.3]
- [11] Kusner, M. J.; Loftus, J. R.; Russell, C.; Silva, R. (2017) — counterfactual fairness: whether a prediction would change if a sensitive attribute were altered. [Sect. 2.3]
- [12] Lu, J.; Liu, A.; Dong, F.; Gu, F.; Gama, J.; Zhang, G. (2019) — review of learning under concept drift; source of the covariate/prior/concept drift distinction used in this paper. [Sect. 2.2]
- [13] Lundberg, S. M.; Lee, S.-I. (2017) — the SHAP method itself, described as providing a mathematically grounded way to assign feature importance using cooperative game theory. [Sect. 1.1, 1.2]
- [14] Mehrabi, N.; Morstatter, F.; Saxena, N.; Lerman, K.; Galstyan, A. (2021) — survey of bias and fairness in machine learning; source of the demographic parity, equal opportunity and individual fairness metric families. [Sect. 2.3]
- [15] Miller, T. (2019) — explanations in AI are social tools as well as technical ones; human-centred explanations promote fairness and trust. [Sect. 5.1, 5.2]
- [16] Nauta, M.; van Bree, R.; Seifert, C. (2022) — stability of feature attribution methods; explanations vary across retrainings or slight data changes. [Sect. 2.1]
- [17] Raji, I. D.; Smart, A.; White, R. N.; Mitchell, M.; Gebru, T.; Hutchinson, B.; Smith-Loud, J.; Theron, D.; Barnes, P. (2020) — end-to-end framework for internal algorithmic auditing; accountability should cover every stage from design to post-deployment. [Sect. 5.1, 5.2, 5.3]
- [18] Ribeiro, M. T.; Singh, S.; Guestrin, C. (2016) — LIME and the finding that explanations influence how people trust AI systems. [Sect. 1.1, 1.2]
- [19] Selbst, A. D.; Barocas, S. (2018) — explainable systems translate complex model reasoning into moral and legal language people can understand. [Sect. 5.3]
- [20] Slack, D.; Hilgard, S.; Jia, E.; Singh, S.; Lakkaraju, H. (2020) — LIME and SHAP can be manipulated by adversarial changes, producing misleading interpretations. [Sect. 2.4]
- [21] Sokol, K.; Flach, P. (2020) — Explainability Fact Sheets for systematically assessing explainable approaches; the paper notes this improves transparency but does not solve explanation consistency under drift. [Sect. 2.4]
- [22] Webb, G. I.; Hyde, R.; Cao, H.; Nguyen, H. L.; Petitjean, F. (2016) — characterises drift as sudden, incremental, recurring or gradual. [Sect. 2.2]
- [23] Widmer, G.; Kubat, M. (1996) — origin of the concept drift description used in the introduction: relationships learned from past data stop holding once underlying patterns move. [Sect. 1.1]
- [24] Zhang, Z.; Chen, L. (2022) — survey of explainable credit risk modelling outlining four challenges: interpretability versus predictive power, measuring explanation stability, fairness under changing data, and interpretability in live systems. [Sect. 2.1]
- [25] Žliobaitė, I. (2010) — argues drift adaptation should go beyond retraining and include systems that keep explanations stable over time. [Sect. 2.2]