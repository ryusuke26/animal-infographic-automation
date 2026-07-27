# Automation: 世界の知らない生きものインフォグラフィック日次制作

Create one complete curiosity-first bilingual infographic package. Use
`$bio-discovery-infographic` and `$endangered-species-factcheck` when
available.

Default to Quality Run. Poster coherence, species identity, readable integrated
typography, rich observation cards, and non-formulaic X writing are completion
requirements. Do not accept a mechanically valid but visibly generic package.

Read and follow:

```text
automation-2-current-state.md
automation-2-production-policy.md
daily-quality-loop.md
templates/x-post-copy-template.md
scripts/normalize_poster.py
scripts/validate_package.py
```

`scripts/compose_poster.py` is retained only for old Fast Run packages,
diagnostic mockups, or preserved rescue artifacts. A deterministic bilingual
layout alone does not complete a new Quality Run.

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

## Phase 2 - Evidence Lock and Copy Lock

Use two or three strong sources unless a concrete conflict requires more.
Settle and record:

- accepted name and naming caveats;
- native range and habitat;
- exact global IUCN category and assessment year/check year;
- exactly three public claims: habitat, visible identity, and behavior or life
  history;
- visual identity guidance and negative constraints;
- one source-supported discovery doorway for the poster and X post.

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
image-prompt-ja.md
image-prompt-en.md
x-post-ja.md
x-post-en.md
```

README must contain:

```text
Workflow mode: Quality Run
```

Each copy file contains the exact title, scientific name, exactly three
observation labels, and short status footer.

Each language image prompt requests a complete vertical 2:3 poster and contains
a `Text, verbatim:` block that matches the corresponding Copy Lock exactly.
Require:

- one identifiable hero organism in an accurate habitat and natural posture;
- a handmade, editorial field-notebook composition designed for this species;
- title and scientific name integrated at the top;
- exactly three numbered observation cards arranged around the silhouette;
- one species-specific spot illustration or icon and explanatory copy in every
  card;
- a quiet integrated status footer;
- no extra text, logos, watermarks, fake maps, generic lookalikes, duplicated
  hero organisms, or invented anatomy.

Do not default to three equal software-style panels. Compose the cards, border,
palette, and negative space around the organism's body plan. The title, habitat,
hero, cards, and footer must feel like one authored poster.

Build X files from `templates/x-post-copy-template.md`. Keep main post, ALT
text, and labeled source/context reply in three separate fenced `text` blocks.

The main post is a complete, separate reading experience, not a recap of card
1, card 2, and card 3. ALT text and the source/context reply are separate posts,
so do not compress the story merely to make room for them. Open with a
species-specific scene, question, image, or action; place the public common and
scientific names on adjacent standalone lines after the hook; then let the
reader follow a connected discovery progression. Use concrete habitat,
appearance, movement, and consequence details in the order that best fits the
species. Connect at least two locked facts in natural prose and vary sentence
rhythm. When the evidence supports it, aim for roughly 220-275 Unicode
characters including line breaks; never pad weak copy and never exceed 275
characters in a new main-post block. Draft naturally first, then trim repeated
modifiers, duplicated facts, or an expendable transition before cutting the
sensory hook, the action-to-meaning payoff, or the Japanese series ending. Avoid
unsupported absolutes, exclusivity, purpose-driven evolution wording,
yesterday's opening, and numbered/bulleted fact patterns. Keep the status quiet
at the end.

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

## Phase 3 - Complete bilingual Image Gen posters

Generate the Japanese poster itself with Image Gen:

```text
images/species_slug_japanese_imagegen_YYYY-MM-DD.png
```

Inspect it before making the companion. Accept it only if:

- the species silhouette, diagnostic structures, posture, and habitat are
  correct;
- one hero organism remains dominant and unobstructed;
- title, scientific name, three cards, and footer form one coherent design;
- every card has a visible number, species-specific spot art, and useful copy;
- all locked text is accurate and readable on a phone;
- the result looks authored for this organism rather than filled into a generic
  template.

If a material problem exists, make at most one targeted Japanese regeneration.
Name the concrete failure and preserve accepted elements.

Then generate the English companion:

```text
images/species_slug_english_imagegen_YYYY-MM-DD.png
```

Use the accepted Japanese poster as a visual reference when supported, or carry
forward its art direction explicitly. Preserve the species, habitat, palette,
handmade medium, hierarchy, and card concept without requiring pixel-identical
placement. Apply the same acceptance criteria and allow at most one targeted
English regeneration.

Both direct posters must themselves be true vertical 2:3. Reject a wrong-ratio
source; do not crop, stretch, or pad it into compliance.

Normalize accepted direct posters to exact posting size:

```text
<bundled-python> scripts/normalize_poster.py \
  --input <direct-imagegen.png> \
  --output <posting.png>
```

The Japanese and English posting PNGs must each be exactly `1024x1536`.

A local text-safe repair is allowed only for a localized generated-text defect
when it preserves the integrated artwork. It must not replace the poster with
the deterministic Fast Run card layout. If a material visual or text blocker
remains after the allowed targeted retry, preserve the artifacts and mark the
package `needs review` or `incomplete`.

## Phase 4 - Editorial, visual, and mechanical QA

Create six posting sidecars from the three fenced blocks in each X-post file.
README links prominently to `x-post-ja.md`, `x-post-en.md`, both direct Image
Gen posters, both posting PNGs, and sidecars.

Check:

- correct species silhouette, diagnostic structures, posture, and habitat;
- no invented, missing, detached, duplicated, or hidden structures;
- one hero organism and exactly three numbered illustrated cards;
- Copy Lock text is exact and legible;
- the whole composition remains coherent at full size and phone size;
- no generic dashboard/card treatment or card placement that buries the hero;
- each X main post works as a small natural-history story rather than a poster
  transcription;
- its opening and sentence pattern do not repeat either of the latest two
  completed posts;
- ALT text describes the accepted poster;
- both posting PNGs are exactly `1024x1536`;
- sidecars match X blocks.

Run:

```text
<bundled-python> scripts/validate_x_post_format.py \
  --ja <package>/x-post-ja.md \
  --en <package>/x-post-en.md

<bundled-python> scripts/validate_package.py <package>
```

Apply deterministic fixes and rerun only the failed check. Validator success is
not a completion signal when the image or writing is visibly weak. Ask the user
only if the unresolved issue requires factual interpretation or subjective
visual choice.

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

Default: Quality Run.

Use Caution Run only for a concrete official-source conflict/unavailability,
taxonomy or naming ambiguity that affects public copy, a prominent
population/legal/threat claim, high lookalike/body-plan risk, or a user factual
correction. Add only the check needed for that trigger.

Use Rescue Run only when the locked status cannot be supported or a required
direct poster remains materially wrong after its one targeted retry. Preserve
work and stop; do not enter an open-ended review or regeneration loop.
