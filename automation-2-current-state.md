# Automation 2 Current State

Updated: 2026-08-10T11:23:30+09:00

This file is the small replace-in-place state record for Automation `automation-2`. Run history remains in automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English Image Gen posters, species-specific illustrated observation cards, and an editorial review of X copy.
- Pending evidence package: none.
- Active package: none; the Blue-billed Curassow run is complete and local-ready.
- Retired package: none.
- Phase 0 preflight passed and the dependency loader returned the bundled Python runtime. Unrelated untracked `scripts/__pycache__/` and `tmp/` were preserved.

## Completed Package

- Topic: Blue-billed Curassow / アオコブホウカンチョウ / *Crax alberti*.
- State: `completed, local-ready`.
- Region: Northern Colombia / South America.
- Editorial classification group: Birds.
- Evidence: the official IUCN 2025 assessment supports Global CR under A4cd, record `e.T22678525A265023587`. METI supports the Japanese name. Smithsonian supports northern Colombian lowland-forest habitat, the adult male's localized blue cere and curled black crest, and forest-floor feeding on fruit and invertebrates.
- Candidate screen: Blue-billed Curassow ranked above White-bellied Heron on discovery strength and above Purple Frog, which failed the global-familiarity gate as a recurring English-language unusual-animal subject.
- Visual resolution: the first Japanese direct poster and first fresh English companion both passed without retries. Each has one complete adult male, a coherent humid lowland-forest composition, exact readable Copy Lock, and exactly three numbered illustrated cards including one complete feeding mini-bird.
- Both canonical direct posters pass the exact 2:3/full-canvas source gate. Four canonical PNGs are exact `1024x1536`, direct/posting pairs are pixel-identical, and eight sidecars, X-format, package, full-size, phone-size, and whitespace QA pass.
- GitHub publishing was not attempted.

## Latest Completed Package

- Latest completed package is `2026-08-10-blue-billed-curassow`.
- State: `completed, local-ready`.
- Region: Northern Colombia / South America.
- Editorial classification group: Birds.

## Recent-Eight Completed Region Rotation

1. 2026-08-03 — Antarctica / Southern Ocean — Antarctic Fur Seal
2. 2026-08-04 — Asia — Greater Hog Badger
3. 2026-08-05 — Africa — Maned Rat
4. 2026-08-06 — Central Australia / Oceania — Southern Marsupial Mole
5. 2026-08-07 — Asia — Jade Vine
6. 2026-08-08 — North Pacific — Sea Angel
7. 2026-08-09 — Western Madagascar / Africa — Madagascan Big-headed Turtle
8. 2026-08-10 — Northern Colombia / South America — Blue-billed Curassow

Asia and Africa each occupy two of the latest eight; every other represented broad region occupies one slot.

## Recent-Eight Completed Classification Rotation

1. 2026-08-03 — Mammals — Antarctic Fur Seal
2. 2026-08-04 — Mammals — Greater Hog Badger
3. 2026-08-05 — Mammals — Maned Rat
4. 2026-08-06 — Mammals — Southern Marsupial Mole
5. 2026-08-07 — Plants — Jade Vine
6. 2026-08-08 — Other invertebrates — Sea Angel
7. 2026-08-09 — Reptiles — Madagascan Big-headed Turtle
8. 2026-08-10 — Birds — Blue-billed Curassow

Mammals occupy 4/8; Plants, Other invertebrates, Reptiles, and Birds occupy one slot each.

## Daily Quality Loop Counters

- `#assessment-year-drift`: 0/2 after the 2026-08-06 policy clarification and counter reset; the curassow footer uses the 2025 assessment year.
- `#species-identity-drift`: 2/3 after the 2026-08-06 visual-viability gate and counter reset; both curassow posters pass species-identity QA.
- `#diagnostic-anatomy-priority`: 0/3 after reaching 3/3 and applying the hidden-anatomy gate; no hidden mechanism is involved in this package.
- `#duplicate-copy-placement`: 2/3; both accepted sources place each locked line once and preserve comfortable card margins.
- `#topic-classification-drift`: 0/3 after the 2026-08-06 nine-group rotation rule and counter reset; Birds join the completed rotation.
- `#source-canvas-drift`: 0/2. Both accepted direct posters pass the exact 2:3/full-canvas gate.

## Next Concrete Change

- The Blue-billed Curassow package is finished at `completed, local-ready`; do not regenerate or alter the accepted posters.
- On the next daily run, perform Phase 0 preflight and screen a new topic. Prefer an absent group such as Amphibians, Fishes, Insects, or Fungi and lichens when unfamiliarity, evidence, naming, and visual viability remain strong; avoid repeating South America or Birds when a comparable alternative passes all hard gates.
- Run exact accepted-name and package collision checks as soon as each candidate enters the slate, before deeper source review.
- GitHub publication remains a separate user-authorized closeout.
