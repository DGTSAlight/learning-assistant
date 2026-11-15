#!/usr/bin/env python3
"""Draw an illustrative u_d waveform comparison as SVG, standard library only.

Example:
    python draw-waveform-example.py --out figure-waveform-example.svg
    python draw-waveform-example.py --alpha-deg 30 --out /abs/path/figure.svg

The sketch uses the ideal single-phase full-bridge controlled rectifier model:
no commutation overlap, no device voltage drops, and (for the lower trace)
continuous load current. It is a teaching sketch, not a textbook figure.
"""

import argparse
import math
import os
import re
import xml.etree.ElementTree as ET

W, H = 900, 590
X0, XW = 95, 745
AMP = 50.0
TRACKS = [
    ("u2  (supply voltage)", 150.0, "#7a7a7a"),
    ("u_d  resistive load", 310.0, "#185fa5"),
    ("u_d  large inductor, continuous current", 470.0, "#a32d2d"),
]

AXIS = "#3d3d3d"
GRID = "#b9b9b9"
TEXT = "#1f1f1f"
MUTED = "#666666"
SHADE = "#f7e4e2"


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def px(theta):
    return X0 + theta / (2 * math.pi) * XW


def py(zero, value):
    return zero - value * AMP


def rich(s):
    """Render u_d, U_i, i_L as real SVG subscripts instead of bare underscores."""
    return re.sub(r"_([A-Za-z])",
                  lambda m: ('<tspan baseline-shift="sub" font-size="0.72em">%s</tspan>'
                             % m.group(1)),
                  esc(s))


def txt(x, y, s, size=13, fill=TEXT, anchor="start", weight="400"):
    return ('<text x="%.1f" y="%.1f" font-family="system-ui, sans-serif" '
            'font-size="%d" font-weight="%s" fill="%s" text-anchor="%s">%s</text>'
            % (x, y, size, weight, fill, anchor, rich(s)))


def line(x1, y1, x2, y2, color=AXIS, width=1.0, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
            'stroke-width="%.1f"%s/>' % (x1, y1, x2, y2, color, width, d))


def polyline(points, zero, color, width=2.2, dash=None):
    coords = " ".join("%.1f,%.1f" % (px(t), py(zero, v)) for t, v in points)
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<polyline points="%s" fill="none" stroke="%s" stroke-width="%.1f" '
            'stroke-linejoin="round"%s/>' % (coords, color, width, d))


def ud_resistive(theta, alpha):
    if theta < alpha:
        return 0.0
    if theta <= math.pi:
        return math.sin(theta)
    if theta < math.pi + alpha:
        return 0.0
    return -math.sin(theta)


def ud_inductive(theta, alpha):
    if theta < alpha:
        return -math.sin(theta)
    if theta < math.pi + alpha:
        return math.sin(theta)
    return -math.sin(theta)


def sample(fn, alpha, bounds):
    """Sample one branch per interval so jumps at boundaries stay visible."""
    out = []
    for lo, hi in zip(bounds[:-1], bounds[1:]):
        n = max(12, int((hi - lo) / (2 * math.pi) * 420))
        pts = []
        for i in range(n):
            t = lo + (hi - lo) * i / (n - 1)
            inner = min(max(t, lo + 1e-9), hi - 1e-9)
            pts.append((t, fn(inner, alpha)))
        out.append(pts)
    return out


def build(alpha_deg):
    alpha = math.radians(alpha_deg)
    bounds = [0.0, alpha, math.pi, math.pi + alpha, 2 * math.pi]
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
             'width="%d" height="%d" role="img">' % (W, H, W, H),
             '<title>Ideal output voltage waveforms of a single-phase full-bridge '
             'controlled rectifier</title>',
             '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H)]

    parts.append(txt(28, 32, "Single-phase full-bridge controlled rectifier - output voltage",
                     16, TEXT, weight="500"))
    parts.append(txt(28, 52, "firing angle alpha = %d deg" % alpha_deg, 12, MUTED))

    # Negative u_d intervals on the inductive trace.
    z_ind = TRACKS[2][1]
    for lo, hi in ((0.0, alpha), (math.pi, math.pi + alpha)):
        parts.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>'
                     % (px(lo), z_ind, px(hi) - px(lo), AMP, SHADE))

    # Vertical reference lines at the firing angle, the zero crossing, and commutation.
    for t in (alpha, math.pi, math.pi + alpha):
        parts.append(line(px(t), 80, px(t), 530, GRID, 1.0, "4 4"))

    # One horizontal zero axis per track; labels sit above each trace.
    for label, zero, color in TRACKS:
        parts.append(line(X0, zero, X0 + XW, zero, AXIS, 1.0))
        parts.append(txt(X0, zero - AMP - 12, label, 13, color, weight="500"))

    # Supply voltage, dashed for reference.
    supply = [(2 * math.pi * i / 420.0, math.sin(2 * math.pi * i / 420.0))
              for i in range(421)]
    parts.append(polyline(supply, TRACKS[0][1], TRACKS[0][2], 1.8, "5 4"))

    # Output voltage traces.
    for fn, (label, zero, color) in ((ud_resistive, TRACKS[1]),
                                     (ud_inductive, TRACKS[2])):
        segs = sample(fn, alpha, bounds)
        for seg in segs:
            parts.append(polyline(seg, zero, color))
        # Instantaneous jumps at triggering / commutation.
        for t in (alpha, math.pi, math.pi + alpha):
            left = fn(t - 1e-9, alpha)
            right = fn(t + 1e-9, alpha)
            if abs(left - right) > 0.02:
                parts.append(line(px(t), py(zero, left), px(t), py(zero, right),
                                  color, 1.4, "3 3"))

    # Annotations on the shape information.
    parts.append(txt(px(math.pi) + 8, TRACKS[1][1] - 12, "u_d = 0", 12, MUTED))
    parts.append(txt(px(math.pi) + 8, TRACKS[2][1] + 44, "negative u_d", 12, "#a32d2d"))
    parts.append(txt(px(math.pi + alpha) + 6, TRACKS[2][1] - 14, "commutation",
                     12, MUTED))

    # Time axis ticks.
    ticks = [(0.0, "0"), (alpha, "alpha (%d deg)" % alpha_deg),
             (math.pi, "pi (180 deg)"), (math.pi + alpha, "pi+alpha (%d deg)"
                                          % (180 + alpha_deg)),
             (2 * math.pi, "2pi (360 deg)")]
    for t, label in ticks:
        parts.append(line(px(t), 532, px(t), 538, AXIS, 1.0))
        anchor = "start" if t == 0 else ("end" if t == 2 * math.pi else "middle")
        parts.append(txt(px(t), 554, label, 12, MUTED, anchor))

    parts.append(txt(28, 578,
                     "Illustrative sketch from the ideal model: no commutation overlap, "
                     "no device voltage drops. Verify against your textbook.",
                     12, MUTED))
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="figure-waveform-example.svg",
                    help="output SVG path (default: ./figure-waveform-example.svg)")
    ap.add_argument("--alpha-deg", type=float, default=60.0,
                    help="firing angle in degrees (default: 60)")
    args = ap.parse_args()
    if not 0 < args.alpha_deg < 180:
        ap.error("--alpha-deg must be between 0 and 180")

    svg = build(args.alpha_deg)
    ET.fromstring(svg)  # fail loudly if the generated markup is not valid XML
    out = os.path.abspath(args.out)
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(svg)
    print("wrote %s (%d bytes, alpha=%.0f deg)" % (out, os.path.getsize(out),
                                                   args.alpha_deg))


if __name__ == "__main__":
    main()
