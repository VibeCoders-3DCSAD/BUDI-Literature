---
paper_id: A--Alenazi-2023
first_author: "Alenazi"
year: 2023
title: "Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking"
venue: "Proceedings of the British Computer Society HCI International Conference (BCSHCI 2023), 1-12"
doi: 10.14236/ewic/BCSHCI2023.1
type: conference-paper
designation: algorithm
status: extracted
modules: [pfm_apps_overview, pfm_apps_features, pfm_apps_problems, income_expense_management, budgeting]
module_rationale:
  pfm_apps_overview: "Abstract, p. 1 and Sec. 3, pp. 2-3 define the reviewed artefact class and its selection procedure — 45 top-rated apps retained from 1335 identified on the UK Google Play Store and Apple Store by the PRISMA-style funnel in Fig. 1, p. 3."
  pfm_apps_features: "Sec. 4.1-4.3, pp. 3-6 and Tables 1-2, pp. 9-10 enumerate the coded functionality inventory: income, expense and transfer transactions, transaction accounts, categories and subcategories, budget names, budget amounts and budget periods."
  pfm_apps_problems: "Sec. 4.1, pp. 3-4 and Sec. 5.4, p. 7 document the reported deficiencies, namely conflated income and expense accounts, banking vocabulary that cannot express envelopes, 33 of 35 apps permitting transfers without sufficient funds, and only seven apps importing transactions automatically."
  income_expense_management: "Sec. 4.2, pp. 4-5 quantify the income and expense transaction machinery — 44 income, 45 expense and 35 transfer transaction apps, with app-provided and user-defined income and expense categories plus subcategories in 15 apps."
  budgeting: "Sec. 4.3, pp. 5-6 splits the corpus into 26 apps with money envelopes and 19 with a single balance, and Sec. 5.3, pp. 6-7 argues for multiple per-category budgets defined by amount, name and period."
---

# Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking

`A--Alenazi-2023` — Alenazi (2023), *Proceedings of the British Computer Society HCI International Conference (BCSHCI 2023), 1-12* \[10.14236/ewic/BCSHCI2023.1]

## Summary

A mental-accounting-lens functionality review of 45 top-rated personal budgeting apps finds that transaction tracking is near-universal while envelope-based budgeting is not, and that account terminology drawn from banking fails to express mental accounts.

## Problem and Motivation

Financial behaviour is deeply embedded in everyday life, yet for many people its success remains problematic, and the need for supporting tools is reflected in the growing number and popularity of budgeting apps (Abstract, p. 1). HCI research on money has focused mostly on exploratory studies of individuals and households whose findings indicate that people tend to use digital tools to a limited extent, so there is little understanding of how apps for personal budgeting could facilitate the tracking and monitoring of daily expenditures (Sec. 1, p. 1). Prior work has documented functionalities of marketplace apps in fitness, diet, depression, personal goals and digital wellbeing, but limited such work has looked at budgeting apps (Sec. 1, p. 1).

The authors supply the two gaps they target: no systematic feature inventory of top-rated budgeting apps, and little theoretical underpinning for such work, especially from the lens of mental accounting theory (Thaler, 1999), even though the value of behavioural economics had already been suggested for healthy choices, digital wellbeing and retirement savings (Sec. 2, p. 2). Mental accounting is introduced as the theory under which people partition and budget money separately in mental accounts usually materialized through money envelopes for specific purposes (Sec. 1, p. 1).

## Method

**Design.** Functionality review with a structured analytic lens: a three-keyword marketplace search, a PRISMA-style screening funnel, description analysis by the first author, and expert evaluation by both authors against mental accounting theory's constructs, with no user study
**Sample.** n = 45 budgeting apps retained from 1335 identified; n = 2 coders (first author for all 45, second author for a randomly selected 5-app iOS subset), functionally coded across the 20 features of Tables 1-2, pp. 9-10
**Context.** geography: United Kingdom marketplaces (Google Play Store and Apple Store); population: Not applicable — commercial mobile applications, no human participants; setting: Virtual/computational: manual expert feature evaluation on a Galaxy S21+ and an iPhone 12, with store descriptions as the primary evidence source

