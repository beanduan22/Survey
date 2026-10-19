# Focused protocol closure — source findings, 2026-10-19

Independent GPT-6.1 model check, not a second human coder. Cutoff2026-06-30. Seven requested records are retained; statuses below distinguish checked publication protocol, a targeted official-artifact correction, and unresolved fulltext access. No active dataset or manuscript edit.

Retrieval chronology: initial standard-web ACM fulltext attempts failed. Follow-up covered author/institution PDF, official supplementary archives, complete artifact and publisher-indexed method/result passages. The final decisions below supersede preliminary partial findings.

## MOAA — two records closed for inspected protocol

Primary publisher body (https://doi.org/10.1145/3660808) was returned by targeted standard-web queries beyond the abstract: §§2–5, equations, methodology and result explanations. IA-027 stays MIX/R/A. DF-090 is PRED/R/A and covers **defect detection, clone detection and authorship attribution**, not authorship alone. §5.3 generates training AEs with four methods, augments the original training set and compares held-out testing accuracy (Fig9); §5.4 stratifies MOAA AEs by three objectives (Fig14). This establishes measured fine-tuning, without inventing unviewed figure values or equating ordinary test accuracy to adaptive robustness. The code-name construction supports A only. PDF/figure-panel access remains a documented source-format limitation, not an unresolved role/interface/oracle.

## SLODA — materially deeper artifact check; no false fulltext closure

Official author-linked repository: https://github.com/CGCL-codes/SLODA . Read complete `CodeBERT/attack/attack_ptm_sloda.py`, the `SLODA_Attacker` functions in `ptm_attacker.py`, `attack_utils.py::insert_at_line`, and real `features/one2zero.jsonl` entries. This establishes a PRED score-query result: a changed predicted label is success; originally incorrect inputs and inputs longer than512 tokens are skipped. The current entry additionally contains an `index>=2612` resume filter, so its local denominator must not be attributed to the whole publication.

**Substantive PP countercheck:** `ptm_attacker.py:70-90` prepends parameter declarations to stored snippets; `:209-274` passes selected snippets directly to insertion. `attack_utils.py:45-97` finds an AST location and renames intersecting identifiers but inserts the snippet without an unreachable-condition wrapper. Pool entry0 invokes HEXDUMP_PRINT with a newly declared pointer; other entries have output or memory effects. These functions do not establish whole-family behavioral preservation. This is a concern about the inspected artifact, not a claim that the unread final paper omitted every possible safeguard. Select the inspected official artifact for this coding decision: change whole-family A to U and record targeted_source_check. This corrects a substantive preservation overstatement; it does not claim full-paper or reproduction verification.

Artifact correspondence also remains unresolved: the attack entry imports `SLODA_Attacker` but instantiates `TAA_Attacker`; `ptm_attacker.py` defines two different `get_importance_score` signatures. No execution was attempted and no new bugs were repaired. These observations limit a reproduction claim; they do not invalidate the specific inspected PRED/R/U evidence or serve as scientific attack failures. Victim-model fine-tuning in README is not evidence of an evaluated defense. An abstract hint about robustness enhancement is not substituted for a defense experiment.

## DaK — source access remains the limiting factor

Primary DOI https://doi.org/10.1145/3591227 and official PLDI identity remain verified. New standard-web publisher full/PDF/download variants failed, as did the official auxiliary archive path `https://dl.acm.org/doi/suppl/10.1145/3591227/suppl_file/pldi23main-p56-p-archive.zip`. YuWang's author publication page provides only DOI; exact-title author/repository searches did not locate readable methods. Metadata API attempts were inaccessible.

A third-party classroom summary supplies leads about EverI, dead-code checks and theorem scope, but it is **not accepted as primary protocol evidence**. Therefore neither interface expansion, F, nor compiler outcome is confirmed. Both records retain protocol_partial, with concrete missing method/result requirements. This is a survey access gap; it has not been relabeled reported-but-unspecified.

## STRUCK — roles verified, method still unavailable

Official EUDL abstract: https://eudl.eu/doi/10.1007/978-3-031-54528-3_22 . It confirms structural attack and measured adversarial training. Springer chapter/PDF, EUDL PDF and GoogleBooks chapter attempts did not expose the method/results. The author publication list supplies no PDF; its two neighboring CollaborateCom page ranges are swapped, so publisher pagination392–413 is retained. No publicly readable official code was found. Both records remain protocol_partial. Exact transformation rules, retained property, test coverage, training construction and evaluation denominator remain unverified; no source absence claim is made.

## Current handoff

Seven assigned records retained; **two MOAA records protocol_checked, one SLODA record targeted_source_check, four DaK/STRUCK records protocol_partial** after expanded source attempts. No record was removed and no unknown was turned into a negative finding. A complete-paper `reported-but-unspecified` conclusion was not used for DaK, STRUCK or SLODA because the relevant complete primary method was not readable. Newly available user-supplied fulltexts can be checked directly against the explicit remaining questions.

Additional publisher-indexed exact-title searches with DaK Destroyer/EverI/evaluation and STRUCK global/local perturbation/method terms did not expose primary method passages; only the official abstracts and secondary summaries were returned. Standard and connector web routes both failed at the same publisher sources. These failed attempts are retained rather than represented as a successful fulltext check.

## SLODA artifact-selected closure update

The official single-commit repository resolves `commit/HEAD` to initial commit **6929ef5**: https://github.com/CGCL-codes/SLODA/commit/HEAD . Full SHA/date could not be obtained: patch request timed out, abbreviated patch failed, and API/atom/commits routes were inaccessible. The short commit is a precise available locator; its pre-cutoff timing is **not** asserted. Source fields retain this limitation.

Newly read helper: https://github.com/CGCL-codes/SLODA/blob/main/dataset/python_parser/run_parser.py . `mutation` selects several rewrite families. `add_if_line` supplies true-condition wrapping, supporting a local construction argument only when fresh names, scope and control flow are preserved; arbitrary declarations or control transfers cannot be included by default. The shift helper emits exponent syntax unsuitable as a universal C rewrite. Combined with direct side-effecting snippet insertion, this supports **whole-family U**, with only explicitly restricted neutral subcases assigned local A. Neither a compiler outcome nor paired execution is established in the inspected attack paths.

Current final scope: MOAA IA-027/DF-090 checked for the quoted publication methods and result types; SLODA IA-037 targeted PRED/R/U correction from primary artifact; DaK IA-016/DF-082 and STRUCK IA-023/DF-095 remain unresolved protocol access pending readable fulltext. No active corpus, manuscript or shared coding file edited.

## Independent opinion on selected author versions

An official conference or author-publication link can establish the identity of a selected full author version. Once that version's actual methods/results support each coded field, lack of a line-by-line VOR comparison is not itself a protocol gap. This applies conditionally to the parent-reported Ramakrishnan arXiv v1, OSeqL official poster-linked arXiv v2, and the complete 2022 CodePoisoner author version: retain their explicit selected-source identity and do not attribute their numbers to an uninspected later publication. This is a methodological opinion on the supplied linkage/evidence, not a new independent re-reading of those papers. Likewise, a complete ShadowCode v6 that defines a functional-equivalence criterion but omits its judging procedure supports a reporting omission; it does not authorize guessing L/S. A pinned Black artifact with read evaluation code and saved outcomes can establish L+X+E; a compilation gate alone does not establish C as an outcome.

## Two substantive coding boundaries — independent primary countercheck

**CodePoisoner TC-010:** https://arxiv.org/html/2210.17029v1 , §§4.1,4.3,6.3,6.5, Table3. The selected complete author version expressly allows functional changes and inserts LM-generated calls. Accordingly the contribution has no whole-program behavior-retention obligation: **PP --**, rather than failed/unsupported preservation U. A behavior-neutral rule subset does not impose that obligation on the full contribution. The reported validity measurement uses tree-sitter parsing, including the parser baseline; **C remains justified only because the survey defines C to include parsing**, not because this establishes compilation or execution. This distinction must remain explicit in prose.

**ShadowCode attack:** https://arxiv.org/html/2407.09164v6 , §§III-A,IV-A,IV-D TableV and AppendixA. Non-functional perturbations form the stealth premise, while evaluated variants include Output Content and Variable Assignment. Non-executing comments can supply local A, but no retained-observable-behavior restriction or check is supplied for the full union: **whole-family U** is justified. ASR/NBR/STF and the success criterion are reported, but the operational judging procedure is unspecified in the read settings/additional details: **R**, without inferring L/S/C/X from the wording of the criterion. This is a reporting limitation in a readable selected version, not failed source retrieval. No active data or manuscript changed.
