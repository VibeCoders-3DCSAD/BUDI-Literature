---
conversion_metadata:
  converted_at: "2026-10-12T07:26:05Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Hu et al., 2023.pdf"
  source_pdf_sha256: "7f64317b7eb44c629665a64a1b6e4aac8a37bd233eebfe555e3ebc4767973a57"
  page_count: 26
  markdown_char_count: 112522
---

| Two-Stage |     | Predict+Optimize |         |     |            | for Mixed | Integer |             | Linear |
| --------- | --- | ---------------- | ------- | --- | ---------- | --------- | ------- | ----------- | ------ |
| Programs  |     | with             | Unknown |     | Parameters |           | in      | Constraints |        |
XinyiHu1,JasperC.H.Lee2,JimmyH.M.Lee1
1DepartmentofComputerScienceandEngineering
TheChineseUniversityofHongKong,Shatin,N.T.,HongKong
2DepartmentofComputerSciences&InstituteforFoundationsofDataScience
UniversityofWisconsin–Madison,WI,USA
{xyhu,jlee}@cse.cuhk.edu.hk,jasper.lee@wisc.edu
Abstract
Considerthesettingofconstrainedoptimization,withsomeparametersunknown
|     | atsolvingtimeandrequiringpredictionfromrelevantfeatures. |           |     |            |          |            | Predict+Optimize |        |     |
| --- | -------------------------------------------------------- | --------- | --- | ---------- | -------- | ---------- | ---------------- | ------ | --- |
|     | is a recent                                              | framework | for | end-to-end | training | supervised | learning         | models | for |
suchpredictions,incorporatinginformationabouttheoptimizationprobleminthe
trainingprocessinordertoyieldbetterpredictionsintermsofthequalityofthe
|     | predictedsolutionunderthetrueparameters. |     |     |     |     | Almostallpriorworkshavefocused |     |     |     |
| --- | ---------------------------------------- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- |
onthespecialcasewheretheunknownsappearonlyintheoptimizationobjective
|     | andnottheconstraints.                   |           | Huetal.proposedthefirstadaptationofPredict+Optimize |          |            |                            |      |              |     |
| --- | --------------------------------------- | --------- | --------------------------------------------------- | -------- | ---------- | -------------------------- | ---- | ------------ | --- |
|     | tohandleunknownsappearinginconstraints, |           |                                                     |          |            | buttheframeworkhassomewhat |      |              |     |
|     | ad-hoc                                  | elements, | and they                                            | provided | a training | algorithm                  | only | for covering | and |
|     | packinglinearprograms.                  |           | Inthiswork,wegiveanewsimplerandmorepowerful         |          |            |                            |      |              |     |
frameworkcalledTwo-StagePredict+Optimize,whichwebelieveshouldbethe
|     | canonical     | framework | for the           | Predict+Optimize |        | setting.  | We also     | give a       | training |
| --- | ------------- | --------- | ----------------- | ---------------- | ------ | --------- | ----------- | ------------ | -------- |
|     | algorithm     | usable    | for all mixed     | integer          | linear | programs, | vastly      | generalizing | the      |
|     | applicability |           | of the framework. | Experimental     |        | results   | demonstrate | the          | superior |
predictionperformanceofourtrainingframeworkoverallclassicalandstate-of-
the-artmethods.
1 Introduction
Optimization problems are prevalent in modern society, and yet the problem parameters are not
alwaysavailableatthetimeofsolving. Forexample,considerthereal-worldapplicationscenario
ofstockingastore:asstoremanagers,weneedtoplacemonthlyordersforproductstostockinthe
store. Wewanttostockproductsthatsellfastandyieldhighprofits,asmuchofthemaspossible,
subjecttothehardconstraintoflimitedstoragespace. However,ordersneedtobeplacedtwoweeks
inadvanceofthemonthlydelivery,andthecustomerdemandnextmonthcannotbeknownexactly
atthetimeoforderplacement. Inthispaper, weconsiderthesupervisedlearningsetting, where
theunknownparameterscanbepredictedfromrelevantfeatures,andtherearesufficienthistorical
(features, parameters) pairs as training data for a prediction model. The goal, then, is to learn a
predictionmodelfromthetrainingdatasuchthat,ifweplugintheestimatedparametersintothe
optimizationproblemandsolveforanestimatedsolution, theestimatedsolutionremainsagood
solutionevenafterthetrueparametersarerevealed.
Theclassicapproachtotheproblemwouldbetotrainasimpleregressionmodel,basedonstandard
lossessuchas(regularized)ℓ loss,topredictparametersfromthefeatures. Itisshown,however,that
2
havingasmallpredictionerrorintheparameterspacedoesnotnecessarilymeanthattheestimated
solutionperformswellunderthetrueparameters. TherecentframeworkofPredict+Optimize,by
37thConferenceonNeuralInformationProcessingSystems(NeurIPS2023).

Elmachtoub and Grigas [7], instead proposes the more effective regret loss for training, which
compares the solution qualities of the true optimal solution and the estimated solution under the
trueparameters. Subsequentworks[6,8,10,13,17,19,27]havesinceappearedintheliterature,
applyingtheframeworktomoreandwiderclassesofoptimizationproblemsaswellasfocusingon
speed-vs-predictionaccuracytradeoffs.
However,allthesepriorworksfocusonlyonthecasewheretheunknownparametersappearinthe
optimizationobjective, andnotintheconstraints. Thetechnicalchallengeforthegeneralization
is immediate: if there were unknown parameters in the constraints, the estimated solution might
not even be feasible under the true parameters revealed afterwards! Thus, in order to tackle the
Predict+Optimizesettingwithunknownsinconstraints,therecentworkofHuetal.[12]presents
the first such adaptation on the framework: they view the estimated solution as representing a
softcommitment. Oncethetrueparametersarerevealed,correctiveactioncanbetakentoensure
feasibility,potentiallyatapenaltycorrespondingtothereal-lifecostof(partially)renegingonasoft
commitment. Theirframeworkcapturesapplicationscenarioswheneversuchcorrectionispossible,
andrequiresthepractitionertospecifyboththecorrectionmechanismandthepenaltyfunction.These
datacanbedeterminedandderivedfromthespecificapplicationscenario. Asanexample,inthe
product-stockingproblem,anadditionalunknownparameteristhestoragespace,becauseitdepends
onhowthecurrentproductsinthestoresellbeforetheneworderarrives. Weneedtoplaceorders
twoweeksaheadbasedonpredictedstoragespace. Thenightbeforetheorderarrives, weknow
thepreciseavailablespace,meaningthattheunknownparameterisrevealed. Apossiblecorrection
mechanismthenistothrowawayexcessproductsthatthestorecannotkeep,whileincurringthe
penaltythatistheretailpriceoftheproducts,aswellasdisposalfees.
WhiletheHuetal.[12]frameworkdoescapturemanyapplicationscenarios,thereareimportant
shortcomings. In their framework, they require the practitioner to specify a correction function
thatamendsaninfeasiblesolutionintoafeasiblesolution. However,thederivationofacorrection
functioncanberatherad-hocinnature. Inparticular,givenaninfeasibleestimatedsolution,there
maybemanywaystotransformthesolutionintoafeasibleone,andyettheirframeworkrequires
thepractitionertopickoneparticularway. Thisleadstotheseconddownside:itisdifficulttogivea
generalalgorithmicframeworkthatappliestoawidevarietyofoptimizationproblems. Huetal.had
torestricttheirattentiononlytopackingandcoveringlinearprograms,forwhichtheycouldpropose
agenericcorrectionfunction. Inthiswork,weaimtovastlygeneralizethekindsofoptimization
problems that Predict+Optimize can tackle under uncertainty in the constraints. In addition, the
approachofHuetal.failstohandletheinterestingsituationinwhichpost-hoccorrectionisstill
desirablewhentheestimatedsolutionisfeasiblebutnotgoodunderthetrueparameters.
Ourcontributionsarethree-fold:
•Tomitigatetheshortcomingsofthepriorwork,weproposeandadvocateanewframework,which
wecallTwo-StagePredict+Optimize1,thatisbothconceptuallysimplerandmoreexpressiveinterms
oftheclassofoptimizationproblemsitcantackle. Thekeyideaforthenewframeworkisthatthe
correctionfunctionisunnecessary. Allthatisrequiredisapenaltyfunctionthatcapturesthecostof
modifyingonesolutiontoanother. Apenaltyfunctionissufficientfordefiningacorrectionprocess:
weformulatethecorrectionprocessitselfasa“Stage2”optimizationproblem,takingtheoriginally
estimatedsolutionaswellasthepenaltyfunctionintoaccount.
•Underthisframework,wefurtherproposeageneralend-to-endtrainingalgorithmthatappliesnot
onlytopackingandcoveringlinearprograms,butalsotoallmixedintegerlinearprograms(MILPs).
WeadapttheapproachofMandiandGuns[18]togiveagradientmethodfortrainingneuralnetworks
topredictparametersfromfeatures.
•Weapplytheproposedmethodtothreebenchmarkstodemonstratethesuperiorempiricalperfor-
manceoverclassicalandstate-of-the-arttrainingmethods.
2 Background
Inthissection,wegivebasicdefinitionsforoptimizationproblemsandthePredict+Optimizesetting
[7],anddescribethestate-of-the-artframework[12]forPredict+Optimizewithunknownparameters
1Theliteraturesometimesuses“two-stage"tomeanapproacheswherethepredictionisagnostictothe
optimizationproblem.Here,“two-stage"referstothesoftcommitmentandthecorrection.
2

inconstraints.Thetheoryisstatedintermsofminimizationbutappliesofcoursealsotomaximization,
uponappropriatenegation.Withoutlossofgenerality,anoptimizationproblem(OP)P canbedefined
asfinding:
x∗ =argminobj(x) s.t. C(x)
x
wherex ∈ Rd isavectorofdecisionvariables, obj : Rd → Risafunctionmappingxtoareal
objectivevaluethatistobeminimized,andC isasetofconstraintsthatmustbesatisfiedoverx. We
callx∗anoptimalsolutionandobj(x∗)theoptimalvalue. Aparameterizedoptimizationproblem
(Para-OP)P(θ)isanextensionofanOPP:
x∗(θ)=argminobj(x,θ) s.t. C(x,θ)
x
whereθ ∈ Rt isavectorofparameters. Theobjectiveobj(x,θ)andconstraintsC(x,θ)canboth
dependonθ. Whentheparametersareknown,aPara-OPisjustanOP.
In the Predict+Optimize setting [7], the true parameters θ ∈ Rt for a Para-OP are not known at
solvingtime,andestimatedparametersθˆareusedinstead. Supposeeachparameterisestimatedby
mfeatures. Theestimationwillrelyonamachinelearningmodeltrainedovernobservationsofa
trainingdataset{(A1,θ1),...,(An,θn)}whereAi ∈Rt×m isafeaturematrixforθi,inorderto
yieldapredictionfunctionf :Rt×m →Rtpredictingparametersθˆ=f(A).
SolvingthePara-OPusingtheestimatedparameters,weobtainanestimatedsolutionx∗(θˆ). When
theunknownparametersappearinconstraints,onemajorchallengeisthatthefeasibleregionisonly
approximatedatsolvingtime, andhencetheestimatedsolutionmaybeinfeasibleunderthetrue
parameters. Fortunately,incertainapplications,theestimatedsolutionisnotahardcommitment,but
onlyrepresentsasoftcommitmentthatcanbemodifiedoncethetrueparametersarerevealed. Huet
al.[12]proposeaPredict+Optimizeframeworkforsuchapplications. Theframeworkisasfollows:
i)theunknownparametersareestimatedasθˆ,andanestimatedsolutionx∗(θˆ)issolvedusingthe
estimatedparameters,ii)thetrueparametersθarerevealed,andifx∗(θˆ)isinfeasibleunderθ,itis
amendedintoacorrectedsolutionx∗ (θˆ,θ)whilepotentiallyincurringsomepenalty,andfinally
corr
iii)thesolutionx∗ (θˆ,θ)isevaluatedaccordingtothesumofboththeobjective,underthetrue
corr
parametersθ,andtheincurredpenaltyfromcorrection.
Moreformally,acorrectionfunctiontakesanestimatedsolutionx∗(θˆ)andtrueparametersθand
returnsacorrectedsolutionx∗ (θˆ,θ)thatisfeasibleunderθ. ApenaltyfunctionPen(x∗(θˆ) →
corr
x∗ (θˆ,θ))takesanestimatedsolutionx∗(θˆ)andthecorrectedsolutionx∗ (θˆ,θ)andreturnsanon-
corr corr
negativepenalty. Boththecorrectionfunctionandthepenaltyfunctionshouldbechosenaccordingto
thepreciseapplicationscenarioathand. Thefinalcorrectedsolutionx∗ (θˆ,θ)isevaluatedusing
corr
thepost-hocregret,whichisdefinedwithrespecttothecorrectedsolutionx∗ (θˆ,θ)andthepenalty
corr
functionPen(x∗(θˆ)→x∗ (θˆ,θ)). Thepost-hocregretisthesumoftwoterms:(a)thedifference
corr
inobjectivebetweenthetrueoptimalsolutionx∗(θ)andthecorrectedsolutionx∗ (θˆ,θ)underthe
corr
trueparametersθ,and(b)thepenaltythatthecorrectionprocessincurs. Mathematically,thepost-hoc
regretfunctionPReg(θˆ,θ): Rt×Rt →R (forminimizationproblems)is:
≥0
PReg(θˆ,θ)= obj(x∗ (θˆ,θ),θ)−obj(x∗(θ),θ) + Pen(x∗(θˆ)→x∗ (θˆ,θ)) (1)
corr corr
whereobj(x∗ (θˆ,θ),θ)isthecorrectedoptimalvalueandobj(x∗(θ),θ)isthetrueoptimalvalue.
corr
Giventhepost-hocregretasalossfunction,theempiricalriskminimizationprincipledictatesthatwe
choosethepredictionfunctiontobethefunctionf fromthesetofmodelsF attainingthesmallest
averagepost-hocregretoverthetrainingdata:
n
1 (cid:88)
f∗ =argmin PReg(f(Ai),θi) (2)
n
f∈F
i=1
3 Two-stagePredict+OptimizeFramework
While the prior work by Hu et al. [12] is the first Predict+Optimize framework for unknowns in
constraints,andisindeedapplicabletoagoodrangeofapplications,ithasseveralshortcomings.
3

