# Automation: 世界の知らない生きものインフォグラフィック日次制作

Create one curiosity-first biological infographic package about a lesser-known living thing from anywhere in the world. Use `$bio-discovery-infographic` for the discovery-first workflow and `$endangered-species-factcheck` for publication-safe fact checks when available.

Reference policy:

```text
automation-2-production-policy.md
daily-quality-loop.md
scripts/validate_package.py
```

GitHub publishing policy:

- This automation should complete the package and mark it `local-ready`.
- Do not attempt `git add`, `git commit`, `git push`, temporary-index commits,
  direct GitHub API publish workarounds, or clone-based publish workarounds from
  a no-approval automation context.
- If GitHub closeout is requested but approval-enabled execution is not
  available, stop before mutating Git state and tell the user to run the
  closeout in an approval-enabled normal conversation.
- In an approval-enabled closeout conversation, publish with scoped staging for
  `infographic-packages/INDEX.md` and the package folder, push to
  `origin/master`, verify `refs/heads/master`, then update README/INDEX from
  `local-ready` to `published` in a small metadata commit.

Follow the phases below in order. Do not start image generation early.

## Phase 0: Preflight

Before choosing a topic, read:

```text
C:\Users\ryusu\.codex\automations\automation-2\memory.md
infographic-packages/INDEX.md
infographic-packages/
```

Use the absolute memory path above when `$CODEX_HOME` is empty or unavailable. Check `git status --short` and note any completed but unpublished package without modifying or mixing unrelated work.

Call `load_workspace_dependencies` during preflight and record the bundled
Python executable before topic selection. If the dependency loader does not
return a usable Python path, retry only when cheap, then stop before Image Gen
and report the tooling blocker. Do not produce a package that cannot run the
required normalization and validators.

Read `daily-quality-loop.md`. Count unresolved Daily Quality Loop tags in
automation memory from each tag's most recent `counter_reset` or
`improvement_applied` record. Carry any threshold reached, or one occurrence
below threshold, into this run. Counts apply only to the same tag and a
materially similar cause.

Classify the run mode during preflight and revise it only when evidence, copy,
image, or user-review risk changes:

- Normal Run: official evidence is available, no material source conflict, no
  prominent high-risk status/population/legal/threat claim, visual identity is
  manageable, and no user correction or image-generation failure has changed the
  locked package.
- Caution Run: IUCN or another authoritative source is unavailable, sources
  conflict, status/population/legal/threat claims are prominent, lookalike or
  anatomy risk is high, the same Daily Quality Loop tag appeared recently, or
  the user corrects evidence, copy, layout, or visual interpretation.
- Rescue Run: required poster ratio fails after retry, visible text drifts from
  Copy Lock, species identity is broken, evidence cannot support the footer, or
  completion would otherwise be misleading.

Default to Normal Run. Escalate only when a listed trigger appears.

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

For an assessed species, the default poster and main-post footer is the global
IUCN category and assessment year. Do not replace an available global IUCN
category with a newer national or regional legal category merely because it is
newer. Put national or regional status in the source/context reply unless the
user explicitly requests it as the main footer.

IUCN verification order is mandatory:

1. Search by the accepted scientific name.
2. Open the matching official IUCN species page.
3. Record the page URL, category, `Last assessed` date, `Global` scope, and
   citation in `sources-qa.md` under `IUCN check: confirmed`.
4. If ordinary page retrieval is incomplete and the in-app Browser is
   available, inspect the official page there before asking the user for a
   screenshot or moving to older official fallbacks. Browser-visible official
   fields count as direct evidence.
5. If no assessment is found, record `IUCN check: no global assessment
   confirmed` plus the completed official search trail. Failed access alone is
   not a completed check.

Resolve source disagreements before proceeding. If a claim remains uncertain, use conservative public wording and record the uncertainty. Do not use population numbers unless they are current, geographically scoped, and clearly sourced.

Evidence Lock is complete only when the exact status footer, assessment year or check year, status-source route, scientific name, native region, and three core public claims are settled.

Distinguish "no global IUCN assessment found after a completed official-source check" from "IUCN could not be accessed". The first can support a conservative evidence-availability footer; the second is unresolved.

If no global IUCN assessment can be confirmed after a completed official-source check, record the assessment year as not applicable and include the check year in a conservative evidence-availability footer. Do not convert “no assessment confirmed” into the formal IUCN category `Not Evaluated (NE)` unless an authoritative source explicitly supports that category.

