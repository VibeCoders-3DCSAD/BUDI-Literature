---
conversion_metadata:
  converted_at: "2026-10-12T07:04:06Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "A. Zhang et al., 2023.pdf"
  source_pdf_sha256: "33617c7d44c1cb12c6146c6c4f3618737b7d4a1f365f14fde3e32ec2a7b0c6f2"
  page_count: 14
  markdown_char_count: 114002
---

An Experimental Evaluation of Anomaly Detection in Time
Series
AoqianZhang ShuqingDeng DongpingCui
BeijingInstituteofTechnology BeijingInstituteofTechnology BeijingInstituteofTechnology
aoqian.zhang@bit.edu.cn shuqing.deng@bit.edu.cn dongping.cui@bit.edu.cn
YeYuan GuorenWang
BeijingInstituteofTechnology BeijingInstituteofTechnology
yuan-ye@bit.edu.cn wanggr@bit.edu.cn
ABSTRACT beenstudiedinvariousapplications,suchasfrauddetection[9],
Anomalydetectionintimeseriesdatahasbeenstudiedfordec- environmentalmonitoringalerting[18]andindustrialmanufac-
adesinbothstatisticsandcomputerscience.Variousalgorithms turing[10],cyberattackidentification[36],etc.Unfortunately,an
havebeenproposedfordifferentscenarios,suchasfrauddetec- anomalyisratherchallengingtodefine,especiallyinthecontext
tion,environmentalmonitoring,manufacturing,andhealthcare. oftimeseriesdata[54].Forthefollowingreasons,itisdifficultto
However,thereisalackofcomparativeevaluationofthesestate- evaluatetheperformanceofananomalydetectionmethodandto
of-the-artapproaches,especiallyinthesametestenvironmentand selectthesuitableone(withappropriateparameters)forhandling
withthesamebenchmark,makingitdifficultforuserstoselectan anomaliesinreal-worldscenarios.
appropriatemethodforreal-worldapplications.Inthispaper,we Thefirstreasonisthecomplexityanddiversityoftimeseries
presentataxonomyofanomalydetectionmethodsbasedonthe data[29].Asingletimeseriesdatamaybeunivariateormultivari-
mainfeatures,i.e.,datadimension,processingtechnique,andan- ate,andthelattermayhaveanumberofdimensions.Moreover,
omalytypeandsixinnerclasses.Weperformsystematicintra-and theanomaliesencounteredmaybeofdifferenttypes[22].Several
inter-classcomparisonsofseventeenstate-of-the-artalgorithmson algorithmshavebeenproposedtodetectanomalousbehaviorusing
realandsyntheticdatasetswithapointmetriccommonlyusedin differenttechniques,buttheyoftenfocusonaspecificcase.For
classificationproblemsandarangemetricspecificallydesignedfor instance,[25]isonlyabletofindanomalousdatapointsinuni-
subsequenceanomaliesintimeseriesdata.Weanalyzetheprop- variatetimeseries.[7]canhandleunivariatedatastreams,butcan
ertiesofthesealgorithmsandtestthemintermsofeffectiveness, onlydetectanomalouspatternsofacertainlength.Therefore,after
efficiency,androbustnesstoanomalyrates,datasizes,numberof analyzingthestate-of-the-artanomalydetectionalgorithms,we
dimensions,anomalypatterns,andthresholdsettings.Wealsotest classifythemintothreefacetsrepresentingthethreemainfeatures
theirperformanceindifferentusecases.Finally,weprovideaprac- [5],i.e.,datadimension,processingtechnique,andanomalytype.
ticalguidefordetectinganomaliesintimeseriesanddiscussions. Wecanfurtherdividethemintoclassesunderaparticularfacet,as
showninFigure1,tomakemoredetailedcomparisons.
PVLDBReferenceFormat: Thesecondreasonisthelackofthoroughtestingwiththesame
AoqianZhang,ShuqingDeng,DongpingCui,YeYuan,andGuorenWang. datasetsonthesameplatformandwiththesamemetrics.Different
AnExperimentalEvaluationofAnomalyDetectioninTimeSeries.PVLDB, worksprovidecomparisonswithdifferentscores,evenwiththe
17(3):483-496,2023. samebasicprecision-recall-F1metric[2].Forexample,[52]calcu-
doi:10.14778/3632093.3632110 latesF1scoreusingaverageprecisionandaveragerecall,whereas
[1]considersF1scoreafterthresholdadjustment.Inaddition,the
PVLDBArtifactAvailability:
baselinesbeingcomparedmaybewritteninadifferentlanguage
Thesourcecode,data,and/orotherartifactshavebeenmadeavailableat
orusedifferentdatastructures.Therefore,forafairperformance
https://github.com/zaqthss/experiment-tsad.
comparison,systematicexperimentsshouldbeperformedbetween
methodsofthesameclassinthesametestenvironment,whichis
1 INTRODUCTION
calledintra-classcomparison.
Timeseriesisoneofthemostcommonlyuseddatatypesinrecent Thethirdreasonarisesfromtheobservationthatsomerecent
decades.Timeseriesanalysisinvolvesmethodsofdataanalysisto papers[1,3,52,58]evaluatetheirmethodsunderpointmetricson
gainvaluableinsights.Anomalydetectionaimstofindrareobser- datasetswithsubsequenceanomaly.Theseareessentiallypoint
vationsthatdeviatesignificantlyfromthemajorityofdata[23]and methods,asananomalyscoreisassignedtoeachdatapointand
isthemostimportantpartoftimeseriesanalysis(mining).Ithas thosepointswhosescoreisaboveathresholdarereportedasan
anomaly.Inaddition,tointerpretthedetectiononasubsequence,
ThisworkislicensedundertheCreativeCommonsBY-NC-ND4.0International theymodifythepredictionresultsbeforeevaluationusingthepoint-
License.Visithttps://creativecommons.org/licenses/by-nc-nd/4.0/toviewacopyof
thislicense.Foranyusebeyondthosecoveredbythislicense,obtainpermissionby adjust[62]method.However,acomprehensiveexperimentshould
emailinginfo@vldb.org.Copyrightisheldbytheowner/author(s).Publicationrights beemployedtoanalyzetheeffectsofthesemeasures.Intermsof
licensedtotheVLDBEndowment.
efficiency,especiallyinbigdataapplicationswheretimeseriesdata
ProceedingsoftheVLDBEndowment,Vol.17,No.3ISSN2150-8097.
doi:10.14778/3632093.3632110 havehighdimensions(morethan50)andlargescales(morethan
483

100k),thetrade-offbetweeneffectivenessandefficiencyshouldbe Interrepresentstheconsiderationofcomparisonsbetweenuni-
considered.Inparticular,thepossibilityofimplementingunivariate variateandmultivariatemethods.Similarly,<Batch,Online,Inter>
modelsoneachdatadimension[28]andfindingouttowhatextent refers to the processing technique, while <Point, Range, Inter>
onlinedetectorsapproximatetheperformanceofbatchmethods focusesonthetypeoftargetanomaly.ThresholdsRobustnessin-
[12,44]couldreceivespecialattention.Therefore,comparisons dicateswhethertheworkexaminestherobustnessofthecompared
betweenclassesinthesamefacet,whichwecallinter-classcom- methodstothresholding.Finally,ApplicationGuidelineindicates
parisons,arealsouseful.Finally,theessentialfeaturesofanomaly whethertheworkprovidespracticalguidelinesformethodselection
detectionalgorithms,includingrobustnessintermsofthreshold inreal-worldscenarioswithdifferentrequirements.
setting,shouldbecapturedintermsofpracticalapplications.Sys- In[57],distance-basedonlinedetectionmethodsofpointout-
tematicexperimentswithdifferentrealcasesandanalysisofthe liersindatastreamsareevaluated.However,onlyefficiencyfactors
behaviorofthesealgorithmswillbehelpfulforusers. suchasCPUtimeandleakagememoryaretestedunderdifferent
parameters.MD[12]comparesruntimeandefficacyofdifferent
1.1 Contributions detectionmethodsforfourtypesofanomaliesinrealstreaming
Tothebestofourknowledge,thisisthefirstin-depthexperimental cases.Itservesasaguideforselectingthe‘best’univariatetech-
studytoprovidebothintra-classandinter-classevaluations.Our niqueintermsofreal-timeandaccuracy,butlacksconsiderations
maincontributionsinthispaperaresummarizedasfollows. forthecharacteristicsofthedatasetsandthetypeofapplication.
TUD[8]focusesonsupervisedmethodsforunivariatedata.TODS
(1) Weproposeataxonomyofmethodsfordetectinganomaliesin
[31]revisesoutlierdefinitionsandproposesanewtaxonomyfor
timeseriesbasedontheiressentialfeaturesinthreefacetsand
anomaly types. It tests batch methods under different anomaly
sixinnerclassesinSection2.
ratesfordifferenttypesofanomalies,butomitsevaluationsunder
(2) Wepresentbriefdescriptionsof17state-of-the-artmethods
otherfactorssuchasdatadimensions.Exathlon[29]generatesa
inSection3.Furthermore,were-implement10ofthemwith
novelbenchmarkingplatform.Threedeeplearningmethodsare
JAVA,refactorallmethodswiththesamecodestructure,and
testedontheproposeddatasetswithrangeanomaliesandeval-
buildatestingframeworktoavoidthepotentialimpact.
uatedbyrangemetrics[53].Itsmajordifferencetoothersisthe
(3) Weprovidesystematicintra-classcomparisonsunderdifferent
capabilityofevaluatingexplanationdiscoveryresults,whichisnot
scenarioswithreal-worldandsyntheticdatasetsinSection4.2,
coveredbyourwork.Nevertheless,itfailstocomparemoretypes
including(a)effectivenesswithpoint-andrange-basedmetrics,
ofanomalydetectionmethodsandprovidemorecomprehensive
(b)anomalyrates,(c)datasizes(scalability),(d)dimensions,(e)
analysis.TSB-UAD[47]establishesanewbenchmarktofacilitate
anomalypatterns.
theevaluationofunivariatemethodsandevaluatesseveralbatch
(4) Weemployinter-classcomparisonsanddrawinterestingfind-
methodstodemonstratetherobustnessoftheproposedbenchmark,
ingsinSection4.3,like(a)pointanomalymethodscanalso
butdoesnotaddressmultivariatetimeseriescases.Theaforemen-
performwellundersubsequenceanomalycases,(b)usingrange
tionedTODS,Exathlon,andTSB-UADprovidenovelbenchmarks
metricsonsubsequencedatacanleadtomorereasonableand
basedondifferenttechniquesthatpresentthemaincontributions
robustresults,(c)point-adjustmethodtendstoreport‘false’
anddifferencesfromotherstudies.Meta[44]presentsaqualitative
higheraccuracyresultsandmaymisleadanalysis.
reviewofonlinedetectorsfromdifferentfamiliesandproposesa
(5) Weanalyzethecapabilityofmethodsunderdifferentapplic-
fairevaluationenvironmentforonlineandofflinedetectorsover
ationcases,consistingof(a)thefalsepositivesandnegatives
multivariatedata.Thegoalistofindouttowhatextentonlinede-
theygenerate,(b)whethertheycandetectanomaliesasearly
tectorsapproximatetheperformanceofofflinedetectors.However,
aspossibleandproviderecommendationsinSection5.
itfocusesonlyonunsupervisedmethodsfordetectingpointanom-
1.2 RelatedWork alies(includingrangeanomalieswithpointmetrics)andleavesout
(semi)supervisedmethods.
Table1:ComparisonofTADExperimentalSurveys HPI[49]makesanexhaustiveevaluationof71anomalydetec-
tionmethodsandevaluatesthemonvariousdatasetswithdifferent
typesofanomalies.Althoughitprovidesacomprehensiveevalu-
Dimension Processing AnomalyType Threshold Application
ExpSurvey <Uni,Mul,Inter> <Batch,Online,Inter> <Point,Range,Inter> Robustness Guideline ation,itstillhassomeuntouchedareas,whichweextendasfollows:
DODDS[57] <(cid:37),(cid:33),(cid:37)> <(cid:37),(cid:33),(cid:37)> <(cid:33),(cid:37),(cid:37)> (cid:37) (cid:37) (1)Theyoptimizetheparametersofallmethodsgloballyoverthe
MD[12] <(cid:33),(cid:37),(cid:37)> <(cid:37),(cid:33),(cid:37)> <(cid:33),(cid:33),(cid:37)> (cid:37) (cid:33)
TUD[8] <(cid:33),(cid:37),(cid:37)> <(cid:33),(cid:37),(cid:37)> <(cid:33),(cid:37),(cid:37)> (cid:37) (cid:33) samewell-labeledsyntheticdataset,butwetunetheseparameters
TODS[31] <(cid:37),(cid:33),(cid:37)> <(cid:33),(cid:37),(cid:37)> <(cid:33),(cid:33),(cid:33)> (cid:37) (cid:37)
Exathlon[29] <(cid:37),(cid:33),(cid:37)> <(cid:33),(cid:37),(cid:37)> <(cid:37),(cid:33),(cid:37)> (cid:33) (cid:33) perdatasettogetafairerevaluationwiththeirbestperformance;
TSB-UAD[47] <(cid:33),(cid:37),(cid:37)> <(cid:33),(cid:37),(cid:37)> <(cid:33),(cid:33),(cid:37)> (cid:37) (cid:37) (2)Theydonotconsiderthetranslationofanomalyscorestoan-
Meta[44] <(cid:37),(cid:33),(cid:37)> <(cid:33),(cid:33),(cid:33)> <(cid:33),(cid:33),(cid:37)> (cid:37) (cid:33)
HPI[49] <(cid:33),(cid:33),(cid:37)> <(cid:33),(cid:37),(cid:37)> <(cid:33),(cid:33),(cid:37)> (cid:37) (cid:33) omalylabelsviathresholding,however,weanalyzetherobustness
Ourwork <(cid:33),(cid:33),(cid:33)> <(cid:33),(cid:33),(cid:33)> <(cid:33),(cid:33),(cid:33)> (cid:33) (cid:33) ofusingdifferentthresholdingtechniquessinceanomalyidenti-
ficationiscrucialinmostreal-worldscenarios;(3)Theysimply
Wesummarize8previousexperimentalstudiesontimeseries implementpointandrangemetricsforpointandsubsequencean-
anomalydetectionandourworkinTable1.Thefirstthreecolumns omalies,respectively,withoutdeeperanalysis.Wealsoperform
representthefundamentalfacetscoveredinthestudy,e.g.,inthe theinter-classcomparisonusingapointmetricforsubsequence
firstcolumn,Uniindicatesthattheworkincludesunivariatedetec- anomalies,whichhasbeenwidelyusedinpreviousstudies,and
tionmethods,Mulstandsformultivariatedetectionmethods,while findinsightfulresults;(4)Theirresearchinsightscanhelpusers
484

