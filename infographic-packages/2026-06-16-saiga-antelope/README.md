# Saiga Antelope Infographic Package

Date: 2026-06-16  
Topic: Saiga Antelope / サイガ / *Saiga tatarica*  
Broad native region: Asia  
Status: completed and published

## Rationale

Selected as a Central Asian dry-steppe ungulate after the previous run used Australia/Oceania. The topic adds a new open-grassland habitat and a strong visual hook: the saiga's downturned, inflated-looking nose.

## Locks

- Evidence Lock: completed before Image Gen.
- Copy Lock: completed before Image Gen.
- Conservation footer: `IUCN Red List 2023: Near Threatened (NT)`.
- Public copy uses no population number, no threat slogan, no subspecies claim, and no unsupported nose-function claim.

## Independent Verifier Trial

Automation memory already contains `Independent verifier trial: completed`, so no verifier was spawned. A local pre-copy independent checklist found no unresolved material conflict after recording the IUCN direct-rendering caveat and avoiding population numbers.

## Visual Production

- Japanese direct Image Gen poster: `images/saiga_antelope_japanese_imagegen_2026-06-16.png`, 1024x1536, vertical 2:3.
- English direct Image Gen poster: `images/saiga_antelope_english_imagegen_2026-06-16.png`, 1024x1536, vertical 2:3.
- Japanese posting PNG: `images/saiga_antelope_japanese_posting_2026-06-16.png`, 1024x1536.
- English posting PNG: `images/saiga_antelope_english_posting_2026-06-16.png`, 1024x1536.
- Deterministic text-safe backup: not created because both direct posters contain readable locked text.

## Completion Notes

- Evidence Lock and Copy Lock were completed before Image Gen.
- Both accepted direct posters are exact target size already; posting PNGs are byte-for-byte copies. No padding, cropping, stretching, or border repair was used.
- The dependency loader was unavailable and no Python executable was found, so `scripts/normalize_poster.py` was not run. No resize was needed because both direct sources were already exactly 1024x1536.
- Visual QA passed: both posters show one tan horned saiga in open dry steppe, with long legs, short tail, ringed horns, long ears, and a large downturned bulbous nose. No fake map, rescue imagery, population graphic, goat/sheep/camel/pronghorn/tapir confusion, or extra animal appears.
- Text QA passed by visual inspection: both posters contain the locked title, scientific name, three observation labels, and `IUCN Red List 2023: Near Threatened (NT)` footer.
- X post files now include copy-paste-ready `Main Post`, `ALT Text`, and `Optional Source / Context Reply` code blocks.
- `thread-drafts.md` exists as a separate copy-paste-friendly thread file; all numbered posts are under 140 characters.
- `git diff --check` passed.
- Optional generated-images mirror was not attempted.
- Avoid selecting Saiga Antelope / サイガ / *Saiga tatarica* again unless explicitly requested.
