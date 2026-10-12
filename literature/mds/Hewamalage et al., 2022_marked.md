---
conversion_metadata:
  converted_at: "2026-10-11T15:10:37Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Hewamalage et al., 2022.pdf"
  source_pdf_sha256: "8d138cafe41a7d0ee656e62bf4d80372eabd90af4cce3889f9a55ccae4f7b92a"
  page_count: 45
  markdown_char_count: 112937
---

DataMiningandKnowledgeDiscovery(2023)37:788–832
https://doi.org/10.1007/s10618-022-00894-5
Forecastevaluationfordatascientists:commonpitfallsand
bestpractices
Hansika Hewamalage1·Klaus Ackermann2·Christoph Bergmeir3
Received:4April2022/Accepted:7November2022/Publishedonline:2December2022
©TheAuthor(s)2022
Abstract
RecenttrendsintheMachineLearning(ML)andinparticularDeepLearning(DL)
domains have demonstrated that with the availability of massive amounts of time
series, ML and DL techniques are competitive in time series forecasting. Neverthe-
less, the different forms of non-stationarities associated with time series challenge
the capabilities of data-driven ML models. Furthermore, due to the domain of fore-
casting being fostered mainly by statisticians and econometricians over the years,
theconceptsrelatedtoforecastevaluationarenotthemainstreamknowledgeamong
MLresearchers.Wedemonstrateinourworkthatasaconsequence,MLresearchers
oftentimes adopt flawed evaluation practices which results in spurious conclusions
suggesting methods that are not competitive in reality to be seemingly competitive.
Therefore,inthisworkweprovideatutorial-likecompilationofthedetailsassociated
with forecast evaluation. This way, we intend to impart the information associated
withforecastevaluationtofitthecontextofML,asmeansofbridgingtheknowledge
gapbetweentraditionalmethodsofforecastingandadoptingcurrentstate-of-the-art
MLtechniques.Weelaboratethedetailsofthedifferentproblematiccharacteristicsof
timeseriessuchasnon-normalityandnon-stationaritiesandhowtheyareassociated
withcommonpitfallsinforecastevaluation.Bestpracticesinforecastevaluationare
outlinedwithrespecttothedifferentstepssuchasdatapartitioning,errorcalculation,
Responsibleeditor:EamonnKeogh
B
ChristophBergmeir
Christoph.Bergmeir@monash.edu
HansikaHewamalage
h.hewamalage@unsw.edu.au
KlausAckermann
Klaus.Ackermann@monash.edu
1 SchoolofComputerScience&Engineering,UniversityofNewSouthWales,Sydney,Australia
2 SoDaLabsandDepartmentofEconometrics&BusinessStatistics,MonashBusinessSchool,
MonashUniversity,Melbourne,Australia
3 DepartmentofDataScienceandAI,FacultyofIT,MonashUniversity,Melbourne,Australia
123

Forecastevaluationfor... 789
statisticaltesting,andothers.Furtherguidelinesarealsoprovidedalongselectingvalid
andsuitableerrormeasuresdependingonthespecificcharacteristicsofthedatasetat
hand.
Keywords Timeseriesforecasting·Forecastevaluation
1 Introduction
In the present era of Big Data, Machine Learning (ML) and Deep Learning (DL)
based techniques are driving the automatic decision making in many domains such
asNaturalLanguageProcessing(NLP)orTimeSeriesClassification(TSC,Bagnall
et al. 2016; Fawaz et al. 2019). Although fields such as NLP and Computer Vision
haveheavilybeendominatedbyMLandDLbasedtechniquesfordecadesbynow,this
hashardlybeenthecaseforthefieldofforecasting,untilveryrecently.Forecasting
wastraditionallythefieldofstatisticiansandeconometricians.However,withmassive
scales of data being collected nowadays, ML and DL has now emerged as the state
oftheartformanyforecastingtasks.Furthermore,withmanycompanieshiringdata
scientists, often these data scientists are tasked with forecasting. Therefore, now in
manysituationspractitionerstaskedwithforecastinghaveagoodbackgroundinML
anddatascience,butarelessawareofthedecadesofresearchintheforecastingspace.
Thisinvolvesmanyaspectsoftheprocessofforecasting,fromthepointofdatapre-
processing, building models to final forecast evaluation. Due to the self-supervised
andsequentialnatureofforecastingtasks,itisoftenassociatedwithmanypitfallsthat
usualMLpractitionersarenotawareof.Theusageofbadevaluationpracticesworsens
thisproblemsincetheyarenotclearlydistinguishingthetrulycompetitivemethods
from the inferior ones by avoiding spurious results. Evaluating the performance of
modelsiskeytothedevelopmentofconceptsandpracticesinanydomain.Hence,in
thisparticularwork,wefocusontheevaluationofpointforecastsasakeystepinthe
overallprocessofforecasting.
Thegeneralprocessofforecastevaluationinvolvesemployinganumberofmodels
havingdifferentcharacteristics,trainingthemonatrainingdatasetandthenapplying
themonavalidationsetafterwards.Then,modelselectionmaybeperformedbyeval-
uating on the validation set to select the best models. Otherwise, ensemble models
maybedevelopedinstead,bycombiningtheforecastsfromallthedifferentmodels,
andusuallyafinalevaluationisthenperformedonatestset(Godahewaetal.2021).
Inresearchareassuchasclassificationandregression,therearewell-establishedstan-
dardpracticesforevaluation.Datapartitioningisperformedbyusingastandardk-fold
Cross-Validation(CV)totunethemodelhyperparametersbasedontheerroronavali-
dationset,themodelwiththebesthyperparametercombinationistestedonthetesting
set,standarderrormeasuressuchassquarederrors,absoluteerrorsorprecision,recall,
orareaunderthecurvearecomputedandfinallythebestmodelsareselected.These
best methods may continue to deliver reasonable predictions for a certain problem
task,i.e.,theygeneralizewell,undertheassumptionthattherearenochangesofthe
distribution of the underlying data, which otherwise would need to be addressed as
123

790 H.Hewamalageetal.
conceptdrift(Webbetal.2016;Ghomeshietal.2019;Ikonomovskaetal.2010)or
non-stationarity.
Incontrast,evaluatingforecastingmodelscanbeasurprisinglycomplicatedtask,
alreadyforpointforecasting.Datapartitioninghasmanydifferentoptionsinthecon-
text of forecasting, including fixed origin, rolling origin evaluation and other CV
setupsaswellascontroversialargumentsassociatedwiththem.Duetotheinherent
dependency,non-stationarityandnon-normalityoftimeseries,thesechoicesarecom-
plex.Also,mosterrormeasuresaresusceptibletobreakdownundercertainofthese
conditions.Otherconsiderationsarewhethertosummarizeerrorsacrossallavailable
time series or consider different steps of the forecast horizon separately etc. As a
consequence,weregularlycomeacrosspapersintopArtificialIntelligence(AI)/ML
conferences and journals (even winning best paper awards) that use inadequate and
misleadingbenchmarkmethodsforcomparison(e.g.,non-seasonalmodelsforlong-
termforecastingonseasonalseries),othersthatusemeanabsolutepercentage error
(MAPE)forevaluationwithseries,e.g.,withvaluesinthe[−1, 1]intervalbecause
theauthorsthinktheMAPEisasomewhatgeneric“timeserieserrormeasure”,even
though MAPE is clearly inadequate in such settings. Other works make statements
alongthelinesofAuto-RegressiveIntegratedMovingAverage(ARIMA)beingable
to tackle non-stationarity whereas ML models can’t, neglecting that the only thing
ARIMAdoesisadifferencingoftheseriesasapre-processingsteptoaddressnon-
stationarity. A step that can easily be done as preprocessing for any ML method as
well.Inotherworks,weseemethodscomparedusingMeanAbsoluteError(MAE)
astheerrormeasure,andonlytheproposedmethodbythoseauthorsistrainedwith
L1loss,allothercompetitorswithL2loss,whichleadstounfaircomparisonsasthe
L1lossoptimizestowardsMAE,whereastheL2lossoptimizestowardsRootMean
Squared Error (RMSE). Many other works evaluate on a handful of somewhat ran-
domlypickedtimeseriesandthenshowplotsofforecastsversusactualsas“proof”of
howwelltheirmethodworks,withoutconsideringsimplebenchmarksormeaningful
errormeasures,andothersimilarproblems.Also,frequentlyforecastingcompetitions
and research works introduce new evaluation measures and methodologies, some-
timesneglectingthepriorresearch,e.g.,byseeminglynotunderstandingthatdividing
aseriesbyitsmeanwillnotsolvescalingissuesformanytypesofnon-stationarities
(e.g.,strongtrends).Thus,thereisnogenerallyacceptedstandardforforecasteval-
uationineverypossiblescenario.Thisgaphasharmedtheevaluationpracticesused
along with ML methods for forecasting significantly in the past. It is damaging the
areacurrently,withspuriousresultsinmanypapers,withresearchersnewtothefield
notbeingabletodistinguishbetweenmethodsthatworkandmethodsthatdon’t,and
theassociatedwasteofresources.
Overall,thisarticlemakesaneffortinthedirectionofraisingawarenessamongML
practitionersregardingthebestpracticesandpitfallsassociatedwiththedifferentsteps
of the point forecast evaluation process. Similar exhaustive efforts have been taken
in the literature to review, formally define and categorize other important concepts
in the ML domain such as concept drift (Webb et al. 2016), concept drift adapta-
tion(Gamaetal.2014)andminingstatisticallysoundpatternsfromdata(Hämäläinen
andWebb2019).Inthetimeseriesspace,lesscomprehensiveand/orsystematicworks
inthedirectionofcertainaspectsofourworkexist.Cerqueiraetal.(2020)haveper-
123

Forecastevaluationfor... 791
formedempiricalstudiesusingdifferentdatapartitioningandperformanceestimation
methodsonsomereal-worldandsyntheticdatasetsandpresentedguidelinesaround
which methods work under different characteristics of time series. In the work by
Petropoulos(2022)aswell,thoseauthorshaveasectiondedicatedtoexplainingfore-
castevaluationmeasures,bestpracticesforbothpointandprobabilisticforecastingas
wellasbenchmarking.Ditzleretal.(2015)haveconductedasurveyonexistingmeth-
ods for learning in non-stationary environments and the associated difficulties and
challenges.IntheworkbyShcherbakovetal.(2013),thoseauthorshavepresenteda
reviewonseveralerrormeasuresforforecastevaluationalongwiththeirdrawbacks
andalsoproposedanothernewmeasuretospecificallybecomerobusttooutlierson
timeseries.Recommendationshavealsobeengivenaroundselectingerrormeasures
underaspecificcontext.Gujarati(2021)hasprovidedacomprehensiveoverviewon
recentdevelopmentsineconometrictechniquesingeneralusingmanyexamples.
The rest of this paper is structured as follows. Section 2 first introduces ter-
minology associated with forecast evaluation, including different forms of non-
stationarities/non-normality seen in time series data. Next, Sect. 3 details the
motivation for this article, along with common pitfalls seen in the literature related
tousingsufficientdatasets,selectingappropriatemeasuresforevaluation,usingcom-
petitive benchmarks, visualisation of results using forecast plots and data leakage
in forecast evaluation. Then, in Sect. 4, we provide best practices and guidelines
around different aspects of forecast evaluation including how to best partition the
dataforagivenforecastingproblemwithnon-stationaritiesinvolvedwiththeseries,
howtoselectevaluationmeasuresdependingonthecharacteristicsofthetimeseries
under consideration and details of popular techniques used for statistical testing for
significance of differences between models. Finally, Sect. 5 concludes the paper by
summarisingtheoverallfindingsofthepaperandhighlightingthebestpracticesfor
forecastevaluation.Thecodeusedforthisworkispubliclyavailableforreproducibil-
ityoftheresults.1
2 Terminologyofforecastevaluation
Thisarticlefocusesonpointforecastevaluation,wheretheinterestistoevaluateone
particular statistic (mean/median) of the overall forecast distribution. However, we
note that there are many works in the literature around predicting distributions and
evaluating accordingly. Figure 1 indicates a common forecasting scenario with the
trainingregionofthedata,theforecastoriginwhichisthelastknowndatapointfrom
which the forecasting begins and the forecast horizon. In this section we provide a
generaloverviewoftheterminologyusedinthecontextofforecastevaluation.
Inforecastevaluation,similartootherMLtasks,validationandtestsetsareused
forhyperparametertuningofthemodelsandfortesting.Evaluationsonvalidationand
testsetsareoftencalledout-of-sample(OOS)evaluationsinforecasting.Thetwomain
setupsforOOSevaluationinforecastingarefixedoriginevaluationandrollingorigin
evaluation (Tashman 2000). Figure 2 shows the difference between the two setups.
1 Availableathttps://github.com/HansikaPH/Forecast_Evaluation_Pitfalls.
123

792 H.Hewamalageetal.
Fig.1 Aforecastingscenariowithtrainingregionofthedata,forecastoriginandtheforecasthorizon
In the fixed origin setup, the forecast origin is fixed as well as the training region,
andtheforecastsarecomputedasone-stepaheadormulti-stepaheaddependingon
therequirements.Intherollingoriginsetup,thesizeoftheforecasthorizonisfixed,
but the forecast origin changes over the time series (rolling origin), thus effectively
creatingmultipletestperiodsforevaluation.Witheverynewforecastorigin,newdata
becomes available for the model which can be used for re-fitting of the model. The
rollingoriginsetupisalsocalledtimeseriescross-validation(tsCV)andprequential
evaluationintheliterature(HyndmanandAthanasopoulos2018;Gamaetal.2013).
Timeseriescanhavedifferentformsofnon-stationaritiesandnon-normalityand
they make time series forecasting and evaluation a more difficult problem in com-
parison to other ML tasks. Listed below are some of such possibly problematic
characteristicsoftimeseries.
1. Non-stationarities.
• Seasonality
• Trends(Deterministic,e.g.,Linear/Exponential)
• StochasticTrends/UnitRoots
• Heteroscedasticity
• StructuralBreaks(suddenchanges,oftenwithlevelshifts)
2. Non-normality
• Non-symmetricdistributions
• Fattails
123

Forecastevaluationfor... 793
Fig.2 Comparisonoffixedoriginversusrollingoriginsetups.Theblueandorangedatapointsrepresent
thetrainingandtestingsetsrespectivelyateachevaluation.Thefigureontheleftsideshowsthefixedorigin
setupwheretheforecastoriginremainsconstant.Thefigureontherightshowstherollingoriginsetup
wheretheforecastoriginrollsforwardandtheforecasthorizonisconstant.Thereddottedlinedtriangle
enclosesallthetimestepsusedfortestingacrossalltheevaluations.Comparedtothefixedoriginsetup,it
isseenthatintherollingoriginsetup,testingdatainstancesineachevaluationpassontothetrainingsetin
thenextevaluationstep
• Intermittency
• Outliers
3. Serieswithveryshorthistory
Non-stationarityingeneralmeansthatthedistributionofthedatainthetimeseriesis
notconstant,butitchangesdependingonthetime(see,e.g.,Sallesetal.2019).What
werefertoasnon-stationarityinthisworkistheviolationofstrongstationaritydefined
asinEq.(1)(CoxandMiller1965).Strongstationarityisdefinedasthedistribution
ofafinitewindow(sub-sequence)ofatimeseries(discrete-timestochasticprocess)
remainingthesameasweshiftthewindowacrosstime.InEq.(1),y referstothetime
t
seriesvalueattimestept;τ ∈Zisthesizeoftheshiftofthewindowandn ∈Nisthe
sizeofthewindow.F Y (y t+τ ,y t+1+τ ,...,y t+n+τ )referstothecumulativedistribution
function of the joint distribution of (y t+τ ,y t+1+τ ,...,y t+n+τ ). Hence, according to
Eq.(1), F isnotafunctionoftime,itdoesnotdependontheshiftofthewindow.
Y
In the rest of this paper, we refer to the violation of strong stationarity simply as
non-stationarity.
F Y (y t+τ ,y t+1+τ ,...,y t+n+τ )= F Y (y t ,y t+1 ,...,y t+n ), forall τ ∈Z and n ∈N
(1)
Figure3givesanexampleofpossibleproblemswhenbuildingMLmodelsonsuch
data,wherethemodelsfailtoproducereasonableforecastsastherangeofvaluesis
differentinthetrainingandtestsets.Differenttypesofnon-stationaritiesareillustrated
inFig.4.Seasonalityusuallymeansthatthemeanoftheserieschangesperiodically
overtime,withafixedlengthperiodicity.Trendscanbetwofold;1)deterministictrends
-changethemeanoftheseries2)stochastictrends(resultingfromunitroots)-change
boththemeanandvarianceoftheseries(Sallesetal.2019).Notethatneithertrend
123

