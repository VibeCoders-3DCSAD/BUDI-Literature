---
paper_id: A--Sarkar-2026
first_author: Sarkar
year: 2026
title: "A Systematic Review of AI-Driven Credit Risk Assessment Models in Commercial Banking (2018-2026)"
venue: "American Journal of Interdisciplinary Studies"
doi: 10.63125/m52yna23
designation: algorithm
status: extracted
modules: [model_algorithm_integration, model_performance_evaluation, data_collection]
module_rationale:
  model_algorithm_integration: "The review synthesises hybrid, ensemble and deep-learning architectures and how they are integrated into bank credit-decision pipelines (Findings, p. 482; Discussion, pp. 485-487)."
  model_performance_evaluation: "The Findings report measured model behaviour across the 27 studies, including AUC gains of 4% to 17%, calibration deterioration and discrimination-versus-calibration divergence (Findings, pp. 483-484)."
  data_collection: "The Methods section specifies the five-database PRISMA search and screening pipeline that produced 298 records and 27 included studies (Methods, pp. 481-482)."
---

# A--Sarkar-2026

## Summary

A systematic review, conducted under PRISMA guidelines, of AI-driven credit risk assessment models in commercial banking between 2018 and 2026. The review screened 298 records across five academic databases, reduced them to 226 unique studies, excluded 143 at title-and-abstract stage, assessed 83 full texts and retained 27 peer-reviewed studies for qualitative thematic synthesis; a meta-analysis was not feasible because of methodological heterogeneity across model types, dataset structures and evaluation practices (Methods, pp. 481-482).

The review's central finding is that AI models consistently outperformed traditional statistical baselines — particularly logistic regression and classical scorecard systems — in predictive discrimination, especially for probability of default (PD) estimation, with ensemble architectures balancing performance against calibration stability while neural architectures showed higher variance and greater sensitivity to data quality (Findings, p. 482-483). This advantage, however, was repeatedly qualified. Data quality, feature engineering and cross-context generalizability remained persistent weaknesses, with 14 of 27 studies reporting substantial degradation when models were transferred to different geographies, product types or macroeconomic environments (Findings, p. 483). Explainability, transparency and governance challenges were raised in 22 of the 27 studies, and the review describes these as a core determinant of whether AI models can move from experimentation to widespread adoption (Findings, p. 484). Post-deployment monitoring is characterised as underdeveloped: concept drift was judged a more serious regulatory risk than data drift, calibration deterioration was reported within 12–18 months of deployment in nine studies, and only five studies provided detailed post-deployment frameworks used in operational bank environments (Findings, p. 484).

The review positions the period as one of technological expansion followed by governance consolidation, in which the field converged on a "performance–explainability–compliance" triangle and regulators increasingly treated credit scoring and creditworthiness AI as higher-risk (Literature Review, p. 465). Its stated conclusion is that AI has matured into a highly promising but still incompletely integrated component of commercial banking risk management, requiring further advances in standardized reporting, privacy-preserving collaboration, causal modelling and regulator-aligned interpretability before it can be considered fully reliable for mission-critical credit decisioning and capital frameworks (Conclusion, p. 487).

## Problem and Motivation

Credit risk in commercial banking is defined in the paper as the probability that a borrower or counterparty will fail to meet contractual debt obligations in full and on time, operationalised through probability of default, loss given default (LGD) and exposure at default (EAD), and used to compute expected credit loss under IFRS 9 frameworks that became central to bank provisioning from 2018 onward (Introduction, p. 460). Credit risk assessment models transform borrower information into decisions about approval, pricing, limits, monitoring and portfolio capital allocation, and in many institutions operate alongside governance requirements for development, validation and ongoing performance monitoring (Introduction, p. 460).

The motivation for a review covering exactly 2018–2026 is framed as the convergence of three forces: the global diffusion of digital financial services and high-volume lending channels; the expansion of data environments that change how banks evaluate borrowers; and supervisory expectations about capital, governance, transparency, documentation and validation discipline (Introduction, p. 460-461). The paper argues that the international significance of AI-driven credit risk assessment rests on the combination of the central role of credit risk in bank safety and economic activity with a cross-border convergence toward measurable, governed and reviewable modelling practices (Introduction, p. 461). It further notes that banking-specific constraints make credit risk a "high-friction" domain for advanced AI, because models must be validated, monitored and governed within strict model risk management expectations while also addressing explainability and fairness obligations in consumer and prudential contexts (Literature Review, p. 465).

