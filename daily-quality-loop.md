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
