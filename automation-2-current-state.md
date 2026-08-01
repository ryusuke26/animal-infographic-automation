# Automation 2 Current State

Updated: 2026-08-01T12:17:32+09:00

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
- Evidence route: preserved official IUCN species-page capture and 13-page 2023
  assessment PDF for `e.T6506A231334630`, Mammal Diversity Database taxonomy,
  Mammal Science standard Japanese-name list, and recent peer-reviewed
  morphology and habitat literature. The prior official-record rendering
  boundary is resolved.
- Confirmed: *Desmana moschata*, Russian Desman / ロシアデスマン, Global
  Critically Endangered (CR), criterion A2ac, assessed 29 March 2023 and
  published 2023, waterways of eastern
  Europe into Kazakhstan, plant-rich slow waters, long flexible snout, large
  webbed hind feet, laterally flattened tail, and underwater bottom-probing.
  No population estimate, national status, or threat ranking is used publicly.
- Phase 0 preflight: passed on 2026-08-01 in the no-approval local automation
  path.
- Duplicate correction: the initial Pyrenean Desman candidate was rejected
  before lock when the exact scientific-name search found the completed
  `2026-06-08-pyrenean-desman` package. Russian Desman then passed exact
  scientific, English, and Japanese name searches.
- Live Automation prompt sync: refreshed on 2026-08-01 with the immediate
  direct-source gate, edit-target eligibility, fresh-canvas retry routing, and
  fixed QA order. `ACTIVE`, the daily 10:00 schedule, model, reasoning effort,
  execution environment, and project target remained unchanged.

## Latest Package

- Latest package: `2026-08-01-russian-desman`.
- State: `completed, local-ready`.
- Production blocker: none. The Japanese poster was regenerated from a fresh
  native `1024x1536` canvas without editing or image-referencing the rejected
  variants. Both language direct/posting pairs pass the exact-2:3 and
  full-canvas source gate.
- Visual QA: passed at full and phone size. The Japanese poster has one
  unobstructed horizontal swimming hero with separate readable limb paths and
  one connected flattened tail; Copy Lock text and exactly three unequal
  illustrated cards are readable and coherent with the accepted English
  companion.
- Composition QA: each poster uses exactly three unequal numbered illustrated
  cards for the bank-and-burrow habitat, webbed hind feet and flattened tail,
  and long-snout bottom-probing. Text is accurate and readable at phone size.
- Posting QA: the four-block X sets and eight sidecars are synchronized and
  ready with both accepted language posters.
- Mechanical QA: direct-source checks, normalization, X format validation,
  full package validation, image dimensions, and within-language pixel
  identity passed.
- GitHub publishing: not attempted; the package remains local-ready.
- Artifact cleanup: the two Japanese blank-right-band rejected PNGs were moved
  to the Windows Recycle Bin at the user's request; accepted assets remain.

## Recent-Eight Region Rotation

1. 2026-07-25 — Ocean/Global — Pelican Eel
2. 2026-07-26 — Asia — Himalayan Monal
3. 2026-07-27 — Africa — Gerenuk
4. 2026-07-28 — Australia/Oceania — Kea
5. 2026-07-29 — Central America/Caribbean — Pygmy Three-toed Sloth
6. 2026-07-30 — Africa — Red River Hog
7. 2026-07-31 — North America — Ringtail
8. 2026-08-01 — Europe — Russian Desman

Previous completed region: Europe.

## Verified Workspace Runtime

- Bundled Python:
  `C:\Users\ryusu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`
- Last verification: bundled runtime loaded on 2026-08-01. The new direct-source
  gate accepts recent valid exact-2:3 posters, rejects the 864x1821 ratio
  failure, rejects the 91px blank-edge Japanese artifact, and makes the current
  Russian Desman package fail full QA as intended.

## Daily Quality Loop Counters

- `#image-text-error`: 1/3 after threshold improvement and counter reset. The
  first English Red River Hog poster inserted a space before the footer colon
  despite explicit spacing invariants; one targeted correction resolved it.
- `#IUCN-unavailable`: historical 2/3. The Gerenuk occurrence was corrected
  with user-supplied official screenshot/PDF evidence; no access caveat remains
  in the package.
- `#IUCN-browser-policy-block`: historical 1/3. Direct IUCN and BirdLife page
  bodies were policy-blocked on 2026-07-29 and the Cuban Tody candidate was
  rejected before lock. User-supplied official IUCN evidence then corrected
  the final package; no access caveat remains.
- `#post-structure-drift`: 0/2 after a user-directed deterministic correction.
  The Gerenuk main posts omitted standalone common/scientific name lines;
  template guidance and a validator check now prevent recurrence.
- `#workflow-friction` for the WindowsApps PowerShell launch failure: 0/3 after
  the approval-aware retry path succeeded on 2026-07-25; `counter_reset: yes`.
- `#species-identity-drift`: 0/3 after threshold improvement and counter reset.
  The first Russian Desman poster hid one forelimb, reaching 3/3 for materially
  similar overlapping-limb failures. The production policy now requires every
  limb to have a visible origin, separate path, separate endpoint, and negative
  space from its near/far counterpart in the first prompt.
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
- When Russian Desman completes, South America will fall out of the latest-eight
  window and Africa will still appear twice. Prefer a credible South American
  or otherwise underrepresented alternative and avoid another consecutive
  European topic.
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
