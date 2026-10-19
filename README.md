# Neural Code Security Survey

《Security and Robustness of Neural Code Systems: A Survey of Attack Surfaces, Defenses, and Evaluation》

当前稿件更新于 **2026-10-19**：148 篇主语料、219 项贡献，覆盖攻击、风险研究、防御和评估资源。文献截止日期为 2026-06-30。

## 当前稿件

- [论文 PDF：47 页，含五处中文作者待办](ACM_survey_codemodel/Neural_Code_Security_Survey_2026-10-19.pdf)
- [LaTeX 正文](ACM_survey_codemodel/Neural_Code_Security_Survey_2026-10-19.tex)
- [完整独立源码包](ACM_survey_codemodel/Survey_Draft_2026-10-19.zip)
- [贡献编码表](ACM_survey_codemodel/survey_coding_table_2026-10-19.csv)
- [编码规则及来源核验材料](ACM_survey_codemodel/supplement_2026-10-19/)
- [详细编译与文件说明](ACM_survey_codemodel/README_2026-10-19.txt)

正文分为九章、四个研究问题。带标注版本中的作者待办位于第 3、5、6、25、29 页，分别涉及工具与方法、人工复核、分类边界、程序保持与结果证据、数字对照。实际核验决定填写在 [author_review.csv](ACM_survey_codemodel/supplement_2026-10-19/author_review.csv)。

## 编译与复算

`ACM_survey_codemodel/main.tex` 是当前带日期正文的编译入口。在 Overleaf 中将它设为 Main document，或在本地运行：

```bash
cd ACM_survey_codemodel
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
python supplement_2026-10-19/reproduce.py
```

仓库附有中文待办卡片 PDF，正常编译使用 pdfLaTeX 即可。修改待办内容时编辑 `author-notes.py` 并运行该脚本（需要 ReportLab 和中文 TrueType 字体）。在正文导言区将 `\showauthornotestrue` 改为 `\showauthornotesfalse` 可隐藏标注，得到 46 页阅读稿。

根目录的 `survey.csv` 与当前贡献编码表保持一致。`ACM_survey_codemodel/1147/` 保存较早的稿件和数据。
