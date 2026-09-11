# Image Generation Prompt Templates

> **このファイルを直接参照する場合も、最初に [AGENTS.md](../AGENTS.md) と [SKILL.md](../SKILL.md) を全文読む。AGENTS.mdのゲートA・Bに従い、今回の全適用要件を理解してからプロンプト・画像を作成する。一部のテンプレートだけをコピーして他の指示を省略しない。**
>
> **最終納品はゲートC・Dに従う。プロンプトに書いた条件と、実際の全ページ・全コマ・全文字を照合し、違反・未確認があれば完成扱いにしない。ユーザー指定の枚数・人物・配置・変更範囲を既定プリセットより優先し、既存の正しい部分を保持する。**

Prompts should be self-contained. Replace brackets with project-specific facts.

## Character reference

```text
Create a reusable manga character reference sheet for [CHARACTER].

Role: [ROLE]
Visual style: [STYLE ANCHORS]
Immutable design:
- silhouette/body: [DETAILS]
- face/hair: [DETAILS]
- outfit: [DETAILS]
- accessories/props: [DETAILS]
- color anchors: [DETAILS]

Show: full-body front, 3/4 view, and one expression close-up if space allows.
Background: simple neutral studio background.
Do not add speech bubbles, text, extra characters, logos, or unrelated props.
The purpose is identity consistency for later manga panels.
```

## Scene reference

```text
Create a reusable manga scene reference for [SCENE].

Visual style: [STYLE ANCHORS]
Spatial anchors: [LAYOUT]
Fixed objects: [OBJECTS]
Lighting/time: [LIGHT]
Palette/materials: [PALETTE]
Camera: clear establishing view that makes spatial relationships easy to reuse.
Do not add main characters, text, watermarks, or unrequested branded objects.
```

## Production text-safe panel/page

```text
Create [ONE PANEL / COMPLETE PAGE] for a Japanese advertising manga.

Canvas/aspect: [ASPECT]
Reading direction: [DIRECTION]
Visual style: [STYLE]
Reference images and roles:
- [FILE]: canonical appearance reference for [CHARACTER/PRODUCT/SCENE]

Story beat: [ONE-SENTENCE BEAT]
Layout: [PANEL LAYOUT]

Panel details:
1. Job: [JOB]
   Camera: [SHOT]
   Character/action: [ACTION]
   Expression: [EMOTION]
   Scene: [SCENE]
   Product/UI: [STATE]
   Reserved text area: [LOCATION/SIZE]
2. ...

Text strategy: production text-safe. Keep speech balloons/caption boxes empty or leave clean reserved areas; do not invent lettering inside them.
Visual hierarchy: [PRIMARY > SECONDARY > CTA AREA]
Continuity: preserve all referenced character, clothing, product, and scene anchors.
Do not add extra people, text, watermarks, UI elements, logos, or props not requested.
Output one clean final artwork image.
```

## Draft integrated-text panel/page

```text
Create [ONE PANEL / COMPLETE PAGE] for a Japanese advertising manga.

Canvas/aspect: [ASPECT]
Reading direction: [DIRECTION]
Visual style: [STYLE]
Reference images: [REFERENCES]
Layout: [LAYOUT]

Use ONLY this approved visible copy:
- Panel 1: 「[COPY]」
- Panel 2: 「[COPY]」
...

Do not paraphrase, translate, add, remove, or duplicate any visible wording.
Keep text large, high-contrast, and away from complex backgrounds.
Preserve referenced character/product continuity.
No extra text, watermark, page number, or unrequested logo.
```

## Theme-to-4-page short manga preset

Use this as a separate story-manga mode when the user gives only a theme and wants a short, complete manga rather than an advertisement.

