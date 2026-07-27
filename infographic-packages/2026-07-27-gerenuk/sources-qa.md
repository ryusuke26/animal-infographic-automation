# Sources and QA — Gerenuk

## Gate State

- Package state: `completed, local-ready`
- Topic Lock time: 2026-07-27T10:00:00+09:00
- Evidence Lock completed: 2026-07-27
- Copy Lock completed: 2026-07-27
- Run mode: Quality Run
- User IUCN Evidence Gate: passed on 2026-07-27 with the official species-page
  screenshot and matching ten-page assessment PDF

Evidence Lock and Copy Lock are complete. Public claims remain limited to the
locked items below.

## Evidence Lock

- Accepted scientific name: *Litocranius walleri* (Brooke, 1878)
- English name: Gerenuk
- Japanese standard name: ジェレヌク
- Native region: the Somali-Masai arid zone of the Horn of Africa and East
  Africa, from Djibouti, Ethiopia, and Somalia through Kenya to northern
  Tanzania
- Habitat: dry thornbush savanna and scrub
- Global status: IUCN Red List Near Threatened (NT)
- Assessment date: 20 April 2016
- Assessment/publication year: 2016
- Assessment identifier: `e.T12142A50190292`
- Official assessment DOI:
  https://doi.org/10.2305/IUCN.UK.2016-2.RLTS.T12142A50190292.en

IUCN check: confirmed directly from the user-supplied official species-page
screenshot and matching ten-page assessment PDF. The screenshot identifies
Gerenuk / *Litocranius walleri*, Near Threatened (NT), Global scope, and last
assessed 20 April 2016. PDF page 1 identifies the same taxon and assessment
`e.T12142A50190292`; page 2 confirms Near Threatened, year published 2016, and
date assessed 20 April 2016. Because the assessment is old, the public footer
names 2016 and makes no claim that the status is recent.

## Preserved Official Evidence

- [Official IUCN species-page screenshot](evidence/iucn_gerenuk_user_screenshot_2026-07-27.png)
  - SHA-256:
    `AE22B545AD5E0B543C498F65C18DB7142D4F6CAA55F666C8D116E1EC803B48A0`
- [Official IUCN assessment PDF](evidence/iucn_gerenuk_user_pdf_2026-07-27.pdf)
  - SHA-256:
    `AA7F7A63295385226495C648C33C07B9AFFA27FCBFC923083F584058325C1F0F`

## Source Set

1. IUCN SSC Antelope Specialist Group 2016, *Litocranius walleri*,
   `e.T12142A50190292`:
   https://doi.org/10.2305/IUCN.UK.2016-2.RLTS.T12142A50190292.en
2. National Museum of Nature and Science, specimen NSMTM32286, with the
   Japanese Mammal Society standard name and linked IUCN metadata:
   https://yoshimoto.kahaku.go.jp/3d/NSMTM32286/
3. Hammer et al. 2021, *Litocranius walleri (Artiodactyla: Bovidae)*,
   *Mammalian Species* 53(1005):65–77:
   https://doi.org/10.1093/mspecies/seab007

## Copy Lock

- Japanese title: ジェレヌク
- English title: Gerenuk
- Scientific name: *Litocranius walleri*
- Japanese observation 1: `東アフリカの 乾いたトゲやぶにすむ`
- Japanese observation 2: `長い首と脚 大きな耳と白い目の輪`
- Japanese observation 3: `後ろ脚で立ち 枝先の葉を食べる`
- Japanese footer: `IUCN Red List 2016：準絶滅危惧（NT）`
- English observation 1: `Lives in East Africa's dry thornbush`
- English observation 2: `Long neck and legs, large ears, white eye rings`
- English observation 3: `Stands on hind legs to browse high leaves`
- English footer: `IUCN Red List 2016: Near Threatened (NT)`
- Public population number, trend, ranked threat, legal status, and urgency:
  omitted

## Claim Check

| Claim | Verdict | Correction / evidence | Confidence |
|---|---|---|---|
| *Litocranius walleri* / Gerenuk / ジェレヌク | accurate | National Museum of Nature and Science links the Japanese Mammal Society standard name to the accepted taxon; the monograph and IUCN assessment use the same taxon | High |
| Global IUCN Near Threatened (NT), assessed and published 2016 | accurate | Official species-page screenshot and matching PDF directly confirm Global NT, assessed 20 April 2016 and published 2016 | High |
| Dry thornbush of the Horn of Africa and East Africa | accurate | 2021 *Mammalian Species* monograph | High |
| Very elongated neck, legs, ears, white eye rings, and male lyre-shaped horns | accurate | 2021 *Mammalian Species* diagnosis and general characters | High |
| Frequently stands on its hind legs to browse leaves up to about two metres high | accurate | 2021 *Mammalian Species* diagnosis | High |

## Publication-Safe Copy

The public package uses exactly three claims: dry East African thornbush
habitat, the long-necked and white-eye-ringed silhouette, and bipedal browsing.
The 2016 IUCN footer is quiet and separate from the discovery-first copy.

## Visual Identity Guidance

- Show exactly one adult male Gerenuk standing upright on its hind legs while
  browsing a thorny shrub in natural dry East African scrub.
- Keep the entire slim tan body visible: very long neck and legs, small narrow
  head, large ears, broad white eye rings, dark preorbital marks, white lips and
  throat, darker brown back saddle, pale belly, black knee tufts, black-tipped
  tail, and ringed lyre-shaped horns.
- Keep both hind feet planted, both forelegs raised, and all four limbs
  anatomically attached and readable.
- Surround it with sparse acacia-like thorn scrub, warm dry soil, grasses, and
  distant low bush; no fake map.
- Do not make a giraffe, dik-dik, impala, springbok, kudu, goat, deer, or
  generic gazelle.
- Do not add giraffe patches, branched antlers, spiral kudu horns, extra
  animals, duplicated limbs, detached horns, logos, signatures, or watermarks.

## Final Visual and Mechanical QA

- Quality Run direct-poster production: completed
- Japanese direct poster: accepted on first generation
- English direct poster: accepted after one unsuccessful targeted retry and a
  one-glyph local text-safe repair for the locked ASCII apostrophe
- One hero organism and complete diagnostic anatomy: passed
- Exactly three numbered icon-bearing cards: passed
- Locked title, scientific name, three labels, and footer: passed
- Direct/posting PNG pairs exact 1024x1536 and pixel-identical: passed
- Six sidecars synchronized: passed
- Main-post identity sequence restored in both languages: passed
- Official screenshot/PDF evidence preservation and source-note sync: passed
- Final package validator: passed
