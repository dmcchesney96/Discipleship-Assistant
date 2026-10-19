# Prompt-pressure v2: initial structural test report

**Date:** 2026-10-17 (America/New_York)  
**Repository:** `dmcchesney96/Discipleship-Assistant`  
**Files:** `skills/daily-discipleship-research-prompt/SKILL.md`, `tests/prompt-pressure-evals.md`, `tests/test_prompt_pressure_contract.py`  
**Baseline file SHA:** `7b5bd4e0da8802bf206f9d0cb2a4997e0d0c4337`  
**Candidate file SHA:** `7b2b6d22ba916f789f0676bd684fd9ab0aca60bf`

## What was actually checked

Used the connected GitHub reader to fetch original `main` and experimental-branch versions, and ran a direct tool-side deterministic comparison of file content. This did **not** execute the Python unit test file or launch fresh independent LLMs.

| Structural check | Result |
|---|---|
| Removing the added section restores every byte of the prior `SKILL.md` | PASS |
| All seven pressure levers represented | PASS |
| Choice limited to two or three relevant levers | PASS |
| Premise/opponent/decision/revision audit sequence present | PASS |
| Evidence-label and fabricated-memory safeguards present | PASS |
| PROMPT_ONLY, SELF_EXECUTE, executor routing, resume checkpoint preserved | PASS |
| Seven test scenarios with explicit non-run status present | PASS |
| Regression test file has four test methods | PASS |
| Original YAML frontmatter unchanged | PASS |

**9/9 structural checks passed.** This demonstrates presence and backward-compatible text preservation, **not** that generated prompts or research are better. The candidate increased skill length from 9,137 to 14,506 characters (+5,369): possible extra cost/complexity must be watched in a real A/B.

## Behavioral/accuracy status

- Fresh-agent A/B prompt generation with blind scoring: **NOT RUN**.
- Downstream dual-arm research with identical sources/model: **NOT RUN**.
- Original-source checks on 3 consequential downstream claims: **NOT RUN**.
- Formal claim of higher factual accuracy, reasoning, or creativity: **NOT SUPPORTED**.

## Next valid evaluation

Use `tests/prompt-pressure-evals.md`: run PP1–PP7 with each pinned skill version in separate fresh sessions, at least three repetitions each. Grade blindly (0–12), check fatal failures and output length, then run same-source downstream research for a subset. Keep branch unmerged until that evidence is available. If candidate fails negative control PP7 or worsens source accuracy, revise or revert.
