---
paper_id: A--Pratama-2024
first_author: Pratama
year: 2024
title: "User Profiling Based on Financial Transaction Patterns: A Clustering Approach for User Segmentation"
venue: "International Journal for Applied Information Management"
doi: Not reported
designation: algorithm
status: extracted
modules: [data_collection, model_development, model_performance_evaluation, income_expense_management, model_algorithm_integration]
module_rationale:
  data_collection: "The dataset is sourced from Kaggle's 'Financial Transactions Dataset' generated with the Python Faker library (Sect. 3.1, p. 220)."
  model_development: "K-Means clustering is developed with feature extraction, Min-Max scaling/standardisation and label/one-hot encoding (Sect. 3.2, pp. 220-221; Sect. 3.3, p. 221)."
  model_performance_evaluation: "Clustering quality is evaluated with the Silhouette Score (0.33), PCA and t-SNE projections (Sect. 4.1, pp. 224-225)."
  income_expense_management: "The analysis segments users by transaction amount, time and type, i.e. transaction-level inflow/outflow tracking (Sect. 3.3, p. 221)."
  model_algorithm_integration: "K-Means is the core clustering algorithm integrated with feature extraction and dimensionality reduction (Sect. 3.3, p. 221)."
---

## Summary

The paper applies K-Means clustering to a simulated financial transaction dataset to segment users based on transaction amount, time, and type. Three clusters were identified: Cluster 0 (mean amount 1876.92, early-week purchases around 11:15 AM), Cluster 1 (mean amount 4147.06, mid-week transfers around 1:35 PM), and Cluster 2 (mean amount 1970.00, later-week purchases around 11:20 AM). The clustering quality is moderate, with a Silhouette Score of 0.33. The authors position the work as a contribution to user profiling and customer segmentation in financial services, arguing that transaction pattern analysis can improve targeted marketing, product personalisation, and customer retention. The study is limited to a single month of simulated data from a public Kaggle dataset, and the authors acknowledge the moderate cluster separation and the need for larger, more diverse datasets.

## Problem and Motivation

Financial institutions increasingly rely on transaction data to optimise services, detect fraud, and personalise offerings. Traditional user segmentation methods rely on historical transaction data and predefined categories, which may not capture evolving user behaviours, especially when historical data are sparse. The paper argues that clustering techniques, particularly K-Means, enable the discovery of hidden patterns in transaction data and can segment users by behaviour rather than by predefined categories. The motivation is to improve customer segmentation, marketing strategies, and financial product personalisation by analysing transaction amounts, times, and types. The authors also note that traditional fraud detection methods focus on broad patterns and miss unique behavioural traits, and that transaction data from diverse platforms show varied interaction patterns influenced by subjective norms and transaction conditions (Sect. 1, p. 218).

## Method

**Design.** Computational clustering study using K-Means; the authors state no formal design label.
**Sample.** N not reported; the unit of analysis is an individual financial transaction (Fig. 3, p. 223, shows approximately 15–20 transactions per cluster).
**Context.** geography: Not reported (dataset is simulated, no country stated); population: fictional financial institution's customers; setting: computational analysis of the Kaggle "Financial Transactions Dataset."

- Source the dataset from Kaggle's "Financial Transactions Dataset," generated with the Python Faker library, containing fields: transaction ID, amount, transaction type, customer ID, and transaction time (Sect. 3.1, p. 220).
- Preprocess: impute missing numerical values using mean or median, fill categorical columns with the most frequent value, remove rows with extensive missing data (Sect. 3.2, p. 220).
- Extract time features from transaction_time: day of week, month, and hour (Sect. 3.2, p. 221).
- Scale numerical features (amount) using Min-Max scaling or standardisation; encode categorical variables (transaction_type, customer_id) using one-hot encoding or label encoding (Sect. 3.2, p. 221).
- Apply K-Means clustering with Euclidean distance (Eq. 1, p. 221) and minimise within-cluster sum of squares (Eq. 2, p. 221).
- Select features for clustering: amount, transaction time (day of week, hour, month), and transaction type (Sect. 3.3, p. 221).
- Use the Silhouette Score to determine the optimal number of clusters, computed for different values of K (Sect. 3.3, p. 222).
- Visualise results with 3D scatter (Fig. 2, p. 223), bar chart (Fig. 3, p. 223), PCA (Fig. 4, p. 224), and t-SNE (Fig. 5, p. 224).
- The authors state K-Means advantages (simplicity, computational efficiency, large datasets) and limitations (dependence on K selection, sensitivity to centroid initialisation, assumption of spherical equal-sized clusters, struggles with outliers and varying density) (Sect. 3.3, p. 221).

