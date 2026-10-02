# Full Discipleship Research Cycle

## Goal

Allow one natural-language request to carry a research question all the way from **what the Brain already knows** to **new durable learning**, without requiring the user to manually ask for each intermediate step.

## One-command loop

`CONTEXT → GAP → CONTRACT → RESEARCH → PRESERVE → VERIFY → STRESS-TEST → COMPARE → UPDATE → FILE → READOUT`

The manager routes to `full-discipleship-research-cycle` when the user clearly asks for the whole process.

## Why this exists

The repository already had strong bounded skills for:

- finding research gaps;
- writing research prompts;
- ingesting sources;
- verifying AI reports;
- checking evidence;
- comparing research;
- connecting patterns;
- maintaining the Living Synthesis;
- curating Drive.

The missing pieces were:

1. a skill that **actually executes** a deep research contract; and
2. an orchestrator that is explicitly allowed to chain the bounded skills through the whole lifecycle.

## Default sequence

1. `ministry-context-retriever`
2. `discipleship-research-scout-agenda-builder` when the question is not already specified
3. `daily-discipleship-research-prompt` in `SELF_EXECUTE` mode
4. `discipleship-deep-research-executor`
5. `discipleship-research-librarian-drive-curator` to preserve the report
6. `ai-research-verification-integration`
7. `source-evidence-checker`
8. `compare-big-picture`
9. `pattern-connector` only when a cross-source pattern materially changes
10. `living-discipleship-synthesis-maintainer` only when durable conclusions change
11. `discipleship-research-librarian-drive-curator` to verify links/placement
12. user-facing readout: simple language first, full evidence below

## Persistence layers

### External Evidence

The generated research report is preserved as `AI-GENERATED RESEARCH INPUT`. It remains an evidence artifact, not project truth merely because the assistant created it.

### Research Intelligence

Store or update:

- Claims & Evidence;
- Verification Queue;
- Contradictions & Disagreements;
- Strongest Converging Principles;
- Research Gaps & Open Questions;
- guardrail candidates.

### Living Synthesis

Update only when assessed evidence materially confirms, strengthens, narrows, complicates, contradicts, or adds a durable conclusion.

### GitHub operating system

A research cycle may create a **guardrail candidate**, but it does not autonomously edit AGENTS.md, governance, or evidence-derived guardrails. Operating-system changes remain explicit change-management work.

## Evidence gates

A full research cycle is not automatically a full synthesis update.

Possible outcomes:

- `NO DURABLE CHANGE`
- `NEW LEAD`
- `STRENGTHENS`
- `NARROWS`
- `COMPLICATES`
- `CONTRADICTS`
- `NEW DURABLE PRINCIPLE`
- `GUARDRAIL CANDIDATE`

## Redundancy gate

Before external research, ask whether the Brain already has enough assessed evidence to answer the question. If yes, stop the external research phase and synthesize what is already known rather than spending research effort to recreate it.

## Verification independence

The research executor cannot certify its own claims by rereading its report.

The verification pass must reopen original/stronger sources and test:

- population;
- date;
- method;
- denominator;
- causality;
- source independence;
- self-report bias;
- contrary evidence;
- multiplication unit/generations;
- transferability.

## User-facing output

Every full-cycle run begins with:

1. **START HERE — What this means in normal language**
2. **The biggest takeaways that may affect discipleship ministry**
3. **What changed in the Discipleship Brain**

Only then does it provide:

4. detailed sourced findings;
5. limitations;
6. one next move, if needed.

## Authorization

A full-cycle request authorizes bounded internal Drive writes for the cycle's report, audit, Research Intelligence, and warranted Living Synthesis updates.

It does not authorize deletion, sharing changes, external communication, ministry commitments, or self-modification of GitHub governance.
