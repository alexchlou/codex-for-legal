# Quick Start

This repository exposes Anthropic's legal workflow suite as a Codex repo-scoped plugin marketplace.

## Install In Codex

1. Add the public marketplace:

   ```bash
   codex plugin marketplace add alexchlou/codex-for-legal
   ```

2. Restart Codex.

3. Open the Plugin Directory, select the `Codex for Legal` marketplace, and install the practice-area plugins you need.

4. Before using a playbook-backed workflow, copy and customize the relevant local configuration template:

   ```bash
   mkdir -p config/local/codex-for-legal/commercial-legal
   cp config/templates/codex-for-legal/commercial-legal/CLAUDE.md \
     config/local/codex-for-legal/commercial-legal/CLAUDE.md
   ```

   `config/local/` is ignored by git and is the right place for house style, playbooks, approval matrices, and matter-specific preferences.

For local development from a clone, you can run `codex plugin marketplace add .` from the repository root. Local-path installs are not Git-backed, so use the public install command above if you want `upgrade` to pull from GitHub.

## First Skill To Try

| You are a... | Install... | First skill |
|---|---|---|
| Privacy lawyer / DPO | `privacy-legal` | `$privacy-legal:use-case-triage` |
| Commercial / contracts lawyer | `commercial-legal` | `$commercial-legal:review` |
| Corporate / M&A lawyer | `corporate-legal` | `$corporate-legal:diligence-issue-extraction` |
| Employment lawyer / HR counsel | `employment-legal` | `$employment-legal:wage-hour-qa` |
| Product counsel | `product-legal` | `$product-legal:is-this-a-problem` |
| IP lawyer / patent agent | `ip-legal` | `$ip-legal:clearance` |
| Litigator | `litigation-legal` | `$litigation-legal:matter-intake` |
| Regulatory / compliance counsel | `regulatory-legal` | `$regulatory-legal:reg-feed-watcher` |
| AI governance lead | `ai-governance-legal` | `$ai-governance-legal:use-case-triage` |
| Clinic supervisor | `legal-clinic` | `$legal-clinic:cold-start-interview` |
| Law student | `law-student` | `$law-student:cold-start-interview` |
| Legal ops / skill discovery | `legal-builder-hub` | `$legal-builder-hub:registry-browser` |
| Westlaw / Practical Law research user | `cocounsel-legal` | `$cocounsel-legal:deep-research` |

## Connector Boundary

V1 is local-file first. References to Drive, CLM IDs, Slack, Westlaw, iManage, Ironclad, eDiscovery, dockets, or other remote systems require separately configured Codex MCP servers or connectors. Until those are configured, provide local files, local exports, or pasted excerpts.

Archived upstream connector metadata lives under each plugin's `references/mcp/` directory for later integration.

## Refresh

For the public Git-backed install:

```bash
codex plugin marketplace upgrade codex-for-legal
```

## Stuck?

- If a skill says setup is missing, run the relevant `cold-start-interview` or `customize` skill and create `config/local/codex-for-legal/<practice>/CLAUDE.md`.
- If a skill asks for a remote source and no connector is configured, provide a local export, local file path, or pasted text.
- Every output is draft legal work product requiring attorney review, source checking, and jurisdiction-specific validation.
