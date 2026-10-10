"""Historical initial-production helper. Superseded by user-selected revision; do not rerun to overwrite current assets or QA records."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from PIL import Image, ImageChops
import hashlib, json

root=Path.cwd()
p=root/'infographic-packages/2026-10-10-lesser-flamingo'
now=datetime.now(ZoneInfo('Asia/Tokyo')).isoformat(timespec='seconds')
def write(path,text): path.write_text(text.strip()+'\n',encoding='utf-8')

qa=p/'sources-qa.md'
text=qa.read_text(encoding='utf-8')
text=text.replace('FSG/BirdLife flight descriptions and gallery establish extended neck, trailing legs, pink coverts/black remiges.', 'Small flight study uses the well-represented flamingo body plan with neck forward/legs trailing; adult bill/body colour is locked to the two exact-taxon photos. Black remiges are depicted qualitatively, with no claim of a photographed individual in flight.')
text=text.replace('Pending generation and separate biological, text, style, full-size and phone-size judgment.', '''Japanese initial full poster passed its immediate 1024x1536 direct-source gate, but the feeding head did not read clearly inverted. Rejected for that localized visual defect; saved audit/lesser_flamingo_japanese_initial_rejected.png and historical image-prompt-ja.md. One eligible localized Image Gen edit used image-prompt-ja-retry.md and the actual feeding photo. Retry passed its immediate source gate. Continuous neck enters at right, the head turns at water level and the bill points left along the surface; natural eye occlusion is retained. Entire defining-feature set re-reviewed after correction: predominantly dark deeply bent bill, eye/face connection, pink oval body/folded coverts, continuous long neck, two coherent legs and shallow-water endpoints. No repeat or additional retry.
Japanese acceptance and 342x513 phone review completed before English generation. English first pass used accepted Japanese composition plus both real references and passed immediate source gate; zero English retries. All nine strings per language were read at full size, including 学名 Phoeniconaias minor, 藻類/湿地/巣, upside-down hyphen, full stops and dated NT footer. Exactly three illustrated numbered explanations with adequate margins; one dominant hero and subordinate distant flock. Night-flight miniatures have coherent paired wings and extended-neck/trailing-leg body plans. Nest is an attached low mud turret with shallow top bowl and one pale egg; incidental drawn surface flecks are not an asserted diagnostic shell pattern.
Style observation: broken blue/sage/ochre crayon strokes with exposed paper run through lake/hills, layered pink-red drawn pigment runs across hero neck/body/legs, and matte rough marks occur in feeding study, flight silhouettes and mud nest. The hero/card art carries drawing texture rather than only the border; warmth and strokes were compared with the purple-frog benchmark. Bill highlights are limited diagnostic accents, not dominant photographic rendering.
Both full-size and saved 342x513 phone previews accepted. Canonical source and posting files all exact 1024x1536; same-language pairs are pixel-identical. No local anatomy/text repair or ratio correction. Illustrative food enlarged qualitatively; surface feeding not exclusive diet, night movement not every-night/only-night claim, usual one-egg wording retained. Adult sex, exact size and toe/feather counts unspecified; far toes naturally submerged. No unresolved material visual or evidence blocker.
Eight UTF-8 sidecars generated with installed offline twitter-text helper; no dependency installation. Pre-image Copy Lock QA passed. Final package validation result recorded below after execution. No explicit user artwork adoption claimed; local-ready is separate from GitHub/X publication.''')
text += f'\n\nFinal visual acceptance recorded: {now}\n'
write(qa,text)

readme=p/'README.md'
text=readme.read_text(encoding='utf-8').replace('State: `in progress`','State: `completed, local-ready`')
text=text.replace('[Japanese](image-prompt-ja.md)', '[Japanese selected localized retry](image-prompt-ja-retry.md); [historical initial](image-prompt-ja.md)')
text=text.replace('Pending final source/visual/package review.', 'Both direct-source gates and separate biological, all-nine-string, three-card, full-size/342x513 phone and crayon/oil-pastel reviews passed. Japanese used one localized feeding-pose retry; English accepted first pass. Four canonical PNGs are exact 1024x1536 and pixel-identical within each language. Eight sidecars synchronized; final package QA recorded below.')
text += f'\nSelected Japanese prompt: image-prompt-ja-retry.md. Selected English prompt: image-prompt-en.md. Initial Japanese source and prompt remain historical audit artifacts.\nFinal local acceptance: {now}. Git/GitHub/X untouched; nothing posted or replied.\n'
write(readme,text)

manifest=[]
for language in ['japanese','english']:
    a=p/f'images/lesser_flamingo_{language}_imagegen_2026-10-10.png'
    b=p/f'images/lesser_flamingo_{language}_posting_2026-10-10.png'
    ia,ib=Image.open(a).convert('RGB'),Image.open(b).convert('RGB')
    assert ia.size==ib.size==(1024,1536)
    same=ImageChops.difference(ia,ib).getbbox() is None
    assert same
    manifest.append({'language':language,'source':str(a.relative_to(p)),'posting':str(b.relative_to(p)),'size':[1024,1536],'pixel_identical':same})
write(p/'audit/acceptance.json',json.dumps({'checked':now,'selected_prompts':{'ja':'image-prompt-ja-retry.md','en':'image-prompt-en.md'},'retries':{'ja':1,'en':0},'pairs':manifest,'assets':{str(f.relative_to(p)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(p.rglob('*')) if f.is_file() and f.name!='acceptance.json'}},ensure_ascii=False,indent=2))
print(now)
print('Four canonical PNGs: exact 1024x1536; both language pairs pixel-identical.')
