---
paper_id: A--Yachamaneni-2025
first_author: Yachamaneni
year: 2025
title: "Credit Card Customer Profiling Using Self-Supervised Representation Learning on Multi-Source Financial Data"
venue: "International Journal of Artificial Intelligence, Data Science, and Machine Learning"
doi: 10.63282/3050-9262.IJAIDSML-V6I1P118
designation: algorithm
status: extracted
modules: [model_algorithm_integration, model_development, model_performance_evaluation]
module_rationale:
  model_algorithm_integration: "The paper presents a unified SSL framework combining contrastive learning, transformer encoders, MLP heads, and a clustering layer into a single pipeline for multi-source financial data (Sect. 3.4-3.5, pp. 169-170)."
  model_development: "The paper details the training workflow including pretext tasks (masked attribute forecasting, time series forecasting, AVP), contrastive learning objective, and feature aggregation (Sect. 3.4, p. 169)."
  model_performance_evaluation: "The paper evaluates the SSL model against K-Means and XGBoost on Silhouette Score, AUC (credit risk), and F1 (churn prediction) (Table 1, p. 171)."
---

## Summary

The paper proposes a self-supervised learning (SSL) framework for credit card customer profiling that integrates multi-source financial data — transaction logs, customer demographics, credit bureau reports, and online banking activity — into a single analytical model. The method uses contrastive learning and transformer-based architectures to learn robust feature embeddings from unlabeled data, avoiding the need for large labeled datasets. The framework is evaluated on a real-world dataset of 100,000 customer records against two baselines, K-Means and XGBoost, across three tasks: clustering quality (Silhouette Score), credit risk prediction (AUC), and churn prediction (F1-Score). The SSL model outperforms both baselines on all three metrics, achieving a Silhouette Score of 0.56, an AUC of 0.91, and an F1-Score of 0.81. An ablation study shows that temporal encoding contributes most to credit risk prediction performance (4.2% AUC drop when removed), followed by web activity features (3.8%) and the pretext task module (2.7%). The authors position SSL as a scalable, privacy-friendly alternative to traditional supervised profiling in financial services.

## Problem and Motivation

Traditional credit card customer profiling relies on supervised machine learning algorithms trained on hand-engineered features from demographic, transactional, and credit history data. These methods face three principal constraints. First, they require large amounts of labeled data, which is costly, time-consuming, and often unavailable due to privacy regulations such as GDPR and CCPA. Second, customer data is typically siloed across disconnected systems — transactional logs, demographic databases, credit bureau records, and web interaction logs are stored separately, preventing the formation of a holistic customer profile. Third, supervised models tend to overfit to their training distribution and struggle to generalize across changing customer behavior, macroeconomic conditions, or policy shifts, leading to data drift that requires constant retraining.

The authors argue that self-supervised learning (SSL) addresses these gaps by learning meaningful representations from unlabeled data through pretext tasks. SSL has already demonstrated success in computer vision and natural language processing, and the paper aims to extend it to heterogeneous, multi-modal financial data for customer profiling. The motivation is to develop a scalable, flexible, and privacy-friendly method that can extract rich behavioral patterns without relying on manual labels. The paper identifies a specific gap: little work has applied SSL to heterogeneous financial data consisting of transactional, demographic, and behavioral modalities, and existing models often fail to exploit temporal and contextual cues such as transaction timing or sequence.

## Method

**Design.** Computational method-development study with comparative benchmark evaluation against two published baselines (K-Means and XGBoost); the authors state no formal design label.

**Sample.** n = 100,000 customer records (privately owned banking company, data collected until February 2025, four data sources: transactional logs, demographics, credit bureau records, and web activity; dataset split 80% training, 10% validation, 10% testing).

**Context.** geography: Not reported (no country or region stated; the data comes from a privately owned banking company); population: Credit card customers of a privately owned banking company; setting: High-performance computing environment with two NVIDIA A100 GPUs and 512GB RAM; no live deployment or human participants.

