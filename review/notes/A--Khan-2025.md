---
paper_id: A--Khan-2025
first_author: Khan
year: 2025
title: "Model-agnostic explainable artificial intelligence methods in finance: a systematic review, recent developments, limitations, challenges and future directions"
venue: "Artificial Intelligence Review"
doi: 10.1007/s10462-025-11215-9
designation: algorithm
status: extracted
modules: [model_algorithm_integration, model_performance_evaluation]
module_rationale:
  model_algorithm_integration: "The review systematically analyses how model-agnostic explainability techniques (SHAP, LIME, counterfactuals, PDPs) integrate with diverse ML/DL models across financial applications, with a full taxonomy and method-by-method treatment in Sect. 8 and Table 3."
  model_performance_evaluation: "Table 7 (p. 43) catalogues the performance metrics — accuracy, F1-score, MSE, RMSE, ROC, confusion matrix — used to evaluate models in the 150 reviewed studies, and Sect. 9.5–9.6 distinguishes model-performance from explainability metrics."
---

# A--Khan-2025 — Model-agnostic explainable artificial intelligence methods in finance

## Summary

A systematic literature review of Model-Agnostic Explainable Artificial Intelligence (MA-XAI) methods applied to financial decision-making. The review screens 1,115 records published between 2010 and July 2024 and retains 150 peer-reviewed studies, classifying them by XAI technique, AI/ML/DL model, financial dataset and evaluation metric. It reports that SHAP and LIME together account for 52% of the MA-XAI methods used in the reviewed studies, that ANN and boosting families dominate the underlying models, and that the most frequently used datasets are credit-scoring and fraud-detection corpora (UCI Credit Card, FICO XAI Challenge, Home Credit Default Risk, Lending Club, Kaggle Fraud Detection, German Credit). The paper proposes a three-axis taxonomy (model-specific vs model-agnostic; local vs global; intrinsic vs post-hoc), itemises limitations of MA-XAI in finance (high-dimensional and temporal data, abstract features, local inconsistency, scalability, real-time constraints, fairness, nonlinearity, static-vs-dynamic relations, missing macro context), and outlines future directions toward hybrid and regulatory-aligned XAI.

## Problem and Motivation

AI and ML have improved predictive capability in credit scoring, fraud detection, portfolio management and risk assessment, but the “black box” nature of complex models raises transparency, trust and regulatory-compliance concerns. Financial regulators, institutions and customers demand explanations that justify automated decisions, particularly under GDPR, Basel III and the FCRA. The paper argues that Model-Agnostic XAI methods are the most widely adopted response because they can be applied to any ML model regardless of architecture, and that a consolidated review of their use in finance is missing. The objectives listed (Sect. 1.2, pp. 3–5) are to perform an SLR of MA-XAI in finance, to document 150 studies under PRISMA, to analyse prevalent techniques, to catalogue datasets and metrics, to detail selection criteria, to identify limitations and advantages, and to propose future research directions.

## Method

**Design.** Systematic literature review (SLR) following Kitchenham and Charters’ systematic-review guidelines and reported through a PRISMA-style multi-stage selection flowchart; the authors state no formal design label beyond “systematic review” and “survey”.
**Sample.** n = 150 peer-reviewed studies (unit of analysis: a published article), selected from an initial pool of 1,115 records published between 2010 and July 2024.
**Context.** geography: global literature, with India publishing the highest number of articles in this domain, followed by the United States and Germany (Sect. 5, p. 20); population: peer-reviewed journal and conference articles on XAI in financial applications (no human participants); setting: academic literature review, with articles retrieved from IEEE Xplore, ACM Digital Library, SpringerLink, ScienceDirect, Web of Science and Google Scholar, refined with Boolean AND/OR operators.

Search and screening stages (Sect. 5.1–5.4, pp. 20–22):

- Initial search yielded 1,115 articles (2010–July 2024).
- Duplicate and ineligible records removed, leaving 370 articles (795 removed).
- Title-and-abstract review removed 130 further papers, leaving 240.
- Full-text analysis applying four criteria (empirical validation, relevance to XAI and financial decision-making, contribution to explainability and transparency, publication in high-impact journals or top-tier conferences) retained 150 high-quality studies.

