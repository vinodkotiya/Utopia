"""
Extract clean article content from a local blog HTML file and push it to a
Shopify blog as an article.

Shopify's article body should be simple semantic HTML (h2/h3/p/ul/li/strong/a/em).
No inline styles, no <script>, no nav/footer/CTA blocks. This script strips all
of that and keeps only the readable content.

USAGE (PowerShell):
    $env:SHOPIFY_TOKEN = (Get-Content shopify/.token -Raw).Trim()
    python shopify/push_blog.py blog/magician-tarot-meaning.html

    # list existing blogs and their IDs first:
    python shopify/push_blog.py --list-blogs
"""

import json
import os
import re
import sys
import urllib.request
import urllib.error
from html.parser import HTMLParser

SHOP = "2qsfpz-t4.myshopify.com"
API_VERSION = "2024-10"
BASE = f"https://{SHOP}/admin/api/{API_VERSION}"

# Absolute base for rewriting relative asset/link references
SITE = "https://utopiastore.ca"

# Tags we keep in the cleaned output
KEEP_TAGS = {"h2", "h3", "p", "ul", "ol", "li", "strong", "em", "b", "i", "a", "br", "blockquote"}

# Phrases that identify CTA / boilerplate paragraphs to drop
CTA_MARKERS = (
    "Looking for personal guidance",
    "Book Our Reader",
    "Book a Clarity",
    "Ready to take the next step",
    "Shop Our Collection",
    "Shop the Collection",
    "Inspired by this article",
    "Back to Blog",
    "Previous Post",
    "Next Post",
    # hidden SEO helper text that some posts include near the footer
    "Related topics covered in this article",
    "North Vancouver metaphysical shop, Utopia Wellness",
)

# Date-only lines like "December 1, 2026" (no other text) are dropped
DATE_RE = re.compile(
    r"^<p>\s*(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s*\d{4}\s*</p>$",
    re.I,
)


