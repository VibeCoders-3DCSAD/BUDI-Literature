---
conversion_metadata:
  converted_at: "2026-09-07T05:54:01Z"
  converter_tool: "markitdown"
  converter_version: "0.1.7"
  source_pdf: "Gan & Kay, 2025.pdf"
  source_pdf_sha256: "81e673ae19598c5e1849c5d4e3cd720b998004c0a45745f1f62732de7dfc5dec"
  page_count: 22
  markdown_char_count: 110679
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Applied Finance Letters, Volume 14, 2025

Financial Knowledge, Health Factors, and Social Support: 
Determinants of Household Savings Behaviour in the U.S.

Lena Gan Author affiliation  
Kansas State University

Sara Kay Author affiliation  
Carnegie Mellon University

This study examines how financial knowledge, health factors, and social support 
influence  household  savings  behaviour  using  data  from  the  2022  Survey  of 
Consumer  Finances.  We  employ  binary  logistic  regression  and  interaction 
analysis  to  analyse  two  savings  measures:  general  savings  behaviour  and 
precautionary  savings  motives.  Our  findings  reveal  that  subjective  financial 
knowledge significantly increases saving likelihood, while health factors such as 
smoking and long COVID negatively impact savings behaviour. A key contribution 
is demonstrating that social support significantly moderates the negative effects 
of health factors on savings  behaviour, providing a crucial buffer during health-
related  financial  challenges.  The  analysis  also  reveals  significant  demographic 
disparities,  with  Hispanic  households  and  single  female-headed  households 
exhibiting  lower  savings  rates.  Notably,  health  challenges  simultaneously 
constrain  general  saving  capacity  while  heightening  precautionary  savings 
awareness, suggesting different pathways for savings behaviour. These findings 
extend  the  Life  Cycle  Hypothesis  by  integrating  behavioural  dimensions  into 
household savings decisions and highlight the need for targeted interventions that 
address health inequalities while strengthening social support networks.

Keywords: household savings, financial knowledge, health factors, social support,  
life cycle hypothesis

1.  Introduction

A  central  question  in  household  finance  research  is  how  individuals  allocate  income 
between current consumption and savings for future needs (Browning & Lusardi, 1996). 
Despite  its  crucial  role  in  financial  security  and  retirement  preparedness,  many  U.S. 
households  continue  to  struggle  with  saving.  Nearly  half  of  those  nearing  retirement 
report insufficient savings (U.S. Federal Reserve, 2023), and recent data from the 2025 
National  Financial  Capability  Survey  (NFCS)  show  that  nearly  40%  of  middle-income 
households  are  financially  fragile,  unable  to  cover  basic  expenses  or  weather

58

---

<!-- PAGE 2 -->

Applied Finance Letters, Volume 14, 2025

unexpected  shocks  (FINRA,  2025).  This  erosion  of  financial  stability  underscores  the 
need to better understand the behavioural and structural factors that shape household 
savings behaviour.

The  Life  Cycle  Hypothesis  (LCH)  offers  a  foundational  framework,  positing  that 
individuals  smooth  consumption  over  time  based  on  expected  lifetime  income  and 
longevity (Ando & Modigliani, 1963). However, actual household savings behaviour often 
diverges  from  this  model’s  predictions.  Subjective  life  expectancy  and  health 
perceptions—rather  than  actuarial  longevity  alone—appear  to  drive  saving  decisions 
(Bloom  et  al.,  2006;  Post  &  Hanewald,  2012).  Poor  health  can  also  reduce  future 
orientation  and  increase  present  bias,  especially  under  uncertainty  (Smith,  1999; 
Cronqvist & Siegel, 2013).

A  growing  literature  suggests  that  financial  knowledge  plays  a  dual  role:  it  enhances 
financial  capability  and  indirectly  shapes  health  behaviours.  Financially  literate 
individuals  tend  to  exhibit  lower  time  preference, stronger  planning  skills,  and  greater 
self-control—traits linked to both saving and healthy lifestyle choices (Meier & Sprenger, 
2010; Lusardi & Mitchell, 2014; Lal et al., 2022). For example, higher financial knowledge 
is associated with a lower probability of smoking (Khan et al., 2021), more engagement 
in preventive care (Xu et al., 2020), and better long-term financial outcomes. These traits 
contribute to longer life expectancy, a link supported by growing longitudinal evidence. 
For instance, lower financial knowledge has been shown to directly and independently 
predict mortality risk in older adults, independent of socioeconomic status and health 
(Gladstone & Hundtofte, 2023; Stewart et al., 2020). Furthermore, the accumulation of 
wealth—a key outcome of financial capability—is one of the strongest socioeconomic 
predictors of survival, underscoring the importance of the wealth-based channel (Chetty 
et al., 2016; Glei et al., 2022). These cognitive and behavioural traits not only promote 
healthier  decisions  but  also  contribute  to  long-term  wealth  accumulation—a  known 
determinant of longevity through better access to healthcare, safer environments, and 
resilience to shocks (Chetty et al., 2016).

Social  support  networks  buffer  negative  financial  effects  of  poor  health  (Chen  et  al., 
2024;  Gertler  &  Gruber,  2002)  by  providing  informal  insurance—reducing  perceived 
saving needs by 24% (Dhakhwa & Barbiarz, 2019), providing emotional support (Bhatia et 
al.,  2023;  Czaja  et  al.,  2021)  and  partially  smoothing  consumption  in  health  crises 
(Gertler  &  Gruber,  2002).  While  these  findings  confirm  the  mitigating  role  of  social 
support, its effectiveness may vary depending on the severity of health conditions and 
the reliability of support networks (Chen et al., 2024; Dhakhwa & Barbiarz, 2019; Bhatia 
et al., 2023; Gertler & Gruber, 2002).

While  the  LCH  provides  a  valuable  foundation  for  understanding  saving  decisions,  its 
original  formulation  does  not  account  for  individual-level  cognitive  and  behavioural 
factors such as financial knowledge, subjective health assessments, or health-related

59

---

<!-- PAGE 3 -->

Applied Finance Letters, Volume 14, 2025

decision-making.  Instead,  it  focuses  on  income,  age,  and  actuarial  life  expectancy  as 
objective  drivers  of  consumption  smoothing  (Modigliani  &  Brumberg,  1954;  Ando  & 
Modigliani,  1963).  As  such,  key  variables  that  shape  modern  household  saving—
especially those involving health shocks, health perceptions, and financial capability—
remain theoretically peripheral or absent in standard LCH models.

This  study  extends  the  LCH  by  incorporating  behavioural  and  cognitive  dimensions—
specifically  financial  knowledge,  subjective  and  objective  health,  and  informal  social 
support—to  better  reflect  the  complexity  of  household  savings  behaviour.  Using  data 
from  the  2022  Survey  of  Consumer  Finances  (SCF),  we  investigate  three  research 
questions:

1.  How do subjective and objective health factors affect savings behaviour?

2.  Does  financial  knowledge  moderate  the  relationship  between  health  status  and

saving?

3.  To what extent does social support moderate the relationship between health factors

and household savings behaviour?

Our findings contribute to a more holistic understanding of household savings behaviour 
by highlighting the interactive roles of financial knowledge, health resilience, and social 
context.

2.  Data and Methods 
2.1. Data

The study used a dataset from the 2022 Survey of Consumer Finances (SCF), a triennial 
survey  conducted  by  the  Board  of  Governors  of  the  Federal  Reserve  System.  The  SCF 
provides detailed and nationally representative data on the financial characteristics of 
U.S.  households,  including  assets,  liabilities,  income  and  financial  decision-making 
(Bhutta et al., 2020). While the SCF is conducted every three years, the 2022 wave was 
selected specifically because it contains unique post-pandemic variables—such as long 
COVID, health disruptions, and pandemic-era saving motivations—that are essential to 
the  present  study’s  examination  of  the  relationship  between  health  factors,  financial 
knowledge,  and  household  savings  behaviour.  These  features  allow  us  to  evaluate 
financial resilience in the context of systemic health uncertainty and capture behavioural 
responses not observable in pre-pandemic waves such as 2019 and earlier waves.

To measure household savings behaviour, we employed two complementary indicators: 
a  general  saving  flow  measure  and  a  precautionary  saving  motive  measure.  First, 
following  Kennickell  (1995),  we  used  the  SCF  question  asking  whether  household 
spending  was  “less  than,”  “equal  to,”  or  “more  than”  income  in  the  previous  year. 
Respondents  who  reported  spending  less  than  income  were  classified  as  savers,

60

---

<!-- PAGE 4 -->

Applied Finance Letters, Volume 14, 2025

capturing a behavioural proxy for net positive saving flow. This simple indicator, though 
not a measure of accumulated assets or net worth, has been widely used and validated 
in  past  studies  as  a  robust  estimate  of  household  savings  behaviour  across  income 
groups and demographic categories (Hogarth & Anguelov, 2003; Rha et al., 2006; Hanna 
& Lindamood, 2010; Yuh & Hanna, 2010).

Second, to better align with our theoretical interest in health-driven household savings 
behaviour,  we  constructed  a  precautionary  savings  variable.  This  binary  measure 
captures  whether  households  reported  saving  for  emergencies,  unemployment,  or 
medical  expenses—motivations  that  became  especially  salient  during  the  COVID-19 
pandemic. Following the approach of Fisher and Anong (2012), households were coded 
as  having  a  precautionary  savings  motive  if  any  of  the  SCF’s  saving  reason  codes 
included  unemployment  reserves,  illness/medical  expenses,  or  emergencies.  This 
secondary measure enables us to distinguish risk-buffering savings motives from other 
saving goals such as wealth preservation or lifestyle maintenance or future aspirations.

The  SCF  uses  a  complex  dual-frame  sampling  system,  combining  an  area-probability 
sample with a list sample that oversamples high-wealth households, thereby capturing 
the full distribution of U.S. household finances (Bhutta et al., 2023). To address missing 
data, the SCF provides five implicates generated through multiple imputation, allowing 
for population-level estimation and variance adjustment (Aizcorbe et al., 2003). The 2022 
SCF dataset includes 4,595 households, when appropriately weighted, is representative 
of 133.6 million U.S. households.

2.2. Variable Definitions

Dependent Variable. Two dependent variables were used to capture different aspects 
of household savings  behaviour. First, a  binary indicator  of net savings  behaviour was 
created based on responses to whether household spending was less than income (1 = 
saver, 0 = non-saver). This flow-based indicator captures behavioural intent to consume 
less  than  earned  income  over  the  past  year.  Second,  precautionary  saving  was 
operationalised as a binary variable indicating whether the household cited emergency, 
health,  or  unemployment-related  motives  for  saving—allowing  us  to  assess  targeted 
financial preparation in response to health risk and uncertainty.

Independent  Variables.  Table  1  provides  detailed  definitions,  measurement 
specifications, and SCF variable codes for all variables used in our analysis.

Table 1: Variable Definitions and Measurement

Variable

Definition

Measurement

SCF 
Variable 
Code

61

---

<!-- PAGE 5 -->

Applied Finance Letters, Volume 14, 2025

Dependent 
Variables

Saver

Precautionary 
Saving Motive

Independent 
Variables

Expected 
longevity

Objective 
financial 
knowledge 
Subjective 
financial 
knowledge

Health status

Smoker

Health 
insurance

Parental 
mortality

COVID 
diagnosis

Long COVID

Social support

Sociodemogra
phic Variables 
Gender/Marital 
status

Whether household 
spent less than 
income in the past 
year 
Whether household 
reported saving for 
emergencies, 
unemployment, or 
medical expenses as 
primary motivations

Respondent’s self-
reported expected age 
at death

“Big Three” financial 
knowledge questions

Self-assessment of 
financial knowledge

Self-reported health 
condition 
Current smoking 
status 
Whether household 
has health insurance 
coverage 
Whether respondent’s 
parent(s) are still alive 
Whether respondent 
was diagnosed with 
COVID-19 
Whether respondent 
experienced long 
COVID symptoms 
Whether household 
could get $3,000 from 
friends/family in 
emergency

Binary (1=Yes, 0=No)

Binary (1=Has precautionary motive, 0=No 
precautionary motive). Coded as 1 if any of 
the six saving motive variables contained 
codes 23 (unemployment reserves), 24 
(illness/medical expenses), or 25 
(emergencies/rainy days/security)

Continuous (years)

Composite score (0-3)

Categorical based on 0-10 scale: Low (0-3), 
Medium  
(4-6), High (7-10)

X7510

X3006, 
X3007, 
X7513, 
X7514, 
X7515, 
X6848

X7381

X7558, 
X7559, 
X7560

X7556

Categorical (Excellent/Good/Fair/Poor)

X6030

Binary (1=Yes, 0=No)

Binary (1=Yes, 0=No)

Binary (1=Yes, 0=No)

Binary (1=Yes, 0=No)

Binary (1=Yes, 0=No)

X7380

X6341

X6026, 
X6028

X19046

X19048

Binary (1=Yes, 0=No)

X6443

Household structure

Categorical (Married/Partner/Single 
Female/Single Male)

X8021, 
X8023

62

---

<!-- PAGE 6 -->

Applied Finance Letters, Volume 14, 2025

Age

Race

Income

Education

IHS net worth

