# Daily Quality Loop

Use this memo to improve the recurring infographic workflow without turning
each run into a growing checklist. The goal is small, repeated learning:
record the most important drift, carry one useful change into the next run,
and only update skills or policy when a failure pattern repeats.

## Daily Entry

At the end of each package run, write one to three entries in automation
memory. Prefer one entry. If nothing meaningful drifted, write one short
`issue: none` entry so future runs know the loop was checked.

```text
Daily Quality Loop
- issue:
  priority:
  tags:
  cause:
  next_action:
  tomorrow_change:
```

Keep entries concrete. Do not write broad lessons, wish lists, or speculative
future systems. The `tomorrow_change` should be one thing the next run can
actually do.

## Priority Order

When several problems happen in one run, record them in this order:

1. `fact-risk` - possible factual error, status error, source misuse, or
   jurisdiction mix-up.
2. `publish-blocker` - a problem that stopped or nearly stopped completion.
3. `quality-drift` - repeated or noticeable decline in Japanese copy, visual
   identity, layout, tone, or audience fit.
4. `ops-friction` - process friction, wasted time, tool failure, or confusing
   handoff that did not threaten publication.

If only one issue can be recorded, choose the highest priority issue.

## Initial Tags

Use these tags first. Add a new tag only when an issue does not fit and the
same kind of issue is likely to matter again.

```text
#IUCN-unavailable
#source-conflict
#old-status-risk
#literal-ja
#tone-drift
#noun-stack
#post-story-compression
#species-identity-drift
#image-text-error
#layout-overcrowded
#source-canvas-drift
#topic-classification-drift
#workflow-friction
```

## Next Actions

- `ignore` - one-off issue, already fixed, unlikely to repeat.
- `watch` - no change today, but use the tag so a future repeat is visible.
- `skill-candidate` - do not edit a skill yet, but count this toward a future
  skill or policy change.
- `fix-now` - fix the current package or policy before completing the run.

`watch` is only a light flag. It does not create a task by itself.

## Escalation Rules

- `fact-risk`: one occurrence triggers `fix-now` when public facts, status,
  jurisdiction, or evidence selection may be wrong.
- `publish-blocker`: two unresolved occurrences with the same tag trigger a
  policy, prompt, template, validator, or execution-path improvement.
- `quality-drift`: three unresolved occurrences with the same tag trigger a
  skill, prompt, template, or validator improvement.
- `ops-friction`: three unresolved occurrences with the same tag, or one large
  time sink, trigger a small workflow or execution-path improvement.

Do not update a skill or policy for every single logged issue. Single issues
usually stay in memory. Repeated tags become candidates.

## Automatic Counting And Improvement

This loop is active work, not a passive diary.

At Phase 0 of every run:

1. Scan `C:\Users\ryusu\.codex\automations\automation-2\memory.md` for Daily
   Quality Loop entries.
2. Count each tag from its most recent `counter_reset` or
   `improvement_applied` record. Older resolved occurrences do not count.
3. Record any tag that is one occurrence below or already at its threshold.
4. Carry the highest-priority unresolved threshold into the current run.

At Phase 5, after recording the current issue:

1. Recount the affected tag.
2. If the threshold is reached, automatically apply the smallest safe,
   deterministic improvement that addresses the repeated cause. Prefer, in
   order: prompt/policy clarification, template change, validator check, then
   a skill change.
3. Do not auto-apply subjective taste changes, new factual claims, external
   side effects, or broad redesigns. Record these as `needs decision` instead.
4. Validate the changed files and synchronize the live Automation prompt when
   execution instructions changed.
5. Write this resolution block to automation memory:

```text
Improvement Resolution
- tag:
- count_since_last_fix:
- threshold:
- improvement_applied:
- files_changed:
- validation:
- counter_reset: yes
```

After `counter_reset: yes`, later occurrences begin again at 1. Counts are by
the same tag and materially similar cause; do not combine unrelated failures
just because they share a broad operational label. When a tag is too broad,
split it into a more precise reusable tag before counting.

## Source Access And IUCN

Do not convert "IUCN could not be opened" into a confident status claim, and
do not convert failed access into a completed "no assessment confirmed"
footer.
When the live IUCN page is unavailable:

1. Retry during Evidence Lock when it is cheap.
2. Check official PDFs, official status-change tables, or a previously saved
   official screenshot/snapshot.
3. If an official snapshot is used, state the snapshot date or access caveat.
4. If an official route or completed official search supports no global
   assessment, use short label-free evidence-availability wording such as
   `IUCN世界評価は確認できず（2026年確認）` or
   `No global IUCN assessment confirmed (checked 2026)`.
5. If only secondary sources are available, remove the IUCN category from
   public copy and mark the status route unresolved; do not mark the package
   `completed` from that evidence alone.
6. If the IUCN category is central to the story and no official basis can be
   confirmed, mark the package `needs review`.

## Sub-Agent Use

Do not spawn sub-agents as a routine way to make the workflow feel safer. Use
them only when they are likely to catch a high-impact issue:

- IUCN or another authoritative source is unavailable.
- Authoritative sources conflict.
- A status, population, legal protection, or threat claim is prominent.
- The species has high lookalike or anatomy risk.
- The same quality tag appeared in a recent run.
- The current package is close to `needs review` or publication blocking.

Routine copy polish, normal final QA, and low-risk layout checks should stay
local unless one of the triggers above is present.

## Periodic Review

After five to ten completed packages, skim the recent Daily Quality Loop
entries and the final Japanese publish rewrites for about 15 minutes. Pick at
most one skill, prompt, template, or policy improvement from that review.

Do not add date-window counting, dashboards, or extra tracking unless the
simple tag loop stops working in practice.

## 2026-07-28 — Kea English footer spacing

Daily Quality Loop
- issue: the first English poster changed the locked footer from
  `2017: Endangered (EN)` to `2017 : Endangered(EN)`.
  priority: quality-drift
  tags: #image-text-error
  cause: the prompt required verbatim text but did not spell out the exact
  ASCII spacing around the colon and parentheses.
  next_action: resolved by one targeted English correction
  tomorrow_change: state ASCII punctuation spacing explicitly in the first
  English Image Gen prompt

