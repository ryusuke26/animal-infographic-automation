# Automation 2 Production Policy

This is the operating policy for:

`世界の知らない生きものインフォグラフィック日次制作`

The default is a short, repeatable Fast Run. Extra gates are added only when a
specific factual or visual risk requires them.

## Operating Targets

- Normal elapsed time: 10-30 minutes after tools respond.
- User touchpoints before publishing: zero by default, one when evidence or
  visual judgment genuinely needs the user.
- Approval budget: batch safe local work; reserve separate approval for
  importing an external file when required and for GitHub publishing.
- Output: one complete bilingual package, not partial art.

These are operating targets, not reasons to skip a factual correction or accept
a misidentified organism.

## Responsibility Map

| Area | Source of truth |
|---|---|
| Execution instructions | `automation-2-updated-prompt.md` |
| Current run state | `automation-2-current-state.md` |
| Completed/incomplete topics | `infographic-packages/INDEX.md` |
| Package artifacts | `infographic-packages/YYYY-MM-DD-species-slug/` |
| X copy structure | `templates/x-post-copy-template.md` |
| Poster composer | `scripts/compose_poster.py` |
| Package validation | `scripts/validate_package.py` |
| X copy validation | `scripts/validate_x_post_format.py` |
| Run learning | `daily-quality-loop.md` and Automation memory |

## Workload Modes

### Fast Run - default

Use when an official status route is available, sources do not materially
conflict, and one text-free illustration can depict the organism safely.

- Keep all checking local.
- Use two or three strong sources, not an open-ended literature review.
- Do not request an IUCN screenshot or PDF from the user when the official page,
  official PDF, or another accepted official route is directly inspectable.
- Generate one text-free base illustration.
- Compose both language posters deterministically from locked copy.
- Run one pre-visual validator pass and one final validator pass.

### Caution Run - exception

Use only when at least one concrete trigger exists:

- the official IUCN/status route cannot be completed;
- authoritative sources materially conflict;
- taxonomy or Japanese naming is unresolved in a way that affects public copy;
- a population, legal-protection, or ranked-threat claim is central;
- the species has a high lookalike or body-plan risk;
- the user corrects a factual or visual interpretation.

Add only the check needed for the trigger. A Caution Run does not automatically
require a sub-agent, a user evidence gate, or additional files.

### Rescue Run - stop condition

Use when the base illustration is materially misidentified, the locked status
cannot be supported, or the deterministic posters still fail final QA after one
targeted repair.

Preserve the work and mark it `needs review` or `incomplete`. Do not start an
unbounded retry loop.

## Fast Workflow

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
- identify an official IUCN page, assessment PDF/DOI, or completed official
  no-assessment search route;
- identify one authoritative taxonomy/name source;
- identify one authoritative biological source for the visual hook.

Do not create a provisional package merely to ask the user for files. A
user-supplied evidence gate is used only when the official route is blocked,
ambiguous, or conflicting after the direct check.

### 2. Evidence and Copy Lock

Create the package and settle:

- English, Japanese, and scientific names;
- broad native region and habitat;
- exact status footer and assessment year/check year;
- three public claims: habitat, visible identity, and behavior/life-history;
- visual identity guidance and important negative constraints.

Use the official IUCN global category by default when one exists. Keep national
or regional legal status in source/context unless the user asks otherwise.

Do not invent IUCN `NE`. When a completed official search finds no global
assessment, use:

- `IUCN世界評価は確認できず（2026年確認）`
- `No global IUCN assessment confirmed (checked 2026)`

Write:

- `infographic-copy-ja.md`
- `infographic-copy-en.md`
- `image-prompt-base.md`
- `x-post-ja.md`
- `x-post-en.md`

The base prompt must contain the exact marker:

`Text policy: no text`

It must request one vertical 2:3, text-free illustration with clear space for
three cards and must not contain a `Text, verbatim:` block.

Build both X files from `templates/x-post-copy-template.md`. Each must contain
three fenced `text` blocks: main post, ALT text, and labeled source/context
reply. Japanese posts dated 2026-07-21 or later retain:

`それが<日本語の種名>の、ちょっと不思議な暮らし。`

Run once:

```text
<bundled-python> scripts/validate_package.py --pre-image <package>
```

Do not start visual production until it passes.

### 3. One illustration, deterministic bilingual posters

Generate one text-free base illustration with Image Gen:

```text
images/species_slug_base_imagegen_YYYY-MM-DD.png
```

Requirements:

- vertical 2:3;
- one clearly identifiable hero organism;
- accurate body plan and habitat;
- no letters, labels, numbers, logos, maps, or watermark;
- enough quiet space for three observation cards.

Make at most one targeted regeneration when the organism identity, anatomy,
pose, habitat, or 2:3 ratio is materially wrong. Do not regenerate because of
text: the base contains no text.

Compose the language posters:

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

The composer supplies exact typography, three numbered icon-bearing cards, and
the status footer at `1024x1536`. Separate Japanese and English Image Gen
posters are not required in Fast Run.

Legacy packages with separate direct Image Gen posters remain valid.

### 4. One final QA pass

Check locally:

- the base depicts the correct species and habitat;
- no invented diagnostic structure appears;
- both posting PNGs are exactly `1024x1536`;
- title, scientific name, three labels, and footer match Copy Lock;
- both X-post files have three fenced blocks;
- sidecars match those blocks;
- README links prominently to `x-post-ja.md` and `x-post-en.md`.

Run once:

```text
<bundled-python> scripts/validate_package.py <package>
```

Apply deterministic fixes directly and rerun only the failed validator. Ask the
user only when the remaining issue requires factual interpretation or visual
taste.

### 5. Finish once

After final QA, update in one batch:

- package README;
- `infographic-packages/INDEX.md`;
- `automation-2-current-state.md`;
- Automation memory and one short Daily Quality Loop entry.

Mark the package `completed, local-ready`. GitHub publishing is a separate
approval-enabled closeout.

## Required Fast Run Package

```text
README.md
sources-qa.md
infographic-copy-ja.md
infographic-copy-en.md
image-prompt-base.md
x-post-ja.md
x-post-en.md
thread-drafts.md                 # only when needed for free-tier X limits
images/
  species_slug_base_imagegen_YYYY-MM-DD.png
  species_slug_japanese_posting_YYYY-MM-DD.png
  species_slug_english_posting_YYYY-MM-DD.png
  six posting sidecars
```

README must contain:

`Workflow mode: Fast Run`

The base Image Gen PNG and both posting PNGs are canonical package assets.

## Public-Copy Rules

- Discovery and education first; no blame, rescue, or unsupported urgency.
- Exactly three observation notes.
- Each note connects a visible trait, habitat, or behavior to meaning; avoid
  bare noun labels.
- No population number unless current, scoped, and necessary.
- Keep naming caveats in `sources-qa.md`, not on the poster.
- Use a short label-free status footer.
- Keep source labels only in source/context replies.

## Approval and User-Input Rules

Do not ask the user to approve routine local reads, copy drafting, layout,
validation, or state updates when the environment permits them.

User input is appropriate only when:

- an official evidence route remains unavailable or conflicting;
- a visual choice cannot be resolved objectively;
- the user must supply a protected/local file;
- an external publish or other consequential action needs approval.

Batch related safe shell work into one preflight call and one final-validation
call whenever practical.

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
for a one-off problem. Change policy, template, composer, or validator only
when the same material cause repeats or one serious fact/publication risk
requires an immediate deterministic fix.
