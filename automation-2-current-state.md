# Automation 2 Current State

Updated: 2026-09-27T21:41:30+09:00

## Workflow

- Default workflow: Quality Run with complete Japanese and English posters and three illustrated observation cards.
- Required art direction: crayon / oil-pastel observation sketch with adult editorial direction, checked against `generated_infographics/purple_frog_ja_2026-04-28.png` for texture and warmth only.
- Pending evidence package: none.
- Active package: none.
- Unfinished visual gate: none.
- Latest package: `2026-09-27-axolotl`.
- Latest state: `completed, published`; content commit `951b55b05b107a2f6764f5853c7b46cf4a90af16` was pushed to `origin/master` and verified remotely. Nothing was posted to X.
- Latest evidence: matching formal IUCN record `T1095A53947343` confirms *Ambystoma mexicanum*, Global Critically Endangered (CR), assessed 23 October 2019 and published 2020; the live IUCN page did not render, so the matching formal assessment text and DOI were checked.
- Latest visual result: one dark mottled wild-type adult with attached external gills, coherent limbs and tail, plus three illustrated explanatory cards in the required crayon/oil-pastel medium. The Japanese card-3 first attempt was rejected for detached limb pieces; a single retry passed full-image review. The English first attempt passed. Full-size and phone-size reviews passed.
- Retired package: `2026-08-21-montseny-brook-newt` is an exact duplicate of `2026-06-26-montseny-brook-newt`; do not post it.

## Latest Completed Package

- Package: `2026-09-27-axolotl`.
- Topic: Axolotl / メキシコサンショウウオ / *Ambystoma mexicanum*.
- Region: Valley of Mexico / North America.
- Editorial classification group: Amphibians.
- State: `completed, published`.
- Selected Japanese source: `axolotl_japanese_imagegen_2026-09-27.png`; selected retry prompt `image-prompt-ja-retry.md`.
- Selected English source: `axolotl_english_imagegen_2026-09-27.png`; first attempt with accepted Japanese composition reference.
- Visual scope: wild-type dark mottled aquatic adult, broad head, attached feathery gills, coherent limbs and finned tail. Three cards explain wild/captive color contrast, adult gills and limb regeneration.
- Artifacts: four canonical 1024x1536 PNGs, two primary X posting sets and eight synchronized sidecars. Direct-source and full package validators, copy checks, full-size and phone-size visual review pass.
- Evidence caveat: IUCN live dynamic page did not render; matching formal assessment text and DOI confirm Global CR assessed 2019 and published 2020. The Japanese retry changed fine pixels across the canvas, so the entire selected source was reviewed again rather than treated as a local pixel patch.

## Recent-Eight Completed Region Rotation

1. 2026-09-20 — East Asia — Black-faced Spoonbill
2. 2026-09-21 — Oceania — Queen Alexandra's Birdwing
3. 2026-09-22 — North America — Sunflower Sea Star
4. 2026-09-23 — Southern Africa — Geometric Tortoise
5. 2026-09-24 — Western Indian Ocean — Madagascar Laceleaf
6. 2026-09-25 — Oceania — Leafy Seadragon
7. 2026-09-26 — Tropical Central and South America — Sunbittern
8. 2026-09-27 — North America — Axolotl

Oceania and North America occupy two slots each. East Asia, Southern Africa, the western Indian Ocean and tropical Central and South America each occupy one slot.

## Recent-Eight Completed Classification Rotation

1. 2026-09-20 — Birds — Black-faced Spoonbill
2. 2026-09-21 — Insects — Queen Alexandra's Birdwing
3. 2026-09-22 — Other invertebrates — Sunflower Sea Star
4. 2026-09-23 — Reptiles — Geometric Tortoise
5. 2026-09-24 — Plants — Madagascar Laceleaf
6. 2026-09-25 — Fishes — Leafy Seadragon
7. 2026-09-26 — Birds — Sunbittern
8. 2026-09-27 — Amphibians — Axolotl

Birds occupy two slots. Amphibians, Fishes, Insects, Other invertebrates, Reptiles and Plants occupy one each. Mammals and Fungi and lichens are absent. Apply the production policy's Topic diversity design without quotas or cooldowns.

## Daily Quality Loop

- Issue: the first Japanese card-3 image used detached limb pieces; a targeted Image Gen retry corrected the explanation but altered fine pixels across the whole image.
- Resolution: one retry was used, the complete selected Japanese image was re-reviewed, and no unresolved visual or evidence carryover remains.

## Next Concrete Change

- Preserve the Axolotl package as `completed, published`; X publication remains separate.
- Use `x-post-ja.md` / `x-post-en.md` as the primary posting sets; sidecars are synchronized backups.
- Japanese main posts must keep `#世界の知らない生き物` alongside the English common-name tag; the 26 and 27 September posting sets and caption sidecars were corrected and included in the GitHub closeout after the user flagged the omission.
- Next run should recalculate latest-eight summaries and scan the latest twenty for within-group, body-form, habitat and discovery-hook repetition.
- For any requested local image edit, verify the whole returned canvas after the one retry even when the request was bounded to a card.