Improvement Resolution
- tag: #image-text-error
- count_since_last_fix: 3
- threshold: 3
- improvement_applied: explicit first-prompt spacing invariants for English
  ASCII punctuation
- files_changed: automation-2-production-policy.md,
  automation-2-updated-prompt.md, automation-2-current-state.md
- validation: Kea visual/text QA, X validation, full package QA, prompt sync,
  and whitespace checks passed
- counter_reset: yes

## 2026-07-28 — Four-part posting sequence and English-name hashtag

Daily Quality Loop
- issue: the posting set flattened the short image-attached main post and the
  fuller first-reply story into one block, so an overflow correction compressed
  the wrong surface.
  priority: quality-drift
  tags: #post-scope-drift
  cause: the workflow modeled main post, ALT, and source reply but did not
  represent the story reply as its own posting target.
  next_action: resolved by restoring the fuller Kea body and recording
  a four-block posting set: main post, story reply, ALT, and source reply
  tomorrow_change: attach both language posters to the short main post, put the
  fuller story in the first reply, trim only the block that actually overflows,
  and add the English common-name hashtag to both main posts

Improvement Resolution
- tag: #post-scope-drift
- count_since_last_fix: user-directed standardization
- threshold: explicit user preference; no automatic threshold wait
- improvement_applied: canonical four-block posting sequence, eight synchronized
  sidecars, minimal story-reply overflow trimming, and mandatory English-name
  hashtag such as `#Kea`
- files_changed: templates/x-post-copy-template.md,
  automation-2-production-policy.md, automation-2-updated-prompt.md,
  scripts/validate_x_post_format.py, automation-2-current-state.md, and Kea
  posting files
- validation: current bilingual four-block X format, misplaced-story rejection,
  hashtag rejection, eight-sidecar package QA, live-prompt equality, and
  whitespace checks passed
- counter_reset: yes

## 2026-08-01 — Direct-source canvas gate

Daily Quality Loop
- issue: the Russian Desman Japanese canonical direct/posting pair had exact
  `1024x1536` outer dimensions but retained a 91px blank right-edge band; an
  earlier wrong-ratio generation had been allowed into the correction path.
  priority: publish-blocker
  tags: #source-canvas-drift
  cause: aspect and canvas integrity were checked after visual correction and
  acceptance, while the mechanical validator checked dimensions but not blank
  rendered canvas.
  next_action: reopen the package as `incomplete, needs review`; regenerate the
  Japanese poster on a fresh 2:3 canvas and do not use either rejected image as
  an edit target
  tomorrow_change: run the direct-source gate immediately after every
  generation or retry and before viewing, editing, referencing, companion
  generation, or normalization

Improvement Resolution
- tag: #source-canvas-drift
- count_since_last_fix: 2 materially related source-canvas failures, including
  the rejected Ringtail wrong-ratio companion and the Russian Desman blank-band
  correction
- threshold: 2 publish-blockers
- improvement_applied: exact 2:3 and blank-edge source gate, edit-target
  eligibility rules, fresh-canvas retry routing, and final package enforcement
- files_changed: `scripts/validate_direct_poster.py`,
  `scripts/normalize_poster.py`, `scripts/validate_package.py`,
  `automation-2-production-policy.md`, `automation-2-updated-prompt.md`,
  `AUTOMATION-2-FILE-MAP.md`, `automation-2-current-state.md`, package README,
  INDEX, Daily Quality Loop, live Automation, and Automation memory
- validation: gate regressions, normalization rejection, package failure on the
  current blank-band artifact, prompt synchronization, protected Automation
  fields, Python syntax, and whitespace checks passed
- counter_reset: yes

## 2026-08-02 — Pacarana clean Quality Run

Daily Quality Loop
- issue: none; both language posters passed direct-source, anatomy, text,
  composition, phone-size, sidecar, X, and package QA on their first generation
- priority: none
- tags: #quality-run-clean
- cause: scientific-name-first duplicate screening, a stable seated pose with
  separate limb paths, and first-prompt ASCII spacing kept the run aligned
- next_action: package closed as `completed, local-ready`
- tomorrow_change: keep the current gates and prioritize an Ocean/Global or
  otherwise underrepresented region without repeating South America

## 2026-08-02 — Pacarana assessment-year correction

Daily Quality Loop
- issue: the official species page and assessment PDF showed a 1 March 2016
  assessment date while the poster footer used the 2017 publication/release year
- priority: fact-risk
- tags: #assessment-year-drift
- cause: the initial official status-change table exposed release timing but not
  the field-level assessment date, and its year was used before stronger official
  evidence arrived
- next_action: corrected all bilingual Copy Lock, poster, posting, source, and
  state artifacts to assessment year 2016; retained publication year 2017 in
  source context and preserved the supplied official evidence with hashes
- tomorrow_change: treat a status-change-table year as publication/release only;
  reopen Copy Lock whenever field-level official assessment evidence arrives

## 2026-08-02 — Pacarana superseded-image cleanup

Daily Quality Loop
- issue: four obsolete 2017-footer PNGs remained after the accepted 2016-footer
  correction
- priority: cleanup
- tags: #rejected-image-cleanup
- cause: superseded images were retained as a temporary evidence trail during
  correction QA
- next_action: moved exactly those four PNGs to the Windows Recycle Bin, kept
  the four canonical images and official evidence, synchronized documentation,
  and reran canonical package QA
- tomorrow_change: after a user accepts the corrected pair, offer reversible
  cleanup of superseded images once canonical and evidence assets are protected

## 2026-08-03 — Antarctic Fur Seal extra-card-text correction

Daily Quality Loop
- issue: the first Japanese poster added unrequested explanatory paragraphs to
  all three observation cards despite an exact six-line Copy Lock
- priority: publish-blocker
- tags: #image-text-error
- cause: the generation followed the illustrated-card concept but elaborated
  the card copy beyond the locked labels
- next_action: used the one allowed targeted text-only retry; removed every
  extra paragraph while preserving the accepted full canvas, anatomy, habitat,
  card art, and six locked lines
