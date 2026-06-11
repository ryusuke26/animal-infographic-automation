from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).parent
IMAGES = ROOT / "images"
IMAGES.mkdir(exist_ok=True)
W, H = 1200, 1500
FOOTER = "IUCN Red List 2019: Least Concern (LC)"


def font(size, bold=False, serif=False):
    if serif:
        candidates = [Path(r"C:\Windows\Fonts\georgiai.ttf")]
    elif bold:
        candidates = [Path(r"C:\Windows\Fonts\meiryob.ttc"), Path(r"C:\Windows\Fonts\arialbd.ttf")]
    else:
        candidates = [Path(r"C:\Windows\Fonts\meiryo.ttc"), Path(r"C:\Windows\Fonts\arial.ttf")]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def centered(draw, y, text, face, fill):
    box = draw.textbbox((0, 0), text, font=face)
    draw.text(((W - box[2] + box[0]) / 2, y), text, font=face, fill=fill)


def draw_art(draw):
    draw.rounded_rectangle((120, 290, 1080, 1040), radius=45, fill="#d8e2c2", outline="#6f8061", width=5)
    draw.rectangle((120, 820, 1080, 1040), fill="#9b7653")
    draw.ellipse((180, 745, 530, 970), fill="#777267", outline="#4e5049", width=5)
    draw.rounded_rectangle((660, 690, 1030, 850), radius=55, fill="#72533d", outline="#4c382b", width=6)
    for x, y in [(230, 510), (305, 420), (870, 430), (940, 550), (560, 915), (790, 950)]:
        draw.ellipse((x - 35, y - 12, x + 35, y + 12), fill="#6f8c55")

    # One continuous, uniformly thick snake with a small head and short blunt tail.
    body = [(360, 710), (420, 610), (570, 560), (735, 610), (790, 735), (700, 835), (545, 840), (455, 780)]
    draw.line(body + [body[0]], fill="#735b3f", width=82, joint="curve")
    draw.ellipse((318, 665, 405, 750), fill="#735b3f", outline="#4f422f", width=4)
    draw.ellipse((339, 687, 348, 696), fill="#151913")
    draw.line((790, 735, 850, 685), fill="#735b3f", width=70)
    draw.ellipse((815, 650, 885, 720), fill="#735b3f", outline="#4f422f", width=4)
    for x, y in [(470, 607), (570, 586), (675, 615), (735, 690), (660, 815), (530, 820), (425, 750)]:
        draw.arc((x - 28, y - 18, x + 28, y + 18), 190, 350, fill="#9b8161", width=3)


def label(draw, box, lines):
    draw.rounded_rectangle(box, radius=18, fill="#f7edcf", outline="#8b765c", width=4)
    face = font(28, bold=True)
    x0, y0, x1, y1 = box
    y = y0 + 30
    for line in lines:
        width = draw.textbbox((0, 0), line, font=face)[2]
        draw.text(((x0 + x1 - width) / 2, y), line, font=face, fill="#493b2c")
        y += 42


def render_png(language, title, labels, output):
    canvas = Image.new("RGB", (W, H), "#eadbb8")
    draw = ImageDraw.Draw(canvas, "RGBA")
    draw.rounded_rectangle((38, 38, 1162, 1462), radius=28, fill="#fff8e8", outline="#586a4d", width=5)
    centered(draw, 78, title, font(68 if language == "en" else 60, bold=True), "#3d4c36")
    centered(draw, 165, "Charina bottae", font(40, serif=True), "#665c48")
    draw_art(draw)
    boxes = [(65, 1090, 405, 1245), (430, 1090, 770, 1245), (795, 1090, 1135, 1245)]
    for box, lines in zip(boxes, labels):
        label(draw, box, lines)
    draw.rounded_rectangle((145, 1325, 1055, 1415), radius=17, fill="#dce2c4")
    centered(draw, 1352, FOOTER, font(29, bold=True), "#35402f")
    canvas.save(output, format="PNG", optimize=True)


def render_svg(language, title, labels, output):
    title_size = 68 if language == "en" else 60
    label_nodes = []
    for x, lines in zip((65, 430, 795), labels):
        tspans = "".join(
            f'<tspan x="{x + 170}" y="{1150 + i * 42}">{escape(line)}</tspan>'
            for i, line in enumerate(lines)
        )
        label_nodes.append(
            f'<rect x="{x}" y="1090" width="340" height="155" rx="18" fill="#f7edcf" stroke="#8b765c" stroke-width="4"/>'
            f'<text text-anchor="middle" font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="28" '
            f'font-weight="700" fill="#493b2c">{tspans}</text>'
        )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1500" viewBox="0 0 1200 1500">
<rect width="1200" height="1500" fill="#eadbb8"/>
<rect x="38" y="38" width="1124" height="1424" rx="28" fill="#fff8e8" stroke="#586a4d" stroke-width="5"/>
<text x="600" y="140" text-anchor="middle" font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="{title_size}" font-weight="700" fill="#3d4c36">{escape(title)}</text>
<text x="600" y="210" text-anchor="middle" font-family="Georgia, serif" font-size="40" font-style="italic" fill="#665c48">Charina bottae</text>
<rect x="120" y="290" width="960" height="750" rx="45" fill="#d8e2c2" stroke="#6f8061" stroke-width="5"/>
<rect x="120" y="820" width="960" height="220" fill="#9b7653"/>
<ellipse cx="355" cy="858" rx="175" ry="112" fill="#777267" stroke="#4e5049" stroke-width="5"/>
<rect x="660" y="690" width="370" height="160" rx="55" fill="#72533d" stroke="#4c382b" stroke-width="6"/>
<path d="M360 710 C390 600 520 550 630 575 C755 600 820 700 770 785 C710 875 560 875 455 800 C390 755 350 720 360 710" fill="none" stroke="#735b3f" stroke-width="82" stroke-linecap="round"/>
<ellipse cx="360" cy="708" rx="44" ry="42" fill="#735b3f" stroke="#4f422f" stroke-width="4"/>
<circle cx="344" cy="691" r="5" fill="#151913"/>
<path d="M785 735 Q830 700 850 685" fill="none" stroke="#735b3f" stroke-width="70" stroke-linecap="round"/>
<ellipse cx="850" cy="685" rx="35" ry="35" fill="#735b3f" stroke="#4f422f" stroke-width="4"/>
{''.join(label_nodes)}
<rect x="145" y="1325" width="910" height="90" rx="17" fill="#dce2c4"/>
<text x="600" y="1382" text-anchor="middle" font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="29" font-weight="700" fill="#35402f">{FOOTER}</text>
</svg>'''
    output.write_text(svg, encoding="utf-8")


ja = [["岩や倒木の下に", "ひそむ"], ["つやのある", "小さなボア"], ["丸い尾を", "盾にする"]]
en = [["Hidden under", "rocks and logs"], ["A small boa", "with smooth scales"], ["Its blunt tail", "becomes a shield"]]

render_png("ja", "ラバーボア", ja, IMAGES / "rubber_boa_japanese_textsafe_2026-06-11.png")
render_png("en", "Rubber Boa", en, IMAGES / "rubber_boa_english_textsafe_2026-06-11.png")
render_svg("ja", "ラバーボア", ja, IMAGES / "rubber_boa_japanese_textsafe_2026-06-11.svg")
render_svg("en", "Rubber Boa", en, IMAGES / "rubber_boa_english_textsafe_2026-06-11.svg")