The method is a multi-stage pipeline. **Data preprocessing** cleans and transforms raw financial data into a structured form, handling missing data, scaling continuous variables (min-max or z-score normalization), encoding categorical attributes as dense embeddings, and synchronizing temporal information across modalities. **Multi-modal feature encoding** uses separate encoders for each data type: temporal encoders for transactional sequences and feedforward layers for static demographic features, mapping raw inputs to a common latent space while retaining modality-specific information. The **SSL pretext task unit** trains the model without labels using contrastive learning, masked attribute reconstruction, time series forecasting, and augmented view prediction (AVP). **Feature aggregation** pools the modality-specific representations into a single unified representation using attention mechanisms or weighted averaging. Finally, **downstream task heads** feed the aggregated representation into task-specific heads for customer segmentation, risk scoring, and churn prediction, fine-tuned with labeled data.

The SSL design includes three pretext tasks. **Masked attribute forecasting** randomly occludes input features and trains the model to predict the occluded values, motivated by BERT-style training to capture contextual relationships among features. **Time series forecasting** randomly permutes a sequence of events (transaction records or web interactions) and trains the model to predict the correct order, helping it capture time-related dependencies. **Augmented view prediction (AVP)** augments the same data point multiple times (adding noise, removing features, random permutations) and trains the model to identify or match these augmentations, learning invariances to small distortions and enhancing generalization.

The **contrastive learning objective** teaches the model to differentiate between comparable and dissimilar data without explicit labels. Given two augmented views of a data instance, the goal is to maximize the cosine similarity of their representations while minimizing similarity with representations of other instances in the batch. Logits are passed through a temperature parameter before the softmax function, adjusting the sharpness of the output distribution and encouraging the model to learn discriminating features by drawing positive pairs nearer and pushing negatives further apart in the embedding space.

The **model architecture** centers on a Transformer encoder with self-attention for sequential data processing. The encoder extracts temporal dependencies from time-series data such as transaction records or web logs. Its multi-head attention enables different heads to attend to various regions of the sequence, learning complex and context-sensitive representations. An **MLP head** refines and aggregates the learned features through one or more fully connected layers with non-linear activations, normalizing high-dimensional embeddings into task-specific representations for risk scoring, purchase prediction, or fraud detection. A **clustering layer** on top of the learned feature representations generates interpretable customer profiles using K-Means or deep clustering, segmenting customers with similar encoded behaviors and attributes.

Evaluation uses a multi-metric assessment. For clustering, the paper uses the **Silhouette Score** (measures intra-cluster cohesion and inter-cluster separation; higher is better) and the **Davies-Bouldin Index** (measures average similarity of each cluster with its closest one; lower is better). For supervised classification, it uses **F1-Score** (balances precision and recall, useful for imbalanced responses), **AUC** (threshold-free measure of class separation), and **Accuracy** (proportion of correctly predicted instances). Precision and recall are also defined and discussed. The dataset is split into 80% training, 10% validation, and 10% testing to avoid data leakage. Training and experimentation run on two NVIDIA A100 GPUs with 512GB RAM.

## Key Findings

- The proposed SSL model achieves a Silhouette Score of 0.56, an AUC of 0.91 for credit risk prediction, and an F1-Score of 0.81 for churn prediction, outperforming both K-Means (0.35, 0.71, 0.58) and XGBoost (0.41, 0.84, 0.69) on every metric (Table 1, p. 171).
- K-Means, used as a control clustering algorithm, produces weak and overlapping clusters (Silhouette 0.35) and limited predictive capability (AUC 0.71, F1 0.58 for churn, F1 0.36 for credit risk) (Sect. 4.4, p. 171).
- XGBoost, a supervised learning algorithm, performs better than K-Means in classification (AUC 0.84, F1 0.69) but only moderately improves clustering quality (Silhouette 0.41) (Sect. 4.4, p. 171).
- The ablation study shows that removing temporal encoding causes the largest AUC drop (4.2%), followed by removing web activity features (3.8%) and removing the pretext task module (2.7%) (Table 2, p. 171).
- The SSL model's performance advantage is attributed to learning rich, generalizing representations from unlabeled data through pretext tasks and temporal encoding, beating both clustering and supervised methods (Sect. 4.4, p. 171).
- The dataset comprises 100,000 customer records from four data sources, split 80% training, 10% validation, and 10% testing (Sect. 4.1, p. 170).
- The paper claims the framework outperforms baselines in "profiling accuracy, clustering performance, and downstream tasks" (Abstract, p. 164), but no separate profiling accuracy metric is reported in the results.

