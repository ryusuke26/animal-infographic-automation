# Puya raimondii Infographic Package

Date: 2026-06-12
Package: `2026-06-12-puya-raimondii`
Topic: Queen of the Andes / プヤ・ライモンディ
Scientific name: *Puya raimondii*
Broad native region: South America
Lineage: Plantae, Bromeliaceae
Status: completed; published

## Rationale

South America had 0 appearances among the most recent 8 completed packages. The
previous run was North American, so this is also a non-consecutive region. The
high-Andes plant lineage, rocky puna habitat, giant spiny rosette, and
once-in-a-lifetime flower spike are distinct from the recent snake, pelagic
tunicate, pitcher plant, stream mammal, bat, fungus, and island insect topics.

## Locked Public Claims

1. *Puya raimondii* is native to the high Andes of Peru and Bolivia.
2. It forms a giant basal rosette of many stiff, narrow, spiny leaves and can
   raise a very tall central flower spike.
3. It is monocarpic: after a long vegetative life, the parent flowers once,
   produces seed, and dies.

## Locked Footer

```text
IUCN Red List 2009: Endangered (EN)
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
  `images/puya_raimondii_japanese_imagegen_2026-06-12.png`.
- English direct Image Gen poster: accepted,
  `images/puya_raimondii_english_imagegen_2026-06-12.png`.
- Visual QA: passed. Both posters show one coherent mature plant with a huge
  ground-level rosette of many stiff toothed leaves, one tall central
  unbranched flower spike, small pale flowers, and an open rocky high-Andes
  habitat. No candelabra branching, pineapple fruit, cactus, palm, forest,
  duplicate spike, fake map, or rescue imagery appears.
- Text QA: passed by visual inspection. Both direct posters contain the locked
  title, scientific name, three observation labels, and dated IUCN footer once.
- Deterministic text-safe backups: Japanese and English SVG/PNG files exist.
- Mechanical QA: direct PNGs are 1024x1536 Japanese and 1003x1568 English;
  text-safe PNGs are 1200x1500; SVG files parse as XML; all thread posts are
  under 140 characters; `git diff --check` reports no whitespace errors.
- INDEX update: completed.
- Automation memory update: completed.
- Optional `generated_images/animal_img` mirror: not attempted.
- GitHub publication: completed to `origin/master`.

Avoid repeating Queen of the Andes / プヤ・ライモンディ /
*Puya raimondii* after completion unless explicitly requested.
