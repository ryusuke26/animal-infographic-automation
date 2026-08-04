# Automation 2 Current State

Updated: 2026-08-04T15:39:28+09:00

This file is the small replace-in-place state record for Automation
`automation-2`. Run history remains in automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English
  Image Gen posters, species-specific illustrated observation cards, and an
  editorial review of X copy.
- Fast Run base/composer packages remain supported for existing artifacts, but
  deterministic composition is not the default or a completion substitute.
- Pending evidence package: none.
- Active package: none.
- Phase 0 preflight: passed on 2026-08-04 in the no-approval local automation
  path. Unrelated untracked `scripts/__pycache__/` and `tmp/` were preserved.
- Duplicate screening: *Arctonyx collaris*, Greater Hog Badger, and
  ブタバナアナグマ were searched across memory, INDEX, package folders, and
  package contents before Evidence Lock; no completed or held-topic collision
  was found.

## Latest Package

- Latest package: `2026-08-04-greater-hog-badger`.
- State: `completed, published`.
- Region: Asia.
- Workflow mode: Quality Run with direct official IUCN evidence.
- Evidence route: the official IUCN 2024 amended global assessment and species
  record screenshot directly confirm Vulnerable (VU), criteria A2cd+3cd+4cd,
  assessed 3 March 2015. The original assessment was published in 2016; the
  2024 amendment changes only one assessor's initials.
- Confirmed: *Arctonyx collaris*, Greater Hog Badger / ブタバナアナグマ,
  Global VU, assessed 2015, originally published 2016 and amended 2024;
  mainland Asian
  forest range, pig-like snout, two dark facial stripes, pale claws, and
  soil-raking food search.
- Visual QA: passed at full and phone size. Both posters show one stable
  full-body hero with four separate limb origins, paths, and paw endpoints,
  one connected short tail, a long pig-like snout, two facial stripes, and
  exactly three unequal numbered illustrated cards.
- Text QA: the first Japanese title-glyph error and first English footer-space
  error were each corrected with the language's one allowed targeted retry.
  The two superseded first generations were moved to the Windows Recycle Bin
  on 2026-08-04; only the four canonical PNGs remain in the package.
- Mechanical QA: both direct-source gates, normalization, X format validation,
  full package validation, exact `1024x1536` dimensions, within-language pixel
  identity, sidecar synchronization, and whitespace checks passed.
- GitHub publishing: package content pushed directly to `origin/master` in
  commit `2e664ca`; published-state metadata is recorded in the follow-up
  closeout commit.

## Recent-Eight Region Rotation

1. 2026-07-28 — Australia/Oceania — Kea
2. 2026-07-29 — Central America/Caribbean — Pygmy Three-toed Sloth
3. 2026-07-30 — Africa — Red River Hog
4. 2026-07-31 — North America — Ringtail
5. 2026-08-01 — Europe — Russian Desman
6. 2026-08-02 — South America — Pacarana
7. 2026-08-03 — Antarctica / Southern Ocean — Antarctic Fur Seal
8. 2026-08-04 — Asia — Greater Hog Badger

Previous completed region: Asia. All eight recent regions are currently unique.

## Verified Workspace Runtime

- Bundled Python:
  `C:\Users\ryusu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`
- Last verification: workspace dependencies loaded on 2026-08-04. Both
  canonical direct posters passed the exact-2:3/full-canvas source gate; both
  posting PNGs are `1024x1536` and pixel-identical to their language source.

## Daily Quality Loop Counters

- `#image-text-error`: 2/3 after the prior threshold improvement and counter
  reset. The current title-glyph occurrence is tracked separately because it
  is not the same material cause as prior extra-card-copy drift.
- `#verbatim-glyph-drift`: 1/3. The first Japanese Greater Hog Badger poster
  substituted one title glyph; the targeted correction restored the exact
  title without changing the accepted art.
- `#IUCN-unavailable`: historical 2/3. The current package now has the directly
  inspected official global assessment PDF and species-record screenshot, so
  no current unavailable-route occurrence is counted.
- `#assessment-year-drift`: 1/2. The current package now records the 2015
  field-level assessment separately from the 2016 original publication and
  2024 amendment, so no new drift is counted.
- `#species-identity-drift`: 1/3 after the prior threshold improvement and
  counter reset. No new anatomy or identity drift occurred in this package.
- `#source-canvas-drift`: 0/2 after the architecture correction and counter
  reset. All four initial/retry sources in this run passed the immediate gate.
- `#topic-alias-duplication`: 1/2. Scientific-name-first screening prevented a
  duplicate in this run.

## Next Concrete Change

- Begin the next topic with accepted scientific-name duplicate screening, then
  search English and Japanese aliases.
- Recalculate the latest-eight rotation; avoid another consecutive Asian topic
  when a credible alternative exists, but do not turn rotation into a quota.
- For unfamiliar Japanese katakana titles, include character-by-character
  spelling in the first Image Gen prompt.
- Keep the immediate direct-source gate before visual review, editing,
  referencing, companion generation, or normalization.
- Keep stable natural poses with four visible limb origins, separate paths, and
  separate endpoints; show difficult movement with one complete small animal
  in a card rather than isolated anatomy.
- Keep the short main post separate from the fuller first-reply story, retain
  the English common-name hashtag in both languages, and disclose any official
  evidence-route caveat in the source/context reply.
- Finish future automation runs at `completed, local-ready`; GitHub publishing
  remains a separate closeout.
