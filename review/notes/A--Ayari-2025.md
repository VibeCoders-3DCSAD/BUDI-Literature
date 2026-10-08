---
paper_id: A--Ayari-2025
first_author: Ayari
year: 2025
title: "Machine learning powered financial credit scoring: a systematic literature review"
venue: "Artificial Intelligence Review"
doi: 10.1007/s10462-025-11416-2
designation: algorithm
status: extracted
modules: [model_algorithm_integration, model_performance_evaluation, rule_based_classification]
module_rationale:
  model_algorithm_integration: "The review systematically synthesises hybrid and ensemble architectures that combine multiple ML algorithms for credit scoring, including RF-SVM, GA-NN, multi-stage ensembles, and stacking frameworks (Sect. 4.1.6, Sect. 4.3.3, Tables 4–6)."
  model_performance_evaluation: "The paper compiles and ranks accuracy and AUC results across four benchmark datasets (German, Australian, Japanese, Lending Club) and catalogs 28 evaluation metrics with their frequency of use (Tables 3, 7–10, Sect. 5–6.3)."
  rule_based_classification: "Decision trees and rule-based models are reviewed as interpretable classifiers for credit scoring, including C4.5, CART, and PLTR which uses short-depth DT rules as predictors in logistic regression (Sect. 4.1.2, Sect. 4.1.1)."
---

## Summary

A systematic literature review of 63 studies published between 2018 and 2024 on machine learning methods for financial credit scoring. The review covers traditional ML models (logistic regression, decision trees, random forest, SVM, KNN), deep learning models (ANN, CNN, LSTM, hybrid DL), and ensemble learning models (gradient boosting, XGBoost, hybrid ensembles). It synthesises performance results across the German, Australian, Japanese, and Lending Club benchmark datasets, catalogs 28 evaluation metrics, and identifies emerging trends in alternative data, explainability, and key adoption challenges including interpretability, bias, and the curse of dimensionality.

## Problem and Motivation

Credit scoring has become a cornerstone of modern lending, enabling banks and financial institutions to assess borrower creditworthiness and reduce default risk. Traditional models based on logistic regression and scorecards are valued for interpretability and regulatory acceptance, but they depend on narrow feature sets, assume linear relationships, and struggle to model complex behavioral patterns. Machine learning models can capture nonlinearities, handle high-dimensional data, and adapt to evolving borrower behavior, yet several research challenges persist: many studies lack standardized datasets, preprocessing methods, or evaluation metrics, hindering cross-study comparisons; complex models such as deep learning and hybrid systems often lack interpretability; integrating alternative data sources raises ethical and privacy concerns; algorithmic bias remains insufficiently addressed; and high-dimensional inputs can lead to overfitting or computational inefficiency. This systematic literature review synthesises existing research to identify major ML methods, assess their strengths and limitations, highlight trends and advancements, and address critical challenges in adoption.

## Method

**Design.** Systematic literature review (SLR) following PRISMA 2020 guidelines; the authors state no formal protocol registration (like PROSPERO) was undertaken, but the methodology was defined in advance to ensure transparency and reproducibility.
**Sample.** n = 63 primary studies (48 journal articles, 13 conference papers) selected from 345 identified studies through database searches and backward snowballing, published between January 2018 and December 2024.
**Context.** geography: International (studies span Australia, Germany, Japan, Taiwan, China, India, Indonesia, Vietnam, Chile, Poland, Bosnia, and others); population: Credit scoring research covering individual borrowers, peer-to-peer lending, mortgage loans, micro-lending, and personal bankruptcy prediction; setting: Systematic literature review of publications from four digital libraries: SpringerLink, ACM Digital Library, IEEE Xplore, and Google Scholar.

## Software

- VOSviewer (version not reported) for bibliographic coupling and keyword co-occurrence analysis
- Excel spreadsheet (version not reported) for structured data extraction

## Key Findings

- Hybrid ensemble models are the most widely used and effective approaches for credit scoring, consistently outperforming single classifiers in accuracy and discrimination power across benchmark datasets.
- Traditional ML models (LR, DT, SVM) remain relevant when interpretability and simplicity are prioritised, particularly for smaller datasets and regulatory compliance.
- DL models show promise for large, high-dimensional datasets but are less frequently adopted due to data-intensive requirements and limited interpretability.
- Accuracy remains the most commonly reported metric (49 uses), followed by AUC (31 uses), F1-score (25 uses), and recall (24 uses), but accuracy is misleading for imbalanced datasets, which are common in credit scoring.
- The most frequently used public datasets were German, Australian, and Japanese credit datasets, while about one-third of studies relied on proprietary institutional datasets.
- Alternative data sources (social media, mobile phone usage, psychometric assessments) are an emerging trend that can enhance credit scoring, particularly for borrowers lacking formal credit histories.
- Explainability methods such as LIME and SHAP are increasingly important for transparency and regulatory compliance.
- Key challenges include interpretability of complex models, potential biases in training data, the curse of dimensionality, and integration of behavioral and attitudinal data.

## Key Figures and Tables

- Fig. 1 (p. 23): PRISMA 2020 flow diagram showing study selection from 345 identified to 63 included studies.
- Fig. 2 (p. 33): Comparative accuracy (± standard deviation) of machine learning models in credit scoring.
- Fig. 3 (p. 34): Comparative accuracy (± standard deviation) of DL models in credit scoring.
- Fig. 4 (p. 34): Comparative accuracy (± standard deviation) of EL models in credit scoring.
- Fig. 5 (p. 35): Bibliographic coupling network of included studies showing three main conceptual clusters.
- Fig. 6 (p. 36): Keyword co-occurrence map showing six thematic clusters.
- Table 1 (p. 5): Selected digital libraries — SpringerLink, ACM Digital Library, IEEE Xplore, Google Scholar.
- Table 2 (p. 21): Binary confusion matrix with TP, FN, FP, TN definitions.
- Table 3 (p. 22): Evaluation metrics and frequency — accuracy 49, AUC 31, F1-score 25, recall 24, KS 13, specificity 14, precision 13, Brier Score 10, G-Mean 10, and 19 additional metrics.
- Tables 4–6 (pp. 24–31): Summary of studies for traditional ML, deep learning, and ensemble learning models with datasets and evaluation metrics.
- Table 7 (p. 32): Comparative evaluation on German dataset, ranked by combined accuracy and AUC.
- Table 8 (p. 32): Ranked comparative evaluation on Australian dataset.
- Table 9 (p. 33): Ranked comparative evaluation on Japanese dataset.
- Table 10 (p. 33): Ranked comparative evaluation on Lending Club dataset.
- Table 11 (p. 36): Global most cited documents — Dumitrescu et al. (410), He et al. (313), Moscato (284), Shen et al. (225), Bao et al. (222).

