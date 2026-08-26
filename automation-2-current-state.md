# Automation 2 Current State

Updated: 2026-08-27T00:16:09+09:00

This file is the small replace-in-place state record for Automation `automation-2`. Run history remains in Automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English Image Gen posters, species-specific illustrated observation cards, and an editorial review of X copy.
- Pending evidence package: none.
- Active package: none.
- Active state: idle after `2026-08-26-desertas-wolf-spider` completed and published. The earlier 2026-08-21 Montseny Brook Newt attempt remains retired and does not count as completed.
- Active evidence: none. The Desertas Wolf Spider's formal IUCN assessment PDF and DOI confirm Global CR under B1ab(ii,iii,v)+2ab(ii,iii,v), assessed 7 April 2014; the current official page body did not render, and the bounded access caveat is disclosed.
- Retired package: `2026-08-21-montseny-brook-newt`, an exact duplicate of the completed and published `2026-06-26-montseny-brook-newt` package. Do not post or publish it.
- The canonical package write gate is available.

## Latest Completed Package

- Package: `2026-08-26-desertas-wolf-spider`.
- Topic: Desertas Wolf Spider / デゼルタ・ウルフスパイダー / *Hogna ingens*.
- State: `completed, published`.
- Region: Deserta Grande, Madeira archipelago, Portugal / Europe.
- Editorial classification group: Other invertebrates.
- Evidence: formal IUCN assessment `e.T58048571A58061007` records Global Critically Endangered under B1ab(ii,iii,v)+2ab(ii,iii,v), assessed and published in 2014. The current official page body did not render, so the preserved full assessment PDF reproduction and DOI are disclosed. EAZA, the 2022 integrative revision, and World Spider Catalog support the accepted name, Castanheira Valley under-rock burrows, stocky grey adult, black-and-white-banded legs, and predation on invertebrates and juvenile Madeira wall lizards. No established standard Japanese common name was confirmed; デゼルタ・ウルフスパイダー is a transparent English-name rendering.
- Duplicate gate: normalized accepted name, *Lycosa ingens*, Desertas Wolf Spider, Deserta Grande Wolf Spider, Japanese rendering variants, and proposed slug were searched across Automation memory, the memory registry, all INDEX sections, package contents, and folder names before Evidence Lock; no completed collision was found. Bornean Flat-headed Frog was rejected as a completed duplicate during candidate screening; White-bellied Heron remained candidate-screen-only.
- Locked discovery: beneath one volcanic rock in a small island valley, a large wolf spider occupies the top-predator role and can catch juvenile Madeira wall lizards.
- Visual resolution: the first Japanese direct poster passed the source gate but was visually rejected because all labels sat outside its cards. One fresh-canvas retry passed with one complete adult female, eight separate walking legs, two distinct pedipalps, exact Copy Lock, volcanic under-rock habitat, and three species-specific illustrated cards. The first English companion passed without retry.
- Artifacts and QA: four canonical `1024x1536` PNGs, eight synchronized sidecars, three authoritative visual references, Copy Lock, prompts, README, Sources QA, and INDEX are synchronized. Both direct sources, X format, package validation, full-size and `360x540` phone-size review, pixel identity, whitespace, eight-leg topology, false-silhouette, and composition QA pass.
- GitHub closeout: package content commit `71511b4` was pushed directly to `origin/master` and the remote ref was verified at `71511b45bd7a465f4c289ee7d6c96d94509e528d` before published-state metadata was prepared.

## Recent-Eight Completed Region Rotation

1. 2026-08-19 — Southern China and Hainan through northern mainland Southeast Asia / Asia — White-eared Night Heron
2. 2026-08-20 — Central-western Queensland, Australia / Oceania — Redfin Blue-eye
3. 2026-08-21 — Amboli, Maharashtra, northern Western Ghats, India / Asia — Amboli Lateritic Toad
4. 2026-08-22 — Frégate Island, Seychelles / Africa — Frigate Island Giant Tenebrionid Beetle
5. 2026-08-23 — Torricelli Mountains, Sandaun Province, Papua New Guinea / Oceania — Tenkile
6. 2026-08-24 — Pacific Northwest of the United States / North America — Noble Polypore
7. 2026-08-25 — Analalava District, northwestern Madagascar / Africa — Tahina Palm
8. 2026-08-26 — Deserta Grande, Madeira archipelago, Portugal / Europe — Desertas Wolf Spider

Africa, Asia, and Oceania each occupy two of the latest eight; North America and Europe each occupy one. The retired 2026-08-21 duplicate does not fill a slot.

## Recent-Eight Completed Classification Rotation

1. 2026-08-19 — Birds — White-eared Night Heron
2. 2026-08-20 — Fishes — Redfin Blue-eye
3. 2026-08-21 — Amphibians — Amboli Lateritic Toad
4. 2026-08-22 — Insects — Frigate Island Giant Tenebrionid Beetle
5. 2026-08-23 — Mammals — Tenkile
6. 2026-08-24 — Fungi and lichens — Noble Polypore
7. 2026-08-25 — Plants — Tahina Palm
8. 2026-08-26 — Other invertebrates — Desertas Wolf Spider

Birds, Fishes, Amphibians, Insects, Mammals, Fungi and lichens, Plants, and Other invertebrates each occupy one slot; Reptiles is absent. The retired 2026-08-21 duplicate does not fill a slot.

## Daily Quality Loop Counters

- `#duplicate-topic-gate`: 1 historical material failure remains recorded. This run applied the full accepted-name, synonym, English-name, Japanese-rendering, slug, INDEX, memory, content, and folder collision gate before Evidence Lock, rejected the completed Bornean Flat-headed Frog candidate, and found zero completed *Hogna ingens* collision.
- `#IUCN-unavailable`: 0 unresolved. The current page body did not render, but the formal full assessment PDF reproduction and exact DOI directly confirmed category, criteria, and assessment date; the bounded access caveat is public.
- `#assessment-year-drift`: 0. The public footer uses the 2014 assessment year, which is also the publication year.
- `#image-text-error`: 1 one-off occurrence, resolved. The first Japanese source put exact labels outside the cards; one fresh-canvas retry grouped each label with its numbered card, and the English first pass remained exact.
- `#species-identity-drift`: 0. Both accepted posters passed stocky-body, grey-colour, black-and-white-band, eight-walking-leg, two-pedipalp, rock-burrow, volcanic-habitat, false-silhouette, text, and card QA against three authoritative references.
- `#workflow-friction`: 0 unresolved. Only three references covering adult topology, adult field appearance, and habitat context were bundled.

## Next Concrete Change

- Begin the next scheduled run with no unfinished package.
- Region rotation is Africa two, Asia two, Oceania two, North America one, and Europe one; use it only after unfamiliarity, evidence, discovery strength, naming, and visual viability.
- Reptiles is absent from the latest eight editorial groups and may break a tie among equally strong candidates.
- Before screening evidence, normalize and search each candidate's accepted scientific name, English name, Japanese name, aliases, and proposed slug across Automation memory, all INDEX sections, and package folder names. Any completed collision is a hard rejection.
- Keep the retired Montseny package as a duplicate and visual-risk exclusion; do not revive it without an explicit user request.
- When authoritative pages expose many visual assets, inspect the inventory first and bundle only the adult-habit, diagnostic-structure, and habitat references needed for Image Gen.
- Keep future Quality Runs local-ready until GitHub publication is explicitly requested and remotely verified.