- tomorrow_change: keep every first prompt explicit that each card contains only
  its number, one locked label, and one spot illustration, with no explanatory
  paragraph or replacement text

## 2026-08-03 — Antarctic Fur Seal hind-flipper and card-layout remake

Daily Quality Loop
- issue: the previously canonical bilingual pair showed the far hind flipper in
  both the hero and card 3 as if it began independently from the middle abdomen;
  narrow accidental gaps between card borders also fragmented the composition
- priority: publish-blocker
- tags: #species-identity-drift
- cause: the original diagonal walking pose obscured the rear pelvis/tail-base
  relationship, while card borders were placed close enough to create slits
  instead of deliberate background channels
- next_action: rejected and preserved all four prior canonical/posting PNGs,
  generated both replacements from text-only fresh 2:3 canvases, exposed the
  paired hind-flipper origins in a stable rear three-quarter stance, and spaced
  three body-aligned cards across one continuous shoreline ground
- tomorrow_change: for rear-limb-sensitive body plans, inspect every hero and
  complete-animal card from pelvis/tail base to both hind-flipper endpoints, and
  reject any card spacing that reads as a hairline gap or narrow wedge

## 2026-08-03 — Antarctic Fur Seal rejected-image cleanup

Daily Quality Loop
- issue: five rejected PNGs remained after the replacement bilingual pair was
  accepted and fully validated
- priority: cleanup
- tags: #rejected-image-cleanup
- cause: failed generations were retained temporarily as an audit trail during
  anatomy and composition review
- next_action: moved exactly five explicitly named rejected PNGs to the Windows
  Recycle Bin, preserved the four canonical poster PNGs, removed stale README
  links, and reran canonical package QA
- tomorrow_change: after user acceptance and canonical validation, offer a
  recoverable cleanup of failed images while preserving evidence and posting
  assets

## 2026-08-04 — Greater Hog Badger localized text corrections

Daily Quality Loop
- issue: the first Japanese poster substituted one title glyph, and the first
  English companion inserted a space before the footer colon
  priority: publish-blocker
  tags: #verbatim-glyph-drift
  cause: dense generated typography drifted at two localized glyph boundaries
  even though the locked six-line copy and English spacing were explicit
  next_action: used each language's one allowed targeted text-only retry while
  preserving the accepted full canvas, anatomy, habitat, card art, and layout
  tomorrow_change: spell unfamiliar Japanese titles character by character in
  the first prompt while retaining the existing English punctuation invariants

## 2026-08-04 — Greater Hog Badger official-evidence synchronization

Daily Quality Loop
- issue: the package retained an unavailable-record caveat and superseded IUCN
  record ID after the official amended assessment became directly available
  priority: publish-blocker
  tags: #official-evidence-sync #assessment-year-drift
  cause: the initial Evidence Lock used the 2016-1 status-change table while
  the field-level assessment record could not be rendered
  next_action: preserved the official PDF and screenshot; synchronized the 2015
  assessment date, 2016 original publication, 2024 amendment context, current
  record ID, source replies, sidecars, README, INDEX, and current state
  tomorrow_change: before closing Evidence Lock, retry the direct record route
  once and distinguish assessment date from original and amended publication

## 2026-08-05 — Maned Rat user-selected visual and Copy Lock synchronization

Daily Quality Loop
- issue: the first Japanese poster had the strongest species-specific authored
  composition, while later attempts improved mechanical details but weakened
  the preferred overall visual; its footer punctuation differed semantically
  trivially from the original Copy Lock
  priority: subjective visual choice
  tags: #user-visual-choice #verbatim-glyph-drift
  cause: the correction loop optimized isolated anatomy and punctuation signals
  after the initial poster had already achieved the user's preferred narrative
  composition
  next_action: accepted the exact user-supplied first PNG, re-locked the
  Japanese footer to its visible punctuation, synchronized main post and ALT,
  then generated the English companion from that accepted visual reference
  tomorrow_change: when the user explicitly selects a stronger source-gate-
  passing variant, treat equivalent punctuation as a Copy Lock decision and
  synchronize all public surfaces once before companion generation

## 2026-08-05 — Maned Rat official-evidence spelling correction

Daily Quality Loop
- issue: the official IUCN assessment was initially missed because its species
  record is registered under *Lophiomys imhausi*, while the current MDD accepted
  name is *Lophiomys imhausii*
- priority: publish-blocker
- tags: #topic-alias-duplication #official-evidence-sync
- cause: the direct evidence route did not complete the taxonomy-source
  incorrect-subsequent-spelling search before the unavailable conclusion
- next_action: visually checked and preserved the official species-page
  screenshot and seven-page PDF; restored Global LC assessed 31 January 2016
  across Copy Lock, prompts, X sets, sidecars, README, INDEX, and current state;
  retained the already-correct canonical posters without regeneration
- tomorrow_change: search IUCN under the accepted name plus every taxonomy-
  source synonym and incorrect subsequent spelling before using the official
  no-assessment route

Improvement Resolution
- tag: #topic-alias-duplication
- count_since_last_fix: 2
- threshold: 2
- improvement_applied: added an accepted-name, historical-spelling, and English-
  alias IUCN search gate before any official-unavailable conclusion
- files_changed: automation-2-production-policy.md,
  automation-2-current-state.md, daily-quality-loop.md
- validation: the supplied official page and PDF resolve under *Lophiomys
  imhausi* / `Crested Rat` and confirm record e.T12308A22368581
- counter_reset: yes

## 2026-08-05 — Maned Rat rejected-image cleanup and English-alias correction

Daily Quality Loop
- issue: three rejected Japanese PNGs remained after acceptance, and the IUCN
  lookup was also delayed because its English name `Crested Rat` differs from
  the public package name `Maned Rat`
- priority: cleanup
- tags: #rejected-image-cleanup #topic-alias-duplication
- cause: failed generation artifacts were retained for audit, while the first
  alias-search improvement covered scientific spellings but not English common-
  name variants
- next_action: moved exactly three explicitly rejected PNGs to the Windows
  Recycle Bin, preserved the four canonical poster PNGs and official evidence,
  removed stale artifact references, and expanded the IUCN search gate to
  English common-name aliases
