from pathlib import Path
import hashlib
import json

P = Path(__file__).resolve().parents[1]
ja = ['オオシャコガイ', 'Tridacna gigas', '光を受けて、藻と暮らす', '体内の藻が光合成し、つくった栄養を貝に渡す。', '水からも、食べ物を', '海水をこし取り、小さなプランクトンも食べる。', '二枚貝で、いちばん大きい', '現生の二枚貝で最大の種で、殻は1mを超えることも。', 'IUCN Red List 2024: 深刻な危機 (CR)']
en = ['Giant Clam', 'Tridacna gigas', 'Algae share their food', 'Algae in its tissues use sunlight and pass nutrients to the clam.', 'A second way to feed', 'It also filters tiny plankton from seawater.', 'The largest living bivalve', 'Its shell can grow longer than one metre.', 'IUCN Red List 2024: Critically Endangered (CR)']

def write(name, text):
    (P / name).write_text(text.strip() + '\n', encoding='utf-8')

medium = '''Style/medium: crayon and oil-pastel field-notebook observation sketch on warm
textured paper; colored pencil only for small diagnostic details. Visible broken
strokes, layered pigment, paper showing through the drawing and imperfect
hand-drawn contours across the hero, habitat and card illustrations. Childlike
warmth with accurate species geometry and adult editorial direction. Use matte,
sketched shading; avoid photorealism, glossy 3D rendering, airbrushed gradients,
cinematic lighting and watercolor/gouache/ink as the dominant medium. Keep type
legible; do not sacrifice exact text or diagnostic anatomy to roughness.'''

common = '''Use case: infographic-diagram
Asset type: complete educational poster, exact vertical 2:3, 1024x1536 pixels.
Primary request: Draw an integrated curiosity-first field observation page about Tridacna gigas. Full artwork fills the complete canvas; warm tinted paper and sketched habitat continue to every edge with no white/transparent bands. One dominant living adult clam and exactly three numbered illustrated explanatory cards. All text is part of the artwork, no mockup, no additional wording.
Reference roles: references/iucn-giant-clam-oblique.jpg (Mei Lin Neo) and references/iucn-giant-clam-top.jpg (James W. Fatherree) are biological identity references only. The purple-frog benchmark is a style reference only for broken crayon texture and warmth; copy no frog, text, conservation category or layout.
Scene: a sunlit shallow tropical western-Pacific coral-reef floor. Muted sea-blue and teal marks above; sparse low coral rubble and sandy ground below. No geographical map and no aquarium setting.
Hero: one living adult giant clam viewed from a gently elevated oblique angle. Its two very thick heavy ivory shell valves rest on reef rubble, opening upward. Each valve has four or five broad radial folds/ribs that meet the upper edge as broad triangular peaks, NOT dozens of narrow scallop ribs, and NO projecting rows of shell scutes/spikes. Its mantle is one connected sheet of golden-olive brown tissue, dark at the edge with restrained teal/blue flecks and a few pale windows; drape it in broad rounded waves along the zigzag shell rim. The mantle is living tissue within the shell, not a plant or a flower. Follow the photographs for connected top surface, asymmetry and openings: a low elongated inhalant slit with smooth edges, no tentacle fringe; a separate small raised round exhalant opening farther along the central axis. No large central cartoon mouth, teeth, eyes on stalks, tongues, coral growing out of mantle, detached lobes or extra valves. Shell and mantle variation is natural; do not paint an electric-blue generic aquarium clam. Naturally hide the underside, hinge, far shell base and some rib roots behind mantle, shell or substrate. No transparent dissected hero.
Composition: title and scientific name across the top, dominant broad hero occupying the middle half, ample air around its silhouette. Use the uneven width and curvature of the clam to arrange three warm paper observation notes in the lower third with one note slightly higher at the side. These are handmade observation cards, not equal software panels. Keep all three explanations fully inside their own cards with generous margins, clear type, and natural line wrapping. Quiet thin footer at bottom; no source labels. The large clam must remain unobscured.
Card 1 is strongest: numbered 1, heading and explanation, illustration of sun rays toward a small connected mantle-edge study with a circular conceptual magnification of tiny golden algae cells in tissue. This is a schematic magnification, not free-floating seaweed growing from the clam. No invented organs or extra text.
Card 2: numbered 2, heading and explanation, a small complete clam in reef water with tiny plankton dots and a restrained flow arrow toward its smooth inhalant slit. Show only external water flow; no cutaway gills or invented internal pathways.
Card 3: numbered 3, heading and explanation, a small study of the two thick broad-ribbed valves seen obliquely. Emphasize bulky shell scale visually without a numeric ruler, human hand, or fabricated proportion comparison.
Typography: editorially clear hand-lettered heading and dark clean explanatory lettering with a handmade feel. All nine locked strings must be verbatim, in order. Card numbers 1, 2, 3 are the only extra text. No added English or Japanese labels, logos, watermarks, slogans, citation text, or duplicate hero.
'''