Taxonomy construction (Sect. 7, pp. 23–26): XAI techniques are differentiated on three axes — model-specific vs model-agnostic; global vs local; intrinsic vs post-hoc. The MA methods reviewed in detail are SHAP, LIME, PDPs, ICE plots, ALE plots, counterfactuals, PASTLE, CASTLE, Anchors, MANE, DALE, Rational Shapley Values and TREPAN (Sect. 8, pp. 26–34). Section 8.3–8.5 additionally treats attention mechanisms, dimensionality reduction, and knowledge distillation / rule extraction as explanation strategies.

Quantitative analysis (Sect. 9, pp. 34–44) answers five research questions (Table 1, p. 24): RQ1 on which XAI framework is widely used, RQ2 on frequent MA-XAI techniques, RQ3 on AI/ML algorithms, RQ4 on datasets, RQ5 on performance metrics.

## Software

Not applicable. The paper is a literature review and reports no software, code, or computational environment of its own.

## Key Findings

- MA explanations are the dominant XAI framework in the reviewed finance literature; MA methods are more widely adopted than model-specific methods because of their versatility (Sect. 9.1, p. 35; Fig. 18).
- SHAP (18 publications) and LIME (14 publications) are the most frequently used MA-XAI techniques; combined they account for 52% of the total MA methods used in the study (Table 4, p. 36; Sect. 9.2, p. 35).
- Counterfactual explanations follow with 10 publications, then teacher-student model (6), dimensionality reduction (4), attention mechanism (3), PDPs (2), MANE (2), and single-publication methods (ICE, ALE, PASTLE, CASTLE, Anchors, DALE, Rational Shapley values, TREPAN) (Table 4, p. 36).
- Among AI/ML algorithms applied in the reviewed studies, ANN variants (8), boosting (7), logistic regression (5), bagging/RF (4), SVM (4), PCA (3), and general/other categories follow; LSTM appears once (Table 5, p. 38).
- The review states that ANNs and Boosting ML algorithms (XGBoost, LightGBM, CatBoost) “dominate financial AI research, accounting for 50% of the total applications” (Sect. 12.4, p. 48).
- The datasets most used in MA-XAI finance research are credit-scoring and fraud-detection corpora: UCI Credit Card, FICO XAI Challenge, Home Credit Default Risk, Lending Club, Kaggle Fraud Detection, German Credit, Kaggle Stock Market, S&P 500, financial-news datasets, Yahoo Finance, and Bank Marketing (Table 6, pp. 41–42).
- Accuracy is the most-reported performance metric (13 studies), followed by MSE and RMSE (3 each), confusion matrix (3), precision & recall (2), MAE (2), ROC (2), and single-use metrics including F1-score, SD, Poisson distribution, p-value, percentage error and RSS (Table 7, p. 43).
- The review introduces explainability metrics — fidelity (approximation accuracy), consistency (stability), and sparsity — as distinct from model-performance metrics (Sect. 9.6, pp. 43–44).
- SHAP is characterised as providing highly faithful, globally and locally consistent feature attributions, making it preferred where transparency and accountability are critical; LIME is characterised as computationally efficient but unstable across perturbations, making it less reliable in high-stakes applications (Sect. 9.6, p. 44).
- The paper lists nine categories of limitations for MA-XAI in finance (Sect. 10–11.7, pp. 45–46): high-dimensional and temporal data, abstract/derived features, lack of global interpretability and domain knowledge, local inconsistency and scalability, computational efficiency and real-time constraints, fairness and bias mitigation, simplification of nonlinear relationships, static vs dynamic relationships, and missing broader context.
- Proposed remedies (Sect. 11.8–11.13, pp. 47–48): model distillation and quantisation for computational efficiency; hybrid XAI models; domain-specific adaptation; real-time computational optimisation; integration with Basel III, GDPR and FCRA regulatory frameworks; and fairness-aware modelling with adversarial debiasing.

## Key Figures and Tables

