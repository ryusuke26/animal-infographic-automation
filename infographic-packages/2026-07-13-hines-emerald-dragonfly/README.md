# Hine's Emerald Dragonfly Infographic Package

Status: completed, local-ready after official IUCN correction
Run date: 2026-07-13

## Rationale

Hine's Emerald adds an insect lineage absent from the latest eight completed packages and avoids repeating the previous Australia/Oceania region. Its groundwater-fed fen habitat, emerald eyes and yellow stripes, and larval use of crayfish burrows provide three compact discovery-first observation cards.

## Locked Public Claims

1. It lives in North American groundwater-fed wetlands with shallow flow and grass-like vegetation.
2. Adults have brilliant green eyes and two creamy-yellow lateral stripes on a dark metallic-green thorax.
3. Aquatic larvae use crayfish burrows as refuge during dry periods and winter.

## Locked Status Footer

- Japanese: `IUCN Red List 2018：低懸念（LC）`
- English: `IUCN Red List 2018: Least Concern (LC)`

The official IUCN page confirms Least Concern, Global scope, and last assessed 8 June 2018. The U.S. ESA Endangered listing remains valid under a different jurisdiction and is explained in the source/context reply.

## Review Notes

- Independent verifier trial: the marker `Independent verifier trial: completed` was already present in automation memory, so the one-run trial was not repeated. A local independent evidence checklist was completed.
- Phase 3.5 dual copy review: two read-only reviewers completed affirmative and critical passes. Accepted fixes softened causal habitat wording, aligned `dry periods`, improved Japanese punctuation, and added direct fact-specific USFWS links. Validator rerun passed; no unresolved blocker remains.
- Phase 5 post-image identity check: the first Japanese candidate was rejected for wing overlap and retained as superseded. One targeted anatomy edit produced a four-wing accepted poster without text or layout drift. The English first pass was accepted. Both accepted posters passed identity, habitat, lookalike, text, and 2:3 checks.
- Phase 5.5 final review: the same two read-only reviewers completed affirmative and critical passes. README sidecar wording was corrected. Critical review caught a curly-apostrophe drift in the first English title; that poster was superseded, one targeted text-only correction restored exact `HINE'S EMERALD`, and both reviewers confirmed no new drift. No unresolved blocker remains.
- User review correction: the in-app Browser exposed the official IUCN global LC assessment. Evidence Lock and Copy Lock were reopened. The public footer was changed from U.S. ESA Endangered to IUCN Red List 2018 LC, while U.S. legal status moved to the source reply. The Japanese editorial label `（英名の音写）` was removed; the naming caveat remains only in `sources-qa.md`. Corrected posters passed visual/text and mechanical QA.

## Asset Status

- Japanese direct Image Gen poster: `images/hines_emerald_dragonfly_japanese_imagegen_2026-07-13.png`, 1024x1536, exact vertical 2:3, corrected title and IUCN 2018 LC footer, accepted
- English direct Image Gen poster: `images/hines_emerald_dragonfly_english_imagegen_2026-07-13.png`, 1024x1536, exact vertical 2:3, corrected IUCN 2018 LC footer, accepted
- Japanese posting PNG at 1024x1536: `images/hines_emerald_dragonfly_japanese_posting_2026-07-13.png`, normalized from the compliant accepted direct source
- English posting PNG at 1024x1536: `images/hines_emerald_dragonfly_english_posting_2026-07-13.png`, normalized from the compliant accepted direct source
- Superseded Japanese candidate: `images/hines_emerald_dragonfly_japanese_imagegen_2026-07-13_wing_overlap_superseded.png`; rejected because only two wings were clearly countable
- Superseded English candidate: `images/hines_emerald_dragonfly_english_imagegen_2026-07-13_curly_apostrophe_superseded.png`; rejected because the title used a curly apostrophe
- Superseded U.S.-ESA-footer assets: direct and posting filenames ending `_status_superseded_usa_esa.png`; retained only as correction history and must not be posted
- Text-safe backups: not planned unless needed
- Optional mirror: not attempted

## Copy-Ready Posting Files

Primary combined posting sets:

- [日本語の投稿セット](x-post-ja.md) — caption, ALT text, and source/context reply in three individually copyable `text` blocks
- [English posting set](x-post-en.md) — caption, ALT text, and source/context reply in three individually copyable `text` blocks

Adjacent plain-text sidecars have been created beside the normalized posting PNGs and are synchronized exactly with these combined Markdown blocks.

The files below are secondary UTF-8 plain-text backups containing one copy target each.

| Language | Caption | ALT text | Source/context reply |
| --- | --- | --- | --- |
| Japanese | [caption](images/hines_emerald_dragonfly_japanese_posting_2026-07-13.caption.txt) | [ALT](images/hines_emerald_dragonfly_japanese_posting_2026-07-13.alt.txt) | [source note](images/hines_emerald_dragonfly_japanese_posting_2026-07-13.source-note.txt) |
| English | [caption](images/hines_emerald_dragonfly_english_posting_2026-07-13.caption.txt) | [ALT](images/hines_emerald_dragonfly_english_posting_2026-07-13.alt.txt) | [source note](images/hines_emerald_dragonfly_english_posting_2026-07-13.source-note.txt) |

## Completion Notes

Evidence Lock and Copy Lock were reopened after the official IUCN page was read in the in-app Browser. Both corrected direct sources passed `scripts/normalize_poster.py`; both posting PNGs are exactly 1024x1536. `scripts/validate_x_post_format.py`, `scripts/validate_package.py --skip-git`, and `git diff --check` passed after correction. INDEX and automation memory were updated. State: completed, local-ready. GitHub publishing was not attempted under the no-approval automation policy.
