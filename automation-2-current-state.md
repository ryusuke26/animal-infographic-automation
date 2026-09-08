# Automation 2 Current State

Updated: 2026-09-08T22:44:22+09:00

This state supersedes the Research Reset and earlier premature acceptance.

## Workflow

- Default workflow: Quality Run with complete Japanese and English posters and three illustrated observation cards.
- Pending evidence package: none.
- Active package: `2026-09-08-sardinian-brook-salamander`.
- Unfinished visual gate: v4 anatomy and scale review after repeated user rejection.
- Latest package: `2026-09-08-sardinian-brook-salamander`.
- Latest state: `needs review, regenerated`; nothing has been posted or published.
- Latest evidence: directly inspected current IUCN record T8371A223758127, Global EN under B2ab(iii,iv), assessed 20 February 2023 and published in 2024; EAZA Amphibian TAG and four exact-taxon IUCN photographs support the anatomy, bottom-walking, mating alignment and egg-placement claims.
- Latest visual result: v4 full redraws show the initial jaw-grip phase with separate adult bodies and a developed larva beside small eggs. Mechanical package QA passes, but visual acceptance remains open. V1/v2 package PNGs were moved to the Recycle Bin; previous acceptance was withdrawn.
- Retired package: `2026-08-21-montseny-brook-newt` is an exact duplicate of `2026-06-26-montseny-brook-newt`; do not post it.

## Latest Completed Package

- Package: `2026-09-07-acigol-killifish`.
- Topic: Acigöl Killifish / アジュギョル・キリフィッシュ / *Anatolichthys transgrediens*.
- Region: Lake Acıgöl basin, southwestern Türkiye / Western Asia.
- Editorial classification group: Fishes.
- State: `completed, published`.
- Selected Japanese source: `acigol_killifish_japanese_imagegen_2026-09-07.png`; first generation, no retry.
- Selected English source: `acigol_killifish_english_imagegen_2026-09-07.png`; first companion generation, no retry.
- Visual scope: one pale grey-silver barred fish with upturned jaw, large dark eye, attached translucent fins and dark caudal-base band, moving through a coherent spring-to-salt-basin scene with exactly three cards.
- Artifacts: four canonical 1024x1536 PNGs, two primary X posting sets and eight synchronized sidecars. Full-size and phone-size review, direct-source, X-format and package validators pass.
- Naming caveat: no established standard Japanese common name was confirmed; アジュギョル・キリフィッシュ is a transparent rendering. Exact scale counts, fin-ray counts and sex are not claimed.

## Recent-Eight Completed Region Rotation

1. 2026-08-31 — Oceania — Oceanic Hawaiian Damselfly
2. 2026-09-01 — Africa — Nimba Otter-shrew
3. 2026-09-02 — Oceania — Fischer's Egg
4. 2026-09-03 — Africa and the western Indian Ocean — Café marron
5. 2026-09-04 — Oceania — Oʻahu Tree Snail
6. 2026-09-05 — Caribbean — Union Island Gecko
7. 2026-09-06 — South America — Blue-eyed Ground Dove
8. 2026-09-07 — Western Asia — Acigöl Killifish

Oceania three, Africa two, Caribbean one, South America one, Western Asia one.

## Recent-Eight Completed Classification Rotation

1. 2026-08-31 — Insects — Oceanic Hawaiian Damselfly
2. 2026-09-01 — Mammals — Nimba Otter-shrew
3. 2026-09-02 — Fungi and lichens — Fischer's Egg
4. 2026-09-03 — Plants — Café marron
5. 2026-09-04 — Other invertebrates — Oʻahu Tree Snail
6. 2026-09-05 — Reptiles — Union Island Gecko
7. 2026-09-06 — Birds — Blue-eyed Ground Dove
8. 2026-09-07 — Fishes — Acigöl Killifish

Each listed group occupies one slot; Amphibians is absent. Rotation is only a tie-breaker after full-history duplicate and evidence screening.

## Daily Quality Loop

- The focused four-image IUCN identity bundle took about 25 minutes despite exact asset selection.
- The first successful local bundle was retained; the three adult views were reused for both languages and the juvenile view stayed variation evidence only.
- Original first-pass and v2 visual approvals were withdrawn after user review. V4 is mechanically valid but still awaiting visual acceptance.
- Repeated asset-bundling friction triggered one policy refinement: begin with at most three role-distinct exact-taxon images, adding a fourth only for material sex, age, or stage variation.

## Next Concrete Change

- Preserve the current Sardinian Brook Salamander v4 candidate and local references for tomorrow's visual review; it is not accepted art.
- Keep the package at `needs review, regenerated`. Do not count it in completed rotation or publish it as completed.
- Begin with at most three role-distinct exact-taxon images; add a fourth only when sex, age, or stage variation materially changes the visual lock, and never repeat a slow export once the first local set is usable.
- Use x-post-ja.md / x-post-en.md as primary posting sets; sidecars are synchronized backups.
- Production rules are centralized in automation-2-production-policy.md;
  historical logs no longer supply active visual instructions.
- New packages use templates/visual-and-copy-brief.md: reference-grounded
  defining features, natural occlusion and three heading/explanation cards.
- Main posts use their own language's single poster by default. Sidecars are
  generated by sync_posting_sidecars.py; X limits use the official weighted parser.
