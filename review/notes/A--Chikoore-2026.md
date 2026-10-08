---
paper_id: A--Chikoore-2026
first_author: Chikoore
year: 2026
title: "Adaptive Credit Scoring Model With Concept Drift Detection and Adaptation Technique for a Dynamic Environment"
venue: "IEEE Access"
doi: 10.1109/ACCESS.2026.3703181
designation: algorithm
status: extracted
modules: [model_algorithm_integration, model_performance_evaluation, model_development, savings_debt_management]
module_rationale:
  model_algorithm_integration: "Adaptive Fusion dynamically weights and fuses three Random Forest models (m0, mretain, mwindow) as pfinal = w0p0 + wrpr + wwpw, and a soft-voting ensemble combines CART/NB/RF/XGBoost (Sec. IV, p. 90370; Eq. 5)."
  model_performance_evaluation: "Sec. V reports accuracy, precision, recall, F1 and ROC-AUC for the vanilla and adaptive models (Table 1 and Figs. 3-7, pp. 90370-90372)."
  model_development: "Sec. IV describes training the vanilla models, retraining on drifted data, and windowed learning with a sliding window of size W = 100 (Algorithm 1, pp. 90370-90371)."
  savings_debt_management: "The paper's dependent construct is loan repayment: 'it tells a lender or investor the probability of the subject being able to pay back a loan' (Sec. I, p. 90365)."
---

# A--Chikoore-2026

## Summary

Chikoore, Ojo and Kogeda propose **Adaptive Fusion**, an adaptive credit-scoring framework intended to detect and adapt to concept drift in dynamic lending environments. The framework begins from four vanilla classifiers — CART, Naive Bayes, Random Forest and XGBoost — benchmarked on the German Credit benchmark dataset. To create drift, the authors modify that dataset by simulation in three ways: increasing every age instance by five years (temporal/population shift), adding Gaussian noise N(0, 1000) to credit amounts, and changing the class distribution so that the defaulted class falls from 30% to 20%. Four adaptation strategies are then compared: model retraining, windowed learning (sliding window of size W = 100), a soft-voting ensemble, and Adaptive Fusion. Adaptive Fusion maintains three Random Forest models — m0 (pre-drift), mretrain (retrained on drifted data) and mwindow (trained on a sliding window) — and fuses their class probabilities with dynamically updated weights. The abstract reports that the Retrained Random Forest, Ensemble and Adaptive Fusion models each attain 95.0% accuracy, 0.9275 precision, 0.9645 recall, 0.9426 F1-score and ROC-AUC above 0.96, and that this exceeds the state-of-the-art DGHNL (94.60% accuracy, AUC 0.9360). The paper is motivated by credit scoring in developing economies, but all evaluation is on the German Credit benchmark with synthetically injected drift.

## Problem and Motivation

The paper argues that static credit-scoring models degrade over time because borrower behaviour, economic conditions and data distributions change, producing concept drift, population drift and label drift. These dynamics "reduce model accuracy and reliability, increase misclassification rates, and expose financial institutions to substantial financial and regulatory risks" (Abstract, p. 90365). The authors state that traditional systems are "one-shot, fixed-memory-based, and trained from fixed training datasets and static models" and therefore "cannot manage and process highly evolving financial data" (Sec. I, p. 90366). A change in the population changes the distribution of variables, which then changes model performance.

The paper also claims a contextual gap: "existing adaptive approaches are largely developed for advanced economies and are not well-suited to developing contexts" (Abstract, p. 90365). The stated aim is "to develop a two-stage credit scoring system that enables the management of the temporal degradation of credit scoring models in general" (Sec. I, p. 90366). The intended application domains include insurance policy approval and renewal, landlord tenant screening, and human-resource recruitment for financially sensitive roles. The authors position the work against drift-adaptation literature that they group into instance-based, model-based, feature-based, and meta-learning/self-adaptive families.

## Method

