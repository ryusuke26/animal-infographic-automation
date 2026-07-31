# Automation 2 Current State

Updated: 2026-07-31T13:19:07+09:00

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
- Evidence route: user-supplied official IUCN species-page capture and matching
  assessment PDF `e.T41680A45215881`, Mammal Diversity Database taxonomy, the
  Mammal Science standard Japanese-name list, Animal Diversity Web, and USDA
  Forest Service.
- Confirmed: *Bassariscus astutus*, Ringtail / カコミスル, Global Least
  Concern (LC), assessed 1 March 2015 and published 2016, southwestern United
  States to Mexico, rocky and riparian habitats, large eyes, a long ringed
  tail, nocturnal activity, and 180-degree hind-foot rotation during headfirst
  descents. The official PDF lists current population trend as Unknown; no
  trend claim is used publicly.
- Phase 0 preflight: passed on 2026-07-31 in the no-approval local automation
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

- Latest package: `2026-07-31-ringtail`.
- State: `completed, published`.
- Production: after user review found the prior headfirst hero and isolated
  card-3 anatomy unnatural, the bilingual pair was fully remade. The Japanese
  redesign passed; the first English companion had a wrong 887x1774 ratio, and
  its one targeted regeneration restored exact 1024x1536.
- Visual QA: both remade posters show one unobstructed Ringtail walking
  naturally on all fours across a broad horizontal sandstone ledge, with large
  dark eyes, pale eye rings, rounded ears, a slender tan-grey body, exactly
  four continuous limbs, and one attached black-and-pale ringed tail. Cat,
  raccoon-mask, civet, lemur, detached-paw, and duplicated-tail traits are
  absent.
- Composition QA: each poster uses exactly three unequal numbered illustrated
  cards around the hero for rocky and riparian habitat, large eyes and ringed
  tail, and the 180-degree hind-foot mechanism. Card 3 now uses one complete
  descending mini Ringtail instead of detached or floating limb anatomy. Text
  is readable at phone size.
- Posting QA: four-block X sets use a moonlit-rock-ledge doorway, a
  connected habitat-to-climbing story reply, actual-poster ALT text, and
  labeled source context. Both main posts include `#Ringtail`; eight sidecars
  match.
- Mechanical QA: both direct/posting pairs are exact 1024x1536 and
  pixel-identical; final X format, package validation, and whitespace checks
  pass after the remake.
- Cleanup: after user approval, six rejected or superseded Ringtail PNGs were
  moved to the Windows Recycle Bin. The four canonical poster PNGs and all
  official IUCN evidence remain.
- GitHub publishing: package/INDEX commit `414b0ba` was pushed to
  `origin/master`; the authoritative remote ref was verified at
  `414b0ba4a944defdd78f70e7f7b744e76bb8f01d` before this published-state
  metadata commit.

## Recent-Eight Region Rotation

1. 2026-07-24 — South America — *Lysurus fossatii*
2. 2026-07-25 — Ocean/Global — Pelican Eel
3. 2026-07-26 — Asia — Himalayan Monal
4. 2026-07-27 — Africa — Gerenuk
5. 2026-07-28 — Australia/Oceania — Kea
6. 2026-07-29 — Central America/Caribbean — Pygmy Three-toed Sloth
7. 2026-07-30 — Africa — Red River Hog
8. 2026-07-31 — North America — Ringtail

Previous completed region: North America.

## Verified Workspace Runtime

- Bundled Python:
  `C:\Users\ryusu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`
- Last verification: bundled runtime loaded on 2026-07-31. The completed
  Ringtail Quality Run passed pre-image Copy Lock, separate direct-poster
  anatomy and text QA, phone-size QA, exact dimensions, X/sidecar checks, and
  full package QA.

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
- `#species-identity-drift`: 2/3 after the threshold correction and counter
  reset. The user found the corrected Ringtail's headfirst hero and isolated
  card-3 anatomy still unnatural. A full composition reset replaced the hero
  with a stable four-footed ledge walk and card 3 with a complete descending
  mini animal.
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
- Europe is absent from the latest eight and Africa appears twice; prefer a
  credible European or otherwise underrepresented alternative and avoid
  another consecutive North American topic.
- During evidence viability, treat an explicit Browser safety-policy block as
  a hard route boundary. Reject the candidate before lock or use a directly
  available official assessment DOI/PDF; use an explicit public caveat only
  while no direct official evidence is available, and remove it if stronger
  evidence later resolves the gap. Do not retry a blocked source through an
  alternate browser surface.
- Generate the complete Japanese poster first, visually accept it, then create
  the English companion from the same art direction. Do not use the deterministic
  composer as the default public asset.
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
