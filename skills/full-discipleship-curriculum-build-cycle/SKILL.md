---
name: full-discipleship-curriculum-build-cycle
description: Orchestrate an end-to-end discipleship curriculum build from relevant Discipleship Brain retrieval and source-gap analysis through targeted research/verification, capability definition, curriculum architecture, full session materials, assessment/transfer design, and run-ready implementation assets. Use when the user asks for a complete course/class/curriculum and wants the Brain/research to shape the whole build without managing intermediate prompts.
metadata:
  short-description: Run the whole Brain-to-curriculum build in one request
---

# Full Discipleship Curriculum Build Cycle

## Purpose

Take a natural-language request such as:

> "Use the Brain and build an eight-week class that helps ordinary people study the Bible for themselves. Make everything we need."

and carry the work from **existing knowledge → source sufficiency → targeted gaps → curriculum architecture → full materials → assessment → implementation readiness** without requiring the user to manually invoke each specialist skill.

Core flow:

`COURSE GOAL → RELEVANT BRAIN CONTEXT → PASTORAL ALIGNMENT LENS → SOURCE/GAP AUDIT → TARGETED RESEARCH IF NEEDED → VERIFICATION → CAPABILITY MAP → CURRICULUM → ASSESSMENT/TRANSFER → RUN-READY ASSETS → QA → PERSIST/STOP`

The aim is not "more content."

The aim is a faithful, research-grounded learning experience that transfers a discipleship capability to ordinary people.

## Resource-design aim

