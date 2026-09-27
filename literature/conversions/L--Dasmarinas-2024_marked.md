---
conversion_metadata:
  converted_at: "2026-09-27T06:26:34Z"
  converter_tool: "markitdown"
  converter_version: "0.1.7"
  source_pdf: "Dasmarinas et al., 2024.pdf"
  source_pdf_sha256: "8b56774e65027d006dc627e9962e8c90330bfdfecaa90ba026e5bed2b5cffc1d"
  page_count: 21
  markdown_char_count: 88956
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

.

FORECASTING THE IMPACT OF COVID-19 ON THE HOUSEHOLD FINAL 
CONSUMPTION EXPENDITURE (HFCE) IN THE PHILIPPINES

ANDRE PERRY P. DASMARIÑAS1, GWENETH H. DE CASTRO2, BEA JANE M. 
LAZONA3, AND LAURENCE P. USONA2

1Accenture Inc., Bonifacio Global City, Uptown Tower 3, Taguig City 1637, Philippines 
2Polytechnic University of the Philippines, Sta. Mesa, Manila 1016, Philippines 
3AMI Risk Consultants Inc., Wilson St., Brgy. Maytunas, San Juan City 1500, Philippines

Abstract: The Household Final Consumption Expenditure (HFCE) is a significant component of the Philippine 
economy. The term "HFCE" refers to families' spending on necessities such as food and drink, clothing, shelter, 
and health care. The gathered data from this study covers the country’s quarterly HFCE from 2001-2021. The 
study  used various  forecasting  methods, including Triple  Exponential  Smoothing,  Seasonal  Autoregressive 
Integrated  Moving  Average  (SARIMA),  and  TBATS  in  modeling  time  series  data  to  depict  the  effects  of 
COVID-19 on the country’s HFCE Growth Rate. The best model to predict the quarterly HFCE growth rate 
from 2022 to 2026  was identified  using error  metrics, particularly  RMSE, MSE,  and MAE.  The  SARIMA 
model had the lowest combined error of the train and test set, marking it as the best model for predicting the 
HFCE  growth  rate.  Moreover,  the  HFCE  growth  rate  was  also  predicted  using  various  machine  learning 
regression algorithms (SVR, XGBoost, and kNN), with a variety of economic indicators as the independent 
variables,  including the inflation  rate,  unemployment  rate,  import of goods  growth  rate, import of  services 
growth  rate,  export of  goods growth rate,  and  export of  services  growth  rates.  The  results  of error  metrics 
showed that SVR was the best regression algorithm for predicting the Philippines’ quarterly HFCE Growth 
Rate. The findings of this study indicate that as COVID-19 spread over the country, the HFCE growth rate 
dramatically decreased. Therefore, models used to predict the HFCE growth rate over the next five years are 
significantly impacted using historical data, including the years when COVID-19 occurred.

Keywords: COVID-19, Extreme Gradient Boosting (XGBoost), Household Final Consumption Expenditure 
(HFCE), kNN Regression, Support Vector Regression (SVR), TBATS, Triple Exponential Smoothing.

1. INTRODUCTION

The  COVID-19  pandemic  has  sparked  a  global  health  crisis,  requiring  several 
governments  to  implement  stringent  preventive  measures  to  stem  the  virus'  spread, 
including national lockdowns and social distancing measures. The first case of COVID-
19 infection in the Philippines was reported in January 2020, and by March, the country 
was placed under a strict community quarantine  that restricted mobility and business 
activities. While these measures have slowed the community spread of COVID-19, they 
have significant adverse impacts on family incomes, jobs, education of children, food 
security,  and  businesses.  A  pandemic  can  disrupt  the  economy  in  a  variety  of  ways. 
Human behavioral changes, such as fear-induced aversion to places of work and public 
gatherings,  were  a  significant  cause  of  economic  damage,  besides  the  impact  of 
mitigation measures (Madhav et al., 2017). The adverse effects of various pandemics on 
inhabitants'  household  income  have  been  established  in  the  past  literature.  The  2020 
economic contraction was the highest annual decline ever reported since the National 
Accounts  data  series  for  the  Philippines  began  in  1946.  The  final  consumption  of 
households was mostly the biggest component of  the Gross Domestic Product (GDP) 
among  the  Association  of  Southeast  Asian  Nations  (ASEAN)  countries  on  the

---

<!-- PAGE 2 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

expenditure side. In the Philippines, Household Final Consumption Expenditure (HFCE) 
was 73.5 % of the GDP, making it an essential component in demand analysis.

As  stated  in  IHS  Markit  Philippines  Manufacturing  PMI  (Biswas,  2021),  the 
Household Final Consumption Expenditure  (HFCE) went down by 7.9%, while gross 
capital formation contracted by 34.4%. Drastic declines in output were reported in some 
sectors of the economy, with the transport and storage industry marking a 30.9% decline, 
while  accommodation  and  food  services  output  went  down  by  45.4%.  Meanwhile, 
according to the Philippine Statistics Authority (PSA), during the third quarter of 2020, 
the unemployment rate increased to 18.9%. Further, World Bank's research said that only 
1 in 10 households that operated a business accessed financial services. The incidence of 
revenue losses among household businesses showed improvement, with the wealthiest 
households  recovering  faster  than  the  poorest  households.  Nearly  two  out  of  five 
households were anxious about not having enough food for the following week. While 
food security continued to improve overall, concerns among households remained. The 
share of household heads unable to buy at least one of the food staples remained the same 
at around 40%, primarily because of food unaffordability. Fewer households reported 
eating less than usual and worried about not having enough food. Households that needed 
medical  treatment  increased  to  28%  in  December  from  20%  in  August  2021.  More 
households cited lack of money as a reason for inadequate access to treatment. However, 
based on the report of the Statista Research Department, in 2021, the HFCE for health in 
the  Philippines  was  valued  at  approximately  627  billion  Philippine  pesos.  Household 
spending on health has gradually increased over the past five years and was highest in 
2021 after the COVID-19 pandemic outbreak. Undeniably, COVID-19 played a massive 
part in the shift of the economy and household expenditure, and the researchers, being 
the children of the working class who were greatly affected by the pandemic, saw the 
need for this study to be conducted.

This  study  aimed  to  depict  the  impact  of  COVID-19  on  the  Household  Final 
Consumption  Expenditure  (HFCE)  Growth  Rate  in  the  Philippines,  wherein  different 
forecasting  methods  were  used  to  model  time  series  data,  particularly  Seasonal 
Autoregressive Integrated Moving Average (SARIMA); Triple Exponential Smoothing; 
and  Trigonometric  seasonability,  Box-Cox  transformation,  ARMA  errors,  Trend 
components and Seasonal components (TBATS). Further, the best model was identified 
to  forecast  the  country’s  HFCE  Growth  Rate.  Moreover,  different  machine  learning 
regression  algorithms  such  as  support  vector  machine  (SVM)  regression,  extreme 
gradient boosting (XGBoost), and k-nearest neighbors (kNN) were used to predict the 
HFCE growth rate, applying various economic indicators as the independent variables, 
namely: Inflation Rate, Unemployment Rate, Import of Goods Growth Rate, Import of 
Services Growth Rate, Export of Goods Growth Rate, and Export of Services Growth 
Rate. Thus, the model with the lowest error metrics – root mean square error (RMSE), 
mean  squared  error  (MSE), mean  absolute  error  (MAE), and  highest  R  squared  were 
selected  as  the  best  machine  learning  regression  algorithms  for  predicting  the  HFCE 
growth rate.

The  primary  purpose  of  this  study  is  to  forecast  the  impact  of  the  COVID-19 
pandemic on the Philippines’  HFCE growth rate  from 2022-2026 through time series 
forecasting models and to identify which model is the best. Moreover, this paper also 
aims  to  determine  the  best  machine-learning  regression  algorithm  for  predicting  the 
country’s HFCE growth rate.

[71]

---

<!-- PAGE 3 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

2. METHODOLOGY

2.1

Research Design

This research was conducted using different time series forecasting models, namely 
SARIMA,  Triple  Exponential  Smoothing,  and  TBATS  in  forecasting  the  quarterly 
HFCE  Growth  Rate  of  the  Philippines.  In  addition,  regression  algorithm  in  machine 
learning was also used in the study and further identified which among them is the best 
for predicting the country’s quarterly HFCE Growth Rate. To supplement the statistical 
analysis performed in this study, the researchers relied on several sets of secondary data 
relating to the HFCE Growth Rate, Inflation Rate, Unemployment Rate, Import of Goods 
Growth Rate, Import of Services Growth Rate, Export of Goods Growth Rate and Export 
of Services Growth Rate. All the data came from the Time Series Data of the Philippine 
Statistics  Authority  (PSA).  PSA  serves  as  the  central  statistical  authority  of  the 
Philippine government on primary data collection.

2.1

Statistical Data Analysis Procedures

2.1.1

Statistical Tool

The researchers used the software RStudio and Orange to clean, organize, analyze, 
predict, and present the data. RStudio software was used to forecast future HFCE Growth 
Rate  values  by  operating  SARIMA,  Triple  Exponential  Smoothing,  and  TBATS.  In 
addition, this software was used to identify the models’ accuracy.  RStudio was a free 
software environment commonly used by statisticians to convey statistical computation 
and graphics. Furthermore, Orange was used in determining which among the machine 
learning  regression  algorithms  had  the  lowest  values  of  error  metrics,  particularly 
Extreme  Gradient  Boosting  (XGBoost),  k-nearest  neighbors  (kNN)  Regression,  and 
Support  Vector  Machine  (SVM)  Regression  in  predicting  HFCE,  considering  the 
dependent variables. Orange was an open-source data visualization, machine learning, 
and data mining toolkit. It featured a visual programming front-end for explorative rapid 
qualitative data analysis and interactive data visualization.

2.1.2

Statistical Treatment of Data

2.1.2.1

Seasonal Autoregressive Integrated Moving Average (SARIMA)

SARIMA stands for Seasonal-ARIMA, and it includes seasonality contribution to 
the  forecast.  The  importance  of  seasonality  is  quite  evident,  and  Auto  Regression 
Integrated Moving Average  (ARIMA) fails to encapsulate that information implicitly. 
The Autoregressive (AR), Integrated (I), and Moving Average (MA) parts of the model 
remain as that of ARIMA. The addition of Seasonality adds robustness to the SARIMA 
model. It is represented as:

[72]

---

<!-- PAGE 4 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

ARIMA      (p, d, q)

(P, D, Q)

Non-seasonal part of 
the model

Seasonal part of 
the model

where 𝑚 is the number of observations per year. We used the uppercase notation 
for the seasonal parts of the model, and lowercase notation for the non-seasonal parts of 
the model. Like ARIMA, the P, D, and Q values for seasonal parts of the model can be 
deduced from the ACF and PACF plots of the data. The researchers used this model to 
predict the next five years’ quarterly data on HFCE Growth Rate, from 2022 to 2026.

Assumptions:

i.  Data should be univariate

The data type that should be used consists of observations with a single characteristic

or attribute.

ii.  Data should be stationary

The  properties  of  a  series  should  not  depend  on  the  time  when  it  is  captured.  In

addition, it must have a constant variance, covariance, and mean.

2.1.2.2

Triple Exponential Smoothing (Holt-Winters method)

Triple exponential smoothing can model seasonality, trend, and level components 
for univariate time series data. Seasonal cycles are patterns in the data that occur over a 
standard number of observations. Triple exponential smoothing is also known as Holt-
Winters Exponential Smoothing. This method adds in the gamma (γ) parameter to account 
for the seasonal component. For this method, you must specify the period for the seasonal 
cycle.  This  study  has  used  the  additive  method.  The  component  form  for  the  additive 
method is:

𝑦̂𝑡+ℎ\𝑡 = ℓ𝑡 + ℎ𝑏𝑡 + 𝑠𝑡+ℎ−𝑚(𝑘+1) 
ℓ𝑡 = 𝛼(𝑦𝑡 − 𝑠𝑡−𝑚) + (1 − 𝛼)(ℓ𝑡−1 + 𝑏𝑡−1) 
𝑏𝑡 = 𝛽∗(ℓ𝑡 − ℓ𝑡−1) + (1 − 𝛽∗)𝑏𝑡−1 
𝑠𝑡 = γ(𝑦𝑡 − ℓ𝑡−1 − 𝑏𝑡−1) + (1 − γ)𝑠𝑡−𝑚,

where 𝑘 is the integer part of (ℎ − 1)/𝑚, which ensures that the estimates of the seasonal 
indices used for forecasting come from the final year of the sample. The level equation 
showed a weighted average between the seasonally adjusted observation 𝑦𝑡 − 𝑠𝑡−𝑚and 
the non-seasonal forecast (ℓ𝑡−1 + 𝑏𝑡−1) for time 𝑡. The trend equation was identical to 
Holt’s  linear  method.  The  seasonal  equation  showed  a  weighted  average  between  the 
current seasonal index, (𝑦𝑡 − ℓ𝑡−1 − 𝑏𝑡−1), and the seasonal index of the same season 
last year (i.e., mm time periods ago).

The equation for the seasonal component is often expressed as:

𝑠𝑡 = 𝛾∗(𝑦𝑡 − ℓ𝑡) + (1 − 𝛾∗)𝑠𝑡−𝑚.

[73]

---

<!-- PAGE 5 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

If  we  substitute ℓt from  the  smoothing  equation  for  the  level  of  the  component  form 
above, we get

𝑠𝑡 = 𝛾∗(1  − 𝛼)(𝑦𝑡 − ℓ𝑡−1  − 𝑏𝑡−1) + [1 − γ∗(1 − α)]𝑠𝑡−𝑚,
which is identical to the smoothing equation for the seasonal component we specify here, 
with  𝛾 = 𝛾∗(1 − 𝛼). The  usual  parameter  restriction  is  0 ≤ 𝛾∗ ≤ 1, which  translates
to 0  ≤ 𝛾 ≤  1 − 𝛼.

2.1.2.3

TBATS

The  names  were  acronyms  for  key  features  of  the  models:  Trigonometric 
seasonality,  Box-Cox  transformation,  Auto  Regression  Integrated  Moving  Average 
(ARMA) errors, and Trend and Seasonal components.  TBATS model took its roots in 
exponential smoothing methods and can be described by the following equations:

λ = 𝑙𝑡−1 + ф𝑏𝑡−1 + ∑ 𝑠𝑡−𝑚𝑖
𝑦𝑡

(𝑖)

+ 𝑑𝑡

𝑇

𝑖=1

𝑙𝑡 = 𝑙𝑡−1 + ф𝑏𝑡−1 + 𝛼𝑑𝑡
𝑏𝑡 = ф𝑏𝑡−1 + 𝛽𝑑𝑡
𝑝

𝑞

𝑑𝑡 = ∑ φ𝑖𝑑𝑡−𝑖 + ∑ 𝛳𝑖𝑒𝑡−𝑖 + 𝑒𝑡

𝑖=1

𝑖=1

where: 
λ- time series at moment 𝑡 (Box-Cox transformed)
𝑦𝑡
(𝑖)- ith seasonal component
𝑠𝑡
𝑙𝑡- local level
𝑏𝑡- trend with damping
𝑑𝑡- ARMA(p,q) process for residuals
𝑒𝑡- Gaussian white noise

Seasonal Part:

𝑘𝑖
(𝑖) =   ∑ 𝑠𝑗,𝑡
𝑠𝑡

(𝑖)

𝑗=1

(𝑖) = 𝑠𝑗,𝑡−1
𝑠𝑗,𝑡
(𝑖) = −𝑠𝑗,𝑡−1
𝑠𝑗,𝑡

(𝑖) 𝑐𝑜𝑠(ωi) + 𝑠𝑗,𝑡−1
(𝑖) 𝑠𝑖𝑛(ωi) + 𝑠𝑗,𝑡−1
ω𝑖 = 2𝜋𝑗/𝑚𝑖

∗(𝑖) 𝑠𝑖𝑛(ωi) + ɣ1
∗(𝑖) 𝑐𝑜𝑠(ωi) + ɣ2

(𝑖)𝑑𝑡
(𝑖)𝑑𝑡

Model Parameters:

𝑇   - Amount of seasonalities 
𝑚𝑖 - Length of the 𝑖th seasonal period
𝑘𝑖   - Amount of harmonics for the 𝑖th seasonal period
λ – Box-Cox transformation 
𝛼, 𝛽 – Smoothing 
ф    - Trend damping 
𝜑𝑖, 𝛳𝑖 – ARMA(p,q) coefficients
(𝑖), ɣ2
ɣ1

(𝑖) – Seasonal smoothing (two for each period)

[74]

---

<!-- PAGE 6 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

Each  seasonality  was  modeled  by  a  trigonometric  representation  based  on  the 
Fourier series. One major advantage of this approach was that it required only (two) 2 
seed states regardless of the length of the period. Another advantage was the ability to 
model  seasonal  effects  of  non-integer  lengths.  For  example,  given  a  series  of  daily 
observations, one can model leap years with  a season of length 365.25. BATS, which 
stands  for  Box-Cox  transformation  ARMA  residuals  Trend  component  in  the  model 
Seasonal components, differed from TBATS only in the way it models seasonal effects. 
In BATS, we had a more traditional approach where each seasonality was modeled by:

(𝑖) = 𝑠𝑡−𝑚𝑖
𝑠𝑡

(𝑖) + ɣi𝑑𝑡.

This  implied  that  BATS  can  only  model  integer  period  lengths.  The  approach 
taken in BATS requires mi seed states for season 𝑖, if this season is long the model may 
become intractable.

2.1.2.4

Extreme Gradient Boosting (XGBoost)

XGBoost was a short-term for the eXtreme Gradient Boosting algorithm developed 
by Chen and Guestrin (2016). It was an implementation of gradient-boosted decision trees 
designed for speed and performance and was a more efficient version of gradient-boosting 
decision trees. The main objective of the algorithm was to optimize parameters given an 
objective  function  that  contains  a  loss  function  and  a  regularization  parameter.  The 
regularization  term  aimed  to  reduce  the  likelihood  of  overfitting  by  controlling  the 
complexity of constructed trees. The complexity of each tree follows the equation:

Ω(𝑓) = 𝛾𝑇 +

1
2

𝑇
2
𝜆 ∑ 𝜔𝑗
𝑗=1

where T is the number of leaves and ω is the vector scores on leaves (Chen and Guestrin, 
2016). The structure score, objective function, of the algorithm is defined as:

𝑇

𝐹 = ∑(𝐺𝑗𝜔𝑗 +

𝑗=1

1
2

(𝐻𝑗 + λ)𝜔𝑗

2)   + γ𝑇

where𝜔𝑗 are independent of each other and the form 𝐺𝑗𝜔𝑗 +

1

2

(𝐻𝑗 + λ)𝜔𝑗

2 is quadratic.

2.1.2.5

K-nearest neighbors (kNN) regression

A  simple  implementation  of  kNN  regression  was  to  calculate  the  average  of  the 
numerical target of the K nearest neighbors.  Another approach used an inverse distance 
weighted  average  of  the  K  nearest  neighbors.  kNN  regression  used  the  same  distance 
functions as kNN classification.

[75]

---

<!-- PAGE 7 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

Distance Functions

Euclidean:                √∑ (𝑥𝑖 − 𝑦𝑖)2

𝑘
𝑖=1
∑ |𝑥𝑖 − 𝑦𝑖|

𝑘
𝑖=1

Manhattan

