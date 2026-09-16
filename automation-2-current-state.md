# Automation 2 Current State

Updated: 2026-09-16T22:08:48+09:00

## Workflow

- Default workflow: Quality Run with complete Japanese and English posters and three illustrated observation cards.
- Pending evidence package: none.
- Active package: none.
- Unfinished visual gate: none.
- Latest package: `2026-09-16-pink-handfish`.
- Latest state: `completed, published`; package content commit `2a2c047` was pushed to `origin/master` and the remote ref was verified. Nothing was posted to X.
- Latest evidence: the user-supplied official IUCN PDF and matching page capture directly confirm record `T123376622A123424329`: *Brachiopsilus dianthus*, Global Endangered (EN) under B1ab(v)+2ab(v) ver 3.1, assessed 30 April 2018 and published in 2020.
- Latest visual result: both first-pass posters show one smooth pink-red adult walking over a cool deep rocky reef with two attached broad pectoral fins and exactly three numbered illustrated cards.
- Retired package: `2026-08-21-montseny-brook-newt` is an exact duplicate of `2026-06-26-montseny-brook-newt`; do not post it.

## Latest Completed Package

- Package: `2026-09-16-pink-handfish`.
- Topic: Pink Handfish / ピンクハンドフィッシュ / *Brachiopsilus dianthus*.
- Region: southern Tasmania / Oceania.
- Editorial classification group: Fishes.
- State: `completed, published`.
- Selected Japanese source: `brachiopsilus_dianthus_japanese_imagegen_2026-09-16.png`; first generation accepted without retry.
- Selected English source: `brachiopsilus_dianthus_english_imagegen_2026-09-16.png`; first companion generation accepted without retry.
- Visual scope: one dominant adult in a frontal three-quarter bottom-walk; three cards cover the 22-year record gap and deep rediscovery, one attached walking pectoral fin and non-drifting hatchlings settled near substrate eggs.
- Artifacts: four canonical 1024x1536 PNGs, two primary X posting sets and eight synchronized sidecars. Full-size and phone-size review, direct-source, X-format, package, pixel-identity and whitespace checks pass.
- Naming caveat: ピンクハンドフィッシュ is a transparent Japanese rendering, not a claimed standardized Japanese national-list name.
- Evidence confirmation: the official ten-page IUCN assessment PDF and matching species-page capture are preserved with verified hashes. They retire the earlier dynamic-page access caveat without changing public copy or art. No population total is used.

## Recent-Eight Completed Region Rotation

1. 2026-09-09 — Africa and the western Indian Ocean — Seychelles Sheath-tailed Bat
2. 2026-09-10 — Oceania — Canterbury Knobbled Weevil
3. 2026-09-11 — Oceania — Barbie Pagoda
4. 2026-09-12 — Africa — Wood's Cycad
5. 2026-09-13 — Southeast Asia — Negros Bleeding-heart
6. 2026-09-14 — East Africa — Nguru Spiny Pygmy Chameleon
7. 2026-09-15 — Oceania — Kauaʻi Cave Wolf Spider
8. 2026-09-16 — Oceania — Pink Handfish

Oceania four; Africa and East Africa three combined; Southeast Asia one.

## Recent-Eight Completed Classification Rotation

1. 2026-09-09 — Mammals — Seychelles Sheath-tailed Bat
2. 2026-09-10 — Insects — Canterbury Knobbled Weevil
3. 2026-09-11 — Fungi and lichens — Barbie Pagoda
4. 2026-09-12 — Plants — Wood's Cycad
5. 2026-09-13 — Birds — Negros Bleeding-heart
6. 2026-09-14 — Reptiles — Nguru Spiny Pygmy Chameleon
7. 2026-09-15 — Other invertebrates — Kauaʻi Cave Wolf Spider
8. 2026-09-16 — Fishes — Pink Handfish

Mammals, Insects, Fungi and lichens, Plants, Birds, Reptiles, Other invertebrates and Fishes occupy one slot each. Amphibians are absent. Rotation remains only a tie-breaker after duplicate, unfamiliarity, discovery, evidence, naming and visual-viability screening.

## Daily Quality Loop

- User-supplied official IUCN evidence directly confirmed the already-locked status, criteria, assessment date, publication year and scope; the earlier dynamic-page access caveat was removed from current package records.
- Both first-pass posters passed without a retry, so no visual or typography drift required correction.
- This run creates no new unresolved carryover and no policy change.

## Next Concrete Change

- Preserve the Pink Handfish package as `completed, published`; content commit `2a2c047` is verified on `origin/master`. X posting remains separate and was not performed.
- Use `x-post-ja.md` / `x-post-en.md` as the primary posting sets; sidecars are synchronized backups.
- Preserve the 2018 assessment year rather than the 2020 publication year and keep Tasmania's state listing separate from the global IUCN footer.
- The next new package should recalculate both latest-eight rotations; Amphibians are currently absent, but rotation remains only a tie-breaker.
- Production rules remain centralized in `automation-2-production-policy.md`; historical logs do not supply active visual instructions.
