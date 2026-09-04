"""
Regenerate blog/blogdata.json from blog/index.html's embedded blog list.
This is the data the homepage "Readings & Reflections" section fetches.

Run directly:  python shopify/gen_blogdata.py
Or import:     from gen_blogdata import regenerate; regenerate()
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(__file__))
INDEX = os.path.join(ROOT, "blog", "index.html")
OUT = os.path.join(ROOT, "blog", "blogdata.json")


def regenerate():
    c = open(INDEX, encoding="utf-8").read()
    m = re.search(r'id="blogData" type="application/json">(.*?)</script>', c, re.S)
    if not m:
        print("gen_blogdata: could not find blogData in index.html; skipped")
        return 0
    data = json.loads(m.group(1))
    slim = [{"c": d["c"], "t": d["t"], "f": d["f"]} for d in data]
    open(OUT, "w", encoding="utf-8").write(
        json.dumps(slim, ensure_ascii=False, separators=(",", ":"))
    )
    print(f"gen_blogdata: wrote {len(slim)} entries to blog/blogdata.json")
    return len(slim)


if __name__ == "__main__":
    regenerate()