794 H.Hewamalageetal.
Fig.3 Forecastsfromdifferentmodelsonaserieswithunitrootbasednon-stationarity,withstochastic
trends.Inthisexample,wehaveacontinuouslyincreasingseries(increasingmean)duetotheunitroot.
TheMLmodelsarebuiltasautoregressivemodelswithoutanypre-orpost-processing,andassuchhave
verylimitedcapacitytopredictvaluesbeyondthedomainofthetrainingset,seeninthesecondpartofthe
testsetwherepredictionsareconsiderablyworsethaninthefirstpart
nor seasonality are concepts that have precise formal definitions. They are usually
merely defined as smoothed versions of the time series, where for the seasonality
thesmoothingoccursoverparticularseasons(e.g.,inadailyseries,theseriesofall
Mondays needs to be smooth, etc.). Heteroscedasticity changes the variance of the
series and structural breaks can change the mean or other properties of the series.
StructuralbreakisatermusedinEconometricsandStatisticsinatimeseriescontext
todescribeasuddenchangeatacertainpointintheseries.Ittherewithhasconsiderable
overlapwiththenotionofsuddenconceptdriftinanMLenvironment,whereasudden
changeofthedatadistributionisobserved(Webbetal.2016).
On the other hand, data can be far from normality, for example having fat tails,
orwhenconditionssuchasoutliersorintermittencyareobservedintheseries.Non-
stationarities and non-normality are both seen quite commonly in many real-world
time series and the decisions taken during forecast evaluation depend on which of
thesecharacteristicstheserieshave.Thereisnosingleuniversalrulethatappliesto
everyscenario.
3 Motivationandcommonpitfalls
AsbrieflyexplainedinSect.1,thereexistmanyMLbasedpapersforforecastingin
therecentliteraturethatareflawedoratleastweakwithregardstoforecastevaluation.
Thissectionisdevotedtoprovidethemotivationofourworkbydiscussingthemost
common problems and pitfalls associated with forecast evaluation in many recent
literature.
3.1 Benchmarksforforecastevaluation
Benchmarks are an important part of forecast evaluation. Comparison against the
rightbenchmarksandespeciallythesimpleronesisessential.However,ofteninthe
123

Forecastevaluationfor... 795
Fig.4 Differentnon-stationaritiesofseries
forecastingliterature,newlyproposedalgorithmsarenotrigorouslycomparedagainst
therelevantbenchmarks.
3.1.1 Naïvebenchmarkonfinanceseries
Arguably the simplest benchmark that is commonly employed in forecasting is the
naïveforecast,alsocalledpersistencemodelorno-changemodel,thatsimplyusesthe
lastknownobservationastheforecast.Ithasdemonstratedcompetitiveperformance
inmanyscenarios(ArmstrongJan2001),especiallyonseriesthatdemonstraterandom
walkproperties.Equation(2)showsthedefinitionofarandomwalk,where(cid:3) iswhite
t
noise;i.e.sampledfromanormaldistribution.Accordingly,thenaïveforecastatany
time step in the horizon can be defined as in Eq. (3). As the naïve forecast is the
lastknownobservation,theforecastisashiftedversionofthetimeserieswherethe
forecastsimplyfollowstheactuals(seeFig.5b).
y t+1 = y t +(cid:3) t (2)
yˆ t+h = y t (3)
Figure5illustratesthebehaviour ofdifferentmodelsthathavebeentrainedwith
differencingasappropriatepreprocessingonaseriesthathasaunitrootbasednon-
stationarity.Iftheserieshasnofurtherpredictablepropertiesabovetheunitroot(as
in this example), i.e., it is a random walk where the innovation added to the last
observationfollowsanormaldistributionwithameanofzero,thenaïveforecastisthe
theoreticallybestforecast,asalsosuggestedbytheRMSEvaluesreportedinTable1.
Other,morecomplexforecastingmethodsinthisscenariowillhavenotruepredictive
powerbeyondthenaïvemethod,andanypotentialsuperiority,e.g.,inerrorevaluations
123

796 H.Hewamalageetal.
Table1 RMSEvaluesofseveral
|     | Model | RMSE |
| --- | ----- | ---- |
MLmethodsandthenaïve
| forecastonarandomwalk | Randomforest(RF) | 1.01 |
| --------------------- | ---------------- | ---- |
simulatedtimeseriesusing
|     | Supportvectormachine | 1.00 |
| --- | -------------------- | ---- |
rollingorigindatapartitioning
|     | Neuralnetwork | 0.98 |
| --- | ------------- | ---- |
|     | Naïve         | 0.96 |
Thenaïveforecastisthetheoreticallybestforecastingmethodhere
Fig.5 Forecastsfromdifferentmodelsonaserieswithunitrootbasednon-stationarity,withstochastic
trends.TheMLmodelsarebuiltasautoregressiveintegratedmodels,i.e.,differencinghasbeendoneas
pre-processing.Themethodsshowverysimilarbehaviourtothenaïveforecast,anddonotaddanyvalue
overitbydefinitionoftheDataGeneratingProcess(DGP)used
isbypurechance,andshouldbeabletobeidentifiedasaspuriousresultonsufficiently
largedatasets.
In many practical applications, we find series that show strongly integrated
behaviour and therewith are close to random walks, as their innovations have high
degreesofnoise(suchasstockmarketdata,exchangeratedata,andtoalesserextent
wind power, wind speed). Here, a naïve forecast is a trivial yet competitive bench-
mark and without comparing against it, quality of more complex models cannot be
123

Forecastevaluationfor... 797
meaningfully assessed. More complex methods will in such series usually show a
behaviour where they mostly follow the series in the same way as the naïve fore-
cast,andimprovementsareoftensmallpercentagesovertheperformanceofthenaïve
benchmark.
Financialtimeseriessuchasexchangeratesandstockpricesareparticularlyprob-
lematictoforecast.Forexample,exchangeratesareafunctionofcurrenteconomic
conditions and expectations about future valuations. Simultaneously, currencies are
tradedonthefuturesmarket(e.g.,amarketparticipantsaystheywillbuyXamount
of US dollars in 1 year price for Y amount of Australian dollars), providing a mar-
ketexpectationoffuturepricemovements.ThesurveybyRossi(2013)hasanalysed
theliteratureonexchangerateforecastingbasedonadditionaleconomicinformation
andconcludedthatthemostchallengingbenchmarkistherandomwalkwithoutdrift
model.Yet,MLbasedresearchershavecontinuedtointroducesophisticatedNeural
Network(NN)modelsforexchangerateforecastingwithoutproperbenchmarking.In
theworkbyWuetal.(2021),thoseauthorshaveintroducedatransformerbasedmodel
withanembeddeddecompositionblockandanautocorrelationmechanismtoaddress
long-termtimeseriesproperties,calledAutoformer.Theirevaluationsetupincludes
anexchangeratedatasetusedinmanyrecentpapersofthistype(Laietal.2018),tobe
forecasted720daysintothefuture.Predictingdailyexchangeratesbasedononlypast
exchangeratesnearly2yearsintothefuturemaysoundlikeanoutrageousclaimto
Economistsalready,andthoseauthorsthemselvesstateinthatpaper,thatthedataset
containsnoobviousperiodicitiesandthusishardtobepredictedcomparedtoother
datasets.Itisthusunclearhowthedecompositionmechanismusedintheirproposed
modelshouldinanywaymakeavalidcontributiontopredictingtheseseries.Asthose
authorshavenotcomparedtheirmodelagainstthenaïvebenchmark,weexperiment
usinganaïveforecastonthisexchangeratedataset,underthesameevaluationsetup
as those authors. The results are as reported in Table 3. Table 3 reports the results
forAutoformerbothfromourexperimentsaswellastheexperimentsreportedinthe
paper.Asseenhere,theerrorvaluesthatwegetforAutoformerareslightlydifferent
fromtheerrorvaluesreportedinthepaper,duetotherandomnessoftheseedvalues
used in the experiments. Regardless, the naïve forecast beats both the results from
Autoformer across all the horizon sizes tested by a considerable margin, indicating
that the proposed method (and all comparison methods used in the original paper)
isessentiallyuselessonthisparticulardataset.Alsokeepinmindthatinthisexam-
pleAutoformertakeshourstorunonCPUoralternativelyneedsaGPUwith24GB
of memory, to finally arrive at results that are worse than trivial results that require
essentiallynocomputationatall.
More recently, in the work by Zhou et al. (2022a), those authors have proposed
aFrequencyimprovedLegendreMemory(FiLM)modelwhichhelpswithremoving
noisinessinsignalsandalsopreserveshistoricalinformationforlong-termforecasting.
Inthatpapertoo,thoseauthorshaveexperimentedonthesameexchangeratedataset.
According to the results reported in that paper, that model outperforms the naïve
forecastonthelongesthorizonsizeof720onthemultivariateforecastingstudyofthe
exchangeratedataset(theFiLMmodelhasreportedanMSEandMAEof0.727and
0.669,respectively,whereasthenaïveforecasthasanMSEof0.817andanMAEof
0.694asreportedinTable3).Wehaveattemptedtoreproducethesameresultsofthe
123

798 H.Hewamalageetal.
Table2 Resultsfromseveral
|     |     | TrialNo. | MSE | MAE |
| --- | --- | -------- | --- | --- |
rerunsoftheFiLMmodelinthe
| workbyZhouetal.(2022a) |     | 1   | 1.100 | 0.798 |
| ---------------------- | --- | --- | ----- | ----- |
|                        |     | 2   | 1.302 | 0.869 |
|                        |     | 3   | 1.491 | 0.940 |
|                        |     | 4   | 1.218 | 0.841 |
|                        |     | 5   | 1.261 | 0.855 |
Table3 ResultsfromthenaïveforecastandtheAutoformermodelontheexchangeratedataset
| Horizon | Naïve       | Autoformer(Rerun) | Autoformer(OriginalPaper) |     |
| ------- | ----------- | ----------------- | ------------------------- | --- |
|         | MAE MSE     | MAE MSE           | MAE MSE                   |     |
| 96      | 0.192 0.078 | 0.279 0.149       | 0.323 0.197               |     |
| 192     | 0.282 0.158 | 0.399 0.299       | 0.369 0.300               |     |
| 336     | 0.388 0.287 | 0.504 0.460       | 0.524 0.509               |     |
| 720     | 0.694 0.817 | 0.963 1.552       | 0.941 1.447               |     |
Bestmodelsshowninboldfacefont
FiLMmodel,toinvestigatethestatisticalsignificanceofthedifferencecomparedto
the naïve forecast. However, using five trials we have been unable to reproduce the
exactsameresultsonthehorizonsizeof720,andalltheresultswehavebeenableto
obtainusingthecodepublishedwiththeoriginalpapershowaperformanceinferior
tothenaïveforecast.TheseresultsfromthefivetrialsarereportedinTable2.Also
note that within each trial, the experiment is repeated 5 times using random seeds
and the mean of the metrics is reported to comply with what the authors have done
intheirwork.AsreportedinTable2,theinabilityoftheFiLMmodeltoconsistently
outperformthenaïveforecastindicatesthattheresultsreportedinthepaperaremost
likelyspuriousandobtainedrandomlybychance.
There have been many other recent works both published in ML outlets or pub-
lishedonpreprintserversalonewhichhavefollowedsimilarapproachestointroduce
NNbasedalgorithmsforlong-termforecastingandthentestedthemusingthesame
exchangeratedatasetbutwithoutcomparisonsagainstthenaïvebenchmarkandthere-
with leading to the same problematic conclusions of superiority of the respective
methods,namelyZhouetal.(2022b);Challuetal.(2022);Duetal.(2022);Sunand
Boning (2022); Woo et al. (2022); Zhou et al. (2022c); Li et al. (2022a); Shabani
etal.(2022).Whileitisgoodpracticetofollowacommonsetupforfurtherresearch
whichallowsforcomparisonagainstthepreviousstate-of-the-artmethods,iftheorig-
inal setup is flawed this means that all successors are flawed as well. As such, the
benchmarksandtheerrormeasureusedplayanimportantroleinsuchasetting.For
instance,byusingarelativeerrormeasure(detailedfurtherinSect.4.2)thatletsus
directlycompareagainstasimplebenchmarksuchasthenaïve,wecanbecertainof
thecompetitivenessofthemodelagainstsimplemethods.
Apartfromthefailuretousethecorrectbenchmarksasexplainedabove,thereare
furtherissuesassociatedwiththeseexchangeratetimeseries,thatmakesproducing
123

Forecastevaluationfor... 799
forecastsforthemafundamentallyflawedtask.Oneissueisthatexchangeratedata
(andinparticularthisdataset)isbasedontradingdays,meaningthatthetimeseries
thatalltheaforementionedworkshavedealtwithdonotcontainweekendsandarenot
equallyspaced,sothatanycommentsonseasonalityandcyclelengthinthesepapers
arelikelywrong.However,themostimportantpointisthatdataismorethaninputinto
analgorithm.Thelargebodyofliteratureineconomicsandfinanceover50yearsstates
thatitisnotsensibletoforecastexchangeratetimeseries,asitviolatestheefficient
markethypothesis(Fama1970).Thenatureofamarketisthatthepricereflectsallthe
informationpubliclyavailable,andevenifitdoesnotdoitforashortperiod(suchas
minutesordays;ormillisecondsinhigh-frequencytrading),andsomeinvestorsenjoy
extrainformation,theywillactonit,andthemarketpricewilladapt.Thereisaknown
persistence in the return volatility of foreign exchange rate markets (Berger et al.
2009).Still,thereisnoevidencethatitisreasonabletoassumetoforecastexchange
rates720daysintothefuture.Thefinalopenquestionofforecastingtheseexchange
ratescompletelyleftoutbytheaforementionedliteratureis,whyweareforecasting
exchange rate in the first place. Is the intention to trade on that information, or is it
forriskmanagement?Howdoesanerrormeasurethattranslatestobeingmorethan
50%ofthetimewrongleadtoanythingelsethanthebankruptcyoftheuser?Would
theauthors themselves besatisfiedthattheirpension fundisusingtheirown model
forinvestingtheirmoney?Weguessitisfairtoanswerthiswithno.
Similar considerations hold for stock price forecasting. Some examples from the
recentMLliteratureinthisareathatbenchmarkonstockmarketrelateddatawithout
comparisonsagainstthenaïvebenchmarkareShenetal.(2020);Duetal.(2021);Lin
etal.(2021).Stockmarketdataisanotherclassicalexamplewheredataisabundant,
but stock returns are deemed to be “almost unpredictable” (Engle 2003), especially
using only past stock prices as inputs alone, in the classic Economics literature, as
stock prices are again assumed to not be a function of their own past but of current
marketconditionsandexpectationsaboutfuturevaluations,andinanefficientmar-
ket,forecastingusingonlypaststockpricedatawillnotyieldresultsmoreaccurate
than a naïve forecast. It is important to note in this context that this holds for stock
pricesand returns,butnotvolatility,whichispredictable, e.g.,usingautoregressive
conditionalheteroskedasticity(ARCH),afindingwhichledtotheawardofthe2003
NobelMemorialPrizeinEconomicSciencestoRobertF.Engle(Engle2003).
Assuch,papersthatclaimthattheycanpredictstockpricesorreturns,orexchange
rates based on historic readings of these same signals alone need to be aware that
their claims contradict some central notions in Economics and that they need to be
evaluatedveryrigorously,astheirresultsarelikelytobespurious.
3.1.2 Othersimpleforecastingbenchmarks
On series that have clear seasonal patterns, models should accordingly be bench-
markedagainsttheseasonalnaïvemodelasthemostsimplisticbenchmark,andalso
othersimplebenchmarksarecommonlyusedinforecasting.IntheworkbyZhouetal.
(2021) those authors have proposed a novel memory and time efficient transformer
based architecture, namely Informer for long sequence forecasting. That paper has
alsowontheoutstandingpaperawardattheAssociationfortheAdvancementofArti-
123

