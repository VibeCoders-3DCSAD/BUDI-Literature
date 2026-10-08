---
paper_id: A--Abdullahi-2025
first_author: Abdullahi
year: 2025
title: "A Systematic Literature Review of Concept Drift Mitigation in Time-Series Applications"
venue: "IEEE Access"
doi: 10.1109/ACCESS.2025.3587231
designation: algorithm
status: extracted
modules: [sarima, model_algorithm_integration, model_performance_evaluation]
module_rationale:
  sarima: "the review surveys time-series forecasting learners and their degradation under nonstationary data, including seasonal variation as a drift signal and forecasting error metrics (Sect. IV-A, p. 119389; Sect. VI-B-2, p. 119398)"
  model_algorithm_integration: "the review's findings chapters compare ensemble, hybrid and roadmap-style combinations of drift detectors and learners, and set out a five-step drift-handling pipeline (Sect. V-A, p. 119392; Sect. V-D, pp. 119396-119397)"
  model_performance_evaluation: "the taxonomy and evaluation sections are organised around detection and forecasting metrics — accuracy, precision, recall, F1, RMSE, MSE, MAE, AUC — with printed equations and a per-study metric-and-dataset table (Sect. VI-B-2, p. 119398; Table 12, p. 119404)"
---

## Summary

This is a Systematic Literature Review (SLR) of how Concept Drift (CD) is detected and adapted in time-series applications, covering both classification and regression learning tasks. The authors follow the PRISMA 2020 statement and the Kitchenham and Charters review guidelines, search six databases (SCOPUS, ScienceDirect, IEEE Xplore, Web of Science, MDPI and ACM), and narrow the pool to 60 studies published between 2013 and 2024. Four research questions organise the review: which ensemble-based learning methods are most effective for detecting CD in time-series data under classification and regression (RQ1); which machine learning models are used in a general context and how actionable they are for drift detection and adaptation (RQ2); which algorithms have been used over the last decades to analyse and handle CD in time-series data and data streams (RQ3); and what the main steps are for addressing CD problems, specifically in time-series data and in the general context (RQ4).

The review reports that ensemble-based learning — ENSDS, a support vector regression ensemble, ELM, OS-ELM, DEMSC and DES — is the most commonly used detection family for time-series data (Sect. V-A, p. 119392), that SVM, k-NN and LSTM are the most widely used learners for drift detection (Sect. V-B, p. 119395), and that ADWIN, HDDM and DDM are the most frequently applied drift-handling techniques (Sect. IV-B-3, p. 119391). The abstract states that Support Vector Machines are the most effective learning algorithms for detection and adaptation in regression and classification tasks using time-series data, attributing this to high detection accuracy and effective memory (Abstract, p. 119380).

The paper contributes a taxonomy that maps AI-based learners onto incremental, gradual, sudden and recurrent drift (Sect. VI-A, pp. 119398-119399), an experimental-evaluation scheme that separates classification metrics from regression metrics and lists prequential, holdout and cross-validation procedures (Sect. VI-B, pp. 119398-119399), a comparative analysis of the proposed roadmap against baseline detectors on detection capability, adaptability and scalability (Sect. VI-C, p. 119400), and twelve figures summarising lessons learned and best practices (Fig. 12, p. 119401). Sixty per cent of the selected studies addressed classification, against six per cent for regression — the imbalance the review is built around (Fig. 7, p. 119389). The paper is a documentary synthesis only; it reports no experiments of its own and no primary outcome data.

## Problem and Motivation

- Concept drift changes the relationship between input data and model target values and continuously alters the statistical properties of a dataset over time, degrading machine learning performance particularly after deployment (Sect. I, p. 119381).
- Time-series forecasting is complicated because the effectiveness of models trained on historical data can decrease over time as the underlying data-generating process changes (Sect. II, p. 119382).
- Previous studies on CD detection and adaptation have limitations: they have primarily focused on classification learning, with minimal attention paid to regression learning tasks (Sect. I, p. 119381).
- Several issues remain in the efficient identification of changes in data distribution features and in responses to CD in a time-series context (Sect. I, p. 119381).
- The evaluation metric performance for validating CD in ML models using benchmark datasets may not accurately reflect real-world industrial data, and determining an appropriate CD detection technique for various datasets is challenging (Sect. I, p. 119381).
- Existing reviews cover performance-based detectors (Bayram et al.), unsupervised detectors (Shen et al.), nonstationary data streams (Han et al.), unsupervised classification (Gemaque et al.), ensembles and windowing (Nayak et al.), detector alarm reliability (Poenaru-Olaru et al.), domain adaptation (Karimian and Beigy) and adaptive learning (Gama et al.), but the authors position their SLR as one of the first to cover regression and classification together in time-series applications (Sect. II, pp. 119382-119383; Sect. I, p. 119381).

