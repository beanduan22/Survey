"""Render the five author TODO cards included by the manuscript.

Requires reportlab only when changing the cards. The bundled PDF is sufficient
for normal pdflatex compilation. Supply --font with a Chinese TrueType font on
systems without the default Droid Sans Fallback font.
"""
from argparse import ArgumentParser
from html import escape
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


NOTES = [
    (
        "补充实际使用的工具与任务",
        "请写明检索、文献筛选、贡献编码和来源核查分别使用的 AI 工具/模型、"
        "版本或访问日期，以及输入材料、判断规则和输出如何采用。按实际日志补充；"
        "已有任务规则见本节和 codebook.md，工具记录见 protocol_audit.csv 的 "
        "protocol_reviewer 字段。请确认这些记录是否覆盖了全部实际使用。",
    ),
    (
        "补充真实的人工复核过程",
        "请核实前文“第一作者两轮编码”是否符合实际，并补充：谁复核、核对哪些记录或字段、"
        "全量还是抽样及其数量/分母、依据哪些原文、如何处理分歧。对已完成的核验，"
        "在 author_review.csv 填写 author_decision、author_correction、author_initials "
        "和 review_date。未完成的记录继续留空；完成后据实更新本段的待确认状态。",
    ),
    (
        "核验分类边界与统计口径",
        "请对照主 CSV 的来源定位确认：PELICAN、CodeJailbreaker 属当前输入攻击；"
        "FDI 的训练更新与检索路径分为两项攻击；隐私诊断归风险研究。核对攻击分组 "
        "46/22/7 与 148 篇、219 项贡献的统计口径，确认多角色记录不是重复计数，"
        "并将实际核验决定填回 author_review.csv。",
    ),
    (
        "核验保持条件与结果证据",
        "请优先核对原文版本、定位和测试范围：Quiring/MHM 的 A+T、PELICAN 的局部 A+F、"
        "PromSec 的 20 个特制案例；再确认 FDI 的 R、SkillJect 的 R+X 和 TIP 的 R+X+E。"
        "逐项区分原始/变换程序的配对检查、良性功能测试、恶意载荷测试及智能体执行，"
        "确认表中代码与正文解释一致，并记录决定。",
    ),
    (
        "核验数字对照及结论方向",
        "请逐项对照原文和 within_study_comparisons.csv：MHM 的 2,000 条训练样本及 "
        "ASR/准确率；STRATA 的 0–1 F1；DIP 的训练集顺序和攻击行列；包幻觉的推荐次数分母"
        "及 HumanEval 变化。另核对 SET 的 5% 投毒与 P8.2/P8.3/P7.2 对照，"
        "确认百分点差值及安全/功能权衡的解释，并记录核验结果。",
    ),
]


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "--font",
        default="/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf",
    )
    args = parser.parse_args()
    pdfmetrics.registerFont(TTFont("AuthorNoteCJK", args.font))
    style = ParagraphStyle(
        "AuthorNote", fontName="Helvetica", fontSize=10.5, leading=15,
        wordWrap="CJK", textColor=colors.HexColor("#442900"),
    )
    heading_style = ParagraphStyle(
        "AuthorNoteHeading", parent=style, fontSize=11.5, leading=16,
        textColor=colors.HexColor("#8A4600"),
    )
    def mixed_text(text):
        return re.sub(
            r"[\u2e80-\u9fff\uf900-\ufaff\uff00-\uffef]+",
            lambda m: '<font name="AuthorNoteCJK">' + m[0] + '</font>',
            escape(text),
        )
    output = Path(__file__).with_suffix(".pdf")
    pdf = canvas.Canvas(str(output), pagesize=(420, 120))
    pdf.setTitle("Author TODO cards for the Neural Code Security Survey")
    for i, (title, body) in enumerate(NOTES, 1):
        paragraph = Paragraph(mixed_text(body), style)
        _, height = paragraph.wrap(396, 1000)
        heading = Paragraph(mixed_text(f"AUTHOR TODO {i:02d} / 作者待办：{title}"), heading_style)
        _, heading_height = heading.wrap(396, 1000)
        page_height = height + heading_height + 32
        pdf.setPageSize((420, page_height))
        pdf.setFillColor(colors.HexColor("#FFF4D9"))
        pdf.setStrokeColor(colors.HexColor("#B56800"))
        pdf.setLineWidth(1)
        pdf.roundRect(1, 1, 418, page_height - 2, 4, fill=1, stroke=1)
        heading.drawOn(pdf, 12, page_height - 12 - heading_height)
        paragraph.drawOn(pdf, 12, 12)
        pdf.showPage()
    pdf.save()
    print(f"Rendered {len(NOTES)} author TODO cards: {output.name}")


if __name__ == "__main__":
    main()
