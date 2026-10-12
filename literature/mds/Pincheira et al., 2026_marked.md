---
conversion_metadata:
  converted_at: "2026-10-11T15:12:18Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Pincheira et al., 2026.pdf"
  source_pdf_sha256: "81444e83e1d203cdd3068931d81bbc6078bee2317c40ac94d8cc673fdb3aabbc"
  page_count: 27
  markdown_char_count: 96070
---

Article
The Paradox Between Correlations and Sign Predictability
PabloPincheira1,* ,AndreaBentancor2 andLorenzoReus1
1 SchoolofBusiness,UniversidadAdolfoIbáñez,Santiago7941169,Chile;lorenzo.reus@uai.cl
2 FacultaddeEconomíayNegocios,UniversidaddeTalca,Santiago894000,Chile;andrea.bentancor@utalca.cl
* Correspondence:pablo.pincheira@uai.cl;Tel.:+56-223311349
Abstract
Thispaperuncoversaparadoxicaldisconnectbetweentwowidelyusedmetricsforforecast
evaluation:MeanDirectionalAccuracy(MDA)andthecorrelationbetweentheforecastand
thetargetvariable. Weshowthataforecastthatismorestronglycorrelatedwiththetarget
maydeliverpoorersignpredictionsthanalesscorrelatedalternative. WithinaGaussian
framework,wederiveanalyticalexpressionsshowingthatdirectionalaccuracydepends
notonlyoncorrelationbutalsoonthestandardizedmeansofboththeforecastandthe
target variable. As a consequence, higher correlation does not guarantee superior sign
predictability. Weillustratethisparadoxthroughanalyticalexamplesandderiveformal
conditions under which it cannot arise. Interestingly, we show that when forecasts are
efficient,theMDAParadoxisimpossible. Finally,wepresentanempiricalapplicationfrom
theexchangerateliteraturethatdemonstratesthepracticalrelevanceofourresults.
Keywords: forecasting; out-of-sample evaluation; mean squared prediction error; ex-
changerates
MSC:91-10;91-11;91B84;62P20;62M10
1. Introduction
Forecastevaluationreliesonavarietyofstatisticalmetrics,eachcapturingdifferent
aspectsofpredictivequality. WhileMeanSquaredPredictionError(MSPE)isthemost
commonlyusedcriterion,othermeasures,suchasMeanAbsoluteError(MAE),correlations
betweenforecastsandthetargetvariable,andMeanDirectionalAccuracy(MDA),arealso
widelyemployed(MDAisalsoknownashit-rate, successrateorsignagreementratio,
anditisconsideredinmanyarticlesstudyingpredictability,including[1–6],amongmany
others).MDA,inparticular,measuresaforecast’sabilitytocorrectlyanticipatethedirection
ofchangeinthetargetvariable,makingitespeciallyrelevantforinvestorsinterestedin
trading strategies based on directional accuracy rather than MSPE. (See, for instance,
AcademicEditor:ZhengXu Ref.[7]).
Received:18December2025 Despitetheusefulnessofthesemetrics,thereareclearandfundamentaldifferences
Revised:3February2026 amongthem. Mostimportantly,whencomparingtwocompetingforecasts,say,forecasts
Accepted:9February2026
A and B, it is entirely possible for one metric to favor forecast A while another favors
Published:24February2026
forecastB.Awell-knownexampleistheso-calledMSPEParadox:undercertaininefficiency
Copyright:©2026bytheauthors.
conditions,theforecastwiththelowestMeanSquaredPredictionErrormayalsoexhibitthe
LicenseeMDPI,Basel,Switzerland.
lowestcorrelationwiththetargetvariable(see[8]). Thisparadoxchallengesthenotionthat
Thisarticleisanopenaccessarticle
distributedunderthetermsand lowerMSPEnecessarilysignalsamoreinformativeorusefulforecast,particularlywhen
conditionsoftheCreativeCommons correlationisinterpretedasaproxyforsignalcontent.
Attribution(CCBY)license.
Mathematics2026,14,752 https://doi.org/10.3390/math14050752

Mathematics2026,14,752 2of27
This paper uncovers another set of paradoxical results, involving the relationship
between the correlation of a forecast with the target variable and Mean Directional Ac-
curacy(MDA).Weshowthat,undercertainconditions,aforecastthatismorestrongly
correlatedwiththetargetmaydeliverworsesignpredictionsthanalesscorrelatedalter-
native. Inotherwords, improvementsincorrelationmaycoincidewithadeterioration
indirectionalperformance.
WithinaGaussianframework,wederiveanalyticalexpressionsthatclarifythisphe-
nomenon. Inparticular,weshowthatsignpredictabilitydependsnotonlyonthecorre-
lationbetweentheforecastandthetargetvariable,butalsoontheirstandardizedmeans,
a result that partly echoes the findings of [9]. These additional dimensions of forecast
behaviormaydistorttherelationshipbetweencorrelationanddirectionalaccuracy. Asa
consequence,highercorrelationdoesnotguaranteesuperiorMDA,andinsomeregions
of the parameter space, the relationship can even reverse. An empirical application to
exchangerateforecastingillustratesthattheseparadoxesarenotmerelytheoreticalcuriosi-
ties, but empirically relevant phenomena that can affect forecast evaluation and model
selectioninpractice.
Itisimportanttoemphasizethat[9]primarilyfocusesonwhattheydescribeas“the
subtleandlittle-understoodconnectionbetweensigndynamicsandvolatilitydynamics”,
asdiscussedonpage1276. Ourfocusisdifferent. Westudytherelationshipbetweensign
predictability,asmeasuredbyMDA,andthecorrelationbetweentheforecastandthetarget
variable, a connection that, to our knowledge, has not been explicitly examined in the
existingliterature.
Therestofthispaperisorganizedasfollows: Section2presentstheanalyticalframe-
work. Section3derivesadecompositionofMDAintermsofthecorrelationbetweenthe
forecastandthetargetvariable. Inthatsection,wealsoprovideseveralanalyticalexamples
inwhichtheMDAParadoxarises. Section4derivesformalconditionsunderwhichthe
MDAParadoxcannotoccur,includingthecaseofMincer–Zarnowitz[10]efficientforecasts.
Section5presentsanempiricalillustration,andSection6concludesthestudy.
2. AnalyticalFramework
LetP denotethetimeseriesofinterest,whichweassumetobeintegratedoforderone,
t
i.e.,I(1). Ourprimaryfocusisonthevariationinthistimeseriesoveraforecasthorizon
h, that is, the change between t and t + h. For notational simplicity, we assume in the
theoreticalsectionsofthispaperthath=1(intheempiricalillustration,weconsiderlonger
horizonsaswell). Accordingly,wedefinethefirstdifferenceas
Y t+1 = P t+1 −P t
Under the I(1) assumption on P t , the series Y t+1 is stationary. At time t, we con-
sidertwocompetingforecastsforY t+1 :X t andZ t . Theseforecastsareconstructedusing
information available at time t, and they are treated as primitives. That is, we do not
modeltheprocessbywhichtheseforecastsaregenerated,nordoweaccountforparameter
estimation uncertainty. In this respect, our framework is similar in spirit to the setup
in [11], which is further emphasized in [12]. (Forecast evaluation has been extensively
reviewed by [13,14]. The literature on nested model comparisons has evolved through
thecontributionsof[15–19],withmorerecentinsightsprovidedby[20]. Atthepopulation
level,Ref.[21]discussestheimplicationsofparameteruncertainty,whileRef.[22]provides
acornerstoneframeworkforevaluatingpredictiveabilityinfinite-sampleandundercon-
ditionalsettings.) Forclarityofexposition,wedropthetimesubscripttinwhatfollows.
Wewillalsoassumethatthejointvector(Y,X,Z)isweaklystationary,ergodicandjointly
normallydistributed. WhiletheGaussianassumptionmayappearrestrictive,itprovides
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 3of27
analyticalclarityandtractability. Moreover,itmayofferareasonableapproximationto
thedistributionofactualfinancialreturnsatmediumtolonghorizons. Whileshort-term
returnsaretypicallycharacterizedbyfat-taileddistributions,longer-horizonlogreturns
canbeviewedasaveragesofshorter-termreturns. BytheCentralLimitTheorem,thisag-
gregationprocessjustifiestheuseoftheGaussianassumptionasaplausibleapproximation
forbothlong-runreturnsandtheirforecasts.
WealsoshowresultsforefficientforecastsintheMincer–Zarnowitz[10]sense,thatis,
unbiasedforecastswhoseerrorsareuncorrelatedwiththeinformationavailableatthetime
theyaremade. Thisorthogonalityconditionensuresthatnoobviouspredictablestructure
remainsintheforecasterrorsandisparticularlyrelevanttoouranalysis.Mincer–Zarnowitz
efficiency plays a central role in preventing the MSPE Paradox from arising. Here, we
also examine whether Mincer–Zarnowitz efficiency is sufficient to prevent paradoxical
discrepanciesbetweenMDAandcorrelation-basedmeasuresofforecastperformance. For
doingso,itisconvenienttorecalltheexactdefinitionofMincer–Zarnowitzefficiencyand
toseehowitlooksinourframework.
Remark: Mincer–Zarnowitz[10]efficiency. A forecast Yf is said to be Mincer–
Zarnowitzefficientifithasnobiasanditisauto-efficient. AforecastYf isunbiasedwhen
(cid:16) (cid:17) (cid:16) (cid:17)
E Y−Yf =0. AforecastYf isauto-efficientwheneverCov Y−Yf,Yf =0;otherwise,
itissaidtobeauto-inefficient.
Inourcontext,inwhichwehavetwoforecastsXandZforthesametargetvariableY,
theywillbeunbiasediftheirexpectedvaluesµ andµ coincidewiththeexpectedvalue
X Z
ofY,whichwewilldenoteµ . So,unbiasednessmeans
Y
µ = µ = µ
X Z Y
Xwillbeauto-efficientaslongas
σ
Cov(Y−X,X) =0⇐⇒Cov(Y,X) =V(X) ⇐⇒ ρ = X ,
YX
σ
Y
where ρ denotes the correlation between forecast X and Y, and σ , σ represent the
YX X Y
standarddeviationsofXandYrespectively. ApplyingthesamereasoningtoforecastZ,we
havethatZwillbeauto-efficientaslongas
σ
ρ = Z ,
YZ
σ
Y
where ρ denotes the correlation between forecast Z and Y, and σ , σ represent the
YZ Z Y
standard deviations of Z and Y respectively. In the next section, we present our first
propositionandasetofexamplesillustratingtheMDAParadox.
3. TheMDAParadox: AKeyResultandaFewExamples
3.1. MDADifferentials
Proposition 1 reveals that MDA differentials reflect features of the bivariate joint
distributionsbetweenthetargetandeachforecast,includingtheircorrelationstructure.
Proposition1. LetYbeatargetvariablewithexpectedvalueµ andstandarddeviationσ >0.
Y Y
Consider two forecasts X and Z with expected values µ and µ and positive standard devia-
X Z
tionsσ andσ respectively. ThecorrelationbetweenYandforecastXisdenotedbyρ ,whereas
X Z YX
thecorrelationbetweenYandforecastZisdenotedbyρ . Wewillalsoassumejointnormalityfor
YZ
thevector(Y,X,Z).Then,thedifferenceinMDAbetweenforecastXandZcanbeexpressedas
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 4of27
(cid:18) (cid:19) (cid:18) (cid:19) (cid:20) (cid:18) (cid:19) (cid:18) (cid:19)(cid:21)
µ µ µ µ µ µ
MDA −MDA = Φ − Z −Φ − X +2 Φ − Y ,− X ;ρ −Φ − Y ,− Z ;ρ (1)
X Z 2 YX 2 YZ
σ σ σ σ σ σ
Z X Y X Y Z
whereΦdenotesthecdfofastandardnormaldistributionandΦ (a,b;ρ)representsthecdfofa
2
standardbivariatenormaldistributionevaluatedatthepoint(a,b)andwithcorrelationcoefficientρ.
ProofofProposition1. WebeginbyexpressingtheMeanDirectionalAccuracy(MDA)
associatedwithforecastX:
MDA =Pr(YX >0) =Pr(Y >0,X >0)+Pr(Y ≤0,X ≤0)
X
Definingthestandardizedvariables
∼ Y−µ ∼ X−µ ∼ Z−µ
Y = Y ; X = X ; Z = Z ,
σ σ σ
Y X Z
wehave
Pr(Y>0,X>0) =Pr (cid:18) Y ∼ > − µ Y ,X ∼ > − µ X (cid:19) =Pr (cid:16) A (cid:92) B (cid:17) ,
σ σ
Y X
where
(cid:26)∼
µ
(cid:27) (cid:26)∼
µ
(cid:27)
A = Y > − Y andB = X > − X
σ σ
Y X
Applyingthestandardprobabilityidentity
Pr (cid:16) A (cid:92) B (cid:17) =1−Pr (cid:16) AC (cid:17) −Pr (cid:16) BC (cid:17) +Pr (cid:16) AC(cid:92) BC (cid:17) ,
whereAC=Ω\A;wehavethat
Pr(Y>0,X>0) =Pr (cid:16) A (cid:92) B (cid:17) =1−Φ (cid:18) − µ Y (cid:19) −Φ (cid:18) − µ X (cid:19) +Φ (cid:18) − µ Y ,− µ X ;ρ (cid:19) ,
2 YX
σ σ σ σ
Y X Y X
whereΦdenotesthecdfofastandardnormaldistributionandΦ representsthecdfofa
2
standardbivariatenormaldistributionwithcorrelationcoefficientρ . Therefore
YX
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
µ µ µ µ
MDA =1−Φ − Y −Φ − X +2Φ − Y ,− X ;ρ .
X 2 YX
σ σ σ σ
Y X Y X
Thisexpressionresemblestheresultshownin[1],butnow,makingexplicittherelation-
shipbetweenMDAandthepopulationparametersofthemarginalandjointdistributions.
ByapplyingthesamereasoningtoforecastZ,weobtain
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
µ µ µ µ
MDA =1−Φ − Y −Φ − Z +2Φ − Y ,− Z ;ρ
Z 2 YZ
σ σ σ σ
Y Z Y Z
SubtractingtheexpressionsforMDA andMDA ,wefind
X Z
(cid:18) (cid:19) (cid:18) (cid:19) (cid:20) (cid:18) (cid:19) (cid:18) (cid:19)(cid:21)
µ µ µ µ µ µ
MDA −MDA = Φ − Z −Φ − X +2 Φ − Y ,− X ;ρ −Φ − Y ,− Z ;ρ ,
X Z 2 YX 2 YZ
σ σ σ σ σ σ
Z X Y X Y Z
□
whichconcludeswiththeproof.
NoticethatExpression(1)isequivalentto
https://doi.org/10.3390/math14050752

