# Automation 2 Current State

Updated: 2026-08-27T23:52:34+09:00

This file is the small replace-in-place state record for Automation `automation-2`. Run history remains in Automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English Image Gen posters, species-specific illustrated observation cards, and an editorial review of X copy.
- Pending evidence package: none.
- Active package: none.
- Active state: idle after `2026-08-27-roatan-spiny-tailed-iguana` completed local-ready. The earlier 2026-08-21 Montseny Brook Newt attempt remains retired and does not count as completed.
- Active evidence: none. The Roatán Spiny-tailed Iguana's formal IUCN assessment reproduction and DOI confirm Global EN under B1ab(v)+2ab(v), assessed 5 June 2018; the current official page body returned 403, and the bounded access caveat is disclosed.
- Retired package: `2026-08-21-montseny-brook-newt`, an exact duplicate of the completed and published `2026-06-26-montseny-brook-newt` package. Do not post or publish it.
- The canonical package write gate is available.

## Latest Completed Package

- Package: `2026-08-27-roatan-spiny-tailed-iguana`.
- Topic: Roatán Spiny-tailed Iguana / ロータントゲオイグアナ / *Ctenosaura oedirhina*.
- State: `completed, local-ready`.
- Region: Roatán, Barbareta, and nearby cays, Bay Islands, Honduras / Central America and the Caribbean.
- Editorial classification group: Reptiles.
- Evidence: formal IUCN assessment `T44191A122558520` records Global Endangered under B1ab(v)+2ab(v), assessed 5 June 2018 and published in 2019. The current official page body returned 403, so the complete formal assessment reproduction and exact DOI were checked against the IUCN SSC Iguana Specialist Group and official IUCN action plan. ITIS, the Reptile Database, the original description, WWF Japan, and peer-reviewed habitat and diet studies support the accepted names, rounded snout, low crest, absent large dewlap, continuous ring-spined tail, island habitat breadth, and primarily herbivorous diet with varied animal items.
- Duplicate gate: normalized accepted name, historical *Ctenosaura bakeri* and *Enyaliosaurus bakeri* combinations, incorrect `Ctenosaura oederhina` spelling, English names, Japanese name, and proposed slug were searched across Automation memory, the memory registry, all INDEX sections, package contents, and folder names before Evidence Lock; no completed collision was found. Keel-scaled Boa was rejected for repeated small-boa silhouette risk against Rubber Boa; White-winged Flufftail remained candidate-screen-only.
- Locked discovery: on sunlit Caribbean limestone, a dark island iguana is recognized by a rounded nose, low crest, and a long tail armored in rings of enlarged spines.
- Visual resolution: the first Japanese direct poster and first English companion both passed without retry. Each has one complete dominant adult, four coherent limbs with natural far-side occlusion, a continuous pelvis-origin ring-spined tail, exact Copy Lock, connected island habitat, and three species-specific illustrated cards.
- Artifacts and QA: four canonical `1024x1536` PNGs, eight synchronized sidecars, three authoritative visual references, Copy Lock, prompts, README, Sources QA, and INDEX are synchronized. Both direct sources, X format, package validation, full-size and `360x540` phone-size review, pixel identity, whitespace, limb topology, false-silhouette, and composition QA pass.
- GitHub closeout: not attempted. The package remains `completed, local-ready` for a separate explicitly requested publication step.

## Recent-Eight Completed Region Rotation

1. 2026-08-20 — Central-western Queensland, Australia / Oceania — Redfin Blue-eye
2. 2026-08-21 — Amboli, Maharashtra, northern Western Ghats, India / Asia — Amboli Lateritic Toad
3. 2026-08-22 — Frégate Island, Seychelles / Africa — Frigate Island Giant Tenebrionid Beetle
4. 2026-08-23 — Torricelli Mountains, Sandaun Province, Papua New Guinea / Oceania — Tenkile
5. 2026-08-24 — Pacific Northwest of the United States / North America — Noble Polypore
6. 2026-08-25 — Analalava District, northwestern Madagascar / Africa — Tahina Palm
7. 2026-08-26 — Deserta Grande, Madeira archipelago, Portugal / Europe — Desertas Wolf Spider
8. 2026-08-27 — Roatán, Barbareta, and nearby cays, Bay Islands, Honduras / Central America and the Caribbean — Roatán Spiny-tailed Iguana

Africa and Oceania each occupy two of the latest eight; Asia, North America, Europe, and Central America and the Caribbean each occupy one. The retired 2026-08-21 duplicate does not fill a slot.

## Recent-Eight Completed Classification Rotation

1. 2026-08-20 — Fishes — Redfin Blue-eye
2. 2026-08-21 — Amphibians — Amboli Lateritic Toad
3. 2026-08-22 — Insects — Frigate Island Giant Tenebrionid Beetle
4. 2026-08-23 — Mammals — Tenkile
5. 2026-08-24 — Fungi and lichens — Noble Polypore
6. 2026-08-25 — Plants — Tahina Palm
7. 2026-08-26 — Other invertebrates — Desertas Wolf Spider
8. 2026-08-27 — Reptiles — Roatán Spiny-tailed Iguana

Fishes, Amphibians, Insects, Mammals, Fungi and lichens, Plants, Other invertebrates, and Reptiles each occupy one slot; Birds is absent. The retired 2026-08-21 duplicate does not fill a slot.

## Daily Quality Loop Counters

- `#duplicate-topic-gate`: 1 historical material failure remains recorded. This run applied the full accepted-name, historical-combination, incorrect-spelling, English-name, Japanese-name, slug, INDEX, memory, content, and folder collision gate before Evidence Lock and found zero completed *Ctenosaura oedirhina* collision.
- `#IUCN-unavailable`: 0 unresolved. The current page body returned 403, but the complete formal assessment reproduction and exact DOI directly confirmed category, criteria, and assessment date; the IUCN SSC Iguana Specialist Group and official action plan matched the route, and the bounded access caveat is public.
- `#assessment-year-drift`: 0. The public footer uses the 2018 assessment year, not the 2019 publication year.
- `#image-text-error`: 0. Both first-pass posters rendered the title, scientific name, all three card labels, and footer exactly once and inside the intended regions.
- `#species-identity-drift`: 0. Both accepted posters passed rounded-snout, low-crest, absent-large-dewlap, four-limb, continuous-ring-spined-tail, charcoal-and-cream-mottling, limestone-habitat, false-silhouette, text, and card QA against three authoritative references.
- `#workflow-friction`: 1 one-off occurrence, resolved. The canonical X validator removes the accented `á` when deriving the required hashtag; both main posts use its compatible `#RoatnSpinytailedIguana` form.

## Next Concrete Change

- Begin the next scheduled run with no unfinished package.
- Region rotation is Africa two, Oceania two, Asia one, North America one, Europe one, and Central America and the Caribbean one; use it only after unfamiliarity, evidence, discovery strength, naming, and visual viability.
- Birds is absent from the latest eight editorial groups and may break a tie among equally strong candidates.
- Before screening evidence, normalize and search each candidate's accepted scientific name, English name, Japanese name, aliases, and proposed slug across Automation memory, all INDEX sections, and package folder names. Any completed collision is a hard rejection.
- Keep the retired Montseny package as a duplicate and visual-risk exclusion; do not revive it without an explicit user request.
- When authoritative pages expose many visual assets, inspect the inventory first and bundle only the adult-habit, diagnostic-structure, and habitat references needed for Image Gen.
- When the English common name contains a diacritic, precompute the validator-derived English-name hashtag before drafting both X main posts.
- Keep future Quality Runs local-ready until GitHub publication is explicitly requested and remotely verified.
