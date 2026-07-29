# Automation 2 Current State

Updated: 2026-07-29T13:33:45+09:00

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
  matching 12-page assessment PDF for `e.T61925A210445926`, supplemented by
  the ASM Mammal Diversity Database, the IUCN SSC Anteater, Sloth and Armadillo
  Specialist Group, METI's current CITES fauna appendix, Smithsonian biology
  review, and the *Mammalian Species* account.
- Confirmed: current accepted treatment *Bradypus pygmaeus*, Japanese name
  ピグミーミツユビナマケモノ, Global Critically Endangered (CR), criteria
  `B1ab(ii,iii)+2ab(ii,iii)`, assessed 22 April 2022 and published 2022, Isla
  Escudo de Veraguas mangrove and tropical-forest habitat, algae-green fur,
  and recorded arboreal, terrestrial, and swimming movement.
  The ASM database's possible *B. variegatus* synonym note remains an internal
  taxonomy caution.
- Phase 0 preflight: passed on 2026-07-29 in the no-approval local automation
  path.
- Pygmy Three-toed Sloth Quality Run: completed through Phase 5 on 2026-07-29.
  The direct IUCN and BirdLife page bodies were initially policy-blocked, so
  the rejected Cuban Tody candidate was dropped before lock. The final
  species' user-supplied official IUCN screenshot and matching PDF later
  replaced the fallback route and removed the public access caveat.
- Live Automation prompt sync: completed on 2026-07-26 with the Quality Run
  prompt and refreshed on 2026-07-28 with explicit first-prompt ASCII spacing
  invariants, the four-part posting sequence, minimal story-reply overflow
  trimming, and the English common-name hashtag rule. `ACTIVE`, the daily
  10:00 schedule, model, reasoning effort, execution environment, and project
  target remained unchanged.

## Latest Package

- Latest package: `2026-07-29-pygmy-three-toed-sloth`.
- State: `completed, local-ready`.
- Production: the initially accepted Japanese and English pair was rejected
  after the user found a fifth limb. The first targeted edit masked only the
  claw endpoint and did not remove the limb; later full-remake drafts had
  unnatural hindlimbs or a detached-looking forelimb. The user then authorized
  abandoning the failing composition.
- Visual QA: the user supplied a Gemini poster as the natural pose reference.
  The user then directed a full composition redesign because the repeated
  diagonal-branch layout kept inducing anatomy failures. The user accepted the
  completely new Japanese poster built around one horizontal branch and a
  suspended side-profile hero: two hindlimbs at the left/back, two forelimbs
  at the right/front, four separate grip points, and three unequal observation
  elements in the surrounding negative space. The English companion preserved
  that exact anatomy and composition. Both direct/posting pairs are exact
  1024x1536 and pixel-identical.
- Cleanup: at the user's request, ten rejected, superseded, or byte-duplicate
  PNGs were moved to the Windows Recycle Bin. Only the four canonical poster
  PNGs remain in `images/`; the Gemini pose reference and official IUCN
  evidence were preserved. X-format validation, full package QA, exact
  1024x1536 dimensions, direct/posting pixel identity, and whitespace checks
  passed after metadata synchronization.
- Posting QA: four-block posting sets follow the short-main, first-reply story,
  media ALT, and source/context sequence. Main-post lengths are Japanese 116
  and English 158; story-reply lengths are Japanese 141 and English 217. Both
  main posts include `#PygmyThreetoedSloth`, and the opening differs from the
  Kea and Gerenuk scenes.
- Evidence correction: the official IUCN screenshot and matching PDF directly
  confirm Global CR, criteria `B1ab(ii,iii)+2ab(ii,iii)`, assessment date
  22 April 2022, and publication year 2022. Both source replies now cite this
  direct route; the earlier access caveat is removed. The possible synonym
  note stays in README and sources QA rather than public poster copy.
- GitHub publishing: the user resumed the established direct-`master`
  closeout. The remote preflight now passes and the scoped package/INDEX
  commit is `bd42f94`; push and authoritative remote-ref verification are
  pending. State remains `completed, local-ready` until both succeed.

## Recent-Eight Region Rotation

1. 2026-07-22 — North America — Pinyon Jay
2. 2026-07-23 — Europe — Alpine Salamander
3. 2026-07-24 — South America — *Lysurus fossatii*
4. 2026-07-25 — Ocean/Global — Pelican Eel
5. 2026-07-26 — Asia — Himalayan Monal
6. 2026-07-27 — Africa — Gerenuk
7. 2026-07-28 — Australia/Oceania — Kea
8. 2026-07-29 — Central America/Caribbean — Pygmy Three-toed Sloth

Previous completed region: Central America/Caribbean.

## Verified Workspace Runtime

- Bundled Python:
  `C:\Users\ryusu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`
- Last verification: bundled runtime loaded on 2026-07-29. The completed Pygmy
  Three-toed Sloth Quality Run passed pre-image Copy Lock, separate
  direct-poster visual QA, phone-size QA, pixel equality, X/sidecar checks, and
  full package QA.

## Daily Quality Loop Counters

- `#image-text-error`: 0/3 after threshold improvement and counter reset. The
  first English Kea poster changed locked footer spacing; one targeted
  correction resolved it. The initial English prompt must now state exact ASCII
  punctuation spacing.
- `#IUCN-unavailable`: historical 2/3. The Gerenuk occurrence was corrected
  with user-supplied official screenshot/PDF evidence; no access caveat remains
  in the package.
- `#IUCN-browser-policy-block`: historical 1/3. Direct IUCN and BirdLife page
  bodies were policy-blocked on 2026-07-29 and the Cuban Tody candidate was
  rejected before lock. User-supplied official IUCN evidence then corrected
  the final package; no access caveat remains.
- `#post-structure-drift`: 0/2 after a user-directed deterministic correction.
  The Gerenuk main posts omitted standalone common/scientific name lines;
  template guidance and a validator check now prevent recurrence.
- `#workflow-friction` for the WindowsApps PowerShell launch failure: 0/3 after
  the approval-aware retry path succeeded on 2026-07-25; `counter_reset: yes`.
- `#species-identity-drift`: 0/3 after the threshold correction and counter
  reset. The Pelican Eel tail-tip miss was followed by a five-limb Pygmy
  Three-toed Sloth and a failed masked correction. The resolved architecture
  now requires abandoning a repeatedly failing composition, approving the
  Japanese hero anatomy before companion production, and tracing each limb
  from torso origin through joint path to endpoint.
- `#layout-overcrowded`: 1/2 after the first Himalayan Monal composition hid
  the crest beneath the title panel; resolved by one targeted composition edit
  plus the opt-in lower-card layout.
- `#generic-production-drift`: reset after one architecture-level correction on
  2026-07-26. Fast Run made the poster and X copy mechanically consistent but
  visibly generic; the default was restored to complete direct Image Gen
  posters and narrative posting copy.

## Next Concrete Change

- On the next new-topic run, begin with the one-batch Quality Run preflight.
  The latest eight now contain each broad region once; choose for lineage,
  habitat, and visual variety while avoiding another Central
  America/Caribbean topic immediately after this run.
- During evidence viability, treat an explicit Browser safety-policy block as
  a hard route boundary. Reject the candidate before lock or use a directly
  available official assessment DOI/PDF; use an explicit public caveat only
  while no direct official evidence is available, and remove it if stronger
  evidence later resolves the gap. Do not retry a blocked source through an
  alternate browser surface.
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
