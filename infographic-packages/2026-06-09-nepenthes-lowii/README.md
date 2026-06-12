# Low's Pitcher Plant Infographic Package

Date: 2026-06-09
Package: `2026-06-09-nepenthes-lowii`
Topic: Low's Pitcher Plant / ネペンテス・ローウィー
Scientific name: *Nepenthes lowii*
Broad native region: Asia
Lineage: Plantae, Nepenthaceae
Status: completed; local-ready, not published

## Rationale

Asia and North America had 0 appearances in the most recent 8 completed packages. The previous package was European, so Asia is a non-consecutive underrepresented region. This topic also shifts the series from recent mammals, fungi, insects, fish, and amphibians to a Bornean montane pitcher plant whose mature aerial pitchers exchange food with mountain tree shrews and receive nitrogen from their droppings.

## Locked Public Claims

1. The species is a climbing pitcher plant native to northern and north-central Borneo.
2. Mature aerial pitchers have a bulbous lower chamber, narrow waist, wide opening, and an upright or reflexed lid that produces a white food secretion.
3. Mountain tree shrews feed at the lid and deposit droppings into the pitcher, providing the plant with nitrogen.

## Locked Footer

```text
IUCN Red List 2000: Vulnerable (VU)
```

## File Manifest

- `sources-qa.md` - Evidence Lock, candidate selection, claim checks, and sources.
- `copy-japanese.md` - locked Japanese poster text.
- `copy-english.md` - locked English poster text.
- `prompt-japanese.md` - locked Japanese Image Gen prompt.
- `prompt-english.md` - locked English Image Gen prompt.
- `x-post-japanese.md` - Japanese post, ALT text, and source reply.
- `x-post-english.md` - English post, ALT text, and source reply.
- `thread-drafts.md` - short Japanese and English thread drafts.
- `images/` - direct Image Gen posters and text-safe backups.
- `render_textsafe.py` - deterministic SVG/PNG backup renderer.

## Completion Notes

- Evidence Lock: completed before Image Gen.
- Copy Lock: completed before Image Gen.
- Japanese direct Image Gen poster: accepted, `images/nepenthes_lowii_japanese_imagegen_2026-06-09.png`.
- English direct Image Gen poster: accepted, `images/nepenthes_lowii_english_imagegen_2026-06-09.png`.
- Deterministic text-safe backups: Japanese and English SVG/PNG files exist.
- Visual QA: passed. Both direct posters show a mature aerial pitcher with a rounded lower chamber, strong narrow waist, broad opening, reflexed lid with pale secretion, and one long-tailed tree shrew feeding over the opening. No porcelain toilet, generic tube, extra animal, fake map, or rescue framing is present.
- Text QA: passed by visual inspection. Both direct posters use the locked language-specific title, scientific name, three labels, and dated IUCN footer.
- Mechanical QA: direct Image Gen PNGs are 1024x1536; text-safe PNGs are 1200x1500; SVG files parse as XML; all short thread posts are under 140 characters; `git diff --check` passed.
- INDEX update: completed.
- Automation memory update: completed.
- Optional `generated_images/animal_img` mirror: not attempted.
- GitHub publication: not attempted; package is local-ready.

Avoid repeating Low's Pitcher Plant / ネペンテス・ローウィー / *Nepenthes lowii* after this package is completed unless explicitly requested.
