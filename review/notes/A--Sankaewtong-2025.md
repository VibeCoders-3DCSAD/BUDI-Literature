---
paper_id: A--Sankaewtong-2025
first_author: Sankaewtong
year: 2025
title: "SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions"
venue: "IEEE Access"
doi: 10.1109/ACCESS.2025.3636560
designation: algorithm
status: extracted
modules: [model_algorithm_integration, data_collection, model_performance_evaluation, rule_based_classification, sarima]
module_rationale:
  model_algorithm_integration: "The paper's core contribution is a taxonomy and comparative synthesis of four methodological families — statistical, network analysis, machine learning, and heuristic-based — and their hybrid combinations, e.g. GNNs merging topology with ML classification (Sec. I.C.2, Sec. II.C, Sec. IV.A)."
  data_collection: "A reproducible OpenAlex search string and seven-stage screening process (FC1–FC7) yields the 103-study corpus, with explicit counts at each filter (Sec. I.C.1, Fig. 4)."
  model_performance_evaluation: "Section II.G systematically reviews evaluation metrics for anomaly detection — accuracy, precision, recall, F1, AUC-ROC, AUC-PR — with formulas and a discussion of class imbalance (Sec. II.G, Eq. 6–9)."
  rule_based_classification: "Heuristic-based methods are treated as a distinct methodological family relying on expert-defined rules and domain insights, with explicit discussion of their brittleness and interpretability (Sec. II.H, Sec. III.D)."
  sarima: "SARIMAX is discussed as a statistical forecasting method for detecting pump-and-dump anomalies in Bitcoin price, incorporating social media sentiment and achieving up to 93% F1 (Sec. III.A.1, p. 9)."
---

## Summary

This Systematization of Knowledge (SoK) maps the state of anomaly detection for cryptoasset transaction networks. It collects 103 peer-reviewed studies through a reproducible OpenAlex search and multi-stage screening, organizes them into four methodological families — statistical analysis, network analysis, machine learning, and heuristic-based — and compares them across data assumptions, detection scope, interpretability, scalability, and robustness. Five cross-cutting gaps emerge: label scarcity, adversarial evasion, real-time scalability, behavioral ambiguity, and multi-chain visibility. The paper proposes a research agenda centred on hybrid graph-neural/heuristic pipelines, drift-aware statistics, explainable deep models, privacy-preserving analytics, and standardized benchmarks.

## Problem and Motivation

Cryptoasset networks now settle hundreds of billions of dollars each day and underpin a rapidly expanding DeFi ecosystem, yet their openness exposes them to fraud, market manipulation, and protocol-level exploits. High-profile incidents such as the Mt. Gox Collapse (2014) and the Poly Network hack (2021) resulted in losses totalling billions of dollars. Existing literature remains fragmented and lacks a unified synthesis: different methods are evaluated under varying assumptions, datasets, and experimental conditions, making direct comparisons difficult. This study addresses that gap by comprehensively reviewing existing literature on anomaly detection within blockchain transaction networks, systematically classifying and analysing existing methods, identifying limitations in current research, and highlighting open research challenges.

## Method

**Design.** Systematic literature review and Systematization of Knowledge (SoK); the authors label it "SoK" but state no formal review design label beyond that.
**Sample.** 103 peer-reviewed publications selected from an initial 5,020 OpenAlex records through a seven-criteria screening process (FC1–FC7), with the unit of analysis being each publication.
**Context.** geography: Not reported (global literature search with no geographic restriction); population: Peer-reviewed articles, preprints, and book chapters on anomaly detection in cryptoasset transaction networks indexed in OpenAlex as of March 6, 2025; setting: Virtual/computational: reproducible database search, multi-stage screening, and thematic classification of the resulting corpus.

- Query OpenAlex with a search string combining anomaly-detection terms, cryptoasset terms, and graph/network terms.
- Apply FC1: exclude records lacking title, author, abstract, DOI, or indexing, and remove duplicates.
- Apply FC2: exclude non-English publications.
- Apply FC3: retain only articles, preprints, or book chapters.
- Apply FC4: exclude review or survey papers, removing 215 such records.
- Apply FC5: exclude papers published before 2009 (the year Bitcoin was introduced).
- Apply FC6: apply a minimum citation threshold of three, based on the citation distribution in Fig. 3.
- Apply FC7: retain only papers with a primary focus on blockchain transaction network analysis, a clearly defined anomaly-detection methodology, and either empirical evaluation or theoretical foundation.
- Classify the final 103 papers using a multi-dimensional framework with primary dimensions (detection methodology, data sources, application domain) and secondary dimensions (temporal aspects, scale of analysis).
- Organize the detailed review around detection methodology as the central organizing principle.
- Compare methodologies in Table 14 across data requirements, detection capabilities, interpretability, scalability, and adaptability/robustness.

## Key Findings

- Machine learning methods dominate the corpus, accounting for 49 out of 103 studies; network analysis follows with 30 studies, then heuristic-based with 14, and statistical with 10.
- Bitcoin and Ethereum are the primary platforms for annotated anomalies, together accounting for 44 of the 61 cases (72%) in the GraphSense TagPack.
- The paper identifies five cross-cutting gaps: label scarcity, adversarial evasion, real-time scalability, behavioral ambiguity, and multi-chain visibility.
- No single methodology is universally superior; the optimal choice is context-dependent, balancing performance against data availability, robustness against novel threats, and interpretability requirements.
- Statistical methods are effective at point anomalies but face data-distribution sensitivity; network analysis excels at structural and collective anomalies but struggles with scalability; machine learning offers broad pattern recognition but requires labelled data and can lack transparency; heuristic methods excel with known threats but fail against novel patterns.
- A stratified deployment strategy is suggested: heuristic rules as an interpretable first line of defence, unsupervised learning for novel patterns in label-scarce environments, and deep learning for high-volume historical analysis where resources and labels permit.
- GNN complexity for real-time detection is highlighted: a single graph convolutional layer has time complexity O(|E|F′ + |V|FF′), scaling to O(Kmd + Knd²) for a full model, which can be prohibitive for real-time retraining on blockchains with millions of nodes and hundreds of millions of edges.
- Privacy-preserving analytics must balance detectability against privacy: stronger privacy tools (mixers, encrypted transactions) make it harder to spot illicit behaviour, while privacy-preserving detection frameworks safeguard user data at the cost of some sensitivity.
- Cross-chain anomaly detection is an urgent open challenge, as bridge exploits and flash-loan manipulations leave traces distributed across multiple blockchain ecosystems.

## Key Figures and Tables

