---
paper_id: I--Yang-2024a
first_author: Yang
year: 2024
title: "Study of an Adaptive Financial Recommendation Algorithm Using Big Data Analysis and User Interest Pattern with Fuzzy K-Means Algorithm"
venue: "International Journal of Computational Intelligence Systems"
doi: 10.1007/s44196-024-00719-x

designation: international
status: extracted
modules: [model_algorithm_integration, model_development, data_collection, model_performance_evaluation, system_development]
module_rationale:
  model_algorithm_integration: "FNFinRec couples fuzzy K-means clustering with neural collaborative filtering in a single pipeline (Fig. 1, p. 5; Sec. 3.5, p. 9)."
  model_development: "Secs. 3.3–3.4 give the training workflow for the fuzzy K-means objective and the NCF embedding/MLP loss (Sec. 3.3, p. 5; Sec. 3.4, p. 8)."
  data_collection: "The financial-profile and user-item data come from the Kaggle 'Finance data analysis' dataset [25] (Table 1, p. 4; Sec. 3, p. 3)."
  model_performance_evaluation: "Clustering and recommendation quality are measured with silhouette coefficient, Davies–Bouldin Index, MSE, Precision@k and Recall@k (Sec. 4.2, p. 9)."
  system_development: "The algorithm is implemented on a Hadoop platform with a MapReduce framework (Abstract, p. 1; Sec. 3.2, p. 4)."
---

## Summary

Yang proposes FNFinRec (Fuzzy Neural Financial Recommendation), an adaptive financial-recommendation algorithm that combines fuzzy K-means clustering over user interest patterns with neural collaborative filtering (NCF) to suggest investment products. The pipeline runs on a Hadoop platform with a MapReduce framework so that large financial datasets can be processed in parallel. Fuzzy logic is used to absorb uncertainty in user preferences and to assign users to overlapping clusters; NCF then learns from a binary user-item interaction matrix and predicts interest in financial services. An adaptive user profile is updated as new interaction data arrive, and a feedback mechanism re-clusters users and refreshes recommendations against real-time market conditions. Evaluation compares FNFinRec against four existing algorithms — ANFIS, PRS-MPT, IFCM and K-L-KM — on silhouette coefficient, Davies–Bouldin Index, mean square error, Precision@k, Recall@k and processing time. The paper claims FNFinRec outperforms the baselines on clustering quality and recommendation accuracy, with competitive processing times; the numeric support for those claims is presented almost entirely in figures rather than tabulated values.

## Problem and Motivation

Conventional financial services face accessibility, personalisation, reachability and information problems: user-interest patterns are only partially observed, so recommendations fail to capture individual interests and fail to adapt to changing market conditions (Abstract, p. 1). The author argues that prior recommendation algorithms which optimise only for diversity and accuracy are insufficient given the growing volume of user-activity data and the heterogeneity of individual interests (Sec. 1, p. 2). Classical K-means clustering struggles with large-scale data and noise because of its preset parameters and sensitivity to initial centroids, and the paper identifies data quality, scalability and real-time flexibility as recurring obstacles in the financial-recommendation literature (Sec. 2.2, p. 3). The stated response is a single pipeline that uses MapReduce on Hadoop for scalable processing, fuzzy K-means for uncertainty management, and neural collaborative filtering for real-time accuracy and adaptability (Sec. 2.2, p. 3). Three contributions are claimed: MapReduce-based processing of large financial datasets, fuzzy K-means clustering of users by interest pattern, and NCF-based adaptive recommendations (Sec. 1, pp. 1–2).

## Method

**Design.** Computational method-development study with comparative benchmark evaluation against four published algorithms (ANFIS, PRS-MPT, IFCM, K-L-KM); the authors state no formal design label.
**Sample.** Not reported — the paper never prints the number of user profiles or interaction records in the Kaggle "Finance data analysis" dataset it uses; the unit of analysis is a user profile (one row of a user-item interaction matrix) and, secondarily, a user–financial-service item pair.
**Context.** geography: the author is affiliated with Tianjin Sino-German University of Applied Sciences, China, but no country is stated for the data or the deployment; population: financial investors aged 21–35 with investment interests spanning mutual funds, equity market, debentures, government bonds, fixed deposits, PPF and gold (Table 1, p. 4); setting: virtual/computational — offline implementation and evaluation on a Hadoop/MapReduce platform, with no live financial-services deployment and no human participants reported.

