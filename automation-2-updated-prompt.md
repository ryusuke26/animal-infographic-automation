# Automation: 世界の知らない生きものインフォグラフィック日次作成

Operational policy reference:

```text
C:\Users\ryusu\Documents\New project 2\automation-2-production-policy.md
```

This prompt is the text to paste into the Automation body. The policy file explains the archive/storage responsibilities, but this prompt remains self-contained for execution.

Create one curiosity-first biological infographic package about a lesser-known living thing from anywhere in the world. Do not limit the selection to the Pyrenees. Prioritize overlooked animals, plants, fungi, or unusual ecosystems that can invite natural-history curiosity without moralizing.

Use the bio-discovery-infographic style: discovery and education first, no savior framing, no blame, no urgency slogans, conservation/status as a quiet footer only.

## Memory and Repeat-Avoidance

Before selecting a topic, read these in order:

```text
$CODEX_HOME/automations/automation-2/memory.md
C:\Users\ryusu\Documents\New project 2\infographic-packages\INDEX.md
C:\Users\ryusu\Documents\New project 2\infographic-packages
```

Avoid repeating completed/generated species unless the user explicitly requests a remake or comparison.

Completed species should be determined from automation memory, `INDEX.md`, and existing package folders, not only from the static list in this prompt.

Completed / do not repeat:

- Pink Fairy Armadillo / ヒメアルマジロ / *Chlamyphorus truncatus*
- Olm / オルム / *Proteus anguinus*
- Indian Purple Frog / Purple Frog / ムラサキガエル / *Nasikabatrachus sahyadrensis*
- Hispaniolan Solenodon / ヒスパニオラソレノドン / *Solenodon paradoxus*
- Star-nosed Mole / ホシバナモグラ / *Condylura cristata*
- Long-eared Jerboa / オオミミトビネズミ / *Euchoreutes naso*
- Yeti crab / イエティクラブ / *Kiwa hirsuta*

Not completed:

- Lowland Streaked Tenrec / シマテンレック / *Hemicentetes semispinosus* was a failed/incomplete generation and should not be counted as completed.

## Fact-Check Requirements

Fact-check rigorously before writing final copy. Use authoritative sources first:

- IUCN Red List for global status when relevant.
- National/regional red lists only with jurisdiction clearly labeled.
- CITES or official legal listings when trade/protection is mentioned.
- Peer-reviewed papers or official monitoring/recovery reports for population, range, habitat, behavior, threats, and unusual traits.

Cross-check:

- common name
- scientific name
- taxonomy
- range
- habitat
- behavior
- conservation status
- population claims
- threats
- image identity guidance

Do not include population numbers unless they are current, geographically specific, and clearly sourced. If sources disagree or are outdated, state the uncertainty and use publication-safe wording.

## Deliverables

Produce both Japanese and English versions:

1. Species/topic selection rationale.
2. Claim-by-claim fact-check table with verdicts, corrected wording, source links, and confidence.
3. Short Japanese infographic copy.
4. Short English infographic copy.
5. Japanese image-generation prompt for a childlike crayon/oil-pastel field-notebook poster.
6. English image-generation prompt for the matching English version.
7. Japanese X post, ALT text, and optional source reply.
8. English X post, ALT text, and optional source reply.
9. Compact source list with dates or assessment years where available.
10. Use Image Gen to generate both Japanese and English raster poster images and save final artifacts plus notes in the workspace.
11. Update `INDEX.md`.
12. Update automation memory.

## Output and Archive Rules

The workspace package folder is the canonical source of truth. Always create one package folder first:

```text
C:\Users\ryusu\Documents\New project 2\infographic-packages\YYYY-MM-DD-species-slug
```

Save all final artifacts there:

- main package notes or README
- Japanese copy
- English copy
- Japanese image prompt
- English image prompt
- Japanese and English posting copy with ALT text
- Image Gen raster image assets
- text-safe SVG poster assets when generated text may be unreliable
- source and QA notes
- updated `INDEX.md` entry

Image Gen raster output is required for a completed run. Text-safe SVG poster assets are useful as backups/reference assets, but they do not replace the Image Gen requirement.

If Image Gen is unavailable or fails, create text-safe SVG poster assets, save all text deliverables, and mark the package as `incomplete` or `needs review` until Image Gen raster images are produced.

Optionally mirror final image files to:

```text
C:\Users\ryusu\.codex\generated_images\animal_img\[species-slug]
```