Racial/ethnic 
background 
Highest level of 
education completed 
Respondent’s age in 
years 
Annual household 
income 
Inverse hyperbolic sine 
transformation of 
household net worth 
Whether household 
owns primary 
residence 
Number of children in 
household 
Current employment 
situation 
Expected change in 
income relative to 
inflation 
Source: 2022 Survey of Consumer Finances

Number of 
children 
Employment 
status

Income 
expectations

Home 
ownership

Categorical (White/Black/Hispanic/Asian 
Other) 
Categorical (No HS/HS/Some 
College/College/Graduate)

Continuous

Continuous (log-transformed)

Continuous (IHS transformed)

Binary (1=Yes, 0=No)

Categorical (0/1-3/4+)

Categorical 
(Employed/Retired/Unemployed/Disabled)

Categorical (Higher/Same/Lower)

X6809

X5931

X14

X5729

Networth

X508

X6903

X4511

X7364

2.3. Descriptive Statistics

Table  2  presents  descriptive  statistics  for  the  sample.  As  shown,  62%  of  households 
(weighted) reported saving (spending less than income) vs. 38% of non-savers, while 40% 
had precautionary savings motives vs 60% without. Married households comprised 46% 
of  respondents,  with  single  females  representing  26%  and  single  males  18%.  Race 
distribution showed White respondents made up 68% of the sample, Black respondents 
15%,  Hispanic  respondents  12%,  and  Asian/Other  respondents  5%.  Educational 
attainment  varied,  with  22%  having  a  bachelor’s  degree  and  17%  having  graduate 
degrees.  Notably,  65%  of  respondents  were  homeowners,  and  17%  were  smokers. 
Regarding  subjective  financial  knowledge,  74%  reported  high  knowledge  levels,  21% 
medium, and 5% low levels.

Table 2: Sample Characteristics (N=4,595)

Variable 
Saver 
Yes 
No 
Precautionary Saver 
Yes 
No

Weighted %

62 
38

40 
60

63

---

<!-- PAGE 7 -->

Applied Finance Letters, Volume 14, 2025

Yes 
No 
Gender/Marital Status 
Married 
With partner 
Single Female 
Single Male 
Race 
White 
Black 
Hispanic 
Asian/Other 
Employment 
Employed 
Unemployed 
Retired 
Disabled 
Education 
Less than High school 
High School 
Some College 
Bachelor’s 
Graduate 
Home Ownership 
Number of Kids 
0 
1-3 
4 or more 
Health Factors 
Respondent is a smoker 
Have Health Insurance 
coverage 
Respondent’s parent(s) still 
alive 
COVID diagnosed 
Long COVID 
Respondent’s health status 
Excellent 
Good 
Fair 
Poor 
Subjective Financial 
Knowledge 
Low 
Medium 
High 
Emergency Social Support

40 
60

46 
10 
26 
18

68 
15 
12 
  5

65 
23 
  5 
  7

9 
22 
30 
22 
17 
65

61 
36 
  3

17

86

62

42 
15

24 
50 
22 
  4

5 
21 
74 
66

Source: 2022 Survey of Consumer Finances

64

---

<!-- PAGE 8 -->

Applied Finance Letters, Volume 14, 2025

Table 3 shows the distribution of continuous variables in the sample. The mean age of 
respondents was 51.3  years (weighted). The  mean expected longevity was 85.1 years. 
Mean household income was $106,251, and mean net worth was $746,821.

Table 3: Descriptive Statistics for Continuous Variables (N=4,595)

Variable

Mean

Median

SD

Respondent’s Age 
Expected longevity 
Income 
Net worth 
Objective financial knowledge (0-3)

51 
85

51.3 
85.1 
$106,251  $59,050 
$746,821  $121,760 
2.1

2

17.4 
11.32 
$58,986 
$612,721 
0.8

Source: 2022 Survey of Consumer Finances

2.4. Conceptual and Empirical Framework

Conceptual  Framework.  Figure  1  presents  a  behavioural  extension  of  the  Life  Cycle 
Hypothesis  (LCH),  integrating  financial  knowledge,  health  factors,  and  social  support 
into saving models traditionally  centred on income, age, and actuarial life expectancy 
(Modigliani  &  Brumberg,  1954).  These  behavioural  inputs  help  explain  systematic 
deviations from rational saving predicted by standard models.

Health  perceptions  and  vulnerability  shape  savings  decisions  more  than  objective 
measures  alone  (Hamermesh,  1985;  Hurd  &  McGarry,  1995).  Financial  knowledge 
contributes to these perceptions and their behavioural consequences through improved 
self-regulation, long-term planning, and future-oriented behaviours (Meier & Sprenger, 
2010;  Lusardi  &  Mitchell,  2014).  Empirical  studies  confirm  that  higher  financial 
knowledge is linked to lower smoking prevalence (Khan et al., 2021), greater engagement 
in  preventive  health  actions  (Xu  et  al.,  2020),  and  improved  executive  function 
(Baumeister  &  Heatherton,  1996).  These  cognitive  traits—especially  self-control  and 
delayed  discounting—bridge  financial  and  health  domains.  Smokers  tend  to  exhibit 
higher discount rates and lower cognitive performance (Bickel et al., 1999; Adams et al., 
2014),  traits 
inversely  associated  with  financial  knowledge.  These  behaviours 
cumulatively  influence  wealth  accumulation  and  health  trajectories,  affecting  both 
perceived and actual life expectancy (Chetty et al., 2016).

Social  support  provides  a  crucial  but  underexplored  buffer  against  health-related 
financial challenges. Social networks serve as informal safety nets, providing resources 
during  crises  and  reducing  financial  stress  (Cox  &  Fafchamps,  2008).  They  buffer  the 
adverse effects of poor health on household savings behaviour by alleviating emotional 
and  economic  burdens  (Mani  et  al.,  2013).  Our  framework  posits  that  social  support 
moderates  the  relationship  between  health  factors  and  household  savings  behaviour,

65

---

<!-- PAGE 9 -->

Applied Finance Letters, Volume 14, 2025

representing a key theoretical contribution.

By jointly examining these behavioural mechanisms, this study offers a more complete 
account of household savings behaviour than classical LCH formulations allow.

Figure 1: Conceptual Framework of the Extended Model

Empirical Specifications. A binary logistic regression model was employed to analyse 
the  probability  of  a  household  savings  (spending  less  than  income)  versus  not  saving 
(spending equal to or more than income). The model can be expressed as:

log[P(Y=1)/P(Y=0)]=β0+β1X1+β2X2+...+βkXk+ϵ

Where:

•  P(Y=1) is the probability of saving (spending less than income)

•  P(Y=0) is the probability of not saving (spending equal to or more than income)

•  β0 is the intercept

•  β1...βk are the regression coefficients

•  X1...Xk are the independent variables

66

---

<!-- PAGE 10 -->

Applied Finance Letters, Volume 14, 2025

•  ϵ is the error term

The odds ratio (OR) for each independent variable was calculated as: OR=exp(β)

Where a value greater than 1 indicates that the variable increases the odds of saving, and 
a value less than 1 indicates that the variable decreases the odds of saving.

2.5. Measurement of Key Variables

Financial  Knowledge  Measurement.  Financial  knowledge  was  assessed  using  both 
objective and subjective indicators drawn from the SCF. Objective financial knowledge 
was  measured  using  the  Big  Three  financial  knowledge  questions,  which  assess 
understanding  of  (1)  compound  interest,  (2)  inflation  and  real  returns,  and  (3)  risk 
diversification. These questions were first developed for the 2004 Health and Retirement 
Study (HRS) and have since become widely adopted in large-scale surveys such as the 
National  Financial  Capability  Study  (NFCS),  the  Survey  of  Household  Economics  and 
Decision  making  (SHED),  and  the  Survey  of  Consumer  Finances  (SCF).  Specifically, 
respondents were asked:

1.  Interest rate: “Suppose you had $100 in a savings account and the interest rate was 
2% per year. After 5 years, how much do you think you would have in the account if 
you left the money to grow?”

2.  Inflation question: “Imagine that the interest rate on your savings account was 1% per 
year and inflation was 2% per year. After 1 year, how much would you be able to buy 
with the money in this account?”

3.  Risk  diversification:  “Do  you  think  that  the  following  statement  is  true  or  false?” 
‘Buying a single company stock usually provides a safer return than a stock mutual 
fund.’

Each response was coded as correct or incorrect and summed, resulting in a composite 
score  ranging  from  0  to  3.  This  three-item  scale  has  been  used  in  numerous  peer-
reviewed studies to capture essential financial decision-making competencies (Hastings 
et al., 2013; Lusardi & Mitchell, 2014). However, its brevity may constrain its construct 
validity as noted by Gignac and Ooi (2022) due to the number of questions. This limitation 
reflects the constraints of the SCF instrument rather than study design. Nonetheless, the 
Big  Three  are  considered  a  validated  minimal  benchmark  for  international  financial 
knowledge assessment and remain suitable for national comparisons (Anderson et al., 
2017;  Behrman  et  al.,  2012;  Goyal  &  Kumar,  2021;  Hastings  et  al.,  2013;  Lusardi  & 
Mitchell, 2011; 2014).

Subjective financial knowledge was measured using a self-assessment question where 
respondents  rated  their  overall  financial  knowledge  on  a  scale  from  0  (not  at  all

67

---

<!-- PAGE 11 -->

Applied Finance Letters, Volume 14, 2025

knowledgeable)  to  10  (very  knowledgeable).  Following  previous  research  (Allgood  & 
Walstad, 2016), we categorised these responses into three levels: Low (0-3), Medium (4-
6),  and  High  (7-10).  This  categorical  approach  captures  meaningful  differences  in 
financial confidence levels, with 77% of respondents reporting high knowledge levels in 
our sample.

Health and Social Support Measures. Health was measured using multiple indicators:

•  Self-reported health status (Excellent/Good/Fair/Poor)

•  Smoking status (Yes/No)

•  COVID-19 diagnosis (Yes/No)

•  Long COVID symptoms (Yes/No)

Following  the  study  by  Ouyang  et  al.  (2025),  social  support  was  measured  using  the 
question about whether the respondent could obtain $3,000 from friends or family in an 
emergency (Yes/No). This measure captures the availability of informal financial safety 
nets that can serve as a temporary financial buffer that might influence saving decisions, 
particularly during health-related financial emergencies.

2.6. Interaction Models and Data Analysis

Interaction Models. To examine the joint effects of financial knowledge, health factors, 
and  social  support  on  household  savings  behaviour,  we  estimated  several  interaction 
models. Our primary interaction model can be expressed as:

log[P(Y=1)/P(Y=0)]=β0+β1(Health)+β2(FinKnowledge)+β3(SocialSupport)+β4
(Health×FinKnowledge)+β5(Health×SocialSupport)+βkXk+ϵ

Where Health  represents various health factors (self-reported  health  status, smoking, 
etc.), Fin Knowledge represents our measures of financial knowledge (both objective and 
subjective),  and  Social  Support  represents  our  measure  of  emergency  support 
availability. These interaction terms allow us to test whether:

1.  The  effect  of  health  factors  on  household  savings  behaviour  varies  by  financial

knowledge level

2.  Social  support  moderates  the  relationship  between  health  factors  and  household

savings behaviour

Data  Analysis  Plan.  We  assessed  multicollinearity  using  Pearsons  correlation  and 
Variance Inflation Factors (VIF). Cross-tabulation for two saving measures (χ² = 2.49, p = 
0.115) confirms they capture distinct but related dimensions, with 39.8% of non-savers 
reporting precautionary motives and 38.9% of savers lacking precautionary motivations,

68

---

<!-- PAGE 12 -->

Applied Finance Letters, Volume 14, 2025

validating our dual-measure approach.

Given  the  SCF’s  complex  sampling  design  and  multiple  imputation,  we  applied 
‘repeated-imputation inference’ (RII) techniques with replicate weights to bootstrap the 
standard  errors,  following  established  practices  for  nonlinear  models  with  multiple 
imputed survey (Lindamood et al., 2007; Montalto & Yuh, 1998; Nielsen & Seay, 2014; 
Shin & Hanna, 2017). All analyses used Stata MP18 with appropriate survey weights.

3. Results and Discussion 
3.1. Multicollinearity Assessment

Our multicollinearity diagnostics indicated no severe multicollinearity issues among the 
predictors  in  our  logistic  regression  model.  The  mean  VIF  was  2.40,  well  below  the 
conventional  threshold  of  concern  of  10.  Pearson’s  correlation  analysis  showed 
expected  associations  between  related  variables.  The  highest  correlations  occurred 
between age and household expected remaining life (r=−0.80), which is expected given 
their  conceptual  relationship.  The  moderate  correlation  between  income  and  wealth 
(r=0.41)  is  also  consistent  with  financial  theory.  Table  4  presents  key  correlation 
coefficients among selected variables.

Log 
Income

Net 
Worth

Age

Poor 
Health

Fin 
Know 
(Obj)

Subj 
Fin 
Know 
(High)

Smoker

Soc 
Sup

Black

Hispa
nic

Expect 
Longev

COVID 
Diagnos
d

Long 
COVID

Log Income  1.000

Net Worth  0.366*

1.000

Age

0.172*

0.175*  1.000

Poor Health  -0.121*

-
0.036*

0.084*  1.000

Fin 
Knowledge 
(Obj)