- Fig. 1 (p. 3): Distribution of document types among the 1,933 publications retained after preliminary screening, with a logarithmic vertical axis.
- Fig. 2 (p. 3): Distribution of the 1,438 selected research papers by publication year, showing growth starting in 2009, with an apparent drop in 2025 due to partial data collection.
- Fig. 3 (p. 3): Citation count distribution of the 1,438 selected research papers, with an inset for the 0–10 citation range.
- Fig. 4 (p. 4): Literature review workflow showing the full selection process from 5,020 records to 103 final publications.
- Fig. 5 (p. 5): Illustration of the UTXO model (left) and the account-based model (right).
- Fig. 6 (p. 7): Taxonomy of anomaly detection techniques.
- Fig. 7 (p. 7): Distribution of the 103 selected research papers across the categories based on the proposed taxonomy.
- Fig. 8 (p. 8): Example of a directed transaction graph among five addresses (A, B, C, D, E), with edges weighted by BTC transferred.
- Table 1 (p. 5): Anomalies listed in public tagpacks, showing raw address counts per category.
- Table 2 (p. 6): Top 10 cryptoassets involved in anomalies listed in Table 1.
- Table 3 (p. 9): Distribution-based and market anomaly detection studies.
- Table 4 (p. 10): Mining behaviour anomaly detection studies.
- Table 5 (p. 11): Structural and community analysis studies.
- Table 6 (p. 12): Temporal and evolutionary network methods.
- Table 7 (p. 14): Graph-based detection and de-anonymization studies.
- Table 8 (p. 16): Supervised learning methods.
- Table 9 (p. 17): Unsupervised and semi-supervised learning methods.
- Table 10 (p. 18): Deep learning and graph neural networks.
- Table 11 (p. 19): Forensic and analytical modelling.
- Table 12 (p. 20): Protocol and cryptographic design.
- Table 13 (p. 21): Heuristic-based methods.
- Table 14 (p. 22): Comparison of anomaly detection methodologies for cryptoassets, with numbers in parentheses indicating the number of studies involved.

## Definitions

- **Anomaly / anomalous transaction** — Activity exhibiting characteristics significantly divergent from what is deemed "normal," often indicative of aberrant behaviour; determining anomalous status can depend on contextual factors and specific transactional or market conditions (Sec. I.A).
- **Point anomalies** — Individual transactions markedly deviating from a typical profile, such as an unusually large single transfer or a transaction involving a previously inactive wallet (Sec. I.A).
- **Contextual anomalies** — Anomalies appearing anomalous primarily due to their context, like occurring at unusual times or representing sudden high-frequency activity from typically inactive accounts (Sec. I.A).
- **Collective anomalies** — Sequences or groups of transactions that seem suspicious when viewed together, even if individual transactions appear normal, such as coordinated pump-and-dump schemes or layering activities used in money laundering (Sec. I.A).
- **UTXO model** — Unspent Transaction Output model used by Bitcoin; tracks discrete chunks of cryptoassets, where each transaction consumes existing UTXOs and generates new ones, providing clear asset traceability valuable for forensic analysis (Sec. II.A).
- **Account-based model** — Model used by Ethereum; functions like a bank account, maintaining a balance that is directly debited or credited (Sec. II.A).
- **EOA (Externally Owned Account)** — Ethereum account controlled by users via private keys; only EOAs can initiate transactions, while smart contracts can only react to transactions they receive (Sec. II.A).
- **MEV (Miner/Validator Extractable Value)** — Value extracted by reordering, inserting, or censoring transactions within a block; can become systemic if left unchecked, impacting DeFi markets by consistently disadvantaging ordinary users (Sec. II.B.3).
- **Pump-and-dump (P&D)** — Coordinated group rapidly buying an illiquid token, driving up the price (the pump), then selling off their holdings en masse (the dump); often involves off-chain coordination on social media (Sec. II.B.3).
- **Wash trading** — Same party (or colluding parties) repeatedly buying and selling an asset to inflate volume or stabilize prices; combined pattern reveals frequent trades between the same addresses with minimal net movement of funds (Sec. II.B.3).
- **Selfish mining** — Miner withholds newly mined blocks from the public network, secretly building a private branch of the chain, then selectively releases blocks to create reorganizations and claim more rewards (Sec. II.B.4).
- **Reentrancy attack** — Vulnerability where a contract sends funds or triggers external calls before updating its state; attackers repeatedly call the same function within a single transaction or block, draining the contract's balance (Sec. II.B.5).
- **Chainlet** — Small, directed pieces of the Bitcoin transaction network that capture common transaction patterns; used in a PDE framework to model Bitcoin price fluctuations (Sec. III.B.2).
- **Ego network** — Subgraph centred on a single node (the "ego") that includes its immediate neighbours (the "alters") and all connections among those neighbours (Sec. III.B.2).
- **Taint analysis** — Marks coins as "tainted" when linked to illegal activity and follows their movements through the blockchain; context-aware versions incorporate address profiling to improve precision (Sec. III.D.1).
- **Peeling chain** — Technique where small outputs are incrementally extracted over sequential transactions (Sec. III.D.1).
- **Anonymity set** — Aggregation of transactions to disrupt linkage analysis (Sec. III.D.1).
- **MSB (Miner Sequence Bootstrapping)** — Statistical method that models each miner's block-discovery event as a Bernoulli trial and uses bootstrapped sequences to detect miners appearing too often in consecutive blocks (Sec. III.A.2).
- **HMTM (Hidden Markov Multi-linear Tensor Model)** — Statistical monitoring framework that models relationships in Bitcoin transaction networks that change over time but whose underlying state is hidden (Sec. III.A.1).
- **MEWMA (Multivariate Exponentially Weighted Moving Average)** — Control chart used with HMTM to monitor deviations and flag anomalies (Sec. III.A.1).
- **TSGN (Transaction SubGraph Networks)** — Method that embeds local subgraphs around potentially malicious addresses for phishing detection (Sec. III.B.3).
- **CFM-LPA** — Not applicable (this term belongs to a different paper, not the present SoK).

## Key Equations

