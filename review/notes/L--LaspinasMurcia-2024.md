---
paper_id: L--LaspinasMurcia-2024
first_author: "Laspinas"
year: 2024
title: "Machine Learning Approaches in Classifying Income Levels"
venue: "TWIST, 19(2), 92-97"
doi: "Not reported"
type: journal-article
designation: local
status: extracted
modules: [model_performance_evaluation]
module_rationale:
  model_performance_evaluation: "Sect. Results and Discussion, Tables 2 and 3 (pp. 4-5) benchmark six classifiers and eleven tuned variants on accuracy, true positive rate, false positive rate, precision, recall, F-measure and kappa under 10-fold cross-validation (p. 3)."
---

# Machine Learning Approaches in Classifying Income Levels

`L--LaspinasMurcia-2024` — Laspinas (2024), *TWIST, 19(2), 92-97* [DOI printed on p. 1 as 10.5281/zenodo.10049652; no DOI recorded in `metadata.json`]

## Summary

Six classifiers — Logistic, Decision Tree (J48), RandomForest, Random Tree, IBk (k-NN) and NaiveBayes — were benchmarked on 16,281 Adult Income records, with the two ensemble methods reaching 98.35% and 98.37% accuracy, the highest of the eleven configurations tested.

## Problem and Motivation

Conventional econometric models depend on linear associations and a limited factor range, which the paper argues obscures the non-linear interactions among variables that shape income levels. Classification and prediction of income levels matter because income disparity constrains economic growth and social mobility, including in the Philippines. The authors state the research disparity as the inadequate use of machine learning methods in predicting adult income levels.

## Method

**Design.** Comparative benchmark study of supervised classifiers with parameter sweeps, evaluated by 10-fold cross-validation; the authors state no formal design label.
**Sample.** n = 16,281 records from the Adult Income Prediction dataset on Kaggle (unit: one adult individual), described by thirteen attributes — age, work class, education, marital-status, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country — with the binary target `Income`.
**Context.** geography: Not reported (Philippine authors, Philippine income context discussed, but no Philippine dataset); population: adults classified above or below $50,000 annual income, drawn from census-derived socioeconomic and demographic data; setting: offline computational experiment in WEKA with no participants and no deployed system.

- Use the Adult Income Prediction dataset from Kaggle, described as census-derived, to predict whether annual income exceeds $50,000 (p. 2).
- Select attributes by information gain with InfoGainAttributeEval and rank them with the Ranker search method (p. 3).
- Use four classifiers named in the method (decision trees J48, RandomForest, IBk for k-NN, Naive Bayes) plus Random Tree and Logistic Regression, giving six classifiers (p. 3).
- Tune J48 by varying the confidence factor for post-pruning over 0.25, 0.50 and 0.75 (p. 3).
- Tune IBk by varying the neighbourhood size k over 3, 5, 7 and 9 (p. 3).
- Evaluate every classifier with 10-fold cross-validation, training on nine folds and testing on the tenth, and average the performance measures (p. 3).
- Report accuracy and correct-instance counts in Table 2 and TP rate, FP rate, precision, recall, F-measure and kappa in Table 3 (pp. 4-5).
- Attribute the ensemble methods' accuracy to their resistance to overfitting, and the k-NN decline to distant neighbours from other classes entering the vote (pp. 4-5).
- Conclude that no universal classifier exists and that selection should follow the dataset and task, recommending ensemble methods as a starting point (p. 5).
- Recommend extending the classifiers to other economic settings and datasets, adding socio-economic factors, and integrating behavioural economics, sociology and psychology (p. 5).

## Software

- WEKA (version not reported), including J48, IBk, InfoGainAttributeEval and Ranker

## Key Findings