A further stated motivation is the gap between research innovation and real-world deployment: the abstract notes that operational requirements such as continuous monitoring, documentation and interoperability create significant barriers to adoption, and the findings report that only four of the 27 reviewed articles documented actual real-world deployment of AI models in production-grade lending environments (Abstract, p. 459; Findings, p. 483).

## Method

**Design.** Systematic review following the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines, with qualitative thematic synthesis in place of meta-analysis; the authors state the design label explicitly (Methods, pp. 481-482).
**Sample.** n = 27 peer-reviewed studies; the unit of analysis is the published study article, drawn from 298 identified records (Methods, pp. 481-482).
**Context.** geography: international — five academic databases (Scopus, Web of Science, IEEE Xplore, ScienceDirect, SSRN) with no country or region restriction stated; population: peer-reviewed empirical studies applying AI techniques to credit risk assessment tasks within commercial banks, including PD, LGD, EAD, early warning systems and credit underwriting; setting: documentary desk review of published literature, no human participants and no primary data collection.

- Search five academic databases (Scopus, Web of Science, IEEE Xplore, ScienceDirect, SSRN) using keyword combinations including "AI credit scoring," "machine learning in banking risk," "deep learning PD models," "creditworthiness prediction," "consumer and commercial lending analytics," and "automated underwriting systems" (Methods, p. 481).
- Identify 298 potentially relevant studies in the initial search phase (Methods, p. 481).
- Remove duplicates using database tools and manual verification, reducing 298 records to 226 unique studies (Methods, p. 481).
- Screen titles and abstracts against inclusion criteria requiring AI techniques applied to credit risk assessment in commercial banks, excluding studies unrelated to banking, without empirical results, or focused on fraud detection or financial forecasting; 143 studies excluded, leaving 83 (Methods, p. 481).
- Obtain and evaluate full texts of the 83 screened articles, excluding those relying solely on synthetic data, lacking methodological transparency, not evaluating performance with recognised risk metrics such as ROC-AUC, PR-AUC, KS, Brier score or calibration curves, or not framed within commercial banking contexts; additional exclusions for AI used exclusively for operational risk, AML analytics, financial sentiment analysis or macroeconomic prediction (Methods, pp. 481-482).
- Retain 27 studies as the final dataset for extraction and synthesis (Methods, p. 482).
- Extract data with a structured template aligned to PRISMA standards, capturing model architectures (gradient boosting, random forests, neural networks, transformer variants), dataset sources, sample sizes, feature engineering strategies, evaluation frameworks, explainability techniques and fairness assessments (Methods, p. 482).
- Use two independent reviewers for extraction, with disagreements resolved through consensus discussions (Methods, p. 482).
- Forego meta-analysis because of methodological heterogeneity in model types, dataset structures and evaluation practices, and instead apply qualitative thematic synthesis (Methods, p. 482).
- Organise synthesis around themes of model performance, calibration behaviour, drift sensitivity, explainability requirements and regulatory alignment (Methods, p. 482).

## Key Findings

