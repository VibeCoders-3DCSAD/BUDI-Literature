---
paper_id: A--ZhangEtAl-2023
first_author: Zhang
year: 2023
title: "An Experimental Evaluation of Anomaly Detection in Time Series"
venue: "Proceedings of the VLDB Endowment"
doi: 10.14778/3632093.3632110
designation: algorithm
status: extracted
modules: [model_performance_evaluation, model_algorithm_integration, data_collection]
module_rationale:
  model_performance_evaluation: "The paper's core contribution is a systematic intra- and inter-class benchmark of seventeen anomaly detection algorithms under point and range metrics (Sect. 4.1.2 Evaluation Metrics, Tables 4-7)."
  model_algorithm_integration: "It compares and combines method classes directly — running univariate methods per dimension and merging their outputs, and testing online against batch detectors — reporting a pipeline-level performance analysis (Sect. 4.3.1, Table 5; Sect. 4.3.2, Figure 11)."
  data_collection: "The evaluation data are sourced from named public benchmarks (Numenta, Exathlon, TODS) plus self-generated synthetic series with controlled anomaly patterns, documented per dataset in Sect. 4.1.1 and Table 3."
---

# A--ZhangEtAl-2023 — An Experimental Evaluation of Anomaly Detection in Time Series

## Summary

This paper is a benchmark and comparative evaluation study rather than a new detector. The authors propose a taxonomy of time series anomaly detection (TAD) methods along three facets — data dimension (univariate/multivariate), processing technique (batch/online), and anomaly type (point/subsequence) — with six inner classes, then run systematic intra-class and inter-class experiments on seventeen state-of-the-art algorithms. Ten of the seventeen are re-implemented in JAVA, all are refactored under one code structure, and a common testing framework is built to remove implementation confounds. Evaluation uses a point metric (precision/recall/F-measure) and a range metric designed for subsequence anomalies, across real-world and synthetic datasets with varied anomaly rates, data sizes, dimensions, anomaly patterns and threshold settings. The paper's headline practical results are that no method dominates across all cases, that deep learning methods do not outperform classical methods on datasets with complex anomaly patterns, that point methods can serve subsequence anomaly data with extreme global values, and that the widely used point-adjust adjustment inflates reported accuracy and can reverse method rankings.

## Problem and Motivation

The paper identifies three obstacles to selecting a suitable TAD method for a real application. First, time series data are complex and diverse — a series may be univariate or multivariate, and anomalies differ in type — yet proposed algorithms each tend to target one specific case; the paper notes that [25] can only find anomalous data points in univariate series while [7] handles univariate streams but only detects anomalous patterns of a fixed length (Sect. 1, p. 483). Second, there is a lack of thorough testing with the same datasets on the same platform and with the same metrics; different works compute even the basic precision-recall-F1 differently, and baselines may be written in different languages or use different data structures (Sect. 1, p. 483). Third, some recent papers evaluate point methods under point metrics on datasets whose anomalies are actually subsequences and then modify predictions with the point-adjust method before evaluation, so the effects of those measures have not been analysed; efficiency trade-offs at high dimension and large scale, the option of running univariate models per dimension, and the degree to which online detectors approximate batch methods also remain untested (Sect. 1, pp. 483-484).

The authors position the work against eight prior experimental surveys (Table 1, p. 484), arguing that DODDS, MD, TUD, TODS, Exathlon, TSB-UAD, Meta and HPI each leave at least one of the three facets, threshold robustness, or an application guideline untouched.

## Method

**Design.** The authors state no formal design label; the paper is a systematic experimental benchmark study with a proposed taxonomy, a re-implementation effort, and intra-class plus inter-class comparative evaluation.

**Sample.** 17 state-of-the-art anomaly detection algorithms (11 of 17 published since 2020; 12 of 17 not compared in the prior surveys reviewed in Sect. 1.2), evaluated over 15 real-world datasets (7 point, 8 subsequence) and 10 synthetic dataset configurations; the unit of analysis is one algorithm's detection result on one dataset.

**Context.** geography: Not reported — the evaluation uses public labelled benchmarks (Yahoo, Twitter, SMTP, DLR, ECG, Power, Sed, Taxi, Machine, Exercise, Exathlon, Swat, Smd) with no country stated for any dataset; population: Not applicable — the units are time series observations, not human participants; setting: Computational — a Windows 10 server with a 3.79GHz 12-core CPU and 128GB RAM, deep-learning methods run on GPU without efficiency comparison while all others are tested under a single-core environment for running-time comparison (Sect. 4.1, p. 487).

