# Sword-billed Hummingbird Infographic Package

Status: completed, local-ready after user IUCN correction
Run date: 2026-07-09

## Rationale

The Sword-billed Hummingbird adds South America to today's rotation after Asia in the previous completed run. It has a clear discovery hook: an Andean hummingbird whose bill can be longer than the rest of its body, matched to long tubular flowers.

## Locked Public Claims

1. It lives around Andean montane/cloud-forest edge habitats from Venezuela to Bolivia.
2. Its extremely long bill reaches nectar in long tubular flowers.
3. Perched birds often hold the long bill upward for balance.

## Locked Status Footer

- Japanese: `IUCN Red List 2024：低懸念（LC）`
- English: `IUCN Red List 2024: Least Concern (LC)`

## Review Notes

- Independent verifier trial: already completed in automation memory; not repeated. Local independent evidence checklist completed in `sources-qa.md`.
- Phase 3.5 dual copy review: complete. Two read-only reviewers ran; low-risk fixes were applied for English X length/source links and status-route caveat wording. UTF-8 local readback rejected reported Japanese line/quote/URL corruption findings.
- Phase 5.5 final review: read-only reviewers timed out and were closed; local affirmative/critical fallback completed. No unresolved blockers found after package QA, X-post validation, dimensions check, visual QA, and `git diff --check`.
- User IUCN correction: official page screenshot supplied after first completion confirms Least Concern (LC), Global scope, and Last assessed 12 June 2024. Evidence Lock and Copy Lock were rerun before the corrected 2024-footer poster generation.

## Asset Status

- Japanese direct Image Gen poster: `images/sword_billed_hummingbird_japanese_imagegen_2026-07-09.png`, 1024x1536, exact 2:3, accepted after 2024-footer regeneration
- English direct Image Gen poster: `images/sword_billed_hummingbird_english_imagegen_2026-07-09.png`, 1024x1536, exact 2:3, accepted after 2024-footer regeneration
- Japanese posting PNG 1024x1536: `images/sword_billed_hummingbird_japanese_posting_2026-07-09.png`, exact 1024x1536
- English posting PNG 1024x1536: `images/sword_billed_hummingbird_english_posting_2026-07-09.png`, exact 1024x1536
- User IUCN screenshot evidence: `images/iucn_ensifera_ensifera_user_screenshot_2026-07-09.png`
- Text-safe backups: not created; not needed for this accepted direct-Image-Gen package
- Optional mirror: not attempted

## Visual QA

- Earlier Japanese and English posters passed visual identity QA but used the superseded 2016 LC footer.
- Corrected Japanese poster: accepted. It shows one hummingbird-like bird in misty Andean cloud forest with long tubular flowers, a green body, bronzy head, white post-ocular spot, forked tail, and a very long black bill held upward. The poster has the locked Japanese title, scientific name, exactly three numbered observation cards, and the locked 2024 LC footer.
- Corrected English poster: accepted. It shows one small hummingbird-like bird in cloud forest with long tubular flowers, green/bronzy plumage, white post-ocular spot, forked tail, and an extremely long black bill held upward. The poster has the locked English title, scientific name, exactly three numbered observation cards, and the locked 2024 LC footer.
- Rejection checks passed: no toucan, kingfisher, sunbird, bee, metal sword beak, fake map, feeder-dominant scene, extra species comparison, population graphic, blame, rescue, or urgency imagery.
- No padding, border, cropping, or stretching was used to repair source ratio. Both direct sources were already 1024x1536.

## QA Commands

- `scripts/validate_x_post_format.py --ja x-post-ja.md --en x-post-en.md`: passed
- `scripts/validate_package.py infographic-packages/2026-07-09-sword-billed-hummingbird`: passed after 2024-footer regeneration
- `git diff --check`: passed

## Completion Notes

Evidence Lock and Copy Lock were completed before first Image Gen, then rerun after user supplied the official IUCN 2024 screenshot. Corrected 2024-footer direct Image Gen posters and exact-size posting PNGs are complete. The package is complete and local-ready. GitHub publishing was not attempted in this run.
