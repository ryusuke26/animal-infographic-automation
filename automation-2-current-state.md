# Automation 2 Current State

Updated: 2026-09-10T21:36:21+09:00

## Workflow

- Default workflow: Quality Run with complete Japanese and English posters and three illustrated observation cards.
- Pending evidence package: none.
- Active package: none.
- Unfinished visual gate: none.
- Latest package: `2026-09-10-canterbury-knobbled-weevil`.
- Latest state: `completed, published`; package content commit `e194fa928f22fe191524a62e45ba7a865511fad1` was pushed to `origin/master` and its remote ref was verified before this state change. Nothing was posted to X.
- Latest evidence: directly inspected current IUCN record `T39307A21424332`, Global CR under B1ab(v)+2ab(v), assessed 19 December 2013 and marked `Needs updating`; New Zealand DOC's 2024 record confirms a second population and supersedes the old one-location context for public interpretation.
- Latest visual result: both first-pass posters were accepted. One stout grey-brown weevil walks naturally on speargrass with a short down-curved rostrum, paired elbowed antennae, closed knobbled wing cases and coherent six-leg topology; exactly three illustrated cards carry the locked explanations.
- Retired package: `2026-08-21-montseny-brook-newt` is an exact duplicate of `2026-06-26-montseny-brook-newt`; do not post it.

## Latest Completed Package

- Package: `2026-09-10-canterbury-knobbled-weevil`.
- Topic: Canterbury Knobbled Weevil / カンタベリー・コブゾウムシ / *Hadramphus tuberculatus*.
- Region: Canterbury, South Island, Aotearoa New Zealand / Oceania.
- Editorial classification group: Insects.
- State: `completed, published`.
- Selected Japanese source: `canterbury_knobbled_weevil_japanese_imagegen_2026-09-10.png`; first generation, no retry.
- Selected English source: `canterbury_knobbled_weevil_english_imagegen_2026-09-10.png`; first companion generation from the accepted Japanese composition, no retry.
- Visual scope: one dominant adult on a diagonal speargrass blade; three cards cover the 1922-to-2004 rediscovery, adult-versus-larval speargrass feeding and the flightless knobbled form without another complete adult.
- Artifacts: four canonical 1024x1536 PNGs, two primary X posting sets and eight synchronized sidecars. Full-size and phone-size review, direct-source, X-format, package, pixel-identity and whitespace checks pass.
- Naming caveat: カンタベリー・コブゾウムシ is a transparent rendering of the official English name rather than a claimed standardized Japanese insect-list name.
- Status caveat: the 2013 IUCN assessment is marked `Needs updating`; its one-location and 138-mature-individual fields are excluded from public copy after DOC confirmed a second population in 2024.

## Recent-Eight Completed Region Rotation

1. 2026-09-03 — Africa and the western Indian Ocean — Café marron
2. 2026-09-04 — Oceania — Oʻahu Tree Snail
3. 2026-09-05 — Caribbean — Union Island Gecko
4. 2026-09-06 — South America — Blue-eyed Ground Dove
5. 2026-09-07 — Western Asia — Acigöl Killifish
6. 2026-09-08 — Europe — Sardinian Brook Salamander
7. 2026-09-09 — Africa and the western Indian Ocean — Seychelles Sheath-tailed Bat
8. 2026-09-10 — Oceania — Canterbury Knobbled Weevil

Africa two, Oceania two, Caribbean one, South America one, Western Asia one and Europe one.

## Recent-Eight Completed Classification Rotation

1. 2026-09-03 — Plants — Café marron
2. 2026-09-04 — Other invertebrates — Oʻahu Tree Snail
3. 2026-09-05 — Reptiles — Union Island Gecko
4. 2026-09-06 — Birds — Blue-eyed Ground Dove
5. 2026-09-07 — Fishes — Acigöl Killifish
6. 2026-09-08 — Amphibians — Sardinian Brook Salamander
7. 2026-09-09 — Mammals — Seychelles Sheath-tailed Bat
8. 2026-09-10 — Insects — Canterbury Knobbled Weevil

Each listed group occupies one slot; Fungi and lichens is absent. Rotation remains only a tie-breaker after duplicate, evidence and visual-viability screening.

## Daily Quality Loop

- The single-image DOC bundle took about three minutes and the two-image IUCN bundle about three and a half minutes.
- The first successful three-image role-distinct reference set was retained and reused for both languages; no further export or image retry was attempted.
- This is the second `#workflow-friction` recurrence after the 2026-09-08 counter reset, so the improvement threshold is not met.
- Tomorrow: when exact IUCN assets are already exposed, prefer one focused IUCN bundle and omit a lower-resolution duplicate source.

## Next Concrete Change

- Preserve the Canterbury Knobbled Weevil package as `completed, published`; GitHub closeout is complete, while X publication remains separate and requires explicit direction.
- Use `x-post-ja.md` / `x-post-en.md` as the primary posting sets; sidecars are synchronized backups.
- Preserve the 2013 IUCN `Needs updating` caveat and do not reintroduce its obsolete one-location or 138-mature-individual fields into public copy.
- The next new package should screen Fungi and lichens only as a tie-breaker after mission, evidence, naming and visual viability.
- Production rules remain centralized in `automation-2-production-policy.md`; historical logs do not supply active visual instructions.
