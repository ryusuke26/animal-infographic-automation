# Automation 2 Current State

Updated: 2026-08-22T22:22:52+09:00

This file is the small replace-in-place state record for Automation `automation-2`. Run history remains in Automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English Image Gen posters, species-specific illustrated observation cards, and an editorial review of X copy.
- Pending evidence package: none.
- Active package: none.
- Active state: idle after `2026-08-22-frigate-island-giant-tenebrionid-beetle` completed, published. The earlier 2026-08-21 Montseny Brook Newt attempt remains retired and does not count as completed.
- Active evidence: none. The selected beetle's official IUCN route was directly inspectable; the official Montseny Brook Newt PDF and page capture remain preserved inside the retired audit package.
- Retired package: `2026-08-21-montseny-brook-newt`, an exact duplicate of the completed and published `2026-06-26-montseny-brook-newt` package. Do not post or publish it.
- The canonical package write gate is available.

## Latest Completed Package

- Package: `2026-08-22-frigate-island-giant-tenebrionid-beetle`.
- Topic: Frigate Island Giant Tenebrionid Beetle / フレガット島オオゴミムシダマシ / *Polposipus herculeanus*.
- State: `completed, published`.
- Region: Frégate Island, Seychelles / Africa.
- Editorial classification group: Insects.
- Evidence: the current official IUCN assessment `T17902A21425713` records Global Vulnerable under D2, assessed 16 November 2013 and published in 2014. The page is annotated `Needs updating`, but it remains the current formal global assessment; the superseded 1996 CR assessment is excluded from the public footer. The official ecology account, Ferguson and Pearce-Kelly, and museum specimens support the accepted name, coastal woodland, daytime trunk use, nocturnal ground foraging, strongly tubercled rounded back, and rotten-log larval development.
- Duplicate gate: normalized accepted name, English name, Japanese display name, aliases, and the proposed slug were searched across Automation memory, all INDEX sections, package contents, and folder names before Evidence Lock; no completed collision was found.
- Locked discovery: a large flightless beetle stays on Frégate's coastal woodland trunks by day, descends after dark to forage, and starts its next generation inside fallen rotten wood.
- Visual resolution: the first Japanese source and first English companion both passed without retry. Each uses one complete six-legged, two-antennaed dark beetle on a diagonal lichen-covered trunk, with three unequal illustrated cards integrated into the day-to-night forest scene.
- Artifacts and QA: four canonical `1024x1536` PNGs, eight synchronized sidecars, Copy Lock, prompts, README, Sources QA, and INDEX are synchronized. Both direct sources, X format, package validation, full-size and phone-size review, pixel identity, and whitespace QA pass.
- GitHub closeout: package content commit `93e64b9` was pushed directly to `origin/master` and the remote ref was verified at `93e64b95eeaca812613b6e75c9815fd437226e22`; published-state metadata follows in the closeout commit.

## Recent-Eight Completed Region Rotation

1. 2026-08-15 — Southeastern Australia and New Zealand South Island / Oceania — Tea-tree Fingers
2. 2026-08-16 — Mahé, Seychelles / Africa — Jellyfish Tree
3. 2026-08-17 — Tokashiki Island, Ryukyu Islands, Japan / Asia — Tokashiki Freshwater Crab
4. 2026-08-18 — Round Island, Mauritius / Africa — Günther's Gecko
5. 2026-08-19 — Southern China and Hainan through northern mainland Southeast Asia / Asia — White-eared Night Heron
6. 2026-08-20 — Central-western Queensland, Australia / Oceania — Redfin Blue-eye
7. 2026-08-21 — Amboli, Maharashtra, northern Western Ghats, India / Asia — Amboli Lateritic Toad
8. 2026-08-22 — Frégate Island, Seychelles / Africa — Frigate Island Giant Tenebrionid Beetle

Africa occupies three of the latest eight, Asia three, and Oceania two. The retired 2026-08-21 duplicate does not fill a slot.

## Recent-Eight Completed Classification Rotation

1. 2026-08-15 — Fungi and lichens — Tea-tree Fingers
2. 2026-08-16 — Plants — Jellyfish Tree
3. 2026-08-17 — Other invertebrates — Tokashiki Freshwater Crab
4. 2026-08-18 — Reptiles — Günther's Gecko
5. 2026-08-19 — Birds — White-eared Night Heron
6. 2026-08-20 — Fishes — Redfin Blue-eye
7. 2026-08-21 — Amphibians — Amboli Lateritic Toad
8. 2026-08-22 — Insects — Frigate Island Giant Tenebrionid Beetle

Fungi and lichens, Plants, Other invertebrates, Reptiles, Birds, Fishes, Amphibians, and Insects each occupy one slot; Mammals is absent. The retired 2026-08-21 duplicate does not fill a slot.

## Daily Quality Loop Counters

- `#duplicate-topic-gate`: 1 historical material failure remains recorded. The beetle run applied the repaired full-name, alias, Japanese-display-name, slug, INDEX, memory, content, and folder collision gate before Evidence Lock and found zero completed matches.
- `#status-version-drift`: 0 unresolved. The current official 2013 VU assessment superseded a still-visible 1996 CR record before Copy Lock.
- `#assessment-year-drift`: 0. The public footer uses the 2013 assessment year, not the 2014 publication year.
- `#species-identity-drift`: 0. Both first-pass posters passed visual identity, six-leg/two-antenna topology, habitat, text, and card QA.

## Next Concrete Change

- Begin the next scheduled run with no unfinished package.
- Region rotation is Africa three, Asia three, and Oceania two; use it only after unfamiliarity, evidence, discovery strength, naming, and visual viability.
- Mammals is absent from the latest eight editorial groups and may break a tie among equally strong candidates.
- Before screening evidence, normalize and search each candidate's accepted scientific name, English name, Japanese name, aliases, and proposed slug across Automation memory, all INDEX sections, and package folder names. Any completed collision is a hard rejection.
- Keep the retired Montseny package as a duplicate and visual-risk exclusion; do not revive it without an explicit user request.
- Keep future Quality Runs local-ready until GitHub publication is explicitly requested and remotely verified.
