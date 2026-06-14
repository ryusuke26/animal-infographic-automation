# Automation 2 File Map

Use this as the quick navigation map for the infographic automation.

## Active Files

| File | Role |
|---|---|
| `automation-2-updated-prompt.md` | Current Automation body text to paste into the Automation settings. |
| `automation-2-production-policy.md` | Human-readable operating policy and responsibility map. |
| `scripts/normalize_poster.py` | Rejects non-2:3 Image Gen posters and resizes accepted 2:3 sources to the canonical `1024x1536` posting size. |
| `infographic-packages/INDEX.md` | Archive ledger for completed, incomplete, and needs-review packages. |
| `infographic-packages/YYYY-MM-DD-species-slug/` | Canonical package folder for each generated topic. |
| `infographic-packages/YYYY-MM-DD-species-slug/images/` | Canonical image assets folder for Image Gen PNGs and text-safe backups. |

## Optional / Non-Canonical

| Path | Role |
|---|---|
| `C:\Users\ryusu\.codex\generated_images\animal_img` | Optional mirror/cache for generated images. Do not use as the source of truth. |
| `$CODEX_HOME/automations/automation-2/memory.md` | Run history and operational decisions. Important, but not the package archive. |

## Rule of Thumb

If a future run needs to know whether a topic is completed, check:

1. automation memory
2. `infographic-packages/INDEX.md`
3. package folders

If a future run needs to know where final upload assets are, check the
package-local `images/` folder for `*_posting_YYYY-MM-DD.png`. These posting
files must be exactly `1024x1536`; `*_imagegen_*.png` files preserve the direct
source output.
