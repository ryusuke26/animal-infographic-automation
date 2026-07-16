# Cookiecutter Shark Infographic Package

Status: completed, published (Caution Run)

## Primary posting sets

- [日本語の投稿セット](x-post-ja.md)
- [English posting set](x-post-en.md)

## Copy-Ready Posting Files

### Japanese sidecars

- [Japanese caption](images/cookiecutter_shark_japanese_posting_2026-07-16.caption.txt)
- [Japanese ALT text](images/cookiecutter_shark_japanese_posting_2026-07-16.alt.txt)
- [Japanese source note](images/cookiecutter_shark_japanese_posting_2026-07-16.source-note.txt)

### English sidecars

- [English caption](images/cookiecutter_shark_english_posting_2026-07-16.caption.txt)
- [English ALT text](images/cookiecutter_shark_english_posting_2026-07-16.alt.txt)
- [English source note](images/cookiecutter_shark_english_posting_2026-07-16.source-note.txt)

## Rationale

ダルマザメは、暗い外洋を昼夜で上下に移動し、腹側を青く光らせながら大きな動物から丸い一片をくり抜く小さなサメ。深い海の青、黒いのどの帯、ほぼ左右対称の尾びれが一目で伝わるため、自然史の発見を先に置く三つの観察カードに向いている。保全情報は主役にせず、IUCNの短いフッターにとどめた。

## Locked claims

1. It moves through warm oceanic waters, staying deeper by day and rising toward the surface at night.
2. Its underside emits blue light; it is a small shark, about 50 cm long.
3. Its jaws can remove a nearly round plug of flesh from larger fish and whales.

The package intentionally contains no population number, trend estimate, threat ranking, legal claim, blame framing, rescue framing, or urgency slogan.

## Evidence and status note

The global footer is `IUCN Red List 2017: Least Concern (LC)` / `IUCN Red List 2017：低懸念（LC）`. The user-provided official IUCN assessment PDF directly confirms `Scope: Global`, `Least Concern (LC)`, `Year Published: 2018`, and `Date Assessed: July 4, 2017` for *Isistius brasiliensis* (Kyne 2018, e.T41830A2956761; inspected locally at `C:\Users\ryusu\Downloads\IUCN.UK.2018-2.RLTS.T41830A2956761.en.2.pdf`, pp. 1-3). The earlier live species-page block is process history only; no status-access caveat remains in public source replies. Full claim-by-claim evidence is in `sources-qa.md`.

## Completion notes

- Evidence Lock and the local independent evidence checklist were completed before Copy Lock.
- Copy Lock was completed before Image Gen; prompts quote the locked title, scientific name, three observations, and footer exactly.
- Japanese and English direct Image Gen posters are present in `images/` as active vertical 2:3 PNGs.
- Japanese and English posting PNGs are present at exact `1024x1536` dimensions, with no padding, borders, cropping, or stretching.
- `scripts/validate_x_post_format.py`, `scripts/validate_package.py`, bundled-Python normalization, sidecar synchronization, image dimensions, pixel identity, and `git diff --check` passed.
- Run mode is Caution because the user supplied stronger official evidence and Evidence Lock was reopened for this correction; the official PDF now directly supports the status footer.
- GitHub publishing completed in package commit `31bf7d4`; `origin/master` was verified at `31bf7d4be732a1410d1d3df43b25407eb1840b87`. The final state is `completed, published`.

## Sources

- [FishBase species summary](https://www.fishbase.se/summary/isistius-brasiliensis.html)
- [JAMSTEC BISMaL taxon record](https://www.godac.jamstec.go.jp/bismal/j/view/9001247)
- [Tokyo Metropolitan Center record](https://www.ifarc.metro.tokyo.lg.jp/watch/fish-zukan/rare/245.html)
- [NOAA cookiecutter jaw study record](https://repository.library.noaa.gov/view/noaa/48913)
- [Frontiers bioluminescence study](https://doi.org/10.3389/fmars.2021.627045)
- [Natural History Museum of Denmark IUCN-linked record](https://collections.snm.ku.dk/en/object/NHMD1519486)
- [Official IUCN assessment PDF / DOI](https://doi.org/10.2305/IUCN.UK.2018-2.RLTS.T41830A2956761.en) (Kyne 2018; local PDF inspected, pp. 1-3)
