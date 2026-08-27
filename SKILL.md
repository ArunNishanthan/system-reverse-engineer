---
name: system-reverse-engineer
description: Use when reverse-engineering, documenting, handing over, onboarding to, or maintaining a large existing software system. Creates scoped, evidence-backed, LLM-ready Markdown that reads like a coherent technical book, combining source-code analysis with domain-expert interviews. Focuses on business flows, entry points, architecture, status lifecycles, important decisions, developer change guidance, Mermaid visualizations, checkpoints, and a lightweight local knowledge graph for agent navigation.
---

# System Reverse Engineer

## Goal

Create a durable **system knowledge pack** from:

`source code + existing artifacts + domain-expert interviews -> verified, narrative Markdown + Mermaid + lightweight knowledge graph`

The output must work directly for humans and LLM tools such as CLI coding agents and notebook/RAG experiences. Do not require or initialize Docusaurus, docmd, MkDocs, or another documentation platform. A presentation layer may be added later without repeating reverse engineering.

The documentation must feel like a **technical book**, not a folder of disconnected reference pages.

## References

Read only when relevant:

- Spring Boot/Spring Batch and framework-aware discovery: `references/framework-discovery.md`
- Knowledge graph creation/maintenance and agent navigation: `references/knowledge-model.md`

## Non-Negotiable Rules

1. **Narrative before inventory.** Explain how the system works before cataloging technical artifacts.
2. **Book-like continuity.** Every module/flow must have a clear place in the reading journey and explain what comes before/after it.
3. **Mermaid only for diagrams. Never create ASCII/text-art diagrams.** Use ordinary text/bullets only when not representing a diagram.
4. **Visual-first for complex behavior.** Start important flows/status lifecycles/architecture explanations with a useful Mermaid overview, then explain it.
5. Establish `System -> Module -> Capability -> Flow -> Subflow` before deep investigation. Never assume a requested module is the whole system.
6. Obtain explicit scope approval. Anything not approved is `OUT_OF_SCOPE`.
7. Never investigate out-of-scope internals. Document only verified boundaries from the in-scope side.
8. Never publish inference as fact. Verify, interview, or mark uncertainty.
9. Interview the domain expert whenever code cannot establish business meaning, ordering, rationale, or operational truth.
10. Focus on understanding, not code dumping. Source code is evidence and an implementation map, not the documentation itself.
11. Statuses are first-class knowledge and must be traced from real reads/writes/conditions, not inferred from enums.
12. Checkpoint continuously so large investigations survive context/session boundaries.
13. Markdown is canonical. The local graph and agent index navigate it; they do not duplicate or replace it.
14. Use sub-agents only for bounded approved investigations. The coordinator owns canonical documentation, graph and checkpoints.

## Stage 0 - Initialize or Resume the Knowledge Pack

Use `<repo-root>/documentation/` unless the repository already has an approved documentation location.

If documentation exists, first read `START_HERE.md`, `AGENT_INDEX.md`, the current checkpoint, and only the relevant module pages. Resume rather than rediscovering the repository.

If no documentation exists, initialize a minimal structure as needed:

```text
documentation/
  START_HERE.md
  SYSTEM_OVERVIEW.md
  GLOSSARY.md
  modules/
  knowledge/
    graph.yaml
  checkpoints/
    current.md
  AGENT_INDEX.md
```

Do not create empty module/reference files before their content is understood.

## Stage 1 - Frame and Approve the System

Establish the conceptual hierarchy:

`SYSTEM -> MODULE -> CAPABILITY -> FLOW -> SUBFLOW -> PROCESSING STEP -> TECHNICAL COMPONENT`

This hierarchy is conceptual; do not render it as ASCII art. When a visual is useful, use Mermaid.

Ask only what is needed to determine:

- system/product purpose
- major known modules/business areas
- requested module/capability scope
- explicit exclusions/deferred areas

Show the proposed scope clearly and obtain user approval before deep investigation. A request such as `Document Outward Clearing` means Outward Clearing is the current scope within a larger system unless explicitly confirmed otherwise.

