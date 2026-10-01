---
paper_id: A--Abdullahi-2025
first_author: "Abdullahi"
year: 2025
title: "A Systematic Literature Review of Concept Drift Mitigation in Time-Series Applications"
venue: "IEEE Access"
doi: 10.1109/ACCESS.2025.3587231
type: journal-article
designation: international-algorithm-specific
status: extracted
modules: [model_algorithm_integration, model_performance_evaluation]
module_rationale:
  model_algorithm_integration: "Sect. VI proposes a five-step AI-learner roadmap that integrates drift detection, drift handling and the learner into one pipeline, and Sect. V-A catalogues ensemble drift-detection families (ENDSD, SVR, ELM, OS-ELM, DEMSC, DES) that combine several methods."
  model_performance_evaluation: "Sect. IV-A tabulates 20 evaluation metrics across the corpus (accuracy dominant, then AUC, AUROC, RMSE, MAE, MSE, F1) and Sect. V-B compares classification and regression learner performance, so the paper is largely about how time-series models are measured."
---

# A Systematic Literature Review of Concept Drift Mitigation in Time-Series Applications

`A--Abdullahi-2025` — Abdullahi (2025), *IEEE Access* \[10.1109/ACCESS.2025.3587231]

## Summary

A PRISMA 2020 systematic review of 60 studies (2013–2024) finds SVM the most effective learner for detecting and adapting concept drift in time-series classification and regression tasks, and maps a five-step AI-learner roadmap against ADWIN, DDM and EDDM baselines.

## Problem and Motivation

Concept drift continuously changes the statistical properties of nonstationary data, degrading the predictive performance of time-series machine learning models after deployment. Existing drift work concentrates on classification learning and pays little attention to regression, and benchmark-based evaluation may not reflect real-world industrial data. Selecting an appropriate detection technique for a given dataset remains difficult.

## Method

