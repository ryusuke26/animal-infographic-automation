# Automation 2 Current State

Updated: 2026-07-25T13:59:04+09:00

This file is the small replace-in-place state record for Automation
`automation-2`. Run history remains in automation memory.

## Workflow

- Default workflow: Fast Run with one text-free base illustration and
  deterministic Japanese/English poster composition.
- New-topic behavior: verify official evidence directly and continue without a
  user evidence stop. Request a screenshot or PDF only when the official route
  remains unavailable, ambiguous, or conflicting.
- Pending evidence package: none.
- Active package: none.
- Evidence received: official IUCN species-page screenshot and matching
  assessment PDF for `e.T18227119A42691734`.
- Confirmed across the two files: accepted taxon, Least Concern (LC), Global
  scope, year published 2015, date assessed 24 May 2012, and citation.
- User IUCN Evidence Gate: satisfied by the complete screenshot and matching
  official PDF.
- Phase 0 preflight: passed on 2026-07-25 in an approval-enabled normal
  conversation after the bounded approved read-only retry.
- Live Automation prompt sync: completed on 2026-07-25 with the Fast Run
  prompt. `ACTIVE`, the daily 10:00 schedule, model, reasoning effort,
  execution environment, and project target remained unchanged.

## Latest Package

- Latest completed package: `2026-07-25-pelican-eel`.
- State: `completed, local-ready`.
- GitHub closeout: not started; publishing remains a separate
  approval-enabled handoff.

## Recent-Eight Region Rotation

1. 2026-07-18 — South America — Darwin's Frog
2. 2026-07-19 — Africa — Water Chevrotain
3. 2026-07-20 — Central America/Caribbean — Cuban Gar
4. 2026-07-21 — Australia/Oceania — Numbat
5. 2026-07-22 — North America — Pinyon Jay
6. 2026-07-23 — Europe — Alpine Salamander
7. 2026-07-24 — South America — *Lysurus fossatii*
8. 2026-07-25 — Ocean/Global — Pelican Eel

Previous completed region: Ocean/Global.

## Verified Workspace Runtime

- Bundled Python:
  `C:\Users\ryusu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`
- Last verification: Python 3.12.13 and Pillow 12.2.0. Fast Run pre-visual/full
  package QA, two legacy-package regression checks, deterministic Japanese
  `1024x1536` composition, prompt synchronization, and whitespace checks passed
  on 2026-07-25.

## Daily Quality Loop Counters

- `#image-text-error`: 0/3 after the pre-image Copy Lock validator improvement;
  `counter_reset: yes`.
- `#IUCN-unavailable`: historical 1/3; the latest affected package was corrected
  with user-supplied official evidence.
- `#workflow-friction` for the WindowsApps PowerShell launch failure: 0/3 after
  the approval-aware retry path succeeded on 2026-07-25; `counter_reset: yes`.
- `#species-identity-drift`: 1/3 after the first Japanese Pelican Eel poster
  hid the diagnostic tail tip; resolved by one targeted retry.

## Next Concrete Change

- On the next new-topic run, begin with the one-batch Fast Run preflight and
  favor Asia if evidence viability and topic variety are comparable.