| 800 |     |     | H.Hewamalageetal. |
| --- | --- | --- | ----------------- |
Table4 Resultsofthe
|     | Model | ETTh1 (720) | ECL (960) |
| --- | ----- | ----------- | --------- |
DHR-ARIMAmodelalongwith
|     |     | MSE MAE | MSE MAE |
| --- | --- | ------- | ------- |
Informerandtheother
| benchmarksontheunivariate | Informer | 0.269 0.435 | 0.582 0.608 |
| ------------------------- | -------- | ----------- | ----------- |
forecastingtaskintheworkby
| Zhouetal.(2021) | Informer† | 0.257 0.421 | 0.594 0.638 |
| --------------- | --------- | ----------- | ----------- |
|                 | LongTrans | 0.273 0.463 | 0.624 0.645 |
|                 | Reformer  | 2.112 1.436 | 7.019 5.105 |
|                 | LSTMa     | 0.683 0.768 | 1.545 1.006 |
|                 | DeepAR    | 0.658 0.707 | 0.657 0.683 |
|                 | ARIMA     | 0.659 0.766 | 1.370 0.982 |
|                 | Prophet   | 2.735 3.253 | 6.901 4.264 |
|                 | DHR-ARIMA | 0.140 0.297 | 0.433 0.499 |
†whichusesacanonicalself-attentionmechanism
Bestmodelsshowninboldfacefont
ficial Intelligence (AAAI) conference 2021. In that work several experiments have
been conducted using Electricity Transformer Temperature data (ETT), Electricity
ConsumptionLoad(ECL)2dataandWeatherdata.TheETTandECLhourlydatasets
clearly show strong multiple seasonal patterns (being hourly series, daily, weekly,
andyearlypatternsaretobeexpected).However,theInformermodelhasonlybeen
benchmarkedagainstnon-seasonalARIMAwhichisnotcapableofhandlingmultiple
seasonalities,andisagrotesquelymisspecifiedmodelthatwouldnotbeusedinprac-
tice.Toclaimitssuperiorperformanceinthelonghorizonforecastingproblems,the
proposedInformermodelinthiscaseneedstobecomparedagainststatisticalstandard
benchmarksthatinherentlyhandlemultipleseasonalitieswell,suchastheDynamic
HarmonicRegressionARIMA(DHR-ARIMA)modelandtheTBATSmodel(Hynd-
manandAthanasopoulos2018).Todemonstratethis,weconductanexperimentwith
aDHR-ARIMAmodelontheETTh andtheECLdatasetsontheirrespectivelongest
1
horizon sizes (720 for the ETTh dataset and 960 for the ECL dataset) for the uni-
1
variateforecastingtask.FortheETTh 1 dataset,dailyandyearlyseasonalpatternsare
incorporatedwhereasfortheECLdataset,alldaily,weeklyandyearlyseasonalities
areincludedusingFouriertermsintheDHR-ARIMAmodel.Theresultsarereported
in Table 4, along with the results for the benchmark models shown in the original
paper.ThehorizonsizeisshownwithinparenthesesnexttothedatasetnameinTable
4.Asseenfromtheseresults,whentheFouriertermsareincorporatedtocapturethe
multipleseasonalities,thestandardDHR-ARIMAcanoutperformARIMAaswellas
thetwovariantsoftheproposedalgorithm,InformerandInformer†.
Apartfromthat,therecentworkbyZengetal.(2022)haschallengedthelong-term
timeseriesforecastingcapabilityoftransformerbasedmodelsingeneralbycomparing
againstarelativelysimplelinearlayerbasedNN,i.e.,asetoflinearmodelstrained
fortheforecastinghorizoninquestiondirectly.Asthoseauthorshavestatedintheir
work,mostoftheperformancegainsoftheaforementionedtransformerbasedmodels
forlong-termforecastingareduetocomparingtheirdirectmulti-stepaheadforecasts
against iterative forecasts that are produced from more traditional methods, which
2
https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014
123

Forecastevaluationfor... 801
inherentlyhaveerroraccumulationissuesduetotherecursivenatureofforecasting.
This claim once again emphasises the need to perform comparisons with the right
andthemostcompetitiveestablishedforecastingbenchmarksfortherelevantstudy,
as directly trained linear models have been shown to outperform all the considered
transformerarchitecturesinthatwork.
3.2 Datasetsforempiricalevaluations
AnothercommonproblemintheMLbasedforecastingliteratureisthatmanyworks
donotusesufficientamountsofdatasets/timeseriesfortheexperimentsforreason-
ablyclaimingthesuperiorperformanceoftheproposedalgorithms.Whileitmaybe
somewhatsubjectivewhatamountofseriesissufficient,oftentimespapersuseonly
a handful of series when the authors clearly don’t seem to care about their particu-
larapplicationand/orwhenhundredsofseriescouldbereadilyavailableforthesame
applicationcase,e.g.,innotoriousstockreturnpredictiontasks.Someexamplesalong
theselines(therearemanymoreintheliterature)aretheworksofLiuetal.(2021,
2020); Godfrey and Gashler (2018); Shen et al. (2020), and Zhang et al. (2021). In
particular,Zhangetal.(2021)use3timeseriesintotal,asimulatedAR(1)process,a
bitcoinpriceseriesandaninfluenza-likeillnessseries,toevaluatetheirnon-parametric
neural network method. While the influenza-like illness series may be a good fore-
castingcasestudy,basicallythesameconsiderationsasforexchangeratesandstock
pricesholdforbitcoinprices,thoughbitcoinwaspresumablyalessefficientmarket,
especiallyinitsinfancy.ThebestmodeltoforecastanAR(1)processistriviallyan
AR(1)model(whichisnotusedasabenchmarkinthatpaper),sofittingcomplexneu-
ralnetworkstothisseriesmakesverylimitedsense.3Theauthorsarehereeffectively
fittinganeuralnetworktomodela2-dimensionallinearrelationshipplusnoise.
3.3 Evaluationmeasuresforforecasting
Avarietyofevaluationmeasureshavebeenproposedforforecastevaluationoverthe
years, and thus ML based forecasting researchers seem to be in a situation unable
toclearlypicktheevaluationmeasuresthatbestsuittheirrequirementsandthedata
athand.Forexample,intheworkbyLaietal.(2018),thoseauthorshaveusedtwo
measuresRootRelativeSquaredError(RSE)andEmpiricalCorrelationCoefficient
(CORR) for the evaluation which both use scaling based on the mean of the time
series.Whilethismayworkasascalingtechniquefortimeseriesthathaveminimal
ornotrends,forseriesthatcontaintrendbasednon-stationaritiesthisdoesnotscale
theseriesmeaningfully.Yet,thisinformationisonlyimplicitandnotconveyedtothe
readerintheirwork.Consequently,therehavebeenmanyotherworkswhichfollowed
thesameevaluationsetupandthemeasureswithoutanyattentiontowhethertheused
3 Onecouldarguethatnotalwaysthetruedatageneratingprocess(DGP)isthebestforecastingmodel,
butthisusuallyhappensforcomplexDGPswherenotenoughdataisavailabletoestimatetheirparameters
correctlyandsosimplermodelsperformbetterforforecasting.However,anAR(1)isalreadyverysimple
sothatcomparedtoaconsiderablymorecomplexneuralnetworkthisconsiderationseemsnotrelevant
here.
123

802 H.Hewamalageetal.
seriescontaintrendsornot(examplesareGuoetal.2022;Shihetal.2019;Wuetal.
2020; Ye et al. 2022). Although this allows for direct comparisons against previous
work,italsohascausedallsuccessiveworkstooverlookthesameissueswithtrended
timeserieswiththeusederrormeasures.
Someworksalsousescale-dependentmeasuressuchasMeanSquaredError(MSE),
RMSEandMAEonmultivariatedatasetshavingmanytimeseries(examplesareCui
etal.2021;Duetal.2021;Yeetal.2022).Whilethisisreasonableifalltheseriesin
thedatasethavesimilarscales,ifthescalesaredifferent,thismeansthattheoverall
error value would be driven by particular series. Some have used the coefficient of
determination(R2)betweentheforecastsandtheactualvaluesasaforecastevaluation
measureaswell(forexampleShenetal.2020;Zhouetal.2022).Thiscanbeaquite
misleading evaluation measure especially in the case of random walk time series,
which may give almost perfect R2 values (close to 1) due to the following nature
of the series indicating a competitive performance of the model, whereas in reality
theseriesdoesnothaveanypredictablepatternsatall.MAPEisanotherevaluation
measurecommonlyappliedincorrectlyonserieshavingverysmallvaluesintherange
[−1,1](examplesareMoonetal.2022;Wuetal.2020).Duetothedenominatorof
theMAPEwhichistheactualvalueofthetimeseries,onserieshavingvaluesclose
to0,MAPEgivesexcessivelylargevaluesirrespectiveoftheactualprediction.
3.4 Forecastplots
Plotswithtimeseriesforecastingresultscanbequitemisleadingandshouldbeused
withcaution.Analysingplotsofforecastsfromdifferentmodelsalongwiththeactuals
andconcludingthattheyseemtofitwellcanleadtowrongconclusions.Itisimportant
tousebenchmarksandevaluationmetricsthatarerightforthecontext.Inascenario
likearandomwalkseriesasinFig.5asstatedbefore,visuallyourmodelsmaylook
likeachievingsimilarorbetteraccuracythanthenaïvemethod,butitwillbeaspurious
result.Thevisualappealofageneratedforecastorthepossibilityofsuchaforecast
tohappeningeneralarenotgoodcriteriatojudgeforecasts.However,manyrecent
forecastingliteratureseemtouseforecastplotsthatdonotconveymuchinformation
regardingtheperformanceofthemethods(forexampleLiuetal.2021, 2020;Duetal.
2021).
Figure 6a shows a monthly time series with yearly seasonal patterns along with
forecasts from the ETS model. The figure furthermore shows the forecasts under
fixedoriginandrollingorigindatapartitioningschemesforthenaïveforecast.When
periodic re-fitting is done with new data coming in as in a rolling origin setup, the
naïve forecast gets continuously updated with the last observed value. For the fixed
origincontextontheotherhand,thenaïveforecastremainsconstantasastraightline
corresponding to the last seen observation in the training series. We see that with a
rolling-originnaïveforecast,thepredictionstendtolookvisuallyveryappealing,as
the forecasts follow the actuals and our eyes are deceived by the smaller horizontal
distances instead of the vertical distances that are relevant for evaluation. Figure 6b
illustratesthisbehaviour.Itisclearhowthehorizontaldistancebetweentheactuals
andthenaïveforecastatbothpointsAandBaremuchlesscomparedtothevertical
123

Forecastevaluationfor... 803
Fig.6 Propertiesofthenaïveforecast
Table5 RMSEvaluesofrolling
Model RMSE
originversusfixedoriginnaïve
forecastsandETSforecastson
Naïve(RollingOrigin) 31.23
thetimeseriesinFig.6a
Naïve(FixedOrigin) 37.10
ETS 29.93
distances which are the relevant ones for evaluation. In these situations we need to
relyontheerrormeasures,astheplotsdonotgiveusmuchinformation.Asreported
inTable5,forthisscenariotheETSforecastshaveasmallerRMSEerrorcompared
tobothrollingoriginandfixedoriginnaïveforecasts.
Figure 7 shows another series having unit root based non-stationarity and fixed
originforecastsfromseveralmodelsandthenaïveforecastforaforecasthorizonof
60timestepsahead.Thisshowsanotherissuewithusingplotstodetermineforecast
accuracy.Asexplainedpreviously,onarandomwalktimeseries,anaïveforecastis
thetheoreticallybestforecastthatcanbeobtained.ThisisalsoclarifiedbytheRMSE
valuesfortheseforecastsfromthedifferentmodelsasreportedinTable6.However,
123

804 H.Hewamalageetal.
Table6 RMSEvaluesofseveral
Model RMSE
methodsandthenaïveforecast
onaunitrootbasedtimeseries
RF 3.18
usingfixedorigindata
SupportVectorMachine 17.88
partitioning
NeuralNetwork 35.22
ARIMA 6.44
Naïve 3.04
Fig.7 Fixedoriginforecastsfromseveralmodelsandthenaïveforecastonarandomwalktimeseries
thenaïveforecastforfixedoriginisaconstant.Althoughthisdoesnotlookrealistic,
andinmostapplicationdomainswecanbecertainthattheactualswillnotbeconstant,
practitionersmaymistakenlyidentifysuchbehaviourasapotentialproblemwiththe
models, where this forecast is indeed the best possible forecast in the sense that it
minimizestheerrorbasedontheinformationavailableatpresent.
Insummary,plotsoftheforecastscanbedeceivingandshouldbeusedmostlyfor
sanity checking. Decisions should mostly be made based on evaluations with error
measuresandnotbasedonplots.
3.5 Dataleakageinforecastevaluation
Dataleakagereferstotheinadvertentuseofdatafromthetestset,ormoregenerally
data not available during inference, while training a model. It is always a potential
problem in any ML task. For example, Kaufman et al. (2012) present an extensive
reviewontheconceptofdataleakagefordataminingandpotentialwaystoavoidit.
Arnott et al. (2019) discuss this in relation to the domain of finance. Hannun et al.
(2021)proposeatechniquebasedonFisherinformationthatcanbeusedtodetectdata
leakage of a model with respect to various subsets of the dataset. Brownlee (2020)
also provide a tutorial overview on data preparation for common ML applications
whileavoidingdataleakageintheprocess.However,inforecastingdataleakagecan
happen easier and can be harder to avoid than in other ML tasks such as classifica-
tion/regression.
123

