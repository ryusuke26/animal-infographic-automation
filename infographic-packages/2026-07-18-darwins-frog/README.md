# Darwin's Frog / ダーウィンガエル

*Rhinoderma darwinii* — discovery-first natural-history package for 2026-07-18.

## Copy-Ready Posting Sets

- [日本語の投稿セット](x-post-ja.md)
- [English posting set](x-post-en.md)

## Status

- Evidence Lock: complete (official IUCN assessment PDF directly confirmed).
- Copy Lock: complete.
- Visual production: complete after Rescue-Run anatomy correction.
- Final QA: passed locally.
- Publication state: completed, published.

## Why this subject

South America had no appearance in the latest eight completed packages, while the preceding package was from Asia. Darwin's Frog adds an amphibian lineage, a cool temperate-forest floor, and a precise discovery hook: the male carries developing young in his vocal sac until froglets emerge.

## Evidence and wording

- Accepted Japanese name, habitat, status route, public claims, corrected visual guide, and local independent-check fallback are recorded in [sources-qa.md](sources-qa.md).
- The quiet footer is `IUCN Red List 2018: Endangered (EN)`.
- The user-provided official IUCN assessment PDF directly confirms *Rhinoderma darwinii*, Global scope, Endangered (EN), year published 2018, and assessment date 17 November 2017. The earlier live-page block remains process history only; public source replies now cite the official PDF/DOI without an access caveat.

## Locked production files

- [Japanese infographic copy](infographic-copy-ja.md)
- [English infographic copy](infographic-copy-en.md)
- [Japanese Image Gen prompt](image-prompt-ja.md)
- [English Image Gen prompt](image-prompt-en.md)

## Copy-Ready Posting Files

- [Japanese caption](images/darwins_frog_japanese_posting_2026-07-18.caption.txt)
- [Japanese ALT text](images/darwins_frog_japanese_posting_2026-07-18.alt.txt)
- [Japanese source note](images/darwins_frog_japanese_posting_2026-07-18.source-note.txt)
- [English caption](images/darwins_frog_english_posting_2026-07-18.caption.txt)
- [English ALT text](images/darwins_frog_english_posting_2026-07-18.alt.txt)
- [English source note](images/darwins_frog_english_posting_2026-07-18.source-note.txt)

## Poster assets

- [Direct Japanese Image Gen poster](images/darwins_frog_japanese_imagegen_2026-07-18.png)
- [Direct English Image Gen poster](images/darwins_frog_english_imagegen_2026-07-18.png)
- [Japanese posting PNG](images/darwins_frog_japanese_posting_2026-07-18.png)
- [English posting PNG](images/darwins_frog_english_posting_2026-07-18.png)

## Completion and QA notes

- Both accepted direct Image Gen posters are vertical 2:3 (1024x1536), and bundled-Python normalization produced exact 1024x1536 posting PNGs without padding, crop, stretching, or border repair.
- One Japanese first-pass Image Gen candidate omitted the dakuten in `ダーウィンガエル`; it is retained as `darwins_frog_japanese_imagegen_2026-07-18_text_rejected.png` for traceability and is not a posting asset.
- User review correctly found that the next Japanese poster had an unsupported point above/behind the eye, not just the true nasal projection. The English poster had a smaller version of the same defect. Both superseded direct sources are retained with `_eye_spike_rejected.png`; neither is a posting asset.
- Corrected Japanese and English sources were edited against the IUCN SSC Amphibian Specialist Group's side-view photograph. Final QA confirms one nasal point only, round lateral eyes, a smooth crown, one correctly identified terrestrial Darwin's Frog per poster, three numbered card/icon cues, unchanged Copy-Lock text, six synchronized sidecars, package validation, and whitespace checks.
- Published to GitHub on 2026-07-18. Package commit: `75ee0ac`; workflow QA commit: `4369082`; published-state metadata was recorded in a dedicated closeout commit.