- Assemble a user set U = {ur1, ur2, …, urm} and an item set I = {i1, i2, …, in}, then build the m×n interaction matrix R whose entry ruri records the interaction between user ur and item i (Sec. 3.1, Eq. 3, p. 3).
- Compute a financial risk score Ψ from investment preferences Pi and expected returns Ei as a weighted sum, and an investment-diversity score D as the entropy of the preference distribution (Sec. 3.1, Eq. 4, p. 3).
- Select features with a random-forest importance score, averaging the per-tree importance of feature j over T trees (Sec. 3.1, Eq. 5, p. 4).
- Preprocess and analyse the data on a Hadoop cluster with the MapReduce framework, splitting work into Map and Reduce stages so processing is parallel and aggregated (Sec. 3.2, p. 4).
- Cluster user profiles with fuzzy K-means by minimising the within-cluster variance objective Jm, with fuzziness parameter m > 1 (Sec. 3.3, Eq. 6, p. 5).
- Compute each user's degree of membership urij in cluster j from the ratio of Euclidean distances to the cluster centroids (Sec. 3.3, Eq. 7, p. 5).
- Update the cluster centroid cj as a membership-weighted mean of the data points, then iterate membership computation and centroid update until the centroid change Δcj falls below a threshold (Sec. 3.3, Eqs. 8–9, pp. 6–7).
- Evaluate cluster quality with the silhouette coefficient and the Davies–Bouldin Index (Sec. 3.3, Eqs. 10–12, p. 7).
- Build the binary user-item interaction matrix (rows users, columns investment avenues such as fixed deposits, mutual funds, equity, bonds, real estate and crypto), with 1 marking interest and 0 otherwise (Table 2, p. 7; Sec. 3.4, p. 8).
- Map each interacted avenue to a risk band — low for fixed deposits and bonds, medium for real estate and mutual funds, high for equity and cryptocurrency — and select among same-band avenues using predefined rules such as interaction frequency and avenue preference (Sec. 3.4, p. 8).
- Represent users and items as d-dimensional embeddings P ∈ ℝ^{m×d} and Q ∈ ℝ^{n×d}, then predict the interaction score via a multi-layer perceptron on the concatenated user and item embeddings (Sec. 3.4, Eqs. 13–14, p. 8).
- Train the NCF with binary cross-entropy for implicit feedback and MSE for explicit feedback, minimising the loss so predicted interest approaches actual interest (Sec. 3.4, Eqs. 15–17, pp. 8–9).
- Generate top-N recommendations per user by sorting predicted ratings and computing Precision@N and Recall@N (Sec. 3.5, Eqs. 18–20, p. 9).
- Use training settings of a fuzziness parameter m, a three-layer NCF, an embedding size of 64, and a top-five recommendation list (Sec. 4.1, p. 9).
- Collect user responses to recommendations through a feedback mechanism, periodically update the clusters on new data, and adjust recommendations against real-time market conditions (Sec. 3.4, p. 8).

## Software

- Hadoop platform with a MapReduce framework (version not reported) — processing and analysis of large financial datasets (Sec. 3.2, p. 4)
- Fuzzy K-means clustering (implementation not reported)
- Neural collaborative filtering with a multi-layer perceptron, three layers, embedding size 64 (Sec. 4.1, p. 9)
- ANFIS baseline implementation, compared in the evaluation (version not reported)
- PRS-MPT baseline implementation (version not reported)
- IFCM baseline implementation (version not reported)
- K-L-KM baseline implementation (version not reported)
- JMP and MATLAB, used by the ANFIS prior study [19] rather than by this paper, cited as context (Sec. 2.1, p. 2)
- Random-forest feature-importance scoring for feature selection (Sec. 3.1, Eq. 5, p. 4)

