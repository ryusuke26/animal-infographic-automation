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
| Package QA validation | `scripts/validate_package.py` | Mechanical package-level checks for required files, PNG dimensions, X copy format, and Copy Lock versus prompt text. |
| Daily quality loop | `daily-quality-loop.md` | End-of-run priorities, tags, next actions, and rules for when repeated issues become skill or policy updates. |
| Optional mirror | `C:\Users\ryusu\.codex\generated_images\animal_img\species-slug` | Convenience copy only; never the source of truth. |
| Run history | `$CODEX_HOME/automations/automation-2/memory.md` | Chronological decisions, failures, fixes, and preferences. |

## GitHub Publish Handoff

The daily automation should complete the package and mark it `local-ready`.
GitHub publishing is a separate approval-enabled closeout step.

In no-approval or automation execution contexts, do not attempt `git add`,
`git commit`, `git push`, temporary-index commits, direct GitHub API publish
workarounds, or clone-based publish workarounds. If the user asks for GitHub
closeout inside a no-approval context, stop before mutating Git state and ask
the user to rerun the closeout in an approval-enabled normal conversation.

When GitHub closeout is run in an approval-enabled context, use scoped staging
only:

```text
git add -- infographic-packages/INDEX.md infographic-packages/YYYY-MM-DD-species-slug
git commit -m "Add <species> infographic package"
git push origin master
git ls-remote origin refs/heads/master
```

After the package commit is verified on `origin/master`, update package README
and `infographic-packages/INDEX.md` from `local-ready` to `published`, then make
a small metadata commit and verify the remote ref again.

## Completion Standard

A package is `completed` only when all of these are true:

- Fact-check table exists.
- Japanese and English infographic copy exist.
- Japanese and English image prompts exist.
- Japanese and English X-post files exist, with the main post, ALT text, and source/context reply each in its own copy-paste-ready fenced `text` code block.
- `scripts/validate_x_post_format.py` passes for both language files.
- `scripts/validate_package.py <package-folder>` passes, or any warning is
  recorded and intentionally accepted.
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

1. Preflight, pending-publication check, and bundled workspace Python discovery.
2. Topic and region lock.
3. Evidence Lock.
4. Run-mode classification and local independent evidence checklist; optional
   read-only verifier only for Caution Run or Rescue Run triggers.
5. Copy Lock.
6. Local two-pass copy review; use sub-agent reviewers only for risk-triggered
   caution or rescue runs.
7. Direct Japanese and English Image Gen poster production.
8. Direct-source `2:3` validation and targeted regeneration of any wrong-ratio poster.
9. Resize accepted `2:3` posters to `1024x1536`.
10. Visual and mechanical QA, with optional deterministic text-safe backups.
11. Final visual/mechanical QA with `scripts/validate_package.py` and any
    risk-triggered review.
12. INDEX, Daily Quality Loop, and automation-memory update.

Image Gen must not start before Evidence Lock and Copy Lock. The exact scientific name, status year/category, native region, three core claims, titles, labels, and footer must be settled and saved first.

Preflight must call `load_workspace_dependencies` and record the bundled Python
path before topic selection. Treat an attempt as failed when it returns no
result within 60 seconds, make at most one retry, then stop before Image Gen if
no usable path is available. Do not defer mandatory normalization and package
validation until after artwork exists.

Do not change facts or wording during image generation. If a factual correction is needed, return to Evidence Lock and Copy Lock before generating again. Use one targeted retry at a time for anatomy, posture, habitat, major composition, or generated-text failure. Deterministic text-safe assets may be repaired independently, but they do not replace either required direct Image Gen poster.

## Workload Modes

Use the lightest mode that protects the package.

### Normal Run

Use this mode when official evidence is available, sources do not materially
conflict, the organism has manageable visual identity risk, and no user
correction or image-generation failure has changed the locked package.

- Keep sub-agents off.
- Use local two-pass checks before Image Gen and before completion.
- Run `scripts/validate_package.py <package-folder>` after the final posting
  PNGs exist.
- Keep the INDEX note short: region, status/footer basis, three public claims,
  asset/QA state, publication state, and avoid-repeat cue.

### Caution Run

