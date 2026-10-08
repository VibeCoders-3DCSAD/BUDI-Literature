---
paper_id: I--Salminen-2023
first_author: Salminen
year: 2023
title: "How can algorithms help in segmenting users and customers? A systematic review and research agenda for algorithmic customer segmentation"
venue: "Journal of Marketing Analytics"
doi: 10.1057/s41270-023-00235-5

designation: international
status: extracted
modules: [model_algorithm_integration, model_performance_evaluation, model_development, data_collection]
module_rationale:
  model_algorithm_integration: "Table 4 (p. 7) lists examples of combining customer segmentation algorithms, and RQ2 (p. 4) reports that roughly 80% of studies use a single algorithm while others combine multiple."
  model_performance_evaluation: "RQ4 (p. 6) identifies 14 evaluation metrics for customer segmentation and Table 5 (p. 8) classifies them into statistics-focused and separation-focused categories."
  model_development: "RQ5 (p. 9) reports that out of 169 studies, 138 (81.7%) used only segment size as a hyperparameter while 31 (18.3%) used additional hyperparameters."
  data_collection: "The methodology (p. 3) describes a systematic literature search across four databases (WoS, Emerald Insight, ACM Digital Library, ABI/INFORM Collection) with a documented screening process in Tables 1-2."
---

## Summary

A systematic literature review of 172 articles on algorithmic customer segmentation (ACS), identifying 46 different algorithms and 14 evaluation metrics. K-means clustering is the most employed algorithm (27 uses, 20.1%). Most studies (roughly 80%) use a single algorithm. The average number of customer segments created is 5.7 (SD = 3.9), with four segments being most common. Evaluation is dominated by technical clustering metrics rather than business outcomes, and only 7 cases (4.1%) used subject matter experts. The authors propose seven key goals and three practical implications for future research.

## Problem and Motivation

Business success depends on understanding customers, and customer segmentation is a key method to achieve this. With the rise of AI and machine learning, firms are increasingly turning to algorithmic approaches, yet they struggle to understand which methods to use—what algorithm to choose, whether to use one or many, how many segments to create, and how to evaluate results. Simultaneously, academic literature lacks a synthesis of how customer segmentation is actually carried out in research studies in terms of methods, parameters, and evaluation. The most cited article assessing clustering in marketing (Punj and Stewart) is from 1983, so an updated review is needed. Both practical and theoretical research gaps hinder development of the body of knowledge around customer segmentation, especially in light of novel AI technologies.

## Method

**Design.** Systematic literature review (SLR) following Kitchenham et al. (2009), conducted in three sequential stages: (a) literature search, (b) assessment of the evidence base, and (c) analysis and synthesis of findings. The authors state no other design label.
**Sample.** n = 172 articles (unit of analysis: published journal article), of which 134 (77.9%) were algorithm-based and used for RQ1-2 and RQ4-5; the full 172 used for RQ3 and RQ6.
**Context.** geography: Not applicable — systematic literature review with no geographic scope stated; population: Journal articles on customer segmentation published from 2000 onward; setting: Four academic databases (Web of Science, Emerald Insight, ACM Digital Library, ABI/INFORM Collection).

- Searched four databases with keywords "customer segmentation*", "user segmentation*", and "audience segmentation*".
- For WoS, kept only business and computer science fields after initial 574 entries; excluded materials science, physics, chemistry, and integrative complementary medicine.
- Screened 479 articles through six hygiene steps: missing information, publication type (removing conference proceedings, book chapters, theses, non-journal articles), recency (pre-2000), duplicates, language (non-English), and disciplines (geography), leaving 204.
- Assessed 204 articles for relevance, removing 32 (15.7%) irrelevant articles (literature reviews or non-empirical), leaving 172 (84.3%).
- Classified 134 (77.9%) as algorithm-based and 38 (22.1%) as non-algorithm-based.
- Coded articles using a data extraction sheet with eight information fields corresponding to the six RQs (Table 3).
- One researcher coded all articles; another researcher verified by randomly investigating a sample of 20 articles.
- Results obtained by carefully reviewing full-text articles.

## Limitations and Gaps

