# Knowledge Model and Graph Reference

Use this reference when creating, updating, validating, or querying the machine-readable system knowledge graph.

## Purpose

The knowledge graph is a **small navigational and impact-analysis model** over the same verified knowledge documented for humans. It is not a second documentation system and must never become an independent source of truth.

Canonical business/technical explanations remain in Markdown/MDX. The graph provides stable identities and typed relationships so agents can quickly answer questions such as:

- Which flows use this job?
- Which jobs write this table?
- What can change this status?
- Which APIs participate in this capability?
- What is affected if this integration changes?
- Where should an agent read next to understand this component?

## Storage

Recommended location:

```text
documentation/
|- docs/                    # canonical human-readable Markdown/MDX
|- knowledge/
|  |- graph.yaml            # compact node/edge graph
|  `- README.md             # optional schema/version note
|- checkpoints/
`- AGENT_INDEX.md
```

For very large systems, split `graph.yaml` by module only when needed for maintainability, while keeping a small top-level index. Do not prematurely create hundreds of graph files.

## Hierarchy

The conceptual hierarchy is:

```text
System
  -> Module
      -> Capability
          -> Flow
              -> Subflow
                  -> ProcessingStep
                      -> TechnicalComponent
```

This hierarchy must reflect the user-approved framing/decomposition. Code/package structure must not silently redefine it.

## Core Node Types

Use only types that materially improve navigation/impact analysis:

- `SYSTEM`
- `MODULE`
- `CAPABILITY`
- `FLOW`
- `SUBFLOW`
- `PROCESSING_STEP`
- `SERVICE`
- `COMPONENT`
- `JOB`
- `JOB_STEP`
- `API`
- `STATUS`
- `ENTITY`
- `TABLE`
- `EVENT`
- `TOPIC`
- `FILE_INTERFACE`
- `INTEGRATION`
- `EXTERNAL_SYSTEM`
- `BUSINESS_RULE`
- `TEST`
- `RUNBOOK`
- `DECISION`

Do not model every class/method as a graph node. Source code remains the detailed implementation graph.

## Core Relationship Types

Prefer a controlled relationship vocabulary:

### Hierarchy

- `HAS_MODULE`
- `HAS_CAPABILITY`
- `HAS_FLOW`
- `HAS_SUBFLOW`
- `HAS_STEP`

### Participation / implementation

- `IMPLEMENTED_BY`
- `USES_JOB`
- `USES_API`
- `USES_COMPONENT`
- `USES_INTEGRATION`
- `TESTED_BY`
- `OPERATED_BY`

### Data

- `OWNS`
- `READS`
- `WRITES`
- `RELATES_TO`

### State

- `SETS_STATUS`
- `READS_STATUS`
- `TRANSITIONS_TO`
- `TRIGGERED_BY`

### Communication

- `CALLS`
- `PUBLISHES`
- `CONSUMES`
- `SENDS_FILE_TO`
- `RECEIVES_FILE_FROM`
- `INTEGRATES_WITH`

### Knowledge / rationale

- `GOVERNED_BY`
- `DECIDED_BY`
- `DEPENDS_ON`

Use the most specific meaningful relationship. Avoid vague edges such as `RELATED_TO` unless no stronger relationship can be established.

## Stable IDs

Every node needs a stable, human-readable ID independent of filenames and Java class renames where possible.

Recommended pattern:

```text
<type>:<module-or-system>:<slug>
```

Examples:

```text
system:cheque-clearing
module:cheque-clearing:outward
flow:outward:file-ingestion
job:outward:clearing-job
table:outward:cheque-item
status:outward:ready
integration:outward:clearing-network
```

Do not use database IDs, generated UUIDs, line numbers, or absolute filesystem paths as canonical node IDs.

## Node Schema

Recommended YAML shape:

```yaml
version: 1
nodes:
  - id: module:cheque-clearing:outward
    type: MODULE
    name: Outward Clearing
    scope: IN_SCOPE
    coverage: DOCUMENTED
    doc: docs/modules/outward/index.md
    evidence:
      - state: USER_CONFIRMED
        reference: "Approved during system framing"

  - id: job:outward:clearing-job
    type: JOB
    name: Clearing Job
    doc: docs/modules/outward/jobs/clearing-job.md
    source:
      - path: outward-service/src/main/java/.../ClearingJobConfig.java
        symbol: clearingJob
    evidence:
      - state: CODE_VERIFIED
        reference: outward-service/src/main/java/.../ClearingJobConfig.java
```

Keep node summaries short. Detailed explanations belong in the linked Markdown page.

## Edge Schema

```yaml
edges:
  - from: flow:outward:file-ingestion
    type: USES_JOB
    to: job:outward:ingestion-job
    evidence:
      state: CODE_VERIFIED
      reference: outward-service/src/main/java/.../IngestionJobConfig.java

  - from: job:outward:ingestion-job
    type: SETS_STATUS
    to: status:outward:ready
    evidence:
      state: CODE_VERIFIED
      reference: outward-service/src/main/java/.../IngestionWriter.java
```