Key design features of the study:

- Taxonomy with three facets and six inner classes (Figure 1, p. 485): data dimension (univariate, multivariate), processing technique (batch, online), anomaly type (point, subsequence), with inner classes including distance-based, pattern-based, and deep-learning-based detection.
- Seventeen algorithms selected across the classes: distance-based NETS [66], STARE [67]; pattern/subsequence NP [24], MERLIN [42], PBAD [19], LRRDS [26], SAND [7], NormA [6], GrammarViz [50], IDK [55]; point-based SHESD [25]; deep-learning BeatGAN [39], Omni [52], USAD [3], GDN [17], RCoder [1], TranAD [58] (Table 2, p. 486).
- Ten methods re-implemented in JAVA, all methods refactored to the same code structure, and a testing framework built "to avoid the potential impact" of implementation differences (Sect. 1.1, p. 484; Sect. 3.4, p. 487).
- POT (automatic threshold selection) and point-adjust (prediction modification before evaluation) are both removed from the framework so the reported scores reflect unmodified detection output; their effects are then studied separately in Sections 4.3.4 and 4.3.5 (Sect. 3.4, p. 487).
- Synthetic datasets are generated from a sine base with injected global, contextual, seasonal and trend anomalies following the guideline in [31]; average anomaly length is set to 50 by default "so any algorithm is applicable" (Sect. 4.1.1, p. 487).
- Experiments on synthetic datasets run ten times with different generating seeds, reporting the average (Sect. 4.1.1, p. 487).
- Systematic hyper-parameter search per method, with a search space designed per parameter from the originating paper's suggestions; datasets split training/validation/test at "4:1:5" and training sets are anomaly-free as required by [3, 17, 52, 58]; the parameter with best validation performance is used for testing (Sect. 4.1.3, p. 488).
- Evaluation metrics: point metrics are precision, recall and F-measure; the range metric is the overlap-based measure from [53] with the default Flat bias; F-measure = 2·Precision·Recall/(Precision+Recall) applies to both (Sect. 4.1.2, p. 488).
- Efficiency is measured as total time for all procedures except file loading and result evaluation (Sect. 4.1.2, p. 488).

The inter-class experiments are the paper's distinctive design choice: univariate methods are run separately on each dimension of multivariate data and their reported anomalies combined (Sect. 4.3.1, p. 491); online methods are run across different window and slide sizes on datasets larger than 100k and dimensions larger than 30 (Sect. 4.3, p. 491); and point methods are applied to datasets with subsequence anomalies under both metrics to expose metric and adjustment effects (Sect. 4.3.3, p. 492).

## Key Findings

