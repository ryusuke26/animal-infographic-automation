# Automation 2 Current State

Updated: 2026-08-14T23:08:27+09:00

This file is the small replace-in-place state record for Automation `automation-2`. Run history remains in automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English Image Gen posters, species-specific illustrated observation cards, and an editorial review of X copy.
- Pending evidence package: none.
- Active package: none.
- Retired package: none.
- The canonical package write gate remains repaired. Kipunji is `completed, published`.

## Completed Package

- Topic: Table Mountain Ghost Frog / テーブルマウンテンゴーストフロッグ / *Heleophryne rosei*.
- State: `completed, published`.
- Region: Table Mountain, South Africa / Africa.
- Editorial classification group: Amphibians.
- Evidence: the user-supplied official IUCN assessment PDF and matching species-page capture directly confirm Global Endangered (EN) under B1ab(iii), assessed 9 April 2024 and published in 2025 as record `e.T9773A247846769`. The public footer uses assessment year 2024. Amphibian Species of the World supports the accepted taxonomy, English name, and Table Mountain range; SANBI supports the cool rushing-stream habitat, flattened pale-green and purple-brown adult, broad toe discs, webbed hind feet, and sucker-mouthed tadpole; CEPF supports the Japanese name spelling.
- Candidate screen: Table Mountain Ghost Frog ranked above Kaiser's Mountain Newt, whose current assessment date was not directly inspectable, and *Pleurotus nebrodensis*, whose Japanese cultivated-name use created a material taxonomy and image-identity ambiguity.
- Visual resolution: the first Japanese source and its first English companion passed the canvas gate but were rejected because the left hind foot disappeared behind the broad dorsal silhouette. They were not used as edit targets and were moved to the Windows Recycle Bin at the user's request. One fresh-canvas retry per language produced accepted posters with four attached limbs, both hind feet outside the torso silhouette, one dominant adult, exact Copy Lock, and exactly three numbered species-specific illustrated cards. The four superseded 2025-footer source/posting PNGs were also moved to the Recycle Bin after the corrected 2024 canonical files and official evidence were protected.
- After direct official evidence separated the 2024 assessment year from 2025 publication, both accepted sources received localized footer edits to 2024. Both canonical direct posters pass the exact 2:3/full-canvas gate. Four canonical PNGs are exact `1024x1536`, direct/posting pairs are pixel-identical, and eight sidecars, X-format, package, full-size, phone-size, and whitespace QA pass.

## Latest Completed Package

- Package: `2026-08-14-kipunji`.
- State: `completed, published`.
- Region: Southern Tanzania / Africa.
- Editorial classification group: Mammals.
- Evidence: the preserved official IUCN assessment PDF and matching Red List page capture directly confirm Global EN under B1ab(ii,iii,iv,v)+2ab(ii,iii,iv,v), assessed 20 March 2018 and published in 2019 as record `e.T136791A17961368`. Public footers use assessment year 2018; the older 2008 CR entry is a previous assessment only.
- Visual resolution: the accepted Japanese and English posters retain one complete branch-standing Kipunji, four traceable limbs, a pelvis-connected pale-tipped tail, and exactly three numbered illustrated cards. A broad Image Gen correction was rejected because it redrew more than the footer. Deterministic localized repairs changed only the final footer-year digit from 2019 to 2018.
- Artifacts and QA: two official evidence files, four canonical `1024x1536` PNGs, eight synchronized sidecars, Copy Lock, prompts, README, sources QA, and INDEX are synchronized. Direct-source, X-format, package, phone/full-size, pixel-identity, and whitespace QA pass. Package content commit `180cdb2` was pushed directly to `origin/master` and remotely verified before the published-state metadata closeout.

## Recent-Eight Completed Region Rotation

1. 2026-08-07 — Philippines / Asia — Jade Vine
2. 2026-08-08 — North Pacific — Sea Angel
3. 2026-08-09 — Western Madagascar / Africa — Madagascan Big-headed Turtle
4. 2026-08-10 — Northern Colombia / South America — Blue-billed Curassow
5. 2026-08-11 — Central and southern Japan / Asia — Itasenpara Bitterling
6. 2026-08-12 — Table Mountain, South Africa / Africa — Table Mountain Ghost Frog
7. 2026-08-13 — East Asia / Asia — Bekko Tombo
8. 2026-08-14 — Southern Tanzania / Africa — Kipunji

Asia and Africa each occupy three of the latest eight; North Pacific and South America occupy one each.

## Recent-Eight Completed Classification Rotation

1. 2026-08-07 — Plants — Jade Vine
2. 2026-08-08 — Other invertebrates — Sea Angel
3. 2026-08-09 — Reptiles — Madagascan Big-headed Turtle
4. 2026-08-10 — Birds — Blue-billed Curassow
5. 2026-08-11 — Fishes — Itasenpara Bitterling
6. 2026-08-12 — Amphibians — Table Mountain Ghost Frog
7. 2026-08-13 — Insects — Bekko Tombo
8. 2026-08-14 — Mammals — Kipunji

Mammals, Plants, Other invertebrates, Reptiles, Birds, Fishes, Amphibians, and Insects each occupy one of the latest eight; Fungi and lichens remains absent.

## Daily Quality Loop Counters

- `#assessment-year-drift`: 2/2 after a second direct official artifact showed that a publication year had been used as the public footer year; Kipunji now uses assessment year 2018, while publication year 2019 remains source context. Future public footers require a directly inspected assessment-date field whenever an official artifact is available.
- `#species-identity-drift`: 2/3; reference role separation restored four-wing identity, while the user explicitly accepted the natural leg overlap in the selected bilingual pair.
- `#diagnostic-anatomy-priority`: 0/3 after reaching 3/3 and applying the hidden-anatomy gate; no hidden mechanism is involved in this package.
- `#duplicate-copy-placement`: 2/3; both selected sources place the six public lines once and retain three illustrated cards.
- `#topic-classification-drift`: 0/3 after the 2026-08-06 nine-group rotation rule and counter reset; Insects now occupies one completed slot.
- `#source-canvas-drift`: 0/2. Both fresh sources passed the exact 2:3/full-canvas gate; rejection was visual, not mechanical.

## Next Concrete Change

- Kipunji is finished at `completed, published`; preserve the accepted bilingual artwork and corrected 2018 footer.
- On the next automation run, perform Phase 0 preflight and select a new topic only if no unfinished package has appeared. Fungi and lichens remains absent from the latest eight, but rotation is still a tie-breaker.
- Package content commit `180cdb2` was pushed directly to `origin/master`; the published-state metadata commit and final remote-ref verification complete this closeout.
