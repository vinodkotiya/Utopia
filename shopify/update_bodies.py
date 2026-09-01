"""
Update the body_html of already-published Shopify articles in place (PUT),
so existing posts pick up the preserved "People also search" line without
creating duplicates.

Reads shopify.md for filename -> article_id mapping, re-cleans the local HTML
with push_blog.clean_html, and PUTs the new body for the files named below.

USAGE:
    $env:SHOPIFY_TOKEN = (Get-Content shopify/.token -Raw).Trim()
    python shopify/update_bodies.py           # updates DEFAULT_FILES
    python shopify/update_bodies.py --all-session   # updates all 20 session posts
"""

import importlib.util
import os
import re
import sys
import time

HERE = os.path.dirname(__file__)
ROOT = os.path.dirname(HERE)
BLOG_DIR = os.path.join(ROOT, "blog")
TRACK = os.path.join(ROOT, "shopify.md")
BLOG_ID = 125558882583

_spec = importlib.util.spec_from_file_location("push_blog", os.path.join(HERE, "push_blog.py"))
pb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pb)

SESSION_FILES = [
    "utopia-wellness-gifts-lonsdale", "psychic-tarot-shop-north-vancouver", "clairvoyant-vs-clairsentient",
    "how-to-read-tarot-spreads", "full-moon-new-moon-rituals", "healing-crystals-north-vancouver",
    "dragonfly-butterfly-signs", "what-to-ask-in-a-reading",
    "angel-numbers-000-111-1234", "signs-from-angels-guardian-archangels", "birth-chart-rising-sign-zodiac",
    "common-dream-meanings-crush-pregnancy-snake-teeth", "aura-cleansing-empaths-energy-clearing",
    "palm-reading-what-palmistry-tells-you", "chakras-reiki-sound-sessions", "tarot-card-meanings-death-swords",
    "twin-flame-soulmate-love-tarot", "sage-palo-santo-cleansing-tools", "spirit-animal-hawk-ladybug-bee",
    "ringing-ear-signs-universe",
]


def load_ids():
    ids = {}
    with open(TRACK, "r", encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\|\s*`([^`]+)`\s*\|\s*done\s*\|\s*(\d+)\s*\|", line)
            if m:
                ids[m.group(1)] = m.group(2)  # last one wins (latest push)
    return ids


def main():
    token = os.environ.get("SHOPIFY_TOKEN")
    if not token:
        print("ERROR: set SHOPIFY_TOKEN")
        return 1

    targets = SESSION_FILES if "--all-session" in sys.argv else SESSION_FILES
    ids = load_ids()

    ok = fail = 0
    for slug in targets:
        fname = slug + ".html"
        aid = ids.get(fname)
        if not aid:
            print(f"SKIP {fname} (no article id in tracker)")
            continue
        raw = open(os.path.join(BLOG_DIR, fname), "r", encoding="utf-8").read()
        body = pb.clean_html(raw)
        payload = {"article": {"id": int(aid), "body_html": body}}
        status, data = pb.api_request("PUT", f"/blogs/{BLOG_ID}/articles/{aid}.json", token, payload)
        if status == 200:
            ok += 1
            print(f"UPDATED {fname} (article {aid})")
        else:
            fail += 1
            print(f"FAIL {fname}: HTTP {status} {str(data)[:150]}")
        time.sleep(0.6)

    print(f"\nDone. Updated {ok}, failed {fail}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
