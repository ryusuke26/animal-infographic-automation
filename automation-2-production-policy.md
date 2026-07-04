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
| X copy layout | `templates/x-post-copy-template.md` | Canonical section order and three copy-paste blocks for each language file. |
| X copy validation | `scripts/validate_x_post_format.py` | Mechanical check for the canonical three-block format, labeled source notes, and Japanese series-ending copy rule. |
| Daily quality loop | `daily-quality-loop.md` | End-of-run priorities, tags, next actions, and rules for when repeated issues become skill or policy updates. |
| Optional mirror | `C:\Users\ryusu\.codex\generated_images\animal_img\species-slug` | Convenience copy only; never the source of truth. |
| Run history | `$CODEX_HOME/automations/automation-2/memory.md` | Chronological decisions, failures, fixes, and preferences. |

## Completion Standard

A package is `completed` only when all of these are true:

- Fact-check table exists.
- Japanese and English infographic copy exist.
- Japanese and English image prompts exist.
- Japanese and English X-post files exist, with the main post, ALT text, and source/context reply each in its own copy-paste-ready fenced `text` code block.
- `scripts/validate_x_post_format.py` passes for both language files.
- Japanese X main post includes a species-specific body line ending exactly with `ちょっと不思議な暮らし。`.
- X free-version thread drafts exist when a 140-character standalone post would be too vague.
- Compact source list exists.
- The locked conservation/status footer has either a confirmed official status basis or a documented completed evidence-availability check; failed source access alone is not enough for `completed`.
- Separate direct Japanese and English Image Gen poster PNGs exist and use the locked copy.
- Both direct Image Gen source posters are vertical `2:3`.
- Separate Japanese and English posting PNGs exist at exactly `1024x1536` pixels.
- Both Image Gen posters pass visual identity QA: the species-specific body plan, distinctive structures, posture, habitat cues, and language-specific text are coherent enough for public posting.
- Text-safe SVG/PNG assets exist when useful for editing or backup.
- `infographic-packages/INDEX.md` is updated.
- Automation memory is updated, including the Daily Quality Loop entry.

If Image Gen fails, is unavailable, one language is missing, either direct
poster has the wrong aspect ratio after its targeted regeneration, or either
poster produces species/anatomy-breaking art, keep the package artifacts but
mark the topic as `incomplete` or `needs review`. A base illustration,
padding-based repair, or deterministic bilingual layout does not replace the
required direct Japanese and English Image Gen posters.

## Fixed Workflow

Every run follows this order:

