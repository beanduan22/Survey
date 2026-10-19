# Contribution and evidence codebook

The active CSV describes evaluated work-role contributions, not one row per method variant or model. Preprint and archival versions are merged by work; an attack is split when different entry surfaces are evaluated. Missing mitigation evaluations are added as defense roles, without counting every compared baseline as another contribution.

## Roles and result types

- Attack: induced prediction failure, insecure output, resource abuse or unauthorized action; includes fixed malicious-request evaluations.
- Risk study: measurement of output security, training membership, extraction, provenance or ecosystem exposure. Diagnostic privacy probes remain here even when the original paper calls them attacks.
- Defense: an evaluated preventive, detective, corrective or owner-protection intervention. Utility-only mitigation studies are identified in their notes; their role does not establish attack reduction.
- Evaluation resource: a repository/project benchmark reporting both functional and security outcomes. Other reusable fragment benchmarks retain their measured attack, risk or defense role.
- PRED: prediction/detection/ranking; GEN: generated artifact; MIX: both; AGT: actions are security outcomes; OBS: existing artifacts measured without victim queries. These describe measured results independently of system form.

## Preservation

- A: stated construction argument under a named contract. It is not a correctness certificate.
- T: original/transformed behavior compared on shared inputs or an expected-output oracle. Coverage and observables are retained separately.
- F: formal equivalence under a stated operational model, including bounded local blocks.
- U: required premise unsupported for the whole evaluated family. Locally justified operators may be discussed without upgrading lossy or syntax-breaking operators.
- --: no coded preservation-dependent program transformation. The applicability/status fields distinguish inspected inapplicability from unresolved coverage.

The preserved property may be a task label, normal functional output, or an already malicious payload under obfuscation. It is not automatically all observable behavior. Parsing/compilation is a separate validity field. Clean functional tests of newly generated programs alone do not supply T for transformed input programs. Tags are multi-label.

## Outcome oracles

R: separately measured model/task score; L: lexical/statistical matching or human/LLM judgment; C: parsing/type/compilation measured as an outcome; S: actual static program analysis; X: observed execution or tests; E: demonstrated security/availability effect; F: a formal outcome-property guarantee. NR: exact oracle unresolved and not included in channel totals. A numerical rate derived from one oracle does not automatically add R.

Execution purpose distinguishes benign utility, transformed-input checking, generated payload testing and agent action. A helper run or command match alone does not establish every downstream effect in a threat model. A detector bound, robustness certificate, DP guarantee and cryptographic channel guarantee concern different properties.

## Source status

- protocol_checked: the named inspected primary methods/results support this decision. The decision's scope is the stated source version.
- targeted_source_check: the retained prior audit inspected a specific claim/protocol; this is not a whole-paper certification.
- version_partial: a named primary version was read, but its relationship to the archived/latest in-cutoff protocol remains limited.
- protocol_partial / protocol_partial_oracle: only some named primary passages were accessible or the oracle remains unresolved.
- source_unavailable: eligible identity/abstract retained; full protocol not established.

protocol_audit_detail retains the original granular check status. protocol_source_url, protocol_source_version and protocol_locator identify the evidence. Legacy role_audit_* fields retain the earlier role-screening layer; protocol_* fields describe the later detailed pass. Raw P0--P4 values exist only in the preserved initial extraction and are not the active coding scheme.

All checks in this revision are model assisted. author_review.csv contains blank fields for actual human decisions; no duplicate-human agreement or kappa has been claimed.

## Final source filter

Five works and all seven of their attack/defense contributions were excluded at the author's request after full protocols or cutoff-version correspondence could not be verified. The current CSV contains only retained contributions. source_exclusions.csv records the five work-level decisions; excluded_records.csv also includes the two earlier role/scope exclusions. Historical search and audit files retain their original decisions, independently of this final filter.

## Search scope

The cutoff is 2026-06-30. A logged supplementary public-index search ran on 2026-10-19 with 16 DBLP/arXiv-restricted queries. Its 107 distinct returns include 18 nonstudy landings, 21 already included studies, 17 newly included works, five secondary reviews, five later works, 40 scope exclusions and one unresolved-cutoff entry. Three further works were included through documented primary-source follow-ups. No initial PRISMA flow, database-wide hit count or complete historical exclusion ledger is reconstructed.
