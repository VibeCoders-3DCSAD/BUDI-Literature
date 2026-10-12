---
conversion_metadata:
  converted_at: "2026-10-12T07:38:46Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Sankaewtong et al., 2025.pdf"
  source_pdf_sha256: "7d528a064115c861edf227c0e0f07dca3db9115b54f8f7969fc1446d62688b33"
  page_count: 43
  markdown_char_count: 361239
---

Received26September2025,accepted19November2025,dateofpublication25November2025,
dateofcurrentversion4December2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3636560
SoK: Advances in Anomaly Detection Techniques
for Cryptoasset Transactions
KRONGTUMSANKAEWTONG 1,TAEHOONKIM2,CLAUDIOJ.TESSONE 2,
ANDYUICHIIKEDA 1,(Member,IEEE)
1GraduateSchoolofAdvancedIntegratedStudiesinHumanSurvivability,KyotoUniversity,Kyoto606-8306,Japan
2UZHBlockchainCenter,UniversityofZürich,8006Zürich,Switzerland
Correspondingauthor:YuichiIkeda(ikeda.yuichi.2w@kyoto-u.ac.jp)
ThisworkwassupportedinpartbytheRippleImpactFund,SiliconValleyCommunityFoundation,underGrant2022-247584(5855).
ABSTRACT Cryptoasset networks now settle hundreds of billions of dollars each day and underpin a
rapidlyexpandingDeFiecosystem.However,theiropennessexposesthemtofraud,marketmanipulation,
andprotocol-levelexploits.ThisSystematizationofKnowledge(SoK)mapsthestateofanomalydetection
inthisenvironment.Afteroutliningblockchaindatacharacteristicsandthefullthreatspectrum,weapplya
reproducibleOpenAlexsearchandmulti-stagescreeningtocollect103peer-reviewedstudies.Theseworks
areorganizedintofourmethodologicalfamilies:statisticalanalysis,networkanalysis,machinelearning,and
heuristic-based, which we compare across data assumptions, detection scope, interpretability, scalability,
and robustness. Five cross-cutting gaps emerge: label scarcity, adversarial evasion, real-time scalability,
behavioralambiguity,andmulti-chainvisibility.Wetranslatethesegapsintoaresearchagendacenteredon
hybridgraph-neural/heuristicpipelines,drift-awarestatistics,explainabledeepmodels,privacy-preserving
analytics,andstandardizedbenchmarks.ThisSoKprovidesbothaconcisesnapshotofcurrenttechniques
andoffersperspectivesonsecuringthenextgenerationofblockchaininfrastructure.
INDEXTERMS Anomaly,crypto-asset,graphtheory,machinelearning.
I. INTRODUCTION [7], [8], healthcare [9], [10], and decentralized applications
A. BACKGROUNDANDMOTIVATION (DApps)[11],[12].
In 2008, blockchain technology was introduced by Satoshi Despiteitsadoptioninvarioussectors,cryptoassetremains
Nakamoto as the foundational distributed ledger under- blockchain’s most prominent and widely recognized appli-
pinning Bitcoin cryptoasset transactions [1]. This ground- cation. Transaction networks, the graphical representation
breaking implementation enabled Bitcoin to address the of transactions between blockchain addresses or entities,
longstanding double-spending problem, where the same have emerged as critical analytical tools for understanding
digitalassetcouldbespentmorethanoncewithoutrelyingon complex patterns and dynamics within cryptoasset ecosys-
atrustedthird-partyauthorityorcentralizedintermediary[2], tems. These networks offer insights into economic activity,
[3]. Blockchain technology achieves trustless verification asset distribution, and user behavior patterns [13], [14],
through cryptographic techniques, decentralized consensus [15] at a granularity unattainable with traditional financial
protocols (such as proof-of-work and proof-of-stake), and monitoring systems [16], [17], [18]. Moreover, analyzing
transparent yet pseudonymous transaction records stored thesetransactionnetworkshelpsrevealsubtlestructuresand
across numerous network nodes. Due to these attributes, anomalies that may indicate suspicious or illicit behaviors,
blockchain rapidly found applications outside of cryptoas- which traditional centralized monitoring mechanisms could
sets, finding widespread adoption across diverse fields overlook.
including finance [4], [5], supply chain management [6], However, the intrinsic characteristics of blockchain sys-
tems,suchaspseudonymityanddecentralization,alsocreate
vulnerabilitiesexploitablebymaliciousactors.Thecryptoas-
The associate editor coordinating the review of this manuscript and
setecosystemhasgrownsignificantly,brieflytoppingUS$3
approvingitforpublicationwasLorisBelcastro .
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
202576 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME13,2025

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
trillionintotalcapitalizationinlate2021andnowhandling hybrid models for financial trend prediction [21], as well
well over US$100 billion in daily on-chain value transfer. as network-theoretical analyses explicitly designed for
Withinthislarge-scaleenvironment,cryptoassetecosystems graph-structuredblockchaindata[18].
havewitnessedanotableriseinfraudulentactivities,includ- Nevertheless, despite considerable efforts in developing
ing money laundering, market manipulation, ransomware such techniques, existing literature remains fragmented and
payments, and illicit financial transactions involving dark lacks a unified synthesis of knowledge. Different methods
marketplaces and cybercrimes. Generally, in this context, are evaluated under varying assumptions, datasets, and
an anomaly or anomalous transaction refers to activity experimentalconditions,makingdirectcomparisonsdifficult
exhibiting characteristics significantly divergent from what andhighlightingtheneedforasystematicreview.Thisstudy
is deemed ‘‘normal,’’ often indicative of aberrant behavior. addresses precisely this gap by comprehensively reviewing
Determining anomalous status can depend on contextual existing literature on anomaly detection within blockchain
factorsandspecifictransactionalormarketconditions.Finan- transaction networks. By systematically classifying and
cial transactions encompass various characteristics, with analyzingexistingmethods,identifyinglimitationsincurrent
anomalies perceived differently depending on the metrics research,andhighlightingopenresearchchallenges,weaim
employed.Atransactionflaggedasanomalousunderoneset to provide clear guidance for future research directions,
ofcriteriamaynotmeetthesamedesignationunderanother potentially aiding future work on more effective, scalable,
framework. Regulatory bodies worldwide are tasked with and interpretable anomaly detection systems for blockchain
scrutinizingtheseanomalieswithinfinancialtransactionsand ecosystems.
implementingrequisiteinterventions.
Withincryptoassets,theseanomaliesarecommonlycate-
B. SCOPEANDCONTRIBUTION
gorizedintothreemaintypes.Pointanomaliesareindividual
This Systematization of Knowledge (SoK) provides a
transactions markedlydeviating froma typical profile,such
comprehensive review and analysis of anomaly detection
asanunusuallylargesingletransferoratransactioninvolving
techniquesspecificallytargetingcryptoassettransactionnet-
a previously inactive wallet. On the other hand, contextual
works.Ourscopecentersonanalyzingtransactiondatasuch
anomalies appear anomalous primarily due to their context,
asgraphsandtimeseriestoidentifyillicitactivities,network
like occurring at unusual times or representing sudden
attacks,orprotocolmisuse,primarilywithinprominentcryp-
high-frequency activity from typically inactive accounts.
toassets like Bitcoin and Ethereum, while also considering
Finally,collectiveanomaliesincludesequencesorgroupsof
techniques applicable to other platforms. We deliberately
transactionsthatseemsuspiciouswhenviewedtogether,even
exclude studies focused solely on market price prediction
ifindividualtransactionsappearnormal,suchascoordinated
without transaction-level analysis or broader blockchain
pump-and-dump schemes or layering activities used in
applicationsoutsidethefinancial/transactionaldomain,such
moneylaundering.
as supply chain management. The key contributions of this
High-profile incidents involving cryptoasset exchanges workare:
and decentralized finance (DeFi) platforms, such as the
• A systematic literature review identifying and syn-
Mt. Gox Collapse (2014) [19] and the hacks of Poly
thesizing critical publications in blockchain anomaly
Network (2021) [20], serve as stark examples of these
detection,utilizingarigorous,reproduciblepaperselec-
vulnerabilitiesandtheresultinganomalies.Sucheventshave
tion process, ensuring comprehensive coverage and
resulted in losses totaling billions of dollars, undermining
reliability.
trust and illustrating significant weaknesses in existing
• A detailed taxonomy of anomaly detection techniques
anomaly detection frameworks. Consequently, a growing
employed within blockchain transaction networks,
urgency and importance is placed on developing robust
clearly articulating methodological distinctions and
anomalydetectionsystemstailoredexplicitlyforblockchain
applicationcontexts.
transactionnetworks.
• A critical analysis highlighting key research gaps,
Consequently, a growing urgency and importance is
methodological limitations, and emerging challenges
placed on developing robust anomaly detection systems
facedbyexistingstudiesinthisdomain.
tailored explicitly for blockchain transaction networks.
• Recommendations for future research directions that
Effective anomaly detection systems help safeguard users
emphasizedevelopinginnovativeapproachestoaddress
andbusinessesbydetectingillicitactivitiesinnearreal-time,
identified limitations, improve detection effectiveness,
thereby maintaining market integrity, enhancing regulatory
scalability, interpretability, and adaptability to diverse
compliance, and bolstering overall ecosystem security.
cryptoasset platforms, and integration with new tech-
The increased complexity, rapid evolution, and immense
nologies.
transaction volume within blockchain systems necessitate
innovative detection methodologies. Researchers have thus This systematic review aims to guide researchers, prac-
exploredvarioustechniquesrangingfromclassicalstatistical titioners, and policymakers by clarifying state-of-the-art in
analysis and heuristic-based rules to more sophisticated cryptoassetanomalydetectionandhighlightingkeyareasfor
machine learning and deep-learning approaches, including futureinvestigation.
VOLUME13,2025 202577

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
FIGURE1. Distributionofdocumenttypesamongthe1,933publications FIGURE2. Distributionofthe1,438selectedresearchpapersby
| retainedafterpreliminaryscreening.Theverticalaxisisshownona |     |     |     |     |     | publicationyear. |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- |
logarithmicscale.
C. METHODOLOGY
1) PAPERSELECTIONPROCESS
| To address | our research | questions |          | on anomaly | detection    |        |     |     |     |
| ---------- | ------------ | --------- | -------- | ---------- | ------------ | ------ | --- | --- | --- |
| within the | cryptoasset  | domain,   | we       | conducted  | a systematic |        |     |     |     |
| literature | search using | the       | OpenAlex | database.  | Our          | search |     |     |     |
stringwasdesignedtocapturethefullbreadthofresearchat
theintersectionofanomalydetection,cryptoassets,andgraph
analytics.Specifically,wequeriedOpenAlexwith:
| (''anomaly  | detection'' |             | OR anomaly | OR      | anomalies   | OR  |     |     |     |
| ----------- | ----------- | ----------- | ---------- | ------- | ----------- | --- | --- | --- | --- |
| ''detection | of          | anomalies'' | OR         | ``fraud | detection'' |     |     |     |     |
``money
| OR forensics        | OR             | fraud OR        |                  | laundering'' |            | OR  |     |     |     |
| ------------------- | -------------- | --------------- | ---------------- | ------------ | ---------- | --- | --- | --- | --- |
| ''market            | manipulation'' |                 | OR ``transaction |              | network'') |     |     |     |     |
| AND (cryptocurrency |                | OR              | crypto           | OR ``crypto  | asset''    |     |     |     |     |
| OR ``crypto         | wallet''       | OR              | bitcoin          | OR ethereum  | OR         | XRP |     |     |     |
| OR Solana           | OR Tether)     | AND             | (graph           | OR graphs    | OR         |     |     |     |     |
| ``graph             |                | ``graph-based'' |                  |              |            |     |     |     |     |
|                     | based''        | OR              |                  | OR           |            |     |     |     |     |
networks OR network) FIGURE3. Citationcountdistributionofthe1,438selectedresearch
papers,Theinsetprovidesacloserlookatthe0–10citationrange.
| This | search returned | a   | total of | 5,020 | publications | (as |     |     |     |
| ---- | --------------- | --- | -------- | ----- | ------------ | --- | --- | --- | --- |
of as of March 6, 2025). We then applied a multi-stage papers published prior to 2009 (FC5). Finally, we applied
|     |     |     |     |     |     | a minimum | citation threshold | of three (FC6), | based on the |
| --- | --- | --- | --- | --- | --- | --------- | ------------------ | --------------- | ------------ |
screeningprocessasfollows.First,weexcludedpublications
lacking a title, author, abstract, DOI, or indexing, as well citation distribution illustrated in Fig.3, which yielded a
as any duplicates (FC1). Next, we excluded all non-English refined set of 509 publications. Finally, from this pool of
papers,weappliedthefollowingcriteriatoensurerelevance
| publications | (FC2). | These | preliminary | filters | were | imple- |     |     |     |
| ------------ | ------ | ----- | ----------- | ------- | ---- | ------ | --- | --- | --- |
mentedtoensurethatthefinalselectionincludedonlyrecords to our study: a primary focus on blockchain transaction
with complete and accurate information suitable for further networkanalysis,aclearlydefinedmethodologyforanomaly
analysis.Afterthesesteps,1,933publicationswereretained, detection,andeitheranempiricalevaluationoratheoretical
spanningvariousdocumenttypes,asshowninFig.1. foundation (FC7). As a result, we obtained a final set of
103publicationsonanomalydetectionincryptoassets.These
| Next, | we selected | publications |     | categorized | as  | articles, |     |     |     |
| ----- | ----------- | ------------ | --- | ----------- | --- | --------- | --- | --- | --- |
preprints, or book chapters (FC3). Book chapters were publications were examined and compared based on their
included because many conference papers are published in methodology, data sources, and reported performance. The
this format. After narrowing these categories, we excluded completeselectionprocessisillustratedinFig.4.
| review or | survey | papers (FC4), | resulting | in  | 1,438 research |     |     |     |     |
| --------- | ------ | ------------- | --------- | --- | -------------- | --- | --- | --- | --- |
papers,and215review/surveypaperswereremoved.Byplot- 2) CLASSIFICATIONFRAMEWORK
tingthepublicationyearsofthesepapersasshowninFig.2, Wedevelopedamulti-dimensionalclassificationframework
weobserveanotablegrowthstartingin2009,theyearBitcoin to systematically organize and analyze the diverse body of
wasintroduced.Notethattheapparentdropfor2025isdueto research on anomaly detection in cryptoasset transaction
thepartialdatacollectedearlyinthatyearanddoesnotreflect networks. This framework distinguishes between primary
a decline in research interest. Consequently, we excluded dimensions, which represent fundamental characteristics
| 202578 |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
of artificially influenced market activity. Furthermore,
the domain of network security enhancement typically
involves detecting contextual or collective anomalies
related to protocol misuse or network-level attacks.
Classifyingstudiesbytheirapplicationdomainclarifies
the practical objective of the proposed techniques and
the specific kinds of divergent or aberrant behaviors
they are designed to identify within the blockchain
ecosystem.
While the primary dimensions, particularly methodology,
provide the main structure for this SoK, analyzing the
literature through secondary dimensions offers valuable
additionalinsightsandrevealsfurthernuances:
• Temporal Aspects: Studies can be viewed based on
whether they perform a static analysis on a snapshot
of the network or employ dynamic analysis to capture
temporalevolutionandbehavioralchangesovertime.
• Scale of Analysis: Techniques may operate at dif-
ferent granularities, focusing on node-level behavior
FIGURE4. Literaturereviewworkflow. (individual addresses/transactions), subgraph patterns
(localneighborhoodsorcommunities),ornetwork-wide
properties.
dictatingthecorenatureofthedetectionapproach,andsec-
ondarydimensions,whichoffercomplementaryperspectives Nonetheless, while recognizing the value of these multiple
for finer-grained analysis. The primary dimensions guiding perspectives, this SoK adopts the detection methodology as
ourclassificationare: the central organizing principle for the in-depth discussion
as it allows for a focused comparison of the core technical
• Detection Methodology: This is the cornerstone of
advancements and sets a clear direction for evaluating the
our classification and forms the primary axis for
state-of-the-artincryptoassetanomalydetection.
the detailed review presented in Section III. We cat-
egorize techniques based on their core algorithmic
II. DEFININGANDCHARACTERIZINGANOMALIESIN
approach into statistical methods, network analysis
BLOCKCHAINTRANSACTIONNETWORKS
techniques, machine learning approaches (including
A. BLOCKCHAINANDCRYPTOASSETFUNDAMENTALS
supervised, unsupervised, and deep learning), and
A blockchain is a type of Distributed Ledger Technology
heuristic-based strategies. We consider methodology
(DLT) that records transactions in a decentralized and
paramount because it fundamentally shapes the detec-
immutablemanner.Securityismaintainedthroughachainof
tionprocess,dictatingdatarequirements,computational
cryptographically linked blocks, where each block contains
complexity,interpretability,andthetypesofanomalies
transaction data, a timestamp, and a hash of the preceding
atechniqueisbestsuitedtoidentify.Itreflectsthecore
block. This structure makes tampering with historical data
technicalinnovationsandprovidesaclearstructurefor
computationallyinfeasible.
comparingresearchcontributions.
Blockchainsystemsprimarilyusetwotransactionmodels,
• Data Sources: Another critical primary dimension
asillustratedinFig.5.
distinguishes whether methods rely on on-chain data
(publiclyavailableontheblockchainledger),off-chain • Unspent Transaction Output (UTXO) model: Used
data(externalsourceslikemarketprices,socialmedia, by Bitcoin, this model tracks discrete chunks of cryp-
or proprietary information), or a hybrid combination. toassets. Each transaction consumes existing UTXOs
The data source fundamentally limits or enables the andgeneratesnewones,providingclearassettraceabil-
scopeofdetectableanomalies. itywhichisvaluableforforensicanalysis.
• ApplicationDomain:Thisdimensionclassifiesstudies • Account-basedmodel:UsedbyEthereum,thismodel
based on their intended target area, directly relating functionslikeabankaccount,maintainingabalancethat
to the types of anomalies (as defined in section I:A) isdirectlydebitedorcredited.Thisapproachsimplifies
theyaimtodetect.Forinstance,techniquesfocusedon statemanagement,especiallyforapplicationsinvolving
financialfrauddetectionmightsearchforspecificpoint smartcontracts.
anomaliesintransactionsorparticularpatternsofcollec- Networkintegrityandagreementontheledger’sstateare
tive anomalies suggestive of illicit fund flows. Studies ensured by consensus mechanisms. The two most common
targeting market manipulation analysis often seek are Proof-of-Work (PoW), which relies on computational
particular collective or contextual anomalies indicative power(mining)tovalidatetransactions,andProof-of-Stake
VOLUME13,2025 202579

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
FIGURE5. IllustrationoftheUnspentTransactionOutput(UTXO)model(left)andtheaccount-basedmodel(right).Onthe
left,eachtransactionconsumesspecificoutputs(e.g.,400BTC,500BTC)andcreatesnewoutputs,someofwhichremain
unspent.Ontheright,thesystemtracksaccountbalances,transitioningfromoneglobalstate(Staten+1)tothenext(State
n+2,n+3)astransactionsoccur.
(PoS), where participants stake their own cryptoassets to However,inpractice,manyanomaliesstraddlemultiplecat-
securethenetwork.Botharedesignedtopreventfraudulent egoriesandtargetdifferentecosystemlevels,fromindividual
activities like double-spending. PoS generally consumes transactions to consensus mechanisms and smart contracts.
significantly less energy than PoW and can potentially Thefollowingpartwilldiscusscommonanomalyandattack
offer better scalability. However, it also introduces different types, illustrating how they map to the anomaly categories
security considerations and potential risks, such as the andhowtheymanifestinreal-worldscenarios.
‘‘nothing at stake’’ problem, though mechanisms exist to
mitigatethis. 1) TRANSACTION-LEVELFRAUDANDABUSES
Transactions on blockchains are pseudonymous, not • Double-SpendingAttempts(Point/Contextual):This
anonymous. Users operate via cryptographic addresses, type of anomaly involves an attacker broadcasting two
whicharenotdirectlytiedtoreal-worldidentities.However, conflictingtransactionsthatspendthesamecoins,aim-
patterns in transaction data can be analyzed to cluster ingtoinvalidateonetransactionafterarecipientbelieves
addresses and potentially de-anonymize users, a key con- it is confirmed. Although consensus mechanisms like
siderationforforensicinvestigation.Furthermore,platforms PoWorPoSaredesignedtomitigatesuchattacks,low
likeEthereumsupporttwodistinctaccounttypes:Externally confirmation times or chain reorganizations may allow
Owned Accounts (EOAs), which are controlled by users double-spending to succeed. In practice, this anomaly
via private keys, and Smart Contract Accounts, which often appears as nearly identical transactions issued in
are governed by their own embedded code. Smart con- rapidsuccessionfromthesameaddress,frequentlywith
tracts are self-executing programs that enable decentralized one transaction replaced by another (e.g., via higher
applications (dApps) by automating complex logic. A key fees). Successful double spending can lead to direct
distinction relevant to anomaly detection is that only EOAs financial losses for merchants or service providers that
can initiate transactions; smart contracts can only react to acceptunconfirmedtransactions.
transactionstheyreceivefromEOAsorothercontracts.This • Single Large/Outlier Transfers (Point): Single large
interaction creates unique on-chain patterns and introduces transfers that greatly exceed an address’s historical
vulnerabilities that can be exploited, making smart contract transactionsizesoftenrepresentpointanomalies.They
behavior a significant source of detectable anomalies. For a are particularly suspicious when coming from an
morecomprehensiveoverviewofblockchaintechnology,its address known for relatively modest activity or when
architecture,anddiverseapplications,werefertheinterested the receiving address is newly created or previously
readertofoundationalreviews[22],[23]. inactive. Such outlier transactions may indicate an
exchangehack,insidertrading,orliquidationofillicitly
B. COMMONANOMALIES/ATTACKS obtainedfunds.Awell-knownhistoricalexampleisthe
Classifying anomalies into point, contextual, and collective Mt. Gox hack, where enormous amounts of Bitcoin
provides a valuable framework for understanding how were siphoned from the exchange’s hot wallets over
malicious behaviors may manifest in blockchain networks. time.Althoughsomeofthetransferswerenotobviously
202580 VOLUME13,2025

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
suspicious at first glance, subsequent investigations Although each payment might be a point anomaly,
revealed a pattern of repeated large outflows that viewing them collectively can also reveal patterns. For
ultimately contributed to the collapse of the platform. instance, the same address receives repeated payments
Becauseasingleoutliercantriggerheightenedscrutiny, from geographically dispersed victims. This dual per-
attackers sometimes break large amounts into smaller, spective underscores how many anomalies cross the
timedmovementstoevadedetection—highlightinghow linebetweenpointandcollectivecategories,especially
anomaliescanevolveintomorecomplexpatternswhen if attackers systematically reuse addresses or quickly
| attackersactrepeatedly. |         |         |          |             |          |          | laundercollectedfunds. |     |     |     |     |     |     |
| ----------------------- | ------- | ------- | -------- | ----------- | -------- | -------- | ---------------------- | --- | --- | --- | --- | --- | --- |
| • Phishing/Dusting      |         | Attacks | (Point): |             | Phishing | in the   |                        |     |     |     |     |     |     |
| cryptoasset             | context | can     | involve  | unsolicited |          | messages |                        |     |     |     |     |     |     |
3) MARKETMANIPULATIONS(MM)
promptinguserstosendfundsorsignmalicioustransac-
|     |     |     |     |     |     |     | • Pump-and-Dump |     | Schemes |     | (Collective): |     | Pump-and- |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | --- | ------------- | --- | --------- |
tionswhiledustingattacksentailsendingtrivial‘‘dust’’
|     |     |     |     |     |     |     | dump schemes |     | rely | on a | coordinated | group | rapidly |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---- | ---- | ----------- | ----- | ------- |
amountsofcryptoassettonumerousaddresses.Though
buyinganilliquidtoken,drivinguptheprice(thepump),
| each dust | transaction | is           | small, | they          | can reveal | wallet      |              |     |       |          |     |       |             |
| --------- | ----------- | ------------ | ------ | ------------- | ---------- | ----------- | ------------ | --- | ----- | -------- | --- | ----- | ----------- |
|           |             |              |        |               |            |             | then selling | off | their | holdings | en  | masse | (the dump). |
| ownership | links       | collectively |        | if recipients |            | consolidate |              |     |       |          |     |       |             |
Whileeachpurchaseorsalealonecouldresemblenor-
| dust in | a single | output. | These | attacks | often | coincide |     |     |     |     |     |     |     |
| ------- | -------- | ------- | ----- | ------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
maltradingactivity,thecollectiveeffectisabruptprice
| with unusual |     | traffic spikes |     | of micro-transactions |     | to  |     |     |     |     |     |     |     |
| ------------ | --- | -------------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andvolumespikesfollowedbyadramaticcrash.These
| unconnected | addresses, |        | marking | a contextual |           | anomaly |          |           |            |           |              |     |             |
| ----------- | ---------- | ------ | ------- | ------------ | --------- | ------- | -------- | --------- | ---------- | --------- | ------------ | --- | ----------- |
|             |            |        |         |              |           |         | schemes  | often     | involve    | off-chain | coordination |     | on social   |
| when viewed | against    | normal |         | transaction  | profiles. | The     |          |           |            |           |              |     |             |
|             |            |        |         |              |           |         | media or | messaging | platforms, |           | combining    |     | an on-chain |
initialdustmightseeminnocuous;however,combining
|     |     |     |     |     |     |     | collective | anomaly | with | an  | external | organizational |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ---- | --- | -------- | -------------- | --- |
theseminuteinputscanhelpadversariesde-anonymize
|     |     |     |     |     |     |     | layer [24]. | Exchanges |     | or regulators |     | monitoring | trade |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | ------------- | --- | ---------- | ----- |
users,eventuallysettingthestageforlargerattacks.
|     |     |     |     |     |     |     | volume       | patterns | and | market | sentiment | can  | sometimes  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------ | --------- | ---- | ---------- |
|     |     |     |     |     |     |     | detect these | schemes  |     | early, | although  | many | happen too |
2) ILLICITFINANCIALACTIVITIES
quicklyfortimelyintervention.
| Money-Laundering |     | (Collective): |     | Money |     | laundering |     |     |     |     |     |     |     |
| ---------------- | --- | ------------- | --- | ----- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
•
• WashTrading(Contextual/Collective):Washtrading
| in cryptoassets |     | frequently | takes | the | form of | layering, |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | ----- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
involvesthesameparty(orcolludingparties)repeatedly
| where funds | are | passed | through | multiple | addresses | or  |     |     |     |     |     |     |     |
| ----------- | --- | ------ | ------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
buyingandsellinganassettoinflatevolumeorstabilize
| mixing       | services | to obfuscate |        | their origins. |        | Individual |                  |         |         |             |     |        |              |
| ------------ | -------- | ------------ | ------ | -------------- | ------ | ---------- | ---------------- | ------- | ------- | ----------- | --- | ------ | ------------ |
|              |          |              |        |                |        |            | prices. Although |         | each    | transaction | can | look   | typical, the |
| transactions | in       | a laundering | scheme | may            | appear | unre-      |                  |         |         |             |     |        |              |
|              |          |              |        |                |        |            | combined         | pattern | reveals | frequent    |     | trades | between the  |
markable,butcollectively,theyshowrepeatedsplitting,
|     |     |     |     |     |     |     | same addresses |     | with | minimal | net movement |     | of funds. |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---- | ------- | ------------ | --- | --------- |
merging,oridenticalsumsmovinginrapidsuccession.
|                  |     |                   |     |             |           |            | This is | especially   | common |         | in newer | token   | markets    |
| ---------------- | --- | ----------------- | --- | ----------- | --------- | ---------- | ------- | ------------ | ------ | ------- | -------- | ------- | ---------- |
| These multi-hop, |     | near-simultaneous |     |             | transfers | suggest    |         |              |        |         |          |         |            |
|                  |     |                   |     |             |           |            | or NFT  | marketplaces |        | wanting | to       | project | artificial |
| that a cluster   |     | of addresses      | is  | cooperating |           | to conceal |         |              |        |         |          |         |            |
liquidity.Ifablockchainrecordsalltradestransparently,
| the trail. | Although | on-chain |     | mixers | can add | further |     |     |     |     |     |     |     |
| ---------- | -------- | -------- | --- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
analyzingrepeatedaddresspairs,cyclicalflows,ornear-
| complexity, | certain | transaction-flow |     |     | signatures, | like |          |       |            |     |                  |     |           |
| ----------- | ------- | ---------------- | --- | --- | ----------- | ---- | -------- | ----- | ---------- | --- | ---------------- | --- | --------- |
|             |         |                  |     |     |             |      | zero net | gains | can expose |     | the manipulative |     | nature of |
uniformamountsorsynchronizedtiming,helpforensic
washtrading.
analystsflagthesecollectiveanomalies.
|           |           |     |                 |     |     |          | Front-Running |     | and | MEV | (Contextual): |     | Front- |
| --------- | --------- | --- | --------------- | --- | --- | -------- | ------------- | --- | --- | --- | ------------- | --- | ------ |
| Terrorist | Financing |     | and Dark-Market |     |     | Payments | •             |     |     |     |               |     |        |
•
runningariseswhenanentity(oftenaminer,validator,
(Contextual/Collective):Illicitfinancingforextremist
|     |     |     |     |     |     |     | or specialized |     | bot) reorders |     | transactions |     | in a block |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------- | --- | ------------ | --- | ---------- |
groupsordark-marketpurchasesoftenentailscontextual
|            |         |       |      |       |      |           | to exploit | opportunities |     | such | as  | large | swaps on a |
| ---------- | ------- | ----- | ---- | ----- | ---- | --------- | ---------- | ------------- | --- | ---- | --- | ----- | ---------- |
| anomalies, | wherein | funds | move | to or | from | addresses |            |               |     |      |     |       |            |
decentralizedexchange.Thesereorderingscreatesmall
| known | for high-risk | activity |     | around | specific | events. |     |     |     |     |     |     |     |
| ----- | ------------- | -------- | --- | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
timewindowswhereanattackercaninsertatransaction
Isolatedtransactionsmightappearnormal,butacloser
|         |         |      |           |     |           |        | that profits | from | price | movements |     | [25]. | Observing |
| ------- | ------- | ---- | --------- | --- | --------- | ------ | ------------ | ---- | ----- | --------- | --- | ----- | --------- |
| look at | timing, | such | as spikes | in  | donations | during |              |      |       |           |     |       |           |
repeatedoccurrencesofnewlyinsertedtransactionsjust
notableextremistevents,canconfirmsuspiciousintent.
beforelargeuserswapsindicatesacontextualanomaly,
Inmanycases,intelligencefromexternalsources(e.g.,
|     |     |     |     |     |     |     | which is | normal | from | a transactional |     | standpoint | but |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---- | --------------- | --- | ---------- | --- |
law-enforcementwatchlists,dark-webscraping)reveals
|            |     |             |      |          |     |             | suspicious  | in block | order. | Miner/validator |     |         | extractable |
| ---------- | --- | ----------- | ---- | -------- | --- | ----------- | ----------- | -------- | ------ | --------------- | --- | ------- | ----------- |
| links that | are | not evident | from | on-chain |     | data alone. |             |          |        |                 |     |         |             |
|            |     |             |      |          |     |             | value (MEV) | can      | become | systemic        |     | if left | unchecked,  |
Thus,theseanomaliesoftenrequiremergingblockchain
impactingDeFimarketsbyconsistentlydisadvantaging
| analysis | with off-chain |     | intelligence | to  | achieve | reliable |     |     |     |     |     |     |     |
| -------- | -------------- | --- | ------------ | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
ordinaryusers.
detection.
| • Ransomware |     | Payments | (Point/Contextual): |     |     | When |     |     |     |     |     |     |     |
| ------------ | --- | -------- | ------------------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
attackersencryptvictims’dataanddemandcryptoasset 4) NETWORK/CONSENSUSATTACKS
inreturnfordecryptionkeys,theresultingransomware • 51%Attacks(Collective):Attacksagainsttheconsen-
paymentstypicallypresentaslarge,one-offtransactions suslayer,suchas51%attacksorselfishmining,arenot
to an address tied to a known strain of ransomware. strictly transactional anomalies but significantly affect
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 202581 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
transactionswhenmaliciousminersrewriteorwithhold TABLE1. Anomalieslistedinpublictagpacks.
| blocks. A  | sudden    | concentration | of               | hashing  | or staking   |     |     |     |
| ---------- | --------- | ------------- | ---------------- | -------- | ------------ | --- | --- | --- |
| power can  | lead to   | chain         | reorganizations, |          | invalidating |     |     |     |
| previously | confirmed | transactions  | or               | enabling | double-      |     |     |     |
spending.Inthecaseofselfishmining,anentitymines
| blocks in | private                  | and selectively | publishes |     | them to the |     |     |     |
| --------- | ------------------------ | --------------- | --------- | --- | ----------- | --- | --- | --- |
| network   | to gain disproportionate |                 | rewards.  |     | Monitoring  |     |     |     |
blockproductionandcorrelatingitwithunusualtransac-
| tion reversals | can | expose | these anomalies, |     | which often |     |     |     |
| -------------- | --- | ------ | ---------------- | --- | ----------- | --- | --- | --- |
involvebothprotocol-levelirregularitiesandsuspicious
transactionpatterns.
| Selfish Mining | or  | Block | Withholding | (Contextual): |     |     |     |     |
| -------------- | --- | ----- | ----------- | ------------- | --- | --- | --- | --- |
•
| In selfish | mining, | a miner | (or pool) | withholds | newly |     |     |     |
| ---------- | ------- | ------- | --------- | --------- | ----- | --- | --- | --- |
minedblocksfromthepublicnetwork,secretlybuilding
| a private | branch of | the | chain. By selectively |     | releasing |     |     |     |
| --------- | --------- | --- | --------------------- | --- | --------- | --- | --- | --- |
theseblockslater,theminercancreatereorganizations
that invalidate others’ blocks and claim more rewards. effectively functioning as Ponzi or pyramid schemes.
Block withholding shares similar dynamics; miners Analyzing on-chain flows reveals a systematic pattern
choose not to publish certain blocks, potentially to inwhichinitialinvestorsreceivepayoutsdrawnentirely
collude or manipulate difficulty. These behaviors rep- from the capital contributed by newer participants.
resent contextual anomalies because they deviate from Each individual deposit may not look out of place,
theexpectedblock-discoverypattern;asinglewithheld but collectively, the scheme exhibits unsustainable
|             |      |         |              |     |             | ‘‘rewards’’ with | minimal legitimate | revenue. Detecting |
| ----------- | ---- | ------- | ------------ | --- | ----------- | ---------------- | ------------------ | ------------------ |
| block might | seem | benign, | but repeated |     | withheld or |                  |                    |                    |
privatelyminedblockscanyieldpersistentadvantages. these vulnerabilities involves tracking net inflows and
Overtime,suchstrategiesthreatennetworkfairnessand outflowsovertime,oftenrequiringaddressclusteringto
reducesecurityassurancesforhonestparticipants. identifyrepeatedparticipants.
| 5) SMART-CONTRACTVULNERABILITIES |     |     |     |     |     | 6) ADDRESSCLUSTERING |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | -------------------- | --- | --- |
• Reentrancy Attacks (Contextual/Collective): Reen- Even though address clustering is not itself a direct attack,
trancyvulnerabilitiesarisewhenacontractsendsfunds it can have significant security and privacy implications.
(or triggers external calls) before updating its state. By grouping multiple addresses likely controlled by the
Attackers can exploit this to repeatedly call the same same entity, often identified through heuristics such as
function (e.g., a withdrawal method) within a single co-spending, shared key usage, or overlapping transaction
transaction or block, draining the contract’s balance in patterns, investigators and adversaries can deanonymize
small increments. Although each call may look like users who believed they were pseudonymous. Moreover,
a normal contract interaction, the sequence viewed studiesoftransactionnetworksfrequentlyrevealcentralizing
collectively reveals an anomalous pattern of repetitive tendenciesdespitetheunderlyingblockchain’sdecentralized
withdrawals in a very short timeframe. A reentrancy architecture: influential ‘‘hub’’ addresses (e.g., exchanges,
exploitmaybeginasasinglesuspiciouscall(contextual mixers, or large custodial services) interact with a dispro-
anomaly)butoftenescalatesintoachainofexploitcalls portionately high number of other addresses, effectively
thatconstituteacollectiveanomaly. concentratingtransactionflow.Thishub-and-spokestructure
• Integer Overflow/Underflow (Point/Contextual): diminishes the ideal of evenly distributed control, creating
Poorly coded smart contracts that do not enforce safe singlepointsoffailureorheightenedregulatoryfocus.From
arithmetic can allow counters or balances to ‘‘wrap a detection standpoint, clustering can pinpoint suspiciously
around’’ when they exceed a maximum integer value large hubs or flows of illicit funds, yet from a privacy
(overflow) or drop below zero (underflow). Such perspective,itcanexposeuserrelationshipsandcompromise
sudden, erratic changes in contract state variables— anonymity,underscoringhowthesamenetworkanalyticscan
like a token balance jumping from near-zero to a huge be both a valuable investigative tool and a serious privacy
| number—can | stand | out | as a point anomaly. |     | If multiple | concern. |     |     |
| ---------- | ----- | --- | ------------------- | --- | ----------- | -------- | --- | --- |
overflowexploitsoccurrapidly,theymayalsobeviewed Theseanomaliesoftencombineorevolveacrossmultiple
as contextual anomalies. These attacks can quickly categories,creatingwhatcanbetermed‘‘layeredcomplexi-
crippleacontract’slogic,enablingunauthorizedminting ties.’’Forinstance,asinglesuspicioustransactionmaylead
oftokensorerroneouspayouts. investigators to uncover a larger laundering operation or
• Ponzi and Pyramid Schemes (Collective): Certain a 51% attack can be accompanied by deliberate double-
decentralized applications promise outsized returns spendingattempts.Similarly,theboundariesbetweenpoint,
to early participants at the expense of later ones, contextual, and collective anomalies can blur: while a
| 202582 |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | ------------- |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
TABLE2. Top10cryptoassetsinvolvedinanomalieslistedintable1. a comprehensive taxonomy depicted in Fig.6. This tax-
|     |     |     |     |     |     |     |     | onomy         | categorizes | existing    | anomaly         |               | detection | techniques |         |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | ----------- | --------------- | ------------- | --------- | ---------- | ------- |
|     |     |     |     |     |     |     |     | into four     | primary     | groups      | based           | on            | their     | core       | method- |
|     |     |     |     |     |     |     |     | ological      | approaches: | statistical |                 | analysis,     | network   | analysis,  |         |
|     |     |     |     |     |     |     |     | machine       | learning,   | and         | heuristic-based |               | methods.  | Each       | pri-    |
|     |     |     |     |     |     |     |     | mary category |             | further     | comprises       | subcategories |           | that       | reflect |
specificmethodologicalcharacteristics,analyticalstrategies,
orunderlyingtheoreticalprinciples.
|     |     |     |     |     |     |     |     | Our rationale  |             | for selecting |               | these   | categories    | is based  | on        |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | ------------- | ------------- | ------- | ------------- | --------- | --------- |
|     |     |     |     |     |     |     |     | methodological |             | clarity       | and practical |         | relevance     | observed  | in        |
|     |     |     |     |     |     |     |     | the existing   | literature. |               | Statistical   | methods | employ        | quantita- |           |
|     |     |     |     |     |     |     |     | tive analysis, | anomaly     |               | scoring,      | and     | probabilistic | modeling  |           |
|     |     |     |     |     |     |     |     | to identify    | deviations  |               | from expected |         | transaction   |           | patterns. |
reentrancy exploit may first appear as a single abnormal Networkanalysistechniquesleverageblockchaintransaction
| transaction | call, | repeated | invocations |     | reveal | a collective |     |         |            |     |             |                 |     |     |          |
| ----------- | ----- | -------- | ----------- | --- | ------ | ------------ | --- | ------- | ---------- | --- | ----------- | --------------- | --- | --- | -------- |
|             |       |          |             |     |        |              |     | graphs’ | structural | and | topological | characteristics |     | to  | identify |
pattern.Moreover,manyincidentsunderscorethecriticalrole
|     |     |     |     |     |     |     |     | anomalous | entities | or  | interactions. | Machine |     | learning | meth- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | ------------- | ------- | --- | -------- | ----- |
of off-chain intelligence—such as social-media chatter or ods encompass data-driven algorithms that autonomously
| market announcements—in |           |     | boosting |               | detection | accuracy | for   |                |               |                 |     |             |          |                 |     |
| ----------------------- | --------- | --- | -------- | ------------- | --------- | -------- | ----- | -------------- | ------------- | --------------- | --- | ----------- | -------- | --------------- | --- |
|                         |           |     |          |               |           |          |       | learn patterns |               | from historical |     | transaction |          | data, including |     |
| manipulative            | behaviors |     | like     | pump-and-dump |           | or wash  | trad- |                |               |                 |     |             |          |                 |     |
|                         |           |     |          |               |           |          |       | supervised,    | unsupervised, |                 | and | deep        | learning | frameworks.     |     |
ing. Consequently, effective monitoring requires combining Finally, heuristic-based approaches utilize rule-based or
| on-chain | analytics | with | external | context | to  | capture | the full |                |     |         |       |             |            |     |        |
| -------- | --------- | ---- | -------- | ------- | --- | ------- | -------- | -------------- | --- | ------- | ----- | ----------- | ---------- | --- | ------ |
|          |           |      |          |         |     |         |          | expert-defined |     | models, | often | integrating | analytical |     | models |
spectrumofillicitactivities. or cryptographic properties intrinsic to specific blockchain
| To complement/show |     |     | the | concept | of the | anomalies | dis- |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | ------- | ------ | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
platforms.
| cussed | above | with the | real-world |     | example, | we draw | on  |     |           |     |          |              |     |        |       |
| ------ | ----- | -------- | ---------- | --- | -------- | ------- | --- | --- | --------- | --- | -------- | ------------ | --- | ------ | ----- |
|        |       |          |            |     |          |         |     | The | frequency | of  | research | publications |     | across | these |
the GraphSense TagPack [26], an open-source, community- categories,showninFig.7,indicatescleartrendsandresearch
| maintained | collection |     | of machine-readable |     |     | attribution | tags. |     |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | ------------------- | --- | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
prioritieswithinthecryptoassetanomalydetectionliterature.
Each tag links one or more blockchain addresses to a real- Machinelearningmethodsdominate,accountingfor49outof
worldactor,e.g.,anexchange,darknetmarket,orsanctioned
|     |     |     |     |     |     |     |     | 103 analyzed | studies, | reflecting |     | the increasing |     | emphasis | on  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | ---------- | --- | -------------- | --- | -------- | --- |
entity.
|     |     |     |     |     |     |     |     | adaptive, | data-driven | techniques |     | capable | of  | handling | large- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ---------- | --- | ------- | --- | -------- | ------ |
Table 1 shows that sextortion and mixing-service activity scale,complextransactiondata.Networkanalysisconstitutes
| dominate | in terms | of  | raw address | counts | despite | appearing |     |                    |     |       |      |             |     |             |     |
| -------- | -------- | --- | ----------- | ------ | ------- | --------- | --- | ------------------ | --- | ----- | ---- | ----------- | --- | ----------- | --- |
|          |          |     |             |        |         |           |     | the second-largest |     | group | with | 30 studies, |     | emphasizing | the |
in only two and seven cases, respectively. Both anomaly importance of graph-based perspectives and the structural
| schemes | naturally | generate | long | address | chains | (victims | in  |          |               |     |             |                |     |            |     |
| ------- | --------- | -------- | ---- | ------- | ------ | -------- | --- | -------- | ------------- | --- | ----------- | -------------- | --- | ---------- | --- |
|         |           |          |      |         |        |          |     | analysis | of blockchain |     | transaction | relationships. |     | Heuristic- |     |
sextortioncampaigns,deposit/withdrawalwalletsinmixers),
|     |     |     |     |     |     |     |     | based approaches, |     | 14  | papers, | and | statistical | techniques, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ------- | --- | ----------- | ----------- | --- |
inflatingtheirfootprintrelativetomoreconcentratedevents 10 studies, while fewer in number, still provide significant
| such as | exchange | hacks. | Conversely, |     | only | a handful | of  |           |              |     |             |           |     |               |     |
| ------- | -------- | ------ | ----------- | --- | ---- | --------- | --- | --------- | ------------ | --- | ----------- | --------- | --- | ------------- | --- |
|         |          |        |             |     |      |           |     | insights, | particularly |     | in contexts | requiring |     | transparency, |     |
addresses represent categories like pyramid or phishing, interpretability,orwell-definedprobabilisticframeworks.
| illustrating | the | long-tail | of  | niche but | still | security-critical |     |      |         |          |     |            |     |         |          |
| ------------ | --- | --------- | --- | --------- | ----- | ----------------- | --- | ---- | ------- | -------- | --- | ---------- | --- | ------- | -------- |
|              |     |           |     |           |       |                   |     | Each | primary | category | is  | subdivided | to  | reflect | specific |
threats.
methodologicaldetails.Withinmachinelearningapproaches,
Turningtoplatformdistribution,Table2showsthatBitcoin supervised learning methods rely on labeled training data,
| and Ethereum |     | are the | main | platforms | for | the anomalies. |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ------- | ---- | --------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
makingthemeffectivebutdata-intensive.Unsupervisedand
Together,theyaccountfor44ofthe61annotatedcases(72%), semi-supervisedlearningapproachesaddressdatascarcityby
making them the primary proving ground for detection identifyingintrinsicpatternsoranomalieswithoutextensive
research.Thepresenceofprivacy-enhancingchains(Monero,
|     |     |     |     |     |     |     |     | labeled | data. Network |     | analysis | methods | focus | on  | varying |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | -------- | ------- | ----- | --- | ------- |
Zcash) with at least two packs each highlights the growing analytical scales (node-level, subgraph-level, and network-
| forensic | interest | in assets | explicitly |     | designed | to obfuscate |     |           |          |      |        |           |     |              |     |
| -------- | -------- | --------- | ---------- | --- | -------- | ------------ | --- | --------- | -------- | ---- | ------ | --------- | --- | ------------ | --- |
|          |          |           |            |     |          |              |     | wide) and | consider | both | static | snapshots |     | and dynamic, |     |
flows.Thecaseslistedherehighlightthebreadthoftoday’s
evolvingblockchainenvironments.Heuristic-basedmethods
threat landscape and foreshadow the twin challenges of employ analytical rules derived from expert knowledge or
| scalability | and | cross-ledger | generalization |     |     | that motivate | the |               |     |             |          |              |     |     |        |
| ----------- | --- | ------------ | -------------- | --- | --- | ------------- | --- | ------------- | --- | ----------- | -------- | ------------ | --- | --- | ------ |
|             |     |              |                |     |     |               |     | cryptographic |     | principles, | offering | transparency |     | and | inter- |
taxonomyforhowanomalydetectionmethodsareorganized pretability. At the same time, statistical approaches use
andpresentednext.
rigorousmathematicalframeworkssuchasdistribution-based
|     |     |     |     |     |     |     |     | anomaly | detection, | time-series |     | forecasting, |     | and statistical |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ----------- | --- | ------------ | --- | --------------- | --- |
C. TAXONOMYOFBLOCKCHAINTRANSACTIONANOMALY profilingtoquantifytransactionanomaliessystematically.
DETECTIONTECHNIQUE While this structured taxonomy aids in clearly under-
To systematically analyze anomaly detection methods standing and organizing existing methods, overlaps and
applied to blockchain transaction networks, we propose hybridization among categories exist. For instance, graph
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 202583 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
FIGURE6. Taxonomyofanomalydetectiontechniques.
FIGURE8. Exampleofadirectedtransactiongraphamongfiveaddresses
(A,B,C,D,E).TheedgesareweightedbytheamountofBTCtransferred
fromoneaddresstoanother.
FIGURE7. Distributionofthe103selectedresearchpapersacrossthe statistical approaches serve as one of the earliest lines of
categoriesbasedontheproposedtaxonomy. defenseandcanbeadaptedtoflagbothsuddenoutliers(point
|                 |             |                 |                            |              | anomalies) | and more nuanced | deviations | that unfold over |
| --------------- | ----------- | --------------- | -------------------------- | ------------ | ---------- | ---------------- | ---------- | ---------------- |
| neural networks |             | combine machine | learning                   | and network- | time.      |                  |            |                  |
| analytic        | techniques, | indicating      | evolving interdisciplinary |              |            |                  |            |                  |
approaches. Such intersections underscore the dynamic E. TRANSACTIONGRAPHSANDNETWORKCONCEPTS
natureofthefield,revealingopportunitiesforfuturemethod-
|     |     |     |     |     | Analyzing | cryptoasset transactions | through | the lens of |
| --- | --- | --- | --- | --- | --------- | ------------------------ | ------- | ----------- |
ological innovation. The subsequent section systematically network science provides powerful tools for understanding
explores each category in-depth, comparing methodologies, the flow of value, identifying influential participants, and
| highlighting | their | strengths and | limitations, and | identifying |                     |             |                 |            |
| ------------ | ----- | ------------- | ---------------- | ----------- | ------------------- | ----------- | --------------- | ---------- |
|              |       |               |                  |             | detecting anomalous | activities. | By representing | blockchain |
keyresearchgaps. dataasgraphs,wecanleveragewell-establishedgraphtheory
conceptsandalgorithmstogaininsightsthatmightbehidden
D. CONCEPTSINSTATISTICALMETHODS whenexaminingindividualtransactionsinisolation.
Statisticalanalysisapproachesincryptoassetnetworkscom- Cryptoassettransactionnetworkscanbenaturallymodeled
monly center on modeling typical transaction or market as graphs. Typically, such graphs are constructed by aggre-
behaviorsviaprobabilitydistributions,time-seriesanalyses, gatingtransactionsoccurringwithinaspecifictimewindow,
or multivariate control frameworks. By measuring devia- e.g.,hourly,daily,orweekly,tocreateasnapshotofnetwork
tions from these established ‘‘normal’’ baselines—whether activity.Mathematically,thissnapshotisrepresentedasG=
through simple metrics like mean and variance or more (V,E)wherenodesV representaddressesortransactionsand
advanced techniques like autoregressive models and tensor- edges E represent relationships or interactions, such as the
based analyses—these methods can highlight anomalous transferoffunds.Forexample,ifuserAsendsx amountof
spikesorpatternsthatsuggestfraudulentactivity.Crucially, tokenstouserB,touserB,werepresentthisasadirectededge
| 202584 |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | ------------- |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
fromnodeAtonodeBweightedbyx,seeFig.8forthesimple • ClosenessCentrality:Indicateshowcloseanodeisto
illustration of the transaction graph. Edges in cryptoasset all other nodes, useful for identifying influential nodes
graphsareusuallydirectedduetothenatureoftransactions, orkeyintermediaries.
i.e.sendertoreceiver,andoftenweightedbytransactionvalue
|     |     |     |     |     |     |     |     |     |     |     |     |     | N −1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
(v)=
orfrequency.Thisdirectednatureallowstrackingtheflowof C C P (4)
d(u,v)
| fundsclearlyfromorigintodestination. |     |     |     |     |     |     |     |     |     |     |     | u∈V |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Several standard graph representations are employed to whered(u,v)istheshortestpathdistancebetweennodes
| analyzeblockchaindata: |     |     |     |     |     |     |     | uandv. |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
BetweennessCentrality:Measurestheextenttowhich
| • TransactionGraph:Nodesrepresentindividualtrans- |     |     |     |     |     |     |     | •   |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
actions, and edges indicate the flow of funds between anodeliesonpathsconnectingothernodes,pinpointing
| transactions. |     |     |     |     |     |     |     | nodescriticalforinformationorvalueflow. |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
• U s e r G r ap h s : N o d e s r e p r e s e n t b lo c k c h a in a d d r e s s es o r X σ (v)
|     |     |     |     |     |     |     |     |     |     |     | (v)= |     | s t |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
us e r s, an d e d g e sr e fl e c t i n t e ra c t io n s o r t ra n sf e r s b e t w ee n C B (5)
σ
|     |     |     |     |     |     |     |     |     |     |     |     | s̸=v̸=t∈V | st  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
addresses/users.
| • Interaction                                     |     | Graphs: | Abstract |     | representation |     | where |         | σ   |            |            |       |        |             |        |
| ------------------------------------------------- | --- | ------- | -------- | --- | -------------- | --- | ----- | ------- | --- | ---------- | ---------- | ----- | ------ | ----------- | ------ |
|                                                   |     |         |          |     |                |     |       | where   |     | st denotes | the        | total | number | of shortest | paths  |
| nodescanrepresententitiessuchaswallets,exchanges, |     |         |          |     |                |     |       |         |     |            |            |       | σ      |             |        |
|                                                   |     |         |          |     |                |     |       | between |     | nodes      | s and node | t,    | and    | (v) is the  | number |
st
or contracts, with edges denoting various forms of ofthosepathspassingthroughnodev.
interactions.
|              |     |             |     |            |             |     |      | Community |     | detection | in  | cryptoasset | networks |     | involves |
| ------------ | --- | ----------- | --- | ---------- | ----------- | --- | ---- | --------- | --- | --------- | --- | ----------- | -------- | --- | -------- |
| These graphs | are | constructed |     | by parsing | transaction |     | data |           |     |           |     |             |          |     |          |
identifyingclustersofaddressesthatexhibitahigherdensity
recordedontheblockchainledger.Eachtransactiontypically
|     |     |     |     |     |     |     |     | of interactions |     | among | themselves |     | than with | the rest | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----- | ---------- | --- | --------- | -------- | ------ |
links one or more input addresses to one or more output network. By leveraging techniques such as modularity opti-
addresses.
|         |       |       |         |                   |     |             |     | mization,   | spectral | clustering, |      | or label | propagation, |           | analysts |
| ------- | ----- | ----- | ------- | ----------------- | --- | ----------- | --- | ----------- | -------- | ----------- | ---- | -------- | ------------ | --------- | -------- |
| Several | basic | graph | metrics | help characterize |     | transaction |     |             |          |             |      |          |              |           |          |
|         |       |       |         |                   |     |             |     | can uncover |          | patterns    | that | suggest  | coordinated  | behavior— |          |
networks: be it legitimate operational clusters like exchanges or
• Degree (k): Number of edges connected to a node. suspicious groups potentially involved in fraud or money
For directed graphs, one can distinguish between in- laundering. This approach helps to simplify and elucidate
degree,thenumberofincomingedges,andout-degree,
|     |     |     |     |     |     |     |     | the complex |     | flow | of transactions |     | on the | blockchain | by  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---- | --------------- | --- | ------ | ---------- | --- |
thenumberofoutgoingedges.Thedegreesofnodevare highlighting both central hubs and isolated pockets within
definedas: thenetwork,therebyprovidingcriticalinsightsforregulatory
|     |     |      | X   |         | X   |     |     | compliance | and | risk | management. |     | Despite | challenges | like |
| --- | --- | ---- | --- | ------- | --- | --- | --- | ---------- | --- | ---- | ----------- | --- | ------- | ---------- | ---- |
|     | k   | (v)= | e   | ,k (v)= |     | e   | (1) |            |     |      |             |     |         |            |      |
in uv out vu scalability and the inherently dynamic nature of blockchain
|       |      |          | u∈V  |      | u∈V       |     |          |                 |     |           |     |         |            |     |          |
| ----- | ---- | -------- | ---- | ---- | --------- | --- | -------- | --------------- | --- | --------- | --- | ------- | ---------- | --- | -------- |
|       |      |          |      |      |           |     |          | data, community |     | detection |     | remains | a powerful |     | tool for |
| where | e is | the edge | from | node | u to node | v   | and vice |                 |     |           |     |         |            |     |          |
uv discerning the underlying structure of transaction networks
versa. The degree of node v can be, then, defined as and enhancing the overall understanding of digital currency
| k(v)=k      | (v)+k   |         | (v)    |            |           |             |         |                                                    |     |     |     |     |     |     |     |
| ----------- | ------- | ------- | ------ | ---------- | --------- | ----------- | ------- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|             | in      | out     |        |            |           |             |         | ecosystems.Forthedetailsongraphtheory,referto[27]. |     |     |     |     |     |     |     |
| • Strength: | Extends |         | degree | by summing |           | edge        | weights |                                                    |     |     |     |     |     |     |     |
| connected   | to      | a node, | useful | for        | capturing | transaction |         |                                                    |     |     |     |     |     |     |     |
|             |         |         |        |            |           |             |         | F. MACHINELEARNINGINANUTSHELL                      |     |     |     |     |     |     |     |
volume.
|     |     |     |     |     |     |     |     | Given | the widespread |     | adoption |     | of machine | learning | for |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------------- | --- | -------- | --- | ---------- | -------- | --- |
• ClusteringCoefficient(C):Measureshowcloselycon-
|     |     |     |     |     |     |     |     | anomaly | detection, |     | a dedicated | and | detailed | discussion | is  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | ----------- | --- | -------- | ---------- | --- |
nectedanode’sneighborsaretoeachother,capturingthe
|     |     |     |     |     |     |     |     | warranted. | For | a comprehensive |     | theoretical |     | background | on  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------------- | --- | ----------- | --- | ---------- | --- |
local density of interactions. The clustering coefficient machine-learningalgorithms,readersarereferredtothewell-
ofnodevisdefinedas:
establishedtextbooks[28],[29].
|     |     |       |     | 2T(v) |     |     |     | Machine | learning |     | has progressed |     | rapidly | over | the past |
| --- | --- | ----- | --- | ----- | --- | --- | --- | ------- | -------- | --- | -------------- | --- | ------- | ---- | -------- |
|     |     | C(v)= |     |       |     |     | (2) |         |          |     |                |     |         |      |          |
k(v)(k(v)−1)
decade,findingapplicationsatvastlydifferentfieldsscales,
|       |      |            |     |        |              |     |         | from microscopic |     | processes |     | such | as protein | folding | [30], |
| ----- | ---- | ---------- | --- | ------ | ------------ | --- | ------- | ---------------- | --- | --------- | --- | ---- | ---------- | ------- | ----- |
| where | T(v) | represents | the | number | of triangles |     | through |                  |     |           |     |      |            |         |       |
[31],[32]andbacterialswimmingbehaviors[33],[34],[35],
nodev.
tohumanbehavioral[36],[37],[38],drugdelivery[39],[40]
| Centrality | measures | help | identify | important |     | nodes | within |            |     |                  |     |               |     |      |         |
| ---------- | -------- | ---- | -------- | --------- | --- | ----- | ------ | ---------- | --- | ---------------- | --- | ------------- | --- | ---- | ------- |
|            |          |      |          |           |     |       |        | and onward | to  | enterprise-scale |     | optimizations |     | like | supply- |
transactionnetworks:
|     |     |     |     |     |     |     |     | chain logistics |     | and | manufacturing |     | workflows | [41], | [42]. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ------------- | --- | --------- | ----- | ----- |
• DegreeCentrality:Nodeswithhigherdegreecentrality
|          |             |     |         |               |     |              |     | In the     | context | of  | cryptoasset | analysis, |     | machine  | learning |
| -------- | ----------- | --- | ------- | ------------- | --- | ------------ | --- | ---------- | ------- | --- | ----------- | --------- | --- | -------- | -------- |
| actively | participate |     | in more | transactions, |     | highlighting |     |            |         |     |             |           |     |          |          |
|          |             |     |         |               |     |              |     | offers the | ability | to  | uncover     | subtle    | and | adaptive | patterns |
potentialhubs.
|     |     |     |        |      |     |     |     | of fraudulent                                        |     | or malicious |     | behavior | by learning | from | vast   |
| --- | --- | --- | ------ | ---- | --- | --- | --- | ---------------------------------------------------- | --- | ------------ | --- | -------- | ----------- | ---- | ------ |
|     |     |     |        | k(v) |     |     |     | amountsoftransactiondata,evenasillicittacticsevolve. |     |              |     |          |             |      |        |
|     |     |     | C (v)= |      |     |     | (3) |                                                      |     |              |     |          |             |      |        |
|     |     |     | D      | −1   |     |     |     |                                                      |     |              |     |          |             |      |        |
|     |     |     |        | N    |     |     |     | • Supervised                                         |     | Learning:    |     | In       | supervised  | ML,  | models |
whereN isthetotalnumberofnodes. such as Random Forest or Support Vector Machines
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 202585 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
(SVMs) are trained on labeled examples of normal or burstiness can reveal deviations from historical
versus anomalous transactions. By ‘‘learning’’ how norms.
known anomalies differ from legitimate activity, these • Behavioral Profiles: Aggregating typical transaction
models can then generalize to flag novel suspicious sizes,counterpartyinteractions,ortimingforanaddress
cases.However,constructingareliablelabeleddataset, helpsidentifyuncharacteristicactivitythatmightsignal
especially in decentralized cryptoasset settings, can be accounttakeoverorillicituse.
challengingduetothescarcityofconfirmedfraudlabels • ExternalSignals:Incorporatingoff-chaindata,suchas
and the possibility that malicious actors continuously socialmediasentimentormarketnews,canbecrucial,
changetheirstrategies. especially for detecting coordinated events like pump-
• Unsupervised Learning: Unsupervised approaches and-dumpschemes.
detectanomaliesbymodelingwhat‘‘normal’’datalooks
like,thenmeasuringhowstronglyeachnewtransaction It is important to note the interplay between ML and
deviates from this norm. Clustering techniques like Network Analysis (discussed conceptually in Section II-E).
k-Means or DBSCAN group transactions according to While our taxonomy presents them as distinct methodolog-
similarity,labelingdatapointsinlow-densityregionsor ical families for clarity, insights from network analysis are
forming their own small clusters as outliers. Likewise, often crucial inputs for ML models. Specifically, graph
distance-based methods such as k-Nearest Neighbors metrics such as node centrality, clustering coefficients,
measure each transaction’s distance to its neighbors: or community structure derived from the transaction graph
points whose distances surpass typical thresholds are frequently serve as powerful engineered features for ML
considered anomalies. Unsupervised methods are par- algorithms. This synergy allows ML models to leverage the
ticularly appealing when labeled anomalies are scarce structural properties of the transaction network identified
ornon-existent. throughnetworkanalysistechniques.
• Semi-Supervised Learning: In many real-world Beyondthelearningparadigms,severalalgorithmclasses
blockchainusecases,onlyasmallsubsetoftransactions
arefrequentlyapplied:
canbeconfidentlylabeled,e.g.,ahandfulofconfirmed
• Distance-Based (k-NN): A straightforward yet effec-
scam addresses. Semi-supervised algorithms use this
tive method is k-Nearest Neighbors, where each trans-
limited information to guide the detection process.
action (represented by its feature vector) is evaluated
Acommontacticistotrainamodelprimarilyonnormal
againstitskclosestneighbors.Transactionswithanoma-
data (e.g., one-class SVMs or autoencoders). Hence,
lously large distances are flagged. While simple to
the system learns normal behavior and flags anything
explain,k-NNcanbecomecomputationallydemanding
sufficientlydifferentassuspicious.Thisapproachaligns
in large-scale blockchain applications unless efficient
well with cryptoasset ecosystems, where legitimate
indexingorapproximatemethodsareemployed.
transactionsvastlyoutnumberknownfraudulentcases.
• Deep Learning: Neural networks often excel at cap- • Clustering Methods (k-Means, DBSCAN): In k-
Means, data points are partitioned into k clusters by
turing complex, high-dimensional relationships. Sim-
minimizing the distance to each cluster’s centroid.
ple feed-forward networks and Convolutional Neural
Transactionsfarfromtheirnearestcentroidorassigned
Networks (CNNs) can process time-series or transac-
to extremely small clusters can be considered anoma-
tionalfeatures.Incontrast,RecurrentNeuralNetworks
lies. DBSCAN, in contrast, forms clusters based on
(RNNs)orLongShort-TermMemory(LSTM)networks
density—pointsinsparselypopulatedregionsareauto-
handle sequential data such as address activity over
maticallydeemedoutliers.Thisdensity-drivenapproach
time. A particularly relevant direction involves Graph
can help reveal groups of addresses interacting in a
Neural Networks (GNNs), which encode both node
suspiciouslytightcircle,unconnectedtotherestofthe
(address) attributes and topological information (who
network.
transacts with whom and how often). GNN-based
• Tree-BasedModels:
models can uncover small, densely connected pockets
potentially involved in money laundering or other -- Isolation Forest: isolates data points by randomly
collusive behaviors that might elude less graph-aware splittingfeatures;anomaliestendtobesplitfromthe
methods. rest of the data more quickly, thus receiving higher
anomalyscores.
Effective ML-based anomaly detection critically depends
-- Random Forest: typically a supervised classifier,
on feature engineering. While raw transaction data such
canalsoprovideoutlierscoresbasedonhowconsis-
as addresses, timestamps, and transaction amounts provide
tently a transaction is classified compared to others.
a starting point, additional transformations often boost
In labeled settings, such as a training set of flagged
performance.Commonfeaturetypesinclude:
addresses, Random Forest can be used directly to
• Temporal Features: Capturing time-based patterns classifytransactionsasnormaloranomalous.
like transaction frequency, value changes over time, • NeuralNetworksApproaches:
202586 VOLUME13,2025

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
-- Feed-forwardNNs:learntomapinputfeatures,e.g., • Recall: indicates the proportion of flagged anomalies
transactionsize,frequency,nodeattributes,toascore that are truly anomalous, highlighting how well a
orlabelindicatinganomalylikelihood. detectoravoidsraisingfalsealarms.
|     | -- Graph | Neural | Networks |     | (GNNs): | such | as Graph |     |     |     |     |     |     |     |     |
| --- | -------- | ------ | -------- | --- | ------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
TP
=
|     | ConvolutionalNetworks(GCNs)orGraphAttention |     |     |     |     |     |     |     |     |     | Recall |     |     |     | (8) |
| --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
TP+FN
|     | Networks |     | (GATs) | capture | the | relational | structure |     |     |     |     |     |     |     |     |
| --- | -------- | --- | ------ | ------- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
amongaddresses.Byiterativelycombininginforma- • F1-Score:indicatestheproportionofflaggedanomalies
tion from neighbors, GNNs detect anomalies that that are truly anomalous, highlighting how well a
might appear only when viewed within the broader detectoravoidsraisingfalsealarms.
|     | transactionsubgraph. |     |     |     |     |     |     |     |     |       |     | Precision×Recall |     |     |     |
| --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ---------------- | --- | --- | --- |
|     |                      |     |     |     |     |     |     |     |     | F1=2× |     |                  |     |     | (9) |
Precision+Recall
G. EVALUATIONMETRICSFORANOMALYDETECTION
|     |     |     |     |     |     |     |     | The other | widely | used | metrics | for | evaluating |     | detection |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ---- | ------- | --- | ---------- | --- | --------- |
Anomalydetectionincryptoassetnetworkstypicallyinvolves
identifying rare, illicit, or otherwise suspicious transactions performance are curve-based, offering a more holistic view
|        |        |        |      |           |           |     |              | of how | a classifier’s |     | performance |     | changes | under | varying |
| ------ | ------ | ------ | ---- | --------- | --------- | --- | ------------ | ------ | -------------- | --- | ----------- | --- | ------- | ----- | ------- |
| within | a much | larger | pool | of benign | activity. |     | This setting |        |                |     |             |     |         |       |         |
poses unique challenges for model evaluation, as standard decision thresholds. A Receiver Operating Characteristic
|         |     |                |     |         |             |     |            | (ROC) curve    | plots | the | true positive   |     | rate (recall) | against    | the |
| ------- | --- | -------------- | --- | ------- | ----------- | --- | ---------- | -------------- | ----- | --- | --------------- | --- | ------------- | ---------- | --- |
| metrics | may | not accurately |     | reflect | performance |     | under high |                |       |     |                 |     |               |            |     |
|         |     |                |     |         |             |     |            | false positive | rate  | (1  | - specificity), | and | the           | Area Under | the |
classimbalance.Thefollowingsubsectionsdiscusscommon
metricsandhighlighthowcurve-basedanalysescanprovide ROC Curve (AUC-ROC) summarizes this overall trade-off.
|     |     |     |     |     |     |     |     | Values | closer | to 1.0 | indicate | better | discrimination |     | ability. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ------ | -------- | ------ | -------------- | --- | -------- |
deeperinsightsintoadetector’seffectiveness.
In most real-world datasets, anomalies constitute only a However, when the number of negative (normal) instances
|       |          |     |                     |     |     |           |           | vastly outweighs |     | the | positives | (anomalies), |     | the ROC | curve |
| ----- | -------- | --- | ------------------- | --- | --- | --------- | --------- | ---------------- | --- | --- | --------- | ------------ | --- | ------- | ----- |
| small | fraction | of  | total transactions. |     | For | instance, | malicious |                  |     |     |           |              |     |         |       |
canyieldanoverlyoptimisticpicture.
addressesorfraudulenttradesmaymakeupfarlessthan1%
of on-chain activity. Such class imbalance can undermine Toaddressthislimitation,manyanomaly-detectionstudies
|       |                    |     |     |             |     |           |        | employ | the Precision-Recall |     |     | (PR) curve | and | calculate | the |
| ----- | ------------------ | --- | --- | ----------- | --- | --------- | ------ | ------ | -------------------- | --- | --- | ---------- | --- | --------- | --- |
| naive | metrics—especially |     |     | accuracy—by |     | rewarding | models |        |                      |     |     |            |     |           |     |
that favor classifying the majority of instances as ‘‘nor- Area Under the Precision-Recall Curve (AUC-PR). The PR
|        |               |     |     |         |          |       |         | curve directly |     | focuses | on precision |     | and recall | over | various |
| ------ | ------------- | --- | --- | ------- | -------- | ----- | ------- | -------------- | --- | ------- | ------------ | --- | ---------- | ---- | ------- |
| mal.’’ | Consequently, |     | an  | anomaly | detector | might | achieve |                |     |         |              |     |            |      |         |
thresholds,makingitmoreinformativeinheavilyimbalanced
deceptivelyhighaccuracywhilescarcelyflagginganyactual
anomalies.Thisimbalancealsocomplicatesthetrainingpro- contexts.UnliketheROCcurve,whichplotsallpositiveand
negativesamplesequally,aPRcurvehighlightshowwellthe
| cess: | many | machine-learning |     | algorithms |     | assume | relatively |          |           |      |           |        |       |       |           |
| ----- | ---- | ---------------- | --- | ---------- | --- | ------ | ---------- | -------- | --------- | ---- | --------- | ------ | ----- | ----- | --------- |
|       |      |                  |     |            |     |        |            | detector | maintains | high | precision | (i.e., | keeps | false | positives |
balancedclasses,andtheirperformanceorconvergencecan
degradewhenoneclassoverwhelminglydominatestheother. low)atdifferentlevelsofrecall(i.e.,detectsalargefraction
ofactualanomalies).Inscenarioswhereanomaliesarerare,
ConfusionMatrix(TP,TN,FP,FN):Aconfusionmatrix
provides a granular look at a detector’s outcomes. Here, a high AUC-PR typically provides a clearer picture of a
model’spracticaleffectivenessthanahighAUC-ROCalone.
| True | Positives | (TP) | are correctly |     | identified | anomalies, | True |     |     |     |     |     |     |     |     |
| ---- | --------- | ---- | ------------- | --- | ---------- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Negatives(TN)arecorrectlyidentifiednormaltransactions,
FalsePositives(FP)arenormaltransactionsmisclassifiedas H. APRIMERONHEURISTIC-BASEDAPPROACHES
anomalies and False Negatives (FN) are missed anomalies. Heuristic-based methods rely on expert-defined rules
The following are matrices that are based on the confusion or domain insights to pinpoint suspicious behavior in
blockchaintransactions.Ratherthanlearningamodelpurely
matrix.
Accuracy: fromdata,theseapproachesencodeknown‘‘redflags,’’such
•
|     |     |     |     |     |     |     |     | as unusually | high-frequency |     |     | transactions, | dusting |     | attempts, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | --- | --- | ------------- | ------- | --- | --------- |
TP+TN orrepetitiveoutputpatternsindicativeofmixersortumblers.
|     |     | Accuracy= |     |       |        |     | (6) |     |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |           |     | TP+TN | +FP+FN |     |     |     |     |     |     |     |     |     |     |
Theserulesoftenstemfromforensicexperienceoranalysis
|     |          |          |     |        |               |     |          | of known | attack | patterns. |     | Because | they | draw | on real- |
| --- | -------- | -------- | --- | ------ | ------------- | --- | -------- | -------- | ------ | --------- | --- | ------- | ---- | ---- | -------- |
|     | Although | accuracy |     | is the | most commonly |     | reported |          |        |           |     |         |      |      |          |
metric, it can be misleading in imbalanced scenarios. world observations, heuristics can be especially effective
|     |     |     |     |     |     |     |     | at catching | known | scams | or  | protocol | misuse | in their | early |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ----- | --- | -------- | ------ | -------- | ----- |
Ifanomaliesrepresentonly1%oftransactions,anaive
|     |          |           |                  |         |           |       |            | stages. They | are        | generally | highly         | interpretable, |               | as       | the logic |
| --- | -------- | --------- | ---------------- | ------- | --------- | ----- | ---------- | ------------ | ---------- | --------- | -------------- | -------------- | ------------- | -------- | --------- |
|     | detector | that      | flags everything |         | as normal | could | achieve    |              |            |           |                |                |               |          |           |
|     |          |           |                  |         |           |       |            | is explicit. | However,   |           | their reliance |                | on predefined |          | patterns  |
|     | 99%      | accuracy, | despite          | failing | to detect | any   | suspicious |              |            |           |                |                |               |          |           |
|     |          |           |                  |         |           |       |            | makes them   | inherently |           | brittle;       | they           | typically     | struggle | to        |
activity.
Precision:indicatestheproportionofflaggedanomalies detect novel or unforeseen attack vectors that deviate from
•
knowntactics.Furthermore,asadversariesevolve,theserule
|     | that | are truly | anomalous, |     | highlighting | how | well a |              |            |     |          |     |         |           |      |
| --- | ---- | --------- | ---------- | --- | ------------ | --- | ------ | ------------ | ---------- | --- | -------- | --- | ------- | --------- | ---- |
|     |      |           |            |     |              |     |        | sets require | continuous |     | updating | by  | experts | to ensure | they |
detectoravoidsraisingfalsealarms.
remaineffective.Consequently,heuristicsoftencomplement
|     |     |     |            |     | TP  |     |     | data-driven | approaches |     | rather | than | replacing | them, | for |
| --- | --- | --- | ---------- | --- | --- | --- | --- | ----------- | ---------- | --- | ------ | ---- | --------- | ----- | --- |
|     |     |     | Precition= |     |     |     | (7) |             |            |     |        |      |           |       |     |
TP+FP
example,byactingasaninitialfilter.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 202587 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
III. CASESOFANOMALYDETECTIONANALYSIS in features, at different time points to capture
Inthissection,wecomprehensivelyreviewexistinganomaly higher-orderrelationshipsandinteractioneffectswithin
detection cases applied to cryptoasset transaction networks, the time-series path X(t). Higher-order terms capture
structured according to the previously proposed taxonomy multi-scaletemporaldependencies.Forinstance,S2(X)
shown in Fig.6. While we categorize existing literature into quantifies volatility interactions. To reduce computa-
four broad classes, statistical analysis, network analysis, tional complexity, the randomized signature is often
machine learning, and heuristic-based, there is often con- employed:
| siderable |     | overlap        | in practice. | For      | instance, | some      | studies |     |     |              |     |     |     |     |      |
| --------- | --- | -------------- | ------------ | -------- | --------- | --------- | ------- | --- | --- | ------------ | --- | --- | --- | --- | ---- |
|           |     |                |              |          |           |           |         |     |     | R(X)=A·Sn(X) |     |     |     |     | (12) |
| grounded  |     | in statistical |              | analysis | may       | integrate | machine |     |     |              |     |     |     |     |      |
learning classifiers to enhance outlier detection or employ whereAisarandommatrixwithentriesdrawnfroma
heuristic rules to filter initial datasets. Conversely, purely specified distribution (e.g., Gaussian or Rademacher).
heuristic-drivenmethodsmightincorporatenetworkmetrics
|     |     |     |     |     |     |     |     | These | signatures | signatures |     | were | applied | to  | Bitcoin |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | ---------- | --- | ---- | ------- | --- | ------- |
(e.g.,modularity,centrality)forimprovedanomalyspotting. price-volume time series to detect pump-and-dump
Ourtaxonomythusservesasaconceptualguideratherthan schemes characterized by abrupt price inflations fol-
a rigid classification, reflecting the multifaceted nature of lowed by sharp declines. Empirical evaluation demon-
anomalydetectionincryptoassetecosystems.Toclearlydis- strates the method’s effectiveness, achieving high
tinguishbetweenlocalfrauddetectionandsystemicsecurity
anomaly-detectionperformanceupto0.88F1score.
risks, these methodologies can be viewed through a layered • Benford’s Law: Another relevant approach relies on
lens, i.e. transaction-layer methods target individual value Benford’s Law to detect fraudulent activities and
transfers,network-layeranalysesexposestructuralclustering
unusualbehaviorsincryptoassettransactions[44].This
and flow patterns, and protocol-layer approaches scrutinize law predicts that the leading digits of many naturally
consensusintegrityandsmartcontractvulnerabilities.
|     |     |     |     |     |     |     |     | occurring | numerical |     | datasets | follow |     | a logarithmic |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | -------- | ------ | --- | ------------- | --- |
distribution:
A. STATISTICALANALYSIS
1
We examine a set of studies employing various statistical P(d)=log (1+ ) (13)
10
d
| analyses | to  | detect | anomalies | in cryptoasset |     | transaction | net- |       |          |      |      |               |     |      |      |
| -------- | --- | ------ | --------- | -------------- | --- | ----------- | ---- | ----- | -------- | ---- | ---- | ------------- | --- | ---- | ---- |
|          |     |        |           |                |     |             |      | where | d ranges | from | 1 to | 9. Deviations |     | from | this |
works.Theseapproachesoftenrelyonfundamentalstatistical
|          |      |         |                 |             |              |                 |     | expected       | distribution |               | often      | serve       | as            | indicators  | of   |
| -------- | ---- | ------- | --------------- | ----------- | ------------ | --------------- | --- | -------------- | ------------ | ------------- | ---------- | ----------- | ------------- | ----------- | ---- |
| metrics, | such | as      | mean, variance, |             | correlation, | higher-order    |     |                |              |               |            |             |               |             |      |
|          |      |         |                 |             |              |                 |     | manipulation   |              | or anomalies. |            | Cryptoasset |               | transaction |      |
| moments, |      | or more | advanced        | time-series |              | and regression- |     |                |              |               |            |             |               |             |      |
|          |      |         |                 |             |              |                 |     | data generally |              | fit the       | conditions |             | for Benford’s |             | Law, |
basedmodelingtocharacterize‘‘normal’’behaviorandflag
giventheirinherentlywidenumericalrange.Thestudy
outliers.Asummaryofthestudiescoveredinthiscategoryis
|     |     |     |     |     |     |     |     | of major | cryptoassets |     | such | as Ethereum |     | and | Bitcoin |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | ---- | ----------- | --- | --- | ------- |
presentedintable3and4.
|     |     |     |     |     |     |     |     | from    | 2009 to | 2018 | revealed  | that         | transaction |       | values |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ---- | --------- | ------------ | ----------- | ----- | ------ |
|     |     |     |     |     |     |     |     | closely | adhered | to   | Benford’s | distribution |             | based | on     |
1) DISTRIBUTION-BASEDANDMARKETANOMALY
MeanAbsoluteDeviation(MAD)thresholds,indicating
DETECTION
|     |            |     |         |     |               |          |     | largely | unmanipulated |     | behavior. |     | By contrast, |     | certain |
| --- | ---------- | --- | ------- | --- | ------------- | -------- | --- | ------- | ------------- | --- | --------- | --- | ------------ | --- | ------- |
| •   | Signature: | One | example | of  | a statistical | approach | for |         |               |     |           |     |              |     |         |
othercryptoassets,e.g.,TENX,VERI,andDOGE,were
|     | outlier | detection | involves | using | signature | to  | encoding |     |     |     |     |     |     |     |     |
| --- | ------- | --------- | -------- | ----- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
identifiedasnon-conformingtoBenford’slaw,aligning
|     | time-series | data | into | a collection |     | of iterated | inte- |     |     |     |     |     |     |     |     |
| --- | ----------- | ---- | ---- | ------------ | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
withpreviouslyreportedscandalsandlawsuits.
|     | grals  | [43]. A | truncated | signature  | S(X) | of order          | n for |             |     |            |        |     |         |        |      |
| --- | ------ | ------- | --------- | ---------- | ---- | ----------------- | ----- | ----------- | --- | ---------- | ------ | --- | ------- | ------ | ---- |
|     |        |         |           |            |      |                   |       | Mahalanobis |     | distances: | Robust |     | anomaly | scores | have |
|     | a path | X(t)    | ∈ Rd      | where X(t) | =    | (X1(t),...,Xd(t)) |       | •           |     |            |        |     |         |        |      |
alsobeendevelopedusingMahalanobisdistances(MD)
|     | records | d features, | e.g. | price | or volume, | overtime | t ∈ |                |     |        |       |            |                 |     |     |
| --- | ------- | ----------- | ---- | ----- | ---------- | -------- | --- | -------------- | --- | ------ | ----- | ---------- | --------------- | --- | --- |
|     |         |             |      |       |            |          |     | in cryptoasset |     | market | price | data [45]. | Mathematically, |     |     |
[0,T]isdefinedas:
|     |     |     |     |     |     |     |     | MD measures |     | the distance |     | of a data | point | r   | from the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | --- | --------- | ----- | --- | -------- |
Sn(X)=(1,S1(X),S2(X),...,Sn(X))
|     |        |     |        |     |     |     | (10) | centerofadistribution,accountingforcovariance: |        |           |                     |        |     |            |         |
| --- | ------ | --- | ------ | --- | --- | --- | ---- | ---------------------------------------------- | ------ | --------- | ------------------- | ------ | --- | ---------- | ------- |
|     | where  |     |        |     |     |     |      |                                                |        |           | q                   |        |     |            |         |
|     |        |     |        |     |     |     |      |                                                | MD(r)= |           | (r −µ)T(cid:54)−1(r |        | −µ) |            | (14)    |
|     |        | Z   | T      |     |     |     |      |                                                |        |           |                     |        |     |            |         |
|     | S1(X)= |     | dX(t), |     |     |     |      |                                                |        |           |                     |        |     |            |         |
|     |        |     |        |     |     |     |      | where                                          | µ ∈    | Rn is the | mean                | vector | and | (cid:54) ∈ | Rn×n is |
0
Rn.
|     |        | Z   | T Z t1 |               |     |     |     | the covariance                |     | matrix | of a | random | vector | r ∈ | The |
| --- | ------ | --- | ------ | ------------- | --- | --- | --- | ----------------------------- | --- | ------ | ---- | ------ | ------ | --- | --- |
|     | S2(X)= |     |        |               |     | ),  |     |                               |     |        |      |        |        |     |     |
|     |        |     |        | dX(t 1 )⊗dX(t | 2   |     |     | anomalyscoreAisthendefinedas: |     |        |      |        |        |     |     |
0 0
|     |        | Z   | Z    | Z    |        |        |     |            |             |       |            | M D(r)      |     |            |      |
| --- | ------ | --- | ---- | ---- | ------ | ------ | --- | ---------- | ----------- | ----- | ---------- | ----------- | --- | ---------- | ---- |
|     |        |     | T t1 | t2   |        |        |     |            |             | A(r)= |            |             |     |            |      |
|     | S3(X)= |     |      | dX(t | )⊗dX(t | )⊗dX(t | ),  |            |             |       |            | √           |     |            | (15) |
|     |        |     |      |      | 1      | 2      | 3   |            |             |       |            | n           |     |            |      |
|     |        |     | 0 0  | 0    |        |        |     |            |             |       |            |             |     |            |      |
|     |        | . . |      |      |        |        |     | This score | effectively |       | identifies | significant |     | deviations |      |
.
(11)
incryptoassetreturnsfromtypicalbehavior,effectively
where ⊗ denotes the tensor product. This opera- flagging unusual market movements as anomalies. For
tion combines the vector differentials, i.e. changes instance, it successfully flagged drastic price surges
| 202588 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
during the metaverse boom in late 2021. Moreover, TABLE3. Distribution-based&Marketanomalydetection.
incorporatingMD-basedanomalyconstraintsintoport-
| folio optimization |     | reduced   |     | annual | portfolio | volatility |        |     |     |     |     |     |     |
| ------------------ | --- | --------- | --- | ------ | --------- | ---------- | ------ | --- | --- | --- | --- | --- | --- |
| from over          | 90% | annually  | to  | the    | 40 −      | 50%        | range, |     |     |     |     |     |     |
| underscoring       | the | potential | of  | these  | methods   | for        | risk-  |     |     |     |     |     |     |
sensitiveinvestors.
| Auto-Regressive |     | Moving |     | Average: |     | Furthermore, |     |     |     |     |     |     |     |
| --------------- | --- | ------ | --- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
•
anomaliesinBitcoinpricehavealsobeenstudiedusing
forecastingmethodssuchasSeasonalAuto-Regressive
| Integrated     | Moving     | Average          |           | with          | Exogenous |              | Fac- |     |     |     |     |     |     |
| -------------- | ---------- | ---------------- | --------- | ------------- | --------- | ------------ | ---- | --- | --- | --- | --- | --- | --- |
| tors (SARIMAX) |            | [46].            | By        | incorporating |           | information  |      |     |     |     |     |     |     |
| gathered       | from       | social           | media,    | detecting     |           | manipulative |      |     |     |     |     |     |     |
| practices,     | such       | as pump-and-dump |           |               | schemes,  | becomes      |      |     |     |     |     |     |     |
| highly         | effective. | These            | anomalies |               | were      | especially   |      |     |     |     |     |     |     |
prevalentduringeconomiccrisesandperiodsofintense
| speculation, | including    |     | the market | turbulence |            | observed |       |     |     |     |     |     |     |
| ------------ | ------------ | --- | ---------- | ---------- | ---------- | -------- | ----- | --- | --- | --- | --- | --- | --- |
| during       | the COVID-19 |     | pandemic.  |            | The social |          | media |     |     |     |     |     |     |
sentimentinputimproveddetectioncapabilities,though
| its contribution   |               | was modest |              | during   | periods     | of intense |     |     |     |     |     |     |     |
| ------------------ | ------------- | ---------- | ------------ | -------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| manipulation.      |               | Overall,   | the combined |          | forecasting |            | and |     |     |     |     |     |     |
| sentiment-analysis |               | framework  |              | achieved | an          | F1-score   | of  |     |     |     |     |     |     |
| up to 93%,         | demonstrating |            | the          | strong   | synergy     | between    |     |     |     |     |     |     |     |
guidingnetworkconnectivityovertime.Bymonitoring
marketdataandexternalsentimentsignals[47].
|          |        |              |     |        |     |         |     | deviations | using | Hotelling’s | T2  | statistic, | significant |
| -------- | ------ | ------------ | --- | ------ | --- | ------- | --- | ---------- | ----- | ----------- | --- | ---------- | ----------- |
| • Hidden | Markov | Multi-linear |     | Tensor |     | Models: | An  |            |       |             |     |            |             |
alternative statistical monitoring framework employs anomalies in cryptoasset transaction behaviors are
flagged.ThemethodflagsBitcointransactionsbetween
| Hidden   | Markov       | Multi-linear |               | Tensor | Models   | (HMTM) |     |          |           |               |     |              |         |
| -------- | ------------ | ------------ | ------------- | ------ | -------- | ------ | --- | -------- | --------- | ------------- | --- | ------------ | ------- |
|          |              |              |               |        |          |        |     | 2011 and | 2013 that | significantly |     | deviate from | typical |
| [48] and | Multivariate |              | Exponentially |        | Weighted | Moving |     |          |           |               |     |              |         |
historicalpatternsaspotentialanomaliesalignwiththe
| Average | (MEWMA) |     | control | charts | [49], | [50]. | The |     |     |     |     |     |     |
| ------- | ------- | --- | ------- | ------ | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
Mt.Goxleakedtransactions[52].
| goal of | HMTM | is  | to model | the | relationships |     | in  |     |     |     |     |     |     |
| ------- | ---- | --- | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Bitcoin transaction networks that change over time • Vector Autoregressive: Vector Autoregressive (VAR)
|           |             |            |         |      |             |      |        | models have  | been   | employed          | to       | evaluate      | behavioral |
| --------- | ----------- | ---------- | ------- | ---- | ----------- | ---- | ------ | ------------ | ------ | ----------------- | -------- | ------------- | ---------- |
| but where | the         | underlying | state   | of   | the network |      | (e.g., |              |        |                   |          |               |            |
|           |             |            |         |      |             |      |        | anomalies    | driven | by external       | economic | factors,      | such       |
| normal,   | suspicious) | is         | hidden. | HMTM | builds      | upon | the    |              |        |                   |          |               |            |
|           |             |            |         |      |             |      |        | as gas price | surges | in Ethereum-based |          | decentralized |            |
Multi-linearTensorModel(MTM)[51]whichmodelthe
autonomousorganizations(DAOs)[53].Inthiscontext,
probabilityofatransactionbetweennodeiandjattime
| t as:    |        |     |     |        |     |        |      | the VAR                  | framework | captures   | how    | present | values of |
| -------- | ------ | --- | --- | ------ | --- | ------ | ---- | ------------------------ | --------- | ---------- | ------ | ------- | --------- |
|          |        |     |     |        |     |        |      | multiple                 | variables | (e.g., gas | prices | and DAO | activity) |
|          | ,u,u,v |     |     | β+<u,v |     | ,u >+ε |      | dependontheirpastvalues: |           |            |        |         |           |
| P(y =1|x |        |     | )=x |        |     |        |      |                          |           |            |        |         |           |
| ijt      | ijt    | i j | t   | ijt    | i   | t j    | ijt  |                          |           |            |        |         |           |
|          |        |     |     |        |     |        | (16) | y =v+A                   | y         | +A y       | +...+A | y       | +u (17)   |
|          |        |     |     |        |     |        |      | t                        | 1 t−1     | 2 t−2      |        | p t−p   | t         |
where y indicates the presence 1 or absence 0 of a wherey = (r gas,a )isavectorcontaininglog-returns
|     | ijt |     |     |     |     |     |     | t   | t   | t   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
transaction, x ijt a vector of covariates, i.e., known fac- of the gas price and user activity at time t, v and
tors,thatmightinfluencethetransaction,e.g.,example A ,...,A are coefficient matrices and u represents
|     |     |     |     |     |     |     |     | 1   | p   |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
transaction size, time of day, etc., β is the coefficient white noise. The VAR model enables the test for
vectorthatquantifiestheeffectofthecovariates,u and Granger causality between gas price changes and
i
u represent latent vectors describing the position of DAO activity while also capturing lagged effects
j
nodesiandjinanunderlyinglatentspace,v t captures and inter-dependencies between these variables over
the latent rules governing node interactions at time t time. Analysis of 5,580 transactions from 7,825 users
andεijt istheerrortermassumednormallydistributed in 191 DAOs revealed a surprising result: despite
around zero. The MTM assumes a static network. significant gas price surges (up to 8500% increases
The HMTM adds a Hidden Markov Model (HMM) to in 2020), the model showed only minor statistical
accountforthefactthatthenetworkcanbeindifferent influenceofgaspricefluctuationsonDAOuseractivity
unobserved states B = Y −(cid:127) where B represents levels.Thisinsensitivitycontradictstypicalmarketself-
|     |     | t   | t   | t   |     | t   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
anomalous deviations, Y is the observed transaction regulation expectations, where higher transaction costs
t
adjacencymatrix,and(cid:127)
t istheexpectedstructurebased wouldtheoreticallydeterparticipation.
on latent variables under normal hidden states. The • Adjusted volume: Notable terrorist attacks can also
=(u ,v
latentstateL t t t )describesthehiddendynamics be identified using an event-study approach based on
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 202589 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
mean-adjustedvolume(AV)ofuseruatdayt [54]: TABLE4. Miningbehavioranomalydetection.
|               |            | AV         | =ln(V      | )−ln(V  | ˆ           | )           | (18)       |             |     |        |             |     |     |       |         |
| ------------- | ---------- | ---------- | ---------- | ------- | ----------- | ----------- | ---------- | ----------- | --- | ------ | ----------- | --- | --- | ----- | ------- |
|               |            |            | u,t        | u,t     |             | u,t         |            |             |     |        |             |     |     |       |         |
| which         | captures   |            | deviations |         | between     | observed    | and        |             |     |        |             |     |     |       |         |
| expected      |            | user-level | volumes.   |         | The average |             | abnormal   |             |     |        |             |     |     |       |         |
| mean-adjusted |            |            | volume     | (AAV)   | is          | then formed | by         |             |     |        |             |     |     |       |         |
| summing       |            | these      | daily AV   | u,t for | each        | user in     | the group  |             |     |        |             |     |     |       |         |
| and           | normalized |            | by the     | total   | number      | of          | users, and |             |     |        |             |     |     |       |         |
| the           | cumulative |            | abnormal   | volume  | (CAV)       | expands     | that       |             |     |        |             |     |     |       |         |
|               |            |            |            |         |             |             |            | assignments |     | in the | t-th trial. | The | MSB | index | is then |
| perspective   |            | across     | longer     | periods | by          | aggregating | AAV        |             |     |        |             |     |     |       |         |
definedas:
valuesaroundaneventwindow:
N
|     |     |     |       | 1 X |     |     |      |                                                    |     |          |          | CT −⟨ST⟩          |      |              |      |
| --- | --- | --- | ----- | --- | --- | --- | ---- | -------------------------------------------------- | --- | -------- | -------- | ----------------- | ---- | ------------ | ---- |
|     |     |     | AAV = |     | AV  |     | (19) |                                                    |     | MSBT     | =        | i                 | i    |              | (21) |
|     |     |     | t     |     | u,t |     |      |                                                    |     |          | i        | σ(cid:2) T(cid:3) |      |              |      |
|     |     |     |       | N t |     |     |      |                                                    |     |          |          | S                 |      |              |      |
|     |     |     |       | u=1 |     |     |      |                                                    |     |          |          | i                 |      |              |      |
|     |     |     |       | T   |     |     |      |                                                    | T⟩  | σ(cid:2) | T(cid:3) |                   |      |              |      |
|     |     |     |       | X   |     |     |      | where                                              | ⟨S  | and      | S denote | the               | mean | and standard |      |
|     |     |     | CAV = | AAV |     |     | (20) |                                                    | i   |          | i        |                   |      |              |      |
|     |     |     | t     |     | t   |     |      | deviationofthebootstrappedconsecutive-blockcounts, |     |          |          |                   |      |              |      |
t=1
|     |     |     |     |     |     |     |     | respectively. |     | An MSB | value | significantly |     | greater | than |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | ----- | ------------- | --- | ------- | ---- |
zero,oftenassessedviaap-valuederivedfromthenor-
| Calculating |     | mean | CAV | for | the two-week |     | intervals |     |     |     |     |     |     |     |     |
| ----------- | --- | ---- | --- | --- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
15,t 1,t mal or empirical distribution of the bootstrap samples,
| before | [t  | −   | − 1] | and after | [t  | +   | + 15] any |     |     |     |     |     |     |     |     |
| ------ | --- | --- | ---- | --------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
terrorist attack isolates sharp bursts of transactional indicates that miner i is an outlier, which may imply
undisclosedstrategicbehaviors,suchasdelayingblock
| activity | consistent |     | with | short-term | planning |     | and exe- |     |     |     |     |     |     |     |     |
| -------- | ---------- | --- | ---- | ---------- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
cution patterns. When applied to Bitcoin blockchain publication.Thismethodologyisalsoextendedtodetect
transactions, categorized into groups like exchanges, miningcartelsbymeasuringhowoftentwominersiand
jappearinsuccession.
| dark | markets, | mixers, |     | gambling | platforms, |     | and other |     |     |     |     |     |     |     |     |
| ---- | -------- | ------- | --- | -------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
services,CAVcanrevealsignificantspikesinabnormal
CT −⟨ST⟩
|     |     |     |     |     |     |     |     |     |     | MCT | =   | ij  | ij  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
transaction volumes through mixers and unregulated σ(cid:2) ST(cid:3) (22)
ij
| exchanges |     | in      | the weeks | preceding |        | major     | terrorist |       |     |        |        | ij         |     |             |     |
| --------- | --- | ------- | --------- | --------- | ------ | --------- | --------- | ----- | --- | ------ | ------ | ---------- | --- | ----------- | --- |
| events.   | A   | focused | case      | study     | on the | Sri Lanka | Easter    |       |     |        |        |            |     |             |     |
|           |     |         |           |           |        |           |           | where | CT  | is the | actual | times that | two | consecutive |     |
ij
bombingdemonstratestheapproachinaction,detecting
|            |     |           |     |          |      |         |           | blocks      | are | first mined    | by  | miner i          | and then | by        | miner |
| ---------- | --- | --------- | --- | -------- | ---- | ------- | --------- | ----------- | --- | -------------- | --- | ---------------- | -------- | --------- | ----- |
| suspicious |     | transfers | by  | a single | user | with no | plausible |             |     |                |     |                  |          |           |       |
|            |     |           |     |          |      |         |           | j. Applying |     | this framework |     | to cryptoassets, |          | including |       |
alternativeexplanation;backwardtraceslinkthewallet
Bitcoin,EthereumandLitecoinandBitcoinCashreveals
toothercrimes,whileforwardtracesrevealsubsequent
|              |     |           |         |     |              |     |            | the presence |                   | of anomalous |         | miners   | in all | four cryptoas- |     |
| ------------ | --- | --------- | ------- | --- | ------------ | --- | ---------- | ------------ | ----------------- | ------------ | ------- | -------- | ------ | -------------- | --- |
| conversion   |     | to Ripple | (XRP)   | and | additional   |     | mixing via |              |                   |              |         |          |        |                |     |
|              |     |           |         |     |              |     |            | sets,        | with particularly |              | notable | clusters |        | of outliers    | in  |
| a high-value |     | deposit   | wallet, |     | underscoring |     | the effec- |              |                   |              |         |          |        |                |     |
BitcoinCash.Someoftheseminersremainunidentified
| tiveness | of  | on-chain | analysis |     | in illuminating |     | terrorist |         |     |             |          |     |        |       |        |
| -------- | --- | -------- | -------- | --- | --------------- | --- | --------- | ------- | --- | ----------- | -------- | --- | ------ | ----- | ------ |
|          |     |          |          |     |                 |     |           | (tagged | as  | ‘Unknown’), | implying |     | hidden | pools | or ad- |
financingstructures.
|     |     |     |     |     |     |     |     | hoc      | collusions. | While    | anomalies |          | are also | observed | in   |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | -------- | --------- | -------- | -------- | -------- | ---- |
|     |     |     |     |     |     |     |     | Litecoin | and         | Bitcoin, | the       | patterns | there    | appear   | less |
2) MININGBEHAVIORANOMALYDETECTION concentrated than in Bitcoin Cash. The framework
| Anomalous  | mining |               | strategies | can   | undermine | the | security   |           |          |          |           |             |     |            |     |
| ---------- | ------ | ------------- | ---------- | ----- | --------- | --- | ---------- | --------- | -------- | -------- | --------- | ----------- | --- | ---------- | --- |
|            |        |               |            |       |           |     |            | is then   | extended |          | further   | to include  | the | analysis   | of  |
| guarantees | of     | proof-of-work |            | (PoW) | systems   | by  | distorting |           |          |          |           |             |     |            |     |
|            |        |               |            |       |           |     |            | Monacoin, |          | adopting | a related | statistical |     | test based | on  |
reward distribution or enabling attacks such as double- a type II binomial model to detect disproportionate
spending.Toaddressthis,variousstatisticalframeworkshave
sequencesofconsecutiveblocks[56].Asalientfinding
beendevelopedtodetectnon-compliantminerbehavior. is that Monacoin exhibits the highest fraction of
• MinerSequenceBootstrapping:Onesuchapproachis suspicious miners, corroborating the network’s self-
MinerSequenceBootstrapping(MSB)[55],whichmod- reported selfish mining incidents. Furthermore, many
els each miner’s block-discovery event as a Bernoulli oftheseflaggedentitiesexhibitcollaborativestructures,
trial with success probability proportional to its hash- suggesting coordinated withholding of blocks among
power share. Under normal conditions, the probability multipleminers.
ofasingleminerdiscoveringconsecutiveblocksinrapid • Miner Share Distributions: Beyond selfish mining,
succession should be relatively small unless its hash the risk of majority attacks by investigating shifts in
power is exceptionally large. Mathematically, let CT miner share distributions is also studied [57]. The
i
denote the number of times miner i mines consecutive analysis examines the assumption that computational
blocks over a given period T, and let ST represent the powerisbroadlydistributed,i.e.,nosingleentityshould
i
outputofareshuffled(bootstrapped)sequenceofblock dominate the network, and proposes creating detailed
| 202590 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
profiles of each major miner or mining pool. By sys- how important these structural analyses are for security,
tematically tracking the evolution of these profiles compliance,andtheoverallhealthofblockchainecosystems.
over time, the approach flags anomalies indicative of A summary of the studies covered in this category is
rapid concentration of hash power, which elevates the presentedintable5.
| threat | of  | a 51% | attack. | Empirical | findings |     | on Bitcoin |     |     |     |     |     |     |     |     |
| ------ | --- | ----- | ------- | --------- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
and Ethereum illustrate how abrupt spikes in a single • CryptoassetTransactionNetworkStructure:Several
miner’s share function as early indicators of potential early works analyze the Bitcoin transaction network
double-spending or extended block rewriting, offering from a structural perspective, with [58] focusing on
a proactive means to detect and mitigate malicious four years of transaction data and revealing a small-
consolidationofhashingresources. worldtopology.Insuchatopology,theaveragegeodesic
|       |             |            |     |       |              |     |          | distance | among | addresses |     | is quite | short, | implying | a   |
| ----- | ----------- | ---------- | --- | ----- | ------------ | --- | -------- | -------- | ----- | --------- | --- | -------- | ------ | -------- | --- |
| These | statistical | techniques |     | offer | a harmonious |     | blend of |          |       |           |     |          |        |          |     |
relativelyhighlevelofinterconnectivity;however,high-
| simplicity        | and       | sophistication |         | in detecting |                | anomalies     | across  |                 |         |             |          |                  |         |           |        |
| ----------------- | --------- | -------------- | ------- | ------------ | -------------- | ------------- | ------- | --------------- | ------- | ----------- | -------- | ---------------- | ------- | --------- | ------ |
|                   |           |                |         |              |                |               |         | degree          | hubs in | these       | networks |                  | can act | as de     | facto  |
| cryptoasset       | networks. |                | Methods |              | like Benford’s |               | Law and |                 |         |             |          |                  |         |           |        |
|                   |           |                |         |              |                |               |         | ‘‘centralized’’ |         | nodes       | handling | disproportionate |         |           | trans- |
| Mahalanobis-based |           | scoring        |         | shine        | for their      | computational |         |                 |         |             |          |                  |         |           |        |
|                   |           |                |         |              |                |               |         | action volumes, |         | potentially |          | undermining      |         | the ethos | of     |
efficiency,easeofimplementation,andbroadgeneralizability
fulldecentralization.Meanwhile,[59]and[60]explore
| across diverse     |               | datasets,      | while   | signature-based |            |             | and tensor |               |         |               |         |                 |                |              |        |
| ------------------ | ------------- | -------------- | ------- | --------------- | ---------- | ----------- | ---------- | ------------- | ------- | ------------- | ------- | --------------- | -------------- | ------------ | ------ |
|                    |               |                |         |                 |            |             |            | broader       | Bitcoin | data          | to show | scale-free-like |                |              | degree |
| models,            | as well       | as forecasting |         | frameworks,     |            | deliver     | deeper     |               |         |               |         |                 |                |              |        |
|                    |               |                |         |                 |            |             |            | distributions | in      | which         | a small | minority        |                | of addresses |        |
| insights           | and capture   |                | complex | temporal        |            | dynamics    | albeit at  |               |         |               |         |                 |                |              |        |
|                    |               |                |         |                 |            |             |            | dominate      | overall | connectivity; |         |                 | thus, although |              | path   |
| a higher           | computational |                | cost.   | Although        | techniques |             | based on   |               |         |               |         |                 |                |              |        |
|                    |               |                |         |                 |            |             |            | lengths       | remain  | short,        | control | is concentrated |                | among        | a      |
| basic distribution |               | properties     |         | scale           | well       | and provide | read-      |               |         |               |         |                 |                |              |        |
handfulofhigh-degreenodes.Whilescale-freebehavior
| ily interpretable |     | signals, | more | advanced |     | approaches | often |              |     |            |     |          |           |          |     |
| ----------------- | --- | -------- | ---- | -------- | --- | ---------- | ----- | ------------ | --- | ---------- | --- | -------- | --------- | -------- | --- |
|                   |     |          |      |          |     |            |       | often arises | in  | real-world |     | systems, | it raises | concerns |     |
requireextensiveparametertuningandrobustcomputational
aboutsinglepointsoffailureorsuspiciousconcentration
| infrastructure, |     | which | can hinder |     | real-time | application | and |            |        |     |              |     |         |        |     |
| --------------- | --- | ----- | ---------- | --- | --------- | ----------- | --- | ---------- | ------ | --- | ------------ | --- | ------- | ------ | --- |
|                 |     |       |            |     |           |             |     | of network | power; |     | for example, |     | a small | clique | of  |
limitadaptabilitytorapidlyevolvingmarketconditions.Like-
|     |     |     |     |     |     |     |     | exchanges | or mixers |     | could | become | a structural |     | choke |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ----- | ------ | ------------ | --- | ----- |
wise,miningbehavioranomalydetectionmethodseffectively
|     |     |     |     |     |     |     |     | point. Both | studies | further |     | incorporate | clustering |     | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ------- | --- | ----------- | ---------- | --- | --- |
highlightirregularitiesinblockdiscoveryandpooldynamics
assortativitymetrics,findingthattheBitcoinnetworkis
| but depend | critically |     | on accurate |     | miner | identification | and |     |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | ----------- | --- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mildlydisassortative:largehubsprimarilyinteractwith
| are vulnerable |       | to sophisticated |     | adversarial |     | strategies. | Col-     |              |            |            |            |               |     |          |        |
| -------------- | ----- | ---------------- | --- | ----------- | --- | ----------- | -------- | ------------ | ---------- | ---------- | ---------- | ------------- | --- | -------- | ------ |
|                |       |                  |     |             |     |             |          | small nodes, | forming    |            | star-like  | substructures |     | centered |        |
| lectively,     | these | approaches       |     | underscore  | a   | trade-off   | between  |              |            |            |            |               |     |          |        |
|                |       |                  |     |             |     |             |          | on major     | exchanges  |            | or service | addresses.    |     | These    | obser- |
| simplicity     | and   | granularity,     |     | suggesting  |     | ample       | room for |              |            |            |            |               |     |          |        |
|                |       |                  |     |             |     |             |          | vations      | align with | additional |            | findings      | in  | [58],    | which  |
improvementthroughhybridmodels,adaptivethresholding,
notesthatcertainregionsexhibitusagepatternsheavily
| and enhanced |     | integration |     | of external |     | factors | to bolster |     |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | --- | ----------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
detectionaccuracyandscalabilityfurther. oriented around small-value gambling transactions,
|     |     |     |     |     |     |     |     | underscoring | how      | socio-economic |           |       | factors | can       | foster |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | -------------- | --------- | ----- | ------- | --------- | ------ |
|     |     |     |     |     |     |     |     | specialized  | clusters | of             | activity. | These | results | highlight |        |
B. NETWORKANALYSIS
|           |               |            |             |          |          |              |             | that although | the | Bitcoin   | network |          | achieves       | short-path |     |
| --------- | ------------- | ---------- | ----------- | -------- | -------- | ------------ | ----------- | ------------- | --- | --------- | ------- | -------- | -------------- | ---------- | --- |
| Network   | analysis      | approaches |             | leverage |          | the inherent | graph       |               |     |           |         |          |                |            |     |
|           |               |            |             |          |          |              |             | efficiency    | and | maintains |         | a degree | of resilience, |            | its |
| structure | of blockchain |            | transaction |          | networks |              | to identify |               |     |           |         |          |                |            |     |
relianceonasmallnumberofhubsandtheinfluenceof
| anomalies. | These | methods |     | analyze | structural |     | properties, |            |          |             |     |           |     |               |     |
| ---------- | ----- | ------- | --- | ------- | ---------- | --- | ----------- | ---------- | -------- | ----------- | --- | --------- | --- | ------------- | --- |
|            |       |         |     |         |            |     |             | regionally | specific | transaction |     | behaviors |     | can introduce |     |
connectivitypatterns,andtopologicalfeaturestodetectsuspi- potentialvulnerabilitiesandunderminethecryptoasset’s
ciousbehaviorsthatmightindicatefraud,moneylaundering,
intendeddecentralization.
orothermaliciousactivities.Forthebrieftheoreticalaspect
|     |     |     |     |     |     |     |     | Whereas | the | above | focuses | solely | on  | Bitcoin, | [61] |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----- | ------- | ------ | --- | -------- | ---- |
ofgraphconstructionandtherelevantpropertiesofthegraph, compares a Bitcoin trader network and an adolescent
refertosectionII-E.
|     |     |     |     |     |     |     |     | friendship     | network |          | using       | community | detection |           | and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | -------- | ----------- | --------- | --------- | --------- | --- |
|     |     |     |     |     |     |     |     | social network |         | analysis | techniques, |           | revealing | interest- |     |
1) STRUCTURAL&COMMUNITYANALYSIS ing parallels and distinctions. Both networks exhibit
Anotablebodyofliteratureconcentratesonglobalnetwork moderate clustering, meaning that nodes tend to form
properties of blockchain transaction graphs, such as degree tightly-knit groups and some reciprocity. Reciprocity,
distributions, clustering, community structure, and core- in this context, refers to the tendency for relationships
periphery organization. These analyses frequently uncover tobemutual,i.e.,ifonepersonorBitcointraderformsa
unexpected hierarchies and densely connected communities connectionwithanother,theotherislikelytoreciprocate
ofaddresses,challengingtheassumptionthatblockchainsare the connection, creating a two-way relationship. It is
fully decentralized. Moreover, detecting strongly clustered also concluded that adolescents prefer a reciprocal
groups, short-lived ephemeral subgraphs, or community relationship with the same gender and that drinkers
‘‘islands’’revealsthatsuspiciousoranomalousactivitymay tend to be more active in their social circle. Notably,
easily concentrate among a few addresses, underscoring this financial network displays assimilation rather than
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 202591 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
homophily; users tend to trade more frequently within TABLE5. Structural&Communityanalysis.
| their own | communities |              | without          | a strong  | tendency     | to      |     |     |     |     |     |
| --------- | ----------- | ------------ | ---------------- | --------- | ------------ | ------- | --- | --- | --- | --- | --- |
| connect   | based       | on similar   | characteristics. |           | Furthermore, |         |     |     |     |     |     |
| unusually | dense       | or exclusive |                  | subgroups | in the       | Bitcoin |     |     |     |     |     |
networkcouldserveasindicatorsofsuspiciousactivity.
| Overall, | these          | findings | underscore  | the     | structural | simi- |     |     |     |     |     |
| -------- | -------------- | -------- | ----------- | ------- | ---------- | ----- | --- | --- | --- | --- | --- |
| larities | and behavioral |          | differences | between | social     | and   |     |     |     |     |     |
financialnetworks,offeringinsightsthatarerelevantfor
understandingdynamicsinbothdomains.
| While      | designed             | as      | a stablecoin | bridging     |           | multiple |     |     |     |     |     |
| ---------- | -------------------- | ------- | ------------ | ------------ | --------- | -------- | --- | --- | --- | --- | --- |
| exchanges, | Tether               | has     | been         | studied      | from both | com-     |     |     |     |     |     |
| munity     | and global-structure |         |              | standpoints. | The       | study    |     |     |     |     |     |
| using a    | Social               | Network | Analysis     | (SNA)        | of the    | Tether   |     |     |     |     |     |
transactiongraph[62]revealsthattheTethertransaction
| graph lacks   | the    | small-world |               | property, | which | typically |     |     |     |     |     |
| ------------- | ------ | ----------- | ------------- | --------- | ----- | --------- | --- | --- | --- | --- | --- |
| characterizes | robust |             | and efficient | networks; |       | instead,  |     |     |     |     |     |
largecryptoassetexchangesdominatethedegreedistri-
bution,actingascentralnodeswithsignificantinfluence
| over transaction |     | flow. | Bitfinex | emerges | as  | a pivotal |     |     |     |     |     |
| ---------------- | --- | ----- | -------- | ------- | --- | --------- | --- | --- | --- | --- | --- |
playerduetoitsco-ownershipandco-administrationties
| with Tether’s | issuer,  | exemplifying |     | a          | ‘‘rich-get-richer’’ |           |     |     |     |     |     |
| ------------- | -------- | ------------ | --- | ---------- | ------------------- | --------- | --- | --- | --- | --- | --- |
| effect that   | suggests | control      |     | by a few   | major               | entities, |     |     |     |     |     |
| potentially   | enabling | manipulative |     | practices. |                     | The net-  |     |     |     |     |     |
work’s low assortativity, indicating that high-volume and weighted aspects of transactions, recognizing that
entities do not form stable links over time, points to the timing and size of transactions are important
transient periods of high trading activity rather than features.Thistemporalinformationmodelsthenetwork
sustainedmarketinteractions.Additionally,theconcept as evolving continuously over time with additions of
of ‘‘bubble networks,’’ defined by short periods of links.Variousrandomwalkstrategiesthenappliedover
intensetradingcenteredonkeynodes,mirrorsfinancial the TWMDG, defining Temporal Successive Edges,
bubblesandfurtherhighlightsstructuralvulnerabilities. L (u) = {e | Src(e) = u,T(e) ≥ t} as the
t
• RandomGraphvs.CryptoassetTransactionGraph: set of edges leaving node u at or after time t and
Complementingtheseglobalanalyses,[63]fitsrandom- assigning selection probabilities P (e) of the random
T
graph models, i.e., Chung–Lu [64] and Buckley– walk selecting successive edge e at time t from node
Osthus[65],toBitcoin’sstructurebyusingmathemati- u would then be P (e) = 1 (unbiased) or with
|     |     |     |     |     |     |     |     | T   | |Lt (u)| |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
cal frameworks that describe how edges form between respect to timestamp or amount (biased). The results
nodes according to probabilistic rules and highlights showthatlocalfeatureslikedegreealoneareinsufficient
the bowtie structure yet reveals that the data deviate for uncovering hidden edges that form ephemeral
from simple scale-free or random attachment models, or secretive transaction clusters, which may harbor
exhibitingpersistentanomaliessuchasover-centralized potential money-laundering or consolidation strategies
clustersandephemeralspikesubgraphslikelyresulting undetectedwhensubgraphpatternsareoverlooked.
from intentional participant behaviors, e.g., strategic • Hierarchical structures of Tokens: Several studies
transaction patterns or the use of mixing services, on token networks and smart contracts explicitly
|     |     |     |     |     |     |     | demonstrate | that nominally | ‘‘decentralized’’ |     | systems |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | ----------------- | --- | ------- |
networkevolutionovertime,andunderlyingeconomic
forces, these deviations indicate that simple random may exhibit pronounced core-periphery or hierarchical
models do not fully capture the network’s structural structures, thereby challenging the principle of net-
features, with ephemeral subgraphs potentially repre- work flatness. For example, [67] conducts community
sentingabrupttransactionburstsoron-chainmixersthat detection on the AAVE token transaction network on
|                  |     |           |     |           |            |      | the Ethereum | blockchain | and reveals | a dominant | core |
| ---------------- | --- | --------- | --- | --------- | ---------- | ---- | ------------ | ---------- | ----------- | ---------- | ---- |
| raise compliance |     | concerns. | In  | a similar | direction, | [66] |              |            |             |            |      |
employs random-walk embeddings for link prediction comprisingcentralizedexchanges,suchasCoinbaseand
by modeling Ethereum transaction records as a Tem- Binance, and key contract wallets that mediate most
= (V,E),
poralWeightedMultidigraph(TWMDG),G token flows. This concentration indicates that a small
whereV isthesetofnodes(accounts)andE istheset group of aggregator nodes can dominate transaction
|          |                 |     |      |        |                |     | throughput, | introducing | single points | of failure | and |
| -------- | --------------- | --- | ---- | ------ | -------------- | --- | ----------- | ----------- | ------------- | ---------- | --- |
| of edges | (transactions). |     | Each | edge e | is represented | as  |             |             |               |            |     |
(u,v,w,t),
e = where u is the source node, v is the potentially obscuring suspicious patterns like cyclical
targetnode,wistheweight(transactionamount),andt liquidity. Similarly, [68] confirms that removing a few
isthetimestamp.Thismodelincorporatesthetemporal topaddresses,particularlymajorexchangeaccountsand
| 202592 |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
pivotalsmartcontractscanfragmenttheconnectivityof preferential attachment, i.e., new edges (transactions)
theentireEthereumtokennetwork,underscoringacrit- arrive with probabilities proportional to existing node
ical structural vulnerability. The study further employs degreesorwealth. Theyshowedthattheprobabilityof
|A∩B|
theJaccardIndexJ(A,B)= ,whichquantifiesthe forminganewlinkconnectingtothenodevis
|A∪B|
| overlap | in  | transaction | patterns |     | by comparing |     | two sets |     |     |     |     | k   | α   |     |     |
| ------- | --- | ----------- | -------- | --- | ------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
|         |     |             |          |     |              |     |          |     |     |     |     | )=  | v   |     |     |
of trading counterparts, with A and B representing, for p(k v P (23)
kα
| example, | the      | sets  | of counterparties |             | that | two     | different |       |     |                 |     | w       | w      |     |        |
| -------- | -------- | ----- | ----------------- | ----------- | ---- | ------- | --------- | ----- | --- | --------------- | --- | ------- | ------ | --- | ------ |
|          |          |       |                   |             |      |         |           | where | k   | is the indegree |     | of node | v, and | α ≥ | 0. The |
| nodes    | interact | with, | and               | the Ordered |      | Jaccard | Index     |       | v   |                 |     |         |        |     |        |
|LCS(A,B)|
(OJI) OJI(A,B) = , where LCS denotes probabilitythatthenewlinkconnectstoanynodewith
|A∪B|
degreek is
| the | longest | common | subsequence |     | between |     | two sets |     |     |     |     |     |     |     |     |
| --- | ------- | ------ | ----------- | --- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
capturing sequential patterns in how accounts trade. p(k)∝n α
|       |      |         |          |         |      |     |            |     |     |     |     | k   | k   |     | (24) |
| ----- | ---- | ------- | -------- | ------- | ---- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | ---- |
| Aside | from | raising | security | issues, | such | a   | structural |     |     |     |     |     |     |     |      |
vulnerability indicates that transactions are anything Buildingonthis,[71]relaxestheassumptionofpurely
butuniformlydistributedandmightreflectapersistent degree-basedattachmentbyintroducingnode‘‘fitness’’
η andthepreferentialattachmentkernelas
| risk                  | if those | key nodes | are | compromised |      | or engage     | in  | i   |     |     |      |       |     |     |      |
| --------------------- | -------- | --------- | --- | ----------- | ---- | ------------- | --- | --- | --- | --- | ---- | ----- | --- | --- | ---- |
| manipulativebehavior. |          |           |     |             |      |               |     |     |     |     |      | θ θ   |     |     |      |
|                       |          |           |     |             |      |               |     |     |     |     | A =k | k +ηη |     |     | (25) |
| Finally,              | [69]     | extends   |     | insights    | into | decentralized |     |     |     |     | ij   | i j   | i j |     |      |
θ
finance (DeFi) by analyzing transaction networks of where for small the initial fitness differences are
three prominent Ethereum-based tokens—Dai (DAI), not significantly amplified, but for larger θ these
Uniswap(UNI),andWrappedBitcoin(WBTC)—using differences can become prominent. The empirical
metrics such as diameter, modularity, and density. results indicate that certain nodes persistently attract
The analysis reveals centralized clusters bridging the transactionsbecauseofhigherfitnessvalues,potentially
network, where large exchanges and pivotal smart overshadowing simpler linear-degree rules. Further
contracts act as intermediaries facilitating most trans- extending these perspectives, [72] targets Ethereum
action flows. These bridging nodes form cross-linked tokens,showingthatmultipleERC-20networksdisplay
communitiesthatbothenhanceliquiditybyconnecting super-linear preferential attachment, indicating that a
isolated network segments and constrain transaction fewnodesquicklybecomehubs.Complementarily,[73]
behaviorswithinspecificclusters.Thispatternsuggests synthesizes findings for both Bitcoin and Ethereum,
that, despite DeFi’s decentralized branding, actual confirming that hubs maintain their dominance even
usage is dominated by a small set of heavily utilized as overall market conditions and prices fluctuate.
addresses, potentially creating single points of trust or Deviations from expected preferential attachment can
failureandexposingsystemicvulnerabilities.Moreover, signal anomalies and potential fraud. For example,
structuralbiaseshintathiddenrisks,suchascoordinated a sudden connection surge to a previously low-degree
market manipulation or irregular trading patterns, node or an unexpectedly high fitness score may raise
| as modularity |     | analysis |     | uncovers | clusters | with | high | suspicion. |     |     |     |     |     |     |     |
| ------------- | --- | -------- | --- | -------- | -------- | ---- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
internal connectivity but limited external interactions, • TransactionnetworkandPriceCorrelation:Another
and centrality calculations highlight influential wallet stream of research addresses the temporal analysis of
|     |     |     |     |     |     |     |     | multiple | cryptoassets |     | or  | snapshots | aligned | with | price |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | --- | --------- | ------- | ---- | ----- |
addressesthatcriticallyshapemarketdynamics.
|     |     |     |     |     |     |     |     | variation. |     | For instance, |     | [16] identifies |     | that the | degree |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------- | --- | --------------- | --- | -------- | ------ |
distributionofmonthlytransactionnetworksforBitcoin,
2) TEMPORAL&EVOLUTIONARYNETWORKMETHODS
|         |              |     |            |         |     |            |        | Ethereum, |           | and Namecoin |               | cannot | be well-fitted |          | by the |
| ------- | ------------ | --- | ---------- | ------- | --- | ---------- | ------ | --------- | --------- | ------------ | ------------- | ------ | -------------- | -------- | ------ |
| Whereas | the previous |     | subsection | centers |     | on static, | cross- |           |           |              |               |        |                |          |        |
|         |              |     |            |         |     |            |        | famous    | power-law |              | distribution, |        | i.e., these    | networks |        |
sectionalanalyses,theworksbelowincorporateatime-based
|                 |     |              |     |       |               |     |     | exhibit | heavy-tailed |      | distributions |     | rather     | than | scale-  |
| --------------- | --- | ------------ | --- | ----- | ------------- | --- | --- | ------- | ------------ | ---- | ------------- | --- | ---------- | ---- | ------- |
| or evolutionary |     | perspective, |     | often | investigating |     | how |         |              |      |               |     |            |      |         |
|                 |     |              |     |       |               |     |     | free    | properties.  | This | structural    |     | uniqueness | is   | further |
blockchaintransactionnetworksgrow,shift,orcorrelatewith
|                 |          |        |              |         |                   |     |         | emphasized |     | by the   | observation |     | that while       | both | Bit- |
| --------------- | -------- | ------ | ------------ | ------- | ----------------- | --- | ------- | ---------- | --- | -------- | ----------- | --- | ---------------- | ---- | ---- |
| external        | factors, | e.g.,  | exchange     | prices. | Methodologically, |     |         |            |     |          |             |     |                  |      |      |
|                 |          |        |              |         |                   |     |         | coin       | and | Ethereum | networks    |     | are heavy-tailed |      | with |
| they frequently |          | deploy | preferential |         | attachment        |     | models, |            |     |          |             |     |                  |      |      |
disassortativemixing,wherehigh-degreenodesconnect
dynamicsnapshots,ortemporalembeddings,differentiating
|     |     |     |     |     |     |     |     | to  | low-degree | nodes, |     | only Bitcoin | exhibits |     | small- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | ------------ | -------- | --- | ------ |
themfrompurelystructuralstudiesthatdonottrackchanges
|     |     |     |     |     |     |     |     | world | properties. |     | These | differences | likely | stem | from |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | --- | ----- | ----------- | ------ | ---- | ---- |
overtime.Asummaryofthestudiescoveredinthiscategory
|     |     |     |     |     |     |     |     | Ethereum’s |     | diverse | use | cases, such | as smart | contracts, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | --- | ----------- | -------- | ---------- | --- |
ispresentedintable6
|     |     |     |     |     |     |     |     | which | create | more | complex | transactional |     | patterns | than |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ---- | ------- | ------------- | --- | -------- | ---- |
• Rich-Get-Richer:Recently,variousworkshavestudied Bitcoin’s simpler peer-to-peer transactions. Likewise,
the preferential attachment, i.e., the ‘‘rich-get-richer’’ [74]usesweeklyordailytransactionnetworksnapshots
phenomenon in Bitcoin and Ethereum, each from a ofBitcointoshowthatduringpricedrops,thenetwork
distinct lens. For example, [70] is among the earliest becomes more heterogeneous, i.e., dominant addresses
studies to show that Bitcoin’s growth follows linear continue trading while most users reduce activity,
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 202593 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
amplifying market volatility. External shocks, such as TABLE6. Temporal&Evolutionarynetworkmethods.
| the Mt.Gox | bankruptcy, |           | disrupted |                | established | patterns.    |     |     |     |     |     |     |
| ---------- | ----------- | --------- | --------- | -------------- | ----------- | ------------ | --- | --- | --- | --- | --- | --- |
| Before     | Mt.Gox’s    | collapse, |           | the out-degree |             | distribution |     |     |     |     |     |     |
| where the  | probability |           | that      | a node         | has         | k outgoing   |     |     |     |     |     |     |
k−α
| connections | follows | roughly       |       | was     | compatible    |        | with  |     |     |     |     |     |
| ----------- | ------- | ------------- | ----- | ------- | ------------- | ------ | ----- | --- | --- | --- | --- | --- |
| a power-law | model   | in            | about | 54%     | of snapshots. |        | After |     |     |     |     |     |
| Mt.Gox,     | this    | compatibility |       | dropped | to            | around | 26%.  |     |     |     |     |     |
Thisshiftindicatesafundamentalchangeinhowusers
| transact, | reflecting | a                | loss of  | confidence | in       | centralized   |     |     |     |     |     |     |
| --------- | ---------- | ---------------- | -------- | ---------- | -------- | ------------- | --- | --- | --- | --- | --- | --- |
| exchanges | and        | a redistribution |          | of         | activity | across        | the |     |     |     |     |     |
| network,  | thereby    | offering         | insights |            | into     | the interplay |     |     |     |     |     |     |
betweennetworkstructureandmarkettrends.
| Several | studies | also | explicitly | link | dynamic | network |     |     |     |     |     |     |
| ------- | ------- | ---- | ---------- | ---- | ------- | ------- | --- | --- | --- | --- | --- | --- |
featurestopriceforecastingorcorrelation.Forinstance,
| [75] applies        | Principal     |             | Component   |              | Analysis   | (PCA)         | to     |     |     |     |     |     |
| ------------------- | ------------- | ----------- | ----------- | ------------ | ---------- | ------------- | ------ | --- | --- | --- | --- | --- |
| daily or            | weekly        | snapshots   |             | of Bitcoin’s |            | address-level |        |     |     |     |     |     |
| graph, revealing    |               | that        | topological |              | indicators | such          | as     |     |     |     |     |     |
| concentration       | in            | node        | degrees     | can          | precede    | significant   |        |     |     |     |     |     |
| price shifts.       | Singular      |             | vectors     | derived      | from       | PCA           | show   |     |     |     |     |     |
| strong correlations |               | with        | Bitcoin     | prices,      | suggesting |               | that   |     |     |     |     |     |
| structural          | changes       | in          | the         | transaction  | network    |               | serve  |     |     |     |     |     |
| as reliable         | predictors.   |             | In a        | similar      | vein,      | [76]          | adopts |     |     |     |     |     |
| correlation-tensor  |               | spectra     | for         | weekly       | XRP        | networks.     |        |     |     |     |     |     |
| A four-dimensional  |               | correlation |             | tensor       | C          | (i,j),(α,β)   | cap-   |     |     |     |     |     |
| tures the           | relationships |             | between     | different    |            | network       | fea-   |     |     |     |     |     |
turesovertime.Tofindthespectrumofthecorrelation
tensor,adoublesingularvaluedecomposition(DSVD)
|     |     |     |     |     |     |     |     | directed | pieces of the | Bitcoin transaction | network | that |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | ------------------- | ------- | ---- |
wasappliedtounfoldthetensorCcanbeunfoldedalong
|     |     |     |     |     |     |     |     | capture | common transaction | patterns. | The idea | is that |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------------ | --------- | -------- | ------- |
achosenmode(dimension):
eachgroup(orcluster)ofsimilarchainletshasacertain
∗
C (i,j),(α,β) =U (i,j) (cid:54) V (26) influence on the Bitcoin price, which we denote by
1 ( α,β)
|     |     |       |     |          |        |     |      | u ( x , t )  | w he r e x r ep r | e s e n t s a n ab    | s tr a c t p os i tio | n t h a t   |
| --- | --- | ----- | --- | -------- | ------ | --- | ---- | ------------ | ----------------- | --------------------- | --------------------- | ----------- |
|     |     | V     | =U  | (cid:54) | W ∗    |     | (27) |              |                   |                       |                       |             |
|     |     | (α,β) |     | (α,β) 2  | ( α,β) |     |      |              |                   |                       |                       |             |
|     |     |       |     |          |        |     |      | o r de r s t | he c h ai nle t c | l u s te r s , i. e., | cl u s te r s w it h  | s im i la r |
Here, U and V are the left and right singular transactionpatternsareplacedclosetogether.ThePDE
|     | (...) | (...) |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:54)
vectors, and i contains the singular values for the i- frameworkusesthesechainletstomodelthecontinuous
th mode. The first SVD in eq.26 is unfolded such that evolutionofBitcoinpricemovements:
| the (i,j) | indices | form | the rows, | and | (α,β) | become | the |         |     |         |     |     |
| --------- | ------- | ---- | --------- | --- | ----- | ------ | --- | ------- | --- | ------- | --- | --- |
|           |         |      |           |     |       |        |     | ∂u(x,t) | ∂   | ∂u(x,t) |     |     |
(α,β)
columns while the second SVD in eq.27 unfold = (d(x) )+r(t)u(x,t)h(x) (29)
|                                       |           |     |        |       |      |         |     | ∂t       | ∂x       | ∂x     |               |     |
| ------------------------------------- | --------- | --- | ------ | ----- | ---- | ------- | --- | -------- | -------- | ------ | ------------- | --- |
| in a manner                           | analogous |     | to the | first | SVD. | In each | SVD |          |          |        |               |     |
| step,oneobtainsalistofsingularvalues: |           |     |        |       |      |         |     |          | ∂u(x,t)) |        |               |     |
|                                       |           |     |        |       |      |         |     | The term | ∂ (d(x)  | models | the diffusion | of  |
∂x ∂x
(cid:54) =diag(σ ,σ ,...), (cid:54) =diag(ρ ,ρ ,...) (28) influence across clusters, with d(x) describing how
| 1   |     | 1 2 |     | 2   | 1   | 2   |     |              |                |         |                     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | ------- | ------------------- | --- |
|     |     |     |     |     |     |     |     | interactions | vary spatially | and the | term r(t)u(x,t)h(x) |     |
where the largest overall singular values are obtained. capturesthelocalgrowthordecayofthisinfluence.The
The singular values represent the amount of variance study concludes that expansions or contractions within
captured by each corresponding singular vector. The transaction subgraphs act as short-horizon signals for
largestsingularvalues,foundalongthediagonalofeach bullorbeardynamics.
(cid:54) , indicate the most significant patterns or modes of • Temporal Change of Transaction Network: One
i
variationinthatmode.Theseareusedtoidentifywhich specialized approach is found in [78], which measures
relationships between the network features impact the Lightning Network’s growth to test if it follows
XRP price movements most. The study discovers a a Barabási–Albert (BA) scale-free pattern. The BA
distinctive relationship between the largest singular modelgeneratesnetworkswhereafewnodesarehighly
values and price peaks, offering early indicators for connected hubs due to preferential attachment; new
impendingsurgesordrops.Extendingtheseapproaches nodes connect to existing nodes with high degree, fol-
further, [77] employs a partial-differential-equation lowing a power-law degree distribution. Their analysis
(PDE) framework using time-varying chainlet patterns of newly opened channels reveals that the network
tomodelBitcoinpricefluctuations.Chainletsaresmall, deviates from the pure BA model. Specifically, new
| 202594 |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
nodes tend to connect to existing nodes with greater way to link transactions and cluster addresses more
Closeness Centrality rather than simply connecting to effectively. Despite zero-knowledge proofs, repetitive
high-degree nodes as predicted by the BA model. spending patterns like round-trip transactions can
This suggests that nodes are strategically choosing partiallydeanonymizeactivity,with87.5%ofaddresses
connectionstoenhanceroutingperformancewithinthe and25.7%oftransactionslinkedtominingrewardsand
LightningNetworkratherthansimplymaximizingtheir shielded pools used mainly by founders, miners and
number of connections, implying that the BA model miningpoolsratherthantypicalprivacy-focusedusers.
maynotbeoptimalforsimulatingordesigningrouting Similarly,[81]explorestheBitcoinnetworkintoentities
protocolsfortheLightningNetwork. such as exchanges, gambling sites, and miners using
Rather than analyzing the entire network at once, features like multi-input patterns and transaction rates,
[79] focuses on locally dynamic structures by building which further refine classification by analyzing behav-
ego networks for labeled Ethereum accounts (e.g., ioral trends over time. These features are used in a
ICO, Mining, Gambling, Ponzi). Ego networks are classificationmethodthatappliesclusteringalgorithms
subgraphs centered on a single node (the ‘‘ego’’) and statistical analysis to group addresses into entities
that includes its immediate neighbors (the ‘‘alters’’) with consistent behavior patterns. This allows outliers,
and all the connections among those neighbors. This i.e., addresses exhibiting unexpected behaviors, to be
approach provides a localized view of an account’s flaggedassuspicious.
direct transaction environment and captures dynamic, • Transaction Flow & Anomaly Analysis: Several
micro-level interactions that can be obscured in a studies address manipulative or fraudulent behaviors
global analysis. The study finds that illegal accounts incryptoassetmarkets.Reference[19]analyzesleaked
(Ponzi and Phish) have much shorter lifecycles (less Mt. Gox data to reveal potential price manipulation
than 20 days) compared to normal accounts. It also linked to abnormal trading activity by constructing
reveals that ICO accounts exhibit high local clustering user-level transaction graphs. Accounts involved in
(≈ 0.18), suggesting that ICO investors frequently ‘‘extremely high’’ and ‘‘extremely low’’ transactions,
transact with one another, while gambling accounts those significantly deviating from the average market
have very low clustering (≈ 0.024), reflecting their price on a given day, are identified. These abnormal
sporadic interaction patterns. Furthermore, the ratio accounts (ABA), which are classified into extremely
of in- to out-transactions varies by account type, and high accounts (EHA) and extremely low accounts
mining, exchange, and Ponzi accounts show a higher (ELA), represent 12.5% of the accounts and approxi-
proportion of out-transactions, which reflects their mately2.8%oftransactionswithABAaccounts.These
distinctoperationalroles. abnormal accounts were correlated with sudden price
changes via SVD, where transaction data are first
dividedintodailysnapshotsandthenrepresentedthese
3) GRAPH-BASEDDETECTION&DE-ANONYMIZATION
snapshotsasmatrices.Then,SVDwasappliedtoextract
Whereas the previous subsections emphasize either static
‘‘basenetworks,’’i.e.,dominantpatternsoftransactions
structure or temporal evolution, the studies below deploy
withinthenetwork.Theresultsshowthattheabnormal
graph-basedmethodstouncovermalicioususage,suspicious
accounts transactions strongly related to the Bitcoin
flows, or anonymity breakdown in blockchain transaction
priceespeciallythevolumeanddirectionoftransactions
networks. These methods often involve refined address-
involvingEHAsandELAs,significantlycorrelatedwith
clustering heuristics, subgraph-based anomaly detection,
fluctuationsintheBitcoinpriceonMt.Gox.Similarly,
or specialized modeling techniques, enabling the identifica-
[82] proposes a Petri-net–based framework to model
tionoffraudulentbehavior.Asummaryofthestudiescovered
concurrency and dynamic transaction flows in Bitcoin.
inthiscategoryispresentedintable7
The model extracts nineteen transaction features. For
• Address Clustering & De-Anonymization: A key example,thein/outratiomeasuresthebalancebetween
theme is the use of enhanced address clustering to incoming and outgoing transactions for an address,
revealhiddenlinksandpartiallyde-identifyactors.For whereahighin/outratiomayindicateanaccumulation
example, [80] focuses on Zcash, an altcoin of Bitcoin phase, while a low ratio suggests funds are being
aiming to protect blockchain anonymity, extending drained.Theidentificationofshortcycles,wherefunds
the traditional multi-input heuristics, which assume rapidly move through a series of addresses and return
that all input addresses in a transaction belong to to the origin, can be indicative of layering techniques
the same user by combining with tracking change used to obscure the source of funds. By combining
(shadow) addresses, addresses automatically generated these features, the framework aims to provide a more
to return leftover funds from a transaction to the comprehensiveapproachtoblockchainforensics.
sender. This results in an increase in the clustering Concerningcomputationalperformance,[83]focuseson
rate by 9% as the change addresses often belong to GPU-acceleratedmethodsforsubgraph-basedanomaly
the same user as the input addresses, providing a detection to address the computational challenges of
VOLUME13,2025 202595

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
TABLE7. Graph-baseddetection&De-anonymization. origin. The presence of cyclical flows, where funds
|     |     |     |     | return to | addresses   | controlled |            | by the    | attacker, | further  |
| --- | --- | --- | --- | --------- | ----------- | ---------- | ---------- | --------- | --------- | -------- |
|     |     |     |     | indicates | coordinated |            | fraudulent | activity. |           | The TSGN |
|     |     |     |     | approach  | effectively |            | identifies | phishing  | scams     | on the   |
|     |     |     |     | Ethereum  | network     | by         | focusing   | on        | these     | subgraph |
patterns.
RecentinvestigationsintotheEOSIOblockchainreveal
|     |     |     |     | that even  | systems    | with | high | transaction |               | through- |
| --- | --- | --- | --- | ---------- | ---------- | ---- | ---- | ----------- | ------------- | -------- |
|     |     |     |     | put remain | vulnerable |      | to   | systematic  | manipulation. |          |
Transaction-graphanalyticsareappliedtouncoverthata
significantportionofaccountsexhibitbot-likebehavior.
|     |     |     |     | For instance,   | [86]    | analyzes     |          | features | such          | as the time |
| --- | --- | --- | --- | --------------- | ------- | ------------ | -------- | -------- | ------------- | ----------- |
|     |     |     |     | intervals       | between | transactions |          | and      | bursty        | co-activity |
|     |     |     |     | where multiple  |         | accounts     | perform  | actions  | in            | close tem-  |
|     |     |     |     | poral proximity |         | to identify  | accounts |          | with regular, | pre-        |
dictablepatternsindicativeofautomation.Theiranalysis
|     |     |     |     | reveals        | that over | 30.75%   | of        | the accounts  | (381,008 | in      |
| --- | --- | --- | --- | -------------- | --------- | -------- | --------- | ------------- | -------- | ------- |
|     |     |     |     | total) exhibit |           | bot-like | behavior, | participating |          | in more |
analyzing large datasets. By constructing localized than 192 million transactions and transferring around
subgraphsaroundeachtargettransactionandanalyzing 640 million EOS tokens in repetitive and exploitative
them with outlier-detection algorithms, the method is ways for malicious purposes like bonus hunting and
scalable by leveraging the parallel processing capa- clickingfraud.Similarly,[87]leverageslocalsubgraph
bilities of GPUs, making it feasible to analyze large embeddingsaroundpotentiallymaliciousaddressesand
datasets while maintaining effectiveness in identifying observes that short-lived, recurrent transaction cycles
anomaloustransactions.ForEthereum,[84]investigates arereliableindicatorsofscambehavior.Bycombining
transactions from an alleged Upbit exchange hack to these various features, accounts that are systematically
studyon-chainlaunderingpatterns.Amoneylaundering abusing the high-throughput capabilities of EOSIO are
| network         | on Ethereum was | constructed  | by crawling   | identified. |     |     |     |     |     |     |
| --------------- | --------------- | ------------ | ------------- | ----------- | --- | --- | --- | --- | --- | --- |
| the transaction | records         | of the Upbit | Hack and then |             |     |     |     |     |     |     |
conducting an analysis of the money laundering net- Although these graph-based methodologies have yielded
work properties by comparing the money laundering rich insights into blockchain networks, several important
networkwiththenormalnetworkonEthereum.Despite considerations remain. Noted that Table 5, 6 and 7 do not
Ethereum’s fast transaction capabilities, the results contain a ‘‘Measure’’ column since these network-focused
show that money laundering accounts on Ethereum methods predominantly emphasize topological or structural
are fast-in and fast-out accounts, meaning that dirty features of the transaction graph rather than, for instance,
money is transferred in and out quickly by money specific predictive or classification metrics. On the plus
laundering accounts. Also, compared with traditional side,structuralorcommunityanalyseseffectivelyilluminate
money laundering accounts that usually transfer high- how small sets of aggregator nodes or hub addresses exert
volumemoney,prudentmoneylaunderingaccountson large-scale influence, and they are readily generalized to
Ethereum tend to transfer very small-volume money differentcryptoassetsortokensystemsbysimplyredefining
to evade the attention of regulatory authorities. The nodeoredgetypes.Temporalandevolutionaryapproaches—
actors take advantage of decentralized exchanges for suchasdynamicsnapshots,preferential-attachmentmodels,
rapidlayeringtoobscuretheoriginoffundsandevade or subgraph anomaly detection—add further realism and
detection. They also found that, like traditional money can capture short-lived or bursty behaviors often missed
laundering accounts, money laundering accounts on by purely static analyses. However, all of these techniques
Ethereum are zero out middle accounts, meaning that face scalability challenges as blockchains grow in both
theypotentiallytransferalmostallincomingmoneyout transaction volume and participant diversity, and complex
tobenefitinabigway. subgraph or multi-dimensional embeddings can quickly
• SubgraphPatterns:Meanwhile,[85]introducesTrans- become computationally expensive for large datasets. Fur-
action SubGraph Networks (TSGN) for phishing thermore, clustering heuristics and models like Chung–Lu
detection. The study used embed local subgraphs or Barabási–Albert can fail to capture special nodes (e.g.,
aroundpotentiallymaliciousaddressesandobservethat centralized exchanges, mixers) or ephemeral patterns aris-
ephemeral,cyclicalin–outflowsarereliableindicators ing from purposeful on-chain manipulations, limiting their
of scam behavior. In phishing attacks, funds typically predictive power. Real-world heterogeneities such as multi-
flowintothescammer’saddressandarequicklymoved signature addresses, advanced DeFi operations, or bridging
out through a series of transactions to obscure their solutionsspanningmultipleblockchainscomplicatestraight-
| 202596 |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
forward generalization. Moreover, while local subgraph weightstominorityclasssamplesthatarehardertoclas-
extraction helps isolate suspicious flows, it risks overlook- sify,therebyimprovingthemodel’sabilitytodistinguish
ing broader interactions that cross these local boundaries. betweenlegitimateandfraudulenttransactions.AnF1-
Hence, future improvements might focus on more scalable score above 95% reflects the synergy between robust
high-performance computing (e.g., GPU-based pipelines) feature engineering including user-specific transaction
plus adaptive heuristics that incorporate domain-specific frequency and connectivity and ensemble-based model
| behaviors(mixers,privacyprotocols,exchangedepositwal- |     |     |     |     |     |     |     | fusion. |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
lets,etc.)whilebalancinginterpretabilitywiththecomplexity Recent work in Ethereum phishing and suspicious
requiredtohandleblockchains’rapidlyshiftingtopologies. addressdetectionleveragesavarietyofmachinelearn-
ingtechniquesandfeatureengineeringapproaches.For
|     |     |     |     |     |     |     |     | instance, | [90] | uses XGBoost | and | RF  | with a | blend of |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ------------ | --- | --- | ------ | -------- |
C. MACHINELEARNING
structuralandtemporalattributesintheEthereumtrans-
| Machine | learning | approaches |     | have | become | increasingly |     |     |     |     |     |     |     |     |
| ------- | -------- | ---------- | --- | ---- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
dominantincryptoassetanomalydetectionduetotheirability action network. By quantifying transaction frequency,
|          |         |          |      |             |             |     |       | inter-event | timing, | local | node degrees, |     | and address | re- |
| -------- | ------- | -------- | ---- | ----------- | ----------- | --- | ----- | ----------- | ------- | ----- | ------------- | --- | ----------- | --- |
| to learn | complex | patterns | from | large-scale | transaction |     | data. |             |         |       |               |     |             |     |
These methods can be categorized based on their learning use,theirpipelineachieves98%F1-scoresforphishing
detection.Meanwhile,[91]focusesonnode2vecembed-
paradigmandarchitecturaldesign.
|     |     |     |     |     |     |     |     | dings combined |       | with Adaptive |     | Boosting | (AdaBoost) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----- | ------------- | --- | -------- | ---------- | --- |
|     |     |     |     |     |     |     |     | to detect      | money | laundering    | in  | Bitcoin, | concluding |     |
1) SUPERVISEDLEARNING
|              |               |              |                 |              |         |            |         | that temporal  |                   | behaviors      | and graph-based |           | embeddings |           |
| ------------ | ------------- | ------------ | --------------- | ------------ | ------- | ---------- | ------- | -------------- | ----------------- | -------------- | --------------- | --------- | ---------- | --------- |
| Supervised   | learning      | methods      |                 | rely on      | labeled | datasets   | to      |                |                   |                |                 |           |            |           |
|              |               |              |                 |              |         |            |         | rank among     | the               | most important |                 | features. |            | Likewise, |
| train models | that          | can classify |                 | transactions | or      | addresses  | as      |                |                   |                |                 |           |            |           |
|              |               |              |                 |              |         |            |         | [92] presents  | ‘‘GuiltyWalker,’’ |                | a               | method    | that       | measures  |
| legitimate   | or anomalous. |              | A number        | of           | works   | have       | applied |                |                   |                |                 |           |            |           |
|              |               |              |                 |              |         |            |         | each address’s |                   | distance       | from known      |           | illicit    | nodes via |
| classical    | supervised    | ML           | for cryptoasset |              | fraud   | detection, |         |                |                   |                |                 |           |            |           |
randomwalks;thesedistance-basedfeatures,whenfed
focusingonconstructingdomain-specificfeaturesandtrain-
|                    |         |             |            |         |            |           |         | into RF      | yield           | notable accuracy |          | gains    | for          | malicious  |
| ------------------ | ------- | ----------- | ---------- | ------- | ---------- | --------- | ------- | ------------ | --------------- | ---------------- | -------- | -------- | ------------ | ---------- |
| ing algorithms     |         | such as     | Random     | Forest, | SVM,       | LightGBM, |         |              |                 |                  |          |          |              |            |
|                    |         |             |            |         |            |           |         | address      | identification. | Across           | these    | studies, |              | consistent |
| or XGBoost.        | Feature | engineering |            | plays   | a crucial  |           | role in |              |                 |                  |          |          |              |            |
|                    |         |             |            |         |            |           |         | improvements |                 | arise from       | layering | graph    | connectivity |            |
| model performance, |         | with        | successful |         | approaches | incorpo-  |         |              |                 |                  |          |          |              |            |
features,e.g.in/outdegrees,clusteringcoefficients,over
| rating features |     | from multiple |     | dimensions |     | ranging | from |     |     |     |     |     |     |     |
| --------------- | --- | ------------- | --- | ---------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
themorecommontransactionortemporalsignals.
| raw transaction      |            | records  | to abstract | topological |           | or temporal |         |                 |     |              |                 |     |       |        |
| -------------------- | ---------- | -------- | ----------- | ----------- | --------- | ----------- | ------- | --------------- | --- | ------------ | --------------- | --- | ----- | ------ |
|                      |            |          |             |             |           |             |         | • Ponzi Scheme  |     | & HYIP       | Identification: |     | Other | works  |
| metrics consistently |            | boosting | detection   |             | accuracy. | The         | most    |                 |     |              |                 |     |       |        |
|                      |            |          |             |             |           |             |         | target specific |     | subproblems, | such            | as  | Ponzi | scheme |
| effective            | supervised | methods  |             | incorporate | diverse   |             | feature |                 |     |              |                 |     |       |        |
detection.Earlyexamplesinclude[93]and[94],which
types,typicallyencompassing(i)Transactionfeaturessuch
|            |           |            |                |              |            |       |         | rely on         | SVM, | decision trees, | and        | XGBoost |             | to detect |
| ---------- | --------- | ---------- | -------------- | ------------ | ---------- | ----- | ------- | --------------- | ---- | --------------- | ---------- | ------- | ----------- | --------- |
| as amount, | fee,      | timestamp, | and            | confirmation |            | time, | (ii)    |                 |      |                 |            |         |             |           |
|            |           |            |                |              |            |       |         | Ponzi contracts |      | on Ethereum.    |            | Results | demonstrate |           |
| Temporal   | features  | such       | as transaction |              | frequency, |       | timing  |                 |      |                 |            |         |             |           |
|            |           |            |                |              |            |       |         | that combining  |      | smart contract  | code-level |         | signals,    | e.g.,     |
| patterns,  | and burst | behavior,  | (iii)          | Graph        | features   |       | such as |                 |      |                 |            |         |             |           |
extractedopcodesandfunctionusage,withtransaction-
| in/out degree, |          | clustering | coefficient, |        | centralities, | and | (iv) |                |         |                 |           |       |         |         |
| -------------- | -------- | ---------- | ------------ | ------ | ------------- | --- | ---- | -------------- | ------- | --------------- | --------- | ----- | ------- | ------- |
|                |          |            |              |        |               |     |      | based metrics, |         | i.e., frequency | and       | daily | volume, | mea-    |
| Behavioral     | features | such       | as address   | reuse, | transaction   |     | size |                |         |                 |           |       |         |         |
|                |          |            |              |        |               |     |      | surably        | improve | classifier      | precision | and   | recall. | In line |
distribution.
withthis,[95]appliesstandardtextclassificationusing
• Fraud & Suspicious Activity Detection: Several SVMandNaiveBayesonSoliditycodetokensforPonzi
studies adopt classic ML approaches with carefully detection. This approach treats the smart contract code
engineeredfeatures.In[88],acombinationofRandom astextandutilizesnaturallanguageprocessingmethods
Forest and XGBoost is employed for fraud detection to identify patterns indicative of Ponzi schemes. The
| in Bitcoin. |     | High accuracy |     | is achieved | by  | synthesizing |     |              |          |          |      |     |         |       |
| ----------- | --- | ------------- | --- | ----------- | --- | ------------ | --- | ------------ | -------- | -------- | ---- | --- | ------- | ----- |
|             |     |               |     |             |     |              |     | near-perfect | accuracy | reported | with | 99% | overall | accu- |
transaction and graph-based metrics, e.g. transaction racy underscores that raw contract text, featuring code
amounts,nodedegrees,andedgetimestamps,allowing usage patterns and address references, can effectively
the ensemble to capture both local (transaction-level) signal suspicious activity. This indicates that even
and global (address-level) patterns. Similarly, [89] without a deep analysis of the opcodes or transaction
| proposes |     | a stacking | ensemble |     | using decision |     | trees, |     |     |     |     |     |     |     |
| -------- | --- | ---------- | -------- | --- | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
history,thetextualcontentofthecontractitselfcontains
naiveBayes,k-nearestneighbors,andrandomforestfor discriminativefeaturesthatcanbeusedtodetectPonzi
Bitcoinfraud.AdaptiveSyntheticSampling(ADASYN) schemes.Buildinguponthislineofwork,[96]proposes
isutilizedtoaddressclassimbalance,complementedby heterogeneousfeatureaugmentation(HFAug),afeature
SHAPforinterpretability.ADASYNisanoversampling augmentation scheme that integrates heterogeneous
| technique |     | that generates |     | synthetic | samples |     | for the |             |          |       |             |     |          |      |
| --------- | --- | -------------- | --- | --------- | ------- | --- | ------- | ----------- | -------- | ----- | ----------- | --- | -------- | ---- |
|           |     |                |     |           |         |     |         | transaction | records, | e.g., | transaction |     | amounts, | time |
minorityclass(e.g.,fraudulenttransactions)byfocusing lags between consecutive transactions and frequency
on harder-to-learn examples. Unlike simpler oversam- oftransactions,andmeta-path-basedstructuralfeatures.
pling methods like SMOTE, ADASYN assigns higher WhenevaluatedusingLogisticRegression(LR),SVM,
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 202597 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
andRF,resultsconfirmthatcapturingbothtemporaland expandedby[105]toincludemulti-digraphembeddings
graph structures significantly strengthens classification thatincorporatetransactiontimewindows,highlighting
performanceforPonzidetection. the importance of temporal features and burst behav-
Focusing on Ponzi or High-Yield Investment Program iors in enriching graph-based signals. Expanding on
(HYIP)detection,[97]usesRF,NN,andk-NNtodetect these efforts, [106] introduces XGBCLUS, a frame-
Ponzi schemes on Ethereum. Over 20,000 Ethereum work designed for anomaly detection that combines
transactions were analyzed and preprocessed to train XGBoost with under-sampling techniques to address
the models. Their main result shows that a large, class imbalance to detect anomalies such as fraudulent
over 70 sets of raw features can be pruned down to ormaliciousactivitieswithinBitcoinnetworks.Byinte-
about10corefeatureswithoutcompromisingaccuracy. gratingexplainableAItechniqueslikeSHAP,theresults
Thesecorefeatureslikelyincludetransaction-leveland show how features such as transaction volumes play a
address-level metrics, such as transaction amounts, paramountroleinclassifyinganomaloustransactions.
frequency, timing intervals, and patterns indicative of • SupervisedDeepLearningApplications:Lastly,[107]
Ponzischemes.Similarly,[98]tacklestheidentification demonstrates a supervised deep-learning approach that
of HYIP operators’ Bitcoin addresses via a custom usesanLSTM/Bi-LSTM/CNNensembleforEthereum
scraping-based approach. They highlight the effect of phishingclassification.Althoughtheseareindeeddeep
transaction features like frequency of transactions per neural architectures, the pipeline is fully supervised,
day, deposit–withdrawal patterns, and transaction size relying on a labeled dataset of malicious and benign
distributions onclassification performance,concluding addresses. Contrary to some graph-based methods, the
that gleaning large labeled sets is critical to robust authors do not incorporate domain-specific features
superviseddetection. (e.g., transaction frequency, node degrees, or gas
• Address Role Classification & Scalable Pipelines: usage). Instead, they embedded the raw addresses and
Another group deals with GPU-accelerated or large- fed them into the ensemble model, achieving near
scale supervised pipelines. References [99] and [100] 99%detectionaccuracy.Thisoutcomeunderscoresthe
adoptSVM,RF,andLogisticRegressionontensofmil- strength of combining address-level embeddings with
lionsofBitcoin/Ethereumtransactions,showcasingthat advanced neural networks for phishing detection in
parallelization (e.g., GPU computing) is essential for Ethereum.
near-real-time detection. Their data includes advanced
features like node centralities, transaction bursts, and Table8providesanoverviewofrepresentativesupervised
timing intervals, and the results indicate that even techniques for cryptoasset anomaly detection, highlighting
incremental improvements in feature engineering can theirperformancemetrics,datasources,andtargetanomalies.
manifestaslargegainsindetectionspeedandprecision In general, Random Forest (RF) appears frequently and
on these large networks. Similarly, [101] examines often outperforms other classic ML methods, e.g., deci-
suspicious-user detection in Bitcoin trust networks sion trees, SVM, or logistic regression, likely due to its
with RF, deriving especially strong signals from node robustness against noisy features and its ability to capture
centralities and trust-based features, where users rate both nonlinear and interaction effects among transaction,
eachotheronascaletoindicatetheirleveloftrust,which temporal, and graph inputs. However, a major drawback
capturehowuserreputation,quantifiedthroughthetrust of most supervised approaches is their susceptibility to
scoresassignedtotheuserbytheirpeers,andtransaction class imbalance, as many real-world datasets exhibit far
patternsconnect. fewer fraudulent or malicious samples than legitimate ones.
Recent works highlight role classification rather than Although techniques like SMOTE or ADASYN partially
directanomalydetection.Reference[102]trainsRFand addressthisimbalance,oversamplingcanintroducesynthetic
XGBoosttoclassifyEthereumaddressesasexchanges, noise, while undersampling risks discarding informative
wallets, or other key agents. They show that addresses samples. Moreover, many of these studies rely heavily on
exhibit distinctive transaction frequencies and code public, on-chain datasets, which may omit off-chain data
usage patterns, making assigning roles with high such as user reputations or external intelligence. Methods
confidencefeasible.Extendingthis,[103]introduceda thatexploitprivateorproprietarydataliketrustscores,code
pipelinecalledGTN2vectoembedEthereumaddresses annotations, or exchange user logs may improve accuracy
with features like gas price and timestamps in random butarelessgeneralizableiftheseproprietarysourcesarenot
walks, enabling robust money laundering detection publiclyavailable.Finally,whileensembleanddeep-learning
via RF classifiers. Similarly, Bitcoin-focused studies pipelines can be scaled to large transaction networks (some
have developed specialized approaches for address employingGPUaccelerationfortensofmillionsofrecords),
classification.Reference[104]proposedmoment-based theirperformancemaystillbeconstrainedbythequalityand
features such as variance and skewness of transaction consistencyoflabels,underliningthecontinuingimportance
amounts and used LightGBM to achieve high F1 of robust data collection and labeling strategies for new
scoresforabnormaladdressdetection.Thiswasfurther researchdirections.
202598 VOLUME13,2025

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
TABLE8. Supervisedlearningmethods. annotations. These approaches aim to capture the underly-
ing structure in transaction or address networks, allowing
researcherstoflagsuspiciousoroutlierbehaviors.
• Clustering-Based Anomaly Detection: A number of
studiesfocusonclustering-basedtechniquestoseparate
normal versus anomalous user activity. For instance,
[108]adoptstrimmedk-meansonBitcoindatatoisolate
potentialfraudclustersbyremovingoutliersthatmight
distort the centroids. Their experiments demonstrate
that removing a small percentage of extreme points
before clustering significantly improves overall fraud
detection rates. Similarly, [109] and [110] combine
k-means,Mahalanobisdistance,andunsupervisedSup-
port Vector Machines (SVMs) to detect anomalies in
both user-centric and transaction-centric graphs. For a
user-centric graph, each node represents an individual
user, aggregating one or more Bitcoin addresses, and
edges between nodes capture transactions between
users.Incontrast,atransaction-centricgraphtreatseach
transaction as a node, and edges typically represent
the Bitcoin flow. By extracting features such as in-
degree, out-degree, average transaction size, and time-
interval statistics, their pipelines reveal that suspicious
transactionsgenerallydeviatemarkedlyfromthetypical
distribution of user behavior. Meanwhile, [111] pro-
posesatwo-stageapproachwhereOne-ClassSVMfirst
flagsoutliersamongBitcointransactions,thenk-means
groups similar outliers by type of attack (e.g. double-
spending,maliciouscampaigns).Thisdual-steppipeline
improvesinterpretability,aseachclusterofanomaliesis
mappedtolikelyfraudscenarios.
• Collective & Address Aggregation Approaches:
Other works focus on either addressing large-scale or
complex transaction graphs. Reference [112] studies
malicious address identification in Bitcoin by combin-
ing temporal burst features, e.g., abrupt increases in
transactionvolumeordegree,andgraph-basedmetrics,
e.g., clustering coefficient, in/out-degree. The study
highlights that aggregating addresses controlled by
the same user is crucial for achieving more accurate
anomaly scoring, i.e., disregarding the concept of
‘‘change addresses’’ can dilute signals indicative of
malicious behavior. In a typical Bitcoin transaction,
a user must spend the entire input, even if they intend
to send only a part of that amount to another party.
Theremainingbalanceisthensentbacktothesender’s
wallet via a new, often unrelated-looking address
called a change address. Reference [113] extends such
ideas using a collective anomaly detection paradigm
in Bitcoin, whereby clusters of wallets owned by
the same user are analyzed as a whole rather than
individually.Experimentalresultsshowthatconsidering
2) UNSUPERVISEDANDSEMI-SUPERVISEDLEARNING thejointbehavioracrossmultipleaddressescanincrease
Unsupervised learning methods address the challenge of recallinidentifyingmaliciousorhackedaccountssince
limitedlabeleddataincryptoassetecosystemsbyidentifying fraudsters often split illicit funds among numerous
intrinsic patterns without requiring extensive ground-truth addresses.
VOLUME13,2025 202599

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
• Semi-Supervised Learning with Graph Embed- TABLE9. Unsupervisedandsemi-supervisedlearningmethods.
dings:Beyonddirectclustering,somesemi-supervised
| approaches  |            | leverage | graph     | embeddings      |               | or       | node rep- |     |     |     |     |     |     |     |
| ----------- | ---------- | -------- | --------- | --------------- | ------------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| resentation |            | learning | to        | detect          | scams.        | For      | example,  |     |     |     |     |     |     |     |
| [114]       | implements |          | a network |                 | embedding     | pipeline | for       |     |     |     |     |     |     |     |
| Ethereum    |            | phishing | detection | by              | incorporating |          | transac-  |     |     |     |     |     |     |     |
| tion        | metadata   | (e.g.,   | amount,   | timestamp).     |               | After    | embed-    |     |     |     |     |     |     |     |
| ding        | addresses  |          | into a    | low-dimensional |               | space,   | they      |     |     |     |     |     |     |     |
applyone-classSVMtoseparatenormalfromphishing
| nodes.       | Results  | indicate     |             | that preserving |              | both         | temporal |     |     |     |     |     |     |     |
| ------------ | -------- | ------------ | ----------- | --------------- | ------------ | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- |
| and          | weighted | edge         | information |                 | during       | embedding    |          |     |     |     |     |     |     |     |
| (transaction |          | sums,        | frequency)  |                 | can markedly |              | enhance  |     |     |     |     |     |     |     |
| the          | recall   | for phishing | address     |                 | detection,   | highlighting |          |     |     |     |     |     |     |     |
thatmorenuancedembeddingscapturesubtlefraudulent
| signatures |     | more | effectively | than | simpler | topological |     |     |     |     |     |     |     |     |
| ---------- | --- | ---- | ----------- | ---- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
embeddingsalone.
| Unsupervised |           | and         | semi-supervised |        | methods    |             | (Table 9) |     |     |     |     |     |     |     |
| ------------ | --------- | ----------- | --------------- | ------ | ---------- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| address      | the lack  | of          | large labeled   |        | datasets   | by          | detecting |     |     |     |     |     |     |     |
| intrinsic    | structure | or outliers |                 | within | blockchain | transaction |           |     |     |     |     |     |     |     |
networks,aclearadvantageoverfullysupervisedapproaches
| that require | extensive  |     | annotation. | Because  |       | many       | suspicious |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | ----------- | -------- | ----- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| behaviors    | are subtle | or  | evolve      | quickly, | these | clustering | and        |     |     |     |     |     |     |     |
outlier-basedtechniques,e.g.,k-meansandOne-ClassSVM,
excelatcapturingneworemergingfraudpatternsthatstrictly
supervisedpipelinesmightmiss.Moreover,groupingsuspi-
ciousactorswithoutpriorlabelsprovidesapracticalfirststep widely applied to tasks ranging from suspicious address
inhighlightinghigh-riskusersortransactionsforsubsequent classificationtocontract-levelfrauddetection.
| investigation.   | By       | detecting  | the     | intrinsic | structure |              | or outliers |            |           |               |         |           |                |          |
| ---------------- | -------- | ---------- | ------- | --------- | --------- | ------------ | ----------- | ---------- | --------- | ------------- | ------- | --------- | -------------- | -------- |
|                  |          |            |         |           |           |              |             | • Temporal | GNNs      | &             | Dynamic | Analysis: |                | Multiple |
| within the       | network, | these      | methods |           | mitigate  | the          | imbalance   |            |           |               |         |           |                |          |
|                  |          |            |         |           |           |              |             | studies    | leverage  | time-evolving |         | behavior  | in transaction |          |
| problem          | inherent | in scarce  |         | labeled   | data,     | a limitation | that        |            |           |               |         |           |                |          |
|                  |          |            |         |           |           |              |             | records.   | In [115], | a temporal    |         | GCN is    | integrated     | with     |
| fully supervised |          | approaches |         | must      | contend   | with.        | However,    |            |           |               |         |           |                |          |
anLSTMbackbonetodetectillicitBitcointransactions
thesemethodsoftensufferfromlimitedinterpretability,e.g.,
|                 |           |                 |               |         |          |              |          | by capturing |             | dynamic        | changes    | in the    | Elliptic       | dataset. |
| --------------- | --------- | --------------- | ------------- | ------- | -------- | ------------ | -------- | ------------ | ----------- | -------------- | ---------- | --------- | -------------- | -------- |
| why a cluster   |           | is flagged      | as suspicious |         | can      | be unclear,  | and      |              |             |                |            |           |                |          |
|                 |           |                 |               |         |          |              |          | Exploiting   | the         | chronological  |            | ordering  | of transaction |          |
| false positives |           | may be          | high          | without | further  | refinements, |          |              |             |                |            |           |                |          |
|                 |           |                 |               |         |          |              |          | blocks       | enhances    | classification |            | accuracy, | as each        | block    |
| such as         | combining | domain-specific |               |         | features | or           | post-hoc |              |             |                |            |           |                |          |
|                 |           |                 |               |         |          |              |          | includes     | a timestamp |                | indicating | when      | it was         | mined,   |
classificationtofilteralerts.Comparedtothefullysupervised
|     |     |     |     |     |     |     |     | forminganorderedsequenceB |     |     |     | → B | →   | B ... |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | ----- |
approaches discussed in the previous section, which tend k k+1 k+2
|            |        |           |     |       |          |         |       | that reflects |         | the timeline | of  | transaction | appearance |          |
| ---------- | ------ | --------- | --- | ----- | -------- | ------- | ----- | ------------- | ------- | ------------ | --- | ----------- | ---------- | -------- |
| to achieve | higher | precision |     | given | abundant | labeled | data, |               |         |              |     |             |            |          |
|            |        |           |     |       |          |         |       | on the        | ledger. | For example, |     | if block    | k is       | followed |
unsupervisedpipelinesmustcarefullytunehyperparameters,
|              |     |           |         |             |     |                 |     | by block | k      | + 1, the | transactions |       | in block | k +      |
| ------------ | --- | --------- | ------- | ----------- | --- | --------------- | --- | -------- | ------ | -------- | ------------ | ----- | -------- | -------- |
| e.g., number | of  | clusters, | outlier | thresholds, |     | and incorporate |     |          |        |          |              |       |          |          |
|              |     |           |         |             |     |                 |     | 1 must   | happen | after    | those in     | block | k. By    | treating |
domainknowledge,e.g.,changeaddressheuristics,toreduce
|     |     |     |     |     |     |     |     | each block | as  | a temporal | slice, | the | model | identifies |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | ------ | --- | ----- | ---------- |
noise.Consequently,whiletheseapproachesareimmensely
|          |              |          |               |     |           |            |           | evolving   | patterns, | e.g.,         | unusual | transaction      |     | values or |
| -------- | ------------ | -------- | ------------- | --- | --------- | ---------- | --------- | ---------- | --------- | ------------- | ------- | ---------------- | --- | --------- |
| flexible | and scalable | for      | preliminary   |     | screening | or         | for newly |            |           |               |         |                  |     |           |
|          |              |          |               |     |           |            |           | addresses, | rather    | than assuming |         | all transactions |     | occur     |
| emerging | fraud        | vectors, | practitioners |     | may       | ultimately | need      |            |           |               |         |                  |     |           |
simultaneously.Relatedly,[116]constructsforwardand
| to fuse        | them | with        | supervised | classifiers, |     | where       | labels |                       |          |             |     |            |         |            |
| -------------- | ---- | ----------- | ---------- | ------------ | --- | ----------- | ------ | --------------------- | -------- | ----------- | --- | ---------- | ------- | ---------- |
|                |      |             |            |              |     |             |        | reverse               | Ethereum | transaction |     | graphs and | applies | a bi-      |
| are available, |      | to maximize |            | detection    |     | performance | and    |                       |          |             |     |            |         |            |
|                |      |             |            |              |     |             |        | graph attention-based |          | network     |     | (LB-GLAT)  |         | to address |
interpretability.
thelimitationsposedbytheacyclicnatureoftransaction
|     |     |     |     |     |     |     |     | graphs, | which | can obscure |     | contextual | relationships. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ----------- | --- | ---------- | -------------- | --- |
3) DEEPLEARNING&GRAPHNEURALNETWORKS The forward graph captures the natural flow of funds
Deep learning architectures have demonstrated exceptional from senders to receivers, while the reverse graph,
performance in cryptoasset anomaly detection by auto- constructed by inverting edge directions, reveals the
matically learning hierarchical representations from raw originoffunds.Learningfrombothdirectionsimproves
transaction data. Neural network approaches such as mul- the detection of money laundering. Reference [117]
tilayer perceptrons (MLPs), convolutional neural networks formalizesthedetectionofmaliciousEthereumactivity
(CNNs), and recurrent neural networks (RNNs) have been using multi-layer temporal snapshots across multiple
| 202600 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
tokens.Theirapproachintegratesthesesnapshotswithin • Heterogeneous, Multi-View & Subgraph-Focused
a temporal framework by segmenting the transaction GNNs: Some approaches emphasize the use of
dataintodistincttimewindowsbasedonthetimestamp multi-type edges or multi-view channels in transac-
on each transaction. Snapshots from different tokens tion networks. Multi-type edges reflect that not all
that fall within the same time window are merged into relationships in a transaction graph are homogeneous;
unified graphs, to which a graph convolution encoder edges may represent distinct types of interactions,
isappliedtoextractspatialandtemporalfeatures.This for instance, a basic fund transfer versus a contract
enables the model to effectively capture cross-token code invocation, or correspond to different analytical
trading patterns and detect evolving behaviors, such as perspectives.Thisideaisoftenoperationalizedthrough
sudden shifts in transaction volumes or unusual flows multi-view channels, where each channel represents
that may indicate malicious activities. The model sig- a subgraph that captures a specific facet of the
nificantly improves precision and recall by integrating overallnetwork.Reference[121]usesaheterogeneous
these temporal snapshots with a GNN-based encoder. graph neural network based on a relational graph
In a related approach, [118] uses a time-decayed convolutional network (RGCN) to account for diverse
mechanismtobuilddynamictransactionsubgraphsfor transaction types on Ethereum, such as contract calls
Bitcoinforecasting(DLForecast).Theresultsshowthat and standard transfers. Explicitly modeling each edge
weightingrecenttransactionsmoreheavilysubstantially type by assigning distinct parameters to different
boostsaccuracyinpredictingfutureedges(transactions) transaction categories proves crucial for effective
andhighlightspotentialanomaliesearlier. phishing detection, particularly in scenarios with label
• Transformer-Based Approaches: Transformer mod- imbalance.Meanwhile,[122]integratesBayesianuncer-
els,whichleverageself-attentionmechanismstocapture tainty modeling with a multi-channel graph attention
relationshipsbetweenelementsinsequences,havebeen network to secure Ethereum-based Internet of Things
widely adopted for anomaly detection due to their (IoT) transactions. Incorporating Bayesian uncertainty
capacity to process long sequences and extract com- enables a more robust handling of noise and class
plex patterns from unstructured data. Reference [119] imbalance by allowing prediction adjustments based
propose BERT4ETH, a pre-trained Transformer-based onestimateduncertainty.Themulti-channelaggregator
modelthattreatssequencesofEthereumaddressesand processesdifferenttransactionsubgraphsindependently,
transactions as ‘‘tokens’’ within a language-modeling improving robustness and classification performance
framework. In natural language processing, tokens whenidentifyinganomalousIoTdeviceaddresses.
typicallyrepresentwordsorsubwordsthatserveasthe Methods proposed in [123] and [124] emphasize the
fundamental units for learning representations. In this importance of extracting localized subgraphs around
context,asubsetofaddressesinatransactionsequence targetaddressesforimprovedclassification.Zhouetal.
israndomlyreplacedwithaspecial[MASK]token,and [123]introduceEthident,ahierarchicalGNN(HGATE)
the model is trained to predict the masked addresses framework that samples micro interaction subgraphs
using the surrounding unmasked tokens. This masked from Ethereum and conducts classification at the
modeling strategy encourages learning robust contex- subgraph level. To address label scarcity, a contrastive
tual relationships among addresses, yielding notable self-supervision module is incorporated, resulting in
improvements in tasks such as phishing classification a 1–5% relative improvement in accuracy compared
and de-anonymization. Similarly, [120] integrates a to baseline GNN models. In a complementary line
Variational Autoencoder (VAE) with a Transformer of work, Nicholls et al. [124] propose FraudLens,
architecturetodetectanomaliesindecentralizedfinance whichrestructurestheBitcointransactiongraphthrough
(DeFi) protocols. The VAE compresses data into a affinity- or feature-based edge construction prior to
low-dimensional latent space while preserving local GNN training. Refinement of the graph structure
features, effectively capturing short-term behavioral through the removal of extraneous edges leads to
patterns within limited time windows. In contrast, the substantial gains in classification performance when
Transformer component models long-range dependen- identifyingillicittransactionnodes.
cies, enabling the detection of relationships between Several studies adopt a star-shaped subgraph centered
temporally distant events. These long-range dependen- aroundeachsuspiciousaddress.Reference[125]focus
ciesenhancethemodel’sabilitytodetectpatternswhere on phishing detection by constructing star subgraphs
past behaviors influence future activity. The resulting enriched with multi-scale features, including inbound
framework, Anomaly VAE-Transformer, demonstrates and outbound transaction volumes, node lifetime, and
strong performance in identifying malicious structural other relevant attributes. The resulting GNN-based
shifts,suchasthoseassociatedwithflash-loanattacks, classification achieves nearly 99% recall on phishing-
and outperforms conventional CNN- and LSTM-based labeledaddresses,effectivelycapturinglocalizedtrans-
methodsonlarge-scaleDeFidatasets. actional patterns characteristic of phishing activity.
VOLUME13,2025 202601

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
Likewise,[126]alsoutilizesstarsubgraphsbutempha- cryptoasset data. Reference [132] transform Ethereum
sizes the aggregation of both node and edge features bytecode and Application Binary Interface (ABI) data
through a two-layer attention mechanism. By incorpo- into grayscale images and employ an attention capsule
ratingmanuallyengineeredfeatures—suchasminimum network for Ponzi scheme detection. This architecture
andmaximumtransactionvalues—intothenodeembed- integrates capsule networks that preserve hierarchical
dings, the approach significantly enhances detection spatialrelationshipsindatawithanattentionmechanism
performance, reaching up to 99.3% recall. This repre- thatselectivelyemphasizessalientfeatures.Theresult-
sents a substantial improvement over embedding-only ing attention-augmented capsules effectively capture
baselinessuchasDeepWalk.Inthesamevein,[127]pro- code-level patterns in visual representations, achieving
poses MP-GCN for phishing node identification, with anF1scoreofapproximately98.38%.Reference[133]
anemphasisondirectedmessagepassing.Byexplicitly introduce ChaosNet, a biologically inspired artificial
modeling the directionality of transactions, MP-GCN neuralnetworkthatemulateschaoticdynamicsobserved
enablesamulti-hopaggregationmechanismthatextends inbiologicalneuronsusingchaoticneuronmodelsbased
beyondimmediate(first-order)neighborstoincorporate on Generalized Luröth Series (GLS) maps. Applied
informationfrommoredistantnodesinthetransaction to Ethereum address classification, the model demon-
graph. This design carefully integrates features along stratesstronggeneralizationandmaintainscompetitive
the flow of transactions, allowing the model better to or superior accuracy with fewer training samples.
capturestructuralandbehavioralpatternscharacteristic Meanwhile,[134]divergesfromtransaction-levelGNNs
ofphishingactivities.Experimentalresultsdemonstrate and applies a standard feedforward NN to identify a
strongclassificationperformance,highlightingthecriti- day-of-the-weekeffectincryptoassetpricing.Although
calroleofdirectionalityindistinguishingphishingfrom not focused on GNNs or anomaly detection, the study
legitimateaddresses. illustrateshowdeeplearningarchitecturescanuncover
• Standard GNN Architectures & Autoencoders: subtlecyclicalpatternsincryptomarketbehavior.Refer-
Another line of research applies GNNs with relatively ence[135]proposearandom-pacedstructure-to-vector
minimalgraphorfeatureengineering.Reference[128] embedding technique for user addresses in NFT and
developapipelinethatcombinesrandom-walkembed- Ethereum networks. This method captures multi-scale
dingsforEthereumroleclassification,suchasidentify- structural identities—encompassing local connectivity,
ingexchangesorminerswithaGCNlayerforfinalpre- community-level relationships, and global structural
dictions.forfinalpredictions.Integratingrandom-walk roles—by sampling structural information at varying
embeddings with GNN-based feature aggregation temporalortopological‘‘paces.’’Theresultingembed-
demonstrates robust performance across large-scale dings support high classification accuracy in detecting
label sets. Reference [129] enhance suspicious address maliciousnodeswithinmetaverse-basedfinancialenvi-
detection on Bitcoin by introducing moment-based ronments.Finally,Huetal.[136]introduceSCSGuard,
features, including the variance and skewness of trans- which adopts a contract-level perspective by mapping
action amounts, into a lightweight GCN architecture, Ethereumbytecodeintoopcodesequencesanddetecting
achievingbothfasterconvergenceandstrongdetection scams using a Gated Recurrent Unit (GRU) network.
accuracy. Reference [130] frame Ethereum anomaly GRUs, a type of recurrent neural network, are partic-
detection as a one-class classification task, employing ularly effective at capturing temporal dependencies in
aGNN-basedautoencodertolearnnoderepresentations sequentialdata.Combinedwithanattentionmechanism,
fromtransactiongraphsandidentifyanomaliesbasedon the model achieves strong performance in identifying
reconstruction error. In this setting, the autoencoder is Ponzi and Honeypot contracts by learning critical
trainedexclusivelyonbenigntransactiondata,enabling opcodepatternsindicativeoffraudulentbehavior.
the detection of anomalous behavior as deviations
fromlearnednormalpatterns.Thismethodoutperforms Despite their notable achievements, the methods in 10,
conventional anomaly detection approaches such as spanning temporal GCNs, Transformer-based models, het-
IsolationForestandSVM,particularlyunderconditions erogeneousgraphnetworks,andspecializedneuralarchitec-
ofsevereclassimbalance.Finally,[131]applystandard tures,exhibitbothstrengthsandchallenges.Onthepositive
GCN and GAT to anti-money laundering and counter- side, time-aware GNNs and Transformer hybrids excel at
financingofterrorism(AML/CFT)detectiononBitcoin capturingdynamicorlong-rangedependencies,allowingthe
transaction networks. While GAT yields a modest detectionofsubtleshiftsintransactionpatternsthatsimpler
performanceimprovementoverGCN,botharchitectures baselineswouldmiss.Heterogeneousormulti-channelGNNs
offer substantial gains relative to simpler graph-based can handle different transaction types, e.g., contract calls
heuristics. versus standard transfers, improving expressiveness when
• Domain-Specific & Novel Neural Architectures: dealingwithcomplexblockchainecosystems.Further,focus-
Other works devise more domain-specific neural ing on local subgraphs or star-shaped neighborhoods often
network architectures tailored to unique aspects of offerscomputationalefficiency,makingitfeasibletoclassify
202602 VOLUME13,2025

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
TABLE10. Deeplearning&Graphneuralnetworks. directionsthatwarrantfurtherexploration.First,mostsuper-
|     |     |     |     |     |     |     | vised methods |     | require | large, | high-quality |     | labeled | datasets, |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | ------ | ------------ | --- | ------- | --------- | --- |
whichcanbeimpracticalduetodatascarcity,evolvingfraud
|     |     |     |     |     |     |     | tactics, | and class | imbalance, |     | where | legitimate |     | ones | dwarf |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---------- | --- | ----- | ---------- | --- | ---- | ----- |
fraudulentsamples.Thisimbalanceforcesdifficulttrade-offs
|     |     |     |     |     |     |     | between | metrics | such | as F1, | recall, | and | accuracy, | requiring |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ---- | ------ | ------- | --- | --------- | --------- | --- |
carefulcalibrationoradvancedoversampling/undersampling.
|     |     |     |     |     |     |     | Second,         | interpretability |                    | remains   | a            | critical     | hurdle;      | ensemble    |        |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ---------------- | ------------------ | --------- | ------------ | ------------ | ------------ | ----------- | ------ |
|     |     |     |     |     |     |     | and deep        | architectures    |                    | often     | act          | as black     | boxes,       | making      | it     |
|     |     |     |     |     |     |     | challenging     | to               | explain            | why       | transactions |              | or addresses |             | are    |
|     |     |     |     |     |     |     | flagged         | as anomalous.    |                    | Third,    | most         | studies      | focus        | on          | single |
|     |     |     |     |     |     |     | blockchain      | ecosystems;      |                    | future    | research     |              | could        | expand      | to     |
|     |     |     |     |     |     |     | multi-chain     | or               | cross-chain        |           | detection,   | given        | that         | malicious   |        |
|     |     |     |     |     |     |     | activities      | often            | spread             | across    | platforms.   |              | Fourth,      | real-time   |        |
|     |     |     |     |     |     |     | detection       | poses            | an additional      |           | challenge    |              | in dynamic   |             | envi-  |
|     |     |     |     |     |     |     | ronments        | such             | as DeFi,           | demanding |              | low-latency, |              | scalable    |        |
|     |     |     |     |     |     |     | methods         | that             | can handle         |           | continuous   | streams      |              | of transac- |        |
|     |     |     |     |     |     |     | tions. Finally, |                  | an ensemble-driven |           |              | paradigm     | where        | multiple    |        |
|     |     |     |     |     |     |     | diverse         | models           | such               | as RF,    | GNN,         | and          | Transformers |             | are    |
|     |     |     |     |     |     |     | simultaneously  |                  | trained            | and       | stacked      | represents   |              | a promising |        |
avenueforboostingrobustnessandgeneralization,especially
|     |     |     |     |     |     |     | under adversarial |                  | conditions. |         | Exploring       |                  | these      | directions,   |        |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ---------------- | ----------- | ------- | --------------- | ---------------- | ---------- | ------------- | ------ |
|     |     |     |     |     |     |     | particularly      | self-supervised, |             |         | active-learning |                  | approaches |               | for    |
|     |     |     |     |     |     |     | label-scarce      | scenarios        |             | and     | improved        | interpretability |            |               | frame- |
|     |     |     |     |     |     |     | works,            | would            | further     | advance | the             | reliability      |            | and practical |        |
deploymentofML-basedsolutionsinthecryptoassetdomain.
|     |     |     |     |     |     |     | D. HEURISTIC-BASED |               |           |             |             |             |                   |             |      |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | ------------- | --------- | ----------- | ----------- | ----------- | ----------------- | ----------- | ---- |
|     |     |     |     |     |     |     | Heuristic-based    |               | anomaly   | detection   |             | methods     | utilize           | expert-     |      |
|     |     |     |     |     |     |     | driven             | or rule-based |           | models      | to          | identify    | anomalous         |             | or   |
|     |     |     |     |     |     |     | fraudulent         | patterns      | within    | cryptoasset |             | transaction |                   | networks.   |      |
|     |     |     |     |     |     |     | These methods      |               | range     | from        | forensic    | and         | analytical        |             | mod- |
|     |     |     |     |     |     |     | eling to           | specialized   |           | protocol    | designs     |             | and cryptographic |             |      |
|     |     |     |     |     |     |     | techniques.        | In            | contrast  | to          | statistical | or          | machine           | learning-   |      |
|     |     |     |     |     |     |     | based techniques,  |               | heuristic |             | approaches  |             | often             | incorporate |      |
suspicious addresses on large-scale graphs. Nonetheless, domain-specific knowledge, emphasizing interpretability,
| several limitations |     | remain. | Many | of these | frameworks |     |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | ------- | ---- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
transparency,andregulatorycompliance.
| require extensive     |      | label            | availability    | or rely      | on carefully    |     |                                |     |            |     |          |            |     |      |     |
| --------------------- | ---- | ---------------- | --------------- | ------------ | --------------- | --- | ------------------------------ | --- | ---------- | --- | -------- | ---------- | --- | ---- | --- |
| tuned hyperparameters |      | for              | performance;    |              | label scarcity  | and |                                |     |            |     |          |            |     |      |     |
|                       |      |                  |                 |              |                 |     | 1) FORENSIC&ANALYTICALMODELING |     |            |     |          |            |     |      |     |
| class imbalance       |      | hamper           | generalization. |              | Domain-specific |     |                                |     |            |     |          |            |     |      |     |
|                       |      |                  |                 |              |                 |     | Forensic                       | and | analytical |     | modeling | approaches |     | rely | on  |
| approaches            | like | those processing |                 | raw bytecode | or capturing    |     |                                |     |            |     |          |            |     |      |     |
expert-definedheuristicsandempiricalobservationstotrace
chaoticneuronbehaviorscanbechallengingtoextendacross
multiple blockchain platforms with differing transaction suspicious activities, particularly those related to money
laundering,ransomwarepayments,andmarketmanipulation.
| structures.     | In addition, | interpretability |           | remains | a challenge;  |     |         |        |         |             |     |       |      |          |     |
| --------------- | ------------ | ---------------- | --------- | ------- | ------------- | --- | ------- | ------ | ------- | ----------- | --- | ----- | ---- | -------- | --- |
|                 |              |                  |           |         |               |     | Summary | of the | studies | categorized |     | under | this | category | is  |
| while attention |              | mechanisms       | partially | address | transparency, |     |         |        |         |             |     |       |      |          |     |
presentedintable11.
| fully justifying |     | why specific | nodes | or  | edges drive | the |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------ | ----- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
classification often requires additional heuristics. Finally, • Modeling & Analysis of Mixing Operations: A
real-time deployment in fast-paced contexts such as DeFi significant focus lies on understanding and model-
demandsfurtherworkonscalabilityandlatency.Thesegaps ing cryptoasset mixing services used for laundering.
suggest avenues for future research, such as self-supervised A heuristic-based goal modeling framework was intro-
or active-learning strategies for label-constrained scenarios, ducedtodetectandcategorizerolesinvolvedinBitcoin
multi-chain or cross-chain anomaly detection architectures, money laundering activities, particularly in mixing
and better interpretability frameworks to align with regula- operations[137].Amixingoperationreferstoaprocess
toryrequirements. where illicitly obtained cryptoasset is combined with
More broadly, these ML-based anomaly detection strate- fundsfromothersources,usingnumerousintermediate
gies face several interrelated limitations and open research addresses,toobscureitsoriginalsourceanddestination,
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 202603 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
thereby complicating tracking efforts. The approach refined approach incorporates address profiling—
classifies Bitcoin addresses involved in these activities classifying addresses as exchanges, darknet markets,
into three distinct roles based on their transaction payment processors, gambling services, and other
behaviorsandstructuralpatterns:entryaddresses(com- categories, to determine which paths are relevant.
municators),whichinitiallyreceiveillicitfunds,kernel Two context-based strategies are introduced to adapt
addresses (soldiers), intermediary addresses frequently the analysis depending on the situation. Evaluation
usedtoobscureandredistributefundswithinthemixing metrics based on expected behavior of illicit funds
network, and exit addresses (communicators), where and observable blockchain patterns are also defined to
funds ultimately leave the network, typically toward assess accuracy. This context-aware method reduces
fiatgatewaysorcryptoassetexchanges.Byheuristically unnecessary tracking and improves the detection of
modelingtheserolesthroughtransactioncharacteristics, meaningfultransactiontrails.
timing patterns, and relational structures, the method • Empirical Laundering Patterns: Further investiga-
systematically uncovers laundering activities within tionsfocusonhowcybercriminalsconvertstolenBitcoin
complexBitcointransactiongraphs. into usable funds exceeding $11 million [141]. One
Further analysis of mixing operations provides a more case study analyzes the Conti ransomware operation,
detailed understanding of the methods used to obscure a prominent ransomware-as-a-service (RaaS) group
illicit activity within blockchain networks. Modern activeuntil2022,whichtargetedbusinessesandcritical
services such as MixTum, Blender, and CryptoMixer infrastructure with high ransom demands [142], [143].
employ advanced techniques, including randomized Findingsshowthatwhilesomeactorsemployadvanced
transaction delays, multiple recipient addresses, parti- obfuscation, many rely on simpler methods such as
tioning transfers into smaller amounts, and the use of repeateduseofcentralizedexchanges,minimallayering,
‘‘sweeper’’transactionstoperiodicallyconsolidatedis- or peer-to-peer transfer networks. Even for high-value
persedfundsbeforeredistribution[138].Temporaland ransomwareproceeds,launderingpatternsofteninvolve
structuralfeatures,suchasdeposit–withdrawalintervals basic fund splitting and direct cash-out services, chal-
andaddressreusepatterns,exhibitconsistentbehaviors. lengingtheassumptionthatcomplexchainsandmultiple
Theanalysisemphasizes‘‘chain-level’’patterns,focus- mixersarealwaysused.
ing on sequences of transactions rather than individual Additional analysis has focused on fraud and scams
ones. Patterns such as short inter-transaction intervals, in the decentralized finance (DeFi) ecosystem, par-
repeatedfund-splitting,andsystematicaddressreuseare ticularly involving ERC-20 tokens on the Ethereum
commonly observed. By tracing how outputs from one blockchain [144]. Using open-source investigative
transaction serve as inputs to the next and identifying methods,includingtransactiontracingtoolslikeEther-
recurring features, such as typical transaction sizes or scan and smart contract analysis tools such as Slither,
timing intervals, it is possible to detect mixer-related patterns of illicit behavior such as rug pulls, pump-
transactionchainswithgreaterconfidence. and-dump schemes, and subsequent laundering activ-
A complementary abstraction model has been pro- ities have been identified. These techniques allow
posed to analyze both centralized and decentralized for examination of transaction histories, token flows,
mixers [139]. This three-phase model includes: taking smart contract behavior, and bridging activities across
inputs, performing the mix, and sending outputs. chains. Malicious actors often attract victims through
Transaction-level analysis of platforms such as Chip- decentralized exchanges, extract funds, and then move
Mixer, Wasabi Wallet, and ShapeShift demonstrates proceeds through mixers or cross-chain bridges. While
how asset-swapping mechanisms and anonymity set the technical complexity of the DeFi infrastructure
construction obscure fund provenance. Two frequently suggests the potential for sophisticated laundering,
observed techniques are peeling chains, where small findings indicate that many schemes rely on relatively
outputs are incrementally extracted over sequential simple methods, such as cashing out via centralized
transactions,andobfuscatingmechanisms,wheretrans- exchanges or using basic bridging strategies. These
actions are aggregated into anonymity sets to disrupt actions leave identifiable on-chain traces that can be
linkageanalysis.Whilethesetechniquesareintendedto systematically analyzed to uncover fraud patterns and
hindertracking,theyleavebehindidentifiabletracesthat actorlinkages.
canbesystematicallyanalyzed.
• Context-Aware Taint Analysis: Improvements to 2) PROTOCOL&CRYPTOGRAPHICDESIGN
traditional taint analysis have also been introduced Protocol and cryptographic design approaches focus on
to enhance the precision of tracing illicit Bitcoin embedding security features within blockchain systems or
flows [140]. Taint analysis marks coins as ‘‘tainted’’ evaluatingexistingmechanismstodetectweaknesses.Instead
when they are linked to illegal activity and follows ofconcentratingexclusivelyonuser-leveltransactionflows,
their movements through the blockchain. Rather these studies often scrutinize the underlying consensus
than tracking every transaction indiscriminately, the protocols,depositframeworks,andoracleimplementationsto
202604 VOLUME13,2025

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
TABLE11. Forensic&Analyticalmodeling. TABLE12. Protocol&Cryptographicdesign.
|     |     |     |     |     |     |     | to-Connected-Vehicle’’ |       |              | (Bit2CV) | scheme    |        | which uses |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | ----- | ------------ | -------- | --------- | ------ | ---------- |
|     |     |     |     |     |     |     | cryptographic          |       | endorsements |          | to verify | the    | origins of |
|     |     |     |     |     |     |     | deposited              | funds | has          | been     | proposed  | [146]. | In this    |
scheme,theanti-fraudmeasuresareprimarilybasedon
|     |     |     |     |     |     |     | a cryptographic |            | endorsement |              | procedure | that  | leverages  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | ----------- | ------------ | --------- | ----- | ---------- |
|     |     |     |     |     |     |     | threshold       | signatures | σ           | = (σ         | ,ε),      | where | σ is an    |
|     |     |     |     |     |     |     |                 |            |             |              | agg       |       | agg        |
|     |     |     |     |     |     |     | aggregated      | signature  | and         | ε represents |           | a set | of indices |
ensurerobustcryptographicguaranteesandresilienceagainst
maliciousactors.Forasummaryofthestudiesdiscussedin correspondingtothesignerswhoparticipatedincreating
thiscategory,refertotable12 the signature. In this scheme, a vehicle must collect
BFTProtocolForensics&Accountability:Onelineof endorsements from a threshold number of authorized
•
|     |     |     |     |     |     |     | parties to | verify | the origin | of  | deposited | funds, | thereby |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ---------- | --- | --------- | ------ | ------- |
workinvestigatesByzantineFaultTolerance(BFT)pro-
providingrobustanti-fraudmeasureswhilemaintaining
| tocol forensics, |     | which | formalizes | post-violation |     | diag- |     |     |     |     |     |     |     |
| ---------------- | --- | ----- | ---------- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
compatibilitywithexistingBitcoininfrastructure.
nosticsandaccountabilityinconsensusprotocols[145].
|             |            |     |        |          |      |        | • DeFi Oracle | Security |               | & Design: |         | Finally, | a broader |
| ----------- | ---------- | --- | ------ | -------- | ---- | ------ | ------------- | -------- | ------------- | --------- | ------- | -------- | --------- |
| When safety | violations |     | occur, | e.g when | more | than a |               |          |               |           |         |          |           |
|             |            |     |        |          |      |        | examination   | of       | decentralized |           | finance | oracles  | [147]     |
thresholdnumberofnodesactmaliciously,theprotocol
|             |     |          |                   |     |     |            | focuses | on how | blockchain |     | protocols | acquire | and |
| ----------- | --- | -------- | ----------------- | --- | --- | ---------- | ------- | ------ | ---------- | --- | --------- | ------- | --- |
| is expected | to  | generate | cryptographically |     |     | verifiable |         |        |            |     |           |         |     |
validatereal-worlddata,particularlymarketpricesand
evidencethatidentifiestheresponsiblereplicas.Tocap-
|                   |     |          |               |     |     |            | exchange | rates, | without | relying | on  | a single | trusted |
| ----------------- | --- | -------- | ------------- | --- | --- | ---------- | -------- | ------ | ------- | ------- | --- | -------- | ------- |
| ture a protocol’s |     | forensic | capabilities, |     | its | support is |          |        |         |         |     |          |         |
party.ThestudyinvestigatesmainstreamDeFiplatforms
summarizedbyatriplet(m,k,d)wheremthemaximum
|     |     |     |     |     |     |     | built primarily |     | on Ethereum, |     | which | commonly | involve |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------ | --- | ----- | -------- | ------- |
numberofmaliciousnodesunderwhichtheprotocolcan
|                                |     |     |     |                  |     |     | cryptoassets | such | as ETH, |     | DAI, MKR, |     | AMPL, and |
| ------------------------------ | --- | --- | --- | ---------------- | --- | --- | ------------ | ---- | ------- | --- | --------- | --- | --------- |
| stillprovideforensicevidence,k |     |     |     | theminimumnumber |     |     |              |      |         |     |           |     |           |
SNX.Inthesesystems,asmallsetofwhitelistedoracles
| of honest         | nodes’       | transcripts |         | required     | to reliably | prove      |                  |           |               |           |              |            |            |
| ----------------- | ------------ | ----------- | ------- | ------------ | ----------- | ---------- | ---------------- | --------- | ------------- | --------- | ------------ | ---------- | ---------- |
|                   |              |             |         |              |             |            | provides         | data that | is aggregated |           | to determine |            | on-chain   |
| culpability       | and          | d the       | number  | of Byzantine |             | nodes that |                  |           |               |           |              |            |            |
|                   |              |             |         |              |             |            | prices, making   |           | the system’s  | integrity |              | highly     | dependent  |
| can be held       | accountable  |             | after   | an agreement |             | violation. |                  |           |               |           |              |            |            |
|                   |              |             |         |              |             |            | on a few         | key       | actors.       | Analysis  | of           | real-world | oracle     |
| Analysis          | of protocols |             | such as | PBFT,        | HotStuff,   | VABA,      |                  |           |               |           |              |            |            |
|                   |              |             |         |              |             |            | deployments      | shows     | that          | reported  | prices       | often      | deviate    |
| and Algorand      | shows        | that        | even    | minor        | design      | variations |                  |           |               |           |              |            |            |
|                   |              |             |         |              |             |            | from current     | exchange  |               | rates,    | and          | oracles    | can suffer |
| can significantly |              | affect      | these   | forensic     | parameters. | For        |                  |           |               |           |              |            |            |
|                   |              |             |         |              |             |            | from operational |           | issues        | and       | anomalies.   | A          | comparison |
example,undercertainconfigurations,e.g.PBFT-MAC,
|                |     |           |     |      |                |      | of designs, | including | those | used | by  | MakerDAO | (DAI |
| -------------- | --- | --------- | --- | ---- | -------------- | ---- | ----------- | --------- | ----- | ---- | --- | -------- | ---- |
| HotStuff-null, | and | Algorand, |     | even | if transcripts | from |             |           |       |      |     |          |      |
andMKR),AmpleForth(AMPL),andSynthetix(SNX),
| all honest | nodes        | are available, |               | no meaningful   |           | forensic |                  |           |         |             |          |            |          |
| ---------- | ------------ | -------------- | ------------- | --------------- | --------- | -------- | ---------------- | --------- | ------- | ----------- | -------- | ---------- | -------- |
|            |              |                | =             |                 |           |          | reveals          | that each | employs |             | unique   | mechanisms | for      |
| evidence   | is produced, |                | d             | 0. By examining |           | message  |                  |           |         |             |          |            |          |
|            |              |                |               |                 |           |          | data aggregation |           | and     | validation. | Proposed |            | improve- |
| structures | and quorum   |                | certificates, |                 | the study | outlines |                  |           |         |             |          |            |          |
conditions under which sufficient forensic data can ments include stronger cryptographic binding of data,
|                 |            |          |          |     |             |        | more transparent |     | governance |            | over     | oracle | selection |
| --------------- | ---------- | -------- | -------- | --- | ----------- | ------ | ---------------- | --- | ---------- | ---------- | -------- | ------ | --------- |
| be collected    | to         | reliably | identify |     | adversarial | nodes. |                  |     |            |            |          |        |           |
|                 |            |          |          |     |             |        | and operation,   |     | and robust | mechanisms |          | for    | detecting |
| This systematic |            | approach | enhances |     | the ability | of BFT |                  |     |            |            |          |        |           |
|                 |            |          |          |     |             |        | and mitigating   |     | anomalous  | data,      | ensuring | that   | on-chain  |
| systems         | to recover | from     | faults   | and | strengthens | their  |                  |     |            |            |          |        |           |
protocolsaccuratelyreflectoff-chainreality.
defenseagainstcoordinatedattacks.
| Cryptographic |     | Endorsement |     | for | Secure | Deposits: |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | --- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
•
Another line of research explores how to secure 3) HEURISTICSFORSECOND-LAYER&ON-CHAINEXPLOITS
Bitcoin-based deposits in specialized environments, Second-layernetworks,suchastheLightningNetwork(LN),
suchasconnectedvehicles,automobilesequippedwith enableoff-chaintransactionsandmicro-paymentstoimprove
internet connectivity allowing them to communicate blockchain scalability, but also introduce new vectors for
with other devices both inside and outside the vehicle, misbehavior. The Lightning Network operates by creating
enabling various applications from navigation and payment channels between users, allowing them to conduct
infotainmenttoadvanceddriverassistancesystemsand multiple transactions off the main Bitcoin blockchain. Only
vehicle-to-vehicle communication. A novel ‘‘Bitcoin- the opening and closing of these channels are recorded
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 202605 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
on-chain.However,thisopacityalsopresentschallengesfor using the constant product formula, which governs the
monitoring and security. Table 13 summarizes the studies price impact of trades on AMMs x · y = k where x
coveredinthiscategory. and y represent the reserves of the two tokens in the
liquiditypool,andk isaconstant.Empiricalevaluation
• Lightning Network Analysis: Research in this area shows that a single attacker can achieve an average
focuses both on identifying LN activity from on-chain daily revenue of approximately $3,414 on Uniswap.
dataandanalyzingvulnerabilitieswithintheLNproto- These findings highlight that while the transparency
colitself.Onestudy[148]evaluatesmultipleheuristics of blockchain transactions enables verification and
toidentifytheseLN-relatedtransactionswithintheon- auditability, it also creates vulnerabilities that can be
chaindata.Thisresearchexploreswhatcanbededuced exploited for market manipulation, underscoring the
andinferredaboutthelayer-twooverlaynetworkbased need for improved safeguards in decentralized trading
onthetransactionsrecordedintheledger.Theanalysis systems.
shows that over 75% of all 2-of-2 multisignature In addition, a hybrid detection approach has been
(2of2 multisig) transactions on the Bitcoin using Pay- proposed to identify pump-and-dump (P&D) schemes
to-Witness-Script-Hash (P2WSH) can be linked to on cryptoasset markets [151]. This method combines
LN channels. By correlating observable patterns, e.g. distance- and density-based anomaly metrics to detect
channelopeningandclosing,withknownLNaddresses, sudden, suspicious price–volume movements across
thestudydemonstratesthatitispossibletoinferaspects multiple exchanges. It reformulates the problem of
ofoff-chainactivityfromon-chainrecords,evenifonly contextual anomaly detection in time series data into
partoftheLNtopologyisrevealed. a point anomaly detection problem by dividing the
Complementarywork[149]investigatesroutingvulner- time series into frames, concatenating the data within
abilitiesintheLN.Thefindingsindicatethatadversaries each frame into high-dimensional data points, and
can strategically deploy LN channels with artificially projecting these points into a two-dimensional space
lowfeestoattractpaymentroutes,effectivelyhijacking using Principal Component Analysis (PCA). In this
the network’s routing topology. This tactic allows reduced space, established distance- and density-based
themtoexertundueinfluence,potentiallycensoringor techniques are applied to effectively detect anomalies.
delayingtransactions.Thestudyrevealsafundamental The approach consistently outperforms single-metric
tradeoff:rationalLNnodes,seekingefficient(low-fee) methodsbycapturinganomalouspatternsthatmightbe
routes, become susceptible to exploitation. To mitigate overlookedwhenusingsolelydistance-basedordensity-
this risk and enhance security, nodes must incur based measures, resulting in a higher detection rate of
higher transaction fees to avoid predictable routing P&D events across top-ranked exchange pairs and a
patterns.ThestudyrevealsthatroutinginLNishighly lowerrateoffalsepositivesoverall.
centralized: nearly 60% of all routes pass through At a broader scale, an agent-based study simulates
only five nodes, and 80% through just ten nodes. price manipulation in the Bitcoin market driven by
This concentration exposes the network to denial-of- Tether injections [152]. The simulation models both
service attacks from a small set of colluding entities. typical trader behavior and a fraudulent agent that
Furthermore, the research models an external attacker repeatedly injects Tether on selected exchanges and
establishing new LN links with minimal fees. Results makessustainedBitcoinpurchases.Inmarketswiththin
indicatethatcreatingasfewasfivesuchlinkscandivert liquidity,thesepurchasespushpricesupward,attracting
a majority 65%-75% of network traffic, regardless of additionalmomentum-followingtradersandmagnifying
thespecificLNimplementation.Thecostofdeploying the effect. The malicious agent then strategically sells
theseattacklinksisdemonstrablylow,underscoringthe small volumes of Bitcoin to recoup funds and satisfy
economicfeasibilityofrouting-basedexploitsintheLN. ‘‘proofofcapital’’requirements,typicallyalignedwith
• On-Chain Market Manipulation: On the on-chain end-of-month reporting. The results demonstrate that
side,sophisticatedmanipulationsoccurondecentralized this feedback loop of Tether inflows and controlled
exchanges (DEXs) that rely on transparent smart con- Bitcoin sell-offs can trigger large price swings in an
tracts for trading. High-frequency or so-called ‘‘sand- illiquid market. The study concludes that concentrated
wich’’ attacks on Automated Market Maker (AMM) controloverstablecoinissuance,combinedwithlimited
platforms such as Uniswap is studied [150]. In a sand- liquidity, leaves the Bitcoin ecosystem vulnerable to
wich attack, an adversary exploits the latency between manipulation by a single actor. It also suggests that
transaction broadcast and execution by observing a morefrequentauditsofstablecoinsandeffortstodeepen
pendingtransactioninthemempool,placingabuyorder marketliquiditycouldhelpreducetheriskofsuchprice
immediately before the victim’s order (front-running), inflationschemes.
and then executing a sell order immediately afterward
(back-running) to profit from the induced price move- Heuristic-based anomaly detection methods for cryp-
ment. The study formalizes the attack mathematically toasset transactions excel in interpretability and domain
202606 VOLUME13,2025

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
TABLE13. Heuristic-basedmethods. of these methodologies, summarizing their applications,
performance,andqualitativefeaturesbasedonthe103studies
reviewed.Whileadirectcomparisonofperformancemetrics
|     |     |     |     |     |     |     | is challenging |        | due to    | the lack  | of         | standardized | benchmark |         |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------ | --------- | --------- | ---------- | ------------ | --------- | ------- |
|     |     |     |     |     |     |     | datasets       | across | studies,  | the table | reveals    | clear        | patterns  | that    |
|     |     |     |     |     |     |     | highlight      | the    | strengths | and       | weaknesses |              | inherent  | to each |
approach.
Regardingdatarequirementsandunderlyingassumptions,
|              |          |                         |     |            |      |            | Statistical       | methods     | commonly    |           | assume     | specific      | data      | distri-     |
| ------------ | -------- | ----------------------- | --- | ---------- | ---- | ---------- | ----------------- | ----------- | ----------- | --------- | ---------- | ------------- | --------- | ----------- |
|              |          |                         |     |            |      |            | butions,          | potentially | limiting    |           | their      | effectiveness |           | in volatile |
|              |          |                         |     |            |      |            | cryptoasset       | markets,    |             | as they   | typically  |               | analyze   | numeric     |
|              |          |                         |     |            |      |            | transaction       | metrics     | rather      | than      | the        | underlying    |           | network     |
|              |          |                         |     |            |      |            | structure.        | Network     | Analysis    |           | techniques | primarily     |           | leverage    |
|              |          |                         |     |            |      |            | the transaction   |             | graph’s     | topology, | making     |               | them less | reliant     |
| specificity, | allowing | investigators           |     | to quickly | flag | suspicious |                   |             |             |           |            |               |           |             |
|              |          |                         |     |            |      |            | on distributional |             | assumptions |           | but        | sensitive     | to        | how the     |
| behaviors    | (e.g.,   | short inter-transaction |     | intervals, |      | mixing,    |                   |             |             |           |            |               |           |             |
graphisconstructedandcomputationallyintensiveforlarge
or protocol exploits) without requiring a large training networks. Machine Learning approaches vary substantially
| dataset. Such | heuristics |     | are relatively | straightforward |     | to  |          |       |          |            |     |         |        |         |
| ------------- | ---------- | --- | -------------- | --------------- | --- | --- | -------- | ----- | -------- | ---------- | --- | ------- | ------ | ------- |
|               |            |     |                |                 |     |     | based on | their | subtype: | supervised |     | methods | depend | heavily |
implement, rely on known illicit patterns, and can be tuned on labeled datasets, which are often scarce; unsupervised
to specific network features (like repeated fund-splitting anddeeplearningmodelscircumventlabelinglimitationsbut
| or cross-chain | bridging). |     | However, | they may | fail | to detect |     |     |     |     |     |     |     |     |
| -------------- | ---------- | --- | -------- | -------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
necessitateextensivedatasetsandcarefulfeatureengineering.
complexorevolvinglaunderingstrategiesbeyondthescope Heuristic methods differ from the others by relying on
| of pre-defined | rules, | leading | to  | higher false | negatives | as  |            |         |        |           |     |        |      |           |
| -------------- | ------ | ------- | --- | ------------ | --------- | --- | ---------- | ------- | ------ | --------- | --- | ------ | ---- | --------- |
|                |        |         |     |              |           |     | explicitly | encoded | domain | expertise |     | rather | than | extensive |
criminals adapt. In addition, purely heuristic approaches data. Although data-light, these methods require continual
can be overly rigid, generating potential false positives expertinputtodefineandupdatetheirrules.
| whenever | normal | users | share | superficial | similarities | with |           |           |     |               |     |             |         |     |
| -------- | ------ | ----- | ----- | ----------- | ------------ | ---- | --------- | --------- | --- | ------------- | --- | ----------- | ------- | --- |
|          |        |       |       |             |              |      | Regarding | detection |     | capabilities, |     | Statistical | methods | are |
illicit addresses (e.g., frequent transactions). Nonetheless, particularly effective at identifying point anomalies, such
whenintegratedintoabroaderdetectionpipeline,potentially
|           |         |           |     |                         |     |     | as sudden | numerical |     | deviations |     | in transaction |     | metrics. |
| --------- | ------- | --------- | --- | ----------------------- | --- | --- | --------- | --------- | --- | ---------- | --- | -------------- | --- | -------- |
| employing | machine | learning, |     | address classification, |     | and |           |           |     |            |     |                |     |          |
NetworkAnalysisexcelsatdetectingstructuralandcollective
external intelligence feeds, heuristic triggers can act as the anomalies, like coordinated fraudulent activities or network
‘‘firstlineofdefense,’’rapidlyfilteringoutlargevolumesof
attacksthatleavedistincttopologicaltraces.MachineLearn-
routineactivitywhileflaggingsuspiciousoutliersfordeeper ing methods offer broad capabilities, identifying not only
investigation.Thissynergybetweendomain-drivenheuristics
|               |          |       |      |                  |     |         | point anomalies |     | but also | complex | contextual |     | and | collective |
| ------------- | -------- | ----- | ---- | ---------------- | --- | ------- | --------------- | --- | -------- | ------- | ---------- | --- | --- | ---------- |
| and automated | analysis | tools | thus | offers promising |     | avenues |                 |     |          |         |            |     |     |            |
patterns,evenuncoveringpreviouslyunseenthreatsthrough
for new research, such as refining heuristics to detect novel learnedmodels.Heuristicapproachesarehighlyeffectivefor
| off-chain exploits |     | or designing |     | feedback loops | that | update |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------------ | --- | -------------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
addressingwell-knownvulnerabilitiesorexplicitanomalous
detectionrulesbasedonconfirmedthreatactorbehaviors. patterns,suchasspecificsmartcontractexploits,bydirectly
encodingdomain-specificknowledgeintorules.
IV. CHALLENGES,LIMITATIONS,ANDFUTURERESEARCH Interpretability varies significantly across methodologies.
DIRECTIONS Statistical methods and Heuristic rules typically offer high
ThisSoKhasreviewedacollectionof103paperscenteredon
|     |     |     |     |     |     |     | interpretability |     | due to | their | transparent | logic | and | straight- |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | ----- | ----------- | ----- | --- | --------- |
anomalydetectionwithincryptoassetecosystems,classifying forward analytical frameworks. Network Analysis provides
the employed techniques into four primary categories: moderate interpretability, enabling visual representations
| statistical analysis, |     | network | analysis, | machine | learning, | and |             |       |             |     |          |          |     |         |
| --------------------- | --- | ------- | --------- | ------- | --------- | --- | ----------- | ----- | ----------- | --- | -------- | -------- | --- | ------- |
|                       |     |         |           |         |           |     | of detected | graph | structures; |     | however, | advanced |     | network |
heuristic-based methods, as detailed in Section III. This metricsmaybelessintuitivetointerpret.MachineLearning
| section synthesizes |     | these | findings, | providing | a comparative |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | ----- | --------- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
methodsrangewidely,withsimpleralgorithmsofferingclear
analysisacrossthesecategories.Italsoidentifiessignificant insights into their decision-making processes. In contrast,
overarching challenges prevalent in the field and delineates complex models, particularly deep neural networks, often
| promising | future | research | trajectories | intended |     | to guide |         |            |          |        |     |            |     |          |
| --------- | ------ | -------- | ------------ | -------- | --- | -------- | ------- | ---------- | -------- | ------ | --- | ---------- | --- | -------- |
|           |        |          |              |          |     |          | operate | as ‘‘black | boxes,’’ | posing |     | challenges | for | forensic |
subsequentinvestigationsinthisdynamicdomain. analysis and trust despite their powerful analytical capabil-
ities.
A. COMPARATIVEANALYSISOFDETECTIONCATEGORIES Scalability and computational requirements introduce
After evaluating the four classes of methodology, we found additional trade-offs. Statistical and Heuristic methods
distinct characteristics and trade-offs concerning their data usuallyhavelowcomputationaldemands,makingthemsuit-
requirements, detection capabilities, interpretability, and able for real-time anomaly detection. Conversely, Network
robustness. Table 14 provides a synthesized comparison Analysis methods can become computationally intensive
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 202607 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
TABLE14. Comparisonofanomalydetectionmethodologiesforcryptoassets(numbersinparenthesesindicatethenumberofstudiesinvolved).
due to the complexity of processing large-scale blockchain cross-chain graph alignment will be pivotal for maintaining
transaction graphs. Machine Learning methods, particularly regulatory compliance without compromising user data
deep learning approaches, require significant computational privacy. Despite their interpretability, heuristic methods are
resources during model training, although inference can be brittle and effective for known threats but limited in their
relativelyfastandscalableoncetrained. abilitytogeneralizeandnecessitateongoingmanualupdates
Finally, adaptability and robustness highlight further tomaintaindetectioneffectiveness.
differences. Statistical methods often face challenges in The comparative analysis presented in Table 14 under-
environments with rapid concept drift, which is common scores that no single methodology is universally superior.
in cryptoasset markets and requires frequent recalibration. The optimal choice is context-dependent, balancing the
Network Analysis methods show robustness against certain need for high performance against the practical constraints
noise and small-scale manipulations but remain sensitive of data availability, the demand for robustness against
to substantial topological changes or sophisticated adver- novel threats, and the requirement for interpretability.
sarial attacks. Machine Learning approaches can adapt From a practical standpoint, these trade-offs suggest a
through retraining yet remain susceptible to adversarial stratified deployment strategy, i.e. heuristic rules serve as
attacks specifically designed to evade detection. Expanding an interpretable first line of defense for known threats,
the research horizon further requires integrating cross- while unsupervised learning is essential for spotting novel
disciplinary paradigms, such as causal inference to distin- patterns in label-scarce environments. Conversely, deep
guishintentionalmanipulationfromactualmarketvolatility, learning workflows are best reserved for high-volume,
and reinforcement learning for dynamic monitoring of historical analysis where computational resources and
user behaviors. Additionally, advancing privacy-preserving labeled data are sufficient to support complex model
analyticsthroughtechniqueslikezero-knowledgeproofsand training.
202608 VOLUME13,2025

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
B. REAL-WORLDANOMALIES or historically and indirect analysis of underlying market
Synthesizing the findings from Section III, this section structure, where changes in transaction network topology
connects the surveyed methodologies to their application or simulated agent behaviors signal price instability and
in detecting prominent real-world anomalies. By grounding manipulationrisk.
the taxonomic analysis in concrete use cases, we can better
evaluate the strengths and limitations of current techniques 2) EXCHANGEEXPLOIT:THEMt.GoxCASE
and highlight where certain methods are most effective. AsthedominantBitcoinexchangeuntilits2014collapse,Mt.
The following discussion focuses on several key real-world Goxisacentralcasestudyforexchange-levelmanipulation.
anomalies,evaluatinghowthesurveyedmethodologieshave Analysesoftransactionhistorybetween2011to2013reveal
beenappliedinpracticetodetectthem. that accounts trading at extreme, unrealistic prices formed
dense clusters and unusual motifs (triangles, self-loops).
TemporalSVDshowedtheseabnormalaccountsweretightly
1) MARKETMANIPULATIONANDPRICE-RELATED correlated with Bitcoin price movements, consistent with
ANOMALIES liquidity creation and fake volume [19]. A complementary
P&D and price–trend manipulation are typically executed approachmodelsmonthlytransactionnetworkswithhidden
viacoordinatedburstsinprice–volumeandburstsintrading Markov tensor methods and monitors latent variables using
activity.Oneeffectiveapproachusessignaturemethods[43] MEWMAcontrolcharts.Thisframeworkflagsthelate-2013
totransformrawtradedata—price,volume,side,andtimes- period as ‘‘out-of-control,’’ providing statistical evidence
tampintopowerfulfeatures.ThistechniquecandetectP&D of manipulation without requiring explicit labeling [52].
withF1scoreupto88%,makingithighlycompetitivewith Broader network studies confirm Mt. Gox’s systemic role:
supervisedmethodswhilerelyingonlyonpubliclyavailable structural break analysis shows that after its bankruptcy,
tradehistories.Similarly,forecasting-anomalypipelinesuse heavy-tailed out-degree distributions lost stability, and net-
models like SARIMAX to flag periods where price trends work heterogeneity lost predictive regularity for price. This
deviate significantly from predictions. The highest-volume indicates that Mt. Gox acted as a central hub driving both
accounts active during these anomalous windows are then liquidityandvolatility[74].
flagged as potential manipulators. This approach is highly Together,thesemethodsi.e.graphclassificationwithSVD,
successful, achieving an F1 score of up to 93%. For latent-variable monitoring, and structural break analysis—
DeFi-specific scams like rug pulls, which often combine highlight how different anomaly detection frameworks can
P&D tactics, forensic investigation using open-source tools reconstructandquantifythemanipulationthatcontributedto
like Etherscan and Slither can reconstruct the entire scam Mt.Gox’sdownfall.
lifecycle [144]. This method reveals the common pattern
of token creation, liquidity seeding, orchestrated buys, and 3) MONEYLAUNDERING&TERRORISTFINANCING
eventualliquidityremoval.Thisanalysisalsoshowsthatthe The detection of illicit financial flows is approached by
subsequentmoneylaunderingmethodsareoftenunsophisti- analyzing on-chain data in relation to real-world events
cated.Finally,ahybriddistance-densityframeworkimproves and network behavior. One line of research focuses on
detection by reducing the dimensionality of price-volume terroristfinancing[54]buildsalabeledmapoflargeon-chain
datawithPCA[151].Thisallowsacombinationofdistance- serviceproviders(exchanges,mixers,gambling,mining,dark
and density-based outlier scores to identify abrupt trading markets) and then monitor for abnormal transfer volume
surges with a lower false-positive rate than single-metric around major terrorist attacks. This approach identifies
methods. significant increases in funds flowing into unregulated
On the other hand, price-related anomalies were studied exchangesandmixers,thechannelsusedtomovefundsfrom
by treating unusual price co-movements as market-level organizers to local operatives and to launder them before
anomalies rather than explicit manipulation. A network- cash-out. Forensic accounting on specific events, such as
centric line links transaction-network structure to price e.g. the Sri Lanka Easter bombing, corroborates these findings
principal-componentdynamicsofBitcoin’saddressnetwork and helps build machine learning models that use on-chain
correlatewithmarketregimes[70],andweeklycorrelation- flow features for risk prediction. Practically, a cross-asset
tensor/PCAsnapshotsofXRPtransactionnetworksproduce move like BTC to XRP shows up as funds leaving Bitcoin
singular-value signals that align with subsequent price into known exchange clusters, so the detector keys on the
bursts [76]. A modeling line uses agent-based simulations inflow/outflow bursts to those exchange wallets rather than
to show how concentrated stable-coin inflows (e.g., Tether) theoff-chainconversionstep.
in thin liquidity can amplify price swings consistent with In more general case of money laundering, various
manipulation-drivenbubblesanddrawdowns[152]. machine learning models are applied. A case study of the
These studies show that market manipulation can be Upbithack[84]onEthereumcharacterizesMLnetworksby
detected through two complementary lenses: direct analysis traditional traits such as fast-in/fast-out transfers and dense
of market data where statistical and machine learning transactionclusters,providingconcretefeaturesforon-chain
modelsidentifyanomalousprice-volumepatternsinreal-time detection. On the Bitcoin network [91] (Elliptic dataset),
VOLUME13,2025 202609

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
graphembeddingsareparticularlyeffective,achievesapprox- value, gas, and time to achieve very high recall. The
imately 92% accuracy, though performance can degrade importance of time is also a key theme; models that create
during market disruptions like dark-market shutdowns. The temporal edge embeddings [125], [126] or use pre-trained
performanceofthesemodelscanbeimprovedwithspecial- Transformersonrawtransactionsequencesreportsignificant
izedfeatures[92],[103].Moreadvancedarchitectureslikea performance gains over static graph methods by capturing
temporal-GCN [115] and LB-GLAT [116] explicitly model the behavioral rhythms of phishing attacks, such as fund
transaction sequences and graph directionality to address consolidationandcash-out[127],[128].
challengeslikeover-smoothing,achievinghighaccuracyand The most effective strategy for Ponzi schemes is
F1-scores. pre-deployment analysis of the contract’s bytecode and
A specific challenge within ML is detecting mixing ABI, as these static features provide accurate flags without
services, which are purpose-built to obfuscate fund origins. needingon-chainhistory.Forphishing,thebestresultscome
Research in this area often interacts with mixers to obtain from combining graph structure with temporal data, using
ground-truthdata,whichisthenusedtoidentifytransaction- heterogeneousGNNsontransactionsubgraphsenrichedwith
and chain-level patterns, e.g., I/O structure, sweeper trans- timeandvaluefeatures,oremployingsequencemodelslike
actions [137]. Mixer mechanisms are formalizes as either Transformers. In practice, a two-stage pipeline is effective:
swapping(usingpeelingchains)orobfuscating(usingCoin- (1) pre-deployment screening for Ponzi-like bytecode
Join), with heuristics identifying over 92% of obfuscating patterns, followed by (2) post-deployment monitoring that
transactions [138]. To improve tracing, context-aware taint fuses graph structure with temporal cues to detect phishing
analysis [139] uses address profiling to define logical exit activity.
points (e.g., exchanges, gambling sites), pruning irrelevant
transactionpaths.However,empiricalstudiesshowacontrast
5) CONSENSUSLAYERATTACKS
to these sophisticated tools, revealing that many criminals
A primary concern is the 51% (or majority) attack, where a
use surprisingly unsophisticated laundering methods, often
colludinggroupcouldrewritetransactionhistory.Empirical
preferring direct transfers to centralized exchanges [140],
analysis of Bitcoin and Ethereum shows that mining power
[141].
is increasingly concentrated among a small number of
entities, challenging the assumption of decentralization and
4) PONZISCHEMESANDPHISHING
creating a tangible risk of a 51% attack [153], [154]. This
The detection of user-facing scams like Ponzi schemes
makes continuous monitoring of miner shares and patterns
and phishing relies heavily on machine learning, with
in consecutive block production a critical early-warning
distinctstrategiestailoredtoeachthreat.ForPonzischemes,
system[57],[111].
research focuses on pre-deployment detection by analyzing
Beyond direct majority control, more subtle strategic
the smart contract itself. One approach analyzes contract
deviations like selfish mining (SM) also identified where
artifacts, such as mapping bytecode or Application Binary
miners selectively withhold newly found blocks to gain
Interface (ABI) features into images for CNN and Capsule
an advantage. Detection methods focus on the statistical
Network pipelines, which effectively learn patterns in the
anomaliesthisbehaviorcreates,specificallyinthefrequency
contract’s logic and function calls [93], [95], [98], [132].
of consecutive block discoveries. One approach uses Miner
Acomplementarymethodusesattention-augmentedRNNsto
Sequence Bootstrapping (MSB) [55], a simulation-based
learndirectlyfromn-gramsofbytecodesequences,creating
method, while a more direct statistical test uses the type II
generalizable detectors for Ponzi and related scams [94],
binomialdistributionasanullmodelforhonestmining[56].
[96], [97], [136]. These studies show that a contract’s static
These methods have identified statistically significant SM
code footprint, including opcode frequency and control-
behavior,particularlyinMonacoinandBitcoinCash.
flowstructure,ishighlydiscriminativeforidentifyingPonzi
For selfish-mining, miner and pair run-length tests with
schemesevenbeforeanyusertransactionshaveoccurred.
accurate miner attribution (clustering) are the most direct
Incontrast,phishingdetectionfocusesonpost-deployment
methods and have revealed real-world anomalies. For 51%
analysis of transaction networks, where Graph Neural
attacks, continuous monitoring of pool shares and simple
Networks (GNNs) are the dominant methodology. Early
burst metrics provides actionable risk indicators, while
work established a baseline by creating transaction-aware
generic one-class models offer a lightweight secondary
network embeddings and applying one-class SVMs to
screen.
handle the severe class imbalance between fraudulent and
licit addresses [85], [90]. Current research builds on this
with more advanced GNNs. Studies consistently find that C. MULTI-CHAINANOMALYDETECTION
heterogeneousGNNs,whichexplicitlymodeldifferentnode Whilemostanomaly-detectionworkissingle-chain,anum-
and edge types (e.g., EOA vs. contract, transfer vs. call), berofstudiesextendtheiranalysisacrossmultiplecryptoas-
outperformsimplerarchitectures[105],[107].Othereffective sets. These approaches, often comparative rather than fully
methodsoperateonasubgraph-level[119],[121],analyzing integrated, reveal two crucial insights. First, that ‘‘normal’’
anaddress’slocalneighborhoodwithfeaturesliketransaction on-chain behavior is not uniform across blockchains and
202610 VOLUME13,2025

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
second, that illicit actors increasingly operate across these + parallelism yield practical, near-real-time fraud detection
| differentecosystems. |     |     |     |     |     |     |     | acrossdistinctnetworks[99]. |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
1) COMPARATIVESTRUCTURE&BEHAVIOR
|             |             |     |     |         |          |     |         | 5) CROSS-CHAINANOMALIES |           |       |            |             |     |             |
| ----------- | ----------- | --- | --- | ------- | -------- | --- | ------- | ----------------------- | --------- | ----- | ---------- | ----------- | --- | ----------- |
| Fundamental | differences |     | in  | network | topology | are | evident |                         |           |       |            |             |     |             |
|             |             |     |     |         |          |     |         | Most of                 | the above | treat | each chain | separately, |     | useful, but |
acrossmajorblockchains.Monthlytransactionnetworksfor
|                      |           |      |          |      |         |              |       | insufficient           | for      | cross-ledger | flows.         | A concrete  |         | illustration |
| -------------------- | --------- | ---- | -------- | ---- | ------- | ------------ | ----- | ---------------------- | -------- | ------------ | -------------- | ----------- | ------- | ------------ |
| Bitcoin,             | Ethereum, | and  | Namecoin | all  | exhibit | heavy-tailed |       |                        |          |              |                |             |         |              |
|                      |           |      |          |      |         |              |       | is terrorist-financing |          | related      | activity       | surrounding |         | the Sri      |
| degree distributions |           | that | deviate  | from | simple  | power        | laws, |                        |          |              |                |             |         |              |
|                      |           |      |          |      |         |              |       | Lanka Easter           | attacks: |              | an event-study | on          | Bitcoin | revealed     |
whilenetworkstatisticslikedegreeassortativityrevealunder-
abnormalvolumethroughmixersandunregulatedexchanges
scorestructuraldifferencesbetweenchains[16].Buildingon
|     |     |     |     |     |     |     |     | in the | pre-event | window; | forward | tracing | then | showed |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ------- | ------- | ------- | ---- | ------ |
this,multi-chainanalysesofpreferentialattachmentformal-
|               |                     |            |             |        |           |             |          | conversion           | to Ripple | (XRP)      | and            | continued     | laundering  | on         |
| ------------- | ------------------- | ---------- | ----------- | ------ | --------- | ----------- | -------- | -------------------- | --------- | ---------- | -------------- | ------------- | ----------- | ---------- |
| ize how       | ‘‘rich-get-richer’’ |            | dynamics    |        | drive hub | formation   | in       |                      |           |            |                |               |             |            |
|               |                     |            |             |        |           |             |          | that ledger          | [54].     | This       | case makes     | the           | cross-chain | need       |
| Bitcoin       | and Ethereum        |            | [73], while | ERC-20 |           | token       | networks |                      |           |            |                |               |             |            |
|               |                     |            |             |        |           |             |          | explicit:            | without   | integrated | address/entity |               | linking     | and real-  |
| often exhibit | super-linear        |            | attachment, |        | which     | accelerates | the      |                      |           |            |                |               |             |            |
|               |                     |            |             |        |           |             |          | time exchange/bridge |           |            | coverage,      | sophisticated |             | actors can |
| concentration |                     | of network | activity    | into   | a         | few hubs    | [72].    |                      |           |            |                |               |             |            |
exploitsiloeddetectors.
| This demonstrates |       | that   | a detector | calibrated |        | to one      | chain’s |       |             |             |     |         |               |      |
| ----------------- | ----- | ------ | ---------- | ---------- | ------ | ----------- | ------- | ----- | ----------- | ----------- | --- | ------- | ------------- | ---- |
|                   |       |        |            |            |        |             |         | While | multi-chain | comparative |     | studies | are valuable, | they |
| topology          | would | likely | fail on    | another,   | making | multi-chain |         |       |             |             |     |         |               |      |
areinsufficientfortrackingsophisticatedactorswhoexploit
baseliningessentialforaccuratedetection.
|     |     |     |     |     |     |     |     | the seams | between | ecosystems |     | [155], [156]. |     | The critical |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ---------- | --- | ------------- | --- | ------------ |
openchallengeismovingfromparallel,side-by-sideanalysis
2) MULTI-ASSETIRREGULARITIES
|               |     |             |     |             |     |                |     | to integrated, | entity-centric |     | detection | that | can follow | illicit |
| ------------- | --- | ----------- | --- | ----------- | --- | -------------- | --- | -------------- | -------------- | --- | --------- | ---- | ---------- | ------- |
| Methodologies |     | that screen | for | macro-level |     | irregularities | are |                |                |     |           |      |            |         |
activityasithopsacrosschains,bridges,andexchanges.
| effective              | at flagging |     | anomalous | activity |          | across | multiple |     |     |     |     |     |     |     |
| ---------------------- | ----------- | --- | --------- | -------- | -------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
| assets simultaneously. |             |     | Robust    | distance | metrics, |        | such as  |     |     |     |     |     |     |     |
Mahalanobis distances, can detect anomalies in return D. CHALLENGESANDLIMITATIONS
vectorsacrossmultiplecryptocurrenciessimultaneously[45]. Several critical and interrelated challenges permeate cryp-
These results highlight periods like the 2021 ‘‘metaverse toasset anomaly detection, spanning technical, behavioral,
boom,’’wherecorrelatedsurgesflaggedjoint-marketstress. andregulatorydimensions.
Similarly,Benford’sLawhasbeenusedtoidentifycurrencies First, the scarcity of accurately labeled data constitutes
whose transaction values deviate from expected statistical a fundamental obstacle. Confirmed illicit addresses are
distributions.WhileBitcoinandEthereumconformed,others exceedingly rare relative to legitimate activity, resulting in
suchasTENX,VERI,andDOGEshowedanomalieslinked severeclassimbalance.Thisimbalancesignificantlyimpedes
to documented scandals [44]. Such macro-level methods supervised learning, which depends on high-quality labeled
serveaseffectiveearly-warningsystems,flaggingcross-asset datasets. The inherent pseudonymity of blockchain systems
irregularitiesthatwarrantdeeperon-chaininvestigation. further complicates ground-truth validation. Consequently,
|     |     |     |     |     |     |     |     | researchers | must | explore | semi-supervised, |     | self-supervised, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ------- | ---------------- | --- | ---------------- | --- |
3) MININGBEHAVIORACROSSPoWCHAINS oractive-learningstrategiestoleverageunlabeleddataeffec-
Mining-centric anomalies have been measured consistently tivelyandenhancemodelrobustnessindetectinganomalies.
across BTC, LTC, ETH, BCH, and MONA. The Miner Toalleviatethesedataconstraints,researchersareencouraged
SequenceBootstrapping(MSB)modeltestswhetheraminer to utilize and contribute to community-maintained repos-
appears too often in consecutive blocks relative to chance, itories such as the GraphSense TagPacks [26] and other
flagging selfish strategies; a paired MSB extends to mining curated, publicly documented label sets. Promoting such
cartels[55].Afollow-onstudygeneralizesthetestandreports open benchmarks, alongside rigorous reporting standards,
thatMonacoinshowsanunusuallyhighfractionofabnormal isessentialtoaddresslabelscarcityandensurereproducible
miners, with persistent selfish-mining signals; Bitcoin Cash validationacrossthefield.
also exhibits bursts of abnormality, and cartel-like coordi- Second,scalabilityandreal-timeconstraintsremainpress-
nation is observed in MONA, ETH, BCH more than in ing issues. Blockchain transaction volumes continuously
BTC and LTC [56]. Monitoring miner-share concentration grow, demanding highly efficient algorithms for anomaly
addsacomplementaryperspectiveandearly-warninglensfor detection capable of processing massive data flows at high
51%attack,withempiricalminer-shareprofilesinBTC/ETH velocity. Real-time detection at block-time granularity is
illustratingthepracticalvalueofsuchtracking[57]. essential to prevent financial losses and mitigate ongo-
|     |     |     |     |     |     |     |     | ing threats | like | smart contract | exploits. |     | Achieving | timely, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | -------------- | --------- | --- | --------- | ------- |
4) SCALABLESUPERVISEDPIPELINESACROSSCHAINS accurate anomaly detection with sub-second inference and
On the supervised side, GPU-accelerated pipelines deploy manageablefalse-positiveratesiscomputationallyintensive,
SVM, Random Forest, and Logistic Regression on tens particularlyforadvancedmethodologieslikenetworkanaly-
of millions of Bitcoin transactions and hundreds of thou- sis or complex machine-learning models. Therefore, further
sands of Ethereum accounts, demonstrating that features researchintoscalable,streaminganomaly-detectionmethods
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 202611 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
is crucial. A major practical challenge is the computational like Zcash which employ techniques like zero-knowledge
cost of advanced detection methods and its impact on real- proofs (ZKPs) that offer legitimate users enhanced con-
timefeasibility.Complexmodelslikegraphneuralnetworks fidentiality. This dual-use ambiguity forces detectors to
(GNNs)exemplifythisissue.Thetimecomplexityofasingle distinguish benign privacy-enhanced behavior from mali-
graphconvolutionallayerisoftenO(|E|F′+|V|FF′),where ciouslaundering.Inpractice,evenprivacymechanismsleave
|V| is the number of nodes, |E| is the number of edges, telltale patterns. For example, mixing services often have
andF/F′ aretheinput/outputfeaturedimensions.Forafull characteristic input/output structures or timing signatures;
modelwithmultiplelayers,thiscanscaletoO(Kmd+Knd2) simple heuristics exploiting these can identify over 92% of
whereKisthenumberoflayers,m/nareedges(transactions) CoinJoin-style transactions despite their obfuscation [138].
/nodes (addresses), and d is the feature dimension [157]. Likewise, analyses of privacy-centric blockchains reveal
Giventhatblockchaintransactiongraphscancontainmillions trade-offs: Zcash’s zero-knowledge shielded pool provides
of nodes and hundreds of millions of edges, this cost can anonymity, yet repetitive usage patterns allowed clustering
be prohibitive for real-time model retraining, which is a of 87.5% of addresses and linking a quarter of ‘‘anony-
key reason why achieving sub-second inference at block- mous’’ transactions to known entities (miners, founders),
timegranularityremainsasignificantchallenge[158].While undermining its privacy in practice [80]. These examples
inference is generally faster than training, latency can still highlight that privacy techniques can be partially pierced
bottleneckhigh-frequencyscenarios.Tomitigatethis,many by analytical methods. Similarly, federated learning and
successfulapproachesemploysubgraphsamplingtoconfine secure multi-party computation (MPC) have been proposed
computation to localized neighborhoods. For instance, the to let exchanges or nodes jointly train anomaly detectors
FraudLens framework [124], using graph restructuring, without sharing raw data, aligning with data protection
reported completing its experiment on the entire Elliptic regulations [159], [160]. Such approaches can preserve
dataset in under a minute on a powerful server. To make confidentiality (each party keeps its own dataset) but come
GNNs scalable for even larger graphs like Ethereum’s full with higher complexity and potential performance hits
transaction history, many successful approaches employ (e.g. communication overhead, convergence issues). Thus,
subgraphsamplingstrategies.TheHGATEframework[123], privacy-preserving analytics in blockchain must balance
forexample,avoidsfull-graphtrainingbyextractingsmaller, detectability vs. privacy: stronger privacy tools (mixers,
localized ‘‘micro interaction subgraphs’’ around target encryptedtransactions)makeithardertospotillicitbehavior,
accounts, which enables efficient mini-batch training while while privacy-preserving detection frameworks (differential
still capturing relevant behavioral patterns. This highlights privacy,federatedmodels)safeguarduserdataatthecostof
a crucial trade-off: localized subgraph methods are compu- somesensitivity.Effectivesolutionswilllikelycombinemul-
tationally efficient and can fit on a single GPU, but they tiple techniques, for instance, incorporating privacy-aware
risk missing broader, collective anomalies that are only heuristics into anomaly models, to ensure that legitimate
visible at a global scale. Full-graph analysis provides more privacy is upheld even as illicit abuse of privacy tools is
comprehensive context but at a significant computational aggressivelydetected.
cost. Therefore, real-time deployment feasibility depends Finally, the challenge of cross-chain anomaly detection
on striking a balance. Current research suggests a hybrid is becoming increasingly pertinent. Attacks such as bridge
approach is most practical: using fast, subgraph-based exploits and flash-loan manipulations often leave traces
methods like HGATE for real-time signal generation, while distributed across multiple blockchain ecosystems, compli-
potentiallyrunningmorecomprehensive,full-graphanalyses cating detection due to fragmented and siloed data sources.
asynchronouslytoensurenetwork-widecoverage. Enhancinginteroperabilityanddevelopingdetectionmethods
Third,distinguishingbenignyetprivacy-preservingbehav- capable of integrating multi-chain data streams are urgent
iors from malicious obfuscation requires sophisticated areas for future research, necessary to effectively identify
behavioral modeling and nuanced feature engineering. complexcross-chainanomalies.
Users increasingly adopt non-custodial wallets and other
privacy-focused tools for legitimate reasons, such as ide- E. FUTURERESEARCHDIRECTIONS
ological beliefs or data sovereignty concerns. However, Addressingthesemultifacetedchallengesrequiresconcerted
criminalsfrequentlyexploitthesetoolsduetotheirpseudony- researchacrosstechnical,behavioral,andregulatorydimen-
mous nature and absence of KYC procedures. Effectively sions.Severalpromisingresearchdirectionsemergeclearly.
addressing this ambiguity demands advanced analytical First, developing hybrid methodologies that integrate
techniques that transcend basic transaction metrics and strengths from different detection categories represents a
incorporatebehavioralinsights.Expandingonthechallenge fertile area for future investigation. Graph Neural Net-
ofbehavioralambiguity,thefieldneedsadeeperintegration works (GNNs) combining network topology with machine
of formal privacy-preserving analytics, where the very learning classification exemplify such approaches, merging
tools designed to protect user privacy can hinder anomaly structural insights with data-driven detection capabilities.
detection. Blockchain users increasingly employ mixers, Similarly, rule-augmented machine learning pipelines that
e.g. CoinJoin protocols or Tornado Cash, and privacy coins leverage heuristics to pre-select anomaly candidates for
202612 VOLUME13,2025

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
deeper analyses promise both interpretability and enhanced explorationtoachievetimely,accuratedetectionatthescale
accuracy. Recent work also explores combining diverse andspeedrequiredbycontemporaryblockchainnetworks.
mathematical anomaly indicators using AI techniques like Finally,establishingstandardizedbenchmarksanddatasets
Boltzmann machines to create more robust signals or is essential to enabling fair, consistent comparisons across
integrating predictive AI with facilitation AI within organi- methods. Creating labeled, timestamped datasets covering
zational frameworks like DAOs [161], [162]. Formalizing major cryptoassets and cross-chain interactions, accompa-
design patterns and best practices for these hybrid systems niedbystandardizedevaluationmetricslikeprecision-recall
could streamline development and improve reliability. This curves and time-to-detect metrics, would significantly
susceptibility highlights a critical operational challenge as advance methodological rigor and facilitate cross-study
| attackerscontinuouslyevolvetheirstrategiestobypassstatic |     |           |        |     |            |     |             | comparisons. |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --------- | ------ | --- | ---------- | --- | ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| filters, anomaly                                         |     | detection | models |     | inevitably |     | suffer from |              |     |     |     |     |     |     |     |
driftandperformancedegradation.Consequently,deploying
V. CONCLUSION
| adaptive | retraining | pipelines |     | and continuous |     | drift | detection |        |                 |     |     |             |     |           |      |
| -------- | ---------- | --------- | --- | -------------- | --- | ----- | --------- | ------ | --------------- | --- | --- | ----------- | --- | --------- | ---- |
|          |            |           |     |                |     |       |           | Growth | has transformed |     | the | cryptoasset |     | ecosystem | into |
mechanismsisasimportantastheinitialmodelselectionto
|     |     |     |     |     |     |     |     | a major | financial | market |     | involving | substantial |     | economic |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ------ | --- | --------- | ----------- | --- | -------- |
mitigatetheseadversarialshifts.
|           |          |     |           |     |            |     |            | activity | and a | large | Decentralized |     | Finance | (DeFi) | sector. |
| --------- | -------- | --- | --------- | --- | ---------- | --- | ---------- | -------- | ----- | ----- | ------------- | --- | ------- | ------ | ------- |
| Recently, | emerging |     | paradigms |     | like Graph |     | Foundation |          |       |       |               |     |         |        |         |
Correspondingly,theattacksurfaceforfraud,marketmanip-
| Models (GFMs)      |            | are opening |           | new              | avenues    | in graph-based |             |            |                    |     |            |                |               |       |           |
| ------------------ | ---------- | ----------- | --------- | ---------------- | ---------- | -------------- | ----------- | ---------- | ------------------ | --- | ---------- | -------------- | ------------- | ----- | --------- |
|                    |            |             |           |                  |            |                |             | ulation,   | and protocol-level |     | exploits   |                | has expanded. |       | Globally, |
| anomaly            | detection. | GFMs        | represent |                  | a paradigm |                | shift in    |            |                    |     |            |                |               |       |           |
|                    |            |             |           |                  |            |                |             | regulatory | frameworks         |     | are        | also maturing, | imposing      |       | greater   |
| graph machine      |            | learning.   | Reference |                  | [163]      | proposes       | a large-    |            |                    |     |            |                |               |       |           |
|                    |            |             |           |                  |            |                |             | scrutiny   | and evolving       |     | compliance | demands,       |               | which | includes  |
| scale pre-training |            | framework   |           | on heterogeneous |            |                | transaction |            |                    |     |            |                |               |       |           |
exploringnewconceptsofsecondaryliability[165].
| graphs.          | The results    | show      | that    | GFMs           | can        | be        | fine-tuned  |               |           |                   |             |                 |             |                |             |
| ---------------- | -------------- | --------- | ------- | -------------- | ---------- | --------- | ----------- | ------------- | --------- | ----------------- | ----------- | --------------- | ----------- | -------------- | ----------- |
|                  |                |           |         |                |            |           |             | This          | SoK       | has mapped        |             | 103             | studies     | on cryptoasset |             |
| to various       | tasks,         | including |         | anomaly        | detection, |           | achieving   |               |           |                   |             |                 |             |                |             |
|                  |                |           |         |                |            |           |             | anomaly       | detection | across            | statistical |                 | analysis,   | network        | anal-       |
| strong accuracy  |                | with      | minimal | supervision.   |            | The       | promise     |               |           |                   |             |                 |             |                |             |
|                  |                |           |         |                |            |           |             | ysis, machine |           | learning          | and         | heuristic-based |             | methods.       | The         |
| of emergent      | capabilities,  |           | e.g.,   | in-context     |            | learning, | zero-       |               |           |                   |             |                 |             |                |             |
|                  |                |           |         |                |            |           |             | comparative   | analysis  |                   | reveals     | inherent        | trade-offs: |                | statistical |
| shot generation, |                | and       | task    | homogenization |            | across    | node,       |               |           |                   |             |                 |             |                |             |
|                  |                |           |         |                |            |           |             | analysis      | offers    | interpretability  |             | but             | faces data  | distribution   |             |
| edge, and        | graph          | levels,   | could   | help           | unify      | the       | fragmented  |               |           |                   |             |                 |             |                |             |
|                  |                |           |         |                |            |           |             | sensitivity,  | network   | analysis          |             | leverages       | topology    | effectively    |             |
| landscape        | of graph-based |           | anomaly |                | detection  |           | approaches. |               |           |                   |             |                 |             |                |             |
|                  |                |           |         |                |            |           |             | but struggles |           | with scalability, |             | machine         | learning    |                | provides    |
Buildingonthisconcept,GNN+LLMhybridapproach[164]
|     |     |     |     |     |     |     |     | powerful | pattern | recognition |     | but often | requires | significant |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ----------- | --- | --------- | -------- | ----------- | --- |
fusesblockchaintransactiongraphswithcross-chaintextual
|     |     |     |     |     |     |     |     | labeled | data and | can | lack transparency. |     | At  | the same | time, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | ------------------ | --- | --- | -------- | ----- |
signals.Byleveragingpre-trainedlanguagemodelsalongside
heuristic-basedmethodsexcelwithknownthreatsviaexpert
structuralembeddings,theycaptureanomalieshiddenbothin
|     |     |     |     |     |     |     |     | rules but | fail | against | novel | patterns | and require |     | ongoing |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ------- | ----- | -------- | ----------- | --- | ------- |
graphtopologiesandsemanticpatterns,promisingespecially
|               |            |     |           |          |     |     |             | updates.         | Across | these   | approaches, |          | persistent | challenges |          |
| ------------- | ---------- | --- | --------- | -------- | --- | --- | ----------- | ---------------- | ------ | ------- | ----------- | -------- | ---------- | ---------- | -------- |
| for detecting | fraudulent |     | behaviors | embedded |     | in  | multi-chain |                  |        |         |             |          |            |            |          |
|               |            |     |           |          |     |     |             | hinder progress, |        | notably | the         | scarcity | of labeled |            | data and |
settings.
|         |           |         |     |        |     |                |     | class imbalance, |     | the | computational |     | demands | of  | real-time |
| ------- | --------- | ------- | --- | ------ | --- | -------------- | --- | ---------------- | --- | --- | ------------- | --- | ------- | --- | --------- |
| Second, | advancing | methods |     | robust | to  | label scarcity | and |                  |     |     |               |     |         |     |           |
detectionatscale,theambiguitybetweenprivacytechniques
| severe data | imbalance |     | is critical. | Techniques |     | such | as semi- |     |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ------------ | ---------- | --- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
andmaliciousobfuscation,andthecomplexityofcross-chain
supervised,self-supervised,andtransferlearningcanexploit
activityanalysis.
| unlabeled | or partially |     | labeled | data, | significantly |     | improving |            |     |       |             |            |     |          |         |
| --------- | ------------ | --- | ------- | ----- | ------------- | --- | --------- | ---------- | --- | ----- | ----------- | ---------- | --- | -------- | ------- |
|           |              |     |         |       |               |     |           | Addressing |     | these | significant | challenges |     | suggests | several |
anomalydetectionindata-scarceenvironments.Furthermore,
|           |      |            |             |     |          |     |            | key directions |            | for | future | research.     | Promising |      | directions |
| --------- | ---- | ---------- | ----------- | --- | -------- | --- | ---------- | -------------- | ---------- | --- | ------ | ------------- | --------- | ---- | ---------- |
| synthetic | data | generation | approaches, |     | designed |     | to emulate |                |            |     |        |               |           |      |            |
|           |      |            |             |     |          |     |            | include        | developing |     | hybrid | methodologies |           | like | GNNs or    |
diverselegitimateandillicitbehaviors,couldfurtheralleviate
|     |     |     |     |     |     |     |     | rule-augmented |     | ML, | advancing | techniques |     | robust | to label |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --------- | ---------- | --- | ------ | -------- |
dataconstraintsandfacilitaterigorousmodelevaluation.
|            |            |          |                  |              |              |                  |             | scarcity         | such         | as self-supervised |             |              | learning         | and         | synthetic |
| ---------- | ---------- | -------- | ---------------- | ------------ | ------------ | ---------------- | ----------- | ---------------- | ------------ | ------------------ | ----------- | ------------ | ---------------- | ----------- | --------- |
| Third,     | improving  | the      | interpretability |              |              | of sophisticated |             |                  |              |                    |             |              |                  |             |           |
|            |            |          |                  |              |              |                  |             | data generation, |              | enhancing          |             | model        | interpretability |             | through   |
| machine    | learning   | models   | remains          |              | vital.       | Advanced         | ML          |                  |              |                    |             |              |                  |             |           |
|            |            |          |                  |              |              |                  |             | Explainable      | AI,          | creating           | highly      | scalable     | real-time        |             | systems,  |
| and deep   | learning   | models   | often            | lack         | transparency |                  | despite     |                  |              |                    |             |              |                  |             |           |
|            |            |          |                  |              |              |                  |             | and crucially,   |              | establishing       |             | standardized | benchmarks       |             | and       |
| their high | accuracy.  | Research |                  | should       | prioritize   |                  | Explainable |                  |              |                    |             |              |                  |             |           |
|            |            |          |                  |              |              |                  |             | datasets         | for rigorous |                    | comparison. |              | Advancing        | cryptoasset |           |
| AI (XAI)   | techniques |          | tailored         | specifically |              | for              | cryptoas-   |                  |              |                    |             |              |                  |             |           |
|            |            |          |                  |              |              |                  |             | anomaly          | detection    |                    | is vital    | not merely   | as               | an          | academic  |
set anomaly detection, employing attention mechanisms, exercise but as a crucial requirement for market integrity,
| saliency | mapping, | or  | post-hoc | interpretation |     |     | methods to |                  |     |     |                 |     |             |     |            |
| -------- | -------- | --- | -------- | -------------- | --- | --- | ---------- | ---------------- | --- | --- | --------------- | --- | ----------- | --- | ---------- |
|          |          |     |          |                |     |     |            | user protection, |     | and | the responsible |     | integration |     | of digital |
elucidatethedecision-makingprocessofthesepowerfulyet
|     |     |     |     |     |     |     |     | assets into | the | global | financial | system, | demanding |     | robust, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | --------- | ------- | --------- | --- | ------- |
opaquemodels.
explainable,andadaptivesolutions.
| Fourth,      | developing    | scalable,     |           | real-time       | anomaly      |            | detection  |            |     |     |     |     |     |     |     |
| ------------ | ------------- | ------------- | --------- | --------------- | ------------ | ---------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| systems      | capable       | of processing |           | high-throughput |              |            | blockchain |            |     |     |     |     |     |     |     |
| data streams | is            | paramount.    |           | Techniques      |              | leveraging | online     | REFERENCES |     |     |     |     |     |     |     |
| learning,    | reinforcement |               | learning, |                 | and hardware |            | accelera-  |            |     |     |     |     |     |     |     |
[1] S.Nakamoto,‘‘Bitcoin:Apeer-to-peerelectroniccashsystem,’’White
tion (e.g., GPUs, TPUs, distributed computing) warrant paper,2008.[Online].Available:https://bitcoin.org/bitcoin.pdf
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 202613 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
[2] B.A.Tama,B.J.Kweka,Y.Park,andK.-H.Rhee,‘‘Acriticalreviewof [25] B. Öz, B. Kraner, N. Vallarano, B. S. Kruger, F. Matthes, and
blockchainanditscurrentapplications,’’inProc.Int.Conf.Electr.Eng. C.J.Tessone,‘‘Timemovesfasterwhenthereisnothingyouanticipate:
Comput.Sci.(ICECOS),Aug.2017,pp.109–113. TheroleoftimeinMEVrewards,’’inProc.WorkshopDecentralized
[3] R. Zhang, R. Xue, and L. Liu, ‘‘Security and privacy on FinanceSecur.,Nov.2023,pp.1–8.
blockchain,’’ ACM Comput. Surv., vol. 52, no. 3, pp.1–34, [26] B. Haslhofer, M. Dragaschnig, R. Stutz, M. Romiti, and
Jul.2019. G. Gomez. (May 2022). Graphsense Tagpacks. [Online]. Available:
[4] O. Ali, M. Ally, and Y. Dwivedi, ‘‘The state of play of blockchain https://github.com/graphsense/graphsense-tagpacks
technology in the financial services sector: A systematic [27] A.-L. Barabási, Network Science. Cambridge, U.K.: Cambridge Univ.
literature review,’’ Int. J. Inf. Manage., vol. 54, Oct. 2020, Press,2016.
Art.no.102199. [28] I.Goodfellow,Y.Bengio,andA.Courville,DeepLearning.Cambridge,
[5] M.Javaid,A.Haleem,R.P.Singh,R.Suman,andS.Khan,‘‘Areviewof MA,USA:MITPress,2016.
blockchaintechnologyapplicationsforfinancialservices,’’BenchCouncil [29] S.L.BruntonandJ.N.Kutz,Data-DrivenScienceandEngineering:
Trans.Benchmarks,vol.2,no.3,2022,Art.no.100073. MachineLearning,DynamicalSystems,andControl.Cambridge,U.K.:
[6] A. Babaei, M. Khedmati, M. R. Akbari Jokar, and E. B. Tirkolaee, CambridgeUniv.Press,2019.
‘‘Designing an integrated blockchain-enabled supply chain [30] Z.Wu,S.B.J.Kan,R.D.Lewis,B.J.Wittmann,andF.H.Arnold,
network under uncertainty,’’ Sci. Rep., vol. 13, no. 1, p.3928, ‘‘Machinelearning-assisteddirectedproteinevolutionwithcombinatorial
Mar.2023. libraries,’’Proc.Nat.Acad.Sci.USA,vol.116,no.18,pp.8852–8858,
[7] P.K.Wan,L.Huang,andH.Holtskog,‘‘Blockchain-enabledinformation Apr.2019.
sharing within a supply chain: A systematic literature review,’’ IEEE [31] J. Jumper et al., ‘‘Highly accurate protein structure prediction with
Access,vol.8,pp.49645–49656,2020. AlphaFold,’’Nature,vol.596,no.7873,pp.583–589,Aug.2021.
[8] M.A.N.AgiandA.K.Jha,‘‘Blockchaintechnologyinthesupplychain: [32] M. van Kempen, S. S. Kim, C. Tumescheit, M. Mirdita, J. Lee,
An integrated theoretical perspective of organizational adoption,’’ Int. C. L. M. Gilchrist, J. Söding, and M. Steinegger, ‘‘Fast and accurate
J.Prod.Econ.,vol.247,May2022,Art.no.108458. proteinstructuresearchwithfoldseek,’’NatureBiotechnol.,vol.42,no.2,
[9] S. Shamshad, K. Mahmood, S. Kumari, and C.-M. Chen, ‘‘A secure pp.243–246,Feb.2024.
blockchain-basede-healthrecordsstorageandsharingscheme,’’J.Inf. [33] H. Jeckel, E. Jelli, R. Hartmann, P. K. Singh, R. Mok, J. F. Totz,
Secur.Appl.,vol.55,Dec.2020,Art.no.102590. L. Vidakovic, B. Eckhardt, J. Dunkel, and K. Drescher, ‘‘Learning
[10] A.Dubovitskaya,Z.Xu,S.Ryu,M.Schumacher,andF.Wang,‘‘Secure the space-time phase diagram of bacterial swarm expansion,’’
andtrustableelectronicmedicalrecordssharingusingblockchain,’’in Proc. Nat. Acad. Sci. USA, vol. 116, no. 5, pp.1489–1494,
Proc.AMIAAnnu.Symp.,2018,pp.650–659. Jan.2019.
[11] A.Bogner,M.Chanson,andA.Meeuw,‘‘Adecentralisedsharingapp [34] K. Sankaewtong, J. J. Molina, and R. Yamamoto, ‘‘Autonomous
runningasmartcontractontheEthereumblockchain,’’inProc.6thInt. navigationofsmartmicroswimmersinnon-uniformflowfields,’’Phys.
Conf.InternetThings,Nov.2016,pp.177–178. Fluids,vol.36,no.4,Apr.2024,Art.no.041902.
[12] L.Marchesi,M.Marchesi,R.Tonelli,andM.I.Lunesu,‘‘Ablockchain [35] K.Sankaewtong,J.J.Molina,M.S.Turner,andR.Yamamoto,‘‘Learning
architectureforindustrialapplications,’’Blockchain:Res.Appl.,vol.3, to swim efficiently in a nonuniform flow field,’’ Phys. Rev. E, Stat.
no.4,Dec.2022,Art.no.100088. Phys.PlasmasFluidsRelat.Interdiscip.Top.,vol.107,no.6,Jun.2023,
[13] F.M.DeCollibus,C.Campajola,andC.J.Tessone,‘‘Themicrovelocity Art.no.065102.
ofmoneyinEthereum,’’EPJDataSci.,vol.14,no.1,p.11,Feb.2025. [36] C.V.Amrutha,C.Jyotsna,andJ.Amudha,‘‘Deeplearningapproach
[14] T.Yan,Y.H.Kim,S.Li,T.Kim,andC.J.Tessone,‘‘ApplyingBasel for suspicious activity detection from surveillance video,’’ in Proc.
frameworktoestimatesystemicriskofdecentralizedfinance,’’Available 2nd Int. Conf. Innov. Mech. Ind. Appl. (ICIMIA), Mar. 2020,
atSSRN5234709,2025. pp.335–339.
[15] B. Kraner, L. Pennella, N. Vallarano, and C. J. Tessone, ‘‘Money in [37] B. M. Lake and M. Baroni, ‘‘Human-like systematic generalization
motion:Micro-velocityandusageofEthereumsliquidstakingtokens,’’ through a meta-learning neural network,’’ Nature, vol. 623, no. 7985,
2025,arXiv:2508.15391. pp.115–121,Nov.2023.
[16] J.Liang,L.Li,andD.Zeng,‘‘Evolutionarydynamicsofcryptocurrency [38] G.Aceto,D.Ciuonzo,A.Montieri,andA.Pescape,‘‘Mobileencrypted
transactionnetworks:Anempiricalstudy,’’PLoSONE,vol.13,no.8, traffic classification using deep learning: Experimental evaluation,
Aug.2018,Art.no.e0202202. lessonslearned,andchallenges,’’IEEETrans.Netw.ServiceManage.,
[17] J. Wu, J. Liu, Y. Zhao, and Z. Zheng, ‘‘Analysis of cryptocurrency vol.16,no.2,pp.445–458,Jun.2019.
transactionsfromanetworkperspective:Anoverview,’’J.Netw.Comput. [39] P.Bannigan,Z.Bao,R.J.Hickman,M.Aldeghi,F.Häse,A.Aspuru-
Appl.,vol.190,Sep.2021,Art.no.103139. Guzik,andC.Allen,‘‘Machinelearningmodelstoacceleratethedesign
[18] T. Yan and C. J. Tessone, ‘‘Network analysis of uniswap: Central- ofpolymericlong-actinginjectables,’’NatureCommun.,vol.14,no.1,
ization and fragility in the decentralized exchange market,’’ 2025, p.35,Jan.2023.
arXiv:2503.07834. [40] E. C. L. de Oliveira, K. Santana, L. Josino, A. H. Lima e Lima, and
[19] W.Chen,J.Wu,Z.Zheng,C.Chen,andY.Zhou,‘‘Marketmanipulation C.deSouzadeSalesJúnior,‘‘Predictingcell-penetratingpeptidesusing
of Bitcoin: Evidence from mining the Mt. Gox transaction network,’’ machinelearningalgorithmsandnavigatingintheirchemicalspace,’’Sci.
in Proc. IEEE Conf. Comput. Commun. (INFOCOM), Apr. 2019, Rep.,vol.11,no.1,p.7628,Apr.2021.
pp.964–972. [41] H.Hu,J.Xu,M.Liu,andM.K.Lim,‘‘Vaccinesupplychainmanagement:
[20] T. Gagliardoni. (2021).The Poly Network Hack Explained. Accessed: Anintelligentsystemutilizingblockchain,IoTandmachinelearning,’’
Mar. 7, 2025. [Online]. Available: https://research.kudelskisecurity. J.Bus.Res.,vol.156,Feb.2023,Art.no.113480.
com/2021/08/12/the-poly-network-hack-explained/ [42] A. Devlin, J. Kossen, H. Goldie-Jones, and A. Yang, ‘‘Global green
[21] B.H.A.Khattak,I.Shafi,C.H.Rashid,M.Safran,S.Alfarhood,andI. hydrogen-basedsteelopportunitiessurroundinghighqualityrenewable
Ashraf,‘‘Profitabilitytrendpredictionincryptofinancialmarketsusing energyandironoredeposits,’’NatureCommun.,vol.14,no.1,p.2578,
Fibonacci technical indicator and hybrid CNN model,’’ J. Big Data, May2023.
vol.11,no.1,p.58,Apr.2024. [43] E. Akyildirim, M. Gambara, J. Teichmann, and S. Zhou, ‘‘Appli-
[22] A.A.Monrat,O.Schelén,andK.Andersson,‘‘Asurveyofblockchain cations of signature methods to market anomaly detection,’’ 2022,
from the perspectives of applications, challenges, and opportunities,’’ arXiv:2201.02441.
IEEEAccess,vol.7,pp.117134–117151,2019. [44] J. Vicic and A. Tosic, ‘‘Application of Benford’s law on cryptocur-
[23] D.TapscottandA.Tapscott,BlockchainRevolution:HowtheTechnology rencies,’’ J. Theor. Appl. Electron. Commerce Res., vol. 17, no. 1,
BehindBitcoinisChangingMoney,Business,andtheWorld.Portfolio, pp.313–326,2022.
2016. [45] G. Bae and J. H. Kim, ‘‘Observing cryptocurrencies through robust
[24] M. Bolz, K. Brundler, L. Kane, P. Patsias, L. Tessendorf, K. Gogol, anomalyscores,’’Entropy,vol.24,no.11,p.1643,2022.
T.Kim,andC.Tessone,‘‘Machinelearning-baseddetectionofpump- [46] G.E.P.Box,G.M.Jenkins,G.C.Reinsel,andG.M.Ljung,TimeSeries
and-dumpschemesinreal-time,’’2024,arXiv:2412.18848. Analysis:ForecastingandControl.Hoboken,NJ,USA:Wiley,2015.
202614 VOLUME13,2025

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
[47] F. Akba, I. T. Medeni, M. S. Guzel, and I. Askerzade, ‘‘Manipulator [71] A. Aspembitova, L. Feng, V. Melnikov, and L. Y. Chew, ‘‘Fitness
detection in cryptocurrency markets based on forecasting anomalies,’’ preferential attachment as a driving mechanism in Bitcoin
IEEEAccess,vol.9,pp.108819–108831,2021. transaction network,’’ PLoS ONE, vol. 14, no. 8, pp.1–20,
| [48] J.H.ParkandY.Sohn,‘‘Detectingstructuralchangesinlongitudinal |     |     |     |     | Aug.2019. |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
networkdata,’’BayesianAnal.,vol.15,no.1,pp.133–157,Mar.2020. [72] F.M.DeCollibus,A.Partida,M.Piškorec,andC.J.Tessone,‘‘Het-
[49] D. C. Montgomery, Statistical Quality Control: A Modern Approach. erogeneouspreferentialattachmentinkeyEthereum-basedcryptoassets,’’
FrontiersPhys.,vol.9,Oct.2021,Art.no.720708.
Hoboken,NJ,USA:Wiley,2020.
|                   |       |             |           |                   | [73] D. Kondor, | N. Bulatovic, | J. Stéger, I. Csabai, | and G. Vattay, | ‘‘The |
| ----------------- | ----- | ----------- | --------- | ----------------- | --------------- | ------------- | --------------------- | -------------- | ----- |
| [50] C. A. Lowry, | W. H. | Woodall, C. | W. Champ, | and S. E. Rigdon, |                 |               |                       |                |       |
‘‘Amultivariateexponentiallyweightedmovingaveragecontrolchart,’’ richstillgetricher:Empiricalcomparisonofpreferentialattachmentvia
Technometrics,vol.34,no.1,pp.46–53,Feb.1992. linkingstatisticsinBitcoinandEthereum,’’FrontiersBlockchain,vol.4,
[51] P. D. Hoff, ‘‘Multilinear tensor regression for longitudinal relational Aug.2021,Art.no.668510.
data,’’Ann.Appl.Statist.,vol.9,no.3,pp.1169–1193,Sep.2015. [74] A. Bovet, C. Campajola, F. Mottes, V. Restocchi, N. Vallarano,
[52] K. Sabri-Laghaie, S. Jafarzadeh Ghoushchi, F. Elhambakhsh, and T. Squartini, and C. J. Tessone, ‘‘The evolving liaisons between the
transactionnetworksofBitcoinanditspricedynamics,’’inProc.JPS
| A. Mardani, | ‘‘Monitoring | blockchain | cryptocurrency | transactions |     |     |     |     |     |
| ----------- | ------------ | ---------- | -------------- | ------------ | --- | --- | --- | --- | --- |
Conf.,vol.40,Sep.2023,Paper011002.
| to improve | the trustworthiness |     | of the | fourth industrial |     |     |     |     |     |
| ---------- | ------------------- | --- | ------ | ----------------- | --- | --- | --- | --- | --- |
revolution (Industry 4.0),’’ Algorithms, vol. 13, no. 12, p.312, [75] D.Kondor,I.Csabai,J.Szüle,M.Pósfai,andG.Vattay,‘‘Inferringthe
Nov.2020. interplaybetweennetworkstructureandmarketeffectsinBitcoin,’’New
[53] Y.Faqir-Rhazoui,M.-J.Ariza-Garzón,J.Arroyo,andS.Hassan,‘‘Effect J.Phys.,vol.16,no.12,Dec.2014,Art.no.125003.
ofthegaspricesurgesonuseractivityintheDAOsoftheEthereum [76] A.Chakraborty,T.Hatsuda,andY.Ikeda,‘‘ProjectingXRPpriceburst
blockchain,’’inProc.ExtendedAbstr.CHIConf.Hum.FactorsComput. bycorrelationtensorspectraoftransactionnetworks,’’Sci.Rep.,vol.13,
| Syst.,NewYork,NY,USA,May2021,pp.1–7. |     |     |     |     | no.1,p.4718,Mar.2023. |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- |
[54] D.Amiram,B.N.Jørgensen,andD.Rabetti,‘‘Coinsforbombs:The [77] Y.WangandH.Wang,‘‘Usingnetworksandpartialdifferentialequations
predictiveabilityofon-chaintransfersforterroristattacks,’’J.Accounting toforecastBitcoinpricemovement,’’Chaos:Interdiscipl.J.Nonlinear
Res.,vol.60,no.2,pp.427–466,May2022. Sci.,vol.30,no.7,Jul.2020,Art.no.073127.
[55] S.-N. Li, Z. Yang, and C. J. Tessone, ‘‘Proof-of-work cryptocurrency [78] Z.Wang,R.Zhang,Y.Sun,H.Ding,andQ.Lv,‘‘Canlightningnetwork’s
mining:Astatisticalapproachtofairness,’’inProc.IEEE/CICInt.Conf. autopilotfunctionuseBAmodelastheunderlyingnetwork?’’Frontiers
Commun.China(ICCCWorkshops),Aug.2020,pp.156–161. Phys.,vol.9,Jan.2022,Art.no.794160.
[56] S.-N.Li,C.Campajola,andC.J.Tessone,‘‘Statisticaldetectionofselfish [79] B. Huang, J. Liu, J. Wu, Q. Li, and H. Lin, ‘‘Temporal analysis
mininginproof-of-workblockchainsystems,’’Sci.Rep.,vol.14,no.1, of transaction ego networks with different labels on Ethereum,’’
p.6251,Mar.2024. in Proc. IEEE Int. Symp. Circuits Syst. (ISCAS), May 2022,
[57] F. A. Aponte-Novoa, A. L. S. Orozco, R. Villanueva-Polanco, and pp.3517–3521.
P. Wightman, ‘‘The 51% attack on blockchains: A mining [80] Z. Zhang, W. Li, H. Liu, and J. Liu, ‘‘A refined analysis of
behavior study,’’ IEEE Access, vol. 9, pp.140549–140564, zcash anonymity,’’ IEEE Access, vol. 8, pp.31845–31853,
| 2021. |     |     |     |     | 2020. |     |     |     |     |
| ----- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
[58] M.LischkeandB.Fabian,‘‘AnalyzingtheBitcoinnetwork:Thefirstfour
[81] M.Jourdan,S.Blandin,L.Wynter,andP.Deshpande,‘‘Characterizing
years,’’FutureInternet,vol.8,no.1,p.7,Mar.2016. entitiesintheBitcoinblockchain,’’inProc.IEEEInt.Conf.DataMining
[59] B.Tao,I.W.-H.Ho,andH.-N.Dai,‘‘Complexnetworkanalysisofthe Workshops(ICDMW),Nov.2018,pp.55–62.
Bitcoin blockchain network,’’ in Proc. IEEE Int. Symp. Circuits Syst. [82] Y. Wu, F. Tao, L. Liu, J. Gu, J. Panneerselvam, R. Zhu, and
(ISCAS),May2021,pp.1–5. M.N.Shahzad,‘‘ABitcointransactionnetworkanalyticmethodforfuture
[60] B. Tao, H.-N. Dai, J. Wu, I. W.-H. Ho, Z. Zheng, and C. F. Cheang, blockchainforensicinvestigation,’’IEEETrans.Netw.Sci.Eng.,vol.8,
‘‘ComplexnetworkanalysisoftheBitcointransactionnetwork,’’IEEE no.2,pp.1230–1241,Apr.2021.
| Trans. Circuits | Syst. II, | Exp. Briefs, | vol. 69, no. | 3, pp.1009–1013, |                    |            |                   |               |       |
| --------------- | --------- | ------------ | ------------ | ---------------- | ------------------ | ---------- | ----------------- | ------------- | ----- |
|                 |           |              |              |                  | [83] S. Morishima, | ‘‘Scalable | anomaly detection | in blockchain | using |
Mar.2022. graphics processing unit,’’ Comput. Electr. Eng., vol. 92, Jun. 2021,
[61] V. Chang, K. Hall, Q. A. Xu, L. M. T. Doan, and Z. Wang, ‘‘A Art.no.107087.
social network analysis of two networks: Adolescent school network [84] Q.Fu,D.Lint,Y.Cao,andJ.Wu,‘‘DoesmoneylaunderingonEthereum
and Bitcoin trader network,’’ Decis. Anal. J., vol. 3, Jun. 2022, havetraditionaltraits?’’inProc.IEEEInt.Symp.CircuitsSyst.(ISCAS),
Art.no.100065.
May2023,pp.1–5.
| [62] G. Rosa | and R. Pareschi, | ‘‘Tether: | A study on | bubble-networks,’’ |               |                 |                 |              |          |
| ------------ | ---------------- | --------- | ---------- | ------------------ | ------------- | --------------- | --------------- | ------------ | -------- |
|              |                  |           |            |                    | [85] J. Wang, | P. Chen, X. Xu, | J. Wu, M. Shen, | Q. Xuan, and | X. Yang, |
FrontiersBlockchain,vol.4,Aug.2021,Art.no.686484.
‘‘TSGN:Transactionsubgraphnetworksassistingphishingdetectionin
[63] Z.Di,G.Wang,L.Jia,andZ.Chen,‘‘Bitcointransactionsasagraph,’’ Ethereum,’’2022,arXiv:2208.12938.
IETBlockchain,vol.2,nos.3–4,pp.57–66,Sep.2022. [86] Y. Huang, H. Wang, L. Wu, G. Tyson, X. Luo, R. Zhang, X. Liu,
[64] W.Aiello,F.Chung,andL.Lu,‘‘Arandomgraphmodelforpowerlaw G. Huang, and X. Jiang, ‘‘Characterizing EOSIO blockchain,’’ 2020,
graphs,’’Exp.Math.,vol.10,no.1,pp.53–66,Jan.2001. arXiv:2002.05369.
[65] P.G.BuckleyandD.Osthus,‘‘Popularitybasedrandomgraphmodels [87] Y.Huang,H.Wang,L.Wu,G.Tyson,X.Luo,R.Zhang,X.Liu,G.Huang,
leading to a scale-free degree sequence,’’ Discrete Math., vol. 282, andX.Jiang,‘‘Understanding(Mis)behaviorontheEOSIOblockchain,’’
nos.1–3,pp.53–68,May2004. Proc. ACM Meas. Anal. Comput. Syst., vol. 4, no. 2, pp.1–28,
| [66] D.Lin,J.Wu,Q.Yuan,andZ.Zheng,‘‘Modelingandunderstanding |     |     |     |     | Jun.2020. |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
Ethereumtransactionrecordsviaacomplexnetworkapproach,’’IEEE [88] T. Ashfaq, R. Khalid, A. S. Yahaya, S. Aslam, A. T. Azar, S.
Trans. Circuits Syst. II, Exp. Briefs, vol. 67, no. 11, pp.2737–2741, Alsafari,andI.A.Hameed,‘‘Amachinelearningandblockchainbased
Nov.2020. efficientfrauddetectionmechanism,’’Sensors,vol.22,no.19,p.7162,
| [67] Z.Ao,L.WilliamCong,G.Horvath,andL.Zhang,‘‘Isdecentralized |                |     |                |                      | Sep.2022.       |               |                         |             |     |
| -------------------------------------------------------------- | -------------- | --- | -------------- | -------------------- | --------------- | ------------- | ----------------------- | ----------- | --- |
| finance actually                                               | decentralized? | A   | social network | analysis of the aave |                 |               |                         |             |     |
|                                                                |                |     |                |                      | [89] N. Nayyer, | N. Javaid, M. | Akbar, A. Aldegheishem, | N. Alrajeh, | and |
protocolontheEthereumblockchain,’’2022,arXiv:2206.08401. M.Jamil,‘‘AnewframeworkforfrauddetectioninBitcointransactions
[68] F. M. De Collibus, M. Piškorec, A. Partida, and C. J. Tessone, ‘‘The throughensemblestackingmodelinsmartcities,’’IEEEAccess,vol.11,
structuralroleofsmartcontractsandexchangesinthecentralisationof pp.90916–90938,2023.
Ethereum-basedcryptoassets,’’Entropy,vol.24,no.8,p.1048,Jul.2022. [90] M. Ghosh, D. Ghosh, R. Halder, and J. Chandra, ‘‘Investigating the
[69] A. Alamsyah and I. F. Muhammad, ‘‘Unraveling the crypto market: impact of structural and temporal behaviors in Ethereum phishing
Ajourneyintodecentralizedfinancetransactionnetwork,’’Digit.Bus., users detection,’’ Blockchain: Res. Appl., vol. 4, no. 4, Dec. 2023,
| vol.4,no.1,Jun.2024,Art.no.100074. |     |     |     |     | Art.no.100153. |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
[70] D.Kondor,M.Pósfai,I.Csabai,andG.Vattay,‘‘Dotherichgetricher? [91] Y.Hu,S.Seneviratne,K.Thilakarathna,K.Fukuda,andA.Seneviratne,
AnempiricalanalysisoftheBitcointransactionnetwork,’’PLoSONE, ‘‘CharacterizinganddetectingmoneylaunderingactivitiesontheBitcoin
vol.9,no.2,pp.1–10,Feb.2014. network,’’2019,arXiv:1912.12060.
| VOLUME13,2025 |     |     |     |     |     |     |     |     | 202615 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
[92] C.Oliveira,J.Torres,M.I.Silva,D.Aparício,J.TiagoAscensão,and [113] M. J. Shayegan, H. R. Sabor, M. Uddin, and C.-L. Chen, ‘‘A
P. Bizarro, ‘‘GuiltyWalker: Distance to illicit nodes in the Bitcoin collective anomaly detection technique to detect crypto wallet
network,’’2021,arXiv:2102.05373. frauds on Bitcoin network,’’ Symmetry, vol. 14, no. 2, p.328,
[93] W.Chen,Z.Zheng,J.Cui,E.Ngai,P.Zheng,andY.Zhou,‘‘Detecting Feb.2022.
PonzischemesonEthereum:Towardshealthierblockchaintechnology,’’ [114] J.Wu,Q.Yuan,D.Lin,W.You,W.Chen,C.Chen,andZ.Zheng,‘‘Who
in Proc. World Wide Web Conf. World Wide Web (WWW), 2018, are the phishers? Phishing scam detection on Ethereum via network
pp.1409–1418. embedding,’’ IEEE Trans. Syst., Man, Cybern., Syst., vol. 52, no. 2,
[94] W.Chen,Z.Zheng,E.C.-H.Ngai,P.Zheng,andY.Zhou,‘‘Exploiting pp.1156–1166,Feb.2022.
blockchain data to detect smart Ponzi schemes on Ethereum,’’ IEEE [115] I. Alarab and S. Prakoonwit, ‘‘Graph-based LSTM for anti-money
Access,vol.7,pp.37575–37586,2019. laundering:Experimentingtemporalgraphconvolutionalnetworkwith
[95] G. Ibba, G. A. Pierro, and M. Di Francesco, ‘‘Evaluating machine- Bitcoin data,’’ Neural Process. Lett., vol. 55, no. 1, pp.689–707,
learning techniques for detecting smart Ponzi schemes,’’ in Proc. Feb.2023.
IEEE/ACM 4th Int. Workshop Emerg. Trends Softw. Eng. Blockchain [116] C. Guo, S. Zhang, P. Zhang, M. Alkubati, and J. Song, ‘‘LB-GLAT:
(WETSEB),May2021,pp.34–40. Long-termbi-graphlayerattentionconvolutionalnetworkforanti-money
[96] C. Jin, J. Jin, J. Zhou, J. Wu, and Q. Xuan, ‘‘Heterogeneous launderingintransactionalblockchain,’’Mathematics,vol.11,no.18,
feature augmentation for Ponzi detection in Ethereum,’’ IEEE p.3927,Sep.2023.
Trans. Circuits Syst. II, Exp. Briefs, vol. 69, no. 9, pp.3919–3923, [117] B.Han,Y.Wei,Q.Wang,F.M.D.Collibus,andC.J.Tessone,‘‘MT2AD:
Sep.2022. Multi-layer temporal transaction anomaly detection in Ethereum net-
[97] I. J. Onu, A. E. Omolara, M. Alawida, O. I. Abiodun, and workswithGNN,’’ComplexIntell.Syst.,vol.10,no.1,pp.613–626,
A. Alabdultif, ‘‘Detection of Ponzi scheme on Ethereum using Feb.2024.
machine learning algorithms,’’ Sci. Rep., vol. 13, no. 1, p.18403, [118] W.Wei,Q.Zhang,andL.Liu,‘‘Bitcointransactionforecastingwithdeep
Oct.2023. networkrepresentationlearning,’’IEEETrans.Emerg.TopicsComput.,
[98] K.Toyoda,P.TakisMathiopoulos,andT.Ohtsuki,‘‘Anovelmethodology vol.9,no.3,pp.1359–1371,Jul.2021.
for HYIP Operators’ Bitcoin addresses identification,’’ IEEE Access, [119] S. Hu, Z. Zhang, B. Luo, S. Lu, B. He, and L. Liu, ‘‘BERT4ETH:
vol.7,pp.74835–74848,2019. A pre-trained transformer for Ethereum fraud detection,’’ in
[99] Y.ElmougyandO.Manzi,‘‘AnomalydetectiononBitcoin,Ethereum Proc. ACM Web Conf., New York, NY, USA, Apr. 2023,
networks using GPU-accelerated machine learning methods,’’ in pp.2189–2197.
Proc. 31st Int. Conf. Comput. Theory Appl. (ICCTA), Dec. 2021, [120] A. Song, E. Seo, and H. Kim, ‘‘Anomaly VAE-transformer: A deep
pp.166–171. learningapproachforanomalydetectionindecentralizedfinance,’’IEEE
[100] Y. Elmougy and L. Liu, ‘‘Demystifying fraudulent transactions and Access,vol.11,pp.98115–98131,2023.
illicit nodes in the Bitcoin network for financial forensics,’’ in Proc. [121] H. Kanezashi, T. Suzumura, X. Liu, and T. Hirofuchi, ‘‘Ethereum
29thACMSIGKDDConf.Knowl.DiscoveryDataMining,Aug.2023, fraud detection with heterogeneous graph neural networks,’’ 2022,
pp.3979–3990. arXiv:2203.12363.
[101] R.MittalandM.P.S.Bhatia,‘‘Detectionofsuspiciousorun-trustedusers [122] Z.Liu,D.Yang,S.Wang,andH.Su,‘‘Adaptivemulti-channelBayesian
incrypto-currencyfinancialtradingapplications,’’Int.J.Digit.Crime graphattentionnetworkforIoTtransactionsecurity,’’Digit.Commun.
Forensics,vol.13,no.1,pp.79–93,Jan.2021. Netw.,vol.10,no.3,pp.631–644,Jun.2024.
[102] X. F. Liu, H.-H. Ren, S.-H. Liu, and X.-J. Jiang, ‘‘Characterizing [123] J. Zhou, C. Hu, J. Chi, J. Wu, M. Shen, and Q. Xuan, ‘‘Behavior-
key agents in the cryptocurrency economy through blockchain aware account de-anonymization on Ethereum interaction graph,’’
transaction analysis,’’ EPJ Data Sci., vol. 10, no. 1, p.21, IEEE Trans. Inf. Forensics Security, vol. 17, pp.3433–3448,
May2021. 2022.
[103] J. Liu, C. Yin, H. Wang, X. Wu, D. Lan, L. Zhou, and C. Ge, [124] J. Nicholls, A. Kuppa, and N.-A. Le-Khac, ‘‘FraudLens: Graph
‘‘Graphembedding-basedmoney laundering detectionforEthereum,’’ structural learning for Bitcoin illicit activity identification,’’ in Proc.
Electronics,vol.12,no.14,p.3180,Jul.2023. Annu. Comput. Secur. Appl. Conf., New York, NY, USA, Dec. 2023,
[104] Y.-J. Lin, P.-W. Wu, C.-H. Hsu, I.-P. Tu, and S.-W. Liao, ‘‘An pp.324–336.
evaluationofBitcoinaddressclassificationbasedontransactionhistory [125] A.Xiong,Y.Tong,C.Jiang,S.Guo,S.Shao,J.Huang,W.Wang,and
summarization,’’ in Proc. IEEE Int. Conf. Blockchain Cryptocurrency B. Qi, ‘‘Ethereum phishing detection based on graph neural
(ICBC),May2019,pp.302–310. networks,’’ IET Blockchain, vol. 4, no. 3, pp.226–234,
[105] D.Lin,J.Wu,Q.Yuan,andZ.Zheng,‘‘T-EDGE:TemporalWEighted Sep.2024.
MultiDiGraphembeddingforEthereumtransactionnetworkanalysis,’’ [126] X. Zhou, W. Yang, and X. Tian, ‘‘Detecting phishing accounts on
FrontiersPhys.,vol.8,p.204,Jun.2020. EthereumbasedontransactionrecordsandEGAT,’’Electronics,vol.12,
[106] M. Hasan, M. S. Rahman, H. Janicke, and I. H. Sarker, ‘‘Detecting no.4,p.993,Feb.2023.
anomaliesinblockchaintransactionsusingmachinelearningclassifiers [127] T.Yu,X.Chen,Z.Xu,andJ.Xu,‘‘MP-GCN:Aphishingnodesdetection
and explainability analysis,’’ Blockchain: Res. Appl., vol. 5, no. 3, approach via graph convolution network for Ethereum,’’ Appl. Sci.,
Sep.2024,Art.no.100207. vol.12,no.14,p.7294,Jul.2022.
[107] R. O. Ogundokun, M. O. Arowolo, R. Damaševičius, and S. [128] S.Li,G.Gou,C.Liu,C.Hou,Z.Li,andG.Xiong,‘‘TTAGN:Temporal
Misra, ‘‘Phishing detection in blockchain transaction networks transaction aggregation graph network for Ethereum phishing scams
using ensemble learning,’’ Telecom, vol. 4, no. 2, pp.279–297, detection,’’inProc.ACMWebConf.,NewYork,NY,USA,Apr.2022,
May2023. pp.661–669.
[108] P.M.Monamo,V.Marivate,andB.Twala,‘‘Unsupervisedlearningfor [129] S. Li, J. Zhou, C. Mo, J. Li, G. K. F. Tso, and Y. Tian, ‘‘Motif-
robustBitcoinfrauddetection,’’inProc.Inf.Secur.SouthAfrica(ISSA), awaretemporalGCNforfrauddetectioninsignedcryptocurrencytrust
Aug.2016,pp.129–134. networks,’’2022,arXiv:2211.13123.
[109] T. Pham and S. Lee, ‘‘Anomaly detection in Bitcoin network using [130] V. Patel, L. Pan, and S. Rajasegarar, ‘‘Graph deep learning based
unsupervisedlearningmethods,’’2016,arXiv:1611.03941. anomalydetectioninEthereumblockchainnetwork,’’inNetworkand
[110] T. Pham and S. Lee, ‘‘Anomaly detection in the Bitcoin system—A SystemSecurity,M.Kutyłowski,J.Zhang,andC.Chen,Eds.,Cham,
networkperspective,’’2016,arXiv:1611.03942. Switzerland:Springer,2020,pp.132–148.
[111] S. Sayadi, S. Ben Rejeb, and Z. Choukair, ‘‘Anomaly detection [131] N.Pocher,M.Zichichi,F.Merizzi,M.Z.Shafiq,andS.Ferretti,‘‘Detect-
model over blockchain electronic transactions,’’ in Proc. 15th Int. inganomalouscryptocurrencytransactions:AnAML/CFTapplication
Wireless Commun. Mobile Comput. Conf. (IWCMC), Jun. 2019, ofmachinelearning-basedforensics,’’Electron.Markets,vol.33,no.1,
pp.895–900. p.37,Jul.2023.
[112] D. Chaudhari, R. Agarwal, and S. K. Shukla, ‘‘Towards malicious [132] L.Bian,L.Zhang,K.Zhao,H.Wang,andS.Gong,‘‘Image-basedscam
addressidentificationinBitcoin,’’inProc.IEEEInt.Conf.Blockchain detection method using an attention capsule network,’’ IEEE Access,
(Blockchain),Dec.2021,pp.425–432. vol.9,pp.33654–33665,2021.
202616 VOLUME13,2025

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
[133] A. Dutta, L. C. Voumik, A. Ramamoorthy, S. Ray, and A. Raihan, [155] T.Yan,C.Huang,andC.J.Tessone,‘‘Tracingcross-chaintransactions
‘‘Predicting cryptocurrency fraud using ChaosNet: The Ethereum between EVM-based blockchains: An analysis of Ethereum-polygon
manifestation,’’ J. Risk Financial Manage., vol. 16, no. 4, p.216, bridges,’’2025,arXiv:2504.15449.
Mar.2023. [156] C. Huang, T. Yan, and C. J. Tessone, ‘‘Seamlessly transferring assets
[134] N.Tosunoglu,H.Abaci,G.Ates,andN.S.Akkaya,‘‘Artificialneural through Layer-0 bridges: An empirical analysis of stargate Bridge’s
networkanalysisofthedayoftheweekanomalyincryptocurrencies,’’ architecture and dynamics,’’ in Proc. Companion ACM Web Conf.,
FinancialInnov.,vol.9,no.1,p.88,May2023. May2024,pp.1776–1784.
[135] B. Tao, H.-N. Dai, H. Xie, and F. L. Wang, ‘‘Structural identity [157] Z. Wu, S. Pan, F. Chen, G. Long, C. Zhang, and P. S. Yu,
representation learning for blockchain-enabled metaverse based on ‘‘A comprehensive survey on graph neural networks,’’ IEEE
complexnetworkanalysis,’’IEEETrans.Computat.SocialSyst.,vol.10, Trans. Neural Netw. Learn. Syst., vol. 32, no. 1, pp.4–24,
| no.5,pp.2214–2225,Oct.2023. |     |     |     |     |     |     | Jan.2021. |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
[136] H. Hu, Q. Bai, and Y. Xu, ‘‘SCSGuard: Deep scam detection [158] Z.Chang,Y.Cai,X.F.Liu,Z.Xie,Y.Liu,andQ.Zhan,‘‘Anomalous
for Ethereum smart contracts,’’ in Proc. IEEE IEEE Conf. nodedetectioninblockchainnetworksbasedongraphneuralnetworks,’’
Comput. Commun. Workshops (INFOCOM WKSHPS), May 2022, Sensors,vol.25,no.1,p.1,Dec.2024.
pp.1–6. [159] L. Cui, Y. Qu, G. Xie, D. Zeng, R. Li, S. Shen, and S. Yu,
[137] M.Liu,H.Chen,andJ.Yan,‘‘Detectingrolesofmoneylaunderingin ‘‘Securityandprivacy-enhancedfederatedlearningforanomalydetection
Bitcoinmixingtransactions:Agoalmodelingandminingframework,’’ in IoT infrastructures,’’ IEEE Trans. Ind. Informat., vol. 18, no. 5,
FrontiersPhys.,vol.9,Jul.2021,Art.no.665399. pp.3492–3500,May2022.
[138] A.Shojaeinasab,A.P.Motamed,andB.Bahrak,‘‘Mixingdetectionon [160] X. Wang, W. Liu, H. Lin, J. Hu, K. Kaur, and M. S. Hossain,
Bitcointransactionsusingstatisticalpatterns,’’IETBlockchain,vol.3, ‘‘AI-empowered trajectory anomaly detection for intelligent
no.3,pp.136–148,Sep.2023. transportation systems: A hierarchical federated learning approach,’’
[139] L.Wu,Y.Hu,Y.Zhou,H.Wang,X.Luo,Z.Wang,F.Zhang,andK.Ren, IEEE Trans. Intell. Transp. Syst., vol. 24, no. 4, pp.4631–4640,
| ‘‘TowardsunderstandinganddemystifyingBitcoincmixingservices,’’in |     |     |     |     |     |     | Apr.2023. |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
Proc.WebConf.,Apr.2021,pp.33–44. [161] Y. Ikeda, R. Hadfi, T. Ito, and A. Fujihara, ‘‘Anomaly detection and
[140] T.Tironsakkul,M.Maarek,A.Eross,andM.Just,‘‘Contextmatters: facilitationAItoempowerdecentralizedautonomousorganizationsfor
securecrypto-assettransactions,’’AISoc.,vol.40,no.5,pp.3999–4010,
| Methods                            | for Bitcoin | tracking,’’ | Forensic |     | Sci. Int., | Digit. Invest., |           |     |     |     |     |
| ---------------------------------- | ----------- | ----------- | -------- | --- | ---------- | --------------- | --------- | --- | --- | --- | --- |
| vols.42–43,Oct.2022,Art.no.301475. |             |             |          |     |            |                 | Jan.2025. |     |     |     |     |
[141] M.Nazzari,‘‘Frompaydaytopayoff:Exploringthemoneylaundering [162] Y. Ikeda, H. Aoyama, T. Hatsuda, Y. Hidaka, T. Shirai, W. Souma,
strategies of cybercriminals,’’ in Trends in Organized Crime. Cham, H. Iyetomi, A. Chakraborty, A. Fujihara, Y. Nakayama, Y. Arai,
Switzerland:Springer,Sep.2023. and K. Sankaewtong, ‘‘Verification of elemental technologies for
|          |             |        |        |         |            |          | anomaly | detection | in crypto | asset transactions,’’ | Res. Inst. Econ- |
| -------- | ----------- | ------ | ------ | ------- | ---------- | -------- | ------- | --------- | --------- | --------------------- | ---------------- |
| [142] T. | C. I. Team. | Wizard | Spider | Update: | Resilient, | Reactive |         |           |           |                       |                  |
and Resolute. Accessed: Mar. 26, 2025. [Online]. Available: omy, Trade Ind. (RIETI), Tokyo, Japan, Tech. Rep. 24-E-085,
| https://www.crowdstrike.com/en-us/blog/wizard-spider-adversary- |     |     |     |     |     |     | Dec.2024. |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
update/ [163] J.Liu,C.Yang,Z.Lu,J.Chen,Y.Li,M.Zhang,T.Bai,Y.Fang,L.Sun,
[143] M. ATT&CK. Conti. Accessed: Mar. 26, 2025. [Online]. Available: P.S.Yu,andC.Shi,‘‘Graphfoundationmodels:Concepts,opportunities
andchallenges,’’IEEETrans.PatternAnal.Mach.Intell.,vol.47,no.6,
https://attack.mitre.org/software/S0575/
[144] A. Trozze, T. Davies, and B. Kleinberg, ‘‘Of degens and defrauders: pp.5023–5044,Jun.2025.
Usingopen-sourceinvestigativetoolstoinvestigatedecentralizedfinance [164] J.Su,C.Jiang,X.Jin,Y.Qiao,T.Xiao,H.Ma,R.Wei,Z.Jing,J.Xu,and
fraudsandmoneylaundering,’’ForensicSci.Int.,Digit.Invest.,vol.46, J.Lin,‘‘Largelanguagemodelsforforecastingandanomalydetection:A
Sep.2023,Art.no.301575. systematicliteraturereview,’’2024,arXiv:2402.10350.
[145] P. Sheng, G. Wang, K. Nayak, S. Kannan, and P. Viswanath, ‘‘BFT [165] T.BarbereauandB.Bodó,‘‘Beyondfinancialregulationofcrypto-asset
protocol forensics,’’ in Proc. ACM SIGSAC Conf. Comput. Commun. walletsoftware:Insearchofsecondaryliability,’’Comput.LawSecur.
Secur.,Nov.2021,pp.1722–1743. Rev.,vol.49,Jul.2023,Art.no.105829.
| [146] L. | Li, X. Chang,  | J. Liu, | J. Liu, | and Z.   | Han, ‘‘Bit2CV: | A novel       |     |     |     |     |     |
| -------- | -------------- | ------- | ------- | -------- | -------------- | ------------- | --- | --- | --- | --- | --- |
| Bitcoin  | anti-fraud     | deposit | scheme  | for      | connected      | vehicles,’’   |     |     |     |     |     |
| IEEE     | Trans. Intell. | Transp. | Syst.,  | vol. 22, | no. 7,         | pp.4181–4193, |     |     |     |     |     |
Jul.2021.
[147] B.Liu,P.Szalachowski,andJ.Zhou,‘‘AfirstlookintoDeFioracles,’’
| in  | Proc. IEEE | Int. Conf. | Decentralized | Appl. | Infrastruct. | (DAPPS), |     |     |     |     |     |
| --- | ---------- | ---------- | ------------- | ----- | ------------ | -------- | --- | --- | --- | --- | --- |
Aug.2021,pp.39–48.
[148] M.NowostawskiandJ.Tøn,‘‘Evaluatingmethodsfortheidentification
| of  | off-chain transactions |     | in the lightning | network,’’ |     | Appl. Sci., vol. 9, |     |     |     |     |     |
| --- | ---------------------- | --- | ---------------- | ---------- | --- | ------------------- | --- | --- | --- | --- | --- |
no.12,p.2519,Jun.2019.
| [149] S. | Tochner, S. | Schmid, | and A. Zohar, | ‘‘Hijacking | routes | in payment |     |     |     |     |     |
| -------- | ----------- | ------- | ------------- | ----------- | ------ | ---------- | --- | --- | --- | --- | --- |
channelnetworks:Apredictabilitytradeoff,’’2019,arXiv:1909.06890. KRONGTUM SANKAEWTONG received the
[150] L.Zhou,K.Qin,C.F.Torres,D.V.Le,andA.Gervais,‘‘High-frequency Ph.D. degree in computational physics from
trading on decentralized on-chain exchanges,’’ in Proc. IEEE Symp. NanyangTechnologicalUniversity,Singapore,for
Secur.Privacy(SP),May2021,pp.428–445.
hisworkonthephasetransitionsofsoftcolloidsin
[151] H.Mansourifar,L.Chen,andW.Shi,‘‘Hybridcryptocurrencypumpand
confinement.HeisaPostdoctoralResearchFellow
dumpdetection,’’2020,arXiv:2003.06551.
withtheGraduateSchoolofAdvancedIntegrated
[152] P.Fratrič,G.Sileno,S.Klous,andT.vanEngers,‘‘Manipulationofthe
StudiesinHumanSurvivability,KyotoUniversity.
Bitcoinmarket:Anagent-basedstudy,’’FinancialInnov.,vol.8,no.1, After joining Kyoto University, he began transi-
p.60,Jun.2022.
tioningfromhisdoctoralresearchinsoftmatter
| [153] T. | Yan, S. Li, | B. Kraner, | L. Zhang, | and | C. J. Tessone, | ‘‘A data |     |     |                |                 |                   |
| -------- | ----------- | ---------- | --------- | --- | -------------- | -------- | --- | --- | -------------- | --------------- | ----------------- |
|          |             |            |           |     |                |          |     |     | physics, where | he investigated | the navigation of |
engineeringframeworkforEthereumbeaconchainrewards:Fromdata
smartmicroswimmersbycouplingmachinelearningwithfluiddynamics
collectiontodecentralizationmetrics,’’Sci.Data,vol.12,no.1,p.519,
|     |     |     |     |     |     |     | simulations. | His current | work further | expands on | this interdisciplinary |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ------------ | ---------- | ---------------------- |
Mar.2025.
[154] T.Yan,S.-N.Li,andC.J.Tessone,‘‘AnalysisofEthereum’sblockreward approach, integrating network science, and machine learning to develop
andblockcreationacrossthemerge,’’inProc.IEEEInt.Conf.Blockchain novel techniques for anomaly detection in cryptocurrency transaction
| Cryptocurrency(ICBC),Jun.2025,pp.1–9. |     |     |     |     |     |     | networks. |     |     |     |        |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ------ |
| VOLUME13,2025                         |     |     |     |     |     |     |           |     |     |     | 202617 |

