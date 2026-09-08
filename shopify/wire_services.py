"""
Wire the new TIER 2 service pages into the Services dropdown of existing
top-level pages. Inserts 4 core service links right after the
"Clarity & Guidance" dropdown item. Idempotent: skips if already present.
Run:  python shopify/wire_services.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(__file__))

# Existing top-level pages that carry the Services dropdown.
PAGES = [
    "index.html", "contact.html", "corporate-gifts.html", "energy-work.html",
    "faq.html", "gatherings.html", "meditations.html", "media.html",
    "mini-guide.html", "shipping-returns.html",
]

DROPDOWN_STYLE = ('style="display:block;padding:.5rem 1rem;font-family:var(--font-body);'
                  'font-size:.72rem;color:rgba(237,232,255,.75);text-decoration:none;white-space:nowrap"')

CLARITY_LI = ('<li><a href="energy-work.html" %s>Clarity &amp; Guidance</a></li>' % DROPDOWN_STYLE)

NEW_LINKS = [
    ("tarot-reading-vancouver.html", "Tarot Reading"),
    ("psychic-mediums-vancouver.html", "Psychics &amp; Mediums"),
    ("reiki-north-vancouver.html", "Reiki"),
    ("energy-clearing-north-vancouver.html", "Energy Clearing"),
    ("intuitive-listening-north-vancouver.html", "Intuitive Listening"),
    ("feng-shui-vancouver.html", "Feng Shui"),
]

INSERT = "".join(
    '\n          <li><a href="%s" %s>%s</a></li>' % (href, DROPDOWN_STYLE, label)
    for href, label in NEW_LINKS
)

for name in PAGES:
    path = os.path.join(ROOT, name)
    if not os.path.exists(path):
        print("SKIP (missing):", name); continue
    html = open(path, encoding="utf-8").read()
    if "tarot-reading-vancouver.html" in html:
        print("SKIP (already wired):", name); continue
    if CLARITY_LI not in html:
        print("SKIP (no matching Clarity dropdown li):", name); continue
    html = html.replace(CLARITY_LI, CLARITY_LI + INSERT, 1)
    # widen dropdown so labels fit
    html = html.replace("border-radius:6px;min-width:180px", "border-radius:6px;min-width:200px")
    open(path, "w", encoding="utf-8").write(html)
    print("wired:", name)
