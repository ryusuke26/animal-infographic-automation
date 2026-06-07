# Historical renderer for the rejected first-pass deterministic drafts.
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).parent
IMAGES = ROOT / "images"
BASE = IMAGES / "honduran_white_bat_base_imagegen_2026-06-07.png"
W, H = 1200, 1500


def font(size, bold=False, serif=False):
    candidates = []
    if serif:
        candidates.append(Path(r"C:\Windows\Fonts\georgiai.ttf"))
    elif bold:
        candidates.extend([
            Path(r"C:\Windows\Fonts\meiryob.ttc"),
            Path(r"C:\Windows\Fonts\YuGothB.ttc"),
        ])
    else:
        candidates.extend([
            Path(r"C:\Windows\Fonts\meiryo.ttc"),
            Path(r"C:\Windows\Fonts\YuGothR.ttc"),
        ])
    candidates.append(Path(r"C:\Windows\Fonts\arial.ttf"))
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def cover_crop(image, size):
    target_w, target_h = size
    scale = max(target_w / image.width, target_h / image.height)
    resized = image.resize(
        (round(image.width * scale), round(image.height * scale)),
        Image.Resampling.LANCZOS,
    )
    left = (resized.width - target_w) // 2
    top = (resized.height - target_h) // 2
    return resized.crop((left, top, left + target_w, top + target_h))


def centered(draw, xy, text, face, fill):
    x, y = xy
    box = draw.textbbox((0, 0), text, font=face)
    draw.text((x - (box[2] - box[0]) / 2, y), text, font=face, fill=fill)


def label(draw, box, lines):
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=20, fill="#fff5da", outline="#6e7650", width=4)
    face = font(34, bold=True)
    total = len(lines) * 43
    y = y0 + ((y1 - y0) - total) / 2
    for line in lines:
        centered(draw, ((x0 + x1) / 2, y), line, face, "#2f392a")
        y += 43


def render_png(language, title, labels, output):
    canvas = Image.new("RGB", (W, H), "#f3e7cc")
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle((42, 42, 1158, 1458), radius=30, fill="#fff9e9", outline="#4b5038", width=5)

    title_size = 70 if language == "ja" else 72
    centered(draw, (600, 82), title, font(title_size, bold=True), "#263b31")
    centered(draw, (600, 172), "Ectophylla alba", font(42, serif=True), "#4b5038")

    art = cover_crop(Image.open(BASE).convert("RGB"), (1040, 790))
    mask = Image.new("L", art.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, art.width, art.height), radius=24, fill=255)
    canvas.paste(art, (80, 245), mask)
    draw.rounded_rectangle((80, 245, 1120, 1035), radius=24, outline="#526b52", width=5)

    boxes = [(75, 1080, 425, 1260), (425, 1080, 775, 1260), (775, 1080, 1125, 1260)]
    for box, lines in zip(boxes, labels):
        label(draw, box, lines)

    draw.rounded_rectangle((150, 1320, 1050, 1410), radius=18, fill="#dce6cf")
    centered(
        draw,
        (600, 1341),
        "IUCN Red List 2015: Near Threatened (NT)",
        font(35, bold=True),
        "#304c3d",
    )
    canvas.save(output, format="PNG", optimize=True)


def multiline_svg(x, y, lines, size=34):
    tspans = []
    start = y - ((len(lines) - 1) * 22)
    for index, line in enumerate(lines):
        tspans.append(
            f'<tspan x="{x}" y="{start + index * 44}">{escape(line)}</tspan>'
        )
    return "".join(tspans)


def render_svg(language, title, labels, output):
    title_size = 70 if language == "ja" else 72
    boxes = [(75, 1080, 350, 180), (425, 1080, 350, 180), (775, 1080, 350, 180)]
    label_nodes = []
    for (x, y, width, height), lines in zip(boxes, labels):
        label_nodes.append(
            f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="20" '
            'fill="#fff5da" stroke="#6e7650" stroke-width="4"/>'
            f'<text x="{x + width / 2}" y="{y + height / 2}" text-anchor="middle" '
            'font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="34" '
            f'font-weight="700" fill="#2f392a">{multiline_svg(x + width / 2, y + height / 2, lines)}</text>'
        )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="1500" viewBox="0 0 1200 1500">
  <defs>
    <clipPath id="artClip"><rect x="80" y="245" width="1040" height="790" rx="24"/></clipPath>
  </defs>
  <rect width="1200" height="1500" fill="#f3e7cc"/>
  <rect x="42" y="42" width="1116" height="1416" rx="30" fill="#fff9e9" stroke="#4b5038" stroke-width="5"/>
  <text x="600" y="145" text-anchor="middle" font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="{title_size}" font-weight="700" fill="#263b31">{escape(title)}</text>
  <text x="600" y="212" text-anchor="middle" font-family="Georgia, serif" font-size="42" font-style="italic" fill="#4b5038">Ectophylla alba</text>
  <image x="80" y="245" width="1040" height="790" preserveAspectRatio="xMidYMid slice" clip-path="url(#artClip)" xlink:href="honduran_white_bat_base_imagegen_2026-06-07.png"/>
  <rect x="80" y="245" width="1040" height="790" rx="24" fill="none" stroke="#526b52" stroke-width="5"/>
  {''.join(label_nodes)}
  <rect x="150" y="1320" width="900" height="90" rx="18" fill="#dce6cf"/>
  <text x="600" y="1376" text-anchor="middle" font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="35" font-weight="700" fill="#304c3d">IUCN Red List 2015: Near Threatened (NT)</text>
</svg>
'''
    output.write_text(svg, encoding="utf-8")


ja_labels = [
    ["葉をかじって", "テントをつくる"],
    ["白い毛と", "黄色い耳・鼻"],
    ["中米の低地林で", "昼休み"],
]
en_labels = [
    ["Cuts leaves into", "roost tents"],
    ["White fur,", "yellow ears", "and nose"],
    ["Day-rests in", "lowland forest"],
]

render_png(
    "ja",
    "シロヘラコウモリ",
    ja_labels,
    IMAGES / "honduran_white_bat_japanese_poster_2026-06-07.png",
)
render_png(
    "en",
    "Honduran White Bat",
    en_labels,
    IMAGES / "honduran_white_bat_english_poster_2026-06-07.png",
)
render_svg(
    "ja",
    "シロヘラコウモリ",
    ja_labels,
    IMAGES / "honduran_white_bat_japanese_poster_2026-06-07.svg",
)
render_svg(
    "en",
    "Honduran White Bat",
    en_labels,
    IMAGES / "honduran_white_bat_english_poster_2026-06-07.svg",
)
