#!/usr/bin/env python3
"""Generates the Overhear episode illustrations as hand-authored SVG.

One scene function per episode, all built from the same small library of
rounded shapes (heads, bodies, arms, props) so the set reads as one series.
Run:  python3 gen.py            -> writes <id>.svg next to this file
      python3 gen.py 06-knife   -> only that one
"""
import math, pathlib, sys

ART = pathlib.Path(__file__).resolve().parent
W = 1024

# ---------------------------------------------------------------- colours
INK = "#2E2A3A"        # eyes, mouths, small details
CREAM = "#FFF6EA"      # paper, cups, plates, chef whites
SKIN_L = "#F6D2B5"
SKIN_M = "#D9A074"
SKIN_D = "#9A6341"
BLUSH = "#F0808A"


def _hex(c):
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def mix(a, b, t):
    a, b = _hex(a), _hex(b)
    return "#%02X%02X%02X" % tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def darken(c, t):
    return mix(c, "#241C33", t)   # shade towards a deep indigo, not black


def lighten(c, t):
    return mix(c, "#FFFFFF", t)


# ---------------------------------------------------------------- builder
class S:
    def __init__(self, title):
        self.parts = []
        self.title = title

    def add(self, s):
        self.parts.append(s)

    def circle(self, cx, cy, r, fill, **kw):
        self.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}"{_attrs(kw)}/>')

    def ellipse(self, cx, cy, rx, ry, fill, **kw):
        self.add(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}"{_attrs(kw)}/>')

    def rect(self, x, y, w, h, fill, rx=0, **kw):
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx:.1f}" fill="{fill}"{_attrs(kw)}/>')

    def path(self, d, fill="none", stroke=None, sw=0, **kw):
        s = f'<path d="{d}" fill="{fill}"'
        if stroke:
            s += f' stroke="{stroke}" stroke-width="{sw:.1f}" stroke-linecap="round" stroke-linejoin="round"'
        self.add(s + _attrs(kw) + "/>")

    def line(self, x1, y1, x2, y2, stroke, sw, **kw):
        self.path(f"M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}", stroke=stroke, sw=sw, **kw)

    def poly(self, pts, stroke, sw, fill="none", **kw):
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
        self.path(d, fill=fill, stroke=stroke, sw=sw, **kw)

    def group(self, **kw):
        self.add(f"<g{_attrs(kw)}>")

    def end(self):
        self.add("</g>")

    def out(self):
        body = "\n".join(self.parts)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {W}" width="{W}" height="{W}">\n'
                f"<!-- Overhear episode art: {self.title}. Hand-authored SVG, no text. -->\n"
                f"{body}\n</svg>\n")


def _attrs(kw):
    out = ""
    for k, v in kw.items():
        k = k.replace("_", "-")
        if isinstance(v, float):
            v = f"{v:.2f}"
        out += f' {k}="{v}"'
    return out


# ---------------------------------------------------------------- stage
def stage(s, dom, spot=(512, 440, 400), ground_y=790):
    """Dominant-colour backdrop: flat field, soft lighter spotlight, darker floor."""
    s.rect(0, 0, W, W, dom)
    cx, cy, r = spot
    s.circle(cx, cy, r, lighten(dom, 0.16))
    s.ellipse(512, ground_y + 260, 820, 290, darken(dom, 0.18))


def shadow(s, cx, cy, rx, ry=None):
    s.ellipse(cx, cy, rx, ry or rx * 0.28, "#241C33", opacity=0.16)


