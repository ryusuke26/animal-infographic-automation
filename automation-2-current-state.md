# Automation 2 Current State

Updated: 2026-09-01T23:09:54+09:00

This file is the small replace-in-place state record for Automation `automation-2`. Run history remains in Automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English Image Gen posters, species-specific illustrated observation cards, and an editorial review of X copy.
- Pending evidence package: none.
- Active package: none.
- Latest package: `2026-09-01-nimba-otter-shrew`.
- Latest state: `completed, published`. Package content commit `327561a4e321a09b6128165ea22ebe505c9d42fa` was pushed to `origin/master` and the remote ref was verified at the same commit.
- Latest evidence: formal IUCN assessment `T13393A111940150` is Global VU under B1ab(i,ii,iii,v), assessed 20 December 2017 and published in 2018. The official 2018-2 category-change table and IUCN SSC Afrotheria records match; current taxonomy and standard Japanese naming are locked through Mammal Diversity Database and the Mammal Society of Japan.
- Latest visual result: first-pass Japanese and English direct posters passed. Each has one dominant compact dark adult in a natural low stream-edge pose, exact Copy Lock, a long thin non-paddle tail, unwebbed feet, and exactly three unequal illustrated cards.
- Retired package: `2026-08-21-montseny-brook-newt`, an exact duplicate of the completed and published `2026-06-26-montseny-brook-newt` package. Do not post or publish it.
- The canonical package write gate is available.

## Latest Completed Package

- Package: `2026-09-01-nimba-otter-shrew`.
- Topic: Nimba Otter-shrew / ヒメポタモガーレ / *Micropotamogale lamottei*.
- State: `completed, published`.
- Region: Mount Nimba and the Putu Range, Guinea, Liberia, and Cote d'Ivoire / West Africa / Africa.
- Editorial classification group: Mammals.
- Evidence: formal IUCN assessment `T13393A111940150` is Global Vulnerable under B1ab(i,ii,iii,v), assessed 20 December 2017. The official IUCN 2018-2 change table and IUCN SSC Afrotheria records match; Mammal Diversity Database, the Mammal Society of Japan, and Monadjem et al. lock taxonomy, bilingual names, forest-stream habitat, movement, and visual identity.
- Candidate screen: Nimba Otter-shrew, White-winged Flufftail, and St Helena Ebony spanned Mammals, Birds, and Plants. The selected mammal ranked first for international unfamiliarity, the sensitive-whiskers-without-webbing discovery doorway, supported VU context, standard Japanese name, and a usable adult identity reference; the absent Mammals rotation slot was only a tie-breaker. Flufftail ranked lower because a stable closed-wing pose hides its white diagnostic feathers. St Helena Ebony was rejected because the accepted-name update and exact field-level IUCN assessment year remained unresolved.
- Duplicate gate: accepted scientific name, Pygmy Otter-shrew alias, English name, standard Japanese name, and slug were searched across Automation memory, memory registry, INDEX, package contents, and folder names. No completed collision was found; earlier occurrences were candidate-only.
- Locked discovery: a small forest-stream hunter uses sensitive whiskers and an enlarged upper lip to locate prey underwater despite lacking webbed feet and a broad paddle tail.
- Artifacts and QA: four canonical `1024x1536` poster PNGs, eight synchronized sidecars, one archived adult identity reference, Copy Lock, prompts, README, and Sources QA are synchronized. Both direct sources, X format, package validation, full-size and `360x540` phone-size review, pixel identity, natural occlusion, unwebbed feet, thin-tail identity, false-silhouette, card, and composition QA pass.

## Recent-Eight Completed Region Rotation

1. 2026-08-25 — Analalava District, northwestern Madagascar / Africa — Tahina Palm
2. 2026-08-26 — Deserta Grande, Madeira archipelago, Portugal / Europe — Desertas Wolf Spider
3. 2026-08-27 — Roatán, Barbareta, and nearby cays, Bay Islands, Honduras / Central America and the Caribbean — Roatán Spiny-tailed Iguana
4. 2026-08-28 — Cebu Island, Philippines / Asia — Cebu Flowerpecker
5. 2026-08-29 — Vâlsan River, Argeș basin, Romania / Europe — Asprete
6. 2026-08-30 — Lake Oku, Cameroon Highlands, Cameroon / Africa — Lake Oku Clawed Frog
7. 2026-08-31 — windward Ko'olau Mountains, O'ahu, Hawai'i / Oceania — Oceanic Hawaiian Damselfly
8. 2026-09-01 — Mount Nimba and the Putu Range, West Africa / Africa — Nimba Otter-shrew

Africa occupies three of the latest eight and Europe two; Central America and the Caribbean, Asia, and Oceania each occupy one. The retired 2026-08-21 duplicate does not fill a slot.

## Recent-Eight Completed Classification Rotation

1. 2026-08-25 — Plants — Tahina Palm
2. 2026-08-26 — Other invertebrates — Desertas Wolf Spider
3. 2026-08-27 — Reptiles — Roatán Spiny-tailed Iguana
4. 2026-08-28 — Birds — Cebu Flowerpecker
5. 2026-08-29 — Fishes — Asprete
6. 2026-08-30 — Amphibians — Lake Oku Clawed Frog
7. 2026-08-31 — Insects — Oceanic Hawaiian Damselfly
8. 2026-09-01 — Mammals — Nimba Otter-shrew

Plants, Other invertebrates, Reptiles, Birds, Fishes, Amphibians, Insects, and Mammals each occupy one slot; Fungi and lichens is absent. The retired 2026-08-21 duplicate does not fill a slot.

## Daily Quality Loop Counters

- `#duplicate-topic-gate`: 0 material catch this run. Full-history screening found no completed collision; all prior mentions of the selected species were candidate-only.
- `#IUCN-unavailable`: 1 bounded rendering occurrence. The current detail page and DOI endpoint did not render their assessment body, so the exact formal assessment, official IUCN 2018-2 category-change table, and IUCN SSC matching record were used and the caveat was disclosed.
- `#assessment-year-drift`: 0. Public copy uses the 2017 assessment year, not the 2018 publication/release year.
- `#image-text-error`: 0. Both first-pass posters render exact Copy Lock with exactly three numbered illustrated cards.
- `#species-identity-drift`: 0. Both accepted adults preserve a compact uniform dark body, low natural pose, unwebbed feet, and a long thin non-paddle tail.
- `#workflow-friction`: 1 brief occurrence. The sandboxed reference-photo download was blocked by network policy; one approved retry succeeded and the verified local copy was reused.

## Next Concrete Change

- No unfinished package remains. The next daily run may screen a new topic after the full-history duplicate gate.
- Keep `2026-09-01-nimba-otter-shrew` at `completed, published`; package content commit `327561a` was remotely verified.
- For small dark mammals, pair one verified adult identity reference with the exact false silhouettes and absent aquatic adaptations before the first prompt; natural far-limb occlusion remains acceptable.
- Latest-eight rotation: Africa three, Europe two, Central America and the Caribbean one, Asia one, and Oceania one; the eight groups present are Plants, Other invertebrates, Reptiles, Birds, Fishes, Amphibians, Insects, and Mammals. Fungi and lichens is absent.