2.2 AnalysisFacets
Theanomalyanalysisproblemscanbecategorizedinvariousways
[22].Inthiswork,weproposeacomprehensivetaxonomyconsist-
ingofthefollowingthreefacets,i.e.,datadimension,processing
technique,andanomalytype,asshowninFigure1.Foreachfacet,
Figure1:Facetsandclassesofanomalydetectionalgorithms
wefurtherdividedetectionmethodsintoclasses.Thedetailsof
thesefacetsandclassesarepresentedinthissection.
| 12.5 |     |       |     | 2.2.1 Datadimension. | Thenumberoftime-dependentvariables |     |     |
| ---- | --- | ----- | --- | -------------------- | ---------------------------------- | --- | --- |
|      | O2  | U n i |     |                      |                                    |     |     |
O3 D i m 1 thatananomalydetectionmethodcanconsidersimultaneouslyis
| 10.0 |     | D i m 2 |     |                                                 |     |     |             |
| ---- | --- | ------- | --- | ----------------------------------------------- | --- | --- | ----------- |
|      |     |         |     | itsessentialfeature[5].FollowingDefinition2.1,𝑿 |     |     | iscalledasa |
eulav 7.5
|     |     | O4  |     | univariatetimeseriesif𝐷 | =   | 1while𝑿 isamultivariatetime |     |
| --- | --- | --- | --- | ----------------------- | --- | --------------------------- | --- |
5.0
seriesif𝐷 >1.
| 2.5 | O1  | O6  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     | O5  | O7  |     |     |     |     |     |
0.0 Scenario1:Highdimension. Theoretically,multivariatemethods
| 1   | 6 11 16 21 | 26 31 36 41 |     |     |     |     |     |
| --- | ---------- | ----------- | --- | --- | --- | --- | --- |
timestamp canexploitcorrelationsbetweendimensions,resultinginbetter
(a) Univariate(above)/Multivariate(below) time series
accuracythanunivariatemethods,whichcanonlytreateachdi-
Figure2:(a)timeseriesand(b)onlineprocessingtechnique
mensionseparately.However,multivariatemethodsrequiremuch
moretime,asunivariatemethodscanachievehighefficiencyby
|     |     |     |     | parallelizing each | dimension. | The test on Swat | (51 dimensions) |
| --- | --- | --- | --- | ------------------ | ---------- | ---------------- | --------------- |
showsthat,theunivariatemethodIDKcosts16.50s,whilethemul-
selecttheoptimalalgorithmforspecificanomalytypes,suchas tivariatemethodPBADtakes125.17s,almost10timesthetime.On
extremumanomalies.Wealsoanalyzereal-worldapplicationsthat theotherhand,[28]implementstheLSTMmodeloneachdimen-
aremoreinterestedinpositive,negative,andearlydetectioncases,
sionofthesatellitedataset,sinceLSTMshavedifficultypredicting
andprovideapracticalguideformethodselection.
m-dimensionalresultsaccuratelywhenmislarge.Therefore,a
Theabovepapersinvestigateproblemsoftimeseriesanomaly systematicinter-classcomparisonsshouldbeperformedtotestthe
detection(TAD)fromvariousaspects,butleaveroomforfurther possibilityofusingunivariatemethodsonmultivariatedata.
analysis.Theoreticalsurveys[5,11,14,22]provideastructured
overviewofresearchmethodswithdifferentemphases.Incontrast, 2.2.2 ProcessingTechniques. Atimeseriescanalsohaveaninfinite
weconsiderthestate-of-the-artmethodsnotcoveredinthesestud- numberofdatapoints(stream).Methodsthatcanhandleinfinite
ies,performacomprehensiveanalysisonwiderrangesasshown timeseriesarecalledonlinemethods,whilethosethatcannotare
calledbatchmethods.Theslidingwindowisthetechniquemost
inTable1,andobtaincontributionsasindicatedinSection1.1.
Theoriginalpapersproposinganomalydetectionalgorithms commonlyusedbyonlinemethods[57].
thatwecompareinourwork[1,3,6,7,17,19,24–26,39,42,50,
|     |     |     |     | Scenario2:LargeScale. | Theoretically,batchmethodshavehigher |     |     |
| --- | --- | --- | --- | --------------------- | ------------------------------------ | --- | --- |
52,55,58,66,67]alsoconsistofempiricalcomparisons.However,
accuracybecausetheycancomparealldatasimultaneously.Incon-
theseexperimentsarelimitedintermsofdatasets,competitors,and
trast,onlinemethodscanrunfasterbecausetheyprocessonlythe
thoroughanalyzesofprecision/recall,efficiency,andsensitivity
datapointsinthecurrentwindow.Ontheonehand,onlinemeth-
| compared | to our study. | We use datasets from | these works and |     |     |     |     |
| -------- | ------------- | -------------------- | --------------- | --- | --- | --- | --- |
odscancontinuouslyupdatetheirmodelsforincrementalanomaly
benchmarksfromNumenta[34],Exathlon[29],andTODS[31].
detectiontoaccountforthefactthattimeseriescharacteristics
evolveovertime[21,44].Ontheotherhand,theefficiencygap,
2 PRELIMINARIES especiallyforlargedatasets,shouldalsobetakenintoaccount[40].
2.1 ProblemDefinition Therefore,like[44],weareinterestedintheextenttowhichonline
methodsapproximatetheperformanceofbatchmethodsandwhat
Anomalydetectionintimeseriesdatacanbedefinedasfollows.
thetrade-offbetweeneffectivenessandefficiencyis.
| Definition2.1(Timeseries).                              |     | Atimeseriesisaseriesofdatapoints |     |                     |                                     |     |     |
| ------------------------------------------------------- | --- | -------------------------------- | --- | ------------------- | ----------------------------------- | --- | --- |
|                                                         |     |                                  |     | 2.2.3 AnomalyTypes. | Inatimeseries,datapointsthatdeviate |     |     |
| indexedintimeorder.Consideratimeseriesof𝑛observations,𝑿 |     |                                  | =   |                     |                                     |     |     |
significantlyfromotherobservationsarecalledpointanomalies.
| {𝒙1 ,...,𝒙𝑛}.The𝑖-thobservation(datapoint)𝒙𝑖 |     |     | ∈ R𝐷 consists |     |     |     |     |
| -------------------------------------------- | --- | --- | ------------- | --- | --- | --- | --- |
Subsequencesofthetimeserieswithlesssimilaritycomparedto
| of𝐷 dimensions{𝑥 | 1,...,𝑥 | 𝐷}andisobservedattimestamp𝑡 |     |     |     |     |     |
| ---------------- | ------- | --------------------------- | --- | --- | --- | --- | --- |
𝑖 𝑖 𝑖.A othersarecalledassubsequenceanomalies.Thecapabilityofa
,...,𝒙ℓ−𝑖+1
subsequence𝑿𝑖,ℓ ={𝒙𝑖 }isasubsetofconsecutivetime methodmustbeevaluatedbyanappropriatemetricrelatedtothe
| pointsfromtimeseries𝑿 |     | startingatposition𝑖withlengthℓ. |     |     |     |     |     |
| --------------------- | --- | ------------------------------- | --- | --- | --- | --- | --- |
typeofanomaly,otherwisemisleadingresultsmaybeobtained
[45,53].Tocomparemethodsindifferentcases,wefurtherdivide
| Definition2.2(AnomalyDetectioninTimeSeries). |     |     | Ananomaly |     |     |     |     |
| -------------------------------------------- | --- | --- | --------- | --- | --- | --- | --- |
pointandsubsequenceanomaliesintothefollowingpatterns[31].
isanobservation(orsubsetofobservations)whichappearstobe
inconsistentwiththeremainderofthatsetofdata[4].Anomaly ={𝒙1 ,...,𝒙𝑛}.Let|𝒙𝑡 −
|     |     |     |     | PointAnomaly. | Givenatimeseries𝑿 |     |     |
| --- | --- | --- | --- | ------------- | ----------------- | --- | --- |
>𝛿,where𝛿isathresholdand𝒙ˆ𝑡
detectionintimeseriesinvolvesfindingtheabnormaldatapoints 𝒙ˆ𝑡| istheexpectedvalue.Global
𝒙𝑖 orsubsequences𝑿𝑖,ℓ inthegiventimeseries. anomaly indicates that𝛿 ∼ 𝜎(𝑿), where 𝜎(𝑿) is the standard
deviationofthewholetimeseries.Contextualanomalywith𝛿 ∼
485

Table2:Anomalydetectionmethodsconsideredhere 3.1 Distance-basedMethods
Distance-basedalgorithms[57]intheliteraturecandetectboth
Algorithm Mul Process Anomaly Threshold Code Speedup pointandsubsequenceanomalies,butforsimplicityweonlyrefer
|     |     | ✓   |     |     | 𝜃𝑘  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ecnatsiD NETS[66] ✓ online point JAVA - topointanomaliesinthefollowingdefinitions.
|     | STARE[67]  |     | online | point       | top-𝜃𝐾 JAVA   | -   |     |                          |     |                          |     |     |         |
| --- | ---------- | --- | ------ | ----------- | ------------- | --- | --- | ------------------------ | --- | ------------------------ | --- | --- | ------- |
|     | NP[24]     | -   | batch  | subsequence | top-𝜃𝐾 python | 1.5 |     |                          |     |                          |     |     |         |
|     | MERLIN[42] | -   | batch  | subsequence | top-𝜃𝐾 matlab | 60  |     |                          |     |                          |     |     |         |
|     |            |     |        |             |               |     |     | Definition3.1(Neighbor). |     | Givenadistancethreshold𝜃 |     |     | 𝑅,adata |
|     | PBAD[19]   | ✓   | batch  | subsequence | top-𝜃𝐾 python | 2.5 |     |                          |     |                          |     |     |         |
LRRDS[26] ✓ batch subsequence cluster r 1 point𝑥 is a neighbor of datapoint𝑥 𝑗(𝑥 ≠ 𝑥 𝑗) if the distance
|     | nrettaP SAND[7] | -   | online | subsequence | top-𝜃𝐾 C&python | 0.3 |     | 𝑖        |     |     | 𝑖   |     |     |
| --- | --------------- | --- | ------ | ----------- | --------------- | --- | --- | -------- | --- | --- | --- | --- | --- |
|     |                 |     |        |             | top-𝜃𝐾          |     | 𝑑(𝑥 | ,𝑥 𝑗) ≤𝜃 |     |     |     |     |     |
|     | NormA[6]        | -   | batch  | subsequence | C&python        | -   |     | 𝑖        | 𝑅.  |     |     |     |     |
|     | GrammarViz[50]  | -   | batch  | subsequence | top-𝜃𝐾 JAVA     | -   |     |          |     |     |     |     |     |
|     | IDK[55]         | -   | batch  | subsequence | top-𝜃𝐾 python   | 20  |     |          |     |     |     |     |     |
SHESD[25] - batch point 𝜃𝑘,top-𝜃𝐾 JAVA Definition3.2(Distance-basedOutlier). Givenatimeseries𝑋,
gninraeLpeeD Be a tG A N [ 3 9] ✓ b a t c h subs e q u e nce top - 𝜃𝐾 p y t h o n - acountthreshold𝜃 andadistancethreshold𝜃 𝑅,distance-based
|     | O m n i [5 | 2 ] ✓ | b a t c h | p o i n t | 𝜃 𝜏 p y t h o | n - |     |     | 𝑘   |     |     |     |     |
| --- | ---------- | ----- | --------- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
U SA D [3 ] ✓ b a t c h p o i n t 𝜃 p y t h o n - outliersaresetofdatapointsthathavelessthan𝜃
|     |           | ✓   |           |           | 𝜃 𝜏         |     |     |     |     |     |     | 𝑘   | neighbors. |
| --- | --------- | --- | --------- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | ---------- |
|     | G D N [1  | 7 ] | b a t c h | p o i n t | 𝜏 p y t h o | n - |     |     |     |     |     |     |            |
|     | RCoder[1] | ✓   | batch     | point     | 𝜃𝜏 python   | -   |     |     |     |     |     |     |            |
TranAD[58] ✓ batch point 𝜃𝜏 python - The key factors are the distance threshold𝜃 and the count
𝑅
threshold𝜃 𝑘,determiningtheneighborsforeachdatapointandthe
𝜎(𝑿𝑡−𝑘,𝑡+𝑘)denotesthatthesuchanomalypointisdifferentfrom anomalies.Foronlinemethods,thefactorswindowsize𝜃
𝑊 andthe
slidesize𝜃
itsneighborsinaspecificrange(windowsize𝑘). 𝑆 affecttheperformanceandareusuallysetdepending
onthesizeofthedataset.Distancemethodsforpointanomalies
| SubsequenceAnomaly. |                  |     | Here,weassumethatthesubsequence |     |      |     |       |       |                    |         |      |             |           |
| ------------------- | ---------------- | --- | ------------------------------- | --- | ---- | --- | ----- | ----- | ------------------ | ------- | ---- | ----------- | --------- |
|                     |                  |     |                                 |     |      |     | often | focus | on the scalability | problem | [57] | and utilize | different |
| 𝑋                   | =𝜌(2𝜋𝜔𝑇 𝑖,𝑗)+𝜏(𝑇 |     | 𝑖,𝑗),where𝜌,𝜔                   |     | and𝜏 |     |       |       |                    |         |      |             |           |
𝑖,𝑗 representsthebasic structurestosaverunningtimes.NETS[66]employsaset-based
shape,trendandseasonality,respectively.Global(shapelet)anomaly
approachfollowingneteffect,thatdatapointsinashortperiodof
referstothesubsequenceswithdissimilarbasicshapes,whichcan
timearelikelytobeconcentratedinasetofsmallregionsinthe
| bedefinedas𝑠(𝜌,𝜌ˆ) |     | >   | 𝛿,where𝑠 | isthesimilarityfunction[31]. |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | -------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
dataspace.STARE[67]observesthatdatadistributionsinmany
| Seasonalanomalywith𝑠(𝜔,𝜔ˆ) |     |     |     | >𝛿meansthatthosesubsequences |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
regionsofthedataspacechangelittleacrosswindowslidesand
haveunusualseasonalitycomparedtothewholeseries.Trendan- thusskipsupdatingdensitiesinlocalregionsthatdonotchange
omalyindicatesthesubsequencesthatsignificantlyalterthetrend
significantly.NP[24]usesbaggingtorobustlydiscoverfrequentand
ofthetimeseries,leadingtoapermanentshiftinthemeanofthe
raresubsequences.Anearestneighborballtechniquethatreplaces
| data,whichcanbedenotedas𝑠(𝜏,𝜏ˆ) |     |     |     |     | >𝛿. |     |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thenearestneighbordistancewhichistoosmallwiththeradiusof
Scenario3:Parameterrelaxation. Nevertheless,itisdifficultto suchaballisproposedtoprovidearobustestimationandsolvethe
twinfreakproblem[24],whichisnotsolvedinmatrixprofile[65].
findaspecificpatternofananomalyinrealdatasets.Currentsub-
DRAG[64]createsacandidatediscordset𝐶andthensearchesitfor
| sequencemethodsrequirethelength |     |     |     |     | ofthetargetsubsequence |     |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
asinput[5–7].However,itisratherdifficulttodeterminesuch alistofdiscordswhosenearestneighbordistanceisgreaterthana
aparameterwithoutsufficientpriorknowledge.Incontrast,the hyper-parameter𝑟.MERLIN[42]providesastructuredsearchto
pointmethodsdonotrequiresuchadditionalinput(thelengthis setsuch𝑟.SinceNETSandMERLINdominatesDRAG,respectively,
inalmostallthedatasetsandhenceweonlyreporttheformertwo
1).Hence,wewonder(1)howpowerfulpointmethodsareinthe
| presenceofanomaliesinsubsequences;(2)howwellthemethods |     |     |     |     |     |     | here. |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
candetectdifferentpatternsofanomalies.
3.2 Pattern-basedMethods
| Example2.3. |     | Pointandsubsequenceanomaliescanbeunivariate |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ormultivariate.Figure2(a)showstwounivariatepointanomalies, Theso-calledpatternrepresentstheregularitiesinthedata,such
𝑂1(global)and𝑂5(contextual).Intermsofpatterns,𝑂3isatrend asanorderedsetofdatapointsthatoccurfrequentlyinthedata,
anomalyasitleadstoapermanentshiftwithalowermean,𝑂2is oraparticulardistribution.Pattern-basedmethods[14]areusu-
aseasonalanomalyand𝑂4,𝑂6areglobalanomalies.Datapoints allyproposedtofindsubsequenceanomalies,whichweuseinthe
in univariate time series𝑋 = {𝑥 ,...,𝑥 } are observed at time followingdefinitions.Pointanomaliescanbefoundifthepattern
|     |     |     |     | 1   | 6   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1,2,3,5,7,8inFigure2(b).Letussetthewindowsize𝜃 𝑊 =4,slide indicatesadistribution.
size𝜃 = 2.Theonlinemethodwillfirstprocessthedatapoints
|       | 𝑆           |     |     |     |     |           |     | Definition3.3(Pattern-basedOutlier). |     |     | Givenatimeseries𝑋,an |     |     |
| ----- | ----------- | --- | --- | --- | --- | --------- | --- | ------------------------------------ | --- | --- | -------------------- | --- | --- |
| { 𝑥 , | . . . , 𝑥 } |     |     |     |     | { 𝑥 , 𝑥 } |     |                                      |     |     |                      |     |     |
1 4 i n th e c u r r e n t w i n do w . A f t e r t h e p r o c e s s i n g , 1 2 ℓ 𝜃
𝑥 , 𝑥 a n o m a l y le n g t h a n d a c o u n t t h r e s h o ld 𝐾 , p a t ter n - b as e d o u t lie r s
i n t h e fi r s t s l i d e w i l l b e e x p i r e d a n d { 5 6 } i n t h e n e w s l id e w il l 𝜃 ℓ
|       |                    |           |           |           |                       |           | a r  | e t h e s e   | t o f t o p - 𝐾 s u    | b s e q u e n c e s | w i th le n | g t h a | n d t h e l o w e s t |
| ----- | ------------------ | --------- | --------- | --------- | --------------------- | --------- | ---- | ------------- | ---------------------- | ------------------- | ----------- | ------- | --------------------- |
| c o m | e i n , f o r m in | g a n e w | w i n d o | w c o n t | a i n i n g { 𝑥 , . . | . , 𝑥 } . |      |               |                        |                     |             |         |                       |
|       |                    |           |           |           | 3                     | 6         | si m | i l a r i t y | t o t h e p a t t er n | s e x tr a c t e d  | fr o m 𝑋 .  |         |                       |
3 ALGORITHMS
Thefactorsforpatternmethodsvarydependingonhowthey
Followingtheproposedtaxonomy,wechoosethelatestrepresent- definepatterns,support,andthresholdforanomalies.Ingeneral,the
ativesforeachclass:11/17ofthesemethodsarepublishedsince keyfactorsarethesupportthreshold𝜃 𝑠𝑢𝑝,theanomalythreshold
2020and12/17arenotcomparedinpriorworksinSection1.2.We 𝜃 𝜏,orthecountthreshold𝜃 𝐾,whichrepresenttheminimumoccur-
willbrieflyintroducethemintheclassofdetectiontechniques, renceofapattern,theborderofananomaly,andtherankofscores
i.e.,distance,pattern,anddeeplearning-basedandextracttheir thatananomalyachieves,respectively.
criticalfactors.Table2liststhepropertiesofeachalgorithm.The ESD[48]computestheExtremeStudentizedDeviateteststat-
‘threshold’columnindicateshowthethresholdforanomaliesisset. istictofindanomalypoints.SHESD[25]extendsESDbyusing
486

