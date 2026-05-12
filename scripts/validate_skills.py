#!/usr/bin/env python3
"""Validate repository skill metadata and README coverage."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "resources" / "skills"
README = ROOT / "README.md"


def read_frontmatter(skill_file: Path) -> dict[str, str]:
    lines = skill_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{skill_file}: missing opening frontmatter delimiter")

    metadata: dict[str, str] = {}
    for line in lines[1:]:
        if line == "---":
            return metadata
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()

    raise ValueError(f"{skill_file}: missing closing frontmatter delimiter")


def main() -> int:
    errors: list[str] = []
    readme_text = README.read_text(encoding="utf-8")

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        errors.append(f"{SKILLS_DIR}: no skill directories found")

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"{skill_dir}: missing SKILL.md")
            continue

        try:
            metadata = read_frontmatter(skill_file)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        name = metadata.get("name")
        description = metadata.get("description")
        if not name:
            errors.append(f"{skill_file}: missing required 'name' frontmatter")
        elif name != skill_dir.name:
            errors.append(
                f"{skill_file}: name '{name}' does not match folder '{skill_dir.name}'"
            )

        if not description:
            errors.append(f"{skill_file}: missing required 'description' frontmatter")

        readme_link = f"resources/skills/{skill_dir.name}/SKILL.md"
        if readme_link not in readme_text:
            errors.append(f"{README}: missing README link for '{skill_dir.name}'")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Validated {len(skill_dirs)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
