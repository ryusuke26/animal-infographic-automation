# Automation 2 Production Policy

This file is the operating policy for the recurring automation:

`世界の知らない生きものインフォグラフィック日次制作`

Use this policy to keep the automation from drifting as the archive grows. The automation prompt should be self-contained, but this file is the human-readable source of truth for how the workflow is organized.

## Responsibility Map

| Area | Source of truth | Purpose |
|---|---|---|
| Execution instructions | `automation-2-updated-prompt.md` | Text to paste into the Automation body. |
| Completed/incomplete topic index | `infographic-packages/INDEX.md` | Lightweight archive table and repeat-avoidance ledger. |
| Package artifacts | `infographic-packages/YYYY-MM-DD-species-slug/` | Canonical package folder for each run. |
| Posting images | `infographic-packages/YYYY-MM-DD-species-slug/images/` | Canonical folder for separate direct Japanese and English Image Gen posters. |
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
- Separate direct Japanese and English Image Gen poster PNGs exist and use the locked copy.
- Both Image Gen posters pass visual identity QA: the species-specific body plan, distinctive structures, posture, habitat cues, and language-specific text are coherent enough for public posting.
- Text-safe SVG/PNG assets exist when useful for editing or backup.
- `infographic-packages/INDEX.md` is updated.
- Automation memory is updated.

If Image Gen fails, is unavailable, one language is missing, or either poster produces species/anatomy-breaking art, keep the package artifacts but mark the topic as `incomplete` or `needs review`. A base illustration or deterministic bilingual layout does not replace the required direct Japanese and English Image Gen posters.

## Fixed Workflow

Every run follows this order:

1. Preflight and pending-publication check.
2. Topic and region lock.
3. Evidence Lock.
4. Copy Lock.
5. Direct Japanese and English Image Gen poster production, with optional deterministic text-safe backups.
6. Visual and mechanical QA.
7. INDEX and automation-memory update.

Image Gen must not start before Evidence Lock and Copy Lock. The exact scientific name, status year/category, native region, three core claims, titles, labels, and footer must be settled and saved first.

Do not change facts or wording during image generation. If a factual correction is needed, return to Evidence Lock and Copy Lock before generating again. Use one targeted retry at a time for anatomy, posture, habitat, major composition, or generated-text failure. Deterministic text-safe assets may be repaired independently, but they do not replace either required direct Image Gen poster.

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

Text-safe backups should use:

```text
species_slug_japanese_textsafe_YYYY-MM-DD.png
species_slug_english_textsafe_YYYY-MM-DD.png
species_slug_japanese_textsafe_YYYY-MM-DD.svg
species_slug_english_textsafe_YYYY-MM-DD.svg
```

Text-free base art may be retained as an optional working asset, but it is not a final deliverable and cannot satisfy either language requirement.

Generated-image mirror copies under `.codex/generated_images/animal_img` are optional. If permissions fail, record it, but do not fail the run if package-local Image Gen PNGs exist.

## Encoding Rules

- Treat all package Markdown, text, SVG, and index files as UTF-8.
- When reading or writing Japanese text from PowerShell, explicitly use UTF-8, for example `Get-Content -Encoding UTF8` and `Set-Content -Encoding UTF8`.
- If Japanese common names, hashtags, or series labels display as mojibake, re-read the file as UTF-8 before editing or making a QA decision.

## Repeat-Avoidance Order

Before selecting a topic, check in this order:

1. `C:\Users\ryusu\.codex\automations\automation-2\memory.md`
2. `C:\Users\ryusu\Documents\New project 2\infographic-packages\INDEX.md`
3. Existing folders under `C:\Users\ryusu\Documents\New project 2\infographic-packages`

Use the absolute memory path when `$CODEX_HOME` is empty or unavailable. The static completed list in the automation prompt is only a fallback cue. Memory and `INDEX.md` are more current.

## Topic Selection

