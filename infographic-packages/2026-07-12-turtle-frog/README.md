# Turtle Frog Infographic Package

Status: completed, published
Run date: 2026-07-12

## Rationale

Turtle Frog adds Australia/Oceania, the only broad region absent from the latest eight completed packages. The previous package used Central America/Caribbean. This amphibian adds sandy subterranean habitat and a strong discovery hook: a round, turtle-like frog that burrows headfirst and develops directly inside the egg.

## Locked Public Claims

1. It is endemic to southwestern Western Australia and lives mainly in sandy soils.
2. Its short, muscular forelimbs help it burrow forward, headfirst.
3. Development is completed inside the egg, so a small froglet hatches without a free-living tadpole stage.

## Locked Status Footer

- Japanese: `IUCN Red List 2021 LC`
- English: `IUCN Red List 2021 LC`

## Review Notes

- Independent verifier trial: the marker `Independent verifier trial: completed` was already present in automation memory, so the one-run trial was not repeated. A local independent evidence checklist was completed.
- Phase 3.5 dual copy review: the read-only affirmative reviewer found no blocker and suggested two English clarity edits, both applied. The critical reviewer timed out and was closed; a local stop-ship pass found no contradiction, unsupported image-facing claim, missing block, status mismatch, or unresolved placeholder. Static checks confirmed three fenced blocks per X file, required source prefixes, the exact Japanese series ending, and prompt/copy string equality.
- Phase 5 post-image identity check: local checklist passed. Both accepted posters show one round pinkish-tan turtle frog with a tiny head, small eyes, short muscular forelimbs, short hind limbs, no shell or tail, and sandy southwestern Australian habitat. All six locked strings are visible and exact in each language.
- Phase 5.5 final review: affirmative and critical read-only reviewers agreed that facts, copy, image identity, visible text, card order, dimensions, source-note format, and static mechanical checks pass. The earlier bundled-Python blocker is resolved: the workspace dependency loader returned the bundled runtime during the 2021-status correction, normalization and both validators passed.
- User IUCN correction: the official page and user-provided screenshot confirm Turtle Frog / *Myobatrachus gouldii*, Least Concern (LC), Global scope, last assessed 18 May 2021. Evidence Lock and Copy Lock were reopened; all public copy now uses `IUCN Red List 2021 LC`. The 2004-footer posters are superseded and must not be posted.

## Asset Status

- Japanese direct Image Gen poster: `images/turtle_frog_japanese_imagegen_2026-07-12.png`, 1024x1536, exact vertical 2:3, accepted with corrected `IUCN Red List 2021 LC` footer
- English direct Image Gen poster: `images/turtle_frog_english_imagegen_2026-07-12.png`, 1024x1536, exact vertical 2:3, accepted with corrected `IUCN Red List 2021 LC` footer
- Japanese posting PNG at 1024x1536: `images/turtle_frog_japanese_posting_2026-07-12.png`, exact 1024x1536, normalized from the compliant direct source
- English posting PNG at 1024x1536: `images/turtle_frog_english_posting_2026-07-12.png`, exact 1024x1536, normalized from the compliant direct source
- Superseded Japanese candidate: `images/turtle_frog_japanese_imagegen_2026-07-12_card_order_superseded.png`; rejected because cards 1 and 2 were swapped
- Superseded 2004-footer assets: filenames ending `_status_superseded_2004.png`; retained only as a correction trail and must not be posted
- Official IUCN evidence screenshot: `images/iucn_myobatrachus_gouldii_user_screenshot_2026-07-12.png`
- Text-safe backups: not planned unless needed
- Optional mirror: not attempted

## Copy-Ready Posting Files

Primary combined posting sets:

- [日本語の投稿セット](x-post-ja.md) — caption, ALT text, and source/context reply in three individually copyable `text` blocks
- [English posting set](x-post-en.md) — caption, ALT text, and source/context reply in three individually copyable `text` blocks

The files below are secondary UTF-8 plain-text backups containing one copy
target each.

| Language | Caption | ALT text | Source/context reply |
| --- | --- | --- | --- |
| Japanese | [caption](images/turtle_frog_japanese_posting_2026-07-12.caption.txt) | [ALT](images/turtle_frog_japanese_posting_2026-07-12.alt.txt) | [source note](images/turtle_frog_japanese_posting_2026-07-12.source-note.txt) |
| English | [caption](images/turtle_frog_english_posting_2026-07-12.caption.txt) | [ALT](images/turtle_frog_english_posting_2026-07-12.alt.txt) | [source note](images/turtle_frog_english_posting_2026-07-12.source-note.txt) |

Use the combined Markdown posting sets above as the default copy route.

## Completion Notes

Evidence Lock and Copy Lock were reopened after the user supplied the official IUCN page and screenshot. The current locked basis is the global Least Concern assessment dated 18 May 2021; the Red List citation is published in 2022. The direct page still returned a 520 error to automated retrieval, so the saved user screenshot is retained as the official-page verification trail.

During the 2021-status correction, the workspace dependency loader returned bundled Python `C:\Users\ryusu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`. Both corrected direct sources passed `scripts/normalize_poster.py`; both posting PNGs are exactly 1024x1536. `scripts/validate_x_post_format.py`, `scripts/validate_package.py --skip-git`, and `git diff --check` passed. No padding, border, crop, or stretch was used. State: completed and published to GitHub in package commit `6f4e6b0`; combined posting-copy workflow improvements were published in commit `d26c15b`.
