"""Historical initial-production helper. Superseded by user-selected revision; do not rerun to overwrite current assets or QA records."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
def write(name, value):
    (ROOT / name).write_text(value.strip() + '\n', encoding='utf-8')

ja = ['コフラミンゴ', 'Phoeniconaias minor', '逆さのくちばしで、こす', '頭を逆さにして、水面近くの微小な藻類などをこし取る。', '夜に、湖から湖へ', '湖の条件が変わると、夜に別の湿地へ移動することが多い。', '泥の塔に、ひとつの卵', '泥を盛った巣をつくり、ふつう一個の卵を産む。', 'IUCN Red List 2018: 準絶滅危惧 (NT)']
en = ['Lesser Flamingo', 'Phoeniconaias minor', 'An upside-down sieve', 'With its head upside down, it filters tiny algae and other food near the surface.', 'Between lakes after dark', 'It often moves to other wetlands at night when local conditions change.', 'One egg on a mud tower', 'It builds a raised mud nest and usually lays a single egg.', 'IUCN Red List 2018: Near Threatened (NT)']

for lang, strings in [('ja', ja), ('en', en)]:
    text = f'Copy format: cards-v2\nTitle: {strings[0]}\nScientific name: *{strings[1]}*\n\nObservation cards:\n'
    for i in range(3):
        text += f'{i+1}. Heading: {strings[2+i*2]}\n   Explanation: {strings[3+i*2]}\n'
    text += '\nFooter/status:\n' + strings[-1]
    write(f'infographic-copy-{lang}.md', text)

policy = Path('automation-2-production-policy.md').read_text(encoding='utf-8')
medium = policy.split('```text\n', 1)[1].split('\n```', 1)[0]
common = '''Use case: scientific-educational
Asset type: finished integrated educational social poster, exact vertical 2:3 full canvas, 1024x1536 preferred.
Primary request: a curiosity-first Lesser Flamingo observation page. The full image itself is the poster, no mockup, no surrounding white canvas. Quiet conservation context, no advocacy.
Input roles: real standing Neil Jones and feeding Anissa Camp photos are biological identity references only. Existing purple-frog image is style reference only, controlling stroke texture and warmth, never its anatomy, labels or old layout.
Subject: one dominant adult Phoeniconaias minor, sex unspecified, in a natural lateral three-quarter standing pose in ankle-deep saline lake water on an East African Rift lake margin. Pale pink oval body, red-pink folded wing accents, long gently S-shaped pink neck. Small head, reddish-orange iris and dark facial skin connecting eye to bill. Strongly bent deep bill predominantly dark maroon/charcoal with black tip, small reddish zone; NEVER a pale pink bill with only a black tip. Two slender pink-red legs, small webbed feet. Keep coherent leg attachments under body and natural overlap; submerged toes/far foot may hide. Avoid yellow legs and yellow bill. Do not copy captive bands/fences/trees from photos. Natural soft rose adult variation; no fixed size, plumage phase or exact toe/feather counts.
Scene: mineral ochre/pale salt shoreline, soft sage-green and turquoise shallow lake, low distant earthy hills. No fake map, flags, tropical forest or exact named-location label. Warm paper fully filled to edges with sketched color, no blank white/transparent edge bands.
Composition: title and scientific name at top. The tall graceful bird is dominant in the upper/middle page, its head, bill, neck, body and legs unobstructed. Exactly THREE numbered illustrated observation cards, individually composed around its long silhouette, not a dashboard. A generous irregular cream field-note card at mid-left explains filtering; two lower asymmetrical field-note studies explain night movement and mud nest. Species-specific crayon number marks 1, 2, 3; legible headings and a useful sentence each. Warm muted handwritten editorial type, large readable letters and generous margins. No fourth note or duplicate main hero. Keep text separate from artwork inside cards; allow sensible line wraps without dropping words.
Card 1 spot illustration: lateral contextual study of lowered continuous pink neck and inverted intact head at water surface, using feeding photo orientation. Strong bend in dark bill retained; tip is at surface, head upside down, not diving the entire neck. Neck clearly continues into study frame, not a detached head. Tiny green marks in water are qualitative microscopic-food symbols; no invented internal filters, teeth, cutaway or exact counts.
Card 2 spot illustration: two small flying Lesser Flamingos over two schematic blue wetland patches under crescent moon; long necks extend forward and legs trail backward, pink coverts with black flight feathers, coherent two wings per bird, perspective occlusion allowed. Qualitative travel scene, no geographic route map, distance or guaranteed nightly schedule.
Card 3 spot illustration: attached low truncated-conical earthen mud nest on a salt-mud island, shallow bowl holding one pale egg. Not a twig nest, volcano, flower or deep cylindrical bucket. Usual single-egg clutch, no absolute claim.
Footer: one quiet integrated short line inside bottom safe area. All title, scientific name, six card strings and footer must be exact and appear once. No extra labels, prose, credits, logos or watermark. Card numbers are layout elements. Latin species spelling exact P-h-o-e-n-i-c-o-n-a-i-a-s minor.
'''
for lang, strings in [('ja', ja), ('en', en)]:
    specific = ('Language: Japanese. Preserve all kana, kanji and punctuation exactly.\n' if lang == 'ja' else 'Language: English. Companion of accepted Japanese composition; preserve palette, hierarchy, card concepts, natural anatomy and crayon medium. ASCII punctuation exactly: no space before colon, one space after colon, one space before (NT); retain the hyphen in upside-down and all full stops.\n')
    write(f'image-prompt-{lang}.md', common + '\n' + medium + '\n\n' + specific + '\nText, verbatim:\n' + '\n'.join('"'+s+'"' for s in strings))

write('evidence/iucn-browser-fields-2026-10-10.md', '''# Official IUCN field transcription
Checked 2026-10-10 in the rendered official in-app browser.
https://www.iucnredlist.org/species/22697369/129912906
- Accepted taxon: Phoeniconaias minor; Lesser Flamingo.
- Scope: Global.
- Category: Near Threatened (NT).
- Criteria: A2c+3c+4c, version 3.1.
- Date Assessed: 07 August 2018.
- Year Published: 2018.
- Population Trend: Decreasing. No population number used.
- Lineage: Animalia > Chordata > Aves > Phoenicopteriformes > Phoenicopteridae > Phoeniconaias.
The initial 2016 record T22697369A93611130 explicitly linked to this latest Global record. Followed that official link; did not use the 2016 assessment. Dynamic shell resolved on next observation.
The BirdLife South Africa 2025 regional VU assessment is scoped to South Africa, Lesotho and Eswatini and is not substituted for this global NT footer. Its table's 2024 Global context still cites the 2018 assessment; 2024 is not Date Assessed.
This is a field-level transcription, not a saved official assessment PDF. Public copy retains the 2018 assessment year.
''')

write('sources-qa.md', '''# Evidence Lock and Sources QA — Lesser Flamingo
Checked 2026-10-10. Evidence Lock and bilingual cards-v2 Copy Lock settled before art.

## Topic diversity and duplicate gate
Latest eight regions: Europe/British grassland; southeastern USA wet pine savanna; Indo-Pacific mangrove estuary; southwestern African desert; western-Pacific coral reef; South American Andes; Europe/British hedgerow; Ocean/Global warm Ningaloo water.
Latest eight groups: Fungi and lichens, Plants, Fishes, Reptiles, Other invertebrates, Plants, Mammals, Fishes.
Latest twenty scan (20 September–9 October): spoonbill/wing-display sunbittern/secretarybird, broad butterfly, salamander, ground mammals, two distinct reptiles, leaflike/estuary/open-water fishes, conifer/rosette/submerged plants, grassland fungus and benthic invertebrates. Saline inland water, long-legged wader, inverted bill and wetland-to-wetland night movement add variety. Filter feeding repeats yesterday's broad food-capture theme, but bill posture, scale, terrestrial-aerial movement and nest architecture differ strongly.

| Candidate | Familiarity and discovery | Contribution to variety | Conservation context / gate | Local-knowledge caution |
|---|---|---|---|---|
| Lesser Flamingo / Phoeniconaias minor | Familiar pink silhouette; upside-down surface filtering and night travel | Saline inland wader, long-necked geometry and mud nest | Latest official Global NT/date confirmed, names and two reference roles viable | Concrete observation; no claim unknown to local people |
| Giant Dragonfly / Petalura gigantea | Large insect with partly terrestrial larval life | Australian peat swamp, six-legged aerial body | NSW official endangered listing found; global date/name route not completed because not selected | No universal obscurity claim |
| Elephant Beetle / Megasoma elephas | Hairy massive beetle and male horns | Neotropical terrestrial insect; adds group contrast | Taxon/visual leads available; official global route not locked, no invented NE | No claim of local ignorance |

Selected Lesser Flamingo for the strongest settled combination of recognizable geometry, inverted-feeding discovery and night movement. No quota/cooldown; selected topic preserved through reference-fetch friction. Two hook drafts: inverted bill as a sieve (selected); night travel between lakes (not selected for main).
Full-history rg searched all package files, INDEX, automation memory and memory registry under Phoeniconaias minor, Phoenicopterus minor/parvus/rubidus/blythi, Phcenicopterus parvus/rubidus, Lesser Flamingo, コフラミンゴ and lesser-flamingo. Only yesterday's unselected candidate and its automation recap matched; no completed, retired or unfinished collision. Historical spellings from digitized ornithology/Avibase context screened conservatively rather than asserted as a modern accepted synonym list. Generic flamingo is not a species alias gate.

## Evidence Lock
- Accepted scientific name: Phoeniconaias minor (É. Geoffroy Saint-Hilaire, 1798). BirdLife/IOC and official IUCN agree; historical combination Phoenicopterus minor retained for duplicate screening.
- English: Lesser Flamingo. Japanese: コフラミンゴ, Tokyo Zoological Park Society explicitly distinguishes it from Greater Flamingo; JICA exact-taxon figure captions pair the Japanese and scientific names.
- Editorial classification group: Birds.
- Exact lineage: Animalia > Chordata > Aves > Phoenicopteriformes > Phoenicopteridae > Phoeniconaias > Phoeniconaias minor.
- Broad native region: Africa and South Asia, notably East African Rift lakes; scene is a qualitative East African saline-alkaline lake margin.
- IUCN check: record T22697369A129912906; Global Near Threatened (NT), A2c+3c+4c ver 3.1; assessed 7 August 2018, published 2018. Direct rendered fields recorded in evidence/iucn-browser-fields-2026-10-10.md. Old 2016 record, 2024 contextual table and 2025 regional VU excluded from footer. No legal, population or ranked-threat claim.
- Doorway: a familiar flamingo turns its bill upside down to collect near-surface microscopic food.

## Claim check / three cards
| Claim | Verdict | Source | Illustration |
|---|---|---|---|
| Upside-down head/bill filters tiny algae and other food near surface | accurate | BirdLife South Africa Ecology; FSG Diet and Foraging; exact feeding photo | Intact head attached to continuous neck at water surface; no internal anatomy |
| Often changes wetlands at night as local conditions change | accurate | BirdLife South Africa Distribution; FSG Movement | Small complete flying birds over qualitative wetlands under moon |
| Raised mud nest, usually one egg | accurate with usual qualifier | BirdLife South Africa Ecology nest turrets/clutch; FSG Breeding | Low truncated mud mound with shallow top bowl and one egg |
| Global NT with 2018 assessment year | accurate, dated | Direct official latest IUCN fields | Quiet bilingual footer |

## Compact visual identity brief
Individual/stage: adult, sex unspecified; no juvenile shown. Adult shade varies; sexes similar, male larger, juvenile grey-brown, but no size/sex inference.
Biological references: references/fsg-standing-neil-jones.webp (Neil Jones, FSG species gallery) for head/eye/bill, neck/body/legs/feet; references/fsg-feeding-anissa-camp.webp (Anissa Camp, FSG exact Lesser feeding gallery) for intact inverted head orientation and continuous low neck. Two role-distinct images, downloaded once and reused. Captive bands and background excluded.
Diagnostic features:
1. Standing head region: dark facial skin around warm red-orange eye joins predominantly maroon-black, deeply bent thick bill. Distinguish Greater's pale pink basal bill and Andean/James's yellow zones.
2. Standing torso: oval pale-pink body with folded deeper pink/red coverts; black flight feathers may naturally hide under coverts; no forced black triangle.
3. Both photos: long slender pink neck connects at chest; feeding view bends naturally downward with head inverted at surface, never severed or twisted into a hole.
4. Standing lower body: two pink-red legs attach beneath torso, long lower segments and webbed feet. Water and perspective may hide far toes; no forced toe count or extra leg.
5. Flight study: FSG/BirdLife flight descriptions and gallery establish extended neck, trailing legs, pink coverts/black remiges. Qualitative small schematic, no exact feather/digit count.
Natural pose: standing lateral three-quarter adult; two legs can overlap and submerged feet can hide. Feeding study context crop is a separate observational detail, not a detached head. Bill remains closed/near-closed; no anatomy exposed, so hidden-aperture mechanism rule is not triggered.
False silhouettes: Greater Flamingo pale basal bill; yellow-legged/yellow-billed Andean forms; orange-red American Flamingo. Do not substitute these.
Uncertainty: reference colours vary by light/plumage; illustration uses pale rose adult plus dark bill. No individual identity, sex, exact size or fixed night schedule claimed. Nest not drawn as a volcano or twig basket.

## Sources
- [Official IUCN latest Global assessment](https://www.iucnredlist.org/species/22697369/129912906), BirdLife International 2018, date fields directly reviewed 2026-10-10.
- [BirdLife South Africa exact-taxon account](https://www.birdlife.org.za/red-data-book/red-list/lesser-flamingo/), 2025 regional account: names, morphology, filtering, night movement, mud nest and usual clutch. Regional VU kept distinct.
- [IUCN SSC Flamingo Specialist Group species descriptions](https://flamingospecialistgroup.org/education/species-description/), Lesser section based on Cornell 2020 account; biological gallery and independent diet/movement support.
- [Tokyo Zoological Park Society name usage](https://www.tokyo-zoo.net/topics/news/tama/3417_24618_2018-01-05.html), 2018; distinct Japanese name.
- [JICA exact-taxon bilingual figure caption](https://openjicareport.jica.go.jp/pdf/1000046125_01.pdf), figure 2-31/2-32, corroborating name only, not global status.
- [Historical original ornithology](https://upload.wikimedia.org/wikipedia/commons/0/09/Ornithologie_Nordost-Afrika%27s_-_der_Nilquellen-_und_K%C3%BCsten_Gebiete_des_Rothen_Meeres_und_des_n%C3%B6rdlichen_Somal-Landes_%28IA_ornithologienord22heug%29.pdf), p.1272, historical names for conservative duplicate search only.
Real reference media URLs: https://i0.wp.com/flamingospecialistgroup.org/wp-content/uploads/2024/09/Lesser-Neil-Jones-scaled.jpg?w=1708&ssl=1 and https://i0.wp.com/flamingospecialistgroup.org/wp-content/uploads/2024/09/zoo-lesser-3-AC-e1725477839523.jpg?w=823&ssl=1. Local browser saves are WEBP. Research reference photographs are not embedded as public poster photography.

## Acceptance record
Pending generation and separate biological, text, style, full-size and phone-size judgment. Mechanical success alone does not certify species identity. No explicit user artwork adoption claimed.
''')

posts = {
'ja': ['逆さのくちばしが、水面の小さな餌をこす。\nコフラミンゴ\nPhoeniconaias minor\n\nIUCN Red List 2018: 準絶滅危惧 (NT)\n#世界の知らない生き物 #LesserFlamingo', '塩湖の浅瀬で、長い首を下ろし、くちばしを逆さにする。水面近くの微小な藻類などが食事になる。湖の条件が変われば、夜に別の湿地へ。ピンクの姿を追うと、ひとつの湖だけでは終わらない。\n\nそれがコフラミンゴの、ちょっと不思議な暮らし。', '縦長2:3のクレヨンとオイルパステルの観察ポスター。塩湖の浅瀬に立つ淡いピンクのコフラミンゴを大きく描く。長い首、暗い曲がったくちばし、赤みのある目、細長いピンクの脚。三枚の番号つきカードが、頭を逆さにした水面での採餌、月の下の湿地間移動、泥を盛った巣の一個の卵を小さな絵と説明で紹介する。上に和名と学名Phoeniconaias minor、下に2018年IUCN世界評価の準絶滅危惧NT表示。餌と移動の絵は模式的。', '出典メモ：IUCN世界NTは2018年8月7日評価。南部アフリカの2025年地域VUとは別。生態はBirdLife South Africa。\nhttps://www.iucnredlist.org/species/22697369/129912906\nhttps://www.birdlife.org.za/red-data-book/red-list/lesser-flamingo/'],
'en': ['An upside-down bill becomes a sieve for tiny food near the surface.\nLesser Flamingo\nPhoeniconaias minor\n\nIUCN Red List 2018: Near Threatened (NT)\n#LesserFlamingo', 'At a salt lake, a pink neck bends down and a dark bill turns upside down to filter tiny food. When local conditions change, the birds often travel to another wetland after dark. Their story stretches beyond a single lake.', 'Vertical 2:3 crayon and oil-pastel observation poster. A pale pink adult Lesser Flamingo stands in a shallow salt lake, with a long neck, deeply bent dark bill, warm reddish eye and slender pink legs. Three numbered illustrated cards explain upside-down surface feeding, night movement between wetlands, and one egg in a raised mud nest. The title and Phoeniconaias minor appear above, with the 2018 global IUCN Near Threatened NT footer below. Food and travel are schematic.', 'Source note: Global IUCN NT assessed 7 Aug 2018; separate from southern Africa regional VU in 2025. Biology: BirdLife South Africa.\nhttps://www.iucnredlist.org/species/22697369/129912906\nhttps://www.birdlife.org.za/red-data-book/red-list/lesser-flamingo/']
}
for lang, blocks in posts.items():
    language = 'japanese' if lang=='ja' else 'english'
    text = f'# X posting set — {lang}\n\n添付画像: images/lesser_flamingo_{language}_posting_2026-10-10.png\n'
    for section, block in zip(['Main post', 'Story reply', 'ALT text', 'Source/context reply'], blocks):
        text += f'\n## {section}\n\n```text\n{block}\n```\n'
    write(f'x-post-{lang}.md', text)

readme = '''# Lesser Flamingo / コフラミンゴ
State: `in progress`
Workflow mode: Quality Run
Editorial classification group: Birds
Broad native region: Africa and South Asia; East African saline-alkaline lake scene.

## Posting sets
- [日本語の投稿セット](x-post-ja.md)
- [English posting set](x-post-en.md)
Each main post attaches its own language's one poster; companion language is separately available. Local production only; GitHub and X publication are separate.

## Selected poster files
'''
for language, label in [('japanese','Japanese'),('english','English')]:
    for role in ['posting','imagegen']:
        readme += f'- [{label} {role} PNG](images/lesser_flamingo_{language}_{role}_2026-10-10.png)\n'
readme += '\nActual prompt paths: [Japanese](image-prompt-ja.md), [English](image-prompt-en.md). Built-in Image Gen.\nReferences: [standing adult](references/fsg-standing-neil-jones.webp), [feeding posture](references/fsg-feeding-anissa-camp.webp). Existing purple-frog benchmark controls style only.\nEvidence: [Sources QA](sources-qa.md), [official fields](evidence/iucn-browser-fields-2026-10-10.md).\n\n## Copy-ready backups\n'
for language,label in [('japanese','Japanese'),('english','English')]:
    readme += label + ': ' + ', '.join(f'[{role}](images/lesser_flamingo_{language}_posting_2026-10-10.{role}.txt)' for role in ['caption','story-reply','alt','source-note']) + '.\n'
readme += '\n## Acceptance and QA\nPending final source/visual/package review. Exact dated Global NT footer; separate 2025 regional VU not substituted. Usual single egg and often-night movement, no fixed schedule or exact food/feather/toe count. Natural leg/foot occlusion allowed. No internal feeding anatomy invented.\n'
write('README.md', readme)
