#!/usr/bin/env python3
"""Generate a 1200x630 Open Graph card for recruiter link previews."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
OUT = Path(__file__).resolve().parents[1] / "og-card.png"

bg = (5, 7, 13)
panel = (10, 14, 23)
green = (0, 255, 163)
cyan = (0, 212, 255)
text = (230, 237, 243)
dim = (139, 150, 168)

img = Image.new("RGB", (W, H), bg)
d = ImageDraw.Draw(img)

def font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

# Left accent
d.rectangle([0, 0, 12, H], fill=green)
# Soft panel
d.rounded_rectangle([48, 48, W - 48, H - 48], radius=18, outline=(30, 37, 56), width=2)

kicker = font(22, bold=True)
name = font(48, bold=True)
role = font(26, bold=True)
meta = font(20)

d.text((88, 100), "CLOUD SECURITY  ·  IDENTITY & ACCESS", fill=green, font=kicker)
d.text((88, 170), "Samuel Kofi Agyei-Tuffour", fill=text, font=name)
d.text((88, 250), "Cloud Security Engineer", fill=cyan, font=role)
d.text((88, 292), "Identity & Access Administrator", fill=cyan, font=role)

d.text((88, 390), "Entra ID  ·  PIM  ·  Conditional Access  ·  IGA", fill=dim, font=meta)
d.text((88, 430), "SC-100  ·  AZ-500  ·  Rotterdam, Netherlands", fill=dim, font=meta)
d.text((88, 500), "Open to Cloud Security / IAM / IGA roles in the Netherlands", fill=green, font=meta)

img.save(OUT, "PNG", optimize=True)
print(f"wrote {OUT} {OUT.stat().st_size} bytes")
