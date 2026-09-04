# Automation 2 Current State

Updated: 2026-09-04T22:51:06+09:00

This file is the small replace-in-place state record for Automation `automation-2`. Run history remains in Automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English Image Gen posters, species-specific illustrated observation cards, and an editorial review of X copy.
- Pending evidence package: none.
- Active package: none.
- Latest package: `2026-09-04-oahu-tree-snail`.
- Latest state: `completed, published`. Package content commit `958305db5a7ac30d4ddbe5601dad841a61f90e88` was pushed to `origin/master` and the remote ref was verified.
- Latest evidence: the directly inspected current official IUCN record `T191A13048229` is Global CR under old criteria A1ce, B1+2abcde, assessed 1 August 1996 and published in 1996; the Needs updating annotation is disclosed. Hawaiʻi DLNR, USFWS, and Holland and Hadfield lock the accepted name, Waiʻanae forest habitat, glossy high-spired banded shell, nocturnal leaf-fungus grazing, and live birth.
- Latest visual result: the first Japanese poster and first English companion both passed without retries. Each has one dominant leaf-crawling adult, a glossy high-spired dark-and-cream shell, continuous body anatomy, and exactly three unequal illustrated cards for habitat, shell variation, and nocturnal grazing with one live young.
- Retired package: `2026-08-21-montseny-brook-newt`, an exact duplicate of the completed and published `2026-06-26-montseny-brook-newt` package. Do not post or publish it.
- The canonical package write gate is available.

## Latest Completed Package

- Package: `2026-09-04-oahu-tree-snail`.
- Topic: Oʻahu Tree Snail / オアフ・ツリースネイル / *Achatinella mustelina*.
- State: `completed, published`.
- Region: Waiʻanae Range, Oʻahu, Hawaiian Islands, United States / central Pacific / Oceania.
- Editorial classification group: Other invertebrates.
- Evidence: the directly inspected current official IUCN assessment `T191A13048229` is Global Critically Endangered under criteria A1ce, B1+2abcde, assessed 1 August 1996, with a Needs updating annotation. Hawaiʻi DLNR and USFWS support the fragmented upper-elevation mesic and wet forest habitat, small glossy high-spired shell, nocturnal arboreal fungus grazing, and live birth.
- Candidate screen: Oʻahu Tree Snail, Seychelles Sheath-tailed Bat, and White-winged Flufftail spanned Other invertebrates, Mammals, and Birds and used exact official IUCN records. Oʻahu Tree Snail ranked first for international unfamiliarity, its connected tree-night-grazing-live-birth discovery progression, direct evidence, and stable leaf-crawling visual identity; the absent Other invertebrates slot was only the final tie-breaker.
- Duplicate gate: accepted scientific name, historical infraspecific names, English and Hawaiian aliases, Japanese renderings, and slugs were searched across Automation memory, memory registry, INDEX, package contents, and folder names. No completed collision or earlier candidate screen was found.
- Locked discovery: a jewel-like land snail spends its life in Waiʻanae forest trees, grazes fungi from leaves after dark, and gives birth to one relatively large live young at a time.
- Artifacts and QA: four canonical `1024x1536` poster PNGs, eight synchronized sidecars, three archived official Hawaiʻi DLNR identity references, Copy Lock, prompts, README, and Sources QA are synchronized. Both first-pass direct posters passed the source gate; X format, package validation, full-size and `360x540` phone-size review, pixel identity, shell/body anatomy, false-silhouette, card, typography, and composition QA pass.

## Recent-Eight Completed Region Rotation

1. 2026-08-28 — Cebu Island, Philippines / Asia — Cebu Flowerpecker
2. 2026-08-29 — Vâlsan River, Argeș basin, Romania / Europe — Asprete
3. 2026-08-30 — Lake Oku, Cameroon Highlands, Cameroon / Africa — Lake Oku Clawed Frog
4. 2026-08-31 — windward Ko'olau Mountains, O'ahu, Hawai'i / Oceania — Oceanic Hawaiian Damselfly
5. 2026-09-01 — Mount Nimba and the Putu Range, West Africa / Africa — Nimba Otter-shrew
6. 2026-09-02 — Tasmania, Australia, and New Zealand / Oceania — Fischer's Egg
7. 2026-09-03 — Rodrigues, Mascarene Islands, Mauritius / Africa and the western Indian Ocean — Café marron
8. 2026-09-04 — Waiʻanae Range, Oʻahu, Hawaiian Islands, United States / central Pacific / Oceania — Oʻahu Tree Snail

Africa and Oceania each occupy three of the latest eight; Asia and Europe each occupy one. The retired 2026-08-21 duplicate does not fill a slot.

## Recent-Eight Completed Classification Rotation

1. 2026-08-28 — Birds — Cebu Flowerpecker
2. 2026-08-29 — Fishes — Asprete
3. 2026-08-30 — Amphibians — Lake Oku Clawed Frog
4. 2026-08-31 — Insects — Oceanic Hawaiian Damselfly
5. 2026-09-01 — Mammals — Nimba Otter-shrew
6. 2026-09-02 — Fungi and lichens — Fischer's Egg
7. 2026-09-03 — Plants — Café marron
8. 2026-09-04 — Other invertebrates — Oʻahu Tree Snail

Birds, Fishes, Amphibians, Insects, Mammals, Other invertebrates, Plants, and Fungi and lichens each occupy one slot; Reptiles is absent. The retired 2026-08-21 duplicate does not fill a slot.

## Daily Quality Loop Counters

- `#duplicate-topic-gate`: 0 material catch this run. Full-history screening found no completed collision or earlier candidate screen for the selected species, display names, renderings, or slug.
- `#IUCN-unavailable`: 0. The current official IUCN page rendered the accepted name, Global CR category, old criteria A1ce and B1+2abcde, Global scope, 1 August 1996 assessment date, publication year, criteria version, and Needs updating annotation directly.
- `#assessment-year-drift`: 0. Public copy uses the field-level 1996 assessment year and prominently discloses the old record's Needs updating annotation in evidence and source replies.
- `#image-text-error`: 0. Both first-pass posters render all six Copy Lock lines exactly, including ʻokina/apostrophe distinctions and ASCII footer spacing.
- `#species-identity-drift`: 0. Both accepted posters preserve a small glossy high-spired dark-and-cream shell, continuous shell-to-body anatomy, four tentacles, and leaf contact without drifting into a giant African land snail, rosy wolf snail, low-spired garden snail, slug, or empty shell.
- `#workflow-friction`: 1 material occurrence. Bundling only three already-visible official DLNR photographs still took about 11.5 minutes; the first successful local copies were retained and reused for both first-pass posters without another export.

## Next Concrete Change

- No unfinished package remains. The next daily run may screen a new topic after the full-history duplicate gate.
- Keep `2026-09-04-oahu-tree-snail` at `completed, published`; package content commit `958305d` was verified on `origin/master`.
- For a page with multiple species galleries, scroll to and verify the target-species alt text before bundling; request only the two or three exact target assets and reuse the first successful local copies.
- Latest-eight rotation: Africa three, Oceania three, Asia one, and Europe one. Birds, Fishes, Amphibians, Insects, Mammals, Other invertebrates, Plants, and Fungi and lichens each occupy one slot; Reptiles is absent.
