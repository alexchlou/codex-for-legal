# Modifications

This repository is a Codex adaptation of Anthropic's `claude-for-legal` project.

## Source

- Upstream project: https://github.com/anthropics/claude-for-legal
- Upstream license: Apache License 2.0

## Changes Made

- Converted Claude plugin marketplace metadata into Codex repo marketplace metadata at `.agents/plugins/marketplace.json`.
- Converted each Claude plugin manifest into a Codex `.codex-plugin/plugin.json` manifest.
- Preserved the upstream legal skills while adapting references from Claude-specific command syntax to Codex skill mentions.
- Renamed the public marketplace identity to `codex-for-legal` / `Codex for Legal`.
- Rewrote user configuration paths from Claude-specific locations to `config/local/codex-for-legal/...`.
- Moved playbook templates into `config/templates/codex-for-legal/...`.
- Archived upstream `.mcp.json` connector configurations under each plugin's `references/mcp/` directory as reference material only.
- Added local-file-first notices to migrated skills because remote connectors are not enabled by default in this Codex adaptation.
- Retained managed-agent markdown files as manual workflow descriptions and added notes that Codex automations should only be created when explicitly requested by the user.
- Added validation tooling in `scripts/validate_codex_migration.py` to check plugin count, skill count, archived MCP reference count, JSON validity, and key migration invariants.
- Added Codex migration attribution to Alexander C. H. Lou while preserving upstream attribution to Anthropic and Thomson Reuters where applicable.

## Non-Affiliation

This project is an unofficial adaptation. It is not affiliated with, endorsed by, or sponsored by Anthropic, Thomson Reuters, or OpenAI.