## Key Figures and Tables

- Figure 1 (p. 164): Credit Card Fraud Detection System Using ML-Based Scoring Engine — introduces the fraud detection context, though the paper's focus is customer profiling.
- Figure 2 (p. 165): Emergence of Self-Supervised Learning (SSL) — outlines SSL definition, core principles, other domain success, applicability to financial data, benefits, and research/industry profession.
- Figure 3 (p. 166): Challenges in Traditional Approaches — constraints to data labeling, isolated data sources, and limited generalization.
- Figure 4 (p. 167): System Architecture — data preprocessing, multi-modal feature encoding, SSL pretext task unit, feature aggregation, and downstream task heads.
- Figure 5 (p. 168): Data Sources — transaction logs, demographics, credit bureau reports, and web activity.
- Figure 6 (p. 168): Feature Engineering — numerical normalization, categorical embeddings, and temporal encoding.
- Figure 7 (p. 169): Self-Supervised Learning Design — contrastive learning objective and pretext tasks.
- Figure 8 (p. 170): Model Architecture — Transformer encoder, MLP head, and clustering layer.
- Figure 9 (p. 171): Graph representing Quantitative Results — bar chart comparing K-Means, XGBoost, and Proposed SSL on Silhouette, AUC, and F1.
- Figure 10 (p. 172): Graph representing Ablation Study Results — bar chart of AUC drop for temporal encoding, web activity, and pretext task removal.
- Table 1 (p. 171): Quantitative Results — Silhouette, AUC (Credit Risk), and F1 (Churn Prediction) for Baseline (K-Means), XGBoost, and Proposed SSL.
- Table 2 (p. 171): Ablation Study Results — AUC Drop for Temporal Encoding (4.2%), Web Activity (3.8%), and Pretext Task (2.7%).

## Limitations and Gaps

- The authors acknowledge that interpretability remains a concern, particularly in regulated industries where transparency is imperative (Sect. 2.4, p. 167).
- The authors acknowledge that existing models do not fully utilise temporal and contextual cues present in customer behaviour, such as the time of day of the transaction or scenario (Sect. 2.4, p. 167).
- The authors suggest future work on federated learning, cross-bank consortium datasets, and reinforcement learning for adaptive personalization (Sect. 5, pp. 172-173).
- [unacknowledged] No confidence intervals, p-values, or statistical significance tests are reported for any of the quantitative results, so the claimed superiority of the SSL model is not statistically established.
- [unacknowledged] The Davies-Bouldin Index is named as a clustering metric in Sect. 4.2 (p. 170) but no value is reported anywhere in the results.
- [unacknowledged] Accuracy and precision/recall are named as evaluation metrics in Sect. 4.2 (p. 170) but no values are reported in Table 1 or the text.
- [unacknowledged] The dataset comes from a single privately owned banking company; no external validation or cross-institution testing is reported, so generalizability is untested.
- [unacknowledged] The number of clusters used for the Silhouette Score calculation is not reported, making the clustering results difficult to interpret or reproduce.
- [unacknowledged] The ablation study only measures AUC drop for credit risk prediction; the effect of module removal on clustering quality or churn prediction is not reported.
- [unacknowledged] The paper reports 100,000 records but does not state the number of features, the class distribution, or how missing data were handled in preprocessing.
- [unacknowledged] The paper's abstract claims "profiling accuracy" as an outcome, but no accuracy metric appears in the results, creating a mismatch between claimed and reported outcomes.
- [unacknowledged] Sections 4.3 and 4.4 are both titled "Quantitative Results," suggesting a duplication error in the manuscript.
- [unacknowledged] Figure 1 is labeled "Credit Card Fraud Detection System Using ML-Based Scoring Engine," which is not the paper's focus (customer profiling), suggesting a possible template or figure mismatch.
- [unacknowledged] No computational training time, energy cost, or model size is reported, limiting assessment of practical scalability.

