# Maintenance Guide

## Goal
Update maintained knowledge after implementation changes without re-running full reverse engineering unnecessarily.

## Start from change impact
For a code/configuration change:
1. identify changed components
2. map them to documented flows/statuses/integrations/decisions through links and implementation references
3. read only affected knowledge pages
4. investigate whether behavior or only implementation detail changed

Do not automatically rewrite business documentation because a class changed.

## Change classifications

### Technical-only change
Behavior and business meaning remain the same. Update implementation references only when useful.

### Behavioral change
Sequence, business rule, status transition, integration contract, failure behavior, or developer guidance changed. Re-run the relevant flow investigation and quality gate.

### Knowledge conflict
New code contradicts maintained knowledge. Mark `CONFLICT`, investigate, and interview an owner if intent is unclear.

### New scope
The change introduces a substantial new subsystem or flow. Return to scope/journey checkpoints before expanding documentation.

## Incremental update flow
`Change -> affected knowledge -> investigate -> verify/interview -> update pages -> update log -> quality gate`

## Log
Maintain `log.md` as knowledge history, not a duplicate Git history. Record meaningful knowledge events such as:
- flow documented or materially revised
- status meaning confirmed
- dependency boundary added
- conflict resolved
- design rationale captured

Keep entries concise.

## Staleness
When existing knowledge appears outdated but cannot be verified, mark it explicitly rather than silently retaining it as fact.
