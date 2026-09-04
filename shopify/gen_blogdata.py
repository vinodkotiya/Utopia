"""
Extract the full blog list from blog/index.html's embedded JSON and write it to
blog/blogdata.json (minimal fields: c, t, f) for the homepage teaser to fetch.

Run:  python shopify/gen_blogdata.py
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(__file__))
INDEX = os.path.join(ROOT, "blog", "index.html")
OUT = os.path.join(ROOT, "blog", "blogdata.json")

c = open(INDEX, encoding="utf-8").read()
m = re.search(r'id="blogData" type="application/json">(.*?)</script>', c, re.S)
data = json.loads(m.group(1))
slim = [{"c": d["c"], "t": d["t"], "f": d["f"]} for d in data]
open(OUT, "w", encoding="utf-8").write(json.dumps(slim, ensure_ascii=False, separators=(",", ":")))
print(f"wrote {len(slim)} entries to blog/blogdata.json")
