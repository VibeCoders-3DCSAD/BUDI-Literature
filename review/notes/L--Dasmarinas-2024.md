---
paper_id: L--Dasmarinas-2024
first_author: "Dasmariñas"
year: 2024
title: "Forecasting the Impact of COVID-19 on the Household Final Consumption Expenditure (HFCE) in the Philippines"
venue: "PUP Journal of Science & Technology, 14(1), 70-90"
doi: 10.70922/ctzevg57
type: journal-article
designation: local
status: extracted
modules: [sarima, model_performance_evaluation, data_collection]
module_rationale:
  sarima: "Sec. 2.1.2.1 defines SARIMA as ARIMA plus a seasonal part, Sec. 3.2.1 fits SARIMA (1,0,0)(0,0,1)[4] on the quarterly series and selects it on the lowest Akaike Information Criterion, and Table 1 reports it as the lowest combined-error forecast of the three time-series models."
  model_performance_evaluation: "Tables 1 and 2 (p. 85) report MAE, RMSE, MSE for SARIMA, exponential smoothing and TBATS on train and test sets and MSE, RMSE, MAE and R² for XGBoost, kNN and SVR, which is the paper's model-selection evidence."
  data_collection: "Sec. 2.1 declares that all seven quarterly series come from the Time Series Data of the Philippine Statistics Authority, and Sec. 3.1 analyses the PSA Household Final Consumption Expenditure series itself over the study window."
---

# Forecasting the Impact of COVID-19 on the Household Final Consumption Expenditure (HFCE) in the Philippines

`L--Dasmarinas-2024` — Dasmariñas (2024), *PUP Journal of Science & Technology* \[10.70922/ctzevg57]

## Summary

On quarterly Philippine HFCE growth data, SARIMA (1,0,0)(0,0,1)[4] returned the lowest combined train-and-test error of the time-series models compared, and SVR returned the lowest error of the machine-learning regressors.

## Problem and Motivation

Household final consumption expenditure is 73.5% of Philippine GDP, and the 2020 contraction was the largest annual decline in the national accounts series that began in 1946 (Sec. 1, p. 71). The study asks how far COVID-19 moved the HFCE growth rate and which forecasting method can be trusted to project it from 2022 to 2026 (Sec. 1, p. 72).

## Method

**Design.** Comparative model-selection study on secondary time-series data; Sec. 2.1 "Research Design" describes the approach and states no formal design label.
**Sample.** n = Not reported (the paper prints no count of observations); unit = one calendar quarter of the national Philippine HFCE growth rate, 2001-2021 (Abstract, p. 70). Unclear: the Abstract states 2001-2021 while the figure captions and body text state 2000-2021.
**Context.** geography: Philippines; population: Not applicable (national aggregate series, no human participants); setting: Not applicable (secondary-data analysis, no field site).

- Source seven quarterly national series from the PSA Time Series Data — HFCE growth rate, inflation, unemployment, import and export growth rates for goods and services — then clean, organize, analyse, predict and present them in RStudio for the time-series arm and Orange for the machine-learning arm, no version being printed for either (Secs. 2.1-2.1.1, pp. 72-73).
- Fit three time-series models to the quarterly HFCE growth rate: SARIMA, Triple Exponential Smoothing (Holt-Winters, additive) and TBATS (Secs. 2.1.2.1-2.1.2.3, pp. 72-75).
- Take the seasonal orders P, D, Q from the ACF and PACF plots of the data, and hold the data to the stated SARIMA assumptions of univariate, stationary series (Sec. 2.1.2.1, p. 73).
- Forecast the next five years of quarterly data, 2022 to 2026, from each of the three time-series models (Sec. 2.1.2.1, p. 73).
- Graph the behaviour of each of the seven quarterly variables across the series (Figs. 3-9, pp. 78-82).
- Select the best time-series model on the lowest combined MSE, RMSE and MAE over the train and test sets (Sec. 3.3, p. 85).
- Regress the HFCE growth rate on the six economic indicators with XGBoost, kNN regression (Euclidean distance) and SVR (polynomial kernel) in Orange (Secs. 2.1.2.4-2.1.2.6, pp. 75-76).
- Rank the three regressors on MSE, RMSE, MAE and R², and report the best-performing algorithm (Sec. 3.4, p. 85).
- Define ADF for stationarity and ACF for order identification in the statistical treatment; no test result is reported for either (Secs. 2.1.2.11-2.1.2.12, p. 78).

