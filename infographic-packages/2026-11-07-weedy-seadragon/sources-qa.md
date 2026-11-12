# Sources and QA — Weedy Seadragon

## Topic diversity and candidate slate

Recent eight span Reptiles, Other invertebrates, Amphibians, Mammals, Birds, Other invertebrates, Plants, and Fishes. This is a second fish after the freshwater butterflyfish, but it adds a marine temperate macroalgae habitat, a narrow syngnathid silhouette, male egg-bearing, and camouflage rather than a surface-water escape mechanism.

| Candidate | Group / habitat / hook | Evidence and duplicate screen | Decision |
|---|---|---|---|
| Weedy Seadragon (*Phyllopteryx taeniolatus*) | Fishes; southern Australian kelp and seagrass; male carries eggs beneath tail | Current official IUCN assessment directly indexed; Australian Museum and Fishes of Australia support form and breeding. Full-history aliases/common names/slug checked. | Selected |
| Sun Bear (*Helarctos malayanus*) | Mammals; Southeast Asian forest; long tongue | Official current record route returned 403 in this run; not used as a fallback-status package. | Not selected |
| Pink Fairy Armadillo (*Chlamyphorus truncatus*) | Mammals; Argentine sand; movable dorsal armour | Available status evidence was older/indirect during screening; no Evidence Lock. | Not selected |

## Evidence Lock

- Exact taxon and accepted public name: *Phyllopteryx taeniolatus* (Weedy Seadragon; Japanese common rendering used here: ウィーディー・シードラゴン). Australian Museum also uses “Common Seadragon”; naming variation is recorded here only.
- Lineage: Animalia > Chordata > Actinopterygii > Syngnathiformes > Syngnathidae > *Phyllopteryx* > *P. taeniolatus*.
- IUCN check: confirmed via official direct indexed assessment. Global Vulnerable (VU), criterion A2bc, assessed 05 July 2024 and published 2025; record `T17177A263199517`. The source DOI is used in the public source reply.
- Range and setting: southern Australian coast and Tasmania; shallow marine vegetation/reef habitat. IUCN’s current assessment gives Australia and 0–50 m; Australian Museum supplies the macroalgae/seagrass setting.
- Claim 1: males brood eggs on the underside of the tail; Australian Museum and Fishes of Australia describe male brood/nourishment of developing eggs. Copy says only that the brood area supports development, not a duration or egg count.
- Claim 2: leaf-like appendages disrupt the outline among vegetation; the official assessment and Australian Museum identify the appendages/seaweed-like appearance. Copy avoids claiming that they are actual leaves or the sole function.
- Claim 3: small fins provide slow movement and the tubular snout takes small crustaceans; Australian Museum and Fishes of Australia support the anatomy/diet. No feeding-rate or universal prey claim.

## Visual identity brief

- Individual/stage: adult, sex unspecified for hero. The first card shows an explicitly male tail study because brood eggs are sex-specific.
- Biological identity references: Australian Museum species page for horse-like head, narrow elongated body, appendages and male egg-bearing; Fishes of Australia species page for small dorsal/pectoral fins, tubular mouth, kelp/seagrass habitat and breeding.
- Diagnostic invariants: (1) long narrow, angular bony trunk; (2) horse-like head with a long tubular snout; (3) sparse, simple flat oval dermal flaps on head, body and tail spines, not branched fronds or a dense leafy cloak; reddish-orange to purplish body with fine yellow spots and bluish trunk bars (Fishes of Australia); (4) small dorsal fin on the back and small pectoral fin behind the head; (5) curled prehensile tail. Egg row appears only under the male tail study.
- Natural pose: lateral swimming profile, with the far pectoral fin naturally hidden. Do not add large paired wings, a seahorse-like upright body, or a full-body blanket of leaf appendages.
- False silhouette: not Leafy Seadragon (*Phycodurus eques*), whose body is densely draped in large leaf-like lobes; not a seahorse, which normally holds a much more upright trunk.

## Copy Lock and art direction

Copy format is `cards-v2`; the three locked claims are recorded in the language-paired copy files and verbatim prompt blocks. The main-post hook adds male egg-bearing; the story continues to the outline/camouflage and feeding sequence beyond any one card.

Style/medium (2026-11-12 replacement): soft natural-history watercolour in sunlit ultramarine-to-teal water, chosen because the reddish-orange body and pale oval flaps stand out against blue-green kelp while keeping the sparse-flap silhouette legible. Superseded 2026-11-07 choice: a deep ultramarine-to-teal cyanotype-and-coloured-pencil marine field plate was selected because sparse copper contours make the seadragon’s thin body, small fins and attached frills readable against a dark kelp habitat without treating the animal as a cartoon dragon.

## Source links

1. [IUCN Red List assessment DOI](https://doi.org/10.2305/IUCN.UK.2025-1.RLTS.T17177A263199517.en) — Global VU, A2bc, 2024 assessment/2025 publication.
2. [Australian Museum: Common/Weedy Seadragon](https://australian.museum/learn/animals/fishes/weedy-seadragon-phyllopteryx-taeniolatus/) — form, male brood and setting.
3. [Fishes of Australia: *Phyllopteryx taeniolatus*](https://fishesofaustralia.net.au/home/species/3127) — taxonomy, ecology and reproduction.

## Visual QA record

- Mechanical pre-image validation: pending image composition at time of this lock.
- Image-generation availability: following the user's plan change, the built-in image-generation tool was not available to this run. The selected posters are therefore deterministic original scientific illustrations/typeset layouts produced locally, not represented as a model-generated artwork.
- Acceptance target: full size and 342×513 phone review must confirm the five invariants, three illustrated cards, exact locked text, dark-water medium coherence and readable footer in both languages.
- Explicit user adoption: none requested or inferred.

### Replacement review — 2026-11-12

- Provenance: the user ran ChatGPT image generation from the current image-prompt-ja.md, then produced the English companion from image-prompt-en.md using the accepted Japanese poster as composition reference. The 2026-11-07 deterministic posters, posting PNGs and prompts are preserved in superseded-deterministic/.
- Rejected user draft: English title on the Japanese poster, missing IUCN footer, and many branched leafy lobes with yellow-green colouring closer to the Leafy Seadragon false silhouette. Corrections were written into both prompts.
- Tail check: an assistant remark that seadragon tails are not prehensile was checked against Fishes of Australia ("tail prehensile") and withdrawn; invariant (5) stands.
- Japanese: direct-source gate passed (1024×1536, exact 2:3). Title, scientific name, three headings/explanations and footer match Copy Lock. Hero shows long ringed trunk, horse-like head and tubular snout, few simple oval flaps on spines, small translucent dorsal and pectoral fins, no caudal fin, curled tail, reddish-orange body with yellow spots and bluish bars. Card 1 eggs attached under a male tail; card 2 outline broken among kelp; card 3 snout drawing in one mysid-like crustacean.
- English: same gate passed; all nine English strings match Copy Lock including footer punctuation spacing; hero and cards are the same accepted art.
- Visual observation: at 342×513 phone size the titles, headings and footer are clearly legible; card explanations are small but readable. Ventral flaps on downward spines read slightly limb-like at phone size; accepted as reference-consistent spine flaps, not legs.
- Posting PNGs are pixel-identical 1024×1536 copies of the direct sources; ALT text rewritten for the watercolour art and eight sidecars regenerated; full package QA passed.
