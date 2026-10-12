---
conversion_metadata:
  converted_at: "2026-10-12T07:34:41Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "R. Huang et al., 2025.pdf"
  source_pdf_sha256: "84dde4f9a91e373683836e5bb17e90e369f0216dde848991fcf6245fa8dd74c2"
  page_count: 10
  markdown_char_count: 53522
---

Wealth-Voyager: Navigating IntelligentWealth Management with
a Multi-Agent Framework
RuiHuang ZimoZhao SiwenChen
BlockchainandIntelligent BlockchainandIntelligent BlockchainandIntelligent
TechnologyResearchCenter TechnologyResearchCenter TechnologyResearchCenter
TheChineseUniversityofHong TheChineseUniversityofHong TheChineseUniversityofHong
Kong,Shenzhen Kong,Shenzhen Kong,Shenzhen
Shenzhen,Guangdong,China Shenzhen,Guangdong,China Shenzhen,Guangdong,China
rayhuang@cuhk.edu.cn zimozhao@link.cuhk.edu.cn siwenchen@cuhk.edu.cn
XiaoyuWu J.LeonZhao∗
IndependentResearcher SchoolofManagementand
Shenzhen,Guangdong,China Economics
xiaoyuwu5@gmail.com TheChineseUniversityofHong
Kong,Shenzhen
Shenzhen,Guangdong,China
leonzhao@cuhk.edu.cn
Abstract Keywords
Risingdemandforhyper-personalizedwealthmanagementisin- Generativelargelanguagemodels(LLMs),Multi-agentsystems,
creasinglyunmetbytraditionaladvisorymodels,whichsufferfrom Behavioralfinance,Portfoliooptimization,Personalizedadvisory
limitationsinscalability,cost-efficiency,andobjectivity.Whilere-
centAI-drivensolutionsshowpromise,theyoftenremainfrag- ACMReferenceFormat:
mented,focusingonisolatedtasksandlackingaunifiedarchitec- RuiHuang,ZimoZhao,SiwenChen,XiaoyuWu,andJ.LeonZhao.2025.
turethatintegrateslong-termstrategywithdynamicbehavioral Wealth-Voyager:NavigatingIntelligentWealthManagementwithaMulti-
adaptation. To bridge this gap, we introduce Wealth-Voyager,
AgentFramework.In2025InternationalConferenceonGenerativeArtificial
a multi-agent framework that synergizes strategic asset alloca- IntelligenceforBusiness(GAIB2025),August04–06,2025,Hongkong,China.
ACM,NewYork,NY,USA,10pages.https://doi.org/10.1145/3766918.3766944
tionwithadaptivetacticaladjustments.Oursystem’sarchitecture
uniquelycombinesAlphaForge,aquantitativeengineforestab-
lishingalong-termstrategicportfolio,withDualAdvisor,anovel 1 Introduction
Belief-Desire-Intention(BDI)groundedrole-playingsimulationthat
Overthepastdecade,risingmacroeconomicvolatilityandrapid
interactivelymanagesuser-specificbehavioralbiasesinresponse
fintechinnovationhavefueledunprecedenteddemandforhyper-
toreal-timeevents.Ourproof-of-conceptcasestudy,conducted
personalizedwealthmanagementsolutions.By2023,globalassets
under live market conditions, demonstrated the efficacy of this
undermanagement(AUM)hadreachedUSD1.2trillion[25],yet
integratedapproach.Thesystem’sadaptivetacticaladjustments
anestimated320millionpotentialinvestorsremainedunderserved
outperformedapassivebaseline,convertingamarginalgaininto
byconventionaladvisorychannels.Thisgapisespeciallyacute
amoresubstantialreturnwhilereducingportfoliovolatility.Our
inChina,whereaburgeoning“newmiddleclass”withrisingin-
work presents a blueprint for a new class of financial co-pilots
vestableassetsisincreasinglyseekingtechnology-enabledfinancial
thatintegratequantitativerigorwithinteractive,cognitively-aware
guidance.Empiricalevidencefrom290Chinesecitiesshowsthat
guidance,enhancingbothdecisionqualityandusertrust.
fintechadoptionsignificantlyenhancesfinancialaccess,depth,and
inclusion—particularlybenefitinghouseholdswithlowerwealth
CCSConcepts
andlimitedaccesstotraditionaladvisoryservices[14].
•Socialandprofessionaltopics→Economicimpact. Traditionalwealthmanagementframeworksareundergrowing
pressuretomeettheevolvingexpectationsofanincreasinglydi-
verseanddigitallysophisticatedinvestorbase.Inmarketssuchas
∗Correspondingauthor.
China,thedominanceofbank-ledfunddistributionchannels—typically
associatedwithhighfeesandlimitedpersonalization—furthercon-
strains access to tailored services, particularly for emerging in-
vestorsandtheexpandingmiddleclass.Beyondstructuralineffi-
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense. ciencies,behavioralchallengessuchasspeculativetrading,early
GAIB2025,Hongkong,China fundredemptions,andlimitedfinancialliteracyremainwidespread.
©2025Copyrightheldbytheowner/author(s). Trustinconventionaladvisorymodelsisfurthererodedbyinade-
ACMISBN979-8-4007-1602-7/25/08
https://doi.org/10.1145/3766918.3766944 quatetransparencyandalackoftimely,proactiveengagement[13].
156

