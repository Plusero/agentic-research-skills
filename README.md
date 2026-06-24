# Agentic Research Skills

> A curated collection of reusable agent skills for academic and manuscript workflows.

Skills are reusable `SKILL.md` instruction files that teach an agent how to perform specific tasks.
This repository stores project skills under `resources/skills/`.

## Contents

- Skills
- Structure
- Usage
- Contributing

---

## Skills

Ready-to-use skills in this repository:

- [`literature-review`](resources/skills/literature-review/SKILL.md) - Summarize academic PDF publications into structured Markdown with per-bullet source locations.
- [`topic-literature-search`](resources/skills/topic-literature-search/SKILL.md) - Search academic sources for a topic, verify candidate papers, and produce a sourced top-10 literature summary.
- [`ieee-manuscript-review`](resources/skills/ieee-manuscript-review/SKILL.md) - Review IEEE Transactions manuscripts using a detailed checklist and issue-based output format.
- [`paper-readability-check`](resources/skills/paper-readability-check/SKILL.md) - Check paper readability with a fixed sentence- and paragraph-level strategy checklist and actionable rewrite guidance.
- [`grammar-check`](resources/skills/grammar-check/SKILL.md) - Check grammar, punctuation, mechanics, and usage with explicit rule references in a reader-friendly before/after HTML report.
- [`scientific-plotting`](resources/skills/scientific-plotting/SKILL.md) - Create publication-quality scientific figures in Python using Matplotlib and SciencePlots.
- [`iec-network-drawio`](resources/skills/iec-network-drawio/SKILL.md) - Create or revise IEC 60617-style distribution-grid diagrams in Draw.io/.drawio files while preserving electrical topology.

## Structure

Each skill uses one folder with a required `SKILL.md` file:

```text
resources/
  skills/
    <skill-name>/
      SKILL.md
```

## Usage

### Cursor

Copy any skill folder into your target project at:

`.cursor/skills/<skill-name>/SKILL.md`

### Claude Code

Based on the Claude Code skills documentation:

1. Copy any skill folder into either:
   - project scope: `.claude/skills/<skill-name>/SKILL.md`
   - personal scope: `~/.claude/skills/<skill-name>/SKILL.md`
2. Keep `SKILL.md` frontmatter (`name`, `description`) intact.
3. Invoke directly with `/skill-name`, or let Claude auto-invoke when the request matches the description.

Reference: [Claude Code Skills Docs](https://code.claude.com/docs/en/skills)

### OpenCode

Based on the OpenCode Agent Skills documentation:

1. Copy any skill folder into one of these locations:
   - project scope: `.opencode/skills/<skill-name>/SKILL.md`
   - personal scope: `~/.config/opencode/skills/<skill-name>/SKILL.md`
   - Claude-compatible scope: `.claude/skills/<skill-name>/SKILL.md` or `~/.claude/skills/<skill-name>/SKILL.md`
   - agent-compatible scope: `.agents/skills/<skill-name>/SKILL.md` or `~/.agents/skills/<skill-name>/SKILL.md`
2. Ensure `SKILL.md` includes frontmatter with `name` and `description`.
3. Keep skill directory name and `name` value aligned (lowercase alphanumeric with hyphens).
4. OpenCode discovers and loads skills via the `skill` tool when available.

Reference: [OpenCode Agent Skills Docs](https://opencode.ai/docs/skills/)

## Contributing

To add a new skill:

1. Create `resources/skills/<skill-name>/`.
2. Add `SKILL.md` with valid frontmatter (`name`, `description`).
3. Keep the folder name and frontmatter `name` value aligned.
4. Keep instructions specific, testable, and scoped to one workflow.
5. Run `python3 scripts/validate_skills.py` before submitting changes.
