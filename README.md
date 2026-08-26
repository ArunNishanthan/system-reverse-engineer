# System Reverse Engineer

An Agent Skill for reverse-engineering large existing software systems into evidence-backed documentation that is useful to both humans and coding agents.

The skill is designed for systems where understanding is spread across source code, microservices, batch jobs, APIs, databases, statuses, files/events, integrations, tests, operational procedures, existing documents, and experienced engineers.

## What it does

The skill follows this workflow:

```text
Frame system
    -> approve scope
    -> map selected module
    -> approve decomposition
    -> reverse engineer progressively
    -> interview domain experts
    -> verify evidence
    -> write canonical Markdown
    -> publish/validate with docmd
```

It deliberately separates **system understanding** from **documentation presentation**.

- `system-reverse-engineer` owns discovery, interviewing, hierarchy, evidence and technical completeness.
- `docmd` and its official agent skill own the documentation site, navigation, Mermaid presentation, search, OKF/agent outputs, MCP integration, validation and build mechanics.

## Key principles

- Never assume the requested module is the whole system.
- `Module != Flow`.
- Establish `System -> Module -> Capability -> Flow -> Subflow -> Processing Step -> Technical Component` before deep investigation.
- Require user approval of system/module scope.
- Require another approval of the selected module's capability/flow decomposition.
- Anything not approved is strictly `OUT_OF_SCOPE`.
- Combine code evidence, existing authoritative artifacts and domain-expert interviews.
- Never present inference as fact.
- Keep unknowns and conflicts explicit.
- Decompose large flows and checkpoint progress so another session can resume safely.
- Use sub-agents for bounded independent investigations when supported; one coordinator owns canonical knowledge.
- Human-facing documentation is mandatory. Agent knowledge alone is not completion.
- Markdown is canonical so the same knowledge can serve humans, Claude/Gemini, Copilot/Notebook and other agents.

## Documentation platform prerequisite

This skill uses **docmd** for human and agent-facing publication.

Before documentation generation, the agent checks for:

1. a usable docmd CLI/runtime
2. the official docmd agent skill/instructions

If the repository already contains a docmd project, it is reused.

If docmd or its official skill is unavailable, the agent stops and asks the user to configure it. It must **not** silently fall back to Docusaurus or invent another documentation framework.

The Markdown source remains directly usable even when docmd MCP is not enabled. MCP is an optional agent access path rather than the source of truth.

## What each documented module should contain

Every approved module becomes an independently useful technical handbook. Where applicable it covers:

- Overview and terminology
- Architecture and component responsibilities
- Capabilities
- Business flows and subflows
- Processing timeline and dependencies
- State/status transitions
- Data model and important table schemas
- Batch jobs and steps
- APIs
- Integrations
- Files, events and messaging
- Business rules
- Variants and branches
- Error handling
- Recovery and reprocessing
- Testing and test-data setup
- Operations and troubleshooting
- Architecture decisions/rationale
- Code map and important entry points

A material category should be documented, marked `NOT_APPLICABLE`, or identified as `UNKNOWN`; it should not silently disappear.

## Evidence model

Material knowledge is classified as:

- `CODE_VERIFIED`
- `DOCUMENT_VERIFIED`
- `USER_CONFIRMED`
- `INFERRED`
- `UNKNOWN`
- `CONFLICT`

`INFERRED` information cannot become authoritative documentation until it is verified or confirmed.

If code and user/domain knowledge disagree, the skill preserves both as a `CONFLICT` and investigates instead of silently choosing one.

## Scope model

Documentation coverage is tracked separately:

- `DOCUMENTED`
- `IN_PROGRESS`
- `TODO`
- `OUT_OF_SCOPE`

An out-of-scope module may appear as a verified dependency boundary, but the agent must not investigate its internals without explicit scope expansion.

## Example

If the user says:

```text
Document Outward Clearing.
```

The skill must **not** interpret Outward Clearing as the entire application or as one flow.

It first establishes something like:

```text
Cheque Clearing Platform
|- Inward Clearing       OUT_OF_SCOPE
|- Outward Clearing      IN_SCOPE
|- Cheque Book           OUT_OF_SCOPE
|- Inventory             OUT_OF_SCOPE
|- Reports               OUT_OF_SCOPE
`- Data Migration        OUT_OF_SCOPE
```

After user approval, it discovers candidate capabilities inside Outward Clearing and asks for another approval before deep reverse engineering.

## User interviewing

The skill interviews the domain expert whenever code cannot reliably establish business or operational truth, including:

- business meaning and terminology
- ordering and gates between processes
- status meaning
- variants and branching rules
- manual/operator activities
- recovery/reprocessing
- testing practices
- troubleshooting
- historical rationale and design decisions

Questions should be focused and preferably asked one at a time. Answers are stored as `USER_CONFIRMED` knowledge and cross-checked against implementation where applicable.

## Status and data modelling

Statuses are first-class knowledge. The skill traces actual writes, reads, conditions, consumers and side effects rather than generating a state machine from an enum.

Important tables/entities are documented with their purpose, ownership, important keys/columns, relationships, lifecycle, readers/writers, relevant flows and source evidence rather than as raw schema dumps.

Mermaid diagrams are used where they improve understanding, including architecture, flow, sequence, state-transition and ER diagrams. Large systems use progressive drill-down instead of giant diagrams.

## Testing and operations

Documentation should help a future engineer safely modify and validate the system. Where applicable it captures:

- prerequisites and configuration
- test-data setup
- how to trigger jobs/APIs/flows
- expected statuses/results
- database verification
- mocks/stubs and existing tests
- integration testing approach
- failure identification
- safe recovery/reprocessing
- troubleshooting entry points

If this cannot be determined from evidence, the agent asks the user instead of inventing a procedure.

## Checkpoints and sub-agents

Large systems are processed incrementally. Checkpoints preserve system framing, approved scope, approved decomposition, completed/in-progress work, open questions, unknowns, conflicts and important user confirmations.

When sub-agents are supported, they may investigate independent bounded questions such as job discovery, schema usage, APIs, integrations or status writes. They return evidence-backed findings; the coordinator reconciles and writes canonical documentation.

## Completion criteria

The task is not complete merely because an agent knowledge/index artifact exists.

For the requested scope, completion requires the relevant system/module framing and decomposition to be approved, technical documentation to be produced, important unknowns/conflicts to be reported, human Markdown pages and useful diagrams to exist, and docmd validation/build to succeed when tooling is available.

## Repository contents

```text
system-reverse-engineer/
|- SKILL.md
|- README.md
`- references/
   `- framework-discovery.md
```

`SKILL.md` contains the workflow and hard behavioral rules. `references/framework-discovery.md` contains additional framework-aware discovery guidance, including Spring Boot/Spring Batch patterns.

## Installation

Copy or clone this directory into the skills location supported by your agent runtime. The skill itself does not depend on this GitHub repository at runtime.

For restricted/offline environments, copy the skill and configure docmd using whatever installation method is approved by your organization.

## Example prompts

```text
Use system-reverse-engineer to document this application with me.
```

```text
Document Outward Clearing only. Interview me when business behavior cannot be established from the code.
```

```text
Continue from the last documentation checkpoint.
```

```text
I changed this processing flow. Update only the affected system documentation.
```

## Proprietary systems

Use the skill only with repositories, AI tooling and infrastructure approved by your organization. The skill is designed to operate beside the source repository; project knowledge does not need to be published to this public repository.
