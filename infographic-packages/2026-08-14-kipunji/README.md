# Kipunji / キプンジザル

Status: `completed, local-ready`

Workflow mode: Quality Run

Evidence handling: Caution Run resolved with the user-supplied official IUCN assessment PDF and matching Red List page capture. They directly confirm Global EN, assessed 20 March 2018 and published in 2019; the older WCS CR label remains excluded from current status.

Region: Southern Tanzania / Africa

Broad native region: Africa

Editorial classification group: Mammals

Accepted scientific name: *Rungwecebus kipunji*

## Posting sets

- [日本語の投稿セット](x-post-ja.md)
- [English posting set](x-post-en.md)

## Poster files

- [Japanese direct Image Gen poster](images/kipunji_japanese_imagegen_2026-08-14.png)
- [Japanese posting PNG](images/kipunji_japanese_posting_2026-08-14.png)
- [English direct Image Gen poster](images/kipunji_english_imagegen_2026-08-14.png)
- [English posting PNG](images/kipunji_english_posting_2026-08-14.png)

## Posting sidecars

- [Japanese main post](images/kipunji_japanese_posting_2026-08-14.caption.txt)
- [Japanese story reply](images/kipunji_japanese_posting_2026-08-14.story-reply.txt)
- [Japanese ALT text](images/kipunji_japanese_posting_2026-08-14.alt.txt)
- [Japanese source note](images/kipunji_japanese_posting_2026-08-14.source-note.txt)
- [English main post](images/kipunji_english_posting_2026-08-14.caption.txt)
- [English story reply](images/kipunji_english_posting_2026-08-14.story-reply.txt)
- [English ALT text](images/kipunji_english_posting_2026-08-14.alt.txt)
- [English source note](images/kipunji_english_posting_2026-08-14.source-note.txt)

## Production files

- [Evidence and fact-check record](sources-qa.md)
- [Japanese Copy Lock](infographic-copy-ja.md)
- [English Copy Lock](infographic-copy-en.md)
- [Japanese Image Gen prompt](image-prompt-ja.md)
- [English Image Gen prompt](image-prompt-en.md)

## Official evidence files

- [IUCN assessment PDF](evidence/iucn_rungwecebus_kipunji_assessment_2019.pdf)
- [IUCN Red List page capture](evidence/iucn_rungwecebus_kipunji_species_page_2026-08-14.png)

## Evidence route

The accepted name is *Rungwecebus kipunji*. The user-supplied official IUCN PDF and matching Red List page capture directly confirm record `e.T136791A17961368`, scope Global, Endangered (EN), criteria `B1ab(ii,iii,iv,v)+2ab(ii,iii,iv,v)`, assessed 20 March 2018 and published in 2019. Public footers therefore use the assessment year 2018; 2019 remains only in source/citation context. The PDF's previous-assessments section records the 2008 CR assessment, so the WCS Tanzania CR label is outdated for current status while its habitat and discovery history remain usable. The Japanese name キプンジザル is supported by a peer-reviewed Japanese primatology paper.

## Locked visual concept

One complete adult Kipunji pauses on a broad mossy branch in a misty southern Tanzanian montane forest. Its shaggy gray-brown coat, broad erect crown crest, dark face and eyelids, dark hands and feet, paler belly, and long tail with a pale distal half remain visible and connected. Both hands and both feet have separate body origins, paths, and contact points; the tail begins at the pelvis and does not cross the torso. Three unequal field-note cards grow around the branch line: a layered mountain-forest vignette, one complete small profile emphasizing the crown crest and pale tail tip, and one complete calling animal with a restrained sound-wave sketch. The composition uses mist, moss, bark rubbings, and canopy gaps rather than a generic grid.

## Visual acceptance

- The first Japanese direct generation passed the exact-2:3/full-canvas gate and was accepted without a retry. It shows one complete dominant Kipunji with four separately traceable limbs and a pelvis-connected pale-tipped tail on a mossy branch, exact Japanese Copy Lock, and exactly three numbered species-specific illustrated cards.
- The first English companion used the accepted Japanese poster as a visual reference only and was accepted without a retry. It preserves the species identity, misty montane forest, branch-led composition, palette, handmade medium, hierarchy, and card concept while rendering the exact English Copy Lock and punctuation on a fresh canvas.
- Both posters remain coherent and readable at full size and phone size. The crown crest, dark face and limbs, shaggy gray-brown coat, pale distal tail, four branch contacts, and complete calling mini-animal remain visible without generic baboon or mangabey drift.
- After the official assessment date became directly inspectable, a broad Image Gen edit was rejected because it redrew more than the footer. The accepted direct posters instead received a deterministic localized text-safe repair limited to the final year digit: Japanese difference box `(539,1454)-(563,1492)` and English difference box `(537,1458)-(561,1496)`. All artwork and non-footer text remain unchanged.

## Final QA

- Topic and duplicate gate: passed
- Global-familiarity gate: passed
- Evidence Lock and Copy Lock: passed
- Pre-image package validation: passed
- Both canonical direct posters pass the exact vertical 2:3 and full-canvas source gate.
- Both direct/posting pairs are exact `1024x1536` and pixel-identical within their language.
- One complete dominant hero and exactly three numbered illustrated cards pass full-size and phone-size visual review in each language.
- Locked poster text is exact and legible, including the corrected 2018 assessment-year footer; English colon, apostrophe, hyphen, and `(EN)` spacing match Copy Lock.
- The Japanese and English main posts and story replies are independently within 275 Unicode characters; both main posts contain `#Kipunji` and open differently from the latest two completed posts.
- Eight sidecars exactly match the four fenced blocks in each posting set.
- Bilingual X-format validation, full package validation, direct-source validation, pixel-identity checks, and `git diff --check` pass.
- The official evidence artifacts are preserved with SHA-256 `378CD661E98BFE02C28CDD06B8F2DE6C03E6D1E026C7075DA8C39E9E654297FC` (PDF) and `3F3FAFAF9BD665478B3836AB868CD2DEAE89F557BFA4707A0E155E0FBB3D70EE` (page capture).
- Package state is `completed, local-ready`; Git and GitHub were not mutated.
