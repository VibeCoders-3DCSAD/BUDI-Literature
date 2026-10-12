---
conversion_metadata:
  converted_at: "2026-10-12T14:26:06Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Fenig & Petersen, 2024.pdf"
  source_pdf_sha256: "fafff576610c8b6eeb9b930366979392f12637199b26abd0df2a2b15095e6f96"
  page_count: 99
  markdown_char_count: 491056
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

NBER WORKING PAPER SERIES

DYNAMIC OPTIMIZATION MEETS BUDGETING:
UNRAVELING FINANCIAL COMPLEXITIES

Guidon Fenig
Luba Petersen

Working Paper 32821
http://www.nber.org/papers/w32821

NATIONAL BUREAU OF ECONOMIC RESEARCH
1050 Massachusetts Avenue
Cambridge, MA 02138
August 2024

This study is financially supported by the Social Sciences and Humanities Research Council of 
Canada. Insight Development Grant:  "Identifying Rules of Thumb in Consumption and Saving 
Decisions." The views expressed herein are those of the authors and do not necessarily reflect the 
views of the National Bureau of Economic Research.

NBER working papers are circulated for discussion and comment purposes. They have not been 
peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies 
official NBER publications.

©  2024  by  Guidon  Fenig  and  Luba  Petersen.  All  rights  reserved.  Short  sections  of  text,  not  to 
exceed  two  paragraphs,  may  be  quoted  without  explicit  permission  provided  that  full  credit, 
including © notice, is given to the source.

---

<!-- PAGE 2 -->

Dynamic Optimization Meets Budgeting: Unraveling Financial Complexities
Guidon Fenig and Luba Petersen
NBER Working Paper No. 32821
August 2024
JEL No. C91,E03,E21,E70

ABSTRACT

This paper explores sources of complexity in dynamic optimization, examining how individuals 
navigate  variation  in  incomes,  prices,  and  returns  in  ten-period  consumption-saving  decisions.  
Our  findings  reveal  that  dynamic  optimization  poses  significant  challenges,  resulting  in 
suboptimal choices even in straightforward scenarios with stable parameters, full information, no 
uncertainty,  and  opportunities  to  learn.  These  challenges  intensify  in  scenarios  involving 
complexities  such  as  inflation  and  compounding  returns,  marked  by  a  pronounced  tendency  to 
over-smooth consumption.

Additionally,  we  introduce  a  novel  budgeting  calculator  designed  to  assist  with  consumption 
planning and to collect valuable non-choice data on subjects' planning strategies and horizons—
an  approach  not  previously  utilized  in  studies  of  dynamic  optimization.  We  observe  significant 
heterogeneity  in  planning  horizons  and  ability  to  optimize  given  a  chosen  horizon.  Complete 
planning  leads  to  better  performance  in  more  complex  scenarios,  even  when  people  do  not 
optimally utilize the calculator.  However, there is little reoptimization after the first period and 
participants tend to stick with suboptimal plans for most of their life cycle. The decision to plan is 
less  influenced  by  the  complexity  of  the  economic  environment  and  more  by  the  length  of  the 
planning horizon.

Guidon Fenig
Department of Economics
University of Ottawa
gfenig@uottawa.ca

Luba Petersen
Department of Economics
Simon Fraser University
8888 University Drive
Burnaby, BC V5A 1S6
and NBER
lubap@sfu.ca

---

<!-- PAGE 3 -->

1

Introduction

In the landscape of ﬁnancial decision-making, dynamic optimization is a crucial element

inﬂuencing choices for both individuals and institutions. This domain spans a broad

spectrum of essential decisions, including investment strategies, labor markets, envi-

ronmental policy formation, and especially, the dynamics of saving and consumption.

Economic theories often assume that agents are capable of navigating these complex

situations eﬀectively. However, empirical evidence suggests a contrasting reality. Many

individuals encounter diﬃculties in planning over time, a challenge emphasized by recent

research (Gabaix and Graeber, 2023; Oprea, 2022). But what makes dynamic optimiza-

tion problems complex?

Our paper investigates how people navigate complexities in consumption-saving de-

cisions, pinpointing ﬁve primary sources of complexity: shifts in the economic environ-

ment, the impact of compounding returns, the length of the planning horizon, compu-

tational challenges, and a lack of experience. To explore these elements, we conducted

incentivized decision-making tasks where participants undertook a series of consumption-

saving exercises over ten-period horizons with full information about all relevant future

variables.

In our baseline scenario, ConstantYP, participants faced consumption decisions under

conditions of constant and known incomes and prices, and without receiving interest on

their savings. In this simpliﬁed setting, theoretically optimal behavior dictates spending

one’s entire income in each period. This design is strategically simple, enabling us to

detect patterns of random decision-making and any systematic biases.

We then introduce various facets of complexity within the optimization problem to

better understand common pitfalls in decision-making.

In the FluctY treatment, we

alter participants’ income between two predictable levels, high and low. This varia-

tion helps us determine if participants can grasp the concept of smoothing their utility

from consumption over time as income changes. The FluctP treatment involves chang-

ing prices between high and low levels. This treatment variation allows us to observe

1

---

<!-- PAGE 4 -->

whether participants take into account the shape of their induced utility function—that

is, how they value each additional unit of consumption—when they decide how much to

spend. In the PosIR treatment, we introduce a new element to our baseline setting by

introducing positive interest on savings. This enables us to assess how the complexity

of decision-making is aﬀected by the presence of compounding returns. Furthermore,

across all treatments, participants made spending decisions sequentially over a ten-period

horizon. This sequential approach to decision-making allowed us, at the subject-level,

to investigate the additional complexity associated with lengthier planning horizons.

Speciﬁcally, we examine whether participants are more likely to make larger planning

errors conditional on their current savings at the start of their decision-making life-cycle.

Our experiments reveal that individuals frequently encounter signiﬁcant challenges in

optimizing their lifetime consumption plans, even in scenarios where income and prices

are stable and savings yield no returns. These results underscore the inherent diﬃculty

of optimization decisions, even under the simplest environments. In our ConstantYP

treatment, the average inexperienced participant managed to attain only 76% of the

unconditional optimal solution (i.e the optimal solution that does not account for current

savings). This performance marginally improves to 82% by the third repetition of the

optimization task, indicating limited learning over time.

Contrary to our expectations, introducing complexity by altering income levels does

not hinder participants’ performance. However, the introduction of more complex el-

ements like compounding interest on savings or ﬂuctuating prices signiﬁcantly reduces

participants’ ability to optimize unconditionally.

In such complex scenarios, inexpe-

rienced participants’ optimization eﬃciency falls to 66% and 62%, respectively. This

decline in performance is persistent, even as participants gain experience through the

second and third iterations of the task. Interestingly, shortening the planning horizon is

more eﬀective in reducing optimization errors than simply gaining more experience. In

the PosIR treatment, for example, participants improve their optimization performance

by over 3 percentage points by reducing the planning horizon by just two periods, a level

of improvement typically seen after repeating the 10-period task twice.

2

---

<!-- PAGE 5 -->

Furthermore, the nature of the errors varies with the type of complexity introduced.

In the PosIR scenario, a common oversight is the undervaluing of early savings, leading

to diminished wealth for later consumption. On the other hand, the FluctP scenario re-

veals a diﬀerent challenge: while most participants recognize the advantage of spending

more when prices are low, their spending often falls short of the optimal level. This is

the ﬁrst study to analyze the complexity of decision-making in the context of inﬂation

in isolation, i.e., when all variables except prices remain constant. It highlights the in-

creased cognitive challenges involved in making optimal decisions under such inﬂationary

conditions.1

To further investigate the impact of these complexities on decision-making, our study

examines the tools individuals commonly use for planning consumption and savings.

Typically, individuals rely on basic tools such as simple calculators or their own math-

ematical skills. This reliance raises an important question: Are the common errors in

dynamic optimization primarily due to calculation mistakes? To address this question,

our study introduces a second set of treatments where participants have access to a bud-

geting calculator. This device goes beyond basic calculations, oﬀering tailored assistance

for creating comprehensive spending plans. It also tracks all computations, allowing us

to analyze how extensively participants plan their spending and whether their planning

behavior changes with the economic conditions they face. This innovative approach,

focusing on non-choice data, provides a unique lens to assess the depth of people’s dy-

namic planning and the impact of economic complexity on their short-sightedness. To

our knowledge, this study is the ﬁrst to utilize non-choice calculator data in the context

of dynamic optimization. By analyzing this data, we gain insights into the decision-

making processes and go beyond just the ﬁnal decisions made by participants.2

Our analysis into the budgeting calculator’s eﬀectiveness yields mixed results. While

1While the experiments conducted by Luhan et al. (2014) and Yamamori et al. (2018) have ana-
lyzed dynamic optimization under ﬂuctuating prices, they simultaneously alter other macroeconomic
variables. In Luhan et al. (2014) experiment, interest rates are positive, and in Yamamori et al. (2018),
savings ﬂuctuate in tandem with prices. This complicates the evaluation of how subjects’ behavior
changes due to purely inﬂationary factors.

2An example of how this type of data can be used is found in Fenig et al. (2022), who apply it to

study group dynamics in non-linear games.

3

---

<!-- PAGE 6 -->

we anticipated that the calculator would streamline the decision-making process, the

actual impact was nuanced. For example, in the ConstantYP treatment, calculator

access led to an increase in utility by eight to eleven percentage points compared to

the unconditional optimal path, and a 3.4 percent rise in monetary rewards normalized

by the maximum potential payoﬀ.

In the PosIR treatment, the calculator improved

optimization by ﬁve to six percentage points, along with a 4.4 percent increase in nor-

malized monetary payoﬀ. However, in FluctY and FluctP, its inﬂuence was minimal or

indiscernible.3

It should be emphasized that the eﬀectiveness of the budgeting tool in simplifying

optimization tasks is contingent upon participants’ proﬁcient utilization. Proﬁcient use

of the calculator increases unconditional optimization by 10 to 20 percentage points. It is

crucial to highlight that in the PosIR setting—unlike in other treatments where problems

are addressable by evaluating one or two periods—calculator use signiﬁcantly facilitates

tackling longer-horizon problems, which are otherwise too challenging to compute man-

ually. Because of these cognitive challenges, one possible heuristic is to compress the

planning horizon. Further investigation reveals that a short-span planning model does

not fully account for deviations from the optimal consumption path. Nevertheless, even

when participants facing positive interest rates formulate full plans—which only about

half of them do—the task remains exceedingly challenging. Although there is a notable

improvement over participants without calculator access, the results remain suboptimal,

as evidenced by their decision-making relative to their planning horizons.

Overall, we ﬁnd strong support to models positing that complexity hinders dynamic

optimization (Gabaix and Graeber, 2023; Woodford, 2019). The most substantial bar-

riers to optimal decision-making include the objective function’s curvature, the impact

of compounding returns, and the length of the planning horizon. Our research indicates

that while varying income alone does not exacerbate decision-making challenges, the

presence of numerical calculations can signiﬁcantly contribute to the complexity of the

task. It is imperative to recognize that the presence of a decision-aid tool like a budget-

3For a more comprehensive analysis, see Appendix E.

4

---

<!-- PAGE 7 -->

ing calculator does not automatically translate to improved outcomes. However, when

used eﬀectively, it can be a powerful aid in navigating complex ﬁnancial decisions.

The structure of the paper is as follows. Section 2 provides a summary of the litera-

ture most relevant to this paper. Section 3 presents the theoretical model, describes the

diﬀerent treatments, outlines the experimental design, and lists the main hypotheses.

Section 4 oﬀers an overview of the main results. In Section 5, we employ econometric

techniques to more formally demonstrate the treatment eﬀects of environmental com-

plexity and the use of the budgeting calculator. In Section 6 we extend our model to

allow for short-span planning. Finally, Section 7 concludes the paper.

2 Related Literature

In this subsection, we explore two distinct yet interconnected bodies of research. The

ﬁrst pertains to the complexities inherent in decision-making, while the second focuses on

learning-to-optimize experiments within the speciﬁc domain of consumption and saving

decisions. These two areas of study provide critical insights that inform our understand-

ing of the challenges and behaviors observed in ﬁnancial decision-making processes.

Many researchers have theorized about the diﬃculties agents face in dynamically

optimizing. A common theme is the inattention to key variables in optimization prob-

lems, as detailed in studies by Schipper (2014), Sims (2003), Ma´ckowiak and Wiederholt

(2015), and Gabaix (2014). These works suggest that agents might either neglect im-

portant variables or focus on a limited subset due to the costs of processing information.

Mis-speciﬁed preferences also contribute to what appears to be optimization errors. Con-

trary to the commonly assumed exponential discounting in many intertemporal planning

models, substantial evidence suggests that individuals tend to discount future utility in

a hyperbolic manner (Loewenstein and Prelec, 1992; Laibson, 1997; O’Donoghue and

Rabin, 1999).

The literature also highlights the numerical challenges in dynamic optimization. Even

the authors of this paper admit to ﬁnding the mathematical aspects of extended multi-

5

---

<!-- PAGE 8 -->

period constrained optimization daunting. Simple three-period problems, which might

seem elementary, can still pose signiﬁcant hurdles for many (Gabaix and Graeber, 2023).

Emphasizing the importance of this, Lusardi and Wallace (2013) highlight that a ﬁrm

grasp on quantitative literacy is a cornerstone of ﬁnancial literacy.

In the context of ﬁnancial planning over lengthy horizons, Ilut and Valchev (2023)

develop a model in which agents, despite perceiving all objective variables relevant to

their payoﬀ, encounter subjective uncertainty about optimizing their actions in the given

state. This necessitates engaging in costly learning processes to determine the optimal

course of action. Our experimental design captures this situation: participants are

fully informed of all relevant variables, yet they face challenges in eﬀective problem-

solving. Moreover, our novel budgeting calculator enables us to observe their planning

process. Our ﬁndings align with the dual reasoning model proposed by these authors.

Initially, our participants tend to rely on cognitive planning (System 2). However, as

they progress through their life cycle, many switch to using intuitive heuristics (System

1). Interestingly, towards the end of their life cycle, as the planning horizon becomes

shorter, some participants revert to cognitive planning (System 2).

The complexity of the economic environment and its impact on dynamic optimization

is a focal point in the literature. Gabaix and Graeber (2023) investigate a three-period

consumption-saving scenario, uncovering that tasks with ﬂuctuating endowments and

positive, compounding interest are viewed by subjects as more challenging, leading to

increased errors and longer decision times. Consistent with Gabaix and Graeber, we ﬁnd

that complexity in speciﬁc environments (PosIR and FluctP) result in poorer optimiza-

tion. We further show that longer planning horizons exacerbate optimization errors.

Indeed, condensing the planning horizon is a commonly employed strategy to reduce

cognitive demands in dynamic optimization tasks. Caliendo and Aadland propose a

framework accommodating heterogeneity in planning horizons, where individuals with

perfect foresight and those adopting hand-to-mouth strategies represent the extremes.

? analyzes experimental data from an environment similar to our PosIR treatment.4 In

4Most of the data analyzed is taken from Carbone and Hey (2004).

6

---

<!-- PAGE 9 -->

their study, the horizon spans 25 periods, and the goal is to analyze alternative models

that participants may have in mind, allowing for deviations from the optimal consump-

tion path. Thus, they conduct a comparison between models and ﬁnd that an exponen-

tial discounting model in which participants discount future consumption (even if they

should not) explains 28% of the data. Furthermore, the rational model—characterized

by no discounting, lack of hyperbolic preferences, and a full planning horizon—accounts

for 22% of the observations, while the short-span planning horizon explains approxi-

mately one ﬁfth of the data. This latter observation is consistent with our ﬁndings that

short-span planning alone cannot account for the majority of deviations observed in our

PosIR treatment.

Dynamic optimization problems are intrinsically complex. The challenges stem from

various factors: the extended planning horizons, a wide array of choice variables, the

options to borrow or save at diﬀering interest rates, and the unpredictability of future

events. Such a diverse range of considerations often leads to decision overload for indi-

viduals, nudging them towards simpler heuristics or fallback options in an attempt to

manage the overload. Simon (1956) develops a model of ’satisﬁcing’ that captures this

process by which a decision maker curtails further search. This idea is further developed

by Krosnick (1991) who links satisﬁcing to a combination of expected task diﬃculty, mo-

tivation, and ability. Caplin et al. (2011) show evidence that in complex decision tasks,

subjects search sequentially and stop searching when they reach their reservation utility.

Non-choice data from our Calculator treatments corroborate these observations of in-

complete searches and suboptimal decision-making, indicating limited average beneﬁts

from tools such as our budgeting calculator. Importantly, we do not observe signiﬁcant

diﬀerences in search behavior as environmental complexity increases (as we move from

ConstantYP to more complex settings). We do, however, ﬁnd a signiﬁcant increase in

calculator usage as the horizon over which subjects are planning is reduced signiﬁcantly

(in the last two periods of their life-cycle). This further substantiates that the planning

horizon is a more salient determinant of complexity for participants than the economic

environment variables.

7

---

<!-- PAGE 10 -->

Our analysis of dynamic optimization facilitated by a budgeting calculator con-

tributes to the extensive body of research on household ﬁnance puzzles. D’Acunto and

Rossi (2023) discuss the success of alternative strategies to mitigate household ﬁnancial

errors: ﬁnancial advising, nudges, and robo-advising. The design of our budgeting tool

falls somewhere in between nudges and robo-advising. The presence of the budgeting

calculator nudges participants to at least consider the complete planning horizon when

making their consumption decisions. The calculator mitigates the cognitive burdens

associated with budgeting calculations but does not advise or encourage participants to

make certain plans.5 D’Acunto et al. (2019) demonstrate that in the context of portfolio

investment, robo-advice helps reduce several behavioral biases, including the disposition

eﬀect, trend chasing, and the rank eﬀect. We also ﬁnd that the introduction of a cal-

culator can signiﬁcantly improve optimization, with more pronounced eﬀects in simpler

environments, such as our ConstantYP treatment. The beneﬁts of our tool in more

complex settings involving compounding interest or ﬂuctuating prices are notably less,

and suggest a need for additional advising or social learning (Ballinger et al., 2003).

Overview of Experimental Designs in Dynamic Optimization

The controlled environment of a laboratory is instrumental in unraveling how individuals

approach optimization amidst the variability of economic conditions. Table 1 provides a

comprehensive summary of the various experimental design diﬀerences across the broad

learning-to-optimize literature (Duﬀy, 2016). In most experiments, participants obtain

interest from their savings, and there is a prevalent uncertainty about future economic

variables, with income being the variable that most frequently changes. The most com-

mon planning horizon across these studies is 20 periods, and it is notable that most

experimental designs do not involve optimal closed-form solutions. The interplay of

complex elements within these experimental settings—such as extended horizons, un-

5The one exception is that the calculator informs participants if they have insuﬃcient income over

their lifetime to fulﬁll their consumption plan.

8

---

<!-- PAGE 11 -->

certainty, returns on savings, and income ﬂuctuations—poses a challenge in discerning

the impact of diﬀerent aspects of complexity on optimization behaviors. To address this,

our parameterization, as detailed at the bottom of the table, introduces one feature of

complexity at a time, allowing for a meticulous examination of each element’s inﬂuence

on optimization.

Table 1: Related learning-to-optimize experimental literature

Paper

Uncertainty

Interest
Rates (IR)

Fluctuating
Variable

Borrowing
Constraints

No. of
Periods

Closed-Form
Solution

Hey and Dardanoni (1988)
Ballinger et al. (2003)
Carbone and Hey (2004)
Brown et al. (2009)
Ballinger et al. (2011)
Carbone and Duﬀy (2014)
Luhan et al. (2014)
Carbone and Infante (2015)
Meissner (2016)
Duﬀy and Li (2019)
Yamamori et al. (2018)
Carbone et al. (2019)
Lu (2022)
Miller and Rholes (2023)
Duﬀy and Orland (2023)
Gabaix and Graeber (2023)
Li (2024)

This paper
ConstantYP
PosIR
FluctY
FluctP

Yes
Yes
Yes
Yes
Yes
No
No
Yes
Yes
No
No
Yes
No
Yes
Yes
No
No

No
No
No
No

>0
>0
>0
= 0
= 0
>0
>0
>0
=0
=0
= 0
>0
>0
>0
= 0
> 0
> 0

= 0
> 0
= 0
= 0

Income
Income
Income
Income
Income
Income
Price and IR
Income
Income
Income
Prices
Income
Income
Income
Income
Income
Income

None
None
Income
Price

Yes
Yes
Yes
Yes
Yes
Yes
Yes
No
No
Yes
Yes
No
No
No
No
No
Yes

Yes
Yes
Yes
Yes

Indeﬁnite
60
25
30
20
25
5
15
20
25
20
15
9
20
3
3
Indeﬁnite

10
10
10
10

No
No
No
No
No
Yes
Yes
No
Yes
Yes
Yes
No
No
No
No
Yes
No

Yes
Yes
Yes
Yes

Although direct comparisons among these experiments are diﬃcult due to their dif-

fering parameters and information sets, two key patterns consistently emerge in the

research. First, there is a noticeable struggle with dynamic planning – individuals often

either consume too much or too little, neglecting the long-term impacts of compounding

returns. Second, the tendency to optimize decisions appears to enhance as the planning

horizon becomes shorter. Echoing this, Ballinger et al. (2011) observes that subjects

typically anticipate only up to three periods ahead, underscoring the cognitive limits in

longer-term ﬁnancial planning.

9

---

<!-- PAGE 12 -->

3 Theoretical Model and Experimental Design

The theoretical framework underpinning this study is a standard intertemporal model

of life-cycle consumption and savings (See Modigliani and Brumberg, 1954). Our model

is based on a ﬁnite-horizon and deterministic framework. Each consumer’s goal is to

subject to:

max
ct

T
(cid:88)

t=1

k

(cid:18) 1

(cid:19)

1 − σ

c1−σ
t

ptct + st = yt + (1 + r)st−1

st ≥ 0 : ∀t and s0 = 0.

(1)

(2)

(3)

We assume a concave utility function, speciﬁcally a constant relative risk aversion

(CRRA) with a parameter σ and a constant k, the variables yt, st, and r represent the

consumer’s exogenous income, savings, and known and constant interest rate, respec-

tively. The constraint st ≥ 0 implies that borrowing is not allowed.

In this ﬁnite horizon model, the consumer faces no uncertainty regarding price and

income processes. They make decisions about consumption, denoted as ct, over T peri-

ods, considering their income, yt, and implicitly decides how much to save at the interest

rate r. The consumer pays a price pt for each unit of consumption.

The optimal consumption path is given by T − 1 Euler equations:

ct+1 =

(cid:18) pt
pt+1

(cid:19) 1

σ

(1 + r)

ct

(4)

These Euler equations relate consumption in period t to consumption in period t + 1

and must be satisﬁed within the optimal consumption path. We use the lifetime budget

constraint (Equation 5) to derive a system of T equations and T unknowns and then

ﬁnd the optimal consumption level c∗

t for t ∈ [1, T ].

10

---

<!-- PAGE 13 -->

T
(cid:88)

t=1

ptct
(1 + r)t−1 ≤

T
(cid:88)

t=1

yt
(1 + r)t−1

(5)

Solving the system of equations also yields the optimal level of consumption for period

1,

c1 =

(cid:18)

3.1 Treatments

(cid:80)T

t=1

1
(1+r)t−1 yt

(cid:18)

p1 + p

1
σ
1

(cid:16)

(cid:80)T

t=2

pt
(1+r)t−1

(cid:17) σ−1

σ

(cid:19)(cid:19)

(6)

Our objective in designing the baseline experimental environment was to create a setting

that would enable participants to solve the dynamic decision problem without relying

on advanced budgeting tools. Therefore, we parameterized our baseline environment,

named ConstantYP, to maintain income and prices constant throughout the entire

consumption horizon. We selected a planning horizon of T = 10 periods, which is

suﬃciently long for participants to plan ahead and also provides ample time for us

to observe their learning through stationary repetitions of the environment. Including

stationary repetitions is critical in life-cycle experiments because some participants may

only understand how to overcome the diﬃculties of the environment halfway through the

sequence, making it impossible for them to adjust their previous consumption choices.

Each participant encountered three repetitions of ten periods, and we re-calibrated the

environment across repetitions to generate slightly diﬀerent optimization problems.

We designed and implemented three additional treatments, each introducing a dis-

tinct dimension of complexity to understand where and why errors occur in decision-

making. The treatments were conducted using a between-subject design. The ﬁrst

treatment, FluctY, varies participants’ income between two predictable levels, high

(yH) and low (yL), throughout the horizon. By ensuring that a higher income is received

in the ﬁrst period, we prevent the budget constraint from binding for an optimizing

participant, and even for individuals who tend to over-consume compared to the uncon-

11

---

<!-- PAGE 14 -->

ditionally optimal solution. This treatment is particularly insightful, as it evaluates the

participants’ capability to smooth their consumption over time in the face of ﬂuctuating

income. In the second treatment, PosIR, the complexity is increased relative to the

ConstantYP treatment by introducing a positive interest rate (r = 0.1) on savings in

every period of each of the three repetitions. This approach allows us to observe the

cognitive challenges associated with compounding returns on savings decisions. Lastly,

in the FluctP treatment, we introduce price ﬂuctuations between two values, high (pH)

and low (pL), for the entire horizon. This treatment investigates whether participants

consider the shape of their utility function—that is, their valuation of each additional

unit of consumption—in their spending decisions, as prices vary. These three treat-

ments, by adding diﬀerent complexity dimensions to the basic optimization setting, help

us dissect the nuances of decision-making under varied economic conditions.

To incentivize participants’ optimization decisions, we induce a standard constant

relative risk aversion (CRRA) per-period utility function:

u(ct) = k

(cid:18) 1

(cid:19)

1 − σ

c1−σ
t

.

Here, we set σ = 0.5 across all treatments. The parameter k is a scaling constant that

does not aﬀect the optimal consumption path. In the FluctP treatment, we assign the

constant k a value of 2.65, and for the other treatments, we assign it a value of 3.35.

This speciﬁc adjustment is made to ensure that the optimal life-cycle utility is equalized

across all treatments, where the interest rate r is set to zero. The chosen value for σ is

intended to create a suﬃciently large intertemporal trade-oﬀ. Table 2 provides details

on the income, price, and interest rate processes for each treatment. It is important to

highlight the variations across repetitions: in the second repetition, income is doubled

relative to the ﬁrst. In the third repetition, both income and prices are doubled compared

to the ﬁrst repetition. Although the nominal variables change from the ﬁrst to the last

repetition, the real variables stay consistent, ensuring identical optimal solutions across

these repetitions.

12

---

<!-- PAGE 15 -->

Table 2: Parameters of Treatments

Treatment

Constant YP PosIR FluctY FluctP

Repetition 1

Repetition 2

Repetition 3

t ∈ {1, 3, 5, 7, 9}
t ∈ {2, 4, 6, 8, 10}

t ∈ {1, 3, 5, 7, 9}
t ∈ {2, 4, 6, 8, 10}

t ∈ {1, 3, 5, 7, 9}
t ∈ {2, 4, 6, 8, 10}

t ∈ {1, 3, 5, 7, 9}
t ∈ {2, 4, 6, 8, 10}

t ∈ {1, 3, 5, 7, 9}
t ∈ {2, 4, 6, 8, 10}

t ∈ {1, 3, 5, 7, 9}
t ∈ {2, 4, 6, 8, 10}

yt

pt

r

yt

pt

r

yt

pt

r

1000
1000

100
100

0

2000
2000

100
100

0

2000
2000

200
200

0

1000
1000

100
100

0.1

2000
2000

100
100

0.1

2000
2000

200
200

0.1

1500
500

100
100

0

3000
3000

100
100

0

3000
3000

200
200

0

1200
1200

150
50

0

2400
2400

150
50

0

2400
2400

300
100

0

Figure 1 displays the optimal consumption path corresponding to each treatment

and repetition. Notably, despite the diﬀerences in the income process, the optimal con-

sumption path remains the same for both the Constant YP and FluctY treatments. In

this frameworks, consumers maximize utility by consuming 10 units per period in Rep-

etitions 1 and 3, and 20 units per period in Repetition 2. In the PosIR treatment, the

optimal consumption path progressively increases, reﬂecting the absence of discounting.

Under the FluctP treatment, the optimal consumption level adjusts in response to price

ﬂuctuations, increasing when prices are low and decreasing when they are high, con-

sistent with a bi-periodic pattern. Additionally, Figure 1 illustrates the consumption

path yt
pt

, representing an agent’s mistaken static optimization approach, where the entire

income is consumed each period without considering the intertemporal dynamics.6

6The exception is the ConstantYP treatment, in which the optimal unconditional consumption path

implies not saving.

13

---

<!-- PAGE 16 -->

In the ConstantYP treatment, the unconditional optimal solution corresponds to the

’Hand-to-Mouth’ (H2M) strategy in the initial period. If a participant opts to save any

income during this period, the conditionally optimal consumption path would diverge

from the H2M heuristic. Conversely, in all other treatments, a marked divergence is

observed between the optimal and H2M consumption paths.7

Figure 1: Theoretical Predictions.

We introduce a second between-subject treatment variation to our study by varying

participants’ access to a budgeting calculator across each of the four parameterizations.

In the Calc treatments, participants were provided with the option to utilize a bud-

geting calculator, enabling them to input hypothetical consumption choices for current

and future periods based on the given income, prices, and interest rates. Figure 2(a)

shows a screenshot of the budgeting calculator. In this example, participants could in-

put a consumption plan for periods 6-10 and calculate the hypothetical per-period and

accumulated points. Participants had unrestricted access to the calculator without any

7We analyze this strategy in Appendix D.

14

---

<!-- PAGE 17 -->

mandatory usage requirements. Upon submitting their decisions, participants could re-

view the history of their consumption choices and corresponding savings balances. The

software recorded all plans after a participant clicked the calculate button. However,

each time subjects submitted their consumption choices, the calculator was cleared.

In contrast, participants in the NoCalc treatment lacked access to the budgeting

calculator. Figure 2(b) displays a screenshot of the NoCalc interface. Although partici-

pants were unable to utilize the tool for ﬁnancial planning, they retained the ability to

review the history of their past choices as well as future incomes, prices, and interest

rates. Participants in both treatments could employ the Windows calculator for their

decisions; however, these inputs were not recorded.8 9

Figure 2: Screenshots for Treatments with a Budget Calculator and Treatments without
a Budget Calculator

8It is noteworthy that our NoCalc treatments provide more detailed and readily accessible infor-
mation compared to standard experiments in consumption smoothing. In these standard experiments,
subjects sometimes only see their current income and accumulated savings, based on which they have
to make their current consumption decisions.

9Household recall of past decisions is shown to be limited D’Acunto and Weber (2022), and house-
holds are unable to pay attention and retain all this information over their lifetime D’Acunto et al.
(2023). As both of our No-Calculator and Calculator treatments provide participants with detailed in-
formation about their past, current, and future individual spending and aggregate variables, we interpret
participants’ optimization performance as an upper-bound on their ability to solve such problems.

15

---

<!-- PAGE 18 -->

3.2 Experimental Procedures

The study recruited undergraduate and graduate participants from various academic

disciplines, resulting in a total of 326 subjects who participated in one of eight treat-

ments. The experiments were conducted in-person at the CRABE Laboratory at Simon

Fraser University (SFU) and the SSRL at the University of Saskatchewan (UofS). Our

participant sample was nearly evenly split between individuals from SFU and UofS.

The experimental sessions were held from July 2017 through May 2018. Table 3 shows

the number of participants per treatment. The experiment was computerized and pro-

grammed using z-Tree Fischbacher (2007).

Table 3: Number of Subjects per Treatment

Treatment

ConstantYP Calc
ConstantYP No Calc

PosIR Calc
PosIR No Calc

FluctY Calc
FluctY No Calc

FluctP Calc
FluctP No Calc

Budgeting
Calculator

Number
of Subjects

Yes
No

Yes
No

Yes
No

Yes
No

44
44

48
43

48
46

45
48

We implemented a “between subjects” design by randomly assigning each subject

to only one of the eight treatments. At the beginning of each session, the experi-

menter read aloud the written instructions provided to the participants. Subsequently,

participants completed an interactive computerized instruction phase and answered in-

centivized control questions. These control questions, detailed in Appendix G, ensured

that participants understood the main features of the dynamic optimization experiment

16

---

<!-- PAGE 19 -->

and the tools available to them. For instance, to illustrate the principle of diminish-

ing marginal utility, given that the induced utility function is concave, a set of control

questions ensured that participants grasp this concept before proceeding with the main

tasks of the experiment. In one set of questions, participants were asked to provide the

utility levels associated with consumption levels of 1, 2, 9, and 10 units using the Con-

sumption to Utility converter provided in all treatments. They then had to recognize

that increasing their consumption from 1 to 2 units results in a larger increase in utility

compared to increasing it from 9 to 10 units. Participants earned points based on their

performance in the control questions: four points for each correct answer on the ﬁrst

attempt, three points for the second attempt, and two points for the third attempt. No

further points were awarded beyond three attempts, and participants were required to

answer all questions correctly to proceed.

After completing these questions, participants proceeded to Stage 1. This stage in-

volved three repetitions of one of the dynamic optimization environments shown in Table

2. Figure 3 displays a screenshot of the main computer interface.10 At the beginning

of each period, participants received income (yt) in tokens and were asked to decide

how many units of output they wanted to purchase. To facilitate their decision-making,

participants could refer to the plot correlating output with points positioned at the bot-

tom right corner of the screen. Alternatively, they could utilize the Output to Points

converter located in the upper right corner of the screen to enhance their understanding

of the utility function’s properties. In the Calc sessions, participants could also use the

budgeting calculator located on the right-hand side of the screen to explore diﬀerent

consumption paths and their implications for own savings and points (utility) before

submitting their ﬁnal choices on the left-hand side of the screen. Our interface design

was intended to ensure that all relevant information was readily accessible to participants

on a single screen.11

10There was no time limit for completing any stage of the experiment. In Stage 1, which consisted of

three repetitions, subjects spent between 3 and 85 minutes in total.

11Participants who requested it were provided with pen and paper to write down calculations, which

could be used at any point during the experiment.

17

---

<!-- PAGE 20 -->

Figure 3: Screenshot of the Experimental Software for Stage 1

In the subsequent three stages of the experiment, we collected data that distinguished

participants across three dimensions: risk preferences, ﬁnancial literacy, and the ability

to use backward induction. In Stage 2, risk preferences were assessed through a task

adapted from Eckel and Grossman (2002), where participants selected from six distinct

50/50 gambles (refer to Appendix H.2 for a screenshot). This assessment oﬀers a foun-

dational measurement of key attributes inﬂuencing various economic decisions, serving

as a control variable. In Stage 3, ﬁnancial literacy was evaluated using a methodology

adapted from Lusardi and Mitchell (2007), involving ﬁve multiple-choice questions with

points awarded for correct ﬁrst-attempt answers. This evaluation is crucial, as ﬁnancially

literate individuals are better positioned to create optimal budgeting plans, particularly

by taking advantage of consumption smoothing and compounding interest rates (refer to

Appendix H.3). In Stage 4, backward induction ability was assessed through the Race to

60 game, proposed by Bosch-Rosa et al. (2018). Participants competed against a com-

puter, selecting numbers from 1 to 10 to reach or exceed 60 ﬁrst, earning eight points

18

---

<!-- PAGE 21 -->

per win (refer to Appendix H.4 for a screenshot). This assessment is crucial, as dynamic

models frequently rely on backward induction for solutions. The experiment concluded

with a demographic questionnaire, collecting information on participants’ age, gender,

education, and employment status.

To determine participants’ compensation, we added up the points they earned in all

four stages and from correctly answering the control questions. For Stage 1, participants

were paid for one randomly selected repetition. Payment was made in Canadian dollars

(CAD) at an exchange rate of 25 points = $1. In addition, participants received a show-

up fee of $7. On average, participants completed the experiment in 40 minutes, and the

average payment was $21.39. Figure 4 provides a summary of the diﬀerent stages of the

experiment.

Figure 4: Sequence of Events in Experimental Sessions.

19

---

<!-- PAGE 22 -->

3.3 Hypotheses

Our analysis centers on two metrics to gauge participants’ optimization abilities. The

ﬁrst metric, the Unconditional Optimal Index, quantiﬁes the relative disparity between

the actual utility and the utility of the unconditional optimal solution, expressed as a

percentage:

U ncOptIndexi,q,r,t = γU = 1 −

|Ui,q,r,t − U unc
q,r,t|
U unc
q,r,t

(7)

where Ui,q,r,t represents the utility associated with the actual consumption choice made in

treatment q, repetition, r, period t by participant i, while U unc

q,r,t represents the treatment-

repetition-period utility associated with unconditionally optimal consumption. Note

that U unc

q,r,t is the same for all participants of the same treatment, repetition and period.

The index takes a value of 1 when a participant chooses a consumption level that matches

the unconditional optimal. The unconditional optimal level of consumption is calculated

at the outset of each repetition, prior to any consumption decisions by participants, based

on the complete sequence of income, prices, and interest rates for that repetition. The

second measure is the Conditional Optimal Index that computes the relative disparity

between the actual utility and the utility linked to participant i’s conditional optimal

solution, also represented as a percentage:

CondOptIndexi,q,r,t = γC = 1 −

|Ui,q,r,t − U cond
i,q,r,t|
U cond
i,q,r,t

(8)

where U cond

i,q,r,t represents the utility associated with subject i’s conditionally optimal con-

sumption in treatment q, repetition r, and period t. The conditional optimal level of

consumption is computed for each period as the repetition progresses, contingent on the

starting balances of participant i and the forthcoming stream of incomes, prices, and

interest rates. The conditional and unconditional optimal solutions coincide in the ﬁrst

period of each repetition.12

12Note that one of the advantages of our indices is that they account for the loss in payoﬀs (utility)
when deviating from the unconditional and conditional paths, rather than just measuring deviations in

20

---

<!-- PAGE 23 -->

In our experiment, participants have complete information about the lifetime stream

of income, prices, and interest rates they will encounter in each sequence. According to

standard rational-agent economic theory, agents knowledgeable in solving constrained

optimization problems would make spending decisions aligned with the unconditional op-

timal consumption path. Should they temporarily deviate from this optimal path, they

would be expected to make conditionally optimal decisions thereafter. The features and

complexity of the economic environment should not inﬂuence ability to optimize. This

serves as the basis of our ﬁrst hypothesis.

Hypothesis 1: (Un)conditional optimal consumption does not diﬀer across environ-

ments or a presence of budgeting calculator: γConstantY P = γF luctY = γF luctP = γP osIR.

However, substantial evidence presented in Table 1 demonstrates signiﬁcant devia-

tions from the (un)conditionally optimal consumption path in spending decisions. Re-

lated work by Gabaix and Graeber (2023) and Enke et al. (2023) highlight the role that

complexity plays in behavioral biases and optimization errors. They show that people

optimize better in environments that are relatively less complex. To identify and rank

the complexity of economic environments, we utilize the model from Gabaix and Grae-

ber (2023), which assesses complexity within an intertemporal consumption framework.

Their ﬁndings indicate that the level of complexity is determined by the number of non-

zero terms in a Taylor expansion of the optimal consumption level. Complexity increases

with the number of interacting variables when a term is non-zero. Hence, we initiate

this analysis by linearizing Equation \ref{eq } through a Taylor expansion:13

c1 =

y1
p1

+

1
T p1

T
(cid:88)

t=2

(yt − y1) −

y1 (T − 1)
2σp1

r +

(cid:18) 1 − σ
σ

(cid:19) y1
T p2
1

T
(cid:88)

t=2

(pt − p1)

(9)

Following Gabaix and Graeber (2023), each element of the problem is assumed to

terms of consumption values.

13Appendix A shows the derivation of the Taylor expansion.

21

---

<!-- PAGE 24 -->

have the same level of complexity, ¯c.14 We assess that our ConstantYP environment

exhibits the least amount of complexity (normalized to zero complexity). The FluctY

treatment entails a complexity level of ¯c, as individuals need to consider the horizon

when calculating optimal choices. Finally, FluctP and PosIR are predicted to have a

complexity level of 2¯c, as individuals now need to consider the interaction between the

horizon and the elasticity of substitution, σ. This leads to our alternative hypothesis

that the relative complexity across environments determines the relative ordering of op-

timization errors.

Alternative Hypothesis 1: (Un)conditional optimal consumption is ordered based on

the complexity of the environment: γConstantY P > γF luctY > γP osIR = γF luctP .

Given that all environments, with the exception of ConstantYP, exhibit inherent

complexity, computing the optimal level of consumption becomes a challenging task. It

is reasonable to anticipate that choices of individuals with access to a budgeting calcula-

tor would be closer to the optimal level of consumption than those without access to it.

This motivates our second hypothesis, which posits that the availability of a budgeting

tool signiﬁcantly improves consumption decisions. Access to a budgeting calculator can

be particularly helpful for individuals who struggle with computing the optimal level,

even in less complex environments.

Hypothesis 2. The budgeting calculator improves (un)conditional optimal consump-

tion: γj,Calc > γj,N oCalc for environment j ∈ {ConstantY P, P osIR, F luctY, F luctP }.

By tracking the consumption decisions of participants over multiple repetitions, we

can evaluate how experience contributes to enhancements in their dynamic optimiza-

tion skills. Evidence from Ballinger et al. (2003) suggests that participants learn from

14For hypothesis formulation and testing purposes, we focus on ordinal ranking rather than cardinal

ranking.

22

---

<!-- PAGE 25 -->

experience. Our experimental design can capture this learning clearly. Comparing the

ﬁrst and third repetitions, where changes are made only in nominal terms, the optimal

consumption paths remain unaltered.

Hypothesis 3. Deviations of consumption from the (un)conditional optimal consump-

tion paths decrease in later repetitions.

A fundamental distinction in calculating unconditional versus conditional optimal

paths lies in the respective planning approaches. For the unconditional path, it is nec-

essary to accurately determine the optimal consumption values for the entire horizon

immediately in period 1. This task becomes increasingly challenging with a longer hori-

zon. On the other hand, the conditional optimal path allows subjects to adjust their

plans in response to unfolding events as each period progresses, making it easier to stay

on or near the optimal path. Consequently, we hypothesize that with a shorter horizon

for optimization, subjects are more likely to make consumption decisions that align with

the conditional optimal path, as the reduced planning horizon simpliﬁes the task.

Hypothesis 4. Deviations of consumption from the conditional optimal consumption

path decrease as the planning horizon becomes shorter.

Our ﬁnal hypothesis links individual characteristics with dynamic optimization capabil-

ities. Dynamic optimization requires participants not only to perform complex ﬁnancial

calculations but also to contemplate their future decisions. We hypothesize that mathe-

matical proﬁciency, ﬁnancial literacy, and backward induction skills will positively cor-

relate with dynamic optimization abilities (see Lusardi and Wallace, 2013). Participants

endowed with these skills are likely better prepared to comprehend and eﬀectively utilize

the budgeting tool, thereby achieving greater alignment with the optimal consumption

paths.

23

---

<!-- PAGE 26 -->

Hypothesis 5. Dynamic optimization is positively correlated with mathematical train-

ing, ﬁnancial literacy, and backward-induction skills.

4 Overview of experimental results

We begin with an overview of optimization performance and calculator usage across the

diﬀerent treatment.

4.1 Average consumption decisions

Figure 5 presents the mean consumption decisions over time for Repetitions 1 and 3

for each treatment, represented by solid black lines. The gray area indicates the 95%

conﬁdence intervals.15 The optimal consumption path is denoted by red dashed lines.

We only include periods 1 to 9 because the consumption decision in Period 10 was trivial;

to maximize their current utility, subjects had to spend all the available cash in their

bank account.16

Across diﬀerent treatments, there are noticeable disparities in participants’ opti-

mization abilities. In the ConstantYP treatment, even in the ﬁrst repetition, the mean

participant with access to the budgeting calculator consistently selects a consumption

path that is nearly optimal.

In other treatments, deviations from optimality exhibit distinct patterns.

In the

PosIR treatment, the optimal path involves saving a relatively larger share of income in

early periods to take advantage of the compounding return. Participants often under-

estimate the beneﬁts of early savings in their lifecycle, leading to overconsumption in

initial periods and underconsumption in subsequent periods. Their ability to optimize

does not appear to improve with experience.17

15The individual time series for the consumption choices can be found in Appendix F.
16To make sure participants had no calculation errors, we displayed a message indicating the exact
consumption amount they needed to enter to spend it all. The vast majority followed this guidance.
Across all subjects and all repetitions, in 90 percent of the cases, they ﬁnished the repetition with no
cash remaining in their bank account.

17We also investigate a scenario where subjects perceive an increase in savings following a simple

24

---

<!-- PAGE 27 -->

Figure 5: Average consumption per period and treatment

In the FluctY treatment, the optimal consumption path remains constant. Optimiz-

ing participants should save a portion of their income in odd-numbered periods to oﬀset

lower income in even-numbered periods. In Repetition 1, less experienced participants

often under-consume in periods with lower income, leading to excessive saving and con-

sumption in Period 9. However, with increased experience, this tendency to oversave

diminishes, particularly when participants have access to the budgeting calculator.

In the FluctP treatment, the optimal plan involves setting aside some income during

odd-numbered periods when prices are relatively high and utilize their entire wealth

interest rate model. This implies that each saved token is believed to grow to an amount represented
by 1 + (cid:80)T
s=t rs by the end of a speciﬁed time horizon. Nonetheless, the data from PosIR cannot be
explained by individuals employing this heuristic.

25

---

<!-- PAGE 28 -->

during even-numbered periods. Although the average participant shows a basic under-

standing of how consumption should ﬂuctuate with price changes, there is a marked

tendency to excessively smooth consumption. This leads to heightened consumption

in odd-numbered periods and inadequate consumption in even-numbered periods rela-

tive to the unconditionally optimal decision. This behavior remains up to Repetition 3.

However, experience leads to notable improvements in optimization, especially for those

participants who do not have access to a budgeting calculator.

Finally, regardless of the availability of a budgeting calculator, participants exhibit

distinct consumption smoothing behaviors across diﬀerent treatments. In simpler treat-

ments like ConstantYP and FluctY, we observe a trend towards undersmoothing of

consumption among experienced participants. On the other hand, in more complex

treatments such as FluctP and PosIR, experienced participants demonstrate a tendency

for oversmoothing. While undersmoothing is not necessarily surprising in ConstantYP

and FluctY (this is the only direction suboptimal behavior can go in), it was ex-ante

unclear how much participants would smooth their consumption in PosIR and FluctP.

This pattern suggests that excess consumption smoothing represents a strategic response

adopted by experienced individuals when navigating complex economic environments.

It resonates with the ‘wait-and-see’ approach, indicating that in scenarios marked by

uncertainty or complexity, the preferred strategy is to maintain the current course of

action, rather than implementing signiﬁcant changes in consumption behavior.

4.2 Measuring Optimization Abilities: Unconditional and Con-

ditional Optimal Index

The distributions of γU (Unconditional Optimal Index) and γC (Conditional Optimal

Index) are shown in Figures 6 and 7, respectively. The distributions are broken down by

repetition and treatment. We separate the 90 to 95 percentage and 95 to 100 percentage

bins to highlight participants’ ability to nearly perfectly optimize, while allowing for the

possibility of rounding.

26

---

<!-- PAGE 29 -->

Figure 6: Histogram of UncOptIndex

These histograms reveal three preliminary observations. First, there are signiﬁcant

optimization errors across all of our treatments, even after signiﬁcant experience.

In

the simplest environment, where incomes and prices are constant and participants have

access to a budgeting calculator, one-quarter of the individuals deviate from the optimal

path by more than 10 percent in Repetition 3. And in more complicated environments

like PosIR and FluctP, deviations are signiﬁcantly more substantial and persistent, re-

gardless of calculator accessibility. Surprisingly, this pattern does not change much for

deviations from the conditional optimal, as shown in Figure 7.

Second, among those at the upper end of the distribution, participants’ abilities to

optimize dynamically—both unconditionally and conditionally—enhance with experi-

ence, particularly in relatively simple environments such as ConstantYP and FluctY.

This improvement is partly attributed to subjects who already had a good understand-

27

---

<!-- PAGE 30 -->

Figure 7: Histogram of CondOptIndex

ing of the problem in the ﬁrst repetition, as they further improved their optimization

skills by the third repetition. Notably, between the ﬁrst and third repetitions, we observe

a signiﬁcant increase of approximately 15 percentage points in the proportion of partici-

pants achieving perfect optimization in ConstantYP, and a 10 percentage point increase

in FluctY. However, in more complex environments like PosIR and FluctP, where the

optimization challenge is greater, the observed eﬀects are comparatively smaller.

Third, the presence of a budgeting calculator signiﬁcantly inﬂuences optimization

in the ConstantYP treatment, more so than in the other treatments, particularly for

participants at the top of the distribution. This eﬀect is less obvious for participants in

the middle or bottom of the distribution. In the ConstantYP environment, the presence

of the budgeting calculator shifts the distribution towards the right, resulting in a 14

percentage point increase in the proportion of participants who achieve perfect optimiza-

28

---

<!-- PAGE 31 -->

tion. However, the beneﬁts provided by the calculator are less pronounced in the other

three environments.

4.3 Evaluation of hypotheses

Table 4 presents the mean deviation of the UncOptIndex (γU ) and CondOptIndex (γC),

measured at the session level for each treatment and repetition. Additionally, we report

the mean deviations for time spent and the number of calculations attempted in the

Calculator treatments. Diﬀerences within and across treatments are documented, with

corrections applied for multiple hypothesis (List et al., 2019).

We ﬁnd compelling evidence to reject Hypothesis 1, which predicts that there should

be no diﬀerence in deviations from both the unconditional and conditional optimal levels

of consumption across diﬀerent environments. Controlling for access to the budget calcu-

lator, both γU and γC are consistently higher in the ConstantYP environment compared

to other treatments across most repetitions. Participants also appear better optimize,

both unconditionally and conditionally, in the FluctY environment than in either PosIR

or FluctP. Notably, PosIR and FluctP exhibit marked similarities, especially when par-

ticipants do not have access to a budgeting calculator. From a broader perspective, the

treatment ordering aligns with Alternative Hypothesis 1 that considers the cognitive

complexity present within the economic environment.

Result 1: The ability to (un)conditionally optimize diﬀers across environments:

γConstantY P > γF luctY > γP osIR = γF luctP .

Our results provide mixed support for Hypothesis 2, which posits that access to

the budgeting calculator signiﬁcantly improves optimization for both unconditional and

conditional consumption decisions. In Repetition 1 and Repetition 3, access to the cal-

culator leads to reductions in mean deviations from the unconditional optimal path by

10.2% and 7.7% in ConstantYP and by 5.8% and 5.9% in PosIR, respectively. Cor-

29

---

<!-- PAGE 32 -->

Repetition 1

γU

γC

Calculator
No Calculator
Diﬀerence

Calculator
No Calculator
Diﬀerence

Calculator

Seconds/period No Calculator

Diﬀerence

No. Sim/period

Calculator

Repetition 2

γU

γC

Calculator
No Calculator
Diﬀerence

Calculator
No Calculator
Diﬀerence

Calculator

Seconds/period No Calculator

Diﬀerence

No. Sim/period

Calculator

Repetition 3

γU

γC

Calculator
No Calculator
Diﬀerence

Calculator
No Calculator
Diﬀerence

Calculator

Seconds/period No Calculator

Diﬀerence

No. Sim/period

Calculator

Table 4: Summary of treatment eﬀects

Treatment

Constant YP Pos IR Fluct Y FluctP

p-value of two sided t-test

[1]

[2]

[3]

[4]

[1] vs [2]

[1] vs [3]

[1] vs [4]

[2] vs [3]

[2] vs [4]

[3] vs [4]

0.862
0.760
0.102∗∗∗

0.859
0.780
0.079∗∗∗

35.569
35.301
0.268

3.705

0.868
0.761
0.107∗∗∗

0.869
0.780
0.089∗∗∗

21.792
17.506
4.286

1.316

0.897
0.820
0.077∗∗∗

0.902
0.836
0.066∗∗∗

20.146
13.118
7.028

1.395

0.718
0.661
0.058∗∗

0.734
0.680
0.054∗∗

51.951
38.615
13.336

0.785
0.778
0.007

0.839
0.826
0.013

37.822
30.600
7.221

0.678
0.621
0.057∗

0.741
0.693
0.049∗∗∗

60.284
47.383
12.901

0.000
0.000

0.000
0.000

0.264
0.616

0.000
0.718

0.038
0.517

0.752
0.647

0.000
0.000

0.000
0.000

0.185
0.046

0.000
0.000

0.000
0.000

0.332
0.654

0.134
0.286

0.758
0.878

0.854
0.666

0.000
0.000

0.000
0.000

0.244
0.000

5.046

4.060

4.162

0.871

0.966

0.953

0.944

0.958

0.922

0.701
0.673
0.028

0.713
0.677
0.035

37.784
18.736
19.048

0.794
0.822
-0.028

0.849
0.858
-0.008

25.208
18.925
6.283

0.680
0.649
0.031

0.736
0.705
0.031

34.988
31.530
3.458

0.000
0.000

0.000
0.000

0.421
0.856

0.000
0.000

0.602
0.000

0.604
0.830

0.000
0.000

0.000
0.000

0.038
0.000

0.000
0.000

0.000
0.000

0.534
0.942

0.556
0.536

0.507
0.425

0.770
0.002

0.000
0.000

0.000
0.000

0.215
0.012

2.621

2.108

1.573

0.510

0.459

0.961

0.986

0.790

0.920

0.761
0.702
0.059∗∗∗

0.766
0.708
0.059∗

29.726
15.518
14.209

0.829
0.840
-0.011

0.875
0.888
-0.013

22.263
16.821
5.442

0.703
0.680
0.023

0.760
0.728
0.032

29.771
21.637
8.134

0.000
0.000

0.000
0.000

0.387
0.527

0.000
0.567

0.210
0.000

0.905
0.130

0.000
0.000

0.000
0.000

0.269
0.000

0.000
0.000

0.000
0.000

0.532
0.482

0.000
0.603

0.887
0.471

0.994
0.021

0.000
0.000

0.000
0.000

0.432
0.123

2.075

1.785

1.478

0.910

0.953

0.974

0.976

0.944

0.972

p-value of two sided t-test (comparisons across repetitions)

Calculator

No Calculator

Constant YP Pos IR Fluct Y FluctP Constant YP

Pos IR

Fluct Y

FluctP

γu

γc

Seconds/period

No. Sim/period

Rep1 vs Rep 2
Rep1 vs Rep 3
Rep2 vs Rep3

Rep1 vs Rep 2
Rep1 vs Rep 3
Rep2 vs Rep3

Rep1 vs Rep 2
Rep1 vs Rep 3
Rep2 vs Rep3

Rep1 vs Rep 2
Rep1 vs Rep 3
Rep2 vs Rep 3

0.985
0.020
0.024

0.935
0.009
0.093

0.000
0.000
0.246

0.007
0.008
0.965

0.741
0.036
0.000

0.650
0.204
0.011

0.613
0.081
0.755

0.032
0.010
0.865

0.615
0.112
0.189

0.690
0.131
0.315

0.144
0.041
0.769

0.012
0.000
0.914

0.941
0.659
0.702

0.891
0.733
0.671

0.299
0.138
0.775

0.006
0.009
0.823

0.998
0.020
0.024

0.986
0.019
0.005

0.000
0.000
0.246

0.707
0.191
0.556

0.887
0.615
0.470

0.113
0.080
0.696

0.054
0.000
0.663

0.202
0.000
0.135

0.000
0.000
0.753

0.693
0.068
0.568

0.842
0.478
0.737

0.000
0.000
0.098

Notes: The p-values reported are obtained from t-tests and have been corrected for multiple hypothesis testing. Signiﬁcance levels are denoted
as follows: ∗p < 0.1, ∗∗p < 0.05, ∗∗∗p < 0.01

30

---

<!-- PAGE 33 -->

respondingly, the improvements in the conditional optimal path are 7.9% and 6.6% in

ConstantYP, and 5.4% and 5.9% in PosIR for Repetitions 1 and 3. All these diﬀerences

are statistically signiﬁcant at the 5% level. However, the evidence indicates that in the

FluctY and FluctP treatments, the calculator’s availability does not signiﬁcantly impact

the optimization of either unconditional or conditional consumption.

Result 2: Access to a budgeting tool does not consistently improve dynamic optimiza-

tion across environments.

Our ﬁndings indicate a complex interaction between experience and the use of the

budgeting calculator in guiding subjects towards the unconditional and conditional op-

timal consumption paths. This observation challenges Hypothesis 3, which posits that

deviations from these optimal paths should diminish in later repetitions. Our compara-

tive analysis of γU and γC across diﬀerent treatments and between repetitions highlights

inconsistencies in the eﬀects of the calculator. PosIR Calc is the only treatment that

consistently demonstrates improvements in optimization over time. For subjects with

access to the calculator in ConstantYP and FluctY, experience does not signiﬁcantly en-

hance performance. As previously shown, experience appears to primarily beneﬁt those

who were already close to the optimal paths in the ﬁrst repetition. The limited learning

observed over time in calculator treatments may be attributed to subjects gathering

most of their learning during the ﬁrst repetition. While the calculator appears to be

useful in exploring various plans and improves learning within a single repetition, this

improvement does not seem to carry over to subsequent repetitions.

On the other hand, in situations where participants do not have access to a calcula-

tor, there is evidence of learning occurring across multiple repetitions, with the PosIR

treatment again being a notable outlier. This ﬁnding is signiﬁcant for experimental

designs where subjects accumulate interest on savings. Our results show that without

the aid of a calculator, learning from stationary repetitions is limited, emphasizing the

crucial role the budgeting tools can play in enhancing learning.

31

---

<!-- PAGE 34 -->

Result 3: Deviations in consumption from the unconditional and conditional optimal

consumption paths do not consistently decrease with experience, particularly when sub-

jects have access to a budgeting tool.

Our remaining hypotheses that relate to the planning horizon and demographic char-

acteristics are explored in the following sections where we exploit our experiments’ panel

data structure. Before we discuss our ﬁnal hypothesis tests, we divert readers’ attention

to a brief analysis of participants’ usage of the budgeting calculator.

4.4 How Participants Use the Budgeting Calculator

All calculations computed in the budgeting calculator were recorded. This dataset en-

ables an evaluation of how participants engaged with the calculator and the impact of

this engagement on decision-making. We observe ﬁve distinct patterns in how partici-

pants ﬁlled in the budgeting calculator in period t.

1. Complete: All entries between t and T = 10 are inputted in each calculation.

2. Sequential: Entries and calculations are conducted sequentially. Subjects compute

Period t calculations ﬁrst, followed by Periods t and t + 1, and again t, t + 1, t + 2,

until they reach T .

3. Partial: Less than T − t + 1 periods are entered into the calculator.18

4. Current Period: Only Period t consumption is inputted.

5. No Inputs: No calculations are made.

How would a fully forward-looking, perfectly optimizing agent utilize the calculator?

If they understand how to solve the optimization problem, they should not spend time

18This type of behavior has been modeled by Caliendo and Aadland (2007). In their model, forward-
looking individuals solve partial-horizon models. They speculate that such behavior in individuals stems
from factors including “...lack of self-control, ﬁnancial illiteracy, distaste for contemplating old age, or
to avoid ﬁnancial planning costs in an uncertain environment, among others.”

32

---

<!-- PAGE 35 -->

doing any calculations. On the other hand, if they are forward-looking but have diﬃculty

with the computational aspect of the problem, they should submit a complete set of

entries before making their spending decisions. We observe participants complete the

calculator in two ways: either immediately ﬁlling in the calculator entirely before pressing

the Calculate button, or sequentially with at least T − t + 1 calculations, inputting and

calculating one period at a time. This latter approach takes more time but provides

participants an opportunity to saliently observe the impact of each period’s consumption-

saving decision. Participants inputting fewer than T − t + 1 periods into the calculator

are categorized as Partial or Current-Period, and are also referred to as myopic planners.

It is important to note that the subjects in the Calculator treatments are not re-

quired to use the budgeting calculator when making their spending decisions. As shown

in Figure 8, the percentage of subjects who do not activate the calculator increases over

time. There are several reasons for this trend: (i) subjects do not need to make cal-

culations every period to determine the optimal consumption path, especially in simple

environments, (ii) subjects underwent an extensive tutorial and practice period before

starting the experiment, (iii) minor changes in the environments between repetitions

may allow subjects to rely on past repetitions to approximate the optimal approach,

and (iv) subjects may experience fatigue after a few periods. Despite this, roughly one-

half of the subjects submit complete sequences of consumption values at the beginning

of each repetition. This is consistent with subjects understanding that the environment

is deterministic, and in order to calculate the unconditional optimal, they must submit

full sequences. Note that if subjects were to attempt to calculate the conditional opti-

mal solution, they may use the calculator in periods 2 to 10, but there is little evidence

of that. Furthermore, there is a constant share of subjects using the calculator to en-

ter consumption values for the current period (between 5% and 20% depending on the

treatment), with only a few subjects partially or sequentially using the calculator over

time.

Considering the notable decline in calculator usage observed after the initial period

of each repetition, we assign participants to a speciﬁc Calculator Type based solely on

33

---

<!-- PAGE 36 -->

Figure 8: Budgeting Calculator Types Over Time

their calculator usage during the ﬁrst period. The distribution of types is summarized

in Figure 9.

5 Evaluation of optimization

In this section, we formally assess the eﬃcacy of the budgeting calculator in improving

consumer optimization. We examine the impacts of the calculator, its usage, learning

outcomes, and demographic factors using the following comprehensive random-eﬀects

panel regression model for each respective environment:

γi,q,r,t =a + b0Calculator + b1Calculator × CalculatorT ypet=1
i,q,r

+ b2Vi,q,r,t + b3Xi + b4P eriod + b5Repetition + µi + errori,q,r,t,

34

---

<!-- PAGE 37 -->

Figure 9: Budgeting calculator usage types, by treatment and repetition

here, γi,q,r,t represents either U ncOptIndexi,q,r,t or CondOptIndexi,q,r,t. The variable

Calculator is a dummy variable that takes the value of 1 in treatments where the

budgeting calculator is present, and 0 otherwise. Additionally, CalculatorT ypet=1

i,q,r is

a categorical variable categorizing participants into one of ﬁve calculator usage types,

with NoCalc serving as the baseline category.

We include time-varying controls denoted as Vi,q,r,t, which capture various factors

such as the amount of time spent in a given period t (denoted as Minutes Spent) and

the cumulative count of calculations performed by the participant since the beginning

of Repetition 1 (denoted as No. of Calculations). It is important to emphasize that

participants who chose to use the budgeting calculator had the freedom to either search

for the optimal levels or enter any desired consumption values. Therefore, it is crucial to

distinguish between participants who eﬀectively used the calculator to ﬁnd the optimal

levels and those who did not. We deﬁne a participant as able to ﬁnd the optimal

consumption if, when using the calculator, their UncOptIndex and CondOptIndex are

equal to or greater than 0.90 at any point up to period t within the repetition. Thus, we

35

---

<!-- PAGE 38 -->

introduce the binary variables Calc γU and Calc γC, which take the value of 1 if subjects

were able to calculate the optimal consumption levels or 0 otherwise.

Furthermore, time-invariant demographic controls, denoted as Xi, are included to

account for participant characteristics unrelated to decisions made in the experiment.

These include variables such as math background score (ranging from 1 to 9), ﬁnan-

cial literacy score (ranging from 0 to 4), backward induction ability (number of wins in

Race-to-60, ranging from 0 to 8), gender, age, institution, level of education, experience

in previous experiments, risk tolerance, the number of years as a student, and perfor-

mance on control questions. This last variable measures the accuracy and consistency

of responses to a set of incentivized control questions designed to assess understanding

of the experimental setup and procedures.

Repetition = {Rep2, Rep3} is a vector of dummy variables that captures the eﬀects

of learning from experience. P eriod = t is a discrete variable that evaluates how the

length of the planning horizon aﬀects optimization. Lastly, the subject-speciﬁc random

eﬀect is denoted by µi.

5.1

Impact of Calculator Usage on Dynamic Optimization

The estimated coeﬃcient on the Calculator dummy variable, ˆb0, presented in Columns

(1), (4), (7), and (10) of Tables 5 and 6 indicates how the presence of the calculator
aﬀects optimization. To further evaluate Hypothesis 2, we test whether ˆb0 > 0 for each
environment. For both unconditional and conditional optimization, we ﬁnd that ˆb0 is

very small, ranging between 0-4 p.p. and not statistically diﬀerent from zero in any

environment.

In the initial period, participants can signiﬁcantly improve their dynamic optimiza-

tion capabilities by utilizing the calculator. In the simplest environment, ConstantYP,

ﬁlling in the calculator with only the current period (ﬁrst period), either partially or

completely, improves unconditional optimization by approximately 7 to 11 percentage

points (p.p.) and conditional optimization by around 6 to 11 p.p. compared to partici-

36

---

<!-- PAGE 39 -->

pants who do not activate the calculator.

Sequential completion of the calculator resulted in a less sizeable and signiﬁcant

eﬀect. On average, there is only a 4 percentage point improvement for unconditional

Table 5: Dependent Variable: OptUncIndex
Constant YP
(2)

POS IR
(5)

(3)

(4)

(6)

(7)

FluctY
(8)

(9)

Calculator

No. of Calculations

(1)

0.043
(0.04)

-0.000
(0.00)

Calc γU

Minutes Spent

Repetition 2

Repetition 3

Period

Math Level

Backward Induction

Financial Literacy

Gender (1=Female)

Age

Control Questions

Calculator Usage

Current Period

Partial

Sequential

Complete

Constant

Observations

Overall R2

-0.018∗∗∗
(0.00)

0.013
(0.01)
0.056∗∗∗
(0.01)
-0.004∗∗∗
(0.00)

-0.018∗∗∗
(0.00)

0.014
(0.01)
0.058∗∗∗
(0.01)
-0.004∗∗∗
(0.00)

0.017
(0.01)

0.016
(0.01)

0.015
(0.02)

-0.026
(0.04)

-0.002
(0.00)

0.004
(0.01)

0.071∗∗
(0.03)
0.108∗∗∗
(0.03)

0.040
(0.03)
0.079∗∗∗
(0.02)
0.545∗
(0.31)

2640

0.12

0.013
(0.01)

0.015
(0.01)

0.013
(0.02)

-0.033
(0.04)

-0.002
(0.00)

0.005
(0.01)

0.080∗∗∗
(0.03)
0.115∗∗∗
(0.03)
0.047∗
(0.03)
0.087∗∗∗
(0.02)
0.544∗
(0.31)

2640

0.12

0.094∗∗∗
(0.03)
-0.019∗∗∗
(0.00)

0.014
(0.01)
0.059∗∗∗
(0.01)
-0.004∗∗∗
(0.00)

0.013
(0.01)

0.013
(0.01)

0.013
(0.02)

-0.030
(0.04)

-0.002
(0.00)

0.004
(0.01)

0.077∗∗∗
(0.03)
0.090∗∗∗
(0.03)

-0.009
(0.03)

0.023
(0.03)
0.589∗∗
(0.30)

2640

0.14

0.006
(0.04)

-0.001
(0.00)

-0.009∗∗∗
(0.00)

-0.006∗
(0.00)

-0.004
(0.01)
0.039∗∗∗
(0.01)
-0.003∗∗
(0.00)

-0.004
(0.01)
0.039∗∗∗
(0.01)
-0.003∗∗
(0.00)

0.006
(0.01)

0.008
(0.01)

0.003
(0.02)

-0.032
(0.04)

0.006
(0.01)

0.008
(0.01)

0.003
(0.02)

-0.031
(0.04)

0.194∗∗∗
(0.03)
-0.010∗∗∗
(0.00)

-0.005
(0.01)
0.033∗∗∗
(0.01)
-0.003∗∗
(0.00)

0.003
(0.01)

0.003
(0.01)

0.000
(0.02)

-0.035
(0.03)

0.004
(0.00)
0.018∗∗∗
(0.01)

0.004
(0.00)
0.018∗∗∗
(0.01)

0.004
(0.00)
0.016∗∗∗
(0.01)

0.013
(0.04)

-0.000
(0.00)

-0.012∗∗∗
(0.00)
0.027∗∗∗
(0.01)
0.050∗∗∗
(0.01)
-0.006∗∗∗
(0.00)

-0.011∗∗
(0.01)
0.027∗∗∗
(0.01)
0.050∗∗∗
(0.01)
-0.006∗∗∗
(0.00)

0.006
(0.01)

0.003
(0.02)

0.008
(0.02)

0.002
(0.04)

-0.000
(0.00)

0.009
(0.01)

0.006
(0.01)

0.002
(0.02)

0.008
(0.02)

0.001
(0.04)

-0.000
(0.00)

0.009
(0.01)

-0.022
(0.03)
0.047∗
(0.03)
-0.084∗∗∗
(0.03)
0.090∗∗∗
(0.03)

-0.321
(0.33)

2730

-0.020
(0.03)
0.049∗
(0.03)
-0.080∗∗
(0.03)
0.093∗∗∗
(0.02)

-0.321
(0.33)

2730

-0.015
(0.03)
0.061∗∗
(0.03)
-0.179∗∗∗
(0.03)
-0.056∗
(0.03)

-0.178
(0.30)

2730

-0.057∗∗
(0.03)

-0.056∗∗
(0.03)

0.038
(0.03)

0.011
(0.02)

-0.032
(0.02)

0.347
(0.34)

2820

0.038
(0.03)

0.011
(0.02)
-0.033∗
(0.02)

0.334
(0.36)

2820

0.118∗∗∗
(0.02)
-0.012∗∗∗
(0.00)
0.034∗∗∗
(0.01)
0.055∗∗∗
(0.01)
-0.006∗∗∗
(0.00)

0.008
(0.01)

0.004
(0.02)

0.005
(0.02)

-0.001
(0.04)

0.000
(0.00)

0.010
(0.01)

-0.043
(0.03)
0.045∗
(0.03)
-0.054∗∗
(0.02)
-0.097∗∗∗
(0.02)

0.286
(0.35)

2820

(10)

0.014
(0.04)

0.002
(0.00)
0.022∗
(0.01)
0.049∗∗∗
(0.01)
0.004∗∗
(0.00)
0.024∗∗∗
(0.01)

0.013
(0.01)

0.000
(0.02)
-0.062∗
(0.04)

-0.005
(0.00)

-0.006
(0.01)

0.003
(0.03)

0.007
(0.03)

-0.001
(0.03)
0.073∗∗∗
(0.03)

0.832
(0.51)

2790

FluctP
(11)

(12)

0.001
(0.00)

0.001
(0.00)
0.023∗
(0.01)
0.050∗∗∗
(0.01)
0.004∗∗
(0.00)
0.024∗∗∗
(0.01)

0.013
(0.01)

-0.001
(0.02)
-0.063∗
(0.04)

-0.004
(0.00)

-0.006
(0.01)

0.006
(0.03)

0.011
(0.03)

0.002
(0.03)
0.076∗∗∗
(0.02)
0.853∗
(0.51)

2790

0.08

0.105∗∗∗
(0.03)

0.002
(0.00)

0.019
(0.01)
0.044∗∗∗
(0.01)
0.004∗∗
(0.00)
0.022∗∗
(0.01)

0.012
(0.01)

0.001
(0.02)
-0.061∗
(0.03)

-0.005
(0.00)

-0.005
(0.01)

0.018
(0.03)

0.013
(0.03)

-0.039
(0.03)

0.036
(0.03)

0.813
(0.50)

2790

0.09

0.08

0.08

0.13

0.05

0.05

0.09

0.08

Notes: This table displays the outcomes of a random eﬀects panel regression analysis. The regression models incorporate demographic control
variables, including gender, age, prior experimental experience, academic degree, aﬃliated institution, current year of study, and risk tolerance
levels. Additionally, we control for participants’ comprehension of the instructions, by adding the participants’ performance in the control
questions. Standard errors are presented in parentheses. Signiﬁcance levels are denoted as follows: ∗p < 0.1, ∗∗p < 0.05, ∗∗∗p < 0.01

37

---

<!-- PAGE 40 -->

Table 6: Dependent Variable: OptCondIndex
Constant YP
(2)

POS IR
(5)

(4)

(6)

(7)

(3)

FluctY
(8)

(1)

FluctP
(11)

(12)

(9)

(10)

0.012
(0.03)

Calculator

0.037
(0.04)

No. of Calculations

-0.001
(0.00)

Calc γC

Minutes Spent

Repetition 2

Repetition 3

Period

Math Level

Backward Induction

Financial Literacy

Gender (1=Female)

Age

Control Questions

Calculator Usage

Current Period

Partial

Sequential

Complete

Constant

Observations

Overall R2

0.095∗∗∗
(0.02)

-0.003
(0.00)
0.017∗∗
(0.01)
0.061∗∗∗
(0.01)
0.009∗∗∗
(0.00)

0.014
(0.01)

0.012
(0.01)

0.018
(0.02)

-0.036
(0.04)

-0.002
(0.00)

0.006
(0.01)

0.061∗∗∗
(0.02)
0.083∗∗∗
(0.02)

-0.030
(0.02)

0.008
(0.02)

0.404
(0.27)

2640

-0.003
(0.00)
0.015∗
(0.01)
0.059∗∗∗
(0.01)
0.009∗∗∗
(0.00)

-0.001
(0.00)
0.016∗
(0.01)
0.060∗∗∗
(0.01)
0.009∗∗∗
(0.00)

0.017
(0.01)

0.017
(0.01)

0.018
(0.02)

-0.030
(0.04)

-0.001
(0.00)

0.006
(0.01)

0.014
(0.01)

0.016
(0.01)

0.016
(0.02)

-0.036
(0.04)

-0.002
(0.00)

0.007
(0.01)

0.071∗∗∗
(0.02)
0.103∗∗∗
(0.02)

0.019
(0.02)
0.060∗∗∗
(0.02)

0.328
(0.28)

2640

0.077∗∗∗
(0.02)
0.110∗∗∗
(0.02)

0.025
(0.02)
0.067∗∗∗
(0.02)

0.328
(0.28)

2640

0.001
(0.04)

0.001
(0.00)

-0.008
(0.01)
0.033∗∗∗
(0.01)
0.023∗∗∗
(0.00)

0.005
(0.01)

0.007
(0.01)

0.002
(0.02)

-0.018
(0.03)

-0.001
(0.00)

0.003
(0.00)

-0.008
(0.01)
0.033∗∗∗
(0.01)
0.023∗∗∗
(0.00)

0.005
(0.01)

0.007
(0.01)

0.002
(0.02)

-0.017
(0.03)

0.003
(0.00)
0.018∗∗∗
(0.01)

0.003
(0.00)
0.018∗∗∗
(0.01)

0.006
(0.03)
0.051∗∗
(0.03)

-0.049
(0.03)
0.087∗∗∗
(0.02)

-0.448
(0.31)

2730

0.006
(0.03)
0.052∗∗
(0.02)

-0.047
(0.03)
0.089∗∗∗
(0.02)

-0.449
(0.31)

2730

0.070∗∗∗
(0.02)

0.000
(0.00)

-0.005
(0.01)
0.036∗∗∗
(0.01)
0.023∗∗∗
(0.00)

0.006
(0.01)

0.006
(0.01)

0.004
(0.02)

-0.016
(0.03)

0.003
(0.00)
0.016∗∗
(0.01)

0.001
(0.03)
0.044∗
(0.02)
-0.074∗∗
(0.03)
0.067∗∗∗
(0.02)

-0.403
(0.31)

2730

-0.000
(0.04)

-0.000
(0.00)

0.001
(0.00)
0.024∗∗∗
(0.01)
0.047∗∗∗
(0.01)
0.010∗∗∗
(0.00)

0.002
(0.00)
0.024∗∗∗
(0.01)
0.047∗∗∗
(0.01)
0.010∗∗∗
(0.00)

0.004
(0.01)

0.001
(0.01)

0.010
(0.02)

0.002
(0.03)

0.000
(0.00)
0.010∗
(0.01)

0.004
(0.01)

0.001
(0.01)

0.010
(0.02)

0.002
(0.03)

0.000
(0.00)

0.010
(0.01)

0.060∗∗∗
(0.02)

0.001
(0.00)
0.026∗∗∗
(0.01)
0.045∗∗∗
(0.01)
0.009∗∗∗
(0.00)

0.004
(0.01)

0.002
(0.01)

0.012
(0.02)

0.003
(0.03)

0.001
(0.00)
0.010∗
(0.01)

-0.043∗
(0.02)

-0.044∗
(0.02)

-0.046∗∗
(0.02)

0.038
(0.02)

0.015
(0.02)

-0.015
(0.02)

0.227
(0.29)

2820

0.036
(0.02)

0.014
(0.02)

-0.017
(0.02)

0.226
(0.31)

2820

0.031
(0.02)

-0.002
(0.02)
-0.046∗∗
(0.02)

0.217
(0.30)

2820

0.000
(0.00)

0.006∗
(0.00)

0.012
(0.01)
0.037∗∗∗
(0.01)
0.020∗∗∗
(0.00)
0.019∗∗
(0.01)

0.010
(0.01)

0.002
(0.02)
-0.063∗∗
(0.03)

-0.005
(0.00)

-0.007
(0.01)

0.003
(0.03)

-0.017
(0.03)

0.012
(0.03)
0.075∗∗∗
(0.02)
0.852∗
(0.45)

2790

0.12

0.007∗∗∗
(0.00)

0.011
(0.01)
0.036∗∗∗
(0.01)
0.020∗∗∗
(0.00)
0.019∗∗
(0.01)

0.010
(0.01)

0.003
(0.02)
-0.062∗∗
(0.03)

-0.005
(0.00)

-0.007
(0.01)

-0.000
(0.03)

-0.020
(0.03)

0.009
(0.03)
0.072∗∗∗
(0.03)
0.835∗
(0.45)

2790

0.12

0.091∗∗∗
(0.02)
0.006∗∗
(0.00)

0.019
(0.01)
0.041∗∗∗
(0.01)
0.019∗∗∗
(0.00)
0.018∗∗
(0.01)

0.010
(0.01)

0.003
(0.02)
-0.058∗
(0.03)

-0.005
(0.00)

-0.006
(0.01)

0.005
(0.03)

0.000
(0.03)

0.017
(0.03)
0.052∗∗
(0.02)
0.802∗
(0.44)

2790

0.13

0.16

0.16

0.18

0.15

0.15

0.15

0.07

0.07

0.10

Notes: This table displays the outcomes of a random eﬀects panel regression analysis. The regression models incorporate demographic control
variables, including gender, age, prior experimental experience, academic degree, aﬃliated institution, current year of study, and risk tolerance
levels. Additionally, we control for participants’ comprehension of the instructions, by adding the participants’ performance in the control
questions. Standard errors are presented in parentheses. Signiﬁcance levels are denoted as follows: ∗p < 0.1, ∗∗p < 0.05, ∗∗∗p < 0.01

optimization and a 2 percentage point improvement for conditional optimization. These

improvements are not statistically signiﬁcant. By contrast, Complete types experience

a 8 p.p.(6 p.p.) improvement in (un)conditional optimization.

38

---

<!-- PAGE 41 -->

In the PosIR environment, characterized by compounding interest on savings, notable

performance disparities were observed across the diﬀerent Calculator Types. When

participants only complete the consumption decision for the current period, there is no

improvement in optimization. However, the Partial and Complete Calculator Types

show improvements of 5 and 9 percentage points, respectively, in their optimization.

Moreover, imperfectly using the calculator still leads to signiﬁcant improvements in

conditional optimization (Column 6).

Sequential completion does not result in any improvement in conditional optimiza-

tion, and it can actually have a negative impact on unconditional optimization. On

average, participants who sequentially optimize in the ﬁrst period of PosIR end up 8

percentage points further away from the optimal unconditional solution compared to

those who did not use the calculator during the experiment.

The eﬃcacy of the calculator is less pronounced in the FluctY environment. We

do not observe consistent improvements in optimization for the Partial, Sequential, and

Complete Calculator Types. In comparison to the NoCalc type, participants who only

ﬁll in the current period are 6 percentage points further from the optimal unconditional

solution and 4 percentage points further from the optimal conditional solution.

Lastly, in the FluctP environment, the calculator beneﬁts are conﬁned to participants

who complete it fully. The Complete Calculator Types are 7 percentage points closer

to both the optimal unconditional and conditional decisions compared to those who

did not use the calculator. Even if a subject fails to ﬁnd the optimal solution using

the calculator, she still improves her conditional optimization by 5 p.p. by ﬁlling the

calculator in completely.

The speciﬁcations presented in columns (3), (6), (9), and (12) of Tables 5 and 6

include dummy variables Calc γU and Calc γC to control for whether a participant has

eﬀectively used the calculator. The estimates demonstrate that eﬀective usage of the

calculator signiﬁcantly improves subjects’ performance by 10 to 20 percentage points

for the UncOptIndex and 6 and 9 percentage points for the CondOptIndex. These

results robustly support a reﬁned version of Hypothesis 2: eﬀective utilization of a

39

---

<!-- PAGE 42 -->

Table 7: Dependent Variable: OptCondIndex

Constant YP
No Calc Calc
(1)

(2)

Pos IR

No Calc Calc
(3)

(4)

FluctY

No Calc Calc
(5)

(6)

FluctP

No Calc Calc
(7)

(8)

Constant

Repetition 2

Repetition 3

Period

0.720∗∗∗
(0.03)

0.000
(0.01)
0.056∗∗∗
(0.01)
0.011∗∗∗
(0.00)

Observations
Overall R2

1320

0.03

0.815∗∗∗
(0.02)

0.010
(0.01)
0.043∗∗∗
(0.01)
0.008∗∗∗
(0.00)

1320

0.02

0.583∗∗∗
(0.03)

-0.003
(0.01)
0.028∗
(0.01)
0.018∗∗∗
(0.00)

1290

0.04

0.580∗∗∗
(0.02)
-0.021∗
(0.01)
0.032∗∗∗
(0.01)
0.028∗∗∗
(0.00)

1440

0.12

0.774∗∗∗
(0.02)
0.032∗∗∗
(0.01)
0.062∗∗∗
(0.01)
0.010∗∗∗
(0.00)

1380

0.03

0.804∗∗∗
(0.03)

0.010
(0.01)
0.036∗∗∗
(0.01)
0.006∗∗∗
(0.00)

1440

0.01

0.585∗∗∗
(0.03)

0.012
(0.02)
0.035∗∗
(0.02)
0.020∗∗∗
(0.00)

1440

0.04

0.657∗∗∗
(0.02)

-0.005
(0.01)

0.018
(0.01)
0.015∗∗∗
(0.00)

1350

0.03

Notes: This table presents the results of a random eﬀects panel regression. Signiﬁcance levels are denoted as
follows: ∗p < 0.1, ∗∗p < 0.05, ∗∗∗p < 0.01

calculator signiﬁcantly reduces deviations from both unconditional and conditional op-

timal consumption paths. Moreover, the results highlight the importance of carrying

out calculations eﬃciently. Simply entering information into the calculator or doing so

incompletely does not guarantee optimization improvements.

5.2 Experience and length of planning horizon

Our data provides strong support for Hypothesis 4, suggesting that conditional opti-

mization improves as participants plan over shorter time horizons. As detailed in Table

7, which disaggregates our results by treatment, we observe signiﬁcant increases in γc
i,t

over time. In the absence of a calculator, participants in the ConstantYP and FluctY

treatments exhibit improvements of 1.1 percentage points per period. This increase is

even more pronounced in the PosIR and FluctP treatments, at 1.8 p.p. and 2.0 p.p. per

period, respectively. These improvements in conditional optimization range from 9 p.p.

to 19 p.p. when comparing the ﬁrst and ninth periods.

Interestingly, the eﬀects are less pronounced for subjects who have access to a calcu-

lator, except in the Pos IR treatment, where within-repetition improvement is notable.

40

---

<!-- PAGE 43 -->

In this case, there is an improvement of 25 p.p. from period 1 to period 9. This suggests

that the calculator does not signiﬁcantly aid subjects in correcting mistakes and ap-

proaching conditional optimization when the planning horizon is shorter and cognitive

load is reduced. A notable exception to this trend is observed in the PosIR treatment,

a relevant ﬁnding since this type of experiment is commonly conducted. Here, the cal-

culator makes a diﬀerence both for within-repetition and between-repetition learning.

Result 4: Deviations from the conditional optimal consumption path diminish as the

planning horizon shortens. However, this eﬀect is less pronounced when participants use

a calculator. The notable exception to this trend is observed in the Pos IR treatment.

5.3 Demographics

Mathematical training and ﬁnancial literacy are key factors associated with ﬁnancial

sophistication (Lusardi and Mitchell, 2011; Van Rooij et al., 2012). Under Hypothesis

5, we posited that individuals with mathematical proﬁciency would excel in sequential

calculations and logical reasoning, crucial for formulating optimal consumption plans.

Financial literacy complements this by oﬀering a practical framework for applying such

calculations to real-world ﬁnancial decisions, such as assessing future costs and beneﬁts

and understanding the time value of money. These combined skills are presumed to

signiﬁcantly aid individuals in solving intertemporal consumption problems, particularly

through the cognitive process of backward induction, which we explicitly elicited in our

study.

In Tables B.1 and B.2 in Appendix B, we examine each treatment individually to

identify whether the presence of the calculator interacts with demographic characteris-

tics. Our results provide little support for Hypothesis 5. Our ﬁndings indicate that in-

dividual characteristics do not consistently aﬀect subjects’ ability to solve intertemporal

41

---

<!-- PAGE 44 -->

consumption problems. No signiﬁcant eﬀects were observed based on other demographic

variables such as gender or age. Higher ﬁnancial literacy leads to a large and signiﬁcant

improvement in optimization in ConstantYP-NoCalc (8-9 p.p. improvement per correct

answer), but not in any other treatment. Stronger backward-induction skills are associ-

ated with better unconditional optimization in ConstantYP-Calc, but no improvements

elsewhere.

Finally, mathematical training has quite a large eﬀect on FluctP-Calc respondents’

unconditional and conditional optimization. Unconditional optimization is 3.5 p.p.

higher for each additional level of mathematical training. We observe a 3.5 × 8 =

28 p.p. diﬀerence between those studying in the most mathematically-intensive degrees

and those with the least mathematically-intensive degrees (there are 9 categories, so a

diﬀerence of 8 math levels). In terms of conditional optimization, we observe a 2.8 × 8

= 22.4 p.p. diﬀerence. Again, this trait does not lead to signiﬁcantly higher levels of

optimization in other treatments.

We are also left intrigued by the ﬁnding that mathematical training does not sig-

niﬁcantly inﬂuence optimization in the PosIR treatment. This is at odds with previous

literature that underscores the correlation between mathematical skill and the ability to

compute compounding returns.An explanation for the inconsistent demographic eﬀects

could be the leveling eﬀect of our extensive training phase before the experiment, which

included a thorough 30-minute instruction session. This training may have equalized

the playing ﬁeld among subjects with varied backgrounds.

Result 5: Individual and demographic characteristics do not have a consistent eﬀect

across economic environments on optimization ability.

6 A Model of Short-Span Planning

A primary reason for sub-optimal consumption plans is short planning horizons. This

phenomenon can be rigorously analyzed by reﬁning our existing economic model. In this

42

---

<!-- PAGE 45 -->

revised model, individuals aim to maximize

subject to:

max
ct

H
(cid:88)

t=1

k

(cid:18) 1

(cid:19)

1 − σ

c1−σ
t

ptct + st = yt + (1 + r)st−1,

(10)

(11)

where H is the horizon, it ranges from 1 to 10. In this context, if H = 10, then

the individual has full foresight (which brings us back to the standard model), and

if H = 1, the model predicts behavior that aligns with the Hand-to-Mouth heuristic,

where individuals consume their income immediately without saving for the future. The

implications of diﬀerent planning horizons are presented in Table C.1 in the Appendix,

which outlines the predicted consumption level in Period 1 by treatment and planning

horizon.

Our focus here is on PosIR because, in the rest of the treatments, the planning

horizon does not signiﬁcantly aﬀect the optimal level of consumption. In ConstantYP,

the optimal consumption level is unaﬀected by the planning horizon, while in FluctY

and FluctP, the primary diﬀerence arises between individuals who plan exclusively for

the current period and those who consider future periods. Additionally, if H is an even

number, the optimal consumption in Period 1 aligns with the solution for a full-span

planner.

In PosIR, the model suggests that individuals maximize the beneﬁts of interest rates

by extending the planning horizon. Notably, as the planning horizon is longer, consump-

tion in Period 1 diminishes, underscoring the signiﬁcance of early savings. We leverage

our model’s predictive power to ascertain a speciﬁc planning horizon for each subject

based on their observed consumption decisions in the initial period of each repetition.

This builds upon the notion that an individual’s consumption choice is inﬂuenced by

their planning horizon and includes a random error component. The error component,

ε, follows a normal distribution with mean zero and standard deviation σ. Then, by per-

43

---

<!-- PAGE 46 -->

forming a maximum likelihood estimation, we can calculate the distribution of horizons

in the sample and the standard deviation.19

The estimated parameters are shown in Table C.2 in the appendix. In this table,

we note that close to 30% of the observations are not explained by short-span planning

model. Among the observations that can be rationalized by the model, approximately

20% of them would correspond to 1-period planners, around 19% would correspond to

individuals that plan for 2 or 3 periods in advance, over 10% would consider 8 periods,

and close to 10% would use the full horizon.

Additionally, we can cross-validate these model predictions with the actual planning

behaviors observed among the subjects in our experiment. This is possible because we

have collected detailed planning data for each subject in every period, derived from

the usage of the budgeting calculator. To directly compare this data, we examine each

subject’s planning horizon in the ﬁrst period of each repetition by observing how many

entries subjects ﬁlled out in the calculator during each of the trials. Note that they can

ﬁll out as few as one entry and as many as 10 periods (the full horizon).20 Consequently,

in Figure 10, we compare the distribution of planning horizons utilized by subjects

against the model’s predictions detailed in Table C.2.21

19The details can be found in Appendix C.
20In our analysis, we make two adjustments when examining the data. The ﬁrst is that we omit
if a subject incrementally increases the planning horizon by
intermediate plans for sequential users:
clicking the Submit button each time they enter an additional consumption value, we only retain the
ﬁnal (longest) plan. The second adjustment recognizes that in a single period, subjects may use the
calculator to test various potential plans, complicating the analysis as it is unclear which plan they intend
to implement. These plans may even diﬀer in their time horizons. To ensure a balanced evaluation,
we assign equal weight to each participant using the budgeting calculator in each repetition. This
means that every individual’s plan contributes equally to the overall distribution. However, the weight
of a speciﬁc plan is inversely proportional to the frequency of calculator usage by that subject. This
approach mitigates the potential overrepresentation of subjects who are simply exploring the payoﬀ
space, preventing their exploratory attempts from disproportionately aﬀecting the distribution.

21Note that the ﬁrst bar represents subjects who did not utilize the calculator for observed planning
behavior and in terms of the Partial-Horizon model were not categorized. As a robustness check, we
implemented an alternative method by taking consumption values from period 1 in each repetition and
comparing them with ten possible consumption values based on the predictions of our model, each
corresponding to a diﬀerent planning horizon. For each horizon, we calculated the squared deviations
between the observed consumption ﬁgures and the model’s predicted values. The horizon with the small-
est squared deviation was identiﬁed as the closest to the subject’s observed consumption behavior. If
these deviations fell below a certain threshold, the consumption pattern was classiﬁed as uncategorized.
This approach’s outcomes did not signiﬁcantly diﬀer from our main analysis ﬁndings.

44

---

<!-- PAGE 47 -->

Figure 10: Comparison between the pre-
dicted and the observed horizon

Figure 10 demonstrates that the model accurately forecasts the frequency with which

a one-period planning horizon is employed. However, it underestimates the use of the

full planning horizon; the model predicts its occurrence at around 10%, whereas, in

reality, subjects choose this option nearly half of the time. Furthermore, the model’s

prediction of a 12% utilization rate for an 8-period planning horizon starkly contrasts

with the actual trials, where this horizon is selected in less than 1% of instances. This

notable discrepancy prompts a conjectural explanation: subjects who are aware of the

beneﬁts of compounding interest rates, but uncertain about the optimal savings amount,

might resort to a straightforward heuristic. Such a heuristic might involve saving half of

their income, yielding a consumption level of 5 units, closely aligning with the model’s

prediction of 5.13 units for an 8-period planner, as detailed in Table C.1.

7 Discussion

Our study represents one of the ﬁrst attempts to understand the role of environmental

complexity in dynamic optimization, focusing on consumption smoothing. We uncover

that diﬀerent environments pose varying levels of challenges, some more demanding

than others. Particularly, while the complexities associated with compounding interest

rates on savings or ﬂuctuating income are well-acknowledged, the challenges related

45

---

<!-- PAGE 48 -->

to ﬂuctuating prices have been less examined. Our research not only ﬁlls this gap

but also presents new empirical evidence demonstrating that many individuals struggle

with planning over extended periods, a fundamental yet often overlooked assumption of

economic theory.

In exploring these complexities, our experiments reveal that individuals frequently

encounter signiﬁcant hurdles in achieving optimal outcomes, even in seemingly straight-

forward scenarios. These challenges arise not only from the variability of economic

conditions but also from cognitive limitations and numerical diﬃculties inherent in dy-

namic decision-making. Our ﬁndings resonate with existing literature on complexity,

such as the works of Oprea (2022), Enke and Graeber (2019), and Gabaix and Grae-

ber (2023), which conceptualize the mind as a cognitive economy faced with numerous

decisions.

Another key aspect of our study is the potential role of a meticulously designed bud-

geting calculator in aiding decision-making. Our results indicate that the mere availabil-

ity of such a tool does not guarantee its eﬀective use. The eﬀectiveness of a budgeting

tool largely depends on how individuals choose to utilize it. This observation is cru-

cial, as it highlights that providing tools for ﬁnancial planning is beneﬁcial, but their

impact hinges on the user’s engagement and understanding. Furthermore, our analysis

of non-choice data from the budget calculator provides deeper insights into individuals’

strategies, preferences, and decision-making horizons. The integration of robo-advisory

features into this budgeting calculator could enhance its utility. Robo-advisors, by pro-

viding automated, data-driven guidance and personalized ﬁnancial recommendations,

can serve as an active form of nudging, potentially increasing the eﬀectiveness of such

tools. Such integration could transform the calculator from a passive instrument into

a more interactive agent in ﬁnancial planning, nudging users towards optimal ﬁnancial

behaviors tailored to their unique data and preferences.

Crucially, our paper makes a signiﬁcant contribution by directly examining indi-

viduals’ capacity for planning, a core assumption in economic theory often taken for

granted. Standard economic models assume that agents can plan eﬀectively, even for

46

---

<!-- PAGE 49 -->

long horizons, which is essential for making optimal present choices. However, empir-

ical evidence supporting this assumption, particularly from laboratory experiments, is

scarce.22 Our work stands as one of the ﬁrst to provide concrete evidence of individuals’

planning abilities—or the lack thereof—by directly observing their plans. This approach

diﬀers markedly from indirect methods using decision trees (see Hey 2002), which infer

planning from decision outcomes. Expanding upon this concept, we can even compare

observed planning-horizons to implied horizons from a short-span horizon model. This

analysis leads us to rule out the short-span model in positive interest rate environments,

pointing towards a broader issue in achieving optimal paths than just the incapacity for

long-term planning.

It is important to emphasize that real-world settings present even greater challenges

for dynamic optimization. The unpredictability of real life, combined with unexpected

events and incomplete information, complicates decision-making. Individuals often pur-

sue multiple goals and are inﬂuenced by behavioral biases like overconﬁdence, loss aver-

sion, and procrastination. Therefore, the deviations from the optimal path observed in

our controlled experiments should be viewed as a lower bound. In more complex real-

world scenarios, these deviations are expected to increase, highlighting the necessity

for strong ﬁnancial planning tools and improved ﬁnancial literacy to help individuals

navigate these challenges eﬀectively.

Looking forward, our study opens several avenues for future research. Investigating

dynamic optimization under diverse conditions such as uncertainty, social learning inﬂu-

ences, expected liquidity constraints, and current binding constraints could enhance our

understanding of decision-making complexities. Further studies on the eﬀects of intro-

ducing and removing budget calculators and the sustained impact of ﬁnancial literacy

initiatives will provide deeper insights into how these tools and educational interventions

aﬀect consumer behavior.

In terms of policy implications, our ﬁndings on suboptimal decision-making due to

22One exception is planning in the context of present bias and procrastination (see Della Vigna and

Malmendier 2006).

47

---

<!-- PAGE 50 -->

cognitive complexity, especially under ﬂuctuating prices, suggest an added layer of wel-

fare loss beyond traditional concerns like menu costs and relative price dispersion in

inﬂationary contexts. These insights highlight the potential for cognitive errors to exac-

erbate welfare losses in realistic settings, thus underscoring the importance of simplifying

ﬁnancial decision environments and improving ﬁnancial literacy.

48

---

<!-- PAGE 51 -->

References

Ballinger, T., M. Palumbo, and N. Wilcox (2003): “Precautionary Savings and

Social Learning Across Generations: An Experiment,” The Economic Journal, 113,

920–947.

Ballinger, T. P., E. Hudson, L. Karkoviata, and N. T. Wilcox (2011): “Sav-

ing Behavior and Cognitive Abilities,” Experimental Economics, 14, 349–374.

Bosch-Rosa, C., T. Meissner, and A. Bosch-Dom`enech (2018): “Cognitive

bubbles,” Experimental Economics, 21, 132–153.

Brown, A., E. Chua, and C. Camerer (2009): “Learning and Visceral Temptation

in Dynamic Saving Experiments,” Quarterly Journal of Economics, 124, 197–231.

Caliendo, F. and D. Aadland (2007): “Short-term planning and the life-cycle

consumption puzzle,” Journal of Economic Dynamics and Control, 31, 1392–1415.

Caplin, A., M. Dean, and D. Martin (2011): “Search and satisﬁcing,” American

Economic Review, 101, 2899–2922.

Carbone, E. and J. Duffy (2014): “Lifecycle Consumption Plans, Social Learn-

ing and External Habits: Experimental Evidence,” Journal of Economic Behavior &

Organization, 106, 413–427.

Carbone, E., K. Georgalos, and G. Infante (2019): “Individual vs. Group

Decision-Making: An Experiment on Dynamic Choice under Risk and Ambiguity,”

Theory and decision, 87, 87–122.

Carbone, E. and J. Hey (2004): “The Eﬀect of Unemployment on Consumption:

An Experimental Analysis,” The Economic Journal, 114, 660–683.

Carbone, E. and G. Infante (2015): “Are Groups Better Planners than Individuals?

An Experimental Analysis,” Journal of Behavioral and Experimental Economics, 57,

112–119.

49

---

<!-- PAGE 52 -->

D’Acunto, F. and A. G. Rossi (2023): “Robo-advice: Transforming households into

rational economic agents,” Annual Review of Financial Economics, 15, 543–563.

D’Acunto, F., A. G. Rossi, and M. Weber (2023): “Crowdsourcing peer informa-

tion to change spending behavior,” Chicago Booth Research Paper.

Della Vigna, S. and U. Malmendier (2006): “Paying not to go to the gym,”

american economic Review, 96, 694–719.

Duffy, J. (2016): “Macroeconomics: A Survey of Laboratory Research,” Handbook of

Experimental Economics, Volume 2.

Duffy, J. and Y. Li (2019): “Lifecycle consumption under diﬀerent income proﬁles:

Evidence and theory,” Journal of Economic Dynamics and Control, 104, 74–94.

Duffy, J. and A. Orland (2023): “Liquidity Constraints, Income Variance, and

Buﬀer Stock Savings: Experimental Evidence,” Working Paper.

D’Acunto, F., N. Prabhala, and A. G. Rossi (2019): “The promises and pitfalls

of robo-advising,” The Review of Financial Studies, 32, 1983–2020.

D’Acunto, F. and M. Weber (2022): “Memory and beliefs: Evidence from the

ﬁeld,” Georgetown University and University of Chicago Working Paper.

Eckel, C. C. and P. J. Grossman (2002): “Sex Diﬀerences and Statistical Stereo-

typing in Attitudes Toward Financial Risk,” Evolution and Human Behavior, 23,

281–295.

Enke, B. and T. Graeber (2019): “Cognitive uncertainty,” Tech. rep., National

Bureau of Economic Research.

Enke, B., T. Graeber, and R. Oprea (2023): “Complexity and Time,” Tech. rep.,

National Bureau of Economic Research.

Fenig, G., G. Gallipoli, and Y. Halevy (2022): “Piercing the’Payoﬀ Function’

Veil: Tracing Beliefs and Motives,” Working Paper.

50

---

<!-- PAGE 53 -->

Fischbacher, U. (2007): “z-Tree: Zurich Toolbox for Ready-Made Economic Experi-

ments,” Experimental Economics, 10, 171–78.

Gabaix, X. (2014): “A sparsity-based model of bounded rationality,” The Quarterly

Journal of Economics, 129, 1661–1710.

Gabaix, X. and T. Graeber (2023): “The Complexity of Economic Decisions,”

Available at SSRN.

Hey, J. and V. Dardanoni (1988): “Optimal Consumption Under Uncertainty: An

Experimental Investigation,” The Economic Journal, 98, 105–116.

Hey, J. D. (2002): “Experimental economics and the theory of decision making under

risk and uncertainty,” The Geneva Papers on Risk and Insurance Theory, 27, 5–21.

Ilut, C. and R. Valchev (2023): “Economic agents as imperfect problem solvers,”

The Quarterly Journal of Economics, 138, 313–362.

Krosnick, J. A. (1991): “Response strategies for coping with the cognitive demands

of attitude measures in surveys,” Applied cognitive psychology, 5, 213–236.

Laibson, D. (1997): “Golden eggs and hyperbolic discounting,” The Quarterly Journal

of Economics, 112, 443–478.

Li, Y. (2024): “Do Tax Deferred Accounts Improve Lifecycle Savings? Experimental

Evidence,” Review of Economics and Statistics, forthcoming.

List, J. A., A. M. Shaikh, and Y. Xu (2019): “Multiple hypothesis testing in

experimental economics,” Experimental Economics, 22, 773–793.

Loewenstein, G. and D. Prelec (1992): “Anomalies in intertemporal choice: Evi-

dence and an interpretation,” The Quarterly Journal of Economics, 107, 573–597.

Lu, K. (2022): “Overreaction to capital taxation in saving decisions,” Journal of Eco-

nomic Dynamics and Control, 144, 104541.

51

---

<!-- PAGE 54 -->

Luhan, W. J., M. W. Roos, and J. Scharler (2014): “An Experiment on Con-

sumption Responses to Future Prices and Interest Rates,” in Experiments in macroe-

conomics, Emerald Group Publishing Limited, 139–166.

Lusardi, A. and O. Mitchell (2007): “Financial Literacy and Retirement Planning:

New Evidence from the Rand American Life Panel,” NBER Working Paper.

Lusardi, A. and O. S. Mitchell (2011): “Financial literacy and planning: Impli-

cations for retirement wellbeing,” .

Lusardi, A. and D. Wallace (2013): “Financial literacy and quantitative reasoning

in the high school and college classroom,” Numeracy, 6, 1.

Ma´ckowiak, B. and M. Wiederholt (2015): “Business cycle dynamics under ra-

tional inattention,” The Review of Economic Studies, 82, 1502–1532.

Meissner, T. (2016): “Intertemporal Consumption and Debt Aversion: An Experi-

mental Study,” Experimental Economics, 19, 281–298.

Miller, L. and R. Rholes (2023): “Joint vs. Individual performance in a dynamic

choice problem,” Journal of Economic Behavior & Organization, 212, 897–934.

Modigliani, F. and R. Brumberg (1954): “Utility Analysis and the Consumption

Function: An Interpretation of Cross Section Data,” in Post Keynesian Economics,

ed. by K.K.Kurihara, Ruthers University Press New Brunswick New Jersey, vol. 1,

388–436.

O’Donoghue, T. and M. Rabin (1999): “Doing it now or later,” American Economic

Review, 89, 103–124.

Oprea, R. (2022): “Simplicity equivalents,” Working Paper.

Schipper, B. C. (2014): “Unawareness—a gentle introduction to both the literature

and the special issue,” Mathematical Social Sciences, 70, 1–9.

52

---

<!-- PAGE 55 -->

Simon, H. A. (1956): “Rational choice and the structure of the environment.” Psycho-

logical review, 63.

Sims, C. A. (2003): “Implications of rational inattention,” Journal of monetary Eco-

nomics, 50, 665–690.

Van Rooij, M. C., A. Lusardi, and R. J. Alessie (2012): “Financial literacy,

retirement planning and household wealth,” The Economic Journal, 122, 449–478.

Woodford, M. (2019): “Monetary policy analysis when planning horizons are ﬁnite,”

NBER macroeconomics annual, 33, 1–50.

Yamamori, T., K. Iwata, and A. Ogawa (2018): “Does money illusion matter in

intertemporal decision making?” Journal of Economic Behavior & Organization, 145,

465 –473.

53

---

<!-- PAGE 56 -->

A Taylor Expansion for Optimal Choice

In this section, we apply a Taylor expansion to the optimal consumption choice for period

1, as speciﬁed in Equation 6. This analysis adheres to the methodology delineated

by Gabaix and Graeber (2023) in their study of complexity. Let ˆyt = yt − y1 and

ˆpt = pt − p1, and assume that ˆyt and ˆpt are negligibly small. Consequently, we can

(12)

(13)

reformulate Equation 6.

c1 =

(cid:18)

(cid:80)T

t=1

y1

(1+r)t−1 + (cid:80)T
(cid:18)

t=2
(cid:16) ˆpt+p1
(1+r)t−1

p1 + p

1
σ
1

(cid:80)T

t=2

ˆyt
(1+r)t−1
(cid:17) σ−1

σ

(cid:19)(cid:19)

We begin by evaluating c1 when ˆyt = 0, r = 0 and ˆpt = 0

c1 =

p1 + p

(cid:16)

1
σ
1

T y1

(T − 1) p

σ−1
σ

1

(cid:17) =

y1
p1

Then we calculate ∂c1
∂ ˆyt

and evaluate it when ˆyt = 0, r = 0 and ˆpt = 0

∂c1
∂ ˆyt

=

(cid:18)

p1 + p

1
σ
1

(cid:104)

(cid:80)T

t=1

(cid:18)

(cid:80)T

t=2

(cid:105)

1
(1+r)t−1
(cid:16) ˆpt+p1
(1+r)t−1

(cid:17) σ−1

σ

(cid:19)(cid:19)

1
σ−1
σ

1

(cid:16)
p

1
σ
1

(cid:17)

(T − 1)

=

=

p1 + p
1
T p1

We then calculate ∂c1

∂r and evaluate it when ˆyt = 0, r = 0 and ˆpt = 0

54

---

<!-- PAGE 57 -->

∂c1
∂r

= −

(cid:16)

y1

(cid:17)
(cid:80)T −1
t=1 t

y1

(cid:80)T −1
t=1 t

T p1 +

(cid:16)(cid:0) 1−σ
σ
T 2p2
1

(cid:1) p1

(cid:80)T −1
t=1 t

(cid:17)

T y1

=

= −

T p1σ
−y1(T −1)(T )
2
T p1σ
y1 (T − 1)
2σp1

=

= −

Finally we calculate ∂c1
∂ ˆpt

and evaluate it when ˆyt = 0, r = 0 and ˆpt = 0

(cid:16)(cid:80)T

t=1

∂c1
∂ ˆpt

= −

1

(cid:17)
(1+r)t−1 ( ˆyt + y1)
(cid:18)

(cid:18)

p1 + p

1
σ
1

(cid:80)T

t=2

(cid:16) ˆpt+p1
(1+r)t−1

(cid:17) σ−1

σ

(cid:19)(cid:19)2

(cid:18)

(cid:0) σ−1
σ

(cid:1) (cid:16) ˆpt+p1
(1+r)

1
σ
1

p

(cid:17)− 1

σ

(cid:19)

= −

T y1

(cid:1)

(cid:0) σ−1
σ
T 2p2
1

=

(cid:18) 1 − σ
σ

(cid:19) y1
T p2
1

Thus, the Taylor expansion is

c1 =

y1
p1

+

1
T p1

T
(cid:88)

t=2

ˆyt −

y1 (T − 1)
2σp1

r +

(cid:18) 1 − σ
σ

(cid:19) y1
T p2
1

T
(cid:88)

t=2

ˆpt

(14)

55

---

<!-- PAGE 58 -->

B Additional Regressions

Calc
(12)

0.001
(0.00)
0.105∗∗∗
(0.02)

-0.002
(0.00)

-0.001
(0.02)

0.018
(0.02)

0.002
(0.00)
0.035∗∗
(0.01)

0.028
(0.02)

-0.011
(0.02)

-0.001
(0.01)

0.013
(0.03)

-0.003
(0.03)
-0.063∗
(0.03)

0.013
(0.03)

0.526
(0.67)

1350
0.16

Table B.1: Dependent Variable: OptUncIndex
Constant YP
Calc
(2)

Pos IR
Calc
(5)

No Calc
(7)

No Calc
(4)

Calc
(3)

Calc
(6)

FluctY
Calc
(8)

No Calc
(1)

Calc
(9)

No Calc
(10)

FluctP
Calc
(11)

No of Calculations

Calc γU

Minutes Spent

Repetition 2

Repetition 3

Period

Math Level

Backward Induction

Financial Literacy

Control Questions

Calculator Usage

Current Period

Partial

Sequential

Complete

Constant

Observations
Overall R2

-0.037∗∗∗
(0.01)

-0.010
(0.02)
0.047∗∗∗
(0.02)
-0.010∗∗∗
(0.00)

0.040
(0.02)

-0.001
(0.02)
0.092∗∗
(0.04)

-0.003
(0.01)

0.677
(0.48)

1320
0.15

-0.012∗∗∗
(0.00)
0.036∗∗∗
(0.01)
0.065∗∗∗
(0.01)

0.001
(0.00)

0.009
(0.01)
0.042∗∗
(0.02)

-0.018
(0.02)

0.005
(0.01)

0.074∗∗∗
(0.02)
0.122∗∗∗
(0.02)
0.051∗∗
(0.02)
0.088∗∗∗
(0.02)

0.601
(0.44)

1320
0.16

-0.001
(0.00)
0.093∗∗∗
(0.02)
-0.010∗
(0.00)
0.038∗∗∗
(0.01)
0.069∗∗∗
(0.01)

0.001
(0.00)

0.007
(0.01)
0.036∗
(0.02)

-0.017
(0.02)

0.003
(0.01)

0.075∗∗∗
(0.02)
0.102∗∗∗
(0.03)

-0.000
(0.03)

0.029
(0.02)
0.662∗
(0.40)

1320
0.21

-0.001
(0.00)
0.213∗∗∗
(0.02)

-0.005
(0.00)

-0.019
(0.01)
0.025∗
(0.01)

-0.000
(0.00)
-0.016∗
(0.01)

0.005
(0.01)

-0.020
(0.02)
0.020∗∗∗
(0.01)

-0.001
(0.00)
0.115∗∗∗
(0.02)

-0.007
(0.01)
0.023∗
(0.01)
0.047∗∗∗
(0.01)
-0.009∗∗∗
(0.00)

0.005
(0.01)

-0.007
(0.02)

-0.013
(0.04)

0.014
(0.01)

0.011
(0.01)
0.031∗
(0.02)
0.063∗∗∗
(0.02)
0.006∗∗
(0.00)

0.015
(0.01)

-0.002
(0.03)

0.021
(0.03)

0.006
(0.02)

-0.011
(0.01)
0.042∗∗∗
(0.01)
0.059∗∗∗
(0.01)
-0.003∗
(0.00)

-0.005
(0.02)

0.024
(0.02)

0.034
(0.03)

0.007
(0.01)

-0.014∗∗∗
(0.00)

0.007
(0.01)
0.035∗∗∗
(0.01)
-0.009∗∗∗
(0.00)

0.004
(0.01)

-0.004
(0.03)

-0.012
(0.04)

0.012
(0.01)

-0.008
(0.01)

-0.009∗∗∗
(0.00)

0.010
(0.01)
0.038∗∗∗
(0.01)
-0.006∗∗∗
(0.00)

0.007
(0.02)

-0.015
(0.03)

0.022
(0.03)

0.013
(0.01)

-0.019
(0.01)
0.037∗∗
(0.01)

0.000
(0.00)

-0.015
(0.01)

0.015
(0.01)

-0.013
(0.03)
0.021∗∗
(0.01)

-0.028
(0.03)

0.035
(0.03)
-0.089∗∗∗
(0.03)
0.081∗∗∗
(0.02)

-0.360
(0.39)

1440
0.14

-0.006
(0.03)
0.052∗∗
(0.03)
-0.176∗∗∗
(0.03)
-0.086∗∗∗
(0.03)

-0.203
(0.24)

1440
0.26

0.267
(0.51)

1380
0.10

-0.068∗∗
(0.03)

-0.049∗
(0.03)

0.016
(0.03)

-0.005
(0.02)
-0.048∗∗
(0.02)

0.432
(0.53)

1440
0.05

0.038
(0.03)
-0.056∗∗
(0.02)
-0.099∗∗∗
(0.03)

0.266
(0.52)

1440
0.14

0.311
(1.10)

1440
0.07

-0.122
(0.73)

1290
0.05

-0.000
(0.00)

0.005
(0.02)

0.029
(0.02)

0.002
(0.00)
0.041∗∗∗
(0.01)

0.027
(0.02)

-0.012
(0.02)

0.002
(0.01)

-0.002
(0.03)

-0.007
(0.03)

-0.022
(0.03)
0.053∗
(0.03)

0.358
(0.68)

1350
0.14

Notes: This table displays the outcomes of a random eﬀects panel regression analysis. The regression models incorporate demographic
control variables, including gender, age, prior experimental experience, academic degree, aﬃliated institution, current year of study, and
risk tolerance levels. Additionally, we control for participants’ comprehension of the instructions, by adding the participants’ performance
in the control questions. Standard errors are presented in parentheses. Signiﬁcance levels are denoted as follows: ∗p < 0.1, ∗∗p < 0.05,
∗∗∗p < 0.01.

56

---

<!-- PAGE 59 -->

Table B.2: Dependent Variable: OptCondIndex

Constant YP
Calc
(2)

No Calc
(1)

Calc
(3)

No Calc
(4)

Pos IR
Calc
(5)

Calc
(6)

No Calc
(7)

FluctY
Calc
(8)

No of Calculations

Calc γC

Minutes Spent

Repetition 2

Repetition 3

Period

Math Level

Backward Induction

Financial Literacy

Control Questions

Calculator Usage

Current Period

Partial

Sequential

Complete

Constant

Observations
Overall R2

-0.001
(0.00)
0.112∗∗∗
(0.02)

-0.004
(0.00)
0.062∗∗∗
(0.01)
0.080∗∗∗
(0.01)
0.006∗∗∗
(0.00)

0.012
(0.01)

0.026
(0.02)

-0.009
(0.02)

0.006
(0.01)

0.008
(0.02)
0.050∗∗
(0.02)
-0.043∗
(0.02)

-0.003
(0.02)

0.468
(0.45)

1320

0.21

0.001
(0.00)
0.052∗∗∗
(0.01)

-0.003
(0.00)

-0.005
(0.01)
0.044∗∗∗
(0.01)
0.028∗∗∗
(0.00)

-0.010
(0.01)

0.009
(0.01)

0.000
(0.00)

-0.014
(0.01)
0.037∗∗∗
(0.01)
0.028∗∗∗
(0.00)

-0.012
(0.01)

0.011
(0.01)

-0.020
(0.02)
0.022∗∗∗
(0.01)

-0.019
(0.02)
0.021∗∗∗
(0.01)

0.004
(0.03)
0.048∗
(0.03)

-0.049
(0.03)
0.084∗∗∗
(0.02)

-0.557
(0.36)

1440

0.24

0.003
(0.03)
0.043∗
(0.03)
-0.058∗
(0.03)
0.075∗∗∗
(0.02)

-0.517
(0.36)

1440

0.26

0.008
(0.01)

-0.000
(0.01)
0.031∗∗
(0.01)
0.018∗∗∗
(0.00)

0.006
(0.02)

-0.009
(0.03)

0.027
(0.03)

0.011
(0.01)

-0.159
(0.68)

1290

0.08

0.002
(0.01)

0.001
(0.01)
0.057∗∗∗
(0.01)
0.011∗∗∗
(0.00)
0.041∗
(0.02)

0.001
(0.02)
0.084∗∗
(0.03)

0.000
(0.01)

0.285
(0.42)

1320

0.19

-0.005∗
(0.00)
0.034∗∗∗
(0.01)
0.067∗∗∗
(0.01)
0.007∗∗∗
(0.00)

0.012
(0.01)

0.036
(0.02)

-0.009
(0.03)

0.006
(0.01)

0.074∗∗∗
(0.02)
0.116∗∗∗
(0.02)

0.028
(0.02)
0.069∗∗∗
(0.02)

0.481
(0.47)

1320

0.17

Calc
(9)

-0.001
(0.00)
0.032∗
(0.02)

-0.001
(0.01)

0.014
(0.01)
0.030∗∗
(0.01)
0.005∗∗∗
(0.00)

-0.004
(0.01)

-0.008
(0.02)

-0.003
(0.03)

0.014
(0.01)

-0.006
(0.01)
0.031∗∗∗
(0.01)
0.061∗∗∗
(0.01)
0.009∗∗∗
(0.00)

-0.008
(0.01)

0.014
(0.02)

0.038
(0.03)

0.006
(0.01)

-0.005
(0.00)

0.008
(0.01)
0.030∗∗
(0.01)
0.006∗∗∗
(0.00)

-0.003
(0.01)

-0.009
(0.02)

-0.004
(0.03)
0.014∗
(0.01)

-0.062∗∗
(0.02)

-0.075∗∗∗
(0.03)

0.000
(0.03)

-0.001
(0.02)
-0.039∗
(0.02)

0.340
(0.44)

1440

0.09

-0.025
(0.03)

-0.013
(0.02)
-0.057∗∗
(0.02)

0.357
(0.44)

1440

0.10

0.388
(0.43)

1380

0.09

No Calc
(10)

FluctP
Calc
(11)

0.019∗∗∗
(0.01)

0.017
(0.02)
0.043∗∗∗
(0.02)
0.022∗∗∗
(0.00)

0.013
(0.01)

-0.005
(0.02)

0.020
(0.03)

0.002
(0.02)

0.473
(0.99)

1440

0.10

0.002
(0.00)

0.005
(0.02)
0.030∗
(0.02)
0.016∗∗∗
(0.00)
0.035∗∗∗
(0.01)

0.021
(0.02)

-0.009
(0.02)

0.000
(0.01)

-0.001
(0.03)

-0.021
(0.03)

0.006
(0.03)
0.061∗∗
(0.03)

0.447
(0.56)

1350

0.17

Calc
(12)

0.001
(0.00)
0.057∗∗∗
(0.02)

-0.001
(0.00)

0.017
(0.02)
0.041∗∗
(0.02)
0.014∗∗∗
(0.00)
0.031∗∗∗
(0.01)

0.023
(0.01)

-0.009
(0.02)

0.000
(0.01)

-0.025
(0.03)

-0.022
(0.03)

0.009
(0.03)
0.051∗
(0.03)

0.440
(0.53)

1350

0.18

Notes: This table displays the outcomes of a random eﬀects panel regression analysis. The regression models incorporate demographic
control variables, including gender, age, prior experimental experience, academic degree, aﬃliated institution, current year of study, and
risk tolerance levels. Additionally, we control for participants’ comprehension of the instructions, by adding the participants’ performance
in the control questions. Standard errors are presented in parentheses. Signiﬁcance levels are denoted as follows: ∗p < 0.1, ∗∗p < 0.05,
∗∗∗p < 0.01.

57

---

<!-- PAGE 60 -->

C Short-Span Planning Model’s Estimation

Our methodology relies on the notion that an individual’s initial consumption choice

is inﬂuenced by their planning horizon and includes a random error component. This

error component, denoted as ε, follows a normal distribution with a mean of zero and a

standard deviation of σ. Therefore, the actual consumption choice for a speciﬁc planning

horizon, denoted by cH, is given by: cH = cH + ε, where H varies from 1 to 10 and cH

represents the theoretically optimal consumption level in Period 1 for the respective

H. Additionally, we consider the possibility that a subset of subjects may make their

consumption choices randomly. We model this by assuming that these subjects’ decisions

follow a uniform distribution ranging from 0 to 10. As a result, our model considers the

population to comprise H + 1 distinct planner types, each characterized by a proportion

ph for h in the range of [0,10].

To deﬁne a log-likelihood function, we integrate these proportions with the corre-

sponding conditional densities. This methodology enables the computation of the sam-

ple log-likelihood for the n observations in our dataset. The log-likelihood function is

expressed as follows:

LogL =

(cid:34)

n
(cid:88)

i=1

ln

ˆp0
100

+

10
(cid:88)

h=1

1
σ

φ

(cid:18) ci,R − c∗
ˆσ

H

ˆph

(cid:19)(cid:35)

,

where ci,R represents the actual consumption of subject i in repetition R. The next

step involves determining the proportions ˆph and the standard deviation ˆσ that maximize

this log-likelihood function.

C.1 Individual-Level Analysis

To assess the model’s predictions against actual planning horizons on an individual

basis, we employ ˆσ to establish a range for cH for each participant, thereby facilitating

the assignment of corresponding planning horizons. Figure C.1 illustrates this detailed

examination. The x-axis shows the horizon predicted by the short-span planning model,

58

---

<!-- PAGE 61 -->

Table C.1: Optimal Consumption Level in Pe-
riod 1, cH

H ConstantYP PosIR FluctY FluctP
10.00
1
9.09
2
8.26
3
7.51
4
6.83
5
6.21
6
5.64
7
5.13
8
4.67
9
4.24
10

15.00
10.00
11.67
10.00
11.00
10.00
10.71
10.00
10.56
10.00

10.00
10.00
10.00
10.00
10.00
10.00
10.00
10.00
10.00
10.00

8.00
4.00
4.80
4.00
4.44
4.00
4.31
4.00
4.24
4.00

Table C.2: Estimation Outcome

Parameter
ˆp1
ˆp2
ˆp3
ˆp4
ˆp5
ˆp6
ˆp7
ˆp8
˜p9
ˆp10
Uncategorized
ˆσ

Coeﬃcient Standard Error

0.21∗∗∗
0.118∗∗∗
0.071∗∗∗
0.035∗∗
0.032∗∗
0.025∗
0
0.116∗∗∗
0.001
0.099∗∗∗
0.291∗∗∗
0.162∗∗∗

0.034
0.028
0.022
0.016
0.015
0.014
NA
0.027
0.021
0.031
0.04
0.013

Note: p7 was set to 0 because otherwise
the function did not converge. Signiﬁcance
∗p < 0.1,
levels are denoted as follows:
∗∗p < 0.05, ∗∗∗p < 0.01

59

---

<!-- PAGE 62 -->

whereas the y-axis presents the mode of the horizons used by subjects with the budgeting

calculator during the ﬁrst period of each repetition. Notably, the patterns observed

herein provide further insight: the actual planning horizons are typically more extended

than those predicted by the short-term horizon model. Moreover, in over 25 percent

of cases, the model either fails to categorize an individual or predicts a horizon of 1,

while subjects opt for the full horizon. Conversely, subjects adhere to the model’s full-

horizon prediction in only 3 percent of cases. Nevertheless, in approximately 3 percent of

instances, the model forecasts full horizon usage, yet individuals select a shorter horizon.

Figure C.1: Comparison between the pre-
dicted and the observed horizon at the indi-
vidual level

60

---

<!-- PAGE 63 -->

D Hand-to-Mouth Heuristic

One evident heuristic that subjects may adopt to circumvent complexity is the ”hand-

to-mouth behavior (H2M),” where they expend all their available cash each period. Yet,

this approach comes with the cost of potential utility loss. When subjects refrain from

saving in any period, they incur a utility reduction of 3.6% in PosIR and 3.4% in both

FluctP and FluctY, relative to the optimal path.23 In the ConstantYP treatment, the

optimal consumption path inherently involves zero savings per period. However, even

in this treatment, we can examine the adoption of this heuristic by observing deviations

from the unconditionally optimal consumption in at least one period. Two relevant

questions arise: Does this heuristic become more prevalent as complexity increases, and

does access to the calculator limit its usage?

To address these questions, Figure D.1 displays the percentage of subjects using the

H2M heuristic across various treatments and over time. In the ConstantYP, FluctY,

and FluctP treatments, subjects who chose not to save, given that not saving was the

implied optimal choice for that speciﬁc period, are excluded from the analysis. The

ﬁgure demonstrates that the adoption of this heuristic varies across treatments.

In the ConstantYP treatment, the percentage of subjects employing the H2M heuris-

tic is small, accounting for less than 10 percent of the periods. Furthermore, there is no

discernible distinction between subjects with calculator access and those without in this

treatment.

In the FluctY treatment, subjects display the correct intuition by employing the H2M

heuristic when their income is low, aligning with consumption smoothing principles.

Here, the heuristic was utilized in 21.99 percent of the periods when the calculator was

present and in 19.08 percent of the periods when it was absent.24

In the context of complex environments, starting with the PosIR treatment, the

absence of a calculator led to a higher incidence of the Hand to Mouth (H2M) heuristic.

23In 9% of the repetitions, participants used this heuristic in all periods.
24Running a test on the equality of proportions at a 95% signiﬁcance level, we do not ﬁnd a statistically

signiﬁcant diﬀerence between the two calculator conditions (p = 0.0699).

61

---

<!-- PAGE 64 -->

The H2M heuristic was utilized in 12.03 percent of the periods when the calculator was

available, and in 16.02 percent of the periods when it was not (across all repetitions).

This pattern underscores the potential utility of the calculator in mitigating reliance on

H2M behavior. Notably, there were 6 subjects who consistently used this heuristic from

the beginning to the end of Repetition 3 when the calculator was not enabled, which is

double the number observed when the calculator was available.

In the FluctP treatment, the H2M heuristic was employed in 22.46 percent of the

periods with calculator access, and in 17.05 percent of periods without it, across all

repetitions.25 Notably, within this treatment, the proportion of subjects utilizing the

heuristic increases during periods of low prices, reﬂecting their awareness of the beneﬁts

of purchasing more units at lower costs, though they often exceed optimal consump-

tion levels. Furthermore, considering participants who consistently applied the heuristic

throughout Repetition 3, only three subjects did so with the calculator enabled, com-

pared to seven without calculator access.

25We reject the null hypothesis of equality of proportions (p = 0.0006). A plausible explanation
for this behavior in the FluctP treatment is that employing the H2M heuristic requires more complex
arithmetic operations—speciﬁcally, dividing numbers by 50 or 150—compared to other treatments,
which typically involve divisions by 100. The budgeting calculator may encourage the adoption of the
H2M heuristic by simplifying these arithmetic challenges.

62

---

<!-- PAGE 65 -->

Figure D.1: Percentage of Subjects Using the Hand-to-Mouth Heuristic

63

---

<!-- PAGE 66 -->

E The Eﬀect of the Calculator on Payoﬀs

In this appendix, we illustrate the eﬀect of using a calculator on payoﬀs. We also use

random choices as a secondary benchmark for comparison.

The table below shows the expected payoﬀs in dollar terms for treatments with and

without a calculator, as well as for random consumption choice simulations. We refer to

these as expected payoﬀs because, for each subject, we averaged the payoﬀs over three

repetitions. This is because subjects were only paid based on one randomly selected

repetition at the end of the experiment.

For the random choice simulations, we conducted 1,000,000 simulations for each

treatment environment and repetition. We then calculated the payoﬀs and took the

average over the repetitions. In these simulations, we ensured that borrowing constraints

were binding and that the cash balance was exhausted in consumption during the last

period.

From the table, we observe the following that subjects with access to a calculator

performed better than those without in the ConstantYP and PosIR treatments, although

the diﬀerence is minimal in FluctY and FluctP. Interestingly, in the PosIR treatment,

subjects with and without a calculator performed worse than the average simulation

for the random choice model. This diﬀerence is more pronounced in the No Calculator

sessions.

Treatment

ConstantYP
PosIR
FluctY
FluctP

Calculator

Average payoﬀs in CAD ($)
No
Calculator
8.87
8.66
9.19
8.89

Random
Choice
8.95
9.28
8.95
8.81

9.2
9.1
9.12
8.95

No Calc vs. Random Calc vs. Random Calc vs. No Calc
(% Chg Norm by
by Max Payoﬀs)
3.42%
4.39%
-0.72%
0.62%

(% Chg Norm by
by Max Payoﬀs)
2.59%
-1.80%
1.76%
1.45%

(% Chg Norm by
by Max Payoﬀs)
-0.83%
-6.19%
2.49%
0.83%

64

---

<!-- PAGE 67 -->

F Individual Time Series

Figure F.1: Constant YP No Calc, Repetition 1 (Session 1)

Figure F.2: Constant YP No Calc, Repetition 3 (Session 1)

65

---

<!-- PAGE 68 -->

Figure F.3: Constant YP No Calc, Repetition 1 (Session 2)

Figure F.4: Constant YP No Calc, Repetition 3 (Session 2)

66

---

<!-- PAGE 69 -->

Figure F.5: Constant YP Calc, Repetition 1 (Session 1)

Figure F.6: Constant YP Calc, Repetition 3 (Session 1)

67

---

<!-- PAGE 70 -->

Figure F.7: Constant YP No Calc, Repetition 1 (Session 2)

Figure F.8: Constant YP Calc, Repetition 3 (Session 2)

68

---

<!-- PAGE 71 -->

Figure F.9: Pos IR No Calc, Repetition 1 (Session 1)

Figure F.10: Pos IR No Calc, Repetition 3 (Session 1)

69

---

<!-- PAGE 72 -->

Figure F.11: Pos IR No Calc, Repetition 1 (Session 2)

Figure F.12: Pos IR No Calc, Repetition 3 (Session 2)

70

---

<!-- PAGE 73 -->

Figure F.13: Pos IR Calc, Repetition 1 (Session 1)

Figure F.14: Pos IR Calc, Repetition 3 (Session 1)

71

---

<!-- PAGE 74 -->

Figure F.15: Pos IR No Calc, Repetition 1 (Session 2)

Figure F.16: Pos IR Calc, Repetition 3 (Session 2)

72

---

<!-- PAGE 75 -->

Figure F.17: FluctY No Calc, Repetition 1 (Session 1)

Figure F.18: FluctY No Calc, Repetition 3 (Session 1)

73

---

<!-- PAGE 76 -->

Figure F.19: FluctY No Calc, Repetition 1 (Session 2)

Figure F.20: FluctY No Calc, Repetition 3 (Session 2)

74

---

<!-- PAGE 77 -->

Figure F.21: FluctY Calc, Repetition 1 (Session 1)

Figure F.22: FluctY Calc, Repetition 3 (Session 1)

75

---

<!-- PAGE 78 -->

Figure F.23: FluctY No Calc, Repetition 1 (Session 2)

Figure F.24: FluctY Calc, Repetition 3 (Session 2)

76

---

<!-- PAGE 79 -->

Figure F.25: FluctP No Calc, Repetition 1 (Session 1)

Figure F.26: FluctP No Calc, Repetition 3 (Session 1)

77

---

<!-- PAGE 80 -->

Figure F.27: FluctP No Calc, Repetition 1 (Session 2)

Figure F.28: FluctP No Calc, Repetition 3 (Session 2)

78

---

<!-- PAGE 81 -->

Figure F.29: FluctP Calc, Repetition 1 (Session 1)

Figure F.30: FluctP Calc, Repetition 3 (Session 1)

79

---

<!-- PAGE 82 -->

Figure F.31: FluctP No Calc, Repetition 1 (Session 2)

Figure F.32: FluctP Calc, Repetition 3 (Session 2)

80

---

<!-- PAGE 83 -->

G Instructions

G.1 Main Instructions

G.1.1 Calc Sessions

The instructions distributed to subjects in treatments where the calculator was enabled are

reproduced on the subsequent pages. All subjects received identical instructions, with the

exception of those in the PosIR treatment, where minor adjustments were made to incorporate

interest rates.

81

---

<!-- PAGE 87 -->

G.1.2 No Calc Sessions

For the sessions in which the budgeting calculator was not enabled the third page of the instructions

was adapted as shown below.

85

---

<!-- PAGE 89 -->

G.2 Interactive Instructions

Figure G.1: Screenshot for Interactive Instructions 1

Figure G.2: Screenshot for Interactive Instructions 2

87

---

<!-- PAGE 90 -->

Figure G.3: Screenshot for Interactive Instructions 3

Figure G.4: Screenshot for Interactive Instructions 4

88

---

<!-- PAGE 91 -->

Figure G.5: Screenshot for Interactive Instructions 5

Figure G.6: Screenshot for Interactive Instructions 6

89

---

<!-- PAGE 92 -->

Figure G.7: Screenshot for Interactive Instructions 7

Figure G.8: Screenshot for Interactive Instructions 8

90

---

<!-- PAGE 93 -->

Figure G.9: Screenshot for Interactive Instructions 9

Figure G.10: Screenshot for Interactive Instructions 10

91

---

<!-- PAGE 94 -->

Figure G.11: Screenshot for Interactive Instructions 11

Figure G.12: Screenshot for Interactive Instructions 12

92

---

<!-- PAGE 95 -->

H Computer Interface

H.1 Control Questions

Figure H.13: Screenshot for Control Question 13

Figure H.14: Screenshot for Control Question 2

93

---

<!-- PAGE 96 -->

Figure H.15: Screenshot for Control Question 3

Figure H.16: Screenshot for Control Question 4

94

---

<!-- PAGE 97 -->

H.2 Risk Preferences Elicitation

Figure H.17: Screenshot for Stage 2

95

---

<!-- PAGE 98 -->

H.3 Financial Literacy

Figure H.18: Screenshot for Stage 3

96

---

<!-- PAGE 99 -->

H.4 Race to 60

Figure H.19: Screenshot for Stage 3

97

<!-- MARKITDOWN CONVERSION -->

<!-- The following is the full MarkItDown conversion for formatting fidelity. -->

NBER WORKING PAPER SERIES
DYNAMIC OPTIMIZATION MEETS BUDGETING:
UNRAVELING FINANCIAL COMPLEXITIES
Guidon Fenig
Luba Petersen
Working Paper 32821
http://www.nber.org/papers/w32821
NATIONAL BUREAU OF ECONOMIC RESEARCH
1050 Massachusetts Avenue
Cambridge, MA 02138
August 2024
This study is financially supported by the Social Sciences and Humanities Research Council of
Canada. Insight Development Grant: "Identifying Rules of Thumb in Consumption and Saving
Decisions." The views expressed herein are those of the authors and do not necessarily reflect the
views of the National Bureau of Economic Research.
NBER working papers are circulated for discussion and comment purposes. They have not been
peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies
official NBER publications.
© 2024 by Guidon Fenig and Luba Petersen. All rights reserved. Short sections of text, not to
exceed two paragraphs, may be quoted without explicit permission provided that full credit,
including © notice, is given to the source.

Dynamic Optimization Meets Budgeting: Unraveling Financial Complexities
Guidon Fenig and Luba Petersen
NBER Working Paper No. 32821
August 2024
JEL No. C91,E03,E21,E70
ABSTRACT
This paper explores sources of complexity in dynamic optimization, examining how individuals
navigate variation in incomes, prices, and returns in ten-period consumption-saving decisions.
Our findings reveal that dynamic optimization poses significant challenges, resulting in
suboptimal choices even in straightforward scenarios with stable parameters, full information, no
uncertainty, and opportunities to learn. These challenges intensify in scenarios involving
complexities such as inflation and compounding returns, marked by a pronounced tendency to
over-smooth consumption.
Additionally, we introduce a novel budgeting calculator designed to assist with consumption
planning and to collect valuable non-choice data on subjects' planning strategies and horizons—
an approach not previously utilized in studies of dynamic optimization. We observe significant
heterogeneity in planning horizons and ability to optimize given a chosen horizon. Complete
planning leads to better performance in more complex scenarios, even when people do not
optimally utilize the calculator. However, there is little reoptimization after the first period and
participants tend to stick with suboptimal plans for most of their life cycle. The decision to plan is
less influenced by the complexity of the economic environment and more by the length of the
planning horizon.
Guidon Fenig
Department of Economics
University of Ottawa
gfenig@uottawa.ca
Luba Petersen
Department of Economics
Simon Fraser University
8888 University Drive
Burnaby, BC V5A 1S6
and NBER
lubap@sfu.ca

1 Introduction
In the landscape of financial decision-making, dynamic optimization is a crucial element
influencing choices for both individuals and institutions. This domain spans a broad
spectrum of essential decisions, including investment strategies, labor markets, envi-
ronmental policy formation, and especially, the dynamics of saving and consumption.
Economic theories often assume that agents are capable of navigating these complex
situations effectively. However, empirical evidence suggests a contrasting reality. Many
individuals encounter difficulties in planning over time, a challenge emphasized by recent
research (Gabaix and Graeber, 2023; Oprea, 2022). But what makes dynamic optimiza-
tion problems complex?
Our paper investigates how people navigate complexities in consumption-saving de-
cisions, pinpointing five primary sources of complexity: shifts in the economic environ-
ment, the impact of compounding returns, the length of the planning horizon, compu-
tational challenges, and a lack of experience. To explore these elements, we conducted
incentivizeddecision-makingtaskswhereparticipantsundertookaseriesofconsumption-
saving exercises over ten-period horizons with full information about all relevant future
variables.
Inourbaselinescenario,ConstantYP,participantsfacedconsumptiondecisionsunder
conditions of constant and known incomes and prices, and without receiving interest on
their savings. In this simplified setting, theoretically optimal behavior dictates spending
one’s entire income in each period. This design is strategically simple, enabling us to
detect patterns of random decision-making and any systematic biases.
We then introduce various facets of complexity within the optimization problem to
better understand common pitfalls in decision-making. In the FluctY treatment, we
alter participants’ income between two predictable levels, high and low. This varia-
tion helps us determine if participants can grasp the concept of smoothing their utility
from consumption over time as income changes. The FluctP treatment involves chang-
ing prices between high and low levels. This treatment variation allows us to observe
1

whether participants take into account the shape of their induced utility function—that
is, how they value each additional unit of consumption—when they decide how much to
spend. In the PosIR treatment, we introduce a new element to our baseline setting by
introducing positive interest on savings. This enables us to assess how the complexity
of decision-making is affected by the presence of compounding returns. Furthermore,
acrossalltreatments,participantsmadespendingdecisionssequentiallyoveraten-period
horizon. This sequential approach to decision-making allowed us, at the subject-level,
to investigate the additional complexity associated with lengthier planning horizons.
Specifically, we examine whether participants are more likely to make larger planning
errors conditional on their current savings at the start of their decision-making life-cycle.
Ourexperimentsrevealthatindividualsfrequentlyencountersignificantchallengesin
optimizing their lifetime consumption plans, even in scenarios where income and prices
are stable and savings yield no returns. These results underscore the inherent difficulty
of optimization decisions, even under the simplest environments. In our ConstantYP
treatment, the average inexperienced participant managed to attain only 76% of the
unconditionaloptimalsolution(i.etheoptimalsolutionthatdoesnotaccountforcurrent
savings). This performance marginally improves to 82% by the third repetition of the
optimization task, indicating limited learning over time.
Contrary to our expectations, introducing complexity by altering income levels does
not hinder participants’ performance. However, the introduction of more complex el-
ements like compounding interest on savings or fluctuating prices significantly reduces
participants’ ability to optimize unconditionally. In such complex scenarios, inexpe-
rienced participants’ optimization efficiency falls to 66% and 62%, respectively. This
decline in performance is persistent, even as participants gain experience through the
second and third iterations of the task. Interestingly, shortening the planning horizon is
more effective in reducing optimization errors than simply gaining more experience. In
the PosIR treatment, for example, participants improve their optimization performance
by over 3 percentage points by reducing the planning horizon by just two periods, a level
of improvement typically seen after repeating the 10-period task twice.
2

Furthermore, the nature of the errors varies with the type of complexity introduced.
In the PosIR scenario, a common oversight is the undervaluing of early savings, leading
to diminished wealth for later consumption. On the other hand, the FluctP scenario re-
veals a different challenge: while most participants recognize the advantage of spending
more when prices are low, their spending often falls short of the optimal level. This is
the first study to analyze the complexity of decision-making in the context of inflation
in isolation, i.e., when all variables except prices remain constant. It highlights the in-
creasedcognitivechallengesinvolvedinmakingoptimaldecisionsundersuchinflationary
conditions.1
To further investigate the impact of these complexities on decision-making, our study
examines the tools individuals commonly use for planning consumption and savings.
Typically, individuals rely on basic tools such as simple calculators or their own math-
ematical skills. This reliance raises an important question: Are the common errors in
dynamic optimization primarily due to calculation mistakes? To address this question,
our study introduces a second set of treatments where participants have access to a bud-
geting calculator. This device goes beyond basic calculations, offering tailored assistance
for creating comprehensive spending plans. It also tracks all computations, allowing us
to analyze how extensively participants plan their spending and whether their planning
behavior changes with the economic conditions they face. This innovative approach,
focusing on non-choice data, provides a unique lens to assess the depth of people’s dy-
namic planning and the impact of economic complexity on their short-sightedness. To
our knowledge, this study is the first to utilize non-choice calculator data in the context
of dynamic optimization. By analyzing this data, we gain insights into the decision-
making processes and go beyond just the final decisions made by participants.2
Our analysis into the budgeting calculator’s effectiveness yields mixed results. While
1While the experiments conducted by Luhan et al. (2014) and Yamamori et al. (2018) have ana-
lyzed dynamic optimization under fluctuating prices, they simultaneously alter other macroeconomic
variables. InLuhanetal.(2014)experiment, interestratesarepositive, andinYamamorietal.(2018),
savings fluctuate in tandem with prices. This complicates the evaluation of how subjects’ behavior
changes due to purely inflationary factors.
2An example of how this type of data can be used is found in Fenig et al. (2022), who apply it to
study group dynamics in non-linear games.
3

we anticipated that the calculator would streamline the decision-making process, the
actual impact was nuanced. For example, in the ConstantYP treatment, calculator
access led to an increase in utility by eight to eleven percentage points compared to
the unconditional optimal path, and a 3.4 percent rise in monetary rewards normalized
by the maximum potential payoff. In the PosIR treatment, the calculator improved
optimization by five to six percentage points, along with a 4.4 percent increase in nor-
malized monetary payoff. However, in FluctY and FluctP, its influence was minimal or
indiscernible.3
It should be emphasized that the effectiveness of the budgeting tool in simplifying
optimization tasks is contingent upon participants’ proficient utilization. Proficient use
ofthecalculatorincreasesunconditionaloptimizationby10to20percentagepoints. Itis
crucialtohighlightthatinthePosIRsetting—unlikeinothertreatmentswhereproblems
are addressable by evaluating one or two periods—calculator use significantly facilitates
tackling longer-horizon problems, which are otherwise too challenging to compute man-
ually. Because of these cognitive challenges, one possible heuristic is to compress the
planning horizon. Further investigation reveals that a short-span planning model does
not fully account for deviations from the optimal consumption path. Nevertheless, even
when participants facing positive interest rates formulate full plans—which only about
half of them do—the task remains exceedingly challenging. Although there is a notable
improvement over participants without calculator access, the results remain suboptimal,
as evidenced by their decision-making relative to their planning horizons.
Overall, we find strong support to models positing that complexity hinders dynamic
optimization (Gabaix and Graeber, 2023; Woodford, 2019). The most substantial bar-
riers to optimal decision-making include the objective function’s curvature, the impact
of compounding returns, and the length of the planning horizon. Our research indicates
that while varying income alone does not exacerbate decision-making challenges, the
presence of numerical calculations can significantly contribute to the complexity of the
task. It is imperative to recognize that the presence of a decision-aid tool like a budget-
3For a more comprehensive analysis, see Appendix E.
4

ing calculator does not automatically translate to improved outcomes. However, when
used effectively, it can be a powerful aid in navigating complex financial decisions.
The structure of the paper is as follows. Section 2 provides a summary of the litera-
ture most relevant to this paper. Section 3 presents the theoretical model, describes the
different treatments, outlines the experimental design, and lists the main hypotheses.
Section 4 offers an overview of the main results. In Section 5, we employ econometric
techniques to more formally demonstrate the treatment effects of environmental com-
plexity and the use of the budgeting calculator. In Section 6 we extend our model to
allow for short-span planning. Finally, Section 7 concludes the paper.
2 Related Literature
In this subsection, we explore two distinct yet interconnected bodies of research. The
firstpertainstothecomplexitiesinherentindecision-making, whilethesecondfocuseson
learning-to-optimize experiments within the specific domain of consumption and saving
decisions. These two areas of study provide critical insights that inform our understand-
ing of the challenges and behaviors observed in financial decision-making processes.
Many researchers have theorized about the difficulties agents face in dynamically
optimizing. A common theme is the inattention to key variables in optimization prob-
lems, as detailed in studies by Schipper (2014), Sims (2003), Ma´ckowiak and Wiederholt
(2015), and Gabaix (2014). These works suggest that agents might either neglect im-
portant variables or focus on a limited subset due to the costs of processing information.
Mis-specifiedpreferencesalsocontributetowhatappearstobeoptimizationerrors. Con-
trary to thecommonly assumed exponential discounting in manyintertemporal planning
models, substantial evidence suggests that individuals tend to discount future utility in
a hyperbolic manner (Loewenstein and Prelec, 1992; Laibson, 1997; O’Donoghue and
Rabin, 1999).
Theliteraturealsohighlightsthenumericalchallengesindynamicoptimization. Even
the authors of this paper admit to finding the mathematical aspects of extended multi-
5

period constrained optimization daunting. Simple three-period problems, which might
seem elementary, can still pose significant hurdles for many (Gabaix and Graeber, 2023).
Emphasizing the importance of this, Lusardi and Wallace (2013) highlight that a firm
grasp on quantitative literacy is a cornerstone of financial literacy.
In the context of financial planning over lengthy horizons, Ilut and Valchev (2023)
develop a model in which agents, despite perceiving all objective variables relevant to
their payoff, encounter subjective uncertainty about optimizing their actions in the given
state. This necessitates engaging in costly learning processes to determine the optimal
course of action. Our experimental design captures this situation: participants are
fully informed of all relevant variables, yet they face challenges in effective problem-
solving. Moreover, our novel budgeting calculator enables us to observe their planning
process. Our findings align with the dual reasoning model proposed by these authors.
Initially, our participants tend to rely on cognitive planning (System 2). However, as
they progress through their life cycle, many switch to using intuitive heuristics (System
1). Interestingly, towards the end of their life cycle, as the planning horizon becomes
shorter, some participants revert to cognitive planning (System 2).
Thecomplexityoftheeconomicenvironmentanditsimpactondynamicoptimization
is a focal point in the literature. Gabaix and Graeber (2023) investigate a three-period
consumption-saving scenario, uncovering that tasks with fluctuating endowments and
positive, compounding interest are viewed by subjects as more challenging, leading to
increased errors and longer decision times. Consistent with Gabaix and Graeber, we find
that complexity in specific environments (PosIR and FluctP) result in poorer optimiza-
tion. We further show that longer planning horizons exacerbate optimization errors.
Indeed, condensing the planning horizon is a commonly employed strategy to reduce
cognitive demands in dynamic optimization tasks. Caliendo and Aadland propose a
framework accommodating heterogeneity in planning horizons, where individuals with
perfect foresight and those adopting hand-to-mouth strategies represent the extremes.
? analyzes experimental data from an environment similar to our PosIR treatment.4 In
4Most of the data analyzed is taken from Carbone and Hey (2004).
6

their study, the horizon spans 25 periods, and the goal is to analyze alternative models
that participants may have in mind, allowing for deviations from the optimal consump-
tion path. Thus, they conduct a comparison between models and find that an exponen-
tial discounting model in which participants discount future consumption (even if they
should not) explains 28% of the data. Furthermore, the rational model—characterized
by no discounting, lack of hyperbolic preferences, and a full planning horizon—accounts
for 22% of the observations, while the short-span planning horizon explains approxi-
mately one fifth of the data. This latter observation is consistent with our findings that
short-span planning alone cannot account for the majority of deviations observed in our
PosIR treatment.
Dynamic optimization problems are intrinsically complex. The challenges stem from
various factors: the extended planning horizons, a wide array of choice variables, the
options to borrow or save at differing interest rates, and the unpredictability of future
events. Such a diverse range of considerations often leads to decision overload for indi-
viduals, nudging them towards simpler heuristics or fallback options in an attempt to
manage the overload. Simon (1956) develops a model of ’satisficing’ that captures this
process by which a decision maker curtails further search. This idea is further developed
by Krosnick (1991) who links satisficing to a combination of expected task difficulty, mo-
tivation, and ability. Caplin et al. (2011) show evidence that in complex decision tasks,
subjects search sequentially and stop searching when they reach their reservation utility.
Non-choice data from our Calculator treatments corroborate these observations of in-
complete searches and suboptimal decision-making, indicating limited average benefits
from tools such as our budgeting calculator. Importantly, we do not observe significant
differences in search behavior as environmental complexity increases (as we move from
ConstantYP to more complex settings). We do, however, find a significant increase in
calculator usage as the horizon over which subjects are planning is reduced significantly
(in the last two periods of their life-cycle). This further substantiates that the planning
horizon is a more salient determinant of complexity for participants than the economic
environment variables.
7

Our analysis of dynamic optimization facilitated by a budgeting calculator con-
tributes to the extensive body of research on household finance puzzles. D’Acunto and
Rossi (2023) discuss the success of alternative strategies to mitigate household financial
errors: financial advising, nudges, and robo-advising. The design of our budgeting tool
falls somewhere in between nudges and robo-advising. The presence of the budgeting
calculator nudges participants to at least consider the complete planning horizon when
making their consumption decisions. The calculator mitigates the cognitive burdens
associated with budgeting calculations but does not advise or encourage participants to
make certain plans.5 D’Acunto et al. (2019) demonstrate that in the context of portfolio
investment, robo-advice helps reduce several behavioral biases, including the disposition
effect, trend chasing, and the rank effect. We also find that the introduction of a cal-
culator can significantly improve optimization, with more pronounced effects in simpler
environments, such as our ConstantYP treatment. The benefits of our tool in more
complex settings involving compounding interest or fluctuating prices are notably less,
and suggest a need for additional advising or social learning (Ballinger et al., 2003).
Overview of Experimental Designs in Dynamic Optimization
Thecontrolledenvironmentofalaboratoryisinstrumentalinunravelinghowindividuals
approach optimization amidst the variability of economic conditions. Table 1 provides a
comprehensive summary of the various experimental design differences across the broad
learning-to-optimize literature (Duffy, 2016). In most experiments, participants obtain
interest from their savings, and there is a prevalent uncertainty about future economic
variables, with income being the variable that most frequently changes. The most com-
mon planning horizon across these studies is 20 periods, and it is notable that most
experimental designs do not involve optimal closed-form solutions. The interplay of
complex elements within these experimental settings—such as extended horizons, un-
5The one exception is that the calculator informs participants if they have insufficient income over
their lifetime to fulfill their consumption plan.
8

certainty, returns on savings, and income fluctuations—poses a challenge in discerning
the impact of different aspects of complexity on optimization behaviors. To address this,
our parameterization, as detailed at the bottom of the table, introduces one feature of
complexity at a time, allowing for a meticulous examination of each element’s influence
on optimization.
|                         | Table 1: Related     | learning-to-optimize |           | experimental |             | literature |             |
| ----------------------- | -------------------- | -------------------- | --------- | ------------ | ----------- | ---------- | ----------- |
|                         |                      |                      | Interest  | Fluctuating  | Borrowing   | No. of     | Closed-Form |
|                         | Paper                | Uncertainty          |           |              |             |            |             |
|                         |                      |                      | Rates(IR) | Variable     | Constraints | Periods    | Solution    |
| HeyandDardanoni(1988)   |                      | Yes                  | >0        | Income       | Yes         | Indefinite | No          |
|                         | Ballingeretal.(2003) | Yes                  | >0        | Income       | Yes         | 60         | No          |
| CarboneandHey(2004)     |                      | Yes                  | >0        | Income       | Yes         | 25         | No          |
|                         | Brownetal.(2009)     | Yes                  | =0        | Income       | Yes         | 30         | No          |
|                         | Ballingeretal.(2011) | Yes                  | =0        | Income       | Yes         | 20         | No          |
| CarboneandDuffy(2014)   |                      | No                   | >0        | Income       | Yes         | 25         | Yes         |
|                         | Luhanetal.(2014)     | No                   | >0        | PriceandIR   | Yes         | 5          | Yes         |
| CarboneandInfante(2015) |                      | Yes                  | >0        | Income       | No          | 15         | No          |
|                         | Meissner(2016)       | Yes                  | =0        | Income       | No          | 20         | Yes         |
|                         | DuffyandLi(2019)     | No                   | =0        | Income       | Yes         | 25         | Yes         |
| Yamamorietal.(2018)     |                      | No                   | =0        | Prices       | Yes         | 20         | Yes         |
|                         | Carboneetal.(2019)   | Yes                  | >0        | Income       | No          | 15         | No          |
|                         | Lu(2022)             | No                   | >0        | Income       | No          | 9          | No          |
| MillerandRholes(2023)   |                      | Yes                  | >0        | Income       | No          | 20         | No          |
| DuffyandOrland(2023)    |                      | Yes                  | =0        | Income       | No          | 3          | No          |
| GabaixandGraeber(2023)  |                      | No                   | >0        | Income       | No          | 3          | Yes         |
|                         | Li(2024)             | No                   | >0        | Income       | Yes         | Indefinite | No          |
|                         | This paper           |                      |           |              |             |            |             |
|                         | ConstantYP           | No                   | =0        | None         | Yes         | 10         | Yes         |
|                         | PosIR                | No                   | >0        | None         | Yes         | 10         | Yes         |
|                         | FluctY               | No                   | =0        | Income       | Yes         | 10         | Yes         |
|                         | FluctP               | No                   | =0        | Price        | Yes         | 10         | Yes         |
Although direct comparisons among these experiments are difficult due to their dif-
fering parameters and information sets, two key patterns consistently emerge in the
research. First, there is a noticeable struggle with dynamic planning – individuals often
either consume too much or too little, neglecting the long-term impacts of compounding
returns. Second, the tendency to optimize decisions appears to enhance as the planning
horizon becomes shorter. Echoing this, Ballinger et al. (2011) observes that subjects
typically anticipate only up to three periods ahead, underscoring the cognitive limits in
| longer-term | financial planning. |     |     |     |     |     |     |
| ----------- | ------------------- | --- | --- | --- | --- | --- | --- |
9

| 3 Theoretical | Model | and | Experimental |     | Design |     |
| ------------- | ----- | --- | ------------ | --- | ------ | --- |
The theoretical framework underpinning this study is a standard intertemporal model
of life-cycle consumption and savings (See Modigliani and Brumberg, 1954). Our model
is based on a finite-horizon and deterministic framework. Each consumer’s goal is to
|     |     | T   | (cid:18) 1 | (cid:19) |     |     |
| --- | --- | --- | ---------- | -------- | --- | --- |
(cid:88)
|     |     | max | k   | c1−σ |     | (1) |
| --- | --- | --- | --- | ---- | --- | --- |
t
|     |     | ct  | 1−σ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
t=1
| subject to: |     |        |             |        |     |     |
| ----------- | --- | ------ | ----------- | ------ | --- | --- |
|             |     | p c +s | = y +(1+r)s |        |     | (2) |
|             |     | t t    | t t         | t−1    |     |     |
|             |     | s ≥ 0  | : ∀t and    | s = 0. |     | (3) |
|             |     | t      |             | 0      |     |     |
We assume a concave utility function, specifically a constant relative risk aversion
(CRRA) with a parameter σ and a constant k, the variables y , s , and r represent the
t t
consumer’s exogenous income, savings, and known and constant interest rate, respec-
tively. The constraint s ≥ 0 implies that borrowing is not allowed.
t
In this finite horizon model, the consumer faces no uncertainty regarding price and
income processes. They make decisions about consumption, denoted as c , over T peri-
t
ods, considering their income, y , and implicitly decides how much to save at the interest
t
rate r. The consumer pays a price p for each unit of consumption.
t
The optimal consumption path is given by T −1 Euler equations:
|     |     |     | (cid:18) | (cid:19)1 |     |     |
| --- | --- | --- | -------- | --------- | --- | --- |
|     |     |     | p        | σ         |     |     |
t
|     |     | c = | (1+r) | c   |     | (4) |
| --- | --- | --- | ----- | --- | --- | --- |
|     |     | t+1 | p     | t   |     |     |
t+1
These Euler equations relate consumption in period t to consumption in period t + 1
and must be satisfied within the optimal consumption path. We use the lifetime budget
constraint (Equation 5) to derive a system of T equations and T unknowns and then
| find the optimal | consumption | level c∗ | for t ∈ [1,T]. |     |     |     |
| ---------------- | ----------- | -------- | -------------- | --- | --- | --- |
t
10

T T
| (cid:88) | p c (cid:88) | y   |     |
| -------- | ------------ | --- | --- |
|          | t t ≤        | t   | (5) |
| (1+r)t−1 | (1+r)t−1     |     |     |
t=1 t=1
Solving the system of equations also yields the optimal level of consumption for period
1,
(cid:80)T
1 y
t
| c =        | t=1 (1+r)t−1 |                   | (6) |
| ---------- | ------------ | ----------------- | --- |
| 1 (cid:18) | (cid:18)     | 1(cid:19)(cid:19) |     |
(cid:16) (cid:17)σ−
|     | 1 (cid:80)T    | pt σ |     |
| --- | -------------- | ---- | --- |
| p   | +pσ            |      |     |
| 1   | 1 t=2 (1+r)t−1 |      |     |
3.1 Treatments
Our objective in designing the baseline experimental environment was to create a setting
that would enable participants to solve the dynamic decision problem without relying
on advanced budgeting tools. Therefore, we parameterized our baseline environment,
named ConstantYP, to maintain income and prices constant throughout the entire
consumption horizon. We selected a planning horizon of T = 10 periods, which is
sufficiently long for participants to plan ahead and also provides ample time for us
to observe their learning through stationary repetitions of the environment. Including
stationary repetitions is critical in life-cycle experiments because some participants may
only understand how to overcome the difficulties of the environment halfway through the
sequence, making it impossible for them to adjust their previous consumption choices.
Each participant encountered three repetitions of ten periods, and we re-calibrated the
environment across repetitions to generate slightly different optimization problems.
We designed and implemented three additional treatments, each introducing a dis-
tinct dimension of complexity to understand where and why errors occur in decision-
making. The treatments were conducted using a between-subject design. The first
treatment, FluctY, varies participants’ income between two predictable levels, high
(y ) and low (y ), throughout the horizon. By ensuring that a higher income is received
H L
in the first period, we prevent the budget constraint from binding for an optimizing
participant, and even for individuals who tend to over-consume compared to the uncon-
11

ditionally optimal solution. This treatment is particularly insightful, as it evaluates the
participants’ capability to smooth their consumption over time in the face of fluctuating
income. In the second treatment, PosIR, the complexity is increased relative to the
ConstantYP treatment by introducing a positive interest rate (r = 0.1) on savings in
every period of each of the three repetitions. This approach allows us to observe the
cognitive challenges associated with compounding returns on savings decisions. Lastly,
in the FluctP treatment, we introduce price fluctuations between two values, high (p )
H
and low (p ), for the entire horizon. This treatment investigates whether participants
L
consider the shape of their utility function—that is, their valuation of each additional
unit of consumption—in their spending decisions, as prices vary. These three treat-
ments, by adding different complexity dimensions to the basic optimization setting, help
us dissect the nuances of decision-making under varied economic conditions.
To incentivize participants’ optimization decisions, we induce a standard constant
relative risk aversion (CRRA) per-period utility function:
(cid:18) (cid:19)
1
u(c ) = k c1−σ.
t 1−σ t
Here, we set σ = 0.5 across all treatments. The parameter k is a scaling constant that
does not affect the optimal consumption path. In the FluctP treatment, we assign the
constant k a value of 2.65, and for the other treatments, we assign it a value of 3.35.
This specific adjustment is made to ensure that the optimal life-cycle utility is equalized
across all treatments, where the interest rate r is set to zero. The chosen value for σ is
intended to create a sufficiently large intertemporal trade-off. Table 2 provides details
on the income, price, and interest rate processes for each treatment. It is important to
highlight the variations across repetitions: in the second repetition, income is doubled
relativetothefirst. Inthethirdrepetition,bothincomeandpricesaredoubledcompared
to the first repetition. Although the nominal variables change from the first to the last
repetition, the real variables stay consistent, ensuring identical optimal solutions across
these repetitions.
12

|     | Table 2: Parameters | of Treatments |     |     |
| --- | ------------------- | ------------- | --- | --- |
Treatment
|     |               | Constant YP | PosIR | FluctY FluctP |
| --- | ------------- | ----------- | ----- | ------------- |
|     | t∈{1,3,5,7,9} | 1000        | 1000  | 1500 1200     |
y
t
|            | t∈{2,4,6,8,10}  | 1000 | 1000 | 500 1200 |
| ---------- | --------------- | ---- | ---- | -------- |
| Repetition | 1 t∈{1,3,5,7,9} | 100  | 100  | 100 150  |
p
t
|     | t∈{2,4,6,8,10} | 100  | 100  | 100 50    |
| --- | -------------- | ---- | ---- | --------- |
|     | r              | 0    | 0.1  | 0 0       |
|     | t∈{1,3,5,7,9}  | 2000 | 2000 | 3000 2400 |
y t
|            | t∈{2,4,6,8,10}  | 2000 | 2000 | 3000 2400 |
| ---------- | --------------- | ---- | ---- | --------- |
| Repetition | 2 t∈{1,3,5,7,9} | 100  | 100  | 100 150   |
p
t
|     | t∈{2,4,6,8,10} | 100  | 100  | 100 50    |
| --- | -------------- | ---- | ---- | --------- |
|     | r              | 0    | 0.1  | 0 0       |
|     | t∈{1,3,5,7,9}  | 2000 | 2000 | 3000 2400 |
y t
|            | t∈{2,4,6,8,10}  | 2000 | 2000 | 3000 2400 |
| ---------- | --------------- | ---- | ---- | --------- |
| Repetition | 3 t∈{1,3,5,7,9} | 200  | 200  | 200 300   |
p
t
|     | t∈{2,4,6,8,10} | 200 | 200 | 200 100 |
| --- | -------------- | --- | --- | ------- |
|     | r              | 0   | 0.1 | 0 0     |
Figure 1 displays the optimal consumption path corresponding to each treatment
and repetition. Notably, despite the differences in the income process, the optimal con-
sumption path remains the same for both the Constant YP and FluctY treatments. In
this frameworks, consumers maximize utility by consuming 10 units per period in Rep-
etitions 1 and 3, and 20 units per period in Repetition 2. In the PosIR treatment, the
optimal consumption path progressively increases, reflecting the absence of discounting.
Under the FluctP treatment, the optimal consumption level adjusts in response to price
fluctuations, increasing when prices are low and decreasing when they are high, con-
sistent with a bi-periodic pattern. Additionally, Figure 1 illustrates the consumption
yt,
path representing an agent’s mistaken static optimization approach, where the entire
pt
income is consumed each period without considering the intertemporal dynamics.6
6TheexceptionistheConstantYPtreatment,inwhichtheoptimalunconditionalconsumptionpath
implies not saving.
13

In the ConstantYP treatment, the unconditional optimal solution corresponds to the
’Hand-to-Mouth’ (H2M) strategy in the initial period. If a participant opts to save any
income during this period, the conditionally optimal consumption path would diverge
from the H2M heuristic. Conversely, in all other treatments, a marked divergence is
| observed  | between        |          | the optimal | and         | H2M consumption |           | paths.7        |           |             |
| --------- | -------------- | -------- | ----------- | ----------- | --------------- | --------- | -------------- | --------- | ----------- |
|           |                | Constant | YP          |             |                 |           |                | Pos IR    |             |
|           | Repetitions1,3 |          |             | Repetition2 |                 |           | Repetitions1,3 |           | Repetition2 |
| 50        |                |          | 50          |             |                 | 50        |                | 50        |             |
| 45        |                |          | 45          |             |                 | 45        |                | 45        |             |
| 40        |                |          | 40          |             |                 | 40        |                | 40        |             |
| 35        |                |          | 35          |             |                 | 35        |                | 35        |             |
| snekoT 30 |                |          | snekoT 30   |             |                 | snekoT 30 |                | snekoT 30 |             |
| 25        |                |          | 25          |             |                 | 25        |                | 25        |             |
| 20        |                |          | 20          |             |                 | 20        |                | 20        |             |
| 15        |                |          | 15          |             |                 | 15        |                | 15        |             |
| 10        |                |          | 10          |             |                 | 10        |                | 10        |             |
| 5         |                |          | 5           |             |                 | 5         |                | 5         |             |
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10
|           |                | Period |           | Period      |     |           | Period         |        | Period      |
| --------- | -------------- | ------ | --------- | ----------- | --- | --------- | -------------- | ------ | ----------- |
|           |                |        | FluctY    |             |     |           |                | FluctP |             |
|           | Repetitions1,3 |        |           | Repetition2 |     |           | Repetitions1,3 |        | Repetition2 |
| 50        |                |        | 50        |             |     | 80        |                | 80     |             |
| 45        |                |        | 45        |             |     | 70        |                | 70     |             |
| 40        |                |        | 40        |             |     | 60        |                | 60     |             |
| 35        |                |        | 35        |             |     |           |                |        |             |
|           |                |        |           |             |     | 50        |                | 50     |             |
| snekoT 30 |                |        | snekoT 30 |             |     |           |                | snekoT |             |
| 25        |                |        | 25        |             |     | snekoT 40 |                | 40     |             |
| 20        |                |        | 20        |             |     | 30        |                | 30     |             |
| 15        |                |        | 15        |             |     |           |                |        |             |
|           |                |        |           |             |     | 20        |                | 20     |             |
| 10        |                |        | 10        |             |     |           |                |        |             |
|           |                |        |           |             |     | 10        |                | 10     |             |
| 5         |                |        | 5         |             |     |           |                |        |             |
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10
|     |     | Period |     | Period |                |     | Period       |     | Period |
| --- | --- | ------ | --- | ------ | -------------- | --- | ------------ | --- | ------ |
|     |     |        |     |        | c∗             | yt  |              |     |        |
|     |     |        |     |        | t              | pt  |              |     |        |
|     |     |        |     | Figure | 1: Theoretical |     | Predictions. |     |        |
We introduce a second between-subject treatment variation to our study by varying
participants’ access to a budgeting calculator across each of the four parameterizations.
In the Calc treatments, participants were provided with the option to utilize a bud-
geting calculator, enabling them to input hypothetical consumption choices for current
and future periods based on the given income, prices, and interest rates. Figure 2(a)
shows a screenshot of the budgeting calculator. In this example, participants could in-
put a consumption plan for periods 6-10 and calculate the hypothetical per-period and
accumulated points. Participants had unrestricted access to the calculator without any
| 7We | analyze | this strategy | in  | Appendix | D.  |     |     |     |     |
| --- | ------- | ------------- | --- | -------- | --- | --- | --- | --- | --- |
14

mandatory usage requirements. Upon submitting their decisions, participants could re-
view the history of their consumption choices and corresponding savings balances. The
software recorded all plans after a participant clicked the calculate button. However,
each time subjects submitted their consumption choices, the calculator was cleared.
In contrast, participants in the NoCalc treatment lacked access to the budgeting
calculator. Figure 2(b) displays a screenshot of the NoCalc interface. Although partici-
pants were unable to utilize the tool for financial planning, they retained the ability to
review the history of their past choices as well as future incomes, prices, and interest
rates. Participants in both treatments could employ the Windows calculator for their
decisions; however, these inputs were not recorded.8 9
a)Calc b)NoCalc
Hypothetical
consumptionchoicesfor
periods6,7,8,9,and10
edamseciohcnoitpmsnoC
5ot1sdoirepni
edamseciohcnoitpmsnoC
5ot1sdoirepni
Figure 2: Screenshots for Treatments with a Budget Calculator and Treatments without
a Budget Calculator
8It is noteworthy that our NoCalc treatments provide more detailed and readily accessible infor-
mation compared to standard experiments in consumption smoothing. In these standard experiments,
subjects sometimes only see their current income and accumulated savings, based on which they have
to make their current consumption decisions.
9Household recall of past decisions is shown to be limited D’Acunto and Weber (2022), and house-
holds are unable to pay attention and retain all this information over their lifetime D’Acunto et al.
(2023). As both of our No-Calculator and Calculator treatments provide participants with detailed in-
formationabouttheirpast,current,andfutureindividualspendingandaggregatevariables,weinterpret
participants’ optimization performance as an upper-bound on their ability to solve such problems.
15

| 3.2 | Experimental |     | Procedures |     |     |     |
| --- | ------------ | --- | ---------- | --- | --- | --- |
The study recruited undergraduate and graduate participants from various academic
disciplines, resulting in a total of 326 subjects who participated in one of eight treat-
ments. The experiments were conducted in-person at the CRABE Laboratory at Simon
Fraser University (SFU) and the SSRL at the University of Saskatchewan (UofS). Our
participant sample was nearly evenly split between individuals from SFU and UofS.
The experimental sessions were held from July 2017 through May 2018. Table 3 shows
the number of participants per treatment. The experiment was computerized and pro-
| grammed | using z-Tree | Fischbacher | (2007).   |             |               |        |
| ------- | ------------ | ----------- | --------- | ----------- | ------------- | ------ |
|         |              | Table       | 3: Number | of Subjects | per Treatment |        |
|         |              |             |           |             | Budgeting     | Number |
Treatment
|     |     |            |         |      | Calculator of | Subjects |
| --- | --- | ---------- | ------- | ---- | ------------- | -------- |
|     |     | ConstantYP | Calc    |      | Yes           | 44       |
|     |     | ConstantYP | No      | Calc | No            | 44       |
|     |     | PosIR      | Calc    |      | Yes           | 48       |
|     |     | PosIR      | No Calc |      | No            | 43       |
|     |     | FluctY     | Calc    |      | Yes           | 48       |
|     |     | FluctY     | No Calc |      | No            | 46       |
|     |     | FluctP     | Calc    |      | Yes           | 45       |
|     |     | FluctP     | No Calc |      | No            | 48       |
We implemented a “between subjects” design by randomly assigning each subject
to only one of the eight treatments. At the beginning of each session, the experi-
menter read aloud the written instructions provided to the participants. Subsequently,
participants completed an interactive computerized instruction phase and answered in-
centivized control questions. These control questions, detailed in Appendix G, ensured
that participants understood the main features of the dynamic optimization experiment
16

and the tools available to them. For instance, to illustrate the principle of diminish-
ing marginal utility, given that the induced utility function is concave, a set of control
questions ensured that participants grasp this concept before proceeding with the main
tasks of the experiment. In one set of questions, participants were asked to provide the
utility levels associated with consumption levels of 1, 2, 9, and 10 units using the Con-
sumption to Utility converter provided in all treatments. They then had to recognize
that increasing their consumption from 1 to 2 units results in a larger increase in utility
compared to increasing it from 9 to 10 units. Participants earned points based on their
performance in the control questions: four points for each correct answer on the first
attempt, three points for the second attempt, and two points for the third attempt. No
further points were awarded beyond three attempts, and participants were required to
answer all questions correctly to proceed.
After completing these questions, participants proceeded to Stage 1. This stage in-
volvedthreerepetitionsofoneofthedynamicoptimizationenvironmentsshowninTable
2. Figure 3 displays a screenshot of the main computer interface.10 At the beginning
of each period, participants received income (y ) in tokens and were asked to decide
t
how many units of output they wanted to purchase. To facilitate their decision-making,
participants could refer to the plot correlating output with points positioned at the bot-
tom right corner of the screen. Alternatively, they could utilize the Output to Points
converter located in the upper right corner of the screen to enhance their understanding
of the utility function’s properties. In the Calc sessions, participants could also use the
budgeting calculator located on the right-hand side of the screen to explore different
consumption paths and their implications for own savings and points (utility) before
submitting their final choices on the left-hand side of the screen. Our interface design
wasintendedtoensurethatallrelevantinformationwasreadilyaccessibletoparticipants
on a single screen.11
10There was no time limit for completing any stage of the experiment. In Stage 1, which consisted of
three repetitions, subjects spent between 3 and 85 minutes in total.
11Participants who requested it were provided with pen and paper to write down calculations, which
could be used at any point during the experiment.
17

Figure 3: Screenshot of the Experimental Software for Stage 1
Inthesubsequentthreestagesoftheexperiment, wecollecteddatathatdistinguished
participants across three dimensions: risk preferences, financial literacy, and the ability
to use backward induction. In Stage 2, risk preferences were assessed through a task
adapted from Eckel and Grossman (2002), where participants selected from six distinct
50/50 gambles (refer to Appendix H.2 for a screenshot). This assessment offers a foun-
dational measurement of key attributes influencing various economic decisions, serving
as a control variable. In Stage 3, financial literacy was evaluated using a methodology
adapted from Lusardi and Mitchell (2007), involving five multiple-choice questions with
pointsawardedforcorrectfirst-attemptanswers. Thisevaluationiscrucial, asfinancially
literate individuals are better positioned to create optimal budgeting plans, particularly
by taking advantage of consumption smoothing and compounding interest rates (refer to
Appendix H.3). In Stage 4, backward induction ability was assessed through the Race to
60 game, proposed by Bosch-Rosa et al. (2018). Participants competed against a com-
puter, selecting numbers from 1 to 10 to reach or exceed 60 first, earning eight points
18

per win (refer to Appendix H.4 for a screenshot). This assessment is crucial, as dynamic
models frequently rely on backward induction for solutions. The experiment concluded
with a demographic questionnaire, collecting information on participants’ age, gender,
| education, | and employment | status. |     |     |     |     |     |
| ---------- | -------------- | ------- | --- | --- | --- | --- | --- |
To determine participants’ compensation, we added up the points they earned in all
four stages and from correctly answering the control questions. For Stage 1, participants
were paid for one randomly selected repetition. Payment was made in Canadian dollars
(CAD) at an exchange rate of 25 points = $1. In addition, participants received a show-
$7.
up fee of On average, participants completed the experiment in 40 minutes, and the
average payment was $21.39. Figure 4 provides a summary of the different stages of the
experiment.
Interactive
Instructions
ControlQuestions
12Questions
BeginExperiment
|     | Stage 1 |     | Stage | 2   | Stage | 3   | Stage 4 |
| --- | ------- | --- | ----- | --- | ----- | --- | ------- |
DynamicOptimizationGame.
|     |     |     | RiskPreference |     | FinancialLiteracy |     | BackwardInduction |
| --- | --- | --- | -------------- | --- | ----------------- | --- | ----------------- |
SubjectsparticipateinONEofthe
|     |                       |     | Elicitation |     | Test        |     | Test’Raceto60’   |
| --- | --------------------- | --- | ----------- | --- | ----------- | --- | ---------------- |
|     | followingenvironments |     | (Eckeland   |     | (Lusardiand |     | (Bosch-Rosaetal. |
1. constantyt,constant,pt,andr=0 Grossman,2002) Mitchell,2007) 2018)
| 2.  | constantyt,constant,pt,andr=0.1  |     |     |     |            |     |              |
| --- | -------------------------------- | --- | --- | --- | ---------- | --- | ------------ |
|     |                                  |     |     |     | 5Questions |     | 8Repetitions |
| 3.  | fluctuatingyt,constant,pt,andr=0 |     |     |     |            |     |              |
| 4.  | constantyt,fluctuating,pt,andr=0 |     |     |     |            |     |              |
EndExperiment
Withorwithouta
Payment
|     | budgetingcalculator |     |     |     |     |     | Demographic |
| --- | ------------------- | --- | --- | --- | --- | --- | ----------- |
• ControlQuestions
|     | 3Repetitions |     |     |     |     |     | Questionnaire |
| --- | ------------ | --- | --- | --- | --- | --- | ------------- |
• 1randomlyselected
repetitioninStage1
•
PerformanceinStages
2,3,and4
|     | Figure | 4: Sequence | of Events | in Experimental |     | Sessions. |     |
| --- | ------ | ----------- | --------- | --------------- | --- | --------- | --- |
19

3.3 Hypotheses
Our analysis centers on two metrics to gauge participants’ optimization abilities. The
first metric, the Unconditional Optimal Index, quantifies the relative disparity between
the actual utility and the utility of the unconditional optimal solution, expressed as a
percentage:
|U −Uunc|
UncOptIndex = γU = 1− i,q,r,t q,r,t (7)
i,q,r,t Uunc
q,r,t
whereU representstheutilityassociatedwiththeactualconsumptionchoicemadein
i,q,r,t
treatment q, repetition, r, period t by participant i, while Uunc represents the treatment-
q,r,t
repetition-period utility associated with unconditionally optimal consumption. Note
that Uunc is the same for all participants of the same treatment, repetition and period.
q,r,t
Theindextakesavalueof1whenaparticipantchoosesaconsumptionlevelthatmatches
the unconditional optimal. The unconditional optimal level of consumption is calculated
attheoutsetofeachrepetition,priortoanyconsumptiondecisionsbyparticipants,based
on the complete sequence of income, prices, and interest rates for that repetition. The
second measure is the Conditional Optimal Index that computes the relative disparity
between the actual utility and the utility linked to participant i’s conditional optimal
solution, also represented as a percentage:
|U −Ucond|
CondOptIndex = γC = 1− i,q,r,t i,q,r,t (8)
i,q,r,t Ucond
i,q,r,t
where Ucond represents the utility associated with subject i’s conditionally optimal con-
i,q,r,t
sumption in treatment q, repetition r, and period t. The conditional optimal level of
consumption is computed for each period as the repetition progresses, contingent on the
starting balances of participant i and the forthcoming stream of incomes, prices, and
interest rates. The conditional and unconditional optimal solutions coincide in the first
period of each repetition.12
12Note that one of the advantages of our indices is that they account for the loss in payoffs (utility)
when deviating from the unconditional and conditional paths, rather than just measuring deviations in
20

In our experiment, participants have complete information about the lifetime stream
of income, prices, and interest rates they will encounter in each sequence. According to
standard rational-agent economic theory, agents knowledgeable in solving constrained
optimizationproblemswouldmakespendingdecisionsalignedwiththeunconditional op-
timal consumption path. Should they temporarily deviate from this optimal path, they
would be expected to make conditionally optimal decisions thereafter. The features and
complexity of the economic environment should not influence ability to optimize. This
| serves | as the | basis of | our | first hypothesis. |     |     |     |     |     |     |     |
| ------ | ------ | -------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
Hypothesis 1: (Un)conditional optimal consumption does not differ across environ-
ments or a presence of budgeting calculator: γConstantYP = γFluctY = γFluctP = γPosIR.
However, substantial evidence presented in Table 1 demonstrates significant devia-
tions from the (un)conditionally optimal consumption path in spending decisions. Re-
lated work by Gabaix and Graeber (2023) and Enke et al. (2023) highlight the role that
complexity plays in behavioral biases and optimization errors. They show that people
optimize better in environments that are relatively less complex. To identify and rank
the complexity of economic environments, we utilize the model from Gabaix and Grae-
ber (2023), which assesses complexity within an intertemporal consumption framework.
Their findings indicate that the level of complexity is determined by the number of non-
zero terms in a Taylor expansion of the optimal consumption level. Complexity increases
with the number of interacting variables when a term is non-zero. Hence, we initiate
this analysis by linearizing Equation \ref{eq } through a Taylor expansion:13
|     |     | y    | 1 T      |       |     | y (T −1) | (cid:18) | 1−σ | (cid:19) y | T        |     |
| --- | --- | ---- | -------- | ----- | --- | -------- | -------- | --- | ---------- | -------- | --- |
|     |     | 1    | (cid:88) |       |     | 1        |          |     | 1          | (cid:88) |     |
|     | c   | = +  |          | (y −y | )−  |          | r+       |     |            | (p −p )  | (9) |
|     | 1   |      |          | t     | 1   |          |          |     | Tp2        | t 1      |     |
|     |     | p Tp |          |       |     | 2σp      |          | σ   |            |          |     |
|     |     | 1    | 1 t=2    |       |     |          | 1        |     | 1          | t=2      |     |
Following Gabaix and Graeber (2023), each element of the problem is assumed to
| terms      | of consumption | values. |                |     |        |                   |     |     |     |     |     |
| ---------- | -------------- | ------- | -------------- | --- | ------ | ----------------- | --- | --- | --- | --- | --- |
| 13Appendix |                | A shows | the derivation |     | of the | Taylor expansion. |     |     |     |     |     |
21

have the same level of complexity, c¯.14 We assess that our ConstantYP environment
exhibits the least amount of complexity (normalized to zero complexity). The FluctY
treatment entails a complexity level of c¯, as individuals need to consider the horizon
when calculating optimal choices. Finally, FluctP and PosIR are predicted to have a
complexity level of 2c¯, as individuals now need to consider the interaction between the
horizon and the elasticity of substitution, σ. This leads to our alternative hypothesis
that the relative complexity across environments determines the relative ordering of op-
timization errors.
Alternative Hypothesis 1: (Un)conditional optimal consumption is ordered based on
the complexity of the environment: γConstantYP > γFluctY > γPosIR = γFluctP.
Given that all environments, with the exception of ConstantYP, exhibit inherent
complexity, computing the optimal level of consumption becomes a challenging task. It
is reasonable to anticipate that choices of individuals with access to a budgeting calcula-
tor would be closer to the optimal level of consumption than those without access to it.
This motivates our second hypothesis, which posits that the availability of a budgeting
tool significantly improves consumption decisions. Access to a budgeting calculator can
be particularly helpful for individuals who struggle with computing the optimal level,
even in less complex environments.
Hypothesis 2. The budgeting calculator improves (un)conditional optimal consump-
tion: γj,Calc > γj,NoCalc for environment j ∈ {ConstantYP,PosIR,FluctY,FluctP}.
By tracking the consumption decisions of participants over multiple repetitions, we
can evaluate how experience contributes to enhancements in their dynamic optimiza-
tion skills. Evidence from Ballinger et al. (2003) suggests that participants learn from
14For hypothesis formulation and testing purposes, we focus on ordinal ranking rather than cardinal
ranking.
22

experience. Our experimental design can capture this learning clearly. Comparing the
first and third repetitions, where changes are made only in nominal terms, the optimal
consumption paths remain unaltered.
Hypothesis 3. Deviations of consumption from the (un)conditional optimal consump-
tion paths decrease in later repetitions.
A fundamental distinction in calculating unconditional versus conditional optimal
paths lies in the respective planning approaches. For the unconditional path, it is nec-
essary to accurately determine the optimal consumption values for the entire horizon
immediately in period 1. This task becomes increasingly challenging with a longer hori-
zon. On the other hand, the conditional optimal path allows subjects to adjust their
plans in response to unfolding events as each period progresses, making it easier to stay
on or near the optimal path. Consequently, we hypothesize that with a shorter horizon
for optimization, subjects are more likely to make consumption decisions that align with
the conditional optimal path, as the reduced planning horizon simplifies the task.
Hypothesis 4. Deviations of consumption from the conditional optimal consumption
path decrease as the planning horizon becomes shorter.
Our final hypothesis links individual characteristics with dynamic optimization capabil-
ities. Dynamic optimization requires participants not only to perform complex financial
calculations but also to contemplate their future decisions. We hypothesize that mathe-
matical proficiency, financial literacy, and backward induction skills will positively cor-
relate with dynamic optimization abilities (see Lusardi and Wallace, 2013). Participants
endowed with these skills are likely better prepared to comprehend and effectively utilize
the budgeting tool, thereby achieving greater alignment with the optimal consumption
paths.
23

Hypothesis 5. Dynamic optimization is positively correlated with mathematical train-
| ing, financial | literacy, | and backward-induction |     | skills. |
| -------------- | --------- | ---------------------- | --- | ------- |
| 4 Overview     |           | of experimental        |     | results |
We begin with an overview of optimization performance and calculator usage across the
| different treatment. |     |             |           |     |
| -------------------- | --- | ----------- | --------- | --- |
| 4.1 Average          |     | consumption | decisions |     |
Figure 5 presents the mean consumption decisions over time for Repetitions 1 and 3
for each treatment, represented by solid black lines. The gray area indicates the 95%
confidence intervals.15 The optimal consumption path is denoted by red dashed lines.
Weonlyincludeperiods1to9becausetheconsumptiondecisioninPeriod10wastrivial;
to maximize their current utility, subjects had to spend all the available cash in their
bank account.16
Across different treatments, there are noticeable disparities in participants’ opti-
mization abilities. In the ConstantYP treatment, even in the first repetition, the mean
participant with access to the budgeting calculator consistently selects a consumption
| path that | is nearly | optimal. |     |     |
| --------- | --------- | -------- | --- | --- |
In other treatments, deviations from optimality exhibit distinct patterns. In the
PosIR treatment, the optimal path involves saving a relatively larger share of income in
early periods to take advantage of the compounding return. Participants often under-
estimate the benefits of early savings in their lifecycle, leading to overconsumption in
initial periods and underconsumption in subsequent periods. Their ability to optimize
| does not appear | to  | improve with experience.17 |     |     |
| --------------- | --- | -------------------------- | --- | --- |
15The individual time series for the consumption choices can be found in Appendix F.
16To make sure participants had no calculation errors, we displayed a message indicating the exact
consumption amount they needed to enter to spend it all. The vast majority followed this guidance.
Across all subjects and all repetitions, in 90 percent of the cases, they finished the repetition with no
| cash remaining | in their | bank account. |     |     |
| -------------- | -------- | ------------- | --- | --- |
17We also investigate a scenario where subjects perceive an increase in savings following a simple
24

)snekoT( noitpmusnoC Constant YP − Calc Rep 1 )snekoT( noitpmusnoC PosIR − Calc Rep 1 )snekoT( noitpmusnoC FluctY − Calc Rep 1 )snekoT( noitpmusnoC FluctP − Calc Rep 1
| 20  |     | 20  |     | 20  |     | 40  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
35
| 15  |     | 15  |     | 15  |     | 30  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
25
| 10  |     | 10  |     | 10  |     | 20    |     |
| --- | --- | --- | --- | --- | --- | ----- | --- |
| 5   |     | 5   |     | 5   |     | 15 10 |     |
5
| 0   |     | 0   |     | 0   |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9
|     | Period |     | Period |     | Period |     | Period |
| --- | ------ | --- | ------ | --- | ------ | --- | ------ |
)snekoT( noitpmusnoC Constant YP − Calc Rep 3 )snekoT( noitpmusnoC PosIR − Calc Rep 3 )snekoT( noitpmusnoC FluctY − Calc Rep 3 )snekoT( noitpmusnoC FluctP − Calc Rep 3
| 20  |     | 20  |     | 20  |     | 40    |     |
| --- | --- | --- | --- | --- | --- | ----- | --- |
| 15  |     | 15  |     | 15  |     | 35 30 |     |
25
| 10  |     | 10  |     | 10  |     | 20  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
15
| 5   |     | 5   |     | 5   |     | 10  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
5
| 0   |     | 0   |     | 0   |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9
|     | Period |     | Period |     | Period |     | Period |
| --- | ------ | --- | ------ | --- | ------ | --- | ------ |
Constant YP − No Calc Rep 1 PosIR − No Calc Rep 1 FluctY − No Calc Rep 1 FluctP − No Calc Rep 1
)snekoT( noitpmusnoC )snekoT( noitpmusnoC )snekoT( noitpmusnoC )snekoT( noitpmusnoC
| 20  |     | 20  |     | 20  |     | 40  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
35
| 15  |     | 15  |     | 15  |     | 30  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
25
| 10  |     | 10  |     | 10  |     | 20 15 |     |
| --- | --- | --- | --- | --- | --- | ----- | --- |
| 5   |     | 5   |     | 5   |     | 10    |     |
5
| 0   |     | 0   |     | 0   |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9
|     | Period |     | Period |     | Period |     | Period |
| --- | ------ | --- | ------ | --- | ------ | --- | ------ |
)snekoT( noitpmusnoC Constant YP − No Calc Rep 3 )snekoT( noitpmusnoC PosIR − No Calc Rep 3 )snekoT( noitpmusnoC FluctY − No Calc Rep 3 )snekoT( noitpmusnoC FluctP − No Calc Rep 3
| 20  |     | 20  |     | 20  |     | 40    |     |
| --- | --- | --- | --- | --- | --- | ----- | --- |
| 15  |     | 15  |     | 15  |     | 35 30 |     |
25
| 10  |     | 10  |     | 10  |     | 20  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
15
| 5   |     | 5   |     | 5   |     | 10  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
5
| 0   |     | 0   |     | 0   |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9
|     | Period |     | Period |     | Period |     | Period |
| --- | ------ | --- | ------ | --- | ------ | --- | ------ |
95% Confidence Interval Mean Consumption Unconditional Optimal
|     |     | Figure 5: Average | consumption | per period | and treatment |     |     |
| --- | --- | ----------------- | ----------- | ---------- | ------------- | --- | --- |
In the FluctY treatment, the optimal consumption path remains constant. Optimiz-
ing participants should save a portion of their income in odd-numbered periods to offset
lower income in even-numbered periods. In Repetition 1, less experienced participants
often under-consume in periods with lower income, leading to excessive saving and con-
sumption in Period 9. However, with increased experience, this tendency to oversave
diminishes, particularly when participants have access to the budgeting calculator.
In the FluctP treatment, the optimal plan involves setting aside some income during
odd-numbered periods when prices are relatively high and utilize their entire wealth
interest rate model. This implies that each saved token is believed to grow to an amount represented
(cid:80)T
by 1+ r by the end of a specified time horizon. Nonetheless, the data from PosIR cannot be
s=t s
| explained | by individuals | employing | this heuristic. |     |     |     |     |
| --------- | -------------- | --------- | --------------- | --- | --- | --- | --- |
25

during even-numbered periods. Although the average participant shows a basic under-
standing of how consumption should fluctuate with price changes, there is a marked
tendency to excessively smooth consumption. This leads to heightened consumption
in odd-numbered periods and inadequate consumption in even-numbered periods rela-
tive to the unconditionally optimal decision. This behavior remains up to Repetition 3.
However, experience leads to notable improvements in optimization, especially for those
participants who do not have access to a budgeting calculator.
Finally, regardless of the availability of a budgeting calculator, participants exhibit
distinct consumption smoothing behaviors across different treatments. In simpler treat-
ments like ConstantYP and FluctY, we observe a trend towards undersmoothing of
consumption among experienced participants. On the other hand, in more complex
treatments such as FluctP and PosIR, experienced participants demonstrate a tendency
for oversmoothing. While undersmoothing is not necessarily surprising in ConstantYP
and FluctY (this is the only direction suboptimal behavior can go in), it was ex-ante
unclear how much participants would smooth their consumption in PosIR and FluctP.
Thispatternsuggeststhatexcessconsumptionsmoothingrepresentsastrategicresponse
adopted by experienced individuals when navigating complex economic environments.
It resonates with the ‘wait-and-see’ approach, indicating that in scenarios marked by
uncertainty or complexity, the preferred strategy is to maintain the current course of
action, rather than implementing significant changes in consumption behavior.
4.2 Measuring Optimization Abilities: Unconditional and Con-
ditional Optimal Index
The distributions of γU (Unconditional Optimal Index) and γC (Conditional Optimal
Index) are shown in Figures 6 and 7, respectively. The distributions are broken down by
repetition and treatment. We separate the 90 to 95 percentage and 95 to 100 percentage
bins to highlight participants’ ability to nearly perfectly optimize, while allowing for the
possibility of rounding.
26

|     |                               | Constant YP                     |                              |                   |                               | PosIR                           |                              |
| --- | ----------------------------- | ------------------------------- | ---------------------------- | ----------------- | ----------------------------- | ------------------------------- | ---------------------------- |
|     | 80                            |                                 |                              | 80                | 80                            |                                 | 80                           |
|     | 70                            |                                 |                              | 70                | 70                            |                                 | 70                           |
|     | )%( egatnecreP 60             |                                 |                              | 60 )%( egatnecreP | 60                            |                                 | 60                           |
|     | 50                            |                                 |                              | 50                | 50                            |                                 | 50                           |
|     | 40                            |                                 |                              | 40                | 40                            |                                 | 40                           |
|     | 30                            |                                 |                              | 30                | 30                            |                                 | 30                           |
|     | 20                            |                                 |                              | 20                | 20                            |                                 | 20                           |
|     | 10                            |                                 |                              | 10                | 10                            |                                 | 10                           |
|     | 0                             |                                 |                              | 0                 | 0                             |                                 | 0                            |
|     | R1R2R3       R1R2R3           |   R1R2R3       R1R2R3           | R1R2R3       R1R2R3          |                   | R1R2R3       R1R2R3           |     R1R2R3       R1R2R3         | R1R2R3       R1R2R3          |
|     |   [0, 0.25)   [0 .25, 0.50 )  | [0 .50, 0.75 )  [0 .75, 0.90 )  | [0 .90, 0.95 )   [0.95, 1]   |                   |   [0, 0.25)   [0 .25, 0.50 )  | [0 .50, 0.75 )  [0 .75, 0.90 )  | [0 .90, 0.95 )   [0.95, 1]   |
|     |                               | UncOptIndex                     |                              |                   |                               | UncOptIndex                     |                              |
|     |                               | FluctY                          |                              |                   |                               | FluctP                          |                              |
|     | 80                            |                                 |                              | 80                | 80                            |                                 | 80                           |
|     | 70                            |                                 |                              | 70                | 70                            |                                 | 70                           |
|     | 60                            |                                 |                              | 60                | 60                            |                                 | 60                           |
|     | )%( egatnecreP                |                                 |                              | )%( egatnecreP    |                               |                                 |                              |
|     | 50                            |                                 |                              | 50                | 50                            |                                 | 50                           |
|     | 40                            |                                 |                              | 40                | 40                            |                                 | 40                           |
|     | 30                            |                                 |                              | 30                | 30                            |                                 | 30                           |
|     | 20                            |                                 |                              | 20                | 20                            |                                 | 20                           |
|     | 10                            |                                 |                              | 10                | 10                            |                                 | 10                           |
|     | 0                             |                                 |                              | 0                 | 0                             |                                 | 0                            |
R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3
|     |                               |                                 |                              |     |                               |                                 |                              |
| --- | ----------------------------- | ------------------------------- | ---------------------------- | --- | ----------------------------- | ------------------------------- | ---------------------------- |
|     |   [0, 0.25)   [0 .25, 0.50 )  | [0 .50, 0.75 )  [0 .75, 0.90 )  | [0 .90, 0.95 )   [0.95, 1]   |     |   [0, 0.25)   [0 .25, 0.50 )  | [0 .50, 0.75 )  [0 .75, 0.90 )  | [0 .90, 0.95 )   [0.95, 1]   |
|     |                               | UncOptIndex                     |                              |     |                               | UncOptIndex                     |                              |
|     |                               |                                 | No Calculator                |     | Calculator                    |                                 |                              |
|     |                               | Figure                          | 6: Histogram                 | of  | UncOptIndex                   |                                 |                              |
These histograms reveal three preliminary observations. First, there are significant
optimization errors across all of our treatments, even after significant experience. In
the simplest environment, where incomes and prices are constant and participants have
access to a budgeting calculator, one-quarter of the individuals deviate from the optimal
path by more than 10 percent in Repetition 3. And in more complicated environments
like PosIR and FluctP, deviations are significantly more substantial and persistent, re-
gardless of calculator accessibility. Surprisingly, this pattern does not change much for
| deviations | from the | conditional | optimal, | as shown | in Figure | 7.  |     |
| ---------- | -------- | ----------- | -------- | -------- | --------- | --- | --- |
Second, among those at the upper end of the distribution, participants’ abilities to
optimize dynamically—both unconditionally and conditionally—enhance with experi-
ence, particularly in relatively simple environments such as ConstantYP and FluctY.
This improvement is partly attributed to subjects who already had a good understand-
27

|                               | Constant YP                     |                              |                               | PosIR                           |                              |
| ----------------------------- | ------------------------------- | ---------------------------- | ----------------------------- | ------------------------------- | ---------------------------- |
| 80                            |                                 | 80                           | 80                            |                                 | 80                           |
| 70                            |                                 | 70                           | 70                            |                                 | 70                           |
| )%( egatnecreP 60             |                                 | 60                           | )%( egatnecreP 60             |                                 | 60                           |
| 50                            |                                 | 50                           | 50                            |                                 | 50                           |
| 40                            |                                 | 40                           | 40                            |                                 | 40                           |
| 30                            |                                 | 30                           | 30                            |                                 | 30                           |
| 20                            |                                 | 20                           | 20                            |                                 | 20                           |
| 10                            |                                 | 10                           | 10                            |                                 | 10                           |
| 0                             |                                 | 0                            | 0                             |                                 | 0                            |
| R1R2R3       R1R2R3           |   R1R2R3       R1R2R3           | R1R2R3       R1R2R3          | R1R2R3       R1R2R3           |   R1R2R3       R1R2R3           | R1R2R3       R1R2R3          |
|   [0, 0.25)   [0 .25, 0.50 )  | [0 .50, 0.75 )  [0 .75, 0.90 )  | [0 .90, 0.95 )   [0.95, 1]   |   [0, 0.25)   [0 .25, 0.50 )  | [0 .50, 0.75 )  [0 .75, 0.90 )  | [0 .90, 0.95 )   [0.95, 1]   |
|                               | CondOptIndex                    |                              |                               | CondOptIndex                    |                              |
|                               | FluctY                          |                              |                               | FluctP                          |                              |
| 80                            |                                 | 80                           | 80                            |                                 | 80                           |
| 70                            |                                 | 70                           | 70                            |                                 | 70                           |
| 60                            |                                 | 60                           | 60                            |                                 | 60                           |
| )%( egatnecreP                |                                 |                              | )%( egatnecreP                |                                 |                              |
| 50                            |                                 | 50                           | 50                            |                                 | 50                           |
| 40                            |                                 | 40                           | 40                            |                                 | 40                           |
| 30                            |                                 | 30                           | 30                            |                                 | 30                           |
| 20                            |                                 | 20                           | 20                            |                                 | 20                           |
| 10                            |                                 | 10                           | 10                            |                                 | 10                           |
| 0                             |                                 | 0                            | 0                             |                                 | 0                            |
R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3
|                               |                                 |                              |                               |                                 |                              |
| ----------------------------- | ------------------------------- | ---------------------------- | ----------------------------- | ------------------------------- | ---------------------------- |
|   [0, 0.25)   [0 .25, 0.50 )  | [0 .50, 0.75 )  [0 .75, 0.90 )  | [0 .90, 0.95 )   [0.95, 1]   |   [0, 0.25)   [0 .25, 0.50 )  | [0 .50, 0.75 )  [0 .75, 0.90 )  | [0 .90, 0.95 )   [0.95, 1]   |
|                               | CondOptIndex                    |                              |                               | CondOptIndex                    |                              |
|                               |                                 | No Calculator                | Calculator                    |                                 |                              |
|                               | Figure                          | 7: Histogram                 | of CondOptIndex               |                                 |                              |
ing of the problem in the first repetition, as they further improved their optimization
skillsbythethirdrepetition. Notably, betweenthefirstandthirdrepetitions, weobserve
a significant increase of approximately 15 percentage points in the proportion of partici-
pants achieving perfect optimization in ConstantYP, and a 10 percentage point increase
in FluctY. However, in more complex environments like PosIR and FluctP, where the
optimization challenge is greater, the observed effects are comparatively smaller.
Third, the presence of a budgeting calculator significantly influences optimization
in the ConstantYP treatment, more so than in the other treatments, particularly for
participants at the top of the distribution. This effect is less obvious for participants in
the middle or bottom of the distribution. In the ConstantYP environment, the presence
of the budgeting calculator shifts the distribution towards the right, resulting in a 14
percentage point increase in the proportion of participants who achieve perfect optimiza-
28

tion. However, the benefits provided by the calculator are less pronounced in the other
three environments.
4.3 Evaluation of hypotheses
Table 4 presents the mean deviation of the UncOptIndex (γU) and CondOptIndex (γC),
measured at the session level for each treatment and repetition. Additionally, we report
the mean deviations for time spent and the number of calculations attempted in the
Calculator treatments. Differences within and across treatments are documented, with
corrections applied for multiple hypothesis (List et al., 2019).
We find compelling evidence to reject Hypothesis 1, which predicts that there should
be no difference in deviations from both the unconditional and conditional optimal levels
ofconsumptionacrossdifferentenvironments. Controllingforaccesstothebudgetcalcu-
lator, both γU and γC are consistently higher in the ConstantYP environment compared
to other treatments across most repetitions. Participants also appear better optimize,
both unconditionally and conditionally, in the FluctY environment than in either PosIR
or FluctP. Notably, PosIR and FluctP exhibit marked similarities, especially when par-
ticipants do not have access to a budgeting calculator. From a broader perspective, the
treatment ordering aligns with Alternative Hypothesis 1 that considers the cognitive
complexity present within the economic environment.
Result 1: The ability to (un)conditionally optimize differs across environments:
γConstantYP > γFluctY > γPosIR = γFluctP.
Our results provide mixed support for Hypothesis 2, which posits that access to
the budgeting calculator significantly improves optimization for both unconditional and
conditional consumption decisions. In Repetition 1 and Repetition 3, access to the cal-
culator leads to reductions in mean deviations from the unconditional optimal path by
10.2% and 7.7% in ConstantYP and by 5.8% and 5.9% in PosIR, respectively. Cor-
29

|     |     | Table | 4: Summary | of treatment | effects |     |     |
| --- | --- | ----- | ---------- | ------------ | ------- | --- | --- |
Treatment
|     |     | ConstantYP | PosIR | FluctY FluctP |     | p-valueoftwosidedt-test |     |
| --- | --- | ---------- | ----- | ------------- | --- | ----------------------- | --- |
[1] [2] [3] [4] [1]vs[2] [1]vs[3] [1]vs[4] [2]vs[3] [2]vs[4] [3]vs[4]
Repetition1
Calculator 0.862 0.718 0.785 0.678 0.000 0.000 0.000 0.000 0.134 0.000
γU NoCalculator 0.760 0.661 0.778 0.621 0.000 0.718 0.000 0.000 0.286 0.000
|     | Difference | 0.102∗∗∗ | 0.058∗∗ | 0.007 0.057∗ |     |     |     |
| --- | ---------- | -------- | ------- | ------------ | --- | --- | --- |
Calculator 0.859 0.734 0.839 0.741 0.000 0.038 0.000 0.000 0.758 0.000
γC NoCalculator 0.780 0.680 0.826 0.693 0.000 0.517 0.000 0.000 0.878 0.000
|     | Difference | 0.079∗∗∗ | 0.054∗∗ | 0.013 0.049∗∗∗ |     |     |     |
| --- | ---------- | -------- | ------- | -------------- | --- | --- | --- |
Calculator 35.569 51.951 37.822 60.284 0.264 0.752 0.185 0.332 0.854 0.244
Seconds/period NoCalculator 35.301 38.615 30.600 47.383 0.616 0.647 0.046 0.654 0.666 0.000
|     | Difference | 0.268 | 13.336 | 7.221 12.901 |     |     |     |
| --- | ---------- | ----- | ------ | ------------ | --- | --- | --- |
No. Sim/period Calculator 3.705 5.046 4.060 4.162 0.871 0.966 0.953 0.944 0.958 0.922
Repetition2
Calculator 0.868 0.701 0.794 0.680 0.000 0.000 0.000 0.000 0.556 0.000
γU
NoCalculator 0.761 0.673 0.822 0.649 0.000 0.000 0.000 0.000 0.536 0.000
|     | Difference | 0.107∗∗∗ | 0.028 | -0.028 0.031 |     |     |     |
| --- | ---------- | -------- | ----- | ------------ | --- | --- | --- |
Calculator 0.869 0.713 0.849 0.736 0.000 0.602 0.000 0.000 0.507 0.000
γC NoCalculator 0.780 0.677 0.858 0.705 0.000 0.000 0.000 0.000 0.425 0.000
|     | Difference | 0.089∗∗∗ | 0.035 | -0.008 0.031 |     |     |     |
| --- | ---------- | -------- | ----- | ------------ | --- | --- | --- |
Calculator 21.792 37.784 25.208 34.988 0.421 0.604 0.038 0.534 0.770 0.215
Seconds/period NoCalculator 17.506 18.736 18.925 31.530 0.856 0.830 0.000 0.942 0.002 0.012
|     | Difference | 4.286 | 19.048 | 6.283 3.458 |     |     |     |
| --- | ---------- | ----- | ------ | ----------- | --- | --- | --- |
No. Sim/period Calculator 1.316 2.621 2.108 1.573 0.510 0.459 0.961 0.986 0.790 0.920
Repetition3
Calculator 0.897 0.761 0.829 0.703 0.000 0.000 0.000 0.000 0.000 0.000
γU NoCalculator 0.820 0.702 0.840 0.680 0.000 0.567 0.000 0.000 0.603 0.000
|     | Difference | 0.077∗∗∗ | 0.059∗∗∗ | -0.011 0.023 |     |     |     |
| --- | ---------- | -------- | -------- | ------------ | --- | --- | --- |
Calculator 0.902 0.766 0.875 0.760 0.000 0.210 0.000 0.000 0.887 0.000
γC
NoCalculator 0.836 0.708 0.888 0.728 0.000 0.000 0.000 0.000 0.471 0.000
|     | Difference | 0.066∗∗∗ | 0.059∗ | -0.013 0.032 |     |     |     |
| --- | ---------- | -------- | ------ | ------------ | --- | --- | --- |
Calculator 20.146 29.726 22.263 29.771 0.387 0.905 0.269 0.532 0.994 0.432
Seconds/period NoCalculator 13.118 15.518 16.821 21.637 0.527 0.130 0.000 0.482 0.021 0.123
|     | Difference | 7.028 | 14.209 | 5.442 8.134 |     |     |     |
| --- | ---------- | ----- | ------ | ----------- | --- | --- | --- |
No. Sim/period Calculator 1.395 2.075 1.785 1.478 0.910 0.953 0.974 0.976 0.944 0.972
p-valueoftwosidedt-test(comparisonsacrossrepetitions)
|     |            |            | Calculator |               |            | NoCalculator |               |
| --- | ---------- | ---------- | ---------- | ------------- | ---------- | ------------ | ------------- |
|     |            | ConstantYP | PosIR      | FluctY FluctP | ConstantYP | PosIR        | FluctY FluctP |
|     | Rep1vsRep2 | 0.985      | 0.741      | 0.615 0.941   | 0.998      | 0.707        | 0.054 0.693   |
γu
|     | Rep1vsRep3 | 0.020 | 0.036 | 0.112 0.659 | 0.020 | 0.191 | 0.000 0.068 |
| --- | ---------- | ----- | ----- | ----------- | ----- | ----- | ----------- |
|     | Rep2vsRep3 | 0.024 | 0.000 | 0.189 0.702 | 0.024 | 0.556 | 0.663 0.568 |
|     | Rep1vsRep2 | 0.935 | 0.650 | 0.690 0.891 | 0.986 | 0.887 | 0.202 0.842 |
γc Rep1vsRep3 0.009 0.204 0.131 0.733 0.019 0.615 0.000 0.478
|     | Rep2vsRep3 | 0.093 | 0.011 | 0.315 0.671 | 0.005 | 0.470 | 0.135 0.737 |
| --- | ---------- | ----- | ----- | ----------- | ----- | ----- | ----------- |
|     | Rep1vsRep2 | 0.000 | 0.613 | 0.144 0.299 | 0.000 | 0.113 | 0.000 0.000 |
Seconds/period Rep1vsRep3 0.000 0.081 0.041 0.138 0.000 0.080 0.000 0.000
|                | Rep2vsRep3 | 0.246 | 0.755 | 0.769 0.775 | 0.246 | 0.696 | 0.753 0.098 |
| -------------- | ---------- | ----- | ----- | ----------- | ----- | ----- | ----------- |
|                | Rep1vsRep2 | 0.007 | 0.032 | 0.012 0.006 |       |       |             |
| No. Sim/period | Rep1vsRep3 | 0.008 | 0.010 | 0.000 0.009 |       |       |             |
|                | Rep2vsRep3 | 0.965 | 0.865 | 0.914 0.823 |       |       |             |
Notes: Thep-valuesreportedareobtainedfromt-testsandhavebeencorrectedformultiplehypothesistesting. Significancelevelsaredenoted
asfollows: ∗p<0.1,∗∗p<0.05,∗∗∗p<0.01
30

respondingly, the improvements in the conditional optimal path are 7.9% and 6.6% in
ConstantYP, and 5.4% and 5.9% in PosIR for Repetitions 1 and 3. All these differences
are statistically significant at the 5% level. However, the evidence indicates that in the
FluctY and FluctP treatments, the calculator’s availability does not significantly impact
the optimization of either unconditional or conditional consumption.
Result 2: Access to a budgeting tool does not consistently improve dynamic optimiza-
tion across environments.
Our findings indicate a complex interaction between experience and the use of the
budgeting calculator in guiding subjects towards the unconditional and conditional op-
timal consumption paths. This observation challenges Hypothesis 3, which posits that
deviations from these optimal paths should diminish in later repetitions. Our compara-
tive analysis of γU and γC across different treatments and between repetitions highlights
inconsistencies in the effects of the calculator. PosIR Calc is the only treatment that
consistently demonstrates improvements in optimization over time. For subjects with
access to the calculator in ConstantYP and FluctY, experience does not significantly en-
hance performance. As previously shown, experience appears to primarily benefit those
who were already close to the optimal paths in the first repetition. The limited learning
observed over time in calculator treatments may be attributed to subjects gathering
most of their learning during the first repetition. While the calculator appears to be
useful in exploring various plans and improves learning within a single repetition, this
improvement does not seem to carry over to subsequent repetitions.
On the other hand, in situations where participants do not have access to a calcula-
tor, there is evidence of learning occurring across multiple repetitions, with the PosIR
treatment again being a notable outlier. This finding is significant for experimental
designs where subjects accumulate interest on savings. Our results show that without
the aid of a calculator, learning from stationary repetitions is limited, emphasizing the
crucial role the budgeting tools can play in enhancing learning.
31

Result 3: Deviations in consumption from the unconditional and conditional optimal
consumption paths do not consistently decrease with experience, particularly when sub-
| jects have | access | to a budgeting | tool. |     |     |     |
| ---------- | ------ | -------------- | ----- | --- | --- | --- |
Our remaining hypotheses that relate to the planning horizon and demographic char-
acteristics are explored in the following sections where we exploit our experiments’ panel
data structure. Before we discuss our final hypothesis tests, we divert readers’ attention
to a brief analysis of participants’ usage of the budgeting calculator.
| 4.4 | How | Participants | Use | the Budgeting |     | Calculator |
| --- | --- | ------------ | --- | ------------- | --- | ---------- |
All calculations computed in the budgeting calculator were recorded. This dataset en-
ables an evaluation of how participants engaged with the calculator and the impact of
this engagement on decision-making. We observe five distinct patterns in how partici-
| pants filled | in  | the budgeting | calculator | in period | t.  |     |
| ------------ | --- | ------------- | ---------- | --------- | --- | --- |
1. Complete: All entries between t and T = 10 are inputted in each calculation.
2. Sequential: Entries and calculations are conducted sequentially. Subjects compute
Period t calculations first, followed by Periods t and t+1, and again t, t+1, t+2,
| until | they | reach T. |     |     |     |     |
| ----- | ---- | -------- | --- | --- | --- | --- |
3. Partial: Less than T −t+1 periods are entered into the calculator.18
| 4. Current |         | Period: Only    | Period t | consumption | is inputted. |     |
| ---------- | ------- | --------------- | -------- | ----------- | ------------ | --- |
| 5. No      | Inputs: | No calculations | are      | made.       |              |     |
How would a fully forward-looking, perfectly optimizing agent utilize the calculator?
If they understand how to solve the optimization problem, they should not spend time
18ThistypeofbehaviorhasbeenmodeledbyCaliendoandAadland(2007). Intheirmodel, forward-
lookingindividualssolvepartial-horizonmodels. Theyspeculatethatsuchbehaviorinindividualsstems
from factors including “...lack of self-control, financial illiteracy, distaste for contemplating old age, or
to avoid financial planning costs in an uncertain environment, among others.”
32

doinganycalculations. Ontheotherhand, iftheyareforward-lookingbuthavedifficulty
with the computational aspect of the problem, they should submit a complete set of
entries before making their spending decisions. We observe participants complete the
calculatorintwoways: eitherimmediatelyfillinginthecalculatorentirelybeforepressing
the Calculate button, or sequentially with at least T −t+1 calculations, inputting and
calculating one period at a time. This latter approach takes more time but provides
participantsanopportunitytosalientlyobservetheimpactofeachperiod’sconsumption-
saving decision. Participants inputting fewer than T −t+1 periods into the calculator
arecategorizedasPartial orCurrent-Period, andarealsoreferredtoasmyopic planners.
It is important to note that the subjects in the Calculator treatments are not re-
quired to use the budgeting calculator when making their spending decisions. As shown
in Figure 8, the percentage of subjects who do not activate the calculator increases over
time. There are several reasons for this trend: (i) subjects do not need to make cal-
culations every period to determine the optimal consumption path, especially in simple
environments, (ii) subjects underwent an extensive tutorial and practice period before
starting the experiment, (iii) minor changes in the environments between repetitions
may allow subjects to rely on past repetitions to approximate the optimal approach,
and (iv) subjects may experience fatigue after a few periods. Despite this, roughly one-
half of the subjects submit complete sequences of consumption values at the beginning
of each repetition. This is consistent with subjects understanding that the environment
is deterministic, and in order to calculate the unconditional optimal, they must submit
full sequences. Note that if subjects were to attempt to calculate the conditional opti-
mal solution, they may use the calculator in periods 2 to 10, but there is little evidence
of that. Furthermore, there is a constant share of subjects using the calculator to en-
ter consumption values for the current period (between 5% and 20% depending on the
treatment), with only a few subjects partially or sequentially using the calculator over
time.
Considering the notable decline in calculator usage observed after the initial period
of each repetition, we assign participants to a specific Calculator Type based solely on
33

|     |            | Figure                              | 8: Budgeting   |     | Calculator | Types                               | Over       | Time   |          |
| --- | ---------- | ----------------------------------- | -------------- | --- | ---------- | ----------------------------------- | ---------- | ------ | -------- |
|     |            |                                     | ConstantYP     |     |            |                                     |            | PosIR  |          |
|     | 100        |                                     |                |     |            | 100                                 |            |        |          |
|     |            | 80                                  |                |     |            | 80                                  |            |        |          |
|     | stcejbuS % |                                     |                |     | stcejbuS % |                                     |            |        |          |
|     |            | 60                                  |                |     |            | 60                                  |            |        |          |
|     |            | 40                                  |                |     |            | 40                                  |            |        |          |
|     |            | 20                                  |                |     |            | 20                                  |            |        |          |
|     |            | 0                                   |                |     |            | 0                                   |            |        |          |
|     |            | 12345678910 12345678910 12345678910 |                |     |            | 12345678910 12345678910 12345678910 |            |        |          |
|     |            |                                     | Period         |     |            |                                     |            | Period |          |
|     |            |                                     | FluctY         |     |            |                                     |            | FluctP |          |
|     | 100        |                                     |                |     |            | 100                                 |            |        |          |
|     |            | 80                                  |                |     |            | 80                                  |            |        |          |
|     | stcejbuS % |                                     |                |     | stcejbuS % |                                     |            |        |          |
|     |            | 60                                  |                |     |            | 60                                  |            |        |          |
|     |            | 40                                  |                |     |            | 40                                  |            |        |          |
|     |            | 20                                  |                |     |            | 20                                  |            |        |          |
|     |            | 0                                   |                |     |            | 0                                   |            |        |          |
|     |            | 12345678910 12345678910 12345678910 |                |     |            | 12345678910 12345678910 12345678910 |            |        |          |
|     |            |                                     | Period         |     |            |                                     |            | Period |          |
|     |            | No Inputs                           | Current Period |     |            | Partial                             | Sequential |        | Complete |
their calculator usage during the first period. The distribution of types is summarized
| in Figure    | 9.  |     |                 |     |     |     |     |     |     |
| ------------ | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
| 5 Evaluation |     |     | of optimization |     |     |     |     |     |     |
In this section, we formally assess the efficacy of the budgeting calculator in improving
consumer optimization. We examine the impacts of the calculator, its usage, learning
outcomes, and demographic factors using the following comprehensive random-effects
| panel | regression | model | for each respective |     | environment: |     |     |     |     |
| ----- | ---------- | ----- | ------------------- | --- | ------------ | --- | --- | --- | --- |
Calculator×CalculatorTypet=1
|     | γ       | =a+b Calculator+b |      |             |     |              |     |        |         |
| --- | ------- | ----------------- | ---- | ----------- | --- | ------------ | --- | ------ | ------- |
|     | i,q,r,t | 0                 |      | 1           |     |              |     | i,q,r  |         |
|     |         | +b V              | +b X | +b Period+b |     | Repetition+µ |     | +error | ,       |
|     |         | 2 i,q,r,t         | 3    | i 4         |     | 5            |     | i      | i,q,r,t |
34

|                |     | Constant YP |     |                |     | PosIR |     |     |
| -------------- | --- | ----------- | --- | -------------- | --- | ----- | --- | --- |
|                | 80  |             |     |                | 80  |       |     |     |
|                | 70  |             |     |                | 70  |       |     |     |
| )%( egatnecreP | 60  |             |     | )%( egatnecreP | 60  |       |     |     |
|                | 50  |             |     |                | 50  |       |     |     |
|                | 40  |             |     |                | 40  |       |     |     |
|                | 30  |             |     |                | 30  |       |     |     |
|                | 20  |             |     |                | 20  |       |     |     |
|                | 10  |             |     |                | 10  |       |     |     |
|                | 0   |             |     |                | 0   |       |     |     |
R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3
|     |       |           |         |       |       |           |         |       |
| --- | ----- | --------- | ------- | ----- | ----- | --------- | ------- | ----- |
 N o input s  Cur rent Pe riod  Partial   S equentia l  C omplet e  N o input s  Cur rent Pe riod  Partial   S equentia l  C omplet e
|                |     |        |     |                |     |        |     |     |
| -------------- | --- | ------ | --- | -------------- | --- | ------ | --- | --- |
|                |     | FluctY |     |                |     | FluctP |     |     |
|                | 80  |        |     |                | 80  |        |     |     |
|                | 70  |        |     |                | 70  |        |     |     |
| )%( egatnecreP | 60  |        |     | )%( egatnecreP | 60  |        |     |     |
|                | 50  |        |     |                | 50  |        |     |     |
|                | 40  |        |     |                | 40  |        |     |     |
|                | 30  |        |     |                | 30  |        |     |     |
|                | 20  |        |     |                | 20  |        |     |     |
|                | 10  |        |     |                | 10  |        |     |     |
|                | 0   |        |     |                | 0   |        |     |     |
R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3 R1R2R3
|     |       |           |         |       |       |           |         |       |
| --- | ----- | --------- | ------- | ----- | ----- | --------- | ------- | ----- |
 N o input s  Cur rent Pe riod  Partial   S equentia l  C omplet e  N o input s  Cur rent Pe riod  Partial   S equentia l  C omplet e
|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure 9: Budgeting calculator usage types, by treatment and repetition
here, γ represents either UncOptIndex or CondOptIndex . The variable
|     | i,q,r,t |     |     | i,q,r,t |     | i,q,r,t |     |     |
| --- | ------- | --- | --- | ------- | --- | ------- | --- | --- |
Calculator is a dummy variable that takes the value of 1 in treatments where the
budgeting calculator is present, and 0 otherwise. Additionally, CalculatorTypet=1 is
i,q,r
a categorical variable categorizing participants into one of five calculator usage types,
| with | NoCalc serving | as the | baseline category. |     |     |     |     |     |
| ---- | -------------- | ------ | ------------------ | --- | --- | --- | --- | --- |
We include time-varying controls denoted as V , which capture various factors
i,q,r,t
such as the amount of time spent in a given period t (denoted as Minutes Spent) and
the cumulative count of calculations performed by the participant since the beginning
of Repetition 1 (denoted as No. of Calculations). It is important to emphasize that
participants who chose to use the budgeting calculator had the freedom to either search
for the optimal levels or enter any desired consumption values. Therefore, it is crucial to
distinguish between participants who effectively used the calculator to find the optimal
levels and those who did not. We define a participant as able to find the optimal
consumption if, when using the calculator, their UncOptIndex and CondOptIndex are
equal to or greater than 0.90 at any point up to period t within the repetition. Thus, we
35

introduce the binary variables Calc γU and Calc γC, which take the value of 1 if subjects
were able to calculate the optimal consumption levels or 0 otherwise.
Furthermore, time-invariant demographic controls, denoted as X , are included to
i
account for participant characteristics unrelated to decisions made in the experiment.
These include variables such as math background score (ranging from 1 to 9), finan-
cial literacy score (ranging from 0 to 4), backward induction ability (number of wins in
Race-to-60, ranging from 0 to 8), gender, age, institution, level of education, experience
in previous experiments, risk tolerance, the number of years as a student, and perfor-
mance on control questions. This last variable measures the accuracy and consistency
of responses to a set of incentivized control questions designed to assess understanding
of the experimental setup and procedures.
Repetition = {Rep2,Rep3} is a vector of dummy variables that captures the effects
of learning from experience. Period = t is a discrete variable that evaluates how the
length of the planning horizon affects optimization. Lastly, the subject-specific random
effect is denoted by µ .
i
5.1 Impact of Calculator Usage on Dynamic Optimization
ˆ
The estimated coefficient on the Calculator dummy variable, b , presented in Columns
0
(1), (4), (7), and (10) of Tables 5 and 6 indicates how the presence of the calculator
ˆ
affects optimization. To further evaluate Hypothesis 2, we test whether b > 0 for each
0
ˆ
environment. For both unconditional and conditional optimization, we find that b is
0
very small, ranging between 0-4 p.p. and not statistically different from zero in any
environment.
In the initial period, participants can significantly improve their dynamic optimiza-
tion capabilities by utilizing the calculator. In the simplest environment, ConstantYP,
filling in the calculator with only the current period (first period), either partially or
completely, improves unconditional optimization by approximately 7 to 11 percentage
points (p.p.) and conditional optimization by around 6 to 11 p.p. compared to partici-
36

| pants | who do | not activate | the | calculator. |     |     |     |     |     |     |     |     |     |
| ----- | ------ | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Sequential completion of the calculator resulted in a less sizeable and significant
effect. On average, there is only a 4 percentage point improvement for unconditional
|     |                |        | Table      | 5: Dependent |        | Variable: | OptUncIndex |        |        |          |        |        |          |
| --- | -------------- | ------ | ---------- | ------------ | ------ | --------- | ----------- | ------ | ------ | -------- | ------ | ------ | -------- |
|     |                |        | ConstantYP |              |        | POSIR     |             |        | FluctY |          |        | FluctP |          |
|     |                | (1)    | (2)        | (3)          | (4)    | (5)       | (6)         | (7)    | (8)    | (9)      | (10)   | (11)   | (12)     |
|     | Calculator     | 0.043  |            |              | 0.006  |           |             | 0.013  |        |          | 0.014  |        |          |
|     |                | (0.04) |            |              | (0.04) |           |             | (0.04) |        |          | (0.04) |        |          |
| No. | ofCalculations |        | -0.000     |              |        | -0.001    |             |        | -0.000 |          |        | 0.001  |          |
|     |                |        | (0.00)     |              |        | (0.00)    |             |        | (0.00) |          |        | (0.00) |          |
|     | CalcγU         |        |            | 0.094∗∗∗     |        |           | 0.194∗∗∗    |        |        | 0.118∗∗∗ |        |        | 0.105∗∗∗ |
|     |                |        |            | (0.03)       |        |           | (0.03)      |        |        | (0.02)   |        |        | (0.03)   |
MinutesSpent -0.018∗∗∗ -0.018∗∗∗ -0.019∗∗∗ -0.009∗∗∗ -0.006∗ -0.010∗∗∗ -0.012∗∗∗ -0.011∗∗ -0.012∗∗∗ 0.002 0.001 0.002
(0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.01) (0.00) (0.00) (0.00) (0.00)
|     |             |       |       |       |        |        |        | 0.027∗∗∗ | 0.027∗∗∗ | 0.034∗∗∗ | 0.022∗ | 0.023∗ |       |
| --- | ----------- | ----- | ----- | ----- | ------ | ------ | ------ | -------- | -------- | -------- | ------ | ------ | ----- |
|     | Repetition2 | 0.013 | 0.014 | 0.014 | -0.004 | -0.004 | -0.005 |          |          |          |        |        | 0.019 |
(0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01)
Repetition3 0.056∗∗∗ 0.058∗∗∗ 0.059∗∗∗ 0.039∗∗∗ 0.039∗∗∗ 0.033∗∗∗ 0.050∗∗∗ 0.050∗∗∗ 0.055∗∗∗ 0.049∗∗∗ 0.050∗∗∗ 0.044∗∗∗
(0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01)
-0.004∗∗∗ -0.004∗∗∗ -0.004∗∗∗ -0.003∗∗ -0.003∗∗ -0.003∗∗ -0.006∗∗∗ -0.006∗∗∗ -0.006∗∗∗ 0.004∗∗ 0.004∗∗ 0.004∗∗
Period
(0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00)
MathLevel 0.017 0.013 0.013 0.006 0.006 0.003 0.006 0.006 0.008 0.024∗∗∗ 0.024∗∗∗ 0.022∗∗
(0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01)
BackwardInduction 0.016 0.015 0.013 0.008 0.008 0.003 0.003 0.002 0.004 0.013 0.013 0.012
(0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.02) (0.02) (0.02) (0.01) (0.01) (0.01)
FinancialLiteracy 0.015 0.013 0.013 0.003 0.003 0.000 0.008 0.008 0.005 0.000 -0.001 0.001
(0.02) (0.02) (0.02) (0.02) (0.02) (0.02) (0.02) (0.02) (0.02) (0.02) (0.02) (0.02)
|     |     |     |     |     |     |     |     |     |     |     | -0.062∗ | -0.063∗ | -0.061∗ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------- |
Gender(1=Female) -0.026 -0.033 -0.030 -0.032 -0.031 -0.035 0.002 0.001 -0.001
(0.04) (0.04) (0.04) (0.04) (0.04) (0.03) (0.04) (0.04) (0.04) (0.04) (0.04) (0.03)
Age -0.002 -0.002 -0.002 0.004 0.004 0.004 -0.000 -0.000 0.000 -0.005 -0.004 -0.005
(0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00)
|     |     |     |     |     | 0.018∗∗∗ | 0.018∗∗∗ | 0.016∗∗∗ |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | -------- | -------- | --- | --- | --- | --- | --- | --- |
ControlQuestions 0.004 0.005 0.004 0.009 0.009 0.010 -0.006 -0.006 -0.005
(0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01)
CalculatorUsage
CurrentPeriod 0.071∗∗ 0.080∗∗∗ 0.077∗∗∗ -0.022 -0.020 -0.015 -0.057∗∗ -0.056∗∗ -0.043 0.003 0.006 0.018
(0.03) (0.03) (0.03) (0.03) (0.03) (0.03) (0.03) (0.03) (0.03) (0.03) (0.03) (0.03)
|     |         | 0.108∗∗∗ | 0.115∗∗∗ | 0.090∗∗∗ | 0.047∗ | 0.049∗ | 0.061∗∗ |       |       | 0.045∗ |       |       |       |
| --- | ------- | -------- | -------- | -------- | ------ | ------ | ------- | ----- | ----- | ------ | ----- | ----- | ----- |
|     | Partial |          |          |          |        |        |         | 0.038 | 0.038 |        | 0.007 | 0.011 | 0.013 |
(0.03) (0.03) (0.03) (0.03) (0.03) (0.03) (0.03) (0.03) (0.03) (0.03) (0.03) (0.03)
Sequential 0.040 0.047∗ -0.009 -0.084∗∗∗ -0.080∗∗ -0.179∗∗∗ 0.011 0.011 -0.054∗∗ -0.001 0.002 -0.039
(0.03) (0.03) (0.03) (0.03) (0.03) (0.03) (0.02) (0.02) (0.02) (0.03) (0.03) (0.03)
0.079∗∗∗ 0.087∗∗∗ 0.090∗∗∗ 0.093∗∗∗ -0.056∗ -0.033∗ -0.097∗∗∗ 0.073∗∗∗ 0.076∗∗∗
|     | Complete |     |     | 0.023 |     |     |     | -0.032 |     |     |     |     | 0.036 |
| --- | -------- | --- | --- | ----- | --- | --- | --- | ------ | --- | --- | --- | --- | ----- |
(0.02) (0.02) (0.03) (0.03) (0.02) (0.03) (0.02) (0.02) (0.02) (0.03) (0.02) (0.03)
Constant 0.545∗ 0.544∗ 0.589∗∗ -0.321 -0.321 -0.178 0.347 0.334 0.286 0.832 0.853∗ 0.813
(0.31) (0.31) (0.30) (0.33) (0.33) (0.30) (0.34) (0.36) (0.35) (0.51) (0.51) (0.50)
Observations 2640 2640 2640 2730 2730 2730 2820 2820 2820 2790 2790 2790
OverallR2 0.12 0.12 0.14 0.08 0.08 0.13 0.05 0.05 0.09 0.08 0.08 0.09
Notes: Thistabledisplaystheoutcomesofarandomeffectspanelregressionanalysis. Theregressionmodelsincorporatedemographiccontrol
variables,includinggender,age,priorexperimentalexperience,academicdegree,affiliatedinstitution,currentyearofstudy,andrisktolerance
levels. Additionally, we control for participants’ comprehension of the instructions, by adding the participants’ performance in the control
∗p<0.1,∗∗p<0.05,∗∗∗p<0.01
| questions. | Standarderrorsarepresentedinparentheses. |     |     |     | Significancelevelsaredenotedasfollows: |     |     |     |     |     |     |     |     |
| ---------- | ---------------------------------------- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
37

|                    |     |        | Table    | 6: Dependent |        | Variable: | OptCondIndex |        |        |          |        |        |          |
| ------------------ | --- | ------ | -------- | ------------ | ------ | --------- | ------------ | ------ | ------ | -------- | ------ | ------ | -------- |
|                    |     |        | Constant | YP           |        | POS       | IR           |        | FluctY |          |        | FluctP |          |
|                    |     | (1)    | (2)      | (3)          | (4)    | (5)       | (6)          | (7)    | (8)    | (9)      | (10)   | (11)   | (12)     |
| Calculator         |     | 0.037  |          |              | 0.001  |           |              | -0.000 |        |          | 0.012  |        |          |
|                    |     | (0.04) |          |              | (0.04) |           |              | (0.04) |        |          | (0.03) |        |          |
| No. ofCalculations |     |        | -0.001   |              |        | -0.001    |              |        | -0.000 |          |        | 0.000  |          |
|                    |     |        | (0.00)   |              |        | (0.00)    |              |        | (0.00) |          |        | (0.00) |          |
| CalcγC             |     |        |          | 0.095∗∗∗     |        |           | 0.070∗∗∗     |        |        | 0.060∗∗∗ |        |        | 0.091∗∗∗ |
|                    |     |        |          | (0.02)       |        |           | (0.02)       |        |        | (0.02)   |        |        | (0.02)   |
MinutesSpent -0.003 -0.001 -0.003 0.001 0.003 0.000 0.001 0.002 0.001 0.007∗∗∗ 0.006∗ 0.006∗∗
(0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00)
Repetition2 0.015∗ 0.016∗ 0.017∗∗ -0.008 -0.008 -0.005 0.024∗∗∗ 0.024∗∗∗ 0.026∗∗∗ 0.011 0.012 0.019
(0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01)
Repetition3 0.059∗∗∗ 0.060∗∗∗ 0.061∗∗∗ 0.033∗∗∗ 0.033∗∗∗ 0.036∗∗∗ 0.047∗∗∗ 0.047∗∗∗ 0.045∗∗∗ 0.036∗∗∗ 0.037∗∗∗ 0.041∗∗∗
(0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01)
Period 0.009∗∗∗ 0.009∗∗∗ 0.009∗∗∗ 0.023∗∗∗ 0.023∗∗∗ 0.023∗∗∗ 0.010∗∗∗ 0.010∗∗∗ 0.009∗∗∗ 0.020∗∗∗ 0.020∗∗∗ 0.019∗∗∗
(0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00)
|     |     |     |     |     |     |     |     |     |     |     | 0.019∗∗ | 0.019∗∗ | 0.018∗∗ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------- |
MathLevel 0.017 0.014 0.014 0.005 0.005 0.006 0.004 0.004 0.004
(0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01)
BackwardInduction 0.017 0.016 0.012 0.007 0.007 0.006 0.001 0.001 0.002 0.010 0.010 0.010
(0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01)
FinancialLiteracy 0.018 0.016 0.018 0.002 0.002 0.004 0.010 0.010 0.012 0.003 0.002 0.003
(0.02) (0.02) (0.02) (0.02) (0.02) (0.02) (0.02) (0.02) (0.02) (0.02) (0.02) (0.02)
Gender(1=Female) -0.030 -0.036 -0.036 -0.018 -0.017 -0.016 0.002 0.002 0.003 -0.062∗∗ -0.063∗∗ -0.058∗
(0.04) (0.04) (0.04) (0.03) (0.03) (0.03) (0.03) (0.03) (0.03) (0.03) (0.03) (0.03)
Age -0.001 -0.002 -0.002 0.003 0.003 0.003 0.000 0.000 0.001 -0.005 -0.005 -0.005
(0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00)
|     |     |     |     |     | 0.018∗∗∗ | 0.018∗∗∗ | 0.016∗∗ | 0.010∗ |     | 0.010∗ |     |     |     |
| --- | --- | --- | --- | --- | -------- | -------- | ------- | ------ | --- | ------ | --- | --- | --- |
ControlQuestions 0.006 0.007 0.006 0.010 -0.007 -0.007 -0.006
(0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01)
CalculatorUsage
CurrentPeriod 0.071∗∗∗ 0.077∗∗∗ 0.061∗∗∗ 0.006 0.006 0.001 -0.043∗ -0.044∗ -0.046∗∗ -0.000 0.003 0.005
(0.02) (0.02) (0.02) (0.03) (0.03) (0.03) (0.02) (0.02) (0.02) (0.03) (0.03) (0.03)
Partial 0.103∗∗∗ 0.110∗∗∗ 0.083∗∗∗ 0.051∗∗ 0.052∗∗ 0.044∗ 0.038 0.036 0.031 -0.020 -0.017 0.000
(0.02) (0.02) (0.02) (0.03) (0.02) (0.02) (0.02) (0.02) (0.02) (0.03) (0.03) (0.03)
Sequential 0.019 0.025 -0.030 -0.049 -0.047 -0.074∗∗ 0.015 0.014 -0.002 0.009 0.012 0.017
(0.02) (0.02) (0.02) (0.03) (0.03) (0.03) (0.02) (0.02) (0.02) (0.03) (0.03) (0.03)
Complete 0.060∗∗∗ 0.067∗∗∗ 0.008 0.087∗∗∗ 0.089∗∗∗ 0.067∗∗∗ -0.015 -0.017 -0.046∗∗ 0.072∗∗∗ 0.075∗∗∗ 0.052∗∗
(0.02) (0.02) (0.02) (0.02) (0.02) (0.02) (0.02) (0.02) (0.02) (0.03) (0.02) (0.02)
Constant 0.328 0.328 0.404 -0.448 -0.449 -0.403 0.227 0.226 0.217 0.835∗ 0.852∗ 0.802∗
(0.28) (0.28) (0.27) (0.31) (0.31) (0.31) (0.29) (0.31) (0.30) (0.45) (0.45) (0.44)
Observations 2640 2640 2640 2730 2730 2730 2820 2820 2820 2790 2790 2790
OverallR2 0.16 0.16 0.18 0.15 0.15 0.15 0.07 0.07 0.10 0.12 0.12 0.13
Notes: Thistabledisplaystheoutcomesofarandomeffectspanelregressionanalysis. Theregressionmodelsincorporatedemographiccontrol
variables,includinggender,age,priorexperimentalexperience,academicdegree,affiliatedinstitution,currentyearofstudy,andrisktolerance
levels. Additionally, we control for participants’ comprehension of the instructions, by adding the participants’ performance in the control
questions. Standarderrorsarepresentedinparentheses. Significancelevelsaredenotedasfollows: ∗p<0.1,∗∗p<0.05,∗∗∗p<0.01
optimization and a 2 percentage point improvement for conditional optimization. These
improvements are not statistically significant. By contrast, Complete types experience
| a 8 p.p.(6 | p.p.) | improvement |     | in (un)conditional |     |     | optimization. |     |     |     |     |     |     |
| ---------- | ----- | ----------- | --- | ------------------ | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
38

InthePosIRenvironment,characterizedbycompoundinginterestonsavings,notable
performance disparities were observed across the different Calculator Types. When
participants only complete the consumption decision for the current period, there is no
improvement in optimization. However, the Partial and Complete Calculator Types
show improvements of 5 and 9 percentage points, respectively, in their optimization.
Moreover, imperfectly using the calculator still leads to significant improvements in
conditional optimization (Column 6).
Sequential completion does not result in any improvement in conditional optimiza-
tion, and it can actually have a negative impact on unconditional optimization. On
average, participants who sequentially optimize in the first period of PosIR end up 8
percentage points further away from the optimal unconditional solution compared to
those who did not use the calculator during the experiment.
The efficacy of the calculator is less pronounced in the FluctY environment. We
do not observe consistent improvements in optimization for the Partial, Sequential, and
Complete Calculator Types. In comparison to the NoCalc type, participants who only
fill in the current period are 6 percentage points further from the optimal unconditional
solution and 4 percentage points further from the optimal conditional solution.
Lastly, intheFluctPenvironment, thecalculatorbenefitsareconfinedtoparticipants
who complete it fully. The Complete Calculator Types are 7 percentage points closer
to both the optimal unconditional and conditional decisions compared to those who
did not use the calculator. Even if a subject fails to find the optimal solution using
the calculator, she still improves her conditional optimization by 5 p.p. by filling the
calculator in completely.
The specifications presented in columns (3), (6), (9), and (12) of Tables 5 and 6
include dummy variables Calc γU and Calc γC to control for whether a participant has
effectively used the calculator. The estimates demonstrate that effective usage of the
calculator significantly improves subjects’ performance by 10 to 20 percentage points
for the UncOptIndex and 6 and 9 percentage points for the CondOptIndex. These
results robustly support a refined version of Hypothesis 2: effective utilization of a
39

|     |     |          | Table 7: | Dependent | Variable: |      | OptCondIndex |           |     |           |
| --- | --- | -------- | -------- | --------- | --------- | ---- | ------------ | --------- | --- | --------- |
|     |     | Constant | YP       |           | Pos       | IR   |              | FluctY    |     | FluctP    |
|     |     | No Calc  | Calc     | No        | Calc      | Calc | No           | Calc Calc | No  | Calc Calc |
|     |     | (1)      | (2)      | (3)       |           | (4)  | (5)          | (6)       | (7) | (8)       |
0.720∗∗∗ 0.815∗∗∗ 0.583∗∗∗ 0.580∗∗∗ 0.774∗∗∗ 0.804∗∗∗ 0.585∗∗∗ 0.657∗∗∗
Constant
|     |     | (0.03) | (0.02) | (0.03) |     | (0.02) | (0.02) | (0.03) | (0.03) | (0.02) |
| --- | --- | ------ | ------ | ------ | --- | ------ | ------ | ------ | ------ | ------ |
Repetition 2 0.000 0.010 -0.003 -0.021∗ 0.032∗∗∗ 0.010 0.012 -0.005
|     |     | (0.01) | (0.01) | (0.01) |     | (0.01) | (0.01) | (0.01) | (0.02) | (0.01) |
| --- | --- | ------ | ------ | ------ | --- | ------ | ------ | ------ | ------ | ------ |
Repetition 3 0.056∗∗∗ 0.043∗∗∗ 0.028∗ 0.032∗∗∗ 0.062∗∗∗ 0.036∗∗∗ 0.035∗∗ 0.018
|     |     | (0.01) | (0.01) | (0.01) |     | (0.01) | (0.01) | (0.01) | (0.02) | (0.01) |
| --- | --- | ------ | ------ | ------ | --- | ------ | ------ | ------ | ------ | ------ |
Period 0.011∗∗∗ 0.008∗∗∗ 0.018∗∗∗ 0.028∗∗∗ 0.010∗∗∗ 0.006∗∗∗ 0.020∗∗∗ 0.015∗∗∗
|              |     | (0.00) | (0.00) | (0.00) |     | (0.00) | (0.00) | (0.00) | (0.00) | (0.00) |
| ------------ | --- | ------ | ------ | ------ | --- | ------ | ------ | ------ | ------ | ------ |
| Observations |     | 1320   | 1320   | 1290   |     | 1440   | 1380   | 1440   | 1440   | 1350   |
| Overall      | R2  | 0.03   | 0.02   | 0.04   |     | 0.12   | 0.03   | 0.01   | 0.04   | 0.03   |
Notes: This table presents the results of a random effects panel regression. Significance levels are denoted as
∗p<0.1,∗∗p<0.05,∗∗∗p<0.01
follows:
calculator significantly reduces deviations from both unconditional and conditional op-
timal consumption paths. Moreover, the results highlight the importance of carrying
out calculations efficiently. Simply entering information into the calculator or doing so
| incompletely | does       | not | guarantee | optimization |     | improvements. |     |         |     |     |
| ------------ | ---------- | --- | --------- | ------------ | --- | ------------- | --- | ------- | --- | --- |
| 5.2          | Experience |     | and       | length       | of  | planning      |     | horizon |     |     |
Our data provides strong support for Hypothesis 4, suggesting that conditional opti-
mization improves as participants plan over shorter time horizons. As detailed in Table
7, which disaggregates our results by treatment, we observe significant increases in γc
i,t
over time. In the absence of a calculator, participants in the ConstantYP and FluctY
treatments exhibit improvements of 1.1 percentage points per period. This increase is
even more pronounced in the PosIR and FluctP treatments, at 1.8 p.p. and 2.0 p.p. per
period, respectively. These improvements in conditional optimization range from 9 p.p.
| to 19 p.p. | when | comparing | the | first | and ninth | periods. |     |     |     |     |
| ---------- | ---- | --------- | --- | ----- | --------- | -------- | --- | --- | --- | --- |
Interestingly, the effects are less pronounced for subjects who have access to a calcu-
lator, except in the Pos IR treatment, where within-repetition improvement is notable.
40

In this case, there is an improvement of 25 p.p. from period 1 to period 9. This suggests
that the calculator does not significantly aid subjects in correcting mistakes and ap-
proaching conditional optimization when the planning horizon is shorter and cognitive
load is reduced. A notable exception to this trend is observed in the PosIR treatment,
a relevant finding since this type of experiment is commonly conducted. Here, the cal-
culator makes a difference both for within-repetition and between-repetition learning.
Result 4: Deviations from the conditional optimal consumption path diminish as the
planning horizon shortens. However, this effect is less pronounced when participants use
a calculator. The notable exception to this trend is observed in the Pos IR treatment.
5.3 Demographics
Mathematical training and financial literacy are key factors associated with financial
sophistication (Lusardi and Mitchell, 2011; Van Rooij et al., 2012). Under Hypothesis
5, we posited that individuals with mathematical proficiency would excel in sequential
calculations and logical reasoning, crucial for formulating optimal consumption plans.
Financial literacy complements this by offering a practical framework for applying such
calculations to real-world financial decisions, such as assessing future costs and benefits
and understanding the time value of money. These combined skills are presumed to
significantly aid individuals in solving intertemporal consumption problems, particularly
through the cognitive process of backward induction, which we explicitly elicited in our
study.
In Tables B.1 and B.2 in Appendix B, we examine each treatment individually to
identify whether the presence of the calculator interacts with demographic characteris-
tics. Our results provide little support for Hypothesis 5. Our findings indicate that in-
dividual characteristics do not consistently affect subjects’ ability to solve intertemporal
41

consumption problems. No significant effects were observed based on other demographic
variables such as gender or age. Higher financial literacy leads to a large and significant
improvement in optimization in ConstantYP-NoCalc (8-9 p.p. improvement per correct
answer), but not in any other treatment. Stronger backward-induction skills are associ-
ated with better unconditional optimization in ConstantYP-Calc, but no improvements
elsewhere.
Finally, mathematical training has quite a large effect on FluctP-Calc respondents’
unconditional and conditional optimization. Unconditional optimization is 3.5 p.p.
higher for each additional level of mathematical training. We observe a 3.5 × 8 =
28 p.p. difference between those studying in the most mathematically-intensive degrees
and those with the least mathematically-intensive degrees (there are 9 categories, so a
difference of 8 math levels). In terms of conditional optimization, we observe a 2.8 × 8
= 22.4 p.p. difference. Again, this trait does not lead to significantly higher levels of
optimization in other treatments.
We are also left intrigued by the finding that mathematical training does not sig-
nificantly influence optimization in the PosIR treatment. This is at odds with previous
literature that underscores the correlation between mathematical skill and the ability to
compute compounding returns.An explanation for the inconsistent demographic effects
could be the leveling effect of our extensive training phase before the experiment, which
included a thorough 30-minute instruction session. This training may have equalized
the playing field among subjects with varied backgrounds.
Result 5: Individual and demographic characteristics do not have a consistent effect
across economic environments on optimization ability.
6 A Model of Short-Span Planning
A primary reason for sub-optimal consumption plans is short planning horizons. This
phenomenon can be rigorously analyzed by refining our existing economic model. In this
42

| revised model, | individuals | aim to maximize |                     |     |     |
| -------------- | ----------- | --------------- | ------------------- | --- | --- |
|                |             |                 | H (cid:18) (cid:19) |     |     |
(cid:88) 1
c1−σ
|     |     | max | k   |     | (10) |
| --- | --- | --- | --- | --- | ---- |
|     |     |     | 1−σ | t   |      |
ct
t=1
| subject | to: |        |             |     |      |
| ------- | --- | ------ | ----------- | --- | ---- |
|         |     | p c +s | = y +(1+r)s | ,   | (11) |
|         |     | t t    | t t         | t−1 |      |
where H is the horizon, it ranges from 1 to 10. In this context, if H = 10, then
the individual has full foresight (which brings us back to the standard model), and
if H = 1, the model predicts behavior that aligns with the Hand-to-Mouth heuristic,
where individuals consume their income immediately without saving for the future. The
implications of different planning horizons are presented in Table C.1 in the Appendix,
which outlines the predicted consumption level in Period 1 by treatment and planning
horizon.
Our focus here is on PosIR because, in the rest of the treatments, the planning
horizon does not significantly affect the optimal level of consumption. In ConstantYP,
the optimal consumption level is unaffected by the planning horizon, while in FluctY
and FluctP, the primary difference arises between individuals who plan exclusively for
the current period and those who consider future periods. Additionally, if H is an even
number, the optimal consumption in Period 1 aligns with the solution for a full-span
planner.
In PosIR, the model suggests that individuals maximize the benefits of interest rates
by extending the planning horizon. Notably, as the planning horizon is longer, consump-
tion in Period 1 diminishes, underscoring the significance of early savings. We leverage
our model’s predictive power to ascertain a specific planning horizon for each subject
based on their observed consumption decisions in the initial period of each repetition.
This builds upon the notion that an individual’s consumption choice is influenced by
their planning horizon and includes a random error component. The error component,
ε, follows a normal distribution with mean zero and standard deviation σ. Then, by per-
43

forming a maximum likelihood estimation, we can calculate the distribution of horizons
in the sample and the standard deviation.19
The estimated parameters are shown in Table C.2 in the appendix. In this table,
we note that close to 30% of the observations are not explained by short-span planning
model. Among the observations that can be rationalized by the model, approximately
20% of them would correspond to 1-period planners, around 19% would correspond to
individuals that plan for 2 or 3 periods in advance, over 10% would consider 8 periods,
and close to 10% would use the full horizon.
Additionally, we can cross-validate these model predictions with the actual planning
behaviors observed among the subjects in our experiment. This is possible because we
have collected detailed planning data for each subject in every period, derived from
the usage of the budgeting calculator. To directly compare this data, we examine each
subject’s planning horizon in the first period of each repetition by observing how many
entries subjects filled out in the calculator during each of the trials. Note that they can
fill out as few as one entry and as many as 10 periods (the full horizon).20 Consequently,
in Figure 10, we compare the distribution of planning horizons utilized by subjects
against the model’s predictions detailed in Table C.2.21
19The details can be found in Appendix C.
20In our analysis, we make two adjustments when examining the data. The first is that we omit
intermediate plans for sequential users: if a subject incrementally increases the planning horizon by
clicking the Submit button each time they enter an additional consumption value, we only retain the
final (longest) plan. The second adjustment recognizes that in a single period, subjects may use the
calculatortotestvariouspotentialplans,complicatingtheanalysisasitisunclearwhichplantheyintend
to implement. These plans may even differ in their time horizons. To ensure a balanced evaluation,
we assign equal weight to each participant using the budgeting calculator in each repetition. This
means that every individual’s plan contributes equally to the overall distribution. However, the weight
of a specific plan is inversely proportional to the frequency of calculator usage by that subject. This
approach mitigates the potential overrepresentation of subjects who are simply exploring the payoff
space, preventing their exploratory attempts from disproportionately affecting the distribution.
21Note that the first bar represents subjects who did not utilize the calculator for observed planning
behavior and in terms of the Partial-Horizon model were not categorized. As a robustness check, we
implemented an alternative method by taking consumption values from period 1 in each repetition and
comparing them with ten possible consumption values based on the predictions of our model, each
corresponding to a different planning horizon. For each horizon, we calculated the squared deviations
betweentheobservedconsumptionfiguresandthemodel’spredictedvalues. Thehorizonwiththesmall-
est squared deviation was identified as the closest to the subject’s observed consumption behavior. If
thesedeviationsfellbelowacertainthreshold,theconsumptionpatternwasclassifiedasuncategorized.
This approach’s outcomes did not significantly differ from our main analysis findings.
44

0.60
0.50
0.40
0.30
0.20
0.10
0.00
No Category/
No Calculator
noitubirtsiD
detciderP
/ gninnalp
devresbo
fo
noitubirtsiD
1 2 3 4 5 6 7 8 9 10
Horizon
Partial Horizon Prediction Observed Planning from Calculator
Figure 10: Comparison between the pre-
dicted and the observed horizon
Figure 10 demonstrates that the model accurately forecasts the frequency with which
a one-period planning horizon is employed. However, it underestimates the use of the
full planning horizon; the model predicts its occurrence at around 10%, whereas, in
reality, subjects choose this option nearly half of the time. Furthermore, the model’s
prediction of a 12% utilization rate for an 8-period planning horizon starkly contrasts
with the actual trials, where this horizon is selected in less than 1% of instances. This
notable discrepancy prompts a conjectural explanation: subjects who are aware of the
benefits of compounding interest rates, but uncertain about the optimal savings amount,
might resort to a straightforward heuristic. Such a heuristic might involve saving half of
their income, yielding a consumption level of 5 units, closely aligning with the model’s
prediction of 5.13 units for an 8-period planner, as detailed in Table C.1.
7 Discussion
Our study represents one of the first attempts to understand the role of environmental
complexity in dynamic optimization, focusing on consumption smoothing. We uncover
that different environments pose varying levels of challenges, some more demanding
than others. Particularly, while the complexities associated with compounding interest
rates on savings or fluctuating income are well-acknowledged, the challenges related
45

to fluctuating prices have been less examined. Our research not only fills this gap
but also presents new empirical evidence demonstrating that many individuals struggle
with planning over extended periods, a fundamental yet often overlooked assumption of
economic theory.
In exploring these complexities, our experiments reveal that individuals frequently
encounter significant hurdles in achieving optimal outcomes, even in seemingly straight-
forward scenarios. These challenges arise not only from the variability of economic
conditions but also from cognitive limitations and numerical difficulties inherent in dy-
namic decision-making. Our findings resonate with existing literature on complexity,
such as the works of Oprea (2022), Enke and Graeber (2019), and Gabaix and Grae-
ber (2023), which conceptualize the mind as a cognitive economy faced with numerous
decisions.
Another key aspect of our study is the potential role of a meticulously designed bud-
geting calculator in aiding decision-making. Our results indicate that the mere availabil-
ity of such a tool does not guarantee its effective use. The effectiveness of a budgeting
tool largely depends on how individuals choose to utilize it. This observation is cru-
cial, as it highlights that providing tools for financial planning is beneficial, but their
impact hinges on the user’s engagement and understanding. Furthermore, our analysis
of non-choice data from the budget calculator provides deeper insights into individuals’
strategies, preferences, and decision-making horizons. The integration of robo-advisory
features into this budgeting calculator could enhance its utility. Robo-advisors, by pro-
viding automated, data-driven guidance and personalized financial recommendations,
can serve as an active form of nudging, potentially increasing the effectiveness of such
tools. Such integration could transform the calculator from a passive instrument into
a more interactive agent in financial planning, nudging users towards optimal financial
behaviors tailored to their unique data and preferences.
Crucially, our paper makes a significant contribution by directly examining indi-
viduals’ capacity for planning, a core assumption in economic theory often taken for
granted. Standard economic models assume that agents can plan effectively, even for
46

long horizons, which is essential for making optimal present choices. However, empir-
ical evidence supporting this assumption, particularly from laboratory experiments, is
scarce.22 Our work stands as one of the first to provide concrete evidence of individuals’
planning abilities—or the lack thereof—by directly observing their plans. This approach
differs markedly from indirect methods using decision trees (see Hey 2002), which infer
planning from decision outcomes. Expanding upon this concept, we can even compare
observed planning-horizons to implied horizons from a short-span horizon model. This
analysis leads us to rule out the short-span model in positive interest rate environments,
pointing towards a broader issue in achieving optimal paths than just the incapacity for
long-term planning.
It is important to emphasize that real-world settings present even greater challenges
for dynamic optimization. The unpredictability of real life, combined with unexpected
events and incomplete information, complicates decision-making. Individuals often pur-
sue multiple goals and are influenced by behavioral biases like overconfidence, loss aver-
sion, and procrastination. Therefore, the deviations from the optimal path observed in
our controlled experiments should be viewed as a lower bound. In more complex real-
world scenarios, these deviations are expected to increase, highlighting the necessity
for strong financial planning tools and improved financial literacy to help individuals
navigate these challenges effectively.
Looking forward, our study opens several avenues for future research. Investigating
dynamic optimization under diverse conditions such as uncertainty, social learning influ-
ences, expected liquidity constraints, and current binding constraints could enhance our
understanding of decision-making complexities. Further studies on the effects of intro-
ducing and removing budget calculators and the sustained impact of financial literacy
initiatives will provide deeper insights into how these tools and educational interventions
affect consumer behavior.
In terms of policy implications, our findings on suboptimal decision-making due to
22One exception is planning in the context of present bias and procrastination (see Della Vigna and
Malmendier 2006).
47

cognitive complexity, especially under fluctuating prices, suggest an added layer of wel-
fare loss beyond traditional concerns like menu costs and relative price dispersion in
inflationary contexts. These insights highlight the potential for cognitive errors to exac-
erbatewelfarelossesinrealisticsettings, thusunderscoringtheimportanceofsimplifying
financial decision environments and improving financial literacy.
48

References
| Ballinger, | T., M. | Palumbo, |     | and N. | Wilcox |         |                |     |             |
| ---------- | ------ | -------- | --- | ------ | ------ | ------- | -------------- | --- | ----------- |
|            |        |          |     |        |        | (2003): | “Precautionary |     | Savings and |
Social Learning Across Generations: An Experiment,” The Economic Journal, 113,
920–947.
| Ballinger, | T. P., | E. Hudson, |     | L. Karkoviata, |     | and | N. T. | Wilcox |               |
| ---------- | ------ | ---------- | --- | -------------- | --- | --- | ----- | ------ | ------------- |
|            |        |            |     |                |     |     |       |        | (2011): “Sav- |
ing Behavior and Cognitive Abilities,” Experimental Economics, 14, 349–374.
Bosch-Dome`nech
| Bosch-Rosa, | C.,          | T. Meissner, |            | and     | A.       |           |     | (2018):  | “Cognitive |
| ----------- | ------------ | ------------ | ---------- | ------- | -------- | --------- | --- | -------- | ---------- |
| bubbles,”   | Experimental |              | Economics, | 21,     | 132–153. |           |     |          |            |
| Brown,      | A., E. Chua, | and          | C.         | Camerer |          |           |     |          |            |
|             |              |              |            |         | (2009):  | “Learning | and | Visceral | Temptation |
in Dynamic Saving Experiments,” Quarterly Journal of Economics, 124, 197–231.
Caliendo, F. and D. Aadland (2007): “Short-term planning and the life-cycle
consumption puzzle,” Journal of Economic Dynamics and Control, 31, 1392–1415.
| Caplin,  | A., M. Dean, | and  | D.         | Martin |         |         |     |               |          |
| -------- | ------------ | ---- | ---------- | ------ | ------- | ------- | --- | ------------- | -------- |
|          |              |      |            |        | (2011): | “Search | and | satisficing,” | American |
| Economic | Review,      | 101, | 2899–2922. |        |         |         |     |               |          |
Carbone, E. and J. Duffy (2014): “Lifecycle Consumption Plans, Social Learn-
ing and External Habits: Experimental Evidence,” Journal of Economic Behavior &
| Organization, | 106,   | 413–427.   |     |     |            |         |     |             |           |
| ------------- | ------ | ---------- | --- | --- | ---------- | ------- | --- | ----------- | --------- |
| Carbone,      | E., K. | Georgalos, |     | and | G. Infante |         |     |             |           |
|               |        |            |     |     |            | (2019): |     | “Individual | vs. Group |
Decision-Making: An Experiment on Dynamic Choice under Risk and Ambiguity,”
| Theory   | and decision, | 87,    | 87–122. |      |        |                 |     |     |              |
| -------- | ------------- | ------ | ------- | ---- | ------ | --------------- | --- | --- | ------------ |
| Carbone, | E. and        | J. Hey |         |      |        |                 |     |     |              |
|          |               |        | (2004): | “The | Effect | of Unemployment |     | on  | Consumption: |
An Experimental Analysis,” The Economic Journal, 114, 660–683.
Carbone, E. and G. Infante(2015): “AreGroupsBetterPlannersthanIndividuals?
An Experimental Analysis,” Journal of Behavioral and Experimental Economics, 57,
112–119.
49

D’Acunto, F. and A. G. Rossi (2023): “Robo-advice: Transforming households into
rational economic agents,” Annual Review of Financial Economics, 15, 543–563.
D’Acunto, F., A. G. Rossi, and M. Weber (2023): “Crowdsourcing peer informa-
tion to change spending behavior,” Chicago Booth Research Paper.
| Della Vigna, |          | S.  | and     | U. Malmendier |              |     |         |         |     |     |           |       |
| ------------ | -------- | --- | ------- | ------------- | ------------ | --- | ------- | ------- | --- | --- | --------- | ----- |
|              |          |     |         |               |              |     | (2006): | “Paying | not | to  | go to the | gym,” |
| american     | economic |     | Review, |               | 96, 694–719. |     |         |         |     |     |           |       |
Duffy, J. (2016): “Macroeconomics: A Survey of Laboratory Research,” Handbook of
| Experimental |        | Economics, |         | Volume | 2.         |             |     |       |           |     |                  |     |
| ------------ | ------ | ---------- | ------- | ------ | ---------- | ----------- | --- | ----- | --------- | --- | ---------------- | --- |
| Duffy,       | J. and | Y.         | Li      |        |            |             |     |       |           |     |                  |     |
|              |        |            | (2019): |        | “Lifecycle | consumption |     | under | different |     | income profiles: |     |
Evidence and theory,” Journal of Economic Dynamics and Control, 104, 74–94.
| Duffy, | J. and | A.       | Orland |              |         |            |         |              |        |        |           |     |
| ------ | ------ | -------- | ------ | ------------ | ------- | ---------- | ------- | ------------ | ------ | ------ | --------- | --- |
|        |        |          |        |              | (2023): | “Liquidity |         | Constraints, |        | Income | Variance, | and |
| Buffer | Stock  | Savings: |        | Experimental |         | Evidence,” | Working |              | Paper. |        |           |     |
D’Acunto, F., N. Prabhala, and A. G. Rossi (2019): “The promises and pitfalls
of robo-advising,” The Review of Financial Studies, 32, 1983–2020.
| D’Acunto, |     | F. and | M.  | Weber |         |     |         |     |          |          |      |     |
| --------- | --- | ------ | --- | ----- | ------- | --- | ------- | --- | -------- | -------- | ---- | --- |
|           |     |        |     |       | (2022): |     | “Memory | and | beliefs: | Evidence | from | the |
field,” Georgetown University and University of Chicago Working Paper.
Eckel, C. C. and P. J. Grossman (2002): “Sex Differences and Statistical Stereo-
typing in Attitudes Toward Financial Risk,” Evolution and Human Behavior, 23,
281–295.
| Enke, B. | and         | T.  | Graeber   |     |         |            |     |               |     |       |                |     |
| -------- | ----------- | --- | --------- | --- | ------- | ---------- | --- | ------------- | --- | ----- | -------------- | --- |
|          |             |     |           |     | (2019): | “Cognitive |     | uncertainty,” |     | Tech. | rep., National |     |
| Bureau   | of Economic |     | Research. |     |         |            |     |               |     |       |                |     |
Enke, B., T. Graeber, and R. Oprea (2023): “Complexity and Time,” Tech. rep.,
| National      | Bureau |            | of Economic |           | Research. |        |         |           |     |            |           |     |
| ------------- | ------ | ---------- | ----------- | --------- | --------- | ------ | ------- | --------- | --- | ---------- | --------- | --- |
| Fenig,        | G., G. | Gallipoli, |             | and       | Y.        | Halevy |         |           |     |            |           |     |
|               |        |            |             |           |           |        | (2022): | “Piercing |     | the’Payoff | Function’ |     |
| Veil: Tracing |        | Beliefs    | and         | Motives,” | Working   |        | Paper.  |           |     |            |           |     |
50

Fischbacher, U. (2007): “z-Tree: Zurich Toolbox for Ready-Made Economic Experi-
| ments,” | Experimental |     | Economics, |     | 10, 171–78. |     |     |     |
| ------- | ------------ | --- | ---------- | --- | ----------- | --- | --- | --- |
| Gabaix, | X.           |     |            |     |             |     |     |     |
(2014): “A sparsity-based model of bounded rationality,” The Quarterly
| Journal | of Economics, |     | 129, | 1661–1710. |     |     |     |     |
| ------- | ------------- | --- | ---- | ---------- | --- | --- | --- | --- |
Gabaix, X. and T. Graeber (2023): “The Complexity of Economic Decisions,”
| Available | at SSRN. |     |     |     |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Hey, J. and V. Dardanoni (1988): “Optimal Consumption Under Uncertainty: An
Experimental Investigation,” The Economic Journal, 98, 105–116.
| Hey, J. D. |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
(2002): “Experimental economics and the theory of decision making under
risk and uncertainty,” The Geneva Papers on Risk and Insurance Theory, 27, 5–21.
Ilut, C. and R. Valchev (2023): “Economic agents as imperfect problem solvers,”
| The Quarterly |     | Journal | of Economics, |     | 138, 313–362. |     |     |     |
| ------------- | --- | ------- | ------------- | --- | ------------- | --- | --- | --- |
Krosnick, J. A. (1991): “Response strategies for coping with the cognitive demands
of attitude measures in surveys,” Applied cognitive psychology, 5, 213–236.
| Laibson, | D.  |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- |
(1997): “Golden eggs and hyperbolic discounting,” The Quarterly Journal
| of Economics, |     | 112, | 443–478. |     |     |     |     |     |
| ------------- | --- | ---- | -------- | --- | --- | --- | --- | --- |
Li, Y. (2024): “Do Tax Deferred Accounts Improve Lifecycle Savings? Experimental
| Evidence,” | Review |     | of Economics |     | and Statistics, | forthcoming. |     |     |
| ---------- | ------ | --- | ------------ | --- | --------------- | ------------ | --- | --- |
List, J. A., A. M. Shaikh, and Y. Xu (2019): “Multiple hypothesis testing in
| experimental |     | economics,” | Experimental |     | Economics,         |     | 22, 773–793.     |              |
| ------------ | --- | ----------- | ------------ | --- | ------------------ | --- | ---------------- | ------------ |
| Loewenstein, |     | G. and      | D. Prelec    |     |                    |     |                  |              |
|              |     |             |              |     | (1992): “Anomalies |     | in intertemporal | choice: Evi- |
dence and an interpretation,” The Quarterly Journal of Economics, 107, 573–597.
Lu, K. (2022): “Overreaction to capital taxation in saving decisions,” Journal of Eco-
| nomic Dynamics |     | and | Control, | 144, | 104541. |     |     |     |
| -------------- | --- | --- | -------- | ---- | ------- | --- | --- | --- |
51

Luhan, W. J., M. W. Roos, and J. Scharler (2014): “An Experiment on Con-
sumption Responses to Future Prices and Interest Rates,” in Experiments in macroe-
| conomics, | Emerald |     | Group | Publishing |     | Limited, 139–166. |     |     |     |
| --------- | ------- | --- | ----- | ---------- | --- | ----------------- | --- | --- | --- |
Lusardi, A. and O. Mitchell (2007): “Financial Literacy and Retirement Planning:
New Evidence from the Rand American Life Panel,” NBER Working Paper.
| Lusardi, | A.             | and | O. S.       | Mitchell |         |            |              |           |        |
| -------- | -------------- | --- | ----------- | -------- | ------- | ---------- | ------------ | --------- | ------ |
|          |                |     |             |          | (2011): | “Financial | literacy and | planning: | Impli- |
| cations  | for retirement |     | wellbeing,” |          | .       |            |              |           |        |
Lusardi, A. and D. Wallace (2013): “Financial literacy and quantitative reasoning
| in the | high school |     | and | college | classroom,” | Numeracy, | 6, 1. |     |     |
| ------ | ----------- | --- | --- | ------- | ----------- | --------- | ----- | --- | --- |
Mac´kowiak,
B. and M. Wiederholt (2015): “Business cycle dynamics under ra-
tional inattention,” The Review of Economic Studies, 82, 1502–1532.
| Meissner, | T.  |     |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(2016): “Intertemporal Consumption and Debt Aversion: An Experi-
| mental | Study,” | Experimental |     | Economics, |     | 19, 281–298. |     |     |     |
| ------ | ------- | ------------ | --- | ---------- | --- | ------------ | --- | --- | --- |
Miller, L. and R. Rholes (2023): “Joint vs. Individual performance in a dynamic
choice problem,” Journal of Economic Behavior & Organization, 212, 897–934.
Modigliani, F. and R. Brumberg (1954): “Utility Analysis and the Consumption
Function: An Interpretation of Cross Section Data,” in Post Keynesian Economics,
ed. by K.K.Kurihara, Ruthers University Press New Brunswick New Jersey, vol. 1,
388–436.
O’Donoghue, T. and M. Rabin(1999): “Doingitnoworlater,” American Economic
| Review, | 89,        | 103–124. |             |               |     |         |        |     |     |
| ------- | ---------- | -------- | ----------- | ------------- | --- | ------- | ------ | --- | --- |
| Oprea,  | R. (2022): |          | “Simplicity | equivalents,” |     | Working | Paper. |     |     |
Schipper, B. C. (2014): “Unawareness—a gentle introduction to both the literature
| and the | special | issue,” |     | Mathematical | Social | Sciences, | 70, 1–9. |     |     |
| ------- | ------- | ------- | --- | ------------ | ------ | --------- | -------- | --- | --- |
52

Simon, H. A. (1956): “Rational choice and the structure of the environment.” Psycho-
| logical review, | 63. |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
| Sims, C.        | A.  |     |     |     |     |
(2003): “Implications of rational inattention,” Journal of monetary Eco-
| nomics, | 50, 665–690. |     |     |     |     |
| ------- | ------------ | --- | --- | --- | --- |
Van Rooij, M. C., A. Lusardi, and R. J. Alessie (2012): “Financial literacy,
retirement planning and household wealth,” The Economic Journal, 122, 449–478.
Woodford, M. (2019): “Monetary policy analysis when planning horizons are finite,”
| NBER      | macroeconomics | annual, | 33, 1–50.     |                |           |
| --------- | -------------- | ------- | ------------- | -------------- | --------- |
| Yamamori, | T., K. Iwata,  | and     | A. Ogawa      |                |           |
|           |                |         | (2018): “Does | money illusion | matter in |
intertemporal decision making?” Journal of Economic Behavior & Organization, 145,
465 –473.
53

| A Taylor |     | Expansion |     |     | for | Optimal |     | Choice |     |
| -------- | --- | --------- | --- | --- | --- | ------- | --- | ------ | --- |
Inthissection, weapplyaTaylorexpansiontotheoptimalconsumptionchoiceforperiod
1, as specified in Equation 6. This analysis adheres to the methodology delineated
by Gabaix and Graeber (2023) in their study of complexity. Let yˆ = y − y and
t t 1
pˆ = p − p , and assume that yˆ and pˆ are negligibly small. Consequently, we can
| t t         | 1        |     |     |           | t   | t   |           |     |     |
| ----------- | -------- | --- | --- | --------- | --- | --- | --------- | --- | --- |
| reformulate | Equation |     | 6.  |           |     |     |           |     |     |
|             |          |     |     | (cid:80)T |     | y1  | (cid:80)T | yˆt |     |
+
|     |     |     |     |          | t=1 (1+r)t−1 |           | t=2      | (1+r)t−1                     |      |
| --- | --- | --- | --- | -------- | ------------ | --------- | -------- | ---------------------------- | ---- |
|     |     |     | c = |          |              |           |          |                              | (12) |
|     |     |     | 1   | (cid:18) | (cid:18)     |           |          | (cid:17)σ− 1(cid:19)(cid:19) |      |
|     |     |     |     |          | 1            | (cid:80)T | (cid:16) |                              |      |
|     |     |     |     | p        | +pσ          |           | pˆt+p1   | σ                            |      |
1
|          |     |            |     |      | 1        | t=2     | (1+r)t−1    |        |      |
| -------- | --- | ---------- | --- | ---- | -------- | ------- | ----------- | ------ | ---- |
| We begin | by  | evaluating | c   | when | yˆ =     | 0, r =  | 0 and       | pˆ = 0 |      |
|          |     |            |     | 1    | t        |         |             | t      |      |
|          |     |            |     |      |          | Ty      |             | y      |      |
|          |     |            |     |      |          | 1       |             | 1      |      |
|          |     |            | c   | =    |          |         |             | =      | (13) |
|          |     |            | 1   |      | (cid:16) |         | σ−1(cid:17) |        |      |
|          |     |            |     |      | 1        |         |             | p      |      |
|          |     |            |     | p    | +pσ      | (T −1)p |             | σ 1    |      |
|          |     |            |     |      | 1 1      |         | 1           |        |      |
Then we calculate ∂c1 and evaluate it when yˆ = 0, r = 0 and pˆ = 0
t t
∂yˆt
|     |     |     |     |     | (cid:80)T | (cid:104) |     | (cid:105) |     |
| --- | --- | --- | --- | --- | --------- | --------- | --- | --------- | --- |
1
∂c
|     |     |     | 1   |     |     | t=1 | (1+r)t−1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
=
|     |     |     | ∂yˆ | (cid:18) | (cid:18) |           | (cid:16) | (cid:17)σ− 1(cid:19)(cid:19) |     |
| --- | --- | --- | --- | -------- | -------- | --------- | -------- | ---------------------------- | --- |
|     |     |     | t   |          | 1        | (cid:80)T |          |                              |     |
|     |     |     |     | p        | +pσ      |           | pˆt+p1   | σ                            |     |
|     |     |     |     |          | 1 1      | t=2       | (1+r)t−1 |                              |     |
1
=
|     |     |     |     |       | (cid:16) |      |     | (cid:17) |     |
| --- | --- | --- | --- | ----- | -------- | ---- | --- | -------- | --- |
|     |     |     |     |       | 1        | σ−1  |     |          |     |
|     |     |     |     | p +pσ | p        | σ (T | −1) |          |     |
|     |     |     |     | 1     | 1        | 1    |     |          |     |
1
=
Tp
1
We then calculate ∂c1 and evaluate it when yˆ = 0, r = 0 and pˆ = 0
t t
∂r
54

|     |     |     |     | (cid:16) |              | (cid:17) | (cid:16)    |                      | (cid:17) |     |     |     |
| --- | --- | --- | --- | -------- | ------------ | -------- | ----------- | -------------------- | -------- | --- | --- | --- |
|     |     |     |     |          | (cid:80)T−1t |          | (cid:0) 1−σ | (cid:1) (cid:80)T−1t |          |     |     |     |
|     |     | ∂c  |     | y        |              | Tp +     |             | p                    |          | Ty  |     |     |
|     |     |     | 1   |          | 1 t=1        | 1        |             | σ 1                  | t=1      | 1   |     |     |
|     |     |     | =   | −        |              |          |             |                      |          |     | =   |     |
|     |     |     | ∂r  |          |              |          | T2p2        |                      |          |     |     |     |
1
(cid:80)T−1t
y
1
|     |     |     | =   | −   | t=1 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | Tp  | σ   |     |     |     |     |     |     |     |
1
−y1(T−1)(T)
|     |     |     | =   |     | 2   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | Tp  | σ   |     |     |     |     |     |     |     |
1
|     |     |     |     | y (T | −1) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | =−  | 1    |     |     |     |     |     |     |     |     |
2σp
1
Finally we calculate ∂c1 and evaluate it when yˆ = 0, r = 0 and pˆ = 0
|     |     |     |     |     |     |     | t   |     |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∂pˆt
|     |     |     |     |           |          |        |          | (cid:18)  |                |           | 1(cid:19) |     |
| --- | --- | --- | --- | --------- | -------- | ------ | -------- | --------- | -------------- | --------- | --------- | --- |
|     |     |     |     | (cid:16)  |          |        | (cid:17) |           | (cid:16)       | (cid:17)− |           |     |
|     |     |     |     | (cid:80)T |          |        |          | 1 (cid:0) | (cid:1) pˆt+p1 |           | σ         |     |
|     |     |     |     |           | 1        | (yˆ +y | )        | pσ σ−1    |                |           |           |     |
|     |     | ∂c  |     | t=1       | (1+r)t−1 | t      | 1        | 1         | σ (1+r)        |           |           |     |
1
= −
|     |     |     |     |     | (cid:18) | (cid:18)    |          |        | 1(cid:19)(cid:19)2 |     |     |     |
| --- | --- | --- | --- | --- | -------- | ----------- | -------- | ------ | ------------------ | --- | --- | --- |
|     |     | ∂pˆ |     |     |          |             | (cid:16) |        | (cid:17)σ−         |     |     |     |
|     |     |     | t   |     |          | 1 (cid:80)T |          | pˆt+p1 | σ                  |     |     |     |
p +pσ
|     |     |     |     |         | 1       | 1   | t=2 | (1+r)t−1 |     |     |     |     |
| --- | --- | --- | --- | ------- | ------- | --- | --- | -------- | --- | --- | --- | --- |
|     |     |     |     | (cid:0) | (cid:1) |     |     |          |     |     |     |     |
|     |     |     |     | Ty      | σ−1     |     |     |          |     |     |     |     |
|     |     |     |     | 1       | σ       |     |     |          |     |     |     |     |
= −
T2p2
1
|     |     |     | (cid:18) | 1−σ | (cid:19) y |     |     |     |     |     |     |     |
| --- | --- | --- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
1
=
|     |     |     |     | σ   | Tp2 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
| Thus, the | Taylor |     | expansion | is  |          |       |     |          |          |            |     |      |
| --------- | ------ | --- | --------- | --- | -------- | ----- | --- | -------- | -------- | ---------- | --- | ---- |
|           |        |     |           |     | T        |       |     | (cid:18) | (cid:19) |            | T   |      |
|           |        |     | y         | 1   | (cid:88) | y (T  | −1) | 1−σ      |          | y (cid:88) |     |      |
|           |        |     | 1         |     |          | 1     |     |          |          | 1          |     |      |
|           |        | c   | = +       |     | yˆ       | −     | r+  |          |          |            | pˆ  | (14) |
|           |        | 1   | p         | Tp  |          | t 2σp |     |          | σ Tp2    |            | t   |      |
|           |        |     | 1         |     | 1        |       | 1   |          |          |            |     |      |
|           |        |     |           |     | t=2      |       |     |          |          | 1 t=2      |     |      |
55

| B Additional | Regressions |                |           |             |        |     |        |     |
| ------------ | ----------- | -------------- | --------- | ----------- | ------ | --- | ------ | --- |
|              | Table       | B.1: Dependent | Variable: | OptUncIndex |        |     |        |     |
|              | ConstantYP  |                | PosIR     |             | FluctY |     | FluctP |     |
NoCalc Calc Calc NoCalc Calc Calc NoCalc Calc Calc NoCalc Calc Calc
|                  | (1) (2) | (3) (4)  | (5) | (6)      | (7) (8) | (9) (10) | (11) | (12)     |
| ---------------- | ------- | -------- | --- | -------- | ------- | -------- | ---- | -------- |
| NoofCalculations |         | -0.001   |     | -0.001   |         | -0.001   |      | 0.001    |
|                  |         | (0.00)   |     | (0.00)   |         | (0.00)   |      | (0.00)   |
| CalcγU           |         | 0.093∗∗∗ |     | 0.213∗∗∗ |         | 0.115∗∗∗ |      | 0.105∗∗∗ |
|                  |         | (0.02)   |     | (0.02)   |         | (0.02)   |      | (0.02)   |
MinutesSpent -0.037∗∗∗ -0.012∗∗∗ -0.010∗ -0.008 -0.009∗∗∗ -0.005 -0.011 -0.014∗∗∗ -0.007 0.011 -0.000 -0.002
(0.01) (0.00) (0.00) (0.01) (0.00) (0.00) (0.01) (0.00) (0.01) (0.01) (0.00) (0.00)
Repetition2 -0.010 0.036∗∗∗ 0.038∗∗∗ 0.010 -0.019 -0.019 0.042∗∗∗ 0.007 0.023∗ 0.031∗ 0.005 -0.001
(0.02) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.02) (0.02) (0.02)
Repetition3 0.047∗∗∗ 0.065∗∗∗ 0.069∗∗∗ 0.038∗∗∗ 0.037∗∗ 0.025∗ 0.059∗∗∗ 0.035∗∗∗ 0.047∗∗∗ 0.063∗∗∗ 0.029 0.018
(0.02) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.02) (0.02) (0.02)
Period -0.010∗∗∗ 0.001 0.001 -0.006∗∗∗ 0.000 -0.000 -0.003∗ -0.009∗∗∗ -0.009∗∗∗ 0.006∗∗ 0.002 0.002
(0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00)
MathLevel 0.040 0.009 0.007 0.007 -0.015 -0.016∗ -0.005 0.004 0.005 0.015 0.041∗∗∗ 0.035∗∗
(0.02) (0.01) (0.01) (0.02) (0.01) (0.01) (0.02) (0.01) (0.01) (0.01) (0.01) (0.01)
BackwardInduction -0.001 0.042∗∗ 0.036∗ -0.015 0.015 0.005 0.024 -0.004 -0.007 -0.002 0.027 0.028
(0.02) (0.02) (0.02) (0.03) (0.01) (0.01) (0.02) (0.03) (0.02) (0.03) (0.02) (0.02)
FinancialLiteracy 0.092∗∗ -0.018 -0.017 0.022 -0.013 -0.020 0.034 -0.012 -0.013 0.021 -0.012 -0.011
(0.04) (0.02) (0.02) (0.03) (0.03) (0.02) (0.03) (0.04) (0.04) (0.03) (0.02) (0.02)
ControlQuestions -0.003 0.005 0.003 0.013 0.021∗∗ 0.020∗∗∗ 0.007 0.012 0.014 0.006 0.002 -0.001
(0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.02) (0.01) (0.01)
CalculatorUsage
CurrentPeriod 0.074∗∗∗ 0.075∗∗∗ -0.028 -0.006 -0.068∗∗ -0.049∗ -0.002 0.013
|         | (0.02)   | (0.02)   | (0.03) | (0.03)  | (0.03) | (0.03) | (0.03) | (0.03) |
| ------- | -------- | -------- | ------ | ------- | ------ | ------ | ------ | ------ |
|         | 0.122∗∗∗ | 0.102∗∗∗ |        | 0.052∗∗ |        |        |        |        |
| Partial |          |          | 0.035  |         | 0.016  | 0.038  | -0.007 | -0.003 |
|         | (0.02)   | (0.03)   | (0.03) | (0.03)  | (0.03) | (0.03) | (0.03) | (0.03) |
Sequential 0.051∗∗ -0.000 -0.089∗∗∗ -0.176∗∗∗ -0.005 -0.056∗∗ -0.022 -0.063∗
|          | (0.02)   | (0.03) | (0.03)   | (0.03)    | (0.02)   | (0.02)    | (0.03) | (0.03) |
| -------- | -------- | ------ | -------- | --------- | -------- | --------- | ------ | ------ |
|          | 0.088∗∗∗ |        | 0.081∗∗∗ | -0.086∗∗∗ | -0.048∗∗ | -0.099∗∗∗ | 0.053∗ |        |
| Complete |          | 0.029  |          |           |          |           |        | 0.013  |
|          | (0.02)   | (0.02) | (0.02)   | (0.03)    | (0.02)   | (0.03)    | (0.03) | (0.03) |
Constant 0.677 0.601 0.662∗ -0.122 -0.360 -0.203 0.267 0.432 0.266 0.311 0.358 0.526
(0.48) (0.44) (0.40) (0.73) (0.39) (0.24) (0.51) (0.53) (0.52) (1.10) (0.68) (0.67)
Observations 1320 1320 1320 1290 1440 1440 1380 1440 1440 1440 1350 1350
OverallR2
|     | 0.15 0.16 | 0.21 0.05 | 0.14 | 0.26 | 0.10 0.05 | 0.14 0.07 | 0.14 | 0.16 |
| --- | --------- | --------- | ---- | ---- | --------- | --------- | ---- | ---- |
Notes: This table displays the outcomes of a random effects panel regression analysis. The regression models incorporate demographic
controlvariables, includinggender, age, priorexperimentalexperience, academicdegree, affiliatedinstitution, currentyearofstudy, and
risktolerancelevels. Additionally,wecontrolforparticipants’comprehensionoftheinstructions,byaddingtheparticipants’performance
in the control questions. Standard errors are presented in parentheses. Significance levels are denoted as follows: ∗p < 0.1, ∗∗p < 0.05,
∗∗∗p<0.01.
56

|     | Table B.2: | Dependent | Variable: | OptCondIndex |        |     |        |     |
| --- | ---------- | --------- | --------- | ------------ | ------ | --- | ------ | --- |
|     | Constant   | YP        | Pos       | IR           | FluctY |     | FluctP |     |
NoCalc Calc Calc NoCalc Calc Calc NoCalc Calc Calc NoCalc Calc Calc
|                  | (1) (2) | (3)      | (4) (5) | (6)      | (7) (8) | (9) (10) | (11) | (12)     |
| ---------------- | ------- | -------- | ------- | -------- | ------- | -------- | ---- | -------- |
| NoofCalculations |         | -0.001   |         | 0.001    |         | -0.001   |      | 0.001    |
|                  |         | (0.00)   |         | (0.00)   |         | (0.00)   |      | (0.00)   |
| CalcγC           |         | 0.112∗∗∗ |         | 0.052∗∗∗ |         | 0.032∗   |      | 0.057∗∗∗ |
|                  |         | (0.02)   |         | (0.01)   |         | (0.02)   |      | (0.02)   |
MinutesSpent 0.002 -0.005∗ -0.004 0.008 0.000 -0.003 -0.006 -0.005 -0.001 0.019∗∗∗ 0.002 -0.001
(0.01) (0.00) (0.00) (0.01) (0.00) (0.00) (0.01) (0.00) (0.01) (0.01) (0.00) (0.00)
Repetition2 0.001 0.034∗∗∗ 0.062∗∗∗ -0.000 -0.014 -0.005 0.031∗∗∗ 0.008 0.014 0.017 0.005 0.017
(0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.02) (0.02) (0.02)
Repetition3 0.057∗∗∗ 0.067∗∗∗ 0.080∗∗∗ 0.031∗∗ 0.037∗∗∗ 0.044∗∗∗ 0.061∗∗∗ 0.030∗∗ 0.030∗∗ 0.043∗∗∗ 0.030∗ 0.041∗∗
(0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.02) (0.02) (0.02)
0.011∗∗∗ 0.007∗∗∗ 0.006∗∗∗ 0.018∗∗∗ 0.028∗∗∗ 0.028∗∗∗ 0.009∗∗∗ 0.006∗∗∗ 0.005∗∗∗ 0.022∗∗∗ 0.016∗∗∗ 0.014∗∗∗
Period
(0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00) (0.00)
MathLevel 0.041∗ 0.012 0.012 0.006 -0.012 -0.010 -0.008 -0.003 -0.004 0.013 0.035∗∗∗ 0.031∗∗∗
(0.02) (0.01) (0.01) (0.02) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01)
BackwardInduction 0.001 0.036 0.026 -0.009 0.011 0.009 0.014 -0.009 -0.008 -0.005 0.021 0.023
(0.02) (0.02) (0.02) (0.03) (0.01) (0.01) (0.02) (0.02) (0.02) (0.02) (0.02) (0.01)
FinancialLiteracy 0.084∗∗ -0.009 -0.009 0.027 -0.020 -0.019 0.038 -0.004 -0.003 0.020 -0.009 -0.009
(0.03) (0.03) (0.02) (0.03) (0.02) (0.02) (0.03) (0.03) (0.03) (0.03) (0.02) (0.02)
ControlQuestions 0.000 0.006 0.006 0.011 0.022∗∗∗ 0.021∗∗∗ 0.006 0.014∗ 0.014 0.002 0.000 0.000
(0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.01) (0.02) (0.01) (0.01)
CalculatorUsage
CurrentPeriod 0.074∗∗∗ 0.008 0.004 0.003 -0.062∗∗ -0.075∗∗∗ -0.001 -0.025
|     | (0.02) | (0.02) | (0.03) | (0.03) | (0.02) | (0.03) | (0.03) | (0.03) |
| --- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
Partial 0.116∗∗∗ 0.050∗∗ 0.048∗ 0.043∗ 0.000 -0.025 -0.021 -0.022
|     | (0.02) | (0.02) | (0.03) | (0.03) | (0.03) | (0.03) | (0.03) | (0.03) |
| --- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
Sequential 0.028 -0.043∗ -0.049 -0.058∗ -0.001 -0.013 0.006 0.009
|          | (0.02)   | (0.02) | (0.03)   | (0.03)   | (0.02)  | (0.02)   | (0.03)  | (0.03) |
| -------- | -------- | ------ | -------- | -------- | ------- | -------- | ------- | ------ |
|          | 0.069∗∗∗ |        | 0.084∗∗∗ | 0.075∗∗∗ | -0.039∗ | -0.057∗∗ | 0.061∗∗ | 0.051∗ |
| Complete |          | -0.003 |          |          |         |          |         |        |
|          | (0.02)   | (0.02) | (0.02)   | (0.02)   | (0.02)  | (0.02)   | (0.03)  | (0.03) |
Constant 0.285 0.481 0.468 -0.159 -0.557 -0.517 0.388 0.340 0.357 0.473 0.447 0.440
(0.42) (0.47) (0.45) (0.68) (0.36) (0.36) (0.43) (0.44) (0.44) (0.99) (0.56) (0.53)
Observations 1320 1320 1320 1290 1440 1440 1380 1440 1440 1440 1350 1350
OverallR2 0.19 0.17 0.21 0.08 0.24 0.26 0.09 0.09 0.10 0.10 0.17 0.18
Notes: This table displays the outcomes of a random effects panel regression analysis. The regression models incorporate demographic
control variables, including gender, age, prior experimental experience, academic degree, affiliated institution, current year of study, and
risktolerancelevels. Additionally,wecontrolforparticipants’comprehensionoftheinstructions,byaddingtheparticipants’performance
|     |     |     |     |     |     | ∗p  | ∗∗p |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
in the control questions. Standard errors are presented in parentheses. Significance levels are denoted as follows: < 0.1, < 0.05,
∗∗∗p<0.01.
57

| C Short-Span |     |     | Planning | Model’s |     | Estimation |     |     |
| ------------ | --- | --- | -------- | ------- | --- | ---------- | --- | --- |
Our methodology relies on the notion that an individual’s initial consumption choice
is influenced by their planning horizon and includes a random error component. This
error component, denoted as ε, follows a normal distribution with a mean of zero and a
standarddeviationofσ. Therefore, theactualconsumptionchoiceforaspecificplanning
horizon, denoted by c , is given by: c = c +ε, where H varies from 1 to 10 and c
|     |     | H   |     | H   | H   |     |     | H   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
represents the theoretically optimal consumption level in Period 1 for the respective
H. Additionally, we consider the possibility that a subset of subjects may make their
consumptionchoicesrandomly. Wemodelthisbyassumingthatthesesubjects’decisions
follow a uniform distribution ranging from 0 to 10. As a result, our model considers the
population to comprise H+1 distinct planner types, each characterized by a proportion
| p for h | in the range | of  | [0,10]. |     |     |     |     |     |
| ------- | ------------ | --- | ------- | --- | --- | --- | --- | --- |
h
To define a log-likelihood function, we integrate these proportions with the corre-
sponding conditional densities. This methodology enables the computation of the sam-
ple log-likelihood for the n observations in our dataset. The log-likelihood function is
| expressed | as follows: |      |          |          |          |            |              |     |
| --------- | ----------- | ---- | -------- | -------- | -------- | ---------- | ------------ | --- |
|           |             |      |          | (cid:34) |          |            | (cid:35)     |     |
|           |             |      | n        | pˆ       | 10 1     | (cid:18) c | −c∗ (cid:19) |     |
|           |             |      | (cid:88) | 0        | (cid:88) | i,R        |              |     |
|           |             | LogL | = ln     | +        | pˆ       | φ          | H ,          |     |
h
|     |     |     |     | 100 | σ   |     | σˆ  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
i=1
h=1
where c represents the actual consumption of subject i in repetition R. The next
i,R
stepinvolvesdeterminingtheproportionspˆ andthestandarddeviationσˆ thatmaximize
h
| this log-likelihood |                  | function. |          |     |     |     |     |     |
| ------------------- | ---------------- | --------- | -------- | --- | --- | --- | --- | --- |
| C.1                 | Individual-Level |           | Analysis |     |     |     |     |     |
To assess the model’s predictions against actual planning horizons on an individual
basis, we employ σˆ to establish a range for c for each participant, thereby facilitating
H
the assignment of corresponding planning horizons. Figure C.1 illustrates this detailed
examination. The x-axis shows the horizon predicted by the short-span planning model,
58

Table C.1: Optimal Consumption Level in Pe-
riod 1, c
H
H ConstantYP PosIR FluctY FluctP
1 10.00 10.00 15.00 8.00
2 10.00 9.09 10.00 4.00
3 10.00 8.26 11.67 4.80
4 10.00 7.51 10.00 4.00
5 10.00 6.83 11.00 4.44
6 10.00 6.21 10.00 4.00
7 10.00 5.64 10.71 4.31
8 10.00 5.13 10.00 4.00
9 10.00 4.67 10.56 4.24
10 10.00 4.24 10.00 4.00
Table C.2: Estimation Outcome
Parameter Coefficient Standard Error
pˆ 0.21∗∗∗ 0.034
1
pˆ 0.118∗∗∗ 0.028
2
pˆ 0.071∗∗∗ 0.022
3
pˆ 0.035∗∗ 0.016
4
pˆ 0.032∗∗ 0.015
5
pˆ 0.025∗ 0.014
6
pˆ 0 NA
7
pˆ 0.116∗∗∗ 0.027
8
p˜ 0.001 0.021
9
pˆ 0.099∗∗∗ 0.031
10
Uncategorized 0.291∗∗∗ 0.04
σˆ 0.162∗∗∗ 0.013
Note: p was set to 0 because otherwise
7
the function did not converge. Significance
levels are denoted as follows: ∗p < 0.1,
∗∗p < 0.05, ∗∗∗p < 0.01
59

whereasthey-axispresentsthemodeofthehorizonsusedbysubjectswiththebudgeting
calculator during the first period of each repetition. Notably, the patterns observed
herein provide further insight: the actual planning horizons are typically more extended
than those predicted by the short-term horizon model. Moreover, in over 25 percent
of cases, the model either fails to categorize an individual or predicts a horizon of 1,
while subjects opt for the full horizon. Conversely, subjects adhere to the model’s full-
horizon prediction in only 3 percent of cases. Nevertheless, in approximately 3 percent of
instances, the model forecasts full horizon usage, yet individuals select a shorter horizon.
10
9
8
7
6
5
4
3
2
1
0
edoM
noziroH
0 1 2 3 4 5 6 7 8 9 10
Finite−Horizon Prediction
Observation 45−degree line
Figure C.1: Comparison between the pre-
dicted and the observed horizon at the indi-
vidual level
60

D Hand-to-Mouth Heuristic
One evident heuristic that subjects may adopt to circumvent complexity is the ”hand-
to-mouth behavior (H2M),” where they expend all their available cash each period. Yet,
this approach comes with the cost of potential utility loss. When subjects refrain from
saving in any period, they incur a utility reduction of 3.6% in PosIR and 3.4% in both
FluctP and FluctY, relative to the optimal path.23 In the ConstantYP treatment, the
optimal consumption path inherently involves zero savings per period. However, even
in this treatment, we can examine the adoption of this heuristic by observing deviations
from the unconditionally optimal consumption in at least one period. Two relevant
questions arise: Does this heuristic become more prevalent as complexity increases, and
does access to the calculator limit its usage?
To address these questions, Figure D.1 displays the percentage of subjects using the
H2M heuristic across various treatments and over time. In the ConstantYP, FluctY,
and FluctP treatments, subjects who chose not to save, given that not saving was the
implied optimal choice for that specific period, are excluded from the analysis. The
figure demonstrates that the adoption of this heuristic varies across treatments.
In the ConstantYP treatment, the percentage of subjects employing the H2M heuris-
tic is small, accounting for less than 10 percent of the periods. Furthermore, there is no
discernible distinction between subjects with calculator access and those without in this
treatment.
IntheFluctYtreatment, subjectsdisplaythecorrectintuitionbyemployingtheH2M
heuristic when their income is low, aligning with consumption smoothing principles.
Here, the heuristic was utilized in 21.99 percent of the periods when the calculator was
present and in 19.08 percent of the periods when it was absent.24
In the context of complex environments, starting with the PosIR treatment, the
absence of a calculator led to a higher incidence of the Hand to Mouth (H2M) heuristic.
23In 9% of the repetitions, participants used this heuristic in all periods.
24Runningatestontheequalityofproportionsata95%significancelevel,wedonotfindastatistically
significant difference between the two calculator conditions (p=0.0699).
61

The H2M heuristic was utilized in 12.03 percent of the periods when the calculator was
available, and in 16.02 percent of the periods when it was not (across all repetitions).
This pattern underscores the potential utility of the calculator in mitigating reliance on
H2M behavior. Notably, there were 6 subjects who consistently used this heuristic from
the beginning to the end of Repetition 3 when the calculator was not enabled, which is
double the number observed when the calculator was available.
In the FluctP treatment, the H2M heuristic was employed in 22.46 percent of the
periods with calculator access, and in 17.05 percent of periods without it, across all
repetitions.25 Notably, within this treatment, the proportion of subjects utilizing the
heuristic increases during periods of low prices, reflecting their awareness of the benefits
of purchasing more units at lower costs, though they often exceed optimal consump-
tion levels. Furthermore, considering participants who consistently applied the heuristic
throughout Repetition 3, only three subjects did so with the calculator enabled, com-
pared to seven without calculator access.
25We reject the null hypothesis of equality of proportions (p = 0.0006). A plausible explanation
for this behavior in the FluctP treatment is that employing the H2M heuristic requires more complex
arithmetic operations—specifically, dividing numbers by 50 or 150—compared to other treatments,
which typically involve divisions by 100. The budgeting calculator may encourage the adoption of the
H2M heuristic by simplifying these arithmetic challenges.
62

50
40
30
20
10
0
egatnecreP
ConstantYP
50
40
30
20
10
0
123456789 123456789 123456789
Period
egatnecreP
PosIR
123456789 123456789 123456789
Period
50
40
30
20
10
0
egatnecreP
FluctY
50
40
30
20
10
0
123456789 123456789 123456789
Period
egatnecreP
FluctP
123456789 123456789 123456789
Period
Calculator No Calculator
Figure D.1: Percentage of Subjects Using the Hand-to-Mouth Heuristic
63

| E The | Effect | of  | the Calculator |     | on Payoffs |     |     |
| ----- | ------ | --- | -------------- | --- | ---------- | --- | --- |
In this appendix, we illustrate the effect of using a calculator on payoffs. We also use
| random | choices as | a secondary | benchmark | for | comparison. |     |     |
| ------ | ---------- | ----------- | --------- | --- | ----------- | --- | --- |
The table below shows the expected payoffs in dollar terms for treatments with and
without a calculator, as well as for random consumption choice simulations. We refer to
these as expected payoffs because, for each subject, we averaged the payoffs over three
repetitions. This is because subjects were only paid based on one randomly selected
| repetition | at the end | of the | experiment. |     |     |     |     |
| ---------- | ---------- | ------ | ----------- | --- | --- | --- | --- |
For the random choice simulations, we conducted 1,000,000 simulations for each
treatment environment and repetition. We then calculated the payoffs and took the
averageovertherepetitions. Inthesesimulations, weensuredthatborrowingconstraints
were binding and that the cash balance was exhausted in consumption during the last
period.
From the table, we observe the following that subjects with access to a calculator
performedbetterthanthosewithoutintheConstantYPandPosIRtreatments, although
the difference is minimal in FluctY and FluctP. Interestingly, in the PosIR treatment,
subjects with and without a calculator performed worse than the average simulation
for the random choice model. This difference is more pronounced in the No Calculator
sessions.
Average payoffs in CAD ($) No Calc vs. Random Calc vs. Random Calc vs. No Calc
Treatment No Random (% Chg Norm by (% Chg Norm by (% Chg Norm by
Calculator
Calculator Choice by Max Payoffs) by Max Payoffs) by Max Payoffs)
| ConstantYP | 8.87 | 9.2  | 8.95 |     | -0.83% | 2.59%  | 3.42%  |
| ---------- | ---- | ---- | ---- | --- | ------ | ------ | ------ |
| PosIR      | 8.66 | 9.1  | 9.28 |     | -6.19% | -1.80% | 4.39%  |
| FluctY     | 9.19 | 9.12 | 8.95 |     | 2.49%  | 1.76%  | -0.72% |
| FluctP     | 8.89 | 8.95 | 8.81 |     | 0.83%  | 1.45%  | 0.62%  |
64

| F Individual |     |     | Time |     | Series |     |     |     |     |     |     |
| ------------ | --- | --- | ---- | --- | ------ | --- | --- | --- | --- | --- | --- |
Constant YP No Calc (Repetition 1)
|     |             |       | ID 1    |       | ID 5    |         | ID 9      |         | ID 13         |     | ID 17             |
| --- | ----------- | ----- | ------- | ----- | ------- | ------- | --------- | ------- | ------------- | --- | ----------------- |
|     |             | 50    |         | 50    |         | 50      |           | 50      |               | 50  |                   |
|     |             | 40    |         | 40    |         | 40      |           | 40      |               | 40  |                   |
|     |             | 30    |         | 30    |         | 30      |           | 30      |               | 30  |                   |
|     |             | 20    |         | 20    |         | 20      |           | 20      |               | 20  |                   |
|     |             | 10    |         | 10    |         | 10      |           | 10      |               | 10  |                   |
|     |             | 0     |         | 0     |         | 0       |           | 0       |               | 0   |                   |
|     |             | 1 2 3 | 4 5 6 7 | 8 9 1 | 2 3 4 5 | 6 7 8 9 | 1 2 3 4 5 | 6 7 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 8 9 |
|     |             |       | ID 2    |       | ID 6    |         | ID 10     |         | ID 14         |     | ID 18             |
|     |             | 50    |         | 50    |         | 50      |           | 50      |               | 50  |                   |
|     |             | 40    |         | 40    |         | 40      |           | 40      |               | 40  |                   |
|     |             | 30    |         | 30    |         | 30      |           | 30      |               | 30  |                   |
|     | noitpmusnoC | 20    |         | 20    |         | 20      |           | 20      |               | 20  |                   |
|     |             | 10    |         | 10    |         | 10      |           | 10      |               | 10  |                   |
|     |             | 0     |         | 0     |         | 0       |           | 0       |               | 0   |                   |
|     |             | 1 2 3 | 4 5 6 7 | 8 9 1 | 2 3 4 5 | 6 7 8 9 | 1 2 3 4 5 | 6 7 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 8 9 |
|     |             |       | ID 3    |       | ID 7    |         | ID 11     |         | ID 15         |     | ID 19             |
|     |             | 50    |         | 50    |         | 50      |           | 50      |               | 50  |                   |
|     |             | 40    |         | 40    |         | 40      |           | 40      |               | 40  |                   |
|     |             | 30    |         | 30    |         | 30      |           | 30      |               | 30  |                   |
|     |             | 20    |         | 20    |         | 20      |           | 20      |               | 20  |                   |
|     |             | 10    |         | 10    |         | 10      |           | 10      |               | 10  |                   |
|     |             | 0     |         | 0     |         | 0       |           | 0       |               | 0   |                   |
|     |             | 1 2 3 | 4 5 6 7 | 8 9 1 | 2 3 4 5 | 6 7 8 9 | 1 2 3 4 5 | 6 7 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 8 9 |
|     |             |       | ID 4    |       | ID 8    |         | ID 12     |         | ID 16         |     | ID 20             |
|     |             | 50    |         | 50    |         | 50      |           | 50      |               | 50  |                   |
|     |             | 40    |         | 40    |         | 40      |           | 40      |               | 40  |                   |
|     |             | 30    |         | 30    |         | 30      |           | 30      |               | 30  |                   |
|     |             | 20    |         | 20    |         | 20      |           | 20      |               | 20  |                   |
|     |             | 10    |         | 10    |         | 10      |           | 10      |               | 10  |                   |
|     |             | 0     |         | 0     |         | 0       |           | 0       |               | 0   |                   |
|     |             | 1 2 3 | 4 5 6 7 | 8 9 1 | 2 3 4 5 | 6 7 8 9 | 1 2 3 4 5 | 6 7 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 8 9 |
Period
|     |     |        |     |               | Unconditional Optimal Consumption |       |       |            |  Consumption Choice |          |     |
| --- | --- | ------ | --- | ------------- | --------------------------------- | ----- | ----- | ---------- | ------------------- | -------- | --- |
|     |     | Figure |     | F.1: Constant |                                   | YP No | Calc, | Repetition | 1                   | (Session | 1)  |
Constant YP No Calc (Repetition 3)
|     |             |       | ID 1    |       | ID 5    |         | ID 9      |         | ID 13         |     | ID 17             |
| --- | ----------- | ----- | ------- | ----- | ------- | ------- | --------- | ------- | ------------- | --- | ----------------- |
|     |             | 50    |         | 50    |         | 50      |           | 50      |               | 50  |                   |
|     |             | 40    |         | 40    |         | 40      |           | 40      |               | 40  |                   |
|     |             | 30    |         | 30    |         | 30      |           | 30      |               | 30  |                   |
|     |             | 20    |         | 20    |         | 20      |           | 20      |               | 20  |                   |
|     |             | 10    |         | 10    |         | 10      |           | 10      |               | 10  |                   |
|     |             | 0     |         | 0     |         | 0       |           | 0       |               | 0   |                   |
|     |             | 1 2 3 | 4 5 6 7 | 8 9 1 | 2 3 4 5 | 6 7 8 9 | 1 2 3 4 5 | 6 7 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 8 9 |
|     |             |       | ID 2    |       | ID 6    |         | ID 10     |         | ID 14         |     | ID 18             |
|     |             | 50    |         | 50    |         | 50      |           | 50      |               | 50  |                   |
|     |             | 40    |         | 40    |         | 40      |           | 40      |               | 40  |                   |
|     |             | 30    |         | 30    |         | 30      |           | 30      |               | 30  |                   |
|     |             | 20    |         | 20    |         | 20      |           | 20      |               | 20  |                   |
|     | noitpmusnoC | 10    |         | 10    |         | 10      |           | 10      |               | 10  |                   |
|     |             | 0     |         | 0     |         | 0       |           | 0       |               | 0   |                   |
|     |             | 1 2 3 | 4 5 6 7 | 8 9 1 | 2 3 4 5 | 6 7 8 9 | 1 2 3 4 5 | 6 7 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 8 9 |
|     |             |       | ID 3    |       | ID 7    |         | ID 11     |         | ID 15         |     | ID 19             |
|     |             | 50    |         | 50    |         | 50      |           | 50      |               | 50  |                   |
|     |             | 40    |         | 40    |         | 40      |           | 40      |               | 40  |                   |
|     |             | 30    |         | 30    |         | 30      |           | 30      |               | 30  |                   |
|     |             | 20    |         | 20    |         | 20      |           | 20      |               | 20  |                   |
|     |             | 10    |         | 10    |         | 10      |           | 10      |               | 10  |                   |
|     |             | 0     |         | 0     |         | 0       |           | 0       |               | 0   |                   |
|     |             | 1 2 3 | 4 5 6 7 | 8 9 1 | 2 3 4 5 | 6 7 8 9 | 1 2 3 4 5 | 6 7 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 8 9 |
|     |             |       | ID 4    |       | ID 8    |         | ID 12     |         | ID 16         |     | ID 20             |
|     |             | 50    |         | 50    |         | 50      |           | 50      |               | 50  |                   |
|     |             | 40    |         | 40    |         | 40      |           | 40      |               | 40  |                   |
|     |             | 30    |         | 30    |         | 30      |           | 30      |               | 30  |                   |
|     |             | 20    |         | 20    |         | 20      |           | 20      |               | 20  |                   |
|     |             | 10    |         | 10    |         | 10      |           | 10      |               | 10  |                   |
|     |             | 0     |         | 0     |         | 0       |           | 0       |               | 0   |                   |
|     |             | 1 2 3 | 4 5 6 7 | 8 9 1 | 2 3 4 5 | 6 7 8 9 | 1 2 3 4 5 | 6 7 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 8 9 |
Period
|     |     |        |     |               | Unconditional Optimal Consumption |       |       |            |  Consumption Choice |          |     |
| --- | --- | ------ | --- | ------------- | --------------------------------- | ----- | ----- | ---------- | ------------------- | -------- | --- |
|     |     | Figure |     | F.2: Constant |                                   | YP No | Calc, | Repetition | 3                   | (Session | 1)  |
65

Constant YP No Calc (Repetition 1)
|             | ID 21         | ID 25             | ID 29             | ID 33             | ID 37             | ID 41                 |
| ----------- | ------------- | ----------------- | ----------------- | ----------------- | ----------------- | --------------------- |
|             | 50            | 50                | 50                | 50                | 50                | 50                    |
|             | 40            | 40                | 40                | 40                | 40                | 40                    |
|             | 30            | 30                | 30                | 30                | 30                | 30                    |
|             | 20            | 20                | 20                | 20                | 20                | 20                    |
|             | 10            | 10                | 10                | 10                | 10                | 10                    |
|             | 0             | 0                 | 0                 | 0                 | 0                 | 0                     |
|             | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|             | ID 22         | ID 26             | ID 30             | ID 34             | ID 38             | ID 42                 |
|             | 50            | 50                | 50                | 50                | 50                | 50                    |
|             | 40            | 40                | 40                | 40                | 40                | 40                    |
|             | 30            | 30                | 30                | 30                | 30                | 30                    |
|             | 20            | 20                | 20                | 20                | 20                | 20                    |
| noitpmusnoC | 10            | 10                | 10                | 10                | 10                | 10                    |
|             | 0             | 0                 | 0                 | 0                 | 0                 | 0                     |
|             | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|             | ID 23         | ID 27             | ID 31             | ID 35             | ID 39             | ID 43                 |
|             | 50            | 50                | 50                | 50                | 50                | 50                    |
|             | 40            | 40                | 40                | 40                | 40                | 40                    |
|             | 30            | 30                | 30                | 30                | 30                | 30                    |
|             | 20            | 20                | 20                | 20                | 20                | 20                    |
|             | 10            | 10                | 10                | 10                | 10                | 10                    |
|             | 0             | 0                 | 0                 | 0                 | 0                 | 0                     |
|             | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|             | ID 24         | ID 28             | ID 32             | ID 36             | ID 40             | ID 44                 |
|             | 50            | 50                | 50                | 50                | 50                | 50                    |
|             | 40            | 40                | 40                | 40                | 40                | 40                    |
|             | 30            | 30                | 30                | 30                | 30                | 30                    |
|             | 20            | 20                | 20                | 20                | 20                | 20                    |
|             | 10            | 10                | 10                | 10                | 10                | 10                    |
|             | 0             | 0                 | 0                 | 0                 | 0                 | 0                     |
|             | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
Period
|     |        |               | Unconditional Optimal Consumption |                  |  Consumption Choice |     |
| --- | ------ | ------------- | --------------------------------- | ---------------- | ------------------- | --- |
|     | Figure | F.3: Constant | YP No                             | Calc, Repetition | 1 (Session          | 2)  |
Constant YP No Calc (Repetition 3)
|             | ID 21         | ID 25             | ID 29             | ID 33             | ID 37             | ID 41                 |
| ----------- | ------------- | ----------------- | ----------------- | ----------------- | ----------------- | --------------------- |
|             | 50            | 50                | 50                | 50                | 50                | 50                    |
|             | 40            | 40                | 40                | 40                | 40                | 40                    |
|             | 30            | 30                | 30                | 30                | 30                | 30                    |
|             | 20            | 20                | 20                | 20                | 20                | 20                    |
|             | 10            | 10                | 10                | 10                | 10                | 10                    |
|             | 0             | 0                 | 0                 | 0                 | 0                 | 0                     |
|             | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|             | ID 22         | ID 26             | ID 30             | ID 34             | ID 38             | ID 42                 |
|             | 50            | 50                | 50                | 50                | 50                | 50                    |
|             | 40            | 40                | 40                | 40                | 40                | 40                    |
|             | 30            | 30                | 30                | 30                | 30                | 30                    |
| noitpmusnoC | 20            | 20                | 20                | 20                | 20                | 20                    |
|             | 10            | 10                | 10                | 10                | 10                | 10                    |
|             | 0             | 0                 | 0                 | 0                 | 0                 | 0                     |
|             | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|             | ID 23         | ID 27             | ID 31             | ID 35             | ID 39             | ID 43                 |
|             | 50            | 50                | 50                | 50                | 50                | 50                    |
|             | 40            | 40                | 40                | 40                | 40                | 40                    |
|             | 30            | 30                | 30                | 30                | 30                | 30                    |
|             | 20            | 20                | 20                | 20                | 20                | 20                    |
|             | 10            | 10                | 10                | 10                | 10                | 10                    |
|             | 0             | 0                 | 0                 | 0                 | 0                 | 0                     |
|             | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|             | ID 24         | ID 28             | ID 32             | ID 36             | ID 40             | ID 44                 |
|             | 50            | 50                | 50                | 50                | 50                | 50                    |
|             | 40            | 40                | 40                | 40                | 40                | 40                    |
|             | 30            | 30                | 30                | 30                | 30                | 30                    |
|             | 20            | 20                | 20                | 20                | 20                | 20                    |
|             | 10            | 10                | 10                | 10                | 10                | 10                    |
|             | 0             | 0                 | 0                 | 0                 | 0                 | 0                     |
|             | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
Period
|     |        |               | Unconditional Optimal Consumption |                  |  Consumption Choice |     |
| --- | ------ | ------------- | --------------------------------- | ---------------- | ------------------- | --- |
|     | Figure | F.4: Constant | YP No                             | Calc, Repetition | 3 (Session          | 2)  |
66

Constant YP No Calc (Repetition 1)
|                | ID 1          |     | ID 5          | ID 9              | ID 13             | ID 17             | ID 21                 |
| -------------- | ------------- | --- | ------------- | ----------------- | ----------------- | ----------------- | --------------------- |
| 50             |               | 50  |               | 50                | 50                | 50                | 50                    |
| 40             |               | 40  |               | 40                | 40                | 40                | 40                    |
| 30             |               | 30  |               | 30                | 30                | 30                | 30                    |
| 20             |               | 20  |               | 20                | 20                | 20                | 20                    |
| 10             |               | 10  |               | 10                | 10                | 10                | 10                    |
| 0              |               | 0   |               | 0                 | 0                 | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 2          |     | ID 6          | ID 10             | ID 14             | ID 18             | ID 22                 |
| 50             |               | 50  |               | 50                | 50                | 50                | 50                    |
| 40             |               | 40  |               | 40                | 40                | 40                | 40                    |
| 30             |               | 30  |               | 30                | 30                | 30                | 30                    |
| 20             |               | 20  |               | 20                | 20                | 20                | 20                    |
| noitpmusnoC 10 |               | 10  |               | 10                | 10                | 10                | 10                    |
| 0              |               | 0   |               | 0                 | 0                 | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 3          |     | ID 7          | ID 11             | ID 15             | ID 19             |                       |
| 50             |               | 50  |               | 50                | 50                | 50                |                       |
| 40             |               | 40  |               | 40                | 40                | 40                |                       |
| 30             |               | 30  |               | 30                | 30                | 30                |                       |
| 20             |               | 20  |               | 20                | 20                | 20                |                       |
| 10             |               | 10  |               | 10                | 10                | 10                |                       |
| 0              |               | 0   |               | 0                 | 0                 | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
|                | ID 4          |     | ID 8          | ID 12             | ID 16             | ID 20             |                       |
| 50             |               | 50  |               | 50                | 50                | 50                |                       |
| 40             |               | 40  |               | 40                | 40                | 40                |                       |
| 30             |               | 30  |               | 30                | 30                | 30                |                       |
| 20             |               | 20  |               | 20                | 20                | 20                |                       |
| 10             |               | 10  |               | 10                | 10                | 10                |                       |
| 0              |               | 0   |               | 0                 | 0                 | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
Period
|     |        |      |          | Unconditional Optimal Consumption |                  |  Consumption Choice |     |
| --- | ------ | ---- | -------- | --------------------------------- | ---------------- | ------------------- | --- |
|     | Figure | F.5: | Constant | YP                                | Calc, Repetition | 1 (Session          | 1)  |
Constant YP No Calc (Repetition 3)
|                | ID 1          |     | ID 5          | ID 9              | ID 13             | ID 17             | ID 21                 |
| -------------- | ------------- | --- | ------------- | ----------------- | ----------------- | ----------------- | --------------------- |
| 50             |               | 50  |               | 50                | 50                | 50                | 50                    |
| 40             |               | 40  |               | 40                | 40                | 40                | 40                    |
| 30             |               | 30  |               | 30                | 30                | 30                | 30                    |
| 20             |               | 20  |               | 20                | 20                | 20                | 20                    |
| 10             |               | 10  |               | 10                | 10                | 10                | 10                    |
| 0              |               | 0   |               | 0                 | 0                 | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 2          |     | ID 6          | ID 10             | ID 14             | ID 18             | ID 22                 |
| 50             |               | 50  |               | 50                | 50                | 50                | 50                    |
| 40             |               | 40  |               | 40                | 40                | 40                | 40                    |
| 30             |               | 30  |               | 30                | 30                | 30                | 30                    |
| noitpmusnoC 20 |               | 20  |               | 20                | 20                | 20                | 20                    |
| 10             |               | 10  |               | 10                | 10                | 10                | 10                    |
| 0              |               | 0   |               | 0                 | 0                 | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 3          |     | ID 7          | ID 11             | ID 15             | ID 19             |                       |
| 50             |               | 50  |               | 50                | 50                | 50                |                       |
| 40             |               | 40  |               | 40                | 40                | 40                |                       |
| 30             |               | 30  |               | 30                | 30                | 30                |                       |
| 20             |               | 20  |               | 20                | 20                | 20                |                       |
| 10             |               | 10  |               | 10                | 10                | 10                |                       |
| 0              |               | 0   |               | 0                 | 0                 | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
|                | ID 4          |     | ID 8          | ID 12             | ID 16             | ID 20             |                       |
| 50             |               | 50  |               | 50                | 50                | 50                |                       |
| 40             |               | 40  |               | 40                | 40                | 40                |                       |
| 30             |               | 30  |               | 30                | 30                | 30                |                       |
| 20             |               | 20  |               | 20                | 20                | 20                |                       |
| 10             |               | 10  |               | 10                | 10                | 10                |                       |
| 0              |               | 0   |               | 0                 | 0                 | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
Period
|     |        |      |          | Unconditional Optimal Consumption |                  |  Consumption Choice |     |
| --- | ------ | ---- | -------- | --------------------------------- | ---------------- | ------------------- | --- |
|     | Figure | F.6: | Constant | YP                                | Calc, Repetition | 3 (Session          | 1)  |
67

Constant YP Calc (Repetition 1)
|             | ID 23         |     | ID 27         | ID 31             | ID 35             | ID 39             | ID 43                 |
| ----------- | ------------- | --- | ------------- | ----------------- | ----------------- | ----------------- | --------------------- |
|             | 50            | 50  |               | 50                | 50                | 50                | 50                    |
|             | 40            | 40  |               | 40                | 40                | 40                | 40                    |
|             | 30            | 30  |               | 30                | 30                | 30                | 30                    |
|             | 20            | 20  |               | 20                | 20                | 20                | 20                    |
|             | 10            | 10  |               | 10                | 10                | 10                | 10                    |
|             | 0             | 0   |               | 0                 | 0                 | 0                 | 0                     |
|             | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|             | ID 24         |     | ID 28         | ID 32             | ID 36             | ID 40             | ID 44                 |
|             | 50            | 50  |               | 50                | 50                | 50                | 50                    |
|             | 40            | 40  |               | 40                | 40                | 40                | 40                    |
|             | 30            | 30  |               | 30                | 30                | 30                | 30                    |
|             | 20            | 20  |               | 20                | 20                | 20                | 20                    |
| noitpmusnoC | 10            | 10  |               | 10                | 10                | 10                | 10                    |
|             | 0             | 0   |               | 0                 | 0                 | 0                 | 0                     |
|             | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|             | ID 25         |     | ID 29         | ID 33             | ID 37             | ID 41             |                       |
|             | 50            | 50  |               | 50                | 50                | 50                |                       |
|             | 40            | 40  |               | 40                | 40                | 40                |                       |
|             | 30            | 30  |               | 30                | 30                | 30                |                       |
|             | 20            | 20  |               | 20                | 20                | 20                |                       |
|             | 10            | 10  |               | 10                | 10                | 10                |                       |
|             | 0             | 0   |               | 0                 | 0                 | 0                 |                       |
|             | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
|             | ID 26         |     | ID 30         | ID 34             | ID 38             | ID 42             |                       |
|             | 50            | 50  |               | 50                | 50                | 50                |                       |
|             | 40            | 40  |               | 40                | 40                | 40                |                       |
|             | 30            | 30  |               | 30                | 30                | 30                |                       |
|             | 20            | 20  |               | 20                | 20                | 20                |                       |
|             | 10            | 10  |               | 10                | 10                | 10                |                       |
|             | 0             | 0   |               | 0                 | 0                 | 0                 |                       |
|             | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
Period
|     |        |      |          | Unconditional Optimal Consumption |                  |  Consumption Choice |     |
| --- | ------ | ---- | -------- | --------------------------------- | ---------------- | ------------------- | --- |
|     | Figure | F.7: | Constant | YP No                             | Calc, Repetition | 1 (Session          | 2)  |
Constant YP Calc (Repetition 3)
|             | ID 23         |     | ID 27         | ID 31             | ID 35             | ID 39             | ID 43                 |
| ----------- | ------------- | --- | ------------- | ----------------- | ----------------- | ----------------- | --------------------- |
|             | 50            | 50  |               | 50                | 50                | 50                | 50                    |
|             | 40            | 40  |               | 40                | 40                | 40                | 40                    |
|             | 30            | 30  |               | 30                | 30                | 30                | 30                    |
|             | 20            | 20  |               | 20                | 20                | 20                | 20                    |
|             | 10            | 10  |               | 10                | 10                | 10                | 10                    |
|             | 0             | 0   |               | 0                 | 0                 | 0                 | 0                     |
|             | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|             | ID 24         |     | ID 28         | ID 32             | ID 36             | ID 40             | ID 44                 |
|             | 50            | 50  |               | 50                | 50                | 50                | 50                    |
|             | 40            | 40  |               | 40                | 40                | 40                | 40                    |
|             | 30            | 30  |               | 30                | 30                | 30                | 30                    |
| noitpmusnoC | 20            | 20  |               | 20                | 20                | 20                | 20                    |
|             | 10            | 10  |               | 10                | 10                | 10                | 10                    |
|             | 0             | 0   |               | 0                 | 0                 | 0                 | 0                     |
|             | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|             | ID 25         |     | ID 29         | ID 33             | ID 37             | ID 41             |                       |
|             | 50            | 50  |               | 50                | 50                | 50                |                       |
|             | 40            | 40  |               | 40                | 40                | 40                |                       |
|             | 30            | 30  |               | 30                | 30                | 30                |                       |
|             | 20            | 20  |               | 20                | 20                | 20                |                       |
|             | 10            | 10  |               | 10                | 10                | 10                |                       |
|             | 0             | 0   |               | 0                 | 0                 | 0                 |                       |
|             | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
|             | ID 26         |     | ID 30         | ID 34             | ID 38             | ID 42             |                       |
|             | 50            | 50  |               | 50                | 50                | 50                |                       |
|             | 40            | 40  |               | 40                | 40                | 40                |                       |
|             | 30            | 30  |               | 30                | 30                | 30                |                       |
|             | 20            | 20  |               | 20                | 20                | 20                |                       |
|             | 10            | 10  |               | 10                | 10                | 10                |                       |
|             | 0             | 0   |               | 0                 | 0                 | 0                 |                       |
|             | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
Period
|     |        |      |          | Unconditional Optimal Consumption |                  |  Consumption Choice |     |
| --- | ------ | ---- | -------- | --------------------------------- | ---------------- | ------------------- | --- |
|     | Figure | F.8: | Constant | YP                                | Calc, Repetition | 3 (Session          | 2)  |
68

Pos IR No Calc (Repetition 1)
|                | ID 1          |         | ID 5      |       | ID 9        | ID 13             | ID 17             | ID 21                 |
| -------------- | ------------- | ------- | --------- | ----- | ----------- | ----------------- | ----------------- | --------------------- |
| 50             |               | 50      |           | 50    |             | 50                | 50                | 50                    |
| 40             |               | 40      |           | 40    |             | 40                | 40                | 40                    |
| 30             |               | 30      |           | 30    |             | 30                | 30                | 30                    |
| 20             |               | 20      |           | 20    |             | 20                | 20                | 20                    |
| 10             |               | 10      |           | 10    |             | 10                | 10                | 10                    |
| 0              |               | 0       |           | 0     |             | 0                 | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 | 8 9 1 | 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 2          |         | ID 6      |       | ID 10       | ID 14             | ID 18             | ID 22                 |
| 50             |               | 50      |           | 50    |             | 50                | 50                | 50                    |
| 40             |               | 40      |           | 40    |             | 40                | 40                | 40                    |
| 30             |               | 30      |           | 30    |             | 30                | 30                | 30                    |
| 20             |               | 20      |           | 20    |             | 20                | 20                | 20                    |
| noitpmusnoC 10 |               | 10      |           | 10    |             | 10                | 10                | 10                    |
| 0              |               | 0       |           | 0     |             | 0                 | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 | 8 9 1 | 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 3          |         | ID 7      |       | ID 11       | ID 15             | ID 19             |                       |
| 50             |               | 50      |           | 50    |             | 50                | 50                |                       |
| 40             |               | 40      |           | 40    |             | 40                | 40                |                       |
| 30             |               | 30      |           | 30    |             | 30                | 30                |                       |
| 20             |               | 20      |           | 20    |             | 20                | 20                |                       |
| 10             |               | 10      |           | 10    |             | 10                | 10                |                       |
| 0              |               | 0       |           | 0     |             | 0                 | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 | 8 9 1 | 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
|                | ID 4          |         | ID 8      |       | ID 12       | ID 16             | ID 20             |                       |
| 50             |               | 50      |           | 50    |             | 50                | 50                |                       |
| 40             |               | 40      |           | 40    |             | 40                | 40                |                       |
| 30             |               | 30      |           | 30    |             | 30                | 30                |                       |
| 20             |               | 20      |           | 20    |             | 20                | 20                |                       |
| 10             |               | 10      |           | 10    |             | 10                | 10                |                       |
| 0              |               | 0       |           | 0     |             | 0                 | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 | 8 9 1 | 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
Period
|     |        |      |     | Unconditional Optimal Consumption |          |            |  Consumption Choice |     |
| --- | ------ | ---- | --- | --------------------------------- | -------- | ---------- | ------------------- | --- |
|     | Figure | F.9: | Pos | IR                                | No Calc, | Repetition | 1 (Session          | 1)  |
Pos IR No Calc (Repetition 3)
|                | ID 1          |         | ID 5      |       | ID 9        | ID 13             | ID 17             | ID 21                 |
| -------------- | ------------- | ------- | --------- | ----- | ----------- | ----------------- | ----------------- | --------------------- |
| 50             |               | 50      |           | 50    |             | 50                | 50                | 50                    |
| 40             |               | 40      |           | 40    |             | 40                | 40                | 40                    |
| 30             |               | 30      |           | 30    |             | 30                | 30                | 30                    |
| 20             |               | 20      |           | 20    |             | 20                | 20                | 20                    |
| 10             |               | 10      |           | 10    |             | 10                | 10                | 10                    |
| 0              |               | 0       |           | 0     |             | 0                 | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 | 8 9 1 | 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 2          |         | ID 6      |       | ID 10       | ID 14             | ID 18             | ID 22                 |
| 50             |               | 50      |           | 50    |             | 50                | 50                | 50                    |
| 40             |               | 40      |           | 40    |             | 40                | 40                | 40                    |
| 30             |               | 30      |           | 30    |             | 30                | 30                | 30                    |
| noitpmusnoC 20 |               | 20      |           | 20    |             | 20                | 20                | 20                    |
| 10             |               | 10      |           | 10    |             | 10                | 10                | 10                    |
| 0              |               | 0       |           | 0     |             | 0                 | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 | 8 9 1 | 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 3          |         | ID 7      |       | ID 11       | ID 15             | ID 19             |                       |
| 50             |               | 50      |           | 50    |             | 50                | 50                |                       |
| 40             |               | 40      |           | 40    |             | 40                | 40                |                       |
| 30             |               | 30      |           | 30    |             | 30                | 30                |                       |
| 20             |               | 20      |           | 20    |             | 20                | 20                |                       |
| 10             |               | 10      |           | 10    |             | 10                | 10                |                       |
| 0              |               | 0       |           | 0     |             | 0                 | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 | 8 9 1 | 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
|                | ID 4          |         | ID 8      |       | ID 12       | ID 16             | ID 20             |                       |
| 50             |               | 50      |           | 50    |             | 50                | 50                |                       |
| 40             |               | 40      |           | 40    |             | 40                | 40                |                       |
| 30             |               | 30      |           | 30    |             | 30                | 30                |                       |
| 20             |               | 20      |           | 20    |             | 20                | 20                |                       |
| 10             |               | 10      |           | 10    |             | 10                | 10                |                       |
| 0              |               | 0       |           | 0     |             | 0                 | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 | 8 9 1 | 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
Period
|     |        |       |     | Unconditional Optimal Consumption |          |            |  Consumption Choice |     |
| --- | ------ | ----- | --- | --------------------------------- | -------- | ---------- | ------------------- | --- |
|     | Figure | F.10: | Pos | IR                                | No Calc, | Repetition | 3 (Session          | 1)  |
69

Pos IR No Calc (Repetition 1)
|                | ID 23         |         | ID 27       |       | ID 31       | ID 35           | ID 39             | ID 43                 |
| -------------- | ------------- | ------- | ----------- | ----- | ----------- | --------------- | ----------------- | --------------------- |
| 50             |               | 50      |             | 50    |             | 50              | 50                | 50                    |
| 40             |               | 40      |             | 40    |             | 40              | 40                | 40                    |
| 30             |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| 20             |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| 10             |               | 10      |             | 10    |             | 10              | 10                | 10                    |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 24         |         | ID 28       |       | ID 32       | ID 36           | ID 40             |                       |
| 50             |               | 50      |             | 50    |             | 50              | 50                |                       |
| 40             |               | 40      |             | 40    |             | 40              | 40                |                       |
| 30             |               | 30      |             | 30    |             | 30              | 30                |                       |
| 20             |               | 20      |             | 20    |             | 20              | 20                |                       |
| noitpmusnoC 10 |               | 10      |             | 10    |             | 10              | 10                |                       |
| 0              |               | 0       |             | 0     |             | 0               | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
|                | ID 25         |         | ID 29       |       | ID 33       | ID 37           | ID 41             |                       |
| 50             |               | 50      |             | 50    |             | 50              | 50                |                       |
| 40             |               | 40      |             | 40    |             | 40              | 40                |                       |
| 30             |               | 30      |             | 30    |             | 30              | 30                |                       |
| 20             |               | 20      |             | 20    |             | 20              | 20                |                       |
| 10             |               | 10      |             | 10    |             | 10              | 10                |                       |
| 0              |               | 0       |             | 0     |             | 0               | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
|                | ID 26         |         | ID 30       |       | ID 34       | ID 38           | ID 42             |                       |
| 50             |               | 50      |             | 50    |             | 50              | 50                |                       |
| 40             |               | 40      |             | 40    |             | 40              | 40                |                       |
| 30             |               | 30      |             | 30    |             | 30              | 30                |                       |
| 20             |               | 20      |             | 20    |             | 20              | 20                |                       |
| 10             |               | 10      |             | 10    |             | 10              | 10                |                       |
| 0              |               | 0       |             | 0     |             | 0               | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
Period
|     |        |       | Unconditional Optimal Consumption |     |          |            |  Consumption Choice |     |
| --- | ------ | ----- | --------------------------------- | --- | -------- | ---------- | ------------------- | --- |
|     | Figure | F.11: | Pos                               | IR  | No Calc, | Repetition | 1 (Session          | 2)  |
Pos IR No Calc (Repetition 3)
|                | ID 23         |         | ID 27       |       | ID 31       | ID 35           | ID 39             | ID 43                 |
| -------------- | ------------- | ------- | ----------- | ----- | ----------- | --------------- | ----------------- | --------------------- |
| 50             |               | 50      |             | 50    |             | 50              | 50                | 50                    |
| 40             |               | 40      |             | 40    |             | 40              | 40                | 40                    |
| 30             |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| 20             |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| 10             |               | 10      |             | 10    |             | 10              | 10                | 10                    |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 24         |         | ID 28       |       | ID 32       | ID 36           | ID 40             |                       |
| 50             |               | 50      |             | 50    |             | 50              | 50                |                       |
| 40             |               | 40      |             | 40    |             | 40              | 40                |                       |
| 30             |               | 30      |             | 30    |             | 30              | 30                |                       |
| noitpmusnoC 20 |               | 20      |             | 20    |             | 20              | 20                |                       |
| 10             |               | 10      |             | 10    |             | 10              | 10                |                       |
| 0              |               | 0       |             | 0     |             | 0               | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
|                | ID 25         |         | ID 29       |       | ID 33       | ID 37           | ID 41             |                       |
| 50             |               | 50      |             | 50    |             | 50              | 50                |                       |
| 40             |               | 40      |             | 40    |             | 40              | 40                |                       |
| 30             |               | 30      |             | 30    |             | 30              | 30                |                       |
| 20             |               | 20      |             | 20    |             | 20              | 20                |                       |
| 10             |               | 10      |             | 10    |             | 10              | 10                |                       |
| 0              |               | 0       |             | 0     |             | 0               | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
|                | ID 26         |         | ID 30       |       | ID 34       | ID 38           | ID 42             |                       |
| 50             |               | 50      |             | 50    |             | 50              | 50                |                       |
| 40             |               | 40      |             | 40    |             | 40              | 40                |                       |
| 30             |               | 30      |             | 30    |             | 30              | 30                |                       |
| 20             |               | 20      |             | 20    |             | 20              | 20                |                       |
| 10             |               | 10      |             | 10    |             | 10              | 10                |                       |
| 0              |               | 0       |             | 0     |             | 0               | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
Period
|     |        |       | Unconditional Optimal Consumption |     |          |            |  Consumption Choice |     |
| --- | ------ | ----- | --------------------------------- | --- | -------- | ---------- | ------------------- | --- |
|     | Figure | F.12: | Pos                               | IR  | No Calc, | Repetition | 3 (Session          | 2)  |
70

Pos IR Calc (Repetition 1)
|                | ID 1          | ID 5        |           | ID 9        | ID 13             | ID 17             |       | ID 21             |
| -------------- | ------------- | ----------- | --------- | ----------- | ----------------- | ----------------- | ----- | ----------------- |
| 50             |               | 50          | 50        |             | 50                | 50                | 50    |                   |
| 40             |               | 40          | 40        |             | 40                | 40                | 40    |                   |
| 30             |               | 30          | 30        |             | 30                | 30                | 30    |                   |
| 20             |               | 20          | 20        |             | 20                | 20                | 20    |                   |
| 10             |               | 10          | 10        |             | 10                | 10                | 10    |                   |
| 0              |               | 0           | 0         |             | 0                 | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 | 5 6 7 8 9 | 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 2          | ID 6        |           | ID 10       | ID 14             | ID 18             |       | ID 22             |
| 50             |               | 50          | 50        |             | 50                | 50                | 50    |                   |
| 40             |               | 40          | 40        |             | 40                | 40                | 40    |                   |
| 30             |               | 30          | 30        |             | 30                | 30                | 30    |                   |
| 20             |               | 20          | 20        |             | 20                | 20                | 20    |                   |
| noitpmusnoC 10 |               | 10          | 10        |             | 10                | 10                | 10    |                   |
| 0              |               | 0           | 0         |             | 0                 | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 | 5 6 7 8 9 | 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 3          | ID 7        |           | ID 11       | ID 15             | ID 19             |       | ID 23             |
| 50             |               | 50          | 50        |             | 50                | 50                | 50    |                   |
| 40             |               | 40          | 40        |             | 40                | 40                | 40    |                   |
| 30             |               | 30          | 30        |             | 30                | 30                | 30    |                   |
| 20             |               | 20          | 20        |             | 20                | 20                | 20    |                   |
| 10             |               | 10          | 10        |             | 10                | 10                | 10    |                   |
| 0              |               | 0           | 0         |             | 0                 | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 | 5 6 7 8 9 | 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 4          | ID 8        |           | ID 12       | ID 16             | ID 20             |       | ID 24             |
| 50             |               | 50          | 50        |             | 50                | 50                | 50    |                   |
| 40             |               | 40          | 40        |             | 40                | 40                | 40    |                   |
| 30             |               | 30          | 30        |             | 30                | 30                | 30    |                   |
| 20             |               | 20          | 20        |             | 20                | 20                | 20    |                   |
| 10             |               | 10          | 10        |             | 10                | 10                | 10    |                   |
| 0              |               | 0           | 0         |             | 0                 | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 | 5 6 7 8 9 | 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
Period
|     |        |       | Unconditional Optimal Consumption |          |            |  Consumption Choice |     |     |
| --- | ------ | ----- | --------------------------------- | -------- | ---------- | ------------------- | --- | --- |
|     | Figure | F.13: | Pos                               | IR Calc, | Repetition | 1 (Session          | 1)  |     |
Pos IR Calc (Repetition 3)
|                | ID 1          | ID 5        |           | ID 9        | ID 13             | ID 17             |       | ID 21             |
| -------------- | ------------- | ----------- | --------- | ----------- | ----------------- | ----------------- | ----- | ----------------- |
| 50             |               | 50          | 50        |             | 50                | 50                | 50    |                   |
| 40             |               | 40          | 40        |             | 40                | 40                | 40    |                   |
| 30             |               | 30          | 30        |             | 30                | 30                | 30    |                   |
| 20             |               | 20          | 20        |             | 20                | 20                | 20    |                   |
| 10             |               | 10          | 10        |             | 10                | 10                | 10    |                   |
| 0              |               | 0           | 0         |             | 0                 | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 | 5 6 7 8 9 | 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 2          | ID 6        |           | ID 10       | ID 14             | ID 18             |       | ID 22             |
| 50             |               | 50          | 50        |             | 50                | 50                | 50    |                   |
| 40             |               | 40          | 40        |             | 40                | 40                | 40    |                   |
| 30             |               | 30          | 30        |             | 30                | 30                | 30    |                   |
| noitpmusnoC 20 |               | 20          | 20        |             | 20                | 20                | 20    |                   |
| 10             |               | 10          | 10        |             | 10                | 10                | 10    |                   |
| 0              |               | 0           | 0         |             | 0                 | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 | 5 6 7 8 9 | 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 3          | ID 7        |           | ID 11       | ID 15             | ID 19             |       | ID 23             |
| 50             |               | 50          | 50        |             | 50                | 50                | 50    |                   |
| 40             |               | 40          | 40        |             | 40                | 40                | 40    |                   |
| 30             |               | 30          | 30        |             | 30                | 30                | 30    |                   |
| 20             |               | 20          | 20        |             | 20                | 20                | 20    |                   |
| 10             |               | 10          | 10        |             | 10                | 10                | 10    |                   |
| 0              |               | 0           | 0         |             | 0                 | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 | 5 6 7 8 9 | 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 4          | ID 8        |           | ID 12       | ID 16             | ID 20             |       | ID 24             |
| 50             |               | 50          | 50        |             | 50                | 50                | 50    |                   |
| 40             |               | 40          | 40        |             | 40                | 40                | 40    |                   |
| 30             |               | 30          | 30        |             | 30                | 30                | 30    |                   |
| 20             |               | 20          | 20        |             | 20                | 20                | 20    |                   |
| 10             |               | 10          | 10        |             | 10                | 10                | 10    |                   |
| 0              |               | 0           | 0         |             | 0                 | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 | 5 6 7 8 9 | 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
Period
|     |        |       | Unconditional Optimal Consumption |          |            |  Consumption Choice |     |     |
| --- | ------ | ----- | --------------------------------- | -------- | ---------- | ------------------- | --- | --- |
|     | Figure | F.14: | Pos                               | IR Calc, | Repetition | 3 (Session          | 1)  |     |
71

Pos IR Calc (Repetition 1)
|                | ID 25         |         | ID 29       |       | ID 33       | ID 37         | ID 41             |       | ID 45             |
| -------------- | ------------- | ------- | ----------- | ----- | ----------- | ------------- | ----------------- | ----- | ----------------- |
| 50             |               | 50      |             | 50    |             | 50            | 50                | 50    |                   |
| 40             |               | 40      |             | 40    |             | 40            | 40                | 40    |                   |
| 30             |               | 30      |             | 30    |             | 30            | 30                | 30    |                   |
| 20             |               | 20      |             | 20    |             | 20            | 20                | 20    |                   |
| 10             |               | 10      |             | 10    |             | 10            | 10                | 10    |                   |
| 0              |               | 0       |             | 0     |             | 0             | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 26         |         | ID 30       |       | ID 34       | ID 38         | ID 42             |       | ID 46             |
| 50             |               | 50      |             | 50    |             | 50            | 50                | 50    |                   |
| 40             |               | 40      |             | 40    |             | 40            | 40                | 40    |                   |
| 30             |               | 30      |             | 30    |             | 30            | 30                | 30    |                   |
| 20             |               | 20      |             | 20    |             | 20            | 20                | 20    |                   |
| noitpmusnoC 10 |               | 10      |             | 10    |             | 10            | 10                | 10    |                   |
| 0              |               | 0       |             | 0     |             | 0             | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 27         |         | ID 31       |       | ID 35       | ID 39         | ID 43             |       | 47                |
| 50             |               | 50      |             | 50    |             | 50            | 50                | 50    |                   |
| 40             |               | 40      |             | 40    |             | 40            | 40                | 40    |                   |
| 30             |               | 30      |             | 30    |             | 30            | 30                | 30    |                   |
| 20             |               | 20      |             | 20    |             | 20            | 20                | 20    |                   |
| 10             |               | 10      |             | 10    |             | 10            | 10                | 10    |                   |
| 0              |               | 0       |             | 0     |             | 0             | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 28         |         | ID 32       |       | ID 36       | ID 40         | ID 44             |       | 48                |
| 50             |               | 50      |             | 50    |             | 50            | 50                | 50    |                   |
| 40             |               | 40      |             | 40    |             | 40            | 40                | 40    |                   |
| 30             |               | 30      |             | 30    |             | 30            | 30                | 30    |                   |
| 20             |               | 20      |             | 20    |             | 20            | 20                | 20    |                   |
| 10             |               | 10      |             | 10    |             | 10            | 10                | 10    |                   |
| 0              |               | 0       |             | 0     |             | 0             | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
Period
|     |        |       | Unconditional Optimal Consumption |     |          |            |  Consumption Choice |     |     |
| --- | ------ | ----- | --------------------------------- | --- | -------- | ---------- | ------------------- | --- | --- |
|     | Figure | F.15: | Pos                               | IR  | No Calc, | Repetition | 1 (Session          |     | 2)  |
Pos IR Calc (Repetition 3)
|                | ID 25         |         | ID 29       |       | ID 33       | ID 37         | ID 41             |       | ID 45             |
| -------------- | ------------- | ------- | ----------- | ----- | ----------- | ------------- | ----------------- | ----- | ----------------- |
| 50             |               | 50      |             | 50    |             | 50            | 50                | 50    |                   |
| 40             |               | 40      |             | 40    |             | 40            | 40                | 40    |                   |
| 30             |               | 30      |             | 30    |             | 30            | 30                | 30    |                   |
| 20             |               | 20      |             | 20    |             | 20            | 20                | 20    |                   |
| 10             |               | 10      |             | 10    |             | 10            | 10                | 10    |                   |
| 0              |               | 0       |             | 0     |             | 0             | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 26         |         | ID 30       |       | ID 34       | ID 38         | ID 42             |       | ID 46             |
| 50             |               | 50      |             | 50    |             | 50            | 50                | 50    |                   |
| 40             |               | 40      |             | 40    |             | 40            | 40                | 40    |                   |
| 30             |               | 30      |             | 30    |             | 30            | 30                | 30    |                   |
| noitpmusnoC 20 |               | 20      |             | 20    |             | 20            | 20                | 20    |                   |
| 10             |               | 10      |             | 10    |             | 10            | 10                | 10    |                   |
| 0              |               | 0       |             | 0     |             | 0             | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 27         |         | ID 31       |       | ID 35       | ID 39         | ID 43             |       | 47                |
| 50             |               | 50      |             | 50    |             | 50            | 50                | 50    |                   |
| 40             |               | 40      |             | 40    |             | 40            | 40                | 40    |                   |
| 30             |               | 30      |             | 30    |             | 30            | 30                | 30    |                   |
| 20             |               | 20      |             | 20    |             | 20            | 20                | 20    |                   |
| 10             |               | 10      |             | 10    |             | 10            | 10                | 10    |                   |
| 0              |               | 0       |             | 0     |             | 0             | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 28         |         | ID 32       |       | ID 36       | ID 40         | ID 44             |       | 48                |
| 50             |               | 50      |             | 50    |             | 50            | 50                | 50    |                   |
| 40             |               | 40      |             | 40    |             | 40            | 40                | 40    |                   |
| 30             |               | 30      |             | 30    |             | 30            | 30                | 30    |                   |
| 20             |               | 20      |             | 20    |             | 20            | 20                | 20    |                   |
| 10             |               | 10      |             | 10    |             | 10            | 10                | 10    |                   |
| 0              |               | 0       |             | 0     |             | 0             | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
Period
|     |        |       | Unconditional Optimal Consumption |     |       |            |  Consumption Choice |     |     |
| --- | ------ | ----- | --------------------------------- | --- | ----- | ---------- | ------------------- | --- | --- |
|     | Figure | F.16: | Pos                               | IR  | Calc, | Repetition | 3 (Session          | 2)  |     |
72

FluctY No Calc (Repetition 1)
|                | ID 1          |         | ID 5        |       | ID 9        | ID 13           | ID 17             | ID 21                 |
| -------------- | ------------- | ------- | ----------- | ----- | ----------- | --------------- | ----------------- | --------------------- |
| 50             |               | 50      |             | 50    |             | 50              | 50                | 50                    |
| 40             |               | 40      |             | 40    |             | 40              | 40                | 40                    |
| 30             |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| 20             |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| 10             |               | 10      |             | 10    |             | 10              | 10                | 10                    |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 2          |         | ID 6        |       | ID 10       | ID 14           | ID 18             | ID 22                 |
| 50             |               | 50      |             | 50    |             | 50              | 50                | 50                    |
| 40             |               | 40      |             | 40    |             | 40              | 40                | 40                    |
| 30             |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| 20             |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| noitpmusnoC 10 |               | 10      |             | 10    |             | 10              | 10                | 10                    |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 3          |         | ID 7        |       | ID 11       | ID 15           | ID 19             |                       |
| 50             |               | 50      |             | 50    |             | 50              | 50                |                       |
| 40             |               | 40      |             | 40    |             | 40              | 40                |                       |
| 30             |               | 30      |             | 30    |             | 30              | 30                |                       |
| 20             |               | 20      |             | 20    |             | 20              | 20                |                       |
| 10             |               | 10      |             | 10    |             | 10              | 10                |                       |
| 0              |               | 0       |             | 0     |             | 0               | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
|                | ID 4          |         | ID 8        |       | ID 12       | ID 16           | ID 20             |                       |
| 50             |               | 50      |             | 50    |             | 50              | 50                |                       |
| 40             |               | 40      |             | 40    |             | 40              | 40                |                       |
| 30             |               | 30      |             | 30    |             | 30              | 30                |                       |
| 20             |               | 20      |             | 20    |             | 20              | 20                |                       |
| 10             |               | 10      |             | 10    |             | 10              | 10                |                       |
| 0              |               | 0       |             | 0     |             | 0               | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
Period
|     |        |       | Unconditional Optimal Consumption |     |          |            |  Consumption Choice |     |
| --- | ------ | ----- | --------------------------------- | --- | -------- | ---------- | ------------------- | --- |
|     | Figure | F.17: | FluctY                            |     | No Calc, | Repetition | 1 (Session          | 1)  |
FluctY No Calc (Repetition 3)
|                | ID 1          |         | ID 5        |       | ID 9        | ID 13           | ID 17             | ID 21                 |
| -------------- | ------------- | ------- | ----------- | ----- | ----------- | --------------- | ----------------- | --------------------- |
| 50             |               | 50      |             | 50    |             | 50              | 50                | 50                    |
| 40             |               | 40      |             | 40    |             | 40              | 40                | 40                    |
| 30             |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| 20             |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| 10             |               | 10      |             | 10    |             | 10              | 10                | 10                    |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 2          |         | ID 6        |       | ID 10       | ID 14           | ID 18             | ID 22                 |
| 50             |               | 50      |             | 50    |             | 50              | 50                | 50                    |
| 40             |               | 40      |             | 40    |             | 40              | 40                | 40                    |
| 30             |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| noitpmusnoC 20 |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| 10             |               | 10      |             | 10    |             | 10              | 10                | 10                    |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 3          |         | ID 7        |       | ID 11       | ID 15           | ID 19             |                       |
| 50             |               | 50      |             | 50    |             | 50              | 50                |                       |
| 40             |               | 40      |             | 40    |             | 40              | 40                |                       |
| 30             |               | 30      |             | 30    |             | 30              | 30                |                       |
| 20             |               | 20      |             | 20    |             | 20              | 20                |                       |
| 10             |               | 10      |             | 10    |             | 10              | 10                |                       |
| 0              |               | 0       |             | 0     |             | 0               | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
|                | ID 4          |         | ID 8        |       | ID 12       | ID 16           | ID 20             |                       |
| 50             |               | 50      |             | 50    |             | 50              | 50                |                       |
| 40             |               | 40      |             | 40    |             | 40              | 40                |                       |
| 30             |               | 30      |             | 30    |             | 30              | 30                |                       |
| 20             |               | 20      |             | 20    |             | 20              | 20                |                       |
| 10             |               | 10      |             | 10    |             | 10              | 10                |                       |
| 0              |               | 0       |             | 0     |             | 0               | 0                 |                       |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9                   |
Period
|     |        |       | Unconditional Optimal Consumption |     |          |            |  Consumption Choice |     |
| --- | ------ | ----- | --------------------------------- | --- | -------- | ---------- | ------------------- | --- |
|     | Figure | F.18: | FluctY                            |     | No Calc, | Repetition | 3 (Session          | 1)  |
73

FluctY No Calc (Repetition 1)
|                | ID 23         |         | ID 27       |       | ID 31       | ID 35           | ID 39             | ID 43                 |
| -------------- | ------------- | ------- | ----------- | ----- | ----------- | --------------- | ----------------- | --------------------- |
| 50             |               | 50      |             | 50    |             | 50              | 50                | 50                    |
| 40             |               | 40      |             | 40    |             | 40              | 40                | 40                    |
| 30             |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| 20             |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| 10             |               | 10      |             | 10    |             | 10              | 10                | 10                    |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 24         |         | ID 28       |       | ID 32       | ID 36           | ID 40             | ID 44                 |
| 50             |               | 50      |             | 50    |             | 50              | 50                | 50                    |
| 40             |               | 40      |             | 40    |             | 40              | 40                | 40                    |
| 30             |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| 20             |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| noitpmusnoC 10 |               | 10      |             | 10    |             | 10              | 10                | 10                    |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 25         |         | ID 29       |       | ID 33       | ID 37           | ID 41             | ID 45                 |
| 50             |               | 50      |             | 50    |             | 50              | 50                | 50                    |
| 40             |               | 40      |             | 40    |             | 40              | 40                | 40                    |
| 30             |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| 20             |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| 10             |               | 10      |             | 10    |             | 10              | 10                | 10                    |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 26         |         | ID 30       |       | ID 34       | ID 38           | ID 42             | ID 46                 |
| 50             |               | 50      |             | 50    |             | 50              | 50                | 50                    |
| 40             |               | 40      |             | 40    |             | 40              | 40                | 40                    |
| 30             |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| 20             |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| 10             |               | 10      |             | 10    |             | 10              | 10                | 10                    |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
Period
|     |        |       | Unconditional Optimal Consumption |     |          |            |  Consumption Choice |     |
| --- | ------ | ----- | --------------------------------- | --- | -------- | ---------- | ------------------- | --- |
|     | Figure | F.19: | FluctY                            |     | No Calc, | Repetition | 1 (Session          | 2)  |
FluctY No Calc (Repetition 3)
|                | ID 23         |         | ID 27       |       | ID 31       | ID 35           | ID 39             | ID 43                 |
| -------------- | ------------- | ------- | ----------- | ----- | ----------- | --------------- | ----------------- | --------------------- |
| 50             |               | 50      |             | 50    |             | 50              | 50                | 50                    |
| 40             |               | 40      |             | 40    |             | 40              | 40                | 40                    |
| 30             |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| 20             |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| 10             |               | 10      |             | 10    |             | 10              | 10                | 10                    |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 24         |         | ID 28       |       | ID 32       | ID 36           | ID 40             | ID 44                 |
| 50             |               | 50      |             | 50    |             | 50              | 50                | 50                    |
| 40             |               | 40      |             | 40    |             | 40              | 40                | 40                    |
| 30             |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| noitpmusnoC 20 |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| 10             |               | 10      |             | 10    |             | 10              | 10                | 10                    |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 25         |         | ID 29       |       | ID 33       | ID 37           | ID 41             | ID 45                 |
| 50             |               | 50      |             | 50    |             | 50              | 50                | 50                    |
| 40             |               | 40      |             | 40    |             | 40              | 40                | 40                    |
| 30             |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| 20             |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| 10             |               | 10      |             | 10    |             | 10              | 10                | 10                    |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                | ID 26         |         | ID 30       |       | ID 34       | ID 38           | ID 42             | ID 46                 |
| 50             |               | 50      |             | 50    |             | 50              | 50                | 50                    |
| 40             |               | 40      |             | 40    |             | 40              | 40                | 40                    |
| 30             |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| 20             |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| 10             |               | 10      |             | 10    |             | 10              | 10                | 10                    |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
Period
|     |        |       | Unconditional Optimal Consumption |     |          |            |  Consumption Choice |     |
| --- | ------ | ----- | --------------------------------- | --- | -------- | ---------- | ------------------- | --- |
|     | Figure | F.20: | FluctY                            |     | No Calc, | Repetition | 3 (Session          | 2)  |
74

FluctY Calc (Repetition 1)
|             | ID 1      | ID 5      | ID 9      | ID 13     |           | ID 17     | ID 21 | ID 25     |
| ----------- | --------- | --------- | --------- | --------- | --------- | --------- | ----- | --------- |
|             | 50        | 50        | 50        | 50        | 50        | 50        |       | 50        |
|             | 40        | 40        | 40        | 40        | 40        | 40        |       | 40        |
|             | 30        | 30        | 30        | 30        | 30        | 30        |       | 30        |
|             | 20        | 20        | 20        | 20        | 20        | 20        |       | 20        |
|             | 10        | 10        | 10        | 10        | 10        | 10        |       | 10        |
|             | 0         | 0         | 0         | 0         | 0         | 0         |       | 0         |
|             | 123456789 | 123456789 | 123456789 | 123456789 | 123456789 | 123456789 |       | 123456789 |
|             | ID 2      | ID 6      | ID 10     | ID 14     |           | ID 18     | ID 22 | ID 26     |
|             | 50        | 50        | 50        | 50        | 50        | 50        |       | 50        |
|             | 40        | 40        | 40        | 40        | 40        | 40        |       | 40        |
|             | 30        | 30        | 30        | 30        | 30        | 30        |       | 30        |
|             | 20        | 20        | 20        | 20        | 20        | 20        |       | 20        |
| noitpmusnoC | 10        | 10        | 10        | 10        | 10        | 10        |       | 10        |
|             | 0         | 0         | 0         | 0         | 0         | 0         |       | 0         |
|             | 123456789 | 123456789 | 123456789 | 123456789 | 123456789 | 123456789 |       | 123456789 |
|             | ID 3      | ID 7      | ID 11     | ID 15     |           | ID 19     | ID 23 | ID 27     |
|             | 50        | 50        | 50        | 50        | 50        | 50        |       | 50        |
|             | 40        | 40        | 40        | 40        | 40        | 40        |       | 40        |
|             | 30        | 30        | 30        | 30        | 30        | 30        |       | 30        |
|             | 20        | 20        | 20        | 20        | 20        | 20        |       | 20        |
|             | 10        | 10        | 10        | 10        | 10        | 10        |       | 10        |
|             | 0         | 0         | 0         | 0         | 0         | 0         |       | 0         |
|             | 123456789 | 123456789 | 123456789 | 123456789 | 123456789 | 123456789 |       | 123456789 |
|             | ID 4      | ID 8      | ID 12     | ID 16     |           | ID 20     | ID 24 | ID 28     |
|             | 50        | 50        | 50        | 50        | 50        | 50        |       | 50        |
|             | 40        | 40        | 40        | 40        | 40        | 40        |       | 40        |
|             | 30        | 30        | 30        | 30        | 30        | 30        |       | 30        |
|             | 20        | 20        | 20        | 20        | 20        | 20        |       | 20        |
|             | 10        | 10        | 10        | 10        | 10        | 10        |       | 10        |
|             | 0         | 0         | 0         | 0         | 0         | 0         |       | 0         |
|             | 123456789 | 123456789 | 123456789 | 123456789 | 123456789 | 123456789 |       | 123456789 |
Period
|     |     |              | Unconditional Optimal Consumption |                  |     |  Consumption Choice |     |     |
| --- | --- | ------------ | --------------------------------- | ---------------- | --- | ------------------- | --- | --- |
|     |     | Figure F.21: | FluctY                            | Calc, Repetition |     | 1 (Session          | 1)  |     |
FluctY Calc (Repetition 3)
|             | ID 1      | ID 5      | ID 9      | ID 13     |           | ID 17     | ID 21 | ID 25     |
| ----------- | --------- | --------- | --------- | --------- | --------- | --------- | ----- | --------- |
|             | 50        | 50        | 50        | 50        | 50        | 50        |       | 50        |
|             | 40        | 40        | 40        | 40        | 40        | 40        |       | 40        |
|             | 30        | 30        | 30        | 30        | 30        | 30        |       | 30        |
|             | 20        | 20        | 20        | 20        | 20        | 20        |       | 20        |
|             | 10        | 10        | 10        | 10        | 10        | 10        |       | 10        |
|             | 0         | 0         | 0         | 0         | 0         | 0         |       | 0         |
|             | 123456789 | 123456789 | 123456789 | 123456789 | 123456789 | 123456789 |       | 123456789 |
|             | ID 2      | ID 6      | ID 10     | ID 14     |           | ID 18     | ID 22 | ID 26     |
|             | 50        | 50        | 50        | 50        | 50        | 50        |       | 50        |
|             | 40        | 40        | 40        | 40        | 40        | 40        |       | 40        |
|             | 30        | 30        | 30        | 30        | 30        | 30        |       | 30        |
| noitpmusnoC | 20        | 20        | 20        | 20        | 20        | 20        |       | 20        |
|             | 10        | 10        | 10        | 10        | 10        | 10        |       | 10        |
|             | 0         | 0         | 0         | 0         | 0         | 0         |       | 0         |
|             | 123456789 | 123456789 | 123456789 | 123456789 | 123456789 | 123456789 |       | 123456789 |
|             | ID 3      | ID 7      | ID 11     | ID 15     |           | ID 19     | ID 23 | ID 27     |
|             | 50        | 50        | 50        | 50        | 50        | 50        |       | 50        |
|             | 40        | 40        | 40        | 40        | 40        | 40        |       | 40        |
|             | 30        | 30        | 30        | 30        | 30        | 30        |       | 30        |
|             | 20        | 20        | 20        | 20        | 20        | 20        |       | 20        |
|             | 10        | 10        | 10        | 10        | 10        | 10        |       | 10        |
|             | 0         | 0         | 0         | 0         | 0         | 0         |       | 0         |
|             | 123456789 | 123456789 | 123456789 | 123456789 | 123456789 | 123456789 |       | 123456789 |
|             | ID 4      | ID 8      | ID 12     | ID 16     |           | ID 20     | ID 24 | ID 28     |
|             | 50        | 50        | 50        | 50        | 50        | 50        |       | 50        |
|             | 40        | 40        | 40        | 40        | 40        | 40        |       | 40        |
|             | 30        | 30        | 30        | 30        | 30        | 30        |       | 30        |
|             | 20        | 20        | 20        | 20        | 20        | 20        |       | 20        |
|             | 10        | 10        | 10        | 10        | 10        | 10        |       | 10        |
|             | 0         | 0         | 0         | 0         | 0         | 0         |       | 0         |
|             | 123456789 | 123456789 | 123456789 | 123456789 | 123456789 | 123456789 |       | 123456789 |
Period
|     |     |              | Unconditional Optimal Consumption |                  |     |  Consumption Choice |     |     |
| --- | --- | ------------ | --------------------------------- | ---------------- | --- | ------------------- | --- | --- |
|     |     | Figure F.22: | FluctY                            | Calc, Repetition |     | 3 (Session          | 1)  |     |
75

FluctY Calc (Repetition 1)
|                | ID 29         |     | ID 33         |     | ID 37         |     | ID 41         |     | ID 45             |
| -------------- | ------------- | --- | ------------- | --- | ------------- | --- | ------------- | --- | ----------------- |
| 50             |               | 50  |               | 50  |               | 50  |               | 50  |                   |
| 40             |               | 40  |               | 40  |               | 40  |               | 40  |                   |
| 30             |               | 30  |               | 30  |               | 30  |               | 30  |                   |
| 20             |               | 20  |               | 20  |               | 20  |               | 20  |                   |
| 10             |               | 10  |               | 10  |               | 10  |               | 10  |                   |
| 0              |               | 0   |               | 0   |               | 0   |               | 0   |                   |
|                | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 30         |     | ID 34         |     | ID 38         |     | ID 42         |     | ID 46             |
| 50             |               | 50  |               | 50  |               | 50  |               | 50  |                   |
| 40             |               | 40  |               | 40  |               | 40  |               | 40  |                   |
| 30             |               | 30  |               | 30  |               | 30  |               | 30  |                   |
| 20             |               | 20  |               | 20  |               | 20  |               | 20  |                   |
| noitpmusnoC 10 |               | 10  |               | 10  |               | 10  |               | 10  |                   |
| 0              |               | 0   |               | 0   |               | 0   |               | 0   |                   |
|                | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 31         |     | ID 35         |     | ID 39         |     | ID 43         |     | 47                |
| 50             |               | 50  |               | 50  |               | 50  |               | 50  |                   |
| 40             |               | 40  |               | 40  |               | 40  |               | 40  |                   |
| 30             |               | 30  |               | 30  |               | 30  |               | 30  |                   |
| 20             |               | 20  |               | 20  |               | 20  |               | 20  |                   |
| 10             |               | 10  |               | 10  |               | 10  |               | 10  |                   |
| 0              |               | 0   |               | 0   |               | 0   |               | 0   |                   |
|                | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 32         |     | ID 36         |     | ID 40         |     | ID 44         |     | 48                |
| 50             |               | 50  |               | 50  |               | 50  |               | 50  |                   |
| 40             |               | 40  |               | 40  |               | 40  |               | 40  |                   |
| 30             |               | 30  |               | 30  |               | 30  |               | 30  |                   |
| 20             |               | 20  |               | 20  |               | 20  |               | 20  |                   |
| 10             |               | 10  |               | 10  |               | 10  |               | 10  |                   |
| 0              |               | 0   |               | 0   |               | 0   |               | 0   |                   |
|                | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 8 9 |
Period
|     |        |       | Unconditional Optimal Consumption |     |                  |     |  Consumption Choice |     |     |
| --- | ------ | ----- | --------------------------------- | --- | ---------------- | --- | ------------------- | --- | --- |
|     | Figure | F.23: | FluctY                            | No  | Calc, Repetition |     | 1 (Session          |     | 2)  |
FluctY Calc (Repetition 3)
|                | ID 29         |     | ID 33         |     | ID 37         |     | ID 41         |     | ID 45             |
| -------------- | ------------- | --- | ------------- | --- | ------------- | --- | ------------- | --- | ----------------- |
| 50             |               | 50  |               | 50  |               | 50  |               | 50  |                   |
| 40             |               | 40  |               | 40  |               | 40  |               | 40  |                   |
| 30             |               | 30  |               | 30  |               | 30  |               | 30  |                   |
| 20             |               | 20  |               | 20  |               | 20  |               | 20  |                   |
| 10             |               | 10  |               | 10  |               | 10  |               | 10  |                   |
| 0              |               | 0   |               | 0   |               | 0   |               | 0   |                   |
|                | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 30         |     | ID 34         |     | ID 38         |     | ID 42         |     | ID 46             |
| 50             |               | 50  |               | 50  |               | 50  |               | 50  |                   |
| 40             |               | 40  |               | 40  |               | 40  |               | 40  |                   |
| 30             |               | 30  |               | 30  |               | 30  |               | 30  |                   |
| noitpmusnoC 20 |               | 20  |               | 20  |               | 20  |               | 20  |                   |
| 10             |               | 10  |               | 10  |               | 10  |               | 10  |                   |
| 0              |               | 0   |               | 0   |               | 0   |               | 0   |                   |
|                | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 31         |     | ID 35         |     | ID 39         |     | ID 43         |     | 47                |
| 50             |               | 50  |               | 50  |               | 50  |               | 50  |                   |
| 40             |               | 40  |               | 40  |               | 40  |               | 40  |                   |
| 30             |               | 30  |               | 30  |               | 30  |               | 30  |                   |
| 20             |               | 20  |               | 20  |               | 20  |               | 20  |                   |
| 10             |               | 10  |               | 10  |               | 10  |               | 10  |                   |
| 0              |               | 0   |               | 0   |               | 0   |               | 0   |                   |
|                | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 32         |     | ID 36         |     | ID 40         |     | ID 44         |     | 48                |
| 50             |               | 50  |               | 50  |               | 50  |               | 50  |                   |
| 40             |               | 40  |               | 40  |               | 40  |               | 40  |                   |
| 30             |               | 30  |               | 30  |               | 30  |               | 30  |                   |
| 20             |               | 20  |               | 20  |               | 20  |               | 20  |                   |
| 10             |               | 10  |               | 10  |               | 10  |               | 10  |                   |
| 0              |               | 0   |               | 0   |               | 0   |               | 0   |                   |
|                | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 | 8 9 | 1 2 3 4 5 6 7 8 9 |
Period
|     |        |       | Unconditional Optimal Consumption |       |            |     |  Consumption Choice |     |     |
| --- | ------ | ----- | --------------------------------- | ----- | ---------- | --- | ------------------- | --- | --- |
|     | Figure | F.24: | FluctY                            | Calc, | Repetition |     | 3 (Session          | 2)  |     |
76

FluctP No Calc (Repetition 1)
|                   | ID 1          |         | ID 5        |       | ID 9        | ID 13           | ID 17             | ID 21                 |
| ----------------- | ------------- | ------- | ----------- | ----- | ----------- | --------------- | ----------------- | --------------------- |
| 70                |               | 70      |             | 70    |             | 70              | 70                | 70                    |
| 60                |               | 60      |             | 60    |             | 60              | 60                | 60                    |
| 50 40             |               | 50 40   |             | 50 40 |             | 50 40           | 50 40             | 50 40                 |
| 30                |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| 20                |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| 10                |               | 10      |             | 10    |             | 10              | 10                | 10                    |
| 0                 |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                   | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                   | ID 2          |         | ID 6        |       | ID 10       | ID 14           | ID 18             | ID 22                 |
| 70                |               | 70      |             | 70    |             | 70              | 70                | 70                    |
| 60 50             |               | 60 50   |             | 60 50 |             | 60 50           | 60 50             | 60 50                 |
| 40                |               | 40      |             | 40    |             | 40              | 40                | 40                    |
| 30                |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| noitpmusnoC 20 10 |               | 20 10   |             | 20 10 |             | 20 10           | 20 10             | 20 10                 |
| 0                 |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                   | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                   | ID 3          |         | ID 7        |       | ID 11       | ID 15           | ID 19             | ID 23                 |
| 70                |               | 70      |             | 70    |             | 70              | 70                | 70                    |
| 60                |               | 60      |             | 60    |             | 60              | 60                | 60                    |
| 50                |               | 50      |             | 50    |             | 50              | 50                | 50                    |
| 40 30             |               | 40 30   |             | 40 30 |             | 40 30           | 40 30             | 40 30                 |
| 20                |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| 10                |               | 10      |             | 10    |             | 10              | 10                | 10                    |
| 0                 |               | 0       |             | 0     |             | 0               | 0                 | 0                     |
|                   | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                   | ID 4          |         | ID 8        |       | ID 12       | ID 16           | ID 20             | ID 24                 |
| 70                |               | 70      |             | 70    |             | 70              | 70                | 70                    |
| 60 50             |               | 60 50   |             | 60 50 |             | 60 50           | 60 50             | 60 50                 |
| 40                |               | 40      |             | 40    |             | 40              | 40                | 40                    |
| 30                |               | 30      |             | 30    |             | 30              | 30                | 30                    |
| 20                |               | 20      |             | 20    |             | 20              | 20                | 20                    |
| 10 0              |               | 10 0    |             | 10 0  |             | 10 0            | 10 0              | 10 0                  |
|                   | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
Period
|     |        |       | Unconditional Optimal Consumption |     |          |            |  Consumption Choice |     |
| --- | ------ | ----- | --------------------------------- | --- | -------- | ---------- | ------------------- | --- |
|     | Figure | F.25: | FluctP                            |     | No Calc, | Repetition | 1 (Session          | 1)  |
FluctP No Calc (Repetition 3)
|                             | ID 1          |                 | ID 5        |                 | ID 9        | ID 13           | ID 17             | ID 21                 |
| --------------------------- | ------------- | --------------- | ----------- | --------------- | ----------- | --------------- | ----------------- | --------------------- |
| 1234567 0000000             |               | 1234567 0000000 |             | 1234567 0000000 |             | 1234567 0000000 | 1234567 0000000   | 1234567 0000000       |
| 0                           |               | 0               |             | 0               |             | 0               | 0                 | 0                     |
|                             | 1 2 3 4 5 6 7 | 8 9 1 2         | 3 4 5 6 7 8 | 9 1 2           | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                             | ID 2          |                 | ID 6        |                 | ID 10       | ID 14           | ID 18             | ID 22                 |
| noitpmusnoC 1234567 0000000 |               | 1234567 0000000 |             | 1234567 0000000 |             | 1234567 0000000 | 1234567 0000000   | 1234567 0000000       |
| 0                           |               | 0               |             | 0               |             | 0               | 0                 | 0                     |
|                             | 1 2 3 4 5 6 7 | 8 9 1 2         | 3 4 5 6 7 8 | 9 1 2           | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                             | ID 3          |                 | ID 7        |                 | ID 11       | ID 15           | ID 19             | ID 23                 |
| 1234567 0000000             |               | 1234567 0000000 |             | 1234567 0000000 |             | 1234567 0000000 | 1234567 0000000   | 1234567 0000000       |
| 0                           |               | 0               |             | 0               |             | 0               | 0                 | 0                     |
|                             | 1 2 3 4 5 6 7 | 8 9 1 2         | 3 4 5 6 7 8 | 9 1 2           | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
|                             | ID 4          |                 | ID 8        |                 | ID 12       | ID 16           | ID 20             | ID 24                 |
| 1234567 0000000             |               | 1234567 0000000 |             | 1234567 0000000 |             | 1234567 0000000 | 1234567 0000000   | 1234567 0000000       |
| 0                           |               | 0               |             | 0               |             | 0               | 0                 | 0                     |
|                             | 1 2 3 4 5 6 7 | 8 9 1 2         | 3 4 5 6 7 8 | 9 1 2           | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 8 9 |
Period
|     |        |       | Unconditional Optimal Consumption |     |          |            |  Consumption Choice |     |
| --- | ------ | ----- | --------------------------------- | --- | -------- | ---------- | ------------------- | --- |
|     | Figure | F.26: | FluctP                            |     | No Calc, | Repetition | 3 (Session          | 1)  |
77

FluctP No Calc (Repetition 1)
|                 | ID 25         |                 | ID 29       |                 | ID 33       | ID 37           | ID 41             |                 | ID 45             |
| --------------- | ------------- | --------------- | ----------- | --------------- | ----------- | --------------- | ----------------- | --------------- | ----------------- |
| 1234567 0000000 |               | 1234567 0000000 |             | 1234567 0000000 |             | 1234567 0000000 | 1234567 0000000   | 1234567 0000000 |                   |
| 0               |               | 0               |             | 0               |             | 0               | 0                 | 0               |                   |
|                 | 1 2 3 4 5 6 7 | 8 9 1 2         | 3 4 5 6 7 8 | 9 1 2           | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9             | 1 2 3 4 5 6 7 8 9 |
|                 | ID 26         |                 | ID 30       |                 | ID 34       | ID 38           | ID 42             |                 | ID 46             |
| 1234567 0000000 |               | 1234567 0000000 |             | 1234567 0000000 |             | 1234567 0000000 | 1234567 0000000   | 1234567 0000000 |                   |
noitpmusnoC
| 0               |               | 0               |             | 0               |             | 0               | 0                 | 0               |                   |
| --------------- | ------------- | --------------- | ----------- | --------------- | ----------- | --------------- | ----------------- | --------------- | ----------------- |
|                 | 1 2 3 4 5 6 7 | 8 9 1 2         | 3 4 5 6 7 8 | 9 1 2           | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9             | 1 2 3 4 5 6 7 8 9 |
|                 | ID 27         |                 | ID 31       |                 | ID 35       | ID 39           | ID 43             |                 | 47                |
| 1234567 0000000 |               | 1234567 0000000 |             | 1234567 0000000 |             | 1234567 0000000 | 1234567 0000000   | 1234567 0000000 |                   |
| 0               |               | 0               |             | 0               |             | 0               | 0                 | 0               |                   |
|                 | 1 2 3 4 5 6 7 | 8 9 1 2         | 3 4 5 6 7 8 | 9 1 2           | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9             | 1 2 3 4 5 6 7 8 9 |
|                 | ID 28         |                 | ID 32       |                 | ID 36       | ID 40           | ID 44             |                 | 48                |
| 1234567 0000000 |               | 1234567 0000000 |             | 1234567 0000000 |             | 1234567 0000000 | 1234567 0000000   | 1234567 0000000 |                   |
| 0               |               | 0               |             | 0               |             | 0               | 0                 | 0               |                   |
|                 | 1 2 3 4 5 6 7 | 8 9 1 2         | 3 4 5 6 7 8 | 9 1 2           | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9             | 1 2 3 4 5 6 7 8 9 |
Period
|     |        |       | Unconditional Optimal Consumption |     |          |            |  Consumption Choice |     |     |
| --- | ------ | ----- | --------------------------------- | --- | -------- | ---------- | ------------------- | --- | --- |
|     | Figure | F.27: | FluctP                            |     | No Calc, | Repetition | 1 (Session          | 2)  |     |
FluctP No Calc (Repetition 3)
|                | ID 25         |         | ID 29       |       | ID 33       | ID 37           | ID 41             |       | ID 45             |
| -------------- | ------------- | ------- | ----------- | ----- | ----------- | --------------- | ----------------- | ----- | ----------------- |
| 70             |               | 70      |             | 70    |             | 70              | 70                | 70    |                   |
| 60             |               | 60      |             | 60    |             | 60              | 60                | 60    |                   |
| 50 40          |               | 50 40   |             | 50 40 |             | 50 40           | 50 40             | 50 40 |                   |
| 30             |               | 30      |             | 30    |             | 30              | 30                | 30    |                   |
| 20             |               | 20      |             | 20    |             | 20              | 20                | 20    |                   |
| 10             |               | 10      |             | 10    |             | 10              | 10                | 10    |                   |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9   | 1 2 3 4 5 6 7 8 9 |
|                | ID 26         |         | ID 30       |       | ID 34       | ID 38           | ID 42             |       | ID 46             |
| 70 60          |               | 70 60   |             | 70 60 |             | 70 60           | 70 60             | 70 60 |                   |
| 50             |               | 50      |             | 50    |             | 50              | 50                | 50    |                   |
| 40             |               | 40      |             | 40    |             | 40              | 40                | 40    |                   |
| noitpmusnoC 30 |               | 30      |             | 30    |             | 30              | 30                | 30    |                   |
| 20 10          |               | 20 10   |             | 20 10 |             | 20 10           | 20 10             | 20 10 |                   |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9   | 1 2 3 4 5 6 7 8 9 |
|                | ID 27         |         | ID 31       |       | ID 35       | ID 39           | ID 43             |       | 47                |
| 70             |               | 70      |             | 70    |             | 70              | 70                | 70    |                   |
| 60             |               | 60      |             | 60    |             | 60              | 60                | 60    |                   |
| 50             |               | 50      |             | 50    |             | 50              | 50                | 50    |                   |
| 40 30          |               | 40 30   |             | 40 30 |             | 40 30           | 40 30             | 40 30 |                   |
| 20             |               | 20      |             | 20    |             | 20              | 20                | 20    |                   |
| 10             |               | 10      |             | 10    |             | 10              | 10                | 10    |                   |
| 0              |               | 0       |             | 0     |             | 0               | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9   | 1 2 3 4 5 6 7 8 9 |
|                | ID 28         |         | ID 32       |       | ID 36       | ID 40           | ID 44             |       | 48                |
| 70             |               | 70      |             | 70    |             | 70              | 70                | 70    |                   |
| 60 50          |               | 60 50   |             | 60 50 |             | 60 50           | 60 50             | 60 50 |                   |
| 40             |               | 40      |             | 40    |             | 40              | 40                | 40    |                   |
| 30             |               | 30      |             | 30    |             | 30              | 30                | 30    |                   |
| 20             |               | 20      |             | 20    |             | 20              | 20                | 20    |                   |
| 10 0           |               | 10 0    |             | 10 0  |             | 10 0            | 10 0              | 10 0  |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 7 | 8 9 1 2 3 4 5 6 7 | 8 9   | 1 2 3 4 5 6 7 8 9 |
Period
|     |        |       | Unconditional Optimal Consumption |     |          |            |  Consumption Choice |     |     |
| --- | ------ | ----- | --------------------------------- | --- | -------- | ---------- | ------------------- | --- | --- |
|     | Figure | F.28: | FluctP                            |     | No Calc, | Repetition | 3 (Session          | 2)  |     |
78

FluctP Calc (Repetition 1)
|                   | ID 1          | ID 5        |           | ID 9        | ID 13             | ID 17             |       | ID 21             |
| ----------------- | ------------- | ----------- | --------- | ----------- | ----------------- | ----------------- | ----- | ----------------- |
| 70                |               | 70          | 70        |             | 70                | 70                | 70    |                   |
| 60                |               | 60          | 60        |             | 60                | 60                | 60    |                   |
| 50 40             |               | 50 40       | 50 40     |             | 50 40             | 50 40             | 50 40 |                   |
| 30                |               | 30          | 30        |             | 30                | 30                | 30    |                   |
| 20                |               | 20          | 20        |             | 20                | 20                | 20    |                   |
| 10                |               | 10          | 10        |             | 10                | 10                | 10    |                   |
| 0                 |               | 0           | 0         |             | 0                 | 0                 | 0     |                   |
|                   | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 | 5 6 7 8 9 | 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                   | ID 2          | ID 6        |           | ID 10       | ID 14             | ID 18             |       | ID 22             |
| 70                |               | 70          | 70        |             | 70                | 70                | 70    |                   |
| 60 50             |               | 60 50       | 60 50     |             | 60 50             | 60 50             | 60 50 |                   |
| 40                |               | 40          | 40        |             | 40                | 40                | 40    |                   |
| 30                |               | 30          | 30        |             | 30                | 30                | 30    |                   |
| noitpmusnoC 20 10 |               | 20 10       | 20 10     |             | 20 10             | 20 10             | 20 10 |                   |
| 0                 |               | 0           | 0         |             | 0                 | 0                 | 0     |                   |
|                   | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 | 5 6 7 8 9 | 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                   | ID 3          | ID 7        |           | ID 11       | ID 15             | ID 19             |       | ID 23             |
| 70                |               | 70          | 70        |             | 70                | 70                | 70    |                   |
| 60                |               | 60          | 60        |             | 60                | 60                | 60    |                   |
| 50                |               | 50          | 50        |             | 50                | 50                | 50    |                   |
| 40 30             |               | 40 30       | 40 30     |             | 40 30             | 40 30             | 40 30 |                   |
| 20                |               | 20          | 20        |             | 20                | 20                | 20    |                   |
| 10                |               | 10          | 10        |             | 10                | 10                | 10    |                   |
| 0                 |               | 0           | 0         |             | 0                 | 0                 | 0     |                   |
|                   | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 | 5 6 7 8 9 | 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                   | ID 4          | ID 8        |           | ID 12       | ID 16             | ID 20             |       | ID 24             |
| 70                |               | 70          | 70        |             | 70                | 70                | 70    |                   |
| 60 50             |               | 60 50       | 60 50     |             | 60 50             | 60 50             | 60 50 |                   |
| 40                |               | 40          | 40        |             | 40                | 40                | 40    |                   |
| 30                |               | 30          | 30        |             | 30                | 30                | 30    |                   |
| 20                |               | 20          | 20        |             | 20                | 20                | 20    |                   |
| 10 0              |               | 10 0        | 10 0      |             | 10 0              | 10 0              | 10 0  |                   |
|                   | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 | 5 6 7 8 9 | 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
Period
|     |        |       | Unconditional Optimal Consumption |       |            |  Consumption Choice |     |     |
| --- | ------ | ----- | --------------------------------- | ----- | ---------- | ------------------- | --- | --- |
|     | Figure | F.29: | FluctP                            | Calc, | Repetition | 1 (Session          | 1)  |     |
FluctP Calc (Repetition 3)
|                | ID 1          | ID 5        |           | ID 9        | ID 13             | ID 17             |       | ID 21             |
| -------------- | ------------- | ----------- | --------- | ----------- | ----------------- | ----------------- | ----- | ----------------- |
| 70             |               | 70          | 70        |             | 70                | 70                | 70    |                   |
| 60             |               | 60          | 60        |             | 60                | 60                | 60    |                   |
| 50 40          |               | 50 40       | 50 40     |             | 50 40             | 50 40             | 50 40 |                   |
| 30             |               | 30          | 30        |             | 30                | 30                | 30    |                   |
| 20             |               | 20          | 20        |             | 20                | 20                | 20    |                   |
| 10             |               | 10          | 10        |             | 10                | 10                | 10    |                   |
| 0              |               | 0           | 0         |             | 0                 | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 | 5 6 7 8 9 | 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 2          | ID 6        |           | ID 10       | ID 14             | ID 18             |       | ID 22             |
| 70 60          |               | 70 60       | 70 60     |             | 70 60             | 70 60             | 70 60 |                   |
| 50             |               | 50          | 50        |             | 50                | 50                | 50    |                   |
| 40             |               | 40          | 40        |             | 40                | 40                | 40    |                   |
| noitpmusnoC 30 |               | 30          | 30        |             | 30                | 30                | 30    |                   |
| 20 10          |               | 20 10       | 20 10     |             | 20 10             | 20 10             | 20 10 |                   |
| 0              |               | 0           | 0         |             | 0                 | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 | 5 6 7 8 9 | 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 3          | ID 7        |           | ID 11       | ID 15             | ID 19             |       | ID 23             |
| 70             |               | 70          | 70        |             | 70                | 70                | 70    |                   |
| 60             |               | 60          | 60        |             | 60                | 60                | 60    |                   |
| 50             |               | 50          | 50        |             | 50                | 50                | 50    |                   |
| 40 30          |               | 40 30       | 40 30     |             | 40 30             | 40 30             | 40 30 |                   |
| 20             |               | 20          | 20        |             | 20                | 20                | 20    |                   |
| 10             |               | 10          | 10        |             | 10                | 10                | 10    |                   |
| 0              |               | 0           | 0         |             | 0                 | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 | 5 6 7 8 9 | 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 4          | ID 8        |           | ID 12       | ID 16             | ID 20             |       | ID 24             |
| 70             |               | 70          | 70        |             | 70                | 70                | 70    |                   |
| 60 50          |               | 60 50       | 60 50     |             | 60 50             | 60 50             | 60 50 |                   |
| 40             |               | 40          | 40        |             | 40                | 40                | 40    |                   |
| 30             |               | 30          | 30        |             | 30                | 30                | 30    |                   |
| 20             |               | 20          | 20        |             | 20                | 20                | 20    |                   |
| 10 0           |               | 10 0        | 10 0      |             | 10 0              | 10 0              | 10 0  |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 3 4 | 5 6 7 8 9 | 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
Period
|     |        |       | Unconditional Optimal Consumption |       |            |  Consumption Choice |     |     |
| --- | ------ | ----- | --------------------------------- | ----- | ---------- | ------------------- | --- | --- |
|     | Figure | F.30: | FluctP                            | Calc, | Repetition | 3 (Session          | 1)  |     |
79

FluctP Calc (Repetition 1)
|                   | ID 25         |         | ID 29       |       | ID 33       | ID 37         | ID 41             |       | ID 45             |
| ----------------- | ------------- | ------- | ----------- | ----- | ----------- | ------------- | ----------------- | ----- | ----------------- |
| 70                |               | 70      |             | 70    |             | 70            | 70                | 70    |                   |
| 60                |               | 60      |             | 60    |             | 60            | 60                | 60    |                   |
| 50 40             |               | 50 40   |             | 50 40 |             | 50 40         | 50 40             | 50 40 |                   |
| 30                |               | 30      |             | 30    |             | 30            | 30                | 30    |                   |
| 20                |               | 20      |             | 20    |             | 20            | 20                | 20    |                   |
| 10                |               | 10      |             | 10    |             | 10            | 10                | 10    |                   |
| 0                 |               | 0       |             | 0     |             | 0             | 0                 | 0     |                   |
|                   | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                   | ID 26         |         | ID 30       |       | ID 34       | ID 38         | ID 42             |       |                   |
| 70                |               | 70      |             | 70    |             | 70            | 70                |       |                   |
| 60 50             |               | 60 50   |             | 60 50 |             | 60 50         | 60 50             |       |                   |
| 40                |               | 40      |             | 40    |             | 40            | 40                |       |                   |
| 30                |               | 30      |             | 30    |             | 30            | 30                |       |                   |
| noitpmusnoC 20 10 |               | 20 10   |             | 20 10 |             | 20 10         | 20 10             |       |                   |
| 0                 |               | 0       |             | 0     |             | 0             | 0                 |       |                   |
|                   | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 |                   |
|                   | ID 27         |         | ID 31       |       | ID 35       | ID 39         | ID 43             |       |                   |
| 70                |               | 70      |             | 70    |             | 70            | 70                |       |                   |
| 60                |               | 60      |             | 60    |             | 60            | 60                |       |                   |
| 50                |               | 50      |             | 50    |             | 50            | 50                |       |                   |
| 40 30             |               | 40 30   |             | 40 30 |             | 40 30         | 40 30             |       |                   |
| 20                |               | 20      |             | 20    |             | 20            | 20                |       |                   |
| 10                |               | 10      |             | 10    |             | 10            | 10                |       |                   |
| 0                 |               | 0       |             | 0     |             | 0             | 0                 |       |                   |
|                   | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 |                   |
|                   | ID 28         |         | ID 32       |       | ID 36       | ID 40         | ID 44             |       |                   |
| 70                |               | 70      |             | 70    |             | 70            | 70                |       |                   |
| 60 50             |               | 60 50   |             | 60 50 |             | 60 50         | 60 50             |       |                   |
| 40                |               | 40      |             | 40    |             | 40            | 40                |       |                   |
| 30                |               | 30      |             | 30    |             | 30            | 30                |       |                   |
| 20                |               | 20      |             | 20    |             | 20            | 20                |       |                   |
| 10 0              |               | 10 0    |             | 10 0  |             | 10 0          | 10 0              |       |                   |
|                   | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 |                   |
Period
|     |        |       | Unconditional Optimal Consumption |     |          |            |  Consumption Choice |     |     |
| --- | ------ | ----- | --------------------------------- | --- | -------- | ---------- | ------------------- | --- | --- |
|     | Figure | F.31: | FluctP                            |     | No Calc, | Repetition | 1 (Session          |     | 2)  |
FluctP Calc (Repetition 3)
|                | ID 25         |         | ID 29       |       | ID 33       | ID 37         | ID 41             |       | ID 45             |
| -------------- | ------------- | ------- | ----------- | ----- | ----------- | ------------- | ----------------- | ----- | ----------------- |
| 70             |               | 70      |             | 70    |             | 70            | 70                | 70    |                   |
| 60             |               | 60      |             | 60    |             | 60            | 60                | 60    |                   |
| 50 40          |               | 50 40   |             | 50 40 |             | 50 40         | 50 40             | 50 40 |                   |
| 30             |               | 30      |             | 30    |             | 30            | 30                | 30    |                   |
| 20             |               | 20      |             | 20    |             | 20            | 20                | 20    |                   |
| 10             |               | 10      |             | 10    |             | 10            | 10                | 10    |                   |
| 0              |               | 0       |             | 0     |             | 0             | 0                 | 0     |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 | 1 2 3 4 5 6 7 8 9 |
|                | ID 26         |         | ID 30       |       | ID 34       | ID 38         | ID 42             |       |                   |
| 70 60          |               | 70 60   |             | 70 60 |             | 70 60         | 70 60             |       |                   |
| 50             |               | 50      |             | 50    |             | 50            | 50                |       |                   |
| 40             |               | 40      |             | 40    |             | 40            | 40                |       |                   |
| noitpmusnoC 30 |               | 30      |             | 30    |             | 30            | 30                |       |                   |
| 20 10          |               | 20 10   |             | 20 10 |             | 20 10         | 20 10             |       |                   |
| 0              |               | 0       |             | 0     |             | 0             | 0                 |       |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 |                   |
|                | ID 27         |         | ID 31       |       | ID 35       | ID 39         | ID 43             |       |                   |
| 70             |               | 70      |             | 70    |             | 70            | 70                |       |                   |
| 60             |               | 60      |             | 60    |             | 60            | 60                |       |                   |
| 50             |               | 50      |             | 50    |             | 50            | 50                |       |                   |
| 40 30          |               | 40 30   |             | 40 30 |             | 40 30         | 40 30             |       |                   |
| 20             |               | 20      |             | 20    |             | 20            | 20                |       |                   |
| 10             |               | 10      |             | 10    |             | 10            | 10                |       |                   |
| 0              |               | 0       |             | 0     |             | 0             | 0                 |       |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 |                   |
|                | ID 28         |         | ID 32       |       | ID 36       | ID 40         | ID 44             |       |                   |
| 70             |               | 70      |             | 70    |             | 70            | 70                |       |                   |
| 60 50          |               | 60 50   |             | 60 50 |             | 60 50         | 60 50             |       |                   |
| 40             |               | 40      |             | 40    |             | 40            | 40                |       |                   |
| 30             |               | 30      |             | 30    |             | 30            | 30                |       |                   |
| 20             |               | 20      |             | 20    |             | 20            | 20                |       |                   |
| 10 0           |               | 10 0    |             | 10 0  |             | 10 0          | 10 0              |       |                   |
|                | 1 2 3 4 5 6 7 | 8 9 1 2 | 3 4 5 6 7 8 | 9 1 2 | 3 4 5 6 7 8 | 9 1 2 3 4 5 6 | 7 8 9 1 2 3 4 5 6 | 7 8 9 |                   |
Period
|     |        |       | Unconditional Optimal Consumption |     |       |            |  Consumption Choice |     |     |
| --- | ------ | ----- | --------------------------------- | --- | ----- | ---------- | ------------------- | --- | --- |
|     | Figure | F.32: | FluctP                            |     | Calc, | Repetition | 3 (Session          | 2)  |     |
80

G Instructions
G.1 Main Instructions
G.1.1 Calc Sessions
The instructions distributed to subjects in treatments where the calculator was enabled are
reproduced on the subsequent pages. All subjects received identical instructions, with the
exception of those in the PosIR treatment, where minor adjustments were made to incorporate
interest rates.
81

Experiment on Consumption and Saving Decisions over Time
Participant Instructions
You are taking part in an economics experiment in which you will be able to earn money. Your earnings
will depend on your decisions. It is therefore important to read these instructions with attention. During
the experiment you are not allowed to communicate with any other participant. If you do not follow
these instructions you will be excluded from the experiment and receive only the show-up payment of
$7.
The experiment consist of 4 PARTS. These instructions are for the first part only. After completing each
part of the experiment, you will receive instructions for each subsequent part. The earnings you
accumulate will be added up at the end of the experiment, and converted to Canadian dollars.
Specifically, for every 25 points you accumulate, you will obtain $1. You will also receive a $7 show-up
payment (if you arrived on time). Before you leave the lab, you will sign a receipt and will be paid in
cash privately.
First Part
In the first part of this experiment, you will be making decisions on how much to save and spend over
a number of periods.
There are two objects of interest in this experiment, tokens and points. The total number of points you
accumulate in a repetition will determine your monetary payoff.
You will participate in 3 repetitions of the exact same experiment, each consisting of 10 periods.
In every repetition, at the beginning of each period, you will receive some tokens. In addition to these
tokens, you may have additional tokens saved from previous periods.
Purchase Decision
Each period, after viewing the total number of tokens you have available, you must decide how many
units of output you would like to buy using tokens. When you submit your purchases orders you can
use up to two decimal places (the minimum you can buy is 0). Output is sold at a certain price per unit.
The output you buy will be transformed into points. The more output you acquire in a period, the higher
will be your points earnings for that period. Importantly, as you purchase more output in a single period,
you will earn fewer and fewer additional points. Your first unit will be worth the most, and each
subsequent point will be worth less.
After submitting your purchase order, the computer will calculate your expenditure as following:
Expenditure = Number of units purchased x Price per unit.
Page 1 of 3

This expenditure will be deducted from your token balance. If, at a certain period, you do not have
enough tokens to buy output, you will not be able to complete your order. You may not spend more
than your token balance.
Your token balance at the start of each period is given by the following:
Tokens at the beginning of current period = Tokens from previous period + Current income
Compensation
The points will be converted into Canadian dollars at the end of the experiment. You will be
compensated according to the following rules:
1. The game will be repeated 3 times. At the end of the experiment, the computer will randomly
select one of the repetitions for payment. That is, there is an equal chance that any repetition
will be the one that counts for payment.
2. The diagram below shows the relation between purchased output, points, and cash ($).
Purchased
Points Cash ($)
Output
3. The amount of points you earn in the randomly selected repetition will be converted into CAD
at the rate:
25 points = $1
4. Any tokens held at the end of a repetition are worthless.
5. Additionally, you will receive 4 points for every control question you answer correctly in the first
attempt; 3 points for every question you answer correctly in the second attempt; and 2 points
for every question you answer correctly in the third attempt.
Information
You will be provided precise information about the income and prices you will face in all 10 periods of
each repetition. That is, there is no uncertainty about these variables. You will also have information
about your previous decisions and economic variables. Please note that prices and income may vary
from repetition to repetition.
Repetitions
The experiment will consist of 3 repetitions of 10 periods each. After a repetition is completed, you will
see a Review Screen that will display your total points from that repetition. There will be no carryover
of tokens or points between repetitions. When a new repetition begins, all token balances and points
will be reset to zero.
Page 2 of 3

Output to Points Converter
Throughout the experiment, you will have access to an Output to Points Converter that you may use to
help you make decisions. To use the Output to Points Converter, you will need to enter the number of
units of output you wish to convert to points. After clicking the OK button, the computer will display
the points associated with the output you entered.
Standard Calculator
You may use a standard calculator by clicking on
Payoff Calculator
Throughout the experiment, you will have access to a calculator that you may use to help you make
decisions.
To use the calculator, you will need to fill in hypothetical values for your purchase decisions in the
current and future periods. After all your hypothetical decisions have been submitted, you will be able
to see what your points and tokens balance would be. You can consider as many hypothetical
combinations as you want before making each decision.
Before the experiment starts you will learn how to use the calculator; you will be able to practice with
it; and finally, you will have to answer some paid control questions.
Remember that your actual purchase decision has to be entered on the left hand side of the screen.
Page 3 of 3

G.1.2 No Calc Sessions
Forthesessionsinwhichthebudgetingcalculatorwasnotenabledthethirdpageoftheinstructions
was adapted as shown below.
85

Output to Points Converter
Throughout the experiment, you will have access to an Output to Points Converter that you may use to
help you make decisions. To use the Output to Points Converter, you will need to enter the number of
units of output you wish to convert to points. After clicking the OK button, the computer will display
the points associated with the output you entered.
Standard Calculator
You may use a standard calculator by clicking on
Income and Expenditure Table
Throughout the experiment, you will have access to an Income and Expenditure Table that you may use
to help you make decisions.
Each period, you will be able to see what your points and tokens balance are.
Before the experiment starts, you will learn how to read the table. You will also have to answer some
paid control questions in which you will be able to put to the test your ability to read the table.
Remember that your actual purchase decision has to be entered on the left hand side of the screen.
Page 3 of 3

G.2 Interactive Instructions
| Figure G.1: | Screenshot | for Interactive | Instructions | 1   |
| ----------- | ---------- | --------------- | ------------ | --- |
| Figure G.2: | Screenshot | for Interactive | Instructions | 2   |
87

| Figure G.3: | Screenshot | for Interactive | Instructions | 3   |
| ----------- | ---------- | --------------- | ------------ | --- |
| Figure G.4: | Screenshot | for Interactive | Instructions | 4   |
88

| Figure G.5: | Screenshot | for Interactive | Instructions | 5   |
| ----------- | ---------- | --------------- | ------------ | --- |
| Figure G.6: | Screenshot | for Interactive | Instructions | 6   |
89

| Figure G.7: | Screenshot | for Interactive | Instructions | 7   |
| ----------- | ---------- | --------------- | ------------ | --- |
| Figure G.8: | Screenshot | for Interactive | Instructions | 8   |
90

| Figure G.9:  | Screenshot | for Interactive | Instructions | 9   |
| ------------ | ---------- | --------------- | ------------ | --- |
| Figure G.10: | Screenshot | for Interactive | Instructions | 10  |
91

| Figure G.11: | Screenshot | for Interactive | Instructions | 11  |
| ------------ | ---------- | --------------- | ------------ | --- |
| Figure G.12: | Screenshot | for Interactive | Instructions | 12  |
92

H Computer Interface
H.1 Control Questions
| Figure H.13: | Screenshot | for Control | Question 13 |
| ------------ | ---------- | ----------- | ----------- |
| Figure H.14: | Screenshot | for Control | Question 2  |
93

| Figure H.15: | Screenshot | for Control | Question 3 |
| ------------ | ---------- | ----------- | ---------- |
| Figure H.16: | Screenshot | for Control | Question 4 |
94

| H.2 Risk | Preferences | Elicitation  |            |             |
| -------- | ----------- | ------------ | ---------- | ----------- |
|          |             | Figure H.17: | Screenshot | for Stage 2 |
95

H.3 Financial Literacy
| Figure H.18: | Screenshot | for Stage 3 |
| ------------ | ---------- | ----------- |
96

H.4 Race to 60
| Figure H.19: | Screenshot | for Stage 3 |
| ------------ | ---------- | ----------- |
97