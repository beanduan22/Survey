> Historical review before the five-work filter. Current corpus and validation are recorded in verification_report.md and final_validation.json.

# Closure integration review — 2026-10-19

Independent GPT-6.1 model check, not a second human coder. Bounded integration check of the dated TeX, exported contribution CSV and supplement verification report; no renewed search for the four blocked works. Only this review file was edited.

## 1. Major — MOAA defense still has an unsupported adaptive-evaluation flag

**Location:** `repo:manuscript/survey_coding_table_2026-10-19.csv:191`, DF-090, `adaptive_evaluation=yes`.

The same row's `coding_note` and `protocol_decision` expressly decline to infer adaptive post-defense ASR. The inspected publication §5.3/Fig9 generates training adversarial examples, augments training, fine-tunes classifiers and reports ordinary held-out test accuracy across defect, clone and authorship tasks. That establishes a defense experiment but does not establish an attacker reoptimizing against the defended model. The inherited `yes` exceeds the retained evidence.

**Minimal repair:** set this DEF record's field to `NR`/`not_checked` (using the project's vocabulary) unless a separate primary locator establishes adaptive evaluation. Do not silently replace it with a claim that the authors did not perform such an experiment. The three-task/PRED/R/A description at TeX1193 is already consistent and needs no change.

## 2. Major — the main-text cutoff statement has an undisclosed artifact exception

**Location:** `repo:manuscript/Neural_Code_Security_Survey_2026-10-19.tex:235` (unqualified “Evidence coding uses a version available by 30 June 2026”); related source-policy paragraph at259.

**Countercheck:** the SLODA row at exported CSV38 correctly retains short commit6929ef5, unknown commit date and unread final experiment scope. Supplement `verification_report.md:8,32` also retains these limitations. Thus the data/report are honest, but the unqualified main-text sentence implies the SLODA evidence version has been demonstrated pre-cutoff. The work's eligibility before the cutoff and the artifact snapshot's unknown timing are different facts.

**Minimal repair:** make the general policy an aim with an explicit named exception. Suggested replacement for the first evidence-policy sentence: “Evidence coding targets versions available by 30 June 2026. SLODA is an eligible pre-cutoff work, but its targeted artifact correction uses commit6929ef5, whose date and correspondence to the pre-cutoff experiment remain unverified.” Retain the existing sentence excluding known post-cutoff additions. This does not require dropping the work or altering the verified205/targeted15/limited6 counts.

## 3. Minor — exported historical Black notes still read as current unresolved coding

**Location:** `repo:manuscript/survey_coding_table_2026-10-19.csv:223` and224, SU-027/SU-028, `role_audit_note`.

The current rows have `outcome_evidence=L+X+E`, a dated primary artifact and `protocol_checked`; their retained role-audit note still says the exact oracle is “unresolved and explicitly NR”. This is the earlier extraction state, not the current finding. The pinned source `tests.py::cwe434/cwe22` supports the reported SECURE=False logic, and the dated TeX1098/1719 correctly presents the bounded execution evidence and test limitation; these conclusions need not be weakened.

**Minimal repair:** preserve the earlier note but prefix it with “Historical role-audit note; superseded by the dated artifact protocol check below:”. Alternatively move it to a clearly dated history field. Do not erase the historical decision or leave it indistinguishable from the active oracle.

## Closure recheck — all three findings closed

Re-read only the three requested integration repairs after regeneration; no new retrieval or expanded scientific review.

1. **PASS / closed:** exported `survey_coding_table_2026-10-19.csv:191`, DF-090, now has `adaptive_evaluation=NR`, consistent with the bounded fine-tuning/test-accuracy evidence.
2. **PASS / closed:** dated TeX235 explicitly identifies the SLODA author-code correction as an exception with unverified commit date, retains the companion source limitation, and does not attribute new pre-cutoff performance results to it.
3. **PASS / closed:** exported CSV223/224, SU-027/SU-028, now labels the old role-screening note Historical and superseded by the pinned-artifact protocol fields. The old decision is retained without presenting it as the current oracle.

No confirmed finding from this bounded integration review remains open. The separately documented source/protocol limitations are not declared resolved by these three editorial/data-integration repairs. Additional bibliography metadata changes were outside this recheck.
