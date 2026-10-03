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

1. `discipleship-convictions-capture` — captures Dan's freeform discipleship philosophy, strategy instincts, curriculum feedback, rejections, and open questions into the canonical Pastoral Lens
2. `discipleship-alignment-lens-retriever` — retrieves the relevant Pastoral Lens before substantial creation/design work
3. `full-discipleship-research-cycle` — explicit multi-skill orchestrator for one-command research
4. `discipleship-deep-research-executor` — conducts a defined deep research contract
5. `discipleship-research-report-publisher` — creates the reusable professional PDF + editable master
6. `full-discipleship-practice-design-cycle` — orchestrates local problem → practice → fit → test/pilot
7. `full-discipleship-curriculum-build-cycle` — orchestrates relevant Brain retrieval → source-gap audit → curriculum → assessment → run-ready assets
8. `discipleship-curriculum-architect` — designs research-grounded multi-session curriculum around capability transfer
9. `discipleship-practice-intelligence-builder` — creates concrete external Practice Cards and comparisons
10. `discipleship-practice-intelligence-backfill` — mines large existing corpora into deduplicated Practice Intelligence
11. `southbrook-practice-fit-assessor` — evaluates local fit and action warrant
12. `discipleship-pilot-learning-evaluator` — evaluates local pilot results and updates action warrant
13. `discipleship-practice-implementation-kit-builder` — creates ready-to-run tools/training for selected pilots
14. `discipleship-research-source-ingestor`
15. `daily-discipleship-research-prompt`
16. `discipleship-research-scout-agenda-builder`
17. `ai-research-verification-integration`
18. `compare-big-picture`
19. `church-movement-case-study-analyzer`
20. `southbrook-interview-qualitative-evidence-analyzer`
21. `southbrook-discipleship-diagnostic`
22. `living-discipleship-synthesis-maintainer`
23. `discipleship-measurement-architect`
24. `discipleship-experiment-pilot-designer`
25. `southbrook-discipleship-operating-system-designer`
26. `discipleship-research-librarian-drive-curator`
27. `strategy-decision-brief-builder`

## Skill rule

A skill owns one bounded transformation. The master assistant chooses which skill(s) to use and which tools/evidence sources are appropriate. Skills should not independently trigger expensive chains of other skills unless a calling workflow explicitly requests that handoff.

`full-discipleship-research-cycle`, `full-discipleship-practice-design-cycle`, and `full-discipleship-curriculum-build-cycle` are intentional orchestrator exceptions. Their bounded job is to manage complete handoff sequences while leaving research, practice intelligence, fit assessment, verification, synthesis, pilot design, measurement, and library work to the specialist skills.

Each skill inherits `AGENTS.md` and governance rules.