Poster and main-post footers should be short and label-free. Use `IUCN Red List 2023: Near Threatened (NT)` for confirmed categories, `IUCN世界評価は確認できず（2026年確認）` in Japanese when no global assessment is confirmed, and `No global IUCN assessment confirmed (checked 2026)` in English. Do not prefix poster footers with `保全メモ：` or `Conservation note:`; source/context replies still use `出典メモ：` and `Source note:`.

If the live IUCN page is unavailable, retry when cheap, then check official PDFs, official status-change tables, official APIs/datasets, or saved official screenshots/snapshots. If an official snapshot is used, disclose the snapshot date or access caveat. If only secondary sources are available, remove the IUCN category from public copy and treat the status route as unresolved; mark the package `needs review` unless another official status or completed evidence-availability check supports the exact footer. If the IUCN category is central to the story and no official basis can be confirmed, mark the package `needs review`.

## Phase 2.5: Independent Evidence Check

Run a local independent checklist after Evidence Lock and before Copy Lock.

Check `C:\Users\ryusu\.codex\automations\automation-2\memory.md` for the exact
marker `Independent verifier trial: completed`.

- In Normal Run mode, do not spawn a verifier. Perform the checklist locally.
- If the marker is absent, do not treat that alone as a reason to spawn a
  verifier.
- In Caution Run or Rescue Run mode, spawn exactly one read-only verifier only
  when the active risk trigger is likely to benefit from a second reader.
- If a verifier is used, give it the selected topic, draft `sources-qa.md`,
  locked public claims, proposed status footer, source list, and visual
  identity guidance.
- Ask the checklist or verifier to independently check the accepted name,
  latest formal conservation status and assessment year/check year, native
  range and habitat, the three public claims, source fit, and lookalike or
  anatomy risks.
- Do not delegate topic selection, final copy decisions, image generation,
  file editing, INDEX updates, memory updates, or publication.
- Reconcile every checklist/verifier finding against authoritative sources. The main
  agent owns the final decision and must record accepted corrections, rejected
  suggestions, and unresolved uncertainty in `sources-qa.md`.
- If a material conflict remains unresolved, do not start Copy Lock or Image
  Gen. Mark the package `needs review`.
- If sub-agent tools are unavailable, the verifier errors, or it times out, use
  the local checklist and continue. Do not spawn replacement or additional
  verifiers.
- If a verifier was used and can be reused without delay, keep that same
  verifier available for one post-Image Gen identity check in Phase 5.

At Phase 6, record verifier use only when a verifier actually ran or when the
local checklist found a material issue. Keep routine Normal Run checklist notes
short.

## Phase 3: Copy Lock

Do not call Image Gen until this phase is complete.

Write and cross-check:

- Japanese and English infographic copy
- exact Japanese and English titles
- scientific name
- three short observation note cards, each with a visible number, a small spot
  illustration or icon cue, and explanatory copy
- exact short label-free footer/status wording
- Japanese and English X posts with the main post, ALT text, and source/context reply each in its own copy-paste-ready fenced `text` code block
- Japanese and English thread drafts when needed
- image prompts based only on Evidence Lock claims

Build both X-post files from `templates/x-post-copy-template.md`; do not invent a package-specific caption layout. Save these files in the package folder before generating images. Recheck every image-facing fact against `sources-qa.md`.

Japanese X main-post copy must include one species-specific body line before the footer/hashtags that ends exactly with `ちょっと不思議な暮らし。`. Do not use `ちょっと不思議な暮らしがあります。` or `ちょっと不思議な暮らしをしています。`.

Copy Lock is complete only when no unresolved placeholder, year, category, name, label, or footer remains.

For Japanese naming, use an established Japanese common name when supported.
If none is confirmed, use a concise katakana rendering of the accepted English
common name as the title and record the caveat only in `sources-qa.md`. Do not
put editorial labels such as `英名の音写`, `仮称`, or `暫定和名` on the poster or
main post unless the user explicitly requests them.

## Phase 3.5: Risk-Triggered Copy Review

Before Image Gen, run a lightweight local copy review: first an affirmative
repair pass for small deterministic fixes, then a critical stop-ship pass for
contradictions, missing copy, validator gaps, status mismatches, and prose
rules not enforced by scripts.

In Normal Run mode, keep sub-agents off and use only the local two-pass review.

Use sub-agent reviewers only in Caution Run or Rescue Run mode when a risk
trigger is present: IUCN or another authoritative source is unavailable,
authoritative sources conflict, a status, population, legal-protection, or
threat claim is prominent, the species has high lookalike/anatomy risk, the
same Daily Quality Loop tag appeared in a recent run, the user corrected
evidence/copy/layout/visual interpretation, or the package is close to
`needs review`.

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
- Add exactly three short numbered observation note cards around the hero.
- Each note card should contain a visible number, a small spot illustration or
  icon cue, and explanatory copy.
