from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).parent
IMAGES = ROOT / "images"
IMAGES.mkdir(exist_ok=True)
W, H = 1200, 1500


def font(size, bold=False, serif=False):
    if serif:
        candidates = [Path(r"C:\Windows\Fonts\georgiai.ttf")]
    elif bold:
        candidates = [
            Path(r"C:\Windows\Fonts\meiryob.ttc"),
            Path(r"C:\Windows\Fonts\YuGothB.ttc"),
            Path(r"C:\Windows\Fonts\arialbd.ttf"),
        ]
    else:
        candidates = [
            Path(r"C:\Windows\Fonts\meiryo.ttc"),
            Path(r"C:\Windows\Fonts\YuGothR.ttc"),
            Path(r"C:\Windows\Fonts\arial.ttf"),
        ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def centered(draw, y, text, face, fill):
    box = draw.textbbox((0, 0), text, font=face)
    draw.text(((W - (box[2] - box[0])) / 2, y), text, font=face, fill=fill)


def draw_art(draw):
    draw.ellipse((120, 285, 1080, 1040), fill="#dce6df", outline="#65756c", width=4)
    draw.polygon([(120, 850), (330, 610), (500, 790), (700, 560), (1080, 850)],
                 fill="#c99767")
    draw.polygon([(120, 900), (360, 705), (510, 850), (740, 670), (1080, 910)],
                 fill="#e6bf82")
    for x, y, r in [(235, 900, 38), (920, 920, 45), (310, 970, 28), (845, 990, 32)]:
        draw.ellipse((x-r, y-r, x+r, y+r), fill="#856d55")

    cx, cy = 600, 890
    for angle in range(0, 360, 12):
        import math
        rad = math.radians(angle)
        length = 250 if angle % 24 else 285
        x2 = cx + math.cos(rad) * length
        y2 = cy + math.sin(rad) * length * 0.44
        draw.line((cx, cy, x2, y2), fill="#71826f", width=18)
        draw.line((cx, cy, x2, y2), fill="#9baa8e", width=8)

    draw.line((600, 895, 600, 380), fill="#647459", width=42)
    for y in range(410, 780, 34):
        spread = 82 - int((780-y) * 0.06)
        draw.line((600, y, 600-spread, y+16), fill="#78866b", width=10)
        draw.line((600, y, 600+spread, y+16), fill="#78866b", width=10)
        for x in (600-spread, 600+spread):
            draw.ellipse((x-13, y+3, x+13, y+29), fill="#e9ead0", outline="#68725d")
    draw.ellipse((580, 348, 620, 400), fill="#dfe5c5", outline="#68725d")


def label(draw, box, lines):
    draw.rounded_rectangle(box, radius=18, fill="#fff7e7", outline="#69735d", width=4)
    face = font(27 if max(map(len, lines)) > 20 else 31, bold=True)
    x0, y0, x1, y1 = box
    line_h = 42
    y = y0 + ((y1-y0) - line_h*len(lines)) / 2
    for line in lines:
        width = draw.textbbox((0, 0), line, font=face)[2]
        draw.text(((x0+x1-width)/2, y), line, font=face, fill="#334136")
        y += line_h


def render_png(language, title, labels, output):
    canvas = Image.new("RGB", (W, H), "#e9dec7")
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle((38, 38, 1162, 1462), radius=28, fill="#fffaf0",
                           outline="#56614f", width=5)
    centered(draw, 76, title, font(66 if language == "ja" else 70, bold=True), "#365345")
    centered(draw, 164, "Puya raimondii", font(40, serif=True), "#5b4a3d")
    draw_art(draw)
    boxes = [(70, 1080, 410, 1245), (430, 1080, 770, 1245), (790, 1080, 1130, 1245)]
    for box, lines in zip(boxes, labels):
        label(draw, box, lines)
    draw.rounded_rectangle((140, 1325, 1060, 1412), radius=17, fill="#d8dfcb")
    centered(draw, 1346, "IUCN Red List 2009: Endangered (EN)",
             font(34, bold=True), "#334a3d")
    canvas.save(output, format="PNG", optimize=True)


def svg_lines(x, center_y, lines):
    line_h = 42
    start = center_y - ((len(lines)-1)*line_h/2)
    return "".join(
        f'<tspan x="{x}" y="{start+i*line_h}">{escape(line)}</tspan>'
        for i, line in enumerate(lines)
    )


def render_svg(language, title, labels, output):
    label_nodes = []
    for x, lines in zip((70, 430, 790), labels):
        size = 27 if max(map(len, lines)) > 20 else 31
        label_nodes.append(
            f'<rect x="{x}" y="1080" width="340" height="165" rx="18" '
            'fill="#fff7e7" stroke="#69735d" stroke-width="4"/>'
            f'<text x="{x+170}" y="1162" text-anchor="middle" '
            f'font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="{size}" '
            f'font-weight="700" fill="#334136">{svg_lines(x+170, 1162, lines)}</text>'
        )
    leaf_nodes = []
    import math
    for angle in range(0, 360, 12):
        rad = math.radians(angle)
        length = 250 if angle % 24 else 285
        x2 = 600 + math.cos(rad)*length
        y2 = 890 + math.sin(rad)*length*0.44
        leaf_nodes.append(
            f'<line x1="600" y1="890" x2="{x2:.1f}" y2="{y2:.1f}" '
            'stroke="#71826f" stroke-width="18" stroke-linecap="round"/>'
        )
    flowers = []
    for y in range(410, 780, 34):
        spread = 82 - int((780-y)*0.06)
        for x in (600-spread, 600+spread):
            flowers.append(
                f'<ellipse cx="{x}" cy="{y+16}" rx="13" ry="13" '
                'fill="#e9ead0" stroke="#68725d" stroke-width="2"/>'
            )
    title_size = 66 if language == "ja" else 70
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1500" viewBox="0 0 1200 1500">
  <rect width="1200" height="1500" fill="#e9dec7"/>
  <rect x="38" y="38" width="1124" height="1424" rx="28" fill="#fffaf0" stroke="#56614f" stroke-width="5"/>
  <text x="600" y="140" text-anchor="middle" font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="{title_size}" font-weight="700" fill="#365345">{escape(title)}</text>
  <text x="600" y="215" text-anchor="middle" font-family="Georgia, serif" font-size="40" font-style="italic" fill="#5b4a3d">Puya raimondii</text>
  <ellipse cx="600" cy="660" rx="480" ry="378" fill="#dce6df" stroke="#65756c" stroke-width="4"/>
  <path d="M120 850 L330 610 L500 790 L700 560 L1080 850 V1010 H120 Z" fill="#c99767"/>
  <path d="M120 900 L360 705 L510 850 L740 670 L1080 910 V1010 H120 Z" fill="#e6bf82"/>
  {''.join(leaf_nodes)}
  <line x1="600" y1="895" x2="600" y2="380" stroke="#647459" stroke-width="42" stroke-linecap="round"/>
  {''.join(flowers)}
  <ellipse cx="600" cy="374" rx="20" ry="26" fill="#dfe5c5" stroke="#68725d" stroke-width="2"/>
  {''.join(label_nodes)}
  <rect x="140" y="1325" width="920" height="87" rx="17" fill="#d8dfcb"/>
  <text x="600" y="1380" text-anchor="middle" font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="34" font-weight="700" fill="#334a3d">IUCN Red List 2009: Endangered (EN)</text>
</svg>
'''
    output.write_text(svg, encoding="utf-8")


ja_labels = [
    ["高アンデスの", "岩地に育つ"],
    ["刺の葉が巨大な", "ロゼットに"],
    ["一度の開花後", "親株は枯れる"],
]
en_labels = [
    ["Rocky high Andes"],
    ["A giant rosette", "of spiny leaves"],
    ["One flowering,", "then the parent dies"],
]

render_png("ja", "プヤ・ライモンディ", ja_labels,
           IMAGES / "puya_raimondii_japanese_textsafe_2026-06-12.png")
render_png("en", "Queen of the Andes", en_labels,
           IMAGES / "puya_raimondii_english_textsafe_2026-06-12.png")
render_svg("ja", "プヤ・ライモンディ", ja_labels,
           IMAGES / "puya_raimondii_japanese_textsafe_2026-06-12.svg")
render_svg("en", "Queen of the Andes", en_labels,
           IMAGES / "puya_raimondii_english_textsafe_2026-06-12.svg")
