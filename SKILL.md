---
name: system-reverse-engineer
description: Use when reverse-engineering, documenting, handing over, onboarding to, or maintaining a large existing software system. Builds scoped, evidence-backed human and agent documentation by framing system/module/capability/flow hierarchy, interviewing domain experts, tracing architecture, statuses, schemas, jobs, APIs, integrations, tests and operations, and publishing verified Markdown through Docusaurus.
---

# System Reverse Engineer

## Purpose

Create maintainable documentation for large brownfield systems from:

`source code + existing artifacts + domain-expert interviews -> verified Markdown -> Docusaurus`

Markdown is canonical. Docusaurus is the human-facing shell. Maintain a lightweight knowledge graph for agent navigation and impact analysis without creating a second source of truth.

## References

Load references only when relevant:

- Docusaurus setup/navigation/Mermaid/MDX/styling/build: `references/docusaurus.md`
- Framework discovery, especially Spring Boot/Spring Batch: `references/framework-discovery.md`
- Knowledge graph/model, impact analysis and agent navigation: `references/knowledge-model.md`

Existing repository conventions and approved/installed dependency versions take precedence for exact commands/configuration.

## Hard Rules

1. Establish system hierarchy before deep investigation; never assume the requested module is the whole system.
2. Keep system, module, capability, flow and subflow distinct unless evidence/user confirmation supports collapsing them.
3. Obtain explicit scope approval before deep exploration. Treat everything else as `OUT_OF_SCOPE`.
4. Never reverse-engineer out-of-scope internals; record only verified boundaries from the in-scope side.
5. Never publish inference as fact. Verify, ask, or mark uncertainty.
6. Interview the domain expert whenever code cannot establish business or operational truth.
7. Checkpoint continuously so work can resume across sessions/context windows.
8. Produce human documentation; agent notes/graph alone never complete the task.
9. Keep Docusaurus infrastructure minimal and stable; do not let frontend work replace documentation work.
10. Preserve human-confirmed rationale and reconcile contradictions explicitly.
11. Keep Markdown/MDX canonical. Treat the knowledge graph as a derived navigational/impact model.

## Stage 0 - Documentation Environment Gate

Use `<repo-root>/documentation/` unless an approved documentation location already exists.

Read `references/docusaurus.md` for setup/repair. Reuse a working Docusaurus project. If none exists, initialize a minimal site using approved/available packages. If tooling is unavailable, stop and ask the user to configure/provide it; never silently switch frameworks.

Run a production build immediately after initialization. Do not begin large-scale documentation on a broken shell. Prefer standard Docusaurus, Markdown/MDX, Mermaid and small CSS changes over custom frontend development.

## Stage 1 - Frame and Approve the System

Establish:

```text
SYSTEM
  -> MODULE
      -> CAPABILITY
          -> FLOW
              -> SUBFLOW
                  -> PROCESSING STEP
                      -> TECHNICAL COMPONENT
```

Ask only what is needed to determine system purpose, major known modules, requested scope and explicit exclusions/deferred areas. Persist framing/scope immediately.

Show the proposed hierarchy and coverage to the user and obtain approval before deep investigation. `Document Outward Clearing` means Outward is current scope inside a larger system unless explicitly confirmed otherwise.

## Stage 2 - Map and Approve the Selected Module

Explore only enough in-scope evidence to propose capabilities and flows. Do not assume package/service boundaries equal business flows.

Show candidate decomposition, uncertainties and boundaries. Obtain user approval/correction before treating it as canonical. This prevents a large module from becoming one artificial flow.

## Stage 3 - Reverse Engineer Progressively

When applicable, read `references/framework-discovery.md` before framework-specific tracing.

Investigate one approved capability/flow/subflow at a time:

1. Read relevant docs and checkpoint context.
2. Trace implementation evidence.
3. Identify architecture, statuses, data, jobs, APIs, integrations, files/events, rules, errors, tests and operations.
4. Record evidence and gaps.
5. Interview the user for knowledge code cannot establish.
6. Cross-check user explanations against implementation where applicable.
7. Reconcile conflicts explicitly.
8. Update canonical human-facing Markdown/MDX.
9. Update affected knowledge-graph nodes/edges after facts are verified.
10. Update navigation/cross-links as needed.
11. Checkpoint before switching bounded areas.