# ---------------------------------------------------------------- people
def head(s, cx, cy, r, skin, hair="bob", hair_color="#4A2E26", face="smile",
         look=(0, 0), glasses=False, moustache=False, beard=False, brows=None,
         part=1):
    """Round head with hair and a simple face. `part` = 1 or -1 flips the fringe sweep."""
    hc = hair_color
    # --- back hair
    if hair in ("bob", "long"):
        s.circle(cx, cy - 0.05 * r, 1.12 * r, hc)
        s.rect(cx - 1.12 * r, cy - 0.05 * r, 2.24 * r, (0.95 if hair == "bob" else 1.5) * r, hc, rx=0.3 * r)
    elif hair == "bun":
        s.circle(cx, cy - 0.05 * r, 1.08 * r, hc)
        s.circle(cx - part * 0.25 * r, cy - 1.12 * r, 0.42 * r, hc)
    elif hair == "ponytail":
        s.circle(cx, cy - 0.05 * r, 1.08 * r, hc)
        s.ellipse(cx - part * 1.05 * r, cy + 0.35 * r, 0.33 * r, 0.75 * r, hc,
                  transform=f"rotate({part * 18} {cx - part * 1.05 * r:.1f} {cy + 0.35 * r:.1f})")
    elif hair == "short":
        s.circle(cx, cy - 0.06 * r, 1.07 * r, hc)
    elif hair == "curly":
        for a in range(-150, -29, 24):
            ang = math.radians(a)
            s.circle(cx + math.cos(ang) * 0.95 * r, cy + 0.02 * r + math.sin(ang) * 0.95 * r, 0.42 * r, hc)
        s.circle(cx, cy - 0.1 * r, 1.0 * r, hc)
    # --- head
    s.circle(cx, cy, r, skin)
    # ears
    s.circle(cx - 0.98 * r, cy + 0.08 * r, 0.17 * r, skin)
    s.circle(cx + 0.98 * r, cy + 0.08 * r, 0.17 * r, skin)
    # --- front hair
    if hair in ("bob", "long", "bun", "ponytail", "short"):
        y0 = cy - 0.22 * r
        x0 = math.sqrt(1 - 0.22 ** 2) * r
        if part > 0:
            d = (f"M{cx - x0:.1f} {y0:.1f} A{r:.1f} {r:.1f} 0 0 1 {cx + x0:.1f} {y0:.1f} "
                 f"Q{cx + 0.55 * r:.1f} {cy - 0.55 * r:.1f} {cx + 0.12 * r:.1f} {cy - 0.3 * r:.1f} "
                 f"Q{cx - 0.45 * r:.1f} {cy - 0.05 * r:.1f} {cx - x0:.1f} {y0:.1f} Z")
        else:
            d = (f"M{cx + x0:.1f} {y0:.1f} A{r:.1f} {r:.1f} 0 0 0 {cx - x0:.1f} {y0:.1f} "
                 f"Q{cx - 0.55 * r:.1f} {cy - 0.55 * r:.1f} {cx - 0.12 * r:.1f} {cy - 0.3 * r:.1f} "
                 f"Q{cx + 0.45 * r:.1f} {cy - 0.05 * r:.1f} {cx + x0:.1f} {y0:.1f} Z")
        s.path(d, fill=hc)
    elif hair == "toque":
        s.rect(cx - 0.98 * r, cy - 1.12 * r, 1.96 * r, 0.62 * r, CREAM, rx=0.18 * r)
        s.ellipse(cx, cy - 1.28 * r, 1.05 * r, 0.58 * r, CREAM)
        s.circle(cx - 0.55 * r, cy - 1.45 * r, 0.45 * r, CREAM)
        s.circle(cx + 0.5 * r, cy - 1.5 * r, 0.48 * r, CREAM)
        s.rect(cx - 0.98 * r, cy - 0.62 * r, 1.96 * r, 0.12 * r, mix(CREAM, INK, 0.12))
    elif hair == "cap":
        s.path(f"M{cx - 1.04 * r:.1f} {cy - 0.25 * r:.1f} A{1.04 * r:.1f} {1.04 * r:.1f} 0 0 1 {cx + 1.04 * r:.1f} {cy - 0.25 * r:.1f} Z", fill=hc)
        s.ellipse(cx + part * 0.85 * r, cy - 0.22 * r, 0.62 * r, 0.15 * r, darken(hc, 0.25))
    elif hair == "bald":
        pass
    # --- face
    ex, ey, er = 0.36 * r, cy - 0.04 * r, 0.085 * r
    lx, ly = look[0] * 0.08 * r, look[1] * 0.08 * r
    if face == "happy":          # closed happy eyes
        for sx in (-1, 1):
            x = cx + sx * ex
            s.path(f"M{x - 0.14 * r:.1f} {ey + 0.02 * r:.1f} Q{x:.1f} {ey - 0.2 * r:.1f} {x + 0.14 * r:.1f} {ey + 0.02 * r:.1f}",
                   stroke=INK, sw=0.07 * r)
    else:
        big = 1.3 if face in ("o", "shock") else 1.0
        s.circle(cx - ex + lx, ey + ly, er * big, INK)
        s.circle(cx + ex + lx, ey + ly, er * big, INK)
        if face in ("o", "shock"):
            s.circle(cx - ex + lx - 0.03 * r, ey + ly - 0.04 * r, er * 0.4, "#FFFFFF")
            s.circle(cx + ex + lx - 0.03 * r, ey + ly - 0.04 * r, er * 0.4, "#FFFFFF")
    if glasses:
        for sx in (-1, 1):
            s.circle(cx + sx * ex, ey, 0.27 * r, "none", stroke=INK, stroke_width=f"{0.055 * r:.1f}")
        s.line(cx - 0.09 * r, ey, cx + 0.09 * r, ey, INK, 0.05 * r)
    # brows
    if brows == "stern":
        s.line(cx - 0.6 * r, cy - 0.42 * r, cx - 0.18 * r, cy - 0.3 * r, INK, 0.065 * r)
        s.line(cx + 0.6 * r, cy - 0.42 * r, cx + 0.18 * r, cy - 0.3 * r, INK, 0.065 * r)
    elif brows == "worried":
        s.line(cx - 0.6 * r, cy - 0.3 * r, cx - 0.18 * r, cy - 0.4 * r, INK, 0.065 * r)
        s.line(cx + 0.6 * r, cy - 0.3 * r, cx + 0.18 * r, cy - 0.4 * r, INK, 0.065 * r)
    elif brows == "up":
        s.line(cx - 0.52 * r, cy - 0.42 * r, cx - 0.2 * r, cy - 0.45 * r, INK, 0.065 * r)
        s.line(cx + 0.52 * r, cy - 0.42 * r, cx + 0.2 * r, cy - 0.45 * r, INK, 0.065 * r)
    # blush
    s.circle(cx - 0.6 * r, cy + 0.3 * r, 0.16 * r, BLUSH, opacity=0.45)
    s.circle(cx + 0.6 * r, cy + 0.3 * r, 0.16 * r, BLUSH, opacity=0.45)
    # mouth
    my = cy + 0.42 * r
    if moustache:
        s.path(f"M{cx - 0.58 * r:.1f} {my - 0.02 * r:.1f} Q{cx - 0.3 * r:.1f} {my - 0.3 * r:.1f} {cx:.1f} {my - 0.08 * r:.1f} "
               f"Q{cx + 0.3 * r:.1f} {my - 0.3 * r:.1f} {cx + 0.58 * r:.1f} {my - 0.02 * r:.1f} "
               f"Q{cx + 0.3 * r:.1f} {my + 0.2 * r:.1f} {cx:.1f} {my + 0.05 * r:.1f} "
               f"Q{cx - 0.3 * r:.1f} {my + 0.2 * r:.1f} {cx - 0.58 * r:.1f} {my - 0.02 * r:.1f} Z", fill=hc)
        if face in ("o", "shock"):
            s.circle(cx, my + 0.32 * r, 0.14 * r, INK)
        elif face in ("smile", "happy", "grin"):
            s.path(f"M{cx - 0.25 * r:.1f} {my + 0.18 * r:.1f} Q{cx:.1f} {my + 0.45 * r:.1f} {cx + 0.25 * r:.1f} {my + 0.18 * r:.1f}",
                   stroke=INK, sw=0.065 * r)
    elif face in ("smile", "happy"):
        s.path(f"M{cx - 0.28 * r:.1f} {my - 0.06 * r:.1f} Q{cx:.1f} {my + 0.22 * r:.1f} {cx + 0.28 * r:.1f} {my - 0.06 * r:.1f}",
               stroke=INK, sw=0.065 * r)
    elif face == "grin":
        s.path(f"M{cx - 0.36 * r:.1f} {my - 0.08 * r:.1f} Q{cx:.1f} {my + 0.45 * r:.1f} {cx + 0.36 * r:.1f} {my - 0.08 * r:.1f} Z", fill=INK)
        s.path(f"M{cx - 0.2 * r:.1f} {my + 0.14 * r:.1f} Q{cx:.1f} {my + 0.3 * r:.1f} {cx + 0.2 * r:.1f} {my + 0.14 * r:.1f} Z", fill="#E26B7A")
    elif face == "o":
        s.ellipse(cx, my + 0.02 * r, 0.14 * r, 0.17 * r, INK)
    elif face == "shock":
        s.ellipse(cx, my + 0.05 * r, 0.2 * r, 0.26 * r, INK)
    elif face == "flat":
        s.line(cx - 0.22 * r, my, cx + 0.22 * r, my, INK, 0.065 * r)
    elif face == "hmm":
        s.path(f"M{cx - 0.22 * r:.1f} {my + 0.05 * r:.1f} Q{cx + 0.02 * r:.1f} {my - 0.12 * r:.1f} {cx + 0.25 * r:.1f} {my + 0.02 * r:.1f}",
               stroke=INK, sw=0.065 * r)
    if beard:
        s.ellipse(cx, cy + 0.72 * r, 0.42 * r, 0.28 * r, hc)
        s.path(f"M{cx - 0.2 * r:.1f} {cy + 0.5 * r:.1f} Q{cx:.1f} {cy + 0.7 * r:.1f} {cx + 0.2 * r:.1f} {cy + 0.5 * r:.1f}", stroke=INK, sw=0.065 * r)


def body(s, cx, top, w, h, color, rt=None, rb=None):
    rt = w * 0.32 if rt is None else rt
    rb = w * 0.12 if rb is None else rb
    x = cx - w / 2
    d = (f"M{x + rt:.1f} {top:.1f} H{x + w - rt:.1f} Q{x + w:.1f} {top:.1f} {x + w:.1f} {top + rt:.1f} "
         f"V{top + h - rb:.1f} Q{x + w:.1f} {top + h:.1f} {x + w - rb:.1f} {top + h:.1f} H{x + rb:.1f} "
         f"Q{x:.1f} {top + h:.1f} {x:.1f} {top + h - rb:.1f} V{top + rt:.1f} Q{x:.1f} {top:.1f} {x + rt:.1f} {top:.1f} Z")
    s.path(d, fill=color)


