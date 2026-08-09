# Automation 2 Current State

Updated: 2026-08-09T11:23:45+09:00

This file is the small replace-in-place state record for Automation
`automation-2`. Run history remains in automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English
  Image Gen posters, species-specific illustrated observation cards, and an
  editorial review of X copy.
- Pending evidence package: none.
- Active package: none; the Madagascan Big-headed Turtle run is complete and
  local-ready.
- Retired package: none.
- Phase 0 preflight passed and the dependency loader returned the bundled
  Python runtime. Unrelated untracked `scripts/__pycache__/` and `tmp/` were
  preserved.

## Completed Package

- Topic: Madagascan Big-headed Turtle / マダガスカルヨコクビガメ /
  *Erymnochelys madagascariensis*.
- State: `completed, local-ready`.
- Region: Western Madagascar / Africa.
- Editorial classification group: Reptiles.
- Evidence: the IUCN/TFTSG assessment supports Global CR under A4d, assessed
  15 January 2008. The current errata citation uses `e.T8070A97396666`; public
  footers correctly retain the assessment year 2008. The 2025 IUCN SSC turtle
  references support the accepted lineage, western river-and-lake habitat,
  large casque-covered head, and current identity. METI supports the Japanese
  name, and the Pleurodira lineage plus Sacramento Zoo support the complete
  side-neck movement.
- Candidate screen: Lord Howe Island Stick Insect was rejected as a completed
  duplicate. White-bellied Heron and Blue-billed Curassow remained viable but
  ranked below the turtle on discovery strength, directly settled assessment
  metadata, visual viability, and rotation value.
- Visual resolution: the first Japanese direct poster and first fresh English
  companion both passed without retries. Each has one dominant complete river
  turtle, a species-specific western Madagascar habitat, exactly three
  numbered illustrated cards, exact readable locked text, and one complete
  small side-neck mechanism turtle in card 3.
- Both canonical direct posters pass the exact 2:3/full-canvas source gate.
  Four canonical PNGs are exact `1024x1536`, direct/posting pairs are
  pixel-identical, and eight sidecars, X-format, package, full-size, phone-size,
  and whitespace QA pass.
- Git and GitHub were not mutated.

## Latest Completed Package

- Latest completed package is `2026-08-09-madagascan-big-headed-turtle`.
- State: `completed, local-ready`.
- Region: Western Madagascar / Africa.
- Editorial classification group: Reptiles.

## Recent-Eight Completed Region Rotation

1. 2026-08-02 — South America — Pacarana
2. 2026-08-03 — Antarctica / Southern Ocean — Antarctic Fur Seal
3. 2026-08-04 — Asia — Greater Hog Badger
4. 2026-08-05 — Africa — Maned Rat
5. 2026-08-06 — Central Australia / Oceania — Southern Marsupial Mole
6. 2026-08-07 — Asia — Jade Vine
7. 2026-08-08 — North Pacific — Sea Angel
8. 2026-08-09 — Western Madagascar / Africa — Madagascan Big-headed Turtle

Asia and Africa each occupy two of the latest eight; every other represented
broad region occupies one slot.

## Recent-Eight Completed Classification Rotation

1. 2026-08-02 — Mammals — Pacarana
2. 2026-08-03 — Mammals — Antarctic Fur Seal
3. 2026-08-04 — Mammals — Greater Hog Badger
4. 2026-08-05 — Mammals — Maned Rat
5. 2026-08-06 — Mammals — Southern Marsupial Mole
6. 2026-08-07 — Plants — Jade Vine
7. 2026-08-08 — Other invertebrates — Sea Angel
8. 2026-08-09 — Reptiles — Madagascan Big-headed Turtle

Mammals occupy 5/8; Plants, Other invertebrates, and Reptiles occupy one slot
each.

## Daily Quality Loop Counters

- `#assessment-year-drift`: 0/2 after the 2026-08-06 policy clarification and
  counter reset; the turtle footer uses the 2008 assessment year rather than
  the later errata context.
- `#species-identity-drift`: 2/3 after the 2026-08-06 visual-viability gate and
  counter reset; both turtle posters pass species-identity QA.
- `#diagnostic-anatomy-priority`: 0/3 after reaching 3/3 and applying the
  hidden-anatomy gate; the complete side-neck card passes without a new issue.
- `#duplicate-copy-placement`: 2/3; both accepted sources place each locked
  line once and preserve comfortable card margins.
- `#topic-classification-drift`: 0/3 after the 2026-08-06 nine-group rotation
  rule and counter reset; the completed Reptiles run improves the spread.
- `#source-canvas-drift`: 0/2. Both accepted direct posters pass the exact
  2:3/full-canvas gate.

## Next Concrete Change

- The Madagascan Big-headed Turtle package is finished at `completed,
  local-ready`; do not regenerate or publish it automatically.
- On the next daily run, perform Phase 0 preflight and screen a new topic.
  Prefer an absent group such as Birds, Amphibians, Fishes, Insects, or Fungi
  and lichens when unfamiliarity, evidence, naming, and visual viability remain
  strong; avoid repeating Africa or Reptiles when a comparable alternative
  passes all hard gates.
- Run exact accepted-name and package collision checks as soon as each
  candidate enters the slate, before deeper source review.
- GitHub publishing remains a separate user-authorized action.
