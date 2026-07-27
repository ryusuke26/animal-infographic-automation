# Automation 2 Current State

Updated: 2026-07-27T12:25:43+09:00

This file is the small replace-in-place state record for Automation
`automation-2`. Run history remains in automation memory.

## Workflow

- Default workflow: Quality Run with separate complete Japanese and English
  Image Gen posters, species-specific illustrated observation cards, and an
  editorial review of X copy.
- Fast Run base/composer packages remain supported for existing artifacts, but
  deterministic composition is no longer the default or a completion
  substitute for a new package.
- New-topic behavior: verify official evidence directly and continue without a
  user evidence stop. Request a screenshot or PDF only when the official route
  remains unavailable, ambiguous, or conflicting.
- Pending evidence package: none.
- Active package: none.
- Evidence route: user-supplied official IUCN species-page screenshot and
  matching ten-page assessment PDF for `e.T12142A50190292`, National Museum of
  Nature and Science, and Hammer et al. 2021.
- Confirmed: accepted taxon *Litocranius walleri*, Japanese standard name
  ジェレヌク, Global Near Threatened (NT), assessed 20 April 2016 and published
  2016, dry East African thornbush habitat, diagnostic body plan, and bipedal
  browsing.
- Phase 0 preflight: passed on 2026-07-27 in the no-approval local automation
  path.
- Gerenuk Quality Run: completed through Phase 5 on 2026-07-27. The official
  screenshot/PDF now directly confirm Global NT, assessed 20 April 2016 and
  published 2016; obsolete access caveats were removed from source replies.
- Live Automation prompt sync: completed on 2026-07-26 with the Quality Run
  prompt. `ACTIVE`, the daily 10:00 schedule, model, reasoning effort,
  execution environment, and project target remained unchanged.

## Latest Package

- Latest completed package: `2026-07-27-gerenuk`.
- State: `completed, local-ready`.
- Production: separate complete Japanese and English ImageGen posters.
  Japanese passed on its first generation. The English first generation and
  one targeted retry both substituted a curly apostrophe for the locked ASCII
  apostrophe; a one-glyph local text-safe repair was accepted without altering
  the integrated artwork.
- Visual QA: one complete bipedal-browsing adult male, exactly three
  species-specific illustrated cards, correct dry thorn-scrub habitat, complete
  diagnostic anatomy, locked text, phone-size coherence, and exact 1024x1536
  direct/posting pairs passed.
- Posting correction: restored the established hook -> common name ->
  scientific name -> discovery story sequence in both main posts. The X
  template and validator now guard the standalone identity lines for packages
  dated 2026-07-24 onward. The Japanese main post was then replaced with the
  user's preferred fuller discovery narrative, shortened to 273 characters;
  its posting caption sidecar is synchronized.
- Tomorrow's posting default: treat the main post as a separate, complete
  natural-history story. Use concrete scene, appearance, movement, and
  consequence details when supported; aim for roughly 220-275 characters
  without filler, and enforce a 275-character maximum for packages dated
  2026-07-28 onward.
- GitHub closeout: blocked on 2026-07-27 before staging because the current
  execution path cannot create `.git/index.lock`. System Git also cannot reach
  github.com. The connected GitHub app confirmed admin/push permission and that
  remote `master` is still identical to
  `b03881729632422f7e4baf5aa96f84cf06374646`, but no remote mutation was made
  because publishing without a matching local commit would desynchronize the
  canonical checkout. No stale index lock remains.

## Recent-Eight Region Rotation

1. 2026-07-20 — Central America/Caribbean — Cuban Gar
2. 2026-07-21 — Australia/Oceania — Numbat
3. 2026-07-22 — North America — Pinyon Jay
4. 2026-07-23 — Europe — Alpine Salamander
5. 2026-07-24 — South America — *Lysurus fossatii*
6. 2026-07-25 — Ocean/Global — Pelican Eel
7. 2026-07-26 — Asia — Himalayan Monal
8. 2026-07-27 — Africa — Gerenuk

Previous completed region: Africa.

## Verified Workspace Runtime

- Bundled Python:
  `C:\Users\ryusu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`
- Last verification: bundled runtime loaded on 2026-07-27. The completed
  Gerenuk Quality Run passed pre-image Copy Lock, separate direct-poster visual
  QA, phone-size QA, pixel equality, X/sidecar checks, and full package QA.

## Daily Quality Loop Counters

- `#image-text-error`: 2/3. The English Gerenuk poster converted a locked ASCII
  apostrophe to a curly glyph in both the first generation and targeted retry;
  one-glyph local text-safe repair resolved it.
- `#IUCN-unavailable`: historical 2/3. The Gerenuk occurrence was corrected
  with user-supplied official screenshot/PDF evidence; no access caveat remains
  in the package.
- `#post-structure-drift`: 0/2 after a user-directed deterministic correction.
  The Gerenuk main posts omitted standalone common/scientific name lines;
  template guidance and a validator check now prevent recurrence.
- `#workflow-friction` for the WindowsApps PowerShell launch failure: 0/3 after
  the approval-aware retry path succeeded on 2026-07-25; `counter_reset: yes`.
- `#species-identity-drift`: 1/3 after the first Japanese Pelican Eel poster
  hid the diagnostic tail tip; resolved by one targeted retry.
- `#layout-overcrowded`: 1/2 after the first Himalayan Monal composition hid
  the crest beneath the title panel; resolved by one targeted composition edit
  plus the opt-in lower-card layout.
- `#generic-production-drift`: reset after one architecture-level correction on
  2026-07-26. Fast Run made the poster and X copy mechanically consistent but
  visibly generic; the default was restored to complete direct Image Gen
  posters and narrative posting copy.

## Next Concrete Change

- On the next new-topic run, begin with the one-batch Quality Run preflight.
  The latest eight regions are evenly represented, so avoid repeating Africa
  when a credible alternative exists.
- Generate the complete Japanese poster first, visually accept it, then create
  the English companion from the same art direction. Do not use the deterministic
  composer as the default public asset.
- For locked ASCII punctuation in generated text, inspect glyph shape before
  accepting the companion and use a one-glyph text-safe repair after the single
  targeted retry instead of entering a regeneration loop.
- Keep each X main post in the established sequence: species-specific hook,
  standalone common name, standalone scientific name, discovery story, then
  quiet status footer.
