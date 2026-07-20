# Water Chevrotain / ミズマメジカ

*Hyemoschus aquaticus* — discovery-first natural-history package for 2026-07-19.

## Copy-Ready Posting Sets

- [日本語の投稿セット](x-post-ja.md)
- [English posting set](x-post-en.md)

## Status

- Evidence Lock: complete (official 2016 IUCN assessment PDF inspected; Global-scope treatment cross-checked against the official IUCN SSC route).
- Copy Lock: complete.
- Visual production: complete.
- Final QA: passed locally.
- Publication state: completed, local-ready.

## Why this subject

The latest eight completed packages contain each broad region once, and the preceding package was South American. Water Chevrotain adds an African forest ungulate, a damp riverside rainforest habitat, a diagnostic white spot-and-stripe pattern, and the quiet surprise of using water as a short-term refuge.

## Evidence and wording

- Accepted names, habitat, status route, claim checks, and exact visual identity guidance are recorded in [sources-qa.md](sources-qa.md).
- The quiet footer is `IUCN Red List 2016: Least Concern (LC)`.
- The user-supplied official IUCN assessment PDF directly confirms *Hyemoschus aquaticus* / Water Chevrotain, Least Concern (LC), publication year 2016, assessment date 7 January 2016, assessor, citation, range, and riverside moist-lowland-forest habitat. The older PDF layout does not print a literal `Scope: Global` field, so species-wide Global treatment remains explicitly cross-checked against the official IUCN SSC current display and the assessment's full range/country coverage. The species-page block is retained only as process history in `sources-qa.md`; public source replies now cite the inspected official PDF rather than an access caveat.

## Locked production files

- [Japanese infographic copy](infographic-copy-ja.md)
- [English infographic copy](infographic-copy-en.md)
- [Japanese Image Gen prompt](image-prompt-ja.md)
- [English Image Gen prompt](image-prompt-en.md)

## Copy-Ready Posting Files

- [Japanese caption](images/water_chevrotain_japanese_posting_2026-07-19.caption.txt)
- [Japanese ALT text](images/water_chevrotain_japanese_posting_2026-07-19.alt.txt)
- [Japanese source note](images/water_chevrotain_japanese_posting_2026-07-19.source-note.txt)
- [English caption](images/water_chevrotain_english_posting_2026-07-19.caption.txt)
- [English ALT text](images/water_chevrotain_english_posting_2026-07-19.alt.txt)
- [English source note](images/water_chevrotain_english_posting_2026-07-19.source-note.txt)

## Poster assets

- [Direct Japanese Image Gen poster](images/water_chevrotain_japanese_imagegen_2026-07-19.png)
- [Direct English Image Gen poster](images/water_chevrotain_english_imagegen_2026-07-19.png)
- [Japanese posting PNG](images/water_chevrotain_japanese_posting_2026-07-19.png)
- [English posting PNG](images/water_chevrotain_english_posting_2026-07-19.png)

## Completion and QA notes

- Phase 2.5 used one bounded read-only verifier attempt; it did not return in time and no replacement was spawned. The local fallback reconciled the Japanese/scientific/English names, current LC display, 2016 record year, West/Central African riverside-forest habitat, three public claims, and the IUCN SSC photo-ID guide's diagnostic anatomy.
- Phase 3.5 local affirmative and critical copy review passed. The English main post and source reply were shortened without changing facts; the canonical three-block validator passed.
- Japanese and English direct Image Gen posters were accepted on the first attempt. Each is exactly 1024x1536 and vertical 2:3. Both show one compact, rounded Water Chevrotain on land beside a forest stream, with short legs, slightly higher hindquarters, no horns or antlers, rows of white spots, two horizontal flank stripes, and exactly three numbered illustrated cards.
- Visible text matches Copy Lock in both languages. No duplicate animal, fawn, duiker, Asian mouse-deer, generic deer, swimming/underwater scene, predator, hunting, fake map, population graphic, blame, rescue, or urgency imagery appears.
- Bundled-Python normalization produced exact 1024x1536 posting PNGs without padding, crop, stretch, or border repair.
- All six UTF-8 sidecars exactly match the corresponding fenced blocks in `x-post-ja.md` and `x-post-en.md`.
- `scripts/validate_x_post_format.py`, `scripts/validate_package.py infographic-packages/2026-07-19-water-chevrotain`, strict UTF-8 checks, image-size/aspect/pixel-identity checks, and `git diff --check` passed.
- Phase 5.5 local affirmative review confirmed the two primary posting-set links, six sidecars, four active PNG assets, visual identity, status evidence route, and validator output. The critical stop-ship pass found no missing file, status mismatch, copy drift, image rejection issue, or publication blocker.
- Post-completion official-PDF review inspected all nine pages by text extraction and visually checked PDF pages 1, 2, and 5. It upgraded the category/year/date evidence without changing the locked footer, posters, main-post copy, or ALT text; only evidence records and source replies required synchronization.
- GitHub publishing was not attempted in this no-approval automation context. Approval-enabled closeout remains separate.
