# Automation 2 Production Policy

This is the operating policy for:

`世界の知らない生きものインフォグラフィック日次制作`

The default is Quality Run. A package is complete only when the Japanese and
English posters work as finished, integrated pieces and the posting copy is
worth reading on its own. Mechanical validation is necessary, but it is not a
substitute for visual or editorial judgment.

## Operating Targets

- Normal elapsed time: roughly 30-60 minutes after tools respond; do not trade
  away poster coherence or writing quality to meet a timer.
- User touchpoints before publishing: zero by default, one only when evidence
  or a genuinely subjective visual choice cannot be resolved locally.
- Approval budget: batch safe local work; reserve separate approval for
  importing a protected file when required and for GitHub publishing.
- Output: one complete bilingual package, not partial art.

## Responsibility Map

| Area | Source of truth |
|---|---|
| Execution instructions | `automation-2-updated-prompt.md` |
| Current run state | `automation-2-current-state.md` |
| Completed/incomplete topics | `infographic-packages/INDEX.md` |
| Package artifacts | `infographic-packages/YYYY-MM-DD-species-slug/` |
| X copy structure | `templates/x-post-copy-template.md` |
| Direct-poster normalization | `scripts/normalize_poster.py` |
| Optional deterministic fallback | `scripts/compose_poster.py` |
| Package validation | `scripts/validate_package.py` |
| X copy validation | `scripts/validate_x_post_format.py` |
| Run learning | `daily-quality-loop.md` and Automation memory |

## Workload Modes

### Quality Run - default

Use when an official status route is available, sources do not materially
conflict, and the organism has manageable visual-identity risk.

- Use two or three strong sources, not an open-ended literature review.
- Do not request an IUCN screenshot or PDF from the user when an accepted
  official route is directly inspectable.
- Lock the exact bilingual poster copy before image generation.
- Generate a complete Japanese poster and a complete English companion poster
  with Image Gen. Each is a full-canvas artwork, not text laid over a generic
  background.
- Give the three cards species-specific number treatments, spot illustrations,
  and explanatory copy.
- Judge poster coherence and X writing manually in addition to running the
  validators.

### Caution Run - exception

Use only when at least one concrete trigger exists:

- the official IUCN/status route cannot be completed;
- authoritative sources materially conflict;
- taxonomy or Japanese naming is unresolved in a way that affects public copy;
- a population, legal-protection, or ranked-threat claim is central;
- the species has a high lookalike or body-plan risk;
- the user corrects a factual or visual interpretation.

Add only the check needed for the trigger. A Caution Run does not automatically
require a user evidence gate, additional files, or a second reviewer.

### Rescue Run - stop condition

Use when the locked status cannot be supported or a required direct poster
still has materially wrong identity, anatomy, composition, text, or aspect ratio
after one targeted retry for that language.

Preserve the work and mark it `needs review` or `incomplete`. Do not enter an
unbounded generation loop. A text-free base plus deterministic bilingual layout
may be retained as a working fallback, but it does not satisfy completion.

## Quality Workflow

### 0. One-batch preflight

Read, in one batch:

- `automation-2-current-state.md`
- Automation memory
- `infographic-packages/INDEX.md`
- recent package folders
- `git status --short`

Call `load_workspace_dependencies` once. Use the returned bundled Python. If the
loader is unavailable, verify the recorded bundled Python path once by checking
its version, Pillow import, and validator startup.

Do not split ordinary read-only inspection into repeated approval prompts. If
the WindowsApps PowerShell launch fails before execution, make at most one
approved retry in an approval-enabled conversation. In a no-approval automation
context, stop without selecting a topic.

If an existing package is genuinely awaiting evidence or review, resume it
instead of selecting another topic. First check whether the missing official
evidence can now be inspected directly; do not repeat an obsolete user request.

### 1. Topic and evidence viability

Reject completed topics using memory, INDEX, and package names. Review the most
recent eight completed regions and prefer an underrepresented region without
turning rotation into a hard quota.

Before locking:

- confirm the accepted scientific name;
- identify the supported English and Japanese public names;
- identify an official IUCN page, assessment PDF/DOI, or completed official
  no-assessment search route;
- identify one authoritative taxonomy/name source;
- identify one authoritative biological source for the three public claims and
  the organism's visual identity;
- choose one curiosity doorway that can carry both poster and post.

Do not create a provisional package merely to ask the user for files. Request
user-supplied evidence only when the official route remains blocked, ambiguous,
or conflicting after the direct check.

### 2. Evidence Lock and Copy Lock

Create the package and settle:

- English, Japanese, and scientific names;
- broad native region and habitat;
- exact status footer and assessment year/check year;
- exactly three public claims: habitat, visible identity, and behavior or
  life-history;
