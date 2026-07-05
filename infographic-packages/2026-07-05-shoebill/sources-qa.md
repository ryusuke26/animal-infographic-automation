# Shoebill Sources QA

Package: `2026-07-05-shoebill`
Topic: Shoebill / ハシビロコウ / *Balaeniceps rex*
Run date: 2026-07-05

## Topic And Region Lock

- Broad native region: Africa.
- Lineage: Bird; family Balaenicipitidae, a distinctive large wetland bird lineage.
- Habitat: extensive freshwater swamps and dense marshes, especially papyrus and reed wetlands with floating vegetation.
- Ecological / visual hook: a huge shoe-shaped bill, patient stand-and-wait hunting, and gray statue-like posture in African wetlands.
- Latest-eight completed package regions before selection: South America, Ocean/Global, Africa, Asia, North America, Central America/Caribbean, Australia/Oceania, Europe. Each appeared once; the immediately previous package was Europe, so Africa is allowed.
- Repeat check: not found in automation memory, INDEX completed entries, or package folder names.

## Evidence Lock

### Accepted Names

| Field | Locked value | Evidence |
|---|---|---|
| English common name | Shoebill | BirdLife DataZone species page and Animal Diversity Web use Shoebill / shoebill. |
| Japanese common name | ハシビロコウ | Standard Japanese common name; used as a public-facing rendering. |
| Scientific name | *Balaeniceps rex* | BirdLife DataZone page slug and Animal Diversity Web classification. |
| Naming caveat | Also called whale-headed stork / whale-headed bird in English; do not treat it as a true stork in public copy. | ADW records historical/common "shoebill or whale-headed stork"; taxonomy has been debated. |

### Conservation / Status Route

- Locked public footer, Japanese: `IUCN Red List 2018: Vulnerable (VU)`
- Locked public footer, English: `IUCN Red List 2018: Vulnerable (VU)`
- Assessment year: 2018.
- Basis: BirdLife DataZone hosts the current species factsheet for Shoebill and links the IUCN Red List assessment. The dynamic factsheet body did not fully render in the browser fetch, but search snippets and the page metadata identify the species, and ADW's generated page currently displays IUCN Red List: Vulnerable. Public copy uses only the category/year and avoids population numbers, trend, or threat ranking.
- CITES/legal context: ADW displays CITES Appendix II; not used in poster footer because the poster footer is reserved for the primary global status.

### Locked Public Claims

1. Shoebills live in large African freshwater swamps and dense marshes, often associated with papyrus/reed wetlands.
2. The bird has a huge shoe-shaped bill with a hooked tip and long legs; adults are gray overall.
3. It often hunts by standing still or walking slowly, then lunging/collapsing forward at fish such as lungfish, catfish, tilapia, and other wetland prey.

### Claims Not Used Publicly

- No population number is used because available numbers vary by source and were not needed for a curiosity-first post.
- No decline percentage, current threat ranking, or country-by-country legal protection claim is used.
- CITES Appendix II is recorded only as source context, not as the main conservation message.

## Source Notes

| Source | Use | Access / caveat |
|---|---|---|
| BirdLife DataZone, Shoebill *Balaeniceps rex* species factsheet, https://datazone.birdlife.org/species/factsheet/shoebill-balaeniceps-rex | Strongest formal status route for IUCN/BirdLife bird assessment and species identity. | Page opened and shows the IUCN Red List assessment section and assessor BirdLife International, but many detail values loaded dynamically; status year/category cross-checked with search result and ADW current display. |
| IUCN Red List species page, https://www.iucnredlist.org/species/22697583/134185102 | Direct official assessment URL for *Balaeniceps rex*. | Direct page body did not render in this environment; retained as official target URL with access caveat. |
| Animal Diversity Web, *Balaeniceps rex*, https://animaldiversity.org/accounts/Balaeniceps_rex/ | Classification, range, habitat, morphology, hunting behavior, diet, and secondary current status display. | ADW text includes some old conservation prose, so current public status relies on IUCN/BirdLife route; ADW's current status widget displays Vulnerable. |
| CITES Checklist, https://checklist.cites.org/ | Trade-listing context for Appendix II. | Search page is dynamic; public copy does not rely on CITES. |

