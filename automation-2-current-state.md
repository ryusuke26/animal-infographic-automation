# Automation 2 Current State

Updated: 2026-08-02T22:33:46+09:00

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
- Evidence route: user-supplied official IUCN species-page screenshot and
  matching nine-page assessment PDF for `e.T6608A22199194`, the Mammal Science
  standard-name list, and the public Pacarana account from Parque de las
  Leyendas in Lima. The official files are preserved with hashes in the package.
- Confirmed: *Dinomys branickii*, Pacarana / パカラナ, Global Least Concern
  (LC), assessed 1 March 2016 and published 2017, South American mountain
  forest, thick dark grey-brown coat with white spots, and the natural feeding
  posture of sitting on the hind legs while holding fruit or stems in the
  forepaws. The official assessment lists population trend as Unknown. No
  population estimate, trend assertion, national status, threat ranking, or
  recovery claim is used publicly.
- Phase 0 preflight: passed on 2026-08-02 in the no-approval local automation
  path.
- Duplicate screening: *Dinomys branickii*, Pacarana, and パカラナ were
  searched across memory, INDEX, package folders, and package contents before
  Evidence Lock. Earlier candidate mentions were held-topic notes, not a
  completed package.
- Live Automation prompt sync: refreshed on 2026-08-01 with the immediate
  direct-source gate, edit-target eligibility, fresh-canvas retry routing, and
  fixed QA order. `ACTIVE`, the daily 10:00 schedule, model, reasoning effort,
  execution environment, and project target remained unchanged.

## Latest Package

- Latest package: `2026-08-02-pacarana`.
- State: `completed, published`.
- Production blocker: none. Japanese and English initially passed on their
  first complete Image Gen generation. Stronger official evidence then reopened
  Copy Lock, and one targeted footer correction per language changed the public
  year from the 2017 publication year to the 2016 assessment year.
- Visual QA: passed at full and phone size. Each poster has one unobstructed
  seated Pacarana with separate readable forelimb and hindlimb paths, one
  connected furry tail, the dark white-spotted coat, and a fruit held between
  both forepaws.
- Composition QA: each poster uses exactly three unequal numbered illustrated
  cards for South American mountain forest, the white-spotted coat, and the
  seated food-holding posture. Text is accurate and readable at phone size.
- Posting QA: the four-block X sets and eight sidecars are synchronized and
  ready with both accepted language posters.
- Mechanical QA: direct-source checks, normalization, X format validation,
  full package validation, image dimensions, and within-language pixel
  identity passed.
- GitHub publishing: package commit `be7af29` was pushed to `origin/master`;
  remote `refs/heads/master` was verified at
  `be7af2949d636e2eaecb93c5dd5b06cdae889e99` before this published-state
  metadata update.
- Artifact cleanup: at the user's request, the four superseded 2017-footer PNGs
  were moved to the Windows Recycle Bin. The package now contains only the four
  corrected canonical poster PNGs; official IUCN evidence remains preserved.

## Recent-Eight Region Rotation

1. 2026-07-26 — Asia — Himalayan Monal
2. 2026-07-27 — Africa — Gerenuk
3. 2026-07-28 — Australia/Oceania — Kea
4. 2026-07-29 — Central America/Caribbean — Pygmy Three-toed Sloth
5. 2026-07-30 — Africa — Red River Hog
6. 2026-07-31 — North America — Ringtail
7. 2026-08-01 — Europe — Russian Desman
8. 2026-08-02 — South America — Pacarana

Previous completed region: South America.

## Verified Workspace Runtime

- Bundled Python:
  `C:\Users\ryusu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`
- Last verification: bundled runtime loaded on 2026-08-02. Both Pacarana
  canonical direct posters passed the exact-2:3/full-canvas source gate; both
  posting PNGs are `1024x1536` and pixel-identical to their language source.

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
- Ocean/Global is now absent from the latest eight while Africa appears twice.
  Prefer a credible Ocean/Global or otherwise underrepresented alternative and
  avoid another consecutive South American topic.
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
