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
    draw.ellipse((145, 280, 1055, 1040), fill="#dbe1cf", outline="#64715b", width=4)
    for x, y, r in [(245, 390, 70), (910, 420, 85), (240, 835, 92), (930, 820, 72)]:
        draw.ellipse((x - r, y - r, x + r, y + r), fill="#a8b98d")

    draw.line((585, 250, 585, 400), fill="#576b45", width=18)
    draw.arc((515, 245, 690, 410), 195, 350, fill="#576b45", width=12)

    upper = [(505, 400), (445, 470), (470, 570), (545, 670), (655, 670), (730, 570), (755, 470), (695, 400)]
    draw.polygon(upper, fill="#8d3340", outline="#4f3c31")
    draw.ellipse((475, 625, 725, 1030), fill="#8d3340", outline="#4f3c31", width=6)
    draw.rectangle((545, 625, 655, 760), fill="#8d3340")
    draw.ellipse((492, 370, 708, 475), fill="#b45b55", outline="#4f3c31", width=6)
    draw.ellipse((520, 392, 680, 452), fill="#4a261f")
    draw.ellipse((455, 260, 745, 410), fill="#9d4d55", outline="#4f3c31", width=6)
    draw.arc((470, 280, 730, 430), 190, 350, fill="#eadfc3", width=13)

    draw.ellipse((610, 325, 825, 455), fill="#76634f", outline="#3e382f", width=5)
    draw.ellipse((765, 315, 850, 385), fill="#76634f", outline="#3e382f", width=4)
    draw.polygon([(842, 345), (885, 362), (842, 375)], fill="#635140")
    draw.ellipse((820, 340, 831, 351), fill="#181716")
    draw.ellipse((788, 300, 824, 340), fill="#806e59", outline="#3e382f", width=3)
    draw.line((635, 420, 570, 465), fill="#57483b", width=18)
    draw.line((720, 430, 675, 480), fill="#57483b", width=18)
    draw.line((785, 420, 755, 482), fill="#57483b", width=16)
    draw.line((630, 375, 535, 350), fill="#57483b", width=16)
    draw.arc((455, 300, 700, 520), 110, 245, fill="#57483b", width=18)


def label(draw, box, lines):
    draw.rounded_rectangle(box, radius=18, fill="#fff6df", outline="#667054", width=4)
    face = font(25 if max(map(len, lines)) > 18 else 31, bold=True)
    x0, y0, x1, y1 = box
    line_h = 42
    y = y0 + ((y1 - y0) - line_h * len(lines)) / 2
    for line in lines:
        width = draw.textbbox((0, 0), line, font=face)[2]
        draw.text(((x0 + x1 - width) / 2, y), line, font=face, fill="#303c2c")
        y += line_h


def render_png(language, title, labels, output):
    canvas = Image.new("RGB", (W, H), "#efe5cb")
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle((38, 38, 1162, 1462), radius=28, fill="#fffaf0", outline="#4e5946", width=5)
    centered(draw, 76, title, font(66 if language == "ja" else 70, bold=True), "#2c4635")
    centered(draw, 164, "Nepenthes lowii", font(40, serif=True), "#5b4a3d")
    draw_art(draw)
    boxes = [(70, 1080, 410, 1245), (430, 1080, 770, 1245), (790, 1080, 1130, 1245)]
    for box, lines in zip(boxes, labels):
        label(draw, box, lines)
    draw.rounded_rectangle((140, 1325, 1060, 1412), radius=17, fill="#d9e2cb")
    centered(draw, 1346, "IUCN Red List 2000: Vulnerable (VU)", font(34, bold=True), "#304b3b")
    canvas.save(output, format="PNG", optimize=True)


def svg_text_lines(x, center_y, lines):
    line_h = 42
    start = center_y - ((len(lines) - 1) * line_h / 2)
    return "".join(
        f'<tspan x="{x}" y="{start + i * line_h}">{escape(line)}</tspan>'
        for i, line in enumerate(lines)
    )


