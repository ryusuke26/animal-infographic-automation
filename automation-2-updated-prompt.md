# Automation: 世界の知らない生きものインフォグラフィック日次制作

Create one complete curiosity-first bilingual infographic package. Use
`$bio-discovery-infographic` and `$endangered-species-factcheck` when
available.

Default to Fast Run. Target 10-30 minutes after tools respond. Keep user
touchpoints and approvals to the minimum required by evidence, visual judgment,
or publishing.

Read and follow:

```text
automation-2-current-state.md
automation-2-production-policy.md
daily-quality-loop.md
templates/x-post-copy-template.md
scripts/compose_poster.py
scripts/validate_package.py
```

GitHub publishing is separate. This automation finishes at
`completed, local-ready` and does not mutate Git in a no-approval context.

## Phase 0 - One-batch preflight

In one batch, inspect current state, Automation memory, INDEX, recent package
folders, and `git status --short`.

Call `load_workspace_dependencies` once and use the bundled Python. If it does
not return a usable path, verify the previously recorded bundled Python once
with its version, Pillow import, and validator startup. Do not use arbitrary
PATH Python or install dependencies.

If a read-only WindowsApps PowerShell launch fails before execution, retry that
same batched read once with approved execution when approvals are available. In
a no-approval automation run, stop before topic selection.

If current state names an unfinished package, resume it. First check whether a
previously missing official source is now directly available. Do not repeat an
obsolete evidence request and do not select a second topic.

## Phase 1 - Topic and evidence viability

Reject completed topics found in memory, INDEX, or package folders.

Review the latest eight completed regions. Prefer an underrepresented region
and avoid repeating yesterday's region when a credible alternative exists, but
do not turn rotation into a hard quota.

Before locking a topic, identify:

- accepted scientific name;
- English and supported Japanese name;
- broad native region, lineage, habitat, and curiosity hook;
- official IUCN page, assessment PDF/DOI, or completed official no-assessment
  route;
- one authoritative taxonomy/name source;
- one authoritative biological source for the three claims and visual identity.

Do not stop for a user IUCN screenshot/PDF by default. Request user evidence
only if the direct official route remains unavailable, ambiguous, or
conflicting.

## Phase 2 - Evidence and Copy Lock

Use two or three strong sources unless a concrete conflict requires more.
Settle and record:

- accepted name and naming caveats;
- native range and habitat;
- exact global IUCN category and assessment year/check year;
- exactly three public claims: habitat, visible identity, and behavior or life
  history;
- visual identity guidance and negative constraints.

For an assessed species, use the confirmed global IUCN category/year in the
poster and main-post footer. Keep national or regional legal status in the
source reply unless the user asks otherwise.

If a completed official search finds no global assessment, do not invent formal
`IUCN NE`. Use:

- `IUCN世界評価は確認できず（2026年確認）`
- `No global IUCN assessment confirmed (checked 2026)`

Create:

```text
README.md
sources-qa.md
infographic-copy-ja.md
infographic-copy-en.md
image-prompt-base.md
x-post-ja.md
x-post-en.md
```

README must contain:

```text
Workflow mode: Fast Run
```

Each copy file contains the exact title, scientific name, exactly three
observation labels, and short status footer.

`image-prompt-base.md` requests one vertical 2:3, text-free illustration with
one hero organism, accurate habitat/body plan, and quiet space for three cards.
It must contain:

```text
Text policy: no text
```

It must not contain `Text, verbatim:`. Ban all letters, labels, numbers, logos,
maps, and watermarks from the base image.

Build X files from `templates/x-post-copy-template.md`. Keep main post, ALT
text, and labeled source/context reply in three separate fenced `text` blocks.
For packages dated 2026-07-21 or later, Japanese main copy includes:

```text
それが<日本語の種名>の、ちょっと不思議な暮らし。
```

Run once:

```text
<bundled-python> scripts/validate_package.py --pre-image <package>
```

Fix deterministic errors locally. Do not start visual production until it
passes.

## Phase 3 - One illustration and bilingual composition

Generate one text-free base illustration with Image Gen:

```text
images/species_slug_base_imagegen_YYYY-MM-DD.png
```

Require vertical 2:3, one identifiable hero organism, accurate body plan and
habitat, no text, and whitespace for callouts.

Make at most one targeted regeneration only when species identity, anatomy,
pose, habitat, or aspect ratio is materially wrong.

Compose Japanese and English posters from that same base:

```text
<bundled-python> scripts/compose_poster.py \
  --background <base.png> \
  --copy <infographic-copy-ja.md> \
  --language ja \
  --output <images/species_slug_japanese_posting_YYYY-MM-DD.png>

<bundled-python> scripts/compose_poster.py \
  --background <base.png> \
  --copy <infographic-copy-en.md> \
  --language en \
  --output <images/species_slug_english_posting_YYYY-MM-DD.png>
```

The deterministic posters, not generated image text, are the canonical public
assets. Separate Japanese and English Image Gen posters are not required in
Fast Run.

## Phase 4 - One final QA pass

Create six posting sidecars from the three fenced blocks in each X-post file.
README links prominently to `x-post-ja.md`, `x-post-en.md`, both posting PNGs,
the base illustration, and sidecars.

Check:

- correct species silhouette, diagnostic structures, posture, and habitat;
- no invented structures;
- one hero organism and exactly three numbered icon-bearing cards;
- Copy Lock text is exact and legible;
- both posting PNGs are exactly `1024x1536`;
- sidecars match X blocks.

Run once:

```text
<bundled-python> scripts/validate_package.py <package>
```

Apply deterministic fixes and rerun only the failed validator. Ask the user only
if the unresolved issue requires factual interpretation or subjective visual
choice. If one targeted repair cannot resolve a material blocker, mark the
package `needs review` or `incomplete`.

## Phase 5 - Finish once

After final QA, update in one batch:

- package README;
- `infographic-packages/INDEX.md`;
- `automation-2-current-state.md`;
- Automation memory with one short Daily Quality Loop entry.

State is `completed, local-ready`. Do not perform GitHub publishing here.

Final response must link:

- `x-post-ja.md` as `日本語の投稿セット`
- `x-post-en.md` as `English posting set`
- Japanese and English posting PNGs

## Escalation modes

Default: Fast Run.

Use Caution Run only for a concrete official-source conflict/unavailability,
taxonomy or naming ambiguity that affects public copy, a prominent
population/legal/threat claim, high lookalike/body-plan risk, or a user factual
correction. Add only the check needed for that trigger.

Use Rescue Run only when the locked status cannot be supported or the base
illustration remains materially wrong after one targeted retry. Preserve work
and stop; do not enter an open-ended review or regeneration loop.
