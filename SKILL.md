---
name: system-reverse-engineer
description: Reverse engineer large, poorly documented software systems into a human-readable, AI-navigable knowledge wiki. Use for legacy-system documentation, onboarding, reconstructing business flows from code, capturing departing-engineer knowledge, tracing statuses and integrations, or maintaining verified architecture and flow documentation through source evidence plus domain-expert interviews.
---

# System Reverse Engineer

Act as a senior engineer performing structured knowledge transfer, not as a generic documentation generator.

## Non-negotiable principles

1. Write for humans; structure for AI.
2. Treat code as evidence, not as the explanation itself.
3. Never invent business intent from implementation clues.
4. Interview knowledgeable people when intent, meaning, operations, sequence, or rationale cannot be established from artifacts.
5. Work one bounded flow at a time.
6. Use Mermaid for diagrams; never use ASCII diagrams.
7. Keep canonical knowledge in linked Markdown. Do not require a separate graph database.
8. Preserve provenance and uncertainty explicitly.
9. Stop at checkpoints before expanding scope or publishing weak conclusions.
10. Prefer connected narrative over class lists, repository dumps, or code-heavy notes.

## Load guides only when needed

- Scope and dependency boundaries: `references/scope-guide.md`
- System/module/flow discovery: `references/discovery-guide.md`
- Evidence investigation and sub-agent delegation: `references/investigation-guide.md`
- Human/domain-expert interviews: `references/interview-guide.md`
- Evidence states and provenance: `references/evidence-guide.md`
- Human-first documentation: `references/writing-guide.md`
- Mermaid diagrams: `references/diagram-guide.md`
- Quality gates and wiki audit: `references/quality-guide.md`
- Updating knowledge after code changes: `references/maintenance-guide.md`

Use templates in `templates/` only after the corresponding content is understood. Never create a large empty documentation tree in advance.

# Workflow

## Stage 0 - Initialize or resume

1. Detect whether a knowledge wiki already exists.
2. If it exists, read in this order: `index.md` -> current checkpoint -> relevant pages -> recent `log.md` entries.
3. If it does not exist, create only the minimum index/checkpoint files.
4. Record the active goal and scope.

### Checkpoint 0 - Workspace ready

Proceed only when the target system, requested outcome, and documentation location are clear.

## Stage 1 - Establish system context

Read `references/discovery-guide.md`.

Determine only enough context to orient a new developer:
- what the system is for
- major business modules/capabilities
- external actors/systems
- high-level processing shape
- important terminology
- major unknowns

Do not descend into every package or service.

### Checkpoint 1 - System context

Present the proposed system map to the domain expert. Ask for correction when boundaries, terminology, or module responsibilities are uncertain. Deep module documentation must not begin until this context is accepted or explicitly marked provisional.

## Stage 2 - Define scope and boundaries

Read `references/scope-guide.md`.

Classify discovered areas as:
- `PRIMARY_SCOPE`: fully reverse engineer and document.
- `DEPENDENCY_BOUNDARY`: understand only enough to explain the contract and impact on primary scope.
- `OUT_OF_SCOPE`: record only when necessary for orientation.

Never recursively document a large dependency merely because traversal reaches it.

### Checkpoint 2 - Scope approval

Show the primary scope, dependency boundaries, exclusions, and unresolved scope questions. Obtain domain-expert approval before deep investigation.

## Stage 3 - Discover the module journey

Identify the module's major capabilities and flows before documenting implementation details. Propose a reading journey, for example:

`Module overview -> Entry flow -> Processing -> Posting -> Submission -> Status lifecycle -> Failure/recovery -> Change guide`

Create a Mermaid overview only when enough evidence exists to make it truthful.

### Checkpoint 3 - Journey approval

Validate with a knowledgeable person:
- major flows are not missing
- sequence is correct
- flow boundaries are sensible
- dependencies are not being mistaken for internal flows

Do not author final flow pages before this checkpoint.

## Stage 4 - Reverse engineer one flow

Select one bounded flow from the approved journey.

### 4A. Build an investigation plan

Read `references/investigation-guide.md`.

Consider independent tracks such as trigger/entry point, execution path, status reads/writes, business-rule implementation, integrations, important persistence, and failure/recovery.

