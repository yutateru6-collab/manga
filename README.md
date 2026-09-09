# ad-manga-creator

A Japanese advertising-manga Agent Skill that combines **ad strategy**, **comic storyboarding**, **visual continuity**, **image-generation prompting**, **exact Japanese typesetting**, and **production QA**.

It is designed for tasks such as:

- app/service promotional manga
- 4-panel social ads
- one-page manga ads
- product explainer comics
- X / Instagram / feed creative concepts
- manga-style performance creative variants
- iterative improvement of an existing ad comic

## Why this exists

A normal comic workflow optimizes for storytelling and visual consistency. A normal ad-creative workflow optimizes for hooks, motivations, proof, and conversion. High-quality ad manga needs both.

This skill adds a third requirement: **production-safe Japanese text**. Final ads default to an art-first workflow where exact Japanese text is typeset after image generation instead of trusting an image model to reproduce long copy perfectly.

## Key behavior

1. Build a claim/fact ledger.
2. Generate 5–10 genuinely different advertising angles.
3. Select concepts using evidence, relevance, visual potential, and risk.
4. Storyboard panel jobs before generating images.
5. Lock character/scene/product continuity.
6. Generate reusable references.
7. Generate artwork in draft or production text-safe mode.
8. Typeset exact Japanese copy.
9. Run ad + manga + visual + factual QA.
10. Revise only the broken unit.

## Repository layout

```text
SKILL.md
references/
  angle-and-hook-system.md
  grounding-and-compliance.md
  manga-storyboard-rules.md
  japanese-copy-and-typesetting.md
  character-consistency.md
  image-generation-prompts.md
  visual-qa.md
templates/
  brief.md
  angle-matrix.md
  4-panel-ad.md
  6-panel-ad.md
  one-page-ad.md
scripts/
  init_project.py
  validate_skill.py
examples/
  fictional-app-example.md
.github/workflows/
  validate.yml
```

## Quick start

```bash
python scripts/init_project.py ./projects/my-ad --title "My Ad Manga"
python scripts/validate_skill.py .
```

Then give the agent a grounded product brief and ask it to use `ad-manga-creator` in Concept, Storyboard, Draft, Production, or Iteration mode.

## Design note: two text modes

**Production mode (recommended):** generate clean art and empty/reserved speech balloons, then overlay exact Japanese text with a deterministic design/editing tool.

**Draft mode:** allow short text inside the generated image, then compare every rendered character to approved copy.

## License and acknowledgements

MIT licensed. See `LICENSE` and `NOTICE.md`.