## Limitations and Gaps

- The authors acknowledge that the review is limited by the heterogeneity of datasets, evaluation metrics, and methodologies in the literature, which complicates direct performance comparisons (Sect. 8, p. 47; Sect. 9, p. 48).
- The authors acknowledge that the search was confined to only four online databases (IEEE Xplore, ACM Digital Library, Springer Link, and Google Scholar), and other digital libraries with relevant studies may have been overlooked (Sect. 8, p. 47).
- The authors acknowledge that identifying all relevant research published within the five-year scope proved challenging due to the increasing volume of studies in the field (Sect. 8, p. 47).
- The authors acknowledge that the review lacks a comparative analysis to identify the most effective models for credit scoring because reviewed articles often used different evaluation metrics, even when relying on common datasets (Sect. 8, p. 47).
- [unacknowledged] The abstract reports 330 research papers extracted from databases, while Sect. 6.1 reports 345 studies identified through database searches and backward snowballing — the two figures are inconsistent.
- [unacknowledged] The paper reports 63 included studies comprising 48 journal articles (79%) and 13 conference papers (21%), but 48 + 13 = 61, not 63; the percentages are also inconsistent with 48/63 = 76.2% and 13/63 = 20.6%.
- [unacknowledged] The paper states it covers publications from January 2018 to December 2024, a seven-year span, but describes this as a "five-year scope" in Sect. 8 (p. 47).
- [unacknowledged] The ranked comparison tables (Tables 7–10) mix accuracy and AUC from different studies that use different preprocessing, feature selection, and evaluation protocols, so the rankings do not constitute a controlled comparison.
- [unacknowledged] Tables 4–6 contain numerous instances of "AN" (not reported) for evaluation metrics, yet these studies are still included in the synthesis; the extent of missing data is not quantified.
- [unacknowledged] The paper does not report inter-rater reliability or agreement statistics for the study selection or quality assessment process.
- [unacknowledged] The quality assessment threshold of 77% is described as a "pragmatic benchmark" without justification or sensitivity analysis.
- [unacknowledged] The paper claims to address "RQ5: What are the challenges in adopting ML models" but the challenges discussed (interpretability, bias, curse of dimensionality) are well-known from prior literature rather than emerging from the review's own synthesis.

## Definitions

- **Credit scoring** — A systematic, data-driven approach to evaluating borrower creditworthiness that quantifies credit risk using applicants' financial behavior and repayment history.
- **PD (Probability of Default)** — Derived from historical repayment data, the most influential factor in Expected Credit Loss estimation under IFRS 9.
- **EAD (Exposure at Default)** — The loan exposure subject to credit risk.
- **LGD (Loss Given Default)** — The proportion of unrecovered assets, calculated as one minus the recovery rate.
- **IFRS 9** — International Financial Reporting Standard 9, which mandates estimation of Expected Credit Loss through PD, EAD, and LGD parameters.
- **SMOTE** — Synthetic Minority Over-sampling Technique, used to address class imbalance in credit scoring datasets.
- **XGBoost** — Extreme Gradient Boosting, an ensemble model combining tree models with gradient boosting.
- **G-Mean** — Geometric Mean, a metric balancing sensitivity and specificity.
- **KS statistic** — Kolmogorov–Smirnov statistic, widely used in credit scoring to measure discriminatory power.
- **LIME** — Local Interpretable Model-agnostic Explanations, a method for explaining black-box model predictions.
- **SHAP** — SHapley Additive exPlanations, a method quantifying the marginal contribution of each feature to a prediction.

## Key Equations

