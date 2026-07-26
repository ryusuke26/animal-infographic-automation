#!/usr/bin/env python3
"""Compose deterministic bilingual posters from one text-free illustration."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


CANVAS = (1024, 1536)
FONT_DIR = Path(r"C:\Windows\Fonts")


def read_utf8(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def field(text: str, label: str) -> str:
    match = re.search(rf"^{re.escape(label)}:\s*(.+?)\s*$", text, re.MULTILINE)
    if not match:
        raise ValueError(f"{label!r} is missing from {text[:80]!r}")
    return match.group(1).strip().strip("*_`")


def parse_copy(path: Path) -> tuple[str, str, list[str], str]:
    text = read_utf8(path)
    title = field(text, "Title")
    scientific = field(text, "Scientific name")

    labels_match = re.search(
        r"Observation labels:\s*(.*?)\n\s*Footer/status:",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not labels_match:
        raise ValueError("Observation labels / Footer status section is missing")
    labels = []
    for line in labels_match.group(1).splitlines():
        match = re.match(r"\s*\d+\.\s*(.+?)\s*$", line)
        if match:
            labels.append(match.group(1).strip())
    if len(labels) != 3:
        raise ValueError(f"expected exactly 3 observation labels, found {len(labels)}")

    footer_match = re.search(
        r"Footer/status:\s*(.*)\Z",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not footer_match:
        raise ValueError("Footer/status section is missing")
    footer_lines = [
        line.strip() for line in footer_match.group(1).splitlines() if line.strip()
    ]
    if not footer_lines:
        raise ValueError("Footer/status is empty")
    return title, scientific, labels, footer_lines[0]


def existing_font(candidates: tuple[str, ...]) -> Path:
    for name in candidates:
        path = FONT_DIR / name
        if path.is_file():
            return path
    raise FileNotFoundError(f"none of these fonts exists: {candidates}")


def font_paths(language: str) -> tuple[Path, Path, Path]:
    if language == "ja":
        regular = existing_font(("meiryo.ttc", "NotoSansJP-VF.ttf", "YuGothM.ttc"))
        bold = existing_font(("meiryob.ttc", "YuGothB.ttc", "NotoSansJP-VF.ttf"))
    else:
        regular = existing_font(("arial.ttf", "segoeui.ttf"))
        bold = existing_font(("arialbd.ttf", "segoeuib.ttf"))
    italic = existing_font(("ariali.ttf", "segoeuii.ttf"))
    return regular, bold, italic


def fit_font(
    draw: ImageDraw.ImageDraw,
    text: str,
    path: Path,
    max_size: int,
    min_size: int,
    max_width: int,
) -> ImageFont.FreeTypeFont:
    for size in range(max_size, min_size - 1, -2):
        font = ImageFont.truetype(str(path), size)
        box = draw.textbbox((0, 0), text, font=font)
        if box[2] - box[0] <= max_width:
            return font
    return ImageFont.truetype(str(path), min_size)


def split_units(text: str, language: str) -> list[str]:
    if language == "ja":
        return list(text)
    words = text.split()
    return [word if index == 0 else f" {word}" for index, word in enumerate(words)]


def wrap_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont,
    max_width: int,
    language: str,
    max_lines: int,
) -> list[str]:
    units = split_units(text, language)
    lines: list[str] = []
    current = ""
    for unit in units:
        candidate = f"{current}{unit}"
        width = draw.textbbox((0, 0), candidate, font=font)[2]
        if current and width > max_width:
            lines.append(current.strip())
            current = unit.lstrip()
        else:
            current = candidate
    if current:
        lines.append(current.strip())
    if len(lines) > max_lines:
        raise ValueError(
            f"text needs {len(lines)} lines but the card allows {max_lines}: {text}"
        )
    if language == "ja" and len(lines) > 1 and len(lines[-1]) <= 2:
        line_count = len(lines)
        chunk_size, remainder = divmod(len(text), line_count)
        balanced: list[str] = []
        offset = 0
        for index in range(line_count):
            length = chunk_size + (1 if index < remainder else 0)
            balanced.append(text[offset : offset + length].strip())
            offset += length
        if all(
            draw.textbbox((0, 0), line, font=font)[2] <= max_width
            for line in balanced
        ):
            lines = balanced
    return lines


def fit_wrapped_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    font_path: Path,
    max_size: int,
    min_size: int,
    max_width: int,
    language: str,
    max_lines: int,
) -> tuple[ImageFont.FreeTypeFont, list[str]]:
    for size in range(max_size, min_size - 1, -1):
        font = ImageFont.truetype(str(font_path), size)
        try:
            lines = wrap_text(
                draw,
                text,
                font,
                max_width=max_width,
                language=language,
                max_lines=max_lines,
            )
        except ValueError:
            continue
        return font, lines
    raise ValueError(f"text cannot fit the observation card: {text}")


def rounded_panel(
    overlay: Image.Image,
    box: tuple[int, int, int, int],
    radius: int,
    fill: tuple[int, int, int, int],
    outline: tuple[int, int, int, int] | None = None,
    width: int = 1,
) -> None:
    ImageDraw.Draw(overlay).rounded_rectangle(
        box,
        radius=radius,
        fill=fill,
        outline=outline,
        width=width,
    )


def draw_icon(
    draw: ImageDraw.ImageDraw,
    index: int,
    x: int,
    y: int,
    color: tuple[int, int, int, int],
) -> None:
    if index == 1:
        draw.ellipse((x, y + 4, x + 30, y + 22), outline=color, width=4)
        draw.line((x + 15, y + 1, x + 15, y + 27), fill=color, width=3)
    elif index == 2:
        draw.arc((x, y, x + 34, y + 24), 10, 170, fill=color, width=4)
        draw.arc((x, y + 10, x + 34, y + 34), 190, 350, fill=color, width=4)
    else:
        points = [
            (x + 17, y),
            (x + 22, y + 12),
            (x + 35, y + 13),
            (x + 25, y + 21),
            (x + 29, y + 34),
            (x + 17, y + 26),
            (x + 5, y + 34),
            (x + 9, y + 21),
            (x - 1, y + 13),
            (x + 12, y + 12),
        ]
        draw.line(points + [points[0]], fill=color, width=3, joint="curve")


def compose(
    background_path: Path,
    copy_path: Path,
    output_path: Path,
    language: str,
    card_layout: str = "standard",
) -> None:
    title, scientific, labels, footer = parse_copy(copy_path)
    regular_path, bold_path, italic_path = font_paths(language)

    with Image.open(background_path) as source:
        background = ImageOps.exif_transpose(source).convert("RGB")
        canvas = ImageOps.fit(
            background,
            CANVAS,
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.45),
        ).convert("RGBA")

    wash = Image.new("RGBA", CANVAS, (250, 244, 226, 35))
    canvas = Image.alpha_composite(canvas, wash)
    panels = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    rounded_panel(panels, (42, 36, 982, 274), 34, (255, 251, 239, 232))
    if card_layout == "lower":
        card_boxes = (
            (54, 930, 704, 1068),
            (320, 1090, 970, 1228),
            (54, 1250, 704, 1388),
        )
    else:
        card_boxes = (
            (54, 736, 704, 898),
            (320, 930, 970, 1092),
            (54, 1124, 704, 1286),
        )
    for box in card_boxes:
        rounded_panel(
            panels,
            box,
            28,
            (255, 252, 242, 226),
            (87, 74, 55, 90),
            2,
        )
    rounded_panel(panels, (42, 1418, 982, 1494), 28, (255, 251, 239, 238))
    canvas = Image.alpha_composite(canvas, panels)
    draw = ImageDraw.Draw(canvas)

    ink = (38, 34, 29, 255)
    muted = (82, 70, 56, 255)
    accents = (
        (39, 113, 122, 255),
        (184, 112, 42, 255),
        (110, 95, 150, 255),
    )

    title_font = fit_font(draw, title, bold_path, 66, 38, 840)
    scientific_font = fit_font(draw, scientific, italic_path, 32, 24, 840)
    draw.text((92, 76), title, font=title_font, fill=ink)
    draw.line((92, 174, 932, 174), fill=(184, 112, 42, 180), width=3)
    draw.text((92, 196), scientific, font=scientific_font, fill=muted)

    number_font = ImageFont.truetype(str(bold_path), 34)
    for index, (box, label, accent) in enumerate(
        zip(card_boxes, labels, accents),
        start=1,
    ):
        left, top, right, bottom = box
        circle = (left + 28, top + 36, left + 98, top + 106)
        draw.ellipse(circle, fill=accent)
        number = str(index)
        number_box = draw.textbbox((0, 0), number, font=number_font)
        number_width = number_box[2] - number_box[0]
        number_height = number_box[3] - number_box[1]
        draw.text(
            (
                circle[0] + (circle[2] - circle[0] - number_width) / 2,
                circle[1] + (circle[3] - circle[1] - number_height) / 2 - 4,
            ),
            number,
            font=number_font,
            fill=(255, 255, 255, 255),
        )
        draw_icon(draw, index, right - 66, top + 24, accent)
        card_font, lines = fit_wrapped_text(
            draw,
            label,
            regular_path,
            max_size=29 if language == "ja" else 28,
            min_size=21,
            max_width=right - left - 168,
            language=language,
            max_lines=2 if language == "ja" else 3,
        )
        line_height = 39 if language == "ja" else 37
        total_height = len(lines) * line_height
        text_y = top + (bottom - top - total_height) / 2 - 2
        for line in lines:
            draw.text((left + 124, text_y), line, font=card_font, fill=ink)
            text_y += line_height

    footer_font = fit_font(draw, footer, bold_path, 28, 20, 860)
    footer_box = draw.textbbox((0, 0), footer, font=footer_font)
    footer_width = footer_box[2] - footer_box[0]
    draw.text(
        ((CANVAS[0] - footer_width) / 2, 1438),
        footer,
        font=footer_font,
        fill=ink,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(output_path, format="PNG", optimize=True)
    with Image.open(output_path) as result:
        if result.size != CANVAS:
            raise RuntimeError(f"unexpected output size {result.size}; expected {CANVAS}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Compose an exact 1024x1536 poster from one text-free Image Gen "
            "background and a locked infographic-copy Markdown file."
        )
    )
    parser.add_argument("--background", required=True, type=Path)
    parser.add_argument("--copy", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--language", required=True, choices=("ja", "en"))
    parser.add_argument(
        "--card-layout",
        choices=("standard", "lower"),
        default="standard",
        help=(
            "place compact cards lower on the poster when the complete hero "
            "silhouette occupies the middle band"
        ),
    )
    args = parser.parse_args()

    try:
        compose(
            args.background.resolve(),
            args.copy.resolve(),
            args.output.resolve(),
            args.language,
            args.card_layout,
        )
    except (OSError, ValueError) as exc:
        raise SystemExit(str(exc)) from exc
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
