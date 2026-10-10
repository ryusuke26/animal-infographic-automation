"""Historical initial-production helper. Superseded by user-selected revision; do not rerun to overwrite current assets or QA records."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib,json
root=Path.cwd()
p=root/'infographic-packages/2026-10-10-lesser-flamingo'
now=datetime.now(ZoneInfo('Asia/Tokyo')).isoformat(timespec='seconds')
def write(path,text): path.write_text(text.strip()+'\n',encoding='utf-8')
for name in ['README.md','sources-qa.md']:
    f=p/name
    write(f,f.read_text(encoding='utf-8')+f'\nFinal package QA: PASS at {now}; includes direct-source, bilingual X weighted-format, eight-sidecar and whitespace checks.\n')
index=root/'infographic-packages/INDEX.md'
text=index.read_text(encoding='utf-8')
row='| 2026-10-10 | Lesser Flamingo / コフラミンゴ | *Phoeniconaias minor* | `2026-10-10-lesser-flamingo` | completed, local-ready | Region: Africa and South Asia / East African saline-alkaline lake scene. Group: Birds; Phoenicopteriformes > Phoenicopteridae. Direct official latest IUCN T22697369A129912906 confirms Global NT A2c+3c+4c ver 3.1, assessed 7 August 2018/published 2018; field transcription saved, no official PDF claimed. Separate 2025 southern-African regional VU excluded. BirdLife/IOC, Tokyo Zoological Park Society/JICA and FSG real standing/feeding photos support names, dark bent bill, upside-down surface filtering, often-night wetland movement and raised mud nest with usual single egg. Full-history accepted name, historical minor/parvus/rubidus/blythi combinations, JP/EN aliases and slug found candidate-only mentions. JA initial passed dimensions but unclear head inversion; one localized retry corrected posture, entire defining set re-reviewed before EN first-pass acceptance. Selected prompts image-prompt-ja-retry.md / image-prompt-en.md. Four exact 1024x1536 PNGs, pixel-identical language pairs, all nine strings, three numbered illustrated explanations, broken crayon/pastel pigment, natural submerged-foot occlusion, full-size/342x513 phone review, eight offline sidecars and full package QA pass. Food/travel/nest studies qualitative, no exact size/sex/feather/toe count or fixed nightly schedule. No material blocker. Git/GitHub/X untouched. Avoid repeat under Phoeniconaias/Phoenicopterus minor, historical parvus/rubidus/blythi names, Lesser Flamingo, コフラミンゴ or lesser-flamingo. |'
assert row not in text
write(index,text.replace('## Incomplete / Do Not Count As Completed',row+'\n\n## Incomplete / Do Not Count As Completed',1))
write(root/'automation-2-current-state.md',f'''# Automation 2 Current State
Updated: {now}

## Workflow
- Default workflow: Quality Run; Japanese/English posters, exact vertical 2:3, exactly three numbered illustrated explanatory cards.
- Required medium: crayon / oil-pastel observation sketch; generated_infographics/purple_frog_ja_2026-04-28.png benchmark controls texture/warmth only.
- Pending evidence package: none.
- Active package: none.
- Unfinished visual gate: none.
- Latest package: 2026-10-10-lesser-flamingo.
- Latest state: completed, local-ready. Git/GitHub/X untouched; nothing posted or replied.
- Latest evidence: latest official IUCN T22697369A129912906 Global NT A2c+3c+4c ver 3.1, assessed 7 August 2018, published 2018; directly rendered field transcription saved. Separate 2025 southern-African regional VU not substituted; no official PDF claimed.
- Latest visual result: tall pale-pink adult with dark bent bill in saline lake; upside-down surface feeding, night travel and mud-nest egg studies. Japanese one localized feeding-pose retry accepted after full defining-feature review; English first pass accepted.
- Retired duplicate exclusion: 2026-08-21-montseny-brook-newt duplicates completed 2026-06-26-montseny-brook-newt; do not post.

## Latest Completed Package
- Topic: Lesser Flamingo / コフラミンゴ / Phoeniconaias minor. Historical combinations/duplicate aliases screened: Phoenicopterus minor/parvus/rubidus/blythi and Phcenicopterus parvus/rubidus; candidate-only mentions, no package collision.
- Region: Africa and South Asia; qualitative East African saline-alkaline lake margin.
- Editorial classification group: Birds. Exact lineage: Animalia > Chordata > Aves > Phoenicopteriformes > Phoenicopteridae > Phoeniconaias.
- Selected Japanese: images/lesser_flamingo_japanese_imagegen_2026-10-10.png; actual prompt image-prompt-ja-retry.md. Initial source/prompt retained as rejected/historical audit.
- Selected English: images/lesser_flamingo_english_imagegen_2026-10-10.png; actual prompt image-prompt-en.md.
- Four canonical PNGs exact 1024x1536, pixel-identical language pairs; nine strings, three illustrated explanatory cards, reference-based identity/anatomy, crayon/pastel medium, full-size/342x513 phone review, eight synchronized sidecars and package QA pass.
- Natural submerged-foot/far-toe and feeding-eye occlusion allowed. Qualitative microscopic-food/travel/nest studies; adult sex/size/feather/toe counts unspecified, usual egg and often-night qualifiers preserved. No unresolved material caveat.
- Previous 2026-10-09-whale-shark remains completed, published after user-authorized GitHub closeout. Nothing posted to X.

## Recent-Eight Completed Region Summary
1. 2026-10-03 — Southeastern USA / Carolina wet pine savanna — Venus Flytrap
2. 2026-10-04 — Tropical Indo-Pacific / mangrove estuaries — Banded Archerfish
3. 2026-10-05 — Southwestern Africa / Namib arid sand and gravel — Namaqua Chameleon
4. 2026-10-06 — Tropical Indo-Pacific / shallow western-Pacific coral reef — Giant Clam
5. 2026-10-07 — South America / temperate Andean woodland — Monkey Puzzle
6. 2026-10-08 — Europe / British autumn hedgerow — Western European Hedgehog
7. 2026-10-09 — Ocean/Global / Ningaloo warm offshore water — Whale Shark
8. 2026-10-10 — Africa and South Asia / East African inland saline lake — Lesser Flamingo

## Recent-Eight Completed Classification Summary
1. Plants — Venus Flytrap
2. Fishes — Banded Archerfish
3. Reptiles — Namaqua Chameleon
4. Other invertebrates — Giant Clam
5. Plants — Monkey Puzzle
6. Mammals — Western European Hedgehog
7. Fishes — Whale Shark
8. Birds — Lesser Flamingo

Diversity informs selection across and within groups/forms/habitats/discoveries without quotas/cooldowns. Long-legged saline-lake wader adds inverted-bill feeding, aerial night travel and mud-nest architecture; broad filtering theme repeats Whale Shark but form, scale, habitat and connected story differ.

## Daily Quality Loop
- Issue: none unresolved.
- Unresolved carryover: none.

## Next Concrete Change
Recalculate diversity next run; retain assessment-date-aware 2018 footer and accepted artwork. GitHub/X publication remains separate. No policy change.
''')
daily=root/'daily-quality-loop.md'
write(daily,daily.read_text(encoding='utf-8')+f'''\n\n## 2026-10-10 — Lesser Flamingo Quality Run
- Completed, local-ready; latest official Global NT assessed 7 August 2018, distinct from 2025 regional VU. Both languages/three cards/nine strings/crayon medium/full-size/342x513 phones and full package checks passed. Git/GitHub/X untouched.
- One concrete learning: an eye shown above a downward bill can make a lowered feeding head read upright; use the real surface-feeding orientation and permit natural eye occlusion. One localized JA retry corrected this; full defining-set review passed. EN first pass accepted. No added policy gate or unresolved carryover.
- Current run time: {now}.
''')
memory=Path(r'C:\Users\ryusu\.codex\automations\automation-2\memory.md')
previous=memory.read_text(encoding='utf-8') if memory.exists() else ''
write(memory,previous+f'''\n\n## {now} — Lesser Flamingo Quality Run completed
- Completed 2026-10-10-lesser-flamingo / Lesser Flamingo / コフラミンゴ / Phoeniconaias minor as completed, local-ready. Birds; Africa and South Asia / East African saline-alkaline lake scene.
- Varied slate compared Giant Dragonfly and Elephant Beetle; latest eight/twenty scan favored inland long-legged wader, inverted bill, night wetland movement and mud nest. Full-history accepted/historical scientific combinations, bilingual aliases and slug found candidate-only mentions, no collision.
- Followed old 2016 IUCN record's latest Global link: directly rendered T22697369A129912906 NT A2c+3c+4c ver 3.1, assessed 7 August 2018, published 2018. Field transcription saved; no PDF claimed. 2025 southern-African regional VU and 2024 contextual table year excluded from global footer. BirdLife/IOC and Tokyo Zoo/JICA support names; FSG two exact-taxon standing/feeding photos reused.
- JA initial source passed dimensions but inverted feeding head read ambiguously upright. One localized Image Gen edit accepted, actual prompt image-prompt-ja-retry.md; entire defining set and full/phone review completed before EN. EN first pass accepted, actual image-prompt-en.md. Initial JA source retained in audit.
- Four exact 1024x1536 PNGs, pixel-identical language pairs, nine strings, three illustrated numbered explanations, visible crayon/pastel marks, natural submerged-foot/feeding-eye occlusion, 342x513 phone reviews, eight offline sidecars and pre-image/immediate-source/full package QA passed. No installs. No exact size/sex/feather/toe count or fixed night schedule, usual single-egg wording. No material blocker.
- README, INDEX, current state and daily loop synchronized. Git/GitHub/X untouched; prior Whale Shark stays published. One learning: real inverted-head orientation with natural eye occlusion reads more accurately than forcing a visible eye. No new gate, policy change or unresolved carryover. Reference download took about ten minutes, then succeeded.
- Current run time: {now}.
''')
f=p/'audit/acceptance.json'
data=json.loads(f.read_text(encoding='utf-8'))
data['final_package_qa']='PASS'
data['closed_at']=now
data['assets']={str(x.relative_to(p)):hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(p.rglob('*')) if x.is_file() and x.name!='acceptance.json'}
write(f,json.dumps(data,ensure_ascii=False,indent=2))
print(now)
