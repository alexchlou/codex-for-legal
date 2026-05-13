---
name: form-generation
description: >
  Reference: DEPRECATED — use `$legal-clinic:draft` instead. This skill has been folded into
  the draft skill, which handles practice-area document generation including
  form population. Kept as a redirect for migration.
user-invocable: false
---

> Codex v1 local-input note: This migrated skill supports local files and pasted text by default. References to Drive, CLM IDs, Slack, Westlaw, iManage, Ironclad, eDiscovery, dockets, or other remote systems require a separately configured Codex connector/MCP server. When a connector is unavailable, ask for a local export, local file path, or pasted excerpts. If `config/local/codex-for-legal/<practice>/CLAUDE.md` is missing, ask the user to run the relevant `cold-start-interview` or `customize` skill and copy from `config/templates/codex-for-legal/<practice>/CLAUDE.md`.


# [DEPRECATED] Form Generation → see `$legal-clinic:draft`

This skill was folded into `skills/draft/` during the v2 rebuild. The `$legal-clinic:draft`
command handles first-draft generation for all clinic documents including form
population (asylum applications, eviction answers, protective order petitions,
etc.) with practice-area templates and jurisdiction-aware formatting.

**Use `$legal-clinic:draft [document type]` instead.**

See `skills/draft/SKILL.md` for the full workflow.
