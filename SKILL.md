---
name: system-reverse-engineer
description: Use when reverse-engineering, documenting, handing over, onboarding to, or maintaining a large existing software system. Builds scoped, evidence-backed human and agent documentation by framing system/module/capability/flow hierarchy, interviewing domain experts, tracing architecture, statuses, schemas, jobs, APIs, integrations, tests and operations, and publishing verified Markdown through Docusaurus.
---

# System Reverse Engineer

## Purpose

Create maintainable documentation for large brownfield systems from:

`source code + existing artifacts + domain-expert interviews -> verified Markdown -> Docusaurus`

Markdown is canonical. Docusaurus is the human-facing documentation shell. This skill owns system framing, scope, reverse engineering, evidence, interviews, technical completeness, documentation content, diagrams, and ensuring the Docusaurus site actually builds.

## References

Load supporting references only when relevant:

- **Docusaurus setup, navigation, Mermaid, MDX, styling or build work:** read `references/docusaurus.md` before changing the documentation site.
- **Framework-specific code discovery, especially Spring Boot/Spring Batch:** read `references/framework-discovery.md` before deep implementation tracing.

These references are guidance. Existing repository conventions and approved/installed dependency versions take precedence for exact commands/configuration.

## Hard Rules

1. **Never assume the requested module is the whole system.** Establish hierarchy first.
2. **Module != flow.** Never collapse system, module, capability and flow merely for convenience.
3. **Scope before deep code exploration.** Anything not explicitly approved is `OUT_OF_SCOPE`.
4. **Never investigate out-of-scope internals.** Record only verified boundaries from the in-scope side.
5. **Never publish inference as fact.** Ask, verify or mark unknown.
6. **Interview the user/domain expert whenever code cannot establish business meaning or operational truth.**
7. **Checkpoint continuously.** Large systems must be resumable across sessions/context windows.
8. **Human documentation is mandatory.** Agent-oriented notes alone never complete the task.
9. **Docusaurus setup is infrastructure, not the main task.** Keep it minimal, stable and separate from reverse engineering.
10. **Preserve human-confirmed rationale.** Never silently overwrite it.

## Stage 0 - Documentation Environment Gate

Preferred location:

```text
<repo-root>/
  documentation/
```

Before initializing, repairing, styling or structurally changing Docusaurus, read `references/docusaurus.md`.

### Existing Docusaurus project

If `documentation/` already contains a working Docusaurus project, reuse it. Read its package/config/sidebar/theme conventions before changing anything. Do not reinitialize or replace a working setup merely to match preferences.

### No Docusaurus project

If no documentation site exists, initialize a minimal Docusaurus site under `documentation/` using the Docusaurus version and package source available/approved in the environment.

If Docusaurus packages/tooling are unavailable, stop and ask the user to configure/provide them. Do not silently switch to another documentation framework.

After initialization, immediately run the available build command. **Do not begin large-scale documentation generation on top of a broken site.** Fix/resolve setup first.

Keep custom frontend work small. Prefer standard Docusaurus features, Markdown/MDX, Mermaid, CSS variables and reusable components only when they materially improve comprehension.

Do not let site setup consume the reverse-engineering task. Once the shell builds, move to system framing and content.

## Stage 1 - Frame the System

Before deep reverse engineering, establish:

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

Ask focused questions needed to establish:

- overall system/product name and purpose
- major known modules/business areas
- exact module(s)/capabilities requested for documentation
- explicit exclusions/deferred areas

A request such as "document Outward Clearing" means Outward Clearing is the **current scope inside a larger system** unless explicitly confirmed otherwise. It does not mean the repository/system is Outward Clearing.

Persist framing and scope immediately in a small documentation metadata/checkpoint area.

### Mandatory framing approval gate

Show the user the current hierarchy/scope before deep investigation, for example:

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

Explore only enough in-scope code/artifacts to identify candidate capabilities and flows. Do not assume package/service boundaries equal business flows.

Report the candidate decomposition with uncertainties, for example:

