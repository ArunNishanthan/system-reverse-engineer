# System Reverse Engineer

An Agent Skill for evidence-driven reverse engineering and living documentation of complex existing software systems.

It is intended for systems where useful knowledge is spread across source code, multiple services, batch jobs, APIs, databases, statuses, files/events, operational behavior, existing artifacts, and the heads of experienced engineers.

## Core ideas

- The user chooses documentation scope before deep discovery.
- Unselected capabilities remain strictly out of scope.
- Code, documents, and domain-expert interviews are combined.
- Unknowns stay unknown instead of being filled with plausible AI-generated behavior.
- Large flows are decomposed and checkpointed so work can continue across sessions.
- Sub-agents can investigate independent bounded questions, while one coordinator owns canonical knowledge.
- A compact knowledge graph helps future coding agents navigate the system quickly.
- Docusaurus + MDX + Mermaid provide the default human-facing documentation experience.
- Statuses, variants, timelines, failures, recovery paths and business rationale are first-class knowledge.

## Skill contents

```text
SKILL.md
references/
  knowledge-model.md
  docusaurus-visuals.md
  framework-discovery.md
```

`SKILL.md` is the skill entry point. References are loaded when the task needs deeper schema, visualization, or framework-specific discovery guidance.

## Installation

The repository itself follows the portable Agent Skills layout. Copy or clone it into the skills location supported by your agent runtime.

Common layouts include a directory containing:

```text
system-reverse-engineer/
  SKILL.md
  references/
```

Claude Code supports project/user skills, and agent runtimes may also support a shared `.agents/skills/` location. Use the current documentation for your CLI/runtime for its preferred skill path.

For an office environment with no internet access, copy this entire directory into the approved local skills location. The skill does not depend on this GitHub repository at runtime.

## Example usage

Fresh codebase:

```text
Use system-reverse-engineer to document this application with me.
```

The skill should first detect whether a documentation knowledge layer exists and ask you to establish scope before deep exploration.

Example scope answer:

```text
Document inward clearing, outward clearing, cheque book and inventory.
Reports and data migration are out of scope.
```

Continuing later:

```text
Continue reverse engineering inward clearing from the last checkpoint.
```

Focused investigation:

```text
Document debit processing. Interview me whenever the business behavior cannot be established from evidence.
```

Maintenance:

```text
I changed the debit processing flow. Update the affected system knowledge and documentation.
```

## Expected target-project layout

The skill can initialize a package similar to:

```text
<project-root>/
├── <microservices...>/
├── documentation/
│   ├── knowledge/
│   │   ├── index.yaml
│   │   ├── scope.yaml
│   │   ├── domains/
│   │   ├── flows/
│   │   ├── statuses/
│   │   ├── components/
│   │   ├── integrations/
│   │   ├── decisions/
│   │   └── evidence/
│   ├── checkpoints/
│   ├── questions/
│   ├── docs/
│   └── src/components/
└── [agent instruction file]
```

The exact layout should respect existing repository conventions.

## Evidence model

The skill distinguishes:

- `CODE_VERIFIED`
- `DOCUMENT_VERIFIED`
- `USER_CONFIRMED`
- `INFERRED`
- `UNKNOWN`
- `CONFLICT`

`INFERRED` information is not authoritative documentation. It must be verified or confirmed first.

## Documentation coverage

Coverage is tracked independently:

- `DOCUMENTED`
- `IN_PROGRESS`
- `TODO`
- `OUT_OF_SCOPE`

This makes intentional omissions visible and prevents an agent from expanding into modules that were deliberately excluded.

## Visual documentation

The default visual strategy combines Mermaid with reusable interactive MDX/React views such as:

- Flow Explorer
- Status Explorer
- Variant Explorer
- Processing Timeline
- Knowledge Graph
- Failure Explorer

The skill intentionally prefers progressive drill-down over giant diagrams and uses semantic color rather than decoration.

## Safety for proprietary systems

Run the skill only with AI tooling, repositories, source code, and infrastructure approved by your organization. The skill is designed to operate locally beside a codebase; it does not require sending project knowledge to this public repository.