## Method

**Design.** Systematic Literature Review following the PRISMA 2020 statement and the Kitchenham and Charters guidelines; the authors label the study a Systematic Literature Review (SLR).
**Sample.** n = 60 primary studies published 2013–2024, the unit of analysis being one selected journal article or conference paper; the six-database search yielded 183 unique papers before screening.
**Context.** geography: Not reported (the search was conducted worldwide and is not restricted to a single nation or area; author affiliations are in Malaysia and Libya); population: Not applicable — the review analyses publications rather than human participants; setting: desk-based documentary review using Microsoft Excel (version 16.77) for data extraction; no field, laboratory, deployment or participant component.

The review proceeds through four stages. Stage 1 is a preliminary study that identifies keywords, formulates the research questions and fixes the search criteria; the search terms combine 'Concept Drift' OR 'CD' with 'Model Degradation', 'Drift Handling' OR 'Drift Detector', 'Concept Evaluation', 'Time-Series' OR 'Time-Series Data', 'Artificial Intelligence' OR 'AI', 'Machine Learning' OR 'ML', 'Regression' and 'Classification' (Sect. III-A, pp. 119384-119385). A preliminary Google Scholar search was reduced to 5,850 records after filtering, and synonyms for 'Concept Drift' were taken from Lima et al. (Sect. III-A-1, p. 119385). Only journal articles published in English between 2013 and 2024 were included.

Stage 2 is the screening process. The six-database search yielded 183 unique papers, screened by two authors (S.J.A. and N.A.); after excluding 123 articles, 60 research articles were selected (Sect. III-B, p. 119385). Inclusion and exclusion criteria covered subject fields (mathematics, computer science, engineering, decision science), the publication window and language (Table 3, p. 119385).

Stage 3 is eligibility and quality assessment. After screening, 60 papers were evaluated; eight articles written in languages other than English were excluded, and the assessment used scoring values of 1 for "Yes", 0.5 for "Partially" and 0 for "No" (Sect. III-C, p. 119386; Table 4, p. 119387). Studies scoring 1 or 0.5 were carried into data extraction.

Stage 4 is data extraction and compilation, conducted by two authors (S.J.A. and N.A.) in Microsoft Excel version 16.77. Extracted fields were authors, title, abstract, volume, number, pages, publisher, keywords, year, datasets, CD algorithm, evaluation metrics, problem scope and algorithm learning, plus publication year, algorithm used, metrics evaluation, domain and ML technique (Sect. III-D, p. 119387).

The review answers four research questions (Table 2, p. 119385). For RQ1, ensemble-based learners are examined; the named methods are ENSDS, an SVR-based ensemble with streaming data points, ELM with explicit drift detection, OS-ELM ensembles, DEMSC and DES (Sect. V-A, pp. 119392-119394). For RQ2, supervised, unsupervised and deep learners are examined, including incremental SVM with domain adaptation, an SVM plus k-means hybrid for network anomaly detection, an autoencoder-based concept drift detector (AECDD), a least-squares support vector classifier with particle adaptive classifier, LSTM-based learners and the selective ensemble-based online adaptive (SEOA) deep network (Sect. V-B, pp. 119395-119396). For RQ3, the algorithms catalogued are DDM, ECDD, ADWIN, MDDT, UTDD, NDE and FHDDM (Sect. V-C, pp. 119395-119396; Table 11, p. 119397). For RQ4, the review states a five-step pipeline — nature of data, concept drift detection, concept drift characterization, model adaptation, and evaluation and validation — separately for the general context and for time-series data (Sect. V-D, pp. 119396-119397).

## Key Findings

