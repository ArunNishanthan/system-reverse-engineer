#!/usr/bin/env python3
"""Validate the system-reverse-engineer knowledge graph.

Usage:
    python scripts/validate_graph.py [graph.yaml] [documentation-root]

Defaults:
    graph.yaml          documentation/knowledge/graph.yaml
    documentation-root documentation/

Requires PyYAML. If it is not installed, the script exits with an actionable
message instead of attempting to install dependencies.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install/provide it using your approved environment setup.", file=sys.stderr)
    sys.exit(2)

ALLOWED_EVIDENCE = {
    "CODE_VERIFIED",
    "DOCUMENT_VERIFIED",
    "USER_CONFIRMED",
    "INFERRED",
    "UNKNOWN",
    "CONFLICT",
}

ALLOWED_COVERAGE = {"DOCUMENTED", "IN_PROGRESS", "TODO", "OUT_OF_SCOPE"}

ALLOWED_NODE_TYPES = {
    "SYSTEM", "MODULE", "CAPABILITY", "FLOW", "SUBFLOW", "PROCESSING_STEP",
    "SERVICE", "COMPONENT", "JOB", "JOB_STEP", "API", "STATUS", "ENTITY",
    "TABLE", "EVENT", "TOPIC", "FILE_INTERFACE", "INTEGRATION", "EXTERNAL_SYSTEM",
    "BUSINESS_RULE", "TEST", "RUNBOOK", "DECISION",
}

ALLOWED_EDGE_TYPES = {
    "HAS_MODULE", "HAS_CAPABILITY", "HAS_FLOW", "HAS_SUBFLOW", "HAS_STEP",
    "IMPLEMENTED_BY", "USES_JOB", "USES_API", "USES_COMPONENT", "USES_INTEGRATION",
    "TESTED_BY", "OPERATED_BY", "OWNS", "READS", "WRITES", "RELATES_TO",
    "SETS_STATUS", "READS_STATUS", "TRANSITIONS_TO", "TRIGGERED_BY", "CALLS",
    "PUBLISHES", "CONSUMES", "SENDS_FILE_TO", "RECEIVES_FILE_FROM",
    "INTEGRATES_WITH", "GOVERNED_BY", "DECIDED_BY", "DEPENDS_ON",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def evidence_states(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, dict):
        state = value.get("state")
        return [state] if state is not None else []
    if isinstance(value, list):
        states = []
        for item in value:
            if isinstance(item, dict) and item.get("state") is not None:
                states.append(item["state"])
        return states
    return []


def main() -> int:
    graph_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("documentation/knowledge/graph.yaml")
    docs_root = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("documentation")

    if not graph_path.is_file():
        print(f"ERROR: graph not found: {graph_path}", file=sys.stderr)
        return 2

    try:
        data = yaml.safe_load(graph_path.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        print(f"ERROR: invalid YAML in {graph_path}: {exc}", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(data, dict):
        fail(errors, "Graph root must be a mapping/object.")
        data = {}

    nodes = data.get("nodes", [])
    edges = data.get("edges", [])

    if not isinstance(nodes, list):
        fail(errors, "'nodes' must be a list.")
        nodes = []
    if not isinstance(edges, list):
        fail(errors, "'edges' must be a list.")
        edges = []

    node_ids: set[str] = set()
    node_by_id: dict[str, dict] = {}

    for i, node in enumerate(nodes):
        label = f"nodes[{i}]"
        if not isinstance(node, dict):
            fail(errors, f"{label}: must be a mapping/object.")
            continue

        node_id = node.get("id")
        if not isinstance(node_id, str) or not node_id.strip():
            fail(errors, f"{label}: missing non-empty 'id'.")
            continue
        if node_id in node_ids:
            fail(errors, f"{label}: duplicate node id '{node_id}'.")
        node_ids.add(node_id)
        node_by_id[node_id] = node

        node_type = node.get("type")
        if node_type not in ALLOWED_NODE_TYPES:
            fail(errors, f"{label} ({node_id}): invalid node type '{node_type}'.")

        coverage = node.get("coverage")
        if coverage is not None and coverage not in ALLOWED_COVERAGE:
            fail(errors, f"{label} ({node_id}): invalid coverage '{coverage}'.")

        scope = node.get("scope")
        if scope is not None and scope not in {"IN_SCOPE", "OUT_OF_SCOPE"}:
            fail(errors, f"{label} ({node_id}): invalid scope '{scope}'.")

        states = evidence_states(node.get("evidence"))
        for state in states:
            if state not in ALLOWED_EVIDENCE:
                fail(errors, f"{label} ({node_id}): invalid evidence state '{state}'.")

        doc = node.get("doc")
        if doc is not None:
            if not isinstance(doc, str) or not doc.strip():
                fail(errors, f"{label} ({node_id}): 'doc' must be a non-empty path string.")
            else:
                candidate = docs_root / doc
                if not candidate.is_file():
                    fail(errors, f"{label} ({node_id}): documentation path does not exist: {candidate}")

    for i, edge in enumerate(edges):
        label = f"edges[{i}]"
        if not isinstance(edge, dict):
            fail(errors, f"{label}: must be a mapping/object.")
            continue

        source = edge.get("from")
        target = edge.get("to")
        edge_type = edge.get("type")

        if source not in node_ids:
            fail(errors, f"{label}: unknown 'from' node '{source}'.")
        if target not in node_ids:
            fail(errors, f"{label}: unknown 'to' node '{target}'.")
        if edge_type not in ALLOWED_EDGE_TYPES:
            fail(errors, f"{label}: invalid edge type '{edge_type}'.")

        states = evidence_states(edge.get("evidence"))
        if not states:
            fail(errors, f"{label} ({source} -> {target}): material edge requires evidence.")
        for state in states:
            if state not in ALLOWED_EVIDENCE:
                fail(errors, f"{label}: invalid evidence state '{state}'.")
            if state == "INFERRED":
                warnings.append(f"{label} ({source} -> {target}) remains INFERRED; do not render it as verified behavior.")

        # Scope guard: an OUT_OF_SCOPE module is allowed as a boundary node, but
        # internal hierarchy must not be expanded beneath it.
        if edge_type in {"HAS_CAPABILITY", "HAS_FLOW", "HAS_SUBFLOW", "HAS_STEP"}:
            parent = node_by_id.get(source, {})
            if parent.get("scope") == "OUT_OF_SCOPE" or parent.get("coverage") == "OUT_OF_SCOPE":
                fail(errors, f"{label}: out-of-scope node '{source}' must not expose internal hierarchy via {edge_type}.")

    for warning in warnings:
        print(f"WARNING: {warning}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s).", file=sys.stderr)
        return 1

    print(f"OK: {len(nodes)} node(s), {len(edges)} edge(s), {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
