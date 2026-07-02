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

- `fact-risk`: one occurrence can justify `fix-now` or `skill-candidate`.
- `publish-blocker`: two occurrences with the same tag justify a policy,
  prompt, or template update.
- `quality-drift`: three occurrences with the same tag justify a skill,
  prompt, or template update.
- `ops-friction`: three occurrences, or one large time sink, justify a small
  workflow change.

Do not update a skill or policy for every single logged issue. Single issues
usually stay in memory. Repeated tags become candidates.

## Source Access And IUCN

Do not convert "IUCN could not be opened" into a confident status claim.
When the live IUCN page is unavailable:

1. Retry during Evidence Lock when it is cheap.
2. Check official PDFs, official status-change tables, or a previously saved
   official screenshot/snapshot.
3. If an official snapshot is used, state the snapshot date or access caveat.
4. If only secondary sources are available, remove the IUCN category from
   public copy and use conservative evidence-availability wording.
5. If the IUCN category is central to the story and no official basis can be
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
