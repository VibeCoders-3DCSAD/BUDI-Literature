---
conversion_metadata:
  converted_at: "2026-10-11T15:01:39Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "De Zarzà et al., 2023.pdf"
  source_pdf_sha256: "5bf260262d1f218aa99a2e4e56e752ae8ab48b59788000c78163a06c6fb533e0"
  page_count: 24
  markdown_char_count: 71134
---

Article
Optimized Financial Planning: Integrating Individual and
Cooperative Budgeting Models with LLM Recommendations
I.deZarzà1,2,3,∗ ,J.deCurtò1,2,3 ,GemmaRoig1,4 andCarlosT.Calafate2
1 InformatikundMathematik,GOETHE-UniversityFrankfurtamMain,
60323FrankfurtamMain,Germany;decurto@em.uni-frankfurt.de(J.d.C.);roig@cs.uni-frankfurt.de(G.R.)
2 DepartamentodeInformáticadeSistemasyComputadores,UniversitatPolitècnicadeValència,
46022València,Spain;calafate@disca.upv.es
3 Estudisd’Informàtica,MultimèdiaiTelecomunicació,UniversitatObertadeCatalunya,
08018Barcelona,Spain
4 HESSIANCenterforAI(hessian.AI),64293Darmstadt,Germany
* Correspondence:dezarza@em.uni-frankfurt.de
Abstract:Intoday’scomplexeconomicenvironment,individualsandhouseholdsalikegrapplewith
thechallengeoffinancialplanning.Thispaperintroducesnovelmethodologiesforbothindividual
andcooperative(household)financialbudgeting. Wefirstlyproposeanoptimizationframework
forindividualbudgetallocation,aimingtomaximizesavingsbyefficientlydistributingmonthly
incomeamongvariousexpensecategories.Wethenextendthismodeltohouseholds,whereinthe
complexityofhandlingmultipleincomesandsharedexpensesisaddressed.Thecooperativemodel
prioritizesnotonlymaximizedsavingsbutalsothepreferencesandneedsofeachmember,fostering
aharmoniousfinancialenvironment,whethertheyareshort-termneedsorlong-termaspirations.
Anotableinnovationinourapproachistheintegrationofrecommendationsfromalargelanguage
model (LLM).Given its vasttraining data andpotent inferential capabilities, the LLM provides
initialfeasiblesolutionstoouroptimizationproblems,actingasaguidingbeaconforindividuals
andhouseholdsunfamiliarwiththenuancesoffinancialplanning.Ourpreliminaryresultsindicate
that the LLM-recommended solutions result in budget plans that are both economically sound,
Citation:deZarzà,I.;deCurtò,J.; meaningthattheyareconsistentwithestablishedfinancialmanagementprinciplesandpromote
Roig,G.;Calafate,C.T.;Optimized
fiscalresilienceandstability,andalignedwiththefinancialgoalsandpreferencesoftheconcerned
FinancialPlanning:Integrating
parties.ThisintegrationofAI-drivenrecommendationswitheconometricmodels,asaninstantiation
IndividualandCooperative
ofanextendedcoevolutionary(EC)theory,pavesthewayforanewerainfinancialplanning,making
BudgetingModelswithLLM
itmoreaccessibleandeffectiveforawideraudience,asweproposeanexampleofanewtheoryin
Recommendations.AI2024,5,91–114.
economicswherehumanbehaviorcanbegreatlyinfluencedbyAIagents.
https://doi.org/10.3390/
ai5010006
Keywords:financialplanning;householdfinance;LLMs;budgeting;extendedcoevolutionary
AcademicEditors:AlbertY.S.Lam
andYanhuiGeng
Received:18November2023
Revised:7December2023 1. Introduction
Accepted:18December2023 Financial planning [1,2] is an indispensable part of modern life. Whether it is an
Published:25December2023 individualplanningtheirmonthlyexpensesorafamilyjugglingwithcombinedfinances,
effective budgeting is crucial for achieving long-term financial security and prosperity.
However, with the proliferation of expenses and the intricate nature of contemporary
economicsystems,theendeavoroffinancialplanningoftenfeelsoverwhelmingtomany.
Copyright: © 2023 by the authors.
Traditionalmethods,whilesystematic,sometimesfallshortinaccommodatingthedynamic
Licensee MDPI, Basel, Switzerland.
nature of financial needs, and often lack the ability to personalize recommendations to
Thisarticleisanopenaccessarticle
catertoindividualorhousehold-specificpriorities.
distributed under the terms and
conditionsoftheCreativeCommons Wearenowenteringtheageofartificialintelligence(AI)[3],atransformativeforce
Attribution(CCBY)license(https:// thathasalreadyrevolutionizednumeroussectors,fromhealthcaretoentertainment. The
creativecommons.org/licenses/by/ vastinferentialandpredictivecapabilitiesofAI,especiallymodelslikethelargelanguage
4.0/).
AI2024,5,91–114.https://doi.org/10.3390/ai5010006 https://www.mdpi.com/journal/ai

AI2024,5 92
model (LLM) [4], offer a unique advantage in the realm of financial planning. By pro-
cessingvastamountsoffinancialdataandpatterns[5],suchmodelscanprovidetailored
recommendationsthatnotonlyadheretogeneralfinancialbestpractices,whicharewidely
accepted principles or guidelines in financial planning that are considered effective for
managingpersonalfinances,butarealsocongruentwithspecificuserinputs.
Inthispaper,wesetouttobridgethetraditionaleconometricmethodsoffinancial
planningwiththepowerofAI-drivenrecommendations. ByconsideringtheLLM’ssugges-
tionsasafoundation,werefineandoptimizebudgetallocationsforbothindividualsand
households. Ourapproachstrivestoachieveabalancebetweenmathematicaloptimization
andreal-worldpracticality,ensuringthatthesolutionsarenotjusteconomicallysoundbut
alsofeasibleanduser-friendly.
Inpracticalterms,whenartificialneuralnetworks(ANNs),includingDLandLLMs,
are trained through supervised learning, they employ a learning rule that iteratively
converges toward an equilibrium, finely balancing the dilemma of underfitting versus
overfitting.Despitetheirabilitytodiscernnonlinearcontinuoustransformations,theiroper-
ationalmechanicsdonotinherentlyencapsulateaninternalrepresentationofthenonlinear
relationshipsbetweentrainingexemplars[6]. Theconsequenceofthislimitationistwofold:
firstly,whenANNsprocessdatawithinter-relationsconfinedwithinEuclideanboundaries,
theyexcel;secondly,whenconfrontedwithdataexistingbeyondtheseconfines,theresults
maynotonlybesuboptimalbutalsounpredictablyaberrant. Thislimitationissimilar,in
manyrespects,totheconstraintsencounteredintraditionalstatisticalregressionmethods.
In the subsequent sections, we will delve into the methodologies that we have de-
velopedforindividualandcooperativefinancialplanning, elucidateontheintegration
ofLLMsinthesemethods,andpresenttheresultsofourpreliminarytests. Throughthis
exploration,wehopetousherinanewparadigminfinancialplanning,onethatismore
accessible, efficient, and in tune with the unique needs of today’s diverse society. That
beingsaid,itisalsonecessarytorecognizethepotentiallimitationsandinherentrisksofAI,
suchaserrorsandhallucinations,andthestrategiesthatcanbeimplementedtomitigate
theseissues,suchasrigorousvalidationprocesses,theconstantmonitoringofAIoutputs,
andtheincorporationoffail-safesandhumanoversight.
Theessenceofthisstudyliesinaddressingacriticalchallenge: thedemocratization
offinancialplanninginalandscaperiddledwithcomplexityandunpredictability. Our
workisdrivenbytheimperativetoequipindividualsandhouseholdswiththetoolsto
navigatetheeconomicmazetowardsustainablefinancialhealth. Theproblemstatementis
twofold—firstly,theneedtosimplifytheintricaciesoffinancialdecisionmakingforthe
non-expertand,secondly,tocreateanadaptivesystemthatisresilienttothevolatilenature
ofeconomicdynamics.
Our motivation is rooted in the recognition that financial security and literacy are
cornerstonesofindividualautonomyandsocietalwell-being. Weproposeaninnovative
solutionthatintersectsthepredictiveacuityofLLMswiththefoundationalconstructsof
econometrics. ThemathematicalcoreofourapproachistooptimizeautilityfunctionU
thatencapsulatesthefinancialhealthofanentity,oftheform:
n
∑
U(I,E) = αlog(S)−β w log(E ) (1)
o o
o=1
where I is income, S is savings, E represents expenses across n categories, w are the
o
personalizedpreferenceweights,andα,βareparameterscalibratingthetrade-offbetween
savingsandexpenditures. Throughthisformulation,weseektocraftasystemthatnot
onlyprovidesbespokefinancialadvicebutalsoevolveswiththeuser’schangingeconomic
scenario,embodyingthefluidityrequiredforreal-worldfinancialplanning.
Theproblemattheheartofourresearchistheincrementalcomplexityofpersonal
financialmanagementinarapidlyevolvingeconomiclandscape. Inanagewherefinancial
instrumentsandmarketsareincreasinglyintricate,theaverageindividualisatasignificant
disadvantagewhenattemptingtoplanforfinancialsecurity. Thischallengeisnotmerely

