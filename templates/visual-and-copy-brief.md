# Visual and copy brief

Use this inside the existing sources-qa.md; do not create another per-run file.
The production policy is authoritative. This template adds no reviewer or
generation step to a normal run. Project format is vertical 2:3.

## Visual identity

- Individual/stage: exact taxon, sex and life stage when material.
- Reference roles: identify each real photograph/description and its purpose;
  keep species-identity references separate from composition references.
- Diagnostic features: 3-5 defining features, each paired with the exact
  reference image region or source description. Describe position, shape and
  attachment; count alone is insufficient. Separate head and body pattern zones.
- Natural pose: one reference-supported viewpoint, and what may be occluded.
- False silhouette: only the 1-3 most likely confusions, with concrete differences.
- Uncertainty: do not turn an unreadable feature into an invented instruction.

Review the full defining-feature set after a retry, including unchanged regions.
Trace visible anatomy; do not force hidden limbs into view. Reject extra limbs
or impossible attachment, not natural overlap. A detail inset must show its
connection/context clearly; a complete miniature animal is optional.

For high-risk anatomy only, a single text-free identity anchor may precede the
poster. Compare it with real references before accepting it. It is an extra
bounded attempt, not a new retry pool: if wrong, resolve the evidence/pose
before further generation. A generated anchor is not biological evidence.

## Three cards

Choose three complementary discoveries, strongest first. Habitat, appearance
and behavior are useful options, not fixed slots. Cover habitat in the scene
or copy without spending a card on a generic location if stronger material exists.

For each card record: heading / explanation / supporting source / illustration.
Heading invites noticing; one short sentence explains the observation, contrast,
mechanism or change. Do not invent a purpose or causal explanation. Aim initially
for about 8-16 Japanese heading characters and 20-40 explanation characters;
these are drafting guides, not gates. Prefer meaningful readable copy to quotas.
English conveys the same claim naturally. Reserve space for both languages.

Use detail studies, attached insets, habitat scenes, developmental comparisons,
or a complete animal as appropriate. Do not duplicate the hero merely to fill cards.

Example of editorial structure (not a species fact to reuse without evidence):
"成長すると、葉が変わる" + "幼木の葉は細長く、成木では幅広い形になる。"

## Copy Lock format for new packages

Use the same format in each infographic-copy file. Every heading AND explanation
belongs to Copy Lock; generate neither extra prose nor a label-only substitute.
Existing label-format packages remain valid and are not migrated automatically.

```text
Copy format: cards-v2
Title: <public name>
Scientific name: *<accepted name>*

Observation cards:
1. Heading: <discovery heading>
   Explanation: <one source-supported explanatory sentence>
2. Heading: <second heading>
   Explanation: <second sentence>
3. Heading: <third heading>
   Explanation: <third sentence>

Footer/status:
<exact status footer>
```

The image prompt's `Text, verbatim:` block has nine quoted strings, in order:
title, scientific name, card 1 heading, card 1 explanation, card 2 heading,
card 2 explanation, card 3 heading, card 3 explanation, footer. Card numbers are
layout elements. Place each heading and explanation only in its assigned card.

## Accepted output record

In the existing package README record each language's selected direct/posting
filenames, the exact prompt file used for the selected attempt, reference files,
and any acceptance caveat. Keep historical prompts labeled as historical.
In sources-qa.md distinguish mechanical pass, visual review and explicit user
adoption. Neither validator success nor adoption certifies an unverified feature.