## Key Findings

- The paper reports no numbered results table with outcome statistics; the comparative results appear in Figs. 4–9 with captions and prose but without printed numeric values.
- Cluster 2 has the highest average silhouette score of 0.690 and is described as the most coherent and well-separated user group (Sec. 4.2.1, p. 9).
- The Davies–Bouldin Index trend line is said to decrease as the number of clusters increases, which the author reads as improving clustering quality; no DBI values are printed (Sec. 4.2.1, p. 10).
- FNFinRec is claimed to show better precision across a range of k values than the baselines, with accuracy potentially falling as k rises — a quantity/quality trade-off (Sec. 4.2.2, p. 11).
- FNFinRec is claimed to obtain consistently better recall than the baselines across all values of k, so more relevant financial products are captured in the top-k list (Sec. 4.2.2, p. 11).
- The MSE comparison in Fig. 6 is claimed to prove FNFinRec is more accurate than competing algorithms, but no MSE value is printed and the figure caption reads "mean average precision" (Sec. 4.2.2, p. 10–11).
- Processing time is discussed with a hypothetical: "If ANFIS requires 60 min to process data, while IFCM only takes 40 min, then IFCM must be more efficient"; no FNFinRec processing time is printed (Sec. 4.2.3, p. 12).
- Similarity computation complexity is claimed to be reduced from o(|u|²) in earlier methods to linear form (Sec. 4.2.3, p. 12).
- Study-sample attributes from Table 1: female 43.1%, male 56.1%; age category 21–35; expected returns in three bands of 10–20%, 20–30% and 30–40% (Table 1, p. 4).
- Training configuration: three NCF layers, embedding size 64, top-five recommendations, fuzziness parameter m > 1 (Sec. 4.1, p. 9; Sec. 3.3, p. 5).

## Key Figures and Tables

- Fig. 1 (p. 5): Overall working flow of FNFinRec — data intake → preprocessing → grouping (fuzzy K-means) → NCF → recommendation output → the pipeline order the paper claims as its integration contribution.
- Figs. (a) and (b) (p. 4): Investment duration analysis and investment monitoring frequency analysis — companion charts to Table 1 whose axis values are not printed in the converted text.
- Fig. 2 (p. 6): Flowchart of the fuzzy K-means clustering algorithm — membership computation, centroid update, convergence check.
- Fig. 3 (p. 6): Cluster centroid update — the membership-weighted centroid formula rendered as an illustration.
- Fig. 4 (p. 10): Clustering quality using silhouette coefficient — average silhouette score plotted by cluster label, with cluster 2 peaking at 0.690.
- Fig. 5 (p. 10): Clustering quality using Davies–Bouldin index scores for different clusters — DBI scores falling as cluster count rises.
- Fig. 6 (p. 11): Recommendation accuracy using mean average precision — MSE comparison across algorithms; the caption and text disagree on which metric is plotted.
- Fig. 7 (p. 12): Recommendation accuracy using Precision@k — FNFinRec above the baselines across k.
- Fig. 8 (p. 13): Recommendation accuracy using Recall@k — FNFinRec above the baselines across k.
- Fig. 9 (p. 13): Processing time analysis — execution times for FNFinRec, ANFIS, PRS-MPT, IFCM and K-L-KM.
- Table 1 (p. 4): Financial profile overview — gender 43.1% female / 56.1% male, age 21–35, features list, expected return bands 10–20%, 20–30%, 30–40%.
- Table 2 (p. 7): User-item interaction matrix — five users × six investment avenues, binary entries.
- Table 3 (p. 8): User investment preferences analysed by risk level — each user mapped to low, medium and high risk avenues.

## Definitions