First,theframeworkrequiresmathematicallyformalizingbothapenaltyfunctionandacorrection
functionfromtheapplicationscenario,andessentiallyimposesdifferentiabilityassumptionsonthe
correctionfunctionfortheframeworktobeusable. Thead-hocnatureofwritingdownacorrection
functionlimitsthepracticalapplicabilityoftheframework. Second,asaresultofneedingasingle
(differentiable)correctionfunction,Huetal.[12]neededtorestricttheirattentiontoonlypacking
andcoveringlinearprograms,inordertoderiveageneralcorrectionfunctionthatisapplicabletoall
theinstances. Thisalsosignificantlylimitstheimmediateapplicabilityoftheirframework. Third,
theirframeworkonlycorrectsanestimatedsolutionwhenitisinfeasibleunderthetrueparameters.
Yet, thereareapplicationswherecorrectionsarepossibleevenwhentheestimatedsolutionwere
feasible,butjustnotverygoodunderthetrueparameters.
Inthispaper,weadvocateusingasimpleryetmorepowerfulframework,whichwecallTwo-Stage
Predict+Optimize,addressingalloftheaboveshortcomings. Thesimplifiedperspectivewillallowus
todiscussmoreeasilyhowtohandletheentireclassofmixedintegerlinearprograms(MILPs)instead
ofbeingrestrictedtojustpackingandcoveringlinearprograms.SinceMILPsincludealloptimization
problemsinNP(underareasonabledefinitionofNPforoptimizationproblems),ourframework
is significantly more applicable in practice. We will describe the Two-Stage Predict+Optimize
frameworkbelow,anddiscussitsapplicationtoMILPsinthenextsection.
Ourframeworkissimple:weforgotheideaofacorrectionfunctionandtreatcorrectionitselfas
an optimization problem, based on the penalty function, the estimated solution and the revealed
trueparameters. RecalltheHuetal.viewofPredict+Optimizeunderuncertaintiesinconstraints:
theestimatedsolutionisaformofsoftcommitment,whichcanbemodifiedatacostoncethetrue
parameters are revealed. The penalty function describes the cost of changing from an estimated
solution to a final solution. The main observation is that, given an estimated solution and the
revealedparameters,weshouldinfactsolveanewoptimizationproblem,formedbyapplyingthetrue
parameterstotheoriginaloptimization,andaddingthepenaltyfunctiontotheobjective. Thefinal
solutionfromthisnewoptimizationthustakesthepenaltyofcorrectionintoaccount. Thisapproach
yieldsthreeimmediateadvantages. First,thepractitionernolongerneedstospecifyacorrection
function, thus reducing the ad-hoc nature of the framework. Second, even feasible solutions are
allowedtobemodifiedafterthetrueparametersarerevealedifthepenaltyofdoingsoisnotinfinity.
Third,conditionedonthesamepenaltyfunction,thesolutionqualityfromourtwo-stageoptimization
approachisalwaysatleastasgoodasthatfromusinganycorrectionfunction. Thelastadvantageis
presentedasPropositionA.1.
NowweformallydefinetheTwo-StagePredict+Optimizeframework.
I.InStage1,theunknownparametersareestimatedasθˆfromfeatures. Thepractitionerthensolves
theStage1optimization,whichisthePara-OPusingtheestimatedparameters,toobtaintheStage1
solutionx∗. TheStage1solutionshouldbeinterpretedassomeformofsoftcommitment,thatwe
1
gettomodifyinStage2atextracost/penalty. AssumingthenotationofthePara-OPinSection2,the
Stage1OPcanbeformulatedas:
x∗ =argmin obj(x,θˆ) s.t. C(x,θˆ)
1
x
II.AtthebeginningofStage2,thetrueparametersθarerevealed. TheStage2optimizationproblem
augmentstheoriginalStage1problembyaddingapenaltytermPen(x∗ →x∗,θ)totheobjective,
1 2
which accounts for the penalty (modelled from the application scenario) for changing from the
softly-committedStage1solutionx∗tothenewStage2andfinalsolutionx∗. TheStage2OPcan
1 2
thenbeformulatedas:
x∗ =argmin obj(x,θ)+Pen(x∗ →x,θ) s.t. C(x,θ)
2 1
x
SolvingtheStage2problemyieldsthefinalStage2“corrected”solutionx∗.
2
III.TheStage2solutionx∗isevaluatedaccordingtotheanalogouspost-hocregret,asfollows:
2
PReg(θˆ,θ)= obj(x∗,θ)+Pen(x∗ →x∗,θ)−obj(x∗(θ),θ)
2 1 2
whereagain,x∗(θ)isanoptimalsolutionofthePara-OPunderthetrueparametersθ. Notethatthe
post-hocregretdependsonallofa)thepredictedparameters,b)theinducedStage1solution,c)the
trueparametersandd)thefinalStage2solution.
Toseethisnewframeworkappliesinpractice,thefollowingexampleexpandsontheproduct-stocking
problemintheintroduction.
4

Example1. Considertheproduct-stockingproblemagain,whereregularordershavetobeplaced
twoweeksaheadofmonthlydeliveries. Sincetheavailablespaceatthetimeofdeliveryisunknown
whenweplacetheregularorders,dependingonthesalesoverthenexttwoweeks,weneedtomake
apredictionontheavailablespacetomakeacorrespondingorder. Welearnthepredictorusing
historicalsalesrecordsfromfeaturessuchastime-of-yearandprice. Then,weusethepredicted
availablespacetooptimizefortheregularorderweplace. ThisistheStage1solution.
Thenightbeforetheorderarrives,theunknownconstraintparameter,i.e.thepreciseavailablespace,
isrevealed. Wecanthencheckifwehaveover-orderedorunder-ordered. Inthecaseofover-ordering,
we would have to call and ask the wholesale company to drop some items from the order. The
companywouldperhapsallowtakingtheitemsoffthefinalbill,butnaturallytheyhaveasurcharge
forlast-minutechanges. Similarly,ifweunder-ordered,wemightrequestthewholesalecompanyto
sendusmoreproducts,againnaturallywithasurchargeforlast-minuteordering. Theupdatedorder
istheStage2decision. Theincurredwholesalersurchargesinducethepenaltyfunction.
Areaderwhoisfamiliarwiththeliteratureontwo-stageoptimizationproblemsmaynotethatthe
aboveframeworkisphrasedslightlydifferentlyfromsomeothertwo-stageproblemformulations. In
particular,sometwo-stageframeworksphraseStage1solutionsashardcommitments,andinclude
recoursevariablesinbothstagesofoptimizationtomodelwhatchangesaremadeinStage2. We
showinAppendixA.1howourframeworkcancapturethisotherperspective,andingeneraldiscuss
howproblemmodellingcanbedoneinournewframework.
Thereadermayalsowonder:whataboutapplicationscenarioswherethe(Stage1)estimatedsolution
isahardcommitment,andthereisabsolutelynocorrection/recourseavailable? InAppendixA.2,we
discusshowourframeworkisstillusefulandapplicableforlearninginthesesituations.
We also give a more detailed comparison, in Appendix A.3, between our new Two-Stage Pre-
dict+OptimizeframeworkandthepriorHuetal.framework. Technically,ifweignored differen-
tiabilityissues,thetwoframeworksaremathematicallyequivalentinexpressiveness. However,we
stressthatournewframeworkisbothconceptuallysimplerandeasiertoapplytoafarwiderclass
ofoptimizationproblems. Weshowconcretelyinthenextsectionhowtoend-to-endtrainaneural
network for this framework for all MILPs, vastly generalizing the method of Hu et al. which is
restrictedtopackingandcovering(non-integer)linearprograms. Inaddition,AppendixA.3also
statesandprovesPropositionA.1,thatifwefixanoptimizationproblem,apredictionmodelanda
penaltyfunction,thenthesolutionqualityfromourtwo-stageapproachisalwaysatleastasgoodas
usingthecorrectionfunctionapproach.
4 Two-StagePredict+OptimizeonMILPs
Inthissection,wedescribehowtogiveanend-to-endtrainingmethodforneuralnetworkstopredict
unknownparametersfromfeatures,undertheTwo-StagePredict+Optimizeframework.Thefollowing
algorithmicmethodisapplicablewheneverbothstagesofoptimizationareexpressibleasMILPs.
Duetothepagelimit,thediscussioninthissectionishigh-levelandbrief,withallthecalculation
detailsdeferredtoAppendixB.
Thestandardwaytotrainaneuralnetworkistouseagradient-basedmethod. IntheTwo-Stage
Predict+Optimizeframework,weusethepost-hocregretPRegasthelossfunction. Therefore,for
eachedgeweightw intheneuralnetwork,weneedtocomputethederivative dPReg. Usingthelaw
e dwe
oftotalderivative,weget
(cid:12) (cid:12)
dPReg(θˆ,θ) ∂PReg(θˆ,θ)(cid:12) ∂x∗∂x∗ ∂θˆ ∂PReg(θˆ,θ)(cid:12) ∂x∗ ∂θˆ
= (cid:12) 2 1 + (cid:12) 1 (3)
dw
e
∂x∗
2
(cid:12)
(cid:12) x∗
∂x∗
1
∂θˆ ∂w
e
∂x∗
1
(cid:12)
(cid:12) x∗
∂θˆ ∂w
e
1 2
Assuch,wewishtocalculateeachtermontherighthandside.
The easiest term to handle is ∂θˆ , since θˆis the neural network output, and so the derivatives
∂we
(cid:12)
canbedirectlycalculatedbystandardbackpropagation[25]. Asfortheterms
∂PReg(θˆ,θ)(cid:12)
and
∂x∗
2
(cid:12)
x∗
(cid:12) 1
∂PReg(θˆ,θ)(cid:12)
, they are easily calculable whenever both the optimization objective and penalty
∂x∗
1
(cid:12)
x∗
2
functionaresmooth,andinfactlinearasinthecaseofMILPs. Whatremainsaretheterms
∂x∗
2 and
∂x∗
1
5

∂x∗ 1. Thechallengeisthatx∗ isthesolutionofaMILPoptimization(Stage2)thatusesx∗ asits
∂θˆ 2 1
parameters,i.e.,differentiatethroughaMILP.Similarly,x∗dependsonθˆthroughaMILP(Stage1).
1
SinceMILPoptimamaynotchangeunderminorparameterperturbations,thegradientscanbeeither
0ornon-existent,whichareuninformative. Wethusneedtocomputesomeapproximationinorderto
getusefultrainingsignals.
Our approach, inspired by the work of Mandi and Guns [18], is to define a new surrogate loss
(cid:94)
function PReg that is differentiable and produces informative gradients. Prior works related to
learningunknownsinconstraints[1,2,27]givewaysofdifferentiatingthroughLPsorLPswith
regularizations. Theseworkscanbeusedinplaceoftheproposedapproach. However,experiments
inAppendixEdemonstratethattheproposedapproachperformsatleastaswellinpost-hocregret
performanceastheothers,whilebeingfaster. Weshowtheconstructionoftheproposedapproach
below,andnotethatitdoesnothaveasimpleclosedform. Nonetheless,wecancomputeitsgradients.
TherestofthesectionassumesthatbothstagesofoptimizationareexpressibleasaMILPinthe
followingstandardform:
x∗ =argminc⊤x s.t. Ax=b,Gx≥h,x≥0,x ∈Z (4)
S
x
withdecisionvariablesx ∈ Rd andproblemparametersc ∈ Rd,A ∈ Rp×d,b ∈ Rp,G ∈ Rq×d,
h ∈ Rq. ThesubsetofindicesS denotesthesetofvariablesthatareunderintegralityconstraints.
Sincetheunknownparametersmayappearinanycombinationofc,A,b,GandhintheStage1
optimization for x∗, the surrogate loss function construction needs computable and informative
1
gradientsforallof
∂x∗
,
∂x∗
,
∂x∗
,
∂x∗
and
∂x∗
.
∂c ∂A ∂b ∂G ∂h
Wefollowtheinterior-pointbasedapproachofMandiandGuns[18],usedalsobyHuetal.[12].
Considerthefollowingconvexrelaxationof(4),forafixedvalueofµ≥0:
d q
(cid:88) (cid:88)
x∗ =argminc⊤x−µ ln(x )−µ ln(s )s.t. Ax=b,Gx−s=h (5)
i i
x,s
i=1 i=1
Thisisarelaxationof(4)byi)droppingallintegralityconstraints,ii)introducingslackvariables
s ≥ 0toturnGx ≥ hintoGx−s = handiii)replacingboththex ≥ 0ands ≥ 0constraints
withthelogarithmbarriertermsintheobjective,withmultiplierµ≥0. Theobservationisthatthe
gradients ∂x, ∂x, ∂x, ∂x and ∂x for(5)areallwell-defined,computableandinformativeforafixed
∂c ∂A ∂b ∂G ∂h
valueofµ≥0: Slater’sconditionholdsfor(5),andsotheKKTconditionsmustbesatisfiedatthe
optimum(x∗,s∗)of(5). WecanthuscomputealltherelevantgradientsviadifferentiatingtheKKT
conditions,usingtheimplicitfunctiontheorem. WegiveallthecalculationdetailsinAppendixB.
Giventheaboveobservation,wethenaimtoconstructthesurrogatelossfunctionbyreplacingthex∗
1
andx∗,whicharesupposedtosolvedusingMILP(4),witha)x thatissolvedfromprogram(5)
2 (cid:101)1
relaxationoftheStage1optimizationproblem,usingthepredictedparametersθˆandb)x thatis
(cid:101)2
solvedfromtheprogram(5)relaxedversionofStage2optimization,usingx andthetrueparameters
(cid:101)1
θ. Theonlyremainingquestionthen,is,whichvaluesofµdoweuseforthetworelaxedproblems?
GivenaMILPintheformof(4),theinterior-pointbasedsolverofMandiandGuns[18]generates
andsolves(5)forasequenceofdecreasingnon-negativeµ,withaterminationconditionthatµcannot
besmallerthansomecutoffvalue. Thus, wesimplychoosethecutoffvaluetouseas“µ”in(5),
(cid:94)
whichthencompletesthedefinitionofthesurrogatelossPReg.
(cid:94)
Algorithmically,wetraintheneuralnetworkonthesurrogatelossPRegasfollows: givenpredicted
parameters,weruntheMandiandGunssolvertogettheoptimalsolution(x∗,s∗)forthefinalvalue
ofµ. Wecanthencomputethegradientoftheoutputsolutionwithrespecttoanyoftheproblem
parametersusingthecalculationsinAppendixB,combinedwithbackpropagation,toyield
dP(cid:94)Reg
dwe
accordingtoEquation(3).
InAppendixC,wegivethreeexampleapplicationscenarios,alongwiththeirpenaltyfunctions,that
ourtrainingapproachcanhandle. Theseproblemsare:a)analloyproductionproblem,forfactory
tryingtosourceoresunderuncertaintyinchemicalcompositionsintherawmaterials,b)avariantof
theclassic0-1knapsackwithunknownweightsandrewards,andc)anurserosterschedulingproblem
with unknown patient load. We show explicitly in Appendix C how both stages of optimization
6

Table1: Relevantproblemsizesofthethreebenchmarks.
Problemname Brassalloyproduction Titanium-alloyproduction 0-1knapsack Nurseschedulingproblem
Dimensionofx 10 10 10 315
Numberofconstraints 12 14 21 846
Numberofunknownparameters 20 40 10 21
Numberoffeatures(perparameter) 4096 4096 4096 8
canbeformulatedasMILPsfortheseapplications,andapplytheAppendixBcalculationstoyield
(cid:94)
gradientcomputationformulasforthesurrogatelossPRegfortheseproblems.
A limitation of our approach is the requirement that both stages must be expressible as MILPs,
constrainingtheoptimizationobjectivestobelinearintheMILPdecisionvariables. Thiscontrasts
theHuetal.framework[12]whichhandlesnon-linearpenalties. WepointoutthatevenMILPscan
handlesomenon-linearitybyusingextradecisionvariables:forexample,theabsolute-valuefunction.
Moreover, the Appendix B gradient calculations can be adapted to handle general differentiable
non-linear objectives. We present only MILPs as a main overarching application for this paper
becauseoftheirwidespreaduseindiscreteoptimization,withreadilyavailablesolvers.
5 ExperimentalEvaluation
Weevaluatetheproposedmethod2onthreebenchmarksdescribedinSection4andAppendixC.Table
1reportstherelevantbenchmarkproblemsizes. Wecompareourmethod(2S)withthestateoftheart
Predict+Optimizemethod,IntOpt-C[12],and5classicalregressionmethods[9]:ridgeregression
(Ridge),k-nearestneighbors(k-NN),classificationandregressiontree(CART),randomforest(RF),
andneuralnetwork(NN).Allofthesemethodsusetheirclassiclossfunctiontotraintheprediction
models. Attesttime,toensurethefeasibilityofthesolutionswhencomputingthepost-hocregret,
weperformStage2optimizationontheestimatedsolutionsfortheseclassicalregressionmethods
beforeevaluatingthefinalsolution. Additionally,CombOptNet[23]isadifferentmethodfocusing
onlearningunknownsinconstraints,butwithadifferentgoalandlossfunction. Weexperimentally
compareourproposedmethodwithCombOptNetonthe0-1knapsackbenchmark—theonlywith
availableCombOptNetcode. WealsopresentaqualitativecomparisoninSection6.
Inthefollowingexperiments,wewillneedtotakecaretodistinguishtwo-stageoptimizationasa
trainingtechnique(Section4)andasanevaluationframework(Section3).Wewilldenoteourtraining
methodas“2S”intheexperiments,andwhenwesay“Two-StagePredict+Optimize”framework,
wealwaysmeanitasanevaluationframework. 2SisalwaysevaluatedaccordingtotheTwo-Stage
Predict+Optimizeframework. Asexplainedabove,wewillalsoevaluatealltheclassicaltraining
methodsusingtheTwo-StagePredict+Optimizeframework. Forourcomparisonwiththepriorwork
ofHuetal.[12],wewillalsodistinguishtheirtrainingmethodandevaluationframework. Thename
“IntOpt-C”alwaysreferstotheirtrainingmethodusingtheircorrectionfunction. Wewillsimply
calltheirevaluationframeworkthe“Huetal.framework”orwithsimilarphrasing(seeSection2to
recalldetails). IntOpt-CwillsometimesbeevaluatedusingournewTwo-StagePredict+Optimize
framework,andsometimesthepriorframeworkofHuetal.[12]usingtheircorrectionfunction.
Themethodsofk-NN,RF,NN,andIntOpt-Caswellas2Shavehyperparameters,whichwetunevia
cross-validation. WeincludethehyperparametertypesandchosenvaluesinAppendixD.Inthemain
paperweonlyreportthepredictionperformances. SeeAppendixHforruntimecomparisons.
AlloyProductionProblem ThealloyproductionproblemisacoveringLP,seeAppendixC.1for
thepracticalmotivationandLPmodel. SinceHuetal.[12]alsoexperimentedonthisproblem,we
useittocompareour2SmethodwithIntOpt-C[12],usingthesamedatasetandexperimentalsetting.
Weconductexperimentsontheproductionoftworealalloys:brassandanalloyblendforstrength-
eningTitanium. Forbrass,2kindsofmetalmaterials,CuandZn,arerequired[14]. Theblendof
thetwomaterialsare,proportionally,req =[627.54,369.72]. Forthetitanium-strengtheningalloy,
4kindsofmetalmaterials,C,Al,V,andFe,arerequired[15]. Theblendofthefourmaterialsare
proportionaltoreq =[0.8,60,40,2.5]. WeusethesamerealdataasthatusedinIntOpt-C[12]as
numericalvaluesinourexperimentinstances. Inthisdataset[23],eachunknownmetalconcentration
2Ourimplementationisavailableathttps://github.com/Elizabethxyhu/NeurIPS_Two_Stage_Predict-Optimize
7