def neck(s, cx, y, r, skin):
    s.rect(cx - 0.28 * r, y - 0.2 * r, 0.56 * r, 0.5 * r, darken(skin, 0.12))


def arm(s, pts, color, w, skin=None, hand=True):
    s.poly(pts, color, w)
    if hand and skin:
        x, y = pts[-1]
        s.circle(x, y, w * 0.56, skin)


def legs(s, cx, top, gap, w, h, color, shoe):
    for sx in (-1, 1):
        x = cx + sx * gap
        s.rect(x - w / 2, top - 10, w, h, color, rx=w * 0.3)
        s.ellipse(x + sx * 0.1 * w, top + h, w * 0.75, w * 0.32, shoe)


def apron(s, cx, top, w, h, color):
    s.path(f"M{cx - w * 0.3:.1f} {top:.1f} H{cx + w * 0.3:.1f} V{top + h * 0.3:.1f} "
           f"Q{cx + w * 0.5:.1f} {top + h * 0.32:.1f} {cx + w * 0.5:.1f} {top + h * 0.5:.1f} V{top + h:.1f} "
           f"H{cx - w * 0.5:.1f} V{top + h * 0.5:.1f} Q{cx - w * 0.5:.1f} {top + h * 0.32:.1f} {cx - w * 0.3:.1f} {top + h * 0.3:.1f} Z",
           fill=color)


# ---------------------------------------------------------------- props
def sparkle(s, cx, cy, r, color, rot=0):
    d = (f"M{cx:.1f} {cy - r:.1f} Q{cx:.1f} {cy:.1f} {cx + r:.1f} {cy:.1f} Q{cx:.1f} {cy:.1f} {cx:.1f} {cy + r:.1f} "
         f"Q{cx:.1f} {cy:.1f} {cx - r:.1f} {cy:.1f} Q{cx:.1f} {cy:.1f} {cx:.1f} {cy - r:.1f} Z")
    s.path(d, fill=color, transform=f"rotate({rot} {cx:.1f} {cy:.1f})")


def steam(s, cx, y, h, color, n=3, gap=34, sw=12):
    for i in range(n):
        x = cx + (i - (n - 1) / 2) * gap
        dy = h * (0.75 if i % 2 else 1.0)
        s.path(f"M{x:.1f} {y:.1f} C{x - 22:.1f} {y - dy * 0.3:.1f} {x + 22:.1f} {y - dy * 0.6:.1f} {x:.1f} {y - dy:.1f}",
               stroke=color, sw=sw, opacity=0.85)


def cup(s, cx, y, w, h, color, liquid=None, handle=1):
    """Mug seen from the front; y is the bottom."""
    s.circle(cx + handle * (w / 2 + w * 0.06), y - h * 0.55, w * 0.28, "none", stroke=color, stroke_width=f"{w * 0.13:.1f}")
    s.rect(cx - w / 2, y - h, w, h, color, rx=w * 0.15)
    s.rect(cx - w / 2, y - h * 0.32, w, h * 0.32, darken(color, 0.08), rx=w * 0.15)
    s.rect(cx - w / 2, y - h * 0.32, w, h * 0.16, darken(color, 0.08))
    s.ellipse(cx, y - h, w / 2, w * 0.17, darken(color, 0.14))
    if liquid:
        s.ellipse(cx, y - h, w * 0.4, w * 0.12, liquid)


def bowl(s, cx, y, w, color, soup):
    s.path(f"M{cx - w / 2:.1f} {y - w * 0.3:.1f} Q{cx - w / 2:.1f} {y:.1f} {cx - w * 0.3:.1f} {y:.1f} H{cx + w * 0.3:.1f} Q{cx + w / 2:.1f} {y:.1f} {cx + w / 2:.1f} {y - w * 0.3:.1f} Z", fill=color)
    s.ellipse(cx, y - w * 0.3, w / 2, w * 0.15, darken(color, 0.1))
    s.ellipse(cx, y - w * 0.3, w * 0.43, w * 0.11, soup)


def spoon(s, x1, y1, x2, y2, color, w):
    s.line(x1, y1, x2, y2, color, w)
    s.ellipse(x2, y2, w * 1.6, w * 1.1, color, transform=f"rotate({math.degrees(math.atan2(y2 - y1, x2 - x1)) + 90:.0f} {x2:.1f} {y2:.1f})")


# ======================================================================
#                                SCENES
# ======================================================================
DOM = {
    "01-surprise": "#EC8DAE",
    "02-cafe": "#C98B5E",
    "03-directions": "#F2C14E",
    "04-market": "#6BB26D",
    "05-kitchen": "#6E86A0",
    "06-knife": "#2E9A96",
    "07-lunch": "#E2604F",
    "08-orders": "#F39A3C",
    "fr-01-agence": "#A58BD3",
    "fr-02-telephone": "#78B9E8",
    "fr-03-rendez-vous": "#86CDB2",
}

# recurring cast
ANYA = dict(skin=SKIN_L, hair="ponytail", hair_color="#C4623A")      # copper ponytail
MARINA = dict(skin=SKIN_M, hair="bob", hair_color="#3A2A2E")
CHEF = dict(skin=SKIN_L, hair="toque", hair_color="#4A3A3C", moustache=True)
LENA = dict(skin=SKIN_D, hair="curly", hair_color="#2A2024")
LEA = dict(skin=SKIN_L, hair="bob", hair_color="#E8C36A")            # blonde bob
ARLETTE = dict(skin=SKIN_M, hair="bun", hair_color="#DDD5D0", glasses=True)
HERVE = dict(skin=SKIN_D, hair="short", hair_color="#1F1A1E", beard=True)