If a flow becomes too large, persist the parent map, split it into child flows/subflows, and investigate children independently.

## Interview Protocol

Treat interviewing as first-class discovery. Ask when evidence cannot establish business purpose/terminology, rationale, ordering/gates, manual activities, timing, status meaning, variants, exceptional paths, recovery/reprocessing, ownership, testing, troubleshooting or historical decisions.

Prefer one precise question at a time. Record answers as `USER_CONFIRMED`; seek implementation evidence when an answer describes current technical behavior.

## Evidence and Scope Contracts

Evidence states:

- `CODE_VERIFIED`
- `DOCUMENT_VERIFIED`
- `USER_CONFIRMED`
- `INFERRED`
- `UNKNOWN`
- `CONFLICT`

Only verified/confirmed knowledge may be stated authoritatively. Keep material `UNKNOWN` visible. Preserve competing evidence for `CONFLICT`. Never invent schedules, statuses, transitions, retries, API semantics, schema relationships, rationale, testing, recovery or out-of-scope behavior.

Coverage states:

- `DOCUMENTED`
- `IN_PROGRESS`
- `TODO`
- `OUT_OF_SCOPE`

Anything not explicitly approved is `OUT_OF_SCOPE`, not `UNKNOWN`. For excluded dependencies, document only the verified boundary and ask before expanding scope.

## Module Documentation Contract

Make every approved module an independently useful technical handbook. For each applicable category, document it, mark `NOT_APPLICABLE`, or expose it as `UNKNOWN`; never silently omit a material category.

Cover where applicable:

1. Overview, boundary and terminology
2. Architecture, component responsibilities and key decisions
3. Approved capabilities
4. Business flows/subflows
5. Processing timeline, triggers, gates and verified schedules
6. State/status meanings and transitions
7. Data model, ownership and lifecycle
8. Important table schemas/keys/status fields and usage
9. Batch jobs, parameters, steps, dependencies and restart/recovery
10. APIs, callers, contracts, validation, effects and errors
11. Integrations, direction, protocol, data and failure/reconciliation behavior
12. Files/events/messaging and producers/consumers
13. Business rules and known rationale
14. Variants/branches and divergence/rejoin points
15. Error handling and failure impact
16. Recovery/reprocessing
17. Testing, test data, triggering and verification
18. Operations/troubleshooting and safe recovery
19. Architecture decisions/rationale
20. Code map and common change entry points

Do not generate filler. Interview the user when missing knowledge is material.

## State, Data and Technical Trace Rules

Do not derive state machines from enums alone. Trace owning entity, business meaning, current state, event/condition, next state, setter, consumer, variant, side effects, failure/recovery and evidence. Search writes, reads, predicates, repository queries, jobs/listeners/controllers and tests. Produce a transition table and Mermaid state diagram when useful.

For important entities/tables, document purpose, ownership, keys, important columns, relationships, lifecycle, readers/writers, relevant flows and evidence. Prefer useful understanding over raw schema dumps.

Connect jobs, APIs and integrations to business flows rather than creating isolated inventories. Explain why each exists, what it reads/writes/calls, state effects, failures/recovery, testing and implementation entry point.

## Testing and Maintainability

Capture runtime/local prerequisites, required configuration, test-data setup, triggering, expected statuses/results, DB verification, mocks/stubs, existing tests, integration-testing approach, troubleshooting/recovery and common change entry points where applicable.

Ask the user when evidence cannot establish actual team testing or operational procedures.

## Knowledge Graph

Read `references/knowledge-model.md` before creating/updating the graph.

Maintain a compact graph under `documentation/knowledge/` when agent navigation/impact analysis is part of the setup. Use stable IDs, controlled node/relationship types and provenance on material nodes/edges.

Update the graph incrementally after facts are verified. Do not model every class/method or duplicate prose. Graph traversal identifies candidate impact, not proof; inspect current code before claiming change impact.

Keep `documentation/AGENT_INDEX.md` small and point it to the approved module map, graph, canonical docs and checkpoint. Do not duplicate the documentation corpus into an agent-only tree.

## Checkpoint / Resume Protocol

