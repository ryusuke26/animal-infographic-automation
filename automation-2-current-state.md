# Automation 2 Current State

Updated: 2026-09-26T19:08:17+09:00

## Workflow

- Default workflow: Quality Run with complete Japanese and English posters and three illustrated observation cards.
- Required art direction: crayon / oil-pastel observation sketch with adult editorial direction, checked against `generated_infographics/purple_frog_ja_2026-04-28.png` for texture and warmth only.
- Pending evidence package: none.
- Active package: none.
- Unfinished visual gate: none.
- Latest package: `2026-09-26-sunbittern`.
- Latest state: `completed, published`; content commit `3ef59e8` was pushed to `origin/master` and verified remotely. Nothing was posted to X.
- Latest evidence: current IUCN record `T22691893A163625651` confirms *Eurypyga helias*, Global Least Concern (LC), last assessed 4 December 2019; the public footer uses assessment year 2019.
- Latest visual result: both first-pass posters show one adult Sunbittern with attached display wings and tail, red eye and striped head, and three explanatory illustrated cards in the required crayon/oil-pastel medium. Full-size and phone-size reviews passed; card 3 shows the parent with chicks but no predator scene.
- Retired package: `2026-08-21-montseny-brook-newt` is an exact duplicate of `2026-06-26-montseny-brook-newt`; do not post it.

## Latest Completed Package

- Package: `2026-09-26-sunbittern`.
- Topic: Sunbittern / ジャノメドリ / *Eurypyga helias*.
- Region: tropical Central and South America / Americas.
- Editorial classification group: Birds.
- State: `completed, published`.
- Selected Japanese source: `sunbittern_japanese_imagegen_2026-09-26.png`; first attempt accepted.
- Selected English source: `sunbittern_english_imagegen_2026-09-26.png`; first attempt accepted with the Wuppertal exact-taxon photograph and Japanese composition reference.
- Visual scope: one adult streamside display bird with a compact barred body, striped head and red eye, long pointed bill and legs, and connected wings and tail showing chestnut-orange, black and pale eye-like patches. Three cards explain the display, shallow-water hunting and nest-defense context.
- Artifacts: four canonical 1024x1536 PNGs, two primary X posting sets and eight synchronized sidecars. Direct-source and full package validators, copy checks, full-size and phone-size visual review pass. English card copy is compact but readable at phone size.
- Evidence caveat: the card 3 illustration shows the parent and chicks at the nest without depicting a predator; its text states the supported diversion behavior. Status is Global LC last assessed 2019, not 2020 (the citation year). No population total is used.

## Recent-Eight Completed Region Rotation

1. 2026-09-19 — Caribbean — Cuban Greater Funnel-eared Bat
2. 2026-09-20 — East Asia — Black-faced Spoonbill
3. 2026-09-21 — Oceania — Queen Alexandra's Birdwing
4. 2026-09-22 — North America — Sunflower Sea Star
5. 2026-09-23 — Southern Africa — Geometric Tortoise
6. 2026-09-24 — Western Indian Ocean — Madagascar Laceleaf
7. 2026-09-25 — Oceania — Leafy Seadragon
8. 2026-09-26 — Tropical Central and South America — Sunbittern

Oceania occupies two slots. Caribbean, East Asia, North America, Southern Africa, the western Indian Ocean and tropical Central and South America each occupy one slot.

## Recent-Eight Completed Classification Rotation

1. 2026-09-19 — Mammals — Cuban Greater Funnel-eared Bat
2. 2026-09-20 — Birds — Black-faced Spoonbill
3. 2026-09-21 — Insects — Queen Alexandra's Birdwing
4. 2026-09-22 — Other invertebrates — Sunflower Sea Star
5. 2026-09-23 — Reptiles — Geometric Tortoise
6. 2026-09-24 — Plants — Madagascar Laceleaf
7. 2026-09-25 — Fishes — Leafy Seadragon
8. 2026-09-26 — Birds — Sunbittern

Birds occupy two slots. Mammals, Fishes, Insects, Other invertebrates, Reptiles and Plants occupy one each. Amphibians and Fungi and lichens are absent. Apply the production policy's Topic diversity design: within-group variety, body forms, habitats and discovery hooks actively inform selection among viable candidates. Familiar species with a less familiar supported aspect are eligible; there are no fixed quotas or cooldowns.

## Daily Quality Loop

- Issue: the pre-image validator caught a syntax mismatch in both prompt text blocks before art; corrected the heading and nine quote-per-line strings, then passed before generation.
- Resolution: no unresolved production carryover or policy change remains; both first-pass posters passed identity, copy, cards, crayon/oil-pastel style and phone-size review.

## Next Concrete Change

- Preserve the Sunbittern package as `completed, published`; GitHub publication is complete and X publication remains separate and was not performed.
- Use `x-post-ja.md` / `x-post-en.md` as the primary posting sets; sidecars are synchronized backups.
- Preserve the Global LC 2019 assessment-year footer and retain the card-3 no-predator visual note in the package QA record.
- The next new package should recalculate latest-eight summaries and scan the latest twenty for subgroup, visual and story repetition. Broaden the initial slate and consider familiar species too under Topic diversity; absence from a group is context, not a quota.
- Production rules remain centralized in `automation-2-production-policy.md`; historical logs do not supply active visual instructions.
