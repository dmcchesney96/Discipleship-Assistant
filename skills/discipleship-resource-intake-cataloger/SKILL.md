---
name: discipleship-resource-intake-cataloger
description: Inventory, triage, deduplicate, and index actual ministry teaching resources (handouts, worksheets, assignments, exercises, facilitation guides, videos, and curricula) for later usefulness review. Distinct from research-source verification and practice-family extraction.
metadata:
  short-description: Catalog practical equipping materials without treating them as research findings
---

# Discipleship Resource Intake & Cataloger

## Purpose
Answer: **What materials do we actually have, what is each meant to help someone do, and which items merit hands-on review?**

Work on *usable artifacts*, not claims about a ministry's effectiveness. A worksheet can be a useful candidate without scientific outcome evidence; an attractive PDF is not proof of spiritual formation.

## Natural trigger
Use when a user adds or points to a folder/collection of assignments, leader scripts, lesson plans, activity sheets, coaching questions, downloadable workbooks, discussion cards, or training resources and wants these organized, inventoried, or triaged for equipping value. For a broad external *research* corpus, use `discipleship-research-source-ingestor`; for descriptions of what a ministry does, use `discipleship-practice-intelligence-builder`.

## Inputs
User-bounded file/folder/link set; existing Discipleship Brain context/index for deduplication; target equipping problem, if supplied; source owner/organization; permission/access information.

## Procedure
1. **Hold the boundary.** Enumerate only the requested collection. Start from available metadata and embedded table of contents; inspect deeply only high-potential items. Do not pretend to have reviewed inaccessible files.
2. **Catalog at useful granularity.** A course PDF may contain twelve individually reusable exercises. Keep one parent source record and child item IDs for substantial exercises; do not create a new record for every paragraph/question.
3. **Capture source identity and traceability:** stable ID, exact link/file ID, title, creator/ministry, date/edition, file type, relevant page/section/timecode, language, intended audience, source family, original vs derived status, current location, access/privacy classification.
4. **Record rights separately:** known explicit license and permitted uses; unknown rights => `PERMISSION UNKNOWN`; internal access is not republication permission. Never infer that free-to-download means free-to-edit or redistribute.
5. **Extract the observable teaching object:** stated learning outcome, instructions, activity format, duration, required leader competence, audience, materials, reflection/practice/coaching steps, expected real-life action, reproducibility cue if present. Distinguish `SOURCE STATES` from `ANALYST INFERENCE`.
6. **Triage usefulness:** `DEEP REVIEW`, `REFERENCE / INDEX ONLY`, `NEEDS ACCESS / DETAILS`, `DUPLICATE`, `OUT OF SCOPE`. Triage priority is not a theological endorsement or effectiveness rating.
7. **Deduplicate carefully:** exact duplicates, alternate formats, successive editions, overlapping exercises, and summaries of a source are different relationships. Link rather than delete; do not count formats or chapters as independent evidence.
8. **Flag stop issues:** theological/safeguarding concerns, identifiable pastoral or minor data, unknown provenance, inaccessible content, licensing uncertainty. Do not copy confidential content into GitHub.
9. **Pass prioritized original items to `discipleship-resource-evaluator`** only when evaluation is requested. Indexing alone does not authorize adaptation, publication, filing changes, or pilot launch.

## Required output: Resource Intake Manifest
- Scope and access coverage (seen/unseen; number of sources/items)
- Parent sources and child item IDs with exact locators
- Intended audience / target capability
- Asset type, version, duplicates, related Practice Cards if known
- Rights status (verified, restrictions, unknown)
- Triage disposition and reason
- Important gaps and next evaluation candidates
- Actual Drive action status: `PROPOSED`, `WRITTEN + VERIFIED`, `NO WRITE`, or `BLOCKED`.

## Storage boundary
Original external materials stay linked to their existing canonical original-source locations (for example, `02 — EXTERNAL EVIDENCE LIBRARY / 07 Practitioner Books, Training & Tools` or other verified source folder). Derived resource records belong in the Resource & Equipping Intelligence area **only after the live Drive destination is verified/created with authorization**; until then, hold proposals in the verified Agent Workspace or return an in-chat manifest. Never assert a proposed folder exists.

## Success / stop
The user can find the exact exercise again, tell what it aims to do, see rights and version, and choose the next review targets. Stop after a complete bounded catalog; do not auto-run a research cycle.
