# Automation 2 Current State

Updated: 2026-09-03T21:59:17+09:00

This file is the small replace-in-place state record for Automation `automation-2`. Run history remains in Automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English Image Gen posters, species-specific illustrated observation cards, and an editorial review of X copy.
- Pending evidence package: none.
- Active package: none.
- Latest package: `2026-09-03-cafe-marron`.
- Latest state: `completed, local-ready`. Git and GitHub were not mutated.
- Latest evidence: the directly inspected current official IUCN record `T33659A164117186` is Global CR under criterion D, assessed 29 June 2025 and published in 2026. Kew POWO, the Kew species profile, Mauritian Wildlife Foundation, and Catalogue of Life through GBIF lock the accepted name, public names, habitat, heterophyllous leaf stages, and corolla colour change.
- Latest visual result: the first Japanese poster and first English companion both passed without retries. Each has one dominant flowering adult shrub, broad glossy adult leaves, long-tubed five-lobed white flowers, and exactly three unequal illustrated cards; the juvenile narrow foliage appears only in the comparison card.
- Retired package: `2026-08-21-montseny-brook-newt`, an exact duplicate of the completed and published `2026-06-26-montseny-brook-newt` package. Do not post or publish it.
- The canonical package write gate is available.

## Latest Completed Package

- Package: `2026-09-03-cafe-marron`.
- Topic: Café marron / カフェマロン / *Ramosmania rodriguesii*.
- State: `completed, local-ready`.
- Region: Rodrigues, Mascarene Islands, Mauritius / Africa and the western Indian Ocean.
- Editorial classification group: Plants.
- Evidence: the directly inspected current official IUCN assessment `T33659A164117186` is Global Critically Endangered under criterion D, assessed 29 June 2025 and published in 2026. Kew and Mauritian Wildlife Foundation sources support the Rodriguan forest habitat, narrow juvenile versus broad adult leaves, and greenish-yellow corollas maturing to white.
- Candidate screen: Café marron, Seychelles Sheath-tailed Bat, and White-winged Flufftail spanned Plants, Mammals, and Birds; all three had directly inspectable official global IUCN assessments. Café marron ranked first for international unfamiliarity, its leaf-and-flower maturation doorway, current evidence, and stable visual identity; the absent Plants slot was only the final tie-breaker.
- Duplicate gate: accepted scientific name, accented and unaccented display names, Japanese renderings, and slug were searched across Automation memory, memory registry, INDEX, package contents, and folder names. No completed collision or earlier candidate screen was found.
- Locked discovery: the same plant begins with long narrow juvenile foliage, later carries shorter broad leaves, and opens greenish-yellow corollas that mature to white.
- Artifacts and QA: four canonical `1024x1536` poster PNGs, eight synchronized sidecars, four archived official IUCN identity references, Copy Lock, prompts, README, and Sources QA are synchronized. Both first-pass direct posters passed the source gate; X format, package validation, full-size and `360x540` phone-size review, pixel identity, false-silhouette, card, and composition QA pass.

## Recent-Eight Completed Region Rotation

1. 2026-08-27 — Roatán, Barbareta, and nearby cays, Bay Islands, Honduras / Central America and the Caribbean — Roatán Spiny-tailed Iguana
2. 2026-08-28 — Cebu Island, Philippines / Asia — Cebu Flowerpecker
3. 2026-08-29 — Vâlsan River, Argeș basin, Romania / Europe — Asprete
4. 2026-08-30 — Lake Oku, Cameroon Highlands, Cameroon / Africa — Lake Oku Clawed Frog
5. 2026-08-31 — windward Ko'olau Mountains, O'ahu, Hawai'i / Oceania — Oceanic Hawaiian Damselfly
6. 2026-09-01 — Mount Nimba and the Putu Range, West Africa / Africa — Nimba Otter-shrew
7. 2026-09-02 — Tasmania, Australia, and New Zealand / Oceania — Fischer's Egg
8. 2026-09-03 — Rodrigues, Mascarene Islands, Mauritius / Africa and the western Indian Ocean — Café marron

Africa occupies three of the latest eight; Oceania occupies two; Central America and the Caribbean, Asia, and Europe each occupy one. The retired 2026-08-21 duplicate does not fill a slot.

## Recent-Eight Completed Classification Rotation

1. 2026-08-27 — Reptiles — Roatán Spiny-tailed Iguana
2. 2026-08-28 — Birds — Cebu Flowerpecker
3. 2026-08-29 — Fishes — Asprete
4. 2026-08-30 — Amphibians — Lake Oku Clawed Frog
5. 2026-08-31 — Insects — Oceanic Hawaiian Damselfly
6. 2026-09-01 — Mammals — Nimba Otter-shrew
7. 2026-09-02 — Fungi and lichens — Fischer's Egg
8. 2026-09-03 — Plants — Café marron

Reptiles, Birds, Fishes, Amphibians, Insects, Mammals, Fungi and lichens, and Plants each occupy one slot; Other invertebrates is absent. The retired 2026-08-21 duplicate does not fill a slot.

## Daily Quality Loop Counters

- `#duplicate-topic-gate`: 0 material catch this run. Full-history screening found no completed collision or earlier candidate screen for the selected species, display names, renderings, or slug.
- `#IUCN-unavailable`: 0. The current official IUCN page rendered the accepted name, Global CR category, criterion D, scope, assessment date, publication year, population context, habitat, and current threats directly.
- `#assessment-year-drift`: 0. Public copy uses the 2025 assessment year and distinguishes it from the 2026 publication year in source notes.
- `#image-text-error`: 0. Both first-pass posters render all six Copy Lock lines exactly, including the acute accent in `Café` and ASCII footer spacing.
- `#species-identity-drift`: 0. Both accepted posters preserve broad adult leaves, long-tubed five-lobed white flowers, and the separate narrow juvenile form without drifting into coffee, gardenia, jasmine, plumeria, or a generic white-flowered shrub.
- `#workflow-friction`: 1 material occurrence. Bundling four already-visible official IUCN image assets took about 65 minutes; the first successful local copies were retained and reused without repeating the export.

## Next Concrete Change

- No unfinished package remains. The next daily run may screen a new topic after the full-history duplicate gate.
- Keep `2026-09-03-cafe-marron` at `completed, local-ready`; GitHub publication remains separate.
- For official visual references, export the smallest non-redundant set that establishes identity and stage variation, normally two or three images; retain and reuse the first successful local bundle rather than repeating a slow asset export.
- Latest-eight rotation: Africa three, Oceania two, Central America and the Caribbean one, Asia one, and Europe one. Reptiles, Birds, Fishes, Amphibians, Insects, Mammals, Fungi and lichens, and Plants each occupy one slot; Other invertebrates is absent.