STLdecomposition[13]andreplacingthemeanandstandardde- Table3:Real-worldandsyntheticdatasetssummary
viationwithmorerobustmedianandmedianabsolutedeviation.
Consideringtheseasonality,SHESDoutperformsESDandhence Real-world Size #Dim Rate% Pattern AvgLength
1.5k 0.7
weonlyreportSHESD.NormA[6],SAND[7]andIDK[55]learna Yahoo[35] 1 Contextual -
|     |     |     |     | Twitter[25] | 14k 1 0.7 Global | -   |
| --- | --- | --- | --- | ----------- | ---------------- | --- |
normalmodel(clusteringthedistributionofnormalpatterns)and Stock[57] 10k 1 5-25 Mixed -
tnioP
thesimilaritydistancetothenormalmodelisusedastheanomaly Tao[57] 568k 3 5-25 Mixed -
|     |     |     |     | SMTP[38] | 95k 3 0.03 Mixed     | -   |
| --- | --- | --- | --- | -------- | -------------------- | --- |
|     |     |     |     | DLR[67]  | 23k 9 2.2 Contextual | -   |
scoresfortargetsubsequences.SANDfurtherextendsthek-Shape
|     |     |     |     | ECG[67] 112k | 32 16.3 Global | -   |
| --- | --- | --- | --- | ------------ | -------------- | --- |
clustering[46]sothatthenormalmodelcanbeupdatedfromone
|     |     |     |     | Power[30] | 35k 1 8.6 Seasonal | 750 |
| --- | --- | --- | --- | --------- | ------------------ | --- |
batchtothenext,makingitselfanonlinemethod.IDKusesIsol- ecneuqesbuS Sed[7] 100k 1 3.0 Global 64
|     |     |     |     | Taxi[53] | 10k 1 10 Global+Seasonal | 207 |
| --- | --- | --- | --- | -------- | ------------------------ | --- |
ationDistributionalKernel[56]tocomputethesimilarity.PBAD
|     |     |     |     | Machine[53] | 22k 1 10 Global+Seasonal | 567 |
| --- | --- | --- | --- | ----------- | ------------------------ | --- |
[19]andGrammarViz[50]userulestoextractthenormalpatterns. Exercise[19] 10k 3 15.1 Mixed 140.2
|     |     |     |     | Exathlon[29] | 3k 19 17.4 Mixed | 64.1 |
| --- | --- | --- | --- | ------------ | ---------------- | ---- |
Theformerpresentsfrequentpatternminingresearch[68]tofind
|     |     |     |     | Swat[41] | 90k 51 12 Mixed | 317.2 |
| --- | --- | --- | --- | -------- | --------------- | ----- |
frequentpatterns(whosesupportisgreaterthan𝜃 Smd[52] 28k 38 9.5 Mixed 336.8
𝑠𝑢𝑝)whilethe
|     |     |     |     | Synthetic | Size #Dim Rate% Pattern | AvgLength |
| --- | --- | --- | --- | --------- | ----------------------- | --------- |
latterimplementstwogrammarinductionmethods[33,43]togen-
|     |     |     |     | tnioP Uni-point-g 1k-100k | 1 5-25 Global | -   |
| --- | --- | --- | --- | ------------------------- | ------------- | --- |
erate a context-freegrammar. LRRDS [26] usesrecurrenceplot Uni-point-c 1k 1 5-25 Contextual -
[69]andextractsthesubsequencesetfromthelocalrecurrence Mul-point 1k-100k 32 5-25 Global -
|     |     |     |     | Uni-sub-g 1k-100k | 1 5-25 Global | 50  |
| --- | --- | --- | --- | ----------------- | ------------- | --- |
rates(LREC)[63].Theanomalyscoreiscomputedbycomparing
|     |     |     |     | ecneuqesbuS Uni-sub-s 1k-100k | 1 5-25 Seasonal | 50  |
| --- | --- | --- | --- | ----------------------------- | --------------- | --- |
|     |     |     |     | Uni-sub-t 1k-100k             | 1 5-25 Trend    | 50  |
similaritiesbetweenstatisticsintheLRECcurve. Mul-sub-g 1k-100k 3/50 5-25 Global 50
|     |     |     |     | Mul-sub-s 1k-100k | 3/50 5-25 Seasonal | 50  |
| --- | --- | --- | --- | ----------------- | ------------------ | --- |
|     |     |     |     | Mul-cor-g         | 5k 3 10 Global     | 50  |
3.3 DeepLearning-basedMethods
|     |     |     |     | Mul-ncor-g | 5k 3 10 Global | 50  |
| --- | --- | --- | --- | ---------- | -------------- | --- |
Recently,severaldeeplearning-basedmethodshavebeenproposed
todetectanomaliesintimeseries[15].Variousarchitectureshave
POT[51](selectingthresholdautomatically)andpoint-adjust[62]
beendevelopedtocapturelatentinformationfromtemporaland
(modifyingpredictionsbeforeevaluation)tomakeafaircompar-
dimensionalaspects.
ison.AnalysisonthesechangescanbefoundinSection4.3.4and
Forreconstructionbasedmethods,afterlearningamodelofthe
4.3.5,respectively.The’Code’columninTable2showstheoriginal
normaldatainthelatentspace,thetesttimeseriesisfirsttrans-
languageinwhicheachmethodwaswritten,whilethe‘Speedup’
formedtothelatentspaceandthenreconstructedtothedataspace.
columnshowstheincreaseinefficiencyafterourimplementation
Finally,thereconstructedvaluesthathavealargerdistancefrom
(exceptSAND,thedecompositiontoolsrunsfarmoreslowly).We
observationswillbeidentifiedasanomalies.OmniAnomaly(Omni)
verifythatthereportedanomaliesofthemethodsbeforeandafter
[52]proposesastochasticrecurrentneuralnetworkbyusingGRU
ourrefactorareidenticalandguaranteereproducibility.
tocapturecomplextemporaldependenciesbetweenmultivariate
observationsindataspace,andavariationalautoencoder(VAE)
4 EXPERIMENT
tomapobservationstostochasticvariables.USAD[3]presentsan
Thissectionwillfirstshowtheexperimentalsettings.Then,insights
encoder-decoderarchitecturewithinatwo-phaseadversarialtrain-
foundoverintra-classandinter-classcomparisonsareexplained.
ingsystem(GAN).BeatGAN[39]alsoprovidesaninterpretable
Similarto[49],wetryourbesttodescribefindingsfromexperi-
| method that | combines autoencoders | and GAN | to detect anom- |     |     |     |
| ----------- | --------------------- | ------- | --------------- | --- | --- | --- |
aloussubsequences. RCoder[1]introducesanencoder-decoder mentalresults.However,ifamethodperformspoorlyinourevalu-
ation,itdoesnotnecessarilymeanthatitstheoryisbad,because
frameworktolearntheboundsofreconstructedsignals.Thekey
themetricandthesituationarequitedifferent.
differenceisthatitssizeoflatentspaceis1andaspectralana-
| lysis with | Fast Fourier Transform | is then applied. | TranAD [58] |     |     |     |
| ---------- | ---------------------- | ---------------- | ----------- | --- | --- | --- |
4.1 Settings
combinestransformer-basedencoder-decodernetworkswithad-
versarialtraining.Predictionbasemethodslearnamodelfromnor- WerunexperimentsonaWindows10serverwitha3.79GHz12
CoreCPUand128GBRAM.Deep-learningmethodsareemployed
maldataandthenpredictsthetargetvaluebasedonthemodeland
observationsbeforethetargettime.Finally,thedifferencebetween withGPUwithoutcomparingtheefficiency.Othersaretestedunder
thepredictedvalueandobservationisusedastheanomalyscore. asingle-coreenvironmenttocomparerunningtimes.
| GDN [17] | employs the Graph | Neural Network | to learn the de- |     |     |     |
| -------- | ----------------- | -------------- | ---------------- | --- | --- | --- |
4.1.1 Datasets. Weemploywidelyusedreal-worlddatasetswith
pendencyrelationshipbetweendifferentdimensionsandusegraph
labelsasbenchmarks,7withpointand8withsubsequenceanom-
attentionmechanismtomakepredictions.
alieswithvarioussizes,dimensions,anomalyrates(lengths)and
patterns.Wealsogeneratesyntheticdatasetswhosebasetypeis
3.4 ImplementationNotes
sine,withdifferentanomalypatterns(SeeSection2.2.3)according
Somewidelyusedsystems,suchasApacheIoTDB[59],canonly totheguidelinein[31]forthecaseoftheunreliabilityofanomaly
supportJAVAasbuilt-infunctions,andhencewerewriteallnon- labels[61].Forpointanomaly,weinjectglobal(g)andcontextual(c)
deeplearningmethodsinJAVA(exceptNormA,theexistingtoolkit outliers.Forsubsequenceanomaly,weaddglobal(g),seasonal(s)
runsdifferently).WealsorefactorNETS,STARE,GrammarViz,and andtrend(t)outliers,respectively.Theaveragelengthissetto50by
SHESD(inJAVA)anddeeplearningmethods(inPython)withour default,soanyalgorithmisapplicable.Inordertoavoidtheeffect
datastructurestoavoidpotentialimpactonefficiency.Weremove ofrandomness,werunexperimentsonsyntheticdatasets10times
487

