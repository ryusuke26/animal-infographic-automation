# Automation 2 Current State

Updated: 2026-08-08T23:01:27+09:00

This file is the small replace-in-place state record for Automation
`automation-2`. Run history remains in automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English
  Image Gen posters, species-specific illustrated observation cards, and an
  editorial review of X copy.
- Pending evidence package: none.
- Active package: none; the Sea Angel run is complete and local-ready.
- Retired package: none.
- Phase 0 preflight passed and the dependency loader returned the bundled
  Python runtime. Unrelated untracked `scripts/__pycache__/` and `tmp/` were
  preserved.

## Completed Package

- Topic: Sea Angel / ハダカカメガイ / *Clione elegantissima*.
- State: `completed, local-ready`.
- Region: Southern Sea of Okhotsk / North Pacific.
- Editorial classification group: Other invertebrates.
- Evidence: JAMSTEC BISMaL and Aquarium Fukushima support the accepted names,
  current gastropod lineage, cold drift-ice-season habitat, shell-less adult
  form, wing-like feet, and conical feeding structures. A 2022 Polar Science
  study supports winter and early-spring occurrence in the southern Sea of
  Okhotsk. Toba Aquarium photographs and primary descriptions support three
  bilateral pairs of buccal cones at the anterior head apex.
- Status route: exact IUCN searches under accepted, historical, broader,
  related, and English names did not surface a global assessment on 2026-08-08.
  Public footers conservatively report no confirmed global assessment and do
  not present formal `IUCN NE`.
- Visual resolution: the user supplied one diagnostic sketch and two real
  feeding photographs after rejecting earlier anatomy and typography failures.
  A fresh Japanese poster used those only as references and passed the complete
  animal, compact head-top origin, thick curved six-cone, Copy Lock, and layout
  gates; the user explicitly selected it despite the small prey icon. A fresh
  English companion preserved the selected anatomy and composition on its
  first generation.
- Both canonical direct posters pass the exact 2:3/full-canvas source gate.
  Four canonical PNGs are exact `1024x1536`, direct/posting pairs are
  pixel-identical, and eight sidecars, X-format, package, full-size, phone-size,
  and whitespace QA pass.
- Git and GitHub were not mutated.

## Latest Completed Package

- Latest completed package is `2026-08-08-sea-angel`.
- State: `completed, local-ready`.
- Region: Southern Sea of Okhotsk / North Pacific.
- Editorial classification group: Other invertebrates.

## Recent-Eight Completed Region Rotation

1. 2026-08-01 — Europe — Russian Desman
2. 2026-08-02 — South America — Pacarana
3. 2026-08-03 — Antarctica / Southern Ocean — Antarctic Fur Seal
4. 2026-08-04 — Asia — Greater Hog Badger
5. 2026-08-05 — Africa — Maned Rat
6. 2026-08-06 — Central Australia / Oceania — Southern Marsupial Mole
7. 2026-08-07 — Asia — Jade Vine
8. 2026-08-08 — North Pacific — Sea Angel

Asia occupies two of the latest eight; every other represented broad region
occupies one slot.

## Recent-Eight Completed Classification Rotation

1. 2026-08-01 — Mammals — Russian Desman
2. 2026-08-02 — Mammals — Pacarana
3. 2026-08-03 — Mammals — Antarctic Fur Seal
4. 2026-08-04 — Mammals — Greater Hog Badger
5. 2026-08-05 — Mammals — Maned Rat
6. 2026-08-06 — Mammals — Southern Marsupial Mole
7. 2026-08-07 — Plants — Jade Vine
8. 2026-08-08 — Other invertebrates — Sea Angel

Mammals occupy 6/8; Plants and Other invertebrates occupy one slot each.

## Daily Quality Loop Counters

- `#assessment-year-drift`: 0/2 after the 2026-08-06 policy clarification and
  counter reset.
- `#species-identity-drift`: 2/3 after the 2026-08-06 visual-viability gate and
  counter reset; the user-approved Sea Angel pair passes species-identity QA.
- `#diagnostic-anatomy-priority`: 0/3 after reaching 3/3 and applying a new
  hidden-anatomy aperture-position/opening-direction gate to the production
  policy. The counter is reset.
- `#duplicate-copy-placement`: 2/3; the first rejected fresh Japanese source
  duplicated the status footer and displaced card labels into the title area.
- `#topic-classification-drift`: 0/3 after the 2026-08-06 nine-group rotation
  rule and counter reset; the completed Other invertebrates run improves the
  latest-eight classification spread.
- `#source-canvas-drift`: 0/2. Both accepted direct posters pass the exact
  2:3/full-canvas gate.

## Next Concrete Change

- The Sea Angel run is finished at `completed, local-ready`; do not regenerate
  or alter the user-selected Japanese poster in a future run.
- On the next daily run, perform Phase 0 preflight and screen a new topic. The
  latest completed group rotation is Mammals 6/8, Plants 1/8, and Other
  invertebrates 1/8, so continue preferring an absent non-mammal group when
  evidence and visual viability are strong.
- Preserve the improved hidden-anatomy gate: aperture position, compact origin,
  bilateral count, intact surrounding body, complete mechanism animal, and
  comfortable card-copy margins must pass together.
- GitHub publishing remains a separate approved action.