```text
Outward Clearing
|- Ingestion
|- Validation
|- Clearing Processing
|- Return Processing
`- Reconciliation
```

### Mandatory decomposition approval gate

Ask the user to approve/correct this map before treating it as canonical.

This prevents a large module from becoming one artificial `outward-flow`.

## Stage 3 - Reverse Engineer Progressively

Before deep implementation tracing in Spring Boot/Spring Batch or another supported framework, read `references/framework-discovery.md` when applicable.

Investigate one approved capability/flow/subflow at a time:

1. Read relevant existing docs/checkpoint context.
2. Trace concrete implementation evidence.
3. Identify architecture, statuses, data, jobs, APIs, integrations, files/events, rules, errors, tests and operations involved.
4. Record evidence and unresolved gaps.
5. Interview the user for knowledge code cannot establish.
6. Cross-check user explanations against implementation where applicable.
7. Reconcile conflicts explicitly.
8. Write/update verified human-facing Markdown/MDX for that bounded area.
9. Update navigation/cross-links as needed.
10. Checkpoint before switching areas.

If a flow becomes too large, split it into child flows/subflows and investigate them independently.

## Interview Protocol

Interviewing is a first-class discovery mechanism.

Ask when evidence cannot establish business purpose, terminology, rationale, ordering, manual activities, operational timing, status meaning, variants, exceptional paths, recovery/reprocessing, ownership, testing practices, troubleshooting or historical decisions.

Prefer one precise question at a time.

Good:

> I verified that ingestion writes `READY`, but I cannot establish what business condition allows Debit processing to begin. What gates Debit after ingestion?

After an answer, record it as `USER_CONFIRMED`, then seek implementation evidence when it describes current technical behavior.

## Evidence / Zero-Hallucination Contract

Use these states:

- `CODE_VERIFIED` - current source/config/tests/schema
- `DOCUMENT_VERIFIED` - authoritative existing artifact
- `USER_CONFIRMED` - domain expert confirmation
- `INFERRED` - plausible but unverified
- `UNKNOWN` - unresolved
- `CONFLICT` - credible sources disagree

Only verified/confirmed knowledge may be stated authoritatively.

`INFERRED` must be verified/confirmed first. `UNKNOWN` remains visible when material. `CONFLICT` preserves competing evidence and triggers investigation.

Never invent schedules, status meanings, transitions, retries, API semantics, schema relationships, rationale, testing procedures, recovery or out-of-scope behavior.

## Scope Contract

Coverage states:

- `DOCUMENTED`
- `IN_PROGRESS`
- `TODO`
- `OUT_OF_SCOPE`

Anything not explicitly approved is `OUT_OF_SCOPE`, not `UNKNOWN`.

For dependencies outside scope, document only:

`in-scope component -> verified interface/event/file/API -> OUT_OF_SCOPE module`

Do not inspect the other module's internals without scope expansion.

## Module Documentation Contract

Every approved module must become an independently useful technical handbook. Each applicable category must be documented, marked `NOT_APPLICABLE`, or identified as `UNKNOWN`.

Required categories where applicable:

1. **Overview** - purpose, boundary, terminology
2. **Architecture** - services/components, responsibilities, runtime relationships, decisions
3. **Capabilities** - approved decomposition
4. **Business Flows** - end-to-end flows/subflows
5. **Processing Timeline** - ordering, triggers, gates, verified schedules
6. **State & Status Model** - meanings, transitions, producers/consumers, conditions, side effects
7. **Data Model** - entities/tables, relationships, ownership, lifecycle
8. **Table Schemas** - important columns/keys/status fields and read/write usage
9. **Batch Jobs** - purpose, trigger, parameters, steps, reader/processor/writer/tasklet, dependencies, restart/recovery
10. **APIs** - purpose, caller, endpoint/contract, validation, data/status effects, errors
11. **Integrations** - direction, protocol, data, trigger, timeout/retry/reconciliation when verified
12. **Files / Events / Messaging** - producers/consumers, formats/topics, ordering
13. **Business Rules** - conditions and rationale
14. **Variants & Branches** - type/size/country/channel/etc. and divergence/rejoin points
15. **Error Handling** - failure states and impact
16. **Recovery / Reprocessing** - automatic/manual behavior and restrictions
17. **Testing** - prerequisites, test data, triggering, expected result, DB/status verification, mocks/stubs/tests
18. **Operations / Troubleshooting** - stuck processing, logs/metrics, safe recovery, prohibited manual actions
19. **Architecture Decisions / Rationale** - why unusual behavior exists
20. **Code Map** - important entry points and where to start for common changes

Do not generate filler. Ask when missing knowledge is material.

## State Transition Rules

Do not derive a state machine from an enum alone. Trace:

- owning entity
- business meaning
- current state
- event/condition
- next state
- setter
- consumer
- variant applicability
- side effects
- failure/recovery
- evidence

Search writes, reads, predicates, repository queries, jobs/listeners/controllers and tests.

Generate a transition table plus Mermaid state diagram when useful. Unknown transitions stay unknown.

## Data / Schema Rules

For important tables/entities document purpose, ownership, keys, important columns, relationships, lifecycle, readers, writers, relevant jobs/APIs/flows and evidence.

Prefer useful technical understanding over raw column dumps. Use Mermaid ER diagrams where helpful.

## Jobs, APIs and Integrations Must Connect to Flows

Do not create isolated inventories.

Every important job/API/integration explains why it exists and where it participates.

Jobs: trigger, parameters, steps, reads/writes, statuses, dependencies, integrations, failure/restart/reprocessing, testing, source.

APIs: purpose, caller, request/response semantics, validation, state/data changes, downstream calls, errors, testing, source.

Integrations: purpose, ownership/direction, protocol, payload/data, trigger, timeout/retry/reconciliation, failure impact, testing, source when verifiable.

## Testing and Maintainability

Capture where applicable:

- runtime/local prerequisites
- required configuration
- test-data setup
- how to trigger flows/jobs/APIs
- expected statuses/results
- DB verification
- mocks/stubs
- existing unit/integration/component tests
- integration testing approach
- safe troubleshooting/recovery
- common change entry points

If evidence does not reveal how the team tests an integration, ask rather than inventing a procedure.

## Checkpoint / Resume Protocol

Do not rely on conversation context.

Persist a small checkpoint containing:

- system framing
- approved scope
- approved module decomposition
- current module/capability/flow
- completed/in-progress/unexplored approved areas
- open questions
- unknowns
- conflicts
- important user confirmations
- last checkpoint

Checkpoint after framing approval, decomposition approval, substantial traces, important user answers, completed flows/subflows, resolved status/variant/conflict work, before switching areas, around sub-agent waves and before context pressure risks losing work.

New sessions must resume from checkpoint + relevant docs instead of rediscovering the repository.

## Sub-Agent Coordination

Use sub-agents when supported and investigations are independent. Otherwise run the same queue sequentially.

Good parallel work: independent child flows, job discovery, API mapping, schema usage, status-write tracing, integration discovery after hierarchy approval.

Each sub-agent receives exact scope, questions, relevant context, allowed paths where practical, evidence requirements and a no-guessing rule.

Sub-agents return findings; **the coordinator is the canonical writer**. Do not delegate system/module hierarchy or business ordering decisions independently.

## Human Documentation / Docusaurus Publishing

Human documentation is a first-class deliverable. Read `references/docusaurus.md` before site/navigation/visual implementation work.

### Information architecture

Prefer a module-oriented sidebar rather than a repository/package-oriented sidebar:

```text
System Overview
Modules
  Outward Clearing
    Overview
    Architecture
    Flows
    Timeline
    Status Model
    Data Model
    Batch Jobs
    APIs
    Integrations
    Testing
    Operations
