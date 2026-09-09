---
name: ad-manga-creator
description: Create evidence-grounded Japanese advertising manga/comic creatives from product facts through angle exploration, storyboard, character/scene continuity, image-generation prompts, production-safe Japanese typesetting, and visual QA. Use for ad manga, promotional comics, 4-panel ads, one-page manga ads, social comic creatives, app/product promotion comics, or when converting a product brief into image-generation-ready comic advertising concepts.
metadata:
  version: 1.0.0
---

# Ad Manga Creator

Create advertising manga that works first as an ad and second as a comic.

The skill combines performance-creative thinking with a comic production workflow. It does **not** assume that a pretty manga page is an effective ad, and it does **not** invent product claims, testimonials, statistics, reviews, prices, features, screenshots, awards, or customer outcomes.

## Core principles

1. **Ground before generating.** Separate verified product facts from assumptions. Unknowns stay unknown.
2. **Explore angles before drawing.** Produce meaningfully different motivations and hooks, not many rewrites of the same idea.
3. **The first panel must earn attention.** It should create recognition, tension, curiosity, contrast, or proof without misleading the viewer.
4. **Every panel has one job.** Do not overload a panel with exposition, multiple claims, and multiple actions.
5. **Show the mechanism when possible.** A product demonstration, screen state, workflow change, or concrete behavior is stronger than generic praise.
6. **Preserve continuity.** Characters, clothing, props, product UI, locations, palette, and reading direction must remain stable unless the story requires a change.
7. **Prefer exact text over baked-in text.** For production, generate artwork separately and typeset Japanese copy afterward. Use integrated AI-rendered text only for drafts or very short text.
8. **One-variable revisions.** When fixing a failed creative, preserve what works and change the smallest responsible unit.
9. **Mobile readability wins.** A comic that requires zooming is not a usable social ad.
10. **Truth beats hype.** A less dramatic claim that is supported is better than a stronger invented claim.

## Modes

### Mode A — Concept only
Deliver angle matrix + recommended concepts. Do not generate final image prompts unless requested.

### Mode B — Storyboard
Deliver selected concept, panel-by-panel storyboard, copy, continuity notes, and asset plan.

### Mode C — Draft image
Generate or brief a fast proof-of-concept comic. Short text may be baked into the image, but exact wording must be checked afterward.

### Mode D — Production
Use the full pipeline: grounded brief → angle selection → storyboard → visual bible → reference images → text-safe artwork → exact Japanese typesetting → QA → revision.

### Mode E — Iteration
Analyze an existing ad manga and performance or review feedback. Diagnose whether the problem is hook, story bridge, proof, offer/CTA, visual clarity, text readability, or continuity. Change one major variable at a time.

## Required working files

For a production job, maintain:

```text
project/
  brief/
    facts.md
    audience.md
    constraints.md
  strategy/
    angle-matrix.md
    selected-concept.md
  storyboard/
    storyboard.md
    copy.md
  bible/
    characters.md
    scenes.md
    product.md
    style.md
  prompts/
    references/
    panels/
    pages/
  artwork/
    references/
    raw/
    final/
  qa/
    qa-report.md
  manifest.json
```

Use `scripts/init_project.py` when a filesystem is available.

## Workflow

### 1. Build the fact ledger

Read the user's supplied product/app/site/material first. Record:

- product name and category
- target user
- verified features
- verified price/offer only if current and supplied or checked
- verified differentiators
- verified proof: analytics, real reviews, case studies, screenshots, demos, awards
- brand voice and visual constraints
- prohibited or risky claims
- desired action after the comic
- target placement/aspect ratio

Mark each substantive claim as one of:

- `VERIFIED` — directly supported by supplied/current source
- `USER-PROVIDED` — stated by the user but not independently verified
- `UNKNOWN` — do not use as a claim
- `INFERENCE` — may guide concepting but must not be presented as a fact

Never convert an inference into ad copy that sounds factual.

See `references/grounding-and-compliance.md`.

### 2. Generate an angle matrix

Create 5–10 **distinct** advertising angles before choosing a story. Vary the underlying motivation, not just wording.

Each angle includes:

| Field | Meaning |
|---|---|
| Segment | The specific situation/person this angle addresses |
| Motivation | Pain, desire, objection, identity, habit, or trigger |
| Hook move | Recognition, curiosity, contrast, proof-first, confession, question, etc. |
| Visual hook | What the first panel literally shows |
| Promise | What the viewer is invited to believe/expect |
| Mechanism | How the product plausibly produces value |
| Proof | What real evidence can appear |
| Story shape | Which manga structure fits |
| CTA | The next action |
| Risk | Unsupported claim, clutter, weak proof, compliance issue, etc. |

Do not choose merely by personal taste. Rank concepts with the heuristic in `references/angle-and-hook-system.md`, then explain why the strongest 1–3 are worth producing.

### 3. Choose a manga advertising structure

Use one of the structures in `references/manga-storyboard-rules.md`, such as:

- Recognition → Friction → Discovery → Payoff → CTA
- Failed old way → Contrast → New mechanism → Proof → CTA
- Objection → Demonstration → Evidence → Resolution → CTA
- Founder/problem origin → Build → Product → Specific benefit → CTA
- Before → Turning point → After, with honest comparable states
- Mini demo story: task → product action → result → next action

Do not force a four-act literary story when a two-beat demo sells the idea better.

### 4. Write the storyboard before prompting images

For every panel specify:

- panel job
- shot size and camera
- location/background
- characters and exact continuity state
- action
- facial expression/body language
- product/UI state
- visual hierarchy
- dialogue/narration/SFX
- maximum text budget
- transition to next panel
- continuity warnings

