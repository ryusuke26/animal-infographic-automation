# Aardvark Infographic Package

Status: completed, published
Run date: 2026-07-14

## Rationale

Aardvark adds Africa, absent from the latest eight completed packages, without repeating the previous North America region. Tubulidentata, moonlit savanna/grassland, powerful digging claws, and sticky-tongue feeding provide a distinct lineage, habitat, and discovery hook.

## Locked Public Claims

1. Aardvarks forage after dark in sub-Saharan savannas and grasslands.
2. Powerful front claws open hard ant and termite nests.
3. A long sticky tongue gathers ants and termites.

## Locked Status Footer

- Japanese: `IUCN Red List 2014：低懸念（LC）`
- English: `IUCN Red List 2014: Least Concern (LC)`

The official IUCN page confirms LC, Global scope, and last assessed 21 January 2014. It was published in 2015 and is annotated `Needs updating`; both source replies disclose that age caveat.

## Review Notes

- Independent verifier trial marker was already present. The current caution trigger was an operational dependency-loader recurrence, which is now resolved and would not benefit from a second evidence reader; local evidence and copy checklists found no blocker.
- Evidence Lock and Copy Lock completed before Image Gen.
- Phase 3.5 local affirmative and critical copy reviews found no unresolved placeholder, status mismatch, unsupported public claim, naming label, or prompt/copy drift.

## Asset Status

- Japanese direct Image Gen poster: `images/aardvark_japanese_imagegen_2026-07-14.png`, 1024x1536, exact vertical 2:3, accepted
- English direct Image Gen poster: `images/aardvark_english_imagegen_2026-07-14.png`, 1024x1536, exact vertical 2:3, accepted
- Japanese posting PNG at 1024x1536: `images/aardvark_japanese_posting_2026-07-14.png`, normalized from the compliant direct source
- English posting PNG at 1024x1536: `images/aardvark_english_posting_2026-07-14.png`, normalized from the compliant direct source
- Text-safe backups: not planned unless needed
- Optional mirror: not attempted

## Copy-Ready Posting Files

Primary combined posting sets:

- [日本語の投稿セット](x-post-ja.md) — caption, ALT text, and source/context reply in three individually copyable `text` blocks
- [English posting set](x-post-en.md) — caption, ALT text, and source/context reply in three individually copyable `text` blocks

Adjacent plain-text sidecars have been created beside the normalized posting PNGs and synchronized exactly with these combined Markdown blocks.

| Language | Caption | ALT text | Source/context reply |
| --- | --- | --- | --- |
| Japanese | [caption](images/aardvark_japanese_posting_2026-07-14.caption.txt) | [ALT](images/aardvark_japanese_posting_2026-07-14.alt.txt) | [source note](images/aardvark_japanese_posting_2026-07-14.source-note.txt) |
| English | [caption](images/aardvark_english_posting_2026-07-14.caption.txt) | [ALT](images/aardvark_english_posting_2026-07-14.alt.txt) | [source note](images/aardvark_english_posting_2026-07-14.source-note.txt) |

## Completion Notes

Japanese and English direct Image Gen posters are exact 1024x1536 vertical 2:3 sources and passed text, body-plan, posture, habitat, card-count, and lookalike QA. Both posting PNGs were normalized from compliant sources without padding, cropping, borders, or stretching. `scripts/validate_x_post_format.py`, `scripts/validate_package.py --skip-git`, and `git diff --check` passed. INDEX and automation memory were updated. State: completed, published. The package was published to `origin/master` in commit `9105e7b`; the dependency-loader retry improvement followed in commit `8e08c28`.
