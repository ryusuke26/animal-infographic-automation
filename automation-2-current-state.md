# Automation 2 Current State

Updated: 2026-08-17T00:16:54+09:00

This file is the small replace-in-place state record for Automation `automation-2`. Run history remains in Automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English Image Gen posters, species-specific illustrated observation cards, and an editorial review of X copy.
- Pending evidence package: none.
- Active package: none.
- Retired package: none.
- The canonical package write gate is available.

## Latest Completed Package

- Package: `2026-08-16-jellyfish-tree`.
- Topic: Jellyfish Tree / ジェリーフィッシュ・ツリー / *Medusagyne oppositifolia*.
- State: `completed, published`.
- Region: Mahé, Seychelles / Africa.
- Editorial classification group: Plants.
- Evidence: the preserved official IUCN assessment PDF and matching Red List page capture directly confirm Global Critically Endangered (CR) under C2a(ii), assessed 12 August 2025 and published in 2025 as record `e.T37781A262047825`. Public footers use assessment year 2025; the superseded fallback record `37781/10072208` and 2007 footer are retained only as audit history.
- Locked discovery: one small tree on exposed Mahé granite, thick opposite leaves, and a many-parted opened fruit whose valves radiate from a central column like umbrella ribs. Public copy does not assert whether the English name refers to flower or fruit because Kew and SPGA differ.
- Visual resolution: the accepted bilingual artwork was preserved. Deterministic localized text-safe repairs changed only the footer year digits from 2007 to 2025: Japanese `(512,1449)-(560,1492)` and English `(442,1462)-(482,1498)`. Four superseded 2007-footer canonical PNGs remain under package evidence. At the user's request, the two explicitly rejected English audit sources were moved to the Windows Recycle Bin; only the four canonical PNGs remain in `images/`.
- Artifacts and QA: two official evidence files, four corrected canonical `1024x1536` PNGs, eight synchronized sidecars, Copy Lock, prompts, README, Sources QA, and INDEX are synchronized. Direct-source, X-format, package, phone/full-size, pixel-identity, stale-footer, and whitespace QA pass. Package content commit `2c9633d` was pushed directly to `origin/master` and remotely verified.

## Recent-Eight Completed Region Rotation

1. 2026-08-09 — Western Madagascar / Africa — Madagascan Big-headed Turtle
2. 2026-08-10 — Northern Colombia / South America — Blue-billed Curassow
3. 2026-08-11 — Central and southern Japan / Asia — Itasenpara Bitterling
4. 2026-08-12 — Table Mountain, South Africa / Africa — Table Mountain Ghost Frog
5. 2026-08-13 — East Asia / Asia — Bekko Tombo
6. 2026-08-14 — Southern Tanzania / Africa — Kipunji
7. 2026-08-15 — Southeastern Australia and New Zealand South Island / Oceania — Tea-tree Fingers
8. 2026-08-16 — Mahé, Seychelles / Africa — Jellyfish Tree

Africa occupies four of the latest eight; Asia occupies two; South America and Oceania occupy one each.

## Recent-Eight Completed Classification Rotation

1. 2026-08-09 — Reptiles — Madagascan Big-headed Turtle
2. 2026-08-10 — Birds — Blue-billed Curassow
3. 2026-08-11 — Fishes — Itasenpara Bitterling
4. 2026-08-12 — Amphibians — Table Mountain Ghost Frog
5. 2026-08-13 — Insects — Bekko Tombo
6. 2026-08-14 — Mammals — Kipunji
7. 2026-08-15 — Fungi and lichens — Tea-tree Fingers
8. 2026-08-16 — Plants — Jellyfish Tree

Reptiles, Birds, Fishes, Amphibians, Insects, Mammals, Fungi and lichens, and Plants each occupy one slot; Other invertebrates is absent.

## Daily Quality Loop Counters

- `#old-status-risk`: 1 occurrence, fixed now. Stronger official evidence superseded a fallback 2007 footer after local-ready closeout; all public, evidence, image, sidecar, INDEX, and state surfaces now use the 2025 assessment.
- `#assessment-year-drift`: policy improvement remains active. The public footer uses the directly inspected assessment year; publication year stays source context even though both are 2025 here.
- `#species-identity-drift`: reset after the Tea-tree Fingers growth-form improvement; no identity or anatomy pixels changed in this evidence correction.
- `#source-canvas-drift`: 0/2. Both corrected direct posters remain exact 2:3 full-canvas sources.

## Next Concrete Change

- Jellyfish Tree is finished at `completed, published`; preserve the accepted artwork and corrected 2025 footer.
- On the next automation run, perform Phase 0 preflight and select a new topic only if no unfinished package has appeared. Other invertebrates is absent from the latest eight, but rotation remains a tie-breaker after unfamiliarity, evidence, naming, and visual viability.
- Package content commit `2c9633d` was published directly to `origin/master`; this closeout synchronizes published-state metadata and completes the final remote-ref verification.
