---
source_file: "Hyndman & Kostenko, 2007.pdf"
source_sha256: "f4908ad19177769540edf84b6f28d94d22754e33a0d7aa64b617579b3cc2f4eb"
page_count: 4
converted_at: "2026-10-21T10:59:44Z"
converter: "markitdown"
---

MINIMUM SAMPLE SIZE REQUIREMENTS
FOR SEASONAL FORECASTING MODELS
Rob J. Hyndman and Andrey V. Kostenko
KEY POINTS
• How much data you need to forecast using a
INTRODUCTION
seasonal model depends on the type of model
“How much data do I need?” is probably the
being used and the amount of random variation
most common question our business clients
in the data.
ask us. The answer is rarely simple. Rather
it depends on the type of statistical model being used and • There are specific minimum sample size
on the amount of random variation in the data. Our usual requirements and we document these for
answer is “as much as possible” because the more data we common seasonal forecasting models.
have, the better we can identify the structure and patterns
• The minimum requirements apply when the
that are used for forecasting.
amount of random variation in the data is very
small. Real data often contain a lot of random
We are sometimes told that “there is no point using data
variation, and sample size requirements
from more than two or three years ago because demand is
increase accordingly.
changing too quickly for older data to be relevant.” This
reflects a misunderstanding of what a statistical model does; • Some published tables on sample size
it is designed to describe the way data changes. A good requirements are overly simplified.
model will allow for changing trend and changing seasonal
patterns. The issue is not whether things have changed, but
whether the way things change can be modeled.
coefficients (parameters) to estimate and the amount of
Rarely do we have so much data that we can afford to omit any. randomness in the data.
More often, we are trying to make do with limited historical
information. In these days of cheap data storage and high- Consider the simple scenario of linear regression. Here,
speed computing, there is no reason not to use all available y = a+bt+e where y is the observed series at time t, t is a
t t t
and relevant historical data when building statistical models. time index (1,2…) and e is a random error term. There are
t
However, we are sometimes asked to forecast very short time 2 parameters: the intercept a and the slope b.
series, and it is helpful to understand the minimum sample
size requirements when fitting statistical models to such data. In Figure 1, next page, we show two data sets, each with only 5
observations. The errors in the right plot have greater variation
RANDOMNESS AND PARAMETERS than the errors in the left plot. In both cases, however, the data
The number of data points required for any statistical were simulated from the same model, using a = 0 and b = 1.
model depends on at least two things: the number of model Then the model was estimated from the 5 data points.
Rob Hyndman is Professor of Statistics at Monash University, Australia, and Editor in Chief of the International
Journal Of Forecasting. As a consultant, he has worked with over 200 clients during the past 20 years, on
projects covering all areas of applied statistics, from forecasting to the ecology of lemmings. He is coauthor of
the well-known textbook, Forecasting: Methods And Applications (Wiley, 1998), and he has published
more than 50 journal articles. Rob is Director of the Business and Economic Forecasting Unit, Monash
University, one of the leading forecasting research groups in the world.
Andrey Kostenko is an independent consultant on complex systems. He received his first degree from a state
university in Russia and, with the help of a prestigious scholarship from the President of the Russian Federation,
an MBA from an institution in the UK. Recently, he was admitted as a PhD student to the Business and Economics
Forecasting Unit, Monash University, Australia.
12 FORESIGHT Issue 6 Spring 2007

Figure 1. Effect of Small vs. Large Random Variation
|     | 51  |     |     | 51  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     | 01  |     |     | 01  |     |     |     |
|     | 5   |     |     | 5   |     |     |     |
| y   | 0   |     | y   | 0   |     |     |     |
|     | 5-  |     |     | 5-  |     |     |     |
|     | 01- |     |     | 01- |     |     |     |
|     | 51- |     |     | 51- |     |     |     |
|     | 1 2 | 3 4 | 5   | 1 2 | 3 4 | 5   |     |
|     |     | t   |     |     | t   |     |     |
The  solid  line  shows  the  true  model  and  the  dashed  variables.” For example, with quarterly data, we can define
line shows the fitted model. The left-hand regression is  three new variables:
fine because the error variance is small. The right-hand
•  Q
regression is inaccurate because the data contain too much   = 1 when t is in the first quarter and zero otherwise;
1,t
random variation.  •  Q  = 1 when t is in the second quarter and zero
2,t
|     |     |     |     | otherwise;  |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | --- |
To accurately estimate a model where the data contain a lot  •  Q  = 1 when t is in the third quarter and zero otherwise.
3,t
of random variation, it is necessary to have a lot of data. On
the other hand, if the data have little variation, it is possible  Then the regression model is:
to estimate a model more or less accurately with only a few
| observations.  |     |     |     | y = a+bt+cQ | +cQ   | +cQ +e        |     |
| -------------- | --- | --- | --- | ----------- | ----- | ------------- | --- |
|                |     |     |     | t           | 1 1,t | 2 2,t 3 3,t t |     |