Persist a small checkpoint containing system framing, approved scope, approved decomposition, current bounded area, completed/in-progress/unexplored approved areas, open questions, unknowns, conflicts, important user confirmations and last checkpoint.

Checkpoint after framing/decomposition approval, substantial traces, important user answers, completed flows/subflows, resolved status/variant/conflict work, before switching areas, around sub-agent waves and before context pressure risks losing work.

New sessions must resume from checkpoint + relevant canonical docs instead of rediscovering the repository.

## Sub-Agent Coordination

Use sub-agents when supported and investigations are independent; otherwise execute the same queue sequentially.

Give each sub-agent exact scope/questions, relevant context, allowed paths where practical, evidence requirements and a no-guessing rule. Sub-agents return evidence-backed findings; the coordinator reconciles and is the canonical writer for Markdown, graph and checkpoints. Do not delegate hierarchy/business-ordering decisions independently.

## Human Documentation / Docusaurus

Read `references/docusaurus.md` before site/navigation/visual work.

Prefer module-oriented navigation:

```text
System Overview
Modules
  <Module>
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
Documentation Coverage
Developer Reference
```

Use overview -> drill-down -> technical reference. Use Mermaid for architecture, flows, sequences, state transitions, ER relationships and dependencies. Split large diagrams. Use consistent semantic visual meaning and never rely on color alone.

Prefer built-in Docusaurus/admonitions/details/tabs and plain Markdown before custom MDX/React. Keep animations subtle/optional; static documentation must remain complete.

## Build Discipline

Use repository-approved dependency versions and existing package manager/scripts. Do not upgrade unless required/approved.

Build Docusaurus after initial setup, after structural config/sidebar/theme changes, and at completion. Treat broken links, invalid MDX/Mermaid, sidebar failures and custom-component errors as defects. Do not declare completion while the required Docusaurus build is broken.

## Completion Gate

For approved scope require:

- framing/scope and module decomposition approved
- major flows verified/confirmed
- architecture, important states, data/tables, jobs/APIs/integrations documented and connected
- testing/operations captured where applicable
- unknowns/conflicts reported
- scope boundaries respected
- human Markdown/MDX and useful diagrams generated
- navigation/cross-links generated
- knowledge graph updated when configured
- agent index points to canonical docs/graph/checkpoint
- Docusaurus production build succeeds
- checkpoint is current

If build tooling cannot run, state that and do not claim it passed. Do not claim semantic completeness while material `UNKNOWN` or `CONFLICT` items remain.

## Maintenance Mode

For later changes:

1. Read relevant docs, graph and checkpoint.
2. Inspect current implementation/change.
3. Identify affected flows/statuses/tables/jobs/APIs/integrations/tests.
4. Update only affected canonical Markdown/MDX.
5. Update affected graph nodes/edges, diagrams, links and navigation.
6. Preserve unrelated and `USER_CONFIRMED` rationale.
7. Run Docusaurus production build.
8. Checkpoint.

If code contradicts human-confirmed rationale, preserve both and ask whether the business rule/design changed.

## Common Failure Modes

| Failure | Required correction |
|---|---|
| Requested module becomes whole system | Frame/approve system hierarchy first |
| Module becomes one giant flow | Map/approve capabilities and flows |
| Agent scans entire repository | Restrict deep analysis to approved scope |
| Docusaurus consumes the task | Build minimal stable shell, then document |
| Only agent knowledge is generated | Continue until human docs exist and build |
| Separate human/agent truths emerge | Canonical Markdown + derived graph/index |
| Enum becomes state machine | Trace actual transitions |
| Schema is dumped without meaning | Explain ownership, lifecycle and usage |
| Jobs/APIs are isolated lists | Connect them to business flows |
| Testing/recovery is guessed | Interview or mark unknown |
| Missing knowledge is hidden | Surface `UNKNOWN`/`CONFLICT` |
| Diagram becomes unreadable | Split into progressive diagrams |
| Graph models every class/method | Keep it semantic and impact-oriented |
| Graph is treated as impact proof | Verify against current code |
| Sub-agents write competing truth | Coordinator reconciles/writes |
| Session restarts discovery | Resume from checkpoint |
| Human rationale is overwritten | Preserve and reconcile |
