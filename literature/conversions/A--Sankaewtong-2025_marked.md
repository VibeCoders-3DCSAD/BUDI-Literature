---
conversion_metadata:
  converted_at: "2026-09-07T10:08:54Z"
  converter_tool: "markitdown"
  converter_version: "0.1.7"
  source_pdf: "Sankaewtong et al., 2025.pdf"
  source_pdf_sha256: "7d528a064115c861edf227c0e0f07dca3db9115b54f8f7969fc1446d62688b33"
  page_count: 43
  markdown_char_count: 232654
---

<!-- PYPDF FALLBACK ONLY: markitdown/pdfminer timed out on this PDF; extracted via pypdf text() -->

<!-- PAGE 1 -->

Received 26 September 2025, accepted 19 November 2025, date of publication 25 November 2025,
date of current version 4 December 2025.
Digital Object Identifier 10.1 109/ACCESS.2025.3636560
SoK: Advances in Anomaly Detection Techniques
for Cryptoasset Transactions
KRONGTUM SANKAEWTONG
 1, TAEHOON KIM 2, CLAUDIO J. TESSONE
 2,
AND YUICHI IKEDA
 1, (Member, IEEE)
1Graduate School of Advanced Integrated Studies in Human Survivability, Kyoto University, Kyoto 606-8306, Japan
2UZH Blockchain Center, University of Zürich, 8006 Zürich, Switzerland
Corresponding author: Y uichi Ikeda (ikeda.yuichi.2w@kyoto-u.ac.jp)
This work was supported in part by the Ripple Impact Fund, Silicon V alley Community Foundation, under Grant 2022-247584(5855).
ABSTRACT Cryptoasset networks now settle hundreds of billions of dollars each day and underpin a
rapidly expanding DeFi ecosystem. However, their openness exposes them to fraud, market manipulation,
and protocol-level exploits. This Systematization of Knowledge (SoK) maps the state of anomaly detection
in this environment. After outlining blockchain data characteristics and the full threat spectrum, we apply a
reproducible OpenAlex search and multi-stage screening to collect 103 peer-reviewed studies. These works
are organized into four methodological families: statistical analysis, network analysis, machine learning, and
heuristic-based, which we compare across data assumptions, detection scope, interpretability, scalability,
and robustness. Five cross-cutting gaps emerge: label scarcity, adversarial evasion, real-time scalability,
behavioral ambiguity, and multi-chain visibility. We translate these gaps into a research agenda centered on
hybrid graph-neural/heuristic pipelines, drift-aware statistics, explainable deep models, privacy-preserving
analytics, and standardized benchmarks. This SoK provides both a concise snapshot of current techniques
and offers perspectives on securing the next generation of blockchain infrastructure.
INDEX TERMS Anomaly, crypto-asset, graph theory, machine learning.
I. INTRODUCTION
A. BACKGROUND AND MOTIVATION
In 2008, blockchain technology was introduced by Satoshi
Nakamoto as the foundational distributed ledger under-
pinning Bitcoin cryptoasset transactions [1]. This ground-
breaking implementation enabled Bitcoin to address the
longstanding double-spending problem, where the same
digital asset could be spent more than once without relying on
a trusted third-party authority or centralized intermediary [2],
[3]. Blockchain technology achieves trustless verification
through cryptographic techniques, decentralized consensus
protocols (such as proof-of-work and proof-of-stake), and
transparent yet pseudonymous transaction records stored
across numerous network nodes. Due to these attributes,
blockchain rapidly found applications outside of cryptoas-
sets, finding widespread adoption across diverse fields
including finance [4], [5], supply chain management [6],
The associate editor coordinating the review of this manuscript and
approving it for publication was Loris Belcastro
 .
[7], [8], healthcare [9], [10], and decentralized applications
(DApps) [11], [12].
Despite its adoption in various sectors, cryptoasset remains
blockchain’s most prominent and widely recognized appli-
cation. Transaction networks, the graphical representation
of transactions between blockchain addresses or entities,
have emerged as critical analytical tools for understanding
complex patterns and dynamics within cryptoasset ecosys-
tems. These networks offer insights into economic activity,
asset distribution, and user behavior patterns [13], [14],
[15] at a granularity unattainable with traditional financial
monitoring systems [16], [17], [18]. Moreover, analyzing
these transaction networks helps reveal subtle structures and
anomalies that may indicate suspicious or illicit behaviors,
which traditional centralized monitoring mechanisms could
overlook.
However, the intrinsic characteristics of blockchain sys-
tems, such as pseudonymity and decentralization, also create
vulnerabilities exploitable by malicious actors. The cryptoas-
set ecosystem has grown significantly, briefly topping US$3
202576

 2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License.