- No single method wins across all cases; "There is no super-algorithm that is suitable for all cases" (Sect. 4.2.1 Summary, p. 488).
- NETS is the most efficient point method and performs best in most cases given proper parameters; PBAD and BeatGAN have better overall accuracy on multivariate data but cost more time.
- Deep learning methods do not outperform classical methods on datasets with complex anomaly patterns; the authors attribute this to insufficient data instances and dimensions to learn a good model (Sect. 4.2.1, p. 488).
- On the Swat dataset (51 dimensions), the univariate method IDK costs 16.50s while the multivariate method PBAD takes 125.17s, almost ten times as long (Sect. 2.2.1, p. 485).
- Methods are stable when the anomaly rate is low (< 25%), contrary to claims about random detection in [44]; some methods improve as the anomaly rate rises because many reported false positives become true positives (Sect. 4.2.2 Summary, p. 489).
- Small data size (< 10k) can produce unstable results for subsequence methods; IDK is recommended when data size exceeds 50k (Sect. 4.2.3 Summary, p. 490).
- LRRDS scales well with data dimension while NETS, Stare and PBAD are significantly affected by it; NETS is recommended when dimension is limited (< 30) and RCoder when dimension is large (> 30) (Sect. 4.2.4 Summary, p. 490).
- For point methods, global anomalies are easier to detect than contextual ones; for subsequence methods, seasonal anomalies are easiest and trend anomalies hardest; no one method fits all patterns, but for global outliers NP is significantly best (Sect. 4.2.5 Summary, p. 491).
- Multivariate methods are preferred over running univariate methods per dimension unless there is sufficient prior knowledge about specific dimensions; the recall gain from combining dimensions does not compensate for the sharp precision drop (Sect. 4.3.1 Summary, p. 491).
- Online methods can outperform batch methods under a proper setting because time series characteristics evolve; but even the fastest online method is ten times slower than the simple batch method SHESD when the window size is 10k (Sect. 4.3.2 Summary, p. 492).
- Point methods can also work well for global subsequence anomalies with extreme values, potentially relaxing the anomaly-length input requirement that subsequence methods carry (Sect. 4.3.3 Summary, p. 492).
- The point-adjust method converts false negatives to true positives, giving an average promotion of 27.0% for point datasets and 31.2% for subsequence datasets under point metrics, but an average negative promotion of −67.6% for subsequence datasets under range metrics; it can reverse method rankings (Sect. 4.3.4, p. 493).
- Threshold robustness differs by method: IDK has the best overall performance while NormA is more robust above a 20% threshold; among deep learning methods RCoder has the best overall performance while Omni is more robust (Sect. 4.3.5 Summary, p. 493).
- POT achieves similar or slightly better results than grid search on the validation set in around 55% of cases (Sect. 4.3.5, p. 493).
- All algorithms generally have higher false negative rate and lower false positive rate, making them better suited to negative applications; NETS and Omni have low FPR and are recommended for negative cases, TranAD and RCoder for positive cases, PBAD over BeatGAN for positive subsequence cases (Sect. 4.3.6, p. 494).
- NP appears best for early detection with a performance improvement of 10.99%; BeatGAN scores a 49% drop under the Front metric compared with Flat, indicating it captures outliers with latency (Sect. 4.3.6, p. 494).

## Key Figures and Tables

- Table 1 (p. 484): Comparison of eight prior TAD experimental surveys against this work across the three facets, threshold robustness and application guideline — only this work marks all three facets and both threshold robustness and application guideline.
- Table 2 (p. 486): Properties of the seventeen considered algorithms — dimension, process, anomaly type, threshold rule, original language and speedup from re-implementation.
- Table 3 (p. 487): Summary of all real-world and synthetic datasets with size, dimensionality, anomaly rate, pattern and average anomaly length.
- Table 4 (p. 489): Accuracy (precision/recall/F-measure) of all seventeen methods across eight real datasets — the paper's main intra-class accuracy table.
- Table 5 (p. 491): Performance on single dimensions versus combination for the multivariate methods PBAD, BeatGAN, SAND and NP on Exercise and on the synthetic Mul_ncor_g.
- Table 6 (p. 493): F-measure with and without point-adjust under point and range metrics for TranAD, USAD, Omni, RCoder, GDN, NETS, Stare and SHESD on Twitter, ECG, Exathlon and Uni-sub-g, with per-method and per-data promotion figures.
- Table 7 (p. 493): F-measure with and without the POT automatic threshold method for TranAD, USAD, Omni and GDN on ECG, DLR, TAO and UNI.
- Figure 3 (p. 488): Time cost over various datasets for point and range anomalies — NETS most efficient, TranAD best time efficiency among deep methods.
- Figure 9 (p. 490): Varying anomaly patterns for point and subsequence methods — global outperforms contextual for point methods; seasonal easiest and trend hardest for subsequence methods.
- Figure 10 (p. 490): Critical difference diagram on the synthetic Uni-sub-g global anomaly case, with average ranks for MERLIN 8.9, LRRDS 8.1, BeatGAN 6.9, GrammarViz 5.9, NormA 5.2, and NP 1.0, SAND 2.4, IDK 3.2, PBAD 3.4.
- Figure 11 (p. 491): Varying window and slide sizes on ECG — accuracy of NETS first increases then decreases with window size, and the fastest online method is still ten times slower than SHESD at a 10k window.
- Figure 13 (p. 492): Case study on Uni-sub-g and Uni-sub-s zooming into 400 data points — PBAD and SAND cover the whole anomaly subsequence while subsequence methods usually lag.
- Figure 14 (p. 492): Illustration of the point-adjust method converting false negatives to true positives within a ground-truth anomaly segment.
- Figure 15 (p. 493): Varying thresholds on ECG and Uni-sub-g — NP drops sharply as the threshold approaches 20% while NormA is smoother; IDK performs best in this experiment.
- Figure 16 (p. 494): FPR and FNR of all methods on real datasets — all algorithms show higher FNR than FPR.
- Figure 17 (p. 494): Early detection under the Front metric on Power and averaged over all real datasets — BeatGAN's advantage under Flat reverses under Front.
- Figure 18 (p. 494): The paper's practical guide for time series anomaly detection, branching on anomaly type, dimensionality, application type, stationarity, knowledge of anomaly length and early-detection need.

