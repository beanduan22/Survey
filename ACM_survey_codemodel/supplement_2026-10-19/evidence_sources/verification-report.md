# 当前来源核实与筛除记录（2026-10-19）

## 本次筛除

根据作者明确要求，DaK、STRUCK、BADS、AdvBinSD、SLODA从主语料、正文、参考文献及统计中筛除。五篇对应七项贡献：五项攻击、两项防御。

当前语料为148篇、219项贡献：75项攻击、30项风险研究、110项防御、4项评估资源。

205项贡献具有命名版本的protocol check，14项具有targeted source check；当前主语料中没有partial、version_partial或source_unavailable记录。检查范围仍以每项实际读取的来源和定位为准；这不表示出版排版全文均已逐字比较，也不代表第二位人类独立编码。

## 筛除明细

| 论文 | 记录 | 原因 |
|---|---|---|
| DaK | IA-016, DF-082 | Full primary methods/results could not be inspected after targeted retrieval. |
| STRUCK | IA-023, DF-095 | Full primary methods/results could not be inspected after targeted retrieval. |
| BADS | TC-029 | Full primary methods/results could not be inspected after targeted retrieval. |
| AdvBinSD | TC-030 | Full primary methods/results could not be inspected after targeted retrieval. |
| SLODA | IA-037 | Complete formal protocol and correspondence of the available artifact to an in-cutoff version could not be verified. |

筛除发生在最终来源核实阶段，历史查询与审计不被改写为新的检索结果。source_exclusions.csv与excluded_records.csv保存决定；原始资料和筛除前版本仍留存。此前要求补全文的记录现为已筛除项，无需再补入本稿。

## 当前交付与验证

- protocol_audit.csv和author_review.csv仅含219项当前记录；人类确认栏继续留空。
- remaining_sources.csv仅保留表头，表示当前没有待补一次来源的主语料记录。
- 统计由当前CSV重算，并与带日期TeX中的表格逐项比较。
- 既有模型审查报告属于筛除前历史，单列在review_history；本轮筛除检查见final_validation.json。
- 编译、独立打包复算与源文件一致性结果以本轮final_validation.json为准。
