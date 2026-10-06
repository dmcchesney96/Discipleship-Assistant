---
name: southbrook-sermon-notes-artifact-builder
description: Convert a Southbrook sermon manuscript, outline, or preaching notes into the public-facing weekly Message Notes artifact used on the Southbrook Church website. Preserve the preacher's sequence and theology, follow the recurring Southbrook Message Notes structure, distinguish Message Notes from Study Questions, and route polished output through the Southbrook brand/artifact layer.
metadata:
  short-description: Build Southbrook weekly sermon Message Notes
---

# Southbrook Sermon Notes Artifact Builder

## Purpose

Create the public-facing weekly **Message Notes** artifact that accompanies a Southbrook sermon.

This skill owns the **content architecture and sermon-to-notes transformation**. It does not own sermon writing, theological revision, or visual-brand policy.

Use the public Southbrook sermon notes pattern documented in `references/public-message-notes-pattern.md` and the blank production scaffold in `templates/message-notes-template.md`.

## Trigger

Use when Dan asks to:

- make sermon notes, message notes, a sermon outline handout, or the weekly downloadable sermon notes;
- turn a manuscript into the same kind of notes people download from the Southbrook website;
- create or revise a Southbrook public sermon outline artifact;
- preserve Southbrook's established sermon-notes format from a preacher's manuscript.

Do not use this skill for:

- small-group study questions;
- student leader discussion guides;
- preacher-only manuscripts;
- sermon research;
- sermon slide decks;
- general sermon summarization with no public handout intent.

Southbrook's website treats **Message Notes** and **Study Questions** as separate artifacts. Do not merge them unless the user explicitly requests a combined resource.

## Source priority

When building a specific week's Message Notes, use sources in this order:

1. the preacher's current manuscript / final outline / explicit current instruction;
2. any current series-specific title, passage, date, artwork, or formatting direction;
3. the established Southbrook Message Notes pattern in this skill;
4. the `southbrook-brand-artifact-stylist` for general Southbrook visual identity;
5. older sermon notes as precedent only.

Never replace the preacher's actual argument with a cleaner argument of your own.

## Core transformation rule

Message Notes should let a person **track the sermon faithfully without reading the whole manuscript**.

Preserve:

- sermon sequence;
- main headings / movements;
- key definitions;
- main assertions;
- important contrasts;
- Scripture references;
- Scripture quotations the preacher actually depends on;
- final application / response movement.

Compress:

- stories and illustrations unless essential to the outline;
- repeated transitions;
- manuscript prose that only supports oral delivery;
- extended explanation that the speaker will supply verbally.

Do not add:

- new theological claims;
- extra application not in the sermon;
- study questions unless requested;
- artificial fill-in-the-blank wording merely to make the handout interactive.

## Recurring Southbrook Message Notes architecture

### 1. Header block

Use this order unless the series requires a clearly established variant:

`SERIES | SERMON TITLE`

`Primary Scripture passage`

`Speaker | Date`

Examples from 2026 public notes include:

- `THINK BIBLICALLY: RESPECTABLE SINS | GRUDGES`
- `THINK BIBLICALLY: RESPECTABLE SINS | GREED`
- `Revival | MARKS OF A SPIRITUAL LEADER`

Series-specific capitalization may vary. Preserve the current series language rather than mechanically forcing one case style.

### 2. Optional framing statement

If the sermon/series uses a repeated framing sentence, place it early.

Examples in the sampled notes include a one-sentence definition of the series or central concept.

Do not invent a series definition if one is absent.

### 3. Major sermon movements

Use concise section headings that mirror the preacher's argument.

Observed patterns include:

- conceptual headings: `Initial Thoughts about Greed`;
- interpretive headings: `Thinking Biblically about Gossip`;
- progression headings: `The Downward Spiral of Anger`;
- response headings: `Releasing a Grudge`, `Taking Personal Inventory`, `Putting a Stop to Gossip`;
- numbered teaching points in expositional series.

A good notes artifact normally makes the sermon movement obvious at a glance.

### 4. Main points

Use bullets or numbered points according to the sermon itself.

Southbrook examples regularly use complete, memorable statements rather than isolated keywords.

Examples of point types:

- definition;
- theological assertion;
- contrast;
- diagnostic statement;
- action / response;
- personal inventory question.

Do not force every sermon into exactly three points.

### 5. Scripture attachment