- num: RandomForest accuracy is 98.35% and Random Tree accuracy 98.37%, the highest of the eleven configurations, on 16,281 records (Table 2, p. 4).
- num: J48 accuracy rises with the confidence factor: 87.21% at C 0.25, 88.96% at C 0.50 and 90.84% at C 0.75 (p. 3); Table 2 prints the last of these as `90.8482` (Table 2, p. 4).
- num: IBk accuracy falls as k grows, from 89.11% at k = 3 through 87.27% at k = 5 and 86.34% at k = 7 to 85.74% at k = 9 (p. 4).
- num: Logistic accuracy is 85.82%, correctly classifying 13,923 instances; NaiveBayes accuracy is 82.24%, the lowest of the six (p. 3, p. 4).
- num: Table 3 reports F-measures of 0.983 for RandomForest and 0.984 for Random Tree against 0.85 for Logistic and 0.807 for NaiveBayes (p. 4).
- num: Table 3 reports kappa of 0.9541 for both ensemble methods, 0.6715 for J48 at C 0.50, and 0.433 for J48 at C 0.75 (p. 4).
- num: Eleven classification tests were run across the six classifiers (p. 3).
- num: The dataset holds 16,281 observations described by thirteen attributes (p. 2).
- num: Information gain ranked `Relationship` highest at 0.16575, then `Marital Status` at 0.15809 and `Capital Gain` at 0.11337, with `Race` lowest at 0.00819 (p. 3).

## Key Figures and Tables

- Table 1 (p. 2): the thirteen attributes with their types and descriptions plus the `Income` target → the feature set is demographic and employment-derived, with no transaction-level or savings variable.
- Table 2 (p. 4): classification accuracy and correctly-predicted counts for all eleven configurations → the two ensemble methods are separated from the rest by roughly eight percentage points.
- Table 3 (p. 4): TP rate, FP rate, precision, recall, F-measure and kappa per configuration → J48 at C 0.75 has the worst kappa (0.433) of any J48 setting, opposite to the accuracy ordering in Table 2.

## Limitations and Gaps

- [unacknowledged] Accuracy and F-measure disagree with the paper's own interpretation: Table 2 accuracy rises with J48's confidence factor to 90.84% at C 0.75 while the F-measure falls to 0.806 and kappa collapses to 0.433, and the authors describe the confidence factor as producing decreasing performance and overfitting.
- [unacknowledged] No confidence intervals, standard deviations, per-fold dispersion, significance tests or class-wise breakdown are reported, so the 98.35% and 98.37% accuracies cannot be distinguished from variation across folds or splits.
- [unacknowledged] Results are reported on training data under cross-validation without a held-out test set, so no independent generalisation figure is given despite the claim that the models generalise to unobserved data.
- The authors acknowledge that the theory and methods are dataset- and task-dependent, so the optimal classifier cannot be named without further study (p. 5).
- The authors recommend testing the classifiers in other economic settings and datasets, adding socio-economic factors, and integrating behavioural economics, sociology and psychology (p. 5).
- [unacknowledged] The study is scoped to aggregate adult income classification on one public dataset; no individual budgeting, savings, debt or application setting is examined.

## Definitions

