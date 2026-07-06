# Maned Wolf Infographic Package

Date: 2026-07-06

Status: completed and local-ready, not published.

## Topic

- Common name: Maned wolf / タテガミオオカミ
- Scientific name: *Chrysocyon brachyurus*
- Broad native region: South America
- Lineage: Mammalia, Carnivora, Canidae
- Habitat: South American open grassland, savanna, scrub, and forest-edge landscapes.
- Hook: A foxlike but neither-fox-nor-wolf canid with very long black legs that eats fruit as well as small animals.

## Evidence And Copy

- Evidence Lock completed before Image Gen.
- Copy Lock completed before Image Gen.
- Locked footer:
  - Japanese: `IUCN Red List 2015：準絶滅危惧（NT）`
  - English: `IUCN Red List 2015: Near Threatened (NT)`
- IUCN status update: the user supplied an IUCN screenshot confirming Maned Wolf / *Chrysocyon brachyurus*, Near Threatened (NT), Global scope, last assessed 13 August 2015, with errata version published in 2016. My direct page access still did not render in this environment, but the screenshot resolves the status/year caveat for package notes.
- Public copy uses no population number, decline percentage, current threat ranking, legal-protection claim, blame, rescue framing, or urgency slogan.

## Image Gen Status

- Japanese first direct poster: `images/maned_wolf_japanese_imagegen_2026-07-06_text_superseded.png`, 1024x1536, rejected because generated labels/footer did not match Copy Lock closely enough.
- Design note: user liked the rejected numbered-card design direction. It remains rejected only because the poster text expanded beyond Copy Lock, not because the visual style itself was disliked.
- Japanese targeted-regeneration direct poster: `images/maned_wolf_japanese_imagegen_2026-07-06.png`, 1024x1536 and vertical 2:3; user review corrected the earlier visual misread and accepted the title as `タテガミオオカミ`.
- English direct poster: `images/maned_wolf_english_imagegen_2026-07-06.png`, 1024x1536 and vertical 2:3; visual/text QA passed.
- Japanese posting PNG: `images/maned_wolf_japanese_posting_2026-07-06.png`, 1024x1536.
- English posting PNG: `images/maned_wolf_english_posting_2026-07-06.png`, 1024x1536.
- No padding, borders, cropping, or stretching were used to repair image ratio.
- Deterministic text-safe backups were not created before closeout; they would not substitute for the failed Japanese direct Image Gen requirement.

## Reviews

- Independent verifier trial ran because the completion marker was absent from automation memory.
- Pre-copy verifier result: no blocker; keep IUCN direct-access caveat visible and enforce lookalike QA.
- Phase 3.5 dual copy review ran with read-only affirmative and critical reviewers. Deterministic fixes applied: English source-note URL punctuation and clearer IUCN caveat wording. X validator passed afterward.
- Post-image verifier check: completed with the same read-only verifier; the earlier title concern was later corrected by user review. English text, anatomy, posture, and habitat were acceptable.
- Phase 5.5 dual final review: completed with read-only affirmative and critical reviewers. Auto-fix applied: shortened the English X main post below normal 280-character posting length. No unresolved completion blocker remains after user correction of the Japanese title read.

## QA Summary

- Required text files exist.
- Japanese and English X-post files each contain three separate fenced `text` blocks.
- Japanese source/context reply begins with `出典メモ：`.
- English source/context reply begins with `Source note:`.
- `scripts/validate_x_post_format.py` passed with bundled Python.
- English X main post was shortened after critical final review flagged a 292-character validator gap.
- Both direct source posters and both posting PNGs are 1024x1536.
- Package is completed and local-ready. Git publishing is still pending because the current shell cannot create `.git/index.lock`.

## Next Step

Ready for posting from local files. GitHub publishing still needs a shell path with normal `.git` write/network access.
