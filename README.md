# System Reverse Engineer

An Agent Skill for reverse-engineering large existing software systems into evidence-backed documentation useful to both humans and coding agents.

The skill is designed for systems where understanding is spread across source code, microservices, batch jobs, APIs, databases, statuses, files/events, integrations, tests, operational procedures, existing documents, and experienced engineers.

## Workflow

```text
Frame system
    -> approve scope
    -> map selected module
    -> approve decomposition
    -> reverse engineer progressively
    -> interview domain experts
    -> verify evidence
    -> write canonical Markdown/MDX
    -> publish and validate with Docusaurus
```

Docusaurus is the human-facing shell. Markdown/MDX remains the canonical documentation so coding agents can read the same knowledge directly from the repository.

## Key principles

- Never assume the requested module is the whole system.
- `Module != Flow`.
- Establish `System -> Module -> Capability -> Flow -> Subflow -> Processing Step -> Technical Component` before deep investigation.
- Require user approval of system/module scope.
- Require another approval of the selected module's capability/flow decomposition.
- Anything not approved is strictly `OUT_OF_SCOPE`.
- Combine code evidence, authoritative artifacts and domain-expert interviews.
- Never present inference as fact.
- Keep unknowns and conflicts explicit.
- Decompose large flows and checkpoint progress so later sessions can resume safely.
- Use sub-agents for bounded independent investigations when supported; one coordinator owns canonical documentation.
- Human-facing documentation is mandatory. Agent notes alone are not completion.

## Docusaurus prerequisite

The skill uses **Docusaurus** for human-facing publication.

If a working Docusaurus site already exists under the repository documentation area, the agent reuses it rather than rebuilding it.

If no site exists, the agent initializes a minimal Docusaurus setup using versions/packages available and approved in the environment, then immediately verifies that the site builds before beginning large-scale documentation work.

If Docusaurus tooling is unavailable, the agent stops and asks the user to configure/provide it. It does not silently switch documentation platforms.

Docusaurus setup is infrastructure, not the reverse-engineering task. The skill deliberately avoids unnecessary frontend customization.

## Module documentation contract

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

A material category is documented, marked `NOT_APPLICABLE`, or identified as `UNKNOWN`; it should not silently disappear.

## Evidence model

Material knowledge is classified as:

- `CODE_VERIFIED`
- `DOCUMENT_VERIFIED`
- `USER_CONFIRMED`
- `INFERRED`
- `UNKNOWN`
- `CONFLICT`

`INFERRED` information cannot become authoritative documentation until verified or confirmed. Conflicting code/user/document evidence is preserved as `CONFLICT` and investigated rather than silently resolved.

## Scope model

Coverage is tracked separately:

- `DOCUMENTED`
- `IN_PROGRESS`
- `TODO`
- `OUT_OF_SCOPE`

An out-of-scope module may appear as a verified dependency boundary, but its internals must not be investigated without explicit scope expansion.

## Example

If the user says:

```text
Document Outward Clearing.
```

The skill must not interpret Outward Clearing as the entire application or as one flow. It first establishes something like:

```text
Cheque Clearing Platform
|- Inward Clearing       OUT_OF_SCOPE
|- Outward Clearing      IN_SCOPE
|- Cheque Book           OUT_OF_SCOPE
|- Inventory             OUT_OF_SCOPE
|- Reports               OUT_OF_SCOPE
`- Data Migration        OUT_OF_SCOPE
```

After user approval, it discovers candidate capabilities/flows inside Outward Clearing and asks for another approval before deep reverse engineering.

## User interviewing

The skill interviews the domain expert whenever code cannot reliably establish business or operational truth, including business meaning, ordering/gates, statuses, variants, manual activities, recovery, testing practices, troubleshooting and historical rationale.

Questions should be focused and preferably asked one at a time. Answers become `USER_CONFIRMED` knowledge and are cross-checked against implementation where applicable.

## Status and data modelling

Statuses are first-class knowledge. The skill traces actual writes, reads, conditions, consumers and side effects rather than generating a state machine from an enum.

Important tables/entities are documented with purpose, ownership, keys/important columns, relationships, lifecycle, readers/writers, relevant flows and source evidence rather than as raw schema dumps.

## Human documentation

Docusaurus navigation is organized by business module rather than repository package structure.

Use Markdown/MDX and Mermaid for architecture, flows, sequences, status/state transitions, ER models and integration/dependency diagrams. Large modules use progressive drill-down instead of giant diagrams.

Prefer standard Docusaurus features such as admonitions, tabs and details before custom React components. Add custom components only when a repeated high-value interaction genuinely improves understanding.

Keep color semantic and consistent, and keep documentation understandable without animation or color alone.

## Agent usage

Agents consume the same canonical Markdown/MDX used by humans. Maintain a small entry point such as `documentation/AGENT_INDEX.md` containing the system/module map, documentation coverage, links to module overview pages, checkpoint location and key references.

Do not maintain a second full agent-only knowledge tree that can drift away from the human documentation.

## Testing and operations

Documentation should help a future engineer safely modify and validate the system. Where applicable it captures prerequisites/configuration, test-data setup, how to trigger jobs/APIs/flows, expected results/statuses, DB verification, mocks/stubs, existing tests, integration testing, failure identification, recovery and troubleshooting.

If evidence cannot establish the real procedure, the agent asks the user rather than inventing one.

## Checkpoints and sub-agents

Large systems are processed incrementally. Checkpoints preserve system framing, approved scope/decomposition, completed/in-progress work, open questions, unknowns, conflicts and important user confirmations.

When sub-agents are supported, they may investigate independent bounded questions such as jobs, schemas, APIs, integrations or status writes. They return evidence-backed findings; the coordinator reconciles and writes canonical documentation.

## Completion criteria

The task is not complete because discovery files or agent notes exist.

For the approved scope, completion requires the relevant hierarchy/decomposition to be approved, technical documentation to be produced, important unknowns/conflicts reported, human Markdown/MDX pages and useful diagrams to exist, navigation/cross-links to be valid, the agent index to point to the same canonical documentation, and the Docusaurus build to succeed.

## Repository contents

```text
system-reverse-engineer/
|- SKILL.md
|- README.md
`- references/
   `- framework-discovery.md
```

`SKILL.md` contains the workflow and hard behavioral rules. `references/framework-discovery.md` contains framework-aware discovery guidance including Spring Boot/Spring Batch patterns.

## Installation

Copy or clone this directory into the skills location supported by your agent runtime. The skill itself does not depend on this GitHub repository at runtime.

For restricted/offline environments, copy the skill and use the Docusaurus dependencies/toolchain approved and available inside that environment.

## Example prompts

```text
Use system-reverse-engineer to document this application with me.
```

```text
Document Outward Clearing only. Interview me when business behavior cannot be established from code.
```

```text
Continue from the last documentation checkpoint.
```

```text
I changed this processing flow. Update only the affected system documentation.
```

## Proprietary systems

Use the skill only with repositories, AI tooling and infrastructure approved by your organization. The skill is designed to operate beside the source repository; project knowledge does not need to be published to this public repository.
