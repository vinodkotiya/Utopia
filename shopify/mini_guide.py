"""
Micro Guidance & Clarity — glossary entry builder for mini-guide.html.

Turns a list of keywords / search phrases into short (2-4 sentence) AEO-safe
glossary entries, runs the full quality gate, and appends the passing entries
into the correct category section of mini-guide.html plus the page's FAQPage
schema.

DESIGN
------
The tool is LLM-agnostic. It gets entry text from a "generator" and then
enforces the quality gate. Two ways to supply text:

  1) --infile FILE   A pipe-delimited file, one keyword per line:
                        CATEGORY | keyword or phrase | entry text (2-4 sentences)
                     (entry text optional; if omitted, the built-in local
                     template generator writes a safe placeholder you can edit)

  2) Plug in your own LLM: set the environment variable and implement the call
     inside llm_generate(). A deterministic local generator is used as fallback
     so the pipeline runs today without any API key.

QUALITY GATE (all from the spec)
  - length: reject < ~15 words or > ~90 words
  - duplicate opening: first 5 words vs last 50 published entries -> regenerate
  - banned phrases: unlock / elevate your / journey within / unleash /
    "in today's fast-paced world" / absolute claims (will, guaranteed, proven)
  - fact-invention: flag entries containing a number, date, study, research,
    "according to"
  - CTA ratio: <= 6 CTAs per batch of 20 (~30% ceiling)
  - similarity: difflib ratio > 0.85 vs any other entry -> regenerate/flag

USAGE (PowerShell)
    python shopify/mini_guide.py --infile shopify/keywords.txt
    python shopify/mini_guide.py --infile shopify/keywords.txt --dry-run
    python shopify/mini_guide.py --status        # show counts per category

Categories accepted (case-insensitive): CRYSTALS, PALMISTRY, SIGNS,
TAROT, ASTROLOGY, RITUALS.  "signs & symbols" also maps to SIGNS.
"""

import argparse
import difflib
import html as _html
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(__file__))
PAGE = os.path.join(ROOT, "mini-guide.html")

CATEGORY_MARKERS = {
    "CRYSTALS": ("<!-- ENTRIES:CRYSTALS -->", "<!-- END:CRYSTALS -->"),
    "PALMISTRY": ("<!-- ENTRIES:PALMISTRY -->", "<!-- END:PALMISTRY -->"),
    "SIGNS": ("<!-- ENTRIES:SIGNS -->", "<!-- END:SIGNS -->"),
    "TAROT": ("<!-- ENTRIES:TAROT -->", "<!-- END:TAROT -->"),
    "ASTROLOGY": ("<!-- ENTRIES:ASTROLOGY -->", "<!-- END:ASTROLOGY -->"),
    "RITUALS": ("<!-- ENTRIES:RITUALS -->", "<!-- END:RITUALS -->"),
}
CATEGORY_ALIASES = {
    "SIGNS & SYMBOLS": "SIGNS", "SIGNS AND SYMBOLS": "SIGNS", "SYMBOLS": "SIGNS",
    "CRYSTAL": "CRYSTALS", "PALM": "PALMISTRY", "RITUAL": "RITUALS",
    "ZODIAC": "ASTROLOGY",
}

BANNED = [
    "unlock", "elevate your", "journey within", "unleash",
    "in today's fast-paced world", "in today\u2019s fast-paced world",
    "guaranteed", "proven",
]
# Absolute / promissory claim patterns (over-matching plain future tense like
# "you will see" is avoided by only flagging predictive claim verbs).
CLAIM_RE = re.compile(
    r"\bwill\s+(bring|give|make|grant|heal|cure|attract|manifest|guarantee|ensure|"
    r"change your|transform|fix|solve|come true|happen)\b",
    re.I,
)
# fact-invention triggers (flag, do not silently publish)
FACT_TRIGGERS = ["study", "studies", "research", "according to", "scientists", "percent", "%"]
YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")
NUMBER_RE = re.compile(r"\b\d+\b")

CTA_TEMPLATES = [
    "We carry {cat_noun} in store on Lonsdale Ave.",
    "Come see our {cat_noun} in person.",
    "Ask us about a Clarity &amp; Guidance session next time you visit.",
]
CAT_NOUNS = {
    "CRYSTALS": "healing crystals", "PALMISTRY": "readers", "SIGNS": "spiritual tools",
    "TAROT": "tarot and oracle decks", "ASTROLOGY": "astrology tools", "RITUALS": "ritual supplies",
}

MIN_WORDS = 15
MAX_WORDS = 90
SIM_THRESHOLD = 0.85
CTA_PER_20 = 6


# ---------------------------------------------------------------------------
# Generation
# ---------------------------------------------------------------------------
def llm_generate(keyword, category, structure):
    """Plug your LLM here. Return a plain-text entry (2-4 sentences) or None.

    Example (pseudo): call your provider with a prompt built from `structure`
    and `keyword`, return the completion text. Left unimplemented on purpose so
    no API key is assumed; the local fallback below runs instead.
    """
    return None


