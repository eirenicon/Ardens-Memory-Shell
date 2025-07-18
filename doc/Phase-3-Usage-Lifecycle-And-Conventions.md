# Ardens Memory Shell — Phase 3: Usage Lifecycle & Conventions

## 1. Memory Entry Lifecycle

### Creation
- **When?** Entries should be created at meaningful moments: after insightful dialogue, decisions, research milestones, or system events.
- **Who?** Both human collaborators and AI agents can author entries.
- **How?** Entries can be manually composed, AI-generated, or produced via automated tools.
- **What?** Each entry must contain:
  - A unique `id` (UUIDv4)
  - The creating `agent` name
  - Accurate `timestamp` in UTC (ISO 8601)
  - Relevant semantic `tags`
  - The main `content` body (plain text or markdown)
  - An optional `hash` of the content for integrity
  - The schema `version` used

### Storage & Commit
- Entries are stored as discrete JSON or Markdown files within a Git repository.
- Recommended directory structure:

