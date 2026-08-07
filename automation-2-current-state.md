# Automation 2 Current State

Updated: 2026-08-07T10:44:40+09:00

This file is the small replace-in-place state record for Automation
`automation-2`. Run history remains in automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English
  Image Gen posters, species-specific illustrated observation cards, and an
  editorial review of X copy.
- Pending evidence package: none.
- Active package: none.
- Retired package: none.
- Phase 0 preflight passed and the dependency loader returned the bundled
  Python runtime. Unrelated untracked `scripts/__pycache__/` and `tmp/` were
  preserved.

## Completed Package

- Topic: Jade Vine / ヒスイカズラ / *Strongylodon macrobotrys*.
- State: `completed, local-ready`.
- Region: Philippines / Asia.
- Editorial classification group: Plants.
- Evidence: Kew POWO accepts the scientific name, lists two heterotypic
  synonyms, and records a Philippine wet-tropical liana. Kew and 筑波実験植物園
  support the bilingual names, pendent blue-green hooked flowers, and visual
  identity. Kew also supports the bat-pollination sequence.
- Status route: exact IUCN searches under the accepted name and both synonyms
  did not surface a global assessment on 2026-08-07. Public footers use the
  conservative no-global-assessment-confirmed wording and do not present
  formal `IUCN NE`.
- Visual production: the first Japanese direct poster and first English
  companion both passed without retry. Each has one connected woody vine, one
  dominant hanging jade-blue truss, trifoliate leaves, and exactly three
  unequal numbered illustrated cards.
- QA: both direct/posting pairs are exact `1024x1536` and pixel-identical;
  direct-source gates, exact Copy Lock, full-size and phone-size visual review,
  eight synchronized sidecars, X format, full package validation, and
  whitespace checks passed.
- GitHub publishing was not attempted.

## Latest Completed Package

- Latest completed package is `2026-08-07-jade-vine`.
- State: `completed, local-ready`.
- Region: Philippines / Asia.
- Editorial classification group: Plants.

## Recent-Eight Completed Region Rotation

1. 2026-07-31 — North America — Ringtail
2. 2026-08-01 — Europe — Russian Desman
3. 2026-08-02 — South America — Pacarana
4. 2026-08-03 — Antarctica / Southern Ocean — Antarctic Fur Seal
5. 2026-08-04 — Asia — Greater Hog Badger
6. 2026-08-05 — Africa — Maned Rat
7. 2026-08-06 — Central Australia / Oceania — Southern Marsupial Mole
8. 2026-08-07 — Asia — Jade Vine

Asia occupies two of the latest eight; every other represented broad region
occupies one slot. Yesterday's Central Australia/Oceania region was not
repeated.

## Recent-Eight Completed Classification Rotation

1. 2026-07-31 — Mammals — Ringtail
2. 2026-08-01 — Mammals — Russian Desman
3. 2026-08-02 — Mammals — Pacarana
4. 2026-08-03 — Mammals — Antarctic Fur Seal
5. 2026-08-04 — Mammals — Greater Hog Badger
6. 2026-08-05 — Mammals — Maned Rat
7. 2026-08-06 — Mammals — Southern Marsupial Mole
8. 2026-08-07 — Plants — Jade Vine

Plants now occupy one slot and Mammals occupy 7/8. The next run should still
strongly prefer a credible non-mammal group other than Plants when evidence,
naming, and visual viability are adequate.

## Daily Quality Loop Counters

- `#assessment-year-drift`: 0/2 after the 2026-08-06 policy clarification and
  counter reset.
- `#species-identity-drift`: 2/3 after the 2026-08-06 visual-viability gate and
  counter reset; today's botanical pair adds no drift event.
- `#diagnostic-anatomy-priority`: 0/3 after the 2026-08-06 nasal-shield prompt
  correction and counter reset.
- `#duplicate-copy-placement`: 1/3; today's poster text was placed once only.
- `#topic-classification-drift`: 0/3 after the 2026-08-06 nine-group rotation
  rule and counter reset; today's Plant selection exercised the correction.
- `#source-canvas-drift`: 0/2. Both direct sources passed exact-2:3/full-canvas
  gates on their first generation.

## Next Concrete Change

- Begin the next run with no active package and select a new topic.
- Do not repeat *Strongylodon macrobotrys*; its package is completed locally.
- Strongly prefer an evidence-ready non-mammal group other than Plants because
  Mammals still occupy seven of the latest eight completed slots.
- Keep publication/citation year separate from the field-level assessment year
  before locking any dated public footer.
- Finish at `completed, local-ready`; GitHub publishing remains separate.