Forecastevaluationfor... 805
Forecasting is usually performed in a self-supervised manner with rolling origin
evaluations where periodic re-training of models is performed, and within this re-
training,itisnormalthatdatatravelsfromthetesttothetrainingsetasseenonFig.
2. As such, it is often difficult and not practical to separate training and evaluation
code bases. As such, we often have to trust the software provider that everything is
implementedcorrectly,andanexternalevaluationisdifficult.
Also, more indirect forms of data leakage can happen in forecasting. In analogy
to classification/regression, where data leakage sometimes happens by normalising
databeforepartitioningforcross-validation,inforecasting,dataleakagecanhappen
byperformingsmoothing,decomposition(modedecomposition),normalisationetc.
overthewholeseriesbeforepartitioningfortrainingandtesting.Thiscansometimes
be seen in ML based forecasting literature. In the work by Ran et al. (2023) those
authorsperformEmpiricalModeDecomposition(EMD)presumablyoverthewhole
series.Zhouetal.(2022)performnormalisationofthetimeseriespresumablybefore
thetrain,testsetsplit.KurangaandPillay(2022)alsoperform0-1normalisationof
thetimeseriespresumablybeforemodelling.Theyhaveusedtwoforecasthorizons
onthesameseries(inarollingoriginfashion),yetthereisnomentiontoperforming
thenormalisationtwicetoreflectthetrainingdataineachcase.Hencethatcouldlead
todataleakagetoo.Todemonstratetheeffectofleakage,weperformanexperiment
on a random walk time series using a rolling origin setup. EMD is performed on
the series and the intrinsic mode functions are each modelled using Random Forest
(RF)modelsandtheresiduemodelledusinganARIMAmodel.Inthedataleakage
scenario,EMDisperformedonthewholeserieswhereasinthenoleakagescenario,
EMD is performed iteratively for each new training set in the rolling origin setup.
As EMD has some low-frequent components, applying it over the full series, these
low-frequent components contain considerable information about the series’ future.
Theforecasthorizonissetto20stepswith50rollingoriginsconstitutinganoverall
testsetof1000steps.TheresultsarereportedinTable7.Asseenbytheresults,with
dataleakagethemodelbecomesthebestmodelevenoutperformingthenaïveforecast
whichisthetheoreticallybestforecastonarandomwalkseries.The p-valueindicates
the p-value from the Wilcoxon signed-rank test applied to measure the statistical
significanceofthedifferencesofthetwotechniques(leakagevs.noleakage)against
thenaïveforecast.Ap-value<0.05indicatesthatthemethodissignificantlydifferent
from the naïve forecast. Therefore, from these results it is clear that although when
noleakageispresentinthemethod,theforecastissignificantlyworsethanthenaïve
forecast, when leakage is incorporated, the method has a nearly significant p-value
rendering it better than the naïve forecast. These forecasts are further visualized in
the plots in Fig. 8. Data leakage can happen even when extracting features such as
tsfeatures (Hyndman et al. 2019), catch22 (Lubba et al. 2019) that are not
constantovertime,tofeedasinputstothemodel.Thus,featurescanbeextractedonly
fromthetrainingsetdata,andmayneedtobere-calculatedeitherperiodicallyorover
thespecificinputwindows.However,thiscanbecomputationallyexpensive.
Anothertypeofleakageespeciallywhentrainingglobalmodelsthatlearnacross
series, which is common practice nowadays for ML models, is when one series in
thedatasetcontainsinformationaboutthefutureofanotherseries.Forexamplewith
anexternalshocklikeCOVID-19oraglobaleconomycollapse,alltheseriesinthe
123

806 H.Hewamalageetal.
Table7 RMSEvaluesforthe
Model RMSE p-value
leakageandnoleakage
experimentsonaunitrootbased
Naïve 3.46 –
timeseries
LeakageModel 3.12 0.067
NoLeakageModel 5.65 1.85x10
−6
Thep-valuesfromthestatisticaltestsofdifferencesagainstthenaïve
forecastarealsoreported
Fig.8 Forecastsfromamodelwithleakageandnoleakageonatimeserieshavingunitrootbasednon-
stationarity
datasetcanbeequallyaffected.Therefore,iftheseriesinthedatasetarenotaligned
and one series contains the future values with respect to another, when splitting the
training region, future information can be already included within the training set.
However,inrealworldapplicationseriesareusuallyalignedsothatthisisnotabig
problem.Ontheotherhand,inacompetitionsetupsuchastheM3andM4forecasting
competitions(MakridakisandHibon2000;Makridakisetal.2020),wheretheseries
arenotaligned,thiscaneasilyhappen(Talagala2020).
Dataleakagecanalsohappensimplyduetousingthewrongforecasthorizon.This
can happen by using data that in practice will become available later. For example,
we could build a one-day-ahead model, but use summary statistics over the whole
day.Thismeansthatwecannotrunthemodeluntilmidnight,whenwehavealldata
fromthatdayavailable.Iftherelevantpeoplewhousetheforecastsworkonlyfrom
9am-5pm,itbecomeseffectivelyasame-daymodel.Theotheroptionistosettheday
tostartandendat5pmeveryday,butthatmayleadtootherproblems.
In conclusion, data leakage dangers are common in self-supervised forecasting
tasks.Itisimportanttoavoidleakageproblems1)inrollingoriginschemesbybeing
abletoverifyandtrusttheimplementation,asexternalevaluationcanbedifficult2)
duringpreprocessingofthedata(normalising,smoothingetc.)andextractingfeatures
suchastsfeaturesbysplittingthedataintotrainingandtestsetsbeforehand3)
bymakingsurethatwithinasetofseries,oneseriesdoesnotcontaininitstraining
periodpotentialinformationaboutthefutureofanotherseries.
123

Forecastevaluationfor... 807
4 Guidelinesandbestpracticesforforecastevaluation
Forecastmodelbuildingandevaluationtypicallyencompassesthefollowingsteps.
• Datapartitioning
• Forecasting
• ErrorCalculation
• ErrorMeasureCalculation
• StatisticalTestsforSignificance(optional)
The process of evaluation in a usual regression problem is quite straightforward.
Thebestmodeloutofapooloffittedmodelsisselectedbasedonthevalueofafinal
errormeasureonthevalidationset.Therelevanterrormeasuresusedetc.arestandard
andestablishedasbestpracticesinthesedomains.However,whenitcomestoforecast
evaluation,manydifferentoptionsareavailableforeachoftheaforementionedsteps
and no standards have been established thus far, and hence all the pitfalls in the
literatureasexplainedinSect.3.Therefore,inthissectionwearepresentingasetofbest
practicesandguidelinesforeachoftheaforementionedstepsinforecastevaluation.
4.1 Datapartitioning
Inthefollowingwepresenttheguidelinesarounddatapartitioningforforecasteval-
uation.
4.1.1 Fixedoriginsetup
Fixedoriginsetupisafasterandeasiertoimplementevaluationsetup.However,witha
singleseries,thefixedoriginsetuponlyprovidesoneforecastpereachforecaststepin
thehorizon.AccordingtoTashman(2000),apreferredcharacteristicofOOSforecast
evaluationistohavesufficientforecastsateachforecaststep.Also,havingmultiple
forecastsforthesameforecaststepallowstoproduceaforecastdistributionpereach
stepforfurtheranalysis.AnotherrequirementofOOSforecastevaluationistomake
theforecasterrormeasuresinsensitivetospecificphasesofbusiness(Tashman2000).
However,withafixedoriginsetup,theerrorsmaybetheresultofparticularpatterns
only observable in that particular region of the horizon (Tashman 2000). Therefore,
the following multi period evaluation setups are introduced as opposed to the fixed
originsetup.
4.1.2 Rollingorigin,timeseriescross-validationandprequentialevaluationsetups
ArmstrongandGrohman(1972)areamongthefirstresearcherstogiveadescriptive
explanation of the rolling origin evaluation setup. Although the terms rolling origin
setupandtsCVareusedinterchangeablyintheliterature,inadditiontotheforecast
originrollingforward,tsCValsoallowstoskiporigins,effectivelyrollingforwardby
morethanonestepatatime(analogouslytothedifferencebetweenaleave-one-out
CVandak-foldCV).
123

808 H.Hewamalageetal.
Fig.9 ComparisonofExpandingWindowversusRollingWindowsetups.Theblueandorangepoints
representthetrainingandtestsets,respectively.ThefigureontheleftsideshowstheExpandingWindow
setupwherethetrainingsetkeepsexpanding.ThefigureontherightshowstheRollingWindowsetup
wherethesizeofthetrainingsetkeepsconstantandthefirstpointofthetrainingsetkeepsrollingforward
Withsuchmultiperiodevaluations,eachtimetheforecastoriginupdates,themodel
encountersnewactualdata.Withnewdatabecomingavailable,wehavetheoptions
to – in the terminology of Tashman (2000) – either update the model (feed in new
dataasinputs)orrecalibrateit(refitwithnewdata).Althoughforsomeofthetradi-
tionalmodelssuchasETSandARIMA,theusualpractice(andtheimplementation
intheforecastpackage)inarollingoriginsetupistorecalibratethemodels,for
generalMLmodelsitismorecommontomostlyjustacceptnewdataasinputsand
only periodically retrain the model (updating). As ML methods tend to work better
with higher granularities, re-fitting is not an option (for example, a monthly series
predicted with ETS vs. a 5-minutely series predicted with Light Gradient Boosting
Models).Therefore,retrainingasthemostrecentdatabecomesavailablehappensin
MLmethodsmostlyonlywhensomesortofconceptdrift(changeoftheunderlying
datageneratingprocess)isencountered(Webbetal.2016).
Rolling origin evaluation can be conducted in two ways; 1) Expanding window
setup 2) Rolling window setup. Figure 9 illustrates the difference between the two
approaches.Theexpandingwindowmethodisagoodsetupforsmalldatasets/short
series (Bell and Smyl 2018). On the other hand, the rolling window setup removes
theoldestdatafromtrainingasnewdatabecomesavailable(Cerqueiraetal.2020).
Thiswillnotmakeadifferencewithforecastingtechniquesthatonlyminimallyattend
tothedistantpast,suchasETS,butmaybebeneficialwithpureautoregressiveML
models,thathavenonotionoftimebeyondthewindows.Apotentialproblemofthe
rollingoriginsetupisthatthefirstfoldsmaynothavemuchdataavailable.However,
thesizeofthefirstfoldsisnotanissuewhendealingwithlongseries,thusmaking
rollingoriginsetupagoodchoicewithsufficientamountsofdata.Ontheotherhand,
with shortseries itis also possible to perform a combination of the aforementioned
two rolling origin setups where we start with an expanding window setup and then
movetoarollingwindowsetup.
123

Forecastevaluationfor... 809
Fig.10 Comparisonof
randomizedCVversusOOS
evaluation.Theblueandorange
dotsrepresentthetrainingand
testsets,respectively.Inthe
usualk-fold-CVsetupthetesting
instancesarechosenrandomly
overtheseries.InOOS,thetest
setisalwaysreservedfromthe
endoftheseries
4.1.3 (Randomized)Cross-validation
Theaforementionedtwotechniquesofdatapartitioningpreservethetemporalorderof
thetimeserieswhensplittingandusingthedata.Acommonmisconceptionisthatthis
isalwaysanecessitywhendealingwithtimeseries.Anotherformofdatapartitioning
istouseacommonrandomizedCVschemeasfirstproposedbyStone(1974).This
schemeisvisualizedinFig.10.Comparedtotheaforementionedvalidationschemes
whichpreservethetemporalorderofthedata,thisformofrandomizedCVstrategy
canmakeefficientuseofthedata,sinceallthedataisusedforbothmodeltraining
as well as evaluation in iterations (Hastie et al. 2009). This helps to make a more
informedestimationaboutthegeneralisationerrorofthemodel.
However, this form of random splitting of a time series does not preserve the
temporalorderofthedata,andisthereforeoftentimesnotusedandseenasproblematic.
Thecommonpointsofcriticismforthisstrategyarethat,1)itcanmakeitdifficultfor
amodeltocaptureserialcorrelationbetweendatapoints(autocorrelation)properly,2)
potentialnon-stationaritiesintimeseriescancauseproblems(forexample,depending
on the way that the data is partitioned, if alldata from Sundays happen to be inthe
test set but not the training set in a series with weekly seasonality, then the model
willnotbeabletoproduceaccurateforecastsforSundayssinceithasneverseendata
ofSundaysbefore),3)thetrainingdatacontainsfutureobservationsandthetestset
containspastdataduetotherandomsplittingand4)sinceevaluationdataisreserved
randomlyacrosstheseries,theforecastingproblemshiftstoamissingvalueimputation
problem which certain time series models are not capable of handling (Petropoulos
2022).
Despitetheseproblems,randomizedCVcanbeappliedtopureARmodelswithout
serialcorrelationissues.Bergmeiretal.(2018)theoreticallyandempiricallyshowthat
CVperformswellinapureARsetup,aslongasthemodelsnestorapproximatethe
true model, as then the errors are uncorrelated, leaving no dependency between the
individualwindows.Tocheckthis,itisimportanttoestimatetheserialcorrelationof
residuals.Forthis,theLjung-Boxtest(LjungandBox1978)canbeusedontheOOS
residualsofthemodels.Whileforoverfittingmodelstherewillbenoautocorrelation
left in the residuals, if the models are underfitted, some autocorrelation will be left
in the OOS residuals. If there is autocorrelation left, then the model still does not
usealltheinformationavailableinthedata,whichmeanstherewillbedependencies
betweentheseparatewindows.Insuchascenario,CVofthetimeseriesdatasetwill
notholdvalid,andunderestimatethetruegeneralisationerror.Theexistenceofsignif-
icantautocorrelationsanywaymeansthatthemodelshouldbeimprovedtodobetter
123

810 H.Hewamalageetal.
ontherespectiveseries(increasetheARordertocaptureautocorrelationetc.),since
themodelhasnotcapturedalltheavailableinformation.Oncethemodelsaresuffi-
cientlycompetentincapturingthepatternsoftheseries,forpureARsetups(without
exogenousvariables),standardk-foldCVisavalidstrategy.Therefore,insituations
withshortseriesandsmallamountsoftrainingdata,whereitisnotpracticallyfeasible
to apply the aforementioned tsCV techniques due to the initial folds involving very
smalllengthsoftheseries,thestandardCVmethodwithsomecontrolofunderfitting
ofthemodelsisabetterchoicewithefficientuseofdata.
The aforementioned problem that the testing windows can contain future obser-
vations, is also addressed by Bergmeir et al. (2018). With the CV strategy, the past
observations not in the training data but existing in the test set can be considered
missingobservations,andthetaskisseenmoreasamissingvalueimputationprob-
lemratherthanaforecastingproblem.ManyforecastingmodelssuchasETS(inits
implementation in the forecast package (Hyndman and Athanasopoulos 2018)),
whichiteratethroughoutthewholeseries,cannotproperlydealwithmissingdata.For
RecurrentNeuralNetworks(RNN)aswell,duetotheirinternalstatesthatareprop-
agatedforwardalongtheseries,standardk-foldCVwhichpartitionsdatarandomly
acrosstheseriesisusuallynotapplicable.Therefore,forsuchmodels,theonlyfeasible
validationstrategyistsCV.ModelssuchasETScananywaytraincompetitivelywith
minimalamountsofdata(asisthecasewiththeinitialfoldsofthetsCVtechnique)
andthus,arenotquiteproblematicwithtsCV.However,forreasonablytrainedpure
AR models, where the forecasts for one window do not in any way depend on the
informationfromotherwindows(duetonotunderfittingandhavingnointernalstate),
itdoesnotmakeadifferencebetweenfillingthemissingvaluesinthemiddleofthe
seriesandpredictingfuturevalues,wherebothareperformedOOS.Nevertheless,the
findingsbyBergmeiretal.(2018)arerestrictedtoonlystationaryseries.
4.1.4 Datapartitioningfornon-stationarydata
Cerqueira et al. (2020) experimented using non-stationary series, where they have
concluded that OOS validation procedures preserving the temporal order (such as
tsCV),aretherightchoicewhennon-stationaritiesexistintheseries.However,apos-
siblecriticismofthatworkisthechoiceofmodels.WehaveseeninSect.3thatML
modelsareoftentimesnotabletoaddresscertaintypesofnon-stationaritiesoutofthe
box. More generally speaking, ML models are non-parametric, data-driven models.
Assuch,themodelsaretypicallyveryflexibleandthefunctionfitteddependsheavily
onthecharacteristicsoftheobserveddata.Thoughrecentlychallenged(Balestriero
etal.2021),acommonnotionisthatMLmodelsaretypicallygoodatinterpolation
andlackextrapolationcapabilities.ThemodelsusedbyCerqueiraetal.(2020)include
severalMLmodelssuchasaRule-basedRegression(RBR)model,aRFmodeland
aGeneralizedLinearModel(GLM),withoutinanywayexplicitlytacklingthenon-
stationarity in the data (similar to our example in Sect. 3). Thus, if a model is poor
andnotproducinggoodforecasts,performingavalidationtoselecthyperparameters,
usinganyoftheaforementionedCVstrategies,willbeoflimitedvalue.Furthermore,
andmoreimportantly,non-stationarityisabroadconceptandbothforthemodelling
andtheevaluationitwilldependonthetypeofnon-stationaritywhichprocedureswill
123