Table2: ComparisonoftheTwo-StagePredict+OptimizeframeworkandtheHuetal. frameworkon
thealloyproductionproblem.
|     |       | PReg          | Two-StagePredict   | Huetal.     |     |
| --- | ----- | ------------- | ------------------ | ----------- | --- |
|     | Alloy | Penaltyfactor | +OptimizeFramework | Framework   |     |
|     |       | 0.25±0.015    | 43.87±2.73         | 68.16±6.26  |     |
|     |       | 0.5±0.015     | 65.71±4.81         | 82.91±5.45  |     |
|     |       | 1±0.015       | 88.75±5.91         | 107.64±6.85 |     |
Brass
|     |                | 2±0.015    | 123.90±6.84  | 150.47±12.99 |     |
| --- | -------------- | ---------- | ------------ | ------------ | --- |
|     |                | 4±0.015    | 161.86±8.49  | 178.69±10.09 |     |
|     |                | 8±0.015    | 194.06±13.09 | 206.84±12.51 |     |
|     |                | 0.25±0.015 | 4.52±0.47    | 6.45±0.81    |     |
|     |                | 0.5±0.015  | 6.03±0.62    | 7.90±0.56    |     |
|     | Titanium-alloy | 1±0.015    | 8.58±0.74    | 10.73±0.81   |     |
|     |                | 2±0.015    | 12.17±1.24   | 14.17±1.31   |     |
|     |                | 4±0.015    | 16.10±1.06   | 17.48±0.99   |     |
|     |                | 8±0.015    | 19.69±0.91   | 21.08±1.91   |     |
Table3: Meanpost-hocregretsandstandarddeviationsforthealloyproductionproblemusingthe
Two-StagePredict+Optimizeframework.
PReg
|     | 2S  | IntOpt-C | Ridge k-NN | CART RF | NN TOV |
| --- | --- | -------- | ---------- | ------- | ------ |
Alloy Penaltyfactor
| 0.25±0.015 | 43.87±2.73 | 45.27±3.35 60.80±2.55 | 63.32±4.39 | 77.80±6.37 60.85±2.35  | 64.96±3.58 |
| ---------- | ---------- | --------------------- | ---------- | ---------------------- | ---------- |
| 0.5±0.015  | 65.71±4.81 | 67.69±4.25 71.12±3.48 | 74.36±5.69 | 93.67±7.03 70.86±3.29  | 74.32±2.90 |
| 1±0.015    | 88.75±5.91 | 89.83±4.79 91.82±6.41 | 96.52±8.90 | 125.50±9.49 90.97±6.14 | 93.12±4.24 |
Brass 312.02±6.94
| 2±0.015 | 123.90±6.84  | 125.46±9.26 133.18±12.98  | 140.77±16.02 | 189.12±16.10 131.12±12.48 | 130.67±10.52 |
| ------- | ------------ | ------------------------- | ------------ | ------------------------- | ------------ |
| 4±0.015 | 161.86±8.49  | 164.94±10.33 215.87±26.54 | 229.22±30.74 | 316.31±30.95 211.40±25.56 | 205.76±24.33 |
| 8±0.015 | 194.06±13.09 | 200.42±8.51 381.30±53.75  | 406.19±60.42 | 570.75±61.42 372.01±51.82 | 355.96±52.25 |
4.52±0.47
| 0.25±0.015 |           | 4.72±0.58 6.43±0.39  | 6.13±0.34 | 7.07±0.45 5.75±0.48  | 6.56±0.59 |
| ---------- | --------- | -------------------- | --------- | -------------------- | --------- |
| 0.5±0.015  | 6.03±0.62 | 6.23±0.64 7.71±0.45  | 7.27±0.39 | 8.57±0.45 6.76±0.55  | 7.38±0.67 |
| 1±0.015    | 8.58±0.74 | 8.71±0.95 10.26±0.62 | 9.55±0.52 | 11.57±0.52 8.76±0.72 | 9.03±0.84 |
Titanium-alloy 2±0.015 12.17±1.24 12.31±1.31 15.37±1.03 14.11±0.84 17.57±0.80 12.78±1.11 12.34±1.21 30.27±0.54
| 4±0.015 | 16.10±1.06 | 16.97±1.70 25.60±1.89 | 23.24±1.56 | 29.57±1.53 20.81±1.93 | 18.95±2.00 |
| ------- | ---------- | --------------------- | ---------- | --------------------- | ---------- |
| 8±0.015 | 19.69±0.91 | 20.80±1.74 46.04±3.65 | 41.49±3.03 | 53.57±3.10 36.88±3.63 | 32.16±3.60 |
isrelatedto4096features. Forexperimentsonbothalloys,350instancesareusedfortrainingand
150instancesfortestingthemodelperformance. ForNN,IntOpt-C,and2S,weusea5-layerfully
connectednetworkwith512neuronsperhiddenlayer.
InthepenaltyfunctiondescribedinAppendixC.1,weneedtochooseapenaltyfactor/multiplierfor
eachsupplier. Weconductexperimentson6typesofpenaltyfactor(σ)settings: 6vectorswhere
eachentryisi.i.d.uniformlysampledfrom[0.25±0.015],[0.5±0.015],[1.0±0.015],[2.0±0.015],
[4.0±0.015],and[8.0±0.015]respectively. Thisrandomsamplingofσ ensuresthatthepenalty
factorforeachsupplierisdifferent,butremainsroughlyonthesamescale.
Thefirstexperimentweruncompares2S+Two-StagePredict+OptimizeframeworkwithIntOpt-C+Hu
etal.framework.Specifically,wecomparea)using2SfortrainingandevaluatingusingtheTwo-Stage
Predict+OptimizeframeworkinSection3,versusb)usingIntOpt-Cfortrainingandevaluatingusing
thesamecorrectionfunctionfromtraining,accordingtotheHuetal.frameworkdescribedinSection2.
Table2comparesthemeanpost-hocregretandstandarddeviationsforthealloyproductionproblem
for the two different frameworks. The table shows that Two-Stage Predict+Optimize framework
always achieves smaller mean post-hoc regret than the Hu et al. framework. Compared with the
Huetal.framework,ourframeworkobtains6.18%-35.63%smallermeanpost-hocregretinbrass
production,and6.59%-29.89%smallermeanpost-hocregretintitanium-alloyproduction.
WepresentafurthercomparisoninAppendixFwithavariantoftheHuetal.framework—theℓ
2
projectionideain[3],whichperformsevenworsethantheHuetal.framework.
ThesecondexperimentcomparesvarioustrainingapproachesallevaluatedundertheTwo-Stage
Predict+Optimizeframework. Thatis,themodelsaretraineddifferently,butattesttime,wealways
useStage2optimizationtogiveafinalsolutionandevaluatepost-hocregretonit. Table3reportsthe
meanpost-hocregretsandstandarddeviationsacross10runsforeachtrainingmethodonthealloy
productionproblem. Thetableshowsthatourmethod,2S,achievesthebestperformance,compared
withIntOpt-Cachievingthesecondbestperformance,beatingalltheclassicaltrainingapproaches.
ComparedwithIntOpt-C,2Sobtains1.20%-3.18%smallermeanpost-hocregretsinbrassproduction,
and1.18%-5.33%smallermeanpost-hocregretintitanium-alloyproduction. Comparedwiththe
classicalapproaches,theimprovementsaremuchmoresignificant. 2Sobtainsatleast2.44%-45.48%
smallermeanpost-hocregretsinbrassproduction,andatleast1.39%-38.78%smallermeanpost-hoc
regretintitanium-alloyproduction. TheaverageTrueOptimalValues(TOV)arereportedinthelast
columnofTable3forreference,althoughthereadershouldtakecaretonotover-interprettheratio
8

Table4:Meanpost-hocregretsandstandarddeviationsfor0-1knapsackproblemusingtheTwo-Stage
Predict+Optimizeframework.
Penalty
| PReg | 2S  | CombOptNet | Ridge | k-NN | CART |     | RF NN | TOV |
| ---- | --- | ---------- | ----- | ---- | ---- | --- | ----- | --- |
factor
| 0.21 | 1.26±0.01 | 9.45±0.19 | 9.46±0.19 | 9.38±0.21 | 8.67±0.13 | 9.50±0.26 | 9.81±0.20 |     |
| ---- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --- |
100 0.25 6.28±0.05 9.60±0.22 9.77±0.19 9.70±0.19 9.19±0.12 9.82±0.27 10.11±0.20 29.68±0.14
| 0.3  | 9.22±0.10 | 10.45±0.34 | 10.16±0.19 | 10.10±0.18 | 9.85±0.11 | 10.22±0.28 | 10.49±0.21 |     |
| ---- | --------- | ---------- | ---------- | ---------- | --------- | ---------- | ---------- | --- |
| 0.21 | 0.73±0.01 | 8.90±8.97  | 9.12±0.22  | 8.91±0.20  | 8.46±0.18 | 9.20±0.27  | 9.66±0.47  |     |
150 0.25 3.64±0.04 9.11±9.41 9.40±0.21 9.19±0.20 8.88±0.17 9.47±0.26 9.92±0.43 40.23±0.19
| 0.3  | 7.27±0.06 | 9.34±9.38  | 9.76±0.22 | 9.53±0.19 | 9.41±0.17 | 9.81±0.24 | 10.23±0.38 |     |
| ---- | --------- | ---------- | --------- | --------- | --------- | --------- | ---------- | --- |
| 0.21 | 0.33±0.01 | 15.16±0.21 | 6.57±0.21 | 6.38±0.29 | 6.26±0.21 | 6.59±0.23 | 7.08±0.95  |     |
200 0.25 1.67±0.03 15.20±0.27 6.80±0.20 6.62±0.29 6.57±0.19 6.82±0.21 7.27±0.88 48.13±0.24
| 0.3  | 3.33±0.06 | 15.25±0.22 | 7.09±0.19 | 6.91±0.28 | 6.95±0.19 | 7.10±0.18 | 7.52±0.80 |     |
| ---- | --------- | ---------- | --------- | --------- | --------- | --------- | --------- | --- |
| 0.21 | 0.07±0.00 | 20.42±0.25 | 2.39±0.22 | 2.18±0.20 | 2.45±0.20 | 2.34±0.32 | 2.70±1.34 |     |
250 0.25 0.34±0.02 20.47±0.13 2.53±0.21 2.34±0.19 2.60±0.19 2.49±0.30 2.82±1.26 53.43±0.26
| 0.3 | 0.69±0.04 | 20.54±0.32 | 2.71±0.20 | 2.54±0.18 | 2.79±0.18 | 2.67±0.28 | 2.97±1.16 |     |
| --- | --------- | ---------- | --------- | --------- | --------- | --------- | --------- | --- |
Table 5: Mean post-hoc regrets and standard deviations for the NSP using the Two-Stage Pre-
dict+Optimizeframework.
| Penaltyfactor | 2S         | Ridge       | k-NN        | CART         |     | RF          | NN         | TOV |
| ------------- | ---------- | ----------- | ----------- | ------------ | --- | ----------- | ---------- | --- |
| 0.25±0.015    | 3.94±1.91  | 6.45±4.68   | 15.20±5.76  | 26.20±8.96   |     | 19.47±7.19  | 4.27±2.22  |     |
| 0.5±0.015     | 6.92±2.26  | 12.68±9.35  | 30.29±11.53 | 52.47±17.96  |     | 38.93±14.42 | 8.20±4.40  |     |
| 1.0±0.015     | 13.12±3.15 | 25.12±18.71 | 60.43±23.07 | 105.01±36.00 |     | 77.86±28.99 | 16.00±8.78 |     |
190.21±26.17
| 2.0±0.015 | 25.04±9.29  | 49.95±37.39   | 120.62±46.08  | 210.02±72.06  |     | 155.64±58.06  | 31.51±17.40  |     |
| --------- | ----------- | ------------- | ------------- | ------------- | --- | ------------- | ------------ | --- |
| 4.0±0.015 | 33.29±9.53  | 99.61±74.78   | 241.01±92.14  | 420.04±144.18 |     | 311.19±116.23 | 62.52±34.64  |     |
| 8.0±0.015 | 46.72±14.80 | 198.91±149.54 | 481.79±184.27 | 840.10±288.45 |     | 622.32±232.56 | 124.54±69.14 |     |
betweenthepost-hocregretandthetrueoptimalvalue,sincethepost-hocregretalsoincludesthe
penaltytermwhichincreaseswiththepenaltyfactors.
0-1knapsack Inthesecondexample,weshowcaseourframeworkonapackingintegerprogram-
mingproblem,avariantofthe0-1knapsackproblem,withunknownitempricesp andsizess . See
|     |     |     |     |     |     |     | i   | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
AppendixC.2fordetailsofanapplicationinrunninga“proxybuyer”business. Here,theunknown
parametersappearinboththeobjectiveandconstraints. Theproposed2Smethodcanhandlethis
MILPstraightforwardly,buttheIntOpt-Cmethodcannotbeapplied. Thus,weonlyexperimentwith
theTwo-StagePredict+Optimizeframeworkforevaluation,andcomparetheproposed2Smethod
withclassicalapproachesandCombOptNet. Again,allapproachesareevaluatedattesttimeusing
theStage2optimizationtoyieldthefinalsolution,onwhichthepost-hocregretiscomputed.
TheMILPformulationofthetwostagesandthepenaltyfunctionaredescribedinAppendixC.2.
WeusethedatasetofPaulusetal.[23],inwhicheach0-1knapsackinstanceconsistsof10items
andeachitemhas4096featuresrelatedtoitspriceandsize. ForbothNNandourmethod,weusea
5-layerfully-connectednetworkwith512neuronsperhiddenlayer. Weconductexperimentson4
differentknapsackcapacities:100,150,200,and250. Weuse700instancesfortrainingand300
instancesfortestingthemodelperformance. Consideringthereal-lifesetting,weuse3scalesofthe
| penaltyfactorforthepenaltyfunctioninAppendixC.2:σ |     |     |     |     | =0.05,0.25,or0.5. |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | --- |
Table4reportsthemeanpost-hocregretsandstandarddeviationsacross10runsforeachapproach
onthis0-1knapsackproblem. Duetothespacelimitationandthefactthatlargerpenaltyfactors
areunrealisticinthisproblemsetting,wepresentpenaltyfactors≥1inAppendixG.Theaverage
TrueOptimalValues(TOV)arereportedinthelastcolumn,againforreference. Asshowninthe
table,ourproposed2Smethodhassignificantlybetterresults. Inaddition,weobservethatacross
allapproaches,thepost-hocregretsdecreaseastheknapsackcapacityincreases:thisisduetothe
factthatasthecapacityincreases,moreandmoreitemscanbeselected,andsominorinaccuracies
inpredictedvalues/weightsdonotaffecttheselectedsetofitemsasmuch. Ontheotherhand,the
advantageofour2Smethodoverotherapproachesactuallybecomesmoresignificantasthecapacity
increases,demonstratingthesuperioraccuracyofourapproach.
NurseSchedulingProblem Ourlastexperimentisonthenurseschedulingproblem(NSP)with
unknownpatientsneeds,withthegoalofschedulinganurserostersatisfyingunknownpatientload
demandswhileminimizingmismatchednurse-shiftpreferencesastheobjective. SeeAppendixC.3
foradescriptionoftheapplicationscenario,theMILPformulationsofthetwostages,aswellasthe
associatedpenaltyfunction. GiventhatNSPisnotanLP,IntOpt-Cagaindoesnotapply,andsowe
9

