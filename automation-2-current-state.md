# Automation 2 Current State

Updated: 2026-08-20T22:08:53+09:00

This file is the small replace-in-place state record for Automation `automation-2`. Run history remains in Automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English Image Gen posters, species-specific illustrated observation cards, and an editorial review of X copy.
- Pending evidence package: none.
- Active package: none.
- Active state: idle after `2026-08-20-redfin-blue-eye` completed, published.
- Active evidence: official IUCN route `T19951A123379010` is Global CR under B1ab(iii,v)+2ab(iii,v), assessed 11 February 2019. The direct assessment body/PDF was blocked by Cloudflare in this run; the exact official DOI and ID were cross-checked against the current IUCN 2025-2 mirror and an independent exact-DOI citation. DCCEEW and AFD/ALA support the accepted identity and three locked claims.
- Retired package: none.
- The canonical package write gate is available.

## Latest Completed Package

- Package: `2026-08-20-redfin-blue-eye`.
- Topic: Redfin Blue-eye / レッドフィン・ブルーアイ / *Scaturiginichthys vermeilipinnis*.
- State: `completed, published`.
- Region: central-western Queensland, Australia / Oceania.
- Editorial classification group: Fishes.
- Evidence: official IUCN route `T19951A123379010` records Global Critically Endangered under B1ab(iii,v)+2ab(iii,v), assessed 11 February 2019. Its direct body/PDF was blocked by Cloudflare; the exact DOI and ID were cross-checked against the current IUCN 2025-2 mirror and an independent exact-DOI citation. DCCEEW and AFD/ALA support the accepted name, Edgbaston Springs range, wetlands less than 8 cm deep, maximum size about 3 cm, blue eye, and red fins displayed by breeding males.
- Locked discovery: in dry inland Queensland, a fish only about 3 cm long lives in clear spring water shallower than a hand is wide; breeding males add a brief flash of red to the shallows.
- Visual resolution: the first Japanese source and first English companion both passed without retry. Each uses one long olive-silver mature male with a blue-ringed eye and localized red fins across a coherent shallow desert-spring field note, with three unequal cards following the fish's horizontal body line.
- Artifacts and QA: four canonical `1024x1536` PNGs, eight synchronized sidecars, Copy Lock, prompts, README, Sources QA, and INDEX are synchronized. Both direct sources, X format, package validation, full-size and phone-size review, pixel identity, and whitespace QA pass.
- GitHub closeout: package commit `2cc16f3` was pushed directly to `origin/master` and the remote ref was verified at `2cc16f3769f27c4481d256427600350ff3bc76b0`; published-state metadata follows in the closeout commit.

## Recent-Eight Completed Region Rotation

1. 2026-08-13 — East Asia / Asia — Bekko Tombo
2. 2026-08-14 — Southern Tanzania / Africa — Kipunji
3. 2026-08-15 — Southeastern Australia and New Zealand South Island / Oceania — Tea-tree Fingers
4. 2026-08-16 — Mahé, Seychelles / Africa — Jellyfish Tree
5. 2026-08-17 — Tokashiki Island, Ryukyu Islands, Japan / Asia — Tokashiki Freshwater Crab
6. 2026-08-18 — Round Island, Mauritius / Africa — Günther's Gecko
7. 2026-08-19 — Southern China and Hainan through northern mainland Southeast Asia / Asia — White-eared Night Heron
8. 2026-08-20 — Central-western Queensland, Australia / Oceania — Redfin Blue-eye

Africa occupies three of the latest eight, Asia three, and Oceania two.

## Recent-Eight Completed Classification Rotation

1. 2026-08-13 — Insects — Bekko Tombo
2. 2026-08-14 — Mammals — Kipunji
3. 2026-08-15 — Fungi and lichens — Tea-tree Fingers
4. 2026-08-16 — Plants — Jellyfish Tree
5. 2026-08-17 — Other invertebrates — Tokashiki Freshwater Crab
6. 2026-08-18 — Reptiles — Günther's Gecko
7. 2026-08-19 — Birds — White-eared Night Heron
8. 2026-08-20 — Fishes — Redfin Blue-eye

Insects, Mammals, Fungi and lichens, Plants, Other invertebrates, Reptiles, Birds, and Fishes each occupy one slot; Amphibians is absent.

## Daily Quality Loop Counters

- `#source-access-caveat`: 1 bounded occurrence in this run. The direct IUCN body/PDF was blocked, but the exact official DOI and ID were cross-checked against the current IUCN 2025-2 mirror and an independent exact-DOI citation; both source replies disclose the caveat.
- `#assessment-year-drift`: 0 in this run. The public footer uses the assessment's field-level 2019 year exposed by the current mirror for the exact official record.
- `#species-identity-drift`: 0 in this run. Both first-pass posters preserve the government-photo-matched slender body, blue eye, localized red fins, and shallow desert-spring habitat.
- `#source-canvas-drift`: 0/2 canonical sources. Both accepted direct posters are exact 1024x1536, exact 2:3, and full-canvas.
- `#image-text-error`: 0 in this run. Both first-pass posters render all six locked lines and the specified ASCII spacing.

## Next Concrete Change

- Begin the next scheduled run with no unfinished package.
- Region rotation is balanced at Africa three, Asia three, and Oceania two; use it only after unfamiliarity, evidence, discovery strength, naming, and visual viability.
- Amphibians is absent from the latest eight editorial groups and may break a tie among equally strong candidates.
- Retry a direct IUCN assessment body once before Copy Lock. If the same exact route remains blocked, use one explicit bounded partner/fallback cross-check and disclose it in both source replies rather than expanding into a loose source pile.
- Keep the successful long-body composition lesson: let irregular cards follow the organism's silhouette and habitat flow instead of forcing three equal panels.
- Keep the next Quality Run local-ready until GitHub publication is explicitly requested and remotely verified.
