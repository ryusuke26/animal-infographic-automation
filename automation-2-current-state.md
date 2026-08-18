# Automation 2 Current State

Updated: 2026-08-17T12:02:30+09:00

This file is the small replace-in-place state record for Automation `automation-2`. Run history remains in Automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English Image Gen posters, species-specific illustrated observation cards, and an editorial review of X copy.
- Pending evidence package: none.
- Active package: none.
- Retired package: none.
- The canonical package write gate is available.

## Latest Completed Package

- Package: `2026-08-17-tokashiki-freshwater-crab`.
- Topic: Tokashiki Freshwater Crab / トカシキオオサワガニ / *Geothelphusa levicervix*.
- State: `completed, local-ready`.
- Region: Tokashiki Island, Ryukyu Islands, Japan / Asia.
- Editorial classification group: Other invertebrates.
- Evidence: supplied official IUCN assessment PDF and matching current-page capture directly confirm Global Endangered (EN) under B1ab(iii)+2ab(iii), assessed and published 2008 as `T134902A4033497`. The taxon-page route is `134902/4033497`; `134902` alone is not the complete assessment identifier. WoRMS accepts *Geothelphusa levicervix*; Okinawa Prefecture supports the Japanese name, Tokashiki-only range, shaded narrow stream/wet-ground habitat, large male claw, and large-egg direct development. Local categories remain source context and are excluded from the public footer.
- Locked discovery: a large landlocked crab moves through a narrow forest stream on Tokashiki Island; a large male can carry one outsized claw, while large eggs develop directly into small crabs.
- Visual resolution: first Japanese and English direct Image Gen posters both passed the exact-2:3/full-canvas source gate and visual review without retries. Supplied official evidence then triggered a bounded deterministic text-safe repair: only the footer year glyphs changed from 2015 to 2008. Each preserves one complete adult male in wet shaded forest habitat, two claws, four visibly separate pairs of walking legs, an unobstructed hero, exact Copy Lock, and exactly three numbered illustrated cards.
- Artifacts and QA: four canonical `1024x1536` PNGs, two official evidence artifacts, four superseded 2015 PNGs, eight synchronized sidecars, Copy Lock, prompts, README, Sources QA, and INDEX are synchronized. Both direct sources, X format, package validation, full-size and phone-size review, pixel identity, localized-diff, and whitespace QA pass. Git and GitHub were deliberately not mutated.

## Recent-Eight Completed Region Rotation

1. 2026-08-10 — Northern Colombia / South America — Blue-billed Curassow
2. 2026-08-11 — Central and southern Japan / Asia — Itasenpara Bitterling
3. 2026-08-12 — Table Mountain, South Africa / Africa — Table Mountain Ghost Frog
4. 2026-08-13 — East Asia / Asia — Bekko Tombo
5. 2026-08-14 — Southern Tanzania / Africa — Kipunji
6. 2026-08-15 — Southeastern Australia and New Zealand South Island / Oceania — Tea-tree Fingers
7. 2026-08-16 — Mahé, Seychelles / Africa — Jellyfish Tree
8. 2026-08-17 — Tokashiki Island, Ryukyu Islands, Japan / Asia — Tokashiki Freshwater Crab

Asia and Africa occupy three of the latest eight; South America and Oceania occupy one each.

## Recent-Eight Completed Classification Rotation

1. 2026-08-10 — Birds — Blue-billed Curassow
2. 2026-08-11 — Fishes — Itasenpara Bitterling
3. 2026-08-12 — Amphibians — Table Mountain Ghost Frog
4. 2026-08-13 — Insects — Bekko Tombo
5. 2026-08-14 — Mammals — Kipunji
6. 2026-08-15 — Fungi and lichens — Tea-tree Fingers
7. 2026-08-16 — Plants — Jellyfish Tree
8. 2026-08-17 — Other invertebrates — Tokashiki Freshwater Crab

Birds, Fishes, Amphibians, Insects, Mammals, Fungi and lichens, Plants, and Other invertebrates each occupy one slot; Reptiles is absent.

## Daily Quality Loop Counters

- `#source-access-caveat`: resolved. The user-supplied official IUCN PDF and matching current-page capture made the assessment fields directly inspectable.
- `#assessment-year-drift`: 1 occurrence, fixed now. Japanese government material's 2015-list context was incorrectly used as a formal assessment year; every public and package surface now uses the official 2008 assessment/publication year and full ID `T134902A4033497`.
- `#species-identity-drift`: 0 in this run. Both first-generation posters preserved the large domed crab, two claws, four separate walking-leg pairs, wet stream habitat, and a single unobstructed hero.
- `#source-canvas-drift`: 0/2. Both direct posters are exact 2:3 full-canvas sources and are pixel-identical to their normalized posting counterparts.

## Next Concrete Change

- Tokashiki Freshwater Crab is finished at `completed, local-ready`; preserve the accepted artwork, official 2008 assessment evidence, and superseded 2015 audit assets. GitHub publication remains separate and was not attempted.
- On the next automation run, perform Phase 0 preflight and select a new topic only if no unfinished package has appeared. Reptiles is absent from the latest eight, but rotation remains a tie-breaker after international unfamiliarity, evidence, naming, and visual viability.
- For any later status update, require the official assessment's own Date Assessed, Year Published, criteria, and full assessment ID before changing public copy.
