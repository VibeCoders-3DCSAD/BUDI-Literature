---
paper_id: I--Hyndman-2007
first_author: Hyndman
year: 2007
title: "Minimum Sample Size Requirements for Seasonal Forecasting Models"
venue: "Foresight: The International Journal of Applied Forecasting"
doi: Not reported
type: journal article
designation: international
status: extracted
modules: [sarima]
module_rationale:
  sarima: "The paper derives minimum sample-size requirements for seasonal forecasting models (including seasonal ARIMA and related seasonal approaches), showing the requirements depend on model complexity and the amount of random variation in the data."
---
`I--Hyndman-2007` — Hyndman and Kostenko (2007), *Foresight: The International Journal of Applied Forecasting* (6, 12–15).

## Summary

This practice article answers the common business question of how much historical data are needed to forecast with a seasonal model. Hyndman and Kostenko show that the minimum sample size depends on the number of parameters in the seasonal model and the signal-to-noise ratio, and they document specific minimum requirements for common seasonal forecasting models. The article warns that published tables of minimum sample sizes are often overly simplified.

## Problem and Motivation

Practitioners need guidance on the minimum length of a seasonal time series for reliable forecasting. A naive rule such as “use at least two or three years” is not sufficient, and the answer depends on model complexity and random variation in the data.

## Method

**Design.** Theoretical/analytical derivation for minimum sample size requirements (practice article).  
**Sample.** Not applicable (no empirical dataset analyzed).  
**Context.** Geography: Not reported; population: Not reported; setting: seasonal forecasting practice.

- Derive minimum sample size requirements as a function of the number of parameters and the amount of random variation in the data.
- Present minimum requirements for common seasonal forecasting models.
- Caution that real data contain random variation and sample size requirements increase accordingly.
- Note that older data need not be discarded if a good model allows for changing trend and seasonal patterns.

## Key Findings

- The minimum sample size required depends on the type of statistical model being used and the amount of random variation in the data.
- Specific minimum sample-size requirements are documented for common seasonal forecasting models.
- The minimum requirements apply when random variation is very small; real data often contain more variation and sample sizes must increase accordingly.
- Published tables on sample-size requirements are often overly simplified.

## Limitations and Gaps

- The article is a short practice piece (four pages) and does not present full derivations or a broad empirical evaluation; it provides guidance rather than a comprehensive simulation study.

## Definitions

Not reported.

## Key Equations

Not reported.

## Statistical Evidence

Not reported.

## Quotes

Not reported.

## Remember This

- Minimum data needed for seasonal forecasting depends on model parameters and noise.
- Requirements increase when random variation is high.
- Published minimum-sample tables are often oversimplified.
- More data is not automatically useless if the model allows changing trends/seasonality.

## Cited Works

- Not reported.

---

Conversion: [Hyndman & Kostenko, 2007_marked.md](../../literature/mds/Hyndman & Kostenko, 2007_marked.md)