## Software

- RStudio (version not reported) — SARIMA, Triple Exponential Smoothing, TBATS
- Orange (version not reported) — XGBoost, kNN regression, SVM regression
- R `TBATS()` function (version not reported), called as TBATS (1, {0, 0}, 0.8, -)

## Key Findings

- num: Table 1 reports SARIMA train MSE = 5.0330, RMSE = 2.2434, MAE = 1.2566 and test MSE = 0.3101, RMSE = 0.5569, MAE = 0.2677 (p. 85).
- num: Table 1 reports Triple Exponential Smoothing train MSE = 6.9866, RMSE = 2.6432, MAE = 1.4267 and test MSE = 13.0627, RMSE = 3.6142, MAE = 2.6146 (p. 85).
- num: Table 1 reports TBATS train MSE = 6.1459, RMSE = 2.4791, MAE = 1.2553 and test MSE = 0.4742, RMSE = 0.6887, MAE = 0.2484 (p. 85).
- num: The selected SARIMA specification is (1,0,0) (0,0,1) [4], with the lowest Akaike Information Criterion (Sec. 3.2.1, p. 83).
- num: The selected exponential-smoothing model is ETS (1,0,0) with a smoothing factor of 0.9454, a trend smoothing factor of 0.0002 and a 0.0001 seasonal change smoothing factor, and the selected TBATS model is TBATS (1, {0,0}, 0.8, -) with a damping parameter of 0.8, an alpha of 1.0222 and a beta of -0.2627 (Secs. 3.2.2-3.2.3, p. 84).
- num: Table 2 reports SVR at MSE 2.3970, RMSE 1.5480, MAE 1.1150 and R² 0.8060, against kNN at 5.4230, 2.3290, 1.3120, 0.5610 and XGBoost at 6.4130, 2.5320, 1.5710, 0.4810 (p. 85).
- num: The lowest HFCE growth rate for 2000-2021 was -15.32% in the second quarter of 2020, and the second quarter of 2021 began to display a growth rate of 7.31% (Sec. 3.1.1, p. 78).
- num: The unemployment rate rose to 10% in the second quarter of 2020 and 18.9% in the third quarter of 2020 (Sec. 3.1.3, p. 80).
- The study concludes that the HFCE growth rate will gradually decline across the forecast years, and that using historical data including the COVID-19 years dramatically affected the five-year model (Sec. 4, p. 86).

## Key Figures and Tables

- Figure 3: HFCE growth rate from Q1 2000 to Q4 2021 → the pandemic trough of -15.32% in Q2 2020 and the return to 7.31% growth in Q2 2021.
- Figure 4: quarterly inflation rate → peaks at 12.20% in Q3 2008, bottoms at 0.3% in Q3 2009, and shows no significant change during the pandemic.
- Figure 5: quarterly unemployment rate → a 4.5% low in Q4 2019, then 10% in Q2 2020 and 18.9% in Q3 2020.
- Figure 6: import of goods growth rate → the lowest reading -38.48% in Q2 2020, recovering to 48.45% from Q2 2021.
- Figure 7: import of services growth rate → the lowest reading -43.73% in Q4 2020, against a 39.86% peak in Q3 2008.
- Figure 8: export of goods growth rate → the lowest reading -30.57% in Q2 2020, recovering to 35.94% from Q2 2021.
- Figure 9: export of services growth rate → the lowest reading -36.01% in Q2 2020, against a 57.09% peak in Q3 2005.
- Figure 10: 2022-2026 HFCE growth rate prediction under SARIMA (1,0,0)(0,0,1)[4] → the forecast path of the selected model.
- Figure 11: 2022-2026 prediction under Triple Exponential Smoothing ETS (1,0,0) → the exponential-smoothing comparison path.
- Figure 12: 2022-2026 prediction under TBATS (1, {0,0}, 0.8, -) → the TBATS comparison path.
- Table 1: accuracy comparison of SARIMA, exponential smoothing and TBATS on train and test sets → SARIMA carries the lowest combined MSE, RMSE and MAE and is the selected time-series model.
- Table 2: accuracy comparison of XGBoost, kNN and SVR → SVR carries the lowest MSE, RMSE and MAE and the highest R², and is the selected regression algorithm.