- **FNFinRec** — Fuzzy Neural Financial Recommendation, the paper's proposed adaptive recommendation algorithm.
- **Fuzzy K-means** — A clustering method that allows each data point to belong to several clusters with a degree of membership, controlled by the fuzziness parameter m > 1.
- **Fuzziness parameter (m)** — Controls the degree of overlap between clusters; larger m means more overlap and users can belong to more than one cluster.
- **NCF** — Neural Collaborative Filtering, the recommendation approach that predicts user interest by learning embeddings and a multi-layer perceptron over user-item interactions.
- **User-item interaction matrix (R)** — An m×n matrix whose entries record whether a user has interacted with a financial product or service; used as the NCF input.
- **Silhouette coefficient** — A clustering-quality measure on [−1, 1], where values close to +1 signify well-separated clusters.
- **Davies–Bouldin Index (DBI)** — A cluster-separation measure based on within-cluster scatter relative to between-centroid distance; lower is better.
- **Precision@N / Recall@N** — Recommendation-accuracy metrics computed over the top-N recommended items for each user.
- **Ψ (financial risk score)** — A weighted sum of investment preferences Pi and expected returns Ei used to analyse user interest patterns.
- **D (investment diversity score)** — Entropy of the distribution of preferences across investment avenues.
- **ANFIS** — Adaptive Neural Fuzzy Inference System, an existing algorithm used as a baseline [19].
- **PRS-MPT** — Portfolio Recommender System based on Markowitz Modern Portfolio Theory, an existing algorithm used as a baseline [20].
- **IFCM** — Improved Fuzzy C-Means Multiview technique, an existing algorithm used as a baseline [22].
- **K-L-KM** — Kullback–Leibler K-Medoids, an existing algorithm used as a baseline [24].

## Key Equations

