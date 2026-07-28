# Sources and QA — Kea

## Gate State

- Package state: `completed, local-ready`
- Topic Lock date: 2026-07-28
- Evidence Lock completed: 2026-07-28
- Copy Lock completed: 2026-07-28
- Run mode: Quality Run
- User IUCN Evidence Gate: passed on 2026-07-28 with the official species-page
  screenshot and matching 13-page assessment PDF

Evidence Lock and Copy Lock are complete. Public claims remain limited to the
locked items below.

## Evidence Lock

- Accepted scientific name: *Nestor notabilis* Gould, 1856
- English name: Kea
- Japanese name: ミヤマオウム
- Native region: New Zealand's South Island
- Habitat: native forest, subalpine scrub, tussock, herb-field, rocky outcrops,
  and alpine slopes
- Global status: IUCN Red List Endangered (EN)
- Criteria: A2be+4be
- Scope: Global
- Assessment date: 1 October 2017
- Assessment/publication year: 2017
- Assessment identifier: `e.T22684831A119243358`
- Official assessment DOI:
  https://doi.org/10.2305/IUCN.UK.2017-3.RLTS.T22684831A119243358.en

IUCN check: confirmed directly from the user-supplied official species-page
screenshot and matching 13-page assessment PDF. The screenshot identifies Kea
/ *Nestor notabilis*, most recently assessed in 2017, Endangered under criteria
A2be+4be, and Global scope. PDF page 1 confirms the taxon, Global scope,
Endangered category, citation, and assessment identifier. PDF page 2 confirms
Endangered A2be+4be, year published 2017, and date assessed 1 October 2017.
The public footer therefore remains `IUCN Red List 2017`.

## Preserved Official Evidence

- [Official IUCN species-page screenshot](evidence/iucn_kea_user_screenshot_2026-07-28.png)
  - SHA-256:
    `237AA16FB77F8D34A8A583E4E1202CD1E211E3E401260381E1940902E0F770D2`
- [Official IUCN assessment PDF](evidence/iucn_kea_user_pdf_2026-07-28.pdf)
  - SHA-256:
    `74FB09AAA8E29CC8653B7D9838DE2AE39594C26C5A12FC441B5AD01227CE2792`

## Source Set

1. BirdLife International 2017, *Nestor notabilis*, The IUCN Red List of
   Threatened Species 2017, user-supplied official screenshot and PDF:
   https://doi.org/10.2305/IUCN.UK.2017-3.RLTS.T22684831A119243358.en
2. New Zealand Department of Conservation, Kea species account:
   https://www.doc.govt.nz/nature/native-animals/birds/birds-a-z/kea/
3. New Zealand Birds Online, Kea species account:
   https://www.nzbirdsonline.org.nz/species/kea
4. Tamagawa University Educational Museum, specimen record for ミヤマオウム /
   *Nestor notabilis*:
   https://jmapps.ne.jp/tamagawa_museum2/det.html?data_id=57517

## Copy Lock

- Japanese title: ミヤマオウム
- English title: Kea
- Scientific name: *Nestor notabilis*
- Japanese observation 1: `南島の森から 高山まで暮らす`
- Japanese observation 2: `オリーブ色の羽 飛ぶと翼の下はオレンジ`
- Japanese observation 3: `くちばしと足で つつき、引き、確かめる`
- Japanese footer: `IUCN Red List 2017：絶滅危惧（EN）`
- English observation 1: `Forest to alpine slopes on South Island`
- English observation 2: `Olive plumage, vivid orange underwings`
- English observation 3: `Probes, pulls and explores with bill and feet`
- English footer: `IUCN Red List 2017: Endangered (EN)`
- Public population number, trend, ranked threat, legal status, and urgency:
  omitted

## Claim Check

| Claim | Verdict | Correction / evidence | Confidence |
|---|---|---|---|
| *Nestor notabilis* / Kea / ミヤマオウム | accurate | IUCN DOI, New Zealand sources, and the Tamagawa University museum record use the same taxon; the museum record supports the Japanese name | High |
| Global IUCN Endangered (EN), A2be+4be, assessed 1 October 2017 and published 2017 | accurate | Official species-page screenshot and matching assessment PDF directly confirm the category, criteria, Global scope, date, year, and assessment identifier | High |
| South Island forest through alpine habitat | accurate | New Zealand DOC and New Zealand Birds Online | High |
| Olive plumage with vivid orange-red underwings | accurate | New Zealand Birds Online identification account | High |
| Uses bill and feet to probe, pull, play, and investigate | accurate | New Zealand DOC describes exploration, object manipulation, and tool use; New Zealand Birds Online describes juvenile play and learning of complex foraging skills | High |

## Publication-Safe Copy

The public package uses exactly three claims: South Island forest-to-alpine
habitat, olive plumage with orange underwings, and exploratory manipulation
with the bill and feet. The 2017 IUCN footer is quiet and separate from the
discovery-first copy.

## Visual Identity Guidance

- Show exactly one adult Kea on a lichen-speckled alpine rock in natural
  alert, exploratory posture.
- Keep the complete large parrot visible: olive-green scalloped plumage, long
  slender strongly curved grey-black upper bill, dark eye and grey cere, dark
  legs, zygodactyl feet, narrow dark tail, and vivid orange-red underwing
  coverts.
- Let a gust lift one wing naturally enough to reveal the orange underwing
  while the other wing remains anatomically coherent and attached.
- Surround it with South Island alpine tussock, low subalpine scrub,
  greywacke-like rocks, distant snowy ridges, and cool mountain light.
- Do not make a kākā, kākāpō, generic green parrot, macaw, parakeet, or
  lorikeet.
- Do not use a bright red bill, blue head, owl-like facial disk, flightless
  body, rainbow plumage, duplicated wings or feet, detached feathers, extra
  hero birds, fake maps, logos, signatures, or watermarks.

## Current Visual and Mechanical QA

- Quality Run direct-poster production: completed
- Japanese direct poster: accepted on first generation
- English direct poster: accepted after one targeted footer-spacing correction
- One hero organism and complete diagnostic anatomy: passed
- Exactly three numbered icon-bearing cards: passed
- Locked title, scientific name, three labels, and footer: passed
- Direct/posting PNG pairs exact 1024x1536: passed
- Phone-size visual and legibility QA: passed
- Latest-two X opening comparison: passed after replacing the initial
  snow-walk opening with a species-specific object-exploration scene
- Six sidecars synchronized: passed
- Official screenshot/PDF evidence preservation and source-note sync: passed
- Final package validator: passed