- The authors acknowledge they did not include articles published before the year 2000, nor keywords dealing with market segmentation or consumer segmentation (Study limitations, p. 13).
- The authors acknowledge that few studies show empirical evidence of the benefits of customer segmentation in organizational use cases or systems, i.e., ecological validity (Discussion, p. 10).
- The authors acknowledge that conceptual vagueness around 'customer segmentation' can hinder scientific advances, as the concept is often treated implicitly (Discussion, p. 10).
- The authors acknowledge that the fundamental challenges of clustering identified by Punj and Stewart (1983)—choice of appropriate metric, selection of variables, cross-validation, and external validation—remain topical and fundamentally unresolved (Discussion, p. 11).
- [unacknowledged] The screening flow in Table 2 (p. 5) begins at 479 articles, but the text (p. 3) reports the WoS initial search yielded 574 entries; the difference of 95 is not explained in the extracted text.
- [unacknowledged] No inter-coder reliability statistic (e.g., Cohen's kappa) is reported; the verification procedure is described only as one researcher checking a random sample of 20 articles (p. 3).
- [unacknowledged] The full search strings and database-specific queries are not reported in the extracted text, making the search non-reproducible from the paper alone.
- [unacknowledged] The paper reports percentages that sometimes use different denominators (172 articles, 169 studies, 151 articles) without reconciling them in the text.
- [unacknowledged] No publication bias assessment or quality appraisal of the included studies is reported.
- [unacknowledged] The review is limited to four databases and excludes conference proceedings, book chapters, and theses (Table 2, p. 5), which may omit relevant ACS work.
- [unacknowledged] No effect sizes or meta-analytic synthesis is performed; all findings are descriptive counts and percentages.
- [unacknowledged] The "roughly 80%" single-algorithm figure is not accompanied by a precise numerator or denominator in the text.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Total articles reviewed after screening | articles | 172 | — | — | Abstract, p. 1; p. 3 |
| Algorithm-based articles | articles | 134 (77.9%) | — | — | p. 3 |
| Non-algorithm-based articles | articles | 38 (22.1%) | — | — | p. 3 |
| Different algorithms identified | algorithms | 46 | — | — | RQ1, p. 4 |
| K-means clustering usage | frequency | 27 (20.1%) | — | — | RQ1, p. 4 |
| Variants of K-means clustering usage | frequency | 10 (7.5%) | — | — | RQ1, p. 4 |
| Fuzzy algorithms usage | frequency | 8 (6.0%) | — | — | RQ1, p. 4 |
| Latent class analysis models usage | frequency | 8 (6.0%) | — | — | RQ1, p. 4 |
| RFM and variants usage | frequency | 6 (4.5%) | — | — | RQ1, p. 4 |
| Self-Organizing Maps usage | frequency | 3 (2.25%) | — | — | RQ1, p. 4 |
| Genetic Algorithms usage | frequency | 3 (2.25%) | — | — | RQ1, p. 4 |
| Algorithms used only once | algorithms | 34 | — | — | Fig. 4, p. 4 |
| Studies using one algorithm | percentage | roughly 80% | — | — | RQ2, p. 4 |
| Most common number of segments | segments | 4 (n = 32, 21.2%) | — | — | RQ3, p. 5 |
| Average number of segments | segments | 5.7 | — | — | RQ3, p. 5 |
| Standard deviation of segments | SD | 3.9 | — | — | RQ3, p. 5 |
| Mode of segments | segments | 4 | — | — | Discussion, p. 10 |
| Median of segments | segments | 5 | — | — | Discussion, p. 10 |
| Minimum segments | segments | 1 | — | — | Discussion, p. 10 |
| Maximum segments | segments | 20 | — | — | Discussion, p. 10 |
| Studies generating 2-5 segments | n | 103 (68.2%) | — | — | RQ3, p. 5 |
| Studies generating 10 or fewer segments | percentage | 92.1% | — | — | RQ3, p. 5 |
| Articles expressing number of segments | articles | 151 (87.7%) | — | — | Fig. 5 caption, p. 5 |
| Articles not reporting segment size | articles | 21 (12.2%) | — | — | Fig. 5 caption, p. 5 |
| Evaluation metrics identified | metrics | 14 | — | — | RQ4, p. 6 |
| Statistics-focused metrics | metrics | 6 (42.9%) | — | — | RQ4, p. 6 |
| Separation-focused metrics | metrics | 8 (57.1%) | — | — | RQ4, p. 6 |
| Studies with hyperparameter information | studies | 169 | — | — | RQ5, p. 9 |
| Studies using only segment size | n | 138 (81.7%) | — | — | RQ5, p. 9 |
| Studies using additional hyperparameters | n | 31 (18.3%) | — | — | RQ5, p. 9 |
| Cases using subject matter experts | cases | 7 (4.1%) | — | — | RQ6, p. 9 |
| Initial WoS search results | entries | 574 | — | — | Literature search, p. 3 |
| Screening step 0: start | articles | 479 | — | — | Table 2, p. 5 |
| Screening step 1: after missing information | articles | 471 | — | — | Table 2, p. 5 |
| Screening step 2: after publication type | articles | 239 | — | — | Table 2, p. 5 |
| Screening step 3: after recency | articles | 234 | — | — | Table 2, p. 5 |
| Screening step 4: after duplicates | articles | 208 | — | — | Table 2, p. 5 |
| Screening step 5: after language | articles | 205 | — | — | Table 2, p. 5 |
| Screening step 6: after disciplines | articles | 204 | — | — | Table 2, p. 5 |
| Irrelevant articles removed | articles | 32 (15.7%) | — | — | p. 3 |
| K-means or derivative popularity | percentage | 27.6% | — | — | PI01, p. 13 |
| Expert panel size (Warner) | experts | 7 | — | — | RQ6, p. 10 |
| Expert count (Safari) | experts | 16 | — | — | RQ6, p. 9 |
| Expert count (Manidatta) | experts | 9 | — | — | RQ6, p. 10 |
| Customers segmented (Manidatta) | customers | 1,600 | — | — | RQ6, p. 10 |
| Segments created (Manidatta) | segments | 8 | — | — | RQ6, p. 10 |
| Months of transaction data (Manidatta) | months | 18 | — | — | RQ6, p. 10 |
| Segments identified by algorithm (Lee and Cho) | segments | 10 | — | — | RQ6, p. 10 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "What algorithm to choose for customer segmentation? Should you use one algorithm or many? How many customer segments should you create? How to evaluate the results?" | Abstract, p. 1 | model_algorithm_integration |
| "The results from extracting information from 172 relevant articles show that algorithmic customer segmentation is the predominant approach for customer segmentation." | Abstract, p. 1 | model_algorithm_integration |
| "We found researchers employing 46 different algorithms and 14 different evaluation metrics." | Abstract, p. 1 | model_performance_evaluation |
| "K-means clustering is the most frequently used algorithm, as it is used 27 times (20.1%) in our sample of reviewed literature." | RQ1, p. 4 | model_algorithm_integration |
| "After a thorough overview of the ACS literature, it appears that in most cases, researchers have utilized one algorithm for customer segmentation (i.e., in roughly 80% of them)." | RQ2, p. 4 | model_algorithm_integration |
| "Most commonly, researchers have suggested/created four customer segments (n = 32, 21.2%). On average, researchers created 5.7 segments (SD = 3.9)." | RQ3, p. 5 | model_development |
| "Overall, we identified 14 different metrics for evaluating customer segmentation outputs, of which six (42.9%) focused on statistical indicators and eight (57.1%) focused on distances and/or similarity calculation." | RQ4, p. 6 | model_performance_evaluation |
| "In our review, out of the 169 studies that offered information about hyperparameters, more than four out of every five articles (n = 138, 81.7%) applied only segment size as a hyperparameter" | RQ5, p. 9 | model_development |
| "In this study, we encountered only seven cases (4.1%) where subject matter experts were used to evaluate the quality of customer segmentation and provide expert opinions." | RQ6, p. 9 | model_performance_evaluation |
| "Customer segmentation evaluation is centered on using metrics derived from clustering practices, rather than using metrics especially tailored to customer segmentation, business outcomes, or ecological validity." | RQ4, p. 6 | model_performance_evaluation |
| "Few studies show empirical evidence of these benefits in organizational use cases or systems (i.e., ecological validity)." | Discussion, p. 10 | model_performance_evaluation |
| "There is no one set of customer segmentation criteria, but the studies vastly vary in terms of the segmentation criteria applied." | Discussion, p. 10 | data_collection |
| "Customer segmentation, especially when applying AI and ML algorithms, is a socio-technical problem." | Discussion, p. 13 | model_algorithm_integration |
| "We did not include articles published before the year 2000 in our sample." | Study limitations, p. 13 | data_collection |

## Key Findings

- 46 different algorithms identified for customer segmentation; K-means is most employed (27 uses, 20.1%).
- Roughly 80% of studies use a single algorithm; multiple algorithms are combined in a minority of studies (Table 4).
- Average number of segments: 5.7 (SD = 3.9); mode = 4, median = 5; range = 1 to 20.
- 14 evaluation metrics identified; 6 (42.9%) statistics-focused, 8 (57.1%) separation-focused.
- Of 169 studies reporting hyperparameters, 138 (81.7%) used only segment size.
- Only 7 cases (4.1%) used subject matter experts for evaluation.
- 92.1% of studies generated ten or fewer segments.
- Few studies show empirical evidence of benefits in organizational use cases.
- K-means or a derivative is the most popular approach (27.6%).

## Key Figures and Tables

- Fig. 1 (p. 2): Hierarchy of key concepts — AI → ML → unsupervised learning → clustering → customer segmentation.
- Fig. 2 (p. 3): Google Scholar search results for segmentation + marketing, 1980-2030 — general increase in interest.
- Fig. 3 (p. 3): Research process — screening, relevance assessment, algorithm assessment, data extraction.
- Fig. 4 (p. 4): Frequency chart of algorithms used — K-means highest at 27, followed by variants at 10.
- Fig. 5 (p. 5): Number of customer segments created — most common is 4, average 5.7.
- Table 1 (p. 4): Search details per database — WoS 574 entries, plus other database counts.
- Table 2 (p. 5): Inclusion/exclusion steps — 479 → 471 → 239 → 234 → 208 → 205 → 204.
- Table 3 (p. 6): Data extraction fields — 8 fields corresponding to RQs.
- Table 4 (p. 7): Examples of combining algorithms — K-means with RFM, SOM, K-medoids, etc.
- Table 5 (p. 8): Segmentation evaluation metrics — 14 metrics classified into statistics-focused and separation-focused.

## Definitions

- **Algorithmic customer segmentation (ACS)** — The application of AI/ML algorithms to divide customers into groups based on their similarities and differences.
- **Hyperparameter** — A configuration setting external to the model, typically set before learning begins; for ACS, the most central is the number of segments created (segment size).
- **Segment size** — The number of customer segments created; the most commonly used hyperparameter in ACS.
- **Statistics-focused metrics** — Evaluation metrics that compare two or more groups using statistical testing or probabilities (ACC, ANOVA, ARI, BIC, MW, TCE).
- **Separation-focused metrics** — Evaluation metrics that calculate distances or similarities between items and centroids (ACE, CHI, DBI, DI, FS, SI, VI, XBI).
- **K-means clustering** — The most frequently used algorithm for customer segmentation (27 uses, 20.1%).
- **RFM** — Recency, Frequency, Monetary gain; used 6 times (4.5%) in the reviewed literature.
- **Ablation study** — A form of experimental design used to study the effect of removing a specific part or feature of a model on its overall performance.

## Remember This

- This is a systematic review of 172 articles on algorithmic customer segmentation, not an empirical study.
- K-means clustering dominates (27 uses, 20.1%); 46 algorithms identified in total.
- Roughly 80% of studies use a single algorithm; combining algorithms is a minority practice.
- Average segments = 5.7 (SD = 3.9), mode = 4, range = 1-20.
- 14 evaluation metrics identified, all technical; few studies use expert validation (7 cases, 4.1%).
- 82% of studies use only segment size as a hyperparameter.
- The paper calls for more empirical evidence of segmentation benefits in organizations.

## Cited Works

- Punj, G., and D.W. Stewart. 1983 — The foundational review of cluster analysis in marketing, used as a benchmark for comparison. [p. 1, p. 11]
- Kitchenham, B., et al. 2009 — The SLR methodology followed by the authors. [p. 3]
- Lee, J.H., and S.C. Park. 2005 — Decision-rule algorithm to discover ideal customer type (one segment). [p. 5]
- Nemati, Y., et al. 2018 — CLV-based framework using expert evaluation. [p. 9]
- Safari, F., et al. 2016 — RFM-based CLV with 16 experts. [p. 9]
- Manidatta, R., et al. 2021 — Fuzzy c-means with 9 experts, 1,600 customers, 8 segments. [p. 10]
- Warner, L.A. 2019 — Audience segmentation with 7-member expert panel. [p. 10]
- Lee, Y., and S. Cho. 2021 — Leuven algorithm with 10 segments validated by expert. [p. 10]
- Böttcher, M., et al. 2009 — Outlier study with 1209 and 8984 segments. [Fig. 5 caption, p. 5]
- Fernández-Delgado, M., et al. 2014 — "Do we need hundreds of classifiers?" cited in discussion. [p. 13]