## Limitations and Gaps

- The authors state explicitly that a poor result in their evaluation "does not necessarily mean that its theory is bad, because the metric and the situation are quite different" (Sect. 4, p. 487).
- The authors acknowledge that hyper-parameters (including thresholds) are selected on a validation set and that "there is a small difference between the validation set and the test set", which is why IDK performs best in the threshold experiment but not in the pattern experiment (Sect. 4.3.5, p. 493).
- The authors acknowledge that Exathlon's capability of evaluating explanation discovery results "is not covered by our work" (Sect. 1.2, p. 484).
- The authors acknowledge that explainability of anomaly detection methods is an open concern and that developing a method with both high accuracy and reasonable explainability "may be of interest for future work" (Sect. 5, p. 494).
- The authors acknowledge that the practical guide "is formed according to current work and future work is still encouraged" (Sect. 5, p. 494).
- [unacknowledged] The Friedman test on the different anomaly patterns yields a p-value greater than 0.05, so the paper cannot claim the compared methods differ significantly across patterns; the claim that a particular method clearly outperforms others rests on the post-hoc rank diagram for single patterns only (Sect. 4.2.5, p. 491).
- [unacknowledged] Deep learning methods are run on GPU and their efficiency is not compared, so the efficiency results cover only non-deep methods and the effectiveness-versus-efficiency trade-off is not complete across all seventeen algorithms (Sect. 4.1, p. 487).
- [unacknowledged] The taxonomy is described as having "six inner classes", but the classes are not enumerated as a closed list anywhere in the text; Figure 1 is referenced for them without a numbered enumeration (Sect. 1.1, p. 484; Figure 1, p. 485).
- [unacknowledged] Several method-dataset cells in Table 4 are reported as dashes — RCoder on Yahoo, Twitter and SMTP, MERLIN on Swat — so the accuracy comparison is not complete for every method on every dataset (Table 4, p. 489).
- [unacknowledged] Results are presented mainly graphically in Figures 3-17 with axes only, so most of the varying-rate, varying-size, varying-dimension and varying-threshold results cannot be reconstructed numerically from the text.
- [unacknowledged] The range metric used depends on the Flat bias default, and the paper does not report sensitivity of its range-metric conclusions to the bias parameter (Sect. 4.1.2, p. 488).
- [unacknowledged] The claim that anomaly rate has little effect on efficiency and that methods are stable below 25% is tested only on synthetic sine-based data, so the stability statement is not established for the real-world datasets (Sect. 4.2.2, p. 489).

## Definitions

- **Point anomaly** — a data point that deviates significantly from other observations; subdivided into global anomaly (δ ∼ σ(X), the standard deviation of the whole series) and contextual anomaly (δ ∼ σ(X_{t−k,t+k}), differing from its neighbours within a window of size k) (Sect. 2.2.3, p. 485).
- **Subsequence anomaly** — a subsequence X_{i,j} = ρ(2πωT_{i,j}) + τ(T_{i,j}) where ρ, ω, τ represent basic shape, trend and seasonality; global (shapelet) anomaly has dissimilar basic shape, seasonal anomaly has unusual seasonality, and trend anomaly permanently shifts the mean of the data (Sect. 2.2.3, p. 486).
- **Intra-class comparison** — systematic experiments between methods of the same class in the same test environment, performed for a fair performance comparison (Sect. 1, p. 483).
- **Inter-class comparison** — comparison between classes within the same facet, e.g. univariate versus multivariate, online versus batch, point versus subsequence methods (Sect. 1, p. 484).
- **Point metric** — precision = TP/(TP+FP) and recall = TP/(TP+FN), with F-measure = 2·Precision·Recall/(Precision+Recall) (Sect. 4.1.2, p. 488).
- **Range metric** — an overlap-based measure between the set of real anomaly ranges R and predicted anomaly ranges P, with Flat bias as the default setting (Sect. 4.1.2, p. 488).
- **Point-adjust** — a prediction modification that, for each point in a ground-truth anomaly segment, converts all observations in that subsequence to true positives if any point in it was detected (Sect. 4.3.4, p. 493).
- **POT** — an automatic threshold-selection method based on extreme value theory, removed from the main framework and studied separately (Sect. 3.4, p. 487; Sect. 4.3.5, p. 493).
- **Anomaly rate a%** — the proportion of injected anomalies in a synthetic dataset, varied from 5% to 25% (Sect. 4.2.2, p. 489).
- **Distance-based outlier** — with count threshold θ_k and distance threshold θ_R, the set of data points that have fewer than θ_k neighbours (Sect. 3.1, p. 486).
- **Pattern-based outlier** — with anomaly length ℓ and count threshold θ_K, the set of top-θ_K subsequences of length ℓ with the lowest similarity to patterns extracted from X (Sect. 3.2, p. 486).

