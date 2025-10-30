#!/usr/bin/env python3
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


def lerp_color(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def main(output_path: Path) -> None:
    size = 1024
    image = Image.new("RGB", (size, size), "#05070a")
    draw = ImageDraw.Draw(image)

    # Subtle vignette glow
    vignette = Image.new("L", (size, size), 0)
    vignette_draw = ImageDraw.Draw(vignette)
    vignette_draw.ellipse((-200, -200, size + 200, size + 200), fill=255)
    vignette = vignette.filter(ImageFilter.GaussianBlur(radius=180))
    for y in range(size):
        for x in range(size):
            alpha = vignette.getpixel((x, y)) / 255.0
            base = image.getpixel((x, y))
            blended = lerp_color(base, (12, 20, 32), alpha * 0.4)
            image.putpixel((x, y), blended)

    # Grid panel frame
    panel_margin = 90
    panel_radius = 80
    draw.rounded_rectangle(
        (panel_margin, panel_margin, size - panel_margin, size - panel_margin),
        radius=panel_radius,
        fill=(12, 18, 30),
        outline=(46, 68, 98),
        width=6,
    )

    # Subtle inner gloss
    gloss = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    gloss_draw = ImageDraw.Draw(gloss)
    gloss_draw.pieslice(
        (
            panel_margin - 30,
            panel_margin - 30,
            size * 0.85,
            size * 0.65,
        ),
        180,
        360,
        fill=(80, 120, 180, 38),
    )
    gloss = gloss.filter(ImageFilter.GaussianBlur(radius=40))
    image.paste(gloss, (0, 0), gloss)

    # LED grid
    rows = 4
    cols = 4
    led_radius = 72
    led_spacing_x = (size - 2 * panel_margin - led_radius * 2) / (cols - 1)
    led_spacing_y = (size - 2 * panel_margin - led_radius * 2) / (rows - 1)

    palette = [
        (143, 255, 122),
        (82, 229, 255),
        (255, 204, 94),
        (255, 102, 122),
    ]

    glow_layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_layer)

    for row in range(rows):
        for col in range(cols):
            cx = panel_margin + led_radius + col * led_spacing_x
            cy = panel_margin + led_radius + row * led_spacing_y

            color = palette[(row + col) % len(palette)]
            intensity = 0.6 + 0.4 * math.sin((row + col) * 0.7 + col)
            brightness = max(0.4, min(1.0, intensity))
            value = tuple(int(c * brightness) for c in color)

            # Base LED
            draw.ellipse(
                (cx - led_radius, cy - led_radius, cx + led_radius, cy + led_radius),
                fill=(18, 28, 42),
            )

            # Inner core
            core_radius = led_radius * 0.6
            draw.ellipse(
                (cx - core_radius, cy - core_radius, cx + core_radius, cy + core_radius),
                fill=value,
            )

            # Glow
            glow_radius = led_radius * 1.5
            glow_color = (*value, 140)
            glow_draw.ellipse(
                (cx - glow_radius, cy - glow_radius, cx + glow_radius, cy + glow_radius),
                fill=glow_color,
            )

    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(radius=60))
    image.paste(glow_layer, (0, 0), glow_layer)

    # Status strip
    strip_height = 72
    strip_rect = (
        panel_margin,
        size - panel_margin - strip_height,
        size - panel_margin,
        size - panel_margin,
    )
    draw.rounded_rectangle(
        strip_rect,
        radius=40,
        fill=(20, 34, 50),
    )
    draw.text(
        (strip_rect[0] + 48, strip_rect[1] + 18),
        "BLINKY LIGHTS",
        fill=(120, 200, 255),
        font=None,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path, format="PNG")
    print(f"Icon exported to {output_path}")


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    output = root / "assets" / "icon-1024.png"
    main(output)