1. Preflight and pending-publication check.
2. Topic and region lock.
3. Evidence Lock.
4. One-run independent verifier trial when its completion marker is absent.
5. Copy Lock.
6. Dual copy review with affirmative and critical reviewers when tools are available, or a local two-pass fallback.
7. Direct Japanese and English Image Gen poster production.
8. Direct-source `2:3` validation and targeted regeneration of any wrong-ratio poster.
9. Resize accepted `2:3` posters to `1024x1536`.
10. Visual and mechanical QA, with optional deterministic text-safe backups.
11. Final visual/mechanical QA and any risk-triggered review.
12. INDEX, Daily Quality Loop, and automation-memory update.

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
species_slug_japanese_posting_YYYY-MM-DD.png
species_slug_english_posting_YYYY-MM-DD.png
species_slug_japanese_textsafe_YYYY-MM-DD.svg
species_slug_english_textsafe_YYYY-MM-DD.svg
```

The `imagegen` files preserve the accepted direct service output and must
already be vertical `2:3`. The `posting` files are the canonical upload assets
and must both be exactly `1024x1536`.

Normalize with `scripts/normalize_poster.py` using the Python executable
returned by `load_workspace_dependencies`; plain `python` is not guaranteed to
be on `PATH`. The script rejects a source outside normal pixel-rounding
tolerance of `2:3`. It only resizes an already compliant source. Never add
padding or borders, crop the artwork, or stretch a wrong-ratio source to make
it appear compliant.

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
- Do not keep a permanent regional cooldown. Recalculate the latest-eight distribution every run and use a temporary cooldown only when current memory or INDEX notes give a still-valid reason.
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
- Distinguish "no global IUCN assessment found after a completed check" from "IUCN could not be accessed". The first can support a conservative evidence-availability footer; the second is unresolved.
- If no global IUCN assessment can be confirmed after a completed official-source check, record the assessment year as not applicable and include the check year in a conservative evidence-availability footer. Do not convert “no assessment confirmed” into the formal IUCN category `Not Evaluated (NE)` unless an authoritative source explicitly supports that category.
- Poster and main-post footers should be short and label-free. Use `IUCN Red List 2023: Near Threatened (NT)` for confirmed categories, `IUCN世界評価は確認できず（2026年確認）` in Japanese when no global assessment is confirmed, and `No global IUCN assessment confirmed (checked 2026)` in English. Do not prefix poster footers with `保全メモ：` or `Conservation note:`; source/context replies still use `出典メモ：` and `Source note:`.
- If the live IUCN page is unavailable, do not stop at `unconfirmed` by default. Retry when cheap, then check official PDFs, official status-change tables, official APIs/datasets, or previously saved official screenshots/snapshots.
- If an official snapshot is used, disclose the snapshot date or access caveat in the source note. If only secondary sources are available, remove the IUCN category from public copy and treat the status route as unresolved; mark the package `needs review` unless another official status or completed evidence-availability check supports the exact footer.
- If the IUCN category is central to the story and no official basis can be confirmed, mark the package `needs review` instead of publishing a confident category.
- Evidence Lock requires the accepted name, native region, exact status footer and year/check year, source-access route, three core public claims, and visual identity guidance to be settled before image work.

## Independent Verifier Trial

The next eligible run performs one controlled sub-agent trial. It spawns
exactly one read-only verifier after Evidence Lock and before Copy Lock, then
reuses that same verifier after Image Gen when the tooling supports reuse. It
must not delegate final decisions or file edits.

The verifier independently checks the accepted name, latest formal
conservation status and assessment year, native range and habitat, the three
public claims, source fit, and visual identity risks. The main agent reconciles
all findings and remains responsible for the final Evidence Lock.

After the direct Japanese and English posters exist, the same verifier performs
one final identity audit covering diagnostic anatomy and markings, posture,
habitat, lookalike confusion, and visible-text consistency. Do not spawn a
second verifier if the first verifier cannot be reused; perform the final
checklist locally instead.

The trial is non-blocking when tooling fails: if sub-agent tools are
unavailable, error, or time out, the main agent performs the same checklist
locally and records the fallback. A material unresolved factual conflict still
blocks Copy Lock and Image Gen.

After the trial, add the exact marker `Independent verifier trial: completed`
to automation memory and record both pre-copy and post-image results in the
package README. Later runs skip the verifier unless the automation policy is
deliberately changed.

## Risk-Triggered Review Gates

Every run still performs local review before Image Gen and before completion,
but sub-agents are not routine. Keep normal copy polish, visual QA, and
mechanical checks local unless a risk trigger is present.

Use sub-agents only when one or more of these triggers applies:

- IUCN or another authoritative source is unavailable.
- Authoritative sources conflict.
- A status, population, legal protection, or threat claim is prominent.
- The species has high lookalike or anatomy risk.
- The same Daily Quality Loop tag appeared in a recent run.
- The package is close to `needs review` or publication blocking.

When sub-agent tools are used, spawn or reuse read-only reviewers only. They
should provide concrete findings and must not edit files, choose topics,
change facts, generate images, publish, or make final decisions.

Use the first review after Copy Lock and before Image Gen. Review the locked
copy, X-post files, image prompts, and source QA. Apply deterministic copy
fixes automatically, then rerun copy validation before image generation. If a
finding changes facts or unresolved status wording, return to Evidence Lock or
keep the package blocked.

Use the second review after visual/mechanical QA and before INDEX,
Daily Quality Loop, or automation-memory completion updates. Review the final
package state, poster paths, posting PNG paths, README status, INDEX entry if
present, and validator output. The goal is to find remaining completion
blockers and auto-fixable inconsistencies before the run is marked completed.

The main agent owns the result. Apply deterministic, low-risk fixes without
waiting for the user, such as copy format corrections, missing status notes,
README/INDEX status mismatches, or validator failures. Re-run the relevant
validators after every fix. If a finding requires factual judgment, new image
generation, source reinterpretation, or user taste, mark the package
`needs review` instead of silently changing the claim.

If sub-agent tools are unavailable, unnecessary, error, or time out, perform
the same review locally in two passes: an affirmative pass for small
repairable gaps, then a critical pass for stop-ship issues. Record whether
sub-agents or the local fallback were used only when that detail matters to a
logged issue or completion blocker.

## Tone Rules

- Discovery and education first.
- No savior framing.
- No blame framing.
- No advocacy slogans.
- No unsupported urgency.
- Conservation/status appears quietly in a short label-free footer, not as the emotional center.

## Copy Lock

- Write final Japanese and English titles, scientific name, three observation labels, short label-free footer, infographic copy, X copy, ALT text, and image prompts before Image Gen.
- Save the locked copy to the package folder.
- Do not leave placeholders or unresolved dates/categories in image-facing text.
- Recheck image-facing claims against `sources-qa.md` before generating art.

## Default Information Density

Use the 2026-06-12 Puya raimondii poster as the default density and composition
reference:

- one large hero organism in its habitat;
- title and scientific name at the top;
- exactly three short observation callouts placed around the hero;
- one quiet label-free conservation/status footer;
- no extra explanatory paragraphs inside the poster.

Keep each observation callout to one short idea, normally one or two display
lines. The three callouts should cover habitat, visible identity, and one
behavior or life-history hook.

Do not add anatomical close-ups, duplicate specimens, lifecycle panels,
cutaways, maps, timelines, comparison species, or behavior insets when the
same fact can be stated in a callout. Add one secondary visual only when it is
essential to understand the subject, is easy to render accurately, and does
not compete with the hero organism. Difficult anatomy should remain in the
caption or ALT text rather than becoming an image-generation requirement.

## Image Rules

- Use Image Gen for every completed package, after Evidence Lock and Copy Lock.
- Generate separate complete Japanese and English posters with Image Gen after both locks.
- Keep both accepted direct Image Gen poster PNGs in the package.
- Require each direct Image Gen source poster to be vertical `2:3`.
- If a source has the wrong ratio, reject and regenerate that language version with a targeted `2:3` instruction.
- If the targeted regeneration still fails, mark the package `needs review`; do not add padding, crop, or stretch.
- Resize each accepted `2:3` source to a canonical `1024x1536` posting PNG.
- Do not mark a package completed unless both posting PNGs are exactly `1024x1536`.
- Both language versions are completion requirements, even when they share the same composition.
- Deterministic text-safe SVG/PNG files are optional editing and fallback assets, not substitutes for either direct Image Gen poster.
- Use childlike crayon/oil-pastel field-notebook poster style.
- Japanese-version posters should use the Japanese name or safe Japanese rendering as the main title.
- English-version posters should use the English common name as the main title.
- Use the exact locked text verbatim in each Image Gen prompt.
- Default to one hero organism and three simple callouts. Do not ask Image Gen
  to solve a detailed anatomical diagram and a finished social poster in the
  same generation.
- If generated text or visual structure fails, make one targeted retry and re-check it. Do not alter facts, labels, or workflow during the retry.
- Image QA must check the organism's body plan, distinctive structures, limb/appendage count, posture, and habitat. If the poster is merely cute or atmospheric but the anatomy/identity is wrong, mark it `needs review` instead of `completed`.
- For species with difficult anatomy, avoid forcing dramatic poses or close-up
  diagrams that Image Gen is likely to break. Use a safer natural posture and
  explain the behavior in the three labels, caption, or ALT text.
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

[locked short status footer]
```

