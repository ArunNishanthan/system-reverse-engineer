# Discovery Guide

## Goal
Build the minimum verified map needed to understand a system/module before deep documentation.

## System reconnaissance
Start broad. Look for:
- deployment/service boundaries
- top-level modules/packages
- scheduled/batch jobs
- inbound APIs/events/files
- outbound integrations
- status/state definitions
- configuration revealing environments or external systems
- existing docs, runbooks, diagrams, tests, tickets, or comments

For Spring Boot/Spring Batch systems, useful anchors often include application entry points, controllers, listeners, schedulers, `Job`/`Step` configuration, readers/processors/writers, repositories, status enums/constants, messaging configuration, and integration clients.

Do not mistake framework structure for business structure. A controller, batch job, and listener may all participate in one business flow.

## Discover the business journey

Reconstruct major capabilities before implementation details. Ask:
- What business object/event enters the module?
- What major transformations/decisions happen?
- What external handoffs occur?
- What outcome marks completion?
- What statuses divide meaningful stages?
- Which flows run before/after one another?

Create a provisional journey. Mark uncertain ordering explicitly.

## Entry point model
Capture both:
- **Functional entry point**: the business event that starts the flow.
- **Technical entry point**: controller, listener, scheduler, job, file watcher, command, etc.

Never substitute the technical entry point for the business trigger.

## Discovery output
At checkpoint, show:
- system/module purpose
- major flows/capabilities
- provisional sequence
- important external dependencies
- notable statuses/state transitions
- terminology/glossary candidates
- unknowns and contradictions

Do not write polished final pages during reconnaissance.
