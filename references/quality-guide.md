# Quality Gate and Wiki Audit Guide

## Flow quality gate
A flow is complete only when applicable checks pass:
- newcomer can understand it without source code
- purpose and business trigger are explicit
- technical entry point is locatable
- process is explained as a connected narrative
- useful Mermaid diagram exists
- important branches/rules are explained
- relevant status progression is understandable
- dependency boundaries are explicit
- failures/recovery are covered when material
- implementation references support rather than dominate
- important claims have evidence/provenance
- unsupported inference is visibly qualified
- previous and next flow context is clear

A failed check means rewrite or investigate; do not merely add a TODO and mark complete.

## Module quality gate
Check:
- end-to-end journey is coherent
- flow order matches business operation
- status model is consistent across pages
- terminology is consistent
- dependencies are not accidentally described as owned internals
- important decisions/rationale are captured
- change guidance points developers to the right flows/components

## Wiki audit
Read as a new developer starting from `index.md`.

Look for:
- unexplained jumps
- orphan pages
- broken links
- duplicated facts with different wording
- contradictions
- stale or superseded knowledge
- excessive bullets/class names
- missing visual explanation
- pages with no clear purpose
- unresolved `UNKNOWN`/`CONFLICT` items that block understanding
- inconsistent evidence labels

## AI navigation audit
Verify an agent can:
1. start at `index.md`
2. identify the relevant module
3. locate the relevant flow/status/decision without scanning the full repo
4. distinguish verified knowledge from inference
5. know when source-code inspection is still required

## Review stance
Do not optimize for page count. Prefer fewer coherent pages over many fragmented reference pages.
