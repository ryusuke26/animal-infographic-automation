# Automation 2 Production Policy

This file is the operating policy for the recurring automation:

`世界の知らない生きものインフォグラフィック日次作成`

Use this policy to keep the automation from drifting as the archive grows. The automation prompt should be self-contained, but this file is the human-readable source of truth for how the workflow is organized.

## Responsibility Map

| Area | Source of truth | Purpose |
|---|---|---|
| Execution instructions | `automation-2-updated-prompt.md` | Text to paste into the Automation body. |
| Completed/incomplete topic index | `infographic-packages/INDEX.md` | Lightweight archive table and repeat-avoidance ledger. |
| Package artifacts | `infographic-packages/YYYY-MM-DD-species-slug/` | Canonical package folder for each run. |
| Posting images | `infographic-packages/YYYY-MM-DD-species-slug/images/` | Canonical image folder for Image Gen PNGs and text-safe backups. |
| Optional mirror | `C:\Users\ryusu\.codex\generated_images\animal_img\species-slug` | Convenience copy only; never the source of truth. |
| Run history | `$CODEX_HOME/automations/automation-2/memory.md` | Chronological decisions, failures, fixes, and preferences. |

## Completion Standard

A package is `completed` only when all of these are true:

- Fact-check table exists.
- Japanese and English infographic copy exist.
- Japanese and English image prompts exist.
- Japanese and English X posts and ALT text exist.
- X free-version thread drafts exist when a 140-character standalone post would be too vague.
- Compact source list exists.
- Image Gen raster PNGs exist for both Japanese and English versions.
- Text-safe SVG/PNG backups exist when generated text may be unreliable.
- `infographic-packages/INDEX.md` is updated.
- Automation memory is updated.

If Image Gen fails or is unavailable, keep the package artifacts but mark the topic as `incomplete` or `needs review`. SVG-only or SVG-derived PNG-only packages are not completed.

## Canonical Storage

Always create the package first:

```text
C:\Users\ryusu\Documents\New project 2\infographic-packages\YYYY-MM-DD-species-slug
```

Always create package-local images:

```text
C:\Users\ryusu\Documents\New project 2\infographic-packages\YYYY-MM-DD-species-slug\images
```

Use stable ASCII filenames:

```text
species_slug_japanese_imagegen_YYYY-MM-DD.png
species_slug_english_imagegen_YYYY-MM-DD.png
species_slug_japanese_textsafe_YYYY-MM-DD.svg
species_slug_english_textsafe_YYYY-MM-DD.svg
```

Generated-image mirror copies under `.codex/generated_images/animal_img` are optional. If permissions fail, record it, but do not fail the run if package-local Image Gen PNGs exist.

## Repeat-Avoidance Order

Before selecting a topic, check in this order:

1. `$CODEX_HOME/automations/automation-2/memory.md`
2. `C:\Users\ryusu\Documents\New project 2\infographic-packages\INDEX.md`
3. Existing folders under `C:\Users\ryusu\Documents\New project 2\infographic-packages`

The static completed list in the automation prompt is only a fallback cue. Memory and `INDEX.md` are more current.

## Topic Selection

- Do not limit selection to the Pyrenees.
- Prioritize overlooked animals, plants, fungi, or unusual ecosystems.
- Choose a different lineage, habitat, region, or ecological hook from the most recent 3-5 completed topics.
- Avoid completed species unless the user explicitly requests a remake or comparison.
- Reuse incomplete topics only when deliberately completing missing deliverables.

## Fact-Check Rules

- Use authoritative sources first.
- Use IUCN Red List for global conservation status when relevant.
- Use national or regional red lists only with the jurisdiction clearly labeled.
- Use CITES or official legal listings when trade or legal protection is mentioned.
- Use peer-reviewed papers or official monitoring/recovery reports for range, habitat, behavior, population, threats, and unusual traits.
- Do not include population numbers unless they are current, geographically specific, and clearly sourced.
- Do not transfer facts from related species onto the selected species unless clearly labeled as related-species context.
- If sources disagree or are outdated, state uncertainty and use publication-safe wording.

## Tone Rules

- Discovery and education first.
- No savior framing.
- No blame framing.
- No advocacy slogans.
- No unsupported urgency.
- Conservation/status appears quietly in a footer, not as the emotional center.

## Image Rules

- Use Image Gen for every completed package.
- Generate both Japanese and English raster poster images.
- Use childlike crayon/oil-pastel field-notebook poster style.
- Japanese-version posters should use the Japanese name or safe Japanese rendering as the main title.
- English-version posters should use the English common name as the main title.
- If generated text is unreliable, keep the Image Gen PNGs and add text-safe SVG/PNG backups.
- Avoid fake maps, unsupported visual claims, blame/rescue imagery, and unsupported population visuals.

## Caption Rules

Japanese captions should follow this compact structure:

```text
[curiosity-first poetic Japanese line]
[English common name]
[Scientific name]

[short paragraph about habitat and behavior]
[short line about visible trait or unusual ecology]
[species-specific final line using ちょっと不思議な暮らし。]

IUCN Red List [assessment year]: [category] ([abbreviation])
```

The final "ちょっと不思議な暮らし" line must be species-specific, not generic.

## X Posting Rules

- Start with a strong curiosity hook.
- Use 0 to 2 relevant hashtags only.
- Add ALT text for each image.
- Keep the main post understandable; do not over-compress until the species/topic becomes unclear.
- If the target is X free-version posting or a 140-character limit, prefer a short thread over a vague standalone caption.
- Recommended 140-character thread structure: main post names the species/topic and hook; reply 1 says what it is and where it lives; reply 2 gives the distinctive trait or behavior; reply 3 gives quiet status and sources.
- Keep every thread post under 140 characters when the free-version constraint applies.
- Put sources or extra context in replies when useful.
- Use ALT text for image description and image-text support; do not make ALT the only place where the core explanation lives.
- Prefer separate Japanese and English posts.
- Keep a repeatable series identity, such as "世界の知らない生きもの" or "ちょっと不思議な暮らし図鑑".

## End-of-Run Updates

Before finishing every run:

- Update `infographic-packages/INDEX.md`.
- Update `$CODEX_HOME/automations/automation-2/memory.md`.
- Record whether Image Gen PNGs exist.
- Record whether generated_images mirror succeeded or failed.
- Record whether the topic should be avoided next time.
