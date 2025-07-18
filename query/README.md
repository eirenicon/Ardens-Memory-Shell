# Querying Memory Entries

The `query/` directory houses strategies, filters, and tools for querying memory entries across the `/entries/` tree.

## Goals

- Enable human and AI agents to recall relevant memories.
- Allow filters by tag, timestamp, agent, hash prefix, etc.
- Support semantic matching or pattern-based queries (in future tools).

## Structure

- `by-agent/`: Entries by memory contributor.
- `by-tag/`: Indexes by tag (e.g., `planning`, `insight`, `error`).
- `recent.md`: Rolling index of most recent entries.

## Future Query Features (Planned)

- CLI query tools for filtered output.
- Text-based recall across natural-language content fields.
- Cross-entry insight extraction.

