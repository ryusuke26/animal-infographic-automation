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
#species-identity-drift
#image-text-error
#layout-overcrowded
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

At Phase 6, after recording the current issue:

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
