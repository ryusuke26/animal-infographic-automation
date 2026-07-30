# Automation 2 Current State

Updated: 2026-07-30T23:14:51+09:00

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
- Evidence route: formal IUCN 2016 assessment DOI
  `e.T41771A100469961`, Mammal Diversity Database taxonomy, Yokohama
  Zoological Gardens, Tobe Zoo, and the IUCN SSC February 2026 African
  wild-pig reassessment meeting note.
- Confirmed: *Potamochoerus porcus*, Red River Hog / アカカワイノシシ,
  Global Least Concern (LC) in the current formal 2016 assessment, West and
  Central African forest and thicket habitat, red-brown coat with white face
  and dorsal markings, long pale ear tassels, and mainly after-dusk group
  foraging for roots and fallen fruit.
- Caution: the 2026 IUCN SSC meeting suggested retaining LC with a decreasing
  trend, but the reassessment had not yet been published. Public status copy
  uses only the current formal 2016 assessment.
- Phase 0 preflight: passed on 2026-07-30 in the no-approval local automation
  path.
- Duplicate correction: the first topic lock incorrectly treated ホライモリ as
  distinct from the completed Olm / *Proteus anguinus* package dated
  2026-04-30. The invalid draft was moved outside `infographic-packages`,
  INDEX and state were restored, and the replacement topic passed exact
  scientific, English, and Japanese name searches before lock.
- Live Automation prompt sync: completed on 2026-07-26 with the Quality Run
  prompt and refreshed on 2026-07-28 with explicit first-prompt ASCII spacing
  invariants, the four-part posting sequence, minimal story-reply overflow
  trimming, and the English common-name hashtag rule. `ACTIVE`, the daily
  10:00 schedule, model, reasoning effort, execution environment, and project
  target remained unchanged.

## Latest Package

- Latest package: `2026-07-30-red-river-hog`.
- State: `completed, published`.
- Production: Japanese direct poster passed on its first generation. The first
  English companion preserved the accepted composition but rendered the footer
  as `2016 : Least Concern (LC)`; one targeted correction restored the locked
  spacing without changing accepted art.
- Visual QA: both posters show one unobstructed adult Red River Hog in humid
  forest after sunset, with a brick-red coat, dark legs and muzzle, narrow
  white face lines, white dorsal mane, long pale ear tassels, cloven hooves,
  and a short tufted tail. Warthog and domestic-pig traits are absent.
- Composition QA: each poster uses exactly three unequal numbered illustrated
  cards around the hero for forest/thicket habitat, red-and-white identity,
  and after-dusk group foraging. Text is readable at phone size.
- Posting QA: four-block X sets use a short ear-tassel doorway, a connected
  forest-to-foraging story reply, actual-poster ALT text, and labeled source
  context. Both main posts include `#RedRiverHog`; eight sidecars match.
- Mechanical QA: both direct/posting pairs are exact 1024x1536; X format,
  full package validation, and whitespace checks passed.
- GitHub publishing: package/INDEX commit `fc6099c` was pushed to
  `origin/master`; the authoritative remote ref was verified at
  `fc6099c6a988f01e68b3f06d68e97870a57f02ad` before this published-state
  metadata commit.

## Recent-Eight Region Rotation

1. 2026-07-23 — Europe — Alpine Salamander
2. 2026-07-24 — South America — *Lysurus fossatii*
3. 2026-07-25 — Ocean/Global — Pelican Eel
4. 2026-07-26 — Asia — Himalayan Monal
5. 2026-07-27 — Africa — Gerenuk
6. 2026-07-28 — Australia/Oceania — Kea
7. 2026-07-29 — Central America/Caribbean — Pygmy Three-toed Sloth
8. 2026-07-30 — Africa — Red River Hog

Previous completed region: Africa.

## Verified Workspace Runtime

- Bundled Python:
  `C:\Users\ryusu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`
- Last verification: bundled runtime loaded on 2026-07-30. The completed Red
  River Hog Quality Run passed pre-image Copy Lock, separate direct-poster
  visual QA, phone-size QA, exact dimensions, X/sidecar checks, and full
  package QA.

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
- `#species-identity-drift`: 0/3 after the threshold correction and counter
  reset. The Pelican Eel tail-tip miss was followed by a five-limb Pygmy
  Three-toed Sloth and a failed masked correction. The resolved architecture
  now requires abandoning a repeatedly failing composition, approving the
  Japanese hero anatomy before companion production, and tracing each limb
  from torso origin through joint path to endpoint.
- `#layout-overcrowded`: 1/2 after the first Himalayan Monal composition hid
  the crest beneath the title panel; resolved by one targeted composition edit
  plus the opt-in lower-card layout.
- `#generic-production-drift`: reset after one architecture-level correction on
  2026-07-26. Fast Run made the poster and X copy mechanically consistent but
  visibly generic; the default was restored to complete direct Image Gen
  posters and narrative posting copy.
- `#topic-alias-duplication`: 1/2. The initial ホライモリ lock duplicated the
  completed Olm / *Proteus anguinus* package. The user caught it; the draft was
  removed from package scope and the replacement topic was checked by exact
  scientific, English, and Japanese names before lock.

## Next Concrete Change

- On the next new-topic run, begin duplicate screening with the accepted
  scientific name, then search English and Japanese aliases across memory,
  INDEX, folder names, and package contents before Evidence Lock.
- North America is absent from the latest eight and Africa appears twice;
  prefer a credible North American or otherwise underrepresented alternative
  and avoid another consecutive Africa topic.
- During evidence viability, treat an explicit Browser safety-policy block as
  a hard route boundary. Reject the candidate before lock or use a directly
  available official assessment DOI/PDF; use an explicit public caveat only
  while no direct official evidence is available, and remove it if stronger
  evidence later resolves the gap. Do not retry a blocked source through an
  alternate browser surface.
- Generate the complete Japanese poster first, visually accept it, then create
  the English companion from the same art direction. Do not use the deterministic
  composer as the default public asset.
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