def render_svg(language, title, labels, output):
    label_nodes = []
    for x, lines in zip((70, 430, 790), labels):
        label_size = 25 if max(map(len, lines)) > 18 else 31
        label_nodes.append(
            f'<rect x="{x}" y="1080" width="340" height="165" rx="18" fill="#fff6df" '
            'stroke="#667054" stroke-width="4"/>'
            f'<text x="{x + 170}" y="1162" text-anchor="middle" '
            f'font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="{label_size}" '
            f'font-weight="700" fill="#303c2c">{svg_text_lines(x + 170, 1162, lines)}</text>'
        )
    title_size = 66 if language == "ja" else 70
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1500" viewBox="0 0 1200 1500">
  <rect width="1200" height="1500" fill="#efe5cb"/>
  <rect x="38" y="38" width="1124" height="1424" rx="28" fill="#fffaf0" stroke="#4e5946" stroke-width="5"/>
  <text x="600" y="140" text-anchor="middle" font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="{title_size}" font-weight="700" fill="#2c4635">{escape(title)}</text>
  <text x="600" y="215" text-anchor="middle" font-family="Georgia, serif" font-size="40" font-style="italic" fill="#5b4a3d">Nepenthes lowii</text>
  <ellipse cx="600" cy="660" rx="455" ry="380" fill="#dbe1cf" stroke="#64715b" stroke-width="4"/>
  <path d="M585 250 V400 M585 300 C640 290 675 260 690 245" fill="none" stroke="#576b45" stroke-width="18" stroke-linecap="round"/>
  <path d="M505 400 C440 470 445 540 470 570 L545 670 H655 L730 570 C755 540 760 470 695 400 Z" fill="#8d3340" stroke="#4f3c31" stroke-width="6"/>
  <ellipse cx="600" cy="827" rx="125" ry="203" fill="#8d3340" stroke="#4f3c31" stroke-width="6"/>
  <rect x="545" y="625" width="110" height="135" fill="#8d3340"/>
  <ellipse cx="600" cy="422" rx="108" ry="53" fill="#b45b55" stroke="#4f3c31" stroke-width="6"/>
  <ellipse cx="600" cy="422" rx="80" ry="30" fill="#4a261f"/>
  <ellipse cx="600" cy="335" rx="145" ry="75" fill="#9d4d55" stroke="#4f3c31" stroke-width="6"/>
  <path d="M485 355 Q600 410 715 355" fill="none" stroke="#eadfc3" stroke-width="13"/>
  <ellipse cx="718" cy="390" rx="108" ry="65" fill="#76634f" stroke="#3e382f" stroke-width="5"/>
  <ellipse cx="808" cy="350" rx="43" ry="35" fill="#76634f" stroke="#3e382f" stroke-width="4"/>
  <path d="M842 345 L885 362 L842 375 Z" fill="#635140"/>
  <circle cx="826" cy="345" r="6" fill="#181716"/>
  <circle cx="806" cy="318" r="20" fill="#806e59" stroke="#3e382f" stroke-width="3"/>
  <path d="M635 420 L570 465 M720 430 L675 480 M785 420 L755 482 M630 375 L535 350 M630 375 C520 385 505 475 540 500" fill="none" stroke="#57483b" stroke-width="17" stroke-linecap="round"/>
  {''.join(label_nodes)}
  <rect x="140" y="1325" width="920" height="87" rx="17" fill="#d9e2cb"/>
  <text x="600" y="1380" text-anchor="middle" font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="34" font-weight="700" fill="#304b3b">IUCN Red List 2000: Vulnerable (VU)</text>
</svg>
'''
    output.write_text(svg, encoding="utf-8")


ja_labels = [
    ["ボルネオの", "山地林に育つ"],
    ["成長すると", "便器形の袋"],
    ["ツパイのふんから", "窒素を得る"],
]
en_labels = [
    ["Borneo montane", "forests"],
    ["Mature pitchers", "become", "toilet-shaped"],
    ["Tree-shrew", "droppings provide", "nitrogen"],
]

render_png("ja", "ネペンテス・ローウィー", ja_labels, IMAGES / "nepenthes_lowii_japanese_textsafe_2026-06-09.png")
render_png("en", "Low's Pitcher Plant", en_labels, IMAGES / "nepenthes_lowii_english_textsafe_2026-06-09.png")
render_svg("ja", "ネペンテス・ローウィー", ja_labels, IMAGES / "nepenthes_lowii_japanese_textsafe_2026-06-09.svg")
render_svg("en", "Low's Pitcher Plant", en_labels, IMAGES / "nepenthes_lowii_english_textsafe_2026-06-09.svg")