- Fig. 1 (p. 2): Key features of AI across finance, healthcare and decision-making systems.
- Fig. 2 (p. 4): Comparative overview of commonly used AI models in finance (ML, DL, XAI) and their roles.
- Fig. 3 (p. 7): Structural breakdown of the survey paper.
- Fig. 4 (p. 17): Comparison between traditional black-box AI models and XAI models.
- Fig. 5 (p. 18): Percentage-wise distribution of XAI techniques across financial applications (credit scoring, fraud detection, risk management).
- Fig. 6 (p. 20): Goals of XAI.
- Fig. 7 (p. 21): Trade-off between model explainability and performance accuracy.
- Fig. 8 (p. 21): Year-wise number of articles published.
- Fig. 9 (p. 22): Geographical distribution of research publications on XAI in finance.
- Fig. 10 (p. 23): PRISMA systematic literature review methodology.
- Fig. 11 (p. 24): Taxonomy of XAI methods.
- Fig. 12 (p. 29): Feature importance comparison for three ML models on cross-entropy loss.
- Fig. 13 (p. 30): SHAP and LIME feature explanations visualised using spectral clustering.
- Fig. 14 (p. 30): Example PDP relating input features to model predictions.
- Fig. 15 (p. 31): ICE plot of single-feature influence at individual-instance level.
- Fig. 16 (p. 31): ALE plot showing feature influences accounting for interactions.
- Fig. 17 (p. 33): Silhouette analysis of LIME-based data clustering.
- Fig. 18 (p. 35): Model-specific vs model-agnostic explainability methods in financial AI.
- Fig. 19 (p. 37): Percentage distribution of MA explainability methods.
- Table 1 (p. 24): Research questions RQ1–RQ5.
- Table 2 (p. 28): Criteria for selecting MA methods (what, examples, mechanism, applicability, explainability, type, ease of use).
- Table 3 (p. 27): MA-XAI methods in finance — SHAP, LIME, PDPs, ICE, ALE, counterfactuals, PASTLE, CASTLE, Anchors, MANE, DALE, Rational Shapley values, TREPAN, with model-agnostic/local/global/post-hoc/intrinsic flags.
- Table 4 (p. 36): Author-wise MA-XAI publications in finance with technique counts.
- Table 5 (p. 38): List of AI models used by the researchers with counts.
- Table 6 (pp. 41–42): Financial dataset descriptions with links.
- Table 7 (p. 43): Performance metrics used by the researchers with counts.

## Limitations and Gaps

Acknowledged by the authors:

- A trade-off exists between explainability and predictive accuracy: interpretable models (decision trees, linear regression) generally achieve lower accuracy than complex models such as DNNs (Sect. 13, p. 49).
- Computational complexity and scalability remain critical concerns for computationally intensive post-hoc methods such as SHAP and LIME on large financial datasets (Sect. 13, p. 49).
- The generalisability of XAI methods across diverse financial contexts is still uncertain; adaptive frameworks tailored to stock prediction, credit scoring and fraud detection are needed (Sect. 13, p. 49).
- Regulatory compliance and trustworthiness require alignment with GDPR, Basel III and the FCRA; standardised XAI-driven auditing tools are not yet established (Sect. 13, p. 49).
- Underexplored applications remain, including portfolio optimisation, internet financing platforms, and advanced fraud-detection mechanisms (Sect. 13, p. 50).
- Local explanations generated by methods such as LIME can vary significantly across similar instances, reducing stakeholder confidence (Sect. 11.2, p. 46).
- MA-XAI methods can oversimplify nonlinear financial relationships and neglect dynamic feature interdependencies, and they generally fail to incorporate broader geopolitical, regulatory and macroeconomic context (Sect. 11.5–11.7, p. 46).

[unacknowledged] The paper contradicts itself on the size of its own review sample: the Abstract (p. 1) states “analysis of 150 peer-reviewed studies”, while Sect. 12.1 (p. 48) states “We reviewed 60 high-quality articles”. Both numbers appear in the paper with no reconciliation.

[unacknowledged] The 50% claim for ANN and boosting families (Sect. 12.4, p. 48) does not match the counts the paper itself reports in Table 5: ANN count 8 and Boosting count 7 out of a Table 5 total of 45, i.e. 33%, not 50%. The review does not state which denominator produces 50%.

[unacknowledged] Table 4 and Table 5 use inconsistent aggregation categories: Table 4 lists “Teacher-student model”, “Dimensionality reduction” and “Attention mechanism” as XAI techniques with counts 6, 4 and 3, while Table 5 lists “Dimensionality Reduction” (1) and “DL Model” (2) as AI algorithms — so the same label names different things across tables.

[unacknowledged] The paper’s RQ4 answer (datasets) does not report any frequency count per dataset, so the relative usage of the eleven datasets in Table 6 cannot be verified from the paper.