- The review reports that ensemble-based learning with classification and regression approaches based on ENSDS, SVR, ELM, OS-ELM, DEMSC and DES were the most commonly used methods for detecting CD in a time-series environment (Sect. V-A, p. 119394).
- SVM, k-NN and LSTM are reported as the most widely used ML models for CD detection because of their efficacy in drift detection, with SVM and k-NN described as robust against feature-based changes and LSTM as capturing temporal dependencies (Sect. V-B, p. 119395).
- Most previous studies used the ADWIN, HDDM and DDM techniques to overcome drift problems, and the drift types commonly discussed are real, incremental, gradual, sudden and recurrent drift (Sect. IV-B-3, p. 119391).
- The review's summary of the selected corpus states that most studies focused on classification tasks (60%), followed by time-series (12%), supervised (7%), imbalance (7%), unsupervised (6%), regression (6%) and semi-supervised (2%) (Fig. 7, p. 119389).
- Most studies employed accuracy as the primary measure to evaluate their models, while other studies used a range of alternative metrics including AUC, AUROC, AVF, CBA, confusion matrix, F1, G-Mean, MAE, MAPE, MASE, MCC, MED, MSE, NRMSD, precision, RCA, recall, RMSE and ROC (Fig. 8, p. 119389; Sect. IV-A, p. 119389).
- The distribution of studies by source gives 46 journal publications and 14 conference proceedings, with the highest journal counts in Expert Systems with Applications (five) and Information Sciences (four) (Sect. IV-A, pp. 119387-119388).
- The number of published papers increased over time, with a particularly significant increase from 2021 to 2022 and the highest number of publications occurring in 2022 (Sect. IV-A, p. 119387).
- The comparative analysis claims the proposed roadmap's use of SVM, GBN, NN and XGBoost has advantages over baseline detectors DDM, EDDM, ADWIN, DW_HDDM and WSTD in detection capability, adaptability and flexibility, and performance and scalability, while baseline techniques are described as computationally efficient and simple to implement (Sect. VI-C, p. 119400).
- The review found that some studies used real-world datasets, others used synthetic datasets, and others a combination of both, and it lists clinical sepsis records, network traffic, Intel Berkeley Research Lab temperature data, NTUST_EE_Lobby, changing-sine sudden and incremental synthetic data, industrial clean and credit data, and the Australian New South Wales electricity market data among the sources (Sect. VII, p. 119401).
- Recommended future directions are adaptive learning models that respond to CD without explicit re-training, unsupervised and semi-supervised drift detection that uses less labelled data, causal representation learning to separate correlation from causation, hybrid detection methods, and deep learning over multimodal sources (Sect. IX, pp. 119404-119405).

## Key Figures and Tables

