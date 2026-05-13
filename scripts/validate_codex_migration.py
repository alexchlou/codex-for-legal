#!/usr/bin/env python3
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PRACTICES = {
    "ai-governance-legal",
    "commercial-legal",
    "corporate-legal",
    "employment-legal",
    "ip-legal",
    "law-student",
    "legal-builder-hub",
    "legal-clinic",
    "litigation-legal",
    "privacy-legal",
    "product-legal",
    "regulatory-legal",
    "cocounsel-legal",
}
EXPECTED_SKILLS = 151
EXPECTED_MCP_REFERENCES = 13
LOCAL_PRIVATE_EXCLUDES = [
    "-g",
    "!privacy-legal-CLAUDE.md",
    "-g",
    "!20260512_PIA_*.md",
]

errors = []


def fail(message):
    errors.append(message)


def rg(args):
    return subprocess.run(
        ["rg", *args, *LOCAL_PRIVATE_EXCLUDES],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


marketplace_path = ROOT / ".agents" / "plugins" / "marketplace.json"
try:
    marketplace = json.loads(marketplace_path.read_text())
except Exception as exc:
    fail(f"Invalid marketplace JSON: {exc}")
    marketplace = {"plugins": []}

plugin_entries = marketplace.get("plugins", [])
plugin_names = {p.get("name") for p in plugin_entries}
if plugin_names != PRACTICES:
    fail(f"Marketplace plugin set mismatch: {sorted(plugin_names)}")
if len(plugin_entries) != 13:
    fail(f"Expected 13 marketplace plugins, found {len(plugin_entries)}")

for entry in plugin_entries:
    name = entry.get("name")
    if not name:
        continue
    if entry.get("source", {}).get("path") != f"./plugins/{name}":
        fail(f"Bad source.path for {name}")
    policy = entry.get("policy", {})
    if policy.get("installation") != "AVAILABLE" or policy.get("authentication") != "ON_INSTALL":
        fail(f"Bad policy for {name}")

    manifest_path = ROOT / "plugins" / name / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text())
    except Exception as exc:
        fail(f"Invalid plugin manifest for {name}: {exc}")
        continue
    if manifest.get("name") != name:
        fail(f"Manifest name mismatch for {name}")
    if manifest.get("skills") != "./skills/":
        fail(f"Manifest skills path mismatch for {name}")

skill_files = list((ROOT / "plugins").glob("*/skills/*/SKILL.md"))
if len(skill_files) != EXPECTED_SKILLS:
    fail(f"Expected {EXPECTED_SKILLS} skills, found {len(skill_files)}")

mcp_refs = list((ROOT / "plugins").glob("*/references/mcp/*.json"))
if len(mcp_refs) != EXPECTED_MCP_REFERENCES:
    fail(f"Expected {EXPECTED_MCP_REFERENCES} archived MCP references, found {len(mcp_refs)}")

active_mcp = [p for p in ROOT.rglob(".mcp.json")]
if active_mcp:
    fail("Active .mcp.json files remain: " + ", ".join(str(p.relative_to(ROOT)) for p in active_mcp))

old_path = "~/.claude/plugins/" + "config"
old_path_scan = rg(["-n", "-F", old_path])
if old_path_scan.returncode == 0:
    fail("Old Claude config path remains:\n" + old_path_scan.stdout.strip())
elif old_path_scan.returncode not in {1, 2}:
    fail(old_path_scan.stderr.strip() or "rg failed while scanning old Claude config paths")

slash_pattern = r"/(?:" + "|".join(re.escape(p) for p in sorted(PRACTICES)) + r"):[a-z0-9-]+"
slash_scan = rg(["-n", slash_pattern, "-g", "*.md"])
if slash_scan.returncode == 0:
    fail("Claude-style namespaced slash commands remain:\n" + slash_scan.stdout.strip())
elif slash_scan.returncode not in {1, 2}:
    fail(slash_scan.stderr.strip() or "rg failed while scanning slash commands")

skill_paths = [str(p.relative_to(ROOT)) for p in skill_files]
missing_note = rg(["--files-without-match", "Codex v1 local-input note", *skill_paths])
if missing_note.returncode == 0 and missing_note.stdout.strip():
    fail("Missing local-input note in skills:\n" + missing_note.stdout.strip())
elif missing_note.returncode not in {0, 1}:
    fail(missing_note.stderr.strip() or "rg failed while scanning local-input notes")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    sys.exit(1)

print("Codex migration validation passed")
print(f"plugins={len(plugin_entries)} skills={len(skill_files)} mcp_references={len(mcp_refs)}")
