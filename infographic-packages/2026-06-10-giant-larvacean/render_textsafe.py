from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).parent
IMAGES = ROOT / "images"
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
    draw.ellipse((135, 285, 1065, 1050), fill="#173c64", outline="#8cc4cc", width=4)
    for x, y, r in [(220, 390, 5), (940, 430, 4), (315, 850, 4), (865, 920, 6)]:
        draw.ellipse((x - r, y - r, x + r, y + r), fill="#d8ecdc")

    draw.ellipse((285, 390, 705, 860), fill="#8dd4d240", outline="#bce5de", width=8)
    draw.ellipse((500, 390, 920, 860), fill="#8dd4d240", outline="#bce5de", width=8)
    draw.ellipse((440, 475, 760, 790), fill="#c9eef050", outline="#d8f3ed", width=6)
    for offset in (0, 55, 110):
        draw.arc((360 + offset, 450, 815 - offset, 825), 200, 340, fill="#9ed9d4", width=3)
        draw.arc((360 + offset, 450, 815 - offset, 825), 20, 160, fill="#9ed9d4", width=3)

    draw.ellipse((545, 565, 660, 690), fill="#dcefcf", outline="#eff8e8", width=4)
    draw.arc((580, 595, 805, 865), 85, 270, fill="#e8f4d8", width=32)

    for y in (515, 585, 655, 725):
        draw.line((185, y, 405, y + 35), fill="#a8d6ce", width=4)
        draw.polygon([(405, y + 35), (388, y + 22), (391, y + 45)], fill="#a8d6ce")

    draw.ellipse((490, 880, 710, 1010), fill="#8bbfbd50", outline="#bce5de", width=5)
    draw.line((600, 1010, 600, 1065), fill="#bce5de", width=5)
    draw.polygon([(600, 1080), (585, 1055), (615, 1055)], fill="#bce5de")


def label(draw, box, lines):
    draw.rounded_rectangle(box, radius=18, fill="#f7edcf", outline="#74a9a4", width=4)
    longest = max(map(len, lines))
    face = font(24 if longest > 28 else 29, bold=True)
    x0, y0, x1, y1 = box
    line_h = 39
    y = y0 + ((y1 - y0) - line_h * len(lines)) / 2
    for line in lines:
        width = draw.textbbox((0, 0), line, font=face)[2]
        draw.text(((x0 + x1 - width) / 2, y), line, font=face, fill="#183f55")
        y += line_h


def render_png(language, title, labels, output):
    canvas = Image.new("RGB", (W, H), "#eee2bf")
    draw = ImageDraw.Draw(canvas, "RGBA")
    draw.rounded_rectangle((38, 38, 1162, 1462), radius=28, fill="#fff9e8", outline="#2b6670", width=5)
    centered(draw, 76, title, font(54 if language == "ja" else 68, bold=True), "#173f5c")
    centered(draw, 160, "Bathochordaeus stygius", font(38, serif=True), "#3f6472")
    draw_art(draw)
    boxes = [(65, 1090, 405, 1250), (430, 1090, 770, 1250), (795, 1090, 1135, 1250)]
    for box, lines in zip(boxes, labels):
        label(draw, box, lines)
    draw.rounded_rectangle((75, 1325, 1125, 1415), radius=17, fill="#d2e6de")
    centered(
        draw,
        1353,
        "IUCN Red List: No species assessment located (checked 2026)",
        font(25, bold=True),
        "#173f4e",
    )
    canvas.save(output, format="PNG", optimize=True)


def svg_tspans(x, center_y, lines, line_h=39):
    start = center_y - ((len(lines) - 1) * line_h / 2)
    return "".join(
        f'<tspan x="{x}" y="{start + i * line_h}">{escape(line)}</tspan>'
        for i, line in enumerate(lines)
    )


