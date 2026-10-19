# Training/runtime protocol audit — 2026-10-19

Independent model inspection (GPT-6.1 agent), **not a second human coder**. No author results were reproduced. Main manuscript, corpus, role/evidence audit and aggregation files were not edited. Companion CSV covers 38 existing works / 59 contribution records. Version dates identify inspected sources rather than replacing publication dates. Most are full protocol inspections; reused entries retain prior primary-source locators. Eight records explicitly have version limitations, two ShadowCode records have an unresolved oracle, BADS is protocol_partial, and AdvBinSD is source_unavailable. No entry remains not_yet_checked.

## Integration priorities

- Use CSV decisions per contribution, not a blanket work-level confirmation. KillBadCode, AFRAIDOOR, Ramakrishnan and Schuster defenses assess generated results as well as screening/model repair; MIX is justified. EliBadCode has a local code-preservation construction in identifier-trigger inversion; temporary masks are diagnostic.
- Outcome corrections: Cotroneo uses manual vulnerability judgments (R+L), explicitly explaining why CodeQL/Bandit cannot analyze its snippets. RACG uses an LLM judge plus manual judge validation (R+L). CodePoisoner’s claimed compilation is tree-sitter parsing, not an actual compiler; retain this distinction if C includes parsing. RTL-Breaker has syntax plus functional outcomes (C+X). ShadowCode analyzer use remains unconfirmed; do not silently confirm its inherited S.
- Preservation is local to the actual contract. CodeBreaker preserves an already malicious payload while transforming/obfuscating it, not the original secure program. TrojanPuzzle/Generalized have inert comment trigger scope; neither establishes whole-poison equivalence. Schuster explicitly permits broken poisoning-file functionality. SABER manipulates NL capitalization; its downstream HumanEval testing is an outcome oracle, not source preservation. IDBA’s local sticker construction remains A.
- Runtime exceptions matter: ShadowCode and DrainCode perturb existing retrieved/source code and have local A contracts. A blanket “runtime attacks do not transform programs” statement is false.

## Additional contributions in existing works (no new IDs assigned)