**Design.** Comparative experimental machine-learning study with simulation-injected concept drift and a benchmark comparison; the authors state no formal design label.
**Sample.** N not reported; the unit of analysis is a credit-applicant record in the German Credit benchmark dataset, replicated across three simulated drift variants.
**Context.** geography: Not reported (the paper evaluates on the German Credit benchmark dataset and is motivated by developing-economy credit scoring, but no country of data collection or deployment is stated); population: credit applicants in the German Credit benchmark dataset; setting: computational simulation on an 11th Gen Intel(R) Core (TM) i5-1135G7 at 2.40 GHz with 8.00 GB installed RAM.

The procedure runs as follows:

- Train four vanilla models — CART, Naive Bayes, Random Forest and XGBoost — on the original (pre-drift) German Credit dataset and evaluate them under static conditions. Random Forest is selected as the baseline because it performed best in this phase (Sec. IV, p. 90370).
- Inject drift in three simulated scenarios. Scenario 1 increases all age instances by five years: Xd = Xn + 5 (Eq. 1), representing a temporal shift in the population. Scenario 2 adds random Gaussian noise to the credit amount: New credit amount = Original Credit amount + N(0,1000), with mean 0 and standard deviation 1000 (Eqs. 2-3). Scenario 3 changes the class distribution, reducing the proportion of the defaulted class to 20% (from an original 70:30 good:bad split) using a class-weighting factor wi (Eq. 4).
- Apply four adaptation strategies. **Retraining** builds mretrain on detected drifted data. **Windowing** builds mwindow on a sliding window of size W = 100 over recently drifted samples. **Ensemble learning** combines the four classifiers by soft voting, taking the mode of their predictions. **Adaptive Fusion** keeps m0, mretrain and mwindow and fuses their class probabilities: pfinal = w0p0 + wrpr + wwpw, with w0 + wr + ww = 1 (Eq. 5).
- Evaluate all strategies across the three drift scenarios (drift1–drift3) using accuracy, precision, recall, F1-score and ROC-AUC.

The paper reports no train/test split proportions, no cross-validation scheme, no random seeds, and no hyperparameter settings for any of the four base classifiers. It reports the execution hardware but not the software library or version used to run the experiments.

## Software

Not reported. The paper names the four algorithms (CART, Naive Bayes, Random Forest, XGBoost) and the Adaptive Fusion strategy, and states the execution hardware (11th Gen Intel Core i5-1135G7 @ 2.40 GHz, 8.00 GB RAM), but it does not name any software framework, library, or version, and it does not report hyperparameter values or random seeds.

## Key Findings

- Adaptive Fusion delivered the strongest and most stable performance across all three drift scenarios, with the highest accuracy, precision, recall, F1-score and ROC-AUC and "minimal degradation as drift occurred" (Sec. V, p. 90371).
- The Ensemble approach was consistently second best, remaining close to Adaptive Fusion but with slightly larger drops, most notably in recall and consequently F1 (Sec. V, p. 90372).
- Batch retraining "yielded middling results: accuracy and precision were reasonable, yet recall and F1 lagged" (Sec. V, p. 90372).
- The sliding window method performed worst overall, with the largest deficits in recall and F1 score (Sec. V, p. 90372).
- In the vanilla (static) test, Random Forest was best: accuracy 0.77, precision 0.737, F1 score 0.680, ROC-AUC 0.768. XGBoost followed closely, "particularly excelling in the ROC-AUC (0.760)". CART and Naive Bayes were lower, with Naive Bayes slightly above CART in ROC-AUC (0.662 vs 0.602) (Sec. V, p. 90370).
- The abstract reports the Retrained Random Forest, Ensemble and Adaptive Fusion models each attaining accuracy 95.0%, precision 0.9275, recall 0.9645, F1-score 0.9426 and ROC-AUC above 0.96 (Abstract, p. 90365).
- Adaptive Fusion "matches the retrained model in all performance metrics, offering a scalable and efficient solution to concept drift" (Sec. VI, p. 90372).
- The proposed approach is compared favourably to the Deep Genetic Hierarchical Network of Learners (DGHNL), which the abstract cites at 94.60% accuracy and AUC 0.9360 (Abstract, p. 90365).
- The authors claim the Adaptive Fusion algorithm "would not introduce significant scalability constraints, as model updates are performed dynamically and can be integrated within existing data processing pipelines" (Sec. VI, p. 90373), a claim made without throughput or latency measurements.

