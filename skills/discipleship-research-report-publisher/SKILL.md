---
name: discipleship-research-report-publisher
description: Transform a completed, verification-aware discipleship research report into a polished, professional, highly skimmable PDF plus an editable source artifact. Preserve claim-level citations, evidence/confidence labels, limitations, and Brain-change notes. Use for full-cycle final research publication or when the user asks to turn a research report into the standard Discipleship Brain PDF format.
metadata:
  short-description: Publish verified discipleship research as a professional PDF
---

# Discipleship Research Report Publisher

## Purpose

Create the **human-reading artifact** for discipleship research.

The deep-research executor produces content. Verification tests important claims. This skill turns the finalized, verification-aware content into a professional report that is easy to skim, reference, print, and revisit.

The finished PDF should feel like a serious research publication rather than a chat transcript or plain exported document.

Use the reusable visual/content standard in:

- `docs/research-report-pdf-standard.md`
- `templates/research-report-pdf-template.md`

## Trigger

Use when:

- a `full-discipleship-research-cycle` reaches final publication;
- the user asks for a research report as a polished PDF;
- an existing research report should be reformatted into the standard Brain research-report design.

Do not use this skill to decide what the research proves. It publishes already analyzed/verification-aware content.

## Required inputs

- final research title;
- research question;
- as-of date;
- verified/assessed key findings;
- evidence/confidence labels;
- major limitations / evidence boundary;
- source ledger with stable source IDs;
- claim register or equivalent claim-to-source mapping;
- Brain impact summary;
- Southbrook implications clearly labeled as hypothesis/question/recommendation status;
- raw/full research content to preserve beneath the summary layer.

## Artifact set

Create **two linked artifacts** whenever the environment supports it:

1. **Editable master**
   - Prefer DOCX for long-form text-heavy reports.
   - Preserve styles, headings, tables, source links, and accessibility.
   - This is the source file used for later corrections/revisions.

2. **Polished PDF**
   - This is the primary human-facing reading artifact.
   - It should visually match the standard in `docs/research-report-pdf-standard.md`.

Do not make the PDF the only surviving copy of the report.

If an editable document workflow is unavailable, use the best available structured source format, but still create the PDF when possible.

## Authoring / rendering workflow

For text-heavy reports, prefer:

`STRUCTURED FINAL CONTENT → DOCX MASTER → PDF EXPORT/CONVERSION → RENDER TO IMAGES → VISUAL QA → FIX → FINAL PDF`

If DOCX is unavailable, use an equivalent reliable HTML/LaTeX/programmatic workflow.

### Mandatory PDF QA

Before calling the artifact finished:

1. render every PDF page to images;
2. inspect for clipped text, overlap, broken glyphs, stranded headings, broken tables, orphaned callouts, and unreadable citations;
3. verify page numbering and running headers;
4. verify the title, date, evidence-weighted answer, source appendix, and final page are present;
5. check that major tables remain readable at normal page size;
6. fix and re-render if needed.

Never claim the PDF is finished without this render-and-inspect pass when rendering capability is available.

## Publication timing in a full research cycle

Publish the polished PDF **after** major claims have passed the owner's required source-based second-pass verification and the cycle has determined what changed in the Brain. Prefer fresh independent verification. When the owning cycle expressly permits a same-agent source-based pass, publish with that limitation visible and never label it independent. Reopening adequate originals and correcting consequential claims remain mandatory; rereading the generated report alone is insufficient.

The raw executor report may be preserved earlier as `AI-GENERATED RESEARCH INPUT`, but the polished PDF should incorporate:

- corrected/downgraded claims;
- final evidence/confidence language;
- meaningful contrary evidence;
- final synthesis/Brain impact;
- source IDs that map to the final source ledger.

The polished PDF must not preserve a claim as settled if verification later weakened it.

## Core report architecture

Default page flow:

1. Cover
2. Start Here / Executive Summary
3. Research framing + definitions/evidence boundary
4. Key findings
5. Biblical/theological analysis when relevant
6. Academic/empirical evidence
7. Case studies / movement evidence when relevant
8. Failure modes / counterevidence
9. Practice → Mechanism → Principle
10. Local-church implications
11. Ideas worth testing
12. What this research does not prove
13. What changed in the Discipleship Brain
14. Unresolved questions / further research
15. Sources / source ledger
16. Optional appendices: claim register, methodology, detailed tables

Do not force empty sections. Preserve the logic of the research while maintaining the standard hierarchy.

## First-three-pages rule

The first 2–3 pages must remain useful even if the reader never finishes the report.

They must contain:

- the research question;
- evidence-weighted answer;
- 3–6 biggest takeaways;
- confidence/evidence read;
- one clear evidence boundary;
- why this matters;
- what changed in the Brain, or a pointer to that section.