If the host supports sub-agents and two or more independent tracks exist, delegate evidence discovery in parallel. Sub-agents discover evidence only; they never own scope, interviews, interpretation, canonical writing, or final diagrams.

### 4B. Reconcile evidence

Separate findings into verified facts, inferences, conflicts, unknowns, and questions that require a person.

### 4C. Interview the domain expert

Read `references/interview-guide.md`.

Interview whenever artifacts cannot reliably establish business meaning or operational intent. Ask one focused question at a time. Incorporate the answer before asking the next.

Typical interview topics include why the flow exists, what business event triggers it, why a status exists, what happens operationally when stuck, why branches differ, historical rationale, and manual recovery.

### Checkpoint 4 - Flow understanding

Before authoring final documentation, ensure the model contains purpose, trigger, technical entry point, connected stages, important branches, relevant statuses, dependency boundaries, outcome, next flow, and material failure/recovery behavior.

Expose unresolved inference or uncertainty instead of hiding it.

## Stage 5 - Author the flow

Read `references/writing-guide.md`, `references/diagram-guide.md`, and `references/evidence-guide.md`. Use `templates/flow.md` as a shape, not a form to fill mechanically.

A significant flow should explain, where relevant:
1. purpose
2. position in the larger journey
3. Mermaid visual overview
4. business trigger and technical entry point
5. connected processing walkthrough
6. business rules and meaningful variants
7. status progression
8. relevant architecture and dependency boundaries
9. important implementation decisions/rationale
10. developer change guidance
11. failure/recovery behavior
12. where to continue reading

Class/job/method names are supporting implementation references, not the primary explanation.

### Checkpoint 5 - Flow quality gate

Read `references/quality-guide.md`.

Do not mark a flow complete unless applicable checks pass:
- a newcomer can understand it without opening source code
- a useful Mermaid diagram exists
- functional and technical entry points are clear
- prose explains the connected journey
- class names do not dominate
- business meaning is present
- relevant statuses are understandable
- dependency boundaries are explicit
- unsupported assumptions are not presented as facts
- previous/next context is clear
- important claims have provenance

If the gate fails, rewrite before moving on. Update the checkpoint and `log.md` after completion, then return to Stage 4 for the next flow.

## Stage 6 - Synthesize the module

After major flows are individually verified:
- write/update the module overview
- create the end-to-end Mermaid journey
- consolidate cross-flow status lifecycle
- consolidate important business rules
- capture important design decisions
- create developer change guidance
- link dependency boundaries to their own modules only when separately documented

### Checkpoint 6 - Module review

Review the module with the domain expert as one story, not as isolated pages. Confirm that the reading journey matches how the business actually operates.

## Stage 7 - Wiki audit

Read `references/quality-guide.md` and review the wiki as a new developer would.

Fix material issues: unexplained jumps, contradictions, orphan pages, broken links, duplicated explanations, inconsistent terminology, class-name-heavy prose, bullet-list documentation, missing diagrams/evidence, unresolved blockers, and unclear module/dependency boundaries.

# Evidence states

Use consistently:
- `CODE_VERIFIED`
- `DOCUMENT_VERIFIED`
- `USER_CONFIRMED`
- `INFERRED`
- `UNKNOWN`
- `CONFLICT`

Only verified or user-confirmed knowledge may be stated authoritatively. Keep inference visibly qualified until verified.

# Human interview rule

Do not use people only as final reviewers. Treat engineers, product owners, operations staff, BAs, and SMEs as evidence sources when artifacts are insufficient.

If source/artifacts can answer reliably, investigate first. If the question concerns intent, meaning, operational convention, or historical rationale, interview rather than guessing.

# Query mode

When asked about an already-documented system rather than to create/update documentation:
1. read `index.md`
2. follow only relevant links
3. answer from maintained knowledge first
4. inspect source only when the wiki is insufficient or verification is required
5. do not activate the full reverse-engineering workflow unless documentation needs creation or repair

# Completion definition

Documentation is complete only when it is understandable by a human developer, navigable by an AI agent, evidence-backed, coherent across flows, explicit about uncertainty, visually supported by Mermaid where useful, and bounded to approved scope.
