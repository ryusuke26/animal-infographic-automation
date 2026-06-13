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
    draw.rounded_rectangle((105, 285, 1095, 1035), radius=80,
                           fill="#d9e2d5", outline="#667264", width=4)
    draw.polygon([(105, 285), (1095, 285), (1095, 500), (820, 460),
                  (635, 530), (105, 485)], fill="#786452")
    draw.ellipse((725, 405, 925, 525), fill="#875f3f", outline="#4f4035", width=4)
    draw.ellipse((755, 430, 895, 485), fill="#d9e2d5")
    draw.line((120, 900, 1080, 790), fill="#667e59", width=55)
    draw.ellipse((365, 620, 755, 960), fill="#f3efdc", outline="#343a36", width=5)
    draw.ellipse((405, 600, 720, 860), fill="#373d3c")
    draw.polygon([(435, 815), (315, 1010), (425, 985), (555, 825)],
                 fill="#303636")
    draw.ellipse((510, 475, 690, 645), fill="#e7a82a", outline="#343a36", width=5)
    draw.ellipse((555, 505, 665, 610), fill="#171918")
    draw.ellipse((580, 525, 615, 560), fill="#3a2b22")
    draw.polygon([(665, 535), (790, 575), (665, 600)], fill="#1e2526")
    draw.polygon([(510, 570), (465, 685), (565, 680)], fill="#f4efdc")
    for x in (485, 635):
        draw.line((x, 875, x - 12, 1035), fill="#a9b9bc", width=13)
        draw.line((x - 12, 1035, x - 42, 1054), fill="#7b888a", width=7)
        draw.line((x - 12, 1035, x + 20, 1050), fill="#7b888a", width=7)
    for x, y in [(170, 745), (250, 650), (915, 700), (1005, 620)]:
        draw.arc((x, y, x + 120, y + 220), 185, 350, fill="#486544", width=13)


def label(draw, box, lines):
    draw.rounded_rectangle(box, radius=18, fill="#fff7e7",
                           outline="#5f6c59", width=4)
    face = font(27 if max(map(len, lines)) > 24 else 30, bold=True)
    x0, y0, x1, y1 = box
    line_h = 42
    y = y0 + ((y1 - y0) - line_h * len(lines)) / 2
    for line in lines:
        width = draw.textbbox((0, 0), line, font=face)[2]
        draw.text(((x0 + x1 - width) / 2, y), line, font=face, fill="#304535")
        y += line_h


def render_png(language, title, labels, output):
    canvas = Image.new("RGB", (W, H), "#e8dcc6")
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle((38, 38, 1162, 1462), radius=28, fill="#fffaf0",
                           outline="#4e5d4c", width=5)
    size = 62 if language == "ja" else 59
    centered(draw, 75, title, font(size, bold=True), "#294b3b")
    centered(draw, 160, "Picathartes gymnocephalus",
             font(37, serif=True), "#54483e")
    draw_art(draw)
    boxes = [(70, 1080, 410, 1248), (430, 1080, 770, 1248),
             (790, 1080, 1130, 1248)]
    for box, lines in zip(boxes, labels):
        label(draw, box, lines)
    draw.rounded_rectangle((120, 1325, 1080, 1412), radius=17, fill="#d6dfce")
    centered(draw, 1346, "IUCN Red List 2018: Vulnerable (VU)",
             font(34, bold=True), "#30483b")
    canvas.save(output, format="PNG", optimize=True)


def svg_text(x, center_y, lines):
    line_h = 42
    start = center_y - ((len(lines) - 1) * line_h / 2)
    return "".join(
        f'<tspan x="{x}" y="{start + i * line_h}">{escape(line)}</tspan>'
        for i, line in enumerate(lines)
    )