A panel should have a single dominant message. If two panels can be merged without losing clarity, merge them. If a panel requires a paragraph, rewrite it.

### 5. Build the visual bible

Before multi-panel generation, lock reusable design facts.

**Characters**
- silhouette/body proportions
- face/hair
- age presentation
- outfit and accessories
- color anchors
- recurring props
- expression range
- forbidden changes

**Scenes**
- spatial layout
- key furniture/landmarks
- lighting/time
- reusable anchors
- forbidden changes

**Product**
- logo handling
- device/product shape
- UI/screenshot source
- colors
- features that may be shown
- features that must not be fabricated

**Style**
- rendering language
- line weight
- shading
- palette
- panel border language
- speech bubble style
- reading direction
- aspect ratio

See `references/character-consistency.md`.

### 6. Choose the text strategy

Use **Production text-safe mode by default** for final ads.

#### Production text-safe mode
1. Generate artwork with empty/clean speech balloons or reserved text areas.
2. Keep exact copy in `storyboard/copy.md`.
3. Add Japanese text in a deterministic layout tool or editing step.
4. Re-check punctuation, kana/kanji, line breaks, emphasis, and CTA.

Advantages:
- exact wording
- consistent fonts
- easier copy revision
- fewer AI text artifacts
- easier localization

#### Draft integrated-text mode
Use only when speed matters more than exact typography or when text is extremely short. After generation, compare every visible character against the approved copy. Regenerate or overlay any incorrect text.

See `references/japanese-copy-and-typesetting.md`.

### 7. Create reference images first

For recurring characters, products, or scenes, create reference sheets before final panels/pages.

Each reference prompt must include:
- subject role
- immutable appearance anchors
- palette
- front/3-quarter/side views if useful
- neutral pose when used as a reusable identity reference
- explicit exclusions

Do not rely on prose alone for long multi-page continuity when reference-image conditioning is available.

### 8. Generate panels/pages with self-contained prompts

Each generation prompt must contain enough context to stand alone:

- output aspect ratio
- visual style anchors
- reference-image roles
- panel layout
- reading direction
- exact character states
- camera/action/emotion
- product/UI state
- reserved text areas or approved short text
- hierarchy and mobile-readability constraints
- negative constraints

Use `references/image-generation-prompts.md`.

For multi-page work, isolate generations enough to reduce accidental state contamination. Keep a generation log and name outputs deterministically.

### 9. Perform visual QA

Do not approve a creative because it is attractive. Check the final artifact against `references/visual-qa.md`.

At minimum verify:

**Ad logic**
- first panel stops/earns attention
- story continues the hook rather than abandoning it
- product appears at the right moment
- mechanism/benefit is understandable
- proof is real
- CTA is clear

**Comic logic**
- panel order is unmistakable
- gaze/action flow supports reading direction
- characters remain identifiable
- geography and props do not teleport without reason
- emotional progression is legible

**Text**
- exact Japanese copy
- natural phrasing
- no mojibake/gibberish
- no clipped balloons
- sufficient contrast and size
- sensible line breaks
- no duplicated headline/dialogue doing the same job

**Product truth**
- no invented screen, feature, statistic, review, certification, award, price, or result
- logo/product geometry is not misleading
- UI is either an accurate source-based rendering or clearly illustrative

**Image integrity**
- hands/eyes/objects are plausible enough for the intended style
- no extra fingers/limbs/duplicate characters
- no unintended text/watermark
- no accidental brand/competitor marks
- no crop removes essential action or CTA

### 10. Revise surgically

Tag every issue as one of:

- `HOOK`
- `STORY`
- `COPY`
- `LAYOUT`
- `CONTINUITY`
- `PRODUCT_TRUTH`
- `TEXT_RENDERING`
- `IMAGE_ARTIFACT`
- `CTA`
- `COMPLIANCE`

Revise the smallest affected unit. If panel 3 has a bad hand, do not rewrite the hook. If the hook is weak, do not spend time polishing panel 6 first.

### 11. Deliver with an audit trail

Final handoff should include:

- selected concept and rationale
- final copy
- final artwork(s)
- fact ledger / claim sources
- known limitations
- QA status
- optional alternate hooks for the next test

For performance iteration, record what changed and why.

## Default output presets

When the user gives no format, choose based on the publishing surface and task. If the surface is unknown, prefer one of these neutral presets and state it:

- square: 1:1
- feed portrait: 4:5
- story/reel portrait: 9:16
- landscape/social card: 16:9

Do not assert current platform pixel requirements from memory when the exact specification matters; verify current official specs if browsing is available.

## Failure modes to prevent

- starting image generation before the ad angle is clear
- 10 concepts that are only headline rewrites
- generic "product changed my life" praise without mechanism or proof
- fabricated user reviews or fake star ratings
- fake urgency/countdowns
- character drift between panels
- product UI invented from memory
- too much Japanese copy inside generated pixels
- speech balloons covering faces or product actions
- CTA added as an afterthought
- hook promises one story and panel 2 starts a different pitch
- re-generating an entire good page to fix one localized defect
- treating visual polish as evidence of advertising effectiveness

## References

Read only the files relevant to the current stage:

- Strategy: `references/angle-and-hook-system.md`
- Grounding/compliance: `references/grounding-and-compliance.md`
- Storyboarding: `references/manga-storyboard-rules.md`
- Japanese text: `references/japanese-copy-and-typesetting.md`
- Continuity: `references/character-consistency.md`
- Image prompting: `references/image-generation-prompts.md`
- QA: `references/visual-qa.md`
