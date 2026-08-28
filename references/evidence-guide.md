# Evidence and Provenance Guide

## Evidence states
Use exactly these states:

- `CODE_VERIFIED` - directly supported by source code/configuration/tests/runtime artifacts.
- `DOCUMENT_VERIFIED` - directly supported by trusted existing documentation/runbook/spec.
- `USER_CONFIRMED` - explicitly confirmed by a knowledgeable person.
- `INFERRED` - plausible synthesis not yet verified.
- `UNKNOWN` - insufficient evidence.
- `CONFLICT` - credible sources disagree.

## Authority rule
Only `CODE_VERIFIED`, `DOCUMENT_VERIFIED`, and `USER_CONFIRMED` knowledge may be written as authoritative fact.

`INFERRED` must be visibly qualified. `UNKNOWN` must stay visible when material. `CONFLICT` must never be silently resolved by choosing the most convenient source.

## Provenance granularity
Attach evidence to important claims, not every sentence. Prioritize provenance for:
- business trigger
- sequence/order
- status meaning/transition
- business rules
- dependency contracts
- retry/recovery behavior
- unusual design decisions

Useful provenance examples:
- `CODE_VERIFIED - OutwardJobConfig#createJob`
- `CODE_VERIFIED - PostingClient#post`
- `DOCUMENT_VERIFIED - OPS_RUNBOOK.md / Recovery`
- `USER_CONFIRMED - Outward SME, 2026-08-28`

## Evidence notes
Keep evidence notes concise and separate from narrative when possible. The human-facing explanation should remain readable.

## Conflict handling
When evidence conflicts:
1. preserve both claims
2. identify likely ownership/freshness differences
3. inspect additional evidence
4. interview a domain expert if needed
5. record the resolution and why one source was superseded

Never rewrite history by deleting the existence of a meaningful conflict from the investigation log.