- The 27 reviewed studies collectively referenced more than 1,240 external citations in the model-diversification theme alone (Findings, p. 482).
- AI models consistently outperformed traditional statistical models in predictive discrimination, particularly in PD estimation, where gradient boosting, random forests and deep neural networks dominated (Findings, p. 482-483).
- Twelve reviewed studies directly compared AI models with logistic regression scorecards; nine reported AUC gains ranging from 4% to 17% (Findings, p. 483).
- Ensemble methods were favoured because they balanced performance with relatively stable calibration, while neural architectures showed higher variance and more sensitivity to data quality (Findings, p. 483).
- At least seven of the 27 studies incorporated temporal, behavioural or transactional features, marking a shift toward dynamic credit risk modelling and improved short-term delinquency and early-warning prediction (Findings, p. 483).
- Only four articles reported actual real-world deployment of AI models in production-grade lending environments (Findings, p. 483).
- Seventeen articles reported that missing data, sparse variables or inconsistent reporting practices across banks restricted model accuracy (Findings, p. 483).
- Eleven studies emphasised domain-informed feature engineering, noting that automatically generated deep-learning features struggled to capture financial behaviour patterns as reliably as manually engineered features (Findings, p. 483).
- Nineteen of 27 studies explicitly tested models across multiple borrower segments or economic conditions, and 14 reported substantial degradation on transfer to different geographies, product types or macroeconomic environments (Findings, p. 483).
- Only five articles used multi-bank datasets; three of these highlighted inconsistencies in variable definitions, data collection processes and loan lifecycle structures (Findings, p. 484).
- Explainability, transparency and governance challenges were highlighted in 22 of the 27 included studies (Findings, p. 484).
- Nineteen studies stressed that banks must justify lending decisions to auditors, regulators and consumers, yet many AI models provided limited interpretability; 14 studies reported that model risk management teams struggled to validate neural network and ensemble models; 11 articles highlighted difficulty generating stable reason codes (Findings, p. 484).
- Ten studies warned that models lacking interpretability were vulnerable to embedded bias and unintentionally discriminatory outcomes, especially when trained on historical data reflecting structural inequalities (Findings, p. 484).
- Sixteen studies reported rapid performance degradation when borrower behaviour, macroeconomic conditions or institutional underwriting strategies shifted; 11 emphasised that concept drift posed more serious risks than data drift (Findings, p. 484).
- Nine studies reported reduced score-to-PD alignment within 12–18 months of deployment, and seven observed that initially fair models could become biased over time (Findings, p. 484).
- Only five studies provided detailed post-deployment frameworks used in operational bank environments, which the review reads as a gap between academic proposals and real-world implementations (Findings, p. 484).
- Eighteen studies noted the absence of high-quality, cross-bank datasets, preventing robust benchmarking and hindering fairness validation (Findings, p. 485).
- Thirteen studies emphasised performance–transparency tension, arguing that the most accurate AI models were often the least interpretable (Findings, p. 485).
- Eleven studies highlighted a lack of stress-testing readiness, stating that nonlinear models behaved unpredictably under extreme macroeconomic scenarios, reducing suitability for capital adequacy and risk-weighted asset estimation (Findings, p. 485).
- Nine studies noted causal reasoning limitations — that AI models captured correlations rather than structural cause–effect relationships (Findings, p. 485).
- Only six studies discussed privacy-preserving learning approaches such as federated learning or secure computation (Findings, p. 485).

## Key Figures and Tables

- Fig. 1 (p. 461): Artificial Intelligence for Credit Risk → positions AI as an umbrella term for computational methods that learn patterns from data within the bank modelling pipeline.
- Fig. 2 (p. 462): AI Credit Risk Assessment Framework → the layered input/model/decision/governance/outcome structure of an AI credit risk system.
- Fig. 3 (p. 466): Credit Risk Models Using AI → the coexistence of regulatory capital models and business-use decisioning models, including hybrid scorecard-plus-challenger structures.
- Fig. 4 (p. 468): Credit Risk Modeling Method Comparison → comparison of logistic scorecards, tree ensembles, support vector machines and deep architectures on tabular credit data.
- Fig. 5 (p. 470): Bank Credit Risk Data Framework → the hierarchy of traditional, transactional and alternative data sources and their governance implications.
- Fig. 6 (p. 472): Credit Risk Modeling Objectives Framework → PD, LGD, EAD, stress testing and early warning as linked objectives.
- Fig. 7 (p. 475): Credit Risk Model Validation Framework → conceptual soundness, outcome analysis and implementation verification as the validation triad.
- Fig. 8 (p. 477): Explainable AI in Credit Risk → the spectrum from post-hoc attribution methods to inherently interpretable models.
- Fig. 9 (p. 480): AI Model Risk Governance Framework → the three-lines-of-defence and lifecycle governance structure for AI credit models.
- Fig. 10 (p. 482): PRISMA Review of AI Credit Risk → the 298 → 226 → 83 → 27 screening flow.
- Fig. 11 (p. 483): AI Credit Risk Model Performance → the reported discrimination advantage of AI models over traditional baselines.
- Fig. 12 (p. 486): AI Credit Risk Comparative Analysis → comparison of pre-2018 and 2018–2026 evidence on performance, explainability, drift and fairness.
- The paper contains no numbered results tables; all quantitative content in the Findings is reported in running prose and in Figures 10–12.

## Definitions

