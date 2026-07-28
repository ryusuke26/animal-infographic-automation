# Automation 2 Current State

Updated: 2026-07-28T13:44:53+09:00

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
  matching 13-page assessment PDF for `e.T22684831A119243358`, New Zealand
  Department of Conservation, New Zealand Birds Online, and Tamagawa University
  Educational Museum.
- Confirmed: accepted taxon *Nestor notabilis*, Japanese name ミヤマオウム,
  Global Endangered (EN), criteria A2be+4be, assessed 1 October 2017 and
  published 2017, South Island forest-to-alpine habitat, olive plumage with
  orange-red underwings, and exploratory manipulation with the bill and feet.
- Phase 0 preflight: passed on 2026-07-28 in the no-approval local automation
  path.
- Kea Quality Run: completed through Phase 5 on 2026-07-28. The user-supplied
  official screenshot/PDF now directly confirm Global EN, criteria A2be+4be,
  assessed 1 October 2017 and published 2017; obsolete access caveats were
  removed from source replies.
- Live Automation prompt sync: completed on 2026-07-26 with the Quality Run
  prompt and refreshed on 2026-07-28 with explicit first-prompt ASCII spacing
  invariants, the four-part posting sequence, minimal story-reply overflow
  trimming, and the English common-name hashtag rule. `ACTIVE`, the daily
  10:00 schedule, model, reasoning effort, execution environment, and project
  target remained unchanged.

## Latest Package

- Latest completed package: `2026-07-28-kea`.
- State: `completed, published`.
- Production: separate complete Japanese and English ImageGen posters.
  Japanese passed on its first generation. The first English generation changed
  the footer to `2017 : Endangered(EN)`; one targeted correction restored the
  locked `2017: Endangered (EN)` spacing while preserving the composition.
- Visual QA: one complete adult Kea, exactly three species-specific illustrated
  cards, correct South Island alpine habitat, visible orange-red underwing
  coverts, locked text, phone-size coherence, and exact 1024x1536
  direct/posting pixel-identical pairs passed.
- Posting correction: the initial snow-walk opening resembled the 2026-07-26
  Himalayan Monal post, so both languages were rewritten around a Kea moving a
  twig. The user later clarified that the Japanese narrative body is posted
  separately and only the highlighted overflow needed trimming. The fuller
  story was restored and minimally tightened in the former 226-character
  combined draft, while retaining habitat, underwing color,
  manipulation, and learning details. The user then confirmed the actual
  publishing order: attach both language posters to a short main post, publish
  the natural-history body as the first reply, apply ALT text to the media, and
  publish sources as a later reply. The four-block posting sets now match that
  sequence. Main-post lengths are Japanese 87 and English 88; story-reply
  lengths are Japanese 142 and English 185. Both main posts include `#Kea`.
- Evidence correction: the user-supplied official screenshot and matching PDF
  were preserved with hashes and synchronized through README, sources QA,
  INDEX, X source replies, and sidecars. Poster footers remain correct.
- GitHub closeout: completed on 2026-07-28 through the established system-Git
  direct-push route after confirming the earlier CLI approval installed or
  authenticated nothing. Package commit `da148a4` and workflow commit
  `1cdebcd` were pushed to `origin/master`; the remote ref was verified at
  `1cdebcd38b1b377dddc0e6bab3e61ba80c8f719d` before this published-state
  metadata commit.

## Recent-Eight Region Rotation

1. 2026-07-21 — Australia/Oceania — Numbat
2. 2026-07-22 — North America — Pinyon Jay
3. 2026-07-23 — Europe — Alpine Salamander
4. 2026-07-24 — South America — *Lysurus fossatii*
5. 2026-07-25 — Ocean/Global — Pelican Eel
6. 2026-07-26 — Asia — Himalayan Monal
7. 2026-07-27 — Africa — Gerenuk
8. 2026-07-28 — Australia/Oceania — Kea

Previous completed region: Australia/Oceania.

## Verified Workspace Runtime

- Bundled Python:
  `C:\Users\ryusu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`
- Last verification: bundled runtime loaded on 2026-07-28. The completed Kea
  Quality Run passed pre-image Copy Lock, separate direct-poster visual QA,
  phone-size QA, pixel equality, X/sidecar checks, and full package QA.

## Daily Quality Loop Counters

- `#image-text-error`: 0/3 after threshold improvement and counter reset. The
  first English Kea poster changed locked footer spacing; one targeted
  correction resolved it. The initial English prompt must now state exact ASCII
  punctuation spacing.
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
  Australia/Oceania appears twice in the latest eight and was the latest
  region; prefer Central America/Caribbean or another underrepresented region
  when a credible alternative exists.
- Generate the complete Japanese poster first, visually accept it, then create
  the English companion from the same art direction. Do not use the deterministic
  composer as the default public asset.
- For locked ASCII punctuation, state exact spaces around colons, parentheses,
  apostrophes, and similar marks in the first English Image Gen prompt; then
  inspect the glyphs before accepting the companion.
- Keep each X main post in the established sequence: species-specific hook,
  standalone common name, standalone scientific name, quiet status footer,
  then hashtags. Attach both accepted language posters to this short post.
- Put the connected natural-history story in the first reply. Count it
  independently from the main post, ALT, and source reply; if only a small
  overflow is highlighted, shorten only enough low-value wording to clear it
  and do not broadly compress the story.
- Include the English common-name hashtag in both language versions, removing
  spaces and punctuation: `#Kea`, `#HimalayanMonal`, and so on.
