# Jellyfish Tree / ジェリーフィッシュ・ツリー

Status: `completed, local-ready`

Workflow mode: Quality Run

Run mode note: Caution Run is limited to resolving a source disagreement about whether the English name refers to the flower or opened fruit. Public copy describes the opened fruit without asserting the name's etymology.

Region: Mahé, Seychelles / Africa

Broad native region: Africa

Editorial classification group: Plants

Accepted scientific name: *Medusagyne oppositifolia*

Japanese naming note: `ジェリーフィッシュ・ツリー` is a transparent katakana rendering of the documented English common name `Jellyfish Tree`; no established standard Japanese common name was confirmed.

## Production files

- [Evidence and fact-check record](sources-qa.md)
- [Official IUCN assessment PDF](evidence/IUCN.UK.2025-2.RLTS.T37781A262047825.en.1.pdf)
- [Matching IUCN Red List page capture](evidence/iucn-red-list-jellyfish-tree-2025-page.png)
- [Japanese Copy Lock](infographic-copy-ja.md)
- [English Copy Lock](infographic-copy-en.md)
- [Japanese Image Gen prompt](image-prompt-ja.md)
- [English Image Gen prompt](image-prompt-en.md)
- [日本語の投稿セット](x-post-ja.md)
- [English posting set](x-post-en.md)

## Poster plan

One complete small tree grows from an exposed granite outcrop on Mahé. Its dark, thick leaves occur in opposite pairs, while a few small opened fruits show many narrow valves radiating from a central column like umbrella ribs. Exactly three unequal illustrated cards trace the habitat, opposite leaves, and opened fruit. Granite rubbings, leaf studies, and irregular field-note scraps are composed around the tree rather than placed in equal software panels.

## Poster files

- [Japanese direct Image Gen poster](images/jellyfish_tree_japanese_imagegen_2026-08-16.png)
- [Japanese posting PNG](images/jellyfish_tree_japanese_posting_2026-08-16.png)
- [English direct Image Gen poster](images/jellyfish_tree_english_imagegen_2026-08-16.png)
- [English posting PNG](images/jellyfish_tree_english_posting_2026-08-16.png)

## Posting sidecars

- [Japanese main post](images/jellyfish_tree_japanese_posting_2026-08-16.caption.txt)
- [Japanese story reply](images/jellyfish_tree_japanese_posting_2026-08-16.story-reply.txt)
- [Japanese ALT text](images/jellyfish_tree_japanese_posting_2026-08-16.alt.txt)
- [Japanese source note](images/jellyfish_tree_japanese_posting_2026-08-16.source-note.txt)
- [English main post](images/jellyfish_tree_english_posting_2026-08-16.caption.txt)
- [English story reply](images/jellyfish_tree_english_posting_2026-08-16.story-reply.txt)
- [English ALT text](images/jellyfish_tree_english_posting_2026-08-16.alt.txt)
- [English source note](images/jellyfish_tree_english_posting_2026-08-16.source-note.txt)

## Evidence route

The user-supplied official IUCN assessment PDF and matching Red List page capture directly confirm Global Critically Endangered (CR) under C2a(ii), assessed 12 August 2025 and published in 2025 as record `e.T37781A262047825`. The public footer therefore uses assessment year 2025. Kew Plants of the World Online accepts *Medusagyne oppositifolia*, places it in Ochnaceae, and records Mahé, Seychelles, as its native range. Seychelles Parks and Gardens Authority supports the exposed-rock habitat and opened-fruit form, while a peer-reviewed Kew-linked study supports the small-tree habit and opposite leaves.

The official assessment records 86 mature individuals and a decreasing trend. Those values remain evidence context and are not added to the poster, main post, or story reply. The C2a(ii) criterion appears only in the labeled source/context reply.

## Locked visual concept

An authored island-botany field notebook follows one complete *Medusagyne oppositifolia* from exposed Mahé granite to thick opposite leaves and a close view of the many-parted opened fruit. The organism remains a real woody tree; the fruit must not become an animal jellyfish, a flower with tentacles, or an umbrella canopy.

## Visual acceptance

- The first Japanese source passed the exact-2:3/full-canvas gate and visual review without a retry. It has one complete tree on exposed granite, clearly paired opposite leaves, several attached dry fruits, exact Copy Lock, and exactly three numbered illustrated cards.
- The first English companion passed the source gate and preserved the accepted composition, but its footer joined `CriticallyEndangered`. One allowed targeted Image Gen correction fixed the spacing but redrew the full canvas, so that broad edit was rejected.
- A deterministic text-safe repair copied only the corrected footer interior onto the accepted first English artwork. The changed bounding box is limited to `(78, 1438, 948, 1507)` on the `1024x1536` canvas; the complete tree, habitat, cards, and all non-footer artwork remain from the accepted first companion.
- After the official 2025 assessment became directly inspectable, both accepted source posters received a second deterministic localized repair limited to the year digits in the footer: Japanese difference box `(512,1449)-(560,1492)` and English difference box `(442,1462)-(482,1498)`. The superseded 2007-footer canonical images are preserved under `evidence/superseded-2007-posters/`; the hero tree, habitat, cards, and all non-footer artwork remain unchanged.
- At the user's request, the two explicitly rejected English audit sources were moved to the Windows Recycle Bin after their exact paths and hashes were verified. Only the four canonical Japanese/English direct and posting PNGs remain in `images/`.

## Final QA

- Both canonical direct posters pass the exact vertical 2:3 and full-canvas source gate.
- Both posting PNGs are exact `1024x1536` and pixel-identical to their accepted direct source.
- Full-size and phone-size visual review passed for the complete tree, exposed-granite habitat, opposite paired leaves, attached opened fruit, readable locked text, and exactly three numbered illustrated cards.
- Japanese and English main posts and story replies are independently within 275 Unicode characters; both main posts contain `#JellyfishTree` and use openings distinct from the latest two completed posts.
- Eight sidecars exactly match the four fenced blocks in each posting set.
- Bilingual X-format validation, full package validation, and whitespace QA pass.
- Official evidence SHA-256: `F41071918BBA3A30461F6EF52B601E84D596EB653A754A0B4BE10BC48C88F1DA` (assessment PDF) and `29956D1F13D14482F37847BB132DFA44F98E715B958626E187DF280F0A10FD3C` (Red List page capture).
- `infographic-packages/INDEX.md`, Automation memory, `automation-2-current-state.md`, and `daily-quality-loop.md` are synchronized to the official 2025 assessment. The two previously unwritable metadata files were rebuilt as new filesystem objects; their unchanged originals are retained under `repair-backups/2026-08-17-automation-2-file-identity/`, and write-handle checks now pass.
- Package state is `completed, local-ready`; Git and GitHub were not mutated.
