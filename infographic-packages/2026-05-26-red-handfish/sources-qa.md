# Sources and QA: Red Handfish

## Publication-Safe Claims

| Field | Checked wording | Confidence | Evidence |
|---|---|---|---|
| Identity | Red Handfish / *Thymichthys politus* | high | DCCEEW 2023; Fishes of Australia 2025 |
| Japanese label | レッドハンドフィッシュ (transliteration) | medium | Based on confirmed official English common name; no standardized Japanese vernacular located |
| Taxonomy | Actinopterygii > Lophiiformes > Brachionichthyidae > *Thymichthys* | high | Fishes of Australia 2025; Tasmania 2020 |
| Place | Endemic to Tasmania; known in south-eastern Tasmania | high | DCCEEW 2023; Fishes of Australia 2025 |
| Habitat | Reef-associated shallow habitat with macroalgae, weeds or seagrass nearby | high | Fishes of Australia 2025; Tasmania 2020 |
| Movement hook | Modified hand-like fins are used to walk over the seabed | high | DCCEEW 2023; Tasmania 2020 |
| Reproductive hook | Eggs are attached at green algae or upright substrates and guarded until hatch | high | Fishes of Australia 2025; Reef Life Survey |
| Global status | IUCN Red List 2020: Critically Endangered (CR) | high | IUCN assessment citation displayed by Fishes of Australia; Reef Life Survey IUCN display |
| Threats | Seaweed habitat degradation and isolation of small populations | high | DCCEEW 2023 |
| Population numbers | Not used in public assets | high | Conservative editorial decision |

## Source-Date Reconciliation

- The Tasmanian listing statement, prepared before the IUCN publication cycle completed, labels IUCN CR as pending.
- The completed IUCN Red List assessment is cited as `Stuart-Smith, Edgar & Last 2020, e.T123423510A123424379` by Fishes of Australia.
- Reef Life Survey currently displays `IUCN Status: Critically Endangered` and says its monitoring contributed to that Red List evaluation.
- The public footer therefore uses `IUCN Red List 2020: Critically Endangered (CR)` without merging Australian EPBC or Tasmanian statutory labels.

## Asset Checklist

| Asset | Status |
|---|---|
| Japanese infographic copy | complete |
| English infographic copy | complete |
| Japanese Image Gen prompt | complete |
| English Image Gen prompt | complete |
| Japanese X post and ALT text | complete |
| English X post and ALT text | complete |
| 140-character thread drafts | complete; each item under 140 characters |
| Japanese Image Gen PNG | complete; inspected; 1024 x 1536 |
| English Image Gen PNG | complete; inspected; 1024 x 1536 |
| Japanese text-safe SVG/PNG | complete; SVG parsed and PNG inspected; 1200 x 1500 |
| English text-safe SVG/PNG | complete; SVG parsed and PNG inspected; 1200 x 1500 |

## Image QA Checklist

- One small bottom-dwelling fish is shown, not a human hand, frog, octopus, seahorse, or generic tropical fish.
- Enlarged pectoral fins look hand-like and contact the seabed in a walking posture.
- Body is red, pink-red, or mottled red/tan with plausible pale fin edging.
- Habitat shows shallow reef sand/rock and low green algae or seagrass rather than coral-reef fantasy scenery.
- No fake map, population count, alarming slogan, rescue framing, or legal-status confusion.
- Generated lettering may be imperfect; text-safe PNGs are authoritative for final typography.

## Image QA Result

- Japanese Image Gen raster: pass. The Japanese title is prominent; the red fish has bottom-contacting hand-like fins, shallow seaweed habitat and a quiet IUCN footer.
- English Image Gen raster: pass. The fish identity, seabed walking pose, seaweed habitat, egg-placement inset and footer are coherent.
- Text-safe backups: pass. Both SVGs parse as XML; both PNG renders preserve exact copy and status wording.
- SVG rasterization used Chrome headless after Edge headless failed; temporary renderer profiles were removed from the canonical package and retained outside it because browser file locks blocked deletion.
- Optional `generated_images/animal_img` mirror was not attempted.

## Sources

- https://www.dcceew.gov.au/environment/biodiversity/threatened/action-plan/priority-fish/red-handfish
- https://fishesofaustralia.net.au/home/species/4323
- https://nre.tas.gov.au/Documents/Red%20Handfish%20Listing%20Statement.pdf
- https://reeflifesurvey.com/species/thymichthys-politus/
- https://doi.org/10.2305/IUCN.UK.2020-1.RLTS.T123423510A123424379.en
