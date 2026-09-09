# Image Generation Prompt Templates

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