## Statistical Evidence

The paper prints its accuracy results graphically and as flattened tables, so most
per-dataset F-measures cannot be reconstructed numerically from the text. The
values below are the quantities the paper states in prose, each as printed.

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Point-adjust promotion on point datasets | average promotion | 27.0% | — | — | Sect. 4.3.4, p. 493 |
| Point-adjust promotion on subsequence datasets under point metrics | average promotion | 31.2% | — | — | Sect. 4.3.4, p. 493 |
| Point-adjust promotion on subsequence datasets under range metrics | average promotion | -67.6% | — | — | Sect. 4.3.4, p. 493 |
| TranAD and Omni under point-adjust | F-measure | 0.245 | — | — | Sect. 4.3.4, p. 493 |
| IDK running time on Swat, 51 dimensions | running time | 16.50 s | — | — | Sect. 1.1, p. 485 |
| PBAD running time on Swat, 51 dimensions | running time | 125.17 s | — | — | Sect. 1.1, p. 485 |
| Fastest online method NETS against batch SHESD at window size 10k | relative running time | ten times slower | — | — | Sect. 4.3.2, p. 492 |
| NP under early detection | performance improvement | 10.99% | — | — | Sect. 4.3.6, p. 494 |
| BeatGAN under the Front metric against Flat | F-measure drop | 49% | — | — | Sect. 4.3.6, p. 494 |
| POT against grid search on the validation set | share of cases similar or slightly better | around 55% | — | — | Sect. 4.3.5, p. 493 |
| Method differences across anomaly patterns | Friedman test p-value | greater than 0.05 | — | > 0.05 | Sect. 4.2.5, p. 491 |
| Method stability at low anomaly rate | anomaly rate boundary | less than 25% | — | — | Sect. 4.2.2 Summary, p. 489 |
| Small data size affecting subsequence methods | data size boundary | less than 10k | — | — | Sect. 4.2.3 Summary, p. 490 |
| IDK recommended above a data size | data size boundary | more than 50k | — | — | Sect. 4.2.3 Summary, p. 490 |
| NETS recommended below a dimension | dimension boundary | less than 30 | — | — | Sect. 4.2.4 Summary, p. 490 |
| SAND decomposition cost on long anomalies | anomaly length threshold | greater than 100 | — | — | Sect. 4.2.1, p. 488 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "There is no super-algorithm that is suitable for all cases" | Sect. 4.2.1 Summary, p. 488 | model_performance_evaluation |
| "Given proper parameters, NETS can perform best in most cases" | Sect. 4.2.1 Summary, p. 488 | model_performance_evaluation |
| "PBAD and BeatGAN have better overall accuracy but cost more time" | Sect. 4.2.1 Summary, p. 488 | model_performance_evaluation |
| "Deep learning methods do not outperform others on datasets with complex anomaly patterns" | Sect. 4.2.1 Summary, p. 488 | model_performance_evaluation |
| "the univariate method IDK costs 16.50s, while the multivariate method PBAD takes 125.17s, almost 10 times the time" | Sect. 1.1, p. 485 | model_algorithm_integration |
| "the Friedman tests yield a p-value greater than 0.05 and thus do not indicate that these methods are significantly different" | Sect. 4.2.5, p. 491 | model_performance_evaluation |
| "there is a particular method that clearly outperforms the others" | Sect. 4.2.5, p. 491 | model_performance_evaluation |
| "Promotion on efficiency cannot compensate for the sharp drop in accuracy" | Sect. 4.3.1 Summary, p. 491 | model_algorithm_integration |
| "Multivariate methods are better, unless we have sufficient prior knowledge about specific dimensions" | Sect. 4.3.1 Summary, p. 491 | model_algorithm_integration |
| "Online methods can outperform batch methods under a proper setting, due to the evolvement characteristic of time series" | Sect. 4.3.2 Summary, p. 492 | model_algorithm_integration |
| "Point methods can also work well for global subsequence anomalies with extreme values" | Sect. 4.3.3 Summary, p. 492 | model_performance_evaluation |
| "point-adjust method tends to report 'false' higher results for algorithms and can lead to misleading analyzes" | Sect. 4.3.4 Summary, p. 493 | model_performance_evaluation |
| "The use of range metrics on datasets with subsequence anomalies is preferable as it leads to more reasonable and robust results" | Sect. 4.3.4 Summary, p. 493 | model_performance_evaluation |
| "Automatic threshold selection methods can still be improved to take effect in practical uses" | Sect. 4.3.5 Summary, p. 493 | model_performance_evaluation |
| "NP appears to be the best performing algorithm for early detection" | Sect. 4.3.6, p. 494 | model_performance_evaluation |
| "We employ widely used real-world datasets with labels as benchmarks, 7 with point and 8 with subsequence anomalies" | Sect. 4.1.1, p. 487 | data_collection |