Mathematics2026,14,752
5of27
|          |     | (cid:18) (cid:19) | (cid:18) | (cid:19) | (cid:20) | (cid:18) |      | (cid:19) | (cid:18) |      |      | (cid:19)(cid:21) |
| -------- | --- | ----------------- | -------- | -------- | -------- | -------- | ---- | -------- | -------- | ---- | ---- | ---------------- |
|          |     | µ                 |          | µ        |          | µ        | µ    |          |          | µ    | µ    |                  |
| MDA −MDA | =   | Φ X               | −Φ       | Z        | +2 Φ     | − Y      | ,− X | ;ρ       | −Φ −     | Y ,− | Z ;ρ | ,                |
| X        | Z   |                   |          |          | 2        |          |      | YX       | 2        |      | YZ   |                  |
|          |     | σ X               |          | σ Z      |          | σ Y      | σ X  |          |          | σ Y  | σ Z  |                  |
butwepreferthenotationofExpression(1)whichkeepsthenegativesignsinalltheterms
includingthoseonthebivariatedistribution. Expression(1)isimportantbecauseitbreaks
downthedifferenceinMDAasthesumoftwocomponentsP1andP2,where
|     |     |     |     |      |                   |       | (cid:18) µ | (cid:19) | (cid:18) µ (cid:19) |       |                  |     |
| --- | --- | --- | --- | ---- | ----------------- | ----- | ---------- | -------- | ------------------- | ----- | ---------------- | --- |
|     |     |     |     |      |                   | P1≡ Φ | − Z        | −Φ       | − X                 |       |                  |     |
|     |     |     |     |      |                   |       | σ          |          | σ                   |       |                  |     |
|     |     |     |     |      |                   |       | Z          |          | X                   |       |                  |     |
|     |     |     |     |      | (cid:20) (cid:18) |       |            | (cid:19) | (cid:18)            |       | (cid:19)(cid:21) |     |
|     |     |     |     |      | Φ                 | µ Y   | µ X        | −Φ       | µ Y                 | µ Z   |                  |     |
|     |     |     |     | P2≡2 | −                 | ,−    | ;ρ         |          | −                   | ,− ;ρ |                  |     |
|     |     |     |     |      | 2                 | σ     | σ YX       |          | 2 σ                 | σ     | YZ               |     |
|     |     |     |     |      |                   | Y     | X          |          | Y                   | Z     |                  |     |
The first component is just a function of the standardized means of the forecasts
µX µZ).Itdoesnotinvolveanymeasureofstatisticalconnectionbetweentheforecasts
( or
σX σZ
and the target variable. Yet, as we will see along our paper, this first term may play a
criticalroleindeterminingMDAdifferentials. ThesecondtermP2contains: measuresof
dependencebetweenforecastsandthetargetvariableandthestandardizedmeansofboth
theforecastsandthetargetvariable. Allthesethreesubcomponentsplayacrucialrolein
determiningthemagnitudeandsignofP2. Thisisthetermwherecorrelationsbetween
theforecastsandthetargetvariablecanexertasignificantinfluence,substantialinsome
contexts,yetsecondarytotheeffectsofthestandardizedmeansofthecompetingforecasts
inothers(amoregeneralExpression(1)canbederivedwithouttheGaussianassumption:
|     |     |      |     | (cid:18) | µ (cid:19) | (cid:18) | µ (cid:19) | (cid:20) | (cid:18) µ | µ   | (cid:19) | (cid:18) µ µ (cid:19)(cid:21) |
| --- | --- | ---- | --- | -------- | ---------- | -------- | ---------- | -------- | ---------- | --- | -------- | ----------------------------- |
|     |     |      |     |          | Z          |          | X          |          | Y,−        | X   |          | Y,− Z                         |
|     | MDA | −MDA |     | =F ∼     | −          | −F ∼     | −          | +2 F     | ∼ ∼ −      |     | −F ∼     | ∼ −                           |
|     |     | X    | Z   |          | σ          |          | σ          |          | σ          | σ   |          | σ σ                           |
|     |     |      |     | Z        | Z          | X        | X          |          | Y X Y      | X   | Y        | Z Y Z                         |
where F∼ and F∼ denote standardized marginal cdfs, whereas F∼∼ and F∼∼ represent
|     |     | X   |     | Z   |     |     |     |     |     |     | YX  | YZ  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
standardizedbivariatedistributions.
Thefollowinglemmaiswell-knownintheliterature,seeforinstance,Refs.[23,24].
However,givenitsimportanceforourresults,wepresentithereandprovideathorough
proofinAppendixA.
Lemma1. LetΦ (a,b;ρ)denotethecumulativedistributionfunctionofthestandardbivariate
2
1),evaluatedatthefixedpoint(a,b)∈R2.
|     | normaldistributionwithcorrelationcoefficientρ |     |     |     |     |     |     | ∈ (−1, |     |     |     |     |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
ThenΦ
2 (a,b;ρ)isdifferentiablewithrespecttoρ,anditsderivativeisgivenbythevalueofthe
jointdensityatthepoint(a,b):
|     |     |     |     |     |     | ∂Φ  | (a,b;ρ) |              |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | --- | --- | --- |
|     |     |     |     |     |     | 2   |         | = ϕ (a,b;ρ), |     |     |     |     |
2
∂ρ
whereϕ (a,b;ρ)isthestandardbivariatenormaldensityfunction
2
|     |     |                     |     |         |           |             | (cid:18) |         |             |                 | (cid:105)(cid:19) |             |
| --- | --- | ------------------- | --- | ------- | --------- | ----------- | -------- | ------- | ----------- | --------------- | ----------------- | ----------- |
|     |     |                     |     |         |           | 1           |          |         | 1 (cid:104) |                 |                   |             |
|     |     |                     | ϕ   | (a,b;ρ) | =         |             | exp      | −       | a2−2ρab+b2  |                 |                   |             |
|     |     |                     |     | 2       |           | (cid:112)   |          |         |             |                 |                   |             |
|     |     |                     |     |         | 2π        | 1−ρ2        |          | 2(1−ρ2) |             |                 |                   |             |
|     |     |                     |     |         |           | >0foralla,b |          | ∈R      | ∈ (−1,      | 1),thefunctionΦ |                   |             |
|     |     | Inparticular,sinceϕ |     |         | 2 (a,b;ρ) |             |          |         | anρ         |                 |                   | 2 (a,b;ρ)is |
strictlyincreasinginρ.
□
|     | ProofofLemma1. |     |     | AppendixA. |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Inwhatfollows,afewformaldefinitionsareinorder.
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 6of27
• WewillsaythattheMDAParadoxoccursinaweaksensewheneverρ = ρ and
YX YZ
MDA ̸= MDA .
X Z
• WewillsaythattheMDAParadoxoccursinastrongsensewheneverρ > ρ and
YX YZ
MDA < MDA ;orwheneverρ < ρ and MDA > MDA .
X Z YX YZ X Z
• WewillsaythattheMDAParadoxdoesnotoccurwhenever(ρ −ρ )(MDA −MDA )
YX YZ X Z
>0sothatcorrelationsandMDAareverymuchaligned.
• Werefertoapureluckbenchmarkasaforecastthatisindependentofthetargetvariable
YandyieldsanMDAof0.5.
3.2. AFewParticularCasesinWhichtheMDAParadoxEmerges
3.2.1. CorrelationIrrelevance
LetXandZbetwoforecastsforthesametargetvariableY,suchthatρ > ρ . Let
YX YZ
usfurtherassumethatµ
̸=0andthat|µY|isbig.
Y σY
Ifµ >0,thenwewillhave
Y
(cid:18) (cid:19) (cid:18) (cid:19)
µ µ µ µ
Φ − Y ,− X ;ρ ≈0; Φ − Y ,− Z ;ρ ≈0
2 YX 2 YZ
σ σ σ σ
Y X Y Z
Therefore
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
µ µ µ µ
MDA −MDA ≈ Φ − Z −Φ − X = Φ X −Φ Z ,
X Z
σ σ σ σ
Z X X Z
anddifferencesinMDAwillnotdependonthecorrelationsbetweentheforecastsandthe
targetvariable.
Ifµ <0then
Y
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
µ µ µ µ µ µ
Φ − Y ,− X ;ρ ≈ Φ − X ; Φ − Y ,− Z ;ρ ≈ Φ − Z .
2 YX 2 YZ
σ σ σ σ σ σ
Y X X Y Z Z
Therefore
(cid:18) (cid:19) (cid:18) (cid:19) (cid:20) (cid:18) (cid:19) (cid:18) (cid:19)(cid:21)
µ µ µ µ
MDA −MDA ≈ Φ − Z −Φ − X +2 Φ − X −Φ − Z ,
X Z
σ σ σ σ
Z X X Z
so
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
µ µ µ µ
MDA −MDA ≈ Φ − X −Φ − Z = Φ Z −Φ X
X Z
σ σ σ σ
X Z Z X
andagain,differencesinMDAwillnotdependonthecorrelationsbetweentheforecasts
andthetargetvariable. Paradoxicalresultsemergewhenever
µ µ
X < Z ifµ >0
Y
σ σ
X Z
or
µ µ
Z < X ifµ <0
Y
σ σ
Z X
Moreover, paradoxical results emerge even when both forecasts are unbiased:
µ = µ = µ . In this case, they arise whenever σ < σ . Let us illustrate with a
Y X Z Z X
numericalexamplehowtheParadoxemergesinthisscenarioevenwhenhavingunbiased
forecasts. Letussupposethat: µ = µ = µ =0.5; µY =2, µX =0.125and µZ =0.5so
Y X Z σY σX σZ
thatσ =1< σ =4. Wewillalsoassumeρ =0.35> ρ =0.25.Inthiscase,wehave
Z X YX YZ
MDA =1−Φ(−2)−Φ(−0.125)+2Φ (−2,−0.125;0.35) ≈0.56
X 2
MDA =1−Φ(−2)−Φ(−0.5)+2Φ (−2,−0.5;0.25) ≈0.69
Z 2
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 7of27
so that we clearly have a paradoxical case, in which ρ = 0.35 > ρ = 0.25 yet
YX YZ
(cid:16) (cid:17) (cid:16) (cid:17)
MDA ≈ 0.56 < MDA ≈ 0.69.NoticealsothatΦ −µZ −Φ −µX ≈ −0.14,which
X Z σZ σX
showsthattheapproximation
(cid:18) (cid:19) (cid:18) (cid:19)
µ µ
MDA −MDA ≈ Φ − Z −Φ − X
X Z
σ σ
Z X
isrelativelyaccurateinthiscase.
3.2.2. TwoIndependentForecasts
LetXandZbetwoindependentforecastsforthesametargetvariableY.Thismeans
ρ = ρ =0
YX YZ
Thisimplies
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
µ µ µ µ µ µ µ µ
Φ − Y ,− X ;0 = Φ − Y Φ − X ; Φ − Y ,− Z ;0 = Φ − Y Φ − Z
2 2
σ σ σ σ σ σ σ σ
Y X Y X Y Z Y Z
Therefore,Expression(1)becomes
(cid:18) (cid:19) (cid:18) (cid:19) (cid:20) (cid:18) (cid:19)(cid:20) (cid:18) (cid:19) (cid:18) (cid:19)(cid:21)(cid:21)
µ µ µ µ µ
MDA −MDA = Φ − Z −Φ − X +2 Φ − Y Φ − X −Φ − Z ,
X Z
σ σ σ σ σ
Z X Y X Z
so
(cid:20) (cid:18) (cid:19) (cid:18) (cid:19)(cid:21)(cid:20) (cid:18) (cid:19)(cid:21)
µ µ µ
MDA −MDA = Φ − Z −Φ − X 1−2Φ − Y
X Z
σ σ σ
Z X Y
and
µ µ
MDA −MDA =0⇐⇒ Z = X orµ =0 (2)
X Z Y
σ σ
Z X
Iftheconditionsintheright-handsideof(2)donothold,thenwewillhaveparadoxical
results because the difference in correlations is exactly zero (ρ −ρ = 0) yet the
YX YZ
difference in MDA will be different from zero. As a matter of fact, we will have the
followingresults
µ µ
If µ >0thenMDA −MDA >0⇐⇒ Z < X
Y X Z σ σ
Z X
µ µ
If µ <0thenMDA −MDA >0⇐⇒ Z > X
Y X Z σ σ
Z X
Insummary,withtwoindependentforecasts,theconditionsontheright-handside
of(2)areenoughtoavoidanyparadoxicalresults. Nevertheless,iftheyarenotsatisfied,
thenparadoxicalresultswillsurelyemergeinaweaksense. Toillustratewithanumerical
example,letussupposethat µY = µZ =1,andthat µX =0. Giventhattheconditionson
σY σZ σX
theright-handsideof(2)donothold,wewillhaveparadoxicalresultsinaweaksense. As
amatteroffact,inthiscaseitisverysimpletoevaluateMDAdifferentials:
(cid:104) (cid:16) (cid:17) (cid:16) (cid:17)(cid:105)(cid:104) (cid:16) (cid:17)(cid:105)
MDA −MDA = Φ −µZ −Φ −µX 1−2Φ −µY
X Z σZ σX σY
= [Φ(−1)−Φ(0)][1−2Φ(−1)] = −0.233
So, inthisnumericalexample, forecastZismuchmoreaccuratethanforecastXin
termsofMDA.Thecomputeddifferenceof−0.233isexplainedbecauseXhasanMDAof
0.5,whereasZhasanMDAof0.733.
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 8of27
3.2.3. OneIndependentForecastwithPositiveVariance
LetXandZbetwoforecastsforthesametargetvariableY,butletusfurtherassume
thatZisindependentfromYandthatXispositivelycorrelatedwithY.Thisimplies
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
µ µ µ µ
ρ =0; 0< ρ <1andΦ − Y ,− Z ;0 = Φ − Y Φ − Z
YZ YX 2 σ σ σ σ
Y Z Y Z
Undertheseconditions,Expression(1)becomes
(cid:18) (cid:19) (cid:18) (cid:19) (cid:20) (cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)(cid:21)
µ µ µ µ µ µ
MDA −MDA = Φ − Z −Φ − X +2 Φ − Y ,− X ;ρ −Φ − Y Φ − Z ,
X Z 2 YX
σ σ σ σ σ σ
Z X Y X Y Z
so
(cid:18) (cid:19)(cid:20) (cid:18) (cid:19)(cid:21) (cid:18) (cid:19) (cid:18) (cid:19)
µ µ µ µ µ
MDA −MDA = Φ − Z 1−2Φ − Y −Φ − X +2Φ − Y ,− X ;ρ (3)
X Z 2 YX
σ σ σ σ σ
Z Y X Y X
Interestingly, Lemma 1 teaches us that Expression (3) is an increasing function of
thecorrelationρ ,andgiventhatweareassumingρ = 0,weconcludethat(3)isan
YX YZ
increasingfunctionofthedifferenceρ −ρ . Notwithstanding,Expression(3)canbe
YX YZ
negativeifthefollowingterm
(cid:18) (cid:19)(cid:20) (cid:18) (cid:19)(cid:21) (cid:18) (cid:19)
µ µ µ
Φ − Z 1−2Φ − Y −Φ − X
σ σ σ
Z Y X
isnegativeenoughtocompensateforthepositiveterm
(cid:18) (cid:19)
µ µ
2Φ − Y ,− X ;ρ
2 YX
σ σ
Y X
When this happens, we will have a case of strong MDA Paradox, as a positively
correlated forecast X will be outperformed by a completely independent forecast Z in
directionalaccuracy. Givenvaluesof
µZ
and
µY,equatingExpression(3)tozerodefinesan
implicitfunctionofthecorrelationρ
σZ
interm
σY
softhestandardizedmean
µX.
Specifically,
YX σX
bysettingMDA −MDA =0,weget:
X Z
(cid:18) (cid:19) (cid:18) (cid:19)(cid:20) (cid:18) (cid:19)(cid:21) (cid:18) (cid:19)
µ µ µ µ µ
Φ − X −Φ − Z 1−2Φ − Y =2Φ − Y ,− X ;ρ
2 YX
σ σ σ σ σ
X Z Y Y X
Intheparticularcaseinwhich µZ = µY,thepreviousexpressionreducesto
σZ σY
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
µ µ µ µ µ
2Φ2 − Y −Φ − Y +Φ − X =2Φ − Y ,− X ;ρ (4)
2 YX
σ σ σ σ σ
Y Y X Y X
Thisrelationimplicitlydefinesathresholdfunctionρ∗(µX/σX )representing,foreach
µX/σX ,theminimumcorrelationbetweenXandYrequiredfortheforecastXtomatchthe
directionalaccuracyoftheuninformedbenchmarkZ:
• Ifρ
YX
> ρ∗(µX/σX ), thenMDA
X
>MDA
Z
;
• Ifρ
YX
< ρ∗(µX/σX ), thenMDA
X
<MDA
Z
.
Every time 0 < ρ
YX
< ρ∗(µX/σX ), we will have a case of strong MDA Paradox in
whichXisoutperformedintermsofMDAbyZ.(Strictlyspeaking,thefunctionρ∗(µX/σX )
isdefinedonlyintheimplicitdomainwheretheleft-handsideof(4)fallswithintherange
(cid:16) (cid:17)
attainablebytheright-handside,asρvariesin(−1,1). SinceΦ −µY,−µX;ρ iscontin-
2 σY σX YX
(cid:110) (cid:16) (cid:17) (cid:16) (cid:17) (cid:111)
uousandstrictlyincreasinginρ ,thisrequiresthat2max 0,Φ −µY +Φ −µX −1 ≤
YX σY σX
https://doi.org/10.3390/math14050752

Mathematics2026,14,752
9of27
| (cid:16) (cid:17) | (cid:16) | (cid:17) | (cid:16) (cid:17) | (cid:110) | (cid:16) | (cid:17) (cid:16) | (cid:17)(cid:111) |
| ----------------- | -------- | -------- | ----------------- | --------- | -------- | ----------------- | ----------------- |
Φ −µX −Φ −µY +2Φ2 −µY ≤ 2min Φ −µY ,Φ −µX . Itisonlyunderthese
| σX  |     | σY  | σY  |     | σY  |     | σX  |
| --- | --- | --- | --- | --- | --- | --- | --- |
conditionsthatauniquethresholdρ∗(µX/σX )existsin(−1,1). Furthermore,itcanbeshown
thatρ∗(µX/σX
|     | )isamonotonicfunctionofµX/σX |     |     |     | .   |     |     |
| --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
Figure1depictsthesethresholdfunctionsforvariouslevelsofµY/σY . Theshadedarea
>
ineachfigurerepresentsParadoxzones. Inparticular,whenρ YX 0,theseareareasin
whichthereisapositivecorrelationbetweenforecastXandY,yetthiscorrelationisnot
largeenoughtomatchtheMDAoftheuninformativebenchmarkZ.

Figure1.ThresholdcorrelationforavoidingtheMDAParadox.Thefiguredepicts,forvariouslevels
ofµ /σ ,theexactcorrelationthataforecastXmusthavewiththetargetvalueY,inordertoachieve
Y Y
thesameMDAastheuninformativebenchmarkforecastZ,whichsatisfiesµ Z /σ Z =µ Y /σ Y .Shaded
areasrepresentParadoxzones.
µX µY,reflecting
| Notably,asshownbyFigure1,thethresholdequalszerowhen |     |     |     |     |     |     | =   |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
σX σY
thataforecastwiththesamestandardizedmeanasthetargetonlyneedstoexhibitpositive
dependencewithYtoimproveuponanuninformativepredictorZthatisalsorelatively
| unbiased( | µZ = | µY). |     |     |     |     |     |
| --------- | ---- | ---- | --- | --- | --- | --- | --- |
σZ σY
LetusillustrateacaseofstrongMDAParadoxwithanumericalexampleinwhich
| µY µZ | µX  |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- |
= = 1, = 0.25and ρ = 0.25.AccordingtoFigure1(rightinferiorcorner),
| σY σZ | σX  |     | YX  |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- |
forecastXwillbeoutperformedbyforecastZinMDAdespitehavingalargercorrelation
| withthetargetvariable. |     |                      | Letuscomputetheexactnumbers: |     |                 |           |        |
| ---------------------- | --- | -------------------- | ---------------------------- | --- | --------------- | --------- | ------ |
|                        |     |                      | =1−Φ(−1)−Φ(−1)+2Φ            |     |                 | (−1,−1;0) | =0.733 |
|                        |     | MDA Z                |                              |     | 2               |           |        |
|                        |     | =1−Φ(−1)−Φ(−0.25)+2Φ |                              |     | (−1,−0.25;0.25) |           | =0.616 |
|                        | MDA | X                    |                              |     | 2               |           |        |
ThesenumbersareconsistentwithFigure1andshowastrongcaseofMDAParadox,
inwhichatotallyindependentforecastZdisplaysahigherMDArelativetoaforecastX
positivelycorrelatedwiththetarget.
3.2.4. TwoExtremelyBiasedForecastswithPositiveCorrelationwiththeTarget
Let us suppose now that both X and Z have a positive correlation with the target
variableY.Letusalsoassumethat µX ≫0and µZ ≪0. Inotherwords,thestandardized
|     |     |     | σX  |     | σZ  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
meanofXispositiveandverybig,whereasthestandardizedmeanofZisnegativeand
verybiginabsolutevalue. Then,theunivariatetermsinExpression(1)satisfies
|     |     |     | (cid:18) µ (cid:19) |     | (cid:18) µ | (cid:19) |     |
| --- | --- | --- | ------------------- | --- | ---------- | -------- | --- |
|     |     |     | Φ X                 | Φ   | Z          |          |     |
|     |     |     | −                   | ≈0; | −          | ≈1       |     |
|     |     |     | σ                   |     | σ          |          |     |
|     |     |     | X                   |     | Z          |          |     |
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 10of27
So,thefirstterm(P1)inMDA −MDA iscloseto1. Forthebivariatenormalterms,
X Z
wehave
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
µ µ µ µ µ
Φ − Y ,− X ;ρ ≈0; Φ − Y ,− Z ;ρ ≈ Φ − Y
2 YX 2 YZ
σ σ σ σ σ
Y X Y Z Y
Therefore,theentireexpressionsatisfies
(cid:18) (cid:19) (cid:18) (cid:19)
µ µ
MDA −MDA ≈1−2Φ − Y =2Φ Y −1
X Z
σ σ
Y Y
Inthisextremecase,thepotentialdependenceofeachforecastonthetargetvariable
playsnoroleindeterminingdifferencesinMDA.Theonlysubcomponentsplayingim-
portantrolesarethestandardizedmeans
µX, µZ
and
µY.Ontheonehand,whenthislatter
σX σZ σY
ratioispositive:
MDA −MDA >0
X Z
indicating that X outperforms Z in correctly predicting the direction of Y. On the other
hand,when
µY
isnegative,
σY
MDA −MDA <0
X Z
indicatingthatZoutperformsXincorrectlypredictingthedirectionofY.Noticethatthisis
irrespectiveoftherelativemagnitudesofρ andρ . Here,paradoxicalresultsemerge
YX ZX
withclarityastheonlyrelevanttermsdeterminingMDA −MDA arethestandardized
X Z
meansofourforecastsandtargetvariable.
Letusillustratethisscenariowithanumericalexampleinwhich µY = −0.25; µZ =
−2, µX =2,ρ =0.25andρ =0.75.Letuscomputetheexactnumb
σY
ers
σZ
σX YZ YX
MDA =1−Φ(0.25)−Φ(2)+2Φ (0.25,2;0.25) =0.61
Z 2
MDA =1−Φ(0.25)−Φ(−2)+2Φ (0.25,−2;0.75) =0.43
X 2
ThesenumbersvividlyshowastrongcaseofMDAParadox: althoughforecastZhas
theweakestcorrelationwithY,itexhibitsanMDAof0.61,wellabovethe0.43observedfor
X,theforecastwiththehighestcorrelationwiththetargetvariable.
3.2.5. AConstantForecastvs. aForecastwithPositiveVariance
LetXandZbetwoforecastsforthesametargetvariableYwithµ ̸=0. Letusfurther
Y
assumethatZisaconstantcthatisindependentofY,whileXispositivelycorrelatedwith
thetargetvariable(ρ >0).ThisimpliesthatthecorrelationbetweenforecastZandYis
YX
notdefined. Nevertheless,ZandYareindependentwithzerocovariance. Thisexampleis
inspiredbyaliteraturethatfrequentlyusesaconstantforecastasatraditionalbenchmark
tocomparenewforecastingalternatives,suchas[25–28]. Wealreadyknowthat
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
µ µ µ µ
MDA =1−Φ − Y −Φ − X +2Φ − Y ,− X ;ρ
X 2 YX
σ σ σ σ
Y X Y X
But we need to derive an expression for MDA = Pr(YZ>0) = Pr(cY >0). It
Z
followsthat


Pr(Y >0)ifc >0
MDA =Pr(YZ>0) = 0ifc =0
Z
Pr(Y
<0)ifc <0
https://doi.org/10.3390/math14050752

Mathematics2026,14,752
11of27
Thisisequivalentto
|     |     |     |           |     |     |    | (cid:16) | (cid:17) (cid:16) | (cid:17) |     |
| --- | --- | --- | --------- | --- | --- | --- | -------- | ----------------- | -------- | --- |
|     |     |     |           |     |     | 1−Φ | −µ Y     | = Φ µ Y           | ifc >0   |     |
|     |     |     |           |     |     |  | σY       | σY                |          |     |
|     |     | MDA | =Pr(YZ>0) |     | =   |     |          | =0                |          |     |
|     |     |     | Z         |     |     |     | 0ifc     |                   |          |     |
|     |     |     |           |     |     |  | (cid:16) | (cid:17)          |          |     |
|     |     |     |           |     |     |     | Φ −µY    | <0                |          |     |
ifc
σY
So,aslongasc ̸= 0,thisconstantforecastwillhaveanMDAgreaterthan0.5ifthe
signofccoincideswiththesignoftheexpectedvalueofY.Toexplorepotentialparadoxical
| outcomes,wewillassumebothc |     |     |      |          | >0andµ   | >0.      |          |          |      |          |
| -------------------------- | --- | --- | ---- | -------- | -------- | -------- | -------- | -------- | ---- | -------- |
|                            |     |     |      |          |          | Y        | Wehave   |          |      |          |
|                            |     |     |      | (cid:18) | (cid:19) | (cid:18) | (cid:19) | (cid:18) |      | (cid:19) |
|                            |     |     |      | µ        |          | µ        |          | µ        | µ    |          |
|                            |     | MDA | =1−Φ | −        | Y −Φ     | − X      | +2Φ      | − Y ,−   | X ;ρ |          |
|                            |     |     | X    |          |          |          |          | 2        |      | YX       |
|                            |     |     |      | σ        |          | σ        |          | σ        | σ    |          |
|                            |     |     |      |          | Y        | X        |          | Y        | X    |          |
or
|     |     |     |     | (cid:18) (cid:19) | (cid:18) | (cid:19) |     | (cid:18) |      | (cid:19) |
| --- | --- | --- | --- | ----------------- | -------- | -------- | --- | -------- | ---- | -------- |
|     |     |     |     | Φ µ Y             | −Φ       | µ X      | +2Φ | µ Y      | µ X  |          |
|     |     | MDA | =   |                   |          | −        |     | − ,−     | ;ρ   |          |
|     |     |     | X   | σ                 |          | σ        | 2   | σ        | σ YX |          |
|     |     |     |     | Y                 |          | X        |     | Y        | X    |          |
Therefore
|     |     |      |     | (cid:18) (cid:19) | (cid:18) | (cid:19) | (cid:18) |        |      | (cid:19) (cid:18) (cid:19) |
| --- | --- | ---- | --- | ----------------- | -------- | -------- | -------- | ------ | ---- | -------------------------- |
|     |     |      |     | µ                 |          | µ        |          | µ µ    |      | µ                          |
| MDA |     | −MDA | =   | Φ Y               | −Φ       | − X +2Φ  |          | − Y ,− | X ;ρ | −Φ Y                       |
|     | X   |      | Z   |                   |          |          | 2        |        | YX   |                            |
|     |     |      |     | σ Y               |          | σ X      |          | σ Y σ  | X    | σ Y                        |
So,finally
|     |     |     |      |     |     | (cid:18) |     | (cid:19) | (cid:18) | (cid:19) |
| --- | --- | --- | ---- | --- | --- | -------- | --- | -------- | -------- | -------- |
|     |     |     |      |     |     | µ        | µ X |          | µ X      |          |
|     |     | MDA | −MDA |     | =2Φ | − Y ,−   | ;ρ  | −Φ       | −        |          |
|     |     |     | X    | Z   |     | 2        |     | YX       |          |          |
|     |     |     |      |     |     | σ Y      | σ X |          | σ X      |          |
It turns out that if µY −→ ∞ while keeping µX set at a fixed value, then
|          |     |     |          | σY  |     |     |     | σX  |     |     |
| -------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| (cid:16) |     |     | (cid:17) |     |     |     |     |     |     |     |
2Φ −µY,−µX;ρ
≈0and
| 2   | σY  | σX  | YX  |     |     |     |          |          |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | --- |
|     |     |     |     |     |     |     | (cid:18) | (cid:19) |     |     |
µ
|     |     |     |     |       | −MDA | ≈ −Φ | −   | X <0 |     |     |
| --- | --- | --- | --- | ----- | ---- | ---- | --- | ---- | --- | --- |
|     |     |     |     | MDA X |      | Z    |     |      |     |     |
σ
X
Therefore, a constant forecast, which is entirely independent of the target variable
Y, can nonetheless achieve higher MDA than a forecast X that is positively correlated
with Y. Let us illustrate with a numerical example this situation. Let us suppose that:
|     |     |     | µY  | µX  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
µ Y = µ X = µ Z = 0.5; = 0.5, = 0.125(sothat σ X =4) andc=µ Z = 0.5. Wewill
|     |     |     | σY  | σX  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
=0.25.Thisimplies
| alsoassumeρ |     | YX  |     |          |     |              |     |     |     |     |
| ----------- | --- | --- | --- | -------- | --- | ------------ | --- | --- | --- | --- |
|             |     |     |     | Cov(X,Y) |     | >0=Cov(Y,Z). |     |     |     |     |
Inthiscasewehave
=1−Φ(−0.5)−Φ(−0.125)+2Φ
|     | MDA |     |     |     |     |     | (−0.5,−0.125;0.25) |     |     | =0.59 |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | ----- |
|     |     | X   |     |     |     |     | 2                  |     |     |       |
=1−Φ(−0.5)
|     |     |     |     | MDA |     |     | =0.69 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
Z
so that we clearly have a paradoxical case, in which Cov(X,Y) > 0 = Cov(Y,Z), yet
| MDA | =0.59 | <MDA |     | =0.69. |     |     |     |     |     |     |
| --- | ----- | ---- | --- | ------ | --- | --- | --- | --- | --- | --- |
|     | X     |      | Z   |        |     |     |     |     |     |     |
3.2.6. AnIndependentForecastvs. aForecastwithPositiveVarianceandDownwardBias
LetXandZbetwoforecastsforthesametargetvariableY.Herewewillassumethat
ZandYareindependentandthatZhasapositivevarianceandzeromean: µ = 0.We
Z
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 12of27
willfurtherassumethatXispositivelycorrelatedwiththetargetvariable(ρ >0),and
YX
thatµ <0; µ >0 andthefollowingconditionholdstrue
X Y
(cid:18) (cid:19) (cid:18) (cid:19)
µ µ
Φ − X −Φ − Y >0.5
σ σ
X Y
Theseassumptionsmayseemarbitrary,yettheyaresimilartokeyfeaturesofourtime
seriesintheempiricalillustrationthatwepresentinSection5. Noticethatourassumptions
for Z and Y imply that Z coincides with a pure luck benchmark, that is, a forecast that
deliversanMDAof0.5. Toseethis,noticethat
(cid:16) (cid:17) (cid:16) (cid:17) (cid:16) (cid:17)
MDA =1−Φ −µY −Φ −µZ +2Φ −µY,−µZ;ρ
Z σY
(cid:16) (cid:17)
σZ
(cid:16)
2
(cid:17)
σY
(cid:16)
σZ
(cid:17)
YZ
(cid:16) (cid:17)
=1−Φ −µY −Φ −µZ +2Φ −µY Φ −µZ
(cid:16)
σY(cid:17) σZ
(cid:16) (cid:17)
σY σZ
=1−Φ −µY −Φ(0)+2Φ −µY Φ(0)
(cid:16)
σY
(cid:17) (cid:16) (cid:17)
σY
=0.5−Φ −µY +Φ −µY =0.5
σY σY
Withthisinmind,letusexplorewhatExpression(1)tellsusintheseconditions
(cid:16) (cid:17) (cid:16) (cid:17) (cid:104) (cid:16) (cid:17) (cid:16) (cid:17)(cid:105)
MDA −MDA = Φ −µ Z −Φ −µ X +2 Φ −µ Y,−µ X;ρ −Φ −µ Y,−µ Z;ρ
X Z σ σ 2 σ σ YX 2 σ σ YZ
(cid:16) (cid:17) (cid:104) (cid:16) Z X(cid:17) (cid:16) Y(cid:17)(cid:105) X Y Z
= 0.5−Φ −µ X +2 Φ −µ Y,−µ X;ρ −0.5Φ −µ Y
σ 2 σ σ YX σ
(cid:104) (cid:16) X (cid:17) (cid:16) (cid:17)Y(cid:105) X (cid:16) (cid:17)Y
= 0.5− Φ −µ X +Φ −µ Y +2Φ −µ Y,−µ X;ρ
σ σ 2 σ σ YX
X Y Y X
But,usingthatµ <0andµ >0,wehave
X Y
(cid:18) (cid:19) (cid:26) (cid:18) (cid:19) (cid:18) (cid:19)(cid:27) (cid:18) (cid:19)
µ µ µ µ µ
Φ − Y ,− X ;ρ ≤ min Φ − X ,Φ − Y = Φ − Y
2 YX
σ σ σ σ σ
Y X X Y Y
Therefore
(cid:20) (cid:18) (cid:19) (cid:18) (cid:19)(cid:21) (cid:18) (cid:19)
µ µ µ
MDA −MDA ≤0.5− Φ − X +Φ − Y +2Φ − Y
X Z
σ σ σ
X Y Y
So
(cid:18) (cid:19) (cid:18) (cid:19)
µ µ
MDA −MDA ≤0.5+Φ − Y −Φ − X <0
X Z
σ σ
Y X
Therefore, forecast Z, which is entirely independent of the target variable Y, can
nonethelessachievehigherMDAthanaforecastXthatispositivelycorrelatedwithY.Let
usillustratethiscasewithanumericalexample. Letussupposethat: µY =0.5, µX = −1
σY σX
andρ =0.5.Thisimplies
YX
(cid:18) (cid:19) (cid:18) (cid:19)
µ µ
Φ − Y =0.31, Φ − X =0.84
σ σ
Y X
and
MDA =1−Φ(−0.5)−Φ(1)+2Φ (−0.5,1;0.5) =0.44
X 2
MDA =0.5
Z
Soweclearlyhaveaparadoxicalcase,inwhichρ >0= ρ ,yetMDA =0.44 <
YX YZ X
MDA = 0.5.WewillreturntothiscaseinSection5,wherewediscusstheparadoxical
Z
resultsobservedinourempiricalapplication.
https://doi.org/10.3390/math14050752

Mathematics2026,14,752
13of27
4. ConditionsUnderWhichtheMDAParadoxIsImpossible
In this section we focus on establishing two results that provide different sets of
conditionsunderwhichtheMDAParadoxisimpossible. Wealsoshowaveryinteresting
proposition that allows for a simple computation of MDA differentials when forecasts
areunbiased andthetargetvariable haszeromean. Beforepresentingallthese results,
weshowandprovethefollowingLemma2,whichisverysimple,butweuseitlaterin
Proposition2.
Lemma2. LetΦ (a,b;ρ)denotethecumulativedistributionfunctionofthestandardbivariate
2
normaldistributionwithcorrelationcoefficientρ ∈ (−1, 1),evaluatedatthefixedpoint(a,b)∈
R2.Then
|     |     |     |     |            |        | (cid:32) |      | (cid:33) |     |     |
| --- | --- | --- | --- | ---------- | ------ | -------- | ---- | -------- | --- | --- |
|     |     |     |     | ∂Φ (a,b;ρ) |        |          | a−ρb |          |     |     |
|     |     |     |     | 2          | =ϕ(b)Φ |          |      |          |     |     |
(cid:112)
|     |     |     |     | ∂b  |     |     | 1−ρ2 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
ProofofLemma2. Let(X,Y)bearandomvectorthatfollowsastandardbivariatenormal
| distributionwithcorrelationcoefficientρ |     |     |     |            |          | ∈ (−1, 1). | Itfollowsthat |     |     |     |
| --------------------------------------- | --- | --- | --- | ---------- | -------- | ---------- | ------------- | --- | --- | --- |
|                                         |     |     |     |            | (cid:12) | (cid:16)   | (cid:17)      |     |     |     |
|                                         |     |     |     | X(cid:12)Y |          | ρy,1−ρ2    |               |     |     |     |
|                                         |     |     |     |            | (cid:12) | N          |               |     |     |     |
(cid:59)
Then
|     |     |     |     | (cid:32) |     |      |     | (cid:33) | (cid:32) | (cid:33) |
| --- | --- | --- | --- | -------- | --- | ---- | --- | -------- | -------- | -------- |
|     |     |     |     | X−ρy     |     | a−ρy |     |          | a−ρy     |          |
Φ
|     |     | Pr(X ≤ | a|Y = y) | =Pr       |      | ≤              | |Y  | = y = |                |     |
| --- | --- | ------ | -------- | --------- | ---- | -------------- | --- | ----- | -------------- | --- |
|     |     |        |          | (cid:112) | 1−ρ2 | (cid:112) 1−ρ2 |     |       | (cid:112) 1−ρ2 |     |
Therefore
|     |     |     |            |     |     |          |     | (cid:32) | (cid:33) |     |
| --- | --- | --- | ---------- | --- | --- | -------- | --- | -------- | -------- | --- |
|     |     |     | (cid:90) b |     |     | (cid:90) | b   | a−ρy     |          |     |
| Φ   |     |     |            |     |     |          | Φ   |          |          |     |
(a,b;ρ) =Pr(X ≤ a,Y ≤ b) = Pr(X ≤ a|Y = y)f (y)dy = (cid:112) f (y)dy
| 2   |     |     | −∞  |     | Y   |     | −∞  | 1−ρ2 | Y   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
and
|     |     |     |     |            |        | (cid:32) |      | (cid:33) |     |     |
| --- | --- | --- | --- | ---------- | ------ | -------- | ---- | -------- | --- | --- |
|     |     |     |     | ∂Φ (a,b;ρ) |        |          | a−ρb |          |     |     |
|     |     |     |     | 2          | =ϕ(b)Φ |          |      |          |     |     |
,
|                          |     |     |     | ∂b  |     |     | (cid:112) 1−ρ2 |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- |
| whichisthedesiredresult. |     |     |     | □   |     |     |                |     |     |     |
Thefollowingpropositionestablishesthat,underMincer–Zarnowitzefficiency,para-
doxicalresultswithrespecttoMDAandcorrelationscannotarise. Thisresultisinlinewith
theMSPEParadox,whichislikewiseimpossiblewhenforecastsareefficient(see[6,8]).
Proposition2.InthecontextofProposition1,ifbothforecastsXandZareMincer–Zarnowitz[10]
efficient,thatistosay
|     |     |       |        |     | σ     |     | σ   |       |        |     |
| --- | --- | ----- | ------ | --- | ----- | --- | --- | ----- | ------ | --- |
|     | µ   | = µ = | µ = µ, | ρ = | X ≥0, | ρ = | Z   | ≥0; ρ | <1andρ | <1  |
|     | X   | Z     | Y      | YX  |       | YZ  |     | YX    |        | YZ  |
|     |     |       |        |     | σ Y   |     | σ Y |       |        |     |
ThentheMDAParadoxisimpossible.
ProofofProposition2. WebeginbyexpressingtheMDAassociatedwithforecastX
|     |     |     |      | (cid:18) | (cid:19) | (cid:18) (cid:19) |     | (cid:18) |       | (cid:19) |
| --- | --- | --- | ---- | -------- | -------- | ----------------- | --- | -------- | ----- | -------- |
|     |     |     |      | µ        |          | µ                 |     | µ        | µ σ   | X        |
|     |     | MDA | =1−Φ | −        | −Φ       | −                 | +2Φ | − ,−     | ;     |          |
|     |     |     | X    |          |          |                   |     | 2        |       |          |
|     |     |     |      | σ Y      |          | σ X               |     | σ Y      | σ X σ | Y        |
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 14of27
Definethefunction
(cid:18) (cid:19) (cid:18) (cid:19)
µ µ σ µ
g(σ ) ≡2Φ − ,− ; X −Φ − ,
X 2 σ σ σ σ
Y X Y X
then
(cid:18) (cid:19)
µ
MDA =1−Φ − +g(σ )
X X
σ
Y
Bysymmetry,theMDAassociatedwithforecastZcanbewrittenas
(cid:18) (cid:19)
µ
MDA =1−Φ − +g(σ )
Z Z
σ
Y
Hence,
MDA −MDA = g(σ )−g(σ )
X Z X Z
Letuscontinueanalyzingthefunctiong(σ )keepinginmindthatthecaseofg(σ )
X Z
followsbysymmetry. Givenσ >0andµ ∈R ,g(σ )isanincreasingfunctionofσ . To
Y X X
seethis,wewillcomputeitsderivative
(cid:16) (cid:17) (cid:16) (cid:17)
∂g(σ X ) = g ′(σ ) = 2∂Φ 2 − σ µ Y ,− σ µ X ;σ σ X Y − ∂Φ − σ µ X
X
∂σ ∂σ ∂σ
X X X
ThederivativeoftheunivariateGaussiandistributionintheright-handsideisstraight-
forward:
(cid:16) (cid:17)
∂Φ − µ (cid:18) (cid:19)
σX
=ϕ −
µ µ
∂σ X σ X σ X 2
ForthederivativeofthebivariateGaussiandistribution,wehave
(cid:16) (cid:17)
2∂Φ 2 − σ µ Y ,− σ µ X ;σ σ X Y =2 (cid:20) ∂Φ 2 ∂b + ∂Φ 2 ∂ρ (cid:21)
∂σ ∂b ∂σ ∂ρ ∂σ
X X X
wherea = − µ ;b = − µ ,andρ = σX.
σY σX σY
FromLemmas1and2weobtain
∂Φ (a,b;ρ)
2 =ϕ (a,b;ρ)
∂ρ 2
(cid:32) (cid:33)
∂Φ (a,b;ρ) a−ρb
2 =ϕ(b)Φ
(cid:112)
∂b 1−ρ2
Furthermore
∂b µ b ∂ρ 1
= = − , =
∂σ X σ X 2 σ X ∂σ X σ Y
Therefore,wehave
(cid:34) (cid:32) a−ρb (cid:33) µ 1 (cid:35) (cid:18) µ (cid:19) µ
g ′(σ X ) =2 ϕ(b)Φ (cid:112) 1−ρ2 σ X 2 +ϕ 2 (a,b;ρ) σ Y −ϕ − σ X σ X 2 ,
orsimply
(cid:34) (cid:32) (cid:33) (cid:35)
a−ρb b 1 b
g ′(σ
X
) =2 −ϕ(b)Φ
(cid:112) 1−ρ2 σ
X
+ϕ
2
(a,b;ρ)
σ
Y
+ϕ(b)
σ
X
https://doi.org/10.3390/math14050752

Mathematics2026,14,752
15of27
Rearrangingtermswehave
|     |     |       |         | (cid:34) | (cid:32) |           | (cid:33)(cid:35) |     |         |     |     |
| --- | --- | ----- | ------- | -------- | -------- | --------- | ---------------- | --- | ------- | --- | --- |
|     |     |       |         | b        |          | a−ρb      |                  |     |         | 1   |     |
|     |     | g ′(σ | ) =ϕ(b) | 1−2Φ     |          |           |                  | +2ϕ | (a,b;ρ) |     |     |
|     |     | X     |         |          |          | (cid:112) |                  | 2   |         | ,   |     |
|     |     |       |         | σ        |          | 1−ρ2      |                  |     |         | σ   |     |
|     |     |       |         | X        |          |           |                  |     |         | Y   |     |
but
(cid:20) (cid:21)
|     |     |     |      | µ     | σ X | µ   | µ   | µ   |     |     |     |
| --- | --- | --- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | a−ρb | = − − |     | −   | = − | +   | =0  |     |     |
|     |     |     |      | σ     | σ   | σ   | σ   | σ   |     |     |     |
|     |     |     |      | Y     | Y   | X   | Y   | Y   |     |     |     |
Therefore
|     |     |     |     | (cid:32) | (cid:33) |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- |
a−ρb
|     |     |     |     | Φ   |     | = Φ(0) | =0.5, |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | ----- | --- | --- | --- | --- |
(cid:112)
1−ρ2
whichmeansthat
|     |     |     |     | ′(σ |     |         | 1   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
|     |     |     |     | g ) | =2ϕ | (a,b;ρ) | >0  |     |     |     |     |
|     |     |     |     | X   | 2   |         | σ   |     |     |     |     |
Y
|             | Thus,g(σ | )isanincreasingfunctioninσ |               |      |     | .Consequently,whenever |       |      |     |     |     |
| ----------- | -------- | -------------------------- | ------------- | ---- | --- | ---------------------- | ----- | ---- | --- | --- | --- |
|             |          | X                          |               |      |     | X                      |       |      |     |     |     |
|             |          |                            |               |      | σ   |                        | σ     |      |     |     |     |
|             |          |                            |               | ρ    | = X | > ρ                    | = Z   |      |     |     |     |
|             |          |                            |               | YX   |     | YZ                     |       |      |     |     |     |
|             |          |                            |               |      | σ Y |                        | σ Y   |      |     |     |     |
| wewillhaveσ |          | > σ                        | ,whichleadsto |      |     |                        |       |      |     |     |     |
|             |          | X Z                        |               |      |     |                        |       |      |     |     |     |
|             |          |                            | MDA           | −MDA | =   | g(σ                    | )−g(σ | ) ≥0 |     |     |     |
|             |          |                            |               | X    | Z   | X                      |       | Z    |     |     |     |
Hence,theMDA-CorrelationParadoxcannotarisewhenbothforecastsareMincer–
□
Zarnowitz[10]efficient,whichcompletestheproof.
Proposition2indicatesthattheMDAParadoxcannotoccurwhencomparingMincer–
Zarnowitz[10]efficientforecasts. Thisisanimportantresult. However,sinceviolations
of efficiency are fairly common in the forecasting literature, it is important to explore
someconditionsunderwhichtheMDAParadoxmaystillbepreventedinthepresence
ofinefficientforecasts. (Violationsofforecastefficiencyhavebeendocumentedacrossa
widerangeofvariablesinnumerousstudies. See[29–33]amongothers.) Thisisprecisely
addressedinthefollowingLemma3.
Lemma3. InthecontextofProposition1,andassumingρ , ρ ϵ(−1, 1),ifthestandardized
|     |     |     |     |     |     |     | YX  | YZ  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
meansofbothforecastsarethesame
|     |     |     |     |     | µ Z | µ X |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | =   | =   | θ,  |     |     |     | (5) |
|     |     |     |     |     | σ   | σ   |     |     |     |     |     |
|     |     |     |     |     | Z   | X   |     |     |     |     |     |
thenparadoxicalresultsbetweenMDAandcorrelationsareimpossible.
| ProofofLemma3: |      | Using(5)in(1)weget |               |     |          |            |       |          |     |            |                  |
| -------------- | ---- | ------------------ | ------------- | --- | -------- | ---------- | ----- | -------- | --- | ---------- | ---------------- |
|                |      |                    |               |     | (cid:20) | (cid:18) µ |       | (cid:19) |     | (cid:18) µ | (cid:19)(cid:21) |
|                |      |                    | Φ(−θ)−Φ(−θ)+2 |     |          | Φ          | Y     |          | −Φ  | Y          |                  |
| MDA            | −MDA | =                  |               |     |          | −          | ,−θ;ρ |          |     | − ,−θ;ρ    | ,                |
|                | X    | Z                  |               |     |          | 2          | σ     | YX       | 2   | σ          | YZ               |
|                |      |                    |               |     |          |            | Y     |          |     | Y          |                  |
so
|     |     |      |     | (cid:20) (cid:18) |     |       | (cid:19) | (cid:18) |         | (cid:19)(cid:21) |     |
| --- | --- | ---- | --- | ----------------- | --- | ----- | -------- | -------- | ------- | ---------------- | --- |
|     |     |      |     |                   | µ   |       |          |          | µ       |                  |     |
|     | MDA | −MDA |     | =2 Φ              | − Y | ,−θ;ρ | −Φ       | −        | Y ,−θ;ρ |                  |     |
|     |     | X    | Z   | 2                 |     | YX    |          | 2        |         | YZ               |     |
|     |     |      |     |                   | σ Y |       |          |          | σ Y     |                  |     |
Ifρ > ρ ,Lemma1impliesthattheright-handsideinthepreviousexpressionis
|     | YX  | YZ  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
non-negative,whichinturnmeansthat
|     |     |     |     | MDA | −MDA |     | ≥0  |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | X    | Z   |     |     |     |     |     |
andnoparadoxicalresultsbetweencorrelationsandMDAcanemergeasstated. □
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 16of27
Lemma3andProposition2establishclearsufficientconditionsunderwhichtheMDA
Paradox is impossible. It remains to investigate whether a simpler condition, such as
unbiasedness, is also sufficient to prevent this paradox. Although the simple example
in Section 3.2.5 shows that this is not the case, it turns out that unbiased forecasts, in
the context of a mean-zero target variable, fall within the framework of Lemma 3. (In
the numerical illustration in example Section 3.2.5, we already showed that the MDA
Paradoxemergeswhenbothforecastsareunbiased. Inthisparticularexampleweassumed
µ = µ = µ = 0.5.) Interestingly, in this setting, a closed-form expression for the
Y X Z
differenceinMDAisalsoavailable,asweshallseenext.
Proposition3. InthecontextofProposition1,if ρ , ρ ϵ(−1, 1)andbothforecastsXandZ
YX YZ
areunbiasedforthemean-zerotargetvariableY,thatistosay
µ = µ = µ =0
X Z Y
Then
1
MDA −MDA = [arcsin(ρ )−arcsin(ρ )],
X Z YX YZ
π
andtheMDAParadoxisimpossible.
ProofofProposition3. IfXandYarejointlynormalrandomvariableswithmeanzero,
unitvariancesandcorrelationcoefficientρ ∈ (−1, 1),thenwehave
(cid:90) ∞(cid:90) ∞ 1 1 −1(x2−2xyρ+y2)
Pr(X >0,Y >0) =
(cid:112)
e 2 1−ρ2 dxdy
0 0 2π 1−ρ2
Usingpolarcoordinatesx =rcosθ, y =rsinθ,wecanwritethisprobabilityas
1 (cid:112) 1 (cid:90) π 2 (cid:90) ∞ e −1 2 (1− 1 ρ − si ρ n 2 2θ) r2 rdrdθ
2π 1−ρ2 0 0
Let A(θ) =
1−ρsin2θ
,thenusingthefollowingchangeinvariables
1−ρ2
1
u = A(θ)r2 =⇒ du = A(θ)rdr, r =0=⇒ u =0, r −→ ∞ =⇒ u −→ ∞;
2
weget
(cid:90) ∞ e −1 2 (1− 1 ρ − si ρ n 2 2θ) r2 rdr = (cid:90) ∞ e −1 2 A(θ)r2 rdr = 1 (cid:90) ∞ e −udu = 1
0 0
A(θ)
0
A(θ)
Thus
Pr(X >0,Y >0) =
2
1
π (cid:112) 1
1
−ρ2
(cid:90)
0
π 2
1−
1−
ρsi
ρ
n
2
2θ
dθ = (cid:112) 1
2
−
π
ρ2(cid:90)
0
π 2
1−ρ
1
sin2θ
dθ
(cid:0) (cid:1) (cid:0) (cid:1)
Let v =tanθ =⇒dv =sec2θ dθ = tan2θ+1 dθ = v2+1 dθ.
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 17of27
Moreover, sin2θ = 2sinθcosθ = 2 tanθ = 2v . Thus, the probability
tan2θ+1 v2+1
Pr(X >0,Y >0) equals
√ (cid:34) (cid:35) √
Pr(X >0,Y >0) =
2
1
π
−ρ2(cid:82)
0
∞
1−ρ (cid:16)
1
2v (cid:17) v2
d
+
v
1
=
2
1
π
−ρ2(cid:82)
0
∞
v2+1
d
−
v
2vρ
√ √ v2+1
= 1−ρ2 (cid:82)∞ 1 dv = 1−ρ2(cid:82)∞ √1 du
√ 2π 0 (v−ρ)2+1− (cid:18) ρ2 (cid:19) 2 (cid:12) π ∞ −ρ u (cid:20) 2+ 1−ρ2 2 (cid:18) (cid:19)(cid:21)
= 1−ρ2 √1 arctan √u (cid:12) (cid:12) = 1 π −arctan √−ρ
2π 1−ρ2 1−ρ2 (cid:12)
−ρ
2π 2 1−ρ2
(cid:18) (cid:19) (cid:18) (cid:19)
= 1 − 1 arctan √−ρ = 1 + 1 arctan √ρ
4 2π 1−ρ2 4 2π 1−ρ2
Inthislaststepwehaveusedthatarctanisanoddfunction. Letusexpressρ =sin(φ)
for φ ∈ (cid:0) −π;π(cid:1) .Giventhatsin2(φ)+cos2(φ)=1,wegetcos2(φ) = 1−ρ2 whichmeans
2 2 (cid:18) (cid:19)
cos(φ) = (cid:112) 1−ρ2.Thereforetan(φ) = √ρ whichmeans φ =arctan √ρ . Yet,we
1−ρ2 1−ρ2
startedwith ρ = sin(φ) whichinturnmeans, φ = arcsin(ρ). Thisleadstotheequality
(cid:18) (cid:19)
arctan √ρ =arcsin(ρ). Sowefinallyhave
1−ρ2
1 1
Pr(X >0,Y >0) = + arcsin(ρ)
4 2π
whichisanincreasingfunctionofρasgivenbythederivative
d(arcsin(ρ)) 1
=
(cid:112)
>0;|ρ| <1
dρ 1−ρ2
Recallingthat
MDA =Pr(YX>0) =Pr(Y>0,X>0)+Pr(Y≤0,X≤0),
X
andusingthesymmetryofthebivariatenormaldistributionwithzeromeansandequal
variances,weget
1 1
MDA =2Pr(Y >0,X >0) = + arcsin(ρ),
X
2 π
whichfinallyleadsto
1
MDA −MDA = [arcsin(ρ )−arcsin(ρ )]
X Z YX YZ
π
□
whichisthedesiredresult. Figure2representsMDA asafunctionofρ.
X
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 18of27
Figure2. TheplotillustratesMDA = 2Pr(Y>0,X>0) = 1 + 1arcsin(ρ) whenforecastXis
X 2 π
unbiasedforthemean-zerotargetvariableY.
5. EmpiricalIllustration
Inthissection,weillustratetheMDAParadoxwithanapplicationinthecontextofthe
exchangerateforecastingliterature. OurtargetvariableistheChileanPeso(CLP)vis-à-vis
the US Dollar. We evaluate forecasts from the Survey of Professional Forecasters (SPF)
conductedbytheCentralBankofChile. Specifically,weusemonthlyobservationsofthe
ChileanPesoandSPFforecastsfortheperiodApril2012–April2024. Forexchangerate
data,weextractthedailyclosingpriceoftheCLPfromBloombergandconvertthemto
monthlyfrequenciesbysamplingfromthelastdayofeachmonth. Wealsosamplethe
closingpricefromthedaybeforethesurveyisreleased. Thelattertimeseriesissimply
denoted as CLP+. We will explain in brief why we consider two different time series
fortheChileanPeso. DatafromtheSPFaredirectlyobtainedfromtheCentralBankof
Chile. Duringthesampleperiod,thesurveyreleasedatevariedbetweenthe9thand13th
ofeachmonth.
Wewillusethefollowingnotation: S denotestheChileanPesoatmontht. Being
t
morespecific,S representstheamountofChileanPesosrequiredtobuyoneU.S.Dollarat
t
theclosingpriceofthelastdayofmontht. So,andjusttogiveanexample,ifmonthtcorre-
spondstoJanuary,S correspondstotheclosingpriceoftheCLPinJanuary31st. Iffollows
t
inthisexample,thatS t+1 wouldrepresenttheclosingpriceoftheCLPinFebruary28.We
havealreadymentionedthatthesurveyisreleasedtothepublicsometimeinthemiddle
ofeachmonth. WewillusethenotationS t+ togenericallydenotetheclosingpriceofthe
CLPthedaybeforethesurveyisreleased. So,followingwiththepreviousexample,ifthe
surveyisreleasedinFebruarythe10th,thenS t+ wouldrepresenttheclosingpriceofthe
CLPinFebruarythe9th. So,thefollowinginequalitydescribesthetimelineintheflowof
information: t < t+ < t+1.
We have spent a few lines describing this timeline because we want to assess the
predictiveabilityofthesurvey,whichisreleasedaroundthemiddleofeachmonth. So,fol-
lowingwiththepreviousexample,ifthesurveyisreleasedinFebruary10ththedifference
S t+1 −S t isnotentirelyunknown. ThisvariationrepresentshowtheCLPchangesfromthe
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 19of27
endofJanuarytotheendofFebruary. Yet,atthemomentthesurveyisreleasedwealready
knowwhathappenedinthefirstninedaysofFebruary. Moregenerally
S t+1 −S t = [S t+1 −S t+ ]+[S t+ −S t ]
The only unknown variable in the right-hand side of the previous expression is
[S t+1 −S t+ ], sothatwouldbethefocusofourinterest. Thesurveyasksforforecastsat
threedifferenthorizons: 2,11and23monthsahead. TheCentralBankofChileprovides
themedianvaluesacrossallrespondents. WelabelSPF2,SPF11andSPF23thetime-series
containing the median of these forecasts 2, 11 and 23 months ahead, respectively. An
importantobservationisinorder: weconsidereachtime-seriesSPF2,SPF11andSPF23as
independentforecastsfortheChileanexchangerateandweexploretheirabilitytocorrectly
predicttheChileanPesoatdifferentforecastinghorizonsh,varyingfromh=1,2,3,6,9,
11, 12, 18 and 24 months ahead. So, despite SPF2 being the median of the respondents
regardingthequestionfortheChileanexchangerate2monthsahead,weexplorealsoif
thisanswerisusefultopredictattheshortesthorizonofonemonth,aswellasthelonger
horizons of 3, 6, 9, 11, 12, 18 and 24 months ahead. This is in line with previous work
by[28]whoshowedthatSPF2,SPF11andSPF23couldbeusefulforecastsoftheChilean
Pesoatseveralhorizons.
Figure3depictstheChileanpeso(ourtargetvariable)duringthesampleperiodof
interestandthetimeseriesofourthreeforecastsSPF2,SPF11andSPF23. Thisfigurereveals
anupwardtrendinallfourseries,whichisaclearevidenceofanon-stationarybehavior.
Toavoidanypotentialspuriousresultsthataresofrequentintheanalysisoftrendingdata
or,moregenerally,non-stationarydata,wefocusonforecastingChileanPesolog-returns,
ratherthantheChileanPesoitself.
1000
900
800
700
600
500
400
2012-04 2013-04 2014-04 2015-04 2016-04 2017-04 2018-04 2019-04 2020-04 2021-04 2022-04 2023-04 2024-04
PLCDSU
CLP SPF2 SPF11 SPF23
Figure3.ChileanPeso(CLP)vis-à-vistheUSDollarandsurvey-basedforecasts.
Figure3showsthatallthreeforecasts, SPF2, SPF11andSPF23, closelytrackedthe
Chilean Peso during the early part of our sample period, from April 2012 to May 2018.
Afterthat,however,thethreeforecastsdisplayasystematicdownwardbias,consistently
underestimatingthevalueoftheUSDollar. Furthermore,inthelatterhalfofthesample,
SPF2tendstolieaboveSPF11,whichinturntendstolieaboveSPF23. Thisorderingsug-
geststhatthemedianforecasterexpectedtheChileanPesotostrengthenastheforecasting
horizonincreased,anoutcomethatdidnotmaterializeduringthisperiod. Ourpredictive
analysisfocusesonthesecondpartofthesampleperiod, fromJune2018toApril2024.
WedosopartlybecauseRef.[28]analyzesthesamedatasetonlyuptoMay2018, and
partlybecauseofthepreviouslydocumenteddownwardbiasinthesurvey. Aswillbecome
https://doi.org/10.3390/math14050752

Mathematics2026,14,752
20of27
evidentbelow,thisbiasedbehaviorappearstobeakeyelementunderlyingtheparadoxical
resultsthatfollow.
≡
Weuselower-caseletterstodenotethenaturallogarithmofavariable,sothat: s t
ln(S ).Theh-periodlog-returnoftheChileanPesoisdefinedas
t
|     |     |     | r =    | s   | −s  |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | t+,t+h | t+h | t+  |     |     |     |     |     |
Wefocusonforecastsofthisvariableathorizonsofh=1,2,3,6,9,11,12,18,24months
ahead. NoticethatthisexpressionrepresentsthelogarithmicreturnoftheCLPbetweenthe
middleofmontht+1andthelastdayofmontht+h. Whenh=1,thereturnspansonlya
fewdays;whenh=3,itcoversroughlytwoandahalfmonths. Forlongerhorizons,the
extensionisstraightforward. Weconsiderthefollowingforecastsobtainedfromthesurvey:
|     |     | S PF2 | sS PF2−s |     |         |     |     |     |     |     |
| --- | --- | ----- | -------- | --- | ------- | --- | --- | --- | --- | --- |
|     |     | r +   | = t+     | t+  | forallh |     |     |     |     |     |
t
|      |          | S PF11    | sS PF11−s   |     |         |     |     |     |     |     |
| ---- | -------- | --------- | ----------- | --- | ------- | --- | --- | --- | --- | --- |
|      |          | r         | =           | t+  | forallh |     |     |     |     |     |
|      |          | t +       | t+          |     |         |     |     |     |     |     |
|      |          | r S PF23  | = sS PF23−s |     | forallh |     |     |     |     |     |
|      |          | t +       | t+          | t+  |         |     |     |     |     |     |
|      | (cid:16) | (cid:17)  |             |     |         |     |     |     |     |     |
| SPFj | ≡        | SPFj SSPF |             |     |         |     |     |     |     |     |
where s t+ ln S t+ and t+ denotes the forecast of the nominal exchange rate
|                                       |     |     |     | ∈   | {2, | 23}representsthecorresponding |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- |
| reportedbytheSPFjatmontht+1.Theindexj |     |     |     |     | 11, |                               |     |     |     |     |
identifiersofthesurvey. RecallthatwetreatSPF2,SPF11,andSPF23asdistinctforecasts
forr . Accordingly,inwhatfollows,weevaluater S PF2, rS PF11andr S PF23asdifferent
| t+,t+h |     |     |     |     | t + |     | t+  | t + |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
forecastsontheirownmerits.
Whenchoosingabenchmarktocompareourforecasts,itisnaturaltoconsiderthe
DriftlessRandomWalk,whichpredictszeroreturnsateveryforecasthorizon. Thiszero
forecasthasbeenalandmarkintheexchangerateliteraturesincetheseminalarticleby[25].
Morerecently,Ref.[27]emphasizesthat,inexchangerateforecasting,thezeroforecastis
thetoughestbenchmarktooutperform. Ref.[34]providesamorerecentexampleinwhich
thezeroforecastisusedasabenchmarkwhenforecastingexchangeratesreturns.
Despite its popularity, one of the drawbacks of the zero forecast is that it has no
variance,soitscorrelationwiththetargetvariableisnotdefined. Alongthesamelines,the
zeroforecastalsoexhibitsapoorMDA,whichisexactlyzero. Therefore,thisparticular
forecastrequiresaslightmodificationtobeusedmoresensibly.
=u
Toaddressthis,letusconsiderthefollowingbenchmarkForecastb t+ t+,whereu t+
isanindependentGaussianwhitenoiseprocess. Wedenoteitsvariancesimplyasσ2 >0.
u
Itfollowsthatthecorrelationbetweenthisbenchmarkforecastandr isexactlyzero,
t+,t+h
whileitsMDAis0.5,justasinexampleSection3.2.6
|         | (cid:0) |                 | (cid:0) |         |           | (cid:1) | (cid:0)         |      |     | (cid:1) |
| ------- | ------- | --------------- | ------- | ------- | --------- | ------- | --------------- | ---- | --- | ------- |
| MDA =Pr | r       | u >0) =Pr       | r       | >0,u    |           | >0 +Pr  | r               | ≤0,u |     | ≤0      |
| b       | t+, t+h | t+              | t+,     | t+h     | t+        |         | t+,             | t+h  | t+  |         |
|         |         | (cid:2) (cid:0) | (cid:1) | (cid:0) |           |         | (cid:1)(cid:3)1 | 1    |     |         |
|         |         | = Pr r t+,      | t+h >0  | +Pr     | r t+, t+h | ≤0      | =               |      |     |         |
2 2
Thus,oursimplegeneralizationofthetraditionalzeroforecastrecoversthestandard
pure-luckbenchmarkforMDA,which—tothebestofourknowledge—isamongthemost
widelyusedbenchmarksinMDAevaluations. Seeforinstance, Refs.[33,35,36]. Italso
serves as a benchmark for correlations, because it now has some variance. Of course,
thebenchmarkcorrelationisexactlyzero. NoticethattheGaussianassumptionforour
benchmarkisnotessential,asweonlyneedindependence,zeromean,somenon-negligible
varianceandasymmetricpdf. aroundzero. Nevertheless,thisassumptionisconsistent
withtheanalyticalframeworkthatwehaveusedinthispaper. (Inanutshell,oursimple
generalizationofthetraditionalzeroforecastisdesignedtoachievethreeobjectives. First,
it is closely related to the traditional zero forecast. Second, it delivers an MDA of 0.5,
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 21of27
therebyrecoveringthestandardpure-luckbenchmarkcommonlyusedinMDAevaluations.
Third,itprovidesameaningfulbenchmarkforcorrelation-basedevaluation. Indeed,itis
impossibletocomputeacorrelationbetweenthezeroforecastandthetargetvariable,as
theformerhaszerovariance. Likewise,adopting0.5asabenchmarkforMDAaloneleaves
openthequestionofwhatcorrelationsuchanimplicitbenchmarkwouldhavewiththe
targetvariable. Ourgeneralizedzeroforecastresolvestheseissuesinaunifiedframework.)
Table1nextreportstheMDAofoursurvey-basedforecasts(Panel1)andtheircor-
relationwithChileanPesoreturns(Panel2). InPanel1, wepresenttheMDAforSPF2,
SFF11andSPF23atdifferenthorizons. Figureswithstarsindicatethatthenullhypothesis
ofthesurvey’sMDAbeingsuperiortothepureluckbenchmark(0.5)isrejectedatusual
significance levels. In other words, figures with stars indicate that the 0.5 benchmark
outperforms the corresponding survey with statistical significance. Panel 2 reports the
correlation between each survey and Chilean Peso returns. Figures with stars indicate
correlationsthatarestatisticallysignificantandpositive.
Table1.ForecastingtheChileanPesovis-à-vistheUSDollarwiththesurveyofprofessionalforecasters.
MDA
Horizon 1 2 3 6 9 11 12 18 24
SPF2 46.5 40.8** 40.8* 35.2*** 38.0** 39.4* 38.0** 49.3 39.4
SPF11 47.9 47.9 47.9 46.5 50.7 52.1 49.3 46.5 36.6**
SPF23 49.3 49.3 46.5 45.1 46.5 47.9 47.9 43.7 33.8***
CorrelationwiththeTargetVariable
Horizon 1 2 3 6 9 11 12 18 24
SPF2 0.19 0.08 0.06 0.14 0.27** 0.25** 0.21* 0.15 0.04
SPF11 0.25* 0.19** 0.21** 0.38*** 0.52*** 0.47*** 0.44*** 0.28* 0.10
SPF23 0.21* 0.20* 0.29*** 0.47*** 0.60*** 0.58*** 0.57*** 0.42** 0.21
Notes:Panel1inTable1reportsMDAofthedifferentversionsoftheSPFatseveralhorizons.Figureswithstars
indicatethatthenullhypothesisofthesurvey’sMDAbeingsuperiortothepureluckbenchmark(0.5)isrejected
atusualsignificancelevels.Panel2presentsthecorrelationbetweeneachsurveyandChileanPesoreturns,with
starsdenotingcorrelationsthataresignificantlypositive. InferenceiscarriedoutwithHACstandarderrors
accordingto[37,38].FurtherinferencedetailscanbefoundinAppendixB.*p<0.1,**p<0.05,***p<0.01.Source:
Author’selaboration.
InthefirstpanelofTable1,onlytwoentriesshowMDArisingslightlyabove50%,
whiletheoverallaverageMDAisadisappointing44.5%, illustratingthesurvey’spoor
performance on this metric. Moreover, eight entries in this panel display statistically
significantresultsinfavorofthe0.5benchmark. Instarkcontrast,weseeonlypositive
figuresinthesecondpanelofthetable,withanaveragecorrelationbetweenthesurvey
andthetargetvariableof29%. Themaximumcorrelationisashighas60%,achievedwith
SPF23whenforecasting9monthsahead. Moreover,19outof27entriesinthissecondpanel
reportstatisticallysignificantandpositivecorrelations.
The MDA Paradox emerges clearly when comparing the two panels of Table 1: in
the first panel, the survey is almost always outperformed by our naïve benchmark in
termsofMDA,whereasinthesecondpanel,thesurveyconsistentlyoutperformsthesame
benchmarkintermsofcorrelations. TheMDAParadoxismostevidentinSPF2forecasts
at 9, 11, and 12 months ahead: despite MDA figures being significantly lower than the
naïve 0.5 benchmark, their correlations with Chilean Peso returns remain positive and
statisticallysignificant. (Asarobustnesscheck,wesplitthepredictivesampleintotwo
balancedsubperiodsandre-estimatedbothMDAandcorrelationmeasuresseparatelyfor
eachwindow. WhilethisexerciserevealssomeheterogeneityinthelevelsofMDAand
https://doi.org/10.3390/math14050752

Mathematics2026,14,752
22of27
correlationsacrosssubsamples,thequalitativemessageremainsunchanged. Evidenceof
theMDAParadox—bothinitsweakand,insomecases,strongform—continuestoemerge
inbothsubperiods,reinforcingtherobustnessandempiricalrelevanceofourmainfindings.
Adetailedversionofthisrobustnessanalysisisavailableuponrequest.)
ResultsinTable1canbebetterunderstoodinlightofourexampleinSection3.2.6,
wheretheMDAParadoxemergesinanenvironmentinwhichwecomparetwoforecastsX
andZforourtargetvariableY,suchthatZandYaretotallyindependent,Zismeanzero
withasymmetricdistribution,Xispositivelycorrelatedwiththetargetvariable(ρ >0),
YX
and µ < 0while µ > 0. Asamatteroffact,Table2nextshowsaveragesofbothour
|     |                                                    | X   |     |     | Y   |     |     |     |     |     |      |     |     |     |
| --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
|     | targetvariableandsurvey-basedforecastsasaproxyforµ |     |     |     |     |     |     |     |     |     | andµ | .   |     |     |
|     |                                                    |     |     |     |     |     |     |     |     |     | X    | Y   |     |     |
Table2.AveragesofChileanPesoreturnsandsurvey-basedforecastsatseveralhorizons.
| Horizon    | 1     | 2     |     | 3     |     | 6     |       | 9   | 11    |     | 12    | 18    |       | 24  |
| ---------- | ----- | ----- | --- | ----- | --- | ----- | ----- | --- | ----- | --- | ----- | ----- | ----- | --- |
| CLPReturns | 0.26  | 0.82  |     | 1.48  |     | 3.27  | 4.78  |     | 5.55  |     | 5.79  | 7.56  | 10.27 |     |
| SPF2       | −0.97 | −0.98 |     | −0.94 |     | −0.79 | −0.67 |     | −0.59 |     | −0.60 | −0.63 | −0.34 |     |
| SPF11      | −2.91 | −2.87 |     | −2.74 |     | −2.37 | −2.06 |     | −1.92 |     | −1.95 | −1.81 | −1.15 |     |
| SPF23      | −4.47 | −4.36 |     | −4.16 |     | −3.68 | −3.31 |     | −3.14 |     | −3.16 | −3.00 | −2.07 |     |
Results in Table 2 show that while forecasts are centered in negative territory, our
targetvariablehasapositivemeanateveryforecasthorizon. Nonetheless,thislastfact
aloneisnotenoughtoobtaintheMDAParadox. InSection3.2.6,weadditionallyusedthe
sufficientcondition
|     |     |     |     |     |     | (cid:18) | (cid:19) | (cid:18) |     | (cid:19) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | -------- | -------- | --- | -------- | --- | --- | --- | --- |
|     |     |     |     |     |     |          | µ        |          | µ   |          |     |     |     |     |
|     |     |     |     |     |     | Φ        | − X      | −Φ       | − Y | >0.5     |     |     |     |     |
|     |     |     |     |     |     |          | σ X      |          | σ Y |          |     |     |     |     |
toguaranteetheParadox. Yet,itisnothardtoderivefromExpression(1)thefollowing
equalitythatisnecessaryandsufficientfortheMDAParadoxtooccurinourspecificcase
|     |     |     |     |      |     | (cid:20) | (cid:18) | (cid:19) | (cid:18) | (cid:19)(cid:21) | (cid:18) |       | (cid:19) |     |
| --- | --- | --- | --- | ---- | --- | -------- | -------- | -------- | -------- | ---------------- | -------- | ----- | -------- | --- |
|     |     |     |     |      |     | 1        | µ X      |          | µ        | Y                |          | µ Y µ | X        |     |
|     |     | MDA |     | −MDA | =   | − Φ      | −        | +Φ       | −        | +2Φ              |          | − ,−  | ;ρ       | (6) |
|     |     |     | X   |      | Z   | 2        | σ        |          | σ        |                  | 2        | σ σ   | YX       |     |
|     |     |     |     |      |     |          | X        |          |          | Y                |          | Y     | X        |     |
Expression(6)indicatesthatwewillhavetheMDAParadoxwhenever
|     |     |     |     |     | (cid:18) |     | (cid:19) |     | (cid:18) | (cid:19) | (cid:18) | (cid:19) |     |     |
| --- | --- | --- | --- | --- | -------- | --- | -------- | --- | -------- | -------- | -------- | -------- | --- | --- |
|     |     |     |     | 2Φ  | µ        | Y µ | X        | Φ   | µ X      | +Φ       | µ        | Y 1      |     |     |
|     |     |     |     |     | −        | ,−  | ;ρ       | <   | −        |          | −        | −        |     |     |
|     |     |     |     |     | 2 σ      | σ   | YX       |     | σ        |          | σ        | 2        |     |     |
|     |     |     |     |     |          | Y   | X        |     | X        |          |          | Y        |     |     |
Asafinalexercise,wecanevaluatethefollowingexpression
|     |     |     |     |     |      | (cid:18) µ | (cid:19) | (cid:18) µ | (cid:19) | (cid:18) | µ      | µ (cid:19) |     |     |
| --- | --- | --- | --- | --- | ---- | ---------- | -------- | ---------- | -------- | -------- | ------ | ---------- | --- | --- |
|     |     |     |     |     | =1−Φ | −          | Y −Φ     | −          | X +2Φ    |          | − Y ,− | X          |     |     |
|     |     |     | MDA | X   |      |            |          |            |          | 2        |        | ;ρ YX      |     | (7) |
|     |     |     |     |     |      | σ          |          | σ          |          |          | σ      | σ          |     |     |
|     |     |     |     |     |      |            | Y        |            | X        |          | Y      | X          |     |     |
usingsampleestimatesoftheparametersµ Y , µ Z , µ X ,σ Y ,σ X andρ YX fromthedataofour
forecastsandtargetvariable,tocheckifourGaussianapproximationmatchestheempirical
MDA presented in Table 1. On average, our Gaussian approach is extremely accurate.
ThemedianMDAreportedfromTable1is46.5%,whilethemedianMDAobtainedfrom
Expression(7)acrossallforecastsandhorizonsis47.1%. ForparticularentriesofTable1
theGaussianapproachisextremelyclose(46.4%vs. 46.5%forSPF23whenh=3), but
forotherentriesthisGaussianapproximationisnotveryaccurate(48.5%vs. 35.2%for
SPF2whenh=6). Allinall,ourGaussianapproximationseemsusefultoexplaintheMDA
Paradoxinthisexampleontheaggregatelevel.
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 23of27
6. Conclusions
Inthispaper,weshowed—boththeoreticallyandempirically—thatevaluatingcom-
petingforecastsbasedontheircorrelationwiththetargetvariableandontheirabilityto
correctlypredictitssignmayleadtooppositeconclusions. Inparticular,aforecastthatis
morestronglycorrelatedwiththetargetvariablemayexhibitalowerMeanDirectional
Accuracy(MDA)thanalesscorrelatedalternative. Thisparadoxcanbeextreme: forecasts
containing genuinely useful information may be completely outperformed in terms of
MDAbyonethatisentirelyindependentoftheunderlyingvariable.
Thisfindingisparticularlystrikingbecausemanystudiesimplicitlyregardaforecast
that outperforms the pure luck benchmark (MDA = 0.5) as “useful.” Yet, within our
framework,evenacompletelyindependentforecastZmayexceedthisbenchmarkwhenthe
targetvariableYhasanonzeromean. Insuchcases,ahigherMDAmayarisemechanically,
for instance, because Z and Y share similar standardized means, rather than from any
genuinepredictivecontent. Fortunately,wealsoidentifyconditionsunderwhichtheMDA
Paradoxcannotoccur. Inparticular,whencomparingMincer–Zarnowitzforecasts,this
paradoxisimpossible.
AllouranalyticalresultsrelyonaGaussianassumption,underwhichcorrelations
fullycharacterize the dependence structureamong thevariables. A naturalavenue for
futureresearchistoinvestigatewhetherourfindingsextendtomoregeneraldistributional
settings. Moreover,theMDAParadoxraisesquestionsabouttheusefulnessofthepure-
luckbenchmarkitself. FutureworkcouldexplorealternativeMDAbenchmarksthatare
eithermoreinformativeormorerobusttothepresenceofthisparadox. Finally,amore
extensiveempiricalassessmentoftheMDAParadoxwouldbevaluable,bothtoidentify
real-worldforecastingenvironmentsinwhichsignpredictabilityconflictswithcorrelation-
basedmeasuresandtoexaminewhethersimilarparadoxicalrelationshipsmayalsoarise
betweenMDAandtraditionalloss-basedcriteriasuchastheMSPE.
AuthorContributions:Conceptualization,P.P.andA.B.;methodology,P.P.,A.B.andL.R.;software,
P.P.;validation,P.P.andL.R.;formalanalysis,P.P.andL.R.;investigation,P.P.andA.B.;resources,
P.P.; datacuration, P.P.; writing—originaldraftpreparation, P.P., A.B.andL.R.; writing—review
andediting,P.P.andL.R.;visualization,P.P.;supervision,P.P.andL.R.;projectadministration,P.P.;
fundingacquisition,L.R.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:PabloPincheiraacknowledgesfinancialsupportfromAgenciaNacionaldeInvestigacióny
DesarrollodeChile(ANID)withFondecytproject#1251636.LorenzoReusacknowledgesfinancialsupport
fromAgenciaNacionaldeInvestigaciónyDesarrollodeChile(ANID)withFondecytproject#1251636.
DataAvailabilityStatement:ThisstudyusespubliclyavailablesecondarydatafromtheCentralBank
ofChile’sSurveyofEconomicExpectations.Nohumanparticipantswereprospectivelyrecruited
forthepurposesofthisstudy.Thesedataarepubliclyavailablehere:https://si3.bcentral.cl/Siete/
ES/Siete/Cuadro/CAP_EXP_ECO/MN_EXP_EC11/EXE_BCCH_04/EXE_BCCH_04. Thisisthe
equivalentoftheFed’sSurveyofProfessionalForecasters.URLaccessedon10June2024.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.Thefundershadnoroleinthedesign
ofthestudy;inthecollection,analyses,orinterpretationofdata;inthewritingofthemanuscript;or
inthedecisiontopublishtheresults.
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
MDA MeanDirectionalAccuracy
MSPE MeanSquaredPredictionError
MAE MeanAbsoluteError
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 24of27
CLP ChileanPesos
USD UnitedStatesDollar
SPF SurveyofProfessionalForecasters
AppendixA
Lemma1. LetΦ (a,b;ρ)denotethecumulativedistributionfunctionofthestandardbivariate
2
normaldistributionwithcorrelationcoefficientρ ∈ (−1, 1),evaluatedatthefixedpoint(a,b)∈R2.
ThenΦ (a,b;ρ)isdifferentiablewithrespecttoρ,anditsderivativeisgivenbythevalueofthe
2
jointdensityatthepoint(a,b):
∂Φ (a,b;ρ)
2 =ϕ (a,b;ρ)
∂ρ 2
whereϕ (a,b;ρ)isthestandardbivariatenormaldensityfunction
2
1 (cid:18) 1 (cid:104) (cid:105)(cid:19)
ϕ 2 (a,b;ρ) = 2π (cid:112) 1−ρ2 exp − 2(1−ρ2) a2−2ρab+b2
Inparticular,sinceϕ (a,b;ρ) >0foralla,b ∈R andρ ∈(−1,1),thefunctionΦ (a,b;ρ)is
2 2
strictlyincreasinginρ.
ProofofLemma1.Usingconditionalprobability,thestandardbivariateGaussiancumulative
distributionfunction(CDF)withcorrelationρcanbewrittenasaunivariateintegral
(cid:32) (cid:33)
(cid:90) a (cid:90) b 1 1 −1(x2−2xyρ+y2) (cid:90) a b−ρx
Φ
2
(a,b;ρ) =
(cid:112)
e 2 1−ρ2 dxdy = ϕ(x)Φ
(cid:112)
dx
−∞ −∞ 2π 1−ρ2 −∞ 1−ρ2
withϕ(x) = √1 e−x 2 2 andΦ(x)thedensityandCDFofastandardnormaldistribution
2π
respectively. Then
(cid:18) (cid:19)
∂Φ 2 ( ∂ a ρ ,b;ρ) = (cid:82) − a ∞ √1 2π e−x 2 2 ∂ ∂ ρ Φ √b− 1− ρx ρ2 dx
(cid:18) (cid:19) (cid:18) (cid:19)
= (cid:82) − a ∞ √1 2π e−x 2 2 ϕ √b− 1− ρx ρ2 × ∂ ∂ ρ √b− 1− ρx ρ2 dx
Notethat
(cid:32) (cid:33) −x
(cid:112)
1−ρ2−[b−ρx]
√−2ρ
∂ b−ρx 2 1−ρ2
=
∂ρ (cid:112) 1−ρ2 1−ρ2
or
(cid:32) (cid:33) −x (cid:112) 1−ρ2+[b−ρx]√ρ
∂ b−ρx 1−ρ2 bρ−x
= =
∂ρ (cid:112) 1−ρ2 1−ρ2 (1−ρ2)2 3
Thus,thederivativeequals
∂Φ 2 (a,b;ρ) = (cid:90) a 1 e −x 2 2 e −( 2 b ( − 1− ρ ρ x 2 )2 ) bρ−x dx
∂ρ −∞ 2π (1−ρ2) 3 2
Now
x2 (b−ρx)2 (x−bρ)2 b2
+ = +
2 2(1−ρ2) 2(1−ρ2) 2
https://doi.org/10.3390/math14050752

Mathematics2026,14,752
25of27
Thus,thederivativeequals
)2
|        |      | ∂Φ (a,b;ρ) |     | 1                   | 2(cid:90) a | −( x − b ρ | bρ−x   |     |     |     |
| ------ | ---- | ---------- | --- | ------------------- | ----------- | ---------- | ------ | --- | --- | --- |
|        |      | 2          | =   | e −b                |             | e (1 − 2   | )      | dx  |     |     |
|        |      |            |     |                     | 2           | 2 ρ        |        |     |     |     |
|        |      | ∂ρ         |     | 2π                  | −∞          |            |        | 3   |     |     |
|        |      |            |     |                     |             |            | (1−ρ2) | 2   |     |     |
| √x−ρb  |      | √1         |     |                     |             |            |        |     |     |     |
| Lett = | , dt | =          | dx. | Thederivativeequals |             |            |        |     |     |     |
1−ρ2 1−ρ2
√a−ρb
|     | ∂Φ  |             |     | 2(cid:82) | 1−ρ2 | 2   | (cid:112) |        |     |     |
| --- | --- | ----------- | --- | --------- | ---- | --- | --------- | ------ | --- | --- |
|     |     | 2 ( a ,b;ρ) | = 1 | e−b       |      | e−t | − t       | 1−ρ2dt |     |     |
|     |     |             |     | π 2       | −∞   | 2   | 2)        |        |     |     |
|     |     | ∂ ρ         | 2   |           |      | (1− | ρ         |        |     |     |
√a−ρb
|     |     |     |     | e−b 2 |     | (cid:82) 1−ρ2 | −e−t 2 |     |     |     |
| --- | --- | --- | --- | ----- | --- | ------------- | ------ | --- | --- | --- |
|     |     |     | = 1 | 2     | √ 1 | −∞            | 2      | tdt |     |     |
|     |     |     | 2   | π     | −ρ2 |               |        |     |     |     |
1
But
|     |     | √a−      |       |       |     | √a− ρb           |     |              |     |     |
| --- | --- | -------- | ----- | ----- | --- | ---------------- | --- | ------------ | --- | --- |
|     |     | (cid:90) | ρb    |       |     | (cid:12)         |     | (a − ρ b) 2  |     |     |
|     |     |          | ρ2 −t | 2     | −t  | 2 (cid:12) 1− ρ2 | −   |              |     |     |
|     |     | 1−       | −e    | 2 tdt | = e | 2 (cid:12)       | = e | 2 (1 − ρ 2 ) |     |     |
|     |     | −∞       |       |       |     | (cid:12)         |     |              |     |     |
−∞
Thusthederivativeequals
|     |     |            |     |           |      | (cid:32)    | (cid:33) |      |     |     |
| --- | --- | ---------- | --- | --------- | ---- | ----------- | -------- | ---- | --- | --- |
|     |     | ∂Φ (a,b;ρ) |     |           | 1    | a−ρb        |          |      |     |     |
|     |     | 2          |     | =         |      |             |          | ϕ(b) |     |     |
|     |     |            |     | (cid:112) |      | ϕ (cid:112) |          |      |     |     |
|     |     |            | ∂ρ  |           | 1−ρ2 | 1−ρ2        |          |      |     |     |
Recallthatthejointdensityϕ (a,b;ρ)canbewrittenastheproductofamarginaland
2
aconditionaldensity
|     |     |     | ϕ   | (a,b;ρ) | = ϕ(a|b)ϕ(b) |     |     |     |     |     |
| --- | --- | --- | --- | ------- | ------------ | --- | --- | --- | --- | --- |
2
wheretheconditionaldistribution
|     |     |     |     |     | (cid:16) | (cid:17) |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | -------- | --- | --- | --- | --- |
ρb,1−ρ2
|     |     |     | a   | | b ∼ | N   |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
Therefore,thecorrespondingconditionaldensityis
|     |        |           |          |          |         |           |     | (cid:32)  | (cid:33) |     |
| --- | ------ | --------- | -------- | -------- | ------- | --------- | --- | --------- | -------- | --- |
|     |        |           | 1        | −(a−ρb)2 |         | 1         |     | a−ρb      |          |     |
|     | ϕ(a|b) | =         |          |          | 2(1−ρ2) | =         |     |           |          |     |
|     |        | (cid:112) |          | e        |         | (cid:112) | ϕ   | (cid:112) |          |     |
|     |        |           | 2π(1−ρ2) |          |         | 1−ρ2      |     | 1−ρ2      |          |     |
Itfollowsthatthederivativesimplyequals
∂Φ
2 (a,b;ρ)
|     |     |     |     | = ϕ(a|b)ϕ(b) |     | =ϕ  | (a,b;ρ) | >0  |     |     |
| --- | --- | --- | --- | ------------ | --- | --- | ------- | --- | --- | --- |
|     |     |     | ∂ρ  |              |     | 2   |         |     |     |     |
□
Whichisthedesiredresult.
AppendixB
Herewedescribeindetailhowweconductinferenceinourempiricalillustration.
MDA.StatisticalsignificanceforMDAisassessedusingat-typetestfollowingRef.[11]i.e.,
atestonthemeanbasedontheCentralLimitTheorem. Leth = I(sign(X ) =sign(Y ))
|     |     |     |     |     |     |     |     | t   | t   | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
denotethehit-rateindicatoranddefined =h −0.5.Thenullhypothesisis
|     |     |     |         |      | t    | t     |     |     |     |     |
| --- | --- | --- | ------- | ---- | ---- | ----- | --- | --- | --- | --- |
|     |     |     | H : E(d | ) =0 | (MDA | =0.5) |     |     |     |     |
|     |     |     | 0       | t    |      |       |     |     |     |     |
Againsttheone-sidedalternative
|     |     |     | E(d   | ) <0 | (MDA | <0.5) |     |     |     |     |
| --- | --- | --- | ----- | ---- | ---- | ----- | --- | --- | --- | --- |
|     |     |     | H 0 : | t    |      |       |     |     |     |     |
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 26of27
Sothatrejectionoccursonlywhendirectionalaccuracyissignificantlyworsethan
randomsignprediction. Theteststatisticis
√ (cid:16) (cid:17) (cid:112)
t = n d −0.5 / Vˆ
t
whereVˆ isaconsistentestimatorofthelong-runvarianceofd . WeestimateVˆ usingthe
t
HACestimatorinRefs.[37,38],whichisconsistentinthepresenceofheteroskedasticity
andautocorrelation. Underthenull,thetstatisticisasymptoticallystandardnormal,and
inferenceisconductedusingaleft-tailedtest.
Correlation. Statisticalsignificanceforthecorrelationisassessedusingaregression-based
test. Specifically,weconsiderthelinearprojection
Y = α+βX +ε ; E(X ε ) =E(ε ) =0
t t t t t t
Fromtextbookformulastheslopecoefficientsatisfies
Cov(X ,Y)
β = t t
Var(X )
t
sothattestingforzerocorrelationisequivalenttotesting
H : β =0
0
Againsttheone-sidedalternative
H : β >0
0
Inferenceisbasedontheusualt-statisticforβ,computedusingHACstandarderrors
toaccountforpotentialheteroskedasticityandautocorrelation,seeRefs.[37,38]. Rejection
thereforeoccursonlyforsufficientlylargepositivevaluesoftheestimatedslopecoefficient.
References
1. Pesaran,M.H.;Timmermann,A.Asimplenonparametrictestofpredictiveperformance.J.Bus.Econ.Stat.1992,10,4.[CrossRef]
2. Orlando,G.;Bufalo,M.Interestratesforecasting:BetweenHullandWhiteandtheCIR#—Howtomakeasinglefactormodel
work.J.Forecast.2021,40,1566–1580.[CrossRef]
3. Orlando,G.;Bufalo,M.TimeseriesforecastingwiththeCIR#model:Fromhecticmarketssentimentstoregularseasonaltourism.
Technol.Econ.Dev.Econ.2023,29,1216–1238.[CrossRef]
4. Ascione,G.;Bufalo,M.;Orlando,G.Modelingvolatilityofdisaster-affectedpopulations:Anon-homogeneousgeometric-skew
Brownianmotionapproach.Commun.NonlinearSci.Numer.Simul.2024,130,107761.[CrossRef]
5. Liu,J.; Papailias,F.; Quinn,B.Direction-of-changeforecastingincommodityfuturesmarkets. Int. Rev. Financ. Anal. 2021,
74,101677.[CrossRef]
6. Pincheira,P.;Hardy,N.TheMSPEparadoxisnotonlyaboutMSPE!Appl.Econ.Lett.2025,1–6.[CrossRef]
7. Anatolyev,S.;Gerco,A.TradingApproachtoTestingforPredictability.J.Bus.Econ.Stat.2005,4,455–461.[CrossRef]
8. Pincheira,P.;Hardy,N.TheMeanSquaredPredictionErrorParadox.J.Forecast.2024,43,2298–2321.[CrossRef]
9. Christoffersen, P.; Diebold, F. Direction of Change Forecasting, and Volatility Dynamics. Manag. Sci. 2006, 52, 1273–1287.
[CrossRef]
10. Mincer,J.;Zarnowitz,V.Theevaluationofeconomicforecasts. InEconomicForecastsandExpectations: AnalysisofForecasting
BehaviorandPerformance;NBER:Cambridge,MA,USA,1969;pp.3–46.
11. Diebold,F.;Mariano,R.ComparingPredictiveAccuracy.J.Bus.Econ.Stat.1995,13,253–263.[CrossRef]
12. Diebold,F.X.Comparingpredictiveaccuracy,twentyyearslater:ApersonalperspectiveontheuseandabuseofDiebold–Mariano
tests.J.Bus.Econ.Stat.2015,33,1.[CrossRef]
13. West,K.D.Forecastevaluation.InHandbookofEconomicForecasting;ElsevierNorth-Holland:Amsterdam,TheNetherlands,2006.
14. Clark,T.E.;McCracken,M.W.Advancesinforecastevaluation. InHandbookofEconomicForecasting;ElsevierNorth-Holland:
Amsterdam,TheNetherlands,2013;pp.1107–1201.
https://doi.org/10.3390/math14050752

Mathematics2026,14,752 27of27
15. Clark,T.E.;McCracken,M.W.Testsofequalforecastaccuracyandencompassingfornestedmodels.J.Econom.2001,105,85–110.
[CrossRef]
16. Clark,T.E.;McCracken,M.W.Evaluatingdirectmultistepforecasts.Econom.Rev.2005,24,369–404.[CrossRef]
17. McCracken,M.W.Asymptoticsforout-of-sampletestsofGrangercausality.J.Econom.2007,140,719–752.[CrossRef]
18. Clark,T.E.;West,K.D.Usingout-of-samplemeansquaredpredictionerrorstotestthemartingaledifferencehypothesis.J.Econom.
2006,135,155–186.[CrossRef]
19. Clark,T.E.;West,K.D.Approximatelynormaltestsforequalpredictiveaccuracyinnestedmodels.J.Econom.2007,138,291–311.
[CrossRef]
20. Pincheira,P.;Hardy,N.;Muñoz,F.“Gowildforawhile!”:Anewtestforforecastevaluationinnestedmodels.Mathematics2021,
9,2254.[CrossRef]
21. West,K.D.Asymptoticinferenceaboutpredictiveability.Econometrica1996,64,1067–1084.[CrossRef]
22. Giacomini,R.;White,H.Testsofconditionalpredictiveability.Econometrica2006,74,1545–1578.[CrossRef]
23. Plackett,R.L.Areductionformulafornormalmultivariateintegrals.Biometrika1954,41,351–360.[CrossRef]
24. Drezner,Z.;Wesolowsky,G.O.Onthecomputationofthebivariatenormalintegral. J.Stat. Comput. Simul. 1990,35,101–107.
[CrossRef]
25. Meese,R.;Rogoff,K.Empiricalexchangeratemodelsoftheseventies: Dotheyfitoutofsample? J.Int. Econ. 1983,14,3–24.
[CrossRef]
26. Chen,Y.;Rogoff,K.S.;Rossi,B.Canexchangeratesforecastcommodityprices?Q.J.Econ.2010,125,1145–1194.[CrossRef]
27. Rossi,B.Exchangeratepredictability.J.Econ.Lit.2013,51,1063–1119.[CrossRef]
28. Pincheira-Brown,P.;Neumann,F.Canwebeattherandomwalk? Thecaseofsurvey-basedexchangerateforecastsinChile.
Financ.Res.Lett.2020,37,101380.[CrossRef]
29. Nordhaus,W.D.Forecastingefficiency:Conceptsandapplications.Rev.Econ.Stat.1987,69,4.[CrossRef]
30. Joutz,F.;Stekler,H.O.AnevaluationofthepredictionoftheFederalReserve.Int.J.Forecast.2000,16,17–38.[CrossRef]
31. Ang,A.;Bekaert,G.;Wei,M.Domacrovariables,assetmarkets,orsurveysforecastinflationbetter? J.Monet. Econ. 2007,54,
1163–1212.[CrossRef]
32. Patton,A.;Timmermann,A.Forecastrationalitytestsbasedonmulti-horizonbounds.J.Bus.Econ.Stat.2012,30,1–17.[CrossRef]
33. Ince,O.;Molodtsova,T.Rationalityandforecastingaccuracyofexchangerateexpectations:Evidencefromsurvey-basedforecasts.
J.Int.Financ.Mark.Inst.Money2017,47,131–151.[CrossRef]
34. Darvas,Z.;Schepp,Z.Exchangeratesandfundamentals:Forecastingwithlongmaturityforwardrates.J.Int.MoneyFinanc.2024,
143,103067.[CrossRef]
35. Cheung,Y.-W.;Chinn,M.D.;Garcia-Pascual,A.Empiricalexchangeratemodelsofthenineties: Areanyfittosurvive? J.Int.
MoneyFinanc.2005,24,1150–1175.[CrossRef]
36. Cheung,Y.-W.;Chinn,M.D.;Garcia-Pascual,A.;Zhang,Y.Exchangeratepredictionredux:Newmodels,newdata,newcurrencies.
J.Int.MoneyFinanc.2019,95,332–362.[CrossRef]
37. Newey,W.;West,K.Hypothesistestingwithefficientmethodofmomentsestimation.Int.Econ.Rev.1987,28,777–787.[CrossRef]
38. Newey,W.;West,K.Automaticlagselectionincovariancematrixestimation.Rev.Econ.Stud.1994,61,631–653.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.
https://doi.org/10.3390/math14050752