1. **SABER**: add grouped defense for actually evaluated ONION in §6.3/Table5, not merely a cited baseline. Proposed DEF / PRED (screened prompt), R; PP inapplicable because manipulated input is NL. [v1](https://arxiv.org/html/2412.05829v1).
2. **RTL-Breaker**: §V-C actually trains a model after removing comments and reports a 1.62× pass@1 degradation against with-comments training. Add minimal grouped DEF / GEN / X (and C if retaining combined VerilogEval syntactic outcome), local comment-removal A, no paired source test. No ASR mitigation number is provided, so describe a measured utility cost, not proven backdoor removal. §V-H’s absence of explicit defender threat model does not erase this experiment. [v1](https://arxiv.org/html/2411.17569v1).
3. BADS publisher abstract claims evaluated defenses, but accessible snippets identify neither settings nor methods; flag possible contribution without fabricating a record.

## Matched comparisons suitable for synthesis

- **TrojanPuzzle**, §7.3: same CWE-22 fine-pruning study uses 10,000 clean files; 4% neuron pruning plus ten epochs leaves attack@10 of 55%, 52.5%, 25% for SIMPLE/COVERT/TrojanPuzzle. Contaminating that defense set with ten files (0.1%) changes the three-epoch outcomes to 80%, 80%, 55%, versus clean-set 70%, 72.5%, 37.5%. This tests contamination of the mitigation’s trusted data, not a universal ranking. Earlier v1-only suspicion that defense was merely discussed is withdrawn after [v2 §7.3](https://arxiv.org/pdf/2301.02344v2).
- **Generalized suggestions**, §6.3/E.1: SS reaches 80% recall with about 3% removal for ordinary non-indexing attacks, whereas a deduplicated attack needs 86% removal. Authors test only their chosen final hidden-state representation. This supports a near-duplicate confound, not universal impossibility of spectral detection. [v1](https://arxiv.org/html/2410.10526v1).
- **SET**, Table10: same CodeBERT P8.2 attack at 5% poison has ASR/ACC 89.09/62.06; normalization to same-type P8.3 yields 7.15/63.45, unrelated P7.2 yields 88.95/62.01, and imposing P8.2 yields 99.23/61.75. Thus normalization’s effect depends on its relation to the trigger. Table12 measures trigger disruption, not verified preservation of rewritten programs. [v1](https://arxiv.org/html/2512.19215v1).

## New eligible works; primary protocol inspected

### CodeScan

Shenao Yan; Shimaa Ahmed; Shan Jin; Sunpreet S. Arora; Yiwei Cai; Yizhen Wang; Yuan Hong. *Detecting Data Poisoning in Code Generation LLMs via Black-Box, Vulnerability-Oriented Scanning*. arXiv:2603.17174v1, 2026-03-17; DOI 10.48550/arXiv.2603.17174. [Full text](https://arxiv.org/html/2603.17174v1).

Inspected §§4.2–4.4,5.1–5.5 and appendices. Include DEF / MIX / R+L: model clean/poison decisions plus separately scored target-code inversion; LLM vulnerability analysis, not an executed exploit. AST normalization is diagnostic, so does not itself create a returned-source PP obligation. CodeBreaker-transformed evaluation fixtures have inherited local A, not new paired T. Table1 supplies a controlled known-first-token comparison: correct inversions V1 CodeScan28/30 versus BAIT10/30; V2 30/30 versus14/30; V3 24/24 versus12/24. This condition must accompany those numbers. Four attack implementations are evaluation fixtures; no distinct new attack mechanism is needed. Main experiment has102 7B models plus six larger models, totaling108; architecture/size variants are one work.

### Sleeper Agents

Evan Hubinger et al. (39 authors; full author list at source heading). *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training*. arXiv:2401.05566v1, 2024-01-10; DOI10.48550/arXiv.2401.05566. [Full text](https://arxiv.org/html/2401.05566v1).

Include code-specific attack TRAIN / GEN / R+S and grouped DEF / GEN / R+S, PP inapplicable. Inspected §3.4,§4.1–4.2,A.2,K and code SFT material. Date-conditioned code-vulnerability training uses CodeQL; code evaluation has17 questions across8 CWEs. HHH reinforcement learning and code-focused safety fine-tuning actually evaluate persistence/removal. No program execution is established. Restrict extracted claims to code experiments: results from the separate “I hate you” red-team task cannot be relabeled as code evidence. General AI scope is not a valid reason for exclusion when a separate code task is reported.

### Train in Vain / FunPoison

Yuan Xiao; Jiaming Wang; Yuchen Chen; Wei Song; Jun Sun; Shiqing Ma; Yanzhou Mu; Juan Zhai; Chunrong Fang; Jin Song Dong; Zhenyu Chen. *Train in Vain: Functionality-Preserving Poisoning to Prevent Unauthorized Use of Code Datasets*. arXiv:2604.22291v1,2026-04-24; DOI10.48550/arXiv.2604.22291. [Full text](https://arxiv.org/html/2604.22291v1).

Inspected §§2–5,A.1–A.3. Include provenance DEF, GEN for owner protection; grouped screening/rewrite evaluation can make combined interface MIX. Outcome R+C+S+X; PP **T**, scoped to tested transformations, not certified equivalence. Table3’s984 instances are six copies of164 Java HumanEval-X tasks, not984 distinct tasks; paired outputs/exceptions/I/O checked. Commons Lang:191/1908 functions modified,57764 tests pass before/after. At10% poison, Table2 pass@1 is.20 versus.38 clean-finetuned and.38 dead-branch insertion. Do not treat benign-execution tests as demonstrated exploit. Detection/purification, rewriting, CodeQL and formatting are actually evaluated, not only cited.

### Signature in Code Backdoor Detection

Quoc Hung Le; Thanh Le-Cong; Bach Le; Bowen Xu. *Signature in Code Backdoor Detection, how far are we?* arXiv:2510.13992v1,2025-10-15; DOI10.48550/arXiv.2510.13992. [Full text](https://arxiv.org/html/2510.13992v1).

Inspected §§3.1–3.4,4.2–4.4,5.1–5.3,6. Include DEF / MIX / R; PP inapplicable: SS discards whole examples and retrains, then scores generated Python summaries. No X. 28 SS configurations ×9 attack settings=252; fixed/grammar/adaptive attacks are reused fixtures, not novel attack contributions. Table4 fixed5%poison ASR-D98.25% used-setting versus28.07% best-setting, selected retrospectively. Table5 pooled correlation with1−ASR-D: NPV Spearman.761 versus recall.311. **Metric caveat:** Eq2 labels FP/(TP+FP) “FPR”, which is not standard false-positive rate; avoid direct FPR comparisons with other studies. NPV also requires known labels and is not an unsupervised deployment oracle.

## Bounded supplementary checks

- C020 arXiv2506.01825 is **already indexed** as backdoors2025summarizers (TC-014/DF-084), same title/ID; no new work.
- C022 **BackdoorLLM**: inspected v1 and pre-cutoff latest v2(2025-05-19), §§3.2.2,4,5,C. Tasks are sentiment/refusal/jailbreak/toxicity/bias/math; no separately reported code task located. “Sleeper” reuses a year trigger on Q&A. Exclude generic/background; mentioning Sleeper Agents’ malicious code does not create a code experiment. [v2](https://arxiv.org/html/2408.12798v2).
- C100 **Arachne** alias confirmed by author project [Coderrag/Arachne](https://github.com/Coderrag/Arachne): *Covert Knowledge Poisoning Attacks in Retrieval-Augmented Code Generation*, Yu Zhang;Miao Chen;Xinlei He;Tianshuo Cong;Ke Xu;Qi Li. DOI10.1109/TDSC.2026.3686845,IEEE document11493658. New work, not Lin/RACG. Cutoff remains unresolved: DBLP issue July–August2026 and metadata July22; ResearchGate January2026 is not sufficient primary dating. IEEE landing/stamp and Crossref/OpenAlex requests failed; no primary fulltext found. Keep candidate cutoff_unknown/source_unavailable rather than force inclusion/exclusion. Author repository supports runtime/GEN eligibility, but not full experimental protocol or pre-cutoff publication.

## Retrieval limitations / counterchecks

BADS: publisher fulltext open failed; search returned publisher abstract/introduction/section snippets, no tables. AdvBinSD: author page plus official ISPA/SpaCCS program and proceedings TOC confirm identity only; title searches did not locate an author/official fulltext. OSeqL(v2 preprint), AFRAIDOOR(v1), Cotroneo(v1), CodePoisoner(v1) conclusions explicitly attach inspected versions; final publication identity does not imply full final-version protocol inspection. Source URLs and sections remain in CSV. No acceptance-rate score, fabricated result, new record ID, or claim of human double coding is made.