## Key Findings

- Three clusters were identified with distinct transaction behaviours (Abstract, p. 217).
- Cluster 0: mean amount 1876.92, std 1143.21, mean hour 11.15, mean day of week 0.77 (Monday), mean month 1, predominantly purchases, amount range 500–4500 (Table 1, p. 222; Sect. 4.1, p. 222).
- Cluster 1: mean amount 4147.06, std 964.44, mean hour 13.59 (1:35 PM), mean day of week 3.12 (Wednesday), mean month 1, predominantly transfers, amount range 2000–6000 (Table 1, p. 222; Sect. 4.1, p. 222).
- Cluster 2: mean amount 1970, std 913.7, mean hour 11.2, mean day of week 4.85 (Friday), mean month 1, predominantly purchases, amount range 700–3500 (Table 1, p. 222; Sect. 4.1, p. 222).
- Silhouette Score of 0.33 indicates moderate clustering quality, with some overlap between clusters (Sect. 4.1, p. 225).
- Figure 3 shows Cluster 2 has the most transactions (just over 20), Cluster 1 around 17, and Cluster 0 just under 15 (Fig. 3, p. 223).
- PCA and t-SNE projections show clear separation between the three clusters (Fig. 4, p. 224; Fig. 5, p. 224).
- The authors suggest Cluster 1 could be targeted with premium financial products and Clusters 0 and 2 with tailored promotions during peak transaction times (Sect. 4.2, p. 225).
- Transaction type: Cluster 0 = Purchase, Cluster 1 = Transfer, Cluster 2 = Purchase (Table 2, p. 222).

## Software

- Python Faker library (dataset generation, Sect. 3.1, p. 220)
- K-Means clustering (implementation not specified)
- PCA (implementation not specified)
- t-SNE (implementation not specified)

## Key Figures and Tables

- Figure 1 (p. 220): Research methodology flow — data collection → preprocessing → clustering.
- Figure 2 (p. 223): 3D clustering of users by hour, amount, and cluster ID — shows three distinct clusters.
- Figure 3 (p. 223): Cluster distribution bar chart — Cluster 2 has most transactions, Cluster 0 has least.
- Figure 4 (p. 224): PCA projection — shows separation of clusters in reduced 2D space.
- Figure 5 (p. 224): t-SNE projection — shows cluster structure in reduced 2D space.
- Table 1 (p. 222): Cluster characteristics summary — mean amount, std amount, mean hour, mean day of week, mean month for each cluster.
- Table 2 (p. 222): Cluster statistical summary — same as Table 1 plus transaction type (Purchase/Transfer/Purchase).

## Limitations and Gaps

- The dataset is limited to a single month of transaction data, which may not capture long-term trends or seasonal variations (Sect. 4.2, p. 225). Acknowledged.
- The moderate Silhouette Score of 0.33 suggests overlap between clusters and potential misclassification (Sect. 4.1, p. 225). Acknowledged.
- The dataset is from a single public Kaggle source, simulated with Faker, and not drawn from a real financial institution, limiting external validity (Sect. 3.1, p. 220). [unacknowledged]
- The total number of transactions (N) is never reported, and cluster sizes are only approximated from a bar chart (Fig. 3, p. 223). [unacknowledged]
- Only K-Means is tested; no comparison with alternative clustering algorithms (e.g. DBSCAN, hierarchical) is performed, despite the authors noting DBSCAN as a potential improvement (Sect. 5, p. 226). [unacknowledged]
- No confidence intervals, p-values, or significance tests are reported for any cluster statistic. [unacknowledged]
- Transaction type is reported only as a single dominant type per cluster, with no distribution or counts. [unacknowledged]
- The paper does not report how many clusters K was tested for before selecting K=3, beyond stating the Silhouette Score was used (Sect. 3.3, p. 222). [unacknowledged]
- No demographic or geographic variables are included, which the authors acknowledge could refine segmentation (Sect. 4.2, p. 225). Acknowledged.
- The data is simulated with Faker, so findings may not reflect real user behaviour (Sect. 3.1, p. 220). [unacknowledged]
- The paper claims the dataset is "ideal" for customer behaviour analysis and fraud detection (Sect. 3.1, p. 220), but no fraud or behavioural ground truth is used to validate the clusters. [unacknowledged]