Subj Fin 
Knowledge 
(High)

0.278*

0.088*  0.093*

-
0.087*

1.000

0.265*

0.118*  0.243*

-
0.046*

0.184*  1.000

Smoker

-0.178*

-
0.057*

-
0.108*

0.080*  -0.149*

-
0.116*

1.000

Social 
Support

0.263*

0.099*  0.073*

-
0.081*

0.206*  0.123*  -0.147*  1.000

Black

-0.216*

Hispanic

-0.150*

-
0.075*

-
0.102*

-
0.072*

-
0.175*

0.041*  -0.197*

0.012

-0.150*

-0.050*

-
0.102*

-
0.802*

-
0.160*

-0.015

-
0.101*

-
0.134*

-
0.121*

0.117*

-
0.240*

1.000

-0.007

-
0.157*

-
0.188*

1.000

-0.003

-0.018  0.120*  0.119*  1.000

Expected 
Longevity

COVID 
Diagnosed

0.147*

0.062*

Long COVID  -0.085*

-0.023

-
0.163*

-
0.132*

-0.014  0.083*  0.018

-0.086*  0.080*

0.052*  -0.055*

-
0.078*

0.029

-
0.090*

-
0.101*

0.059*  0.168*

1.000

0.019  0.126*  0.075*

0.395*

1.000

69

---

<!-- PAGE 13 -->

Applied Finance Letters, Volume 14, 2025

Note:  *  indicates  significance  at  p  <  0.05  level.  Highest  correlation  between  age  and 
expected longevity (r = -0.802) reflects conceptual relationship.

The  binary  logistic  regression  model  examining  factors  associated  with  household 
savings behaviour demonstrated adequate fit with a McFadden pseudo-R² of .16 and a c-
statistic of .77, indicating good discriminatory power. Table 5 summarises the results of 
the logistic regression model predicting the likelihood of being a saver.

3.2. Logistic Regression Results

The  binary  logistic  regression  model  examining  factors  associated  with  household 
savings behaviour demonstrated adequate fit with a McFadden pseudo-R² of .16 and a c-
statistic of .77, indicating good discriminatory power. Table 5 summarises the results of 
the logistic regression model predicting the likelihood of being a saver.

Table 5: Logistic Regression Results Predicting Household Savings Behaviour 
Variable

95% CI

Coeff

OR

SE

p

Socioeconomic factors 
Log income 
IHS net worth 
Demographic characteristics 
Age 
Black 
Hispanic 
Other race 
Household structure 
Single male head 
Single female head 
Children in household 
Education level 
High school graduate 
Some college 
College graduate or higher 
Employment level 
Employed 
Retired  
Disabled 
Health factors 
Expected longevity 
Good health 
Fair health 
Poor health 
Smoker

0.231 
0.033

0.084 
0.008

1.260 
1.034

[1.069, 1.484] 
[1.018, 1.050]

.006** 
<.001***

[0.988, 1.011] 
[0.762, 1.281] 
[0.552, 0.908] 
[0.620, 1.241]

.898 
.930 
.006** 
.460

[0.714, 1.137] 
[0.513, 0.844] 
[0.624, 0.981]

.381 
.001*** 
.033*

[1.018, 1.989] 
[0.908, 1.793] 
[0.998, 2.041]

.039* 
.160 
.052

[1.042, 2.475] 
[0.798, 2.136] 
[0.618, 1.820]

.032* 
.288 
.832

[0.996, 1.014] 
[0.702, 1.095] 
[0.619, 1.070] 
[0.410, 1.009] 
[0.543, 0.893]

.239 
.246 
.140 
.055 
.004**

-0.001 
-0.012 
-0.346 
-0.131

-0.104 
-0.419 
-0.245

0.353 
0.244 
0.356

0.474 
0.266 
0.059

0.005 
-0.132 
-0.206 
-0.441 
-0.362

0.999 
0.988 
0.708 
0.877

0.901 
0.658 
0.783

1.423 
1.276 
1.427

1.61 
1.31 
1.06

1.005 
0.876 
0.814 
0.643 
0.696

0.006 
0.132 
0.127 
0.177

0.119 
0.127 
0.115

0.171 
0.174 
0.183

0.22 
0.251 
0.276

0.005 
0.114 
0.140 
0.230 
0.127

70

---

<!-- PAGE 14 -->

Applied Finance Letters, Volume 14, 2025

0.183

0.113

.672 
.614 
.159 
.019*

1.081 
1.065 
0.868 
0.734

0.183 
0.125 
0.101 
0.131

0.078 
0.063 
-0.142 
-0.309

[0.754, 1.548] 
[0.833, 1.362] 
[0.712, 1.057] 
[0.567, 0.950]

Has health insurance 
Parents living 
COVID diagnosed 
Long COVID 
Financial knowledge & social 
support 
Objective financial knowledge  
Subjective fin. knowledge 
(Medium) 
0.205 
Subjective fin. knowledge (High)  0.534 
0.096 
0.275 
Emergency social support 
0.130 
0.170 
Expected income (up) 
0.097 
-0.084 
Expected income (down) 
Constant 
1.043 
-3.690 
Note:  CI  =  confidence  interval;  OR  =  odds  ratio.  Reference  categories:  White 
(race/ethnicity),  Married/partnered  (household  structure),  Less  than  high  school 
(education),  Self-reported  health  excellent/very  good  (health  status),  Low  (subjective 
financial knowledge), No social support. *p<.05, **p<.01, ***p<.001.

[1.141, 2.551] 
[1.090, 1.589] 
[0.920, 1.529] 
[0.760, 1.112] 
[0.003, 0.193]

.009** 
.004** 
.189 
.388 
<.001***

1.706 
1.316 
1.186 
0.920 
0.025

[0.962, 1.499]

[0.820, 1.823]

1.201

1.222

0.204

0.201

.325

.106

3.3. Key Findings

Socioeconomic factors strongly predicted household savings behaviour. Higher income 
(OR = 1.260, p = .006) and net worth (OR = 1.034, p < .001) increased saving likelihood. 
Significant demographic disparities emerged: Hispanic households had 0.71 times the 
odds of saving compared to White households (OR = 0.708, p = .006), and single female-
headed  households  had  0.66  times  the  odds  compared  to  married/partnered 
households (OR = 0.658, p = .001).

Health factors showed significant negative associations with saving. Smokers had 0.70 
times  the  odds  of  saving  compared  to  non-smokers  (OR  =  0.696,  p  =  .004),  while 
households affected by long COVID had 0.73 times the odds compared to unaffected 
households (OR = 0.734, p = .019). Poor health showed marginally significant effects (OR 
= 0.643, p = .055). Contrary to theoretical expectations, expected longevity did not predict 
household savings behaviour (OR = 1.005, p = .239).

Financial  knowledge  effects  varied  by  measurement  type.  While  objective  knowledge 
was  non-significant  (OR  =  1.201,  p  =  .106),  households  with  high  subjective  financial 
knowledge  had  1.71  times  the  odds  of  saving  compared  to  those  with  low  subjective 
financial knowledge (OR = 1.706, p = .009). Households with emergency social support 
had 1.32 times the odds of saving compared to those without such support (OR = 1.316, 
p = .004).

3.4 Interaction Analysis and Robustness Checks

71

---

<!-- PAGE 15 -->

Applied Finance Letters, Volume 14, 2025

Interaction  Effects.  To  address  our  third  research  question  about  social  support 
moderation,  we  tested  interactions  between  health  factors  and  emergency  social 
support. Table 6 presents these results.

Table 6: Interaction Effects on Household Savings Behaviour

Health Factor

Interaction with Social Support

Coefficient  OR

Poor health × Social support  0.687 
Smoker × Social support 
0.319 
Long COVID × Social support 0.446

1.988 
1.376 
1.562

p-value 
.015* 
.064 
.023*

Note:  Each  interaction  term  tested  in  separate  models  including  all  main  effects  and 
controls from Table 5, *p < .05.

Social support significantly moderates the negative health effects on household savings 
behaviour.  The  significant  interaction  between  poor  health  and  social  support  (OR  = 
1.988,  p  =  .015)  indicates  that  emergency  social  support  substantially  reduces  the 
negative impact of poor health on saving probability. Similarly, social support buffered 
the negative effects of long COVID (OR = 1.562, p = .023). In contrast, financial knowledge 
did  not  significantly  moderate  health-savings  relationships,  suggesting  that  social 
capital—rather than individual knowledge—provides the primary buffer against health-
related financial challenges.

Robustness  checks  using  probit  specifications  and  continuous  savings  measures 
confirmed these patterns. Most importantly, analysis using precautionary saving motives 
as  our  second  dependent  variable  revealed  theoretically  meaningful  mechanistic 
differences. Table 7 compares key findings across both saving measures.

Table 7: Comparison of Key Findings across Saving Measures

Variable

General Saving

OR

p

Precautionary Motives 
p 
OR

0.696 
0.734

Health factors 
Smoker 
Long COVID 
Demographics 
Black households 
Hispanic households 
Single female head 
Financial Knowledge 
High subjective fin. knowledge  1.706

0.988 
0.708 
0.658

.004** 
.019*

.930 
.006** 
.001***

0.893 
1.433

1.575 
1.186 
0.883

.344 
.003**

<.001*** 
.166 
.266

.009**

1.057

.765

72

---

<!-- PAGE 16 -->

Applied Finance Letters, Volume 14, 2025

Variable 
Social Support 
Social support

General Saving

Precautionary Motives

1.316

.004**

0.915

.335

These contrasting patterns reveal different saving pathways: health challenges reduce 
general  saving  capacity  while 
increasing  emergency  awareness,  demographic 
vulnerabilities manifest differently across saving types, and financial confidence affects 
general  saving  more  than  precautionary  concerns.  This  validates  our  dual-measure 
approach  to  capturing  household  savings  behaviour.  Most  notably,  long  COVID 
demonstrates  opposite  effects  across  measures—reducing  general  saving  capacity 
while 
intentions—suggesting  health  challenges 
simultaneously constrain ability while heightening financial vulnerability awareness.

increasing  emergency-focused

3.5. Visual Analysis of Key Relationships

To  illustrate  our  main  findings  about  social  support  moderation  and  demographic 
vulnerabilities,  we  present  visual  representations  of  predicted  probabilities  from  our 
regression models.

Figure 2: Household Structure, Social Support, and Household Savings Behaviour

Figure  2  reveals  a  clear  vulnerability  gradient  across  household  types.  Social  support 
consistently  enhances  saving  probabilities  across  all  groups,  yet  structural 
disadvantages  persist.  Single  female  households  remain  most  financially  vulnerable, 
with  saving  probabilities  approximately  7  percentage  points  lower  than  married 
households even when emergency social support is available (0.55 vs. 0.62).

73

---

<!-- PAGE 17 -->

Applied Finance Letters, Volume 14, 2025

Figure 3: Social Support Moderation of Health Effects

Figure  3  demonstrates  our  key  theoretical  contribution:  social  support  substantially 
buffers  negative  health  effects  on  household  savings  behaviour.  Without  emergency 
support, poor health  reduces saving probability by 12 percentage points (from 0.54 to 
0.42). In contrast, households with social support experience only an 8 percentage point 
decline  (from  0.60  to  0.52).  This  buffering  effect  validates  our  theoretical  framework 
about  social  capital  as  a  protective  factor  against  health-related  financial  challenges, 
directly addressing our third research question about social support moderation.

4. Discussion

This  study  advances  the  Life  Cycle  Hypothesis  by  integrating  dimensions  of  expected 
longevity, financial knowledge, health factors, and social support to explain household 
savings behaviour. Our findings largely confirm the importance of financial knowledge 
while revealing new pathways through which health and social factors shape financial 
outcomes.

Subjective financial knowledge emerged as a stronger predictor of saving than objective 
knowledge,  suggesting  that  financial  confidence  may  be  as  important  as  factual 
knowledge  in  guiding  decisions  (Morris  et  al.,  2022).  This  finding  has  important 
implications  for  financial  education  programs,  which  should  emphasise  confidence-
building alongside knowledge acquisition.

Contrary  to  theoretical  expectations,  expected  longevity  did  not  predict  household 
savings  behaviour.  Instead,  direct  health  factors—smoking,  long  COVID,  and  poor 
health—emerged  as  significant  barriers.  These  results  suggest  that  immediate  health 
limitations influence saving more than abstract life expectancy projections, consistent 
with bounded rationality theories (De Nardi et al., 2010).

A  key  contribution  is  identifying  social  support  as  a  significant  moderator  of  health-

74

---

<!-- PAGE 18 -->

Applied Finance Letters, Volume 14, 2025

savings relationships. While poor health typically reduced saving likelihood, this effect 
was  substantially  attenuated  for  households  with  emergency  social  support.  This 
provides  empirical  support  for  the  buffering  hypothesis  (Cohen  &  Wills,  1985)  and 
highlights the protective role of informal safety nets during health adversity.

Significant  demographic  disparities  emerged,  with  single  female  households  and 
Hispanic  households  showing  persistently  lower  saving  rates  despite  controlling  for 
income  and  education.  These  gaps  suggest  structural  barriers—including  caregiving 
burdens and systemic discrimination—that inhibit saving among vulnerable groups.

5. Conclusion