def scene_01(s):
    dom = DOM["01-surprise"]
    stage(s, dom)
    box = "#FFF6EA"; ribbon = "#C7406F"; shirt_m = "#5E4B9E"; shirt_a = "#3FA7A0"
    lid = "#F8D9E4"
    # Marina (left) holding the big box
    mx, my, r = 330, 300, 100
    shadow(s, 340, 835, 180)
    shadow(s, 720, 835, 130)
    legs(s, mx, 700, 42, 60, 125, darken(shirt_m, 0.35), INK)
    body(s, mx, 400, 230, 320, shirt_m)
    neck(s, mx, 400, r, SKIN_M)
    # box: body, lid, ribbon, bow
    bx, by, bw, bh = 360, 530, 330, 210
    s.rect(bx - bw / 2, by, bw, bh, box, rx=16)
    s.rect(bx - bw / 2, by + bh - 40, bw, 40, darken(box, 0.1), rx=12)
    s.rect(bx - 24, by, 48, bh, ribbon)
    s.rect(bx - bw / 2 - 14, by - 70, bw + 28, 84, lid, rx=16)
    s.rect(bx - bw / 2 - 14, by + 2, bw + 28, 14, darken(lid, 0.15))
    s.rect(bx - 24, by - 70, 48, 84, ribbon)
    s.ellipse(bx - 62, by - 78, 56, 32, ribbon, transform=f"rotate(-18 {bx - 62} {by - 78})")
    s.ellipse(bx + 62, by - 78, 56, 32, ribbon, transform=f"rotate(18 {bx + 62} {by - 78})")
    s.path(f"M{bx - 20} {by - 70} L{bx - 60} {by - 10} L{bx - 30} {by - 20} Z", fill=ribbon)
    s.path(f"M{bx + 20} {by - 70} L{bx + 60} {by - 10} L{bx + 30} {by - 20} Z", fill=ribbon)
    s.circle(bx, by - 74, 26, darken(ribbon, 0.2))
    # Marina's arms hugging the box
    arm(s, [(mx - 100, 460), (mx - 160, 590), (bx - 110, 690)], shirt_m, 46, SKIN_M)
    arm(s, [(mx + 100, 460), (mx + 195, 590), (bx + 120, 690)], shirt_m, 46, SKIN_M)
    head(s, mx, my, r, face="smile", look=(1, 0), **MARINA)
    # Anya (right) surprised, hands up
    ax, ay = 720, 360
    legs(s, ax, 700, 40, 56, 125, darken(shirt_a, 0.35), INK)
    body(s, ax, 450, 200, 270, shirt_a)
    neck(s, ax, 450, r * 0.92, SKIN_L)
    arm(s, [(ax - 80, 510), (ax - 150, 470), (ax - 175, 390)], shirt_a, 40, SKIN_L)
    arm(s, [(ax + 80, 510), (ax + 160, 460), (ax + 180, 380)], shirt_a, 40, SKIN_L)
    head(s, ax, ay, r * 0.92, face="o", look=(-1, 0), brows="up", part=-1, **ANYA)
    # sparkles around the secret box
    for (x, y, rr, rot) in [(150, 470, 28, 0), (575, 400, 22, 20), (120, 610, 16, 10), (600, 540, 16, 0), (560, 300, 18, 0)]:
        sparkle(s, x, y, rr, "#FFF6EA", rot)


def scene_02(s):
    dom = DOM["02-cafe"]
    stage(s, dom, spot=(512, 420, 400))
    counter = "#5A3B2E"; apron_c = "#F2E3C9"; shirt = "#3F7F86"; shirt_a = "#C7406F"
    cupc = "#FFF6EA"; coffee = "#4A2C1E"; cake = "#F3C9A4"; jam = "#C7406F"
    # birthday bunting across the top (the cafe is one year old today)
    s.path("M40 120 Q512 230 984 120", stroke=darken(dom, 0.4), sw=8)
    for i in range(9):
        t = (i + 0.5) / 9
        x = 40 + t * 944
        y = 120 + 110 * 4 * t * (1 - t) * 0.5 + 110 * 0.5 * (1 - (1 - 2 * t) ** 2) * 0 + (2 * t * (1 - t)) * 110
        y = 120 + (1 - (2 * t - 1) ** 2) * 55
        col = [cupc, "#C7406F", shirt][i % 3]
        s.path(f"M{x - 34:.0f} {y:.0f} L{x + 34:.0f} {y:.0f} L{x:.0f} {y + 70:.0f} Z", fill=col)
    # barista behind the counter
    bx, by, r = 512, 390, 100
    body(s, bx, 490, 250, 200, shirt)
    apron(s, bx, 530, 230, 170, apron_c)
    neck(s, bx, 490, r, SKIN_M)
    arm(s, [(bx - 115, 550), (bx - 175, 600), (bx - 215, 630)], shirt, 44, SKIN_M)
    arm(s, [(bx + 115, 550), (bx + 170, 600), (bx + 200, 630)], shirt, 44, SKIN_M)
    head(s, bx, by, r, face="happy", part=1, skin=SKIN_M, hair="bun", hair_color="#3A2A2E")
    # counter
    s.rect(60, 640, 904, 260, counter, rx=26)
    s.rect(60, 640, 904, 34, lighten(counter, 0.25), rx=17)
    # big coffee on the counter (left)
    cup(s, 270, 640, 190, 165, cupc, liquid=coffee, handle=-1)
    steam(s, 270, 470, 120, "#FFF6EA", n=3, gap=44, sw=14)
    # cake slice with one candle (right)
    s.ellipse(650, 632, 150, 36, cupc)
    s.path("M570 628 L730 628 L730 556 Q650 520 570 556 Z", fill=cake)
    s.path("M570 628 L730 628 L730 604 L570 604 Z", fill=darken(cake, 0.18))
    s.path("M570 578 Q650 545 730 578 L730 556 Q650 520 570 556 Z", fill=jam)
    s.rect(642, 470, 16, 70, "#C7406F", rx=6)
    s.ellipse(650, 452, 12, 22, "#F2A23B")
    s.circle(650, 458, 5, "#FFF6EA")
    # Anya, in front of the counter at the right, delighted
    ax, ay = 880, 600
    body(s, ax, 690, 230, 240, shirt_a)
    neck(s, ax, 690, r, SKIN_L)
    head(s, ax, ay, r, face="o", look=(-1, 0), brows="up", part=-1, **ANYA)
    sparkle(s, 820, 420, 20, "#FFF6EA")
    sparkle(s, 580, 420, 14, "#FFF6EA")


def scene_03(s):
    dom = DOM["03-directions"]
    stage(s, dom, spot=(512, 380, 420), ground_y=760)
    sky = lighten(dom, 0.16); ochre = darken(dom, 0.45); shirt_a = "#3FA7A0"; shirt_g = "#C7406F"
    # museum in the background, top-left (columns + pediment)
    mx = 240
    s.path(f"M{mx - 210} 270 L{mx} 160 L{mx + 210} 270 Z", fill=ochre)
    s.rect(mx - 190, 268, 380, 30, ochre)
    for i in range(5):
        s.rect(mx - 165 + i * 76, 298, 40, 150, ochre, rx=6)
    s.rect(mx - 200, 444, 400, 28, ochre, rx=6)
    s.rect(mx - 215, 468, 430, 26, darken(ochre, 0.2), rx=6)
    # signpost: one big arrow pointing left, towards the museum
    px = 600
    s.rect(px - 11, 240, 22, 520, darken(dom, 0.55), rx=8)
    s.path(f"M{px + 160} 230 H{px - 70} L{px - 165} 290 L{px - 70} 350 H{px + 160} Q{px + 180} 350 {px + 180} 330 V250 Q{px + 180} 230 {px + 160} 230 Z",
           fill="#FFF6EA")
    shadow(s, 800, 825, 150)
    shadow(s, 250, 825, 140)
    # passer-by (right), a woman pointing left
    gx, gy, r = 800, 460, 96
    legs(s, gx, 700, 40, 56, 120, darken(shirt_g, 0.35), INK)
    body(s, gx, 550, 210, 230, shirt_g)
    neck(s, gx, 550, r, SKIN_D)
    arm(s, [(gx + 90, 610), (gx + 130, 690), (gx + 120, 720)], shirt_g, 42, SKIN_D)
    arm(s, [(gx - 95, 610), (gx - 190, 530), (gx - 290, 470)], shirt_g, 42, SKIN_D)
    head(s, gx, gy, r, face="smile", look=(-1, 0), part=1, skin=SKIN_D, hair="bob", hair_color="#1F1A1E")
    # Anya (left) with a map, unsure
    ax, ay = 250, 540
    legs(s, ax, 700, 40, 56, 120, darken(shirt_a, 0.35), INK)
    body(s, ax, 640, 200, 110, shirt_a)
    neck(s, ax, 640, r * 0.92, SKIN_L)
    arm(s, [(ax - 80, 690), (ax - 120, 740), (ax - 70, 760)], shirt_a, 40, SKIN_L)
    arm(s, [(ax + 80, 690), (ax + 120, 740), (ax + 70, 760)], shirt_a, 40, SKIN_L)
    s.path("M160 650 L250 636 L340 650 L340 760 L250 774 L160 760 Z", fill="#FFF6EA")
    s.path("M250 636 V774", stroke=darken("#FFF6EA", 0.15), sw=5)
    s.path("M180 680 Q220 720 255 700 T325 720", stroke=darken(dom, 0.4), sw=10)
    s.circle(318, 686, 12, "#C7406F")
    s.circle(ax - 70, 765, 22, SKIN_L)
    s.circle(ax + 70, 765, 22, SKIN_L)
    head(s, ax, ay, r * 0.92, face="hmm", look=(1, 0), brows="worried", part=-1, **ANYA)
    sparkle(s, 400, 560, 20, "#FFF6EA")