- Search the UK Google Play Store (Android) and Apple Store (iOS) with three keywords — budget, budgeting and finance — yielding 1335 apps (Fig. 1, p. 3).
- Screen in the stated order: remove duplicates (326), remove non-free apps (78), remove apps with fewer than 1000 reviews and a rating below 4.0 (810), remove apps unrelated to budgeting (71), and remove apps requiring access to the user's bank account (5), leaving 45 eligible apps (Fig. 1, p. 3; Sec. 3, pp. 2-3).
- Take the top-rated apps with an average rating score of four out of five and at least 1000 reviews; the retained set is 21 Google-Play-only apps and 24 apps available on both platforms (Sec. 3, p. 3).
- Analyse all apps' descriptions iteratively to identify broad functionalities such as tracking transactions and monitoring budgets, accepting that the descriptions restrict findings to those broad functionalities (Sec. 3, p. 3).
- Use mental accounting theory's constructs as the expert-evaluation codebook: funds (sources and uses), expenditures and categories for grouping them, and mental accounts or envelopes for allocating budgets to categories (Sec. 3, p. 3).
- Identify further functionalities iteratively over several months of discussion between the two authors — create transaction accounts, link the app to a real bank account, and set date, time and currency for transactions — reconciling the key concepts of transaction and transaction account through weekly conversations, notably that transactions cover income, expense and transfer, and that transaction accounts are containers holding all three types (Sec. 3, p. 3).
- Perform expert evaluation with the first author on all 45 apps using a Galaxy S21+, and the second author on five apps on an iPhone 12 selected at random from the 24 Apple Store apps, to discuss and reconcile the identified functionalities (Sec. 3, p. 3).
- Report functionality presence as raw app counts per feature, with premium-only functionality marked separately in the appendix tables (Tables 1-2, pp. 9-10).

## Software

- The 45 reviewed consumer budgeting apps (Google Play and Apple Store), listed by name and publisher in Appendix A, Tables 1-2, pp. 9-10; versions Not reported (store listings accessed 1 April 2022)
- GnuCash, one of the 45 apps, was the only one separating income, expense and asset accounts (Sec. 4.1, p. 4)
- No analysis software, scripting, or statistical package is named anywhere in the paper

## Key Findings

- num: Abstract, p. 1 states that all apps support tracking of transactions and that one third of the apps do not support budgeting informed by money envelopes; Sec. 4.3, p. 5 gives the underlying counts as 26 apps with money envelopes and 19 without, so the printed share is 19 of 45 rather than one third.
- num: Sec. 4, p. 3 splits the corpus into 8 apps that only track expenses without monitoring and 33 that also monitor expenses against an allocated budget.
- num: Sec. 4.1, p. 3 reports 44 apps supporting depositing funds, 45 supporting paying for expenses and only 11 supporting saving, with 41 apps conflating the income and expense account into one container.
- num: Sec. 4.1, p. 3 counts banking-domain account labels across the corpus as virtual cash accounts (17), virtual credit card account (17), virtual debt account (13), saving accounts (11), virtual bank accounts (9) and investment accounts (7), with 18 apps using more than one such term.
- num: Sec. 4.1, pp. 3-4 reports that only seven apps support integration with online banking services, and only as a premium feature, which the authors read as evidence that the banking vocabulary is not earned by banking-level functionality.
- num: Sec. 4.1, p. 4 finds that only GnuCash uses terms that clearly distinguish available-funds, wealth and expense accounts; three apps use wallet, one financial account, one payment account and two budget.
- num: Sec. 4.2, p. 4 reports 44 apps creating income transactions, 43 supporting the income date, 18 the income time and 40 the income currency, split into 12 apps with per-transaction currency choice and 28 with settings-level currency.
- num: Sec. 4.2, p. 5 reports 45 apps creating expense transactions with an amount and a date, 18 supporting the time and 41 the currency; only four apps ask for the payment method.
- num: Sec. 4.2, p. 5 reports 35 apps supporting transfer transactions, of which 33 permit a transfer larger than the funds available in the source account.
- num: Sec. 4.2, p. 5 reports app-provided categories in 38 apps for income and 40 for expense, user-defined categories in 36 and 42 apps, one-off categories in four and two apps, and subcategories for transactions in 15 apps.
- num: Sec. 4.2, p. 5 reports that all 45 apps accept manual entry while only seven import transactions automatically from linked online banking accounts and only seven encourage comparison with bank statements.
- num: Sec. 4.3, p. 5 reports that all 19 single-budget apps show overspending with a minus sign, but eight do not change its colour, while only seven colour it red.
- num: Sec. 4.3, p. 6 reports that 15 of the 26 multiple-budget apps allow a custom budget name while 11 reuse the expense category name, and that budget periods are available as daily in seven apps, weekly in 15, fortnightly in 26, biannually in three and annually in 14, with 17 apps offering several periods and six accepting a user-specified date.
- qual: Sec. 4, p. 3 reports that only Goodbudget and SimpleBudget mention envelope systems in their descriptions, that neither cites mental accounting theory, and that no app's description reports any evaluation through user studies.
- qual: Sec. 5.4, p. 7 argues that budgeting apps prioritize cognitive operations over financial behaviours, and grounds the critique in the small number of apps that integrate online banking for automatic import of real transactions.
- qual: Sec. 5.3, pp. 6-7 draws on Snow and Vyas's envelope and jar studies to argue that digital envelopes have been overlooked because prior work treated those artefacts as material storage for specific purposes rather than as materialization of mental accounts.