Developer Reference
Documentation Coverage
```

Each flow may have child pages when large.

### Visual quality

Use Docusaurus Markdown/MDX and Mermaid for architecture, end-to-end flows, subflows, sequences, state transitions, ER relationships and dependency maps.

Prefer overview -> drill-down -> technical reference. Never force a complex module into one diagram/page.

Use consistent semantic colors for categories such as normal processing, decisions, integrations, failures/unknowns and out-of-scope boundaries. Ensure meaning is still understandable without color.

Prefer built-in Docusaurus/admonition/tabs/details capabilities before custom React. Add reusable custom MDX components only for repeated high-value interactions such as a status/variant explorer; do not build bespoke UI for every page.

Keep animations subtle and optional. Documentation must remain understandable as static content.

### Agent usability

Because Markdown is canonical, agents should be able to read `documentation/docs/` directly without needing the rendered site.

Maintain a small agent entry point such as `documentation/AGENT_INDEX.md` or equivalent containing:

- system/module map
- approved scope/coverage
- links to module overview pages
- current checkpoint location
- key glossary/reference links

Do not duplicate all documentation into an agent-only knowledge tree. The index should navigate the same Markdown humans use.

## Docusaurus Build Discipline

Docusaurus infrastructure must not become an unfinished side project. Follow `references/docusaurus.md` for detailed setup/build guidance.

- Pin/use the repository-approved dependency versions.
- Do not upgrade dependencies unless required/approved.
- Build immediately after initial setup.
- Build after structural navigation/configuration changes.
- Build again at completion.
- Treat broken links, invalid MDX/Mermaid and sidebar failures as documentation defects.
- If the build is broken, do not declare documentation complete.
- Do not rewrite a working Docusaurus configuration merely for aesthetics.

## Completion Gate

Do **not** declare completion because discovery/agent notes exist.

Completion requires for approved scope:

- system framing approved
- module scope approved
- capability/flow decomposition approved
- major flows verified/confirmed
- architecture documented
- important state transitions documented
- important data/table schemas documented
- jobs/APIs/integrations connected to flows
- testing/operations captured where applicable
- unknowns/conflicts reported
- scope boundaries respected
- human Markdown/MDX pages generated
- useful Mermaid diagrams generated
- Docusaurus navigation/cross-links generated
- agent index points to the same canonical docs
- Docusaurus build succeeds
- checkpoint is current

If build tooling cannot run, state that and do not claim it passed.

Semantic completeness cannot be claimed while material `UNKNOWN` or `CONFLICT` items remain.

## Maintenance Mode

For later changes:

1. read relevant docs/checkpoint
2. inspect current implementation/change
3. identify affected flows/statuses/tables/jobs/APIs/integrations/tests
4. update only affected canonical Markdown/MDX
5. update affected diagrams/cross-links/navigation
6. preserve unrelated and `USER_CONFIRMED` rationale
7. run Docusaurus build
8. checkpoint

If code contradicts human-confirmed rationale, preserve both and ask whether the business rule/design changed.

## Common Failure Modes

| Failure | Required correction |
|---|---|
| Treat requested module as entire system | Frame system first and obtain approval |
| Treat module as one flow | Discover capabilities/flows and obtain approval |
| Scan entire repository | Restrict deep analysis to approved scope |
| Spend the task rebuilding Docusaurus | Get a minimal working shell, build it, then document |
| Docusaurus unavailable | Ask user to configure/provide it; do not switch platforms |
| Generate only agent knowledge | Continue until human documentation exists and builds |
| Maintain separate human/agent truth | Use canonical Markdown + small agent index |
| Enum -> state diagram | Trace actual transitions |
| Dump schema without meaning | Explain ownership, relationships, lifecycle and usage |
| List jobs/APIs without context | Connect them to flows |
| Guess testing/recovery | Interview user or mark unknown |
| Hide missing knowledge | Surface `UNKNOWN`/`CONFLICT` |
| Giant Mermaid graph | Decompose into progressive diagrams |
| Sub-agents edit canonical docs independently | Coordinator merges findings |
| Restart discovery every session | Resume from checkpoint |
| Rewrite human rationale | Preserve and reconcile |
