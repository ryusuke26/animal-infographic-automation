Add-Type -AssemblyName System.Drawing

$root = if ($PSScriptRoot) {
    $PSScriptRoot
} else {
    Join-Path (Get-Location) "infographic-packages\2026-06-14-mexican-burrowing-toad"
}
$images = Join-Path $root "images"
New-Item -ItemType Directory -Force $images | Out-Null

$width = 1200
$height = 1500
$paper = [System.Drawing.ColorTranslator]::FromHtml("#FFF8E8")
$ink = [System.Drawing.ColorTranslator]::FromHtml("#3D342C")
$green = [System.Drawing.ColorTranslator]::FromHtml("#526A53")
$soil = [System.Drawing.ColorTranslator]::FromHtml("#9B765D")
$frog = [System.Drawing.ColorTranslator]::FromHtml("#4A3A32")
$spot = [System.Drawing.ColorTranslator]::FromHtml("#D68B35")
$pool = [System.Drawing.ColorTranslator]::FromHtml("#AFC8C8")

function New-Font([float]$size, [System.Drawing.FontStyle]$style = [System.Drawing.FontStyle]::Regular) {
    $families = @("Yu Gothic", "Meiryo", "Arial")
    foreach ($family in $families) {
        try {
            return [System.Drawing.Font]::new($family, $size, $style)
        } catch {
        }
    }
    return [System.Drawing.SystemFonts]::DefaultFont
}

function Draw-CenteredText($graphics, $text, $font, $brush, [float]$y) {
    $size = $graphics.MeasureString($text, $font)
    $graphics.DrawString($text, $font, $brush, ($width - $size.Width) / 2, $y)
}