## Limitations and Gaps

- [unacknowledged] The headline conclusion — that the historical data including the COVID-19 years "dramatically affected" the model for the next five years — is asserted without any supporting test: there is no structural-break test, no re-estimation on a pre-pandemic window, and no comparison of forecasts fitted with and without 2020-2021 (Conclusions, p. 86).
- [unacknowledged] Table 2 and the results narrative contradict each other: the text attributes "the lowest MSE (6.413), RMSE (2.532)" to SVR, which are XGBoost's values in the table, and says XGBoost showed the highest R² when its 0.4810 is the lowest of the three (p. 85).
- [unacknowledged] The SARIMA selection rests on the combined train-and-test error, yet TBATS records the lower test MAE (0.2484 against 0.2677), so the "lowest combined error" claim repeated in the Abstract and the Conclusion does not hold metric by metric, and the paper does not discuss this (Table 1, p. 85).
- [unacknowledged] No stationarity test result is reported although ADF is defined and stationarity is stated as a SARIMA assumption, and the ACF and PACF plots from which P, D and Q are said to be deduced are not shown (SARIMA model section, p. 73; Statistical treatment section, p. 78).
- [unacknowledged] The two arms are never compared with one another: SARIMA, ETS and TBATS are ranked on the univariate series and XGBoost, kNN and SVR on a regression with six economic indicators, but no cross-arm comparison is reported (Tables 1-2, p. 85).
- [unacknowledged] The 2022-2026 forecasts appear only as plots; no point forecast values, prediction intervals or other uncertainty bounds are tabulated, so the forecast itself cannot be reconstructed numerically (Figs. 10-12, pp. 83-84).
- [unacknowledged] The observation window is internally inconsistent — the Abstract gives quarterly data from 2001-2021 while the figure captions and body text give 2000-2021 — and no count of observations is printed, so the length of the series used cannot be established from the text (Abstract, p. 70; the seven series sections, pp. 78-82).
- [unacknowledged] The figure sequence starts at Figure 3: no Figure 1 or Figure 2 appears in the conversion, so the reader has no data-source or conceptual figure (pp. 78-82).
- [unacknowledged] Chen and Guestrin (2016), the source given for the XGBoost objective function, has no entry in the reference list (p. 75; References, pp. 87-90).
- [unacknowledged] The study models a national aggregate growth rate, so nothing in it speaks to individual household spending, budget allocation or saving behaviour (Research Design section, p. 72).

## Definitions

- **SARIMA** — Seasonal-ARIMA: ARIMA plus a seasonality contribution, written as the non-seasonal part ARIMA (p, d, q) and the seasonal part (P, D, Q), with m the number of observations per year.
- **TBATS** — Trigonometric seasonality, Box-Cox transformation, ARMA errors, Trend and Seasonal components.
- **BATS** — Box-Cox transformation, ARMA residuals, Trend component, Seasonal components; differs from TBATS only in the way it models seasonal effects.
- **Triple Exponential Smoothing (Holt-Winters method)** — Exponential smoothing that models seasonality, trend and level, adding the gamma (γ) parameter for the seasonal component and requiring a specified seasonal period; the study uses the additive method.
- **kNN regression** — A simple implementation that calculates the average, or an inverse-distance weighted average, of the numerical target of the K nearest neighbours, using the same distance functions as kNN classification.
- **SVR** — A regression algorithm working on the Support Vector Machine principle, fitting the error inside a margin called the ε-tube, supporting linear and non-linear regression; the study utilizes polynomial kernels.
- **HFCE** — Household Final Consumption Expenditure: families' spending on necessities such as food and drink, clothing, shelter, and health care.
- **ADF test** — A test that expands the Dickey-Fuller equation to include a high-order regressive process; the null hypothesis assumes a unit root, α=1, and a p-value below the significance level implies stationarity.
- **ACF** — A technique that plots the correlation coefficient against lag to show how correlated the values of a time series are; values beyond the significance limits, approximately α = 0.05, show evidence of correlation.
- **R²** — The proportion of variation of data points explained by the regression line or model, computed as the ratio of the sum of squared regression to the total sum of squares.
- **RMSE** — An ideal general-purpose error metric for numerical forecasts, scale-dependent and therefore valid only for comparing prediction errors of different models for a particular variable, with the smaller value the better performance.

