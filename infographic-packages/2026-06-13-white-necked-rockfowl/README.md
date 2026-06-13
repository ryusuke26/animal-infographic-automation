# White-necked Rockfowl Infographic Package

Date: 2026-06-13
Package: `2026-06-13-white-necked-rockfowl`
Topic: White-necked Rockfowl / ハゲチメドリ
Scientific name: *Picathartes gymnocephalus*
Broad native region: Africa
Lineage: Animalia, Aves, Passeriformes, Picathartidae
Status: completed; published

## Rationale

Africa had 0 appearances among the most recent 8 completed packages. The
previous run was South American, so this is also a non-consecutive region.
The passerine lineage, rocky West African forest habitat, bare yellow head,
and mud cup nest beneath rock differ from the recent plant, snake, pelagic
tunicate, pitcher plant, stream mammal, bat, fungus, and island insect topics.

## Locked Public Claims

1. *Picathartes gymnocephalus* is native to rocky forests of West Africa.
2. Adults have a bare yellow head with large black facial patches, white
   underparts, dark upperparts, long legs, and a long tail.
3. The bird builds a deep mud cup nest attached beneath a protected rock
   surface.

## Locked Footer

```text
IUCN Red List 2018: Vulnerable (VU)
```

## File Manifest

- `sources-qa.md` - Evidence Lock, claim checks, visual guidance, and sources.
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
- Japanese direct Image Gen poster: accepted,
  `images/white_necked_rockfowl_japanese_imagegen_2026-06-13.png`.
- English direct Image Gen poster: accepted,
  `images/white_necked_rockfowl_english_imagegen_2026-06-13.png`.
- Visual QA: passed. Both posters show one coherent upright adult with a
  yellow-orange bare head, black facial patch, black bill, white throat and
  underparts, dark folded wings, two long pale legs, and one long dark tail in
  damp rocky forest. Each includes one mud cup nest attached beneath a rock
  overhang. No blue crown, red nape, yellow belly, extra limb, duplicated tail,
  exposed tree nest, hanging woven nest, fake map, or rescue imagery appears.
- Text QA: passed by visual inspection. Both direct posters contain the locked
  title, scientific name, three observation labels, and dated IUCN footer once.
- Deterministic text-safe backups: Japanese and English SVG/PNG files exist.
- Mechanical QA: direct PNGs are 1122x1402 Japanese and 1024x1536 English;
  text-safe PNGs are 1200x1500; SVG files parse as XML; all thread posts are
  under 140 characters; `git diff --check` reports no whitespace errors.
- INDEX update: completed.
- Automation memory update: completed.
- Optional `generated_images/animal_img` mirror: not attempted.
- GitHub publication: completed to `origin/master`.

Avoid repeating White-necked Rockfowl / ハゲチメドリ /
*Picathartes gymnocephalus* after completion unless explicitly requested.
