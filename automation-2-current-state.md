# Automation 2 Current State

Updated: 2026-08-05T13:20:11+09:00

This file is the small replace-in-place state record for Automation
`automation-2`. Run history remains in automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English
  Image Gen posters, species-specific illustrated observation cards, and an
  editorial review of X copy.
- Pending evidence package: none.
- Active package: none.
- Phase 0 preflight: passed on 2026-08-05 with bundled Python 3.12.13 and
  Pillow available. Unrelated untracked `scripts/__pycache__/` and `tmp/` were
  preserved.
- Duplicate screening: *Lophiomys imhausii*, *Lophiomys imhausi*, Maned Rat,
  Crested Rat, and タテガミネズミ were searched across memory, INDEX, package
  folders, and package contents before Evidence Lock; no collision was found.

## Latest Package

- Latest package: `2026-08-05-maned-rat`.
- State: `completed, local-ready`.
- Region: Africa / East Africa.
- Workflow mode: Quality Run with a narrow Caution Run taxonomy and spelling
  cross-check.
- Evidence route: current MDD accepts *Lophiomys imhausii*. The user-supplied
  official IUCN species-page screenshot and matching seven-page assessment PDF
  directly confirm Global LC under older spelling *Lophiomys imhausi*, assessed
  31 January 2016, published 2016, record `e.T12308A22368581`. Both official
  evidence files are preserved with hashes in the package.
- Confirmed: Maned Rat / タテガミネズミ; eastern African wooded and riparian
  habitat; long gray-brown mane; black-and-white lateral warning bands; and
  application of chewed *Acokanthera* compounds to specialized flank hairs.
- Visual QA: the user selected the supplied first Japanese generation as the
  canonical visual. Its correct 2016 LC footer was synchronized into Japanese
  Copy Lock and posting copy; no image regeneration was needed after official
  evidence confirmation. The English companion passed first generation. Both
  posters retain one dominant hero, wooded-stream habitat, and exactly three
  numbered illustrated cards.
- Mechanical QA: both direct-source gates, exact `1024x1536` direct/posting
  pixel identity, X format, eight sidecars, full package validation, phone/full-
  size visual review, and whitespace checks passed.
- Cleanup: at the user's request, exactly three explicitly rejected Japanese
  PNGs were moved to the Windows Recycle Bin. Only the four canonical direct
  and posting PNGs remain; official evidence files were preserved.
- GitHub publishing: not attempted. Final state is local-ready only.

## Recent-Eight Region Rotation

1. 2026-07-29 — Central America/Caribbean — Pygmy Three-toed Sloth
2. 2026-07-30 — Africa — Red River Hog
3. 2026-07-31 — North America — Ringtail
4. 2026-08-01 — Europe — Russian Desman
5. 2026-08-02 — South America — Pacarana
6. 2026-08-03 — Antarctica / Southern Ocean — Antarctic Fur Seal
7. 2026-08-04 — Asia — Greater Hog Badger
8. 2026-08-05 — Africa — Maned Rat

Previous completed region: Africa. Africa appears twice; Australia/Oceania is
the only absent broad region in the latest eight.

## Verified Workspace Runtime

- Bundled Python:
  `C:\Users\ryusu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`
- Verification: both canonical direct posters pass the exact-2:3/full-canvas
  source gate; both posting PNGs are `1024x1536` and pixel-identical to their
  language source.

## Daily Quality Loop Counters

- `#image-text-error`: 2/3 after the prior threshold improvement and counter
  reset. No extra-card-copy occurrence was added in this package.
- `#verbatim-glyph-drift`: 2/3. The Japanese footer punctuation differed from
  the initial lock; the user selected that poster and the semantically
  equivalent visible punctuation was re-locked across public surfaces.
- `#IUCN-unavailable`: historical 2/3. The Maned Rat occurrence was removed
  after the official page and assessment PDF were found under *L. imhausi*.
- `#assessment-year-drift`: 1/2. No new assessment/publication date conflation
  occurred; only the confirmed 2016 record year is public.
- `#species-identity-drift`: 1/3 after the prior threshold improvement and
  counter reset. The user explicitly accepted the Japanese visual; the English
  companion passed identity review on first generation.
- `#source-canvas-drift`: 0/2 after the architecture correction and counter
  reset. Every generated or edited source passed the immediate direct gate.
- `#topic-alias-duplication`: 0/2 after threshold improvement and counter reset.
  IUCN evidence checks now require taxonomy-source synonyms and incorrect
  subsequent spellings plus English common-name aliases before an unavailable
  conclusion.

## Next Concrete Change

- Begin the next run with scientific-name-first duplicate screening and reject
  both accepted names and historical assessment spellings.
- Recalculate the latest-eight rotation; prefer Australia/Oceania and avoid a
  consecutive African topic when a credible evidence-ready alternative exists.
- Recheck the IUCN direct route under the accepted name, taxonomy-source
  synonyms, incorrect subsequent spellings, and English common-name aliases
  before retaining an access caveat; do not infer a field assessment date from
  a release citation.
- Keep the immediate direct-source gate before visual review, editing,
  referencing, companion generation, or normalization.
- When the user explicitly selects a source-gate-passing visual, synchronize a
  semantically equivalent punctuation choice across Copy Lock, X copy, ALT,
  prompts, and sidecars before generating the companion.
- Finish future automation runs at `completed, local-ready`; GitHub publishing
  remains a separate closeout.