- **Credit risk** — the probability that a borrower or counterparty will fail to meet contractual debt obligations in full and on time, generating loss through write-offs, recovery costs and reduced earnings (Introduction, p. 460).
- **PD / LGD / EAD** — probability of default, loss given default and exposure at default, the measurable components through which credit risk is operationalised and used to compute expected credit loss under IFRS 9 (Introduction, p. 460).
- **AI-driven credit risk assessment model** — in empirical research, a model narrowed to measurable tasks such as binary default classification, ordinal credit rating assignment or continuous loss estimation, evaluated with standardised metrics such as AUC, F1 and calibration error (Introduction, p. 460).
- **Model Risk Management (MRM)** — the lifecycle-oriented governance structure through which models are developed, validated, approved, monitored and retired, associated in the paper with SR 11-7 and the three-lines-of-defence architecture (Model Risk Management for AI Credit Risk, p. 478).
- **Data drift** — changes in the input-feature distribution (Post-deployment monitoring, p. 480).
- **Concept drift** — changes in the relationship between features and default outcomes; the paper reports it as posing greater regulatory concern than data drift because it undermines PD calibration, risk segmentation and expected-loss estimates (Post-deployment monitoring, p. 480).
- **Champion–challenger framework** — the productionisation pattern in which incumbent logistic or scorecard models serve as the champion while ML systems operate in parallel as challengers, producing comparative evidence on discrimination, stability and calibration (Implementation and Future Research Agenda, p. 479).
- **WOE binning** — Weight of Evidence discretisation used in scorecard transformations for interpretability and stability under regulatory-aligned modelling (Data Foundations and Feature Engineering, p. 471).
- **CCF** — credit conversion factor, described as a central modelling object for exposure at default in revolving credit and undrawn commitments (PD/LGD/EAD, Stress Testing, and Early Warning, p. 473).
- **PIT versus TTC PD** — point-in-time designs embed contemporaneous conditions and borrower signals, while through-the-cycle designs smooth cyclical variation to represent long-run creditworthiness and align with rating stability (PD/LGD/EAD, Stress Testing, and Early Warning, p. 472).

## Limitations and Gaps

