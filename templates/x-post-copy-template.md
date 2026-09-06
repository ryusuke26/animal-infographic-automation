# X post copy template

Use one file per language. For packages dated 2026-07-28 or later, keep exactly
these four sections and put each copy target in its own fenced `text` block:
main post, story reply, ALT text, and source/context reply. Earlier three-block
packages are grandfathered and need not be rewritten.

## Main post

- Attach the single accepted poster in the post's language: Japanese for the
  Japanese main post, English for the English main post. Provide the companion
  language in a separate reply/post if wanted; when both are explicitly requested
  together, put the audience's language first. Both files are still produced.
- Open with the strongest supported discovery, contrast, scene or action.
  Write two short hook candidates during drafting and select one; keep only the
  selected text in the posting set. Do not save the most interesting fact only
  for a reply. One follow-through sentence before the identity lines is allowed.
- Put the public common name and scientific name on two adjacent standalone
  lines after the hook. Do not fold them into prose.
- Follow with the quiet conservation-status footer.
- End with 1-2 hashtags. Always include the English common name with spaces and
  punctuation removed, for example `#Kea` or `#HimalayanMonal`.
- Keep this post short. The fuller natural-history story belongs in the first
  reply.
- Main post and story reply each have a budget of 275 X-weighted characters,
  counted with the official parser (CJK generally 2, URLs 23, emoji sequences 2).
  Do not count raw Unicode characters or cut based on their number.
- Avoid a generic definition such as `<name>は〜です` in the opening.
- Reveal the name after the hook when that improves curiosity.
- Compare the latest two completed posts and change the opening and sentence
  pattern when they feel repeated.
- Frame unfamiliarity as the viewer's discovery, not universal ignorance.
  Never claim that nobody knows the species or that it is unknown in its home
  region. Prefer viewer-relative wording or a concrete scene that lets the
  organism feel newly discovered without making a universal familiarity claim.

```text
<species-specific hook>
<public common name on its own line>
<scientific name on its own line>

<quiet status footer>
<#EnglishCommonName hashtag, plus at most one series hashtag>
```

## Story reply

Write the first reply as the fuller natural-history story, not as the three
poster cards copied into sentences.

- Let the reader follow one observable progression, such as setting -> visible
  identity -> movement -> consequence. Connect at least two locked facts
  through cause, contrast, movement, or observation instead of listing them.
- Vary short and long sentences. Do not use numbered facts or three parallel
  bullet sentences.
- Use concrete habitat, body, and behavior detail when the evidence supports
  it. Never add filler solely to use the available limit.
- Count this reply independently from the main post, ALT text, and source
  reply, using the weighted budget above.
- If the composer highlights only an overflow segment, preserve the established
  structure and fuller story. Shorten only enough low-value wording to clear
  that overflow instead of broadly rewriting the reply.
- Avoid unsupported absolutes (`only`, `exclusive`, `nothing else can reach`)
  and purpose-driven evolution wording such as `evolved in order to`.
- Keep curiosity first and conservation second: let the reader meet the
  organism through habitat, appearance, or behavior before the story turns
  toward a source-supported risk or dependency. Do not turn the reply into an
  advocacy slogan or imply that unfamiliarity itself proves endangerment.
- For Japanese packages dated 2026-07-21 or later, end with the exact standalone
  line `それが<日本語の種名>の、ちょっと不思議な暮らし。`. Replace the placeholder
  with the public Japanese poster title. Do not use
  `ちょっと不思議な暮らしがあります。` or
  `ちょっと不思議な暮らしをしています。`.

```text
<fuller connected discovery story>

<Japanese exact series ending when applicable>
```

## ALT text

Describe the actual attached poster in the same language. When posting the
English companion separately, use its English ALT instead of reusing Japanese ALT.

```text
<complete ALT text>
```

## Source/context reply

For new cards-v2 packages keep this publishable as one ordinary reply within
275 X-weighted characters: authority, relevant year/context and one or two direct
links. Put the detailed evidence table and complete bibliography in sources-qa.md.
Do not remove a material uncertainty to fit the limit. If it cannot be stated
accurately within the budget, revise the source selection/wording before art.
Historical long source blocks are retained as archival copy, not certified as
fitting one ordinary X reply.

```text
<Japanese must begin with 出典メモ： / English must begin with Source note:>
```

Generate sidecars with scripts/sync_posting_sidecars.py; the two X Markdown files
are the editing source of truth. Templates/x-launch-notes.md contains optional
profile drafts and one lightweight distribution experiment, not daily run gates.
