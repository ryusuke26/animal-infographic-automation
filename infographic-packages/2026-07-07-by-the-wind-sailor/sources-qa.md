# By-the-wind sailor sources and QA

Package: `infographic-packages/2026-07-07-by-the-wind-sailor`

## Topic and rotation

- Topic: By-the-wind sailor / Velella / カツオノカンムリ
- Scientific name: *Velella velella* (Linnaeus, 1758)
- Broad native region: Ocean/Global
- Lineage: Cnidaria; Hydrozoa; Porpitidae
- Habitat: open-ocean surface / neuston, warm and temperate seas
- Visual/ecological hook: a blue floating hydroid colony with a small clear triangular sail that catches wind at the sea surface
- Latest-eight region check before selection: Africa, Asia, North America, Central America/Caribbean, Australia/Oceania, Europe, Africa, South America. Ocean/Global had 0 appearances and the previous completed package was South America, so Ocean/Global was preferred.

## Evidence Lock

Evidence Lock status: complete.

Accepted public identity:
- English common name: By-the-wind sailor; Velella is also acceptable as a short common label.
- Japanese common name: カツオノカンムリ. Public copy also uses ベレラ as a readable name label.
- Scientific name: *Velella velella*.
- Naming caveat: public copy must not call it a true jellyfish. It is a floating hydrozoan colony, related to jellyfish, sea anemones, and corals within Cnidaria.

Conservation/status lock:
- Global IUCN assessment: no global IUCN species assessment confirmed in the 2026 search.
- Assessment year: not applicable.
- Poster/main-post footer, Japanese: `世界全体のIUCN評価は確認できず（2026年確認）`
- Poster/main-post footer, English: `No global IUCN assessment confirmed (checked 2026)`
- Do not use formal `IUCN Not Evaluated (NE)` unless a direct authoritative source later supports that category.

Locked public claims:
1. It floats at the ocean surface as a blue hydrozoan colony, not a true jellyfish.
2. A small stiff/clear sail catches the wind and moves the colony across the surface.
3. Tentacles/polyps hanging below the float catch plankton; wind shifts can strand many on beaches.

Threats and population:
- No population number, population trend, legal status, current threat ranking, rescue framing, blame, or urgency claim is used.
- Public copy mentions no threats.

Visual identity guidance:
- Show one blue oval raft/float at the sea surface, with a small transparent triangular sail rising above it.
- Show short blue-purple tentacles/polyps below the raft in water.
- Keep it as one colony, not a swarm, not a true bell-shaped jellyfish, not a Portuguese man o' war, not a generic blue plastic shape.
- No fake map, beach-stranding pile, people, pets, rescue imagery, warning icon, population chart, or stinging-danger scene.

## Sources

- World Register of Marine Species route for taxonomic name: `https://www.marinespecies.org/` search for *Velella velella* (dynamic page access may vary; used as the taxonomic route without relying on an unverified local AphiaID).
- National Park Service / Point Reyes descriptions are cited through current news excerpts because the NPS page did not surface directly in search here. Publicly attributed claims: Velella are free-floating hydrozoans related to jellyfish, sea anemones, and corals; they live at the ocean surface; the clear sail catches wind; strong onshore winds strand them.
- San Francisco Chronicle, 2026-04-28, "Why thousands of blue sea creatures are suddenly appearing on California beaches": current secondary route quoting NPS/Point Reyes for hydrozoan identity, sail movement, wind-driven stranding, and surface life.
- Scripps Institution of Oceanography context via Axios San Diego, 2024-04-30: Velella are not true jellyfish, are typically harmless to humans, have a sail-like appendage, and surface when conditions provide zooplankton activity.
- General natural-history cross-check: widely available encyclopedic and literature summaries agree that *Velella velella* is a blue neustonic hydrozoan colony with a sail and underside feeding polyps.
- IUCN check: searches for `site:iucnredlist.org "Velella velella"` and `Velella velella IUCN Red List` returned no direct species assessment in this run; public copy uses conservative no-assessment-confirmed wording.

## Phase 2.5 independent verifier trial

Automation memory already contains the exact marker `Independent verifier trial: completed`, so the one-run verifier trial was not repeated. Local independent checklist result: no material conflict found in accepted name, broad range/habitat, three public claims, footer wording, or visual identity guidance. Keep the source-access caveat visible because the direct NPS and WoRMS pages may be dynamic in this environment.

## Copy Lock

Copy Lock status: complete.

Japanese title: カツオノカンムリ
English title: By-the-wind sailor
Scientific name line: *Velella velella*

Japanese observation labels:
- 海面にうく青い群体
- 小さな帆で風まかせ
- 下の触手でプランクトン

English observation labels:
- Blue colony at the surface
- A tiny sail catches wind
- Hanging polyps catch plankton

## Phase 3.5 dual copy review

Status before Image Gen: complete. Two read-only reviewers found no factual blocker. Both flagged the deterministic footer-label rule for poster/main-post text; accepted and fixed by removing `保全メモ：` / `Conservation note:` from poster copy, image prompts, and X main posts. Source-note prefixes and direct HTTPS links remain only in the separate source/context replies. Validator passed after the fix.

## Phase 5 image QA

Status: complete.

Accepted direct Image Gen source posters:
- Japanese: `images/by_the_wind_sailor_japanese_imagegen_2026-07-07.png`, 1024x1536, exact vertical 2:3.
- English: `images/by_the_wind_sailor_english_imagegen_2026-07-07.png`, 1024x1536, exact vertical 2:3.

Normalized posting PNGs:
- Japanese: `images/by_the_wind_sailor_japanese_posting_2026-07-07.png`, 1024x1536.
- English: `images/by_the_wind_sailor_english_posting_2026-07-07.png`, 1024x1536.

Ratio/normalization:
- Both accepted direct Image Gen source posters were already 1024x1536 and exact vertical 2:3.
- Posting PNGs were created with `scripts/normalize_poster.py` using bundled workspace Python.
- No padding, border, cropping, or stretching was used to repair a wrong-ratio source.

Visual/text QA:
- Japanese poster accepted after one targeted retry for title-text caution. The first Japanese source is retained as `images/by_the_wind_sailor_japanese_imagegen_2026-07-07_text_superseded.png` and is not for posting.
- Accepted Japanese poster text matches Copy Lock: `カツオノカンムリ`, `Velella velella`, three observation labels, and label-free 2026 no-IUCN-assessment footer.
- Accepted English poster text matches Copy Lock: `By-the-wind sailor`, `Velella velella`, three observation labels, and label-free 2026 no-IUCN-assessment footer.
- Identity QA passed: one blue oval floating colony at the sea surface, transparent triangular sail, short blue-purple hanging tentacles/polyps, open-ocean surface setting.
- Lookalike/anatomy risks checked: not a bell-shaped true jellyfish, not a Portuguese man o' war, not a swarm, no fake map, no beach-stranding pile, no warning/rescue scene.
- Post-image independent checklist was local because the one-run verifier trial was already completed in a prior run and no verifier was kept for this package.

## Phase 5.5 dual final review

Status: complete. Two read-only reviewers checked the final package before INDEX/memory closeout. Auto-fix applied: Japanese ALT text no longer says `保全メモ` because the accepted poster/main-post footer is label-free under the current rule. No unresolved blockers remained. Final validator passed; X block lengths are Japanese 176/84/176 and English 279/224/254. `git diff --check` was clean.