def render_svg(language, title, labels, output):
    label_nodes = []
    for x, lines in zip((65, 430, 795), labels):
        size = 24 if max(map(len, lines)) > 28 else 29
        label_nodes.append(
            f'<rect x="{x}" y="1090" width="340" height="160" rx="18" fill="#f7edcf" '
            'stroke="#74a9a4" stroke-width="4"/>'
            f'<text x="{x + 170}" y="1170" text-anchor="middle" '
            f'font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="{size}" '
            f'font-weight="700" fill="#183f55">{svg_tspans(x + 170, 1170, lines)}</text>'
        )
    title_size = 54 if language == "ja" else 68
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1500" viewBox="0 0 1200 1500">
  <rect width="1200" height="1500" fill="#eee2bf"/>
  <rect x="38" y="38" width="1124" height="1424" rx="28" fill="#fff9e8" stroke="#2b6670" stroke-width="5"/>
  <text x="600" y="135" text-anchor="middle" font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="{title_size}" font-weight="700" fill="#173f5c">{escape(title)}</text>
  <text x="600" y="205" text-anchor="middle" font-family="Georgia, serif" font-size="38" font-style="italic" fill="#3f6472">Bathochordaeus stygius</text>
  <ellipse cx="600" cy="667" rx="465" ry="382" fill="#173c64" stroke="#8cc4cc" stroke-width="4"/>
  <ellipse cx="495" cy="625" rx="210" ry="235" fill="#8dd4d2" fill-opacity="0.24" stroke="#bce5de" stroke-width="8"/>
  <ellipse cx="710" cy="625" rx="210" ry="235" fill="#8dd4d2" fill-opacity="0.24" stroke="#bce5de" stroke-width="8"/>
  <ellipse cx="600" cy="632" rx="160" ry="158" fill="#c9eef0" fill-opacity="0.30" stroke="#d8f3ed" stroke-width="6"/>
  <path d="M405 550 Q600 470 795 550 M405 625 Q600 545 795 625 M405 700 Q600 620 795 700" fill="none" stroke="#9ed9d4" stroke-width="3"/>
  <ellipse cx="602" cy="628" rx="58" ry="63" fill="#dcefcf" stroke="#eff8e8" stroke-width="4"/>
  <path d="M620 665 Q760 710 770 850" fill="none" stroke="#e8f4d8" stroke-width="32" stroke-linecap="round"/>
  <path d="M185 515 L405 550 M185 585 L405 620 M185 655 L405 690 M185 725 L405 760" fill="none" stroke="#a8d6ce" stroke-width="4"/>
  <ellipse cx="600" cy="945" rx="110" ry="65" fill="#8bbfbd" fill-opacity="0.30" stroke="#bce5de" stroke-width="5"/>
  <path d="M600 1010 V1065" stroke="#bce5de" stroke-width="5"/><path d="M600 1080 L585 1055 H615 Z" fill="#bce5de"/>
  {''.join(label_nodes)}
  <rect x="75" y="1325" width="1050" height="90" rx="17" fill="#d2e6de"/>
  <text x="600" y="1380" text-anchor="middle" font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="25" font-weight="700" fill="#173f4e">IUCN Red List: No species assessment located (checked 2026)</text>
</svg>
'''
    output.write_text(svg, encoding="utf-8")


ja_labels = [
    ["深い海をただよう", "尾索動物"],
    ["粘液のハウスで", "微粒子をこす"],
    ["使い終えたハウスは", "深く沈む"],
]
en_labels = [
    ["A pelagic tunicate", "in deep water"],
    ["A mucus house", "filters fine particles"],
    ["Used houses sink", "into the deep"],
]

render_png(
    "ja",
    "ジャイアント・ラーバシアン",
    ja_labels,
    IMAGES / "giant_larvacean_japanese_textsafe_2026-06-10.png",
)
render_png(
    "en",
    "Giant Larvacean",
    en_labels,
    IMAGES / "giant_larvacean_english_textsafe_2026-06-10.png",
)
render_svg(
    "ja",
    "ジャイアント・ラーバシアン",
    ja_labels,
    IMAGES / "giant_larvacean_japanese_textsafe_2026-06-10.svg",
)
render_svg(
    "en",
    "Giant Larvacean",
    en_labels,
    IMAGES / "giant_larvacean_english_textsafe_2026-06-10.svg",
)
