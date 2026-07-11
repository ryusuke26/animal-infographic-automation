# Jamaican Iguana Infographic Package

Status: completed, local-ready
Run date: 2026-07-11

## Rationale

The Jamaican Iguana adds Central America/Caribbean after the previous completed package used North America. In the latest eight completed packages, Central America/Caribbean had no appearances while South America appeared twice. This reptile also adds dry limestone forest habitat, a Caribbean island-endemic lineage, and a strong visual hook in the blue-green crest, dark back chevrons, and rock-sunning posture.

## Locked Public Claims

1. It is endemic to Jamaica and now associated with the Hellshire Hills dry limestone forest.
2. It is a heavy-bodied rock iguana with a blue-green crest and dark chevron-like markings on the back.
3. It eats leaves, flowers, and fruit, and may help move seeds through the island forest.

## Locked Status Footer

- Japanese: `IUCN Red List 2021 CR`
- English: `IUCN Red List 2021 CR`

## Review Notes

- Independent verifier trial: exact marker `Independent verifier trial: completed` was already present in automation memory, so the trial was not repeated. Local independent evidence checklist completed before Copy Lock.
- Phase 3.5 dual copy review: two read-only reviewers were spawned but timed out and were closed without findings; local affirmative and critical copy review completed. A later direct-IUCN check found the latest global assessment was CR in 2021, not the earlier 2010 route. Copy Lock was reopened and both posters were regenerated with `IUCN Red List 2021 CR`.
- Phase 5 post-image identity check: local fallback completed because no reusable verifier was available. Anatomy, posture, habitat, lookalike, and visible-text checks passed for accepted posters.
- Phase 5.5 final review: two read-only reviewers were spawned but timed out and were closed without findings; local affirmative and critical final review completed. No stale pending notes, status mismatches, missing files, validator gaps, or unresolved blockers remained.

## Asset Status

- Japanese direct Image Gen poster: `images/jamaican_iguana_japanese_imagegen_2026-07-11.png`, 1024x1536, exact vertical 2:3, accepted with `IUCN Red List 2021 CR`
- English direct Image Gen poster: `images/jamaican_iguana_english_imagegen_2026-07-11.png`, 1024x1536, exact vertical 2:3, accepted with `IUCN Red List 2021 CR`
- Japanese posting PNG 1024x1536: `images/jamaican_iguana_japanese_posting_2026-07-11.png`, exact 1024x1536
- English posting PNG 1024x1536: `images/jamaican_iguana_english_posting_2026-07-11.png`, exact 1024x1536
- Superseded Japanese first-pass text candidates: `images/jamaican_iguana_japanese_imagegen_2026-07-11_text_superseded_v1.png` and `images/jamaican_iguana_japanese_imagegen_2026-07-11_text_superseded_v2.png`; rejected for observation-label/footer text drift
- Superseded 2010-status sources and posting PNGs: filenames ending `_status_superseded_2010.png`; retained only as a correction trail and not for publication.
- Text-safe backups: not created; not expected unless Image Gen text needs deterministic backup
- Optional mirror: not attempted

## Copy-Ready Posting Files

Each posting PNG has adjacent UTF-8 text files for direct copying.

| Language | Main caption | ALT text | Source/context reply |
| --- | --- | --- | --- |
| Japanese | [caption](images/jamaican_iguana_japanese_posting_2026-07-11.caption.txt) | [ALT](images/jamaican_iguana_japanese_posting_2026-07-11.alt.txt) | [source note](images/jamaican_iguana_japanese_posting_2026-07-11.source-note.txt) |
| English | [caption](images/jamaican_iguana_english_posting_2026-07-11.caption.txt) | [ALT](images/jamaican_iguana_english_posting_2026-07-11.alt.txt) | [source note](images/jamaican_iguana_english_posting_2026-07-11.source-note.txt) |

The structured Markdown sources remain `x-post-ja.md` and `x-post-en.md`.

## Visual QA

- Japanese accepted poster: passed. It shows one heavy-bodied blue-green Jamaican rock iguana basking on pale limestone in dry forest, with a dorsal crest, dark chevron-like back markings, long ringed tail, four clawed legs, exactly three numbered observation cards, and the locked `IUCN Red List 2021 CR` footer.
- English accepted poster: passed. It shows one heavy-bodied blue-green Jamaican rock iguana basking on pale limestone in dry forest, with a dorsal crest, dark chevron-like back markings, long ringed tail, four clawed legs, exactly three numbered observation cards, and the locked `IUCN Red List 2021 CR` footer.
- Rejection checks passed: no generic bright pet green iguana, bearded dragon, monitor lizard, crocodile, dinosaur-like monster, fake map, zoo cage, keeper hands, rescue scene, population graphic, or threat-heavy imagery.
- No padding, border, cropping, or stretching was used to repair source ratio. Both accepted direct sources were already 1024x1536.

## QA Commands

- `scripts/validate_x_post_format.py --ja x-post-ja.md --en x-post-en.md`: passed
- `scripts/validate_package.py infographic-packages/2026-07-11-jamaican-iguana --skip-git`: passed
- `git diff --check`: passed
- X block lengths: Japanese 165/109/240; English 280/315/242. English ALT is longer than a normal post but within X ALT-text expectations; English main and source reply fit 280 characters.

## Completion Notes

Evidence Lock and Copy Lock were completed before Image Gen. The original IUCN 2010 route was corrected on 2026-07-11 after direct verification of the latest global CR assessment dated 25 August 2021; both direct posters and posting PNGs were regenerated with the 2021 footer. Separate Japanese and English direct Image Gen posters exist, both are vertical 2:3, and both posting PNGs are exactly 1024x1536. State: completed and local-ready; GitHub publishing not attempted per no-approval automation policy.