[unacknowledged] The review reports no inter-rater reliability for its screening decisions, no PRISMA checklist, no risk-of-bias assessment of the 150 included studies, and no meta-analytic synthesis; all evidence is descriptive tabulation.

[unacknowledged] The designation of “most widely used” MA-XAI methods rests on publication counts (Table 4) rather than on reported performance comparisons, so claims such as “LIME and SHAP are effective in detecting bias and ensuring fairness” (Sect. 9.2, p. 35) are not backed by a quantitative synthesis within the paper.

## Definitions

- **XAI (Explainable Artificial Intelligence)** — A collection of techniques and approaches designed to empower human users to comprehend, trust, and oversee AI outputs and decisions (Sect. 1.3.8, p. 6).
- **Model-specific (MS) explanation** — Explanation methods tailored to classes of models, such as specific types of NNs (Sect. 7.1.1, p. 24).
- **Model-agnostic (MA) explanation** — Explanation that does not depend on the type of neural network and operates solely on its input and output (Sect. 7.1.2, p. 25).
- **Global explanation** — Dataset-level explanation revealing the overall relationships learned by the neural network (Sect. 7.2.1, p. 25).
- **Local explanation** — Explanation focused on a single input (Sect. 7.2.2, p. 25).
- **Intrinsic model** — A model inherently interpretable because of its simple, transparent structure (decision trees, linear regression, rule-based systems) (Sect. 7.3.1, p. 26).
- **Post-hoc explanation** — Methods applied after a model has been trained to provide insights into its decision-making process (LIME, SHAP, saliency maps) (Sect. 7.3.2, p. 26).
- **SHAP (Shapley Additive exPlanations)** — A unified approach to interpreting ML models based on cooperative game theory and Shapley values, quantifying each feature’s contribution to the final prediction (Sect. 8.1.1, p. 28).
- **LIME (Local Interpretable Model-agnostic Explanations)** — A technique that explains individual predictions by locally approximating the black-box model with an interpretable model (Sect. 8.2, p. 33).
- **PDPs (Partial Dependence Plots)** — A method showing how one feature influences another and the target feature, providing global explanations (Sect. 8.1.2, p. 29).
- **ICE (Individual Conditional Expectation) plots** — A visualisation showing how each instance’s prediction changes when a feature is varied (Sect. 8.1.3, p. 29).
- **ALE (Accumulated Local Effects) plots** — Plots that consider the local distribution of features to provide unbiased insights in the presence of feature interactions (Sect. 8.1.4, p. 29).
- **Counterfactual explanations** — Explanations showing how changing certain features can alter a model’s prediction (Sect. 8.1.5, p. 30).
- **PASTLE** — Partial Dependency and Accumulated Local Effects, a hybrid combining PDP and ALE strengths (Sect. 8.1.6, p. 32).
- **CASTLE** — Conditional Accumulated SHAP and Local Effects, combining SHAP values and ALE (Sect. 8.1.7, p. 32).
- **Anchors** — Specific conditions or rules that guarantee a certain prediction with high precision (Sect. 8.1.8, p. 32).
- **MANE** — Model-Agnostic Neural Explanations for any ML model using NNs (Sect. 8.1.9, p. 32).
- **DALE** — Differential Accumulated Local Effects, comparing feature-change effects between groups or contexts (Sect. 8.1.10, p. 32).
- **Rational Shapley Values (RSV)** — A refinement of traditional Shapley values addressing interaction-heavy scenarios (Sect. 8.1.11, p. 32).
- **TREPAN** — Decision Tree Induction based on TREPANning; builds compact interpretable decision trees (Sect. 8.1.12, p. 33).
- **Fidelity** — How well a simpler interpretable surrogate approximates the behaviour of the original complex model (Sect. 9.6.1, p. 43).
- **Sparsity** — The conciseness of an explanation, typically measured by the number of features used (Sect. 9.6.1.2, p. 44).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Review sample, initial search yield 2010–July 2024 | number of articles | 1,115 | — | — | Sect. 5.1, p. 20 |
| Review sample, after automated filtering and duplicate removal | number of articles | 370 | — | — | Sect. 5.2, p. 21 |
| Review sample, records removed at automated filtering stage | number of articles | 795 | — | — | Sect. 5.2, p. 21 |
| Review sample, after title-and-abstract review | number of articles | 240 | — | — | Sect. 5.3, p. 22 |
| Review sample, additional papers removed at title-and-abstract stage | number of articles | 130 | — | — | Sect. 5.3, p. 22 |
| Review sample, final high-quality studies selected | number of articles | 150 | — | — | Sect. 5.4, p. 22 |
| Review sample as stated in the abstract | number of studies | 150 | — | — | Abstract, p. 1 |
| Review sample as stated in Sect. 12.1 | number of articles | 60 | — | — | Sect. 12.1, p. 48 |
| SHAP usage in reviewed MA-XAI finance studies | publication count | 18 | — | — | Table 4, p. 36 |
| LIME usage in reviewed MA-XAI finance studies | publication count | 14 | — | — | Table 4, p. 36 |
| PDPs usage in reviewed MA-XAI finance studies | publication count | 2 | — | — | Table 4, p. 36 |
| ICE Plots usage in reviewed MA-XAI finance studies | publication count | 1 | — | — | Table 4, p. 36 |
| ALE Plots usage in reviewed MA-XAI finance studies | publication count | 1 | — | — | Table 4, p. 36 |
| Counterfactuals usage in reviewed MA-XAI finance studies | publication count | 10 | — | — | Table 4, p. 36 |
| PASTLE usage in reviewed MA-XAI finance studies | publication count | 1 | — | — | Table 4, p. 36 |
| CASTLE usage in reviewed MA-XAI finance studies | publication count | 1 | — | — | Table 4, p. 36 |
| Anchors usage in reviewed MA-XAI finance studies | publication count | 1 | — | — | Table 4, p. 36 |
| MANE usage in reviewed MA-XAI finance studies | publication count | 2 | — | — | Table 4, p. 36 |
| DALE usage in reviewed MA-XAI finance studies | publication count | 1 | — | — | Table 4, p. 36 |
| Rational Shapley values usage in reviewed MA-XAI finance studies | publication count | 1 | — | — | Table 4, p. 36 |
| TREPAN usage in reviewed MA-XAI finance studies | publication count | 1 | — | — | Table 4, p. 36 |
| Teacher-student model usage in reviewed studies | publication count | 6 | — | — | Table 4, p. 36 |
| Dimensionality reduction usage in reviewed studies | publication count | 4 | — | — | Table 4, p. 36 |
| Attention mechanism usage in reviewed studies | publication count | 3 | — | — | Table 4, p. 36 |
| Combined share of LIME and SHAP among MA methods used | percentage | 52% | — | — | Sect. 9.2, p. 35 |
| ANN (GAM, GLM, CANN, SOFM, DNN) usage | publication count | 8 | — | — | Table 5, p. 38 |
| Logistic Regression (LR), Bayesian LR usage | publication count | 5 | — | — | Table 5, p. 38 |
| LSTM usage | publication count | 1 | — | — | Table 5, p. 38 |
| PCA usage | publication count | 3 | — | — | Table 5, p. 38 |
| Naïve Bayes / Bayesian approach usage | publication count | 1 | — | — | Table 5, p. 38 |
| Decision Tree Classifier usage | publication count | 2 | — | — | Table 5, p. 38 |
| General ML model usage | publication count | 2 | — | — | Table 5, p. 38 |
| Boosting (XGB, Regression Tree, Light GBM) usage | publication count | 7 | — | — | Table 5, p. 38 |
| Bagging (RF) usage | publication count | 4 | — | — | Table 5, p. 38 |
| SVM, SVM Regression, dual fuzzy SVM usage | publication count | 4 | — | — | Table 5, p. 38 |
| Regression, Poisson Regression usage | publication count | 2 | — | — | Table 5, p. 38 |
| Genetic Algorithm (clustering) usage | publication count | 1 | — | — | Table 5, p. 38 |
| Decision Support System (clustering) usage | publication count | 1 | — | — | Table 5, p. 38 |
| Fuzzy Logic usage | publication count | 1 | — | — | Table 5, p. 38 |
| Dimensionality Reduction usage | publication count | 1 | — | — | Table 5, p. 38 |
| DL Model usage | publication count | 2 | — | — | Table 5, p. 38 |
| Share of applications attributable to ANNs and Boosting algorithms | percentage | 50% | — | — | Sect. 12.4, p. 48 |
| Accuracy as reported evaluation metric | study count | 13 | — | — | Table 7, p. 43 |
| Precision & Recall as reported evaluation metric | study count | 2 | — | — | Table 7, p. 43 |
| F1-Score as reported evaluation metric | study count | 1 | — | — | Table 7, p. 43 |
| Mean Squared Error (MSE) as reported evaluation metric | study count | 3 | — | — | Table 7, p. 43 |
| Root Mean Squared Error (RMSE) as reported evaluation metric | study count | 3 | — | — | Table 7, p. 43 |
| Standard deviation (SD) as reported evaluation metric | study count | 1 | — | — | Table 7, p. 43 |
| Poisson Distribution as reported evaluation metric | study count | 1 | — | — | Table 7, p. 43 |
| P-Value as reported evaluation metric | study count | 1 | — | — | Table 7, p. 43 |
| Percentage Error as reported evaluation metric | study count | 1 | — | — | Table 7, p. 43 |
| Mean Absolute Error (MAE) as reported evaluation metric | study count | 2 | — | — | Table 7, p. 43 |
| Root Sum Square (RSS) as reported evaluation metric | study count | 1 | — | — | Table 7, p. 43 |
| Confusion Matrix as reported evaluation metric | study count | 3 | — | — | Table 7, p. 43 |
| Receiver Operating Characteristics (ROC) as reported evaluation metric | study count | 2 | — | — | Table 7, p. 43 |
| PwC (2017) projection of global GDP rise attributable to AI by 2030 | percentage | up to 14% | — | — | Sect. 1.1, p. 2 |
| Stock prediction accuracy reported by Khan et al. using social media | accuracy | 80.53% | — | — | Sect. 3.2.1, p. 11 |
| Stock prediction accuracy reported by Khan et al. using financial news | accuracy | 75.16% | — | — | Sect. 3.2.1, p. 11 |
| DNN predictive power reported by Dixon et al. | accuracy | 68% | — | — | Sect. 3.2.1, p. 12 |
| LSTM stock-price forecasting accuracy reported by Ozbayoglu et al. | accuracy | 91.5% | — | — | Sect. 3.2.1, p. 12 |
| Sequence-to-sequence market-trend accuracy reported by Wang et al. | accuracy | 85% | — | — | Sect. 3.2.1, p. 12 |
| Deep reinforcement learning trading precision reported by Huang | precision | 92% | — | — | Sect. 3.2.1, p. 12 |
| LSTM credit-card fraud detection F1-score reported by Jurgovsky et al. | F1-score | 0.93 | — | — | Sect. 3.2.2, p. 12 |
| RF and logistic-regression fraud detection F1-score reported by Jurgovsky et al. | F1-score | 0.85 | — | — | Sect. 3.2.2, p. 12 |
| IMEML model accuracy reported by Talukder et al. on 284,807 credit-card transactions | accuracy | 99.94% | — | — | Sect. 3.2.2, p. 12 |
| IMEML model precision reported by Talukder et al. | precision | 99.91% | — | — | Sect. 3.2.2, p. 12 |
| IMEML model recall reported by Talukder et al. | recall | 99.14% | — | — | Sect. 3.2.2, p. 12 |
| IMEML model F1-score reported by Talukder et al. | F1-score | 99.52% | — | — | Sect. 3.2.2, p. 12 |
| IMEML model AUC reported by Talukder et al. | AUC | 100% | — | — | Sect. 3.2.2, p. 12 |
| DBN fraud detection accuracy reported by Bhowmik et al. with 70:30 split | accuracy | 94% | — | — | Sect. 2, p. 8 |
| DNN credit scoring AUC reported by Xiao et al. | AUC | 0.92 | — | — | Sect. 3.2.5, p. 14 |
| DNN credit scoring accuracy advantage over FICO reported by Xiao et al. | percentage advantage | 20% | — | — | Sect. 3.2.5, p. 14 |
| Cost savings of LVQ neural network over logit-based credit methods reported by Abedin et al. | percentage | 6–25% | — | — | Sect. 3.2.5, p. 14 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "Through analysis of 150 peer-reviewed studies, the paper identifies key challenges, such as balancing interpretability with predictive accuracy, managing computational complexity, and meeting regulatory requirements." | Abstract, p. 1 | model_algorithm_integration |
| "LIME and SHAP have been widely used in the finance domain because they can be applied to any ML model, which accounts for 52% of the total MA methods used in this study." | Sect. 9.2, p. 35 | model_algorithm_integration |
| "MA explanation does not depend on the type of neural network and operates solely on its input and output." | Sect. 7.1.2, p. 25 | model_algorithm_integration |
| "In finance, where decision-making is heavily regulated and explanations are crucial for transparency and trust, MA-XAI methods play a key role in interpreting complex model outputs." | Sect. 8, p. 26 | model_algorithm_integration |
| "SHAP provides highly faithful, globally, and locally consistent feature attributions, making it a preferred choice for financial decision-making, where transparency and accountability are critical." | Sect. 9.6, p. 44 | model_performance_evaluation |
| "LIME, while computationally efficient, may suffer from stability issues, as different perturbations can yield slightly different explanations for the same instance, making it less reliable in high-stakes financial applications such as risk management." | Sect. 9.6, p. 44 | model_performance_evaluation |
| "Financial datasets frequently encompass high-dimensional data involving numerous market variables, economic indicators, and complex temporal structures." | Sect. 10.1, p. 45 | model_algorithm_integration |
| "MA-XAI techniques, such as SHAP and LIME, struggle to manage high-dimensional and sequential data, as their explanations become less insightful or overly generalized." | Sect. 10.1, p. 45 | model_algorithm_integration |
| "Future research should focus on developing scalable, real-time XAI solutions that optimize both accuracy and computational feasibility, particularly in the context of high-frequency financial transactions." | Sect. 9.6, p. 44 | model_performance_evaluation |
| "The ideal solution should have both high explainability and performance." | Sect. 4.4, p. 19 | model_algorithm_integration |
| "Given the regulatory sensitivity of fraud detection, integrating XAI techniques into fraud detection models is crucial for ensuring accountability and compliance." | Sect. 3.2.2, p. 12 | model_algorithm_integration |
| "They highlighted the trade-off between explainability and model accuracy, particularly in DL models." | Sect. 12.5, p. 49 | model_algorithm_integration |
| "It was identified that Artificial Neural Networks (ANNs) and Boosting ML algorithms (XGBoost, LightGBM, and CatBoost) dominate financial AI research, accounting for 50% of the total applications." | Sect. 12.4, p. 48 | model_algorithm_integration |
| "Given the inherent volatility and noise present in financial data, local explanations generated by methods like LIME can vary significantly across similar instances." | Sect. 11.2, p. 46 | model_performance_evaluation |
| "Financial practitioners prefer sparse explanations because simpler explanations are easier to interpret and justify to stakeholders (e.g., regulators and customers)." | Sect. 9.6.1.2, p. 44 | model_performance_evaluation |

