# Investigation and Delegation Guide

## Goal
Gather evidence efficiently without turning discovery into uncontrolled browsing.

## Plan one bounded flow
Before investigating, write the question the flow analysis must answer in one sentence. Then identify independent evidence tracks.

Common tracks:
- trigger and technical entry point
- main execution path
- status reads/writes and transitions
- business rules/branch conditions
- integrations and dependency contracts
- important persistence usage
- failures, retries, reconciliation, manual recovery

## Sub-agent rule
When the host supports sub-agents and at least two tracks are independent, delegate them in parallel.

Good delegation:
- one agent traces statuses
- one traces the entry/execution path
- one traces external integrations

Bad delegation:
- several agents all broadly “understand the module”
- asking sub-agents to write final documentation
- delegating business interpretation without reconciliation

Sub-agent output should be evidence notes containing:
- finding
- evidence location
- evidence state
- uncertainty/conflict
- questions raised

The coordinator owns scope, interviews, interpretation, narrative, Mermaid, checkpoints, and canonical files.

## Deterministic before generative
Prefer direct code/search/static evidence for structural questions. Spend strong-model reasoning on sequence, meaning, contradictions, and cross-component synthesis.

## Reconciliation
After investigation, merge duplicate findings and resolve disagreements. Never average contradictory claims. Preserve `CONFLICT` until verified.

Build a provisional flow model:
`purpose -> trigger -> stages -> branches -> statuses -> dependencies -> outcome -> next flow`

Only after this model is coherent should the interview stage begin.