class ArticleExtractor(HTMLParser):
    """Pulls the inner HTML of the first <article>...</article>, keeping only
    a whitelist of semantic tags and dropping attributes (except href on <a>)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_article = False
        self.article_depth = 0
        self.out = []
        self._article_started = False

    def handle_starttag(self, tag, attrs):
        if tag == "article" and not self._article_started:
            self.in_article = True
            self._article_started = True
            self.article_depth = 1
            return
        if not self.in_article:
            return
        if tag == "article":
            self.article_depth += 1
            return

        attrs_d = dict(attrs)

        # We keep only whitelisted semantic tags; other containers (div, section,
        # nav) are transparent — their tags are dropped but their text/children
        # still flow through. CTA blocks are removed later at the block level.
        if tag in KEEP_TAGS:
            if tag == "a":
                href = self._rewrite_href(attrs_d.get("href", ""))
                self.out.append(f'<a href="{href}">')
            elif tag == "br":
                self.out.append("<br>")
            else:
                self.out.append(f"<{tag}>")

    def handle_endtag(self, tag):
        if not self.in_article:
            return
        if tag == "article":
            self.article_depth -= 1
            if self.article_depth == 0:
                self.in_article = False
            return
        if tag in KEEP_TAGS and tag != "br":
            self.out.append(f"</{tag}>")

    def handle_data(self, data):
        if not self.in_article:
            return
        self.out.append(data)

    def _rewrite_href(self, href):
        if not href:
            return "#"
        if href.startswith("../"):
            return SITE + "/" + href[3:]
        if href.startswith("index.html"):
            return SITE + "/blog/" + href
        if href.endswith(".html") and not href.startswith("http"):
            return SITE + "/blog/" + href
        return href


def clean_html(raw: str) -> str:
    ext = ArticleExtractor()
    ext.feed(raw)
    html = "".join(ext.out)

    # Collapse whitespace inside the assembled markup
    html = re.sub(r"[ \t]+", " ", html)
    html = re.sub(r"\s*\n\s*", "\n", html)

    # Split into block elements, drop CTA paragraphs and empties
    # Normalize: ensure each block tag is on its own line for filtering
    html = re.sub(r"(</(?:h2|h3|p|ul|ol|li|blockquote)>)", r"\1\n", html)
    lines = [ln.strip() for ln in html.split("\n")]

    # The <h1> title is emitted as bare text (h1 not in KEEP_TAGS). Drop that
    # leading title line since Shopify renders the article title separately.
    title_text = ""
    m = re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.S)
    if m:
        title_text = re.sub(r"<[^>]+>", "", m.group(1)).strip()

    kept = []
    for ln in lines:
        if not ln:
            continue
        text_only = re.sub(r"<[^>]+>", "", ln).strip()
        # drop empty / whitespace-only blocks (but keep list structure)
        if not text_only and "<br" not in ln and "<ul" not in ln and "</ul" not in ln and "<ol" not in ln and "</ol" not in ln:
            continue
        # drop the bare title line
        if title_text and text_only == title_text:
            continue
        # drop date-only paragraphs
        if DATE_RE.match(ln):
            continue
        # drop CTA / SEO helper blocks
        if any(mrk in ln for mrk in CTA_MARKERS):
            continue
        # drop legacy hidden comma-keyword SEO lines: many commas and no
        # sentence period. BUT keep an intentional "People also search" line,
        # which is meant to be published.
        if (
            text_only.count(",") >= 4
            and "." not in text_only
            and "People also search" not in text_only
        ):
            continue
        kept.append(ln)

    body = "\n".join(kept).strip()
    return insert_mid_cta(body)


# Simple, theme-friendly mid-article call to action (no inline styles, no script)
MID_CTA = (
    '<p><strong>Looking for personal guidance?</strong> '
    'Book a Clarity &amp; Guidance session with one of our experienced readers &mdash; '
    'in person at 1826 Lonsdale Ave, North Vancouver. '
    '<a href="https://utopiastore.ca/energy-work.html">Book a reading &rarr;</a></p>'
)


def insert_mid_cta(body: str) -> str:
    """Insert a simple CTA after the first 2 content paragraphs (the intro),
    just before the first <h2>. Falls back to the midpoint if no <h2>."""
    if not body:
        return body
    lines = body.split("\n")
    # Prefer inserting right before the first H2 (end of intro section)
    for i, ln in enumerate(lines):
        if ln.startswith("<h2"):
            lines.insert(i, MID_CTA)
            return "\n".join(lines)
    # No H2: drop it near the middle
    mid = max(1, len(lines) // 2)
    lines.insert(mid, MID_CTA)
    return "\n".join(lines)


def extract_meta(raw: str):
    title = ""
    m = re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.S)
    if m:
        title = re.sub(r"<[^>]+>", "", m.group(1)).strip()
    desc = ""
    m = re.search(r'<meta name="description" content="([^"]*)"', raw)
    if m:
        desc = m.group(1).strip()
    return title, desc


def api_request(method, path, token, body=None):
    url = BASE + path
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "X-Shopify-Access-Token": token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def list_blogs(token):
    status, data = api_request("GET", "/blogs.json", token)
    print(f"HTTP {status}")
    print(json.dumps(data, indent=2) if isinstance(data, dict) else data)


def push(path, token, blog_id=None):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    title, desc = extract_meta(raw)
    body = clean_html(raw)

    if not title:
        print("ERROR: could not find <h1> title in the file.")
        return 1

    # Resolve a blog id if not provided: use the first blog on the store
    if blog_id is None:
        status, data = api_request("GET", "/blogs.json", token)
        if status != 200 or not isinstance(data, dict) or not data.get("blogs"):
            print(f"Could not list blogs (HTTP {status}): {data}")
            return 2
        blog_id = data["blogs"][0]["id"]
        print(f"Using blog id {blog_id} ({data['blogs'][0].get('title')})")

    article = {
        "article": {
            "title": title,
            "body_html": body,
            "author": "Utopia Wellness & Gifts",
            "published": True,  # publish live
        }
    }
    if desc:
        article["article"]["summary_html"] = f"<p>{desc}</p>"

    status, data = api_request("POST", f"/blogs/{blog_id}/articles.json", token, article)
    if status in (200, 201) and isinstance(data, dict):
        a = data["article"]
        print("SUCCESS — article PUBLISHED live")
        print(f"  id:     {a['id']}")
        print(f"  title:  {a['title']}")
        print(f"  handle: {a.get('handle')}")
        print(f"\nPreview in admin: https://{SHOP}/admin/articles/{a['id']}")
        return 0
    print(f"FAILED (HTTP {status}): {data}")
    return 3


def main():
    token = os.environ.get("SHOPIFY_TOKEN")
    if not token:
        print("ERROR: set SHOPIFY_TOKEN env var (from shopify/.token).")
        return 1

    args = sys.argv[1:]
    if not args:
        print("Usage: python shopify/push_blog.py <blog/file.html> [--blog-id N]")
        print("       python shopify/push_blog.py --list-blogs")
        return 1

    if args[0] == "--list-blogs":
        list_blogs(token)
        return 0

    path = args[0]
    blog_id = None
    if "--blog-id" in args:
        blog_id = int(args[args.index("--blog-id") + 1])

    return push(path, token, blog_id)


if __name__ == "__main__":
    sys.exit(main())