- `P(Y = 1 | x) = 1 / (1 + e^{-(β₀ + βᵀx)})` — Logistic regression probability of default (formula 1, p. 8).
- `ℓ(β₀, β) = Σ [yᵢ log p(xᵢ) + (1 − yᵢ) log(1 − p(xᵢ))]` — Log-likelihood function for logistic regression (formula 2, p. 9).
- `Accuracy = (TP + TN) / (TP + TN + FP + FN)` — Accuracy formula (formula 3, p. 21).
- `Precision = TP / (TP + FP)` — Precision formula (formula 4, p. 21).
- `Recall = TP / (TP + FN)` — Recall formula (formula 5, p. 21).
- `F1-Score = 2 × (Precision × Recall) / (Precision + Recall)` — F1-score formula (formula 6, p. 21).
- `Specificity = TN / (TN + FP)` — Specificity formula (formula 7, p. 22).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Studies identified through database searches and backward snowballing | count | 345 | — | — | Sect. 6.1, p. 23 |
| Primary studies included in final synthesis | count | 63 | — | — | Sect. 6.1, p. 23 |
| Journal articles among included studies | count (%) | 48 (79%) | — | — | Sect. 6.1, p. 23 |
| Conference papers among included studies | count (%) | 13 (21%) | — | — | Sect. 6.1, p. 23 |
| Research papers extracted from four databases (abstract) | count | 330 | — | — | Abstract, p. 1 |
| Accuracy usage count across reviewed studies | count | 49 | — | — | Table 3, p. 22 |
| AUC usage count across reviewed studies | count | 31 | — | — | Table 3, p. 22 |
| F1-Score usage count across reviewed studies | count | 25 | — | — | Table 3, p. 22 |
| Recall usage count across reviewed studies | count | 24 | — | — | Table 3, p. 22 |
| Specificity usage count across reviewed studies | count | 14 | — | — | Table 3, p. 22 |
| KS usage count across reviewed studies | count | 13 | — | — | Table 3, p. 22 |
| Precision usage count across reviewed studies | count | 13 | — | — | Table 3, p. 22 |
| Brier Score usage count across reviewed studies | count | 10 | — | — | Table 3, p. 22 |
| G-Mean usage count across reviewed studies | count | 10 | — | — | Table 3, p. 22 |
| Type II error usage count across reviewed studies | count | 7 | — | — | Table 3, p. 22 |
| H-measure usage count across reviewed studies | count | 6 | — | — | Table 3, p. 22 |
| Type I error usage count across reviewed studies | count | 5 | — | — | Table 3, p. 22 |
| German dataset, GA + NN (Kazemi et al. 2023) | accuracy | 91.91% | — | — | Table 7, p. 32 |
| German dataset, GA + NN (Kazemi et al. 2023) | AUC | 92.60% | — | — | Table 7, p. 32 |
| German dataset, AugBoost-ELM (Zou and Gao 2022) | accuracy | 76.17% | — | — | Table 7, p. 32 |
| German dataset, AugBoost-ELM (Zou and Gao 2022) | AUC | 94.22% | — | — | Table 7, p. 32 |
| German dataset, gcForest (Li et al. 2021) | accuracy | 81.20% | — | — | Table 7, p. 32 |
| German dataset, gcForest (Li et al. 2021) | AUC | 86.80% | — | — | Table 7, p. 32 |
| German dataset, SVM-RF (Yao and Chen 2019) | accuracy | 83.55% | — | — | Table 7, p. 32 |
| German dataset, SVM-RF (Yao and Chen 2019) | AUC | 84.00% | — | — | Table 7, p. 32 |
| German dataset, Proposed (Zhang et al. 2021) | accuracy | 79.50% | — | — | Table 7, p. 32 |
| German dataset, Proposed (Zhang et al. 2021) | AUC | 83.84% | — | — | Table 7, p. 32 |
| German dataset, Multi-stage ensemble (Zhang et al. 2021) | accuracy | 79.50% | — | — | Table 7, p. 32 |
| German dataset, Multi-stage ensemble (Zhang et al. 2021) | AUC | 83.12% | — | — | Table 7, p. 32 |
| German dataset, Proposed (Shen et al. 2019) | accuracy | 78.70% | — | — | Table 7, p. 32 |
| German dataset, Proposed (Shen et al. 2019) | AUC | 81.02% | — | — | Table 7, p. 32 |
| German dataset, XGB-BO (Yotsawat et al. 2021) | accuracy | 79.50% | — | — | Table 7, p. 32 |
| German dataset, XGB-BO (Yotsawat et al. 2021) | AUC | 80.50% | — | — | Table 7, p. 32 |
| German dataset, Proposed (Guo et al. 2019) | accuracy | 78.30% | — | — | Table 7, p. 32 |
| German dataset, Proposed (Guo et al. 2019) | AUC | 80.60% | — | — | Table 7, p. 32 |
| German dataset, HS-RF (Goh et al. 2020) | accuracy | 76.40% | — | — | Table 7, p. 32 |
| German dataset, HS-RF (Goh et al. 2020) | AUC | 80.44% | — | — | Table 7, p. 32 |
| German dataset, CS-NNE (Yotsawat et al. 2021) | accuracy | 74.40% | — | — | Table 7, p. 32 |
| German dataset, CS-NNE (Yotsawat et al. 2021) | AUC | 80.11% | — | — | Table 7, p. 32 |
| German dataset, mg-mGBDT (Liu et al. 2021) | accuracy | 76.53% | — | — | Table 7, p. 32 |
| German dataset, mg-mGBDT (Liu et al. 2021) | AUC | 78.46% | — | — | Table 7, p. 32 |
| German dataset, GSCI (Chen et al. 2020) | accuracy | 77.75% | — | — | Table 7, p. 32 |
| German dataset, GSCI (Chen et al. 2020) | AUC | 70.42% | — | — | Table 7, p. 32 |
| Australian dataset, Multi-stage ensemble (Zhang et al. 2021) | accuracy | 92.36% | — | — | Table 8, p. 32 |
| Australian dataset, Multi-stage ensemble (Zhang et al. 2021) | AUC | 96.65% | — | — | Table 8, p. 32 |
| Australian dataset, GA + NN (Kazemi et al. 2023) | accuracy | 91.91% | — | — | Table 8, p. 32 |
| Australian dataset, GA + NN (Kazemi et al. 2023) | AUC | 92.60% | — | — | Table 8, p. 32 |
| Australian dataset, Proposed (Zhang et al. 2021) | accuracy | 90.58% | — | — | Table 8, p. 32 |
| Australian dataset, Proposed (Zhang et al. 2021) | AUC | 94.83% | — | — | Table 8, p. 32 |
| Australian dataset, Proposed (Shen et al. 2019) | accuracy | 90.58% | — | — | Table 8, p. 32 |
| Australian dataset, Proposed (Shen et al. 2019) | AUC | 91.03% | — | — | Table 8, p. 32 |
| Australian dataset, gcForest (Li et al. 2021) | accuracy | 88.55% | — | — | Table 8, p. 32 |
| Australian dataset, gcForest (Li et al. 2021) | AUC | 94.25% | — | — | Table 8, p. 32 |
| Australian dataset, XGB-BO (Yotsawat et al. 2021) | accuracy | 88.70% | — | — | Table 8, p. 32 |
| Australian dataset, XGB-BO (Yotsawat et al. 2021) | AUC | 93.25% | — | — | Table 8, p. 32 |
| Australian dataset, mg-mGBDT (Liu et al. 2021) | accuracy | 88.26% | — | — | Table 8, p. 32 |
| Australian dataset, mg-mGBDT (Liu et al. 2021) | AUC | 94.07% | — | — | Table 8, p. 32 |
| Australian dataset, Proposed (Guo et al. 2019) | accuracy | 87.40% | — | — | Table 8, p. 32 |
| Australian dataset, Proposed (Guo et al. 2019) | AUC | 94.00% | — | — | Table 8, p. 32 |
| Australian dataset, SVM-RF (Yao and Chen 2019) | accuracy | 87.94% | — | — | Table 8, p. 32 |
| Australian dataset, SVM-RF (Yao and Chen 2019) | AUC | 92.10% | — | — | Table 8, p. 32 |
| Australian dataset, HS-RF (Goh et al. 2020) | accuracy | 87.38% | — | — | Table 8, p. 32 |
| Australian dataset, HS-RF (Goh et al. 2020) | AUC | 86.14% | — | — | Table 8, p. 32 |
| Australian dataset, AugBoost-ELM (Zou and Gao 2022) | accuracy | 84.39% | — | — | Table 8, p. 32 |
| Australian dataset, AugBoost-ELM (Zou and Gao 2022) | AUC | 94.22% | — | — | Table 8, p. 32 |
| Australian dataset, GSCI (Chen et al. 2020) | accuracy | 91.16% | — | — | Table 8, p. 32 |
| Australian dataset, GSCI (Chen et al. 2020) | AUC | 91.43% | — | — | Table 8, p. 32 |
| Australian dataset, CS-NNE (Yotsawat et al. 2021) | accuracy | 84.93% | — | — | Table 8, p. 32 |
| Australian dataset, CS-NNE (Yotsawat et al. 2021) | AUC | 91.31% | — | — | Table 8, p. 32 |
| Japanese dataset, Multi-stage ensemble (Zhang et al. 2021) | accuracy | 93.16% | — | — | Table 9, p. 33 |
| Japanese dataset, Multi-stage ensemble (Zhang et al. 2021) | AUC | 96.95% | — | — | Table 9, p. 33 |
| Japanese dataset, gcForest (Li et al. 2021) | accuracy | 88.99% | — | — | Table 9, p. 33 |
| Japanese dataset, gcForest (Li et al. 2021) | AUC | 96.02% | — | — | Table 9, p. 33 |
| Japanese dataset, Proposed (Zhang et al. 2021) | accuracy | 89.85% | — | — | Table 9, p. 33 |
| Japanese dataset, Proposed (Zhang et al. 2021) | AUC | 95.30% | — | — | Table 9, p. 33 |
| Japanese dataset, Proposed (Guo et al. 2019) | accuracy | 87.00% | — | — | Table 9, p. 33 |
| Japanese dataset, Proposed (Guo et al. 2019) | AUC | 94.20% | — | — | Table 9, p. 33 |
| Japanese dataset, AugBoost-ELM (Zou and Gao 2022) | accuracy | 86.87% | — | — | Table 9, p. 33 |
| Japanese dataset, AugBoost-ELM (Zou and Gao 2022) | AUC | 93.99% | — | — | Table 9, p. 33 |
| Japanese dataset, mg-mGBDT (Liu et al. 2021) | accuracy | 86.90% | — | — | Table 9, p. 33 |
| Japanese dataset, mg-mGBDT (Liu et al. 2021) | AUC | 93.11% | — | — | Table 9, p. 33 |
| Japanese dataset, GSCI (Chen et al. 2020) | accuracy | 89.13% | — | — | Table 9, p. 33 |
| Japanese dataset, GSCI (Chen et al. 2020) | AUC | 89.48 | — | — | Table 9, p. 33 |
| Lending Club dataset, GSCI (Chen et al. 2020) | accuracy | 91.70% | — | — | Table 10, p. 33 |
| Lending Club dataset, GSCI (Chen et al. 2020) | AUC | 93.78% | — | — | Table 10, p. 33 |
| Lending Club dataset, HS-RF (Goh et al. 2020) | accuracy | 85.71% | — | — | Table 10, p. 33 |
| Lending Club dataset, HS-RF (Goh et al. 2020) | AUC | 85.71% | — | — | Table 10, p. 33 |
| Lending Club dataset, LR (Ariza-Garzón et al. 2020) | accuracy | 78.10% | — | — | Table 10, p. 33 |
| Lending Club dataset, LR (Ariza-Garzón et al. 2020) | AUC | 66.60% | — | — | Table 10, p. 33 |
| Lending Club dataset, mg-mGBDT (Liu et al. 2021) | accuracy | 67.86% | — | — | Table 10, p. 33 |
| Lending Club dataset, mg-mGBDT (Liu et al. 2021) | AUC | 73.74% | — | — | Table 10, p. 33 |
| Lending Club dataset, XGB-BO (Yotsawat et al. 2021) | accuracy | 67.86% | — | — | Table 10, p. 33 |
| Lending Club dataset, XGB-BO (Yotsawat et al. 2021) | AUC | 72.48% | — | — | Table 10, p. 33 |
| Lending Club dataset, RF-RUS (Moscato 2021) | accuracy | 64.00% | — | — | Table 10, p. 33 |
| Lending Club dataset, RF-RUS (Moscato 2021) | AUC | 71.70% | — | — | Table 10, p. 33 |
| Lending Club dataset, CS-NNE (Yotsawat et al. 2021) | accuracy | 63.61% | — | — | Table 10, p. 33 |
| Lending Club dataset, CS-NNE (Yotsawat et al. 2021) | AUC | 70.82% | — | — | Table 10, p. 33 |
| Most cited document, Dumitrescu et al. (2022) | cites | 410 | — | — | Table 11, p. 36 |
| Most cited document, He et al. (2018) | cites | 313 | — | — | Table 11, p. 36 |
| Most cited document, Moscato (2021) | cites | 284 | — | — | Table 11, p. 36 |
| Most cited document, Shen et al. (2021) | cites | 225 | — | — | Table 11, p. 36 |
| Most cited document, Bao et al. (2019) | cites | 222 | — | — | Table 11, p. 36 |
| Cao et al. (2021) LR model accuracy with optimal threshold 0.18 | accuracy | 86.58% | — | — | Sect. 4.1.1, p. 9 |
| Dumitrescu et al. (2022) PLTR AUC on Australian dataset | AUC | 92.99% | — | — | Sect. 4.1.1, p. 9 |
| Dumitrescu et al. (2022) PLTR AUC on Taiwan dataset | AUC | 77.80% | — | — | Sect. 4.1.1, p. 9 |
| Dumitrescu et al. (2022) PLTR AUC on Housing dataset | AUC | 90.11% | — | — | Sect. 4.1.1, p. 9 |
| Ariza-Garzón et al. (2020) LR accuracy on Lending Club | accuracy | 78.10% | — | — | Sect. 4.1.1, p. 9 |
| Ariza-Garzón et al. (2020) LR AUC on Lending Club | AUC | 66.60% | — | — | Sect. 4.1.1, p. 9 |
| Syed Nor et al. (2019) DT bankruptcy model accuracy | accuracy | 83.29% | — | — | Sect. 4.1.2, p. 10 |
| Khedr et al. (2021) DT classifier accuracy | accuracy | 94.85% | — | — | Sect. 4.1.2, p. 10 |
| Khedr et al. (2021) DT classifier F1-score | F1-score | 96.75% | — | — | Sect. 4.1.2, p. 10 |
| Maharjan (2022) C4.5 F1-score on German dataset | F1-score | 85.23% | — | — | Sect. 4.1.2, p. 10 |
| Maharjan (2022) C4.5 accuracy on German dataset | accuracy | 78.33% | — | — | Sect. 4.1.2, p. 10 |
| Trivedi (2020) RF + chi-Square accuracy on German dataset | accuracy | 93.12% | — | — | Sect. 4.1.3, p. 10 |
| Trivedi (2020) RF + chi-Square F1-score on German dataset | F1-score | 93.10% | — | — | Sect. 4.1.3, p. 10 |
| Li et al. (2021) gcForest accuracy on German dataset | accuracy | 81.20% | — | — | Sect. 4.1.3, p. 10 |
| Li et al. (2021) gcForest AUC on German dataset | AUC | 86.80% | — | — | Sect. 4.1.3, p. 10 |
| Moscato (2021) RF-RUS accuracy on Lending Club | accuracy | 64.00% | — | — | Sect. 4.1.3, p. 11 |
| Moscato (2021) RF-RUS recall on Lending Club | recall | 63.00% | — | — | Sect. 4.1.3, p. 11 |
| Moscato (2021) RF-RUS AUC on Lending Club | AUC | 71.70% | — | — | Sect. 4.1.3, p. 11 |
| Aji and Dhini (2019) RF with AdaBoost accuracy | accuracy | 72.95% | — | — | Sect. 4.1.3, p. 11 |
| Aji and Dhini (2019) RF with AdaBoost recall | recall | 73.00% | — | — | Sect. 4.1.3, p. 11 |
| Aji and Dhini (2019) RF with AdaBoost specificity | specificity | 70.40% | — | — | Sect. 4.1.3, p. 11 |
| Tran et al. (2021) RF F1-score on Kalapa dataset | F1-score | 83.00% | — | — | Sect. 4.1.3, p. 11 |
| Tran et al. (2021) RF AUC on Kalapa dataset | AUC | 81.00% | — | — | Sect. 4.1.3, p. 11 |
| Parvin and Saleena (2020) RF accuracy on Australian dataset | accuracy | 88.41% | — | — | Sect. 4.1.3, p. 11 |
| Parvin and Saleena (2020) RF recall on Australian dataset | recall | 80.00% | — | — | Sect. 4.1.3, p. 11 |
| Parvin and Saleena (2020) RF precision on Australian dataset | precision | 87.00% | — | — | Sect. 4.1.3, p. 11 |
| Parvin and Saleena (2020) RF F1-score on Australian dataset | F1-score | 84.00% | — | — | Sect. 4.1.3, p. 11 |
| Zhang et al. (2018) NCSM accuracy on Australian dataset | accuracy | 91.71% | — | — | Sect. 4.1.3, p. 11 |
| Zhang et al. (2018) NCSM accuracy on German dataset | accuracy | 82.14% | — | — | Sect. 4.1.3, p. 11 |
| Teles et al. (2021) SVM accuracy on bank institution dataset | accuracy | 98.34% | — | — | Sect. 4.1.4, p. 11 |
| Teles et al. (2021) RF accuracy on bank institution dataset | accuracy | 98.20% | — | — | Sect. 4.1.4, p. 11 |
| Dm and Mm (2018) LR accuracy on training data | accuracy | 77.27% | — | — | Sect. 4.1.4, p. 12 |
| Dm and Mm (2018) LR accuracy on test data | accuracy | 73.33% | — | — | Sect. 4.1.4, p. 12 |
| Dm and Mm (2018) SVM accuracy on training data | accuracy | 88.29% | — | — | Sect. 4.1.4, p. 12 |
| Dm and Mm (2018) SVM accuracy on test data | accuracy | 86.12% | — | — | Sect. 4.1.4, p. 12 |
| Wang and Li (2019) IFOA-SVM precision | precision | 93% | — | — | Sect. 4.1.4, p. 12 |
| Mukid et al. (2018) WKNN gaussian kernel accuracy | accuracy | 82.40% | — | — | Sect. 4.1.5, p. 12 |
| Mukid et al. (2018) WKNN gaussian kernel sensitivity | sensitivity | 99.34% | — | — | Sect. 4.1.5, p. 12 |
| Mukid et al. (2018) WKNN gaussian kernel specificity | specificity | 11.11% | — | — | Sect. 4.1.5, p. 12 |
| Loo et al. (2023) KNN accuracy | accuracy | 89% | — | — | Sect. 4.1.5, p. 12 |
| Pratiwi et al. (2019) k-NN error with k = 1 | error | 1.89% | — | — | Sect. 4.1.5, p. 12 |
| Pratiwi et al. (2019) PNN error with k = 13 | error | 20.75% | — | — | Sect. 4.1.5, p. 12 |
| Goh et al. (2020) MHS-RF accuracy on Australian dataset | accuracy | 87.38% | — | — | Sect. 4.1.6, p. 13 |
| Nalic et al. (2020) hybrid model accuracy on Bosnia dataset | accuracy | 87.69% | — | — | Sect. 4.1.6, p. 13 |
| Nalic et al. (2020) hybrid model F1-score on Bosnia dataset | F1-score | 87.69% | — | — | Sect. 4.1.6, p. 13 |
| Yao and Chen (2019) RF-SVM accuracy on Australian dataset | accuracy | 87.94% | — | — | Sect. 4.1.6, p. 13 |
| Yao and Chen (2019) RF-SVM recall on Australian dataset | recall | 83.85% | — | — | Sect. 4.1.6, p. 13 |
| Yao and Chen (2019) RF-SVM AUC on Australian dataset | AUC | 92.10% | — | — | Sect. 4.1.6, p. 13 |
| Tripathi et al. (2019) hybrid model accuracy on Australian dataset | accuracy | 92.69% | — | — | Sect. 4.1.6, p. 13 |
| Tripathi et al. (2019) hybrid model recall on Australian dataset | recall | 97.16% | — | — | Sect. 4.1.6, p. 13 |
| Tripathi et al. (2019) hybrid model specificity on Australian dataset | specificity | 88.46% | — | — | Sect. 4.1.6, p. 13 |
| Yuan et al. (2022) two-stage model AUC | AUC | 86.33% | — | — | Sect. 4.1.6, p. 14 |
| Yuan et al. (2022) two-stage model G-mean | G-mean | 86.12% | — | — | Sect. 4.1.6, p. 14 |
| Boughaci et al. (2021) k-means + RF recall on Taiwan dataset | recall | 100% | — | — | Sect. 4.1.6, p. 14 |
| Boughaci et al. (2021) k-means + RF precision on Taiwan dataset | precision | 100% | — | — | Sect. 4.1.6, p. 14 |
| Boughaci et al. (2021) k-means + RF F1-score on Taiwan dataset | F1-score | 100% | — | — | Sect. 4.1.6, p. 14 |
| Suleiman et al. (2021) SOM + KNN accuracy | accuracy | 96.30% | — | — | Sect. 4.1.6, p. 14 |
| Suleiman et al. (2021) SOM + neural networks accuracy | accuracy | 97.30% | — | — | Sect. 4.1.6, p. 14 |
| Bao et al. (2019) unsupervised + supervised accuracy on Chinese P2P dataset | accuracy | 92.00% | — | — | Sect. 4.1.6, p. 14 |
| Ibrahim and Olagunju (2022) SOM + CART accuracy | accuracy | 96.70% | — | — | Sect. 4.1.6, p. 14 |
| Kazemi et al. (2023) GA + NN accuracy on Australian dataset | accuracy | 91.91% | — | — | Sect. 4.2.1, p. 15 |
| Kazemi et al. (2023) GA + NN AUC on Australian dataset | AUC | 92.60% | — | — | Sect. 4.2.1, p. 15 |
| Kazemi et al. (2021) GA + NN improvement on Australian dataset | accuracy improvement | 2.68% | — | — | Sect. 4.2.1, p. 15 |
| Kazemi et al. (2021) GA + NN improvement on German dataset | accuracy improvement | 0.1% | — | — | Sect. 4.2.1, p. 15 |
| Diaconescu and Neagoe (2020) DL neural network accuracy on German dataset | accuracy | 84.83% | — | — | Sect. 4.2.1, p. 15 |
| Dastile and Celik (2021) 2D CNN accuracy on Australian dataset | accuracy | 95.00% | — | — | Sect. 4.2.2, p. 15 |
| Zhu et al. (2018) CNN + relief accuracy | accuracy | 91.64% | — | — | Sect. 4.2.2, p. 15 |
| Zhu et al. (2018) CNN + relief AUC | AUC | 96.89% | — | — | Sect. 4.2.2, p. 15 |
| Zhu et al. (2018) CNN + relief KS | KS | 91.64% | — | — | Sect. 4.2.2, p. 15 |
| Neagoe et al. (2018) DCNN accuracy on German dataset | accuracy | 90.85% | — | — | Sect. 4.2.2, p. 15 |
| Neagoe et al. (2018) MLP accuracy on German dataset | accuracy | 81.20% | — | — | Sect. 4.2.2, p. 15 |
| Neagoe et al. (2018) DCNN accuracy on Australian dataset | accuracy | 99.74% | — | — | Sect. 4.2.2, p. 15 |
| Neagoe et al. (2018) MLP accuracy on Australian dataset | accuracy | 90.75% | — | — | Sect. 4.2.2, p. 15 |
| Ala'raj et al. (2021) bidirectional LSTM accuracy | accuracy | 82.40% | — | — | Sect. 4.2.3, p. 16 |
| Ala'raj et al. (2021) bidirectional LSTM specificity | specificity | 95.15% | — | — | Sect. 4.2.3, p. 16 |
| Ala'raj et al. (2021) bidirectional LSTM AUC | AUC | 78.47% | — | — | Sect. 4.2.3, p. 16 |
| Wang et al. (2018) AM-LSTM AUC on P2P dataset | AUC | 71.00% | — | — | Sect. 4.2.3, p. 16 |
| Wang et al. (2018) AM-LSTM KS on P2P dataset | KS | 31.00% | — | — | Sect. 4.2.3, p. 16 |
| Ala'raj et al. (2022) LSTM accuracy on transactional dataset | accuracy | 90.69% | — | — | Sect. 4.2.3, p. 16 |
| Ala'raj et al. (2022) LSTM recall on transactional dataset | recall | 72.87% | — | — | Sect. 4.2.3, p. 16 |
| Ala'raj et al. (2022) LSTM KS on transactional dataset | KS | 82.94% | — | — | Sect. 4.2.3, p. 16 |
| Ala'raj et al. (2022) LSTM AUC on transactional dataset | AUC | 91.00% | — | — | Sect. 4.2.3, p. 16 |
| Adisa et al. (2022) optimized LSTM accuracy on Australian dataset | accuracy | 89.27% | — | — | Sect. 4.2.3, p. 16 |
| Pławiak et al. (2020) DGHNL accuracy on Australian dataset | accuracy | 97.39% | — | — | Sect. 4.2.4, p. 17 |
| Pławiak et al. (2020) DGHNL accuracy on German dataset | accuracy | 94.60% | — | — | Sect. 4.2.4, p. 17 |
| Shen et al. (2021) DL ensemble AUC on German dataset | AUC | 80.32% | — | — | Sect. 4.2.4, p. 17 |
| Shen et al. (2021) DL ensemble KS on German dataset | KS | 39.48% | — | — | Sect. 4.2.4, p. 17 |
| Liu et al. (2021) mg-mGBDT accuracy on Australian dataset | accuracy | 88.26% | — | — | Sect. 4.3.1, p. 17 |
| Liu et al. (2021) mg-mGBDT AUC on Australian dataset | AUC | 94.07% | — | — | Sect. 4.3.1, p. 17 |
| Zou and Gao (2022) AugBoost-ELM accuracy on Japanese dataset | accuracy | 86.87% | — | — | Sect. 4.3.1, p. 18 |
| Zou and Gao (2022) AugBoost-ELM F1-score on Japanese dataset | F1-score | 87.91% | — | — | Sect. 4.3.1, p. 18 |
| Bai et al. (2022) GBST AUC on 360 Finance dataset | AUC | 82.51% | — | — | Sect. 4.3.1, p. 18 |
| Bai et al. (2022) GBST KS on 360 Finance dataset | KS | 51.64% | — | — | Sect. 4.3.1, p. 18 |
| Zhang et al. (2020) OICSM AUC on Lending Club | AUC | 73.39% | — | — | Sect. 4.3.1, p. 18 |
| Zhang et al. (2020) OICSM AUC on Paipaidai | AUC | 71.76% | — | — | Sect. 4.3.1, p. 18 |
| Ampountolas et al. (2021) XGBoost recall on micro-loans dataset | recall | 88.00% | — | — | Sect. 4.3.2, p. 18 |
| Ampountolas et al. (2021) XGBoost specificity on micro-loans dataset | specificity | 71.00% | — | — | Sect. 4.3.2, p. 18 |
| Ampountolas et al. (2021) XGBoost F1-score on micro-loans dataset | F1-score | 78.00% | — | — | Sect. 4.3.2, p. 18 |
| Xia et al. (2021) SurvXGBoost AUC | AUC | 68.08% | — | — | Sect. 4.3.2, p. 18 |
| Xia et al. (2021) SurvXGBoost out-of-sample AUC | AUC | 68.07% | — | — | Sect. 4.3.2, p. 18 |
| Xia et al. (2021) SurvXGBoost out-of-time AUC | AUC | 67.07% | — | — | Sect. 4.3.2, p. 19 |
| Xia et al. (2021) SurvXGBoost misclassification cost | misclassification cost | 64.84% | — | — | Sect. 4.3.2, p. 19 |
| Yotsawat et al. (2021) XGBoost-BO improvement on German dataset | accuracy improvement | 4.10% | — | — | Sect. 4.3.2, p. 19 |
| Yotsawat et al. (2021) XGBoost-BO improvement on Lending Club | accuracy improvement | 3.03% | — | — | Sect. 4.3.2, p. 19 |
| Yotsawat et al. (2021) XGBoost-BO improvement on Australian dataset | accuracy improvement | 2.76% | — | — | Sect. 4.3.2, p. 19 |
| He et al. (2018) ensemble F1-score on Japanese dataset | F1-score | 88.04% | — | — | Sect. 4.3.3, p. 19 |
| He et al. (2018) ensemble AUC on Japanese dataset | AUC | 92.79% | — | — | Sect. 4.3.3, p. 19 |
| He et al. (2018) ensemble G-mean on Japanese dataset | G-mean | 86.22% | — | — | Sect. 4.3.3, p. 19 |
| He et al. (2018) ensemble KS on Japanese dataset | KS | 75.80% | — | — | Sect. 4.3.3, p. 19 |
| Rofik et al. (2024) stacking ensemble accuracy on German dataset | accuracy | 83.21% | — | — | Sect. 4.3.3, p. 19 |
| Rofik et al. (2024) stacking ensemble precision on German dataset | precision | 79.29% | — | — | Sect. 4.3.3, p. 19 |
| Rofik et al. (2024) stacking ensemble recall on German dataset | recall | 91.78% | — | — | Sect. 4.3.3, p. 19 |
| Rofik et al. (2024) stacking ensemble F1-score on German dataset | F1-score | 85.08% | — | — | Sect. 4.3.3, p. 19 |
| Zhang et al. (2021) multi-stage ensemble accuracy on Japanese dataset | accuracy | 93.16% | — | — | Sect. 4.3.3, p. 19 |
| Zhang et al. (2021) multi-stage ensemble F1-score on Japanese dataset | F1-score | 93.45% | — | — | Sect. 4.3.3, p. 19 |
| Zhang et al. (2021) multi-stage ensemble AUC on Japanese dataset | AUC | 96.95% | — | — | Sect. 4.3.3, p. 19 |
| Jin et al. (2021) ensemble recall on Polish 2 dataset | recall | 93.79% | — | — | Sect. 4.3.3, p. 19 |
| Jin et al. (2021) ensemble F1-score on Polish 2 dataset | F1-score | 15.76% | — | — | Sect. 4.3.3, p. 19 |
| Yotsawat et al. (2021) CS-NNE accuracy on Polish dataset | accuracy | 91.30% | — | — | Sect. 4.3.3, p. 20 |
| Shen et al. (2019) ensemble accuracy on Australian dataset | accuracy | 90.58% | — | — | Sect. 4.3.3, p. 20 |
| Shen et al. (2019) ensemble F1-score on Australian dataset | F1-score | 95.40% | — | — | Sect. 4.3.3, p. 20 |
| Shen et al. (2019) ensemble AUC on Australian dataset | AUC | 91.03% | — | — | Sect. 4.3.3, p. 20 |
| Shen et al. (2019) ensemble G-mean on Australian dataset | G-mean | 90.94% | — | — | Sect. 4.3.3, p. 20 |
| Jiao et al. (2021) CNN-XGBoost accuracy on Australian dataset | accuracy | 88.20% | — | — | Sect. 4.3.3, p. 20 |
| Jiao et al. (2021) CNN-XGBoost F1-score on Australian dataset | F1-score | 87.43% | — | — | Sect. 4.3.3, p. 20 |
| Chen et al. (2020) GSCI recall on Australian dataset | recall | 94.53% | — | — | Sect. 4.3.3, p. 20 |
| Chen et al. (2020) GSCI F1-score on Australian dataset | F1-score | 90.91% | — | — | Sect. 4.3.3, p. 20 |
| Chen et al. (2020) GSCI AUC on Australian dataset | AUC | 91.43% | — | — | Sect. 4.3.3, p. 20 |
| Chen et al. (2020) GSCI accuracy on RRDai dataset | accuracy | 93.35% | — | — | Sect. 4.3.3, p. 20 |
| Zhang and Chi (2021) heterogeneous ensemble AUC on Chilean dataset | AUC | 70.50% | — | — | Sect. 4.3.3, p. 20 |
| Li et al. (2022) OCDDEL accuracy on Lending Club | accuracy | 89.38% | — | — | Sect. 4.3.3, p. 20 |
| Guo et al. (2019) self-adaptive ensemble accuracy on Australian dataset | accuracy | 87.40% | — | — | Sect. 4.3.3, p. 21 |
| Guo et al. (2019) self-adaptive ensemble F1-score on Australian dataset | F1-score | 86.80% | — | — | Sect. 4.3.3, p. 21 |
| Guo et al. (2019) self-adaptive ensemble AUC on Australian dataset | AUC | 94.00% | — | — | Sect. 4.3.3, p. 21 |
| Tripathi et al. (2018) weighted voting accuracy on Japanese dataset | accuracy | 87.98% | — | — | Sect. 4.3.3, p. 21 |
| Tripathi et al. (2018) weighted voting F1-score on Japanese dataset | F1-score | 90.69% | — | — | Sect. 4.3.3, p. 21 |
| Quality assessment minimum score for included studies | percentage | 77% | — | — | Sect. 3.5.2, p. 8 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "Over the past few decades, credit scoring has become an important tool in the financial sector." | Abstract, p. 1 | model_algorithm_integration |
| "A total of 330 research papers were extracted from four different online databases and digital libraries. After the study selection procedure, 63 research papers were selected for this systematic review." | Abstract, p. 1 | model_performance_evaluation |
| "Traditional models most commonly based on logistic regression or scorecards, are valued for their interpretability, transparency, and regulatory acceptance." | Sect. 1, p. 2 | rule_based_classification |
| "ML models can capture nonlinearities, handle high-dimensional data, and adapt to evolving borrower behavior." | Sect. 1, p. 2 | model_algorithm_integration |
| "Analysis of the reviewed studies indicates that hybrid ensemble models are the most widely used, reflecting their ability to combine multiple algorithms, leverage complementary strengths, improve predictive accuracy, and manage heterogeneous borrower profiles." | Sect. 7.1, p. 38 | model_algorithm_integration |
| "Accuracy remains the most commonly reported metric, reflecting its intuitive appeal. However, its reliability is limited in imbalanced datasets, which are common in credit scoring." | Sect. 7.3, p. 40 | model_performance_evaluation |
| "Using alternative data in credit scoring is an emerging trend that enhances predictive accuracy by incorporating non-traditional data sources." | Sect. 7.4.1, p. 40 | model_algorithm_integration |
| "Interpretability and explainability are critical emerging trends and advancements in the development of ML models for credit scoring." | Sect. 7.4.2, p. 42 | model_performance_evaluation |
| "The curse of dimensionality presents significant challenges when applying ML to high-dimensional data." | Sect. 7.5.3, p. 44 | model_performance_evaluation |
| "DL techniques show promise with large datasets but face limitations related to interpretability and data availability." | Sect. 9, p. 48 | model_algorithm_integration |
| "Ensemble and hybrid models, which often combine feature optimization and multiple classifiers, consistently outperform traditional single models in terms of accuracy and discrimination power across popular credit scoring datasets." | Sect. 9, p. 48 | model_algorithm_integration |
| "This review is limited by the heterogeneity of datasets, evaluation metrics, and methodologies in the literature, which complicates direct performance comparisons." | Sect. 9, p. 48 | model_performance_evaluation |
| "Decision trees can be highly sensitive to the training data, which leads to overfitting or instability when the dataset changes slightly." | Sect. 4.1.2, p. 9 | rule_based_classification |
| "A key advantage of DTs is their interpretability, as they provide clear, understandable decision rules." | Sect. 4.1.2, p. 9 | rule_based_classification |
| "The most frequently used public datasets were German, Australian, and Japanese credit datasets, while about one-third of studies relied on proprietary institutional datasets." | Sect. 6.2, p. 23 | model_performance_evaluation |
| "Hybrid models demand substantial computational resources due to the integration of multiple algorithms. Such resource intensity may hinder the scalability, practicality, and interpretability of hybrid techniques." | Sect. 7.2.2, p. 39 | model_algorithm_integration |
| "The diversity of metrics reported across studies indicates both the complexity of credit scoring tasks and the absence of standardized evaluation protocols, making direct comparisons across models challenging." | Sect. 7.3, p. 40 | model_performance_evaluation |
| "Biases in training datasets can lead ML models to exhibit unfairness based on several criteria. In credit scoring, for example, these criteria may include age, gender, race, caste, and religion." | Sect. 7.5.2, p. 44 | model_performance_evaluation |
| "The need to develop and implement effective techniques for model interpretability remains a pressing concern in the field of credit scoring." | Sect. 7.5.1, p. 44 | model_performance_evaluation |
| "Future research should focus on establishing standardized benchmarking protocols to enable fair and consistent evaluation of credit scoring models." | Sect. 9, p. 48 | model_performance_evaluation |

