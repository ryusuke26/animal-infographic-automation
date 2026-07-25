# Sources and QA — Pelican Eel

## Gate State

- Package state: `completed, published`
- Topic Lock time: 2026-07-25T12:09:08+09:00
- Evidence inspection time: 2026-07-25T12:47:06+09:00
- Evidence Lock completed: 2026-07-25T12:55:26+09:00
- Copy Lock completed: 2026-07-25
- Run mode: Caution Run because the species has a highly
  unusual and easy-to-distort mouth, pharynx, and tail silhouette

Evidence Lock and Copy Lock are complete. Public claims remain limited to the
locked items below.

## Copy Lock

- Japanese title: フクロウナギ
- English title: Pelican Eel
- Scientific name: *Eurypharynx pelecanoides*
- Japanese observation 1: `熱帯・温帯の 深い海にすむ`
- Japanese observation 2: `大きな口で 甲殻類や魚・イカを食べる`
- Japanese observation 3: `細長い尾の先に 小さな発光器がひとつ`
- Japanese footer: `IUCN Red List 2012：低懸念（LC）`
- English observation 1: `Lives deep in tropical and temperate oceans`
- English observation 2:
  `A huge mouth engulfs crustaceans, fish, and squid`
- English observation 3:
  `One tiny light organ tips its long tapering tail`
- English footer: `IUCN Red List 2012: Least Concern (LC)`
- X-post structure: canonical three fenced `text` blocks in each language
- Public population number, population trend, ranked threat, and
  legal-protection claims: omitted
- Local affirmative repair pass: passed
- Local critical stop-ship pass: passed
- X-post validator: passed
- Package pre-image validator: passed
- Image Gen permission: unlocked

## Final Visual and Mechanical QA

- Japanese direct source:
  `images/pelican_eel_japanese_imagegen_2026-07-25.png`
- English direct source:
  `images/pelican_eel_english_imagegen_2026-07-25.png`
- Both accepted direct sources: exact 1024x1536 vertical 2:3
- Japanese targeted retry: accepted after exposing the full attached tail and
  its single terminal light organ
- English first attempt: accepted
- Locked title, scientific name, three observation labels, and footer: visually
  present and correct in both posters
- One hero specimen and exactly three numbered illustrated note cards: passed
- Mouth/pharynx/tail silhouette and single tail-tip light organ: passed
- Bird beak, external pelican pouch, head lure, duplicate hero, rows of lights,
  extra glowing points, and fake map: absent
- Normalized posting PNGs: exact 1024x1536
- Direct/posting pixel identity: passed for both languages
- Six posting sidecars: synchronized with the three fenced X blocks in each
  language
- Final package validator: passed after README link repair

## Candidate Identity

- English common name: Pelican Eel
- Japanese common name: フクロウナギ
- Accepted scientific name: *Eurypharynx pelecanoides* Vaillant, 1882
- Broad native region: Ocean/Global
- Lineage: family Eurypharyngidae
- Habitat candidate: deep oceanic midwaters; widespread in tropical and
  temperate oceans
- Curiosity hook: enormous expandable mouth/pharynx, black tapering body, and
  a small light organ at the tail tip

Taxonomy and naming route:

- WoRMS lists *Eurypharynx pelecanoides* as accepted, AphiaID 127165, and lists
  フクロウナギ as a Japanese name:
  https://www.marinespecies.org/aphia.php?p=taxdetails&id=127165
- JAMSTEC BISMaL supports the family name フクロウナギ科 and the
  Eurypharyngidae lineage:
  https://www.godac.jamstec.go.jp/bismal/j/view/0002915

Order-level placement differs in the current reference displays
(`Anguilliformes` versus `Saccopharyngiformes`). Reconcile this during Phase 2
and omit the order from public copy unless it becomes useful and unambiguous.

## IUCN Evidence Route

- Official species page:
  https://www.iucnredlist.org/species/18227119/42691734
- IUCN taxon ID: `18227119`
- Assessment ID: `42691734`
- Assessment citation key: `e.T18227119A42691734`
- Official assessment DOI:
  https://doi.org/10.2305/IUCN.UK.2015-4.RLTS.T18227119A42691734.en
- Ordinary retrieval did not expose the current record body.
- The in-app Browser reached the exact official species URL on IUCN Red List
  version 2026-1, but the record body did not render.
- A reliable museum-backed fish reference cites Iwamoto (2015), assessment
  `e.T18227119A42691734`, and reports Least Concern. This is only an
  evidence-viability cross-check and is not yet the locked footer:
  https://fishesofaustralia.net.au/home/species/3300

IUCN check: confirmed via official IUCN species-page screenshot and matching
official IUCN PDF. The complete screenshot visibly confirms the accepted taxon,
Least Concern (LC), `Last assessed: 24 May 2012`, and
`Scope of assessment: Global`. The PDF independently confirms the taxon,
category, assessment date, publication year, citation, and assessment ID.

## Preserved Official Evidence

- `evidence/iucn_pelican_eel_assessment_2015.pdf`
  - copied from the user-supplied download without modifying the original
  - 8 pages
  - SHA-256:
    `F8739E51893CDA0F3F708314B15481B0A13D1696728CB4F35775126945E5D418`
