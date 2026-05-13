---
name: session
description: >
  Run a focused N-question study session on a subject — MBE, essay, or
  flashcards. Tracks performance and updates the study plan. Use when the
  user says "run me 10 questions on [subject]", "do a session on [subject]",
  "let's do 5 cards on [subject]", or wants to drill a fixed number of
  questions and have the plan adapt.
argument-hint: "<subject> <n> [--mbe | --essay | --flashcards]"
---

> Codex v1 local-input note: This migrated skill supports local files and pasted text by default. References to Drive, CLM IDs, Slack, Westlaw, iManage, Ironclad, eDiscovery, dockets, or other remote systems require a separately configured Codex connector/MCP server. When a connector is unavailable, ask for a local export, local file path, or pasted excerpts. If `config/local/codex-for-legal/<practice>/CLAUDE.md` is missing, ask the user to run the relevant `cold-start-interview` or `customize` skill and copy from `config/templates/codex-for-legal/<practice>/CLAUDE.md`.


# $law-student:session

1. Parse `$ARGUMENTS` — subject and N. If missing, ask:
   > What subject, and how many questions? (e.g., `Evidence 10` or `Contracts 5 --essay`.)
2. Load `config/local/codex-for-legal/law-student/CLAUDE.md` → jurisdiction, exam format, weak subjects.
3. Load `config/local/codex-for-legal/law-student/study-plan.yaml` if it exists. Read `session_history` for this subject to weight subtopics toward where the student has been weak.
4. Route by method flag:
   - `--mbe` (default for bar prep subjects): load `bar-prep-questions` skill, run N MBE-style questions. Apply jurisdiction handling (see that skill's `## Jurisdiction handling`). Label each `[UBE/majority]` or `[state-specific]`.
   - `--essay`: load `bar-prep-questions`, run N essay prompts. Grade per essay-mode rubric.
   - `--flashcards`: load `flashcards` skill, run N cards in `--drill` mode.
5. Run N questions one at a time. After each, explain right/wrong and flag rule-body when jurisdictions diverge.
6. At session end, write session results:
   - If `study-plan.yaml` exists: append to `session_history` per the schema in the `study-plan` skill.
   - If not: write to `config/local/codex-for-legal/law-student/session-history.yaml`.
7. Report:
   - Score: X/N (percentage)
   - Missed: list with subtopic tags
   - Weak subtopics this session
   - Pattern vs. prior sessions on this subject (if history has 2+ prior)
   - What the plan now recommends next