for lang, strings in [('ja',ja),('en',en)]:
    title, sci, h1,e1,h2,e2,h3,e3,footer = strings
    write(f'infographic-copy-{lang}.md', f'''Copy format: cards-v2
Title: {title}
Scientific name: *{sci}*

Observation cards:
1. Heading: {h1}
   Explanation: {e1}
2. Heading: {h2}
   Explanation: {e2}
3. Heading: {h3}
   Explanation: {e3}

Footer/status:
{footer}''')
    specific = 'Language: Japanese. Render all Japanese glyphs precisely. Scientific name stays in Latin. ASCII footer punctuation: no space before colon, one after colon, one before (CR). The shell-length text is exactly 1m with no inserted space.' if lang=='ja' else 'Language: English. Preserve the accepted Japanese composition, hero geometry, palette, cards and crayon texture; Japanese poster is a composition reference only, real photographs remain identity references. Replace all Japanese text with the locked English text below. Footer punctuation: no space before the colon, one space after the colon, one space before (CR). No spaces inside (CR). Use natural line breaks without altering words or punctuation.'
    write(f'image-prompt-{lang}.md', common + '\n' + medium + '\n\n' + specific + '\n\nText, verbatim:\n' + '\n'.join('"'+s+'"' for s in strings))

write('x-post-ja.md', '''# X投稿セット — 日本語

添付画像: images/giant_clam_japanese_posting_2026-10-06.png

## Main post

```text
殻の中に、日差しから栄養をつくる藻がいる。
オオシャコガイ
Tridacna gigas

IUCN Red List 2024: 深刻な危機 (CR)
#世界の知らない生き物 #GiantClam
```

## Story reply

```text
浅いサンゴ礁で、大きな貝が波打つ外套膜を広げる。その体内では藻が光を受け、栄養を貝に渡す。貝自身も海水からプランクトンをこし取る。動かない食卓には、光と水の二つの入口がある。

それがオオシャコガイの、ちょっと不思議な暮らし。
```

## ALT text

```text
縦長2:3のクレヨンとオイルパステルの観察ポスター。浅いサンゴ礁の砂と礫の上に、一個体のオオシャコガイを大きく描く。厚い白い二枚の殻には大きな稜があり、開いた上面に黄金色からオリーブ色の外套膜が波打つ。濃い縁、小さな青緑の斑、入水側の細長い裂け目と別の小さな出水口が見える。三枚の番号と小さな絵つきカードが、体内の藻から光合成の栄養を受け取ること、海水からプランクトンをこし取ること、現生の二枚貝で最大の種で殻が1mを超える場合があることを説明する。下部にIUCN Red Listの2024年評価による深刻な危機CR表示。
```

## Source/context reply

```text
出典メモ：IUCN公式で世界CR・2024年5月23日評価、同年刊行を確認。共生・ろ過摂食・大きさはモントレーベイ水族館。旧資料のVUは現在の評価と区別。 https://www.iucnredlist.org/species/22137/119167161 https://www.montereybayaquarium.org/animals-the-ocean/animals-a-to-z/giant-clam
```''')
write('x-post-en.md', '''# X posting set — English

Attach: images/giant_clam_english_posting_2026-10-06.png

## Main post

```text
Inside this shell, algae turn sunlight into food to share.
Giant Clam
Tridacna gigas

IUCN Red List 2024: Critically Endangered (CR)
#GiantClam
```

## Story reply

```text
On a shallow reef, a giant clam spreads its rippled mantle. Algae inside its tissues capture light and pass nutrients to their host. The clam also filters plankton from seawater. For this stationary diner, food arrives through both sunlight and water.
```

## ALT text

```text
Vertical 2:3 crayon and oil-pastel observation poster. One giant clam rests on sand and rubble on a shallow coral reef. Its two thick ivory valves have a few broad radial folds. Golden-olive mantle tissue spreads in rounded waves along their zigzag margins, with dark edges and small teal flecks. An elongated inhalant slit and a separate small raised exhalant opening are visible. Three numbered illustrated notes explain food shared by photosynthetic algae inside the tissues, plankton filtered from seawater, and the largest living bivalve species, whose shell can exceed one metre. A quiet footer gives the IUCN Red List 2024 assessment: Critically Endangered (CR).
```

## Source/context reply

```text
Source note: IUCN confirms Global CR, assessed 23 May 2024; published 2024. Monterey Bay Aquarium supports symbiosis, filter feeding and size. Older VU accounts are outdated. https://www.iucnredlist.org/species/22137/119167161 https://www.montereybayaquarium.org/animals-the-ocean/animals-a-to-z/giant-clam
```''')