Persist the approved framing immediately.

## Stage 2 - Map and Approve the Selected Module

Explore only enough in-scope code/artifacts to identify candidate capabilities and business flows. Do not assume Java packages, microservices, jobs, controllers, or repositories are business flows.

Show the candidate module decomposition and uncertainties. Use Mermaid when visualization improves understanding. Obtain user approval/correction before deep reverse engineering.

A large module must not be represented as one artificial flow merely because the user initially named only that module.

## Stage 3 - Discover the Reading Journey

Before writing detailed pages, determine the **narrative order** for the approved scope.

For a module, establish:

1. What is this module and why does it exist?
2. Where does processing enter the module?
3. What are the major flows and in what business/processing order should a newcomer learn them?
4. Where do flows branch or rejoin?
5. What statuses are important to understanding progression?
6. What important external boundaries exist?
7. Which business/technical decisions are essential context?

Persist this order and use it to organize pages. File creation order does not determine reading order.

`START_HERE.md` must provide the top-level reading path. Module overview pages must provide the module reading path. Flow pages must link conceptually to previous/next flows where meaningful.

## Stage 4 - Reverse Engineer One Flow at a Time

When applicable, read `references/framework-discovery.md` before framework-specific tracing.

For each approved flow/subflow:

1. Determine its purpose and relationship to the previous/next processing stage.
2. Find the real entry point/trigger.
3. Trace the end-to-end processing path.
4. Identify the architecture/components necessary to understand the flow.
5. Trace important business rules and variants.
6. Trace important status changes from actual implementation evidence.
7. Identify important integrations/data only when needed to understand the flow.
8. Identify important implementation decisions/rationale.
9. Identify developer entry points for changing the flow.
10. Interview the user for missing business/rationale/operational knowledge.
11. Reconcile conflicts.
12. Write/update the canonical flow page.
13. Update affected graph/index/checkpoint.

If the flow becomes too large, split it into subflows and create an overview Mermaid diagram that links the conceptual stages together. Do not force everything into one giant diagram or page.

## Flow Page Contract

Every important flow should answer, where applicable:

### 1. Purpose
What business/process problem does this flow solve?

### 2. Position in the journey
What happens before this flow? What causes it to begin? What normally happens after it?

### 3. Visual overview
Use a Mermaid flowchart or sequence diagram showing the meaningful processing stages. Never use ASCII diagrams.

### 4. Entry point
Explain the business trigger and technical entry point. Point to the relevant job/controller/listener/service/class/symbol without dumping its source code.

### 5. Processing walkthrough
Explain the flow in the same order it executes or occurs. Keep the narrative connected to the visual overview.

### 6. Business rules and variants
Capture rules a future developer must understand, especially knowledge that is not obvious from code.

### 7. Status progression
Explain important status transitions involved in the flow and link to the module status model when appropriate.

### 8. Architecture involved
Explain only the services/components/integrations/data stores needed to understand this flow.

### 9. Important implementation decisions
Capture why unusual or non-obvious behavior exists. Preserve user-confirmed rationale.

### 10. Developer change guide
Explain where a developer should start when modifying this flow: important entry points, components, statuses/rules/integrations to consider, and relevant verification/testing where known.

### 11. Failure/recovery notes
Include when materially important and verified/confirmed.

### 12. Continue reading
Point to the logical next flow/subflow and useful related concepts. Do not leave the reader stranded.

Do not mechanically add empty sections. Mark material missing knowledge `UNKNOWN` and interview when it matters.

## Module Book Contract

A documented module should normally read in this order:

1. **Overview** - purpose, boundary, terminology, reading guide
2. **Architecture** - only enough system structure to understand the module
3. **End-to-end journey** - one Mermaid overview connecting the major flows
4. **Flows** - detailed pages in narrative/process order
5. **Status lifecycle** - cross-flow state progression
6. **Business rules / variants** - cross-cutting rules not best explained in one flow
7. **Important decisions** - business and implementation rationale worth preserving
8. **Developer change guide** - where to start for common modifications
9. **Further technical references** - only when they add value

