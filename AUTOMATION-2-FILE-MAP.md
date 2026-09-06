# Automation 2 File Map

Use this as the quick navigation map for the infographic automation.

## Active Files

| File | Role |
|---|---|
| `automation-2-updated-prompt.md` | Short execution entry point synchronized to the live Automation; references the quality policy. |
| `automation-2-production-policy.md` | Single source of production quality rules, approval budget, and exception modes. |
| `templates/visual-and-copy-brief.md` | Compact identity brief and cards-v2 copy syntax; reuse within existing package files. |
| `templates/x-post-copy-template.md` | Language-matched single-image posts, discovery hooks and exact copy structure. |
| `templates/x-launch-notes.md` | Optional profile/pinned-post drafts and a lightweight distribution experiment. |
| `scripts/README.md` | Helper commands and one-time offline X counting setup. |
| `scripts/sync_posting_sidecars.py` | Derives sidecars from primary X posting sets; checks only unless --write. |
| `automation-2-current-state.md` | Small current-state record for pending IUCN evidence, latest completion, regional rotation, and active quality counters. |
| `daily-quality-loop.md` | Active guidance first; old entries searched only for a relevant issue, not reread each run. |
| `scripts/validate_direct_poster.py` | Immediate read-only source gate: exact vertical 2:3 plus no material near-white/transparent edge band, before review or editing. |
| `scripts/normalize_poster.py` | Rechecks the source gate and resizes accepted direct posters to canonical `1024x1536` posting assets. |
| `scripts/compose_poster.py` | Optional deterministic fallback for old Fast Run packages, diagnostics, or preserved rescue artifacts; not a Quality Run completion substitute. |
| `scripts/validate_package.py` | Validates current direct-poster Quality Run packages and retains compatibility with Fast Run base/composer packages. |
| `scripts/sync_automation_prompt.py` | Safely replaces only the live Automation prompt and `updated_at`, preserving and verifying all schedule/runtime fields when the Automation API tool is unavailable. |
| `infographic-packages/INDEX.md` | Archive ledger for completed, incomplete, and needs-review packages. |
| `infographic-packages/YYYY-MM-DD-species-slug/` | Canonical package folder for each generated topic. |
| `infographic-packages/YYYY-MM-DD-species-slug/images/` | Canonical folder for separate direct Japanese/English Image Gen posters, exact-size posting PNGs, and sidecars. |

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
files must be exactly `1024x1536`; current Quality Run packages also retain
separate `*_japanese_imagegen_YYYY-MM-DD.png` and
`*_english_imagegen_YYYY-MM-DD.png` direct source posters. Fast Run packages
from 2026-07-25 through 2026-07-26 may instead retain one shared
`*_base_imagegen_YYYY-MM-DD.png`.