- **Adult Income Prediction dataset** — The Kaggle dataset (Patki, n.d.) of census-derived demographic and employment attributes used for all experiments (p. 2).
- **J48** — The Weka decision tree classifier whose confidence factor governs post-pruning; the paper tunes it at 0.25, 0.50 and 0.75 (p. 3).
- **IBk** — The Weka implementation of k-nearest neighbours; `k` is the neighbourhood size, tuned at 3, 5, 7 and 9 (p. 3).
- **InfoGainAttributeEval** — The Weka evaluator that scores a feature by the information gain it yields relative to the class (p. 3).
- **Ranker** — The Weka search method that orders attributes by their assessed value, most significant to least (p. 3).
- **F-measure** — The harmonic summary of precision and recall reported for every configuration in Table 3 (p. 4).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Income classification accuracy, Logistic | accuracy | 85.82% | — | — | Table 2, p. 4 |
| Income classification accuracy, J48 C 0.25 | accuracy | 87.21% | — | — | Table 2, p. 4 |
| Income classification accuracy, J48 C 0.50 | accuracy | 88.96% | — | — | Table 2, p. 4 |
| Income classification accuracy, J48 C 0.75 | accuracy | 90.8482 | — | — | Table 2, p. 4 |
| Income classification accuracy, J48 C 0.75 as stated in the text | accuracy | 90.84% | — | — | Sec. Results and Discussion, p. 3 |
| Income classification accuracy, RandomForest | accuracy | 98.35% | — | — | Table 2, p. 4 |
| Income classification accuracy, Random Tree | accuracy | 98.37% | — | — | Table 2, p. 4 |
| Income classification accuracy, IBk k = 3 | accuracy | 89.11% | — | — | Table 2, p. 4 |
| Income classification accuracy, IBk k = 5 | accuracy | 87.27% | — | — | Table 2, p. 4 |
| Income classification accuracy, IBk k = 7 | accuracy | 86.34% | — | — | Table 2, p. 4 |
| Income classification accuracy, IBk k = 9 | accuracy | 85.74% | — | — | Table 2, p. 4 |
| Income classification accuracy, NaiveBayes | accuracy | 82.24% | — | — | Table 2, p. 4 |
| Correctly predicted instances, Logistic | correct instances | 13,923 | — | — | Table 2, p. 4 |
| Correctly predicted instances, RandomForest | correct instances | 16,013 | — | — | Table 2, p. 4 |
| Correctly predicted instances, Random Tree | correct instances | 16,016 | — | — | Table 2, p. 4 |
| Classification performance, Logistic | precision | 0.849 | — | — | Table 3, p. 4 |
| Classification performance, Logistic | recall (printed as TP rate) | 0.855 | — | — | Table 3, p. 4 |
| Classification performance, Logistic | false positive rate | 0.319 | — | — | Table 3, p. 4 |
| Classification performance, Logistic | F-measure | 0.85 | — | — | Table 3, p. 4 |
| Classification performance, Logistic | kappa | 0.5717 | — | — | Table 3, p. 4 |
| Classification performance, J48 C 0.25 | precision | 0.868 | — | — | Table 3, p. 4 |
| Classification performance, J48 C 0.25 | recall (printed as TP rate) | 0.872 | — | — | Table 3, p. 4 |
| Classification performance, J48 C 0.25 | false positive rate | 0.326 | — | — | Table 3, p. 4 |
| Classification performance, J48 C 0.25 | F-measure | 0.864 | — | — | Table 3, p. 4 |
| Classification performance, J48 C 0.25 | kappa | 0.6065 | — | — | Table 3, p. 4 |
| Classification performance, J48 C 0.50 | precision | 0.886 | — | — | Table 3, p. 4 |
| Classification performance, J48 C 0.50 | recall (printed as TP rate) | 0.89 | — | — | Table 3, p. 4 |
| Classification performance, J48 C 0.50 | false positive rate | 0.264 | — | — | Table 3, p. 4 |
| Classification performance, J48 C 0.50 | F-measure | 0.885 | — | — | Table 3, p. 4 |
| Classification performance, J48 C 0.50 | kappa | 0.6715 | — | — | Table 3, p. 4 |
| Classification performance, J48 C 0.75 | precision | 0.808 | — | — | Table 3, p. 4 |
| Classification performance, J48 C 0.75 | recall (printed as TP rate) | 0.821 | — | — | Table 3, p. 4 |
| Classification performance, J48 C 0.75 | false positive rate | 0.443 | — | — | Table 3, p. 4 |
| Classification performance, J48 C 0.75 | F-measure | 0.806 | — | — | Table 3, p. 4 |
| Classification performance, J48 C 0.75 | kappa | 0.433 | — | — | Table 3, p. 4 |
| Classification performance, RandomForest | precision | 0.983 | — | — | Table 3, p. 4 |
| Classification performance, RandomForest | recall (printed as TP rate) | 0.984 | — | — | Table 3, p. 4 |
| Classification performance, RandomForest | false positive rate | 0.035 | — | — | Table 3, p. 4 |
| Classification performance, RandomForest | F-measure | 0.983 | — | — | Table 3, p. 4 |
| Classification performance, RandomForest | kappa | 0.9541 | — | — | Table 3, p. 4 |
| Classification performance, Random Tree | precision | 0.984 | — | — | Table 3, p. 4 |
| Classification performance, Random Tree | recall (printed as TP rate) | 0.984 | — | — | Table 3, p. 4 |
| Classification performance, Random Tree | false positive rate | 0.047 | — | — | Table 3, p. 4 |
| Classification performance, Random Tree | F-measure | 0.984 | — | — | Table 3, p. 4 |
| Classification performance, Random Tree | kappa | 0.9541 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 3 | precision | 0.888 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 3 | recall (printed as TP rate) | 0.891 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 3 | false positive rate | 0.247 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 3 | F-measure | 0.888 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 3 | kappa | 0.6812 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 5 | precision | 0.868 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 5 | recall (printed as TP rate) | 0.873 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 5 | false positive rate | 0.286 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 5 | F-measure | 0.868 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 5 | kappa | 0.6245 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 7 | precision | 0.858 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 7 | recall (printed as TP rate) | 0.863 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 7 | false positive rate | 0.309 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 7 | F-measure | 0.858 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 7 | kappa | 0.5943 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 9 | precision | 0.851 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 9 | recall (printed as TP rate) | 0.857 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 9 | false positive rate | 0.326 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 9 | F-measure | 0.851 | — | — | Table 3, p. 4 |
| Classification performance, IBk k = 9 | kappa | 0.5735 | — | — | Table 3, p. 4 |
| Classification performance, NaiveBayes | precision | 0.809 | — | — | Table 3, p. 4 |
| Classification performance, NaiveBayes | recall (printed as TP rate) | 0.822 | — | — | Table 3, p. 4 |
| Classification performance, NaiveBayes | false positive rate | 0.442 | — | — | Table 3, p. 4 |
| Classification performance, NaiveBayes | F-measure | 0.807 | — | — | Table 3, p. 4 |
| Classification performance, NaiveBayes | kappa | 0.4361 | — | — | Table 3, p. 4 |
| Feature informativeness, Relationship | information gain score | 0.16575 | — | — | Sec. Feature Selection, p. 3 |
| Feature informativeness, Marital Status | information gain score | 0.15809 | — | — | Sec. Feature Selection, p. 3 |
| Feature informativeness, Capital Gain | information gain score | 0.11337 | — | — | Sec. Feature Selection, p. 3 |
| Feature informativeness, Native Country | information gain score | 0.00901 | — | — | Sec. Feature Selection, p. 3 |
| Feature informativeness, Race | information gain score | 0.00819 | — | — | Sec. Feature Selection, p. 3 |
| Classifier configurations evaluated | number of classification tests | 11 | — | — | Sec. Results and Discussion, p. 3 |
| Evaluation sample size | records | 16,281 | — | — | Sec. Dataset, p. 2 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "RandomForest and Random Tree classifiers demonstrated the highest efficacy across all metrics." | Abstract, p. 1 | model_performance_evaluation |
| "Tests results revealed accuracy of 87.21%, 88.96%, and 90.84% for confidence levels of 0.25, 0.50, and 0.75." | Sec. Results and Discussion, p. 3 | model_performance_evaluation |
| "The accuracy of Logistic was 85.82%, correctly classifying 13,923 instances." | Sec. Results and Discussion, p. 3 | model_performance_evaluation |
| "The Random Forest classifier and the Random Tree classifier achieved accuracy levels of 98.35% and 98.37%, respectively." | Sec. Results and Discussion, p. 3 | model_performance_evaluation |
| "Despite having the lowest accuracy among the tested classifiers, Naive Bayes remains a popular option due to its simplicity and effectiveness with large data sets" | Sec. Results and Discussion, p. 4 | model_performance_evaluation |
| "As indicated by the F-measure, the Decision Tree (J48) classifier exhibits a trend in which increasing the confidence factor (C) leads to decreased performance." | Sec. Results and Discussion, p. 4 | model_performance_evaluation |
| "this classification revealed the 'Relationship' attribute to be the most predictive of income levels, with a value of 0.16575." | Sec. Feature Selection, p. 3 | model_performance_evaluation |
| "The results demonstrate that there is no universal classifier and that the selection of a classifier should be based on the task and dataset at hand." | Sec. Results and Discussion, p. 5 | model_performance_evaluation |
| "The classifier was evaluated using 10-fold cross-validation, a technique that guarantees a balanced and unbiased estimation of model performance" | Sec. Data Classification and Cross-Validation, p. 3 | model_performance_evaluation |
| "it is necessary to examine the suitability of these machine learning classifiers in various economic settings and datasets" | Sec. Recommendations, p. 5 | model_performance_evaluation |

