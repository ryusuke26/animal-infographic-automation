# Automation: 世界の知らない生きものインフォグラフィック日次制作

Create one complete curiosity-first bilingual infographic package in this
workspace. Use bio-discovery-infographic, endangered-species-factcheck and
imagegen when applicable. Follow the user's latest instructions.

Read automation-2-current-state.md, automation-2-production-policy.md,
templates/visual-and-copy-brief.md and templates/x-post-copy-template.md.
The production policy is the single source of quality rules; this prompt is
the execution entry point. Project requirements override generic skill examples
such as 4:5 layout or shortening copy into bare labels. Use exact vertical 2:3.
Do not import obsolete rules from historical package prompts or learning logs.
Choose one art direction after selecting the species and strongest supported
discovery, following the policy's Species-led art direction. Crayon/pastel
remains an option alongside woodblock, collage, landscape/portrait treatments
and contemporary art. No compulsory daily changes, weekday assignments or
quotas. Produce one Japanese/English pair in the same style and composition
concept; do not add routine multi-style trials. Match palette, brightness and
background density to the selected medium; no universal pale paper or benchmark.

1. Preflight in one batch: current state, INDEX, recent package folders, recent
   Automation memory and git status. Read the active guidance at the beginning
   of daily-quality-loop.md; search older entries only for a relevant failure,
   duplicate alias or unresolved counter. Resume an active unfinished package.
   Use bundled Python; verify its recorded fallback once if the runtime loader
   is unavailable. Use the installed X text helper offline; do not install
   dependencies during a normal production run.
2. Screen a small, varied candidate slate under the policy's naming, full-history
   duplicate, evidence and visual-viability gates. Apply its Topic diversity
   design across and within groups, body forms, habitats and discovery hooks;
   occasionally include familiar species with an unfamiliar supported aspect.
   Diversity actively informs selection without fixed quotas or cooldowns.
   Preserve the selected topic when tools encounter friction.
3. Complete Evidence Lock, the compact visual identity brief and bilingual
   Copy Lock before art. Record the selected style and reason briefly in the
   existing sources-qa.md; include its medium cues and diagnostic invariants in
   both poster prompts. Use cards-v2 for new packages: three headings with one
   explanatory sentence each, strongest discovery first. Settle defining
   structures from real references, including sex/stage variation and allowed
   natural occlusion. Run validate_package.py --pre-image <package>.
4. Generate the Japanese full poster, then run validate_direct_poster.py
   immediately. Review species identity, natural anatomy, all three illustrated
   explanations, exact text, chosen-medium coherence and mobile readability
   before the English companion. Match review to the selected medium while
   preserving diagnostic form, structures and markings; a mechanical pass
   does not establish visual acceptance.
   Apply the production policy's bounded retry and optional high-risk anchor
   rules. Never distort a natural pose to display every limb. After any retry,
   recheck every defining feature, not just the repaired region.
5. Generate the English companion with the accepted Japanese art direction,
   composition concept and real identity references. Apply the same source
   and visual gates. Normalize only accepted
   sources to 1024x1536. Record selected files, actual prompt paths and acceptance
   caveats in the existing README/sources-qa.md.
6. Prepare both X posting sets. Main post begins with the strongest supported
   discovery and attaches its own language's single poster by default; the
   companion language is available separately/in a reply. Never publish or send
   replies from this task without explicit user authorization. Run
   sync_posting_sidecars.py <package> --write, then validate_package.py <package>.
   The package validator already runs X-format checks; do not duplicate them
   unless diagnosing a failure. Review full-size and phone-size images once.
7. Finish once: after a successful daily package, perform the policy's weekly
   visual reflection only if the current Asia/Tokyo ISO week has no completed
   ledger marker. First use reviews available recent work; no backfill, new
   art or separate weekly automation. Compare species clarity, explanatory
   readability and visual variety; use reactions only when measured data is
   accessible. Record one concise result in daily-quality-loop.md and mirror
   its week key in current state, rechecking the ledger to avoid duplicate
   completion. Update package README, INDEX and current state. Record at most
   one concrete daily learning; retain the weekly pointer and unresolved carryover.
   Finish completed, local-ready. GitHub closeout and X publication are separate.
   Do not mutate Git or publish in a no-approval automation context.

Use the scripts under scripts/ with bundled Python. Their --help is sufficient
for ordinary operation; read implementation only when diagnosing a failure.
Mechanical passes never certify biological identity. If a material blocker
remains after the allowed retry, preserve work as needs review or incomplete;
do not enter an open-ended generation loop or silently change the species.

Final response links prominently to x-post-ja.md as 日本語の投稿セット,
x-post-en.md as English posting set, and both selected posting PNGs. Include
only material remaining caveats and the local-ready/publication state.
