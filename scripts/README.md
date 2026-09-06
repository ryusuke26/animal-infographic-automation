# Production helpers

Use the bundled Python with Pillow. All validation and sidecar generation run
locally without API keys or network requests. Run commands from the project root.

X counting uses Node.js and the official `twitter-text` parser, pinned at 3.1.0
in x-text/package-lock.json. One-time installation (already performed for this
workspace; not a daily production step):

```text
npm ci --prefix scripts/x-text --ignore-scripts --no-audit --no-fund
```

Node is resolved from PATH; set INFOGRAPHIC_NODE to its absolute executable if
needed. A missing parser is an actionable validation error, never a silent
fallback to raw character counting. Unicode normalization, CJK, emoji sequences
and shortened URLs use the official parser. The project budget is 275 weighted
characters per main/story block; cards-v2 also checks the source reply.

Ordinary production commands:

```text
<bundled-python> scripts/validate_package.py <package> --pre-image
<bundled-python> scripts/validate_direct_poster.py --input <new-direct.png>
<bundled-python> scripts/normalize_poster.py --input <accepted-direct.png> --output <posting.png>
<bundled-python> scripts/sync_posting_sidecars.py <package> --write
<bundled-python> scripts/validate_package.py <package>
```

sync_posting_sidecars.py without --write checks only. It refuses missing or
ambiguous posting files and validates both languages before writing. Existing
matching sidecars are untouched. X Markdown files remain the source of truth.

Copy Lock supports historical three-label files and new cards-v2 heading /
explanation pairs. See ../templates/visual-and-copy-brief.md. Machine checks
compare locked text with prompts, not text rendered inside images, and never
certify species identity; visual review remains required.

Regression checks (temporary fixtures only; no accepted artifacts are rewritten):

```text
<bundled-python> -B -m unittest discover -s scripts/tests -v
```

Sources: [X counting rules](https://docs.x.com/fundamentals/counting-characters),
[official parser](https://github.com/twitter/twitter-text/tree/master/js).
