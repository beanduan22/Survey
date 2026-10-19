"""Recompute counts and verify manuscript table views from the released CSV.
Run from any directory: python supplement_2026-10-19/reproduce.py
"""
import csv
import json
import re
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / 'Neural_Code_Security_Survey_2026-10-19.tex'
def summarize(rows):
    attacks = [row for row in rows if row["role"] == "attack"]
    groups = {
        "inference_input_attacks": [row for row in attacks if row["lifecycle_surface"] == "inference input"],
        "training_attacks": [row for row in attacks if row["lifecycle_surface"] == "training"],
        "runtime_context_attacks": [row for row in attacks if row["lifecycle_surface"] == "runtime context"],
        "output_ecosystem_risks": [row for row in rows if row["role"] == "risk study"],
        "defenses": [row for row in rows if row["role"] == "defense"],
    }
    return {
        "works": len({row["work_id"] for row in rows}),
        "contributions": len(rows),
        "protocol_audit_by_record": dict(Counter(r['protocol_audit_status'] for r in rows)),
        "protocol_checked_works": len({r['work_id'] for r in rows if r['protocol_audit_status'] in {'protocol_checked','targeted_source_check'}}),
        "roles": dict(sorted(Counter(row["role"] for row in rows).items())),
        "attack_surfaces": dict(sorted(Counter(row["lifecycle_surface"] for row in attacks).items())),
        "inference_tables": dict(sorted(Counter(row["inference_table"] for row in attacks
                                               if row["lifecycle_surface"] == "inference input").items())),
        "preservation_by_role": {
            role: {
                "applicable": sum(row["preservation_support"] != "--" for row in rows if row["role"] == role),
                **dict(sorted(Counter(
                    code for row in rows if row["role"] == role
                    for code in row["preservation_support"].split("+")
                ).items())),
            } for role in ("attack", "risk study", "defense", "evaluation resource")
        },
        "source_checked_works": len({row["work_id"] for row in rows
                                     if row["protocol_audit_status"] in {"protocol_checked", "targeted_source_check"}}),
        "role_audit_by_work": dict(Counter({row["work_id"]: row["role_audit_status"]
                                          for row in rows}.values())),
        "defense_groups": dict(Counter(row["defense_group"] for row in rows if row["role"] == "defense")),
        "outcome_evidence_by_group": {
            name: {"records": len(group), **dict(sorted(Counter(
                code for row in group for code in row["outcome_evidence"].split("+") if code
            ).items()))} for name, group in groups.items()
        },
    }

def check_manuscript(rows):
    """Check the manuscript views against the active contribution records."""
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    attacks = [row for row in rows if row["role"] == "attack"]
    tables = {
        "tab:evasion-program": [r for r in attacks if r["inference_table"] == "program/binary/feature"],
        "tab:evasion-prompt": [r for r in attacks if r["inference_table"] == "prompt/comment"],
        "tab:evasion-benchmarks": [r for r in attacks if r["inference_table"] == "benchmark"],
        "tab:poison": [r for r in attacks if r["lifecycle_surface"] == "training"],
        "tab:runtime": [r for r in attacks if r["lifecycle_surface"] == "runtime context"],
        "tab:gensec": [r for r in rows if r["role"] == "risk study"],
        "tab:defenses": [r for r in rows if r["role"] == "defense"],
    }
    interfaces = {"prediction": "PRED", "generation": "GEN", "mixed": "MIX",
                  "agent": "AGT", "observational": "OBS", "observation": "OBS",
                  "discriminative": "PRED", "generative": "GEN"}
    for label, group in tables.items():
        start = manuscript.index("\\label{" + label + "}")
        end = manuscript.index("\\end{longtable}", start)
        section = manuscript[start:end]
        keys = re.findall(r"\\cite\{([^}]+)\}", section)
        assert Counter(keys) == Counter(r["citation_key"] for r in group), label
        if label.startswith("tab:evasion-"):
            continue
        by_key = {r["citation_key"]: r for r in group}
        for line in section.splitlines():
            citation = re.search(r"\\cite\{([^}]+)\}", line)
            if not citation:
                continue
            record = by_key[citation[1]]
            cells = re.split(r"(?<!\\)&", line)
            codes = re.sub(r"\\allowbreak|\s", "", cells[-2])
            assert codes == record["outcome_evidence"], (label, citation[1], "outcome")
            result = re.search(r"\\textsf\{([^}]+)\}", cells[-1])[1]
            assert result == interfaces[record["model_interface"]], (label, citation[1], "interface")
            if label in {"tab:poison", "tab:defenses"}:
                assert cells[-3].strip() == record["preservation_support"], (label, citation[1], "preservation")

    summary = summarize(rows)
    labels = {
        "inference_input_attacks": "Inference-input attacks",
        "training_attacks": "Training compromise",
        "runtime_context_attacks": "Runtime-context attacks",
        "output_ecosystem_risks": "Output/ecosystem risk", "defenses": "Defenses",
    }
    for group, counts in summary["outcome_evidence_by_group"].items():
        expected = [counts["records"]] + [counts.get(code, 0) for code in "RLCSXEF"]
        matches = re.findall(r"(?m)^" + re.escape(labels[group]) + r" & ([\d &]+)\\\\", manuscript)
        assert any([int(x.strip()) for x in match.split("&")] == expected
                   for match in matches), group
    preservation_labels = {"attack": "Attacks", "risk study": "Risk studies",
                           "defense": "Defenses", "evaluation resource": "Evaluation resources"}
    for role, label in preservation_labels.items():
        counts = summary["preservation_by_role"][role]
        expected = [counts["applicable"]] + [counts.get(code, 0) for code in "UATF"]
        assert label + " & " + " & ".join(map(str, expected)) + " \\\\" in manuscript, role

rows = list(csv.DictReader((ROOT / 'survey_coding_table_2026-10-19.csv').open()))
assert len({r['record_id'] for r in rows}) == len(rows)
check_manuscript(rows)
print(json.dumps(summarize(rows), indent=2))