def render_svg(language, title, labels, output):
    labels_svg = []
    for x, lines in zip((70, 430, 790), labels):
        labels_svg.append(
            f'<rect x="{x}" y="1080" width="340" height="168" rx="18" '
            'fill="#fff7e7" stroke="#5f6c59" stroke-width="4"/>'
            f'<text x="{x + 170}" y="1164" text-anchor="middle" '
            'font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="28" '
            f'font-weight="700" fill="#304535">{svg_text(x + 170, 1164, lines)}</text>'
        )
    title_size = 62 if language == "ja" else 59
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1500" viewBox="0 0 1200 1500">
  <rect width="1200" height="1500" fill="#e8dcc6"/>
  <rect x="38" y="38" width="1124" height="1424" rx="28" fill="#fffaf0" stroke="#4e5d4c" stroke-width="5"/>
  <text x="600" y="140" text-anchor="middle" font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="{title_size}" font-weight="700" fill="#294b3b">{escape(title)}</text>
  <text x="600" y="215" text-anchor="middle" font-family="Georgia, serif" font-size="37" font-style="italic" fill="#54483e">Picathartes gymnocephalus</text>
  <rect x="105" y="285" width="990" height="750" rx="80" fill="#d9e2d5" stroke="#667264" stroke-width="4"/>
  <path d="M105 285 H1095 V500 L820 460 L635 530 L105 485 Z" fill="#786452"/>
  <ellipse cx="825" cy="465" rx="100" ry="60" fill="#875f3f" stroke="#4f4035" stroke-width="4"/>
  <ellipse cx="825" cy="458" rx="70" ry="27" fill="#d9e2d5"/>
  <line x1="120" y1="900" x2="1080" y2="790" stroke="#667e59" stroke-width="55"/>
  <ellipse cx="560" cy="790" rx="195" ry="170" fill="#f3efdc" stroke="#343a36" stroke-width="5"/>
  <ellipse cx="562" cy="730" rx="157" ry="130" fill="#373d3c"/>
  <path d="M435 815 L315 1010 L425 985 L555 825 Z" fill="#303636"/>
  <ellipse cx="600" cy="560" rx="90" ry="85" fill="#e7a82a" stroke="#343a36" stroke-width="5"/>
  <ellipse cx="610" cy="557" rx="55" ry="53" fill="#171918"/>
  <circle cx="598" cy="542" r="18" fill="#3a2b22"/>
  <path d="M665 535 L790 575 L665 600 Z" fill="#1e2526"/>
  <path d="M510 570 L465 685 L565 680 Z" fill="#f4efdc"/>
  <path d="M485 875 L473 1035 M635 875 L623 1035" stroke="#a9b9bc" stroke-width="13"/>
  {''.join(labels_svg)}
  <rect x="120" y="1325" width="960" height="87" rx="17" fill="#d6dfce"/>
  <text x="600" y="1380" text-anchor="middle" font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="34" font-weight="700" fill="#30483b">IUCN Red List 2018: Vulnerable (VU)</text>
</svg>
'''
    output.write_text(svg, encoding="utf-8")


ja_labels = [
    ["西アフリカの", "岩の森にすむ"],
    ["黄色い裸の頭と", "長い尾"],
    ["岩陰に泥の", "椀形巣をつくる"],
]
en_labels = [
    ["Rocky forests", "of West Africa"],
    ["A bare yellow head", "and long tail"],
    ["Mud cup nests", "beneath rock"],
]

render_png("ja", "ハゲチメドリ", ja_labels,
           IMAGES / "white_necked_rockfowl_japanese_textsafe_2026-06-13.png")
render_png("en", "White-necked Rockfowl", en_labels,
           IMAGES / "white_necked_rockfowl_english_textsafe_2026-06-13.png")
render_svg("ja", "ハゲチメドリ", ja_labels,
           IMAGES / "white_necked_rockfowl_japanese_textsafe_2026-06-13.svg")
render_svg("en", "White-necked Rockfowl", en_labels,
           IMAGES / "white_necked_rockfowl_english_textsafe_2026-06-13.svg")