Forecastevaluationfor... 811
performwell.Forexample,withabruptstructuralbreaksandlevelshiftsoccurringin
theunknownfuture,butnotinthetrainingandtestset,itwillbeimpossibleforthe
models to address this change and none of the aforementioned evaluation strategies
woulddosoeither.Inthissituation,eventsCVwouldgrosslyunderestimatethegen-
eralisationerror.ForamoregradualunderlyingchangeoftheDGP,avalidationset
attheendoftheserieswouldbemoreappropriatesinceinthatcase,thedatapoints
closertotheendoftheseriesmaybealreadyundergoingthechangeofthedistribu-
tion.Ontheotherhand,iftheserieshasdeterministictrendorseasonality,whichare
straightforwardtoforecast,theycanbesimplyextractedfromtheseriesandpredicted
separatelywhereasthestationaryremaindercanbehandledusingthemodel.Insuch
a setup, the k-fold CV scheme will work well for the model, since the remainder
complieswiththestationaritycondition.Forothernon-deterministictrends,thereare
severaldatapre-processingstepsmentionedintheliteraturesuchaslag-1differencing,
logarithmic transformation (for exponential trends), Seasonal and Trend Decompo-
sitionusingLoess(STLDecomposition),localwindownormalisation(Hewamalage
etal.2021),movingaveragesmoothing,percentagechangetransform,wavelettrans-
form etc. (Salles et al. 2019). The findings of Salles et al. (2019) have concluded
that there is no single universally best transformation technique across all datasets;
ratheritdependsonthecharacteristicsoftheindividualdatasets.Ifappropriatedata
pre-processingstepsareappliedtoenablemodelstohandlenon-stationarities,witha
pure AR setup, the CV strategy stillholds valid after the data transformation, if the
transformationachievesstationarity.Assuch,toconclude,fornon-stationarities,tsCV
seemsthemostadequateasitpreservesthetemporalorderinthedata.However,there
aresituationswherealsotsCVwillbemisleading,andtheforecastingpractitionerwill
alreadyforthemodellingneedtoattempttounderstandthetypeofnon-stationarity
theyaredealingwith.Thisinformationcansubsequentlybeusedforevaluation,which
mayrenderCVmethodsforstationarydataapplicableaftertransformationsofthedata
tomakethemstationary.
4.1.5 Summaryandguidelinesfordatapartitioning
It is important to identify which out of the above data partitioning strategies most
closely estimates (without under/overestimation) the final error of a model for the
test set under the given scenario (subject to different non-stationarities/serial corre-
lations/amount of data of the given time series). The gist of the guidelines for data
partitioningisvisualizedbytheflowchartinFig.11.Iftheseriesarenotshort,tsCVis
usuallypreferrableoverk-foldCV,iftherearenopracticalconsiderationssuchasthat
animplementationofanalgorithmisusedthatisnotprimarilyintendedfortimeseries
forecasting, and that internally performs a certain type of cross-validation. If series
areshort,thenk-foldCVshouldbeused,accountingadequatelyfornon-stationarities
andautocorrelationintheresiduals.
123

812 H.Hewamalageetal.
Fig.11 Flowchartforguidelinesondatapartitioning
4.2 Errormeasuresforforecastevaluation
Once the predictions are obtained from models, the next requirement is to compute
errors of the predictions to assess the model performance. Bias in predictions is a
commonissueandbecauseofthis,amodelcanbeveryaccurate(forecastsbeingvery
close to actuals), but consistently produce more overestimations than underestima-
tions,whichmaybeconcerningfromabusinessperspective.Therefore,forecastbias
iscalculatedwithasign,asopposedtoabsoluteerrors,sothatitindicatesthedirec-
tionoftheforecasterrors,eitherpositiveornegative.Forexample,scale-dependent
forecast bias can be assessed with the Mean Error (ME) as defined in Equation 4.
Here, y indicates the true value of the series, yˆ the forecast and n, the number of
t t
allavailable errors.Other scale-freeversions ofbiascan bedefined byscalingwith
respecttoappropriatescalingfactors,suchasactualvaluesoftheseries.
(cid:2)n (cid:3) (cid:4)
1
ME= y −yˆ (4)
t t
n
t=1
Two other popular and simple error measures used in a usual regression context
are MSE and MAE, which are both scale-dependent measures. Depending on the
business context, it can be a valid objective to forecast more accurately the series
thathavehigherscales,sincetheymaybereallytheobjectsofinterest.However,the
problem with scale-dependent measures is that, as soon as the scale of the series is
changed(forexampleconvertingfromonecurrencytoanother),thevalueoftheerror
measures change (Tashman 2000). On the other hand, for certain businesses, it is a
requirementtocompareerrorsacrossseries.Forexample,ifwesaythatMAEis10
for a particular series, we have no idea whether it is a good or a bad accuracy. For
aserieswithanaveragevalueof1000,thisamountofaccuracyispresumablyquite
good,whereasforanotherserieswithanaveragevalueof1,itisaverybadaccuracy.
Forthisreason,themeasuresneedtobescaledtoachievescale-independentmeasures,
andithasturnedouttobenexttoimpossibletodevelopascalingprocedurethatworks
forany typeofpossiblenon-stationarity andnon-normality inatimeseries.Hence,
awidevarietyoferrormeasureshavebeenproposedbyresearchersforthispurpose
overtheyears.Nevertheless,eventuallyweencounteraparticularconditionofthetime
seriesintherealworld,thatmakestheproposederrormeasurefail(Svetunkov2021).
123

Forecastevaluationfor... 813
Therearemanyoptionsavailableforscalingsuchasper-step,per-seriesorper-dataset
scaling.Scalingcanalsobedonebydividingeitherbyin-sampleorOOSvaluesof
thetimeseries.Apartfromdividingbycertainquantities,scalingcanalsobeachieved
throughlogtransformationoferrorsandrankingbasedonerrorsaswell.Thekeyto
selectingaparticularerrormeasureforforecastevaluationisthatitismathematically
andpracticallyrobustunderthegivendata.
Differentpointforecastevaluationmeasuresaretargetedtowardsoptimizingfora
specificstatisticofthedistribution.Forexample,measureswithsquaredbaseerrors
such as MSE and RMSE optimize for the mean whereas others with absolute value
baseerrorssuchasMAEandMeanAbsoluteScaledError(MASE)optimizeforthe
median.Althoughthemeanandmedianarethesameforasymmetricdistribution,that
doesnotholdforskeweddistributionsaswithintermittentseries.Thereexistnumerous
controversiesintheliteratureregardingthis.Petropoulos(2022)suggestthatitisnot
appropriatetoevaluatethesameforecastsusingmanydifferenterrormeasures,since
eachoneoptimizesforadifferentstatisticofthedistribution.AlsoaccordingtoKolassa
(2020),ifdifferentpointforecastevaluationmeasuresareconsidered,multiplepoint
forecastsforeachseriesandtimepointalsoneedtobecreated.Kolassa(2020)further
argues that, if the ultimate evaluation measure is, e.g., MAE which focuses on the
median of the distribution, it does not make sense to optimize the models using an
error measure like MSE (which accounts for the mean). It is more meaningful to
consider MAE also during model training as well. However, these arguments hold
onlyifitisnotanapplicationrequirementforthesameforecaststoperformgenerally
well under all these measures. Koutsandreas et al. (2021) have empirically shown
that,whenthesamplesizeislarge,awidevarietyoferrormeasuresagreeonthemost
consistently dominating methods as the best methods for that scenario. They have
also demonstrated that using two different error measures for optimizing and final
evaluationhasaninsignificantimpactonthefinalaccuracyofthemodels.Bermúdez
et al. (2006) have developed a fuzzy ETS model optimized via a multi-objective
functioncombiningthreeerrormeasuresMAPE,RMSEandMAE.Empiricalresults
havedemonstratedthatusingsuchamixoferrormeasuresinsteadofjustoneforthe
loss function leads to overall better, robust and generalisable results even when the
final evaluation is performed with just one of those measures. Fry and Lichtendahl
(2020)alsoassesstheirsameforecastsacrossnumerouserrormeasuresinabusiness
context.Evaluatingthesameforecastswithrespecttomanyevaluationmeasuresisa
formofsanitycheckingtoensurethatevenunderothermeasures(thoughnotdirectly
optimizingforthem),theforecastsstillperformwell.
Therearemanydifferentpointforecasterrormeasuresavailableintheforecasting
literature categorized based on 1) whether squared or absolute errors are used 2)
techniques used to make them scale-free and 3) the operator such as mean, median
usedtosummarizetheerrors(Koutsandreasetal.2021).Also,therearedifferentforms
of base errors involved with each of the error measures. In the following base error
definitions, y indicatesthetruevalueoftheseries, yˆ theforecastandT,thenumber
t t
oftimestepsinthetrainingregionofthetimeseries.
123

814 H.Hewamalageetal.
•
Scale-dependentbaseerror
= −yˆ
| e t y t | t   | (5) |
| ------- | --- | --- |
• Percentageerror
100e
| p = | t   | (6) |
| --- | --- | --- |
t
y t
• Percentageerror(In-samplescaling)-NamedasscaledError(sE)intheworkof
PetropoulosandKourentzes(2015).
(cid:5)t e
| p† =  |     | (7) |
| ----- | --- | --- |
| t 1 T |     |     |
t=1 y
T t
•
Percentageabsoluteerror(In-samplescaling)-NamedasscaledAbsoluteError
(sAE)intheworkofPetropoulosandKourentzes(2015).
|e |
| p‡ = (cid:5)t |     |     |
| ------------- | --- | --- |
(8)
| t 1 T |     |     |
| ----- | --- | --- |
t=1 y t
T
• Relativeerror-eb
inEq.(9)isthescale-dependentbaseerrorofthebenchmark
t
method.
e t
r = (9)
t eb
t
• Scalederror(usingMAEforthebenchmark)
e
| = t         |       |      |
| ----------- | ----- | ---- |
| q t (cid:5) |       | (10) |
| 1 T |y      | −y |  |      |
| T− t =2     | t t−1 |      |
1
• Scalederror(usingMSEforthebenchmark)
e2
| q† = t |     |     |
| ------ | --- | --- |
(cid:5) (11)
| t 1 T (y  | −y )2 |     |
| --------- | ----- | --- |
| T− t =2 t | t−1   |     |
1
• Logarithmicerror-lninEq.(12)definesthenaturallogarithm.
| l =ln(y +1)−ln(yˆ | +1) | (12) |
| ----------------- | --- | ---- |
| t t               | t   |      |
Thisismathematicallyequivalenttothefollowing.
(cid:6) (cid:7)
+1
y
| l =ln t |     | (13) |
| ------- | --- | ---- |
| t yˆ +1 |     |      |
t
123

Forecastevaluationfor... 815
• Rate-basederror(Kourentzes2014)
(cid:2)t
1
c = yˆ − y (14)
t t i
t
i=1
Table8containsthedefinitionsoferrormeasuresproposedintheliteratureusing
theaforementionedbaseerrors.InthedefinitionsofTable8,nindicatesthenumberof
allavailablebaseerrors,mdenotesthenumberoftimeseries,hindicatesthenumber
oftimestepsintheforecasthorizonandh ,thehorizonsizefortheith series.
i
Depending on each of the characteristics of time series as also stated in Sect. 2,
differenterrormeasuresdefinedinTable8arepreferableorshouldbeavoidedineach
case.Table9summarisesthisinformationandcanbeusedtochooseerrormeasures
undergivencharacteristicsofthedata.InTable9,thescalingcolumnindicatesthetype
ofscalingassociatedwitheacherrormeasurementionedinthepreviouscolumn.This
includesnoscaling,scalingbasedonactualvalues,scalingbasedonbenchmarkerrors
as well as the categorisation such as per-step, per-series and all-series (per-dataset)
scaling.The†signinTable9indicatesthattherespectiveerrormeasuresneedtobe
usedwithcautionunderthegivencircumstances.
In almost any scenario, when applying error measures that scale based on errors
fromabenchmarkmethod,therelativecompetenceofthebenchmarkmethodinthe
intendedforecasthorizonneedstobetakenintoaccount,sinceotherwisebenchmark
errorscanunnecessarilydrivetheoverallerrormeasurevalueshigherorlower.With
series having seasonality, percentage based measures may underestimate the errors
atpeaksheavily,duetodividingbylargeactualvalues(Wong2019;Kunst2016)or
overstatetheerrorsattroughs.Thiscanbeovercomebyscalingbasedonaggregated
values(perseries,all-series).Onserieshavingtrendsorstructuralbreakswithlevel
shifts,scale-freemeasureswhichcomputetheirscalebyaggregatingthevalues(actual
values or benchmark errors) at several time steps, tend to face problems. This is as
explainedbyChenetal.(2017),thattheerrorvaluesateachtimestepneedtocomply
with the scale of the series at each point. A scale computed by aggregating over
severaltimestepswhichincludesuchlevelshiftsmaynotalwaysbeagoodestimator
torepresentthescalingfactorsforallthetimestepsofsuchaseries.Alsoonseries
withexponentialtrends,logtransformationbasederrormeasuresgreatlyreducethe
impactoferrorsfrommodels.Unitrootsareverysimilartotrendsexceptthatmeasures
whichcomputeaper-stepscalingmaynotcapturepeakpointsonsuchseriessimilar
toseasonalseries.
Similarly,onserieshavingheteroscedasticitytoo,duetopotentialpeaksandtroughs
intheserieswhichmayhaveveryhighandlowvariances,measuressuchasMAPE
and RMSPE may have problems with capturing those points correctly. Apart from
that,logtransformationbasederrorscanreducetheimpactfromheteroscedasticityas
well.Especiallyonserieshavingstructuralbreaks,withmeasureswhichscalebased
on benchmark errors, when those errors are computed in-sample, they may not be
representative of the errors that happen OOS when the structural breaks are either
in the forecast horizon or the forecast origin. On intermittent series, measures that
optimize for the median are problematic since they consider constant zeros as the
123