## Remember This

- This is a systematic literature review of 63 studies (2018–2024) on ML for credit scoring, following PRISMA 2020 guidelines.
- Hybrid ensemble models are reported as the most widely used and effective approaches, consistently outperforming single classifiers.
- The review catalogs 28 evaluation metrics, with accuracy (49 uses) and AUC (31 uses) being the most frequently reported.
- Benchmark datasets analysed include German, Australian, Japanese, and Lending Club, with ranked accuracy and AUC comparisons in Tables 7–10.
- Emerging trends include alternative data (social media, mobile phone usage, psychometrics) and explainability methods (LIME, SHAP).
- Key challenges are interpretability, potential biases, the curse of dimensionality, and integration of behavioral/attitudinal data.
- The paper contains an internal inconsistency: the abstract reports 330 extracted papers while Sect. 6.1 reports 345 identified studies.

## Cited Works

- Dastile, X.; Celik, T.; Potsane, M. (2020) (context) — Systematic literature survey of statistical and ML models in credit scoring from 2010–2018, finding ensemble methods outperform single classifiers. [p. 3]
- Kumar, A.; Sharma, S.; Mahdavi, M. (2021) (context) — Literature review on ML technologies for digital credit scoring in rural finance, emphasizing fintech and AI for underserved populations. [p. 3]
- Hayashi, Y. (2022) (context) — Systematic review of DL in credit scoring (2019–2022), highlighting Deep Belief Networks and CNN performance. [p. 4]
- Lenka, S.R.; Bisoy, S.K.; Priyadarshini, R.; Sain, M. (2022) (context) — Empirical analysis of ensemble learning for imbalanced credit scoring datasets, recommending CatBoost with GA-based feature selection. [p. 4]
- Markov, A.; Seleznyova, Z.; Lapshin, V. (2022) (context) — Review of credit scoring methods from 2016–2021, noting shift from traditional models to ensemble and neural network approaches. [p. 4]
- Kamimura, E.S.; Pinto, A.R.F.; Nagano, M.S. (2023) (context) — Review of optimization methods for credit scoring models (2008–2022), finding growing trend toward hybrid models. [p. 4]
- Dumitrescu, E.; Hué, S.; Hurlin, C.; Tokpavi, S. (2022) (methodology) — Introduced Penalized Logistic Tree Regression (PLTR) combining DT rules with LR for interpretable credit scoring. [p. 36]
- He, H.; Zhang, W.; Zhang, S. (2018) (methodology) — Proposed ensemble model adapting to different class imbalance ratios using BalanceCascade, RF, XGBoost, stacking, and PSO. [p. 36]
- Moscato, V. (2021) (methodology) — Benchmarked ML approaches for credit score prediction in P2P lending, assessing predictive performance and interpretability. [p. 36]
- Shen, F.; Zhao, X.; Kou, G.; Alsaadi, F.E. (2021) (methodology) — Combined improved SMOTE with LSTM and AdaBoost in a DL ensemble framework for imbalanced credit data. [p. 36]
- Bao, W.; Ning, L.; Yue, K. (2019) (methodology) — Integrated unsupervised learning at consensus and clustering stages with supervised models for credit risk assessment. [p. 36]
- Bhandary, R.; Ghosh, B.K. (2025) (context) — Empirical comparison of traditional and modern ML techniques for credit card default prediction using real-world data. [p. 47]
- Bhandary, R.; Shenoy, S.S.; Shetty, A.; Shetty, A.D. (2023) (context) — Qualitative study on educational loan repayment attitudes among college students in India. [p. 45]
- Bussmann, N.; Giudici, P.; Marinelli, D.; Papenbrock, J. (2021) (methodology) — Explainable ML in credit risk management using correlation networks and Shapley values. [p. 43]
- Bücker, M.; Szepannek, G.; Gosiewska, A.; Biecek, P. (2022) (methodology) — Framework for transparency, auditability, and explainability of ML models in credit scoring using LIME and SHAP. [p. 43]
- Ayari, H.; Guetari, R. (2025) (methodology) — Integrating genetic algorithms and ensemble learning for improved and transparent credit scoring using SHAP. [p. 43]
- De Cnudde, S.; Moeyersoms, J.; Stankova, M.; Tobback, E.; Javaly, V.; Martens, D. (2019) (methodology) — Enhanced credit scoring with Facebook data for microfinance, finding BFF relationships have stronger predictive value. [p. 41]
- Niu, B.; Ren, J.; Li, X. (2019) (methodology) — Credit scoring using mobile phone-derived social network data for loan default prediction. [p. 41]
- Djeundje, V.B.; Crook, J.; Calabrese, R.; Hamid, M. (2021) (methodology) — Enhancing credit scoring with alternative data including email and psychometric variables. [p. 42]
- Ribeiro, M.T.; Singh, S.; Guestrin, C. (2019) (methodology) — LIME method for explaining predictions of any classifier. [p. 3]
- Lundberg, S.M.; Lee, S.-I. (2017) (methodology) — SHAP unified approach to interpreting model predictions. [p. 3]
- Page, M.J.; McKenzie, J.E.; Bossuyt, P.M.; et al. (2021) (methodology) — PRISMA 2020 statement for reporting systematic reviews. [p. 5]
- Van Eck, N.; Waltman, L. (2010) (methodology) — VOSviewer software for bibliometric mapping. [p. 28]
- Chawla, N.V.; Bowyer, K.W.; Hall, L.O.; Kegelmeyer, W.P. (2002) (methodology) — SMOTE synthetic minority over-sampling technique. [p. 3]
- ElKelish, W.W. (2021) (context) — IFRS 9 financial instruments, information quality, and stock returns. [p. 2]
- Bhatore, S.; Mohan, L.; Reddy, Y.R. (2020) (context) — Systematic literature review of ML techniques for credit risk evaluation. [p. 2]
```