## Definitions

- **Self-Supervised Learning (SSL)** — A machine learning paradigm where models learn meaningful representations from unlabeled data by solving auxiliary or pretext tasks, avoiding the need for human annotation (Sect. 1.1, p. 165).
- **Contrastive Learning** — An SSL objective that maximizes cosine similarity between representations of augmented views of the same instance while minimizing similarity with other instances in the batch (Sect. 3.4.1, p. 169).
- **Pretext Tasks** — Auxiliary tasks such as masked attribute forecasting, time series forecasting, and augmented view prediction (AVP) used to train the model without labels (Sect. 3.4.2, p. 169).
- **Transformer Encoder** — A self-attention-based architecture that extracts temporal dependencies from sequential data such as transaction records or web logs (Sect. 3.5, p. 169).
- **MLP Head** — A multi-layer perceptron that refines and aggregates learned features into task-specific representations for downstream work like risk scoring or fraud detection (Sect. 3.5, p. 170).
- **Clustering Layer** — A layer applied on top of learned feature representations to generate interpretable customer profiles using K-Means or deep clustering (Sect. 3.5, p. 170).
- **Silhouette Score** — A clustering metric measuring intra-cluster cohesion and inter-cluster separation; higher values indicate better-defined clusters (Sect. 4.2, p. 170).
- **Davies-Bouldin Index** — A clustering metric measuring average similarity of each cluster with its closest one; lower values indicate better clustering (Sect. 4.2, p. 170).
- **AUC** — Area Under the Receiver Operating Characteristic Curve, a threshold-free measure of how well a model separates classes (Sect. 4.2, p. 170).
- **F1-Score** — A classification metric balancing precision and recall, useful for imbalanced responses (Sect. 4.2, p. 170).
- **AVP (Augmented View Prediction)** — A pretext task where the same data point is augmented multiple times and the model learns to identify or match these augmentations (Sect. 3.4.2, p. 169).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Customer segmentation clustering quality, Baseline (K-Means) | Silhouette Score | 0.35 | — | — | Table 1, p. 171 |
| Credit risk prediction, Baseline (K-Means) | AUC | 0.71 | — | — | Table 1, p. 171 |
| Churn prediction, Baseline (K-Means) | F1-Score | 0.58 | — | — | Table 1, p. 171 |
| Credit risk prediction, Baseline (K-Means) | F1-Score | 0.36 | — | — | Sect. 4.4, p. 171 |
| Customer segmentation clustering quality, XGBoost | Silhouette Score | 0.41 | — | — | Table 1, p. 171 |
| Credit risk prediction, XGBoost | AUC | 0.84 | — | — | Table 1, p. 171 |
| Churn prediction, XGBoost | F1-Score | 0.69 | — | — | Table 1, p. 171 |
| Customer segmentation clustering quality, Proposed SSL | Silhouette Score | 0.56 | — | — | Table 1, p. 171 |
| Credit risk prediction, Proposed SSL | AUC | 0.91 | — | — | Table 1, p. 171 |
| Churn prediction, Proposed SSL | F1-Score | 0.81 | — | — | Table 1, p. 171 |
| Ablation: removal of Temporal Encoding | AUC Drop | 4.2% | — | — | Table 2, p. 171 |
| Ablation: removal of Web Activity | AUC Drop | 3.8% | — | — | Table 2, p. 171 |
| Ablation: removal of Pretext Task | AUC Drop | 2.7% | — | — | Table 2, p. 171 |
| Evaluation sample size | records | 100,000 | — | — | Sect. 4.1, p. 170 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "This paper presents an original scheme for credit card customer profiling based on self-supervised representation learning and financial data from multiple sources." | Abstract, p. 164 | model_algorithm_integration |
| "Traditional methods depend largely on supervised learning, which has to be based on large labeled data points." | Abstract, p. 164 | model_algorithm_integration |
| "Self-Supervised Learning (SSL) is a field in machine learning in which models are trained to learn meaningful representations of unlabeled training data through solving auxiliary or alternate (pretext) tasks." | Sect. 1.1, p. 165 | model_development |
| "The model is trained using Self-Supervised Learning (SSL) module and does not require labeled data." | Sect. 3.1, p. 167 | model_development |
| "The SSL model presented outperformed all baselines on every one of the metrics, which proves the worth of learning through multi-modal signals in a label-efficient way." | Sect. 4.4, p. 171 | model_performance_evaluation |
| "Temporal Encoding: The removal of temporal encoding led to the greatest decline in performance, whereby the AUC slumped by 4.2%." | Sect. 4.5, p. 172 | model_performance_evaluation |
| "The sample consisted of 100,000 records of customers of a privately owned banking company, where data was collected until February 2025." | Sect. 4.1, p. 170 | model_development |
| "It was multi-modal data, including four sources of information: transactional logs, demographics information, credit bureau records and traces of web activity." | Sect. 4.1, p. 170 | model_algorithm_integration |
| "The encoder extracts temporal dependencies from time-series data, such as transaction data or weblogs." | Sect. 3.5, p. 169 | model_algorithm_integration |
| "The framework suggested was based on using multi-source data, including transaction logs, demographic information, credit bureau reports, and web activity, compiled to create comprehensive representations of the customers." | Sect. 5, p. 172 | model_algorithm_integration |