only comparetheproposed2Strainingmethodwiththeclassicalapproaches,usingtheTwo-Stage
Predict+Optimizeframeworkforevaluation. EachNSPinstanceconsistsof15nurses,7days,and3
shiftsperday. ThenursepreferencesareobtainedfromtheNSPLibdataset[26],whichiswidely
usedforNSP[16,20]. Thenumberofpatientsthateachnursecanserveinoneshiftisrandomly
generatedfrom[10,20],representingthefactthateachnursehasdifferentcapabilities. Giventhatwe
areunabletofinddatasetsspecificallyforthepatientloaddemandsandrelevantpredictionfeatures,
wefollowtheexperimentalapproachofDemirovicetal.[4,5,6]anduserealdatafromadifferent
problem(theICONschedulingcompetition)asthenumericalvaluesrequiredforourexperiment
instances. Inthisdataset,theunknownnumberofpatientspershiftispredictedby8features.
Sincetherearefarfewerfeaturesthanthepreviousexperiments,forbothNNand2Sweuseasmaller
networkstructure:a4-layerfully-connectednetworkwith16neuronsperhiddenlayer. Weuse210
instancesfortrainingand90instancesfortesting. Justlikethefirstexperiment,weuse6scalesof
penaltyfactors(seeAppendixC.3forthepenaltyfunction):γ withi.i.d.entriesdrawnuniformly
from[0.25±0.015],[0.5±0.015],[1.0±0.015],[2.0±0.015],[4.0±0.015],and[8.0±0.015].
Table5reportsthemeanpost-hocregretsandstandarddeviationsacross10runsforeachapproach
ontheNSP.Thetableshowsthattheproposed2Smethodagainhasthebestperformanceamong
all the training approaches. Our 2S method obtains at least 7.61%, 15.65%, 17.99%, 20.51%,
46.76%,and62.49%smallerpost-hocregretthanotherclassicalmethodswhenthepenaltyfactoris
[0.25±0.015],[0.5±0.015],[1.0±0.015],[2.0±0.015],[4.0±0.015],and[8.0±0.015]respectively.
RuntimeAnalysis AppendixHgivesthetrainingtimesforeachmethod.Mostclassicalapproaches
arefasterthanour2Smethod,althoughasshowntheirpost-hocregretsaremuchworse. Inalloy
production,theonlysettingwhereIntOpt-Capplies,itsrunningtimeisshorterbutcomparablewith
2S.In0-1knapsack,theonlyproblemwithpublicCombOptNetcode,the2Smethodismuchfaster.
6 LiteratureReview
Section1alreadysummarizedpriorworksinPredict+Optimize,mostofwhichfocusonlearning
unknownsonlyintheobjective. OnlytheHuetal.[12]frameworkconsidersunknownsinconstraints.
Herewesummarizeotherworksrelatedtolearningunknownsinoptimizationproblemconstraints,
particularlythoseoutsideofPredict+Optimize. Theseworkscanbeplacedintotwocategories.
Onecategoryalsoconsiderslearningunknownsinconstraints,butwithverydifferentgoalsandmea-
suresofloss. Forexample,CombOptNet[23]andNandwanietal.[21]focusonlearningparameters
soastomakethepredictedoptimalsolution(first-stagesolutioninourproposedframework)asclose
tothetrueoptimalsolutionx∗ aspossibleinthesolutionspace/metric. Bycontrast,ourproposed
frameworkexplicitlyformulatesthetwo-stageframeworkandpost-hocregretinordertodirectly
capturerewardsandcostsinapplicationscenarios. Experimentson0-1knapsackinSection5show
thattheseothermethodsyieldworsepredictiveperformancewhenevaluatedonthepost-hocregret,
undertheproposedtwo-stageframework.
AnothercategorygiveswaystodifferentiatethroughLPsorLPswithregularizations,asatechnical
component in a gradient-based training algorithm. As mentioned in Section 4, these works can
indeedbeusedinplaceofourproposedapproachinSection4/AppendixB.However,wepointout
that: (i) these other technical tools are essentially orthogonal to our primary contribution, which
isthetwo-stageframework(Section3),and(ii)nonetheless,experimentsonthe0-1knapsackin
AppendixEdemonstratethatourgradientcalculationapproachperformsatleastaswellinpost-hoc
regretperformanceasotherworks,whilebeingfaster.
7 Summary
WeproposedTwo-StagePredict+Optimize:anew,conceptuallysimplerandmorepowerfulframework
forthePredict+Optimizesettingwhereunknownparameterscanappearbothintheobjectiveandin
constraints. Weshowedhowthesimplerperspectiveofferedbytheframeworkallowsustogivea
generaltrainingframeworkforallMILPs,contrastingpriorworkwhichapplyonlytocoveringand
packingLPs. Experimentalresultsdemonstratethatourtrainingmethodofferssignificantlybetter
predictionperformanceoverotherclassicalandstate-of-the-artapproaches.
10

Acknowledgments
We thank the anonymous referees for their constructive comments. In addition, Xinyi Hu and
JimmyH.M.LeeacknowledgethefinancialsupportofaGeneralResearchFund(RGCRef. No.
CUHK14206321)bytheUniversityGrantsCommittee,HongKong. JasperC.H.Leewassupported
inpartbythegenerousfundingofaCroucherFellowshipforPostdoctoralResearch,NSFaward
DMS-2023239,NSFMediumAwardCCF-2107079andNSFAiTFAwardCCF-2006206.
References
[1] A.Agrawal,B.Amos,S.Barratt,S.Boyd,S.Diamond,andJ.Z.Kolter. Differentiableconvex
optimizationlayers. Advancesinneuralinformationprocessingsystems,32,2019.
[2] B.AmosandJ.Z.Kolter. Optnet: Differentiableoptimizationasalayerinneuralnetworks. In
InternationalConferenceonMachineLearning,pages136–145.PMLR,2017.
[3] B. Chen, P. L. Donti, K. Baker, J. Z. Kolter, and M. Bergés. Enforcing policy feasibility
constraintsthroughdifferentiableprojectionforenergyoptimization. InProceedingsofthe
TwelfthACMInternationalConferenceonFutureEnergySystems,pages199–210,2021.
[4] E.Demirovic´,P.J.Stuckey,J.Bailey,J.Chan,C.Leckie,K.Ramamohanarao,andT.Guns.
An investigation into Prediction+Optimisation for the knapsack problem. In International
ConferenceonIntegrationofConstraintProgramming,ArtificialIntelligence,andOperations
Research,pages241–257.Springer,2019.
[5] E.Demirovic´,P.J.Stuckey,J.Bailey,J.Chan,C.Leckie,K.Ramamohanarao,andT.Guns.
Predict+Optimisewithrankingobjectives: Exhaustivelylearninglinearfunctions. Proceedings
oftheTwenty-EighthInternationalJointConferenceonArtificialIntelligence,pages1078–1085,
2019.
[6] E.Demirovic´,P.J.Stuckey,T.Guns,J.Bailey,C.Leckie,K.Ramamohanarao,andJ.Chan.
Dynamic programming for Predict+Optimise. In Proceedings of the Thirty-Fourth AAAI
ConferenceonArtificialIntelligence,pages1444–1451,2020.
[7] A. N. Elmachtoub and P. Grigas. Smart “Predict, then Optimize”. Management Science,
68(1):9–26,2022.
[8] A.N.Elmachtoub,J.C.N.Liang,andR.McNellis. Decisiontreesfordecision-makingunder
thepredict-then-optimizeframework. InProceedingsofthe37thInternationalConferenceon
MachineLearning,pages2858–2867,2020.
[9] J.Friedman,T.Hastie,andR.Tibshirani. Theelementsofstatisticallearning. Springerseries
instatisticsNewYork,2001. Volume1,Number10.
[10] A.U.Guler,E.Demirovic´,J.Chan,J.Bailey,C.Leckie,andP.J.Stuckey. Adivideandconquer
algorithmforPredict+Optimizewithnon-convexproblems. InProceedingsoftheThirty-Sixth
AAAIConferenceonArtificialIntelligence,2022.
[11] GurobiOptimization,LLC. GurobiOptimizerReferenceManual,2023.
[12] X.Hu,J.C.H.Lee,andJ.H.M.Lee. Predict+OptimizeforpackingandcoveringLPswith
unknown parameters in constraints. In Proceedings of the AAAI Conference on Artificial
Intelligence,2022.
[13] X.Hu,J.C.H.Lee,J.H.M.Lee,andA.Z.Zhong.Branch&Learnforrecursivelyanditeratively
solvableproblemsinPredict+Optimize. InAdvancesinNeuralInformationProcessingSystems,
2022.
[14] K.B.KabirandI.Mahmud. Studyoferosion-corrosionofstainlesssteel,brassandaluminum
byopencircuitpotentialmeasurements. JournalofChemicalEngineering,pages13–17,2010.
[15] N.Kahraman,B.Gülenç,andF.Findik. Joiningoftitanium/stainlesssteelbyexplosivewelding
andeffectoninterface. JournalofMaterialsProcessingTechnology,169(2):127–133,2005.
11

[16] B.MaenhoutandM.Vanhoucke. BranchingstrategiesinaBranch-and-Priceapproachfora
multipleobjectivenurseschedulingproblem. Journalofscheduling,13(1):77–93,2010.
[17] J.Mandi,V.Bucarey,M.M.K.Tchomba,andT.Guns. Decision-focusedlearning:Throughthe
lensoflearningtorank. InInternationalConferenceonMachineLearning,pages14935–14947.
PMLR,2022.
[18] J.MandiandT.Guns. InteriorpointsolvingforLP-basedPrediction+Optimisation. Advances
inNeuralInformationProcessingSystems,33:7272–7282,2020.
[19] M.Mulamba,J.Mandi,M.Diligenti,M.Lombardi,V.Bucarey,andT.Guns. Contrastivelosses
andsolutioncachingforPredict-and-Optimize. arXivpreprintarXiv:2011.05354,2020.
[20] R.Muniyan,R.Ramalingam,S.S.Alshamrani,D.Gangodkar,A.Dumka,R.Singh,A.Gehlot,
and M. Rashid. Artificial bee colony algorithm with Nelder–Mead method to solve nurse
schedulingproblem. Mathematics,10(15):2576,2022.
[21] Y.Nandwani,R.Ranjan,P.Singla,etal. Asolver-freeframeworkforscalablelearninginneural
ilparchitectures. AdvancesinNeuralInformationProcessingSystems,35:7972–7986,2022.
[22] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin,
N.Gimelshein,L.Antiga,A.Desmaison,A.Kopf,E.Yang,Z.DeVito,M.Raison,A.Tejani,
S.Chilamkurthy,B.Steiner,L.Fang,J.Bai,andS.Chintala. Pytorch: Animperativestyle,
high-performancedeeplearninglibrary. InAdvancesinNeuralInformationProcessingSystems
32,pages8024–8035.2019.
[23] A.Paulus,M.Rolínek,V.Musil,B.Amos,andG.Martius. Comboptnet: FittherightNP-hard
problembylearningintegerprogrammingconstraints. InInternationalConferenceonMachine
Learning,pages8443–8453.PMLR,2021.
[24] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel,
P.Prettenhofer,R.Weiss,V.Dubourg,J.Vanderplas,A.Passos,D.Cournapeau,M.Brucher,
M.Perrot,andE.Duchesnay. Scikit-learn: MachinelearninginPython. JournalofMachine
LearningResearch,12:2825–2830,2011.
[25] D.E.Rumelhart,G.E.Hinton,andR.J.Williams.Learningrepresentationsbyback-propagating
errors. nature,323(6088):533–536,1986.
[26] M.VanhouckeandB.Maenhout. Nsplib–anurseschedulingproblemlibrary: Atooltoevaluate
(meta-)heuristicprocedures. InOperationalresearchforhealthpolicy:makingbetterdecisions,
proceedingsofthe31stannualmeetingoftheworkinggrouponoperationsresearchappliedto
healthservices,pages151–165,2007.
[27] B.Wilder,B.Dilkina,andM.Tambe. Meldingthedata-decisionspipeline: Decision-focused
learningforcombinatorialoptimization. InProceedingsoftheThirty-ThirdAAAIConference
onArtificialIntelligence,pages1658–1665,2019.
12

A DetaileddiscussionontheTwo-StagePredict+Optimizeframework
A.1 Problemmodellingusingtheframework
As mentioned in Section 3, the proposed Two-Stage Prediction+Optimize framework is phrased
differently from some other two-stage problem formulations. The proposed framework phrases
Stage1solutionsassoftcommitments,andcorrectsStage1solutionswithpenaltyinStage2. On
the other hand, some two-stage frameworks phrase Stage 1 solutions as hard commitments, and
includeexplicitrecoursevariablesinbothstagesofOPtomodelthecorrectioninStage2. Some
optimizationproblemsaremorenaturaltoexpressaccordingtooneperspectivethantheother,while
someproblemsmightbestraightforwardtoexpressineither. Thissectionaimstoshowthatour
framework,whileexplicitlystatedandmotivatedaccordingtothefirstperspective,isinfactgeneral
enoughtoalsoeasilymodelthesecondperspectiveofhardcommitmentsandrecourseactions. In
whatfollows,wefirstdescribedifferenttypesofvariablesandhowourframeworkcancapturethem.
Then,wegivetwoexampleproblemsthatrespectivelyusethesoft/hardcommitmentperspectives,
andwedetailhowtheproblemcanbemodelled.
Softcommitmentvariables: Thesearevariableswhichrepresentdecisionsthatcorrespondtosoft
commitmentsmadeinStage1inanapplication,namelydecisionsthatmaybemodified
oncethetrueparametersarerevealed,butatacostorpenalty. ThediscussioninSection3is
tailoredforthiskindofvariables—simplydefinesuchavariableinStage1anduseafinite
penaltyfunctiontomodelthecostofchangingthissoftcommitmentinStage2.
Hardcommitmentvariables: Thesearevariablesx∗ whichrepresenthardcommitmentsmade
hard
inStage1,meaningthataftercommitment,theyabsolutelycannotchangeinStage2. To
model these variables in our framework, simply write a penalty function that is infinite
wheneverStage1andStage2solutionsforthesevariablesaredifferent. Explicitly,adda
term∞·1[x∗ ̸= x∗ ]. Thisway,noStage2solutionwillchangethesevariables
hard,1 hard,2
fromwhattheywerecommittedtoinStage1.
Recourse/othervariables: Thesearevariableswhichrepresentexplicitactions/decisionstakenonly
inStage2,oncethetrueparametersarerevealed. Thesevariablesarenecessary,forexample,
whenStage1actionsareallhardcommitmentvariables,toensurethatwehaveamechanism
forcorrectiveactionifthehardStage1decisionsareinanyway“incompatible"withthe
revealedparameters. Thesecorrectiveactionsalsotypicallycomeatacost. Thus,tomodel
thesevariables,simplyincludetheminbothStages1and2,andincorporatetheircostinto
theobjectiveoftheoptimizationproblem. Thereshouldalsobe0penaltyformodifying
thesevariablesbetweenthestages.
To summarize, Stage 1 actions can be classified as either soft or hard commitments, depending
onwhethertheycanbechangedinStage2(atafinitepenalty). Stage2actionsareclassifiedas
“recourse"variables,whicharesimplyvariablesthathavenopenaltyfromchangingbetweenStage
1toStage2. Theabovediscussionshowshowourframeworkcapturesallthesepossibilities. We
nowgivetwoexampleapplications:thefirstoneismorenaturallyexpressedviathesoftcommitment
perspective,andthesecondoneismorenaturaltophraseusinghardcommitments+recourse. We
givealsotheirexplicitformulationstodemonstratehowthemodellingisdoneinourframework.
Wefirstshowanexampleproblemwhichisnaturallymodelledusingsoftcommitmentvariables
andpenaltyfunctions. Considertheproduct-stockingprobleminExample1again,whereregular
ordershavetobeplacedtwoweeksaheadofmonthlydeliveries. Weaimtomaximizethenetprofit
bysellingstockedproducts,undertheconstraintthattheavailablestoragespaceislimited. Each
productihasapurchasepricepu(thepriceofpurchasingtheproductfromthewholesalecompany)
i
andasellingpriceps(thepriceofsellingtheproducttocustomers),andneedss spacetobestocked.
i i
Letx denotewhethertheproductiisordered. InStage1,i.e.,twoweeksbeforethedelivery,the
i
availablestoragespaceSpatthetimeofdeliveryisunknown,andweplacetheorderxbasedon
estimatedspace. InStage2,i.e.,thenightbeforethedelivery,thepreciseavailablespaceisrevealed,
andweaskthewholesalecompanytochangetheorderbutneedtopayasurchargeforlast-minute
changes. Assumethesurchargeforthelast-minutechangeintheorderofproductiisc . Inthis
i
example,x isthusasoftcommitmentvariable,andwemodelthesurchargec usingthepenalty
i i
functionoftheframework.
13