This study examined how financial knowledge, health factors, and social support interact 
to influence household savings behaviour using data from the 2022 Survey of Consumer 
Finances.  Our  findings  extend  the  Life  Cycle  Hypothesis  by  incorporating  behavioural 
dimensions that better reflect modern saving challenges. Subjective financial knowledge 
significantly increases saving likelihood, while health factors such as smoking and long 
COVID  negatively  impact  savings  behaviour.  A  key  contribution  is  demonstrating  that 
social support significantly moderates the negative effects of health factors on savings 
behaviour, providing crucial buffer effects during health-related financial challenges.

Our findings suggest several policy implications. Financial education initiatives should 
emphasise  confidence-building  and  target  vulnerable  populations  facing  structural 
barriers. The interplay between health and financial well-being suggests opportunities for 
cross-sector collaboration, with health practitioners incorporating financial counselling 
and financial advisors assessing client health. Strengthening social support networks—
both formal and informal—can provide protective effects against financial deterioration 
during health crises.

Limitations and Future Research

Several limitations should be acknowledged. The cross-sectional nature of the SCF data 
limits causal inference; future research should leverage longitudinal designs to examine 
how health and financial knowledge changes influence saving trajectories. Our reliance 
on  brief  financial  knowledge  measures  may  not  capture  multidimensional  knowledge 
complexity  (Gignac  &  Ooi,  2022).  Additionally,  this  U.S.-focused  study  may  limit 
generalizability across different cultural and policy contexts.

Despite  these  limitations,  this  study  advances  understanding  by  demonstrating  how 
financial  knowledge  and  social  resources  can  mitigate  adverse  health  effects  on 
household  savings  behaviour.  The  findings  underscore  the  need  for  interdisciplinary 
interventions  that  address  not  only  knowledge  gaps  but  also  health  inequalities  and 
social capital deficiencies to enhance household financial resilience.

75

---

<!-- PAGE 19 -->

Applied Finance Letters, Volume 14, 2025

References

Adams, S., Bose, N., & Rustichini, A. (2014). How different are smokers? An analysis based on

personal finances. Journal of Economic Behavior & Organization, 107, 40-50. 
https://doi.org/10.1016/j.jebo.2014.08.003

Aizcorbe, A. M., Kennickell, A. B., & Moore, K. B. (2003). Recent changes in US family

finances: Evidence from the 1998 and 2001 Survey of Consumer Finances. Fed. Res. 
Bull., 89, 1.

Allgood, S., & Walstad, W. B. (2016). The effects of perceived and actual financial literacy on

financial behaviors. Economic Inquiry, 54(1), 675-697. https://doi.org/10.1111/ecin.12255

Anderson, A., Baker, F., & Robinson, D. T. (2017). Precautionary savings, retirement planning

and misperceptions of financial literacy. Journal of Financial Economics, 126(2), 383-398. 
https://doi.org/10.1016/j.jfineco.2017.07.008

Ando, A., & Modigliani, F. (1963). The ‘life cycle’ hypothesis of saving: Aggregate  
implications and tests. The American economic review, 53(1), 55-84.

Baumeister, R. F., & Heatherton, T. F. (1996). Self-regulation failure: An overview.

Psychological Inquiry, 7(1), 1–15. https://doi.org/10.1207/s15327965pli0701_1

Behrman, J. R., Mitchell, O. S., Soo, C. K., & Bravo, D. (2012). How financial literacy affects

household wealth accumulation. American Economic Review, 102(3), 300-304. 
https://doi.org/10.1257/aer.102.3.300

Bhatia, R., Hirsch, C., Arnold, A. M., Newman, A. B., & Mukamal, K. J. (2023). Social

networks, social support, and life expectancy in older adults: the Cardiovascular Health 
Study. Archives of Gerontology and Geriatrics, 111, 104981. https://doi.org/10.1016/ 
j.archger.2023.104981

Bickel, W. K., Odum, A. L., & Madden, G. J. (1999). Impulsivity and cigarette smoking: Delay  
discounting in current, never, and ex-smokers. Psychopharmacology, 146(4), 447–454. 
https://doi.org/10.1007/PL00005490

Browning, M., & Lusardi, A. (1996). Household saving: Micro theories and micro facts. Journal

of Economic Literature, 34(4), 1797–1855.

Chen, T. F., Pien, L. C., Fan, C. S., Liang, K. L., & Chiu, Y. W. (2024). Financial strain and

social support as moderators of the relationship between living alone and depressive 
symptoms in older people. BMC Geriatrics, 24(1), 646.https://doi.org/10.1186/s12877-024-
05248-2

Chetty, R., Stepner, M., Abraham, S., et al. (2016). The association between income and life  
expectancy in the United States, 2001–2014. JAMA, 315(16), 1750–1766. https://doi.org/ 
10.1001/jama.2016.4226

76

---

<!-- PAGE 20 -->

Applied Finance Letters, Volume 14, 2025

Cronqvist, H., & Siegel, S. (2015). The origins of savings behavior. Journal of Political

Economy, 123(1), 123-169. https://doi.org/10.1086/679284

Cohen, S., & Wills, T. A. (1985). Stress, social support, and the buffering hypothesis.

Psychological Bulletin, 98(2), 310-357. https://doi.org/10.1037/0033-2909.98.2.310

Cox, D., & Fafchamps, M. (2008). Extended family and kinship networks: Economic insights  
and evolutionary directions. Handbook of Development Economics, 4, 3711-3784. 
https://doi.org/10.1016/S1573-4471(07)04058-2

Czaja, S. J., Moxley, J. H., & Rogers, W. A. (2021). Social support, isolation, loneliness, and

health among older adults in the PRISM randomized controlled trial. Frontiers in Psychology, 
12, 728658.https://doi.org/10.3389/fpsyg.2021.728658

De Nardi, M., French, E., & Jones, J. B. (2010). Why do the elderly save? The role of medical  
expenses. Journal of Political Economy, 118(1), 39-75.https://doi.org/10.1086/651674

Dhakhwa, M., & Babiarz, P. (2019). Does family support network influence the perceived need

for emergency savings. Consumer Interests Annual, 65, 1-12.

Federal Reserve Board. (2023). Economic well-being of U.S. households in 2022. Board of

Governors of the Federal Reserve System. https://www.federalreserve.gov/publications/ 
2023-economic-well-being-of-us-households-in-2022.htm

Fisher, P. J., & Anong, S. T. (2012). Relationship of saving motives to saving habits. Journal of

Financial Counseling and Planning, 23(1), 63-79.

FINRA Investor Education Foundation. (2025). The state of U.S. financial capability: The 2024  
National Financial Capability Study. https://www.finra.org/media\center/newsreleases/ 
2025/finra-foundation-releases-sixth-wave-national-financial-capability

Gignac, G. E., & Ooi, E. (2022). Measurement error in research on financial literacy: How much

error is there and how does it influence effect size estimates? Journal of Consumer 
Affairs, 56(2), 938-956. https://doi.org/10.1111/joca.12417

Gladstone, J. J., & Hundtofte, C. S. (2023). A lack of financial planning predicts increased

mortality risk: Evidence from cohort studies in the United Kingdom and United States. Plos 
one, 18(9), e0290506.https://doi.org/10.1371/journal.pone.0290506

Glei, D. A., Lee, C., & Weinstein, M. (2022). Assessment of mortality disparities by wealth  
relative to other measures of socioeconomic status among US adults. JAMA network 
open, 5(4), e226547-e226547. http://doi.org/10.1001/jamanetworkopen.2022.6547

Goyal, K., & Kumar, S. (2021). Financial literacy: A systematic review and bibliometric

analysis. International Journal of Consumer Studies, 45(1), 80-105. https://doi.org/ 
10.1111/ijcs.12605

77

---

<!-- PAGE 21 -->

Applied Finance Letters, Volume 14, 2025

Hamermesh, D. S. (1985). Expectations, life expectancy, and economic behavior. The Quarterly

Journal of Economics, 100(2), 389-408.

Hastings, J. S., Madrian, B. C., & Skimmyhorn, W. L. (2013). Financial literacy, financial  
education, and economic outcomes. Annual Review of Economics, 5(1), 347-373. 
https://doi.org/10.1146/annurev-economics-082312-125807

Hogarth, J. M., & Anguelov, C. E. (2003). Can consumers be taught to be rational? The case of

saving behavior. Journal of Consumer Affairs, 37(1), 117-137.

Hurd, M. D., & McGarry, K. (1995). Evaluation of the subjective probabilities of survival in the

health and retirement study. Journal of Human Resources, 30, S268-S292. 
https://doi.org/10.2307/146285

Kennickell, A. B. (1995). Saving and permanent income: Evidence from the 1992 SCF. Division

of Research and Statistics, Division of Monetary Affairs, Federal Reserve Board.

Khan, M. S. R., Putthinun, P., Watanapongvanich, S., Yuktadatta, P., Uddin, M. A., & Kadoya,  
Y. (2021). Do financial literacy and financial education influence smoking behavior in the 
United States? International Journal of Environmental Research and Public Health, 18(5), 
2579-2604. https://doi.org/10.3390/ijerph18052579

Lal, S., Nguyen, T. X. T., Sulemana, A. S., Khan, M. S. R., & Kadoya, Y. (2022). Does financial  
literacy influence preventive health check-up behavior in Japan? a cross-sectional 
study. BMC Public Health, 22(1), 1704-1805. https://doi.org/10.1186/s12889-022-14079-8

Lindamood, S., Hanna, S. D., & Bi, L. (2007). Using the Survey of Consumer Finances: Some  
methodological considerations and issues. Journal of Consumer Affairs, 41(2), 195-222.

Lusardi, A., & Mitchell, O. S. (2011). Financial literacy around the world: An overview. Journal

of Pension Economics & Finance, 10(4), 497-508. 
https://doi.org/10.1017/S1474747211000448

Lusardi, A., & Mitchell, O. S. (2014). The economic importance of financial literacy: Theory

and evidence. Journal of Economic Literature, 52(1), 5–44. https://doi.org/10.1257/jel.52.1.5

Mani, A., Mullainathan, S., Shafir, E., & Zhao, J. (2013). Poverty impedes cognitive function.

Science, 341(6149), 976-980. https://doi.org/10.1126/science.1238041

Meier, S., & Sprenger, C. D. (2010). Present-biased preferences and credit card borrowing.

American Economic Journal: Applied Economics, 2(1), 193–210. 
https://doi.org/10.1257/app.2.1.193

Modigliani, F., & Brumberg, R. (1954). Utility analysis and the consumption function: An

interpretation of cross-section data. In K. K. Kurihara (Ed.), Post-Keynesian economics (pp. 
388-436). Rutgers University Press.

78

---

<!-- PAGE 22 -->

Applied Finance Letters, Volume 14, 2025

Montalto, C. P., & Yuh, Y. (1998). Estimating nonlinear models with multiply imputed data.

Financial counseling and Planning, 9(1), 97-101. https://ssrn.com/abstract=132596

Morris, T., Maillet, S., & Koffi, V. (2022). Financial knowledge, financial confidence and

learning capacity on financial behavior: a Canadian study. Cogent Social Sciences, 8(1), 
1996919. https://doi.org/10.1080/23311886.2021.1996919

Nielsen, R. B., & Seay, M. C. (2014). Complex samples and regression‐based inference:

Considerations for consumer researchers.  Journal of Consumer Affairs, 48(3), 603-619. 
https://doi.org/10.1111/joca.12038

Ouyang, C., Joseph, M., Zhang, Y., & Naveed, K. (2025). The interplay of financial safety nets,

long-term goals, and saving habits: A moderated mediation study. International Journal of 
Financial Studies, 13(1), 47. https://doi.org/10.3390/ijfs13010047

Post, T., & Hanewald, K. (2013). Longevity risk, subjective survival expectations, and individual

saving behavior. Journal of Economic Behavior & Organization, 86, 200-220.

Rha, J. Y., Montalto, C. P., & Hanna, S. D. (2006). The effect of self-control mechanisms on  
household saving behavior. Journal of Financial Counseling and Planning, 17(2).

Shin, S. H., & Hanna, S. D. (2017). Accounting for complex sample designs in analyses of the

Survey of Consumer Finances. Journal of Consumer Affairs, 51(2), 433-447.

Smith, J. P. (1999). Healthy bodies and thick wallets: the dual relation between health and

economic status. Journal of Economic Perspectives, 13(2), 145-166.    
https://doi.org/10.1257/jep.13.2.145

Stewart, C. C., Yu, L., Lamar, M., Wilson, R. S., Bennett, D. A., & Boyle, P. A. (2020).

Associations of health and financial literacy with mortality in advanced age. Ageing clinical 
and experimental research, 32(5), 951-957.  
https://doi.org/10.1007/s40520-019-01259-7

Xu, J., Murphy, M., & Akin, H. (2020). Financial literacy and preventive health behavior:

Evidence from the 2017 U.S. National Financial Capability Study. Health Education & 
Behavior, 47(6), 812–818. https://doi.org/10.1177/1090198120929923

Yuh, Y., & Hanna, S. D. (2010). Which households think they save? Journal of Consumer

Affairs, 44(1), 70-97. https://doi.org/10.1111/j.1745-6606.2010.01158.x

79

<!-- MARKITDOWN CONVERSION -->

<!-- The following is the full MarkItDown conversion for formatting fidelity. -->