## Remember This

- This is a comparative benchmark study of seventeen TAD algorithms, not a new detector; its contribution is taxonomy plus systematic intra- and inter-class evaluation.
- The taxonomy has three facets — data dimension, processing technique, anomaly type — and six inner classes.
- Ten of the seventeen methods were re-implemented in JAVA and all were refactored under one code structure to remove implementation confounds.
- POT and point-adjust were removed from the main framework and analysed separately; point-adjust inflates scores and can reverse method rankings.
- Headline finding: no method wins everywhere; deep learning does not beat classical methods on complex anomaly patterns.
- Practical recommendations: NETS for low dimension, RCoder for high dimension, IDK for data above 50k, NP for early detection, Omni/NETS for negative applications, TranAD/RCoder for positive applications.

## Cited Works

- Yoon, Lee & Lee (2019) — NETS, extremely fast outlier detection from a data stream via set-based processing; one of the two distance-based methods compared. [p. 486]
- Yoon, Lee & Lee (2020) — STARE, ultrafast local outlier detection with stationary region skipping; the second distance-based method compared. [p. 486]
- He, Chu & Wang (2020) — Neighbor Profile (NP), bagging nearest neighbours for unsupervised time series mining; a nearest-neighbour-ball technique solving the twin freak problem. [p. 486]
- Nakamura, Imamura, Mercer & Keogh (2020) — MERLIN, parameter-free discovery of arbitrary-length anomalies in massive time series archives. [p. 486]
- Feremans, Vercruyssen, Cule, Meert & Goethals (2019) — PBAD, pattern-based anomaly detection in mixed-type time series. [p. 486]
- Hu, Feng, Ji, Yan & Zhou (2019) — LRRDS, discord search with local recurrence rates in multivariate time series. [p. 486]
- Boniol, Paparrizos, Palpanas & Franklin (2021) — SAND, streaming subsequence anomaly detection, extending k-Shape clustering to an online normal model. [p. 486]
- Boniol, Linardi, Roncallo, Palpanas, Meftah & Remy (2021) — NormA, unsupervised and scalable subsequence anomaly detection in large data series. [p. 486]
- Senin, Lin, Wang, Oates, Gandhi, Boedihardjo, Chen & Frankenstein (2018) — GrammarViz 3.0, interactive discovery of variable-length time series patterns via grammar induction. [p. 486]
- Hochenbaum, Vallis & Kejariwal (2017) — SHESD, automatic anomaly detection in the cloud via statistical learning, extending ESD with STL decomposition and robust median/MAD. [p. 486]
- Ting, Liu, Zhang & Zhu (2022) — IDK, a new distributional treatment for time series using the Isolation Distributional Kernel. [p. 486