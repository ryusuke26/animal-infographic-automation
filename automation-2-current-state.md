# Automation 2 Current State

Updated: 2026-08-07T00:38:15+09:00

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
  Python runtime. Unrelated untracked
  `scripts/__pycache__/` and `tmp/` were preserved.

## Completed Package

- Topic: Southern Marsupial Mole / フクロモグラ / *Notoryctes typhlops*.
- State: `completed, published`.
- Evidence: the user-supplied official IUCN screenshot and matching 11-page PDF
  confirm Global LC, assessed 15 March 2014 and published 2016, record
  `e.T14879A21965004`. Public footers use assessment year 2014.
- User-selected recovery: after comparing localized nasal-shield variants, the
  user explicitly selected the source-gate-passing photo-informed Japanese
  sketch poster. That visual choice supersedes the poster's earlier rejection.
- English companion: the first fresh-canvas generation used only the accepted
  Japanese poster as a visual reference and preserved its silhouette, broad
  nasal shield, two dominant foreclaws, hard ringed tail, dune cutaway,
  handmade medium, and exact English Copy Lock.
- QA: both direct/posting pairs are exact `1024x1536` and pixel-identical; four
  canonical PNGs, eight synchronized sidecars, direct-source gates, X format,
  full package validation, phone/full-size visual review, and whitespace checks
  passed.
- Earlier rejected workspace PNGs remained in the Windows Recycle Bin; no
  failed cache artifacts were imported into the package.
- Selected-image cleanup completed: the two user-confirmed cache images still
  match the canonical direct posters by SHA-256. Exactly nine rejected or
  superseded regular cache PNGs with non-matching hashes were moved to the
  Windows Recycle Bin in an approval-enabled context. The cache now contains
  only the two accepted images, and the package still contains only its four
  required direct/posting PNGs.
- GitHub closeout: package commit `f5156fa` and workflow-quality commit
  `647826f` were pushed directly to `origin/master`; the remote ref matched
  local HEAD at `647826fe824107c05ff84bb0b90d77e5393e094c` before the
  published-state metadata update.

## Latest Completed Package

- Latest completed package is `2026-08-06-southern-marsupial-mole`.
- State: `completed, published`.
- Region: Central Australia / Oceania.
- Editorial classification group: Mammals.

## Recent-Eight Completed Region Rotation

1. 2026-07-30 — Africa — Red River Hog
2. 2026-07-31 — North America — Ringtail
3. 2026-08-01 — Europe — Russian Desman
4. 2026-08-02 — South America — Pacarana
5. 2026-08-03 — Antarctica / Southern Ocean — Antarctic Fur Seal
6. 2026-08-04 — Asia — Greater Hog Badger
7. 2026-08-05 — Africa — Maned Rat
8. 2026-08-06 — Central Australia / Oceania — Southern Marsupial Mole

Australia/Oceania is now represented. Africa occupies two of the latest eight;
the other represented broad regions occupy one slot each.

## Recent-Eight Completed Classification Rotation

1. 2026-07-30 — Mammals — Red River Hog
2. 2026-07-31 — Mammals — Ringtail
3. 2026-08-01 — Mammals — Russian Desman
4. 2026-08-02 — Mammals — Pacarana
5. 2026-08-03 — Mammals — Antarctic Fur Seal
6. 2026-08-04 — Mammals — Greater Hog Badger
7. 2026-08-05 — Mammals — Maned Rat
8. 2026-08-06 — Mammals — Southern Marsupial Mole

Mammals occupy 8/8 completed slots. The next run must strongly prefer a
credible non-mammal candidate. The ideal correction also fills the missing
classification gap; region is now a secondary consideration. Completing this
package is not a new-selection exception because the user explicitly reopened
an already selected retired topic.

## Daily Quality Loop Counters

- `#assessment-year-drift`: 0/2 after the 2026-08-06 policy clarification and
  counter reset.
- `#species-identity-drift`: 2/3 after the 2026-08-06 visual-viability gate and
  counter reset; the user explicitly accepted the coherent source-gate-passing
  stylized shield treatment, so this recovery adds no new drift event.
- `#diagnostic-anatomy-priority`: 0/3 after the latest prompt was hardened to
  require exactly one continuous nasal pad with at most one shallow crease and
  to ban stacked lobes.
- `#duplicate-copy-placement`: 1/3.
- `#topic-classification-drift`: 0/3 after the 2026-08-06 nine-group rotation
  rule and metadata gate were added in response to an 8/8 mammal concentration.
- `#source-canvas-drift`: 0/2. Every generated source passed the mechanical
  exact-2:3/full-canvas gate; the blocker was biological identity.

## Next Concrete Change

- Begin the next run with no active package and select a new topic.
- Do not repeat *Notoryctes typhlops*; its completed package is published.
- Strongly prefer an evidence-ready non-mammal with a reliably representable
  body plan because Mammals occupy all eight latest completed slots. Region is
  secondary now that Australia/Oceania is represented.
- Keep publication/citation year separate from the field-level assessment year
  before locking any dated public footer.
- Finish at `completed, local-ready`; GitHub publishing remains separate.