- `U = {ur1, ur2, .., urm}` — The user set (Sec. 3.1, Eq. 1).
- `I = {i1, i2, .., in}` — The financial-product/service item set (Sec. 3.1, Eq. 2).
- `Rm×n = [r11 … r1n ; … ; rm1 … rmn]` — The user-item interaction matrix (Sec. 3.1, Eq. 3).
- `D = −Σ pi log(pi)` — Investment diversity score as the entropy of the preference distribution (Sec. 3.1, Eq. 4).
- `Ij = (1/T) Σ_{t=1}^{T} Ij(t)` — Random-forest importance of feature j averaged over T trees (Sec. 3.1, Eq. 5).
- `Jm = Σ_{k=1}^{K} Σ_{i=1}^{m} ur^m_ik · ‖xk − ck‖²` — Fuzzy K-means objective minimising within-cluster variance (Sec. 3.3, Eq. 6).
- `urij = 1 / Σ_{k=1}^{K} (‖xi − cj‖ / ‖xi − ck‖)^{2/(m−1)}` — Membership of data point xi in cluster j (Sec. 3.3, Eq. 7).
- `cj = Σ ur^m_ij xi / Σ ur^m_ij` — Membership-weighted centroid update (Sec. 3.3, Eq. 8).
- `Δcj = ‖cj(new) − cj(old)‖` — Convergence check on centroid change (Sec. 3.3, Eq. 9).
- `DBI = (1/k) Σ_{i=1}^{K} max_{j≠i} ((Si + Sj) / d(centi + centj))` — Davies–Bouldin Index (Sec. 3.3, Eq. 10).
- `Si = (1/Ci) Σ_{x∈Ci} d(x, centi)` — Within-cluster scatter for cluster i (Sec. 3.3, Eq. 11).
- `Mij = ‖centi − centj‖` — Distance between cluster centroids (Sec. 3.3, Eq. 12).
- `r̂uri = f(pur, qi)` — Interaction prediction from user and item embeddings (Sec. 3.4, Eq. 13).
- `f(pur, qi) = MLP(f(pur ⊕ qi))` — MLP over concatenated user and item embeddings (Sec. 3.4, Eq. 14).
- `Yuri = 1 if user ur has invested in item i, else 0` — Implicit-feedback label (Sec. 3.4, Eq. 15).
- `L(Yuri) = Σ_{(ur,i)∈R} [ruri log r̂uri + (1 − ruri) log(1 − r̂uri)]` — Binary cross-entropy loss for implicit feedback (Sec. 3.4, Eq. 16).
- `L = (1/|R|) Σ_{(ur,i)∈R} |rur,i − r̂ur,i|²` — MSE loss for explicit feedback (Sec. 3.4, Eq. 17).
- `Top−Nur = argsort_i r̂ur [∶ N]` — Top-N recommendation generation (Sec. 3.5, Eq. 18).
- `pre@N = |{recitems} ∩ {relitems}| / N` — Precision at N (Sec. 3.5, Eq. 19).
- `Recall@N = |{recitems} ∩ {relitems}| / |{relitems}|` — Recall at N (Sec. 3.5, Eq. 20).
- `s(i) = (b(i) − a(i)) / max(a(i), b(i))` — Silhouette coefficient (Sec. 4.2.1, Eq. 21).
- `MSE = (1/|R|) Σ_{(ur,i)∈R} |rur,i − r̂ur,i|²` — Mean square error used for recommendation accuracy (Sec. 4.2.2, Eq. 22).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Study sample gender distribution, female | percentage | 43.1% | — | — | Table 1, p. 4 |
| Study sample gender distribution, male | percentage | 56.1% | — | — | Table 1, p. 4 |
| Study sample age category | age range | 21–35 | — | — | Table 1, p. 4 |
| Study sample expected return, band 1 | expected return | 10–20% | — | — | Table 1, p. 4 |
| Study sample expected return, band 2 | expected return | 20–30% | — | — | Table 1, p. 4 |
| Study sample expected return, band 3 | expected return | 30–40% | — | — | Table 1, p. 4 |
| Clustering quality, cluster 2, proposed FNFinRec | average silhouette score | 0.690 | — | — | Sec. 4.2.1, p. 9 |
| NCF model configuration, proposed FNFinRec | embedding size | 64 | — | — | Sec. 4.1, p. 9 |
| NCF model configuration, proposed FNFinRec | number of layers | 3 | — | — | Sec. 4.1, p. 9 |
| Recommendation list length, proposed FNFinRec | top-N recommendations | 5 | — | — | Sec. 4.1, p. 9 |
| Processing time, ANFIS baseline | minutes | 60 | — | — | Sec. 4.2.3, p. 12 |
| Processing time, IFCM baseline | minutes | 40 | — | — | Sec. 4.2.3, p. 12 |
| Clustering accuracy, prior study [11] | accuracy | over 70% | — | — | Sec. 1, p. 2 |
| Fund recommendation, prior study K-L-KM [24] | average KL similarity | 0.85 | — | — | Sec. 2.2, p. 3 |
| Fund recommendation, prior study K-L-KM [24] | RMSE | 0.93 to 0.94 | — | — | Sec. 2.2, p. 3 |
| Portfolio recommender dataset, prior study PRS-MPT [20] | number of Indian equities | 297 | — | — | Sec. 2.1, p. 2 |
| Fuzzy K-means time complexity | complexity | O(T × K × n × d) | — | — | Sec. 3.3, p. 7 |
| User similarity complexity, prior methods | complexity | o(\|u\|²) | — | — | Sec. 4.2.3, p. 12 |
| Similarity complexity after the proposed approach | complexity | linear form | — | — | Sec. 4.2.3, p. 12 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "The results show that the proposed FNFinRec algorithm outperforms existing methods regarding clustering quality and recommendation accuracy." | Abstract, p. 1 | model_performance_evaluation |
| "Cluster 2 has the highest average silhouette score of 0.690, making it the most coherent and well-separated adaptive financial recommendation system user group." | Sec. 4.2.1, p. 9 | model_performance_evaluation |
| "If ANFIS requires 60 min to process data, while IFCM only takes 40 min, then IFCM must be more efficient as shown in Fig. 9." | Sec. 4.2.3, p. 12 | model_performance_evaluation |
| "The study demonstrates its progressive nature in the test of real financial data, reaching a clustering accuracy of over 70% significant recommendation for subsequent financial analysis and user data management" | Sec. 1, p. 2 | model_performance_evaluation |
| "KL similarity is 0.85 accurate on average and RMSE ranges from 0.93 to 0.94." | Sec. 2.2, p. 3 | model_performance_evaluation |
| "Fuzzy K-means clustering is applied, in which fuzzy logic helps to handle uncertainties in financial data and clusters users with similar patterns." | Abstract, p. 1 | model_algorithm_integration |
| "The Neutral Collaborative Filtering (NCF) recommendation approach aims to predict user interests in financial products/services by learning from user interaction data." | Abstract, p. 1 | model_algorithm_integration |
| "Implemented on a Hadoop platform with a MapReduce framework, the FNFinRec ensures efficient processing of large datasets." | Abstract, p. 1 | system_development |
| "The suggested FNFinRec algorithm’s whole process flow is illustrated in this Fig. 1. Starting with the intake of data and progressing via preprocessing, grouping, and NCF, it culminates in the output of recommendations." | Sec. 3.1, p. 4 | model_algorithm_integration |
| "The silhouette coefficient is an evaluation tool for user interest pattern grouping, and it is helpful in more extensive data on intelligent investment strategies." | Sec. 4.2.1, p. 9 | model_performance_evaluation |
| "The research found that processing times can vary greatly across FNFinRec, ANFIS, PRS-MPT, IFCM, and K-L-KM." | Sec. 4.2.3, p. 12 | model_performance_evaluation |
| "The study proposes an automatic recommender system for investment types using adaptive fuzzy k means algorithm with neural architecture based on user feedback and improves decisions" | Sec. 1, p. 2 | model_algorithm_integration |
| "The model relies on past data, which may not accurately predict market trends or investor behavior." | Sec. 2.1, p. 2 | model_algorithm_integration |
| "Further research might look into making AI systems that are easier to understand and interact with more external data sources that are updated in real-time, such as social media and news." | Sec. 5, p. 13 | model_algorithm_integration |

