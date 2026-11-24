#!/usr/bin/env python3
"""Render THE WORLD TODAY — Tuesday, 24 November 2026 front page.

Deterministic PIL drawing: fixed strings, fixed coordinates, no clock,
no randomness, no network. Output: 1024x1024 PNG, entry.png.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (247, 243, 232)
INK = (17, 17, 17)
NAVY = (20, 33, 61)
GOLD = (201, 162, 39)
RED = (178, 34, 34)
GREY = (90, 86, 78)
RULE = (120, 116, 104)
FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, fill=INK):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def kicker(draw, x, y, text, color=RED):
    draw.text((x, y), text, font=SANS_B(17), fill=color)
    return y + 24


def headline(draw, x, y, text, size, max_w, leading):
    return para(draw, x, y, text, SERIF_B(size), max_w, leading)


def rule(draw, x, y, w, color=RULE, width=2):
    draw.line([(x, y), (x + w, y)], fill=color, width=width)


def draw_lead_art(draw):
    """Simple drawn scene: Gaza City skyline at dusk with a smoke plume."""
    x0, y0, x1, y1 = 24, 232, 500, 428
    draw.rectangle([x0, y0, x1, y1], fill=(233, 214, 178))
    for i, col in enumerate([(240, 196, 130), (236, 178, 120), (228, 158, 112)]):
        draw.rectangle([x0, y0 + i * 24, x1, y0 + (i + 1) * 24], fill=col)
    draw.ellipse([x0 + 330, y0 + 18, x0 + 386, y0 + 74], fill=(250, 226, 150))
    draw.ellipse([x0 + 150, y0 + 30, x0 + 210, y0 + 90], fill=(120, 116, 110))
    draw.ellipse([x0 + 175, y0 + 8, x0 + 235, y0 + 68], fill=(105, 101, 96))
    draw.ellipse([x0 + 205, y0 + 40, x0 + 250, y0 + 95], fill=(130, 126, 120))
    for bx, bw, bh in [(0, 70, 90), (78, 55, 130), (141, 80, 105), (229, 60, 145),
                       (297, 65, 95), (370, 62, 125), (440, 36, 85)]:
        draw.rectangle([x0 + bx, y1 - bh, x0 + bx + bw, y1], fill=(58, 52, 48))
        for wy in range(y1 - bh + 12, y1 - 8, 22):
            for wx in range(x0 + bx + 10, x0 + bx + bw - 12, 20):
                draw.rectangle([wx, wy, wx + 8, wy + 10], fill=(250, 226, 150))
    draw.rectangle([x0, y0, x1, y1], outline=INK, width=3)
    draw.text((x0 + 10, y1 - 30), "GAZA CITY", font=SANS_B(16), fill=(255, 255, 255))


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # ---- Masthead ----
    d.rectangle([0, 0, W, 132], fill=NAVY)
    d.text((512, 18), "THE WORLD TODAY", font=SERIF_B(64), fill=(255, 255, 255),
           anchor="ma")
    d.text((512, 92), "TUESDAY, 24 NOVEMBER 2026", font=SANS_B(26), fill=GOLD,
           anchor="ma")
    d.line([(0, 132), (W, 132)], fill=GOLD, width=4)
    # ---- Lead story: GAZA ----
    y = kicker(d, 24, 148, "GAZA  |  LEAD STORY")
    y = headline(d, 24, y, "HAMAS SECURITY CHIEF KILLED", 36, 976, 44)
    draw_lead_art(d)
    tx = 524
    ty = para(d, tx, 232,
              "Naeem Abu Nahel, director of Hamas' internal security apparatus, "
              "was killed in an Israeli airstrike in western Gaza City on Tuesday, "
              "with six others, including two police officers.",
              SANS(19), 476, 26)
    ty += 10
    ty = para(d, tx, ty,
              "The strike hits Gaza's security leadership as the fragile "
              "ceasefire strains.",
              SANS(19), 476, 26)
    d.text((tx, 404), "Source: Reuters", font=SANS(16), fill=GREY)
    rule(d, 24, 448, 976, width=3)

    # ---- Stories 2 & 3 ----
    col_w, gap = 476, 24
    # Ukraine (left)
    y = kicker(d, 24, 466, "UKRAINE")
    y = headline(d, 24, y, "ZAPORIZHZHIA HIT OVERNIGHT", 27, col_w, 33)
    y = para(d, 24, y + 4,
             "Russian attack kills 2 and wounds about 40, including four children, "
             "at an apartment building.",
             SANS(17), col_w, 23)
    d.text((24, 612), "Source: Governor Semikin", font=SANS(15), fill=GREY)
    # Sanofi (right)
    x2 = 24 + col_w + gap
    y2 = kicker(d, x2, 466, "BUSINESS")
    y2 = headline(d, x2, y2, "SANOFI BUYS INSMED FOR $41BN", 27, col_w, 33)
    y2 = para(d, x2, y2 + 4,
              "Sanofi agrees to buy US biotech Insmed for $41bn cash ($175/share) "
              "\u2014 2026's biggest biopharma deal.",
              SANS(17), col_w, 23)
    d.text((x2, 612), "Source: Sanofi, Paris", font=SANS(15), fill=GREY)
    rule(d, 24, 640, 976, width=2)
    # ---- Stories 4 & 5 ----
    y = kicker(d, 24, 656, "DEFENCE")
    y = headline(d, 24, y, "GERMANY GETS UKRAINE'S DELTA", 27, col_w, 33)
    y = para(d, 24, y + 4,
             "Germany is the first foreign country to gain access to Ukraine's "
             "DELTA battlefield system.",
             SANS(17), col_w, 23)
    d.text((24, 800), "Source: Ukraine Defence Ministry", font=SANS(15), fill=GREY)
    y2 = kicker(d, x2, 656, "CONGO")
    y2 = headline(d, x2, y2, "EBOLA TEAMS EVACUATED", 27, col_w, 33)
    y2 = para(d, x2, y2 + 4,
              "WHO staff and Ebola responders evacuated safely from Akwe hospital "
              "in Ituri after sheltering 3+ days amid fighting.",
              SANS(17), col_w, 23)
    d.text((x2, 800), "Source: WHO chief Tedros", font=SANS(15), fill=GREY)
    # ---- IN BRIEF strip ----
    d.rectangle([0, 828, W, H], fill=NAVY)
    d.text((24, 842), "IN BRIEF", font=SANS_B(22), fill=GOLD)
    d.line([(24, 876), (1000, 876)], fill=GOLD, width=2)
    briefs = [
        ("IRAQ", "PM orders the oil ministry to manage oilfields in "
                 "Kurdish-controlled areas."),
        ("KOREA", "Russian warplanes enter South Korea's air defence zone "
                  "near Ulleungdo; Seoul scrambles F-15Ks."),
        ("UN", "47,000 women killed by partners or family in 2025 \u2014 "
               "five every hour (UNODC + UN Women)."),
        ("SPACE", "Euclid finds the most distant quasar, J1504+6252 "
                  "\u201cD\u00fan Aonghasa\u201d, 630m years after the Big Bang (ESA)."),
    ]
    bw = 476
    for i, (tag, text) in enumerate(briefs):
        bx = 24 + (i % 2) * (bw + gap)
        by = 888 + (i // 2) * 62
        d.text((bx, by), tag + ": ", font=SANS_B(17), fill=GOLD)
        tw = d.textlength(tag + ": ", font=SANS_B(17))
        para(d, bx + tw, by, text, SANS(17), bw - tw, 22, fill=(255, 255, 255))
    img.save("entry.png", format="PNG")


if __name__ == "__main__":
    main()