Theproposedframeworkcannaturallymodelthisproblem. TheStage1OPcanbeformulatedas:
(cid:88)
x∗ =argmax (ps−pu)x
1 i i i
x
i
s.t. (cid:88) s x ≤Sˆp, x∈{0,1}
i i
i
InStage2,theorderx∗canbechangedwithsurcharges,whichcanbemodelledasapenaltyfunction:
1
(cid:88)
Pen(x∗ →x)= c |x∗−x |
1 i 1 i
i
ThentheStage2OPcanbeformulatedas:
(cid:88) (cid:88)
x∗ =argmax (ps−pu)x − c |x∗−x |
2 i i i i 1 i
x
i i
(cid:88)
s.t. s x ≤Sp, x∈{0,1}
i i
i
Next,wegiveanexampleproblemwhichismorenaturallymodelledusinghardcommitmentvariables
andrecoursevariables. Consideraproduction-planningproblem:acompanyownsasetoffacilities
andprovidesservicestoasetofcustomers. Eachfacilityicanprovideafixedamountofservicesm
i
andhasafixedoperatingcostf inthestandardworkingmode. Thecompanyaimstomeetcustomer
i
demandsdattheminimumoperatingcosts. InStage1,thecompanydecideswhichfacilitiestoopen
for production based on the estimated demands dˆ. This is a binary decision variable x for each
i
facilityi. InStage2,theordersfromcustomersarriveandthedemandsdarerevealed. Iftheservices
providedbytheoperatingfacilitiesinthestandardmodecannotmeetdemands,thecompanywill
asksomefacilitiesthatarealreadyoperating(i.e.x = 1)toworkovertime,butnaturallyneedto
i
payhighovertimefees. Leto denotetheunitovertimefeeforproducingserviceinfacilityi,andσ
i i
denotetheamountofserviceprovidedbyovertimeworkinginfacilityi.
Thisexampleisnaturallymodelledusinghardcommitmentvariablesandrecoursevariables. Which
facilities to operate, x, is a vector of 0/1 hard commitment variables. The amount of service, σ,
providedbytheovertimeworkingmodeofoperatingfacilitiescanbemodeledbyrecoursevariables,
and the recourse costs are the overtime fees o. Using hard commitment variables and recourse
variables,theStage1OPcanbeformulatedas:
(cid:88) (cid:88)
x∗,σ∗ =argmin f x + o σ
1 1 i i i i
x,σ
i i
s.t. (cid:88) (m +σ )x ≥dˆ, x∈{0,1}, σ ≥0
i i i
i
InStage2,weincludeaterm∞·1[x∗ ̸=x]inthepenaltyfunctionpartoftheStage2objectiveto
1
makesurethatxcannotbechanged,whilethepenaltyforchangingσiszerosinceitisarecourse
variable. TheStage2OPisformulatedas:
(cid:88) (cid:88)
x∗,σ∗ =argmin f x + o σ +∞·1[x∗ ̸=x]
2 2 i i i i 1
x,σ
i i
(cid:88)
s.t. (m +σ )x ≥d, x∈{0,1}, σ ≥0
i i i
i
Insummary,wediscussedhowtomodelinourframeworksoftandhardcommitmentactionsinStage
1,aswellasrecourse/otheractionsinStage2. Wegavetwoconcreteexamplestodemonstratehow
suchmodellingcanbedone.
A.2 Whatifcorrection/recourseisnotpossibleintheapplication?
Themotivatingpremiseofthispaperisthattheapplicationscenarioathandallowsforsomepost-
hoccorrectiveactiononcethetrueparametersarerevealed. Onenaturalquestionis:whatifsuch
14

correctiveaction(Stage2actions)isnotactuallypossibleintheapplication? Forexample,inour
runningexampleoftheproduct-stockingproblem,weconsideredawholesalecompanythatallowsfor
orderchangesthenightbefore. Otherwholesalersmaynotallowsuchacorrection/modification. Our
frameworkcanessentiallystillmodelthesescenarios:justsetthepenaltyofmodificationtoinfinity
|                                          | Concretely,usethepenaltyfunction∞·1[x∗ |     | ̸=x∗](or |
| ---------------------------------------- | -------------------------------------- | --- | -------- |
| (oratleast,verylargenumbersforpractice). |                                        |     | 2 1      |
replace∞withaverylargenumber). Thispenaltyfunctionencouragesthelearningalgorithmto
learnconservativepredictionsthatmaximizethechancesofyieldingStage1decisionsthatremain
feasibleinStage2.
Toshowthis,werananotherquickexperiment,usingthe0-1knapsackproblemsettinginthepaper
(with knapsack capacity = 100). This time, as we varied the magnitude of the penalty function,
wemeasureattesttimetheempiricalfractionofStage1solutionsthatremainfeasibleunderthe
trueparameters. TheresultsinTable6demonstrateourclaimthatasthepenaltytermincreases,
thepredictionsgetmoreandmorelikelytoremainfeasible,makingitareasonablewaytotraina
predictorevenwhenStage2correctionmechanismsdonotactuallyexistintheapplication.
Table6: MeanandstandarddeviationofempiricalfractionofStage1solutionsthatremainfeasible
inStage2,forthe0-1knapsackproblemwhencapacityis100usingtheTwo-StagePredict+Optimize
framework.
|     | PenaltyFactor | Feasibility% |     |
| --- | ------------- | ------------ | --- |
|     | 0.05          | 0.00%±0.00%  |     |
|     | 0.25          | 0.00%±0.00%  |     |
|     | 0.5           | 1.73%±0.52%  |     |
|     | 1             | 50.93%±1.92% |     |
|     | 2             | 51.63%±1.22% |     |
|     | 4             | 99.07%±0.31% |     |
A.3 Two-StagePredict+OptimizevsPriorHuetal.Framework
AsmentionedearlierinSection3,Two-StagePredict+Optimizeistechnicallymathematicallyequiva-
lenttothepriorframeworkofHuetal.[12],inthesenseofexpressiveness,ignoringdifferentiability
issues. Ontheonehand,wecanregardtheStage2optimizationasaformofcorrectionfunction,
andhenceTwo-StagePredict+OptimizecanbeconsideredasaspecialcaseoftheHuetal.[12]
framework. On the other hand, given a correction function as in the Hu et al. [12] framework,
we can simply modify the penalty function such that we keep the penalty value of the corrected
solution,andmakethepenaltyvalueinfiniteforallotherpotentialStage2solutions. Thisforces
theStage2optimizationtoalwaysemulatethecorrectionfunction. Inthissense,ourTwo-Stage
Predict+OptimizeframeworkcanalsoemulatetheHuetal.[12]framework,meaningthatthetwo
frameworksaretechnicallyequivalent.
Nevertheless,theTwo-StagePredict+Optimizeframeworkisbothconceptuallysimplerandeasier
toapply. Inthemainpaper,weshowedhowtoperformend-to-endneuralnetworktrainingwithin
thisnewframeworkwheneverbothstagesofoptimizationcanbephrasedasMILPs,andalsogive
empiricalexperimentalresults. Together,theydemonstratethemuchmoregeneralapplicabilityof
theTwo-StagePredict+Optimizeframework.
We end this appendix with the statement and short proof that, conditioned on the same penalty
functionandpredictionmodel,Two-StagePredict+Optimizealwaysoutputsatleastasgoodafinal
solutionasthepriorframeworkusinganycorrectionfunction.
PropositionA.1. ConsideranarbitraryminimizationPara-OPP,penaltyfunctionPen,correction
functionx∗ ,estimatedparametersθˆandtrueparametersθ. Letx∗(θˆ)andx∗(θˆ)bothdenotethe
corr
1
estimatedsolutionfromtheestimatedparametersθˆ,x∗(θˆ,θ)betheoutputfinalsolutionfromthe
2
Two-StagePredict+Optimizeframework,andx∗ (θˆ,θ)betheoutputcorrectedsolutionfromthe
corr
| priorframeworkofHuetal. | Then, |     |     |
| ----------------------- | ----- | --- | --- |
obj(x∗(θˆ,θ),θ)+Pen(x∗(θˆ)→x∗(θˆ,θ))≤obj(x∗ (θˆ,θ),θ)+Pen(x∗(θˆ)→x∗ (θˆ,θ))
| 2   | 1 2 | corr | corr |
| --- | --- | ---- | ---- |
Proof. ObservethatbothsidesoftheinequalityaretheobjectiveoftheStage2optimizationproblem,
evaluatedatx∗andx∗ respectively. Sincex∗istheoptimalsolutiontotheminimizationproblem,
| 2 corr | 2   |     |     |
| ------ | --- | --- | --- |
theinequalityfollowsdirectly.
15

