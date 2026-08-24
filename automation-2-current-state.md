# Automation 2 Current State

Updated: 2026-08-25T00:20:22+09:00

This file is the small replace-in-place state record for Automation `automation-2`. Run history remains in Automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English Image Gen posters, species-specific illustrated observation cards, and an editorial review of X copy.
- Pending evidence package: none.
- Active package: none.
- Active state: idle after `2026-08-24-noble-polypore` completed and published. The earlier 2026-08-21 Montseny Brook Newt attempt remains retired and does not count as completed.
- Active evidence: none. The selected Noble Polypore's direct IUCN assessment shell loaded without its body; the exact field-level Global CR assessment is preserved through the disclosed Global Fungal Red List reproduction of IUCN content.
- Retired package: `2026-08-21-montseny-brook-newt`, an exact duplicate of the completed and published `2026-06-26-montseny-brook-newt` package. Do not post or publish it.
- The canonical package write gate is available.

## Latest Completed Package

- Package: `2026-08-24-noble-polypore`.
- Topic: Noble Polypore / ノーブル・ポリポア / *Bridgeoporus nobilissimus*.
- State: `completed, published`.
- Region: Pacific Northwest of the United States / North America.
- Editorial classification group: Fungi and lichens.
- Evidence: the directly inspectable Global Fungal Red List reproduction of IUCN content records assessment `T76195622A97167627` as Global Critically Endangered under A2c; C2a(i), assessed 22 April 2015; the direct official IUCN page body did not render and the caveat is disclosed. USDA Forest Service and the genus paper support the accepted name, Noble Polypore common name, old-fir attachment, coarse white fibres, cinnamon aging, algae-green surface, perennial growth, and more than 100 tube layers. No established standard Japanese common name was confirmed; ノーブル・ポリポア is a transparent English-name rendering.
- Duplicate gate: normalized accepted name, *Oxyporus nobilissimus*, *Fomes nobilissimus*, Noble Polypore, Fuzzy Sandozi, Japanese display-name variants, and proposed slug were searched across Automation memory, the memory registry, all INDEX sections, package contents, and folder names before Evidence Lock; no completed collision was found.
- Locked discovery: what first resembles a mossy doormat at the foot of a giant fir is a long-lived shaggy conk that records years of growth in stacked pore layers.
- Visual resolution: the first Japanese direct poster and first English companion both passed exact-2:3/full-canvas and visual review without retries. Each shows one massive low shelf/conk visibly attached to a fir base, documented white/cinnamon/algae-green surface variation, a thick pale margin, a pore-bearing underside, and three species-specific illustrated cards.
- Artifacts and QA: four canonical `1024x1536` PNGs, eight synchronized sidecars, Copy Lock, prompts, README, Sources QA, and INDEX are synchronized. Both direct sources, X format, package validation, full-size and `360x540` phone-size review, pixel identity, whitespace, and manual growth-form/false-silhouette/composition QA pass.
- GitHub closeout: package content commit `3294a91` was pushed directly to `origin/master` and the remote ref was verified at `3294a9148d80e1eea27ddec1440a7aebd0cd74be` before published-state metadata was prepared.

## Recent-Eight Completed Region Rotation

1. 2026-08-17 — Tokashiki Island, Ryukyu Islands, Japan / Asia — Tokashiki Freshwater Crab
2. 2026-08-18 — Round Island, Mauritius / Africa — Günther's Gecko
3. 2026-08-19 — Southern China and Hainan through northern mainland Southeast Asia / Asia — White-eared Night Heron
4. 2026-08-20 — Central-western Queensland, Australia / Oceania — Redfin Blue-eye
5. 2026-08-21 — Amboli, Maharashtra, northern Western Ghats, India / Asia — Amboli Lateritic Toad
6. 2026-08-22 — Frégate Island, Seychelles / Africa — Frigate Island Giant Tenebrionid Beetle
7. 2026-08-23 — Torricelli Mountains, Sandaun Province, Papua New Guinea / Oceania — Tenkile
8. 2026-08-24 — Pacific Northwest of the United States / North America — Noble Polypore

Asia occupies three of the latest eight, Africa two, Oceania two, and North America one. The retired 2026-08-21 duplicate does not fill a slot.

## Recent-Eight Completed Classification Rotation

1. 2026-08-17 — Other invertebrates — Tokashiki Freshwater Crab
2. 2026-08-18 — Reptiles — Günther's Gecko
3. 2026-08-19 — Birds — White-eared Night Heron
4. 2026-08-20 — Fishes — Redfin Blue-eye
5. 2026-08-21 — Amphibians — Amboli Lateritic Toad
6. 2026-08-22 — Insects — Frigate Island Giant Tenebrionid Beetle
7. 2026-08-23 — Mammals — Tenkile
8. 2026-08-24 — Fungi and lichens — Noble Polypore

Other invertebrates, Reptiles, Birds, Fishes, Amphibians, Insects, Mammals, and Fungi and lichens each occupy one slot; Plants is absent. The retired 2026-08-21 duplicate does not fill a slot.

## Daily Quality Loop Counters

- `#duplicate-topic-gate`: 1 historical material failure remains recorded. The Noble Polypore run applied the repaired accepted-name, basionym, historical-combination, English/Japanese-name, alias, slug, INDEX, memory, content, and folder collision gate before Evidence Lock and found zero completed matches.
- `#IUCN-unavailable`: 0 unresolved. The direct assessment body did not render, but the field-level specialist-group reproduction of IUCN content confirmed category, criteria, and assessment date; both public source replies disclose the bounded fallback.
- `#assessment-year-drift`: 0. The public footer uses the 2015 assessment year, not the 2016 errata-publication year.
- `#image-text-error`: 0. Both first-pass posters render the exact title, scientific name, three labels, and footer without repair.
- `#species-identity-drift`: 0. Both accepted posters passed fir-attachment, low shelf/conk profile, shaggy-fibre, color-variation, pore-layer, false-silhouette, text, and card QA against the official assessment photograph and USDA descriptions.

## Next Concrete Change

- Begin the next scheduled run with no unfinished package.
- Region rotation is Asia three, Africa two, Oceania two, and North America one; use it only after unfamiliarity, evidence, discovery strength, naming, and visual viability.
- Plants is absent from the latest eight editorial groups and may break a tie among equally strong candidates.
- Before screening evidence, normalize and search each candidate's accepted scientific name, English name, Japanese name, aliases, and proposed slug across Automation memory, all INDEX sections, and package folder names. Any completed collision is a hard rejection.
- Keep the retired Montseny package as a duplicate and visual-risk exclusion; do not revive it without an explicit user request.
- Keep future Quality Runs local-ready until GitHub publication is explicitly requested and remotely verified.