GAIB2025,August04–06,2025,Hongkong,China Huangetal.
Moreover,mostincumbentplatformslackthereal-time,behavior- NewsCrawler(real-timeintelligenceextraction),AlphaForge
awareanalyticsrequiredtosupportinvestorsduringvolatilemarket (scenario-awareportfoliooptimization),andDualAdvisor(BDI-
conditions,ultimatelyfailingtoaddressbothperformance-driven based advisory simulation)–to emulate the workflow of elite
goalsandthepsychologicalfactorsthatshaperetailinvestment investment-researchteams.
behavior[14]. • Behaviour-awarepersonalization.LeveragingLLM-basedse-
Toaddressthesechallenges,recentresearchhasincreasingly manticreasoning,AssistHubinferslatentclientpreferencesand
focusedonemergingtechnologiesthatenablemoreadaptiveand cognitivebiases,enablingpersonalisedstrategiesalignedwith
investor-centricsolutions.Advancesinlargelanguagemodels(LLMs) individualbehaviouralprofilesthatadaptandimproveovertime.
andmulti-agentframeworksofferpromisingalternativestocon- • Real-timeadaptivedecision-making.Bycontinuouslymoni-
ventionalfinancialadvisorysystems.LLM-basedadvisorsfacilitate toringmarketdynamicsthroughNewsCrawlerandperforming
personalized,context-awareinteractions[21,27],yetremaincostly on-the-flyre-optimizationinAlphaForge,thesystemreduces
todeployandlimitedinadaptability[7].Multi-agentsystemsim- decisionlatency,supportstimelyportfoliorebalancing,andproac-
provescalabilitybydistributingfinancialtasksacrossspecialized tivelymitigatestheimpactofblack-swanevents.
roles[10,20].However,mostimplementationsexhibitthreekey • Bridgingtheeducation–decisiongap.Throughexplainable
limitations.First,thelackofbehavioralmodelingpreventsthese dialogueandinteractivescenariotesting,DualAdvisoralignsfi-
systemsfromaccountingforcognitivebiases—suchasoverconfi- nancialeducationwithactionableportfoliochoices,empowering
denceorlossaversion—thatfrequentlyshaperetailinvestorbe- userstodeveloplong-termwealth-managementcompetence.
havior.Second,intheabsenceofinteractiveexplainability,users
• Transparencyandtrustbydesign.Throughscenario-based
receiveopaquerecommendationsthatunderminetrustandreduce
analysis,rationaletracing,andverifiableneutralrecommenda-
engagement.Third,thestaticnatureoftheirdecisionlogicimpedes
tions, the system reveals its decision-making logic, promotes
real-timeresponsivenesstomarketevents—anessentialcapability
financialliteracy,andbuildsusertrustinatransparentandac-
formaintainingportfoliorelevanceinvolatileenvironments.
countablemanner.
Given these limitations in existing systems, the choice of an
Collectively, WealthVoyager introduces a promising frame-
underlyinginvestmentphilosophyiscritical.Weanchorourframe-
workthattransitionsfromstaticassetallocationstrategiestoan
workinassetallocation,whichfinancialliteraturewidelyrecog-
interactivesystemcapableofdeliveringpersonalized,adaptive,and
nizesasthecornerstoneoflong-termportfolioreturns,responsible
transparentwealthmanagementatscale.
forover90%ofperformancevariance[4,5,12].Incontrasttomore
speculativeandvolatilestrategieslikemarkettimingorstockpick-
ing,assetallocationprovidesamorestable,risk-managedpathto 2 RelatedWork
wealthgrowththroughdiversificationandsystematicriskmanage-
2.1 Multi-AgentFrameworks
ment.Thisphilosophyisimplementedthroughtwocomplementary
layers:StrategicAssetAllocation(SAA),whichsetsthefounda- Multi-agent(MA)frameworkshavegainedincreasingtractionin
tional,long-termpolicyportfolio,andTacticalAssetAllocation financialdecision-makingbydistributingportfoliomanagement
(TAA),which enablesdynamic, short-termadjustmentsto that tasksamongspecializedagents,eachresponsibleforsubtaskssuch
policy.ThestructuredyetflexiblenatureoftheSAA-TAAframe- asassetselection,marketmonitoring,orriskcontrol.Recentsys-
workmakesitanidealdomainforanadvisorysystemthatmust temssuchasFinCon[29]incorporatelargelanguagemodels(LLMs)
alsoaddressthecriticalgapsinbehavioralmodelingandreal-time ashigh-levelcoordinatorsacrossagentteams,facilitatingnatural
adaptiveness. language-basedcommunicationandreflectivebeliefrevisionin
WepresentWealth-Voyager,abehavior-aware,multi-agent volatileenvironments.MASA[20]introducesarole-basedstruc-
financialadvisoryframeworkcoordinatedbyacentralLLM-based turecomprisingrewardmaximizers,risksolvers,andmacroob-
meta-controller.Thesystemintegratesstructuredfinancialsignals, servers,witheachagentadaptingautonomouslythroughdeeprein-
unstructuredmarketnarratives,andinvestor-specificbehavioral forcementlearning.Earlierframeworks,includingMAPS[18]and
traitstodeliveradaptive,personalized,andinterpretableportfolio MSPM[11],emphasizedmodularitybydecouplingstrategygenera-
guidance.Throughstructuredfunctioncallsandsharedmemory, tionfromassetevaluation,therebyenhancingdiversityandscalabil-
theLLMorchestratesateamofspecializedagentsresponsiblefor ity.Morerecentefforts,suchasMASS[10]andTradingAgents[28],
userprofiling,newsinterpretation,portfoliooptimization,andad- simulatecollaborativetradingdeskswhereLLM-drivenagentsas-
visorydialoguesimulation.ByembeddingMonteCarlo–basedrisk sumespecializedroles—suchassentimentanalysisandtradeexecu-
modeling,event-drivenrebalancing,andcognitivebiasadaptation, tion—demonstratingstrongperformanceinhigh-frequencytrading
Wealth-Voyagermovesbeyondstaticallocationtools.Itfunctions environments.
asaninteractiveco-pilot,enablinguserstounderstand,trust,and Whileexistingsystemsdemonstratestrongspecialization,they
iterativelyrefinetheirfinancialdecisionsindynamicmarketenvi- often focus on short-term trading or static planning, with lim-
ronments. itedsupportforcontinuousadaptationorinvestor-facingeduca-
tion.Wealth-Voyageraddressesthesegapsbyenablingpersistent,
behavior-awarecoordinationthatevolveswithuserpreferences
KeyContributions:
andmarketdynamics.Leveragingreal-timenewsanalyticsanda
• Modularmulti-agentcollaboration.WealthVoyagerorches- MonteCarlore-samplingloop,itcananticipaterarebutdisrup-
tratesfourspecialisedagents–AssistHub(behaviouralprofiling), tiveeventssuchasmarketshocks.Meanwhile,theDualAdvisor
157

Wealth-Voyager:NavigatingIntelligentWealthManagementwithaMulti-AgentFramework GAIB2025,August04–06,2025,Hongkong,China
modulefostersfinancialliteracythroughinteractivedialoguesthat 3 Framework
clarifytrade-offs,surfacebiases,andenablescenario-basedlearn- 3.1 OverallArchitecture
ing—shiftingthesystemfromexecutiontolong-terminvestorem-
Toprovidepersonalizedandreal-timefinancialadvisoryservices
powerment.
forindividualusers,weproposeanend-to-endframeworknamed
Wealth-Voyager.AsillustratedinFig.1,thesystemintegrates
multiplecollaboratingagentsthatdynamicallyinteractwithcore
2.2 LargeLanguageModelsforInvestment tools,includinganintelligentcustomerassistant,anewscrawler,
andportfoliooptimizationmodels.Inaddition,arole-playingdia-
DecisionSupport
loguemodulethatemploysadual-agent,role-playingsimulation
Largelanguagemodels(LLMs)havebecomeincreasinglyinfluential todeliveradaptiveguidancethatisresponsivetobothreal-time
infinancialdecisionsupportbyenablingcontextualunderstanding, marketeventsandtheuser’suniquebehavioralprofile.
generation,andinteractionacrossarangeofinvestment-related
tasks.FinLLM[21]appliesinstructiontuningtoprovidepersonal-
izedadvicetoretailinvestors,whileBloombergGPT [27]demon- 3.2 CoreModules
stratestheadvantagesoflarge-scale,domain-specificpretraining
AssistHubisanintelligentcustomerservicemodule,implemented
fortaskssuchasentityrecognitionandfinancialquestionanswer-
asanagenticworkflowontheDify[17]platformandpowered
ing.LLM-Advisor [16]integratesreal-timenewssummarization
by ChatGPT-4 [1]. Through a guided conversational process of
andeventinterpretationintoaninteractiveadvisoryworkflow,and
context-aware,adaptivetestingandinteractivecalibrationdynamic,
LLM-Survey [7]offersacomprehensiveoverviewofhowLLMs
itdynamicallyhandlesgeneralinquiriesandassistsusersinarticu-
supporttheassetmanagementlifecycle—frominformationextrac-
latingtheirwealthmanagementgoals(e.g.,retirementsavings,edu-
tiontoportfolioconstruction.Despitethisprogress,manyexisting
cationalfunds),detailingtheircurrentfinancialstatus,andcomplet-
systemsunder-addresscriticalchallengesrelatedtoprobabilistic
ingapersonalizedriskassessment.AssistHubreplacesthe"static
uncertaintyandbehavioralbiasesininvestordecision-making.
questionnaire"withaguidedmulti-rounddialoguemechanismto
Despiterecentadvances,manyLLM-basedfinancialsystemsstill
comprehensiveuserprofile.Thisprofile,whichencapsulatesthe
struggle with behavioral uncertainty, limited transparency, and
user’sfinancialstatus,long-termgoals,andrisktolerance,serves
highdeploymentcosts.WhileLLM-Advisorincorporatesreal-time
asafoundationalinputrequiredbytheotherspecializedmodules
dataandBloombergGPT scaleswellfordomaincoverage,suchsys-
withintheWealth-Voyagerframeworktodeliverpersonalized
temsoftenoperateassingle-passgeneratorswithoutintrospection
analysisandadvice.
oradaptivefeedback.Wealth-Voyagerintroducesacost-efficient,
NewsCrawleroperatesasadedicatedModelContextProto-
dialogue-centricinterfacegroundedinbehavioralfinance,where
col(MCP) [22] server responsible for the real-time aggregation
abelief–desire–intention(BDI)frameworksupportsexplainable,
andprocessingofmarketinformationfromawidearrayofon-
bias-awarerecommendations.Bysimulatingadvisor–clientinterac-
linesources.Thismoduleservestwocriticalfunctionswithinthe
tions,thesystemuncoverscognitivebiasesandpromotesreflective
Wealth-Voyagerframework.Firstly,itperiodicallyextractsex-
decisionsthroughtransparentstrategyrationales.
pectedreturnforecastsformajorassetclassesfromresearchreports
publishedbyprofessionalfinancialinstitutions.Thisdataprovides
theAlphaForgemodulewithrealisticandtimelyinputs,signif-
icantlyenhancingthepracticalapplicabilityandaccuracyofthe
2.3 TraditionalandBehaviour-Aware
portfoliooptimizationalgorithms.Secondly,NewsCrawlercurates
ApproachestoPortfolioOptimization
andretrievesdailymarketnewstailoredtoeachuser’sspecific
Traditionalportfoliooptimizationtechniques,suchasmean–variance profile,includingtheirstatedinvestmentinterests,risktolerance,
analysis and Conditional Value at Risk (CVaR), remain founda- andexistingportfoliocomposition.Thispersonalizednewsfeed
tional to financial planning [9]. Monte Carlo simulation (MCS) servesasthefoundationalcontextfortherole-playingdialogues
has further enabled probabilistic outcome estimation, although withintheDualAdvisormodule.
earlyimplementationsaregenerallyofflineandsingle-pass.MCS- AlphaForgeisthequantitativecoreofWealth-Voyagerwhich
Interactive[3]introducesconversationalsimulation,whileoursys- isbasedonmordenportfoliotheory.Drawingonmarketexpec-
tem(seeAppendixA.3)advancesthislinebysupportingcustom tations(returns,volatilities,andcross-assetcorrelations)continu-
assetuniversesanduser-definedriskthresholds,coupledwithan ouslyharvestedbyNewsCrawlerandtheinvestor-specificcon-
LLM-drivenre-samplingloopforadaptiveportfoliogeneration. straintsproducedbyAssistHub,itconstructsalong-termstrategic
Beyond numerical optimization, behavior-aware systems in- asset-allocationthatbalancesgrowth,risk,andliquidity.Internally,
corporate cognitive biases—such as loss aversion and overcon- AlphaForge employs a constrained mean–variance engine aug-
fidence—thatinfluence real-worldinvestordecisions. Cognitive- mentedwithliquiditycaps,draw-downlimits,andleveragecon-
AwareAdvisors[6,8]demonstratethatembeddingbehavioralpro- trols.Thesolveroutputstargetweightsalongsideforward-looking
filingimprovestrustandengagement.Ourapproachadoptsanine- metrics—projectedreturn,volatility,Value-at-Risk,andliquidity
dimensionalbiasvector(seeAppendixA.2)toguideLLM-based coverage—that feed downstream advisory logic. The full math-
advisorydialogue,aligningwithfindingsfromTrust-AwareGAI ematical specification and optimization routine are provided in
Advisors[26]onpersonalized,trust-sensitiveinteraction. AppendixA.3
158