## Limitations and Gaps

- The paper's own comparative results are reported almost entirely in figures (Figs. 4–9) with no printed numeric values for MSE, Precision@k or Recall@k, so the recommendation-accuracy claims cannot be read off or verified from the text. [unacknowledged]
- No sample size is printed anywhere: the Kaggle "Finance data analysis" dataset [25] is cited as the source, but neither the number of user profiles nor the number of interaction records is reported, and the train-test split is described only qualitatively. [unacknowledged]
- The silhouette score is printed for cluster 2 only (0.690); the scores for the other clusters and the overall mean are not printed, and Fig. 4 is described only qualitatively. [unacknowledged]
- The Davies–Bouldin Index discussion states only that "the trend line decreases" as clusters increase; no DBI value is printed for any cluster count, so the clustering-quality comparison against the baselines cannot be reconstructed. [unacknowledged]
- The processing-time comparison is offered as a hypothetical ("If ANFIS requires 60 min … while IFCM only takes 40 min"); FNFinRec's own processing time, and the processing times of PRS-MPT and K-L-KM, are not printed. [unacknowledged]
- The abstract states FNFinRec "outperforms existing methods," but no significance test, confidence interval, variance estimate, or per-fold result is reported anywhere in the paper for any metric. [unacknowledged]
- Fig. 6's caption reads "Recommendation accuracy using mean average precision" while the surrounding text and Eq. 22 discuss MSE; the plotted metric and the reported metric therefore disagree, and no value is printed to resolve it. [unacknowledged]
- The evaluation is entirely offline on a public Kaggle investment-preferences dataset with no live financial-services deployment, no human participants, and no Philippine data, so external validity to local PFM expense forecasting or budgeting is untested. [unacknowledged]
- The paper never reports precision, recall, F1 or MSE for the proposed FNFinRec and the four baselines in tabular form, so the "outperforms" claim rests on figure reading rather than on printed values. [unacknowledged]
- The authors acknowledge that conventional methods suffer data-quality, scalability and real-time-flexibility obstacles (Sec. 2.2, p. 3), and they acknowledge that further research is needed on explainable AI and integration with real-time external data sources such as social media and news (Sec. 5, p. 13).
- The authors acknowledge that dealing with the scale and complexity of financial big data, keeping computation efficient, and adapting to evolving user behaviour are major challenges that the algorithm resolves (Sec. 5, pp. 12–13), but they do not report measurements showing the size of those gains.

