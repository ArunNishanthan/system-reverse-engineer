---
name: system-reverse-engineer
description: Use when reverse-engineering, documenting, handing over, onboarding to, or maintaining a large existing software system. Builds scoped, evidence-backed human and agent documentation by framing system/module/capability/flow hierarchy, interviewing domain experts, tracing code, statuses, schemas, jobs, APIs, integrations, tests and operations, and publishing verified Markdown through docmd.
---

# System Reverse Engineer

## Purpose

Create maintainable documentation for large brownfield systems from three sources:

`source code + existing artifacts + domain-expert interviews -> verified Markdown -> docmd`

The Markdown documentation is canonical and must serve both humans and agents. docmd owns presentation, navigation, search, Mermaid rendering, OKF/agent outputs, MCP integration, validation and build mechanics. This skill owns system framing, scope, reverse engineering, evidence, interviews, technical completeness and documentation content.

## Hard Rules

1. **Never assume the requested module is the whole system.** Establish hierarchy first.
2. **Module != flow.** Never collapse system, module, capability and flow merely for convenience.
3. **Scope before deep code exploration.** Anything not explicitly approved is `OUT_OF_SCOPE`.
4. **Never investigate out-of-scope internals.** Record only verified boundaries from the in-scope side.
5. **Never publish inference as fact.** Ask, verify or mark unknown.
6. **Interview the user/domain expert whenever code cannot establish business meaning or operational truth.**
7. **Checkpoint continuously.** Large systems must be resumable across sessions/context windows.
8. **Human documentation is mandatory.** Agent-oriented knowledge alone never completes the task.
9. **Do not build a documentation framework.** Use docmd and its official skill/instructions.
10. **Preserve human-confirmed rationale.** Never silently overwrite it during regeneration or maintenance.

## Stage 0 - Documentation Environment Gate

Before documentation work, inspect the repository root and documentation area.

Preferred location:

```text
<repo-root>/
  documentation/
```

### Existing docmd project

If a docmd project already exists, use it. Read its project instructions/configuration and continue without rebuilding the site infrastructure.

### No docmd project

Check whether both are available:

- docmd CLI/runtime
- official docmd agent skill/instructions

If both are available, ask the user for permission to initialize docmd under `documentation/` unless they already explicitly requested initialization.

If either is unavailable, **stop documentation generation** and ask the user to configure/install docmd and its official agent skill. Do not silently fall back to Docusaurus, another framework, or a homemade site.

Suggested message:

> This repository does not have a usable docmd setup. Please configure docmd and its official agent skill, then ask me to continue. I will not improvise a different documentation platform.

When the official docmd skill is available, use it for docmd initialization, Markdown/frontmatter conventions, navigation, Mermaid presentation, OKF/agent outputs, validation and build. Do not duplicate or invent docmd-specific behavior in this skill.

The documentation source must remain useful as ordinary Markdown even when MCP is unavailable. docmd MCP is an optional efficient agent interface; do not make documentation correctness depend on MCP transport availability.

## Stage 1 - Frame the System

Before deep reverse engineering, establish the conceptual hierarchy:

```text
SYSTEM
  -> MODULE
      -> CAPABILITY
          -> FLOW
              -> SUBFLOW
                  -> PROCESSING STEP
                      -> TECHNICAL COMPONENT
```

Not every system needs every level, but levels must not be collapsed without evidence or user confirmation.

Ask focused questions needed to establish at least:

- overall system/product name and purpose
- major known modules/business areas
- exact module(s)/capabilities requested for documentation
- explicit exclusions or deferred areas

A request such as "document Outward Clearing" means Outward Clearing is the **current scope inside a larger system** unless the user explicitly confirms otherwise. It does not mean the entire repository/system is Outward Clearing.

Persist the framing and scope immediately.

### Mandatory framing approval gate

Before deep investigation, show the user your current hierarchy and scope, for example:

```text
Cheque Clearing Platform
|- Inward Clearing       OUT_OF_SCOPE
|- Outward Clearing      IN_SCOPE
|- Cheque Book           OUT_OF_SCOPE
|- Inventory             OUT_OF_SCOPE
|- Reports               OUT_OF_SCOPE
`- Data Migration        OUT_OF_SCOPE
```

Ask the user to approve/correct it. **Do not proceed to deep reverse engineering until approved.**

## Stage 2 - Map the Selected Module Before Documenting It

Explore only enough in-scope code/artifacts to identify candidate capabilities and flows. Do not generate final documentation yet.

Report the candidate decomposition to the user, including uncertainties. Example:

```text
Outward Clearing
|- Ingestion
|- Validation
|- Clearing Processing
|- Return Processing
`- Reconciliation
```

### Mandatory decomposition approval gate

Ask the user to approve/correct the module decomposition before treating these as canonical flows/capabilities.

This prevents a large module from becoming one artificial `outward-flow` and prevents technical package structure from being mistaken for business structure.

## Stage 3 - Reverse Engineer Progressively

Investigate one approved capability/flow/subflow at a time.

For each bounded investigation:

1. Read existing relevant documentation/checkpoint context.
2. Trace concrete implementation evidence.
3. Identify statuses, data, jobs, APIs, integrations, files/events, rules, errors, tests and operational behavior involved.
4. Record evidence and unresolved gaps.
5. Interview the user for business/operational knowledge code cannot establish.
6. Cross-check user explanations against implementation where applicable.
7. Reconcile conflicts explicitly.
8. Write/update the verified Markdown for that bounded area.
9. Checkpoint before switching areas.

If a flow becomes too large, split it into child flows/subflows, persist the parent map, and investigate children independently.

## Interview Protocol

Interviewing is a first-class discovery mechanism, not a fallback.

Ask when evidence cannot establish:

- business purpose or terminology
- why a rule/design exists
- ordering between independently triggered processes
- manual/operator activities
- operational timing
- status business meaning
- variants/branches and their conditions
- exceptional paths and recovery/reprocessing
- ownership boundaries
- how the team actually tests a flow/integration
- troubleshooting practices
- historical decisions or deliberate omissions

Prefer one precise question at a time.

Good:

> I verified that ingestion writes `READY`, but I cannot establish what business condition allows Debit processing to begin. What gates Debit after ingestion?

Bad:

> Explain the whole module.

After an answer, save it as `USER_CONFIRMED`, then search for supporting implementation evidence when the statement describes current technical behavior.

## Evidence / Zero-Hallucination Contract

Every material claim uses one of these states:

- `CODE_VERIFIED` - directly supported by current source/configuration/tests/schema
- `DOCUMENT_VERIFIED` - supported by an authoritative existing artifact
- `USER_CONFIRMED` - explicitly confirmed by a domain expert
- `INFERRED` - plausible but not verified
- `UNKNOWN` - unresolved
- `CONFLICT` - credible sources disagree

Authoritative human documentation may state `CODE_VERIFIED`, `DOCUMENT_VERIFIED` and `USER_CONFIRMED` knowledge as facts.

`INFERRED` must be verified or confirmed before becoming authoritative prose.

`UNKNOWN` must remain visible when material. Do not make a diagram look complete by inventing a transition.

`CONFLICT` must preserve competing evidence and trigger investigation/user clarification.

Never invent schedules, status meanings, transition rules, retries, API semantics, schema relationships, business rationale, testing procedures, operational recovery or behavior beyond an out-of-scope boundary.

## Scope Contract

Track coverage separately from evidence:

- `DOCUMENTED`
- `IN_PROGRESS`
- `TODO`
- `OUT_OF_SCOPE`

Anything not explicitly approved for current documentation is `OUT_OF_SCOPE`, not `UNKNOWN`.

If an in-scope component calls an excluded module, document only:

`in-scope component -> verified interface/event/file/API -> OUT_OF_SCOPE module`

Do not follow the dependency internally. Ask before expanding scope. Sub-agents inherit the same boundary.

## Module Documentation Contract

Every approved module must become an independently useful technical handbook. Each applicable category must be documented, explicitly `NOT_APPLICABLE`, or identified as `UNKNOWN`; important categories must not silently disappear.

Required categories where applicable:

1. **Overview** - purpose, ownership/boundary, terminology
2. **Architecture** - services/components and responsibilities, runtime relationships, key design decisions
3. **Capabilities** - module decomposition
4. **Business Flows** - end-to-end flows and subflows
5. **Processing Timeline** - ordering, triggers, gates, schedules only when verified
6. **State & Status Model** - definitions, transitions, producers/consumers, conditions and side effects
7. **Data Model** - entities/tables, relationships, ownership and lifecycle
8. **Table Schemas** - important columns/keys/status fields and read/write usage
9. **Batch Jobs** - purpose, trigger, parameters, steps, reader/processor/writer/tasklet, dependencies, restart/recovery
10. **APIs** - purpose, caller, endpoint/contract, validation, status/data effects, errors
11. **Integrations** - direction, protocol, data exchanged, trigger, retry/timeout/reconciliation behavior when verified
12. **Files / Events / Messaging** - producers/consumers, formats/topics, ordering and processing relationship
13. **Business Rules** - conditions and rationale where known
14. **Variants & Branches** - type/size/country/channel/etc. and where flows diverge/rejoin
15. **Error Handling** - failure states and impact
16. **Recovery / Reprocessing** - automatic/manual behavior and restrictions
17. **Testing** - prerequisites, test data, triggering, expected result, DB/status verification, mocks/stubs and existing tests
18. **Operations / Troubleshooting** - how to identify stuck processing, logs/metrics when verified, safe recovery and prohibited manual actions
19. **Architecture Decisions / Rationale** - why unusual behavior exists, especially deliberate omissions
20. **Code Map** - important entry points and where to start for common changes

Do not generate filler for a missing category. Ask the user when the missing knowledge is material.

## State Transition Rules

Statuses are first-class system knowledge.

Do not derive a state machine from an enum alone. Trace:

- entity owning the status
- business meaning
- current status
- event/condition
- next status
- code that sets it
- code/process that consumes it
- variant applicability
- side effects
- failure/recovery path
- evidence

Search writes, reads, predicates, repository queries, jobs/listeners/controllers, tests and user knowledge.

Generate both a readable transition table and Mermaid state diagram when useful. Unknown transitions remain unknown.

## Data / Schema Rules

For important tables/entities document:

- business/technical purpose
- owning module/component
- primary/foreign/business keys
- important columns, especially statuses and routing fields
- relationships
- lifecycle
- writers
- readers
- relevant jobs/APIs/flows
- schema/entity/migration/query evidence

Prefer useful technical understanding over dumping every column. Use Mermaid ER diagrams where they improve comprehension.

## Jobs, APIs and Integrations Must Connect to Flows

Do not create isolated inventories.

Every important job/API/integration should explain **why it exists and where it participates in the module's behavior**.

For jobs include trigger, parameters, steps, data read/write, statuses, dependencies, integrations, failure/restart/reprocessing, testing and source location.

For APIs include purpose, caller, request/response semantics, validation, state/data changes, downstream calls, errors, testing and source location.

For integrations include purpose, ownership/direction, protocol, payload/data, trigger, timeout/retry/reconciliation behavior, failure impact, testing and source location when verifiable.

## Testing and Maintainability

Documentation is incomplete if a future engineer understands architecture but cannot safely change or test it.

Capture where applicable:

- local/runtime prerequisites
- required configuration
- test-data setup
- how to trigger a flow/job/API
- expected statuses/results
- database verification
- mocks/stubs/test doubles
- existing unit/integration/component tests
- integration testing approach
- safe troubleshooting/recovery
- common change entry points

If the repository does not reveal how the team tests an external integration, ask the user rather than inventing a process.

## Checkpoint / Resume Protocol

Do not rely on conversation context for large projects.

Persist a small resume/checkpoint artifact in the documentation workspace containing at least:

- system framing
- approved scope
- approved module decomposition
- current module/capability/flow
- completed areas
- in-progress areas
- unexplored approved areas
- open questions
- unknowns
- conflicts
- important user confirmations
- last checkpoint

Checkpoint after:

- framing/scope approval
- decomposition approval
- substantial code trace
- important user answer
- completed flow/subflow
- resolved status model/variant/conflict
- before switching bounded areas
- before/after a sub-agent investigation wave
- before context pressure risks losing work