AI2024,5 93
academic but a pressing real-world issue that affects the quality of life and long-term
well-beingofindividualsandfamilies. Theneedforaccessiblefinancialplanningisfurther
highlighted by the widening gap in financial literacy, which can lead to poor financial
decisionsandincreasedeconomicinequality.
Ourworkismotivatedbytheimperativetorenderfinancialplanningnotonlymore
approachable but also more aligned with the diverse and dynamic financial goals of
individuals. WeaimtoaddressthisbyleveragingthecomputationalprowessofLLMsto
distillcomplexfinancialdataintoactionableinsights. Themathematicalunderpinningof
ourapproachisanoptimizationframework,tailoredtothenuancesofpersonalfinance,
whichcanberepresentedas:
max{U(x) :x∈ F, G(x) ≤0, H(x) =0} (2)
x
Here,xsymbolizesthefinancialdecisionvariables,Uistheutilityfunctionthatquan-
tifiesfinancialhealth,F definesthefeasiblesetbasedonfinancialconstraints,G represents
inequalityconstraints(suchasbudgetlimits),andHcapturesequalityconstraints(suchas
income–expensebalance). Ourmotivationistoimplementasystemthatempowersusers
withpersonalized,intelligentrecommendations,thusequippingthemtomakeinformed
financialchoicesinpursuitofeconomicresilienceandprosperity.
Theremainderofthispaperisstructuredasfollows: Section2providesrelatedwork.
Section3focusesonthematerialsandmethodologyadopted,presentingthefoundational
aspectsandresearchmethodologypertinenttotheoptimizationmodels.InSection4,weex-
plorethesignificanceofLLMsinindividualbudgeting,emphasizingtheirrecommendation-
drivenapproachtofinancialplanning. Section5offersanin-depthlookintocooperative
financialplanningforhouseholds,showcasingthesynergisticviewbetweenLLMrecom-
mendationsandhouseholdmembers’financialpriorities.ThesubsequentSection6presents
theintricaciesofcooperativebudgetingwithinanestablishedextendedcoevolutionary(EC)
framework,elucidatingitsinnovativefacets. Movingforward,Section7describesoursim-
ulationframework,detailinghowLLM-informeddecisionscanbesimulatedandanalyzed,
whilealsohighlightinginSection7.3theimportanceoflong-termplanningdependencies
tofurtherdevelopthesimulatedframework. Finally,inSection8,wedrawourconclusions,
recapitulatingtheprimaryfindingsandlookingaheadatpromisingdirectionsforfuture
workinthisdomain.
2. RelatedWork
Thelandscapeoffinancialplanningandoptimizationhasbeendeeplyenrichedby
theintersectionofcomputationalintelligenceandeconomictheories. Inthissection,we
contextualizeourcontributionswithinthespectrumofexistingliterature,delineatingthe
evolutionoffinancialplanningmethodologiesfromtraditionalmodelstoAI-augmented
frameworks.
Traditionalfinancialplanninghasbeenheavilyinfluencedbyseminalworkssuchas
thoseofMarkowitz[7]onportfoliooptimizationandAndoandModigliani’slife-cycle
hypothesis [8]. The optimization of financial assets has been extensively studied, with
methodsrangingfromlinearprogramming[9]tomoresophisticatedstochasticmodels
[10].
Theinfusionofbehavioraleconomicsintofinancialoptimizationmodelshasprovided
amorethoroughunderstandingofhumanfinancialbehavior,asevidencedbytheworksof
Thalerandothers[11]. Thishasledtomodelsthataccountforirrationaldecisionmaking
andheuristicsusedbyindividuals,addingcomplexitytotheoptimizationproblems[12].
TheadventofAI[13,14]infinancialplanninghasopenednewavenuesforpersonal-
izedandadaptivefinancialadvice. Earlysystemsutilizedrule-basedexpertsystems[15],
whilerecentadvancementshaveleveragedmachinelearningforpredictiveanalyticsin
finance[16].
TheintegrationofLLMs[4]intofinancialplanningisarelativelynewandemerging
field. RecentstudieshavebeguntoexplorethecapabilitiesofmodelslikeOpenAI’sGPT

AI2024,5 94
seriesandexplainableAItechniquesingeneratingfinancialnarratives[17,18]. Ourwork
extendsthislineofresearchbyembeddingLLMinsightsintotheoptimizationframework,
anovelapproachthathasnotbeenextensivelycoveredintheexistingliterature.
Comparative studies have highlighted the strengths and weaknesses of AI-driven
financialtoolscomparedtotraditionalmethods[19–21]. However, thereremainsagap
intheliteratureregardingtheefficacyofLLMrecommendationswithinthecooperative
budgetingcontext,anareaourresearchdirectlyaddresses.
While existing works provide a foundational understanding of the financial opti-
mizationlandscape,thereremainsalacunawhenitcomestotheintegrationofreal-time,
AI-driven,personalizedrecommendationsintothesemodels. Ourresearchfillsthisgap
bynotonlyintegratingbutalsocriticallyexaminingandrefiningtheroleofLLMswithin
financialplanningandoptimizationframeworks.
Insummary,ourresearchbuildsupontherichheritageoffinancialoptimizationwhile
branchingintotherelativelyunchartedterritoryofLLM-augmentedfinancialplanning. By
doingso,weaimtocontributeasignificantadvancementinthedomain,tailoredforthe
dynamiceconomicworldofthe21stcentury.
3. MaterialsandMethodology
Thisresearchproposesanoptimizationmodelforindividualandcooperativefinancial
planning,bothenhancedbytheintegrationoflargelanguagemodel(LLM)recommenda-
tions. Thetwoprimaryfacetsofthisapproachare: (1)foundationalmathematicalmodels
that describe budgeting optimization problems, and (2) computational algorithms that
incorporatetheLLM’srecommendationsintofinancialdecision-makingprocesses.
The objective of maximizing savings by allocating monthly income across various
expense categories is grounded in core principles of theory in household finance. This
approachalignswiththelife-cyclehypothesisofAndoandModigliani(1963)[8],which
positsthatindividualsplantheirconsumptionandsavingsbehaviorovertheirlifetime
toachievefinancialstability. Furthermore, itreflectstheprinciplesofoptimalportfolio
selection from the theory of modern portfolio of Markowitz (1952) [7], adapted to the
contextofhouseholdbudgeting,wheretheportfolioisamixofexpensesandsavings.
Our model also incorporates the behavioral aspects of financial decision making
as discussed by Xiao (2008) [22], acknowledging that individuals have varying prefer-
encesandsubjectiveweightsondifferentexpensecategories. Additionally,Browningand
Lusardi’s(1996)researchonmicrotheoriesandmicrofactsofhouseholdsaving[23]pro-
videsempiricalsupportfortherelevanceofoptimizingsavingsbehavioratthehousehold
level.
Forthecooperativefinancialrecommendationmodel,wedrawontheseindividual
financial behaviors and extend them to a household context, considering the collective
utilitymaximizationandsharedfinancialresponsibilities,resonatingwiththecooperative
gametheoryinhouseholdeconomics[24].
IndividualFinancialRecommendationModel
Objective:Ourprimarygoalistofindthebestallocationofanindividual’smonthlyin-
come across various expense categories while maximizing their potential savings
[7,8,22,23].
Variables:
• I : Monthlyincome.
• E : Expenseforcategoryz(e.g.,rent,groceries,utilitybills,entertainment).
z
• S: Savingsforthemonth.
ObjectiveFunction: Thisfunctionemphasizesmaximizingsavingsaftercoveringall
necessaryexpenses.
∑
MaximizeS = I− E . (3)
z
z

AI2024,5
95
Constraints: Theconstraintsensurenon-negativeexpenses, savings, andthattotal
expensesdonotsurpassthemonthlyincome.
|     | E ≥0∀z, |     | (4) |
| --- | ------- | --- | --- |
z
|     | S ≥0, |     | (5) |
| --- | ----- | --- | --- |
∑
|     | E ≤ I. |     | (6) |
| --- | ------ | --- | --- |
z
z
CooperativeFinancialRecommendationModel(Household)
Objective:
In a household setting, our aim is to optimize combined budget allocation for all
members. Weensurethateachmember’spreferencesandnecessitiesareaccommodated,
aimingforanoverallmaximizationofhouseholdsavings.
Variables:
• I o : Monthlyincomeofmembero.
• E : Expenseforcategoryzbymembero.
zo
• S o : Savingsforthemonthbymembero.
• T : Totalcombinedsavingsofthehousehold.
S
ObjectiveFunction:
Thisfunctionprioritizestheoverallsavingsofthehousehold,giveneachmember’s
incomeandexpenses.
|           | ∑    | ∑      |     |
| --------- | ---- | ------ | --- |
| MaximizeT | = (I | − E ). | (7) |
|           | S o  | zo     |     |
|           | o    | z      |     |
Constraints:
Theconstraintsareextensionsoftheindividualmodelbutfactorinmultiplemembers.
|     | E ≥0∀z,o, |     | (8) |
| --- | --------- | --- | --- |
zo
|     | S ≥0∀o, |     | (9) |
| --- | ------- | --- | --- |
o
∑
|     | E ≤ I ∀o, |     | (10) |
| --- | --------- | --- | ---- |
zo o
z
∑
|     | T = S | .   | (11) |
| --- | ----- | --- | ---- |
|     | S     | o   |      |
o
Preferences/Weights:
Topersonalizethemodel,weintroduceweightsw representingtheimportanceof
zo
anexpensecategoryzformembero. Thisensuresthatindividualpreferencesarenotlost
inthecollectivemodel.
|           | ∑      | ∑      |      |
| --------- | ------ | ------ | ---- |
| MaximizeT | = (I − | w E ). | (12) |
|           | S o    | zo zo  |      |
|           | o      | z      |      |
CollaborativeConstraint:
Factoringinsharedexpenses,suchasrent,canleadtosubstantialsavings. Therefore,
weintroduceacombinedexpenseconstraint.
|                 | ≤        | +E       |      |
| --------------- | -------- | -------- | ---- |
| E rent,combined | E rent,1 | rent,2 . | (13) |
IncorporatingLLMRecommendations
Thetrueinnovationofourapproachliesinblendingtraditionaloptimizationtech-
niques with AI-driven insights [25,26]. The LLM’s vast knowledge base and advanced
languageprocessingcapabilitiescanprovidenuanced,context-awarerecommendationsfor
individualsandhouseholds.
GivenarecommendationR z fromtheLLMforanexpensecategoryz,wecanadjust
ourinitialfinancialallocations.
|     | E z ≈ R z ∀z. |     | (14) |
| --- | ------------- | --- | ---- |