Applied Finance Letters, Volume 14, 2025
Financial Knowledge, Health Factors, and Social Support:
Determinants of Household Savings Behaviour in the U.S.
Lena Gan Author affiliation
Kansas State University
Sara Kay Author affiliation
Carnegie Mellon University
This study examines how financial knowledge, health factors, and social support
influence household savings behaviour using data from the 2022 Survey of
Consumer Finances. We employ binary logistic regression and interaction
analysis to analyse two savings measures: general savings behaviour and
precautionary savings motives. Our findings reveal that subjective financial
knowledge significantly increases saving likelihood, while health factors such as
smoking and long COVID negatively impact savings behaviour. A key contribution
is demonstrating that social support significantly moderates the negative effects
of health factors on savings behaviour, providing a crucial buffer during health-
related financial challenges. The analysis also reveals significant demographic
disparities, with Hispanic households and single female-headed households
exhibiting lower savings rates. Notably, health challenges simultaneously
constrain general saving capacity while heightening precautionary savings
awareness, suggesting different pathways for savings behaviour. These findings
extend the Life Cycle Hypothesis by integrating behavioural dimensions into
household savings decisions and highlight the need for targeted interventions that
address health inequalities while strengthening social support networks.
Keywords: household savings, financial knowledge, health factors, social support,
life cycle hypothesis
1. Introduction
A central question in household finance research is how individuals allocate income
between current consumption and savings for future needs (Browning & Lusardi, 1996).
Despite its crucial role in financial security and retirement preparedness, many U.S.
households continue to struggle with saving. Nearly half of those nearing retirement
report insufficient savings (U.S. Federal Reserve, 2023), and recent data from the 2025
National Financial Capability Survey (NFCS) show that nearly 40% of middle-income
households are financially fragile, unable to cover basic expenses or weather
58

Applied Finance Letters, Volume 14, 2025
unexpected shocks (FINRA, 2025). This erosion of financial stability underscores the
need to better understand the behavioural and structural factors that shape household
savings behaviour.
The Life Cycle Hypothesis (LCH) offers a foundational framework, positing that
individuals smooth consumption over time based on expected lifetime income and
longevity (Ando & Modigliani, 1963). However, actual household savings behaviour often
diverges from this model’s predictions. Subjective life expectancy and health
perceptions—rather than actuarial longevity alone—appear to drive saving decisions
(Bloom et al., 2006; Post & Hanewald, 2012). Poor health can also reduce future
orientation and increase present bias, especially under uncertainty (Smith, 1999;
Cronqvist & Siegel, 2013).
A growing literature suggests that financial knowledge plays a dual role: it enhances
financial capability and indirectly shapes health behaviours. Financially literate
individuals tend to exhibit lower time preference, stronger planning skills, and greater
self-control—traits linked to both saving and healthy lifestyle choices (Meier & Sprenger,
2010; Lusardi & Mitchell, 2014; Lal et al., 2022). For example, higher financial knowledge
is associated with a lower probability of smoking (Khan et al., 2021), more engagement
in preventive care (Xu et al., 2020), and better long-term financial outcomes. These traits
contribute to longer life expectancy, a link supported by growing longitudinal evidence.
For instance, lower financial knowledge has been shown to directly and independently
predict mortality risk in older adults, independent of socioeconomic status and health
(Gladstone & Hundtofte, 2023; Stewart et al., 2020). Furthermore, the accumulation of
wealth—a key outcome of financial capability—is one of the strongest socioeconomic
predictors of survival, underscoring the importance of the wealth-based channel (Chetty
et al., 2016; Glei et al., 2022). These cognitive and behavioural traits not only promote
healthier decisions but also contribute to long-term wealth accumulation—a known
determinant of longevity through better access to healthcare, safer environments, and
resilience to shocks (Chetty et al., 2016).
Social support networks buffer negative financial effects of poor health (Chen et al.,
2024; Gertler & Gruber, 2002) by providing informal insurance—reducing perceived
saving needs by 24% (Dhakhwa & Barbiarz, 2019), providing emotional support (Bhatia et
al., 2023; Czaja et al., 2021) and partially smoothing consumption in health crises
(Gertler & Gruber, 2002). While these findings confirm the mitigating role of social
support, its effectiveness may vary depending on the severity of health conditions and
the reliability of support networks (Chen et al., 2024; Dhakhwa & Barbiarz, 2019; Bhatia
et al., 2023; Gertler & Gruber, 2002).
While the LCH provides a valuable foundation for understanding saving decisions, its
original formulation does not account for individual-level cognitive and behavioural
factors such as financial knowledge, subjective health assessments, or health-related
59

Applied Finance Letters, Volume 14, 2025
decision-making. Instead, it focuses on income, age, and actuarial life expectancy as
objective drivers of consumption smoothing (Modigliani & Brumberg, 1954; Ando &
Modigliani, 1963). As such, key variables that shape modern household saving—
especially those involving health shocks, health perceptions, and financial capability—
remain theoretically peripheral or absent in standard LCH models.
This study extends the LCH by incorporating behavioural and cognitive dimensions—
specifically financial knowledge, subjective and objective health, and informal social
support—to better reflect the complexity of household savings behaviour. Using data
from the 2022 Survey of Consumer Finances (SCF), we investigate three research
questions:
1. How do subjective and objective health factors affect savings behaviour?
2. Does financial knowledge moderate the relationship between health status and
saving?
3. To what extent does social support moderate the relationship between health factors
and household savings behaviour?
Our findings contribute to a more holistic understanding of household savings behaviour
by highlighting the interactive roles of financial knowledge, health resilience, and social
context.
2. Data and Methods
2.1. Data
The study used a dataset from the 2022 Survey of Consumer Finances (SCF), a triennial
survey conducted by the Board of Governors of the Federal Reserve System. The SCF
provides detailed and nationally representative data on the financial characteristics of
U.S. households, including assets, liabilities, income and financial decision-making
(Bhutta et al., 2020). While the SCF is conducted every three years, the 2022 wave was
selected specifically because it contains unique post-pandemic variables—such as long
COVID, health disruptions, and pandemic-era saving motivations—that are essential to
the present study’s examination of the relationship between health factors, financial
knowledge, and household savings behaviour. These features allow us to evaluate
financial resilience in the context of systemic health uncertainty and capture behavioural
responses not observable in pre-pandemic waves such as 2019 and earlier waves.
To measure household savings behaviour, we employed two complementary indicators:
a general saving flow measure and a precautionary saving motive measure. First,
following Kennickell (1995), we used the SCF question asking whether household
spending was “less than,” “equal to,” or “more than” income in the previous year.
Respondents who reported spending less than income were classified as savers,
60

Applied Finance Letters, Volume 14, 2025
capturing a behavioural proxy for net positive saving flow. This simple indicator, though
not a measure of accumulated assets or net worth, has been widely used and validated
in past studies as a robust estimate of household savings behaviour across income
groups and demographic categories (Hogarth & Anguelov, 2003; Rha et al., 2006; Hanna
& Lindamood, 2010; Yuh & Hanna, 2010).
Second, to better align with our theoretical interest in health-driven household savings
behaviour, we constructed a precautionary savings variable. This binary measure
captures whether households reported saving for emergencies, unemployment, or
medical expenses—motivations that became especially salient during the COVID-19
pandemic. Following the approach of Fisher and Anong (2012), households were coded
as having a precautionary savings motive if any of the SCF’s saving reason codes
included unemployment reserves, illness/medical expenses, or emergencies. This
secondary measure enables us to distinguish risk-buffering savings motives from other
saving goals such as wealth preservation or lifestyle maintenance or future aspirations.
The SCF uses a complex dual-frame sampling system, combining an area-probability
sample with a list sample that oversamples high-wealth households, thereby capturing
the full distribution of U.S. household finances (Bhutta et al., 2023). To address missing
data, the SCF provides five implicates generated through multiple imputation, allowing
for population-level estimation and variance adjustment (Aizcorbe et al., 2003). The 2022
SCF dataset includes 4,595 households, when appropriately weighted, is representative
of 133.6 million U.S. households.
2.2. Variable Definitions
Dependent Variable. Two dependent variables were used to capture different aspects
of household savings behaviour. First, a binary indicator of net savings behaviour was
created based on responses to whether household spending was less than income (1 =
saver, 0 = non-saver). This flow-based indicator captures behavioural intent to consume
less than earned income over the past year. Second, precautionary saving was
operationalised as a binary variable indicating whether the household cited emergency,
health, or unemployment-related motives for saving—allowing us to assess targeted
financial preparation in response to health risk and uncertainty.
Independent Variables. Table 1 provides detailed definitions, measurement
specifications, and SCF variable codes for all variables used in our analysis.
Table 1: Variable Definitions and Measurement
SCF
Variable Definition Measurement Variable
Code
61

Applied Finance Letters, Volume 14, 2025
Dependent
|     |     |     |     |
| --- | --- | --- | --- |
Variables
Whether household
spent less than
| Saver  |     | Binary (1=Yes, 0=No)  | X7510  |
| ------ | --- | --------------------- | ------ |
income in the past
year
Whether household  Binary (1=Has precautionary motive, 0=No  X3006,
reported saving for  precautionary motive). Coded as 1 if any of  X3007,
Precautionary  emergencies,  the six saving motive variables contained  X7513,
Saving Motive  unemployment, or  codes 23 (unemployment reserves), 24  X7514,
medical expenses as  (illness/medical expenses), or 25  X7515,
primary motivations  (emergencies/rainy days/security)  X6848
Independent
|     |     |     |     |
| --- | --- | --- | --- |
Variables

| Expected   | Respondent’s self-     |                     |        |
| ---------- | ---------------------- | ------------------- | ------ |
|            |                        | Continuous (years)  | X7381  |
| longevity  | reported expected age  |                     |        |
at death
| Objective  |     |     | X7558,  |
| ---------- | --- | --- | ------- |
financial  “Big Three” financial  Composite score (0-3)   X7559,
| knowledge   | knowledge questions   |                                              | X7560  |
| ----------- | --------------------- | -------------------------------------------- | ------ |
| Subjective  |                       | Categorical based on 0-10 scale: Low (0-3),  |        |
Self-assessment of
| financial  |     | Medium   | X7556  |
| ---------- | --- | -------- | ------ |
financial knowledge
| knowledge  |     | (4-6), High (7-10)  |     |
| ---------- | --- | ------------------- | --- |
Self-reported health
Health status  Categorical (Excellent/Good/Fair/Poor)  X6030
condition
Current smoking
| Smoker  |     | Binary (1=Yes, 0=No)  | X7380  |
| ------- | --- | --------------------- | ------ |
status
Whether household
Health
|     | has health insurance  | Binary (1=Yes, 0=No)  | X6341  |
| --- | --------------------- | --------------------- | ------ |
insurance
coverage
| Parental  | Whether respondent’s  |     | X6026,  |
| --------- | --------------------- | --- | ------- |
Binary (1=Yes, 0=No)
| mortality  | parent(s) are still alive  |     | X6028  |
| ---------- | -------------------------- | --- | ------ |
Whether respondent
COVID
|     | was diagnosed with  | Binary (1=Yes, 0=No)  | X19046  |
| --- | ------------------- | --------------------- | ------- |
diagnosis
COVID-19
Whether respondent
| Long COVID  | experienced long  | Binary (1=Yes, 0=No)  | X19048  |
| ----------- | ----------------- | --------------------- | ------- |
COVID symptoms
Whether household
could get $3,000 from
| Social support  |     | Binary (1=Yes, 0=No)  | X6443  |
| --------------- | --- | --------------------- | ------ |
friends/family in
emergency
Sociodemogra
|     |     |     |     |
| --- | --- | --- | --- |
phic Variables
| Gender/Marital  |     | Categorical (Married/Partner/Single  | X8021,  |
| --------------- | --- | ------------------------------------ | ------- |
Household structure
| status  |     | Female/Single Male)  | X8023  |
| ------- | --- | -------------------- | ------ |

62

Applied Finance Letters, Volume 14, 2025
|            | Racial/ethnic        | Categorical (White/Black/Hispanic/Asian  |        |
| ---------- | -------------------- | ---------------------------------------- | ------ |
| Race       |                      |                                          | X6809  |
|            | background           | Other)                                   |        |
|            | Highest level of     | Categorical (No HS/HS/Some               |        |
| Education  |                      |                                          | X5931  |
|            | education completed  | College/College/Graduate)                |        |
Respondent’s age in
| Age  |     | Continuous  | X14  |
| ---- | --- | ----------- | ---- |
years
Annual household
| Income  |     | Continuous (log-transformed)  | X5729  |
| ------- | --- | ----------------------------- | ------ |
income
Inverse hyperbolic sine
IHS net worth  transformation of  Continuous (IHS transformed)  Networth
household net worth
Whether household
Home
|     | owns primary  | Binary (1=Yes, 0=No)  | X508  |
| --- | ------------- | --------------------- | ----- |
ownership
residence
| Number of   | Number of children in  |                         |        |
| ----------- | ---------------------- | ----------------------- | ------ |
|             |                        | Categorical (0/1-3/4+)  | X6903  |
| children    | household              |                         |        |
| Employment  | Current employment     | Categorical             |        |
X4511
| status  | situation  | (Employed/Retired/Unemployed/Disabled)  |     |
| ------- | ---------- | --------------------------------------- | --- |
Expected change in
Income
|     | income relative to  | Categorical (Higher/Same/Lower)  | X7364  |
| --- | ------------------- | -------------------------------- | ------ |
expectations
inflation
Source: 2022 Survey of Consumer Finances