- tomorrow_change: complete scientific-name, historical-spelling, and English-
  alias searches before declaring an official IUCN route unavailable; after
  user acceptance, offer recoverable cleanup of rejected visual artifacts

## 2026-08-06 — Southern Marsupial Mole Rescue Run

Daily Quality Loop
- issue: both source-gate-passing Japanese generations showed only two
  traceable limbs on the dominant hero; the first also duplicated observation
  label 1 outside its card
- priority: publish-blocker
- tags: #species-identity-drift #duplicate-copy-placement
- cause: the underground side-on silhouette repeatedly hid the far-side limbs,
  while the first composition treated the habitat claim as both a subtitle and
  card copy despite the six-line lock
- next_action: preserved exactly two rejected Japanese PNGs under explicit
  filenames, stopped before English generation, and marked the active package
  `needs review` under Rescue Run
- tomorrow_change: resume the same package; do not use rejected pixels as an
  edit target or reference, and require a user decision before any fresh-canvas
  attempt beyond the retry limit

## 2026-08-06 — Southern Marsupial Mole official-date and diagnostic-anatomy correction

Daily Quality Loop
- issue: the package used the 2016 publication/citation year as the public
  assessment year, and visual QA focused on simultaneous limb visibility while
  missing a plug-like face, incorrect forefoot digits, and undersized claws
- priority: fact-risk
- tags: #assessment-year-drift #diagnostic-anatomy-priority
- cause: the first evidence route exposed the category and release year but not
  the field-level assessment date; the visual checklist treated generic limb
  inventory as more important than this species' nasal shield and two-claw
  split-spade forefeet
- next_action: preserved the user-supplied official PDF and screenshot; changed
  every package footer to assessed year 2014; re-locked observation 2 to the two
  huge foreclaws; rewrote visual guidance around nasal shield, digits III/IV,
  and three subordinate digits; recycled exactly two failed PNGs
- tomorrow_change: require direct `Date Assessed` evidence before any dated
  footer and rank diagnostic facial/paw architecture above generic visible-limb
  counting for difficult fossorial species

Improvement Resolution
- tag: #assessment-year-drift
- count_since_last_fix: 2
- threshold: 2
- improvement_applied: publication/citation years can no longer substitute for
  an unavailable field-level assessment year; Evidence Lock remains unresolved
  and `needs review` until `Date Assessed` is confirmed
- files_changed: automation-2-production-policy.md,
  automation-2-current-state.md, daily-quality-loop.md
- validation: corrected Southern Marsupial Mole Copy Lock passes pre-image QA;
  bilingual X-format validation and `git diff --check` pass
- counter_reset: yes

## 2026-08-06 — Southern Marsupial Mole visual retirement

Daily Quality Loop
- issue: fresh Japanese generation, a localized face correction, and the
  English companion still converted the species' diagnostic nasal shield and
  digit III/IV digging claws into generic mole, pig-nose, or tusk-like forms
- priority: publish-blocker
- tags: #species-identity-drift #diagnostic-anatomy-priority
- cause: the topic depends on a rare combination of facial and forefoot anatomy
  that prose-only Image Gen prompting did not preserve reliably; earlier QA
  also over-weighted how many limbs were visible instead of whether the face,
  digit hierarchy, and claw origins identified the species
- next_action: retired the package as `incomplete`, recycled exactly four failed
  Japanese workspace PNGs, kept zero package PNGs, and did not import the failed
  English output
- tomorrow_change: screen visually high-risk candidates for a usable
  authoritative reference before topic lock; reject prose-only topics whose
  identity depends on rare face-plus-digit architecture

Improvement Resolution
- tag: #species-identity-drift
- count_since_last_fix: 3
- threshold: 3
- improvement_applied: added a pre-lock visual-viability gate requiring a
  usable reference or reliably represented body plan for rare diagnostic anatomy
- files_changed: automation-2-production-policy.md,
  automation-2-current-state.md, daily-quality-loop.md
- validation: package image count is zero, rejected workspace links are removed,
  the retired package is not active, and `git diff --check` passes
- counter_reset: yes

## 2026-08-06 — Southern Marsupial Mole user-reference revisit

Daily Quality Loop
- issue: one user-authorized fresh generation used the supplied anatomy-and-
  pose sketch and improved the body axis, forefoot placement, and dominant-claw
  scale, but still rendered a round pig-like nasal disc and left the three
  subordinate digits on each hero forefoot unresolved
- priority: publish-blocker
- tags: #species-identity-drift #diagnostic-anatomy-priority
- cause: the rough reference successfully constrained pose but did not provide
  a literal close-up nasal-shield silhouette or fully labeled digit topology;
  the generator's generic two-nostril mole/pig prior remained stronger
- next_action: rejected the Japanese result, stopped before English generation,
  kept package image count at zero, and stopped after the exact cache file could
  not be sent to the Recycle Bin because of sandbox permissions
- tomorrow_change: for rare face-plus-digit anatomy, distinguish a useful pose
  map from a sufficient identity reference; require a literal nasal-shield
  close-up and labeled five-digit forefoot view before another manual revisit

## 2026-08-06 — Southern Marsupial Mole photo-informed sketch revisit

Daily Quality Loop
- issue: five anatomy photographs corrected the prior undersized-shield model,
  but the sketch-style generation converted one broad nasal pad into three
  stacked armour-like lobes and again omitted clear subordinate forefoot digits
- priority: publish-blocker
- tags: #species-identity-drift #diagnostic-anatomy-priority
- cause: synthesizing several front and side views made the generator treat
  shallow surface divisions as repeated anatomical segments
- next_action: rejected the Japanese preview, stopped before English generation,
  kept package image count at zero, and changed Visual Lock to exactly one
  continuous pad with at most one shallow crease and no stacked lobes
- tomorrow_change: do not blend multiple ambiguous reference views directly for
  rare anatomy; require one user-approved simplified composite that fixes the
  shield continuity and five-digit topology before any further manual retry

