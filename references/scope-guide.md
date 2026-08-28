# Scope and Dependency Boundary Guide

## Purpose
Prevent reverse engineering from expanding uncontrollably across a large system.

## Scope classes

### PRIMARY_SCOPE
The requested module/system. Investigate its business purpose, flows, statuses, rules, architecture, failures, decisions, and change guidance deeply enough for onboarding-quality documentation.

### DEPENDENCY_BOUNDARY
A separate subsystem touched by the primary scope. Investigate only what is needed to explain:
- why primary scope calls/depends on it
- when interaction occurs
- data/request/event exchanged
- expected response/outcome
- failure behavior visible to primary scope
- statuses around the boundary
- technical integration entry point

Do not reverse engineer dependency internals unless the user promotes it to primary scope.

### OUT_OF_SCOPE
Areas not needed to explain the current scope. Mention only when necessary for orientation.

## Boundary test
When traversal reaches another component, ask:
1. Does the current flow own this behavior?
2. Could this component reasonably be documented as an independent module?
3. Do we need its internals to understand the primary flow?

If 2 is yes and 3 is no, classify it as `DEPENDENCY_BOUNDARY`.

## Required stop condition
If a substantial independent subsystem is discovered, stop scope expansion and surface it:

> `<name>` appears to be a substantial independent module. For the current scope I will document only its integration contract and impact. It can be reverse engineered separately if needed.

Do not silently expand scope.

## Scope checkpoint output
Keep it short:
- Primary scope
- Dependency boundaries
- Explicit exclusions
- Open scope questions
- Proposed next flow/module to investigate
