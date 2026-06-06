# Automation: 世界の知らない生きものインフォグラフィック日次制作

Create one curiosity-first biological infographic package about a lesser-known living thing from anywhere in the world. Use `$bio-discovery-infographic` for the discovery-first workflow and `$endangered-species-factcheck` for publication-safe fact checks when available.

Reference policy:

```text
automation-2-production-policy.md
```

Follow the phases below in order. Do not start image generation early.

## Phase 0: Preflight

Before choosing a topic, read:

```text
C:\Users\ryusu\.codex\automations\automation-2\memory.md
infographic-packages/INDEX.md
infographic-packages/
```

Use the absolute memory path above when `$CODEX_HOME` is empty or unavailable. Check `git status --short` and note any completed but unpublished package without modifying or mixing unrelated work.

## Phase 1: Topic And Region Lock

Reject completed topics found in memory, `INDEX.md`, or package folders.

For each candidate, identify:

- broad native region: Africa, Asia, Europe, North America, Central America/Caribbean, South America, Australia/Oceania, or Ocean/Global
- lineage
- habitat
- ecological or visual hook

Review the most recent 8 completed packages. Prefer regions with 0 appearances, avoid a region that already appears 2 or more times when a credible underrepresented alternative exists, and avoid using the same broad region in consecutive runs. Australia/Oceania is currently overrepresented and remains on cooldown until the rolling rule allows it again. User-requested species, dated awareness days, and deliberate remakes may override the rotation rule when recorded.

Choose a topic only after checking regional, lineage, habitat, and hook variety.

## Phase 2: Evidence Lock

Do not call Image Gen during this phase.

Verify and record in `sources-qa.md`:

- accepted common and scientific names
- taxonomy and naming caveats
- native range and broad region
- habitat
- behavior and distinctive traits
- conservation status, assessment year, and jurisdiction
- threats, only if public copy mentions them
- exact visual identity guidance

Use authoritative sources first: IUCN Red List when relevant, official regional lists with jurisdiction labels, CITES/legal listings when applicable, peer-reviewed papers, and official monitoring or recovery reports.

Resolve source disagreements before proceeding. If a claim remains uncertain, use conservative public wording and record the uncertainty. Do not use population numbers unless they are current, geographically scoped, and clearly sourced.

Evidence Lock is complete only when the exact status footer, assessment year, scientific name, native region, and three core public claims are settled.

## Phase 3: Copy Lock

Do not call Image Gen until this phase is complete.

Write and cross-check:

- Japanese and English infographic copy
- exact Japanese and English titles
- scientific name
- three short observation labels
- exact footer/status wording
- Japanese and English X posts with ALT text
- Japanese and English thread drafts when needed
- image prompts based only on Evidence Lock claims

Save these files in the package folder before generating images. Recheck every image-facing fact against `sources-qa.md`.

Copy Lock is complete only when no unresolved placeholder, year, category, name, label, or footer remains.

## Phase 4: Visual Production

Create:

```text
infographic-packages/YYYY-MM-DD-species-slug/
infographic-packages/YYYY-MM-DD-species-slug/images/
```

Use Image Gen only after Evidence Lock and Copy Lock.

Preferred visual workflow:

1. Generate one strong text-light or text-free base illustration with accurate organism identity and habitat.
2. Add the locked Japanese and English text locally with deterministic typography to create final Japanese and English poster PNGs.
3. Keep the accepted Image Gen base artwork in `images/`.
4. Create text-safe SVG files when useful for editing or backup.

Separate Japanese and English Image Gen scenes are optional, not required. Use them only when two distinct compositions add real value and generation capacity allows.

Do not regenerate artwork for spelling, footer-year, font, clipping, or translation problems. Fix those in the deterministic text layer. Regenerate Image Gen artwork only when the organism identity, anatomy, posture, habitat, or major composition is wrong.

Style: childlike crayon/oil-pastel field-notebook poster, warm handmade educational tone, accurate identity and habitat cues, no fake maps, no unsupported visual claims.

Image QA must check body plan, distinctive structures, limb/appendage count, posture, habitat, and absence of confusing lookalikes. Use a safer natural posture for difficult anatomy. If the generated organism remains incorrect, mark the package `needs review` rather than forcing repeated generations.

## Phase 5: Package And QA

Save at least:

- `README.md` with rationale and completion notes
- `sources-qa.md`
- Japanese and English infographic copy
- Japanese and English image prompts
- Japanese and English X post copy with ALT text
- short thread drafts when needed
- accepted Image Gen base artwork
- final Japanese and English poster PNGs
- text-safe SVG/PNG assets when useful

Use stable ASCII filenames with species slug, language, asset type, and date.

Use UTF-8 for all Markdown, text, SVG, and index files. In PowerShell, explicitly use UTF-8. If Japanese text displays as mojibake or `?`, re-read the source as UTF-8 and regenerate the affected deterministic asset before making a QA decision.

Verify:

- required files exist
- final PNG dimensions are suitable for posting
- SVG files parse as XML
- final Japanese and English poster text matches Copy Lock
- all thread posts satisfy the intended character limit
- `git diff --check` reports no whitespace errors

## Tone And Caption Rules

- Natural-history discovery first.
- No moralizing, savior framing, blame, or urgency slogans.
- Keep conservation/status as a quiet footer.
- Japanese posters foreground the Japanese common name or a clearly labeled safe rendering.

Japanese X copy should follow:

```text
[curiosity-first poetic Japanese line]
[English common name]
[Scientific name]

[short habitat/behavior paragraph]
[short distinctive trait line]
[species-specific line using ちょっと不思議な暮らし]

[locked conservation/status footer]
```

Provide ALT text, 0-2 relevant hashtags, and an optional source/context reply. For Japanese posts, default to `#世界の知らない生き物`. Prefer separate Japanese and English posts.

## Phase 6: Finish

Before finishing, update:

```text
infographic-packages/INDEX.md
C:\Users\ryusu\.codex\automations\automation-2\memory.md
```

In the INDEX Notes field and automation memory, record:

- broad native region
- topic and scientific name
- package folder and artifacts
- source and assessment years
- Evidence Lock and Copy Lock completion
- Image Gen base status and visual QA
- whether deterministic Japanese and English posters exist
- optional mirror result if attempted
- local-ready or published state
- whether the topic should be avoided next time

The run is `completed` when the evidence and copy are locked, the accepted Image Gen base exists, final Japanese and English poster PNGs pass QA, text deliverables and sources are present, and INDEX plus automation memory are updated. Optional mirroring and Git publishing may remain separate, but their state must be recorded.