2.3. Descriptive Statistics
Table 2 presents descriptive statistics for the sample. As shown, 62% of households
(weighted) reported saving (spending less than income) vs. 38% of non-savers, while 40%
had precautionary savings motives vs 60% without. Married households comprised 46%
of respondents, with single females representing 26% and single males 18%. Race
distribution showed White respondents made up 68% of the sample, Black respondents
15%,  Hispanic  respondents  12%,  and  Asian/Other  respondents  5%.  Educational
attainment  varied,  with  22%  having  a  bachelor’s  degree  and  17%  having  graduate
degrees. Notably, 65% of respondents were homeowners, and 17% were smokers.
Regarding subjective financial knowledge, 74% reported high knowledge levels, 21%
medium, and 5% low levels.

Table 2: Sample Characteristics (N=4,595)

| Variable             | Weighted %  |     |     |
| -------------------- | ----------- | --- | --- |
| Saver                |             |     |     |
| Yes                  | 62          |     |     |
| No                   | 38          |     |     |
| Precautionary Saver  |             |     |     |
| Yes                  | 40          |     |     |
| No                   | 60          |     |     |

63

Applied Finance Letters, Volume 14, 2025
Yes 40
No 60
Gender/Marital Status
Married 46
With partner 10
Single Female 26
Single Male 18
Race
White 68
Black 15
Hispanic 12
Asian/Other 5
Employment
Employed 65
Unemployed 23
Retired 5
Disabled 7
Education
Less than High school 9
High School 22
Some College 30
Bachelor’s 22
Graduate 17
Home Ownership 65
Number of Kids
0 61
1-3 36
4 or more 3
Health Factors
Respondent is a smoker 17
Have Health Insurance
86
coverage
Respondent’s parent(s) still
62
alive
COVID diagnosed 42
Long COVID 15
Respondent’s health status
Excellent 24
Good 50
Fair 22
Poor 4
Subjective Financial
Knowledge
Low 5
Medium 21
High 74
Emergency Social Support 66
Source: 2022 Survey of Consumer Finances
64

Applied Finance Letters, Volume 14, 2025
Table 3 shows the distribution of continuous variables in the sample. The mean age of
respondents was 51.3 years (weighted). The mean expected longevity was 85.1 years.
Mean household income was $106,251, and mean net worth was $746,821.
Table 3: Descriptive Statistics for Continuous Variables (N=4,595)
Variable Mean Median SD
Respondent’s Age 51.3 51 17.4
Expected longevity 85.1 85 11.32
Income $106,251 $59,050 $58,986
Net worth $746,821 $121,760 $612,721
Objective financial knowledge (0-3) 2.1 2 0.8
Source: 2022 Survey of Consumer Finances
2.4. Conceptual and Empirical Framework
Conceptual Framework. Figure 1 presents a behavioural extension of the Life Cycle
Hypothesis (LCH), integrating financial knowledge, health factors, and social support
into saving models traditionally centred on income, age, and actuarial life expectancy
(Modigliani & Brumberg, 1954). These behavioural inputs help explain systematic
deviations from rational saving predicted by standard models.
Health perceptions and vulnerability shape savings decisions more than objective
measures alone (Hamermesh, 1985; Hurd & McGarry, 1995). Financial knowledge
contributes to these perceptions and their behavioural consequences through improved
self-regulation, long-term planning, and future-oriented behaviours (Meier & Sprenger,
2010; Lusardi & Mitchell, 2014). Empirical studies confirm that higher financial
knowledge is linked to lower smoking prevalence (Khan et al., 2021), greater engagement
in preventive health actions (Xu et al., 2020), and improved executive function
(Baumeister & Heatherton, 1996). These cognitive traits—especially self-control and
delayed discounting—bridge financial and health domains. Smokers tend to exhibit
higher discount rates and lower cognitive performance (Bickel et al., 1999; Adams et al.,
2014), traits inversely associated with financial knowledge. These behaviours
cumulatively influence wealth accumulation and health trajectories, affecting both
perceived and actual life expectancy (Chetty et al., 2016).
Social support provides a crucial but underexplored buffer against health-related
financial challenges. Social networks serve as informal safety nets, providing resources
during crises and reducing financial stress (Cox & Fafchamps, 2008). They buffer the
adverse effects of poor health on household savings behaviour by alleviating emotional
and economic burdens (Mani et al., 2013). Our framework posits that social support
moderates the relationship between health factors and household savings behaviour,
65

Applied Finance Letters, Volume 14, 2025
representing a key theoretical contribution.
By jointly examining these behavioural mechanisms, this study offers a more complete
account of household savings behaviour than classical LCH formulations allow.
Figure 1: Conceptual Framework of the Extended Model
Empirical Specifications. A binary logistic regression model was employed to analyse
the probability of a household savings (spending less than income) versus not saving
(spending equal to or more than income). The model can be expressed as:
log[P(Y=1)/P(Y=0)]=β0+β1X1+β2X2+...+βkXk+ϵ
Where:
• P(Y=1) is the probability of saving (spending less than income)
• P(Y=0) is the probability of not saving (spending equal to or more than income)
• β0 is the intercept
• β1...βk are the regression coefficients
• X1...Xk are the independent variables
66

Applied Finance Letters, Volume 14, 2025
• ϵ is the error term
The odds ratio (OR) for each independent variable was calculated as: OR=exp(β)
Where a value greater than 1 indicates that the variable increases the odds of saving, and
a value less than 1 indicates that the variable decreases the odds of saving.
2.5. Measurement of Key Variables
Financial Knowledge Measurement. Financial knowledge was assessed using both
objective and subjective indicators drawn from the SCF. Objective financial knowledge
was measured using the Big Three financial knowledge questions, which assess
understanding of (1) compound interest, (2) inflation and real returns, and (3) risk
diversification. These questions were first developed for the 2004 Health and Retirement
Study (HRS) and have since become widely adopted in large-scale surveys such as the
National Financial Capability Study (NFCS), the Survey of Household Economics and
Decision making (SHED), and the Survey of Consumer Finances (SCF). Specifically,
respondents were asked:
1. Interest rate: “Suppose you had $100 in a savings account and the interest rate was
2% per year. After 5 years, how much do you think you would have in the account if
you left the money to grow?”
2. Inflation question: “Imagine that the interest rate on your savings account was 1% per
year and inflation was 2% per year. After 1 year, how much would you be able to buy
with the money in this account?”
3. Risk diversification: “Do you think that the following statement is true or false?”
‘Buying a single company stock usually provides a safer return than a stock mutual
fund.’
Each response was coded as correct or incorrect and summed, resulting in a composite
score ranging from 0 to 3. This three-item scale has been used in numerous peer-
reviewed studies to capture essential financial decision-making competencies (Hastings
et al., 2013; Lusardi & Mitchell, 2014). However, its brevity may constrain its construct
validity as noted by Gignac and Ooi (2022) due to the number of questions. This limitation
reflects the constraints of the SCF instrument rather than study design. Nonetheless, the
Big Three are considered a validated minimal benchmark for international financial
knowledge assessment and remain suitable for national comparisons (Anderson et al.,
2017; Behrman et al., 2012; Goyal & Kumar, 2021; Hastings et al., 2013; Lusardi &
Mitchell, 2011; 2014).
Subjective financial knowledge was measured using a self-assessment question where
respondents rated their overall financial knowledge on a scale from 0 (not at all
67

Applied Finance Letters, Volume 14, 2025
knowledgeable) to 10 (very knowledgeable). Following previous research (Allgood &
Walstad, 2016), we categorised these responses into three levels: Low (0-3), Medium (4-
6), and High (7-10). This categorical approach captures meaningful differences in
financial confidence levels, with 77% of respondents reporting high knowledge levels in
our sample.
Health and Social Support Measures. Health was measured using multiple indicators:
• Self-reported health status (Excellent/Good/Fair/Poor)
• Smoking status (Yes/No)
• COVID-19 diagnosis (Yes/No)
• Long COVID symptoms (Yes/No)
Following the study by Ouyang et al. (2025), social support was measured using the
question about whether the respondent could obtain $3,000 from friends or family in an
emergency (Yes/No). This measure captures the availability of informal financial safety
nets that can serve as a temporary financial buffer that might influence saving decisions,
particularly during health-related financial emergencies.
2.6. Interaction Models and Data Analysis
Interaction Models. To examine the joint effects of financial knowledge, health factors,
and social support on household savings behaviour, we estimated several interaction
models. Our primary interaction model can be expressed as:
log[P(Y=1)/P(Y=0)]=β0+β1(Health)+β2(FinKnowledge)+β3(SocialSupport)+β4
(Health×FinKnowledge)+β5(Health×SocialSupport)+βkXk+ϵ
Where Health represents various health factors (self-reported health status, smoking,
etc.), Fin Knowledge represents our measures of financial knowledge (both objective and
subjective), and Social Support represents our measure of emergency support
availability. These interaction terms allow us to test whether:
1. The effect of health factors on household savings behaviour varies by financial
knowledge level
2. Social support moderates the relationship between health factors and household
savings behaviour
Data Analysis Plan. We assessed multicollinearity using Pearsons correlation and
Variance Inflation Factors (VIF). Cross-tabulation for two saving measures (χ² = 2.49, p =
0.115) confirms they capture distinct but related dimensions, with 39.8% of non-savers
reporting precautionary motives and 38.9% of savers lacking precautionary motivations,
68

Applied Finance Letters, Volume 14, 2025
validating our dual-measure approach.
Given  the  SCF’s  complex  sampling  design  and  multiple  imputation,  we  applied
‘repeated-imputation inference’ (RII) techniques with replicate weights to bootstrap the
standard errors, following established practices for nonlinear models with multiple
imputed survey (Lindamood et al., 2007; Montalto & Yuh, 1998; Nielsen & Seay, 2014;
Shin & Hanna, 2017). All analyses used Stata MP18 with appropriate survey weights.

3. Results and Discussion
3.1. Multicollinearity Assessment
Our multicollinearity diagnostics indicated no severe multicollinearity issues among the
predictors in our logistic regression model. The mean VIF was 2.40, well below the
conventional  threshold  of  concern  of  10.  Pearson’s  correlation  analysis  showed
expected associations between related variables. The highest correlations occurred
between age and household expected remaining life (r=−0.80), which is expected given
their conceptual relationship. The moderate correlation between income and wealth
(r=0.41)  is  also  consistent  with  financial  theory.  Table  4  presents  key  correlation
coefficients among selected variables.
Subj
|     |         |        |      |         | Fin    |       |         |      |        |       |         | COVID   |        |
| --- | ------- | ------ | ---- | ------- | ------ | ----- | ------- | ---- | ------ | ----- | ------- | ------- | ------ |
|     | Log     | Net    |      | Poor    |        | Fin   |         | Soc  |        | Hispa | Expect  |         | Long   |
|     |         |        | Age  |         | Know   |       | Smoker  |      | Black  |       |         | Diagnos |        |
|     | Income  | Worth  |      | Health  |        | Know  |         | Sup  |        | nic   | Longev  |         | COVID  |
|     |         |        |      |         | (Obj)  |       |         |      |        |       |         | d       |        |
(High)
|                      |         |         |         |        |     |     |     |     |     |     |     |     |     |
| -------------------- | ------- | ------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Log Income           | 1.000   |         |         |        |     |     |     |     |     |     |     |     |     |
|                      |         |         |         |        |     |     |     |     |     |     |     |     |     |
| Net Worth            | 0.366*  | 1.000   |         |        |     |     |     |     |     |     |     |     |     |
|                      |         |         |         |        |     |     |     |     |     |     |     |     |     |
| Age                  | 0.172*  | 0.175*  | 1.000   |        |     |     |     |     |     |     |     |     |     |
|                      |         | -       |         |        |     |     |     |     |     |     |     |     |     |
| Poor Health -0.121*  |         |         | 0.084*  | 1.000  |     |     |     |     |     |     |     |     |     |
0.036*
Fin
|            |         |         |         | -   |        |     |     |     |     |     |     |     |     |
| ---------- | ------- | ------- | ------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| Knowledge  | 0.278*  | 0.088*  | 0.093*  |     | 1.000  |     |     |     |     |     |     |     |     |
0.087*
(Obj)
Subj Fin
|            |         |         |         | -   |         |        |     |     |     |     |     |     |     |
| ---------- | ------- | ------- | ------- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| Knowledge  | 0.265*  | 0.118*  | 0.243*  |     | 0.184*  | 1.000  |     |     |     |     |     |     |     |
0.046*
(High)
|         |          | -       | -       |         |          | -       |        |     |     |     |     |     |     |
| ------- | -------- | ------- | ------- | ------- | -------- | ------- | ------ | --- | --- | --- | --- | --- | --- |
| Smoker  | -0.178*  |         |         | 0.080*  | -0.149*  |         | 1.000  |     |     |     |     |     |     |
|         |          | 0.057*  | 0.108*  |         |          | 0.116*  |        |     |     |     |     |     |     |
| Social  |          |         |         | -       |          |         |        |     |     |     |     |     |     |
0.263*  0.099*  0.073*  0.206*  0.123*  -0.147*  1.000
| Support    |          |         |         | 0.081*  |          |         |         |                |         |         |        |     |     |
| ---------- | -------- | ------- | ------- | ------- | -------- | ------- | ------- | -------------- | ------- | ------- | ------ | --- | --- |
|            |          | -       | -       |         |          | -       |         | -              |         |         |        |     |     |
| Black      | -0.216*  |         |         | 0.041*  | -0.197*  |         | 0.117*  |                | 1.000   |         |        |     |     |
|            |          | 0.075*  | 0.102*  |         |          | 0.101*  |         | 0.240*         |         |         |        |     |     |
|            |          | -       | -       |         |          | -       |         | -              | -       |         |        |     |     |
| Hispanic   | -0.150*  |         |         | 0.012   | -0.150*  |         | -0.007  |                |         | 1.000   |        |     |     |
|            |          | 0.072*  | 0.175*  |         |          | 0.134*  |         | 0.157* 0.188*  |         |         |        |     |     |
| Expected   |          | -       | -       | -       |          | -       |         |                |         |         |        |     |     |
|            | -0.050*  |         |         |         | -0.015   |         | -0.003  | -0.018         | 0.120*  | 0.119*  | 1.000  |     |     |
| Longevity  |          | 0.102*  | 0.802*  | 0.160*  |          | 0.121*  |         |                |         |         |        |     |     |
| COVID      |          |         | -       |         |          |         |         |                | -       |         |        |     |     |
0.147*  0.062*  -0.014  0.083*  0.018  -0.086*  0.080*  0.059*  0.168*  1.000
| Diagnosed  |     |     | 0.163*  |     |     |     |     |     | 0.101*  |     |     |     |     |
| ---------- | --- | --- | ------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
|            |     |     | -       |     |     | -   |     | -   |         |     |     |     |     |
Long COVID -0.085*  -0.023  0.052*  -0.055*  0.029  0.019  0.126*  0.075*  0.395*  1.000
|     |     |     | 0.132*  |     |     | 0.078*  |     | 0.090*  |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- |