## Remember This

- The paper proposes an SSL framework for credit card customer profiling using multi-source data: transaction logs, demographics, credit bureau reports, and web activity.
- Evaluation uses 100,000 customer records from a private bank, split 80/10/10, against K-Means and XGBoost baselines.
- The SSL model achieves Silhouette 0.56, AUC 0.91 (credit risk), and F1 0.81 (churn), outperforming both baselines on every metric.
- The ablation study shows temporal encoding is the most important module (4.2% AUC drop when removed), followed by web activity (3.8%) and pretext task (2.7%).
- No confidence intervals, p-values, or significance tests are reported for any result.
- The Davies-Bouldin Index, accuracy, precision, and recall are named as metrics but never reported.

## Cited Works

- MacQueen, J. (1967) — K-Means clustering, cited as a traditional customer profiling technique (Sect. 2.1, p. 166).
- Reynolds, D. (2009) — Gaussian mixture models, cited alongside K-Means for traditional profiling (Sect. 2.1, p. 166).
- Quinlan, J. R. (1986) — Decision trees, cited for overfitting on small or noisy data (Sect. 2.1, p. 166).
- Breiman, L. (2001) — Random forests, cited as a supervised machine learning algorithm for financial tasks (Sect. 2.2, p. 166).
- Chen, T., & Guestrin, C. (2016) — XGBoost, cited as a scalable tree-boosting system and used as a baseline in this paper (Sect. 2.2, p. 166).
- Chen, X., Fan, H., Girshick, R., & He, K. (2020) — MoCo, cited for contrastive learning success in computer vision (Sect. 2.3, p. 167).
- Chen, T., Kornblith, S., Norouzi, M., & Hinton, G. (2020) — SimCLR, cited for contrastive learning of visual representations (Sect. 2.3, p. 167).
- Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019) — BERT, cited for transformer-based pre-training on unlabeled text (Sect. 2.3, p. 167).
- Somepalli, G., Goldblum, M., Schwarzschild, A., Bruss, C. B., & Goldstein, T. (2021) — SAINT, cited for row attention and contrastive pre-training on tabular data (Sect. 2.3, p. 167).
- Liu, X., Zhang, F., Hou, Z., Mian, L., Wang, Z., Zhang, J., & Tang, J. (2021) — Self-supervised learning: generative or contrastive, cited for SSL on transactions (Sect. 2.3, p. 167).