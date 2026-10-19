> Historical review before the five-work filter. Current corpus and validation are recorded in verification_report.md and final_validation.json.

# Verification integration review — 2026-10-19

Independent GPT-6.1 model check; not a second human coder. Bounded integration check only, using the existing inspected-source evidence, active corpus, verification tables, `apply_evidence.py` and the dated neural-code-security TeX. No new retrieval and no active-file edits.

## Concrete issue

### Minor — BaxBench exclusion is one framework and one scenario

Location: `repo:manuscript/Neural_Code_Security_Survey_2026-10-19.tex:1097`.

Current wording: “uses 351 tasks, excluding two frameworks”.

The already inspected BaxBench v3 §4/Table2 excludes the Python-Django environment and Compiler scenario. Compiler is not a second framework. The denominator351 is correct:392−28−14+1=351.

Replace with: **“uses 351 tasks, excluding the Python-Django framework and the Compiler scenario”**. The following restriction to comparisons within that subset is accurate and should stay.

## Confirmed integration checks

- Active totals match:153 works/226 contributions;80 attacks,30 risks,112 defenses,4 resources. Status counts are193 protocol checks,14 targeted checks and19 limited records. The207 checked contributions span141 works; the TeX role coverage table matches.
- DF-094 retains its own DEF/generation/L/PP-inapplicable codes after copying OE-025. It points specifically to §5.4/Table6 of the named FSE author v2 and retains the publisher-text limitation. Its lexical exposure evidence is not overwritten with the risk record’s R+L+X.
- All11 copied child-defense patches retain their intended role, interface and outcome codes after parent verification. This includes DF-091, DF-093, DF-094 and DF-095. The patch is reapplied after the parent audit in `apply_evidence.py`.
- DF-095 remains `protocol_partial`, sourced to the official abstract; full methods, training split, metrics and preservation validation remain unresolved. Its retained A is explicitly provisional in the record and is not represented as a completed protocol check.
- Both Black records retain L+X+E, `version_partial`, `author_artifact_current_state`, the October2026 access date and the missing cutoff snapshot/journal comparison. A compilation gate has not been promoted to outcome C. The TeX retains the publication/artifact correspondence limitation.
- Every nonempty source URL/version/scope/comparison/gap field in both verification tables is preserved in the corresponding active record; no mismatch was found.
- BaxBench’s active evidence uses62%, with351-task subset values labeled separately. No old60% headline remains in the dated TeX. The sole issue above is the naming of the excluded dimension.

No other required correction was identified within this bounded check.

## Integrating-owner closure

The minor finding was corrected in the generating source and regenerated TeX: the351-task subset excludes the Python-Django framework and the Compiler scenario. Active corpus/table checks passed after this correction.
