# System Reverse Engineer

An Agent Skill for turning a large existing software system into an evidence-backed **LLM-ready technical knowledge pack** that is also readable by humans like a coherent technical book.

It is intended for complex brownfield systems where important understanding is distributed across source code, batch jobs, APIs, statuses, integrations, existing artifacts and experienced engineers.

## What it optimizes for

The primary goal is not to generate a documentation website or exhaustive code reference.

The goal is that a new developer can:

- understand the system progressively from a clear starting point
- understand modules and their end-to-end business flows
- see where each flow enters the implementation
- visually follow processing using Mermaid
- understand important status lifecycles
- preserve business rules and important implementation decisions
- know where to start when modifying a flow
- ask an LLM grounded questions over the same Markdown knowledge

## Output

The skill produces platform-independent Markdown, Mermaid diagrams, a lightweight local knowledge graph and resumable checkpoints.

A typical project knowledge pack looks like:

```text
documentation/
  START_HERE.md
  SYSTEM_OVERVIEW.md
  GLOSSARY.md
  modules/
    <module>/
      OVERVIEW.md
      ARCHITECTURE.md
      flows/
        <flow>.md
      STATUSES.md
      BUSINESS_RULES.md
      DECISIONS.md
      CHANGE_GUIDE.md
  knowledge/
    graph.yaml
  checkpoints/
    current.md
  AGENT_INDEX.md
```

Files are created only when they add value; the skill does not generate empty boilerplate pages.

The same knowledge can be consumed directly by humans, CLI coding agents, Copilot/Notebook-style tools, RAG systems, IDEs or a future documentation UI.

## Core workflow

1. Frame the overall system.
2. Agree which modules/capabilities are in scope.
3. Discover candidate capabilities and flows inside the selected module.
4. Get the domain expert to approve/correct the decomposition.
5. Establish the narrative/processing order.
6. Reverse engineer one bounded flow at a time.
7. Interview the domain expert where code cannot explain business meaning or rationale.
8. Write verified canonical Markdown in reading order.
9. Update the lightweight knowledge graph and agent index.
10. Checkpoint continuously so later sessions can resume.

## Documentation reads like a book

The skill deliberately avoids producing a pile of independent reference pages.

The intended reading journey is conceptually:

**System overview -> Module overview -> End-to-end journey -> Flow 1 -> Flow 2 -> ... -> Status lifecycle -> Important rules/decisions -> Developer change guidance**

`START_HERE.md` provides the overall reading path. Each module overview explains its flow order. Flow pages explain what happens before and after them and point readers toward the next logical concept.

Technical inventories such as jobs, APIs, tables and classes are supporting information rather than the primary narrative.

## Flow documentation

An important flow normally explains:

- purpose
- where it sits in the larger processing journey
- business trigger and technical entry point
- Mermaid visual overview
- processing walkthrough
- important business rules and variants
- important status progression
- architecture/components needed to understand the flow
- important implementation decisions
- where a developer should start when changing it
- material failure/recovery behavior
- what to read next

The skill avoids filling pages with ordinary source-code snippets. It points to implementation entry points and uses code snippets only when a small piece of code is genuinely necessary to explain unusual behavior.

## Mermaid only

All actual diagrams must use Mermaid.

This includes architecture, end-to-end journeys, flowcharts, sequence diagrams, status/state transitions, integration relationships and ER/data diagrams when needed.

**ASCII/text-art diagrams are prohibited.**

Large diagrams are decomposed into an overview and smaller drill-down diagrams rather than forcing an entire module into one graph.

## Status lifecycle

Statuses are first-class system knowledge.

The skill traces actual status writes, reads, predicates, consumers and conditions instead of generating a state machine from an enum.

For important statuses it captures business meaning, who sets it, why, who consumes it, verified next states, relevant flows, important side effects and known reasons processing may remain/stall there.

Mermaid state diagrams are paired with concise explanatory text/tables.

## Business and implementation knowledge

The skill interviews the domain expert to preserve knowledge that code often cannot reveal, particularly:

- business terminology and meaning
- ordering/gates between processes
- business rules and variants
- why statuses exist
- why unusual implementation decisions were made
- manual/operational behavior
- important recovery expectations
- upstream/downstream assumptions

User explanations are recorded as `USER_CONFIRMED` and cross-checked against implementation where applicable.

## Evidence model

Material knowledge uses these evidence states:

- `CODE_VERIFIED`
- `DOCUMENT_VERIFIED`
- `USER_CONFIRMED`
- `INFERRED`
- `UNKNOWN`
- `CONFLICT`

Inference is discovery material, not authoritative documentation. Important unknowns and conflicts remain visible rather than being filled with plausible-looking content.

## Scope model

Coverage is tracked separately:

- `DOCUMENTED`
- `IN_PROGRESS`
- `TODO`
- `OUT_OF_SCOPE`

Anything not explicitly approved is treated as `OUT_OF_SCOPE`. An excluded module may appear as a known boundary but its internals are not reverse engineered without scope expansion.

## Lightweight knowledge graph

The local graph exists primarily for CLI/LLM navigation and later documentation maintenance.

It stays intentionally small, focusing on concepts such as:

- System
- Module
- Capability
- Flow
- Status
- Integration
- Decision
- important Component entry points when useful

It does **not** model every table, API, job, class, method or test by default.

The graph helps an agent find the relevant flow/page and semantic relationships. Rich explanations remain in canonical Markdown.

## Agent usage

`AGENT_INDEX.md` is a cheap entry point for coding agents. It points to the system/module map, approved scope, module overview pages, graph and current checkpoint.

The intended navigation is:

**Agent index -> graph/reading path -> relevant Markdown -> source code only when needed**

This avoids repeatedly scanning the entire repository.

## Framework-aware discovery

`references/framework-discovery.md` contains additional guidance for framework-aware reverse engineering, particularly Spring Boot and Spring Batch.

The framework implementation is evidence for the business/system story; package structure is not automatically treated as the documentation hierarchy.

## Knowledge-model reference

`references/knowledge-model.md` defines the local graph conventions, evidence/provenance and maintenance behavior.

The skill deliberately keeps the graph smaller than a full source-code dependency graph.

## Checkpoints and sub-agents

Large systems are investigated incrementally. The current checkpoint preserves approved scope/decomposition/reading order, completed and in-progress work, open questions, important unknowns/conflicts, user confirmations and the recommended next action.

When the runtime supports sub-agents, they may investigate bounded independent questions after scope/decomposition are approved. The coordinator reconciles findings and owns canonical Markdown, graph and checkpoints.

## Example prompts

```text
Use system-reverse-engineer to document this application with me.
```

```text
Document Outward Clearing only. First establish how it fits into the larger system, then interview me when business behavior cannot be established from code.
```

```text
Continue from the documentation checkpoint.
```

```text
Update the documentation for this changed processing flow.
```

## Platform independence

The skill does not require Docusaurus, docmd, MkDocs or another site generator.

If a team later wants a website, the canonical Markdown can be rendered by a presentation platform without repeating the system-discovery work.

## Repository contents

```text
system-reverse-engineer/
|- SKILL.md
|- README.md
`- references/
   |- framework-discovery.md
   `- knowledge-model.md
```

## Proprietary systems

Use the skill only with repositories, AI tooling and infrastructure approved by the organization. The knowledge pack is intended to live beside the source repository and does not need to be published externally.