- Degree: `kin(v) = Σu∈V euv`, `kout(v) = Σu∈V evu`, `k(v) = kin(v) + kout(v)` — Number of incoming, outgoing, and total edges connected to a node (Sec. II.E, Eq. 1).
- Clustering coefficient: `C(v) = 2T(v) / (k(v)(k(v)−1))` — Local density of interactions, where T(v) is the number of triangles through node v (Sec. II.E, Eq. 2).
- Degree centrality: `CD(v) = k(v) / (N−1)` — Nodes with higher degree centrality participate in more transactions (Sec. II.E, Eq. 3).
- Closeness centrality: `CC(v) = (N−1) / Σu∈V d(u,v)` — How close a node is to all other nodes (Sec. II.E, Eq. 4).
- Betweenness centrality: `CB(v) = Σs≠v≠t∈V σst(v) / σst` — Extent to which a node lies on paths connecting other nodes (Sec. II.E, Eq. 5).
- Accuracy: `(TP + TN) / (TP + TN + FP + FN)` — Commonly reported but misleading in imbalanced scenarios (Sec. II.G, Eq. 6).
- Precision: `TP / (TP + FP)` — Proportion of flagged anomalies that are truly anomalous (Sec. II.G, Eq. 7).
- Recall: `TP / (TP + FN)` — Proportion of actual anomalies that are flagged (Sec. II.G, Eq. 8).
- F1-Score: `2 × (Precision × Recall) / (Precision + Recall)` — Harmonic mean of precision and recall (Sec. II.G, Eq. 9).
- Signature: `Sn(X) = (1, S1(X), S2(X), ..., Sn(X))` where `S1(X) = ∫0T dX(t)`, `S2(X) = ∫0T ∫0t1 dX(t1) ⊗ dX(t2)`, etc. — Encodes time-series data into iterated integrals; higher-order terms capture multi-scale temporal dependencies (Sec. III.A.1, Eq. 10–11).
- Randomized signature: `R(X) = A · Sn(X)` — Reduces computational complexity, where A is a random matrix (Sec. III.A.1, Eq. 12).
- Benford's Law: `P(d) = log10(1 + 1/d)` — Predicts leading digit distribution; deviations indicate manipulation (Sec. III.A.1, Eq. 13).
- Mahalanobis distance: `MD(r) = √((r−μ)T Σ−1 (r−μ))` — Distance of a data point from the centre of a distribution, accounting for covariance (Sec. III.A.1, Eq. 14).
- Anomaly score: `A(r) = MD(r) / √n` — Identifies significant deviations in cryptoasset returns (Sec. III.A.1, Eq. 15).
- MTM transaction probability: `P(yijt=1|xijt, ui, uj, vt) = xijtβ + <ui, vt, uj> + εijt` — Multi-linear Tensor Model for transaction probability (Sec. III.A.1, Eq. 16).
- VAR model: `yt = v + A1yt−1 + A2yt−2 + ... + Apyt−p + ut` — Vector Autoregressive model capturing dependencies between variables over time (Sec. III.A.1, Eq. 17).
- Adjusted volume: `AVu,t = ln(Vu,t) − ln(ˆVu,t)` — Deviations between observed and expected user-level volumes (Sec. III.A.1, Eq. 18).
- Average abnormal volume: `AAVt = (1/Nt) Σu=1N AVu,t` — Average of daily adjusted volumes across users (Sec. III.A.1, Eq. 19).
- Cumulative abnormal volume: `CAVt = Σt=1T AAVt` — Expands the perspective across longer periods (Sec. III.A.1, Eq. 20).
- Miner Sequence Bootstrapping: `MSBTi = (CTi − ⟨STi⟩) / σ[STi]` — Detects miners appearing too often in consecutive blocks (Sec. III.A.2, Eq. 21).
- Mining cartel detection: `MCTij = (CTij − ⟨STij⟩) / σ[STij]` — Detects pairs of miners appearing in succession (Sec. III.A.2, Eq. 22).
- Preferential attachment: `p(kv) = kvα / Σw kwα` — Probability of forming a new link to node v (Sec. III.B.2, Eq. 23).
- Preferential attachment kernel: `Aij = kiθ kjθ + ηiηj` — Includes node "fitness" ηi (Sec. III.B.2, Eq. 25).
- Correlation tensor unfolding: `C(i,j),(α,β) = U(i,j) Σ1 V*(α,β)` and `V(α,β) = U(α,β) Σ2 W*(α,β)` — Double singular value decomposition for XRP network analysis (Sec. III.B.2, Eq. 26–27).
- PDE for Bitcoin price: `∂u(x,t)/∂t = ∂/∂x (d(x) ∂u(x,t)/∂x) + r(t)u(x,t)h(x)` — Models continuous evolution of Bitcoin price movements using chainlets (Sec. III.B.2, Eq. 29).
- Jaccard Index: `J(A,B) = |A∩B| / |A∪B|` — Quantifies overlap in transaction patterns (Sec. III.B.1).
- Ordered Jaccard Index: `OJI(A,B) = |LCS(A,B)| / |A∪B|` — Captures sequential patterns in how accounts trade (Sec. III.B.1).
- Temporal Weighted Multidigraph edge: `e = (u, v, w, t)` — Source node, target node, weight (transaction amount), and timestamp (Sec. III.B.1).
- Temporal successive edges: `Lt(u) = {e | Src(e) = u, T(e) ≥ t}` — Set of edges leaving node u at or after time t (Sec. III.B.1).

## Limitations and Gaps

