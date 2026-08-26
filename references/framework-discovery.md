# Framework-Aware Discovery

Use this reference to accelerate code investigation without confusing framework conventions with business truth.

## General Rule

Framework patterns identify **places to investigate**. They do not prove business purpose, ordering, or semantics.

Trace both directions where possible:

```text
entry/trigger -> processing -> persistence/integration -> state/output
state/output -> consumers/selectors -> next processing
```

Tests, configuration, deployment manifests, SQL/migrations, schemas, and operational scripts may contain important evidence outside application source.

## Spring Boot / Java

Useful investigation targets:

- `@RestController`, `@Controller`, request mappings
- `@Service`, application/use-case classes
- `@Repository`, Spring Data repositories, custom DAO/JDBC code
- `@Scheduled`
- `@EventListener`, application events
- Kafka/JMS/MQ listeners and producers
- configuration properties and profiles
- security/filter/interceptor chains when relevant to behavior
- database migrations and schema definitions
- exception handlers
- integration clients (Feign, WebClient, RestClient, RestTemplate, SDKs)

Do not treat bean wiring as business flow unless runtime ordering is actually established.

## Spring Batch

Investigate:

- `Job` definitions
- `Step` definitions
- job launchers/schedulers
- readers/processors/writers
- tasklets
- partitioners
- listeners
- deciders
- execution context usage
- skip/retry policies
- transaction boundaries
- job repository/restart configuration
- selectors/queries that gate eligible records
- status writes inside processors/writers/listeners
- downstream calls and file output

For each important job establish, where evidence permits:

```text
business purpose
trigger/gate
input
eligibility/status query
steps
reader -> processor -> writer/tasklet
state changes
database effects
external effects
output
restart/retry/skip behavior
next known consumer
```

Never infer that Job B follows Job A merely because their names or scheduled times appear sequential.

## APIs

For each important API trace:

```text
route
-> validation/auth behavior relevant to business
-> service/use case
-> state reads/writes
-> integrations/events
-> response/error semantics
```

OpenAPI/Swagger is strong evidence for exposed contract when current and generated from code, but it may not explain business rationale.

## Messaging

Investigate:

- topic/queue names from configuration, not only constants
- producer call sites
- consumer/listener bindings
- payload/schema definitions
- keys/partitioning when behaviorally relevant
- retry/DLQ configuration
- idempotency/deduplication
- status writes before/after publish/consume

Do not assume delivery guarantees from the messaging technology alone; verify configuration and code.

## Database and Status Discovery

Search status constants/enums, but then trace:

- assignments/updates
- SQL update statements
- repository update methods
- query predicates/selectors
- switch/case/if branches
- API response mappings
- batch eligibility queries
- tests asserting transitions

A database column called `status` is not enough to define its business meaning.

For relationships, prefer schema/migration/ORM evidence. A matching `*_id` name without a constraint/mapping may only be a hypothesis.

## Files / SFTP / Batch Interfaces

Investigate:

- file watchers/pollers/schedulers
- naming patterns
- parsers/readers
- header/trailer validation
- record-count/amount reconciliation
- archive/error directories
- duplicate detection/idempotency
- outbound writers
- SFTP/SSH clients
- acknowledgements/response files
- status transitions tied to file processing

Ask the user about operational conventions not encoded in code, such as expected arrival windows or manual recovery procedures.

## Other Frameworks

For Node/Python/.NET/Go/etc., use the same conceptual model:

```text
entry points
triggers
business processing
state
persistence
integrations
outputs
consumers
failure/recovery
```

Identify framework-native routers/controllers, schedulers, workers, ORM/data layers, event handlers and configuration, but keep the knowledge model framework-neutral.

## Repository Boundaries

A business flow may span repositories/microservices. Once the user has scoped the business capability, follow verified cross-service dependencies **only when the target is within scope**.

If target ownership is ambiguous, ask before deep exploration.

If target is out of scope, record only the boundary contract/evidence available from the in-scope side.
