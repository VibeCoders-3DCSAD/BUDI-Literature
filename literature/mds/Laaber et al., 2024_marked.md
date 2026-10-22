---
source_file: "Laaber et al., 2024.pdf"
source_sha256: "8e55a1b96eb0297df4b19f47f10236127f12e489e5e782d4ee478215573f8a67"
page_count: 17
converted_at: "2026-10-21T10:59:57Z"
converter: "markitdown"
---

1
| Testing |     | Medical |     | Rules |     | Web |     | Services |     |     | in  | Practice |     |     |
| ------- | --- | ------- | --- | ----- | --- | --- | --- | -------- | --- | --- | --- | -------- | --- | --- |
Christoph Laaber, Shaukat Ali, Thomas Schwitalla, and Jan F. Nygård
Abstract—TheCancerRegistryofNorway(CRN)collectsandprocessescancer-relateddataforpatientsinNorway.Forthis,itemploys
asociotechnicalsoftwaresystemthatevolveswithchangingrequirementsandmedicalstandards.Thecurrentpracticeistomanuallytest
CRN’ssystemtopreventfaultsandensureitsdependability.ThispaperfocusesonautomaticallytestingGURI,theCRN’smedicalrule
engine,usingasystem-leveltestingtool,EvoMaster,inbothitsblack-boxandwhite-boxmodes,andanovelCRN-specific
EvoMaster-basedtool,EvoGURI.Weempiricallyevaluatethetools’effectivenessregardingcodecoverage,errorsfound,domain-specific
rulecoverage,andabilitytoidentifyartificialfaultstenversionsofGURI.Ourresultsshowthatallthetoolsachievesimilarcodecoverage
andidentifiedasimilarnumberoferrors.Forrulecoverage,EvoGURIandEvoMaster’sblack-boxmodeproducetestsuitesthatcoverthe
highestnumberofruleswithPass,Fail,andWarningresults.ThetestsuitesofEvoGURIandtwoEvoMaster white-boxtoolsidentifythe
4202 ceD 61  ]ES.sc[  1v13711.2142:viXra mostfaultsinamutationtestingexperiment.Basedonourfindings,werecommendusingEvoGURIinCRN’scurrentpractice.Finally,we
presentkeytakeawaysandoutlineopenresearchquestionsfortheresearchcommunity.
IndexTerms—automatedsoftwaretesting,testgeneration,RESTAPIs,cancerregistry,electronichealthrecords,ruleengine
✦
1 INTRODUCTION correct and reliable CaReSS is. To this end, testing is one
methodtoensurethedependabilityofCaReSS.
Cancerisaleadingcauseofdeathworldwide,withnearly10 This paper reports on a case study in the real-world
milliondeathsin2022[14].Consequently,mostcountriessys- context of the CRN, focusing on testing one of the key
|     |     |     |     |     |     |     | components | of  | CaReSS, | called | GURI | —   | a rule | engine |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | ------ | ---- | --- | ------ | ------ |
tematicallycollectdataaboutcancerpatientsinspecialized
registries to improve patient care by supporting decision- responsibleforcheckingmedicalrulesforvariouspurposes
makingandconductingresearch.Theseregistriesmaintain suchasdatavalidationandaggregation.Currently,GURIis
specializedsoftwaresystemstocollect,curate,andanalyze primarilytestedmanually,asalsoreportedbyHaasetal.[24]
cancer data. However, engineering such software systems thatmanualtestingisacommonpracticeinindustry.This
posesmanychallenges,suchas(1)collectingdataforpatients paperinvestigatestestgenerationtoolstoenableautomated
throughouttheirlivesfromdiversesources,e.g.,hospitals, testing to alleviate manual testing of GURI. For this, our
|     |     |     |     |     |     |     | study takes | a popular |     | open-source, |     | AI-based | system-level |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | ------------ | --- | -------- | ------------ | --- |
laboratories,andotherregistries;(2)dealingwithcontinuous
evolution,e.g.,duetosoftwareupdates,newrequirements, test generation tool called EvoMaster [6], which has been
updatedregulations,andnewmedicalresearch;and(3)in- shown to be superior to nine other representational state
|         |               |     |         |                     |     |     | transfer | (REST) | application | programming |     |     | interface | (API) |
| ------- | ------------- | --- | ------- | ------------------- | --- | --- | -------- | ------ | ----------- | ----------- | --- | --- | --------- | ----- |
| creased | incorporation | of  | machine | learning algorithms |     | to  |          |        |             |             |     |     |           |       |
decision support and production of statistics for relevant testing tools [29], addresses domain-specific challenges by
stakeholders,includingpatientsandpolicymakers. devising a novel CRN-specific EvoMaster extension called
|     |         |               |          |           |        |     | EvoGURI, | and | performs | automated |     | testing | of GURI | with |
| --- | ------- | ------------- | -------- | --------- | ------ | --- | -------- | --- | -------- | --------- | --- | ------- | ------- | ---- |
| Our | context | is the Cancer | Registry | of Norway | (CRN), |     |          |     |          |           |     |         |         |      |
whichhasdevelopedaCancerRegistrationSupportSystem thesetoassessthetestingeffectivenessofGURIfromvarious
| (CaReSS) | to support | collecting, | processing, | and | managing |     | perspectives. |          |            |     |       |          |         |      |
| -------- | ---------- | ----------- | ----------- | --- | -------- | --- | ------------- | -------- | ---------- | --- | ----- | -------- | ------- | ---- |
|          |            |             |             |     |          |     | In our        | previous | conference |     | paper | [31], we | applied | Evo- |
cancer-relateddatafromvariousmedicalentitiessuchasNor-
wegianhospitalsandlaboratories.Basedontheprocessing, Master’sfouroff-the-shelftools,i.e.,black-boxandwhite-box
theCRNgeneratesstatisticsthatareconsumedbyexternal toolswiththreeevolutionaryalgorithms(EAs),totestGURI’s
10versions,relyingonGURI’sdefaultOpenAPISpecification
entities,includingpolicymakers,hospitals,andpatients.It
|                  |     |          |             |            |           |     | (OAS). | We assessed | EvoMaster’s |     | effectiveness |     | with | three |
| ---------------- | --- | -------- | ----------- | ---------- | --------- | --- | ------ | ----------- | ----------- | --- | ------------- | --- | ---- | ----- |
| further provides |     | data for | researchers | to conduct | research. |     |        |             |             |     |               |     |      |       |
Naturally,thequalityofstatisticsanddatadependsonhow metrics: source code coverage, errors found, and domain-
specificrulecoverage.WefoundthatEvoMasterstrugglesto
|     |     |     |     |     |     |     | cover specific | rules, | limiting | its | applicability |     | for | the CRN. |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------ | -------- | --- | ------------- | --- | --- | -------- |
• C.LaaberiswiththeSimulaResearchLaboratory,Oslo,Norway Toaddressthislimitation,thispaperextendstheprevious
E-mail:laaber@simula.no paperby(1)extendingEvoMasterwithdomain-specificrule
•
S.AliiswiththeSimulaResearchLaboratoryandtheOsloMetropolitan objectivesandtargetsintotheEvoGURItool;(2)assessingthe
University,Oslo,Norway
E-mail:shaukat@simula.no toolswithtwoOAStypes,i.e.,thedefaultandstrictversion
• T.SchwitallaiswiththeCancerRegistryofNorway,NorwegianInstitute withaddedvariableconstraints;and(3)strengtheningthe
ofPublicHealth,Oslo,Norway empiricalevaluationthroughamutationtestingexperiment
E-mail:thsc@kreftregisteret.no
• J.F.NygårdiswiththeCancerRegistryofNorway,NorwegianInstitute comprising 2,279 rule mutations from 8 rule mutation
| ofPublicHealth,Oslo,NorwayandUiTTheArcticUniversityofNorway, |     |     |     |     |     |     | operators. |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Tromsø,Norway The results of our experiments show that all five tools’
E-mail:jfn@kreftregisteret.no effectivenessissimilarintermsofcodecoverageanderrors

2
foundacrossallGURIversions.However,weobservethat The aggregation rule below determines the state of
EvoGURIandEvoMaster’sblack-boxtoolgeneratetestsuites Morphologicallyverified,basedonagivenBasisvalueofcancer
| thatexecutemorerulesleadingtoPass,Fail,andWarning |     |     |     |     |     |     |     | messages: |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
results. During the test generation phase, the EvoMaster ifBasis∈[’22’,’32’,’33’,’34’,’35’,’36’,’37’,’38’,’39’,’57’,’60’,
white-boxtoolwiththeManyIndependentObjective(MIO) ’70’,’72’,’74’,’75’,’76’,’79’]then
Morphologicallyverified=’Yes’
algorithmexecutesruleswithPass,Fail,andWarningresults
elseifBasis∈[’00’,’10’,’20’,’23’,’29’,’30’,’31’,’40’,’45’,’46’,
withthehighestfrequencycomparedtoallexecutedrules,
’47’,’90’,’98’]then
| followed | by EvoGURI |     | and | the other | EvoMaster |     | white-box |     |     |     |     |     |     |     |
| -------- | ---------- | --- | --- | --------- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Morphologicallyverified=’No’
tools.Wefurthercomparetheruleexecutionsobservedby
else
GURI inproduction,andtheresultsshowthatnotoolcan Morphologicallyverified=null
| Pass rules | as often | as  | observed | in  | production, | but | they all | endif |     |     |     |     |     |     |
| ---------- | -------- | --- | -------- | --- | ----------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- |
aregoodattriggeringFailandWarningresults,whichare
|     |     |     |     |     |     |     |     | Both | rule types | can | yield | four result | types for | a given |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | --- | ----- | ----------- | --------- | ------- |
theexceptionalandcornercasesonewouldpredominantly
like to test. In terms of mutation testing, EvoGURI and cancermessageorcase:Passresultsfromasuccessfulrule
the EvoMaster white-box tools with the Many-Objective execution,i.e.,thecancermessagewithallitsdataisvalid,or
thecancercasewassuccessfullyaggregatedwithaprevious
| Sorting    | Algorithm | (MOSA)   |     | and    | Whole | Test Suite | (WTS) |             |     |          |     |                  |      |         |
| ---------- | --------- | -------- | --- | ------ | ----- | ---------- | ----- | ----------- | --- | -------- | --- | ---------------- | ---- | ------- |
|            |           |          |     |        |       |            |       | cancer case | and | a number | of  | cancer messages; | Fail | results |
| algorithms | achieve   | mutation |     | scores | (MSs) | between    | 0.96  |             |     |          |     |                  |      |         |
and 1, showing that the generated test suites are highly fromanunsuccessfulruleexecution,i.e.,thecancermessage
isinvalid,orthecancercasefailstobeaggregated;Warningis
effectiveinidentifyingartificialseededfaults.Ourresultsdo
|             |      |      |           |       |            |       |        | the result | where | the rule | execution | is successful; | however, |     |
| ----------- | ---- | ---- | --------- | ----- | ---------- | ----- | ------ | ---------- | ----- | -------- | --------- | -------------- | -------- | --- |
| not suggest | that | rule | evolution | plays | a critical | role, | as the |            |       |          |           |                |          |     |
tools’effectivenessremainsstableacrossthe10ruleversions. the data appears to be dubious (e.g., a patient’s age is 120
Finally,wenoticethatrelyingonastrictOASwithprecise years,whichistheoreticallyvalidbuthighlyunlikely);and
|     |     |     |     |     |     |     |     | Not Applied | is  | a rule | that is | partially executed | against | an  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | ------- | ------------------ | ------- | --- |
variableconstraintsimprovesthetools’effectivenessacross
allthetoolsandstudiedmetrics. input, which only applies to validation rules of the form
Basedonourresults,werecommendusingEvoGURIas apply =⇒ rule, where apply is the condition on which
ruleisapplied(intheexampleabove:acancermessagewith
| the automated |     | testing | solution | for | GURI | and CaReSS. | In  |     |     |     |     |     |     |     |
| ------------- | --- | ------- | -------- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
messageType!=H,therulewouldresultinNotApplied).
particular,thispapercomparedtoourpreviousconference
paper[31]showsthatourdomain-awareEvoGURIcombined GURIisacomponentofCaReSSthatstorestherulesin
|        |            |       |     |        |          |                |     | a database, | exposes | a        | REST | API (internally | at the     | CRN), |
| ------ | ---------- | ----- | --- | ------ | -------- | -------------- | --- | ----------- | ------- | -------- | ---- | --------------- | ---------- | ----- |
| with a | strict OAS | leads | to  | vastly | improved | effectiveness, |     |             |         |          |      |                 |            |       |
|        |            |       |     |        |          |                |     | receives    | cancer  | messages | and  | cases for       | validation | and   |
covering0.50percentagepoints(pp)morePassand0.60pp
more Fail results. Finally, we provide detailed discussions aggregation,andreturnstheresult.Uponreceivingacancer
messageorcase,GURIappliesallrulesandreturnstheresult
| and lessons | from | our | industrial | case | study | regarding | its |     |     |     |     |     |     |     |
| ----------- | ---- | --- | ---------- | ---- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
foreachrule.Newrulesandupdatestotherulesaredone
generalizationtoothercontextsandpointoutkeyresearch
areasthatdeserveattentionfromthesoftwareengineering throughagraphicaluserinterface(GUI),whichisavailable
| community.    |     |         |     |     |     |     |     | tomedicalpersonnel. |     |     |       |     |     |     |
| ------------- | --- | ------- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ----- | --- | --- | --- |
| 2 APPLICATION |     | CONTEXT |     |     |     |     |     | 3 EXPERIMENTAL      |     |     | STUDY |     |     |     |
Weperformlaboratoryexperiments[45]ofautomatedtest
| The CRN | regularly | collects |     | cancer | patients’ | data | (e.g., di- |     |     |     |     |     |     |     |
| ------- | --------- | -------- | --- | ------ | --------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
generationtechniquesforRESTAPIsattheCRNtounder-
| agnostic, | treatment), |     | based | on which | cancer | research | and |     |     |     |     |     |     |     |
| --------- | ----------- | --- | ----- | -------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
statistics can be conducted. To ensure the quality of the standtheireffectivenessofcoveringsourcecode;revealing
collected data, the CRN’s CaReSS has introduced several errors;executingdomain-specificelements,i.e.,medicalrules;
|            |         |     |          |     |       |            |     | and achieving | high | rule | mutation | scores. | Our experiment |     |
| ---------- | ------- | --- | -------- | --- | ----- | ---------- | --- | ------------- | ---- | ---- | -------- | ------- | -------------- | --- |
| preventive | efforts | to  | discover | and | amend | inaccurate | or  |               |      |      |          |         |                |     |
missing data. Patient data is submitted to the CRN as comprises a real-world study subject, i.e., CRN’s medical
cancermessages,whichcontainthepatientdataas51medical ruleengineGURI,andfiveRESTAPItestgenerationtools.
variables.Cancermessagesarecodedbymedicalpersonell
in a stringent process and aggregated into cancer cases. 3.1 ResearchQuestions
Cancermessagesandcasesrepresentatimelineofapatient’s
Ourstudyinvestigatesthefollowingfiveresearchquestions
diagnoses,treatments,andfollow-ups.Thecodingprocess (RQs)toassesstheeffectivenessofthetestgenerationtools:
| relies on | standard | classification |     | systems |     | and depends | on  |     |     |     |     |     |     |     |
| --------- | -------- | -------------- | --- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
hundredsofmedicalrulesforvalidatingcancermessagesand RQ1(codecoverage) How much code coverage do the
toolsachieve?
| aggregating | cancer | cases. | Consequently, |     |     | these rules | are of |     |     |     |     |     |     |     |
| ----------- | ------ | ------ | ------------- | --- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
two types: validation rules and aggregation rules, which are RQ2(codeerrors) Howmanycode-relatederrorsdothe
defined by medical experts and implemented in GURI for toolstrigger?
| automated | validation |     | and aggregation |     | of  | cancer | messages |                              |     |     |     |     |            |     |
| --------- | ---------- | --- | --------------- | --- | --- | ------ | -------- | ---------------------------- | --- | --- | --- | --- | ---------- | --- |
|           |            |     |                 |     |     |        |          | RQ3(executedrulesandresults) |     |     |     | How | many rules | can |
andcases.Theserulesconstantlyevolve,e.g.,duetoupdated thetoolsexecuteandwhichresultsdotheyyield?
medicalknowledgeandprocedures.
|       |                 |     |       |       |        |      |             | RQ4(ruleandresultfrequency) |     |     |     | How | often do | the exe- |
| ----- | --------------- | --- | ----- | ----- | ------ | ---- | ----------- | --------------------------- | --- | --- | --- | --- | -------- | -------- |
| Below | is a validation |     | rule, | which | states | that | for all the |                             |     |     |     |     |          |          |
cutedrulesyieldeachresulttypeduringtestgeneration,
cancermessagesoftypeH,ifthesurgeryvalueisequalto96, andhowdoesitcomparetoproductionGURI?
thenthebasisvaluemustbegreaterthan32.
|     |     |     |     |     |     |     |     | RQ5(mutationtesting) |     |     | Howeffectivearethegenerated |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --------------------------- | --- | --- | --- |
∀messageType=H =⇒ (surgery =96 =⇒ basis>32) testsinfindingruleerrors?

3
Table1 tools [6]. EvoMaster was recently shown to be the most
RuleEvolution effectivetool,intermsofsourcecodecoverageandtriggered
errors,amongtendifferenttools[29].
Version Date Rules Intermsoftestingapproach,ourexperimentsuseboth
Validation Aggregation black-box and white-box testing. EvoMaster-BB relies on
v1 12.12.2017 30 32 randomtesting,RESTrequestsamplingbasedonanOAS,
v2 30.05.2018 31 33 and an archive to store the generated tests that cover new
v3 06.02.2019 48 35 targets [7]. The targets are the different HTTP endpoints
v4
|     |     | 27.08.2019 |     |     | 49  | 35  |     |     |     |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
v5 11.11.2019 53 37 and their status codes, e.g., successful (4xx status code)
v6 25.09.2020 56 37 andfaulty(5xxstatuscode)request-responsepairs.Onthe
v7 24.11.2020 66 38 other hand, EvoMaster-WB uses an EA to generate tests
v8 20.04.2021 69 43 relying on random sampling of REST requests, coverage
v9
|     |     | 13.01.2022 |     |     | 69  | 43  |     |     |     |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
v10 21.01.2022 70 43 feedback, and mutation [6, 38, 52]. The EA relies on the
|     |     |     |     |     |     |     |     | same targets | as EvoMaster-BB |     | as search | objectives |     | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------------- | --- | --------- | ---------- | --- | --- |
additionallyincorporatescodecoveragecriteriasuchasline,
RQ1 and RQ2 are “traditionally” investigated research branch,andmethodcoverage.EvoMaster-WBsupportsthree
questions for evaluating test generation tools in terms of EAs: (1) MIO [5], which is a many-objective evolutionary
effectiveness,includingRESTAPItestgeneration[29].RQ3 algorithm(MaOEA)focusingonscalabilityinthepresenceof
andRQ4aredomain-specificRQsthatevaluatethetestgener- manytestingtargets,thatwasspecificallydesignedforREST
ationtools’effectivenessintestingGURI’smainfunctionality, APItestgenerationandisEvoMaster’sdefault;(2)MOSA[42],
i.e.,validatingandaggregatingcancermessagesandcancer which is the first MaOEA that was designed for unit test
generationwithEvoSuite[19];and(3)WTS[20],whichisa
| cases. RQ3 | studies |     | the test | generation |     | tools’ capability | to  |     |     |     |     |     |     |     |
| ---------- | ------- | --- | -------- | ---------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
executethemedicalrulesandyieldallpossibleresulttypes single objective genetic algorithm (GA) that was designed
perrule,withtheultimategoaloftestingallrule-resultpairs. forunittestgenerationandistheoriginalEAofEvoSuite.
ThegoalofRQ4istoinvestigatethefrequencyofeachrule’s In addition, influenced by our previous paper’s find-
result types during test generation and how these results ings[31],weextendEvoMaster-BBtoincludeCRN-context-
compare to the results from the production system. RQ5 specific targets (see Section 2). We call this extension
appliesthetraditionalconceptofmutationtestingtomedical EvoGURI,whichleveragesthereturnedresulttypesforeach
rules(insteadofsourcecode)toevaluatethegeneratedtest ruleasacoveredtarget,inadditiontoEvoMaster-BB’sREST
suites’abilityinfinding(artificial)rulefaults. endpoint and status code targets. For each test case (i.e.,
HTTPrequest),EvoGURIparsestheresponsebodyintorule
3.2 StudySubject—GURI andresultpairs,e.g.,V01(validationrulenumber1)hadthe
resultPass.Notethatalltherulesareexecutedagainstthe
GURIisimplementedasaJavawebapplicationwithSpring
cancermessageorcaseofeachtestcase.Eachtestcasecovers
Boot,whichexposesRESTAPIendpointstoCRN’sinternal
n
systems and provides a web interface for medical coders. targets, one for each rule, for a specific REST endpoint
Although GURI has 32 REST endpoints, we only focus and status code. EvoGURI saves a test case in an external
|         |      |             |     |       |     |          |          | archive, | if it covers new | targets, | i.e., | it executes | a rule | that |
| ------- | ---- | ----------- | --- | ----- | --- | -------- | -------- | -------- | ---------------- | -------- | ----- | ----------- | ------ | ---- |
| on 2 in | this | experiment, | as  | these | are | the ones | handling |          |                  |          |       |             |        |      |
yieldsanewresult.Throughthis,EvoGURIkeepstestcases
| the rules, | i.e., | one | for validating |     | cancer | messages | with |     |     |     |     |     |     |     |
| ---------- | ----- | --- | -------------- | --- | ------ | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
validation rules and one for aggregating cancer messages withuncoveredrule-result-pairswiththegoalofgenerating
acomprehensivetestsuitethatimprovesrulefaultdiscovery
intocancercaseswithaggregationrules.GURI’smostrecent
comparedtothestandardEvoMastertestsuites.
| version | consists | of  | 70 validation | rules | and | 43 aggregation |     |     |     |     |     |     |     |     |
| ------- | -------- | --- | ------------- | ----- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
rules. Since GURI was introduced, its source code has Our experiment investigates all four EvoMaster tool
parameterizationsandEvoGURI,whichwesimplycall“tool”
| hardly | changed; | however, |     | its rules | have | been subject | to  |     |     |     |     |     |     |     |
| ------ | -------- | -------- | --- | --------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
intheremainderofthepaper:(1)EvoMaster-BB:EvoMaster
evolutionduetoupdatedmedicalknowledge,suchasrule
additions,deletions,andmodifications.Consequently,based black-box; (2) EvoMaster-WB-MIO: EvoMaster white-box
withMIO;(3)EvoMaster-WB-MOSA:EvoMasterwhite-box
| on these | changes, | we  | form | 10 rule | sets | as 10 versions | in  |            |                       |     |     |           |     |        |
| -------- | -------- | --- | ---- | ------- | ---- | -------------- | --- | ---------- | --------------------- | --- | --- | --------- | --- | ------ |
|          |          |     |      |         |      |                |     | with MOSA; | (4) EvoMaster-WB-WTS: |     |     | EvoMaster |     | white- |
thisexperiment.Specifically,outof28uniquepointsintime
when the rules were changed in GURI, we select 10 dates box with WTS; and (5) EvoGURI: EvoMaster-BB with rule-
wherethechangesaremostsevere(themostruleadditions resulttargets.BeyondthetestingapproachandtheEA,our
experimentusesthedefaultparametersofEvoMaster,similar
anddeletionsoccurred).Table1depictsthisruleevolution.
toKimetal.[29].
3.3 TestGenerationTools
The automated REST API test generation tools form the 3.4 OASTypes
independentvariableofourexperimentalstudy.Weselect
|            |              |              |      |          |         |           |          | In our previous | paper   | [31],    | we relied | on the        | OAS | that is |
| ---------- | ------------ | ------------ | ---- | -------- | ------- | --------- | -------- | --------------- | ------- | -------- | --------- | ------------- | --- | ------- |
| EvoMaster, | a            | search-based |      | software | testing | framework | to       |                 |         |          |           |               |     |         |
|            |              |              |      |          |         |           |          | generated       | by GURI | based on | its Java  | data transfer |     | objects |
| generate   | system-level |              | test | suites   | for web | APIs      | exposing |                 |         |          |           |               |     |         |
(DTOs)andSpringBoot’sOASextension.WecallthisOAS
HypertextTransferProtocol(HTTP)endpointsamongothers,
inversionv2.0.01 typethedefaultOAS.However,OASsareoftenincomplete,
withmultipleparameterizationsasthe
|     |     |     |     |     |     |     |     | which leads | to ineffective | REST | test | generation | tools | [53]. |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | ---- | ---- | ---------- | ----- | ----- |
ThisisalsothecaseforCRN’sdefaultOAS,wheremedical
1.https://github.com/WebFuzzing/EvoMaster/releases/tag/v2.0.
|     |     |     |     |     |     |     |     | variables | are underconstrained |     | which, | consequently, |     | lets |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------------- | --- | ------ | ------------- | --- | ---- |
0

4
|     |     |     | Table2 |     |     |     | RQ2(codeerrors): |     |     | Weusethreetypesof500errorstrig- |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | ---------------- | --- | --- | ------------------------------- | --- | --- | --- | --- |
RulemutationoperatorsbasedonIsakuetal.[28] geredbythetools,asdefinedbyKimetal.[29]:(1)Unique
Errorsarethenumberoferrorsgroupedbytheircomplete
Name ID Description stack traces; (2) Unique Failure Points are the number of
|           |     |     |          |          | ±1  | ±1    | occurrencesofthesameerror,i.e.,thefirstlineofastacktrace; |     |     |     |     |     |     |     |
| --------- | --- | --- | -------- | -------- | --- | ----- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| AlterDate |     |     | AD Alter | the date | by  | year, |                                                           |     |     |     |     |     |     |     |
month,or±1day.
|                  |     |     |                             |     |     |     | and | (3) Unique | Library | Failure | Points | are | the number | of  |
| ---------------- | --- | --- | --------------------------- | --- | --- | --- | --- | ---------- | ------- | ------- | ------ | --- | ---------- | --- |
| NegateInequality |     |     | NI Change=to!=andviceversa. |     |     |     |     |            |         |         |        |     |            |     |
ReverseInclusion RI ChangeinconditiontonotInand errorsthatareuniquefailurepointsoccurringinthelibrary
|     |     |     | viceversa. |     |       |     | code. |     |     |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |            | >   | <=, < | >=, |       |     |     |     |     |     |     |     |
SwapComparison SComp Swap with with and RQ3(executedrulesandresults): The first domain-
viceversa.
SwapConnective SConn Swapandwithorandviceversa. specific metric is the number of (unique) executed rules
| SwapStartswith/Endswith |     |     | SSE Swap | startswith |     | twith |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | -------- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
perresulttypeandruletypeduringatool’sexecution.For
endswithandviceversa.
Rule A implies Rule example,atoolexecutes70validationruleswithPass,5with
| SwapSubrule |     |     | SSR If  |             |     |           |       |         |          |     |         |             |     |         |
| ----------- | --- | --- | ------- | ----------- | --- | --------- | ----- | ------- | -------- | --- | ------- | ----------- | --- | ------- |
|             |     |     | B       | then change | it  | to Rule B |       |         |          |     |         |             |     |         |
|             |     |     |         |             |     |           | Fail, | 10 with | Warning, | and | 70 with | Not Applied | of  | a total |
|             |     |     | implies | Rule        | A.  |           |       |         |          |     |         |             |     |         |
SwapSubstringIndices SSI Ifsubstring(i,j)thenchange of70validationrulesinv10.Notethateachrulecanhave
|     |     |     | ittosubstring(j,i). |     |     |     | multipleresulttypesduringatool’sexecution. |     |     |     |     |            |         |     |
| --- | --- | --- | ------------------- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | ---------- | ------- | --- |
|     |     |     |                     |     |     |     | RQ4(ruleandresultfrequency):               |     |     |     |     | The second | domain- |     |
specificmetricisthefrequencyoftheresulttypesperrule
the random input generator (informed by the OAS) try relativetothetotalnumberofruleexecutionsduringatool’s
| invalid variable |     | values. | Our previous | paper | [31] | showed |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------- | ------------ | ----- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
execution.Forexample,atoolexecutesruleV011%withPass,
| that, especially |     | for validation |     | rules, the | four | EvoMaster |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------------- | --- | ---------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
5%withFail,0%withWarning,and94%withNotApplied,
tools struggle to generate tests that result in Pass, Fail, or totalingto100%ofallexecutionsofthisrule.Additionally,
Warning,andmostrulesinmosttestsarebeingNotApplied. wecomparethefrequenciesofthetoolstoproductionGURI,
| Consequently, | we  | augment | the | default OAS | by  | manually |     |     |     |     |     |     |     |     |
| ------------- | --- | ------- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
deployedattheCRN,todeterminetheirsimilarity.
adding variable constraints to reflect the valid values as RQ5(mutationtesting): Thethirddomain-specificmet-
definedbyaCRN-internalvariablerepository.Wecallthis ric is inspired by the MS of (code) mutation testing [43].
OAStypethestrictOAS.Throughoutthispaper,wereport
|     |     |        |     |     |     |         | Instead | of code | mutations, |     | we rely | on the | rule mutations |     |
| --- | --- | ------ | --- | --- | --- | ------- | ------- | ------- | ---------- | --- | ------- | ------ | -------------- | --- |
|     |     | strict |     |     |     | default |         |         |            |     |         |        | Mkilled        |     |
results based on the OAS and compare to the fromSection3.5.TheMSisdefinedasMS = ,where
Mtotal
| OASinRQ3,RQ4,andRQ5. |     |     |     |     |     |     | Mkilled |        |        |             |         |     |           |      |
| -------------------- | --- | --- | --- | --- | --- | --- | ------- | ------ | ------ | ----------- | ------- | --- | --------- | ---- |
|                      |     |     |     |     |     |     |         | is the | number | of “killed” | mutants |     | that lead | to a |
Mtotal
|     |     |     |     |     |     |     | failing | test, | and | the | total number |     | of mutants, | in  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | --- | --- | ------------ | --- | ----------- | --- |
ourcase2,279.WefurtherdifferentiatebetweentheMSfor
3.5 RuleMutationOperators
validationandaggregationrules,whichwedenoteasMSV
Toevaluatethetoolswithrespecttotheirfault-findingability, andMSA,respectively.
weemployartificialrulechanges,i.e.,rulemutations,ina
mutationtestingexperimentinRQ5.Forthis,weadaptthe8
rulemutationoperatorsintroducedinourpreviouswork[28],
|          |          |       |              |       |     |          | 3.7 | ExperimentSetup |     |     |     |     |     |     |
| -------- | -------- | ----- | ------------ | ----- | --- | -------- | --- | --------------- | --- | --- | --- | --- | --- | --- |
| as shown | in Table | 2. In | our previous | work, | we  | used the |     |                 |     |     |     |     |     |     |
operatorstogeneratealargersetofvalidrulestouseastest The experiment setup is concerned with the experiment
inputs,whereasinthispaper,weemploythemutatedrules executionsettingsandexecutionenvironment.
asfaultyGURIversionsandexecutethegeneratedtestsuites TodealwiththestochasticnatureoftheEAsunderlying
(bythefivetools)againstit.Themutationoperatorsconsider EvoMaster, each tool is executed repeatedly for 30 repeti-
(1)alteringdates(AD);(2)changingsetcontainment(RI);and tions[8].Eachtoolisexecutedfor1hourforeachrepetition
(3)swappinglogicaloperators(NI,SComp,andSConn),built- and version by following the practice of Kim et al. [29].
infunctions(SSE),subruleclauses(SSR),andindices(SSI). Theyalsoobservedthatforcomplexandconstrainedinput
Weapplyeachoperatoroneatatimeoneveryruleatevery parameters,sourcecodecoverageandthrownerrorshardly
possiblelocation.Therefore,eachoperatormaybeapplied increase after 10 minutes, which is also our case. Beyond
zerotomultipletimesperrulewhentherearenoormultiple
thesesettings,theexperimentsconsiderthetoolparameteri-
possible locations, e.g., a rule contains no or multiple and zationsfromSection3.3.Theexperimentfurtherrandomizes
operators.Inversionv10,applyingthe8operatorsonthe theorderofthetoolsandversionsineachrepetition,with
| 70 validation | and | 43 aggregation |     | rules leads | to  | 2,279 rule |     |     |     |     |     |     |     |     |
| ------------- | --- | -------------- | --- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
randomizedmultipleinterleavedtrials(RMIT)[1],reducing
mutations. potentialconfoundingfactorsthatstemfromtheexecution
environmentortheexecutionorder.
Mutationtestingisknowntobecomputationallyexpen-
3.6 EvaluationMetrics
|     |     |     |     |     |     |     | sive | [43]; in | our context, | we  | need to | execute | the REST | test |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ------------ | --- | ------- | ------- | -------- | ---- |
ToevaluatetheeffectivenessofthetoolsandanswertheRQs, suitesagainsteachofthe2,279mutation.Asingletestsuite
werelyonthefollowingevaluationmetrics,whicharethe
|     |     |     |     |     |     |     | execution | takes | approximately |     | 10s. | For the | five tools, | 10  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ------------- | --- | ---- | ------- | ----------- | --- |
dependentvariablesofourstudy: versions,30repetitions,twoOAStypes,thismeansthatexe-
cutingalltestsuitesagainstallmutantstakesapproximately
| RQ1(codecoverage): |     |     | We rely | on line, | branch, | and |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | ------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
JaCoCo2,
method coverage extracted with similar to Kim 791.32dayswhenexecutedsequentially.Tokeepareasonable
etal.[29]. experiment runtime, we only execute the tools’ test suites
|     |     |     |     |     |     |     | againstGURI |     | in(themostrecent)versionv10forasingle |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
2.version0.8.8availableathttps://www.jacoco.org/jacoco repetitiontakingapproximately63.31days(sequentially).We

5
select the repetition with the median code coverage (from research,inparticular,adaptedbyarecentpublication[29],
RQ1). toanswerRQ1andRQ2.ForRQ3andRQ4,weemploytwo
We executed the experiments on the Experimental In- setsofdomain-specificmetrics,i.e.,thenumberofexecuted
frastructure for Exploration of Exascale Computing (eX3) rules and their results in RQ3 and the frequency of result
high-performancecomputing(HPC)cluster3 hostedatthe types per executed rule compared to the total number of
firstauthor’sinstitution,whichusesSlurm21.08.8-2as resultsinRQ4,whichareofspecificinteresttotheCRN.For
its cluster management software. The experiments were RQ5,weadaptthewell-knownMSformedicalrules(instead
scheduled on nodes of the same type (using the rome16q ofcodemutations)[43].Nevertheless,itisunclearwhether
partitionofeX3).ThenodeshaveanAMDEPYC7302P16- these domain-specific metrics are correlated with “good”
Core central processing units (CPUs) @ 3GHz supporting testcasesforthedomainexpertsorsufficientlytargetedto
simultaneous multithreading with 2 threads per core, run assesstestgenerationtoolsfortheCRN.Furtherinvestigation
Ubuntu 22.04.5, and have 128GB total memory. The via dedicated empirical studies is required to answer this
experiments were conducted in 2024. The Java tools were question.
exclusivelybuiltandranwithOpenJDK17.0.11builtby In terms of internal validity, a crucial threat is that
Adoptium4. EvoMaster white-box requires manually creating a subject
under test (SUT) driver. Failure to do so concerning how
3.8 StatisticalAnalyses EvoMasterexpectsthedrivertobeimplementedandGURI
requirestobecontrolledcouldthreatentheEvoMaster-WB
Ourpreviousconferencepaper[32]didnotreporttheresults
results. Similarly, an incorrect injection of the JaCoCo code
basedonstatisticaltests,whichweaddedinthispaper.
coverageagent,implementationoftheanalysesscripts,and
We use hypothesis testing and effect size measures to
adaptationofGURItoretrieveruleexecutionscouldalterthe
compare the different observations. An observation is a
study’sresultsandimplications.Wethoroughlytestedour
concretemetricvalue(seeSection3.6)foraparticulartool,
implementationstovalidatethecorrectbehaviortomitigate
GURIversion,repetition,andOAStype.
this threat. Further internal validity threats relate to the
OurexperimentsforRQ1toRQ4followacompleteblock
experiment design include: (1) the number of repetitions
design, i.e., we compare five tools in 10 versions across 30
(30inourstudy),(2)thetimebudgetfortestgeneration(1
repeatedmeasures(i.e.,repetitions).Hence,weemploythe
hour), and (3) the tool parameters (see Section 3.3). These
non-parametric Friedman test [21] and, from a statistical
design decisions are based on previous research [8, 29];
perspective, consider the tool-version pairs as individual
however,differentexperimentdesigndecisionsmightlead
subjects. We state the null hypothesis H that the subjects
0 to different results. Finally, EvoMaster relies on OpenAPI5
arethesame,andthealternativehypothesisH thattheyare
1 schema definitions to generate tests. An incorrect schema
different.UponrejectingH ,weapplyNemenyi’spost-hoc
0 definitionpotentiallyleadstosuboptimaltests,whichcould
test[40]toidentifywhichtool-versionpairsarestatistically
impactthereportedresults.Ourexperimentsusetheschema
different.
definitions generated by springdoc-openapi6 (default OAS),
As effect size measure, we use the Vargha-Delaney
whichGURIalreadyemploys,andrefinethesebymanually
Aˆ
12 [46] to characterize the magnitude of the differences. addingvariableconstraintstoformthestrictOAS.Consid-
Two version-tool pairs are the same if Aˆ 12 = 0.5. If eringthemanyparameterstoconfigure,wetrytobuildthe
Aˆ
12
>0.5,thefirstpairislargerthanthesecond,otherwise
baseofourempiricalstudyontheknowledgebuiltbythe
if Aˆ 12 < 0.5. The magnitude values are divided into four existingliteraturetomitigatetheseinternalthreats.
nominalcategories,whichrelyonthescaledAˆ
12 definedas The primary external validity threat is related to the
Aˆs
1
c
2
aled =(Aˆ
12
−0.5)∗2[26]:“negligible”(|Aˆs
1
c
2
aled|<0.147),
generalizationisinherenttothestudydesign:acasestudy
“small” (0.147 ≤ |Aˆscaled| < 0.33), “medium” (0.33 ≤
12 on a single study subject, i.e., CRN’s rule engine GURI.
|Aˆscaled|<0.474),and“large”(|Aˆscaled|≥0.474).
12 12 All results are only valid in the context of our case study
Weconsiderobservationsstatisticallysignificantdifferent
and are probably not transferable to other case studies.
atalevelα=0.01andwithanon-negligibleeffectsize.We
Nevertheless,weprovideimplicationsand“moregeneral”
controlthefalsediscoveryratewiththeBenjamini-Yekutieli
conclusionsinthediscussionsection.Moreover,ourresults
procedure[11],whichisconsideredamorepowerfulthan,
are tightly coupled with the test generation tool(s), i.e.,
e.g.,theBonferroniorHolmcorrectionsforfamily-wiseType
EvoMasterinitsfourparameterizationsandourCRN-specific
Ierrors.
extensionEvoGURI(seeSection3.3),anddonotgeneralize
NotethatwedonotusestatisticaltestsforRQ5because
tootherRESTAPItestgenerationtools.Finally,weperform
weonlyhaveasingleMSvaluepertool(seeSection3.7)
laboratoryexperimentsontheresearchHPCclustereX3with
a standalone version of GURI and not a field experiment
3.9 ThreatstoValidity against the real-world GURI (or the testing environment)
We classify threats into construct, internal, and external hosted at the CRN. Consequently, our results might not
validity. generalizetotherealsystem.Theextractionofthereal-world
Thebiggestthreattotheconstructvalidityconcernsthe GURIintoastandaloneversionfortheempiricalstudy,was,
choiceofthemetricsforevaluatingthetools’effectiveness. however,donebytheCRNdevelopers,whichshouldreduce
We rely on metrics widely used in the API test generation thisthreat.
3.https://www.ex3.simula.no 5.https://www.openapis.org
4.https://adoptium.net 6.https://springdoc.org

6
4 RESULTS
RQ1 Summary: All the tools achieve a similar line,
branch, and method coverage, with a slight edge for
ThissectionpresentstheresultsforeachRQ. EvoGURIandEvoMaster-BB,whicharestatisticallyequal
to or better than all the other tools. In the context of
theCRN,optingforasimplertestgenerationtool,i.e.,
EvoGURI or EvoMaster-BB, is preferred over a more
4.1 RQ1:CodeCoverage complex tool, i.e., any EvoMaster-WB, to cover more
sourcecode.
Westudythecodecoverageachievedbythetoolsinterms
ofline,branch,andmethodcoverages.Table3depictsthe
4.2 RQ2:CodeErrors
coverage results. We refrain from reporting coverages for
each version, as the source code does not change between ThesecondRQstudiesthethrownerrorsrelatedtosource
versions; only the rules change (see Section 3.2). Each row codebythetoolsintermsofunique500errors,uniquefailure
reportsthecoverageinpercentasthearithmeticmeanand points,anduniquelibraryfailurepoints.Table4showsthe
standard deviation (“Mean±SD”) across all the versions resultsforeachtoolacrossalltheversionsandrepetitions.
and repetitions, as well as the coverage difference in pp Similar to RQ1, we refrain from reporting errors for each
for each version when using the strict and default OASs version.Foreacherrortype(“ErrorType”,seeSection3.6),
(“Diff. Mean±SD”). In addition, we provide the results of thetabledepictsfourcategories(“ErrorCat.”):(1)thetotal
the statistical tests. (1) The “Tool Comp.” columns count numberoferrors(“All”,higherisbetter);(2)errorsthatare
how often the tool is worse (“<”), equal (“=”), and better duetothetools’intervention,e.g.,theattachedJavaagent
(“>”)thantheothertools.Notethatwecompareeachtoolin (“Tool”, lower is better); (3) input-output (I/O) errors that
eachversionagainsttheothertoolsinthesameversionand, occur during the test generation (“I/O”, lower is better);
hence,wereport40comparisons(4othertoolsin10versions). and(4)remainingerrorsthatarenotattributedtotheTool
(2) The “OAS Comp.” columns count how often the same andI/Ocategoriesbutactuallyduetoerrorsthrownbythe
toolisworse(“<”),equal(“=”),andbetter(“>”)whenusing application, i.e., GURI (“Remaining”, higher is better). In
thestrictordefaultOASsperversion(10comparisons). addition,thetablereportstheresultsofthestatisticaltests
Weobservethatalltoolsperformsimilarly,i.e.,approx- foreachtoolandversioncomparing(1)toeveryothertool
imately 21% line coverage, 16% branch coverage, and 21% and version (“Tool Comp.”) and (2) the strict and default
method coverage. Note that the relatively low (absolute) OASs(“OASComp.”),similartoRQ1.
coverage values must be considered with caution because
we generated tests for (only) 2 of 32 REST endpoints (see 4.2.1 UniqueErrors
Section 3.2), as only these two handle the medical rules. Weobservethatthedifferenttoolstriggerbetween4.18and
However,thecodecoverageisstillofinterestasarelative 5.64errors(“All”);however,onacloserinspection,wenotice
comparisonamongthetools.Regardingit,thetoolsperform thatthethreeEvoMaster-WBtoolsexperienceahighnumber
similarly, which is a different observation as obtained by oftool-relatederrors,i.e.,thecoverageagentattachedtothe
Kimetal.[29],whereEvoMaster-WB-MIOachievesahigher Javavirtualmachine(JVM)throwsaKillSwitchexception
codecoveragethanEvoMaster-BBby7.35pp(line),7.87pp whenconcurrentthreadsarerunningafterthetestgeneration
(branch),and5.69pp(method).Inaddition,Kimetal.[29] hasfinished.Thisscenarioinflatesthe“All”errors.Moreover,
reportthatthelineandmethodcoveragesaresimilarlyhigher wecanseethatallthetoolssufferfromavaryingdegreeof
thanthebranchcoverage,whichalignswithourfindings.A I/O errors, most often due to broken I/O pipe exceptions.
potential reason for the low coverage values is that all the However,EvoGURIandEvoMaster-BBsuffermorefromI/O
toolsreachthemaximumcodecoverageachievablethrough errorsthanEvoMaster-WB.Finally,thenumberof“Remain-
thetwoRESTAPIsusedinourexperiment. ing”uniqueerrorsvariesthefivetoolsbetween0.91and2.59.
Intermsofstatisticaltests,weobservethat,althoughthe MorepronouncedthanforRQ1,EvoGURIandEvoMaster-BB
meandifferencesamongthetoolsareminuscule,thereare outperformthethreeEvoMaster-WBtoolsinthe“Remaining”
statisticaldifferences:EvoGURIandEvoMaster-BBperform category, which is most important as it depicts real errors.
equally well by being better than 15 tool-version pairs for A potential reason is that trying more randomly sampled
line coverage, 16 for branch coverage, and 5 for method inputsleadstofindingmoreuniqueerrorsconsistently.
coverage, as well as never worse. This shows that black- The statistical tests reveal that EvoGURI is in 27 cases
boxapproachesaresuperiortowhite-boxapproachesinour equal and in 13 cases better than the other tool-version
settingandsuggeststhatasimplerandomsamplingleadsto pairs in finding errors (i.e., “Remaining” category). Simi-
(slightly)betterresultsthantryingtoemployasophisticated larly, EvoMaster-BB is equal in 25 and better in 15 cases.
searchalgorithm. When using the strict OAS instead of the default OAS,
WhencomparingthetwoOAStypes,weobservethatall EvoGURI,EvoMaster-BB,andEvoMaster-WB-WTSfindmore
the tools for all three coverage types perform better when errors,whileEvoMaster-WB-MIOandEvoMaster-WB-MOSA
usingthestrictOAS,showingameanimprovementbetween orlargelyunaffected.
0.98and5.89pp,Especially,theEvoMaster-WBtoolsbenefit
from the strict OAS, as they spend less time evolving an 4.2.2 UniqueFailurePoints
alreadyinvalidrequest.ThisresultisinlinewithKimetal. We observe a similar trend: “All” errors are inflated by
[29] who also found that test generation tools often suffer tool-related and I/O errors, leaving between 0.34 and 1.29
frombadperformanceduetosamplinginvalidinputdata. “Remaining” unique failure points, where EvoGURI and

7
Table3
Sourcecodecoveragepertoolacrossalltheversionsandrepetitions,eachcomparedtotheothertoolsineachversionandbetweentheOAStypes.
|     | Coverage Tool     | Mean±SD     | ToolComp. | OASComp.       |     |     |
| --- | ----------------- | ----------- | --------- | -------------- | --- | --- |
|     |                   |             | < =       | > Diff.Mean±SD | < = | >   |
|     | Line EvoGURI      | 20.99%±0.11 | 0 25      | 15 0.98pp±0.03 | 0 0 | 10  |
|     | EvoMaster-BB      | 21.00%±0.06 | 0 25      | 15 1pp±0.02    | 0 0 | 10  |
|     | EvoMaster-WB-MIO  | 20.05%±0.56 | 26 14     | 0 4.72pp±0.87  | 0 0 | 10  |
|     | EvoMaster-WB-MOSA | 20.42%±0.49 | 13 27     | 0 2.25pp±0.42  | 0 0 | 10  |
|     | EvoMaster-WB-WTS  | 20.77%±0.42 | 0 31      | 9 1.90pp±0.24  | 0 0 | 10  |
|     | Branch EvoGURI    | 16.40%±0.49 | 0 24      | 16 1.82pp±0.16 | 0 0 | 10  |
|     | EvoMaster-BB      | 16.4%±0.49  | 0 24      | 16 1.60pp±0.37 | 0 0 | 10  |
|     | EvoMaster-WB-MIO  | 15.14%±0.66 | 30 10     | 0 5.89pp±1.01  | 0 0 | 10  |
|     | EvoMaster-WB-MOSA | 15.73%±0.48 | 9 30      | 1 3.33pp±0.30  | 0 0 | 10  |
|     | EvoMaster-WB-WTS  | 16.12%±0.40 | 4 26      | 10 3pp±0.12    | 0 0 | 10  |
|     | Method EvoGURI    | 21%±0       | 0 35      | 5 0.91pp±0.12  | 0 0 | 10  |
|     | EvoMaster-BB      | 21%±0       | 0 35      | 5 0.89pp±0.15  | 0 0 | 10  |
|     | EvoMaster-WB-MIO  | 20.54%±0.51 | 15 25     | 0 3.34pp±0.62  | 0 0 | 10  |
|     | EvoMaster-WB-MOSA | 20.79%±0.41 |           | 1.57pp±0.22    |     |     |
|     |                   |             | 0 40      | 0              | 0 0 | 10  |
|     | EvoMaster-WB-WTS  | 20.98%±0.13 | 0 35      | 5 1.32pp±0.08  | 0 0 | 10  |
Table4
500errorspertoolacrossalltheversionsandrepetitions,eachcomparedtotheothertoolsineachversionandbetweentheOAStypes.
| Tool    | Error                      |           | Mean±SD   | ToolComp. | OASComp.       |        |
| ------- | -------------------------- | --------- | --------- | --------- | -------------- | ------ |
|         | Type                       | Cat.      |           | < =       | > Diff.Mean±SD | < = >  |
| EvoGURI | UniqueErrors               | All       | 4.34±1.54 | 10 28     | 2 −0.06±0.94   | 1 9 0  |
|         |                            | Tool      | 0±0       | 0 10      | 30 0±0         | 0 10 0 |
|         |                            | I/O       | 1.82±1.24 | 12 28     | 0 −1.39±0.83   | 0 2 8  |
|         |                            | Remaining | 2.52±0.84 | 0 27      | 13 1.33±0.33   | 0 0 10 |
|         | UniqueFailurePoints        | All       | 1.99±0.14 | 7 33      | 0 −0.15±0.08   | 0 10 0 |
|         |                            | Tool      | 0±0       | 0 10      | 30 0±0         | 0 10 0 |
|         |                            | I/O       | 0.77±0.42 | 0 39      | 1 −0.21±0.26   | 0 9 1  |
|         |                            | Remaining | 1.22±0.42 | 0 26      | 14 0.06±0.29   | 0 9 1  |
|         | UniqueLibraryFailurePoints |           | 1±0       | 0 30      | 10 0.98±0.03   | 0 0 10 |
EvoMaster-BB UniqueErrors All 4.57±1.82 9 27 4 0.27±1.07 1 9 0
|     |                            | Tool      | 0±0       | 0 10  | 30 0±0       | 0 10 0 |
| --- | -------------------------- | --------- | --------- | ----- | ------------ | ------ |
|     |                            |           | 1.98±1.39 |       | −1.13±0.84   |        |
|     |                            | I/O       |           | 12 28 | 0            | 0 5 5  |
|     |                            | Remaining | 2.59±0.88 | 0 25  | 15 1.40±0.33 | 0 0 10 |
|     | UniqueFailurePoints        | All       | 2.02±0.29 | 7 33  | 0 −0.10±0.10 | 0 10 0 |
|     |                            | Tool      | 0±0       | 0 10  | 30 0±0       | 0 10 0 |
|     |                            | I/O       | 0.73±0.45 | 0 40  | 0 −0.22±0.26 | 0 9 1  |
|     |                            |           | 1.29±0.50 |       | 0.13±0.33    |        |
|     |                            | Remaining |           | 0 23  | 17           | 0 9 1  |
|     | UniqueLibraryFailurePoints |           | 1±0       | 0 30  | 10 0.98±0.02 | 0 0 10 |
EvoMaster-WB-MIO UniqueErrors All 4.73±3.32 3 32 5 1.94±0.81 0 10 0
|     |                            | Tool      | 2.72±1.97 | 20 20 | 0 1.34±0.57  | 0 10 0 |
| --- | -------------------------- | --------- | --------- | ----- | ------------ | ------ |
|     |                            | I/O       | 1.11±0.92 | 0 32  | 8 0.74±0.26  | 0 10 0 |
|     |                            |           | 0.91±1.39 |       | −0.13±0.30   |        |
|     |                            | Remaining |           | 18 22 | 0            | 1 9 0  |
|     | UniqueFailurePoints        | All       | 1.97±1.28 | 3 37  | 0 0.24±0.42  | 0 10 0 |
|     |                            | Tool      | 0.76±0.48 | 20 20 | 0 0.36±0.15  | 0 10 0 |
|     |                            | I/O       | 0.86±0.66 | 1 39  | 0 0.56±0.22  | 1 9 0  |
|     |                            | Remaining | 0.34±0.48 | 21 19 | 0 −0.68±0.12 | 9 1 0  |
|     |                            |           | 0.33±0.47 |       | 0.33±0.11    |        |
|     | UniqueLibraryFailurePoints |           |           | 23 17 | 0            | 0 10 0 |
EvoMaster-WB-MOSA UniqueErrors All 4.18±2.02 6 32 2 0.43±0.59 0 10 0
|                  |                            | Tool      | 2.10±1.08 | 20 20 | 0 −0.4±0.27  | 0 10 0 |
| ---------------- | -------------------------- | --------- | --------- | ----- | ------------ | ------ |
|                  |                            | I/O       | 0.72±0.78 | 0 32  | 8 0.50±0.19  | 2 8 0  |
|                  |                            | Remaining | 1.36±1.20 | 9 31  | 0 0.32±0.20  | 0 10 0 |
|                  |                            |           | 2.11±0.99 |       | −0.07±0.34   |        |
|                  | UniqueFailurePoints        | All       |           | 2 38  | 0            | 0 10 0 |
|                  |                            | Tool      | 0.87±0.37 | 20 20 | 0 −0.08±0.07 | 0 10 0 |
|                  |                            | I/O       | 0.63±0.64 | 0 40  | 0 0.42±0.23  | 2 8 0  |
|                  |                            | Remaining | 0.61±0.49 | 9 31  | 0 −0.41±0.08 | 0 10 0 |
|                  | UniqueLibraryFailurePoints |           | 0.61±0.49 | 2 38  | 0 0.61±0.09  | 0 3 7  |
|                  |                            |           | 5.64±1.65 |       | 1.60±0.48    |        |
| EvoMaster-WB-WTS | UniqueErrors               | All       |           | 0 25  | 15           | 0 8 2  |
|                  |                            | Tool      | 2.65±0.87 | 20 20 | 0 −0.2±0.25  | 0 10 0 |
|                  |                            | I/O       | 1±0.78    | 0 32  | 8 0.81±0.20  | 5 5 0  |
|                  |                            | Remaining | 2.00±0.91 | 3 35  | 2 0.99±0.21  | 0 2 8  |
|                  | UniqueFailurePoints        | All       | 2.79±0.70 | 0 21  | 19 0.59±0.23 | 0 9 1  |
|                  |                            |           | 1.02±0.19 |       | 0.01±0.04    |        |
|                  |                            | Tool      |           | 20 20 | 0            | 0 10 0 |
|                  |                            | I/O       | 0.87±0.61 | 0 40  | 0 0.68±0.17  | 5 5 0  |
|                  |                            | Remaining | 0.9±0.31  | 4 33  | 3 −0.10±0.08 | 0 10 0 |
|                  | UniqueLibraryFailurePoints |           | 0.90±0.30 | 0 35  | 5 0.90±0.08  | 0 0 10 |

8
EvoMaster-BBoutperformEvoMaster-WB.Inmostcases,this 4.3.1 Observation1:ToolDifferences
failure point is caused by a date parsing exception, e.g.,
EvoGURIandEvoMaster-BBareonpar,executingthemost
whenthediagnosisdateofacancermessageismalformed.
validation rules for Pass (31.36 and 31.36), Fail (37.86 and
Allthetoolsfindthisfailurepoint,however,EvoGURIand
38.06),andWarning(0.78and0.75).Thestatisticaltestscon-
EvoMaster-BBfinditmoreconsistently.
firmthis,whereEvoGURIandEvoMaster-BBaresignificantly
Thestatisticaltestsyieldsimilarresultsasfortheunique
betterthanthethreeEvoMaster-WBtoolsforPassandFailin
errors.EvoGURIandEvoMaster-BBareeitherequalorbetter
alltheversionsandonlyequaltooneanother.ForWarning,
than the remaining tools, except for I/O errors. In terms
EvoGURI,EvoMaster-BB,andEvoMaster-WB-WTSareequal.
ofOASstypes,strictleadsto(mostly)thesamenumberof
OnlyforNotApplied,allthetoolsmanagetoexecuteallthe
uniquefailurepointsacrossallfourtools.
rulesforit.
Thetoolchoicemakeslessofadifferenceforaggregation
4.2.3 UniqueLibraryFailurePoints
rules.Allthetoolsyield37.6Pass,about7Warning,and0
Although seldom, all four tools trigger a unique library Not Applied rule results. We only observe differences for
failurepoint(i.e.,auniquefailurepointwherethecauseis Failresults,whereEvoGURI,EvoMaster-BB,andEvoMaster-
locatedinGURI’ssourcecode,seeSection3.6).Uponcloser WB-WTSoutperformEvoMaster-WB-MIOandEvoMaster-WB-
inspection,weidentify1GURIruleparsingerroronspecific MOSA.
inputs. Similar to the unique failure points, EvoGURI and TheseresultsareinlinewithRQ1andRQ2,i.e.,EvoGURI
EvoMaster-BBconsistentlyfindthisfailurepointacrossallthe and EvoMaster-BB are equal or superior to EvoMaster-WB.
versions.TheEvoMaster-WBtoolsfindittoavaryingdegree
Readers accustomed to REST API test generation research
in 0.33 (EvoMaster-WB-MIO), 0.61 (EvoMaster-WB-MOSA), maybesurprised,suchasKimetal.[29],aswhite-boxtools
and0.9(EvoMaster-WB-WTS)oftheversions.
usuallyhaveanadvantageoverblack-boxtools.Onereason
Thestatisticaltestsareinlinewiththeuniqueerrorsand whytheblack-boxapproachesperformbetteristhattheEA
uniquefailurepoints,EvoGURIandEvoMaster-BBareequal of EvoMaster-WB optimizes for “irrelevant” objectives for
to 30 and better than 10, and EvoMaster-WB-WTS is equal covering rules. Once EvoMaster-WB finds better solutions
to35andbetterthan5tool-versionpairs.UsingstrictOAS
forthesourcecodecoverage,itsteersitselfintoasituation
improvesthefailurepointdiscoveryforEvoGURI,EvoMaster-
where it does not execute more (different) rules anymore.
BB, and EvoMaster-WB-WTS in all versions, for EvoMaster- Conversely,EvoGURIandEvoMaster-BB,withtheirsimpler
WB-MOSAin7versions,andhasnoeffectonEvoMaster-WB-
approach(concerningcoveringsourcecode),exercisesmore
MIO.
diverseinputs(i.e.,cancermessagesandcases),whichleads
tomoreexecutedrules.
RQ2Summary: EvoGURIandEvoMaster-BBaretiedfor Moreover, we notice that EvoGURI and EvoMaster-BB
themosteffectivetoolinfindingerrors,failurepoints, havelowervarianceinthenumberofexecutedrulesamong
andlibraryfailurepoints,outperformingtheEvoMaster-
identicalrepetitions,whereasalltheEvoMaster-WBexperi-
WB tools. Similar to RQ1, this suggests employing
encehighervariancesasindicatedbytheerrorbarsinFig.1.
one of these two at the CRN for their error-revealing
capabilities.
ThismeansthattheEvoMaster-WBtoolscannotconsistently
executethesamerulesforidenticalrepetitions.
4.3 RQ3:ExecutedRulesandResults 4.3.2 Observation2:RuleTypeDifferences
Thisdomain-specificRQevaluatesthetools’abilitytoexecute Thisleadstothesecondobservation,wherethetoolsarenot
medicalrules.Figure1showsthenumberof(distinct)rules equally-effectiveinexecutingvalidationrulesastheyarefor
(onthey-axis)byeachtool(onthex-axis)foreachversion aggregationrules.Allthetoolsexecutealltheaggregation
ofGURI.Thedashedlinedepictsthetotalnumberofrules rules with Pass, whereas they only manage between 11.2
intheparticularversion.Eachbarrepresentsthearithmetic and 31.4 of 54.1 validation rules. The reason is inherent to
meanoftheruleresultsPass,Fail,WarningandNotApplied manyvalidationrules,whichcanonlyyieldaPass(aswell
(seeSection3.6),withtheerrorbarsindicatingthestandard asFailandWarning)iftheleftpartofanimplicationistrue
deviations. The first two rows depict the validation rules, (seeSection3.6)andotherwisereturnaNotAppliedresult
whereas the last two rows show the aggregation rules. In (whichallthetoolsmanageforalltherules).ForFailresults,
additionandsimilartotheTables3and4,Table5showsthe notoolmanagestoexecutealltherulesforneithervalidation
numberofexecutedrulespertoolandruletypeaggregated nor aggregation rules. However, the tools manage more
across the versions and repetitions for each result type Failresultsforvalidationrules,i.e.,18.03to38.06,thanfor
(“Mean±SD”), compares the tool-version pairs with the aggregationrules,i.e.,3.95to7.1.Thisshowsthatthetools
statisticaltests(“ToolComp.”,seeSection3.8),anddepicts are more capable of yielding Pass results for aggregation
thedifferencebetweentheOAStypes(“OASComp.”). rules and Fail and Not Applied for validation rules; and,
Wemakefourmainobservations:(1)thereisadifference conversely,strugglemoretoyieldPassforvalidationrules
ineffectivenessdependingonwhichtoolisemployed,(2)the andFailandNotAppliedforaggregationrules.Theyequally
toolsarenotequallyeffectiveforvalidationandaggregation struggletotriggerWarningresults,whichcanbeexplained
rules,(3)thetooleffectivenessdoesnotchangeacrosstheten byitbeingmorechallengingfindingcornercasesoralack
versions,and(4)usingthestrictOASachievesequalorbetter ofcorner-case-scenariosthatleadtoWarningresults.
effectivenessforallthetools.Wediscusstheseobservations Weconcludethatallthetoolsfollowthesametrendsin
indetailbelow: their capabilities and struggles in yielding the four result

9
Figure1.Numberofexecutedrulesandresultspertoolandversionacrossalltherepetitions.Thebarsarearithmeticmeans,theerrorbarsare
standarddeviations,andthedashedlinedepictsthenumberoftotalrulesofaversion.
types. However, as also outlined before, EvoGURI and unchangedfortheotherresulttypes.TheEvoMaster-WBtools
EvoMaster-BBachievebetterresultsthantheEvoMaster-WB benefitmorefromthestrictOASforPass,Fail,andWarning
tools. results. Overall, using the strict OAS is either equally or
moreeffectivethanwhenusingthedefaultOAS,makingita
4.3.3 Observation3:VersionDifferences universalsuggestiontoemployastrictOAS.Thisisinline
withtheobservationsofKimetal.[29]thatbetterOASlead
Weobservethat,withchangingrulesetsduetotheaddition,
tomoreeffectivetestgeneration.
deletion,andmodificationofrules,thetools’effectivenessis
hardlyimpacted.Forvalidationrules,theyshowincreasing
numberofPassandFailwiththegrowingnumberofrules RQ3Summary: EvoGURIandEvoMaster-BBaremore
effective in generating tests that yield Pass, Fail, and
overtheversionhistory;however,theproportionsbetween
WarningresultsthantheEvoMaster-WBtools.Whilethe
the rule results across the versions remains the same. All
results are unaffected by the rule evolution, using the
the tools manage to Pass new rules in new versions, but
strictOASleadstoconsiderablybetterresultsandcan,
thenumberofFailandWarningremainsconstantacrossthe therefore,beuniversallysuggestedfortheCRN.
versions.ThissuggeststhattheruleevolutionattheCRNis
notanimportantfactorforchoosingaparticulartoolover
another. 4.4 RQ4:RuleandResultFrequency
Thisdomain-specificRQevaluatesthetools’capabilitiesto
4.3.4 Observation4:OASDifferences
executerulesandtheirresulttypesfrequentduringthetest
Finally,wecomparethenumberofexecutedrulesandresults generationphase.Theideaisthatifatoolexecuteseachrule
when using the strict OAS instead of the default OAS. We and result more often, on average across all the rules, it is
observefromTable5thatthestrictOASconsiderablyraises morelikelytogenerateteststhatcanexposefaultsineach
thenumberofexecutedruleswithaPassandFailresultfor rule.Figure2showstheaverageruleexecutionfrequencyfor
validationrulesforallthetools.EvoGURIandEvoMaster-BB eachresulttyperelativetothetotalnumberofruleexecutions
alsobenefitfromthestrictOASforyieldingmoreWarning during a test generation phase (i.e., a 1h repetition in our
results. Aggregation rules are less affected. EvoGURI and experiments)acrossalltherules(onthey-axis)pertooland
EvoMaster-BB show an increase in Fail results and remain resulttype(onthex-axis),andversion(inthefacets).Each

10
Table5
Executedrulesandresultspertoolacrossalltheversionsandrepetitions,eachcomparedtotheothertoolsineachversionandbetweentheOAS
types.
|     | RuleType | #Rules | Tool |     | ResultType | Mean±SD | ToolComp. | OASComp.       |     |     |
| --- | -------- | ------ | ---- | --- | ---------- | ------- | --------- | -------------- | --- | --- |
|     |          |        |      |     |            |         | < =       | > Diff.Mean±SD | <   | = > |
Validation 54.1±14.24 EvoGURI Pass 31.36±7.69 0 10 30 26.95±7.52 0 0 10
|     |     |     |                   |     |            | 37.86±8.91  |       | 32.73±8.92    |     |      |
| --- | --- | --- | ----------------- | --- | ---------- | ----------- | ----- | ------------- | --- | ---- |
|     |     |     |                   |     | Fail       |             | 0 10  | 30            | 0   | 0 10 |
|     |     |     |                   |     | Warning    | 0.78±0.42   | 0 20  | 20 0.78±0.41  | 0   | 2 8  |
|     |     |     |                   |     | NotApplied | 54.1±14.24  | 0 40  | 0 0±0         | 0   | 10 0 |
|     |     |     | EvoMaster-BB      |     | Pass       | 31.4±7.69   | 0 10  | 30 26.99±7.56 | 0   | 0 10 |
|     |     |     |                   |     | Fail       | 38.06±8.92  | 0 10  | 30 32.64±8.84 | 0   | 0 10 |
|     |     |     |                   |     |            | 0.75±0.43   |       | 0.75±0.40     |     |      |
|     |     |     |                   |     | Warning    |             | 0 23  | 17            | 0   | 2 8  |
|     |     |     |                   |     | NotApplied | 54.1±14.24  | 0 40  | 0 0±0         | 0   | 10 0 |
|     |     |     | EvoMaster-WB-MIO  |     | Pass       | 11.2±5.54   | 30 10 | 0 10.22±2.11  | 0   | 0 10 |
|     |     |     |                   |     | Fail       | 18.03±9.47  | 29 11 | 0 16.22±4.78  | 0   | 0 10 |
|     |     |     |                   |     | Warning    | 0.07±0.26   | 16 24 | 0 0.07±0.05   | 0   | 10 0 |
|     |     |     |                   |     |            | 54.02±14.31 |       | 17.44±8.04    |     |      |
|     |     |     |                   |     | NotApplied |             | 0 40  | 0             | 0   | 0 10 |
|     |     |     | EvoMaster-WB-MOSA |     | Pass       | 16.52±5.04  | 20 20 | 0 15.8±3.05   | 0   | 0 10 |
|     |     |     |                   |     | Fail       | 26.21±6.89  | 20 20 | 0 25.17±6.10  | 0   | 0 10 |
|     |     |     |                   |     | Warning    | 0.20±0.40   | 16 24 | 0 0.20±0.14   | 0   | 10 0 |
|     |     |     |                   |     | NotApplied | 54.1±14.24  | 0 40  | 0 7.93±4.71   | 0   | 9 1  |
|     |     |     |                   |     |            | 22.79±5.98  |       | 22.18±5.11    |     |      |
|     |     |     | EvoMaster-WB-WTS  |     | Pass       |             | 20 10 | 10            | 0   | 0 10 |
|     |     |     |                   |     | Fail       | 30.88±7.11  | 20 11 | 9 30.03±7.03  | 0   | 0 10 |
|     |     |     |                   |     | Warning    | 0.37±0.48   | 5 35  | 0 0.37±0.20   | 0   | 5 5  |
|     |     |     |                   |     | NotApplied | 54.1±14.24  | 0 40  | 0 2.16±1.94   | 0   | 10 0 |
Aggregation 37.6±3.94 EvoGURI Pass 37.6±3.94 0 40 0 0±0 0 10 0
|     |     |     |                   |     |            | 5.74±0.46  |       | 2.27±0.11    |     |      |
| --- | --- | --- | ----------------- | --- | ---------- | ---------- | ----- | ------------ | --- | ---- |
|     |     |     |                   |     | Fail       |            | 0 19  | 21           | 0   | 0 10 |
|     |     |     |                   |     | Warning    | 7.1±0.30   | 0 40  | 0 0±0        | 0   | 10 0 |
|     |     |     |                   |     | NotApplied | 0±0        | 0 40  | 0 0±0        | 0   | 10 0 |
|     |     |     | EvoMaster-BB      |     | Pass       | 37.6±3.94  | 0 40  | 0 0±0        | 0   | 10 0 |
|     |     |     |                   |     | Fail       | 5.72±0.49  | 0 20  | 20 2.31±0.10 | 0   | 0 10 |
|     |     |     |                   |     |            | 7.1±0.30   |       | 0±0          |     |      |
|     |     |     |                   |     | Warning    |            | 0 40  | 0            | 0   | 10 0 |
|     |     |     |                   |     | NotApplied | 0±0        | 0 40  | 0 0±0        | 0   | 10 0 |
|     |     |     | EvoMaster-WB-MIO  |     | Pass       | 37.26±5.26 | 0 40  | 0 27.04±5.05 | 0   | 0 10 |
|     |     |     |                   |     | Fail       | 3.95±0.94  | 30 10 | 0 3.12±0.23  | 0   | 0 10 |
|     |     |     |                   |     | Warning    | 6.90±1.12  | 0 40  | 0 5.38±0.72  | 0   | 0 10 |
|     |     |     |                   |     |            | 0±0        |       | 0±0          |     |      |
|     |     |     |                   |     | NotApplied |            | 0 40  | 0            | 0   | 10 0 |
|     |     |     | EvoMaster-WB-MOSA |     | Pass       | 37.6±3.94  | 0 40  | 0 28.50±4.61 | 0   | 0 10 |
|     |     |     |                   |     | Fail       | 4.83±0.63  | 20 20 | 0 3.59±0.37  | 0   | 0 10 |
|     |     |     |                   |     | Warning    | 7.1±0.30   | 0 40  | 0 5.41±0.65  | 0   | 0 10 |
|     |     |     |                   |     | NotApplied | 0±0        | 0 40  | 0 0±0        | 0   | 10 0 |
|     |     |     |                   |     |            | 37.6±3.94  |       | 29.2±4.46    |     |      |
|     |     |     | EvoMaster-WB-WTS  |     | Pass       |            | 0 40  | 0            | 0   | 0 10 |
|     |     |     |                   |     | Fail       | 5.23±0.55  | 1 29  | 10 3.65±0.21 | 0   | 0 10 |
|     |     |     |                   |     | Warning    | 7.1±0.30   | 0 40  | 0 5.51±0.58  | 0   | 0 10 |
|     |     |     |                   |     | NotApplied | 0±0        | 0 40  | 0 0±0        | 0   | 10 0 |
barrepresentsthearithmeticmean,andtheerrorbarsarethe frequenciesforPass(5.76%)andFail(11.67%),andthelowest
standarddeviations.Thefirsttworowsareforthevalidation forNotApplied.Thisisalsosupportedbythestatisticaltests
rules, and the last two rows are for the aggregation rules. fromTable5.Thissuggeststhatthemostsophisticatedsearch
Inaddition,similartothepreviousRQs,Table6depictsthe algorithmmanagestogeneratemoretests(relativelytoallthe
samedataaggregatedacrosstheversionsandprovidesthe generatedtests)thatleadtoPassandFail,whicharearguably
resultsofthestatisticaltestsbetweenthetool-versionpairs theresulttypesofthehighestinteresttotheCRNdevelopers.
andthetwoOAStypes. ThebestperformingtoolsfromRQ3,i.e.,EvoGURIperforms
We make six observations: (1) EvoMaster-WB-MIO is mostlyequallytoandEvoMaster-BBperformsoftenworse
most effective in triggering Pass and Fail with EvoGURI thantheothertool-versionpairs.Foraggregationrules,the
performing competitively; (2) Not Applied for validation toolsshowmostlysimilarfrequenciestooneanotherwitha
| rules    | and Passfor | aggregationrules    |           | arethe most | frequent    | minor. |     |     |     |     |
| -------- | ----------- | ------------------- | --------- | ----------- | ----------- | ------ | --- | --- | --- | --- |
| results; | (3) there   | is no effectiveness |           | difference  | across the  |        |     |     |     |     |
| versions | as in       | RQ3; (4) there      | is a high | degree      | of variance |        |     |     |     |     |
amongrepetitions;(5)thestrictOASimproveseffectiveness 4.4.2 Observation2:ResultTypeDifferences
forPassandFailresults;and(6)theresultdistributionofthe
generatedtestsisdifferentfromproductionGURI;
|     |     |     |     |     |     | In terms   | of the four    | result types, | the results  | show that |
| --- | --- | --- | --- | --- | --- | ---------- | -------------- | ------------- | ------------ | --------- |
|     |     |     |     |     |     | one result | type dominates | the execution | frequencies. | Not       |
4.4.1 Observation1:ToolDifferences
|     |     |     |     |     |     | Applied | results are | most common | for validation | rules, |
| --- | --- | --- | --- | --- | --- | ------- | ----------- | ----------- | -------------- | ------ |
We observe different results when comparing the tools as whereasPassresultsaremostcommonforaggregationrules.
for RQ3. For validation rules, EvoMaster-WB-MIO, which Thisobservationisconsistentacrossthedifferenttoolsand
| wastheworstperformingtoolinRQ3,achievesthehighest |     |     |     |     |     | versions. |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |

11
Figure2.Ruleexecutionfrequencybyresulttyperelativetothetotalnumberofruleexecutionsduringatestgenerationphase(i.e.,repetition)for
eachrule,tool,andversion.Thebarsarearithmeticmeansandtheerrorbarsarestandarddeviations.
4.4.3 Observation3:VersionDifferences paper[31],wherewereportedtheresultsbasedonthedefault
|                 |           |         |                 |        | OAS, EvoMaster-WB-MIO |     | and EvoMaster-WB-MOSA |     |     | often |
| --------------- | --------- | ------- | --------------- | ------ | --------------------- | --- | --------------------- | --- | --- | ----- |
| Similar to RQ3, | we hardly | observe | any differences | across |                       |     |                       |     |     |       |
thedifferentversionsforallthetools.Thisstrengthensour failedtoexecuterulesatall.Thisdoesnothappenwiththe
strictOASanymore.Overall,wecanconcludethatrelyingon
| suggestion | from RQ3 that | rule evolution | is not | a deciding |     |     |     |     |     |     |
| ---------- | ------------- | -------------- | ------ | ---------- | --- | --- | --- | --- | --- | --- |
thestrictOASpositivelyaffectstheruleexecutionfrequency.
factorforchoosingonetooloveranother.
4.4.6 Observation6:ComparisontoProductionGURI
4.4.4 Observation4:RepetitionDifferences
|     |     |     |     |     | Finally, | we compare | the tools’ | rule execution | and | result |
| --- | --- | --- | --- | --- | -------- | ---------- | ---------- | -------------- | --- | ------ |
Thefirstobservationisthatthereisahighdegreeofvariance
frequencytothosefromproductionGURI,i.e.,toreal-world
of the rule execution frequency across the different rules statistics of rule execution results. Table 7 depicts this for
| and repetitions, | irrespective | of the tool, | version, | rule type, |     |     |     |     |     |     |
| ---------------- | ------------ | ------------ | -------- | ---------- | --- | --- | --- | --- | --- | --- |
“Production”andcomparesittoallthefivetools.Thevalues
andresulttype.Thismeansthatwhilegeneratingtests,the
|     |     |     |     |     | are arithmetic | means | and standard | deviations | relative | to  |
| --- | --- | --- | --- | --- | -------------- | ----- | ------------ | ---------- | -------- | --- |
toolsexecutethedifferentruleswithvaryingfrequencyin the total number of rules. Note that we only consider the
the different repetitions. This is caused by how EvoGURI toolresultsforthelatestversion,i.e.,v10,astheproduction
| and EvoMaster | generate | (new) variable | values | of cancer |     |     |     |     |     |     |
| ------------- | -------- | -------------- | ------ | --------- | --- | --- | --- | --- | --- | --- |
resultsareonlyavailableforthecurrentversion.
randomly.
messages and cancer cases: However, when we We observe that the distributions of the tools are con-
comparethiswiththeresultsfromRQ3,wenoticethatthe siderably different from production GURI. In production,
frequencyvariancehashardlyanyimpactonthenumberof
|     |     |     |     |     | most rules | are Not | Applied (73.75%) | followed | by  | Pass |
| --- | --- | --- | --- | --- | ---------- | ------- | ---------------- | -------- | --- | ---- |
executedrules,i.e.,theirvarianceacrossrulesandrepetitions
results(26.19%).Onlyafractionfails,andevenfeweryielda
isminuscule. warning.Thesituationisevenmoreextremeforaggregation
rules:99.88%oftherulesPass,andonlyanegligiblenumber
4.4.5 Observation5:OASDifferences
|     |     |     |     |     | Fail or yield | a Warning. | The closest | tool to | production, | in  |
| --- | --- | --- | --- | --- | ------------- | ---------- | ----------- | ------- | ----------- | --- |
SimilartoRQ3,employingthestrictOASlargelyimproves termsofeffectiveness,isEvoMaster-WB-MIO.However,none
theeffectivenessofthetools:acrossallthetools,PassandFail ofthetoolsachievesasimilarnumberofrulesthatPassor
resultsaretriggeredmoreoftenthanwhenusingthedefault Failforbothruletypes.
OAS, at the expense of Not Applied results for EvoGURI, Interestingly, the tools often achieve higher Fail and
EvoMaster-BB, and EvoMaster-WB-WTS. In our previous Warningratesthaninproduction.Inparticular,Failresults

12
Table6
Ruleandresultfrequenciespertoolacrossalltheversionsandrepetitions,eachcomparedtotheothertoolsineachversionandbetweentheOAS
types.
| RuleType   | Tool              | ResultType | Mean±SD      | ToolComp. | OASComp.        |        |
| ---------- | ----------------- | ---------- | ------------ | --------- | --------------- | ------ |
|            |                   |            |              | < =       | > Diff.Mean±SD  | < = >  |
| Validation | EvoGURI           | Pass       | 2.92%±0.42   | 1 33      | 6 1.77pp±0.15   | 0 0 10 |
|            |                   | Fail       | 5.84%±0.93   | 1 33      | 6 3.64pp±1.05   | 0 0 10 |
|            |                   | Warning    | 0.01%±0.00   | 0 28      | 12 0.01pp±0.00  | 0 2 8  |
|            |                   | NotApplied | 91.23%±1.08  | 9 30      | 1 −5.41pp±1.13  | 10 0 0 |
|            | EvoMaster-BB      | Pass       | 2.39%±0.40   | 20 20     | 0 1.22pp±0.14   | 0 0 10 |
|            |                   | Fail       | 4.79%±0.78   | 24 16     | 0 2.56pp±0.80   | 0 0 10 |
|            |                   | Warning    | 0.00%±0.00   | 0 33      | 7 0.00pp±0.00   | 0 2 8  |
|            |                   | NotApplied | 92.81%±1.00  | 0 13      | 27 −3.78pp±0.88 | 10 0 0 |
|            | EvoMaster-WB-MIO  | Pass       | 5.76%±3.80   | 0 25      | 15 5.18pp±0.54  | 0 0 10 |
|            |                   | Fail       | 11.67%±8.83  | 0 29      | 11 10.32pp±2.84 | 0 0 10 |
|            |                   | Warning    | 0.01%±0.09   | 17 23     | 0 0.01pp±0.02   | 0 10 0 |
|            |                   | NotApplied | 82.41%±12.06 | 13 27     | 0 14.17pp±8.24  | 0 10 0 |
|            | EvoMaster-WB-MOSA | Pass       | 3.02%±1.82   | 4 34      | 2 2.98pp±0.68   | 0 0 10 |
|            |                   | Fail       | 6.21%±3.42   | 3 35      | 2 6.15pp±0.62   | 0 0 10 |
|            |                   | Warning    | 0.01%±0.03   | 6 34      | 0 0.01pp±0.01   | 0 10 0 |
|            |                   | NotApplied | 90.77%±4.94  | 3 33      | 4 4.63pp±5.48   | 0 10 0 |
|            | EvoMaster-WB-WTS  | Pass       | 2.88%±0.61   | 2 34      | 4 2.85pp±0.36   | 0 0 10 |
|            |                   | Fail       | 6.05%±1.26   | 0 31      | 9 5.99pp±0.79   | 0 0 10 |
|            |                   | Warning    | 0.01%±0.01   | 0 36      | 4 0.01pp±0.00   | 0 5 5  |
|            |                   | NotApplied | 91.07%±1.65  | 8 31      | 1 −5.08pp±2.94  | 10 0 0 |
Aggregation EvoGURI Pass 89.19%±0.88 0 31 9 0.75pp±0.10 0 0 10
|     |              | Fail       | 3.18%±0.40  | 3 37 | 0 0.55pp±0.07  | 0 0 10 |
| --- | ------------ | ---------- | ----------- | ---- | -------------- | ------ |
|     |              | Warning    | 7.63%±0.71  | 3 34 | 3 −1.30pp±0.16 | 10 0 0 |
|     |              | NotApplied | 0%±0        | 0 40 | 0 0pp±0        | 0 10 0 |
|     | EvoMaster-BB | Pass       | 89.08%±0.90 | 5 32 | 3 0.66pp±0.07  | 0 0 10 |
|     |              | Fail       | 3.18%±0.41  | 3 37 | 0 0.57pp±0.07  | 0 0 10 |
|     |              | Warning    | 7.74%±0.73  | 0 33 | 7 −1.23pp±0.13 | 10 0 0 |
|     |              | NotApplied | 0%±0        | 0 40 | 0 0pp±0        | 0 10 0 |
EvoMaster-WB-MIO Pass 90.19%±8.96 0 23 17 65.68pp±9.11 0 0 10
|     |     | Fail       | 3.53%±0.86 | 0 34  | 6 2.31pp±0.45 | 0 1 9  |
| --- | --- | ---------- | ---------- | ----- | ------------- | ------ |
|     |     | Warning    | 5.36%±2.22 | 22 18 | 0 3.53pp±0.93 | 0 5 5  |
|     |     | NotApplied | 0%±0       | 0 40  | 0 0pp±0       | 0 10 0 |
EvoMaster-WB-MOSA Pass 88.68%±1.03 26 14 0 67.84pp±7.95 0 0 10
|     |                  | Fail       | 3.33%±0.61  | 0 40 | 0 1.28pp±0.53  | 0 6 4  |
| --- | ---------------- | ---------- | ----------- | ---- | -------------- | ------ |
|     |                  | Warning    | 7.99%±1.03  | 0 25 | 15 5.85pp±1.02 | 0 4 6  |
|     |                  | NotApplied | 0%±0        | 0 40 | 0 0pp±0        | 0 10 0 |
|     | EvoMaster-WB-WTS | Pass       | 89.07%±0.92 | 3 32 | 5 69.88pp±4.69 | 0 0 10 |
|     |                  | Fail       | 3.27%±0.43  | 0 40 | 0 0.53pp±0.33  | 0 10 0 |
|     |                  | Warning    | 7.66%±0.77  | 3 34 | 3 5.76pp±0.63  | 0 0 10 |
|     |                  | NotApplied | 0%±0        | 0 40 | 0 0pp±0        | 0 10 0 |
Table7
Ruleexecutionfrequencybyresulttyperelativetothetotalnumberofruleexecutionsduringatestgenerationphase(i.e.,repetition)foreachruleand
tool.Thevaluesarearithmeticmeans±standarddeviationssummarizedonruletypelevelacrossalltheindividualrules.Productioncorrespondsto
theruleexecutionsfromproductionGURI.Thevaluesforthetestgenerationtoolsareforthelatestversionv10,averagedacrossalltherepetitions.
| RuleType | Tool | ResultType |      |         |     |            |
| -------- | ---- | ---------- | ---- | ------- | --- | ---------- |
|          |      | Pass       | Fail | Warning |     | NotApplied |
Validation Production 26.19%±37.32 0.05%±0.15 6.55×10−6%±5.52×10−5 73.75%±37.38
|             | EvoGURI           | 2.59%±5.20   | 5.27%±7.62   | 0.01%±0.05  |     | 92.14%±9.63  |
| ----------- | ----------------- | ------------ | ------------ | ----------- | --- | ------------ |
|             | EvoMaster-BB      | 2.03%±4.46   | 4.11%±6.41   | 0.00%±0.03  |     | 93.86%±8.06  |
|             | EvoMaster-WB-MIO  | 5.07%±15.93  | 10.87%±23.62 | 0.00%±0.12  |     | 84.06%±27.91 |
|             | EvoMaster-WB-MOSA | 2.83%±7.77   | 6.46%±11.74  | 0.01%±0.13  |     | 90.71%±14.03 |
|             | EvoMaster-WB-WTS  | 2.58%±5.34   | 5.32%±8.06   | 0.01%±0.08  |     | 92.10%±9.94  |
|             |                   | 99.88%±0.47  | 0.02%±0.08   | 0.10%±0.47  |     | 0%±0         |
| Aggregation | Production        |              |              |             |     |              |
|             | EvoGURI           | 89.81%±18.72 | 2.88%±10.61  | 7.31%±15.41 |     | 0%±0         |
|             | EvoMaster-BB      | 89.67%±18.97 | 2.90%±10.63  | 7.43%±15.66 |     | 0%±0         |
|             | EvoMaster-WB-MIO  | 90.57%±18.54 | 3.31%±11.86  | 6.12%±14.13 |     | 0%±0         |
|             | EvoMaster-WB-MOSA | 89.38%±19.70 | 3.02%±10.94  | 7.61%±16.26 |     | 0%±0         |
|             |                   | 89.49%±19.33 | 2.99%±10.79  | 7.52%±15.89 |     | 0%±0         |
EvoMaster-WB-WTS

13
|     |     |     |     | Table8 |     |     |     | resultsfromRQ3,wherehardlyanyrulesyieldedPass,Fail, |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Mutationtestingresults. or Warning and most are Not Applied; consequently, the
|     |     |     |     |     |     |     |     | generated | tests | are incapable | of killing | the mutants. |     | For |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ------------- | ---------- | ------------ | --- | --- |
Tool OASType Tests MSV MSA aggregationrules,theOASdoesnotimpacttheMSs,asall
thetoolsareabletoPassalltherules.
|     | EvoGURI      |     | strict  |     | 43  | 0.96 | 1   |             |     |                               |     |     |     |     |
| --- | ------------ | --- | ------- | --- | --- | ---- | --- | ----------- | --- | ----------------------------- | --- | --- | --- | --- |
|     |              |     | default |     | 19  | 0    | 1   |             |     |                               |     |     |     |     |
|     | EvoMaster-BB |     | strict  |     | 10  | 0    | 0   |             |     |                               |     |     |     |     |
|     |              |     |         |     |     |      |     | RQ5Summary: |     | EvoGURI,EvoMaster-WB-MOSA,and |     |     |     |     |
|     |              |     | default |     | 8   | 0    | 0   |             |     |                               |     |     |     |     |
EvoMaster-WB-MIO strict 34 0.13 1 EvoMaster-WB-WTS are highly effective in killing mu-
default 13 0 1 tants for both validation and aggregation rules, with
|     | EvoMaster-WB-MOSA |     | strict  |     | 48  | 0.96 | 1   |                                           |       |            |                     |            |            |     |
| --- | ----------------- | --- | ------- | --- | --- | ---- | --- | ----------------------------------------- | ----- | ---------- | ------------------- | ---------- | ---------- | --- |
|     |                   |     |         |     |     |      |     | EvoMaster-BB                              |       | failing to | detect the mutants. |            | The strict |     |
|     |                   |     | default |     | 17  | 0    | 1   |                                           |       |            |                     |            |            |     |
|     |                   |     |         |     |     |      |     | OAS                                       | has a | big impact | on the MS for       | validation | rules.     |     |
|     | EvoMaster-WB-WTS  |     | strict  |     | 50  | 0.96 | 1   |                                           |       |            |                     |            |            |     |
|     |                   |     | default |     | 20  | 0    | 1   | WecansuggestEvoGURIbeingusedattheCRNdueto |       |            |                     |            |            |     |
itshighMSsandsimplersetupthantheEvoMaster-WB
tools.
| occur      | considerably |       | more     | often    | with 4.11% | to          | 10.87% for |     |     |     |     |     |     |     |
| ---------- | ------------ | ----- | -------- | -------- | ---------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| validation |              | rules | and 2.88 | to 3.31% | for        | aggregation | rules.     |     |     |     |     |     |     |     |
The tools trigger Warning results in around 0.01% of the 6 DISCUSSION AND LESSONS LEARNED
validationruleexecutionsandbetween6.12%and7.61%for Thissectiondiscussestheresultsandoutlineslessonslearned,
aggregationrules.Thisshowsthatallthetoolsarepotentin
whichprovideresearchopportunities.
manygeneratingtestsforfailureandcornercasesthatlead
toFailandWarningresults.
6.1 NeedforDomain-SpecificObjectives,Targets,and
EvaluationMetrics
|     | RQ4 Summary: |     | EvoMaster-WB-MIO |     |     | has the | highest |     |     |     |     |     |     |     |
| --- | ------------ | --- | ---------------- | --- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
number of Pass and Fail results with EvoGURI being From RQ1 and RQ2, we see that the differences among
competitively. For all the tools, the validation rules the tools are minor, even though they may be statistically
are the easiest to yielding Not Applied followed by significant. Hence, we require domain-specific evaluation
Fail, and aggregation rules are the easiest to return metricstodifferentiatebetweenthetoolswhentraditional
|     | Pass followed |     | by Warning. | The | strict | OAS improves |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | ----------- | --- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
evaluationmetricsfailtodoso.Therefore,weintroducedtwo
effectivenessacrossallthetools,especiallyforPassand
noveldomain-specificmetricsinRQ3andRQ4andadapted
|     | Fail results. |     | Compared | to production |     | GURI, | no tool |     |     |     |     |     |     |     |
| --- | ------------- | --- | -------- | ------------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
awell-knownmetric,i.e.,MS,toourdomain-specificcasein
|     | can Pass | a similar | amount | of  | rules, | but all are | good |     |     |     |     |     |     |     |
| --- | -------- | --------- | ------ | --- | ------ | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
atgeneratingteststhatleadtoFailandWarningresults; RQ5.Moreover,influencedbythefindingsofourprevious
paper[31],weextendedthebesttool,i.e.,EvoMaster-BB,and
|     |     |     |     |     |     |     |     | incorporate | domain-specific |     | targets (rule | and | result types) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | --- | ------------- | --- | ------------- | --- |
5 RQ5: MUTATION TESTING into the test generation process with EvoGURI. Our paper
showsthatdomain-specificityisessentialtoevaluatingcur-
Finally,thisRQevaluatestheabilityinfindingartificialrule
renttoolsandadaptingthemforreal-worldcontexts.Hence,
| faults | by  | the tools’ | generated |     | test suites. | Based | on the | 8              |     |                 |       |         |              |     |
| ------ | --- | ---------- | --------- | --- | ------------ | ----- | ------ | -------------- | --- | --------------- | ----- | ------- | ------------ | --- |
|        |     |            |           |     |              |       |        | going forward, |     | test generation | tools | require | (1) encoding |     |
rulemutationoperators,theexperimentcomprises2,279rule
domain-specificobjectivesintheirsearch,e.g.,withadded
| mutations |     | against | which | the test | suites | are executed | (see |     |     |     |     |     |     |     |
| --------- | --- | ------- | ----- | -------- | ------ | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
domain-specificsearchobjectives(e.g.,rule(result)countor
Sections 3.5 and 3.7). Table 8 depicts the MSs per tool and distancemetricstoapplyingrules[2]),oraddingteststhat
OAStype,i.e.,separatingtheMSforvalidationrulesMSV
reachunseendomain-specifictargetstothearchive(similarto
andaggregationrulesMSA.
Padhyeetal.[41]);(2)keepingtestsafterthesearchthatcover
We observe that EvoGURI, EvoMaster-WB-MOSA, and eachdomain-specifictargetforregressiontestingscenarios;
| EvoMaster-WB-WTS |     |     | achieve | the | highest | MS for | validation |     |     |     |     |     |     |     |
| ---------------- | --- | --- | ------- | --- | ------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
and(3)evaluatingtestgenerationtoolswithdomain-specific
rules,i.e.,0.96,almostkillingallthemutants.Foraggregation
metrics(ruleexecutionstatusandruleexecutionresultsin
rules,EvoGURIandtheEvoMaster-WBtoolsachieveaperfect
ourcase)toshowtheireffectivenesswhentraditionalmetrics
scoreof1,killingallthemutants.AreasonforthehighMSs
donotshowdifferences(alsodiscussedbyBöhmeetal.[12]).
| is  | that the | mutations | are | relatively | easy | to kill, | as a minor |     |     |     |     |     |     |     |
| --- | -------- | --------- | --- | ---------- | ---- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
changetotherulealreadyyieldsadifferentresultandcan
6.2 OracleProblemforRuleExecutionResults
bedetectedbythetestsuite.
Interestingly,EvoMaster-BB,whichistiedforthenumber The oracle problem is a well-known problem in software
of executed rules with EvoGURI in RQ3, has a MS of 0 testing [10], which extends also to domain-specific goals.
forbothvalidationandaggregationrules.Weassumethat Whileweshowthatthecurrenttoolscanexecuteruleswith
this happens because of the low number of retained test different results, it is unclear if, for a randomly generated
cases in the final test suite. All the other tools generate testinput,aruleisexpectedtoPass,Fail,yieldaWarning,
larger test suites, as they aim for covering more search orshouldbeNotApplied.Currentresearchdoesnotoffer
targets than EvoMaster-BB (see Section 3.3). Actually, the a solution; there simply is no implicit oracle [10] for rule
increased number of search targets is the key difference executions.Goingforward,thisneedstobeaddressed,and
betweenEvoMaster-BBandEvoGURI.
|     |     |     |     |     |     |     |     | we see four | potential | aspects: | (1) using | tests that | lead | to a |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | -------- | --------- | ---------- | ---- | ---- |
SimilartotheotherRQs,employingthestrictOASenables specificruleresult(Pass,Fail,Warning)andemployingthem
killing mutants at all for validation rules. This is in line inaregressiontestingsetting,e.g.,ifatestpassesarulein
withourpreviouspaper’sresults[31]andthedefaultOAS version 1, it should also pass in version 2, for which one

14
couldusethetestsuitesgeneratedbyEvoGURI;(2)applying metamorphic testing; and required evaluations that go
differential testing by comparing the outputs of the same beyondcodecoverageanderrors[13].Thisshowsthatwhile
random test input to, e.g., a reference implementation for ourresultsarespecifictoGURI,thechallengesareimportant
the medical rules, as they should be standardized, which to the research community. Consequently, our paper is a
we explored in Isaku et al. [28]; (3) devising metamorphic valuablecasestudyprovidingdataforthesechallenges.
| relations | on the | rules | that are | either | semantics-preserving |     |     |     |     |     |     |     |     |     |     |
| --------- | ------ | ----- | -------- | ------ | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(similartoLuetal.[37])orareknowntoleadtoinvalidrules
6.5 CallforStudieswithDomain-SpecificGoals
| and comparing |     | the outputs |     | to the | correct | implementation; |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | --- | ------ | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and(4)usinglargelanguagemodels(LLMs)asoracles,as
|     |     |     |     |     |     |     |     | Based on | our | findings | showing | that | code | coverage | and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | ------- | ---- | ---- | -------- | --- |
theyarelikelytrainedonthemedicalknowledge,regulations, uncoverederrorsareinsufficienttoevaluateautomatedtest
andstandards,bypromptingwhetheraruleresultreturned generation tools, we conclude that there is a dire need for
byGURIiscorrectforagiveninput.
|     |     |     |     |     |     |     |     | more industrial |          | and      | public | sector | case  | studies       | like ours. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | -------- | -------- | ------ | ------ | ----- | ------------- | ---------- |
|     |     |     |     |     |     |     |     | As also         | outlined | by Böhme |        | et al. | [12], | code coverage | is         |
6.3 ChallengeofGeneratingMedicalData insufficienttovalidatetestgenerationtoolsandfuzzers.For
Generating synthetic medical data is a challenge for re- example,whichtoolisbetterwhencodecoverageisequal,
ornoerrorsarefound?ExactlythishappensintheCRN’s
| searchers | from | many | fields | are trying | to  | tackle | [16, 23]. In |           |          |           |     |       |           |            |     |
| --------- | ---- | ---- | ------ | ---------- | --- | ------ | ------------ | --------- | -------- | --------- | --- | ----- | --------- | ---------- | --- |
|           |      |      |        |            |     |        |              | case. The | research | community |     | needs | to better | understand |     |
softwaretesting,generatingsyntheticandvalidmedicaldata
|            |            |     |             |     |                 |     |           | domain-specific |     | needs | for test | generation, |     | objectives, | and |
| ---------- | ---------- | --- | ----------- | --- | --------------- | --- | --------- | --------------- | --- | ----- | -------- | ----------- | --- | ----------- | --- |
| is equally | important. |     | The current |     | test generation |     | tools are |                 |     |       |          |             |     |             |     |
targetstooptimizefor,andevaluationmetricsthatarebetter
| good at       | generating | syntax-compliant |              |     | data     | (e.g., | according    |         |      |               |     |            |      |      |            |
| ------------- | ---------- | ---------------- | ------------ | --- | -------- | ------ | ------------ | ------- | ---- | ------------- | --- | ---------- | ---- | ---- | ---------- |
|               |            |                  |              |     |          |        |              | aligned | with | stakeholders’ |     | interests; | and, | as a | next step, |
| to an OpenAPI |            | schema           | definition). |     | However, |        | the individ- |         |      |               |     |            |      |      |            |
evolvecurrenttoolstosupportthesedomain-specificneeds
| ual variable | values | (i.e., | medical |     | variables) | are | randomly |     |     |     |     |     |     |     |     |
| ------------ | ------ | ------ | ------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
better.
generated.Thisleadstomanyinvalidcancermessagesand
casestobecheckedbytheruleengine,suchaswhenusing
| the default | OAS | as done | in  | our | previous | paper | [31]. We |           |     |      |     |     |     |     |     |
| ----------- | --- | ------- | --- | --- | -------- | ----- | -------- | --------- | --- | ---- | --- | --- | --- | --- | --- |
|             |     |         |     |     |          |       |          | 7 RELATED |     | WORK |     |     |     |     |     |
improvedonthisinthispaperbyaddingastrictOASthat
constrainsthemedicalvariablestoonlyvalidvalues,which 7.1 TestGenerationforRESTAPIs
| we manually | derived |     | from | CRN-internal |     | documentation, |     |     |     |     |     |     |     |     |     |
| ----------- | ------- | --- | ---- | ------------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Manyindustrialapplications,especiallythosebuiltwiththe
whichimproveseffectivenessacrossallourRQs.However,
|     |     |     |     |     |     |     |     | microservice |     | architecture | expose | REST | APIs. | As  | a result, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------ | ------ | ---- | ----- | --- | --------- |
thisonlyleadstovaliddataandnotnecessarilytorealistic
thereisanincreasingdemandforautomatedtestingofsuch
| data, i.e., | in our         | context,   | data        | that    | accurately  |                 | mimics real |              |                |              |         |                 |       |              |           |
| ----------- | -------------- | ---------- | ----------- | ------- | ----------- | --------------- | ----------- | ------------ | -------------- | ------------ | ------- | --------------- | ----- | ------------ | --------- |
|             |                |            |             |         |             |                 |             | REST APIs.   | Consequently,  |              | we      | can             | see a | significant  | rise in   |
| cancer      | patient        | data.      | We identify |         | four        | potential       | ways to     |              |                |              |         |                 |       |              |           |
|             |                |            |             |         |             |                 |             | publications | in             | recent       | years   | [22]. Moreover, |       | several      | open-     |
| address     | this challenge |            | in the      | context | of          | test generation | in          |              |                |              |         |                 |       |              |           |
|             |                |            |             |         |             |                 |             | source       | and industrial |              | REST    | API testing     | tools | are          | available |
| the future: | (1) using      | generative |             | models  | such        | as              | generative  |              |                |              |         |                 |       |              |           |
|             |                |            |             |         |             |                 |             | such as      | EvoMaster      | [4–7],       | RESTler |                 | [9],  | RestTestGen  | [15],     |
| adversarial | networks       |            | (GANs)      | or      | variational | autoencoders    |             |              |                |              |         |                 |       |              |           |
|             |                |            |             |         |             |                 |             | RESTest      | [39],          | Schemathesis |         | [18], Dredd     |       | [17], Tcases | [30],     |
(VAEs)trainedonrealpatientrecordstogeneratevalidand
|     |     |     |     |     |     |     |     | bBOXRT | [33, | 34], and | APIFuzzer | [3]. | Even | though | any of |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | -------- | --------- | ---- | ---- | ------ | ------ |
realisticcancermessagesandcasestodirectlytestGURI[25];
|     |     |     |     |     |     |     |     | these tools | can | be used | in our | context, | we  | use | EvoMaster, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ------ | -------- | --- | --- | ---------- |
(2)usinggeneratedcancermessagesandcasesinEvoMaster
sinceitisopen-sourceandhasbeenshowntobethemost
| either as | seeds | or when | new | requests |     | are sampled; | and |     |     |     |     |     |     |     |     |
| --------- | ----- | ------- | --- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
effectiveregardingsourcecodecoverageandthrownerrors
| (3) employing | LLMs, |     | possibly | trained | on  | electronic | health |     |     |     |     |     |     |     |     |
| ------------- | ----- | --- | -------- | ------- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
amongtendifferenttoolsinarecentstudy[29].
| records | (EHRs) | or medical |     | text [35, | 44, 49, | 50], | to generate |     |     |     |     |     |     |     |     |
| ------- | ------ | ---------- | --- | --------- | ------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Generally,RESTAPItestingapproachesareclassifiedinto
variablevalues.
|     |     |     |     |     |     |     |     | black-box | (no | source code | access) |     | and white-box |     | (requires |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----------- | ------- | --- | ------------- | --- | --------- |
sourcecodeaccess)[22].Theexistingliteraturehasdeveloped
6.4 GeneralityoftheResults testingtechniquesfromthreemainperspectivestoevaluate
While the results are specific to the case study, i.e., GURI testing effectiveness [22]: (1) coverage criteria, e.g., code
at the CRN, the findings and lessons learned are likely coverage(e.g.,branchcoverage)andschemacoverage(e.g.,
applicable in other contexts. (1) Other countries also have request input parameters); (2) fault detection, e.g., service
medicalregistriessimilartotheCRN,whichalsodealswith errors (i.e, HTTP status code 5XX) and REST API schema
EHR. These can benefit from the challenges and findings violations;and(3)performancemetrics,i.e.,relatedtothere-
outlinedinthispapertointroduceautomatedtestgeneration sponsetimeofRESTAPIrequests.Toachievetheseobjectives,
tools. (2) Rule-based systems, in general, potentially face variousalgorithmshavebeendevelopedintheliterature.For
similar challenges. Once generated tests pass the input instance,EvoMasterhasimplementedseveralEAsincluding
validation and execute rules, they will also have to deal random testing [5–7]. Various extensions have been also
with, e.g., domain-specific objectives, the oracle problem, proposedtoEvoMaster,suchashandlingsequencesofREST
andgeneratingdatathatexecutestherules.(3)Anysystem API calls and their dependencies [54], handling database
thatdynamicallyloadstargetsofinterestwilllikelyalsobe access through structured query language (SQL) [51], and
affectedbytheneedfordomain-specificobjectivesandtar- testingremoteprocedurecall(RPC)-basedAPIs[55].Inour
gets.(4)ResearchersatarecentDagstuhlseminardiscussed case,wehaveaccesstothesourcecodeofGURI;therefore,we
similar challenges, such as domain-specific objectives and employboththeblack-boxandthewhite-box(parameterized
targets;comparisontoproduction;domain-specificoracles withthreeEAs)toolsofEvoMaster.However,anextended
suchasreferenceimplementations,differentialtesting,and investigationinthefuturemayincludeothertools.

15
Compared to the literature, our main contribution is automatedtestgenerationsolution.Wealsoprovidelessons
applyinganopen-sourceRESTAPItestingtoolinthereal- learnedthatarebeneficialforresearchersandpractitioners.
worldcontextoftheCRN.Weassessthetool’seffectiveness
| in achieving | code coverage, |     | errors | found, | and | domain- |     |     |     |     |     |     |     |     |
| ------------ | -------------- | --- | ------ | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
ACKNOWLEDGEMENTS
| specific | metrics (e.g., | related | to medical |     | rules defined | for |     |     |     |     |     |     |     |     |
| -------- | -------------- | ------- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ThisworkreceivedfundingfromTheResearchCouncilof
| validating | and aggregating |     | cancer | messages | and | cancer |                                                 |              |     |                |     |     |             |     |
| ---------- | --------------- | --- | ------ | -------- | --- | ------ | ----------------------------------------------- | ------------ | --- | -------------- | --- | --- | ----------- | --- |
| cases).    |                 |     |        |          |     |        | Norway(RCN)undertheproject309642andhasbenefited |              |     |                |     |     |             |     |
|            |                 |     |        |          |     |        | from the                                        | Experimental |     | Infrastructure |     | for | Exploration | of  |
ExascaleComputing(eX3),whichissupportedbytheRCN
| 7.2 DevelopmentandTestingofCancerRegistrySys- |     |     |     |     |     |     | project270053. |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
tems
InourrecentpaperwiththeCRN[32],weassessthecurrent
REFERENCES
| state of      | practice and | identify | challenges |         | (e.g., test | automa- |                                                           |          |       |           |                |     |     |             |
| ------------- | ------------ | -------- | ---------- | ------- | ----------- | ------- | --------------------------------------------------------- | -------- | ----- | --------- | -------------- | --- | --- | ----------- |
|               |              |          |            |         |             |         | [1] A.AbediandT.Brecht,“Conductingrepeatableexperimentsin |          |       |           |                |     |     |             |
| tion, testing | evolution,   | and      | testing    | machine | learning    | (ML)    |                                                           |          |       |           |                |     |     |             |
|               |              |          |            |         |             |         | highly                                                    | variable | cloud | computing | environments,” |     | in  | Proceedings |
algorithms) when testing CRN’s CaReSS. In our previous of the 8th ACM/SPEC on International Conference on Performance
paper[31],wetookthefirstconcretesteptowardshandling Engineering,ser.ICPE2017. NewYork,NY,USA:ACM,2017,pp.
287–292.[Online].Available:http://doi.acm.org/10.1145/3030207.
thosechallenges,particularlyassessingtheeffectivenessof
3030229
anexistingtestingtoolintheCRN’scontext.Inthispaper,
|     |     |     |     |     |     |     | [2] S. Ali, | M. Z. | Iqbal, A. | Arcuri, | and | L. C. Briand, | “Generating |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --------- | ------- | --- | ------------- | ----------- | --- |
we extend our previous paper based on our findings and test data from OCL constraints with search techniques,” IEEE
introduceadomain-specificextensiontoEvoMasternamed TransactionsonSoftwareEngineering,vol.39,no.10,pp.1376–1402,
Oct.2013.[Online].Available:https://doi.org/10.1109/tse.2013.17
| EvoGURI, | refine the | OAS | to only | generate | valid | cancer |                |     |            |        |     |         |             |       |
| -------- | ---------- | --- | ------- | -------- | ----- | ------ | -------------- | --- | ---------- | ------ | --- | ------- | ----------- | ----- |
|          |            |     |         |          |       |        | [3] APIFuzzer, |     | “APIFuzzer | – HTTP | API | testing | framework,” | 2022, |
messagesandcases,andassessthefault-findingcapabilities
|     |     |     |     |     |     |     | accessed | 23.8.2023. |     | [Online]. | Available: | https://github.com/ |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --------- | ---------- | ------------------- | --- | --- |
ofthegeneratedtestsuiteswithadomain-specificmutation KissPeter/APIFuzzer
|     |     |     |     |     |     |     | [4] A. Arcuri, | “EvoMaster: |     | Evolutionary |     | multi-context |     | automated |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | --- | ------------ | --- | ------------- | --- | --------- |
testingapproach.Threeotherrecentworksbuildcyber-cyber
systemtestgeneration,”inProceedingsofthe11thIEEEInternational
physicaltwinsforGURI[36],incorporateMLclassifiersinto
|           |           |         |      |           |         |         | Conference | on    | Software   | Testing, | Verification |     | and Validation, | ser.       |
| --------- | --------- | ------- | ---- | --------- | ------- | ------- | ---------- | ----- | ---------- | -------- | ------------ | --- | --------------- | ---------- |
| EvoMaster | to reduce | testing | cost | [27], and | utilize | LLMs to |            |       |            |          |              |     |                 |            |
|           |           |         |      |           |         |         | ICST       | 2018. | IEEE, Apr. | 2018,    | pp. 394–397. |     | [Online].       | Available: |
https://doi.org/10.1109/ICST.2018.00046
| generate | test cases used | in  | a differential |     | testing | approach |         |       |                  |     |      |          |             |     |
| -------- | --------------- | --- | -------------- | --- | ------- | -------- | ------- | ----- | ---------------- | --- | ---- | -------- | ----------- | --- |
|          |                 |     |                |     |         |          | [5] ——, | “Test | suite generation |     | with | the Many | Independent |     |
withareferenceimplementation[28].
Objective(MIO)algorithm,”InformationandSoftwareTechnology,
| In the | past, we developed |     | a   | model-based | engineering |     |      |          |          |      |       |           |            |        |
| ------ | ------------------ | --- | --- | ----------- | ----------- | --- | ---- | -------- | -------- | ---- | ----- | --------- | ---------- | ------ |
|        |                    |     |     |             |             |     | vol. | 104, pp. | 195–206, | Dec. | 2018. | [Online]. | Available: | https: |
frameworktosupportCaReSSattheCRN[47].Theframe- //doi.org/10.1016/j.infsof.2018.05.003
|     |     |     |     |     |     |     | [6] ——, | “RESTful | API | automated | test | case | generation | with |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | --------- | ---- | ---- | ---------- | ---- |
workaimstocreatehigh-levelandabstractmodelstocapture
|     |     |     |     |     |     |     | EvoMaster,” |     | ACM Transactions |     | on  | Software | Engineering | and |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------------- | --- | --- | -------- | ----------- | --- |
variousrules,theirvalidation,selection,andaggregation.The
Methodology,vol.28,no.1,pp.1–37,Feb.2019.[Online].Available:
frameworkisimplementedbasedontheUnifiedModeling https://doi.org/10.1145/3293455
Language (UML) and Object Constraint Language (OCL), [7] ——,“Automatedblack-andwhite-boxtestingofRESTfulAPIs
withEvoMaster,”IEEESoftware,vol.38,no.3,pp.72–78,May2021.
wheretheUMLisusedtocapturedomainconceptsandthe
[Online].Available:https://doi.org/10.1109/MS.2020.3013820
OCLisusedtospecifymedicalrules.Theimplementation
|     |     |     |     |     |     |     | [8] A.ArcuriandL.Briand,“Apracticalguideforusingstatistical |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
oftheframeworkhasbeenincorporatedinsideGURI,which teststoassessrandomizedalgorithmsinsoftwareengineering,”
is the subject of testing in this paper. As a follow-up, we in Proceedings of the 33rd International Conference on Software
|                |           |     |          |          |          |     | Engineering, |     | ser. ICSE | 2011. | ACM, | 2011, | pp. 1–10. | [Online]. |
| -------------- | --------- | --- | -------- | -------- | -------- | --- | ------------ | --- | --------- | ----- | ---- | ----- | --------- | --------- |
| also developed | an impact |     | analysis | approach | focusing | on  |              |     |           |       |      |       |           |           |
Available:https://doi.org/10.1145/1985793.1985795
capturing changes in rules and assessing their impact to [9] V.Atlidakis,P.Godefroid,andM.Polishchuk,“RESTler:Stateful
facilitateasystematicevolutionofrules[48].Finally,wealso RESTAPIfuzzing,”inProceedingsofthe41stIEEE/ACMInternational
developed a search-based approach to refactor such rules ConferenceonSoftwareEngineering,ser.ICSE2019. IEEE,May2019.
[Online].Available:https://doi.org/10.1109/icse.2019.00083
regardingtheirunderstandabilityandmaintainability[37]. [10] E.T.Barr,M.Harman,P.McMinn,M.Shahbaz,andS.Yoo,“The
Comparedtotheexistingworks,thispaperfocusesontesting oracleprobleminsoftwaretesting:Asurvey,”IEEETransactionson
GURI as a first step toward building cost-effective testing SoftwareEngineering,vol.41,no.5,pp.507–525,May2015.[Online].
Available:https://doi.org/10.1109/tse.2014.2372785
techniquesattheCRN. [11] Y.BenjaminiandD.Yekutieli,“Thecontrolofthefalsediscovery
rateinmultipletestingunderdependency,”TheAnnalsofStatistics,
|               |     |     |     |     |     |     | vol.                                   | 29, no. | 4, pp. 1165–1188, |     | Aug.        | 2001. | [Online].       | Available: |
| ------------- | --- | --- | --- | --- | --- | --- | -------------------------------------- | ------- | ----------------- | --- | ----------- | ----- | --------------- | ---------- |
| 8 CONCLUSIONS |     |     |     |     |     |     | https://doi.org/10.1214/aos/1013699998 |         |                   |     |             |       |                 |            |
|               |     |     |     |     |     |     | [12] M. Böhme,                         | L.      | Szekeres,         | and | J. Metzman, | “On   | the reliability | of         |
Thispaperreportsonanempiricalstudyevaluatingthetest coverage-basedfuzzerbenchmarking,”inProceedingsofthe44th
effectivenessofEvoMaster’sfourtestingtoolsandEvoGURIa IEEE/ACM International Conference on Software Engineering, ser.
|     |     |     |     |     |     |     | ICSE2022. |     | ACM,May2022,pp.1621–1633.[Online].Available: |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
domain-specificEvoMasterextensiononareal-worldsystem,
https://doi.org/10.1145/3510003.3510230
theCancerRegistryofNorway(CRN)’sCancerRegistration
|     |     |     |     |     |     |     | [13] M.Böhme,M.Christakis,R.Padhye,K.Serebryany,A.Zeller,and |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
Support System (CaReSS). CaReSS is a complex software H.F.Eniser,“Softwarebugdetection:Challengesandsynergies
|        |               |               |     |        |           |         | (Dagstuhl | seminar | 23131),” |     | Dagstuhl | Reports, | vol. 13, | no. 3, pp. |
| ------ | ------------- | ------------- | --- | ------ | --------- | ------- | --------- | ------- | -------- | --- | -------- | -------- | -------- | ---------- |
| system | that collects | and processes |     | cancer | patients’ | data in |           |         |          |     |          |          |          |            |
92–105,Oct.2023.[Online].Available:https://drops.dagstuhl.de/
Norwayandproducesstatisticsanddataforitsendusers.
entities/document/10.4230/DagRep.13.3.92
Ourresultsshowthatthefivestudiedtestingtoolsperform
|     |     |     |     |     |     |     | [14] F. Bray,     | M.  | Laversanne, | H.        | Sung,   | J. Ferlay, | R.         | L. Siegel, |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ----------- | --------- | ------- | ---------- | ---------- | ---------- |
|     |     |     |     |     |     |     | I. Soerjomataram, |     | and         | A. Jemal, | “Global | cancer     | statistics | 2022:      |
similarlyregardingcodecoverageanderrorsreportedacross
GLOBOCANestimatesofincidenceandmortalityworldwidefor
| all the | studied versions. |     | However, | in  | terms of | domain- |     |     |     |     |     |     |     |     |
| ------- | ----------------- | --- | -------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
36cancersin185countries,”CA:ACancerJournalforClinicians,
| specific  | metrics, our | CRN-specific |     | EvoGURI | is      | the most |      |         |                 |          |     |       |           |            |
| --------- | ------------ | ------------ | --- | ------- | ------- | -------- | ---- | ------- | --------------- | -------- | --- | ----- | --------- | ---------- |
|           |              |              |     |         |         |          | vol. | 74, no. | 3, pp. 229–263, | May/June |     | 2024. | [Online]. | Available: |
| effective | tool; hence, | we recommend |     | it for  | the CRN | as an    |      |         |                 |          |     |       |           |            |
https://doi.org/10.3322/caac.21834

16
[15] D.Corradini,A.Zampieri,M.Pasqua,E.Viglianisi,M.Dallago, [32] ——,“Challengesoftestinganevolvingcancerregistrationsupport
and M. Ceccato, “Automated black-box testing of nominal and systeminpractice,”inProceedingsofthe45thIEEE/ACMInternational
error scenarios in RESTful APIs,” Software Testing, Verification ConferenceonSoftwareEngineering:CompanionProceedings,ser.ICSE-
and Reliability, vol. 32, no. 5, Jan. 2022. [Online]. Available: Companion2023. IEEE,May2023,pp.355–359.[Online].Available:
https://doi.org/10.1002/stvr.1808 https://doi.org/10.1109/ICSE-Companion58688.2023.00102
[16] F.K.DankarandM.Ibrahim,“Fakeittillyoumakeit:Guidelines [33] N. Laranjeiro, J. Agnelo, and J. Bernardino, “A black box
foreffectivesyntheticdatageneration,”AppliedSciences,vol.11, tool for robustness testing of REST services,” IEEE Access,
no.5,2021. vol. 9, pp. 24738–24754, Feb. 2021. [Online]. Available:
[17] Dredd,“Dredd–HTTPAPItestingframework,”2021,accessed https://doi.org/10.1109/ACCESS.2021.3056505
23.8.2023.[Online].Available:https://dredd.org [34] N. Laranjeiro, C. F. F. Santos, and J. Agnelo, “EvoReFuzz –
[18] D. Dygalo, “Schemathesis: Property-based testing for API evolutionary REST fuzzer,” 2022, accessed 23.8.2023. [Online].
schemas,” 2023, accessed 23.8.2023. [Online]. Available: https: Available:https://git.dei.uc.pt/cnl/bBOXRT
//schemathesis.readthedocs.io [35] V. Liévin, C. E. Hother, and O. Winther, “Can large language
[19] G.FraserandA.Arcuri,“EvoSuite:Automatictestsuitegeneration modelsreasonaboutmedicalquestions?”2023.[Online].Available:
for object-oriented software,” in Proceedings of the 19th ACM https://doi.org/10.48550/arXiv.2207.08143
SIGSOFTSymposiumandthe13thEuropeanConferenceonFoundations [36] C. Lu, Q. Xu, T. Yue, S. Ali, T. Schwitalla, and J. F.
ofSoftwareEngineering,ser.ESEC/FSE2011. ACM,2011.[Online]. Nygård, “EvoCLINICAL: Evolving cyber-cyber digital twin
Available:https://doi.org/10.1145/2025113.2025179 with active transfer learning for automated cancer registry
[20] ——,“Wholetestsuitegeneration,”IEEETransactionsonSoftware system,” in Proceedings of the 31th ACM Joint European Software
Engineering, vol. 39, no. 2, pp. 276–291, Feb. 2013. [Online]. Engineering Conference and Symposium on the Foundations of
Available:https://doi.org/10.1109/TSE.2012.14 Software Engineering, ser. ESEC/FSE 2023. New York, NY,
[21] M. Friedman, “The use of ranks to avoid the assumption of USA: ACM, Nov. 2023, pp. 1973–1984. [Online]. Available:
normality implicit in the analysis of variance,” Journal of the https://doi.org/10.1145/3611643.3613897
AmericanStatisticalAssociation,vol.32,no.200,pp.675–701,1937. [37] H. Lu, S. Wang, T. Yue, S. Ali, and J. F. Nygård, “Automated
[Online]. Available: https://www.tandfonline.com/doi/abs/10. refactoringofOCLconstraintswithsearch,”IEEETransactionson
1080/01621459.1937.10503522 SoftwareEngineering,vol.45,no.2,pp.148–170,Feb.2019.[Online].
[22] A.Golmohammadi,M.Zhang,andA.Arcuri,“TestingRESTful Available:https://doi.org/10.1109/tse.2017.2774829
APIs: A survey,” ACM Transactions on Software Engineering and [38] B.Marculescu,M.Zhang,andA.Arcuri,“Onthefaultsfoundin
Methodology,vol.33,no.1,pp.1–41,Nov.2023.[Online].Available: RESTAPIsbyautomatedtestgeneration,”ACMTransactionson
https://doi.org/10.1145/3617175 SoftwareEngineeringandMethodology,vol.31,no.3,pp.1–43,Jul.
[23] A. Goncalves, P. Ray, B. Soper, J. Stevens, L. Coyle, and A. P. 2022.[Online].Available:https://doi.org/10.1145/3491038
Sales,“Generationandevaluationofsyntheticpatientdata,”BMC [39] A. Martin-Lopez, S. Segura, and A. Ruiz-Cortés, “RESTest:
MedResMethodol,vol.20,no.1,p.108,2020,goncalves,Andre Automatedblack-boxtestingofRESTfulwebAPIs,”inProceedings
Ray,PriyadipSoper,BradenStevens,JenniferCoyle,LindaSales, of the 30th ACM SIGSOFT International Symposium on Software
Ana Paula eng England BMC Med Res Methodol. 2020 May TestingandAnalysis,ser.ISSTA2021. ACM,Jul.2021,pp.682–685.
7;20(1):108.doi:10.1186/s12874-020-00977-1.[Online].Available: [Online].Available:https://doi.org/10.1145/3460319.3469082
https://www.ncbi.nlm.nih.gov/pubmed/32381039 [40] P.B.Nemenyi,“Distribution-freemultiplecomparisons,”Doctoral
[24] R. Haas, D. Elsner, E. Juergens, A. Pretschner, and S. Apel, Thesis,PrincetonUniversity,1963.
“How can manual testing processes be optimized? Developer [41] R. Padhye, C. Lemieux, K. Sen, L. Simon, and H. Vijayakumar,
survey,optimizationguidelines,andcasestudies,”inProceedings “FuzzFactory:Domain-specificfuzzingwithwaypoints,”Proceedings
of the 29th ACM Joint European Software Engineering Conference oftheACMonProgrammingLanguages,vol.3,no.OOPSLA,pp.1–29,
and Symposium on the Foundations of Software Engineering, Oct.2019.[Online].Available:https://doi.org/10.1145/3360600
ser. ESEC/FSE 2021. ACM, Aug. 2021. [Online]. Available: [42] A. Panichella, F. M. Kifetew, and P. Tonella, “Automated test
https://doi.org/10.1145/3468264.3473922 casegenerationasamany-objectiveoptimisationproblemwith
[25] M. Hernandez, G. Epelde, A. Alberdi, R. Cilla, and D. Rankin, dynamic selection of the targets,” IEEE Transactions on Software
“Syntheticdatagenerationfortabularhealthrecords:Asystematic Engineering, vol. 44, no. 2, pp. 122–158, Feb. 2018. [Online].
review,”Neurocomputing,vol.493,pp.28–45,2022. Available:https://doi.org/10.1109/tse.2017.2663435
[26] M.R.HessandJ.D.Kromrey,“Robustconfidenceintervalsfor [43] M. Papadakis, M. Kintis, J. Zhang, Y. Jia, Y. Le Traon, and
effectsizes:Acomparativestudyofcohen’sdandcliff’sdeltaunder M. Harman, “Chapter six - mutation testing advances: An
non-normalityandheterogeneousvariances,”AnnualMeetingofthe analysis and survey,” in Advances in Computers. Elsevier,
AmericanEducationalResearchAssociation,Apr.2004. 2019, vol. 112, pp. 275–378. [Online]. Available: https:
[27] E. Isaku, H. Sartaj, C. Laaber, S. Ali, T. Yue, T. Schwitalla, //doi.org/10.1016/bs.adcom.2018.03.015
and J. F. Nygård, “Cost reduction on testing evolving cancer [44] K. Singhal, S. Azizi, T. Tu, S. S. Mahdavi, J. Wei, H. W.
registry system,” in Proceedings of the 39th IEEE International Chung,N.Scales,A.Tanwani,H.Cole-Lewis,S.Pfohl,P.Payne,
Conference on Software Maintenance and Evolution, ser. ICSME M. Seneviratne, P. Gamble, C. Kelly, N. Scharli, A. Chowdhery,
2023. IEEE, Oct. 2023, pp. 508–518. [Online]. Available: P. Mansfield, B. Aguera y Arcas, D. Webster, G. S. Corrado,
https://doi.org/10.1109/ICSME58846.2023.00065 Y.Matias,K.Chou,J.Gottweis,N.Tomasev,Y.Liu,A.Rajkomar,
[28] E. Isaku, C. Laaber, H. Sartaj, S. Ali, T. Schwitalla, and J. F. J. Barral, C. Semturs, A. Karthikesalingam, and V. Natarajan,
Nygård, “LLMs in the heart of differential testing: A case “Largelanguagemodelsencodeclinicalknowledge,”2022.[Online].
study on a medical rule engine,” 2024. [Online]. Available: Available:https://doi.org/10.48550/arXiv.2212.13138
https://doi.org/10.48550/arXiv.2404.03664 [45] K.-J. Stol and B. Fitzgerald, “The ABC of software engineering
[29] M.Kim,Q.Xin,S.Sinha,andA.Orso,“Automatedtestgeneration research,” ACM Transactions on Software Engineering and
forRESTAPIs:Notimetorestyet,”inProceedingsofthe31stACM Methodology,vol.27,no.3,pp.1–51,Oct.2018.[Online].Available:
SIGSOFTInternationalSymposiumonSoftwareTestingandAnalysis, https://doi.org/10.1145/3241743
ser.ISSTA2022. ACM,Jul.2022,pp.289–301.[Online].Available: [46] A.VarghaandH.D.Delaney,“Acritiqueandimprovementofthe
https://doi.org/10.1145/3533767.3534401 "CL"commonlanguageeffectsizestatisticsofMcGrawandWong,”
[30] K. Kimbrough, Juglar, and T. Kruse, “Tcases: A model-based JournalofEducationalandBehavioralStatistics,vol.25,no.2,pp.101–
testcasegenerator,”2023,accessed23.8.2023.[Online].Available: 132,2000.[Online].Available:https://doi.org/10.2307/1165329
https://github.com/Cornutum/tcases [47] S. Wang, H. Lu, T. Yue, S. Ali, and J. Nygård, “MBF4CR: A
[31] C. Laaber, T. Yue, S. Ali, T. Schwitalla, and J. F. Nygård, model-based framework for supporting an automated cancer
“Automatedtestgenerationformedicalruleswebservices:Acase registrysystem,”inProceedingsofthe12thEuropeanConferenceon
studyattheCancerRegistryofNorway,”inProceedingsofthe31st ModellingFoundationsandApplications,ser.ECMFA2016. Springer
ACMJointEuropeanSoftwareEngineeringConferenceandSymposium International Publishing, 2016, pp. 191–204. [Online]. Available:
on the Foundations of Software Engineering, ser. ESEC/FSE 2023. https://doi.org/10.1007/978-3-319-42061-5_12
NewYork,NY,USA:ACM,Nov.2023,pp.1937–1948.[Online]. [48] S. Wang, T. Schwitalla, T. Yue, S. Ali, and J. F. Nygård,
Available:https://doi.org/10.1145/3611643.3613882 “RCIA: Automated change impact analysis to facilitate a
practical cancer registry system,” in Proceedings of the 33rd

17
IEEE International Conference on Software Maintenance and [Online].Available:https://doi.org/10.1007/978-3-030-88106-1_8
Evolution,ser.ICSME2017. IEEE,Sep.2017.[Online].Available: [52] ——, “Adaptive hypermutation for search-based system
https://doi.org/10.1109/icsme.2017.22 test generation: A study on REST APIs with EvoMaster,”
[49] X. Yang, A. Chen, N. PourNejatian, H. C. Shin, K. E. Smith, ACM Transactions on Software Engineering and Methodology,
C. Parisien, C. Compas, C. Martin, A. B. Costa, M. G. vol. 31, no. 1, pp. 1–52, Jan. 2022. [Online]. Available:
Flores, Y. Zhang, T. Magoc, C. A. Harle, G. Lipori, D. A. https://doi.org/10.1145/3464940
Mitchell, W. R. Hogan, E. A. Shenkman, J. Bian, and Y. Wu, [53] ——,“OpenproblemsinfuzzingRESTfulAPIs:Acomparisonof
“A large language model for electronic health records,” npj tools,”ACMTransactionsonSoftwareEngineeringandMethodology,
Digital Medicine, vol. 5, no. 1, Dec. 2022. [Online]. Available: vol. 32, no. 6, pp. 144:1–144:45, Nov. 2023. [Online]. Available:
https://doi.org/10.1038/s41746-022-00742-2 https://doi.org/10.1145/3597205
[50] L. Yunxiang, L. Zihan, Z. Kai, D. Ruilong, and Z. You, [54] M. Zhang, B. Marculescu, and A. Arcuri, “Resource and
“ChatDoctor:Amedicalchatmodelfine-tunedonLLaMAmodel dependencybasedtestcasegenerationforRESTfulwebservices,”
using medical domain knowledge,” 2023. [Online]. Available: EmpiricalSoftwareEngineering,vol.26,no.4,Jun.2021.[Online].
https://doi.org/10.48550/arXiv.2303.14070 Available:https://doi.org/10.1007/s10664-020-09937-1
[51] M. Zhang and A. Arcuri, “Enhancing resource-based test case [55] M.Zhang,A.Arcuri,Y.Li,Y.Liu,andK.Xue,“White-boxfuzzing
generationforRESTfulAPIswithSQLhandling,”inProceedings RPC-basedAPIswithEvoMaster:Anindustrialcasestudy,”ACM
of the 13th International Symposium on Search Based Software TransactionsonSoftwareEngineeringandMethodology,vol.32,no.5,
Engineering, ser. SSBSE 2021. Springer, Oct. 2021, pp. 103–117. Sep.2023.[Online].Available:https://doi.org/10.1145/3585009