K.Sankaewtongetal.:SoK:AdvancesinAnomalyDetectionTechniquesforCryptoassetTransactions
TAEHOON KIM isaSeniorResearchAssociate YUICHI IKEDA (Member, IEEE) has been a
withtheBlockchainandDLTGroup,Informatics ProfessorofphysicswiththeGraduateSchoolof
Department, University of Zürich (UZH); and Advanced Integrated Studies in Human Surviv-
a member of the UZH Blockchain Center. His ability, Kyoto University, since 2012. Formerly,
researchfocusesoncomplexsystemsandnetwork hewasanAssociateProfessorwiththeUniversity
science to bring a multidisciplinary perspective of Tokyo and a Senior Research Engineer with
that blends blockchain technology and neuroin- HitachiLtd.Healsostudiedcomputationalplasma
formatics. His doctoral research in biosystems physicsatUCBerkeley,in1997,andworkedon
scienceandengineeringfocusedonconnectivity global energy issues at the International Energy
inferencemethodsandgraphicalmodels,includ- Agency, in 2010. Currently, he leads a crypto
inggraphkernelsandgraphneuralnetworks.Withhands-onexperiencewith networkanalysisprojectatRIETI,developinganAI-enhancedDAOsystem
MLsoftwarestacksandcloudsolutions,heisadeptwithhigh-performance foranomalydetectionincryptomarketsusingtechniques,suchasnetwork
computing environments. His work extends to developing web apps science, data science, and machine learning. He created the EDISON-X
(‘‘Thirdview.io’’)usingmodernAIsoftwarestackssincehisinitiationinthe blockchainenergyplatformanddevelopedadecentralizedidentitysystemon
Ethereumecosystem,in2021. XPRL.AsafounderofKyotoUniversityBlockchainCenter,heorganizes
aninternationalconference,BlockchainKaigi(BCK),teachesblockchain
|     |     |     |     | economics, | and mentors students. | He has authored | 128 peer-reviewed      |
| --- | --- | --- | --- | ---------- | --------------------- | --------------- | ---------------------- |
|     |     |     |     | papers, 37 | patent applications,  | and 34 academic | books. He received the |
UBRIConnect2025EducatorAwardfromRipple’sUniversityBlockchain
|     | CLAUDIOJ.TESSONEheadstheBlockchainand |     |     | ResearchInitiative. |     |     |     |
| --- | ------------------------------------- | --- | --- | ------------------- | --- | --- | --- |
DistributedLedgerTechnologiesGroup,Univer-
|     | sity of Zürich      | (UZH). He is also | a Co-Founder   |     |     |     |     |
| --- | ------------------- | ----------------- | -------------- | --- | --- | --- | --- |
|     | and the Chairperson | of the            | UZH Blockchain |     |     |     |     |
Center.Hestudiesblockchainsasaparadigmof
|     | socio-economic | complexity: linking | microscopic |     |     |     |     |
| --- | -------------- | ------------------- | ----------- | --- | --- | --- | --- |
agentbehaviour,incentives(placedonpurposeor
|     | inadvertently), | and interactions | with their emer- |     |     |     |     |
| --- | --------------- | ---------------- | ---------------- | --- | --- | --- | --- |
gentproperties.Themainpillarsofhisresearch
include:consensusanalysisandmodeling(looking
atthequalityofconsensusachievedinreal-worldsituations,theeffectsof
incentives,andinequalityeffectsofrewarddistribution),cryptoeconomics
| (inequality, centralization, | asset circulation, | and hoarding), | large-scale |     |     |     |     |
| ---------------------------- | ------------------ | -------------- | ----------- | --- | --- | --- | --- |
blockchainanalyticsandforensics,anddesignoftoken-basedeconomies.
| 202618 |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | ------------- |