# Automation 2 Current State

Updated: 2026-09-09T10:46:04+09:00

This state supersedes the Research Reset and earlier premature acceptance.

## Workflow

- Default workflow: Quality Run with complete Japanese and English posters and three illustrated observation cards.
- Pending evidence package: none.
- Active package: none.
- Unfinished visual gate: none after the user's explicit adoption and X-post confirmation.
- Latest package: `2026-09-09-seychelles-sheath-tailed-bat`.
- Latest state: `completed, published`; package content commit `d673a930b8787ea2e9eb9d125bfab0cd87699156` is verified on GitHub. Nothing was posted to X.
- Latest evidence: directly inspected current IUCN record T5112A271898609, Global CR under C2a(i), assessed 13 December 2024 and published in 2025; Mammal Diversity Database, Gerlach 2006 and two exact-taxon IUCN photographs support naming, boulder-cave roosts, clear cave flyways, insect diet and the visible identity lock.
- Latest visual result: user review rejected the earlier canonical pair for branching wing/leg/membrane anatomy. Those four PNGs were moved to the Windows Recycle Bin. The replacements use one bat with both wings fully folded, exactly two ceiling-gripping feet and no additional bats in the cards; both languages pass full-size and phone-size review. After a primary-source posture check distinguished hind-limb rest from four-limb alert/movement, the user explicitly accepted the current posters.
- Retired package: `2026-08-21-montseny-brook-newt` is an exact duplicate of `2026-06-26-montseny-brook-newt`; do not post it.

## Latest Completed Package

- Package: `2026-09-09-seychelles-sheath-tailed-bat`.
- Topic: Seychelles Sheath-tailed Bat / セーシェルサシオコウモリ / *Coleura seychellensis*.
- Region: Mahé and Silhouette, Seychelles / western Indian Ocean / Africa.
- Editorial classification group: Mammals.
- State: `completed, published`.
- Selected Japanese source: `seychelles_sheath_tailed_bat_japanese_imagegen_2026-09-09.png`; user-requested full redraw followed by one Card 1 heading-placement edit.
- Selected English source: `seychelles_sheath_tailed_bat_english_imagegen_2026-09-09.png`; full redraw from the accepted Japanese replacement.
- Visual scope: one compact dark-brown bat hangs beneath a horizontal granite ceiling with wings fully folded and two feet attached; exactly three illustrated cards cover roost ceiling, flight corridor and nocturnal insects without additional bat figures.
- Artifacts: four canonical 1024x1536 PNGs, two primary X posting sets and eight synchronized sidecars. Full-size and phone-size review, direct-source, X-format, package, pixel-identity and whitespace checks pass.
- Naming caveat: セーシェルサシオコウモリ is database-backed but not claimed as a formally standardized Japanese mammal-list name. Tail-sheath detail is not used as a public card claim because the retained photographs do not resolve it clearly.

## Recent-Eight Completed Region Rotation

1. 2026-09-02 — Oceania — Fischer's Egg
2. 2026-09-03 — Africa and the western Indian Ocean — Café marron
3. 2026-09-04 — Oceania — Oʻahu Tree Snail
4. 2026-09-05 — Caribbean — Union Island Gecko
5. 2026-09-06 — South America — Blue-eyed Ground Dove
6. 2026-09-07 — Western Asia — Acigöl Killifish
7. 2026-09-08 — Europe — Sardinian Brook Salamander
8. 2026-09-09 — Africa and the western Indian Ocean — Seychelles Sheath-tailed Bat

Africa two, Oceania two, Caribbean one, South America one, Western Asia one, Europe one.

## Recent-Eight Completed Classification Rotation

1. 2026-09-02 — Fungi and lichens — Fischer's Egg
2. 2026-09-03 — Plants — Café marron
3. 2026-09-04 — Other invertebrates — Oʻahu Tree Snail
4. 2026-09-05 — Reptiles — Union Island Gecko
5. 2026-09-06 — Birds — Blue-eyed Ground Dove
6. 2026-09-07 — Fishes — Acigöl Killifish
7. 2026-09-08 — Amphibians — Sardinian Brook Salamander
8. 2026-09-09 — Mammals — Seychelles Sheath-tailed Bat

Each listed group occupies one slot; Insects is absent. Rotation is only a tie-breaker after full-history duplicate and evidence screening.

## Daily Quality Loop

- The focused two-image IUCN identity bundle took about 17 minutes despite exact asset selection; this is the first recurrence after the latest workflow-friction counter reset.
- The first successful local copies were retained and reused for both languages; no repeated export was attempted.
- The Japanese first pass exposed an ambiguous central wing overlap. One localized edit corrected only the hero anatomy while preserving the locked text and cards; the English companion used that corrected composition.
- Tomorrow: keep the initial exact-taxon bundle role-distinct and minimal, then prefer the first successful local copies for both languages.
- User review later rejected that apparent correction because the hero and Card 1 still contained branching wing/leg/membrane shapes. Four PNGs were recycled and both languages were fully redrawn with folded wings and no card bats; the earlier visual acceptance is superseded.

## Next Concrete Change

- Preserve the user-requested Seychelles Sheath-tailed Bat full redraws and local references; do not reopen generation without user direction.
- Preserve the package as `completed, published`. No unfinished package remains; X publication still requires explicit user direction.
- Begin with at most three role-distinct exact-taxon images; add a fourth only when sex, age, or stage variation materially changes the visual lock, and never repeat a slow export once the first local set is usable.
- Use x-post-ja.md / x-post-en.md as primary posting sets; sidecars are synchronized backups.
- Production rules are centralized in automation-2-production-policy.md;
  historical logs no longer supply active visual instructions.
- New packages use templates/visual-and-copy-brief.md: reference-grounded
  defining features, natural occlusion and three heading/explanation cards.
- Main posts use their own language's single poster by default. Sidecars are
  generated by sync_posting_sidecars.py; X limits use the official weighted parser.
