---
name: system-reverse-engineer
description: Use when documenting, onboarding to, reverse-engineering, or maintaining understanding of an existing software system where behavior spans multiple services, jobs, APIs, databases, statuses, integrations, files, events, or undocumented business workflows.
---

# System Reverse Engineer

## Overview

Build and maintain an evidence-backed system knowledge layer beside an existing codebase. Combine source-code investigation, existing artifacts, and structured interviews with domain experts. Never turn an inference into a fact.

The knowledge model is optimized for agents; generated Docusaurus documentation is optimized for humans. Source code remains the source of truth for implementation behavior, while user-confirmed knowledge captures business meaning and rationale that code cannot establish.

## Non-Negotiable Rules

1. **Scope before discovery.** Do not deeply inspect or document a capability until the user explicitly puts it in scope.
2. **Everything not included is out of scope.** Crossing an out-of-scope boundary is allowed only far enough to record the verified dependency. Do not reverse-engineer the other side.
3. **No hallucinated facts.** Every factual knowledge item must have evidence or explicit user confirmation.
4. **Inference is temporary.** `INFERRED` information must be verified from evidence or confirmed by a user before appearing as authoritative documentation.
5. **Ask rather than guess.** Interview the user when business meaning, ordering, rationale, operational behavior, variants, failure handling, or scope cannot be established.
6. **Checkpoint continuously.** Persist meaningful discoveries before moving to another substantial investigation and before context pressure becomes risky.
7. **Canonical knowledge has one writer.** Sub-agents investigate and return evidence; the coordinator reconciles and writes canonical knowledge.
8. **Preserve human knowledge.** Never silently overwrite `USER_CONFIRMED` explanations or decisions.
9. **Progressive disclosure.** Split large flows into subflows. Do not create unreadable mega-diagrams or mega-pages.
10. **Documentation is living system knowledge.** When code changes, identify and update only affected knowledge and documentation.

## Startup Protocol

### 1. Detect documentation state

From the repository/workspace root, look for:

- `documentation/knowledge/index.yaml`
- `documentation/knowledge/scope.yaml`
- `documentation/checkpoints/resume.yaml`
- an existing Docusaurus site or other established documentation system

If the knowledge layer exists, read the index, scope, resume checkpoint, and only the detailed files relevant to the requested work.

If it does not exist, enter **INITIALIZE** mode.

### 2. Establish scope before deep exploration

If scope has not already been established for the requested work, ask the user what business capabilities/modules/flows they want documented. Ask one focused question at a time when clarification is needed.

Example:

> Which modules or business capabilities should I document? Anything you do not include will remain out of scope unless you later expand the scope.

Create/update `documentation/knowledge/scope.yaml` immediately after confirmation.

Coverage states are separate from evidence states:

- `DOCUMENTED` — sufficiently investigated and verified
- `IN_PROGRESS` — currently being investigated
- `TODO` — explicitly intended for later documentation
- `OUT_OF_SCOPE` — deliberately excluded

`UNKNOWN` is not a coverage state. It means there is an unresolved knowledge gap inside an in-scope area.

### 3. Initialize when needed

For a repository without the knowledge/documentation package, create this conceptual structure (adapt to existing project conventions rather than duplicating an established docs platform):

```text
documentation/
├── knowledge/
│   ├── index.yaml
│   ├── scope.yaml
│   ├── domains/
│   ├── flows/
│   ├── statuses/
│   ├── components/
│   ├── integrations/
│   ├── decisions/
│   └── evidence/
├── checkpoints/
│   └── resume.yaml
├── questions/
├── docs/
├── src/components/
└── [Docusaurus configuration]
```

Also create or amend a repository-level agent instruction file when appropriate so future agents are directed to read `documentation/knowledge/index.yaml` before architectural work and to maintain affected knowledge after changes. Do not overwrite existing agent instructions; integrate minimally.

Read `references/knowledge-model.md` for the canonical schemas and evidence rules. Read `references/docusaurus-visuals.md` before creating the human-facing documentation site or diagrams.

## Core Reverse-Engineering Loop

For each in-scope capability:

1. **Orient** — read the small knowledge index and existing confirmed knowledge.
2. **Map** — establish the business-level flow from existing evidence and user input before deep technical tracing.
3. **Decompose** — if a flow is too large to reason about safely, create child flows and investigate them independently.
4. **Investigate** — trace concrete implementation evidence: entry points, jobs, schedulers, controllers, consumers, services, persistence, statuses, files, events, integrations, configuration, and tests.
5. **Record evidence** — capture source path + symbol/line where practical, artifact reference, or user-confirmed statement.
6. **Find gaps** — explicitly list relationships or meanings that evidence does not establish.
7. **Interview** — ask the user targeted questions for the highest-value gaps. Prefer one question at a time. Do not ask questions that code/artifacts can answer reliably.
8. **Cross-check** — use new user knowledge to guide another code search. A user statement may explain intent; code establishes current implementation.
9. **Reconcile** — if sources disagree, mark `CONFLICT`; do not silently choose one.
10. **Checkpoint** — update canonical knowledge and resume state before switching to another substantial area.
11. **Render** — generate/update human documentation only from verified/confirmed knowledge; visibly mark genuine unknowns.
12. **Validate** — check graph references, evidence links, scope boundaries, documentation links, and consistency between knowledge and rendered views.

Repeat until the requested scope reaches the agreed coverage level.

## Interview Protocol

Interviewing domain experts is a first-class discovery mechanism.

Ask when code cannot establish:

- business purpose or terminology
- why a design or rule exists
- ordering between independently triggered processes
- operational timing that is not encoded reliably
- manual/operator steps
- status business meaning
- variants and branching rules
- exceptional or recovery procedures
- historical decisions and deliberate omissions
- ownership boundaries

Good question:

> I verified that `IngestionJob` writes `READY`, and `DebitJob` reads records after reconciliation. I cannot establish what gates Debit after ingestion. Is reconciliation the required business step between them, and what indicates it has completed?

Bad question:

> How does this system work?

Save useful answers as structured `USER_CONFIRMED` knowledge with the question/answer context and date when practical. Then attempt to locate implementation evidence where the answer describes current behavior.

If user knowledge conflicts with code, preserve both and create a `CONFLICT` requiring resolution.

## Evidence and Anti-Hallucination Policy

Use these evidence states:

- `CODE_VERIFIED` — directly supported by current source/config/tests
- `DOCUMENT_VERIFIED` — directly supported by an authoritative existing artifact
- `USER_CONFIRMED` — explicitly supplied/confirmed by a domain expert
- `INFERRED` — plausible relationship discovered by reasoning but not yet verified
- `UNKNOWN` — unresolved gap
- `CONFLICT` — credible sources disagree

Authoritative human documentation may state `CODE_VERIFIED`, `DOCUMENT_VERIFIED`, and `USER_CONFIRMED` knowledge as facts, with provenance available in the evidence view.

`INFERRED` must never silently become authoritative prose. Verify it, ask the user, or keep it in discovery notes.

`UNKNOWN` must be displayed honestly when it materially affects understanding.

`CONFLICT` must show the competing evidence and remain unresolved until investigated or confirmed.

Never invent:

- schedules
- status meanings
- transition rules
- retry/recovery behavior
- API semantics
- database relationships
- business rationale
- downstream behavior beyond the verified boundary

## Large Flows and Mandatory Checkpoints

Do not attempt to hold a large system in conversation context.

Split hierarchically:

```text
Domain
  -> Flow
      -> Subflow
          -> Component / status transition / integration
```

Create a child flow when a section has multiple independent stages, variants, triggers, or failure paths, or when its evidence cannot be reviewed coherently as one unit.

Checkpoint after:

- establishing or changing scope
- confirming a business flow or subflow
- completing a substantial code trace
- receiving important user answers
- resolving status transitions or variants
- resolving a conflict
- before delegating a new investigation wave
- before switching domains/subflows
- before generating a major documentation section
- whenever context pressure could lose material discoveries

`resume.yaml` should remain small and contain at least current scope, current investigation, completed/in-progress/unexplored areas, open questions, conflicts, and last checkpoint.

## Sub-Agent Coordination

Use sub-agents when the runtime supports them and investigations are genuinely independent. Otherwise run the same queue sequentially.

Good parallel investigations:

- separate microservices within an already established business boundary
- independent batch jobs
- API cataloguing versus status-write discovery
- database/table usage versus external integration discovery
- separate child flows whose parent relationship is already known

Do not delegate agents to independently invent the business ordering between components.

Each sub-agent receives:

- exact scope boundary
- question(s) to answer
- relevant known graph nodes
- allowed repository paths where practical
- required evidence format
- instruction to report unknowns and conflicts instead of guessing

Sub-agents return discovery reports; they do **not** directly mutate canonical knowledge unless the runtime provides an explicit safe merge protocol controlled by the coordinator.

The coordinator:

1. compares findings
2. detects conflicts
3. asks the user where business knowledge is needed
4. verifies important inferred links
5. updates canonical knowledge
6. checkpoints

## What to Discover

Within scope, model only what improves system understanding or maintenance:

### Business/domain
- capabilities and terminology
- end-to-end flows and child flows
- business rules and rationale
- variants (type, amount/size, country, channel, etc.)
- manual/operator steps