write('evidence/iucn-browser-fields-2026-10-06.md', '''# Official IUCN field transcription

Checked 2026-10-06 in Codex in-app browser; not a downloaded assessment PDF.
URL: https://www.iucnredlist.org/species/22137/119167161
Initial navigation-only page rendered on the next AX state request.

- Species: Tridacna gigas / Giant Clam
- Record: T22137A119167161
- Global category and criteria: Critically Endangered, A2acd, ver 3.1
- Date Assessed: 23 May 2024
- Year Published: 2024
- Scope: Global
- Population trend: Decreasing; no numerical population claim used.
- Upper/lower depth: 0 / 20 metres
- System / habitat: Marine / Marine Neritic
- Taxonomy: Animalia > Mollusca > Bivalvia > Cardiida > Cardiidae > Tridacna
- Native extant entries include Australia, Indonesia, Malaysia (Sabah), Palau, Philippines, Solomon Islands and Timor-Leste. Range is not generalized from all Tridacna species.
- Citation displayed: Neo, M.L. & Li, R. 2024; e.T22137A119167161.
- DOI: https://dx.doi.org/10.2305/IUCN.UK.2024-2.RLTS.T22137A119167161.en

Web text fetch returned 403; browser fields directly settled the lock. No second-hand-date fallback and no official PDF claim. Reference image credits displayed in gallery/photographs: Mei Lin Neo and James W. Fatherree. Reference asset URLs are recorded in sources-qa.md.''')

