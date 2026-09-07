---
conversion_metadata:
  converted_at: "2026-09-07T09:48:29Z"
  converter_tool: "markitdown"
  converter_version: "0.1.7"
  source_pdf: "Wang-Ly & Newell, 2023.pdf"
  source_pdf_sha256: "3a9b62dcf2b0b18bb97b827f116a04456858176da817950b0acc60f765b76598"
  page_count: 47
  markdown_char_count: 179287
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

How Income Volatility Influences Saving Decisions: Evidence from the Lab

Nathan Wang-Ly*,1, Ben R. Newell1,2

1 School of Psychology, UNSW Sydney, NSW 2052, Australia

2 UNSW Institute of Climate Risk & Response, UNSW Sydney, NSW 2052, Australia

* Corresponding author (Email: nathan.wang-ly@unsw.edu.au).

July 16, 2023

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 2 -->

Abstract

Around the world, it is becoming increasingly common for individuals to have volatile incomes,

which fluctuate from pay to pay. Previous research offers mixed evidence as to whether this

uncertainty about one’s income may increase or decrease saving behaviour. Across four incentivised

online experiments (N = 712), we examine the relationship between income volatility and saving

behaviour using a novel financial decision making task. In this task, participants receive hypothetical

income that is either consistent or that varies to different degrees. We capture participants’ perceptions

of how volatile their income is and observe how this influences their decision to spend this income or

save it towards an impending emergency. Our results indicate that receiving a more volatile income,

as measured by its coefficient of variation (CV), leads to higher savings within our task (£213 more

saved per 0.1 increase in CV). However, there appears to be a threshold level of volatility that must be

exceeded before participants save differently relative to receiving a stable income.

Keywords: Income volatility, Precautionary saving, Uncertainty, Financial decision making

PSYCInfo classification: 3900, 3920

JEL classification: D14, G51

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 3 -->

1.

Introduction

No one can be certain about how much they will earn in the future. However, not all uncertainties are

equal; some individuals have greater confidence in their future incomes than others. An individual

working in a traditional salaried role can reasonably expect to earn the same amount each pay cycle.

In contrast, an individual who is employed casually or who freelances may find that their earnings

fluctuate unpredictably. Around the world, economic trends suggest that this latter scenario is

becoming increasingly common. In Australia, permanent full-time employment rates have declined

from previous decades, insecure part-time employment has become prevalent, and there has been a

dramatic rise in platform work (often referred to as ‘gig work’) (Senate Select Committee on Job

Security, 2022). Similar trends have been observed across other advanced economies in Asia and

Europe (Hipp et al., 2015; Kalleberg & Hewison, 2013).

Previous research has identified numerous ways in which income uncertainty may negatively

impact individuals’ and their families’ lives. Experiencing fluctuations in income has been associated

with psychological depression (Prause et al., 2009), higher risk of mortality (Halliday, 2007), greater

risk of divorce (Nunley & Seals, 2010), and increased probability of mortgage default (Diaz-Serrano,

2005). Much of this research has been based on ‘inter-year’ income volatility (income that varies

between years), with research on ‘intra-year’ income volatility (income that varies within a year)

being comparatively scarce. Only recently has there been an increase in studies examining how

financial and health outcomes are influenced by monthly fluctuations in income (e.g., Anvari-Clark &

Ansong, 2022; Gladstone et al., 2020), many of which have been motivated by the growth of the gig

economy (e.g., Sayre, 2022; Wang et al., 2022), as well as the severe disruption to income caused by

the COVID-19 pandemic (Wang-Ly & Newell, 2022). However, given the challenges of manipulating

income in real-world settings, these studies have typically been observational in nature. These

observational studies are inherently limited in their ability to prove causal links between the

experience of income volatility and outcomes of interest (Rosenbaum, 2015).

To our knowledge, only two studies have investigated the influence of intra-year income

volatility via experimental methods, with both finding evidence suggesting that volatility drives

individuals to behave in a more financially impatient manner. The first study involved providing

income spikes to Kenyan participants via an unconditional cash transfer program (West et al., 2020).

Financial impatience was measured by giving participants multiple hypothetical choices between a

‘smaller-sooner’ reward (e.g., KSH 500 today) and a ‘larger-later’ reward (e.g., KSH 525 in six

months). Participants who received the income spikes tended to choose the smaller-sooner option

more often compared to those who did not receive the spikes, demonstrating a greater degree of

financial impatience. In the second study, participants completed simulated work tasks for

hypothetical income as part of a lab-based experiment (Peetz et al., 2021). Participants either received

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 4 -->

a stable income (the same income per work task) or a volatile income (income that varied between

work tasks). At the end of the experiment, participants who received the volatile income were more

likely to choose the smaller-sooner participation reward (USD 15 today vs USD 17 in two weeks)

compared to those who had received the stable income.

Inspired by these two studies, we saw an opportunity to apply a similar experimental

approach to better understand how income volatility influences key household financial decisions. In

the present research, we chose to focus our attention on saving behaviour for two reasons. First,

income uncertainty tends to be more severe for individuals in poorer financial circumstances (Bania &

Leete, 2022). For these individuals, the ability to accumulate savings and create ‘financial slack’ is

especially critical for meeting unexpected expenses and avoiding debt (Mullainathan & Shafir, 2009).

Second, the literature offers conflicting perspectives on whether income volatility should increase or

decrease saving behaviour, meaning our work could offer useful clarifying evidence.

On the one hand, the argument that experiencing income volatility increases saving behaviour

seems intuitive. To illustrate, imagine that you wanted to accumulate a certain amount of savings for

future needs (e.g., a holiday or to buffer against future emergencies). If you earned a steady and

predictable income, a prudent strategy might involve setting aside a consistent amount of money such

that you would achieve the goal within your desired timeframe. Now suppose that your income was

instead volatile and unpredictable. The consistent saving strategy would no longer be feasible; instead,

it might be necessary to save more to insure against a potential dip in future income. This is the basic

premise underlying the traditional economic perspective of how income volatility should affect saving

behaviour. Early theoretical work suggested that being uncertain about one’s future earnings should

boost precautionary saving motives (Drèze & Modigliani, 1972; Leland, 1968; Sandmo, 1970). This

view has been supported by numerous empirical studies (for an overview, see Lugilde et al., 2019).1

For example, one study involving US personal income data found that doubling the level of income

uncertainty of an individual or household was associated with a 29 percent increase in their ratio of

wealth to income (i.e., a greater saving rate) (Kazarosian, 1997).

On the other hand, there are several valid reasons why income volatility might instead be

expected to reduce saving behaviour. First, if income volatility results in greater financial impatience

(Peetz et al., 2021; West et al., 2020), individuals may be biased towards actions that offer immediate

benefits (spending) over actions that offer benefits in the distant future (saving). This would be

consistent with previous work showing that more present-focused time preferences are associated

with lower retirement savings balances (Goda et al., 2019). Second, experiencing income volatility

may induce feelings of stress or scarcity, as dips in income can create temporary shortfalls between

1 However, see Fulford (2015) for evidence that income uncertainty is not an important motive for precautionary 
saving.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 5 -->

available funds and upcoming expenses, forcing individuals to make difficult trade-offs between their

immediate and future needs (Bania & Leete, 2022). Both stress and scarcity have been found to

impair long-term and goal-directed decision making (Haushofer & Fehr, 2014; Mani et al., 2013,

2020; Schwabe & Wolf, 2009), providing additional reason to believe that income volatility might

reduce one’s propensity to save. Third, individuals may decide to save less as part of a considered

choice to abandon (or at least heavily discount) their focus on the long-term. They may instead shift

their focus to achieving short-term outcomes, where the associated rewards are typically better

defined and allow for earlier gratification—an approach that has been argued to be a rational response

to uncertainty (Fawcett et al., 2012; Pepper & Nettle, 2017). Consistent with this view, numerous

studies have shown that saving rates are negatively impacted when individuals feel a lack of control

over their future circumstances (Cobb-Clark et al., 2016; Perry & Morris, 2005; Shapiro & Wu, 2011).

2.

Overview of studies

To assess the merit of these opposing perspectives, we conducted four laboratory-based experiments

in which we manipulated the volatility of participants’ income and observed how this affected the way

they traded off between spending and saving. All four experiments involved a novel financial decision

making task where participants received hypothetical income for completing work tasks (similar to

Peetz et al., 2021) and could choose between spending their earnings or saving for an impending

emergency.

In Experiment 1, we tested three levels of income volatility (including no volatility) and

observed the highest saving rates from participants whose income was most volatile. However, we

also observed a discrepancy between participants’ self-reported perceptions of how volatile their

income was and their observed saving behaviour. Experiment 2 examined whether this was because

participants’ saving behaviour was instead being driven by other dimensions of the income sequence

(e.g., the minimum income received). Experiment 3 provided evidence that the discrepancy was due

to participants being asked to provide an absolute judgment of volatility; participants were able to

distinguish between levels of volatility when instead making relative judgments. Finally, in

Experiment 4, we tested a single condition in which we made participants’ income even more volatile

than the most volatile condition in Experiment 1. This established a clearer relationship between

income volatility and increased saving behaviour while also suggesting the existence of a volatility

threshold that needed to be exceeded for saving behaviour to be influenced.

Our study seeks to make several contributions to the literature. First, we continue to expand

the body of experimental work examining the effect of income volatility on financial decisions. We

offer experimental evidence in support of the view that experiencing volatile income increases saving

behaviour. Second, we examine the impact of different degrees of income volatility, allowing us to

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 6 -->

investigate not only on the extensive margin of the income volatility effect, but also the intensive

margin. Third, we offer a novel financial decision making task that has potential for reuse in future

income volatility experiments or could be adapted to answer similar questions around influences on

saving behaviour.

3.

Experiment 1

The purpose of Experiment 1 was to examine how participants’ saving behaviour within our financial

decision making task was influenced by the level of income volatility they experienced. We generated

different sequences of income that varied in their coefficients of variation (CV). CV is a commonly

referenced measure of income volatility (Bania & Leete, 2009; Farrell & Greig, 2016; Hannagan &

Morduch, 2015) that can be calculated by dividing the standard deviation of a sequence by its mean.

Therefore, the larger the CV value, the more volatile the income. One advantage of the CV metric is

that it provides a standardised value that allows for comparison across incomes that may differ in

magnitude, frequency, and timing.2 For Experiment 1, we tested three income sequences with CV

values of 0 (i.e., no volatility), 0.30 and 0.60.

3.1.  Method

3.1.1.  Participants

We recruited 241 participants3 (Mage = 39.65 years; 144 males; 95 females; 1 non-binary; 1 preferred

not to say) from Prolific Academic, an online participant recruitment platform. Our sample size was

based on an a priori power analysis conducted using statistical software G*Power (Faul et al., 2007)

based on detecting a small effect in a between-subjects study (𝛿 = .80; 𝛾 = .20; 𝛼 = .05). To be eligible

for our sample, participants needed to be between the ages of 18 and 65, located in the UK, and fluent

in English. Participants received £3.00 (USD 3.77) in exchange for their participation and were also

eligible for an additional bonus of £3.00 (USD 3.77) based on their performance in the financial

decision making task. Additional details on the demographic and financial characteristics of our

participant samples for each experiment are provided in the Online Appendix.

2 However, see Kvålseth (2017) for an alternative measure of volatility (the ‘second-order coefficient of 
variation’) that has additional useful properties such as being restricted between zero and one, and being less 
sensitive to outliers. 
3 In both Experiments 1 and 2, we encountered an issue during data collection which led to having one 
participant more than was intended.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 7 -->

3.1.2.  Materials

The financial decision making task4 used in Experiment 1 involved completing work tasks for

hypothetical income and making decisions around spending and saving for an impending emergency.

In each round of the game, participants were asked to rearrange a six-character string of letters (e.g.,

“hksykjl”) into alphabetical order as their work task. Upon completion, they received income and

were asked how much they wanted to spend. Money could be spent to purchase points (£1.00 = 1

point), which were later used to determine eligibility for the bonus performance-based payment.5 Any

money that was not spent remained as savings and was carried over into subsequent rounds, where it

could again be spent or saved.

The income participants received for their work tasks varied depending on which of the three

experimental conditions they were allocated to: No Volatility (n = 81), Low Volatility (n = 80), and

High Volatility (n = 80). In all three conditions, participants received the same total income across the

15 task rounds: £15,000. However, the extent to which their income fluctuated differed. In the No

Volatility condition, participants received £1,000 after each work task—corresponding to a CV of 0.

In the Low Volatility condition, participants’ income ranged between £431 and £1,340, with the

overall sequence of incomes having a CV of 0.30.6 In the High Volatility condition, incomes ranged

between £173 and £2,088, with a CV of 0.60. For participants in the Low and High Volatility

conditions, the order in which they received the different incomes was randomised. For more details

on the income sequences used across the experiments, see the Online Appendix.

At the end of the task (after the 15th round), participants encountered a financial emergency:

home repairs costing £4,500 that had resulted from storm damages. When this emergency occurred, if

participants had adequate savings, they “won” the task, meaning they could keep the points they had

purchased. However, if participants’ savings were inadequate, they lost all their purchased points.

Importantly, while participants were advised at the start of the task that there would be a financial

emergency, they were not told when it would occur nor how much it would cost. Therefore, their

objective was to balance the competing goals of maximising points purchased (to potentially earn the

bonus payment) while ensuring they saved enough to withstand the financial emergency (to avoid

losing their points).

Just prior to revealing the cost of the financial emergency, participants were asked to provide

a series of responses. This timing was deliberate such that participants’ responses would not be

