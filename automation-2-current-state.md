# Automation 2 Current State

Updated: 2026-09-14T21:45:46+09:00

## Workflow

- Default workflow: Quality Run with complete Japanese and English posters and three illustrated observation cards.
- Pending evidence package: none.
- Active package: none.
- Unfinished visual gate: none.
- Latest package: `2026-09-14-nguru-spiny-pygmy-chameleon`.
- Latest state: `completed, published`; package content commit `c6f3c8fb91f9778592cca8510f8adcfeda1c2297` was pushed to `origin/master` and its remote ref was verified before this state change. Nothing was posted to X.
- Latest evidence: the directly inspected current IUCN record `T172524A1344202` confirms Global Critically Endangered (CR) under B1ab(iii,v), assessed 21 August 2013 and marked Needs updating. ITIS, Redbond et al. 2021, the original description and Tiergarten Schonbrunn support identity, mature-male rostral shape, pointed scales and low-forest crepuscular activity.
- Latest visual result: both posters show one tiny green-brown adult male walking along a mossy twig with a broad downward rostral process, pointed head-to-back outline, four coherent grasping limbs, one tapered tail and exactly three numbered illustrated cards.
- Retired package: `2026-08-21-montseny-brook-newt` is an exact duplicate of `2026-06-26-montseny-brook-newt`; do not post it.

## Latest Completed Package

- Package: `2026-09-14-nguru-spiny-pygmy-chameleon`.
- Topic: Nguru Spiny Pygmy Chameleon / ヌグルコノハカメレオン / *Rhampholeon acuminatus*.
- Region: Nguru Mountains, Tanzania / East Africa.
- Editorial classification group: Reptiles.
- State: `completed, published`.
- Selected Japanese source: `rhampholeon_acuminatus_japanese_imagegen_2026-09-14.png`; one targeted text-only retry removed an invalid extra title line.
- Selected English source: `rhampholeon_acuminatus_english_imagegen_2026-09-14.png`; first companion generation, no retry.
- Visual scope: one adult male in a stable twig-walking pose; three cards cover the pointed body outline, mature male/female rostral comparison and low-forest dawn/dusk activity.
- Artifacts: four canonical 1024x1536 PNGs, two primary X posting sets and eight synchronized sidecars. Full-size and phone-size review, direct-source, X-format, package, pixel-identity and whitespace checks pass.
- Rejected-image cleanup: the invalid-title Japanese first attempt and its hash-identical Image Gen cache source were moved to the Windows Recycle Bin on user request; all four canonical PNGs and both exact-taxon evidence photographs remain.
- Naming caveat: ヌグルコノハカメレオン is a published specialist rendering, not a claimed standardized national-list name.
- Evidence caveat: public status wording uses the 2013 IUCN assessment year; the current record is marked Needs updating and no population number is used.

## Recent-Eight Completed Region Rotation

1. 2026-09-07 — Western Asia — Acigöl Killifish
2. 2026-09-08 — Europe — Sardinian Brook Salamander
3. 2026-09-09 — Africa and the western Indian Ocean — Seychelles Sheath-tailed Bat
4. 2026-09-10 — Oceania — Canterbury Knobbled Weevil
5. 2026-09-11 — Oceania — Barbie Pagoda
6. 2026-09-12 — Africa — Wood's Cycad
7. 2026-09-13 — Southeast Asia — Negros Bleeding-heart
8. 2026-09-14 — East Africa — Nguru Spiny Pygmy Chameleon

Africa three; Oceania two; Western Asia, Europe and Southeast Asia one each.

## Recent-Eight Completed Classification Rotation

1. 2026-09-07 — Fishes — Acigöl Killifish
2. 2026-09-08 — Amphibians — Sardinian Brook Salamander
3. 2026-09-09 — Mammals — Seychelles Sheath-tailed Bat
4. 2026-09-10 — Insects — Canterbury Knobbled Weevil
5. 2026-09-11 — Fungi and lichens — Barbie Pagoda
6. 2026-09-12 — Plants — Wood's Cycad
7. 2026-09-13 — Birds — Negros Bleeding-heart
8. 2026-09-14 — Reptiles — Nguru Spiny Pygmy Chameleon

Fishes, Amphibians, Mammals, Insects, Fungi and lichens, Plants, Birds and Reptiles occupy one slot each. Other invertebrates are absent. Rotation remains only a tie-breaker after duplicate, unfamiliarity, discovery, evidence, naming and visual-viability screening.

## Daily Quality Loop

- One visibly screened two-image Tiergarten Schonbrunn identity bundle took about 25 minutes despite both carousel targets being isolated before export.
- Both local copies were reused across languages; no second bundle was attempted. One Japanese text-only retry was used, while the English companion passed first time.
- This is the third `#workflow-friction` recurrence after the 2026-09-11 counter reset. The threshold is met; the existing one-bundle and first-usable-copy rules already represent the smallest safe deterministic bound, so a new policy rule would only duplicate them. The counter resets after this documented no-op resolution.
- Tomorrow: preserve the current cap, stop after the first usable local copies and treat slow external bundling as measured latency rather than a reason to relax identity evidence.

## Next Concrete Change

- Preserve the Nguru Spiny Pygmy Chameleon package as `completed, published`; GitHub closeout is complete, while X posting remains separate and requires explicit direction.
- Use `x-post-ja.md` / `x-post-en.md` as the primary posting sets; sidecars are synchronized backups.
- Preserve the Global CR 2013 wording, retain the Needs updating caveat in package records and do not add a population number to public copy.
- The next new package should recalculate both latest-eight rotations; Other invertebrates is currently absent, but rotation remains only a tie-breaker.
- Production rules remain centralized in `automation-2-production-policy.md`; historical logs do not supply active visual instructions.
