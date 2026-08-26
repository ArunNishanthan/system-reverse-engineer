# Knowledge Model

Use this reference when initializing or updating the canonical machine-readable knowledge layer.

## Principles

- Keep `index.yaml` small enough for an agent to read at session start.
- Detailed files are normalized and loaded on demand.
- Stable IDs connect nodes; human names may change.
- Every material factual relationship has provenance.
- Evidence belongs near the claim or via a stable evidence ID.
- Do not copy large source-code excerpts into knowledge files.
- Knowledge files describe system semantics and navigation, not implementation source.

## Scope

Suggested `knowledge/scope.yaml`:

```yaml
version: 1
capabilities:
  inward-clearing:
    coverage: IN_PROGRESS
    include: true
  reports:
    coverage: OUT_OF_SCOPE
    include: false
    reason: Deferred by documentation owner
rules:
  default_unspecified: OUT_OF_SCOPE
```

The user controls scope. Never convert an excluded capability to included merely because code references it.

## Index

Suggested `knowledge/index.yaml`:

```yaml
version: 1
system:
  id: cheque-platform
  name: Cheque Platform
scope: scope.yaml
domains:
  - id: inward-clearing
    file: domains/inward-clearing.yaml
flows:
  - id: micr-ingestion
    domain: inward-clearing
    file: flows/micr-ingestion.yaml
statuses:
  - entity: cheque
    file: statuses/cheque.yaml
components:
  - id: inward-debit-job
    file: components/inward-debit-job.yaml
open_questions: ../questions/open.md
resume: ../checkpoints/resume.yaml
```

Keep summaries short. Do not place entire flow definitions here.

## Evidence States

Use exactly these semantic states unless the project explicitly extends them:

```text
CODE_VERIFIED
DOCUMENT_VERIFIED
USER_CONFIRMED
INFERRED
UNKNOWN
CONFLICT
```

Example code evidence:

```yaml
evidence:
  state: CODE_VERIFIED
  sources:
    - type: source
      path: services/inward/src/main/java/example/DebitProcessor.java
      symbol: DebitProcessor.process
      note: Sets DEBIT_SUCCESS after successful downstream response
```

Example user evidence:

```yaml
evidence:
  state: USER_CONFIRMED
  sources:
    - type: interview
      question: What business step gates debit after ingestion?
      answer: Reconciliation must complete successfully before debit starts.
      confirmed_by: domain-expert
      date: 2026-08-26
```

Do not invent a person's identity if it was not supplied. `domain-expert` is sufficient.

## Domain

```yaml
id: inward-clearing
name: Inward Clearing
coverage: IN_PROGRESS
purpose:
  text: Cheques presented by another institution against accounts in this bank.
  evidence:
    state: USER_CONFIRMED
flows:
  - micr-ingestion
  - reconciliation
  - debit-processing
  - icca-processing
variants:
  - small-cheque
  - large-cheque
out_of_scope_dependencies:
  - id: reports
    boundary: reporting event
```

Do not include example values as facts in a real project unless verified.

## Flow

```yaml
id: debit-processing
name: Debit Processing
domain: inward-clearing
coverage: IN_PROGRESS
parent_flow: inward-clearing-e2e
previous:
  - reconciliation
next:
  - icca-processing
triggers: []
components:
  - inward-debit-job
reads: []
writes: []
integrations: []
statuses: []
variants: []
unknowns: []
evidence: []
```

A `previous`/`next` edge is a factual relationship and needs evidence. If not verified, keep it in `hypotheses` instead:

```yaml
hypotheses:
  - claim: icca-processing follows debit-processing
    state: INFERRED
    reason: Naming and timestamps suggest ordering, but no gate has been established.
```

## Status Model

Statuses require more rigor than enums.

```yaml
entity: cheque
statuses:
  - id: DEBIT_PENDING
    meaning:
      text: Awaiting debit processing
      evidence:
        state: USER_CONFIRMED
    producers:
      - component: reconciliation-job
        evidence:
          state: CODE_VERIFIED
    consumers:
      - component: debit-job
        evidence:
          state: CODE_VERIFIED
transitions:
  - from: DEBIT_PENDING
    to: DEBIT_SUCCESS
    trigger: successful debit response
    variants: []
    side_effects: []
    evidence:
      state: CODE_VERIFIED
```

If only the enum is known:

```yaml
- id: DEBIT_PENDING
  meaning:
    state: UNKNOWN
```

Do not manufacture a meaning from the name.

## Component

```yaml
id: inward-debit-job
type: batch-job
name: InwardDebitJob
service: inward-processing
business_flows:
  - debit-processing
entry_points: []
reads: []
writes: []
integrations: []
status_reads: []
status_writes: []
source_locations: []
evidence: []
```

Useful component types include `service`, `api`, `batch-job`, `scheduler`, `consumer`, `producer`, `repository`, `table`, `collection`, `file-interface`, and `external-system`. Do not force a component into a type that does not fit.

## Decision/Rationale

Capture deliberate architectural or operational choices separately from implementation facts:

```yaml
id: no-automatic-retry-for-x
decision: Do not automatically retry downstream X.
rationale: Downstream eventually responds through reconciliation and automatic retry can duplicate processing.
status: active
evidence:
  state: USER_CONFIRMED
related:
  flows: [some-flow]
  components: [some-component]
```

This is especially valuable to future coding agents because a seemingly missing mechanism may be deliberate.

## Conflicts

```yaml
claim: Debit starts immediately after ingestion
state: CONFLICT
sources:
  - state: USER_CONFIRMED
    statement: Reconciliation gates debit.
  - state: CODE_VERIFIED
    statement: Scheduler appears capable of selecting READY records directly.
resolution: null
```

Do not resolve a conflict by majority vote or model confidence. Investigate or ask.

## Resume Checkpoint

Keep `checkpoints/resume.yaml` compact:

```yaml
version: 1
current_domain: inward-clearing
current_flow: debit-processing
completed:
  - micr-ingestion
  - reconciliation
in_progress:
  - debit-processing
unexplored:
  - icca-processing
open_questions:
  - id: q-17
    text: What gates debit after reconciliation?
conflicts: []
last_checkpoint: 2026-08-26T12:00:00+08:00
```

The resume file is navigation, not history. Store durable discoveries in canonical knowledge files.

## Checkpoint Transaction

A checkpoint should conceptually happen in this order:

1. write/update detailed knowledge nodes
2. update index if nodes were added/removed
3. update open questions/conflicts
4. update coverage/scope if changed
5. update `resume.yaml` last

This reduces the chance that resume state claims work is saved when canonical knowledge is not.

## Structural Validation

Where scripting/tooling is permitted, validate at least:

- YAML/JSON parses
- unique IDs
- all index file references exist
- graph edges reference known nodes or explicit out-of-scope boundaries
- evidence paths are syntactically valid
- coverage values are valid
- evidence states are valid
- no authoritative rendered fact points only to `INFERRED`
- no out-of-scope node has deep internal knowledge accidentally generated
- documentation links resolve

Structural validation cannot prove business semantics. Keep semantic verification evidence-driven.