## Remember This

- Ensemble methods dominate: RandomForest 98.35%, Random Tree 98.37% accuracy on 16,281 Adult Income records.
- J48 accuracy rises with confidence factor while its F-measure and kappa fall — the two tables disagree.
- IBk peaks at k = 3 (89.11%) and degrades monotonically to 85.74% at k = 9.
- No confidence intervals, significance tests or held-out test set are reported.
- The study classifies aggregate adult income; no budgeting, savings or debt setting is examined.

## Cited Works

- Peng, C. Y. J.; Lee, K. L.; Ingersoll, G. M. (2002) (methodology) — earlier evidence that logistic regression is an effective classifier for binary outcomes, matching the 85.82% accuracy here. [p. 3]
- Liaw, A.; Wiener, M. (2002) (methodology) — the randomForest implementation whose ensemble behaviour the paper credits for the highest accuracy. [p. 3]
- Zhou, Z. H. (2012) (methodology) — ensemble methods cited as the reason ensembles prevent overfitting and sustain high performance. [p. 5]
- Rajesh, K.; Karthikeyan (2017) (finding) — higher confidence levels may improve a decision tree classifier's efficacy, cited for the J48 accuracy trend. [p. 3]
- Dudani, S. A. (1976) (methodology) — the distance-weighted k-nearest neighbour rule cited as the basis for varying `k` to reduce error probability. [p. 3]
- Franco-Lopez, H.; Ek, A. R.; Bauer, M. E. (2001) (finding) — larger neighbourhoods bring in more disturbance and distant neighbours of other classes, cited to explain IBk's decline. [p. 4]
- Kohavi, R. (1995) (methodology) — cross-validation and bootstrap for accuracy estimation and model selection, cited to justify 10-fold cross-validation. [p. 3]
- John, G. H.; Langley, P. (1995) (context) — Naive Bayes simplicity and effectiveness on large data sets, cited to explain its retention despite the lowest accuracy. [p. 4]
- Martin, M. A. (2006) (context) — family structure and income inequality, cited to explain why `Relationship` is the most predictive attribute. [p. 3]
- Schoeni, R. F. (1995) (context) — marital status and earnings, cited to support `Marital Status` as the second-ranked attribute. [p. 3]
- Frank, R. (2010) (context) — the effect of financial transactions and investments on income, cited for `Capital Gain` as third-ranked. [p. 3]
- Patki, S. (n.d.) (methodology) — the Kaggle Adult Income Prediction dataset supplying all 16,281 records and thirteen attributes. [p. 2]
- Hassan, S. A.; Khan, T. (2017) (methodology) — information gain feature evaluation, cited for the InfoGainAttributeEval and Ranker combination. [p. 3]
- Blachnik, M. (2017) (context) — instance selection for classifier performance estimation, cited with Telikani et al. (2021) and Yapp et al. (2020) for evaluating multiple classifiers. [p. 5]

---

Conversion: [`L--LaspinasMurcia-2024_marked.md`](../../literature/paper-markdowns/L--LaspinasMurcia-2024_marked.md)