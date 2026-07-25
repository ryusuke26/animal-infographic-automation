# Automation 2 File Map

Use this as the quick navigation map for the infographic automation.

## Active Files

| File | Role |
|---|---|
| `automation-2-updated-prompt.md` | Current Fast Run Automation body text to synchronize into the Automation settings. |
| `automation-2-production-policy.md` | Human-readable Fast Run policy, approval budget, and exception modes. |
| `automation-2-current-state.md` | Small current-state record for pending IUCN evidence, latest completion, regional rotation, and active quality counters. |
| `daily-quality-loop.md` | Lightweight end-of-run improvement loop: priorities, tags, next actions, and skill-update triggers. |
| `scripts/compose_poster.py` | Builds deterministic Japanese and English `1024x1536` posters from one text-free Image Gen base plus locked copy. |
| `scripts/normalize_poster.py` | Legacy direct-poster normalizer; retained for existing packages and deliberate legacy runs. |
| `scripts/validate_package.py` | Validates Fast Run packages with one text-free base and two deterministic posting PNGs while retaining compatibility with legacy direct-poster packages. |
| `scripts/sync_automation_prompt.py` | Safely replaces only the live Automation prompt and `updated_at`, preserving and verifying all schedule/runtime fields when the Automation API tool is unavailable. |
| `infographic-packages/INDEX.md` | Archive ledger for completed, incomplete, and needs-review packages. |
| `infographic-packages/YYYY-MM-DD-species-slug/` | Canonical package folder for each generated topic. |
| `infographic-packages/YYYY-MM-DD-species-slug/images/` | Canonical folder for the text-free base, deterministic bilingual posting PNGs, and sidecars. |

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
files must be exactly `1024x1536`; Fast Run keeps one
`*_base_imagegen_YYYY-MM-DD.png` as the shared text-free source. Older packages
may retain separate language-specific direct Image Gen sources.