- The authors acknowledge that the scarcity of accurately labelled data constitutes a fundamental obstacle: confirmed illicit addresses are exceedingly rare relative to legitimate activity, resulting in severe class imbalance that impedes supervised learning (Sec. IV.D).
- The authors acknowledge that scalability and real-time constraints remain pressing issues: blockchain transaction volumes continuously grow, and achieving timely, accurate anomaly detection with sub-second inference and manageable false-positive rates is computationally intensive, particularly for network analysis or complex machine-learning models (Sec. IV.D).
- The authors acknowledge that distinguishing benign yet privacy-preserving behaviours from malicious obfuscation requires sophisticated behavioural modelling and nuanced feature engineering (Sec. IV.D).
- The authors acknowledge that cross-chain anomaly detection is becoming increasingly pertinent, as bridge exploits and flash-loan manipulations often leave traces distributed across multiple blockchain ecosystems (Sec. IV.D).
- The authors acknowledge that a direct comparison of performance metrics across the 103 studies is challenging due to the lack of standardized benchmark datasets (Sec. IV.A).
- The authors acknowledge that many supervised methods rely heavily on public, on-chain datasets, which may omit off-chain data such as user reputations or external intelligence (Sec. III.C.1).
- The authors acknowledge that ensemble and deep-learning pipelines may still be constrained by the quality and consistency of labels (Sec. III.C.1).
- The authors acknowledge that clustering heuristics and models like Chung–Lu or Barabási–Albert can fail to capture special nodes (e.g., centralized exchanges, mixers) or ephemeral patterns arising from purposeful on-chain manipulations, limiting their predictive power (Sec. III.B.3).
- The authors acknowledge that real-world heterogeneities such as multi-signature addresses, advanced DeFi operations, or bridging solutions spanning multiple blockchains complicate straightforward generalization (Sec. III.B.3).
- The authors acknowledge that local subgraph extraction risks overlooking broader interactions that cross local boundaries (Sec. III.B.3).
- The authors acknowledge that purely heuristic approaches can be overly rigid, generating potential false positives whenever normal users share superficial similarities with illicit addresses (Sec. III.D.3).
- The authors acknowledge that heuristic methods may fail to detect complex or evolving laundering strategies beyond the scope of pre-defined rules, leading to higher false negatives as criminals adapt (Sec. III.D.3).
- [unacknowledged] The paper does not report any formal quality assessment or risk-of-bias appraisal of the 103 included studies, despite being a systematic review.
- [unacknowledged] The paper does not report inter-rater reliability for the screening or classification process; the coding of studies into methodological families is presented without a second coder or agreement statistic.
- [unacknowledged] The minimum citation threshold of three (FC6) may systematically exclude recent or niche work that has not yet accrued citations, introducing a temporal bias against newer research.
- [unacknowledged] The paper's own taxonomy is presented as the organizing principle, but no sensitivity analysis or alternative taxonomy is tested; the assignment of studies to exactly one of four families is not validated against an independent scheme.
- [unacknowledged] The paper reports no meta-analytic synthesis, no pooled effect sizes, and no quantitative comparison across studies; Table 14 is qualitative, so the comparative claims about methodology performance rest on narrative rather than statistical aggregation.
- [unacknowledged] The OpenAlex search was executed on March 6, 2025, meaning the corpus reflects a snapshot and cannot capture subsequent publications; the authors note the apparent 2025 drop is due to partial data but do not discuss how this affects the completeness of the review.
- [unacknowledged] The paper excludes studies focused solely on market price prediction without transaction-level analysis and broader blockchain applications outside the financial/transactional domain, which may omit relevant anomaly-detection methods from adjacent fields.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| OpenAlex search results | publications | 5,020 | — | — | Sec. I.C.1, p. 3 |
| After initial screening (FC1) | publications | 1,933 | — | — | Sec. I.C.1, p. 3 |
| After review/survey exclusion (FC4) | research papers | 1,438 | — | — | Sec. I.C.1, p. 3 |
| Review/survey papers removed | review/survey papers | 215 | — | — | Sec. I.C.1, p. 3 |
| After citation threshold (FC6) | publications | 509 | — | — | Sec. I.C.1, p. 3 |
| Final selected set | publications | 103 | — | — | Sec. I.C.1, p. 3 |
| Machine learning studies | studies | 49 | — | — | Sec. II.C, p. 6 |
| Network analysis studies | studies | 30 | — | — | Sec. II.C, p. 6 |
| Heuristic-based studies | studies | 14 | — | — | Sec. II.C, p. 6 |
| Statistical studies | studies | 10 | — | — | Sec. II.C, p. 6 |
| Bitcoin/Ethereum share of annotated cases | cases | 44 of 61 (72%) | — | — | Sec. II.B, p. 5 |
| Total cryptoasset capitalization | USD | US$3 trillion | — | — | Sec. I.A, p. 1 |
| Daily on-chain value transfer | USD | over US$100 billion | — | — | Sec. I.A, p. 1 |
| Signature method F1 score | F1 | 0.88 | — | — | Sec. III.A.1, p. 8 |
| SARIMAX F1 score | F1 | 93% | — | — | Sec. III.A.1, p. 9 |
| Stacking ensemble F1 score | F1 | above 95% | — | — | Sec. III.C.1, p. 11 |
| XGBoost/RF phishing F1 score | F1 | 98% | — | — | Sec. III.C.1, p. 11 |
| SVM/Naive Bayes Ponzi accuracy | accuracy | 99% | — | — | Sec. III.C.1, p. 11 |
| Attention capsule network F1 | F1 | 98.38% | — | — | Sec. III.C.3, p. 14 |
| Star subgraph GNN recall | recall | nearly 99% | — | — | Sec. III.C.3, p. 14 |
| Two-layer attention star subgraph recall | recall | 99.3% | — | — | Sec. III.C.3, p. 14 |
| LSTM/Bi-LSTM/CNN ensemble accuracy | accuracy | near 99% | — | — | Sec. III.C.1, p. 12 |
| Uniswap sandwich attack daily revenue | USD | $3,414 | — | — | Sec. III.D.3, p. 16 |
| CoinJoin-style transaction identification | % | 92% | — | — | Sec. III.D.1, p. 15 |
| Mt. Gox abnormal accounts | % accounts | 12.5% | — | — | Sec. III.B.3, p. 10 |
| Mt. Gox abnormal transactions | % transactions | 2.8% | — | — | Sec. III.B.3, p. 10 |
| Zcash address clustering | % addresses | 87.5% | — | — | Sec. III.B.3, p. 10 |
| Zcash transaction linking | % transactions | 25.7% | — | — | Sec. III.B.3, p. 10 |
| EOSIO bot-like accounts | % accounts | 30.75% | — | — | Sec. III.B.3, p. 10 |
| EOSIO bot-like accounts (count) | accounts | 381,008 | — | — | Sec. III.B.3, p. 10 |
| EOSIO bot transactions | transactions | 192 million | — | — | Sec. III.B.3, p. 10 |
| EOSIO bot tokens transferred | EOS tokens | 640 million | — | — | Sec. III.B.3, p. 10 |
| DAO study transactions | transactions | 5,580 | — | — | Sec. III.A.1, p. 9 |
| DAO study users | users | 7,825 | — | — | Sec. III.A.1, p. 9 |
| DAO study DAOs | DAOs | 191 | — | — | Sec. III.A.1, p. 9 |
| Gas price surges | % increase | 8500% | — | — | Sec. III.A.1, p. 9 |
| LN 2-of-2 multisig linked to LN | % | over 75% | — | — | Sec. III.D.3, p. 16 |
| LN routes through five nodes | % routes | nearly 60% | — | — | Sec. III.D.3, p. 16 |
| LN routes through ten nodes | % routes | 80% | — | — | Sec. III.D.3, p. 16 |
| LN attack links diverting traffic | % traffic | 65%-75% | — | — | Sec. III.D.3, p. 16 |
| Conti ransomware proceeds | USD | over $11 million | — | — | Sec. III.D.1, p. 15 |
| Mt. Gox abnormal accounts share | % | 12.5% | — | — | Sec. III.B.3, p. 10 |
| Zcash shielded pool linking | % addresses | 87.5% | — | — | Sec. III.B.3, p. 10 |
| EOSIO bot-like share | % accounts | 30.75% | — | — | Sec. III.B.3, p. 10 |
| Bitcoin/Ethereum annotated cases | cases | 44 of 61 | — | — | Sec. II.B, p. 5 |
| Bitcoin/Ethereum annotated cases | % | 72% | — | — | Sec. II.B, p. 5 |
| GraphSense TagPack raw address counts — sextortion | addresses | Not reported (Table 1 shows raw counts but the table is not fully legible in the extraction) | — | — | Table 1, p. 5 |
| GraphSense TagPack raw address counts — mixing services | addresses | Not reported (Table 1 shows raw counts but the table is not fully legible in the extraction) | — | — | Table 1, p. 5 |
| GraphSense TagPack — exchange hacks | addresses | Not reported (Table 1 shows raw counts but the table is not fully legible in the extraction) | — | — | Table 1, p. 5 |
| GraphSense TagPack — pyramid schemes | addresses | Not reported (Table 1 shows raw counts but the table is not fully legible in the extraction) | — | — | Table 1, p. 5 |
| GraphSense TagPack — phishing | addresses | Not reported (Table 1 shows raw counts but the table is not fully legible in the extraction) | — | — | Table 1, p. 5 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "Cryptoasset networks now settle hundreds of billions of dollars each day and underpin a rapidly expanding DeFi ecosystem." | Abstract, p. 1 | model_algorithm_integration |
| "Five cross-cutting gaps emerge: label scarcity, adversarial evasion, real-time scalability, behavioral ambiguity, and multi-chain visibility." | Abstract, p. 1 | model_algorithm_integration |
| "We categorize techniques based on their core algorithmic approach into statistical methods, network analysis techniques, machine learning approaches, and heuristic-based strategies." | Sec. I.C.2, p. 4 | model_algorithm_integration |
| "Machine learning methods dominate, accounting for 49 out of 103 analyzed studies, reflecting the increasing emphasis on adaptive, data-driven techniques." | Sec. II.C, p. 6 | model_algorithm_integration |
| "Anomaly detection in cryptoasset networks typically involves identifying rare, illicit, or otherwise suspicious transactions within a much larger pool of benign activity." | Sec. II.G, p. 7 | model_performance_evaluation |
| "Blockchain transactions are pseudonymous, not anonymous. Users operate via cryptographic addresses, which are not directly tied to real-world identities." | Sec. II.A, p. 5 | data_collection |
| "Heuristic-based methods rely on expert-defined rules or domain insights to pinpoint suspicious behavior in blockchain transactions." | Sec. II.H, p. 7 | rule_based_classification |
| "The scarcity of accurately labeled data constitutes a fundamental obstacle. Confirmed illicit addresses are exceedingly rare relative to legitimate activity, resulting in severe class imbalance." | Sec. IV.D, p. 12 | model_performance_evaluation |
| "No single methodology is universally superior. The optimal choice is context-dependent, balancing the need for high performance against the practical constraints of data availability." | Sec. IV.A, p. 11 | model_algorithm_integration |
| "Graph Neural Networks (GNNs) combining network topology with machine learning classification exemplify such approaches, merging structural insights with data-driven detection capabilities." | Sec. IV.E, p. 13 | model_algorithm_integration |
| "The challenge of cross-chain anomaly detection is becoming increasingly pertinent. Attacks such as bridge exploits and flash-loan manipulations often leave traces distributed across multiple blockchain ecosystems." | Sec. IV.D, p. 12 | data_collection |
| "Distinguishing benign yet privacy-preserving behaviors from malicious obfuscation requires sophisticated behavioral modeling and nuanced feature engineering." | Sec. IV.D, p. 12 | model_performance_evaluation |
| "Establishing standardized benchmarks and datasets is essential to enabling fair, consistent comparisons across methods." | Sec. IV.E, p. 13 | model_performance_evaluation |
| "The time complexity of a single graph convolutional layer is often O(\|E\|F′+\|V\|FF′), where \|V\| is the number of nodes, \|E\| is the number of edges, and F/F′ are the input/output feature dimensions." | Sec. IV.D, p. 12 | model_algorithm_integration |
| "A stratified deployment strategy, i.e. heuristic rules serve as an interpretable first line of defense for known threats, while unsupervised learning is essential for spotting novel patterns in label-scarce environments." | Sec. IV.A, p. 11 | rule_based_classification |

