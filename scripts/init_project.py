#!/usr/bin/env python3
"""Initialize an ad-manga project workspace."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

DIRS = [
    "brief",
    "strategy",
    "storyboard",
    "bible",
    "prompts/references",
    "prompts/panels",
    "prompts/pages",
    "artwork/references",
    "artwork/raw",
    "artwork/final",
    "qa",
]

FILES = {
    "brief/facts.md": "# Fact Ledger\n\n| Claim / asset | Status | Source | Allowed in ad? | Notes |\n|---|---|---|---|---|\n",
    "brief/audience.md": "# Audience\n\n- Primary segment:\n- Situation:\n- Pain/desire:\n- Objection:\n- Audience language:\n",
    "brief/constraints.md": "# Constraints\n\n- Placement/aspect:\n- Brand rules:\n- Must include:\n- Must avoid:\n- Compliance/risk notes:\n",
    "strategy/angle-matrix.md": "# Angle Matrix\n\n| # | Segment | Motivation | Hook | Visual hook | Promise | Mechanism | Proof | CTA | Risk |\n|---|---|---|---|---|---|---|---|---|---|\n",
    "strategy/selected-concept.md": "# Selected Concept\n\n- Angle:\n- Why selected:\n- Evidence:\n- What it tests:\n- Main risk:\n",
    "storyboard/storyboard.md": "# Storyboard\n",
    "storyboard/copy.md": "# Approved Copy\n\nKeep exact final Japanese copy here.\n",
    "bible/characters.md": "# Characters\n",
    "bible/scenes.md": "# Scenes\n",
    "bible/product.md": "# Product / UI\n",
    "bible/style.md": "# Visual Style\n\n- Reading direction:\n- Aspect ratio:\n- Rendering style:\n- Palette:\n- Panel borders:\n- Balloon style:\n- Text mode: production-text-safe\n",
    "qa/qa-report.md": "# QA Report\n\n| Severity | Tag | Location | Problem | Smallest safe fix | Status |\n|---|---|---|---|---|---|\n",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", help="Project directory")
    parser.add_argument("--title", default="Untitled Ad Manga")
    args = parser.parse_args()

    root = Path(args.output)
    root.mkdir(parents=True, exist_ok=True)
    for d in DIRS:
        (root / d).mkdir(parents=True, exist_ok=True)
    for rel, content in FILES.items():
        path = root / rel
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    manifest = root / "manifest.json"
    if not manifest.exists():
        manifest.write_text(
            json.dumps(
                {
                    "title": args.title,
                    "skill": "ad-manga-creator",
                    "text_mode": "production-text-safe",
                    "status": "initialized",
                    "selected_concept": None,
                    "assets": {"references": [], "raw": [], "final": []},
                    "qa": {"status": "not_started", "blocking_issues": []},
                },
                ensure_ascii=False,
                indent=2,
            ) + "\n",
            encoding="utf-8",
        )

    print(f"Initialized: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