For more information, see https://creativecommons.org/licenses/by/4.0/ VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
trillion in total capitalization in late 2021 and now handling
well over US$100 billion in daily on-chain value transfer.
Within this large-scale environment, cryptoasset ecosystems
have witnessed a notable rise in fraudulent activities, includ-
ing money laundering, market manipulation, ransomware
payments, and illicit financial transactions involving dark
marketplaces and cybercrimes. Generally, in this context,
an anomaly or anomalous transaction refers to activity
exhibiting characteristics significantly divergent from what
is deemed ‘‘normal,’’ often indicative of aberrant behavior.
Determining anomalous status can depend on contextual
factors and specific transactional or market conditions. Finan-
cial transactions encompass various characteristics, with
anomalies perceived differently depending on the metrics
employed. A transaction flagged as anomalous under one set
of criteria may not meet the same designation under another
framework. Regulatory bodies worldwide are tasked with
scrutinizing these anomalies within financial transactions and
implementing requisite interventions.
Within cryptoassets, these anomalies are commonly cate-
gorized into three main types. Point anomalies are individual
transactions markedly deviating from a typical profile, such
as an unusually large single transfer or a transaction involving
a previously inactive wallet. On the other hand, contextual
anomalies appear anomalous primarily due to their context,
like occurring at unusual times or representing sudden
high-frequency activity from typically inactive accounts.
Finally, collective anomalies include sequences or groups of
transactions that seem suspicious when viewed together, even
if individual transactions appear normal, such as coordinated
pump-and-dump schemes or layering activities used in
money laundering.
High-profile incidents involving cryptoasset exchanges
and decentralized finance (DeFi) platforms, such as the
Mt. Gox Collapse (2014) [19] and the hacks of Poly
Network (2021) [20], serve as stark examples of these
vulnerabilities and the resulting anomalies. Such events have
resulted in losses totaling billions of dollars, undermining
trust and illustrating significant weaknesses in existing
anomaly detection frameworks. Consequently, a growing
urgency and importance is placed on developing robust
anomaly detection systems tailored explicitly for blockchain
transaction networks.
Consequently, a growing urgency and importance is
placed on developing robust anomaly detection systems
tailored explicitly for blockchain transaction networks.
Effective anomaly detection systems help safeguard users
and businesses by detecting illicit activities in near real-time,
thereby maintaining market integrity, enhancing regulatory
compliance, and bolstering overall ecosystem security.
The increased complexity, rapid evolution, and immense
transaction volume within blockchain systems necessitate
innovative detection methodologies. Researchers have thus
explored various techniques ranging from classical statistical
analysis and heuristic-based rules to more sophisticated
machine learning and deep-learning approaches, including
hybrid models for financial trend prediction [21], as well
as network-theoretical analyses explicitly designed for
graph-structured blockchain data [18].
Nevertheless, despite considerable efforts in developing
such techniques, existing literature remains fragmented and
lacks a unified synthesis of knowledge. Different methods
are evaluated under varying assumptions, datasets, and
experimental conditions, making direct comparisons difficult
and highlighting the need for a systematic review. This study
addresses precisely this gap by comprehensively reviewing
existing literature on anomaly detection within blockchain
transaction networks. By systematically classifying and
analyzing existing methods, identifying limitations in current
research, and highlighting open research challenges, we aim
to provide clear guidance for future research directions,
potentially aiding future work on more effective, scalable,
and interpretable anomaly detection systems for blockchain
ecosystems.
B. SCOPE AND CONTRIBUTION
This Systematization of Knowledge (SoK) provides a
comprehensive review and analysis of anomaly detection
techniques specifically targeting cryptoasset transaction net-
works. Our scope centers on analyzing transaction data such
as graphs and time series to identify illicit activities, network
attacks, or protocol misuse, primarily within prominent cryp-
toassets like Bitcoin and Ethereum, while also considering
techniques applicable to other platforms. We deliberately
exclude studies focused solely on market price prediction
without transaction-level analysis or broader blockchain
applications outside the financial/transactional domain, such
as supply chain management. The key contributions of this
work are:
• A systematic literature review identifying and syn-
thesizing critical publications in blockchain anomaly
detection, utilizing a rigorous, reproducible paper selec-
tion process, ensuring comprehensive coverage and
reliability.
• A detailed taxonomy of anomaly detection techniques
employed within blockchain transaction networks,
clearly articulating methodological distinctions and
application contexts.
• A critical analysis highlighting key research gaps,
methodological limitations, and emerging challenges
faced by existing studies in this domain.
• Recommendations for future research directions that
emphasize developing innovative approaches to address
identified limitations, improve detection effectiveness,
scalability, interpretability, and adaptability to diverse
cryptoasset platforms, and integration with new tech-
nologies.
This systematic review aims to guide researchers, prac-
titioners, and policymakers by clarifying state-of-the-art in
cryptoasset anomaly detection and highlighting key areas for
future investigation.
VOLUME 13, 2025 202577

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
FIGURE 1. Distribution of document types among the 1,933 publications
retained after preliminary screening. The vertical axis is shown on a
logarithmic scale.
C. METHODOLOGY
1) PAPER SELECTION PROCESS
To address our research questions on anomaly detection
within the cryptoasset domain, we conducted a systematic
literature search using the OpenAlex database. Our search
string was designed to capture the full breadth of research at
the intersection of anomaly detection, cryptoassets, and graph
analytics. Specifically, we queried OpenAlex with:
(''anomaly detection'' OR anomaly OR anomalies OR
''detection of anomalies'' OR ``fraud detection''
OR forensics OR fraud OR ``money laundering'' OR
''market manipulation'' OR ``transaction network'')
AND (cryptocurrency OR crypto OR ``crypto asset''
OR ``crypto wallet'' OR bitcoin OR ethereum OR XRP
OR Solana OR Tether) AND (graph OR graphs OR
``graph based'' OR ``graph-based'' OR
networks OR network)
This search returned a total of 5,020 publications (as
of as of March 6, 2025). We then applied a multi-stage
screening process as follows. First, we excluded publications
lacking a title, author, abstract, DOI, or indexing, as well
as any duplicates (FC1). Next, we excluded all non-English
publications (FC2). These preliminary filters were imple-
mented to ensure that the final selection included only records
with complete and accurate information suitable for further
analysis. After these steps, 1,933 publications were retained,
spanning various document types, as shown in Fig. 1.
Next, we selected publications categorized as articles,
preprints, or book chapters (FC3). Book chapters were
included because many conference papers are published in
this format. After narrowing these categories, we excluded
review or survey papers (FC4), resulting in 1,438 research
papers, and 215 review/survey papers were removed. By plot-
ting the publication years of these papers as shown in Fig.2,
we observe a notable growth starting in 2009, the year Bitcoin
was introduced. Note that the apparent drop for 2025 is due to
the partial data collected early in that year and does not reflect
a decline in research interest. Consequently, we excluded
FIGURE 2. Distribution of the 1,438 selected research papers by
publication year.
FIGURE 3. Citation count distribution of the 1,438 selected research
papers, The inset provides a closer look at the 0–10 citation range.
papers published prior to 2009 (FC5). Finally, we applied
a minimum citation threshold of three (FC6), based on the
citation distribution illustrated in Fig.3, which yielded a
refined set of 509 publications. Finally, from this pool of
papers, we applied the following criteria to ensure relevance
to our study: a primary focus on blockchain transaction
network analysis, a clearly defined methodology for anomaly
detection, and either an empirical evaluation or a theoretical
foundation (FC7). As a result, we obtained a final set of
103 publications on anomaly detection in cryptoassets. These
publications were examined and compared based on their
methodology, data sources, and reported performance. The
complete selection process is illustrated in Fig.4.
2) CLASSIFICATION FRAMEWORK
We developed a multi-dimensional classification framework
to systematically organize and analyze the diverse body of
research on anomaly detection in cryptoasset transaction
networks. This framework distinguishes between primary
dimensions, which represent fundamental characteristics
202578 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
FIGURE 4. Literature review workflow.
dictating the core nature of the detection approach, and sec-
ondary dimensions, which offer complementary perspectives
for finer-grained analysis. The primary dimensions guiding
our classification are:
• Detection Methodology: This is the cornerstone of
our classification and forms the primary axis for
the detailed review presented in Section III. We cat-
egorize techniques based on their core algorithmic
approach into statistical methods, network analysis
techniques, machine learning approaches (including
supervised, unsupervised, and deep learning), and
heuristic-based strategies. We consider methodology
paramount because it fundamentally shapes the detec-
tion process, dictating data requirements, computational
complexity, interpretability, and the types of anomalies
a technique is best suited to identify. It reflects the core
technical innovations and provides a clear structure for
comparing research contributions.
• Data Sources: Another critical primary dimension
distinguishes whether methods rely on on-chain data
(publicly available on the blockchain ledger), off-chain
data (external sources like market prices, social media,
or proprietary information), or a hybrid combination.
The data source fundamentally limits or enables the
scope of detectable anomalies.
• Application Domain: This dimension classifies studies
based on their intended target area, directly relating
to the types of anomalies (as defined in section I:A)
they aim to detect. For instance, techniques focused on
financial fraud detection might search for specific point
anomalies in transactions or particular patterns of collec-
tive anomalies suggestive of illicit fund flows. Studies
targeting market manipulation analysis often seek
particular collective or contextual anomalies indicative
of artificially influenced market activity. Furthermore,
the domain of network security enhancement typically
involves detecting contextual or collective anomalies
related to protocol misuse or network-level attacks.
Classifying studies by their application domain clarifies
the practical objective of the proposed techniques and
the specific kinds of divergent or aberrant behaviors
they are designed to identify within the blockchain
ecosystem.
While the primary dimensions, particularly methodology,
provide the main structure for this SoK, analyzing the
literature through secondary dimensions offers valuable
additional insights and reveals further nuances:
• Temporal Aspects: Studies can be viewed based on
whether they perform a static analysis on a snapshot
of the network or employ dynamic analysis to capture
temporal evolution and behavioral changes over time.
• Scale of Analysis: Techniques may operate at dif-
ferent granularities, focusing on node-level behavior
(individual addresses/transactions), subgraph patterns
(local neighborhoods or communities), or network-wide
properties.
Nonetheless, while recognizing the value of these multiple
perspectives, this SoK adopts the detection methodology as
the central organizing principle for the in-depth discussion
as it allows for a focused comparison of the core technical
advancements and sets a clear direction for evaluating the
state-of-the-art in cryptoasset anomaly detection.
II. DEFINING AND CHARACTERIZING ANOMALIES IN
BLOCKCHAIN TRANSACTION NETWORKS
A. BLOCKCHAIN AND CRYPTOASSET FUNDAMENTALS
A blockchain is a type of Distributed Ledger Technology
(DLT) that records transactions in a decentralized and
immutable manner. Security is maintained through a chain of
cryptographically linked blocks, where each block contains
transaction data, a timestamp, and a hash of the preceding
block. This structure makes tampering with historical data
computationally infeasible.
Blockchain systems primarily use two transaction models,
as illustrated in Fig.5.
• Unspent Transaction Output (UTXO) model: Used
by Bitcoin, this model tracks discrete chunks of cryp-
toassets. Each transaction consumes existing UTXOs
and generates new ones, providing clear asset traceabil-
ity which is valuable for forensic analysis.
• Account-based model: Used by Ethereum, this model
functions like a bank account, maintaining a balance that
is directly debited or credited. This approach simplifies
state management, especially for applications involving
smart contracts.
Network integrity and agreement on the ledger’s state are
ensured by consensus mechanisms. The two most common
are Proof-of-Work (PoW), which relies on computational
power (mining) to validate transactions, and Proof-of-Stake
VOLUME 13, 2025 202579

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
FIGURE 5. Illustration of the Unspent Transaction Output (UTXO) model (left) and the account-based model (right). On the
left, each transaction consumes specific outputs (e.g., 400 BTC, 500 BTC) and creates new outputs, some of which remain
unspent. On the right, the system tracks account balances, transitioning from one global state (State n+1) to the next (State
n+2, n+3) as transactions occur.
(PoS), where participants stake their own cryptoassets to
secure the network. Both are designed to prevent fraudulent
activities like double-spending. PoS generally consumes
significantly less energy than PoW and can potentially
offer better scalability. However, it also introduces different
security considerations and potential risks, such as the
‘‘nothing at stake’’ problem, though mechanisms exist to
mitigate this.
Transactions on blockchains are pseudonymous, not
anonymous. Users operate via cryptographic addresses,
which are not directly tied to real-world identities. However,
patterns in transaction data can be analyzed to cluster
addresses and potentially de-anonymize users, a key con-
sideration for forensic investigation. Furthermore, platforms
like Ethereum support two distinct account types: Externally
Owned Accounts (EOAs), which are controlled by users
via private keys, and Smart Contract Accounts, which
are governed by their own embedded code. Smart con-
tracts are self-executing programs that enable decentralized
applications (dApps) by automating complex logic. A key
distinction relevant to anomaly detection is that only EOAs
can initiate transactions; smart contracts can only react to
transactions they receive from EOAs or other contracts. This
interaction creates unique on-chain patterns and introduces
vulnerabilities that can be exploited, making smart contract
behavior a significant source of detectable anomalies. For a
more comprehensive overview of blockchain technology, its
architecture, and diverse applications, we refer the interested
reader to foundational reviews [22], [23].
B. COMMON ANOMALIES/ATTACKS
Classifying anomalies into point, contextual, and collective
provides a valuable framework for understanding how
malicious behaviors may manifest in blockchain networks.
However, in practice, many anomalies straddle multiple cat-
egories and target different ecosystem levels, from individual
transactions to consensus mechanisms and smart contracts.
The following part will discuss common anomaly and attack
types, illustrating how they map to the anomaly categories
and how they manifest in real-world scenarios.
1) TRANSACTION-LEVEL FRAUD AND ABUSES
• Double-Spending Attempts (Point/Contextual): This
type of anomaly involves an attacker broadcasting two
conflicting transactions that spend the same coins, aim-
ing to invalidate one transaction after a recipient believes
it is confirmed. Although consensus mechanisms like
PoW or PoS are designed to mitigate such attacks, low
confirmation times or chain reorganizations may allow
double-spending to succeed. In practice, this anomaly
often appears as nearly identical transactions issued in
rapid succession from the same address, frequently with
one transaction replaced by another (e.g., via higher
fees). Successful double spending can lead to direct
financial losses for merchants or service providers that
accept unconfirmed transactions.
• Single Large/Outlier Transfers (Point): Single large
transfers that greatly exceed an address’s historical
transaction sizes often represent point anomalies. They
are particularly suspicious when coming from an
address known for relatively modest activity or when
the receiving address is newly created or previously
inactive. Such outlier transactions may indicate an
exchange hack, insider trading, or liquidation of illicitly
obtained funds. A well-known historical example is the
Mt. Gox hack, where enormous amounts of Bitcoin
were siphoned from the exchange’s hot wallets over
time. Although some of the transfers were not obviously
202580 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
suspicious at first glance, subsequent investigations
revealed a pattern of repeated large outflows that
ultimately contributed to the collapse of the platform.
Because a single outlier can trigger heightened scrutiny,
attackers sometimes break large amounts into smaller,
timed movements to evade detection—highlighting how
anomalies can evolve into more complex patterns when
attackers act repeatedly.
• Phishing/Dusting Attacks (Point): Phishing in the
cryptoasset context can involve unsolicited messages
prompting users to send funds or sign malicious transac-
tions while dusting attacks entail sending trivial ‘‘dust’’
amounts of cryptoasset to numerous addresses. Though
each dust transaction is small, they can reveal wallet
ownership links collectively if recipients consolidate
dust in a single output. These attacks often coincide
with unusual traffic spikes of micro-transactions to
unconnected addresses, marking a contextual anomaly
when viewed against normal transaction profiles. The
initial dust might seem innocuous; however, combining
these minute inputs can help adversaries de-anonymize
users, eventually setting the stage for larger attacks.
2) ILLICIT FINANCIAL ACTIVITIES
• Money-Laundering (Collective): Money laundering
in cryptoassets frequently takes the form of layering,
where funds are passed through multiple addresses or
mixing services to obfuscate their origins. Individual
transactions in a laundering scheme may appear unre-
markable, but collectively, they show repeated splitting,
merging, or identical sums moving in rapid succession.
These multi-hop, near-simultaneous transfers suggest
that a cluster of addresses is cooperating to conceal
the trail. Although on-chain mixers can add further
complexity, certain transaction-flow signatures, like
uniform amounts or synchronized timing, help forensic
analysts flag these collective anomalies.
• Terrorist Financing and Dark-Market Payments
(Contextual/Collective): Illicit financing for extremist
groups or dark-market purchases often entails contextual
anomalies, wherein funds move to or from addresses
known for high-risk activity around specific events.
Isolated transactions might appear normal, but a closer
look at timing, such as spikes in donations during
notable extremist events, can confirm suspicious intent.
In many cases, intelligence from external sources (e.g.,
law-enforcement watchlists, dark-web scraping) reveals
links that are not evident from on-chain data alone.
Thus, these anomalies often require merging blockchain
analysis with off-chain intelligence to achieve reliable
detection.
• Ransomware Payments (Point/Contextual): When
attackers encrypt victims’ data and demand cryptoasset
in return for decryption keys, the resulting ransomware
payments typically present as large, one-off transactions
to an address tied to a known strain of ransomware.
Although each payment might be a point anomaly,
viewing them collectively can also reveal patterns. For
instance, the same address receives repeated payments
from geographically dispersed victims. This dual per-
spective underscores how many anomalies cross the
line between point and collective categories, especially
if attackers systematically reuse addresses or quickly
launder collected funds.
3) MARKET MANIPULATIONS (MM)
• Pump-and-Dump Schemes (Collective): Pump-and-
dump schemes rely on a coordinated group rapidly
buying an illiquid token, driving up the price (the pump),
then selling off their holdings en masse (the dump).
While each purchase or sale alone could resemble nor-
mal trading activity, the collective effect is abrupt price
and volume spikes followed by a dramatic crash. These
schemes often involve off-chain coordination on social
media or messaging platforms, combining an on-chain
collective anomaly with an external organizational
layer [24]. Exchanges or regulators monitoring trade
volume patterns and market sentiment can sometimes
detect these schemes early, although many happen too
quickly for timely intervention.
• Wash Trading (Contextual/Collective): Wash trading
involves the same party (or colluding parties) repeatedly
buying and selling an asset to inflate volume or stabilize
prices. Although each transaction can look typical, the
combined pattern reveals frequent trades between the
same addresses with minimal net movement of funds.
This is especially common in newer token markets
or NFT marketplaces wanting to project artificial
liquidity. If a blockchain records all trades transparently,
analyzing repeated address pairs, cyclical flows, or near-
zero net gains can expose the manipulative nature of
wash trading.
• Front-Running and MEV (Contextual): Front-
running arises when an entity (often a miner, validator,
or specialized bot) reorders transactions in a block
to exploit opportunities such as large swaps on a
decentralized exchange. These reorderings create small
time windows where an attacker can insert a transaction
that profits from price movements [25]. Observing
repeated occurrences of newly inserted transactions just
before large user swaps indicates a contextual anomaly,
which is normal from a transactional standpoint but
suspicious in block order. Miner/validator extractable
value (MEV) can become systemic if left unchecked,
impacting DeFi markets by consistently disadvantaging
ordinary users.
4) NETWORK/CONSENSUS ATTACKS
• 51% Attacks (Collective): Attacks against the consen-
sus layer, such as 51% attacks or selfish mining, are not
strictly transactional anomalies but significantly affect
VOLUME 13, 2025 202581

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
transactions when malicious miners rewrite or withhold
blocks. A sudden concentration of hashing or staking
power can lead to chain reorganizations, invalidating
previously confirmed transactions or enabling double-
spending. In the case of selfish mining, an entity mines
blocks in private and selectively publishes them to the
network to gain disproportionate rewards. Monitoring
block production and correlating it with unusual transac-
tion reversals can expose these anomalies, which often
involve both protocol-level irregularities and suspicious
transaction patterns.
• Selfish Mining or Block Withholding (Contextual):
In selfish mining, a miner (or pool) withholds newly
mined blocks from the public network, secretly building
a private branch of the chain. By selectively releasing
these blocks later, the miner can create reorganizations
that invalidate others’ blocks and claim more rewards.
Block withholding shares similar dynamics; miners
choose not to publish certain blocks, potentially to
collude or manipulate difficulty. These behaviors rep-
resent contextual anomalies because they deviate from
the expected block-discovery pattern; a single withheld
block might seem benign, but repeated withheld or
privately mined blocks can yield persistent advantages.
Over time, such strategies threaten network fairness and
reduce security assurances for honest participants.
5) SMART-CONTRACT VULNERABILITIES
• Reentrancy Attacks (Contextual/Collective): Reen-
trancy vulnerabilities arise when a contract sends funds
(or triggers external calls) before updating its state.
Attackers can exploit this to repeatedly call the same
function (e.g., a withdrawal method) within a single
transaction or block, draining the contract’s balance in
small increments. Although each call may look like
a normal contract interaction, the sequence viewed
collectively reveals an anomalous pattern of repetitive
withdrawals in a very short timeframe. A reentrancy
exploit may begin as a single suspicious call (contextual
anomaly) but often escalates into a chain of exploit calls
that constitute a collective anomaly.
• Integer Overflow/Underflow (Point/Contextual):
Poorly coded smart contracts that do not enforce safe
arithmetic can allow counters or balances to ‘‘wrap
around’’ when they exceed a maximum integer value
(overflow) or drop below zero (underflow). Such
sudden, erratic changes in contract state variables—
like a token balance jumping from near-zero to a huge
number—can stand out as a point anomaly. If multiple
overflow exploits occur rapidly, they may also be viewed
as contextual anomalies. These attacks can quickly
cripple a contract’s logic, enabling unauthorized minting
of tokens or erroneous payouts.
• Ponzi and Pyramid Schemes (Collective): Certain
decentralized applications promise outsized returns
to early participants at the expense of later ones,
TABLE 1. Anomalies listed in public tagpacks.
effectively functioning as Ponzi or pyramid schemes.
Analyzing on-chain flows reveals a systematic pattern
in which initial investors receive payouts drawn entirely
from the capital contributed by newer participants.
Each individual deposit may not look out of place,
but collectively, the scheme exhibits unsustainable
‘‘rewards’’ with minimal legitimate revenue. Detecting
these vulnerabilities involves tracking net inflows and
outflows over time, often requiring address clustering to
identify repeated participants.
6) ADDRESS CLUSTERING
Even though address clustering is not itself a direct attack,
it can have significant security and privacy implications.
By grouping multiple addresses likely controlled by the
same entity, often identified through heuristics such as
co-spending, shared key usage, or overlapping transaction
patterns, investigators and adversaries can deanonymize
users who believed they were pseudonymous. Moreover,
studies of transaction networks frequently reveal centralizing
tendencies despite the underlying blockchain’s decentralized
architecture: influential ‘‘hub’’ addresses (e.g., exchanges,
mixers, or large custodial services) interact with a dispro-
portionately high number of other addresses, effectively
concentrating transaction flow. This hub-and-spoke structure
diminishes the ideal of evenly distributed control, creating
single points of failure or heightened regulatory focus. From
a detection standpoint, clustering can pinpoint suspiciously
large hubs or flows of illicit funds, yet from a privacy
perspective, it can expose user relationships and compromise
anonymity, underscoring how the same network analytics can
be both a valuable investigative tool and a serious privacy
concern.
These anomalies often combine or evolve across multiple
categories, creating what can be termed ‘‘layered complexi-
ties.’’ For instance, a single suspicious transaction may lead
investigators to uncover a larger laundering operation or
a 51% attack can be accompanied by deliberate double-
spending attempts. Similarly, the boundaries between point,
contextual, and collective anomalies can blur: while a
202582 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
TABLE 2. Top 10 cryptoassets involved in anomalies listed in table 1.
reentrancy exploit may first appear as a single abnormal
transaction call, repeated invocations reveal a collective
pattern. Moreover, many incidents underscore the critical role
of off-chain intelligence—such as social-media chatter or
market announcements—in boosting detection accuracy for
manipulative behaviors like pump-and-dump or wash trad-
ing. Consequently, effective monitoring requires combining
on-chain analytics with external context to capture the full
spectrum of illicit activities.
To complement/show the concept of the anomalies dis-
cussed above with the real-world example, we draw on
the GraphSense TagPack [26], an open-source, community-
maintained collection of machine-readable attribution tags.
Each tag links one or more blockchain addresses to a real-
world actor, e.g., an exchange, darknet market, or sanctioned
entity.
Table 1 shows that sextortion and mixing-service activity
dominate in terms of raw address counts despite appearing
in only two and seven cases, respectively. Both anomaly
schemes naturally generate long address chains (victims in
sextortion campaigns, deposit/withdrawal wallets in mixers),
inflating their footprint relative to more concentrated events
such as exchange hacks. Conversely, only a handful of
addresses represent categories like pyramid or phishing,
illustrating the long-tail of niche but still security-critical
threats.
Turning to platform distribution, Table2 shows that Bitcoin
and Ethereum are the main platforms for the anomalies.
Together, they account for 44 of the 61 annotated cases (72%),
making them the primary proving ground for detection
research. The presence of privacy-enhancing chains (Monero,
Zcash) with at least two packs each highlights the growing
forensic interest in assets explicitly designed to obfuscate
flows. The cases listed here highlight the breadth of today’s
threat landscape and foreshadow the twin challenges of
scalability and cross-ledger generalization that motivate the
taxonomy for how anomaly detection methods are organized
and presented next.
C. TAXONOMY OF BLOCKCHAIN TRANSACTION ANOMAL Y
DETECTION TECHNIQUE
To systematically analyze anomaly detection methods
applied to blockchain transaction networks, we propose
a comprehensive taxonomy depicted in Fig.6. This tax-
onomy categorizes existing anomaly detection techniques
into four primary groups based on their core method-
ological approaches: statistical analysis, network analysis,
machine learning, and heuristic-based methods. Each pri-
mary category further comprises subcategories that reflect
specific methodological characteristics, analytical strategies,
or underlying theoretical principles.
Our rationale for selecting these categories is based on
methodological clarity and practical relevance observed in
the existing literature. Statistical methods employ quantita-
tive analysis, anomaly scoring, and probabilistic modeling
to identify deviations from expected transaction patterns.
Network analysis techniques leverage blockchain transaction
graphs’ structural and topological characteristics to identify
anomalous entities or interactions. Machine learning meth-
ods encompass data-driven algorithms that autonomously
learn patterns from historical transaction data, including
supervised, unsupervised, and deep learning frameworks.
Finally, heuristic-based approaches utilize rule-based or
expert-defined models, often integrating analytical models
or cryptographic properties intrinsic to specific blockchain
platforms.
The frequency of research publications across these
categories, shown in Fig.7, indicates clear trends and research
priorities within the cryptoasset anomaly detection literature.
Machine learning methods dominate, accounting for 49 out of
103 analyzed studies, reflecting the increasing emphasis on
adaptive, data-driven techniques capable of handling large-
scale, complex transaction data. Network analysis constitutes
the second-largest group with 30 studies, emphasizing the
importance of graph-based perspectives and the structural
analysis of blockchain transaction relationships. Heuristic-
based approaches, 14 papers, and statistical techniques,
10 studies, while fewer in number, still provide significant
insights, particularly in contexts requiring transparency,
interpretability, or well-defined probabilistic frameworks.
Each primary category is subdivided to reflect specific
methodological details. Within machine learning approaches,
supervised learning methods rely on labeled training data,
making them effective but data-intensive. Unsupervised and
semi-supervised learning approaches address data scarcity by
identifying intrinsic patterns or anomalies without extensive
labeled data. Network analysis methods focus on varying
analytical scales (node-level, subgraph-level, and network-
wide) and consider both static snapshots and dynamic,
evolving blockchain environments. Heuristic-based methods
employ analytical rules derived from expert knowledge or
cryptographic principles, offering transparency and inter-
pretability. At the same time, statistical approaches use
rigorous mathematical frameworks such as distribution-based
anomaly detection, time-series forecasting, and statistical
profiling to quantify transaction anomalies systematically.
While this structured taxonomy aids in clearly under-
standing and organizing existing methods, overlaps and
hybridization among categories exist. For instance, graph
VOLUME 13, 2025 202583

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
FIGURE 6. Taxonomy of anomaly detection techniques.
FIGURE 7. Distribution of the 103 selected research papers across the
categories based on the proposed taxonomy.
neural networks combine machine learning and network-
analytic techniques, indicating evolving interdisciplinary
approaches. Such intersections underscore the dynamic
nature of the field, revealing opportunities for future method-
ological innovation. The subsequent section systematically
explores each category in-depth, comparing methodologies,
highlighting their strengths and limitations, and identifying
key research gaps.
D. CONCEPTS IN STATISTICAL METHODS
Statistical analysis approaches in cryptoasset networks com-
monly center on modeling typical transaction or market
behaviors via probability distributions, time-series analyses,
or multivariate control frameworks. By measuring devia-
tions from these established ‘‘normal’’ baselines—whether
through simple metrics like mean and variance or more
advanced techniques like autoregressive models and tensor-
based analyses—these methods can highlight anomalous
spikes or patterns that suggest fraudulent activity. Crucially,
FIGURE 8. Example of a directed transaction graph among five addresses
(A, B, C, D, E). The edges are weighted by the amount of BTC transferred
from one address to another.
statistical approaches serve as one of the earliest lines of
defense and can be adapted to flag both sudden outliers (point
anomalies) and more nuanced deviations that unfold over
time.
E. TRANSACTION GRAPHS AND NETWORK CONCEPTS
Analyzing cryptoasset transactions through the lens of
network science provides powerful tools for understanding
the flow of value, identifying influential participants, and
detecting anomalous activities. By representing blockchain
data as graphs, we can leverage well-established graph theory
concepts and algorithms to gain insights that might be hidden
when examining individual transactions in isolation.
Cryptoasset transaction networks can be naturally modeled
as graphs. Typically, such graphs are constructed by aggre-
gating transactions occurring within a specific time window,
e.g., hourly, daily, or weekly, to create a snapshot of network
activity. Mathematically, this snapshot is represented as G=
(V, E) where nodes V represent addresses or transactions and
edges E represent relationships or interactions, such as the
transfer of funds. For example, if user A sends x amount of
tokens to user B, to user B, we represent this as a directed edge
202584 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
from node A to node B weighted by x, see Fig.8 for the simple
illustration of the transaction graph. Edges in cryptoasset
graphs are usually directed due to the nature of transactions,
i.e. sender to receiver, and often weighted by transaction value
or frequency. This directed nature allows tracking the flow of
funds clearly from origin to destination.
Several standard graph representations are employed to
analyze blockchain data:
• Transaction Graph: Nodes represent individual trans-
actions, and edges indicate the flow of funds between
transactions.
• User Graphs: Nodes represent blockchain addresses or
users, and edges reflect interactions or transfers between
addresses/users.
• Interaction Graphs: Abstract representation where
nodes can represent entities such as wallets, exchanges,
or contracts, with edges denoting various forms of
interactions.
These graphs are constructed by parsing transaction data
recorded on the blockchain ledger. Each transaction typically
links one or more input addresses to one or more output
addresses.
Several basic graph metrics help characterize transaction
networks:
• Degree (k): Number of edges connected to a node.
For directed graphs, one can distinguish between in-
degree, the number of incoming edges, and out-degree,
the number of outgoing edges. The degrees of node v are
defined as:
kin(v)=
∑
u∈V
euv, kout (v)=
∑
u∈V
evu (1)
where euv is the edge from node u to node v and vice
versa. The degree of node v can be, then, defined as
k(v)= kin(v)+ kout (v)
• Strength: Extends degree by summing edge weights
connected to a node, useful for capturing transaction
volume.
• Clustering Coefficient (C): Measures how closely con-
nected a node’s neighbors are to each other, capturing the
local density of interactions. The clustering coefficient
of node v is defined as:
C(v)= 2T (v)
k(v)(k(v)− 1) (2)
where T (v) represents the number of triangles through
node v.
Centrality measures help identify important nodes within
transaction networks:
• Degree Centrality: Nodes with higher degree centrality
actively participate in more transactions, highlighting
potential hubs.
CD(v)= k(v)
N− 1 (3)
where N is the total number of nodes.
• Closeness Centrality: Indicates how close a node is to
all other nodes, useful for identifying influential nodes
or key intermediaries.
CC (v)= N− 1∑
u∈V d(u, v) (4)
where d(u, v) is the shortest path distance between nodes
u and v.
• Betweenness Centrality: Measures the extent to which
a node lies on paths connecting other nodes, pinpointing
nodes critical for information or value flow.
CB(v)=
∑
s̸=v̸=t∈V
σst (v)
σst
(5)
where σst denotes the total number of shortest paths
between nodes s and node t, and σst (v) is the number
of those paths passing through node v.
Community detection in cryptoasset networks involves
identifying clusters of addresses that exhibit a higher density
of interactions among themselves than with the rest of the
network. By leveraging techniques such as modularity opti-
mization, spectral clustering, or label propagation, analysts
can uncover patterns that suggest coordinated behavior—
be it legitimate operational clusters like exchanges or
suspicious groups potentially involved in fraud or money
laundering. This approach helps to simplify and elucidate
the complex flow of transactions on the blockchain by
highlighting both central hubs and isolated pockets within
the network, thereby providing critical insights for regulatory
compliance and risk management. Despite challenges like
scalability and the inherently dynamic nature of blockchain
data, community detection remains a powerful tool for
discerning the underlying structure of transaction networks
and enhancing the overall understanding of digital currency
ecosystems. For the details on graph theory, refer to [27].
F. MACHINE LEARNING IN A NUTSHELL
Given the widespread adoption of machine learning for
anomaly detection, a dedicated and detailed discussion is
warranted. For a comprehensive theoretical background on
machine-learning algorithms, readers are referred to the well-
established textbooks [28], [29].
Machine learning has progressed rapidly over the past
decade, finding applications at vastly different fields scales,
from microscopic processes such as protein folding [30],
[31], [32] and bacterial swimming behaviors [33], [34], [35],
to human behavioral [36], [37], [38], drug delivery [39], [40]
and onward to enterprise-scale optimizations like supply-
chain logistics and manufacturing workflows [41], [42].
In the context of cryptoasset analysis, machine learning
offers the ability to uncover subtle and adaptive patterns
of fraudulent or malicious behavior by learning from vast
amounts of transaction data, even as illicit tactics evolve.
• Supervised Learning: In supervised ML, models
such as Random Forest or Support V ector Machines
VOLUME 13, 2025 202585

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
(SVMs) are trained on labeled examples of normal
versus anomalous transactions. By ‘‘learning’’ how
known anomalies differ from legitimate activity, these
models can then generalize to flag novel suspicious
cases. However, constructing a reliable labeled dataset,
especially in decentralized cryptoasset settings, can be
challenging due to the scarcity of confirmed fraud labels
and the possibility that malicious actors continuously
change their strategies.
• Unsupervised Learning: Unsupervised approaches
detect anomalies by modeling what ‘‘normal’’ data looks
like, then measuring how strongly each new transaction
deviates from this norm. Clustering techniques like
k-Means or DBSCAN group transactions according to
similarity, labeling data points in low-density regions or
forming their own small clusters as outliers. Likewise,
distance-based methods such as k-Nearest Neighbors
measure each transaction’s distance to its neighbors:
points whose distances surpass typical thresholds are
considered anomalies. Unsupervised methods are par-
ticularly appealing when labeled anomalies are scarce
or non-existent.
• Semi-Supervised Learning: In many real-world
blockchain use cases, only a small subset of transactions
can be confidently labeled, e.g., a handful of confirmed
scam addresses. Semi-supervised algorithms use this
limited information to guide the detection process.
A common tactic is to train a model primarily on normal
data (e.g., one-class SVMs or autoencoders). Hence,
the system learns normal behavior and flags anything
sufficiently different as suspicious. This approach aligns
well with cryptoasset ecosystems, where legitimate
transactions vastly outnumber known fraudulent cases.
• Deep Learning: Neural networks often excel at cap-
turing complex, high-dimensional relationships. Sim-
ple feed-forward networks and Convolutional Neural
Networks (CNNs) can process time-series or transac-
tional features. In contrast, Recurrent Neural Networks
(RNNs) or Long Short-Term Memory (LSTM) networks
handle sequential data such as address activity over
time. A particularly relevant direction involves Graph
Neural Networks (GNNs), which encode both node
(address) attributes and topological information (who
transacts with whom and how often). GNN-based
models can uncover small, densely connected pockets
potentially involved in money laundering or other
collusive behaviors that might elude less graph-aware
methods.
Effective ML-based anomaly detection critically depends
on feature engineering. While raw transaction data such
as addresses, timestamps, and transaction amounts provide
a starting point, additional transformations often boost
performance. Common feature types include:
• Temporal Features: Capturing time-based patterns
like transaction frequency, value changes over time,
or burstiness can reveal deviations from historical
norms.
• Behavioral Profiles: Aggregating typical transaction
sizes, counterparty interactions, or timing for an address
helps identify uncharacteristic activity that might signal
account takeover or illicit use.
• External Signals: Incorporating off-chain data, such as
social media sentiment or market news, can be crucial,
especially for detecting coordinated events like pump-
and-dump schemes.
It is important to note the interplay between ML and
Network Analysis (discussed conceptually in Section II-E).
While our taxonomy presents them as distinct methodolog-
ical families for clarity, insights from network analysis are
often crucial inputs for ML models. Specifically, graph
metrics such as node centrality, clustering coefficients,
or community structure derived from the transaction graph
frequently serve as powerful engineered features for ML
algorithms. This synergy allows ML models to leverage the
structural properties of the transaction network identified
through network analysis techniques.
Beyond the learning paradigms, several algorithm classes
are frequently applied:
• Distance-Based (k-NN): A straightforward yet effec-
tive method is k-Nearest Neighbors, where each trans-
action (represented by its feature vector) is evaluated
against its k closest neighbors. Transactions with anoma-
lously large distances are flagged. While simple to
explain, k-NN can become computationally demanding
in large-scale blockchain applications unless efficient
indexing or approximate methods are employed.
• Clustering Methods (k-Means, DBSCAN): In k-
Means, data points are partitioned into k clusters by
minimizing the distance to each cluster’s centroid.
Transactions far from their nearest centroid or assigned
to extremely small clusters can be considered anoma-
lies. DBSCAN, in contrast, forms clusters based on
density—points in sparsely populated regions are auto-
matically deemed outliers. This density-driven approach
can help reveal groups of addresses interacting in a
suspiciously tight circle, unconnected to the rest of the
network.
• Tree-Based Models:
-- Isolation Forest: isolates data points by randomly
splitting features; anomalies tend to be split from the
rest of the data more quickly, thus receiving higher
anomaly scores.
-- Random Forest: typically a supervised classifier,
can also provide outlier scores based on how consis-
tently a transaction is classified compared to others.
In labeled settings, such as a training set of flagged
addresses, Random Forest can be used directly to
classify transactions as normal or anomalous.
• Neural Networks Approaches:
202586 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
-- Feed-forward NNs: learn to map input features, e.g.,
transaction size, frequency, node attributes, to a score
or label indicating anomaly likelihood.
-- Graph Neural Networks (GNNs): such as Graph
Convolutional Networks (GCNs) or Graph Attention
Networks (GA Ts) capture the relational structure
among addresses. By iteratively combining informa-
tion from neighbors, GNNs detect anomalies that
might appear only when viewed within the broader
transaction subgraph.
G. EVALUATION METRICS FOR ANOMAL Y DETECTION
Anomaly detection in cryptoasset networks typically involves
identifying rare, illicit, or otherwise suspicious transactions
within a much larger pool of benign activity. This setting
poses unique challenges for model evaluation, as standard
metrics may not accurately reflect performance under high
class imbalance. The following subsections discuss common
metrics and highlight how curve-based analyses can provide
deeper insights into a detector’s effectiveness.
In most real-world datasets, anomalies constitute only a
small fraction of total transactions. For instance, malicious
addresses or fraudulent trades may make up far less than 1%
of on-chain activity. Such class imbalance can undermine
naive metrics—especially accuracy—by rewarding models
that favor classifying the majority of instances as ‘‘nor-
mal.’’ Consequently, an anomaly detector might achieve
deceptively high accuracy while scarcely flagging any actual
anomalies. This imbalance also complicates the training pro-
cess: many machine-learning algorithms assume relatively
balanced classes, and their performance or convergence can
degrade when one class overwhelmingly dominates the other.
Confusion Matrix (TP, TN, FP, FN): A confusion matrix
provides a granular look at a detector’s outcomes. Here,
True Positives (TP) are correctly identified anomalies, True
Negatives (TN) are correctly identified normal transactions,
False Positives (FP) are normal transactions misclassified as
anomalies and False Negatives (FN) are missed anomalies.
The following are matrices that are based on the confusion
matrix.
• Accuracy:
Accuracy= TP+ TN
TP+ TN+ FP+ FN (6)
Although accuracy is the most commonly reported
metric, it can be misleading in imbalanced scenarios.
If anomalies represent only 1% of transactions, a naive
detector that flags everything as normal could achieve
99% accuracy, despite failing to detect any suspicious
activity.
• Precision: indicates the proportion of flagged anomalies
that are truly anomalous, highlighting how well a
detector avoids raising false alarms.
Precition= TP
TP+ FP (7)
• Recall: indicates the proportion of flagged anomalies
that are truly anomalous, highlighting how well a
detector avoids raising false alarms.
Recall= TP
TP+ FN (8)
• F1-Score: indicates the proportion of flagged anomalies
that are truly anomalous, highlighting how well a
detector avoids raising false alarms.
F1= 2× Precision× Recall
Precision+ Recall (9)
The other widely used metrics for evaluating detection
performance are curve-based, offering a more holistic view
of how a classifier’s performance changes under varying
decision thresholds. A Receiver Operating Characteristic
(ROC) curve plots the true positive rate (recall) against the
false positive rate (1 - specificity), and the Area Under the
ROC Curve (AUC-ROC) summarizes this overall trade-off.
V alues closer to 1.0 indicate better discrimination ability.
However, when the number of negative (normal) instances
vastly outweighs the positives (anomalies), the ROC curve
can yield an overly optimistic picture.
To address this limitation, many anomaly-detection studies
employ the Precision-Recall (PR) curve and calculate the
Area Under the Precision-Recall Curve (AUC-PR). The PR
curve directly focuses on precision and recall over various
thresholds, making it more informative in heavily imbalanced
contexts. Unlike the ROC curve, which plots all positive and
negative samples equally, a PR curve highlights how well the
detector maintains high precision (i.e., keeps false positives
low) at different levels of recall (i.e., detects a large fraction
of actual anomalies). In scenarios where anomalies are rare,
a high AUC-PR typically provides a clearer picture of a
model’s practical effectiveness than a high AUC-ROC alone.
H. A PRIMER ON HEURISTIC-BASED APPROACHES
Heuristic-based methods rely on expert-defined rules
or domain insights to pinpoint suspicious behavior in
blockchain transactions. Rather than learning a model purely
from data, these approaches encode known ‘‘red flags,’’ such
as unusually high-frequency transactions, dusting attempts,
or repetitive output patterns indicative of mixers or tumblers.
These rules often stem from forensic experience or analysis
of known attack patterns. Because they draw on real-
world observations, heuristics can be especially effective
at catching known scams or protocol misuse in their early
stages. They are generally highly interpretable, as the logic
is explicit. However, their reliance on predefined patterns
makes them inherently brittle; they typically struggle to
detect novel or unforeseen attack vectors that deviate from
known tactics. Furthermore, as adversaries evolve, these rule
sets require continuous updating by experts to ensure they
remain effective. Consequently, heuristics often complement
data-driven approaches rather than replacing them, for
example, by acting as an initial filter.
VOLUME 13, 2025 202587

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
III. CASES OF ANOMALY DETECTION ANALYSIS
In this section, we comprehensively review existing anomaly
detection cases applied to cryptoasset transaction networks,
structured according to the previously proposed taxonomy
shown in Fig.6. While we categorize existing literature into
four broad classes, statistical analysis, network analysis,
machine learning, and heuristic-based, there is often con-
siderable overlap in practice. For instance, some studies
grounded in statistical analysis may integrate machine
learning classifiers to enhance outlier detection or employ
heuristic rules to filter initial datasets. Conversely, purely
heuristic-driven methods might incorporate network metrics
(e.g., modularity, centrality) for improved anomaly spotting.
Our taxonomy thus serves as a conceptual guide rather than
a rigid classification, reflecting the multifaceted nature of
anomaly detection in cryptoasset ecosystems. To clearly dis-
tinguish between local fraud detection and systemic security
risks, these methodologies can be viewed through a layered
lens, i.e. transaction-layer methods target individual value
transfers, network-layer analyses expose structural clustering
and flow patterns, and protocol-layer approaches scrutinize
consensus integrity and smart contract vulnerabilities.
A. STATISTICAL ANAL YSIS
We examine a set of studies employing various statistical
analyses to detect anomalies in cryptoasset transaction net-
works. These approaches often rely on fundamental statistical
metrics, such as mean, variance, correlation, higher-order
moments, or more advanced time-series and regression-
based modeling to characterize ‘‘normal’’ behavior and flag
outliers. A summary of the studies covered in this category is
presented in table 3 and 4.
1) DISTRIBUTION-BASED AND MARKET ANOMALY
DETECTION
• Signature: One example of a statistical approach for
outlier detection involves using signature to encoding
time-series data into a collection of iterated inte-
grals [43]. A truncated signature S(X) of order n for
a path X(t) ∈ Rd where X(t) = (X 1(t),..., X d (t))
records d features, e.g. price or volume, overtime t ∈
[0, T ] is defined as:
Sn(X)= (1, S1(X), S2(X),..., Sn(X)) (10)
where
S1(X)=
∫T
0
dX(t),
S2(X)=
∫T
0
∫t1
0
dX(t1)⊗ dX(t2),
S3(X)=
∫T
0
∫t1
0
∫t2
0
dX(t1)⊗ dX(t2)⊗ dX(t3),
... (11)
where ⊗ denotes the tensor product. This opera-
tion combines the vector differentials, i.e. changes
in features, at different time points to capture
higher-order relationships and interaction effects within
the time-series path X(t). Higher-order terms capture
multi-scale temporal dependencies. For instance, S2(X)
quantifies volatility interactions. To reduce computa-
tional complexity, the randomized signature is often
employed:
R(X)= A· Sn(X) (12)
where A is a random matrix with entries drawn from a
specified distribution (e.g., Gaussian or Rademacher).
These signatures signatures were applied to Bitcoin
price-volume time series to detect pump-and-dump
schemes characterized by abrupt price inflations fol-
lowed by sharp declines. Empirical evaluation demon-
strates the method’s effectiveness, achieving high
anomaly-detection performance up to 0.88 F1 score.
• Benford’s Law: Another relevant approach relies on
Benford’s Law to detect fraudulent activities and
unusual behaviors in cryptoasset transactions [44]. This
law predicts that the leading digits of many naturally
occurring numerical datasets follow a logarithmic
distribution:
P(d)= log10(1+ 1
d ) (13)
where d ranges from 1 to 9. Deviations from this
expected distribution often serve as indicators of
manipulation or anomalies. Cryptoasset transaction
data generally fit the conditions for Benford’s Law,
given their inherently wide numerical range. The study
of major cryptoassets such as Ethereum and Bitcoin
from 2009 to 2018 revealed that transaction values
closely adhered to Benford’s distribution based on
Mean Absolute Deviation (MAD) thresholds, indicating
largely unmanipulated behavior. By contrast, certain
other cryptoassets, e.g., TENX, VERI, and DOGE, were
identified as non-conforming to Benford’s law, aligning
with previously reported scandals and lawsuits.
• Mahalanobis distances: Robust anomaly scores have
also been developed using Mahalanobis distances (MD)
in cryptoasset market price data [45]. Mathematically,
MD measures the distance of a data point r from the
center of a distribution, accounting for covariance:
MD(r)=
√
(r−µ)T6−1(r−µ) (14)
where µ∈ Rn is the mean vector and 6 ∈ Rn×n is
the covariance matrix of a random vector r∈ Rn. The
anomaly score A is then defined as:
A(r)= MD(r)√n (15)
This score effectively identifies significant deviations
in cryptoasset returns from typical behavior, effectively
flagging unusual market movements as anomalies. For
instance, it successfully flagged drastic price surges
202588 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
during the metaverse boom in late 2021. Moreover,
incorporating MD-based anomaly constraints into port-
folio optimization reduced annual portfolio volatility
from over 90% annually to the 40 − 50% range,
underscoring the potential of these methods for risk-
sensitive investors.
• Auto-Regressive Moving A verage: Furthermore,
anomalies in Bitcoin price have also been studied using
forecasting methods such as Seasonal Auto-Regressive
Integrated Moving Average with Exogenous Fac-
tors (SARIMAX) [46]. By incorporating information
gathered from social media, detecting manipulative
practices, such as pump-and-dump schemes, becomes
highly effective. These anomalies were especially
prevalent during economic crises and periods of intense
speculation, including the market turbulence observed
during the COVID-19 pandemic. The social media
sentiment input improved detection capabilities, though
its contribution was modest during periods of intense
manipulation. Overall, the combined forecasting and
sentiment-analysis framework achieved an F1-score of
up to 93%, demonstrating the strong synergy between
market data and external sentiment signals [47].
• Hidden Markov Multi-linear Tensor Models: An
alternative statistical monitoring framework employs
Hidden Markov Multi-linear Tensor Models (HMTM)
[48] and Multivariate Exponentially Weighted Moving
Average (MEWMA) control charts [49], [50]. The
goal of HMTM is to model the relationships in
Bitcoin transaction networks that change over time
but where the underlying state of the network (e.g.,
normal, suspicious) is hidden. HMTM builds upon the
Multi-linear Tensor Model (MTM)[51] which model the
probability of a transaction between node i and j at time
t as:
P(yijt= 1|xijt, ui, uj, vt )= xijtβ+< ui, vt, uj>+εijt
(16)
where yijt indicates the presence 1 or absence 0 of a
transaction, xijt a vector of covariates, i.e., known fac-
tors, that might influence the transaction, e.g., example
transaction size, time of day, etc., β is the coefficient
vector that quantifies the effect of the covariates, ui and
uj represent latent vectors describing the position of
nodes i and j in an underlying latent space, vt captures
the latent rules governing node interactions at time t
andεijt is the error term assumed normally distributed
around zero. The MTM assumes a static network.
The HMTM adds a Hidden Markov Model (HMM) to
account for the fact that the network can be in different
unobserved states Bt = Yt−t where Bt represents
anomalous deviations, Yt is the observed transaction
adjacency matrix, andt is the expected structure based
on latent variables under normal hidden states. The
latent state Lt= (ut, vt ) describes the hidden dynamics
TABLE 3. Distribution-based & Market anomaly detection.
guiding network connectivity over time. By monitoring
deviations using Hotelling’s T 2 statistic, significant
anomalies in cryptoasset transaction behaviors are
flagged. The method flags Bitcoin transactions between
2011 and 2013 that significantly deviate from typical
historical patterns as potential anomalies align with the
Mt. Gox leaked transactions [52].
• V ector Autoregressive: V ector Autoregressive (V AR)
models have been employed to evaluate behavioral
anomalies driven by external economic factors, such
as gas price surges in Ethereum-based decentralized
autonomous organizations (DAOs) [53]. In this context,
the V AR framework captures how present values of
multiple variables (e.g., gas prices and DAO activity)
depend on their past values:
yt= v+ A1yt−1+ A2yt−2+... + Apyt−p+ ut (17)
where yt= (r gas
t , at ) is a vector containing log-returns
of the gas price and user activity at time t, v and
A1,..., Ap are coefficient matrices and ut represents
white noise. The V AR model enables the test for
Granger causality between gas price changes and
DAO activity while also capturing lagged effects
and inter-dependencies between these variables over
time. Analysis of 5,580 transactions from 7,825 users
in 191 DAOs revealed a surprising result: despite
significant gas price surges (up to 8500% increases
in 2020), the model showed only minor statistical
influence of gas price fluctuations on DAO user activity
levels. This insensitivity contradicts typical market self-
regulation expectations, where higher transaction costs
would theoretically deter participation.
• Adjusted volume: Notable terrorist attacks can also
be identified using an event-study approach based on
VOLUME 13, 2025 202589

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
mean-adjusted volume (A V) of useru at day t [54]:
A Vu,t= ln(Vu,t )− ln(ˆVu,t ) (18)
which captures deviations between observed and
expected user-level volumes. The average abnormal
mean-adjusted volume (AA V) is then formed by
summing these daily A Vu,t for each user in the group
and normalized by the total number of users, and
the cumulative abnormal volume (CA V) expands that
perspective across longer periods by aggregating AA V
values around an event window:
AA Vt= 1
Nt
N∑
u=1
A Vu,t (19)
CA Vt=
T∑
t=1
AA Vt (20)
Calculating mean CA V for the two-week intervals
before [t − 15, t− 1] and after [t + 1, t+ 15] any
terrorist attack isolates sharp bursts of transactional
activity consistent with short-term planning and exe-
cution patterns. When applied to Bitcoin blockchain
transactions, categorized into groups like exchanges,
dark markets, mixers, gambling platforms, and other
services, CA V can reveal significant spikes in abnormal
transaction volumes through mixers and unregulated
exchanges in the weeks preceding major terrorist
events. A focused case study on the Sri Lanka Easter
bombing demonstrates the approach in action, detecting
suspicious transfers by a single user with no plausible
alternative explanation; backward traces link the wallet
to other crimes, while forward traces reveal subsequent
conversion to Ripple (XRP) and additional mixing via
a high-value deposit wallet, underscoring the effec-
tiveness of on-chain analysis in illuminating terrorist
financing structures.
2) MINING BEHAVIOR ANOMALY DETECTION
Anomalous mining strategies can undermine the security
guarantees of proof-of-work (PoW) systems by distorting
reward distribution or enabling attacks such as double-
spending. To address this, various statistical frameworks have
been developed to detect non-compliant miner behavior.
• Miner Sequence Bootstrapping: One such approach is
Miner Sequence Bootstrapping (MSB)[55], which mod-
els each miner’s block-discovery event as a Bernoulli
trial with success probability proportional to its hash-
power share. Under normal conditions, the probability
of a single miner discovering consecutive blocks in rapid
succession should be relatively small unless its hash
power is exceptionally large. Mathematically, let C T
i
denote the number of times miner i mines consecutive
blocks over a given period T , and let ST
i represent the
output of a reshuffled (bootstrapped) sequence of block
TABLE 4. Mining behavior anomaly detection.
assignments in the t-th trial. The MSB index is then
defined as:
MSBT
i = C T
i −⟨S T
i⟩
σ
[
ST
i
] (21)
where⟨ST
i⟩ and σ
[
ST
i
]
denote the mean and standard
deviation of the bootstrapped consecutive-block counts,
respectively. An MSB value significantly greater than
zero, often assessed via a p-value derived from the nor-
mal or empirical distribution of the bootstrap samples,
indicates that miner i is an outlier, which may imply
undisclosed strategic behaviors, such as delaying block
publication. This methodology is also extended to detect
mining cartels by measuring how often two miners i and
j appear in succession.
MC T
ij=
C T
ij−⟨S T
ij⟩
σ
[
ST
ij
] (22)
where C T
ij is the actual times that two consecutive
blocks are first mined by miner i and then by miner
j. Applying this framework to cryptoassets, including
Bitcoin, Ethereum and Litecoin and Bitcoin Cashreveals
the presence of anomalous miners in all four cryptoas-
sets, with particularly notable clusters of outliers in
Bitcoin Cash. Some of these miners remain unidentified
(tagged as ‘Unknown’), implying hidden pools or ad-
hoc collusions. While anomalies are also observed in
Litecoin and Bitcoin, the patterns there appear less
concentrated than in Bitcoin Cash. The framework
is then extended further to include the analysis of
Monacoin, adopting a related statistical test based on
a type II binomial model to detect disproportionate
sequences of consecutive blocks [56]. A salient finding
is that Monacoin exhibits the highest fraction of
suspicious miners, corroborating the network’s self-
reported selfish mining incidents. Furthermore, many
of these flagged entities exhibit collaborative structures,
suggesting coordinated withholding of blocks among
multiple miners.
• Miner Share Distributions: Beyond selfish mining,
the risk of majority attacks by investigating shifts in
miner share distributions is also studied [57]. The
analysis examines the assumption that computational
power is broadly distributed, i.e., no single entity should
dominate the network, and proposes creating detailed
202590 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
profiles of each major miner or mining pool. By sys-
tematically tracking the evolution of these profiles
over time, the approach flags anomalies indicative of
rapid concentration of hash power, which elevates the
threat of a 51% attack. Empirical findings on Bitcoin
and Ethereum illustrate how abrupt spikes in a single
miner’s share function as early indicators of potential
double-spending or extended block rewriting, offering
a proactive means to detect and mitigate malicious
consolidation of hashing resources.
These statistical techniques offer a harmonious blend of
simplicity and sophistication in detecting anomalies across
cryptoasset networks. Methods like Benford’s Law and
Mahalanobis-based scoring shine for their computational
efficiency, ease of implementation, and broad generalizability
across diverse datasets, while signature-based and tensor
models, as well as forecasting frameworks, deliver deeper
insights and capture complex temporal dynamics albeit at
a higher computational cost. Although techniques based on
basic distribution properties scale well and provide read-
ily interpretable signals, more advanced approaches often
require extensive parameter tuning and robust computational
infrastructure, which can hinder real-time application and
limit adaptability to rapidly evolving market conditions. Like-
wise, mining behavior anomaly detection methods effectively
highlight irregularities in block discovery and pool dynamics
but depend critically on accurate miner identification and
are vulnerable to sophisticated adversarial strategies. Col-
lectively, these approaches underscore a trade-off between
simplicity and granularity, suggesting ample room for
improvement through hybrid models, adaptive thresholding,
and enhanced integration of external factors to bolster
detection accuracy and scalability further.
B. NETWORK ANAL YSIS
Network analysis approaches leverage the inherent graph
structure of blockchain transaction networks to identify
anomalies. These methods analyze structural properties,
connectivity patterns, and topological features to detect suspi-
cious behaviors that might indicate fraud, money laundering,
or other malicious activities. For the brief theoretical aspect
of graph construction and the relevant properties of the graph,
refer to section II-E.
1) STRUCTURAL & COMMUNITY ANALYSIS
A notable body of literature concentrates on global network
properties of blockchain transaction graphs, such as degree
distributions, clustering, community structure, and core-
periphery organization. These analyses frequently uncover
unexpected hierarchies and densely connected communities
of addresses, challenging the assumption that blockchains are
fully decentralized. Moreover, detecting strongly clustered
groups, short-lived ephemeral subgraphs, or community
‘‘islands’’ reveals that suspicious or anomalous activity may
easily concentrate among a few addresses, underscoring
how important these structural analyses are for security,
compliance, and the overall health of blockchain ecosystems.
A summary of the studies covered in this category is
presented in table 5.
• Cryptoasset Transaction Network Structure: Several
early works analyze the Bitcoin transaction network
from a structural perspective, with [58] focusing on
four years of transaction data and revealing a small-
world topology. In such a topology, the average geodesic
distance among addresses is quite short, implying a
relatively high level of interconnectivity; however, high-
degree hubs in these networks can act as de facto
‘‘centralized’’ nodes handling disproportionate trans-
action volumes, potentially undermining the ethos of
full decentralization. Meanwhile, [59] and [60] explore
broader Bitcoin data to show scale-free-like degree
distributions in which a small minority of addresses
dominate overall connectivity; thus, although path
lengths remain short, control is concentrated among a
handful of high-degree nodes. While scale-free behavior
often arises in real-world systems, it raises concerns
about single points of failure or suspicious concentration
of network power; for example, a small clique of
exchanges or mixers could become a structural choke
point. Both studies further incorporate clustering and
assortativity metrics, finding that the Bitcoin network is
mildly disassortative: large hubs primarily interact with
small nodes, forming star-like substructures centered
on major exchanges or service addresses. These obser-
vations align with additional findings in [58], which
notes that certain regions exhibit usage patterns heavily
oriented around small-value gambling transactions,
underscoring how socio-economic factors can foster
specialized clusters of activity. These results highlight
that although the Bitcoin network achieves short-path
efficiency and maintains a degree of resilience, its
reliance on a small number of hubs and the influence of
regionally specific transaction behaviors can introduce
potential vulnerabilities and undermine the cryptoasset’s
intended decentralization.
Whereas the above focuses solely on Bitcoin, [61]
compares a Bitcoin trader network and an adolescent
friendship network using community detection and
social network analysis techniques, revealing interest-
ing parallels and distinctions. Both networks exhibit
moderate clustering, meaning that nodes tend to form
tightly-knit groups and some reciprocity. Reciprocity,
in this context, refers to the tendency for relationships
to be mutual, i.e., if one person or Bitcoin trader forms a
connection with another, the other is likely to reciprocate
the connection, creating a two-way relationship. It is
also concluded that adolescents prefer a reciprocal
relationship with the same gender and that drinkers
tend to be more active in their social circle. Notably,
this financial network displays assimilation rather than
VOLUME 13, 2025 202591

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
homophily; users tend to trade more frequently within
their own communities without a strong tendency to
connect based on similar characteristics. Furthermore,
unusually dense or exclusive subgroups in the Bitcoin
network could serve as indicators of suspicious activity.
Overall, these findings underscore the structural simi-
larities and behavioral differences between social and
financial networks, offering insights that are relevant for
understanding dynamics in both domains.
While designed as a stablecoin bridging multiple
exchanges, Tether has been studied from both com-
munity and global-structure standpoints. The study
using a Social Network Analysis (SNA) of the Tether
transaction graph [62] reveals that the Tether transaction
graph lacks the small-world property, which typically
characterizes robust and efficient networks; instead,
large cryptoasset exchanges dominate the degree distri-
bution, acting as central nodes with significant influence
over transaction flow. Bitfinex emerges as a pivotal
player due to its co-ownership and co-administration ties
with Tether’s issuer, exemplifying a ‘‘rich-get-richer’’
effect that suggests control by a few major entities,
potentially enabling manipulative practices. The net-
work’s low assortativity, indicating that high-volume
entities do not form stable links over time, points to
transient periods of high trading activity rather than
sustained market interactions. Additionally, the concept
of ‘‘bubble networks,’’ defined by short periods of
intense trading centered on key nodes, mirrors financial
bubbles and further highlights structural vulnerabilities.
• Random Graph vs. Cryptoasset Transaction Graph:
Complementing these global analyses, [63] fits random-
graph models, i.e., Chung–Lu [64] and Buckley–
Osthus [65], to Bitcoin’s structure by using mathemati-
cal frameworks that describe how edges form between
nodes according to probabilistic rules and highlights
the bowtie structure yet reveals that the data deviate
from simple scale-free or random attachment models,
exhibiting persistent anomalies such as over-centralized
clusters and ephemeral spike subgraphs likely resulting
from intentional participant behaviors, e.g., strategic
transaction patterns or the use of mixing services,
network evolution over time, and underlying economic
forces, these deviations indicate that simple random
models do not fully capture the network’s structural
features, with ephemeral subgraphs potentially repre-
senting abrupt transaction bursts or on-chain mixers that
raise compliance concerns. In a similar direction, [66]
employs random-walk embeddings for link prediction
by modeling Ethereum transaction records as a Tem-
poral Weighted Multidigraph (TWMDG), G= (V, E),
where V is the set of nodes (accounts) and E is the set
of edges (transactions). Each edge e is represented as
e = (u, v, w, t), where u is the source node, v is the
target node, w is the weight (transaction amount), and t
is the timestamp. This model incorporates the temporal
TABLE 5. Structural & Community analysis.
and weighted aspects of transactions, recognizing that
the timing and size of transactions are important
features. This temporal information models the network
as evolving continuously over time with additions of
links. V arious random walk strategies then applied over
the TWMDG, defining Temporal Successive Edges,
Lt (u) = {e | Src(e) = u, T (e) ≥ t} as the
set of edges leaving node u at or after time t and
assigning selection probabilities PT (e) of the random
walk selecting successive edge e at time t from node
u would then be PT (e) = 1
|Lt (u)| (unbiased) or with
respect to timestamp or amount (biased). The results
show that local features like degree alone are insufficient
for uncovering hidden edges that form ephemeral
or secretive transaction clusters, which may harbor
potential money-laundering or consolidation strategies
undetected when subgraph patterns are overlooked.
• Hierarchical structures of Tokens: Several studies
on token networks and smart contracts explicitly
demonstrate that nominally ‘‘decentralized’’ systems
may exhibit pronounced core-periphery or hierarchical
structures, thereby challenging the principle of net-
work flatness. For example, [67] conducts community
detection on the AA VE token transaction network on
the Ethereum blockchain and reveals a dominant core
comprising centralized exchanges, such as Coinbase and
Binance, and key contract wallets that mediate most
token flows. This concentration indicates that a small
group of aggregator nodes can dominate transaction
throughput, introducing single points of failure and
potentially obscuring suspicious patterns like cyclical
liquidity. Similarly, [68] confirms that removing a few
top addresses, particularly major exchange accounts and
202592 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
pivotal smart contracts can fragment the connectivity of
the entire Ethereum token network, underscoring a crit-
ical structural vulnerability. The study further employs
the Jaccard Index J (A, B)=|A∩B|
|A∪B| , which quantifies the
overlap in transaction patterns by comparing two sets
of trading counterparts, with A and B representing, for
example, the sets of counterparties that two different
nodes interact with, and the Ordered Jaccard Index
(OJI) OJI (A, B) = |LCS(A,B)|
|A∪B| , where LCS denotes
the longest common subsequence between two sets
capturing sequential patterns in how accounts trade.
Aside from raising security issues, such a structural
vulnerability indicates that transactions are anything
but uniformly distributed and might reflect a persistent
risk if those key nodes are compromised or engage in
manipulative behavior.
Finally, [69] extends insights into decentralized
finance (DeFi) by analyzing transaction networks of
three prominent Ethereum-based tokens—Dai (DAI),
Uniswap (UNI), and Wrapped Bitcoin (WBTC)—using
metrics such as diameter, modularity, and density.
The analysis reveals centralized clusters bridging the
network, where large exchanges and pivotal smart
contracts act as intermediaries facilitating most trans-
action flows. These bridging nodes form cross-linked
communities that both enhance liquidity by connecting
isolated network segments and constrain transaction
behaviors within specific clusters. This pattern suggests
that, despite DeFi’s decentralized branding, actual
usage is dominated by a small set of heavily utilized
addresses, potentially creating single points of trust or
failure and exposing systemic vulnerabilities. Moreover,
structural biases hint at hidden risks, such as coordinated
market manipulation or irregular trading patterns,
as modularity analysis uncovers clusters with high
internal connectivity but limited external interactions,
and centrality calculations highlight influential wallet
addresses that critically shape market dynamics.
2) TEMPORAL & EVOLUTIONARY NETWORK METHODS
Whereas the previous subsection centers on static, cross-
sectional analyses, the works below incorporate a time-based
or evolutionary perspective, often investigating how
blockchain transaction networks grow, shift, or correlate with
external factors, e.g., exchange prices. Methodologically,
they frequently deploy preferential attachment models,
dynamic snapshots, or temporal embeddings, differentiating
them from purely structural studies that do not track changes
over time. A summary of the studies covered in this category
is presented in table 6
• Rich-Get-Richer: Recently, various works have studied
the preferential attachment, i.e., the ‘‘rich-get-richer’’
phenomenon in Bitcoin and Ethereum, each from a
distinct lens. For example, [70] is among the earliest
studies to show that Bitcoin’s growth follows linear
preferential attachment, i.e., new edges (transactions)
arrive with probabilities proportional to existing node
degrees or wealth. They showed that the probability of
forming a new link connecting to the node v is
p(kv)= kα
v∑
w kαw
(23)
where kv is the indegree of node v, and α ≥ 0. The
probability that the new link connects to any node with
degree k is
p(k)∝ nk kα (24)
Building on this, [71] relaxes the assumption of purely
degree-based attachment by introducing node ‘‘fitness’’
ηi and the preferential attachment kernel as
Aij= kθ
i kθ
j +ηiηj (25)
where for small θ the initial fitness differences are
not significantly amplified, but for larger θ these
differences can become prominent. The empirical
results indicate that certain nodes persistently attract
transactions because of higher fitness values, potentially
overshadowing simpler linear-degree rules. Further
extending these perspectives, [72] targets Ethereum
tokens, showing that multiple ERC-20 networks display
super-linear preferential attachment, indicating that a
few nodes quickly become hubs. Complementarily, [73]
synthesizes findings for both Bitcoin and Ethereum,
confirming that hubs maintain their dominance even
as overall market conditions and prices fluctuate.
Deviations from expected preferential attachment can
signal anomalies and potential fraud. For example,
a sudden connection surge to a previously low-degree
node or an unexpectedly high fitness score may raise
suspicion.
• Transaction network and Price Correlation: Another
stream of research addresses the temporal analysis of
multiple cryptoassets or snapshots aligned with price
variation. For instance, [16] identifies that the degree
distribution of monthly transaction networks for Bitcoin,
Ethereum, and Namecoin cannot be well-fitted by the
famous power-law distribution, i.e., these networks
exhibit heavy-tailed distributions rather than scale-
free properties. This structural uniqueness is further
emphasized by the observation that while both Bit-
coin and Ethereum networks are heavy-tailed with
disassortative mixing, where high-degree nodes connect
to low-degree nodes, only Bitcoin exhibits small-
world properties. These differences likely stem from
Ethereum’s diverse use cases, such as smart contracts,
which create more complex transactional patterns than
Bitcoin’s simpler peer-to-peer transactions. Likewise,
[74] uses weekly or daily transaction network snapshots
of Bitcoin to show that during price drops, the network
becomes more heterogeneous, i.e., dominant addresses
continue trading while most users reduce activity,
VOLUME 13, 2025 202593

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
amplifying market volatility. External shocks, such as
the Mt.Gox bankruptcy, disrupted established patterns.
Before Mt.Gox’s collapse, the out-degree distribution
where the probability that a node has k outgoing
connections follows roughly k−α was compatible with
a power-law model in about 54% of snapshots. After
Mt.Gox, this compatibility dropped to around 26%.
This shift indicates a fundamental change in how users
transact, reflecting a loss of confidence in centralized
exchanges and a redistribution of activity across the
network, thereby offering insights into the interplay
between network structure and market trends.
Several studies also explicitly link dynamic network
features to price forecasting or correlation. For instance,
[75] applies Principal Component Analysis (PCA) to
daily or weekly snapshots of Bitcoin’s address-level
graph, revealing that topological indicators such as
concentration in node degrees can precede significant
price shifts. Singular vectors derived from PCA show
strong correlations with Bitcoin prices, suggesting that
structural changes in the transaction network serve
as reliable predictors. In a similar vein, [76] adopts
correlation-tensor spectra for weekly XRP networks.
A four-dimensional correlation tensor C(i,j),(α,β) cap-
tures the relationships between different network fea-
tures over time. To find the spectrum of the correlation
tensor, a double singular value decomposition (DSVD)
was applied to unfold the tensorC can be unfolded along
a chosen mode (dimension):
C(i,j),(α,β)= U(i,j)61V∗
(α,β) (26)
V(α,β)= U(α,β)62W∗
(α,β) (27)
Here, U(...) and V(...) are the left and right singular
vectors, and 6i contains the singular values for the i-
th mode. The first SVD in eq.26 is unfolded such that
the (i, j) indices form the rows, and (α,β ) become the
columns while the second SVD in eq.27 unfold (α,β )
in a manner analogous to the first SVD. In each SVD
step, one obtains a list of singular values:
61= diag(σ1,σ 2,...), 6 2= diag(ρ1,ρ 2,...) (28)
where the largest overall singular values are obtained.
The singular values represent the amount of variance
captured by each corresponding singular vector. The
largest singular values, found along the diagonal of each
6i, indicate the most significant patterns or modes of
variation in that mode. These are used to identify which
relationships between the network features impact
XRP price movements most. The study discovers a
distinctive relationship between the largest singular
values and price peaks, offering early indicators for
impending surges or drops. Extending these approaches
further, [77] employs a partial-differential-equation
(PDE) framework using time-varying chainlet patterns
to model Bitcoin price fluctuations. Chainlets are small,
TABLE 6. Temporal & Evolutionary network methods.
directed pieces of the Bitcoin transaction network that
capture common transaction patterns. The idea is that
each group (or cluster) of similar chainlets has a certain
influence on the Bitcoin price, which we denote by
u(x, t) where x represents an abstract position that
orders the chainlet clusters, i.e., clusters with similar
transaction patterns are placed close together. The PDE
framework uses these chainlets to model the continuous
evolution of Bitcoin price movements:
∂u(x, t)
∂t = ∂
∂x (d(x)∂u(x, t)
∂x )+ r(t)u(x, t)h(x) (29)
The term ∂
∂x (d(x)∂u(x,t)
∂x ) models the diffusion of
influence across clusters, with d(x) describing how
interactions vary spatially and the term r(t)u(x, t)h(x)
captures the local growth or decay of this influence. The
study concludes that expansions or contractions within
transaction subgraphs act as short-horizon signals for
bull or bear dynamics.
• Temporal Change of Transaction Network: One
specialized approach is found in [78], which measures
the Lightning Network’s growth to test if it follows
a Barabási–Albert (BA) scale-free pattern. The BA
model generates networks where a few nodes are highly
connected hubs due to preferential attachment; new
nodes connect to existing nodes with high degree, fol-
lowing a power-law degree distribution. Their analysis
of newly opened channels reveals that the network
deviates from the pure BA model. Specifically, new
202594 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
nodes tend to connect to existing nodes with greater
Closeness Centrality rather than simply connecting to
high-degree nodes as predicted by the BA model.
This suggests that nodes are strategically choosing
connections to enhance routing performance within the
Lightning Network rather than simply maximizing their
number of connections, implying that the BA model
may not be optimal for simulating or designing routing
protocols for the Lightning Network.
Rather than analyzing the entire network at once,
[79] focuses on locally dynamic structures by building
ego networks for labeled Ethereum accounts (e.g.,
ICO, Mining, Gambling, Ponzi). Ego networks are
subgraphs centered on a single node (the ‘‘ego’’)
that includes its immediate neighbors (the ‘‘alters’’)
and all the connections among those neighbors. This
approach provides a localized view of an account’s
direct transaction environment and captures dynamic,
micro-level interactions that can be obscured in a
global analysis. The study finds that illegal accounts
(Ponzi and Phish) have much shorter lifecycles (less
than 20 days) compared to normal accounts. It also
reveals that ICO accounts exhibit high local clustering
(≈ 0.18), suggesting that ICO investors frequently
transact with one another, while gambling accounts
have very low clustering ( ≈ 0.024), reflecting their
sporadic interaction patterns. Furthermore, the ratio
of in- to out-transactions varies by account type, and
mining, exchange, and Ponzi accounts show a higher
proportion of out-transactions, which reflects their
distinct operational roles.
3) GRAPH-BASED DETECTION & DE-ANONYMIZATION
Whereas the previous subsections emphasize either static
structure or temporal evolution, the studies below deploy
graph-based methods to uncover malicious usage, suspicious
flows, or anonymity breakdown in blockchain transaction
networks. These methods often involve refined address-
clustering heuristics, subgraph-based anomaly detection,
or specialized modeling techniques, enabling the identifica-
tion of fraudulent behavior. A summary of the studies covered
in this category is presented in table 7
• Address Clustering & De-Anonymization: A key
theme is the use of enhanced address clustering to
reveal hidden links and partially de-identify actors. For
example, [80] focuses on Zcash, an altcoin of Bitcoin
aiming to protect blockchain anonymity, extending
the traditional multi-input heuristics, which assume
that all input addresses in a transaction belong to
the same user by combining with tracking change
(shadow) addresses, addresses automatically generated
to return leftover funds from a transaction to the
sender. This results in an increase in the clustering
rate by 9% as the change addresses often belong to
the same user as the input addresses, providing a
way to link transactions and cluster addresses more
effectively. Despite zero-knowledge proofs, repetitive
spending patterns like round-trip transactions can
partially deanonymize activity, with 87.5% of addresses
and 25.7% of transactions linked to mining rewards and
shielded pools used mainly by founders, miners and
mining pools rather than typical privacy-focused users.
Similarly, [81] explores the Bitcoin network into entities
such as exchanges, gambling sites, and miners using
features like multi-input patterns and transaction rates,
which further refine classification by analyzing behav-
ioral trends over time. These features are used in a
classification method that applies clustering algorithms
and statistical analysis to group addresses into entities
with consistent behavior patterns. This allows outliers,
i.e., addresses exhibiting unexpected behaviors, to be
flagged as suspicious.
• Transaction Flow & Anomaly Analysis: Several
studies address manipulative or fraudulent behaviors
in cryptoasset markets. Reference [19] analyzes leaked
Mt. Gox data to reveal potential price manipulation
linked to abnormal trading activity by constructing
user-level transaction graphs. Accounts involved in
‘‘extremely high’’ and ‘‘extremely low’’ transactions,
those significantly deviating from the average market
price on a given day, are identified. These abnormal
accounts (ABA), which are classified into extremely
high accounts (EHA) and extremely low accounts
(ELA), represent 12.5% of the accounts and approxi-
mately 2.8% of transactions with ABA accounts. These
abnormal accounts were correlated with sudden price
changes via SVD, where transaction data are first
divided into daily snapshots and then represented these
snapshots as matrices. Then, SVD was applied to extract
‘‘base networks,’’ i.e., dominant patterns of transactions
within the network. The results show that the abnormal
accounts transactions strongly related to the Bitcoin
price especially the volume and direction of transactions
involving EHAs and ELAs, significantly correlated with
fluctuations in the Bitcoin price on Mt. Gox. Similarly,
[82] proposes a Petri-net–based framework to model
concurrency and dynamic transaction flows in Bitcoin.
The model extracts nineteen transaction features. For
example, the in/out ratio measures the balance between
incoming and outgoing transactions for an address,
where a high in/out ratio may indicate an accumulation
phase, while a low ratio suggests funds are being
drained. The identification of short cycles, where funds
rapidly move through a series of addresses and return
to the origin, can be indicative of layering techniques
used to obscure the source of funds. By combining
these features, the framework aims to provide a more
comprehensive approach to blockchain forensics.
Concerning computational performance, [83] focuses on
GPU-accelerated methods for subgraph-based anomaly
detection to address the computational challenges of
VOLUME 13, 2025 202595

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
TABLE 7. Graph-based detection & De-anonymization.
analyzing large datasets. By constructing localized
subgraphs around each target transaction and analyzing
them with outlier-detection algorithms, the method is
scalable by leveraging the parallel processing capa-
bilities of GPUs, making it feasible to analyze large
datasets while maintaining effectiveness in identifying
anomalous transactions. For Ethereum, [84] investigates
transactions from an alleged Upbit exchange hack to
study on-chain laundering patterns. A money laundering
network on Ethereum was constructed by crawling
the transaction records of the Upbit Hack and then
conducting an analysis of the money laundering net-
work properties by comparing the money laundering
network with the normal network on Ethereum. Despite
Ethereum’s fast transaction capabilities, the results
show that money laundering accounts on Ethereum
are fast-in and fast-out accounts, meaning that dirty
money is transferred in and out quickly by money
laundering accounts. Also, compared with traditional
money laundering accounts that usually transfer high-
volume money, prudent money laundering accounts on
Ethereum tend to transfer very small-volume money
to evade the attention of regulatory authorities. The
actors take advantage of decentralized exchanges for
rapid layering to obscure the origin of funds and evade
detection. They also found that, like traditional money
laundering accounts, money laundering accounts on
Ethereum are zero out middle accounts, meaning that
they potentially transfer almost all incoming money out
to benefit in a big way.
• Subgraph Patterns: Meanwhile, [85] introduces Trans-
action SubGraph Networks (TSGN) for phishing
detection. The study used embed local subgraphs
around potentially malicious addresses and observe that
ephemeral, cyclical in–out flows are reliable indicators
of scam behavior. In phishing attacks, funds typically
flow into the scammer’s address and are quickly moved
out through a series of transactions to obscure their
origin. The presence of cyclical flows, where funds
return to addresses controlled by the attacker, further
indicates coordinated fraudulent activity. The TSGN
approach effectively identifies phishing scams on the
Ethereum network by focusing on these subgraph
patterns.
Recent investigations into the EOSIO blockchain reveal
that even systems with high transaction through-
put remain vulnerable to systematic manipulation.
Transaction-graph analytics are applied to uncover that a
significant portion of accounts exhibit bot-like behavior.
For instance, [86] analyzes features such as the time
intervals between transactions and bursty co-activity
where multiple accounts perform actions in close tem-
poral proximity to identify accounts with regular, pre-
dictable patterns indicative of automation. Their analysis
reveals that over 30.75% of the accounts (381,008 in
total) exhibit bot-like behavior, participating in more
than 192 million transactions and transferring around
640 million EOS tokens in repetitive and exploitative
ways for malicious purposes like bonus hunting and
clicking fraud. Similarly, [87] leverages local subgraph
embeddings around potentially malicious addresses and
observes that short-lived, recurrent transaction cycles
are reliable indicators of scam behavior. By combining
these various features, accounts that are systematically
abusing the high-throughput capabilities of EOSIO are
identified.
Although these graph-based methodologies have yielded
rich insights into blockchain networks, several important
considerations remain. Noted that Table 5, 6 and 7 do not
contain a ‘‘Measure’’ column since these network-focused
methods predominantly emphasize topological or structural
features of the transaction graph rather than, for instance,
specific predictive or classification metrics. On the plus
side, structural or community analyses effectively illuminate
how small sets of aggregator nodes or hub addresses exert
large-scale influence, and they are readily generalized to
different cryptoassets or token systems by simply redefining
node or edge types. Temporal and evolutionary approaches—
such as dynamic snapshots, preferential-attachment models,
or subgraph anomaly detection—add further realism and
can capture short-lived or bursty behaviors often missed
by purely static analyses. However, all of these techniques
face scalability challenges as blockchains grow in both
transaction volume and participant diversity, and complex
subgraph or multi-dimensional embeddings can quickly
become computationally expensive for large datasets. Fur-
thermore, clustering heuristics and models like Chung–Lu
or Barabási–Albert can fail to capture special nodes (e.g.,
centralized exchanges, mixers) or ephemeral patterns aris-
ing from purposeful on-chain manipulations, limiting their
predictive power. Real-world heterogeneities such as multi-
signature addresses, advanced DeFi operations, or bridging
solutions spanning multiple blockchains complicate straight-
202596 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
forward generalization. Moreover, while local subgraph
extraction helps isolate suspicious flows, it risks overlook-
ing broader interactions that cross these local boundaries.
Hence, future improvements might focus on more scalable
high-performance computing (e.g., GPU-based pipelines)
plus adaptive heuristics that incorporate domain-specific
behaviors (mixers, privacy protocols, exchange deposit wal-
lets, etc.) while balancing interpretability with the complexity
required to handle blockchains’ rapidly shifting topologies.
C. MACHINE LEARNING
Machine learning approaches have become increasingly
dominant in cryptoasset anomaly detection due to their ability
to learn complex patterns from large-scale transaction data.
These methods can be categorized based on their learning
paradigm and architectural design.
1) SUPERVISED LEARNING
Supervised learning methods rely on labeled datasets to
train models that can classify transactions or addresses as
legitimate or anomalous. A number of works have applied
classical supervised ML for cryptoasset fraud detection,
focusing on constructing domain-specific features and train-
ing algorithms such as Random Forest, SVM, LightGBM,
or XGBoost. Feature engineering plays a crucial role in
model performance, with successful approaches incorpo-
rating features from multiple dimensions ranging from
raw transaction records to abstract topological or temporal
metrics consistently boosting detection accuracy. The most
effective supervised methods incorporate diverse feature
types, typically encompassing (i) Transaction features such
as amount, fee, timestamp, and confirmation time, (ii)
Temporal features such as transaction frequency, timing
patterns, and burst behavior, (iii) Graph features such as
in/out degree, clustering coefficient, centralities, and (iv)
Behavioral features such as address reuse, transaction size
distribution.
• Fraud & Suspicious Activity Detection: Several
studies adopt classic ML approaches with carefully
engineered features. In [88], a combination of Random
Forest and XGBoost is employed for fraud detection
in Bitcoin. High accuracy is achieved by synthesizing
transaction and graph-based metrics, e.g. transaction
amounts, node degrees, and edge timestamps, allowing
the ensemble to capture both local (transaction-level)
and global (address-level) patterns. Similarly, [89]
proposes a stacking ensemble using decision trees,
naive Bayes, k-nearest neighbors, and random forest for
Bitcoin fraud. Adaptive Synthetic Sampling (ADASYN)
is utilized to address class imbalance, complemented by
SHAP for interpretability. ADASYN is an oversampling
technique that generates synthetic samples for the
minority class (e.g., fraudulent transactions) by focusing
on harder-to-learn examples. Unlike simpler oversam-
pling methods like SMOTE, ADASYN assigns higher
weights to minority class samples that are harder to clas-
sify, thereby improving the model’s ability to distinguish
between legitimate and fraudulent transactions. An F1-
score above 95% reflects the synergy between robust
feature engineering including user-specific transaction
frequency and connectivity and ensemble-based model
fusion.
Recent work in Ethereum phishing and suspicious
address detection leverages a variety of machine learn-
ing techniques and feature engineering approaches. For
instance, [90] uses XGBoost and RF with a blend of
structural and temporal attributes in the Ethereum trans-
action network. By quantifying transaction frequency,
inter-event timing, local node degrees, and address re-
use, their pipeline achieves 98% F1-scores for phishing
detection. Meanwhile, [91] focuses on node2vec embed-
dings combined with Adaptive Boosting (AdaBoost)
to detect money laundering in Bitcoin, concluding
that temporal behaviors and graph-based embeddings
rank among the most important features. Likewise,
[92] presents ‘‘GuiltyWalker,’’ a method that measures
each address’s distance from known illicit nodes via
random walks; these distance-based features, when fed
into RF yield notable accuracy gains for malicious
address identification. Across these studies, consistent
improvements arise from layering graph connectivity
features, e.g. in/out degrees, clustering coefficients, over
the more common transaction or temporal signals.
• Ponzi Scheme & HYIP Identification: Other works
target specific subproblems, such as Ponzi scheme
detection. Early examples include [93] and [94], which
rely on SVM, decision trees, and XGBoost to detect
Ponzi contracts on Ethereum. Results demonstrate
that combining smart contract code-level signals, e.g.,
extracted opcodes and function usage, with transaction-
based metrics, i.e., frequency and daily volume, mea-
surably improve classifier precision and recall. In line
with this, [95] applies standard text classification using
SVM and Naive Bayes on Solidity code tokens for Ponzi
detection. This approach treats the smart contract code
as text and utilizes natural language processing methods
to identify patterns indicative of Ponzi schemes. The
near-perfect accuracy reported with 99% overall accu-
racy underscores that raw contract text, featuring code
usage patterns and address references, can effectively
signal suspicious activity. This indicates that even
without a deep analysis of the opcodes or transaction
history, the textual content of the contract itself contains
discriminative features that can be used to detect Ponzi
schemes. Building upon this line of work, [96] proposes
heterogeneous feature augmentation (HFAug), a feature
augmentation scheme that integrates heterogeneous
transaction records, e.g., transaction amounts, time
lags between consecutive transactions and frequency
of transactions, and meta-path-based structural features.
When evaluated using Logistic Regression (LR), SVM,
VOLUME 13, 2025 202597

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
and RF, results confirm that capturing both temporal and
graph structures significantly strengthens classification
performance for Ponzi detection.
Focusing on Ponzi or High-Yield Investment Program
(HYIP) detection, [97] uses RF, NN, and k-NN to detect
Ponzi schemes on Ethereum. Over 20,000 Ethereum
transactions were analyzed and preprocessed to train
the models. Their main result shows that a large,
over 70 sets of raw features can be pruned down to
about 10 core features without compromising accuracy.
These core features likely include transaction-level and
address-level metrics, such as transaction amounts,
frequency, timing intervals, and patterns indicative of
Ponzi schemes. Similarly, [98] tackles the identification
of HYIP operators’ Bitcoin addresses via a custom
scraping-based approach. They highlight the effect of
transaction features like frequency of transactions per
day, deposit–withdrawal patterns, and transaction size
distributions on classification performance, concluding
that gleaning large labeled sets is critical to robust
supervised detection.
• Address Role Classification & Scalable Pipelines:
Another group deals with GPU-accelerated or large-
scale supervised pipelines. References [99] and [100]
adopt SVM, RF, and Logistic Regression on tens of mil-
lions of Bitcoin/Ethereum transactions, showcasing that
parallelization (e.g., GPU computing) is essential for
near-real-time detection. Their data includes advanced
features like node centralities, transaction bursts, and
timing intervals, and the results indicate that even
incremental improvements in feature engineering can
manifest as large gains in detection speed and precision
on these large networks. Similarly, [101] examines
suspicious-user detection in Bitcoin trust networks
with RF, deriving especially strong signals from node
centralities and trust-based features, where users rate
each other on a scale to indicate their level of trust, which
capture how user reputation, quantified through the trust
scores assigned to the user by their peers, and transaction
patterns connect.
Recent works highlight role classification rather than
direct anomaly detection. Reference [102] trains RF and
XGBoost to classify Ethereum addresses as exchanges,
wallets, or other key agents. They show that addresses
exhibit distinctive transaction frequencies and code
usage patterns, making assigning roles with high
confidence feasible. Extending this, [103] introduced a
pipeline called GTN2vec to embed Ethereum addresses
with features like gas price and timestamps in random
walks, enabling robust money laundering detection
via RF classifiers. Similarly, Bitcoin-focused studies
have developed specialized approaches for address
classification. Reference [104] proposed moment-based
features such as variance and skewness of transaction
amounts and used LightGBM to achieve high F1
scores for abnormal address detection. This was further
expanded by [105] to include multi-digraph embeddings
that incorporate transaction time windows, highlighting
the importance of temporal features and burst behav-
iors in enriching graph-based signals. Expanding on
these efforts, [106] introduces XGBCLUS, a frame-
work designed for anomaly detection that combines
XGBoost with under-sampling techniques to address
class imbalance to detect anomalies such as fraudulent
or malicious activities within Bitcoin networks. By inte-
grating explainable AI techniques like SHAP , the results
show how features such as transaction volumes play a
paramount role in classifying anomalous transactions.
• Supervised Deep Learning Applications:Lastly, [107]
demonstrates a supervised deep-learning approach that
uses an LSTM/Bi-LSTM/CNN ensemble for Ethereum
phishing classification. Although these are indeed deep
neural architectures, the pipeline is fully supervised,
relying on a labeled dataset of malicious and benign
addresses. Contrary to some graph-based methods, the
authors do not incorporate domain-specific features
(e.g., transaction frequency, node degrees, or gas
usage). Instead, they embedded the raw addresses and
fed them into the ensemble model, achieving near
99% detection accuracy. This outcome underscores the
strength of combining address-level embeddings with
advanced neural networks for phishing detection in
Ethereum.
Table 8 provides an overview of representative supervised
techniques for cryptoasset anomaly detection, highlighting
their performance metrics, data sources, and target anomalies.
In general, Random Forest (RF) appears frequently and
often outperforms other classic ML methods, e.g., deci-
sion trees, SVM, or logistic regression, likely due to its
robustness against noisy features and its ability to capture
both nonlinear and interaction effects among transaction,
temporal, and graph inputs. However, a major drawback
of most supervised approaches is their susceptibility to
class imbalance, as many real-world datasets exhibit far
fewer fraudulent or malicious samples than legitimate ones.
Although techniques like SMOTE or ADASYN partially
address this imbalance, oversampling can introduce synthetic
noise, while undersampling risks discarding informative
samples. Moreover, many of these studies rely heavily on
public, on-chain datasets, which may omit off-chain data
such as user reputations or external intelligence. Methods
that exploit private or proprietary data like trust scores, code
annotations, or exchange user logs may improve accuracy
but are less generalizable if these proprietary sources are not
publicly available. Finally, while ensemble and deep-learning
pipelines can be scaled to large transaction networks (some
employing GPU acceleration for tens of millions of records),
their performance may still be constrained by the quality and
consistency of labels, underlining the continuing importance
of robust data collection and labeling strategies for new
research directions.
202598 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
TABLE 8. Supervised learning methods.
2) UNSUPERVISED AND SEMI-SUPERVISED LEARNING
Unsupervised learning methods address the challenge of
limited labeled data in cryptoasset ecosystems by identifying
intrinsic patterns without requiring extensive ground-truth
annotations. These approaches aim to capture the underly-
ing structure in transaction or address networks, allowing
researchers to flag suspicious or outlier behaviors.
• Clustering-Based Anomaly Detection: A number of
studies focus on clustering-based techniques to separate
normal versus anomalous user activity. For instance,
[108] adopts trimmed k-means on Bitcoin data to isolate
potential fraud clusters by removing outliers that might
distort the centroids. Their experiments demonstrate
that removing a small percentage of extreme points
before clustering significantly improves overall fraud
detection rates. Similarly, [109] and [110] combine
k-means, Mahalanobis distance, and unsupervised Sup-
port V ector Machines (SVMs) to detect anomalies in
both user-centric and transaction-centric graphs. For a
user-centric graph, each node represents an individual
user, aggregating one or more Bitcoin addresses, and
edges between nodes capture transactions between
users. In contrast, a transaction-centric graph treats each
transaction as a node, and edges typically represent
the Bitcoin flow. By extracting features such as in-
degree, out-degree, average transaction size, and time-
interval statistics, their pipelines reveal that suspicious
transactions generally deviate markedly from the typical
distribution of user behavior. Meanwhile, [111] pro-
poses a two-stage approach where One-Class SVM first
flags outliers among Bitcoin transactions, then k-means
groups similar outliers by type of attack (e.g. double-
spending, malicious campaigns). This dual-step pipeline
improves interpretability, as each cluster of anomalies is
mapped to likely fraud scenarios.
• Collective & Address Aggregation Approaches:
Other works focus on either addressing large-scale or
complex transaction graphs. Reference [112] studies
malicious address identification in Bitcoin by combin-
ing temporal burst features, e.g., abrupt increases in
transaction volume or degree, and graph-based metrics,
e.g., clustering coefficient, in/out-degree. The study
highlights that aggregating addresses controlled by
the same user is crucial for achieving more accurate
anomaly scoring, i.e., disregarding the concept of
‘‘change addresses’’ can dilute signals indicative of
malicious behavior. In a typical Bitcoin transaction,
a user must spend the entire input, even if they intend
to send only a part of that amount to another party.
The remaining balance is then sent back to the sender’s
wallet via a new, often unrelated-looking address
called a change address. Reference [113] extends such
ideas using a collective anomaly detection paradigm
in Bitcoin, whereby clusters of wallets owned by
the same user are analyzed as a whole rather than
individually. Experimental results show that considering
the joint behavior across multiple addresses can increase
recall in identifying malicious or hacked accounts since
fraudsters often split illicit funds among numerous
addresses.
VOLUME 13, 2025 202599

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
• Semi-Supervised Learning with Graph Embed-
dings: Beyond direct clustering, some semi-supervised
approaches leverage graph embeddings or node rep-
resentation learning to detect scams. For example,
[114] implements a network embedding pipeline for
Ethereum phishing detection by incorporating transac-
tion metadata (e.g., amount, timestamp). After embed-
ding addresses into a low-dimensional space, they
apply one-class SVM to separate normal from phishing
nodes. Results indicate that preserving both temporal
and weighted edge information during embedding
(transaction sums, frequency) can markedly enhance
the recall for phishing address detection, highlighting
that more nuanced embeddings capture subtle fraudulent
signatures more effectively than simpler topological
embeddings alone.
Unsupervised and semi-supervised methods (Table 9)
address the lack of large labeled datasets by detecting
intrinsic structure or outliers within blockchain transaction
networks, a clear advantage over fully supervised approaches
that require extensive annotation. Because many suspicious
behaviors are subtle or evolve quickly, these clustering and
outlier-based techniques, e.g., k-means and One-Class SVM,
excel at capturing new or emerging fraud patterns that strictly
supervised pipelines might miss. Moreover, grouping suspi-
cious actors without prior labels provides a practical first step
in highlighting high-risk users or transactions for subsequent
investigation. By detecting the intrinsic structure or outliers
within the network, these methods mitigate the imbalance
problem inherent in scarce labeled data, a limitation that
fully supervised approaches must contend with. However,
these methods often suffer from limited interpretability, e.g.,
why a cluster is flagged as suspicious can be unclear, and
false positives may be high without further refinements,
such as combining domain-specific features or post-hoc
classification to filter alerts. Compared to the fully supervised
approaches discussed in the previous section, which tend
to achieve higher precision given abundant labeled data,
unsupervised pipelines must carefully tune hyperparameters,
e.g., number of clusters, outlier thresholds, and incorporate
domain knowledge, e.g., change address heuristics, to reduce
noise. Consequently, while these approaches are immensely
flexible and scalable for preliminary screening or for newly
emerging fraud vectors, practitioners may ultimately need
to fuse them with supervised classifiers, where labels
are available, to maximize detection performance and
interpretability.
3) DEEP LEARNING & GRAPH NEURAL NETWORKS
Deep learning architectures have demonstrated exceptional
performance in cryptoasset anomaly detection by auto-
matically learning hierarchical representations from raw
transaction data. Neural network approaches such as mul-
tilayer perceptrons (MLPs), convolutional neural networks
(CNNs), and recurrent neural networks (RNNs) have been
TABLE 9. Unsupervised and semi-supervised learning methods.
widely applied to tasks ranging from suspicious address
classification to contract-level fraud detection.
• Temporal GNNs & Dynamic Analysis: Multiple
studies leverage time-evolving behavior in transaction
records. In [115], a temporal GCN is integrated with
an LSTM backbone to detect illicit Bitcoin transactions
by capturing dynamic changes in the Elliptic dataset.
Exploiting the chronological ordering of transaction
blocks enhances classification accuracy, as each block
includes a timestamp indicating when it was mined,
forming an ordered sequence Bk→ Bk+1→ Bk+2...
that reflects the timeline of transaction appearance
on the ledger. For example, if block k is followed
by block k + 1, the transactions in block k +
1 must happen after those in block k. By treating
each block as a temporal slice, the model identifies
evolving patterns, e.g., unusual transaction values or
addresses, rather than assuming all transactions occur
simultaneously. Relatedly, [116] constructs forward and
reverse Ethereum transaction graphs and applies a bi-
graph attention-based network (LB-GLA T) to address
the limitations posed by the acyclic nature of transaction
graphs, which can obscure contextual relationships.
The forward graph captures the natural flow of funds
from senders to receivers, while the reverse graph,
constructed by inverting edge directions, reveals the
origin of funds. Learning from both directions improves
the detection of money laundering. Reference [117]
formalizes the detection of malicious Ethereum activity
using multi-layer temporal snapshots across multiple
202600 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
tokens. Their approach integrates these snapshots within
a temporal framework by segmenting the transaction
data into distinct time windows based on the timestamp
on each transaction. Snapshots from different tokens
that fall within the same time window are merged into
unified graphs, to which a graph convolution encoder
is applied to extract spatial and temporal features. This
enables the model to effectively capture cross-token
trading patterns and detect evolving behaviors, such as
sudden shifts in transaction volumes or unusual flows
that may indicate malicious activities. The model sig-
nificantly improves precision and recall by integrating
these temporal snapshots with a GNN-based encoder.
In a related approach, [118] uses a time-decayed
mechanism to build dynamic transaction subgraphs for
Bitcoin forecasting (DLForecast). The results show that
weighting recent transactions more heavily substantially
boosts accuracy in predicting future edges (transactions)
and highlights potential anomalies earlier.
• Transformer-Based Approaches: Transformer mod-
els, which leverage self-attention mechanisms to capture
relationships between elements in sequences, have been
widely adopted for anomaly detection due to their
capacity to process long sequences and extract com-
plex patterns from unstructured data. Reference [119]
propose BERT4ETH, a pre-trained Transformer-based
model that treats sequences of Ethereum addresses and
transactions as ‘‘tokens’’ within a language-modeling
framework. In natural language processing, tokens
typically represent words or subwords that serve as the
fundamental units for learning representations. In this
context, a subset of addresses in a transaction sequence
is randomly replaced with a special [MASK] token, and
the model is trained to predict the masked addresses
using the surrounding unmasked tokens. This masked
modeling strategy encourages learning robust contex-
tual relationships among addresses, yielding notable
improvements in tasks such as phishing classification
and de-anonymization. Similarly, [120] integrates a
V ariational Autoencoder (V AE) with a Transformer
architecture to detect anomalies in decentralized finance
(DeFi) protocols. The V AE compresses data into a
low-dimensional latent space while preserving local
features, effectively capturing short-term behavioral
patterns within limited time windows. In contrast, the
Transformer component models long-range dependen-
cies, enabling the detection of relationships between
temporally distant events. These long-range dependen-
cies enhance the model’s ability to detect patterns where
past behaviors influence future activity. The resulting
framework, Anomaly V AE-Transformer, demonstrates
strong performance in identifying malicious structural
shifts, such as those associated with flash-loan attacks,
and outperforms conventional CNN- and LSTM-based
methods on large-scale DeFi datasets.
• Heterogeneous, Multi-View & Subgraph-Focused
GNNs: Some approaches emphasize the use of
multi-type edges or multi-view channels in transac-
tion networks. Multi-type edges reflect that not all
relationships in a transaction graph are homogeneous;
edges may represent distinct types of interactions,
for instance, a basic fund transfer versus a contract
code invocation, or correspond to different analytical
perspectives. This idea is often operationalized through
multi-view channels, where each channel represents
a subgraph that captures a specific facet of the
overall network. Reference [121] uses a heterogeneous
graph neural network based on a relational graph
convolutional network (RGCN) to account for diverse
transaction types on Ethereum, such as contract calls
and standard transfers. Explicitly modeling each edge
type by assigning distinct parameters to different
transaction categories proves crucial for effective
phishing detection, particularly in scenarios with label
imbalance. Meanwhile, [122] integrates Bayesian uncer-
tainty modeling with a multi-channel graph attention
network to secure Ethereum-based Internet of Things
(IoT) transactions. Incorporating Bayesian uncertainty
enables a more robust handling of noise and class
imbalance by allowing prediction adjustments based
on estimated uncertainty. The multi-channel aggregator
processes different transaction subgraphs independently,
improving robustness and classification performance
when identifying anomalous IoT device addresses.
Methods proposed in [123] and [124] emphasize the
importance of extracting localized subgraphs around
target addresses for improved classification. Zhou et al.
[123] introduce Ethident, a hierarchical GNN (HGA TE)
framework that samples micro interaction subgraphs
from Ethereum and conducts classification at the
subgraph level. To address label scarcity, a contrastive
self-supervision module is incorporated, resulting in
a 1–5% relative improvement in accuracy compared
to baseline GNN models. In a complementary line
of work, Nicholls et al. [124] propose FraudLens,
which restructures the Bitcoin transaction graph through
affinity- or feature-based edge construction prior to
GNN training. Refinement of the graph structure
through the removal of extraneous edges leads to
substantial gains in classification performance when
identifying illicit transaction nodes.
Several studies adopt a star-shaped subgraph centered
around each suspicious address. Reference [125] focus
on phishing detection by constructing star subgraphs
enriched with multi-scale features, including inbound
and outbound transaction volumes, node lifetime, and
other relevant attributes. The resulting GNN-based
classification achieves nearly 99% recall on phishing-
labeled addresses, effectively capturing localized trans-
actional patterns characteristic of phishing activity.
VOLUME 13, 2025 202601

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
Likewise, [126] also utilizes star subgraphs but empha-
sizes the aggregation of both node and edge features
through a two-layer attention mechanism. By incorpo-
rating manually engineered features—such as minimum
and maximum transaction values—into the node embed-
dings, the approach significantly enhances detection
performance, reaching up to 99.3% recall. This repre-
sents a substantial improvement over embedding-only
baselines such as DeepWalk. In the same vein,[127] pro-
poses MP-GCN for phishing node identification, with
an emphasis on directed message passing. By explicitly
modeling the directionality of transactions, MP-GCN
enables a multi-hop aggregation mechanism that extends
beyond immediate (first-order) neighbors to incorporate
information from more distant nodes in the transaction
graph. This design carefully integrates features along
the flow of transactions, allowing the model better to
capture structural and behavioral patterns characteristic
of phishing activities. Experimental results demonstrate
strong classification performance, highlighting the criti-
cal role of directionality in distinguishing phishing from
legitimate addresses.
• Standard GNN Architectures & Autoencoders:
Another line of research applies GNNs with relatively
minimal graph or feature engineering. Reference [128]
develop a pipeline that combines random-walk embed-
dings for Ethereum role classification, such as identify-
ing exchanges or miners with a GCN layer for final pre-
dictions. for final predictions. Integrating random-walk
embeddings with GNN-based feature aggregation
demonstrates robust performance across large-scale
label sets. Reference [129] enhance suspicious address
detection on Bitcoin by introducing moment-based
features, including the variance and skewness of trans-
action amounts, into a lightweight GCN architecture,
achieving both faster convergence and strong detection
accuracy. Reference [130] frame Ethereum anomaly
detection as a one-class classification task, employing
a GNN-based autoencoder to learn node representations
from transaction graphs and identify anomalies based on
reconstruction error. In this setting, the autoencoder is
trained exclusively on benign transaction data, enabling
the detection of anomalous behavior as deviations
from learned normal patterns. This method outperforms
conventional anomaly detection approaches such as
Isolation Forest and SVM, particularly under conditions
of severe class imbalance. Finally, [131] apply standard
GCN and GA T to anti-money laundering and counter-
financing of terrorism (AML/CFT) detection on Bitcoin
transaction networks. While GA T yields a modest
performance improvement over GCN, both architectures
offer substantial gains relative to simpler graph-based
heuristics.
• Domain-Specific & Novel Neural Architectures:
Other works devise more domain-specific neural
network architectures tailored to unique aspects of
cryptoasset data. Reference [132] transform Ethereum
bytecode and Application Binary Interface (ABI) data
into grayscale images and employ an attention capsule
network for Ponzi scheme detection. This architecture
integrates capsule networks that preserve hierarchical
spatial relationships in data with an attention mechanism
that selectively emphasizes salient features. The result-
ing attention-augmented capsules effectively capture
code-level patterns in visual representations, achieving
an F1 score of approximately 98.38%. Reference [133]
introduce ChaosNet, a biologically inspired artificial
neural network that emulates chaotic dynamics observed
in biological neurons using chaotic neuron models based
on Generalized Luröth Series (GLS) maps. Applied
to Ethereum address classification, the model demon-
strates strong generalization and maintains competitive
or superior accuracy with fewer training samples.
Meanwhile, [134] diverges from transaction-level GNNs
and applies a standard feedforward NN to identify a
day-of-the-week effect in cryptoasset pricing. Although
not focused on GNNs or anomaly detection, the study
illustrates how deep learning architectures can uncover
subtle cyclical patterns in crypto market behavior. Refer-
ence [135] propose a random-paced structure-to-vector
embedding technique for user addresses in NFT and
Ethereum networks. This method captures multi-scale
structural identities—encompassing local connectivity,
community-level relationships, and global structural
roles—by sampling structural information at varying
temporal or topological ‘‘paces.’’ The resulting embed-
dings support high classification accuracy in detecting
malicious nodes within metaverse-based financial envi-
ronments. Finally, Hu et al. [136] introduce SCSGuard,
which adopts a contract-level perspective by mapping
Ethereum bytecode into opcode sequences and detecting
scams using a Gated Recurrent Unit (GRU) network.
GRUs, a type of recurrent neural network, are partic-
ularly effective at capturing temporal dependencies in
sequential data. Combined with an attention mechanism,
the model achieves strong performance in identifying
Ponzi and Honeypot contracts by learning critical
opcode patterns indicative of fraudulent behavior.
Despite their notable achievements, the methods in 10,
spanning temporal GCNs, Transformer-based models, het-
erogeneous graph networks, and specialized neural architec-
tures, exhibit both strengths and challenges. On the positive
side, time-aware GNNs and Transformer hybrids excel at
capturing dynamic or long-range dependencies, allowing the
detection of subtle shifts in transaction patterns that simpler
baselines would miss. Heterogeneous or multi-channel GNNs
can handle different transaction types, e.g., contract calls
versus standard transfers, improving expressiveness when
dealing with complex blockchain ecosystems. Further, focus-
ing on local subgraphs or star-shaped neighborhoods often
offers computational efficiency, making it feasible to classify
202602 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
TABLE 10. Deep learning & Graph neural networks.
suspicious addresses on large-scale graphs. Nonetheless,
several limitations remain. Many of these frameworks
require extensive label availability or rely on carefully
tuned hyperparameters for performance; label scarcity and
class imbalance hamper generalization. Domain-specific
approaches like those processing raw bytecode or capturing
chaotic neuron behaviors can be challenging to extend across
multiple blockchain platforms with differing transaction
structures. In addition, interpretability remains a challenge;
while attention mechanisms partially address transparency,
fully justifying why specific nodes or edges drive the
classification often requires additional heuristics. Finally,
real-time deployment in fast-paced contexts such as DeFi
demands further work on scalability and latency. These gaps
suggest avenues for future research, such as self-supervised
or active-learning strategies for label-constrained scenarios,
multi-chain or cross-chain anomaly detection architectures,
and better interpretability frameworks to align with regula-
tory requirements.
More broadly, these ML-based anomaly detection strate-
gies face several interrelated limitations and open research
directions that warrant further exploration. First, most super-
vised methods require large, high-quality labeled datasets,
which can be impractical due to data scarcity, evolving fraud
tactics, and class imbalance, where legitimate ones dwarf
fraudulent samples. This imbalance forces difficult trade-offs
between metrics such as F1, recall, and accuracy, requiring
careful calibration or advanced oversampling/undersampling.
Second, interpretability remains a critical hurdle; ensemble
and deep architectures often act as black boxes, making it
challenging to explain why transactions or addresses are
flagged as anomalous. Third, most studies focus on single
blockchain ecosystems; future research could expand to
multi-chain or cross-chain detection, given that malicious
activities often spread across platforms. Fourth, real-time
detection poses an additional challenge in dynamic envi-
ronments such as DeFi, demanding low-latency, scalable
methods that can handle continuous streams of transac-
tions. Finally, an ensemble-driven paradigm where multiple
diverse models such as RF, GNN, and Transformers are
simultaneously trained and stacked represents a promising
avenue for boosting robustness and generalization, especially
under adversarial conditions. Exploring these directions,
particularly self-supervised, active-learning approaches for
label-scarce scenarios and improved interpretability frame-
works, would further advance the reliability and practical
deployment of ML-based solutions in the cryptoasset domain.
D. HEURISTIC-BASED
Heuristic-based anomaly detection methods utilize expert-
driven or rule-based models to identify anomalous or
fraudulent patterns within cryptoasset transaction networks.
These methods range from forensic and analytical mod-
eling to specialized protocol designs and cryptographic
techniques. In contrast to statistical or machine learning-
based techniques, heuristic approaches often incorporate
domain-specific knowledge, emphasizing interpretability,
transparency, and regulatory compliance.
1) FORENSIC & ANALYTICAL MODELING
Forensic and analytical modeling approaches rely on
expert-defined heuristics and empirical observations to trace
suspicious activities, particularly those related to money
laundering, ransomware payments, and market manipulation.
Summary of the studies categorized under this category is
presented in table 11.
• Modeling & Analysis of Mixing Operations: A
significant focus lies on understanding and model-
ing cryptoasset mixing services used for laundering.
A heuristic-based goal modeling framework was intro-
duced to detect and categorize roles involved in Bitcoin
money laundering activities, particularly in mixing
operations [137]. A mixing operation refers to a process
where illicitly obtained cryptoasset is combined with
funds from other sources, using numerous intermediate
addresses, to obscure its original source and destination,
VOLUME 13, 2025 202603

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
thereby complicating tracking efforts. The approach
classifies Bitcoin addresses involved in these activities
into three distinct roles based on their transaction
behaviors and structural patterns: entry addresses (com-
municators), which initially receive illicit funds, kernel
addresses (soldiers), intermediary addresses frequently
used to obscure and redistribute funds within the mixing
network, and exit addresses (communicators), where
funds ultimately leave the network, typically toward
fiat gateways or cryptoasset exchanges. By heuristically
modeling these roles through transaction characteristics,
timing patterns, and relational structures, the method
systematically uncovers laundering activities within
complex Bitcoin transaction graphs.
Further analysis of mixing operations provides a more
detailed understanding of the methods used to obscure
illicit activity within blockchain networks. Modern
services such as MixTum, Blender, and CryptoMixer
employ advanced techniques, including randomized
transaction delays, multiple recipient addresses, parti-
tioning transfers into smaller amounts, and the use of
‘‘sweeper’’ transactions to periodically consolidate dis-
persed funds before redistribution [138]. Temporal and
structural features, such as deposit–withdrawal intervals
and address reuse patterns, exhibit consistent behaviors.
The analysis emphasizes ‘‘chain-level’’ patterns, focus-
ing on sequences of transactions rather than individual
ones. Patterns such as short inter-transaction intervals,
repeated fund-splitting, and systematic address reuse are
commonly observed. By tracing how outputs from one
transaction serve as inputs to the next and identifying
recurring features, such as typical transaction sizes or
timing intervals, it is possible to detect mixer-related
transaction chains with greater confidence.
A complementary abstraction model has been pro-
posed to analyze both centralized and decentralized
mixers [139]. This three-phase model includes: taking
inputs, performing the mix, and sending outputs.
Transaction-level analysis of platforms such as Chip-
Mixer, Wasabi Wallet, and ShapeShift demonstrates
how asset-swapping mechanisms and anonymity set
construction obscure fund provenance. Two frequently
observed techniques are peeling chains, where small
outputs are incrementally extracted over sequential
transactions, and obfuscating mechanisms, where trans-
actions are aggregated into anonymity sets to disrupt
linkage analysis. While these techniques are intended to
hinder tracking, they leave behind identifiable traces that
can be systematically analyzed.
• Context-Aware Taint Analysis: Improvements to
traditional taint analysis have also been introduced
to enhance the precision of tracing illicit Bitcoin
flows [140]. Taint analysis marks coins as ‘‘tainted’’
when they are linked to illegal activity and follows
their movements through the blockchain. Rather
than tracking every transaction indiscriminately, the
refined approach incorporates address profiling—
classifying addresses as exchanges, darknet markets,
payment processors, gambling services, and other
categories, to determine which paths are relevant.
Two context-based strategies are introduced to adapt
the analysis depending on the situation. Evaluation
metrics based on expected behavior of illicit funds
and observable blockchain patterns are also defined to
assess accuracy. This context-aware method reduces
unnecessary tracking and improves the detection of
meaningful transaction trails.
• Empirical Laundering Patterns: Further investiga-
tions focus on how cybercriminals convert stolen Bitcoin
into usable funds exceeding $11 million [141]. One
case study analyzes the Conti ransomware operation,
a prominent ransomware-as-a-service (RaaS) group
active until 2022, which targeted businesses and critical
infrastructure with high ransom demands [142], [143].
Findings show that while some actors employ advanced
obfuscation, many rely on simpler methods such as
repeated use of centralized exchanges, minimal layering,
or peer-to-peer transfer networks. Even for high-value
ransomware proceeds, laundering patterns often involve
basic fund splitting and direct cash-out services, chal-
lenging the assumption that complex chains and multiple
mixers are always used.
Additional analysis has focused on fraud and scams
in the decentralized finance (DeFi) ecosystem, par-
ticularly involving ERC-20 tokens on the Ethereum
blockchain [144]. Using open-source investigative
methods, including transaction tracing tools like Ether-
scan and smart contract analysis tools such as Slither,
patterns of illicit behavior such as rug pulls, pump-
and-dump schemes, and subsequent laundering activ-
ities have been identified. These techniques allow
for examination of transaction histories, token flows,
smart contract behavior, and bridging activities across
chains. Malicious actors often attract victims through
decentralized exchanges, extract funds, and then move
proceeds through mixers or cross-chain bridges. While
the technical complexity of the DeFi infrastructure
suggests the potential for sophisticated laundering,
findings indicate that many schemes rely on relatively
simple methods, such as cashing out via centralized
exchanges or using basic bridging strategies. These
actions leave identifiable on-chain traces that can be
systematically analyzed to uncover fraud patterns and
actor linkages.
2) PROTOCOL & CRYPTOGRAPHIC DESIGN
Protocol and cryptographic design approaches focus on
embedding security features within blockchain systems or
evaluating existing mechanisms to detect weaknesses. Instead
of concentrating exclusively on user-level transaction flows,
these studies often scrutinize the underlying consensus
protocols, deposit frameworks, and oracle implementations to
202604 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
TABLE 11. Forensic & Analytical modeling.
ensure robust cryptographic guarantees and resilience against
malicious actors. For a summary of the studies discussed in
this category, refer to table 12
• BFT Protocol Forensics & Accountability:One line of
work investigates Byzantine Fault Tolerance (BFT) pro-
tocol forensics, which formalizes post-violation diag-
nostics and accountability in consensus protocols [145].
When safety violations occur, e.g when more than a
threshold number of nodes act maliciously, the protocol
is expected to generate cryptographically verifiable
evidence that identifies the responsible replicas. To cap-
ture a protocol’s forensic capabilities, its support is
summarized by a triplet (m, k, d) where m the maximum
number of malicious nodes under which the protocol can
still provide forensic evidence, k the minimum number
of honest nodes’ transcripts required to reliably prove
culpability and d the number of Byzantine nodes that
can be held accountable after an agreement violation.
Analysis of protocols such as PBFT, HotStuff, V ABA,
and Algorand shows that even minor design variations
can significantly affect these forensic parameters. For
example, under certain configurations, e.g. PBFT-MAC,
HotStuff-null, and Algorand, even if transcripts from
all honest nodes are available, no meaningful forensic
evidence is produced, d = 0. By examining message
structures and quorum certificates, the study outlines
conditions under which sufficient forensic data can
be collected to reliably identify adversarial nodes.
This systematic approach enhances the ability of BFT
systems to recover from faults and strengthens their
defense against coordinated attacks.
• Cryptographic Endorsement for Secure Deposits:
Another line of research explores how to secure
Bitcoin-based deposits in specialized environments,
such as connected vehicles, automobiles equipped with
internet connectivity allowing them to communicate
with other devices both inside and outside the vehicle,
enabling various applications from navigation and
infotainment to advanced driver assistance systems and
vehicle-to-vehicle communication. A novel ‘‘Bitcoin-
TABLE 12. Protocol & Cryptographic design.
to-Connected-V ehicle’’ (Bit2CV) scheme which uses
cryptographic endorsements to verify the origins of
deposited funds has been proposed [146]. In this
scheme, the anti-fraud measures are primarily based on
a cryptographic endorsement procedure that leverages
threshold signatures σ = (σagg,ε ), where σagg is an
aggregated signature and ε represents a set of indices
corresponding to the signers who participated in creating
the signature. In this scheme, a vehicle must collect
endorsements from a threshold number of authorized
parties to verify the origin of deposited funds, thereby
providing robust anti-fraud measures while maintaining
compatibility with existing Bitcoin infrastructure.
• DeFi Oracle Security & Design: Finally, a broader
examination of decentralized finance oracles [147]
focuses on how blockchain protocols acquire and
validate real-world data, particularly market prices and
exchange rates, without relying on a single trusted
party. The study investigates mainstream DeFi platforms
built primarily on Ethereum, which commonly involve
cryptoassets such as ETH, DAI, MKR, AMPL, and
SNX. In these systems, a small set of whitelisted oracles
provides data that is aggregated to determine on-chain
prices, making the system’s integrity highly dependent
on a few key actors. Analysis of real-world oracle
deployments shows that reported prices often deviate
from current exchange rates, and oracles can suffer
from operational issues and anomalies. A comparison
of designs, including those used by MakerDAO (DAI
and MKR), AmpleForth (AMPL), and Synthetix (SNX),
reveals that each employs unique mechanisms for
data aggregation and validation. Proposed improve-
ments include stronger cryptographic binding of data,
more transparent governance over oracle selection
and operation, and robust mechanisms for detecting
and mitigating anomalous data, ensuring that on-chain
protocols accurately reflect off-chain reality.
3) HEURISTICS FOR SECOND-LAYER & ON-CHAIN EXPLOITS
Second-layer networks, such as the Lightning Network (LN),
enable off-chain transactions and micro-payments to improve
blockchain scalability, but also introduce new vectors for
misbehavior. The Lightning Network operates by creating
payment channels between users, allowing them to conduct
multiple transactions off the main Bitcoin blockchain. Only
the opening and closing of these channels are recorded
VOLUME 13, 2025 202605

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
on-chain. However, this opacity also presents challenges for
monitoring and security. Table 13 summarizes the studies
covered in this category.
• Lightning Network Analysis: Research in this area
focuses both on identifying LN activity from on-chain
data and analyzing vulnerabilities within the LN proto-
col itself. One study [148] evaluates multiple heuristics
to identify these LN-related transactions within the on-
chain data. This research explores what can be deduced
and inferred about the layer-two overlay network based
on the transactions recorded in the ledger. The analysis
shows that over 75% of all 2-of-2 multisignature
(2of2 multisig) transactions on the Bitcoin using Pay-
to-Witness-Script-Hash (P2WSH) can be linked to
LN channels. By correlating observable patterns, e.g.
channel opening and closing, with known LN addresses,
the study demonstrates that it is possible to infer aspects
of off-chain activity from on-chain records, even if only
part of the LN topology is revealed.
Complementary work [149] investigates routing vulner-
abilities in the LN. The findings indicate that adversaries
can strategically deploy LN channels with artificially
low fees to attract payment routes, effectively hijacking
the network’s routing topology. This tactic allows
them to exert undue influence, potentially censoring or
delaying transactions. The study reveals a fundamental
tradeoff: rational LN nodes, seeking efficient (low-fee)
routes, become susceptible to exploitation. To mitigate
this risk and enhance security, nodes must incur
higher transaction fees to avoid predictable routing
patterns. The study reveals that routing in LN is highly
centralized: nearly 60% of all routes pass through
only five nodes, and 80% through just ten nodes.
This concentration exposes the network to denial-of-
service attacks from a small set of colluding entities.
Furthermore, the research models an external attacker
establishing new LN links with minimal fees. Results
indicate that creating as few as five such links can divert
a majority 65%-75% of network traffic, regardless of
the specific LN implementation. The cost of deploying
these attack links is demonstrably low, underscoring the
economic feasibility of routing-based exploits in the LN.
• On-Chain Market Manipulation: On the on-chain
side, sophisticated manipulations occur on decentralized
exchanges (DEXs) that rely on transparent smart con-
tracts for trading. High-frequency or so-called ‘‘sand-
wich’’ attacks on Automated Market Maker (AMM)
platforms such as Uniswap is studied [150]. In a sand-
wich attack, an adversary exploits the latency between
transaction broadcast and execution by observing a
pending transaction in the mempool, placing a buy order
immediately before the victim’s order (front-running),
and then executing a sell order immediately afterward
(back-running) to profit from the induced price move-
ment. The study formalizes the attack mathematically
using the constant product formula, which governs the
price impact of trades on AMMs x· y = k where x
and y represent the reserves of the two tokens in the
liquidity pool, and k is a constant. Empirical evaluation
shows that a single attacker can achieve an average
daily revenue of approximately $3,414 on Uniswap.
These findings highlight that while the transparency
of blockchain transactions enables verification and
auditability, it also creates vulnerabilities that can be
exploited for market manipulation, underscoring the
need for improved safeguards in decentralized trading
systems.
In addition, a hybrid detection approach has been
proposed to identify pump-and-dump (P&D) schemes
on cryptoasset markets [151]. This method combines
distance- and density-based anomaly metrics to detect
sudden, suspicious price–volume movements across
multiple exchanges. It reformulates the problem of
contextual anomaly detection in time series data into
a point anomaly detection problem by dividing the
time series into frames, concatenating the data within
each frame into high-dimensional data points, and
projecting these points into a two-dimensional space
using Principal Component Analysis (PCA). In this
reduced space, established distance- and density-based
techniques are applied to effectively detect anomalies.
The approach consistently outperforms single-metric
methods by capturing anomalous patterns that might be
overlooked when using solely distance-based or density-
based measures, resulting in a higher detection rate of
P&D events across top-ranked exchange pairs and a
lower rate of false positives overall.
At a broader scale, an agent-based study simulates
price manipulation in the Bitcoin market driven by
Tether injections [152]. The simulation models both
typical trader behavior and a fraudulent agent that
repeatedly injects Tether on selected exchanges and
makes sustained Bitcoin purchases. In markets with thin
liquidity, these purchases push prices upward, attracting
additional momentum-following traders and magnifying
the effect. The malicious agent then strategically sells
small volumes of Bitcoin to recoup funds and satisfy
‘‘proof of capital’’ requirements, typically aligned with
end-of-month reporting. The results demonstrate that
this feedback loop of Tether inflows and controlled
Bitcoin sell-offs can trigger large price swings in an
illiquid market. The study concludes that concentrated
control over stablecoin issuance, combined with limited
liquidity, leaves the Bitcoin ecosystem vulnerable to
manipulation by a single actor. It also suggests that
more frequent audits of stablecoins and efforts to deepen
market liquidity could help reduce the risk of such price
inflation schemes.
Heuristic-based anomaly detection methods for cryp-
toasset transactions excel in interpretability and domain
202606 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
TABLE 13. Heuristic-based methods.
specificity, allowing investigators to quickly flag suspicious
behaviors (e.g., short inter-transaction intervals, mixing,
or protocol exploits) without requiring a large training
dataset. Such heuristics are relatively straightforward to
implement, rely on known illicit patterns, and can be tuned
to specific network features (like repeated fund-splitting
or cross-chain bridging). However, they may fail to detect
complex or evolving laundering strategies beyond the scope
of pre-defined rules, leading to higher false negatives as
criminals adapt. In addition, purely heuristic approaches
can be overly rigid, generating potential false positives
whenever normal users share superficial similarities with
illicit addresses (e.g., frequent transactions). Nonetheless,
when integrated into a broader detection pipeline, potentially
employing machine learning, address classification, and
external intelligence feeds, heuristic triggers can act as the
‘‘first line of defense,’’ rapidly filtering out large volumes of
routine activity while flagging suspicious outliers for deeper
investigation. This synergy between domain-driven heuristics
and automated analysis tools thus offers promising avenues
for new research, such as refining heuristics to detect novel
off-chain exploits or designing feedback loops that update
detection rules based on confirmed threat actor behaviors.
IV. CHALLENGES, LIMITATIONS, AND FUTURE RESEARCH
DIRECTIONS
This SoK has reviewed a collection of 103 papers centered on
anomaly detection within cryptoasset ecosystems, classifying
the employed techniques into four primary categories:
statistical analysis, network analysis, machine learning, and
heuristic-based methods, as detailed in Section III. This
section synthesizes these findings, providing a comparative
analysis across these categories. It also identifies significant
overarching challenges prevalent in the field and delineates
promising future research trajectories intended to guide
subsequent investigations in this dynamic domain.
A. COMPARATIVE ANAL YSIS OF DETECTION CATEGORIES
After evaluating the four classes of methodology, we found
distinct characteristics and trade-offs concerning their data
requirements, detection capabilities, interpretability, and
robustness. Table 14 provides a synthesized comparison
of these methodologies, summarizing their applications,
performance, and qualitative features based on the 103 studies
reviewed. While a direct comparison of performance metrics
is challenging due to the lack of standardized benchmark
datasets across studies, the table reveals clear patterns that
highlight the strengths and weaknesses inherent to each
approach.
Regarding data requirements and underlying assumptions,
Statistical methods commonly assume specific data distri-
butions, potentially limiting their effectiveness in volatile
cryptoasset markets, as they typically analyze numeric
transaction metrics rather than the underlying network
structure. Network Analysis techniques primarily leverage
the transaction graph’s topology, making them less reliant
on distributional assumptions but sensitive to how the
graph is constructed and computationally intensive for large
networks. Machine Learning approaches vary substantially
based on their subtype: supervised methods depend heavily
on labeled datasets, which are often scarce; unsupervised
and deep learning models circumvent labeling limitations but
necessitate extensive datasets and careful feature engineering.
Heuristic methods differ from the others by relying on
explicitly encoded domain expertise rather than extensive
data. Although data-light, these methods require continual
expert input to define and update their rules.
Regarding detection capabilities, Statistical methods are
particularly effective at identifying point anomalies, such
as sudden numerical deviations in transaction metrics.
Network Analysis excels at detecting structural and collective
anomalies, like coordinated fraudulent activities or network
attacks that leave distinct topological traces. Machine Learn-
ing methods offer broad capabilities, identifying not only
point anomalies but also complex contextual and collective
patterns, even uncovering previously unseen threats through
learned models. Heuristic approaches are highly effective for
addressing well-known vulnerabilities or explicit anomalous
patterns, such as specific smart contract exploits, by directly
encoding domain-specific knowledge into rules.
Interpretability varies significantly across methodologies.
Statistical methods and Heuristic rules typically offer high
interpretability due to their transparent logic and straight-
forward analytical frameworks. Network Analysis provides
moderate interpretability, enabling visual representations
of detected graph structures; however, advanced network
metrics may be less intuitive to interpret. Machine Learning
methods range widely, with simpler algorithms offering clear
insights into their decision-making processes. In contrast,
complex models, particularly deep neural networks, often
operate as ‘‘black boxes,’’ posing challenges for forensic
analysis and trust despite their powerful analytical capabil-
ities.
Scalability and computational requirements introduce
additional trade-offs. Statistical and Heuristic methods
usually have low computational demands, making them suit-
able for real-time anomaly detection. Conversely, Network
Analysis methods can become computationally intensive
VOLUME 13, 2025 202607

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
TABLE 14. Comparison of anomaly detection methodologies for crypto assets (numbers in parentheses indicate the number of studies involved).
due to the complexity of processing large-scale blockchain
transaction graphs. Machine Learning methods, particularly
deep learning approaches, require significant computational
resources during model training, although inference can be
relatively fast and scalable once trained.
Finally, adaptability and robustness highlight further
differences. Statistical methods often face challenges in
environments with rapid concept drift, which is common
in cryptoasset markets and requires frequent recalibration.
Network Analysis methods show robustness against certain
noise and small-scale manipulations but remain sensitive
to substantial topological changes or sophisticated adver-
sarial attacks. Machine Learning approaches can adapt
through retraining yet remain susceptible to adversarial
attacks specifically designed to evade detection. Expanding
the research horizon further requires integrating cross-
disciplinary paradigms, such as causal inference to distin-
guish intentional manipulation from actual market volatility,
and reinforcement learning for dynamic monitoring of
user behaviors. Additionally, advancing privacy-preserving
analytics through techniques like zero-knowledge proofs and
cross-chain graph alignment will be pivotal for maintaining
regulatory compliance without compromising user data
privacy. Despite their interpretability, heuristic methods are
brittle and effective for known threats but limited in their
ability to generalize and necessitate ongoing manual updates
to maintain detection effectiveness.
The comparative analysis presented in Table 14 under-
scores that no single methodology is universally superior.
The optimal choice is context-dependent, balancing the
need for high performance against the practical constraints
of data availability, the demand for robustness against
novel threats, and the requirement for interpretability.
From a practical standpoint, these trade-offs suggest a
stratified deployment strategy, i.e. heuristic rules serve as
an interpretable first line of defense for known threats,
while unsupervised learning is essential for spotting novel
patterns in label-scarce environments. Conversely, deep
learning workflows are best reserved for high-volume,
historical analysis where computational resources and
labeled data are sufficient to support complex model
training.
202608 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
B. REAL-WORLD ANOMALIES
Synthesizing the findings from Section III, this section
connects the surveyed methodologies to their application
in detecting prominent real-world anomalies. By grounding
the taxonomic analysis in concrete use cases, we can better
evaluate the strengths and limitations of current techniques
and highlight where certain methods are most effective.
The following discussion focuses on several key real-world
anomalies, evaluating how the surveyed methodologies have
been applied in practice to detect them.
1) MARKET MANIPULATION AND PRICE-RELATED
ANOMALIES
P&D and price–trend manipulation are typically executed
via coordinated bursts in price–volume and bursts in trading
activity. One effective approach uses signature methods [43]
to transform raw trade data—price, volume, side, and times-
tamp into powerful features. This technique can detect P&D
with F1 score up to 88%, making it highly competitive with
supervised methods while relying only on publicly available
trade histories. Similarly, forecasting-anomaly pipelines use
models like SARIMAX to flag periods where price trends
deviate significantly from predictions. The highest-volume
accounts active during these anomalous windows are then
flagged as potential manipulators. This approach is highly
successful, achieving an F1 score of up to 93%. For
DeFi-specific scams like rug pulls, which often combine
P&D tactics, forensic investigation using open-source tools
like Etherscan and Slither can reconstruct the entire scam
lifecycle [144]. This method reveals the common pattern
of token creation, liquidity seeding, orchestrated buys, and
eventual liquidity removal. This analysis also shows that the
subsequent money laundering methods are often unsophisti-
cated. Finally, a hybrid distance-density framework improves
detection by reducing the dimensionality of price-volume
data with PCA [151]. This allows a combination of distance-
and density-based outlier scores to identify abrupt trading
surges with a lower false-positive rate than single-metric
methods.
On the other hand, price-related anomalies were studied
by treating unusual price co-movements as market-level
anomalies rather than explicit manipulation. A network-
centric line links transaction-network structure to price e.g.
principal-component dynamics of Bitcoin’s address network
correlate with market regimes [70], and weekly correlation-
tensor/PCA snapshots of XRP transaction networks produce
singular-value signals that align with subsequent price
bursts [76]. A modeling line uses agent-based simulations
to show how concentrated stable-coin inflows (e.g., Tether)
in thin liquidity can amplify price swings consistent with
manipulation-driven bubbles and drawdowns [152].
These studies show that market manipulation can be
detected through two complementary lenses: direct analysis
of market data where statistical and machine learning
models identify anomalous price-volume patterns in real-time
or historically and indirect analysis of underlying market
structure, where changes in transaction network topology
or simulated agent behaviors signal price instability and
manipulation risk.
2) EXCHANGE EXPLOIT: THE Mt.Gox CASE
As the dominant Bitcoin exchange until its 2014 collapse, Mt.
Gox is a central case study for exchange-level manipulation.
Analyses of transaction history between 2011 to 2013 reveal
that accounts trading at extreme, unrealistic prices formed
dense clusters and unusual motifs (triangles, self-loops).
Temporal SVD showed these abnormal accounts were tightly
correlated with Bitcoin price movements, consistent with
liquidity creation and fake volume [19]. A complementary
approach models monthly transaction networks with hidden
Markov tensor methods and monitors latent variables using
MEWMA control charts. This framework flags the late-2013
period as ‘‘out-of-control,’’ providing statistical evidence
of manipulation without requiring explicit labeling [52].
Broader network studies confirm Mt. Gox’s systemic role:
structural break analysis shows that after its bankruptcy,
heavy-tailed out-degree distributions lost stability, and net-
work heterogeneity lost predictive regularity for price. This
indicates that Mt. Gox acted as a central hub driving both
liquidity and volatility [74].
Together, these methods i.e. graph classification with SVD,
latent-variable monitoring, and structural break analysis—
highlight how different anomaly detection frameworks can
reconstruct and quantify the manipulation that contributed to
Mt. Gox’s downfall.
3) MONEY LAUNDERING & TERRORIST FINANCING
The detection of illicit financial flows is approached by
analyzing on-chain data in relation to real-world events
and network behavior. One line of research focuses on
terrorist financing [54] builds a labeled map of large on-chain
service providers (exchanges, mixers, gambling, mining, dark
markets) and then monitor for abnormal transfer volume
around major terrorist attacks. This approach identifies
significant increases in funds flowing into unregulated
exchanges and mixers, the channels used to move funds from
organizers to local operatives and to launder them before
cash-out. Forensic accounting on specific events, such as
the Sri Lanka Easter bombing, corroborates these findings
and helps build machine learning models that use on-chain
flow features for risk prediction. Practically, a cross-asset
move like BTC to XRP shows up as funds leaving Bitcoin
into known exchange clusters, so the detector keys on the
inflow/outflow bursts to those exchange wallets rather than
the off-chain conversion step.
In more general case of money laundering, various
machine learning models are applied. A case study of the
Upbit hack [84] on Ethereum characterizes ML networks by
traditional traits such as fast-in/fast-out transfers and dense
transaction clusters, providing concrete features for on-chain
detection. On the Bitcoin network [91] (Elliptic dataset),
VOLUME 13, 2025 202609

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
graph embeddings are particularly effective, achieves approx-
imately 92% accuracy, though performance can degrade
during market disruptions like dark-market shutdowns. The
performance of these models can be improved with special-
ized features [92], [103]. More advanced architectures like a
temporal-GCN [115] and LB-GLA T [116] explicitly model
transaction sequences and graph directionality to address
challenges like over-smoothing, achieving high accuracy and
F1-scores.
A specific challenge within ML is detecting mixing
services, which are purpose-built to obfuscate fund origins.
Research in this area often interacts with mixers to obtain
ground-truth data, which is then used to identify transaction-
and chain-level patterns, e.g., I/O structure, sweeper trans-
actions [137]. Mixer mechanisms are formalizes as either
swapping (using peeling chains) or obfuscating (using Coin-
Join), with heuristics identifying over 92% of obfuscating
transactions [138]. To improve tracing, context-aware taint
analysis [139] uses address profiling to define logical exit
points (e.g., exchanges, gambling sites), pruning irrelevant
transaction paths. However, empirical studies show a contrast
to these sophisticated tools, revealing that many criminals
use surprisingly unsophisticated laundering methods, often
preferring direct transfers to centralized exchanges [140],
[141].
4) PONZI SCHEMES AND PHISHING
The detection of user-facing scams like Ponzi schemes
and phishing relies heavily on machine learning, with
distinct strategies tailored to each threat. For Ponzi schemes,
research focuses on pre-deployment detection by analyzing
the smart contract itself. One approach analyzes contract
artifacts, such as mapping bytecode or Application Binary
Interface (ABI) features into images for CNN and Capsule
Network pipelines, which effectively learn patterns in the
contract’s logic and function calls [93], [95], [98], [132].
A complementary method uses attention-augmented RNNs to
learn directly from n-grams of bytecode sequences, creating
generalizable detectors for Ponzi and related scams [94],
[96], [97], [136]. These studies show that a contract’s static
code footprint, including opcode frequency and control-
flow structure, is highly discriminative for identifying Ponzi
schemes even before any user transactions have occurred.
In contrast, phishing detection focuses on post-deployment
analysis of transaction networks, where Graph Neural
Networks (GNNs) are the dominant methodology. Early
work established a baseline by creating transaction-aware
network embeddings and applying one-class SVMs to
handle the severe class imbalance between fraudulent and
licit addresses [85], [90]. Current research builds on this
with more advanced GNNs. Studies consistently find that
heterogeneous GNNs, which explicitly model different node
and edge types (e.g., EOA vs. contract, transfer vs. call),
outperform simpler architectures [105], [107]. Other effective
methods operate on a subgraph-level [119], [121], analyzing
an address’s local neighborhood with features like transaction
value, gas, and time to achieve very high recall. The
importance of time is also a key theme; models that create
temporal edge embeddings [125], [126] or use pre-trained
Transformers on raw transaction sequences report significant
performance gains over static graph methods by capturing
the behavioral rhythms of phishing attacks, such as fund
consolidation and cash-out [127], [128].
The most effective strategy for Ponzi schemes is
pre-deployment analysis of the contract’s bytecode and
ABI, as these static features provide accurate flags without
needing on-chain history. For phishing, the best results come
from combining graph structure with temporal data, using
heterogeneous GNNs on transaction subgraphs enriched with
time and value features, or employing sequence models like
Transformers. In practice, a two-stage pipeline is effective:
(1) pre-deployment screening for Ponzi-like bytecode
patterns, followed by (2) post-deployment monitoring that
fuses graph structure with temporal cues to detect phishing
activity.
5) CONSENSUS LAYER ATTACKS
A primary concern is the 51% (or majority) attack, where a
colluding group could rewrite transaction history. Empirical
analysis of Bitcoin and Ethereum shows that mining power
is increasingly concentrated among a small number of
entities, challenging the assumption of decentralization and
creating a tangible risk of a 51% attack [153], [154]. This
makes continuous monitoring of miner shares and patterns
in consecutive block production a critical early-warning
system [57], [111].
Beyond direct majority control, more subtle strategic
deviations like selfish mining (SM) also identified where
miners selectively withhold newly found blocks to gain
an advantage. Detection methods focus on the statistical
anomalies this behavior creates, specifically in the frequency
of consecutive block discoveries. One approach uses Miner
Sequence Bootstrapping (MSB) [55], a simulation-based
method, while a more direct statistical test uses the type II
binomial distribution as a null model for honest mining [56].
These methods have identified statistically significant SM
behavior, particularly in Monacoin and Bitcoin Cash.
For selfish-mining, miner and pair run-length tests with
accurate miner attribution (clustering) are the most direct
methods and have revealed real-world anomalies. For 51%
attacks, continuous monitoring of pool shares and simple
burst metrics provides actionable risk indicators, while
generic one-class models offer a lightweight secondary
screen.
C. MUL TI-CHAIN ANOMAL Y DETECTION
While most anomaly-detection work is single-chain, a num-
ber of studies extend their analysis across multiple cryptoas-
sets. These approaches, often comparative rather than fully
integrated, reveal two crucial insights. First, that ‘‘normal’’
on-chain behavior is not uniform across blockchains and
202610 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
second, that illicit actors increasingly operate across these
different ecosystems.
1) COMPARATIVE STRUCTURE & BEHAVIOR
Fundamental differences in network topology are evident
across major blockchains. Monthly transaction networks for
Bitcoin, Ethereum, and Namecoin all exhibit heavy-tailed
degree distributions that deviate from simple power laws,
while network statistics like degree assortativity reveal under-
score structural differences between chains [16]. Building on
this, multi-chain analyses of preferential attachment formal-
ize how ‘‘rich-get-richer’’ dynamics drive hub formation in
Bitcoin and Ethereum [73], while ERC-20 token networks
often exhibit super-linear attachment, which accelerates the
concentration of network activity into a few hubs [72].
This demonstrates that a detector calibrated to one chain’s
topology would likely fail on another, making multi-chain
baselining essential for accurate detection.
2) MULTI-ASSET IRREGULARITIES
Methodologies that screen for macro-level irregularities are
effective at flagging anomalous activity across multiple
assets simultaneously. Robust distance metrics, such as
Mahalanobis distances, can detect anomalies in return
vectors across multiple cryptocurrencies simultaneously [45].
These results highlight periods like the 2021 ‘‘metaverse
boom,’’ where correlated surges flagged joint-market stress.
Similarly, Benford’s Law has been used to identify currencies
whose transaction values deviate from expected statistical
distributions. While Bitcoin and Ethereum conformed, others
such as TENX, VERI, and DOGE showed anomalies linked
to documented scandals [44]. Such macro-level methods
serve as effective early-warning systems, flagging cross-asset
irregularities that warrant deeper on-chain investigation.
3) MINING BEHAVIOR ACROSS PoW CHAINS
Mining-centric anomalies have been measured consistently
across BTC, LTC, ETH, BCH, and MONA. The Miner
Sequence Bootstrapping (MSB) model tests whether a miner
appears too often in consecutive blocks relative to chance,
flagging selfish strategies; a paired MSB extends to mining
cartels [55]. A follow-on study generalizes the test and reports
that Monacoin shows an unusually high fraction of abnormal
miners, with persistent selfish-mining signals; Bitcoin Cash
also exhibits bursts of abnormality, and cartel-like coordi-
nation is observed in MONA, ETH, BCH more than in
BTC and LTC [56]. Monitoring miner-share concentration
adds a complementary perspective and early-warning lens for
51% attack, with empirical miner-share profiles in BTC/ETH
illustrating the practical value of such tracking [57].
4) SCALABLE SUPERVISED PIPELINES ACROSS CHAINS
On the supervised side, GPU-accelerated pipelines deploy
SVM, Random Forest, and Logistic Regression on tens
of millions of Bitcoin transactions and hundreds of thou-
sands of Ethereum accounts, demonstrating that features
+ parallelism yield practical, near-real-time fraud detection
across distinct networks [99].
5) CROSS-CHAIN ANOMALIES
Most of the above treat each chain separately, useful, but
insufficient for cross-ledger flows. A concrete illustration
is terrorist-financing related activity surrounding the Sri
Lanka Easter attacks: an event-study on Bitcoin revealed
abnormal volume through mixers and unregulated exchanges
in the pre-event window; forward tracing then showed
conversion to Ripple (XRP) and continued laundering on
that ledger [54]. This case makes the cross-chain need
explicit: without integrated address/entity linking and real-
time exchange/bridge coverage, sophisticated actors can
exploit siloed detectors.
While multi-chain comparative studies are valuable, they
are insufficient for tracking sophisticated actors who exploit
the seams between ecosystems [155], [156]. The critical
open challenge is moving from parallel, side-by-side analysis
to integrated, entity-centric detection that can follow illicit
activity as it hops across chains, bridges, and exchanges.
D. CHALLENGES AND LIMITATIONS
Several critical and interrelated challenges permeate cryp-
toasset anomaly detection, spanning technical, behavioral,
and regulatory dimensions.
First, the scarcity of accurately labeled data constitutes
a fundamental obstacle. Confirmed illicit addresses are
exceedingly rare relative to legitimate activity, resulting in
severe class imbalance. This imbalance significantly impedes
supervised learning, which depends on high-quality labeled
datasets. The inherent pseudonymity of blockchain systems
further complicates ground-truth validation. Consequently,
researchers must explore semi-supervised, self-supervised,
or active-learning strategies to leverage unlabeled data effec-
tively and enhance model robustness in detecting anomalies.
To alleviate these data constraints, researchers are encouraged
to utilize and contribute to community-maintained repos-
itories such as the GraphSense TagPacks [26] and other
curated, publicly documented label sets. Promoting such
open benchmarks, alongside rigorous reporting standards,
is essential to address label scarcity and ensure reproducible
validation across the field.
Second, scalability and real-time constraints remain press-
ing issues. Blockchain transaction volumes continuously
grow, demanding highly efficient algorithms for anomaly
detection capable of processing massive data flows at high
velocity. Real-time detection at block-time granularity is
essential to prevent financial losses and mitigate ongo-
ing threats like smart contract exploits. Achieving timely,
accurate anomaly detection with sub-second inference and
manageable false-positive rates is computationally intensive,
particularly for advanced methodologies like network analy-
sis or complex machine-learning models. Therefore, further
research into scalable, streaming anomaly-detection methods
VOLUME 13, 2025 202611

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
is crucial. A major practical challenge is the computational
cost of advanced detection methods and its impact on real-
time feasibility. Complex models like graph neural networks
(GNNs) exemplify this issue. The time complexity of a single
graph convolutional layer is often O(|E|F′+|V|FF′), where
|V| is the number of nodes, |E| is the number of edges,
and F/F′ are the input/output feature dimensions. For a full
model with multiple layers, this can scale to O(Kmd+ Knd 2)
where K is the number of layers, m/n are edges (transactions)
/nodes (addresses), and d is the feature dimension [157].
Given that blockchain transaction graphs can contain millions
of nodes and hundreds of millions of edges, this cost can
be prohibitive for real-time model retraining, which is a
key reason why achieving sub-second inference at block-
time granularity remains a significant challenge [158]. While
inference is generally faster than training, latency can still
bottleneck high-frequency scenarios. To mitigate this, many
successful approaches employ subgraph sampling to confine
computation to localized neighborhoods. For instance, the
FraudLens framework [124], using graph restructuring,
reported completing its experiment on the entire Elliptic
dataset in under a minute on a powerful server. To make
GNNs scalable for even larger graphs like Ethereum’s full
transaction history, many successful approaches employ
subgraph sampling strategies. The HGA TE framework[123],
for example, avoids full-graph training by extracting smaller,
localized ‘‘micro interaction subgraphs’’ around target
accounts, which enables efficient mini-batch training while
still capturing relevant behavioral patterns. This highlights
a crucial trade-off: localized subgraph methods are compu-
tationally efficient and can fit on a single GPU, but they
risk missing broader, collective anomalies that are only
visible at a global scale. Full-graph analysis provides more
comprehensive context but at a significant computational
cost. Therefore, real-time deployment feasibility depends
on striking a balance. Current research suggests a hybrid
approach is most practical: using fast, subgraph-based
methods like HGA TE for real-time signal generation, while
potentially running more comprehensive, full-graph analyses
asynchronously to ensure network-wide coverage.
Third, distinguishing benign yet privacy-preserving behav-
iors from malicious obfuscation requires sophisticated
behavioral modeling and nuanced feature engineering.
Users increasingly adopt non-custodial wallets and other
privacy-focused tools for legitimate reasons, such as ide-
ological beliefs or data sovereignty concerns. However,
criminals frequently exploit these tools due to their pseudony-
mous nature and absence of KYC procedures. Effectively
addressing this ambiguity demands advanced analytical
techniques that transcend basic transaction metrics and
incorporate behavioral insights. Expanding on the challenge
of behavioral ambiguity, the field needs a deeper integration
of formal privacy-preserving analytics, where the very
tools designed to protect user privacy can hinder anomaly
detection. Blockchain users increasingly employ mixers,
e.g. CoinJoin protocols or Tornado Cash, and privacy coins
like Zcash which employ techniques like zero-knowledge
proofs (ZKPs) that offer legitimate users enhanced con-
fidentiality. This dual-use ambiguity forces detectors to
distinguish benign privacy-enhanced behavior from mali-
cious laundering. In practice, even privacy mechanisms leave
telltale patterns. For example, mixing services often have
characteristic input/output structures or timing signatures;
simple heuristics exploiting these can identify over 92% of
CoinJoin-style transactions despite their obfuscation [138].
Likewise, analyses of privacy-centric blockchains reveal
trade-offs: Zcash’s zero-knowledge shielded pool provides
anonymity, yet repetitive usage patterns allowed clustering
of 87.5% of addresses and linking a quarter of ‘‘anony-
mous’’ transactions to known entities (miners, founders),
undermining its privacy in practice [80]. These examples
highlight that privacy techniques can be partially pierced
by analytical methods. Similarly, federated learning and
secure multi-party computation (MPC) have been proposed
to let exchanges or nodes jointly train anomaly detectors
without sharing raw data, aligning with data protection
regulations [159], [160]. Such approaches can preserve
confidentiality (each party keeps its own dataset) but come
with higher complexity and potential performance hits
(e.g. communication overhead, convergence issues). Thus,
privacy-preserving analytics in blockchain must balance
detectability vs. privacy: stronger privacy tools (mixers,
encrypted transactions) make it harder to spot illicit behavior,
while privacy-preserving detection frameworks (differential
privacy, federated models) safeguard user data at the cost of
some sensitivity. Effective solutions will likely combine mul-
tiple techniques, for instance, incorporating privacy-aware
heuristics into anomaly models, to ensure that legitimate
privacy is upheld even as illicit abuse of privacy tools is
aggressively detected.
Finally, the challenge of cross-chain anomaly detection
is becoming increasingly pertinent. Attacks such as bridge
exploits and flash-loan manipulations often leave traces
distributed across multiple blockchain ecosystems, compli-
cating detection due to fragmented and siloed data sources.
Enhancing interoperability and developing detection methods
capable of integrating multi-chain data streams are urgent
areas for future research, necessary to effectively identify
complex cross-chain anomalies.
E. FUTURE RESEARCH DIRECTIONS
Addressing these multifaceted challenges requires concerted
research across technical, behavioral, and regulatory dimen-
sions. Several promising research directions emerge clearly.
First, developing hybrid methodologies that integrate
strengths from different detection categories represents a
fertile area for future investigation. Graph Neural Net-
works (GNNs) combining network topology with machine
learning classification exemplify such approaches, merging
structural insights with data-driven detection capabilities.
Similarly, rule-augmented machine learning pipelines that
leverage heuristics to pre-select anomaly candidates for
202612 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
deeper analyses promise both interpretability and enhanced
accuracy. Recent work also explores combining diverse
mathematical anomaly indicators using AI techniques like
Boltzmann machines to create more robust signals or
integrating predictive AI with facilitation AI within organi-
zational frameworks like DAOs [161], [162]. Formalizing
design patterns and best practices for these hybrid systems
could streamline development and improve reliability. This
susceptibility highlights a critical operational challenge as
attackers continuously evolve their strategies to bypass static
filters, anomaly detection models inevitably suffer from
drift and performance degradation. Consequently, deploying
adaptive retraining pipelines and continuous drift detection
mechanisms is as important as the initial model selection to
mitigate these adversarial shifts.
Recently, emerging paradigms like Graph Foundation
Models (GFMs) are opening new avenues in graph-based
anomaly detection. GFMs represent a paradigm shift in
graph machine learning. Reference [163] proposes a large-
scale pre-training framework on heterogeneous transaction
graphs. The results show that GFMs can be fine-tuned
to various tasks, including anomaly detection, achieving
strong accuracy with minimal supervision. The promise
of emergent capabilities, e.g., in-context learning, zero-
shot generation, and task homogenization across node,
edge, and graph levels, could help unify the fragmented
landscape of graph-based anomaly detection approaches.
Building on this concept, GNN+LLM hybrid approach [164]
fuses blockchain transaction graphs with cross-chain textual
signals. By leveraging pre-trained language models alongside
structural embeddings, they capture anomalies hidden both in
graph topologies and semantic patterns, promising especially
for detecting fraudulent behaviors embedded in multi-chain
settings.
Second, advancing methods robust to label scarcity and
severe data imbalance is critical. Techniques such as semi-
supervised, self-supervised, and transfer learning can exploit
unlabeled or partially labeled data, significantly improving
anomaly detection in data-scarce environments. Furthermore,
synthetic data generation approaches, designed to emulate
diverse legitimate and illicit behaviors, could further alleviate
data constraints and facilitate rigorous model evaluation.
Third, improving the interpretability of sophisticated
machine learning models remains vital. Advanced ML
and deep learning models often lack transparency despite
their high accuracy. Research should prioritize Explainable
AI (XAI) techniques tailored specifically for cryptoas-
set anomaly detection, employing attention mechanisms,
saliency mapping, or post-hoc interpretation methods to
elucidate the decision-making process of these powerful yet
opaque models.
Fourth, developing scalable, real-time anomaly detection
systems capable of processing high-throughput blockchain
data streams is paramount. Techniques leveraging online
learning, reinforcement learning, and hardware accelera-
tion (e.g., GPUs, TPUs, distributed computing) warrant
exploration to achieve timely, accurate detection at the scale
and speed required by contemporary blockchain networks.
Finally, establishing standardized benchmarks and datasets
is essential to enabling fair, consistent comparisons across
methods. Creating labeled, timestamped datasets covering
major cryptoassets and cross-chain interactions, accompa-
nied by standardized evaluation metrics like precision-recall
curves and time-to-detect metrics, would significantly
advance methodological rigor and facilitate cross-study
comparisons.
V. CONCLUSION
Growth has transformed the cryptoasset ecosystem into
a major financial market involving substantial economic
activity and a large Decentralized Finance (DeFi) sector.
Correspondingly, the attack surface for fraud, market manip-
ulation, and protocol-level exploits has expanded. Globally,
regulatory frameworks are also maturing, imposing greater
scrutiny and evolving compliance demands, which includes
exploring new concepts of secondary liability [165].
This SoK has mapped 103 studies on cryptoasset
anomaly detection across statistical analysis, network anal-
ysis, machine learning and heuristic-based methods. The
comparative analysis reveals inherent trade-offs: statistical
analysis offers interpretability but faces data distribution
sensitivity, network analysis leverages topology effectively
but struggles with scalability, machine learning provides
powerful pattern recognition but often requires significant
labeled data and can lack transparency. At the same time,
heuristic-based methods excel with known threats via expert
rules but fail against novel patterns and require ongoing
updates. Across these approaches, persistent challenges
hinder progress, notably the scarcity of labeled data and
class imbalance, the computational demands of real-time
detection at scale, the ambiguity between privacy techniques
and malicious obfuscation, and the complexity of cross-chain
activity analysis.
Addressing these significant challenges suggests several
key directions for future research. Promising directions
include developing hybrid methodologies like GNNs or
rule-augmented ML, advancing techniques robust to label
scarcity such as self-supervised learning and synthetic
data generation, enhancing model interpretability through
Explainable AI, creating highly scalable real-time systems,
and crucially, establishing standardized benchmarks and
datasets for rigorous comparison. Advancing cryptoasset
anomaly detection is vital not merely as an academic
exercise but as a crucial requirement for market integrity,
user protection, and the responsible integration of digital
assets into the global financial system, demanding robust,
explainable, and adaptive solutions.
REFERENCES
[1] S. Nakamoto, ‘‘Bitcoin: A peer-to-peer electronic cash system,’’ White
paper, 2008. [Online]. Available: https://bitcoin.org/bitcoin.pdf
VOLUME 13, 2025 202613

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
[2] B. A. Tama, B. J. Kweka, Y . Park, and K.-H. Rhee, ‘‘A critical review of
blockchain and its current applications,’’ in Proc. Int. Conf. Electr . Eng.
Comput. Sci. (ICECOS), Aug. 2017, pp. 109–113.
[3] R. Zhang, R. Xue, and L. Liu, ‘‘Security and privacy on
blockchain,’’ ACM Comput. Surv., vol. 52, no. 3, pp. 1–34,
Jul. 2019.
[4] O. Ali, M. Ally, and Y . Dwivedi, ‘‘The state of play of blockchain
technology in the financial services sector: A systematic
literature review,’’ Int. J. Inf. Manage., vol. 54, Oct. 2020,
Art. no. 102199.
[5] M. Javaid, A. Haleem, R. P . Singh, R. Suman, and S. Khan, ‘‘A review of
blockchain technology applications for financial services,’’BenchCouncil
Trans. Benchmarks, vol. 2, no. 3, 2022, Art. no. 100073.
[6] A. Babaei, M. Khedmati, M. R. Akbari Jokar, and E. B. Tirkolaee,
‘‘Designing an integrated blockchain-enabled supply chain
network under uncertainty,’’ Sci. Rep., vol. 13, no. 1, p. 3928,
Mar. 2023.
[7] P . K. Wan, L. Huang, and H. Holtskog, ‘‘Blockchain-enabled information
sharing within a supply chain: A systematic literature review,’’ IEEE
Access, vol. 8, pp. 49645–49656, 2020.
[8] M. A. N. Agi and A. K. Jha, ‘‘Blockchain technology in the supply chain:
An integrated theoretical perspective of organizational adoption,’’ Int.
J. Prod. Econ., vol. 247, May 2022, Art. no. 108458.
[9] S. Shamshad, K. Mahmood, S. Kumari, and C.-M. Chen, ‘‘A secure
blockchain-based e-health records storage and sharing scheme,’’ J. Inf.
Secur . Appl., vol. 55, Dec. 2020, Art. no. 102590.
[10] A. Dubovitskaya, Z. Xu, S. Ryu, M. Schumacher, and F. Wang, ‘‘Secure
and trustable electronic medical records sharing using blockchain,’’ in
Proc. AMIA Annu. Symp., 2018, pp. 650–659.
[11] A. Bogner, M. Chanson, and A. Meeuw, ‘‘A decentralised sharing app
running a smart contract on the Ethereum blockchain,’’ in Proc. 6th Int.
Conf. Internet Things, Nov. 2016, pp. 177–178.
[12] L. Marchesi, M. Marchesi, R. Tonelli, and M. I. Lunesu, ‘‘A blockchain
architecture for industrial applications,’’ Blockchain: Res. Appl., vol. 3,
no. 4, Dec. 2022, Art. no. 100088.
[13] F. M. De Collibus, C. Campajola, and C. J. Tessone, ‘‘The microvelocity
of money in Ethereum,’’ EPJ Data Sci., vol. 14, no. 1, p. 11, Feb. 2025.
[14] T. Y an, Y . H. Kim, S. Li, T. Kim, and C. J. Tessone, ‘‘Applying Basel
framework to estimate systemic risk of decentralized finance,’’ Available
at SSRN 5234709, 2025.
[15] B. Kraner, L. Pennella, N. V allarano, and C. J. Tessone, ‘‘Money in
motion: Micro-velocity and usage of Ethereums liquid staking tokens,’’
2025, arXiv:2508.15391.
[16] J. Liang, L. Li, and D. Zeng, ‘‘Evolutionary dynamics of cryptocurrency
transaction networks: An empirical study,’’ PLoS ONE, vol. 13, no. 8,
Aug. 2018, Art. no. e0202202.
[17] J. Wu, J. Liu, Y . Zhao, and Z. Zheng, ‘‘Analysis of cryptocurrency
transactions from a network perspective: An overview,’’J. Netw. Comput.
Appl., vol. 190, Sep. 2021, Art. no. 103139.
[18] T. Y an and C. J. Tessone, ‘‘Network analysis of uniswap: Central-
ization and fragility in the decentralized exchange market,’’ 2025,
arXiv:2503.07834.
[19] W. Chen, J. Wu, Z. Zheng, C. Chen, and Y . Zhou, ‘‘Market manipulation
of Bitcoin: Evidence from mining the Mt. Gox transaction network,’’
in Proc. IEEE Conf. Comput. Commun. (INFOCOM), Apr. 2019,
pp. 964–972.
[20] T. Gagliardoni. (2021). The Poly Network Hack Explained. Accessed:
Mar. 7, 2025. [Online]. Available: https://research.kudelskisecurity.
com/2021/08/12/the-poly-network-hack-explained/
[21] B. H. A. Khattak, I. Shafi, C. H. Rashid, M. Safran, S. Alfarhood, and I.
Ashraf, ‘‘Profitability trend prediction in crypto financial markets using
Fibonacci technical indicator and hybrid CNN model,’’ J. Big Data ,
vol. 11, no. 1, p. 58, Apr. 2024.
[22] A. A. Monrat, O. Schelén, and K. Andersson, ‘‘A survey of blockchain
from the perspectives of applications, challenges, and opportunities,’’
IEEE Access, vol. 7, pp. 117134–117151, 2019.
[23] D. Tapscott and A. Tapscott, Blockchain Revolution: How the Technology
Behind Bitcoin is Changing Money, Business, and the World. Portfolio,
2016.
[24] M. Bolz, K. Brundler, L. Kane, P . Patsias, L. Tessendorf, K. Gogol,
T. Kim, and C. Tessone, ‘‘Machine learning-based detection of pump-
and-dump schemes in real-time,’’ 2024, arXiv:2412.18848.
[25] B. Öz, B. Kraner, N. V allarano, B. S. Kruger, F. Matthes, and
C. J. Tessone, ‘‘Time moves faster when there is nothing you anticipate:
The role of time in MEV rewards,’’ in Proc. Workshop Decentralized
Finance Secur ., Nov. 2023, pp. 1–8.
[26] B. Haslhofer, M. Dragaschnig, R. Stutz, M. Romiti, and
G. Gomez. (May 2022). Graphsense Tagpacks. [Online]. Available:
https://github.com/graphsense/graphsense-tagpacks
[27] A.-L. Barabási, Network Science. Cambridge, U.K.: Cambridge Univ.
Press, 2016.
[28] I. Goodfellow, Y . Bengio, and A. Courville, Deep Learning. Cambridge,
MA, USA: MIT Press, 2016.
[29] S. L. Brunton and J. N. Kutz, Data-Driven Science and Engineering:
Machine Learning, Dynamical Systems, and Control. Cambridge, U.K.:
Cambridge Univ. Press, 2019.
[30] Z. Wu, S. B. J. Kan, R. D. Lewis, B. J. Wittmann, and F. H. Arnold,
‘‘Machine learning-assisted directed protein evolution with combinatorial
libraries,’’ Proc. Nat. Acad. Sci. USA, vol. 116, no. 18, pp. 8852–8858,
Apr. 2019.
[31] J. Jumper et al., ‘‘Highly accurate protein structure prediction with
AlphaFold,’’Nature, vol. 596, no. 7873, pp. 583–589, Aug. 2021.
[32] M. van Kempen, S. S. Kim, C. Tumescheit, M. Mirdita, J. Lee,
C. L. M. Gilchrist, J. Söding, and M. Steinegger, ‘‘Fast and accurate
protein structure search with foldseek,’’Nature Biotechnol., vol. 42, no. 2,
pp. 243–246, Feb. 2024.
[33] H. Jeckel, E. Jelli, R. Hartmann, P . K. Singh, R. Mok, J. F. Totz,
L. Vidakovic, B. Eckhardt, J. Dunkel, and K. Drescher, ‘‘Learning
the space-time phase diagram of bacterial swarm expansion,’’
Proc. Nat. Acad. Sci. USA, vol. 116, no. 5, pp. 1489–1494,
Jan. 2019.
[34] K. Sankaewtong, J. J. Molina, and R. Y amamoto, ‘‘Autonomous
navigation of smart microswimmers in non-uniform flow fields,’’ Phys.
Fluids, vol. 36, no. 4, Apr. 2024, Art. no. 041902.
[35] K. Sankaewtong, J. J. Molina, M. S. Turner, and R. Y amamoto, ‘‘Learning
to swim efficiently in a nonuniform flow field,’’ Phys. Rev. E, Stat.
Phys. Plasmas Fluids Relat. Interdiscip. Top., vol. 107, no. 6, Jun. 2023,
Art. no. 065102.
[36] C. V . Amrutha, C. Jyotsna, and J. Amudha, ‘‘Deep learning approach
for suspicious activity detection from surveillance video,’’ in Proc.
2nd Int. Conf. Innov. Mech. Ind. Appl. (ICIMIA) , Mar. 2020,
pp. 335–339.
[37] B. M. Lake and M. Baroni, ‘‘Human-like systematic generalization
through a meta-learning neural network,’’ Nature, vol. 623, no. 7985,
pp. 115–121, Nov. 2023.
[38] G. Aceto, D. Ciuonzo, A. Montieri, and A. Pescape, ‘‘Mobile encrypted
traffic classification using deep learning: Experimental evaluation,
lessons learned, and challenges,’’ IEEE Trans. Netw. Service Manage.,
vol. 16, no. 2, pp. 445–458, Jun. 2019.
[39] P . Bannigan, Z. Bao, R. J. Hickman, M. Aldeghi, F. Häse, A. Aspuru-
Guzik, and C. Allen, ‘‘Machine learning models to accelerate the design
of polymeric long-acting injectables,’’ Nature Commun., vol. 14, no. 1,
p. 35, Jan. 2023.
[40] E. C. L. de Oliveira, K. Santana, L. Josino, A. H. Lima e Lima, and
C. de Souza de Sales Júnior, ‘‘Predicting cell-penetrating peptides using
machine learning algorithms and navigating in their chemical space,’’Sci.
Rep., vol. 11, no. 1, p. 7628, Apr. 2021.
[41] H. Hu, J. Xu, M. Liu, and M. K. Lim, ‘‘V accine supply chain management:
An intelligent system utilizing blockchain, IoT and machine learning,’’
J. Bus. Res., vol. 156, Feb. 2023, Art. no. 113480.
[42] A. Devlin, J. Kossen, H. Goldie-Jones, and A. Y ang, ‘‘Global green
hydrogen-based steel opportunities surrounding high quality renewable
energy and iron ore deposits,’’ Nature Commun., vol. 14, no. 1, p. 2578,
May 2023.
[43] E. Akyildirim, M. Gambara, J. Teichmann, and S. Zhou, ‘‘Appli-
cations of signature methods to market anomaly detection,’’ 2022,
arXiv:2201.02441.
[44] J. Vicic and A. Tosic, ‘‘Application of Benford’s law on cryptocur-
rencies,’’ J. Theor . Appl. Electron. Commerce Res., vol. 17, no. 1,
pp. 313–326, 2022.
[45] G. Bae and J. H. Kim, ‘‘Observing cryptocurrencies through robust
anomaly scores,’’ Entropy, vol. 24, no. 11, p. 1643, 2022.
[46] G. E. P . Box, G. M. Jenkins, G. C. Reinsel, and G. M. Ljung, Time Series
Analysis: F orecasting and Control. Hoboken, NJ, USA: Wiley, 2015.
202614 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
[47] F. Akba, I. T. Medeni, M. S. Guzel, and I. Askerzade, ‘‘Manipulator
detection in cryptocurrency markets based on forecasting anomalies,’’
IEEE Access, vol. 9, pp. 108819–108831, 2021.
[48] J. H. Park and Y . Sohn, ‘‘Detecting structural changes in longitudinal
network data,’’ Bayesian Anal., vol. 15, no. 1, pp. 133–157, Mar. 2020.
[49] D. C. Montgomery, Statistical Quality Control: A Modern Approach.
Hoboken, NJ, USA: Wiley, 2020.
[50] C. A. Lowry, W. H. Woodall, C. W. Champ, and S. E. Rigdon,
‘‘A multivariate exponentially weighted moving average control chart,’’
Technometrics, vol. 34, no. 1, pp. 46–53, Feb. 1992.
[51] P . D. Hoff, ‘‘Multilinear tensor regression for longitudinal relational
data,’’ Ann. Appl. Statist., vol. 9, no. 3, pp. 1169–1193, Sep. 2015.
[52] K. Sabri-Laghaie, S. Jafarzadeh Ghoushchi, F. Elhambakhsh, and
A. Mardani, ‘‘Monitoring blockchain cryptocurrency transactions
to improve the trustworthiness of the fourth industrial
revolution (Industry 4.0),’’ Algorithms, vol. 13, no. 12, p. 312,
Nov. 2020.
[53] Y . Faqir-Rhazoui, M.-J. Ariza-Garzón, J. Arroyo, and S. Hassan, ‘‘Effect
of the gas price surges on user activity in the DAOs of the Ethereum
blockchain,’’ in Proc. Extended Abstr . CHI Conf. Hum. Factors Comput.
Syst., New Y ork, NY , USA, May 2021, pp. 1–7.
[54] D. Amiram, B. N. Jørgensen, and D. Rabetti, ‘‘Coins for bombs: The
predictive ability of on-chain transfers for terrorist attacks,’’J. Accounting
Res., vol. 60, no. 2, pp. 427–466, May 2022.
[55] S.-N. Li, Z. Y ang, and C. J. Tessone, ‘‘Proof-of-work cryptocurrency
mining: A statistical approach to fairness,’’ in Proc. IEEE/CIC Int. Conf.
Commun. China (ICCC Workshops), Aug. 2020, pp. 156–161.
[56] S.-N. Li, C. Campajola, and C. J. Tessone, ‘‘Statistical detection of selfish
mining in proof-of-work blockchain systems,’’ Sci. Rep., vol. 14, no. 1,
p. 6251, Mar. 2024.
[57] F. A. Aponte-Novoa, A. L. S. Orozco, R. Villanueva-Polanco, and
P . Wightman, ‘‘The 51% attack on blockchains: A mining
behavior study,’’ IEEE Access, vol. 9, pp. 140549–140564,
2021.
[58] M. Lischke and B. Fabian, ‘‘Analyzing the Bitcoin network: The first four
years,’’ Future Internet, vol. 8, no. 1, p. 7, Mar. 2016.
[59] B. Tao, I. W.-H. Ho, and H.-N. Dai, ‘‘Complex network analysis of the
Bitcoin blockchain network,’’ in Proc. IEEE Int. Symp. Circuits Syst.
(ISCAS), May 2021, pp. 1–5.
[60] B. Tao, H.-N. Dai, J. Wu, I. W.-H. Ho, Z. Zheng, and C. F. Cheang,
‘‘Complex network analysis of the Bitcoin transaction network,’’ IEEE
Trans. Circuits Syst. II, Exp. Briefs , vol. 69, no. 3, pp. 1009–1013,
Mar. 2022.
[61] V . Chang, K. Hall, Q. A. Xu, L. M. T. Doan, and Z. Wang, ‘‘A
social network analysis of two networks: Adolescent school network
and Bitcoin trader network,’’ Decis. Anal. J., vol. 3, Jun. 2022,
Art. no. 100065.
[62] G. Rosa and R. Pareschi, ‘‘Tether: A study on bubble-networks,’’
Frontiers Blockchain, vol. 4, Aug. 2021, Art. no. 686484.
[63] Z. Di, G. Wang, L. Jia, and Z. Chen, ‘‘Bitcoin transactions as a graph,’’
IET Blockchain, vol. 2, nos. 3–4, pp. 57–66, Sep. 2022.
[64] W. Aiello, F. Chung, and L. Lu, ‘‘A random graph model for power law
graphs,’’ Exp. Math., vol. 10, no. 1, pp. 53–66, Jan. 2001.
[65] P . G. Buckley and D. Osthus, ‘‘Popularity based random graph models
leading to a scale-free degree sequence,’’ Discrete Math., vol. 282,
nos. 1–3, pp. 53–68, May 2004.
[66] D. Lin, J. Wu, Q. Y uan, and Z. Zheng, ‘‘Modeling and understanding
Ethereum transaction records via a complex network approach,’’ IEEE
Trans. Circuits Syst. II, Exp. Briefs, vol. 67, no. 11, pp. 2737–2741,
Nov. 2020.
[67] Z. Ao, L. William Cong, G. Horvath, and L. Zhang, ‘‘Is decentralized
finance actually decentralized? A social network analysis of the aave
protocol on the Ethereum blockchain,’’ 2022, arXiv:2206.08401.
[68] F. M. De Collibus, M. Piškorec, A. Partida, and C. J. Tessone, ‘‘The
structural role of smart contracts and exchanges in the centralisation of
Ethereum-based cryptoassets,’’Entropy, vol. 24, no. 8, p. 1048, Jul. 2022.
[69] A. Alamsyah and I. F. Muhammad, ‘‘Unraveling the crypto market:
A journey into decentralized finance transaction network,’’ Digit. Bus.,
vol. 4, no. 1, Jun. 2024, Art. no. 100074.
[70] D. Kondor, M. Pósfai, I. Csabai, and G. V attay, ‘‘Do the rich get richer?
An empirical analysis of the Bitcoin transaction network,’’ PLoS ONE,
vol. 9, no. 2, pp. 1–10, Feb. 2014.
[71] A. Aspembitova, L. Feng, V . Melnikov, and L. Y . Chew, ‘‘Fitness
preferential attachment as a driving mechanism in Bitcoin
transaction network,’’ PLoS ONE, vol. 14, no. 8, pp. 1–20,
Aug. 2019.
[72] F. M. De Collibus, A. Partida, M. Piškorec, and C. J. Tessone, ‘‘Het-
erogeneous preferential attachment in key Ethereum-based cryptoassets,’’
Frontiers Phys., vol. 9, Oct. 2021, Art. no. 720708.
[73] D. Kondor, N. Bulatovic, J. Stéger, I. Csabai, and G. V attay, ‘‘The
rich still get richer: Empirical comparison of preferential attachment via
linking statistics in Bitcoin and Ethereum,’’ Frontiers Blockchain, vol. 4,
Aug. 2021, Art. no. 668510.
[74] A. Bovet, C. Campajola, F. Mottes, V . Restocchi, N. V allarano,
T. Squartini, and C. J. Tessone, ‘‘The evolving liaisons between the
transaction networks of Bitcoin and its price dynamics,’’ in Proc. JPS
Conf., vol. 40, Sep. 2023, Paper 011002.
[75] D. Kondor, I. Csabai, J. Szüle, M. Pósfai, and G. V attay, ‘‘Inferring the
interplay between network structure and market effects in Bitcoin,’’ New
J. Phys., vol. 16, no. 12, Dec. 2014, Art. no. 125003.
[76] A. Chakraborty, T. Hatsuda, and Y . Ikeda, ‘‘Projecting XRP price burst
by correlation tensor spectra of transaction networks,’’ Sci. Rep., vol. 13,
no. 1, p. 4718, Mar. 2023.
[77] Y . Wang and H. Wang, ‘‘Using networks and partial differential equations
to forecast Bitcoin price movement,’’ Chaos: Interdiscipl. J. Nonlinear
Sci., vol. 30, no. 7, Jul. 2020, Art. no. 073127.
[78] Z. Wang, R. Zhang, Y . Sun, H. Ding, and Q. Lv, ‘‘Can lightning network’s
autopilot function use BA model as the underlying network?’’ Frontiers
Phys., vol. 9, Jan. 2022, Art. no. 794160.
[79] B. Huang, J. Liu, J. Wu, Q. Li, and H. Lin, ‘‘Temporal analysis
of transaction ego networks with different labels on Ethereum,’’
in Proc. IEEE Int. Symp. Circuits Syst. (ISCAS), May 2022,
pp. 3517–3521.
[80] Z. Zhang, W. Li, H. Liu, and J. Liu, ‘‘A refined analysis of
zcash anonymity,’’ IEEE Access, vol. 8, pp. 31845–31853,
2020.
[81] M. Jourdan, S. Blandin, L. Wynter, and P . Deshpande, ‘‘Characterizing
entities in the Bitcoin blockchain,’’ in Proc. IEEE Int. Conf. Data Mining
Workshops (ICDMW), Nov. 2018, pp. 55–62.
[82] Y . Wu, F. Tao, L. Liu, J. Gu, J. Panneerselvam, R. Zhu, and
M. N. Shahzad, ‘‘A Bitcoin transaction network analytic method for future
blockchain forensic investigation,’’ IEEE Trans. Netw. Sci. Eng., vol. 8,
no. 2, pp. 1230–1241, Apr. 2021.
[83] S. Morishima, ‘‘Scalable anomaly detection in blockchain using
graphics processing unit,’’ Comput. Electr . Eng., vol. 92, Jun. 2021,
Art. no. 107087.
[84] Q. Fu, D. Lint, Y . Cao, and J. Wu, ‘‘Does money laundering on Ethereum
have traditional traits?’’ in Proc. IEEE Int. Symp. Circuits Syst. (ISCAS),
May 2023, pp. 1–5.
[85] J. Wang, P . Chen, X. Xu, J. Wu, M. Shen, Q. Xuan, and X. Y ang,
‘‘TSGN: Transaction subgraph networks assisting phishing detection in
Ethereum,’’ 2022, arXiv:2208.12938.
[86] Y . Huang, H. Wang, L. Wu, G. Tyson, X. Luo, R. Zhang, X. Liu,
G. Huang, and X. Jiang, ‘‘Characterizing EOSIO blockchain,’’ 2020,
arXiv:2002.05369.
[87] Y . Huang, H. Wang, L. Wu, G. Tyson, X. Luo, R. Zhang, X. Liu, G. Huang,
and X. Jiang, ‘‘Understanding (Mis)behavior on the EOSIO blockchain,’’
Proc. ACM Meas. Anal. Comput. Syst., vol. 4, no. 2, pp. 1–28,
Jun. 2020.
[88] T. Ashfaq, R. Khalid, A. S. Y ahaya, S. Aslam, A. T. Azar, S.
Alsafari, and I. A. Hameed, ‘‘A machine learning and blockchain based
efficient fraud detection mechanism,’’ Sensors, vol. 22, no. 19, p. 7162,
Sep. 2022.
[89] N. Nayyer, N. Javaid, M. Akbar, A. Aldegheishem, N. Alrajeh, and
M. Jamil, ‘‘A new framework for fraud detection in Bitcoin transactions
through ensemble stacking model in smart cities,’’ IEEE Access, vol. 11,
pp. 90916–90938, 2023.
[90] M. Ghosh, D. Ghosh, R. Halder, and J. Chandra, ‘‘Investigating the
impact of structural and temporal behaviors in Ethereum phishing
users detection,’’ Blockchain: Res. Appl., vol. 4, no. 4, Dec. 2023,
Art. no. 100153.
[91] Y . Hu, S. Seneviratne, K. Thilakarathna, K. Fukuda, and A. Seneviratne,
‘‘Characterizing and detecting money laundering activities on the Bitcoin
network,’’ 2019, arXiv:1912.12060.
VOLUME 13, 2025 202615

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
[92] C. Oliveira, J. Torres, M. I. Silva, D. Aparício, J. Tiago Ascensão, and
P . Bizarro, ‘‘GuiltyWalker: Distance to illicit nodes in the Bitcoin
network,’’ 2021, arXiv:2102.05373.
[93] W. Chen, Z. Zheng, J. Cui, E. Ngai, P . Zheng, and Y . Zhou, ‘‘Detecting
Ponzi schemes on Ethereum: Towards healthier blockchain technology,’’
in Proc. World Wide Web Conf. World Wide Web (WWW), 2018,
pp. 1409–1418.
[94] W. Chen, Z. Zheng, E. C.-H. Ngai, P . Zheng, and Y . Zhou, ‘‘Exploiting
blockchain data to detect smart Ponzi schemes on Ethereum,’’ IEEE
Access, vol. 7, pp. 37575–37586, 2019.
[95] G. Ibba, G. A. Pierro, and M. Di Francesco, ‘‘Evaluating machine-
learning techniques for detecting smart Ponzi schemes,’’ in Proc.
IEEE/ACM 4th Int. Workshop Emerg. Trends Softw. Eng. Blockchain
(WETSEB), May 2021, pp. 34–40.
[96] C. Jin, J. Jin, J. Zhou, J. Wu, and Q. Xuan, ‘‘Heterogeneous
feature augmentation for Ponzi detection in Ethereum,’’ IEEE
Trans. Circuits Syst. II, Exp. Briefs , vol. 69, no. 9, pp. 3919–3923,
Sep. 2022.
[97] I. J. Onu, A. E. Omolara, M. Alawida, O. I. Abiodun, and
A. Alabdultif, ‘‘Detection of Ponzi scheme on Ethereum using
machine learning algorithms,’’ Sci. Rep., vol. 13, no. 1, p. 18403,
Oct. 2023.
[98] K. Toyoda, P . Takis Mathiopoulos, and T. Ohtsuki, ‘‘A novel methodology
for HYIP Operators’ Bitcoin addresses identification,’’ IEEE Access,
vol. 7, pp. 74835–74848, 2019.
[99] Y . Elmougy and O. Manzi, ‘‘Anomaly detection on Bitcoin, Ethereum
networks using GPU-accelerated machine learning methods,’’ in
Proc. 31st Int. Conf. Comput. Theory Appl. (ICCTA), Dec. 2021,
pp. 166–171.
[100] Y . Elmougy and L. Liu, ‘‘Demystifying fraudulent transactions and
illicit nodes in the Bitcoin network for financial forensics,’’ in Proc.
29th ACM SIGKDD Conf. Knowl. Discovery Data Mining, Aug. 2023,
pp. 3979–3990.
[101] R. Mittal and M. P . S. Bhatia, ‘‘Detection of suspicious or un-trusted users
in crypto-currency financial trading applications,’’ Int. J. Digit. Crime
F orensics, vol. 13, no. 1, pp. 79–93, Jan. 2021.
[102] X. F. Liu, H.-H. Ren, S.-H. Liu, and X.-J. Jiang, ‘‘Characterizing
key agents in the cryptocurrency economy through blockchain
transaction analysis,’’ EPJ Data Sci., vol. 10, no. 1, p. 21,
May 2021.
[103] J. Liu, C. Yin, H. Wang, X. Wu, D. Lan, L. Zhou, and C. Ge,
‘‘Graph embedding-based money laundering detection for Ethereum,’’
Electronics, vol. 12, no. 14, p. 3180, Jul. 2023.
[104] Y .-J. Lin, P .-W. Wu, C.-H. Hsu, I.-P . Tu, and S.-W. Liao, ‘‘An
evaluation of Bitcoin address classification based on transaction history
summarization,’’ in Proc. IEEE Int. Conf. Blockchain Cryptocurrency
(ICBC), May 2019, pp. 302–310.
[105] D. Lin, J. Wu, Q. Y uan, and Z. Zheng, ‘‘T-EDGE: Temporal WEighted
MultiDiGraph embedding for Ethereum transaction network analysis,’’
Frontiers Phys., vol. 8, p. 204, Jun. 2020.
[106] M. Hasan, M. S. Rahman, H. Janicke, and I. H. Sarker, ‘‘Detecting
anomalies in blockchain transactions using machine learning classifiers
and explainability analysis,’’ Blockchain: Res. Appl., vol. 5, no. 3,
Sep. 2024, Art. no. 100207.
[107] R. O. Ogundokun, M. O. Arowolo, R. Damaševičius, and S.
Misra, ‘‘Phishing detection in blockchain transaction networks
using ensemble learning,’’ Telecom, vol. 4, no. 2, pp. 279–297,
May 2023.
[108] P . M. Monamo, V . Marivate, and B. Twala, ‘‘Unsupervised learning for
robust Bitcoin fraud detection,’’ in Proc. Inf. Secur . South Africa (ISSA),
Aug. 2016, pp. 129–134.
[109] T. Pham and S. Lee, ‘‘Anomaly detection in Bitcoin network using
unsupervised learning methods,’’ 2016, arXiv:1611.03941.
[110] T. Pham and S. Lee, ‘‘Anomaly detection in the Bitcoin system—A
network perspective,’’ 2016, arXiv:1611.03942.
[111] S. Sayadi, S. Ben Rejeb, and Z. Choukair, ‘‘Anomaly detection
model over blockchain electronic transactions,’’ in Proc. 15th Int.
Wireless Commun. Mobile Comput. Conf. (IWCMC), Jun. 2019,
pp. 895–900.
[112] D. Chaudhari, R. Agarwal, and S. K. Shukla, ‘‘Towards malicious
address identification in Bitcoin,’’ in Proc. IEEE Int. Conf. Blockchain
(Blockchain), Dec. 2021, pp. 425–432.
[113] M. J. Shayegan, H. R. Sabor, M. Uddin, and C.-L. Chen, ‘‘A
collective anomaly detection technique to detect crypto wallet
frauds on Bitcoin network,’’ Symmetry, vol. 14, no. 2, p. 328,
Feb. 2022.
[114] J. Wu, Q. Y uan, D. Lin, W. Y ou, W. Chen, C. Chen, and Z. Zheng, ‘‘Who
are the phishers? Phishing scam detection on Ethereum via network
embedding,’’ IEEE Trans. Syst., Man, Cybern., Syst., vol. 52, no. 2,
pp. 1156–1166, Feb. 2022.
[115] I. Alarab and S. Prakoonwit, ‘‘Graph-based LSTM for anti-money
laundering: Experimenting temporal graph convolutional network with
Bitcoin data,’’ Neural Process. Lett., vol. 55, no. 1, pp. 689–707,
Feb. 2023.
[116] C. Guo, S. Zhang, P . Zhang, M. Alkubati, and J. Song, ‘‘LB-GLA T:
Long-term bi-graph layer attention convolutional network for anti-money
laundering in transactional blockchain,’’ Mathematics, vol. 11, no. 18,
p. 3927, Sep. 2023.
[117] B. Han, Y . Wei, Q. Wang, F. M. D. Collibus, and C. J. Tessone, ‘‘MT2AD:
Multi-layer temporal transaction anomaly detection in Ethereum net-
works with GNN,’’ Complex Intell. Syst., vol. 10, no. 1, pp. 613–626,
Feb. 2024.
[118] W. Wei, Q. Zhang, and L. Liu, ‘‘Bitcoin transaction forecasting with deep
network representation learning,’’ IEEE Trans. Emerg. Topics Comput.,
vol. 9, no. 3, pp. 1359–1371, Jul. 2021.
[119] S. Hu, Z. Zhang, B. Luo, S. Lu, B. He, and L. Liu, ‘‘BERT4ETH:
A pre-trained transformer for Ethereum fraud detection,’’ in
Proc. ACM Web Conf., New Y ork, NY , USA, Apr. 2023,
pp. 2189–2197.
[120] A. Song, E. Seo, and H. Kim, ‘‘Anomaly V AE-transformer: A deep
learning approach for anomaly detection in decentralized finance,’’ IEEE
Access, vol. 11, pp. 98115–98131, 2023.
[121] H. Kanezashi, T. Suzumura, X. Liu, and T. Hirofuchi, ‘‘Ethereum
fraud detection with heterogeneous graph neural networks,’’ 2022,
arXiv:2203.12363.
[122] Z. Liu, D. Y ang, S. Wang, and H. Su, ‘‘Adaptive multi-channel Bayesian
graph attention network for IoT transaction security,’’ Digit. Commun.
Netw., vol. 10, no. 3, pp. 631–644, Jun. 2024.
[123] J. Zhou, C. Hu, J. Chi, J. Wu, M. Shen, and Q. Xuan, ‘‘Behavior-
aware account de-anonymization on Ethereum interaction graph,’’
IEEE Trans. Inf. F orensics Security, vol. 17, pp. 3433–3448,
2022.
[124] J. Nicholls, A. Kuppa, and N.-A. Le-Khac, ‘‘FraudLens: Graph
structural learning for Bitcoin illicit activity identification,’’ in Proc.
Annu. Comput. Secur . Appl. Conf., New Y ork, NY , USA, Dec. 2023,
pp. 324–336.
[125] A. Xiong, Y . Tong, C. Jiang, S. Guo, S. Shao, J. Huang, W. Wang, and
B. Qi, ‘‘Ethereum phishing detection based on graph neural
networks,’’ IET Blockchain, vol. 4, no. 3, pp. 226–234,
Sep. 2024.
[126] X. Zhou, W. Y ang, and X. Tian, ‘‘Detecting phishing accounts on
Ethereum based on transaction records and EGA T,’’Electronics, vol. 12,
no. 4, p. 993, Feb. 2023.
[127] T. Y u, X. Chen, Z. Xu, and J. Xu, ‘‘MP-GCN: A phishing nodes detection
approach via graph convolution network for Ethereum,’’ Appl. Sci.,
vol. 12, no. 14, p. 7294, Jul. 2022.
[128] S. Li, G. Gou, C. Liu, C. Hou, Z. Li, and G. Xiong, ‘‘TTAGN: Temporal
transaction aggregation graph network for Ethereum phishing scams
detection,’’ in Proc. ACM Web Conf., New Y ork, NY , USA, Apr. 2022,
pp. 661–669.
[129] S. Li, J. Zhou, C. Mo, J. Li, G. K. F. Tso, and Y . Tian, ‘‘Motif-
aware temporal GCN for fraud detection in signed cryptocurrency trust
networks,’’ 2022, arXiv:2211.13123.
[130] V . Patel, L. Pan, and S. Rajasegarar, ‘‘Graph deep learning based
anomaly detection in Ethereum blockchain network,’’ in Network and
System Security, M. Kutyłowski, J. Zhang, and C. Chen, Eds., Cham,
Switzerland: Springer, 2020, pp. 132–148.
[131] N. Pocher, M. Zichichi, F. Merizzi, M. Z. Shafiq, and S. Ferretti, ‘‘Detect-
ing anomalous cryptocurrency transactions: An AML/CFT application
of machine learning-based forensics,’’ Electron. Markets, vol. 33, no. 1,
p. 37, Jul. 2023.
[132] L. Bian, L. Zhang, K. Zhao, H. Wang, and S. Gong, ‘‘Image-based scam
detection method using an attention capsule network,’’ IEEE Access,
vol. 9, pp. 33654–33665, 2021.
202616 VOLUME 13, 2025

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
[133] A. Dutta, L. C. V oumik, A. Ramamoorthy, S. Ray, and A. Raihan,
‘‘Predicting cryptocurrency fraud using ChaosNet: The Ethereum
manifestation,’’ J. Risk Financial Manage., vol. 16, no. 4, p. 216,
Mar. 2023.
[134] N. Tosunoglu, H. Abaci, G. Ates, and N. S. Akkaya, ‘‘Artificial neural
network analysis of the day of the week anomaly in cryptocurrencies,’’
Financial Innov., vol. 9, no. 1, p. 88, May 2023.
[135] B. Tao, H.-N. Dai, H. Xie, and F. L. Wang, ‘‘Structural identity
representation learning for blockchain-enabled metaverse based on
complex network analysis,’’ IEEE Trans. Computat. Social Syst., vol. 10,
no. 5, pp. 2214–2225, Oct. 2023.
[136] H. Hu, Q. Bai, and Y . Xu, ‘‘SCSGuard: Deep scam detection
for Ethereum smart contracts,’’ in Proc. IEEE IEEE Conf.
Comput. Commun. Workshops (INFOCOM WKSHPS), May 2022,
pp. 1–6.
[137] M. Liu, H. Chen, and J. Y an, ‘‘Detecting roles of money laundering in
Bitcoin mixing transactions: A goal modeling and mining framework,’’
Frontiers Phys., vol. 9, Jul. 2021, Art. no. 665399.
[138] A. Shojaeinasab, A. P . Motamed, and B. Bahrak, ‘‘Mixing detection on
Bitcoin transactions using statistical patterns,’’ IET Blockchain, vol. 3,
no. 3, pp. 136–148, Sep. 2023.
[139] L. Wu, Y . Hu, Y . Zhou, H. Wang, X. Luo, Z. Wang, F. Zhang, and K. Ren,
‘‘Towards understanding and demystifying Bitcoinc mixing services,’’ in
Proc. Web Conf., Apr. 2021, pp. 33–44.
[140] T. Tironsakkul, M. Maarek, A. Eross, and M. Just, ‘‘Context matters:
Methods for Bitcoin tracking,’’ F orensic Sci. Int., Digit. Invest.,
vols. 42–43, Oct. 2022, Art. no. 301475.
[141] M. Nazzari, ‘‘From payday to payoff: Exploring the money laundering
strategies of cybercriminals,’’ in Trends in Organized Crime. Cham,
Switzerland: Springer, Sep. 2023.
[142] T. C. I. Team. Wizard Spider Update: Resilient, Reactive
and Resolute. Accessed: Mar. 26, 2025. [Online]. Available:
https://www.crowdstrike.com/en-us/blog/wizard-spider-adversary-
update/
[143] M. A TT&CK. Conti. Accessed: Mar. 26, 2025. [Online]. Available:
https://attack.mitre.org/software/S0575/
[144] A. Trozze, T. Davies, and B. Kleinberg, ‘‘Of degens and defrauders:
Using open-source investigative tools to investigate decentralized finance
frauds and money laundering,’’ F orensic Sci. Int., Digit. Invest., vol. 46,
Sep. 2023, Art. no. 301575.
[145] P . Sheng, G. Wang, K. Nayak, S. Kannan, and P . Viswanath, ‘‘BFT
protocol forensics,’’ in Proc. ACM SIGSAC Conf. Comput. Commun.
Secur ., Nov. 2021, pp. 1722–1743.
[146] L. Li, X. Chang, J. Liu, J. Liu, and Z. Han, ‘‘Bit2CV: A novel
Bitcoin anti-fraud deposit scheme for connected vehicles,’’
IEEE Trans. Intell. Transp. Syst., vol. 22, no. 7, pp. 4181–4193,
Jul. 2021.
[147] B. Liu, P . Szalachowski, and J. Zhou, ‘‘A first look into DeFi oracles,’’
in Proc. IEEE Int. Conf. Decentralized Appl. Infrastruct. (DAPPS),
Aug. 2021, pp. 39–48.
[148] M. Nowostawski and J. Tøn, ‘‘Evaluating methods for the identification
of off-chain transactions in the lightning network,’’ Appl. Sci., vol. 9,
no. 12, p. 2519, Jun. 2019.
[149] S. Tochner, S. Schmid, and A. Zohar, ‘‘Hijacking routes in payment
channel networks: A predictability tradeoff,’’ 2019, arXiv:1909.06890.
[150] L. Zhou, K. Qin, C. F. Torres, D. V . Le, and A. Gervais, ‘‘High-frequency
trading on decentralized on-chain exchanges,’’ in Proc. IEEE Symp.
Secur . Privacy (SP), May 2021, pp. 428–445.
[151] H. Mansourifar, L. Chen, and W. Shi, ‘‘Hybrid cryptocurrency pump and
dump detection,’’ 2020, arXiv:2003.06551.
[152] P . Fratrič, G. Sileno, S. Klous, and T. van Engers, ‘‘Manipulation of the
Bitcoin market: An agent-based study,’’ Financial Innov., vol. 8, no. 1,
p. 60, Jun. 2022.
[153] T. Y an, S. Li, B. Kraner, L. Zhang, and C. J. Tessone, ‘‘A data
engineering framework for Ethereum beacon chain rewards: From data
collection to decentralization metrics,’’ Sci. Data, vol. 12, no. 1, p. 519,
Mar. 2025.
[154] T. Y an, S.-N. Li, and C. J. Tessone, ‘‘Analysis of Ethereum’s block reward
and block creation across the merge,’’ inProc. IEEE Int. Conf. Blockchain
Cryptocurrency (ICBC), Jun. 2025, pp. 1–9.
[155] T. Y an, C. Huang, and C. J. Tessone, ‘‘Tracing cross-chain transactions
between EVM-based blockchains: An analysis of Ethereum-polygon
bridges,’’ 2025, arXiv:2504.15449.
[156] C. Huang, T. Y an, and C. J. Tessone, ‘‘Seamlessly transferring assets
through Layer-0 bridges: An empirical analysis of stargate Bridge’s
architecture and dynamics,’’ in Proc. Companion ACM Web Conf.,
May 2024, pp. 1776–1784.
[157] Z. Wu, S. Pan, F. Chen, G. Long, C. Zhang, and P . S. Y u,
‘‘A comprehensive survey on graph neural networks,’’ IEEE
Trans. Neural Netw. Learn. Syst. , vol. 32, no. 1, pp. 4–24,
Jan. 2021.
[158] Z. Chang, Y . Cai, X. F. Liu, Z. Xie, Y . Liu, and Q. Zhan, ‘‘Anomalous
node detection in blockchain networks based on graph neural networks,’’
Sensors, vol. 25, no. 1, p. 1, Dec. 2024.
[159] L. Cui, Y . Qu, G. Xie, D. Zeng, R. Li, S. Shen, and S. Y u,
‘‘Security and privacy-enhanced federated learning for anomaly detection
in IoT infrastructures,’’ IEEE Trans. Ind. Informat., vol. 18, no. 5,
pp. 3492–3500, May 2022.
[160] X. Wang, W. Liu, H. Lin, J. Hu, K. Kaur, and M. S. Hossain,
‘‘AI-empowered trajectory anomaly detection for intelligent
transportation systems: A hierarchical federated learning approach,’’
IEEE Trans. Intell. Transp. Syst., vol. 24, no. 4, pp. 4631–4640,
Apr. 2023.
[161] Y . Ikeda, R. Hadfi, T. Ito, and A. Fujihara, ‘‘Anomaly detection and
facilitation AI to empower decentralized autonomous organizations for
secure crypto-asset transactions,’’ AI Soc., vol. 40, no. 5, pp. 3999–4010,
Jan. 2025.
[162] Y . Ikeda, H. Aoyama, T. Hatsuda, Y . Hidaka, T. Shirai, W. Souma,
H. Iyetomi, A. Chakraborty, A. Fujihara, Y . Nakayama, Y . Arai,
and K. Sankaewtong, ‘‘V erification of elemental technologies for
anomaly detection in crypto asset transactions,’’ Res. Inst. Econ-
omy, Trade Ind. (RIETI), Tokyo, Japan, Tech. Rep. 24-E-085,
Dec. 2024.
[163] J. Liu, C. Y ang, Z. Lu, J. Chen, Y . Li, M. Zhang, T. Bai, Y . Fang, L. Sun,
P . S. Y u, and C. Shi, ‘‘Graph foundation models: Concepts, opportunities
and challenges,’’ IEEE Trans. Pattern Anal. Mach. Intell., vol. 47, no. 6,
pp. 5023–5044, Jun. 2025.
[164] J. Su, C. Jiang, X. Jin, Y . Qiao, T. Xiao, H. Ma, R. Wei, Z. Jing, J. Xu, and
J. Lin, ‘‘Large language models for forecasting and anomaly detection: A
systematic literature review,’’ 2024, arXiv:2402.10350.
[165] T. Barbereau and B. Bodó, ‘‘Beyond financial regulation of crypto-asset
wallet software: In search of secondary liability,’’ Comput. Law Secur .
Rev., vol. 49, Jul. 2023, Art. no. 105829.
KRONGTUM SANKAEWTONG received the
Ph.D. degree in computational physics from
Nanyang Technological University, Singapore, for
his work on the phase transitions of soft colloids in
confinement. He is a Postdoctoral Research Fellow
with the Graduate School of Advanced Integrated
Studies in Human Survivability, Kyoto University.
After joining Kyoto University, he began transi-
tioning from his doctoral research in soft matter
physics, where he investigated the navigation of
smart microswimmers by coupling machine learning with fluid dynamics
simulations. His current work further expands on this interdisciplinary
approach, integrating network science, and machine learning to develop
novel techniques for anomaly detection in cryptocurrency transaction
networks.
VOLUME 13, 2025 202617

