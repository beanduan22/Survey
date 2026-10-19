> Historical review before the five-work filter. Current corpus and validation are recorded in verification_report.md and final_validation.json.

# Final bounded evidence review — 2026-10-19

Reviewer: independent model protocol check (GPT-6.1); not a second human coder or an inter-rater reliability exercise.

Target: `repo:manuscript/Neural_Code_Security_Survey_2026-10-19.tex`, inspected at the 153-work / 224-contribution integration. Line references below concern this snapshot and may move during integration. No manuscript, active corpus, or audit CSV was changed. Only this report was created.

## Required corrections

### Major 1 — MHM paired execution was missed in the inherited coding

- Locations: TeX **1150** (MHM defense row), **1423–1425** (preservation totals), **1466/1470** (outcome totals). Active records IA-002 and DF-001 currently contain A / R.
- Strongest countercheck: [AAAI 2020 published PDF](https://ojs.aaai.org/index.php/AAAI/article/download/5469/5325), printed **p. 1174**, PDF page 6, results paragraph immediately before Table 4. The authors state that restored adversarial programs compile and execute, and report matching execution results on the test cases. This is an explicit reported paired check, beyond the earlier construction rules. Test input details and the per-variant denominator remain insufficiently specified.
- Correction: PP **A+T**, recorded compilation support, outcome **R+C+X**, with the scope “reported restored adversarial programs on supplied test cases; no exhaustive equivalence guarantee.” Regenerate the two affected aggregate rows from active data. Suggested defense table cells: `A+T & R+\\allowbreak C+\\allowbreak X & \\textsf{PRED}` (single LaTeX backslashes when inserted).
- Retraction: the previous A-only/no-paired-check interpretation in the inherited input audit must be withdrawn. The numerical MHM contrast in TeX1591 is itself correct.

### Major 2 — Extraction and membership remain conflated in the privacy synthesis

- Location: TeX **1097**, “Traces of Memorisation combines extraction and membership”.
- Countercheck: [Traces v1](https://arxiv.org/html/2312.11658v1), §§4.4–4.5 and Table 3: prefix-conditioned greedy suffix extraction, assessed by EM/BLEU-4. Membership inference supplies conceptual background; a membership classifier is not the reported experiment. The revised corpus correctly makes this result GEN.
- Suggested replacement for the opening portion: “Traces of Memorisation evaluates prefix-conditioned extraction. Gotcha, AdvPrompt-MIA and Buzzer assess training membership through different query and inference procedures …”. Apply the subsequent AUC/TPR/FPR sentence to the membership studies, and retain the extraction denominator separately.

### Major 3 — CodeGarrison's corrected table category is contradicted by its prose placement

- Locations: TeX **1167** correctly says input-perturbation classifier; **1283** still places its embedding classifier among detectors in “How Are Poisoning and Backdoors Detected or Removed?”.
- Countercheck: the retained [CodeGarrison v1](https://arxiv.org/html/2502.13459v1) protocol uses perturbed-code fixtures and detector classification. It does not establish detection/removal of an installed learned backdoor merely by classifying those fixtures. The source audit correctly moved DF-026 into input robustness.
- Correction: remove `ghannoum2025codegarrison` and “or embedding classifiers” from this backdoor-detector enumeration. Add an input-defense sentence: “CodeGarrison classifies adversarially perturbed code using learned embeddings.” Preserve its detector contribution and the existing PRED/R row.

### Minor 4 — Protocol coverage prose adds targeted checks into the protocol total

- Location: TeX **256**; generating script `ccfa-workfiles/manuscript/neural-code-security/source/evidence_revision.py:75`.
- Countercheck: Table audit-coverage protocol column sums to **169**, targeted to **14**, limited to **41**. The stated **183 records / 123 works** is the union of protocol and targeted checks. Protocol-only coverage is **169 records / 113 works**. The table itself agrees with the active corpus.
- Minimal replacement: “Protocol or targeted source checks reached 183 contribution records from 123 works; 41 records retain a partial, version-limited, or unavailable-source status.” Synchronize the generating script so regeneration retains the correction.

## Confirmed closures and counterchecks

- CodeIP: MIX, R+L, no X; prose explicitly identifies CodeBLEU and message recovery without executable task tests.
- SWEET: MIX; U for the complete robustness transformation set; F is retained for the conditional statistical detection bound, not preservation certification. Companion contract records the bounded scope.
- PromSec: T and X retained; TeX1448/1478 correctly restrict paired fuzzing to 20 specially constructed cases.
- Gu unlearning: R+L+X, synthetic biographies and retained pass@1 are explicit. No table-row/prose configuration mismatch was copied into the survey.
- Credential Revealer: both table and prose identify the two operational keys as public Stripe examples. Private-payment-credential disclosure is explicitly not inferred.
- RoPGen: table and prose correctly use data plus gradient augmentation.
- CodeGarrison: table/result-type correction is retained; only its backdoor-section placement remains unresolved as above.

## Same-study numerical checks: suspicions withdrawn

Directly rechecked the existing primary sources, without expanding the literature search:

1. [MHM Table 4](https://ojs.aaai.org/index.php/AAAI/article/download/5469/5325): clean accuracy and attack rates copied correctly; 2,000 examples and the 24.9/37.4 percentage-point reductions are correct. Training actually creates fresh models with identical hyperparameters; “same classifier” should be understood as the same architecture/evaluation setting.
2. [STRATA Appendix G/Table 9](https://arxiv.org/html/2009.13562): original .363/.243/.212 and robust .367/.342/.240 agree. The survey's uneven-transfer conclusion is supported and narrower than the original paper's categorical wording.
3. [DIP §4.5/Table 3](https://aclanthology.org/2023.acl-long.430.pdf): row/column orientation and all eight quoted ASRs agree; the combined-training interpretation is supported for the evaluated CodeBERT clone detector.
4. [Package mitigation §6/Tables 4–5](https://www.usenix.org/system/files/usenixsecurity25-spracklen.pdf): DeepSeek 16.14→2.66 and HumanEval51.4→25.3 agree; 13.48/26.1 percentage-point differences are correct. Utility is correctly distinguished from package-risk evaluation.
5. [SET v1 Table 10](https://arxiv.org/html/2512.19215v1): 5% poison P8.2 baseline89.09/62.06, P8.3 ASR7.15, P7.2 ASR88.95 agree. No cross-study ASR comparison or overgeneralized normalization claim was introduced.

## Counts, scope and source-version checks

- Abstract, corpus description, RQ2/RQ3 summaries and coverage-alignment table consistently use 153 works / 224 contributions, with 80 attacks,30 risks,110 defenses,4 resources. Surface counts49/24/7 and defense group counts39/29/4/38 match the active records. No remaining old global count was identified in the inspected manuscript.
- Preservation/outcome tables match the inspected active data before the MHM correction; those counts must be regenerated after that correction.
- Compared source URL/version fields for records covered by this model's four protocol audit slices against the active protocol fields: no integration substitutions or version-string mismatches found. Also checked explicit arXiv URL/version identifiers and date strings: no identified URL/version conflict or post-cutoff inspected source. This is a field-consistency check, not independent verification of every publication/version history.
- Source-limited formal-version comparisons remain labeled `version_partial` where inherited from the audited slices. No claim of a second human coder was introduced.
- Delivery export was still in progress during review; the earlier delivery README contains old counts, so the final export should replace it from the completed active state. This was not treated as a finished-package defect.

## Integrating-owner closure

The four identified issues were incorporated into the generating source and active data:

1. MHM IA-002/DF-001 now carry A+T and R+C+X, with the published p.1174 locator and bounded test coverage. Preservation/outcome totals were regenerated.
2. Traces is described as prefix-conditioned extraction; membership metrics refer to the membership studies.
3. CodeGarrison appears in the input-defense group and prose, and has been removed from the backdoor-detector enumeration.
4. The coverage sentence explicitly combines protocol and targeted checks; the table retains169/14/41 separately.

The same-study MHM wording now identifies common architectures retrained under the same evaluation, rather than implying identical weights. The four numerical contrasts and SET example retain the primary values checked by the reviewer. Active CSV/table comparison and the final LaTeX build passed after these changes. Source/version limitations remain recorded; no human agreement statistic is asserted.
