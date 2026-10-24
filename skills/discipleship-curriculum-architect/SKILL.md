---
name: discipleship-curriculum-architect
description: "Turn a defined discipleship formation/equipping outcome plus relevant verified Brain evidence into a coherent multi-session curriculum that transfers real capability: outcomes, progression, modeling, guided practice, independent practice, feedback, assessment, participant/leader materials, and reproduction where appropriate. Use for course/class/curriculum design; do not use to run a broad research cycle or launch ministry without authorization."
metadata:
  short-description: Build research-grounded discipleship curriculum for capability transfer
---

# Discipleship Curriculum Architect

## Purpose

Turn discipleship research, Scripture/theological anchors, documented practice, and local ministry context into a **coherent learning journey that changes what ordinary people can faithfully understand, practice, and help others do**.

The goal is not to fill a calendar with content.

The goal is to transfer a capability.

For example, a Bible-study course should not merely produce people who can name a method. It should increasingly produce people who can responsibly work through an unfamiliar passage, explain the reasons for their interpretation, recognize where they need help, respond faithfully, and—when appropriate—help another person begin learning the same process.

## Resource-design aim

Apply [the heart of our resources](../../AGENTS.md#heart-of-the-resources-we-create), explicitly adopted by Dan: practice following Jesus together and equip people to help someone else do the same. In the design and final review, identify the concrete practice, the relational support or shared setting, and the supported next step for helping another person. Scale these to the resource and audience; preserve existing competence and pastoral boundaries.

## Trigger

Use when the user asks to:

- build or redesign a discipleship curriculum, class, course, training series, workshop sequence, or multi-week learning experience;
- turn existing Brain research into a teachable progression;
- create a week-by-week course around a defined discipleship skill or formation outcome;
- build facilitator and participant materials from an already-defined evidence base.

If the user asks for the **entire pipeline** from Brain retrieval/gap analysis through research, curriculum, assessment, and run-ready assets, route to `full-discipleship-curriculum-build-cycle`.

If the practice itself has not been selected and the question is primarily what Southbrook should do, use `full-discipleship-practice-design-cycle` first.

## Boundary

This skill designs curriculum. It does not:

- treat an AI report as theological authority;
- conduct broad external research when the evidence base is undefined;
- certify doctrinal questions that require pastoral/elder judgment;
- convert course completion into evidence of spiritual maturity;
- launch, schedule, publicize, or require participation without authorization.

## Inputs

Use the smallest sufficient set of:

- target people / audience;
- desired transformation and end capability;
- duration and cadence;
- course setting and time available per session;
- relevant Brain research and Living Synthesis;
- relevant Practice Cards / documented practices;
- Southbrook context, constraints, and language;
- relevant `USER ALIGNMENT / PASTORAL LENS` entries, especially `02 — Bible & Curriculum Design Philosophy`;
- Scripture/theological anchors and doctrinal guardrails;
- source-quality notes and unresolved questions;
- accessibility needs;
- desired multiplication/reproduction outcome, if any.

If one of these is missing but can be responsibly inferred from the user's request and current project context, proceed and label the assumption. Ask only when the missing decision would materially change the course.

## Pastoral alignment layer

Before substantial curriculum creation or redesign, retrieve the smallest relevant pastoral lens through `discipleship-alignment-lens-retriever`.

Use the lens to understand:
- what Dan believes the curriculum should produce;
- preferred balance of Scripture, explanation, discussion, practice, feedback, and application;
- desired tone/depth/accessibility;
- what he has explicitly rejected or found unhelpful;
- unresolved design tensions.

Label this input `USER ALIGNMENT / PASTORAL LENS`. It is not research evidence or doctrinal authority. If it conflicts with the user's current instruction, approved Southbrook doctrine/decisions, or stronger evidence, surface the tension rather than silently forcing the preference.

## Core design convictions

### 1. Capability before coverage

Start with:

> What should an ordinary participant be increasingly able to understand, practice, discern, and reproduce after this course?

Do not begin by filling Week 1 through Week 8 with topics.

### 2. Backward design from authentic performance

Define the final real-world performance first.

Then identify the subskills, knowledge, habits, and practice repetitions required to reach it.

### 3. Formation is more than information

A discipleship curriculum may include knowledge, but should also consider:

- understanding;
- practice;
- obedience;
- character/attitude where appropriate;
- confidence grounded in competence;
- community/support;
- mission;
- ownership;
- reproduction.

Do not claim a class caused heart transformation that the evidence cannot establish.

### 4. Use a responsibility-transfer loop

Default pattern:

`MODEL → GUIDE → PRACTICE → FEEDBACK → RELEASE → TEACH-BACK`

Not every session needs every stage in equal proportion, but the course should visibly move participants from dependence toward responsible ownership.

### 5. Practice on fresh tasks

Familiarity can masquerade as competence.

When transfer matters, use unfamiliar passages, scenarios, conversations, or ministry situations to see whether the learner can carry the skill beyond the example used in teaching.

### 6. Feedback is part of the intervention

Participants need correction-rich practice, not only explanation.

Feedback should identify the reasoning/practice move to revise and return responsibility to the learner rather than replacing their work with the leader's finished answer.

### 7. Fade scaffolds by demonstrated ability

Reduce prompts, templates, supplied questions, and leader direction as learners demonstrate the relevant skill.

Do not remove access to wise help, Scripture, Christian community, pastors, teachers, or trustworthy resources merely to create artificial independence.

### 8. Reproduction should match competence

If multiplication is part of the course, participants may help others early in **bounded, demonstrated skills** while remaining under coaching.

Do not equate early participation with unrestricted teaching authority.

### 9. Ordinary-person reproducibility matters

Ask:

- Can a normal church member understand this?
- Can they practice it outside the classroom?
- Can a volunteer facilitator carry it?
- Can the core process be remembered without a giant manual?
- Can another person eventually learn it from them?

### 10. Accessibility is not an optional add-on

Where relevant, design for differences in:

- literacy;
- reading confidence;
- education;
- language;
- disability;
- schedule/cognitive load;
- prior biblical knowledge.

Audio/oral and visual practices may support access without lowering theological seriousness.

## Source architecture

Build from distinct evidence layers and never collapse them.

### A. Scripture + theological/doctrinal anchors

Use Scripture and responsible biblical/theological scholarship for claims about what Scripture teaches and what faithful interpretation/formation requires.

Southbrook's approved doctrinal commitments and pastoral judgment govern local doctrinal boundaries.

### B. Learning / formation evidence

Use credible research for mechanisms such as:

- retrieval;
- worked examples/modeling;
- deliberate/guided practice;
- feedback;
- scaffolding/fading;
- self-explanation;
- transfer;
- learning by teaching;
- habit/behavior support.

Adjacent learning evidence can support a mechanism without proving the exact ministry curriculum.

### C. Practice intelligence

Use documented church, ministry, missionary, historical, or practitioner practices to understand how a method actually operates.

A documented practice is not automatically a proven practice.

### D. User alignment / pastoral lens

Use the canonical Pastoral Convictions & Design Lens to improve fit. It records Dan's stated convictions/preferences and should shape design choices where appropriate without being treated as proof that a method works.

### E. Southbrook-local evidence

Use current diagnostic findings, participant experience, leader observation, pilot learning, and approved decisions to shape fit.

### F. AI-generated research

Treat as input and lead-generation.

Consequential claims used to shape theology, interpretation, assessment, or strategy should be verified against original/stronger sources when possible.

## Workflow

### Stage 1 — Write the course contract

State:

- audience;
- current starting point;
- problem being addressed;
- desired transformation;
- final capability;
- duration/cadence;
- local constraints;
- what the course is **not** trying to accomplish.

Use one clear end statement:

> By the end of this course, a participant should increasingly be able to ______ in a real setting with ______ level of support.

### Stage 2 — Build the competency map

Break the end capability into:

- essential knowledge;
- observable skills;
- judgment/discernment moves;
- practices/habits;
- relational/support behaviors;
- common misconceptions;
- prerequisite capabilities;
- reproduction/helping skills if relevant.

Distinguish **must know**, **must be able to do**, and **helpful enrichment**.

### Stage 3 — Build the evidence/source packet

For each major design choice, record:

- source or Brain record;
- evidence type;
- what it supports;
- what it does not establish;
- confidence;
- whether verification is still needed.

Do not dump the whole Brain into the course. Retrieve only what could materially improve the design.

### Stage 4 — Design the course arc

Sequence sessions so responsibility grows.

A common progression is:

1. orientation + baseline;
2. leader models the core process;
3. learners practice parts with high support;
4. learners integrate multiple parts;
5. supports begin fading;
6. learners handle fresh tasks;
7. learners practice helping another person;
8. authentic transfer / final performance + next-step plan.

This is a pattern, not a mandatory eight-week template.

### Stage 5 — Design every session

Each session should normally define:

- **formation outcome** — what kind of response/ownership is being cultivated;
- **skill outcome** — what the participant should be able to do;
- **knowledge/theology** — what they need to understand;
- **retrieval/connect** — recall prior learning;
- **model/demo** — make expert reasoning/practice visible;
- **guided practice** — participants attempt the work with prompts;
- **independent/paired practice** — participants carry more responsibility;
- **feedback/correction** — specific response to actual attempts;
- **response/obedience** — how learning becomes lived faith;
- **between-session practice** — real repetition outside class;
- **evidence/source keys** — where consequential content/design claims came from;
- **common failure modes** — what facilitators should watch for;
- **bridge forward** — how this session prepares for the next.

Avoid sessions that are mostly lecture when the stated outcome is a skill.

### Stage 6 — Design between-session transfer

Homework should be practice, not filler.

Prefer:

- short repeatable practices;
- real-life use;
- retrieval;
- reflection on attempts;
- one authentic application;
- preparation to explain/teach when appropriate.

Track burden. A theoretically strong curriculum that ordinary people cannot sustain is not strong in practice.

### Stage 7 — Build assessment around the actual capability

Use the smallest useful set of:

- baseline diagnostic;
- weekly formative checks;
- observation of practice;
- participant self-reflection;
- facilitator feedback;
- final authentic performance;
- fresh-task transfer;
- delayed retention/transfer check when feasible;
- next-generation performance when reproduction is claimed.

Do not make confidence, attendance, satisfaction, or content recall the sole evidence of capability.

### Stage 8 — Build reproduction deliberately when relevant

If the North Star requires a reproducible skill, specify:

- what participants may begin helping others do;
- what competence must be demonstrated first;
- what remains under supervision;
- how teach-back is observed;
- how errors are corrected;
- what evidence counts as the next person becoming capable.

### Stage 9 — Create the curriculum asset stack

Apply [the shared Southbrook document-build workflow](../../docs/southbrook-document-build-workflow.md) to every authored artifact, including native Google Docs and internal Brain documents. Read `southbrook-brand-artifact-stylist` and its observed header/text patterns before production. Preserve the requested format, source attribution, and status labels; complete appropriate layout and brand QA before saving or delivering.

Create only what the course needs, typically:

1. Course brief / one-page overview
2. Outcome + competency map
3. Course-at-a-glance
4. Full facilitator guide
5. Participant workbook/guide
6. Session handouts/tools
7. Between-session practice
8. Assessment/rubric
9. Source/evidence ledger
10. Facilitator preparation notes
11. Accessibility adaptations
12. Reproduction/teach-back guide when relevant
13. Post-course continuation plan

### Stage 10 — Run curriculum QA

The curriculum is not finished until it passes all of these:

#### Biblical/theological fidelity
- Scripture is handled in context.
- The course does not smuggle disputed interpretation in as settled fact.
- Doctrinal boundaries are explicit where needed.

#### Evidence fidelity
- Consequential claims are traceable.
- AI synthesis is not masquerading as primary evidence.
- Research is not overstated.

#### Learning design
- outcomes are observable;
- practice matches the outcome;
- feedback exists;
- responsibility increases;
- fresh transfer is tested.

#### Formation
- knowledge connects to obedience/life with Jesus rather than becoming a technique detached from discipleship.

#### Reproducibility
- ordinary participants can carry the core practice;
- leader dependence decreases where appropriate;
- teach-back is bounded and coachable.

#### Load
- the course is realistically teachable in the available time;
- homework is sustainable;
- leader preparation is manageable.

## Conditional guardrails for Bible interpretation curriculum

When the course teaches people to study/interpret Scripture, also require:

1. **Text before tools.** Participants should learn to observe the passage before outsourcing conclusions.
2. **Observation, interpretation, and application are distinguished.**
3. **Context matters.** Literary, historical, canonical, and genre context are introduced proportionately to the audience.
4. **Meaning precedes application.** Personal response should flow from responsible interpretation rather than replace it.
5. **Reasons are visible.** Learners should point to textual/contextual reasons for conclusions.
6. **Uncertainty is teachable.** Participants should know how to say, "I am not sure," identify the question, seek wise help, and revise.
7. **Resources are used responsibly.** Study Bibles, commentaries, dictionaries, pastors/teachers, and appropriate technology help readers test and deepen understanding rather than replace reading.
8. **AI is not an unaccountable Bible authority.** If AI tools are taught, include source checking, error awareness, and pastoral/theological boundaries.
9. **Fresh-passage transfer matters.** Course completion is not evidence of biblical independence.
10. **Independence does not mean isolation.** The aim is responsible personal engagement inside the life and teaching community of the church.

## Output

# Discipleship Curriculum — [Title]

## Course contract
- audience
- problem
- desired transformation
- final capability
- duration/cadence
- constraints

## Evidence/source foundation
- relevant Brain sources
- external/verified sources when used
- confidence/boundaries
- unresolved gaps

## Competency map
- knowledge
- skills
- discernment
- practices
- reproduction capabilities

## Course at a glance
- session
- outcome
- core practice
- responsibility level
- between-session practice
- assessment signal

## Full session plans
Complete week-by-week/session-by-session materials.

## Facilitator assets

## Participant assets

## Assessment + transfer plan

## Reproduction/continuation plan

## Curriculum QA

## What remains uncertain / requires human review

## Persistence

A curriculum draft is **PROPOSED**, not approved ministry practice.

Drafts belong in Agent Workspace / proposal space or the user-specified curriculum folder until leadership approval.

If the curriculum is piloted, store active materials and learning with the relevant pilot in:

`09 — EXPERIMENTS, PILOTS & LEARNING`

Do not silently promote the curriculum into approved Southbrook strategy or Living Synthesis merely because it has been written.

## Stop conditions

Stop when:

- the requested curriculum and required assets are complete;
- the evidence is sufficient for the design decision;
- the next step requires doctrinal/pastoral approval;
- a material evidence gap prevents responsible teaching of a consequential claim;
- the user asked only for an outline/architecture and not full production.

## Success test

A successful curriculum should let us answer:

1. What real capability should participants leave with?
2. What is the progression from dependence to ownership?
3. Where do participants practice, not merely listen?
4. Where do they receive correction?
5. How do we know the skill transfers to a fresh setting?
6. How does the course contribute to abiding, transformation, mission, disciple-making, or multiplication?
7. Can ordinary people carry and eventually reproduce what they received?