𝑘
Minkowski(∑ (|𝑥𝑖 − 𝑦𝑖|𝑞
𝑖=1

1
)
𝑞

The above three distance measures were only valid for continuous variables. Thus, this 
study used the Euclidean Distance Function.

2.1.2.6

Support Vector Regression (SVR)

This  was  a  regression  algorithm  that  supported  both  linear  and  non-linear 
regressions. This method worked on the principle of the Support Vector Machine. SVR 
was  a  regression  that  was  used  for  predicting  continuous  ordered  variables.  In  simple 
regression, the idea was to minimize the error rate while in SVR the idea was to fit the 
error inside a certain threshold, which means that SVR’s work  was to approximate the 
best value within a given margin called ε- tube. Moreover, this study utilized polynomial 
kernels. In general, the polynomial kernel was defined as:

𝐾(𝑋1, 𝑋2) = (𝑎 + 𝑋1

𝑇𝑋2)𝑏

2.1.2.7

Mean Squared Error (MSE)

The mean squared error of a model concerning a test set was the mean of the squared 
prediction errors over all instances in the test set. The prediction error was the difference 
between the true value and the predicted value for an instance.

𝑀𝑆𝐸 =

𝑛
𝑖=1

∑ (𝑦𝑖 − 𝑦𝑖)2
𝑛

where:

𝑛 - the total number of terms for which the error is to be calculated

𝑦𝑖 - the observed value of the variable

𝑦𝑖 - the predicted value of the variable

2.1.2.8

Root Mean Square Error (RMSE)

Root Mean Squared Error Root mean squared error (RMSE) was the square root of 
the mean of the square of all the errors. The use of RMSE was widespread, and it was 
regarded as an ideal general-purpose error metric for numerical forecasts.

𝑅𝑀𝑆𝐸 = √

1
𝑛

𝑛
∑(𝑆𝑖 − 𝑂𝑖)2
𝑖=1

[76]

---

<!-- PAGE 8 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

where:

𝑂𝑖are the observations,  
𝑆𝑖are the predicted values of a variable, and  
𝑛is the number of observations available for analysis.

RMSE was a good measure of accuracy, but only to compare prediction errors of 
different  models  or  model  configurations  for  a  particular  variable  and  not  between 
variables,  as  it  is  scale-dependent.  Meanwhile,  the  smaller  the  value,  the  better  the 
model’s performance.

2.1.2.9

Mean Absolute Error (MAE)

Mean Absolute Error was a model evaluation metric used with regression models. 
The mean absolute error of a model to a test set was the mean of the absolute values of 
the individual prediction errors on overall instances in the test set. Each prediction error 
was the difference between the true value and the predicted value for the instance.

where:

𝑀𝐴𝐸 =

𝑛
𝑖=1

∑ |(𝑥𝑖 − 𝑥)|
𝑛

𝑛 = the number of errors 
Σ = summation symbol (which means “add them all up”) 
|(𝑥𝑖 − 𝑥)| = the absolute errors

2.1.2.10

Coefficient of determination (R²)

This referred to the proportion of variation of data points explained by the regression 
line or model. It can be determined as a ratio of the total variation of data points explained 
by the regression line (Sum of squared regression) and the total variation of data points 
from the mean (also termed as sum of squares total or total sum of squares). The following 
formula represents the ratio.

𝑅2 =

𝑆𝑆𝑅
𝑆𝑆𝑇

=

∑(𝑦̂𝑖  − 𝑦̅)2
∑(𝑦𝑖 − 𝑦̅)2

where:

𝑦̂𝑖 represents the prediction or a point on the regression line,

𝑦̅represents the mean of all the values, and

𝑦𝑖represents the actual values or the points.

2.1.2.11

Auto-Correlation Function (ACF)

Auto-correlation  function  (ACF)  was  a  statistical  technique  used  to  identify  how 
correlated  the  values  in  a  time  series  are  with  each  other  by  plotting  the  correlation 
coefficient against lag. The data values beyond the significance limits were statistically 
significant at approximately  α  =  0.05,  which  shows  evidence  of  correlation.  ACF  was 
formulated as follows:

∑

𝑟̂𝑘 =

𝑛−𝑘
𝑡=𝑘+1

(𝑥𝑡−𝑘 − 𝑥)(𝑥𝑡 − 𝑥)
𝑛
∑ (𝑥𝑡 − 𝑥)
𝑡=1

2

[77]

---

<!-- PAGE 9 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

where:

𝑘 = Lag; 𝑘 = 1,2, … , 𝑛 
𝑥𝑡= Value of 𝑥 at row 𝑡 
𝑥= Mean of 𝑥 
𝑛= Number of observations in the series

2.1.2.12

Augmented Dickey-Fuller Test (ADF)

Augmented  Dickey-Fuller  Test  (ADF)  was  a  statistical  test  for  analyzing  the 
stationary of a series. The ADF test expanded the Dickey-Fuller test equation to include 
a high-order regressive process in the model. The null hypothesis assumed the presence 
of a unit root, that  was α=1; the p-value obtained should be less than the significance 
level to reject the null hypothesis; thereby, inferring that the series was stationary. ADF 
was formulated as follows:

𝑦𝑡 = 𝑐 + 𝛽𝑡 + 𝛼𝑦𝑡−1 + ф1 △ 𝑌𝑡−1 + ф2 △ 𝑌𝑡−2. . +ф𝑝 △ 𝑌𝑡−𝑝 + 𝑒𝑡

where:

𝑡 = Time index, 
𝛼 = Intercept constant called a drift, 
𝛽 = Coefficient on a time trend, 
𝛾 = Coefficient presenting process root, i.e. the focus of testing, 
𝑝 = Lag order of the first-differences autoregressive process, 
𝑒𝑡= Independent identically distributed residual term.

3. RESULTS AND DISCUSSION

This section presented the purpose of the study, research design, data source for

secondary data, and statistical data analysis procedures.

3.1

Graphs of the Behavior of Specific Variables

3.1.1

Household Final Consumption Expenditure

Figure  3  shows  that  the  graph  exhibited  a  major  downward  trend  from  the  2nd 
quarter of 2020 to the 1st quarter of 2021, recording all quarters within this duration with 
a negative growth rate. The lowest HFCE growth rate recorded for 2000-2021 was during 
the 2nd quarter of 2020 with -15.32%. One of the reasons for this decline was due to the 
government's preventive measures, primarily when lockdowns were implemented; thus, 
limiting the exposure of people outside their homes. On the other hand, in the 2nd quarter 
of 2021 began to display a growth rate of 7.31%.

[78]

---

<!-- PAGE 10 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

Figure 3.  Philippines’ household final consumption expenditure from Q1 2000 to Q4

2001.

3.1.2

Inflation rate

Based on Figure 4, the inflation rate in the country from the 2nd quarter of 2007 was 
at  2.4%  and  continuously  increased  until  the  3rd quarter  of  2008,  reaching  its  peak  at 
12.20%. The lowest point of the quarterly data of inflation rate for 2000-2021 was in the 
third quarter of 2009 with 0.3%. On the other hand, the inflation rate during the COVID-
19 pandemic caused no significant changes.

Figure 4. Philippines’ inflation rate from Q1 2000 to Q4 2001.

[79]

---

<!-- PAGE 11 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

Figure 5. Philippines’ unemployment rate from Q1 2000 to Q4 2001.

3.1.3

Unemployment Rate

Figure 5 shows the unemployment rate in the Philippines from the 1st quarter of 
2000 to the 4th quarter of 2021. It can be inferred that in the 4th quarter of 2005, there was 
a sudden decline in the unemployment rate. It continued to decline until it rose to 8.7% 
in the first quarter of 2018. It immediately declined again for the next quarters up to the 
extent that its lowest record was at 4.5% during the 4th quarter of 2019, which is a good 
indication in terms of unemployment.  However, due to the COVID-19 pandemic, the 
unemployment growth rate in the country began to increase rapidly starting from the 2nd 
quarter of 2020 with 10% and 18.9% during the 3rd quarter of 2020.

3.1.4

Import of Goods

Figure 6 shows the growth rate of import of goods in the Philippines from the 1st 
quarter of 2000 to the 4th quarter of 2021. The import of goods growth rate experienced 
a  major  decline  that  started  in  the  3rd  quarter  of  2001,  from  20.67%  to  -0.22%.  It 
continued to decline until it rose to 18.48% in the 4th quarter of 2002. Unfortunately, it 
immediately  declined  again  for  the  following  quarters,  until  it  showed  another  major 
decline in the 1st quarter of 2009, which had a -10.69% rate. In the 1st quarter of 2010, it 
showed  a  major  increase  with  a  28.36%  rate,  and  though it  experienced  a  downward 
trend, it stayed stable for the following quarters. In the 2nd quarter of 2020, the lowest 
import of goods was recorded at -38.48% and continued to decline until the last quarter 
of the year. This decline was a visible result of the COVID-19 pandemic. Fortunately, it 
was slowly showing a major upward trend starting from the 2nd quarter of 2021, with 
48.45%.

[80]

---

<!-- PAGE 12 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

Figure 6. Philippines’ import of goods growth rate from Q1 2000 to Q4 2001.

3.1.5

Import of Services

Figure 7 shows the growth rate of import of services in the Philippines from the 1st 
quarter of 2000 to the 4th quarter of 2021. The import of services growth rate experienced 
a major decline that started in the 4th quarter of 2001, from 31.16% to -8.33%. As the 
import of services gradually increased through the years, reaching its peak at 39.86% 
during the 3rd quarter of 2008, it immediately went down in the following years and the 
lowest  ever  recorded  was  from  the  4th  quarter  of  2020  with  a  value  of  -43.73%. 
Fortunately, it was slowly showing a major upward trend starting from the 2nd quarter of 
2021 at 1.03%.

Figure 7. Philippines’ import of services growth rate from Q1 2000 to Q4 2001.

[81]

---

<!-- PAGE 13 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

3.1.6

Export of Goods

Figure 8. Philippines’ export of goods growth rate from Q1 2000 to Q4 2001.

Figure 8 shows the growth rate of export of goods in the Philippines from the 1st 
quarter of 2000 to the 4th quarter of 2021. The export of goods’ growth rate experienced 
a  major  decline  that  started  in  the  2nd  quarter  of  2001,  from  9.32%  to  -10.56%.  It 
continued to decline until it rose to 28.88% in the 1st quarter of 2010. Unfortunately, it 
immediately  declined  again  for  the  following  quarters  until  it  showed  another  major 
decline in the 1st quarter of 2013 which had a -12.72% rate. In the 1st quarter of 2014, it 
showed  a  major  increase  with  a  14.13%  rate,  and  though it  experienced  a  downward 
trend, it stayed stable for the following quarters. In the 2nd quarter of 2020, the lowest 
export of goods was recorded at -30.57% and continued to decline until the last quarter 
of the year. This decline was a visible result of the COVID-19 pandemic. Fortunately, it 
was slowly showing a major upward trend starting from the 2nd quarter of 2021, with 
35.94%.

3.1.7

Export of Services

Figure 9 shows the growth rate of export of services in the Philippines from the 1st 
quarter of 2000 to the 4th quarter of 2021. The export of services growth rate experienced 
a major decline that started in the 4th quarter of 2003, from 28% to 0.47%. As the import 
of services gradually increased through the years reaching its peak at 57.09% during the 
3rd quarter of 2005, it immediately went down in the following years and the lowest ever 
recorded was from the 2nd quarter of 2020 with a value of -36.01%. Fortunately, it was 
slowly showing a major upward trend starting from the 2nd quarter of 2021 at 20.17%.

[82]

---

<!-- PAGE 14 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

Figure 9. Philippines’ export of services growth rate from Q1 2000 to Q4 2001.

3.2

Five-year Predicted Values of the Household Final Consumption Expenditure

3.2.1

SARIMA Model

Figure  10  presents  the  plot  of  the  Household  Final  Consumption  Expenditure 
Growth Rate prediction for 2022 to 2026 using the SARIMA model. It exhibited the best 
model  with  SARIMA  (1,0,0)  (0,0,1)  [4],  which  had  the  lowest  Akaike  Information 
Criterion (AIC).

Figure 10. HFCE growth rate predicted values for 2022 – 2026 using SARIMA.

[83]

---

<!-- PAGE 15 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

3.2.2

Triple Exponential Smoothing Model

Figure  11.  HFCE  growth  rate  predicted  values  for  2022  -  2026  using  exponential

smoothing.

Figure 11 exhibited the plot of Household Final Consumption Expenditure Growth 
Rate prediction for 2022 to 2026 using the Triple Exponential Smoothing model. The 
best model was ETS (1,0,0) which incorporated a smoothing factor of  0.9454, a trend 
smoothing factor of  0.0002, and a 0.0001 seasonal change smoothing factor.

3.2.3

TBATS model

Figure 12 shows the plot of household final consumption expenditure growth rate 
prediction for 2022 to 2026 using the TBATS model. The  best model was calculated 
using TBATS () functions in the R program with TBATS (1, {0, 0}, 0.8, -). Furthermore, 
this model constituted a damping parameter of 0.8, an alpha of 1.0222, and a beta of  -
0.2627.

Figure 12. HFCE growth rate predicted values for 2022 - 2026 using TBATS.

[84]

---

<!-- PAGE 16 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

3.3 
Expenditure

Best Statistical Model for Predicting Household Final Consumption

Table 1 presents the comparison of accuracy for the five-year forecast of Household 
Final  Consumption  Expenditure  Growth  Rate  using  SARIMA,  Triple  Exponential 
Smoothing,  and  TBATS.  The  models  with  the  lowest  combined  Mean  Squared  Error 
(MSE), Root Mean Square Error (RMSE), and Mean Absolute Error (MAE) for train 
and test sets were chosen as the best models. This depicted that SARIMA (1,0,0) (0,0,1) 
[4] performed the best model for predicting the HFCE from 2022 to 2026 with combined
train (MSE = 5.0330, RMSE = 2.2434, MAE = 1.2566) and test (MSE = 0.3101, RMSE
= 0.5569, MAE = 0.2677) set, followed by TBATS (1, {0,0}, 0.8, -) and ETS (1,0,0).

Table 1. Comparison of accuracy for SARIMA, exponential smoothing, and TBATS.

ACCURACY

SARIMA

MODELS 
Exponential 
Smoothing

TBATS

MSE 
RMSE 
MAE

Train 
5.0330 
2.2434 
1.2566

Test 
0.3101 
0.5569 
0.2677

Train 
6.9866 
2.6432 
1.4267

Test 
13.0627 
3.6142 
2.6146

Train 
6.1459 
2.4791 
1.2553

Test 
0.4742 
0.6887 
0.2484

3.4

Best machine Learning Regression Algorithm for predicting Household final 
consumption expenditure

Table  2  shows  the  obtained  regression  metrics  results  for  Extreme  Gradient 
Boosting (XGBoost), k-nearest neighbors (kNN), and Support Vector Regression (SVR). 
The  results  showed  that  the  SVR  algorithm  outperformed  the  other  two  models  in 
predicting  the  Philippines’  Quarterly  Household  Final  Consumption  Expenditure 
(HFCE). The table reflected the lowest MSE (6.413), RMSE (2.532), and MAE (1.115) 
on SVR. Moreover, the R-squared value of SVR (0.806) was the highest among the three 
algorithms,  implying  that  it  best  describes  how  well  the  regression  model  explains 
observed  data.  Thus,  80.6%  of  the  variability  observed  in  the  target  variable  was 
explained by the regression model. It was also found that the XGBoost algorithm had the 
lowest  performance  reflected  by  the  highest  MSE,  RMSE,  MAE,  and  R²  values. 
Moreover, it was also revealed that the XGBoost had almost equal performance  with 
kNN in predicting the HFCE Growth Rate. Thus, among the three models, SVR was the 
best regression algorithm for predicting the country’s quarterly HFCE Growth Rate.

Table 2. Comparison of accuracy of regression algorithm (XGBoost, KNN, and SVR).

ACCURACY

MSE 
RMSE 
MAE 
R2

XGBoost 
6.4130 
2.5320 
1.5710 
0.4810

REGRESSION ALGORITHM 
kNN 
5.4230 
2.3290 
1.3120 
0.5610

SVR 
2.3970 
1.5480 
1.1150 
0.8060

[85]

---

<!-- PAGE 17 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

4. CONCLUSIONS

In  this  study,  the  researchers  have  analyzed  the  impact  of  COVID-19  on  the 
Philippines’ quarterly Household Final Consumption Expenditure (HFCE).  Time-series 
analyses were used to forecast the quarterly HFCE of the country covering the period of 
2022 to 2026.  The visualization of the trajectory of the pandemic was shown using line 
graphs.

Moreover, the researchers created a model to forecast the HFCE growth rate from 
2022 to 2026 using SARIMA, Triple Exponential Smoothing, and the TBATS model. 
Using MSE, RMSE, and MAE, the researchers built a model selection table containing 
the best forecasting outcomes. The results showed that SARIMA (1,0,0) (0,0,1) [4] was 
the best model for predicting the HFCE growth rate for the next five years.  Wherein, it 
implied that the Household Final Consumption Expenditure growth rate will gradually 
decline during the span of forecasted years.

Furthermore,  regression  algorithms  in  machine  learning,  specifically  XGBoost, 
kNN, and SVR were compared in terms of error metrics (RMSE, MSE, and MAE) and 
the  goodness  of  fit  of  regression  models  (R²)  to  identify  which  among  them  has  the 
highest  performance  in  predicting  HFCE.  Thus,  the  results  revealed  that  with  the 
Inflation Rate, Unemployment Rate, Import of Goods and Services Growth Rate, Export 
of  Goods  and  Services  Growth  Rate  being  the  predictor variables  and  HFCE  Growth 
Rate  as  the  outcome  variable,  Support  Vector  Regression  was  the  best  regression 
algorithm to be used for prediction.

In conclusion, based on the data, a  drastic decline in the HFCE growth rate was 
observed  when  COVID-19  spread  throughout  the  country. Thus,  the  use  of  historical 
data, including the years when COVID-19 occurred, dramatically affected the model for 
forecasting the HFCE growth rate for the next five (5) years.

5. ACKNOWLEDGMENT

The  researchers  would  like  to  offer  their  sincerest  gratitude  to  their  professors  who 
helped them with their study:  Ms. Sandrilito Abogada for imparting her knowledge and 
skills in forecasting and machine learning, and to Assoc. Prof. Laurence P. Usona, for 
his guidance and assistance in completing this research.

Finishing the researchers’ study without the expertise, understanding, and patience of 
Mr. Peter John B. Aranas, their research adviser, is impossible. The researchers would 
like to thank their parents, as well, for their unconditional support and love.

It would take a lot of pages to enumerate the people whom the researchers are indebted 
to, like their friends who gave support, motivation, and unexpected willingness to help 
the team with their study. Lastly, this research was only done with the cooperation and 
dedication of the researchers themselves in conducting this study.

[86]

---

<!-- PAGE 18 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

6. REFERENCES

Arapova, E. (2018). Determinants of household final consumption expenditures in Asian 
countries:  A  panel  model,  1991–2015.  Applied  Econometrics  and  International 
Development, 18(1), 121-140.

Bajaj,  A.  (2022).  ARIMA  &  SARIMA:  Real-World  Time  Series  Forecasting. 
https://neptune.ai/blog/arima-sarima-real-world-time-series-

Neptune.Ai. 
forecasting-guide

Biswas,  R.  (2021).  Philippines  Economic  Rebound  Hit  by  New  COVID-19  Wave. 
Escalating  New  COVID-19  Cases  Dampens  Recovery.  https://ihsmarkit.com/ 
research-analysis/  Philippine,  https://  ihsmarkits-economic-rebound-hit-by-new- 
covid19-wave.html.com/research-analysis/  Philippines-economic-rebound-hit-by-
new - covid19 -wave.html

Blaconá, M.T, Andreozzi, L. and Magnano, L. (2014). Time series models for different 
seasonal 
https://forecasters.org/wp-content/ 
from 
uploads/gravity_forms/72a51b93047891f1ec3608bdbd77ca58d/2014/06/Blacon%
C3%A1_MT_ISF2014.pdf.pdf

Retrieved

patterns.

Brownlee,  J.  (2019,  August  21).  A  Gentle  Introduction  to  SARIMA  for  Time  Series 
Forecasting in Python.Machine Learning Mastery. https://machinelearningmastery. 
com/sarima-for-time-series-forecasting-in-python/

Brownlee,  J.  (2021,  March  6).  XGBoost  for  Regression.Machine  Learning  Mastery.

https://machinelearningmastery.com/xgboost-for-regression/

Chatterjee,  S.  (2018,  January  30).  Time  series  analysis  using  Arima  model  in  R. 
DataScience+.  Retrieved  July  25,  2022,  from  https://datascienceplus.com/time-
series-analysis-using-arima-model-in-r/

Dela Cruz, A. (2019). Forecasting Philippine household final consumption expenditure 
on  education  using  discrete  wavelet  transformation  on  hybrid  ARIMA-ANN 
model. Indian Journal of Science and Technology, 12(33). 
https://doi.org/10.17485/ijst/2019/v12i33/146427

Erero, J. &Makananisa M. (2020). Impact of Covid-19 on the South African economy: 
A CGE, Holt-Winter and SARIMA model’s analysis. Turkish Economic Review, 
7(4). 
from 
Retrieved 
http://www.kspjournals.org/index.php/TER/article/view/2129

Frost,  J.  (2021,  May  18).  Exponential  Smoothing  for  Time  Series  Forecasting. 
Statistics  By  Jim.  https://statisticsbyjim.com/time-series/exponential-smoothing-
time-series-forecasting/

Fürnkranz, J., Chan, P. K., Craw, S., Sammut, C., Uther, W., Ratnaparkhi, A., Jin, X., 
Han,  J.,  Yang,  Y.,  Morik,  K.,  Dorigo,  M.,  Birattari,  M.,  Stützle,  T.,  Brazdil,  P., 
Vilalta, R., Giraud-Carrier, C., Soares, C., Rissanen, J., Baxter, R. A., . . . De Raedt, 
L.  (2011).  Mean  Squared  Error.  Encyclopedia  of  Machine  Learning,  653. 
https://doi.org/10.1007/978-0-387-30164-8_528

Fürnkranz, J., Chan, P. K., Craw, S., Sammut, C., Uther, W., Ratnaparkhi, A., Jin, X., 
Han,  J.,  Yang,  Y.,  Morik,  K.,  Dorigo,  M.,  Birattari,  M.,  Stützle,  T.,  Brazdil,  P.,

[87]

---

<!-- PAGE 19 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

Vilalta, R., Giraud-Carrier, C., Soares, C., Rissanen, J., Baxter, R. A., . . . De Raedt, 
L. (2011a).  Mean  Absolute  Error.  Encyclopedia  of  Machine  Learning,  652.
https://doi.org/10.1007/978-0-387-30164-8_525

Gubangco, A. G. D., Joves, J. D. S., & Pizarro-Uy, A. C. D. (2022). Consumption in the 
Philippines:  In  the  course  of  unemployment  and  loan  acquisition.  Journal  of 
Economics, Finance and Accounting Studies, 4(2), 18-34.

Han,  R.  (2022,  May).  What  is  TBATS  model  in  time  series  in  R  How  to  use  it  -
https://www.projectpro.io/recipes/what-is-tbats-model-time-series-

.ProjectPro. 
use-it

Handriyani, R., Sahyar, M. M., & Si, A. M. (2018). Analysis the effect of household 
consumption  expenditure,  investment  and  labor  to  economic  growth:  A  case  in 
province 
Arad, 
Sumatra. 
of  North 
SeriaȘtiințeEconomice, 28(4), 45-54.

StudiaUniversitatisVasileGoldiș

Hyndman,  R.  J.  (2018).  In  G.  Athanasopoulos  (Ed.),  Forecasting:  Principles  and

Practice (2nd ed). Otexts. https://otexts.com/fpp2/holt-winters.html

Karabiber OA, Xydis G. (2019). Electricity price forecasting in the Danish Day-ahead 
market using the TBATS, ANN and ARIMA methods. Energies.12(5). Retrieved 
from https://doi.org/10.3390/en12050928

Kumar,  A.  (2022,  February  21).  R-squared,  R²  in  Linear  Regression:  Concepts, 
Examples.  Data  Analytics.  https://vitalflux.com/r-squared-explained-machine-
learning/

Long,  G.  (2010).  GDP  prediction  by  support  vector  machine  trained  with  genetic 
algorithm.  2010  2nd  International  Conference  on  Signal  Processing  Systems. 
https://doi.org/10.1109/icsps.2010.5555854

Madhav, N., Oppenheim, B., Gallivan,M., Mulembakani, P., Rubin, E., and Wolfe, N. 
(2017).  Pandemics:  Risks,  Impacts,  and  Mitigation.  lnJamison  DT,  Gelband  H, 
Horton S, et al., (Eds). Disease Control Priorities: Improving Health and Reducing 
Poverty (3rd ed). Washington DC.

McCloskey,  B.(2022).  Forecasting  My  Future  Grocery  Bills.  Towards  Data  Science. 
from  https://towardsdatascience.com/forecasting-my-future-grocery-

Retrieved 
bills-59515b9348d3

Obinna, O. (2020). Effect of inflation on household final consumption expenditure in

Nigeria. Journal of Economics and Development Studies, 8(1), 104-111.

Pascasio, M. C., Dimafelix, A. D., Dimafelix, J. A. F., Chavez, L. T., &Robredo, J. E. P. 
(n.d.). Demystifying the Household Final Consumption Expenditure (HFCE) in the 
Philippine System of National Accounts (PSNA). Philippine Statistics Authority. 
https://psa.gov.ph/sites/default/files/1.1.1%20Demystifying%20the%20Househol
d%20Final%20Consumption%20Expenditure%20%28HFCE%29%20in%20the%
20Philippine%20System%20of%20National%20Accounts%20%28PSNA%29_0.
pdf

Pedamkar,  P.  (2021,  November  15).  Support  Vector  Regression.  EDUCBA.

https://www.educba.com/support-vector-regression/

[88]

---

<!-- PAGE 20 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

Philippine Statistics Authority .(2017). Inflation Rate.In Official Concept and Definition.

https://psa.gov.ph/ISSiP/concepts-and-definitions/161406

Priambodo, B., Rahayu, S., Hazidar, A. H., Naf’an, E., Masril, M., Handriani, I., Pratama 
Putra, Z., KudrNseaf, A., Setiawan, D., &Jumaryadi, Y. (2019). Predicting GDP of 
Indonesia using K-Nearest Neighbour Regression. Journal of Physics:Conference 
Series, 1339(1), 012040. https://doi.org/10.1088/1742-6596/1339/1/012040

Qureshi,  S.  ,Chu  B.  &  Demers,  F.  (2020).  Forecasting  Canadian  GDP  growth  using 
XGBoost.Carleton Economic Papers 20(14), Carleton University, Department of 
Economics. Retrieved from https://ideas.repec.org/p/car/carecp/20-14.html

Rohmah, M. F., Putra, I. K. G. D., Hartati, R. S., &Ardiantoro, L. (2021). Comparison 
four  kernels  of  SVR  to  predict  consumer  price  index.  Journal  of  Physics: 
Conference 
https://doi.org/10.1088/1742-
6596/1737/1/012018

1737(1),

012018.

Series,

SAP.(2018).  SAP  HANA  Predictive  Analysis  Library  (PAL).  Triple  Exponential 
Smoothing,400.  https://help.sap.com/doc/86fb8d26952748debc8d08db756e6c1f/ 
1.0.12/en-US/ SAP_HANA_Predictive_Analysis_Library_PAL_en.pdf

Sayad,  S.  (n.d.).KNN  Regression.Saedsayad.  https://www.saedsayad.com/  k_nearest_

neighbors_reg.htm

Statista, Inc. (2022, January). Household final consumption expenditure on health in the 
to  2021.  https://www.statista.com/statistics/709061/

Philippines  from  2017 
philippines-household-co.statista.com/statistics/709061/nsumption-expenditure-
health/ Philippines-household-consumption-expenditure-health/

Sugiarto,  S.,  &Wibowo,  W.  (2020).  Determinants  of  regional  household  final

consumption expenditure in Indonesia.JEJAK, 13(2), 332-344.

Team,  E.  A.  (2022,  July  16).  Calculating  Mean  Squared  Error  in  Python.  Educative: 
for  Software  Developers.  https://www.educative.io/

Interactive  Courses 
answers/calculating-mean-squared-error-in-python

Teixeira-Pinto,  A.  (2021,  August  2).  2  K-nearest  Neighbours  Regression  |  Machine 
Learning  for  Biostatistics.The  University  of  Sydney.  https://bookdown.org/ 
tpinto_home/Regression-and-Classification/k-nearest-neighbours- regression.html

TenthPlanet.  (2020,  November  23).  Time-Series  Forecasting  using  TBATS  model  – 
https://blog.tenthplanet.in/time-series-

Technologies.  Blogs.

TenthPlanet 
forecasting-tbats/

The  World  Bank  Group.(2020).  Impacts  of  COVID-19  on  Households  in  the 
the  Philippines  COVID-19  Households  Survey.

Philippines.Results  from 
https://thedocs.worldbank.org/en/doc/ab24c2a718fb53a344c5942d236b2fe6-
0070062021/original/Philippines-COVID-19-High-Frequency-Survey-
Household-Results-Slides.pdf

The World Bank Group.(2020b, November).Monitoring COVID-19 Impacts on Families

and Firms in the Philippines.https://www.worldbank.org/en/country/philippines/ 
brief/monitoring-covid-19-impacts-on-firms-and-families-in-the-philippines

[89]

---

<!-- PAGE 21 -->

Dasmariñas, De Castro, Lazona & Usona

PUP J. Sci. Tech.

Varlamova, J., &Larionova, N. (2015).Macroeconomic and demographic determinants 
of household expenditures in OECD countries.Procedia Economics and Finance, 
24, 727-733.

Yadav,  A.  (2018,  October  22).  SUPPORT  VECTOR  MACHINES(SVM)  –  Towards 
Data Science. Medium. https://towardsdatascience.com/support-vector-machines-
svm-c9ef22815589

World Health Organization. (2020, January 10). Coronavirus.

https://www.who.int/health-topics/coronavirus#tab=tab_1

[90]

<!-- MARKITDOWN CONVERSION -->

<!-- The following is the full MarkItDown conversion for formatting fidelity. -->

.
FORECASTING THE IMPACT OF COVID-19 ON THE HOUSEHOLD FINAL
CONSUMPTION EXPENDITURE (HFCE) IN THE PHILIPPINES
ANDRE PERRY P. DASMARIÑAS1, GWENETH H. DE CASTRO2, BEA JANE M.
LAZONA3, AND LAURENCE P. USONA2
1Accenture Inc., Bonifacio Global City, Uptown Tower 3, Taguig City 1637, Philippines
2Polytechnic University of the Philippines, Sta. Mesa, Manila 1016, Philippines
3AMI Risk Consultants Inc., Wilson St., Brgy. Maytunas, San Juan City 1500, Philippines
Abstract: The Household Final Consumption Expenditure (HFCE) is a significant component of the Philippine
economy. The term "HFCE" refers to families' spending on necessities such as food and drink, clothing, shelter,
and health care. The gathered data from this study covers the country’s quarterly HFCE from 2001-2021. The
study used various forecasting methods, including Triple Exponential Smoothing, Seasonal Autoregressive
Integrated Moving Average (SARIMA), and TBATS in modeling time series data to depict the effects of
COVID-19 on the country’s HFCE Growth Rate. The best model to predict the quarterly HFCE growth rate
from 2022 to 2026 was identified using error metrics, particularly RMSE, MSE, and MAE. The SARIMA
model had the lowest combined error of the train and test set, marking it as the best model for predicting the
HFCE growth rate. Moreover, the HFCE growth rate was also predicted using various machine learning
regression algorithms (SVR, XGBoost, and kNN), with a variety of economic indicators as the independent
variables, including the inflation rate, unemployment rate, import of goods growth rate, import of services
growth rate, export of goods growth rate, and export of services growth rates. The results of error metrics
showed that SVR was the best regression algorithm for predicting the Philippines’ quarterly HFCE Growth
Rate. The findings of this study indicate that as COVID-19 spread over the country, the HFCE growth rate
dramatically decreased. Therefore, models used to predict the HFCE growth rate over the next five years are
significantly impacted using historical data, including the years when COVID-19 occurred.
Keywords: COVID-19, Extreme Gradient Boosting (XGBoost), Household Final Consumption Expenditure
(HFCE), kNN Regression, Support Vector Regression (SVR), TBATS, Triple Exponential Smoothing.
1.INTRODUCTION
The COVID-19 pandemic has sparked a global health crisis, requiring several
governments to implement stringent preventive measures to stem the virus' spread,
including national lockdowns and social distancing measures. The first case of COVID-
19 infection in the Philippines was reported in January 2020, and by March, the country
was placed under a strict community quarantine that restricted mobility and business
activities. While these measures have slowed the community spread of COVID-19, they
have significant adverse impacts on family incomes, jobs, education of children, food
security, and businesses. A pandemic can disrupt the economy in a variety of ways.
Human behavioral changes, such as fear-induced aversion to places of work and public
gatherings, were a significant cause of economic damage, besides the impact of
mitigation measures (Madhav et al., 2017). The adverse effects of various pandemics on
inhabitants' household income have been established in the past literature. The 2020
economic contraction was the highest annual decline ever reported since the National
Accounts data series for the Philippines began in 1946. The final consumption of
households was mostly the biggest component of the Gross Domestic Product (GDP)
among the Association of Southeast Asian Nations (ASEAN) countries on the

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
expenditure side. In the Philippines, Household Final Consumption Expenditure (HFCE)
was 73.5 % of the GDP, making it an essential component in demand analysis.
As stated in IHS Markit Philippines Manufacturing PMI (Biswas, 2021), the
Household Final Consumption Expenditure (HFCE) went down by 7.9%, while gross
capital formation contracted by 34.4%. Drastic declines in output were reported in some
sectors of the economy, with the transport and storage industry marking a 30.9% decline,
while accommodation and food services output went down by 45.4%. Meanwhile,
according to the Philippine Statistics Authority (PSA), during the third quarter of 2020,
the unemployment rate increased to 18.9%. Further, World Bank's research said that only
1 in 10 households that operated a business accessed financial services. The incidence of
revenue losses among household businesses showed improvement, with the wealthiest
households recovering faster than the poorest households. Nearly two out of five
households were anxious about not having enough food for the following week. While
food security continued to improve overall, concerns among households remained. The
share of household heads unable to buy at least one of the food staples remained the same
at around 40%, primarily because of food unaffordability. Fewer households reported
eating less than usual and worried about not having enough food. Households that needed
medical treatment increased to 28% in December from 20% in August 2021. More
households cited lack of money as a reason for inadequate access to treatment. However,
based on the report of the Statista Research Department, in 2021, the HFCE for health in
the Philippines was valued at approximately 627 billion Philippine pesos. Household
spending on health has gradually increased over the past five years and was highest in
2021 after the COVID-19 pandemic outbreak. Undeniably, COVID-19 played a massive
part in the shift of the economy and household expenditure, and the researchers, being
the children of the working class who were greatly affected by the pandemic, saw the
need for this study to be conducted.
This study aimed to depict the impact of COVID-19 on the Household Final
Consumption Expenditure (HFCE) Growth Rate in the Philippines, wherein different
forecasting methods were used to model time series data, particularly Seasonal
Autoregressive Integrated Moving Average (SARIMA); Triple Exponential Smoothing;
and Trigonometric seasonability, Box-Cox transformation, ARMA errors, Trend
components and Seasonal components (TBATS). Further, the best model was identified
to forecast the country’s HFCE Growth Rate. Moreover, different machine learning
regression algorithms such as support vector machine (SVM) regression, extreme
gradient boosting (XGBoost), and k-nearest neighbors (kNN) were used to predict the
HFCE growth rate, applying various economic indicators as the independent variables,
namely: Inflation Rate, Unemployment Rate, Import of Goods Growth Rate, Import of
Services Growth Rate, Export of Goods Growth Rate, and Export of Services Growth
Rate. Thus, the model with the lowest error metrics – root mean square error (RMSE),
mean squared error (MSE), mean absolute error (MAE), and highest R squared were
selected as the best machine learning regression algorithms for predicting the HFCE
growth rate.
The primary purpose of this study is to forecast the impact of the COVID-19
pandemic on the Philippines’ HFCE growth rate from 2022-2026 through time series
forecasting models and to identify which model is the best. Moreover, this paper also
aims to determine the best machine-learning regression algorithm for predicting the
country’s HFCE growth rate.
[71]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
2.METHODOLOGY
2.1 Research Design
This research was conducted using different time series forecasting models, namely
SARIMA, Triple Exponential Smoothing, and TBATS in forecasting the quarterly
HFCE Growth Rate of the Philippines. In addition, regression algorithm in machine
learning was also used in the study and further identified which among them is the best
for predicting the country’s quarterly HFCE Growth Rate. To supplement the statistical
analysis performed in this study, the researchers relied on several sets of secondary data
relating to the HFCE Growth Rate, Inflation Rate, Unemployment Rate, Import of Goods
Growth Rate, Import of Services Growth Rate, Export of Goods Growth Rate and Export
of Services Growth Rate. All the data came from the Time Series Data of the Philippine
Statistics Authority (PSA). PSA serves as the central statistical authority of the
Philippine government on primary data collection.
2.1 Statistical Data Analysis Procedures
2.1.1 Statistical Tool
The researchers used the software RStudio and Orange to clean, organize, analyze,
predict, and present the data. RStudio software was used to forecast future HFCE Growth
Rate values by operating SARIMA, Triple Exponential Smoothing, and TBATS. In
addition, this software was used to identify the models’ accuracy. RStudio was a free
software environment commonly used by statisticians to convey statistical computation
and graphics. Furthermore, Orange was used in determining which among the machine
learning regression algorithms had the lowest values of error metrics, particularly
Extreme Gradient Boosting (XGBoost), k-nearest neighbors (kNN) Regression, and
Support Vector Machine (SVM) Regression in predicting HFCE, considering the
dependent variables. Orange was an open-source data visualization, machine learning,
and data mining toolkit. It featured a visual programming front-end for explorative rapid
qualitative data analysis and interactive data visualization.
2.1.2 Statistical Treatment of Data
2.1.2.1 Seasonal Autoregressive Integrated Moving Average (SARIMA)
SARIMA stands for Seasonal-ARIMA, and it includes seasonality contribution to
the forecast. The importance of seasonality is quite evident, and Auto Regression
Integrated Moving Average (ARIMA) fails to encapsulate that information implicitly.
The Autoregressive (AR), Integrated (I), and Moving Average (MA) parts of the model
remain as that of ARIMA. The addition of Seasonality adds robustness to the SARIMA
model. It is represented as:
[72]

Dasmariñas, De Castro, Lazona & Usona                    PUP J. Sci. Tech.

| ARIMA      (p, d, q)  |     |     | (P, D, Q)         |
| --------------------- | --- | --- | ----------------- |
|                       |     |     |                   |
|                       |     |     |                   |
| Non-seasonal part of  |     |     | Seasonal part of  |
| the model             |     |     | the model         |

where 𝑚 is the number of observations per year. We used the uppercase notation
for the seasonal parts of the model, and lowercase notation for the non-seasonal parts of
the model. Like ARIMA, the P, D, and Q values for seasonal parts of the model can be
deduced from the ACF and PACF plots of the data. The researchers used this model to
predict the next five years’ quarterly data on HFCE Growth Rate, from 2022 to 2026.

Assumptions:
i.  Data should be univariate

The data type that should be used consists of observations with a single characteristic
or attribute.

ii.  Data should be stationary

The properties of a series should not depend on the time when it is captured. In
addition, it must have a constant variance, covariance, and mean.

2.1.2.2  Triple Exponential Smoothing (Holt-Winters method)
Triple exponential smoothing can model seasonality, trend, and level components
for univariate time series data. Seasonal cycles are patterns in the data that occur over a
standard number of observations. Triple exponential smoothing is also known as Holt-
Winters Exponential Smoothing. This method adds in the gamma (γ) parameter to account
for the seasonal component. For this method, you must specify the period for the seasonal
cycle. This study has used the additive method. The component form for the additive
method is:
| 𝑦̂       | =ℓ𝑡+ℎ𝑏 | +𝑠           |         |
| -------- | ------ | ------------ | ------- |
| 𝑡+ℎ\𝑡    |        | 𝑡 𝑡+ℎ−𝑚(𝑘+1) |         |
| ℓ𝑡 =𝛼(𝑦  | −𝑠     | )+(1−𝛼)(ℓ    | +𝑏 )    |
| 𝑡        | 𝑡−𝑚    |              | 𝑡−1 𝑡−1 |
| 𝑏𝑡 =𝛽∗(ℓ | −ℓ     | )+(1−𝛽∗)𝑏    |         |
|          | 𝑡      | 𝑡−1          | 𝑡−1     |
| =γ(𝑦     |        | )+(1−γ)𝑠     |         |
| 𝑠𝑡 𝑡     | −ℓ 𝑡−1 | −𝑏 𝑡−1       | 𝑡−𝑚,    |
where 𝑘 is the integer part of (ℎ−1)/𝑚, which ensures that the estimates of the seasonal
indices used for forecasting come from the final year of the sample. The level equation
showed a weighted average between the seasonally adjusted observation 𝑦 −𝑠 and
𝑡 𝑡−𝑚
the non-seasonal forecast (ℓ +𝑏 ) for time 𝑡. The trend equation was identical to
| 𝑡−1 | 𝑡−1 |     |     |
| --- | --- | --- | --- |
Holt’s linear method. The seasonal equation showed a weighted average between the
current seasonal index, (𝑦 −ℓ −𝑏 ), and the seasonal index of the same season
| 𝑡 𝑡−1 | 𝑡−1 |     |     |
| ----- | --- | --- | --- |
last year (i.e., mm time periods ago).

The equation for the seasonal component is often expressed as:
| 𝑠 =𝛾∗(𝑦 | −ℓ  | )+(1−𝛾∗)𝑠 | .   |
| ------- | --- | --------- | --- |
| 𝑡       | 𝑡   | 𝑡         | 𝑡−𝑚 |
[73]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
If we substitute ℓt from the smoothing equation for the level of the component form
above, we get
𝑠 =𝛾∗(1 −𝛼)(𝑦 −ℓ −𝑏 )+[1−γ∗(1−α)]𝑠 ,
𝑡 𝑡 𝑡−1 𝑡−1 𝑡−𝑚
which is identical to the smoothing equation for the seasonal component we specify here,
with 𝛾 =𝛾∗(1−𝛼).The usual parameter restriction is 0≤𝛾∗ ≤1,which translates
to 0 ≤𝛾 ≤ 1−𝛼.
2.1.2.3 TBATS
The names were acronyms for key features of the models: Trigonometric
seasonality, Box-Cox transformation, Auto Regression Integrated Moving Average
(ARMA) errors, and Trend and Seasonal components. TBATS model took its roots in
exponential smoothing methods and can be described by the following equations:
𝑇
𝑦λ =𝑙 +ф𝑏 +∑𝑠(𝑖) +𝑑
𝑡 𝑡−1 𝑡−1 𝑡−𝑚𝑖 𝑡
𝑖=1
𝑙 =𝑙 +ф𝑏 +𝛼𝑑
𝑡 𝑡−1 𝑡−1 𝑡
𝑏 =ф𝑏 +𝛽𝑑
𝑡 𝑡−1 𝑡
𝑝 𝑞
𝑑 =∑φ 𝑑 +∑𝛳𝑒 +𝑒
𝑡 𝑖 𝑡−𝑖 𝑖 𝑡−𝑖 𝑡
𝑖=1 𝑖=1
where:
𝑦λ- time series at moment 𝑡 (Box-Cox transformed)
𝑡
𝑠(𝑖)- ith seasonal component
𝑡
𝑙 - local level
𝑡
𝑏 - trend with damping
𝑡
𝑑 - ARMA(p,q) process for residuals
𝑡
𝑒 - Gaussian white noise
𝑡
Seasonal Part:
𝑘𝑖
𝑠(𝑖) = ∑𝑠(𝑖)
𝑡 𝑗,𝑡
𝑗=1
𝑠(𝑖) =𝑠(𝑖) 𝑐𝑜𝑠(ω)+𝑠∗(𝑖) 𝑠𝑖𝑛(ω)+ɣ(𝑖)𝑑
𝑗,𝑡 𝑗,𝑡−1 i 𝑗,𝑡−1 i 1 𝑡
𝑠(𝑖) =−𝑠(𝑖) 𝑠𝑖𝑛(ω)+𝑠∗(𝑖) 𝑐𝑜𝑠(ω)+ɣ(𝑖)𝑑
𝑗,𝑡 𝑗,𝑡−1 i 𝑗,𝑡−1 i 2 𝑡
ω =2𝜋𝑗/𝑚
𝑖 𝑖
Model Parameters:
𝑇 - Amount of seasonalities
𝑚 - Length of the 𝑖th seasonal period
𝑖
𝑘 - Amount of harmonics for the 𝑖th seasonal period
𝑖
λ – Box-Cox transformation
𝛼,𝛽 – Smoothing
ф - Trend damping
𝜑 ,𝛳 – ARMA(p,q) coefficients
𝑖 𝑖
ɣ(𝑖),ɣ(𝑖) – Seasonal smoothing (two for each period)
1 2
[74]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
Each seasonality was modeled by a trigonometric representation based on the
Fourier series. One major advantage of this approach was that it required only (two) 2
seed states regardless of the length of the period. Another advantage was the ability to
model seasonal effects of non-integer lengths. For example, given a series of daily
observations, one can model leap years with a season of length 365.25. BATS, which
stands for Box-Cox transformation ARMA residuals Trend component in the model
Seasonal components, differed from TBATS only in the way it models seasonal effects.
In BATS, we had a more traditional approach where each seasonality was modeled by:
𝑠(𝑖) =𝑠(𝑖) +ɣ𝑑 .
𝑡 𝑡−𝑚𝑖 i 𝑡
This implied that BATS can only model integer period lengths. The approach
taken in BATS requires m seed states for season 𝑖, if this season is long the model may
i
become intractable.
2.1.2.4 Extreme Gradient Boosting (XGBoost)
XGBoost was a short-term for the eXtreme Gradient Boosting algorithm developed
by Chen and Guestrin (2016). It was an implementation of gradient-boosted decision trees
designed for speed and performance and was a more efficient version of gradient-boosting
decision trees. The main objective of the algorithm was to optimize parameters given an
objective function that contains a loss function and a regularization parameter. The
regularization term aimed to reduce the likelihood of overfitting by controlling the
complexity of constructed trees. The complexity of each tree follows the equation:
𝑇
1
Ω(𝑓)=𝛾𝑇+ 𝜆∑𝜔2
2 𝑗
𝑗=1
where T is the number of leaves and ω is the vector scores on leaves (Chen and Guestrin,
2016). The structure score, objective function, of the algorithm is defined as:
𝑇
1
𝐹 =∑(𝐺𝜔 + (𝐻 +λ)𝜔2) +γ𝑇
𝑗 𝑗 2 𝑗 𝑗
𝑗=1
where𝜔 are independent of each other and the form 𝐺𝜔 + 1 (𝐻 +λ)𝜔2 is quadratic.
𝑗 𝑗 𝑗 2 𝑗 𝑗
2.1.2.5 K-nearest neighbors (kNN) regression
A simple implementation of kNN regression was to calculate the average of the
numerical target of the K nearest neighbors. Another approach used an inverse distance
weighted average of the K nearest neighbors. kNN regression used the same distance
functions as kNN classification.
[75]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
Distance Functions
Euclidean: √∑𝑘 (𝑥 −𝑦)2
𝑖=1 𝑖 𝑖
Manhattan ∑𝑘 |𝑥 −𝑦|
𝑖=1 𝑖 𝑖
1
Minkowski(∑𝑘 (|𝑥 −𝑦|𝑞)𝑞
𝑖=1 𝑖 𝑖
The above three distance measures were only valid for continuous variables. Thus, this
study used the Euclidean Distance Function.
2.1.2.6 Support Vector Regression (SVR)
This was a regression algorithm that supported both linear and non-linear
regressions. This method worked on the principle of the Support Vector Machine. SVR
was a regression that was used for predicting continuous ordered variables. In simple
regression, the idea was to minimize the error rate while in SVR the idea was to fit the
error inside a certain threshold, which means that SVR’s work was to approximate the
best value within a given margin called ε- tube. Moreover, this study utilized polynomial
kernels. In general, the polynomial kernel was defined as:
𝐾(𝑋 ,𝑋 )=(𝑎+𝑋𝑇𝑋 )𝑏
1 2 1 2
2.1.2.7 Mean Squared Error (MSE)
The mean squared error of a model concerning a test set was the mean of the squared
prediction errors over all instances in the test set. The prediction error was the difference
between the true value and the predicted value for an instance.
∑𝑛 (𝑦 −𝑦)2
𝑀𝑆𝐸 = 𝑖=1 𝑖 𝑖
𝑛
where:
𝑛 - the total number of terms for which the error is to be calculated
𝑦 - the observed value of the variable
𝑖
𝑦 - the predicted value of the variable
𝑖
2.1.2.8 Root Mean Square Error (RMSE)
Root Mean Squared Error Root mean squared error (RMSE) was the square root of
the mean of the square of all the errors. The use of RMSE was widespread, and it was
regarded as an ideal general-purpose error metric for numerical forecasts.
𝑛
1
𝑅𝑀𝑆𝐸 =√ ∑(𝑆 −𝑂)2
𝑛 𝑖 𝑖
𝑖=1
[76]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
where:
𝑂are the observations,
𝑖
𝑆are the predicted values of a variable, and
𝑖
𝑛is the number of observations available for analysis.
RMSE was a good measure of accuracy, but only to compare prediction errors of
different models or model configurations for a particular variable and not between
variables, as it is scale-dependent. Meanwhile, the smaller the value, the better the
model’s performance.
2.1.2.9 Mean Absolute Error (MAE)
Mean Absolute Error was a model evaluation metric used with regression models.
The mean absolute error of a model to a test set was the mean of the absolute values of
the individual prediction errors on overall instances in the test set. Each prediction error
was the difference between the true value and the predicted value for the instance.
∑𝑛 |(𝑥 −𝑥)|
𝑀𝐴𝐸 = 𝑖=1 𝑖
𝑛
where:
𝑛 = the number of errors
Σ = summation symbol (which means “add them all up”)
|(𝑥 −𝑥)| = the absolute errors
𝑖
2.1.2.10 Coefficient of determination (R²)
This referred to the proportion of variation of data points explained by the regression
line or model. It can be determined as a ratio of the total variation of data points explained
by the regression line (Sum of squared regression) and the total variation of data points
from the mean (also termed as sum of squares total or total sum of squares). The following
formula represents the ratio.
𝑆𝑆𝑅 ∑(𝑦̂ −𝑦̅)2
𝑅2 = = 𝑖
𝑆𝑆𝑇 ∑(𝑦 −𝑦̅)2
𝑖
where:
𝑦̂ represents the prediction or a point on the regression line,
𝑖
𝑦̅represents the mean of all the values, and
𝑦represents the actual values or the points.
𝑖
2.1.2.11 Auto-Correlation Function (ACF)
Auto-correlation function (ACF) was a statistical technique used to identify how
correlated the values in a time series are with each other by plotting the correlation
coefficient against lag. The data values beyond the significance limits were statistically
significant at approximately α = 0.05, which shows evidence of correlation. ACF was
formulated as follows:
∑𝑛−𝑘 (𝑥 −𝑥)(𝑥 −𝑥)
𝑡=𝑘+1 𝑡−𝑘 𝑡
𝑟̂ =
𝑘 ∑𝑛 (𝑥 −𝑥) 2
𝑡=1 𝑡
[77]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
where:
𝑘 = Lag; 𝑘 =1,2,…,𝑛
𝑥 = Value of 𝑥 at row 𝑡
𝑡
𝑥= Mean of 𝑥
𝑛= Number of observations in the series
2.1.2.12 Augmented Dickey-Fuller Test (ADF)
Augmented Dickey-Fuller Test (ADF) was a statistical test for analyzing the
stationary of a series. The ADF test expanded the Dickey-Fuller test equation to include
a high-order regressive process in the model. The null hypothesis assumed the presence
of a unit root, that was α=1; the p-value obtained should be less than the significance
level to reject the null hypothesis; thereby, inferring that the series was stationary. ADF
was formulated as follows:
𝑦 =𝑐+𝛽𝑡+𝛼𝑦 +ф △𝑌 +ф △𝑌 ..+ф △𝑌 +𝑒
𝑡 𝑡−1 1 𝑡−1 2 𝑡−2 𝑝 𝑡−𝑝 𝑡
where:
𝑡 = Time index,
𝛼 = Intercept constant called a drift,
𝛽 = Coefficient on a time trend,
𝛾 = Coefficient presenting process root, i.e. the focus of testing,
𝑝 = Lag order of the first-differences autoregressive process,
𝑒 = Independent identically distributed residual term.
𝑡
3. RESULTS AND DISCUSSION
This section presented the purpose of the study, research design, data source for
secondary data, and statistical data analysis procedures.
3.1 Graphs of the Behavior of Specific Variables
3.1.1 Household Final Consumption Expenditure
Figure 3 shows that the graph exhibited a major downward trend from the 2nd
quarter of 2020 to the 1st quarter of 2021, recording all quarters within this duration with
a negative growth rate. The lowest HFCE growth rate recorded for 2000-2021 was during
the 2nd quarter of 2020 with -15.32%. One of the reasons for this decline was due to the
government's preventive measures, primarily when lockdowns were implemented; thus,
limiting the exposure of people outside their homes. On the other hand, in the 2nd quarter
of 2021 began to display a growth rate of 7.31%.
[78]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
Figure 3. Philippines’ household final consumption expenditure from Q1 2000 to Q4
2001.
3.1.2 Inflation rate
Based on Figure 4, the inflation rate in the country from the 2nd quarter of 2007 was
at 2.4% and continuously increased until the 3rd quarter of 2008, reaching its peak at
12.20%. The lowest point of the quarterly data of inflation rate for 2000-2021 was in the
third quarter of 2009 with 0.3%. On the other hand, the inflation rate during the COVID-
19 pandemic caused no significant changes.
Figure 4. Philippines’ inflation rate from Q1 2000 to Q4 2001.
[79]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
Figure 5. Philippines’ unemployment rate from Q1 2000 to Q4 2001.
3.1.3 Unemployment Rate
Figure 5 shows the unemployment rate in the Philippines from the 1st quarter of
2000 to the 4th quarter of 2021. It can be inferred that in the 4th quarter of 2005, there was
a sudden decline in the unemployment rate. It continued to decline until it rose to 8.7%
in the first quarter of 2018. It immediately declined again for the next quarters up to the
extent that its lowest record was at 4.5% during the 4th quarter of 2019, which is a good
indication in terms of unemployment. However, due to the COVID-19 pandemic, the
unemployment growth rate in the country began to increase rapidly starting from the 2nd
quarter of 2020 with 10% and 18.9% during the 3rd quarter of 2020.
3.1.4 Import of Goods
Figure 6 shows the growth rate of import of goods in the Philippines from the 1st
quarter of 2000 to the 4th quarter of 2021. The import of goods growth rate experienced
a major decline that started in the 3rd quarter of 2001, from 20.67% to -0.22%. It
continued to decline until it rose to 18.48% in the 4th quarter of 2002. Unfortunately, it
immediately declined again for the following quarters, until it showed another major
decline in the 1st quarter of 2009, which had a -10.69% rate. In the 1st quarter of 2010, it
showed a major increase with a 28.36% rate, and though it experienced a downward
trend, it stayed stable for the following quarters. In the 2nd quarter of 2020, the lowest
import of goods was recorded at -38.48% and continued to decline until the last quarter
of the year. This decline was a visible result of the COVID-19 pandemic. Fortunately, it
was slowly showing a major upward trend starting from the 2nd quarter of 2021, with
48.45%.
[80]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
Figure 6. Philippines’ import of goods growth rate from Q1 2000 to Q4 2001.
3.1.5 Import of Services
Figure 7 shows the growth rate of import of services in the Philippines from the 1st
quarter of 2000 to the 4th quarter of 2021. The import of services growth rate experienced
a major decline that started in the 4th quarter of 2001, from 31.16% to -8.33%. As the
import of services gradually increased through the years, reaching its peak at 39.86%
during the 3rd quarter of 2008, it immediately went down in the following years and the
lowest ever recorded was from the 4th quarter of 2020 with a value of -43.73%.
Fortunately, it was slowly showing a major upward trend starting from the 2nd quarter of
2021 at 1.03%.
Figure 7. Philippines’ import of services growth rate from Q1 2000 to Q4 2001.
[81]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
3.1.6 Export of Goods
Figure 8. Philippines’ export of goods growth rate from Q1 2000 to Q4 2001.
Figure 8 shows the growth rate of export of goods in the Philippines from the 1st
quarter of 2000 to the 4th quarter of 2021. The export of goods’ growth rate experienced
a major decline that started in the 2nd quarter of 2001, from 9.32% to -10.56%. It
continued to decline until it rose to 28.88% in the 1st quarter of 2010. Unfortunately, it
immediately declined again for the following quarters until it showed another major
decline in the 1st quarter of 2013 which had a -12.72% rate. In the 1st quarter of 2014, it
showed a major increase with a 14.13% rate, and though it experienced a downward
trend, it stayed stable for the following quarters. In the 2nd quarter of 2020, the lowest
export of goods was recorded at -30.57% and continued to decline until the last quarter
of the year. This decline was a visible result of the COVID-19 pandemic. Fortunately, it
was slowly showing a major upward trend starting from the 2nd quarter of 2021, with
35.94%.
3.1.7 Export of Services
Figure 9 shows the growth rate of export of services in the Philippines from the 1st
quarter of 2000 to the 4th quarter of 2021. The export of services growth rate experienced
a major decline that started in the 4th quarter of 2003, from 28% to 0.47%. As the import
of services gradually increased through the years reaching its peak at 57.09% during the
3rd quarter of 2005, it immediately went down in the following years and the lowest ever
recorded was from the 2nd quarter of 2020 with a value of -36.01%. Fortunately, it was
slowly showing a major upward trend starting from the 2nd quarter of 2021 at 20.17%.
[82]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
Figure 9. Philippines’ export of services growth rate from Q1 2000 to Q4 2001.
3.2 Five-year Predicted Values of the Household Final Consumption Expenditure
3.2.1 SARIMA Model
Figure 10 presents the plot of the Household Final Consumption Expenditure
Growth Rate prediction for 2022 to 2026 using the SARIMA model. It exhibited the best
model with SARIMA (1,0,0) (0,0,1) [4], which had the lowest Akaike Information
Criterion (AIC).
Figure 10. HFCE growth rate predicted values for 2022 – 2026 using SARIMA.
[83]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
3.2.2 Triple Exponential Smoothing Model
Figure 11. HFCE growth rate predicted values for 2022 - 2026 using exponential
smoothing.
Figure 11 exhibited the plot of Household Final Consumption Expenditure Growth
Rate prediction for 2022 to 2026 using the Triple Exponential Smoothing model. The
best model was ETS (1,0,0) which incorporated a smoothing factor of 0.9454, a trend
smoothing factor of 0.0002, and a 0.0001 seasonal change smoothing factor.
3.2.3 TBATS model
Figure 12 shows the plot of household final consumption expenditure growth rate
prediction for 2022 to 2026 using the TBATS model. The best model was calculated
using TBATS () functions in the R program with TBATS (1, {0, 0}, 0.8, -). Furthermore,
this model constituted a damping parameter of 0.8, an alpha of 1.0222, and a beta of -
0.2627.
Figure 12. HFCE growth rate predicted values for 2022 - 2026 using TBATS.
[84]

Dasmariñas, De Castro, Lazona & Usona      PUP J. Sci. Tech.
3.3  Best Statistical Model for Predicting Household Final Consumption
Expenditure
Table 1 presents the comparison of accuracy for the five-year forecast of Household
Final Consumption Expenditure Growth Rate using SARIMA, Triple Exponential
Smoothing, and TBATS. The models with the lowest combined Mean Squared Error
(MSE), Root Mean Square Error (RMSE), and Mean Absolute Error (MAE) for train
and test sets were chosen as the best models. This depicted that SARIMA (1,0,0) (0,0,1)
[4]performed the best model for predicting the HFCE from 2022 to 2026 with combined
train (MSE = 5.0330, RMSE = 2.2434, MAE = 1.2566) and test (MSE = 0.3101, RMSE
= 0.5569, MAE = 0.2677) set, followed by TBATS (1, {0,0}, 0.8, -) and ETS (1,0,0).
Table 1. Comparison of accuracy for SARIMA, exponential smoothing, and TBATS.
MODELS
Exponential
| ACCURACY  | SARIMA  |     | TBATS  |
| --------- | ------- | --- | ------ |
Smoothing
|       | Train  Test     | Train  Test      | Train  Test     |
| ----- | --------------- | ---------------- | --------------- |
| MSE   | 5.0330  0.3101  | 6.9866  13.0627  | 6.1459  0.4742  |
| RMSE  | 2.2434  0.5569  | 2.6432  3.6142   | 2.4791  0.6887  |
| MAE   | 1.2566  0.2677  | 1.4267  2.6146   | 1.2553  0.2484  |
3.4  Best machine Learning Regression Algorithm for predicting Household final
consumption expenditure
Table 2 shows the obtained regression metrics results for Extreme Gradient
Boosting (XGBoost), k-nearest neighbors (kNN), and Support Vector Regression (SVR).
The results showed that the SVR algorithm outperformed the other two models in
predicting  the  Philippines’  Quarterly  Household  Final  Consumption  Expenditure
(HFCE). The table reflected the lowest MSE (6.413), RMSE (2.532), and MAE (1.115)
on SVR. Moreover, the R-squared value of SVR (0.806) was the highest among the three
algorithms, implying that it best describes how well the regression model explains
observed data. Thus, 80.6% of the variability observed in the target variable was
explained by the regression model. It was also found that the XGBoost algorithm had the
lowest performance reflected by the highest MSE, RMSE, MAE, and R² values.
Moreover, it was also revealed that the XGBoost had almost equal performance with
kNN in predicting the HFCE Growth Rate. Thus, among the three models, SVR was the
best regression algorithm for predicting the country’s quarterly HFCE Growth Rate.
Table 2. Comparison of accuracy of regression algorithm (XGBoost, KNN, and SVR).
REGRESSION ALGORITHM
ACCURACY
|       | XGBoost  | kNN     | SVR     |
| ----- | -------- | ------- | ------- |
| MSE   | 6.4130   | 5.4230  | 2.3970  |
| RMSE  | 2.5320   | 2.3290  | 1.5480  |
| MAE   | 1.5710   | 1.3120  | 1.1150  |
| R2    | 0.4810   | 0.5610  | 0.8060  |
[85]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
4. CONCLUSIONS
In this study, the researchers have analyzed the impact of COVID-19 on the
Philippines’ quarterly Household Final Consumption Expenditure (HFCE). Time-series
analyses were used to forecast the quarterly HFCE of the country covering the period of
2022 to 2026. The visualization of the trajectory of the pandemic was shown using line
graphs.
Moreover, the researchers created a model to forecast the HFCE growth rate from
2022 to 2026 using SARIMA, Triple Exponential Smoothing, and the TBATS model.
Using MSE, RMSE, and MAE, the researchers built a model selection table containing
the best forecasting outcomes. The results showed that SARIMA (1,0,0) (0,0,1) [4] was
the best model for predicting the HFCE growth rate for the next five years. Wherein, it
implied that the Household Final Consumption Expenditure growth rate will gradually
decline during the span of forecasted years.
Furthermore, regression algorithms in machine learning, specifically XGBoost,
kNN, and SVR were compared in terms of error metrics (RMSE, MSE, and MAE) and
the goodness of fit of regression models (R²) to identify which among them has the
highest performance in predicting HFCE. Thus, the results revealed that with the
Inflation Rate, Unemployment Rate, Import of Goods and Services Growth Rate, Export
of Goods and Services Growth Rate being the predictor variables and HFCE Growth
Rate as the outcome variable, Support Vector Regression was the best regression
algorithm to be used for prediction.
In conclusion, based on the data, a drastic decline in the HFCE growth rate was
observed when COVID-19 spread throughout the country. Thus, the use of historical
data, including the years when COVID-19 occurred, dramatically affected the model for
forecasting the HFCE growth rate for the next five (5) years.
5. ACKNOWLEDGMENT
The researchers would like to offer their sincerest gratitude to their professors who
helped them with their study: Ms. Sandrilito Abogada for imparting her knowledge and
skills in forecasting and machine learning, and to Assoc. Prof. Laurence P. Usona, for
his guidance and assistance in completing this research.
Finishing the researchers’ study without the expertise, understanding, and patience of
Mr. Peter John B. Aranas, their research adviser, is impossible. The researchers would
like to thank their parents, as well, for their unconditional support and love.
It would take a lot of pages to enumerate the people whom the researchers are indebted
to, like their friends who gave support, motivation, and unexpected willingness to help
the team with their study. Lastly, this research was only done with the cooperation and
dedication of the researchers themselves in conducting this study.
[86]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
6. REFERENCES
Arapova, E. (2018). Determinants of household final consumption expenditures in Asian
countries: A panel model, 1991–2015. Applied Econometrics and International
Development, 18(1), 121-140.
Bajaj, A. (2022). ARIMA & SARIMA: Real-World Time Series Forecasting.
Neptune.Ai. https://neptune.ai/blog/arima-sarima-real-world-time-series-
forecasting-guide
Biswas, R. (2021). Philippines Economic Rebound Hit by New COVID-19 Wave.
Escalating New COVID-19 Cases Dampens Recovery. https://ihsmarkit.com/
research-analysis/ Philippine, https:// ihsmarkits-economic-rebound-hit-by-new-
covid19-wave.html.com/research-analysis/ Philippines-economic-rebound-hit-by-
new - covid19 -wave.html
Blaconá, M.T, Andreozzi, L. and Magnano, L. (2014). Time series models for different
seasonal patterns. Retrieved from https://forecasters.org/wp-content/
uploads/gravity_forms/72a51b93047891f1ec3608bdbd77ca58d/2014/06/Blacon%
C3%A1_MT_ISF2014.pdf.pdf
Brownlee, J. (2019, August 21). A Gentle Introduction to SARIMA for Time Series
Forecasting in Python.Machine Learning Mastery. https://machinelearningmastery.
com/sarima-for-time-series-forecasting-in-python/
Brownlee, J. (2021, March 6). XGBoost for Regression.Machine Learning Mastery.
https://machinelearningmastery.com/xgboost-for-regression/
Chatterjee, S. (2018, January 30). Time series analysis using Arima model in R.
DataScience+. Retrieved July 25, 2022, from https://datascienceplus.com/time-
series-analysis-using-arima-model-in-r/
Dela Cruz, A. (2019). Forecasting Philippine household final consumption expenditure
on education using discrete wavelet transformation on hybrid ARIMA-ANN
model. Indian Journal of Science and Technology, 12(33).
https://doi.org/10.17485/ijst/2019/v12i33/146427
Erero, J. &Makananisa M. (2020). Impact of Covid-19 on the South African economy:
A CGE, Holt-Winter and SARIMA model’s analysis. Turkish Economic Review,
7(4). Retrieved from
http://www.kspjournals.org/index.php/TER/article/view/2129
Frost, J. (2021, May 18). Exponential Smoothing for Time Series Forecasting.
Statistics By Jim. https://statisticsbyjim.com/time-series/exponential-smoothing-
time-series-forecasting/
Fürnkranz, J., Chan, P. K., Craw, S., Sammut, C., Uther, W., Ratnaparkhi, A., Jin, X.,
Han, J., Yang, Y., Morik, K., Dorigo, M., Birattari, M., Stützle, T., Brazdil, P.,
Vilalta, R., Giraud-Carrier, C., Soares, C., Rissanen, J., Baxter, R. A., . . . De Raedt,
L. (2011). Mean Squared Error. Encyclopedia of Machine Learning, 653.
https://doi.org/10.1007/978-0-387-30164-8_528
Fürnkranz, J., Chan, P. K., Craw, S., Sammut, C., Uther, W., Ratnaparkhi, A., Jin, X.,
Han, J., Yang, Y., Morik, K., Dorigo, M., Birattari, M., Stützle, T., Brazdil, P.,
[87]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
Vilalta, R., Giraud-Carrier, C., Soares, C., Rissanen, J., Baxter, R. A., . . . De Raedt,
L. (2011a). Mean Absolute Error. Encyclopedia of Machine Learning, 652.
https://doi.org/10.1007/978-0-387-30164-8_525
Gubangco, A. G. D., Joves, J. D. S., & Pizarro-Uy, A. C. D. (2022). Consumption in the
Philippines: In the course of unemployment and loan acquisition. Journal of
Economics, Finance and Accounting Studies, 4(2), 18-34.
Han, R. (2022, May). What is TBATS model in time series in R How to use it -
.ProjectPro. https://www.projectpro.io/recipes/what-is-tbats-model-time-series-
use-it
Handriyani, R., Sahyar, M. M., & Si, A. M. (2018). Analysis the effect of household
consumption expenditure, investment and labor to economic growth: A case in
province of North Sumatra. StudiaUniversitatisVasileGoldiș Arad,
SeriaȘtiințeEconomice, 28(4), 45-54.
Hyndman, R. J. (2018). In G. Athanasopoulos (Ed.), Forecasting: Principles and
Practice (2nd ed). Otexts. https://otexts.com/fpp2/holt-winters.html
Karabiber OA, Xydis G. (2019). Electricity price forecasting in the Danish Day-ahead
market using the TBATS, ANN and ARIMA methods. Energies.12(5). Retrieved
from https://doi.org/10.3390/en12050928
Kumar, A. (2022, February 21). R-squared, R² in Linear Regression: Concepts,
Examples. Data Analytics. https://vitalflux.com/r-squared-explained-machine-
learning/
Long, G. (2010). GDP prediction by support vector machine trained with genetic
algorithm. 2010 2nd International Conference on Signal Processing Systems.
https://doi.org/10.1109/icsps.2010.5555854
Madhav, N., Oppenheim, B., Gallivan,M., Mulembakani, P., Rubin, E., and Wolfe, N.
(2017). Pandemics: Risks, Impacts, and Mitigation. lnJamison DT, Gelband H,
Horton S, et al., (Eds). Disease Control Priorities: Improving Health and Reducing
Poverty (3rd ed). Washington DC.
McCloskey, B.(2022). Forecasting My Future Grocery Bills. Towards Data Science.
Retrieved from https://towardsdatascience.com/forecasting-my-future-grocery-
bills-59515b9348d3
Obinna, O. (2020). Effect of inflation on household final consumption expenditure in
Nigeria. Journal of Economics and Development Studies, 8(1), 104-111.
Pascasio, M. C., Dimafelix, A. D., Dimafelix, J. A. F., Chavez, L. T., &Robredo, J. E. P.
(n.d.). Demystifying the Household Final Consumption Expenditure (HFCE) in the
Philippine System of National Accounts (PSNA). Philippine Statistics Authority.
https://psa.gov.ph/sites/default/files/1.1.1%20Demystifying%20the%20Househol
d%20Final%20Consumption%20Expenditure%20%28HFCE%29%20in%20the%
20Philippine%20System%20of%20National%20Accounts%20%28PSNA%29_0.
pdf
Pedamkar, P. (2021, November 15). Support Vector Regression. EDUCBA.
https://www.educba.com/support-vector-regression/
[88]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
Philippine Statistics Authority .(2017). Inflation Rate.In Official Concept and Definition.
https://psa.gov.ph/ISSiP/concepts-and-definitions/161406
Priambodo, B., Rahayu, S., Hazidar, A. H., Naf’an, E., Masril, M., Handriani, I., Pratama
Putra, Z., KudrNseaf, A., Setiawan, D., &Jumaryadi, Y. (2019). Predicting GDP of
Indonesia using K-Nearest Neighbour Regression. Journal of Physics:Conference
Series, 1339(1), 012040. https://doi.org/10.1088/1742-6596/1339/1/012040
Qureshi, S. ,Chu B. & Demers, F. (2020). Forecasting Canadian GDP growth using
XGBoost.Carleton Economic Papers 20(14), Carleton University, Department of
Economics. Retrieved from https://ideas.repec.org/p/car/carecp/20-14.html
Rohmah, M. F., Putra, I. K. G. D., Hartati, R. S., &Ardiantoro, L. (2021). Comparison
four kernels of SVR to predict consumer price index. Journal of Physics:
Conference Series, 1737(1), 012018. https://doi.org/10.1088/1742-
6596/1737/1/012018
SAP.(2018). SAP HANA Predictive Analysis Library (PAL). Triple Exponential
Smoothing,400. https://help.sap.com/doc/86fb8d26952748debc8d08db756e6c1f/
1.0.12/en-US/ SAP_HANA_Predictive_Analysis_Library_PAL_en.pdf
Sayad, S. (n.d.).KNN Regression.Saedsayad. https://www.saedsayad.com/ k_nearest_
neighbors_reg.htm
Statista, Inc. (2022, January). Household final consumption expenditure on health in the
Philippines from 2017 to 2021. https://www.statista.com/statistics/709061/
philippines-household-co.statista.com/statistics/709061/nsumption-expenditure-
health/ Philippines-household-consumption-expenditure-health/
Sugiarto, S., &Wibowo, W. (2020). Determinants of regional household final
consumption expenditure in Indonesia.JEJAK, 13(2), 332-344.
Team, E. A. (2022, July 16). Calculating Mean Squared Error in Python. Educative:
Interactive Courses for Software Developers. https://www.educative.io/
answers/calculating-mean-squared-error-in-python
Teixeira-Pinto, A. (2021, August 2). 2 K-nearest Neighbours Regression | Machine
Learning for Biostatistics.The University of Sydney. https://bookdown.org/
tpinto_home/Regression-and-Classification/k-nearest-neighbours- regression.html
TenthPlanet. (2020, November 23). Time-Series Forecasting using TBATS model –
TenthPlanet Technologies. Blogs. https://blog.tenthplanet.in/time-series-
forecasting-tbats/
The World Bank Group.(2020). Impacts of COVID-19 on Households in the
Philippines.Results from the Philippines COVID-19 Households Survey.
https://thedocs.worldbank.org/en/doc/ab24c2a718fb53a344c5942d236b2fe6-
0070062021/original/Philippines-COVID-19-High-Frequency-Survey-
Household-Results-Slides.pdf
The World Bank Group.(2020b, November).Monitoring COVID-19 Impacts on Families
and Firms in the Philippines.https://www.worldbank.org/en/country/philippines/
brief/monitoring-covid-19-impacts-on-firms-and-families-in-the-philippines
[89]

Dasmariñas, De Castro, Lazona & Usona PUP J. Sci. Tech.
Varlamova, J., &Larionova, N. (2015).Macroeconomic and demographic determinants
of household expenditures in OECD countries.Procedia Economics and Finance,
24, 727-733.
Yadav, A. (2018, October 22). SUPPORT VECTOR MACHINES(SVM) – Towards
Data Science. Medium. https://towardsdatascience.com/support-vector-machines-
svm-c9ef22815589
World Health Organization. (2020, January 10). Coronavirus.
https://www.who.int/health-topics/coronavirus#tab=tab_1
[90]