B GradientCalculationsforProblem(5)
|               | ∂x∗ | InthecontextoftheMILP,theunknownparameterθˆmayeitherbec,A,b,G, |     |     |     |     |     |     |     |
| ------------- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| Approximating | 1.  |                                                                |     |     |     |     |     |     |     |
∂θˆ
or h. Using the solution x and the barrier weight µ returned from solving Problem (5), we can
∂x∗
compute the relevant derivatives of 1. The case of c has already been derived by Mandi and
∂cˆ
Guns[18](seeAppendixA.1andA.2intheirpaper). Problem(5)canberewrittenas:
d+q
(cid:88)
|     |     |     | x∗ =argminc′⊤x′−µ |     |     | ln(x′) |     |     |     |
| --- | --- | --- | ----------------- | --- | --- | ------ | --- | --- | --- |
i
|     |     |     |     | x′  |     |     |     |     | (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i=1
|     |     |     | s.t. | A′x′ =b′ |     |     |     |     |     |
| --- | --- | --- | ---- | -------- | --- | --- | --- | --- | --- |
where
|     |     |     | c′ =[c   | 0]∈Rd+q  |               |     |     |     |     |
| --- | --- | --- | -------- | -------- | ------------- | --- | --- | --- | --- |
|     |     |     | x′ =[x   | s]∈Rd+q  |               |     |     |     |     |
|     |     |     | (cid:20) | (cid:21) |               |     |     |     |     |
|     |     |     |          | A 0      |               |     |     |     |     |
|     |     |     | A′ =     |          | ∈R(p+q)×(d+q) |     |     |     |     |
|     |     |     |          | G −I     |               |     |     |     |     |
(cid:20) (cid:21)
b ∈Rp+q
b′ =
h
FactB.1. ConsidertheLPrelaxation(6),definingx′asafunctionofc′,A′andb′. Then,according
toMandiandGuns[18],underthisdefinitionofx∗,
|     |     |       |     |   | ∂x′ |    |    |    |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     |     | −X′−1T | A′⊤ | −c′ |     |     | τI  |     |     |
∂c′
|     |     |    | A′  | 0 −b′  | ∂y′ | = | 0   |    |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
′
|     |     | −c′⊤ | b′⊤ | κ   | ∂ ∂ | c τ | x⊤  |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|     |     |      |     | τ   | ∂c′ |     |     |     |     |
whereX′ =diag(x′),t=µX′−1e,T =diag(t),y′isthelagrangianmultiplierofProblem(6),and
κandτ areadditionalvariablesaddedbyMandiandGuns[18]torepresentthedualitygap. The
∂x∗
| gradient | 1 canbeobtainedbysolvingthissystemofequalities. |     |     |     |     |     |     |     |     |
| -------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
∂cˆ
| Definethenotationf(x,c,G,h)=c⊤x−µ |     |     |     | (cid:80)d |            | (cid:80)q | ln(G⊤x−h |                   |     |
| --------------------------------- | --- | --- | --- | --------- | ---------- | --------- | -------- | ----------------- | --- |
|                                   |     |     |     |           | ln(x i )−µ |           |          | i ). Then,Problem |     |
|                                   |     |     |     | i=1       |            |           | i=1      | i                 |     |
(5)canbeexpressedasfinding:
|     |     | x∗  | =argminf(x,c,G,h) |     |     | s.t. Ax=b |     |     | (7) |
| --- | --- | --- | ----------------- | --- | --- | --------- | --- | --- | --- |
x
|     |     |     |     |     |     |     |     | ∂x∗,∂x∗,∂x∗ | ∂x∗ |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
Usingthisnotation,wewritedownthefollowingfourlemmasoncomputing ,and
|     |     |     |     |     |     |     |     | ∂G ∂h ∂A | ∂b  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
approximately.
LemmaB.2. ConsidertheLPrelaxation(7),definingx∗ asafunctionofc,A,b,Gandh. Then,
underthisdefinitionofx∗,
∂x∗
|     |     | =(H−1A⊤(AH−1A⊤)−1AH−1−H−1)f |     |     |     |     | (x,c,G,h) |     |     |
| --- | --- | --------------------------- | --- | --- | --- | --- | --------- | --- | --- |
|     | ∂G  |                             |     |     |     |     | Gx        |     |     |
whereH = f xx (x,c,G,h)denotesthematrixofsecondderivativesoff withrespecttodifferent
coordinatesofx,andsimilarlyforothersubscripts,andexplicitly:
|     |      |            | (cid:26) µx−2+µ | (cid:80)q   | G2     | /(G⊤x−h |       | )2,     |     |
| --- | ---- | ---------- | --------------- | ----------- | ------ | ------- | ----- | ------- | --- |
|     |      |            |                 |             |        |         |       | i j =k  |     |
|     | f    | (x,c,G,h)= |                 | j (cid:80)q | i= 1 i | j i     |       |         | (8) |
|     | xkxj |            |                 | µ G         | G /    | ( G⊤x   | −h )2 | , j ̸=k |     |
|     |      |            |                 | i=1 ij      | ik     | i       | i     |         |     |
and
(cid:26)
|     |     |            | µG  | x /(G⊤x−h | )2−µ/(G⊤x−h |     |     | ) r =j |     |
| --- | --- | ---------- | --- | --------- | ----------- | --- | --- | ------ | --- |
|     | f   | (x,c,G,h)= |     | ℓj j ℓ    | ℓ           |     | ℓ   | ℓ      |     |
Gℓrxj
|     |     |     | µG  | x /(G⊤x−h | )2  |     |     | r ̸=j |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | ----- | --- |
|     |     |     |     | ℓj r ℓ    | ℓ   |     |     |       |     |
Notethatwhentherearenoequalityconstraints,i.e.,A=0,wehave
∂x∗
|     |     |     |     | =−H−1f | (x,c,G,h) |     |     |     |     |
| --- | --- | --- | --- | ------ | --------- | --- | --- | --- | --- |
|     |     |     | ∂G  | Gx     |           |     |     |     |     |
whichisthesameastheLemma3in[12].
16

Proof. UsingtheLagrangianmultipliery,theLagrangianrelaxationofProblem(7)canbewrittenas
|     |     | L(x,y;c,G,h)=f(x,c,G,h)+y⊤(b−Ax) |     |     |     |     |     |     |     | (9) |
| --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| x∗  |     |                                  |     |     |     |     |     | x∗  |     |     |
Since = argmin f(x,c,G,h) s.t. Ax = b is an optimum, must obey the Karush-Kuhn-
x
Tucker(KKT)conditions,obtainedbysettingthepartialderivativeofEquation(9)withrespectto
xandyto0. Letf (x,c,G,h)denotesthevectoroffirstderivativesoff withrespecttodifferent
x
coordinatesofx,f (x,c,G,h)denotesthematrixofsecondderivativesoff withrespecttodifferent
xx
coordinatesofx,weobtain:
(x,c,G,h)−A⊤y
|     |     |     |     | f x |     |     | =0  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(10)
Ax−b=0
TheimplicitdifferentiationoftheseKKTconditionswithrespecttoGallowsustogetthefollowing
systemofequalities:
|     | (cid:20) |           |     | (cid:21) (cid:20) |           |     |     | (cid:21)(cid:20) | (cid:21) |      |
| --- | -------- | --------- | --- | ----------------- | --------- | --- | --- | ---------------- | -------- | ---- |
|     | f        | (x,c,G,h) |     | f                 | (x,c,G,h) |     | −A⊤ |                  | ∂x       |      |
|     | Gx       |           |     | +                 | xx        |     |     |                  | ∂G =0    | (11) |
|     |          | 0         |     |                   |           |     |     |                  | ∂y       |      |
|     |          |           |     |                   | A         |     | 0   |                  |          |      |
∂G
Bysolvingthissystemofequalities,wecanobtain
∂x∗
=(H−1A⊤(AH−1A⊤)−1AH−1−H−1)f
Gx (x,c,G,h)
∂G
| Sincef(x,c,G,h)=c⊤x−µ |     |     | (cid:80)d | ln(x )−µ | (cid:80)q | ln(G⊤x−h |     | ),wehave |     |     |
| --------------------- | --- | --- | --------- | -------- | --------- | -------- | --- | -------- | --- | --- |
|                       |     |     | i=1       | i        |           | i=1      | i   | i        |     |     |
(cid:80)q
|     | f (x,c,G,h)=c |     | −µx−1−µ  |             |          | G         | /(G⊤x−h |     | )      |      |
| --- | ------------- | --- | -------- | ----------- | -------- | --------- | ------- | --- | ------ | ---- |
|     | xj            |     | j        | j           |          | i =1 i j  | i       | i   |        |      |
|     |               |     | (cid:26) | −2+µ        | (cid:80) | q 2       | ⊤x−h    |     | )2,    |      |
|     |               |     |          | µx          |          | G         | /(G     |     | i j =k | (12) |
|     | f (x,c,G,h)=  |     |          | j (cid:80)q |          | i=1 ij    | i       |     |        |      |
|     | xkxj          |     |          | µ           | G        | G /(G⊤x−h |         | )2, | j ̸=k  |      |
|     |               |     |          |             | i=1      | ij ik     | i       | i   |        |      |
and
|     |     |     | (cid:26) | µG x | /(G⊤x−h | )2−µ/(G⊤x−h |     |     | ) r =j |     |
| --- | --- | --- | -------- | ---- | ------- | ----------- | --- | --- | ------ | --- |
|     |     |     |          | ℓj j | ℓ       | ℓ           |     | ℓ   | ℓ      |     |
f Gℓrxj (x,c,G,h)=
|     |     |     |     | µG x | /(G⊤x−h | )2  |     |     | r ̸=j |     |
| --- | --- | --- | --- | ---- | ------- | --- | --- | --- | ----- | --- |
|     |     |     |     | ℓj r | ℓ       | ℓ   |     |     |       |     |
LemmaB.3. ConsidertheLPrelaxation(7),definingx∗ asafunctionofc,A,b,Gandh. Then,
underthisdefinitionofx∗,
∂x∗
|           |                          | =(H−1A⊤(AH−1A⊤)−1AH−1−H−1)f |     |     |     |     |     | (x,c,G,h) |     |     |
| --------- | ------------------------ | --------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- |
|           | ∂h                       |                             |     |     |     |     |     | hx        |     |     |
| whereH =f | isdefinedasinLemmaB.2and |                             |     |     |     |     |     |           |     |     |
xx
|     |     | f   | (x,c,G,h)=−µG |     |     | /(G⊤x−h |     | )2  |     |     |
| --- | --- | --- | ------------- | --- | --- | ------- | --- | --- | --- | --- |
|     |     |     | hℓxj          |     |     | ℓj      | ℓ   | ℓ   |     |     |
Notethatwhentherearenoequalityconstraints,i.e.,A=0,wehave
∂x∗
|     |     |     |     | =−H−1f |     | (x,c,G,h) |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --------- | --- | --- | --- | --- |
hx
∂h
whichisthesameastheLemma2in[12].
Proof. AsstatedintheproofofLemmaB.2,usingtheLagrangianrelaxationandtheKarush-Kuhn-
Tucker(KKT)conditions,weobtain:
|     |     |     |     | f (x,c,G,h)−A⊤y |     |     | =0  |     |     |      |
| --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     | x               |     |     |     |     |     | (13) |
Ax−b=0
TheimplicitdifferentiationoftheseKKTconditionswithrespecttohallowsustogetthefollowing
systemofequalities:
|     | (cid:20) |           |     | (cid:21) (cid:20) |           |     | −A⊤ | (cid:21)(cid:20) | ∂x (cid:21) |      |
| --- | -------- | --------- | --- | ----------------- | --------- | --- | --- | ---------------- | ----------- | ---- |
|     | f hx     | (x,c,G,h) |     | f                 | (x,c,G,h) |     |     |                  |             |      |
|     |          |           |     | +                 | xx        |     |     |                  | ∂h =0       | (14) |
|     |          | 0         |     |                   | A         |     | 0   |                  | ∂y          |      |
∂h
Bysolvingthissystemofequalities,wecanobtain
∂x∗
|     |     | =(H−1A⊤(AH−1A⊤)−1AH−1−H−1)f |     |     |     |     |     | (x,c,G,h) |     |     |
| --- | --- | --------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- |
|     | ∂h  |                             |     |     |     |     |     | hx        |     |     |
17

(cid:80)d
where H = f is defined as in Lemma B.2. Since f(x,c,G,h) = c⊤x − µ ln(x ) −
|     |                | xx           |     |      |         |     |         |     |     | i=1 | i   |
| --- | -------------- | ------------ | --- | ---- | ------- | --- | ------- | --- | --- | --- | --- |
| µ   | (cid:80)q ln(G | x−h ),wehave |     |      |         |     |         |     |     |     |     |
|     | i=1 i          | i            |     |      |         |     |         |     |     |     |     |
|     |                |              |     | f    | (x)=−µG |     | /(G⊤x−h | )2  |     |     |     |
|     |                |              |     | hℓxj |         | ℓj  | ℓ       | ℓ   |     |     |     |
LemmaB.4. ConsidertheLPrelaxation(7),definingx∗ asafunctionofc,A,b,Gandh. Then,
underthisdefinitionofx∗,
∂x∗
|     |     |     | =H−1(−A⊤(AH−1A⊤)−1(I |     |     |     | x+AH−1I |     | y)+I y) |     |     |
| --- | --- | --- | -------------------- | --- | --- | --- | ------- | --- | ------- | --- | --- |
|     |     | ∂A  |                      |     |     |     | 2       |     | 1 1     |     |     |
ij
| whereI | =−∂A⊤,I |      | = ∂A | ,andH | =f  | isdefinedasinLemmaB.2. |     |     |     |     |     |
| ------ | ------- | ---- | ---- | ----- | --- | ---------------------- | --- | --- | --- | --- | --- |
|        | 1       |      | 2    |       | xx  |                        |     |     |     |     |     |
|        |         | ∂Aij | ∂Aij |       |     |                        |     |     |     |     |     |
Proof. AsstatedintheproofofLemmaB.2,usingtheLagrangianrelaxationandtheKarush-Kuhn-
Tucker(KKT)conditions,weobtain:
|     |     |     |     |     | f (x,c,G,h)−A⊤y |     |     | =0  |     |     |     |
| --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
x
(15)
Ax−b=0
|                          | A ∈ Rp×d, |          | i ∈   | {1,...,p},j                                     | ∈ {1,...,d}, |     |     |                  |                 |          |      |
| ------------------------ | --------- | -------- | ----- | ----------------------------------------------- | ------------ | --- | --- | ---------------- | --------------- | -------- | ---- |
| Since                    |           | fix      |       |                                                 |              |     | the | implicit         | differentiation | of these | KKT  |
| conditionswithrespecttoA |           |          |       | ij allowsustogetthefollowingsystemofequalities: |              |     |     |                  |                 |          |      |
|                          |           | (cid:34) | −∂A⊤y | (cid:35)                                        | (cid:20)     |     |     | (cid:21)(cid:34) | ∂x (cid:35)     |          |      |
|                          |           |          |       |                                                 | f (x,c,G,h)  |     | −A⊤ |                  |                 |          |      |
|                          |           |          | ∂Aij  | +                                               | xx           |     |     |                  | ∂Aij =0         |          | (16) |
|                          |           |          | ∂A    |                                                 |              | A   | 0   |                  | ∂y              |          |      |
x
|      |         |     | ∂Aij |                                               |     |     |     |     | ∂Aij |     |     |
| ---- | ------- | --- | ---- | --------------------------------------------- | --- | --- | --- | --- | ---- | --- | --- |
|      | =−∂A⊤,I |     | ∂A   |                                               |     |     |     |     |      |     |     |
| LetI | 1       | 2 = |      | . Bysolvingthissystemofequalities,wecanobtain |     |     |     |     |      |     |     |
|      | ∂Aij    |     | ∂Aij |                                               |     |     |     |     |      |     |     |
∂x∗
|     |     |     | =H−1(−A⊤(AH−1A⊤)−1(I |     |     |     | x+AH−1I |     | y)+I y) |     |     |
| --- | --- | --- | -------------------- | --- | --- | --- | ------- | --- | ------- | --- | --- |
|     |     | ∂A  |                      |     |     |     | 2       |     | 1 1     |     |     |
ij
| whereH | =f  | isdefinedasinLemmaB.2. |     |     |     |     |     |     |     |     |     |
| ------ | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
xx
LemmaB.5. ConsidertheLPrelaxation(7),definingx∗ asafunctionofc,A,b,Gandh. Then,
underthisdefinitionofx∗,
∂x∗
=H−1A⊤(AH−1A⊤)−1I
∂b
| whereH | =f xx | isdefinedasinLemmaB.2. |     |     |     |     |     |     |     |     |     |
| ------ | ----- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proof. AsstatedintheproofofLemmaB.2,usingtheLagrangianrelaxationandtheKarush-Kuhn-
Tucker(KKT)conditions,weobtain:
|     |     |     |     |     | f (x,c,G,h)−A⊤y |     |     | =0  |     |     |      |
| --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     | x               |     |     |     |     |     | (17) |
Ax−b=0
TheimplicitdifferentiationoftheseKKTconditionswithrespecttoballowsustogetthefollowing
systemofequalities:
|     |     |     | (cid:20) | (cid:21) | (cid:20)    |     |     | (cid:21)(cid:20) | (cid:21) |     |      |
| --- | --- | --- | -------- | -------- | ----------- | --- | --- | ---------------- | -------- | --- | ---- |
|     |     |     | 0        |          | f (x,c,G,h) |     | −A⊤ |                  | ∂x       |     |      |
|     |     |     |          | +        | xx          |     |     |                  | ∂b =0    |     | (18) |
|     |     |     | −I       |          | A           |     | 0   |                  | ∂y       |     |      |
∂b
Bysolvingthissystemofequalities,wecanobtain
∂x∗
=H−1A⊤(AH−1A⊤)−1I
∂b
| whereH | =f  | isdefinedasinLemmaB.2. |     |     |     |     |     |     |     |     |     |
| ------ | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
xx
18

C DetailsforCaseStudies
|     |     |     |     |     |     |     |                     |     | (cid:12)            | (cid:12) |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------------------- | -------- | --- |
|     |     |     |     |     |     |     | ∂PReg(θˆ,θ)(cid:12) |     | ∂PReg(θˆ,θ)(cid:12) |          | ∂x∗ |
Sincethepenaltyfunctionpartlyorsolelyaffectstheterms , ,and 2,
|     |     |     |     |     |     |     | ∂x∗ |     | (cid:12) | ∂x∗ (cid:12) | ∂x∗ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- |
|     |     |     |     |     |     |     |     | 2   | x∗       | 1 x∗         | 1   |
wegivethreecasestudiesforourframeworktoshowhowtodesignthepenaltyfunctionandcompute 1 2
gradientsusingthecorrespondingpenaltyfunction.
C.1 AlloyProductionProblem
Wefirstdemonstrate,usingtheexampleofthealloyproductionproblem,howourframeworkcan
tackle problems solvable by the prior work of Hu et al. [12]. An alloy production factory needs
to produce a certain amount of a particular alloy, requiring a mixture of M kinds of metals. To
| thatend,itmustacquireatleastreq |     |     |     | tonsofeachofthem |     |     | ∈   | [M]metals. |                    |     |     |
| ------------------------------- | --- | --- | --- | ---------------- | --- | --- | --- | ---------- | ------------------ | --- | --- |
|                                 |     |     |     | m                |     |     |     |            | Therawmaterialsare |     |     |
tobeobtainedfromK suppliers,eachsupplyingadifferenttypeofore. Thefactoryplanstobuy
oresfromsitesandthenextractthemetalsthemselves. Theoresuppliedbysitek ∈[K]containsa
con ∈[0,1]fractionofmaterialmatapriceofcost perton. Thegoalofthefactoryistomeet
| km  |     |     |     |     |     | k   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
itsrequirementsforeachmetalattheminimumcost. However, theprecisemetalconcentrations
(averagedinabatch)areunknownbeforethefactoryactuallycompletesmetalextraction. Thefactory
willestimatemetalconcentrationsbasedonhistoricalbuyingrecords,consideringfeaturessuchas
theoretype,oreorigin,site-reportedpreliminarysamplesandsoon. Thenthefactorywilldecide
howmuchoretoorderfromeachsite. ThisistheStage1solution. TheStage1OPisthealloy
productionproblemusingtheestimatedmetalconcentrationscoˆn,andcanbeformulatedasfollows:
|     |     | x∗  | =argmincost⊤x |     |     | s.t. coˆn⊤x≥req, |     | x≥0 |     |     |     |
| --- | --- | --- | ------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
1
x
Afterthefactoryobtainstheoresandcompletesmetalextraction,i.e.,inStage2,theprecisemetal
concentrations/amounts are known. Since the purchased ores are already processed, the factory
cannotreturnoresevenifithasboughttoomuch. However,iftheobtainedmetalsdonotsatisfy
therequirements,thefactorycanpost-hocdecidetolast-minuteordermoreoresatahigherprice,
forexample,(1+σ )cost pertonfromthesitek,whereσ ≥0isanon-negativetunablescalar
|            |                                      | k   | k      |                     |     |     | k   |     |     |     |      |
| ---------- | ------------------------------------ | --- | ------ | ------------------- | --- | --- | --- | --- | --- | --- | ---- |
| parameter. | Inthisscenario,thepenaltyfunctionis: |     |        |                     |     |     |     |     |     |     |      |
|            |                                      |     | Pen(x∗ | →x)=(σ◦cost)⊤(x−x∗) |     |     |     |     |     |     |      |
|            |                                      |     |        | 1                   |     |     |     | 1   |     |     | (19) |
where◦istheHadamard/entrywiseproduct.
Withrespecttotheabovepenaltyfunction,wearenowreadytodefinetheStage2OP:
|     | x∗ =argmincost⊤x+(σ◦cost)⊤(x−x∗) |     |     |     |     |     |      | con⊤x≥req, |     | x≥x∗ |      |
| --- | -------------------------------- | --- | --- | --- | --- | --- | ---- | ---------- | --- | ---- | ---- |
|     |                                  |     |     |     |     |     | s.t. |            |     |      | (20) |
|     | 2                                |     |     |     |     | 1   |      |            |     | 1    |      |
x
Notethatsincetheprecisemetalconcentrationsconarerevealed,thetrueconcentrationsareusedas
theproblemparametersinsteadoftheestimatedconcentrations. Thefinalamountoforesbought
fromeachsite,includingtheoresboughtinbothStage1andStage2,istheStage2solution.
The above formulation is based on the “soft commitment" modelling approach discussed in Ap-
pendixA.1.
Thepost-hocregretforthealloyproductionproblemcanbeexplicitlywrittenas:
|     | PReg(θˆ,θ)=cost⊤x∗+(σ◦cost)⊤(x∗−x∗)−cost⊤x∗(con) |     |     |     |     |     |     |     |     |     | (21) |
| --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |                                                  |     |     | 2   |     |     | 2 1 |     |     |     |      |
wherex∗(con)isanoptimalsolutionofthealloyproductionproblemunderthetrueconcentrations
con. WenowshowhowtocomputetherelevantgradientsasdiscussedinSection4andAppendixB.
|     |     |     |     |     |     |     |     |     |     | ∂PReg(θˆ,θ)(cid:12) | (cid:12) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | -------- |
UsingEquation(21),itisstraightforwardtocomputethatthei-thiteminvector and
|     |     |     |     |     |     |     |     |     |     | ∂x∗ | (cid:12) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- |
2 x∗
|                     |     |                     |     | (cid:18) |                     | (cid:19) |        |       | (cid:18) |                     | (cid:19)1 |
| ------------------- | --- | ------------------- | --- | -------- | ------------------- | -------- | ------ | ----- | -------- | ------------------- | --------- |
|                     |     | ∂PReg(θˆ,θ)(cid:12) |     | (cid:12) | ∂PReg(θˆ,θ)(cid:12) | (cid:12) |        |       |          | ∂PReg(θˆ,θ)(cid:12) | (cid:12)  |
| thei-thiteminvector |     |                     |     | :        |                     |          | = (1+σ | )cost | ,        |                     | =         |
|                     |     |                     | ∂x∗ | (cid:12) | ∂x∗                 | (cid:12) |        | i     | i        | ∂x∗                 | (cid:12)  |
|                     |     |                     | 1   | x∗       | 2                   | x∗       |        |       |          | 1                   | x∗        |
|                     |     |                     |     | 2        |                     | 1        | i      |       |          |                     | 2 i       |
−σ i cost i .
∂x∗
| Nowweshowhowtocomputetheapproximationoftheremainingterm, |     |     |     |     |     |     |     |     | 2.  |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∂x∗
1
19

Approximation
∂x∗
2. We use the same interior-point LP solver to help compute the relevant
∂x∗
1
derivatives. First, theestimatedparametersarefedintotheLPsolvertosolvetheStage1OPto
obtaintheStage1optimalsolutionx∗andthecorrespondingµ,whichareusedtocomputetheterm
1
∂x∗ 1. ThentheStage1optimalsolutionx∗andthetrueparametersarefedintotheLPsolvertosolve
∂θˆ 1
theStage2OPtoobtaintheStage2optimalsolutionx∗andthecorrespondingµ,whichareusedto
2
computetheterm
∂x∗
2. ConsidertheStage2OPinprogram(20). ItisclearthattheStage2OPisa
∂x∗
MILP,withx∗inthe 1 objectiveandx∗inhoftheconstraints. ApplyingLemmaB.3,wecancompute
2 1
anapproximategradientofthe
∂x∗
2 term.
∂x∗
1
C.2 Variantof0-1Knapsack
Thesecondexample,whichwecalltheproxybuyerproblem,isavariantofthe0-1knapsackproblem.
Theunknownparametersappearinboththeobjectiveandconstraints. Thisproblem,asweshallsee,
canbehandledbyourframework,butnotbythepriorapproachbyHuetal.[12],sincetheproblem
isinherentlydiscreteandcannotbeformulatedasLPs.
Aproxybuyerisapersonwhopurchasesgoodsforotherspossiblyforaprofit. Consideraproxy
buyerwhoisfromCityA,withaveryhighcostofliving,whoregularlytravelstoCityBwithamuch
lowercostofliving. Givenherregulartravels,herfriendsinCityAhaveaskedhertohelppurchase
everyday-lifeproducts,whicharesignificantlycheaperinCityB,yetthetimeandtransportation
cost from City A to City B makes it prohibitive for most people to just go to City B themselves.
ThetravellercommutesbetweenCityAandCityBonceeverythreemonths,andhasaknownand
limitedcapacitycapofgoodsshecouldcarryandbringback. Beforeeachtrip,herfriendswould
makerequestsforthingstobuy. Forsimplicity,onerequestcontainsoneitem. Ifthebuyerbrings
back the item as requested, her friends will pay her 20% of the price-tag p of each item i as a
i
courtesy-thankyou. Wedenotethis“profit”byf ,i.e.,f =20%p .
i i i
Thebuyerispopular, andmanyfriendsaskherforfavours. Onedaybeforethebuyerleavesfor
CityB,thebuyerneedstodecidewhichofherfriends’requeststoaccept,giventhelimitedcapacity,
andinformthemaccordingly. Thebuyerwantstomaximizethetotalamountofcourtesy-thankyou
moneyshegets,subjecttothehardconstraintofthelimitedsuitcasecapacitycap. However,the
precisepricep ofeachitemiisunknown,duetotheuncertaintyofthepriceitself,thevolatilityof
i
theexchangerate,andtheuncertaintyofthediscountactivitiesoftheitems. Thus,the“profit”f of
i
buyingitemiisunknown. Inaddition,theexactsizes ofeachitemiisalsoestimated. Thebuyer
i
willestimatetheprofit,i.e.,theprices,andthesizesbasedonpastexperiences,consideringfeatures
suchastime-of-year,holiday-or-not,brandandsoon. Thebuyerwilldecidewhichrequeststoaccept
basedontheestimation. ThisistheStage1solution. TheStage1OPistheproxybuyerproblem
usingtheestimatedsizessˆandestimatedprofitsfˆ:
x∗ =argmaxfˆ⊤x, s.t. sˆ⊤x≤cap, x∈{0,1}
1
x
AfterthebuyerarrivesatCityB,thebuyerknowstheprecisepriceandsizeofeachitem. Ifshe
cannotcarryalltheacceptedrequests,forexample,ifthepackagingforcertainitemshavechanged
sinceshelastboughtthem,thebuyerwillnecessarilyneedtodropsomeoftheserequests. Thebuyer
usuallyfeelsbadaboutrenegingonapromisetoherfriends,andtreatsherfriendstoamealasan
apologyiftherequestcannotbefulfilledaftershepromised. Forsimplicity,weassumethattheprice
oftheapology-mealislinearintheprofitofthedroppedrequest,sincemoreexpensiveitemsare
considered“moreimportant”requests. Here,thelinearityfactorisindependentoftherequest. That
is,ifshedropsitemi,shehastospendσf amountofmoney,whereσ ≥0isanon-negativetunable
i
scalarparameter. Inthisscenario,thepenaltyfunctionis:
Pen(x∗ →x)=σf⊤(x∗−x) (22)
1 1
WearenowreadytodefinetheStage2OPwithrespecttotheabovepenaltyfunction:
x∗ =argmaxf⊤x−σf⊤(x∗−x), s.t. s⊤x≤cap, x≤x∗, x∈{0,1} (23)
2 1 1
x
Therequeststhatwerefinallyfilled,namelytheitemsthatwereactuallyboughtbythebuyerand
broughthometoCityA,formstheStage2solution.
20

Thenthesimplifiedformofthepost-hocregretfortheproxybuyerproblemcanbewrittenas:
PReg(θˆ,θ)=f⊤x∗(f,s)−f⊤x∗+σf⊤(x∗−x∗)
(24)
|     |     |     |     |     |     | 2   | 1 2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
wherex∗(f,s)isanoptimalsolutionoftheproxybuyerproblemunderthetrueproxyfeesf
and
truesizess.
(cid:12)
UsingEquation(24),itisstraightforwardtocomputethatthei-thiteminvector ∂PReg(θˆ,θ)(cid:12) and
|                     |                     |     |          |                     |          |          |                     |     | ∂x∗ (cid:12) |
| ------------------- | ------------------- | --- | -------- | ------------------- | -------- | -------- | ------------------- | --- | ------------ |
|                     |                     |     |          |                     |          |          |                     |     | 2 x∗         |
|                     |                     |     | (cid:18) |                     |          | (cid:19) | (cid:18)            |     | (cid:19) 1   |
|                     | ∂PReg(θˆ,θ)(cid:12) |     | (cid:12) | ∂PReg(θˆ,θ)(cid:12) | (cid:12) |          | ∂PReg(θˆ,θ)(cid:12) |     | (cid:12)     |
| thei-thiteminvector |                     |     | :        |                     |          | =(−1−σ)f | ,                   |     | =σf .        |
|                     |                     | ∂x∗ | (cid:12) | ∂x∗                 | (cid:12) |          | i                   | ∂x∗ | (cid:12) i   |
|                     |                     | 1   | x∗       |                     | 2 x∗     |          |                     | 1   | x∗           |
|                     |                     |     | 2        |                     |          | 1 i      |                     |     | 2 i          |
∂x∗
Approximation 2. SimilartothecomputationinSectionC.1,weobtaintheStage1optimal
∂x∗
1
solutionx∗, theSta ge2optimalsolutionx∗, andthecorrespondingµfromtheinterior-pointLP
1 2
∂x∗
computetheterm 2. ConsidertheStage2OPinprogram(23),itisclearthattheStage2OPisa
∂x∗
MILP,withx∗inthe 1 objectiveandx∗inhoftheconstraints. ApplyingLemmaB.3,wecancompute
| 2   |     |     | 1   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∂x∗
| anapproximategradientofthe |     |     | 2 term. |     |     |     |     |     |     |
| -------------------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
∂x∗
1
C.3 NurseSchedulingProblem
Ourlastexampleisthenurseschedulingproblem(NSP),whichcanbehandledbyourframework
butnotbythepriorworkofHuetal.[12]sinceitisneitherapackingLPnoracoveringLP.
Consider a large optometry center that needs to assign nurses to shifts per day to meet patients’
needs. Every Monday morning, the center collects the nurses’ preferences for each shift of the
followingweek. Sincenursesmayhavetheirownactivitiesanderrandsduringunscheduledshifts,
theywanttobeinformedoftheirschedulesasearlyaspossible. Afterthepreferencesarecollected,
onMondaynight,thecentersetsapreliminaryshiftschedulefortheupcomingweekbasedonthe
estimatednumberofpatientsforeachshift. Supposetherearennurses,kdays,andsshiftsperday,
thenthenumberofthetotalshiftsist=k×s. WeformulatethedecisionvariablesasaBoolean
vectorx∈{0,1}d,whered=n×k×s. ∈{1,2,3,4}drepresentthevalueofeachnurse’s
LetP
Nt
preferences for a particular shift (the higher the number the better), and H ∈ represents the
numberofpatientsineachshift, whichareunknownandneedtobepredicted. Eachnurseican
servem patientsinoneshift. Theobjectiveistomaximizethenurses’preferencesunderasetof
i
constraints: (1)theschedulemustsatisfythepatientdemand,undereachshift(2)eachnursemustbe
scheduledforexactlyoneshifteachday(3)nonursemaybescheduledtoworkanightshiftfollowed
immediatelybyamorningshift. TheStage1OPistheNSPusingtheestimatednumberofpatients
Hˆ:
x∗ =argmaxP⊤x
1
x
n−1 (cid:88)
≥Hˆ
|     | s.t. |     | m i x it+j |     | j ∀j | ∈{0,...,t−1} |     |     |     |
| --- | ---- | --- | ---------- | --- | ---- | ------------ | --- | --- | --- |
i=0
s−1
|     |     | (cid:88) |           |     | ∀i={0,...,n−1}, |                |     |     |     |
| --- | --- | -------- | --------- | --- | --------------- | -------------- | --- | --- | --- |
|     |     |          | x it+sj+q | =1  |                 |                |     |     |     |
|     |     |          |           |     |                 | j ={0,...,k−1} |     |     |     |
q=0
∀i={0,...,n−1},
|     |     | x         |     | +x      |     | ≤1             |     |     |     |
| --- | --- | --------- | --- | ------- | --- | -------------- | --- | --- | --- |
|     |     | it+sj+s−1 |     | it+sj+s |     | j ={0,...,k−2} |     |     |     |
x∈{0,1}
Toprovidebetterservicetopatients,theoptometrycenterhasimplementedanappointmentsystem
thatrequirespatientstoscheduleanappointmentinadvancetoreceivemedicalcare. Reservationsfor
theupcomingweek,fromMondaytoSunday,closeeverySundayevening. Atthispoint,thecenter
knowstheprecisenumberofpatientsforeachshiftofthenextweek. Thecentermightadjusttheshift
scheduletosatisfytheactualpatientdemandortoimprovetheoverallnursepreferences. However,
duetothelatenoticeforschedulechanges,thenurse’spreferencemaybecomelower. Forexample,
ifanurseisrescheduledtoashiftforwhichheroriginalpreferenceis5,nowherpreferenceforthis
shiftmaybecome4duetothelatenotice. Besides,anursemaybemoreunhappytobechangedto
21

alow-preferenceshift. Inthisscenario,sincethenurses’preferencesarein{1,2,3,4},thepenalty
functioncanbeformulatedas:
d−1
(cid:88)
|     |     | Pen(x∗ →x)= |     | Pen(x∗ | →x) |     | (25) |
| --- | --- | ----------- | --- | ------ | --- | --- | ---- |
|     |     | 1           |     | 1      | i   |     |      |
i=0
wherethei-thiteminthepenaltyfunctionis:
(cid:26)
|     |        |       | γ (5−P | )2(x −x∗ | ) x | ≥x∗  |     |
| --- | ------ | ----- | ------ | -------- | --- | ---- | --- |
|     | Pen(x∗ | →x) = | i      | i i      | 1i  | i 1i |     |
|     | 1      | i     |        |          |     | <x∗  |     |
|     |        |       | 0      |          | x   | i    |     |
1i
WearenowreadytodefinetheStage2OPwithrespecttotheabovepenaltyfunction:
(cid:88) d−1
| x∗ =argmaxP⊤x− |     |     | Pen(x∗ |       |     |     |     |
| -------------- | --- | --- | ------ | ----- | --- | --- | --- |
|                |     |     |        | →x) i |     |     |     |
| 2              |     |     |        | 1     |     |     |     |
|                | x   |     | i=0    |       |     |     |     |
n−1
(cid:88)
|     |      | m x    | ≥H  | ∀j ∈{0,...,t−1} |     |     |     |
| --- | ---- | ------ | --- | --------------- | --- | --- | --- |
|     | s.t. | i it+j | j   |                 |     |     |     |
i=0
s−1
|     | (cid:88) |         |     | ∀i={0,...,n−1}, |     |     |     |
| --- | -------- | ------- | --- | --------------- | --- | --- | --- |
|     |          | x       | =1  |                 |     |     |     |
|     |          | it+sj+q |     | j ={0,...,k−1}  |     |     |     |
q=0
∀i={0,...,n−1},
|     | x it+sj+s−1 |     | +x it+sj+s | ≤1  |     |     |     |
| --- | ----------- | --- | ---------- | --- | --- | --- | --- |
j ={0,...,k−2}
x∈{0,1}
Thenthesimplifiedformofthepost-hocregretfortheNSPcanbewrittenas:
d−1
| PReg(θˆ,θ)=P⊤x∗(H)−P⊤x∗+ |     |     |     | (cid:88) | Pen(x∗ | →x∗) |      |
| ------------------------ | --- | --- | --- | -------- | ------ | ---- | ---- |
|                          |     |     |     |          |        | i    | (26) |
|                          |     |     |     | 2        |        | 1 2  |      |
i=0
(cid:12)
∂PReg(θˆ,θ)(cid:12)
UsingEquation(26),itisstraightforwardtocomputethatthei-thiteminvector and
∂x∗ (cid:12)
2 x∗
|     | ∂PReg(θˆ,θ)(cid:12) | (cid:12) |     |     |     |     | 1   |
| --- | ------------------- | -------- | --- | --- | --- | --- | --- |
thei-thiteminvector :
|     | ∂x∗ | (cid:12) |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- |
|     | 1   | x∗       |     |     |     |     |     |
2
|    |     |    |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
(cid:12)
|     | ∂PReg(θˆ,θ)(cid:12) |             | (cid:26) −P | +2γ (5−P | )   | x∗ ≥x∗   |     |
| --- | ------------------- | ----------- | ----------- | -------- | --- | -------- | --- |
|     |                     | (cid:12)    |             | i i      | i   | 2 i 1 i  |     |
|    |                     | (cid:12)   | =           |          |     |          |     |
|     | ∂x∗                 |             | −P          |          |     | x ∗ <x ∗ |     |
|     | 2                   | (cid:12) x∗ |             | i        |     | 2i 1i    |     |
1 i
|     |                    | (cid:12)   |    |            |     |       |     |
| --- | ------------------- | ---------- | --- | ---------- | --- | ----- | --- |
|     | ∂PReg(θˆ,θ)(cid:12) |            |     | (cid:26)   | x∗  | ≥x∗   |     |
|     |                     |            |     | −2γ i (5−P | i ) |       |     |
|     |                    | (cid:12)   |  = |            | 2   | i 1 i |     |
|     | ∂x∗                 | (cid:12)   |     | 0          | x ∗ | <x ∗  |     |
|     |                     | 1 (cid:12) |     |            | 2i  | 1i    |     |
x∗
2 i
∂x∗
Approximation 2. SimilartothecomputationinSectionC.1,weobtaintheStage1optimal
∂x∗
solutionx∗, 1 ge2optimalsolutionx∗, andthecorrespondingµfromtheinterior-pointLP
| 1 theSta |     |     | 2   |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- |
∂x∗
computetheterm 2. UsingthepenaltyfunctioninEquation(25),theStage2OPcanbeformulated
∂x∗
1
22

asaMILPbyaddingnewvariablesσandonemoreconstraint:
d−1
(cid:88)
| x∗ =argmaxP⊤x− |     | γ (5−P | )2σ |     |
| -------------- | --- | ------ | --- | --- |
| 2              |     | i      | i i |     |
|                | x   | i=0    |     |     |
n−1
(cid:88)
|     | s.t. m x | ≥H ∀j  | ∈{0,...,t−1} |     |
| --- | -------- | ------ | ------------ | --- |
|     | i        | it+j j |              |     |
i=0
s−1
|     | (cid:88) | ∀i={0,...,n−1}, |                |     |
| --- | -------- | --------------- | -------------- | --- |
|     | x        | =1              |                |     |
|     | it+sj+q  |                 | j ={0,...,k−1} |     |
q=0
∀i={0,...,n−1},
|     | x it+sj+s−1 | +x it+sj+s | ≤1  |     |
| --- | ----------- | ---------- | --- | --- |
j ={0,...,k−2}
−x∗
|     | σ i ≥x i | ∀i={0,...,d−1} |     |     |
| --- | -------- | -------------- | --- | --- |
1i
x∈{0,1}
σ ∈{0,1}
SupposetheStage2OPoftheNSPcanbewrittenas:
x∗ =argmin−P⊤x+(γ◦(5−P)2)⊤σ
2
x
|     | s.t. | G 1 x≥H |     |     |
| --- | ---- | ------- | --- | --- |
Ax=b
G x≥−1
2
σ−x≥−x∗
1
x,σ ∈{0,1}
ThenthestandardformoftheStage2OPis:
x′ =argminc⊤x′
2
x′
A′x′
|     |     | s.t. | =b  |     |
| --- | --- | ---- | --- | --- |
Gx≥h
|     |     | x′  | ∈{0,1} |     |
| --- | --- | --- | ------ | --- |
where
| (cid:2)    | γ◦(5−P)2(cid:3) | ∈R2d, | σ]∈R2d     |          |
| ---------- | --------------- | ----- | ---------- | -------- |
| c = −P     |                 |       | x′ =[x     |          |
| (cid:34) G | 0 (cid:35)      |       | (cid:34) H | (cid:35) |
1
| G = G | 0 ∈R(t+nk−n+d)×2d, |     | h = −1 | ∈Rt+nk−n+d |
| ----- | ------------------ | --- | ------ | ---------- |
2
| −I  | I   |     | −x∗ |     |
| --- | --- | --- | --- | --- |
1
]∈Rnk×2d
| A′ =[ A | 0   |     |     |     |
| ------- | --- | --- | --- | --- |
andb∈Rnk isanall-onesvector.
Itisclearthatx∗isintheobjectiveandx∗isinhoftheconstraints. ApplyingLemmaB.3,wecan
| 2   |     | 1   |     |     |
| --- | --- | --- | --- | --- |
∂x∗
computeanapproximategradientofthe 2 term.
∂x∗
1
23

D HyperparametersfortheExperiments
Themethodsofk-NN,RF,NN,andIntOpt-Caswellas2Shavehyperparameters,whichwetune
viacross-validation: fork-NN,wetryk ∈{1,3,5};forRF,wetrydifferentnumbersoftreesinthe
forest{10,50,100};forNN,IntOpt-C,and2S,wetreatthelearningrate,epochsandweightdecay
ashyperparameters.
Tables7,8,and9showthefinalhyperparameterchoicesforthethreeproblems:1)analloyproduction
problem,2)theclassic0-1knapsackproblem,and3)anurserosterschedulingproblem.
Table7: Hyperparametersoftheexperimentsonthealloyproductionproblem.
Model Hyperparameters
Proposed optimizer:optim.Adam;learningrate:5×10−7;µ=10−3;epochs=20
k-NN k=5
RF n_estimator=100
NN optimizer:optim.Adam;learningrate:10−3;epochs=20
Table8: Hyperparametersoftheexperimentsonthe0-1knapsackproblem.
Model Hyperparameters
Proposed optimizer:optim.Adam;learningrate:10−7;µ=10−3;epochs=12
k-NN k=5
RF n_estimator=100
NN optimizer:optim.Adam;learningrate:10−3;epochs=12
Table9: Hyperparametersoftheexperimentsonthenurseschedulingproblem.
Model Hyperparameters
Proposed optimizer:optim.Adam;learningrate:10−1;µ=10−3;epochs=8
k-NN k=5
RF n_estimator=100
NN optimizer:optim.Adam;learningrate:10−2;epochs=8
Ridge, k-NN, CART and RF are implemented using scikit-learn [24]. The neural network is
implementedusingPyTorch[22]. Tocomputethetwostagesofoptimizationattesttimeforour
method,andtocomputetheoptimalsolutionofan(MI)LPunderthetrueparameters,weusethe
MILPsolverfromGurobi[11].
E Comparisonsofthe2SMethodandthePriorDifferentiationMethods
Inthissection,wecomparetheproposedmethodwithpriorworks[1,2,27]thatprovidewaysof
differentiatingthroughLPsorLPswithregularization. WeconductcomparisonswithCvxpyLayer
[1]butnotOptNet[2]orQPTL[27]. ThereasonisthatthecalculationmethodproposedinQPTLis
LP+quadraticregularizationusingOptNet,andCvxpyLayerisjustaconicextensiontoOptNet. We
comparedCvxpyLayer[1]witha)noregularization,b)quadraticregularizationandc)log-barrier
(like our Section 4/Appendix B). The key indicator of its predictive performance is the type of
regularizationused,withthelog-barrierversionperformingthebest,butstillslightlyworsethanour
method. WeappliedCvxpyLayer[1]tothe0-1knapsackbenchmarktocomparewithour2Smethod.
Table 10 reports the mean post-hoc regrets and standard deviations across 10 runs and Table 11
reportstheaveragetrainingtimes. Moreprecisely,weuseitwithvariousregularizations(a. LPwith
noregularization,b. withquadraticregularization,c. withlog-barrierasinourpaper)toreplacethe
Section4/AppendixBgradientcalculations. WefindthatCvxpyLayer[1]nevergivesbettersolution
qualitywhile2Sis30%–50%faster.
24