## Remember This

- A PRISMA-style systematic review of Model-Agnostic XAI methods in finance, screening 1,115 records (2010–July 2024) down to 150 included studies.
- Proposes a three-axis XAI taxonomy: model-specific vs model-agnostic; local vs global; intrinsic vs post-hoc.
- Reports that SHAP (18 studies) and LIME (14 studies) together account for 52% of the MA-XAI methods used across the reviewed finance literature.
- Counterfactual explanations (10 studies) are the third most-used technique; PDPs, ICE, ALE, PASTLE, CASTLE, Anchors, MANE, DALE, Rational Shapley values and TREPAN each appear in ≤2 studies.
- ANN and boosting families dominate the underlying ML models, but the paper’s 50% dominance claim does not match the counts in its own Table 5 (8 + 7 out of 45 = 33%).
- The paper contradicts itself on sample size: the Abstract says 150 studies, Sect. 12.1 says 60 high-quality articles.
- The datasets most used in MA-XAI finance research are credit-scoring and fraud-detection corpora (UCI Credit Card, FICO XAI Challenge, Home Credit Default Risk, Lending Club, Kaggle Fraud Detection, German Credit).
- Accuracy is the most-reported evaluation metric (13 studies); MSE and RMSE follow (3 each).
- The paper distinguishes model-performance metrics from explainability metrics (fidelity, consistency, sparsity).
- Nine categories of MA-XAI limitations are itemised, and six remedy directions (hybrid XAI, domain adaptation, distillation, real-time optimisation, regulatory alignment, fairness) are proposed.
- The review reports no inter-rater reliability, no risk-of-bias assessment, and no meta-analytic synthesis; all findings are descriptive tabulation.