AI2024,5 96
WiththeseLLM-generatedinsightsservingasafoundation,theoptimizationmodel
canbefine-tunedatalaterstagetosuitspecificneeds,balancingmathematicalaccuracy
withreal-worldfinancialinsights.
3.1. ProspectiveValidationFrameworkforAI-DrivenLLMFinancialRecommendations
ThisframeworkcanbedesignedtoupholdtheintegrityandapplicabilityofAI-driven
insights,ensuringthattheyarenotonlyrelevantbutalsoconformtothehigheststandards
offinancialprudence.
Amulti-tieredverificationprocessthatscrutinizestheLLMoutputforreliabilityand
truthfulnesscanbeproposed. Thisprocesswouldinvolve:
• ExpertReview: EachLLM-generatedrecommendationisevaluatedbyfinancialex-
pertstoensurethatitisconsistentwithestablishedeconomicprinciplesandreal-world
conditions. ExpertsmaymodifyLLMsuggestionstocorrectanyinaccuraciesorto
betteralignwithconservativefinancialpractices.
• ContextualAnalysis: ThemodelcontextualizesLLMresponsesbyexaminingthem
againstcurrentfinancialtrends,regulatoryguidelines,andeconomicindicators. This
ensuresthattheadviceisnotonlymathematicallysoundbutalsopractical,taking
intoaccountthesocio-economicenvironmentoftheusers.
• RiskAssessment: Riskanalysisisconductedtoevaluatethepotentialharmthatcould
arisefromfollowingtheLLM’sadvice. Thisincludesstresstestingtherecommenda-
tionsagainstvariouseconomicscenariostogaugetheirresilienceandadaptability.
• Ethical Considerations: An ethical review is performed to ensure that the LLM’s
advicedoesnotinadvertentlyleadtofinancialdecisionsthatcouldbedetrimentalto
theuser’slong-termwell-beingorthatcouldperpetuatebiases.
The objective function within the optimization framework would be then defined
asfollows:
MaximizeU(S,E,C) = f(S)−g(E,C) (15)
whereU(S,E,C)istheutilityfunctiondependentonsavingsS,avectorofexpensesE,and
acontextvectorCthatincludesbotheconomicconditionsanduser-specificcircumstances.
The function f(S) quantifies the utility derived from savings, emphasizing the goal of
maximization,whileg(E,C)isapenaltyfunctionthatincreaseswhenexpensesareeither
economicallyunsoundorpotentiallyharmful.
TointegrateLLMinsightseffectively,aconstraintadaptationstrategycanbeemployed
whereLLMrecommendationsadjusttheboundariesofthefeasiblesolutionspacerather
thandictatingfixedallocations. Thiswouldallowsustomaintainaflexibleyetcontrolled
optimizationenvironmentwhereLLMinputsserveasinformedguidelinesratherthan
rigiddirectives. Theoptimizationproblemwouldthenbecome:
MaximizeU(S,E,C) (16)
subjecttoE ≤E≤E , (17)
min LLM
∑
S+ E≤ I, (18)
S,E≥0, (19)
where E and E are vectors of minimum and LLM-recommended expenses,
min LLM
respectively.
Throughthismeticulousapproach,wecanensurethatthefinancialplanningmethod-
ologies proposed in this study are not only innovative and AI-enhanced but are also
reliable,ethicallyresponsible,andpracticallyapplicableinavarietyoffinancialcontexts.
Thismethodology,withtheproposalofathoroughvalidationmechanism,setsaprecedent
fortheresponsibleintegrationofAIinthesensitiverealmofpersonalfinance.

AI2024,5 97
3.2. RAGApproachwithLLMRecommendations
Additionally,toaddressthepotentialforLLMhallucination,themethodologycould
integrate a retrieval augmented generation (RAG) approach into the recommendation
generationprocess. ThissophisticatedmechanismcanenhancetherobustnessoftheLLM’s
outputsbyanchoringitsresponsesinverifiabledata,therebysignificantlyreducingthe
likelihoodofgeneratingspuriousormisleadingfinancialadvice.
The RAG process can operate by first querying a large-scale dataset of financial
information,regulatoryguidelines,andhistoricaleconomicdata.TheLLMthensynthesizes
thisretrievedinformationwithitspre-trainedknowledgetogeneraterecommendationsthat
arenotonlycontextuallyrichbutalsodata-grounded. HereishowtheRAGmethodology
couldbeincorporated:
• Data Retrieval: Prior to recommendation generation, the LLM queries a curated
datasettoretrieverelevantfinancialdataandhistoricaltrendsthatmirrortheuser’s
querycontext.
• AugmentedGeneration: Themodelcombinesitsownlanguage-understandingcapa-
bilitieswiththeretrieveddatatogenerateadraftrecommendation. Thisstepensures
thateachpieceofadviceisinformedbyempiricaldata,therebyenhancingitsaccuracy
andrelevance.
• Validation and Refinement: The draft recommendation is then passed through a
validationfilter,whichincludesacomparisonagainstup-to-datefinancialmodelsand
acheckforcompliancewithcurrenteconomicconditions.
• ExpertOversight:Thefinalstagecaninvolvehumanoversight,wherefinancialexperts
reviewtheLLM-generatedadvicetoensurethatitadherestoprofessionalstandards
andreflectssoundfinancialjudgment.
TheincorporationofRAGintoourrecommendationgenerationprocesscanbemathe-
maticallyrepresentedintheoptimizationmodelasanadditionalsetofconstraintsthatthe
LLM’sresponsesmustsatisfy:
RAG(E,D) →E (20)
LLM
where RAG(E,D) represents the RAG process with expenses E and retrieved data D,
mappingtotheLLM’srecommendedexpensesE .
LLM
Incorporating the RAG methodology into the LLM framework could significantly
mitigate the risk of hallucinations by ensuring that the model’s recommendations are
continuouslygroundedinempiricalevidence. Itcanalsoprovideanadditionallayerof
confidenceinthemodel’soutputs,reinforcingtheirreliabilityforend-usersseekingsound
financialplanningadvice.
4. LLM-InformedBudgeting
Inthemoderneraofdata-drivensolutions,usinganLLMtoprovidefinancialadvice
offers an innovative approach to household budgeting. Given the intricate nature of
individualspendinghabitsandthemyriadofwaysinwhichfundscanbeallocated,using
thepowerofAIcansignificantlyenhancepersonalizedfinancialrecommendations.
Thevalueadditionofourresearchtothefieldoffinancialplanningliesinthenovel
synthesis of econometric modeling and state-of-the-art AI. By integrating the insights
from LLMs intotraditional financial planning frameworks, we provide amulti-faceted
approachthatalignswiththecontemporarydemandforpersonalizedfinancialadvice.This
integrationheraldsasignificantshiftfromone-size-fits-allfinancialadvisoriestosolutions
thatrespectindividualfinancialnarrativesandtheuniqueeconomiccontextsthatthey
existin.
Ourmodelsoffersignificantimprovementsoverexistingmethodologiesbyincorpo-
ratingbehavioraleconomicfactorsandreal-timedataanalysis,therebydeliveringamore
granularandresponsivefinancialplanningtool.Themathematicalmodelthatencapsulates
ourapproachcanberepresentedas:

AI2024,5 98
max U(x,θ) subjectto x∈ F(Ψ), G(x,Φ) ≤0, H(x,Λ) =0 (21)
x
Here,xdenotesthevectorofdecisionvariablesforfinancialplanning,Uistheutility
function enhanced by LLM insights θ, F represents the feasible region influenced by
externaldataΨ,andG,HarethesetsofconstraintsparameterizedbyΦandΛ,respectively,
signifyingeconomicconditionsanduserpreferences. TheLLM’scapabilitytodigestand
interpret large volumes of data transcends the capabilities of traditional methods, thus
enabling our model to adaptively recalibrate recommendations in accordance with the
fluctuatingeconomicindicatorsandpersonalfinancialgoals.
Moreover, the transformative potential of our methodology becomes particularly
salientwhenconsideringtheadaptabilityofLLMstoachanginginformationlandscape,
a feature that conventional financial planning tools lack. By continually learning from
newdata,ourmodelremainsattheforefrontoffinancialplanninginnovation,marking
a decisive step toward a more intelligent, adaptable, and personalized financial plan-
ningparadigm.
The approach leverages the capabilities of OpenAI’s GPT-4 model to analyze a
user’s financial data and provide a bespoke recommendation based on that data. The
processinvolves:
1. DataInput:Usersprovideabreakdownoftheirmonthlyincomeandprimaryexpenses.
2. LLMAnalysis:Themodelevaluatesthedatainthecontextofsoundfinancialplanning.
3. RecommendationGeneration: TheLLMthenoffersadetailedrecommendationon
howtheusermightbestallocatetheirremainingfunds.
ThePythonscript,get_financial_recommendation,takesastringrepresentationof
theuser’sfinancialdataandattemptstoretrieveorgeneratearecommendation.
Keyfeaturesofthescriptinclude:
• CachingMechanism: Toenhanceefficiency,thescriptmaintainsa
recommendation_cache. Iftheuser’sfinancialdatamatchapreviousentry,astored
recommendationisreturnedwithoutinvokingtheLLM,therebysavingcomputational
resourcesandtime.
• RobustErrorHandling:RecognizingthepotentialforAPIerrorsortimeouts,thescript
employsaretrymechanismwithexponentialbackoff.Thisensuresthattransientissues
donotleadtoimmediatefailuresandoffersaresilientapproach.
• User-Friendly Output: The LLM’s response is parsed to retrieve a clear, concise
recommendationthatisthenreturnedtotheuser.
Here,wedescribeanexampleforclarity. Considerauserwithamonthlyincomeof
USD5000andmajorexpensesthatincludeUSD1200forrent,USD400forgroceries,USD
200forutilities, andUSD100forentertainment. Whentheyinputthesedata, theLLM
couldprovidearecommendationlike:
“Based on your financial data for the month, after accounting for your major
expenses,youhave$2100remaining. Irecommendallocating$500towardsan
emergency fund, $300 towards investments, $200 for miscellaneous expenses,
andsavingtheremaining$1100.”
AdvantagesoftheLLMApproach:
1. Personalization: Unlikegenericfinancialadvice,theLLMapproachtailorsrecommen-
dationstotheindividual’suniquefinancialsituation.
2. Scalability: Theapproachcancatertoavastnumberofuserssimultaneously,making
itsuitableforintegrationintofinancialplanningappsorplatforms.
3. Learning Over Time: As LLMs evolve and receive more training, the quality and
depthoftheirrecommendationscanonlyimprove.
Whilethecurrentimplementationprovidesrobustfinancialrecommendations,future
versionscould:

AI2024,5 99
• Integratereal-timedatasourcestoprovideup-to-the-minuteadvice.
• Considerlonger-termfinancialgoals,suchasbuyingahomeorretirementplanning,
initsrecommendations.
• Incorporateuserfeedbacktocontinuallyrefineandenhancerecommendations.
Inconclusion,usingLLMsforhouseholdfinancialrecommendationsrepresentsasig-
nificantstepforwardinthemarriageofAIandfinancialplanning.Byofferingpersonalized,
scalable,andincreasinglysophisticatedadvice,thisapproachpromisestorevolutionizethe
wayindividualsmanagetheirfinances.
Figure 1 delineates the proposed financial planning methodology that makes use
of the capabilities of LLMs to enhance data analysis and supports the formulation of
robust recommendations. This schematic presents a sequence of interconnected stages
startingwiththeaggregationoffinancialdata,proceedingtoanin-depthanalysisphase,
whichconvergeintotheapplicationofLLMinsightsforthegenerationoftailoredfinancial
recommendations. Theiterativecycleisfundamentalformaintainingtherelevancyand
efficacyofthefinancialplan,adaptingdynamicallytotheevolvingeconomiclandscape
andindividualandcooperativefinancialobjectives.
LLM
Financial
DataAnalysis In- Recommendation
Data
sights
Review&
Monitoring Implementation
IterativeFeedback Adjust
Figure1.FlowchartillustratingthefinancialplanningmethodologywiththeintegrationofLLMs.The
processstartswithdatacollection,followedbyanalysis,integrationofLLMinsights,recommendation,
implementation,anditerativereviewwithmonitoringtoadjusttheplan.
4.1. VerificationMechanismforLLM-GeneratedFinancialAdvice
Inourapproach,wecouldensurethealignmentoftheLLM-generatedrecommenda-
tionswithestablishedfinancialtruthsbyimplementingaverificationmechanismwithin
thePythonscript: get_financial_recommendation. Thismechanismcancross-referencethe
recommendationsagainstacomprehensivefinancialdatabasethatincludesawidearray
ofeconomicindicators,historicalfinancialdata,andregulatorycompliancerequirements.
Here,wedescribetheprocessindetail:
• RecommendationGeneration: ThescriptfirstinvokestheLLMtogenerateaprelimi-
naryfinancialrecommendationbasedontheuser’sinputdata.
• DatabaseCross-Reference: UponobtainingtheLLM’soutput,thescriptautomatically
queriesafinancialdatabase,seekingcorroborationfortheproposedfinancialstrategies.
Thisdatabaseisconsistentlyupdatedtoreflectthelatestfinancialtruths,including
markettrends,taxlaws,andindustrystandards.
• TruthAlignmentCheck: ThescriptcomparestheLLM’srecommendationagainstthe
databaseentriestoverifytheaccuracyandrelevanceoftheadvice. Recommendations
thatsignificantlydivergefromthefinancialtruthsareflaggedforfurtherreview.
• FeedbackLoopforAdjustment: Incaseswherediscrepanciesarise,thescriptadjusts
therecommendationsbyapplyingasetofheuristicrulesderivedfromthefinancial
truths. Thisiterativeprocessensuresthatthefinaladviceprovidedtotheuserisboth
data-drivenandalignedwithfinancialrealities.
• HumanExpertReview: Thelaststepinvolvesafinancialexpertwhoreviewsand,
if necessary, refines the script’s output to ensure full compliance with financial
bestpractices.

AI2024,5 100
Mathematically,thisverificationmechanismcanberepresentedasaconstraintsatis-
factionproblem,wherethegeneratedrecommendationsRmustsatisfyasetofconditions
CbasedonthetruthsTfromthefinancialdatabaseD:
∀r ∈ R,∃t ∈ T :C(r,t) →ValidRecommendation. (22)
Incorporatingthistruth-checkingprotocolcouldenhancethereliabilityofourLLM-
informedbudgetingsystem,ensuringthatusersreceiverecommendationsthatarenotonly
personalizedbutalsopragmaticallysoundandfinanciallyvalid.
4.2. PromptEngineeringforImprovedLLMFinancialRecommendations
ToempowerusersinoptimizingtheirinteractionswiththeLLM,wecanalsointroduce
aguidedpromptoptimizationfeaturewithinourLLM-informedbudgetingsystem. This
enhancementcaneducateusersonconstructingeffectiveprompts,therebyimprovingthe
qualityofthefinancialrecommendationsthattheyreceive. Hereishowwecanincorporate
thisguidanceintotheuserexperience:
• PromptTemplates: Weprovideuserswithacollectionofprompttemplatesthatare
designed based on successful financial inquiry patterns. These templates serve as
startingpointsforuserstoarticulatetheirfinancialdataandquestions.
• PromptFeedbackMechanism: Afteruserssubmittheirprompts,oursystemanalyzes
the prompt structure and provides instant feedback on how to refine it for clearer
communicationandbetter-alignedfinancialrecommendations.
• AdaptiveLearningfromUserInteraction: Asusersinteractwiththesystem,itcan
employMLalgorithmstolearnfromthequalityofrecommendationsgeneratedfrom
past prompts. The system then suggests modifications to the prompts for future
queries,aimingtomaximizetherelevanceandprecisionoftherecommendations.
• InformativeTutorialsandTips: Alongsidedirectfeedback,usershaveaccesstoeduca-
tionalmaterialsthatexplaintheprinciplesofeffectivepromptconstruction,including
clarity,specificity,andtheinclusionofrelevantfinancialcontext.
• ExpertSystemInsights: Abuilt-inexpertsystemanalyzesuserpromptsandcompares
themwithadatabaseofoptimizedpromptsandtheiroutcomes. Byhighlightingkey
differences,thesystemoffersactionableinsightsforuserstoimprovetheirqueries.
Mathematically,thisprocesscanbeviewedasanoptimizationproblemwheretheaim
istomaximizetheutilityUofapromptPwithrespecttothequalityQoftherecommenda-
tionRasfollows:
maxU(P) s.t. Q(R|P)ismaximized. (23)
P
ThefunctionU(P)denotestheutilityoftheprompt,whichisafunctionofitseffec-
tivenessingeneratinghigh-qualityrecommendations Q(R|P). Byiterativelyrefining P
basedonsystemfeedbackandlearning,wecanensureacontinuousimprovementinthe
prompt’sutility.
4.3. ECTheoryforHouseholdFinance: BeyondEuclideanDomains
Theextendedcoevolutionary(EC)theoryprovidesasophisticatedframeworkthat
allows us to navigate beyond the intrinsic limitations of ANNs. While these models
mightstrugglewithcapturingtheintricaciesofnon-Euclideanspacesduetotheirreliance
on linear transformations within a Euclidean framework, EC theory embraces a more
holisticview.
ECtheory,throughitsfoundationalprinciplesofcoadaptationandcoevolution,inher-
entlyaccountsforthecomplexanddynamicinter-relationshipscharacteristicofreal-world
scenarios,whichoftenextendbeyondlinearlydefinablespaces. Thisadaptabilityismade
possiblebyECtheory’scapacitytomodelinteractionswithinamulti-dimensionalspace

AI2024,5 101
thatcaneffectivelyrepresentthehigh-levelabstractionsandnonlinearinterdependencies
offinancialdata.
∆x(t+1) = F(x(t),x(t−1),...,x(0)). (24)
Here, ∆x(t+1) represents the change in the strategy vector at time t+1, and F
encapsulatesanonlinearfunctionofthestrategyvectorsatallprevioustimesteps,capturing
the essence of iterative learning and strategic adaptation over time. This function F is
not restricted to the confines of a Euclidean space, enabling the EC model to explore a
morediversesolutionspaceandofferingarobustmechanismforidentifyingequilibriain
complexsystems.
Furthermore, the EC theory facilitates the integration of external insights, such as
thosederivedfromLLMs,intoitsevolutionaryprocess. ByconsideringtheLLMoutputs
asauxiliarydatapoints,theECmodelcanrefineitsstrategicoutlook,effectivelybridging
thegapbetweenthetraditionaloptimizationtechniquesandthehigh-dimensionalspaceof
AI-drivenrecommendations.
x(t+1) =x(t)+γ(R−x(t))+∆x(t+1). (25)
Intheequationabove,γrepresentstherateofintegrationofLLMrecommendations
denoted by R into the current strategy x(t). The term ∆x(t+1), as previously defined,
ensuresthattheECmodeldynamicallyevolves,reflectingboththeinsightsfromLLMs
andtheiterativelearningprocess.
By leveraging the flexibility and multidimensional approach of EC theory, we can
transcendthetraditionallimitationsposedbyANNs. Thisprogressivemodelingapproach
notonlyalignswiththecomplexnatureoffinancialecosystemsbutalsooffersarobust
platformfordevelopingadvancedfinancialplanningtoolsthatarebothcomprehensive
andcapableofevolvingintandemwiththechangingeconomiclandscape.
5. LLMCooperativeBudgetingandFinancialPlanningforHouseholds
Cooperativebudgetingemergesasanimperativewhenmultipleindividuals,such
as partners or roommates, decide to combine their financial resources and manage ex-
penses collectively. By jointly analyzing incomes and costs, households can better allo-
cate resources, set shared financial goals, and plan for both short-term needs and long-
termobjectives.
TheprovidedPythonscript,get_cooperative_financial_recommendation,seeksto
tapintothepotentialofLLMstogeneratebudgetingadvicetailoredforhouseholdsthat
arepoolingtheirresources.
KeyScriptFeatures:
• Caching Mechanism: Repetitive queries are bypassed by maintaining a
recommendation_cache. Ifdatafromahouseholdmatchapriorrequest,thecached
recommendationisreturned,therebyconservingcomputationaleffort.
• RetrywithExponentialBackoff: ThescriptisrobustagainstpotentialAPItimeouts
orotherexceptions. Byemployingaretrymechanismthatincreasesthewaitingtime
aftereachattempt,itprovidesresilienceagainsttransientissues.
• TailoredRecommendations: TheresponsefromtheLLMisparsedtoyieldasuccinct
andactionablecooperativefinancialrecommendationforthehousehold.
SampleUseCase
Considerahouseholdcomprisingtwomembers:
• Member1withanincomeofUSD5000,payingrentofUSD800andspendingUSD300
ongroceries.
• Member2earningUSD4000,havingarentofUSD700andgroceryexpensesamounting
toUSD350.
UponfeedingthesecombineddatatotheLLM,arecommendationcouldemergeas:

AI2024,5 102
“Giventhecombinedincomeandindividualexpenses,thehouseholdhasare-
mainingamountof$7850afterrentandgroceries. Itisadvisedtoallocate$1500
forjointsavings,$1000forutilitiesandsharedamenities,$500towardsentertain-
mentandleisure,andsetaside$1000asanemergencyfund. Theresidualamount
canbedirectedtowardsindividualsavingsorothersharedfinancialgoals.”
BenefitsofCollaborativeBudgeting:
1. SharedResponsibility: Distributingfinancialresponsibilitiescanalleviateindividual
burdensandpromotemutualaccountability.
2. StrategicDecisionMaking: Withpooledresources, householdscanmakemorein-
formedchoicesaboutinvestments,largepurchases,andsavings.
3. AchievementofCommonGoals: Beitbuyinganewhome,planningavacation,or
preparingforfamilyexpansions,cooperativebudgetingcanexpeditetherealization
ofsharedaspirations.
EnhancementsfortheFuture:
Thescript,whileeffective,canbeaugmentedfurtherby:
• Incorporatingfeedbackmechanismswherehouseholdmemberscanadjustrecommen-
dationsbasedonchangingfinancialscenarios.
• Integratingdatafromfinancialinstitutionsinreal-timeformorecurrentandaccurate
recommendations.
• Introducingfunctionalitiestohandlemorecomplexfinancialsituations,suchasin-
vestments,loans,andmortgages.
Inessence,cooperativebudgetingfacilitatedbyAI-drivenmodelscanrevolutionize
thewayhouseholdsmanagetheirfinances,promotingacultureoftransparency,mutual
trust,andsharedfinancialgrowth.
6. CooperativeBudgetingwithintheECFramework
Cooperativebudgetingforhouseholdsrepresentsatangibleinstantiationoftheex-
tendedcoevolutionary(EC)framework’sprinciplesfirstintroducedin[27]. Byanalyzing
this in the context of the EC theory, we illuminate the synergistic confluence of game-
theoreticmodels,LLMs,andadaptivelearninginpracticalMASscenarios.
LetusconsiderahouseholdHconsistingofnmembers,whereeachmemberoisan
agent. Eachagenthasafinancialprofilecharacterizedbyitsincome I andexpensesE .
o o
Thecollectivebudgetofthehouseholdcanbeexpressedas:
n
∑
B = I −E . (26)
H o o
o=1
ThegoalistocooperativelyallocateacommonbudgetB acrossmemberstooptimize
H
somehousehold-wideutilityfunctionU .Thisutilitycanbeameasureoffinancialstability,
H
savings,oranyothermetricsignificanttothehousehold.
IncorporatingtheadaptivelearningmechanismfromtheECframework,eachagento
iterativelyadjustsitsexpensesE basedonaderivedutilityU thattakesintoaccountthe
o o
household’scollectivegoalandindividualpreferences. Theadjustmentcanbemathemati-
callyrepresentedanalogoustothepreviousequationas:
E
o
(t+1) = E
o
(t)+α∇U
o
(E
o
(t),E−o (t)). (27)
Here,αremainsthelearningrate,and∇U signifiesthegradientofutilitywithrespect
o
toagento’sexpenses,consideringotheragents’expensesasE−o .
Thestrategyofagento,specificallyitsexpenseE ,canbeinfluencedbyrecommenda-
o
tionsfromanLLM.RepresentingtheLLM’srecommendationforagentoattimetasR ,
o,t
andsimilartotheequationpresentedbefore,thenewexpensecanbemodeledas:
E
o
(t+1) = (1−β)(E
o
(t)+α∇U
o
(E
o
(t),E−o (t)))+βR
o,t
. (28)

AI2024,5 103
Here,βdesignatestheinfluencerateoftheLLMontheagent’sexpensestrategy.
Given that LLM recommendations, like budget suggestions, come with inherent
uncertainties,aconfidencemeasureC associatedwitheachrecommendationR should
o,t o,t
beconsidered. Thisisanalogoustothepreviousequation,andtheupdatedexpensecanbe
modeledas:
E
o
(t+1) = (1−βC
o,t
)(E
o
(t)+α∇U
o
(E
o
(t),E−o (t)))+βC
o,t
R
o,t
. (29)
Eachhouseholdmembermayhavedistinctfinancialprioritiesandconstraints,echoing
theECtheory’semphasisonheterogeneousagents. TheutilityforeachagentU would
o
thusencapsulateindividualpreferences,likeriskaversionorfuturefinancialgoals.
Thecooperativebudgetingscenarioforhouseholdsaptlydemonstratestheapplicabil-
ityoftheECtheoryinreal-worldcontexts. Thisintersectionoftheoreticalconstructswith
tangibleapplicationsshowcasestherobustnessandversatilityoftheECframework. The
useofmathematicalrepresentationsdeepensourunderstanding,offeringaquantitative
lens to perceive the dynamics of the household as a multi-agent system influenced by
adaptivelearningandLLMs.
LinearOptimizationModelforFinancialPlanningwithLLMConstraints
Another instance of the same financial planning scenario is the following, where
weproposetousetheLLMrecommendationasboundsoftheoptimizationmodel. We
constructalinearoptimizationmodeltodistributethemonthlyincome I acrossvarious
expensecategorieswhilemaximizingpotentialsavings.Themodelisformulatedasfollows:
Let I representthemonthlyincomeofahousehold,andE representtheexpensesin
z
categoryz,wherezcanberent,groceries,utilitybills,orentertainment. LetSdenotethe
savingsforthemonth. ThegoalistomaximizeSsubjecttotheconstraintsimposedbythe
financialdataandrecommendationsfromtheLLM.
Theobjectivefunctionandconstraintsarepresentedasfollows:
∑
MaximizeS = I− E (30)
z
z
E ≥0∀z, (Non-negativityofexpenses) (31)
z
S ≥0, (Non-negativityofsavings) (32)
∑
E ≤ I, (Totalexpensesdonotexceedincome) (33)
z
z
AdditionalconstraintsarederivedfromtheLLMrecommendations,whichsuggest
percentagesofincometobeallocatedtowardeachcategory. Let p bethepercentageof
z
incomerecommendedforcategoryz,andErecbetherecommendedexpensescalculatedas
z
p ·I. Wecanintroduceboundsbasedontheserecommendationstoguidetheoptimization:
z
E ≥ Emin, (Minimumspending) (34)
z z
E ≤ Erec, (LLM-recommendedspending) (35)
z z
whereEminisalowerboundtoensurethateachcategorymeetsessentialspendingrequire-
z
ments. TheupperboundErec isinfluencedbytheLLM’sadviceandrepresentsanideal
z
spendingtargetassuggestedbythemodel.
7. SimulationFramework: LLM-InformedDecisions
TocomprehendtheLLM’s effectivenessinfinancial advice, itis essentialtoassess
its recommendations. Let us delve into its suggestions for individual and cooperative
financialmanagement:

AI2024,5 104
7.1. UserFinancialRecommendation
OpenAImodel: gpt4-0613
response=openai.ChatCompletion.create(model="gpt-4-0613",messages=[{"role":
"system","content": "Youareanexpertfinancialplannerwithextensiveknowledge
inhouseholdfinanceandbudgeting. Provideadetailedrecommendationonhowto
allocatefundsbasedonthegivendata."},{"role":"user","content":f"Here’smyfinan-
cialdataforthemonth: {income_data_string}. Canyouprovidearecommendation
onhowIshouldspendorsavetheremainingfunds?"}])
Theinstructiongiventothemodelfocusedonitsexpertiseasafinancialplanner. This
queryisindicativeofhowtheLLMwouldprocessindividualfinancialdataandprovidea
comprehensiverecommendation.
LLMUserFinancialRecommendation
Ofcourse,basedonyourprovidedincomeandexpenditure,yourtotalspending
addsupto$1900outof$5000. Thisleavesyouwitharemainingbalanceof$3100.
Let’sbreakdownandallocateyourremainingbalanceasfollows:
1. **EmergencyFund**: Ifyoudon’talreadyhaveanemergencyfund,aimtobuild
one.Thisshouldconsistof3–6months’worthoflivingexpensestocoverunexpected
costs,suchasamedicalemergencyorcarrepair. Ifyoudon’thavesuchafundpot,
thenit’sgoodtoallocatearound20%($620)oftheremainingmoneytowardsit.
2. **RetirementSavings**: Ifyou’renotcurrentlycontributingtoaretirementfund,
it’sagoodideatostart. Ageneralruleistoallocate15–20%ofyourincometowards
yourretirement.Inthiscasefromtheremainingsum,considerallocating20%($620).
3. **DebtPayments**: Ifyouhaveanyoutstandingdebtlikestudentloans,credit
carddebt,etc,it’scrucialtoallocateaportionofyourincometowardspayingthese
off. Fornow,fromthisremainingbalanceyoucouldallocate15%($465).
4.**PersonalSavings/Investments**:It’salwaysagoodideatoinvestinyourfuture,
whetheritmeansbuyingahouse,startingyourownbusiness,ortakingavacation.
Youcouldaimtoallocate20%($620)forthispurpose.
5. **Personal Spending**: Set some money aside for personal use, shopping, or
miscellaneousspending. Around10%($310)couldbeallocatedforthispurpose.
6. **HealthandFitness**: Considerthisasaninvestmentinyourhealth. Allocate
about5%($155).
7. **Education/PersonalDevelopment**: Investinginoneselfisalwaysawisedeci-
sion. 5%oftheremainingmoneywhichwouldbearound$155couldbededicated
forthispurpose.
8. **Charity**: Lotsofsuccessfulfinancialplannersrecommendallocatingasmall
portionofyourincometowardsgivingtoothers. Around5%($155)shouldbeagain
agoodstart.
Here’showthefinalallocationlookslike:
• EmergencyFund: $620
• RetirementSavings: $620
• Debtpayments: $465
• PersonalSavings/Investments: $620
• PersonalSpending: $310
• HealthandFitness: $155
• Education/PersonalDevelopment: $155
• Charity: $155
Analysis: Therecommendationbeginsbyacknowledgingtheuser’sfinancialstate,
ensuringtransparencyintheLLM’scalculations. Themodelthenmeticulouslydividesthe

AI2024,5 105
leftoverfundsintoeightcategories. Thesecategoriesrepresentthefundamentalareasthat
mostindividualsneedtoconsiderintheirfinancialplanning. Theproportionalallocation
seemsbalancedandencouragesbothsavingandinvestingwhilealsoemphasizingpersonal
well-beingandcommunitygiving.
This framework aligns well with traditional financial planning advice, indicating
themodel’sefficacyinthisdomain. Moreover,theclarityandstructureprovidedbythe
modelcangreatlyassistusersinunderstandingtheirfinancialstandingandplanningtheir
futureexpenditures.
7.2. CooperativeFinancialRecommendation
OpenAImodel: gpt4-0613
response=openai.ChatCompletion.create(model="gpt-4-0613",messages=[{"role":
"system","content": "Youareanexpertfinancialplannerwithexpertiseincoopera-
tivebudgetingforhouseholds. Provideacomprehensiverecommendationbased
onthecombinedfinancialdata."},{"role": "user","content": f"Here’sourcombined
householdfinancialdata: {household_data_string}. Canyourecommendhowwe
shouldcollaborativelybudgetourexpenses?"}])
Inthisinquiry, themodelwastaskedwithprovidingacomprehensiverecommen-
dation based on combined financial data, embodying the complexities of cooperative
budgetingforhouseholds.
Analysis: Themodeladoptsadetailedapproachtocooperativefinancialplanning,
startingwithaclearbreakdownofcombinedincomeandessentialexpenseslikehousing
andgroceries. Thepercentagesusedtoallocatevariousexpenses,suchashousingtaking
up25–30%oftheincome,alignwithwidelyacceptedfinancialguidelines.
Aparticularlynoteworthyaspectofthisrecommendationistheinclusionofanemer-
gencyfund,highlightingtheLLM’scapacitytoforeseepotentialfinancialpitfallsandits
alignmentwithprudentfinancialpractices.
Thecooperativerecommendation,muchliketheindividualone,iscomprehensive,
detailed,andalignswithstandardfinancialplanningguidelines.Thisreinforcesthemodel’s
reliabilityinproducingaccurateandactionablefinancialadvice.

AI2024,5 106
LLMCooperativeFinancialRecommendation
Absolutely. Here’sacomprehensivebudgetingplanbasedonthecombinedfinan-
cialdata:
1.**IncomeAnalysis:**Yourcombinedtotalmonthlyincomeis$5000+$4000=$9000.
2.**HousingExpenses:**Yourcombinedrentis$800+$700=$1500,whichis16.67%
ofyourincome. Consideringthathousingshouldgenerallybearound25–30%of
yourincome,you’reinagoodpositionhere.
3. **Grocery Expenses:** Your combined grocery cost is $300 + $350 = $650 per
month. Thiscostisapproximately7.2%ofyourtotalincomewhichisbelowthe
usual10–15%range. Youaresofarmanagingthisexpenseeffectivelybuttheremay
beroomforimprovednutritionordesiredtreatswithinthisbudget.
4. **Savings:**Agoodruleofthumbwouldbetosaveatleast20%ofyourincome.
Inyourcase,thatwouldbe$1800permonth.
5. **Other Expenses:** After accounting for rent, groceries and savings, you have
$4050lefteachmonth($9000−$1500−$650−$1800).Youshouldusethisremaining
moneytocoverotherexpenses.Itwouldbeadvisabletodistributeitasfollows:
• **Utilities: 5–10%ofincome:**Thiswouldbeabout$450–$900.
• **Healthcare: 5–10%ofincome:**Thisshouldbeapproximately$450–$900.
• **Transportation: 10–15%ofincome:**Thisshouldideallybebetween$900–
$1350.
• **Recreational&PersonalExpenses: 5–10%ofincome:**Thisistypically$450–
$900.
• **RetirementContribution: Atleast10%ofincome:**Thiswouldbe$900in
yourcase.
Thisdistributionmayvarybasedonyourpersonalneeds,lifestyle,debtrepayments,
andobligations. Itwouldbewisetokeeptrackofyourexpensestoensureyou’re
in-linewithyoursetbudget.
6. **EmergencyFund:**Itisalsoimportanttoensurethatyouhaveanemergency
fundinplace. Ideally,thisfundshouldcover3–6months’worthoflivingexpenses,
andgivenyourexpenserate,thisshouldbesomewherebetween$10,800–$21,600. If
youdonothaveanadequateemergencyfundinplace,thenportionofyoursavings
shouldbeallocatedtothisfunduntilthetargetismet.
Endoftheday,thegoalistoensuretheincomeisdistributedinawaythatcovers
alltheneeds,whilealsoensuringthere’sfinancialgrowthandstability. Regularly
revisityourbudgetandadjustaccordinglybasedonchangesinincome,expenses,
andfinancialgoals.
7.3. TheSignificanceofLong-TermModelsinFinancialPlanning
Financialplanning[28,29],atitscore,isnotjustaboutbudgetingforthenextmonthor
year: itisaboutlayingafoundationfortheentirelife-cycle[30,31]. Decisionsmadetoday
willinevitablyimpactfinancialsecurity,flexibility,andwealthaccumulationinthedistant
future. Withthisunderstanding,therearisesanimperativeneedforlong-termmodelsin
thedomainoffinancialplanning.
Long-termmodelsbringforesighttofinancialdecisionmaking. Byanalyzinglong-
termimplicationsofcurrentfinancialdata,thesemodelsofferrecommendationsthatare
notjustaboutimmediatebenefitbutalsocatertofuturefinancialhealth. Theimportanceof
long-termmodelsbecomesevenmorepronouncedinsituationsthatinvolveuncertainties
likechangingjobmarkets,economicfluctuations,orpersonallifeevents.
Hereisaglimpseintothekeybenefitsandfunctionalitiesoflong-termmodelsinthe
financialdomain:
• ConsumptionSmoothing:Long-termmodelsassistinbalancingconsumptionpatterns
overtime,ensuringthatindividualsdonotoverspendduringprosperousperiodsor

AI2024,5 107
facehardshipduringleantimes. Byforecastingfutureincomestreamsandfinancial
obligations, long-term models promote consistent living standards throughout an
individual’slife.
• Life-cycle Modeling: These models simulate various stages of an individual’s life,
fromearlycareerstages,potentialfamilyplanning,andmid-lifecrises,toretirement.
By doing so, they help in preparing for financial needs and challenges typical to
eachphase.
• Risk Management: LLMs highlight potential risks by analyzing economic trends,
inflationrates,andpersonalfinancialdata. Theyhelptodevisestrategiestomitigate
theserisks,beitthroughinvestments,insurance,orsavings.
• Investment Guidance: Based on long-term financial goals and market predictions,
LLMsprovideguidanceonwhereandhowmuchtoinvest. Thisincludessuggestions
ondiversifyingportfolios,adjustingassetallocations,andmore.
• Future Projections: One of the standout features of LLMs is their ability to project
financialfuturesbasedoncurrentdataanddecisions. Theyofferaroadmapofwhere
one’sfinancescouldbein5,10,oreven30yearsfromnow.
7.4. Long-TermCooperativeFinancialRecommendation
OpenAImodel: gpt4-0613
response=openai.ChatCompletion.create(model="gpt-4-0613",messages=[{"role":
"system","content": "Youareanexpertfinancialplannerwithexpertiseinlife-cycle
modelsandcooperativebudgetingforhouseholds. Provideacomprehensiverec-
ommendationbasedonthecombinedfinancialdatathatconsidersconsumption
smoothingovertheentirelife-cycle."},{"role": "user","content": f"Here’sourcom-
binedhouseholdfinancialdata,alongwithsomefutureprojectionsandlifeevents:
{household_data_string}. Can you recommend how we should collaboratively
budgetourexpenses?"}])
Hereisanexampleusagewithmorecomprehensivedatatakingintoaccountlong-term
dependencies:

AI2024,5 108
LLMLong-TermCooperativeFinancialRecommendation
Usingthelife-cyclemodelinvolvessettingyoursavingandspendinghabitswitha
long-termvision. Consumptionsmoothingisakeypartofthis,aimingtoallocate
resourcesinawaythatmaintainsaconsistentstandardoflivingthroughoutyour
life. Here are my recommendations based on both your income and projected
lifeevents:
1. **StartanEmergencyFund**: Saveaportionofyourcombinedincomeconsis-
tently until you have about three to six months’ worth of living expenses. Con-
sideringyourincomesandbasicmonthlyexpenses,whichtotal$2150,I’dsuggest
allocatingatleast$500/monthforthisinitially.
2. **CreateaChildFund**: Sinceyou’replanningtohaveachildin3years,cre-
ating a dedicated child fund should be a priority. It will help cover everything
frompregnancy-relatedmedicalcoststofutureschoolingexpenses. Let’sallocate
$300/monthforthisfund.
3. **RetirementSaving**: Member2isplanningtoretirein20years,soasubstantial
partoftheincomeshouldgotowardsretirementsavings. Ifnotalreadystarted,I
proposeanimmediatebeginningwithaninitialtierofatleast$600amonth.
4. **IncomeAdjustment**: ThepotentialpaycutforMember1shouldbeplanned
forinadvance. Tofacilitateconsumptionsmoothing,considerincreasingsavingsor
reducingnon-essentialexpensestoaccommodatetheprojected10%paycut.
5. **HousingExpenses**: Yourtotalmonthlyrentis$1500. Ifyoustayinthecurrent
rentalsituationforthelongterm,therecouldbeanopportunitytobuyahouse,as
longasit’sfinanciallyreasonable.
6. **DailyLivingandUnexpectedExpenses**: Allocatetherestoftheincomefor
yourdailylivingexpensesandunexpectedcosts(carrepairs,medicalexpenses,etc.).
Insummary,thisisaroughrecommendationonwhichcategoriescanthebudget
bedivided:
• **EmergencyFund**: $500/month
• **ChildFund**: $300/month
• **RetirementSavings**: $600/month
• **Housing**: $1,500/month
• **Groceries**: $650/month
• **Daily Living and Unexpected Costs**: The balance of your incomes after
removingtheaboveexpenses(approximately$2450).
Thisplanwillrequirereviewandadjustmentonaregularbasis,atleastyearly,to
accommodatechangesinincomeornewfinancialneeds/goals. Remember,thekey
tothelife-cyclemodelisflexibilityandlong-termplanning.
As seen from our simulation framework, when LLMs like gpt-4-0613 are given a
long-term perspective, they provide advice that aligns with the core tenets of financial
planning. Whetheritisindividualorcooperativebudgeting,themodel’srecommendations
reflectanunderstandingoftheintricatedancebetweencurrentspending,futureneeds,
andlong-termfinancialgrowth.
Analysis:Thelong-termcooperativefinancialrecommendationexemplifiesthemodel’s
capacitytoengagewithcomplexfinancialscenariosthatspanacrossanindividual’slife-
time.Notably:
• ConsumptionSmoothing: Themodelemphasizesconsumptionsmoothingbysuggest-
ingaconsistentstandardofliving. Itsadviceonadjustingincometoaccommodatea
projectedpaycutisparticularlysalient,asitshowcasesthemodel’sabilitytosuggest
proactivemeasuresagainstpotentialfinancialsetbacks.
• EmergencyandSpecificFunds: Theinclusionofbothanemergencyfundandachild
fundshowcasesthemodel’scomprehensiveapproach. Ithighlightsanunderstanding

AI2024,5 109
ofimmediateneeds(likeemergencies)andfutureevents(likeplanningforachild),
thuspromotingfinancialpreparedness.
• RetirementPlanning:Themodel’sadvicetoprioritizeretirementsavingsforMember2,
whoplanstoretirein20years,underscoresitsalignmentwithalong-termvision. It
demonstratesanacuteawarenessofthetime-sensitivenatureofretirementplanning.
Overall,themodel’slong-termcooperativefinancialrecommendationreflectsagood
understandingofthelife-cyclemodel’sprinciples. Itmeticulouslyintegratesimmediate
financialneedswithlong-termgoals,showcasingitspotentialtoserveasavaluabletoolin
thedomainoffinancialplanning.
7.5. SimulationofFinancialPlanningwithLLMRecommendations
Goingbeyond, wepresentasimulationthatintegratesfinancialrecommendations
from an LLM into the financial planning process of synthetic household datasets. Our
approachinvolvesgeneratingsyntheticfinancialprofilesfortenhouseholds,encompassing
monthly income and expenses across four categories: rent, groceries, utility bills, and
entertainment. The monthly incomes are normally distributed around a mean of USD
5000withastandarddeviationofUSD1000. Expensesineachcategoryarealsogenerated
followinganormaldistributionwithcategory-specificmeansandvariances.
Once the synthetic dataset is established, we employ an LLM to provide financial
planningadviceforeachhousehold.TheLLMispromptedtoanalyzethefinancialdataand
recommendallocationsaspercentagesofthehousehold’smonthlyincome. Theadviceis
structuredtoincludeessentialexpenditures,savings,anddiscretionaryspending,following
soundfinancialplanningprinciples.
TheLLM’stextualrecommendationsareparsedusingregularexpressionstoextract
thesuggestedallocationpercentagesforeachfinancialcategory. Theseextractedvaluesare
thentranslatedintomonetaryamountsbasedontherespectivehousehold’sincomeand
storedalongsidetheoriginaldata.
Subsequently,weapplyalinearprogrammingoptimizationmodeltoeachhousehold’s
financialdata,aimingtomaximizesavingswhileadheringtorealisticconstraints. This
model takes into account minimum spending requirements for each expense category,
ensuringthattheoptimizedplanremainspracticalandsustainable.
Finally, we visualize the simulation results, comparing the original savings, LLM-
recommendedsavings,andoptimizedsavingswithbounds. Thiscomparisonhighlights
thepotentialimpactofAI-drivenfinancialadvicewhencombinedwithtraditionalopti-
mizationtechniques.
The instance of a financial planning scenario in Figure 2 not only showcases the
feasibilityofutilizingAIinpersonalfinancialplanningbutalsoservesasabenchmarkfor
evaluatingtheLLM’sperformanceagainsttraditionaloptimizationmodels. Thefindings
suggestthatLLMscaneffectivelycontributetofinancialdecisionmaking,offeringinsights
thatalignwithrecognizedfinancialbestpractices.
Thesimulationinvolvesseveralstages:
1. Generationofsyntheticfinancialdataforeachhousehold,withrandomdistributions
forincomeandexpenses.
2. RetrievaloffinancialrecommendationsfromanLLM,whichanalyzesthesynthetic
dataandprovidesallocationpercentagesforvariousexpensecategories.
3. Parsing of the LLM output to translate percentage-based recommendations into
monetaryallocations.
4. Applicationofalinearoptimizationmodeltodetermineanoptimizedsavingsstrategy
foreachhousehold,independentofLLMrecommendations,usingfixedminimum
spendingboundsforeachexpensecategory.
5. Visualcomparisonofthehouseholds’originalsavings,thesavingsasrecommended
bytheLLM,andthesavingspost-optimization,highlightingthepotentialofLLM
guidanceinenhancingfinancialdecisionmaking.

AI2024,5 110
LLMRecommendation
LLM_output=Basedonyourincomeandexpensedata,hereishowIwillsuggest
allocatingyourfunds:
• Rent: 24%ofincome
• Groceries: 8%ofincome
• UtilityBills: 4%ofincome
• Entertainment: 2%ofincome
• EmergencyFund: 20%ofincome
• RetirementSavings: 15%ofincome
• Non-retirementSavings: 10%ofincome
• Debts: 8.5%ofincome
• PersonalSpending: 8.5%ofincome
Figure 2. Comparative analysis of household savings across three different financial planning
scenarios. The’OriginalSavings’barsrepresentthesavingscalculatedfromthesyntheticdataset
withoutanyoptimization. The’OptimizedSavingswithBounds’barsillustratethesavingsafter
applyingalinearoptimizationmodelthatmaximizessavingswhileconsideringminimumessential
expenditures.The’LLMRecommendedSavings’barsreflecttheaggregateofsavingscategoriesas
suggestedbytheLLM,includingemergencyfund,retirementsavings,andnon-retirementsavings.
IntheprocessofdevelopingourLLMfinancialrecommendersystem,wemapped
theinteractionsbetweenvariouscomponentstoensureaseamlessuserexperienceand
robustperformance. Figure3illustratesthesequenceofeventsfromthemomentauser
inputstheirfinancialdatatothereceiptofpersonalizedrecommendationsandsubsequent
budgetoptimization. Thisdiagramdelineatesthesystem’sworkflow,highlightingtherole
oftheLLMinanalyzingfinancialdataandgeneratingtailoredadvice.Thesequencefurther
demonstratestheintegrationofanoptimizationmodelthatfine-tunestheinitialrecom-
mendationstoaccommodateuser-specificfinancialgoalsandconstraints. Theinteraction
betweentheuser,LLM,andoptimizationmodelencapsulatesthesynergyofAI-driven
insights with algorithmic precision, which is central to the innovative approach of our
financialplanningsystem.

AI2024,5 111
User APIInterface LLMSystem OptimizationModel Database
ProvideFinancialData
CChheecckkCCaacchhee Retrievecachedrecommendationifavailable
QueryCache
CachedRecommendation
RequestAnalysis
AnalyzeData
Recommendation
CacheRecommendation
ReceiveRecommendation
OOppttiimmiizzaattiioonn AdjustallocationsbasedonLLMrecommendation
InputLLMRecommendations
CalculateOptimizedPlan
OptimizedAllocation
ReviewandAdjustBudget
Figure3.SequencediagramoftheLLMfinancialrecommendersystemillustratingtheinteraction
betweentheuser,LLMsystem,APIinterface,optimizationmodel,anddatabase.
ThequalitativeanalysisinTable1distinctlyshowcasestheadvantagesofourproposed
modelsovertraditionalfinancialplanningmethodologies. Keyenhancementsincludethe
capacityforhighpersonalization,wheretheLLM’sinferentialabilitiestailorrecommen-
dationstospecificuserscenarios. Unliketraditionalmodels,ourapproachdynamically
adaptstomarketchanges,leveragingtheLLM’scapacitytoanalyzecurrentdatatrends.
Scalabilityisanothersignificantimprovement: theAI-drivenmodelcansimultaneously
catertoavastarrayofusers,afeatchallengingfortraditionalmethods. Intermsofuser
accessibility,theproposedsystemsimplifiescomplexfinancialconcepts,makingfinancial
planning more approachable for the general public. The integration of real-time data
ensures that the advice is always relevant and timely, a critical aspect often lacking in
conventional models. Finally, the proposed methodology excels in long-term financial
planning,withtheabilitytoprojectandadapttofuturefinancialscenarios,providingusers
withacomprehensiveviewoftheirfinancialtrajectory.

AI2024,5 112
Table1.ComparativeanalysisoftraditionalandproposedLLM-integratedmodels.
Proposed Models with
Criteria TraditionalModels Comments
LLMIntegration
TheintegrationofLLMsallowsforhighly
Personalization Low High personalizedfinancialplanningbasedon
individualorhousehold-specificdata.
LLMscanrapidlyadjustrecommendations
AdaptabilitytoMarketChanges Limited Enhanced in response to fluctuating market condi-
tions.
TheAI-drivenapproachcaneasilyscaleto
Scalability Moderate High handlealargenumberofuserssimultane-
ously.
TheuseofLLMsmakesfinancialplanning
UserAccessibility Variable Improved more accessible to users without deep fi-
nancialknowledge.
Proposedmodelscanintegrateandanalyze
Real-timeDataIntegration Limited Enhanced
real-timedataforup-to-dateadvice.
LLMscanprojectlong-termfinancialout-
Long-termFinancialPlanning Moderate Superior comes, aidinginmoreeffectivelife-cycle
financialplanning.
8. ConclusionsandFutureWork
Thetransitionfromtraditionaloptimizationapproachestotheuseoftheextended
coevolutionary(EC)theorypresentsaninnovativedirectionforthedomainoffinancial
planning. Byanalyzingcooperativebudgetingwithinhouseholds,thispaperilluminates
thecompatibilityofgame-theoreticmodels,adaptivelearning,andtheinfluentialroleof
largelanguagemodels(LLMs)inshapingfinancialrecommendations.
TheprovidedpipelineexemplifiespracticalapplicationsoftheECtheory[27],demon-
stratingamarriagebetweenadaptivelearningmechanismsandLLMstogeneratefinancial
advisories,asaninstantiationofaneweconomictheorywherehumandecisionscanbe
greatlyinfluencedbyAIagents. ThroughiterativerefinementsinfluencedbyLLMrec-
ommendations,thesystemiterativelyapproachesoptimalfinancialallocations. Theclear
distinctionbetweenindividualizedfinancialrecommendationsandcooperativehousehold
budgetingreinforcestheversatilityofthisapproach,whichcouldbeseamlesslyintegrated
intohouseholdmembersbytheuseofasmartphone,smartwatch,orpersonalcomputer.
Futureworkmayinvolve:
• ExpansionofUtilityFunctions: Futurestudiescoulddelvedeeperintoconstructing
morecomprehensiveutilityfunctions,encompassingfactorslikechangingfinancial
landscapes,inflationrates,andsocio-economicconsiderations.
• ModelRobustness: AnalyzingtherobustnessofLLMrecommendationsindiverse
financial scenarios, especially under market volatility, would be beneficial. This
ensuresthesystem’sresilienceandadaptabilitytoexternalshocks.
• IntegrationwithReal-timeData: Byinterfacingtheproposedmethodologywithreal-
timefinancialdatabases,therecommendationscanberenderedevenmoretimelyand
relevant.
• Human-in-the-loopMechanism: WhileLLMsareproficient,humanexpertiseremains
indispensable.Incorporatingahuman-in-the-loopmechanism,wherefinancialexperts
refineorvalidateLLMrecommendations,couldelevatethesystem’sreliability.
• EthicalConsiderations: AswithanyAI-drivensystem,ethicalconsiderations,espe-
ciallyinadomainascrucialasfinance,areparamount. Futureworkmustensurethat
therecommendationsareunbiased,transparent,andinthebestinterestoftheusers.

AI2024,5 113
• ScalabilitytoLargerCooperativeEntities: Whilehouseholdsweretheprimaryfocus,
scalingthemodeltoaddresscooperativebudgetingforlargerentities,likecommunity
groupsorsmallbusinesses,couldbeanaturalprogression.
In essence, the integration of the EC framework into financial planning is but the
tipoftheiceberg. Thepotentialapplicationsandrefinementsarevast,openingavenues
forresearchandpracticalimplementationsthatcansignificantlyenhancethequalityof
financialadvisoriesanddecision-makingprocesses.
AuthorContributions:Authorcontributions:conceptualization,J.d.C.andI.d.Z.;fundingacquisi-
tion,G.R.,C.T.C.,andI.d.Z.;investigation,I.d.Z.andJ.d.C.;methodology,I.d.Z.,J.d.C.,andG.R.;
software,J.d.C.andI.d.Z.;supervision,C.T.C.andG.R.;writing—originaldraft,J.d.C.andI.d.Z.;
writing—reviewandediting,J.d.C.,I.d.Z.,C.T.C.,andG.R.Allauthorshavereadandagreedtothe
publishedversionofthemanuscript.
Funding: WethankthefollowingfundingsourcesfromGOETHE-UniversityFrankfurtamMain;
‘DePP—Dezentrale Plannung von Platoons im Straßengüterverkehr mit Hilfe einer KI auf Basis
einzelnerLKW’,‘CenterforDataScience&AI’,and‘xAIBiology’.Weacknowledgethesupportof
R&DprojectPID2021-122580NB-I00,fundedbyMCIN/AEI/10.13039/501100011033andERDF.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Dataarecontainedwithinthearticle.
ConflictsofInterest:Theauthorsdeclarethattheyhavenoconflictsofinterest.Thefundershadno
roleinthedesignofthestudy,inthecollection,analyses,orinterpretationofdata,inthewritingof
themanuscript,orinthedecisiontopublishtheresults.
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
LargeLanguageModels LLMs
DeepLearning DL
ArtificialNeuralNetworks ANNs
Multi-AgentSystems MASs
ArtificialIntelligence AI
ExtendedCoevolutionary EC
RetrievalAugmentedGeneration RAG
References
1. Campbell,J.Y.Householdfinance.J.Financ.2006,61,1553–1604.[CrossRef]
2. Guiso,L.;Sodini,P.Householdfinance:Anemergingfield.InHandbookoftheEconomicsofFinance;Elsevier:Amsterdam,The
Netherlands,2013;Volume2;pp.1397–1532.
3. Vaswani,A.;Shazeer,N.;Parmar,N.;Uszkoreit,J.;Jones,L.;Gomez,A.N.;Kaiser,Ł.;Polosukhin,I.Attentionisallyouneed.In
ProceedingsoftheAdvancesinNeuralInformationProcessingSystems30,(NIPS2017),LongBeach,CA,USA,4–9December
2017;pp.5998–6008.
4. Radford,A.;Kim,J.W.;Hallacy,C.;Ramesh,A.;Goh,G.;Agarwal,S.;Sastry,G.;Askell,A.;Mishkin,P.;Clark,J.;etal. Learning
transferablevisualmodelsfromnaturallanguagesupervision. InProceedingsofthe38thInternationalConferenceonMachine
Learning,Virtual,18–24July2021.
5. Perry,V.G.;Martin,K.;Schnare,A. AlgorithmsforAll:CanAIintheMortgageMarketExpandAccesstoHomeownership?AI
2023,4,888–903.[CrossRef]
6. Roccetti,M.;Delnevo,G.;Casini,L.;Mirri,S. Analternativeapproachtodimensionreductionforparetodistributeddata:Acase
study. J.BigData2021,8,39. [CrossRef][PubMed]
7. Markowitz,H.PortfolioSelection.J.Financ.1952,7,77–91..[CrossRef]
8. Ando,A.;Modigliani,F.The‘LifeCycle’HypothesisofSaving:AggregateImplicationsandTests.Am.Econ.Rev.1963,53,55–84.
Availableonline:http://www.jstor.org/stable/1817129(accessedon8November2023).
9. Charnes,A.;Cooper,W.W.ManagementModelsandIndustrialApplicationsofLinearProgramming.Manag.Sci.1957,4,38–91.
[CrossRef]

AI2024,5 114
10. Merton,R.C.LifetimePortfolioSelectionunderUncertainty: TheContinuous-TimeCase. Rev. Econ. Stat. 1969,51,247–257.
[CrossRef]
11. Thaler,R.H.TowardaPositiveTheoryofConsumerChoice.J.Econ.Behav.Organ.1980,1,39–60.[CrossRef]
12. Kahneman, D. Maps of Bounded Rationality: Psychology for Behavioral Economics. Am. Econ. Rev. 2003, 93, 1449–1475.
[CrossRef]
13. Dixon,M.;Klabjan,D.;Bang,J.H.Classification-basedFinancialMarketsPredictionusingDeepNeuralNetworks.Algorithmic
Financ.2017,6,67–77.[CrossRef]
14. Mhlanga,D.Industry4.0inFinance:TheImpactofArtificialIntelligence(AI)onDigitalFinancialInclusion.Int.J.Financ.Stud.
2020,8,45.[CrossRef]
15. Althnian,A.DesignofaRule-BasedPersonalFinanceManagementSystemBasedonFinancialWell-Being.Int.J.Adv.Comput.
Sci.Appl.2021,12,182–187.[CrossRef]
16. Nazareth,N.;Reddy,Y.Y.R.FinancialApplicationsofMachineLearning:ALiteratureReview.ExpertSyst.Appl.2023,219,119640.
[CrossRef]
17. Dowling, M.; Lucey, B. ChatGPT for (Finance) Research: The Bananarama Conjecture. Financ. Res. Lett. 2023, 53, 103662.
[CrossRef]
18. Weber,P.;Carl,K.V.;Hinz,O.ApplicationsofExplainableArtificialIntelligenceinFinance—ASystematicReviewofFinance,
InformationSystems,andComputerScienceLiterature.Manag.Rev.Q.2023,1–41..[CrossRef]
19. Kumar, S.; Lim, W.M.; Sivarajah, U.; Kaur, J.ArtificialIntelligenceandBlockchainIntegrationinBusiness: Trendsfroma
Bibliometric-ContentAnalysis.Inf.Syst.Front.2023,25,871–896.[CrossRef][PubMed]
20. Pallathadka,H.;Ramirez-Asis,E.H.;Loli-Poma,T.P.;Kaliyaperumal,K.;Ventayen,R.J.M.;Naved,M.ApplicationsofArtificial
IntelligenceinBusinessManagement,E-commerceandFinance.Mater.TodayProc.2023,80,2610–2613.[CrossRef]
21. Arsenyan,J.;Piepenbrink,A.ArtificialIntelligenceResearchinManagement:AComputationalLiteratureReview.IEEETrans.
Eng.Manag.2023..[CrossRef]
22. Xiao,J.J.Applyingbehaviortheoriestofinancialbehavior.InHandbookofConsumerFinanceResearch;Springer:NewYork,NY,
USA,2008;pp.69–81.._5.[CrossRef]
23. Browning,M.;Lusardi,A.HouseholdSaving:MicroTheoriesandMicroFacts.J.Econ.Lit.1996,34,1797–1855.Availableonline:
http://www.jstor.org/stable/2729595(accessedon8November2023).
24. Branzei,R.;Dimitrov,D.; Tijs,S.ModelsinCooperativeGameTheory; SpringerScience&BusinessMedia: Berlin/Heidelberg,
Germany,2008;Volume556.
25. Baker,H.K.; Filbeck,G.; Ricciardi,V.(Eds.). FinancialBehavior: Players,Services,Products,andMarkets,FinancialMarketsand
Investments;OxfordAcademic:NewYork,NY,USA,2017.
26. Arner,D.W.;Zetzsche,D.A.;Buckley,R.P.;Barberis,J.N.FinTechandRegTech:EnablingInnovationWhilePreservingFinancial
Stability.Georget.J.Int.Aff.2017,18,47–58.Availableonline:http://www.jstor.org/stable/26395923(accessedon8November
2023).[CrossRef]
27. deZarzà,I.;deCurtò,J.;Roig,G.;Manzoni,P.;Calafate,C.T. EmergentCooperationandStrategyAdaptationinMulti-Agent
Systems:AnExtendedCoevolutionaryTheorywithLLMs. Electronics2023,12,2722. .[CrossRef]
28. Alhenawi,Y.;Hassan,M.K.;Hasan,R. Evolutionofresearchinfinanceoverthelasttwodecades—Atopographicalview.Res.Int.
Bus.Financ. 2022,59,101550.[CrossRef]
29. Luigi,G.;Luana,Z.Frompatriarchytopartnership:Genderequalityandhouseholdfinance. J.Financ.Econ.2023,147,573–595.
30. Chai,J.;Horneff,W.;Maurer,R.;Mitchell,O.S. OptimalPortfolioChoiceovertheLifeCyclewithFlexibleWork,Endogenous
Retirement,andLifetimePayouts. Rev.Financ.2011,15,875–907. .[CrossRef]
31. Browning,M.;Crossley,T.F.TheLife-CycleModelofConsumptionandSaving.J.Econ.Perspect.2001,15,3–22. .[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.