write('sources-qa.md', '''# Giant Clam — Evidence Lock and production QA

Workflow mode: Quality Run
Editorial classification group: Other invertebrates
Evidence Lock: complete before art
Copy Lock: cards-v2; nine strings per language locked before art

## Topic diversity and selection

Recent eight completed: Okapi (Central Africa, Mammals), Secretarybird (sub-Saharan Africa, Birds), Giant Anteater (Central/South America, Mammals), Tri-spine Horseshoe Crab (East/SE Asian coasts, Other invertebrates), Pink Waxcap (Europe grassland, Fungi and lichens), Venus Flytrap (Carolina wet savanna, Plants), Banded Archerfish (Indo-Pacific estuary, Fishes), Namaqua Chameleon (SW African desert, Reptiles).
Latest twenty completed entries were read from INDEX: bat/cloud-rat mammals, birds, butterfly/weevil insects, sea star, tortoises/chameleons, aquatic and rosette plants, seadragon/archerfish, salamander, fungus and horseshoe crab. New subject is a stationary bivalve with shell-and-mantle silhouette and nutritional partnership rather than movement, hunting or leaf-shape change. Indo-Pacific region overlaps the recent fish, but sunlit reef floor differs from mangrove surface hunting. No quota or cooldown applied.

| Candidate | Familiarity and discovery | Contribution to variety | Conservation context | Local-knowledge caution |
|---|---|---|---|---|
| Giant Clam / Tridacna gigas | Familiar large shell, less familiar food shared by algae inside tissues | Stationary reef bivalve, broad ribbed form; nutritional partnership | Official Global CR and exact assessment date directly confirmed | No assertion that people at home do not know it |
| Giant Dragonfly / Petalura gigantea | Semi-aquatic burrowing larva, flying adult; Australian Museum | Australian wetland insect, distinct from butterfly/weevil | Regional NSW endangered route; global dated assessment and Japanese name not settled in bounded slate | No regional-to-global category conversion |
| Monkey Puzzle / Araucaria araucana | Familiar garden tree with persistent stiff triangular leaves; Kew | South American conifer, strong contrast but plants appeared three days ago | Kew Global EN display; exact IUCN date not needed after selecting clam | Retain recognition and Mapudungun names in source context, no unknown-to-everyone claim |

Selected clam combines a strong supported discovery with new body form and feeding story. Naming/duplicate gates: accepted name, Tridacna (Tridacna) gigas, Chama gigas, Chama gigantea, Dinodacna cookiana, Giant Clam, True Giant Clam, killer clam, オオシャコガイ, オオジャコガイ, オオジャコ and giant-clam searched across full workspace Markdown, INDEX, general MEMORY and full Automation memory; no completed, retired or unfinished collision. Nautilus mentions in squid packages are unrelated comparisons.

## Evidence Lock and claim check

| Claim / exact scope | Verdict / safe wording | Source / confidence |
|---|---|---|
| Accepted name and lineage | accurate: Tridacna gigas (Linnaeus, 1758); Animalia > Mollusca > Bivalvia > Cardiida > Cardiidae > Tridacninae > Tridacna | GBIF Backbone / IUCN, high |
| Japanese name | accurate: オオシャコガイ is the GBIF public Japanese name; オオジャコガイ is a documented variant in Miyakojima museum search result | GBIF exact-taxon page, high for selected spelling; museum PDF not obtained, not represented as reviewed |
| Global status and date | accurate: CR A2acd ver 3.1; assessed 23 May 2024, published 2024; public footer uses assessment year | Official directly rendered IUCN fields, high |
| Sunlit coral-reef floor | accurate: shallow tropical Indo-Pacific reef; scene is western-Pacific reef, not all genus-wide localities | IUCN extant geography / species habitat, high |
| Card 1: algae share food | accurate: photosynthetic symbionts in tissues pass nutrients to host; clam is an animal, not itself a plant | Monterey Bay Aquarium; exact-taxon ADW food habits corroborates, high |
| Card 2: plankton filtering | accurate: particulate food also filtered from seawater; no exclusive reliance on sunlight claim | Monterey Bay Aquarium; ADW food habits, high |
| Card 3: largest living bivalve, shell over 1m possible | accurate: species-level maximum/possibility, not all individuals; no population number or giant age claim | Monterey Bay Aquarium exact T. gigas size statement, high |
| Shell/soft-body identity | accurate: heavy paired valves, few broad radial folds, mantle tissue, smooth inhalant slit and separate raised exhalant aperture | Two exact-taxon official IUCN photographs; ADW physical description and DORIS identification, high |

The 2001 ADW and DORIS VU lines are outdated against directly confirmed 2024 IUCN CR. Their conservation/legal sections are not used. No population, ranked-threat, Red Sea presence, permanent byssal attachment, or legal-protection claim is copied from genus-wide or old accounts. Initial guessed EN search was discarded before lock; selected footer is CR.

## Compact visual identity

- Individual/stage: one living adult Tridacna gigas; external sex not diagnosed. Adult shell lacks projecting scutes; juvenile features not transplanted.
- Reference roles: references/iucn-giant-clam-oblique.jpg (Mei Lin Neo) settles connected mantle, shell attachment, reef substrate and raised exhalant aperture. references/iucn-giant-clam-top.jpg (James W. Fatherree) settles broad waves, golden tissue/dark margin and smooth elongated inhalant slit. Two images only; no extra gallery export.
- Defining feature 1: two thick broad-ribbed valves, not a thin many-ribbed scallop; outer shell visible below mantle in oblique image; source specifies four/five broad ribs.
- Defining feature 2: a connected golden/olive mantle spreads on the upper shell margins in broad rounded waves; both images show dark edging and variable pale windows/flecks.
- Defining feature 3: two distinct openings on the exposed mantle surface; larger smooth slit at one end, smaller raised round outlet at the other. Top photo settles position/shape; oblique photo settles outlet height. No tentacle fringe.
- Defining feature 4: upward opening, heavy shell resting among sand/coral rubble, coral behind rather than a coral-shaped body; both habitat views.
- Natural pose: gently elevated oblique. Mantle naturally hides parts of inner shell and rib roots; far shell base, hinge and underside need not be visible. No natural-limb visibility issue.
- False silhouettes: generic scuted aquarium clam, many-ribbed scallop, flower/seaweed growing from shell. Specific absence of shell scutes, broad radial geometry and attached soft tissue distinguish these.
- Uncertainty: colour is individual variation, not diagnosis alone. Count of mantle waves is not claimed as shell-rib count. Algae inset is a conceptual cell magnification, not a literal organ section. Card 2 shows only outside water flow; no hidden feeding anatomy exposed.
- Style-only reference: ../../generated_infographics/purple_frog_ja_2026-04-28.png inspected before art; controls crayon texture/warmth only.

## Three card illustration locks

1. Sun/connected mantle study and conceptual algae-cell enlargement support nutrient partnership.
2. Small complete clam with plankton dots and outside flow toward smooth slit supports an additional food route.
3. Paired broad-ribbed shell study supports exceptional bivalve size without a fabricated ruler.
All headings and explanatory sentences are locked in the two infographic-copy files and the verbatim prompt blocks. Main-hook drafts: JA selected 殻の中に、日差しから栄養をつくる藻がいる。; alternate 大きな貝の食卓には、光と水の入口がある。 EN selected Inside this shell, algae turn sunlight into food to share.; alternate A sunlit reef feeds this clam in two different ways. Latest two Japanese main/story patterns were compared; no repeated opening retained.

## Sources and reference provenance

- IUCN official: https://www.iucnredlist.org/species/22137/119167161 — directly read 2026-10-06. Field transcription in evidence/iucn-browser-fields-2026-10-06.md; no PDF claimed.
- Monterey Bay Aquarium: https://www.montereybayaquarium.org/animals-the-ocean/animals-a-to-z/giant-clam — genus-labelled page, exact T. gigas size statement and shared feeding biology used; broad range/legal/colour claims excluded.
- GBIF Backbone: https://www.gbif.org/es/species/4372619 — selected Japanese name, accepted name, synonyms and lineage.
- University of Michigan ADW: https://animaldiversity.org/accounts/Tridacna_gigas/ — species-specific morphology/food, 2001 account; status/legal sections excluded as outdated.
- DORIS specialist identification: https://doris.ffessm.fr/Especes/Tridacna-gigas-Benitier-geant-2488 — published 2025, revised 2026; morphology/variation used, VU/distribution excluded.
- Japanese name variant pointer: https://www.city.miyakojima.lg.jp/soshiki/kyouiku/syougaigakusyu/hakubutsukan/files/no.27_1-26_adaniyaakira.pdf — official museum 2023 search result; web fetch timed out, shell network denied; not treated as read PDF. GBIF directly supports the chosen spelling.
- Candidate sources: https://australian.museum/learn/animals/insects/south-eastern-petaltail/ and https://www.kew.org/plants/monkey-puzzle-tree .
- Reference 1 asset: https://wir.iucnredlist.org/PPqMzMRm-dqdjMW-gGS.jpg — Mei Lin Neo.
- Reference 2 asset: https://wir.iucnredlist.org/Chm4cSF4-dqndlB-k2N.jpg — James W. Fatherree.
Both downloaded through observed pageAssets and inspected locally; source photographs are identity references, not posting attachments. Asset bundling took about 14 minutes, then succeeded. Rights/credit strips are retained in the saved originals and are not copied into generated art.

## Acceptance record — pending art

Mechanical pre-image pass required before generation. Direct-source gates immediately after every generation. Biological identity, exact text, three illustrated explanations, medium and full/phone review remain separate manual gates. No explicit user adoption claimed. State incomplete until both accepted direct sources, posting PNGs and sidecars exist.''')