## Key Figures and Tables

- Figure 1 (p. 3): PRISMA diagram of the app selection funnel, 1335 → 931 → 121 → 50 → 45 → the only quantitative result figure in the paper, and the source of every selection count.
- Table 1 (Appendix A, p. 9): main functionalities and subfunctionalities of funds and expenses for the 45 apps, 11 numbered columns covering funds and expense transaction tracking, account creation, funds and expense categories, currency, date and time → the per-app codebook underlying the §4.1 and §4.2 counts.
- Table 2 (Appendix A, p. 10): main functionalities and subfunctionalities of transaction accounts, transfers between them, and the types of provided budgets, 15 numbered columns with `*` marking premium-only features → the per-app codebook underlying the §4.3 budget counts.
- No chart, plot or model diagram appears anywhere in the paper; results are counts only.

## Limitations and Gaps

- [unacknowledged] The paper's own headline figure disagrees with its own counts: the abstract says "one third of the apps do not support budgeting informed by money envelopes" (p. 1), while the results (p. 5) reports 26 envelope apps and 19 non-envelope apps out of 45, i.e. a little over two fifths, not one third.
- [unacknowledged] The results (p. 5) assert "all apps support budgeting functionality and therefore the monitoring of expenses against the allocated budgets (45 apps)", which contradicts the 8-versus-33 split reported three paragraphs earlier on p. 3 and the same page's 19-versus-26 split; the discussion (p. 6) then says "a few do not support budgeting" and the conclusion (p. 7) says apps monitor against available funds or allocated budget, so three different totals coexist.
- [unacknowledged] The single-budget count is inconsistent across the paper: the results section (p. 5) classifies 19 apps as single-budget, but Table 2, p. 10 has a "Create single budget" column from which the text (p. 3) reads only seven apps, with 26 multiple-budget apps; four of the 19 are said to support multiple budgets only as premium.
- [unacknowledged] Column references in the body text do not match the appendix numbering: the text cites "Table 2, col 10" for single-budget creation and "col 13" for budget period (pp. 3, 5), while the Table 2 header on p. 10 numbers Create single budget as column 12, Create multiple budgets as column 13 and Set budget period as column 14.
- [unacknowledged] The PRISMA funnel does not account for the retained cross-platform apps: Fig. 1, p. 3 leaves "50 Remaining (Google Play only)" before excluding five bank-access apps to yield 45, whereas §3, p. 3 states the 45 comprise 21 Google-Play-only apps and 24 apps on both platforms.
- [unacknowledged] No user study, no usability test and no in-app behavioural data were collected, so the paper reports feature presence only and cannot say whether any of these functionalities is used, understood or effective; it says so only implicitly by noting that no app's description reports evaluation through user studies (Sec. 4, p. 3).
- [unacknowledged] Every count is a raw presence tally with no second-coder agreement statistic, so the reliability of the two-coder classification is asserted ("discuss and reconcile", Sec. 3, p. 3) but never quantified.
- [unacknowledged] The corpus is drawn from UK storefronts in one snapshot (accessed 1 April 2022) with a rating-and-review filter, so apps popular outside the UK storefronts, paid-only apps and apps below 1000 reviews are outside the frame by construction.
- [unacknowledged] App versions are not recorded, so all feature counts describe whatever build the store served in April 2022 and may not hold for later releases.
- [unacknowledged] The paper evaluates only manual tracking and static budget monitoring: no reviewed app is examined for forecasting, prediction, spending irregularity detection, or any algorithmic component, so absence of such features is a property of the chosen codebook rather than a finding about app capability.
- The authors frame the contribution as new knowledge for design rather than as an evaluation against a benchmark, and no competing apps or prior feature inventories are quantitatively compared (Abstract, p. 1; Sec. 6, p. 7).

## Definitions

