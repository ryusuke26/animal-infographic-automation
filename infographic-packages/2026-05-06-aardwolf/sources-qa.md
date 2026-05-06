# Sources and QA Notes

## Source List

1. Mammal Diversity Database, *Proteles cristatus*, Southern Aardwolf. Accessed 2026-05-06. Used for current spelling, Hyaenidae taxonomy, distribution, taxonomy note that the epithet changed from *cristata* to *cristatus*, and IUCN Least Concern status display. https://www.mammaldiversity.org/taxon/1006074/
2. Animal Diversity Web, *Proteles cristata* account. Accessed 2026-05-06. Used for eastern/southern African range, dry savanna and grassland habitat, nocturnal behavior, dens, morphology, termite diet, sticky tongue, and conservation status. https://animaldiversity.org/accounts/Proteles_cristata/
3. National Geographic, "Aardwolf." Accessed 2026-05-06. Used for public-facing cross-check of common/scientific name, IUCN Least Concern display, 2014 assessment note, range, dry grassland habitat, termite diet, and visual traits. https://www.nationalgeographic.com/animals/mammals/facts/aardwolves
4. GBIF Backbone Taxonomy, *Proteles cristata* (Sparrman, 1783). Accessed 2026-05-06. Used for database cross-check of the older/common spelling, Hyaenidae placement, and English common name. https://www.gbif.org/species/2433502
5. Kotobank, アードウルフ / ツチオオカミ. Accessed 2026-05-06. Used for Japanese common names, Japanese public-facing description, termite diet, range, and morphology. https://kotobank.jp/word/%E3%81%82%E3%83%BC%E3%81%A9%E3%81%86%E3%82%8B%E3%81%B5-3142637
6. Britannica, "Aardwolf." Accessed 2026-05-06. Used as a secondary cross-check for termite-specialist diet, nocturnal dry-plains life, striped hyena-like appearance, and broad distribution. https://www.britannica.com/animal/aardwolf

## Taxonomy Note

Mammal Diversity Database uses *Proteles cristatus* and notes that the species epithet was changed from *cristata* to *cristatus* to match the masculine genus. GBIF, Animal Diversity Web, and National Geographic still display *Proteles cristata*. This package uses *Proteles cristatus* as the current main spelling and records *P. cristata* as an alternate/source spelling.

## Conservation Note

Mammal Diversity Database currently displays IUCN Red List status as Least Concern. National Geographic states that IUCN last assessed the aardwolf in 2014 and found it to be a species of little concern. This package uses a quiet footer only: "IUCN Red List: Least Concern (LC)." It does not include population numbers, trends, or threat-centered framing.

## Image Identity Guidance

Required traits:

- small slender hyena-like mammal
- large pointed ears
- long narrow muzzle
- buff-gray or yellowish coat
- dark vertical stripes, not spots
- dark mane along neck and back
- black lower legs and black tail tip
- dry grassland at dusk or night
- small termite mound or termite trail cue

Avoid:

- wolf-like face or dog-like body
- aardvark body or long aardvark snout
- spotted hyena spots
- dramatic hunting or attack scene
- fake maps
- population numbers
- guilt, blame, or rescue framing

## Completion QA Checklist

- [x] Topic does not repeat completed package list.
- [x] Redo package created separately from the earlier Sargassum frogfish package.
- [x] Different lineage/habitat from recent plant, sea slug, bird, and fish topics.
- [x] Japanese and English copy saved.
- [x] Japanese and English Image Gen prompts saved.
- [x] X posts, ALT text, and source replies saved.
- [x] Numbered X free-version thread drafts saved.
- [x] Source/QA notes saved.
- [x] Text-safe SVG backups saved.
- [x] Text-safe SVG XML validation passed.
- [x] Image Gen raster PNGs copied into `images/`.
- [x] Image Gen dimension check passed: Japanese 1024 x 1536; English 1024 x 1536.
- [x] Image QA: generated Japanese and English posters show aardwolf identity cues and readable core text. Package text and text-safe SVGs remain authoritative.
- [x] `infographic-packages/INDEX.md` updated.
- [x] Automation memory updated.