**Design.** Systematic literature review (SLR) following the PRISMA 2020 statement and Kitchenham-Charters guidelines: a secondary, non-experimental synthesis of 60 published studies, plus a proposed non-executed AI-learner roadmap with a qualitative comparison to baseline drift detectors. No original dataset is collected, trained or evaluated by the authors.
**Sample.** Primary (the review's own corpus): n = 60 included studies, unit = published journal article or conference paper published 2013–2024, drawn from 183 unique records screened with 123 excluded (eight for non-English language); the 60 split into N = 46 journal articles and N = 14 conference proceedings. Secondary dataset analysed by the review: none — no dataset is collected, modelled or benchmarked by the authors; Sect. VI-B only specifies a prospective evaluation on real-world financial, weather and sensor time series and reports no results from it.
**Context.** geography: Not applicable to a study population: the literature search was conducted worldwide and explicitly not restricted to a single nation or area. Author affiliations are Universiti Teknologi PETRONAS and Universiti Malaysia Sabah Labuan (Malaysia) and Alasmarya Islamic University, Zliten (Libya).; population: Not reported — the unit of analysis is published literature (60 studies), not human participants or patients.; setting: Virtual/literature-based: database searching of SCOPUS, ScienceDirect, IEEE Xplore, Web of Science, ACM Digital Library and MDPI, with a preliminary Google Scholar keyword search and data extraction in Microsoft Excel 16.77; no laboratory, clinical or field setting was involved..

- Frame the review on PRISMA 2020 and Kitchenham-Charters guidelines, structured in four screening stages: preliminary study, screening, eligibility/quality assessment, and data extraction (Sect. III).
- Build search strings from 'Concept Drift' OR 'CD' AND 'Model Degradation' AND 'Drift Handling' AND 'Drift Detector' AND 'Concept Evaluation' AND 'Time-Series' AND 'AI/ML' AND 'Regression' AND 'Classification', taking synonyms from Lima et al. [34].
- Search six databases — SCOPUS, ScienceDirect, IEEE Xplore, Web of Science, ACM Digital Library and MDPI — over titles, abstracts and keywords for English-language journal and conference papers published 2013–2024.
- Screen 183 unique records with two reviewers, exclude 123 (including eight non-English articles), and retain 60 studies, then score eligibility and quality as 1 (Yes), 0.5 (Partially), 0 (No).
- Extract year, algorithm, metrics, domain, ML techniques, datasets, CD algorithm, problem scope and algorithm learning into Microsoft Excel 16.77, with extraction done by two authors.
- Pose four research questions: which ensemble methods detect drift (RQ1), which ML models are used and how actionable they are (RQ2), which drift-handling algorithms were used over the last decade (RQ3), and what the main pipeline steps are (RQ4).
- Characterise the corpus by publication year, journal, ML problem scope, evaluation metric and learner algorithm (Figs. 5–9), then tabulate studies by classification learner, regression learner, model performance and drift-handling technique (Tables 5–8).
- Propose a roadmap of AI-based learners keyed to drift speed and severity (incremental, gradual, sudden, recurrent) and specify the metrics, evaluation procedures (prequential, holdout, cross-validation) and baselines it should use (Sect. VI).
- Compare that roadmap qualitatively against Page-Hinkley, ADWIN, DDM, EDDM, DW_HDDM and WSTD on detection capability, adaptability/flexibility, and performance/scalability (Sect. VI-C).
- Synthesise lessons learned and best practices on computational cost, window sizing, drift-type handling, drift-versus-noise discrimination, ensemble diversity, evaluation thoroughness, system architecture, and real versus synthetic data (Sect. VIII).

## Software

- Microsoft Excel (version 16.77) — data extraction and compilation of the 60 included studies
- SCOPUS (version not reported) — bibliographic database
- ScienceDirect (version not reported) — bibliographic database
- IEEE Xplore (version not reported) — bibliographic database
- Web of Science (version not reported) — bibliographic database
- ACM Digital Library (version not reported) — bibliographic database
- MDPI (version not reported) — bibliographic database
- Google Scholar (version not reported) — preliminary keyword-combination search to build the search strategy

## Key Findings

- num: 60 studies published 2013–2024 were included after 183 unique records were screened and 123 articles excluded, eight of the exclusions being non-English papers (Abstract, p. 1; Sect. III-B, p. 6; Sect. III-C, p. 7).
- num: SVM is reported as the most effective learning algorithm for detecting and adapting concept drift in both regression and classification time-series tasks, with k-NN and LSTM next most used (Abstract, p. 1; Sect. V-B, p. 16).
- num: Fig. 7 problem-scope shares of the included studies: classification 60%, time-series 12%, supervised 7%, imbalance 7%, unsupervised 6%, regression 6%, semi-supervised 2% (Sect. IV-A, p. 10).
- num: The 60 studies split into N = 46 journal articles and N = 14 conference papers, concentrated in Expert Systems with Applications (five) and Information Sciences (four) (Sect. IV-A, p. 9).
- num: The preliminary Google Scholar keyword search returned 5,850 records after filtering (Sect. III-A-1, p. 6).
- num: The corpus catalogues 21 learner algorithms and 20 evaluation metrics (counted from the enumerations printed in Sect. IV-A, pp. 10–11).
- num: Publication volume over 2013–2024 peaks in 2022, with the sharpest rise between 2021 and 2022 (Sect. IV-A, p. 8, Fig. 5).
- num: Accuracy is the dominant evaluation metric across the reviewed studies, ahead of AUC, AUROC, RMSE, MAE, MSE and F1 (Sect. IV-A, pp. 10–11, Fig. 8).
- ADWIN, HDDM and DDM are the most-used drift-handling techniques in the corpus, and each is matched to a specific drift type (Sect. IV-B-3, p. 12).
- Ensemble approaches — ENSDS, SVR, ELM, OS-ELM, DEMSC and dynamic ensemble selection — are identified as the most common drift-detection families in time-series settings (Sect. V-A, p. 15).

## Key Figures and Tables

- Fig. 1 (p. 3): Concept drift types by speed → incremental, gradual, sudden and recurrent drift are the taxonomy used throughout the roadmap.
- Fig. 2 (p. 5): Systematic literature review mapping process → the survey methodology is organised into four screening stages.
- Fig. 3 (p. 5): Google Scholar keyword-combination results → the preliminary search used to select search terms, reduced to 5,850 records after filtering.
- Fig. 4 (p. 7): PRISMA 2020 flow diagram of study screening and selection → the documented path from database search to 183 screened, 123 excluded and 60 included.
- Fig. 5 (p. 8): Distribution of studies by publication year → CD research grows over 2013–2024, peaking in 2022.
- Fig. 6 (p. 9): Distribution of studies by journal → 46 journal and 14 conference papers, led by Expert Systems with Applications and Information Sciences.
- Fig. 7 (p. 9): Characteristics of studies based on the problem scope of machine learning → classification 60%, time-series 12%, supervised 7%, imbalance 7%, unsupervised 6%, regression 6%, semi-supervised 2% (read from the chart, stated in Sect. IV-A, p. 10).
- Fig. 8 (p. 10): Characteristics of studies based on evaluation metrics → accuracy is the primary reported measure, with 20 metrics in total.
- Fig. 9 (p. 10): Characteristics of studies using learning algorithms → 21 learners catalogued, with SVM and LSTM most frequent.
- Fig. 10 (p. 16): Ensemble-based learners for concept drift detection in time-series data → the ensemble families that answer RQ1.
- Fig. 11 (p. 20): Illustration of AI learners for concept drift detection → maps AI learners onto drift speed and severity categories.
- Fig. 12 (p. 22): Lessons learned and best practices for concept drift mitigation in time-series applications → the graphical summary of the Sect. VIII practices.
- Table 1 (p. 4): Comparison with other studies in the same domain → positions this SLR against earlier concept drift reviews.
- Table 2 (p. 6): Formulated research questions and motivation → the four RQs that structure Sections V-A to V-D.
- Table 3 (p. 6): Inclusion and exclusion criteria → eligibility rules for the screened records.
- Table 4 (p. 8): Eligibility and quality assessment scoring criteria → 1 for Yes, 0.5 for Partially, 0 for No.
- Table 7 (p. 13): Studies categorized by model performance for CD detection and adaptation in a general context → links error metrics to drift detection.
- Table 8 (p. 14): Studies categorized by a technique that handles concept drift → maps ADWIN, HDDM, DDM and related detectors to drift types.
- Table 9 (p. 15): Summary of ensemble-based learning concept drift detection techniques → the ENSDS, SVR, ELM, OS-ELM, DEMSC and DES families.
- Table 12 (p. 24): Evaluation metrics and datasets for CD detection from the selected studies → the per-study metric and dataset inventory.
- Table 13 (p. 25): State-of-the-art studies with their contributions, strengths and weaknesses → the qualitative appraisal of each included study.
- Table 14 (p. 26): PRISMA 2020 checklist → self-reported compliance, obtained from prisma-statement.org on 19 May 2025.

## Limitations and Gaps

- Search-criteria restriction acknowledged by the authors: only English-language journal and conference papers published between 2013 and 2024 in SCOPUS, ScienceDirect, IEEE Xplore, Web of Science, MDPI and ACM were eligible, so some relevant studies were excluded (Sect. IX Conclusion, p. 24).
- The authors note that most proposed drift detection, handling and adaptation methods remain unsolved, that reliance on simulation datasets may not capture real-world scenarios, and that single-dataset testing limits generalizability (Sect. IX, p. 24).
- Comparisons with active state-of-the-art approaches are limited, and similarity-based and dissimilarity-based detection methods for time-series data were not investigated (Sect. IX, p. 24).
- The authors recommend broader database coverage and adaptive learning models that adapt to drift without explicit re-training, plus unsupervised and semi-supervised detectors, causal representation learning and multimodal deep learning (Sect. IX, pp. 24–26).
- [unacknowledged] The Sect. VI-B 'experimental evaluation' and Sect. VI-C 'comparative analysis' are presented as performed but report no numerical result; the roadmap-versus-baseline comparison is qualitative only.
- [unacknowledged] Tables 5–13, which hold the per-study datasets, metrics and state-of-the-art appraisals behind Figures 5–9, appear only as captions in the converted text, so the per-study values cannot be verified against the figures.
- [unacknowledged] The Fig. 7 problem-scope percentages are chart-read proportions and their denominators are never stated, so they cannot be tied back to the 60 included studies without the original figure.

## Definitions

- **Concept Drift (CD)** — Continuous change in the statistical properties of a dataset over time, i.e. a change in the relationship between input data and model target values, which degrades ML performance after deployment.
- **Dataset shift** — Any change in the joint distribution of input and target variables between training and testing; unlike CD it need not imply time evolution.
- **Incremental drift** — Minimal, continuous change in the original data distribution; hard to detect in real time because increments are small.
- **Gradual drift** — Noticeable change in the target data distribution, producing long-term effects but allowing earlier detection than incremental drift.
- **Sudden drift** — Abrupt and significant change in the data distribution at a particular time point, causing unforeseen model behaviour.
- **Recurrent drift** — An old concept reappears after a period of absence, changing previously observed concepts.
- **ADWIN** — Adaptive windowing detector that shrinks its window when statistical differences between sub-windows exceed a specified confidence level.
- **DDM / EDDM / HDDM** — Drift Detection Method, Early Drift Detection Method and Hoeffding Drift Detection Method — error-rate and statistical-distance detectors used as baselines.
- **Prequential evaluation** — Test-then-train protocol in which each new data point tests the model before training on it, simulating a constant data stream.
- **PRISMA 2020** — Preferred Reporting Items for Systematic Reviews and Meta-Analyses 2020, the reporting and screening standard the review follows.

## Key Equations

- `Accuracy (ACC) = (TP + TN) / (TP + TN + FP + FN)` — Proportion of instances, drift and no-drift, correctly identified.
- `Precision (P) = TP / (TP + FP)` — Share of flagged drift that is genuinely drift.
- `Recall (R) = TP / (TP + FN)` — Share of actual drift events the model detects.
- `F1 = 2 x Precision x Recall / (Precision + Recall)` — Harmonic balance of precision and recall.
- `RMSE = sqrt( (1/n) * sum_{i=1}^{n} (y_hat_i - y_i)^2 )` — Root mean squared prediction error, used for time-series drift models.
- `MSE = (1/n) * sum_{i=1}^{n} (y_hat_i - y_i)^2` — Average squared prediction error; abrupt rises signal drift.
- `MAE = (1/n) * sum_{i=1}^{n} |y_hat_i - y_i|` — Average absolute prediction error over the stream.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Studies included in the systematic review after screening | included studies | 60 | — | — | Sect. III-B Stage 2 Screening Process, p. 6 |
| Unique records retrieved and reviewed during screening | screened records | 183 | — | — | Sect. III-B Stage 2 Screening Process, p. 6 |
| Articles excluded during screening | excluded records | 123 | — | — | Sect. III-B Stage 2 Screening Process, p. 6 |
| Records excluded for being written in a language other than English | excluded records | eight | — | — | Sect. III-C Stage 3 Eligibility and Quality Assessment, p. 7 |
| Preliminary Google Scholar search output after quality filtering | records | 5,850 | — | — | Sect. III-A-1 Keyword Identification, p. 6 |
| Included studies published in journals | studies | N = 46 | — | — | Sect. IV-A Characteristics of the Selected Studies, p. 9 |
| Included studies published in conference proceedings | studies | N = 14 | — | — | Sect. IV-A Characteristics of the Selected Studies, p. 9 |
| Included studies published in Expert Systems with Applications, the highest-output journal | publications | five | — | — | Sec. IV-A Characteristics of the Selected Studies, p. 9 |
| Included studies published in Information Sciences, second-highest journal output | publications | four | — | — | Sec. IV-A Characteristics of the Selected Studies, p. 9 |
| Share of included studies whose ML problem scope is classification (Fig. 7 chart-read proportion) | share of studies | 60% | — | — | Sec. IV-A Characteristics of the Selected Studies, p. 10 (Fig. 7) |
| Share of included studies whose ML problem scope is time-series (Fig. 7 chart-read proportion) | share of studies | 12% | — | — | Sec. IV-A Characteristics of the Selected Studies, p. 10 (Fig. 7) |
| Share of included studies whose ML problem scope is supervised (Fig. 7 chart-read proportion) | share of studies | 7% | — | — | Sec. IV-A Characteristics of the Selected Studies, p. 10 (Fig. 7) |
| Share of included studies whose ML problem scope is imbalance (Fig. 7 chart-read proportion) | share of studies | 7% | — | — | Sec. IV-A Characteristics of the Selected Studies, p. 10 (Fig. 7) |
| Share of included studies whose ML problem scope is unsupervised (Fig. 7 chart-read proportion) | share of studies | 6% | — | — | Sec. IV-A Characteristics of the Selected Studies, p. 10 (Fig. 7) |
| Share of included studies whose ML problem scope is regression (Fig. 7 chart-read proportion) | share of studies | 6% | — | — | Sec. IV-A Characteristics of the Selected Studies, p. 10 (Fig. 7) |
| Share of included studies whose ML problem scope is semi-supervised (Fig. 7 chart-read proportion) | share of studies | 2% | — | — | Sec. IV-A Characteristics of the Selected Studies, p. 10 (Fig. 7) |
| Quality scoring scale applied to each screened study during eligibility assessment | score for Yes / Partially / No | 1 / 0.5 / 0 | — | — | Sect. III-C Stage 3 Eligibility and Quality Assessment, p. 7 |
| Sensor count in the Mica2Dot real temperature dataset used by an included fog-DeepStream study | sensors | 54 | — | — | Sec. VII Discussion, p. 22 |
| Publication window covered by the review's search strategy | years | 2013 – 2024 | — | — | Sec. III-A-1 Keyword Identification, p. 6 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "This study conducted a Systematic Literature Review (SLR) that classified, identified, and recommended an optimal method for the detection and adaptation of CD in regression and classification tasks involving time-series data." | Abstract, p. 1 | model_algorithm_integration |
| "However, certain limitations exist, and most studies on CD detection and adaptation in time-series data have focused on classification learning, with minimal attention paid to regression learning." | Abstract, p. 1 | model_algorithm_integration |
| "60 studies published between 2013 and 2024 were thoroughly surveyed and evaluated using PRISMA guidelines." | Abstract, p. 1 | model_algorithm_integration |
| "Additionally, the evaluation metric performance for the validation of CD in ML models using benchmark datasets may not accurately reflect real-world industrial data." | Sec. I Introduction, p. 2 | model_algorithm_integration |
| "A comparative review of existing CD detection approaches based on accuracy, adaptability, and computational efficiency was conducted by synthesizing recent developments and identifying research gaps." | Sec. I Introduction, p. 2 | model_algorithm_integration |
| "These approaches maintain a set of competing models, allowing dynamic selection of the most relevant hypothesis based on the current input." | Sec. II Related Reviews, p. 3 | model_algorithm_integration |
| "This indicates that most advancements in CD detection and adaptation can be attributed to the focus on classification problems within time-series contexts." | Sec. IV-A Characteristics of the Selected Studies, p. 10 | model_algorithm_integration |
| "In addition, most studies have employed SVM and LSTM models for CD detection and adaptation because of their ability to handle dynamic data shifts." | Sec. IV-A Characteristics of the Selected Studies, p. 11 | model_algorithm_integration |
| "Metrics such as MSE and MAE are employed in time-series forecasting because of their accurate measurement of error magnitude over time." | Sec. IV-B-2 Summary of Studies Based on Model Performance, p. 12 | model_algorithm_integration |
| "For example, abrupt increases in error rates, such as the mean squared error (MSE), classification error, or abrupt decreases in confidence scores, indicate drift." | Sec. IV-B-2 Summary of Studies Based on Model Performance, p. 12 | model_performance_evaluation |
| "the SVM and k-NN models are robust against feature-based changes, whereas LSTM captures temporal dependencies, making them appropriate options for various types of drifts in time-series applications." | Sec. V-B RQ2, p. 16 | model_algorithm_integration |
| "Temporal trends frequently exhibit trends, seasonality, and autocorrelations." | Sec. V-D RQ4, p. 17 | model_algorithm_integration |
| "However, standard drift detection techniques such as Page-Hinkley, ADWIN, DDM, and EDDM have been used as baselines." | Sec. VI-B-4 Baseline Methods, p. 21 | model_algorithm_integration |
| "The Intel Berkeley Research Lab provided real temperature data from 54 Mica2Dot sensors that contained weather plates." | Sec. VII Discussion, p. 22 | model_algorithm_integration |
| "For example, ADWIN dynamically adjusts the window size based on variations in the observed data." | Sec. VIII-B Selecting Appropriate Window Sizes, p. 23 | model_algorithm_integration |
| "The OAR-DLSTM method assigns prediction tasks to multiple sub-models based on recurring concepts to manage hybrid recurring drifts in industrial processes" | Sec. VIII-C Handling Different Drift Types, p. 23 | model_algorithm_integration |
| "The lesson learned is that both data types are important because synthetic data allow rigorous and controlled experimentation, whereas real-world data demonstrate practical applicability and unforeseen challenges." | Sec. VIII-H Real-World Versus Synthetic Data, p. 24 | model_algorithm_integration |
| "However, reliance on simulation datasets may not fully capture real-world scenarios. Moreover, several studies have tested the proposed method using a single dataset, which may limit generalizability." | Sec. IX Conclusion and Future Directions, p. 24 | model_algorithm_integration |
| "Finally, this study was unable to investigate other approaches to CD detection, such as similarity and dissimilarity-based methods, using time-series data." | Sec. IX Conclusion and Future Directions, p. 24 | model_algorithm_integration |
| "Most existing methods in the literature require training models after drift detection, which can be time-consuming and disruptive in real-world scenarios" | Sec. IX Future Directions, p. 25 | model_algorithm_integration |

## Remember This

- PRISMA 2020 review of 60 studies on concept drift detection and adaptation in time-series data, 2013–2024.
- SVM is the recommended learner; k-NN and LSTM are the next most used, ahead of XGBoost and RF.
- ADWIN, HDDM and DDM are the dominant statistical drift-handling techniques in the corpus.
- Problem scope is lopsided: 60% classification against only 6% regression and 2% semi-supervised.
- Roadmap compares AI learners against Page-Hinkley, ADWIN, DDM, EDDM, DW_HDDM and WSTD qualitatively only.

## Cited Works

- Page, M. J.; McKenzie, J. E.; Bossuyt, P. M.; et al. (2021) (methodology) — PRISMA 2020 statement supplied the reporting standard for the review's screening and selection process. [p. 5]
- Kitchenham, B.; Charters, S. (2007) (methodology) — Study screening and selection followed the established software engineering systematic review guidelines. [p. 5]
- Sezer, O. B.; Gudelek, M. U.; Ozbayoglu, A. M. (2020) (context) — Financial time series forecasting with deep learning: a systematic literature review covering 2005 to 2019. [p. 1]
- Gama, J.; Zliobaite, I.; Bifet, A.; Pechenizkiy, M.; Bouchachia, A. (2014) (context) — Survey of adaptive learning methods for concept drift, categorising window-based and ensemble strategies with strengths and limits. [p. 4]
- Bayram, F.; Ahmed, B. S.; Kassler, A. (2022) (methodology) — Analysis and hierarchical taxonomy of performance-based concept drift detectors from the past decade. [p. 3]
- Shen, P. K.; Ming, Y.; Li, H.; Gao, J.; Zhang, W. (2023) (context) — Survey of unsupervised concept drift detectors with a taxonomy for real applications, but lacking empirical evaluation. [p. 3]
- Lima, M.; Neto, M.; Filho, S. T.; De A. Fagundes, R. A. (2022) (methodology) — Supplied the synonyms for 'concept drift' used to broaden the review's keyword combinations. [p. 6]
- Cavalcante, R. C.; Oliveira, A. L. I. (2015) (finding) — Ensemble ELM with explicit drift detection shortened prediction time of online sequential ELM while maintaining accuracy. [p. 14]
- Uchiteleva, E.; Primak, S. L.; Luccini, M.; Hussein, A. R.; Shami, A. (2022) (methodology) — TriLS three-layered, three-state system adjusts a lightweight predictive model in time for IIoT nonstationary environments. [p. 3]
- Tang, J.; Lin, K.-Y.; Li, L. (2022) (finding) — Incremental SVM with domain adaptation evaluated drift handling on five industrial datasets including clean and credit data. [p. 22]
- Sun, L.; Ji, Y.; Zhu, M.; Gu, F.; Dai, F.; Li, K. (2021) (finding) — DLSTM, LSTM and OAR learners assigned prediction tasks to sub-models to handle hybrid recurring drift in process industry streams. [p. 19]
- Alencar, B. M.; Canario, J. P.; Lobao Neto, R.; et al. (2023) (finding) — Fog-DeepStream combined LSTM, concept drift and deep neural networks on 54 Mica2Dot weather sensor readings. [p. 22]
- Kaminskyi, D.; Li, B.; Muller, E. (2022) (finding) — Autoencoder-based unsupervised drift detection used synthetic changing-sine sudden and incremental streams. [p. 22]
- Heidrich, B.; Ludwig, N.; Turowski, M.; Mikut, R.; Hagenmeyer, V. (2022) (finding) — RMSE and MASE were used to evaluate a concept drift model in an energy time-series forecasting context. [p. 18]
- Disabato, S.; Roveri, M. (2024) (methodology) — Tiny machine learning solution integrated k-NN, SVM and NN with a hybrid adaptation module for gradual drift. [p. 19]

---
Conversion: [`A--Abdullahi-2025_marked.md`](../../literature/conversions/A--Abdullahi-2025_marked.md)
