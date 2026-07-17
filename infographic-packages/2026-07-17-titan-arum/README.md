# Titan Arum / ショクダイオオコンニャク

*Amorphophallus titanum* — discovery-first natural-history package for 2026-07-17.

## Copy-Ready Posting Sets

- [日本語の投稿セット](x-post-ja.md)
- [English posting set](x-post-en.md)

## Status

- Evidence Lock: complete.
- Copy Lock: complete.
- Visual production: complete.
- Final QA: passed.
- Publication state: completed, published. Package commit `75e52fa` was pushed to `origin/master`; this metadata is recorded in a dedicated follow-up commit.

## Why this subject

Asia had no appearance in the latest eight completed packages. Titan arum adds a flowering-plant lineage, a Sumatran lowland-rainforest habitat, and a discovery hook that is both visual and accurate: its spectacular display is a single inflorescence of many tiny flowers, and a bloom uses heat and scent to attract insect pollinators.

## Evidence and wording

- Accepted Japanese name, taxonomy, habitat, anatomy, and pollination wording are recorded in [sources-qa.md](sources-qa.md).
- The quiet footer is `IUCN Red List 2018: Endangered (EN)`.
- A user-provided official IUCN assessment PDF directly confirms Global scope, Endangered (EN), Year Published 2018, and Date Assessed 25 April 2018 on pages 1–2. The exact evidence and earlier page-access process history are recorded in [sources-qa.md](sources-qa.md); public source notes use the direct PDF basis without an access caveat.

## Locked production files

- [Japanese infographic copy](infographic-copy-ja.md)
- [English infographic copy](infographic-copy-en.md)
- [Japanese Image Gen prompt](image-prompt-ja.md)
- [English Image Gen prompt](image-prompt-en.md)

## Copy-Ready Posting Files

Posting sidecars are created beside each accepted posting PNG during final visual production.

- [Japanese caption](images/titan_arum_japanese_posting_2026-07-17.caption.txt)
- [Japanese ALT text](images/titan_arum_japanese_posting_2026-07-17.alt.txt)
- [Japanese source note](images/titan_arum_japanese_posting_2026-07-17.source-note.txt)
- [English caption](images/titan_arum_english_posting_2026-07-17.caption.txt)
- [English ALT text](images/titan_arum_english_posting_2026-07-17.alt.txt)
- [English source note](images/titan_arum_english_posting_2026-07-17.source-note.txt)

## Planned assets

- [Direct Japanese Image Gen poster](images/titan_arum_japanese_imagegen_2026-07-17.png)
- [Direct English Image Gen poster](images/titan_arum_english_imagegen_2026-07-17.png)
- [Japanese posting PNG](images/titan_arum_japanese_posting_2026-07-17.png)
- [English posting PNG](images/titan_arum_english_posting_2026-07-17.png)

## Completion and QA notes

- Both accepted direct Image Gen posters are exact vertical 2:3 at 1024x1536. Each was normalized with the bundled workspace Python to its exact 1024x1536 posting PNG; the direct/posting pixel pairs are identical, with no padding, cropping, stretching, or border repair.
- Local visual QA and the reused read-only verifier confirm one correct titan arum per poster: pale yellow-green spadix, deeply pleated burgundy spathe, green/cream exterior, Sumatran limestone-rainforest context, three numbered note cards, and no Rafflesia/lily/mushroom/carnivorous-plant confusion or simultaneous large leaf.
- All visible poster text matches Copy Lock. The six posting sidecars are synchronized with the three fenced blocks in each combined posting set.
- The bundled Python X-post validator and package validator passed; strict UTF-8 checks, dimensions, pixel identity, and `git diff --check` also passed.
- No text-safe backup or mirror was needed. No Git operation was attempted; GitHub publishing needs an approval-enabled normal conversation.