K. Sankaewtong et al.: SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions
TAEHOON KIM is a Senior Research Associate
with the Blockchain and DLT Group, Informatics
Department, University of Zürich (UZH); and
a member of the UZH Blockchain Center. His
research focuses on complex systems and network
science to bring a multidisciplinary perspective
that blends blockchain technology and neuroin-
formatics. His doctoral research in biosystems
science and engineering focused on connectivity
inference methods and graphical models, includ-
ing graph kernels and graph neural networks. With hands-on experience with
ML software stacks and cloud solutions, he is adept with high-performance
computing environments. His work extends to developing web apps
(‘‘Thirdview.io’’) using modern AI software stacks since his initiation in the
Ethereum ecosystem, in 2021.
CLAUDIO J. TESSONE heads the Blockchain and
Distributed Ledger Technologies Group, Univer-
sity of Zürich (UZH). He is also a Co-Founder
and the Chairperson of the UZH Blockchain
Center. He studies blockchains as a paradigm of
socio-economic complexity: linking microscopic
agent behaviour, incentives (placed on purpose or
inadvertently), and interactions with their emer-
gent properties. The main pillars of his research
include: consensus analysis and modeling (looking
at the quality of consensus achieved in real-world situations, the effects of
incentives, and inequality effects of reward distribution), cryptoeconomics
(inequality, centralization, asset circulation, and hoarding), large-scale
blockchain analytics and forensics, and design of token-based economies.
YUICHI IKEDA (Member, IEEE) has been a
Professor of physics with the Graduate School of
Advanced Integrated Studies in Human Surviv-
ability, Kyoto University, since 2012. Formerly,
he was an Associate Professor with the University
of Tokyo and a Senior Research Engineer with
Hitachi Ltd. He also studied computational plasma
physics at UC Berkeley, in 1997, and worked on
global energy issues at the International Energy
Agency, in 2010. Currently, he leads a crypto
network analysis project at RIETI, developing an AI-enhanced DAO system
for anomaly detection in crypto markets using techniques, such as network
science, data science, and machine learning. He created the EDISON-X
blockchain energy platform and developed a decentralized identity system on
XPRL. As a founder of Kyoto University Blockchain Center, he organizes
an international conference, Blockchain Kaigi (BCK), teaches blockchain
economics, and mentors students. He has authored 128 peer-reviewed
papers, 37 patent applications, and 34 academic books. He received the
UBRI Connect 2025 Educator Award from Ripple’s University Blockchain
Research Initiative.
202618 VOLUME 13, 2025