From  a  purely  statistical  point  of  view,  it  is  always  It is not necessary to include a term for the fourth quarter
necessary to have more observations than parameters.  because it is implicitly defined whenever the first 3 dummies
So, theoretically, it is feasible to estimate the regression  are equal to zero. Note that any one of the quarters could
line above with as few as 3 observations. (Any less and  be omitted, not necessarily the fourth quarter. Alternatively,
the  estimated  parameters  have  infinite  standard  errors,  we could omit the intercept and include seasonal dummy
and therefore prediction intervals will be infinitely wide.)  variables for all 4 quarters.
For the data in the left-hand plot, a regression through 3
observations  still  gives  reasonable  forecasting  results.  Whatever approach is taken, if m is the number of months
However, for the data in the right-hand plot, one would need  or quarters in a year, then m parameters are required. A
thousands of observations to get the same level of accuracy  regression usually also has another parameter for the time
that is possible with 3 observations in the left-hand plot.  trend. So the total number of parameters in the model is
m+1. Consequently, m+2 observations is the theoretical
This example illustrates that the size of the data set depends  minimum number for estimation; that is, 6 observations
on both the model and the level of randomness in the data.  for quarterly data and 14 observations for monthly data.
To give a reliable answer to questions of sample size, it is  But this will be sufficient only when there is almost no
essential to take the variability of the data into account.  randomness.  For  most  realistic  problems,  substantially
more data are required.
MINIMUM REQUIREMENTS
| FOR THREE COMMON METHODS |     |     | Holt-Winters Methods |     |     |     |     |
| ------------------------ | --- | --- | -------------------- | --- | --- | --- | --- |
Regression with Seasonal Dummies Holt-Winters (exponential smoothing) methods require the
When data are seasonal, a common way of handling the  estimation of up to 3 parameters (smoothing weights) for
seasonality in a regression framework is to add “dummy  the Level, Trend, and Seasonal components of the data.
|     |     |     |     | Spring 2007  Issue 6  FORESIGHT |     |     | 13  |
| --- | --- | --- | --- | ------------------------------- | --- | --- | --- |