write('README.md', '''# Giant Clam / オオシャコガイ bilingual infographic package

State: `incomplete`
Workflow mode: Quality Run
Editorial classification group: Other invertebrates
Broad native region: tropical Indo-Pacific; selected scene is shallow western-Pacific coral reef.

## Posting sets

- [日本語の投稿セット](x-post-ja.md)
- [English posting set](x-post-en.md)

Each main post attaches its own language's single poster. Both remain local; GitHub and X publication are separate.

## Poster files — planned canonical selections

- [Japanese direct PNG](images/giant_clam_japanese_imagegen_2026-10-06.png)
- [Japanese posting PNG](images/giant_clam_japanese_posting_2026-10-06.png)
- [English direct PNG](images/giant_clam_english_imagegen_2026-10-06.png)
- [English posting PNG](images/giant_clam_english_posting_2026-10-06.png)

## Copy-ready backups

- Japanese: [caption](images/giant_clam_japanese_posting_2026-10-06.caption.txt), [story](images/giant_clam_japanese_posting_2026-10-06.story-reply.txt), [ALT](images/giant_clam_japanese_posting_2026-10-06.alt.txt), [source](images/giant_clam_japanese_posting_2026-10-06.source-note.txt).
- English: [caption](images/giant_clam_english_posting_2026-10-06.caption.txt), [story](images/giant_clam_english_posting_2026-10-06.story-reply.txt), [ALT](images/giant_clam_english_posting_2026-10-06.alt.txt), [source](images/giant_clam_english_posting_2026-10-06.source-note.txt).

## Evidence and production

- [Evidence Lock and QA](sources-qa.md), [JA Copy Lock](infographic-copy-ja.md), [EN Copy Lock](infographic-copy-en.md).
- Actual prompt paths: [JA](image-prompt-ja.md), [EN](image-prompt-en.md). Built-in Image Gen planned.
- Identity references: [oblique](references/iucn-giant-clam-oblique.jpg), [top](references/iucn-giant-clam-top.jpg). Existing purple-frog benchmark is style-only.
- Official IUCN species fields directly confirmed Global CR A2acd, assessed 23 May 2024, published 2024. [Field transcription](evidence/iucn-browser-fields-2026-10-06.md).
- Poster/main public footer uses assessment year. Old secondary VU pages are excluded from conservation wording. Japanese spelling follows GBIF; オオジャコガイ is a naming variant.
- Acceptance caveats and visual review will be recorded after production. No Git/GitHub/X mutation authorized by this run.''')

refs = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (P/'references').glob('*.jpg')}
write('audit/reference-hashes.json',json.dumps(refs,indent=2))
