# Automation 2 Current State

Updated: 2026-08-23T22:09:50+09:00

This file is the small replace-in-place state record for Automation `automation-2`. Run history remains in Automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English Image Gen posters, species-specific illustrated observation cards, and an editorial review of X copy.
- Pending evidence package: none.
- Active package: none.
- Active state: idle after `2026-08-23-tenkile` completed and published. The earlier 2026-08-21 Montseny Brook Newt attempt remains retired and does not count as completed.
- Active evidence: none. The selected Tenkile's official IUCN route was directly inspectable; the formal assessment is annotated `Needs updating` but remains current.
- Retired package: `2026-08-21-montseny-brook-newt`, an exact duplicate of the completed and published `2026-06-26-montseny-brook-newt` package. Do not post or publish it.
- The canonical package write gate is available.

## Latest Completed Package

- Package: `2026-08-23-tenkile`.
- Topic: Tenkile / スコットキノボリカンガルー / *Dendrolagus scottae*.
- State: `completed, published`.
- Region: Torricelli Mountains, Sandaun Province, Papua New Guinea / Oceania.
- Editorial classification group: Mammals.
- Evidence: the current official IUCN assessment `T6435A21956375` records Global Critically Endangered under A2d, assessed 30 September 2015 and published in 2019. The page is annotated `Needs updating`, but it remains the current formal global assessment; no population count is used publicly. Mammal Diversity Database, the Mammal Society of Japan, Tenkile Conservation Alliance, and the original description support the accepted taxonomy, English and Japanese names, Torricelli mid-montane rainforest, uniform blackish coat, shoulder hair whorl, and high proportion of time on the ground.
- Duplicate gate: normalized accepted name, Scott's Tree Kangaroo, Tenkile Tree Kangaroo, スコットキノボリカンガルー, テンキレ, scientific name, and proposed slug were searched across Automation memory, all INDEX sections, package contents, and folder names before Evidence Lock; prior hits were candidate screens only and no completed collision was found.
- Locked discovery: a nearly black tree-kangaroo moves between mossy trunks and the Torricelli forest floor, where a shoulder hair whorl and quadrupedal ground path make the familiar group silhouette newly specific.
- Visual resolution: the Japanese first source passed the direct and identity gates but duplicated Card 1 text under the scientific name. Its allowed generative correction redrew 99.895% of pixels outside the requested area and was rejected; a deterministic repair changed only 47,029 pixels inside the text band and 0 outside. The first English companion passed without retry.
- Artifacts and QA: four canonical `1024x1536` PNGs, eight synchronized sidecars, Copy Lock, prompts, README, Sources QA, and INDEX are synchronized. Both direct sources, X format, package validation, full-size and phone-size review, pixel identity, whitespace, and manual species-identity/anatomy/composition QA pass.
- GitHub closeout: package content commit `84cc674` was pushed directly to `origin/master` and the remote ref was verified at `84cc67440e8930876a7a49a98c9a010cea31862a` before published-state metadata was prepared.

## Recent-Eight Completed Region Rotation

1. 2026-08-16 — Mahé, Seychelles / Africa — Jellyfish Tree
2. 2026-08-17 — Tokashiki Island, Ryukyu Islands, Japan / Asia — Tokashiki Freshwater Crab
3. 2026-08-18 — Round Island, Mauritius / Africa — Günther's Gecko
4. 2026-08-19 — Southern China and Hainan through northern mainland Southeast Asia / Asia — White-eared Night Heron
5. 2026-08-20 — Central-western Queensland, Australia / Oceania — Redfin Blue-eye
6. 2026-08-21 — Amboli, Maharashtra, northern Western Ghats, India / Asia — Amboli Lateritic Toad
7. 2026-08-22 — Frégate Island, Seychelles / Africa — Frigate Island Giant Tenebrionid Beetle
8. 2026-08-23 — Torricelli Mountains, Sandaun Province, Papua New Guinea / Oceania — Tenkile

Africa occupies three of the latest eight, Asia three, and Oceania two. The retired 2026-08-21 duplicate does not fill a slot.

## Recent-Eight Completed Classification Rotation

1. 2026-08-16 — Plants — Jellyfish Tree
2. 2026-08-17 — Other invertebrates — Tokashiki Freshwater Crab
3. 2026-08-18 — Reptiles — Günther's Gecko
4. 2026-08-19 — Birds — White-eared Night Heron
5. 2026-08-20 — Fishes — Redfin Blue-eye
6. 2026-08-21 — Amphibians — Amboli Lateritic Toad
7. 2026-08-22 — Insects — Frigate Island Giant Tenebrionid Beetle
8. 2026-08-23 — Mammals — Tenkile

Plants, Other invertebrates, Reptiles, Birds, Fishes, Amphibians, Insects, and Mammals each occupy one slot; Fungi and lichens is absent. The retired 2026-08-21 duplicate does not fill a slot.

## Daily Quality Loop Counters

- `#duplicate-topic-gate`: 1 historical material failure remains recorded. The Tenkile run applied the repaired full-name, English/Japanese-name, alias, slug, INDEX, memory, content, and folder collision gate before Evidence Lock and found zero completed matches.
- `#status-version-drift`: 0 unresolved. The current formal CR assessment is correctly retained despite its `Needs updating` annotation.
- `#assessment-year-drift`: 0. The public footer uses the 2015 assessment year, not the 2019 publication year.
- `#image-text-error`: 0 unresolved. The duplicated Japanese observation was removed with a measured 2.99% local repair after the global redraw retry was rejected.
- `#species-identity-drift`: 0. Both accepted posters passed black-coat, shoulder-whorl, four-limb, attached-tail, habitat, text, and card QA against official TCA photographs and the original description.

## Next Concrete Change

- Begin the next scheduled run with no unfinished package.
- Region rotation is Africa three, Asia three, and Oceania two; use it only after unfamiliarity, evidence, discovery strength, naming, and visual viability.
- Fungi and lichens is absent from the latest eight editorial groups and may break a tie among equally strong candidates.
- Before screening evidence, normalize and search each candidate's accepted scientific name, English name, Japanese name, aliases, and proposed slug across Automation memory, all INDEX sections, and package folder names. Any completed collision is a hard rejection.
- Keep the retired Montseny package as a duplicate and visual-risk exclusion; do not revive it without an explicit user request.
- Keep future Quality Runs local-ready until GitHub publication is explicitly requested and remotely verified.