Use this mode when one or more risk triggers appears: IUCN or another
authoritative source is unavailable, authoritative sources conflict, a status,
population, legal-protection, or threat claim is prominent, the species has high
lookalike/anatomy risk, the same Daily Quality Loop tag appeared recently, or
the user corrects evidence, copy, layout, or visual interpretation.

- Keep Evidence Lock and Copy Lock explicit.
- Use read-only sub-agent review only when it is likely to catch a high-impact
  issue; otherwise use the local two-pass fallback.
- Record the trigger and the accepted/rejected findings in README or
  `sources-qa.md`, not in an overlong INDEX note.

### Rescue Run

Use this mode when a required poster has the wrong ratio after a retry, visible
text drifts from Copy Lock, species identity is broken, evidence cannot support
the footer, or a completed package would otherwise be misleading.

- Stop broad iteration.
- Make at most one targeted retry per concrete image or text failure.
- If the retry does not fix the blocker, preserve artifacts and mark the
  package `needs review` or `incomplete`.
- Do not silently rewrite locked facts, stretch/crop/pad images into compliance,
  or use a deterministic layout as a substitute for missing direct Image Gen
  posters.

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
species_slug_japanese_posting_YYYY-MM-DD.caption.txt
species_slug_japanese_posting_YYYY-MM-DD.alt.txt
species_slug_japanese_posting_YYYY-MM-DD.source-note.txt
species_slug_english_posting_YYYY-MM-DD.caption.txt
species_slug_english_posting_YYYY-MM-DD.alt.txt
species_slug_english_posting_YYYY-MM-DD.source-note.txt
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

The primary copy surface is the combined Markdown file for each language:
`x-post-ja.md` and `x-post-en.md`. Each must contain the final caption, ALT
text, and source/context reply as three separate fenced `text` blocks. In the
completion response, always provide prominent clickable links labeled
`日本語の投稿セット` and `English posting set`. Opening either combined
Markdown file should expose all three rendered `text` blocks so each can be
copied with its own top-right copy button. Do this by default on every run
without asking the user.

Also create the three adjacent UTF-8 plain-text sidecars for each posting PNG:
`.caption.txt`, `.alt.txt`, and `.source-note.txt`. These are secondary backup
and direct-file copy targets, not the primary user-facing route. Each sidecar
contains only the final copy-ready text for that one purpose, with no Markdown
heading, code fence, placeholder, or explanatory wrapper. Keep the sidecars
synchronized with the combined Markdown blocks. In the package README, put
the two combined Markdown links first, followed by the optional six sidecar
links under `Copy-Ready Posting Files`.

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
- The default public footer for an assessed species is the confirmed global
  IUCN category and assessment year. Do not replace an available global IUCN
  category with a newer national or regional legal category merely because the
  latter is newer. Put national or regional status in the source/context reply
  unless the user explicitly requests it as the main footer.
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
- IUCN verification order is mandatory: search by the accepted scientific
  name, open the matching official species page, and record the page URL,
  category, `Last assessed` date, `Global` scope, and citation. If normal page
  retrieval is incomplete and the in-app Browser is available, inspect the
  official page in that browser before asking for a screenshot or using older
  fallbacks. Browser-visible official fields are acceptable direct evidence.
- If the official species page is blocked by the environment's browser security
  policy after the required official route and Browser attempt, do not probe
  alternate browsers, raw URLs, APIs, or other workarounds.
- When an official IUCN PDF itself displays the accepted taxon, exact category,
  Global scope, publication year or assessment date, and citation, record
  `IUCN check: confirmed via official IUCN PDF`. Record the PDF URL or local
  evidence file, exact pages and fields, publication year, assessment date, and
  citation in `sources-qa.md`. Treat the species-page block as process history;
  it does not require an access caveat in public source replies once the
  official PDF directly supports the footer. Use Caution Run only when another
  listed trigger applies, including a user correction.
- When neither the official IUCN species page nor an official IUCN PDF can be
  inspected, but an official partner display plus the official IUCN DOI route
  independently provide the exact category, assessment year, and Global scope,
  record `IUCN check: confirmed via official partner/fallback route`, mark the
  run Caution, and disclose the direct-page access caveat in `sources-qa.md` and
  both labeled source replies. Do not convert this route into a no-assessment
  footer. If only secondary sources remain, keep the status route unresolved
  and mark the package `needs review`.