## Definitions

- **K-Means** — An unsupervised clustering algorithm that partitions data into K clusters based on proximity to cluster centroids (Sect. 3.3, p. 221).
- **Silhouette Score** — A metric ranging from -1 to +1 that evaluates how well each data point fits its assigned cluster, with higher values indicating better separation (Sect. 3.3, p. 222).
- **WCSS** — Within-cluster sum of squares, the objective function K-Means minimises (Eq. 2, p. 221).
- **Cluster 0** — Early-week purchase-focused cluster with moderate transaction amounts (Sect. 4.1, p. 222).
- **Cluster 1** — Mid-week transfer-focused cluster with high transaction amounts (Sect. 4.1, p. 222).
- **Cluster 2** — Later-week purchase-focused cluster with moderate transaction amounts (Sect. 4.1, p. 222).
- **PCA** — Principal Component Analysis, used to project clusters into 2D space (Fig. 4, p. 224).
- **t-SNE** — t-Distributed Stochastic Neighbor Embedding, used to project clusters into 2D space (Fig. 5, p. 224).

## Key Equations

- `d(x_i, C_j) = √(Σ_{k=1}^{n} (x_{i,k} − c_{j,k})²)` — Euclidean distance between data point x_i and centroid C_j (Eq. 1, p. 221).
- `WCSS = Σ_{i=1}^{K} Σ_{x_i ∈ C_k} (x_i, c_k)²` — Within-cluster sum of squares (Eq. 2, p. 221).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Cluster 0 mean transaction amount | mean_amount | 1876.92 | — | — | Table 1, p. 222 |
| Cluster 1 mean transaction amount | mean_amount | 4147.06 | — | — | Table 1, p. 222 |
| Cluster 2 mean transaction amount | mean_amount | 1970 | — | — | Table 1, p. 222 |
| Cluster 0 std transaction amount | std_amount | 1143.21 | — | — | Table 1, p. 222 |
| Cluster 1 std transaction amount | std_amount | 964.44 | — | — | Table 1, p. 222 |
| Cluster 2 std transaction amount | std_amount | 913.7 | — | — | Table 1, p. 222 |
| Cluster 0 mean hour of transaction | mean_hour | 11.15 | — | — | Table 1, p. 222 |
| Cluster 1 mean hour of transaction | mean_hour | 13.59 | — | — | Table 1, p. 222 |
| Cluster 2 mean hour of transaction | mean_hour | 11.2 | — | — | Table 1, p. 222 |
| Cluster 0 mean day of week | mean_day_of_week | 0.77 | — | — | Table 1, p. 222 |
| Cluster 1 mean day of week | mean_day_of_week | 3.12 | — | — | Table 1, p. 222 |
| Cluster 2 mean day of week | mean_day_of_week | 4.85 | — | — | Table 1, p. 222 |
| Cluster 0 mean month | mean_month | 1 | — | — | Table 1, p. 222 |
| Cluster 1 mean month | mean_month | 1 | — | — | Table 1, p. 222 |
| Cluster 2 mean month | mean_month | 1 | — | — | Table 1, p. 222 |
| Clustering quality | Silhouette Score | 0.33 | — | — | Sect. 4.1, p. 225 |
| Cluster 0 transaction amount range | min–max | 500 to 4500 | — | — | Sect. 4.1, p. 222 |
| Cluster 1 transaction amount range | min–max | 2000 to 6000 | — | — | Sect. 4.1, p. 222 |
| Cluster 2 transaction amount range | min–max | 700 to 3500 | — | — | Sect. 4.1, p. 222 |
| Cluster 0 transaction count (approx.) | count | just under 15 | — | — | Fig. 3, p. 223 |
| Cluster 1 transaction count (approx.) | count | around 17 | — | — | Fig. 3, p. 223 |
| Cluster 2 transaction count (approx.) | count | just over 20 | — | — | Fig. 3, p. 223 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "This study uses clustering techniques, specifically K-means, to analyze transaction data and segment users based on transaction amounts, times, and types." | Abstract, p. 217 | model_algorithm_integration |
| "Three clusters were identified, each demonstrating distinct transaction behaviors." | Abstract, p. 217 | model_algorithm_integration |
| "The study also highlights the importance of improving clustering accuracy, as indicated by the moderate Silhouette Score of 0.33." | Abstract, p. 217 | model_performance_evaluation |
| "The K-Means algorithm is one of the most widely used clustering techniques in unsupervised machine learning." | Sect. 3.3, p. 221 | model_algorithm_integration |
| "Amount, representing the monetary value of each transaction, is an essential feature as it helps group users based on their spending habits, distinguishing between high spenders and low spenders." | Sect. 3.3, p. 221 | income_expense_management |
| "The Silhouette Score is an effective method for determining the optimal number of clusters in clustering algorithms like K-Means." | Sect. 3.3, p. 222 | model_performance_evaluation |
| "With a score of 0.33, the clustering is neither exceptionally good nor poor." | Sect. 4.1, p. 225 | model_performance_evaluation |
| "Cluster 1, on the other hand, has the highest average transaction amount at 4147.06, with a standard deviation of 964.44, indicating a higher variation in transaction sizes." | Sect. 4.1, p. 222 | model_performance_evaluation |
| "Additionally, the dataset used in this analysis is limited to a single month of transaction data, which may not capture long-term trends or seasonal variations in transaction behavior." | Sect. 4.2, p. 225 | data_collection |
| "This research highlights the potential of clustering techniques, particularly K-means, in understanding complex user behaviors in financial transactions." | Sect. 5, p. 226 | model_algorithm_integration |
| "Future studies could include a more extended time period and incorporate other factors, such as geographic location, socio-economic status, or account types." | Sect. 4.2, p. 225 | data_collection |
| "The average day of the week for transactions in this cluster is 0.77, which likely corresponds to Monday." | Sect. 4.1, p. 222 | income_expense_management |

