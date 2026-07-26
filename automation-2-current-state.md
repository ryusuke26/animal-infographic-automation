# Automation 2 Current State

Updated: 2026-07-26T21:28:57+09:00

This file is the small replace-in-place state record for Automation
`automation-2`. Run history remains in automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English
  Image Gen posters, species-specific illustrated observation cards, and an
  editorial review of X copy.
- Fast Run base/composer packages remain supported for existing artifacts, but
  deterministic composition is no longer the default or a completion
  substitute for a new package.
- New-topic behavior: verify official evidence directly and continue without a
  user evidence stop. Request a screenshot or PDF only when the official route
  remains unavailable, ambiguous, or conflicting.
- Pending evidence package: none.
- Active package: none.
- Evidence route: user-supplied official IUCN species-page screenshot and
  matching nine-page assessment PDF for `e.T22679182A264164432`, Tokyo
  Zoological Park Society, and Baral 2022.
- Confirmed: accepted taxon *Lophophorus impejanus*, established Japanese name
  ニジキジ, Global Least Concern (LC) in 2024, Himalayan high-country habitat,
  adult-male visual identity, and seasonal elevational movement.
- Phase 0 preflight: passed on 2026-07-26 in the no-approval local automation
  path.
- Himalayan Monal Quality Run remake: completed from Phase 3 on 2026-07-26.
  Evidence Lock and the three observation facts were reused unchanged; X main
  posts were rewritten as species-specific discovery scenes.
- Live Automation prompt sync: completed on 2026-07-26 with the Quality Run
  prompt. `ACTIVE`, the daily 10:00 schedule, model, reasoning effort,
  execution environment, and project target remained unchanged.

## Latest Package

- Latest completed package: `2026-07-26-himalayan-monal`.
- State: `completed, published`.
- Production: separate complete Japanese and English ImageGen posters. The
  first Japanese poster was retained as rejected after duplicated observation
  copy; one targeted retry passed. The English companion passed on its first
  generation. Previous Fast Run posters remain under `old_fast_run` names.
- Official evidence correction: screenshot/PDF preserved in the package;
  obsolete direct-record access caveats removed from source notes.
- GitHub closeout: package commit `bc0bdd5` and Quality Run workflow commit
  `fffeaea` published to `origin/master`; the published-state metadata commit
  and remote master ref were verified during closeout.

## Recent-Eight Region Rotation

1. 2026-07-19 — Africa — Water Chevrotain
2. 2026-07-20 — Central America/Caribbean — Cuban Gar
3. 2026-07-21 — Australia/Oceania — Numbat
4. 2026-07-22 — North America — Pinyon Jay
5. 2026-07-23 — Europe — Alpine Salamander
6. 2026-07-24 — South America — *Lysurus fossatii*
7. 2026-07-25 — Ocean/Global — Pelican Eel
8. 2026-07-26 — Asia — Himalayan Monal

Previous completed region: Asia.

## Verified Workspace Runtime

- Bundled Python:
  `C:\Users\ryusu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`
- Last verification: bundled runtime loaded on 2026-07-26. The completed
  Himalayan Monal package was remade in Quality Run. Pre-image Copy Lock,
  separate direct-poster visual QA, pixel equality, X/sidecar checks, and full
  package QA passed.

## Daily Quality Loop Counters

- `#image-text-error`: 1/3. The first Japanese Quality Run poster duplicated two
  observation sentences above the cards; one targeted retry removed them.
- `#IUCN-unavailable`: historical 1/3; the latest affected package was corrected
  with user-supplied official evidence.
- `#workflow-friction` for the WindowsApps PowerShell launch failure: 0/3 after
  the approval-aware retry path succeeded on 2026-07-25; `counter_reset: yes`.
- `#species-identity-drift`: 1/3 after the first Japanese Pelican Eel poster
  hid the diagnostic tail tip; resolved by one targeted retry.
- `#layout-overcrowded`: 1/2 after the first Himalayan Monal composition hid
  the crest beneath the title panel; resolved by one targeted composition edit
  plus the opt-in lower-card layout.
- `#generic-production-drift`: reset after one architecture-level correction on
  2026-07-26. Fast Run made the poster and X copy mechanically consistent but
  visibly generic; the default was restored to complete direct Image Gen
  posters and narrative posting copy.

## Next Concrete Change

- On the next new-topic run, begin with the one-batch Quality Run preflight and
  favor Africa if evidence viability and topic variety are comparable.
- Generate the complete Japanese poster first, visually accept it, then create
  the English companion from the same art direction. Do not use the deterministic
  composer as the default public asset.
- Write each X main post as a species-specific discovery scene rather than a
  transcription of the three observation cards.