69

Applied Finance Letters, Volume 14, 2025
Note: * indicates significance at p < 0.05 level. Highest correlation between age and
expected longevity (r = -0.802) reflects conceptual relationship.
The  binary  logistic  regression  model  examining  factors  associated  with  household
savings behaviour demonstrated adequate fit with a McFadden pseudo-R² of .16 and a c-
statistic of .77, indicating good discriminatory power. Table 5 summarises the results of
the logistic regression model predicting the likelihood of being a saver.
3.2. Logistic Regression Results
The  binary  logistic  regression  model  examining  factors  associated  with  household
savings behaviour demonstrated adequate fit with a McFadden pseudo-R² of .16 and a c-
statistic of .77, indicating good discriminatory power. Table 5 summarises the results of
the logistic regression model predicting the likelihood of being a saver.

Table 5: Logistic Regression Results Predicting Household Savings Behaviour
| Variable  | Coeff  | SE  OR  | 95% CI   | p   |
| --------- | ------ | ------- | -------- | --- |
|           |        |         |          |     |
Socioeconomic factors
| Log income  | 0.231  | 0.084  1.260  | [1.069, 1.484]  | .006**  |
| ----------- | ------ | ------------- | --------------- | ------- |
IHS net worth  0.033  0.008  1.034  [1.018, 1.050]  <.001***
| Demographic characteristics  |         |               |                 |         |
| ---------------------------- | ------- | ------------- | --------------- | ------- |
| Age                          | -0.001  | 0.006  0.999  | [0.988, 1.011]  | .898    |
| Black                        | -0.012  | 0.132  0.988  | [0.762, 1.281]  | .930    |
| Hispanic                     | -0.346  | 0.127  0.708  | [0.552, 0.908]  | .006**  |
| Other race                   | -0.131  | 0.177  0.877  | [0.620, 1.241]  | .460    |
|                              |         |               |                 |         |
Household structure
Single male head  -0.104  0.119  0.901  [0.714, 1.137]  .381
Single female head  -0.419  0.127  0.658  [0.513, 0.844]  .001***
Children in household  -0.245  0.115  0.783  [0.624, 0.981]  .033*
|     |     |     |     |     |
| --- | --- | --- | --- | --- |
Education level
High school graduate  0.353  0.171  1.423  [1.018, 1.989]  .039*
| Some college  | 0.244  | 0.174  1.276  | [0.908, 1.793]  | .160  |
| ------------- | ------ | ------------- | --------------- | ----- |
College graduate or higher  0.356  0.183  1.427  [0.998, 2.041]  .052
| Employment level  |        |              |                 |        |
| ----------------- | ------ | ------------ | --------------- | ------ |
| Employed          | 0.474  | 0.22  1.61   | [1.042, 2.475]  | .032*  |
| Retired           | 0.266  | 0.251  1.31  | [0.798, 2.136]  | .288   |
| Disabled          | 0.059  | 0.276  1.06  | [0.618, 1.820]  | .832   |
| Health factors    |        |              |                 |        |
Expected longevity  0.005  0.005  1.005  [0.996, 1.014]  .239
| Good health  | -0.132  | 0.114  0.876  | [0.702, 1.095]  | .246    |
| ------------ | ------- | ------------- | --------------- | ------- |
| Fair health  | -0.206  | 0.140  0.814  | [0.619, 1.070]  | .140    |
| Poor health  | -0.441  | 0.230  0.643  | [0.410, 1.009]  | .055    |
| Smoker       | -0.362  | 0.127  0.696  | [0.543, 0.893]  | .004**  |

70

Applied Finance Letters, Volume 14, 2025
Has health insurance 0.078 0.183 1.081 [0.754, 1.548] .672
Parents living 0.063 0.125 1.065 [0.833, 1.362] .614
COVID diagnosed -0.142 0.101 0.868 [0.712, 1.057] .159
Long COVID -0.309 0.131 0.734 [0.567, 0.950] .019*
Financial knowledge & social
support
Objective financial knowledge 0.183 0.113 1.201 [0.962, 1.499] .106
Subjective fin. knowledge
0.201 0.204 1.222 [0.820, 1.823] .325
(Medium)
Subjective fin. knowledge (High) 0.534 0.205 1.706 [1.141, 2.551] .009**
Emergency social support 0.275 0.096 1.316 [1.090, 1.589] .004**
Expected income (up) 0.170 0.130 1.186 [0.920, 1.529] .189
Expected income (down) -0.084 0.097 0.920 [0.760, 1.112] .388
Constant -3.690 1.043 0.025 [0.003, 0.193] <.001***
Note: CI = confidence interval; OR = odds ratio. Reference categories: White
(race/ethnicity), Married/partnered (household structure), Less than high school
(education), Self-reported health excellent/very good (health status), Low (subjective
financial knowledge), No social support. *p<.05, **p<.01, ***p<.001.
3.3. Key Findings
Socioeconomic factors strongly predicted household savings behaviour. Higher income
(OR = 1.260, p = .006) and net worth (OR = 1.034, p < .001) increased saving likelihood.
Significant demographic disparities emerged: Hispanic households had 0.71 times the
odds of saving compared to White households (OR = 0.708, p = .006), and single female-
headed households had 0.66 times the odds compared to married/partnered
households (OR = 0.658, p = .001).
Health factors showed significant negative associations with saving. Smokers had 0.70
times the odds of saving compared to non-smokers (OR = 0.696, p = .004), while
households affected by long COVID had 0.73 times the odds compared to unaffected
households (OR = 0.734, p = .019). Poor health showed marginally significant effects (OR
= 0.643, p = .055). Contrary to theoretical expectations, expected longevity did not predict
household savings behaviour (OR = 1.005, p = .239).
Financial knowledge effects varied by measurement type. While objective knowledge
was non-significant (OR = 1.201, p = .106), households with high subjective financial
knowledge had 1.71 times the odds of saving compared to those with low subjective
financial knowledge (OR = 1.706, p = .009). Households with emergency social support
had 1.32 times the odds of saving compared to those without such support (OR = 1.316,
p = .004).
3.4 Interaction Analysis and Robustness Checks
71

Applied Finance Letters, Volume 14, 2025
Interaction  Effects.  To  address  our  third  research  question  about  social  support
moderation,  we  tested  interactions  between  health  factors  and  emergency  social
support. Table 6 presents these results.

Table 6: Interaction Effects on Household Savings Behaviour

| Health Factor                      |     | Interaction with Social Support  |        |          |     |
| ---------------------------------- | --- | -------------------------------- | ------ | -------- | --- |
|                                    |     | Coefficient                      | OR     | p-value  |     |
| Poor health × Social support       |     | 0.687                            | 1.988  | .015*    |     |
| Smoker × Social support            |     | 0.319                            | 1.376  | .064     |     |
| Long COVID × Social support 0.446  |     |                                  | 1.562  | .023*    |     |
|                                    |     |                                  |        |          |     |
Note: Each interaction term tested in separate models including all main effects and
controls from Table 5, *p < .05.
Social support significantly moderates the negative health effects on household savings
behaviour. The significant interaction between poor health and social support (OR =
1.988, p = .015) indicates that emergency social support substantially reduces the
negative impact of poor health on saving probability. Similarly, social support buffered
the negative effects of long COVID (OR = 1.562, p = .023). In contrast, financial knowledge
did  not  significantly  moderate  health-savings  relationships,  suggesting  that  social
capital—rather than individual knowledge—provides the primary buffer against health-
related financial challenges.
Robustness  checks  using  probit  specifications  and  continuous  savings  measures
confirmed these patterns. Most importantly, analysis using precautionary saving motives
as  our  second  dependent  variable  revealed  theoretically  meaningful  mechanistic
differences. Table 7 compares key findings across both saving measures.

Table 7: Comparison of Key Findings across Saving Measures

| Variable  |     | General Saving  |     | Precautionary Motives  |     |
| --------- | --- | --------------- | --- | ---------------------- | --- |
|           |     | OR              | p   | OR                     | p   |
|           |     |                 |     |                        |     |
Health factors
| Smoker               |     | 0.696  | .004**   | 0.893  | .344      |
| -------------------- | --- | ------ | -------- | ------ | --------- |
| Long COVID           |     | 0.734  | .019*    | 1.433  | .003**    |
| Demographics         |     |        |          |        |           |
| Black households     |     | 0.988  | .930     | 1.575  | <.001***  |
| Hispanic households  |     | 0.708  | .006**   | 1.186  | .166      |
| Single female head   |     | 0.658  | .001***  | 0.883  | .266      |
|                      |     |        |          |        |           |
Financial Knowledge
| High subjective fin. knowledge  |     | 1.706  | .009**  | 1.057  | .765  |
| ------------------------------- | --- | ------ | ------- | ------ | ----- |

72

Applied Finance Letters, Volume 14, 2025
Variable General Saving Precautionary Motives
Social Support
Social support 1.316 .004** 0.915 .335
These contrasting patterns reveal different saving pathways: health challenges reduce
general saving capacity while increasing emergency awareness, demographic
vulnerabilities manifest differently across saving types, and financial confidence affects
general saving more than precautionary concerns. This validates our dual-measure
approach to capturing household savings behaviour. Most notably, long COVID
demonstrates opposite effects across measures—reducing general saving capacity
while increasing emergency-focused intentions—suggesting health challenges
simultaneously constrain ability while heightening financial vulnerability awareness.
3.5. Visual Analysis of Key Relationships
To illustrate our main findings about social support moderation and demographic
vulnerabilities, we present visual representations of predicted probabilities from our
regression models.
Figure 2: Household Structure, Social Support, and Household Savings Behaviour
Figure 2 reveals a clear vulnerability gradient across household types. Social support
consistently enhances saving probabilities across all groups, yet structural
disadvantages persist. Single female households remain most financially vulnerable,
with saving probabilities approximately 7 percentage points lower than married
households even when emergency social support is available (0.55 vs. 0.62).
73

Applied Finance Letters, Volume 14, 2025
Figure 3: Social Support Moderation of Health Effects
Figure 3 demonstrates our key theoretical contribution: social support substantially
buffers negative health effects on household savings behaviour. Without emergency
support, poor health reduces saving probability by 12 percentage points (from 0.54 to
0.42). In contrast, households with social support experience only an 8 percentage point
decline (from 0.60 to 0.52). This buffering effect validates our theoretical framework
about social capital as a protective factor against health-related financial challenges,
directly addressing our third research question about social support moderation.
4. Discussion
This study advances the Life Cycle Hypothesis by integrating dimensions of expected
longevity, financial knowledge, health factors, and social support to explain household
savings behaviour. Our findings largely confirm the importance of financial knowledge
while revealing new pathways through which health and social factors shape financial
outcomes.
Subjective financial knowledge emerged as a stronger predictor of saving than objective
knowledge, suggesting that financial confidence may be as important as factual
knowledge in guiding decisions (Morris et al., 2022). This finding has important
implications for financial education programs, which should emphasise confidence-
building alongside knowledge acquisition.
Contrary to theoretical expectations, expected longevity did not predict household
savings behaviour. Instead, direct health factors—smoking, long COVID, and poor
health—emerged as significant barriers. These results suggest that immediate health
limitations influence saving more than abstract life expectancy projections, consistent
with bounded rationality theories (De Nardi et al., 2010).
A key contribution is identifying social support as a significant moderator of health-
74