## Key Figures and Tables

- Fig. 1 (p. 90369): Concept drift detection — generic scheme where a test statistic compares old and new samples against a threshold; the null hypothesis is no concept drift.
- Fig. 2 (p. 90370): Model adaptation architecture — m0, mretrain and mwindow feed a fusion layer that produces the final prediction.
- Fig. 3 (p. 90370): Vanilla model performance on original dataset — bar chart of CART, Naive Bayes, Random Forest and XGBoost under static conditions.
- Fig. 4 (p. 90371): ROC-AUC for adaptive retraining — tracks whether AUC drops as drift accumulates.
- Fig. 5 (p. 90371): Model evaluation on adaptive strategies — comparison of retraining, windowing, ensemble and Adaptive Fusion.
- Fig. 6 (p. 90372): ROC-AUC for adaptive windowing.
- Fig. 7 (p. 90372): ROC-AUC for ensemble adaptation and adaptive fusion.
- Table 1 (p. 90371): Vanilla model performance on original dataset — the paper's only numbered results table; the text supplies Random Forest's accuracy (0.77), precision (0.737), F1 (0.680) and ROC-AUC (0.768), plus XGBoost's ROC-AUC (0.760) and Naive Bayes/CART ROC-AUC (0.662/0.602).

## Limitations and Gaps

- The evaluation rests entirely on the **German Credit benchmark dataset** with synthetically injected drift. The authors acknowledge that future work "needs to include the use of a data stream that can be studied and analyzed to detect different kinds of concept drift the data may suffer" (Sec. VII, p. 90373).
- The paper claims developing-economy relevance in its abstract and framing but evaluates only on a German benchmark dataset; no developing-economy data is used. [unacknowledged]
- The abstract reports that the Retrained Random Forest, Ensemble **and** Adaptive Fusion models all attain identical metrics (95.0% accuracy, 0.9275 precision, 0.9645 recall, 0.9426 F1, ROC-AUC above 0.96), while the body states Adaptive Fusion "outperformed all the other strategies" and that the Ensemble "slightly trailed in the ROC-AUC" (Sec. V, p. 90372). The two accounts do not agree, and the paper does not reconcile them. [unacknowledged]
- The reported accuracy jumps from 0.77 for the vanilla Random Forest (Table 1, p. 90371) to 95.0% for the adaptive models (Abstract, p. 90365). The paper does not explain or reconcile this ~18-point gap, nor does it clarify the mixed use of 0–1 and percentage scales. [unacknowledged]
- No confidence intervals, p-values, significance tests, or variance estimates are reported for any of the paper's own comparisons. The only related-work statistical claim cited is that local logistic regression "consistently and statistically significantly" outperforms global counterparts in a cited study (Sec. II-A, p. 90367). [unacknowledged]
- The three drift scenarios (drift1–drift3) are not reported numerically per scenario. The results are described qualitatively and shown in ROC-AUC figures without printed values, so the comparison cannot be reconstructed from the text. [unacknowledged]
- The sample size N of the German Credit dataset is never stated. Only the original class proportion (70:30 good:bad) is given (Sec. III, p. 90370). [unacknowledged]
- Precision, recall and F1 are reported for Random Forest in the vanilla test but not for XGBoost, CART or Naive Bayes; only ROC-AUC is given for those three (Sec. V, p. 90370). [unacknowledged]
- The hardware is a consumer laptop (11th Gen Intel Core i5-1135G7, 8.00 GB RAM), which limits any inference about scalability to production credit-scoring volumes. [unacknowledged]
- The window size W = 100 is stated but never justified or sensitivity-tested. [unacknowledged]
- The claim that the algorithm "would not introduce significant scalability constraints" and is "not expected to pose substantial compliance challenges" (Sec. VI, p. 90373) is asserted without measurement or regulatory analysis. [unacknowledged]
- The authors acknowledge that continuously updating models "raises important considerations around stability, transparency and auditability, necessitating oversight approaches that can accommodate adaptive decision systems" (Sec. VII, p. 90373).
- The authors acknowledge the need for "stronger monitoring and governance frameworks" as adaptive credit scoring expands access to credit (Sec. VII, p. 90373).
- The paper reports no fairness metric despite claiming the model "accounts for fairness and bias" (Sec. VII, p. 90373); no protected-attribute analysis is performed. [unacknowledged]
- No ablation isolates the contribution of the three component models (m0, mretrain, mwindow) to the fused result, and the fusion weights w0, wr, ww are never reported. [unacknowledged]