## Remember This

- K-Means clustering identified three user segments from financial transaction data: early-week purchases (Cluster 0), mid-week transfers (Cluster 1), and later-week purchases (Cluster 2).
- Cluster 1 has the highest mean transaction amount (4147.06) and is dominated by transfers.
- Silhouette Score of 0.33 indicates moderate cluster quality with some overlap.
- Dataset is a single-month simulated Kaggle dataset; N is not reported.
- The study is an algorithm paper using K-Means, PCA, and t-SNE, with no real financial institution data.
- The authors recommend density-based techniques like DBSCAN for future refinement (Sect. 5, p. 226).

## Cited Works

- Zhang, Z., Chen, L., Liu, Q., & Wang, P. (2020) — Fraud detection method for low-frequency transactions using DBSCAN clustering [8].
- Zhao, H., Luo, X., Ma, R., & Xi, L. (2021) — Extended regularized K-means for high-dimensional customer segmentation with correlated variables [28].
- Martinovska, C., Stojkovic, N., Kosturanova, E., & Klekovska, M. (2021) — Data mining in client-oriented businesses; clustering algorithm selection for decision-making [27].
- Bilgiç, E., Çakır, Ö., Kantardzic, M., Duan, Y., & Cao, G. (2021) — Retail analytics: store segmentation using rule-based purchasing behaviour analysis [29].
- Komati, D. (2025) — Machine learning architectures for real-time financial decision systems [30].
- Chen, Q. (2024) — Application of K-Means algorithm in marketing [25].
- Eckhardt, C. M., et al. (2022) — Unsupervised machine learning methods and emerging applications in healthcare [26].
- Adeniran, I. A., et al. (2024) — Data-driven approaches to improve customer experience in banking [6].