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
scripts/validate_direct_poster.py
scripts/validate_package.py
```

`scripts/compose_poster.py` is retained only for old Fast Run packages,
diagnostic mockups, or preserved rescue artifacts. A deterministic bilingual
layout alone does not complete a new Quality Run.

GitHub publishing is separate. This automation finishes at
`completed, local-ready` and does not mutate Git in a no-approval context.

## Phase 0 - One-batch preflight

In one batch, inspect current state, Automation memory, INDEX, recent package
folders, and `git status --short`. Build latest-eight rotation summaries for
both broad regions and editorial classification groups.

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

Review the latest eight completed broad regions and editorial classification
groups. Use these nine editorial groups: Mammals, Birds, Reptiles, Amphibians,
Fishes, Insects, Other invertebrates, Plants, and Fungi and lichens. These are
selection buckets, not formal taxonomic ranks; record the exact lineage
separately in Evidence Lock.

The editorial mission is to introduce living things that are internationally
overlooked in general-audience wildlife culture, not merely organisms with an
unusual appearance or an obscure scientific name. Apply a global-familiarity
gate before rotation:

- check both Japanese- and English-language general-audience exposure;
- reject household-name animals and recurring zoo, aquarium, wildlife-video,
  and generic weird-animals staples unless the user explicitly requests one;
- treat a familiar silhouette or widely known nickname as familiar even when
  most viewers do not know the scientific name;
- allow a species that is well known within its home region but little known
  internationally; never erase local or Indigenous knowledge by claiming that
  nobody knows it;
- record a one-sentence Global familiarity check, Discovery doorway,
  Conservation doorway, and Local-knowledge caution for every screened
  candidate. Search-result counts alone do not prove unfamiliarity.

When no package must be resumed, screen a small slate of two or three credible
candidates spanning at least two editorial groups when available. When
credible options exist, include at least two species with directly inspectable
official global IUCN assessments. Prefer CR, EN, VU, or NT over LC when
unfamiliarity, discovery strength, naming safety, sources, and visual viability
are otherwise comparable.

Among candidates that pass the hard naming, evidence, and visual-viability
gates, rank in this order: international unfamiliarity, natural-history
discovery strength, directly supportable conservation context, then region and
classification rotation. Rotation is a tie-breaker, not the editorial mission.
Avoid repeating yesterday's region or editorial group when a comparably strong
alternative exists, and prefer groups absent from the latest eight. If one
group already occupies four or more of the latest eight completed packages, do
not lock another from that group unless every credible alternative fails a
hard gate; record that reason.

An unavailable official page for one assessed candidate is not a reason to
prefer an unassessed species. Screen another unfamiliar assessed candidate
first. A no-global-assessment route is an intentional exception for an
exceptionally strong discovery topic, not an easier evidence fallback. Do not
complete two consecutive no-global-assessment packages unless every credible
unfamiliar assessed alternative fails a hard naming, evidence, or visual gate;
record the exception and reason.

Incomplete, needs-review, and retired packages do not fill a completed
rotation slot, but they remain duplicate and visual-risk exclusions unless the
user explicitly requests a revisit.

Before locking a topic, identify:

- accepted scientific name;
- English and supported Japanese name;
- the four candidate-screen records: global familiarity, discovery doorway,
  conservation doorway, and local-knowledge caution;
- one editorial classification group from the nine-group list;
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
Editorial classification group: <one allowed group>
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

Build X files from `templates/x-post-copy-template.md`. Keep main post, story
reply, ALT text, and labeled source/context reply in four separate fenced
`text` blocks.

The main post is the short image-attached doorway. Attach both accepted posting
PNGs. Open with a species-specific scene, question, image, or action; place the
public common and scientific names on adjacent standalone lines; follow with
the quiet status footer and 1-2 hashtags. Both language versions include the
English common-name hashtag with spaces and punctuation removed, for example
`#Kea` or `#HimalayanMonal`.

Put the complete natural-history story in the first reply, not in the main
post. It is not a recap of card 1, card 2, and card 3. Let the reader follow a
connected discovery progression using concrete habitat, appearance, movement,
and consequence details in the order that best fits the species. Connect at
least two locked facts in natural prose and vary sentence rhythm. Count the
story reply independently from the main post, ALT text, and source reply.
Neither main post nor story reply may exceed 275 Unicode characters. If only an
overflow segment is flagged, preserve the established structure and fuller
story and trim only enough low-value wording to clear it. Avoid unsupported
absolutes, exclusivity, purpose-driven evolution wording, yesterday's opening,
and numbered/bulleted fact patterns.