- Fig. 1 (p. 119382): Concept drift types based on speed [14] → CD is classed as incremental, gradual, sudden or recurring, with incremental involving minimal change and sudden involving a significant change at a specific time point.
- Fig. 2 (p. 119384): Systematic literature review mapping process → the survey methodology section is organised into four stages in the screening process.
- Fig. 3 (p. 119384): Google Scholar keyword combination results → the preliminary keyword combinations produce an initial output later reduced to 5,850 records after filtering.
- Fig. 4 (p. 119386): PRISMA 2020 flow diagram of study screening and selection → the flow runs from database search to the 60 included studies.
- Fig. 5 (p. 119387): Distribution of studies by publication year → publications increase over 2013–2024, with the highest number in 2022.
- Fig. 6 (p. 119388): Distribution of studies by journals → N = 46 journal articles and N = 14 conference proceedings.
- Fig. 7 (p. 119389): Characteristics of studies based on the problem scope of machine learning → classification 60%, time-series 12%, supervised 7%, imbalance 7%, unsupervised 6%, regression 6%, semi-supervised 2%.
- Fig. 8 (p. 119389): Characteristics of studies based on evaluation metrics → accuracy dominates, with a long tail of classification and regression metrics.
- Fig. 9 (p. 119389): Characteristics of studies using learning algorithms → the surveyed algorithm set spans ANN, autoencoder, CNN, DNN, DT, FCN, GNB, GRU, k-NN, LR, LSTM, MLP, NB, NN, PNN, RF, RGF, RNN, SVM, XGBoost and YOLO.
- Fig. 10 (p. 119395): Ensemble-based learners for concept drift detection in time-series data → the ensemble family is mapped across the surveyed techniques.
- Fig. 11 (p. 119399): Illustration of AI learners for concept drift detection → learners are grouped by the four drift speeds, with SVM, GNB and MLP for incremental drift, k-NN, SVM and NN for gradual drift, XGBoost, RNN, GBN and MLP for sudden drift, and DLSTM, LSTM, OAR and RF for recurrent drift.
- Fig. 12 (p. 119401): Lessons learned and best practices for concept drift mitigation in time-series applications → the summary spans computational cost and efficiency, window size selection, handling different drift types, drift versus noise, ensemble diversity, experimental evaluation, system architecture, and real-world versus synthetic data.
- Table 1 (p. 119383): Comparison with other studies in the same domain → positions this SLR against prior surveys and reviews.
- Table 2 (p. 119385): Formulated research questions and motivation → lists the four RQs and why each is asked.
- Table 3 (p. 119385): Inclusion and exclusion criteria → the filters applied during screening.
- Table 4 (p. 119387): Eligibility and quality assessment scoring criteria → Yes = 1, Partially = 0.5, No = 0.
- Table 5 (p. 119390): Studies categorized based on classification learning algorithms → datasets, work descriptions, publication years and algorithm learners.
- Table 6 (p. 119391): Studies categorized based on regression learning algorithms → datasets, work descriptions, publication years and regression learners.
- Table 7 (p. 119391): Studies categorized by model performance for CD detection and adaptation in a general context → the metrics used to evidence drift and adaptation.
- Table 8 (p. 119393): Studies categorized based on a technique that handles concept drift → techniques mapped to drift types, with ADWIN, HDDM and DDM the most used.
- Table 9 (p. 119394): Summary of ensemble-based learning concept drift detection techniques → the ensemble methods catalogued for RQ1.
- Table 10 (p. 119397): Summary of machine learning techniques for detecting concept drift in a general context → supervised, unsupervised and deep learners for RQ2.
- Table 11 (p. 119397): Summary of algorithms used in the past decade to handle concept drift → DDM, ECDD, ADWIN, MDDT, UTDD, NDE and FHDDM among others.
- Table 12 (p. 119404): Summary of the evaluation metrics and datasets for CD detection from the selected studies → pairs each selected study with its metrics and datasets.
- Table 13 (p. 119404): Summary of state-of-the-art studies and their contributions, strengths and weaknesses → the review's own synthesis of each surveyed work.
- Table 14 (p. 119406): PRISMA 2020 checklist → sections, numbers and placements in the publication.

## Software

- Microsoft Excel (version 16.77) — used by two authors for data extraction and compilation of the 60 selected studies (Sect. III-D, p. 119387).
- No modelling, simulation or analysis software is reported; the paper contains no experiments of its own.

## Definitions

- **Concept Drift (CD)** — a change in the relationship between input data and model target values; it continuously changes the statistical properties of a dataset over time (Sect. I, p. 119381).
- **Incremental CD** — a minimal and continuous change in the original data distribution and in the relationship between features and target variables (Sect. VI-A-1, p. 119398).
- **Gradual CD** — a gradual and noticeable change in the target data distribution, with long-term effects that allow earlier detection than incremental drift (Sect. VI-A-2, p. 119398).
- **Sudden CD** — an abrupt and significant change in the original data distribution at a particular time point and in the relationship between features and target variables (Sect. VI-A-3, p. 119398).
- **Recurrent CD** — a situation in which an old concept reappears after a period of absence (Sect. VI-A-4, p. 119398).
- **Dataset shift** — any change in the joint distribution of input and target variables between the training and testing stages; unlike CD it does not always imply time evolution (Sect. I-A, p. 119381).
- **ADWIN (Adaptive Windowing)** — a detector that dynamically adjusts the window size based on variations in the observed data, decreasing the window when the statistical difference between sub-windows exceeds a specified confidence level (Sect. VIII-B, p. 119402).
- **DDM (Drift Detection Method)** — a drift detector used to detect CD in financial time-series predictions (Sect. V-D-2, p. 119396).
- **EDDM (Early Drift Detection Method)** — a detector that uses statistical distance measures to detect gradual drifts by tracking slow changes (Sect. IV-B-3, p. 119391).
- **HDDM (Hoeffding Drift Detection Method)** — a detector based on Hoeffding bounds that also uses statistical distance measures for gradual drift (Sect. IV-B-3, p. 119391).
- **FHDDM (Fast Hoeffding Drift Detection Method)** — a sliding-window and Hoeffding-inequality method reported to have lower detection delay, fewer false positives and fewer false negatives (Sect. V-C, p. 119396).
- **CUSUM and EWMA** — techniques that use cumulative changes or weighted averages to facilitate rapid identification of incremental drifts (Sect. IV-B-3, p. 119391).
- **AECDD** — autoencoder-based concept drift detector, an unsupervised, reconstruction-based drift detection model for multivariate streaming data (Sect. V-B, p. 119395).
- **SEOA** — selective ensemble-based online adaptive deep neural network that adjusts information flow in response to nearby data variations (Sect. V-B, p. 119395).
- **MDDT** — multiscale drift detection test, designed to filter noise present in drift indicators and to handle abrupt shifts (Sect. V-C, p. 119395; Sect. VIII-D, p. 119402).
- **Prequential evaluation** — constant updating and testing of the model as new data arrives, with each new data point used to test the model followed by training (Sect. VI-B-3, p. 119399).
- **TML-CD** — Tiny Machine Learning for concept drift, an on-device adaptation solution operating under stringent memory and energy constraints (Sect. VIII-A, p. 119402).