Do not bury the answer behind methodology.

## Claim-level citation standard

The user wants citations **next to supported claims**, not only in a bibliography.

### Source keys

Assign every cited source a stable source key from the final source ledger:

- `[S1]`
- `[S2]`
- `[S3]`

Use the same key throughout the report.

### Placement

Place citations immediately after the sentence, clause, statistic, or table cell they support.

Examples:

- Structured teaching plus actual teaching produced a larger average learning benefit than preparation alone. `[S4]`
- The movement's reported church count is organizational self-report rather than independent verification. `[S9]`
- The study followed adolescents across multiple waves, but the sample does not directly represent an adult local-church population. `[S2, Methods]`

Multiple sources:

`[S2; S6; S11]`

Specific pages/sections when useful:

`[S5, pp. 42–47]`

### Source appendix

Every source key must map to:

- author / organization;
- title;
- year/date;
- source type;
- direct URL/DOI/stable link when available;
- brief provenance note when needed.

Make source titles/links clickable in the editable master and PDF when the authoring system supports hyperlinks.

Do not use a source key for a source that cannot be identified.

## Evidence labels

Use project evidence/confidence language visually, but sparingly.

Recommended badges/callouts:

- `HIGH CONFIDENCE`
- `PROMISING`
- `CONTEXT DEPENDENT`
- `UNCERTAIN`
- `CONTRADICTED`

Also distinguish when needed:

- DOCUMENTED EVIDENCE
- ORGANIZATIONAL CLAIM
- PRACTITIONER OPINION
- INTERPRETATION
- HYPOTHESIS

Do not decorate every paragraph with a badge. Use labels where they help the reader judge a major finding.

## Required callout types

Use only when relevant:

### Evidence-weighted answer
The one-sentence or short-paragraph answer on the cover.

### Evidence boundary
What the evidence cannot establish.

### Why this matters
Why a finding matters for forming multiplying disciples.

### Do not overclaim
A tempting inference the evidence does not support.

### Southbrook implication
A local hypothesis/question/application. It must not be presented as external evidence.

### Brain change
What the research strengthened, narrowed, complicated, contradicted, or left unchanged.

## Table / figure rules

- Use tables for comparison, not decoration.
- Prefer 3–5 columns; split overly wide tables.
- Keep a short interpretation directly above or below every consequential table.
- Never make the reader infer the conclusion from a wall of data.
- If charts are used, label axes/units and cite the source beneath the chart.
- Do not use 3D charts, ornamental graphics, or stock photography.
- Diagrams should explain a mechanism, pathway, model, or evidence relationship.

## Writing style

- Pastor/leader-readable, research-grade.
- Lead with conclusions.
- Short paragraphs.
- Strong section headings.
- Concrete sentences.
- Avoid academic throat-clearing.
- Preserve nuance without filling every sentence with caveats.
- Use bold selectively for scan points, not entire paragraphs.
- Keep technical detail in body/appendix after the plain-language answer.

## File naming

Default:

`YYYY-MM-DD — [Short Research Title] — Discipleship Research.pdf`

Editable master:

`YYYY-MM-DD — [Short Research Title] — Discipleship Research.docx`

When filenames cannot use long punctuation safely, use standard hyphens.

## Drive placement

Resolve the live Drive folder before mutation.

Default for AI-assisted external research:

`02 — EXTERNAL EVIDENCE LIBRARY → 8. AI-Generated Deep Research`

Store the polished PDF and editable master together when appropriate, and link them to:

- raw executor research input;
- verification artifact;
- relevant Research Intelligence;
- any Living Synthesis update.

Do not guess Drive IDs.

## Output contract

Return:

### Published artifacts
- PDF title + link/path
- Editable master title + link/path
- page count

### Publication QA
- render inspected: yes/no
- clipping/overlap: pass/fail
- citation/source-key integrity: pass/fail
- source appendix present: yes/no
- major tables readable: yes/no
- fixes made after first render, if any

### Persistence
- Drive destination
- links to raw report/audit when available

### Notes
Only material publication limitations.

## Boundary

This skill publishes; it does not:

- independently re-run the research;
- override verification results;
- promote findings into the Living Synthesis;
- convert a hypothesis into an approved Southbrook decision.

## PRACTICAL report architecture override

When publishing `full-discipleship-practical-research-cycle`, use the owner's practical contract order: plain learning → concrete methods → worked operational examples → comparison/tradeoffs → documentation and outcome limits → reusable practices → Brain impact → audit/source ledger. Do not force an academic section, local pilot, or new principle. Preserve technical source traceability, default PDF/editable master, user format overrides and full visual QA. A constructed example must be labeled original illustration, not an observed event.
