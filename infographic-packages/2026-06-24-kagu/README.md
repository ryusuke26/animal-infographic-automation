# Kagu / カグー package

Date: 2026-06-24 JST
Scientific name: *Rhynochetos jubatus*
Broad native region: Australia/Oceania
Package status: completed and published to GitHub

## Rationale

Australia/Oceania had zero appearances in the latest eight completed packages, while North America had two and the immediately preceding region was Central America/Caribbean. Kagu adds a New Caledonian ground-bird lineage, humid forest-floor habitat, long-crest identity, and leaf-litter probing hook.

## Locked workflow state

- Evidence Lock completed before Image Gen.
- Copy Lock completed before Image Gen.
- Evidence Lock and Copy Lock were reopened after the user supplied official IUCN screenshots; the corrected 2019 EN footer was locked before the two final poster edits.
- Japanese title: カグー.
- English title: Kagu.
- Scientific name: *Rhynochetos jubatus*.
- Three claims: New Caledonia's forest floor; long crest and red-orange legs; probes leaf litter with its bill.
- Japanese footer: `IUCN Red List 2019: Endangered (EN)`.
- English footer: `IUCN Red List 2019: Endangered (EN)`.
- Assessment year: 2019; last assessed 14 August 2019; global scope; criteria A3e+4ad; C2a(i).
- Population trend: Decreasing, recorded in evidence but omitted from poster and main post.
- The official IUCN status and year were confirmed from user-supplied screenshots of the IUCN search result and assessment page after Codex's own direct access was blocked.
- Automation memory already contains `Independent verifier trial: completed`; no verifier was spawned. Local pre-copy checklist passed.

## Completion state

- Superseded Japanese source: `images/kagu_japanese_imagegen_2026-06-24.png` — correct identity and old conservative footer; retained for audit history.
- Accepted Japanese direct source: `images/kagu_japanese_imagegen_v2_2026-06-24.png` — exactly 1024x1536 and vertical 2:3 with the corrected 2019 EN footer.
- Rejected English first candidate: `images/kagu_english_imagegen_2026-06-24.png` — exactly 1024x1536 and vertical 2:3; superseded because the nasal covers looked like an enlarged flower-like cluster.
- Superseded English v2 source: `images/kagu_english_imagegen_v2_2026-06-24.png` — correct identity and old conservative footer; retained for audit history.
- Accepted English direct source: `images/kagu_english_imagegen_v3_2026-06-24.png` — exactly 1024x1536 and vertical 2:3 with subtle nasal covers and the corrected 2019 EN footer.
- Japanese posting PNG: `images/kagu_japanese_posting_2026-06-24.png` — exactly 1024x1536.
- English posting PNG: `images/kagu_english_posting_2026-06-24.png` — exactly 1024x1536.
- Posting PNGs were created with the bundled workspace Python and `scripts/normalize_poster.py`. Both accepted direct sources were already exact-size 2:3; no padding, border, cropping, stretching, or ratio repair was used.
- Post-image local identity audit passed for body plan, one-bird count, two legs, folded wings, long crest, bill and leg colors, posture, forest-floor habitat, lookalike avoidance, and exact visible text.
- Each Japanese and English X-post file contains exactly three fenced `text` blocks. Required source-note prefixes and direct links are present.
- All short thread posts are under 140 characters.
- Deterministic text-safe backups were not created; they were optional and unnecessary because both accepted direct posters passed text QA.
- Optional generated-images mirror was not attempted. Package-local files are canonical.
- The pre-correction posting PNGs are retained with `_pre_iucn_` filenames for audit history.

## Deliverables

- `sources-qa.md`
- `infographic-copy-ja.md`
- `infographic-copy-en.md`
- `image-prompt-ja.md`
- `image-prompt-en.md`
- `x-post-ja.md`
- `x-post-en.md`
- `thread-drafts.md`
- two user-supplied official IUCN screenshots under `evidence/`
- accepted Japanese and English direct Image Gen sources plus exact-size posting PNGs under `images/`

Avoid this topic next time unless a deliberate remake or comparison is requested.

## Publication

- Package and INDEX commit: `665912a` (`Add Kagu infographic package`), pushed to `origin/master` on 2026-06-24.