function Save-Poster($language, $title, $labels, $slug) {
    $bitmap = [System.Drawing.Bitmap]::new($width, $height)
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $graphics.Clear($paper)

    $inkBrush = [System.Drawing.SolidBrush]::new($ink)
    $greenBrush = [System.Drawing.SolidBrush]::new($green)
    $soilBrush = [System.Drawing.SolidBrush]::new($soil)
    $frogBrush = [System.Drawing.SolidBrush]::new($frog)
    $spotBrush = [System.Drawing.SolidBrush]::new($spot)
    $poolBrush = [System.Drawing.SolidBrush]::new($pool)
    $paperBrush = [System.Drawing.SolidBrush]::new($paper)
    $borderPen = [System.Drawing.Pen]::new($green, 5)

    $titleFont = New-Font $(if ($language -eq "ja") { 62 } else { 56 }) ([System.Drawing.FontStyle]::Bold)
    $scienceFont = New-Font 34 ([System.Drawing.FontStyle]::Italic)
    $labelFont = New-Font $(if ($language -eq "ja") { 29 } else { 25 }) ([System.Drawing.FontStyle]::Bold)
    $footerFont = New-Font 31 ([System.Drawing.FontStyle]::Bold)

    $graphics.DrawRectangle($borderPen, 38, 38, 1124, 1424)
    Draw-CenteredText $graphics $title $titleFont $greenBrush 75
    Draw-CenteredText $graphics "Rhinophrynus dorsalis" $scienceFont $inkBrush 165

    $graphics.FillEllipse($poolBrush, 120, 740, 960, 230)
    $graphics.FillRectangle($soilBrush, 90, 900, 1020, 150)
    $graphics.FillEllipse($frogBrush, 325, 420, 550, 430)
    $graphics.FillPolygon($frogBrush, @(
        [System.Drawing.PointF]::new(300, 610),
        [System.Drawing.PointF]::new(420, 520),
        [System.Drawing.PointF]::new(420, 700)
    ))
    $graphics.FillEllipse($inkBrush, 344, 575, 24, 18)
    $graphics.FillEllipse($inkBrush, 385, 550, 24, 18)
    foreach ($point in @(
        @(470, 490), @(565, 455), @(665, 490), @(730, 570),
        @(500, 660), @(615, 700), @(760, 670)
    )) {
        $graphics.FillEllipse($spotBrush, $point[0], $point[1], 36, 25)
    }
    $limbPen = [System.Drawing.Pen]::new($frog, 34)
    $graphics.DrawLine($limbPen, 430, 720, 305, 830)
    $graphics.DrawLine($limbPen, 770, 720, 905, 830)
    $graphics.DrawLine($limbPen, 420, 660, 285, 690)
    $graphics.DrawLine($limbPen, 785, 660, 920, 690)

    for ($i = 0; $i -lt 3; $i++) {
        $x = 60 + ($i * 380)
        $graphics.FillRectangle($paperBrush, $x, 1090, 340, 155)
        $graphics.DrawRectangle($borderPen, $x, 1090, 340, 155)
        $format = [System.Drawing.StringFormat]::new()
        $format.Alignment = [System.Drawing.StringAlignment]::Center
        $format.LineAlignment = [System.Drawing.StringAlignment]::Center
        $graphics.DrawString(
            $labels[$i],
            $labelFont,
            $greenBrush,
            [System.Drawing.RectangleF]::new($x + 10, 1100, 320, 135),
            $format
        )
        $format.Dispose()
    }

    $graphics.FillRectangle($greenBrush, 125, 1325, 950, 85)
    Draw-CenteredText $graphics "IUCN Red List 2020: Least Concern (LC)" $footerFont $paperBrush 1344

    $png = Join-Path $images "${slug}_2026-06-14.png"
    $bitmap.Save($png, [System.Drawing.Imaging.ImageFormat]::Png)

    $titleEscaped = [System.Security.SecurityElement]::Escape($title)
    $labelsEscaped = $labels | ForEach-Object { [System.Security.SecurityElement]::Escape($_) }
    $svg = @"
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1500" viewBox="0 0 1200 1500">
  <rect width="1200" height="1500" fill="#FFF8E8"/>
  <rect x="38" y="38" width="1124" height="1424" fill="none" stroke="#526A53" stroke-width="5"/>
  <text x="600" y="140" text-anchor="middle" font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="62" font-weight="700" fill="#526A53">$titleEscaped</text>
  <text x="600" y="215" text-anchor="middle" font-family="Georgia, serif" font-size="34" font-style="italic" fill="#3D342C">Rhinophrynus dorsalis</text>
  <ellipse cx="600" cy="855" rx="480" ry="115" fill="#AFC8C8"/>
  <rect x="90" y="900" width="1020" height="150" fill="#9B765D"/>
  <ellipse cx="600" cy="635" rx="275" ry="215" fill="#4A3A32"/>
  <path d="M300 610 L420 520 L420 700 Z" fill="#4A3A32"/>
  <circle cx="356" cy="584" r="11" fill="#3D342C"/>
  <circle cx="397" cy="559" r="11" fill="#3D342C"/>
  <g fill="#D68B35">
    <ellipse cx="488" cy="502" rx="18" ry="13"/><ellipse cx="583" cy="468" rx="18" ry="13"/>
    <ellipse cx="683" cy="502" rx="18" ry="13"/><ellipse cx="748" cy="582" rx="18" ry="13"/>
    <ellipse cx="518" cy="672" rx="18" ry="13"/><ellipse cx="633" cy="712" rx="18" ry="13"/>
  </g>
  <g stroke="#4A3A32" stroke-width="34" stroke-linecap="round">
    <path d="M430 720 L305 830"/><path d="M770 720 L905 830"/>
    <path d="M420 660 L285 690"/><path d="M785 660 L920 690"/>
  </g>
  <g font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="28" font-weight="700" text-anchor="middle" fill="#526A53">
    <rect x="60" y="1090" width="340" height="155" fill="#FFF8E8" stroke="#526A53" stroke-width="5"/>
    <rect x="440" y="1090" width="340" height="155" fill="#FFF8E8" stroke="#526A53" stroke-width="5"/>
    <rect x="820" y="1090" width="340" height="155" fill="#FFF8E8" stroke="#526A53" stroke-width="5"/>
    <text x="230" y="1178">$($labelsEscaped[0])</text>
    <text x="610" y="1178">$($labelsEscaped[1])</text>
    <text x="990" y="1178">$($labelsEscaped[2])</text>
  </g>
  <rect x="125" y="1325" width="950" height="85" fill="#526A53"/>
  <text x="600" y="1380" text-anchor="middle" font-family="Yu Gothic, Meiryo, Arial, sans-serif" font-size="31" font-weight="700" fill="#FFF8E8">IUCN Red List 2020: Least Concern (LC)</text>
</svg>
"@
    $svgPath = Join-Path $images "${slug}_2026-06-14.svg"
    [System.IO.File]::WriteAllText($svgPath, $svg, [System.Text.UTF8Encoding]::new($false))

    foreach ($item in @(
        $titleFont, $scienceFont, $labelFont, $footerFont,
        $inkBrush, $greenBrush, $soilBrush, $frogBrush, $spotBrush,
        $poolBrush, $paperBrush, $borderPen, $limbPen, $graphics, $bitmap
    )) {
        $item.Dispose()
    }
}

Save-Poster "ja" "メキシコジムグリガエル" @(
    "乾いた季節は`n地面の下",
    "後ろ向きに`n土へもぐる",
    "大雨の夜、`n一時池で鳴く"
) "mexican_burrowing_toad_japanese_textsafe"

Save-Poster "en" "Mexican Burrowing Toad" @(
    "Underground through`nthe dry season",
    "Digs backward`ninto the soil",
    "Calls in rain-filled`ntemporary pools"
) "mexican_burrowing_toad_english_textsafe"
