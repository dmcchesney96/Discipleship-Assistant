# Skills

The skill library has two layers.

## Shared ministry intelligence core

Reusable across ministry assistants:

1. `ministry-second-brain-intake`
2. `ministry-context-retriever`
3. `current-state-synthesizer`
4. `source-evidence-checker`
5. `knowledge-conflict-resolver`
6. `decision-action-extractor`
7. `institutional-memory-writer`
8. `pattern-connector`

## Discipleship-specific skills

1. `full-discipleship-research-cycle` — explicit multi-skill orchestrator for one-command research
2. `discipleship-deep-research-executor` — conducts a defined deep research contract
3. `discipleship-research-report-publisher` — creates the reusable professional PDF + editable master
4. `full-discipleship-practice-design-cycle` — orchestrates local problem → practice → fit → test/pilot
5. `full-discipleship-curriculum-build-cycle` — orchestrates relevant Brain retrieval → source-gap audit → curriculum → assessment → run-ready assets
6. `discipleship-curriculum-architect` — designs research-grounded multi-session curriculum around capability transfer
7. `discipleship-practice-intelligence-builder` — creates concrete external Practice Cards and comparisons
8. `discipleship-practice-intelligence-backfill` — mines large existing corpora into deduplicated Practice Intelligence
9. `southbrook-practice-fit-assessor` — evaluates local fit and action warrant
10. `discipleship-pilot-learning-evaluator` — evaluates local pilot results and updates action warrant
11. `discipleship-practice-implementation-kit-builder` — creates ready-to-run tools/training for selected pilots
12. `discipleship-research-source-ingestor`
13. `daily-discipleship-research-prompt`
14. `discipleship-research-scout-agenda-builder`
15. `ai-research-verification-integration`
16. `compare-big-picture`
17. `church-movement-case-study-analyzer`
18. `southbrook-interview-qualitative-evidence-analyzer`
19. `southbrook-discipleship-diagnostic`
20. `living-discipleship-synthesis-maintainer`
21. `discipleship-measurement-architect`
22. `discipleship-experiment-pilot-designer`
23. `southbrook-discipleship-operating-system-designer`
24. `discipleship-research-librarian-drive-curator`
25. `strategy-decision-brief-builder`

## Skill rule

A skill owns one bounded transformation. The master assistant chooses which skill(s) to use and which tools/evidence sources are appropriate. Skills should not independently trigger expensive chains of other skills unless a calling workflow explicitly requests that handoff.

`full-discipleship-research-cycle`, `full-discipleship-practice-design-cycle`, and `full-discipleship-curriculum-build-cycle` are intentional orchestrator exceptions. Their bounded job is to manage complete handoff sequences while leaving research, practice intelligence, fit assessment, verification, synthesis, pilot design, measurement, and library work to the specialist skills.

Each skill inherits `AGENTS.md` and governance rules.
