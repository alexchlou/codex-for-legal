# Migration Notes

This repo was generated from Anthropic's `claude-for-legal` repository and adapted for Codex plugin loading.

Codex migration and adaptation by Alexander C. H. Lou. Upstream authorship and license attribution are preserved.

## Format Changes

- Claude marketplace metadata was converted into `.agents/plugins/marketplace.json`.
- Each Claude plugin manifest was converted into `.codex-plugin/plugin.json`.
- Practice-area playbooks were moved into `config/templates/codex-for-legal/<practice>/CLAUDE.md` templates.
- User-specific playbooks belong in ignored `config/local/codex-for-legal/<practice>/CLAUDE.md` files.
- Remote MCP connector JSON files are archived as references and are not enabled by default.

## V1 Boundary

V1 supports local files, local exports, and pasted text. Remote systems must be connected separately through Codex MCP configuration before a skill may rely on them.