## Key Equations

- `Accuracy = (TP + TN) / (TP + TN + FP + FN)` — proportion of correctly identified instances, both drift and no drift, among the total (Eq. 1, p. 119399).
- `Precision = TP / (TP + FP)` — positive predictive value, the proportion of detected drift that is actual drift (Eq. 2, p. 119399).
- `Recall = TP / (TP + FN)` — the proportion of actual drift detected by the model (Eq. 3, p. 119399).
- `F1 = (2 × Precision × Recall) / (Prescision + Recall)` — balance between precision and recall, printed with the misspelling "Prescision" in the denominator (Eq. 4, p. 119399).
- `RMSE = sqrt((1/n) Σ (ŷᵢ − yᵢ)²)` — square root of the average squared difference between predicted and actual values (Eq. 5, p. 119399).
- `MSE = (1/n) Σ (ŷᵢ − yᵢ)²` — average of the squared differences between predicted and actual values (Eq. 6, p. 119399).
- `MAE = (1/n) Σ |ŷᵢ − yᵢ|` — absolute difference between predicted and actual values (Eq. 7, p. 119399).
- AUC is described in words rather than as an equation: it measures the ability of the model to distinguish between drift and no-drift cases across different threshold settings (Sect. VI-B-2, p. 119399).

## Limitations and Gaps

- The authors acknowledge that the review analysed 60 research articles selected from multiple databases (SCOPUS, Science Direct, IEEE Xplore, Web of Science, MDPI and ACM), and that because the search criteria focused on journal papers published between 2013 and 2024, some relevant studies were excluded (Sect. IX, p. 119403).
- The authors acknowledge that studies conducted in languages other than English were excluded (Sect. IX, p. 119403).
- The authors acknowledge that reliance on simulation datasets may not fully capture real-world scenarios, and that several studies tested their proposed method on a single dataset, which may limit generalizability (Sect. IX, p. 119403).
- The authors acknowledge that comparisons with active approaches from state-of-the-art studies are limited, and that the study was unable to investigate other approaches to CD detection such as similarity and dissimilarity-based methods using time-series data (Sect. IX, p. 119403).
- The authors state that most of the currently proposed drift detection, handling and adaptation methods have not been solved (Sect. IX, p. 119403).
- [unacknowledged] The paper reports no primary outcome statistics of its own: the results section reports counts of studies, percentages of corpus characteristics and a search-flow account, and the only performance claims (for example, that SVM is most effective) are synthesised from other papers without a pooled effect size, a benchmark table or a numerical comparison across studies.
- [unacknowledged] The abstract's claim that SVM is "the most effective learning algorithms" is grounded in frequency of use and qualitative statements about high detection accuracy and effective memory rather than in an extracted, comparable metric, so the ranking cannot be verified from the evidence presented (Abstract, p. 119380; Sect. IV-A, p. 119390).
- [unacknowledged] The quality-assessment outcome is reported as a scoring rubric only; no per-study score, score distribution, or list of studies excluded on quality grounds is printed, so the quality filter cannot be reconstructed (Sect. III-C, p. 119386; Table 4, p. 119387).
- [unacknowledged] The review's own quantitative synthesis is confined to descriptive counts (publication year, journal, problem scope, metric, algorithm), and no meta-analysis, subgroup analysis or publication-bias assessment is reported.
- [unacknowledged] Search-flow numbers are stated at different stages without reconciling them: a Google Scholar preliminary search reduced to 5,850 records (Sect. III-A-1, p. 119385) versus 183 unique papers from the six-database search, of which 123 were excluded to leave 60 (Sect. III-B, p. 119385). The relationship between the 5,850 and the 183 is not explained.
- [unacknowledged] The paper states that "This SLR consists of eight sections" while enumerating nine numbered sections, I through IX (Sect. I, p. 119382), and the section describing conclusions is listed as Section IX.
- [unacknowledged] The inclusion window is described inconsistently: the review states that the search encompassed the period from 2013 to 2024 "except for articles published earlier in 2012", while older works from 2007, 2009 and 2012 are discussed in the related-reviews section (Sect. III-B-1, p. 119385; Sect. II, p. 119383).
- [unacknowledged] No inter-rater agreement statistic is reported for the two-author screening, eligibility and extraction steps, and no protocol registration is reported.
- [unacknowledged] Tables 5 to 11 are narrative catalogue tables of other authors' work; the extraction here cannot recover per-study values from them because the conversion renders them as prose summaries, so no per-study metric can be entered in Statistical Evidence.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Preliminary Google Scholar search output after quality filtering | records | 5,850 | — | — | Sect. III-A-1, p. 119385 |
| Records yielded by the six-database search | unique papers | 183 | — | — | Sect. III-B, p. 119385 |
| Articles excluded during screening | articles | 123 | — | — | Sect. III-B-1, p. 119385 |
| Research articles selected after screening | studies | 60 | — | — | Sect. III-B-1, p. 119385 |
| Non-English articles excluded | articles | 8 | — | — | Sect. III-C, p. 119386 |
| Papers evaluated for eligibility and quality after screening | studies | 60 | — | — | Sect. III-C, p. 119386 |
| Quality assessment scoring, "Yes" | score | 1 | — | — | Sect. III-C, p. 119386; Table 4, p. 119387 |
| Quality assessment scoring, "Partially" | score | 0.5 | — | — | Sect. III-C, p. 119386; Table 4, p. 119387 |
| Quality assessment scoring, "No" | score | 0 | — | — | Sect. III-C, p. 119386; Table 4, p. 119387 |
| Journal publications in the selected corpus | studies | N = 46 | — | — | Sect. IV-A, p. 119387 |
| Conference proceedings in the selected corpus | studies | N = 14 | — | — | Sect. IV-A, p. 119387 |
| Publications in Expert Systems with Applications | studies | 5 | — | — | Sect. IV-A, p. 119388 |
| Publications in Information Sciences | studies | 4 | — | — | Sect. IV-A, p. 119388 |
| Problem scope of the selected studies, classification | share of studies | 60% | — | — | Sect. IV-A, Fig. 7, p. 119389 |
| Problem scope of the selected studies, time-series | share of studies | 12% | — | — | Sect. IV-A, Fig. 7, p. 119389 |
| Problem scope of the selected studies, supervised | share of studies | 7% | — | — | Sect. IV-A, Fig. 7, p. 119389 |
| Problem scope of the selected studies, imbalance | share of studies | 7% | — | — | Sect. IV-A, Fig. 7, p. 119389 |
| Problem scope of the selected studies, unsupervised | share of studies | 6% | — | — | Sect. IV-A, Fig. 7, p. 119389 |
| Problem scope of the selected studies, regression | share of studies | 6% | — | — | Sect. IV-A, Fig. 7, p. 119389 |
| Problem scope of the selected studies, semi-supervised | share of studies | 2% | — | — | Sect. IV-A, Fig. 7, p. 119389 |
| Synthetic benchmark series generated to demonstrate CD | artificial time-series | 3 | — | — | Sect. I, p. 119381 |
| Synthetic benchmark series length | instances per series | 20,000 | — | — | Sect. I, p. 119381 |
| Synthetic benchmark drift onset | instance index | 10,001 | — | — | Sect. I, p. 119381 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "Machine Learning (ML) plays a key role in time-series applications because it analyzes observed data and predicts future values." | Abstract, p. 119380 | sarima |
| "CD refers to continuous changes in the statistical properties of datasets. This affects the predictive performance of ML models." | Abstract, p. 119380 | model_performance_evaluation |
| "This is possible because of their high detection accuracy and effective memory." | Abstract, p. 119380 | model_performance_evaluation |
| "Most studies focused on classification tasks (60%), followed by time-series (12%), supervised (7%), imbalance (7%), unsupervised (6%), regression (6%), and semi-supervised (2%)." | Sect. IV-A, Fig. 7, p. 119389 | sarima |
| "The findings demonstrated that most studies employed accuracy as the primary measure to evaluate their models, whereas other studies concentrated on a range of alternative metrics to evaluate CD detection models." | Sect. IV-A, p. 119389 | model_performance_evaluation |
| "In addition, most studies have employed SVM and LSTM models for CD detection and adaptation because of their ability to handle dynamic data shifts." | Sect. IV-A, p. 119390 | model_performance_evaluation |
| "Performance metrics serve as tools for identifying and addressing CD proactively." | Sect. IV-B-2, p. 119391 | model_performance_evaluation |
| "Ensemble-based learning methods have emerged as promising solutions because of their inherent diversity and robustness." | Sect. V-A, p. 119392 | model_algorithm_integration |
| "SVM, k-NN, and LSTM have been widely used because of their efficacy in drift detection." | Sect. V-B, p. 119395 | model_performance_evaluation |
| "The basic steps for addressing CD are the same for both general contexts, with time-series data provided in Sections I and II." | Sect. V-D, p. 119396 | model_algorithm_integration |
| "The investigation revealed that some studies used real-world datasets, whereas others used synthetic datasets or a combination of both." | Sect. VII, p. 119401 | model_performance_evaluation |
| "Real-world data are extremely important for validating the robustness, practicality, and applicability of CD detection methods" | Sect. VIII-H, p. 119402 | model_performance_evaluation |
| "Differentiating between the actual CD and random fluctuations or outliers is a key challenge, as misidentification leads to excessive model updates and instability." | Sect. VIII-D, p. 119402 | model_algorithm_integration |
| "However, reliance on simulation datasets may not fully capture real-world scenarios." | Sect. IX, p. 119403 | model_performance_evaluation |
| "This SLR also confirms that using AI-based learners to detect, handle, and adapt to CD in time-series scenarios is a promising approach." | Sect. IX, p. 119403 | model_algorithm_integration |

