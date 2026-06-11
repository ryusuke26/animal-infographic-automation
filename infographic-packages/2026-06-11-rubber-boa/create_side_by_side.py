from pathlib import Path

from PIL import Image


ROOT = Path(__file__).parent
IMAGES = ROOT / "images"
JA = IMAGES / "rubber_boa_japanese_imagegen_corrected_v4_2026-06-11.png"
EN = IMAGES / "rubber_boa_english_imagegen_candidate_v3_2026-06-11.png"
OUTPUT = IMAGES / "rubber_boa_bilingual_side_by_side_review_2026-06-11.png"


ja = Image.open(JA).convert("RGB")
en = Image.open(EN).convert("RGB")
scale = 0.58
size = (round(ja.width * scale), round(ja.height * scale))
ja = ja.resize(size, Image.Resampling.LANCZOS)
en = en.resize(size, Image.Resampling.LANCZOS)

gap = 16
canvas = Image.new("RGB", (size[0] * 2 + gap, size[1]), "#ffffff")
canvas.paste(ja, (0, 0))
canvas.paste(en, (size[0] + gap, 0))
canvas.save(OUTPUT, format="PNG", optimize=True)