Apply [the heart of our resources](../../AGENTS.md#heart-of-the-resources-we-create), explicitly adopted by Dan: practice following Jesus together and equip people to help someone else do the same. In the design and final review, identify the concrete practice, the relational support or shared setting, and the supported next step for helping another person. Scale these to the resource and audience; preserve existing competence and pastoral boundaries.

## Natural-language trigger

Automatically route here when the user asks for a **complete multi-session curriculum/course/class/training** and clearly wants the existing Brain/research/resources to shape the build, especially language such as:

- "Build the full 8-week class."
- "Use the Brain and make the whole curriculum."
- "Create everything we need to teach people how to..."
- "Reference our research and resources and build the full course."
- "Do the research you need and then make the curriculum without me prompting each step."

The user never needs to say the skill name.

### Precedence

This route takes precedence over:

- `full-discipleship-practice-design-cycle` when the requested artifact is specifically a curriculum/course;
- `discipleship-practice-implementation-kit-builder` when the request requires actual curriculum architecture, not merely tools for an already-designed pilot;
- `compare-big-picture` when comparison is only one intermediate step in a full curriculum build.

If the user asks only for an outline, syllabus, week sequence, or redesign of an existing curriculum, route directly to `discipleship-curriculum-architect`.

## Authorization boundary

A full curriculum-build request authorizes:

- Brain retrieval and analysis;
- bounded internal synthesis;
- targeted external research where materially needed;
- curriculum design;
- draft facilitator/participant materials;
- assessment design;
- internal artifact creation.

It does **not** automatically authorize:

- launching the class;
- committing staff/volunteers;
- publishing publicly;
- spending money;
- changing approved church doctrine/strategy;
- recording a draft as an approved Southbrook decision.

Drive writes should follow the user's explicit request or established project authorization and must preserve PROPOSED vs APPROVED status.

## Stage 1 — Define the course contract

Translate the user's request into:

- target audience;
- starting assumptions;
- discipleship problem;
- desired transformation;
- final authentic capability;
- duration/cadence;
- setting/session length if known;
- local constraints;
- required outputs;
- multiplication/reproduction goal if relevant.

Do not ask for details that can be responsibly inferred and labeled.

Ask only if a missing decision would materially change doctrine, audience safety, or the entire course design.

## Stage 2 — Retrieve the smallest sufficient Brain context

Route to:

`ministry-context-retriever → discipleship-alignment-lens-retriever`

Search the canonical Discipleship Brain first for the bounded topic. Retrieve the smallest relevant Pastoral Convictions & Design Lens separately as `USER ALIGNMENT / PASTORAL LENS`, especially the Bible & Curriculum Design Philosophy for curriculum work.

Retrieve only evidence likely to change the course, such as:

- relevant Living Synthesis entries;
- verified Research Intelligence;
- relevant Practice Cards/landscapes;
- prior research reports;
- Southbrook diagnostic/local context;
- existing class notes/templates;
- prior pilots/learning;
- approved doctrinal or strategic constraints;
- relevant pastoral convictions, curriculum preferences, explicit "NOT FOR US" constraints, and open tensions.

Do **not** load the entire Brain or the entire Pastoral Lens simply because they exist.

Report:

- what is already known;
- what is promising but uncertain;
- what is missing;
- whether the current evidence base is sufficient;
- which design choices are being shaped by the Pastoral Lens rather than evidence.

## Stage 3 — Run the source/gap audit

Create a compact matrix:

| Design question | Existing support | Source quality | Gap? | Action |
|---|---|---|---|---|

Include at minimum:

- biblical/theological content;
- formation/learning mechanisms;
- practical teaching methods;
- local fit;
- assessment/transfer;
- reproduction/teach-back where relevant.

### Redundancy rule

If the Brain already contains sufficient assessed evidence, **do not research the same question again**.

### Gap rule

Only research gaps that could materially change:

- what is taught;
- how it is taught;
- how capability is assessed;
- theological/pastoral guardrails;
- accessibility;
- reproduction strategy.

## Stage 4 — Fill material gaps only

When meaningful gaps remain, use the narrowest tool/skill.

Possible routes:

- `source-evidence-checker` — verify a consequential existing claim;
- `discipleship-deep-research-executor` — run a bounded new research contract for a genuine missing question;
- `discipleship-practice-intelligence-builder` — gather concrete methods used by credible practitioners/churches;
- `church-movement-case-study-analyzer` — deepen one especially relevant model;
- `ai-research-verification-integration` — interrogate an AI-generated report already in the Brain.

Do not launch a full research cycle unless the curriculum truly depends on a major unanswered research question.

### Special theological rule

For Bible interpretation, doctrine, spiritual authority, or similarly consequential theological content:

- do not let AI-generated research be the sole authority;
- prioritize Scripture, responsible scholarship, primary/approved doctrinal sources, and pastoral/theological accountability;
- preserve genuine interpretive disagreement instead of inventing certainty.

## Stage 5 — Build the evidence packet

Before writing the curriculum, consolidate the minimum usable evidence set.

Separate:

- Scripture/theological anchors;
- verified research;
- mechanism support;
- documented practice;
- reported outcomes;
- local evidence;
- practitioner opinion;
- interpretation/hypothesis.

This packet becomes the curriculum's source foundation.

Do not count repeated AI reports drawing on the same underlying source as independent convergence.

## Stage 6 — Architect the curriculum

Route to:

`discipleship-curriculum-architect`

The architect must:

1. define the final authentic performance;
2. build the competency map;
3. backward-design the progression;
4. create the course arc;
5. design each session;
6. include modeling, guided practice, actual participant practice, and feedback;
7. fade scaffolds as capability increases;
8. include between-session repetition;
9. test transfer on fresh tasks;
10. build bounded teach-back/reproduction when appropriate;
11. create the facilitator + participant asset stack.

A multi-week course that merely divides information across weeks has not completed this stage.

## Stage 7 — Design measurement and transfer

Route to `discipleship-measurement-architect` when the course needs a meaningful evaluation plan.

Measure the construct the course claims to develop.

For skill-building courses, distinguish:

- attendance;
- satisfaction;
- knowledge recall;
- confidence;
- actual performance;
- fresh-task transfer;
- continued practice;
- help given to another person;
- next-generation capability when reproduction is claimed.

Where feasible, include:

- baseline;
- formative practice evidence;
- final authentic task;
- delayed/continued-use check.

Do not turn spiritual maturity into a simplistic grade.

## Stage 8 — Make the course run-ready when requested

If the user's request includes "everything we need," "ready to run," or equivalent, route operational pieces to:

`discipleship-practice-implementation-kit-builder`

Use it only for the pieces beyond curriculum architecture, such as:

- facilitator training;
- quick-start guide;
- coaching rhythm;
- launch checklist;
- troubleshooting;
- fidelity essentials vs adaptable elements;
- escalation/safeguarding boundaries;
- implementation learning prompts.

The curriculum architect owns the learning journey and session content. The implementation-kit builder owns practical execution support.

## Stage 9 — Create requested artifacts

When requested and tools permit, produce the appropriate editable/source artifacts and final participant/leader outputs.

Possible artifacts:

- master curriculum document;
- facilitator guide;
- participant workbook;
- printable handouts/cards;
- assessment rubric;
- slide outline/deck;
- launch/training guide;
- source/evidence ledger.

Use the relevant artifact skill/tool instructions for PDFs, DOCX, slides, or spreadsheets.

Do not invent links or claim files were created when they were not.

## Stage 10 — Run final curriculum QA

Before calling the work complete, verify:

### Source QA
- important factual/theological claims are traceable;
- AI reports are not treated as evidence by themselves;
- uncertainty is preserved.

### Curriculum QA
- each week advances the final capability;
- content volume does not crowd out practice;
- participants actually do the skill;
- feedback is built in;
- supports fade;
- final assessment matches the outcome;
- fresh transfer is tested.

### Discipleship QA
- the course supports life with Jesus, obedience, formation, mission, disciple-making, or multiplication rather than technique alone;
- early reproduction is bounded by competence and coaching;
- authority/safeguards are proportionate.

### Reproducibility QA
- ordinary leaders can facilitate it;
- ordinary participants can remember/use the core process;
- staff dependence is not unnecessarily high.

### Local-fit QA
- Southbrook language and constraints are honored;
- relevant stored curriculum/design preferences are honored where they do not conflict with current instruction, doctrine, approved decisions, or stronger evidence;
- PROPOSED vs APPROVED status is clear.

If a serious QA failure is found, fix it before final delivery.

## Stage 11 — Preserve appropriately

When the user authorized saving:

- raw/new research → appropriate Research Intelligence/source area;
- reusable verified principles → Living Synthesis only if evidence warrants;
- curriculum draft → proposal/Agent Workspace or user-specified curriculum folder;
- approved pilot curriculum → relevant `09 — EXPERIMENTS, PILOTS & LEARNING` folder;
- approved strategic decisions → `10 — STRATEGY & DECISIONS`.

Creating a curriculum does not make the curriculum approved strategy.

## Final readout

Lead with:

# START HERE — What this course is designed to produce

Explain the final real-world capability in plain language.

Then give:

## Course shape
The progression and why it is sequenced that way.

## What the Brain contributed
The most important existing findings/practices that shaped the design.

## What new research was needed
Only genuine gaps researched, with boundaries.

## What participants will actually practice
Not just what they will hear.

## How we will know whether capability transferred
Assessment + fresh-task transfer + continuation/reproduction.

## Materials created
Exact artifacts completed.

## What remains proposed / needs human review
Doctrinal, pastoral, staffing, launch, or approval boundaries.

## What was saved in the Brain
Links/status when applicable.

## Stop conditions

Stop when:

- the complete requested curriculum and run-ready assets are finished;
- additional research would be repetitive rather than decision-changing;
- a material theological/doctrinal issue requires human pastoral judgment;
- the user requested a draft only;
- the next action is launch/approval rather than curriculum construction.

## Success test

A successful one-command curriculum build answers:

1. What does the Brain already know about this problem?
2. What important source gaps actually mattered?
3. What final capability are we trying to transfer?
4. What sequence develops that capability?
5. Where do participants practice and receive feedback?
6. How does responsibility move from leader to learner?
7. How will we test fresh transfer instead of completion?
8. How does the curriculum connect to the North Star?
9. Can ordinary leaders and participants carry it?
10. What is still proposed, uncertain, or awaiting human approval?
