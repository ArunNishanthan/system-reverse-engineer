# Human-First Writing Guide

## Audience
Primary audience: a developer new to the system.
Secondary audience: AI agents navigating and maintaining the knowledge.

Write so the developer can understand the flow without opening source code. Structure the Markdown so an agent can locate the right page quickly.

## Narrative rule
Explain behavior in connected prose. Use bullets and tables for compact supporting facts, not as the primary description of a process.

Bad:
- Controller: X
- Service: Y
- Repository: Z
- Status: READY

Better:
“Once the file is accepted, Outward creates the processing records and moves them into READY. READY is the handoff point to posting; the posting job selects only records in this state...”

## Developer-centric does not mean code-heavy
Prioritize:
- why the flow exists
- what triggers it
- sequence and branches
- status meaning
- dependency handoffs
- failure/recovery
- where a developer should start when changing behavior

Use implementation names as evidence anchors.

A compact implementation map is useful:

| Responsibility | Implementation entry point | Why it matters |
|---|---|---|
| Starts posting | `PostingJobConfig` | Defines job/step ordering |
| Calls posting dependency | `PostingClient` | Integration boundary |

Do not inventory every class, table, endpoint, or job unless it materially helps understanding.

## Flow continuity
Every major flow page should make clear:
- what happens before it
- why this flow starts
- what marks completion
- what happens next

Avoid isolated pages that strand the reader.

## Code snippets
Use only when code itself expresses an unusual algorithm, workaround, protocol detail, or rule that prose cannot explain clearly. Prefer names and source references over copied code.

## Unknowns
Do not smooth over missing knowledge. State material unknowns directly and link them to the checkpoint/interview queue where appropriate.

## Reading journey
A module should feel like a short technical book:
`Overview -> Journey -> Individual flows -> Status lifecycle -> Business rules/decisions -> Failure/recovery -> Change guidance`