The final "ちょっと不思議な暮らし" line must be species-specific, not generic.
For poster and main-post footers, avoid label prefixes such as `保全メモ：`
or `Conservation note:`. Put source labels only in the separate
source/context reply.

## X Posting Rules

`templates/x-post-copy-template.md` is the source of truth for file structure. Do not create a new caption layout per package.

- Start with a strong curiosity hook.
- Use 0 to 2 relevant hashtags only. For Japanese posts in this series, default to the fixed series tag `#世界の知らない生き物`.
- Add ALT text for each image.
- In each language file, place the complete main post, ALT text, and source/context reply in three separate fenced `text` code blocks. Do not leave any of these three copy targets as ordinary Markdown paragraphs.
- The Japanese source/context reply must begin with `出典メモ：`; the English reply must begin with `Source note:`. Name the strongest sources, include useful direct links, and state any access or status caveat. This source note is required, not optional.
- Keep the main post understandable; do not over-compress until the species/topic becomes unclear.
- Japanese main posts must contain one species-specific body line before the footer/hashtags that ends exactly with `ちょっと不思議な暮らし。`. Do not use `ちょっと不思議な暮らしがあります。` or `ちょっと不思議な暮らしをしています。`.
- If the target is X free-version posting or a 140-character limit, prefer a short thread over a vague standalone caption.
- Recommended 140-character thread structure: main post names the species/topic and hook; reply 1 says what it is and where it lives; reply 2 gives the distinctive trait or behavior; reply 3 gives quiet status and sources.
- Keep every thread post under 140 characters when the free-version constraint applies.
- Put sources or extra context in replies when useful.
- Use ALT text for image description and image-text support; do not make ALT the only place where the core explanation lives.
- Prefer separate Japanese and English posts.
- Keep a repeatable series identity, such as "世界の知らない生きもの" or "ちょっと不思議な暮らし図鑑".

