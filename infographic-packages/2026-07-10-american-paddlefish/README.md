# American Paddlefish Infographic Package

Status: completed, published
Run date: 2026-07-10

## Rationale

The American Paddlefish adds North America after the previous completed package used South America. In the latest eight completed packages, North America had no appearances while South America and Ocean/Global each had two. This fish also adds freshwater big-river habitat and an ancient ray-finned-fish lineage, with a strong visual hook in the paddle-shaped rostrum.

## Locked Public Claims

1. It is native to large river systems of North America, especially the Mississippi River basin and Gulf Slope drainages.
2. Its broad paddle-shaped rostrum helps it sense tiny prey signals in cloudy river water.
3. It swims with its mouth open and filters plankton from the water.

## Locked Status Footer

- Japanese: `IUCN Red List 2019：危急（VU）`
- English: `IUCN Red List 2019: Vulnerable (VU)`

## Review Notes

- Independent verifier trial: exact marker was absent in automation memory, so one read-only verifier was spawned after Evidence Lock. The parent wait timed out and the verifier was closed; no replacement verifier was spawned. Its later memory-visible findings were reconciled: electroreception support was strengthened with Cornell Chronicle, the later user-supplied official IUCN screenshot resolved the direct-IUCN caveat, and mojibake was rejected after UTF-8 readback plus validators.
- Phase 3.5 dual copy review: local affirmative and critical passes completed before Image Gen. Low-risk deterministic fix shortened English X copy/source reply. No unresolved copy blockers.
- Phase 5 post-image identity check: local fallback completed because the verifier was unavailable after timeout. Anatomy, posture, habitat, lookalike, and visible-text checks passed for accepted posters.
- Phase 5.5 final review: local affirmative and critical passes completed. No unresolved blockers after package QA, X-post validation, image dimensions check, visual QA, and `git diff --check`.
- Source correction: the user supplied the official IUCN page `https://www.iucnredlist.org/species/17938/81763841` plus screenshot evidence confirming Paddlefish / *Polyodon spathula*, Vulnerable (VU), criteria A2cd, Global scope, and Last assessed 14 September 2019. FishBase 2025-2 remains a supporting route.

## Asset Status

- Japanese direct Image Gen poster: `images/american_paddlefish_japanese_imagegen_2026-07-10.png`, 1024x1536, exact vertical 2:3, accepted after targeted text retry
- English direct Image Gen poster: `images/american_paddlefish_english_imagegen_2026-07-10.png`, 1024x1536, exact vertical 2:3, accepted on first pass
- Japanese posting PNG 1024x1536: `images/american_paddlefish_japanese_posting_2026-07-10.png`, exact 1024x1536
- English posting PNG 1024x1536: `images/american_paddlefish_english_posting_2026-07-10.png`, exact 1024x1536
- Superseded Japanese first-pass text candidate: `images/american_paddlefish_japanese_imagegen_2026-07-10_text_superseded.png`; rejected because the second observation added an unsupported comma after `吻で`
- User IUCN screenshot evidence: `images/iucn_polyodon_spathula_user_screenshot_2026-07-10.png`
- Text-safe backups: not created; not expected unless Image Gen text needs deterministic backup
- Optional mirror: not attempted

## Visual QA

- Japanese accepted poster: passed. It shows one smooth gray-blue freshwater fish with a broad flat paddle-shaped rostrum, small lateral eye, open mouth, large gill-cover flap, forked heterocercal tail, murky big-river habitat, exactly three numbered observation cards, and the locked 2019 VU footer.
- English accepted poster: passed. It shows one smooth gray-blue freshwater fish with a broad flat paddle-shaped rostrum, small lateral eye, open mouth, large gill-cover flap, forked heterocercal tail, broad slow river water, exactly three numbered observation cards, and the locked 2019 VU footer.
- Rejection checks passed: no shark, sawfish, sturgeon barbels, catfish whiskers, duck bill, platypus bill, sword nose, ocean, reef, aquarium, fishing/caviar/dam scene, fake map, people, population graphic, rescue imagery, or threat slogan.
- No padding, border, cropping, or stretching was used to repair source ratio. Both accepted direct sources were already 1024x1536.

## QA Commands

- `scripts/validate_x_post_format.py --ja x-post-ja.md --en x-post-en.md`: passed
- `scripts/validate_package.py infographic-packages/2026-07-10-american-paddlefish --skip-git`: passed
- `git diff --check`: passed

## Completion Notes

Evidence Lock and Copy Lock were completed before Image Gen. Separate Japanese and English direct Image Gen posters exist, both are vertical 2:3, and both posting PNGs are exactly 1024x1536. Final visual/text QA, X-post validation, package QA, and `git diff --check` passed. Package commit `44c6e17` (`Add american paddlefish infographic package`) was pushed to `origin/master`; remote `refs/heads/master` verified at `44c6e175db995da5007b78b1f85bf530a6cf3a41`. State: completed and published.