def local_generate(keyword, category, structure):
    """Deterministic, safe fallback text. Produces a neutral, non-hallucinated
    placeholder in one of the 4 structures so the pipeline runs end-to-end.
    Intended to be reviewed/edited or replaced by llm_generate output."""
    term = keyword.strip().rstrip("?.").strip()
    term_cap = term[0].upper() + term[1:] if term else term
    noun = CAT_NOUNS.get(category, "spiritual tools")
    if structure == "A":
        return (f"{term_cap}, plainly: a question people often bring us about {category.lower()}. "
                f"The short answer depends on your own situation and what you noticed at the time. "
                f"For a fuller picture, it helps to talk it through with a reader.")
    if structure == "B":
        return (f"What does &ldquo;{term}&rdquo; usually mean? Most people are asking how to read it in the context of their own life. "
                f"The honest answer is that it is a prompt to pay attention, not a fixed prediction.")
    if structure == "C":
        return (f"In everyday {category.lower()} practice, {term} is usually taken as a gentle prompt rather than a rule. "
                f"What it points to depends on what is already on your mind when it comes up.")
    # D
    return (f"To make sense of {term}, most people start by noticing the context and one decision that is already live. "
            f"A common mistake is treating it as a fixed answer rather than a nudge to look closer.")


def generate_text(keyword, category, structure):
    txt = llm_generate(keyword, category, structure)
    if txt:
        return txt.strip()
    return local_generate(keyword, category, structure)


# ---------------------------------------------------------------------------
# Quality gate
# ---------------------------------------------------------------------------
def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def word_count(s):
    return len(strip_tags(s).split())


def first_words(s, n=5):
    return " ".join(strip_tags(s).lower().split()[:n])


def check_entry(text, keyword, prior_openings, prior_texts):
    """Return list of problems (empty list = passes)."""
    problems = []
    plain = strip_tags(text)
    wc = word_count(text)
    if wc < MIN_WORDS:
        problems.append(f"too short ({wc}w)")
    if wc > MAX_WORDS:
        problems.append(f"too long ({wc}w)")
    low = " " + plain.lower() + " "
    for b in BANNED:
        if b in low:
            problems.append(f"banned phrase: {b.strip()}")
    m = CLAIM_RE.search(plain)
    if m:
        problems.append(f"absolute claim: {m.group(0)}")
    if YEAR_RE.search(plain) or any(t in plain.lower() for t in FACT_TRIGGERS):
        problems.append("fact-invention flag (number/date/study/research)")
    fw = first_words(text)
    if fw in prior_openings:
        problems.append("duplicate opening (first 5 words)")
    for pt in prior_texts:
        if difflib.SequenceMatcher(None, plain, strip_tags(pt)).ratio() > SIM_THRESHOLD:
            problems.append("too similar to another entry")
            break
    return problems


# ---------------------------------------------------------------------------
# HTML building / page editing
# ---------------------------------------------------------------------------
def slugify(s):
    s = strip_tags(s).lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s).strip("-")
    return s[:80]


def heading_for(keyword):
    k = keyword.strip()
    return k[0].upper() + k[1:] if k else k


def build_entry_html(keyword, text, cta=None):
    slug = slugify(keyword)
    parts = [f'        <div class="mg-entry">',
             f'          <h3 id="{slug}">{_html.escape(heading_for(keyword))}</h3>',
             f'          <p>{text}</p>']
    if cta:
        parts.append(f'          <p class="mg-cta">{cta}</p>')
    parts.append('        </div>')
    return "\n".join(parts)


def faq_item(keyword, text):
    def esc(s):
        s = strip_tags(s)
        s = (s.replace("&amp;", "&").replace("&ldquo;", '"').replace("&rdquo;", '"')
               .replace("&rsquo;", "'").replace("&mdash;", "-").replace("&ndash;", "-"))
        return s.replace("\\", "\\\\").replace('"', '\\"')
    q = esc(heading_for(keyword))
    a = esc(text)
    return '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q, a)


def load_page():
    return open(PAGE, encoding="utf-8").read()


def existing_slugs(page):
    return set(re.findall(r'<h3 id="([^"]+)"', page))


def collect_prior(page):
    """Return (openings set, texts list) from existing entries for dedupe."""
    texts = re.findall(r'<div class="mg-entry">.*?<p>(.*?)</p>', page, re.S)
    openings = set(first_words(t) for t in texts)
    return openings, texts


def insert_into_category(page, category, entry_html):
    start, end = CATEGORY_MARKERS[category]
    i = page.index(start) + len(start)
    j = page.index(end)
    middle = page[i:j]
    # remove the "Entries coming soon" placeholder on first insert
    middle = re.sub(r'\s*<p class="mg-empty">.*?</p>', "", middle)
    middle = middle.rstrip() + "\n" + entry_html + "\n        "
    return page[:i] + middle + page[j:]