def scene_04(s):
    dom = DOM["04-market"]
    stage(s, dom, spot=(512, 400, 420))
    wood = "#8A5A3C"; apple = "#D8453F"; leaf = "#2F7A47"; shirt_s = "#3F5F9E"; shirt_a = "#C7406F"
    stripe = "#FFF6EA"
    # awning
    s.rect(80, 120, 864, 120, darken(dom, 0.35))
    for i in range(7):
        s.rect(80 + i * 124 + 62, 120, 62, 120, stripe)
    for i in range(14):
        s.circle(80 + 31 + i * 62, 242, 31, (stripe if i % 2 else darken(dom, 0.35)))
    s.rect(80, 120, 864, 14, darken(dom, 0.5))
    # seller behind stall
    sx, sy, r = 330, 420, 100
    body(s, sx, 520, 250, 200, shirt_s)
    apron(s, sx, 560, 230, 160, "#5E4B9E")
    neck(s, sx, 520, r, SKIN_M)
    head(s, sx, sy, r, face="smile", look=(1, 0), part=1, skin=SKIN_M, hair="cap", hair_color="#5E4B9E", moustache=True)
    # stall table
    s.rect(60, 640, 904, 60, wood, rx=20)
    s.rect(60, 690, 904, 200, darken(wood, 0.2), rx=20)
    s.rect(120, 720, 784, 20, lighten(wood, 0.15), rx=10)
    s.rect(120, 800, 784, 20, lighten(wood, 0.15), rx=10)
    # crates of apples
    def crate(cx, y, w):
        s.rect(cx - w / 2, y - 70, w, 70, lighten(wood, 0.2), rx=10)
        s.rect(cx - w / 2 + 14, y - 58, w - 28, 10, darken(wood, 0.1), rx=5)
        rows = [(5, -70), (4, -112), (3, -152), (2, -190)]
        for n, dy in rows:
            for i in range(n):
                x = cx + (i - (n - 1) / 2) * 50
                s.circle(x, y + dy, 28, apple)
                s.circle(x - 8, y + dy - 9, 8, lighten(apple, 0.4), opacity=0.7)
    crate(185, 640, 250)
    crate(440, 640, 250)
    # seller offering an apple, in the clear space over the stall
    arm(s, [(sx + 110, 580), (sx + 220, 580), (sx + 300, 540)], shirt_s, 44, SKIN_M)
    s.circle(sx + 325, 505, 38, apple)
    s.circle(sx + 313, 493, 10, lighten(apple, 0.4), opacity=0.7)
    s.rect(sx + 322, 460, 6, 20, leaf, rx=3)
    s.ellipse(sx + 346, 468, 18, 9, leaf, transform=f"rotate(-30 {sx + 346} 468)")
    # Anya right, tasting one
    ax, ay = 830, 440
    body(s, ax, 540, 220, 200, shirt_a)
    neck(s, ax, 540, r * 0.92, SKIN_L)
    arm(s, [(ax - 90, 600), (ax - 150, 560), (ax - 120, 500)], shirt_a, 40, SKIN_L)
    s.circle(ax - 105, 478, 32, apple)
    s.circle(ax - 115, 468, 9, lighten(apple, 0.4), opacity=0.7)
    s.rect(ax - 108, 440, 5, 16, leaf, rx=2)
    head(s, ax, ay, r * 0.92, face="happy", part=-1, **ANYA)
    sparkle(s, 940, 360, 18, "#FFF6EA")
    sparkle(s, 700, 330, 14, "#FFF6EA")


def scene_05(s):
    dom = DOM["05-kitchen"]
    stage(s, dom, spot=(512, 420, 410))
    steel = darken(dom, 0.3); jacket = "#FFF6EA"; shirt_a = "#C7406F"; soup = "#E07A3A"
    # hanging pots on a rail
    s.rect(100, 120, 824, 14, darken(dom, 0.5), rx=7)
    for x, w in [(200, 110), (380, 80), (560, 120), (760, 90)]:
        s.line(x, 134, x, 170, darken(dom, 0.5), 6)
        s.rect(x - w / 2, 170, w, w * 0.7, steel, rx=12)
        s.rect(x - w / 2, 170, w, 14, lighten(steel, 0.25), rx=7)
    # counter
    s.rect(60, 700, 904, 200, steel, rx=24)
    s.rect(60, 700, 904, 30, lighten(steel, 0.3), rx=15)
    # chef (right): stern, tasting
    cx, cy, r = 700, 400, 110
    body(s, cx, 510, 300, 220, jacket)
    s.circle(cx - 40, 560, 10, INK); s.circle(cx - 40, 620, 10, INK); s.circle(cx + 10, 560, 10, INK); s.circle(cx + 10, 620, 10, INK)
    neck(s, cx, 510, r, SKIN_L)
    arm(s, [(cx - 130, 570), (cx - 210, 520), (cx - 160, 450)], jacket, 50, SKIN_L)
    spoon(s, cx - 160, 455, cx - 95, 478, "#CFD9E4", 16)
    arm(s, [(cx + 130, 570), (cx + 180, 640), (cx + 150, 690)], jacket, 50, SKIN_L)
    head(s, cx, cy, r, face="hmm", look=(-1, 0), brows="stern", part=1, **CHEF)
    # Anya (left) nervous, holding the bowl of solyanka
    ax, ay = 300, 430
    body(s, ax, 540, 230, 200, shirt_a)
    neck(s, ax, 540, r * 0.92, SKIN_L)
    arm(s, [(ax - 95, 600), (ax - 70, 690), (ax + 10, 650)], shirt_a, 42, SKIN_L)
    arm(s, [(ax + 95, 600), (ax + 170, 680), (ax + 230, 650)], shirt_a, 42, SKIN_L)
    bowl(s, ax + 130, 700, 230, "#FFF6EA", soup)
    for (dx, dy) in [(-40, -72), (10, -62), (55, -75), (-10, -84)]:
        s.circle(ax + 130 + dx, 700 + dy, 9, "#2F7A47")
    steam(s, ax + 130, 615, 120, "#FFF6EA", n=3, gap=42, sw=14)
    head(s, ax, ay, r * 0.92, face="smile", look=(1, 0), brows="worried", part=-1, **ANYA)
    # a nervous sweat drop
    s.path(f"M{ax + 105} 345 Q{ax + 122} 380 {ax + 105} 392 Q{ax + 88} 380 {ax + 105} 345 Z", fill="#CFE6F5")


