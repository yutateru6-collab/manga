# ad-manga-creator

## 制作前の必読順・完成条件

最初に [AGENTS.md](AGENTS.md) を全文読み、続いて [SKILL.md](SKILL.md)、[画像生成プロンプト](references/image-generation-prompts.md)、今回のモードに適用される各参照規則を末尾まで読む。

**全文読了 → 全要件の意味・適用範囲・実装先・検証方法を整理 → 制作へ実装 → 最終成果物で全要件を検証**を必須とする。一部だけ読んで作り始めない。「理解した」「プロンプトに書いた」だけで合格にしない。画像制作では全ページ・全コマ・全文字を確認し、違反・未確認があれば完成扱いにしない。詳しい適用条件と検証手順はAGENTS.mdに従う。

2026-09-11にこの遵守手順を追加した。既存の広告・短編・文字組み・修正ルールは維持する。指示の更新は、既存画像の修正や新しい自動画像検査機能の実装を意味しない。

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
AGENTS.md
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