GAIB2025,August04–06,2025,Hongkong,China Huangetal.
Figure1:ThearchitectureoftheproposedWealth-Voyagerframework.
DualAdvisormoduleutilizesanovelrole-playingframework • AdvisorAgent:Actsastherationalanchor.Itinterprets
poweredbytwodistinctlargelanguagemodel(LLM)agents,which marketdevelopmentswithprofessionalneutralityandproac-
simulateconsultationsbetweenaprofessionalinvestmentadvisor tively detects behavioral biases reflected in the user’s re-
andtheuser.Theprimarypurposeofthismoduleistogenerate sponses.Forexample,itmaycautionagainstoverreactionto
real-time, tactical investment advice. By dynamically modeling newsduetohighpolicysensitivityordiscourageimpulsive
advisor-clientinteractionsinresponsetomarketevents,DualAd- “gain-chasing”behavior.TheAdvisorcontinuouslysteers
visorprovidesactionablerecommendationsthathelpusersmake the dialogue toward strategies consistent with the user’s
timelyportfolioadjustmentstonavigatemarketvolatilityeffec- statedlong-termfinancialgoals.
tively. • UserAgent:Servesasahigh-fidelity"digitaltwin"ofthe
user,designedtoinjectpsychologicallyplausible,andoften
3.3 Role-Playing-BasedAdvisorySimulation biased,humanbehaviorintothesimulation.Itspurposeis
Traditionalfinancialadvisorysystemstypicallyrelyonstaticuser nottobeperfectlyrationalbuttorealisticallymodelhowa
profiles,whichfailtocapturethedynamicinterplaybetweenevolv- specificindividualwouldreacttomarketchangesbasedon
ingmarketconditionsandaninvestor’sreal-timecognitiveand theiruniquefinancialcircumstances,goals,andbehavioral
emotionalresponses[24].Toaddressthislimitation,wepropose tendencies.
DualAdvisor,arole-playingmodulewithinWealth-Voyager,de-
signedtosimulatemulti-turn,psychologicallyinformeddialogue
Eachagentisinstantiatedusingrole-specificsystemprompts.The
UserAgentpromptdynamicallyincorporatesthecompleteuser
betweenaprofessionaladvisorandadigitallymodeledclient.The
profile, including financial goals, risk tolerance, and quantified
objectiveistomovebeyondstaticrecommendationsbygenerat-
behavioralattributes,therebyensuringpsychologicallycoherent
ingadvisoryresponsesthatarebothresponsivetomarketsignals
andcontext-awareresponses.
andadaptivetouser-specificbehavioralbiases.Thisisachieved
Thisdual-agentdesignfulfillstwocomplementaryobjectives.
throughanagent-basedinteractionbetweentwolargelanguage
Firstly,itgeneratespersonalized,bias-awareinvestmentguidance
model(LLM)agents,groundedinabehaviorallyrichuserprofile.
byanticipatorilymodelingtheuser’slikelyemotionalreactions.
3.3.1 AgentRolesandDialogueObjectives. Toeffectivelysimulate Secondly,therecordedconversationactsasa“behavioralmirror”
complexfinancialdecision-making,wedecomposetheadvisory forinvestoreducation,enablinguserstoobservehowprofessional
interaction into two specialized agent roles, inspired by recent reasoningcanmitigatetheirowncognitivedistortions,thereby
developmentsinsocial-agentsimulation[19]. enhancingtheirfinancialself-awarenessovertime.
159