def scene_06(s):
    dom = DOM["06-knife"]
    stage(s, dom, spot=(512, 440, 420))
    board = "#C9956A"; fish = "#CFD9E4"; fish_d = "#9FB0C2"; blade = "#E9EEF2"; handle = "#3A2A2E"; jacket = "#FFF6EA"; shirt_a = "#C7406F"
    # counter
    s.rect(60, 690, 904, 210, darken(dom, 0.35), rx=24)
    s.rect(60, 690, 904, 30, lighten(darken(dom, 0.35), 0.3), rx=15)
    # chef (left) shocked, hands on toque
    cx, cy, r = 250, 400, 108
    body(s, cx, 510, 290, 200, jacket)
    s.circle(cx - 40, 560, 10, INK); s.circle(cx - 40, 620, 10, INK); s.circle(cx + 10, 560, 10, INK); s.circle(cx + 10, 620, 10, INK)
    neck(s, cx, 510, r, SKIN_L)
    arm(s, [(cx - 125, 570), (cx - 210, 440), (cx - 100, 300)], jacket, 50, SKIN_L)
    arm(s, [(cx + 125, 570), (cx + 210, 440), (cx + 110, 300)], jacket, 50, SKIN_L)
    head(s, cx, cy, r, face="shock", look=(1, 0), brows="up", part=1, **CHEF)
    # Anya (right) pointing at the fish
    ax, ay = 800, 430
    body(s, ax, 540, 220, 180, shirt_a)
    neck(s, ax, 540, r * 0.9, SKIN_L)
    arm(s, [(ax + 90, 600), (ax + 120, 680), (ax + 90, 700)], shirt_a, 42, SKIN_L)
    arm(s, [(ax - 90, 600), (ax - 170, 580), (ax - 230, 560)], shirt_a, 42, SKIN_L)
    head(s, ax, ay, r * 0.9, face="grin", look=(-1, 0), part=-1, **ANYA)
    # cutting board
    s.ellipse(512, 690, 300, 70, board)
    s.ellipse(512, 680, 300, 70, lighten(board, 0.15))
    # big fish
    fx, fy = 500, 640
    s.path(f"M{fx + 180} {fy} L{fx + 300} {fy - 80} L{fx + 280} {fy} L{fx + 300} {fy + 80} Z", fill=fish_d)   # tail
    s.ellipse(fx, fy, 230, 95, fish)
    s.path(f"M{fx - 60} {fy - 90} Q{fx + 40} {fy - 150} {fx + 110} {fy - 70}", fill=fish_d)       # dorsal fin
    s.ellipse(fx + 30, fy + 50, 60, 22, fish_d, transform=f"rotate(20 {fx + 30} {fy + 50})")
    s.path(f"M{fx + 80} {fy - 85} Q{fx + 110} {fy} {fx + 80} {fy + 85}", stroke=fish_d, sw=10)    # gill
    for i in range(3):
        s.path(f"M{fx - 150 + i * 60} {fy - 40} Q{fx - 120 + i * 60} {fy} {fx - 150 + i * 60} {fy + 40}", stroke=fish_d, sw=7)
    s.circle(fx - 150, fy - 20, 20, "#FFFFFF")
    s.circle(fx - 146, fy - 18, 11, INK)
    s.path(f"M{fx - 215} {fy + 15} Q{fx - 190} {fy + 30} {fx - 165} {fy + 20}", stroke=fish_d, sw=8)
    # the knife, stuck in the fish, blade down
    kx = fx + 10
    s.path(f"M{kx - 22} {fy - 40} L{kx + 22} {fy - 40} L{kx + 18} {fy - 170} L{kx - 18} {fy - 170} Z", fill=blade)
    s.rect(kx - 34, fy - 330, 68, 170, handle, rx=24)
    s.rect(kx - 40, fy - 180, 80, 26, "#B08A4A", rx=10)
    s.circle(kx, fy - 280, 10, "#B08A4A"); s.circle(kx, fy - 220, 10, "#B08A4A")
    # shock marks
    for (x, y, rr) in [(160, 240, 14), (120, 300, 10), (380, 230, 12)]:
        sparkle(s, x, y, rr, "#FFF6EA")


def scene_07(s):
    dom = DOM["07-lunch"]
    stage(s, dom, spot=(512, 430, 410))
    table = "#8A5A3C"; pot = "#3E5468"; soup = "#F2B544"; jacket = "#FFF6EA"; shirt_a = "#3FA7A0"; herb = "#2F7A47"
    # table
    s.rect(40, 700, 944, 200, table, rx=24)
    s.rect(40, 700, 944, 30, lighten(table, 0.25), rx=15)
    # Anya (left) behind the pot, proud, ladle in hand
    ax, ay, r = 215, 400, 100
    body(s, ax, 510, 240, 220, shirt_a)
    neck(s, ax, 510, r, SKIN_L)
    arm(s, [(ax - 105, 580), (ax - 150, 650), (ax - 120, 700)], shirt_a, 42, SKIN_L)
    arm(s, [(ax + 105, 580), (ax + 180, 520), (ax + 235, 455)], shirt_a, 42, SKIN_L)
    head(s, ax, ay, r, face="happy", part=-1, **ANYA)
    # big pot of soup
    px, py = 440, 700
    s.circle(px - 215, py - 160, 38, "none", stroke=darken(pot, 0.2), stroke_width="24")
    s.circle(px + 215, py - 160, 38, "none", stroke=darken(pot, 0.2), stroke_width="24")
    s.rect(px - 190, py - 250, 380, 250, pot, rx=40)
    s.rect(px - 190, py - 250, 380, 70, lighten(pot, 0.12), rx=34)
    s.rect(px - 190, py - 215, 380, 35, lighten(pot, 0.12))
    s.ellipse(px, py - 250, 190, 52, darken(pot, 0.15))
    s.ellipse(px, py - 250, 172, 42, soup)
    for (dx, dy) in [(-90, -8), (-30, 6), (40, -10), (100, 4), (10, -22), (-60, 14)]:
        s.circle(px + dx, py - 250 + dy, 9, herb)
    steam(s, px, py - 305, 170, "#FFF6EA", n=3, gap=70, sw=16)
    # ladle
    s.line(ax + 240, 450, px - 40, py - 245, "#CFD9E4", 14)
    s.ellipse(px - 40, py - 245, 40, 26, "#CFD9E4")
    # chef (right), delighted, holding his empty bowl out for seconds
    cx, cy = 790, 380
    body(s, cx, 490, 300, 240, jacket)
    s.circle(cx - 40, 540, 10, INK); s.circle(cx - 40, 600, 10, INK); s.circle(cx + 10, 540, 10, INK); s.circle(cx + 10, 600, 10, INK)
    neck(s, cx, 490, r * 1.08, SKIN_L)
    arm(s, [(cx - 135, 560), (cx - 200, 640), (cx - 120, 690)], jacket, 50, SKIN_L)
    arm(s, [(cx + 135, 560), (cx + 190, 640), (cx + 110, 690)], jacket, 50, SKIN_L)
    bowl(s, cx - 5, 700, 230, "#FFF6EA", darken("#FFF6EA", 0.1))
    s.path(f"M{cx - 118} 650 Q{cx - 5} 690 {cx + 108} 650", stroke=shirt_a, sw=14)
    s.circle(cx - 120, 690, 26, SKIN_L); s.circle(cx + 110, 690, 26, SKIN_L)
    head(s, cx, cy, r * 1.08, face="grin", look=(-1, 0), part=1, **CHEF)
    for (x, y, rr) in [(920, 230, 22), (960, 330, 14), (870, 300, 12)]:
        sparkle(s, x, y, rr, "#FFF6EA")


