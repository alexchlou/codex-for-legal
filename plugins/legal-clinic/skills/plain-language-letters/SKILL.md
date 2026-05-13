---
name: plain-language-letters
description: >
  Reference: DEPRECATED — use `$legal-clinic:client-letter` for routine correspondence or
  `$legal-clinic:status client` for substantive updates. Split into two more focused skills
  during the v2 rebuild. Kept as a redirect for migration.
user-invocable: false
---

> Codex v1 local-input note: This migrated skill supports local files and pasted text by default. References to Drive, CLM IDs, Slack, Westlaw, iManage, Ironclad, eDiscovery, dockets, or other remote systems require a separately configured Codex connector/MCP server. When a connector is unavailable, ask for a local export, local file path, or pasted excerpts. If `config/local/codex-for-legal/<practice>/CLAUDE.md` is missing, ask the user to run the relevant `cold-start-interview` or `customize` skill and copy from `config/templates/codex-for-legal/<practice>/CLAUDE.md`.


# [DEPRECATED] Plain-Language Letters → see `$legal-clinic:client-letter` and `$legal-clinic:status client`

This skill was split during the v2 rebuild:

- **Routine correspondence** (appointment confirms, document requests, brief
  "we filed it" updates) → `skills/client-letter/` — use `$legal-clinic:client-letter [type]`

- **Substantive client status updates** → `skills/status/` in client-facing
  mode — use `$legal-clinic:status client`

Both apply the plain-language standards (reading level, no jargon) from CLAUDE.md.

See the respective SKILL.md files for full workflows.
