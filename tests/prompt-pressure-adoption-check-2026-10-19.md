# Adoption check — adaptive critical research prompting (2026-10-19)

## Decision and scope

User explicitly requested that the discussed, refined prompting skill become the repository version on 2026-10-19. This release updates the existing `skills/daily-discipleship-research-prompt/SKILL.md` **in place** instead of creating a competing skill/router. The original skill remains recoverable from Git history and its prior blob SHA `7b5bd4e0da8802bf206f9d0cb2a4997e0d0c4337`.

## What's new

Four selectively applied reasoning checks are embedded in research prompts and SELF_EXECUTE contracts: challenge the premise, steelman the strongest alternative, name reversal criteria, then reconsider a recommendation only if warranted. A compact seven-lever optional toolkit is retained for audience, creative constraints, high standards and fair opposition. Narrow factual/source tasks avoid artificial debates. Integrity rules prohibit fabricated earlier conversations, invented sources, falsely causal claims and unjustified disciple-generation extrapolations.

## Checks actually performed

Read original `main`, candidate branch and updated contract tests directly using connected GitHub; 10/10 **static text/structural comparisons** passed:

1. Original `SKILL.md` reconstructs exactly when the one new section is removed.
2. Original frontmatter is byte-identical.
3. Both invocation modes and literal deep-research-executor handoff remain present.
4. All four critical checks appear.
5. Narrow fact-check exemption and proportionate use appear.
6. Seven optional levers and 2–3 selection limit appear.
7. Unverified/false-memory/generational safeguards appear.
8. Interrupted-work restart/checkpoint requirement persists.
9. Added Python regression file defines five test methods.
10. Key assertions in the Python tests match candidate skill text.

**Scope of checks:** These were deterministic connector-side comparisons; the Python test suite was added but not executed on a checkout in this run. Structural compliance is **not a demonstration of model reasoning performance**. The prior 2026-10-17 one-session same-gap A/B pilot was not blinded or repeated; its provisional 9/12 vs 12/12 ratings are directional development feedback only. No new independent A/B or fact-accuracy evaluation was executed for this release.

## Size and reversibility

Baseline skill: 9,137 characters. Refined skill: 13,065 characters (+3,928). The first experimental version was 14,506 characters; this final one is shorter by 1,441. No changes to research-executor or substantive Brain source/evidence hierarchy. Any regressions can be rolled back using Git commit history.

## Operational follow-up

When convenient, run `python tests/check_skills.py` and `python -m unittest discover -s tests -p 'test_prompt_pressure_contract.py'` on a GitHub checkout. Then repeat `tests/prompt-pressure-evals.md` PP1–PP7 with pinned baseline and candidate, fresh isolated runs, blind scoring, independent original-source audit, and cost tracking. A practical benefit claim should rest on those results, not static checks.
