# Gerenuk Infographic Package

- Date: 2026-07-27
- Package state: `completed, published`
- Publication state: `published to GitHub`
- Workflow mode: Quality Run
- Workflow position: Phase 5 complete and published

## Topic Lock

- English common name: Gerenuk
- Japanese common name: ジェレヌク
- Scientific name: *Litocranius walleri*
- Broad native region: Africa
- Lineage: antelope family, Bovidae
- Habitat: dry thornbush savanna and scrub in the Horn of Africa and East Africa
- Curiosity hook: a long-necked antelope rises onto its hind legs to reach
  leaves above the ordinary browsing line

## Evidence Lock

- Global IUCN category: Near Threatened (NT)
- Assessment date: 20 April 2016
- Assessment/publication year: 2016
- Official assessment:
  https://doi.org/10.2305/IUCN.UK.2016-2.RLTS.T12142A50190292.en
- Japanese standard name and linked IUCN metadata:
  https://yoshimoto.kahaku.go.jp/3d/NSMTM32286/
- Taxonomy, habitat, visible identity, and bipedal browsing:
  https://doi.org/10.1093/mspecies/seab007

Evidence Lock and Copy Lock are complete. The user-supplied official IUCN
species-page screenshot and matching ten-page assessment PDF directly confirm
Gerenuk / *Litocranius walleri*, Global Near Threatened (NT), assessed 20 April
2016 and published in 2016. Public copy omits population numbers, trend, ranked
threats, legal status, blame, and urgency.

## Preserved Official Evidence

- [Official IUCN species-page screenshot](evidence/iucn_gerenuk_user_screenshot_2026-07-27.png)
  - SHA-256:
    `AE22B545AD5E0B543C498F65C18DB7142D4F6CAA55F666C8D116E1EC803B48A0`
- [Official IUCN assessment PDF](evidence/iucn_gerenuk_user_pdf_2026-07-27.pdf)
  - SHA-256:
    `AA7F7A63295385226495C648C33C07B9AFFA27FCBFC923083F584058325C1F0F`

## Primary Posting Sets

- [日本語の投稿セット](x-post-ja.md)
- [English posting set](x-post-en.md)

Combined Markdown files above are the primary copy surface. Plain-text sidecars
are synchronized backups:

- [Japanese caption](images/gerenuk_japanese_posting_2026-07-27.caption.txt)
- [Japanese ALT text](images/gerenuk_japanese_posting_2026-07-27.alt.txt)
- [Japanese source note](images/gerenuk_japanese_posting_2026-07-27.source-note.txt)
- [English caption](images/gerenuk_english_posting_2026-07-27.caption.txt)
- [English ALT text](images/gerenuk_english_posting_2026-07-27.alt.txt)
- [English source note](images/gerenuk_english_posting_2026-07-27.source-note.txt)

## Locked Copy

- [Japanese infographic copy](infographic-copy-ja.md)
- [English infographic copy](infographic-copy-en.md)
- [Japanese direct-poster prompt](image-prompt-ja.md)
- [English direct-poster prompt](image-prompt-en.md)

## Poster Assets

- [Japanese direct ImageGen PNG](images/gerenuk_japanese_imagegen_2026-07-27.png)
- [Japanese posting PNG](images/gerenuk_japanese_posting_2026-07-27.png)
- [English direct ImageGen PNG](images/gerenuk_english_imagegen_2026-07-27.png)
- [English posting PNG](images/gerenuk_english_posting_2026-07-27.png)

Rejected English generations are preserved for audit:

- [First English generation, curly-apostrophe drift](images/gerenuk_english_imagegen_rejected_text_2026-07-27.png)
- [Targeted English retry, same drift](images/gerenuk_english_imagegen_rejected_apostrophe_retry_2026-07-27.png)

## Image QA

- Japanese direct poster: accepted on the first generation.
- English first generation: rejected because `East Africa's` used a curly
  apostrophe instead of the locked ASCII apostrophe.
- One targeted English retry: rejected because the same glyph drift remained.
- Local text-safe repair: accepted after replacing only that apostrophe while
  preserving the integrated artwork and surrounding letterforms.
- Both accepted posters show one complete adult male Gerenuk in natural
  bipedal browsing posture with long neck and legs, large ears, broad white eye
  rings, ringed lyre-shaped horns, and a complete tail.
- Both hind feet, both raised forelegs, horns, ears, neck, and tail are visible
  and anatomically attached. The cards do not cover the hero silhouette.
- Exactly three irregular numbered cards appear in each poster. Every card has
  species-specific spot art and useful explanatory copy.
- Giraffe patches, branched antlers, spiral kudu horns, extra hero animals,
  duplicated or detached limbs, maps, logos, and watermarks are absent.
- Direct and posting PNGs are exact 1024x1536 and pixel-identical in each
  language.

## Final QA

- Pre-image validation: passed
- Japanese and English full-size visual QA: passed
- Phone-size coherence and legibility check: passed
- X format validation: passed
- Main-post sequence restored: hook, standalone common name, standalone
  scientific name, discovery story, quiet status footer
- Six posting sidecars: synchronized
- User-supplied official screenshot/PDF: preserved and propagated into source
  notes
- Full package validation: passed
- GitHub publishing: completed in package commit `901e65c`; narrative X
  workflow improvements were published in commit `17c6f88`