Relationships are facts too. Every material edge requires provenance.

## Evidence States

Use the same evidence contract as the main skill:

- `CODE_VERIFIED`
- `DOCUMENT_VERIFIED`
- `USER_CONFIRMED`
- `INFERRED`
- `UNKNOWN`
- `CONFLICT`

`INFERRED` edges may exist temporarily during discovery but must be clearly marked and must not be rendered as established architecture/state behavior.

Do not create a relationship merely because two classes share a name, package, table, enum, or configuration prefix.

## Scope and Coverage

Node scope/coverage must remain separate from evidence.

Coverage values:

- `DOCUMENTED`
- `IN_PROGRESS`
- `TODO`
- `OUT_OF_SCOPE`

An out-of-scope node may exist only to represent a known boundary. Example:

```yaml
- id: module:cheque-clearing:reports
  type: MODULE
  name: Reports
  scope: OUT_OF_SCOPE
```

An in-scope integration edge may point to it, but the graph must not contain reverse-engineered internal jobs/tables/flows for that module unless scope is expanded.

## Status Transition Modeling

State transitions require stronger modeling than ordinary enum membership.

A `TRANSITIONS_TO` edge should include transition context:

```yaml
- from: status:outward:received
  type: TRANSITIONS_TO
  to: status:outward:validated
  context:
    entity: entity:outward:cheque-item
    trigger: "Validation succeeds"
    setter: component:outward:validation-processor
  evidence:
    state: CODE_VERIFIED
    reference: outward-service/src/main/java/.../ValidationProcessor.java
```

Do not create all pairwise status edges from an enum. Trace actual setters, conditions, queries, consumers and tests.

## Table / Data Modeling

Represent important business entities and physical tables separately when that distinction matters:

```text
ENTITY --IMPLEMENTED_BY--> TABLE
FLOW   --READS-----------> TABLE
JOB    --WRITES----------> TABLE
```

Do not model every column as a node. Important columns belong in the table's Markdown documentation. Create graph nodes only for cross-cutting concepts such as statuses when useful.

## Graph vs Markdown

The graph answers **where and what is connected**.

Markdown answers **how, why and what exactly happens**.

Example:

```text
Graph:
Outward Ingestion -> USES_JOB -> IngestionJob -> WRITES -> CHEQUE_ITEM

Markdown:
Why ingestion exists, trigger, file format, validations, step-by-step processing,
important columns, error behavior, recovery, testing and implementation references.
```

Never move rich explanations exclusively into graph metadata.

## AGENT_INDEX Integration

`AGENT_INDEX.md` is the agent's cheap entry point. It should link to:

- system/module map
- graph location
- current documentation coverage
- module overview docs
- checkpoint/resume state
- glossary

Recommended agent navigation:

```text
AGENT_INDEX.md
  -> knowledge/graph.yaml
      -> relevant node.doc
          -> source evidence/code only when needed
```

Agents should not load the entire documentation corpus or source tree for every question.

## Impact Analysis

For a proposed code change, use graph traversal as a candidate-impact mechanism, not proof.

Example:

```text
STATUS
  <- SETS_STATUS - JOB
  <- READS_STATUS - JOB
  <- READS_STATUS - API
  <- TRANSITIONS_TO/FROM - STATUS
  <- referenced by - FLOW
```

The graph identifies likely affected areas. The agent must still inspect current code before changing behavior or documentation.

Never claim "only these components are affected" solely because the graph contains only those edges.

## Maintenance Rules

When verified documentation changes:

1. update the canonical Markdown/MDX
2. update affected graph nodes/edges
3. preserve stable IDs where the concept is unchanged
4. update evidence when implementation moves
5. remove obsolete relationships only after verifying they no longer exist
6. preserve unresolved conflicts until resolved
7. validate that every graph doc path exists
8. validate that every edge endpoint exists
9. checkpoint the change

If code changes but documentation has not yet been verified, mark impacted graph knowledge `IN_PROGRESS`/`UNKNOWN` rather than pretending the old model is current.

## Validation Checklist

Before declaring a module complete:

- every graph node has a unique ID
- every edge references existing nodes
- important nodes link to canonical docs
- material edges have evidence
- no `INFERRED` relationship is rendered as verified behavior
- out-of-scope internals were not modeled
- approved hierarchy matches the graph
- major flows connect to their jobs/APIs/integrations/data/statuses
- important jobs/APIs are connected back to business flows
- status transitions are based on actual evidence
- graph paths and documentation links resolve

## Anti-Patterns

Do not:

- create a second prose documentation tree inside `knowledge/`
- model every Java class/method
- use package hierarchy as the business graph
- create edges from naming similarity alone
- duplicate entire Markdown pages in YAML
- treat graph completeness as proof of system completeness
- let sub-agents independently rewrite the canonical graph
- follow out-of-scope nodes into their internals
- regenerate stable IDs on every run

The coordinator owns canonical graph updates after reconciling sub-agent findings.