Improvement Resolution
- tag: #diagnostic-anatomy-priority
- count_since_last_fix: 3
- threshold: 3
- improvement_applied: exact one-pad continuity and anti-segmentation constraints
  were added to the package Visual Lock and Japanese prompt
- files_changed: sources-qa.md, image-prompt-ja.md, README.md,
  automation-2-current-state.md, daily-quality-loop.md
- validation: corrected Copy Lock passes pre-image QA; package image count remains zero
- counter_reset: yes

## 2026-08-07 — Southern Marsupial Mole user-selected recovery

Daily Quality Loop
- issue: a source-gate-passing, coherent Japanese poster remained retired after
  anatomy-focused review, but the user later compared the localized variants
  and explicitly selected that earlier poster as the final visual
- priority: completion-recovery
- tags: #user-selected-poster #selected-poster-preservation
- cause: the prior review treated stylized nasal-pad surface relief as a hard
  blocker after the user had already shifted priority toward the overall face,
  claw scale, and authored poster coherence
- next_action: imported the exact user-selected Japanese source, generated the
  English companion from it as a reference on the first attempt, normalized
  both languages, synchronized eight sidecars, and completed full QA
- tomorrow_change: when a user explicitly selects a source-gate-passing poster
  after informed comparison, preserve it as canonical and do not regenerate it
  merely to optimize one isolated visual detail

## 2026-08-07 — Southern Marsupial Mole cache cleanup audit

Daily Quality Loop
- issue: the package was already clean, but nine rejected or superseded PNGs
  remained in the thread-level Image Gen cache after the user reconfirmed the
  final Japanese and English pair
- priority: housekeeping
- tags: #artifact-cleanup
- cause: Image Gen cache storage is outside the writable workspace boundary;
  the Windows Recycle Bin call was denied as an unauthorized operation
- next_action: stopped after the first exact-target failure, preserved the two
  accepted cache images and all four canonical package PNGs, and recorded the
  nine pending cache targets
- tomorrow_change: perform cache cleanup only in an approval-enabled context;
  never replace a denied Recycle Bin operation with a stronger deletion method

## 2026-08-07 — Southern Marsupial Mole cache cleanup completed

Daily Quality Loop
- issue: nine rejected or superseded PNGs remained in the thread Image Gen
  cache after the accepted bilingual pair was finalized
- priority: housekeeping
- tags: #artifact-cleanup #selected-poster-preservation
- cause: the first exact Recycle Bin attempt ran without permission to mutate
  the cache directory and correctly stopped
- next_action: revalidated all 11 cache PNGs by SHA-256, protected the two
  hashes matching the accepted direct posters, and moved exactly nine other
  regular PNGs to the Windows Recycle Bin with approval
- tomorrow_change: preserve accepted cache hashes explicitly before any
  approval-enabled cleanup and verify that only accepted cache images remain

## 2026-08-07 — Jade Vine Quality Run completed

Daily Quality Loop
- issue: the latest-eight completed classification rotation had become
  Mammals 8/8, leaving every other editorial group absent
- priority: editorial-diversity
- tags: #topic-classification-drift #rotation
- cause: recent evidence-ready selections repeatedly favored mammals
- next_action: screened a non-mammal slate, selected an evidence-ready Plant,
  and completed the bilingual package with first-pass direct posters
- tomorrow_change: continue preferring an absent non-mammal group other than
  Plants when evidence, naming, and visual identity gates remain strong

## 2026-08-08 — Sea Angel Quality Run completed

Daily Quality Loop
- issue: the first Japanese feeding card rendered the sea angel's short mouth
  cones as three long tube-like structures even though the calm hero, Copy
  Lock, and overall under-ice composition were already strong
- priority: localized-visual-accuracy
- tags: #diagnostic-anatomy-priority #selected-poster-preservation
- cause: a small side-view feeding inset compressed the far-side cone cluster
  and exaggerated the visible near-side structures into tubes
- next_action: used the one allowed localized edit to shorten the visible
  structures into a near-side cluster of conical mouth parts, preserved the
  accepted hero and full canvas, then completed the English companion on its
  first generation
- tomorrow_change: for small paired or clustered feeding anatomy, prompt the
  intended viewing angle and visible-versus-occluded structures explicitly in
  the first generation instead of relying on a total-count instruction alone

## 2026-08-08 — Sea Angel card-3 Rescue Run completed

Daily Quality Loop
- issue: user review showed that the accepted feeding card kept the head closed
  and projected three beak-like structures from the face instead of opening the
  anterior oral folds and showing six internally originating buccal cones
- priority: material-anatomy-correction
- tags: #diagnostic-anatomy-priority #visual-acceptance-withdrawal
- cause: the earlier review checked cone length and apparent clustering but did
  not verify the opening action, anatomical origin, bilateral pair count, and
  completeness of the mechanism animal as one combined acceptance gate
- next_action: rebuilt Japanese from a fresh text-only 2:3 canvas, rebuilt the
  English companion from the corrected accepted Japanese art direction, and
  used only one eligible localized fit correction per language
- tomorrow_change: for internal feeding structures, require the prompt and
  visual checklist to verify opening tissue, inside-to-outside origin, exact
  bilateral count, and a complete mechanism animal before accepting the card

## 2026-08-08 — Sea Angel head-apex research and Rescue Run pause

Daily Quality Loop
- issue: the revised feeding card still opened a large circular cavity across
  the face instead of placing the mouth at the top/front head apex; after web
  research corrected the anatomy, the bounded fresh retry visibly cramped the
  card explanations and broke their integration with the illustrations
- priority: incomplete-publish-blocker
- tags: #diagnostic-anatomy-priority #duplicate-copy-placement
  #visual-acceptance-withdrawal
- cause: the earlier anatomy gate checked opening, origin, and cone count but
  not the exact external aperture position; the retry then optimized anatomy
  without preserving comfortable card-copy margins as an equally hard gate
- next_action: withdrew completion, kept both fresh candidates unpromoted,
  paused before English production, moved the package out of the completed
  rotation, and added separate hidden-anatomy and card-typography gates to the
  production policy