Table10: Meanpost-hocregretsandstandarddeviationsofthe2SmethodandCvxpyLayerwith
differentregularizationonthe0-1knapsackproblem.
Penalty
| PReg    | factor |           | 2S  | CvxpyLayer+log | CvxpyLayer+quad_reg |     | CvxpyLayer+no_reg |     |
| ------- | ------ | --------- | --- | -------------- | ------------------- | --- | ----------------- | --- |
|         | 0.05   | 1.26±0.01 |     | 1.26±0.01      | 1.27±0.01           |     | 7.70±0.39         |     |
| cap=100 | 0.25   | 6.28±0.05 |     | 6.28±0.05      | 6.34±0.03           |     | 8.87±0.92         |     |
|         | 0.5    | 9.22±0.10 |     | 9.47±0.31      | 9.96±0.54           |     | 10.13±0.46        |     |
|         | 0.05   | 0.73±0.01 |     | 0.74±0.01      | 0.75±0.03           |     | 6.74±0.58         |     |
| cap=150 | 0.25   | 3.64±0.04 |     | 3.64±0.04      | 3.70±0.03           |     | 7.18±0.77         |     |
|         | 0.5    | 7.27±0.06 |     | 7.28±0.08      | 7.39±0.06           |     | 8.43±0.58         |     |
Table11:Averageruntime(inseconds)ofthe2SmethodandCvxpyLayerwithdifferentregularization
onthe0-1knapsackproblem.
| Runtime |     | 2S     | CvxpyLayer+log | CvxpyLayer+quad_reg |        | CvxpyLayer+no_reg |        |     |
| ------- | --- | ------ | -------------- | ------------------- | ------ | ----------------- | ------ | --- |
| cap=100 |     | 204.76 | 438.24         |                     | 571.38 |                   | 344.50 |     |
| cap=150 |     | 245.61 | 467.65         |                     | 662.30 |                   | 366.83 |     |
F FrameworksComparisonsontheAlloyProductionProblem
Inthissection,wefurthercomparedtheproposedframeworkwiththeframeworkusingthediffer-
entiableprojectionideain[3]onthealloyproductionbenchmark. Theideain[3]istousethel
2
projection,andweimplementeditusingCvxpyLayer. Theexperimentset-upfollowsthatofTable2:
bothtrainingandtestingusel projectioninthesecondstage,asopposedtosolvingthesecondstage
2
optimizationproblemdefinedinSection3. Table12showsboththepost-hocregretandtrainingtime
forl 2 projection. Wefindthatnotonlyisl 2 projectionslow,butithasevenworsepost-hocregret
thantheHuetal. correction[12]. WesuspectthatthisisduetotheHuetal. correctionfunction
[12]preservingthedirectionofthesolutionvectorwhereasl projectioncanchangethedirection,
2
andthatthismakesadifferenceforAlloyProduction. Inanycase,thisexperimentconfirmsagain
thatourTwo-Stageframeworkhasbetterpost-hocregretthanaframeworkbasedondifferentiable
projections,reinforcingthemainmessageofourpaper.
Table12: Comparisonofthreeframeworksonthealloyproductionproblem.
|     |     |     |     |     | PReg |     |     | Average |
| --- | --- | --- | --- | --- | ---- | --- | --- | ------- |
Penaltyfactor 0.25±0.015 0.5±0.015 1±0.015 2±0.015 4±0.015 8±0.015 runtime
Two-StagePredict+
|     | 43.87±2.73 | 65.71±4.81 |     | 88.75±5.91 | 123.90±6.84 | 161.86±8.49 | 194.06±13.09 | 268.22 |
| --- | ---------- | ---------- | --- | ---------- | ----------- | ----------- | ------------ | ------ |
OptimizeFramework
Huetal.Framework 68.16±6.26 82.91±5.45 107.64±6.85 150.47±12.99 178.69±10.09 206.84±12.51 228.00
l2_projection 103.28±4.87 118.90±6.99 150.15±11.45 212.62±20.58 337.59±23.24 562.41±34.29 442.97
G Experimentsonthe0-1KnapsackProblemwithLargePenaltyFactors
Table13reportsthemeanpost-hocregretsandstandarddeviationsacross10runsforeachapproach
onthe0-1knapsackproblemwithlargepenaltyfactors(penaltyfactors≥1). Withmoredata,we
canmakefurtheranalysisoftheperformanceoftheproposed2Smethod. ObservingTables4and13,
wecanseethatthetrend,intermsofthedifferencebetween2Sandothermethods,firstdecreases,
thenincreases,asthepenaltyfactorincreases. ThetrendinTables4and13isidenticaltothetrendin
Table3. Wecanexplainthisphenomenonasfollows.
First,whenthepenaltyfactorissmall,therationalbehaviorforthebuyeristojusttakeeveryorder,
andonlydecidewhichorderstodropwhenthetrueparametersarerevealed(atclosetonocost). 2S
identifiesandexploitsthisbehaviorforsmallpenalties,whileclassicregressionmethodsareagnostic
tothispossibletactic. Thus,theadvantageof2Scomparedtoclassicregressionmethodsislargein
thesmallpenaltycase.
Second,whenthepenaltyfactorislarge,2Swillanalogouslylearntobeconservative,suchthatthe
firststagesolutionlikelyremainsfeasibleunderthetrueparameters,inordertoavoidthenecessary
(andhigh)penaltyduetohavingtochangetoafeasiblesolution. Again,classicregressionmethods
willbeagnostictothispossibletactic,leadingtoalargeadvantageof2Sovertheclassicmethods.
25

