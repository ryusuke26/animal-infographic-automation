from pathlib import Path
import random

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).parent
IMAGES = ROOT / "images"
SOURCE = IMAGES / "rubber_boa_english_imagegen_candidate_v3_2026-06-11.png"
OUTPUT = IMAGES / "rubber_boa_japanese_matched_layout_candidate_2026-06-11.png"


def font(size, bold=True):
    candidates = [
        Path(r"C:\Windows\Fonts\meiryob.ttc") if bold else Path(r"C:\Windows\Fonts\meiryo.ttc"),
        Path(r"C:\Windows\Fonts\YuGothB.ttc") if bold else Path(r"C:\Windows\Fonts\YuGothR.ttc"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def fit(draw, text, max_width, start_size):
    size = start_size
    while size > 18:
        face = font(size)
        box = draw.textbbox((0, 0), text, font=face)
        if box[2] - box[0] <= max_width:
            return face
        size -= 2
    return font(size)


def centered(draw, box, lines, start_size, fill):
    x0, y0, x1, y1 = box
    face = fit(draw, max(lines, key=len), x1 - x0 - 24, start_size)
    line_height = int(face.size * 1.35)
    total = line_height * len(lines)
    y = y0 + (y1 - y0 - total) / 2
    for line in lines:
        bounds = draw.textbbox((0, 0), line, font=face)
        width = bounds[2] - bounds[0]
        draw.text(((x0 + x1 - width) / 2, y), line, font=face, fill=fill)
        y += line_height


def textured_patch(image, box, base, radius=10, seed=1):
    x0, y0, x1, y1 = box
    width, height = x1 - x0, y1 - y0
    random.seed(seed)
    patch = Image.new("RGB", (width, height), base)
    pixels = patch.load()
    for y in range(height):
        for x in range(width):
            jitter = random.randint(-5, 5)
            pixels[x, y] = tuple(max(0, min(255, value + jitter)) for value in base)
    mask = Image.new("L", (width, height), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, width - 1, height - 1), radius=radius, fill=255)
    image.paste(patch, (x0, y0), mask)


image = Image.open(SOURCE).convert("RGB")
draw = ImageDraw.Draw(image)

# Replace only the English title while retaining the scientific name and artwork.
textured_patch(image, (115, 42, 910, 202), (248, 237, 207), radius=12, seed=11)
draw = ImageDraw.Draw(image)
for x in range(135, 890, 28):
    draw.line((x, 52, x + 16, 47), fill="#b9c4bd", width=2)
centered(draw, (115, 42, 910, 202), ["ラバーボア"], 78, "#4a2f1e")

# Replace text in the upper parts of the three existing information boxes.
# The lower inset illustrations remain untouched.
textured_patch(image, (52, 1054, 327, 1181), (250, 239, 211), radius=9, seed=21)
textured_patch(image, (354, 1054, 657, 1181), (250, 239, 211), radius=9, seed=22)
textured_patch(image, (690, 1054, 976, 1181), (250, 239, 211), radius=9, seed=23)
draw = ImageDraw.Draw(image)

centered(draw, (52, 1054, 327, 1181), ["岩や倒木の", "下にひそむ"], 36, "#466479")
centered(draw, (354, 1054, 657, 1181), ["つやのある", "小さなボア"], 36, "#55733f")
centered(draw, (690, 1054, 976, 1181), ["丸い尾を", "盾にする"], 36, "#8a552b")

image.save(OUTPUT, format="PNG", optimize=True)