- `evidence/iucn_pelican_eel_user_screenshot_2026-07-25.png`
  - copied from the user-supplied screenshot without modifying the original
  - SHA-256:
    `477433FC70627FABE701161A0F58B9BAE9931058863C5ECBB96347709DE089B7`
- `evidence/iucn_pelican_eel_user_screenshot_full_2026-07-25.png`
  - complete official page screenshot used for the gate decision
  - SHA-256:
    `F354A1882E838C6135241FC734B36D051EB123F5AEAA65BE683AFA0499A4710A`

### Inspected Fields

Initial screenshot:

- page title: Pelican Eel
- accepted taxon: *Eurypharynx pelecanoides*
- abstract: most recently assessed in 2012
- category: Least Concern (LC)
- citation row: Iwamoto, T. 2015, matching assessment identifier
- scope of assessment: Global
- missing from visible screenshot: labeled `Last assessed` field

Complete screenshot:

- page title: Pelican Eel
- accepted taxon: *Eurypharynx pelecanoides*
- category: Least Concern (LC)
- last assessed: 24 May 2012
- scope of assessment: Global
- matching Iwamoto 2015 assessment citation

Official PDF p.1:

- accepted taxon: *Eurypharynx pelecanoides*
- English common name: Pelican Eel
- assessor: Iwamoto, T.
- category: Least Concern (LC)
- citation: Iwamoto, T. 2015. *Eurypharynx pelecanoides*. The IUCN Red List of
  Threatened Species 2015: e.T18227119A42691734
- DOI:
  https://doi.org/10.2305/IUCN.UK.2015-4.RLTS.T18227119A42691734.en

Official PDF p.2:

- accepted taxon: *Eurypharynx pelecanoides* Vaillant, 1882
- order: Saccopharyngiformes
- family: Eurypharyngidae
- category and criteria: Least Concern, version 3.1
- year published: 2015
- date assessed: 24 May 2012
- range: circumglobal in tropical and temperate waters
- depth: 500-7,625 m, more typically 1,200-1,400 m in the cited assessment

Official PDF p.5:

- current population trend: Unknown
- system: Marine
- diet context: crustaceans, fish, and squid
- assessment threat statement: no current threats identified
- no species-specific conservation measures recorded

The PDF contains no literal Global-scope field. The complete screenshot supplies
`Scope of assessment: Global`, while the screenshot and PDF both supply the
exact assessment date. Together the official files fully satisfy the User IUCN
Evidence Gate.

## Evidence Lock

- Accepted name: *Eurypharynx pelecanoides* Vaillant, 1882
- English name: Pelican Eel
- Japanese name: フクロウナギ
- Native region: Ocean/Global; circumglobal tropical and temperate waters
- Status-source route: official IUCN screenshot plus official assessment PDF
- Global status: Least Concern (LC)
- Assessment date/year: 24 May 2012 / 2012
- Publication year: 2015
- Japanese footer: `IUCN Red List 2012：低懸念（LC）`
- English footer: `IUCN Red List 2012: Least Concern (LC)`

## Locked Core Public Claims

- Habitat: deep oceanic midwaters across tropical and temperate oceans; the
  IUCN assessment gives 500-7,625 m and says 1,200-1,400 m is more typical.
- Visible identity: an enormous mouth with a highly expandable pharynx on a
  long, black, scale-less, tapering body.
- Ecology/anatomy hook: it feeds on crustaceans, fish, and squid; the tail ends
  in one small pinkish light organ.

No population number, trend, ranked threat, or legal-protection claim is
proposed.

## Claim Check

| Claim | Verdict | Evidence | Confidence |
|---|---|---|---|
| Accepted taxon and names | accurate | official IUCN screenshot/PDF; WoRMS for フクロウナギ | High |
| Global LC, assessed 24 May 2012 | accurate | complete official screenshot and PDF pp.1-2 | High |
| Circumglobal tropical/temperate deep-water habitat | accurate | official PDF p.2 | High |
| Diet includes crustaceans, fish, and squid | accurate | official PDF p.5, citing Nielsen et al. 1989 | High |
| Enormous expandable mouth/pharynx and black scale-less body | accurate | Fishes of Australia morphology summary and cited references | Medium-High |
| One small pinkish light organ at the tail tip | accurate | Fishes of Australia morphology summary and cited references | Medium-High |

## Local Independent Evidence Check

- Accepted name, category, assessment date, Global scope, range, habitat,
  three public claims, source fit, and visual identity risks were checked
  locally after Evidence Lock.
- The initial screenshot-reading error was corrected using the complete
  screenshot supplied by the user.
- No unresolved evidence conflict remains.
- Caution Run remains appropriate for later visual QA because the mouth,
  pharynx, and tail silhouette are unusually easy to distort.

## Visual Identity Risks

- Do not depict a short-bodied ordinary eel with a normal narrow jaw.
- Do not turn the mouth into a pelican beak or add a bird-like pouch.
- Keep the skull and eyes small relative to the mouth.
- Keep the body very long, dark, soft-looking, and tapering.
- Place only one small light organ at the tail tip; do not add rows of lights.
- The exact open-mouth shape and tail silhouette must be checked against an
  authoritative reference before Image Gen acceptance.