This mirror is optional/cache-like, not canonical. If filesystem permissions deny the mirror copy, keep the workspace package as the successful output and record the mirror failure in package notes and automation memory.

## Growing Archive Maintenance

Because this automation runs repeatedly, maintain the archive as it grows:

- Before choosing a topic, read automation memory and scan existing package folder names.
- Read `INDEX.md` before selecting a topic, if it exists.
- Avoid any completed species listed in memory or already present under `infographic-packages`.
- Prefer a different lineage, habitat, region, or ecological hook from the most recent 3-5 completed topics.
- If a previous run was incomplete, only reuse that topic when explicitly selected or when the new package clearly completes the missing deliverables.
- Keep filenames ASCII and stable, using a species slug and language marker.
- When useful, update or create an index file in the workspace that lists completed packages, species names, status, and notes.
- Always update `INDEX.md` before finishing.

## Infographic Copy Rules

Keep each infographic minimal:

- one title
- scientific name
- three observation notes
- one quiet context/status note

Avoid:

- advocacy slogans
- blame
- rescue framing
- fake maps
- unsupported urgency
- unsupported claims such as "only X remain" or "on the brink" unless directly sourced

## Caption Rules

Create social captions in the user's preferred reference structure.

Japanese caption structure:

```text
[curiosity-first poetic Japanese line]
[English common name]
[Scientific name]

[short paragraph about habitat and behavior]
[short line about visible trait or unusual ecology]
[species-specific final line using ちょっと不思議な暮らし。]

IUCN Red List [assessment year]: [category] ([abbreviation])
```

The final "ちょっと不思議な暮らし" line must be species-specific, not generic. Shape it around the living thing's distinctive trait.

Good example direction for olm:

```text
光のない水をたどる、ちょっと不思議な暮らし。
```

## Image Rules

Use Image Gen for every completed package. Generate both Japanese and English raster poster images.

Style:

- childlike crayon/oil-pastel field-notebook poster
- warm, handmade, educational
- accurate species identity and habitat cues
- no fake maps
- no unsupported visual claims

If generated text is unreliable, still keep the Image Gen raster images, but also create text-safe SVG posters with deterministic text. The SVGs are accuracy backups, not replacements for Image Gen output.

Save final visual artifacts first under the workspace package folder:

```text
C:\Users\ryusu\Documents\New project 2\infographic-packages\YYYY-MM-DD-species-slug
```

Then, if filesystem permissions allow, mirror generated image files under:

```text
C:\Users\ryusu\.codex\generated_images\animal_img
```

Use a species-named folder and English ASCII filenames that include species, language, and date.

Example:

```text
animal_img/
  olm/
    olm_japanese_2026-04-30.png
    olm_english_2026-04-30.png
```

Also save final artifacts and notes in the workspace package folder.

## X Posting Support

When providing posting copy for X:

- Use a strong curiosity-first opening line.
- Use 0 to 2 relevant hashtags only.
- Provide ALT text for each image.
- Keep the main post readable; put sources or extra context in a reply when useful.
- Prefer separate Japanese and English posts.
- Keep a repeatable series identity, such as "世界の知らない生きもの" or "ちょっと不思議な暮らし図鑑".

## Memory Update

Before finishing, update:

```text
C:\Users\ryusu\Documents\New project 2\infographic-packages\INDEX.md
```

Record:

- date
- topic
- Japanese name
- scientific name
- package folder
- status: completed / incomplete / needs review
- short operational note
- whether Image Gen raster images exist
- whether the topic should be avoided next time

Before finishing, update:

```text
$CODEX_HOME/automations/automation-2/memory.md
```

Record:

- selected species/topic
- scientific name
- workspace package path
- generated artifacts
- whether Image Gen raster images exist for both Japanese and English versions
- key sources and assessment years
- any image QA notes
- whether the topic should be avoided next time
- any user preference discovered during the run

## Completion Criteria

The run is complete when:

- the workspace package folder exists
- all required text deliverables are saved
- final Image Gen raster images exist for both Japanese and English versions
- text-safe SVG backups exist when generated text may be unreliable
- fact-check sources are listed
- X posting copy and ALT text are included
- INDEX.md is updated
- automation memory is updated

The run is still complete if generated_images mirroring fails due to permissions, as long as the workspace package folder contains the final Image Gen raster images and the failure is recorded.

The run is not complete if only SVG/HTML-derived images exist and Image Gen raster images were not produced.