Applied Finance Letters, Volume 14, 2025
savings relationships. While poor health typically reduced saving likelihood, this effect
was substantially attenuated for households with emergency social support. This
provides empirical support for the buffering hypothesis (Cohen & Wills, 1985) and
highlights the protective role of informal safety nets during health adversity.
Significant demographic disparities emerged, with single female households and
Hispanic households showing persistently lower saving rates despite controlling for
income and education. These gaps suggest structural barriers—including caregiving
burdens and systemic discrimination—that inhibit saving among vulnerable groups.
5. Conclusion
This study examined how financial knowledge, health factors, and social support interact
to influence household savings behaviour using data from the 2022 Survey of Consumer
Finances. Our findings extend the Life Cycle Hypothesis by incorporating behavioural
dimensions that better reflect modern saving challenges. Subjective financial knowledge
significantly increases saving likelihood, while health factors such as smoking and long
COVID negatively impact savings behaviour. A key contribution is demonstrating that
social support significantly moderates the negative effects of health factors on savings
behaviour, providing crucial buffer effects during health-related financial challenges.
Our findings suggest several policy implications. Financial education initiatives should
emphasise confidence-building and target vulnerable populations facing structural
barriers. The interplay between health and financial well-being suggests opportunities for
cross-sector collaboration, with health practitioners incorporating financial counselling
and financial advisors assessing client health. Strengthening social support networks—
both formal and informal—can provide protective effects against financial deterioration
during health crises.
Limitations and Future Research
Several limitations should be acknowledged. The cross-sectional nature of the SCF data
limits causal inference; future research should leverage longitudinal designs to examine
how health and financial knowledge changes influence saving trajectories. Our reliance
on brief financial knowledge measures may not capture multidimensional knowledge
complexity (Gignac & Ooi, 2022). Additionally, this U.S.-focused study may limit
generalizability across different cultural and policy contexts.
Despite these limitations, this study advances understanding by demonstrating how
financial knowledge and social resources can mitigate adverse health effects on
household savings behaviour. The findings underscore the need for interdisciplinary
interventions that address not only knowledge gaps but also health inequalities and
social capital deficiencies to enhance household financial resilience.
75

Applied Finance Letters, Volume 14, 2025
References
Adams, S., Bose, N., & Rustichini, A. (2014). How different are smokers? An analysis based on
personal finances. Journal of Economic Behavior & Organization, 107, 40-50.
https://doi.org/10.1016/j.jebo.2014.08.003
Aizcorbe, A. M., Kennickell, A. B., & Moore, K. B. (2003). Recent changes in US family
finances: Evidence from the 1998 and 2001 Survey of Consumer Finances. Fed. Res.
Bull., 89, 1.
Allgood, S., & Walstad, W. B. (2016). The effects of perceived and actual financial literacy on
financial behaviors. Economic Inquiry, 54(1), 675-697. https://doi.org/10.1111/ecin.12255
Anderson, A., Baker, F., & Robinson, D. T. (2017). Precautionary savings, retirement planning
and misperceptions of financial literacy. Journal of Financial Economics, 126(2), 383-398.
https://doi.org/10.1016/j.jfineco.2017.07.008
Ando, A., & Modigliani, F. (1963). The ‘life cycle’ hypothesis of saving: Aggregate
implications and tests. The American economic review, 53(1), 55-84.
Baumeister, R. F., & Heatherton, T. F. (1996). Self-regulation failure: An overview.
Psychological Inquiry, 7(1), 1–15. https://doi.org/10.1207/s15327965pli0701_1
Behrman, J. R., Mitchell, O. S., Soo, C. K., & Bravo, D. (2012). How financial literacy affects
household wealth accumulation. American Economic Review, 102(3), 300-304.
https://doi.org/10.1257/aer.102.3.300
Bhatia, R., Hirsch, C., Arnold, A. M., Newman, A. B., & Mukamal, K. J. (2023). Social
networks, social support, and life expectancy in older adults: the Cardiovascular Health
Study. Archives of Gerontology and Geriatrics, 111, 104981. https://doi.org/10.1016/
j.archger.2023.104981
Bickel, W. K., Odum, A. L., & Madden, G. J. (1999). Impulsivity and cigarette smoking: Delay
discounting in current, never, and ex-smokers. Psychopharmacology, 146(4), 447–454.
https://doi.org/10.1007/PL00005490
Browning, M., & Lusardi, A. (1996). Household saving: Micro theories and micro facts. Journal
of Economic Literature, 34(4), 1797–1855.
Chen, T. F., Pien, L. C., Fan, C. S., Liang, K. L., & Chiu, Y. W. (2024). Financial strain and
social support as moderators of the relationship between living alone and depressive
symptoms in older people. BMC Geriatrics, 24(1), 646.https://doi.org/10.1186/s12877-024-
05248-2
Chetty, R., Stepner, M., Abraham, S., et al. (2016). The association between income and life
expectancy in the United States, 2001–2014. JAMA, 315(16), 1750–1766. https://doi.org/
10.1001/jama.2016.4226
76

Applied Finance Letters, Volume 14, 2025
Cronqvist, H., & Siegel, S. (2015). The origins of savings behavior. Journal of Political
Economy, 123(1), 123-169. https://doi.org/10.1086/679284
Cohen, S., & Wills, T. A. (1985). Stress, social support, and the buffering hypothesis.
Psychological Bulletin, 98(2), 310-357. https://doi.org/10.1037/0033-2909.98.2.310
Cox, D., & Fafchamps, M. (2008). Extended family and kinship networks: Economic insights
and evolutionary directions. Handbook of Development Economics, 4, 3711-3784.
https://doi.org/10.1016/S1573-4471(07)04058-2
Czaja, S. J., Moxley, J. H., & Rogers, W. A. (2021). Social support, isolation, loneliness, and
health among older adults in the PRISM randomized controlled trial. Frontiers in Psychology,
12, 728658.https://doi.org/10.3389/fpsyg.2021.728658
De Nardi, M., French, E., & Jones, J. B. (2010). Why do the elderly save? The role of medical
expenses. Journal of Political Economy, 118(1), 39-75.https://doi.org/10.1086/651674
Dhakhwa, M., & Babiarz, P. (2019). Does family support network influence the perceived need
for emergency savings. Consumer Interests Annual, 65, 1-12.
Federal Reserve Board. (2023). Economic well-being of U.S. households in 2022. Board of
Governors of the Federal Reserve System. https://www.federalreserve.gov/publications/
2023-economic-well-being-of-us-households-in-2022.htm
Fisher, P. J., & Anong, S. T. (2012). Relationship of saving motives to saving habits. Journal of
Financial Counseling and Planning, 23(1), 63-79.
FINRA Investor Education Foundation. (2025). The state of U.S. financial capability: The 2024
National Financial Capability Study. https://www.finra.org/media\center/newsreleases/
2025/finra-foundation-releases-sixth-wave-national-financial-capability
Gignac, G. E., & Ooi, E. (2022). Measurement error in research on financial literacy: How much
error is there and how does it influence effect size estimates? Journal of Consumer
Affairs, 56(2), 938-956. https://doi.org/10.1111/joca.12417
Gladstone, J. J., & Hundtofte, C. S. (2023). A lack of financial planning predicts increased
mortality risk: Evidence from cohort studies in the United Kingdom and United States. Plos
one, 18(9), e0290506.https://doi.org/10.1371/journal.pone.0290506
Glei, D. A., Lee, C., & Weinstein, M. (2022). Assessment of mortality disparities by wealth
relative to other measures of socioeconomic status among US adults. JAMA network
open, 5(4), e226547-e226547. http://doi.org/10.1001/jamanetworkopen.2022.6547
Goyal, K., & Kumar, S. (2021). Financial literacy: A systematic review and bibliometric
analysis. International Journal of Consumer Studies, 45(1), 80-105. https://doi.org/
10.1111/ijcs.12605
77

Applied Finance Letters, Volume 14, 2025
Hamermesh, D. S. (1985). Expectations, life expectancy, and economic behavior. The Quarterly
Journal of Economics, 100(2), 389-408.
Hastings, J. S., Madrian, B. C., & Skimmyhorn, W. L. (2013). Financial literacy, financial
education, and economic outcomes. Annual Review of Economics, 5(1), 347-373.
https://doi.org/10.1146/annurev-economics-082312-125807
Hogarth, J. M., & Anguelov, C. E. (2003). Can consumers be taught to be rational? The case of
saving behavior. Journal of Consumer Affairs, 37(1), 117-137.
Hurd, M. D., & McGarry, K. (1995). Evaluation of the subjective probabilities of survival in the
health and retirement study. Journal of Human Resources, 30, S268-S292.
https://doi.org/10.2307/146285
Kennickell, A. B. (1995). Saving and permanent income: Evidence from the 1992 SCF. Division
of Research and Statistics, Division of Monetary Affairs, Federal Reserve Board.
Khan, M. S. R., Putthinun, P., Watanapongvanich, S., Yuktadatta, P., Uddin, M. A., & Kadoya,
Y. (2021). Do financial literacy and financial education influence smoking behavior in the
United States? International Journal of Environmental Research and Public Health, 18(5),
2579-2604. https://doi.org/10.3390/ijerph18052579
Lal, S., Nguyen, T. X. T., Sulemana, A. S., Khan, M. S. R., & Kadoya, Y. (2022). Does financial
literacy influence preventive health check-up behavior in Japan? a cross-sectional
study. BMC Public Health, 22(1), 1704-1805. https://doi.org/10.1186/s12889-022-14079-8
Lindamood, S., Hanna, S. D., & Bi, L. (2007). Using the Survey of Consumer Finances: Some
methodological considerations and issues. Journal of Consumer Affairs, 41(2), 195-222.
Lusardi, A., & Mitchell, O. S. (2011). Financial literacy around the world: An overview. Journal
of Pension Economics & Finance, 10(4), 497-508.
https://doi.org/10.1017/S1474747211000448
Lusardi, A., & Mitchell, O. S. (2014). The economic importance of financial literacy: Theory
and evidence. Journal of Economic Literature, 52(1), 5–44. https://doi.org/10.1257/jel.52.1.5
Mani, A., Mullainathan, S., Shafir, E., & Zhao, J. (2013). Poverty impedes cognitive function.
Science, 341(6149), 976-980. https://doi.org/10.1126/science.1238041
Meier, S., & Sprenger, C. D. (2010). Present-biased preferences and credit card borrowing.
American Economic Journal: Applied Economics, 2(1), 193–210.
https://doi.org/10.1257/app.2.1.193
Modigliani, F., & Brumberg, R. (1954). Utility analysis and the consumption function: An
interpretation of cross-section data. In K. K. Kurihara (Ed.), Post-Keynesian economics (pp.
388-436). Rutgers University Press.
78

Applied Finance Letters, Volume 14, 2025
Montalto, C. P., & Yuh, Y. (1998). Estimating nonlinear models with multiply imputed data.
Financial counseling and Planning, 9(1), 97-101. https://ssrn.com/abstract=132596
Morris, T., Maillet, S., & Koffi, V. (2022). Financial knowledge, financial confidence and
learning capacity on financial behavior: a Canadian study. Cogent Social Sciences, 8(1),
1996919. https://doi.org/10.1080/23311886.2021.1996919
Nielsen, R. B., & Seay, M. C. (2014). Complex samples and regression‐based inference:
Considerations for consumer researchers. Journal of Consumer Affairs, 48(3), 603-619.
https://doi.org/10.1111/joca.12038
Ouyang, C., Joseph, M., Zhang, Y., & Naveed, K. (2025). The interplay of financial safety nets,
long-term goals, and saving habits: A moderated mediation study. International Journal of
Financial Studies, 13(1), 47. https://doi.org/10.3390/ijfs13010047
Post, T., & Hanewald, K. (2013). Longevity risk, subjective survival expectations, and individual
saving behavior. Journal of Economic Behavior & Organization, 86, 200-220.
Rha, J. Y., Montalto, C. P., & Hanna, S. D. (2006). The effect of self-control mechanisms on
household saving behavior. Journal of Financial Counseling and Planning, 17(2).
Shin, S. H., & Hanna, S. D. (2017). Accounting for complex sample designs in analyses of the
Survey of Consumer Finances. Journal of Consumer Affairs, 51(2), 433-447.
Smith, J. P. (1999). Healthy bodies and thick wallets: the dual relation between health and
economic status. Journal of Economic Perspectives, 13(2), 145-166.
https://doi.org/10.1257/jep.13.2.145
Stewart, C. C., Yu, L., Lamar, M., Wilson, R. S., Bennett, D. A., & Boyle, P. A. (2020).
Associations of health and financial literacy with mortality in advanced age. Ageing clinical
and experimental research, 32(5), 951-957.
https://doi.org/10.1007/s40520-019-01259-7
Xu, J., Murphy, M., & Akin, H. (2020). Financial literacy and preventive health behavior:
Evidence from the 2017 U.S. National Financial Capability Study. Health Education &
Behavior, 47(6), 812–818. https://doi.org/10.1177/1090198120929923
Yuh, Y., & Hanna, S. D. (2010). Which households think they save? Journal of Consumer
Affairs, 44(1), 70-97. https://doi.org/10.1111/j.1745-6606.2010.01158.x
79