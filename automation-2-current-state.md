# Automation 2 Current State

Updated: 2026-07-24T13:19:49+09:00

This file is the small replace-in-place state record for Automation
`automation-2`. Run history remains in automation memory.

## Workflow

- User IUCN Evidence Gate: enabled in canonical policy and prompt.
- New-topic behavior: stop after Topic Lock as `awaiting-user-iucn-evidence`;
  resume the same package after the user supplies the official IUCN page
  screenshot and matching assessment PDF.
- Pending evidence package: none.
- Live Automation prompt sync: completed on 2026-07-24. The guarded sync
  changed only `prompt` and `updated_at`; `ACTIVE`, the daily 10:00 schedule,
  model, execution environment, project target, and working directory remained
  unchanged.

## Latest Package

- Latest completed package: `2026-07-24-lysurus-fossatii`.
- State: `completed, published`.
- GitHub closeout: completed. Package commit `a336e1f` and workflow commit
  `2fc7007` reached `origin/master` before the published-state metadata update;
  the final remote ref is recorded in automation memory after push.

## Recent-Eight Region Rotation

1. 2026-07-17 — Asia — Titan Arum
2. 2026-07-18 — South America — Darwin's Frog
3. 2026-07-19 — Africa — Water Chevrotain
4. 2026-07-20 — Central America/Caribbean — Cuban Gar
5. 2026-07-21 — Australia/Oceania — Numbat
6. 2026-07-22 — North America — Pinyon Jay
7. 2026-07-23 — Europe — Alpine Salamander
8. 2026-07-24 — South America — *Lysurus fossatii*

Previous completed region: South America.

## Verified Workspace Runtime

- Bundled Python:
  `C:\Users\ryusu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`
- Last verification: Python 3.12.13; Pillow 12.2.0; package-validator
  `--help`, pre-image QA, and full package QA passed on 2026-07-24.

## Daily Quality Loop Counters

- `#image-text-error`: 0/3 after the pre-image Copy Lock validator improvement;
  `counter_reset: yes`.
- `#IUCN-unavailable`: historical 1/3; the latest affected package was corrected
  with user-supplied official evidence.

## Next Concrete Change

- On the next new-topic run, verify that the Automation creates the provisional
  package, records `awaiting-user-iucn-evidence`, and stops with the two-file
  evidence request before Evidence Lock.