- Evidence Lock must record either `IUCN check: confirmed` with those fields or
  `IUCN check: no global assessment confirmed` with the completed official
  search trail. `IUCN could not be accessed` is never a completed check.
- If an official snapshot is used, disclose the snapshot date or access caveat in the source note. If only secondary sources are available, remove the IUCN category from public copy and treat the status route as unresolved; mark the package `needs review` unless another official status or completed evidence-availability check supports the exact footer.
- If the IUCN category is central to the story and no official basis can be confirmed, mark the package `needs review` instead of publishing a confident category.
- Evidence Lock requires the accepted name, native region, exact status footer and year/check year, source-access route, three core public claims, and visual identity guidance to be settled before image work.

## Japanese Naming Fallback

- Use an established Japanese common name when an authoritative or reliable
  Japanese naming source supports it.
- When no established Japanese name is confirmed, use a concise katakana
  rendering of the accepted English common name as the poster title.
- Record the naming caveat in `sources-qa.md`, but do not print editorial labels
  such as `英名の音写`, `仮称`, `暫定和名`, or `unofficial translation` on the
  poster or main X post unless the user explicitly asks for that disclosure.
- Never invent a Japanese taxonomic name or present a katakana rendering as an
  established standard name.

## Independent Evidence Check

Every run performs a local independent checklist after Evidence Lock and before
Copy Lock. Check the accepted name, latest formal conservation status and
assessment year/check year, native range and habitat, the three public claims,
source fit, and visual identity risks.

The old one-run sub-agent verifier trial is no longer a routine step. If the
exact marker `Independent verifier trial: completed` is already present in
automation memory, do not repeat it. If the marker is absent, still default to
local checking in Normal Run mode.

Spawn or reuse a read-only verifier only in Caution Run or Rescue Run mode when
the risk trigger is likely to benefit from a second reader. The verifier must
not edit files, choose topics, change facts, generate images, publish, or make
final decisions. The main agent reconciles all findings and remains responsible
for Evidence Lock, Copy Lock, and final package status.

After image generation, run the same identity/text-consistency checklist
locally unless a read-only verifier was already spawned for a caution/rescue
trigger and can be reused without delay. Do not spawn a second verifier just to
complete a routine final check.

## Risk-Triggered Review Gates

Every run still performs local review before Image Gen and before completion,
but sub-agents are not routine. Keep normal copy polish, visual QA, and
mechanical checks local unless a risk trigger is present.

Use sub-agents only when one or more of these triggers applies and the current
run is in Caution Run or Rescue Run mode:

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
- exactly three short observation note cards placed around the hero;
- each note card should include a visible number, a small spot illustration or
  icon cue, and explanatory copy;
- one quiet label-free conservation/status footer;
- no extra explanatory paragraphs inside the poster.

Keep exactly three observation notes. Do not add a fourth note to solve a copy
problem. Keep each note to one clear observation, normally two or three short
display lines. Avoid bare label-like fragments; each note should connect a
visible trait, habitat, or behavior to what it helps the organism do. The three
notes should cover habitat, visible identity, and one behavior or life-history
hook.

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
- Default to one hero organism and three numbered observation note cards, each
  with a small spot illustration/icon cue plus explanatory copy. Do not ask
  Image Gen to solve a detailed anatomical diagram and a finished social poster
  in the same generation.
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
- In the INDEX Notes field, keep only the searchable summary: broad region,
  status/footer basis, three public claims, direct/posting asset QA state,
  publication state, and avoid-repeat cue.
- Put detailed evidence, review findings, retries, user corrections, optional
  mirror results, and Daily Quality Loop details in README, `sources-qa.md`, or
  automation memory instead of the INDEX row.
- Record the one concrete `tomorrow_change`, if any, in automation memory.
- Leave GitHub state as `local-ready` during no-approval automation runs. Do not
  attempt GitHub publish from that context; record that publish requires an
  approval-enabled closeout conversation.
- In the final completion response, always surface clickable links to
  `x-post-ja.md` as `日本語の投稿セット` and `x-post-en.md` as
  `English posting set`; do not make users hunt through individual sidecars.