Hence, Holt-Winters forecasting is often thought of as a the famous “airline” model of Box et al. (1994) is a
3-parameter method. However, the starting values for the monthly ARIMA (0,1,1)(0,1,1) model and so contains
12
Level, Trend, and Seasonal are also parameters that should 0+1+0+1+1+12 = 15 parameters.
be estimated.
Consequently, at least p+q+P+Q+d+mD+1 observations
For monthly data, there are 2 parameters associated with the are required to estimate a seasonal ARIMA model. For
initial level and initial trend values and 11 extra parameters the airline model, at least 16 observations are required.
associated with the initial seasonal components. (We don’t Note that this is actually less than for the Holt-Winters
need a starting value for the seasonal because it can be method applied to monthly data. There is a widely-held
calculated from the other 11 by imposing the constraint that misconception that ARIMA models are complex (and
the values must sum to zero for the additive model and to 12 therefore need more data) while exponential smoothing
for the multiplicative model.) methods such as Holt-Winters are simple (and need less
data). The truth is more complicated.
Similarly, for quarterly data, there are an extra 5 parameters.
These are often forgotten because the Holt-Winters THE CONSEQUENCES OF
equations are usually estimated using heuristic methods RANDOMNESS IN THE DATA
(see Makridakis et al., 1998). A better modelling approach Randomness in the data implies that the minimum statistical
(giving more accurate forecasts) is to estimate these starting requirements discussed in the previous section will be
values along with the smoothing parameters (Hyndman et insufficient to estimate seasonal models. But how much
al., 2002). Just because the starting values are not often more data will we need to compensate for randomness?
estimated along with the other parameters does not mean While there unfortunately are no specific rules, the general
they can be ignored. They are still parameters which require principle is straightforward.
estimation, even if that is sometimes done using relatively
simplistic approaches. In fact, the issue of specifying One way to think about the data requirement
these parameters becomes particularly important in small is in terms of the width of the prediction
sample sizes, especially when low values of the smoothing intervals (margins for error) around the point forecasts.
parameters are used, as they can have a big effect on the The minimum sample sizes we gave above are the
forecast values. numbers for which the prediction intervals are finite.
Smaller sample sizes than this and the PIs are infinite.
In general, for data with m seasons per year, there are m+1 As sample size (n) increases, the PIs decrease at a rate
initial values and 3 smoothing parameters, giving m+4 proportional to the square root of n. If you quadruple the
parameters altogether. Consequently, m+5 observations length of the series, you will cut in half the width of a PI.
is the theoretical minimum number for estimation: that is,
9 observations for quarterly data and 17 observations for USING SUPPLEMENTAL INFORMATION
monthly data. Again, these minima are not necessarily When data are scarce, consider using other information in
adequate to deal with randomness in the data. addition to the available data. As Michael Leonard shows in
the next commentary in this Foresight section, it is possible
ARIMA Models to use analogous time series that exhibit patterns similar to
Seasonal ARIMA models are usually described using the time series being forecast. Duncan et al. (2001) show
the notation ARIMA (p,d,q)(P,D,Q) where each of the how to draw information from analogous time series using
m
letters in parentheses indicates some aspect of the model. Bayesian pooling. Bayesian forecasting is often a productive
See Makridakis et al. (1998) for a description of seasonal choice when data are limited because it allows for the
ARIMA models. inclusion of other information, including expert opinion.
A seasonal ARIMA model has p+q+P+Q parameters. CONCLUSION
However, if differencing is required, an additional d+mD Forecasting short time series is fraught with difficulty, and
observations are lost. So a total of p+q+P+Q+d+mD sometimes we are compelled to provide forecasts from fewer
effective parameters are used in the model. For example, data points than we would like to have. We have discussed the
14 FORESIGHT Issue 6 Spring 2007

minimum number of observations that are required to estimate REFERENCES
some popular forecasting models, but it must be emphasized Box, G. E. P., Jenkins, G. M. & Reinsel, G. C. (1994). Time
that for many practical problems substantially more data are Series Analysis: Forecasting and Control (3rd ed.), Englewood
Cliffs, NJ: Prentice-Hall.
required before the resulting forecasts can be trusted.
Duncan, G., Gorr, W. & Szczypula, J. (2001). Forecasting analo-
Some authors report universal minimum data requirements gous time series, in J. S. Armstrong (Ed.), Principles of Forecast-
for different forecasting techniques, including those ing, Norwell, MA: Kluwer Academic Publishers, 195-213.
designed for seasonal time series. For example, see Hanke
Hanke, J. E., Reitsch, A. G. & Wichern, D. (1998). Business
et al. (1998, p.73). Such tables are misleading, because they Forecasting (6th ed.), Englewood Cliffs, NJ: Prentice-Hall.
ignore the underlying variability of the data, and, as we
Hyndman, R. J., Koehler, A. B., Snyder, R. D. & Grose, S.
have stressed, data requirements depend critically on the
(2002). A state space framework for automatic forecasting using
variability of the data. exponential smoothing methods, International Journal of Fore-
casting, 18 (3), 439–454.
Having short time series also significantly complicates the
Makridakis, S. G., Wheelwright, S. C. & Hyndman, R. J. (1998).
development and verification of models intended to produce
Forecasting: methods and applications (3rd ed.), New York : John
seasonal forecasts. What may be irrelevant when you have Wiley & Sons.
a lengthy time series can be very important for short data
samples. For example, when modelling short seasonal time
series, the choice of starting values becomes critical.
In short, there is no easy answer. One certainty is that
it is always necessary to have more observations than
parameters. But since in most practical applications the data Contact Info:
exhibit a lot of random variation, it is usually necessary to Rob J. Hyndman
have many more observations than parameters. Monash University, Australia
Rob.Hyndman@buseco.monash.edu
Andrey V. Kostenko
Independent Complex Systems Consultant, Russia
Andrey.Kostenko@ruenglish.com
Spring 2007 Issue 6 FORESIGHT 15