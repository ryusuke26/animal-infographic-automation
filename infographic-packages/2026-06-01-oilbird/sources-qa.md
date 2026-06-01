# Sources and QA: Oilbird

## Verdict

Overall: Ready, with one status-source caveat.

The public package is safe because it avoids population numbers, local trend claims, threat claims, and exact map boundaries. The IUCN species page could not be opened directly in the current browser session, so the status is recorded with the exact IUCN taxon ID and assessment URL context from cross-references, and treated as a quiet footer rather than the main hook.

## Claim Check

| Claim | Verdict | Publication wording | Source |
|---|---|---|---|
| English common name is Oilbird | accurate | Oilbird | Encyclopaedia Britannica; ADW |
| Japanese common name is アブラヨタカ | accurate | アブラヨタカ | Kotobank |
| Scientific name is *Steatornis caripensis* | accurate | *Steatornis caripensis* | ADW; Britannica; Wikimedia Commons / Wikidata taxon records |
| Taxonomy | needs context | アブラヨタカ科の鳥 / oilbird family; avoid order-level claim | ADW uses Caprimulgiformes/Steatornithidae; Wikimedia/IOC-derived records use Steatornithiformes/Steatornithidae |
| Range | accurate with broad wording | 南米北部など / northern South American forests | ADW; Britannica |
| Habitat | accurate | caves by day; forests at night | ADW; Britannica |
| Diet | accurate | fruit-eating / 夜に果実を探す | ADW; Britannica |
| Echolocation | accurate | audible clicks help it move through darkness | PLOS ONE 2010; ADW; Britannica |
| Visual identity | accurate | reddish-brown bird with white spotting, large eyes, broad bill, gape bristles, cave/forest/fruit cues | ADW; Britannica; visual source cross-check |
| Conservation status | needs context | IUCN Red List 2016: Least Concern (LC) | IUCN taxon ID 22689633 / assessment URL cross-references; ADW status display; Wikidata cites IUCN Red List 2021.3 as LC |
| Population number | accurate omission | No number used | Policy choice; sources vary and are not needed for this post |
| Threats | accurate omission | No threat claim used | Policy choice |

## Source Notes

- [Animal Diversity Web: *Steatornis caripensis*](https://animaldiversity.org/accounts/Steatornis_caripensis/), University of Michigan Museum of Zoology. Used for common name, scientific name, range, cave habitat, fruit diet, and conservation-status cross-check.
- [Encyclopaedia Britannica: Oilbird](https://www.britannica.com/animal/oilbird). Used for broad natural-history description, cave life, fruit diet, and echolocation context.
- [Brinklov et al. 2010, PLOS ONE: Intense Echolocation Calls from Two 'Whispering' Bats and the Oilbird](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0008264). Used for the echolocation/clicking claim.
- [Kotobank: アブラヨタカ](https://kotobank.jp/word/%E3%81%82%E3%81%B6%E3%82%89%E3%82%88%E3%81%9F%E3%81%8B-3141469). Used for Japanese common-name check.
- [Wikimedia Commons category: *Steatornis caripensis*](https://commons.wikimedia.org/wiki/Category:Steatornis_caripensis). Used only as a taxonomy/status cross-reference showing IUCN taxon ID 22689633 and family/order treatment, not as the main biology source.
- [IUCN Red List information page](https://iucn.org/resources/iucn-red-list-threatened-species). Used for category-system context because the species assessment page itself was not directly fetchable during this run.

## Publication-Safe Wording

### Japanese

アブラヨタカ
Steatornis caripensis

洞窟で昼をすごす
夜に果実を探す
クリック音で暗闇を進む

IUCN Red List 2016: Least Concern (LC)

### English

Oilbird
Steatornis caripensis

Rests in caves by day
Searches for fruit at night
Clicks through the dark

IUCN Red List 2016: Least Concern (LC)

## Image Identity Guidance

- Show a bird, not a bat or owl.
- Key traits: reddish-brown body, pale/white spots, large dark eye, broad slightly hooked bill, long bristles around the gape, long wing and tail.
- Habitat cues: cave mouth, dark cave interior, humid northern South American forest outside, fruit branch.
- Avoid fake maps, population graphics, rescue/blame imagery, predatory talon emphasis, owl ear tufts, and bat wings.

## QA Notes

- Image Gen Japanese and English posters were generated and copied into `images/`.
- Visual identity passed: both show a reddish-brown spotted cave bird, large eye, bill bristles, cave entrance, forest, and fruit cues.
- Generated raster footers omit the 2016 assessment year, so text-safe backups and captions are authoritative for the dated IUCN wording.
- Text-safe SVG/PNG backups are required and included.
- No population number, local count, trend, map, or threat claim appears in public copy.