- tomorrow_change: settle aperture position, opening direction, internal
  origin, bilateral count, intact surrounding body, and card-copy margins
  together before accepting any full poster

Improvement Resolution
- tag: #diagnostic-anatomy-priority
- count_since_last_fix: 3
- threshold: 3
- improvement_applied: added a five-property hidden-anatomy evidence gate and
  independent card-typography acceptance check
- files_changed: automation-2-production-policy.md, Sea Angel evidence and
  prompts, README, INDEX, current state, Daily Quality Loop, and Automation
  memory
- validation: both rejected fresh sources passed exact-2:3 mechanical gates;
  editorial rejection and incomplete state were recorded; pre-image Copy Lock
  QA and whitespace checks passed
- counter_reset: yes

## 2026-08-08 — Sea Angel user-reference Rescue Run completed

Daily Quality Loop
- issue: text-only anatomy instructions repeatedly produced lateral cones, a
  circular face cavity, cropped mechanism anatomy, or cramped card copy
- priority: user-reference-resolution
- tags: #diagnostic-anatomy-priority #selected-poster-preservation
- cause: the hidden feeding mechanism needed both a simple topology reference
  and real-animal references for cone thickness, curvature, compact origin, and
  organic asymmetry
- next_action: used the user's diagnostic sketch and two feeding photographs as
  references only, generated a fresh Japanese poster with one complete card-3
  animal and six thick countable cones, promoted it after explicit user
  approval, then generated the English companion from the accepted composition
- tomorrow_change: when a hidden mechanism remains wrong after the bounded
  retry, preserve rejected sources and use a deliberate user-supplied topology
  plus real-anatomy reference set before any fresh continuation

## 2026-08-09 — Madagascan Big-headed Turtle Quality Run completed

Daily Quality Loop
- issue: the first selection slate included Lord Howe Island Stick Insect even
  though that species already had a completed package
- priority: duplicate-topic-prevention
- tags: #duplicate-topic-gate #selection
- cause: the candidate entered the evidence slate before its accepted
  scientific name was checked against both INDEX and package folders
- next_action: rejected the duplicate before topic lock, screened an assessed
  Reptiles replacement, and completed the turtle package with first-pass
  Japanese and English direct posters
- tomorrow_change: run exact accepted-name and package collision checks as soon
  as each candidate enters the slate, before deeper source review

## 2026-08-10 — Blue-billed Curassow Quality Run completed

Daily Quality Loop
- issue: none
- priority: none
- tags: none
- cause: candidate collision checks, Evidence Lock, Copy Lock, and the initial visual-identity prompt all worked as intended
- next_action: completed the bilingual package with first-pass Japanese and English direct posters and all final validators passing
- tomorrow_change: keep the exact-name collision check and first-prompt localized-cere constraint; continue preferring absent groups when the editorial mission and hard gates remain strong

## 2026-08-11 — Itasenpara Bitterling Quality Run completed

Daily Quality Loop
- issue: the official IUCN species-page body could not be directly rendered even though the current category and field-level assessment date were available through an IUCN-linked FishBase record and the official IUCN assessment-change table
- priority: evidence-route-caution
- tags: #IUCN-unavailable #assessment-year-drift
- cause: the official species page was blocked at the browser permission boundary; no alternate browser or bypass route was used
- next_action: recorded the access boundary, cross-checked Global EN and 7 December 2017, kept the Japanese national category separate, and completed first-pass bilingual posters with all final QA passing
- tomorrow_change: prefer a directly inspectable official assessment page or PDF during candidate screening when an equally unfamiliar, well-named, visually viable topic is available; keep linked cross-check wording explicit when the species page body is unavailable

## 2026-08-11 — Itasenpara official IUCN evidence synchronized

Daily Quality Loop
- issue: the completed package still carried an official-page-unavailable caveat after the user supplied the matching official species-page capture and 10-page assessment PDF
- priority: evidence-route-caution resolved
- tags: #official-evidence-sync #assessment-year-drift
- cause: the direct official assessment record became inspectable only after the initial local-ready closeout
- next_action: verified Global EN B2ab(ii,iii,v), assessment date 7 December 2017, publication year 2019, and record `e.T213A116034178`; preserved both official artifacts and synchronized README, Sources QA, INDEX, current state, bilingual source replies, and source sidecars without regenerating the already-correct posters
- tomorrow_change: when stronger official evidence arrives after closeout, reopen Evidence Lock once, distinguish assessment date from publication year, and synchronize every public source surface before rerunning package QA

## 2026-08-12 — Table Mountain Ghost Frog Quality Run completed

Daily Quality Loop
- issue: the first Japanese source and its English companion both hid the left hind foot behind the frog's broad dorsal silhouette even though all four limb origins and paths had been requested
- priority: species-identity correction
- tags: #species-identity-drift #limb-topology
- cause: the general limb-separation rule did not explicitly require both hind-foot endpoints to remain outside a broad torso silhouette in a dorsal three-quarter pose
- next_action: rejected both initial sources, preserved them as named audit artifacts, used one fresh-canvas retry per language, and accepted only posters with four attached limbs and both hind feet fully visible outside the torso
- tomorrow_change: for broad-bodied quadrupeds viewed dorsally or in dorsal three-quarter, require both complete hind feet beyond the outer torso silhouette in the first prompt and visual gate

Improvement Resolution
- tag: #species-identity-drift
- count: 3
- threshold: 3
- improvement: added the explicit broad-torso hind-foot endpoint rule to `automation-2-production-policy.md` and synchronized both accepted-language prompt records
- files_changed: automation-2-production-policy.md, bilingual image prompts, package README, INDEX, current state, Daily Quality Loop, and Automation memory
- validation: both accepted direct sources pass exact 2:3/full-canvas QA; canonical PNGs, bilingual X format, full package, sidecars, full-size, phone-size, and whitespace QA pass
- counter_reset: yes

## 2026-08-12 — Table Mountain Ghost Frog official IUCN evidence synchronized

