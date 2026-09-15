# Kauaʻi Cave Wolf Spider bilingual infographic package

State: `completed, local-ready`

Workflow mode: Quality Run

Editorial classification group: Other invertebrates

Broad native region: Kōloa Basin, Kauaʻi, Hawaiʻi / Oceania

## Posting sets

- [日本語の投稿セット](x-post-ja.md)
- [English posting set](x-post-en.md)

## Poster files

- Japanese direct Image Gen poster: [adelocosa_anops_japanese_imagegen_2026-09-15.png](images/adelocosa_anops_japanese_imagegen_2026-09-15.png)
- Japanese posting PNG: [adelocosa_anops_japanese_posting_2026-09-15.png](images/adelocosa_anops_japanese_posting_2026-09-15.png)
- English direct Image Gen poster: [adelocosa_anops_english_imagegen_2026-09-15.png](images/adelocosa_anops_english_imagegen_2026-09-15.png)
- English posting PNG: [adelocosa_anops_english_posting_2026-09-15.png](images/adelocosa_anops_english_posting_2026-09-15.png)

## Copy-ready sidecars

- Japanese: [main post](images/adelocosa_anops_japanese_posting_2026-09-15.caption.txt), [story reply](images/adelocosa_anops_japanese_posting_2026-09-15.story-reply.txt), [ALT text](images/adelocosa_anops_japanese_posting_2026-09-15.alt.txt), [source note](images/adelocosa_anops_japanese_posting_2026-09-15.source-note.txt)
- English: [main post](images/adelocosa_anops_english_posting_2026-09-15.caption.txt), [story reply](images/adelocosa_anops_english_posting_2026-09-15.story-reply.txt), [ALT text](images/adelocosa_anops_english_posting_2026-09-15.alt.txt), [source note](images/adelocosa_anops_english_posting_2026-09-15.source-note.txt)

## Evidence and production files

- [Evidence Lock and Sources QA](sources-qa.md)
- [USFWS exact-taxon parent and spiderlings reference](evidence/adelocosa_anops_usfws_spiderlings_2005.webp)
- [USFWS 2022 five-year review](evidence/adelocosa_anops_usfws_5year_review_2022.pdf)
- [IUCN 1996 assessment PDF](evidence/iucn_adelocosa_anops_assessment_1996.pdf)
- [IUCN Red List page capture](evidence/iucn_adelocosa_anops_page_capture_2026-09-15.png)
- [Superseded U.S.-ESA-footer posters](evidence/superseded-us-esa-footer-posters/)
- [Japanese Copy Lock](infographic-copy-ja.md)
- [English Copy Lock](infographic-copy-en.md)
- [Japanese Image Gen prompt](image-prompt-ja.md)
- [English Image Gen prompt](image-prompt-en.md)

## Locked scope

- Accepted name: *Adelocosa anops* Gertsch, 1973.
- English public name: Kauaʻi Cave Wolf Spider.
- Japanese public name: カウアイ洞窟オオカミグモ, a transparent rendering rather than a claimed standardized Japanese arachnid-list name.
- Status: Global Endangered (EN) under IUCN criterion B1+2c, assessed 1 August 1996 in record `T513A13058776` and annotated `Needs Updating`. The final 2022 USFWS five-year review separately retains Endangered status under the U.S. Endangered Species Act.
- Public claims: adults have no eyes; unusually long sensory hairs occur on the front legs and feet; an official exact-taxon photograph records newly hatched spiderlings on a parent's back.
- Discovery doorway: a wolf spider crosses humid lava in darkness with no eyes at all.

## Production result

- Evidence Lock and bilingual cards-v2 Copy Lock were reopened and completed against the user-supplied official IUCN PDF and matching page capture.
- The IUCN assessment, one visibly screened public-domain USFWS exact-taxon reference and the package-local 2022 five-year review are retained. The IUCN record controls the global footer; USFWS supplies separate current U.S. legal and biological context.
- The first Japanese generation passed the direct-source gate and established the accepted composition, but its footer converted the locked fullwidth Japanese colon and parentheses to ASCII and Card 3 gave the pale spiderlings dark eye-like dots. One targeted Image Gen edit removed the dots while preserving the hero and layout; it retained the ASCII footer punctuation. A deterministic local text-safe repair replaced only the footer card with the exact locked string. Selected prompt: [image-prompt-ja.md](image-prompt-ja.md), plus the recorded targeted edit and local footer repair.
- The first English companion generation passed the direct-source and visual gates without retry. Its typographic apostrophe is recorded as the natural curly form in Copy Lock. Selected prompt: [image-prompt-en.md](image-prompt-en.md).
- The official-evidence correction replaced only the quiet status band in each accepted direct poster. A first Image Gen correction candidate was rejected because pixel comparison showed a 98.58% canvas redraw. The accepted localized repairs changed 0.93555% of Japanese pixels and 1.21695% of English pixels, with zero differences outside the status bands. Superseded U.S.-ESA-footer PNGs remain under `evidence/superseded-us-esa-footer-posters/`.
- Both direct sources and posting PNGs are exact `1024x1536`; each posting file is pixel-identical to its accepted direct source.

## Final QA

- Both posters show one lone adult *Adelocosa anops* with a smooth eye-free reddish-brown carapace, pale abdomen and four coherent pairs of orange-brown legs on damp porous lava. The lower black reflective mouthparts remain correctly separated from the eye-free carapace.
- Exactly three numbered illustrated cards show the eye-free head, attached front-leg sensory hairs and a complete parent carrying pale unmarked spiderlings. Every heading and explanation remains paired with its own art.
- Full-size and `360x540` phone-size review confirm readable hierarchy, an unobstructed hero, species-specific cave composition and no unsafe crop. Both corrected IUCN footers remain visually integrated inside the original footer positions.
- The posters do not drift into an eyed wolf spider, tarantula, harvestman, insect, whip spider, web-building scene, duplicated hero or horror composition.
- Eight UTF-8 sidecars match the four fenced blocks in each primary posting set. Direct-source, bilingual X-format, full-package, dimension, pixel-identity, card, composition, typography and species-identity QA pass.
- State is `completed, local-ready` after official-IUCN synchronization. Git, GitHub and X remain unchanged.
