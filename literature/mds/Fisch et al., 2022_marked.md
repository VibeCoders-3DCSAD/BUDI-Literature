---
conversion_metadata:
  converted_at: "2026-10-11T15:07:09Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Fisch et al., 2022.pdf"
  source_pdf_sha256: "2d018a39c5eb3d76534935513cfe031f653294d28951ca5365a48b6053c65aa2"
  page_count: 15
  markdown_char_count: 60314
---

Received:7July2021 Accepted:3August2021 Publishedon:3June2022
DOI:10.1002/sam.11586
RESEARCH ARTICLE
A linear time method for the detection of collective
and point anomalies
AlexanderT.M.Fisch1 IdrisA.Eckley2 PaulFearnhead2
1STOR-iCentreforDoctoralTraining,
Abstract
LancasterUniversity,Lancaster,UK
Thechallengeofefficientlyidentifyinganomaliesindatasequencesisanimpor-
2DepartmentofMathematicsand
Statistics,LancasterUniversity,Lancaster, tant statistical problem that now arises in many applications. Although there
UK
has been substantial work aimed at making statistical analyses robust to out-
Correspondence liers,orpointanomalies,therehasbeenmuchlessworkondetectinganomalous
IdrisA.Eckley,Departmentof segments, or collective anomalies, particularly in those settings where point
MathematicsandStatistics,Lancaster
anomalies might also occur. In this article, we introduce collective and point
University,Lancaster,UK.
Email:i.eckley@lancaster.ac.uk anomalies(CAPA),acomputationallyefficientapproachthatissuitablewhen
collectiveanomaliesarecharacterizedbyeitherachangeinmean,variance,or
Fundinginformation
BritishTelecommunicationsplc; both,anddistinguishesthemfrompointanomalies.Empiricalresultsshowthat
EngineeringandPhysicalSciences CAPAhasclosetolinearcomputationalcostaswellasbeingmoreaccurateat
ResearchCouncil,Grant/Award
detectingandlocatingcollectiveanomaliesthanotherapproaches.Wedemon-
Numbers:EP/K032208/1,EP/L015692/1,
EP/N031938/1,EP/R014604/1 stratetheutilityofCAPAthroughitsabilitytodetectexoplanetsfromlightcurve
data from the Kepler telescope and its capacity to detect machine faults from
temperaturedata.
KEYWORDS
dynamicprogramming,epidemicchangepoints,exoplanets,NumentaAnomalyBenchmark,
outliers,robuststatistics
1 INTRODUCTION Conversely,collectiveanomaliesaredefinedassequences
ofobservationsthatarenotnecessarilyanomalouswhen
Anomalydetectionisanareaofconsiderableimportance consideredindividually,buttogetherformananomalous
formanytimeseriesapplications,suchasfaultdetection pattern.
or fraud prevention, and has been subject to increasing A number of different approaches can be taken to
attention in recent years. See [6, 33] for comprehensive detect point (i.e., contextual and/or global) anomalies.
reviews of the area. As Chandola et al. [6] highlight, Theseareobservationsthatdonotconformwiththepat-
anomalies can fall into one of three categories: global tern of the data. Hence, the problem of detecting point
anomalies,contextualanomalies,orcollectiveanomalies. anomalies can be reformulated as inferring the general
Global anomalies and contextual anomalies are defined patternofthedatainamannerthatisrobusttoanomalies.
as single observations that are outliers with regard to Thefieldofrobuststatisticsoffersawiderangeofmethods
thecompletedatasetandtheirlocalcontext,respectively. aimedatthisproblem[7,31,34,36].Themachinelearning
ThisisanopenaccessarticleunderthetermsoftheCreativeCommonsAttributionLicense,whichpermitsuse,distributionandreproductioninanymedium,providedthe
originalworkisproperlycited.
©2022TheAuthors.StatisticalAnalysisandDataMiningpublishedbyWileyPeriodicalsLLC.
494 wileyonlinelibrary.com/sam StatAnalDataMin:TheASADataSciJournal.2022;15:494–508.

