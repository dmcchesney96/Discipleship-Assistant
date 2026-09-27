---
name: decision-action-extractor
description: Extract confirmed decisions, proposed decisions, action items, owners, dates, dependencies, and open questions from meetings, notes, documents, or chats without inventing commitments.
---

# Decision & Action Extractor

## Workflow

1. Identify source/date/audience.
2. Separate:
   - DECIDED
   - PROPOSED / TENTATIVE
   - ACTION
   - OWNER
   - DEADLINE / REVIEW DATE
   - DEPENDENCY
   - OPEN QUESTION
3. Preserve exact wording when ambiguity affects responsibility or scope.
4. Never convert a recommendation, silence, draft, or discussion into approval.
5. If owner/date is absent, leave unknown rather than assigning one.
6. Note decisions that supersede earlier direction.

## Output

### Decisions
| Decision | Status | Decision-maker | Date | Source |

### Actions
| Action | Owner | Due | Dependency | Status |

### Open questions

### Superseded/changed direction

Use `institutional-memory-writer` only when rationale/history is worth preserving beyond task tracking.