Do not organize the primary reading path around `APIs`, `Tables`, `Jobs`, `Repositories`, or `Classes`. Those are supporting implementation concepts, not the story of the system.

## Status Model

Statuses are especially important.

For each important status establish:

- business meaning
- owning entity/process
- who/what sets it
- condition/event that sets it
- who/what consumes/checks it
- valid next statuses when verified
- important side effects
- why a record may remain/stall there when known
- relevant flow(s)
- implementation evidence

Trace actual writes, reads, predicates, repository queries, jobs/listeners/controllers and tests. Never generate a lifecycle from an enum alone.

Use a Mermaid `stateDiagram-v2` when a lifecycle is useful. Accompany it with concise explanation/table because the diagram alone is not sufficient.

## Architecture and Visual Rules

Use Mermaid for all actual diagrams, including:

- system/module architecture
- end-to-end journeys
- flowcharts
- sequence diagrams
- state transitions
- integration relationships
- ER/data relationships when genuinely needed

Never use ASCII boxes, arrows, trees, timelines, or text-art diagrams.

A diagram must answer a clear question. Split large diagrams into overview + drill-down diagrams. Do not visualize every class or table. Visualize the business/processing model first and technical implementation second.

## Code and Technical Detail Rules

Developer-centric does **not** mean code-heavy.

Prefer an implementation map such as:

| Responsibility | Implementation entry point | Why it matters |
|---|---|---|
| Job orchestration | `OutwardIngestionJobConfig` | Starts and coordinates ingestion |
| Validation | `ValidationProcessor` | Applies the main ingestion rules |

Use code snippets only when a small piece of code is essential to explain an unusual algorithm, workaround, rule, or implementation decision. Do not copy ordinary configuration/service/repository code into documentation.

Document jobs, APIs, tables, integrations and schemas when they materially help explain a flow, status, decision, change path, or boundary. Avoid exhaustive inventories unless the user explicitly requests them.

## Interview Protocol

Interviewing is a primary knowledge source, not a fallback.

Ask when code cannot establish:

- business meaning/terminology
- why processing is ordered a certain way
- business rules/variants
- important status meaning
- why a technical decision exists
- manual/operator behavior
- recovery/reprocessing expectations
- downstream/upstream expectations
- important testing/verification knowledge

Prefer one focused question at a time and explain what evidence/gap prompted it when useful.

Record answers as `USER_CONFIRMED`. If the answer describes current technical behavior, cross-check against implementation where practical. If evidence conflicts, preserve a `CONFLICT` and clarify rather than silently choosing.

## Evidence and Scope

Evidence states:

- `CODE_VERIFIED`
- `DOCUMENT_VERIFIED`
- `USER_CONFIRMED`
- `INFERRED`
- `UNKNOWN`
- `CONFLICT`

Only verified/confirmed knowledge may be presented as established fact. `INFERRED` is temporary discovery knowledge, not authoritative prose. Keep material `UNKNOWN` and `CONFLICT` visible.

Coverage states:

- `DOCUMENTED`
- `IN_PROGRESS`
- `TODO`
- `OUT_OF_SCOPE`

Anything not explicitly approved is `OUT_OF_SCOPE`, not `UNKNOWN`.

## Lightweight Knowledge Graph

Read `references/knowledge-model.md` before creating/updating the graph.

The graph exists primarily so CLI/LLM agents can cheaply locate relevant knowledge and maintain affected documentation later. It is not intended as the primary human interface.

Keep it small. Prefer semantic concepts such as:

- `SYSTEM`
- `MODULE`
- `CAPABILITY`
- `FLOW`
- `STATUS`
- `INTEGRATION`
- `DECISION`
- `COMPONENT` only for important technical entry points

Do not model every table, entity, job, job step, API, class, method or test by default. Add another node type only when repeated use proves it materially improves navigation.

The graph should primarily answer:

- Which module/flow should an agent read?
- What flow comes before/after this flow?
- Which important statuses belong to this flow/module?
- Which important integration/decision/component is associated with it?
- Which canonical Markdown page contains the explanation?

Keep rich explanations in Markdown. Graph relationships require evidence just like prose.

## AGENT_INDEX.md

Keep this file short. It should tell an agent:

- what system this is
- where to start reading
- approved scope/coverage
- module overview paths
- graph location
- current checkpoint location
- how to interpret evidence/unknown/out-of-scope markers

Agents should follow `AGENT_INDEX -> graph/reading path -> relevant Markdown -> source code only when needed` rather than loading the entire repository.

## Checkpoint / Resume Protocol

Persist `documentation/checkpoints/current.md` (or an approved equivalent) containing:

- approved system/module scope
- approved module decomposition
- approved reading/flow order
- current bounded investigation
- completed/in-progress/TODO areas
- open questions
- material unknowns/conflicts
- important user confirmations not yet fully incorporated
- next recommended action

Checkpoint after approvals, substantial traces, important user answers, completed flows/subflows, and before switching bounded areas or ending a session.

## Sub-Agent Coordination

Use sub-agents when supported for independent bounded investigations after hierarchy/scope/decomposition are approved.

Good tasks include tracing one child flow, locating status writes/reads for a known status, identifying a flow's entry point, or investigating a specific integration boundary.

Every sub-agent receives exact scope, question, known context, evidence requirements and a no-guessing rule. Sub-agents return findings; the coordinator reconciles and writes canonical Markdown/graph/checkpoint.

Do not let separate agents independently decide the system hierarchy, business flow ordering, or canonical documentation structure.

## Maintenance Mode

When code changes later:

1. Read `AGENT_INDEX.md`, graph, checkpoint and affected canonical docs.
2. Inspect the actual implementation change.
3. Determine which documented flows/statuses/decisions are affected.
4. Update only affected Markdown and Mermaid diagrams.
5. Update the lightweight graph if semantic relationships changed.
6. Preserve unrelated `USER_CONFIRMED` rationale.
7. Mark conflicts when new code contradicts documented rationale rather than silently rewriting history.
8. Update checkpoint/coverage.

## Completion Gate

For the approved scope, do not claim completion until:

- system/module framing is approved
- module capability/flow decomposition is approved
- reading/processing journey is coherent
- `START_HERE.md` leads readers into the documented system
- module overview explains where to start and how flows connect
- important flows have entry points and Mermaid visual overviews
- important status lifecycles are documented from evidence
- important business rules and decisions are captured
- developer change guidance exists where useful
- pages connect logically rather than feeling isolated
- material unknowns/conflicts are visible
- scope boundaries are respected
- lightweight graph/index point to canonical Markdown
- checkpoint is current

The success test is:

> Can a new developer start from `START_HERE.md`, progressively understand the system like reading a technical book, visually follow a module's major flows, understand important statuses and decisions, find the implementation entry point when needed, and use an LLM to ask grounded questions over the same knowledge?

## Common Failure Modes

| Failure | Correction |
|---|---|
| Documentation feels "here and there" | Rebuild the reading journey and previous/next relationships |
| Primary structure is jobs/APIs/tables | Reorganize around business/module flows |
| Developer-centric becomes code snippets | Replace with explanation + implementation entry-point map |
| Requested module becomes whole system | Frame and approve system first |
| Module becomes one giant flow | Discover and approve capabilities/flows |
| ASCII/text-art diagram appears | Replace it with Mermaid |
| Giant Mermaid diagram | Split overview from drill-down diagrams |
| Enum becomes state machine | Trace real status writes/reads/conditions |
| Agent scans everything | Use scope + graph/index + bounded discovery |
| Graph becomes another documentation corpus | Keep explanations in canonical Markdown |
| Graph models every technical artifact | Keep only semantic navigation concepts |
| Business/rationale knowledge is guessed | Interview the user |
| Missing knowledge is hidden | Surface `UNKNOWN`/`CONFLICT` |
| Session starts discovery again | Resume from checkpoint |