FISCHetal. 495
community has also provided a rich corpus of work for Methodsspecificallyaimedatdetectingepidemicchanges
the detection of point anomalies. Commonly used meth- tend to use scan statistics [5, 19, 39], which involve test-
ods include nearest-neighbor-based approaches, such as ing many, or all, possible intervals for whether they con-
the local outlier factor [4], and information theoretical tain a collective anomaly. Often the challenge for these
methods such as the one introduced by Guha et al. [15]. procedures is that a true collective anomaly may overlap
It is beyond the scope of this paper to review them all. manytestedintervalsandthusonecollectiveanomalymay
Instead, we refer to excellent reviews that can be found leadtomanysignificanttests—andanalgorithmneedsan
in [6, 33]. References [1, 25, 42] and references therein automatedandreliablewaytochoosewhichtoflagasthe
provide examples of more recent developments in the actualcollectiveanomalies.Furthermore,manyproposed
area. methods are not robust to the presence of point anoma-
One common drawback of several point anomaly lies.Bycomparison,weproposeanapproachthatjointly
approaches is their limited ability to detect anomalous estimatesbothcollectiveandpointanomalies.
segments, or collective anomalies. Such features are of This article introduces an estimation procedure that
significance in many applications, such as in analyz- allowsfortheidentificationofcollectiveandpointanoma-
ing brain imaging data [2] or detecting regions of the lies (CAPA). The CAPA procedure is based on minimiz-
genome with unusual copy number [3, 39, 45]. Current ing a penalized cost, and thus can be easily adapted
methods for detecting collective anomalies include hid- to many different applications by appropriate choice of
denMarkovmodels,smoothing-basedapproaches,orepi- cost—though our current implementation focuses on
demicchangepointmethods.HiddenMarkovmodels[40] anomaliesthatcorrespondtochangesinmeanorinmean
arenaturalforapplicationswherecollectiveanomaliesare and variance. Furthermore we demonstrate empirically
restrictedtobeofasmallnumberofdifferenttypes,such that it scales well to large data, with a computational
as for detecting copy number variation where different cost that is linear in the number of data points. Since
states of the hidden Markov model would correspond to the first version of CAPA appeared on arXiv [10], a sim-
different, discrete, values for the copy number. But they ilaralgorithmhasbeenindependentlyproposedbyZhao
are less appropriate in situations where each collective andYau[46].Whilefocusedonanepidemicchangepoint
anomalyisdistinct,andtheytendtobeslowtofit,which setting,ZhaoandYau[46]doesnotexplicitlyconsiderdis-
canmaketheminfeasibleforsomebig-dataapplications. tinguishing between point and collective anomalies. As
Bycomparison,smoothing-basedapproaches,liketheone we show in the simulation results, methods that do not
proposed by Schwartzman et al. [38], are often very fast. allow for point anomalies can perform poorly if they are
However, thesmoothingsteplimitsinterpretabilitymak- present.
ing the approach vulnerable to point anomalies and dif- We provide some theoretical justification for our
ferentiatingbetweenpointandcollectiveanomaliesnigh methodbyshowingthatCAPAisconsistentwhenanalyz-
impossible.Furthermore,thesemethodsachieveoptimal ingdatawithoutpointanomalies.Wefurtherdemonstrate
powerwhenthebandwidthofthesmoothingkernelisof empirically the performance of CAPA in a simulation
thesamelengthscaleasthecollectiveanomalies,meaning study,whereitisshowntooutperformanumberofalter-
thattheycanstrugglewhenanomaliesareofverydifferent native approaches to detecting collective anomalies. We
lengths. also apply CAPA to two real datasets. The first dataset is
Asaresult,ourapproachisbasedonmodelingcollec- lightcurve data gathered by the Kepler space telescope.
tive anomalies as epidemic changepoints. The epidemic There we show that CAPA can be used to detect Kepler
changepoint model, first introduced by Levin and Kline 1132-b, an exoplanet which orbits the star Kepler 1132
[26],assumesthatthereisatypicalbehavior,fromwhich [30].Theseconddatasetisamachinetemperaturedataset
the data deviates during collective anomalies. Epidemic obtained on an expensive industrial machine. There we
changepoints can therefore be viewed as two classical showthatCAPAcanbeusedtodetectbothcriticalfailures
changepoints:oneawayfromandonebacktothetypical aswellasearlywarningsigns,highlightingthealgorithms
distribution, and a simple approach to detecting collec- usefulness for predictive maintenance. While CAPA is
tiveanomalieswouldbetouseoneofthemanymethods based on a model that assumes independent noise, our
for changepoint detection (see [8, 14, 18, 22, 28] among application of CAPA to the machine temperature dataset
manyothers).However,thisdoesnotexploitthefactthat shows how it can still be robustly applied to data with
thebehaviorofthesegmentbeforethestartandafterthe strongauto-correlation.
end of an anomalous segment is the same. This reduces CAPA has been implemented in the R package
itsstatisticalpower,ascanbeseeninSection5,whichis anomaly [13] which is available from CRAN, together
adisadvantage,especiallywhenfacedwithaweaksignal. withatutorialintroduction[12].
19321872,
2022,
4,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sam.11586
by
Cochrane
Philippines,
Wiley
Online
Library
on
[10/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

496 FISCHetal.
2 A MODELING FRAMEWORK log-likelihood of Gaussian data. In this case, 𝜃 = (𝜇, 𝜎2)
FOR COLLECTIVE AND POINT containsboththemeanandvarianceandweestimateK,
ANOMALIES s , …,s ,ande , …,e byminimizing
1 K 1 K
[ ( ) ]
Weassumethatthedatafollowaparametricmodelwhere ∑ ( ) x −𝜇̂ 2
log 𝜎̂2 + t 0
collective anomalies are epidemic changes in the model 0 𝜎̂
t∉∪[̃s+1,̃e] 0
parameters. While, in practice, it is unlikely that the dis- i i ( )
t to rib th u e tio s n am of e th fa e m d i a ly ta o i f n d a i n st a r n ib o u m ti a o l n o s us as se t g h m e e d n is t t w rib il u l t b i e o l n on o g f + ∑K̃
⎡
⎢ ⎢ ( ̃e𝑗 −̃s𝑗 )
⎛
⎜ ⎜log
⎛
⎜ ⎜
∑ ̃e
t= 𝑗 ̃s𝑗+1 ( x t −x (̃s )𝑗+1)∶̃e𝑗
2⎞
⎟ ⎟+1
⎞
⎟ ⎟+𝛽
⎤
⎥ ⎥,
thetypicaldata,itcanneverthelessbeexpectedthataset 𝑗=1 ⎢ ⎣ ⎜ ⎝ ⎜ ⎝ ̃e𝑗 −̃s𝑗 ⎟ ⎠ ⎟ ⎠ ⎥ ⎦
ofparametersdifferentfromthetypicaldistributionswill
(2)
offerabetterfit.Wesaythatdatax , …,x followapara-
1 n
metric epidemic changepoint model if x
t
has probability subjecttõe −̃s ≥2,thatis,aminimumsegmentlengthof
i i
densityfunctionf(x
t
,𝜃(t))and 2,toaccountforthefactthat𝜃istwodimensional.
{ It is well known that many changepoint detection
𝜃(t)= 𝜃 𝑗 s𝑗 <t≤e𝑗 , methods struggle in the presence of point anomalies in
𝜃 otherwise, thedataandtendtofittwochangepointsaroundeachof
0
them[8].Anapproachbasedonminimizingtheabovecost
where 𝜃 is the, usually unknown, parameter of the typ- functionisnotintrinsicallyimmunetothisphenomenon
0
ical distribution, from which the model deviates during either.However,giventhatpointoutlierscannaturallybe
the K anomalous segments (s 1 , e 1 ), …,(s K , e K ) by adopt- viewed as single observations with a larger variance, we
ing behaviors characterized by the parameters 𝜃 1 , …,𝜃 K can incorporate them in the model as epidemic changes,
all different from 𝜃 0 . We assume these windows do not i ( n var ) iance ( only, o ) f length one. We therefore choose K ̃ , overlap,thatis,e 1 ≤s 2 , …,e K−1 ≤s K .Fittinganepidemic ̃s 1 ,̃e 1 , …, ̃s K̃ ,̃e K̃ , 𝜇 0 , 𝜎 0 , as well as the set of point
changepoint requires only one new set of parameters anomalies O⊂{1, …,n}, which minimize the modified
for 𝜃, since the typical parameter is shared across the
penalizedcost
non-anomalous segments. This compares favorably with
the two additional sets of parameters for 𝜃 introduced ∑ [ ( ) ( x −𝜇̂ ) 2 ] whenanepidemicchangepointisfittedusingtwoclassi- log 𝜎̂2 + t 0
0 𝜎̂
cal changepoints. We can therefore expect to gain statis- t∉∪[̃s i + ∑ 1,̃e i ] [ ∪O (( ) 0 ) ]
tical power, which is confirmed by the empirical results + log x −𝜇̂ 2 +𝛾𝜎̂2 +1+𝛽′
t 0 0
inSection5. t∈O
( )
ciat O ed ur w a i p th pr t o h a e ch no is rm to a f l ir s s t t a e te s , tim 𝜃̂ 0 a , t u e s t i h n e g p s a t r a a n m da e r t d ers ro a b s u so st - + ∑K̂ ⎡ ⎢ ⎢ ( ̃e𝑗 −̃s𝑗 ) ⎛ ⎜ ⎜log ⎛ ⎜ ⎜ ∑ ̃ t e = 𝑗 ̃s𝑗+1 ( x t −x (̃s )𝑗+1)∶̃e𝑗 2⎞ ⎟ ⎟+1 ⎞ ⎟ ⎟+𝛽 ⎤ ⎥ ⎥,
statisticalmethods,seeSection3.Itisthenpossibletoinfer 𝑗=1 ⎢
⎣
⎜
⎝
⎜
⎝
̃e𝑗 −̃s𝑗 ⎟
⎠
⎟
⎠
⎥
⎦
the num(ber a)nd loc(ation o)f epidemic changes by choos-
ing K ̃ , ̃s 1 ,̃e 1 , …, ̃s K̃ ,̃e K̃ , to minimize the penalized (3)
cost
where 𝛽′ is a penalty smaller than 𝛽. This modification
∑ ( ) ∑K̂ ⎡ ⎛ ∑̃e𝑗 ( )⎞ ⎤ ensures that it is now cheaper to fit an outlier as an epi-
 x t ,𝜃̂ 0 + ⎢ ⎢ min ⎜ ⎜  x t ,𝜃̃ 𝑗 ⎟ ⎟ +𝛽⎥ ⎥ , demicchangepointinvarianceonly,ratherthanasafull
t∉∪[̃s
i
+1,̃e
i
] 𝑗=1⎣
𝜃̃
𝑗 ⎝t=̃s𝑗+1 ⎠ ⎦ epidemic change. The constant, 𝛾>0 ensures that the
(1) argumentofthelogarithmwillbelargerthan0.Werecom-
subject to e i −s i
≥̂
l, where
̂
l is the minimum segment mendsetting𝛾tothelevelof(preci)sionoftheobservations,
length,foranappropriatecostfunction(x,𝜃)andasuit- subjecttorequiring𝛾 >exp −𝛽′ whichensuresthatno
ablepenalty,𝛽.Forexample,(x,𝜃)couldbedefinedasthe
inliersarefittedaspointanomalies,asshownbyProposi-
negative log-likelihood of x under the parametric model tion3inSection4.
using parameter 𝜃. A common choice for the penalty 𝛽 Thismodificationhastheaddedbenefitthatitallows
wouldthenbe𝛼log(n)[14,22,44],wheretheconstant𝛼 the algorithm to distinguish between point and collec-
dependsonthemodelconsidered. tive anomalies. This property is important for a range
Using the formulation in (1), we can infer the loca- of applications in which collective and point anoma-
tion of joint epidemic changes in mean and variance lies have different interpretations (see Section 6.1 for an
by minimizing the penalized cost related to the negative example).
19321872,
2022,
4,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sam.11586
by
Cochrane
Philippines,
Wiley
Online
Library
on [10/10/2026].
See the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are governed
by
the
applicable
Creative
Commons
License

FISCHetal. 497
(
3 ESTIMATION OF COLLECTIVE
min C(k)+(m−k)
AND POINT ANOMALIES
0≤k≤m−2
[ ( ) ] )]
We now turn to consider the problem of minimizing the ∑m ( )
penalized cost SD introduced in the previous section. log 1 x −x 2 +1 +𝛽 ,
t (k+1)∶m
m−k
Unlikeintheclassicalchangepointproblemconsideredby t=k+1
Jacksonetal.[17],thepenalizedcostgivenbyEquation(1)
where𝜇̂ and𝜎̂2 aretheestimatedmeanandvariancefor
cannotbeminimizedusingadynamicprogram,sincethe 0 0
parameter𝜃 issharedacrossmultiplesegmentsandtypi- non-anomalous data, minimizes the approximate penal-
0
izedcostforjointepidemicchangesinmeanandvariance
callyunknown.Wethereforeuserobuststatisticstoobtain
anestimate,𝜃̂ ,for𝜃 fromthefulldata.Suchrobustesti- defined in Equation (2). As a by-product of minimiz-
0 0
ing this, it is straightforward to get the set of anomalous
mates can be obtained for a variety of models [16, 20].
regions that correspond to the minimum and these give
For example, the median, M-estimators, or the clipped
our estimates of the number and location of collective
mean can be used to robustly estimate the mean. The
anomalies.Similarly,wecanminimizetheapproximation
interquartilerange,themedianabsolutedeviation,orthe
to its point anomaly robust analogue in Equation (3) by
clippedSDcanbeusedtoestimatethevariance.Bycom-
solvingthedynamicprogram
parison, an approach advocated by Zhao and Yau [46]
is to alternately estimate the collective anomalies condi- [ ( )
tional on an estimate for 𝜃 0 , and then estimate 𝜃 0 given C(m)=min C(m−1)+log ( 𝜎̂2 ) + x m −𝜇̂ 0 2 ,
0 𝜎̂
the collective anomalies. This leads to a larger computa- 0
tional overhead than CAPA. Furthermore, it is possible (
to extend CAPA to an online setting [9], while this is
min C(k)+(m−k)
not possible when using such an alternating estimation 0≤k≤m−2
procedure. [ ( ) ] )
Havingobtained𝜃̂
0 ,wethenminimize log 1
∑m (
x −x
)
2 +1 +𝛽 ,
t (k+1)∶m
m−k
∑ ( ) ∑K̂ ⎡ ⎛ ∑̂e𝑗 ( )⎞ ⎤ t=k+1 ]
t∉∪[̂s i +1,̂e i ]  x t ,𝜃̂ 0 + 𝑗=1 ⎢ ⎢ ⎣ m 𝜃̂ i 𝑗 n ⎜ ⎜ ⎝t=̂s𝑗+1  x t ,𝜃̂ 𝑗 ⎟ ⎟ ⎠ +𝛽⎥ ⎥ ⎦ , C(m−1)+1+log ( 𝛾𝜎̂ 0 2+ ( x m −𝜇̂ 0 ) 2 ) +𝛽′ ,
(4)
as an approximation to (1). Since it can be expected that
most data belongs to the typical distribution,
𝜃̂
should
thus also inferring the number and location of point
0
anomalies, with a negligible increase in computational
becloseto𝜃 .Onemightthereforeexpectthatusingthis
0
cost.WecallthisalgorithmCAPA.Pseudocodeforthefull
estimatewillhavelittleimpactontheperformanceofthe
CAPAalgorithmisgivenbyAlgorithm1intheSupporting
method,andweshowthistheoreticallyforjointchanges
Information.
inmeanandvarianceinSection4.2.
Solving the full dynamic program is at least O(n2).
Theapproximationtothepenalizedcostin(5)canbe
This is because it requires n steps over a solution space
minimizedexactlybysolvingthedynamicprogram
0≤k≤m−l, which is of size O(n) on average. However,
[
( ) wecanreducethesizeofthesolutionspacebyborrowing
C(m)=min C(m−1)+ x 𝜃̂ , ideas on pruning from [22], provided the loss function is
m 0
( ( ) )] suchthataddingafreechangepointwillnotincreasethe
∑m ( ) cost—a property which holds for many commonly used min C(k)+min  x𝜃̂ +𝛽 ,
t costfunctionssuchasthenegativelog-likelihood.Indeed,
0≤k≤m− ̂ l 𝜃̂ t=k+1 thefollowingpropositionholds:
(5)
Proposition1. Letthecostfunction,(⋅,⋅),besuchthat
whereC(m)isthecostofthemostefficientpartitionofthe ( ) ( )
∑c ∑b−1
firstmobservationsandC(0)=0.Forexample,solvingthe
min (x,𝜃) ≥min (x,𝜃)
dynamicprogram 𝜃 t 𝜃 t
t=a t=a
( ) [
( ) ∑c
C(m)=min C(m−1)+log ( 𝜎̂2 ) + x m −𝜇̂ 0 2 , +min (x t ,𝜃) 0 𝜎̂ 𝜃
0 t=b
19321872,
2022,
4,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sam.11586
by
Cochrane
Philippines,
Wiley
Online
Library
on
[10/10/2026].
See
the
Terms
and Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

498 FISCHetal.
( ) ( )
holdsforalla,b,andcsuchthata+ ̂ l≤b<c− ̂ l.Then,if 𝜇(t),𝜎(t)2 = 𝜇 ,𝜎2 ,fort +1≤t≤t . (7) k+1 k+1 k k+1
( )
∑m Here 0 = t ≤ … ≤ t = n denote the start of the
C(k)+min (x,𝜃) ≥C(m) (6) 0 K+1
𝜃 t series, the K changepoints, and the end of the series.
t=k
We assume that the mean and/or varian(ce change)s
( )
holds for some k<m− ̂ l, we can exclude that k from the at these changepoints, that is 𝜇 k ,𝜎 k 2 ≠ 𝜇 k+1 ,𝜎 k 2 +1 .
solutionspaceforallfuturestepsm′ ≥m+ ̂ lofthedynamic These changes in mean and variance can be of varying
program. strength. To quantify this, we define the signal strength
△ 𝜎,k of the change in variance at the kth changepoint
Thus,wecankeeptrackofthesetoftimeindicesthat
tobe
we need to minimize over in the dynamic program. For
(√ √ )
each of these, we check, at each time step, if (7) holds, 𝜎 𝜎 2 𝜎 𝜎
△2 = k − k+1 = k + k+1 −2.
and, if it does, we remove the index from the set. See 𝜎,k 𝜎 𝜎 𝜎 𝜎
k+1 k k+1 k
steps15–22ofAlgorithm2intheSupportingInformation
formoredetail.Thiscansignificantlyreducethecompu- Wenotethat△2 isequalto0if,andonlyif,𝜎 =𝜎 .
𝜎,k k+1 k
tational cost. In practice, we found that it was close to Wealsodefinethesignalstrength△ 𝜇,k ofchangeinmean
O(n)forthedetectionofjointepidemicchangesinmean
atthekthchangepointtobe
andvariancewhenthenumberoftrueepidemicchanges
increased linearly with the number of observations. The |𝜇 −𝜇 |
time after which a k can be discarded in the minimiza- △ 𝜇,k = √k 𝜎 𝜎 k+1 .
k k+1
tion step also depends on the minimum segment length,
somethingnotconsideredby[22]. These two quantities can be combined into a global
measureofsignalstrength
( )
4 THEORY FOR JOINT CHANGES 1 1
△ =log 1+ △2 + △2
IN MEAN AND VARIANCE k 2 𝜎,k 4 𝜇,k
forthekthchange(seeLemma7intheSupportingInfor-
We now introduce some theoretical results for CAPA.
In particular, we establish the consistency of CAPA at mationfordetails). ( ) detectingcollectiveanomalieswhenanalyzingdatawith- Wenowdefinethep{enalizedcost̃ x i∶}𝑗 ,𝜏′,𝛼 ofdata
out point outliers. To do this, we demonstrate that it can x i:j underpartition𝜏′ = i−1,̂ t 1 ′, … ,̂ t K ′ ̂′ ,𝑗 tobe
be viewed as a corollary of the consistency of a statis-
tical procedure, such as optimal partitioning from [17], ( ) ∑K̂′ ( )
that minimizes a penalized cost function to detect clas- ̃ x i∶𝑗 ,𝜏′,𝛼 = ̃ x (̂t +1)∶̂t +K ̂′𝛼log(n)1+𝛿,
k k+1
sical (i.e., nonepidemic) changepoints. Consequently, we k=0
will begin by proving the consistency of a penalized cost
for 𝛿, 𝛼>0. Here, 𝛼log(n)1+𝛿 corresponds to the com-
methodforthedetectionofchangesinmeanandvariance
monly used strengthened SIC-type penalty [14, 27] for
inSection4.1.Wethenproceedtoprovingtheconsistency
introducinganadditionalchangepoint.Thecostofaseg-
of CAPA at detecting collective anomalies in Section 4.2.
mentx issettobe
Like other cost function-based approaches, CAPA is sig- a:b
nificantlyaffectedbythechoiceofpenalties.Wetherefore
̃ (x )=̃ (x ,{a−1,b})
concludethissectionbydiscussingsuitablechoicesforthis a∶b a∶b
important hyper parameter in Section 4.3. The proofs of ( (∑ ( ) ) )
alltheoremsandpropositionsstatedinthissectioncanbe =(b−a+1) log b a x t −x a∶b 2 +1 ,
foundintheSupportingInformation. b−a+1
which is the same as the segment cost used to infer the
4.1 Consistencyofclassical
locationofepidemicchangesinmeanandvariance.Since
changepointdetection
this leaves two parameters to fit, we impose a minimum
segmentlengthoftwoforallpartitions.
Considerthesequencex 1 , … ,x n ∈Rn whichisnormally We also introduce the following assumption which
distributedwithK ∈Nchangepoints.Thesequencethere- ensuresthatthechangepointsaresufficientlyspacedapart
foresatisfiesx =𝜇(t)+𝜎(t)𝜂 for𝜂
i.
∼
i.d.
N(0,1),where toallowfortheirdetection:
t t t
19321872,
2022,
4, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sam.11586
by
Cochrane
Philippines,
Wiley
Online
Library
on
[10/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of use; OA
articles
are
governed
by
the
applicable
Creative
Commons
License

FISCHetal. 499
Assumption 1. There exists some
𝛿̃>0
such that for epidemicchangepointmodelbysetting
1≤k≤K+1
𝜎 𝜎 |𝜇 −𝜇 |
△2 𝜎,k = 𝜎 k + 𝜎 0 −2 and △ 𝜇,k = √k 𝜎 𝜎 0 . log(n)1+𝛿+𝛿̃ 0 k k 0
t −t ≥ ( ),
k k−1 min △ ,△2,△ ,△2
k k k−1 k−1 Wemakethefollowingassumptions:
where△ =△ =∞forconvenienceofnotation. Assumption2.
(a)Thereexistssome𝛿̃>0suchthatfor
0 K+1
1≤k≤K
Then,thefollowingconsistencyresultholds:
log(n)1+𝛿+𝛿̃
Theorem1. Assumethatobservationsx , …,x followthe e −s ≥ ( ),
1 n k k min △ ,△2
distribution specified in (7) and that Assumption 1 holds. k k
LetK ̂ and ̂ t 1 , … ,̂ t K̂ bethenumberandlocationsofchange- s −e ≥ ( log(n)1+𝛿+𝛿̃ ).
points inferred by minimizing the penalized cost function k+1 k ̃ (x ,𝜏,𝛼).ThenthereexistsaconstantCsuchthat∀𝜀>0 min △ k ,△2 k ,△ k+1 ,△2 k+1
1∶n
thereexistconstantsA(𝛼,𝜀)andB(𝛼,𝛿̃,𝛿,𝜀)suchthat
√
(b)e −s ≤ nfor1≤k≤K.
( ) k k
P K ̂ =K,|̂ t −t |< A ( (𝛼𝜀) )log(n)1+𝛿 1≤k≤K Assumption 2a is analogous to Assumption 1.
k k min △ △2 Assumption 2b is only needed when the parameters of
k k
thetypicaldistributionareunknownandguaranteessthat ≥1−Cn−𝜀
the robust estimates of the typical parameter will con-
vergesquicklyenoughtothegroundtruth.Thefollowing
holdsforalln≥B(𝛼,𝛿̃,𝛿,𝜀).
consistencyresultthenholdsforCAPA:
( )
leng
T
e
h
s
e
su
pr
c
o
h
of
as
of
o
t
b
h
ta
is
in
r
i
e
n
s
g
ul
u
t
p
a
p
d
e
d
r
re
a
s
n
se
d
s
l
s
o
e
w
v
e
e
r
ra
b
l
o
n
u
o
n
v
d
e
s
l c
o
h
n
al
a
- Theorem 2. Let ̂s 1 ,̂e 1 , … ,̂s K̂ ,̂e K̂ be the partition
inferred by CAPA on observations x , …,x using a mini- 1 n
range of transformations of the residual sum of squares mumsegmentlengthof 2and𝛼log(n)1+𝛿aspenaltyforboth
arisingfromthefactthatjointchangesinmeanandvari-
point anomalies and epidemic changepoints. If x , …,x
1 n
ance were considered instead of only changes in mean,
follow the distribution specified above and Assumption 2
as in pre-existing work [14]. In particular, the lower holds,thenthereexistsaconstant C suchthat ∀𝜀>0there
boundonthemomentgeneratingfunctionoftheweighted existconstantsA(𝛼,𝜀)andB(𝛼,𝛿̃,𝛿,𝜀)suchthat
sum of 𝜒2-distribution in Lemma 12 is of independent (
interest. P K ̂ =K, |̂e −e |< A ( (𝛼𝜀) )log(n)1+𝛿,
k k min △ △2
k k
)
4.2 ConsistencyofCAPA
A(𝛼𝜀)
|̂s −s |< ( )log(n)1+𝛿 1≤k≤K
k k min △ △2
The results we obtained in the previous section can be k k
extendedtoprovetheconsistencyofCAPAforthedetec- ≥1−Cn−𝜀
tion of joint epidemic changes in mean and variance. As
in the previous section, consider data x
1
, …,x
n
which is holdsforalln≥B(𝛼,𝛿̃,𝛿,𝜀).
oftheformx =𝜇(t)+𝜎(t)𝜂 ,where𝜂 ∼N(0,1).Sincewe
t t t
nowassumeepidemicchanges,wehave Both for this result and Theorem 1, the strengthened
SIC was used as penalty to simplify the exposition of the
{( )
proof.Averysimilarresultcouldbederivedtoshowthat
( 𝜇(t),𝜎(t)2 ) = ( 𝜇 𝑗 ,𝜎 𝑗 2 ) s𝑗 <t≤e𝑗 , an𝛼log(n)typepenaltyforasufficientlylarge𝛼 achieves
𝜇 ,𝜎2 otherwise.
consistency.ThisresultsuggeststhatCAPAfitscollective
0 0
anomaliesassuch,despitebeingabletofitthemasamix-
Here, 𝜇 and 𝜎2 are the typical mean and variance, tureofpointanomaliesanddatabelongingtothetypical
0 0
respectively, and K is the number of epidemic change- distribution.
points.Thevariabless ande denotethestartingandend Theboundsontheaccuracyofthedetectedepidemic
k k
pointofthekthanomalouswindow,respectively.Treating changepoints can be tightened. For all 𝛿>𝛿 , it is pos-
0
thes ande likeclassicalchangepointsallowsustoextend sible to show that the detected epidemic changepoints
k k
the definitions of △ 𝜎 and △ 𝜇, and therefore △, to the mustbewithin A(𝛼,𝜀) log(n)1+𝛿 0 ofthetrueepidemic
min(△ ,△2)
k k
19321872,
2022,
4,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sam.11586
by Cochrane
Philippines,
Wiley
Online
Library
on
[10/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use; OA
articles
are
governed
by
the
applicable
Creative
Commons
License

500 FISCHetal.
( ) ( )
changepointsoncen≥B(𝛼,𝛿̃,𝛿,𝜀)andn≥B 𝛼,𝛿̃,𝛿 ,𝜀 . 𝛾, defined in Section 3, satisfies 1≥𝛾 ≥exp −𝛽′ . Then,
0
thereexistsaconstantK(𝛽′)=𝛽′+o(𝛽′)suchthat
This is because Theorem 1 then also holds for the
penalty 𝛼log(n)1+𝛿 0, which therefore guarantees that the
i∉O ̂ ⇒
(
x −𝜇̂
)
2 <𝜎̂2K
(
𝛽′
)
fitted epidemic changepoints of the optimal partition i
with K fitted epidemic changepoints must be within
A(𝛼,𝜀) log(n)1+𝛿 0 ofthetrueepidemicchangepoints. and
min(△ ,△2)
k k ( ) ( )
x −𝜇̂ 2 >𝜎̂2K 𝛽′
i
{ }
4.3 Penalties ⇒i∈O ̂ ∨∃k∈{1, … ,K ̂ }∶i∈ ̂s +1, … ,̂e .
k k
This proposition defines a threshold for |x −𝜇|/𝜎
Wenowturntotheproblemoftuningthepenalties𝛽 and i
below which the ith observation will not be considered
𝛽′ introduced in Section 2. In the previous section, we
a point anomaly and above which the ith observation
showedthatCAPAisconsistentwhenusingan𝛼log(n)1+𝛿
willnotbeconsideredtypical.Furthermore,thisdetection
penaltyforbothcollectiveandpointanomalies.Theresult
threshold asymptotically behaves like 𝛽′. This provides a
can be tightened slightly to show that consistency is
natural way of choosing the penalty 𝛽′ for point anoma-
achievedbyusingan𝛼log(n)penaltyforcollectiveanoma-
liesbasedonhowlargeoutliers,asmeasuredby|x −𝜇|/𝜎
liesandan𝛼′log(n)penaltyforpointanomaliesforsuffi- i
cientlylargeconstants𝛼and𝛼′.
areassumedtobe.ForGa√ussiandata,extremevaluethe-
oryplacesthethresholdat (2+𝜀)log(n),whichconfirms
Inpractice,werecommendchoosing𝛼and𝛼′withthe
thechoiceof𝛽′derivedfromProposition2.
aim of controlling the asymptotic rate of false positives
Inpractice,thetypicalparametersareoftenunknown
under the null hypothesis that no anomalies—collective
and the constants 𝛼 and 𝛼′ should be slightly inflated
or point—are present. Relatively tight results can be
to reflect this additional uncertainty. This effect on
derived for the case in which the typical mean and vari-
𝛼, is offset by the fact that the Bonferroni correc-
ance are known and the observations are normally dis-
tion used in the proof of Proposition 2 becomes loose
tributed. Indeed, the following proposition holds under
when the minimum segment length exceeds 2 as it does
theseassumptions: not exploit correlations. We chose 𝛽′ =3log(n) and 𝛽 =
Proposition2. Letx , …,x bei.i.d.N(𝜇,𝜎2)distributed, 4log(n)asdefaultpenaltiesforpointandcollectiveanoma-
1 n
for known 𝜇 and 𝜎. Then there exist constants C and C lies, respectively, in our software implementation and 1 2
suchthatwhenthepenaltyforpointanomalies,𝛽′,andthe recommend inflating both penalties, while maintaining
penaltyforco√llectiveanomalies,𝛽,satisfy𝛽′ ≥2𝜓 and𝛽 ≥ their ratio, when dealing with autocorrelated data (see
2(2+2𝜓 +2 2𝜓),then Section6.2).
P(K ̂ =0, O ̂ =∅)≥1−C ne−𝜓 −C (ne−𝜓 )2.
1 2
5 SIMULATION STUDY
forall𝜓>0.
To assess the potential of CAPA, we compare its perfor-
TheproofofthisresultreliesonaboundoftheMGF
mancetothatofotherpopularanomalyandchangepoint
of the cost function under the data distribution and can
methods on simulated data. In particular, we compare
therefore be extended to other cost functions and data
with Pruned Exact Linear Time (PELT) as implemented
distributions and to the classical changepoint setting. As
in the changepoint package [21, 23], a commonly used
a consequence of Proposition 2, setting the penalty for
changepointdetectionmethod,luminol[29],analgorithm
collective anomalies to (4+𝜀)log(n) and the penalty for
developed by LinkedIn to detect segments of atypical
pointanomaliesto(2+𝜀)log(n),where𝜀>0controlsthe
behavior, as well as BreakoutDetection [18] which was
asymptoticrateoffalsepositivesinthisscenario,sincethe
introducedbyTwittertodetectchangesinmeaninaway
probabilityofobservingfalsepositivesthentendsto0asn
whichisrobusttopointanomalies.
tendsto∞.
The simulation study was conducted over simulated
Moreover,thefollowingpropositionholdsundergen-
timeserieseachconsistingof5000observations,forwhich
eral(i.e.,model-free)assumptions:
the typical data follows a N(0, 1) distribution. Epidemic
Proposition3. Let(𝜇̂,𝜎̂),O ̂ ,and𝛽′correspondtotheesti- changepoints occur at a rate of 0.0005 (corresponding to
matedparametersofthetypicaldistribution,theinferredset anaverageofabout2.5epidemicchangesineachseries),
ofpointanomalies,andthepenaltyforpointanomaliesused withtheirlengthbeingi.i.d.Pois(30)-distributed.Ineach
byCAPA,respectively.Assume,moreover,thattheconstant anomaloussegmentthedataisagainnormallydistributed,
19321872,
2022,
4,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sam.11586
by
Cochrane
Philippines,
Wiley
Online
Library
on
[10/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

FISCHetal. 501
with the means being i.i.d. N(0, a2) distributed and SDs 5.2 Precision
i.i.d. Γ(1/b, 1/b) distributed. We used a = 1, and a = 10
for weak and strong changes in mean, respectively, as Wealsoinvestigatedtheprecisionofthetruepositivesfor
well as b = 1 and b = 10 for weak and strong changes the four methods. We compared the mean absolute dis-
invariance,respectively.Shortanomalieswherealsosim- tancebetweendetectedchanges(i.e.,truechangeswhich
ulated using a = b = 5 and collective anomalies of i.i.d. had a detected changes within 20 observations) and the
Pois(6)-distributedlength. nearest estimated change across all the 12 scenarios. We
Wecomparedtheperformanceofthefourmethodsin used the default penalties for all methods (i.e., the BIC
the presence of both strong and weak changes in mean penalty for PELT) except BreakoutDetection, where we
and/or variance, and for data with and without point found that the default penalty returned no true positives
anomalies. For data with point anomalies, we simulated at all for many scenarios. We therefore used the results
10 i.i.d. N(0, 102) distributed data points occurring at weobtainedwhenderivingtheROCcurvestosetthebeta
randomly sampled locations in the typical data. Robust- parametertoanappropriatelevelforeachcase.
ness to model misspecification was also investigated by The results of this analysis can be found in Table 1.
using t -distributed noise and AR(1)-distributed noise We see that CAPA is generally most accurate. Moreover,
10
with autocorrelation parameter 𝜌 = 0.3. The compari- itsprecisionisnottoostronglyaffectedbythepresenceof
son of these methods is made using the three different pointanomalies,unlikethatofPELT,whoseperformance
approacheswedetailbelow. issignificantlydeterioratedbyanomalies,especiallywhen
thesignalisweak.ThereasonforthisisthatPELTfitsaddi-
tionalchangesinthepresenceofanomalies,whichresults
5.1 Receiveroperatingcharacteristic inshortersegments.Thisleadstolessaccurateparameter
estimates,andconsequentlypoorerestimatesfortheloca-
We obtained receiver operating characteristic (ROC) tionofthechangepoint.CAPAdoesnotfacethisproblem
curves for the four methods. For BreakoutDetection and since the parameter of the typical distribution is shared
PELT, we considered detected changes within 20 time acrossallsegments.
points of true changes to be true positives and classified
all other detected changes as false positives. For lumi-
nol and CAPA, we considered detected starting and end 5.3 Runtime
pointsofepidemicchangestobetruepositivesiftheywere
within20observationsofastartingandendpoints,respec- Finally,weinvestigatedtherelationshipbetweentherun-
tively.Theresultsregardingtheprecisionoftruepositives timeofthefourmethodsandthenumberofobservations.
in Section 5.2 suggest that the results in this section are Our comparison is based on data following a distribu-
robustwithregardtothechoiceoferrortolerance.Weset tion identical to the one we used in Sections 5.1 and 5.2.
theminimumsegmentlengthto10forPELT,CAPA,and SincethistypeofdatafavorsPELTandCAPA,becausethe
BreakoutDetection. To obtain the ROC curves we varied expected number of changes increases with the number
thepenaltyforcollectiveanomalies𝛽inCAPA,thepenalty ofobservations,wealsocomparedtheruntimeofthefour
inPELT,thethresholdinluminol,andthebetaparameter methodsonstationaryN(0,1)data,whichrepresentsthe
ofBreakoutDetection. worstcasescenarioforthesemethods.
TheresultingROCcurves,aswellasexamplesofreal- Figure 2 displays the average speed over 50 repeti-
izations of the data for the scenario of weak and strong tionsforthe2cases.Whencomparingtheslopesbetween
changesinmeancanbefoundinFigure1.Theresultsfor 10,000 and 50,000 datapoints, the slope is very close to
joint changes in mean and variance, as well as changes 2 for BreakoutDetection in both cases as well as CAPA
in variance can be found in the Supporting Information. andPELTforstationarydata,suggestingquadraticscaling.
We see that CAPA generally outperforms PELT, even in In the presence of epidemic changes however, that slope
the absence of point anomalies. This is due to it having is 1.26 for CAPA—1.14 even between 25,000 and 50,000
morestatisticalpower,byexploitingtheepidemicnature datapoints—thussuggestingnearlinearruntime.
of the change. This becomes particularly apparent when
the changes are weak. CAPA also outperform Breakout-
Detectionandluminolforepidemicchangesinmean,the 6 APPLICATIONS
scenarioforwhichthesemethodsweredeveloped.More-
over, the performance of CAPA is barely affected by the WenowturntoapplyingCAPAtoKeplerlightcurvedata
presenceofpointanomalies,unlikethatofthenonrobust and a machine temperature dataset. These two applica-
methods. tions are illustrative of the two main flavors of anomaly
19321872,
2022,
4,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sam.11586
by
Cochrane
Philippines,
Wiley
Online
Library
on
[10/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by the
applicable
Creative
Commons
License

502 FISCHetal.
FIGURE 1 DataexamplesandROCcurvesforchangesinmeanforCAPA(black),PELT(red),BreakoutDetection(green),and
luminol(blue).Thecaptionsforeachplotshowwhetherthedatawassimulatedwithweak,strongorshortcollectiveanomalies,withpoint
anomalies(PAs),orwithcorrelated(AR)orheavy-tailed(T)noise
detection: In the Kepler lightcurve data, anomalies can 6.1 Keplerlightcurvedata
point to the presence of an exoplanet, i.e. a potentially
exciting scientific discovery. This application is therefore CAPA can be applied to the Kepler light curve data to
anexampleofnoveltydetection,similarinspirittoother detectexoplanetsviatheso-calledtransitmethod[37]first
applications such as the detection of copy number varia- proposedbyStruve[41].Thismethodconsistofmeasuring
tions[3]ortheanalysisoffMRIdata[2].Conversely,inthe theluminosityofastaratregularintervals,withtheaimof
machinetemperature,datasetanomaliescanpointtoward detectingsegmentsofreducedluminosity.Theseindicate
a potentially critical problem. It therefore falls under the the transit of a planet [37] past the star, as in an eclipse,
same category as fraud and other fault detection proce- and can naturally be interpreted as collective anomalies:
dures. ashortperiodofreducedluminosityfollowedbyareturn
19321872,
2022,
4,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sam.11586
by
Cochrane
Philippines,
Wiley
Online
Library
on
[10/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 19321872, 2022, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/sam.11586 by Cochrane Philippines, Wiley Online Library on [10/10/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| FISCHetal. |     |     |     |     |     | 503 |
| ---------- | --- | --- | --- | --- | --- | --- |
TABLE 1 PrecisionoftruepositivesmeasuredinmeanabsolutedistanceforCAPA,PELT,luminol,andBreakoutDetection
Breakout
| Mean   | Variance | PAs | CAPA | PELT | Detection | Luminol |
| ------ | -------- | --- | ---- | ---- | --------- | ------- |
| Weak   | —        | —   | 1.79 | 1.50 | 3.40      | 9.91    |
| Weak   | —        | 10  | 1.72 | 2.27 | 3.75      | 10.70   |
| Strong | —        | —   | 0.16 | 0.61 | 5.38      | 15.99   |
| Strong | —        | 10  | 0.19 | 0.67 | 4.68      | 15.60   |
| —      | Weak     | —   | 1.41 | 1.43 | 4.60      | 9.87    |
| —      | Weak     | 10  | 1.31 | 1.89 | 4.49      | 10.76   |
| —      | Strong   | —   | 0.33 | 0.73 | 5.19      | 12.03   |
| —      | Strong   | 10  | 0.33 | 0.79 | 5.17      | 11.29   |
| Weak   | Weak     | —   | 1.16 | 1.30 | 4.00      | 11.40   |
| Weak   | Weak     | 10  | 1.22 | 1.63 | 4.00      | 11.30   |
| Strong | Strong   | —   | 0.09 | 0.56 | 3.78      | 16.31   |
| Strong | Strong   | 10  | 0.09 | 0.58 | 3.77      | 15.71   |
Bestresultsareshowninboldforeachrow.
Abbreviations:CAPA,collectiveandpointanomalies;PAs,pointanomalies.
FIGURE 2 Log–logplotoftheruntimeofCAPA(black),PELT(red),BreakoutDetection(green),andluminol(blue)fortwoscenarios:
(A)withepidemicchangesand(B)stationarydata
tothebaselinelevel.Thelightcurvesaretypicallyprepro- reducesthelatter’sluminositybyonly1%[37].Theability
cessed [32] and both the raw and whitened light curves to automate the analysis of lightcurves would be benefi-
forover40millionstarscanbeaccessedonline.Wehave cial,giventhelargenumberoflightcurvesthathavebeen
includedthewhitenedlightcurveofthestarKepler1132in gatheredandneedanalyzing.
Figure3toillustratethenatureofthistypeofdata.Wenote Sincethereductioninluminositycausedbytransiting
thepresenceofaglobalanomalyonday1550andthenoisy planetsisknowntobeweak,weamplifythesignaltonoise
nature of the data. These make the detection of transits ratiobyexploitingtheperiodicnatureofthetransitsignal.
challenging given the weak signal induced by planetary Iftheperiodofanorbitingplanetwereknown,thesignal
transits. Indeed, even the transit of Jupiter past the sun ofitstransitcouldbestrengthenedbyconsideringalldata

504 FISCHetal.
FIGURE 3 (A)LightcurveofKepler1132,obtainedatapproximately30-minintervals.Missingvaluesareduetoperiodsinwhichthe
starwasnotobserved.Notethepresenceofapointanomalyonday1550—withluminosity—13—andthefactthatnotransitsignatureis
apparenttotheeye.(B)Thisremainstrueafterzoominginona120-daysubsetofthedata,despitetheknownpresenceofKepler1132-b,an
exoplanetorbitingthisstarevery62.9days
points to have been gathered at their measurement time 1132-b, whose radius is about 2.5 times that of the earth
modulothatperiod.Wewouldthusobtainanirregularly [30].Aswithspectralmethods,wealsoobserveresonance
sampledtimeserieswhichwecantransformintoaregu- ofthemainsignalatintegerfractionsofthatperiod.
larlysampledtimeseriesbybinningthedataintoequally Furthermore, recalling that there are currently over
sized bins and taking the average within each bin. We 40 million recorded light curves for different starts, we
could then apply CAPA to this preprocessed data, which require a fast automated procedure. The cost of running
wouldexhibitastrongermeananomalyforanyplanetwith CAPA for one putative orbital period is small relative to
theassociatedperiod.Theresultsobtainedbyapplyingthis thecostofbinningthedataforthatperiod.Analysisofthe
methodtothelightcurveofKepler1132usingaperiodof Kepler1132dataforall20,000orbitalperiodsconsidered
62.8,62.9,and63.0dayscanbefoundinFigure4.Usinga tooklessthan5minonastandardlaptop.
periodof62.9daysresultsinapromisingdip,whichisnot We also applied CAPA to the light curves of further
presentwhenusing62.8or63daysasperiod. stars with confirmed exoplanets and were able to detect
Given a light curve, the periods of exoplanets orbit- their transit signal at the right period. A more detailed
ing the corresponding star, if any are present, are obvi- expositionoftheseresultscanbefoundintheSupporting
ously not known a priori. However, we can use the Information.
approach described in the previous paragraph to test a
range of candidate periods: Since transits appear as peri-
ods of reduced mean, we simply record the stren(gth o)f 6.2 Machinetemperaturedata
thestrongestchangeinmean,asdefinedbymax k △ 𝜇,k
(see Section 4), of any detected collective anomalies for Wenowturntoanalyzingthemachinetemperaturedata
each candidate period, expecting it to be largest for the taken from the Numenta Anomaly Benchmark [1] and
orbitalperiodofexoplanets.Wetriedallperiodsfrom1to included,withpermission,intheanomalypackage.The
200days with increments of 0.01days for the light curve data, displayed in Figure 6A, were obtained from a heat
of Kepler 1132. The result of this analysis can be found sensor on a large industrial machine over the course of
in Figure 5. The largest change in mean is recorded at a approximately 3 months at a 5 min sampling frequency.
periodof62.89days.Thisresultisconsistentwiththeexist- The dataset, consisting of n = 22,695 observations, was
ing literature, which considers Kepler 1132 to be orbited analyzed by an engineer who identified three relevant
approximately every 62.892days by the exoplanet Kepler events:aplannedshutdown,acatastrophicsystemfailure,
19321872,
2022,
4,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sam.11586
by
Cochrane
Philippines,
Wiley
Online
Library
on
[10/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

FISCHetal. 505
FIGURE 4 CAPAappliedwithdefaultpenaltiestothelightcurveofKepler1132preprocessedusingdifferentperiods:(A)62.8days,
(B)62.9daysand(C)63.0days
( )
FIGURE 5 Thestrongestchangeinmean,asmeasuredbymax k △ 𝜇,k ,detectedbyCAPAforthelightcurveofKepler1132.All
periodsfrom1to200daysat0.01-dayincrementwereexamined
as well as a period of anomalous behavior preceding the penalties of CAPA by a factor of (1+𝜌̂)∕(1−𝜌̂). We then
failure whichwas, in hindsight,deemedto have beenan applied CAPA to the data using a maximum segment
earlywarningsign. length m = 1500 to prevent the fitting of long anomalies
Giventhatthereisalargeamountofstructureinthe whicharemerelyaresultofmodelmis-specification.The
data, most notably auto-correlation, we used the mini- resultscanbeseeninFigure6B.Allanomaliesflaggedby
mumcovariancedeterminantcovarianceestimator[35]to theengineerwherecorrectlydetected.Furthermore,only
robustlyestimatedtheAR(1)coefficient.Thisgaveanesti- a single additional collective anomaly was detected. We
mate𝜌̂=0.98and,following[24],weinflatedthedefault refrain from calling it a false positive as it is not possible
19321872,
2022,
4,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sam.11586
by
Cochrane
Philippines,
Wiley
Online
Library
on
[10/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

506 FISCHetal.
FIGURE 6 Machinetemperaturedatawithanonymizedy-axis.(A)Therawdatawithlabeledeventsofinterestlabeledbyreddots.(B)
TheoutputofCAPA,withdetectedcollectiveanomaliesgivenbyblueregions
toknowwhatwouldhavehappenedwithouttheplanned anomaly. In CAPA this threshold is determined by the
shut-down. choiceofpenalties.Whileourtheorygivesdefaultchoices
forthesepenaltiesifthedataisindependent,largerpenal-
ties may be needed if there is temporal correlation—see
7 DISCUSSION our approach in Section 6.2. Where possible we would
recommend tuning penalties on training data where it is
Wehaveintroducedanovelframeworkfordetectingcol- knownthattherearenoanomalies.
lectiveandpointanomaliesinunivariatedata.Itinvolves The CAPA framework can be extended beyond the
specifying a cost for a segment of data in terms of seg- off-lineanomalydetectioninunivariateseriesthatwehave
ment specific parameters, and estimating the parameters considered. Early attempts at this include [11, 43] which
for normal regions of the data. Using this cost, we can extend CAPA to analyzing multivariate data, while [9]
thenquantifyevidencethatasingleobservationisapoint extendsCAPAtoanonlinesetting.
anomaly,orasetofconsecutiveobservationsareacollec-
tiveanomaly,basedonthecostofthesepossibilitiesrela- ACKNOWLEDGMENTS
tive to the cost for the observation or observations being This research has made use of the NASA Exoplanet
fromanormal(baseline)region.TheCAPAalgorithmthen Archive, which is operated by the California Institute
estimates the location of point and collective anomalies of Technology, under contract with the National Aero-
by minimizing a penalized version of this cost over all nautics and Space Administration under the Exoplanet
possible locations of collective and point anomalies. The Exploration Program. The authors would like to thank
frameworkisgeneralinthat,bychoosingappropriatecost the Isaac Newton Institute for Mathematical Sciences
functionsforsegmentsofdata,itcanbeappliedtodiffer- for support and hospitality during the program Statisti-
entdatatypesandtodetectdifferenttypesofanomalies.A calScalabilitywhenworkonthispaperwasundertaken.
keyfeatureofCAPArelativetorelatedanomalydetection TheauthorsacknowledgeBritishTelecommunicationsplc
methodsisitsabilitytojointlyestimatepointandcollective (BT) for financial support and David Yearling and Kjeld
anomalies. Jensen in BT Research & Innovation for helpful discus-
As with any anomaly detection method, care must sions.ThisworkwassupportedbyEPSRCgrantnumbers
be made in terms of choosing thresholds which specify EP/K032208/1(INI),EP/R014604/1(INI),EP/N031938/1
howmuchevidenceisneededtoflagapointorcollective (StatScale),andEP/L015692/1(STOR-i).
19321872,
2022,
4,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sam.11586
by
Cochrane
Philippines,
Wiley
Online
Library
on
[10/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 19321872, 2022, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/sam.11586 by Cochrane Philippines, Wiley Online Library on [10/10/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| FISCHetal.        |     |     |           |     |     |     |     |     |     |     |     | 507 |
| ----------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DATA AVAILABILITY |     |     | STATEMENT |     |     |     |     |     |     |     |     |     |
17. B.Jackson,J.D.Scargle,D.Barnes,S.Arabhi,A.Alt,P.Giou-
Thedatathatsupportthefindingsofthisstudyareopenly mousis,E.Gwin,P.Sangtrakulcharoen,L.Tan,andT.T.Tsai,An
algorithmforoptimalpartitioningofdataonaninterval,IEEE
| available, | includingwithinthe |     | anomaly |     | Rpackageavail- |     |     |     |     |     |     |     |
| ---------- | ------------------ | --- | ------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
able on CRAN (https://CRAN.R-project.org/package= SignalProcess.Lett.12(2005),no.2,105–108.
18. N.A.James,A.Kejariwal,andD.S.Matteson,Leveragingcloud
| anomaly). | Citations | to other | sources | are | provided | in the |                                                |     |     |     |         |     |
| --------- | --------- | -------- | ------- | --- | -------- | ------ | ---------------------------------------------- | --- | --- | --- | ------- | --- |
|           |           |          |         |     |          |        | datatomitigateuserexperiencefrom“breakingbad,” |     |     |     | BigData |     |
manuscriptandtheRpackage.
2016IEEEInt.Conf.,IEEE,2016,pp.3499–3508.
19. X.J.Jeng,T.T.Cai,andH.Li,Simultaneousdiscoveryofrare
ORCID
|               |     |                                       |     |     |     |     | and | common | segment | variants, Biometrika | 100 (2012), | no. 1, |
| ------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | ------ | ------- | -------------------- | ----------- | ------ |
| IdrisA.Eckley |     | https://orcid.org/0000-0001-9957-2460 |     |     |     |     |     |        |         |                      |             |        |
157–172.
| PaulFearnhead |     | https://orcid.org/0000-0002-9386-2341 |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
20. J.JurecˇkováandJ.Picek,RobuststatisticalmethodswithR,CRC
Press,NewYork,2005.
21. R.KillickandI.Eckley,Changepoint:AnRpackageforchange-
REFERENCES
pointanalysis,J.Stat.Softw.58(2014),no.3,1–19.
| 1. S. Ahmad, | A.  | Lavin, S. | Purdy, and | Z.  | Agha, Unsupervised |     |     |     |     |     |     |     |
| ------------ | --- | --------- | ---------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
22. R.Killick,P.Fearnhead,andI.A.Eckley,Optimaldetectionof
real-timeanomalydetectionforstreamingdata,Neurocomputing
changepointswithalinearcomputationalcost,J.Am.Stat.Assoc.
262(2017),134–147.
107(2012),no.500,1590–1598.
2. J.A.AstonandC.Kirch,Evaluatingstationarityviachange-point
|                                         |     |     |     |     |            |         | 23. R. Killick, | K.  | Haynes, | I. A. Eckley, P. Fearnhead, | and | J. Lee, |
| --------------------------------------- | --- | --- | --- | --- | ---------- | ------- | --------------- | --- | ------- | --------------------------- | --- | ------- |
| alternativeswithapplicationstofMRIdata, |     |     |     |     | Ann. Appl. | Stat. 6 |                 |     |         |                             |     |         |
Changepoint:AnRpackageforchangepointanalysis.RPack-
(2012),no.4,1906–1948.
3. L.BardwellandP.Fearnhead,Bayesiandetectionofabnormal ageVersion2.3.2018,availableathttps://CRAN.R-project.org/
package=changepoint
segmentsinmultipletimeseries,BayesianAnal.12(2017),no.1,
|     |     |     |     |     |     |     | 24. M. Lavielle |     | and E. | Moulines, Least-squares | estimation | of an |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------ | ----------------------- | ---------- | ----- |
193–218.
4. M.M.Breunig,H.-P.Kriegel,R.T.Ng,andJ.Sander,LOF:Iden- unknownnumberofshiftsinatimeseries,J.TimeSer.Anal.21
(2000),no.1,33–59.
tifyingdensity-basedlocaloutliers.Proc.2000ACMSIGMODInt.
|     |     |     |     |     |     |     | 25. A. Lavin | and | S. Ahmad, | Evaluating real-time | anomaly | detec- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | -------------------- | ------- | ------ |
Conf.Manage.Data,SIGMOD’00,Assoc.Comput.Mach.,New
York,NY,USA,2000,pp.93–104. tionalgorithms—Thenumentaanomalybenchmark.2015IEEE
|     |     |     |     |     |     |     | 14th | Int. Conf. | Mach. | Learn. Appl. (ICMLA), | IEEE, | 2015, |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | ----- | --------------------- | ----- | ----- |
5. T.Cai,X.JessieJeng,andH.Li,Robustdetectionandidentifi-
pp.38–44.
cationofsparsesegmentsinultrahighdimensionaldataanalysis,
J.R.Stat.Soc.Ser.B74(2012),no.5,773–797. 26. B. Levin and J. Kline, The cusum test of homogeneity with an
applicationinspontaneousabortionepidemiology,Stat.Med.4
6. V.Chandola,A.Banerjee,andV.Kumar,Anomalydetection:A
(1985),no.4,469–488.
survey,ACMComput.Sur.41(2009),no.3,15–58.
7. R. B. Cleveland, W. S. Cleveland, and I. Terpenning, STL: A 27. H. Li, A. Munk, and H. Sieling, FDR-control in multiscale
|                |     |               |           |       |     |                | change-point |     | segmentation, | Electron. J. | Stat. 10 (2016), | no. 1, |
| -------------- | --- | ------------- | --------- | ----- | --- | -------------- | ------------ | --- | ------------- | ------------ | ---------------- | ------ |
| seasonal-trend |     | decomposition | procedure | based | on  | loess, J. Off. |              |     |               |              |                  |        |
918–959.
Stat.6(1990),no.1,3.
8. P.FearnheadandG.Rigaill,Changepointdetectioninthepres- 28. T. F. Ma and C. Y. Yau, A pairwise likelihood-based approach
enceofoutliers,J.Am.Stat.Assoc.114(2019),no.525,169–183. for changepoint detection in multivariate time series models,
Biometrika103(2016),no.2,409–421.
9. Fisch,A.T.M.,L.Bardwell,andI.A.Eckley,Realtimeanomaly
detectionandcategorisation,arXiv.2009.06670. 29. R. Maheshwari, Y. Yang, R. Hou, B. Li, and Z. Liang, Lumi-
10. Fisch,A.T.M.,I.A.Eckley,andP.Fearnhead,2018:Alinear nol:Anomalydetectionandcorrelationlibrary,2014,available
athttps://github.com/linkedin/luminol
timemethodforthedetectionofpointandcollectiveanomalies.
arXiv.1806.01947. 30. T. D. Morton, S. T. Bryson, J. L. Coughlin, J. F. Rowe,
11. Fisch,A.T.M.,I.A.Eckley,andP.Fearnhead,Subsetmultivari- G.Ravichandran,E.A.Petigura,M.R.Haas,andN.M.Batalha,
FalsepositiveprobabilitiesforallKeplerobjectsofinterest:1284
atecollectiveandpointanomalydetection.J.Comput.Graph.Stat
31(2022),no.2,574–585. newlyvalidatedplanetsand428likelyfalsepositives,Astrophys.
12. Fisch,A.T.M.,D.Grose,I.A.Eckley,P.Fearnhead,andL.Bard- J.822(2016),no.2,86.
31. N.MulerandV.J.Yohai,RobustestimatesforGARCHmodels,
| well, 2020: | Anomaly:Detectionofanomalousstructureintime |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
seriesdata.arXiv.2010.09353. J.Stat.Plan.Inf.138(2008),no.10,2918–2940.
13. A. T. M. Fisch, D. J. Grose, I. A. Eckley, and P. Fearnhead, 32. S. E. Thompson, Data Validation Time Series File: Descrip-
tionoftheFileFormatandContent,KeplerScienceDocument
Anomaly:AnRpackagefordetectinganomaliesindata,RPack-
age Version 4.0.0, 2020, available at https://CRAN.R-project. KSCI-19079-001.(2016).
org/package=anomaly 33. M. A. Pimentel, D. A. Clifton, L. Clifton, and L. Tarassenko,
14. P. Fryzlewicz, Wild binary segmentation for multiple change- A review of novelty detection, Signal Process. 99 (2014),
| pointdetection,Ann.Stat.42(2014),no.6,2243–2281. |     |     |     |     |     |     | 215–249. |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
15. S.Guha,N.Mishra,G.Roy,andO.Schrijvers,Robustrandom 34. P. Rousseeuw and V. J. Yohai, Robust regression by means of
cutforestbasedanomalydetectiononstreams,Int.Conf.Mach. S-estimators. In: J. Franke, W. Härdle, and D. Martin (eds).
Learn.,2016,pp.2712–2721. Robustandnonlineartimeseriesanalysis.Lecturenotesinstatis-
16. F.R.Hampel,E.M.Ronchetti,P.J.Rousseeuw,andW.A.Sta- tics,vol.26Springer,NewYork,(1984),256–272.
hel,Robuststatistics—theapproachbasedoninfluencefunctions, 35. P.J.Rousseeuw,Leastmedianofsquaresregression,J.Am.Stat.
| Wiley,NewYork,1986. |     |     |     |     |     |     | Assoc.79(1984),no.388,871–880. |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |

 19321872, 2022, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/sam.11586 by Cochrane Philippines, Wiley Online Library on [10/10/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 508 |     |     |     |     |     |     | FISCHetal. |
| --- | --- | --- | --- | --- | --- | --- | ---------- |
36. P. J. Rousseeuw, Multivariate estimation with high breakdown 44. Y.-C.Yao,Estimatingthenumberofchange-pointsviaSchwarz’
point,Math.Stat.Appl.8(1985),283–297. criterion,Stat.Prob.Lett.6(1988),no.3,181–189.
37. P. Sartoretti and J. Schneider, On the detection of satellites of 45. N. R. Zhang, D. O. Siegmund, H. Ji, and J. Z. Li, Detecting
extrasolarplanetswiththemethodoftransits,Astron.Astrophys. simultaneouschangepointsinmultiplesequences,Biometrika97
| Suppl.Ser.134(1999),no.3,553–560. |     |     |     | (2010),no.3,631–645. |     |     |     |
| --------------------------------- | --- | --- | --- | -------------------- | --- | --- | --- |
38. A.Schwartzman,Y.Gavrilov,andR.J.Adler,Multipletestingof 46. Z. Zhao and C. Y. Yau, Alternating dynamic programming for
|     |     |     |     | multiple epidemic | change-point | estimation, J. | Comput. Graph. |
| --- | --- | --- | --- | ----------------- | ------------ | -------------- | -------------- |
localmaximafordetectionofpeaksin1D,Ann.Stat.39(2011),
| no.6,3290–3319. |     |     |     | Stat.30(2021),808–821. |     |     |     |
| --------------- | --- | --- | --- | ---------------------- | --- | --- | --- |
39. D.Siegmund,B.Yakir,andN.R.Zhang,Detectingsimultaneous
variantintervalsinalignedsequences,Ann.Appl.Stat.5(2011),
|     |     |     |     | SUPPORTING | INFORMATION |     |     |
| --- | --- | --- | --- | ---------- | ----------- | --- | --- |
no.2A,645–668. Additional supporting information may be found online
| 40. P. Smyth, | Markov monitoring | with unknown | states, IEEE |                   |             |            |                 |
| ------------- | ----------------- | ------------ | ------------ | ----------------- | ----------- | ---------- | --------------- |
|               |                   |              |              | in the Supporting | Information | section at | the end of this |
J.Select.AreasCommun.12(1994),no.9,1600–1612.
article.
41. O.Struve,Proposalforaprojectofhigh-precisionstellarradial
velocitywork,Observatory72(1952),199–200.
| 42. P. D. | Talagala, R. J. Hyndman, | K. Smith-Miles, | S. Kan- |     |     |     |     |
| --------- | ------------------------ | --------------- | ------- | --- | --- | --- | --- |
Howtocitethisarticle:A.T.M.Fisch,I.
danaarachchi,andM.A.Muñoz,Anomalydetectioninstreaming
A.Eckley,andP.Fearnhead,Alineartimemethod
nonstationarytemporaldata,J.Comput.Graph.Stat.29(2020),
forthedetectionofcollectiveandpointanomalies,
13–27.
43. Tveten,M.,I.A.Eckley,andP.Fearnhead,2021:Scalablechange- Stat.Anal.DataMin.:ASADataSci.J.15(2022),
494–508.https://doi.org/10.1002/sam.11586
| point and | anomaly detection | in cross-correlated | data with an |     |     |     |     |
| --------- | ----------------- | ------------------- | ------------ | --- | --- | --- | --- |
applicationtoconditionmonitoring.arXiv.2010.06937.