#!/usr/bin/env python3
"""Small dependency-free repository validator for ad-manga-creator."""
from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "NOTICE.md",
    "references/angle-and-hook-system.md",
    "references/grounding-and-compliance.md",
    "references/manga-storyboard-rules.md",
    "references/japanese-copy-and-typesetting.md",
    "references/character-consistency.md",
    "references/image-generation-prompts.md",
    "references/visual-qa.md",
    "templates/brief.md",
    "templates/angle-matrix.md",
    "templates/4-panel-ad.md",
    "templates/6-panel-ad.md",
    "templates/one-page-ad.md",
    "scripts/init_project.py",
]


def validate_frontmatter(text: str) -> list[str]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return ["SKILL.md: missing YAML frontmatter"]
    end = text.find("\n---\n", 4)
    if end == -1:
        return ["SKILL.md: unclosed YAML frontmatter"]
    fm = text[4:end]
    for field in ("name:", "description:"):
        if field not in fm:
            errors.append(f"SKILL.md: frontmatter missing {field[:-1]}")
    if "name: ad-manga-creator" not in fm:
        errors.append("SKILL.md: unexpected skill name")
    return errors


def relative_links(text: str) -> set[str]:
    links = set()
    for target in re.findall(r"`((?:references|templates|scripts)/[^`]+)`", text):
        links.add(target)
    return links


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []

    for rel in REQUIRED:
        if not (root / rel).is_file():
            errors.append(f"missing required file: {rel}")

    skill_path = root / "SKILL.md"
    if skill_path.is_file():
        text = skill_path.read_text(encoding="utf-8")
        errors.extend(validate_frontmatter(text))
        for rel in sorted(relative_links(text)):
            if not (root / rel).exists():
                errors.append(f"SKILL.md references missing path: {rel}")

    # Guard against accidental empty reference/template files.
    for folder in ("references", "templates"):
        p = root / folder
        if p.is_dir():
            for md in p.glob("*.md"):
                if len(md.read_text(encoding="utf-8").strip()) < 80:
                    errors.append(f"suspiciously short file: {md.relative_to(root)}")

    if errors:
        print("VALIDATION FAILED")
        for err in errors:
            print(f"- {err}")
        return 1

    print("VALIDATION PASSED")
    print(f"Required files: {len(REQUIRED)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