- **Mental accounting** — the behavioural economics theory under which people partition and budget money separately in mental accounts usually materialized through money envelopes for specific purposes (Sec. 1, p. 1).
- **Money envelope** — an analogue budgeting container whose name states the purpose of the money stored in it, such as grocery money (Sec. 2, p. 2).
- **Mental account** — the theory's labelled category for a purpose-specific sum, used here as the theoretical counterpart of an app budget (Sec. 4.1, p. 3).
- **Money-in / money-out / wealth account** — the three account types the paper derives from mental accounting: storing available funds such as income, storing assets or wealth, and using available funds for spending (Sec. 4.1, p. 3).
- **Transaction account** — the app-side container that holds the three transaction types; the paper's proposed vocabulary separates these from the user's real bank account (Sec. 3, p. 3; Sec. 5.4, p. 7).
- **Income / expense / transfer transaction** — the paper's three transaction types: depositing funds, paying for expenses, and transferring money from a source account to a destination account (Sec. 4.2, p. 4).
- **Single budget** — the app pattern where one main budget, usually equal to the available funds, covers all expenses regardless of category (Sec. 4.3, p. 5).
- **Multiple budgets** — the app pattern aligning with mental accounting, where users allocate a different budget to each expense category such as bills, rent or groceries (Sec. 4.3, pp. 5-6).
- **Premium functionality** — the paywall-gated subset of features, marked `*` in Table 2, p. 10; four of the multiple-budget apps and the bank-linking feature are premium-only (Sec. 4.3, p. 6; Sec. 4.1, p. 4).
- **Top-rated** — the inclusion filter of an average rating score of four out of five with at least 1000 reviews (Sec. 3, pp. 2-3).

## Key Equations

