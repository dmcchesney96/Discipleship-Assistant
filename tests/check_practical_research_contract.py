#!/usr/bin/env python3
"""Static routing/packaging checks; does not certify reasoning or live writes."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
def require(path, markers):
    file = ROOT / path
    if not file.exists():
        errors.append(f'Missing {path}')
        return
    content = file.read_text()
    for marker in markers:
        if marker not in content:
            errors.append(f'{path}: missing {marker}')

cycle = 'full-discipleship-practical-research-cycle'
verifier = 'discipleship-practice-source-verifier'
for file in ['AGENTS.md', 'docs/skill-routing.md', 'agents/manager.md', 'config/assistant.yaml', 'skills/README.md']:
    require(file, [cycle])
for file in ['AGENTS.md', 'docs/skill-routing.md', 'config/assistant.yaml']:
    require(file, [verifier])
require(f'skills/{cycle}/SKILL.md', ['UNKNOWN', 'CAPTURE MODE', 'NO DURABLE CHANGE', 'raw report', 'PRACTICE INTELLIGENCE', 'BLOCKED', 'format overrides', 'references/practical-research-contract.md'])
require(f'skills/{verifier}/SKILL.md', ['PRESCRIBED METHOD', 'REPORTED USE', 'OBSERVED USE', 'INACCESSIBLE', 'UNVERIFIED', 'UNKNOWN', 'source-family', 'same-agent', 'references/operational-verification-register.md'])
require(f'skills/{cycle}/references/practical-research-contract.md', ['Resume checkpoint', 'Worked example', 'unknowns'])
require(f'skills/{verifier}/references/operational-verification-register.md', ['Claim type', 'Access depth', 'Corrected wording'])
for skill, template in [('discipleship-resource-evaluator', 'discipleship-resource-review-card-template.md'), ('discipleship-resource-comparison-extractor', 'discipleship-resource-comparison-template.md')]:
    require(f'skills/{skill}/SKILL.md', [f'references/{template}'])
    require(f'skills/{skill}/references/{template}', [])
for error in errors:
    print(error)
print(f'{"FAIL" if errors else "PASS"}: practical research contract, {len(errors)} errors (structural only)')
sys.exit(bool(errors))
