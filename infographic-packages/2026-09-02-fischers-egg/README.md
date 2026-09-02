# Fischer's Egg bilingual infographic package

State: `completed, published`

Workflow mode: Quality Run

Editorial classification group: Fungi and lichens

Broad native region: Tasmania, Australia, and New Zealand / Oceania

## Posting sets

- [日本語の投稿セット](x-post-ja.md)
- [English posting set](x-post-en.md)

## Poster files

- Japanese direct Image Gen poster: [fischers_egg_japanese_imagegen_2026-09-02.png](images/fischers_egg_japanese_imagegen_2026-09-02.png)
- Japanese posting PNG: [fischers_egg_japanese_posting_2026-09-02.png](images/fischers_egg_japanese_posting_2026-09-02.png)
- English direct Image Gen poster: [fischers_egg_english_imagegen_2026-09-02.png](images/fischers_egg_english_imagegen_2026-09-02.png)
- English posting PNG: [fischers_egg_english_posting_2026-09-02.png](images/fischers_egg_english_posting_2026-09-02.png)

## Copy-ready sidecars

- Japanese: [main post](images/fischers_egg_japanese_posting_2026-09-02.caption.txt), [story reply](images/fischers_egg_japanese_posting_2026-09-02.story-reply.txt), [ALT text](images/fischers_egg_japanese_posting_2026-09-02.alt.txt), [source note](images/fischers_egg_japanese_posting_2026-09-02.source-note.txt)
- English: [main post](images/fischers_egg_english_posting_2026-09-02.caption.txt), [story reply](images/fischers_egg_english_posting_2026-09-02.story-reply.txt), [ALT text](images/fischers_egg_english_posting_2026-09-02.alt.txt), [source note](images/fischers_egg_english_posting_2026-09-02.source-note.txt)

## Evidence and production files

- [Evidence Lock and Sources QA](sources-qa.md)
- [Official IUCN identity reference 1](evidence/iucn_claustula_fischeri_reference_1.jpg)
- [Official IUCN identity reference 2](evidence/iucn_claustula_fischeri_reference_2.jpg)
- [Japanese Copy Lock](infographic-copy-ja.md)
- [English Copy Lock](infographic-copy-en.md)
- [Japanese Image Gen prompt](image-prompt-ja.md)
- [English Image Gen prompt](image-prompt-en.md)

## Locked scope

- Accepted name: *Claustula fischeri* K.M.Curtis.
- English public name: Fischer's Egg, used by the IUCN assessment and Atlas of Living Australia; Bunyip Egg is an Australian alias.
- Japanese public name: フィッシャーズ・エッグ, a transparent katakana rendering of the official English name; no established standard Japanese common name was confirmed.
- Global status: IUCN Red List Endangered (EN) under B2ab(ii,iii,iv,v); C2a(i), assessed 25 June 2015 and published in 2015, record `T75720773A75720776`. The current page is annotated `Needs updating`.
- Public claims: it occurs on damp forest ground in Tasmania and New Zealand; its white hollow egg-shaped fruitbody emerges from a brown outer layer; a tear opens access to the dry brown spore mass inside.
- Discovery doorway: a forest-floor fungus that looks like a small white egg, yet opens to reveal a dry brown spore mass rather than a yolk.

## Production result

- The first Japanese generation passed the exact-2:3/full-canvas source gate, but a later user review caught `タスマシア` in Card 1 instead of the locked `タスマニア`. One targeted Image Gen edit produced the correct word but redrew 99.83362% of the canvas, so that candidate was rejected. A measured local text-safe repair changed only 659 pixels (0.04190%) inside `(194,337)-(221,364)`, with zero changes outside the bounded character cell; the accepted poster now renders `タスマニアとNZの湿った森に現れる`.
- The first English companion also passed without retry. It preserves the accepted forest-floor palette, root-and-leaf frame, hero form, unequal card concepts, and quiet footer while adapting the locked typography to English.
- Both direct sources and both posting PNGs are exact `1024x1536`; within each language the direct and posting files are pixel-identical.

## Final QA

- Both posters contain one dominant mature fruitbody, exactly three numbered species-specific illustrated cards, exact integrated Copy Lock, and a quiet status footer.
- Full-size and phone-size review confirm readable text, coherent damp-forest composition, matte white ovoid identity, irregular brown outer layer, dry brown cutaway interior, and no food-egg, puffball, truffle, potato, or stinkhorn silhouette.
- Eight copy-ready sidecars match the four fenced blocks in each posting set.
- Full-size and `360x540` phone-size re-review confirm the corrected Card 1 reads `タスマニア`, with its line break, neighboring glyphs, card illustration, and all non-target poster content preserved.
- Direct-source, bilingual X-format, full-package, dimension, pixel-identity, phone/full-size, card, composition, and species-identity QA pass.
- State is `completed, published`; the package was published directly to `origin/master` in content commit `510f058`.