### Runtime/technical
- services and repositories
- APIs/controllers
- jobs, steps, readers/processors/writers
- schedulers/triggers
- events/topics/queues/listeners
- files and file interfaces
- external systems
- database tables/collections and meaningful relationships
- configuration that changes behavior

### State
Statuses are first-class knowledge. For each important status capture:

- owning entity
- business meaning
- producer(s)
- consumer(s)
- valid known previous/next states
- transition trigger
- conditions/variant applicability
- side effects
- failure/recovery path
- evidence

Never infer a complete state machine merely from an enum. Search writes, predicates, consumers, tests, database queries, and user knowledge.

### Operations
- processing timelines
- dependencies/gates
- monitoring signals when verifiable
- failure modes
- retry/restart/reprocessing/reconciliation behavior
- deliberate absence of retry or automation and why, when known

## Knowledge Graph Strategy

The knowledge graph is a lightweight navigational graph, not a giant dump of source code.

Keep `index.yaml` intentionally small. It should tell an agent where detailed knowledge lives and how major concepts connect. Normalize detailed records into domain/flow/status/component/integration files.

Agents should navigate:

```text
agent instructions -> knowledge/index.yaml -> relevant node file -> evidence -> source code
```

Humans should navigate:

```text
system -> domain -> flow -> subflow -> variant/status/component -> implementation/evidence
```

Do not duplicate the same fact across many canonical files. Render multiple human views from one normalized fact where practical.

## Human Documentation

Default target for a new documentation package: **Docusaurus + MDX + Mermaid**, because it combines Markdown portability with rich React-based interactive views. Respect an existing approved documentation platform if the repository already has one.

Human documentation must be:

- business-first, not repository-tree-first
- visually clear and attractive
- progressively drillable
- searchable and linkable
- usable without animations
- explicit about unknown/conflicting information
- traceable to evidence

Recommended top-level information architecture:

```text
Getting Started
Business Flows
Processing Components
Statuses & State Machines
Data
Integrations
Operations
Developer Reference
Documentation Coverage
```

For complex domains, provide multiple views over the same canonical knowledge:

- end-to-end business flow
- processing timeline
- variant comparison
- status/state explorer
- technical sequence
- dependency/service map
- failure/recovery explorer

Read `references/docusaurus-visuals.md` for visualization and color rules.

## Maintenance Mode

When documentation already exists and code changes:

1. read the knowledge index and affected nodes
2. inspect the actual code change/current implementation
3. identify impacted flows, statuses, components, integrations, decisions, and pages
4. update evidence-backed canonical knowledge
5. preserve unrelated knowledge
6. update only affected rendered documentation
7. validate references and links
8. checkpoint the new state

Never regenerate the whole knowledge base merely because one component changed.

If a code change appears to contradict `USER_CONFIRMED` rationale, do not erase the rationale. Record the conflict/change and ask whether the business rule itself changed.

## Scope Boundary Behavior

If an in-scope flow calls an out-of-scope module, document only the verified boundary:

```text
In-scope component -> interface/event/file/API -> OUT-OF-SCOPE capability
```

Do not inspect the out-of-scope capability's internals to explain what it does. Ask for scope expansion first.

This rule applies to sub-agents too.

## Completion Criteria

A requested documentation scope is complete only when:

- requested capabilities have explicit coverage states
- major business flows are mapped
- large flows are decomposed into understandable child flows
- important statuses/transitions and variants are represented
- technical components are linked to business flows
- unknowns and conflicts are explicit
- factual documentation is backed by evidence/confirmation
- out-of-scope boundaries were respected
- resume/checkpoint state is current
- generated documentation builds/validates where tooling permits
- links/graph references are structurally valid

Do not claim semantic completeness when unresolved `UNKNOWN` or `CONFLICT` items materially affect the flow. Report them.

## Common Failure Modes

| Failure | Correct behavior |
|---|---|
| Scan every repository immediately | Establish scope first |
| Assume class names reveal business flow | Treat as hypothesis; verify/interview |
| Document an enum as a state machine | Trace writes/reads/transitions/tests |
| Follow an excluded dependency deeply | Record boundary only |
| Generate docs before understanding flow | Build/checkpoint knowledge first |
| Let parallel agents edit canonical files | Coordinator merges evidence |
| Hide gaps to make diagrams look complete | Display unknowns |
| Giant Mermaid diagram | Progressive overview + child diagrams |
| Random decorative colors | Use semantic visual vocabulary |
| Rewrite hand-authored rationale | Preserve and reconcile |
| Re-scan everything after restart | Read index + resume checkpoint |
