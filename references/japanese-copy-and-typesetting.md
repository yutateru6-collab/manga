# Japanese Copy and Typesetting

## Default: exact text outside generated pixels

For production ads, keep approved copy as text data and overlay it after artwork generation.

Image models can produce excellent art while still changing kanji, punctuation, small kana, or line order. Exact ad claims and CTAs should be deterministic.

## Copy rules

- Prefer spoken Japanese over translation-like marketing Japanese.
- One balloon = one thought.
- Delete information the image already communicates.
- Keep the strongest noun/verb near the beginning of a line.
- Avoid abstract piles such as “革新的・効率的・画期的”. Show the specific benefit.
- Use punctuation sparingly.
- Avoid excessive `！` and `…` unless character voice justifies it.
- Keep character voice consistent across panels.

## Balloon rules

- do not cover eyes, hands performing the product action, product UI, or proof
- tail direction must point unambiguously to the speaker
- leave internal padding
- avoid extremely wide one-line balloons on narrow mobile panels
- avoid more than 2–3 balloons in a small panel

## Line breaks

Break by semantic unit, not mechanically by character count.

Poor:

```text
覚えたつもりだ
った単語が翌日
には消えている
```

Better:

```text
覚えたつもりの単語、
翌日には
もう出てこない。
```

## Emphasis

Use one main emphasis device at a time:

- bold/weight
- size
- accent color
- short highlight box

Do not emphasize half the sentence.

## CTA

A CTA should describe one next action:

- 試してみる
- 無料で始める
- 使い方を見る
- 詳細を見る

Do not stack three actions in one final panel.

## Draft integrated-text QA

When text is rendered inside the generated image, compare character-by-character against approved copy for:

- kanji substitutions
- small ゃゅょ / っ
- dakuten/handakuten
- long vowel mark
- punctuation
- missing/duplicated characters
- line order
- speaker assignment

Any mismatch in a claim, price, offer, product name, or CTA is a blocking defect.