4 Experimental instructions and select screenshots of the task are provided in the Online Appendix. Code for the 
task is available in the Supplementary Materials (https://osf.io/pqgha/).  
5 Participants were eligible for a bonus payment (in addition to their participation payment) if their final score in 
the task was within the top 10 percent of their experimental condition. 
6 Previous work has estimated that the average household experiences a CV of between 0.30 to 0.40 (Farrell et 
al., 2019; Hannagan & Morduch, 2015); however, this varies substantially between lower- and higher-income 
households (Mills & Amick, 2010; Morris et al., 2015).

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 8 -->

affected by the outcome of the experiment (i.e., whether they had saved adequately). Participants were

asked to rate how volatile they perceived their income to have been during the task (0 = “Not

Volatile”; 10 = “Extremely volatile”). Participants were advised that they could think of volatility as a

reflection of how well they could predict their income if there was an additional round (Konovalova

& Pachur, 2021). We similarly asked participants to rate how difficult it was to decide how much to

spend or save each round (0 = “Not difficult”; 10 = “Extremely difficult”). Finally, we measured

financial impatience using the ‘fill-in-the-blank’ approach (Smith & Hantula, 2008), which has been

previously used in studies involving delay discounting (Chapman, 1996; Kirby & Maraković, 1995;

Weatherly et al., 2010). Participants were instructed to imagine that they were given the choice

between two bonus rewards for their involvement in the experiment. The first option was to receive

£50 in two weeks’ time. Alternatively, they could opt for an immediate reward. Participants were

asked to indicate the lowest amount they would accept immediately (‘smaller-sooner amount’) that

would make it preferable to the larger, delayed reward. The response was bounded between £0 and

£50, with a lower smaller-sooner amount indicating a higher degree of financial impatience.

3.1.3.  Procedure

Participants were advised that they would be playing a financial decision making game and received

instructions outlining the work tasks and the objective of the game. This was followed by a practice

stage which included three practice rounds (with income of £50 per work task) and a practice

financial emergency (a £50 parking ticket fine).

After the practice stage, participants’ savings and points were reset to zero and they began the

15 experiment rounds. Once the experiment rounds were complete, participants were informed that

the financial emergency was about to occur and were asked to provide responses to perceived

volatility, perceived difficulty, and financial impatience measures described in the previous section.

Following this, the cost of the emergency was revealed, and participants were advised of the outcome

of the game. Finally, participants were asked to provide information about their demographics and

financial situations before receiving a debrief of the experiment.

3.2.

Results

For all four experiments, we conducted Bayesian statistical analyses (using default priors) and report

the Bayes factors (BF10) associated with our results. In cases where the Bayes factor was less than one

(i.e., evidence favoured the null hypothesis), we reported the inverse Bayes factor (BF01) to assist with

comparability of evidence strength. Interpretations of Bayes factors were based on guidelines

suggested in Lee and Wagenmakers (2013). Unless indicated otherwise, analyses of variance

(ANOVAs) were used for overall tests of differences across multiple conditions and t-tests were used

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 9 -->

for pairwise comparisons between conditions. Our experiment data and code have been made

available in the Supplementary Materials (https://osf.io/pqgha/).

3.2.1.  Perceived volatility ratings

We first examined whether there were differences between conditions in participants’ ratings of how

volatile their income was (‘perceived volatility ratings’). As seen in Figure 1, our analysis indicated

that there was extreme evidence that perceived volatility ratings differed between conditions (BF10 =

6.72×1013), suggesting that our income volatility manipulation had worked. This difference was

driven by substantially lower volatility ratings in the No Volatility condition (M = 3.17) compared to

the Low Volatility (M = 6.00) and High Volatility (M = 6.40) conditions (BF10 = 2.04×108 and

1.11×1011 respectively). However, there was moderate evidence suggesting that perceived volatility

ratings did not differ between the Low and High Volatility conditions (BF01 = 3.15).

Figure 1. Mean perceived volatility ratings by level of income volatility in Experiment 1. Standard

error bars indicated.

3.2.2.  Final savings

We next analysed how much participants had saved at the end of the task (‘final savings’). As seen in

Figure 2, we observed very strong evidence that final savings differed between conditions (BF10 =

38.71). Participants saved substantially more in the High Volatility condition (M = £8,571.64)

compared to the No Volatility (M = £6,647.88) and Low Volatility (M = £6,579.54) conditions (BF10 =

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 10 -->

33.67 and 24.23 respectively). However, there was moderate evidence suggesting that final savings

did not differ between the No and Low Volatility conditions (BF01 = 5.84).

Figure 2. Distribution of final savings by level of income volatility in Experiment 1. Means and

standard error bars indicated.

3.2.3.  Perceived difficulty and financial impatience

We then examined participants’ ratings of how difficult they found it to decide how much to spend or

save throughout the task (‘perceived difficulty’). There was moderate evidence that these ratings did

not differ between conditions (BF01 = 6.44). The mean rating provided across the conditions was 4.07

(out of 10). Likewise, there was moderate evidence that financial impatience did not vary between

conditions, as measured via participants’ smaller-sooner amounts (BF01 = 7.67). The mean amount

participants were willing to accept immediately instead of a £50 reward in two weeks’ time was

£37.60.

3.3.  Discussion

Our results indicated that participants saved substantially more in the High Volatility

condition than the No and Low Volatility conditions—consistent with the view that income volatility

increases savings motives. However, we did not observe the same boost in savings for the Low

Volatility condition relative to the No Volatility condition. The simplest explanation would be that

participants’ income was volatile enough to impact their saving behaviour in the High Volatility

condition but was not volatile enough to do so in the Low Volatility condition. This would imply that

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 11 -->

there exists a threshold between the CVs we used (0.30 for Low Volatility; 0.60 for High Volatility)

which must be surpassed before a change in saving behaviour would be observed. However,

complicating this explanation was the fact that participants in the Low and High Volatility conditions

reported their income as being similarly volatile (based on their perceived volatility ratings). The

question we thus needed to address was why participants in the Low Volatility condition did not save

differently (relative to the No Volatility condition) despite perceiving their income to be as volatile as

the High Volatility condition.

One possibility we considered was whether the increased saving behaviour observed from

participants in the High Volatility condition was being driven by something other than income

volatility (as defined by CV). This idea was inspired by recent work which showed that individuals’

perceptions of a number sequence’s variance is not always perfectly related to the objective statistical

variance of the sequence (Konovalova & Pachur, 2021). In their study, Konovalova and Pachur (2021)

examined how other characteristics of a number sequence (e.g., mean, range, pairwise distance)

contributed to perceptions of variance. The study found that a sequence’s range often served as a

better individual predictor of participants’ perceptions of variance than statistical variance itself.

This led us to examine in Experiment 2 whether three other dimensions of the income

sequences we gave participants could better account for their saving behaviour: the minimum income

participants received during the task, the maximum income, and the range of incomes. As shown in

Table 1, the income sequences used in Experiment 1 varied not only in their CV, but also these

additional dimensions. As an example, it may have been the minimum income participants received

that was driving their saving decisions—perhaps because the income shock associated with earning an

unexpectedly low income forced participants to update their view of how uncertain the (experimental)

world was, thereby prompting them to save more as a precaution (Chamon et al., 2013; Collins &

Gjertson, 2013). If this were the case, it would explain why participants’ perceived volatility ratings

did not neatly map onto their saving behaviour.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 12 -->

Table 1.

Dimensions of income sequences used in Experiment 1.

Condition

Incomes (£)

No Volatility

1,000 1,000 1,000 1,000 1,000

CV

0.00

Min

Max

Range

1,000

1,000

0

1,000 1,000 1,000 1,000 1,000

1,000 1,000 1,000 1,000 1,000

Low Volatility

431 570 656 794 873

0.30

431

1,340

909

883 910 990 1,158 1,202

1,277 1,279 1,311 1,326 1,340

High Volatility

173 274 466 526 529

0.60

173

2,088

1,915

650 661 847 1,101 1,374

1,404 1,436 1,571 1,900 2,088

Note. CV = Coefficient of variation. Min, Max = Minimum/Maximum incomes received during task.

While the main focus for this study is saving behaviour, it is worth noting that our income

volatility manipulation did not appear to increase participants’ financial impatience—contrary to prior

findings (Peetz et al., 2021; West et al., 2020). One possible reason for our failure to observe an effect

is that both our income volatility manipulation and our measure of financial impatience were

hypothetical. While Peetz et al. (2021) also manipulated the volatility of hypothetical income, their

measure of financial impatience involved participants choosing between two real payments. In the

case of West et al. (2020), the measure of financial impatience involved hypothetical choices, but

participants experienced volatility in their real income. Another possibility for the inconsistency in our

findings could be due to our use of different methods of measuring financial impatience. While our

study used a fill-in-the-blank approach, both prior studies used ‘binary-choice’ tasks, which give

participants the choice between defined smaller-sooner and larger-later amounts. Previous work

suggests that binary-choice tasks can produce steeper discounting rates compared to fill-in-the-blank

tasks (Smith & Hantula, 2008). It is therefore possible that the effect of income volatility on financial

impatience is small—one that our measure was unable to detect, but that more sensitive measures may

have been able to. Though exploring these potential explanations (or any others) was beyond the

scope of our study, our null result suggests the need for further investigation to have greater

confidence in the link between income volatility and financial impatience.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 13 -->

4.

Experiment 2

For Experiment 2, we generated three new income sequences that would allow us to tease apart

whether the minimum income, maximum income, or range of incomes would provide a better account

for saving behaviour than CV. The new sequences were designed such that they could be compared

against one another, as well as against the High Volatility condition from Experiment 1. Each

sequence shared a different set of dimensions with the High Volatility condition: either the minimum

income (but not the maximum or range), the maximum income (but not the minimum or range), or

both the minimum and maximum incomes (and therefore also the range). Notably, however, all three

conditions shared the same statistical variance as one another (CVs = 0.37) but were deliberately

created to be less volatile than the High Volatility condition (CV = 0.60).

4.1.  Method

4.1.1.  Participants

We recruited 241 new participants (Mage = 39.65 years; 108 males; 130 females; 2 non-binaries; 1

preferred not to say) from Prolific Academic using the same eligibility criteria described for

Experiment 1. In addition to these criteria, we excluded anyone who had participated in the previous

experiment. Participants again received a £3.00 (USD 3.77) participation payment and were eligible

for a £3.00 (USD 3.77) bonus payment based on their task performance.

4.1.2.  Materials and procedure

Experiment 2 used the same financial decision making task and procedure as described for

Experiment 1. However, participants were assigned to three new conditions which used different

income sequences from the prior experiment: “Same Range” (n = 80), “Same Min” (n = 81), and

“Same Max” (n = 80). The names of these conditions indicated what characteristic(s) their income

sequence shared with the High Volatility condition from Experiment 1.

In the Same Range condition, participants’ income sequence shared the same minimum and

maximum values as the High Volatility condition (£173 and £2,088 respectively), and therefore the

same range (£1,915). However, the income sequence was constructed to have a lower coefficient of

variation (CV = 0.37 vs 0.60 for the High Volatility condition). This would allow us to directly

compare the two conditions to determine whether CV was driving the difference in saving behaviour

or whether it was one of the other dimensions.

In the Same Min condition, participants’ income ranged from £173 to £1,580 across rounds—

sharing the same minimum income as the High Volatility condition but differing in the maximum

income and range. Conversely, the Same Max condition shared the same maximum income as the

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 14 -->

High Volatility condition (£2,088) but had a different minimum income (£681) and range. Notably,

however, the range of the Same Min and Same Max conditions were designed to be identical

(£1,407). Both sequences were also constructed to share the same CV as the Same Range condition

(CV = 0.37).

All three sequences therefore shared the same statistical variance (unlike in Experiment 1),

but varied in their minimum income, maximum income, and range of incomes. As with the previous

experiment, regardless of which income sequence participants received, their total income across the

task was £15,000. By keeping this and all other task parameters the same as Experiment 1, it became

possible to directly compare the High Volatility condition from the first experiment with the new

conditions in Experiment 2.

4.2.

Results

4.2.1.  Comparisons between Same Range, Same Min, and Same Max conditions

We first analysed the data from our three Experiment 2 conditions. This allowed us to explore whether

any differences in our measures were being driven by dimensions of participants’ income sequences

other than CV.

Across our four measures (perceived volatility, final savings, perceived difficulty, and

financial impatience), we consistently observed no differences between our three conditions. The

evidence for this was moderate for perceived volatility (BF01 = 3.91), strong for final savings (BF01 =

16.19), moderate for perceived difficulty (BF01 = 6.82), and strong for financial impatience (BF01 =

12.50).

4.2.2.  Comparisons against High Volatility condition

We then compared the perceived volatility ratings and final savings of our three Experiment 2

conditions against the High Volatility condition from Experiment 1 (see Figure 3).

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 15 -->

(a)  Mean perceived volatility ratings

(b)  Distribution of final savings

Figure 3. Perceived volatility ratings and final savings by level of income volatility in Experiment 2.

High Volatility condition from Experiment 1 shown on right of dotted line for comparison. Means and

standard error bars indicated.

There was anecdotal evidence that participants perceived their income to be more volatile in

the High Volatility condition (M = 6.40) than the Same Range condition (M = 5.69) (BF10 = 1.52).

However, there was moderate evidence that the perceived volatility ratings did not differ between the

High Volatility condition and the Same Min (M = 6.31) or Same Max (M = 6.11) conditions (BF01 =

5.66 and 4.18 respectively).

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 16 -->

In contrast, there was consistent evidence that participants saved more in the High Volatility

condition (M = £8,571.64) compared to the other three conditions. The evidence was moderate for the

Same Range (M = £7,096.65) and Same Max (M = £6,842.40) conditions (BF10 = 3.03 and 6.69

respectively), and anecdotal for the Same Min condition (M = £7,362.69) (BF10 = 1.16).

4.3.  Discussion

Our results did not support the hypothesis that saving behaviour was being driven by a dimension of

the income sequence other than CV. Despite varying the minimum income, maximum income, and

range of incomes between conditions, participants all exhibited similar saving behaviour. If anything,

our findings provided greater reason to believe that CV was the driver of saving behaviour. All three

conditions saved less than the High Volatility condition, with the consistent difference being their

lower CV (CV = 0.37 vs 0.60). Thus, we saw further evidence that increased income volatility

corresponded to higher savings within our task.

However, we continued to observe a discrepancy between participants’ perceptions of their

income’s volatility and their saving behaviour. While participants saved more in the High Volatility

condition, their perceived volatility ratings were similar to the ratings provided in our Experiment 2

conditions (with the exception of the Same Range condition, where the evidence of a difference was

only anecdotal). This echoed what we had observed in Experiment 1, in which participants from the

Low and High Volatility conditions had rated their income as similarly volatile despite exhibiting

different saving behaviour.

This led us to consider a new hypothesis: that participants were giving similar responses on

our perceived volatility rating scale because we were asking them to make an absolute judgment with

only one objective point of reference (0 = “not volatile at all”). Previous work suggests that judgments

can differ when made from an absolute versus relative standpoint (e.g., Fox & Tversky, 1995; Goffin

& Olson, 2011; Stewart et al., 2006). It was therefore possible that participants in different conditions

were perceiving the volatility of their income differently, but shared similar thought processes in how

this should be reflected in their response on the scale—for example, thinking “there is some volatility

but not an extreme amount, so I will respond with a seven”. This could explain why participants who

experienced some degree of income volatility (i.e., all conditions except for the No Volatility

condition) provided similar ratings of perceived volatility while differing in their saving behaviour.

To examine this hypothesis, we needed participants to provide relative judgments of their

income’s volatility. To obtain these judgments, we adapted our procedure in Experiment 3 such that

participants would have two attempts at the financial decision making task. These two attempts used

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 17 -->

income sequences with different levels of volatility, allowing us to compare participants’ perceived

volatility ratings between attempts.

5.

Experiment 3

For Experiment 3, participants were given two attempts at the financial decision making task. In one

attempt, participants received the same income as the Low Volatility condition from Experiment 1; in

the other, they received the same income as the High Volatility condition. The ordering of the income

sequences was counterbalanced.

Our goal was to examine whether participants would be sensitive to the different levels of

volatility between their attempts. We preregistered7 three key hypotheses based on this goal prior to

conducting the experiment. First, participants would provide higher perceived volatility ratings during

their High Volatility attempt compared to their Low Volatility attempt. Second, participants would

provide similar ratings during their first attempt, irrespective of whether they received the Low

Volatility or High Volatility income sequence. This would be consistent with what had been observed

in Experiment 1. Third, perceived volatility ratings would differ when comparing second attempts at

the task. We expected that since participants would be making relative judgments of volatility in their

second attempts, they would provide higher ratings if this second attempt involved the High Volatility

income sequence, whereas they would provide lower ratings if their second attempt instead involved

the Low Volatility income sequence.

5.1.  Method

5.1.1.  Participants

We recruited 150 new participants (Mage = 38.85 years; 75 males; 74 females; 1 non-binary) from

Prolific Academic using the same eligibility criteria as described in the previous two experiments.

Sample size was based on an a priori power analysis that allowed for detection of a small effect in

both between- and within-subjects comparisons (𝛿 = .80; 𝛾 = .20; 𝛼 = .05). Participants received a

£4.50 (USD 5.66) participation payment and were eligible for a £3.00 (USD 3.77) bonus payment

based on their task performance.

5.1.2.  Materials and procedure

For Experiment 3, the procedure was adapted such that participants were given two attempts at the

financial decision making task. In one attempt, participants received the same income sequence that

7 Our experiment was preregistered using the AsPredicted platform (https://aspredicted.org/bg6gi.pdf).

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 18 -->

was used in the Low Volatility condition from Experiment 1; in the other, they received the High

Volatility income sequence. The order in which participants received these attempts was

counterbalanced, meaning half of participants received the Low Volatility version first (“Low to

High”; n = 75), while the other half received the High Volatility version first (“High to Low”; n = 75).

The inherent issue in allowing participants two attempts at the task is that participants’

behaviour in the second attempt may be confounded by learnings from their first attempt. This would

impair our ability to compare our results against the behaviour we had observed in Experiment 1. We

sought to mitigate this concern through several deliberate design choices when adjusting our

procedure from the previous experiments. First, at the end of participants’ first attempt, we advised

them that the emergency had occurred, but did not reveal how much it cost. This was only revealed at

the end of the experiment after participants had completed both attempts. Second, we explicitly

indicated to participants that the timing and cost of the emergency may differ between attempts. This

sought to dissuade participants from assuming that the timing of the emergency would be the same for

both attempts.8 Finally, although participants’ final score in the experiment was calculated by

combining their performance in each attempt, we visually reset their score to zero in between

attempts. This was intended to reiterate to participants that the two attempts were independent.

The overall procedure thus proceeded as follows. Participants were advised that they would

be given two attempts at a financial decision making game. After reading the instructions, participants

underwent the practice stage, followed by their first attempt at the task. At the end of the first attempt,

participants were informed that the financial emergency was about to occur and were asked to rate the

volatility of their income. Participants were then told that the cost of the emergency would only be

revealed after they had completed their second attempt, which they subsequently commenced. At the

end of their second attempt, participants were again asked to rate the volatility of their income.

Following this, the cost of both emergencies was revealed9 and participants were advised of the

outcome of each attempt. Participants’ total score across both attempts was used to determine

eligibility for the bonus reward. Finally, participants were asked to provide information about their

demographic and financial situations, before receiving a debrief.

8 However, in both attempts, the emergency needed to occur after the 15th round so that the income sequences 
used would be consistent with those from Experiment 1.     
9 As with the previous experiments, the first emergency involved home repairs with a total cost of £4,500. The 
second emergency involved a car breakdown and cost £2,500.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 19 -->

5.2.

Results

5.2.1.  Comparison of volatility ratings between attempts

Figure 4 shows participants’ mean perceived volatility ratings as a function of the level of volatility

(Low or High) and whether it was their first or second attempt. As predicted, we observed moderate

evidence that participants provided similar ratings during their first attempt, regardless of whether this

was the Low Volatility or the High Volatility version (BF01 = 3.28). However, contrary to our

prediction, there was also anecdotal evidence that ratings did not differ on participants’ second

attempt either (BF01 = 2.13).

Figure 4. Mean perceived volatility ratings by level of income volatility and task attempt in

Experiment 4. Low and High Volatility conditions from Experiment 1 shown on right of dotted line

for comparison. Standard error bars indicated.

While we did not find evidence for our hypothesis when examining volatility ratings at the

group level, we did observe evidence at the individual participant level. We conducted a paired t-test

comparing participants’ ratings in their Low Volatility and High Volatility attempts. This indicated that

there was anecdotal evidence of participants providing higher ratings during their High Volatility

attempt compared to their Low Volatility attempt (BF10 = 2.91), with the mean difference between

ratings being 0.43.

5.2.2.  Additional pre-registered analyses

As part of our preregistration, we planned two additional analyses that were unrelated to our main

hypotheses about perceived volatility ratings. First, we hypothesised that participants would save

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 20 -->

more in the High Volatility condition than in the Low Volatility condition (see Figure 5). We examined

this by conducting a Bayesian ANOVA where level of income volatility and task attempt were entered

as variables. This provided Bayes factors for different combinations of predictive models, from which

we could compute inclusion factors.10 Our findings contradicted our hypothesis; there was moderate

evidence against an income volatility level effect (BF01 = 3.36). Instead, we observed extreme

evidence in favour of a task attempt effect (BF10 = 5.01×106), with participants saving substantially

more in their second attempt regardless of whether it involved the Low or High Volatility income

sequence. There was also anecdotal evidence against an interaction between task attempt and income

volatility level (BF01 = 2.11).

Figure 5. Distribution of final savings by level of income volatility and task attempt in Experiment 3.

Low and High Volatility conditions from Experiment 1 shown on right of dotted line for comparison.

Means and standard error bars indicated.

Our other additional hypothesis was that we should see similar perceived volatility ratings and

final savings from participants completing their first attempts at the task as what was observed in

Experiment 1. This would provide a signal of reliability for participants’ behaviour within our task.

We started by comparing the participants from Experiment 3 who received the Low Volatility income

sequence first with participants in the Low Volatility condition from Experiment 1. There was

moderate evidence to suggest that participants provided similar perceived volatility ratings (Figure 4)

and ended the task with similar final savings amounts (Figure 5; BF01 = 5.08 and 4.51 respectively).

When drawing the same comparison between the High Volatility counterparts, we again observed

10 Inclusion factors are computed by comparing the posterior odds of models that include and exclude a 
predictor of interest (Van Den Bergh et al., 2020). These help to quantify the level of evidence for whether the 
predictor should be included.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 21 -->

moderate evidence in favour of the perceived volatility ratings being similar (BF01 = 5.44). However,

we found moderate evidence that participants’ final savings differed (BF10 = 5.50); participants who

received the High Volatility income sequence in their first task attempt in Experiment 3 appeared to

have saved substantially less than those who were in the High Volatility condition from Experiment 1

(M = £6,834.69 vs £8,571.64).

5.3.  Discussion

Experiment 3 provided some credence to our hypothesis that participants were sensitive to different

levels of income volatility, but we were failing to capture this when asking for an absolute judgment

on our 11-point scale (0 = “Not Volatile”; 10 = “Extremely Volatile”). This helped to explain why

participants’ ratings of income volatility across our previous experiments did not necessarily align

with their observed saving behaviour. It also reintroduced the possibility of an income volatility

‘threshold’ that needed to be exceeded for participants to adjust their behaviour within the task. As a

reminder, we observed in Experiment 1 that participants saved more in the High Volatility condition

relative to those who had received a stable income, but that this difference was not observed for the

Low Volatility condition.

However, before we could make any claims about a potential threshold, we first needed to

resolve the inconsistency between the saving behaviour we had observed from participants in

Experiment 1’s High Volatility condition and the participants who received the High Volatility

condition as their first attempt in Experiment 3. In theory, these participants should have exhibited

similar saving behaviour; the only difference was that those in Experiment 3 would have known that

they would be completing a second (independent) attempt at the task. The fact that we observed

higher savings in Experiment 1 but not 3 called into question how reliable our finding was, and by

extension, whether there was even an income volatility effect at all.

This led us to run a single additional experimental condition in Experiment 4 in which we

further increased the income volatility that participants would experience (“Very High Volatility”; CV

= 0.90). We expected that running the results of this condition would help to build confidence in one

of two conclusions. If these participants did not save any differently compared to participants who

received stable incomes (in Experiment 1), we could be more confident that income volatility does not

influence saving decisions, and that the increased saving effect we observed in the High Volatility

condition from Experiment 1 was likely a false positive. In contrast, if we did observe higher savings

in this Very High Volatility condition, we would instead have greater support for an effect of income

volatility on saving behaviour and consider our results from Experiment 3 to be a false negative.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 22 -->

6.

Experiment 4

In Experiment 4, we generated a new income sequence that was more volatile than the conditions

from Experiment 1. This condition was known as the Very High Volatility condition and had a CV of

0.90. All participants were placed in this condition and completed only one attempt at the financial

decision making task.

6.1.  Method

6.1.1.  Participants

We recruited 80 new participants (Mage = 36.63 years; 34 males; 46 females) from Prolific Academic

using the same eligibility criteria as described in the previous experiments. Our sample size was based

on having the same number of participants per condition as Experiment 1. Participants received £3.00

(USD 3.77) in exchange for their participation and were also eligible for an additional bonus of £3.00

(USD 3.77) based on their performance in the financial decision making task.

6.1.2.  Materials and procedure

Experiment 4 used the same financial decision making task and followed the same procedure as

Experiment 1. All participants—henceforth referred to as the Very High Volatility condition—

received a newly generated income sequence that ranged from £44 to £3,457, with the CV of the

sequence being 0.90. Consistent with all other income sequences, the total income received across the

task remained at £15,000.

6.2.

Results

In this section, we first compare perceived volatility ratings and final savings between our Very High

Volatility condition and the No Volatility condition in Experiment 1. We then report on analyses using

our combined data across all four experiments, where we grouped conditions with the same level of

income volatility. We pooled our conditions from Experiment 2 into a group labelled “Medium

Volatility”, as these participants all received an income sequence with a CV of 0.37—between the

CVs of Experiment 1’s Low Volatility condition (CV = 0.30) and High Volatility condition (CV =

0.60). We then pooled participants’ first attempts from Experiment 3 with their respective Experiment

1 conditions (i.e., Low or High Volatility). Finally, we excluded data from participants’ second

attempts in Experiment 3; our prior results suggested that participants tended to save more on their

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 23 -->

second attempt (regardless of level of income volatility), rendering these data incomparable to our

other conditions, where participants were completing their first or only attempt.11

6.2.1.  Comparison of Very High Volatility to No Volatility

We observed extreme evidence that participants perceived their income to be substantially more

volatile in the Very High Volatility condition (M = 6.79) compared to the No Volatility condition (M =

3.17) (BF10 = 1.03×1013). There was also strong evidence that participants saved more in the Very

High Volatility condition than the No Volatility condition (M = £8,342.80 vs £6,647.88) (BF10 =

10.97).

6.2.2.  Combined analyses on income volatility effect

A Bayesian ANOVA indicated that there was extreme evidence that perceived volatility ratings

differed between income volatility levels (BF10 = 4.62×1025). However, as is evident from Figure 6,

this effect appears to be entirely driven by lower volatility ratings in Experiment 1’s No Volatility

condition. When excluding this condition from the analysis, there was anecdotal evidence that the

remaining conditions did not differ in their volatility ratings (BF01 = 1.41).

Figure 6. Mean perceived volatility ratings by level of income volatility across Experiments 1 to 4.

Standard error bars indicated.

11 We recognise that this pooled analysis approach forgoes random assignment of participants to experiment 
conditions. However, given our experiments drew from the same participant pool, offered similar incentives, 
and were conducted within months of each other, we considered it unlikely that any of our observed results 
would be driven by systematic differences in participant characteristics.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 24 -->

A similar analysis of participants’ final savings yielded inconclusive evidence as to whether

they differed as a function of income volatility level (BF01 = 1.01) (see Figure 7). We thus chose to

exploit the fact that each income volatility level was quantifiable based on its CV and that this could

be treated as a continuous measure. When instead analysing final savings as a function of CV, we

observed very strong evidence that a higher CV was associated with more savings (BF10 = 45.89). A

Bayesian regression approach yielded a median posterior estimate for the CV effect to be £2,134.69.

This suggested that a 0.1 increase in CV corresponded to an average increase in savings of

approximately £213 within our task (95% HDI: [£92, £328]).

Figure 7. Distribution of final savings by level of income volatility across Experiments 1 to 4. Means

and standard error bars indicated.

7.

General Discussion

7.1.

The relationship between income volatility and saving behaviour

Across four experiments, our collective results provide preliminary evidence that people save more

when faced with fluctuations in income and are consistent with the view that uncertainty drives

precautionary savings motives (Carroll & Kimball, 2018). However, the fact that there exists

empirical work supporting both that income uncertainty increases saving behaviour (e.g., Caballero,

1991; Miles, 1997) and decreases saving behaviour (e.g., Cobb-Clark et al., 2016; Perry & Morris,

2005) suggests that the relationship is not so straightforward. Our findings could be interpreted as

indicative of what people intend to do when faced with a volatile income, but not necessarily what

they follow through with—a gap between saving intentions and behaviours (Rabinovich & Webley,

2007).

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 25 -->

By design, our financial decision making task was a highly simplified version of the true

trade-off that people must make between spending and saving for the future. One of the key

differences between our hypothetical setting and the real world was that participants never needed to

worry about their income being insufficient to meet immediate expenses as there were none within

our task; instead, they could afford to entirely focus their attention on the long-term goal (i.e.,

accumulating adequate savings for the emergency). In contrast, in the real world, people with volatile

incomes may be faced with the looming fear that an unanticipated drop in their income may leave

them unable to fulfil their financial obligations. It is perhaps this financial pressure, or the feelings of

stress and scarcity that accompany the pressure, that leads people to overly focus on the short-term

and overrides their underlying intention to save more. One potential hypothesis is therefore that the

experience of income volatility has differential effects on saving behaviour depending on one’s

financial situation (van Schie et al., 2012). The motivation to save more in response to a fluctuating

income may be a luxury for those in strong financial positions who need not be concerned about it

affecting their short-term liquidity.

7.2.

Perceptions of income volatility

Our findings also suggest that income volatility may need to exceed some threshold before it

impacts saving decisions. Within our experimental task, this threshold appeared to be around a

coefficient of variation of 0.60. Below this CV level (i.e., in the Low Volatility condition of

Experiment 1 and the three Experiment 2 conditions), saving behaviour did not differ relative from

participants who received a steady income. At this CV level (i.e., our High Volatility conditions), we

observed inconsistent results—increased saving behaviour in Experiment 1 but not in Experiment 3.

Above this CV level (i.e., in the Very High Volatility condition), we observed the highest amount of

savings. For reference, as noted earlier, the typical household is estimated to experience a CV of

between 0.30 to 0.40.

If such a threshold does exist, this naturally raises the question of how people judge whether

their income is volatile or not. While our results show that CV serves as a reasonable predictor for

participants’ savings within our task, we note three potential extensions upon our work. First, future

work may seek to assess other definitions of volatility, such as the second-order coefficient of

volatility proposed by Kvålseth (2017). Second, there may be opportunities to build upon our second

experiment and further investigate whether other characteristics of income sequences better explain

people’s perceptions of their volatility (Konovalova & Pachur, 2021). Third, it may be worthwhile to

distinguish between income volatility and predictability. For some individuals, income may fluctuate

between pay periods, but in a predictable manner. This may occur if income is correlated with the

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 26 -->

time of year (e.g., seasonal work or annual bonuses) or if individuals have control over how much

they work and therefore their earnings (Peetz et al., 2021).

7.3.

Facilitating intentions to save

Finally, our findings suggest there may be opportunities within the financial sector to better support

consumers whose incomes are volatile. Banks in particular have visibility over their customers’

income and can therefore readily identify which of their customers have highly volatile incomes and

may be motivated to save more. It may be possible to then develop interventions that help consumers

follow through with their intentions. For example, messages could be deployed to customers when a

spike in income is detected (relative to their usual earnings). Such ‘just-in-time’ interventions can be

highly effective (often used in health settings; e.g., Forman et al., 2019; Van Der Laan & Orcholska,

2022); in this case, potentially by combating the natural tendency to spend more of money that is

considered a bonus or windfall (Arkes et al., 1994; Epley & Gneezy, 2007).

8.

Conclusion

Recent economic trends, such as the rapid rise of the gig economy, have made it increasingly common

for individuals to have incomes that are unstable and fluctuate within a year. Our study set out to

investigate how experiencing this income volatility affects saving decisions. Using a novel financial

decision making task, we provide evidence that higher income volatility results in increased saving

behaviour. To the best of our knowledge, our study is the first to address this question experimentally

and offers many fruitful avenues for further research. By improving our understanding of the

relationship between income volatility and saving, we may be able to better tailor financial products

and services for individuals with volatile incomes, and better meet their financial needs.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 27 -->

9.

References

Anvari-Clark, J., & Ansong, D. (2022). Predicting financial well-being using the financial capability

perspective: The roles of financial shocks, income volatility, financial products, and savings

behaviors. Journal of Family and Economic Issues, 43, 730–743.

https://doi.org/10.1007/s10834-022-09849-w

Arkes, H. R., Joyner, C. A., Pezzo, M. V., Nash, J. G., Siegel-Jacobs, K., & Stone, E. (1994). The

psychology of windfall gains. Organizational Behavior and Human Decision Processes,

59(3), 331–347. https://doi.org/10.1006/obhd.1994.1063

Bania, N., & Leete, L. (2009). Monthly household income volatility in the U.S., 1991/92 vs. 2002/03.

Economics Bulletin, 29(3), 2100–2112.

Bania, N., & Leete, L. (2022). Monthly income volatility and health outcomes. Contemporary

Economic Policy, 40(4), 636–658. https://doi.org/10.1111/coep.12580

Caballero, R. J. (1991). Earnings uncertainty and aggregate wealth accumulation. The American

Economic Review, 81(4), 859–871.

Carroll, C. D., & Kimball, M. S. (2018). Precautionary saving and precautionary wealth. In

Macmillan Publishers Ltd (Ed.), The new Palgrave dictionary of economics (pp. 10591–

10599). Palgrave Macmillan UK. https://doi.org/10.1057/978-1-349-95189-5_2079

Chamon, M., Liu, K., & Prasad, E. (2013). Income uncertainty and household savings in China.

Journal of Development Economics, 105, 164–177.

https://doi.org/10.1016/j.jdeveco.2013.07.014

Chapman, G. B. (1996). Temporal discounting and utility for health and money. Journal of

Experimental Psychology: Learning, Memory, and Cognition, 22(3), Article 3.

https://doi.org/10.1037/0278-7393.22.3.771

Cobb-Clark, D. A., Kassenboehmer, S. C., & Sinning, M. G. (2016). Locus of control and savings.

Journal of Banking & Finance, 73, 113–130. https://doi.org/10.1016/j.jbankfin.2016.06.013

Collins, J. M., & Gjertson, L. (2013). Emergency savings for low-income consumers. Focus, 30(1),

12–17.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 28 -->

Diaz-Serrano, L. (2005). Income volatility and residential mortgage delinquency across the EU.

Journal of Housing Economics, 14(3), 153–177. https://doi.org/10.1016/j.jhe.2005.07.003

Drèze, J. H., & Modigliani, F. (1972). Consumption decisions under uncertainty. Journal of Economic

Theory, 5(3), 308–335.

Epley, N., & Gneezy, A. (2007). The framing of financial windfalls and implications for public policy.

The Journal of Socio-Economics, 36(1), 36–47. https://doi.org/10.1016/j.socec.2005.12.012

Farrell, D., & Greig, F. (2016). Paychecks, paydays, and the online platform economy. JPMorgan

Chase Institute. https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-

co/institute/pdf/jpmc-institute-volatility-2-report.pdf

Farrell, D., Greig, F., & Yu, C. (2019). Weathering volatility 2.0: A monthly stress test to guide

savings. JPMorgan Chase Institute.

https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-

co/institute/pdf/institute-volatility-cash-buffer-report.pdf

Faul, F., Erdfelder, E., Lang, A.-G., & Buchner, A. (2007). G*Power 3: A flexible statistical power

analysis program for the social, behavioral, and biomedical sciences. Behavior Research

Methods, 39(2), 175–191. https://doi.org/10.3758/BF03193146

Fawcett, T. W., McNamara, J. M., & Houston, A. I. (2012). When is it adaptive to be patient? A

general framework for evaluating delayed rewards. Behavioural Processes, 89(2), 128–136.

https://doi.org/10.1016/j.beproc.2011.08.015

Forman, E. M., Goldstein, S. P., Crochiere, R. J., Butryn, M. L., Juarascio, A. S., Zhang, F., & Foster,

G. D. (2019). Randomized controlled trial of OnTrack, a just-in-time adaptive intervention

designed to enhance weight loss. Translational Behavioral Medicine, 9(6), 989–1001.

https://doi.org/10.1093/tbm/ibz137

Fox, C. R., & Tversky, A. (1995). Ambiguity aversion and comparative ignorance. The Quarterly

Journal of Economics, 110(3), Article 3. https://doi.org/10.2307/2946693

Fulford, S. L. (2015). The surprisingly low importance of income uncertainty for precaution.

European Economic Review, 79, 151–171. https://doi.org/10.1016/j.euroecorev.2015.07.016

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 29 -->

Gladstone, J., Nieboer, J., & Raghavan, K. (2020). Understanding consumer financial wellbeing

through banking data (No. 58; FCA Occasional Paper). Financial Conduct Authority.

https://www.fca.org.uk/publication/occasional-papers/occasional-paper-58.pdf

Goda, G. S., Levy, M., Manchester, C. F., Sojourner, A., & Tasoff, J. (2019). Predicting retirement

savings using survey measures of exponential-growth bias and present bias. Economic

Inquiry, 57(3), 1636–1658. https://doi.org/10.1111/ecin.12792

Goffin, R. D., & Olson, J. M. (2011). Is it all relative? Comparative judgments and the possible

improvement of self-ratings and ratings of others. Perspectives on Psychological Science,

6(1), 48–60. https://doi.org/10.1177/1745691610393521

Halliday, T. J. (2007). Income volatility and health (No. 3234; IZA Discussion Paper Series). The

Institute for the Study of Labor. https://docs.iza.org/dp3234.pdf

Hannagan, A., & Morduch, J. (2015). Income gains and month-to-month income volatility: Household

evidence from the US Financial Diaries (No. 2659883; NYU Wagner Research Paper).

https://www.financialaccess.org/publications-index/2015/usfd

Haushofer, J., & Fehr, E. (2014). On the psychology of poverty. Science, 344(6186), 862–867.

https://doi.org/10.1126/science.1232491

Hipp, L., Bernhardt, J., & Allmendinger, J. (2015). Institutions and the prevalence of nonstandard

employment. Socio-Economic Review, 13(2), 351–377. https://doi.org/10.1093/ser/mwv002

Kalleberg, A. L., & Hewison, K. (2013). Precarious work and the challenge for Asia. American

Behavioral Scientist, 57(3), 271–288. https://doi.org/10.1177/0002764212466238

Kazarosian, M. (1997). Precautionary savings—A panel study. Review of Economics and Statistics,

79(2), 241–247. https://doi.org/10.1162/003465397556593

Kirby, K. N., & Maraković, N. N. (1995). Modeling myopic decisions: Evidence for hyperbolic delay-

discounting within subjects and amounts. Organizational Behavior and Human Decision

Processes, 64(1), 22–30. https://doi.org/10.1006/obhd.1995.1086

Konovalova, E., & Pachur, T. (2021). The intuitive conceptualization and perception of variance.

Cognition, 217, 104906. https://doi.org/10.1016/j.cognition.2021.104906

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 30 -->

Kvålseth, T. O. (2017). Coefficient of variation: The second-order alternative. Journal of Applied

Statistics, 44(3), 402–415. https://doi.org/10.1080/02664763.2016.1174195

Lee, M. D., & Wagenmakers, E.-J. (2013). Bayesian cognitive modeling: A practical course.

Cambridge University Press.

Leland, H. E. (1968). Saving and uncertainty: The precautionary demand for saving. The Quarterly

Journal of Economics, 82(3), 465. https://doi.org/10.2307/1879518

Lugilde, A., Bande, R., & Riveiro, D. (2019). Precautionary saving: A review of the empirical

literature. Journal of Economic Surveys, 33(2), 481–515. https://doi.org/10.1111/joes.12284

Mani, A., Mullainathan, S., Shafir, E., & Zhao, J. (2013). Poverty impedes cognitive function.

Science, 341(6149), 976–980. https://doi.org/10.1126/science.1238041

Mani, A., Mullainathan, S., Shafir, E., & Zhao, J. (2020). Scarcity and cognitive function around

payday: A conceptual and empirical analysis. Journal of the Association for Consumer

Research, 5(4), 365–376. https://doi.org/10.1086/709885

Miles, D. (1997). A household level study of the determinants of incomes and consumption. The

Economic Journal, 107(440), 1–25. https://doi.org/10.1111/1468-0297.00139

Mills, G. B., & Amick, J. (2010). Can savings help overcome income instability? (Brief 18;

Perspectives on Low-Income Working Families). The Urban Institute.

https://www.urban.org/sites/default/files/publication/32771/412290-Can-Savings-Help-

Overcome-Income-Instability-.PDF

Morris, P., A., Hill, H., D., Gennetian, L., A., Rodrigues, C., & Wolf, S. (2015). Income volatility in

U.S. households with children: Another growing disparity between the rich and the poor?

(No. 1429-15; IRP Discussion Paper). Institute for Research on Poverty.

https://www.irp.wisc.edu/wp/wp-content/uploads/2018/05/dp142915.pdf

Mullainathan, S., & Shafir, E. (2009). Savings policy and decisionmaking in low-income households.

In M. Barr & R. Blank (Eds.), Insufficient funds: Savings, assets, credit and banking among

low-income households (pp. 121–145). Russell Sage Foundation Press.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 31 -->

Nunley, J. M., & Seals, A. (2010). The effects of household income volatility on divorce. American

Journal of Economics and Sociology, 69(3), 983–1010. https://doi.org/10.1111/j.1536-

7150.2010.00731.x

Peetz, J., Robson, J., & Xuereb, S. (2021). The role of income volatility and perceived locus of

control in financial planning decisions. Frontiers in Psychology, 12, 638043.

https://doi.org/10.3389/fpsyg.2021.638043

Pepper, G. V., & Nettle, D. (2017). The behavioural constellation of deprivation: Causes and

consequences. Behavioral and Brain Sciences, 40, e314.

https://doi.org/10.1017/S0140525X1600234X

Perry, V. G., & Morris, M. D. (2005). Who is in control? The role of self-perception, knowledge, and

income in explaining consumer financial behavior. Journal of Consumer Affairs, 39(2), 299–

313. https://doi.org/10.1111/j.1745-6606.2005.00016.x

Prause, J., Dooley, D., & Huh, J. (2009). Income volatility and psychological depression. American

Journal of Community Psychology, 43(1–2), 57–70. https://doi.org/10.1007/s10464-008-

9219-3

Rabinovich, A., & Webley, P. (2007). Filling the gap between planning and doing: Psychological

factors involved in the successful implementation of saving intention. Journal of Economic

Psychology, 28(4), 444–461. https://doi.org/10.1016/j.joep.2006.09.002

Rosenbaum, P. R. (2015). How to see more in observational studies: Some new quasi-experimental

devices. Annual Review of Statistics and Its Application, 2(1), 21–48.

https://doi.org/10.1146/annurev-statistics-010814-020201

Sandmo, A. (1970). The effect of uncertainty on saving decisions. The Review of Economic Studies,

37(3), 353. https://doi.org/10.2307/2296725

Sayre, G. M. (2022). The costs of insecurity: Pay volatility and health outcomes. Journal of Applied

Psychology. Advance online publication. https://doi.org/10.1037/apl0001062

Schwabe, L., & Wolf, O. T. (2009). Stress prompts habit behavior in humans. The Journal of

Neuroscience, 29(22), 7191–7198. https://doi.org/10.1523/JNEUROSCI.0979-09.2009

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 32 -->

Senate Select Committee on Job Security. (2022). The job insecurity report.

https://parlinfo.aph.gov.au/parlInfo/download/committees/reportsen/024780/toc_pdf/Thejobin

securityreport.pdf;fileType%3Dapplication%2Fpdf

Shapiro, J., & Wu, S. (2011). Fatalism and savings. The Journal of Socio-Economics, 40(5), 645–651.

https://doi.org/10.1016/j.socec.2011.05.003

Smith, C. L., & Hantula, D. A. (2008). Methodological considerations in the study of delay

discounting in intertemporal choice: A comparison of tasks and modes. Behavior Research

Methods, 40(4), 940–953. https://doi.org/10.3758/BRM.40.4.940

Stewart, N., Chater, N., & Brown, G. D. A. (2006). Decision by sampling. Cognitive Psychology,

53(1), 1–26. https://doi.org/10.1016/j.cogpsych.2005.10.003

Van Den Bergh, D., Van Doorn, J., Marsman, M., Draws, T., Van Kesteren, E.-J., Derks, K.,

Dablander, F., Gronau, Q. F., Kucharský, Š., Gupta, A. R. K. N., Sarafoglou, A., Voelkel, J.

G., Stefan, A., Ly, A., Hinne, M., Matzke, D., & Wagenmakers, E.-J. (2020). A tutorial on

conducting and intepreting a Bayesian ANOVA in JASP. L’Année Psychologique, 120(1), 73–

96. https://doi.org/10.3917/anpsy1.201.0073

Van Der Laan, L. N., & Orcholska, O. (2022). Effects of digital just-in-time nudges on healthy food

choice – A field experiment. Food Quality and Preference, 98, 104535.

https://doi.org/10.1016/j.foodqual.2022.104535

van Schie, R. J. G., Donkers, B., & Dellaert, B. G. C. (2012). Savings adequacy uncertainty: Driver or

obstacle to increased pension contributions? Journal of Economic Psychology, 33(4), Article

4. https://doi.org/10.1016/j.joep.2012.04.004

Wang, S., Li, L. Z., & Coutts, A. (2022). National survey of mental health and life satisfaction of gig

workers: The role of loneliness and financial precarity. BMJ Open, 12(12), e066389.

https://doi.org/10.1136/bmjopen-2022-066389

Wang-Ly, N., & Newell, B. R. (2022). Allowing early access to retirement savings: Lessons from

Australia. Economic Analysis and Policy, 75, 716–733.

https://doi.org/10.1016/j.eap.2022.07.002

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 33 -->

Weatherly, J. N., Terrell, H. K., & Derenne, A. (2010). Delay discounting of different commodities.

The Journal of General Psychology, 137(3), 273–286.

https://doi.org/10.1080/00221309.2010.484449

West, C., Whillans, A., & DeVoe, S. (2020). Income volatility increases financial impatience (No. 21–

053; Working Paper). Harvard Business School.

https://www.hbs.edu/ris/Publication%20Files/21-053_54843a1e-7599-4981-a829-

bac3234830cc.pdf

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 34 -->

ONLINE APPENDIX

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 35 -->

Appendix A – Demographic and financial characteristics of our samples

Table A1. Demographic characteristics of samples in Experiments 1 to 4.

N

Age (%)

18-24 years old

25-34 years old

35-44 years old

45-54 years old

55-64 years old

65 years or older

Prefer not to say

Gender (%)

Male

Female

Non-binary/Gender fluid

Different identity

Prefer not to say

Education level (%)

Did not complete high school

High school graduate

Undergraduate degree (e.g., Bachelor’s degree)

Postgraduate degree (e.g., Master’s or Doctoral degree)

Prefer not to say

Note. Percentages are rounded and may not sum to 100 percent.

Exp 1

Exp 2

Exp 3

Exp 4

241

241

150

80

11.6

27.4

26.1

20.3

13.7

0.8

0.0

59.8

39.4

0.4

0.4

0.0

0.8

36.1

45.2

17.4

0.4

10.8

27.4

28.2

20.3

12.4

0.8

0.0

44.8

53.9

0.8

0.0

0.4

1.2

41.1

37.8

19.1

0.8

9.3

34.7

24.0

20.0

12.0

0.0

0.0

50.0

49.3

0.7

0.0

0.0

1.3

42.0

40.7

16.0

0.0

17.5

25.0

31.2

17.5

6.3

1.3

1.3

42.5

57.5

0.0

0.0

0.0

2.5

35.0

31.2

30.0

1.3

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 36 -->

Table A2. Financial characteristics of samples in Experiments 1 to 4.

N

Employment status (%)

Full-time

Part-time

Contract/Temporary

Student

Unemployed

Unable to work

Other

Prefer not to say

Pay frequency

Weekly

Fortnightly

Monthly

Other

Not applicable

Prefer not to say

Annual personal income (%)

Negative or nil income

£0-£9,999

£10,000-£19,999

£20,000-£29,999

£30,000-£39,999

£40,000-£49,999

£50,000-£59,999

£60,000-£69,999

£70,000 or more

Prefer not to say

Exp 1

241

Exp 2

241

Exp 3

150

Exp 4

80

61.0

16.2

2.5

4.2

5.0

5.0

5.0

1.7

10.0

5.0

72.2

4.2

7.1

1.7

1.7

16.6

16.2

20.3

16.2

8.7

5.8

3.3

5.4

5.8

52.7

20.3

1.7

6.2

8.3

2.5

7.8

0.4

11.6

2.1

68.5

5.8

10.8

1.2

4.6

15.8

14.1

25.7

13.3

5.8

4.2

4.2

4.6

7.9

55.3

16.0

0.0

3.3

13.3

4.7

7.3

0.0

8.0

2.7

68.0

5.3

15.3

0.7

4.0

18.0

16.7

25.3

14.0

7.3

4.7

2.7

1.3

6.0

48.8

21.2

1.3

10.0

6.3

6.3

5.0

1.3

7.5

1.3

62.5

3.8

18.8

6.3

6.3

17.5

11.2

20.0

15.0

10.0

1.3

5.0

7.5

6.3

Note. Percentages are rounded and may not sum to 100 percent.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 37 -->

Appendix B – Summary of income sequences used across Experiments 1 to 4

Table B1. Dimensions of income sequences used across Experiments 1 to 4.

Condition

Incomes (£)

CV

Min

Max

Range

No Volatility

1,000 1,000 1,000 1,000 1,000

0.00

1,000

1,000

0

1,000 1,000 1,000 1,000 1,000

1,000 1,000 1,000 1,000 1,000

Low Volatility

431 570 656 794 873

0.30

431

1,340

909

883 910 990 1,158 1,202

1,277 1,279 1,311 1,326 1,340

High Volatility

173 274 466 526 529

0.60

173

2,088

1,915

650 661 847 1,101 1,374

1,404 1,436 1,571 1,900 2,088

Same Range

173 881 911 929 946

0.37

173

2,088

1,915

952 956 981 989 996

1,022 1,041 1,063 1,072 2,088

Same Min

173 552 654 851 863

0.37

173

1,580

1,407

864 889 1,017 1,036 1,211

1,240 1,257 1,310 1,503 1,580

Same Max

681 689 746 767 772

0.37

681

2,088

1,407

782 785 816 983 994

1,029 1,242 1,275 1,351 2,088

Very High Volatility

44 152 184 299 372

536 763 767 788 1,101

1,300 1,618 1,654 1,965 3,457

Note. CV = Coefficient of variation. Min = Minimum income. Max = Maximum income.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 38 -->

Appendix C – Experimental instructions for financial decision making task

The following instructions were given to participants in Experiments 1, 2, and 4. Horizontal rules are

used to indicate different instruction screens.

About this study

•  This study is being run by UNSW Sydney to investigate how people make financial

decisions when faced with uncertainty.

•  You will make decisions around spending and saving in a financial decision making game,

as well as answer some simple questionnaires.

•  You will receive £3.00 for participating in this experiment and may be eligible for a bonus

payment of £3.00 depending on your performance in the game.

How this experiment will run:

•  You will first be presented instructions that explain how the financial decision making

game works.

•  You will then be given a few practice rounds to get familiar with the game.

•  After the practice rounds, you will begin the real experiment rounds.

•  Finally, you will be asked to provide some information about yourself and your financial

situation.

•  The experiment should take about 20 minutes to complete. If you have any questions or

issues during or after the experiment, please contact Nathan Wang-Ly (nathan.wang-

ly@unsw.edu.au).

•  Press the Continue button to proceed to the consent form for this experiment.

How the Game Works – Working for Income

The game will consist of multiple rounds where you will be asked to complete work tasks. Your task

each round will be to arrange a sequence of letters in alphabetical order (see example image

below). After completing each work task, you will receive money as your income.

How the Game Works – Spending or Saving

Each time you receive your income, you will be asked to decide how much of your money you want

to spend or save. You can spend your money to buy points (1 point per £1 spent). These points will

be used to determine whether you are eligible for a bonus payment. Any money that you don't spend

will remain in your account as savings and carry over to future rounds.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 39 -->

How the Game Works – The Financial Emergency

At the end of the game, a financial emergency will occur that you will need to pay for. If you have

enough saved in your account when this happens, you will win the game and get to keep your

points. However, if you do not have enough saved, you will lose the game and lose all your points.

How the Game Works – Bonus Payment

Once we have finished collecting data for this experiment, the best performing participants (top

10% of scores) will receive a bonus payment of £3.00 in addition to their participation payment.

Your goal is therefore to buy as many points as you can while still making sure you have enough

saved for the financial emergency. Remember: You will not be told when this emergency will occur

nor how much it will cost.

You will now get to play a few practice rounds to become familiar with how everything works. Just

like in the real game, a financial emergency will occur at the end of these rounds. Once you finish

with the practice rounds, the points you have earned and your account balance will be reset, and

you will begin the experiment rounds. Click Continue when you are ready to begin.

[After practice rounds had been completed]

Thank you for completing the practice rounds. You will now begin the real experiment rounds. Your

points and savings balance have been reset to zero. The number of rounds and the cost of the

financial emergency will be different for the experiment stage. Your goal remains the same: To buy

as many points as you can while making sure you have enough saved for the financial emergency.

Important: You will later be asked questions about the income you received and your decisions to

spend or save so please ensure you are paying attention throughout the game.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 40 -->

The following instructions were given to participants in Experiment 3. Horizontal rules are used to

indicate different instruction screens.

About this study

•  This study is being run by UNSW Sydney to investigate how people make financial

decisions when faced with uncertainty.

•  You will make decisions around spending and saving in a financial decision making game,

as well as answer some simple questionnaires.

•  You will receive £4.50 for participating in this experiment and may be eligible for a bonus

payment of £3.00 depending on your performance in the game.

How this experiment will run:

•  You will first be presented instructions that explain how the financial decision making

game works.

•  You will then be given a few practice rounds to get familiar with the game.

•  After the practice rounds, you will be given the opportunity to play the game twice.

•  Finally, you will be asked to provide some information about yourself and your financial

situation.

•  The experiment should take about 30 minutes to complete. If you have any questions or

issues during or after the experiment, please contact Nathan Wang-Ly (nathan.wang-

ly@unsw.edu.au).

•  Press the Continue button to proceed to the consent form for this experiment.

How the Game Works – Working for Income

The game will consist of multiple rounds where you will be asked to complete work tasks. Your task

each round will be to arrange a sequence of letters in alphabetical order (see example image

below). After completing each work task, you will receive money as your income.

How the Game Works – Spending or Saving

Each time you receive your income, you will be asked to decide how much of your money you want

to spend or save. You can spend your money to buy points (1 point per £1 spent). These points will

be used to determine whether you are eligible for a bonus payment. Any money that you don't spend

will remain in your account as savings and carry over to future rounds.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 41 -->

How the Game Works – The Financial Emergency

At the end of the game, a financial emergency will occur that you will need to pay for. If you have

enough saved in your account when this happens, you will win the game and get to keep your

points. However, if you do not have enough saved, you will lose the game and lose all your points.

How the Game Works – Two Attempts

You will be given the opportunity to play the game twice. The timing and cost of the financial

emergency may be different between attempts. The income you receive may also differ. The cost of

the financial emergency and the outcome of each game will only be revealed once you have

completed both attempts. However, your performance in your first attempt will not affect the second

attempt. Your points and savings will be reset to zero in between attempts.

How the Game Works – Bonus Payment

After you have completed both attempts, we will add up your points from each attempt to give a

final score for the experiment. If your final score is within the top 10% of participants who

complete this experiment, you will receive a bonus payment of £4.50 in addition to your

participation payment.

You will now get to play a few practice rounds to become familiar with how everything works. Just

like in the real game, a financial emergency will occur at the end of these rounds. Once you finish

with the practice rounds, the points you have earned and your account balance will be reset, and

you will begin your first attempt at the game. Click Continue when you are ready to begin.

[After practice rounds had been completed]

Thank you for completing the practice rounds. You will now begin your first attempt at the game.

Your points and savings balance have been reset to zero. The number of rounds and the cost of the

financial emergency will be different for the experiment stage. Your goal remains the same: To buy

as many points as you can while making sure you have enough saved for the financial emergency.

Important: You will later be asked questions about the income you received and your decisions to

spend or save so please ensure you are paying attention throughout the game.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 42 -->

[After participants provided responses to the perceived income volatility measure for their first task

attempt]

Thank you for answering the question. Your performance in the first attempt has been recorded and

we will now begin the second attempt when you press the button below. As this is a new attempt,

your points and savings balance have been reset to zero. Your goal remains the same: To buy as

many points as you can while making sure you have enough saved for the financial emergency.

Remember: The timing and cost of the financial emergency may be different for this attempt. The

income you receive may also differ.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 43 -->

Appendix D – Select screenshots of financial decision making task

Figure D1. Introduction to the experimental study.

Figure D2. Example “work task” where participants rearranged a six-character string of letters into

alphabetical order.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 44 -->

Figure D3. Example of participant receiving income upon completion of their work task.

Figure D4. Example of participant deciding how much of their available funds to use on purchasing

points.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 45 -->

Figure D5. Example feedback screen indicating how many points participants had purchased, their

new points total, and their remaining savings.

Figure D6. Perceived income volatility rating scale. Slider was set by default at 5 but was required to

be moved to progress to the next screen.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 46 -->

Figure D7. Perceived financial difficulty rating scale. Slider was set by default at 5 but was required

to be moved to progress to the next screen.

Figure D8. Financial impatience measure requiring participants to provide a hypothetical ‘smaller-

sooner’ amount that would be preferred immediately over a larger later payment.

Electronic copy available at: https://ssrn.com/abstract=4509925

---

<!-- PAGE 47 -->

Figure D9. Announcement of the financial emergency occurring.

Figure D10. Outcome screen for a participant who won by saving adequately for the emergency.

Participants who lost were shown a similar screen but were advised that they had lost their purchased

points.

Electronic copy available at: https://ssrn.com/abstract=4509925

<!-- MARKITDOWN CONVERSION -->

<!-- The following is the full MarkItDown conversion for formatting fidelity. -->

How Income Volatility Influences Saving Decisions: Evidence from the Lab
Nathan Wang-Ly*,1, Ben R. Newell1,2
1 School of Psychology, UNSW Sydney, NSW 2052, Australia
2 UNSW Institute of Climate Risk & Response, UNSW Sydney, NSW 2052, Australia
* Corresponding author (Email: nathan.wang-ly@unsw.edu.au).
July 16, 2023
Electronic copy available at: https://ssrn.com/abstract=4509925

Abstract
Around the world, it is becoming increasingly common for individuals to have volatile incomes,
which fluctuate from pay to pay. Previous research offers mixed evidence as to whether this
uncertainty about one’s income may increase or decrease saving behaviour. Across four incentivised
online experiments (N = 712), we examine the relationship between income volatility and saving
behaviour using a novel financial decision making task. In this task, participants receive hypothetical
income that is either consistent or that varies to different degrees. We capture participants’ perceptions
of how volatile their income is and observe how this influences their decision to spend this income or
save it towards an impending emergency. Our results indicate that receiving a more volatile income,
as measured by its coefficient of variation (CV), leads to higher savings within our task (£213 more
saved per 0.1 increase in CV). However, there appears to be a threshold level of volatility that must be
exceeded before participants save differently relative to receiving a stable income.
Keywords: Income volatility, Precautionary saving, Uncertainty, Financial decision making
PSYCInfo classification: 3900, 3920
JEL classification: D14, G51
Electronic copy available at: https://ssrn.com/abstract=4509925

1. Introduction
No one can be certain about how much they will earn in the future. However, not all uncertainties are
equal; some individuals have greater confidence in their future incomes than others. An individual
working in a traditional salaried role can reasonably expect to earn the same amount each pay cycle.
In contrast, an individual who is employed casually or who freelances may find that their earnings
fluctuate unpredictably. Around the world, economic trends suggest that this latter scenario is
becoming increasingly common. In Australia, permanent full-time employment rates have declined
from previous decades, insecure part-time employment has become prevalent, and there has been a
dramatic rise in platform work (often referred to as ‘gig work’) (Senate Select Committee on Job
Security, 2022). Similar trends have been observed across other advanced economies in Asia and
Europe (Hipp et al., 2015; Kalleberg & Hewison, 2013).
Previous research has identified numerous ways in which income uncertainty may negatively
impact individuals’ and their families’ lives. Experiencing fluctuations in income has been associated
with psychological depression (Prause et al., 2009), higher risk of mortality (Halliday, 2007), greater
risk of divorce (Nunley & Seals, 2010), and increased probability of mortgage default (Diaz-Serrano,
2005). Much of this research has been based on ‘inter-year’ income volatility (income that varies
between years), with research on ‘intra-year’ income volatility (income that varies within a year)
being comparatively scarce. Only recently has there been an increase in studies examining how
financial and health outcomes are influenced by monthly fluctuations in income (e.g., Anvari-Clark &
Ansong, 2022; Gladstone et al., 2020), many of which have been motivated by the growth of the gig
economy (e.g., Sayre, 2022; Wang et al., 2022), as well as the severe disruption to income caused by
the COVID-19 pandemic (Wang-Ly & Newell, 2022). However, given the challenges of manipulating
income in real-world settings, these studies have typically been observational in nature. These
observational studies are inherently limited in their ability to prove causal links between the
experience of income volatility and outcomes of interest (Rosenbaum, 2015).
To our knowledge, only two studies have investigated the influence of intra-year income
volatility via experimental methods, with both finding evidence suggesting that volatility drives
individuals to behave in a more financially impatient manner. The first study involved providing
income spikes to Kenyan participants via an unconditional cash transfer program (West et al., 2020).
Financial impatience was measured by giving participants multiple hypothetical choices between a
‘smaller-sooner’ reward (e.g., KSH 500 today) and a ‘larger-later’ reward (e.g., KSH 525 in six
months). Participants who received the income spikes tended to choose the smaller-sooner option
more often compared to those who did not receive the spikes, demonstrating a greater degree of
financial impatience. In the second study, participants completed simulated work tasks for
hypothetical income as part of a lab-based experiment (Peetz et al., 2021). Participants either received
Electronic copy available at: https://ssrn.com/abstract=4509925

a stable income (the same income per work task) or a volatile income (income that varied between
work tasks). At the end of the experiment, participants who received the volatile income were more
likely to choose the smaller-sooner participation reward (USD 15 today vs USD 17 in two weeks)
compared to those who had received the stable income.
Inspired by these two studies, we saw an opportunity to apply a similar experimental
approach to better understand how income volatility influences key household financial decisions. In
the present research, we chose to focus our attention on saving behaviour for two reasons. First,
income uncertainty tends to be more severe for individuals in poorer financial circumstances (Bania &
Leete, 2022). For these individuals, the ability to accumulate savings and create ‘financial slack’ is
especially critical for meeting unexpected expenses and avoiding debt (Mullainathan & Shafir, 2009).
Second, the literature offers conflicting perspectives on whether income volatility should increase or
decrease saving behaviour, meaning our work could offer useful clarifying evidence.
On the one hand, the argument that experiencing income volatility increases saving behaviour
seems intuitive. To illustrate, imagine that you wanted to accumulate a certain amount of savings for
future needs (e.g., a holiday or to buffer against future emergencies). If you earned a steady and
predictable income, a prudent strategy might involve setting aside a consistent amount of money such
that you would achieve the goal within your desired timeframe. Now suppose that your income was
instead volatile and unpredictable. The consistent saving strategy would no longer be feasible; instead,
it might be necessary to save more to insure against a potential dip in future income. This is the basic
premise underlying the traditional economic perspective of how income volatility should affect saving
behaviour. Early theoretical work suggested that being uncertain about one’s future earnings should
boost precautionary saving motives (Drèze & Modigliani, 1972; Leland, 1968; Sandmo, 1970). This
view has been supported by numerous empirical studies (for an overview, see Lugilde et al., 2019).1
For example, one study involving US personal income data found that doubling the level of income
uncertainty of an individual or household was associated with a 29 percent increase in their ratio of
wealth to income (i.e., a greater saving rate) (Kazarosian, 1997).
On the other hand, there are several valid reasons why income volatility might instead be
expected to reduce saving behaviour. First, if income volatility results in greater financial impatience
(Peetz et al., 2021; West et al., 2020), individuals may be biased towards actions that offer immediate
benefits (spending) over actions that offer benefits in the distant future (saving). This would be
consistent with previous work showing that more present-focused time preferences are associated
with lower retirement savings balances (Goda et al., 2019). Second, experiencing income volatility
may induce feelings of stress or scarcity, as dips in income can create temporary shortfalls between
1 However, see Fulford (2015) for evidence that income uncertainty is not an important motive for precautionary
saving.
Electronic copy available at: https://ssrn.com/abstract=4509925

available funds and upcoming expenses, forcing individuals to make difficult trade-offs between their
immediate and future needs (Bania & Leete, 2022). Both stress and scarcity have been found to
impair long-term and goal-directed decision making (Haushofer & Fehr, 2014; Mani et al., 2013,
2020; Schwabe & Wolf, 2009), providing additional reason to believe that income volatility might
reduce one’s propensity to save. Third, individuals may decide to save less as part of a considered
choice to abandon (or at least heavily discount) their focus on the long-term. They may instead shift
their focus to achieving short-term outcomes, where the associated rewards are typically better
defined and allow for earlier gratification—an approach that has been argued to be a rational response
to uncertainty (Fawcett et al., 2012; Pepper & Nettle, 2017). Consistent with this view, numerous
studies have shown that saving rates are negatively impacted when individuals feel a lack of control
over their future circumstances (Cobb-Clark et al., 2016; Perry & Morris, 2005; Shapiro & Wu, 2011).
2. Overview of studies
To assess the merit of these opposing perspectives, we conducted four laboratory-based experiments
in which we manipulated the volatility of participants’ income and observed how this affected the way
they traded off between spending and saving. All four experiments involved a novel financial decision
making task where participants received hypothetical income for completing work tasks (similar to
Peetz et al., 2021) and could choose between spending their earnings or saving for an impending
emergency.
In Experiment 1, we tested three levels of income volatility (including no volatility) and
observed the highest saving rates from participants whose income was most volatile. However, we
also observed a discrepancy between participants’ self-reported perceptions of how volatile their
income was and their observed saving behaviour. Experiment 2 examined whether this was because
participants’ saving behaviour was instead being driven by other dimensions of the income sequence
(e.g., the minimum income received). Experiment 3 provided evidence that the discrepancy was due
to participants being asked to provide an absolute judgment of volatility; participants were able to
distinguish between levels of volatility when instead making relative judgments. Finally, in
Experiment 4, we tested a single condition in which we made participants’ income even more volatile
than the most volatile condition in Experiment 1. This established a clearer relationship between
income volatility and increased saving behaviour while also suggesting the existence of a volatility
threshold that needed to be exceeded for saving behaviour to be influenced.
Our study seeks to make several contributions to the literature. First, we continue to expand
the body of experimental work examining the effect of income volatility on financial decisions. We
offer experimental evidence in support of the view that experiencing volatile income increases saving
behaviour. Second, we examine the impact of different degrees of income volatility, allowing us to
Electronic copy available at: https://ssrn.com/abstract=4509925

investigate not only on the extensive margin of the income volatility effect, but also the intensive
margin. Third, we offer a novel financial decision making task that has potential for reuse in future
income volatility experiments or could be adapted to answer similar questions around influences on
saving behaviour.
3. Experiment 1
The purpose of Experiment 1 was to examine how participants’ saving behaviour within our financial
decision making task was influenced by the level of income volatility they experienced. We generated
different sequences of income that varied in their coefficients of variation (CV). CV is a commonly
referenced measure of income volatility (Bania & Leete, 2009; Farrell & Greig, 2016; Hannagan &
Morduch, 2015) that can be calculated by dividing the standard deviation of a sequence by its mean.
Therefore, the larger the CV value, the more volatile the income. One advantage of the CV metric is
that it provides a standardised value that allows for comparison across incomes that may differ in
magnitude, frequency, and timing.2 For Experiment 1, we tested three income sequences with CV
values of 0 (i.e., no volatility), 0.30 and 0.60.
3.1. Method
3.1.1. Participants
We recruited 241 participants3 (M = 39.65 years; 144 males; 95 females; 1 non-binary; 1 preferred
age
not to say) from Prolific Academic, an online participant recruitment platform. Our sample size was
based on an a priori power analysis conducted using statistical software G*Power (Faul et al., 2007)
based on detecting a small effect in a between-subjects study (𝛿 = .80; 𝛾 = .20; 𝛼 = .05). To be eligible
for our sample, participants needed to be between the ages of 18 and 65, located in the UK, and fluent
in English. Participants received £3.00 (USD 3.77) in exchange for their participation and were also
eligible for an additional bonus of £3.00 (USD 3.77) based on their performance in the financial
decision making task. Additional details on the demographic and financial characteristics of our
participant samples for each experiment are provided in the Online Appendix.
2 However, see Kvålseth (2017) for an alternative measure of volatility (the ‘second-order coefficient of
variation’) that has additional useful properties such as being restricted between zero and one, and being less
sensitive to outliers.
3 In both Experiments 1 and 2, we encountered an issue during data collection which led to having one
participant more than was intended.
Electronic copy available at: https://ssrn.com/abstract=4509925

3.1.2. Materials
The financial decision making task4 used in Experiment 1 involved completing work tasks for
hypothetical income and making decisions around spending and saving for an impending emergency.
In each round of the game, participants were asked to rearrange a six-character string of letters (e.g.,
“hksykjl”) into alphabetical order as their work task. Upon completion, they received income and
were asked how much they wanted to spend. Money could be spent to purchase points (£1.00 = 1
point), which were later used to determine eligibility for the bonus performance-based payment.5 Any
money that was not spent remained as savings and was carried over into subsequent rounds, where it
could again be spent or saved.
The income participants received for their work tasks varied depending on which of the three
experimental conditions they were allocated to: No Volatility (n = 81), Low Volatility (n = 80), and
High Volatility (n = 80). In all three conditions, participants received the same total income across the
15 task rounds: £15,000. However, the extent to which their income fluctuated differed. In the No
Volatility condition, participants received £1,000 after each work task—corresponding to a CV of 0.
In the Low Volatility condition, participants’ income ranged between £431 and £1,340, with the
overall sequence of incomes having a CV of 0.30.6 In the High Volatility condition, incomes ranged
between £173 and £2,088, with a CV of 0.60. For participants in the Low and High Volatility
conditions, the order in which they received the different incomes was randomised. For more details
on the income sequences used across the experiments, see the Online Appendix.
At the end of the task (after the 15th round), participants encountered a financial emergency:
home repairs costing £4,500 that had resulted from storm damages. When this emergency occurred, if
participants had adequate savings, they “won” the task, meaning they could keep the points they had
purchased. However, if participants’ savings were inadequate, they lost all their purchased points.
Importantly, while participants were advised at the start of the task that there would be a financial
emergency, they were not told when it would occur nor how much it would cost. Therefore, their
objective was to balance the competing goals of maximising points purchased (to potentially earn the
bonus payment) while ensuring they saved enough to withstand the financial emergency (to avoid
losing their points).
Just prior to revealing the cost of the financial emergency, participants were asked to provide
a series of responses. This timing was deliberate such that participants’ responses would not be
4 Experimental instructions and select screenshots of the task are provided in the Online Appendix. Code for the
task is available in the Supplementary Materials (https://osf.io/pqgha/).
5 Participants were eligible for a bonus payment (in addition to their participation payment) if their final score in
the task was within the top 10 percent of their experimental condition.
6 Previous work has estimated that the average household experiences a CV of between 0.30 to 0.40 (Farrell et
al., 2019; Hannagan & Morduch, 2015); however, this varies substantially between lower- and higher-income
households (Mills & Amick, 2010; Morris et al., 2015).
Electronic copy available at: https://ssrn.com/abstract=4509925

affected by the outcome of the experiment (i.e., whether they had saved adequately). Participants were
asked to rate how volatile they perceived their income to have been during the task (0 = “Not
Volatile”; 10 = “Extremely volatile”). Participants were advised that they could think of volatility as a
reflection of how well they could predict their income if there was an additional round (Konovalova
& Pachur, 2021). We similarly asked participants to rate how difficult it was to decide how much to
spend or save each round (0 = “Not difficult”; 10 = “Extremely difficult”). Finally, we measured
financial impatience using the ‘fill-in-the-blank’ approach (Smith & Hantula, 2008), which has been
previously used in studies involving delay discounting (Chapman, 1996; Kirby & Maraković, 1995;
Weatherly et al., 2010). Participants were instructed to imagine that they were given the choice
between two bonus rewards for their involvement in the experiment. The first option was to receive
£50 in two weeks’ time. Alternatively, they could opt for an immediate reward. Participants were
asked to indicate the lowest amount they would accept immediately (‘smaller-sooner amount’) that
would make it preferable to the larger, delayed reward. The response was bounded between £0 and
£50, with a lower smaller-sooner amount indicating a higher degree of financial impatience.
3.1.3. Procedure
Participants were advised that they would be playing a financial decision making game and received
instructions outlining the work tasks and the objective of the game. This was followed by a practice
stage which included three practice rounds (with income of £50 per work task) and a practice
financial emergency (a £50 parking ticket fine).
After the practice stage, participants’ savings and points were reset to zero and they began the
15 experiment rounds. Once the experiment rounds were complete, participants were informed that
the financial emergency was about to occur and were asked to provide responses to perceived
volatility, perceived difficulty, and financial impatience measures described in the previous section.
Following this, the cost of the emergency was revealed, and participants were advised of the outcome
of the game. Finally, participants were asked to provide information about their demographics and
financial situations before receiving a debrief of the experiment.
3.2. Results
For all four experiments, we conducted Bayesian statistical analyses (using default priors) and report
the Bayes factors (BF ) associated with our results. In cases where the Bayes factor was less than one
10
(i.e., evidence favoured the null hypothesis), we reported the inverse Bayes factor (BF ) to assist with
01
comparability of evidence strength. Interpretations of Bayes factors were based on guidelines
suggested in Lee and Wagenmakers (2013). Unless indicated otherwise, analyses of variance
(ANOVAs) were used for overall tests of differences across multiple conditions and t-tests were used
Electronic copy available at: https://ssrn.com/abstract=4509925

for pairwise comparisons between conditions. Our experiment data and code have been made
available in the Supplementary Materials (https://osf.io/pqgha/).
3.2.1. Perceived volatility ratings
We first examined whether there were differences between conditions in participants’ ratings of how
volatile their income was (‘perceived volatility ratings’). As seen in Figure 1, our analysis indicated
that there was extreme evidence that perceived volatility ratings differed between conditions (BF =
10
6.72×1013), suggesting that our income volatility manipulation had worked. This difference was
driven by substantially lower volatility ratings in the No Volatility condition (M = 3.17) compared to
the Low Volatility (M = 6.00) and High Volatility (M = 6.40) conditions (BF = 2.04×108 and
10
1.11×1011 respectively). However, there was moderate evidence suggesting that perceived volatility
ratings did not differ between the Low and High Volatility conditions (BF = 3.15).
01
Figure 1. Mean perceived volatility ratings by level of income volatility in Experiment 1. Standard
error bars indicated.
3.2.2. Final savings
We next analysed how much participants had saved at the end of the task (‘final savings’). As seen in
Figure 2, we observed very strong evidence that final savings differed between conditions (BF =
10
38.71). Participants saved substantially more in the High Volatility condition (M = £8,571.64)
compared to the No Volatility (M = £6,647.88) and Low Volatility (M = £6,579.54) conditions (BF =
10
Electronic copy available at: https://ssrn.com/abstract=4509925

33.67 and 24.23 respectively). However, there was moderate evidence suggesting that final savings
did not differ between the No and Low Volatility conditions (BF = 5.84).
01
Figure 2. Distribution of final savings by level of income volatility in Experiment 1. Means and
standard error bars indicated.
3.2.3. Perceived difficulty and financial impatience
We then examined participants’ ratings of how difficult they found it to decide how much to spend or
save throughout the task (‘perceived difficulty’). There was moderate evidence that these ratings did
not differ between conditions (BF = 6.44). The mean rating provided across the conditions was 4.07
01
(out of 10). Likewise, there was moderate evidence that financial impatience did not vary between
conditions, as measured via participants’ smaller-sooner amounts (BF = 7.67). The mean amount
01
participants were willing to accept immediately instead of a £50 reward in two weeks’ time was
£37.60.
3.3. Discussion
Our results indicated that participants saved substantially more in the High Volatility
condition than the No and Low Volatility conditions—consistent with the view that income volatility
increases savings motives. However, we did not observe the same boost in savings for the Low
Volatility condition relative to the No Volatility condition. The simplest explanation would be that
participants’ income was volatile enough to impact their saving behaviour in the High Volatility
condition but was not volatile enough to do so in the Low Volatility condition. This would imply that
Electronic copy available at: https://ssrn.com/abstract=4509925

there exists a threshold between the CVs we used (0.30 for Low Volatility; 0.60 for High Volatility)
which must be surpassed before a change in saving behaviour would be observed. However,
complicating this explanation was the fact that participants in the Low and High Volatility conditions
reported their income as being similarly volatile (based on their perceived volatility ratings). The
question we thus needed to address was why participants in the Low Volatility condition did not save
differently (relative to the No Volatility condition) despite perceiving their income to be as volatile as
the High Volatility condition.
One possibility we considered was whether the increased saving behaviour observed from
participants in the High Volatility condition was being driven by something other than income
volatility (as defined by CV). This idea was inspired by recent work which showed that individuals’
perceptions of a number sequence’s variance is not always perfectly related to the objective statistical
variance of the sequence (Konovalova & Pachur, 2021). In their study, Konovalova and Pachur (2021)
examined how other characteristics of a number sequence (e.g., mean, range, pairwise distance)
contributed to perceptions of variance. The study found that a sequence’s range often served as a
better individual predictor of participants’ perceptions of variance than statistical variance itself.
This led us to examine in Experiment 2 whether three other dimensions of the income
sequences we gave participants could better account for their saving behaviour: the minimum income
participants received during the task, the maximum income, and the range of incomes. As shown in
Table 1, the income sequences used in Experiment 1 varied not only in their CV, but also these
additional dimensions. As an example, it may have been the minimum income participants received
that was driving their saving decisions—perhaps because the income shock associated with earning an
unexpectedly low income forced participants to update their view of how uncertain the (experimental)
world was, thereby prompting them to save more as a precaution (Chamon et al., 2013; Collins &
Gjertson, 2013). If this were the case, it would explain why participants’ perceived volatility ratings
did not neatly map onto their saving behaviour.
Electronic copy available at: https://ssrn.com/abstract=4509925

Table 1.
Dimensions of income sequences used in Experiment 1.
Condition Incomes (£) CV Min Max Range
No Volatility 1,000 1,000 1,000 1,000 1,000 0.00 1,000 1,000 0
1,000 1,000 1,000 1,000 1,000
1,000 1,000 1,000 1,000 1,000
Low Volatility 431 570 656 794 873 0.30 431 1,340 909
883 910 990 1,158 1,202
1,277 1,279 1,311 1,326 1,340
High Volatility 173 274 466 526 529 0.60 173 2,088 1,915
650 661 847 1,101 1,374
1,404 1,436 1,571 1,900 2,088
Note. CV = Coefficient of variation. Min, Max = Minimum/Maximum incomes received during task.
While the main focus for this study is saving behaviour, it is worth noting that our income
volatility manipulation did not appear to increase participants’ financial impatience—contrary to prior
findings (Peetz et al., 2021; West et al., 2020). One possible reason for our failure to observe an effect
is that both our income volatility manipulation and our measure of financial impatience were
hypothetical. While Peetz et al. (2021) also manipulated the volatility of hypothetical income, their
measure of financial impatience involved participants choosing between two real payments. In the
case of West et al. (2020), the measure of financial impatience involved hypothetical choices, but
participants experienced volatility in their real income. Another possibility for the inconsistency in our
findings could be due to our use of different methods of measuring financial impatience. While our
study used a fill-in-the-blank approach, both prior studies used ‘binary-choice’ tasks, which give
participants the choice between defined smaller-sooner and larger-later amounts. Previous work
suggests that binary-choice tasks can produce steeper discounting rates compared to fill-in-the-blank
tasks (Smith & Hantula, 2008). It is therefore possible that the effect of income volatility on financial
impatience is small—one that our measure was unable to detect, but that more sensitive measures may
have been able to. Though exploring these potential explanations (or any others) was beyond the
scope of our study, our null result suggests the need for further investigation to have greater
confidence in the link between income volatility and financial impatience.
Electronic copy available at: https://ssrn.com/abstract=4509925

4. Experiment 2
For Experiment 2, we generated three new income sequences that would allow us to tease apart
whether the minimum income, maximum income, or range of incomes would provide a better account
for saving behaviour than CV. The new sequences were designed such that they could be compared
against one another, as well as against the High Volatility condition from Experiment 1. Each
sequence shared a different set of dimensions with the High Volatility condition: either the minimum
income (but not the maximum or range), the maximum income (but not the minimum or range), or
both the minimum and maximum incomes (and therefore also the range). Notably, however, all three
conditions shared the same statistical variance as one another (CVs = 0.37) but were deliberately
created to be less volatile than the High Volatility condition (CV = 0.60).
4.1. Method
4.1.1. Participants
We recruited 241 new participants (M = 39.65 years; 108 males; 130 females; 2 non-binaries; 1
age
preferred not to say) from Prolific Academic using the same eligibility criteria described for
Experiment 1. In addition to these criteria, we excluded anyone who had participated in the previous
experiment. Participants again received a £3.00 (USD 3.77) participation payment and were eligible
for a £3.00 (USD 3.77) bonus payment based on their task performance.
4.1.2. Materials and procedure
Experiment 2 used the same financial decision making task and procedure as described for
Experiment 1. However, participants were assigned to three new conditions which used different
income sequences from the prior experiment: “Same Range” (n = 80), “Same Min” (n = 81), and
“Same Max” (n = 80). The names of these conditions indicated what characteristic(s) their income
sequence shared with the High Volatility condition from Experiment 1.
In the Same Range condition, participants’ income sequence shared the same minimum and
maximum values as the High Volatility condition (£173 and £2,088 respectively), and therefore the
same range (£1,915). However, the income sequence was constructed to have a lower coefficient of
variation (CV = 0.37 vs 0.60 for the High Volatility condition). This would allow us to directly
compare the two conditions to determine whether CV was driving the difference in saving behaviour
or whether it was one of the other dimensions.
In the Same Min condition, participants’ income ranged from £173 to £1,580 across rounds—
sharing the same minimum income as the High Volatility condition but differing in the maximum
income and range. Conversely, the Same Max condition shared the same maximum income as the
Electronic copy available at: https://ssrn.com/abstract=4509925

High Volatility condition (£2,088) but had a different minimum income (£681) and range. Notably,
however, the range of the Same Min and Same Max conditions were designed to be identical
(£1,407). Both sequences were also constructed to share the same CV as the Same Range condition
(CV = 0.37).
All three sequences therefore shared the same statistical variance (unlike in Experiment 1),
but varied in their minimum income, maximum income, and range of incomes. As with the previous
experiment, regardless of which income sequence participants received, their total income across the
task was £15,000. By keeping this and all other task parameters the same as Experiment 1, it became
possible to directly compare the High Volatility condition from the first experiment with the new
conditions in Experiment 2.
4.2. Results
4.2.1. Comparisons between Same Range, Same Min, and Same Max conditions
We first analysed the data from our three Experiment 2 conditions. This allowed us to explore whether
any differences in our measures were being driven by dimensions of participants’ income sequences
other than CV.
Across our four measures (perceived volatility, final savings, perceived difficulty, and
financial impatience), we consistently observed no differences between our three conditions. The
evidence for this was moderate for perceived volatility (BF = 3.91), strong for final savings (BF =
01 01
16.19), moderate for perceived difficulty (BF = 6.82), and strong for financial impatience (BF =
01 01
12.50).
4.2.2. Comparisons against High Volatility condition
We then compared the perceived volatility ratings and final savings of our three Experiment 2
conditions against the High Volatility condition from Experiment 1 (see Figure 3).
Electronic copy available at: https://ssrn.com/abstract=4509925

(a) Mean perceived volatility ratings
(b) Distribution of final savings
Figure 3. Perceived volatility ratings and final savings by level of income volatility in Experiment 2.
High Volatility condition from Experiment 1 shown on right of dotted line for comparison. Means and
standard error bars indicated.
There was anecdotal evidence that participants perceived their income to be more volatile in
the High Volatility condition (M = 6.40) than the Same Range condition (M = 5.69) (BF = 1.52).
10
However, there was moderate evidence that the perceived volatility ratings did not differ between the
High Volatility condition and the Same Min (M = 6.31) or Same Max (M = 6.11) conditions (BF =
01
5.66 and 4.18 respectively).
Electronic copy available at: https://ssrn.com/abstract=4509925

In contrast, there was consistent evidence that participants saved more in the High Volatility
condition (M = £8,571.64) compared to the other three conditions. The evidence was moderate for the
Same Range (M = £7,096.65) and Same Max (M = £6,842.40) conditions (BF = 3.03 and 6.69
10
respectively), and anecdotal for the Same Min condition (M = £7,362.69) (BF = 1.16).
10
4.3. Discussion
Our results did not support the hypothesis that saving behaviour was being driven by a dimension of
the income sequence other than CV. Despite varying the minimum income, maximum income, and
range of incomes between conditions, participants all exhibited similar saving behaviour. If anything,
our findings provided greater reason to believe that CV was the driver of saving behaviour. All three
conditions saved less than the High Volatility condition, with the consistent difference being their
lower CV (CV = 0.37 vs 0.60). Thus, we saw further evidence that increased income volatility
corresponded to higher savings within our task.
However, we continued to observe a discrepancy between participants’ perceptions of their
income’s volatility and their saving behaviour. While participants saved more in the High Volatility
condition, their perceived volatility ratings were similar to the ratings provided in our Experiment 2
conditions (with the exception of the Same Range condition, where the evidence of a difference was
only anecdotal). This echoed what we had observed in Experiment 1, in which participants from the
Low and High Volatility conditions had rated their income as similarly volatile despite exhibiting
different saving behaviour.
This led us to consider a new hypothesis: that participants were giving similar responses on
our perceived volatility rating scale because we were asking them to make an absolute judgment with
only one objective point of reference (0 = “not volatile at all”). Previous work suggests that judgments
can differ when made from an absolute versus relative standpoint (e.g., Fox & Tversky, 1995; Goffin
& Olson, 2011; Stewart et al., 2006). It was therefore possible that participants in different conditions
were perceiving the volatility of their income differently, but shared similar thought processes in how
this should be reflected in their response on the scale—for example, thinking “there is some volatility
but not an extreme amount, so I will respond with a seven”. This could explain why participants who
experienced some degree of income volatility (i.e., all conditions except for the No Volatility
condition) provided similar ratings of perceived volatility while differing in their saving behaviour.
To examine this hypothesis, we needed participants to provide relative judgments of their
income’s volatility. To obtain these judgments, we adapted our procedure in Experiment 3 such that
participants would have two attempts at the financial decision making task. These two attempts used
Electronic copy available at: https://ssrn.com/abstract=4509925

income sequences with different levels of volatility, allowing us to compare participants’ perceived
volatility ratings between attempts.
5. Experiment 3
For Experiment 3, participants were given two attempts at the financial decision making task. In one
attempt, participants received the same income as the Low Volatility condition from Experiment 1; in
the other, they received the same income as the High Volatility condition. The ordering of the income
sequences was counterbalanced.
Our goal was to examine whether participants would be sensitive to the different levels of
volatility between their attempts. We preregistered7 three key hypotheses based on this goal prior to
conducting the experiment. First, participants would provide higher perceived volatility ratings during
their High Volatility attempt compared to their Low Volatility attempt. Second, participants would
provide similar ratings during their first attempt, irrespective of whether they received the Low
Volatility or High Volatility income sequence. This would be consistent with what had been observed
in Experiment 1. Third, perceived volatility ratings would differ when comparing second attempts at
the task. We expected that since participants would be making relative judgments of volatility in their
second attempts, they would provide higher ratings if this second attempt involved the High Volatility
income sequence, whereas they would provide lower ratings if their second attempt instead involved
the Low Volatility income sequence.
5.1. Method
5.1.1. Participants
We recruited 150 new participants (M = 38.85 years; 75 males; 74 females; 1 non-binary) from
age
Prolific Academic using the same eligibility criteria as described in the previous two experiments.
Sample size was based on an a priori power analysis that allowed for detection of a small effect in
both between- and within-subjects comparisons (𝛿 = .80; 𝛾 = .20; 𝛼 = .05). Participants received a
£4.50 (USD 5.66) participation payment and were eligible for a £3.00 (USD 3.77) bonus payment
based on their task performance.
5.1.2. Materials and procedure
For Experiment 3, the procedure was adapted such that participants were given two attempts at the
financial decision making task. In one attempt, participants received the same income sequence that
7 Our experiment was preregistered using the AsPredicted platform (https://aspredicted.org/bg6gi.pdf).
Electronic copy available at: https://ssrn.com/abstract=4509925

was used in the Low Volatility condition from Experiment 1; in the other, they received the High
Volatility income sequence. The order in which participants received these attempts was
counterbalanced, meaning half of participants received the Low Volatility version first (“Low to
High”; n = 75), while the other half received the High Volatility version first (“High to Low”; n = 75).
The inherent issue in allowing participants two attempts at the task is that participants’
behaviour in the second attempt may be confounded by learnings from their first attempt. This would
impair our ability to compare our results against the behaviour we had observed in Experiment 1. We
sought to mitigate this concern through several deliberate design choices when adjusting our
procedure from the previous experiments. First, at the end of participants’ first attempt, we advised
them that the emergency had occurred, but did not reveal how much it cost. This was only revealed at
the end of the experiment after participants had completed both attempts. Second, we explicitly
indicated to participants that the timing and cost of the emergency may differ between attempts. This
sought to dissuade participants from assuming that the timing of the emergency would be the same for
both attempts.8 Finally, although participants’ final score in the experiment was calculated by
combining their performance in each attempt, we visually reset their score to zero in between
attempts. This was intended to reiterate to participants that the two attempts were independent.
The overall procedure thus proceeded as follows. Participants were advised that they would
be given two attempts at a financial decision making game. After reading the instructions, participants
underwent the practice stage, followed by their first attempt at the task. At the end of the first attempt,
participants were informed that the financial emergency was about to occur and were asked to rate the
volatility of their income. Participants were then told that the cost of the emergency would only be
revealed after they had completed their second attempt, which they subsequently commenced. At the
end of their second attempt, participants were again asked to rate the volatility of their income.
Following this, the cost of both emergencies was revealed9 and participants were advised of the
outcome of each attempt. Participants’ total score across both attempts was used to determine
eligibility for the bonus reward. Finally, participants were asked to provide information about their
demographic and financial situations, before receiving a debrief.
8 However, in both attempts, the emergency needed to occur after the 15th round so that the income sequences
used would be consistent with those from Experiment 1.
9 As with the previous experiments, the first emergency involved home repairs with a total cost of £4,500. The
second emergency involved a car breakdown and cost £2,500.
Electronic copy available at: https://ssrn.com/abstract=4509925

5.2. Results
5.2.1. Comparison of volatility ratings between attempts
Figure 4 shows participants’ mean perceived volatility ratings as a function of the level of volatility
(Low or High) and whether it was their first or second attempt. As predicted, we observed moderate
evidence that participants provided similar ratings during their first attempt, regardless of whether this
was the Low Volatility or the High Volatility version (BF = 3.28). However, contrary to our
01
prediction, there was also anecdotal evidence that ratings did not differ on participants’ second
attempt either (BF = 2.13).
01
Figure 4. Mean perceived volatility ratings by level of income volatility and task attempt in
Experiment 4. Low and High Volatility conditions from Experiment 1 shown on right of dotted line
for comparison. Standard error bars indicated.
While we did not find evidence for our hypothesis when examining volatility ratings at the
group level, we did observe evidence at the individual participant level. We conducted a paired t-test
comparing participants’ ratings in their Low Volatility and High Volatility attempts. This indicated that
there was anecdotal evidence of participants providing higher ratings during their High Volatility
attempt compared to their Low Volatility attempt (BF = 2.91), with the mean difference between
10
ratings being 0.43.
5.2.2. Additional pre-registered analyses
As part of our preregistration, we planned two additional analyses that were unrelated to our main
hypotheses about perceived volatility ratings. First, we hypothesised that participants would save
Electronic copy available at: https://ssrn.com/abstract=4509925

more in the High Volatility condition than in the Low Volatility condition (see Figure 5). We examined
this by conducting a Bayesian ANOVA where level of income volatility and task attempt were entered
as variables. This provided Bayes factors for different combinations of predictive models, from which
we could compute inclusion factors.10 Our findings contradicted our hypothesis; there was moderate
evidence against an income volatility level effect (BF = 3.36). Instead, we observed extreme
01
evidence in favour of a task attempt effect (BF = 5.01×106), with participants saving substantially
10
more in their second attempt regardless of whether it involved the Low or High Volatility income
sequence. There was also anecdotal evidence against an interaction between task attempt and income
volatility level (BF = 2.11).
01
Figure 5. Distribution of final savings by level of income volatility and task attempt in Experiment 3.
Low and High Volatility conditions from Experiment 1 shown on right of dotted line for comparison.
Means and standard error bars indicated.
Our other additional hypothesis was that we should see similar perceived volatility ratings and
final savings from participants completing their first attempts at the task as what was observed in
Experiment 1. This would provide a signal of reliability for participants’ behaviour within our task.
We started by comparing the participants from Experiment 3 who received the Low Volatility income
sequence first with participants in the Low Volatility condition from Experiment 1. There was
moderate evidence to suggest that participants provided similar perceived volatility ratings (Figure 4)
and ended the task with similar final savings amounts (Figure 5; BF = 5.08 and 4.51 respectively).
01
When drawing the same comparison between the High Volatility counterparts, we again observed
10 Inclusion factors are computed by comparing the posterior odds of models that include and exclude a
predictor of interest (Van Den Bergh et al., 2020). These help to quantify the level of evidence for whether the
predictor should be included.
Electronic copy available at: https://ssrn.com/abstract=4509925

moderate evidence in favour of the perceived volatility ratings being similar (BF = 5.44). However,
01
we found moderate evidence that participants’ final savings differed (BF = 5.50); participants who
10
received the High Volatility income sequence in their first task attempt in Experiment 3 appeared to
have saved substantially less than those who were in the High Volatility condition from Experiment 1
(M = £6,834.69 vs £8,571.64).
5.3. Discussion
Experiment 3 provided some credence to our hypothesis that participants were sensitive to different
levels of income volatility, but we were failing to capture this when asking for an absolute judgment
on our 11-point scale (0 = “Not Volatile”; 10 = “Extremely Volatile”). This helped to explain why
participants’ ratings of income volatility across our previous experiments did not necessarily align
with their observed saving behaviour. It also reintroduced the possibility of an income volatility
‘threshold’ that needed to be exceeded for participants to adjust their behaviour within the task. As a
reminder, we observed in Experiment 1 that participants saved more in the High Volatility condition
relative to those who had received a stable income, but that this difference was not observed for the
Low Volatility condition.
However, before we could make any claims about a potential threshold, we first needed to
resolve the inconsistency between the saving behaviour we had observed from participants in
Experiment 1’s High Volatility condition and the participants who received the High Volatility
condition as their first attempt in Experiment 3. In theory, these participants should have exhibited
similar saving behaviour; the only difference was that those in Experiment 3 would have known that
they would be completing a second (independent) attempt at the task. The fact that we observed
higher savings in Experiment 1 but not 3 called into question how reliable our finding was, and by
extension, whether there was even an income volatility effect at all.
This led us to run a single additional experimental condition in Experiment 4 in which we
further increased the income volatility that participants would experience (“Very High Volatility”; CV
= 0.90). We expected that running the results of this condition would help to build confidence in one
of two conclusions. If these participants did not save any differently compared to participants who
received stable incomes (in Experiment 1), we could be more confident that income volatility does not
influence saving decisions, and that the increased saving effect we observed in the High Volatility
condition from Experiment 1 was likely a false positive. In contrast, if we did observe higher savings
in this Very High Volatility condition, we would instead have greater support for an effect of income
volatility on saving behaviour and consider our results from Experiment 3 to be a false negative.
Electronic copy available at: https://ssrn.com/abstract=4509925

6. Experiment 4
In Experiment 4, we generated a new income sequence that was more volatile than the conditions
from Experiment 1. This condition was known as the Very High Volatility condition and had a CV of
0.90. All participants were placed in this condition and completed only one attempt at the financial
decision making task.
6.1. Method
6.1.1. Participants
We recruited 80 new participants (M = 36.63 years; 34 males; 46 females) from Prolific Academic
age
using the same eligibility criteria as described in the previous experiments. Our sample size was based
on having the same number of participants per condition as Experiment 1. Participants received £3.00
(USD 3.77) in exchange for their participation and were also eligible for an additional bonus of £3.00
(USD 3.77) based on their performance in the financial decision making task.
6.1.2. Materials and procedure
Experiment 4 used the same financial decision making task and followed the same procedure as
Experiment 1. All participants—henceforth referred to as the Very High Volatility condition—
received a newly generated income sequence that ranged from £44 to £3,457, with the CV of the
sequence being 0.90. Consistent with all other income sequences, the total income received across the
task remained at £15,000.
6.2. Results
In this section, we first compare perceived volatility ratings and final savings between our Very High
Volatility condition and the No Volatility condition in Experiment 1. We then report on analyses using
our combined data across all four experiments, where we grouped conditions with the same level of
income volatility. We pooled our conditions from Experiment 2 into a group labelled “Medium
Volatility”, as these participants all received an income sequence with a CV of 0.37—between the
CVs of Experiment 1’s Low Volatility condition (CV = 0.30) and High Volatility condition (CV =
0.60). We then pooled participants’ first attempts from Experiment 3 with their respective Experiment
1 conditions (i.e., Low or High Volatility). Finally, we excluded data from participants’ second
attempts in Experiment 3; our prior results suggested that participants tended to save more on their
Electronic copy available at: https://ssrn.com/abstract=4509925

second attempt (regardless of level of income volatility), rendering these data incomparable to our
other conditions, where participants were completing their first or only attempt.11
6.2.1. Comparison of Very High Volatility to No Volatility
We observed extreme evidence that participants perceived their income to be substantially more
volatile in the Very High Volatility condition (M = 6.79) compared to the No Volatility condition (M =
3.17) (BF = 1.03×1013). There was also strong evidence that participants saved more in the Very
10
High Volatility condition than the No Volatility condition (M = £8,342.80 vs £6,647.88) (BF =
10
10.97).
6.2.2. Combined analyses on income volatility effect
A Bayesian ANOVA indicated that there was extreme evidence that perceived volatility ratings
differed between income volatility levels (BF = 4.62×1025). However, as is evident from Figure 6,
10
this effect appears to be entirely driven by lower volatility ratings in Experiment 1’s No Volatility
condition. When excluding this condition from the analysis, there was anecdotal evidence that the
remaining conditions did not differ in their volatility ratings (BF = 1.41).
01
Figure 6. Mean perceived volatility ratings by level of income volatility across Experiments 1 to 4.
Standard error bars indicated.
11 We recognise that this pooled analysis approach forgoes random assignment of participants to experiment
conditions. However, given our experiments drew from the same participant pool, offered similar incentives,
and were conducted within months of each other, we considered it unlikely that any of our observed results
would be driven by systematic differences in participant characteristics.
Electronic copy available at: https://ssrn.com/abstract=4509925

A similar analysis of participants’ final savings yielded inconclusive evidence as to whether
they differed as a function of income volatility level (BF = 1.01) (see Figure 7). We thus chose to
01
exploit the fact that each income volatility level was quantifiable based on its CV and that this could
be treated as a continuous measure. When instead analysing final savings as a function of CV, we
observed very strong evidence that a higher CV was associated with more savings (BF = 45.89). A
10
Bayesian regression approach yielded a median posterior estimate for the CV effect to be £2,134.69.
This suggested that a 0.1 increase in CV corresponded to an average increase in savings of
approximately £213 within our task (95% HDI: [£92, £328]).
Figure 7. Distribution of final savings by level of income volatility across Experiments 1 to 4. Means
and standard error bars indicated.
7. General Discussion
7.1. The relationship between income volatility and saving behaviour
Across four experiments, our collective results provide preliminary evidence that people save more
when faced with fluctuations in income and are consistent with the view that uncertainty drives
precautionary savings motives (Carroll & Kimball, 2018). However, the fact that there exists
empirical work supporting both that income uncertainty increases saving behaviour (e.g., Caballero,
1991; Miles, 1997) and decreases saving behaviour (e.g., Cobb-Clark et al., 2016; Perry & Morris,
2005) suggests that the relationship is not so straightforward. Our findings could be interpreted as
indicative of what people intend to do when faced with a volatile income, but not necessarily what
they follow through with—a gap between saving intentions and behaviours (Rabinovich & Webley,
2007).
Electronic copy available at: https://ssrn.com/abstract=4509925

By design, our financial decision making task was a highly simplified version of the true
trade-off that people must make between spending and saving for the future. One of the key
differences between our hypothetical setting and the real world was that participants never needed to
worry about their income being insufficient to meet immediate expenses as there were none within
our task; instead, they could afford to entirely focus their attention on the long-term goal (i.e.,
accumulating adequate savings for the emergency). In contrast, in the real world, people with volatile
incomes may be faced with the looming fear that an unanticipated drop in their income may leave
them unable to fulfil their financial obligations. It is perhaps this financial pressure, or the feelings of
stress and scarcity that accompany the pressure, that leads people to overly focus on the short-term
and overrides their underlying intention to save more. One potential hypothesis is therefore that the
experience of income volatility has differential effects on saving behaviour depending on one’s
financial situation (van Schie et al., 2012). The motivation to save more in response to a fluctuating
income may be a luxury for those in strong financial positions who need not be concerned about it
affecting their short-term liquidity.
7.2. Perceptions of income volatility
Our findings also suggest that income volatility may need to exceed some threshold before it
impacts saving decisions. Within our experimental task, this threshold appeared to be around a
coefficient of variation of 0.60. Below this CV level (i.e., in the Low Volatility condition of
Experiment 1 and the three Experiment 2 conditions), saving behaviour did not differ relative from
participants who received a steady income. At this CV level (i.e., our High Volatility conditions), we
observed inconsistent results—increased saving behaviour in Experiment 1 but not in Experiment 3.
Above this CV level (i.e., in the Very High Volatility condition), we observed the highest amount of
savings. For reference, as noted earlier, the typical household is estimated to experience a CV of
between 0.30 to 0.40.
If such a threshold does exist, this naturally raises the question of how people judge whether
their income is volatile or not. While our results show that CV serves as a reasonable predictor for
participants’ savings within our task, we note three potential extensions upon our work. First, future
work may seek to assess other definitions of volatility, such as the second-order coefficient of
volatility proposed by Kvålseth (2017). Second, there may be opportunities to build upon our second
experiment and further investigate whether other characteristics of income sequences better explain
people’s perceptions of their volatility (Konovalova & Pachur, 2021). Third, it may be worthwhile to
distinguish between income volatility and predictability. For some individuals, income may fluctuate
between pay periods, but in a predictable manner. This may occur if income is correlated with the
Electronic copy available at: https://ssrn.com/abstract=4509925

time of year (e.g., seasonal work or annual bonuses) or if individuals have control over how much
they work and therefore their earnings (Peetz et al., 2021).
7.3. Facilitating intentions to save
Finally, our findings suggest there may be opportunities within the financial sector to better support
consumers whose incomes are volatile. Banks in particular have visibility over their customers’
income and can therefore readily identify which of their customers have highly volatile incomes and
may be motivated to save more. It may be possible to then develop interventions that help consumers
follow through with their intentions. For example, messages could be deployed to customers when a
spike in income is detected (relative to their usual earnings). Such ‘just-in-time’ interventions can be
highly effective (often used in health settings; e.g., Forman et al., 2019; Van Der Laan & Orcholska,
2022); in this case, potentially by combating the natural tendency to spend more of money that is
considered a bonus or windfall (Arkes et al., 1994; Epley & Gneezy, 2007).
8. Conclusion
Recent economic trends, such as the rapid rise of the gig economy, have made it increasingly common
for individuals to have incomes that are unstable and fluctuate within a year. Our study set out to
investigate how experiencing this income volatility affects saving decisions. Using a novel financial
decision making task, we provide evidence that higher income volatility results in increased saving
behaviour. To the best of our knowledge, our study is the first to address this question experimentally
and offers many fruitful avenues for further research. By improving our understanding of the
relationship between income volatility and saving, we may be able to better tailor financial products
and services for individuals with volatile incomes, and better meet their financial needs.
Electronic copy available at: https://ssrn.com/abstract=4509925

9. References
Anvari-Clark, J., & Ansong, D. (2022). Predicting financial well-being using the financial capability
perspective: The roles of financial shocks, income volatility, financial products, and savings
behaviors. Journal of Family and Economic Issues, 43, 730–743.
https://doi.org/10.1007/s10834-022-09849-w
Arkes, H. R., Joyner, C. A., Pezzo, M. V., Nash, J. G., Siegel-Jacobs, K., & Stone, E. (1994). The
psychology of windfall gains. Organizational Behavior and Human Decision Processes,
59(3), 331–347. https://doi.org/10.1006/obhd.1994.1063
Bania, N., & Leete, L. (2009). Monthly household income volatility in the U.S., 1991/92 vs. 2002/03.
Economics Bulletin, 29(3), 2100–2112.
Bania, N., & Leete, L. (2022). Monthly income volatility and health outcomes. Contemporary
Economic Policy, 40(4), 636–658. https://doi.org/10.1111/coep.12580
Caballero, R. J. (1991). Earnings uncertainty and aggregate wealth accumulation. The American
Economic Review, 81(4), 859–871.
Carroll, C. D., & Kimball, M. S. (2018). Precautionary saving and precautionary wealth. In
Macmillan Publishers Ltd (Ed.), The new Palgrave dictionary of economics (pp. 10591–
10599). Palgrave Macmillan UK. https://doi.org/10.1057/978-1-349-95189-5_2079
Chamon, M., Liu, K., & Prasad, E. (2013). Income uncertainty and household savings in China.
Journal of Development Economics, 105, 164–177.
https://doi.org/10.1016/j.jdeveco.2013.07.014
Chapman, G. B. (1996). Temporal discounting and utility for health and money. Journal of
Experimental Psychology: Learning, Memory, and Cognition, 22(3), Article 3.
https://doi.org/10.1037/0278-7393.22.3.771
Cobb-Clark, D. A., Kassenboehmer, S. C., & Sinning, M. G. (2016). Locus of control and savings.
Journal of Banking & Finance, 73, 113–130. https://doi.org/10.1016/j.jbankfin.2016.06.013
Collins, J. M., & Gjertson, L. (2013). Emergency savings for low-income consumers. Focus, 30(1),
12–17.
Electronic copy available at: https://ssrn.com/abstract=4509925

Diaz-Serrano, L. (2005). Income volatility and residential mortgage delinquency across the EU.
Journal of Housing Economics, 14(3), 153–177. https://doi.org/10.1016/j.jhe.2005.07.003
Drèze, J. H., & Modigliani, F. (1972). Consumption decisions under uncertainty. Journal of Economic
Theory, 5(3), 308–335.
Epley, N., & Gneezy, A. (2007). The framing of financial windfalls and implications for public policy.
The Journal of Socio-Economics, 36(1), 36–47. https://doi.org/10.1016/j.socec.2005.12.012
Farrell, D., & Greig, F. (2016). Paychecks, paydays, and the online platform economy. JPMorgan
Chase Institute. https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-
co/institute/pdf/jpmc-institute-volatility-2-report.pdf
Farrell, D., Greig, F., & Yu, C. (2019). Weathering volatility 2.0: A monthly stress test to guide
savings. JPMorgan Chase Institute.
https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-
co/institute/pdf/institute-volatility-cash-buffer-report.pdf
Faul, F., Erdfelder, E., Lang, A.-G., & Buchner, A. (2007). G*Power 3: A flexible statistical power
analysis program for the social, behavioral, and biomedical sciences. Behavior Research
Methods, 39(2), 175–191. https://doi.org/10.3758/BF03193146
Fawcett, T. W., McNamara, J. M., & Houston, A. I. (2012). When is it adaptive to be patient? A
general framework for evaluating delayed rewards. Behavioural Processes, 89(2), 128–136.
https://doi.org/10.1016/j.beproc.2011.08.015
Forman, E. M., Goldstein, S. P., Crochiere, R. J., Butryn, M. L., Juarascio, A. S., Zhang, F., & Foster,
G. D. (2019). Randomized controlled trial of OnTrack, a just-in-time adaptive intervention
designed to enhance weight loss. Translational Behavioral Medicine, 9(6), 989–1001.
https://doi.org/10.1093/tbm/ibz137
Fox, C. R., & Tversky, A. (1995). Ambiguity aversion and comparative ignorance. The Quarterly
Journal of Economics, 110(3), Article 3. https://doi.org/10.2307/2946693
Fulford, S. L. (2015). The surprisingly low importance of income uncertainty for precaution.
European Economic Review, 79, 151–171. https://doi.org/10.1016/j.euroecorev.2015.07.016
Electronic copy available at: https://ssrn.com/abstract=4509925

Gladstone, J., Nieboer, J., & Raghavan, K. (2020). Understanding consumer financial wellbeing
through banking data (No. 58; FCA Occasional Paper). Financial Conduct Authority.
https://www.fca.org.uk/publication/occasional-papers/occasional-paper-58.pdf
Goda, G. S., Levy, M., Manchester, C. F., Sojourner, A., & Tasoff, J. (2019). Predicting retirement
savings using survey measures of exponential-growth bias and present bias. Economic
Inquiry, 57(3), 1636–1658. https://doi.org/10.1111/ecin.12792
Goffin, R. D., & Olson, J. M. (2011). Is it all relative? Comparative judgments and the possible
improvement of self-ratings and ratings of others. Perspectives on Psychological Science,
6(1), 48–60. https://doi.org/10.1177/1745691610393521
Halliday, T. J. (2007). Income volatility and health (No. 3234; IZA Discussion Paper Series). The
Institute for the Study of Labor. https://docs.iza.org/dp3234.pdf
Hannagan, A., & Morduch, J. (2015). Income gains and month-to-month income volatility: Household
evidence from the US Financial Diaries (No. 2659883; NYU Wagner Research Paper).
https://www.financialaccess.org/publications-index/2015/usfd
Haushofer, J., & Fehr, E. (2014). On the psychology of poverty. Science, 344(6186), 862–867.
https://doi.org/10.1126/science.1232491
Hipp, L., Bernhardt, J., & Allmendinger, J. (2015). Institutions and the prevalence of nonstandard
employment. Socio-Economic Review, 13(2), 351–377. https://doi.org/10.1093/ser/mwv002
Kalleberg, A. L., & Hewison, K. (2013). Precarious work and the challenge for Asia. American
Behavioral Scientist, 57(3), 271–288. https://doi.org/10.1177/0002764212466238
Kazarosian, M. (1997). Precautionary savings—A panel study. Review of Economics and Statistics,
79(2), 241–247. https://doi.org/10.1162/003465397556593
Kirby, K. N., & Maraković, N. N. (1995). Modeling myopic decisions: Evidence for hyperbolic delay-
discounting within subjects and amounts. Organizational Behavior and Human Decision
Processes, 64(1), 22–30. https://doi.org/10.1006/obhd.1995.1086
Konovalova, E., & Pachur, T. (2021). The intuitive conceptualization and perception of variance.
Cognition, 217, 104906. https://doi.org/10.1016/j.cognition.2021.104906
Electronic copy available at: https://ssrn.com/abstract=4509925

Kvålseth, T. O. (2017). Coefficient of variation: The second-order alternative. Journal of Applied
Statistics, 44(3), 402–415. https://doi.org/10.1080/02664763.2016.1174195
Lee, M. D., & Wagenmakers, E.-J. (2013). Bayesian cognitive modeling: A practical course.
Cambridge University Press.
Leland, H. E. (1968). Saving and uncertainty: The precautionary demand for saving. The Quarterly
Journal of Economics, 82(3), 465. https://doi.org/10.2307/1879518
Lugilde, A., Bande, R., & Riveiro, D. (2019). Precautionary saving: A review of the empirical
literature. Journal of Economic Surveys, 33(2), 481–515. https://doi.org/10.1111/joes.12284
Mani, A., Mullainathan, S., Shafir, E., & Zhao, J. (2013). Poverty impedes cognitive function.
Science, 341(6149), 976–980. https://doi.org/10.1126/science.1238041
Mani, A., Mullainathan, S., Shafir, E., & Zhao, J. (2020). Scarcity and cognitive function around
payday: A conceptual and empirical analysis. Journal of the Association for Consumer
Research, 5(4), 365–376. https://doi.org/10.1086/709885
Miles, D. (1997). A household level study of the determinants of incomes and consumption. The
Economic Journal, 107(440), 1–25. https://doi.org/10.1111/1468-0297.00139
Mills, G. B., & Amick, J. (2010). Can savings help overcome income instability? (Brief 18;
Perspectives on Low-Income Working Families). The Urban Institute.
https://www.urban.org/sites/default/files/publication/32771/412290-Can-Savings-Help-
Overcome-Income-Instability-.PDF
Morris, P., A., Hill, H., D., Gennetian, L., A., Rodrigues, C., & Wolf, S. (2015). Income volatility in
U.S. households with children: Another growing disparity between the rich and the poor?
(No. 1429-15; IRP Discussion Paper). Institute for Research on Poverty.
https://www.irp.wisc.edu/wp/wp-content/uploads/2018/05/dp142915.pdf
Mullainathan, S., & Shafir, E. (2009). Savings policy and decisionmaking in low-income households.
In M. Barr & R. Blank (Eds.), Insufficient funds: Savings, assets, credit and banking among
low-income households (pp. 121–145). Russell Sage Foundation Press.
Electronic copy available at: https://ssrn.com/abstract=4509925

Nunley, J. M., & Seals, A. (2010). The effects of household income volatility on divorce. American
Journal of Economics and Sociology, 69(3), 983–1010. https://doi.org/10.1111/j.1536-
7150.2010.00731.x
Peetz, J., Robson, J., & Xuereb, S. (2021). The role of income volatility and perceived locus of
control in financial planning decisions. Frontiers in Psychology, 12, 638043.
https://doi.org/10.3389/fpsyg.2021.638043
Pepper, G. V., & Nettle, D. (2017). The behavioural constellation of deprivation: Causes and
consequences. Behavioral and Brain Sciences, 40, e314.
https://doi.org/10.1017/S0140525X1600234X
Perry, V. G., & Morris, M. D. (2005). Who is in control? The role of self-perception, knowledge, and
income in explaining consumer financial behavior. Journal of Consumer Affairs, 39(2), 299–
313. https://doi.org/10.1111/j.1745-6606.2005.00016.x
Prause, J., Dooley, D., & Huh, J. (2009). Income volatility and psychological depression. American
Journal of Community Psychology, 43(1–2), 57–70. https://doi.org/10.1007/s10464-008-
9219-3
Rabinovich, A., & Webley, P. (2007). Filling the gap between planning and doing: Psychological
factors involved in the successful implementation of saving intention. Journal of Economic
Psychology, 28(4), 444–461. https://doi.org/10.1016/j.joep.2006.09.002
Rosenbaum, P. R. (2015). How to see more in observational studies: Some new quasi-experimental
devices. Annual Review of Statistics and Its Application, 2(1), 21–48.
https://doi.org/10.1146/annurev-statistics-010814-020201
Sandmo, A. (1970). The effect of uncertainty on saving decisions. The Review of Economic Studies,
37(3), 353. https://doi.org/10.2307/2296725
Sayre, G. M. (2022). The costs of insecurity: Pay volatility and health outcomes. Journal of Applied
Psychology. Advance online publication. https://doi.org/10.1037/apl0001062
Schwabe, L., & Wolf, O. T. (2009). Stress prompts habit behavior in humans. The Journal of
Neuroscience, 29(22), 7191–7198. https://doi.org/10.1523/JNEUROSCI.0979-09.2009
Electronic copy available at: https://ssrn.com/abstract=4509925

Senate Select Committee on Job Security. (2022). The job insecurity report.
https://parlinfo.aph.gov.au/parlInfo/download/committees/reportsen/024780/toc_pdf/Thejobin
securityreport.pdf;fileType%3Dapplication%2Fpdf
Shapiro, J., & Wu, S. (2011). Fatalism and savings. The Journal of Socio-Economics, 40(5), 645–651.
https://doi.org/10.1016/j.socec.2011.05.003
Smith, C. L., & Hantula, D. A. (2008). Methodological considerations in the study of delay
discounting in intertemporal choice: A comparison of tasks and modes. Behavior Research
Methods, 40(4), 940–953. https://doi.org/10.3758/BRM.40.4.940
Stewart, N., Chater, N., & Brown, G. D. A. (2006). Decision by sampling. Cognitive Psychology,
53(1), 1–26. https://doi.org/10.1016/j.cogpsych.2005.10.003
Van Den Bergh, D., Van Doorn, J., Marsman, M., Draws, T., Van Kesteren, E.-J., Derks, K.,
Dablander, F., Gronau, Q. F., Kucharský, Š., Gupta, A. R. K. N., Sarafoglou, A., Voelkel, J.
G., Stefan, A., Ly, A., Hinne, M., Matzke, D., & Wagenmakers, E.-J. (2020). A tutorial on
conducting and intepreting a Bayesian ANOVA in JASP. L’Année Psychologique, 120(1), 73–
96. https://doi.org/10.3917/anpsy1.201.0073
Van Der Laan, L. N., & Orcholska, O. (2022). Effects of digital just-in-time nudges on healthy food
choice – A field experiment. Food Quality and Preference, 98, 104535.
https://doi.org/10.1016/j.foodqual.2022.104535
van Schie, R. J. G., Donkers, B., & Dellaert, B. G. C. (2012). Savings adequacy uncertainty: Driver or
obstacle to increased pension contributions? Journal of Economic Psychology, 33(4), Article
4. https://doi.org/10.1016/j.joep.2012.04.004
Wang, S., Li, L. Z., & Coutts, A. (2022). National survey of mental health and life satisfaction of gig
workers: The role of loneliness and financial precarity. BMJ Open, 12(12), e066389.
https://doi.org/10.1136/bmjopen-2022-066389
Wang-Ly, N., & Newell, B. R. (2022). Allowing early access to retirement savings: Lessons from
Australia. Economic Analysis and Policy, 75, 716–733.
https://doi.org/10.1016/j.eap.2022.07.002
Electronic copy available at: https://ssrn.com/abstract=4509925

Weatherly, J. N., Terrell, H. K., & Derenne, A. (2010). Delay discounting of different commodities.
The Journal of General Psychology, 137(3), 273–286.
https://doi.org/10.1080/00221309.2010.484449
West, C., Whillans, A., & DeVoe, S. (2020). Income volatility increases financial impatience (No. 21–
053; Working Paper). Harvard Business School.
https://www.hbs.edu/ris/Publication%20Files/21-053_54843a1e-7599-4981-a829-
bac3234830cc.pdf
Electronic copy available at: https://ssrn.com/abstract=4509925

ONLINE APPENDIX
Electronic copy available at: https://ssrn.com/abstract=4509925

Appendix A – Demographic and financial characteristics of our samples
Table A1. Demographic characteristics of samples in Experiments 1 to 4.
|                                  | Exp 1  Exp 2  | Exp 3  Exp 4  |
| -------------------------------- | ------------- | ------------- |
| N                                | 241  241      | 150  80       |
| Age (%)                          |               |               |
|    18-24 years old               | 11.6  10.8    | 9.3  17.5     |
|    25-34 years old               | 27.4  27.4    | 34.7  25.0    |
|    35-44 years old               | 26.1  28.2    | 24.0  31.2    |
|    45-54 years old               | 20.3  20.3    | 20.0  17.5    |
|    55-64 years old               | 13.7  12.4    | 12.0  6.3     |
|    65 years or older             | 0.8  0.8      | 0.0  1.3      |
|    Prefer not to say             | 0.0  0.0      | 0.0  1.3      |
| Gender (%)                       |               |               |
|    Male                          | 59.8  44.8    | 50.0  42.5    |
|    Female                        | 39.4  53.9    | 49.3  57.5    |
|    Non-binary/Gender fluid       | 0.4  0.8      | 0.7  0.0      |
|    Different identity            | 0.4  0.0      | 0.0  0.0      |
|    Prefer not to say             | 0.0  0.4      | 0.0  0.0      |
| Education level (%)              |               |               |
|    Did not complete high school  | 0.8  1.2      | 1.3  2.5      |
|    High school graduate          | 36.1  41.1    | 42.0  35.0    |
   Undergraduate degree (e.g., Bachelor’s degree)  45.2  37.8  40.7  31.2
   Postgraduate degree (e.g., Master’s or Doctoral degree)  17.4  19.1  16.0  30.0
|    Prefer not to say  | 0.4  0.8  | 0.0  1.3  |
| --------------------- | --------- | --------- |
Note. Percentages are rounded and may not sum to 100 percent.

Electronic copy available at: https://ssrn.com/abstract=4509925

Table A2. Financial characteristics of samples in Experiments 1 to 4.
|                             | Exp 1  | Exp 2  | Exp 3  | Exp 4  |
| --------------------------- | ------ | ------ | ------ | ------ |
| N                           | 241    | 241    | 150    | 80     |
| Employment status (%)       |        |        |        |        |
|    Full-time                | 61.0   | 52.7   | 55.3   | 48.8   |
|    Part-time                | 16.2   | 20.3   | 16.0   | 21.2   |
|    Contract/Temporary       | 2.5    | 1.7    | 0.0    | 1.3    |
|    Student                  | 4.2    | 6.2    | 3.3    | 10.0   |
|    Unemployed               | 5.0    | 8.3    | 13.3   | 6.3    |
|    Unable to work           | 5.0    | 2.5    | 4.7    | 6.3    |
|    Other                    | 5.0    | 7.8    | 7.3    | 5.0    |
|    Prefer not to say        | 1.7    | 0.4    | 0.0    | 1.3    |
| Pay frequency               |        |        |        |        |
|    Weekly                   | 10.0   | 11.6   | 8.0    | 7.5    |
|    Fortnightly              | 5.0    | 2.1    | 2.7    | 1.3    |
|    Monthly                  | 72.2   | 68.5   | 68.0   | 62.5   |
|    Other                    | 4.2    | 5.8    | 5.3    | 3.8    |
|    Not applicable           | 7.1    | 10.8   | 15.3   | 18.8   |
|    Prefer not to say        | 1.7    | 1.2    | 0.7    | 6.3    |
| Annual personal income (%)  |        |        |        |        |
|    Negative or nil income   | 1.7    | 4.6    | 4.0    | 6.3    |
|    £0-£9,999                | 16.6   | 15.8   | 18.0   | 17.5   |
|    £10,000-£19,999          | 16.2   | 14.1   | 16.7   | 11.2   |
|    £20,000-£29,999          | 20.3   | 25.7   | 25.3   | 20.0   |
|    £30,000-£39,999          | 16.2   | 13.3   | 14.0   | 15.0   |
|    £40,000-£49,999          | 8.7    | 5.8    | 7.3    | 10.0   |
|    £50,000-£59,999          | 5.8    | 4.2    | 4.7    | 1.3    |
|    £60,000-£69,999          | 3.3    | 4.2    | 2.7    | 5.0    |
|    £70,000 or more          | 5.4    | 4.6    | 1.3    | 7.5    |
|    Prefer not to say        | 5.8    | 7.9    | 6.0    | 6.3    |
Note. Percentages are rounded and may not sum to 100 percent.
|     |     |     |     |     |
| --- | --- | --- | --- | --- |
Electronic copy available at: https://ssrn.com/abstract=4509925

Appendix B – Summary of income sequences used across Experiments 1 to 4
Table B1. Dimensions of income sequences used across Experiments 1 to 4.
| Condition  | Incomes (£)  | CV  Min  | Max  Range  |
| ---------- | ------------ | -------- | ----------- |
No Volatility  1,000 1,000 1,000 1,000 1,000  0.00  1,000  1,000  0
1,000 1,000 1,000 1,000 1,000
1,000 1,000 1,000 1,000 1,000
| Low Volatility  | 431 570 656 794 873  | 0.30  431  | 1,340  909  |
| --------------- | -------------------- | ---------- | ----------- |
883 910 990 1,158 1,202
1,277 1,279 1,311 1,326 1,340
High Volatility  173 274 466 526 529  0.60  173  2,088  1,915
650 661 847 1,101 1,374
1,404 1,436 1,571 1,900 2,088
| Same Range  | 173 881 911 929 946   | 0.37  173  | 2,088  1,915  |
| ----------- | --------------------- | ---------- | ------------- |
952 956 981 989 996
1,022 1,041 1,063 1,072 2,088
| Same Min  | 173 552 654 851 863   | 0.37  173  | 1,580  1,407  |
| --------- | --------------------- | ---------- | ------------- |
864 889 1,017 1,036 1,211
1,240 1,257 1,310 1,503 1,580
| Same Max  | 681 689 746 767 772   | 0.37  681  | 2,088  1,407  |
| --------- | --------------------- | ---------- | ------------- |
782 785 816 983 994
1,029 1,242 1,275 1,351 2,088
| Very High Volatility  | 44 152 184 299 372  |     |     |
| --------------------- | ------------------- | --- | --- |
536 763 767 788 1,101
1,300 1,618 1,654 1,965 3,457
Note. CV = Coefficient of variation. Min = Minimum income. Max = Maximum income.
|     |     |     |     |
| --- | --- | --- | --- |
Electronic copy available at: https://ssrn.com/abstract=4509925

Appendix C – Experimental instructions for financial decision making task
The following instructions were given to participants in Experiments 1, 2, and 4. Horizontal rules are
used to indicate different instruction screens.
About this study
• This study is being run by UNSW Sydney to investigate how people make financial
decisions when faced with uncertainty.
• You will make decisions around spending and saving in a financial decision making game,
as well as answer some simple questionnaires.
• You will receive £3.00 for participating in this experiment and may be eligible for a bonus
payment of £3.00 depending on your performance in the game.
How this experiment will run:
• You will first be presented instructions that explain how the financial decision making
game works.
• You will then be given a few practice rounds to get familiar with the game.
• After the practice rounds, you will begin the real experiment rounds.
• Finally, you will be asked to provide some information about yourself and your financial
situation.
• The experiment should take about 20 minutes to complete. If you have any questions or
issues during or after the experiment, please contact Nathan Wang-Ly (nathan.wang-
ly@unsw.edu.au).
• Press the Continue button to proceed to the consent form for this experiment.
How the Game Works – Working for Income
The game will consist of multiple rounds where you will be asked to complete work tasks. Your task
each round will be to arrange a sequence of letters in alphabetical order (see example image
below). After completing each work task, you will receive money as your income.
How the Game Works – Spending or Saving
Each time you receive your income, you will be asked to decide how much of your money you want
to spend or save. You can spend your money to buy points (1 point per £1 spent). These points will
be used to determine whether you are eligible for a bonus payment. Any money that you don't spend
will remain in your account as savings and carry over to future rounds.
Electronic copy available at: https://ssrn.com/abstract=4509925

How the Game Works – The Financial Emergency
At the end of the game, a financial emergency will occur that you will need to pay for. If you have
enough saved in your account when this happens, you will win the game and get to keep your
points. However, if you do not have enough saved, you will lose the game and lose all your points.
How the Game Works – Bonus Payment
Once we have finished collecting data for this experiment, the best performing participants (top
10% of scores) will receive a bonus payment of £3.00 in addition to their participation payment.
Your goal is therefore to buy as many points as you can while still making sure you have enough
saved for the financial emergency. Remember: You will not be told when this emergency will occur
nor how much it will cost.
You will now get to play a few practice rounds to become familiar with how everything works. Just
like in the real game, a financial emergency will occur at the end of these rounds. Once you finish
with the practice rounds, the points you have earned and your account balance will be reset, and
you will begin the experiment rounds. Click Continue when you are ready to begin.
[After practice rounds had been completed]
Thank you for completing the practice rounds. You will now begin the real experiment rounds. Your
points and savings balance have been reset to zero. The number of rounds and the cost of the
financial emergency will be different for the experiment stage. Your goal remains the same: To buy
as many points as you can while making sure you have enough saved for the financial emergency.
Important: You will later be asked questions about the income you received and your decisions to
spend or save so please ensure you are paying attention throughout the game.
Electronic copy available at: https://ssrn.com/abstract=4509925

The following instructions were given to participants in Experiment 3. Horizontal rules are used to
indicate different instruction screens.
About this study
• This study is being run by UNSW Sydney to investigate how people make financial
decisions when faced with uncertainty.
• You will make decisions around spending and saving in a financial decision making game,
as well as answer some simple questionnaires.
• You will receive £4.50 for participating in this experiment and may be eligible for a bonus
payment of £3.00 depending on your performance in the game.
How this experiment will run:
• You will first be presented instructions that explain how the financial decision making
game works.
• You will then be given a few practice rounds to get familiar with the game.
• After the practice rounds, you will be given the opportunity to play the game twice.
• Finally, you will be asked to provide some information about yourself and your financial
situation.
• The experiment should take about 30 minutes to complete. If you have any questions or
issues during or after the experiment, please contact Nathan Wang-Ly (nathan.wang-
ly@unsw.edu.au).
• Press the Continue button to proceed to the consent form for this experiment.
How the Game Works – Working for Income
The game will consist of multiple rounds where you will be asked to complete work tasks. Your task
each round will be to arrange a sequence of letters in alphabetical order (see example image
below). After completing each work task, you will receive money as your income.
How the Game Works – Spending or Saving
Each time you receive your income, you will be asked to decide how much of your money you want
to spend or save. You can spend your money to buy points (1 point per £1 spent). These points will
be used to determine whether you are eligible for a bonus payment. Any money that you don't spend
will remain in your account as savings and carry over to future rounds.
Electronic copy available at: https://ssrn.com/abstract=4509925

How the Game Works – The Financial Emergency
At the end of the game, a financial emergency will occur that you will need to pay for. If you have
enough saved in your account when this happens, you will win the game and get to keep your
points. However, if you do not have enough saved, you will lose the game and lose all your points.
How the Game Works – Two Attempts
You will be given the opportunity to play the game twice. The timing and cost of the financial
emergency may be different between attempts. The income you receive may also differ. The cost of
the financial emergency and the outcome of each game will only be revealed once you have
completed both attempts. However, your performance in your first attempt will not affect the second
attempt. Your points and savings will be reset to zero in between attempts.
How the Game Works – Bonus Payment
After you have completed both attempts, we will add up your points from each attempt to give a
final score for the experiment. If your final score is within the top 10% of participants who
complete this experiment, you will receive a bonus payment of £4.50 in addition to your
participation payment.
You will now get to play a few practice rounds to become familiar with how everything works. Just
like in the real game, a financial emergency will occur at the end of these rounds. Once you finish
with the practice rounds, the points you have earned and your account balance will be reset, and
you will begin your first attempt at the game. Click Continue when you are ready to begin.
[After practice rounds had been completed]
Thank you for completing the practice rounds. You will now begin your first attempt at the game.
Your points and savings balance have been reset to zero. The number of rounds and the cost of the
financial emergency will be different for the experiment stage. Your goal remains the same: To buy
as many points as you can while making sure you have enough saved for the financial emergency.
Important: You will later be asked questions about the income you received and your decisions to
spend or save so please ensure you are paying attention throughout the game.
Electronic copy available at: https://ssrn.com/abstract=4509925

[After participants provided responses to the perceived income volatility measure for their first task
attempt]
Thank you for answering the question. Your performance in the first attempt has been recorded and
we will now begin the second attempt when you press the button below. As this is a new attempt,
your points and savings balance have been reset to zero. Your goal remains the same: To buy as
many points as you can while making sure you have enough saved for the financial emergency.
Remember: The timing and cost of the financial emergency may be different for this attempt. The
income you receive may also differ.
Electronic copy available at: https://ssrn.com/abstract=4509925

Appendix D – Select screenshots of financial decision making task
Figure D1. Introduction to the experimental study.
Figure D2. Example “work task” where participants rearranged a six-character string of letters into
alphabetical order.
Electronic copy available at: https://ssrn.com/abstract=4509925

Figure D3. Example of participant receiving income upon completion of their work task.
Figure D4. Example of participant deciding how much of their available funds to use on purchasing
points.
Electronic copy available at: https://ssrn.com/abstract=4509925

Figure D5. Example feedback screen indicating how many points participants had purchased, their
new points total, and their remaining savings.
Figure D6. Perceived income volatility rating scale. Slider was set by default at 5 but was required to
be moved to progress to the next screen.
Electronic copy available at: https://ssrn.com/abstract=4509925

Figure D7. Perceived financial difficulty rating scale. Slider was set by default at 5 but was required
to be moved to progress to the next screen.
Figure D8. Financial impatience measure requiring participants to provide a hypothetical ‘smaller-
sooner’ amount that would be preferred immediately over a larger later payment.
Electronic copy available at: https://ssrn.com/abstract=4509925

Figure D9. Announcement of the financial emergency occurring.
Figure D10. Outcome screen for a participant who won by saving adequately for the emergency.
Participants who lost were shown a similar screen but were advised that they had lost their purchased
points.
Electronic copy available at: https://ssrn.com/abstract=4509925