- The authors acknowledge that the review relies on 27 eligible studies but that the underlying research landscape is constrained by limited access to high-quality, multi-bank and cross-jurisdiction datasets, so most included studies draw on single-institution or region-specific data, restricting external validity (LIMITATION, p. 488).
- The authors acknowledge that heterogeneity across studies — dataset size, feature construction, model architectures, evaluation metrics and validation protocols — limits quantitative synthesis or meta-analysis and requires qualitative integration instead (LIMITATION, p. 488).
- The authors acknowledge publication bias: research demonstrating strong AI performance is more likely to be published than studies reporting negative or inconclusive outcomes, potentially inflating perceptions of AI effectiveness (LIMITATION, p. 488).
- The authors acknowledge that included studies vary widely in methodological rigour, especially in drift management, fairness evaluation and explainability testing, making fully consistent conclusions difficult (LIMITATION, p. 488).
- The authors acknowledge that the evolving regulatory landscape adds complexity, since several included studies predate recent AI governance frameworks and therefore do not align with current supervisory expectations (LIMITATION, p. 488).
- The authors acknowledge that the rapid pace of AI advancement means findings may become outdated quickly as new architectures, privacy-preserving techniques and regulatory standards emerge (LIMITATION, p. 488).
- The review does not perform a meta-analysis, so no pooled effect size, confidence interval or p-value is produced for any outcome; every quantitative result in the Findings is a count of studies or a range reported across studies (Methods, p. 482; Findings, pp. 482-485).
- [unacknowledged] The 27 included primary studies are never enumerated in a table, appendix or numbered list, so the reader cannot trace any theme count back to a specific study or reconcile the theme-level counts with each other.
- [unacknowledged] The Findings report theme-level citation volumes of more than 1,240, over 980, more than 1,150, more than 760 and more than 1,300 external citations; the paper does not explain how these relate to a single corpus total, and their sum far exceeds any single reported figure (Findings, pp. 482-485).
- [unacknowledged] The Discussion opens with a paragraph that is repeated verbatim in full — "The findings of this systematic review demonstrate that AI-driven credit risk assessment models between 2018 and 2026 consistently outperformed traditional statistical baselines, particularly logistic regression and classical scorecard systems." — appearing twice in immediate succession (Discussion, p. 485).
- [unacknowledged] No per-study AUC, PR-AUC, KS, Brier score, calibration curve or confidence interval is reported for any of the 27 studies, even though the Methods state that studies lacking such recognised risk metrics were excluded at full-text stage (Methods, pp. 481-482; Findings, pp. 482-485).
- [unacknowledged] The reported "AUC gains ranging from 4% to 17%" is given as a range over nine studies with no distributional detail, no per-study values, no confidence interval and no significance test (Findings, p. 483).
- [unacknowledged] The review provides no geographic breakdown of the 27 included studies, no publication-year breakdown, and no journal or venue breakdown, so the composition of the evidence base cannot be assessed (Methods, pp. 481-482).
- [unacknowledged] The review offers no assessment of its own screening reliability beyond stating that two independent reviewers extracted data and resolved disagreements by consensus; no inter-rater agreement statistic is reported (Methods, p. 482).
- [unacknowledged] Because the review is a documentary synthesis, it carries no primary dataset, no participant sample and no primary experimental design, so no claim in it can be independently re-tested from the paper's own materials.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Studies identified by the initial database search | count | 298 | — | — | Methods, p. 481 |
| Unique studies remaining after duplicate screening | count | 226 | — | — | Methods, p. 481 |
| Studies excluded at title and abstract screening | count | 143 | — | — | Methods, p. 481 |
| Articles eligible for full-text review | count | 83 | — | — | Methods, p. 481 |
| Studies retained in the final synthesis dataset | count | 27 | — | — | Methods, p. 482 |
| External citations referenced across the reviewed studies, model-diversification theme | citations | more than 1,240 | — | — | Findings, p. 482 |
| Reviewed studies directly comparing AI models with logistic regression scorecards | count | 12 | — | — | Findings, p. 483 |
| Reviewed studies reporting AUC gains | count | 9 | — | — | Findings, p. 483 |
| Reported AUC gain from AI models over logistic regression scorecards | AUC gain | 4% to 17% | — | — | Findings, p. 483 |
| Reviewed studies incorporating temporal, behavioral or transactional features | count | at least seven | — | — | Findings, p. 483 |
| Articles reporting actual real-world deployment of AI models in production-grade lending environments | count | 4 | — | — | Findings, p. 483 |
| External citations across the data quality, feature engineering and generalizability theme | citations | over 980 | — | — | Findings, p. 483 |
| Articles noting missing data, sparse variables or inconsistent reporting restricted model accuracy | count | 17 | — | — | Findings, p. 483 |
| Studies emphasizing the importance of domain-informed feature engineering | count | 11 | — | — | Findings, p. 483 |
| Studies explicitly testing models across multiple borrower segments or economic conditions | count | 19 | — | — | Findings, p. 483 |
| Studies reporting substantial degradation in predictive accuracy on transfer to different geographies, product types or macroeconomic environments | count | 14 | — | — | Findings, p. 483 |
| Articles using multi-bank datasets | count | 5 | — | — | Findings, p. 484 |
| Multi-bank studies highlighting inconsistencies in variable definitions, data collection processes and loan lifecycle structures | count | 3 | — | — | Findings, p. 484 |
| Studies highlighting explainability, transparency and governance challenges | count | 22 | — | — | Findings, p. 484 |
| External citations across the explainability, transparency and governance theme | citations | more than 1,150 | — | — | Findings, p. 484 |
| Studies stressing that banks must justify lending decisions to auditors, regulators and consumers | count | 19 | — | — | Findings, p. 484 |
| Studies observing that model risk management teams had difficulty validating neural network and ensemble models | count | 14 | — | — | Findings, p. 484 |
| Articles highlighting operational challenges in generating stable reason codes for customer disclosures | count | 11 | — | — | Findings, p. 484 |
| Studies warning that models lacking interpretability were vulnerable to embedded bias and discriminatory outcomes | count | 10 | — | — | Findings, p. 484 |
| External citations across the post-deployment monitoring theme | citations | more than 760 | — | — | Findings, p. 484 |
| Studies reporting that performance degradation emerged rapidly when borrower behaviour, macroeconomic conditions or underwriting strategies shifted | count | 16 | — | — | Findings, p. 484 |
| Studies emphasizing that concept drift posed more serious risks than data drift | count | 11 | — | — | Findings, p. 484 |
| Studies reporting reduced score-to-PD alignment within 12–18 months of deployment | count | 9 | — | — | Findings, p. 484 |
| Studies providing detailed post-deployment frameworks used in operational bank environments | count | 5 | — | — | Findings, p. 484 |
| Studies observing that initially fair models could become biased over time | count | 7 | — | — | Findings, p. 484 |
| External citations across the strategic research gaps theme | citations | more than 1,300 | — | — | Findings, pp. 484-485 |
| Studies noting the absence of high-quality, cross-bank datasets | count | 18 | — | — | Findings, p. 485 |
| Studies emphasizing tensions between performance and transparency | count | 13 | — | — | Findings, p. 485 |
| Studies highlighting a lack of stress-testing readiness in AI models | count | 11 | — | — | Findings, p. 485 |
| Studies noting that AI models captured correlations rather than structural cause–effect relationships | count | 9 | — | — | Findings, p. 485 |
| Studies discussing privacy-preserving learning approaches such as federated learning or secure computation | count | 6 | — | — | Findings, p. 485 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "Following the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines, the review synthesizes evidence from 27 peer-reviewed studies" | Abstract, p. 459 | data_collection |
| "The search strategy identified 298 potentially relevant studies, reflecting the rapid expansion of AI-focused credit risk research in recent years." | Methods, p. 481 | data_collection |
| "After applying the full-text eligibility criteria, 27 studies remained and formed the final dataset for data extraction and synthesis." | Methods, p. 482 | data_collection |
| "The review showed that AI models consistently outperformed traditional statistical models in predictive discrimination, particularly in Probability of Default estimation" | Findings, pp. 482-483 | model_performance_evaluation |
| "Twelve of the reviewed studies directly compared AI models with logistic regression scorecards, and nine reported AUC gains ranging from 4% to 17%" | Findings, p. 483 | model_performance_evaluation |
| "Among the 27 included studies, 19 explicitly tested models across multiple borrower segments or economic conditions, and 14 reported substantial degradation in predictive accuracy when models were transferred" | Findings, p. 483 | model_performance_evaluation |
| "only four articles reported actual real-world deployment of AI models in production-grade lending environments" | Findings, p. 483 | model_algorithm_integration |
| "The review found that while AI models offered superior predictive accuracy, they also introduced substantial governance burdens due to their opacity" | Findings, p. 484 | model_algorithm_integration |
| "Eleven studies emphasized that concept drift—changes in the underlying relationship between predictors and default outcomes—posed more serious risks than data drift" | Findings, p. 484 | model_performance_evaluation |
| "Ultimately, although AI models demonstrated strong in-sample performance, the findings indicated that generalizability challenges formed a major barrier to sustainable, scalable deployment." | Findings, p. 484 | model_performance_evaluation |
| "Another limitation arises from publication bias, as research demonstrating strong AI performance is more likely to be published than studies reporting negative or inconclusive outcomes" | LIMITATION, p. 488 | model_performance_evaluation |
| "AI has matured into a highly promising but still incompletely integrated component of commercial banking risk management" | Conclusion, p. 487 | model_algorithm_integration |

## Remember This

- Sarkar (2026) is a PRISMA systematic review of 27 peer-reviewed studies on AI-driven credit risk assessment in commercial banking, 2018–2026, not a primary empirical study.
- The screening flow is 298 identified → 226 unique → 143 excluded → 83 full text → 27 included; no meta-analysis was performed and no pooled effect size is reported.
- The review's headline quantitative claims are counts of studies and one range: nine studies reported AUC gains from 4% to 17% over logistic regression scorecards, and only four articles documented production deployment.
- The review's dominant constraints are data quality and generalizability (14 of 27 studies reported degradation on transfer; 18 noted the absence of cross-bank datasets), explainability and governance (22 of 27 studies), and post-deployment drift (16 studies reporting rapid degradation; nine reporting reduced score-to-PD alignment within 12–18 months).
- No confidence interval and no p-value appears anywhere in the paper; every CI and p cell in the evidence table is `—`.
- The Discussion repeats its opening paragraph verbatim, and the Findings report theme-level citation counts that are not reconciled with one another — both `[unacknowledged]` in this extraction.
- The review supplies no enumeration of the 27 included studies, no per-study metrics and no geographic or publication-year breakdown of its evidence base.