```text
Create a complete Japanese short manga from the following theme.

Theme: [THEME]
Tone: [SURREAL / DARK COMEDY / SF / IRONIC / HORROR / HEARTWARMING / OTHER]
Target reader: [OPTIONAL]
Text density: [LOW / MEDIUM]

Core format:
- Exactly 4 pages / 4 final images.
- Each image is one complete manga page.
- Clear beginning, development, escalation, and payoff.
- The ending MUST contain a real punchline, twist, reversal, irony, or unsettling final implication.
- Do not merely stop the story. The final panel or final line should change how the reader interprets what came before.
- Keep dialogue and narration concise and natural Japanese.
- Prioritize readability over decorative detail.

Story structure:
Page 1 — Setup
- Introduce protagonist, world, and the unusual premise quickly.
- Establish the key visual motif or object.
- End with curiosity or a small disturbance.

Page 2 — Development
- Show how the premise works.
- Let the protagonist participate or benefit.
- Increase scale, consequence, or absurdity.

Page 3 — Escalation
- Reveal that the phenomenon has spread, changed society, or contains a hidden layer.
- Plant the final clue or transition into the twist.
- End with a question, discovery, or ominous reveal.

Page 4 — Payoff
- Reveal the hidden truth or unexpected logic.
- Deliver the twist cleanly.
- Make the final panel or final line the strongest beat of the whole manga.
- Avoid over-explaining after the punchline.

Visual style:
- High-quality Japanese manga page design.
- Mostly black-and-white / grayscale with screen tones or ink shading.
- Use selective spot color only, not full color.
- Keep panel borders clean and reading flow obvious.
- Vary shot size: establishing shots, medium shots, close-ups, and one strong reveal shot where appropriate.
- Expressions must clearly communicate the emotional beat.
- Keep backgrounds detailed enough to establish place, but never so busy that text becomes hard to read.

Selective-color rule:
Use only 2–3 accent colors across the entire 4-page story.
Recommended meanings:
- deep red: danger, advertising, warning, desire, irony, social pressure
- cyan / cool blue: technology, memory, systems, machines, alien or abnormal light
- muted green: company logo, institutional reassurance, controlled normality
- yellow only when specifically useful for warning or uncanny emphasis

Color only the story-important targets, such as:
1. the central symbolic object
2. the abnormal device or technology
3. a repeated logo, sign, interface, or institutional symbol
4. one emotional symbol when necessary
5. the final reveal if color strengthens the punchline

Do NOT color:
- ordinary skin, clothes, buildings, and backgrounds unless the story specifically requires it
- large areas merely for decoration
- every sound effect or every panel

Title:
- Add a clear title at the top of page 1.
- Use the same title treatment or a reduced running-title treatment on pages 2–4 when appropriate.
- The title should fit the story tone and should not spoil the twist.

Panel numbering:
- Add a tiny reading-order number to the edge/corner of EVERY panel.
- Numbers must be very small and unobtrusive.
- Use tiny circled numerals or tiny boxed numerals.
- Number each panel exactly once.
- No duplicated numbers.
- No missing numbers.
- Follow natural Japanese manga reading order for the actual layout.
- The number is only a reading aid and must never compete with dialogue or artwork.

Page numbering:
- Add a tiny page marker at the bottom-right of each page:
  1/4, 2/4, 3/4, 4/4

Text rules:
- Japanese must sound natural and concise.
- Keep each speech balloon short enough to read at normal phone size.
- Avoid paragraph-length balloons.
- Prefer dialogue and images over explanatory narration.
- Keep important text large, high-contrast, and away from complex backgrounds.
- Do not duplicate the same information in narration and dialogue.
- Do not invent extra slogans or copy unless they serve the story.

Continuity rules:
- Lock protagonist face, hair, age, outfit, and silhouette across all 4 pages.
- Lock recurring supporting characters.
- Lock the shape and color treatment of important props, vehicles, devices, logos, signs, and locations.
- Use page 1 as a visual anchor for later pages when image-reference conditioning is available.
- Preserve the same manga rendering language and spot-color palette across all pages.

Before image generation, internally design:
1. three title candidates
2. the selected title
3. the protagonist visual bible
4. recurring object / logo / device bible
5. the 4-page story outline
6. page-by-page panel plan
7. exact approved Japanese dialogue / narration
8. spot-color plan and meaning
9. continuity anchors
10. final punchline test

Punchline test:
Before generating, verify all of the following:
- Is there a genuine final turn rather than a simple ending?
- Does the twist follow logically from clues already shown?
- Is the last line or last image stronger than the explanation before it?
- Can any explanatory sentence after the twist be deleted?
- Does the reader understand the irony without an extra paragraph?
If not, revise the story before drawing.

Generation procedure:
- Generate page 1 first as the canonical visual reference.
- Use page 1 as the visual anchor for pages 2–4 whenever reference-image editing/conditioning is available.
- Preserve all characters, props, logo shapes, vehicle shapes, and palette anchors.
- If generating pages 2–4 together, explicitly reference page 1 and repeat the fixed continuity rules.
- If text quality is unreliable, generate short readable text only and repair exact Japanese afterward rather than accepting broken lettering.

Per-page image prompt template:
Create page [N] of 4 of the same Japanese short manga.

Title: [TITLE]
Theme: [THEME]
Tone: [TONE]
Canvas/aspect: portrait manga page, approximately A-series proportion / 1000:1414 or equivalent.
Reading direction: natural Japanese manga order.
Visual style: mostly grayscale Japanese manga, selective spot color only, crisp line art, readable speech balloons, balanced panel spacing.
Reference image: page 1 is the canonical appearance reference for all recurring characters, props, vehicles, devices, logos, and color anchors.

Page role: [SETUP / DEVELOPMENT / ESCALATION / PAYOFF]
Page beat: [ONE-SENTENCE PAGE PURPOSE]

Panel 1:
- job: [JOB]
- shot: [SHOT]
- action: [ACTION]
- expression: [EXPRESSION]
- exact visible text: 「[TEXT]」
- spot color: [NONE / RED / CYAN / GREEN / OTHER]

Panel 2:
...

Panel-order markers:
- add one tiny unobtrusive number to each panel corner
- number every panel exactly once
- no duplicate or missing numbers

Page marker: [N]/4 in very small type at bottom right.

Continuity:
- preserve all recurring character identities exactly
- preserve recurring object and logo geometry
- preserve grayscale base and the same 2–3 accent colors
- do not add unrequested characters, props, text, logos, or panels

Typography:
- large readable Japanese
- short balloons
- high contrast
- clean line breaks
- no clipped text

Output one clean final manga page image.
```

### Theme-to-4-page QA checklist

Before approving the 4 pages, verify:

- exactly 4 pages exist
- every page has clear reading flow
- every panel has one tiny unique reading-order number
- page markers are correct: 1/4, 2/4, 3/4, 4/4
- title is present and does not spoil the twist
- spot color is limited and meaningful
- no unnecessary full-color regions
- character identity is consistent across pages
- recurring object/device/logo geometry is consistent
- Japanese text is natural and readable
- no duplicated, missing, or garbled text
- the final page contains a genuine punchline/twist
- the final panel or line is the strongest beat

## Localized repair prompt

```text
Edit only the following defect(s):
- [DEFECT]

Preserve everything else: composition, character identity, clothing, scene, product geometry, panel layout, palette, and all already-correct elements.
Do not introduce new text or objects.
```

## Prompt anti-patterns

Avoid:

- “make it engaging” without specifying what visually earns attention
- long character prose with no immutable anchors
- asking the model to invent an accurate app screen
- mixing draft text instructions with “leave balloons empty”
- changing style adjectives between panels
- using contradictory camera/layout directions
- requesting many repair changes in one regeneration when only one defect matters