## Definitions

- **Adaptive Fusion** — The paper's proposed strategy: maintaining m0, mretrain and mwindow, and fusing their class probabilities with dynamically adjusted weights (Eq. 5).
- **Concept drift** — Evolving patterns in data over time that degrade a model's learned relationships between input features and target variables.
- **Population drift** — A change in the distribution of variables within a population, one of the drift types the paper distinguishes.
- **Label drift** — Drift in the target variable distribution, named alongside concept and population drift in the abstract.
- **Vanilla model** — A base classifier (CART, Naive Bayes, Random Forest or XGBoost) trained under static, non-adaptive conditions.
- **Retraining** — Rebuilding a model on detected drifted data (mretrain).
- **Windowing** — Training on a sliding window of size W = 100 over recently drifted samples (mwindow).
- **Ensemble learning** — Soft voting across the four classifiers, taking the mode of their predictions.
- **DGHNL** — Deep Genetic Hierarchical Network of Learners, the state-of-the-art model the paper compares against (94.60% accuracy, AUC 0.9360).
- **ADHE** — Adaptive and Dynamic Heterogeneous Ensemble, a cited credit-scoring approach using data-stream learning (Sec. II-B).
- **AMUSE** — Adaptive Model Updating using a Simulated Environment, a reinforcement-learning-based model-update framework (Sec. II-B).
- **CDDF-HML** — Concept Drift Detection Framework with Hybrid Meta-Learning, a cited drift-detection framework (Sec. II-D).
- **KME** — Knowledge-Maximized Ensemble, a hybrid data-stream classifier cited in the discussion; reported at 85%–95% accuracy on synthetic datasets.
- **DriftLens** — A cited unsupervised real-time concept-drift detector for deep learning models (Sec. II-A).
- **CatSight** — A cited concept-drift detector for multivariate time series using Common Spatial Patterns (Sec. II-A).
- **German Credit dataset** — The benchmark dataset used for all experiments, originally a 70:30 good/bad split, modified by simulation to inject drift.

## Key Equations

