# Automation 2 Current State

Updated: 2026-08-18T22:42:26+09:00

This file is the small replace-in-place state record for Automation `automation-2`. Run history remains in Automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English Image Gen posters, species-specific illustrated observation cards, and an editorial review of X copy.
- Pending evidence package: none.
- Active package: none.
- Active state: idle after `2026-08-18-gunthers-gecko` completed and published.
- Active evidence: preserved official IUCN errata PDF and matching current-page capture confirm Global VU D2, assessed 23 April 2018 as `T16926A152274946`. Red List year 2018 remains public; 2019 is only the errata-publication year, and the separately displayed 2024 Critically Depleted result is Green Status rather than a Red List category.
- Retired package: none.
- The canonical package write gate is available.

## Latest Completed Package

- Package: `2026-08-18-gunthers-gecko`.
- Topic: Günther's Gecko / ギュンターヒルヤモリ / *Phelsuma guentheri*.
- State: `completed, published`.
- Region: Round Island, Mauritius / Africa.
- Editorial classification group: Reptiles.
- Evidence: preserved official IUCN errata PDF and matching current-page capture directly confirm Global Vulnerable (VU) under D2, assessed 23 April 2018 as `T16926A152274946`. The Red List year remains 2018; the errata version was published in 2019, and the separate 2024 Critically Depleted result is Green Status rather than a Red List category. The Reptile Database, Mauritius government material, and Roesch et al. (2021) support taxonomy, palm-rich habitat, muted large body, adhesive toe pads, day-and-night activity, and communal nesting.
- Locked discovery: a gray-brown day gecko disappears against Round Island palm trunks, moves by day and night, and several females can share one attached-egg nest site.
- Visual resolution: the user accepted the communal-nesting Card 2 revision as the final Japanese poster, explicitly allowing its wider redraw and softer rendering; natural far-side limb occlusion remains valid and was not forced into view. The first fresh-canvas English companion passed without retry. Both have one dominant muted gecko, exactly three numbered illustrated cards, exact Copy Lock, and coherent palm-and-screwpine habitat.
- Artifacts and QA: four canonical `1024x1536` PNGs, two official evidence artifacts, four preserved Japanese visual-history artifacts, eight synchronized sidecars, Copy Lock, prompts, README, Sources QA, and INDEX are synchronized. Both direct sources, X format, package validation, full-size and phone-size review, pixel identity, and whitespace QA pass. Package content commit `063b34e` was pushed directly to `origin/master` and remotely verified.
- Automation memory sync: the completion and GitHub closeout entry was appended during the approved publication closeout.

## Recent-Eight Completed Region Rotation

1. 2026-08-11 — Central and southern Japan / Asia — Itasenpara Bitterling
2. 2026-08-12 — Table Mountain, South Africa / Africa — Table Mountain Ghost Frog
3. 2026-08-13 — East Asia / Asia — Bekko Tombo
4. 2026-08-14 — Southern Tanzania / Africa — Kipunji
5. 2026-08-15 — Southeastern Australia and New Zealand South Island / Oceania — Tea-tree Fingers
6. 2026-08-16 — Mahé, Seychelles / Africa — Jellyfish Tree
7. 2026-08-17 — Tokashiki Island, Ryukyu Islands, Japan / Asia — Tokashiki Freshwater Crab
8. 2026-08-18 — Round Island, Mauritius / Africa — Günther's Gecko

Africa occupies four of the latest eight, Asia three, and Oceania one.

## Recent-Eight Completed Classification Rotation

1. 2026-08-11 — Fishes — Itasenpara Bitterling
2. 2026-08-12 — Amphibians — Table Mountain Ghost Frog
3. 2026-08-13 — Insects — Bekko Tombo
4. 2026-08-14 — Mammals — Kipunji
5. 2026-08-15 — Fungi and lichens — Tea-tree Fingers
6. 2026-08-16 — Plants — Jellyfish Tree
7. 2026-08-17 — Other invertebrates — Tokashiki Freshwater Crab
8. 2026-08-18 — Reptiles — Günther's Gecko

Fishes, Amphibians, Insects, Mammals, Fungi and lichens, Plants, Other invertebrates, and Reptiles each occupy one slot; Birds is absent.

## Daily Quality Loop Counters

- `#source-access-caveat`: resolved. The user-supplied official errata PDF and matching current-page capture directly expose Global VU D2, assessment date 23 April 2018, Red List publication year 2018, current record `T16926A152274946`, DOI, and the separate Green Status panel.
- `#assessment-year-drift`: 0 in this run. The public footer uses the directly inspected 2018 assessment year.
- `#species-identity-drift`: resolved by user-reviewed viewpoint logic. Natural far-side limb occlusion is not treated as missing anatomy; no corrective limb was forced into the accepted posters.
- `#source-canvas-drift`: 0/2 canonical sources. Both accepted direct posters are exact 1024x1536, exact 2:3, and full-canvas.
- `#selected-poster-preservation`: explicit exception recorded. The accepted Japanese Card 2 revision changed 67.396% outside the intended local region, but the user reviewed and selected that exact wider redraw as the final poster.

## Next Concrete Change

- Begin the next scheduled run with no unfinished package.
- Exclude Africa from an otherwise tied candidate slate because it now occupies four of the latest eight; use rotation only after unfamiliarity, evidence, discovery strength, naming, and visual viability.
- Birds is absent from the latest eight classification groups and may break a tie among equally strong candidates.
- Keep the next Quality Run local-ready until GitHub publication is explicitly requested and remotely verified.