|     | NETS | SHESD USAD | Omni |     | PBAD SAND | MERLIN | NormA |     |     |     |     |
| --- | ---- | ---------- | ---- | --- | --------- | ------ | ----- | --- | --- | --- | --- |
Stare TranAD GDN RCoder LRRDS NP GrammarViz IDK NETS SHESD USAD Omni
|     |     |     |     | 103 |     |     |     |     | Stare TranAD | GDN RCoder |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- |
103
| )s( tsoc emiT |     |     |     | )s( tsoc emiT 102 |     |     |     | 1.00 |     | 100 |     |
| ------------- | --- | --- | --- | ----------------- | --- | --- | --- | ---- | --- | --- | --- |
101
|      |     |     |     | 101 |     |     |     |                |     | )s( tsoc emiT |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------- | --- |
| 10−1 |     |     |     |     |     |     |     | erusaem-F 0.75 |     |               |     |
100
0.50
| 10−3 | Yahoo | Twitter SMTP | DLR | 0   | Power Sed | Taxi | Machine |     |     | 10−1 |     |
| ---- | ----- | ------------ | --- | --- | --------- | ---- | ------- | --- | --- | ---- | --- |
0.25
|     |     | Dataset                          |     |     |                                  | Dataset |     |     |     |     |     |
| --- | --- | -------------------------------- | --- | --- | -------------------------------- | ------- | --- | --- | --- | --- | --- |
|     |     | (a) Time cost with point anomaly |     |     | (b) Time cost with range anomaly |         |     |     |     |     |     |
0.00
10−2
|     |     |     |     |     |     |     |     | 5 7.5 | 1012.51517.52022.525 | 5 7.5 1012.51517.52022.525 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------------------- | -------------------------- | --- |
Figure3:Timecostovervariousdatasets Anomaly rate % Anomaly rate %
|     |     |     |     |     |     |     |     | (a) F-measure on Uni-poing-g |     | (b) Time cost on Uni-point-g |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | ---------------------------- | --- |
withdifferentgeneratingseedsandreporttheaverageresults.The
summaryofalldatasetscanbefoundinTable3.
4.1.2 EvaluationMetrics.
|                 | Accuracy. | Differentmetricsareusedwithrespecttoanomaly |               |     |                          |     |     |     |     |     |     |
| --------------- | --------- | ------------------------------------------- | ------------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
| types.𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 |           | =                                           | 𝑇 𝑃 and𝑅𝑒𝑐𝑎𝑙𝑙 |     | = 𝑇 𝑃 𝐹𝑁[2]areutilizedas |     |     |     |     |     |     |
|                 |           | 𝑇𝑃                                          | + 𝐹𝑃          |     | 𝑇𝑃 +                     |     |     |     |     |     |     |
pointmetrics,whereTP,FP,FNarethenumberoftruepositives, Figure4:Varyingrateson(a-b)Uni-point-g(c-d)Tao
falsepositives,andfalsenegatives,respectively.Wechooseare-
centmetricproposedforsubsequenceanomalywhichfocuseson
theoverlapofpredictedanomalyandtrueanomaly[53]asrange
(orsubsequence)metric.Specifically,givenasetofrealanomaly Point.WecanseethatNETSalwayshavehighaccuracyacross
ranges𝑅 {𝑅 ,...,𝑅 }andasetofpredictedanomalyranges alldatasets.Starereliesheavilyontheparameterindicatingthe
|     |     | = 1 | 𝑁𝑟  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑁
𝑃 {𝑃 ,...,𝑃 },wehave𝑅𝑒𝑐𝑎𝑙𝑙 𝑇(𝑅,𝑃) ∑︁ 𝑟 𝑅𝑒𝑐 𝑎 𝑙𝑙𝑇(𝑅𝑖,𝑃) numberofanomalypointsineachwindow.Complexdistributions
|     | = 1 | 𝑁𝑝  |     |     | = 𝑖 | = 1 𝑁 | and |                                                          |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | -------------------------------------------------------- | --- | --- | --- |
|     |     |     |     |     |     | 𝑟     |     | ofrealanomaliesresultsinitsrelativelyloweraccuracy.Asfor |     |     |     |
∑︁ 𝑁 𝑝
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 𝑇(𝑅,𝑃)= 𝑖 𝑃𝑟𝑒𝑐 𝑖𝑠 𝑖𝑜𝑛𝑇(𝑅,𝑃𝑖) deeplearningmethods,allexceptRCoderareclosetoNETSon
|                              |     |     | = 1 | 𝑁        | .Ingeneral,thedefaultset- |                    |     |                                                       |                  |                       |           |
| ---------------------------- | --- | --- | --- | -------- | ------------------------- | ------------------ | --- | ----------------------------------------------------- | ---------------- | --------------------- | --------- |
|                              |     |     |     | 𝑝        |                           |                    |     | Yahoo and                                             | perform worse on | others. RCoder, which | cannot be |
| tingFlatbias[53]isemployed.𝐹 |     |     |     | −𝑚𝑒𝑎𝑠𝑢𝑟𝑒 |                           | 2∗𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑅𝑒𝑐𝑎𝑙𝑙 |     |                                                       |                  |                       |           |
|                              |     |     |     |          | =                         | 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙   |     | usedforunivariatedataduetoitsmechanism,performsbeston |                  |                       |           |
appliesforbothmetrics.
ECGwith32dimensionsbutpoorlyonotherswhosedimensions
aresmallerthannine.Overall,itissurprisingthatdeeplearning
|     | Efficiency. | Apartfromloadingthedatafromthefileandresult |     |     |     |     |     |     |     |     |     |
| --- | ----------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
methodsdonotbehavewell.Thepossiblereasonisthatthenumber
evaluation,thetotaltimeofalltheotherprocedureswillbeadded
ofdatainstancesanddimensionsarenotsufficienttolearnagood
andreportedasthetimecostofthetargetmethod.
model.Figure3(a)showstheefficiencyofeachmethod.Weonly
showthefirst4datasets,sinceothersaresimilar.NETScomputes
| 4.1.3 | ParameterSearch. |     | Inordertocomparemethodsfairlyand |     |     |     |     |     |     |     |     |
| ----- | ---------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
precisely(underbestconfigurations),thoughallofthemareunsu- onaselectedsub-dimension,makingitthemostefficientmethod.
pervisedmethods,westillemployasystematic(hyper)-parameter TranADshowsthebesttimeefficiencyduetoitsarchitecture.
searchprocess.Specifically,wedesignasearchspaceforeachpara- Sub.MultivariatemethodsPBADandBeatGANachievehigher
meter(includingthreshold)accordingtothesuggestionsintheir accuracythanunivariatemethodsonmultivariatedata.Inpartic-
ular,univariatemethodshavehighrecallbutverylowprecision.
paper,e.g.,forUSADwetunethelatentsizewith{2,5,10,20}[3]
orbasedonthedistributionsofthetargetdataset.Wethensplit LRRDSperformsbetterthanPBADandBeatGANonlyonSed.This
thedatasetintotraining,validationandtestsetwitha‘4:1:5’ra- isbecausethemeanofabnormalpatternsinSedisobviouslylower
tio.It’sworthnotingthatthetrainingsetsareanomaly-free,as thanthatofnormalpatterns,soLRRDSiseasiertoidentifywith
requiredby[3,17,52,58].Theparameterwiththebestperformance embeddingtechniquesthansimplemeanandlengthfeatures.Asfor
invalidationsetwillbesettledfortesting. univariatemethods,NormAcanperformquitewellonallunivariate
data.MERLINperformsexceptionallywellonPower,showingthe
4.2 Intra-classComparisons capabilityoverseasonality.SANDdoesnotperformwellonlong
anomalies(e.g.,thelengthoftheanomalyinPoweris750).Ithasto
Asmentionedearlier,articlespresentingnewmethodsofteninclude
decomposealargematrixmanytimesiftheanomalyhasalarge
suchcomparisons,butthevarietyofcaseswithrespecttofactors
length.Wenotethatittakesmuchmoretimewhenthelengthof
| and | datasets | is often | limited. | For simplicity, |     | we use | "Point" to |     |     |     |     |
| --- | -------- | -------- | -------- | --------------- | --- | ------ | ---------- | --- | --- | --- | --- |
denote the results of point methods and "Sub" of subsequence theanomalyisgreaterthan100.BothGrammarVizandPBADuse
apatternminingapproachtoidentifysequencepatterns,sothey
methods."Summary"standsforthetake-awayconclusions.
arecomparableonunivariatedatasets.
4.2.1 VaryingDatasets. Wefirstevaluatetheperformanceofall Summary.(1)Thereisnosuper-algorithmthatissuitableforall
methodsondifferentdatasetswiththeirbestparameters.Toobtain cases.(2)Givenproperparameters,NETScanperformbestinmost
theresultsoftheunivariatemethodsonmultivariatedata,werun cases.(3)PBADandBeatGANhavebetteroverallaccuracybutcost
themseparatelyoneachdimension(similarto[52]),andcombine moretime.(4)Deeplearningmethodsdonotoutperformotherson
allthereportedanomalies.ResultsareshowninTable4. datasetswithcomplexanomalypatterns.
488

Table4:Accuracyovervariousdatasets
|         | NETS |     | Stare | SHESD |     | TranAD |     | USAD |     | GDN |     | Omni |     | RCoder |
| ------- | ---- | --- | ----- | ----- | --- | ------ | --- | ---- | --- | --- | --- | ---- | --- | ------ |
| Dataset | P R  | F   | P R F | P     | R F | P R    | F   | P R  | F   | P R | F   | P R  | F   | P R F  |
Yahoo 0.727 1 0.842 0.429 0.375 0.400 1 0.625 0.769 0.368 0.875 0.519 0.368 0.875 0.518 0.368 0.875 0.519 0.471 1 0.64 - - -
Twitter 0.739 0.878 0.802 0.203 0.959 0.335 0.260 0.176 0.210 0.737 0.189 0.301 0.205 0.412 0.274 0.484 0.419 0.449 0.079 0.878 0.145 - - -
SMTP 0.400 0.375 0.387 0.294 0.313 0.303 0.001 1 0.003 0.001 0.188 0.003 0.001 0.222 0.002 0.004 0.022 0.007 0.250 0.375 0.300 0.001 0.312 0.001
DLR 0.468 0.424 0.445 0.109 0.517 0.179 0.061 1 0.115 0.115 0.224 0.152 0.115 0.224 0.154 0.118 0.852 0.060 0.180 0.180 0.180 0.030 0.252 0.053
ECG 0.484 0.441 0.462 0.239 0.267 0.252 0.373 0.430 0.399 0.160 0.557 0.248 0.280 0.293 0.286 0.232 0.328 0.272 0.347 0.165 0.224 0.640 0.426 0.512
Dataset PBAD LRRDS BeatGAN SAND NP MERLIN GrammarViz NormA IDK
|     | P R | F P | R F P | R   | F P | R F | P R | F P | R   | F P | R F | P R | F   | P R F |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Power 0.262 0.758 0.389 0.415 0.248 0.310 0.498 0.340 0.404 0.159 0.156 0.157 0.575 0.575 0.575 0.936 0.998 0.966 0.453 0.222 0.298 0.868 0.810 0.838 0.343 0.244 0.285
Sed 0.310 0.800 0.446 0.597 0.972 0.739 0.690 0.723 0.706 0.657 0.769 0.708 0.695 0.814 0.750 0.505 0.829 0.627 0.435 0.533 0.479 0.435 0.669 0.527 0.938 0.938 0.938
Taxi 0.143 0.664 0.235 0.164 0.463 0.242 0.354 0.437 0.391 0.250 0.242 0.246 0.468 0.498 0.482 0.460 0.460 0.460 0.333 0.135 0.192 0.441 0.533 0.482 0.498 0.373 0.427
Machine 0.227 0.500 0.312 0.073 0.500 0.127 0.521 0.471 0.495 0.100 0.106 0.103 0.009 0.018 0.012 0.143 0.429 0.215 0.197 1 0.33 0.171 0.332 0.226 0.429 0.454 0.441
Exercise 0.495 1 0.662 0.283 0.656 0.396 0.756 0.760 0.758 0.293 0.672 0.408 0.309 0.983 0.470 0.377 0.971 0.543 0.553 0.745 0.635 0.292 0.743 0.420 0.171 0.405 0.245
Exathlon 0.515 0.856 0.643 0.197 0.341 0.250 0.299 0.694 0.418 0.206 1 0.341 0.149 0.993 0.259 0.200 1 0.334 0.147 1 0.256 0.095 0.849 0.170 0.169 1 0.289
Swat 0.185 0.566 0.279 0.286 0.124 0.173 0.340 0.233 0.276 0.082 0.993 0.151 0.055 1 0.104 - - - 0.137 1 0.242 0.063 0.529 0.113 0.041 1 0.079
Smd 0.294 0.303 0.298 0.676 0.098 0.171 0.273 0.235 0.253 0.070 0.925 0.129 0.082 0.980 0.151 0.063 0.732 0.116 0.018 1 0.035 0.088 0.742 0.157 0.085 0.799 0.154
|     | PBAD  | BeatGAN | NP     | GrammarViz |     | IDK |     |      | NETS  | SHESD  |     | USAD | Omni   |     |
| --- | ----- | ------- | ------ | ---------- | --- | --- | --- | ---- | ----- | ------ | --- | ---- | ------ | --- |
|     | LRRDS | SAND    | MERLIN | NormA      |     |     |     |      | Stare | TranAD |     | GDN  | Rcoder |     |
| 1.0 |       |         |        |            |     |     |     | 1.00 |       |        |     | 101  |        |     |
102
0.8
| erusaem-F |     |     | )s( tsoc emiT |     |     |     | erusaem-F | 0.75 |     |     | )s( tsoc emiT | 100 |     |     |
| --------- | --- | --- | ------------- | --- | --- | --- | --------- | ---- | --- | --- | ------------- | --- | --- | --- |
| 0.6       |     |     | 101           |     |     |     |           |      |     |     |               |     |     |     |
|           |     |     |               |     |     |     |           | 0.50 |     |     | 10−1          |     |     |     |
0.4
|     |     |     | 100  |     |     |     |     |      |     |     | 10−2 |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- |
| 0.2 |     |     |      |     |     |     |     | 0.25 |     |     |      |     |     |     |
| 0.0 |     |     | 10−1 |     |     |     |     | 0.00 |     |     | 10−3 |     |     |     |
5 7.5 1012.51517.52022.525 5 7.5 1012.51517.52022.525 1k 2k 5k 10k 20k 50k 100k 1k 2k 5k 10k 20k 50k 100k
|     | Anomaly rate % |     |     | Anomaly rate % |     |     |     |     | Data size |     |     |     | Data size |     |
| --- | -------------- | --- | --- | -------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --------- | --- |
(a) F-measure on Uni-sub-g (b) Time cost on Uni-sub-g (b) Time cost on Uni-point-g
(a) F-measure on Uni-poing-g
| 0.8 |     |     | 101 |     |     |     |     |     |     |     |     | 103 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1.00
| 0.6       |     |     | )s( tsoc emiT |     |     |     |           | 0.75 |     |     | )s( tsoc emiT |     |     |     |
| --------- | --- | --- | ------------- | --- | --- | --- | --------- | ---- | --- | --- | ------------- | --- | --- | --- |
| erusaem-F |     |     |               |     |     |     | erusaem-F |      |     |     |               | 101 |     |     |
| 0.4       |     |     |               |     |     |     |           | 0.50 |     |     |               |     |     |     |
10−1
| 0.2 |     |     |     |     |     |     |     | 0.25 |     |     |      |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- |
| 0.0 |     |     | 100 |     |     |     |     | 0.00 |     |     | 10−3 |     |     |     |
5 7.5 1012.51517.52022.525 5 7.5 1012.51517.52022.525 1k 2k 5k 10k 20k 50k 100k 1k 2k 5k 10k 20k 50k 100k
|     | Anomaly rate % |     |     | Anomaly rate % |     |     |     |     | Data size |     |     |     | Data size |     |
| --- | -------------- | --- | --- | -------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --------- | --- |
(c) F-measure on Mul-sub-s (d) Time cost on Mul-sub-s (c) F-measure on TAO (d) Time cost on TAO
Figure5:Varyingrateson(a-b)Uni-sub-g(c-d)Mul-sub-s Figure6:Varyingsizeson(a-b)Uni-point-g(c-d)Tao
| 4.2.2 | VaryingAnomalyRate𝑎%. |     | [61]claimsthatcurrentdatasets |     |     |     |                  |     |     |                                      |     |     |     |     |
| ----- | --------------------- | --- | ----------------------------- | --- | --- | --- | ---------------- | --- | --- | ------------------------------------ | --- | --- | --- | --- |
|       |                       |     |                               |     |     |     | timecomplexityof |     |     | MERLINandGrammarVizislinearlyrelated |     |     |     |     |
containtoofewanomaliesforevenasimplemethodtofindthem.
tothenumberofanomaloussubsequences.Whenwecomparethe
However,themajorityofthedatashouldbenormal.Therefore,we resultsofthedifferentmethods,wefindthatmostofthem,suchas
varyanomalyratesfrom5%to25%totestthesensitivityofthe
PBAD,remainstableorperformbetterwhentheanomalyrateis
methodsonsyntheticdatasets.Thedatasizeis10kforpointand
lower,butgraduallybecomeworseastheanomalyrateincreases.
5kforsubsequenceanomalies.
Incontrast,LRRDSandBeatGANperformsevenbetteratahigher
Point.AsillustratedinFigures4(a,c),allnon-deeplearningmeth-
anomalyrate,whichisduetothereductionoffalsepositivescaused
odsarerelativelystable.NETSperformabitworseonTaowhenthe byroughrecognitionofanomalypoint.
anomalyrateachieves25%.Sinceitisdifficulttosetanappropriate Summary.(1)Methodsarestablewhenanomalyisrare(<25%),
| 𝜃 𝑘 and𝜃 | 𝑅 toidentifytheanomalouspointsbecausetheyalsohave |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whichisdifferenttothestatementsaboutrandomdetectionin[44].
asimilarnumberofneighborsasnormalpoints.Onthecontrary,
(2)Amethodmayperformbetterasanomalyrateincreasessince
mostdeeplearningmethodsachieveabetterresultwithincreasing
thelargenumberofthereportedfalsepositivescanbecometrue
anomalyrate.ThismaybebecauseTranAD,USAD,andGDNfailto positives.(3)Anomalyrateshowslittleeffectontheefficiency.
learnagoodmodel(evenwiththebestparameterviagridsearch)
andtendtopredictmorepointsasanomalies.Therefore,morefalse 4.2.3 VaryingDataSize𝑛. Tocheckthesensitivityandscalability
positivesbecometruepositiveswhentheanomalyrateincreases. againstthedatasize,werunexperimentsbyvaryingdatasizes
OminiandRCodermanagetolearnabettermodelandperform from1kto100konrealandsyntheticdatasetswith10%anomalies.
wellonUni-point-gandTao,respectively. Point.TheresultsinFigures6(b,d)showthatallmethodscost
Sub.Figures5(b,d)showthat,thetimecostsofallmethodsre- moretimeasthedatasizeincreases.Intermsofaccuracy,they
mainconstantforbothunivariateandmultivariatedata,except showconsistentresultsagainstthedatasize.ItisnotedthatSHESD
forMERLINandGrammarViz,whichisduetothefactthatthe makesexceptionsinsomecases.StareandNETSarethetwofastest
489

|     | PBAD  | BeatGAN |     | NP GrammarViz |     | IDK | NETS  | SHESD  | Rcoder GDN |     |      |      |             |
| --- | ----- | ------- | --- | ------------- | --- | --- | ----- | ------ | ---------- | --- | ---- | ---- | ----------- |
|     |       |         |     |               |     |     | Stare | TranAD | USAD Omni  |     |      | NETS | Stare SHESD |
|     | LRRDS | SAND    |     | MERLIN NormA  |     |     | 1.00  |        |            |     | 10−1 |      |             |
104
| 1.0 |     |     |     |     |     |     | 0.75 |     |     | )s(tsoc emiT |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ------------ | --- | --- | --- |
erusaem-F
| 0.8       |     |     | )s( tsoc emiT |     |     |     |      |     |     |     |     |     |     |
| --------- | --- | --- | ------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
| erusaem-F |     |     |               | 102 |     |     | 0.50 |     |     |     |     |     |     |
0.6
0.25
| 0.4 |     |     |     |     |     |     |     |     |     |     | 10−2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
100
|     |     |     |     |     |     |     | 0.00 | Global                 | Contextual |     |     | Global                 | Contextual |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---------------------- | ---------- | --- | --- | ---------------------- | ---------- |
| 0.2 |     |     |     |     |     |     |      | Anomaly pattern        |            |     |     | Anomaly pattern        |            |
|     |     |     |     |     |     |     |      | (a) F-measure on Stock |            |     |     | (b) Time cost on Stock |            |
0.0
1k 2k 5k 10k 20k 50k 100k 1k 2k 5k 10k 20k 50k 100k PBAD SAND MERLIN NormA PBAD SAND MERLIN NormA
Data size Data size LRRDS NP GrammarViz IDK LRRDS NP GrammarViz IDK
|     | (a) F-measure on Uni-sub-g |     |     | (b) Time cost on Uni-sub-g |     |     | BeatGAN |     |     |     |     |     |     |
| --- | -------------------------- | --- | --- | -------------------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
1.00
| 1.0           |     |     |               | 103 |     |     |                |     |     |              |     |     |     |
| ------------- | --- | --- | ------------- | --- | --- | --- | -------------- | --- | --- | ------------ | --- | --- | --- |
|               |     |     |               |     |     |     | erusaem-F 0.75 |     |     | )s(tsoc emiT | 101 |     |     |
| erusaem-F 0.8 |     |     | )s( tsoc emiT | 102 |     |     | 0.50           |     |     |              |     |     |     |
100
| 0.6 |       |                |      | 101       |         |          | 0.25        |                          |       |     |        |                          |       |
| --- | ----- | -------------- | ---- | --------- | ------- | -------- | ----------- | ------------------------ | ----- | --- | ------ | ------------------------ | ----- |
| 0.4 |       |                |      | 100       |         |          | 0.00 Global | Seasonal                 | Trend |     | Global | Seasonal                 | Trend |
|     |       |                |      |           |         |          |             | Anomaly pattern          |       |     |        | Anomaly pattern          |       |
|     |       |                |      |           |         |          |             | (c) F-measure on Uni-sub |       |     |        | (d) Time cost on Uni-sub |       |
| 0.2 |       |                |      | 10−1      |         |          |             |                          |       |     |        |                          |       |
|     | 1k 2k | 5k 10k 20k 50k | 100k | 1k 2k 5k  | 10k 20k | 50k 100k |             |                          |       |     |        |                          |       |
|     |       | Data size      |      | Data size |         |          |             |                          |       |     |        |                          |       |
(c) F-measure on Mul-sub-s (d) Time cost on Mul-sub-s Figure9:Varyingpatternson(a-b)point(c-d)subsequence
Figure7:Varyingsizeson(a-b)Uni-sub-g(c-d)Mul-sub-s
|     |     |     |     |     |     |     |            | 9          | 8 7 | 6 5 | 4 3 | 2 1      |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | --- | --- | -------- | --- |
|     |     |     |     |     |     |     |            | MERLIN 8.9 |     |     |     | 1.0 NP   |     |
|     |     |     |     |     |     |     |            | LRRDS 8.1  |     |     |     | 2.4 SAND |     |
|     |     |     |     |     |     |     | BeatGAN    | 6.9        |     |     |     | 3.2 IDK  |     |
|     |     |     |     |     |     |     | GrammarViz | 5.9        |     |     |     | 3.4 PBAD |     |
|     |     |     |     |     |     |     |            | NormA 5.2  |     |     |     |          |     |
Figure10:Criticaldifferencediagramonsubg
|     |     |     |     |     |     |     | 4.2.4 VaryingDataDimension|𝐷|. |     |     |     | Hereweperformexperiments |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | ------------------------ | --- | --- |
onrealdatasetsbyvaryingthedimensionsofthedata.
Point.Figures8(a-b)showthatallmethodshavebetterresultswith
|     |     | PBAD | LRRDS | BeatGAN |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.3 largerdimensions.Besides,weneedtoadjusttheparameter𝜃 𝑅with
102
)s( tsoc emiT thechangeindimensiontogetareasonableresult.Wealsoretrain
erusaem-F 0.2
themodelsofthedeeplearningmethods,whichresultsinallbut
|     |     |     |     | 101 |     |     | RCoderremainingstableasthedatadimensionincreases.RCoder |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
0.1
hasmorereferencedataandestimatorswithmoredatadimensions,
100 whichsignificantlyincreasesitsaccuracy.Intermsofefficiency,all
| 0.0 | 1 5 | 10 20 30 40 | 50  | 1 5 10 | 20 30 | 40 50 |     |     |     |     |     |     |     |
| --- | --- | ----------- | --- | ------ | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
Data dimension Data dimension distance-basedmethodscostmoretimeasthedimensionincreases,
|     | (c) F-measure on Swat |     |     | (d) Time cost on Swat |     |     |     |     |     |     |     |     |     |
| --- | --------------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sinceitismoreexpensivetocomputethedistance.
Sub.Theresultofthesubsequenceanomalycanbecheckedin
Figure8:Varyingdimensionson(a-b)ECG(c-d)Swat
Figure8(c-d).LRRDSappliesdimensionalcompressionandexhibits
greatscalability.Incontrast,PBADmustextractthefeaturesineach
dimension,whichresultsinasignificantlyhighertimeoverheadas
methods.Thelattertwoalgorithmstakeadvantageofthe“seteffect"
thedimensionincreases.Sincetheanomalyislocalizeddifferently
thatskipsadditionalupdateswhennewdataarrives.
ineachdimensionofSwat,itisnotsurprisingthatperformance
Sub.AscanbeseeninFigure7,mostpattern-basedmethodsshow varieswidelyacrossallmethods,includingBeatGAN.
unstableresultsforsmall(e.g.,5k)becauseitisdifficulttoextract Summary.(1)LRRDSscaleswellwithdatadimension,whileNETS,
patterns.Whenthedataislargeenough,theresultsofthesub-
Stare,andPBADaresignificantlyaffectedbyit.(2)Thesparsity
sequencemethodsareusuallyquiteconsistent.LRRDSreflectsthe
problemcanbehandledbyagoodparametersetting.(3)Sincethe
| sametrendinSection4.2.2.Wedonotreporttheresultsof |     |     |     |     |     | LRRDS |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
numberofestimatorsincreaseswiththedatadimension,RCoder
after20kbecauseitisoutofmemoryanddonotreporttheresults achievesbetterresultswithhigherdimensions.(4)NETSisrecom-
ofMERLINafter10kbecauseittakesmorethanadaytorun.Both
mendedwhendatadimensionislimited(<30).(5)RCoderisagood
ofthemshowpoorscalability.
choicewhendatadimensionislarge(>30).
Summary.(1)Stare,NETS,andNormAhavegoodefficiency(also
referredtotheresultsinFigure3).(2)Smalldatasize(<10k)may 4.2.5 VaryingAnomalyPatterns. Finally,wetesttheselectedal-
leadtounstableresultsforsubsequencemethods.(3)Werecom- gorithmsfordifferentpatternsofanomalies.
mendIDKwhenthedatasizeismorethan50kbecauseitprovides Point.AsshowninFigures9(a-b),allmethodsachievebetterac-
goodscalabilityandstableperformance. curacyforglobalanomaly(0.618)thancontextualanomaly(0.551),
490

which is consistent with the common sense. They have similar NETS Stare SHESD
efficiencyforthesetwoanomalypatterns.
|     |     |     |     |     |     |     | 0.4 |     |     | )sm( tsoc emiT |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- |
Sub.TheresultforthesubsequencecaseisshowninFigures9(c-d). erusaem-F 103
| Theaveragef-measuresare0.550,0.619,and0.398forglobal,sea- |     |     |     |     |     |     | 0.3 |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sonal,andtrendanomaly,respectively.Consistentwithprevious
|     |     |     |     |     |     |     | 0.2 |     |     | 101 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
observations,PBADandNormAhasstableperformanceacrossall
0.1
patterns.SANDandNPperformparticularlywellonglobalandsea- 200 1000 2000 5000 800010000 200 1000 2000 5000 800010000
|     |     |     |     |     |     |     |     | Window size |     |     | Winidow size |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ------------ | --- |
sonaloutliers.DetectingtrendoutliersischallengingforBeatGAN (c) F-measure on ECG (d) Time cost on ECG
andIDK,reflectingtheneedforimprovementofnon-stationary 0.6 104
timeseries.Tofindoutwhethertherearemethodsthatfitallpat- )sm( tsoc emiT
erusaem-F
| terns,weapplytheFriedmantest[20]andapost-hocWilcoxon |     |     |     |     |     |     | 0.4 |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
test[60](with𝛼=0.05)tothef-measuresfordifferentanomalypat- 102
0.2
terns.First,theFriedmantestsyieldap-valuegreaterthan0.05and
thusdonotindicatethatthesemethodsaresignificantlydifferent. 0.0 100
|     |     |     |     |     |     |     | 30 300 | 600 | 750 1500 | 3000 30 | 300 600 750 | 1500 3000 |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | -------- | ------- | ----------- | --------- |
Figure10showsthecriticaldifferencediagram[16]fortheglobal Silde size Silde size
anomalyasanexample.Methodsthatarenotconnectedbyabold (c) F-measure on ECG (d) Time cost on ECG
linediffersignificantlyintheiraverageranks.Thisprovesthatfor
Figure11:Varying(a-b)windowsizes(c-d)slidesizesonECG
asingleanomalypatternthereisaparticularmethodthatclearly
outperformstheothers.Forexample,NPnotonlyachievesfirst
placeforglobaloutliers,butalsosignificantlyoutperformsothers. 4.3.1 UnivariateMethodsinMultivariateDatasets. Asreportedin
| Summary.(1)Inpointmethods,global |     |     |     | anomaliesareeasierto |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Section4.2.1,thepointmethodSHESDlagsfarbehindmultivariate
detectthancontextualones.(2)Insubsequencemethods,seasonal ones,therefore,wefocusonthesubsequencecase.
anomaliesareeasiesttofind,whiletrend anomaliesarehardest Settings.Ifthedetectedanomaliesindifferentdimensionsoverlap
tofind.(3)Noonemethodfitsallpatterns.Butcertainmethods aftercombination,wemergethemintoalargerange(subsequence)
areclearlybetterthanothersforaparticularanomalypattern,e.g.,
asthefinalresult.Followingthesamelogic,wealsorunmultivariate
| NP performsbestfortheglobalanomaly.(4) |     |     |     | SAND | andIDKare |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
methods(PBADandBeatGAN)foreachdimensionseparatelyand
notsuitablefornon-stationarytimeseries(withtrend anomaly). combinethedetectedanomaliesfordirectcomparison,theresults
(5)Distance-basedmethodsarewellsuitedforglobalandseasonal ofwhicharedisplayedinthe‘Combination’columninTable5.
anomalies.(6)IDKcanalsoworkwellforglobalanomaly,whichis WenotethatanomaliesinExercise(similarresultsareobserved
differentfromRI(8)in[49].
inotherrealdatasets)alwaysoccurinalldimensionsatthesame
position.Therefore,wetesttheeffectsofsuch‘overlap’onanother
4.3 Inter-classComparisons
syntheticdata.The‘ncor’indicatesthatpositionsofthegenerated
anomaliesaredifferentineachdimension.‘A1-A3’denotethethree
Inthissection,wewilltesttheperformanceofmethodsbetween
dimensions.
differentclassesunderthesamefacet.Inthedatadimensionfacet,
werununivariatemethodsseparatelyforeachdimensionofthe Results.Comparedwiththeresultsoneachdimensionandafter
multivariatedataandthencombinetheresults.Intheprocessing combination,mostofthemethodshaveapromotiononrecallbut
techniquefacet,werunonlinemethodsacrossdifferentwindowand asharpreductiononprecision,sincetheaggregationineachdi-
slidesizesondatasetslargerthan100kandwithdimensionslarger mensionwillinvolveinmorepredictedanomalies(covermorereal
|     |     |     |     |     |     |     | anomalies | but also | much more | false positives). | Compared | with |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --------- | ----------------- | -------- | ---- |
than30.Intheanomalytypefacet,asmentionedinSection1,werun
combinedresultsonthesyntheticdata,wefindoutthatanomaly
bothpointandsubsequencemethodsondatasetswithsubsequence
anomaliesunderdifferentevaluationmetricstoanalyzetheimpact positions(co-occurornot)donotclearlyimpacttheeffectiveness
ofthemetricsandtheadjustmentinpredictions.Inaddition,we and efficiency. Univariate methods can achieve good results on
alsotesttheimpactofthresholdsandperformanceunderdifferent somespecificdimensionsbutactspoorlyoverall,whilemultivariate
onesperformtheopposite,showingtheadvantageofconsidering
applicationaspects.
relationshipsoverdimensions.
|     |     |     |     |     |     |     | Summary. | Promotion | on efficiency | cannot | compensate | for the |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------------- | ------ | ---------- | ------- |
sharpdropinaccuracy(weomitefficiencyresultsandshowonein
Table5:Performanceonsingledimensionandcombination
motivatingscenario1).Multivariatemethodsarebetter,unlesswe
havesufficientpriorknowledgeaboutspecificdimensions.
| Dataset  | PBAD          | BeatGAN |             | SAND |     | NP  |                                         |     |     |     |                   |     |
| -------- | ------------- | ------- | ----------- | ---- | --- | --- | --------------------------------------- | --- | --- | --- | ----------------- | --- |
|          | P R           | F P     | R F         | P R  | F P | R F |                                         |     |     |     |                   |     |
|          |               |         |             |      |     |     | 4.3.2 OnlineMethodsinBatchedTimeSeries. |     |     |     | AsexplainedinSec- |     |
| Exercise | 0.495 1 0.662 | 0.756   | 0.760 0.758 |      |     |     |                                         |     |     |     |                   |     |
Combination 0.220 1 0.360 0.332 0.997 0.498 0.293 0.672 0.408 0.309 0.983 0.47 tion4.2.1,theonlinemethodSANDsuffersfromtheiterationsof
| E_A1 | 0.357 1 0.526 | 0.708 | 0.72 0.714  | 0.483 0.513 0.498 | 0.894 | 0.943 0.918 |            |                |     |                    |                  |     |
| ---- | ------------- | ----- | ----------- | ----------------- | ----- | ----------- | ---------- | -------------- | --- | ------------------ | ---------------- | --- |
|      |               |       |             |                   |       |             | eigenvalue | decompositions |     | and its efficiency | is significantly | af- |
| E_A2 | 0.389 1 0.560 | 0.505 | 0.498 0.501 | 0.27 0.275 0.272  | 0.222 | 0.224 0.223 |            |                |     |                    |                  |     |
E_A3 0.352 0.719 0.473 0.249 0.248 0.248 0.192 0.204 0.197 0.196 0.202 0.199 fected.Thus,wefocusonthepointcase.
| Mul_ncor_g | 0.684 1 0.813 | 0.514 | 0.753 0.611 |     |     |     |     |     |     |     |     |     |
| ---------- | ------------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Combination 0.097 1 0.178 0.215 0.861 0.344 0.250 0.897 0.391 0.279 0.941 0.431 Settings.WeruntwoexperimentsinECGvaryingwindowsizes
| M_A1 | 0.092 0.300 0.140 | 0.219 | 0.246 0.232 | 0.315 0.329 0.322 | 0.377 | 0.463 0.416 |                    |     |                                             |     |     |     |
| ---- | ----------------- | ----- | ----------- | ----------------- | ----- | ----------- | ------------------ | --- | ------------------------------------------- | --- | --- | --- |
|      |                   |       |             |                   |       |             | 𝜃 𝑊 andslidesizes𝜃 |     | 𝑆.Similarresultsareobservedinotherdatasets. |     |     |     |
| M_A2 | 0.083 0.390 0.137 | 0.222 | 0.355 0.273 | 0.261 0.353 0.300 | 0.245 | 0.368 0.294 |                    |     |                                             |     |     |     |
M_A3 0.107 0.402 0.168 0.223 0.358 0.275 0.311 0.42 0.357 0.217 0.325 0.260 𝜃 𝑆 =150inthefirstcaseand𝜃 𝑊 =3𝑘inthesecond.Itshouldbe
491

|           |     | PBAD NP    | IDK           | TranAD |     | noitavresbO | 2.5 |     | 2.5  |     |     |
| --------- | --- | ---------- | ------------- | ------ | --- | ----------- | --- | --- | ---- | --- | --- |
|           |     | SAND NormA | NETS          |        |     |             | 0.0 |     | 0.0  |     |     |
| 1.0       |     |            | 102           |        |     | −2.5        |     |     | −2.5 |     |     |
| 0.8       |     |            | )s( tsoc emiT |        |     |             | 2.5 |     | 2.5  |     |     |
| erusaem-F |     |            |               |        |     | DABP        |     |     |      |     |     |
| 0.6       |     |            | 100           |        |     |             | 0.0 |     | 0.0  |     |     |
| 0.4       |     |            |               |        |     | −2.5        |     |     | −2.5 |     |     |
|           |     |            |               |        |     |             | 2.5 |     | 2.5  |     |     |
10−2
| 0.2 |                            |                |     |                            |              | DNAS | 0.0 |     | 0.0  |     |     |
| --- | -------------------------- | -------------- | --- | -------------------------- | ------------ | ---- | --- | --- | ---- | --- | --- |
| 0.0 |                            |                |     |                            |              | −2.5 |     |     | −2.5 |     |     |
|     | 20 30                      | 40 50 60 70    | 100 | 20 30 40                   | 50 60 70 100 |      |     |     |      |     |     |
|     |                            | Anomaly length |     | Anomaly length             |              |      | 2.5 |     | 2.5  |     |     |
|     | (a) F-measure on Uni-sub-g |                |     | (b) Time cost on Uni-sub-g |              | STEN |     |     |      |     |     |
|     |                            |                |     |                            |              |      | 0.0 |     | 0.0  |     |     |
| 1.0 |                            |                | 102 |                            |              |      |     |     |      |     |     |
|     |                            |                |     |                            |              | −2.5 |     |     | −2.5 |     |     |
0.8
| erusaem-F |     |     | )s( tsoc emiT 101 |     |     | DAnarT | 2.5 |     | 2.5 |     |     |
| --------- | --- | --- | ----------------- | --- | --- | ------ | --- | --- | --- | --- | --- |
0.6
|     |     |     |     |     |     |     | 0.0 |     | 0.0 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
100
| 0.4 |     |     |      |     |     | −2.5 |     |               | −2.5    |               |     |
| --- | --- | --- | ---- | --- | --- | ---- | --- | ------------- | ------- | ------------- | --- |
|     |     |     |      |     |     |      | 200 | 300 400 500   | 600 200 | 300 400 500   | 600 |
| 0.2 |     |     | 10−1 |     |     |      |     | Timestamp     |         | Timestamp     |     |
|     |     |     |      |     |     |      |     | (a) Uni-sub-g |         | (b) Uni-sub-s |     |
0.0
|     | 20 30 | 40 50 60 70    | 100 | 20 30 40       | 50 60 70 100 |     |     |     |     |     |     |
| --- | ----- | -------------- | --- | -------------- | ------------ | --- | --- | --- | --- | --- | --- |
|     |       | Anomaly length |     | Anomaly length |              |     |     |     |     |     |     |
(c) F-measure on Uni-sub-s (d) Time cost on Uni-sub-s Figure13:Casestudyon(a)Uni-sub-g(b)Uni-sub-s
Figure12:Varyinglengthson(a-b)Uni-sub-g(c-d)Uni-sub-s
|            |     |     |     |     |     |     | Ground Truth      | 0 1 1 1 1 0                                | 0 1 1 1 1 1 1 0 0 1 | 1 0 0 1 1 1 1 1 0 |     |
| ---------- | --- | --- | --- | --- | --- | --- | ----------------- | ------------------------------------------ | ------------------- | ----------------- | --- |
|            |     |     |     |     |     |     | TP P :3 r ,  e FN | d :1 ic 2, t  F i 1 o :0 n .30 0 0 0 0 0 0 | 0 0 1 0 0 0 0 0 0 0 | 0 0 0 0 1 0 1 0 0 |     |
| notedthat𝜃 |     | 𝜃   |     |     |     |     |                   |                                            | After point-adjust  |                   |     |
𝑆 ≤ 𝑊 alwaysholds.ThebatchmethodSHESDis A d j u s t   R e s u lt 0 0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 1 1 1 1 1 0
|     |     |     |     |     |     |     | T P :1 1 , F | N : 4 ,  F1 :0 .7 9 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------------- | --- | --- | --- |
usedasabaseline.
| Results.Figure11(a)showsthattheaccuracyof |     |     |     |     | NETSfirstin- |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
Figure14:Point-adjustmethod
creasesandthendecreaseswithincreasingwindowsize.Thereason
isthatifthewindowsizeistoosmall,itisdifficulttofindenough
neighborsevenforanormaldatapoint,leadingtofalsepositives. Results. Figure 12 shows the sensitivity of the methods to the
Ifthewindowsizeistoolarge,thenumberofneighborsforalocal anomalylengthℓ.PBADdoesnotidentifythesubsequencewhose
anomalypointmayexceedthepredefinedthreshold𝜃 𝑘,leadingto lengthisexactlyℓ,makingitdifferentfromothers.Othermethods
falsenegatives.AscanbeseeninFigure11(b),asexpected,alar- claimtoachievethebestaccuracywhenℓissimilartotheactual
| gerwindowsizecausesthemethodstoconsumemoredatapoints, |     |     |     |     |     | length(ℓ |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
=50)oftheanomalies,whichcanbeseeninFigures12(a,
whichcostsmoretime.OnepossibleexplanationforFigure11(c)is c).IDKdemonstratesrobustnessfortheinputlength,whilethebest
thatalargerslidesizeincreasesthevariationinthenumberofan- inputlengthatNormAisdifficulttopredict.Itisinterestingthat
omalypoints,whichdecreasestheaccuracyofStare.Ontheother NETSunderglobal patterns(inFigure12(a))canalsogivegood
hand,iftheslidesizeistoolarge,theintermediateinformation resultswithmuchlesstime(inFigure12(b)).InFigure13(a),we
storedforNETSchangestoomuch,whichalsonegativelyaffects
zoominon400datapointsintheUni-sub-gdatasetandhighlight
theaccuracy.RegardingtheefficiencyshowninFigure11(d),Stare theactualanomalyingreen,whiletheanomalyidentifiedbythe
takelesstimeastheslidesizeincreases.NETScannotexploitthe differentmethodsishighlightedinred.WefindoutthatPBAD
‘neteffect’whentheslidesizeisequaltothewindowsize.There- andSANDcancoverthewholeanomalysubsequence.NETSis
fore,itcantaketheleasttimeforamedium𝜃 𝑆.Itisnotedthateven alsoabletomatchsometrueanomaly(ontheright),whilethe
thefastestonlinemethodNETSwillbetentimesslowerthanthe
subsequencemethodsusuallyhavealagintheresult.Weperform
| simplebatchmethodSHESDwhen𝜃 |     |     |     | =10𝑘. |     |                                                           |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ----- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- |
|                             |     |     | 𝑊   |       |     | anotherexperimentwithUni-sub-sandfindsimilarresultsforthe |     |     |     |     |     |
Summary.(1)Largersizesdonotnecessarilyproducebetterres- subsequencemethodsintermsoflengthℓ.However,pointmethods
ults,butcostmoretime.(2)Onlinemethodscanoutperformbatch cannotgiveaccurateresultsinsuchcomplexcases(inFigure12(c)).
methodsunderapropersetting,duetotheevolvementcharacter- Combiningthesetwoobservations,wearguethatpointmethods
isticoftimeseries.
facilitatethedetectionofsomeglobaloutliers,whileanomalous
patternsrequiringlong-termcontextarehardtodetect.
| 4.3.3 | PointMethodsinSubsequenceAnomalies. |     |     | Subsequencemeth- |     |                                                 |     |     |     |     |      |
| ----- | ----------------------------------- | --- | --- | ---------------- | --- | ----------------------------------------------- | --- | --- | --- | --- | ---- |
|       |                                     |     |     |                  |     | Summary.(1)Pointmethodscanalsoworkwellforglobal |     |     |     |     | sub- |
odsalwaysconsidertheanomalylengthℓasaninputparameter[7].
sequenceanomalieswithextremevalues,whichmayhelprelax
However,thisaffectsaccuracytosomeextent,sincesubsequence
thelengthinputrequirement.(2)Thelengthparameterℓ,which
anomaliesinrealtimeseriesdatararelyhaveafixedlength.Incon-
isclosetotheactualanomalylength,givesgoodresults.Adaptive
trast,pointanomalymethodsrequirenosuchinput(thelengthis1).
inputlengthareneededtodealwithreal-worldsituations.
Therefore,wewouldliketoknowtheeffectofanomalylengthand
whetherwecanperformpointmethodsforsubsequenceanomalies. 4.3.4 EffectofMetricsandAdjustment. Usingpointmetricsfor
Settings.Weuseunivariatedatawithinjectedglobalandseasonal
datasetswithsubsequenceanomalywillbiastheaccuracyofmany
anomaliestoavoidtheeffectofdimensions.Weomittrendbecause timeseriesanomalydetectionsystemsbynotcapturingspecific
theyhavesimilarresultstoseasonal.Forbrevity,wereportonly properties[53].Forareal-timeapplication,itmightbemoreim-
NETSandTranAD,asotherpointmethodsperformsimilarly. portanttodetecttheearlierpartofananomalytoreduceresponse
492

Table6:F-measurew/opoint-adjustunderdifferentmetrics
|     |     |     |     |     |     |     |     |     |     | RCoder Omni | GDN | TranAD | USAD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | ---- |
0.5
1.0
| Algorithm |         |             | PointMetric        |         |          | RangeMetric |         | 0.4       |     |     | 0.8       |     |     |
| --------- | ------- | ----------- | ------------------ | ------- | -------- | ----------- | ------- | --------- | --- | --- | --------- | --- | --- |
|           |         |             |                    |         |          |             |         | erusaem-F |     |     | noisicerP |     |     |
|           | Twitter | ECG inc/alg | Exathlon Uni-sub-g | inc/alg | Exathlon | Uni-sub-g   | inc/alg | 0.3       |     |     |           |     |     |
| TranAD    | 0.455   | 0.224       | 0.245 0.299        |         | 0.484    | 0.345       |         |           |     |     | 0.6       |     |     |
|           |         | 39.7%       |                    | 6.1%    |          |             | -68.9%  |           |     |     |           |     |     |
| TranAD∗   | 0.466   | 0.397       | 0.246 0.414        |         | 0.246    | 0.039       |         | 0.2       |     |     | 0.4       |     |     |
| USAD      | 0.274   | 0.286       | 0.246 0.330        |         | 0.245    | 0.365       |         |           |     |     |           |     |     |
USAD∗ 0.289 0.448 31.0% 0.246 0.452 6.1% 0.245 0.038 -44.8% 0.1 0.2
| Omni  | 0.138 | 0.318 36.4% | 0.245 0.267 | 14.3% | 0.409 | 0.240 | -53.5% |     |     |     |     |     |     |
| ----- | ----- | ----------- | ----------- | ----- | ----- | ----- | ------ | --- | --- | --- | --- | --- | --- |
| Omni∗ | 0.166 | 0.483       | 0.246 0.553 |       | 0.246 | 0.079 |        | 0.0 |     |     | 0.0 |     |     |
RCoder - 0.441 - - - - 0% 20% 40% 60% 80% 100% 0.0 0.2 0.4 0.6 0.8 1.0
| RCoder∗ |       | 43.0%       |             |       | -     |       | -      |     |                      | Threshold |        |                     | Recall |
| ------- | ----- | ----------- | ----------- | ----- | ----- | ----- | ------ | --- | -------------------- | --------- | ------ | ------------------- | ------ |
|         | -     | 0.631       | -           | -     | -     | -     |        |     | (a) F-measure on ECG |           |        | (b) PR Curve on ECG |        |
| GDN     | 0.449 | 0.274       | 0.238 0.267 |       | 0.851 | 0.239 |        |     |                      |           |        |                     |        |
| GDN∗    | 0.460 | 0.410 26.9% | 0.246 0.554 | 14.7% | 0.246 | 0.079 | -69.1% |     |                      |           |        |                     |        |
|         |       |             |             |       |       |       |        |     |                      | NP        | MERLIN | NormA               | IDK    |
| NETS    | 0.802 | 0.461       | 0.286 0.942 |       | 0.217 | 0.942 |        |     |                      |           |        |                     |        |
| NETS∗   | 0.852 | 0.666 25.3% |             | 42.8% |       |       | -28.5% |     |                      |           | 1.0    |                     |        |
|         |       |             | 0.754       | 1     | 0.080 | 1     |        | 0.8 |                      |           |        |                     |        |
| Stare   | 0.334 | 0.252 66.6% | 0.253 0.653 | 14.5% | 0.189 | 0.438 | -85.0% |     |                      |           |        |                     |        |
| Stare∗  | 0.334 | 0.589       | 0.312 0.725 |       | 0.018 | 0.090 |        |     |                      |           | 0.8    |                     |        |
SHESD 0.209 0.339 0.257 0.978 0.227 0.979 erusaem-F 0.6 noisicerP
| SHESD∗ |       | 82.8% |       | 43.8% |       |     | -29.0% |     |     |     | 0.6 |     |     |
| ------ | ----- | ----- | ----- | ----- | ----- | --- | ------ | --- | --- | --- | --- | --- | --- |
|        | 0.510 | 0.488 | 0.776 | 1     | 0.090 | 1   |        |     |     |     |     |     |     |
0.4
| inc/data | 23.1% | 58.3% | 18.5% 12.5% |     | -53.4% | -54.8% |     |     |     |     | 0.4 |     |     |
| -------- | ----- | ----- | ----------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
|          |       |       |             |     |        |        |     | 0.2 |     |     | 0.2 |     |     |
|          |       |       |             |     |        |        |     | 0.0 |     |     | 0.0 |     |     |
time[32].Therefore,theoverlapofpredictedanomaliesandac- 0% 20% 40% 60% 80% 100% 0.0 0.2 0.4 0.6 0.8 1.0
tualanomaliesshouldbeaddressed.Todealwithinterpretationsof Threshold Recall
|     |     |     |     |     |     |     |     |     | (c) F-measure on Uni-sub-g |     |     | (d) PR Curve on Uni-sub-g |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | ------------------------- | --- |
suchoverlapsandtheproblemoflabelimbalance,somemethods
[3,52,58]useapoint-adjustmethod[62]thatconvertsfalsenegat- Figure15:Varyingthresholdson(a-b)ECG(c-d)Uni-sub-g
ivestotruepositives.AsshowninFigure14,foreachpointinthe
anomalysegmentofthegroundtruth,ifitisdetectedasananom-
Table7:F-measurew/oPOTmethod
alybytheproposedalgorithm,allobservationsinthesubsequence
willbeconsideredtohavebeencorrectlydetectedasanomalies.
|     |     |     |     |     |     |     |     | DataSet | TranAD | TranAD-P USAD | USAD-P | Omni Omni-P | GDN GDN-P |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ------------- | ------ | ----------- | --------- |
Therefore,suchamethodignoreslatencyandreportsmuchhigher
|     |     |     |     |     |     |     |     | ECG | 0.248 | 0.350 0.286 | 0.338 | 0.224 0.345 | 0.271 0.353 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | ----- | ----------- | ----------- |
accuracythanitactuallyis.RCoderproposesadifferentwayto
|     |     |     |     |     |     |     |     | DLR | 0.152 | 0.007 0.154 | 0.070 | 0.065 0.070 | 0.060 0.069 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | ----- | ----------- | ----------- |
adjustpredictions[1].However,wefocusonanalyzingthemore TAO 0.181 0.181 0.180 0.181 0.181 0.181 0.012 0.181
widelyusedpoint-adjustmethodinthiswork. UNI 0.179 0.182 0.158 0.182 0.660 0.181 0.181 0.183
Settings.Weconductexperimentswithbothpoint(Twitter,ECG)
andsubsequencedatasets(Exathlon,Uni-sub-g).Theresultsofpoint
robustnessofeachalgorithmw.r.t.thresholdandtheimpactofthe
datasetsareevaluatedbythepointmetricandtheresultsofsub-
POT[51]methodforautomaticthresholdselection.
sequencedatasetsareevaluatedbybothpointandrangemetrics.
|     |     |     |     |     |     |     |     | Settings. | We  | unify the threshold | setting | for all | methods in the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------------- | ------- | ------- | -------------- |
Resultswiththepoint-adjustmethodaredenotedby∗.
followingway:letthethresholdbetheratioofpoints/sequences
Results.Table6showsthef-measureindifferentcases.‘inc/alg’
identifiedasanomalies.0%meansallarenormal,while100%means
givestheaveragepromotionafterapplyingpoint-adjustmethod
|     |     |     |     |     |     |     |     | allareanomalies.However, |     |     | NETS,Stare,andSHESDhavedifferent |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | -------------------------------- | --- | --- |
permethodand‘inc/data’showsthispromotionperdata.Point-
logicinidentifyinganomalies(morethanonefactorisconsidered),
adjustmethodcanhaveagreatimpactontheevaluationasfollows:
sowereportonlyothermethodsinthispart.Theoverallperform-
(1)Overall,thealgorithmwillhaveanaveragepromotionof27.0%
anceistheareaincludedbytherecallandprecisioncurves.Besides,
forpointdatasetsandahigherpromotionof31.2%forsubsequence
theresultsofusingPOTmethodarepresentedinTable7.
datasetsunderpointmetrics.(2)Forsubsequencedatasetswith
Results.Figure15(c,d)showtheresultsonUni-sub-g.Wenote
rangemetrics,thealgorithmshaveanaveragenegativepromotion
thatNP,despitehavingabetterbestF-measurethanNormA,drops
of−67.6%.(3)TranADandOmnihaveahigherf-measure(0.245)
sharplyasthethresholdapproaches20%.Incontrast,NormAshows
thanGDN(0.238)underthepointmetric,butGDNperformsfar
betterrobustnessasthecurveissmoother.Itisinterestingtonote
better(0.851)thanTranAD(0.484)andOmni(0.409)onExathlon
underrangemetric.(4)Starehasahigherf-measure(0.334)than thatIDKperformsbestinthisexperiment,butdoesnotoutperform
SHESD(0.209),butaftertheadjustment,SHESDwillperformbetter inFigure9.Thereasonforthisisthatinallotherexperiments
weperformagridsearchonthevalidationsettofindtheproper
(0.510)thanStare(0.334)onTwitter.Suchinversionscanconfusean-
|     |     |     |     |     |     |     |     | (hyper)-parameters, |     | but there | is a small | difference | between the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --------- | ---------- | ---------- | ----------- |
omalydetectionsystemsandinfluenceuserpreferencesinselecting
validationsetandthetestset.Asforthepointmethodsshownin
appropriatemethods..
Figures15(a,b),RCodershowstheoverallbestperformanceamong
Summary.(1)point-adjustmethodtendstoreport‘false’higher
allthedeeplearningmethods,whileOmnishowsbetterrobustness.
resultsforalgorithmsandcanleadtomisleadinganalyzes.(2)The
IntermsoftheimpactofPOTmethod,GDNalwayshaveabetter
useofrangemetricsondatasetswithsubsequenceanomaliesis
resultafterusingit.Othermethodsshowdifferentpreferenceson
preferableasitleadstomorereasonableandrobustresults.
differentdatasets.Inaround55%cases,POTcanachievesimilaror
4.3.5 EffectofThreshold. Thresholdisakeyhyper-parameterfor slightlybetterresultsthangridsearchonvalidationset.
anomaly detection problems whose effect has seldom been dis- Summary.(1)Automaticthresholdselectionmethodscanstillbe
cussedinexistingworks,asstatedinSection1.2.Wewilltestthe improvedtotakeeffectinpracticaluses.(2)IDKhasthebestoverall
493

|     |     | FPR | FNR |     |     | FPR | FNR |     | Input :  |     |     |     | N   |     | NETS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | ---- |
TimeSeries x
| 1.00 |     |     |     | 1.00 |     |     |     |     |     |     |     |     |     | Y   |     |
| ---- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
RCoder
| 0.75  |     |     |     | 0.75  |     |     |     |              |                     |       |                |                 | P o     | s i t iv e      |            |
| ----- | --- | --- | --- | ----- | --- | --- | --- | ------------ | ------------------- | ----- | -------------- | --------------- | ------- | --------------- | ---------- |
|       |     |     |     |       |     |     |     | Anomaly type |                     | Point | High Dimension |                 | Y  ap p | l i c a t ion N | Omni       |
| eulaV |     |     |     | eulaV |     |     |     |              |                     |       |                |                 |         |                 |            |
| 0.50  |     |     |     | 0.50  |     |     |     | Subsequence  |                     |       |                |                 |         | Y               | NP         |
| 0.25  |     |     |     | 0.25  |     |     |     |              |                     |       |                | N               | E       | a rl y N        | M E R L IN |
|       |     |     |     |       |     |     |     | K n          | o w l e d g e   of  |       |                |                 | De te   | c t io n        |            |
|       |     |     |     |       |     |     |     |              | a n o m a l y       | Y     | P              | o s i t iv e    |         | Y               | P B A D    |
| 0.00  |     |     |     | 0.00  |     |     |     |              |                     |       |  ap            | p l i c a t ion |         |                 |            |
NETS Stare TranAD RCoder USAD GDN Omni PBAD LRRD B SAND NPMER G N IDK d i s t r i b u t i o n Y
|     |     |     |     |     | S eatGAN |     | LI r N ammar o rmA |     |     |      |                |     |               |             | SAND |
| --- | --- | --- | --- | --- | -------- | --- | ------------------ | --- | --- | ---- | -------------- | --- | ------------- | ----------- | ---- |
|     |     |     |     |     |          |     | V iz               |     | N   | S ta | ti o n a r y   | Y   | K n o w l e d | g e   o f   |      |
(a) Point Methods (b) Subsequence Methods t im e   se r i e s a n o m a l y  l e n g t h N IDK
|     |     |     |     |     |     |     |     |     |     |     |     | N   |     |     | NormA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Figure16:FPRandFNRonrealdatasets
|     |     |     |     |     |     |     |     | Figure | 18: A | practical | guide | for | timeseries | anomaly | detec- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --------- | ----- | --- | ---------- | ------- | ------ |
tion
20%
| 1.00           | Flat  |     |     | erusaem-F fo niaG |               | 10.99% |               |     |     |     |     |     |     |     |     |
| -------------- | ----- | --- | --- | ----------------- | ------------- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                | Front |     |     |                   | 4.75%         | 1.87%  |               |     |     |     |     |     |     |     |     |
| erusaem-F 0.75 |       |     |     | 0%                |               |        |               |     |     |     |     |     |     |     |     |
|                |       |     |     |                   | -7.30% -7.59% |        | -4.50% -1.72% |     |     |     |     |     |     |     |     |
-13.96%
| 0.50 |     |     |     | -20% |     |     |     |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.25
-40%
0.00
PBAD LRRD B eatGAN SAND NPMERG N IDK PBAD LRRD B eatGAN -48.76% SAND NPMERG N IDK WeseesimilarresultsinFigure17(b),wheretheaveragecompar-
|     |     | S   | Lr I a Nmmar o rmA |     | S   | Lr IN | ammar o rmA |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------------ | --- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
V iz V iz isonistestedoverallrealdatasets.BeatGANscoresa49%drop
|     | (a) F-measure on power |     |     | (b) Front compared to Flat on all real datasets |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------------- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
comparedtoitsperformanceundertheFlatmetric,showingthatit
capturesoutlierswithlatency.NPappearstobethebestperforming
Figure17:EarlydetectionunderFrontmetric
algorithmforearlydetection,withaperformanceimprovementof
10.99%.
performance,whileNormAismorerobust,specificallywhenthe Summary.(1)Specificmetricsarerequiredfordifferentscenarios.
thresholdisabove20%.(3)RCoderhasthebestoverallperformance, (2)Allsubsequencemethodsarebettersuitedfornegativeapplica-
whileOmniismorerobust.
tionsandPBADcanbeselectedforpositivecases.(3)NPisrecom-
4.3.6 Application. Inthissection,wefocusonanomalydetection mendedforearlydetection.(4)Omniisrecommendedfornegative
applications,whileRCoderisbetterforpositiveones.
inreal-worldapplications.Scenario1:Someapplicationsaremore
interestedinpositiveoutcomes,suchascancerdetection,where
wedonotwantcancerpatientstogoundetected.Othersaremore 5 DISCUSSIONS
interestedinnegativeoutcomes,suchaswhenwedonotwanta
Inthispaper,ataxonomyofanomalydetectionmethodsispresen-
goodemailtobecomespam.Scenario2:Inthepreviousstudy,we
tedandsystematicexperimentalintra-andinter-classcomparisons
assumedthatallpositionsofanoutlierrangeareequallyimportant.
areproposed.DetailedfindingsareshownintheSummarypartof
Therefore,largeroverlapsleadtoahigherscoreofthemetric.How-
Section4.Wefirstsummarizethesefindingsintoapracticalguide
ever,inpractice,therearemanysituationswhereearlyresponseis
andfinallyhighlightsomeresearchopportunitiesbelow.
critical,e.g.,cancerdetectionorreal-timesystems.
APracticalGuide.Apracticalguidefortimeseriesanomalyde-
Settings.Weemployexperimentsonallrealdatasetswithpoint
|                                            |     |     |     |     |     |     | 𝐹 𝑃   | tectionispresentedinFigure18basedontheexperimentalfindings |     |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ----- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| andsubsequencemethodsforScenario1,where𝐹𝑃𝑅 |     |     |     |     |     |     | = 𝐹𝑃, |                                                            |     |     |     |     |     |     |     |
|                                            |     |     |     |     |     |     | 𝑇𝑁 +  | onvariousaspectsliketypeofanomaly,dimensionality,typeof    |     |     |     |     |     |     |     |
𝐹𝑁𝑅= 𝐹 𝑁
𝑇𝑃 + 𝐹𝑁.Scenario2isparticularlysuitableforsubsequence applicationetc.Suchaguideisformedaccordingtocurrentwork
methods.Flatdenotesthemetricwiththesamescoreforallposi- andfutureworkisstillencouraged.
tions,whileFrontassignsmoreweighttotheearlypositionsofthe Explainability.Theexplainabilityofanomalydetectionmethods
subsequenceanomaly[53].
hasraisedmanyconcernsinrecentyears[37].Adecisionmaker
Results.Allalgorithmsgenerallyhaveahigherfalsenegativerate
maybemoreinterestedinthecauseoftheoccurrenceofoutliersso
andalowerfalsepositiverate,ascanbeseeninFigure16.This thattheycantakeappropriateaction,especiallyintheareaofIoT
suggeststhattheyaremoresuitablefornegativeapplications(not data[27].Developingamethodthatprovidesbothhighaccuracy
reportingfalseanomalies)andaremorecapableofdetectingnormal andreasonableexplainabilitymaybeofinterestforfuturework.
samplesthanabnormalsamples.Inparticular,NETSandOmnihave
lowFPRandarerecommendedfornegativecasessuchasspamde-
ACKNOWLEDGMENTS
tection.Ontheotherhand,TranADandRCoderarerecommended
forpositiveapplicationssincetheymanagetoreportallanomalies. AoqianZhangissupportedbytheNSFC(GrantNos.6210070801,
Similarly,PBADismoresuitablethanBeatGANforsuchcasesdue U21B2007).GuorenWangissupportedbytheNSFC(GrantNos.
toitslowerFNR. 61732003,U2001211).YeYuanissupportedbytheNationalKeyR&D
Figure17(a)showstheperformanceofthealgorithmsunderFlat ProgramofChina(GrantNo.2022YFB2702100),theNSFC(Grant
andFrontmetricsonPower.(Similarresultsareobservedonother Nos.61932004,62225203,U21A20516)andtheDITDP(GrantNo.
real-worlddatasets.)BeatGANhasahigherf-measurethanPBAD JCKY2021211B017).Wealsothankallthemembersofourcom-
undertheFlatmetric,butachievesalowerscorewhentheFront munitywhoopensourcedtheirdataandcodes,whichhelpusalot
| metricisused,indicatingthatitisnotsuitableforearlydetection. |     |     |     |     |     |     |     | onthiswork. |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
494

REFERENCES
[30] EamonnJ.Keogh,JessicaLin,Sang-HeeLee,andHelgaVanHerle.2007.Finding
[1] AhmedAbdulaal,ZhuanghuaLiu,andTomerLancewicki.2021.PracticalAp- themostunusualtimeseriessubsequence:algorithmsandapplications.Knowl.
proachtoAsynchronousMultivariateTimeSeriesAnomalyDetectionandLoc- Inf.Syst.11,1(2007),1–27. https://doi.org/10.1007/s10115-006-0034-6
alization.InKDD.ACM,2485–2494. [31] Kwei-HerngLai,DaochenZha,JunjieXu,YueZhao,GuanchuWang,andXia
[2] CharuC.Aggarwal.2013.OutlierAnalysis.Springer. Hu.2021.RevisitingTimeSeriesOutlierDetection:DefinitionsandBenchmarks.
[3] JulienAudibert,PietroMichiardi,FrédéricGuyard,SébastienMarti,andMariaA. InThirty-fifthConferenceonNeuralInformationProcessingSystemsDatasetsand
Zuluaga.2020.USAD:UnSupervisedAnomalyDetectiononMultivariateTime BenchmarksTrack(Round1). https://openreview.net/forum?id=r8IvOsnHchr
Series.InKDD.ACM,3395–3404. [32] NikolayLaptev,SaeedAmizadeh,andIanFlint.2015. GenericandScalable
[4] VicBarnett,TobyLewis,etal.1994.Outliersinstatisticaldata.Vol.3.WileyNew FrameworkforAutomatedTime-seriesAnomalyDetection.InKDD.ACM,1939–
York. 1947.
[5] AneBlázquez-García,AngelConde,UsueMori,andJoséAntonioLozano.2021. [33] N.JesperLarssonandAlistairMoffat.1999.OfflineDictionary-BasedCompres-
AReviewonOutlier/AnomalyDetectioninTimeSeriesData. ACMComput. sion.InDataCompressionConference,DCC1999,Snowbird,Utah,USA,March
Surv.54,3(2021),56:1–56:33. 29-31,1999.IEEEComputerSociety,296–305.
[6] PaulBoniol,MicheleLinardi,FedericoRoncallo,ThemisPalpanas,Mohammed [34] AlexanderLavinandSubutaiAhmad.2015. EvaluatingReal-TimeAnomaly
Meftah,andEmmanuelRemy.2021. Unsupervisedandscalablesubsequence DetectionAlgorithms-TheNumentaAnomalyBenchmark.InICMLA.IEEE,
anomalydetectioninlargedataseries.VLDBJ.30,6(2021),909–931. 38–44.
[7] PaulBoniol,JohnPaparrizos,ThemisPalpanas,andMichaelJ.Franklin.2021. [35] Kim-HungLeandPaoloPapotti.2020. User-drivenErrorDetectionforTime
SAND:StreamingSubsequenceAnomalyDetection.Proc.VLDBEndow.14,10 SerieswithEvents.InICDE.IEEE,745–757.
(2021),1717–1729. [36] DanLi,DachengChen,BaihongJin,LeiShi,JonathanGoh,andSee-KiongNg.
[8] MohammadBraeiandSebastianWagner.2020.AnomalyDetectioninUnivariate 2019.MAD-GAN:MultivariateAnomalyDetectionforTimeSeriesDatawith
Time-series:ASurveyontheState-of-the-Art.CoRRabs/2004.00433(2020). GenerativeAdversarialNetworks.InICANN(4)(LectureNotesinComputer
[9] BernardoBranco,PedroAbreu,AnaSofiaGomes,MarianaS.C.Almeida,JoãoTi- Science),Vol.11730.Springer,703–716.
agoAscensão,andPedroBizarro.2020.InterleavedSequenceRNNsforFraud [37] ZhongLi,YuxuanZhu,andMatthijsvanLeeuwen.2022.ASurveyonExplainable
Detection.InKDD.ACM,3101–3109. AnomalyDetection.CoRRabs/2210.06959(2022).
[10] MikelCanizo,IsaacTriguero,AngelConde,andEnriqueOnieva.2019.Multi- [38] FeiTonyLiu,KaiMingTing,andZhi-HuaZhou.2008.IsolationForest.InICDM.
headCNN-RNNformulti-timeseriesanomalydetection:Anindustrialcase IEEEComputerSociety,413–422.
study.Neurocomputing363(2019),246–260. [39] ShenghuaLiu,BinZhou,QuanDing,BryanHooi,ZhengboZhang,Huawei
[11] RaghavendraChalapathyandSanjayChawla.2019.DeepLearningforAnomaly Shen,andXueqiCheng.2022.Timeseriesanomalydetectionwithadversarial
Detection:ASurvey.CoRRabs/1901.03407(2019). reconstructionnetworks.IEEETransactionsonKnowledgeandDataEngineering
[12] DhruvChoudhary,ArunKejariwal,andFrancoisOrsini.2017.OntheRuntime- (2022).
EfficacyTrade-offofAnomalyDetectionTechniquesforReal-TimeStreaming [40] YueLu,RenjieWu,AbdullahMueen,MariaA.Zuluaga,andEamonnJ.Keogh.
Data.CoRRabs/1710.04735(2017). 2022.MatrixProfileXXIV:ScalingTimeSeriesAnomalyDetectiontoTrillions
[13] RobertBCleveland,WilliamSCleveland,JeanEMcRae,andIrmaTerpenning. ofDatapointsandUltra-fastArrivingDataStreams.InKDD’22:The28thACM
1990.STL:Aseasonal-trenddecomposition.J.Off.Stat6,1(1990),3–73. SIGKDDConferenceonKnowledgeDiscoveryandDataMining,Washington,DC,
[14] AndrewA.Cook,GokselMisirli,andZhongFan.2020.AnomalyDetectionfor USA,August14-18,2022,AidongZhangandHuzefaRangwala(Eds.).ACM,
IoTTime-SeriesData:ASurvey.IEEEInternetThingsJ.7,7(2020),6481–6494. 1173–1182.
[15] ZahraZamanzadehDarban,GeoffreyI.Webb,ShiruiPan,CharuC.Aggarwal, [41] AdityaP.MathurandNilsOleTippenhauer.2016. SWaT:awatertreatment
andMahsaSalehi.2022.DeepLearningforTimeSeriesAnomalyDetection:A testbedforresearchandtrainingonICSsecurity.In2016InternationalWorkshop
Survey.CoRRabs/2211.05244(2022). onCyber-physicalSystemsforSmartWaterNetworks,CySWater@CPSWeek2016,
[16] JanezDemsar.2006.StatisticalComparisonsofClassifiersoverMultipleData Vienna,Austria,April11,2016.IEEEComputerSociety,31–36. https://doi.org/
Sets.J.Mach.Learn.Res.7(2006),1–30. 10.1109/CySWater.2016.7469060
[17] AilinDengandBryanHooi.2021. GraphNeuralNetwork-BasedAnomaly [42] TakaakiNakamura,MakotoImamura,RyanMercer,andEamonnJ.Keogh.2020.
DetectioninMultivariateTimeSeries.InAAAI.AAAIPress,4027–4035. MERLIN:Parameter-FreeDiscoveryofArbitraryLengthAnomaliesinMassive
[18] EthanW.DereszynskiandThomasG.Dietterich.2011.SpatiotemporalModels TimeSeriesArchives.In20thIEEEInternationalConferenceonDataMining,
forData-AnomalyDetectioninDynamicEnvironmentalMonitoringCampaigns. ICDM2020,Sorrento,Italy,November17-20,2020.IEEE,1190–1195.
ACMTrans.Sens.Networks8,1(2011),3:1–3:36. [43] CraigG.Nevill-ManningandIanH.Witten.1997. IdentifyingHierarchical
[19] LenFeremans,VincentVercruyssen,BorisCule,WannesMeert,andBartGoeth- StructureinSequences:Alinear-timealgorithm. J.Artif.Intell.Res.7(1997),
als.2019. Pattern-BasedAnomalyDetectioninMixed-TypeTimeSeries.In 67–82.
ECML/PKDD(1)(LectureNotesinComputerScience),Vol.11906.Springer,240– [44] AntoniosNtroumpogiannis,MichailGiannoulis,NikolaosMyrtakis,Vassilis
256. Christophides,EricSimon,andIoannisTsamardinos.2023.Ameta-levelanalysis
[20] MiltonFriedman.1937.Theuseofrankstoavoidtheassumptionofnormality ofonlineanomalydetectors.VLDBJ.32,4(2023),845–886.
implicitintheanalysisofvariance.Journaloftheamericanstatisticalassociation [45] JohnPaparrizos,PaulBoniol,ThemisPalpanas,RueySTsay,AaronElmore,and
32,200(1937),675–701. MichaelJFranklin.2022.Volumeunderthesurface:anewaccuracyevaluation
[21] MarkusGoldsteinandSeiichiUchida.2016. Acomparativeevaluationofun- measurefortime-seriesanomalydetection.ProceedingsoftheVLDBEndowment
supervisedanomalydetectionalgorithmsformultivariatedata.PloSone11,4 15,11(2022),2774–2787.
(2016),e0152173. [46] JohnPaparrizosandLuisGravano.2015.k-Shape:EfficientandAccurateClus-
[22] ManishGupta,JingGao,CharuC.Aggarwal,andJiaweiHan.2014. Outlier teringofTimeSeries.InProceedingsofthe2015ACMSIGMODInternational
DetectionforTemporalData:ASurvey.IEEETrans.Knowl.DataEng.26,9(2014), ConferenceonManagementofData,Melbourne,Victoria,Australia,May31-June
2250–2267. 4,2015,TimosK.Sellis,SusanB.Davidson,andZacharyG.Ives(Eds.).ACM,
[23] D.M.Hawkins.1980.IdentificationofOutliers.Springer. 1855–1870.
[24] YuanduoHe,XuChu,andYashaWang.2020.NeighborProfile:BaggingNearest [47] JohnPaparrizos,YuhaoKang,PaulBoniol,RueyS.Tsay,ThemisPalpanas,andMi-
NeighborsforUnsupervisedTimeSeriesMining.InICDE.IEEE,373–384. chaelJ.Franklin.2022.TSB-UAD:AnEnd-to-EndBenchmarkSuiteforUnivariate
[25] JordanHochenbaum,OwenS.Vallis,andArunKejariwal.2017. Automatic Time-SeriesAnomalyDetection.Proc.VLDBEndow.15,8(2022),1697–1711.
AnomalyDetectionintheCloudViaStatisticalLearning.CoRRabs/1704.07706 [48] BernardRosner.1975.Onthedetectionofmanyoutliers.Technometrics17,2
(2017). (1975),221–227.
[26] MinHu,XiaoweiFeng,ZhiweiJi,KeYan,andShengchenZhou.2019.Anovel [49] SebastianSchmidl,PhillipWenig,andThorstenPapenbrock.2022. Anomaly
computationalapproachfordiscordsearchwithlocalrecurrenceratesinmul- DetectioninTimeSeries:AComprehensiveEvaluation.Proc.VLDBEndow.15,9
tivariatetimeseries.Inf.Sci.477(2019),220–233. (2022),1779–1797.
[27] RuihongHuang,ZhiweiChen,ZhichengLiu,ShaoxuSong,andJianminWang. [50] PavelSenin,JessicaLin,XingWang,TimOates,SunilGandhi,ArnoldP.Boedi-
2019. TsOutlier:ExplainingOutlierswithUniformProfilesoverIoTData.In hardjo,CrystalChen,andSusanFrankenstein.2018.GrammarViz3.0:Interactive
IEEEBigData.IEEE,2024–2027. DiscoveryofVariable-LengthTimeSeriesPatterns.ACMTrans.Knowl.Discov.
[28] KyleHundman,ValentinoConstantinou,ChristopherLaporte,IanColwell,and Data12,1(2018),10:1–10:28.
TomSöderström.2018.DetectingSpacecraftAnomaliesUsingLSTMsandNon- [51] AlbanSiffer,Pierre-AlainFouque,AlexandreTermier,andChristineLargouët.
parametricDynamicThresholding.InKDD.ACM,387–395. 2017.AnomalyDetectioninStreamswithExtremeValueTheory.InKDD.ACM,
[29] VincentJacob,FeiSong,ArnaudStiegler,BijanRad,YanleiDiao,andNesime 1067–1075.
Tatbul.2021.Exathlon:ABenchmarkforExplainableAnomalyDetectionover [52] YaSu,YoujianZhao,ChenhaoNiu,RongLiu,WeiSun,andDanPei.2019.Robust
TimeSeries.Proc.VLDBEndow.14,11(2021),2613–2626. AnomalyDetectionforMultivariateTimeSeriesthroughStochasticRecurrent
NeuralNetwork.InKDD.ACM,2828–2837.
495

[53] NesimeTatbul,TaeJunLee,StanZdonik,MejbahAlam,andJustinGottschlich. [62] HaowenXu,WenxiaoChen,NengwenZhao,ZeyanLi,JiahaoBu,ZhihanLi,Ying
2018.PrecisionandRecallforTimeSeries.InNeurIPS.1924–1934. Liu,YoujianZhao,DanPei,YangFeng,JieChen,ZhaogangWang,andHonglin
[54] MarkusThill,WolfgangKonen,andThomasBäck.2017.Onlineanomalydetec- Qiao.2018.UnsupervisedAnomalyDetectionviaVariationalAuto-Encoderfor
tiononthewebscopeS5dataset:Acomparativestudy.InEAIS.IEEE,1–8. SeasonalKPIsinWebApplications.InWWW.ACM,187–196.
[55] KaiMingTing,ZongyouLiu,HangZhang,andYeZhu.2022.ANewDistribu- [63] HuiYang,SatishT.S.Bukkapatnam,andLeandroG.Barajas.2011. Localre-
tionalTreatmentforTimeSeriesandAnAnomalyDetectionInvestigation.Proc. currencebasedperformancepredictionandprognosticsinthenonlinearand
VLDBEndow.15,11(2022),2321–2333. nonstationarysystems.PatternRecognit.44,8(2011),1834–1840.
[56] KaiMingTing,Bi-CunXu,TakashiWashio,andZhi-HuaZhou.2020.Isolation [64] DragomirYankov,EamonnJ.Keogh,andUmaaRebbapragada.2008.Diskaware
DistributionalKernel:ANewToolforKernelbasedAnomalyDetection.InKDD discorddiscovery:findingunusualtimeseriesinterabytesizeddatasets.Knowl.
’20:The26thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining, Inf.Syst.17,2(2008),241–262.
VirtualEvent,CA,USA,August23-27,2020,RajeshGupta,YanLiu,JiliangTang, [65] Chin-ChiaMichaelYeh,YanZhu,LiudmilaUlanova,NurjahanBegum,YifeiDing,
andB.AdityaPrakash(Eds.).ACM,198–206. HoangAnhDau,DiegoFurtadoSilva,AbdullahMueen,andEamonnJ.Keogh.
[57] LuanTran,LiyueFan,andCyrusShahabi.2016.Distance-basedOutlierDetection 2016. MatrixProfileI:AllPairsSimilarityJoinsforTimeSeries:AUnifying
inDataStreams.Proc.VLDBEndow.9,12(2016),1089–1100. ViewThatIncludesMotifs,DiscordsandShapelets.InIEEE16thInternational
[58] ShreshthTuli,GiulianoCasale,andNicholasR.Jennings.2022.TranAD:Deep ConferenceonDataMining,ICDM2016,December12-15,2016,Barcelona,Spain.
TransformerNetworksforAnomalyDetectioninMultivariateTimeSeriesData. IEEEComputerSociety,1317–1322.
Proc.VLDBEndow.15,6(2022),1201–1214. [66] SusikYoon,Jae-GilLee,andByungSukLee.2019.NETS:ExtremelyFastOutlier
[59] ChenWang,XiangdongHuang,JialinQiao,TianJiang,LeiRui,JinruiZhang, DetectionfromaDataStreamviaSet-BasedProcessing.Proc.VLDBEndow.12,
RongKang,JulianFeinauer,KevinMcgrail,PengWang,DiaohanLuo,JunYuan, 11(2019),1303–1315.
JianminWang,andJiaguangSun.2020.ApacheIoTDB:Time-seriesdatabasefor [67] SusikYoon,Jae-GilLee,andByungSukLee.2020.UltrafastLocalOutlierDe-
InternetofThings.Proc.VLDBEndow.13,12(2020),2901–2904. tectionfromaDataStreamwithStationaryRegionSkipping.InKDD.ACM,
[60] FrankWilcoxon.1992.Individualcomparisonsbyrankingmethods.InBreak- 1181–1191.
throughsinstatistics.Springer,196–202. [68] MohammedJ.ZakiandWagnerMeiraJr.2014. DataMiningandAnalysis:
[61] RenjieWuandEamonnKeogh.2021. Currenttimeseriesanomalydetection FundamentalConceptsandAlgorithms.CambridgeUniversityPress.
benchmarksareflawedandarecreatingtheillusionofprogress.IEEETransactions [69] YongZou,MarcoThiel,M.CarmenRomano,andJürgenKurths.2007. Ana-
onKnowledgeandDataEngineering(2021). lyticalDescriptionofRecurrencePlotsofDynamicalSystemswithNontrivial
Recurrences.Int.J.Bifurc.Chaos17,12(2007),4273–4283.
496