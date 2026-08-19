# Automation 2 Current State

Updated: 2026-08-19T13:48:58+09:00

This file is the small replace-in-place state record for Automation `automation-2`. Run history remains in Automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English Image Gen posters, species-specific illustrated observation cards, and an editorial review of X copy.
- Pending evidence package: none.
- Active package: none.
- Active state: idle after `2026-08-19-white-eared-night-heron` completed local-ready.
- Active evidence: the supplied official IUCN 2025 assessment PDF and current-page capture directly confirm *Oroanassa magnifica* as Global NT under C2a(ii), assessed 12 May 2025 as `T22697232A175978137`. The PDF records *Gorsachius magnificus* and *Nycticorax magnificus* as synonyms; ITIS and AviList independently support the accepted current combination.
- Retired package: none.
- The canonical package write gate is available.

## Latest Completed Package

- Package: `2026-08-19-white-eared-night-heron`.
- Topic: White-eared Night Heron / ハイナンミゾゴイ / *Oroanassa magnifica*.
- State: `completed, local-ready`.
- Region: southern China and Hainan through northern mainland Southeast Asia / Asia.
- Editorial classification group: Birds.
- Evidence: the supplied official 14-page IUCN assessment PDF directly identifies Global Near Threatened (NT), criterion C2a(ii), assessed 12 May 2025 as `T22697232A175978137`, and reconciles the current *Oroanassa magnifica* combination with former synonyms. Avibase supports ハイナンミゾゴイ; Cornell eBird and Gao et al. (2013) support shaded forest streams, white post-ocular stripes, chestnut neck sides, and adults leaving the nest after sunset and returning before dawn.
- Locked discovery: in a forest where the stream is already dark before sunset, the white-striped heron waits at its tree nest by day, leaves after sunset, and returns before dawn.
- Visual resolution: user review reopened both language identity gates because the compact, barrel-chested silhouettes read too much like generic night herons. The accepted Japanese source now has a slender outlined neck, tapered white throat, lean oval torso, and three cards stacked on the left. After that card arrangement was approved, a fresh English companion aligned the same left-card/right-hero structure while preserving the shallow-S neck, long coherent legs, and species markings. The earlier anatomically accepted English correction is preserved as superseded.
- Artifacts and QA: four canonical `1024x1536` PNGs, rejected/superseded generation evidence, accepted audit copies, the official IUCN PDF and page capture, eight synchronized sidecars, Copy Lock, prompts, README, Sources QA, and INDEX are synchronized. Both direct sources, X format, package validation, full-size and phone-size review, pixel identity, and whitespace QA pass.
- Automation memory sync: the completion and Daily Quality Loop entry were appended during local-ready closeout.

## Recent-Eight Completed Region Rotation

1. 2026-08-12 — Table Mountain, South Africa / Africa — Table Mountain Ghost Frog
2. 2026-08-13 — East Asia / Asia — Bekko Tombo
3. 2026-08-14 — Southern Tanzania / Africa — Kipunji
4. 2026-08-15 — Southeastern Australia and New Zealand South Island / Oceania — Tea-tree Fingers
5. 2026-08-16 — Mahé, Seychelles / Africa — Jellyfish Tree
6. 2026-08-17 — Tokashiki Island, Ryukyu Islands, Japan / Asia — Tokashiki Freshwater Crab
7. 2026-08-18 — Round Island, Mauritius / Africa — Günther's Gecko
8. 2026-08-19 — Southern China and Hainan through northern mainland Southeast Asia / Asia — White-eared Night Heron

Africa occupies four of the latest eight, Asia three, and Oceania one.

## Recent-Eight Completed Classification Rotation

1. 2026-08-12 — Amphibians — Table Mountain Ghost Frog
2. 2026-08-13 — Insects — Bekko Tombo
3. 2026-08-14 — Mammals — Kipunji
4. 2026-08-15 — Fungi and lichens — Tea-tree Fingers
5. 2026-08-16 — Plants — Jellyfish Tree
6. 2026-08-17 — Other invertebrates — Tokashiki Freshwater Crab
7. 2026-08-18 — Reptiles — Günther's Gecko
8. 2026-08-19 — Birds — White-eared Night Heron

Amphibians, Insects, Mammals, Fungi and lichens, Plants, Other invertebrates, Reptiles, and Birds each occupy one slot; Fishes is absent.

## Daily Quality Loop Counters

- `#source-access-caveat`: resolved. The supplied official PDF and current-page capture directly expose the category, scope, criterion, assessment date, record ID, taxonomy, identification, range, habitat, and behavior fields used in QA.
- `#assessment-year-drift`: 0 in this run. The public footer uses the official 2025 assessment year.
- `#species-identity-drift`: 2 user-detected language corrections in this run. Both initial language silhouettes overused a squat generic night-heron body plan; the final bilingual pair now preserves the white post-ocular stripe, chestnut neck, slim readable neck, lean torso, coherent legs and feet, shaded forest-stream habitat, and aligned card architecture.
- `#source-canvas-drift`: 0/2 canonical sources. Both accepted direct posters are exact 1024x1536, exact 2:3, and full-canvas.
- `#image-text-error`: 1 isolated punctuation drift. The Japanese source rendered a semantically equivalent ASCII colon plus one space; the failed bounded edit was rejected, and Copy Lock was synchronized to the stronger initial poster without pixel repair.

## Next Concrete Change

- Begin the next scheduled run with no unfinished package.
- Exclude Africa from an otherwise tied candidate slate because it still occupies four of the latest eight; use rotation only after unfamiliarity, evidence, discovery strength, naming, and visual viability.
- Fishes is absent from the latest eight classification groups and may break a tie among equally strong candidates.
- For mixed-script Japanese IUCN footers, prefer a factually equivalent ASCII colon plus one following space in the initial Copy Lock when typography allows; do not spend a retry on semantically neutral punctuation unless legibility or meaning changes.
- Before prompting anatomy-sensitive birds, compare multiple adult photographs in both resting and alert/foraging postures and lock the species-specific head-to-neck-to-shoulder silhouette; avoid generic group labels such as `stocky night-heron` when they erase the target's relative proportions.
- When the user supplies a directly inspectable official assessment after fallback evidence was used, reopen only the affected evidence surfaces, preserve the official artifacts with hashes, and remove obsolete access caveats before final validation.
- Keep the next Quality Run local-ready until GitHub publication is explicitly requested and remotely verified.