## Key Equations

- `ARIMA(p, d, q) (P, D, Q)[m]` — SARIMA notation: non-seasonal orders, seasonal orders, m observations per year.
- `ŷ_{t+h|t} = ℓ_t + hb_t + s_{t+h−m(k+1)}` — Additive Holt-Winters forecast from level, trend and seasonal index.
- `ℓ_t = α(y_t − s_{t−m}) + (1 − α)(ℓ_{t−1} + b_{t−1})` — Level as weighted average of deseasonalized observation and non-seasonal forecast.
- `s_t = γ*(1 − α)(y_t − ℓ_{t−1} − b_{t−1}) + [1 − γ*(1 − α)]s_{t−m}` — Seasonal index with γ = γ*(1 − α) and 0 ≤ γ* ≤ 1.
- `MSE = (1/n) Σ (y_i − ŷ_i)²` — Mean of the squared prediction errors over the test set.
- `RMSE = √[(1/n) Σ (S_i − O_i)²]` — Root mean square error; observations O_i, predictions S_i, n observations.
- `MAE = (1/n) Σ |x_i − x̄|` — Mean of the absolute values of the individual prediction errors.
- `R² = SSR/SST = Σ(ŷ_i − ȳ)² / Σ(y_i − ȳ)²` — Variation explained by the model relative to the mean.
- `r̂_k = Σ_{t=k+1}^{n−k}(x_{t−k} − x̄)(x_t − x̄) / [n Σ_{t=1}^{n}(x_t − x̄)²]` — Auto-correlation at lag k.
- `y_t = c + βt + αy_{t−1} + φ₁ΔY_{t−1} + … + φ_pΔY_{t−p} + e_t` — ADF form whose null hypothesis is a unit root.
- `Ω(f) = γT + (1/2) λ Σ_{j=1}^{T} ω_j²` — XGBoost tree complexity, regularized to reduce overfitting.
- `K(X1, X2) = (a + X1ᵀX2)^b` — Polynomial kernel used by the SVR model.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Five-year HFCE growth rate forecast, SARIMA (1,0,0) (0,0,1) [4], train set | MSE | 5.0330 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, SARIMA (1,0,0) (0,0,1) [4], train set | RMSE | 2.2434 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, SARIMA (1,0,0) (0,0,1) [4], train set | MAE | 1.2566 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, SARIMA (1,0,0) (0,0,1) [4], test set | MSE | 0.3101 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, SARIMA (1,0,0) (0,0,1) [4], test set | RMSE | 0.5569 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, SARIMA (1,0,0) (0,0,1) [4], test set | MAE | 0.2677 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, Exponential Smoothing, train set | MSE | 6.9866 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, Exponential Smoothing, train set | RMSE | 2.6432 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, Exponential Smoothing, train set | MAE | 1.4267 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, Exponential Smoothing, test set | MSE | 13.0627 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, Exponential Smoothing, test set | RMSE | 3.6142 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, Exponential Smoothing, test set | MAE | 2.6146 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, TBATS, train set | MSE | 6.1459 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, TBATS, train set | RMSE | 2.4791 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, TBATS, train set | MAE | 1.2553 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, TBATS, test set | MSE | 0.4742 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, TBATS, test set | RMSE | 0.6887 | — | — | Table 1, p. 85 |
| Five-year HFCE growth rate forecast, TBATS, test set | MAE | 0.2484 | — | — | Table 1, p. 85 |
| Quarterly HFCE growth rate regression, SVR, as tabulated | MSE | 2.3970 | — | — | Table 2, p. 85 |
| Quarterly HFCE growth rate regression, SVR, as tabulated | RMSE | 1.5480 | — | — | Table 2, p. 85 |
| Quarterly HFCE growth rate regression, SVR, as tabulated | MAE | 1.1150 | — | — | Table 2, p. 85 |
| Quarterly HFCE growth rate regression, SVR, as tabulated | R2 | 0.8060 | — | — | Table 2, p. 85 |
| Quarterly HFCE growth rate regression, SVR, error values stated in the narrative | MSE | 6.413 | — | — | Sec. 3.4, p. 85 |
| Quarterly HFCE growth rate regression, SVR, error values stated in the narrative | RMSE | 2.532 | — | — | Sec. 3.4, p. 85 |
| Quarterly HFCE growth rate regression, kNN, as tabulated | MSE | 5.4230 | — | — | Table 2, p. 85 |
| Quarterly HFCE growth rate regression, kNN, as tabulated | RMSE | 2.3290 | — | — | Table 2, p. 85 |
| Quarterly HFCE growth rate regression, kNN, as tabulated | MAE | 1.3120 | — | — | Table 2, p. 85 |
| Quarterly HFCE growth rate regression, kNN, as tabulated | R2 | 0.5610 | — | — | Table 2, p. 85 |
| Quarterly HFCE growth rate regression, XGBoost, as tabulated | MSE | 6.4130 | — | — | Table 2, p. 85 |
| Quarterly HFCE growth rate regression, XGBoost, as tabulated | RMSE | 2.5320 | — | — | Table 2, p. 85 |
| Quarterly HFCE growth rate regression, XGBoost, as tabulated | MAE | 1.5710 | — | — | Table 2, p. 85 |
| Quarterly HFCE growth rate regression, XGBoost, as tabulated | R2 | 0.4810 | — | — | Table 2, p. 85 |
| Variability in the HFCE growth rate target explained by the SVR regression model | explained variability | 80.6% | — | — | Sec. 3.4, p. 85 |
| Philippine HFCE share of GDP | share of GDP | 73.5 % | — | — | Sec. 1 Introduction, p. 71 |
| Lowest quarterly HFCE growth rate recorded for 2000-2021 (Q2 2020) | growth rate | -15.32% | — | — | Sec. 3.1.1, p. 78 |
| Quarterly HFCE growth rate at the start of the recovery (Q2 2021) | growth rate | 7.31% | — | — | Sec. 3.1.1, p. 78 |
| Peak quarterly inflation rate (Q3 2008) | inflation rate | 12.20% | — | — | Sec. 3.1.2, p. 79 |
| Philippine unemployment rate, Q2 2020 | unemployment rate | 10% | — | — | Sec. 3.1.3, p. 80 |
| Philippine unemployment rate, Q3 2020 | unemployment rate | 18.9% | — | — | Sec. 3.1.3, p. 80 |
| Import of goods growth rate, Q2 2020 | growth rate | -38.48% | — | — | Sec. 3.1.4, p. 80 |
| Import of services growth rate, Q4 2020 | growth rate | -43.73% | — | — | Sec. 3.1.5, p. 81 |
| Export of goods growth rate, Q2 2020 | growth rate | -30.57% | — | — | Sec. 3.1.6, p. 82 |
| Export of services growth rate, Q2 2020 | growth rate | -36.01% | — | — | Sec. 3.1.7, p. 82 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "The SARIMA model had the lowest combined error of the train and test set, marking it as the best model for predicting the HFCE growth rate." | Abstract, p. 70 | sarima |
| "The best model to predict the quarterly HFCE growth rate from 2022 to 2026 was identified using error metrics, particularly RMSE, MSE, and MAE." | Abstract, p. 70 | model_performance_evaluation |
| "Therefore, models used to predict the HFCE growth rate over the next five years are significantly impacted using historical data, including the years when COVID-19 occurred." | Abstract, p. 70 | sarima |
| "The gathered data from this study covers the country's quarterly HFCE from 2001-2021." | Abstract, p. 70 | data_collection |
| "All the data came from the Time Series Data of the Philippine Statistics Authority (PSA)." | Sec. 2.1 Research Design, p. 72 | data_collection |
| "The researchers used the software RStudio and Orange to clean, organize, analyze, predict, and present the data." | Sec. 2.1.1 Statistical Tool, p. 72 | model_performance_evaluation |
| "SARIMA stands for Seasonal-ARIMA, and it includes seasonality contribution to the forecast." | Sec. 2.1.2.1, p. 72 | sarima |
| "The importance of seasonality is quite evident, and Auto Regression Integrated Moving Average (ARIMA) fails to encapsulate that information implicitly." | Sec. 2.1.2.1, p. 72 | sarima |
| "Like ARIMA, the P, D, and Q values for seasonal parts of the model can be deduced from the ACF and PACF plots of the data." | Sec. 2.1.2.1, p. 73 | sarima |
| "It exhibited the best model with SARIMA (1,0,0) (0,0,1) [4], which had the lowest Akaike Information Criterion (AIC)." | Sec. 3.2.1 SARIMA Model, p. 83 | sarima |
| "The results showed that the SVR algorithm outperformed the other two models in predicting the Philippines' Quarterly Household Final Consumption Expenditure (HFCE)." | Sec. 3.4, p. 85 | model_performance_evaluation |
| "The table reflected the lowest MSE (6.413), RMSE (2.532), and MAE (1.115) on SVR." | Sec. 3.4, p. 85 | model_performance_evaluation |
| "Thus, among the three models, SVR was the best regression algorithm for predicting the country's quarterly HFCE Growth Rate." | Sec. 3.4, p. 85 | model_performance_evaluation |
| "Thus, 80.6% of the variability observed in the target variable was explained by the regression model." | Sec. 3.4, p. 85 | model_performance_evaluation |
| "The results showed that SARIMA (1,0,0) (0,0,1) [4] was the best model for predicting the HFCE growth rate for the next five years." | Sec. 4 Conclusions, p. 86 | sarima |
| "In conclusion, based on the data, a drastic decline in the HFCE growth rate was observed when COVID-19 spread throughout the country." | Sec. 4 Conclusions, p. 86 | sarima |