def scene_08(s):
    dom = DOM["08-orders"]
    stage(s, dom, spot=(512, 430, 410))
    rail = darken(dom, 0.45); ticket = "#FFF6EA"; shirt_a = "#3FA7A0"; shirt_l = "#5E4B9E"; steel = darken(dom, 0.35)
    # ticket rail with a crowd of order slips
    s.rect(60, 150, 904, 16, rail, rx=8)
    for i, (x, rot, h) in enumerate([(120, -8, 150), (210, 6, 170), (300, -4, 140), (390, 9, 180), (480, -6, 150), (570, 4, 170),
                                      (660, -9, 150), (750, 5, 160), (840, -5, 180), (920, 7, 140)]):
        s.group(transform=f"rotate({rot} {x} 160)")
        s.rect(x - 42, 160, 84, h, ticket, rx=8)
        for k in range(3):
            s.rect(x - 28, 190 + k * 30, 56 - k * 12, 9, darken(dom, 0.2), rx=4)
        s.end()
        s.rect(x - 10, 146, 20, 26, rail, rx=6)
    # a couple of loose tickets fluttering
    for (x, y, rot) in [(150, 430, -25), (880, 400, 20)]:
        s.group(transform=f"rotate({rot} {x} {y})")
        s.rect(x - 36, y - 55, 72, 110, ticket, rx=8)
        for k in range(3):
            s.rect(x - 24, y - 35 + k * 26, 48 - k * 10, 8, darken(dom, 0.2), rx=4)
        s.end()
    # pass counter
    s.rect(60, 700, 904, 200, steel, rx=24)
    s.rect(60, 700, 904, 30, lighten(steel, 0.3), rx=15)
    # Anya (centre-left) overwhelmed, hands up
    ax, ay, r = 370, 430, 100
    body(s, ax, 540, 240, 190, shirt_a)
    neck(s, ax, 540, r, SKIN_L)
    arm(s, [(ax - 105, 600), (ax - 190, 520), (ax - 170, 420)], shirt_a, 42, SKIN_L)
    arm(s, [(ax + 105, 600), (ax + 170, 530), (ax + 150, 440)], shirt_a, 42, SKIN_L)
    head(s, ax, ay, r, face="shock", look=(0, -1), brows="worried", part=-1, **ANYA)
    s.path(f"M{ax + 118} 340 Q{ax + 138} 380 {ax + 118} 392 Q{ax + 98} 380 {ax + 118} 340 Z", fill="#CFE6F5")
    s.path(f"M{ax - 150} 360 Q{ax - 135} 395 {ax - 150} 405 Q{ax - 165} 395 {ax - 150} 360 Z", fill="#CFE6F5")
    # Lena (right), calm, bringing a plate of fish
    lx, ly = 760, 440
    body(s, lx, 550, 240, 180, shirt_l)
    neck(s, lx, 550, r, SKIN_D)
    arm(s, [(lx - 105, 610), (lx - 170, 660), (lx - 220, 660)], shirt_l, 42, SKIN_D)
    arm(s, [(lx + 105, 610), (lx + 150, 670), (lx + 120, 700)], shirt_l, 42, SKIN_D)
    s.ellipse(lx - 250, 650, 120, 34, "#FFF6EA")
    s.ellipse(lx - 250, 636, 70, 24, "#CFD9E4")
    s.path(f"M{lx - 180} 636 L{lx - 150} 618 L{lx - 150} 654 Z", fill="#9FB0C2")
    s.circle(lx - 290, 634, 5, INK)
    head(s, lx, ly, r, face="smile", look=(-1, 0), part=1, **LENA)


def scene_fr01(s):
    dom = DOM["fr-01-agence"]
    stage(s, dom, spot=(512, 420, 410))
    desk = "#4A3360"; wall = darken(dom, 0.3); door = lighten(dom, 0.3); pen = "#2E2A3A"; plant = "#5FB37A"; shirt_l = "#3FA7A0"; shirt_a = "#C7406F"
    # door frame behind Léa
    s.rect(110, 110, 300, 620, wall, rx=16)
    s.rect(135, 135, 250, 595, door, rx=10)
    s.circle(355, 440, 12, wall)
    # desk at right with plant
    s.rect(500, 600, 470, 300, desk, rx=26)
    s.rect(500, 600, 470, 30, lighten(desk, 0.3), rx=15)
    s.rect(860, 500, 70, 100, "#B0784F", rx=14)
    for (dx, dy, rot) in [(-30, -60, -30), (0, -90, 0), (30, -60, 30), (-10, -40, -10), (15, -45, 15)]:
        s.ellipse(895 + dx, 500 + dy, 22, 46, plant, transform=f"rotate({rot} {895 + dx} {500 + dy})")
    # Arlette (right) behind desk, handing a pen
    ax, ay, r = 720, 380, 98
    body(s, ax, 480, 240, 170, shirt_a)
    neck(s, ax, 480, r, SKIN_M)
    arm(s, [(ax + 100, 540), (ax + 160, 600), (ax + 130, 620)], shirt_a, 42, SKIN_M)
    arm(s, [(ax - 100, 540), (ax - 190, 520), (ax - 250, 470)], shirt_a, 42, SKIN_M)
    head(s, ax, ay, r, face="smile", look=(-1, 0), part=1, **ARLETTE)
    # the pen (big, between them)
    s.group(transform="rotate(-35 455 470)")
    s.rect(455 - 110, 470 - 22, 220, 44, pen, rx=16)
    s.rect(455 + 60, 470 - 14, 60, 28, "#C9A24A", rx=8)
    s.path("M345 470 L300 458 L300 482 Z", fill="#C9A24A")
    s.end()
    # Léa (left) new, with a bag, a bit nervous
    lx, ly = 290, 410
    shadow(s, 290, 835, 150)
    legs(s, lx, 700, 40, 56, 120, darken(shirt_l, 0.35), INK)
    body(s, lx, 500, 210, 220, shirt_l)
    neck(s, lx, 500, r * 0.95, SKIN_L)
    s.rect(130, 560, 110, 130, "#B0784F", rx=20)
    s.path("M150 560 Q185 500 220 560", stroke="#B0784F", sw=12)
    arm(s, [(lx - 90, 560), (lx - 120, 640), (lx - 100, 680)], shirt_l, 40, SKIN_L)
    arm(s, [(lx + 90, 560), (lx + 150, 520), (lx + 190, 480)], shirt_l, 40, SKIN_L)
    head(s, lx, ly, r * 0.95, face="smile", look=(1, 0), brows="worried", part=-1, **LEA)
    sparkle(s, 480, 300, 20, "#FFF6EA")
    sparkle(s, 560, 250, 14, "#FFF6EA")


