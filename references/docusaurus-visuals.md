# Docusaurus and Visualization Guidelines

Use these rules when creating or updating the human-facing documentation experience.

## Goal

Make complex systems easier to understand through progressive, interactive views. Visual polish serves comprehension; it must never hide uncertainty or fabricate completeness.

## Default Stack

For a new documentation package, prefer:

- Docusaurus
- MDX for pages that need interaction
- Mermaid for portable diagrams
- small reusable React components for interaction Mermaid cannot express cleanly
- canonical YAML/JSON knowledge as the data source where practical

Do not replace an existing approved documentation platform merely to use Docusaurus.

## Information Architecture

Prefer business navigation:

```text
Getting Started
  System Overview
  Architecture
  Processing Timeline
Business Flows
  <Domain>
    Overview
    End-to-End Flow
    Child Flows
    Variants
Statuses & State Machines
Processing Components
  Jobs
  APIs
  Events
  File Interfaces
Data
Integrations
Operations
  Timeline
  Failure & Recovery
Developer Reference
Documentation Coverage
```

Repository/service navigation is a secondary technical view.

## Progressive Diagrams

Never solve complexity by putting everything into one diagram.

Use three levels when needed:

1. **Overview** — 5-9 meaningful business stages
2. **Subflow** — detailed stages for one selected node
3. **Technical** — sequence/component/data/status details

A user should be able to click or navigate from overview to detail and back.

## Mermaid Selection

Use Mermaid for:

- `flowchart` — business flows, dependency paths
- `sequenceDiagram` — API/job/integration interactions
- `stateDiagram-v2` — verified state transitions
- `erDiagram` — meaningful data relationships
- `classDiagram` — only when class/domain structure genuinely aids understanding
- timelines/Gantt only when they communicate verified scheduling/ordering clearly

Do not create a state diagram from enum values alone.

Do not put unknown edges into Mermaid as if they are known. Label them `Unknown`/`Needs confirmation`, use a visually distinct uncertainty treatment, or omit the edge and show an adjacent callout.

## Semantic Color Vocabulary

Define colors centrally through CSS/theme variables so dark/light themes remain readable. Never scatter random hex colors across generated pages.

Suggested semantic roles (actual theme colors may be chosen to meet accessibility/brand requirements):

- **Primary/business stage** — primary/accent color
- **External system/boundary** — secondary/neutral accent
- **Success/completed** — success semantic color
- **Warning/in-progress** — warning semantic color
- **Failure/return/error** — danger semantic color
- **Unknown/unverified** — muted/dashed/uncertainty treatment
- **Out of scope** — neutral muted treatment with explicit OUT OF SCOPE label

Color must not be the only carrier of meaning. Pair it with labels/icons/borders/patterns.

## Interactive Components

Create reusable components only when they add comprehension beyond normal Markdown/Mermaid. Keep them generic and driven by canonical knowledge where feasible.

Recommended components:

### `FlowExplorer`

Purpose: drill from end-to-end business flow into child flows/components.

Useful behavior:

- select/click stage
- show purpose, trigger, outputs, statuses and evidence summary
- links to detailed page/sequence/source references
- breadcrumb back to parent flow

### `StatusExplorer`

Purpose: understand status meaning and transitions.

Useful filters:

- entity
- business variant
- processing stage

Display:

- known previous/next states
- producer/consumer
- transition trigger
- failure/recovery
- evidence badge
- explicit unknowns

### `VariantExplorer`

Purpose: compare branching behavior such as small/large, country, channel, type, or product.

Prefer a common-path + divergence + convergence view. Avoid duplicating the entire flow for each variant when most stages are shared.

### `ProcessingTimeline`

Purpose: explain time-oriented systems such as clearing/batch platforms.

Display verified events/jobs/windows in business order. Distinguish clock schedule from dependency ordering. Do not fabricate times from log examples.

### `KnowledgeGraph`

Purpose: navigational overview for humans, not an attempt to render every source-level node.

Allow filtering by domain/node type and progressive expansion. Large graphs must start collapsed.

### `FailureExplorer`

Purpose: show what can fail, observable state, effect, recovery/retry/reconciliation, and ownership when known.

Unknown recovery behavior must be explicit.

## Animation

Animation is optional and explanatory, never required to understand the page.

Good uses:

- Play an end-to-end processing sequence one stage at a time
- Highlight the current node while accompanying text changes
- Animate expansion/collapse of a selected branch

Avoid:

- constant motion
- decorative particles
- slow transitions
- animations that imply an unverified ordering
- animations that make screenshots/printing unusable

Respect reduced-motion preferences.

## Evidence UI

Do not clutter every sentence with implementation paths. Provide compact evidence badges/details:

```text
CODE VERIFIED
USER CONFIRMED
DOCUMENT VERIFIED
NEEDS CONFIRMATION
CONFLICT
OUT OF SCOPE
```

A detail drawer/panel can show paths, symbols, interview statements, or artifact references.

The visual UI must never transform `INFERRED` into a green/verified-looking fact.

## Coverage UI

Provide a coverage view so readers understand intentional omissions:

```text
DOCUMENTED
IN PROGRESS
TODO
OUT OF SCOPE
```

This prevents readers from interpreting absent documentation as an absent feature.

## Page Pattern for a Complex Flow

Recommended order:

1. title + short business purpose + coverage/evidence summary
2. interactive or Mermaid end-to-end flow
3. processing timeline if relevant
4. variant selector/comparison
5. status explorer
6. child-flow cards
7. technical sequence/components
8. data/integrations
9. failures/recovery
10. evidence + open questions

Do not front-load pages with Java class names or infrastructure details unless the page itself is technical reference.

## Accessibility and Readability

- support light and dark themes
- maintain sufficient text/background contrast
- do not encode meaning only with color
- provide textual alternatives to interactive views
- ensure diagrams remain usable at laptop widths
- make large diagrams zoomable or break them down
- use consistent terminology from the knowledge model
- keep animations keyboard/reduced-motion friendly

## Generated vs Human Content

Separate generated sections/components from hand-authored rationale where practical. If regeneration could overwrite a human explanation, preserve it or ask before replacing it.

A good pattern is for generated views to consume canonical knowledge while narrative business context remains an explicitly managed field with provenance.

## Build/Validation

Before claiming documentation is ready, where the environment permits:

- install with the repository's approved package manager
- run the Docusaurus build
- fix broken links and MDX errors
- verify Mermaid rendering
- verify key interactive pages in light/dark themes if practical
- verify unknown/conflict/out-of-scope states render distinctly
- verify mobile/laptop overflow for major diagrams

A successful build proves structure, not semantic correctness. Semantic correctness still comes from evidence and confirmation.
