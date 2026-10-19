# Final version verification — training/runtime and remaining defenses

Date: 2026-10-19. Evidence cutoff: **2026-06-30**. Reviewer: independent GPT-6.1 model check, **not a second human coder**.

## Coverage and status meaning

The accompanying CSV covers the assigned **15 works / 18 existing contribution records**, including Gotcha DF-091 and BaxBench DF-093. It changes no active dataset or manuscript. Seventeen rows are `protocol_checked`; OSeqL DF-023 retains `version_partial`.

`protocol_checked` closes the method/evaluation gap for the **explicitly named inspected fulltext**. It does not assert that an accepted/latest author manuscript is byte-identical to the publisher version. `version_verification_scope` distinguishes published fulltext, author-hosted proceedings PDF, accepted author version, and latest author manuscript. Publisher access limitations remain recorded separately. Classification was checked against methods, metrics and result settings, not title identity.

## Comparison ledger

| Work | Inspected source and comparison decision |
|---|---|
| RMCBench | [Latest v1](https://arxiv.org/html/2409.15154v1), with ASE proceedings frontmatter; §§3–4.3 and evaluation table rechecked. No later arXiv version. Response judgments remain R+L, without executed malware validation. Publisher PDF/fulltext failed. |
| Traces | [Latest v2, 2024-01-15](https://arxiv.org/html/2312.11658v2); extraction game, sample selection, greedy evaluation and categories compared to prior v1 extraction. Table3 retained. Nearby prose contains a contradictory percentage; use the named table. |
| Gotcha | [Camera-ready v2, 2024-10-15](https://arxiv.org/html/2310.01166v2); classifier and known-training setting retained. Defense v1 Table4 becomes TableVII, with the same sampling rows. Both records checked. |
| Credential Revealer | [Accepted v2, 2024-05-20](https://arxiv.org/html/2309.07639v2) expands tools and adds actual blocking intervention. Update provenance; do not label the whole experiment unchanged. New defense recommendation below. |
| License | [Institution-hosted published FORGE PDF](https://repository.tudelft.nl/file/File_68b1c265-aa1e-4cd8-b7fc-a51a5361b464), confirmed as final by [repository metadata](https://repository.tudelft.nl/record/uuid:9573bc63-4fe3-4125-adc4-c86ab424c631). §§4–5 retain exact-file hashes and comment searches. |
| OSeqL | [Full latest v2](https://arxiv.org/html/2312.04004v2), [official CAIN final-title page](https://conf.researchr.org/details/cain-2025/cain-2025-call-for-posters/3/Finding-Trojan-Triggers-in-Code-LLMs-An-Occlusion-based-Human-in-the-loop-Approach), and [author poster](https://aftabhussain.github.io/documents/pubs/cain25-oseql-poster.pdf). Official page explicitly links the preprint; final two-page protocol tables remain unavailable. |
| SafeCoder | [Latest v2, 2024-07-12](https://arxiv.org/html/2402.09497v2), linked as Paper by the [ETH SRI ICML publication page](https://www.sri.inf.ethz.ch/publications/jhe2024safecoder). Same previously inspected version; rechecked training/data and Table1. Separate CodeQL security and benchmark utility outcomes. |
| PromSec | [Latest v1](https://arxiv.org/html/2409.12699v1), with CCS proceedings frontmatter; method and §5.2/Table4 reread. PP-T is limited to the specially designed paired-fuzzing subset, not the entire main benchmark. |
| DetectCodeGPT | [Accepted v5, 2024-07-30](https://arxiv.org/html/2401.06461v5); perturbation and provenance score retained, evaluation expanded. §VI-A still argues correctness in most cases; no paired behavior test establishes T. |
| GPTSniffer | [Published JSS PDF](https://riccardorubei.github.io/files/J_2024_2.pdf), online 2024-04-16; same classifier/split logic, plus §4.2.3 and §5.2.2 prompt-engineered tests. AI-only disguised sets must not be interpreted as balanced accuracy evaluation. |
| Rewrite detector | [Published AAAI PDF](https://ojs.aaai.org/index.php/AAAI/article/view/32082/34237); rewriting/similarity protocol and original m4 main-table means unchanged. Table3 becomes Table1. Correct/incorrect source-code grouping is not paired preservation of rewrites. |
| Scrub It Out | [Author-hosted ICSE proceedings PDF](https://zhaoyang-chu.github.io/assets/CodeEraser.pdf), final DOI/ISBN frontmatter. Compared method, settings and Tables3–4 to prior v1; cited main rows retained. HumanEval is utility evidence. |
| Gu unlearning | [Accepted v2, 2026-01-28](https://arxiv.org/html/2502.05739v2); expands to eight model configurations. Dataset/measurement contract and original CodeLlama7B rows retained. Attribute leakage is explicitly expert-judged; pass@1 is executed utility. |
| BaxBench | [Latest v3, 2025-05-30](https://arxiv.org/html/2502.11844v3), checked against [official PMLR metadata/abstract](https://proceedings.mlr.press/v267/vero25a.html). Three roles, HTTP functional tests and end-to-end exploits retained; headline and agent subset changed as detailed in CSV. |
| Practical hallucinations | [ISSTA-accepted v2, 2025-01-17](https://arxiv.org/html/2409.20550v2); manual taxonomy/security example retained. §V reports general RAG functionality, without a separately measured security-defense endpoint. Do not convert the broad nonfunctional rate into a vulnerability rate. |

## Required integration recommendations

1. **Credential Revealer: add a defense contribution**, without inventing a record ID here. §5.4/Table6 evaluates mandatory public-code blocking: Copilot plausible outputs decrease 2702→1396, reported rate .33→.29 and strong-match rate .04→.02; CodeWhisperer remains 129→130. Recommended role DEF, interface GEN, outcome L, PP inapplicable; no functionality-retention test is reported. Maintain the existing risk record and public Stripe-test-key qualification. The new source covers six NCCTs rather than the earlier two.
2. **BaxBench: update v1 headline 60% to v3 62% where that headline is used.** Preserve the all-task versus 351-task agent-subset distinction and conditional-security denominators; Table2 is an agent comparison on a reduced setting, not an improvement measured on all 392 tasks. Existing records remain sufficient for the three roles under the survey's artifact-result interface rule.
3. **Gu: record v2's expanded model coverage.** Original 7B values can stay when correctly labeled, but the earlier three-model description must not be carried as the latest study scope.
4. **GPTSniffer: record the formal extension and final table numbering.** Preserve the separation of cross-source, task-paired and disguised AI-only tests.
5. **OSeqL: retain the precise remaining gap.** The CAIN title, author list and official preprint linkage are verified; the final two-page detailed methods/results have not been read. No new preservation obligation follows from deliberately diagnostic line occlusion.

## Access attempts and residual limitations

Publisher ACM PDF/fulltext attempts for RMCBench (10.1145/3691620.3695480), Credential Revealer (10.1145/3660818), PromSec (10.1145/3658644.3690298), and License (10.1145/3650105.3652298) failed. License was resolved through TU Delft's final PDF. The other works use the named latest/accepted full author manuscript.

SafeCoder PMLR PDF and its raw GitHub mirror failed (the latter returned unsupported octet-stream); ETH research-collection bitstream also returned403. The ETH laboratory page endorses the inspected arXiv version as its Paper. BaxBench's official PMLR raw PDF failed; official bibliographic/abstract content and full latest arXiv were read instead. These are **publisher-text access limitations, not absent author-protocol evidence**.

For OSeqL, the official CAIN program explicitly points to arXiv2312.04004; the author publication page supplies only its poster. A guessed author final-paper path was inaccessible and poster screenshot extraction failed. Full preprint tables were read; neither poster/abstract agreement nor the final-title match is treated as proof that the final two-page tables are unchanged.

## Counterchecks withdrawn

- Rewrite detector's formal main-table m4 means do **not** change: a different ablation setting is not evidence of a main-table revision.
- CodeEraser's Qwen Table4 retention is **99.99**, matching results prose; no correction to99.00 is justified by this check.
- Dynamic utility tests in Gu/CodeEraser/BaxBench do not create source-program PP-T evidence.
- Practical hallucinations' RAG pass@1 is not a security-specific defense result, so no extra security DEF record is recommended solely from that table.
