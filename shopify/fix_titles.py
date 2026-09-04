"""
Re-set the title (and summary) of already-published Shopify articles so any
HTML entities (&amp;, &mdash;, &ldquo; ...) are decoded to plain text.

Reads shopify.md for filename -> latest article_id, decodes the title via the
fixed push_blog.extract_meta, and PUTs title + summary_html.

USAGE:
    $env:SHOPIFY_TOKEN = (Get-Content shopify/.token -Raw).Trim()
    python shopify/fix_titles.py            # only titles that contain entities
    python shopify/fix_titles.py --all      # every tracked article
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


def load_ids():
    ids = {}
    with open(TRACK, "r", encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\|\s*`([^`]+)`\s*\|\s*done\s*\|\s*(\d+)\s*\|", line)
            if m:
                ids[m.group(1)] = m.group(2)  # last wins = latest push
    return ids


def raw_title(raw):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.S)
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else ""


def main():
    token = os.environ.get("SHOPIFY_TOKEN")
    if not token:
        print("ERROR: set SHOPIFY_TOKEN")
        return 1
    do_all = "--all" in sys.argv
    ids = load_ids()

    ok = fail = skip = 0
    for fname, aid in ids.items():
        path = os.path.join(BLOG_DIR, fname)
        if not os.path.exists(path):
            continue
        raw = open(path, "r", encoding="utf-8").read()
        rt = raw_title(raw)
        title, desc = pb.extract_meta(raw)  # decoded
        # Only fix when the raw title actually differs from decoded (has entities)
        if not do_all and rt == title:
            skip += 1
            continue
        payload = {"article": {"id": int(aid), "title": title}}
        if desc:
            payload["article"]["summary_html"] = f"<p>{desc}</p>"
        status, data = pb.api_request("PUT", f"/blogs/{BLOG_ID}/articles/{aid}.json", token, payload)
        if status == 200:
            ok += 1
            print(f"FIXED {fname} -> {title}")
        else:
            fail += 1
            print(f"FAIL {fname}: HTTP {status} {str(data)[:120]}")
        time.sleep(0.6)

    print(f"\nDone. Fixed {ok}, failed {fail}, skipped(no entities) {skip}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