| 816 |     |     |     |     |     |     | H.Hewamalageetal. |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- |
erehw,
)(cid:3)+5.0,(cid:3)+|
|
te|002
tyˆ|+|
)
|     |     |     |     |     |     |            | )          | | tyˆ|+| |         |
| --- | --- | --- | --- | --- | --- | ---------- | ---------- | -------- | ------- |
|     |     |     |     |     |     |            | | te|002 | |          |         |
|     |     |     |     |     |     | )2p(naidem | | tyˆ|+|   |          | ty|(xam |
te|002
|     | )2e(naidem   |             |           |              | )| )2p(     | t   |              | ty|            |                      |
| --- | ------------ | ----------- | --------- | ------------ | ----------- | --- | ------------ | -------------- | -------------------- |
|     | )2e( t       | )|          |           |              | tp|(naide t |     |              |                |                      |
|     | t            | te|(na 2e t | |         | )|           |             |     | ty|          | (naidem=EPAdMs | tluafedyb1.0=(cid:3) |
|     |              | 1=t         | te|       | tp|(         | (cid:2)n    | 1=t |              | (cid:2)n       | 1=t                  |
|     | (cid:2)n 1=t | (cid:12)n   |           |              |             |     | (            |                |                      |
|     |              |             | (cid:12)n | 1=t (cid:2)n | 1=t         |     | (cid:2)n 1=t |                |                      |
idem=EAdM (cid:8) (cid:9) (cid:9) (cid:10)n2 1(cid:10)=EPSMR n (cid:11) 1 n
1(cid:10)=ESMR n (cid:11) (cid:8) (cid:9) (cid:9) (cid:10)n m=EPAdM (cid:8) (cid:9) (cid:9) 1 n
| (cid:8)    | (cid:9) (cid:9) |        |       | 1 n |     | =EPSdMR |        |     | =EPAMsm |
| ---------- | --------------- | ------ | ----- | --- | --- | ------- | ------ | --- | ------- |
| noitinfieD | =ESdMR          | =ESMRG | =EAMG |     |     |         | =EPAMs |     |         |
=EPAM
|     |     |                                              |     |     |                                              |     | tsrfiEPAMs(rorrEegatnecrePetulosbAnaeMcirtemmyS | )EPAdMs(rorrEegatnecrePetulosbAnaideMcirtemmyS |     |
| --- | --- | -------------------------------------------- | --- | --- | -------------------------------------------- | --- | ----------------------------------------------- | ---------------------------------------------- | --- |
|     |     | sotetnyS,ESMRG(rorrEderauqSnaeMtooRcirtemoeG |     |     | dnarejoB,EPSMR(rorrEegatnecrePerauqSnaeMtooR |     |                                                 |                                                |     |
)EPSdMR(rorrEegatnecrePerauqSnaideMtooR
egatnecrePetulosbAnaeMcirtemmySdefiidoM
)EPAdM(rorrEegatnecrePetulosbAnaideM
)EAMG(rorrEetulosbAnaeMcirtemoeG )EPAM(rorrEegatnecrePetulosbAnaeM
)ESdMR(rorrEderauqSnaideMtooR
|     | )ESMR(rorrEderauqSnaeMtooR |                           |     |     |     |     | ))3991(sikadirkaMybdesoporp |     |                          |
| --- | -------------------------- | ------------------------- | --- | --- | --- | --- | --------------------------- | --- | ------------------------ |
|     |                            | )EAdM(rorrEetulosbAnaideM |     |     |     |     |                             |     | )7102niliuS,EPAMsm(rorrE |
erutaretilgnitsacerofehtnisnoitinfiederusaemrorrE
|     |     | )5002nalyoBdna |     |     |     | )0202draagdleM |     |     |     |
| --- | --- | -------------- | --- | --- | --- | -------------- | --- | --- | --- |
erusaemrorrE
tnednepeD-elacS
|     |     |     |     | desabserusaeM egatnecrePno |     |     |     |     |     |
| --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- |
serusaeM
yrogetaC
| 8elbaT |     |     |     |     | srorrE |     |     |     |     |
| ------ | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
123

Forecastevaluationfor... 817
aotsreferCerehw,
)|
ty|
|          |           |             | |                          | |               |                                |              |              |
| -------- | --------- | ----------- | -------------------------- | --------------- | ------------------------------ | ------------ | ------------ |
| )|te     |           |             | tyˆ|+| 2                   | e t ty|         | | 1+                           |              |              |
|          | ty        |             |                            | 1+              | te|                            |              |              |
|          |           | | te|       |                            | 1+              | h T                            |              |              |
| |(natcra |           |             | h                          | T h             | 1+ + = dlohserhtnoitasiraluger |              |              |
|          | |         | | 1+        | ty| +                      | = + = T         | h T t                          |              |              |
|          | te|       | ty|         | T                          | t(cid:5) T +    | (cid:5)T                       |              |              |
|          |           | + h T       | 1+ (cid:5)                 | t               | T =                            | )            |              |
|          |           | 1+ 1+ =     |                            | (cid:5)         | t 1 h                          | 2†p(         | )‡p(         |
| (cid:2)n | 1=t h     | (cid:5) T t | h T 1                      | h 1 h           | ,C(xam                         | )†p( t       | t | |        |
|          | +         | T + h T     | + =(cid:8) (cid:9) (cid:9) | (cid:10)=EPSMRW | 1 h                            | t            | te| ty|      |
|          | T         | = T =       | T t                        |                 |                                | (cid:2)n 1=t | (cid:2)n 1=t |
| 1        | n (cid:5) | t(cid:5) t  | (cid:5)                    |                 |                                | (cid:2)n 1=t | 1= 1=        |
1 n n
| noitinfieD =EPAAM |     |       | =EPAWs |     |       | 1 n 1 n | (cid:5) t(cid:5) n t |
| ----------------- | --- | ----- | ------ | --- | ----- | ------- | -------------------- |
|                   |     | =EPAW |        |     | =EATR | =ESMs   | =EAMs                |
=EMs
=DN
|     |     |     |     | )EPSMRW(rorrEegatnecrePderauqSnaeMtooRdethgieW |     |     | elacsehT-)0202.latesanilaS,DN(noitaiveDdezilamroN |
| --- | --- | --- | --- | ---------------------------------------------- | --- | --- | ------------------------------------------------- |
)EPAWs(rorrEegatnecrePetulosbAdethgieWcirtemmyS
,EPAAM(rorrEegatnecrePetulosbAtnegnatcrAnaeM ynamgnisuyllabolgdetupmocsirotanimonedehtni
|     |     |     |     |     |     | seztneruoKdnasoluoporteP,EMs(rorrEnaeMdelacS | dnasoluoporteP,EAMs(rorrEetulosbAnaeMdelacS |
| --- | --- | --- | --- | --- | --- | -------------------------------------------- | ------------------------------------------- |
dnasoluoporteP,ESMs(rorrEderauqSnaeMdelacS
)EPAW(rorrEegatnecrePetulosbAdethgieW
)EATR(rorrEetulosbAlatoTevitaleR
)6102miKdnamiK
|     |     |     |     |     |     | )5102seztneruoK | )5102seztneruoK |
| --- | --- | --- | --- | --- | --- | --------------- | --------------- |
erusaemrorrE
)5102 .seires
deunitnoc
yrogetaC
8elbaT
123

818 H.Hewamalageetal.
deunitnoc
8elbaT
noitinfieD
erusaemrorrE
yrogetaC
(cid:11) (cid:5)
)2
t e( 1= n t (cid:5) 1 n =ESMRN
sanilaS,ESMRN(rorrEderauqSnaeMtooRdezilamroN
)|
ty|( 1= n t 1 n
detupmocsirotanimonedehtnielacsehT-)0202.late
.seiresynamgnisuyllabolg
(cid:2)n 1 )| tr|( =EARM
)EARM(rorrEetulosbAevitaleRnaeM
desabserusaeM
n 1=t
evitaleRno
srorrE
)| tr|(naide (cid:8) m=EARdM
)EARdM(rorrEetulosbAevitaleRnaideM
(cid:9) (cid:2)n (cid:9) )2r( 1(cid:10)=ESRMR
)ESRMR(srorrEderauqSevitaleRnaeMtooR
t n 1=t (cid:8) (cid:9) (cid:12)n (cid:9) | tr| (cid:10)n =EARMG
)EARMG(rorrEetaulosbAevitaleRnaeMcirtemoeG
1= (cid:8)t (cid:9) (cid:12)n (cid:9) 2r (cid:10)n2 =ESMRGR
)ESMRGR(rorrEderauqSnaeMtooRcirtemoeGevitaleR
t 1=t EAM
ehtfoEAMehtsibEAMerehw,
=EAMleR
)EAMleR(rorrEetulosbAnaeMevitaleR
serusaeMevitaleR
bEAM dohtemkramhcneb ESM
ehtfoESMehtsibESMerehw,
=ESMleR
)ESMleR(rorrEderauqSnaeMevitaleR
bESM dohtemkramhcneb
123

Forecastevaluationfor... 819
deunitnoc
8elbaT
noitinfieD
erusaemrorrE
yrogetaC
(cid:13)
ESM
ehtfoESMehtsibESMerehw,
=ESMRleR
)ESMRleR(rorrEderauqSnaeMtooRevitaleR
bESM dohtemkramhcneb
(cid:11)
(cid:5)
2 t e
1=
n t
(cid:5)
(cid:11)
=ESR
)8102.lateiaL,ESR(rorrEderauqSevitaleRtooR
2)y¯−
ty(
1=
n t
1 (cid:5)
⎞
(cid:17)
(cid:16)
⎛
iEAMerehw,
ih1=
m i
⎠
ih
iEAM
(cid:12)m
⎝=EAMleRgvA
,EAMleRgvA(rorrEetulosbAnaeMevitaleRegarevA
b
b iEAM
1=i
)3102sedliFdnaoknedyvaD
seireshtiehtrofdohtemkramhcnebehtfoEAMehtsi
(cid:2)n
1
tq
=ESAM
)ESAM(rorrEdelacSetulosbAnaeM
desabserusaeM
n
1=t
delacSno
-dnyH(srorrE
dnanam
)6002relheoK
) tq(naide
(cid:8) m=ESAdM
)ESAdM(rorrEdelacSetulosbAnaideM
(cid:9)
(cid:2)n
(cid:9)
†q
1(cid:10)=ESSMR
sikadirkaM,ESSMR(rorrEdelacSderauqSnaeMtooR
t
n
1=t
)2202.late
123

| 820 |     |     |     |     | H.Hewamalageetal. |     |
| --- | --- | --- | --- | --- | ----------------- | --- |
sibEAMerehw,)}
|     |     |     |     | otdengissathgiewasi |     | ehtfonaemehtsi |
| --- | --- | --- | --- | ------------------- | --- | -------------- |
ehtsiXdnarorreehtsiEerehw,)}X>E{I(naem001
,)
2)
thgiewasi
) ¯ˆy− i
¯ˆy− i
tiyˆ(2)
tiyˆ()
bEAM<EAM{I(naem001=)EAM(BP
|                             |                         | t               |                               |                |                       | ¯ˆydnaiseiresfonaemehtsi i |
| --------------------------- | ----------------------- | --------------- | ----------------------------- | -------------- | --------------------- | -------------------------- |
| .dohtemkramhcnebehtfoEAMeht |                         | werehw,         |                               |                | ¯y− i                 | ¯y− i                      |
|                             |                         |                 | tpetsemittarorreehtotdengissa | t              |                       |                            |
|                             |                         |                 |                               | werehw,        | tiy(                  | tiy(                       |
|                             |                         | 2               |                               |                | 1+                    | 1+                         |
|                             |                         | l t w t         |                               |                | h                     | h                          |
|                             |                         | w t             |                               |                | + = T                 | + T                        |
|                             |                         | 1=t             |                               | |              | tpetsemittarorreeht T | T = iseiresrofsnoitciderp  |
|                             |                         | 1= n            |                               | te             | (cid:5) t             | (cid:5) t                  |
|                             | tl                      | n (cid:5)t      |                               | | w            | t                     |                            |
|                             | (cid:2)n 1=t            | (cid:5)(cid:13) |                               | w t            | 1=t (cid:11)(         |                            |
|                             |                         |                 |                               | | =(cid:5) 1 n | (cid:2)m              | 1=i                        |
|                             | 1(cid:10)=ELSMR n       | =ELSMRWN        | 2                             | tc| n t        |                       |                            |
|                             | (cid:8) (cid:9) (cid:9) |                 | c t                           | (cid:5)1=t     |                       |                            |
|                             |                         |                 | (cid:2)n 1=t                  | (cid:2)n       | 1                     | m                          |
| noitinfieD                  |                         |                 |                               | =EAMW          |                       | ¯yerehw i                  |
|                             | nigram                  |                 |                               | =RAM           | =RROC                 |                            |
=RSM
dnarejoB,ELSMR(rorrEcimhtiragoLderauqSnaeMtooR
)6002relheoKdnanamdnyH,erocSBP(retteBegatnecreP a)spetsemitdnaseiresssorca(semitynamwohstnuoC- tistroperdnakramhcnebehtnahtrettebsidohtemnevig )8102.lateiaL,RROC(tneicfifeoCnoitalerroClaciripmE
)9102(gnoW-XnigraMroftnevElacitirCfoegatnecreP
cimhtiragoLderauqSnaeMtooRdethgieWdezilamroN
stsaceroffoegatnecrepehterusaemotsihtdesoporp
dnarejoB,EAMW(rorrEetulosbAnaeMdethgieW
|     | .nigramanahtrehgihsirorrefoeulavehterehw | )0202draagdleMdnarejoB,ELSMRWN(rorrE |     |     |     |     |
| --- | ---------------------------------------- | ------------------------------------ | --- | --- | --- | --- |
)RAM(etaRetulosbAnaeM
)RSM(etaRderauqSnaeM
|     | )0202draagdleM |     |     |     | )0202draagdleM |     |
| --- | -------------- | --- | --- | --- | -------------- | --- |
.egatnecrepasa
erusaemrorrE
seztneruoK(serus
deunitnoc gnitnuoC/sknaR
noitamrofsnarT -aeMdesab-etaR
| desabserusaeM | desabserusaeM |     |     |     |     |     |
| ------------- | ------------- | --- | --- | --- | --- | --- |
rorrErehtO serusaeM
yrogetaC
| 8elbaT |     |     |     | )4102 |     |     |
| ------ | --- | --- | --- | ----- | --- | --- |
| no     | no  |     |     |       |     |     |
123

Forecastevaluationfor... 821
best prediction. Measures with per-step scaling based on actual values can also be
problematiconintermittentseriesduetodividingbyzero.Thiscanbeaddressedby
usingper-seriesscaling,butcanagainhaveissuesifalltimestepshavezerovalues.
Withmeasuresthatscalebasedonbenchmarkerrorsonintermittentseries,itcanbe
problematicwhenbenchmarkerrorshaveprefectpredictions(zeroerrors),forexample
withthenaïvemethodgivingexactzerosonzeroactualvalues.Withrespecttooutliers,
some applications may be interested in capturing them whereas others may want to
berobustagainstthem.Toberobustagainstoutliers,geometricmeanormediancan
be used as the summary operator instead of the mean. Absolute base errors need to
beusedinsteadofsquaredbaseerrorstoberobustagainstoutliers.Measureswhich
scale based on per-step or per-series quantities may be heavily affected by outliers.
Similarly,withmeasuresthatscalebasedonbenchmarkerrors,iftheforecastofthe
benchmarkinthehorizonisheavilyaffectedbytheoutliersinthetrainingregionof
theseries,itcanbeproblematic.
TheflowchartinFig.12providesfurthersupportforforecastevaluationmeasure
selectionbasedonuserrequirementsandothercharacteristicsinthedata.InFig.12,
the error measures selected to be used with outlier time series are in the context of
beingrobustagainstoutliers,notcapturingthem.
4.3 Statisticaltestsforsignificance
Whileforecastevaluationmeasuresarecriticaltoseetherelativeperformanceofthe
methods and select the best ones from their rankings, they do not give information
regarding the statistical significance of the differences between these methods; i.e.
whether better performance of the best method is just by chance on this sample of
the series or whether it is likely to dominate all the methods significantly in other
samplesofthedata.Theselectedbestmethodcouldbetheonlyonetouse,orthere
could be other methods that are not significantly different from the best that can
be used interchangeably due to their other preferable properties such as simplicity,
computationalefficiencyetc.
There are many ways of performing statistical significance tests reported in the
literature.TheDiebold-Marianotest(DieboldandMariano2002)andtheWilcoxon
rank-sumtest(MannandWhitney1947)arebothdesignedforcomparingonlybetween
twocompetingforecasts,notnecessarilymethodsormodels.However,theDiebold-
Mariano testis designed specifically for time series and parametric, meaning that it
has the assumption of normality of the data whereas the Wilcoxon test is a generic
non-parametric testbasedontheranks ofthemethods.Duetoconsidering ranksof
methodsforeachseriesseparately,theerrormeasuresuseddonotnecessarilyhaveto
bescale-free.TheGiacomini-Whitetest(GiacominiandWhite2006)againisbasedon
thecomparisonoftwoforecasts,withthepotentialtoassesstheconditionalpredictive
ability (CPA), a concept that refers to conditioning the choice of a potential future
stateoftheeconomy,animportantconceptformacroeconomicforecastingofasmall
numberofseries.AcontinuationinthislineofresearchisworkbyLietal.(2022b)that
focusesonconditionalsuperiorpredictiveability,inregardstoabenchmarkmethod
and time series with general serial dependence. It should be noted that many of the
123

822 H.Hewamalageetal.
scitsiretcarahcseiresemittnereffidnodesabnoitaulavetsaceroflanfirofserusaemrorregnitcelesroftsilkcehC
9elbaT
gnilacS
rorrE
sreiltuO
ecnettimretnI
)secnereffiD
elacShtiW(skaerB
larutcurtS
yticitsadecsoreteH
stooRtinU
dnerT
ytilanosaeS
yranoitatS
serusaeM
/raeniL(
)tnuoC
tsaceroF
gniniarT
tsaceroF
).pxE
0>>(ataD
nigirO
noigeR
noziroH
enoN
ESMR
✗
✓
✓
✓
✓
✓
✓
✓
✓
✓
EAM
✓
✗
✓
✓
✓
✓
✓
✓
✓
✓
lautcA
rePSOO
EPAM
✗
✗
✓
✓
✓
†✓
†✓
✓
✗
✓
seulaV
petS
EPSMR
✗
✗
✓
✓
✓
†✓
†✓
✓
✗
✓
EPAMs
✓
✗
✓
✓
✓
✓
✓
✓
✓
✓
EPAMsm
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
rePSOO
EPAW
✗
✗
✓
✓
✗
✓
✗
✗
✓
✓
seireS
EPSMRW
✗
†✓
✓
✓
✗
✓
✗
✗
✓
✓
elpmaS-nI
EAMs
✗
✗
✗
✗
✗
✓
✗
✗
✓
✓
seireSreP
ESMs
✗
†✓
✗
✗
✗
✓
✗
✗
✓
✓
llASOO
DN
✓
✗
✓
✓
✓
✓
✓
✓
✓
✓
seireS
ESMRN
✗
✓
✓
✓
✓
✓
✓
✓
✓
✓
123

Forecastevaluationfor... 823
kramhcneB
srorrE
|         |        | elpmaS-nI | elpmaS-nI           |
| ------- | ------ | --------- | ------------------- |
|         | rePSOO | rePSOO    | seireSreP seireSllA |
| gnilacS | petS   | seireS    |                     |
enoNsnoitamrofsnarThtiwserusaeM
serusaeMevitaleR
| serusaeM | EARdM EARMG | ESRMR | ESSMR |
| -------- | ----------- | ----- | ----- |
|          | EARM        | ESAM  |       |
rorrEsreiltuOecnettimretnI)secnereffiDelacShtiW(skaerBlarutcurtSyticitsadecsoreteH
|     | †✓ †✓ †✓ | †✓      |        |
| --- | -------- | ------- | ------ |
|     |          | ✗ ✓     | ✗ ✓ ✓  |
|     | ✗ ✗ ✗    | †✓ †✓ ✗ | †✓ ✓ ✓ |
tsaceroF
nigirO
|     | ✓ ✓ ✓ | ✓ ✓ ✗ | ✗ ✓ ✓ |
| --- | ----- | ----- | ----- |
gniniarT noigeR
|     | †✓ †✓ †✓ | †✓ †✓ †✓ | †✓ ✓ ✓ |
| --- | -------- | -------- | ------ |
tsaceroF noziroH
|     | ✓ ✓ ✓ | ✓ ✓ | ✓ ✓ |
| --- | ----- | --- | --- |
|     |       | ✗   | ✗   |
†✓
|     | ✓ ✓ ✓ | ✓ ✓ ✓ | ✓ ✓ |
| --- | ----- | ----- | --- |
stooRtinU
|     | ✗ ✗ ✗ | ✗ ✗ ✓ | ✓ ✓ ✓ |
| --- | ----- | ----- | ----- |
/raeniL(
dnerTytilanosaeS ).pxE
|     | ✗ ✗ ✗    | ✗ ✗ ✓    | ✓ ✓ †✓ |
| --- | -------- | -------- | ------ |
|     | †✓ †✓ †✓ | †✓ †✓ †✓ | †✓ †✓  |
✓
deunitnoc
yranoitatS 0>>(ataD
9elbaT )tnuoC
|     | †✓ †✓ †✓ | †✓ †✓ †✓ | †✓ †✓ |
| --- | -------- | -------- | ----- |
✓
123

824 H.Hewamalageetal.
Fig.12 Flowchartforforecasterrormeasureselection
mentioned comparison tests are per-se designed for comparing two forecasts, and a
multipletestingofmorethantworequiresacorrectionformultiplehypothesistesting,
suchas,e.g.,aBonferronicorrection.
There are other techniques developed to perform comparison within a group of
methods(morethan2)aswell.Meansoferrordistributionsfromdifferentmethods
can be used to compare the mean performance of the methods. The F-test and the
t-test are statistical tests in this respect. They both have parametric assumptions for
123

Forecastevaluationfor... 825
Fig.13 AnexampleofaCDdiagramtovisualizethesignificanceofthedifferencesbetweenanumberof
competingmethods.ThebestthreemethodsA,BandCarenotsignificantlydifferentfromeachother.On
theotherhand,methodsD,EandFaresignificantlyworsethanthosethreemethods.Theamountofdata
hasnotbeenenoughtocheckwhethermethodEissignificantlybetterthanmethodDorworsethanmethod
F
the means of the error distributions, that they need to follow a normal distribution.
Although,accordingtotheCentralLimitTheorem,thiscouldholdformeasuressuch
asMSE,MAEetc.,forasufficientlylargerandomsample(ofsizen ≥ 30),itdoes
notholdfore.g.,RMSE,sincetherootofanormallydistributedvariableisfollowing
achi-squaredistribution,whichisclosetonormalitybutnotequivalent.Ontheother
hand,theFriedmantest(Friedman1937, 1939, 1940)isanon-parametricstatistical
testthatcanbeusedtodetectsignificancebetweenmultiplecompetingmethods,using
theranksofthemethodsaccordingtomeanerrors.
The Friedman test is usually followed by a post-hoc test, when the null hypoth-
esis which states that “there are no significant differences between the methods”,
is rejected. There are different types of post-hoc tests, for example, the Hochberg
procedure (Hochberg 1988), the Holm process (Holm 1979), the Bonferroni-Dunn
procedure(Dunn1961),theNemenyimethod(Nemenyi1963),theMultipleCompar-
isons with the Best (MCB) method (practically equivalent to the Nemenyi method)
ortheMultipleComparisonswiththeMean(ANOM)method(Halperinetal.1955),
and others. In general, the ANOM test holds less value in practice since it is more
usefultofindwhichmethodsarenotsignificantlydifferentfromthebest,thanfrom
some averagely performing method overall. The Nemenyi method works by defin-
ing confidence bounds, in terms of a Critical Distance (CD) around the mean ranks
of the methods to identify which methods have overlapping confidence bounds and
whichdonot.AsDemšar(2006)suggests,ifallthecomparisonsaretobeperformed
againstonecontrolmethodasopposedtoeachmethodagainsteachother,procedures
suchasBonferroni-DunnandHochberg’sarebetterovertheNemenyitest.Once,the
quantitativeresultsforthesignificanceofthedifferencesareobtainedusinganyofthe
aforementionedmethods,theycanbevisualizedusingCDdiagrams(Demšar2006).
In general, in these diagrams, a horizontal axis reports the average ranks of all the
methods. Groups of methods that are not significantly different from each other are
connectedusingblackbars.ThisisillustratedinFig.13,anexampleCDdiagram.
123

826 H.Hewamalageetal.
Fig.14 Flowchartforstatisticaltestsselectiontomeasuresignificanceofmodeldifferences
Whenperformingsignificancetesting,theamountofdataincludedheavilyimpacts
theresultsofthesignificancetests.Forexample,withaveryhighnumberofseries,
the CD is usually very low, producing significant results for even small differences
betweenmodels.Thismeansthattheresultsaremorereliable,thateventheslightest
differences between models encountered for such a large amount of data are statis-
tically highly significant. On the other hand, it also depends on the number and the
relative performance of thesetofmodels included inthecomparison. For example,
having more and more poorly performing methods in the group may tend towards
making the CD larger, thus making other intermediate methods have no significant
differencefromthebest.TheflowchartinFig.14summarisesthedecisionmaking
process in selecting a statistical test to measure significance of differences between
models.
5 Conclusions
Model evaluation, just as in any other domain, is a crucial step in forecasting. In
othermajorfieldssuchasregression,classification,thereexistestablishedtechniques
that are the standard best practices. On the contrary, in the domain of forecasting,
123

Forecastevaluationfor... 827
evaluationremainsamuchmorecomplextask.Thegeneraltrendintheliteraturehas
beentoproposenewmethodologiestoaddresspitfallsassociatedwiththepreviously
introduced. Nevertheless, for example with the forecast evaluation measures, to the
best of our knowledge, all the introduced measures thus far can break under given
certaincharacteristics/non-stationaritiesofthetimeseries.GeneralMLpractitioners
andDataScientistsnewtothefieldofforecastingareoftennotawareoftheseissues.
Consequently,aswedemonstratethroughourwork,forecastevaluationpracticesused
by many works even published at top-tier venues in the ML domain can be flawed.
All of this is a consequence of the lack of established best practices and guidelines
for the different steps of the forecast evaluation process. Therefore, to support the
MLcommunityinthisaspect,weprovideacompilationofcommonpitfallsandbest
practice guidelines related to forecast evaluation. The key set of guidelines that we
developareasfollows.
• To claim the competitiveness of the proposed methods, they need to be bench-
markedonsufficientlylargeamountsofdatasets.
• Itisalwaysimportanttocomparemodelsagainsttherightandthesimplestbench-
markssuchasthenaïveandtheseasonalnaïve.
• Using forecast plots can be misleading; making decisions purely based on the
visualappealonforecastplotsisnotadvisable.
• Dataleakageneedstobeavoidedexplicitlyinrollingoriginevaluationandother
datapre-processingtaskssuchassmoothing,decompositionandnormalisationof
theseries.
• Ifenoughdataareavailable,tsCVistheprocedureofchoice.Also,formodelswith
a continuous state such as RNNs and ETS where the temporal order of the data
isimportant,tsCVmaybetheonlyapplicablevalidationstrategy.k-foldCVisa
validandadataefficientstrategyofdatapartitioningforforecastmodelvalidation
withpureARbasedsetups,whenthemodelsdonotunderfitthedata(whichcanbe
detectedwithatestforserialcorrelationintheresiduals,suchastheLjung-Box
test). As such, we advise this procedure especially for short series where tsCV
leadstotestsetsthataretoosmall.However,ifthemodelsunderfit,itisadvisable
toimprovethemodelsfirstbeforeusinganyCVtechnique.
• Thereisnosinglegloballyacceptedevaluationmeasureforallscenarios.Itdepends
onthecharacteristicsofthedataassummarizedinTable9.
• Whenusingstatisticaltestingforsignificanceofthedifferencesbetweenmodels,
balancingthediversityofthecomparedmodelsagainstthenumberofdatapoints
isimportanttoavoidspuriousstatisticalsimilarity/differencebetweenmodels.
While the literature on evaluation measures is quite extensive, the exact errors
(squared/absolute),summarisationoperators(mean/median/geometricmean),typeof
scalingtouse(global/per-series/per-step/,in-sample/OOS,relative/percentage)differ
basedontheuserexpectations,businessutilityandthecharacteristicsoftheunderlying
timeseries.Duetothelackofproperknowledgeinforecastevaluation,MLresearch
intheliteraturethusfarhasofteneitherstruggledtodemonstratethecompetitiveness
of its models or arrived at spurious conclusions. It is our objective that this effort
encouragesbetterandcorrectforecastevaluationpracticeswithintheMLcommunity.
Asapotentialavenueforfurtherworkespeciallywithrespecttoevaluationmeasures,
123

828 H.Hewamalageetal.
itwouldbeusefultodesigncombinationbasedevaluationmeasuresforforecasting,
similar to the Huber loss for model training, which is a combination of the MAE
andtheRMSE.Thesetypesofmeasurescanbequiterobust,combiningthestrengths
of both measures while minimising the potential disadvantages associated with the
individualmeasures.
Acknowledgements ThisworkwasdoneaspartofthePhDdegreeofHansikaHewamalageattheFaculty
ofIT,MonashUniversity.ThisresearchwassupportedbytheAustralianResearchCouncilundergrant
DE190100045,aFacebookStatisticsforImprovingInsightsandDecisionsresearchawardandMonash
UniversityGraduateResearchfunding.WewouldliketothanktwoanonymousreviewersandtheAssociate
Editorwhosecommentshaveleadtoconsiderableimprovementsofthepaper.
OpenAccess ThisarticleislicensedunderaCreativeCommonsAttribution4.0InternationalLicense,which
permitsuse,sharing,adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreativeCommonslicence,
andindicateifchangesweremade.Theimagesorotherthirdpartymaterialinthisarticleareincluded
inthearticle’sCreativeCommonslicence,unlessindicatedotherwiseinacreditlinetothematerial.If
materialisnotincludedinthearticle’sCreativeCommonslicenceandyourintendeduseisnotpermitted
bystatutoryregulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfromthe
copyrightholder.Toviewacopyofthislicence,visithttp://creativecommons.org/licenses/by/4.0/.
References
ArmstrongJ(2001)Evaluatingforecastingmethods.In:ArmstrongJS(ed)Principlesofforecasting:a
handbookforresearchersandpractitioners.KluwerAcademicPublishers,Norwell,MA
ArmstrongJS,GrohmanMC(1972)Acomparativestudyofmethodsforlong-rangemarketforecasting.
ManagSci19(2):211–221
ArnottR,HarveyCR,MarkowitzH(2019)Abacktestingprotocolintheeraofmachinelearning.JFinanc
DataSci
BagnallA,LinesJ,BostromA,LargeJ,KeoghE(2016)Thegreattimeseriesclassificationbakeoff:areview
andexperimentalevaluationofrecentalgorithmicadvances.DataMinKnowlDisc31(3):606–660
BalestrieroR,PesentiJ,LeCunY(2021)Learninginhighdimensionalwaysamountstoextrapolation.
arXivpreprintarXiv:2110.09485
BellF,SmylS,(2018)Forecastingatuber:anintroduction.https://eng.uber.com/forecasting-introduction/
BergerD,ChaboudA,HjalmarssonE(2009)Whatdrivesvolatilitypersistenceintheforeignexchange
market?JFinancEcon94(2):192–213
BergmeirC,HyndmanRJ,KooB(2018)Anoteonthevalidityofcross-validationforevaluatingautore-
gressivetimeseriesprediction.ComputStatDataAnal120:70–83
BermúdezJD,SeguraJV,VercherE(2006)Adecisionsupportsystemmethodologyforforecastingoftime
seriesbasedonsoftcomputing.ComputStatDataAnal51(1):177–191
BojerCS,MeldgaardJP(2020)Kaggleforecastingcompetitions:anoverlookedlearningopportunity.Int
JForecast
BrownleeJ(2020)Datapreparationformachinelearning:datacleaning,featureselection,anddatatrans-
formsinPython.MachLearnMastery
CerqueiraV,TorgoL,MozeticˇI(2020)Evaluatingtimeseriesforecastingmodels:anempiricalstudyon
performanceestimationmethods.MachLearn109(11):1997–2028
ChalluC,OlivaresK.G,OreshkinBN,Garza,F,Mergenthaler-CansecoM,DubrawskiA(2022)N-hits:
neuralhierarchicalinterpolationfortimeseriesforecasting.arXiv:2201.12886
ChenC,TwycrossJ,GaribaldiJM(2017)Anewaccuracymeasurebasedonboundedrelativeerrorfor
timeseriesforecasting.PLoSONE12(3):e0174202
CoxD,MillerH(1965)TheTheoryofStochasticProcesses
Cui Y, Xie J, Zheng K (2021) Historical inertia: a neglected but powerful baseline for long sequence
time-seriesforecasting.In:Proceedingsofthe30thACMInternationalConferenceonInformation&
123

Forecastevaluationfor... 829
KnowledgeManagement.CIKM’21.AssociationforComputingMachinery,NewYork,NY,USA,
pp2965-2969
DavydenkoA,FildesR(2013)Measuringforecastingaccuracy:Thecaseofjudgmentaladjustmentsto
SKU-leveldemandforecasts.IntJForecast29(3):510–522
DemšarJ(2006)Statisticalcomparisonsofclassifiersovermultipledatasets.JMachLearnRes7(1):1–30
DieboldFX,MarianoRS(2002)Comparingpredictiveaccuracy.JBusEconStat20(1):134–144
DitzlerG,RoveriM,AlippiC,PolikarR(2015)Learninginnonstationaryenvironments:asurvey.IEEE
ComputIntellMag10(4):12–25
DunnOJ(1961)Multiplecomparisonsamongmeans.JAmStatAssoc56(293):52–64
DuD,SuB,WeiZ(2022)Preformer:predictivetransformerwithmulti-scalesegment-wisecorrelations
forlong-termtimeseriesforecasting.arXiv:2202.11356
DuY,WangJ,FengW,PanS,QinT,XuR,WangC(2021)Adarnn:adaptivelearningandforecastingof
timeseries.In:Proceedingsofthe30thACMInternationalConferenceonInformation&Knowledge
Management.CIKM’21.AssociationforComputingMachinery,NewYork,NY,USA,pp402-411
EngleRF(2003)Riskandvolatility:econometricmodelsandfinancialpractice.NobelLect.https://www.
nobelprize.org/uploads/2018/06/engle-lecture.pdf
FamaEF(1970)Efficientcapitalmarkets:areviewoftheoryandempiricalwork.JFinanc25(2):383–417
FawazHI,ForestierG,WeberJ,IdoumgharL,MullerP-A(2019)Deeplearningfortimeseriesclassification:
areview.DataMinKnowlDiscov33(4):917–963
Friedman M (1937) The use of ranks to avoid the assumption of normality implicit in the analysis of
variance.JAmStatAssoc32(200):675–701
FriedmanM(1939)Acorrection:theuseofrankstoavoidtheassumptionofnormalityimplicitinthe
analysisofvariance.JAmStatAssoc34(205):109–109
FriedmanM(1940)Acomparisonofalternativetestsofsignificancefortheproblemofmrankings.Ann
MathStat11(1):86–92
FryC,LichtendahlC(2020)Googlepractitionersession.In:40thInternationalSymposiumonForecasting.
https://www.youtube.com/watch?v=FoUX-muLlB4&t=3007s
Gama J, Sebastiao R, Rodrigues PP (2013) On evaluating stream learning algorithms. Mach Learn
90(3):317–346
GamaJ.a,ŽliobaitundefinedI,BifetA,PechenizkiyM,BouchachiaA(2014)Asurveyonconceptdrift
adaptation.ACMComputSurv46(4)
GhomeshiH,GaberMM,KovalchukY(2019)EACD:evolutionaryadaptationtoconceptdriftsindata
streams.DataMinKnowlDisc33(3):663–694
GiacominiR,WhiteH(2006)Testsofconditionalpredictiveability.Econometrica74(6):1545–1578
GodahewaR,BandaraK,WebbGI,SmylS,BergmeirC(2021)Ensemblesoflocalisedmodelsfortime
seriesforecasting.KnowlBasedSyst233:107518
GodfreyLB,GashlerMS(2018)Neuraldecompositionoftime-seriesdataforeffectivegeneralization.
IEEETransNeuralNetwLearnSyst29(7):2973–2985
GujaratiDN(2021)Essentialsofeconometrics.SagePublications,Christchurch,NewZealand
GuoY,ZhangS,YangJ,YuG,WangY(2022)Dualmemoryscalenetworkformulti-steptimeseries
forecastinginthermalenvironmentofaquaculturefacility:acasestudyofrecirculatingaquaculture
watertemperature.ExpertSystAppl208:118218
HalperinM,GreenhouseSW,CornfieldJ,ZalokarJ(1955)Tablesofpercentagepointsforthestudentized
maximumabsolutedeviateinnormalsamples.JAmStatAssoc50(269):185–195
HämäläinenW,WebbGI,(2019)Atutorialonstatisticallysoundpatterndiscovery.DataMinKnowl
Discov33(2):325–377
HannunA,GuoC,vanderMaatenL(2021)Measuringdataleakageinmachine-learningmodelswithfisher
information.In:deCampos,C,Maathuis,MH(eds)ProceedingsoftheThirty-SeventhConference
onUncertaintyinArtificialIntelligence.vol161,pp760–770
HastieT,TibshiraniR,FriedmanJ(2009)Theelementsofstatisticallearning:datamining,inference,and
prediction.Springer,NewYork,NY
HewamalageH,BergmeirC,BandaraK(2021)Recurrentneuralnetworksfortimeseriesforecasting:
currentstatusandfuturedirections.IntJForecast37(1):388–427
HochbergY(1988)Asharperbonferroniprocedureformultipletestsofsignificance.Biometrika75(4):800–
802
HolmS(1979)Asimplesequentiallyrejectivemultipletestprocedure.ScandJStat6(2):65–70
123

830 H.Hewamalageetal.
HyndmanRJ,AthanasopoulosG(2018)Forecasting:principlesandPractice,2ndedn.OTexts.https://
otexts.com/fpp2/
HyndmanRJ,KoehlerAB(2006)Anotherlookatmeasuresofforecastaccuracy.IntJForecast22(4):679–
688
HyndmanR,KangY,TalagalaT,WangE,YangY(2019)tsfeatures:timeseriesfeatureextraction.R
packageversion1.0.0.https://pkg.robjhyndman.com/tsfeatures/
IkonomovskaE,GamaJ,DžeroskiS(2010)Learningmodeltreesfromevolvingdatastreams.DataMin
KnowlDiscov23(1):128–168
KaufmanS,RossetS,PerlichC,StitelmanO(2012)Leakageindatamining:Formulation,detection,and
avoidance.ACMTransKnowlDiscovData6(4):1–21
KimS,KimH(2016)Anewmetricofabsolutepercentageerrorforintermittentdemandforecasts.IntJ
Forecast32(3):669–679
KolassaS(2020)Whythebestpointforecastdependsontheerrororaccuracymeasure.IntJForecast
36(1):208–211
KourentzesN(2014)Onintermittentdemandmodeloptimisationandselection.IntJProdEcon156:180–
190
KoutsandreasD,SpiliotisE,PetropoulosF,AssimakopoulosV(2021)Aasures.JOperResSoc,1–18
KunstR(2016)Visualizationofdistancemeasuresimpliedbyforecastevaluationcriteria.In:Interna-
tionalSymposiumonForecasting2016.https://forecasters.org/wp-content/uploads/gravity_forms/7-
621289a708af3e7af65a7cd487aee6eb/2016/07/Kunst_Robert_ISF2016.pdf
KurangaC,PillayN(2022)Acomparativestudyofnonlinearregressionandautoregressivetechniquesin
hybridwithparticleswarmoptimizationfortime-seriesforecasting.ExpertSystAppl190:116163
LaiG,ChangW.-C,YangY,LiuH(2018)Modelinglong-andshort-termtemporalpatternswithdeep
neuralnetworks.In:The41stInternationalACMSIGIRConferenceonResearch&Developmentin
InformationRetrieval.SIGIR’18.AssociationforComputingMachinery,NewYork,NY,USA,pp
95-104
LiJ,LiaoZ,QuaedvliegR(2022)Conditionalsuperiorpredictiveability.RevEconStud89(2):843–875
LiB,DuS,LiT,HuJ,JiaZ(2022a)Draformer:differentiallyreconstructedattentiontransformerfor
time-seriesforecasting.arXiv:2206.05495
LinG,LinA,CaoJ(2021)Multidimensionalknnalgorithmbasedoneemdandcomplexitymeasuresin
financialtimeseriesforecasting.ExpertSystAppl168:114443
LiuS,JiH,WangMC(2020)Nonpoolingconvolutionalneuralnetworkforecastingforseasonaltimeseries
withtrends.IEEETransNeuralNetwLearnSyst31(8):2879–2888
LiuQ,LongL,PengH,WangJ,YangQ,SongX,Riscos-NúñezA,Pérez-JiménezMJ(2021)Gated
spikingneuralpsystemsfortimeseriesforecasting.IEEETransNeuralNetwLearnSyst,1–10
LjungGM,BoxGEP(1978)Onameasureoflackoffitintimeseriesmodels.Biometrika65(2):297–303
LubbaCH,SethiSS,KnauteP,SchultzSR,FulcherBD,JonesNS(2019)catch22:CAnonicaltime-series
CHaracteristics.DataMinKnowlDisc33(6):1821–1852
MakridakisS(1993)Accuracymeasures:theoreticalandpracticalconcerns.IntJForecast9(4):527–529
MakridakisS,HibonM(2000)Them3-competition:results,conclusionsandimplications.IntJForecast
16(4):451–476
MakridakisS,SpiliotisE,AssimakopoulosV(2020)TheM4Competition:100,000timeseriesand61
forecastingmethods.IntJForecast36(1):54–74
MakridakisS,SpiliotisE,AssimakopoulosV(2022)M5accuracycompetition:results,findings,andcon-
clusions.IntJForecast38(4):1346–1364
MannHB,WhitneyDR(1947)Onatestofwhetheroneoftworandomvariablesisstochasticallylarger
thantheother.AnnMathStat18(1):50–60
MoonH,LeeH,SongB(2022)Mixedpoolingofseasonalityfortimeseriesforecasting:anapplicationto
pallettransportdata.ExpertSystAppl201:117195
NemenyiP(1963)Distribution-freemultiplecomparisons.In:Ph.D.thesis,PrincetonUniversity
PetropoulosFetal(2022)Forecasting:theoryandpractice.IntJForecast38(3):705–871
Petropoulos F, Kourentzes N (2015) Forecast combinations for intermittent demand. J Oper Res Soc
66(6):914–924
RanP,DongK,LiuX,WangJ(2023)Short-termloadforecastingbasedonceemdanandtransformer.
ElectricPowerSysRes214:108885
RossiB(2013)Exchangeratepredictability.JEconLit51(4):1063–1119
123

Forecastevaluationfor... 831
SalinasD,FlunkertV,GasthausJ,JanuschowskiT(2020)Deepar:probabilisticforecastingwithautore-
gressiverecurrentnetworks.IntJForecast36(3):1181–1191
SallesR,BellozeK,PortoF,GonzalezPH,OgasawaraE(2019)Nonstationarytimeseriestransformation
methods:anexperimentalreview.KnowlBasedSyst164:274–291
ShabaniA,AbdiA,MengL,SylvainT(2022)Scaleformer:iterativemulti-scalerefiningtransformersfor
timeseriesforecasting.arXiv:2206.04038
ShcherbakovM,BrebelsA,ShcherbakovaN,TyukovA,JanovskyT,KamaevV(2013)Asurveyofforecast
errormeasures.WorldApplSciJ24(24):171–176
ShenZ,ZhangY,LuJ,XuJ,XiaoG(2020)Anoveltimeseriesforecastingmodelwithdeeplearning.
Neurocomputing396:302–313
ShihS-Y,SunF-K,LeeH-Y(2019)Temporalpatternattentionformultivariatetimeseriesforecasting.
MachLearn108(8):1421–1441
Stone M (1974) Cross-validatory choice and assessment of statistical predictions. J R Stat Soc Ser B
Methodol36(2):111–147
SuilinA(2017)kaggle-web-traffic.Accessed:2018-11-19.https://github.com/Arturus/kaggle-web-traffic/
Sun F-K, Boning D S (2022) Fredo: frequency domain-based long-term time series forecasting.
arXiv:2205.12301
SvetunkovI(2021)Forecastingandanalyticswithadam.OpenForecast,(version:[currentdate]).https://
openforecast.org/adam/
SyntetosAA,BoylanJE(2005)Theaccuracyofintermittentdemandestimates.IntJForecast21(2):303–314
Talagala TS(2020)Atooltodetect potentialdataleaksinforecastingcompetitions.In:International
SymposiumonForecasting2020.https://thiyanga.netlify.app/talk/isf20-talk/
TashmanLJ(2000)Out-of-sampletestsofforecastingaccuracy:ananalysisandreview.IntJForecast
16(4):437–450
WebbGI,HydeR,CaoH,NguyenHL,PetitjeanF(2016)Characterizingconceptdrift.DataMinKnowl
Discov30(4):964–994
Wong L (2019) Error metrics in time series forecasting. In: International Symposium
on Forecasting 2019. https://isf.forecasters.org/wp-content/uploads/gravity_forms/2-
dd30f7ae09136fa695c552259bdb3f99/2019/07/ISF_2019_slides.pdf
Woo G, Liu C, Sahoo D, Kumar A, Hoi S (2022) Etsformer: exponential smoothing transformers for
time-seriesforecasting.arXiv:2202.01381
WuZ,PanS,LongG,JiangJ,ChangX,ZhangC(2020)Connectingthedots:Multivariatetimeseries
forecastingwithgraphneuralnetworks.In:Proceedingsofthe26thACMSIGKDDInternationalCon-
ferenceonKnowledgeDiscovery&DataMining.KDD’20.AssociationforComputingMachinery,
NewYork,NY,USA,pp753-763
WuH,XuJ,WangJ,LongM(2021)Autoformer:DecompositiontransformerswithAuto-Correlationfor
long-termseriesforecasting.In:AdvancesinNeuralInformationProcessingSystems
YeJ,LiuZ,DuB,SunL,LiW,FuY,XiongH(2022)Learningtheevolutionaryandmulti-scalegraph
structureformultivariatetimeseriesforecasting.In:Proceedingsofthe28thACMSIGKDDConfer-
enceonKnowledgeDiscoveryandDataMining.KDD’22.AssociationforComputingMachinery,
NewYork,NY,USA,pp2296-2306
ZengA,ChenM,ZhangL,XuQ(2022)Aretransformerseffectivefortimeseriesforecasting?
ZhangX,HeK,BaoY(2021)Error-feedbackstochasticmodelingstrategyfortimeseriesforecastingwith
convolutionalneuralnetworks.Neurocomputing459:234–248
ZhouY,ZhangM,LinK-P(2022)Timeseriesforecastingbythenovelgaussianprocesswaveletself-join
adjacent-feedbackloopreservoirmodel.ExpertSystAppl198:116772
ZhouT,MaZ,wangX,WenQ,SunL,YaoT,YinW,JinR(2022a)Film:frequencyimprovedlegendre
memorymodelforlong-termtimeseriesforecasting.In:AdvancesinNeuralInformationProcessing
Systems.arXiv:2205.08897
ZhouT,MaZ,WenQ,WangX,SunL,JinR(2022b)FEDformer:Frequencyenhanceddecomposed
transformerforlong-termseriesforecasting.In:ChaudhuriK,JegelkaS,SongL,SzepesvariC,Niu
G,SabatoS(eds),Proceedingsofthe39thInternationalConferenceonMachineLearning.Vol.162
ofProceedingsofMachineLearningResearch.PMLR,pp27268–27286
ZhouH,ZhangS,PengJ,ZhangS,LiJ,XiongH,ZhangW(2021)Informer:Beyondefficienttransformerfor
longsequencetime-seriesforecasting.In:TheThirty-FifthAAAIConferenceonArtificialIntelligence,
AAAI2021,VirtualConference.vol35.AAAIPress,pp11106–11115
123

832 H.Hewamalageetal.
ZhouT,ZhuJ,WangX,MaZ,WenQ,SunL,JinR(2022c)Treedrnet:arobustdeepmodelforlongterm
timeseriesforecasting.arXiv:2206.12106
Publisher’sNote SpringerNatureremainsneutralwithregardtojurisdictionalclaimsinpublishedmaps
andinstitutionalaffiliations.
123