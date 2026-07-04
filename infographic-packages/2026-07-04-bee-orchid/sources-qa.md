# Bee Orchid Sources QA

Package: `2026-07-04-bee-orchid`
Topic: Bee orchid / ビー・オーキッド
Scientific name: *Ophrys apifera* Huds.
Region: Europe
Lineage: flowering plant, terrestrial orchid, Orchidaceae
Evidence Lock status: completed before Image Gen
Copy Lock status: completed before Image Gen

## Topic And Region Lock

Latest eight completed package regions before this selection:
Australia/Oceania, Central America/Caribbean, North America, Asia, Africa, Ocean/Global, South America, Europe.

All broad regions appear once in the latest eight, and the previous completed run was Australia/Oceania. Bee orchid adds a European flowering-plant subject and a grassland/floral mimicry hook after recent conifer, coral, clam, frog, mammal, cephalopod, and marsupial entries. It is not present in automation memory, INDEX, or package folder names.

Selected hook: a grassland orchid whose fuzzy brown lip looks like a small bee beneath pink sepals.

## Evidence Lock

### Accepted Names

| Field | Locked wording | Evidence | Verdict |
|---|---|---|---|
| English common name | Bee orchid | The Wildlife Trusts species page uses Bee orchid; Kew POWO confirms the scientific name. | accurate |
| Japanese title | ビー・オーキッド | Safe Japanese rendering of the English common name; avoids inventing a formal Japanese vernacular name. | publication-safe |
| Scientific name | *Ophrys apifera* Huds. | Kew Plants of the World Online lists *Ophrys apifera* Huds. as accepted, first published in 1762. | accurate |
| Taxonomy caveat | Many synonyms exist; use the accepted Kew name in public copy. | Kew POWO lists the accepted name and numerous synonyms. | accurate |

### Range, Habitat, And Region

| Claim | Locked wording | Evidence | Verdict |
|---|---|---|---|
| Broad native region | Europe | Kew native range begins Europe to Mediterranean and N. Iran; the poster frames the European grassland doorway. | accurate with scope note |
| Native range | Europe to the Mediterranean and North Iran | Kew POWO native range statement and country list. | accurate |
| Habitat | dry or chalky/limestone grassland and coastal grassland | Wildlife Trusts says dry, chalk and limestone grasslands and lists grassland/coastal habitats; Kew says temperate tuberous geophyte. | accurate |

### Traits And Ecology

| Claim | Locked wording | Evidence | Verdict |
|---|---|---|---|
| Bee-like flower | fuzzy brown lip with yellow markings, pink sepals like wings | Wildlife Trusts identification text. | accurate |
| Pollination hook | the flower mimics a female bee; males can attempt mating and transfer pollen | Wildlife Trusts overview/about text; public copy keeps it simple and avoids overgeneralizing to every region. | accurate with scope note |
| UK self-pollination caveat | in the UK, the right bee species is absent and bee orchids are self-pollinated | Wildlife Trusts page. Public copy keeps this jurisdiction-specific instead of making it a global conditional rule. | accurate |
| Underground life | a tuberous geophyte | Kew POWO general information. Public copy does not over-explain mycorrhizae. | accurate |

### Conservation Status

Locked status footer:

- Japanese: `保全メモ：世界全体のIUCN評価は確認できず（2026年確認）`
- English: `Conservation note: no global IUCN assessment confirmed (checked 2026)`

Evidence and caveat:

- A global IUCN Red List species assessment could not be confirmed during the 2026 check. No formal IUCN category is assigned in public copy.
- Kew POWO and Wildlife Trusts were used for accepted name, range, habitat, and visual/ecology claims.
- Wildlife Trusts records a jurisdiction-specific UK note: protected in Northern Ireland under the Wildlife Order, 1985. This is not converted into a global status and is not used in the poster footer.
- Orchidaceae are broadly regulated under CITES Appendix II, but trade control is not central to this curiosity-first post and is not used as the public status footer.
- No population number, trend, threat ranking, blame, rescue, or urgency wording is used.

## Three Core Public Claims

1. Bee orchid is a terrestrial orchid native from Europe through the Mediterranean region.
2. It grows in open grassland settings, especially dry or chalky/limestone grassland.
3. Its fuzzy brown lip with yellow markings looks bee-like; in some places pollination involves bee mimicry, while Wildlife Trusts notes UK plants are self-pollinated because the right bee species is absent there.

## Visual Identity Guidance

Show one flowering bee orchid plant in open chalk/limestone grassland. Important visual cues:

- slender green stem with a small rosette or narrow green leaves;
- several flowers, but one large hero flower should dominate the poster;
- three pink sepals like soft wings;
- fuzzy rounded brown lip/labellum with yellow markings and a bee-like abdomen pattern;
- small green petals/central column near the lip;
- short grass, pale limestone pieces, and warm meadow light;
- no actual oversized bee as the hero, no honeycomb, no hive, no cartoon bee face, no fake map, no garden pot, no cutaway, no duplicate poster panels, no rescue or threat imagery.

## Source List

- Plants of the World Online, Kew: *Ophrys apifera* Huds., https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:647746-1. Used for accepted name, publication, native range, and tuberous geophyte/temperate biome context. Accessed 2026-07-04.
- The Wildlife Trusts: Bee orchid, https://www.wildlifetrusts.org/wildlife-explorer/wildflowers/bee-orchid. Used for common name, flower identity, habitat, UK self-pollination caveat, and Northern Ireland jurisdiction note. Accessed 2026-07-04.
- IUCN Red List public search/check, 2026-07-04. No global species assessment confirmed for public footer; no formal NE category assigned.
- CITES Appendices context, 2026-07-04. Orchidaceae broadly appear in Appendix II; not used as the poster footer because this package does not discuss trade.

## Independent Verifier Trial

The automation memory already contains the exact marker `Independent verifier trial: completed`, so no new Phase 2.5 verifier was spawned. Local independent checklist result: accepted name, broad native region, habitat, three public claims, conservative status footer, and visual identity guidance were checked against the source list above. No unresolved material conflict.

## Phase 3.5 Dual Copy Review

Completed before Image Gen with two read-only reviewers. Auto-fixes applied after reviewer findings: changed the Japanese visible label from generic flower-petal wording to `ハチみたいな唇弁`; narrowed self-pollination wording to the sourced UK-specific caveat; changed awkward `IUCN全球評価` to `世界全体のIUCN評価`; fixed Japanese source-note wording; shortened English X main/source copy to fit standard posting length. Validator was rerun and passed. No unresolved placeholders, mismatched years, unsupported category, or X-format issue remained before Image Gen.

## Phase 5 Visual And Mechanical QA

Completed after Image Gen.

- Japanese direct Image Gen poster: `images/bee_orchid_japanese_imagegen_2026-07-04.png`, 1024x1536, exact vertical 2:3.
- English direct Image Gen poster: `images/bee_orchid_english_imagegen_2026-07-04.png`, 1024x1536, exact vertical 2:3.
- Japanese posting PNG: `images/bee_orchid_japanese_posting_2026-07-04.png`, 1024x1536.
- English posting PNG: `images/bee_orchid_english_posting_2026-07-04.png`, 1024x1536.
- `scripts/normalize_poster.py` succeeded for both language versions using bundled workspace Python. No padding, border, cropping, or stretching was used; direct sources were already exact 2:3.
- Japanese first direct poster was rejected for a potentially ambiguous generated footer glyph in `確認できず`; it is retained as `images/bee_orchid_japanese_imagegen_2026-07-04_text_superseded.png` and must not be posted.
- Visual identity QA passed locally for the accepted posters: one terrestrial orchid in chalk/limestone grassland, pink sepals, fuzzy brown/yellow labellum, narrow green leaves, exactly three observation labels, and quiet status footer. No actual oversized bee, honeycomb, hive, fake map, garden pot, duplicate panel, population graphic, or rescue imagery.
- Text QA passed locally for accepted posters: Japanese shows `ビー・オーキッド`, `Ophrys apifera`, the three locked Japanese labels, and `保全メモ：世界全体のIUCN評価は確認できず（2026年確認）`; English shows `Bee Orchid`, `Ophrys apifera`, the three locked English labels, and `Conservation note: no global IUCN assessment confirmed (checked 2026)`.
- X post validator passed after copy-review fixes.
- Japanese and English main posts and source/context replies are under standard 280-character posting length; ALT text is intentionally longer.
- Thread draft posts are under 140 characters.

## Phase 5.5 Dual Final Review

Completed before INDEX and automation-memory completion updates with two read-only reviewers. Accepted findings: README and sources QA still had stale pending status, INDEX entry was missing, the superseded Japanese poster needed explicit labeling, and the English source note could be misread as tying the Wildlife Trusts URL to the IUCN search. Auto-fixes applied: completion notes updated, INDEX entry added in Phase 6, superseded Japanese poster documented, and English source note reordered. Reviewer concern that Japanese copy labels were collapsed was rejected after local UTF-8 readback confirmed separate lines in copy and prompt files. No unresolved blockers remain.
