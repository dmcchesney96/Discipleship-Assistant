#!/usr/bin/env python3
"""Dependency-free structural checks for discipleship synthesis repo contracts.

This checks routing, templates, and safety language. It does NOT test semantic
reasoning or independently verify research. Run from repository root:
    python3 tests/check_principle_contract.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXPECT = {
    "AGENTS.md": [
        "discipleship-principle-backfill",
        "docs/principle-synthesis-system.md",
        "Master Principles Index",
    ],
    "docs/skill-routing.md": [
        "discipleship-principle-backfill",
        "Historical evidence-to-principle backfill",
        "living synthesis only when warranted",
    ],
    "docs/drive-map.md": ["Master Principles Index", "LIVING DISCIPLESHIP SYNTHESIS"],
    "docs/principle-synthesis-system.md": [
        "source-family",
        "Master Index",
        "NOT",  # strong boundary against automatic promotion
    ],
    "skills/discipleship-principle-backfill/SKILL.md": [
        "resumable manifest",
        "source-family",
        "DEEP REVIEWED",
        "NO DURABLE CHANGE",
        "Southbrook",
    ],
    "skills/living-discipleship-synthesis-maintainer/SKILL.md": [
        "stable",
        "counterevidence",
        "INDEX OUT OF SYNC",
    ],
    "skills/pattern-connector/SKILL.md": [
        "source-family map",
        "alternative explanation",
    ],
    "skills/compare-big-picture/SKILL.md": [
        "Candidate Principle Disposition",
        "NO DURABLE CHANGE",
    ],
    "templates/durable-principle-record-template.md": [
        "Principle ID",
        "Claim-level evidence map",
        "Independent primary source families",
        "Version and epistemic change log",
    ],
    "templates/principle-master-index-template.md": [
        "Topic record URL",
        "Last reviewed",
        "never recycle",
    ],
    "templates/principle-backfill-manifest-template.md": [
        "Resume pointer",
        "DEEP REVIEWED",
        "Candidate disposition ledger",
    ],
    "tests/principle-synthesis-cases.md": [
        "Case A",
        "Case B",
        "Case C",
        "Case D",
        "NOT RUN",
    ],
}
errors = []
for path, markers in EXPECT.items():
    f = ROOT / path
    if not f.is_file():
        errors.append(f"MISSING FILE: {path}")
        continue
    body = f.read_text(encoding="utf-8")
    for marker in markers:
        if marker not in body:
            errors.append(f"MISSING MARKER in {path}: {marker}")

if errors:
    print(f"FAIL — {len(errors)} structural-contract error(s)")
    for error in errors:
        print(" -", error)
    raise SystemExit(1)
print(f"PASS — {len(EXPECT)} structural files checked, all required markers found")
print("NOTE: This is NOT a behavioral LLM evaluation or research verification.")