Table 5 only has the increasing trend from the large penalty, since it is neither a covering nor a
packingprogram,andsothereisnoanalogoustactic/exploitationforthesmallpenalty.
Table13: Meanpost-hocregretsandstandarddeviationsfor0-1knapsackproblemwithlargepenalty
factorsusingtheTwo-StagePredict+Optimizeframework.
Penalty
PReg 2S CombOptNet Ridge k-NN CART RF NN TOV
factor
1 10.90±0.15 10.93±0.17 10.93±0.19 11.11±0.17 11.16±0.14 11.01±0.31 11.26±0.23
cap=100 2 12.31±0.16 12.45±0.25 12.48±0.20 12.49±0.21 13.77±0.26 12.60±0.39 12.78±0.30 29.68±0.14
4 14.54±0.15 15.66±0.47 15.57±0.25 15.68±0.39 19.01±0.56 15.77±0.62 15.84±0.50
1 10.23±0.12 10.22±0.18 10.46±0.23 10.40±0.18 10.46±0.19 10.49±0.21 10.86±0.30
cap=150 2 11.18±0.15 11.74±0.34 11.88±0.30 11.63±0.20 12.56±0.31 11.83±0.19 12.12±0.17 40.23±0.19
4 13.20±0.16 14.33±0.46 14.71±0.49 14.43±0.33 16.75±0.63 14.53±0.29 14.65±0.41
1 6.77±0.36 15.30±0.28 7.67±0.18 7.51±0.27 7.71±0.20 7.67±0.16 8.00±0.65
cap=200 2 8.19±0.12 15.39±0.16 8.84±0.22 8.69±0.26 9.24±0.30 8.80±0.20 8.97±0.37 48.13±0.24
4 9.71±0.35 15.46±0.22 11.17±0.40 11.06±0.32 12.29±0.59 11.05±0.46 10.91±0.53
1 1.37±0.08 20.69±0.20 3.08±0.19 2.94±0.16 3.17±0.17 3.05±0.25 3.28±0.96
cap=250 2 3.34±0.15 20.78±0.20 3.80±0.20 3.73±0.15 3.94±0.20 3.79±0.26 3.89±0.58 53.43±0.26
4 4.46±0.09 20.93±0.20 5.25±0.35 5.32±0.27 5.47±0.35 5.29±0.48 5.11±0.39
H RuntimesfortheExperiments
Inthispaper,allmodelsaretrainedwithIntel(R)Xeon(R)CPUE5-2630v2@2.60GHzprocessors.
Table14showstheaverageruntimeacross10simulationsfordifferentoptimizationproblems. Since
thetestingtimeofdifferentapproachesisquitesimilar,here,theruntimereferstoonlythetraining
timeofthepredictionmodelanddoesnotincludethetestingtime.Attrainingtime,onlytheproposed
2SmethodandIntOpt-CsolvetheLP.TrainingfortheusualNNdoesnotinvolvetheLPatall,and
sotrainingismuchfaster(butgivesworseresults).
SinceIntOpt-Ccannothandlethevariantofthe0-1knapsackproblemandtheNSP,weonlyreport
theruntimeofIntOpt-Cforthealloyproductionproblem.
SincetheprovidedcodeofCombOptNetisonlyavailableforthe0-1knapsackproblem,weonly
reporttheruntimeofCombOptNetforthe0-1knapsackproblem. AsTable14shows,CombOptNet
isdrasticallyslowerthantheproposed2Smethod.
Inthealloyproductionproblem,theruntimesoftheproposed2Smethodarealittlelargerthanthat
ofIntOpt-C.Thereasonisthat2SneedstosolvetwoLPswhentrainingwhileIntOpt-Conlyneeds
tosolveone. Butinthealloyproductionproblem,theunknownparametersareonthelefthandside
oftheinequalityconstraintsandthegradientcomputationincludesmatrixcomputation,whichisalso
time-consuming. Thus,theruntimesofthe2Smethodarelargerbutnottwiceaslargeasthatofthe
IntOpt-Cmethod.
Inboththealloyproductionproblemandthevariantofthe0-1knapsackproblem,theruntimesofthe
2SmethodaremuchbetterthanRF.
Theruntimeofthe2SmethodislargeintheNSP.Thisisbecauseweusetheformulationwhereeach
decisionvariablecorrespondstowhetheraspecificnurseisassignedtoaspecificdayandaspecific
shift. Thus,thenumberofthedecisionvariableoftherelaxedLPislargeandtheLPtakesmoretime
tosolve.
Table14: Averageruntime(inseconds)forthealloyproduction,0-1knapsack,andnursescheduling
problems.
Alloyproduction 0-1knapsack
Runtime(s) Nursescheduling
Brass Titanium-alloy Capacity=100 Capacity=150 Capacity=200 Capacity=250
2S 268.22 394.53 204.76 245.61 202.65 193.46 537.32
IntOpt-C 228.00 331.38 N\A
CompOptNet N\A 2341.40 2940.26 2394.05 2383.39 N\A
Ridge 20.22 56.89 22.33 <1
k-NN 25.14 70.22 26.00 <1
CART 30.33 94.89 34.83 <1
RF 959.50 2552.25 1034.07 2.11
NN 212.22 321.11 135.80 11.39
26