Daily Quality Loop
- issue: the initial package used the 2025 publication year as the public IUCN footer year because the field-level assessment date had not yet been directly inspected
- priority: evidence correction
- tags: #official-evidence-sync #assessment-year-drift
- cause: the specialist reassessment notice identified the 2025 Red List release but did not expose the formal `Date Assessed` field used by the public-footer policy
- next_action: verified the user-supplied official 12-page PDF and matching species-page capture, locked Global EN B1ab(iii), 9 April 2024 assessment, 2025 publication, and record `e.T9773A247846769`; corrected both poster footers with localized edits and synchronized Copy Lock, prompts, X blocks, sidecars, README, Sources QA, INDEX, current state, and Automation memory
- tomorrow_change: when an official release notice and field-level assessment page are not both directly inspectable, keep assessment year unresolved until the PDF or `Last assessed` field is confirmed; never infer the public footer year from the Red List release year

## 2026-08-12 — Table Mountain Ghost Frog rejected-image cleanup

Daily Quality Loop
- issue: two anatomy-rejected direct sources and four superseded 2025-footer source/posting PNGs remained after the corrected package passed final QA
- priority: exact-target cleanup
- tags: #rejected-image-cleanup #selected-poster-preservation
- cause: rejected and superseded images were retained temporarily during visual and official-evidence correction
- next_action: protected the four corrected canonical PNGs and two official evidence files, enumerated six exact regular PNG targets, verified no links or directories, and moved only those six files to the Windows Recycle Bin at the user's request
- tomorrow_change: after canonical and evidence QA passes, offer one exact-target recoverable cleanup instead of leaving rejected assets indefinitely

## 2026-08-13 — Bekko Tombo user-selected recovery

Daily Quality Loop
- issue: a localized leg-topology correction added stiff free leg shapes and weakened the original poster's natural four-wing composition without producing a clearly better whole
- priority: subjective visual recovery
- tags: #selected-poster-preservation #species-identity-drift
- cause: the correction optimized isolated leg traceability after the initial source had already achieved the strongest species-specific silhouette, exact copy, three illustrated cards, and authored wetland composition
- next_action: verified the user's selected PNG was byte-identical to the initial source, promoted that exact poster without pixel alteration, preserved the rejected retry, and completed the English companion on its first generation
- tomorrow_change: for perched insects, reserve six-leg readability through the first pose and perch geometry; when an informed user explicitly selects a source-gate-passing stronger whole, preserve that exact source before companion production

## 2026-08-13 — Bekko Tombo fresh rebuild stopped

Daily Quality Loop
- issue: renewed review found the earlier accepted poster anatomy unsafe, while both a new anatomy-led canvas and one final composition-from-scratch canvas still produced materially wrong leg or wing topology
- priority: incomplete-publish-blocker
- tags: #diagnostic-anatomy-priority #rejected-image-cleanup
- cause: repeated prompt constraints did not reliably produce a naturally perched six-legged dragonfly with four unambiguous attached wings
- next_action: stopped the regeneration loop, withdrew the prior bilingual pair, moved exactly seven old, superseded, and rejected PNGs to the Windows Recycle Bin, preserved official evidence and all text assets, and marked the package `incomplete, Rescue Run`
- tomorrow_change: do not resume with another denser prompt; require a deliberately different visual route anchored by a reliable real-anatomy reference or leave the topic incomplete

## 2026-08-13 — Bekko Tombo reference-led Rescue attempt

Daily Quality Loop
- issue: a user sketch offered a useful natural leg gesture but contained a broken wing, while real photographs were needed to control species and four-wing anatomy
- priority: incomplete-publish-blocker
- tags: #diagnostic-anatomy-priority #reference-role-separation
- cause: the first reference-led source improved the perch grip but exposed only three unambiguous hero wings; the one real-photo-only retry restored four wings but overlapped the six legs and drifted footer punctuation
- next_action: rejected and preserved both exact-2:3 Japanese candidates, stopped before English production, and kept the package `incomplete, Rescue Run`
- tomorrow_change: if resumed, establish a clean anatomy reference or topology sketch that simultaneously fixes four wing roots and six thorax-to-perch leg paths before attempting an integrated poster

## 2026-08-13 — Bekko Tombo user-selected reference recovery completed

Daily Quality Loop
- issue: further regeneration cost was no longer proportionate after the reference-led retry restored four clear marked wings but retained a naturally overlapped leg cluster
- priority: informed user visual selection
- tags: #selected-poster-preservation #reference-role-separation
- cause: the integrated field-note composition and four-wing species identity were strong, while strict six-path leg traceability remained difficult at the chosen three-quarter resting angle
- next_action: verified the user-supplied selection was byte-identical to the saved retry, promoted that exact Japanese source, accepted one English companion under the same leg-overlap allowance, normalized four canonical PNGs, recycled the unused three-wing candidate, synchronized ALT and package records, and closed `completed, local-ready`
- tomorrow_change: preserve explicit user-selected visual tradeoffs in QA records and stop spending generation budget once the user accepts a source-safe, coherent whole

## 2026-08-14 — Kipunji official IUCN evidence synchronized

Daily Quality Loop
- issue: the initial Kipunji public footer used the 2019 publication year before the official field-level assessment date became directly inspectable
- priority: evidence correction
- tags: #official-evidence-sync #assessment-year-drift
- cause: the citation year was treated as the assessment year until the user-supplied official PDF and Red List page capture exposed `Date Assessed: 20 March 2018`
- next_action: locked Global EN and assessment year 2018, preserved both official artifacts, synchronized public/source surfaces, and corrected only the final footer-year digit in the accepted bilingual artwork
- tomorrow_change: require a directly inspected assessment-date field before locking any dated public IUCN footer

## 2026-08-15 — Tea-tree Fingers Quality Run completed

Daily Quality Loop
- issue: the first Japanese poster rendered the fungus as raised glove-like cylinders rather than a low flattened branch-clasping stroma
- priority: species-identity correction
- tags: #species-identity-drift #growth-form
- cause: the first prompt did not separately gate substrate attachment, profile height, lobe geometry, and false glove-like silhouettes for a sessile organism
- next_action: rejected the first source, generated one fresh-canvas retry with the documented low flattened growth form, completed the English companion, and added a sessile-organism growth-form gate to production policy
- tomorrow_change: for sessile organisms, lock substrate attachment, relative scale, profile, surface, lobe geometry, and false silhouettes before the first generation

