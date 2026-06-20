# Snow Plant Infographic Package

Date: 2026-06-20

Topic: Snow Plant / スノープラント / *Sarcodes sanguinea*

Package slug: `2026-06-20-snow-plant`
Status: completed, published

## Rationale

Selected for the North America rotation slot. North America had zero appearances among the latest eight completed packages, South America had two, and the previous package was Ocean/Global. The topic adds a non-animal lineage and a montane conifer-forest-floor habitat. Its curiosity hook is a scarlet flowering plant that has no chlorophyll and obtains carbon through fungi.

Alternatives considered before lock included a North American ice crawler and the Texas blind salamander. Snow Plant offered stronger lineage, habitat, and visual-hook contrast with the recent eight-package sequence while keeping the anatomy simple enough for one-hero poster QA.

## Locked Facts

- Broad native region: North America.
- Lineage: flowering plant; Ericaceae; Monotropoideae.
- Habitat: western North American montane conifer-forest floor and needle litter.
- Core claims: no chlorophyll; emerges through conifer litter; gets carbon through fungi.
- Public footer: `Conservation note: no global IUCN assessment confirmed (checked 2026)`.
- The footer is an evidence-availability note, not an IUCN Not Evaluated (NE) category.
- No population, trend, threat, rescue, or blame claim is used.

## Locks And Verification

- Evidence Lock: completed before Image Gen.
- Independent verifier trial: automation memory already contains `Independent verifier trial: completed`, so no new verifier was spawned. The local pre-copy checklist found no unresolved conflict. Visual cautions are mushroom/coral-fungus/pinecone confusion, accidental green leaves, oversized orchid petals, and growth directly from solid snow.
- Copy Lock: completed before Image Gen. Japanese and English titles, scientific name, three labels, footer, X copy, ALT text, thread drafts, and image prompts contain no unresolved placeholder.

## Completion Notes

- Japanese direct Image Gen poster: `images/snow_plant_japanese_imagegen_2026-06-20.png` - 1024x1536, vertical 2:3, accepted.
- English direct Image Gen poster: `images/snow_plant_english_imagegen_2026-06-20.png` - 1024x1536, vertical 2:3, accepted.
- Japanese posting PNG: `images/snow_plant_japanese_posting_2026-06-20.png` - exactly 1024x1536 and byte-identical to the accepted direct source.
- English posting PNG: `images/snow_plant_english_posting_2026-06-20.png` - exactly 1024x1536 and byte-identical to the accepted direct source.
- The direct outputs were already canonical size, so no resampling was needed. No padding, cropping, stretching, border repair, or deterministic replacement was used.
- Deterministic text-safe backups were not created because both direct posters contain readable locked text.
- Optional generated-images mirror was not attempted. Package-local files are the archive of record.

## Post-Image QA

- Text QA passed: each poster shows the correct language title, *Sarcodes sanguinea*, exactly three locked observation labels, and the locked conservative footer.
- Visual identity QA passed: one stout scarlet fleshy flowering shoot emerges through conifer needles; red scale-like bracts and multiple nodding cream-centered red-pink flowers are visible; no green leaves appear.
- Habitat QA passed: shaded conifer-forest floor with needle litter, stones, and cones; no fake map and no plant growing from solid snow.
- Lookalike QA passed: neither poster reads as a mushroom, coral fungus, red pinecone, ordinary leafy plant, orchid, rafflesia, or pitcher plant.
- Tone QA passed: no blame, urgency slogan, rescue framing, population graphic, or unsupported threat claim.
- Local post-image checklist was used because the one-run independent verifier trial was already completed in automation memory.
- Thread draft lines are under 140 characters.

## Publication

- Package state: completed and published to `origin/master` in commit `18b81cd` (`Add snow plant infographic package`).
- Avoid selecting this topic again unless explicitly requested.

## Mini Picture Book Extension

- Added the five-page Japanese mini picture book `森のちかの ひみつのバトン` under `storybook/`.
- All five page PNGs are direct Image Gen outputs at exactly 1024x1536 and vertical 2:3.
- The child-facing “food baton” metaphor was tightened so the source carbon begins with the tree's photosynthesis, passes through fungal hyphae, and reaches Snow Plant; the copy does not imply that Snow Plant is independent of sunlight at the ecosystem level.
- The first page 4 candidate was rejected because it placed the flowering shoot below ground. One targeted correction moved the red shoot above ground and retained only roots and hyphae below.
- Storybook copy, continuity lock, prompt summary, per-page QA, and final assets are recorded in `storybook/`.