- Do not limit selection to the Pyrenees.
- Prioritize overlooked animals, plants, fungi, or unusual ecosystems.
- Assign each candidate a broad native region: Africa, Asia, Europe, North America, Central America/Caribbean, South America, Australia/Oceania, or Ocean/Global.
- Review the most recent 8 completed packages before selection.
- Prefer regions with 0 appearances and avoid a region already used 2 or more times when a credible underrepresented alternative exists.
- Avoid the same broad region in consecutive runs.
- Australia/Oceania is currently on cooldown because it is overrepresented in the recent archive; resume it only when the rolling rule allows.
- Choose a different lineage, habitat, region, and ecological hook where practical.
- Avoid completed species unless the user explicitly requests a remake or comparison.
- Reuse incomplete topics only when deliberately completing missing deliverables.
- User-requested topics, dated awareness days, and deliberate remakes may override region rotation when the reason is recorded.

## Fact-Check Rules

- Use authoritative sources first.
- Use IUCN Red List for global conservation status when relevant.
- Use national or regional red lists only with the jurisdiction clearly labeled.
- Use CITES or official legal listings when trade or legal protection is mentioned.
- Use peer-reviewed papers or official monitoring/recovery reports for range, habitat, behavior, population, threats, and unusual traits.
- Do not include population numbers unless they are current, geographically specific, and clearly sourced.
- Do not transfer facts from related species onto the selected species unless clearly labeled as related-species context.
- If sources disagree or are outdated, state uncertainty and use publication-safe wording.
- Evidence Lock requires the accepted name, native region, exact status footer and year, three core public claims, and visual identity guidance to be settled before image work.

## Tone Rules

- Discovery and education first.
- No savior framing.
- No blame framing.
- No advocacy slogans.
- No unsupported urgency.
- Conservation/status appears quietly in a footer, not as the emotional center.

## Copy Lock

- Write final Japanese and English titles, scientific name, three observation labels, footer, infographic copy, X copy, ALT text, and image prompts before Image Gen.
- Save the locked copy to the package folder.
- Do not leave placeholders or unresolved dates/categories in image-facing text.
- Recheck image-facing claims against `sources-qa.md` before generating art.

## Image Rules

- Use Image Gen for every completed package, after Evidence Lock and Copy Lock.
- Generate separate complete Japanese and English posters with Image Gen after both locks.
- Keep both accepted direct Image Gen poster PNGs in the package.
- Both language versions are completion requirements, even when they share the same composition.
- Deterministic text-safe SVG/PNG files are optional editing and fallback assets, not substitutes for either direct Image Gen poster.
- Use childlike crayon/oil-pastel field-notebook poster style.
- Japanese-version posters should use the Japanese name or safe Japanese rendering as the main title.
- English-version posters should use the English common name as the main title.
- Use the exact locked text verbatim in each Image Gen prompt.
- If generated text or visual structure fails, make one targeted retry and re-check it. Do not alter facts, labels, or workflow during the retry.
- Image QA must check the organism's body plan, distinctive structures, limb/appendage count, posture, and habitat. If the poster is merely cute or atmospheric but the anatomy/identity is wrong, mark it `needs review` instead of `completed`.
- For species with difficult anatomy, avoid forcing dramatic poses that Image Gen repeatedly breaks. Use a safer natural posture and explain the behavior in labels or inset diagrams.
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
- Use 0 to 2 relevant hashtags only. For Japanese posts in this series, default to the fixed series tag `#世界の知らない生き物`.
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
- Update `C:\Users\ryusu\.codex\automations\automation-2\memory.md`.
- Record the broad native region in the INDEX Notes field and automation memory.
- Record whether Evidence Lock and Copy Lock were completed before Image Gen.
- Record whether separate direct Japanese and English Image Gen posters exist and pass QA.
- Record whether optional deterministic text-safe backups exist.
- Record whether generated_images mirror succeeded or failed.
- Record whether the package is local-ready or published.
- Record whether the topic should be avoided next time.