## 2026-08-16 — Jellyfish Tree Quality Run completed

Daily Quality Loop
- issue: the English footer correction redrew the full canvas despite a localized spacing instruction
- priority: poster-preservation
- tags: #localized-text-repair #selected-poster-preservation
- cause: the generative edit reinterpreted accepted artwork outside the footer
- next_action: rejected the broad edit and used a verified footer-only deterministic repair
- tomorrow_change: check global pixel drift immediately after localized edits and route broad redraws to the bounded text-safe repair

## 2026-08-16 — Jellyfish Tree official IUCN evidence synchronized

Daily Quality Loop
- issue: the local-ready package retained a fallback 2007 IUCN footer after the current 2025 official assessment became directly inspectable
- priority: fact-risk
- tags: #official-evidence-sync #old-status-risk
- cause: the initial run could not render the direct IUCN record and locked a Kew/CBD fallback route that was later superseded by the user-supplied official PDF and page capture
- next_action: verified Global CR C2a(ii), assessment date 12 August 2025, publication year 2025, and record `e.T37781A262047825`; preserved both official artifacts, synchronized public and evidence text surfaces, and changed only the footer year pixels in the accepted bilingual artwork
- tomorrow_change: when stronger official evidence arrives after local-ready closeout, reopen Evidence Lock and scan every public, sidecar, image, INDEX, and state surface for the superseded record before final QA

## 2026-08-17 — Automation state file-identity repair

Daily Quality Loop
- issue: `automation-2-current-state.md` and `daily-quality-loop.md` remained individually unwritable even though sibling files were writable and both targets had normal attributes and Modify-capable ACLs
- priority: ops-friction resolved
- tags: #workflow-friction #file-identity-repair
- cause: stale file-specific sandbox authorization identity rather than a broad ACL, ownership, read-only, or sharing-lock problem
- next_action: protected original content and SHA-256 hashes, rebuilt both files as new filesystem objects, replaced only the exact two targets with backups retained, and verified new write handles plus Jellyfish Tree state synchronization
- tomorrow_change: if the same signature recurs, use one exact-target backup-and-recreate repair; do not broaden ACLs or change ownership

## 2026-08-17 — Jellyfish Tree rejected-image cleanup

Daily Quality Loop
- issue: two explicitly rejected English audit PNGs remained in the completed package after the canonical bilingual pair passed final QA
- priority: recoverable artifact cleanup
- tags: #rejected-image-cleanup #selected-poster-preservation
- cause: the missing-space source and broad generative edit were retained temporarily while the localized footer-only repair and official 2025 evidence correction were verified
- next_action: protected the four canonical PNGs and evidence assets, verified the two exact rejected paths and hashes, moved only those files to the Windows Recycle Bin, and confirmed four canonical PNGs with zero rejected PNGs remaining
- tomorrow_change: after a localized repair passes pixel and package QA, offer one exact-target recoverable cleanup instead of retaining rejected audit art in `images/`

## 2026-08-17 — Jellyfish Tree GitHub closeout

Daily Quality Loop
- issue: the corrected and cleaned package was complete locally but had not yet been published to the repository remote
- priority: publication closeout
- tags: #github-closeout #remote-verification
- cause: GitHub publication remained intentionally separate from the no-approval Quality Run and the later file-identity repair
- next_action: committed the scoped package and synchronized workflow records as `2c9633d`, pushed that commit directly to `origin/master`, verified the remote ref, and synchronized the package, INDEX, and current state to `completed, published`
- tomorrow_change: keep future Quality Runs at `completed, local-ready` until an explicitly approved direct-push closeout verifies the remote branch

## 2026-08-17 — Tokashiki Freshwater Crab Quality Run completed

Daily Quality Loop
- issue: the direct IUCN record UI returned an unreadable body despite the specific global record being available by URL
- priority: source-access caveat contained
- tags: #source-access-caveat #assessment-year-verification
- cause: the IUCN web interface did not render a readable record body in this environment, so the primary record could not itself expose field-level text during this run
- next_action: retained the direct record URL and identifier `134902`, corroborated Global EN and 2015 with Japanese Ministry of the Environment and Okinawa Prefecture materials, kept local categories out of public copy, then completed first-pass bilingual posters and full QA
- tomorrow_change: when a direct IUCN record is temporarily unreadable, document the limitation, corroborate only with strong official sources, and retry the record before any later status change

## 2026-08-17 — Tokashiki Freshwater Crab official IUCN correction

Daily Quality Loop
- issue: the local-ready package used 2015 as the global IUCN assessment year after a Japanese source's 2015-list context was treated as field-level assessment evidence
- priority: fact-risk resolved
- tags: #official-evidence-sync #assessment-year-drift
- cause: the live IUCN UI was unreadable during the initial run, and the assessment's own Date Assessed, Year Published, criteria, and full assessment identifier were not directly inspected before Copy Lock
- next_action: used the supplied official PDF and matching current-page capture to lock Global EN under B1ab(iii)+2ab(iii), assessed and published 2008 as `T134902A4033497`; preserved both evidence artifacts and four superseded 2015 PNGs, then synchronized all public/package/state records with a bounded footer-only text-safe repair
- tomorrow_change: never promote a list context, PDF copyright year, or taxon-page numeric route into a public assessment year; require the assessment's own date fields and full assessment ID before Copy Lock

## 2026-08-18 — Tokashiki Freshwater Crab GitHub closeout

Daily Quality Loop
- issue: the corrected package was complete locally but had not yet been published to the repository remote
- priority: publication closeout
- tags: #github-closeout #remote-verification
- cause: GitHub publication remained intentionally separate from the Quality Run and later official-evidence correction
- next_action: committed the scoped package and synchronized workflow records as `a2d9066`, published that commit to `origin/master`, verified the remote ref, and synchronized README, INDEX, and current state to `completed, published`
- tomorrow_change: keep future Quality Runs at `completed, local-ready` until an explicitly requested closeout verifies the remote branch before changing published-state metadata