- `Xd = Xn + 5` — Scenario 1 drift: each age instance increased by five years (Eq. 1, p. 90369).
- `f(x) = (1 / (σ√(2π))) · e^(−(x−µ)² / (2σ²))` — Gaussian density for the noise added to credit amounts (Eq. 2, p. 90370).
- `f(x) = (1 / (1000√(2π))) · e^(−x² / (2·1000²))` — The Scenario 2 noise density with σ = 1000 (Eq. 3, p. 90370).
- `P′(Ci) = (wi · P(Ci)) / (Σj wj · P(Cj))` — Scenario 3 class-probability reweighting, normalised to sum to 1 (Eq. 4, p. 90370).
- `jp_final = w0p0 + wrpr + wwpw` — Adaptive Fusion of the three Random Forest models' class probabilities, with w0 + wr + ww = 1 (Eq. 5, p. 90370; the conversion renders the left-hand symbol as `jp_final`).
- `ŷ_ensemble,i(x) = mode({ŷ_i,j(x)}^4_{j=1})` — Soft-voting ensemble prediction (Algorithm 1, p. 90371).
- `ŷ_fusion(x) = argmax_c pfinal(x)_c` — Final fused class prediction (Algorithm 1, p. 90371).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Vanilla Random Forest performance on original dataset | accuracy | 0.77 | — | — | Sec. V, p. 90370 (Table 1) |
| Vanilla Random Forest performance on original dataset | precision | 0.737 | — | — | Sec. V, p. 90370 (Table 1) |
| Vanilla Random Forest performance on original dataset | F1 score | 0.680 | — | — | Sec. V, p. 90370 (Table 1) |
| Vanilla Random Forest performance on original dataset | ROC-AUC | 0.768 | — | — | Sec. V, p. 90370 (Table 1) |
| Vanilla XGBoost performance on original dataset | ROC-AUC | 0.760 | — | — | Sec. V, p. 90370 |
| Vanilla Naive Bayes performance on original dataset | ROC-AUC | 0.662 | — | — | Sec. V, p. 90370 |
| Vanilla CART performance on original dataset | ROC-AUC | 0.602 | — | — | Sec. V, p. 90370 |
| Retrained Random Forest, Ensemble and Adaptive Fusion models | accuracy | 95.0% | — | — | Abstract, p. 90365 |
| Retrained Random Forest, Ensemble and Adaptive Fusion models | precision | 0.9275 | — | — | Abstract, p. 90365 |
| Retrained Random Forest, Ensemble and Adaptive Fusion models | recall | 0.9645 | — | — | Abstract, p. 90365 |
| Retrained Random Forest, Ensemble and Adaptive Fusion models | F1-score | 0.9426 | — | — | Abstract, p. 90365 |
| Retrained Random Forest, Ensemble and Adaptive Fusion models | ROC-AUC | exceeding 0.96 | — | — | Abstract, p. 90365 |
| DGHNL state-of-the-art comparison | accuracy | 94.60% | — | — | Abstract, p. 90365 |
| DGHNL state-of-the-art comparison | AUC | 0.9360 | — | — | Abstract, p. 90365 |
| Instance-based transfer learning credit risk model [6] | AUC improvement | 24% | — | — | Sec. II-A, p. 90367 |
| DriftLens real-time drift detection [9] | classification time | less than 0.2 seconds | — | — | Sec. II-A, p. 90367 |
| DriftLens speed relative to other detectors [9] | speed | at least five times faster | — | — | Sec. II-A, p. 90367 |
| DriftLens use-case performance [9] | use cases outperformed | 11 out of 13 | — | — | Sec. II-A, p. 90367 |
| DriftLens drift curve fit [9] | correlation index | ≥ 0.85 | — | — | Sec. II-A, p. 90367 |
| CatSight average accuracy increase over conventional classification [10] | accuracy increase | 10.5% | — | — | Sec. II-A, p. 90367 |
| Knowledge-Maximized Ensemble (KME) accuracy on synthetic datasets [22] | accuracy | 85% to 95% | — | — | Sec. VI, p. 90372 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "This study proposes an adaptive credit scoring framework, termed Adaptive Fusion, designed to address drift in developing economy environments." | Abstract, p. 90365 | model_algorithm_integration |
| "Experimental results demonstrate that the Retrained Random Forest, Ensemble, and Adaptive Fusion models achieve superior and consistent performance" | Abstract, p. 90365 | model_performance_evaluation |
| "each attaining an accuracy of 95.0%, a precision of 0.9275, a recall of 0.9645, an F1-score of 0.9426, and ROC-AUC values exceeding 0.96" | Abstract, p. 90365 | model_performance_evaluation |
| "Compared to state-of-the-art models such as the Deep Genetic Hierarchical Network of Learners (DGHNL), which achieves 94.60% accuracy and an AUC of 0.9360, the proposed approach demonstrates improved predictive capability" | Abstract, p. 90365 | model_performance_evaluation |
| "The Adaptive Fusion algorithm, which dynamically weights and integrates model outputs in real time, emerges as the most robust solution, enabling continuous adaptation to evolving data patterns." | Abstract, p. 90365 | model_algorithm_integration |
| "The process starts by training the initial model using the vanilla models, CART, XGBoost, Naïve Bayes, and Random Forest." | Sec. IV, p. 90370 | model_development |
| "In this vanilla testing phase, Random Forest proved to be the best performer; hence, it was used as the baseline for adaptive model development." | Sec. IV, p. 90370 | model_development |
| "It achieved the highest accuracy (0.77), precision (0.737), F1 score (0.680), and ROC-AUC (0.768), indicating a strong predictive capability" | Sec. V, p. 90370 | model_performance_evaluation |
| "Across all three drift scenarios (drift1–drift3), the adaptive_fusion strategy delivered the strongest and most stable performance, achieving the highest values for accuracy, precision, recall, F1-score, and ROC-AUC with minimal degradation as drift occurred" | Sec. V, p. 90371 | model_algorithm_integration |
| "The sliding window method performed the worst overall, with the largest deficits in recall and F1 score. These findings support the adoption of adaptive_fusion as a default strategy for drift-prone settings." | Sec. V, p. 90372 | model_performance_evaluation |
| "The proposed Adaptive_Fusion method differs from static ensembles by updating model weights dynamically rather than keeping them fixed after training." | Sec. VI, p. 90372 | model_algorithm_integration |
| "Credit scores are calculated based on financial history, current assets, and liabilities. Typically, it tells a lender or investor the probability of the subject being able to pay back a loan." | Sec. I, p. 90365 | savings_debt_management |
| "Future work needs to include the use of a data stream that can be studied and analyzed to detect different kinds of concept drift the data may suffer" | Sec. VII, p. 90373 | model_development |
| "This innovation fills a critical gap in the current literature, as most adaptive credit scoring models rely on either retraining or fixed ensemble strategies." | Sec. VI, p. 90372 | model_algorithm_integration |

