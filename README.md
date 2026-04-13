# Agentic Research Skills

> A curated collection of reusable Cursor skills for academic and manuscript workflows.

Cursor skills are reusable `SKILL.md` instruction files that teach the agent how to perform specific tasks.  
This repository stores project skills under `resources/skills/`.

## Contents

- Skills
- Usage
- Contributing

---

## Skills

Ready-to-use skills in this repository:

- [`literature-review`](resources/skills/literature-review/SKILL.md) - Summarize academic PDF publications into structured Markdown with per-bullet source locations.
- [`manuscript-review`](resources/skills/manuscript-review/SKILL.md) - Review IEEE Transactions manuscripts using a detailed checklist and issue-based output format.

## Structure

Each skill uses one folder with a required `SKILL.md` file:

```text
resources/
  skills/
    <skill-name>/
      SKILL.md
```

## Usage

Copy any skill folder into your target project at:

`.cursor/skills/<skill-name>/SKILL.md`

## Contributing

To add a new skill:

1. Create `resources/skills/<skill-name>/`.
2. Add `SKILL.md` with valid frontmatter (`name`, `description`).
3. Keep instructions specific, testable, and scoped to one workflow.