- Put one quiet label-free conservation/status footer at the bottom.
- Keep each note to one clear observation, normally two or three short display
  lines.
- Avoid bare label-like fragments; connect a visible trait, habitat, or
  behavior to what it helps the organism do.
- Do not add anatomical close-ups, duplicate specimens, lifecycle panels,
  cutaways, maps, timelines, comparison species, or behavior insets when a
  note card can explain the fact.
- Add a secondary visual only when essential, simple, and identity-safe.
  Difficult anatomical detail belongs in the caption or ALT text.

Required visual workflow:

1. Generate a complete Japanese poster with Image Gen using only the locked Japanese copy.
2. Generate a complete English poster with Image Gen using only the locked English copy.
3. Before Image Gen, ensure the `Text, verbatim:` quoted lines in each image prompt exactly match the locked title, scientific name, three observation notes, and footer in the matching infographic copy file.
4. Require each direct Image Gen source to be vertical `2:3`. Pixel dimensions may vary, but the aspect ratio must be within normal pixel-rounding tolerance of `2:3`.
5. If either source is not `2:3`, reject that language version and regenerate it with a targeted instruction to use a vertical `2:3` canvas. Do not add borders or padding, crop the poster, stretch it, or accept a different ratio.
6. After a ratio failure, make a targeted regeneration attempt for that language. If the regenerated poster still fails the ratio or other QA, keep the artifacts but mark the package `needs review`; do not fabricate a compliant posting file.
7. Keep accepted direct Image Gen source PNGs in `images/`.
8. Resize each accepted `2:3` source to an exact `1024x1536` posting PNG with `scripts/normalize_poster.py`. Use the Python executable returned by `load_workspace_dependencies`; do not assume `python` is on `PATH`.
9. Save the final files as `species_slug_japanese_posting_YYYY-MM-DD.png` and `species_slug_english_posting_YYYY-MM-DD.png`.
10. Create deterministic text-safe SVG/PNG versions when useful for editing or backup, but do not use them as substitutes for a missing Japanese or English Image Gen poster.

Normalization command shape:

```text
<bundled-python> scripts/normalize_poster.py --input <accepted-imagegen.png> --output <language-posting.png>
```

The Japanese and English direct Image Gen source posters must themselves be `2:3`. Their exact `1024x1536` posting versions are also completion requirements. If either language is absent, has the wrong aspect ratio, is rejected by visual QA, is replaced only by a deterministic layout, or lacks an exact-size posting PNG, mark the package `incomplete` or `needs review`.

Do not change facts or wording during image generation. If a factual correction is required, return to Evidence Lock and Copy Lock before generating again. Use at most one targeted visual retry at a time for anatomy, posture, habitat, major composition, or generated-text failure, then re-run QA instead of repeatedly changing the whole workflow.

Style: childlike crayon/oil-pastel field-notebook poster, warm handmade educational tone, accurate identity and habitat cues, numbered observation note cards with small spot illustrations/icons and explanatory copy, no fake maps, no unsupported visual claims.

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
- Japanese posting sidecars: `.caption.txt`, `.alt.txt`, and `.source-note.txt`
- English posting sidecars: `.caption.txt`, `.alt.txt`, and `.source-note.txt`
- text-safe SVG/PNG assets when useful

Use stable ASCII filenames with species slug, language, asset type, and date.

Whenever a posting PNG exists, create all three adjacent UTF-8 plain-text
sidecars for its language. Each file must contain only the final copy-ready
text for that single purpose, without Markdown headings, code fences,
placeholders, or explanatory text, so the entire file can be copied as-is when
opened. Keep sidecars synchronized with the corresponding three fenced blocks
in the X-post Markdown file. Treat `x-post-ja.md` and `x-post-en.md` as the
primary copy surfaces: each combines caption, ALT text, and source/context
reply as three fenced `text` blocks with individual copy buttons when rendered.
Put prominent clickable links to both combined Markdown files first in the
package README, followed by links to all six sidecars under
`Copy-Ready Posting Files`. Do this automatically on every run; do not ask the
user first.

Use UTF-8 for all Markdown, text, SVG, and index files. In PowerShell, explicitly use UTF-8. If Japanese text displays as mojibake or `?`, re-read the source as UTF-8 and regenerate the affected deterministic asset before making a QA decision.

Verify:

- required files exist
- both accepted direct Image Gen source posters are vertical `2:3`
- both normalized posting PNGs are exactly `1024x1536` pixels
- no padding, borders, cropping, or stretching were used to repair an incorrect source ratio
- any SVG files that exist parse as XML
- final Japanese and English Image Gen poster text matches Copy Lock
- `scripts/validate_package.py <package-folder>` passes after final posting PNGs exist
- both posting PNGs have adjacent `.caption.txt`, `.alt.txt`, and `.source-note.txt` files
- all six sidecars are plain UTF-8, contain only copy-ready text, and exactly match the corresponding X-post fenced block
- the package README links all six sidecars under `Copy-Ready Posting Files`
- the package README prominently links `x-post-ja.md` and `x-post-en.md` as the primary combined posting sets
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

In Normal Run mode, keep sub-agents off and use only the local two-pass review.

Use sub-agent reviewers only in Caution Run or Rescue Run mode when a risk
trigger is present: IUCN or another authoritative source is unavailable,
authoritative sources conflict, a status, population, legal-protection, or
threat claim is prominent, the species has high lookalike/anatomy risk, the
same Daily Quality Loop tag appeared in a recent run, the user corrected
evidence/copy/layout/visual interpretation, or the package is close to
`needs review`.

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
- Keep conservation/status as a quiet label-free footer.
- Japanese posters foreground an established Japanese name when authoritative
  support exists; otherwise use a concise katakana rendering and keep the naming
  caveat in `sources-qa.md`, not in public copy.

Japanese X copy should follow:

```text
[curiosity-first poetic Japanese line]
[English common name]
[Scientific name]

[short habitat/behavior paragraph]
[short distinctive trait line]
[species-specific line ending exactly with ちょっと不思議な暮らし。]

[locked short conservation/status footer]
```

Provide ALT text, 0-2 relevant hashtags, and a required separate source/context reply. Use `templates/x-post-copy-template.md` as the canonical layout. In each language file, put the complete main post, the ALT text, and the source/context reply in three separate fenced `text` code blocks so each item can be copied with one action. Do not leave any of those three items as ordinary Markdown paragraphs. The Japanese reply must begin exactly with `出典メモ：`; the English reply must begin exactly with `Source note:`. Name the strongest sources, include useful direct links, and state any source-access or status caveat. For Japanese posts, default to `#世界の知らない生き物`. Prefer separate Japanese and English posts.

## Phase 6: Finish

Before finishing, update:

```text
infographic-packages/INDEX.md
C:\Users\ryusu\.codex\automations\automation-2\memory.md
```

In the final completion response, always include prominent clickable links
labeled `日本語の投稿セット` for `x-post-ja.md` and `English posting set` for
`x-post-en.md`. These combined Markdown files are the primary user-facing copy
route because opening them exposes the caption, ALT text, and source/context
reply as separate rendered `text` blocks with individual copy buttons. The
plain-text sidecars remain secondary backups.

Then add the Daily Quality Loop entry to automation memory.

After recording the current issue, recount the affected tag from its most
recent reset. Thresholds are: fact-risk 1 when public facts, status,
jurisdiction, or evidence selection may be wrong; publish-blocker 2;
quality-drift 3; ops-friction 3 or one large time sink. When a threshold is
reached, automatically apply the smallest safe deterministic prompt, policy,
template, validator, or execution-path improvement; validate it; synchronize
the live Automation prompt when execution instructions changed; then record an
`Improvement Resolution` block with count, threshold, files, validation, and
`counter_reset: yes`. Subjective taste, new factual claims, external side
effects, or broad redesigns require `needs decision` instead of an automatic
change.

In the INDEX Notes field and automation memory, record:

- INDEX: keep the searchable summary short. Include broad region,
  status/footer basis, three public claims, direct/posting asset QA state,
  publication state, and avoid-repeat cue.
- README / `sources-qa.md` / automation memory: put detailed evidence, retries,
  user corrections, review findings, optional mirror results, and Daily Quality
  Loop details here instead of lengthening the INDEX row.
- automation memory: record the one concrete `tomorrow_change`, if any.

The run is `completed` only when the evidence and copy are locked, the status footer has a confirmed official basis or completed no-assessment check rather than failed source access alone, separate direct Japanese and English Image Gen source PNGs both exist in vertical `2:3` and pass visual/text QA, exact `1024x1536` posting PNGs exist for both languages without padding/cropping/stretching, Japanese and English labeled source notes are present, text deliverables and sources are complete, and INDEX plus automation memory are updated with the Daily Quality Loop entry. A base illustration or deterministic bilingual layout alone is not completion. Optional text-safe backups, mirroring, and Git publishing may remain separate, but their state must be recorded.

In no-approval automation contexts, Git publishing must remain separate: record
the package as `local-ready`, record that GitHub closeout needs an
approval-enabled normal conversation, and do not probe Git publishing with
workarounds.