## Remember This

- Adaptive Fusion maintains three Random Forest models (m0, mretrain, mwindow) and fuses their class probabilities with dynamic weights (Eq. 5).
- Drift is simulated on the German Credit benchmark in three ways: age +5, credit amount +N(0,1000), and default class reduced to 20%.
- Four adaptation strategies are compared: retraining, windowing (W = 100), soft-voting ensemble, and Adaptive Fusion.
- Vanilla Random Forest was best in the static test (accuracy 0.77, ROC-AUC 0.768); XGBoost ROC-AUC 0.760; Naive Bayes 0.662; CART 0.602.
- The abstract reports 95.0% accuracy, 0.9275 precision, 0.9645 recall, 0.9426 F1 and ROC-AUC above 0.96 for the Retrained RF, Ensemble and Adaptive Fusion models — identical values for all three, which conflicts with the body's ranking.
- DGHNL is cited at 94.60% accuracy and AUC 0.9360 as the state-of-the-art comparison.
- No confidence intervals, p-values, per-scenario numbers, or hyperparameters are reported for the paper's own experiments.

## Cited Works

- World Bank Group (2019) (context) — Disruptive Technologies in the Credit Information Sharing Industry; cited for the definition and role of credit scoring. [p. 90366]
- FasterCapital (2025) (context) — Credit Scoring Models: A Comparison of Different Approaches and Their Applications; cited for scoring letter/value ranges and for the need for adaptive scoring under changing data distributions. [p. 90366]
- Addy, W. A.; Ajayi-Nifise, A. O.; Bello, B. G.; Tula, S. T.; Odeyemi, O.; Falaiye, T. (2024) (context) — Comprehensive review of AI in credit scoring, models and predictive analytics; cited for behavioural/collection/fraud scoring categories and for the inaccuracy of static models after economic change. [p. 90366]
- Liu, A.; Lu, J.; Zhang, G. (2021) (methodology) — Diverse Instance-Weighting Ensemble (DiwE), an instance-based ensemble that measures diversity by regional drift disagreement. [p. 90366]
- Nikolaidis, D.; Doumpos, M. (2022) (methodology) — Adaptive behavioural credit scoring using local regions of competence via kNN; local logistic regression reportedly outperforms global counterparts. [p. 90366]
- Wang, M.; Yang, H. (2021) (methodology) — Personal credit risk assessment based on instance-based transfer learning; reports a 24% AUC improvement over conventional ML. [p. 90367]
- Wei, Q.; Liu, Y.; Wu, K. (2021) (methodology) — Transfer learning for credit scoring; SPY-Transfer and SPY-TrAdaBoost address the cold-start problem. [p. 90367]
- Barddal, J. P.; Loezer, L.; Enembreck, F.; Lanzuolo, R. (2020) (methodology) — Data stream classification applied to credit scoring on three Brazilian datasets; Adaptive Random Forests match or outperform batch models. [p. 90367]
- Greco, S.; Vacchetti, B.; Apiletti, D.; Cerquitelli, T. (2025) (methodology) — DriftLens, an unsupervised real-time concept-drift detector for deep learning representations; classifies drift in under 0.2 seconds, 11 of 13 use cases, correlation index ≥ 0.85. [p. 90367]
- Flórez, A.; Rodríguez-Moreno, I.; Artetxe, A.; Olaizola, I. G.; Sierra, B. (2023) (methodology) — CatSight, concept-drift detection in multivariate time series using Common Spatial Patterns; average accuracy increase of 10.5%. [p. 90367]
- Chislett, L.; Vallejos, C. A.; Cannings, T. I.; Liley, J. (2024) (methodology) — AMUSE, reinforcement-learning-based adaptive model updating in a simulated environment. [p. 90368]
- Tang, J.; Lin, K.-Y.; Li, L. (2022) (methodology) — Incremental SVM with domain adaptation for drift data; gains over standard and incremental SVM on four of five industrial and four synthetic datasets. [p. 90368]
- Museba, T. (2023) (baseline) — Adaptive and Dynamic Heterogeneous Ensemble (ADHE) for credit scoring; reportedly outperforms state-of-the-art models on prediction accuracy. [p. 90368]
- Bayram, B.; Köroglu, B.; Gönen, M. (2020) (methodology) — Card-based incremental Gradient Boosting Tree for credit card fraud detection under concept drift and class imbalance. [p. 90368]
- Rabash, A. J.; Nazri, M. Z. A.; Shapii, A.; Al-Jumaily, A. (2023) (context) — Literature survey of stream learning under concept and feature drift. [p. 90368]
- Prasad, G. V.; Sharma, K. (2024) (methodology) — CDDF-HML, a hybrid meta-learning framework for gradual and abrupt concept drift detection. [p. 90369]
- Aguiar, G. J.; Cano, A. (2023) (methodology) — Meta-learning framework that recommends a drift detector in real time from sliding-window meta-features. [p. 90369]
- Lima, M.; Neto, M.; Filho, T. S.; Fagundes, R. A. D. A. (2022) (methodology) — Systematic literature review of learning under concept drift for regression; source of the three-phase drift detection/understanding/adaptation structure. [p. 90369]
- Krempl, G.; Hofer, V.; Nielsen, M. K.; Verge, T. (2000) (context) — Models for drift-adaptive scoring; cited in support of explicit drift modelling in evolving financial datasets. [p. 90372]
- Museba, T. (2022) (context) — Adaptive particle swarm optimised XGBoost ensemble for online credit scoring; cited for limitations of windowed models in capturing long-term behavioural shifts. [p. 90372]
- Abadifard, S.; Bakhshi, S.; Gheibuni, S.; Can, F. (2023) (context) — DynED, dynamic ensemble diversification for data stream classification. [p. 90372]
- Ren, S.; Liao, B.; Zhu, W.; Li, W. (2018) (context) — Knowledge-Maximized Ensemble for different types of concept drift; reported at 85%–95% accuracy on synthetic datasets. [p. 90372]