## Remember This

- This SoK maps 103 peer-reviewed studies on cryptoasset anomaly detection, selected from an initial 5,020 OpenAlex records through a seven-criteria screening process.
- The four methodological families are statistical analysis (10 studies), network analysis (30 studies), machine learning (49 studies), and heuristic-based (14 studies).
- Five cross-cutting gaps structure the research agenda: label scarcity, adversarial evasion, real-time scalability, behavioral ambiguity, and multi-chain visibility.
- Bitcoin and Ethereum together account for 44 of 61 annotated anomaly cases (72%) in the GraphSense TagPack.
- The paper proposes hybrid graph-neural/heuristic pipelines, drift-aware statistics, explainable deep models, privacy-preserving analytics, and standardized benchmarks as future directions.
- GNN computational complexity O(Kmd + Knd²) is identified as a key bottleneck for real-time deployment on large blockchain graphs.
- No single methodology is universally superior; a stratified deployment strategy is recommended, with heuristics as first-line defence, unsupervised learning for novel patterns, and deep learning for high-volume historical analysis.

## Cited Works

- Nakamoto, S. (2008) — Bitcoin whitepaper introducing the foundational distributed ledger and solving double-spending. [p. 1]
- Chen, W., Wu, J., Zheng, Z., Chen, C., and Zhou, Y. (2019) — Market manipulation of Bitcoin: evidence from mining the Mt. Gox transaction network, using user-level transaction graphs and SVD. [p. 8]
- GraphSense TagPack (2022) — Open-source, community-maintained collection of machine-readable attribution tags linking blockchain addresses to real-world actors. [p. 5]
- Barabási, A.-L. (2016) — Network Science textbook covering graph theory fundamentals. [p. 7]
- Akyildirim, E., Gambara, M., Teichmann, J., and Zhou, S. (2022) — Applications of signature methods to market anomaly detection, achieving 0.88 F1 on Bitcoin price-volume time series. [p. 8]
- Vicic, J. and Tosic, A. (2022) — Application of Benford's Law on cryptocurrencies, finding Bitcoin and Ethereum conform while TENX, VERI, and DOGE deviate. [p. 8]
- Bae, G. and Kim, J. H. (2022) — Observing cryptocurrencies through robust anomaly scores using Mahalanobis distances on market price data. [p. 8]
- Akba, F., Medeni, I. T., Guzel, M. S., and Askerzade, I. (2021) — Manipulator detection in cryptocurrency markets based on forecasting anomalies using SARIMAX with social media sentiment, achieving up to 93% F1. [p. 9]
- Park, J. H. and Sohn, Y. (2020) — Detecting structural changes in longitudinal network data using Hidden Markov Multi-linear Tensor Models. [p. 9]
- Sabri-Laghaie, K., Jafarzadeh Ghoushchi, S., Elhambakhsh, F., and Mardani, A. (2020) — Monitoring blockchain cryptocurrency transactions using HMTM and MEWMA control charts, flagging Mt. Gox leaked transactions. [p. 9]
- Faqir-Rhazoui, Y., Ariza-Garzón, M.-J., Arroyo, J., and Hassan, S. (2021) — Effect of gas price surges on user activity in DAOs of the Ethereum blockchain, analysing 5,580 transactions from 7,825 users in 191 DAOs. [p. 9]
- Amiram, D., Jørgensen, B. N., and Rabetti, D. (2022) — Coins for bombs: predictive ability of on-chain transfers for terrorist attacks, using mean-adjusted volume and cumulative abnormal volume. [p. 10]
- Li, S.-N., Yang, Z., and Tessone, C. J. (2020) — Proof-of-work cryptocurrency mining: a statistical approach to fairness, introducing Miner Sequence Bootstrapping (MSB). [p. 10]
- Li, S.-N., Campajola, C., and Tessone, C. J. (2024) — Statistical detection of selfish mining in proof-of-work blockchain systems, finding Monacoin has the highest fraction of suspicious miners. [p. 10]
- Aponte-Novoa, F. A., Orozco, A. L. S., Villanueva-Polanco, R., and Wightman, P. (2021) — The 51% attack on blockchains: a mining behavior study, profiling miner share distributions on Bitcoin and Ethereum. [p. 10]
- Zhang, Z., Li, W., Liu, H., and Liu, J. (2020) — A refined analysis of Zcash anonymity, achieving 87.5% address clustering and linking 25.7% of transactions to mining rewards. [p. 10]
- Fu, Q., Lint, D., Cao, Y., and Wu, J. (2023) — Does money laundering on Ethereum have traditional traits? Case study of the Upbit hack, finding fast-in/fast-out and zero-out middle accounts. [p. 10]
- Hu, Y., Seneviratne, S., Thilakarathna, K., Fukuda, K., and Seneviratne, A. (2019) — Characterizing and detecting money laundering activities on the Bitcoin network using node2vec embeddings and AdaBoost, achieving ~92% accuracy. [p. 11]
- Ogundokun, R. O., Arowolo, M. O., Damaševičius, R., and Misra, S. (2023) — Phishing detection in blockchain transaction networks using LSTM/Bi-LSTM/CNN ensemble, achieving near 99% detection accuracy. [p. 12]
- Alarab, I. and Prakoonwit, S. (2023) — Graph-based LSTM for anti-money laundering: temporal graph convolutional network with Bitcoin data. [p. 13]
- Guo, C., Zhang, S., Zhang, P., Alkubati, M., and Song, J. (2023) — LB-GLAT: long-term bi-graph layer attention convolutional network for anti-money laundering in transactional blockchain. [p. 13]
- Hu, S., Zhang, Z., Luo, B., Lu, S., He, B., and Liu, L. (2023) — BERT4ETH: a pre-trained transformer for Ethereum fraud detection. [p. 13]
- Song, A., Seo, E., and Kim, H. (2023) — Anomaly VAE-transformer: a deep learning approach for anomaly detection in decentralized finance. [p. 13]
- Zhou, J., Hu, C., Chi, J., Wu, J., Shen, M., and Xuan, Q. (2022) — Behavior-aware account de-anonymization on Ethereum interaction graph, introducing Ethident (HGATE). [p. 14]
- Nicholls, J., Kuppa, A., and Le-Khac, N.-A. (2023) — FraudLens: graph structural learning for Bitcoin illicit activity identification. [p. 14]
- Hu, H., Bai, Q., and Xu, Y. (2022) — SCSGuard: deep scam detection for Ethereum smart contracts using GRU and attention on opcode sequences. [p. 14]
- Liu, M., Chen, H., and Yan, J. (2021) — Detecting roles of money laundering in Bitcoin mixing transactions: a goal modeling and mining framework. [p. 15]
- Tironsakkul, T., Maarek, M., Eross, A., and Just, M. (2022) — Context matters: methods for Bitcoin tracking, introducing context-aware taint analysis. [p. 15]
- Trozze, A., Davies, T., and Kleinberg, B. (2023) — Of degens and defrauders: using open-source investigative tools to investigate decentralized finance frauds and money laundering. [p. 15]
- Sheng, P., Wang, G., Nayak, K., Kannan, S., and Viswanath, P. (2021) — BFT protocol forensics, formalizing post-violation diagnostics with (m, k, d) triplet. [p. 20]
- Tochner, S., Schmid, S., and Zohar, A. (2019) — Hijacking routes in payment channel networks: a predictability tradeoff, finding 60% of LN routes pass through five nodes. [p. 16]
- Zhou, L., Qin, K., Torres, C. F., Le, D. V., and Gervais, A. (2021) — High-frequency trading on decentralized on-chain exchanges, formalizing sandwich attacks on Uniswap. [p. 16]
- Mansourifar, H., Chen, L., and Shi, W. (2020) — Hybrid cryptocurrency pump and dump detection using distance- and density-based anomaly metrics with PCA. [p. 16]
- Fratrič, P., Sileno, G., Klous, S., and van Engers, T. (2022) — Manipulation of the Bitcoin market: an agent-based study simulating Tether injections. [p. 16]
- Yan, T., Li, S., Kraner, B., Zhang, L., and Tessone, C. J. (2025) — A data engineering framework for Ethereum beacon chain rewards. [p. 12]
- Yan, T., Huang, C., and Tessone, C. J. (2025) — Tracing cross-chain transactions between EVM-based blockchains: an analysis of Ethereum-polygon bridges. [p. 12]
- Ikeda, Y., Hadfi, R., Ito, T., and Fujihara, A. (2025) — Anomaly detection and facilitation AI to empower decentralized autonomous organizations for secure crypto-asset transactions. [p. 13]
- Liu, J., Yang, C., Lu, Z., Chen, J., Li, Y., Zhang, M., Bai, T., Fang, Y., Sun, L., Yu, P. S., and Shi, C. (2025) — Graph foundation models: concepts, opportunities and challenges. [p. 13]
- Su, J., Jiang, C., Jin, X., Qiao, Y., Xiao, T., Ma, H., Wei, R., Jing, Z., Xu, J., and Lin, J. (2024) — Large language models for forecasting and anomaly detection: a systematic literature review. [p. 13]
- Barbereau, T. and Bodó, B. (2023) — Beyond financial regulation of crypto-asset wallet software: in search of secondary liability. [p. 13]
- Wu, Z., Pan, S., Chen, F., Long, G., Zhang, C., and Yu, P. S. (2021) — A comprehensive survey on graph neural networks, providing the GNN complexity analysis O(Kmd + Knd²). [p. 12]
- Chang, Z., Cai, Y., Liu, X. F., Xie, Z., Liu, Y., and Zhan, Q. (2024) — Anomalous node detection in blockchain networks based on graph neural networks. [p. 12]
- Cui, L., Qu, Y., Xie, G., Zeng, D., Li, R., Shen, S., and Yu, S. (2022) — Security and privacy-enhanced federated learning for anomaly detection in IoT infrastructures. [p. 12]
- Wang, X., Liu, W., Lin, H., Hu, J., Kaur, K., and Hossain, M. S. (2023) — AI-empowered trajectory anomaly detection for intelligent transportation systems: a hierarchical federated learning approach. [p. 12]
- Bolz, M., Brundler, K., Kane, L., Patsias, P., Tessendorf, L., Gogol, K., Kim, T., and Tessone, C. (2024) — Machine learning-based detection of pump-and-dump schemes in real-time. [p. 5]
- Öz, B., Kraner, B., Vallarano, N., Kruger, B. S., Matthes, F., and Tessone, C. J. (2023) — Time moves faster when there is nothing you anticipate: the role of time in MEV rewards. [p. 5]
- De Collibus, F. M., Campajola, C., and Tessone, C. J. (2025) — The microvelocity of money in Ethereum. [p. 4]
- Yan, T., Kim, Y. H., Li, S., Kim, T., and Tessone, C. J. (2025) — Applying Basel framework to estimate systemic risk of decentralized finance. [p. 4]
- Kraner, B., Pennella, L., Vallarano, N., and Tessone, C. J. (2025) — Money in motion: micro-velocity and usage of Ethereum's liquid staking tokens. [p. 4]
- Liang, J., Li, L., and Zeng, D. (2018) — Evolutionary dynamics of cryptocurrency transaction networks: an empirical study. [p. 4]
- Wu, J., Liu, J., Zhao, Y., and Zheng, Z. (2021) — Analysis of cryptocurrency transactions from a network perspective: an overview. [p. 4]
- Yan, T. and Tessone, C. J. (2025) — Network analysis of Uniswap: centralization and fragility in the decentralized exchange market. [p. 4]
- Gagliardoni, T. (2021) — The Poly Network hack explained. [p. 1]
- Khattak, B. H. A., Shafi, I., Rashid, C. H., Safran, M., Alfarhood, S., and Ashraf, I. (2024) — Profitability trend prediction in crypto financial markets using Fibonacci technical indicator and hybrid CNN model. [p. 2]
- Monrat, A. A., Schelén, O., and Andersson, K. (2019) — A survey of blockchain from the perspectives of applications, challenges, and opportunities. [p. 5]
- Tapscott, D. and Tapscott, A. (2016) — Blockchain revolution: how the technology behind Bitcoin is changing money, business, and the world. [p. 5]
- Goodfellow, I., Bengio, Y., and Courville, A. (2016) — Deep Learning textbook. [p. 7]
- Brunton, S. L. and Kutz, J. N. (2019) — Data-Driven Science and Engineering: Machine Learning, Dynamical Systems, and Control. [p. 7]
- Box, G. E. P., Jenkins, G. M., Reinsel, G. C., and Ljung, G. M. (2015) — Time Series Analysis: Forecasting and Control, providing the SARIMAX framework. [p. 9]
- Montgomery, D. C. (2020) — Statistical Quality Control: A Modern Approach, providing the MEWMA control chart framework. [p. 9]
- Lowry, C. A., Woodall, W. H., Champ, C. W., and Rigdon, S. E. (1992) — A multivariate exponentially weighted moving average control chart. [p. 9]
- Hoff, P. D. (2015) — Multilinear tensor regression for longitudinal relational data. [p. 9]
- Lischke, M. and Fabian, B. (2016) — Analyzing the Bitcoin network: the first four years, revealing small-world topology. [p. 11]
- Tao, B., Ho, I. W.-H., and Dai, H.-N. (2021) — Complex network analysis of the Bitcoin blockchain network. [p. 11]
- Tao, B., Dai, H.-N., Wu, J., Ho, I. W.-H., Zheng, Z., and Cheang, C. F. (2022) — Complex network analysis of the Bitcoin transaction network. [p. 11]
- Chang, V., Hall, K., Xu, Q. A., Doan, L. M. T., and Wang, Z. (2022) — A social network analysis of two networks: adolescent school network and Bitcoin trader network. [p. 11]
- Rosa, G. and Pareschi, R. (2021) — Tether: a study on bubble-networks. [p. 11]
- Di, Z., Wang, G., Jia, L., and Chen, Z. (2022) — Bitcoin transactions as a graph. [p. 11]
- Aiello, W., Chung, F., and Lu, L. (2001) — A random graph model for power law graphs. [p. 11]
- Buckley, P. G. and Osthus, D. (2004) — Popularity based random graph models leading to a scale-free degree sequence. [p. 11]
- Lin, D., Wu, J., Yuan, Q., and Zheng, Z. (2020) — Modeling and understanding Ethereum transaction records via a complex network approach. [p. 11]
- Ao, Z., William Cong, L., Horvath, G., and Zhang, L. (2022) — Is decentralized finance actually decentralized? A social network analysis of the AAVE protocol on the Ethereum blockchain. [p. 11]
- De Collibus, F. M., Piškorec, M., Partida, A., and Tessone, C. J. (2022) — The structural role of smart contracts and exchanges in the centralisation of Ethereum-based cryptoassets. [p. 11]
- Alamsyah, A. and Muhammad, I. F. (2024) — Unraveling the crypto market: a journey into decentralized finance transaction network. [p. 12]
- Kondor, D., Pósfai, M., Csabai, I., and Vattay, G. (2014) — Do the rich get richer? An empirical analysis of the Bitcoin transaction network. [p. 12]
- Aspembitova, A., Feng, L., Melnikov, V., and Chew, L. Y. (2019) — Fitness preferential attachment as a driving mechanism in Bitcoin transaction network. [p. 12]
- De Collibus, F. M., Partida, A., Piškorec, M., and Tessone, C. J. (2021) — Heterogeneous preferential attachment in key Ethereum-based cryptoassets. [p. 12]
- Kondor, D., Bulatovic, N., Stéger, J., Csabai, I., and Vattay, G. (2021) — The rich still get richer: empirical comparison of preferential attachment via linking statistics in Bitcoin and Ethereum. [p. 12]
- Bovet, A., Campajola, C., Mottes, F., Restocchi, V., Vallarano, N., Squartini, T., and Tessone, C. J. (2023) — The evolving liaisons between the transaction networks of Bitcoin and its price dynamics. [p. 12]
- Kondor, D., Csabai, I., Szüle, J., Pósfai, M., and Vattay, G. (2014) — Inferring the interplay between network structure and market effects in Bitcoin. [p. 12]
- Chakraborty, A., Hatsuda, T., and Ikeda, Y. (2023) — Projecting XRP price burst by correlation tensor spectra of transaction networks. [p. 12]
- Wang, Y. and Wang, H. (2020) — Using networks and partial differential equations to forecast Bitcoin price movement. [p. 12]
- Wang, Z., Zhang, R., Sun, Y., Ding, H., and Lv, Q. (2022) — Can Lightning Network's autopilot function use BA model as the underlying network? [p. 12]
- Huang, B., Liu, J., Wu, J., Li, Q., and Lin, H. (2022) — Temporal analysis of transaction ego networks with different labels on Ethereum. [p. 13]
- Jourdan, M., Blandin, S., Wynter, L., and Deshpande, P. (2018) — Characterizing entities in the Bitcoin blockchain. [p. 13]
- Wu, Y., Tao, F., Liu, L., Gu, J., Panneerselvam, J., Zhu, R., and Shahzad, M. N. (2021) — A Bitcoin transaction network analytic method for future blockchain forensic investigation, proposing a Petri-net-based framework. [p. 13]
- Morishima, S. (2021) — Scalable anomaly detection in blockchain using graphics processing unit. [p. 13]
- Wang, J., Chen, P., Xu, X., Wu, J., Shen, M., Xuan, Q., and Yang, X. (2022) — TSGN: transaction subgraph networks assisting phishing detection in Ethereum. [p. 13]
- Huang, Y., Wang, H., Wu, L., Tyson, G., Luo, X., Zhang, R., Liu, X., Huang, G., and Jiang, X. (2020) — Characterizing EOSIO blockchain, finding 30.75% of accounts exhibit bot-like behaviour. [p. 13]
- Huang, Y., Wang, H., Wu, L., Tyson, G., Luo, X., Zhang, R., Liu, X., Huang, G., and Jiang, X. (2020) — Understanding (Mis)behavior on the EOSIO blockchain. [p. 13]
- Ashfaq, T., Khalid, R., Yahaya, A. S., Aslam, S., Azar, A. T., Alsafari, S., and Hameed, I. A. (2022) — A machine learning and blockchain based efficient fraud detection mechanism. [p. 14]
- Nayyer, N., Javaid, N., Akbar, M., Aldegheishem, A., Alrajeh, N., and Jamil, M. (2023) — A new framework for fraud detection in Bitcoin transactions through ensemble stacking model in smart cities, achieving above 95% F1. [p. 14]
- Ghosh, M., Ghosh, D., Halder, R., and Chandra, J. (2023) — Investigating the impact of structural and temporal behaviors in Ethereum phishing users detection, achieving 98% F1. [p. 14]
- Oliveira, C., Torres, J., Silva, M. I., Aparício, D., Ascensão, J. T., and Bizarro, P. (2021) — GuiltyWalker: distance to illicit nodes in the Bitcoin network. [p. 14]
- Chen, W., Zheng, Z., Cui, J., Ngai, E., Zheng, P., and Zhou, Y. (2018) — Detecting Ponzi schemes on Ethereum: towards healthier blockchain technology. [p. 14]
- Chen, W., Zheng, Z., Ngai, E. C.-H., Zheng, P., and Zhou, Y. (2019) — Exploiting blockchain data to detect smart Ponzi schemes on Ethereum. [p. 14]
- Ibba, G., Pierro, G. A., and Di Francesco, M. (2021) — Evaluating machine-learning techniques for detecting smart Ponzi schemes, achieving 99% accuracy with SVM and Naive Bayes. [p. 14]
- Jin, C., Jin, J., Zhou, J., Wu, J., and Xuan, Q. (2022) — Heterogeneous feature augmentation for Ponzi detection in Ethereum. [p. 14]
- Onu, I. J., Omolara, A. E., Alawida, M., Abiodun, O. I., and Alabdultif, A. (2023) — Detection of Ponzi scheme on Ethereum using machine learning algorithms. [p. 14]
- Toyoda, K., Mathiopoulos, P. T., and Ohtsuki, T. (2019) — A novel methodology for HYIP operators' Bitcoin addresses identification. [p. 14]
- Elmougy, Y. and Manzi, O. (2021) — Anomaly detection on Bitcoin, Ethereum networks using GPU-accelerated machine learning methods. [p. 14]
- Elmougy, Y. and Liu, L. (2023) — Demystifying fraudulent transactions and illicit nodes in the Bitcoin network for financial forensics. [p. 14]
- Mittal, R. and Bhatia, M. P. S. (2021) — Detection of suspicious or un-trusted users in crypto-currency financial trading applications. [p. 14]
- Liu, X. F., Ren, H.-H., Liu, S.-H., and Jiang, X.-J. (2021) — Characterizing key agents in the cryptocurrency economy through blockchain transaction analysis. [p. 14]
- Liu, J., Yin, C., Wang, H., Wu, X., Lan, D., Zhou, L., and Ge, C. (2023) — Graph embedding-based money laundering detection for Ethereum. [p. 14]
- Lin, Y.-J., Wu, P.-W., Hsu, C.-H., Tu, I.-P., and Liao, S.-W. (2019) — An evaluation of Bitcoin address classification based on transaction history summarization. [p. 14]
- Lin, D., Wu, J., Yuan, Q., and Zheng, Z. (2020) — T-EDGE: temporal weighted multidigraph embedding for Ethereum transaction network analysis. [p. 14]
- Hasan, M., Rahman, M. S., Janicke, H., and Sarker, I. H. (2024) — Detecting anomalies in blockchain transactions using machine learning classifiers and explainability analysis. [p. 14]
- Monamo, P. M., Marivate, V., and Twala, B. (2016) — Unsupervised learning for robust Bitcoin fraud detection using trimmed k-means. [p. 17]
- Pham, T. and Lee, S. (2016) — Anomaly detection in Bitcoin network using unsupervised learning methods. [p. 17]
- Pham, T. and Lee, S. (2016) — Anomaly detection in the Bitcoin system — a network perspective. [p. 17]
- Sayadi, S., Ben Rejeb, S., and Choukair, Z. (2019) — Anomaly detection model over blockchain electronic transactions, using One-Class SVM and k-means. [p. 17]
- Chaudhari, D., Agarwal, R., and Shukla, S. K. (2021) — Towards malicious address identification in Bitcoin. [p. 17]
- Shayegan, M. J., Sabor, H. R., Uddin, M., and Chen, C.-L. (2022) — A collective anomaly detection technique to detect crypto wallet frauds on Bitcoin network. [p. 17]
- Wu, J., Yuan, Q., Lin, D., You, W., Chen, W., Chen, C., and Zheng, Z. (2022) — Who are the phishers? Phishing scam detection on Ethereum via network embedding. [p. 17]
- Kanezashi, H., Suzumura, T., Liu, X., and Hirofuchi, T. (2022) — Ethereum fraud detection with heterogeneous graph neural networks. [p. 18]
- Liu, Z., Yang, D., Wang, S., and Su, H. (2024) — Adaptive multi-channel Bayesian graph attention network for IoT transaction security. [p. 18]
- Xiong, A., Tong, Y., Jiang, C., Guo, S., Shao, S., Huang, J., Wang, W., and Qi, B. (2024) — Ethereum phishing detection based on graph neural networks, achieving nearly 99% recall. [p. 18]
- Zhou, X., Yang, W., and Tian, X. (2023) — Detecting phishing accounts on Ethereum based on transaction records and EGAT, achieving up to 99.3% recall. [p. 18]
- Yu, T., Chen, X., Xu, Z., and Xu, J. (2022) — MP-GCN: a phishing nodes detection approach via graph convolution network for Ethereum. [p. 18]
- Li, S., Gou, G., Liu, C., Hou, C., Li, Z., and Xiong, G. (2022) — TTAGN: temporal transaction aggregation graph network for Ethereum phishing scams detection. [p. 18]
- Li, S., Zhou, J., Mo, C., Li, J., Tso, G. K. F., and Tian, Y. (2022) — Motif-aware temporal GCN for fraud detection in signed cryptocurrency trust networks. [p. 18]
- Patel, V., Pan, L., and Rajasegarar, S. (2020) — Graph deep learning based anomaly detection in Ethereum blockchain network. [p. 18]
- Pocher, N., Zichichi, M., Merizzi, F., Shafiq, M. Z., and Ferretti, S. (2023) — Detecting anomalous cryptocurrency transactions: an AML/CFT application of machine learning-based forensics. [p. 18]
- Bian, L., Zhang, L., Zhao, K., Wang, H., and Gong, S. (2021) — Image-based scam detection method using an attention capsule network, achieving 98.38% F1. [p. 18]
- Dutta, A., Voumik, L. C., Ramamoorthy, A., Ray, S., and Raihan, A. (2023) — Predicting cryptocurrency fraud using ChaosNet: the Ethereum manifestation. [p. 18]
- Tosunoglu, N., Abaci, H., Ates, G., and Akkaya, N. S. (2023) — Artificial neural network analysis of the day of the week anomaly in cryptocurrencies. [p. 18]
- Tao, B., Dai, H.-N., Xie, H., and Wang, F. L. (2023) — Structural identity representation learning for blockchain-enabled metaverse based on complex network analysis. [p. 18]
- Hu, H., Bai, Q., and Xu, Y. (2022) — SCSGuard: deep scam detection for Ethereum smart contracts using GRU with attention. [p. 18]
- Liu, M., Chen, H., and Yan, J. (2021) — Detecting roles of money laundering in Bitcoin mixing transactions: a goal modeling and mining framework. [p. 19]
- Shojaeinasab, A., Motamed, A. P., and Bahrak, B. (2023) — Mixing detection on Bitcoin transactions using statistical patterns, identifying over 92% of obfuscating transactions. [p. 19]
- Wu, L., Hu, Y., Zhou, Y., Wang, H., Luo, X., Wang, Z., Zhang, F., and Ren, K. (2021) — Towards understanding and demystifying Bitcoin mixing services. [p. 19]
- Tironsakkul, T., Maarek, M., Eross, A., and Just, M. (2022) — Context matters: methods for Bitcoin tracking. [p. 19]
- Nazzari, M. (2023) — From payday to payoff: exploring the money laundering strategies of cybercriminals, analysing Conti ransomware proceeds exceeding $11 million. [p. 19]
- Sheng, P., Wang, G., Nayak, K., Kannan, S., and Viswanath, P. (2021) — BFT protocol forensics, formalizing forensic support as a (m, k, d) triplet. [p. 20]
- Li, L., Chang, X., Liu, J., Liu, J., and Han, Z. (2021) — Bit2CV: a novel Bitcoin anti-fraud deposit scheme for connected vehicles. [p. 20]
- Liu, B., Szalachowski, P., and Zhou, J. (2021) — A first look into DeFi oracles. [p. 20]
- Nowostawski, M. and Tøn, J. (2019) — Evaluating methods for the identification of off-chain transactions in the Lightning Network, finding over 75% of 2-of-2 multisig transactions linked to LN. [p. 21]
- Tochner, S., Schmid, S., and Zohar, A. (2019) — Hijacking routes in payment channel networks: a predictability tradeoff, finding nearly 60% of routes pass through five nodes and 80% through ten nodes. [p. 21]
- Zhou, L., Qin, K., Torres, C. F., Le, D. V., and Gervais, A. (2021) — High-frequency trading on decentralized on-chain exchanges, finding a single attacker can achieve ~$3,414 daily revenue on Uniswap. [p. 21]
- Mansourifar, H., Chen, L., and Shi, W. (2020) — Hybrid cryptocurrency pump and dump detection. [p. 21]
- Fratrič, P., Sileno, G., Klous, S., and van Engers, T. (2022) — Manipulation of the Bitcoin market: an agent-based study. [p. 21]