# Automation 2 Current State

Updated: 2026-08-03T23:22:09+09:00

This file is the small replace-in-place state record for Automation
`automation-2`. Run history remains in automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English
  Image Gen posters, species-specific illustrated observation cards, and an
  editorial review of X copy.
- Fast Run base/composer packages remain supported for existing artifacts, but
  deterministic composition is no longer the default or a completion
  substitute for a new package.
- New-topic behavior: verify official evidence directly and continue without a
  user evidence stop. Request a screenshot or PDF only when the official route
  remains unavailable, ambiguous, or conflicting.
- Pending evidence package: none.
- Active package: none.
- Evidence route: the official IUCN 9 April 2026 Red List update and current
  assessment record `e.T2058A293563664`, the National Museum of Nature and
  Science marine-mammal database, and the Australian Antarctic Division's
  updated Fur Seals account. The direct pre-publication PDF endpoint returned
  HTTP 403, while the official IUCN release directly states the current global
  category and the assessment author's BAS profile identifies the record.
- Confirmed: *Arctocephalus gazella*, Antarctic Fur Seal /
  ナンキョクオットセイ, Global Endangered (EN), 2026, breeding mainly on
  sub-Antarctic islands, small external ears, dense fur, and four-footed walking
  over land. No population estimate, national status, legal category, or threat
  slogan is used in poster or main-post copy.
- Phase 0 preflight: passed on 2026-08-03 in the no-approval local automation
  path.
- Duplicate screening: *Arctocephalus gazella*, Antarctic Fur Seal, and
  ナンキョクオットセイ were
  searched across memory, INDEX, package folders, and package contents before
  Evidence Lock; no completed package or held-topic collision was found.
- Live Automation prompt sync: refreshed on 2026-08-01 with the immediate
  direct-source gate, edit-target eligibility, fresh-canvas retry routing, and
  fixed QA order. `ACTIVE`, the daily 10:00 schedule, model, reasoning effort,
  execution environment, and project target remained unchanged.

## Latest Package

- Latest package: `2026-08-03-antarctic-fur-seal`.
- State: `completed, local-ready`.
- Production blocker: resolved. The user rejected the previous bilingual pair
  because the far hind flipper in both the hero and card 3 appeared to emerge
  from the middle abdomen, and narrow accidental gaps fragmented the card
  system. Both replacements were generated on fresh exact-2:3 canvases from
  text only; no rejected image was used as an edit target or reference.
- Visual QA: passed at full and phone size. The accepted posters use a stable
  rear three-quarter stance with the rump and tail base facing the viewer; both
  hind flippers begin there as a paired structure and remain continuous to
  separate endpoints. Card 3 repeats this relationship with a complete small
  seal. The English poster was explicitly accepted by the user.
- Composition QA: passed. Three unequal cards follow the long hero silhouette,
  with broad deliberate shoreline background between card borders and one
  continuous pebble ground, border vocabulary, palette, and quiet footer. No
  hairline gap or narrow wedge divides the card system.
- Posting QA: the four-block X sets and eight sidecars are synchronized; ALT
  text now describes the accepted rear three-quarter posters.
- Mechanical QA: both direct-source gates, normalization, X format validation,
  full package validation, image dimensions, and within-language pixel
  identity passed.
- GitHub publishing: not attempted. This no-approval automation stops at
  `completed, local-ready`.
- Rejected artifact cleanup: at the user's request, the Japanese extra-text
  first generation and all four previously canonical/posting PNGs were moved
  to the Windows Recycle Bin. Only the four canonical poster PNGs remain. A
  later English retry was stopped on user acceptance before completion and
  produced no retained package artifact.

## Recent-Eight Region Rotation

1. 2026-07-27 — Africa — Gerenuk
2. 2026-07-28 — Australia/Oceania — Kea
3. 2026-07-29 — Central America/Caribbean — Pygmy Three-toed Sloth
4. 2026-07-30 — Africa — Red River Hog
5. 2026-07-31 — North America — Ringtail
6. 2026-08-01 — Europe — Russian Desman
7. 2026-08-02 — South America — Pacarana
8. 2026-08-03 — Antarctica / Southern Ocean — Antarctic Fur Seal

Previous completed region: Antarctica / Southern Ocean.

## Verified Workspace Runtime

- Bundled Python:
  `C:\Users\ryusu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`
- Last verification: bundled runtime loaded on 2026-08-03. Both remade
  Antarctic Fur Seal canonical direct posters passed the exact-2:3/full-canvas
  source gate; both posting PNGs are `1024x1536` and pixel-identical to their
  language source.

## Daily Quality Loop Counters

- `#image-text-error`: 2/3 after threshold improvement and counter reset. The
  first Japanese Antarctic Fur Seal poster added unrequested explanatory
  paragraphs to all three cards despite a locked six-line text set; one
  targeted text-only correction removed them without changing anatomy or
  composition.
- `#IUCN-unavailable`: historical 2/3. The Gerenuk occurrence was corrected
  with user-supplied official screenshot/PDF evidence; no access caveat remains
  in the package.
- `#IUCN-browser-policy-block`: historical 1/3. Direct IUCN and BirdLife page
  bodies were policy-blocked on 2026-07-29 and the Cuban Tody candidate was
  rejected before lock. User-supplied official IUCN evidence then corrected
  the final package; no access caveat remains.
- `#assessment-year-drift`: 1/2. The initial Pacarana footer used the 2017
  publication/release year because only the official category-change table was
  available. User-supplied field-level evidence showed an assessment date of
  1 March 2016; all public and package artifacts were corrected to assessment
  year 2016 while retaining publication year 2017 in source context.
- `#post-structure-drift`: 0/2 after a user-directed deterministic correction.
  The Gerenuk main posts omitted standalone common/scientific name lines;
  template guidance and a validator check now prevent recurrence.
- `#workflow-friction` for the WindowsApps PowerShell launch failure: 0/3 after
  the approval-aware retry path succeeded on 2026-07-25; `counter_reset: yes`.
- `#species-identity-drift`: 1/3 after threshold improvement and counter reset.
  The first Russian Desman poster hid one forelimb, reaching 3/3 for materially
  similar overlapping-limb failures. The production policy now requires every
  limb to have a visible origin, separate path, separate endpoint, and negative
  space from its near/far counterpart in the first prompt. This new occurrence
  was the Antarctic Fur Seal pair's visually disconnected far hind-flipper
  origin; the package was remade from text-only fresh canvases with the paired
  rear pelvis/tail-base relationship exposed.
- `#layout-overcrowded`: 1/2 after the first Himalayan Monal composition hid
  the crest beneath the title panel; resolved by one targeted composition edit
  plus the opt-in lower-card layout.
- `#source-canvas-drift`: 0/2 after an architecture correction and counter
  reset. Ringtail produced a wrong-ratio English companion, and Russian Desman
  later retained a 91px blank right band inside an exact-size PNG. The workflow
  now gates exact ratio and full-canvas coverage immediately after every
  generation, before any edit or companion work.
- `#generic-production-drift`: reset after one architecture-level correction on
  2026-07-26. Fast Run made the poster and X copy mechanically consistent but
  visibly generic; the default was restored to complete direct Image Gen
  posters and narrative posting copy.
- `#topic-alias-duplication`: 1/2. The initial ホライモリ lock duplicated the
  completed Olm / *Proteus anguinus* package. The user caught it; the draft was
  removed from package scope and the replacement topic was checked by exact
  scientific, English, and Japanese names before lock.

## Next Concrete Change

- Begin the next new-topic duplicate screening
  with the accepted scientific name, then search English and Japanese aliases
  across memory, INDEX, folder names, and package contents before Evidence
  Lock.
- Asia is now absent from the latest eight while Africa appears twice. Prefer a
  credible Asian or otherwise underrepresented alternative and avoid another
  consecutive Antarctica / Southern Ocean topic.
- During evidence viability, treat an explicit Browser safety-policy block as
  a hard route boundary. Reject the candidate before lock or use a directly
  available official assessment DOI/PDF; use an explicit public caveat only
  while no direct official evidence is available, and remove it if stronger
  evidence later resolves the gap. Do not retry a blocked source through an
  alternate browser surface.
- Generate the complete Japanese poster first, visually accept it, then create
  the English companion from the same art direction. Do not use the deterministic
  composer as the default public asset.
- Immediately after each Image Gen result, run
  `scripts/validate_direct_poster.py`. A wrong ratio or material blank edge is a
  rejected generation, not an edit target. Use a fresh 2:3 generation and count
  it as the language's one retry.
- When a climbing mechanism risks distorted anatomy, keep the hero in a stable
  natural pose and move the mechanism into a complete-animal observation
  drawing. Never explain the motion with isolated or floating limbs.
- For pinnipeds and other rear-limb-sensitive body plans, expose the pelvic and
  tail-base region in a stable rear three-quarter stance when both hind-limb
  origins must be compared. Judge each root-to-tip path in the hero and any
  complete-animal card before accepting the poster.
- For locked ASCII punctuation, state exact spaces around colons, parentheses,
  apostrophes, and similar marks in the first English Image Gen prompt; then
  inspect the glyphs before accepting the companion.
- Keep each X main post in the established sequence: species-specific hook,
  standalone common name, standalone scientific name, quiet status footer,
  then hashtags. Attach both accepted language posters to this short post.
- Put the connected natural-history story in the first reply. Count it
  independently from the main post, ALT, and source reply; if only a small
  overflow is highlighted, shorten only enough low-value wording to clear it
  and do not broadly compress the story.
- Include the English common-name hashtag in both language versions, removing
  spaces and punctuation: `#Kea`, `#HimalayanMonal`, and so on.