Not applicable — the paper reports feature-presence counts and design implications only, and contains no formal model, formula or metric definition.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Apps identified in the marketplace search | apps | 1335 | — | — | Fig. 1, p. 3 |
| Apps identified from Google Play Store | apps | 742 | — | — | Fig. 1, p. 3 |
| Apps identified from Apple Store | apps | 593 | — | — | Fig. 1, p. 3 |
| Apps excluded as duplicates | apps | 326 | — | — | Fig. 1, p. 3 |
| Duplicates excluded from Google Play Store | apps | 191 | — | — | Fig. 1, p. 3 |
| Duplicates excluded from Apple Store | apps | 128 | — | — | Fig. 1, p. 3 |
| Duplicates present on both stores | apps | 7 | — | — | Fig. 1, p. 3 |
| Apps excluded as not free | apps | 78 | — | — | Fig. 1, p. 3 |
| Non-free apps excluded from Google Play Store | apps | 18 | — | — | Fig. 1, p. 3 |
| Non-free apps excluded from Apple Store | apps | 60 | — | — | Fig. 1, p. 3 |
| Apps excluded for fewer than 1000 reviews and rating below 4.0 | apps | 810 | — | — | Fig. 1, p. 3 |
| Low-review and low-rating exclusions on Google Play Store | apps | 439 | — | — | Fig. 1, p. 3 |
| Low-review and low-rating exclusions on Apple Store | apps | 371 | — | — | Fig. 1, p. 3 |
| Apps excluded as unrelated to budgeting | apps | 71 | — | — | Fig. 1, p. 3 |
| Unrelated apps excluded from Google Play Store | apps | 44 | — | — | Fig. 1, p. 3 |
| Unrelated apps excluded from Apple Store | apps | 27 | — | — | Fig. 1, p. 3 |
| Apps remaining after duplicate, price, rating and relevance screens | apps | 931 | — | — | Fig. 1, p. 3 |
| Google Play apps remaining at that stage | apps | 533 | — | — | Fig. 1, p. 3 |
| Apple Store apps remaining at that stage | apps | 398 | — | — | Fig. 1, p. 3 |
| Apps remaining after the rating-and-review screen | apps | 121 | — | — | Fig. 1, p. 3 |
| Google Play apps remaining at that stage | apps | 94 | — | — | Fig. 1, p. 3 |
| Apple Store apps remaining at that stage | apps | 27 | — | — | Fig. 1, p. 3 |
| Apps remaining on Google Play only before the bank-access screen | apps | 50 | — | — | Fig. 1, p. 3 |
| Apps excluded for requiring access to the user's bank account | apps | 5 | — | — | Fig. 1, p. 3 |
| Apps eligible for analysis | apps | 45 | — | — | Fig. 1, p. 3; Sec. 3, p. 3 |
| Retained apps available only on Google Play Store | apps | 21 | — | — | Sec. 3, p. 3 |
| Retained apps available on both platforms | apps | 24 | — | — | Sec. 3, p. 3 |
| Retained apps in the Finance marketplace category | apps | 44 | — | — | Sec. 4, p. 3 |
| Retained apps in the Business marketplace category | apps | 1 | — | — | Sec. 4, p. 3 |
| Apps whose descriptions were analysed by the first author | apps | 45 | — | — | Sec. 3, p. 3 |
| Apps expert-evaluated by the first author on Galaxy S21+ | apps | 45 | — | — | Sec. 3, p. 3 |
| Apps independently expert-evaluated by the second author on iPhone 12 | apps | 5 | — | — | Sec. 3, p. 3 |
| Transaction-tracking support, all apps | apps | 45 | — | — | Abstract, p. 1; Sec. 4, p. 3 |
| Apps tracking expenses without monitoring a budget | apps | 8 | — | — | Sec. 4, p. 3 |
| Apps also monitoring expenses against an allocated budget | apps | 33 | — | — | Sec. 4, p. 3 |
| Apps supporting budgeting functionality and budget monitoring | apps | 45 | — | — | Sec. 4.3, p. 5 |
| Apps supporting budgeting via money envelopes | apps | 26 | — | — | Sec. 4.3, p. 5 |
| Apps not supporting envelope-based budgeting | apps | 19 | — | — | Sec. 4.3, p. 5 |
| Abstract's stated share of apps without envelope budgeting | share | one third | — | — | Abstract, p. 1 |
| Apps with money envelopes available only as a premium feature | apps | 4 | — | — | Sec. 4, p. 3 |
| Apps whose descriptions mention an envelope-system design basis | apps | 2 | — | — | Sec. 4, p. 3 |
| Apps whose descriptions report evaluation through user studies | apps | 0 | — | — | Sec. 4, p. 3 |
| Apps supporting creation of a funds account | apps | 44 | — | — | Sec. 4.1, p. 3 |
| Apps supporting creation of an expense account | apps | 45 | — | — | Sec. 4.1, p. 3 |
| Apps supporting creation of a saving account | apps | 11 | — | — | Sec. 4.1, p. 3 |
| Apps with a funds or expense account, although the two are conflated in use | apps | 41 | — | — | Sec. 4.1, p. 3 |
| Apps that only deposit funds on the home screen instead of a dedicated account | apps | 4 | — | — | Sec. 4.1, p. 3 |
| Apps labelled "virtual bank accounts" | apps | 9 | — | — | Sec. 4.1, p. 4 |
| Apps labelled "virtual cash accounts" | apps | 17 | — | — | Sec. 4.1, p. 4 |
| Apps labelled "saving accounts" | apps | 11 | — | — | Sec. 4.1, p. 4 |
| Apps labelled "investment accounts" | apps | 7 | — | — | Sec. 4.1, p. 4 |
| Apps labelled "virtual credit card account" | apps | 17 | — | — | Sec. 4.1, p. 4 |
| Apps labelled "virtual debt account" | apps | 13 | — | — | Sec. 4.1, p. 4 |
| Apps using more than one banking-domain account term | apps | 18 | — | — | Sec. 4.1, p. 4 |
| Apps supporting integration with users' online banking services | apps | 7 | — | — | Sec. 4.1, p. 4 |
| Apps using the everyday-practice term "wallet" for an account | apps | 3 | — | — | Sec. 4.1, p. 4 |
| Apps using the term "financial account" | apps | 1 | — | — | Sec. 4.1, p. 4 |
| Apps using the term "payment account" | apps | 1 | — | — | Sec. 4.1, p. 4 |
| Apps using the term "budget" as an account label | apps | 2 | — | — | Sec. 4.1, p. 4 |
| Apps with terminology that clearly separates funds, wealth and expense accounts | apps | 1 | — | — | Sec. 4.1, p. 4 |
| Apps allowing creation of income transactions | apps | 44 | — | — | Sec. 4.2, p. 4 |
| Apps allowing the income transaction date to be set | apps | 43 | — | — | Sec. 4.2, p. 4 |
| Apps allowing the income transaction time to be set | apps | 18 | — | — | Sec. 4.2, p. 4 |
| Apps allowing the income transaction currency to be set | apps | 40 | — | — | Sec. 4.2, p. 4 |
| Apps offering a per-transaction currency list | apps | 12 | — | — | Sec. 4.2, p. 4 |
| Apps offering only a settings-level currency list | apps | 28 | — | — | Sec. 4.2, p. 4 |
| Apps allowing creation of expense transactions | apps | 45 | — | — | Sec. 4.2, p. 5 |
| Apps allowing the expense transaction amount to be set | apps | 45 | — | — | Sec. 4.2, p. 5 |
| Apps allowing the expense transaction date to be set | apps | 45 | — | — | Sec. 4.2, p. 5 |
| Apps allowing the expense transaction time to be set | apps | 18 | — | — | Sec. 4.2, p. 5 |
| Apps allowing the expense transaction currency to be set | apps | 41 | — | — | Sec. 4.2, p. 5 |
| Apps asking for the payment method on an expense transaction | apps | 4 | — | — | Sec. 4.2, p. 5 |
| Apps entering income and expense through one plus icon | apps | 35 | — | — | Sec. 4.2, p. 5 |
| Apps entering income and expense through separate home-screen buttons | apps | 8 | — | — | Sec. 4.2, p. 5 |
| Apps entering transactions through a register button opening a new page | apps | 1 | — | — | Sec. 4.2, p. 5 |
| Apps using a drag interaction for expense entry | apps | 1 | — | — | Sec. 4.2, p. 5 |
| Apps supporting transfer transactions | apps | 35 | — | — | Sec. 4.2, p. 5 |
| Apps supporting the transfer amount | apps | 35 | — | — | Sec. 4.2, p. 5 |
| Apps supporting the transfer date | apps | 30 | — | — | Sec. 4.2, p. 5 |
| Apps supporting the transfer time | apps | 11 | — | — | Sec. 4.2, p. 5 |
| Apps supporting the transfer currency | apps | 25 | — | — | Sec. 4.2, p. 5 |
| Apps attaching a label to a transfer | apps | 5 | — | — | Sec. 4.2, p. 5 |
| Apps attaching a receipt to a transfer, premium only | apps | 3 | — | — | Sec. 4.2, p. 5 |
| Apps permitting a transfer larger than the source account's funds | apps | 33 | — | — | Sec. 4.2, p. 5 |
| Apps blocking a transfer when funds are insufficient | apps | 1 | — | — | Sec. 4.2, p. 5 |
| Apps providing app-defined income categories | apps | 38 | — | — | Sec. 4.2, p. 5 |
| Apps providing app-defined expense categories | apps | 40 | — | — | Sec. 4.2, p. 5 |
| Apps allowing user-defined income categories | apps | 36 | — | — | Sec. 4.2, p. 5 |
| Apps allowing user-defined expense categories | apps | 42 | — | — | Sec. 4.2, p. 5 |
| Apps allowing only one-off income categories | apps | 4 | — | — | Sec. 4.2, p. 5 |
| Apps allowing only one-off expense categories | apps | 2 | — | — | Sec. 4.2, p. 5 |
| Apps supporting subcategories for transactions | apps | 15 | — | — | Sec. 4.2, p. 5 |
| Apps accepting manually entered transactions | apps | 45 | — | — | Sec. 4.2, p. 5 |
| Apps importing transactions automatically from linked bank accounts | apps | 7 | — | — | Sec. 4.2, p. 5 |
| Apps encouraging comparison of entered transactions with bank statements | apps | 7 | — | — | Sec. 4.2, p. 5 |
| Single-budget apps signalling overspending with a minus symbol | apps | 19 | — | — | Sec. 4.3, p. 5 |
| Single-budget apps that leave the overspending indicator uncoloured | apps | 8 | — | — | Sec. 4.3, p. 5 |
| Single-budget apps colouring the overspending indicator red | apps | 7 | — | — | Sec. 4.3, p. 5 |
| Single-budget apps exposing the fund as an explicit named budget | apps | 5 | — | — | Sec. 4.3, p. 5 |
| Explicit single-budget apps supporting a daily period | apps | 1 | — | — | Sec. 4.3, p. 5 |
| Explicit single-budget apps supporting a weekly period | apps | 2 | — | — | Sec. 4.3, p. 5 |
| Explicit single-budget apps supporting a monthly period | apps | 4 | — | — | Sec. 4.3, p. 5 |
| Explicit single-budget apps supporting a yearly period | apps | 1 | — | — | Sec. 4.3, p. 5 |
| Explicit single-budget apps supporting a user-defined period | apps | 1 | — | — | Sec. 4.3, p. 5 |
| Apps creating a single budget, per the body's table citation | apps | 7 | — | — | Sec. 4, p. 3; Table 2, col 10 |
| Multiple-budget apps allowing a customized budget name | apps | 15 | — | — | Sec. 4.3, p. 6 |
| Multiple-budget apps reusing the expense category as the budget name | apps | 11 | — | — | Sec. 4.3, p. 6 |
| Multiple-budget apps offering a daily budget period | apps | 7 | — | — | Sec. 4.3, p. 6 |
| Multiple-budget apps offering a weekly budget period | apps | 15 | — | — | Sec. 4.3, p. 6 |
| Multiple-budget apps offering a fortnightly budget period | apps | 26 | — | — | Sec. 4.3, p. 6 |
| Multiple-budget apps offering a biannual budget period | apps | 3 | — | — | Sec. 4.3, p. 6 |
| Multiple-budget apps offering an annual budget period | apps | 14 | — | — | Sec. 4.3, p. 6 |
| Multiple-budget apps offering several predefined periods | apps | 17 | — | — | Sec. 4.3, p. 6 |
| Multiple-budget apps accepting a user-specified budget start date | apps | 6 | — | — | Sec. 4.3, p. 6 |
| Apps supporting forecasting, prediction or any algorithmic component | apps | Not assessed | — | — | Sec. 4.1-4.3, pp. 3-6 |
| Inferential statistic reported for any functionality count | CI or p-value | Not reported | — | — | Sec. 4, pp. 3-6 |
| Inter-coder agreement statistic for the two-coder classification | agreement | Not reported | — | — | Sec. 3, p. 3 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "a functionality review from the lens of mental accounting theory of 45 top-rated budgeting apps selected from 1335 apps on Google Play Store and Apple Store" | Abstract, p. 1 | pfm_apps_overview |
| "Findings indicate that while all apps support tracking of transactions, one third of the apps do not support budgeting informed by money envelopes." | Abstract, p. 1 | pfm_apps_problems |
| "Mental accounting is a behavioural economics theory according to which people commonly partition and budget money separately in mental accounts usually materialized through money envelopes for specific purposes." | Sec. 1, p. 1 | budgeting |
| "the main purpose of mental accounting is to use labelled categories for sources such as regular income and uses of funds such as food, to help individuals and households organize their spending" | Sec. 1, p. 1 | budgeting |
| "our findings indicate insufficient support for budgeting functionality and important challenges of such apps due to the overlapping meanings and insufficient clarity of the key concepts" | Sec. 1, p. 1 | pfm_apps_problems |
| "we removed duplicates, apps that were not free, apps not related to budgeting, those requiring access to one's bank accounts and retained top-rated apps with an average rating score of four out of five" | Sec. 3, pp. 2-3 | pfm_apps_overview |
| "The limited information available in the apps' descriptions was rather restricted to these broad functionalities." | Sec. 3, p. 3 | pfm_apps_features |
| "While most functionalities were easily identified by each of them from apps' descriptions, functionalities reflecting the key concepts of transactions and accounts required additional clarification through weekly conversations" | Sec. 3, p. 3 | pfm_apps_overview |
| "two main types of budgeting apps, those that provide functionality of tracking expenses without monitoring (8 apps) and those that provide also the budgeting functionality for monitoring expenses against their allocated budget (33 apps)" | Sec. 4, p. 3 | budgeting |
| "Most of the apps show limited theoretical underpinning, with only two apps Goodbudget and SimpleBudget explicitly mentioning in their description that their design was informed by money envelope systems" | Sec. 4, p. 3 | budgeting |
| "for most of the apps, the income and expense accounts, although conceptually distinct, in practice they tend to be one and the same account similar to a bank account or a wallet" | Sec. 4.1, p. 4 | pfm_apps_problems |
| "the direct association with banking practices is limited since only seven apps support the integration of the budgeting apps with users' online banking services and only as premium feature" | Sec. 4.1, p. 4 | pfm_apps_problems |
| "this terminology from banking domain also fails to provide specific types of expense accounts such as those for different categories of expenses or the equivalent of money envelopes" | Sec. 4.1, p. 4 | pfm_apps_problems |
| "Interestingly, most of the apps supporting transfer transactions allow them without sufficient funds in the source account (33 apps out of 35)." | Sec. 4.2, p. 5 | pfm_apps_problems |
| "Findings indicate that all apps support budgeting functionality and therefore the monitoring of expenses against the allocated budgets (45 apps), although they do so in different ways." | Sec. 4.3, p. 5 | budgeting |
| "While most of these apps support budgeting under mental accounts or money envelopes (26 apps), others do not (19 apps)." | Sec. 4.3, p. 5 | budgeting |
| "While all 19 apps use the account balance to represent the overspent of available funds using the minus symbol, eight apps do not change the colour of this information, albeit seven apps use colour red" | Sec. 4.3, p. 5 | pfm_apps_features |
| "spending money from a general pot rather than specific pots for different expense categories, can more easily lead to over expenditure" | Sec. 5, p. 6 | budgeting |
| "The lack of support for differentiating among these distinct types of account is problematic." | Sec. 5, p. 6 | pfm_apps_problems |
| "While all budgeting apps support the tracking of expenses, a few do not support budgeting" | Sec. 5, p. 6 | pfm_apps_problems |
| "Such functions however prioritize cognitive operations rather than financial behaviours themselves." | Sec. 5.4, p. 7 | pfm_apps_problems |
| "This indicates limited support for encouraging users to compare their entered transactions with those in bank statements." | Sec. 5.4, p. 7 | pfm_apps_problems |
| "we strongly call for better design for budgeting app articulating the concept of mental accounting and support the use of money envelopes with allocated budget" | Sec. 5.3, p. 7 | budgeting |
| "Findings suggest the value of more nuanced vocabulary for describing the key concepts of accounts, transactions and budgets as informed by mental accounting theory" | Sec. 6, p. 7 | pfm_apps_features |