def rebuild_faq_schema(page):
    """Rebuild the FAQPage schema fresh from every .mg-entry currently on the
    page. This guarantees valid JSON (no comment markers left inside the JSON)
    and keeps schema perfectly in sync with the visible content."""
    entries = re.findall(r'<div class="mg-entry">.*?<h3[^>]*>(.*?)</h3>\s*<p>(.*?)</p>', page, re.S)
    items = ",".join(faq_item(q, a) for q, a in entries)
    new_schema = ('<script id="mgFaqSchema" type="application/ld+json">'
                  '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
                  + items + ']}</script>')
    return re.sub(
        r'<script id="mgFaqSchema" type="application/ld\+json">.*?</script>',
        lambda _: new_schema,
        page,
        count=1,
        flags=re.S,
    )


def parse_infile(path):
    """Yield (category, keyword, text_or_None)."""
    for raw in open(path, encoding="utf-8"):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        cat = parts[0].upper() if parts else ""
        cat = CATEGORY_ALIASES.get(cat, cat)
        if cat not in CATEGORY_MARKERS:
            print(f"  SKIP (unknown category): {line}")
            continue
        keyword = parts[1] if len(parts) > 1 else ""
        text = parts[2] if len(parts) > 2 and parts[2] else None
        if keyword:
            yield cat, keyword, text


def status():
    page = load_page()
    for cat, (start, end) in CATEGORY_MARKERS.items():
        seg = page[page.index(start):page.index(end)]
        n = seg.count('class="mg-entry"')
        print(f"  {cat}: {n} entries")
    q_count = page.count('"@type":"Question"')
    print(f"  FAQ schema questions: {q_count}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--infile", help="pipe-delimited keywords file")
    ap.add_argument("--dry-run", action="store_true", help="validate + preview, do not write")
    ap.add_argument("--status", action="store_true", help="show entry counts and exit")
    args = ap.parse_args()

    if args.status:
        status()
        return 0
    if not args.infile:
        print("Provide --infile FILE (or --status). See docstring for format.")
        return 1

    page = load_page()
    seen_slugs = existing_slugs(page)
    prior_openings, prior_texts = collect_prior(page)

    STRUCTS = ["A", "B", "C", "D"]
    accepted = []      # (category, keyword, text, cta_or_None)
    rejected = []      # (keyword, reason)
    batch_cta = 0
    batch_index = 0

    items = list(parse_infile(args.infile))
    for cat, keyword, supplied in items:
        slug = slugify(keyword)
        if slug in seen_slugs:
            rejected.append((keyword, "already exists on page"))
            continue

        # Try up to 4 structures to pass the gate
        chosen = None
        for attempt in range(4):
            structure = STRUCTS[(batch_index + attempt) % 4]
            text = supplied if (supplied and attempt == 0) else generate_text(keyword, cat, structure)
            probs = check_entry(text, keyword, prior_openings, prior_texts)
            if not probs:
                chosen = text
                break
            last_probs = probs
        if not chosen:
            rejected.append((keyword, "; ".join(last_probs)))
            continue

        # CTA: ~1 in 4, but keep <= 6 per rolling 20
        cta = None
        window_start = max(0, len(accepted) - 19)
        window_ctas = sum(1 for a in accepted[window_start:] if a[3])
        if (len(accepted) % 4 == 3) and window_ctas < CTA_PER_20:
            tmpl = CTA_TEMPLATES[len(accepted) % len(CTA_TEMPLATES)]
            cta = tmpl.format(cat_noun=CAT_NOUNS.get(cat, "spiritual tools"))

        accepted.append((cat, keyword, chosen, cta))
        prior_openings.add(first_words(chosen))
        prior_texts.append(chosen)
        seen_slugs.add(slug)
        batch_index += 1

    # Report
    print(f"Accepted: {len(accepted)}  Rejected: {len(rejected)}")
    for kw, why in rejected:
        print(f"  REJECT  {kw}  ({why})")

    if args.dry_run:
        print("\n--- DRY RUN PREVIEW ---")
        for cat, kw, text, cta in accepted:
            print(f"[{cat}] {kw}\n  {strip_tags(text)}" + (f"\n  CTA: {strip_tags(cta)}" if cta else ""))
        return 0

    if not accepted:
        print("Nothing to write.")
        return 0

    # Apply: insert entries by category, then rebuild the FAQ schema fresh
    for cat, kw, text, cta in accepted:
        page = insert_into_category(page, cat, build_entry_html(kw, text, cta))
    page = rebuild_faq_schema(page)

    open(PAGE, "w", encoding="utf-8").write(page)
    print(f"\nWrote {len(accepted)} entries to mini-guide.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
