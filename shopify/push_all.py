"""
Batch-publish every local blog HTML file to Shopify, one at a time.

- Reuses the cleaning + CTA + publish logic from push_blog.py
- Tracks progress in shopify.md (Markdown table). Already-done files are skipped
  on re-run, so this is safe to stop and resume and will not create duplicates.
- Rate-limited to stay under Shopify's REST API bucket (~2 calls/sec).

USAGE (PowerShell):
    $env:SHOPIFY_TOKEN = (Get-Content shopify/.token -Raw).Trim()
    python shopify/push_all.py

    # limit how many to push in one run (optional):
    python shopify/push_all.py --limit 20
"""

import importlib.util
import os
import re
import sys
import time
from datetime import datetime

HERE = os.path.dirname(__file__)
ROOT = os.path.dirname(HERE)
BLOG_DIR = os.path.join(ROOT, "blog")
TRACK_FILE = os.path.join(ROOT, "shopify.md")
BLOG_ID = 125558882583  # "Utopia Wellness & Gifts" blog
DELAY_SECONDS = 0.6      # ~1.6 req/sec, comfortably under the limit

SKIP = {"index.html", "TEMPLATE.html"}

# Load push_blog.py as a module to reuse its functions
_spec = importlib.util.spec_from_file_location("push_blog", os.path.join(HERE, "push_blog.py"))
pb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pb)


def load_done():
    """Return a set of filenames already marked done in shopify.md."""
    done = {}
    if not os.path.exists(TRACK_FILE):
        return done
    with open(TRACK_FILE, "r", encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\|\s*`([^`]+)`\s*\|\s*(\w+)\s*\|\s*([^|]*)\|\s*([^|]*)\|", line)
            if m:
                done[m.group(1)] = {
                    "status": m.group(2).strip(),
                    "article_id": m.group(3).strip(),
                    "when": m.group(4).strip(),
                }
    return done


def ensure_track_header():
    if os.path.exists(TRACK_FILE):
        return
    with open(TRACK_FILE, "w", encoding="utf-8") as f:
        f.write("# Shopify Blog Import Tracker\n\n")
        f.write(f"Target blog: **Utopia Wellness & Gifts** (id `{BLOG_ID}`)\n\n")
        f.write("| File | Status | Article ID | Timestamp |\n")
        f.write("|------|--------|-----------|-----------|\n")


def append_track(filename, status, article_id, when):
    with open(TRACK_FILE, "a", encoding="utf-8") as f:
        f.write(f"| `{filename}` | {status} | {article_id} | {when} |\n")


def push_one(path, token):
    """Create and publish one article. Returns (status_str, article_id_or_msg)."""
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    title, desc = pb.extract_meta(raw)
    body = pb.clean_html(raw)
    if not title:
        return "FAILED", "no <h1> title"
    if not body:
        return "FAILED", "empty body"

    article = {
        "article": {
            "title": title,
            "body_html": body,
            "author": "Utopia Wellness & Gifts",
            "published": True,
        }
    }
    if desc:
        article["article"]["summary_html"] = f"<p>{desc}</p>"

    status, data = pb.api_request("POST", f"/blogs/{BLOG_ID}/articles.json", token, article)
    if status in (200, 201) and isinstance(data, dict):
        return "done", str(data["article"]["id"])
    # Rate-limited: signal caller to back off and retry
    if status == 429:
        return "RATELIMIT", str(data)
    return "FAILED", f"HTTP {status}: {str(data)[:200]}"


def main():
    token = os.environ.get("SHOPIFY_TOKEN")
    if not token:
        print("ERROR: set SHOPIFY_TOKEN env var (from shopify/.token).")
        return 1

    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])

    ensure_track_header()
    done = load_done()

    files = sorted(
        f for f in os.listdir(BLOG_DIR)
        if f.endswith(".html") and f not in SKIP
    )

    # Only push files not already marked done successfully
    todo = [f for f in files if done.get(f, {}).get("status") != "done"]

    print(f"Total blog files: {len(files)}")
    print(f"Already done:     {sum(1 for f in files if done.get(f, {}).get('status') == 'done')}")
    print(f"To push:          {len(todo)}")
    if limit:
        todo = todo[:limit]
        print(f"This run (limit): {len(todo)}")
    print()

    ok = 0
    fail = 0
    for i, filename in enumerate(todo, 1):
        path = os.path.join(BLOG_DIR, filename)

        # basic retry loop for rate-limits
        attempts = 0
        while True:
            attempts += 1
            status, info = push_one(path, token)
            if status == "RATELIMIT" and attempts <= 5:
                print(f"[{i}/{len(todo)}] rate-limited, backing off 3s...")
                time.sleep(3)
                continue
            break

        when = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        append_track(filename, status, info if status == "done" else "-", when)

        if status == "done":
            ok += 1
            print(f"[{i}/{len(todo)}] OK   {filename}  -> article {info}")
        else:
            fail += 1
            print(f"[{i}/{len(todo)}] FAIL {filename}  -> {info}")

        time.sleep(DELAY_SECONDS)

    print()
    print(f"Run complete. Published: {ok}  Failed: {fail}")
    print(f"Tracker updated: {TRACK_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