## Remember This

- Corpus is 45 top-rated UK-store apps retained from 1335 through a PRISMA funnel; evidence is store descriptions plus two-author expert evaluation, with no user study.
- The paper's central finding is an asymmetry: 45 apps support transaction tracking, but only 26 support money-envelope budgets and 19 do not.
- Banking-flavoured account labels are the norm (17 virtual cash accounts, 17 virtual credit card, 13 virtual debt) while only GnuCash separates funds, wealth and expense accounts.
- Only 7 apps import transactions from a bank and only 7 encourage comparison with statements, which is the basis for the "cognitive rather than behavioural" critique.
- The 19 single-budget apps mostly flag overspending with a minus sign only, and 33 of 35 transfer-capable apps permit transfers beyond available funds.

## Cited Works

- Thaler, R. H. (1999) (methodology) — Mental accounting theory supplies the paper's entire analytic lens and its account, transaction and envelope vocabulary. [Sec. 1, p. 1]
- Kaye, J. J.; Chen, K.; Evans, A. (2014) (methodology) — Money talks: tracking finances, the primary source for analogue tracking tools and participants discontinuing budgeting apps. [Sec. 1, p. 1; Sec. 2, p. 2]
- Snow, S. C.; Vyas, A. (2015a) (methodology) — Envelope, jar and coin-jar studies underpinning the paper's argument that digital envelopes are missing. [Sec. 2, p. 2; Sec. 5.3, p. 7]
- Vyas, A.; Chippendale, L.; Lewis, A.; et al. (2016) (methodology) — Analogue budgeting and tracking tools across individuals and households. [Sec. 2, p. 2]
- Lewis, M.; Perry, M. (2019) (methodology) — Follow the money: managing personal finance digitally, cited for limited digital tool use. [Sec. 1, p. 1]
- Vines, R.; Dunphy, P.; Monk, A. (2014) (methodology) — Exploratory HCI work on money and financial practices establishing the limited-digital-use baseline. [Sec. 1, p. 1]
- Bitrián, P.; Buil, I.; Catalán, S. (2021) (methodology) — Gamification of PFM apps, cited for budgeting apps being a fast-growing finance-app category. [Sec. 1, p. 1]
- QYResearch (no date) (methodology) — Supplies the $1.4M 2018 global revenue and 2025 doubling estimate for budgeting tools. [Sec. 1, p. 1]
- Lolla, S.; Sas, C. (2023) (methodology) — Evaluating mobile apps targeting personal goals, the closest methodological precedent for a marketplace functionality review. [Sec. 1, p. 1]
- Almoallim, S.; Sas, C. (2022) (methodology) — Functionality review of digital wellbeing apps, the same lab's precedent for coding marketplace apps against a theory. [Sec. 1, p. 1]
- Chung, A. E.; et al. (2018) (methodology) — Health and fitness app content analysis, cited as prior marketplace-app functionality methodology. [Sec. 1, p. 1]
- Stockinger, K.; et al. (2013) (methodology) — Behavioural economics previously suggested for healthier choices, cited to show the theory was under-used in HCI. [Sec. 2, p. 2]
- Lee, M. K.; Kiesler, S.; Forlizzi, J. (2011) (methodology) — Mining behavioral economics to design persuasive technology for healthy choices. [Sec. 2, p. 2]
- Gunaratne, J.; Nov, O. (2015) (methodology) — Behaviour theory-driven interfaces for retirement saving performance, cited as prior behavioural-economics HCI work. [Sec. 2, p. 2]
- Partners, D. (no date) (methodology) — Goodbudget app, one of only two whose description cites an envelope-system design basis. [Sec. 4, p. 3]
- Tanu, F. (2011) (methodology) — SimpleBudget (Envelope Budget), the other envelope-citing app and the only one without an income account. [Sec. 4.2, p. 4]

---

Conversion: [`A--Alenazi-2023_marked.md`](../../literature/paper-markdowns/A--Alenazi-2023_marked.md)