A new session must read the checkpoint and relevant Markdown first rather than rediscovering the entire repository.

## Sub-Agent Coordination

Use sub-agents when supported and tasks are independent. Otherwise execute the same queue sequentially.

Good parallel tasks include independent child flows, job discovery, API mapping, schema usage, status-write tracing and integration discovery after the module boundary is approved.

Each sub-agent receives exact scope, question(s), relevant known context, allowed paths where practical, evidence requirements and explicit instruction not to guess.

Sub-agents return evidence-backed findings. **The coordinator is the canonical writer.** The coordinator detects conflicts, interviews the user where needed, merges verified findings and checkpoints.

Do not delegate agents to independently decide the system/module/capability hierarchy or invent business ordering.

## Human Documentation / docmd Publishing

The human documentation is a first-class deliverable, not a rendering afterthought.

Use the official docmd skill/instructions for presentation details. This skill supplies verified content and required information architecture.

Human pages should be:

- business-first and technically deep
- clear and visually attractive
- searchable and cross-linked
- progressively drillable
- concise at overview level and detailed on child pages
- explicit about unknown/conflicting knowledge
- usable by new developers, maintainers and operations/support readers

Use Mermaid where diagrams improve understanding, especially for:

- system/module architecture
- end-to-end flows
- subflows
- sequences
- status/state transitions
- ER/data relationships
- service/integration dependencies

Prefer overview -> drill-down -> technical reference. Never create one giant diagram for a large module. Use consistent semantic colors according to the docmd/Mermaid guidance rather than decorative random colors.

Markdown remains canonical. docmd may additionally generate search/navigation, OKF/graph outputs, LLM context files and MCP access. These are consumers/derived representations, not separate sources of truth.

## Completion Gate

Do **not** declare the requested scope complete merely because discovery files or agent context exist.

Completion requires, for the approved scope:

- system framing approved
- module scope approved
- module capability/flow decomposition approved
- major business flows verified/confirmed
- architecture documented
- important state transitions documented
- important data model/table schemas documented
- jobs/APIs/integrations connected to flows
- testing and operational knowledge captured where applicable
- unknowns/conflicts explicitly reported
- out-of-scope boundaries respected
- human Markdown pages generated
- useful Mermaid diagrams generated
- navigation/cross-links generated
- agent/OKF outputs generated when configured by docmd
- docmd validation succeeds
- docmd build succeeds
- checkpoint/resume state is current

If build/validation tooling cannot be executed, state that explicitly and do not claim it passed.

Semantic completeness cannot be claimed while material `UNKNOWN` or `CONFLICT` items remain. Report them clearly.

## Maintenance Mode

For later code changes:

1. read relevant documentation/checkpoint first
2. inspect current implementation/change
3. identify affected modules/flows/statuses/tables/jobs/APIs/integrations/tests
4. update only affected verified Markdown
5. update affected diagrams/cross-links
6. preserve unrelated and `USER_CONFIRMED` rationale
7. use docmd validation/build
8. checkpoint

If current code contradicts human-confirmed rationale, preserve both and ask whether the business rule/design decision changed.

## Common Failure Modes

| Failure | Required correction |
|---|---|
| Treat requested module as entire system | Frame system first and obtain approval |
| Treat module as one flow | Discover capabilities/flows and obtain decomposition approval |
| Scan entire repository | Restrict deep analysis to approved scope |
| Configure/build Docusaurus | Stop; use docmd + official docmd skill |
| docmd unavailable | Ask user to configure it; do not improvise another platform |
| Generate only agent knowledge | Continue until human documentation is complete |
| Enum -> state diagram | Trace real transitions and evidence |
| Dump schema without meaning | Document ownership, relationships, lifecycle and usage |
| List jobs/APIs without context | Connect them to business flows |
| Guess how testing/recovery works | Interview user or mark unknown |
| Hide missing knowledge | Surface `UNKNOWN`/`CONFLICT` |
| Giant Mermaid graph | Decompose into progressive diagrams |
| Sub-agents edit canonical docs independently | Coordinator merges evidence |
| Restart discovery every session | Resume from checkpoint |
| Rewrite human rationale during maintenance | Preserve and reconcile |
