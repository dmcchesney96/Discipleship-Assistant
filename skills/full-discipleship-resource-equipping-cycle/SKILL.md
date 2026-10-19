---
name: full-discipleship-resource-equipping-cycle
description: "Orchestrate an end-to-end, bounded resource/equipping workflow for real church handouts, worksheets, assignments, exercises, and leader guides: catalog originals, evaluate content, compare compatible resources, draft original tools when requested, propose bounded tests, and preserve traceable resource intelligence. Separate from full research and complete curriculum build cycles."
metadata:
  short-description: Run intake → evaluate → compare → design → learning for practical equipping tools
---

# Full Discipleship Resource & Equipping Cycle

## North Star
**Disciples who make disciples who make disciples.** This is a *resource workflow*, not a separate spiritual mission. Answer: **Which real tools can help ordinary people actually follow Jesus and help others do the same, and what should Southbrook adapt or develop?**

## Natural triggers
Use when user requests the **whole chain**, e.g.:
- "Evaluate this folder of handouts and assignments, compare the useful ones, and design a few resources for our training."
- "Process these ministry toolkits into a usable reviewed resource library."
- "Run our resources loop and propose practical materials for equipping disciple-makers."

For *only one* evaluation / comparison / tool, route to the specialist and stop. For "research whether X works", route to `full-discipleship-research-cycle`. For "how should our church implement X" without concrete supplied materials, use `full-discipleship-practice-design-cycle`. For a complete multi-week class/course, use `full-discipleship-curriculum-build-cycle` **and** resource review as a narrow intermediate step where valuable; do not run two whole orchestrators.

## Output / authorization contract
Translate the request into: source boundary, target learners, equipping outcome, artifacts requested, review depth, permissions/access, and desired destination. Infer minor missing details with labeled assumptions, but ask if missing source access, doctrine, rights or audience safety fundamentally blocks the task.

Authorized internal work: retrieve, inventory, evaluate, compare, draft requested original resources, suggest limited tests. Do **not** auto-publish, send, launch training, approve doctrine, commit personnel, or promote drafts to active practice. Drive writes require user authorization/standing permission and verified parent folder; preserve original material.

## Bounded chain (manager-owned, not automatic inter-skill recursion)
1. **Scope / current context:** use `ministry-context-retriever` for existing materials/index, targeted Southbrook current reality and `discipleship-alignment-lens-retriever` for design preferences. The user may specify sources without wanting whole-Brain browsing.
2. **Intake / dedup:** `discipleship-resource-intake-cataloger` inventories originals, child exercises, provenance, versions, rights, sensitivity and review priorities. Never call every source "evidence of effectiveness."
3. **Evaluate:** `discipleship-resource-evaluator` reviews priority artifacts at exact locators with six independent lenses; record must-fix risks, use case, rights status and honest limitations. Skip low-yield material by explicit reason.
4. **Compare:** `discipleship-resource-comparison-extractor` compares reviewed alternatives sharing a purpose; if only one is present, skip comparison. Avoid forced winner or incompatible cherry-picking.
5. **Decide design disposition:** `USE / CONSIDER AS-IS (RIGHTS + PASTORAL CHECK)`, `ADAPT WITH PERMISSION`, `WRITE ORIGINAL INSPIRED BY GENERAL METHODS`, `TRY ALTERNATIVES`, `MORE INFO`, `NOT NOW`. Recommendation does not equal decision.
6. **Draft (when requested):** `discipleship-training-tool-designer` creates the smallest adequate original assets and links inspiration. For full curriculum use existing curriculum architect; for a selected pilot implementation kit use existing kit builder.
7. **Quality check:** verify source trace, theological/safeguarding/rights gates, cross-resource coherence, usability, capability transfer, teacher/coach burden, accessibility, reproduction and versioning. Distinguish simulation/editorial QA from live field testing.
8. **Testing proposal (not automatic execution):** identify a bounded hands-on try with a few participants, observations, learning question, feedback and stop/adapt criteria. For a ministry experiment/pilot, hand off to `discipleship-experiment-pilot-designer` and later `discipleship-pilot-learning-evaluator` *only when relevant and authorized*.
9. **File / index:** `discipleship-research-librarian-drive-curator` manages verified destinations and links to originals. Separate `SOURCE`, `RESOURCE REVIEW`, `COMPARISON`, `DRAFT`, `PILOT MATERIAL`, `APPROVED TOOL`; never overwrite versions or imply approval. Proposed new resource intelligence folder must not be described as existing until verified.
10. **Readout / stop:** report coverage, what the best materials teach us, strongest weaknesses, what was designed vs suggested, unreviewed/blocked items, permission issues, exact saved links, and the next decision; then stop. No research synthesis update unless a verified generalizable claim changes.

## Escalation rules
- `source-evidence-checker` for consequential causal/empirical claims, not every helpful assignment.
- `church-movement-case-study-analyzer` if resource meaning depends on undocumented organizational operating context.
- `southbrook-practice-fit-assessor` if evaluating a broad ministry practice or commitment, not merely a handout's suitability.
- `full-discipleship-curriculum-build-cycle` for complete multi-session capability progression.
- `southbrook-brand-artifact-stylist` only after substance is settled, when ministry-facing final drafts are requested.

## Checkpoint / resumption for large folders
After each bounded batch write an honest manifest: source IDs and locators, processed vs pending, dedup links, evaluations completed, rights gaps, draft links, unresolved issues, next precise task. On resumption read checkpoint and compare to live folder changes; do not replay finished work or claim unfinished parts complete. Stop at authorization/usage/source-access barriers and give a precise restart instruction.

## Final reporting contract
- **START HERE:** 2–4 useful takeaways, not a file dump
- **Scope and coverage:** reviewed / indexed only / inaccessible / deferred, exact counts where known
- **Best resource elements and why:** observation separated from prediction
- **Comparisons and recommendations:** tradeoffs, permissions, local fit
- **New draft assets:** exact files + status; otherwise explicitly none
- **Potential test:** what a real user would need to demonstrate
- **Brain/GitHub changes:** actual writes verified vs proposals
- **What not to claim yet:** no efficacy, impact, approval, or reuse-rights overclaim.

## Success criterion
Not the number of PDFs cataloged. Success is an auditable chain from source material through reviewed useful techniques into a simpler, workable, teachable tool and then honest learning from actual use, **without treating the resources as empirical research papers**.
