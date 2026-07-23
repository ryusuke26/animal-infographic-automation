# Alpine Salamander / アルプスサンショウウオ

[日本語の投稿セット](x-post-ja.md)
[English posting set](x-post-en.md)

## Status

- State: completed, local-ready
- Publication: not published; GitHub closeout requires an approval-enabled normal conversation
- Run mode: Caution Run (user-supplied official evidence reopened Evidence Lock)
- Topic: Alpine Salamander / *Salamandra atra*
- Broad native region: Europe
- Package date: 2026-07-23

## Why this topic

The latest eight completed packages contain each broad region once, and the previous package was from North America. Alpine Salamander adds a European terrestrial-amphibian lineage, damp alpine woodland/meadow habitat, and a discovery hook about a glossy black salamander that gives birth to fully developed young without depositing eggs in open water.

## Copy-Ready Posting Files

Primary combined posting sets:

- [日本語の投稿セット](x-post-ja.md)
- [English posting set](x-post-en.md)

Backup sidecars:

- [Japanese caption](images/alpine_salamander_japanese_posting_2026-07-23.caption.txt)
- [Japanese ALT text](images/alpine_salamander_japanese_posting_2026-07-23.alt.txt)
- [Japanese source note](images/alpine_salamander_japanese_posting_2026-07-23.source-note.txt)
- [English caption](images/alpine_salamander_english_posting_2026-07-23.caption.txt)
- [English ALT text](images/alpine_salamander_english_posting_2026-07-23.alt.txt)
- [English source note](images/alpine_salamander_english_posting_2026-07-23.source-note.txt)

## Locked public story

1. It lives in cool, damp mountain woods and meadows.
2. Its glossy black body appears after rain.
3. Its young are born ready for life on land.

## Status basis

The official IUCN species page and PDF for record e.T19843A227233771 directly confirm *Salamandra atra*, Global scope, Least Concern (LC), publication year 2024, assessment date February 8, 2023, and the formal citation. PDF page 5 also supports the damp alpine habitat, wet-weather activity, and fully developed young born on land. The former partner/fallback access caveat has been removed from both public source replies. See [sources-qa.md](sources-qa.md).

## Completion notes

- Evidence Lock: complete via the official IUCN species page and PDF; the page screenshot plus PDF pages 1, 2, and 5 were visually inspected on 2026-07-24
- Independent evidence check: the single read-only Caution-run verifier timed out after 60 seconds; the local fallback found no unresolved blocker
- Copy Lock: complete; local affirmative/critical review passed and both X main posts/source replies fit 280 characters
- Japanese direct Image Gen poster: accepted on the first attempt at exact 1024x1536 vertical 2:3; one glossy black salamander, four limbs, one tail, exact title/scientific name/three numbered cards/footer, and no Fire Salamander spots or axolotl gills
- English direct Image Gen poster: accepted on the first attempt at exact 1024x1536 vertical 2:3; one glossy black salamander, four limbs, one tail, exact title/scientific name/three numbered cards/footer, and the spaces in `2024: Least Concern` are visibly preserved
- Both posting PNGs: exact 1024x1536 after `scripts/normalize_poster.py`; direct/posting pixel comparisons are identical, so no padding, crop, stretch, or border repair occurred
- Six UTF-8 sidecars: present and synchronized with the three fenced blocks in each combined X-post file
- Final local affirmative/critical review: no remaining blocker
- Post-lock evidence correction: both source/context replies and their sidecars now cite the official PDF without the obsolete record-access caveat; the footer, poster text, main posts, ALT text, and images did not need changes
- `scripts/validate_x_post_format.py`, `scripts/validate_package.py`, sidecar synchronization, dimensions/aspect checks, pixel identity, thread-length checks, and `git diff --check`: passed
- Package state: completed, local-ready; no Git state was mutated