def scene_fr02(s):
    dom = DOM["fr-02-telephone"]
    stage(s, dom, spot=(512, 430, 410))
    desk = "#FFF6EA"; phone = "#2E3A5E"; shirt_l = "#C7406F"; clockc = "#FFF6EA"
    # wall clock at ten o'clock
    s.circle(800, 230, 95, clockc)
    s.circle(800, 230, 95, "none", stroke=darken(dom, 0.4), stroke_width="14")
    for a in range(0, 360, 90):
        rad = math.radians(a)
        s.circle(800 + math.cos(rad) * 70, 230 + math.sin(rad) * 70, 7, darken(dom, 0.4))
    s.line(800, 230, 800, 180, INK, 10)                                   # hour -> twelve? no: ten
    s.line(800, 230, 800 - 52, 200, INK, 10)
    s.circle(800, 230, 9, INK)
    # desk
    s.rect(60, 640, 904, 260, desk, rx=26)
    s.rect(60, 640, 904, 30, darken(desk, 0.1), rx=15)
    # phone base with curly cord
    s.rect(560, 560, 220, 90, phone, rx=22)
    s.rect(590, 575, 160, 20, lighten(phone, 0.2), rx=10)
    for k in range(3):
        for j in range(3):
            s.circle(620 + j * 50, 612 + k * 0, 9, lighten(phone, 0.35))
    s.path("M570 600 C 540 560 520 600 500 560 S 460 560 450 520 S 420 520 410 470", stroke=phone, sw=12)
    # Léa at the desk holding the handset
    lx, ly, r = 330, 400, 108
    body(s, lx, 520, 260, 160, shirt_l)
    neck(s, lx, 520, r, SKIN_L)
    arm(s, [(lx - 110, 590), (lx - 170, 640), (lx - 150, 660)], shirt_l, 44, SKIN_L)
    head(s, lx, ly, r, face="smile", look=(1, 0), part=1, **LEA)
    # handset held up to the ear: earpiece at the ear, mouthpiece by the chin
    hx, hy = lx + 112, 420
    s.group(transform=f"rotate(8 {hx} {hy})")
    s.rect(hx - 22, hy - 110, 44, 220, phone, rx=22)
    s.ellipse(hx, hy - 118, 46, 34, phone)
    s.ellipse(hx, hy + 118, 46, 34, phone)
    s.end()
    arm(s, [(lx + 115, 590), (lx + 180, 540), (hx + 6, hy + 10)], shirt_l, 44, SKIN_L)
    s.circle(hx + 6, hy + 10, 28, SKIN_L)
    # sound arcs: the caller's voice coming out of the earpiece
    for i, rr in enumerate([70, 120, 170]):
        s.path(f"M{hx + 40:.0f} {hy - 118 - rr * 0.7:.0f} A{rr} {rr} 0 0 1 {hx + 40 + rr * 0.6:.0f} {hy - 118 + rr * 0.35:.0f}",
               stroke="#FFF6EA", sw=16)


def scene_fr03(s):
    dom = DOM["fr-03-rendez-vous"]
    stage(s, dom, spot=(512, 430, 410))
    desk = "#4A3360"; cal = "#FFF6EA"; mark = "#C7406F"; cupc = "#FFF6EA"; coffee = "#4A2C1E"; shirt_l = "#C7406F"; shirt_h = "#2E3A5E"
    # wall calendar, one day marked
    cx0, cy0 = 512, 230
    s.rect(cx0 - 170, cy0 - 120, 340, 250, cal, rx=18)
    s.rect(cx0 - 170, cy0 - 120, 340, 56, mark, rx=18)
    s.rect(cx0 - 170, cy0 - 90, 340, 26, mark)
    s.circle(cx0 - 90, cy0 - 120, 14, darken(cal, 0.15)); s.circle(cx0 + 90, cy0 - 120, 14, darken(cal, 0.15))
    for row in range(3):
        for col in range(6):
            x = cx0 - 125 + col * 50; y = cy0 - 20 + row * 52
            s.rect(x - 16, y - 14, 32, 28, darken(cal, 0.1), rx=6)
    s.circle(cx0 - 25, cy0 + 32, 26, mark)
    # desk
    s.rect(60, 650, 904, 250, desk, rx=26)
    s.rect(60, 650, 904, 30, lighten(desk, 0.3), rx=15)
    # Hervé (left), delighted, hands up
    hx, hy, r = 260, 420, 100
    body(s, hx, 530, 250, 160, shirt_h)
    s.path(f"M{hx} 530 L{hx - 18} 560 L{hx} 640 L{hx + 18} 560 Z", fill="#C9A24A")     # tie
    neck(s, hx, 530, r, SKIN_D)
    arm(s, [(hx - 105, 590), (hx - 190, 520), (hx - 180, 430)], shirt_h, 42, SKIN_D)
    arm(s, [(hx + 105, 590), (hx + 170, 640), (hx + 190, 650)], shirt_h, 42, SKIN_D)
    head(s, hx, hy, r, face="grin", look=(1, 0), brows="up", part=1, **HERVE)
    # Léa (right) with two coffees on a tray
    lx, ly = 750, 430
    body(s, lx, 540, 240, 160, shirt_l)
    neck(s, lx, 540, r, SKIN_L)
    arm(s, [(lx - 105, 600), (lx - 190, 640), (lx - 230, 610)], shirt_l, 42, SKIN_L)
    arm(s, [(lx + 105, 600), (lx + 140, 660), (lx + 110, 700)], shirt_l, 42, SKIN_L)
    s.rect(lx - 300, 600, 300, 22, darken(cupc, 0.2), rx=11)
    cup(s, lx - 230, 600, 100, 85, cupc, liquid=coffee, handle=-1)
    cup(s, lx - 90, 600, 100, 85, cupc, liquid=coffee, handle=1)
    steam(s, lx - 230, 510, 70, "#FFF6EA", n=2, gap=28, sw=10)
    steam(s, lx - 90, 510, 70, "#FFF6EA", n=2, gap=28, sw=10)
    head(s, lx, ly, r, face="happy", part=-1, **LEA)
    for (x, y, rr) in [(120, 250, 22), (180, 330, 14), (860, 300, 18), (910, 240, 12)]:
        sparkle(s, x, y, rr, "#FFF6EA")


SCENES = {
    "01-surprise": scene_01, "02-cafe": scene_02, "03-directions": scene_03, "04-market": scene_04,
    "05-kitchen": scene_05, "06-knife": scene_06, "07-lunch": scene_07, "08-orders": scene_08,
    "fr-01-agence": scene_fr01, "fr-02-telephone": scene_fr02, "fr-03-rendez-vous": scene_fr03,
}

if __name__ == "__main__":
    ids = sys.argv[1:] or list(SCENES)
    for eid in ids:
        s = S(eid)
        SCENES[eid](s)
        (ART / f"{eid}.svg").write_text(s.out())
        print("wrote", eid)