For packages dated 2026-07-21 or later, the Japanese story reply ends with:

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

Immediately after every initial generation or retry, and before visual review,
editing, companion generation, or normalization, run:

```text
<bundled-python> scripts/validate_direct_poster.py \
  --input <direct-imagegen.png>
```

The source must be exact vertical 2:3 and must not contain a material
near-white or transparent edge band. A failure is a rejected generation even
when the outer PNG is `1024x1536`. Do not crop, stretch, pad, locally extend,
or reflow it. Do not use failed pixels as an edit target or image reference;
carry accepted art direction forward in words and generate a fresh poster on a
new 2:3 canvas. This consumes the language's one allowed retry.

After the source gate passes, inspect it before making the companion. Accept it
only if:

- the species silhouette, diagnostic structures, posture, and habitat are
  correct;
- when limb anatomy is material, the first prompt assigns every limb a visible
  shoulder or hip origin, separate path, separate endpoint, and negative space
  from its near/far counterpart;
- one hero organism remains dominant and unobstructed;
- title, scientific name, three cards, and footer form one coherent design;
- every card has a visible number, species-specific spot art, and useful copy;
- all locked text is accurate and readable on a phone;
- the result looks authored for this organism rather than filled into a generic
  template.

Before the one allowed Japanese retry, classify the failure. Use a targeted edit
only when the source gate passes and the defect is localized while hero
topology, full canvas, and overall composition are already acceptable. Use a
fresh generation for wrong ratio, blank bands, global reflow, pose-induced
anatomy, or silhouette reconstruction. Label every supplied image as `edit
target` or `reference image`; never let a rejected source become the base
canvas.

For difficult motion or climbing mechanics, keep the hero in a stable natural
pose and show the mechanism with one complete small animal in a card, never an
isolated or floating body part. If the same anatomy defect remains after the
retry, preserve the artifacts and enter Rescue Run.

Then generate the English companion:

```text
images/species_slug_english_imagegen_YYYY-MM-DD.png
```

Use the accepted Japanese poster as a visual reference when supported, or carry
forward its art direction explicitly. Preserve the species, habitat, palette,
handmade medium, hierarchy, and card concept without requiring pixel-identical
placement. Apply the same acceptance criteria and allow at most one English
retry. Run the direct-source gate immediately after both the
initial English generation and its retry; the same edit-target eligibility
rules apply.

When the English Copy Lock contains ASCII punctuation, state its exact spacing
in the first English Image Gen prompt, for example `no space before the colon`,
`one space after the colon`, and `one space before (EN)`. This is part of the
initial prompt, not a reason for an extra regeneration.

Only direct posters that passed both the source gate and visual acceptance may
be normalized.

Normalize accepted direct posters to exact posting size:

```text
<bundled-python> scripts/normalize_poster.py \
  --input <direct-imagegen.png> \
  --output <posting.png>
```

The Japanese and English posting PNGs must each be exactly `1024x1536`.

A local text-safe repair is allowed only for a localized generated-text defect
on a source-gate-passing poster when it preserves the integrated artwork. It
must not repair dimensions, blank canvas, anatomy, pose, or global layout, and
must not replace the poster with the deterministic Fast Run card layout. If a
material visual or text blocker remains after the allowed retry, preserve the
artifacts and mark the package `needs review` or `incomplete`.

## Phase 4 - Editorial, visual, and mechanical QA

Create eight posting sidecars from the four fenced blocks in each X-post file.
README links prominently to `x-post-ja.md`, `x-post-en.md`, both direct Image
Gen posters, both posting PNGs, and sidecars.

Check:

- both canonical direct posters still pass
  `scripts/validate_direct_poster.py`, before subjective QA;
- both posting PNGs are exactly `1024x1536`;
- correct species silhouette, diagnostic structures, posture, and habitat;
- no invented, missing, detached, duplicated, or hidden structures;
- one hero organism and exactly three numbered illustrated cards;
- Copy Lock text is exact and legible;
- the whole composition remains coherent at full size and phone size;
- no generic dashboard/card treatment or card placement that buries the hero;
- each main post is a short doorway for the two attached language posters;
- each story reply works as a small natural-history story rather than a poster
  transcription;
- its opening and sentence pattern do not repeat either of the latest two
  completed posts;
- both language main posts include the English common-name hashtag;
- ALT text describes the accepted poster;
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

Record the package's broad region and editorial classification group in README
and INDEX, and refresh both latest-eight rotation summaries in current state.

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