Validate both files with the bundled workspace Python before completion:

```text
<bundled-python> scripts/validate_x_post_format.py --ja <japanese-x-post.md> --en <english-x-post.md>
```

If validation fails, the package is not completed even when the wording itself is accurate.

## Daily Quality Loop

Use `daily-quality-loop.md` at the end of every run. Add one to three entries
to automation memory; prefer one. If no meaningful issue occurred, add a short
`issue: none` entry so the next run knows the loop was checked.

Record each entry with:

```text
issue:
priority:
tags:
cause:
next_action:
tomorrow_change:
```

Choose the issue by priority: `fact-risk`, then `publish-blocker`, then
`quality-drift`, then `ops-friction`. Use the initial tags from
`daily-quality-loop.md` so repeats can be found with search. The next run
should carry forward at most one concrete `tomorrow_change`.

Do not update skills or policy for every issue. Single issues usually stay in
memory. Repeated tags become `skill-candidate` according to the escalation
rules in `daily-quality-loop.md`.

## End-of-Run Updates

Before finishing every run:

- Update `infographic-packages/INDEX.md`.
- Update `C:\Users\ryusu\.codex\automations\automation-2\memory.md`.
- Add the Daily Quality Loop entry from `daily-quality-loop.md`.
- Record the broad native region in the INDEX Notes field and automation memory.
- Record whether Evidence Lock and Copy Lock were completed before Image Gen.
- Record the status-source route, including whether the footer is based on a confirmed official category, a completed no-assessment check, or an unresolved access problem.
- Record whether separate direct Japanese and English Image Gen posters exist and pass QA.
- Record both direct source dimensions, confirm both sources are `2:3`, and confirm both posting PNGs are exactly `1024x1536`.
- Record whether optional deterministic text-safe backups exist.
- Record the one-run independent verifier result when the trial occurs.
- Record the risk-triggered final review result or local fallback, including any auto-fixes applied and remaining blockers.
- Record whether generated_images mirror succeeded or failed.
- Record whether the package is local-ready or published.
- Record whether the topic should be avoided next time.
- Record the one concrete `tomorrow_change`, if any.
