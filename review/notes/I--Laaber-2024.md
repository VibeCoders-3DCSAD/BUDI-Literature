---
paper_id: I--Laaber-2024
first_author: Laaber
year: 2024
title: "Testing Medical Rules Web Services in Practice"
venue: "arXiv preprint arXiv:2412.11731 [cs.SE]"
doi: 10.48550/arXiv.2412.11731
type: preprint
designation: algorithm
status: extracted
modules: [rule_based_classification]
module_rationale:
  rule_based_classification: "Evaluates automated testing of a medical rule engine (GURI) that executes rule-based logic; the study uses expected-output oracles for system-level testing."
---
`I--Laaber-2024` — Laaber, Ali, Schwitalla, and Nygård (2024), arXiv:2412.11731 [cs.SE].

## Summary

This preprint evaluates automated system-level testing of GURI, the Cancer Registry of Norway's medical rule engine implemented as web services. The authors compare EvoMaster in black-box and white-box modes with a domain-specific tool EvoGURI across ten versions of GURI, measuring code coverage, errors found, domain-specific rule coverage, and ability to identify artificial faults. The testing uses expected-output oracles derived from the rule engine's behavior/domain knowledge.

## Problem and Motivation

Manual testing of evolving medical rule systems is costly and error-prone. The study investigates whether automated test generation can effectively test rule-based medical web services in practice.

## Method

**Design.** Empirical evaluation of automated test generation tools on a real industrial system (case study).  
**Sample.** Ten versions of the GURI medical rule engine (Cancer Registry of Norway).  
**Context.** Geography: Norway; population: Not reported; setting: medical rule engine web services for cancer registry data processing.

- Apply EvoMaster (black-box and white-box) and EvoGURI to generate tests for GURI.
- Evaluate effectiveness via code coverage, errors found, domain-specific rule coverage, and fault-detection on artificial faults.
- Compare tool performance across ten versions of the system.

## Key Findings

- All tools achieve similar code coverage; differences emerge in error discovery and domain-specific rule coverage.
- Automated testing can find errors and exercise medical rules in practice.
- The domain-specific EvoGURI variant can leverage domain knowledge for rule-focused testing.

## Limitations and Gaps

- Uses expected-output/system-level testing with oracles; the study does not evaluate equivalence partitioning or boundary value analysis as test design techniques for deriving test cases from input domains.
- Preprint, not peer reviewed; results may change in final publication.

## Definitions

Not reported.

## Key Equations

Not reported.

## Statistical Evidence

Not reported.

## Quotes

Not reported.

## Remember This

- Tests a medical rule engine (rule-based system) with automated system-level tests.
- Uses expected-output oracles; not a study of EP/BVA techniques.
- Evaluated on ten versions of GURI from Cancer Registry of Norway.

## Cited Works

- Not reported.

---

Conversion: [Laaber et al., 2024_marked.md](../../literature/mds/Laaber et al., 2024_marked.md)
