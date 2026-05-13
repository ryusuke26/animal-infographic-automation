# Automation: 世界の知らない生きものインフォグラフィック日次制作

Create one curiosity-first biological infographic package about a lesser-known living thing from anywhere in the world. Use `$bio-discovery-infographic` for the discovery-first package workflow and `$endangered-species-factcheck` for publication-safe fact checks when available.

Reference policy:

```text
automation-2-production-policy.md
```

## 1. Start Here

Before choosing a topic, read:

```text
$CODEX_HOME/automations/automation-2/memory.md
infographic-packages/INDEX.md
infographic-packages/
```

Avoid completed topics found in memory, `INDEX.md`, or package folders. Prefer a different lineage, habitat, region, or ecological hook from the most recent 3-5 completed packages. Incomplete topics do not count as completed unless this run deliberately finishes them.

## 2. Tone

- Natural-history discovery first.
- No moralizing, savior framing, blame, or urgency slogans.
- Keep conservation/status as a quiet footer.
- Do not use population numbers unless they are current, geographically scoped, and clearly sourced.
- Japanese posters should foreground the Japanese common name.

## 3. Fact Check

Verify before writing final copy:

- common name and scientific name
- taxonomy
- range and habitat
- behavior and distinctive traits
- conservation status
- threats, if mentioned
- image identity guidance

Use authoritative sources first: IUCN Red List when relevant, official regional lists with jurisdiction labels, CITES/legal listings when applicable, peer-reviewed papers, and official monitoring or recovery reports. If sources disagree, state the uncertainty and use conservative public wording.

## 4. Package

Create one canonical package folder:

```text
infographic-packages/YYYY-MM-DD-species-slug/
infographic-packages/YYYY-MM-DD-species-slug/images/
```

Save at least:

- package notes or `README.md` with rationale, fact-check table, source list, and QA notes
- Japanese and English infographic copy
- Japanese and English Image Gen prompts
- Japanese and English X post copy with ALT text
- short 140-character thread drafts when a standalone X free-version post would be unclear
- Japanese and English Image Gen raster poster PNGs in `images/`
- image QA notes confirming species identity, body structure, posture, and habitat cues are coherent enough for public posting
- text-safe SVG/PNG backups when generated text may be unreliable

Use stable ASCII filenames with species slug, language, asset type, and date.

Use UTF-8 for all package Markdown, text, SVG, and index files. When reading or writing Japanese text from PowerShell, explicitly use UTF-8. If Japanese common names, hashtags, or series labels display as mojibake, re-read as UTF-8 before editing or making QA decisions.

## 5. Visual Rules

Use Image Gen for every completed package. Generate both Japanese and English raster posters.

Style: childlike crayon/oil-pastel field-notebook poster, warm handmade educational tone, accurate species identity and habitat cues, no fake maps, no unsupported visual claims.

Text-safe SVG/PNG backups are accuracy backups. They do not replace the required Image Gen raster images.

Image Gen PNGs also need visual identity QA. Check body plan, distinctive structures, limb/appendage count, posture, and habitat. If the art is cute or atmospheric but species/anatomy-breaking, mark the package `needs review` instead of `completed`. For difficult anatomy, avoid repeated dramatic poses that break the organism; use a safer natural posture and explain the behavior in labels or an inset.

## 6. Caption Rules

For Japanese X copy, keep the user's compact structure:

```text
[curiosity-first poetic Japanese line]
[English common name]
[Scientific name]

[short habitat/behavior paragraph]
[short distinctive trait line]
[species-specific line using ちょっと不思議な暮らし]

IUCN Red List [assessment year]: [category] ([abbreviation])
```

Also provide ALT text, 0-2 relevant hashtags, and an optional source/context reply. For Japanese posts, default to the fixed series tag `#世界の知らない生き物`. Prefer separate Japanese and English posts.

## 7. Finish

Before finishing, update:

```text
infographic-packages/INDEX.md
$CODEX_HOME/automations/automation-2/memory.md
```

Record topic, scientific name, package folder, artifacts, source years, image QA, Image Gen status, optional mirror result if attempted, and whether the topic should be avoided next time.

The run is complete only when the package folder, text deliverables, sources, Japanese and English Image Gen PNGs, visual identity QA, needed backups, X copy/ALT text, `INDEX.md`, and automation memory are all present. Optional `generated_images` mirroring may fail without failing the run if package-local assets are complete and the failure is recorded.