- visual identity guidance and important negative constraints;
- one emotional doorway: unusual structure, hidden habitat, seasonal life,
  surprising behavior, or another source-supported discovery hook.

Use the official IUCN global category by default when one exists. Keep national
or regional legal status in source/context unless the user asks otherwise.

Do not invent IUCN `NE`. When a completed official search finds no global
assessment, use:

- `IUCN世界評価は確認できず（2026年確認）`
- `No global IUCN assessment confirmed (checked 2026)`

Write:

- `README.md`
- `sources-qa.md`
- `infographic-copy-ja.md`
- `infographic-copy-en.md`
- `image-prompt-ja.md`
- `image-prompt-en.md`
- `x-post-ja.md`
- `x-post-en.md`

README must contain:

`Workflow mode: Quality Run`

Each infographic-copy file contains the exact title, scientific name, exactly
three observation labels, and a short label-free status footer.

Each image prompt:

- requests a complete vertical 2:3 poster, not a mockup;
- includes a `Text, verbatim:` block matching Copy Lock exactly;
- gives one identifiable hero organism an accurate body plan, posture, and
  habitat;
- requests exactly three numbered observation cards;
- gives each card one small species-specific illustration or icon plus its
  explanatory text;
- reserves a quiet integrated footer;
- bans extra text, logos, watermarks, fake maps, invented anatomy, duplicated
  hero organisms, and generic lookalike substitutions.

The layout must be composed around the actual silhouette and habitat. Do not
default to three equal software-style rectangles. Card size, placement, border,
icon, and color may vary to support the species, while remaining a coherent
paired-language design.

Build both X files from `templates/x-post-copy-template.md`. New packages
contain four fenced `text` blocks: main post, story reply, ALT text, and labeled
source/context reply.

Attach both accepted posting PNGs to the main post. The main post must:

- open with a species-specific scene, image, question, or action;
- place the public common and scientific names on adjacent standalone lines
  after the hook;
- place the quiet conservation-status footer after the identity lines;
- include the English common-name hashtag in both language versions, with
  spaces and punctuation removed, such as `#Kea` or `#HimalayanMonal`;
- remain a short doorway into the attached bilingual posters rather than
  carrying the full natural-history explanation.

The first story reply is not a transcription of the three cards. It must:

- reveal the organism through a connected discovery progression, letting
  setting, visible identity, movement, and consequence unfold in the order
  that best fits the species;
- connect at least two locked facts in natural prose;
- vary sentence length and rhythm;
- avoid numbered lists, flat fact bullets, and the previous day's opening;
- use available space for a fuller story when evidence supports it, without
  padding weak copy;
- never exceed 275 characters in either a new main-post or story-reply block;
- trim repeated modifiers, duplicated facts, or expendable transitions before
  cutting the sensory hook, action-to-meaning payoff, or series ending;
- count the story reply independently from the main post, ALT, and
  source/context blocks; when only an overflow segment is flagged, preserve the
  structure and fuller story and trim only enough low-value wording to clear
  that overflow;
- avoid unsupported absolutes, exclusivity, and purpose-driven evolution
  wording.

Japanese story replies dated 2026-07-21 or later retain:

`それが<日本語の種名>の、ちょっと不思議な暮らし。`

Run once:

```text
<bundled-python> scripts/validate_package.py --pre-image <package>
```

Do not start visual production until it passes.

### 3. Complete bilingual poster production

Generate the Japanese poster first as a complete Image Gen artwork:

```text
images/species_slug_japanese_imagegen_YYYY-MM-DD.png
```

Inspect it before generating the companion. Accept it only when:

- the organism is immediately identifiable and no diagnostic structure is
  invented, hidden, detached, or duplicated;
- title, name, three cards, and footer form one visual system;
- all three cards contain a visible number, species-specific spot art, and
  useful explanatory copy;
- the hero remains dominant and unobstructed;
- text is legible enough for mobile viewing;
- the result feels authored for this species rather than filled into a generic
  template.

If a material issue appears, make at most one targeted regeneration for the
Japanese version. Name the concrete failure and preserve all accepted elements.

Then generate the complete English companion:

```text
images/species_slug_english_imagegen_YYYY-MM-DD.png
```

Use the accepted Japanese poster as a visual reference when the tool supports
it, or carry forward its art direction explicitly. Preserve the species,
habitat, palette, handmade medium, hierarchy, and card concept without forcing
pixel-identical placement. Inspect it against the same standard and make at most
one targeted regeneration for a material English-version issue.

When the English Copy Lock contains ASCII punctuation, state its exact spacing
in the first English Image Gen prompt, for example `no space before the colon`,
`one space after the colon`, and `one space before (EN)`. This is part of the
initial prompt, not a reason for an extra regeneration.

The direct posters must themselves be true vertical 2:3. Do not crop, stretch,
or add padding to repair a wrong source ratio.

Normalize each accepted direct source to the canonical posting size:

```text
<bundled-python> scripts/normalize_poster.py \
  --input <direct-imagegen.png> \
  --output <posting.png>
```

The result must be exactly `1024x1536`. Local text-safe repair is allowed only
for a localized generated-text defect when it preserves the integrated artwork.
It must not flatten the poster into the deterministic Fast Run layout. If text
cannot be repaired without redesigning the poster, use the targeted Image Gen
retry or mark the package `needs review`.

`scripts/compose_poster.py` remains available for old Fast Run packages,
diagnostic mockups, or preserved rescue artifacts. Its output alone cannot
complete a new Quality Run.

### 4. Editorial, visual, and mechanical QA

Create eight posting sidecars from the four fenced blocks in each X-post file.
README links prominently to `x-post-ja.md`, `x-post-en.md`, both direct Image
Gen posters, both posting PNGs, and the sidecars.

Perform one deliberate QA pass:

- compare silhouette, diagnostic structures, posture, and habitat with the
  authoritative visual reference;
- reject invented, missing, detached, duplicated, or hidden structures;
- confirm one hero organism and exactly three numbered illustrated cards;
- confirm the title, scientific name, three labels, and footer match Copy Lock;
- judge the integrated composition at full size and phone size;
- reject generic dashboard/card styling or cards that bury the hero;
- confirm the main post is the short image-attached doorway and the first reply
  carries the connected natural-history story;
- read each story reply aloud and reject flat poster-summary prose;
- compare the latest two completed X files and rewrite any repeated opening or
  sentence pattern;
- confirm ALT text describes the actual accepted poster;
- confirm sidecars match the fenced blocks;
- confirm both posting PNGs are exactly `1024x1536`.

Run:

```text
<bundled-python> scripts/validate_x_post_format.py \
  --ja <package>/x-post-ja.md \
  --en <package>/x-post-en.md

<bundled-python> scripts/validate_package.py <package>
```

Apply deterministic fixes directly and rerun only the failed check. Machine
success is not enough when the poster or prose is visibly weak. Ask the user
only when the remaining issue requires factual interpretation or subjective
visual taste.

### 5. Finish once

After final QA, update in one batch:

- package README;
- `infographic-packages/INDEX.md`;
- `automation-2-current-state.md`;
- Automation memory and one short Daily Quality Loop entry.

Mark the package `completed, local-ready`. GitHub publishing is a separate
approval-enabled closeout.

## Required Quality Run Package

```text
README.md
sources-qa.md
infographic-copy-ja.md
infographic-copy-en.md
image-prompt-ja.md
image-prompt-en.md
x-post-ja.md
x-post-en.md
thread-drafts.md                 # only when needed for free-tier X limits
images/
  species_slug_japanese_imagegen_YYYY-MM-DD.png
  species_slug_english_imagegen_YYYY-MM-DD.png
  species_slug_japanese_posting_YYYY-MM-DD.png
  species_slug_english_posting_YYYY-MM-DD.png
  eight posting sidecars
```

The two complete direct Image Gen posters and their exact-size posting versions
are canonical assets.

## Public-Copy Rules

- Discovery and education first; no blame, rescue, or unsupported urgency.
- Exactly three observation notes.
- Each note connects a visible trait, habitat, or behavior to meaning.
- Every note card has a visible number, a small species-specific illustration
  or icon, and explanatory copy rather than a bare label.
- No population number unless current, scoped, and necessary.
- Keep naming caveats in `sources-qa.md`, not on the poster.
- Use a short label-free status footer.
- Keep source labels only in source/context replies.
- Treat the main post as a short image-attached doorway: hook, identity,
  conservation footer, and hashtags.
- Treat the first story reply as a miniature natural-history story, not as
  three poster labels joined by line breaks.
- Count the four posting blocks independently and trim only the block that
  actually exceeds its limit.

## Approval and User-Input Rules

Do not ask the user to approve routine local reads, copy drafting, image
generation, validation, or state updates when the environment permits them.

User input is appropriate only when:

- an official evidence route remains unavailable or conflicting;
- a visual choice cannot be resolved objectively after the allowed targeted
  retry;
- the user must supply a protected/local file;
- an external publish or other consequential action needs approval.

Batch related safe shell work whenever practical.

## GitHub Closeout

No-approval automation runs stop at `local-ready`.

In an approval-enabled closeout:

1. stage only INDEX and the package folder;
2. commit and push to `origin/master`;
3. verify `refs/heads/master`;
4. update README/INDEX from `local-ready` to `published`;
5. make the small metadata commit, push, and verify again.

## Daily Quality Loop

Record at most one concrete issue per run. Do not add a gate or checklist item
for every one-off problem. Change policy, template, prompt, or validator only
when the same material cause repeats or one serious public-quality failure
shows that the production architecture is wrong.
