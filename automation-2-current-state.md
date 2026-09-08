# Automation 2 Current State

Updated: 2026-09-09T07:53:47+09:00

This state supersedes the Research Reset and earlier premature acceptance.

## Workflow

- Default workflow: Quality Run with complete Japanese and English posters and three illustrated observation cards.
- Pending evidence package: none.
- Active package: none.
- Unfinished visual gate: none after the user's explicit adoption and X-post confirmation.
- Latest package: `2026-09-08-sardinian-brook-salamander`.
- Latest state: `completed, published`; the user confirmed it was posted to X, and package content commit `0965f09` is verified on GitHub.
- Latest evidence: directly inspected current IUCN record T8371A223758127, Global EN under B2ab(iii,iv), assessed 20 February 2023 and published in 2024; EAZA Amphibian TAG and four exact-taxon IUCN photographs support the anatomy, bottom-walking, mating alignment and egg-placement claims.
- Latest visual result: the user explicitly adopted the v4 redraws after confirming the species infographic was posted to X. V4 shows the initial jaw-grip phase with separate adult bodies and a developed larva beside small eggs; previous rejected assets remain out of the package.
- Retired package: `2026-08-21-montseny-brook-newt` is an exact duplicate of `2026-06-26-montseny-brook-newt`; do not post it.

## Latest Completed Package

- Package: `2026-09-08-sardinian-brook-salamander`.
- Topic: Sardinian Brook Salamander / サルデーニャ・イモリ / *Euproctus platycephalus*.
- Region: Sardinia, Italy / Mediterranean Europe.
- Editorial classification group: Amphibians.
- State: `completed, published`.
- Selected Japanese source: `sardinian_brook_salamander_japanese_imagegen_2026-09-08.png`; user-adopted v4 full redraw.
- Selected English source: `sardinian_brook_salamander_english_imagegen_2026-09-08.png`; user-adopted v4 companion.
- Visual scope: one broad-headed olive-brown adult in a Sardinian stream, an initial jaw-grip pair, small eggs with a developed larva, and exactly three illustrated cards.
- Artifacts: four canonical 1024x1536 PNGs, two primary X posting sets and eight synchronized sidecars. Full-size and phone-size review, direct-source, X-format and package validators pass.
- Naming caveat: no established standard Japanese common name was confirmed; サルデーニャ・イモリ is a transparent rendering. Pair and egg/larva scenes are qualitative illustrations, not measured anatomical plates.

## Recent-Eight Completed Region Rotation

1. 2026-09-01 — Africa — Nimba Otter-shrew
2. 2026-09-02 — Oceania — Fischer's Egg
3. 2026-09-03 — Africa and the western Indian Ocean — Café marron
4. 2026-09-04 — Oceania — Oʻahu Tree Snail
5. 2026-09-05 — Caribbean — Union Island Gecko
6. 2026-09-06 — South America — Blue-eyed Ground Dove
7. 2026-09-07 — Western Asia — Acigöl Killifish
8. 2026-09-08 — Europe — Sardinian Brook Salamander

Africa two, Oceania two, Caribbean one, South America one, Western Asia one, Europe one.

## Recent-Eight Completed Classification Rotation

1. 2026-09-01 — Mammals — Nimba Otter-shrew
2. 2026-09-02 — Fungi and lichens — Fischer's Egg
3. 2026-09-03 — Plants — Café marron
4. 2026-09-04 — Other invertebrates — Oʻahu Tree Snail
5. 2026-09-05 — Reptiles — Union Island Gecko
6. 2026-09-06 — Birds — Blue-eyed Ground Dove
7. 2026-09-07 — Fishes — Acigöl Killifish
8. 2026-09-08 — Amphibians — Sardinian Brook Salamander

Each listed group occupies one slot; Insects is absent. Rotation is only a tie-breaker after full-history duplicate and evidence screening.

## Daily Quality Loop

- The focused four-image IUCN identity bundle took about 25 minutes despite exact asset selection.
- The first successful local bundle was retained; the three adult views were reused for both languages and the juvenile view stayed variation evidence only.
- Original first-pass and v2 visual approvals were withdrawn after user review. The user explicitly adopted v4 after confirming the infographic was posted to X.
- Repeated asset-bundling friction triggered one policy refinement: begin with at most three role-distinct exact-taxon images, adding a fourth only for material sex, age, or stage variation.

## Next Concrete Change

- Preserve the user-adopted Sardinian Brook Salamander v4 artwork and local references; do not reopen generation without user direction.
- Preserve the package as `completed, published`. No unfinished package remains.
- Begin with at most three role-distinct exact-taxon images; add a fourth only when sex, age, or stage variation materially changes the visual lock, and never repeat a slow export once the first local set is usable.
- Use x-post-ja.md / x-post-en.md as primary posting sets; sidecars are synchronized backups.
- Production rules are centralized in automation-2-production-policy.md;
  historical logs no longer supply active visual instructions.
- New packages use templates/visual-and-copy-brief.md: reference-grounded
  defining features, natural occlusion and three heading/explanation cards.
- Main posts use their own language's single poster by default. Sidecars are
  generated by sync_posting_sidecars.py; X limits use the official weighted parser.