Keep Scripture adjacent to the point it supports.

For each passage, choose one of two treatments:

- **reference only** when the passage is supporting material and the speaker will read/explain it;
- **reference + quoted text** when the passage is central to the argument or the existing notes include the text.

Do not duplicate a passage citation and full text unnecessarily.

Preserve the translation named in the manuscript. If no translation is supplied, do not guess.

### 6. Final response / application

When the sermon contains a clear response movement, preserve it near the end.

Observed Southbrook forms include:

- personal-inventory questions;
- action bullets;
- concise response statements;
- a final sequence of practical steps.

Keep this faithful to the sermon rather than turning it into a separate discussion guide.

## Message Notes vs. Study Questions

**Message Notes** = track the sermon.

**Study Questions** = process/discuss the sermon afterward.

When the site publishes both, they are separate downloads.

If the request is ambiguous, default to Message Notes only when the input is a sermon manuscript and the user asks for the weekly outline/notes.

## Fidelity rules

- Do not reorder the sermon simply because another structure is aesthetically cleaner.
- Do not flatten biblical exposition into generic life principles.
- Do not remove hard or specific biblical language solely for brevity.
- Do not add citations or verses not present in the source unless the user explicitly asks for editorial help.
- Preserve meaningful repeated words or phrases when they carry the sermon argument.
- Correct obvious typographical noise only when meaning is unambiguous; do not silently rewrite disputed wording.

## Length and density

The public examples are compact but content-rich.

Default production target:

- usually a short multi-page handout rather than a one-page summary;
- enough Scripture and point detail to follow the message;
- not a transcript;
- not a sparse fill-in sheet.

Let the sermon determine length. Do not cut Scripture or major points merely to hit a fixed page count.

## Visual production

After content architecture is approved or sufficiently clear:

`southbrook-sermon-notes-artifact-builder → southbrook-brand-artifact-stylist → artifact-specific production skill`

For a DOCX/PDF handout:

- use the Southbrook brand stylist's verified visual rules;
- preserve series-specific visual identity when current artwork/style is available;
- do not overwrite a series-specific design with generic cyan merely for consistency;
- keep the public handout clean, print-friendly, and easy to scan;
- render and inspect before final delivery.

### Series-specific visual rule

The stable sermon-note **content grammar** is stronger than any single series' visual treatment.

Therefore:

- keep the header/outline/Scripture/response architecture stable;
- allow series title treatment, artwork, accent color, and typography emphasis to vary;
- use current series assets when available;
- fall back to the general Southbrook brand system when no series-specific design is supplied.

## Production workflow

### Step 1 — identify the sermon contract

Extract:

- series;
- sermon title;
- primary passage;
- speaker;
- date;
- sermon big idea / framing sentence if explicitly present;
- major movements;
- main points;
- Scripture attached to each point;
- closing response.

### Step 2 — map the manuscript

Create a source-faithful outline before styling.

Do not start with a generic template and force the sermon into it.

### Step 3 — compress for public tracking

Convert oral prose into concise notes while preserving meaning.

### Step 4 — verify Scripture placement

Check that each Scripture reference or quote is attached to the correct sermon movement.

### Step 5 — compare with Southbrook pattern

Check against `references/public-message-notes-pattern.md`.

### Step 6 — brand and produce

Apply current series identity if available, then Southbrook brand rules.

### Step 7 — QA

Render the final artifact and confirm:

- no missing sermon movement;
- no added theological material;
- title/passage/speaker/date are correct;
- Scripture is readable and not detached from its point;
- headings are scannable;
- notes are neither transcript-heavy nor too skeletal;
- Message Notes have not accidentally become Study Questions;
- no clipped text, broken glyphs, or awkward page breaks.

## Quality test

Before finishing, ask:

1. Could someone who missed one sentence in the sermon find the speaker's current movement quickly?
2. Would the preacher recognize this as *their* argument rather than an AI summary?
3. Are the central Scriptures visible at the points where they matter?
4. Is the handout complete enough to be useful later in the week?
5. Is the application faithful to what was preached?
6. Does the artifact look like Southbrook without becoming over-designed?

## Stop conditions

Stop when:

- the sermon can be followed accurately from the notes;
- the artifact preserves Southbrook's recurring Message Notes grammar;
- the next edit would change the preacher's content rather than improve the handout;
- missing manuscript information requires human clarification.