## Remember This

- This is an SLR of 60 studies (2013–2024) on concept drift detection and adaptation in time-series applications, covering classification and regression; it is not an empirical study and reports no primary outcomes.
- PRISMA 2020 and Kitchenham and Charters guidelines were used; six databases were searched; 183 unique records were screened down to 60 included studies.
- The corpus is 46 journal articles and 14 conference papers; classification accounts for 60% of the problem scope and regression only 6%.
- The review's headline claim is that SVM is the most effective learning algorithm for detection and adaptation; the supporting evidence is frequency of use and qualitative statements, not a pooled comparison.
- Ensemble-based learning, SVM/k-NN/LSTM learners, and ADWIN/HDDM/DDM detectors are the three most frequently reported families.
- The paper's own contribution is a taxonomy, a five-step drift-handling pipeline, an evaluation-metric scheme with seven printed equations, and twelve lessons-learned figures.

## Cited Works

- Bayram, F.; Ahmed, B. S.; Kassler, A. (2022) (context) — Overview of performance-aware drift detectors, categorising performance-based detection methods and presenting them hierarchically. [p. 119382]
- Shen, P. K.; Ming, Y.; Li, H.; Gao, J.; Zhang, W. (2023) (context) — Survey of unsupervised concept drift detection with a taxonomy for real applications, but lacking empirical evaluation. [p. 119382]
- Han, M.; Chen, Z.; Li, M.; Wu, H.; Zhang, X. (2022) (context) — Survey of active and passive concept drift handling methods for nonstationary data streams. [p. 119382]
- Gemaque, R. N.; Costa, A. F. J.; Giusti, R.; Dos Santos, E. M. (2020) (context) — Overview of unsupervised drift detection methods with a taxonomy for unsupervised strategies. [p. 119382]
- Nayak, P. A. et al. (2021) (context) — Literature review of concept drift handling emphasising ensemble learning, adaptive windowing and weighting, without unsupervised or semi-supervised insight. [p. 119382]
- Poenaru-Olaru, L.; Cruz, L.; van Deursen, A.; Rellermeyer, J. S. (2022) (context) — Comparative study of drift detectors as alarming systems, examining timeliness of drift reports and false alarms. [p. 119382]
- Karimian, M.; Beigy, H. (2023) (methodology) — Concept Drift Domain Adaptation (CDDA) handling drift through multi-source domain adaptation with improved execution time and memory usage. [p. 119383]
- Gama, J.; Žliobaitė, I.; Bifet, A.; Pechenizkiy, M.; Bouchachia, A. (2014) (context) — Survey of concept drift adaptation covering window-based approaches and ensemble methods with their strengths and limitations. [p. 119383]
- Cavalcante, R. C.; Oliveira, A. L. I. (2015) (methodology) — Ensemble extreme learning machine with explicit drift detection and online decision-model updating for financial time-series prediction; the source of the 3-series, 20,000-instance synthetic example. [p. 119381]
- Thalor, M. A.; Patil, S. (2016) (baseline) — ENSDS ensemble classification for nonstationary data streams, reported to outperform Learn++.NSE on several evaluation metrics. [p. 119392]
- Liu, J.; Zio, E. (2016) (baseline) — SVR-based ensemble for drifting data streams with recurring patterns, reducing computational complexity by partial updating and feature vector selection. [p. 119392]
- Grim, L. F. L.; Gradvohl, A. L. S. (2018) (baseline) — High-performance OS-ELM ensembles for regression and time-series forecasting, reported to outperform serial versions. [p. 119394]
- Saadallah, A.; Priebe, F.; Morik, K. (2020) (baseline) — Drift-based dynamic ensemble member selection using clustering (DEMSC) for time-series forecasting with standardisation error and scalability analysis. [p. 119394]
- Boulegane, D.; Bifet, A.; Elghazel, H.; Madhusudan, G. (2020) (baseline) — Streaming time-series forecasting with multi-target regression and dynamic ensemble selection (DES). [p. 119394]
- Tang, J.; Lin, K.-Y.; Li, L. (2022) (methodology) — Domain adaptation for incremental SVM classification of drift data, evaluated on five industrial datasets including clean and credit data. [p. 119395]
- Jain, M.; Kaur, G.; Saxena, V. (2022) (methodology) — K-means clustering plus SVM hybrid drift detection for network anomaly detection across Testbed, NSL-KDD and CIDDS-2017 datasets. [p. 119395]
- Kaminskyi, D.; Li, B.; Müller, E. (2022) (methodology) — Reconstruction-based unsupervised drift detection (AECDD) over multivariate streaming data using Changing Sine Sudden and Changing Sine Incremental synthetic datasets. [p. 119395]
- Guo, H.; Zhang, S.; Wang, W. (2021) (methodology) — Selective ensemble-based online adaptive (SEOA) deep neural networks for streaming data with concept drift. [p. 119395]
- Wang, X.; Kang, Q.; Zhou, M.; Pan, L.; Abusorrah, A. (2021) (methodology) — Multiscale drift detection test (MDDT) for fast learning in nonstationary environments, reported to achieve the highest recall for drift points. [p. 119395]
- Pesaranghader, A.; Viktor, H. L. (2016) (methodology) — Fast Hoeffding Drift Detection Method (FHDDM) using a sliding window and Hoeffding inequality, reported to reduce detection delay, false positives and false negatives. [p. 119396]
- Ramanan, N.; Tahmasbi, R.; Deokwoo, M. S.; Shalini, J.; Claudionor, H.; Coelho, N. (2021) (methodology) — Unsupervised Temporal Drift Detector (UTDD) for real-time detection of seasonal variation and temporal CD without ground truth. [p. 119395]
- Dehghan, M.; Beigy, H.; ZareMoodi, P. (2016) (methodology) — NDE algorithm using ensemble classifiers to detect drift by tracking the distribution of ensemble error. [p. 119396]
- Uchiteleva, E.; Primak, S. L.; Luccini, M.; Hussein, A. R.; Shami, A. (2022) (methodology) — TriLS three-layered, three-state drift-aware time-series prediction for IIoT, moving drift detection and model rebuilding to the cloud. [p. 119382]
- Disabato, S.; Roveri, M. (2024) (methodology) — Tiny Machine Learning for concept drift (TML-CD) integrating k-NN, SVM and NN learners with a hybrid adaptation module for gradual drift. [p. 119398]
- Rahmani, K. et al. (2023) (context) — Assessment of data drift effects on clinical sepsis prediction models using real electronic health records, motivating continuous model monitoring. [p. 119381]
- Lima, M.; Neto, M.; Filho, T. S.; Fagundes, R. A. De A. (2022) (context) — Systematic literature review of learning under concept drift for regression, also the source of the synonyms for 'Concept Drift' used in the search strategy. [p. 119385]