Wealth-Voyager:NavigatingIntelligentWealthManagementwithaMulti-AgentFramework GAIB2025,August04–06,2025,Hongkong,China
3.3.2 BDI-GroundedBehavioralProfile. Toenablerealisticsimu- suggestionsderivedfromtheconsensus,andkeyareasoffocusfor
lation,weconstructacomprehensiveuserprofilethatservesasa thenearfuture.
behavioralfingerprint.Drawingfrombehavioraleconomics,this
profileextendsbeyondconventionaldatabyquantifyingarangeof 4 UserStudy
user-specificbiases.Thesearebroadlycategorizedintoemotional
Toevaluatethepracticaleffectivenessanddecision-supportcapabil-
indicators(e.g.,lossaversion,overconfidence),whichmodelthe
itiesoftheWealth-Voyagersystem,weconductedamonth-long
user’scorefeelingsaboutriskandsecurity,capturingtheaffective
pilot study from April 2 to May 2, 2025. The study involved a
responsesundermarketstressthatoftendriveintuitivedecisions,
mid-careerparticipantfocusedonretirementplanningandaimed
andcognitiveindicators(e.g.,herdingtendency,policysensitiv-
tosimulaterealisticinvestmentscenariosunderlivemarketcon-
ity),whichsimulatehowtheuserprocessesmarketinformationand
ditions. During this period the system was fully deployed in a
formsjudgments,reflectingtheirsystematicpatternsofreasoning.
sandboxenvironment,enablingend-to-endvalidationofitscore
TooperationalizethisbehavioralprofilewithintheUserAgent,
modules—includingbehaviouralprofiling,adaptiverebalancing,
wemodelitsinternaldeliberationusingtheBelief–Desire–Intention
andagent-drivenmarketresponse.
(BDI)framework,awell-establishedparadigmforrationalagency
Importantly,theexperimentcoincidedwithaperiodofelevated
thatmirrorshumanpracticalreasoning.Thisstructuresequentially
geopoliticalandfinancialuncertainty,markedbyasharpescala-
modelstheagent’s:
tioninglobaltradetensions.Thisprovidedanaturalstress-test
• Beliefs(B):Itssubjectiveunderstandingofthecurrentmar- forevaluatinghowWealth-Voyagerrespondstovolatilemarket
ket. events.
• Desires (D): Long-term investment goals and emotional Thestudyfocusonthequantitativeperformance(e.g.returns
inclinationsderivedfromtheuserprofile. andvolatility)ofbothStrategicAssetAllocation(SAA),whichbased
• Intentions(I):Actionablestepsproposedforportfolioad- onlong-terminvestmentgoalsandTacticalAssetAllocation(TAA),
justment. whichbasedonSAAanddynamicallyadjustedaccordingtoshort-
termmarketsignals(suchaspolicychanges,macroeconomicdata),
WeoperationalizeBDIreasoningviaastep-wisepromptingmech-
andqualitativeuserexperienceofferinganintegratedviewofthe
anism:theLLMissequentiallyqueriedforitsbeliefs,desires,and
robustness,adaptability,andusabilityofoursystem.
intentionsinresponsetonewmarketinformation.Thischain-of-
thoughtdesignimprovesboththelogicalconsistencyandinter-
4.1 ParticipantProfile
pretabilityofthesimulateddecisionprocess.
The case involves a 45-year-old professional planning to retire
3.3.3 DialogueFlowandConsensusMechanism. Theagentinter- withineightyears,withtheobjectiveofgrowinginvestableassetsto
actionunfoldsasastructured,multi-turnconsultationdesignedto
supportacomfortablepost-retirementlifestyle.Duringonboarding,
transformauser’spotentialbiasedreactionsintoareasonedaction
theuserreportedsubstantialwealthandmoderateliquidityrequire-
plan.Thedialogueprogressesthroughfourdistinctphases:
mentsbutdidnotspecifykeyparameterssuchasrisktoleranceor
• RationalInitialization:TheAdvisorAgentsynthesizes returnobjectives.Theinitialportfolioallocation(Table1a)includes
dailymarketnewsthroughthelensoftheuser’sprofileto a20%concentrationinrealestateinvestmenttrusts(REITs)—an
formulateascenario-specificinterpretation.Thisinterpreta- unusuallyhighexposureforabalancedportfolio—introducingliq-
tionservesastheinitialprompt,triggeringtheUserAgent’s uidityconstraintsandlimitingdiversification.
BDIreasoningprocess. Onboardinginteractionsrevealedthreeprimaryconcerns:(i)
• BehavioralResponse:TheUserAgentthengeneratesits mitigatinglargedrawdownsnearretirement,(ii)maintainingac-
initialBDIresponse,surfacingtheuser’slikelyfirstreaction, cess to capital within six months for potential obligations, and
completewithanypossiblebiases. (iii)receivingclear,rationale-driveninvestmentguidance.These
• Cognitive Debiasing: The Advisor Agent critiques this concernsinformedthesystem’sevaluationcriteria,emphasizing
response,identifiesirrationalpatternsbasedontheuser’s drawdowncontrol,risk-adjustedperformance,andinterpretability.
profile,andrecommendsalternative,goal-alignedplans. Incontrasttoconventionalsystemsthatprovidestaticrecom-
• IterativeConsensus:Theagentsengageinaniterativedia- mendationsoropaqueoptimizations,Wealth-Voyagerinferred
logue.TheUserAgenteitherrevisesitsintentionsbasedon latentpreferencesandappliedastructured,investment-bank-style
theAdvisor’sfeedbackordefendsitspositiontopromptfur- workflowtorevisetheportfolio.Theresultingallocation(Table1b)
therclarification.Thedialogueterminateswhenaconsensus improveddiversificationandmorecloselyalignedwiththeuser’s
isreached,governedbyapragmaticmechanism:eitherthe implicitriskprofile—demonstratingWealth-Voyager’scapacityto
Advisorgeneratesaspecificagreementphrase(e.g.,"Agree, translatevaguefinancialgoalsintoactionable,personalizedinvest-
nomodificationneeded")orapredefinedmaximumoften mentstrategies.
roundsisreached.
4.2 SystemOperation
Theentireinteractionculminatesinafinal,user-facingdeliver-
able:theDailyInvestmentBriefing.Thisstructuredreportsumma- Toensuretimelyadaptationtomarketshifts,thesystemcontinu-
rizestheessenceofthedialogue,providingtheuserwithaclear ouslyscrapedmacroeconomicnewsandmonitoredreal-timeasset
andactionablesummarythatincludesamarketoverview,theAd- prices.TheAlphaForgefirstlyimplementsStrategicAssetAlloca-
visorAgent’stailoredinterpretation,concreteportfolioadjustment tion(SAA)byoptimizinglong-termweightsunderconstraintssuch
160

GAIB2025,August04–06,2025,Hongkong,China Huangetal.
Table1:Comparisonbetweenuser-declaredbaselineprofileandAI-optimisedallocation.
Attribute User-declared(Apr2,2025) AI-optimised(DualAdvisor)
Initialcapital RMB3,000,000 RMB3,000,000
Targetamount RMB4,500,000+ RMB4,500,000+
Risktolerance N/A Medium(maxloss20%)
Leverageallowed No No
Liquidityneed Medium Medium
Strategicassetmix A-shares30%,Bonds35%, A-shares35.3%,Bonds41.1%,
Gold15%,REITs20% Gold17.6%,REITs6.0%
Expectedreturn N/A 6.53%
Expectedvolatility N/A 9.42%
Notes.“A-shares”areRMB-denominatedequitiesonmainlandChineseexchanges;“Bonds”arefixed-incomesecurities;“Gold”includesphysicalbullionorETFexposure;
“REITs”arereal-estateinvestmenttrusts.N/A=notprovidedatonboarding.
asmaximumdrawdownthresholds.Addtionally,theNewsCrawler anchoring with real-time tactical rebalancing achieves superior
modulegeneratedpersonalisedbriefingsandcontextualinterpre- returnswithoutincreasingriskexposure.
tationstailoredtotheparticipant’sportfolioexposures.Uponde-
tectionofdisruptiveevents—suchasunexpectedpolicyshiftsor
volatilityspikes—theDualAdvisormoduleassessedpotentialport-
folioimpactsandissuedpreemptiverebalancingproposalstohedge
downsideriskwhilepreservingupsidepotentialandalsoemploys
TacticalAssetAllocation(TAA)toadjustpositionsinresponseto
4.4 ComparativeAnalysiswithExistingMarket
real-timemarketeventswiththealgorithmintheAlphaForge.
Solutions
OnApril2,2025,asuddentariffshock(aminor“black-swan”
event)wasdetected.Tacticaladjustmentswereexecutedpriorto RecentindustryanalyseshighlightthegrowingadoptionofAI-
significantmarketdrawdowns.Theseincludedareductioninequity drivenwealth-managementsystemsinChina,notably:AntGroup’s
holdings,increasedexposuretogoldandgovernmentbonds,anda AntFortune [2],JDDigits’JDXiaobei [15],andPingAn’sIntel-
moderateuptickinREITallocation.Thisrepositioningenabledthe ligentWealthButler [23].Theseplatformsprovidefoundational
participanttolimitlossesandcapitaliseonshort-termmispricings. investmentguidancethroughrule-basedallocationandbasicuser
profiling.
Incontrast,Wealth-Voyagerwasco-developedwithagroupof
4.3 PerformanceAcrossPortfolioStrategies
noviceandintermediateinvestorswhouseditalongsideexisting
Figure2comparessegment-levelreturnsofpassiveandtacticalport- marketsolutionsoverasix-weekperiod.Feedbackfromthisreal-
foliosfromApril2toMay9,2025.Followingatariff-inducedshock worlddeploymentinformedthedesignofkeydifferentiators:real-
(Apr02–Apr09),thetacticalapproachreducedlosses(−2.56%vs. timeadaptiverecommendations,personalizedbehavioralmodeling,
−2.79%).Inthereboundphase(Apr09–Apr23),itcapturedgreater andconversationalexplanationmechanisms.
upside(3.24%vs.2.16%).Acrosssubsequentintervals,tacticalre- Wealth-Voyagernotonlysupportsstandardinvestmentadvi-
turnsremainedconsistentlyhigher,notablyduringApr30–May07 soryfunctionsbutalsointroducesnoveldimensionsthatenhance
(1.15%vs.0.68%).Evenduringmildpullbacks(May07–May09),the theuserexperience.AsshowninTable3,oursystemoutperforms
tacticalstrategylimiteddownsidemoreeffectively. existingofferingsinareassuchasdynamicresponsiveness,person-
TheseresultsunderscoretheadvantageoflayeringTacticalAsset alizationdepth,andeducationalengagement—featuresthatusers
Allocation(TAA)atopaStrategicAssetAllocation(SAA)frame- highlightedascriticalforbuildinglong-termfinancialliteracyand
work,enhancingresponsivenesswithoutsacrificingstability. confidence.
Table2comparestheperformanceofthreeportfoliostrategies: The comparison reveals that while current mainstream plat-
theuser-declaredbaseline(Original),abehaviorallyAnchoredport- formsfulfillbaselineadvisoryrequirements,theyremainlimited
folio,andadynamicallyrebalancedTacticalstrategy.Anchoring intheirresponsivenessandpersonalizationdepth.Usersreported
aloneyieldssubstantialgains,increasingtheannualreturnfrom thatWealth-Voyager’sabilitytoexplaininvestmentlogicinplain
3.72% to 6.53% while nearly halving annualised volatility (from languageandadapttotheirevolvingpreferencessignificantlyim-
18.08%to9.42%). provedtheirengagementandunderstandingofportfoliomanage-
Buildingonthisfoundation,theTacticalstrategydeliversfur- ment.
therimprovements.Overtheevaluationperiod,cumulativereturn Wealth-Voyageradvancestheparadigmbyenablingadaptive
risesfrom0.24%to1.86%,withannualvolatilityreducedto12.10%, intradayassetrebalancing,integratingbehavioralfinancesignals,
outperformingbothbaselineandAnchoredstrategiesonarisk- andprovidinginterpretablerecommendationsviadialogue-based
adjustedbasis. interfaces.Theseenhancementscollectivelypositionitasamore
Theseresultsvalidatetheeffectivenessof WealthVoyager’s transparentandresponsiveco-advisoracrossdiverseinvestorseg-
layereddecisionarchitecture:theintegrationofstrategicbehavioral ments.
161

Wealth-Voyager:NavigatingIntelligentWealthManagementwithaMulti-AgentFramework GAIB2025,August04–06,2025,Hongkong,China
Figure2:Segment-levelreturnsforpassiveandtacticalportfolios(April2–May9,2025).
Table2:Performancecomparisonacrossuser-declared,anchored,andtacticalportfoliostrategies.
|           | (a)Originalvs.Anchored |              |               |           | (b)Anchoredvs.Tactical |            |               |
| --------- | ---------------------- | ------------ | ------------- | --------- | ---------------------- | ---------- | ------------- |
| Portfolio |                        | AnnualReturn | Annual        | Portfolio |                        | Cumulative | Annual        |
|           |                        | (%)          | Volatility(%) |           |                        | Return(%)  | Volatility(%) |
| Original  |                        | 3.72         | 18.08         | Anchored  |                        | 0.24       | 13.70         |
| Anchored  |                        | 6.53         | 9.42          | Tactical  |                        | 1.86       | 12.10         |
Notes.Original:user-declaredallocation;Anchored:allocationanchoredbybehavioralsignalsviaDualAdvisor;Tactical:adaptivelyrebalancedbasedonlive
marketsignals.
Annualreturn=projectedyearlygain;cumulativereturn=totalreturnovertheobservedperiod;annualvolatility=yearlyreturndispersion.
Table3:CapabilitycomparisonbetweenWealth-Voyagerandrepresentativemarketofferings.✓=supported;✗=absent.
|     | Feature                       |     | AntFortune | JDXiaobei PingAnButler |     | Wealth-Voyager |     |
| --- | ----------------------------- | --- | ---------- | ---------------------- | --- | -------------- | --- |
|     | Diverseasset-classsupport     |     | ✓          | ✓                      | ✓   | ✓              |     |
|     | Interactiveinterface          |     | ✓          | ✓                      | ✓   | ✓              |     |
|     | Real-timedynamicadjustment    |     | ✗          | ✗                      | ✗   | ✓              |     |
|     | Personalizedcustomization     |     | ✗          | ✗                      | ✗   | ✓              |     |
|     | Financialeducationintegration |     | ✗          | ✗                      | ✗   | ✓              |     |
5 Conclusion usertrustandself-awarenessbyexposingcognitivebiasesinan
explainabledialogue.
Inthispaper,weintroducedWealth-Voyager,anovelmulti-agent
frameworkthatunifiesbehaviouralprofiling,real-timemarketin- Ourvalidation,whilepromising,hasseverallimitations:thepro-
telligence,andquantitativeoptimizationintoacohesivepipeline. totypewasevaluatedonasingleuserandalimitedassetuniverse,
anditsperformanceiscontingentontheunderlyingLLM.Toad-
Throughthecoordinationoffourspecializedmodules—AssistHub,
dressthesegapsandstrengthentherobustnessofourfindings,our
NewsCrawler,AlphaForge,andDualAdvisor—oursystemdeliv-
futureworkwillprioritizeamulti-facetedevaluation.Weplanto
ersinteractivedecisionsupportthatmovesbeyondpassiverecom-
mendations.Thiswasevidencedbyourproof-of-conceptdeploy- conductlarger,longitudinalstudieswithadiversecohortofusers
ment,wherethesystem’sadaptiveadviceoutperformedapassive tostatisticallyvalidatethesystem’sadaptabilityacrossdifferent
|     |     |     |     | behavioral profiles. | Furthermore, | we will expand | the asset uni- |
| --- | --- | --- | --- | -------------------- | ------------ | -------------- | -------------- |
baselineby+1.62ppduringaperiodofelevatedmacrouncertainty,
verse,testtheframeworkundervariedmarketregimestoassessits
anditsstrategicallocationsimprovedtheuser’srisk-returntrade-
resilience,andperformsystematicbenchmarkingagainststate-of-
off(+2.81ppannualizedreturn,−8.66ppvolatility).Qualitative
feedbackalsoindicatedthatthedual-agentsimulationenhances the-artsystemstohighlighttheadvantagesofourbehavior-aware
162

| GAIB2025,August04–06,2025,Hongkong,China |     |     |     |     |     |     |     |     |     | Huangetal. |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- |
approach.Beyondtheseevaluations,wealsoaimtoenhancethe [17] AlexLeatherwoodandVicMatta.2025.BuildingAIApplicationswithDify.ai:
coremethodologybyexploringreinforcementlearningtorefine AHands-OnWorkshop.(2025).
thenegotiationdynamicswithinDualAdvisorandinvestigating [18] JinhoLee,RaehyunKim,Seok-WonYi,andJaewooKang.2020.MAPS:Multi-
agentreinforcementlearning-basedportfoliomanagementsystem.arXivpreprint
domain-specificmodelstoimproveperformanceandreduceinfer- arXiv:2007.05402(2020).
|     |     |     |     |     | [19] Guohao | Li, Hasan | Hammoud, Hani | Itani, Dmitrii | Khizbullin, | and Bernard |
| --- | --- | --- | --- | --- | ----------- | --------- | ------------- | -------------- | ----------- | ----------- |
encecosts.
Ghanem.2023.Camel:Communicativeagentsfor"mind"explorationoflarge
Bybridgingthegapbetweenbehaviouralfinance,quantitative languagemodelsociety.AdvancesinNeuralInformationProcessingSystems36
analysis,andgenerativeAI,Wealth-Voyagerchartsaviablepath (2023),51991–52008.
towardthenextgenerationoffinancialco-pilots.Webelievethis [20] ZhenglongLi,VincentTam,andKwanLYeung.2024.Developingamulti-agent
andself-adaptiveframeworkwithdeepreinforcementlearningfordynamic
| work represents | a significant | step toward | more effective, | trans- |     |     |     |     |     |     |
| --------------- | ------------- | ----------- | --------------- | ------ | --- | --- | --- | --- | --- | --- |
portfolioriskmanagement.arXivpreprintarXiv:2402.00515(2024).
[21] Xiao-YangLiu,GuoxuanWang,HongyangYang,andDaochenZha.2023.FinGPT:
parent,andtrustworthyhuman-AIcollaborationinthecomplex
DemocratizingInternet-ScaleDataforFinancialLargeLanguageModels.arXiv
domainofwealthmanagement.
preprintarXiv:2307.10485(2023).
|     |     |     |     |     | [22] ModelContextProtocolInitiative.2024.              |     |     | IntroductiontotheModelContext |                      |     |
| --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | ----------------------------- | -------------------- | --- |
|     |     |     |     |     | Protocol.https://modelcontextprotocol.io/introduction. |     |     |                               | Accessed:2025-07-11. |     |
Acknowledgments [23] PingAnGroup.n.d..IntelligentWealthButler-PingAnGroup.https://group.
|     |     |     |     |     | pingan.com/. | Accessed:2025-07-11. |     |     |     |     |
| --- | --- | --- | --- | --- | ------------ | -------------------- | --- | --- | --- | --- |
Wegratefullyacknowledgethegenerousfinancialandcomputa-
|     |     |     |     |     | [24] MichaelPompian.2016. |     | Riskprofilingthroughabehavioralfinancelens. |     |     | CFA |
| --- | --- | --- | --- | --- | ------------------------- | --- | ------------------------------------------- | --- | --- | --- |
tionalsupportfromProf.ZhaoandtheBlockchainandIntelligent InstituteResearchFoundation.
|     |     |     |     |     | [25] Statista | Research | Department. 2023. | Global | wealth-management | market |
| --- | --- | --- | --- | --- | ------------- | -------- | ----------------- | ------ | ----------------- | ------ |
TechnologyResearchCenter(CBIT).Wealsoextendoursincere size, 2019–2023. https://www.statista.com/statistics/1266189/global-wealth-
thankstoourindustrymentor,Dr.XiaoyuWu(formerlyofBlack- management-market-size/. Accessed:2025-07-07.
Rock),forherinvaluableinsightsthatshapedthisresearch,and [26] TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,
andIadhOunis.2025.AreGenerativeAIAgentsEffectivePersonalizedFinancial
toAmosChenandWarrenLiofGoogleCloudfortheirhelpful
|     |     |     |     |     | Advisors?.InProc.SIGIR2025. |     | arXiv:2504.05862. |     |     |     |
| --- | --- | --- | --- | --- | --------------------------- | --- | ----------------- | --- | --- | --- |
feedbackonanearlydemonstrationofourwork. [27] ShijieWu,CaolanSlack,BryanKelly,OzanIrsoy,andetal.2023.BloombergGPT:
ALargeLanguageModelforFinance.arXivpreprintarXiv:2303.17564(2023).
|     |     |     |     |     | [28] YijiaXiao,EdwardSun,DiLuo,andWeiWang.2024. |     |     |     | TradingAgents:Multi- |     |
| --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | -------------------- | --- |
References AgentsLLMFinancialTradingFramework.arXivpreprintarXiv:2412.20138(2024).
[29] YangyangYu,ZhiyuanYao,HaohangLi,ZhiyangDeng,YuechenJiang,Yupeng
[1] JoshAchiam,StevenAdler,SandhiniAgarwal,LamaAhmad,IlgeAkkaya,Floren- Cao,ZhiChen,JordanSuchow,ZhenyuCui,RongLiu,etal.2024. Fincon:A
ciaLeoniAleman,DiogoAlmeida,JankoAltenschmidt,SamAltman,Shyamal synthesizedllmmulti-agentsystemwithconceptualverbalreinforcementfor
Anadkat,etal.2023. Gpt-4technicalreport. arXivpreprintarXiv:2303.08774 enhancedfinancialdecisionmaking.AdvancesinNeuralInformationProcessing
| (2023).                                                            |     |     |     |     | Systems37(2024),137010–137045. |     |     |     |     |     |
| ------------------------------------------------------------------ | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |
| [2] AntGroup.n.d..AntFortune-AntGroup.https://www.antfortune.com/. |     |     |     | Ac- |                                |     |     |     |     |     |
cessed:2025-07-11.
| [3] KousikBarnwal.2023. | UserFriendlyPortfolioOptimisationUsingMonteCarlo            |     |     |     | A Appendix |     |     |     |     |     |
| ----------------------- | ----------------------------------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
| Simulation.             | https://medium.com/@indubarnwal752/user-friendly-portfolio- |     |     |     |            |     |     |     |     |     |
optimization-using-mcs-5154ff52dc14 A.1 Monte-Carlo–DrivenMeta-Agent
| [4] Z.Bodie.1995.Investments.(1995). |     | Book. |     |     |     |     |     |     |     |     |
| ------------------------------------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
[5] GaryP.Brinson,L.RandolphHood,andGilbertL.Beebower.1986.Determinants
| ofPortfolioPerformance.FinancialAnalystsJournal42,4(1986),39–44. |     |     |     | http: |     |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
//www.jstor.org/stable/4478947
[6] AbhijeetChandra,ArnavKumar,andShaBala.2025. CognitiveBiasesand Algorithm1InvestmentAdvisorLoop(simplified)
| Robo-AdvisoryAdoption:ExperimentalEvidence. |     |     | JournalofBehavioraland |     |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
ExperimentalFinance37(2025),100742.doi:10.1016/j.jbef.2024.100742 Require: Userconfig𝑐0 ,successthreshold𝜏,maxrounds𝑅
[7] XuDong,ThanosStratopoulos,andChristinaWang.2024. LargeLanguage 1: 𝑐 ←𝑐0 ; 𝑏𝑒𝑠𝑡 ←𝑐0 ; 𝑏𝑒𝑠𝑡 ←0
M o d e ls fo r Fi n a n c i a l a n d I n v e s t m e n t M a n a g e m en t. 𝑐 𝑝
|               |                               |                            | T h e J o urnalofPortfolio |     | for𝑟 | ←1to𝑅do |     |     |     |     |
| ------------- | ----------------------------- | -------------------------- | -------------------------- | --- | ---- | ------- | --- | --- | --- | --- |
| Ma n a g em e | nt 5 1 , 2 ( 2 0 2 4 ), 2 1 1 | – 2 3 0 . d o i:1 0 .3 9 0 | 5 /j pm .2 02 4. 1 .3 5 0  |     | 2:   |         |     |     |     |     |
←MonteCarloSim(𝑐)
| [8] KimSandyEichlerandElizabethSchwab.2024. |                                 |                             | EvaluatingRobo-Advisors       |                        | 3: 𝑝   |       |        |     |     |     |
| ------------------------------------------- | ------------------------------- | --------------------------- | ----------------------------- | ---------------------- | ------ | ----- | ------ | --- | --- | --- |
| t h r o u g h B                             | e h a v i o r a l F i n an ce : | A C r i ti c a l R e v      | ie w o f T e c h n o lo g y P | o t e n ti a l, R a -  |        |       |        |     |     |     |
|                                             |                                 |                             |                               |                        | 4: if𝑝 | >𝑏𝑒𝑠𝑡 | 𝑝 then |     |     |     |
| ti o n a l it y, a                          | n d I n v e s t o r E x pe ct   | a tio n s . F r o n ti e rs | i nB e ha v i o r al E c o no | m i c s 3 ( 2 02 4 ) , |        |       |        |     |     |     |
1489159.doi:10.3389/frbhe.2024.1489159 5: 𝑏𝑒𝑠𝑡 𝑐 ←𝑐; 𝑏𝑒𝑠𝑡 𝑝 ←𝑝
| [9] Financial      | Edge Training. 2024. | Portfolio                                         | Optimisation Explained: | Mean– | 6: endif |         |     |     |     |     |
| ------------------ | -------------------- | ------------------------------------------------- | ----------------------- | ----- | -------- | ------- | --- | --- | --- | --- |
| V a r i an c e , C | V a R a n d Beyond.  | https://www.fe.training/free-resources/portfolio- |                         |       | if𝑝      | ≥𝜏 then |     |     |     |     |
| o p ti m i s a ti  | o n -g u id e /      |                                                   |                         |       | 7:       |         |     |     |     |     |
break
| [10] TaianGuo,HaiyangShen,JinshengHuang,ZhengyangMao,JunyuLuo,Zhuoru |     |     |     |     | 8:  |     |     |     |     |     |
| -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Chen,XuhuiLiu,BingyuXia,LuchenLiu,YunMa,etal.2025.MASS:Multi-Agent
9: endif
S i m u l a tionScalingforPortfolioConstruction.arXivpreprintarXiv:2505.10278
10: 𝑐 ←LLM_Adjust(cid:0)𝑐,allowed_params(cid:1)
( 2 0 2 5 ) .
| [11] ZhenhanHuangandFumihideTanaka.2022.MSPM:Amodularizedandscal- |     |     |     |     | 11: endfor |     |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
a b le m u lti - a g e n t re i n fo r c e m e n t l e a r n i n g - b a sedsystemforfinancialportfolio return(𝑏𝑒𝑠𝑡 ,𝑏𝑒𝑠𝑡 𝑝)
| m a na ge m e | n t . 1 7 , 2 (2 | 0 2 2 ) , e 0 2 6 3 6 8 9 . |     |     | 12: | 𝑐   |     |     |     |     |
| ------------- | ---------------- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
P l os o n e
[12] RogerG.IbbotsonandPaulD.Kaplan.2000.DoesAssetAllocationPolicyExplain
40,90,or100PercentofPerformance?FinancialAnalystsJournal56,1(2000),
26–33. http://www.jstor.org/stable/4480220
| [13] CFAInstitute.2022. | EnhancingInvestors’Trust:2022CFAInstituteInvestor                   |     |     |     |     |     |     |     |     |     |
| ----------------------- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TrustStudy.             | https://www.cfainstitute.org/sites/default/files/-/media/documents/ |     |     |     |     |     |     |     |     |     |
FunctionDescriptionsforAlgorithm1(InvestmentAdvisorLoop):
article/Enhancing-Investors-Trust-Report_2022_Online.pdf
[14] InternationalMonetaryInstitute.2024. ChinaWealthManagementCompe- • MonteCarloSim(𝑐):runsaMonteCarlorolloutunderconfigu-
| tency Evaluation | Report (2023). | https://www.imi.ruc.edu.cn/docs/2024-06/ |     |     |     |     |     |     |     |     |
| ---------------- | -------------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ration𝑐andreturnsthesuccessprobabilityestimate.
cad95d7db7774df4a82a04bb5c212e8f.pdf.
[15] JDDigits.n.d..JDXiaobei-JDDigits.https://jr.jd.com/. Accessed:2025-07-11. LLM_Adjust(𝑐,allowed_params):interactswithanLLM-based
•
[16] KausikLakkaraju,SaiK.R.Vuruma,VishalPallagani,BharathMuppasani,and dialogueagenttoproposeadjustmentstothecurrentusercon-
BiplavSrivastava.2023.CanLLMsBeGoodFinancialAdvisors?AnInitialStudy
inPersonalFinanceDecisionMaking.InProc.ICAPSFinPlanWorkshop.1–6. figuration𝑐,subjecttoawhitelistofallowedparameters.
163

Wealth-Voyager:NavigatingIntelligentWealthManagementwithaMulti-AgentFramework GAIB2025,August04–06,2025,Hongkong,China
Algorithm2ConstructionofBehaviourVector • DecisionDelay:Thisisabehaviorwhereinvestorsareslowto
Require: ConversationID𝑖𝑑;defaultmappingM(Table4) makedecisionsduetodiscomfortwithuncertaintyorputting
1: 𝐻 ←LoadDialogueHistory(𝑖𝑑) offdecisionsuntiltheyreceiveprofessionaladvice.
2: ifContainsStructuredBlock(𝐻)then
3: 𝐸←ParseStructuredBlock(𝐻) Table4:DefaultPersonalityMappingM
4: else
5: 𝐸←LLM_ProfileExtract(𝐻)
6: endif Purpose Vectorslice(loss_aversion,...,decision_delay)
7: if𝐸incompletethen retirement [0.8,0.5,0.8,0.5,0.4,0.8,0.3,0.2,0.6]
8: 𝐸←FillDefaults(𝐸) child_education [0.7,0.6,0.5,0.5,0.5,0.7,0.4,0.4,0.5]
9: endif house_purchase [0.6,0.7,0.4,0.5,0.6,0.6,0.3,0.3,0.7]
10: 𝑝 ←𝐸.investment_purpose⊲retirement/education/house/ wealth_growth [0.3,0.8,0.6,0.5,0.7,0.3,0.8,0.7,0.3]
growth
11: v←M[𝑝]
12: v[4] ←𝐸.real_time_emotion
13: returnDict(keys,v) A.3 Constraint-AwarePortfolioOptimiser
Algorithm3Multi-StageOptimizationProcedure
A.2 Large-Model–AssistedBehaviourProfiling
Require: Meanreturns𝜇,covarianceΣ,userconfig𝜅
FunctionDescriptionsforAlgorithm2(BehaviourVectorConstruc- 1: Infertargetreturn𝑟★,vollimit𝜎max ,CVaRlimit
tion):
2: Deriveliquiditytiers,leverageflagandrestrictedsetR
• LoadDialogueHistory(𝑖𝑑):retrievestheentireconversation 3: Buildboxbounds𝑏 𝑖 forallassets
historyforagivenconversationID. 4: 𝑤(0) ←ERC_Init(Σ)
• ContainsStructuredBlock(𝐻):checksifawell-formed,machine- 5: 𝑤 MS←closed-formmax-Sharpesolution
readableblockispresentinthedialogue. 6: if𝑤 MS feasibleandmeetsallriskcapsthen
• ParseStructuredBlock(𝐻):parsesastructuredblocktodi- 7: return𝑤 MS
rectlyextractuserprofileattributes. 8: endif
• LLM_ProfileExtract(𝐻):usesalanguagemodeltoinferuser ⊲—Stage1:smoothlocalsearch—
attributes from free-form dialogue if no structured block is 9: L(𝑤)←−Sharpe(𝑤)+𝜆IlliqPenalty(𝑤)
found.
10:
𝑤★←SLSQP(cid:0)L,𝑤(0),𝑏
𝑖
,constraints(cid:1)
• FillDefaults(𝐸):fillsmissingentriesintheextractedprofile 11: ifsuccessthen
vector𝐸usingpredefineddefaultvalues.
12:
returnPostProcess(𝑤★)
13: endif
BehavioralMetricDescriptions:
⊲—Stage2:globalrepair—
• LossAversion:Thisisanemotionalbiaswhereinvestorstend 14: 𝑤⋄ ←DifferentialEvolution(cid:0)L,𝑏 𝑖 ,constraints(cid:1)
tofeelthepainoflossesmorethanthepleasureofgains.
15: ifsuccessthen
• News&PolicySensitivity:Thismetricgaugeshowmuch 16: returnPostProcess(𝑤⋄)
aninvestor’sdecisionsareirrationallyswayedbyimmediate
17: else
mediaheadlinesandpolicychanges.
18: returnFailReport()
• Investment Experience: An investor’s behavior is uncon- 19: endif
sciously influenced by past experiences, which can provide
moreaccurateinsightintotheirriskprofile.
• Real-TimeEmotion:Thisreferstoreasoninginfluencedby
feelings,whichcanoverpowerlogicalthinkingduringtimesof FunctionDescriptionsforAlgorithm3(Multi-StageOptimization):
stressandaffectinvestmentdecisions. • ERC_Init(Σ):returnsanequalriskcontributionportfolioini-
• HerdingTendency:Thisisabehaviorwhereinvestorsdonot tializationgiventhecovariancematrixΣ.
havetheirownideasandinsteadfollowtheleadoftheirfriends • SLSQP(L,𝑤(0),𝑏 𝑖 ,constraints):appliesSequentialLeastSquares
andcolleaguesinmakinginvestmentdecisions. QuadraticProgrammingtolocallyoptimizetheobjective L
• RegretAversion:Thisisanemotionalbiaswhereinvestors startingfrom𝑤(0).
avoidtakingdecisiveactionsbecausetheyfearthattheirchosen • DifferentialEvolution(L,𝑏 𝑖 ,constraints):appliesaglobal
coursewillproveunwiseinhindsight. evolutionarysearchtooptimize L incasethelocalmethod
• Overconfidence:Thisisanemotionalbiasbestdescribedas fails.
unwarrantedfaithinone’sownthoughtsandabilities. • PostProcess(𝑤):normalizesandsanitizesacandidateweight
• Illusion of Control: This is a cognitive bias where people vectorbeforereturningit.
believetheycancontrolorinfluenceinvestmentoutcomeswhen • FailReport(): generates a diagnostic message if no feasible
theyactuallycannot. solutionisfound.
164

GAIB2025,August04–06,2025,Hongkong,China Huangetal.
A.4 IllustrativeCaseStudy:ATacticalResponse B ResearchMethods
Narrative B.1 PartOne
Toillustratethepracticalutilityoftheframework,thisappendix Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi
offersanarrativewalkthroughofafive-stagetacticalresponsetoa malesuada,quaminpulvinarvarius,metusnuncfermentumurna,
simulatedmarketcrisis.Theboxbelowsummarizesthekeyevents, idsollicitudinpurusodiositametenim.Aliquamullamcorpereu
correspondinganalyses,andportfolioadjustmentsmadeateach ipsumvelmollis.Curabiturquisdictumnisl.Phasellusvelsemper
stage. risus,etlaciniadolor.Integerultriciescommodosemnecsemper.
B.2 PartTwo
Etiamcommodofeugiatnislpulvinarpellentesque.Etiamauctor
sodalesligula,nonvariusnibhpulvinarsemper.Suspendissenec
lectusnonipsumconvallisconguehendreritvitaesapien.Donec
atlaoreeteros.Vivamusnonpurusplacerat,scelerisquediameu,
InvestmentStrategyReviewandOutlook
cursusante.Etiamaliquamtortorauctorefficiturmattis.
Phase1:CrisisResponse(Apr2:TariffShock)
News:OnApril2,theU.S.Presidentannounceda"LiberationDay"tariffpolicy, C OnlineResources
triggeringaglobalstockmarketsell-off.
Analysis:Themarketexperiencedasuddendownturn.Foraclientwitha Namidfermentumdui.Suspendissesagittistortoranullamollis,
"retirement"objective,theprimarytaskistostrictlycontrolportfoliodrawdown inpulvinarexpretium.Sedinterdumorciquismetuseuismod,et
andprotecthard-earnedcapital.Wemustadoptdecisivedefensivemeasures
sagittisenimmaximus.Vestibulumgravidamassautfelissuscipit
topreventpanicfromaffectingthelong-termplan.
PortfolioAdjustment: congue.Quisquemattiselitarisusultricescommodovenenatiseget
A-Shares Bonds Gold REITs dui.Etiamsagittiseleifendelementum.
27.9%↓ 26.6%↓ 38.0%↑ 7.5%↑ Naminterdummagnaatlectusdignissim,acdignissimlorem
Phase2:MarketObservation&FinalHedging(Apr8:Pre-Rebound rhoncus.Maecenaseuarcuacnequeplacerataliquam.Nuncpulv-
Signals)
News:OnApril8,"pre-reboundsignals"emergedasthestockmarketsawa inarmassaetmattislacinia.
minorrecoveryandtheCBOEVolatilityIndex(VIX)stabilized.
Analysis:Themarketdeclinehaspaused,butthetruetrendremainsuncertain.
Suchafragilereboundisnotworththerisk.Maintainingcautionandcomplet-
ingthefinaldefensiveadjustmentsarecrucialtoensureweareinthesafest
positionbeforethesituationfullyclears,allowingustoseizetheinitiativelater.
PortfolioAdjustment:
A-Shares Bonds Gold REITs
18.9%↓ 34.3%↑ 41.3%↑ 5.5%↓
Phase3:DecisiveRe-entry(Apr9:TariffSuspension)
News:OnApril9,thesuspensionofsometariffswasannounced,leadingtoa
rapidrecoveryinglobalriskassets.
Analysis:Thisdefinitivepositivenewshasturnedthemarket’sdirection.While
ourpreviousdefensiveposturewassuccessful,wemustnowrespondswiftly.
Toavoidmissingthecoreofthisrally,weneedtoactimmediatelyandreinvest
capitalintotheA-sharemarket,akeyoffensivemoveinour"phasedre-entry"
plan.
PortfolioAdjustment:
A-Shares Bonds Gold REITs
36.0%↑ 24.9%↓ 31.4%↓ 7.3%↑
Phase4:TrendConfirmation&Steadiness(Apr11:ConsumerConfi-
denceDrop)
News:OnApril11,theUniversityofMichiganConsumerSentimentIndexfell
toanear-recordlow,creatingmixedmarketsignals.
Analysis:Negativemacroeconomicnewsservesasareminderthatthemarket’s
foundationisnotyetsolid.Thisconfirmsthewisdomofourearlierdecision
nottogoall-inatonce.Duringsuchperiodsofmixedsignals,thebeststrategy
istoremainpatient,maintainthecurrentallocation,andobservefurtherdevel-
opments.
PortfolioAdjustment:
A-Shares Bonds Gold REITs
36.0%(Hold) 24.9%(Hold) 31.4%(Hold) 7.3%(Hold)
Phase5:CrisisAversion&Normalization(May2:U.S.StocksRecover)
News:OnMay2,U.S.stockserasedall"LiberationDay"losses.
Analysis:Themarketturmoilhassubsided,andyourportfoliohassuccessfully
passedthisstresstest.Our"defensefirst,offenselater"tacticprovedeffective.
Themarket’sfocusnowreturnstofundamentals,andsoourfocusmustshift
fromshort-termresponsesbacktoyoureight-yearretirementobjective.
PortfolioAdjustment:
A-Shares Bonds Gold REITs
36.0%(Hold) 24.9%(Hold) 31.4%(Hold) 7.3%(Hold)
165