## Remember This

- FNFinRec is a fuzzy K-means plus neural collaborative filtering pipeline for financial product recommendation, implemented on Hadoop/MapReduce.
- The evaluation compares FNFinRec against ANFIS, PRS-MPT, IFCM and K-L-KM on silhouette coefficient, DBI, MSE, Precision@k, Recall@k and processing time.
- The best printed clustering result is cluster 2's average silhouette score of 0.690; no DBI, MSE, Precision@k or Recall@k value is printed anywhere.
- The processing-time comparison is hypothetical (ANFIS 60 min vs IFCM 40 min); FNFinRec's own time is not reported.
- Training configuration is three NCF layers, embedding size 64, top-five recommendations.
- The study sample has no reported N; Table 1 gives only 43.1% female / 56.1% male, age 21–35, and expected-return bands of 10–20%, 20–30%, 30–40%.
- Several literature-benchmark values are quoted in the paper (clustering accuracy over 70%, KL similarity 0.85, RMSE 0.93–0.94, 297 Indian equities) but they belong to prior studies, not to FNFinRec.

## Cited Works

- Luo, W. (2020) (context) — Optimised incremental clustering with kernels for investment recommendation; tested on Shanghai Stock Exchange stocks. [p. 2]
- Asemi, A.; Asemi, A.; Ko, A. (2023) (baseline) — ANFIS model using demographic profile and financial types with seven parameters to give adaptive investment recommendations; one of the four comparison algorithms. [p. 2]
- Sengupta, A.; Jana, P.; Dutta, P.N.; Mukherjee, I. (2024) (baseline) — PRS-MPT portfolio recommender using Modern Portfolio Theory, greedy algorithm and integer programming on 297 Indian equities; one of the four comparison algorithms. [p. 2]
- Li, L.; Wang, J.; Li, X. (2020) (context) — K-means evaluation of China Merchants Bank's Financial Capricorn Intelligence platform. [p. 2]
- Dandugala, L.S.; Vani, K.S. (2024) (baseline) — IFCM clustering with MobileNet V2 and 3L-BiLSTM on MapReduce/Hadoop; one of the four comparison algorithms. [p. 3]
- You, J. (2023) (context) — E-commerce recommendation combining big-data analysis with genetic fuzzy clustering; reports minimal MAE. [p. 3]
- Chiou-Wei, S.Z.; Lee, Y.T. (2024) (baseline) — K-L-KM fund recommendation using enhanced KL distance; reports average KL similarity 0.85 and RMSE 0.93–0.94; one of the four comparison algorithms. [p. 3]
- Li, Y.; Chu, X.; Tian, D.; Feng, J.; Mu, W. (2021) (methodology) — Customer segmentation with K-means and adaptive particle-swarm optimisation of cluster centres. [p. 2]
- Huang, L.; Lu, H. (2024) (methodology) — Intelligent financial data management system using higher-order hybrid clustering; reported clustering accuracy over 70%. [p. 2]
- Chen, Z.L. (2022) (methodology) — Clustering algorithm research for text big data, cited for handling noise and initial-centroid sensitivity. [p. 2]
- Sharaf, M.; Hemdan, E.E.D.; El-Sayed, A.; El-Bahnasawy, N.A. (2022) (context) — Survey of recommendation systems for financial services. [p. 2]
- Zare, H.; Emadi, S. (2020) (methodology) — Improved K-means for determining customer satisfaction with optimal cluster numbers and initial centres. [p. 2]
- Wan, H.; Yu, S. (2023) (methodology) — Recommendation system based on an adaptive learning cognitive map model. [p. 2]
- Leung, M.F.; Jawaid, A.; Ip, S.W.; Kwok, C.H.; Yan, S. (2023) (context) — Portfolio recommendation using machine learning and big-data analytics, linked to financial literacy gains. [p. 1]
- Datta, N. (2022) (methodology) — Kaggle "Finance data analysis" dataset (Version 1.0) supplying the financial profile data used in Table 1 and the interaction matrices. [p. 4]