## Visual Identity Guidance

- Show one large gray shoebill in a freshwater papyrus/reed swamp.
- Essential traits: massive pale yellowish shoe-shaped bill with dark mottling, hooked bill tip, large forward-facing eyes, gray body, long dark legs, long separate toes, subtle rear head crest.
- Safe pose: standing still or slow-walking in shallow water among papyrus/reeds; bill angled slightly downward; one prey fish may be suggested in water only if simple and not graphic.
- Avoid: generic heron, pelican, stork, crane, flamingo, toucan-like colors, open ocean, fake map, nest/chick scene, zoo bars, people, rescue or trade imagery, population icons.

## Independent / Local Verification

- Automation memory already contains `Independent verifier trial: completed`, so no new one-run verifier was spawned.
- Local pre-copy checklist result: accepted name, scientific name, Africa range, freshwater swamp habitat, three public claims, footer, and visual identity guidance reconciled against the listed sources. No unresolved material conflict.

## Copy Review

- Phase 3.5 spawned exactly two read-only copy reviewers, affirmative and critical.
- The affirmative reviewer later returned possible formatting concerns, but UTF-8 line-number readback showed the cited files were structurally correct; no copy change was needed.
- The critical reviewer timed out before Image Gen, so the allowed local two-pass fallback was used for critical review.
- Affirmative pass: kept status short and label-free; avoided population and threat claims.
- Critical pass: checked that Japanese X post has a species-specific line ending exactly with `ちょっと不思議な暮らし。`, that source replies begin with required labels, and that image prompts match locked facts.
- Validator result before Image Gen: `OK: ... use the canonical three-block format`.
- Unresolved blockers: none before Image Gen.

## Post-Image QA

- Japanese direct poster: `images/shoebill_japanese_imagegen_2026-07-05.png`, 1024x1536, exact vertical 2:3.
- English direct poster: `images/shoebill_english_imagegen_2026-07-05.png`, 1024x1536, exact vertical 2:3.
- Japanese posting PNG: `images/shoebill_japanese_posting_2026-07-05.png`, 1024x1536.
- English posting PNG: `images/shoebill_english_posting_2026-07-05.png`, 1024x1536.
- No padding, borders, cropping, or stretching were used to repair source ratio; direct sources were already exact 2:3.
- Visual identity QA: both posters show one gray shoebill-like bird in freshwater papyrus/reed wetland, with a massive pale yellow mottled shoe-shaped bill, hooked tip, large eye, long dark legs, separate long toes, and a still hunting posture. No generic heron, pelican pouch, crane/flamingo colors, fake map, zoo bars, people, nests, chicks, duplicate bird, population graphic, or rescue imagery.
- Text QA: both posters contain title, scientific name, exactly three observation callouts, and `IUCN Red List 2018: Vulnerable (VU)`. Japanese labels are legible enough for public posting.
- Independent verifier post-image path: one-run verifier marker already existed, so local post-image identity checklist was used. No unresolved anatomy, lookalike, habitat, or text blocker.

## Final Review

- Phase 5.5 spawned exactly two read-only final reviewers.
- Affirmative final reviewer reported apparent Japanese mojibake, label-line joining, and prompt-quote issues, but UTF-8 readback showed the cited Japanese files are structurally correct and readable; those findings were rejected as display/encoding artifacts.
- Earlier critical copy reviewer returned late with a valid blocker: Japanese and English source/context replies exceeded 280 characters. Both replies were shortened, and validator plus character counts were rerun. Final source/context reply lengths: Japanese 205, English 265.
- Critical final reviewer timed out, so local critical fallback checked required files, X format, source-note labels, Japanese ending rule, image dimensions, visual/text QA, and `git diff --check`.
- Auto-fixes applied: shortened Japanese and English X source/context replies only.
- Unresolved blockers: none.