## Remember This

- SARIMA (1,0,0)(0,0,1)[4] wins the time-series comparison; SVR wins the regression comparison, on separate setups.
- Data are quarterly Philippine national series from the PSA Time Series Data; no observation count is printed.
- Table 2's narrative contradicts its own numbers: it hands SVR the XGBoost row's MSE and RMSE.
- The pandemic's effect on the forecast is asserted in the conclusion and never tested.
- No stationarity result, no ACF/PACF plot and no prediction intervals are reported.

## Cited Works

- Chen, T.; Guestrin, C. (2016) (methodology) — XGBoost as gradient-boosted decision trees optimizing a loss function plus a regularization parameter (Sec. 2.1.2.4, p. 75; no reference-list entry).
- Hyndman, R. J.; Athanasopoulos, G. (2018) (methodology) — Forecasting textbook source for the additive Holt-Winters seasonal equations used in Sec. 2.1.2.2 [References, p. 88].
- Brownlee, J. (2019) (methodology) — A gentle introduction to SARIMA for time-series forecasting, cited in support of the SARIMA treatment [References, p. 87].
- Brownlee, J. (2021) (methodology) — XGBoost for regression, cited in support of the XGBoost treatment [References, p. 87].
- Han, R. (2022) (methodology) — Practical guide to what the TBATS model is and how to use it in R [References, p. 88].
- Karabiber, O. A.; Xydis, G. (2019) (baseline) — TBATS compared with ANN and ARIMA for Danish day-ahead electricity price forecasting [References, p. 88].
- Blaconá, M. T.; Andreozzi, L.; Magnano, L. (2014) (baseline) — Time-series models for different seasonal patterns [References, p. 87].
- Dela Cruz, A. (2019) (baseline) — Discrete wavelet transformation on a hybrid ARIMA-ANN model for forecasting Philippine HFCE on education [References, p. 87].
- Erero, J.; Makananisa, M. (2020) (baseline) — CGE, Holt-Winter and SARIMA analysis of the COVID-19 impact on the South African economy [References, p. 87].
- Qureshi, S.; Chu, B.; Demers, F. (2020) (baseline) — Forecasting Canadian GDP growth using XGBoost [References, p. 89].
- Rohmah, M. F.; et al. (2021) (baseline) — Comparison of four kernels of SVR to predict the consumer price index [References, p. 89].
- Priambodo, B.; et al. (2019) (baseline) — Predicting Indonesian GDP using k-nearest neighbour regression [References, p. 89].
- Long, G. (2010) (baseline) — GDP prediction by support vector machine trained with a genetic algorithm [References, p. 88].
- Arapova, E. (2018) (context) — Panel model of the determinants of household final consumption expenditures in Asian countries, 1991-2015 [References, p. 87].
- Varlamova, J.; Larionova, N. (2015) (context) — Macroeconomic and demographic determinants of household expenditures in OECD countries [References, p. 90].

---

Conversion: [`L--Dasmarinas-2024_marked.md`](../../literature/paper-markdowns/L--Dasmarinas-2024_marked.md)
