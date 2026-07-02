# Automation: 世界の知らない生きものインフォグラフィック日次制作

Create one curiosity-first biological infographic package about a lesser-known living thing from anywhere in the world. Use `$bio-discovery-infographic` for the discovery-first workflow and `$endangered-species-factcheck` for publication-safe fact checks when available.

Reference policy:

```text
automation-2-production-policy.md
daily-quality-loop.md
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

Review the most recent 8 completed packages. Prefer regions with 0 appearances, avoid a region that already appears 2 or more times when a credible underrepresented alternative exists, and avoid using the same broad region in consecutive runs. Do not keep a permanent regional cooldown: recalculate the latest-eight distribution every run and use a temporary cooldown only when current memory or INDEX notes give a still-valid reason. User-requested species, dated awareness days, and deliberate remakes may override the rotation rule when recorded.

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

If no global IUCN assessment can be confirmed, record the assessment year as not applicable and include the check year in a conservative evidence-availability footer. Do not convert “no assessment confirmed” into the formal IUCN category `Not Evaluated (NE)` unless an authoritative source explicitly supports that category.

If the live IUCN page is unavailable, retry when cheap, then check official PDFs, official status-change tables, or saved official screenshots/snapshots. If an official snapshot is used, disclose the snapshot date or access caveat. If only secondary sources are available, remove the IUCN category from public copy and use conservative evidence-availability wording. If the IUCN category is central to the story and no official basis can be confirmed, mark the package `needs review`.

## Phase 2.5: Independent Verifier Trial

Run this trial once, after Evidence Lock and before Copy Lock.

Check `C:\Users\ryusu\.codex\automations\automation-2\memory.md` for the exact
marker `Independent verifier trial: completed`.

- If the marker is absent and sub-agent tools are available, spawn exactly one
  read-only verifier.
- Give the verifier the selected topic, draft `sources-qa.md`, locked public
  claims, proposed status footer, source list, and visual identity guidance.
- Ask it to independently check the accepted name, latest formal conservation
  status and assessment year, native range and habitat, the three public
  claims, source fit, and lookalike or anatomy risks.
- Do not delegate topic selection, final copy decisions, image generation,
  file editing, INDEX updates, memory updates, or publication.
- Reconcile every verifier finding against authoritative sources. The main
  agent owns the final decision and must record accepted corrections, rejected
  suggestions, and unresolved uncertainty in `sources-qa.md`.
- If a material conflict remains unresolved, do not start Copy Lock or Image
  Gen. Mark the package `needs review`.
- If sub-agent tools are unavailable, the verifier errors, or it times out,
  perform the same independent checklist locally and continue. Record the
  fallback instead of failing the run.
- Do not spawn replacement or additional verifiers during this trial.
- If the verifier ran successfully and the tooling supports reuse, keep that
  same verifier available for one post-Image Gen identity check in Phase 5.

At Phase 6, record the trial result in the package `README.md` and automation
memory, including whether a verifier ran, pre-copy and post-image findings,
corrections, and fallbacks. Add the exact marker
`Independent verifier trial: completed` to automation memory so later runs do
not repeat the trial automatically.

## Phase 3: Copy Lock

Do not call Image Gen until this phase is complete.

Write and cross-check:

- Japanese and English infographic copy
- exact Japanese and English titles
- scientific name
- three short observation labels
- exact footer/status wording
- Japanese and English X posts with the main post, ALT text, and source/context reply each in its own copy-paste-ready fenced `text` code block
- Japanese and English thread drafts when needed
- image prompts based only on Evidence Lock claims

Build both X-post files from `templates/x-post-copy-template.md`; do not invent a package-specific caption layout. Save these files in the package folder before generating images. Recheck every image-facing fact against `sources-qa.md`.

Japanese X main-post copy must include one species-specific body line before the footer/hashtags that ends exactly with `ちょっと不思議な暮らし。`. Do not use `ちょっと不思議な暮らしがあります。` or `ちょっと不思議な暮らしをしています。`.

Copy Lock is complete only when no unresolved placeholder, year, category, name, label, or footer remains.

## Phase 3.5: Risk-Triggered Copy Review

Before Image Gen, run a lightweight local copy review: first an affirmative
repair pass for small deterministic fixes, then a critical stop-ship pass for
contradictions, missing copy, validator gaps, status mismatches, and prose
rules not enforced by scripts.

Use sub-agent reviewers only when a risk trigger is present: IUCN or another
authoritative source is unavailable, authoritative sources conflict, a status,
population, legal-protection, or threat claim is prominent, the species has
high lookalike/anatomy risk, the same Daily Quality Loop tag appeared in a
recent run, or the package is close to `needs review`.

If sub-agents are used, spawn or reuse read-only reviewers only. Give them
`sources-qa.md`, locked infographic copy, Japanese and English X-post files,
image prompts, proposed README status, and the current
`scripts/validate_x_post_format.py` output. Do not delegate topic choice,
factual final decisions, file editing, image generation, INDEX updates, memory
updates, publication, or user taste calls.

Apply deterministic, low-risk copy fixes automatically when they do not change
facts or visual claims, then rerun validators. Examples: X-format mistakes,
Japanese series-ending copy rule violations, source-note prefix errors,
prompt/copy string mismatches, and missing completion notes.

If a finding requires factual judgment, new source interpretation, new image
generation, or subjective style choice, return to Evidence Lock/Copy Lock or
mark the package `needs review`; do not silently change the claim. Record
sub-agent use or local fallback only when it matters to a logged issue or
completion blocker.

## Phase 4: Visual Production

Create:

```text
infographic-packages/YYYY-MM-DD-species-slug/
infographic-packages/YYYY-MM-DD-species-slug/images/
```

Use Image Gen only after Evidence Lock and Copy Lock.

Default poster density and composition:

- Use the 2026-06-12 Puya raimondii poster as the reference level.
- Show one large hero organism in its habitat.
- Put the title and scientific name at the top.
- Add exactly three short observation callouts around the hero.
- Put one quiet conservation/status footer at the bottom.
- Keep each callout to one short idea, normally one or two display lines.
- Do not add anatomical close-ups, duplicate specimens, lifecycle panels,
  cutaways, maps, timelines, comparison species, or behavior insets when a
  callout can explain the fact.
- Add a secondary visual only when essential, simple, and identity-safe.
  Difficult anatomical detail belongs in the caption or ALT text.

Required visual workflow:

1. Generate a complete Japanese poster with Image Gen using only the locked Japanese copy.
2. Generate a complete English poster with Image Gen using only the locked English copy.
3. Require each direct Image Gen source to be vertical `2:3`. Pixel dimensions may vary, but the aspect ratio must be within normal pixel-rounding tolerance of `2:3`.
4. If either source is not `2:3`, reject that language version and regenerate it with a targeted instruction to use a vertical `2:3` canvas. Do not add borders or padding, crop the poster, stretch it, or accept a different ratio.
5. After a ratio failure, make a targeted regeneration attempt for that language. If the regenerated poster still fails the ratio or other QA, keep the artifacts but mark the package `needs review`; do not fabricate a compliant posting file.
6. Keep accepted direct Image Gen source PNGs in `images/`.
7. Resize each accepted `2:3` source to an exact `1024x1536` posting PNG with `scripts/normalize_poster.py`. Use the Python executable returned by `load_workspace_dependencies`; do not assume `python` is on `PATH`.
8. Save the final files as `species_slug_japanese_posting_YYYY-MM-DD.png` and `species_slug_english_posting_YYYY-MM-DD.png`.
9. Create deterministic text-safe SVG/PNG versions when useful for editing or backup, but do not use them as substitutes for a missing Japanese or English Image Gen poster.

Normalization command shape:

```text
<bundled-python> scripts/normalize_poster.py --input <accepted-imagegen.png> --output <language-posting.png>
```

The Japanese and English direct Image Gen source posters must themselves be `2:3`. Their exact `1024x1536` posting versions are also completion requirements. If either language is absent, has the wrong aspect ratio, is rejected by visual QA, is replaced only by a deterministic layout, or lacks an exact-size posting PNG, mark the package `incomplete` or `needs review`.

Do not change facts or wording during image generation. If a factual correction is required, return to Evidence Lock and Copy Lock before generating again. Use at most one targeted visual retry at a time for anatomy, posture, habitat, major composition, or generated-text failure, then re-run QA instead of repeatedly changing the whole workflow.

Style: childlike crayon/oil-pastel field-notebook poster, warm handmade educational tone, accurate identity and habitat cues, no fake maps, no unsupported visual claims.

Image QA must check body plan, distinctive structures, limb/appendage count, posture, habitat, and absence of confusing lookalikes. Use a safer natural posture for difficult anatomy and do not require a generated anatomical inset. If the generated organism remains incorrect, mark the package `needs review` rather than forcing repeated generations.

## Phase 5: Package And QA

Save at least:

- `README.md` with rationale and completion notes
- `sources-qa.md`
- Japanese and English infographic copy
- Japanese and English image prompts
- Japanese and English X post copy with ALT text
- short thread drafts when needed
- final direct Japanese Image Gen poster PNG
- final direct English Image Gen poster PNG
- final Japanese posting PNG at exactly `1024x1536`
- final English posting PNG at exactly `1024x1536`
- text-safe SVG/PNG assets when useful

Use stable ASCII filenames with species slug, language, asset type, and date.

Use UTF-8 for all Markdown, text, SVG, and index files. In PowerShell, explicitly use UTF-8. If Japanese text displays as mojibake or `?`, re-read the source as UTF-8 and regenerate the affected deterministic asset before making a QA decision.

Verify:

- required files exist
- both accepted direct Image Gen source posters are vertical `2:3`
- both normalized posting PNGs are exactly `1024x1536` pixels
- no padding, borders, cropping, or stretching were used to repair an incorrect source ratio
- any SVG files that exist parse as XML
- final Japanese and English Image Gen poster text matches Copy Lock
- Japanese X copy has a separate source/context reply beginning exactly with `出典メモ：`
- English X copy has a separate source/context reply beginning exactly with `Source note:`
- each Japanese and English X-post file contains three separate copy-paste-ready fenced `text` code blocks: one for the main post, one for ALT text, and one for the source/context reply
- both source notes name the strongest sources, include useful direct links, and state any source-access or status caveat
- the Japanese main post includes a species-specific body line ending exactly with `ちょっと不思議な暮らし。`
- all thread posts satisfy the intended character limit
- the bundled workspace Python successfully runs `scripts/validate_x_post_format.py --ja <japanese-x-post.md> --en <english-x-post.md>`
- `git diff --check` reports no whitespace errors

If the independent verifier trial ran and the same verifier is still
available, send it the final `sources-qa.md`, locked copy, and both direct
poster images for one read-only identity audit. Ask it to check anatomy,
diagnostic markings, posture, habitat, lookalike confusion, and whether visible
text still matches Copy Lock. Reconcile its findings locally. Do not spawn a
second verifier. If reuse is unavailable, perform this checklist locally and
record the fallback.

## Phase 5.5: Risk-Triggered Final Review

Before INDEX, Daily Quality Loop, or automation-memory completion updates, run
a lightweight local final review: first an affirmative repair pass for small
deterministic fixes, then a critical stop-ship pass for completion blockers,
missing files, validator gaps, status mismatches, and prose rules not enforced
by scripts.

Use sub-agent reviewers only when a risk trigger is present: IUCN or another
authoritative source is unavailable, authoritative sources conflict, a status,
population, legal-protection, or threat claim is prominent, the species has
high lookalike/anatomy risk, the same Daily Quality Loop tag appeared in a
recent run, or the package is close to `needs review`.

If sub-agents are used, spawn or reuse read-only reviewers only. Give them the
package folder, `sources-qa.md`, locked copy, Japanese and English X-post
files, README status, INDEX entry if present, direct poster paths, posting PNG
paths, and validator output. Do not delegate topic choice, factual final
decisions, file editing, image generation, INDEX updates, memory updates,
publication, or user taste calls.

Apply deterministic, low-risk fixes automatically when they do not change
facts or visual claims, then rerun validators. Examples: X-format mistakes,
Japanese series-ending copy rule violations, source-note prefix errors,
README/INDEX status mismatches, and missing completion notes.

If a finding requires factual judgment, new source interpretation, new image
generation, or subjective style choice, mark the package `needs review`
instead of silently changing the claim. Record sub-agent use or local fallback
only when it matters to a logged issue or completion blocker.

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
[species-specific line ending exactly with ちょっと不思議な暮らし。]

[locked conservation/status footer]
```

Provide ALT text, 0-2 relevant hashtags, and a required separate source/context reply. Use `templates/x-post-copy-template.md` as the canonical layout. In each language file, put the complete main post, the ALT text, and the source/context reply in three separate fenced `text` code blocks so each item can be copied with one action. Do not leave any of those three items as ordinary Markdown paragraphs. The Japanese reply must begin exactly with `出典メモ：`; the English reply must begin exactly with `Source note:`. Name the strongest sources, include useful direct links, and state any source-access or status caveat. For Japanese posts, default to `#世界の知らない生き物`. Prefer separate Japanese and English posts.

## Phase 6: Finish

Before finishing, update:

```text
infographic-packages/INDEX.md
C:\Users\ryusu\.codex\automations\automation-2\memory.md
```

Then add the Daily Quality Loop entry to automation memory.

In the INDEX Notes field and automation memory, record:

- broad native region
- topic and scientific name
- package folder and artifacts
- source and assessment years
- Evidence Lock and Copy Lock completion
- Japanese and English direct Image Gen poster status, source dimensions, `2:3` validation, and visual QA
- Japanese and English normalized posting PNG status and exact `1024x1536` dimensions
- Japanese and English labeled source-note status
- whether deterministic text-safe backups exist
- independent verifier trial result, when the one-run trial occurs
- risk-triggered final review result or local two-pass fallback, including auto-fixes and unresolved blockers
- Daily Quality Loop entry using `issue`, `priority`, `tags`, `cause`, `next_action`, and `tomorrow_change`
- optional mirror result if attempted
- local-ready or published state
- whether the topic should be avoided next time
- the one concrete `tomorrow_change`, if any

The run is `completed` only when the evidence and copy are locked, separate direct Japanese and English Image Gen source PNGs both exist in vertical `2:3` and pass visual/text QA, exact `1024x1536` posting PNGs exist for both languages without padding/cropping/stretching, Japanese and English labeled source notes are present, text deliverables and sources are complete, and INDEX plus automation memory are updated with the Daily Quality Loop entry. A base illustration or deterministic bilingual layout alone is not completion. Optional text-safe backups, mirroring, and Git publishing may remain separate, but their state must be recorded.
