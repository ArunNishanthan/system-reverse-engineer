# System Reverse Engineer

A reusable Agent Skill for turning large, poorly documented software systems into a verified, human-readable and AI-navigable knowledge wiki.

The skill is designed for systems where source code alone is not enough to reconstruct the real business flow. It combines code investigation, explicit scope control, domain-expert interviews, provenance, Mermaid diagrams, staged checkpoints, and quality gates.

## Core idea

**Write for humans. Structure for AI. Verify against evidence.**

The generated documentation should help a new developer understand:
- what the system/module does
- where a flow starts
- how processing moves end to end
- what important statuses mean
- which dependencies are involved
- what happens on failure or recovery
- which business rules matter
- where to start when changing the code

At the same time, the linked Markdown structure should be easy for Claude Code, Codex, Gemini CLI, Copilot, or other agents to navigate without repeatedly reverse engineering the full repository.

## Workflow

The skill uses explicit checkpoints:

1. Workspace ready
2. System context validated
3. Scope and dependency boundaries approved
4. Module journey approved
5. Individual flow understanding reconciled
6. Flow quality gate passed
7. Module story reviewed
8. Wiki audit completed

The agent must interview knowledgeable people when source code cannot establish intent, business meaning, operational convention, historical rationale, or missing sequence.

## Scope model

- `PRIMARY_SCOPE` - reverse engineer fully.
- `DEPENDENCY_BOUNDARY` - understand only the integration contract and impact needed by the primary scope.
- `OUT_OF_SCOPE` - do not investigate beyond orientation needs.

This prevents a module investigation from recursively expanding into every large dependency it touches.

## Knowledge format

Canonical knowledge stays in linked Markdown. Mermaid is used for real diagrams. A separate graph database is not required.

A typical generated wiki may look like:

```text
documentation/
  index.md
  system-overview.md
  glossary.md
  log.md
  checkpoints/
    current.md
  modules/
    outward-clearing/
      overview.md
      statuses.md
      decisions.md
      change-guide.md
      flows/
        ingestion.md
        posting.md
        submission.md
```

The structure grows only as verified knowledge is produced; the skill must not create large sets of empty placeholder files.

## Evidence states

The skill distinguishes:

- `CODE_VERIFIED`
- `DOCUMENT_VERIFIED`
- `USER_CONFIRMED`
- `INFERRED`
- `UNKNOWN`
- `CONFLICT`

Only verified or user-confirmed information should be presented as authoritative.

## Human-first documentation

Developer-centric does not mean class-heavy. The documentation should explain behavior and business meaning first, using implementation names only as supporting references.

A flow page should read like a connected technical chapter, not a repository inventory.

## Sub-agents

For substantial flows, when the host supports sub-agents and two or more investigation tracks are independent, the coordinator should delegate evidence discovery. Typical tracks include entry points, statuses, integrations, business rules, persistence, and failure handling.

Sub-agents do not write canonical documentation. The coordinator reconciles evidence, interviews people, draws diagrams, and owns final narrative quality.

## Repository structure

```text
SKILL.md
README.md
agents/
  openai.yaml
references/
  scope-guide.md
  discovery-guide.md
  investigation-guide.md
  interview-guide.md
  evidence-guide.md
  writing-guide.md
  diagram-guide.md
  quality-guide.md
  maintenance-guide.md
templates/
  index.md
  checkpoint.md
  module.md
  flow.md
  status.md
```

`SKILL.md` is intentionally the control plane. Detailed instructions live in references and are loaded only for the stage that needs them.
