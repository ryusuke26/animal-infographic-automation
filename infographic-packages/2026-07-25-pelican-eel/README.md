# Pelican Eel Infographic Package

- Date: 2026-07-25
- Package state: `completed`
- Publication state: `published`
- Workflow position: Phase 7 GitHub closeout completed

## Topic Lock

- English common name: Pelican Eel
- Japanese common name: フクロウナギ
- Scientific name: *Eurypharynx pelecanoides*
- Broad native region: Ocean/Global
- Lineage: deep-sea gulper eel, family Eurypharyngidae
- Habitat: deep oceanic midwaters across tropical and temperate oceans
- Curiosity hook: an enormous expandable mouth and pharynx on a dark,
  tapering body whose tail ends in a small light organ

The official PDF confirms order Saccopharyngiformes and family
Eurypharyngidae.

## Official IUCN Evidence

The complete screenshot and matching PDF were supplied on 2026-07-25 and
preserved under `evidence/`.

- The complete screenshot confirms the accepted taxon, Least Concern (LC),
  `Last assessed: 24 May 2012`, the matching assessment citation, and
  `Scope of assessment: Global`.
- PDF p.1 confirms the accepted taxon, Least Concern (LC), assessor, citation,
  and assessment identifier.
- PDF p.2 confirms `Year Published: 2015` and
  `Date Assessed: May 24, 2012`.
- PDF p.5 confirms population trend Unknown, marine habitat/ecology context,
  and the assessment's threat statement.

Official routes remain:

- Species page:
  https://www.iucnredlist.org/species/18227119/42691734
- Assessment DOI:
  https://doi.org/10.2305/IUCN.UK.2015-4.RLTS.T18227119A42691734.en

Evidence Lock is complete. Locked public status footer:

- Japanese: `IUCN Red List 2012：低懸念（LC）`
- English: `IUCN Red List 2012: Least Concern (LC)`

Copy Lock is complete. Japanese and English infographic copy, image prompts,
accepted posters, combined posting sets, synchronized sidecars, and short
thread drafts are present.

Pre-image validation passed:

- `scripts/validate_x_post_format.py`
- `scripts/validate_package.py --pre-image`
- `git diff --check`
- all eight short-thread posts remain under 140 characters

## Primary Posting Sets

- [日本語の投稿セット](x-post-ja.md)
- [English posting set](x-post-en.md)

Combined Markdown files above are the primary copy surface. Plain-text
sidecars are synchronized backups:

- [Japanese caption](images/pelican_eel_japanese_posting_2026-07-25.caption.txt)
- [Japanese ALT text](images/pelican_eel_japanese_posting_2026-07-25.alt.txt)
- [Japanese source note](images/pelican_eel_japanese_posting_2026-07-25.source-note.txt)
- [English caption](images/pelican_eel_english_posting_2026-07-25.caption.txt)
- [English ALT text](images/pelican_eel_english_posting_2026-07-25.alt.txt)
- [English source note](images/pelican_eel_english_posting_2026-07-25.source-note.txt)

## Locked Copy

- [Japanese infographic copy](infographic-copy-ja.md)
- [English infographic copy](infographic-copy-en.md)
- [Japanese image prompt](image-prompt-ja.md)
- [English image prompt](image-prompt-en.md)
- [Short thread drafts](thread-drafts.md)

## Poster Assets

- [Japanese direct Image Gen source](images/pelican_eel_japanese_imagegen_2026-07-25.png)
- [English direct Image Gen source](images/pelican_eel_english_imagegen_2026-07-25.png)
- [Japanese posting PNG](images/pelican_eel_japanese_posting_2026-07-25.png)
- [English posting PNG](images/pelican_eel_english_posting_2026-07-25.png)

## Image QA

- Japanese first attempt: rejected because the hero tail tip was hidden behind
  a card and the attached light organ was not visible on the main silhouette.
- Japanese targeted retry: accepted. The complete tail is visible and ends in
  exactly one attached pinkish light organ. All six locked text strings remain
  correct.
- English first attempt: accepted. The full body and attached tail-tip light
  organ are visible, and all six locked text strings are correct.
- Both accepted direct sources are exact 1024x1536 vertical 2:3 PNGs.
- Both posters contain one hero eel, exactly three numbered icon-bearing cards,
  and no bird beak, external pelican pouch, head lure, extra glowing points,
  duplicate hero, or fake map.
- Both accepted direct/posting pairs are exact 1024x1536 vertical 2:3 and
  pixel-identical after normalization. No padding, crop, stretch, or border
  repair was used.
- Japanese and English source posters, posting PNGs, six sidecars, Copy Lock,
  and X copy are synchronized.

## Final QA

- Run mode: Caution Run due to the species' unusual mouth, pharynx, and tail.
- Evidence Lock: official IUCN screenshot and PDF directly confirm Global LC,
  assessed 24 May 2012 and published 2015.
- Copy Lock and `scripts/validate_package.py --pre-image`: passed before Image
  Gen.
- X-post format and all eight short-thread limits: passed.
- Direct-source and posting dimensions: exact 1024x1536.
- Posting pixel identity: passed for both languages.
- Final package validator and `git diff --check`: passed after the README
  sidecar links were added.
- GitHub closeout: package commit `2fa8e05` and Fast Run workflow commit
  `76d34b7` reached `origin/master`; the remote ref was verified before this
  published-state metadata update.
