# Infographic Package Index

Canonical package root: `C:\Users\ryusu\Documents\New project 2\infographic-packages`

This index is for the recurring automation "世界の知らない生きものインフォグラフィック日次作成". The workspace package folder is the source of truth. `C:\Users\ryusu\.codex\generated_images\animal_img` is only an optional mirror/cache when permissions allow.

## Completed / Avoid Repeating

| Date | Topic | Scientific name | Package | Status | Notes |
|---|---|---|---|---|---|
| 2026-04-29 | Pink Fairy Armadillo / ヒメアルマジロ | *Chlamyphorus truncatus* | `2026-04-29-pink-fairy-armadillo` | completed | Avoid repeat. |
| 2026-04-30 | Olm / オルム | *Proteus anguinus* | `2026-04-30-olm` | completed | Avoid repeat. |
| 2026-05-01 | Hispaniolan Solenodon / ヒスパニオラソレノドン | *Solenodon paradoxus* | `2026-05-01-hispaniolan-solenodon-remake` | completed | Remake package counts as completed. Use current global IUCN framing, not outdated ADW status. |
| 2026-05-01 | Star-nosed Mole / ホシバナモグラ | *Condylura cristata* | `2026-05-01-star-nosed-mole-remake` | completed | Remake package counts as completed. |
| 2026-05-01 | Long-eared Jerboa / オオミミトビネズミ | *Euchoreutes naso* | `2026-05-01-long-eared-jerboa` | completed | Caption shortened in `captions-short.md`. |
| 2026-05-02 | Yeti crab / イエティクラブ | *Kiwa hirsuta* | `2026-05-02-yeti-crab` | completed | Package-local `images/` contains Image Gen raster PNGs plus text-safe SVG/PNG backups; generated_images mirror succeeded with approval. |
| 2026-05-03 | Welwitschia / ウェルウィッチア | *Welwitschia mirabilis* | `2026-05-03-welwitschia` | completed | Package-local `images/` contains Image Gen raster PNGs plus text-safe SVG backups; optional generated_images mirror failed due permissions. Avoid repeat. |

| 2026-05-04 | Blue glaucus / アオミノウミウシ | *Glaucus atlanticus* | `2026-05-04-blue-glaucus` | completed | Package-local `images/` contains Image Gen raster PNGs plus text-safe SVG backups; optional generated_images mirror failed due sandbox permissions. Avoid repeat. |
| 2026-05-05 | Hooded Pitohui / ズグロモリモズ | *Pitohui dichrous* | `2026-05-05-hooded-pitohui` | completed | Package-local `images/` contains Image Gen raster PNGs plus text-safe SVG backups. Avoid repeat. |

| 2026-05-06 | Sargassum Frogfish / ハナオコゼ | *Histrio histrio* | `2026-05-06-sargassum-frogfish` | completed | Package-local `images/` contains Image Gen raster PNGs plus text-safe SVG backups. Avoid repeat. |

| 2026-05-06 | Aardwolf / アードウルフ | *Proteles cristatus* | `2026-05-06-aardwolf` | completed | Redo package for today's run; package-local `images/` contains Image Gen raster PNGs plus text-safe SVG backups. Avoid repeat. |

## Incomplete / Do Not Count As Completed

| Date | Topic | Scientific name | Package | Status | Notes |
|---|---|---|---|---|---|
| 2026-04-29 | Lowland Streaked Tenrec / シマテンレック | *Hemicentetes semispinosus* | `2026-04-29-lowland-streaked-tenrec` | incomplete | Failed/incomplete generation; may be remade if selected deliberately. |

## Needs Review / Clarify Later

| Date | Topic | Package | Reason |
|---|---|---|---|
| 2026-05-01 | Eastern Waterfan | `2026-05-01-eastern-waterfan` | Present in package folder but not confirmed in automation memory. Check contents before counting as completed. |

## Maintenance Rules

- Read automation memory first, then this index, then package folder names.
- Add every completed run here with topic, scientific name, package path, status, and one operational note.
- If a run is partial, put it under "Incomplete" instead of "Completed".
- Do not rely on `generated_images` as the archive of record.
- Keep package slugs and filenames ASCII.
