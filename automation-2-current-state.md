# Automation 2 Current State

Updated: 2026-08-11T20:23:14+09:00

This file is the small replace-in-place state record for Automation `automation-2`. Run history remains in automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English Image Gen posters, species-specific illustrated observation cards, and an editorial review of X copy.
- Pending evidence package: none.
- Active package: none; the Itasenpara Bitterling run is complete and published.
- Retired package: none.
- Phase 0 preflight passed. The dependency loader was not exposed in this environment, so the previously recorded bundled Python 3.12.13 runtime, Pillow 12.2.0 import, and validator startup were verified once. The preflight worktree was clean.

## Completed Package

- Topic: Itasenpara Bitterling / イタセンパラ / *Acheilognathus longipinnis*.
- State: `completed, published`.
- Region: Central and southern Japan / Asia.
- Editorial classification group: Fishes.
- Evidence: the directly inspected official IUCN assessment PDF and matching species-page capture confirm Global EN under B2ab(ii,iii,v), assessed 7 December 2017 and published in 2019 as `e.T213A116034178`; 2017 remains the public footer year. Japan's Ministry of the Environment and the National Museum of Nature and Science support the Japanese and scientific names, floodplain-water habitat, deep thin high-backed body, autumn male coloration, and mussel spawning with juvenile emergence around May. Japan's national CR category remains separate from the public global footer.
- Candidate screen: Itasenpara ranked above Australian Lungfish, which failed the global-familiarity gate as a recurring air-breathing ancient-fish subject. Mountain Chicken Frog remained credible but its field-level IUCN assessment date could not be directly inspected in this environment.
- Visual resolution: the first Japanese direct poster and first fresh English companion both passed without retries. Each has one complete breeding male, a coherent autumn-backwater field-note composition, exact readable Copy Lock, and exactly three numbered illustrated cards including one complete female beside a restrained freshwater-mussel cutaway.
- Both canonical direct posters pass the exact 2:3/full-canvas source gate. Four canonical PNGs are exact `1024x1536`, direct/posting pairs are pixel-identical, and eight sidecars, X-format, package, full-size, phone-size, and whitespace QA pass.
- Package content commit `7fd33fd` was pushed directly to `origin/master`; the remote ref was verified at `7fd33fd3b0f9de708ff786d2f490df00286063ae` before the published-state metadata update.

## Latest Completed Package

- Latest completed package is `2026-08-11-itasenpara-bitterling`.
- State: `completed, published`.
- Region: Central and southern Japan / Asia.
- Editorial classification group: Fishes.

## Recent-Eight Completed Region Rotation

1. 2026-08-04 — Asia — Greater Hog Badger
2. 2026-08-05 — Africa — Maned Rat
3. 2026-08-06 — Central Australia / Oceania — Southern Marsupial Mole
4. 2026-08-07 — Asia — Jade Vine
5. 2026-08-08 — North Pacific — Sea Angel
6. 2026-08-09 — Western Madagascar / Africa — Madagascan Big-headed Turtle
7. 2026-08-10 — Northern Colombia / South America — Blue-billed Curassow
8. 2026-08-11 — Central and southern Japan / Asia — Itasenpara Bitterling

Asia occupies three of the latest eight and Africa occupies two; every other represented broad region occupies one slot.

## Recent-Eight Completed Classification Rotation

1. 2026-08-04 — Mammals — Greater Hog Badger
2. 2026-08-05 — Mammals — Maned Rat
3. 2026-08-06 — Mammals — Southern Marsupial Mole
4. 2026-08-07 — Plants — Jade Vine
5. 2026-08-08 — Other invertebrates — Sea Angel
6. 2026-08-09 — Reptiles — Madagascan Big-headed Turtle
7. 2026-08-10 — Birds — Blue-billed Curassow
8. 2026-08-11 — Fishes — Itasenpara Bitterling

Mammals occupy 3/8; Plants, Other invertebrates, Reptiles, Birds, and Fishes occupy one slot each.

## Daily Quality Loop Counters

- `#assessment-year-drift`: 0/2 after the 2026-08-06 policy clarification and counter reset; the Itasenpara footer uses the field-level 2017 assessment year, not the later IUCN change-table release.
- `#species-identity-drift`: 2/3 after the 2026-08-06 visual-viability gate and counter reset; both Itasenpara posters pass deep-body, fin, color, and habitat identity QA.
- `#diagnostic-anatomy-priority`: 0/3 after reaching 3/3 and applying the hidden-anatomy gate; no hidden mechanism is involved in this package.
- `#duplicate-copy-placement`: 2/3; both accepted sources place each locked line once and preserve comfortable card margins.
- `#topic-classification-drift`: 0/3 after the 2026-08-06 nine-group rotation rule and counter reset; Fishes join the completed rotation.
- `#source-canvas-drift`: 0/2. Both accepted direct posters pass the exact 2:3/full-canvas gate.

## Next Concrete Change

- The Itasenpara Bitterling package is finished at `completed, published`; do not regenerate or alter the accepted posters.
- On the next daily run, perform Phase 0 preflight and screen a new topic. Prefer an absent group such as Amphibians, Insects, or Fungi and lichens when unfamiliarity, evidence, naming, and visual viability remain strong; avoid repeating Asia or Fishes when a comparable alternative passes all hard gates.
- Run exact accepted-name and package collision checks as soon as each candidate enters the slate, before deeper source review.
- GitHub closeout is complete for the Itasenpara Bitterling package; package commit `7fd33fd` is on `origin/master`, with this published-state metadata update following as the final closeout commit.
