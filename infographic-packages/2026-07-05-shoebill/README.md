# Shoebill Infographic Package

Date: 2026-07-05
Topic: Shoebill / ハシビロコウ / *Balaeniceps rex*
Broad native region: Africa
Status: completed and published on 2026-07-05

## Rationale

The shoebill is a lesser-known African wetland bird with a strong curiosity hook: it can look almost statue-still while carrying an enormous shoe-shaped bill. The package focuses on noticing its swamp habitat, bill shape, and patient hunting posture without using population numbers, blame, urgency, or rescue framing.

## Locked Facts

- Accepted public names: Shoebill / ハシビロコウ / *Balaeniceps rex*.
- Native region: Africa.
- Habitat: large freshwater swamps and papyrus/reed wetlands.
- Core claims: papyrus wetland life; huge shoe-shaped bill; still wait-and-strike hunting.
- Footer: `IUCN Red List 2018: Vulnerable (VU)`.
- Source caveat: the direct IUCN/BirdLife pages are retained as the official status route, but the live page body was thin in this environment. Public copy is limited to the 2018 VU category and basic ecology cross-checked with Animal Diversity Web.

## Artifacts

- Sources and QA: `sources-qa.md`
- Japanese copy: `shoebill_infographic_copy_ja.md`
- English copy: `shoebill_infographic_copy_en.md`
- Japanese image prompt: `shoebill_image_prompt_ja.md`
- English image prompt: `shoebill_image_prompt_en.md`
- Japanese X copy: `shoebill_x_post_ja.md`
- English X copy: `shoebill_x_post_en.md`
- Thread drafts: `thread_drafts.md`
- Japanese direct Image Gen poster: `images/shoebill_japanese_imagegen_2026-07-05.png`
- English direct Image Gen poster: `images/shoebill_english_imagegen_2026-07-05.png`
- Japanese posting PNG: `images/shoebill_japanese_posting_2026-07-05.png`
- English posting PNG: `images/shoebill_english_posting_2026-07-05.png`

## Completion Notes

- Evidence Lock completed before Image Gen.
- Copy Lock completed before Image Gen.
- Independent verifier trial marker was already present in automation memory, so no new one-run verifier was spawned. Local pre-copy and post-image checklists found no unresolved material conflict.
- Phase 3.5 spawned two read-only copy reviewers. The affirmative reviewer later returned apparent formatting issues, but UTF-8 line readback showed the files were structurally correct; the critical reviewer timed out, so the allowed local critical fallback was used. No copy blockers remained.
- A late critical copy-review result found that Japanese and English source/context replies exceeded 280 characters. Both replies were shortened and revalidated; final reply lengths are Japanese 205 and English 265.
- Both direct Image Gen sources are 1024x1536 and exact vertical 2:3.
- Both normalized posting PNGs are 1024x1536.
- No padding, borders, cropping, or stretching were used to repair source ratio.
- Visual QA passed for one gray shoebill in freshwater papyrus/reed wetland, a large pale mottled shoe-shaped bill, hooked tip, large eye, long dark legs, separated toes, and a still hunting posture.
- Text QA passed for both posters: title, scientific name, exactly three labels, and the IUCN 2018 VU footer are present.
- Japanese and English X files passed `scripts/validate_x_post_format.py`; both have three fenced `text` blocks and required source-note labels.
- Deterministic text-safe backups were not created because both direct posters passed visual/text QA.
- Optional generated-images mirror was not separately attempted; direct Image Gen source cache exists under `C:\Users\ryusu\.codex\generated_images\019f3048-8c44-7340-b8d0-2542c590d25d`.
- Phase 5.5 spawned two read-only final reviewers. The affirmative reviewer reported apparent Japanese encoding and formatting issues, but UTF-8 readback showed the files were correct; those findings were rejected as display artifacts. The critical final reviewer timed out, so local critical fallback was used. No unresolved blockers remain.
- GitHub publishing first failed on 2026-07-05 in the normal shell path: `git add` was blocked by `.git/index.lock` permission, and a later alternate-index push could not connect to `github.com:443`. A dedicated publish path was then used for scoped staging, commit, push, and remote verification.
