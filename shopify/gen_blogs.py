"""
Generate 8 new blog HTML files from blog/TEMPLATE.html.

Each post is defined below with: slug, title, date, iso date, breadcrumb,
category, meta description, intro paragraphs, body sections, FAQ, and a
"People also search" keyword line (added after the FAQ for SEO).

Run:  python shopify/gen_blogs.py
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(__file__))
TEMPLATE = os.path.join(ROOT, "blog", "TEMPLATE.html")
BLOG_DIR = os.path.join(ROOT, "blog")

P_CLS = 'text-[clamp(0.9rem,1.8vw,1.05rem)] font-light leading-[1.9] mb-6'
H2_CLS = 'text-[clamp(1.2rem,3vw,1.7rem)] leading-[1.3] mt-12 mb-5'
H3_CLS = 'text-[1.1rem] leading-[1.3] mt-8 mb-3'
UL_CLS = 'list-disc pl-6 mb-6 space-y-2 text-[clamp(0.9rem,1.8vw,1.05rem)] font-light leading-[1.9]'


def P(text):
    return f'<p class="{P_CLS}" style="color:var(--text-body)">{text}</p>'


def H2(text):
    return f'<h2 class="{H2_CLS}" style="font-family:var(--font-display);color:var(--text-heading)">{text}</h2>'


def H3(text):
    return f'<h3 class="{H3_CLS}" style="font-family:var(--font-display);color:var(--text-heading)">{text}</h3>'


def UL(items):
    lis = "\n".join(f"        <li>{it}</li>" for it in items)
    return f'<ul class="{UL_CLS}" style="color:var(--text-body)">\n{lis}\n      </ul>'


# Each "body" is a list of blocks. Block types: ('h2', text), ('h3', text),
# ('p', text), ('ul', [items]). FAQ is a list of (question, answer) tuples.
POSTS = [
    {
        "slug": "utopia-wellness-gifts-lonsdale",
        "title": "Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave, North Vancouver",
        "breadcrumb": "Utopia on Lonsdale",
        "date": "September 1, 2026",
        "iso": "2026-09-01",
        "category": "SPIRITUALITY",
        "meta": "Utopia Wellness & Gifts is the wellness and gift store at 1826 Lonsdale Ave, North Vancouver, offering crystals, meaningful gifts, and in-person Clarity & Guidance sessions.",
        "intro": [
            "Utopia Wellness &amp; Gifts is the wellness and gift store at 1826 Lonsdale Avenue in North Vancouver. If you searched &ldquo;Utopia Lonsdale,&rdquo; &ldquo;Utopia Wellness &amp; Gifts,&rdquo; or &ldquo;1826 Lonsdale,&rdquo; you are looking for the physical shop on the Lonsdale corridor &mdash; crystals, meaningful gifts, and in-person Clarity &amp; Guidance sessions.",
            "The store is easy to reach from the North Shore and Vancouver. Free parking is available at the back of the building. You can walk in for gifts or book a reader online at UtopiaStore.ca.",
        ],
        "body": [
            ("h2", "How to find Utopia"),
            ("p", "Look for Utopia Wellness &amp; Gifts on Lonsdale Ave near 19th Street. The public address is 1826 Lonsdale Ave, North Vancouver. Call 604-984-8782 if you need directions or same-day availability."),
            ("h2", "What the store is known for"),
            ("ul", [
                "Premium gifts, jewelry, and home décor",
                "Healing crystals and intention items",
                "Tarot, intuitive, and mediumship-style sessions",
                "Workshops, New Moon circles, Mind Spa, and Dream Machine experiences",
            ]),
            ("h2", "Utopia vs searching &ldquo;near me&rdquo;"),
            ("p", "Queries like &ldquo;crystal shop near me&rdquo; or &ldquo;psychic North Vancouver&rdquo; often surface Utopia because the store is a long-standing Lonsdale location, not only an online catalog. In-store you can see the piece, meet a reader, and leave with something useful the same day."),
            ("p", "A session or a short visit is the fastest way to confirm you have the right Utopia. Hours and booking: UtopiaStore.ca or 604-984-8782."),
        ],
        "faq": [
            ("Is Utopia Wellness &amp; Gifts the same as Utopia Sacred Space?", "Yes. The store has used earlier names, including Utopia Sacred Space. The current public name is Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave."),
            ("Is there parking?", "Yes. Free parking is at the back of the store."),
            ("Can I shop and get a reading the same day?", "Often yes, subject to reader availability. Walk-ins are welcome; booking online is more reliable."),
        ],
        "keywords": "utopia lonsdale, utopia wellness & gifts, 1826 lonsdale ave north vancouver, utopia store north vancouver, utopia near me, crystal shop lonsdale",
    },
    {
        "slug": "psychic-tarot-shop-north-vancouver",
        "title": "Psychic Reading &amp; Tarot in North Vancouver (Near Lonsdale)",
        "breadcrumb": "Psychic &amp; Tarot Shop",
        "date": "September 1, 2026",
        "iso": "2026-09-01",
        "category": "PSYCHIC GUIDANCE",
        "meta": "Searching for a psychic reading or tarot shop near you in North Vancouver? Utopia at 1826 Lonsdale Ave offers in-person Clarity & Guidance sessions and spiritual tools.",
        "intro": [
            "If you searched &ldquo;psychic reading near me,&rdquo; &ldquo;tarot shop North Vancouver,&rdquo; &ldquo;witch store near me,&rdquo; or &ldquo;occult shop Vancouver,&rdquo; you want a real local place &mdash; not only an app. Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave offers in-person Clarity &amp; Guidance sessions and the tools people usually buy after a reading: decks, crystals, incense, and journals.",
            "Sessions are with named readers on set days. You can walk in when a reader is free or book at UtopiaStore.ca.",
        ],
        "body": [
            ("h2", "What you can book"),
            ("ul", [
                "Short introductory session (Glimpse)",
                "Tarot and intuitive readings",
                "Mediumship-style sessions with selected readers",
                "Longer clarity sessions for love, work, or life direction",
            ]),
            ("h2", "What &ldquo;near me&rdquo; usually means on the North Shore"),
            ("p", "Most local searches come from North Vancouver, West Vancouver, and people already on Lonsdale. Utopia is a storefront you can enter the same day, with parking behind the shop."),
            ("h2", "How this is different from online-only platforms"),
            ("p", "You meet a specific reader in a shop, pay a session price rather than a ticking per-minute clock, and can take a physical item home. That is the practical difference people want when they type &ldquo;tarot cards near me&rdquo; or &ldquo;psychic North Vancouver.&rdquo;"),
            ("p", "Call 604-984-8782 or visit UtopiaStore.ca."),
        ],
        "faq": [
            ("Do I need an appointment?", "Booking is safer. Walk-ins are accepted if the reader is free."),
            ("Is this a witch store or a gift shop?", "Both kinds of searchers come in. The public positioning is wellness and gifts, with readings and spiritual tools available."),
            ("Are readings only in person?", "In-person is the core offer. Ask when booking if a reader also works by video."),
        ],
        "keywords": "psychic north vancouver, tarot cards north vancouver, witch store near me, occult shop near me, metaphysical store vancouver, tarot shop near me",
    },
    {
        "slug": "clairvoyant-vs-clairsentient",
        "title": "Clairvoyant vs Clairsentient: What These Abilities Mean in a Reading",
        "breadcrumb": "Clairvoyant vs Clairsentient",
        "date": "September 1, 2026",
        "iso": "2026-09-01",
        "category": "PSYCHIC GUIDANCE",
        "meta": "Clairvoyance is clear seeing; clairsentience is clear feeling. Learn the difference between the clair senses and how readers use them in a Clarity & Guidance session.",
        "intro": [
            "Clairvoyance is clear seeing &mdash; images, symbols, or inner pictures. Clairsentience is clear feeling &mdash; emotions, body sensations, or the &ldquo;tone&rdquo; of a situation. People search &ldquo;clairvoyant vs clairsentient,&rdquo; &ldquo;types of clairvoyance,&rdquo; and &ldquo;clear seeing&rdquo; when they want to know how a reader is actually working.",
            "In a Clarity &amp; Guidance session at Utopia, a reader may use one primary sense or several together with tarot, oracle cards, or a pendulum. You do not need to label yourself before you book.",
        ],
        "body": [
            ("h2", "Simple definitions"),
            ("ul", [
                "<strong>Clairvoyance:</strong> visions, images, colours, scenes",
                "<strong>Clairaudience:</strong> words, phrases, inner hearing",
                "<strong>Clairsentience:</strong> feeling energy or emotion",
                "<strong>Claircognizance:</strong> sudden knowing without a picture",
            ]),
            ("h2", "Why the difference matters"),
            ("p", "If you want visual symbolism, a clairvoyant-leaning or tarot-heavy session may feel clearer. If you want emotional truth in relationships, clairsentience often lands first. Ask for the style you prefer when you book."),
            ("h2", "What to expect at Utopia"),
            ("p", "Readers describe what comes through in plain language. The goal is usable clarity &mdash; love, work, timing, next step &mdash; not a lecture on psychic theory."),
        ],
        "faq": [
            ("Is clairvoyance more accurate than clairsentience?", "No. Accuracy depends on the reader and how well the session is focused, not on which &ldquo;clair&rdquo; is used."),
            ("Can someone have more than one ability?", "Yes. Most working readers blend senses with tools."),
        ],
        "keywords": "types of clairvoyance, clairvoyant vs clairsentient, clear seeing, clairsentient meaning, psychic abilities",
    },
    {
        "slug": "how-to-read-tarot-spreads",
        "title": "How to Read Tarot Cards: Spreads Beginners Actually Use",
        "breadcrumb": "How to Read Tarot",
        "date": "September 1, 2026",
        "iso": "2026-09-01",
        "category": "TAROT",
        "meta": "Learn how to read tarot with a simple 3-card spread, the Celtic Cross, and the true meaning of the Death card. Beginner-friendly guidance from Utopia in North Vancouver.",
        "intro": [
            "Learning how to read tarot starts with a simple spread and one clear question. Searches like &ldquo;how to read tarot,&rdquo; &ldquo;3 card spread,&rdquo; &ldquo;Celtic Cross,&rdquo; and &ldquo;death card meaning&rdquo; are the same journey: understand the cards without getting lost.",
            "You can practice at home with a deck from Utopia, or sit with a reader first so you see how a focused question works.",
        ],
        "body": [
            ("h2", "A 3-card spread (start here)"),
            ("ul", [
                "Situation",
                "Challenge",
                "Advice / next step",
            ]),
            ("h2", "Celtic Cross"),
            ("p", "A larger layout for a full-life or high-stakes question. Use it when a 3-card spread is not enough. It is not required for beginners."),
            ("h2", "The Death card"),
            ("p", "Death in tarot is usually ending and transition, not a prediction of physical death. It often flags a chapter closing so another can start."),
            ("h2", "How to ask better questions"),
            ("p", "Ask &ldquo;What do I need to understand about this job change?&rdquo; not only &ldquo;Will I get the job?&rdquo; Specific questions produce specific cards."),
            ("p", "Utopia carries decks and offers readings if you want to learn by watching a session. UtopiaStore.ca | 604-984-8782."),
        ],
        "faq": [
            ("Do I need a Rider&ndash;Waite deck?", "It is the most common teaching deck. Any deck you will actually use is fine."),
            ("Can I read for myself?", "Yes. Write the question down first so you do not change it mid-spread."),
        ],
        "keywords": "celtic cross, 3 card tarot spread, how to read tarot, death card tarot, tarot cards near me, rider waite",
    },
    {
        "slug": "full-moon-new-moon-rituals",
        "title": "Full Moon Ritual and New Moon Intentions (Simple and Usable)",
        "breadcrumb": "Full Moon &amp; New Moon Rituals",
        "date": "September 1, 2026",
        "iso": "2026-09-01",
        "category": "RITUALS",
        "meta": "A simple full moon ritual for release and a new moon practice for setting one clear intention. Usable steps plus New Moon Circles at Utopia in North Vancouver.",
        "intro": [
            "A full moon ritual is a time to review and release. A new moon is a time to set one clear intention. People search &ldquo;full moon ritual,&rdquo; &ldquo;new moon,&rdquo; &ldquo;charged water,&rdquo; and &ldquo;sage in the house&rdquo; because they want a practice they can finish in one evening.",
            "You do not need a complicated altar. One candle, one page in a journal, and one honest sentence is enough.",
        ],
        "body": [
            ("h2", "Full moon &mdash; three steps"),
            ("ul", [
                "Write what you are done carrying.",
                "Sit quietly for a few minutes.",
                "Choose one small action for the next two weeks.",
            ]),
            ("h2", "New moon &mdash; three steps"),
            ("ul", [
                "Write one intention (not ten).",
                "Keep it where you will see it.",
                "Take one matching action within 48 hours.",
            ]),
            ("h2", "Smoke, sage, and &ldquo;charged&rdquo; water"),
            ("p", "If you cleanse a room, ventilate well and be considerate of neighbours and building rules. Moon water is simply water set aside with an intention; treat it as a reminder, not a medical product."),
            ("p", "Utopia hosts New Moon Circles and sells simple ritual supplies in store. Dates: UtopiaStore.ca."),
        ],
        "faq": [
            ("Do I have to follow the exact calendar date?", "The night of or the closest evening you can keep is fine."),
            ("Is this only for women?", "No. Circles and home practice are open unless a specific event says otherwise."),
        ],
        "keywords": "full moon ritual, new moon ritual, how to charge water, smudging sage, moon journal",
    },
    {
        "slug": "healing-crystals-north-vancouver",
        "title": "Healing Crystals in North Vancouver: How to Choose and Use Them",
        "breadcrumb": "Healing Crystals",
        "date": "September 1, 2026",
        "iso": "2026-09-01",
        "category": "CRYSTALS",
        "meta": "How to choose and use healing crystals, from a crystal shop in North Vancouver. See stones in person at Utopia on Lonsdale and keep your practice simple.",
        "intro": [
            "If you searched &ldquo;crystal shop North Vancouver,&rdquo; &ldquo;healing crystals near me,&rdquo; or &ldquo;how to charge crystals,&rdquo; you want a place to see stones in person and a simple way to use them. Utopia Wellness &amp; Gifts on Lonsdale stocks crystals as gifts, desk pieces, and companions to readings &mdash; not as medical devices.",
            "Pick by feel and by use: sleep, focus, a gift, protection of a space. Then keep the practice small.",
        ],
        "body": [
            ("h2", "How to choose in store"),
            ("p", "Hold two options. Keep the one you do not want to put down. If you are gifting, choose by the person&rsquo;s actual life (new job, new home, comfort), not only by a colour chart."),
            ("h2", "How people &ldquo;charge&rdquo; or cleanse"),
            ("p", "Common methods are rest, moonlight on a windowsill, or a short intention. Avoid anything that damages the stone or your home."),
            ("h2", "Pair with a session"),
            ("p", "Many customers buy a small stone after a Clarity &amp; Guidance session as a reminder of the next step, not as a substitute for the conversation."),
        ],
        "faq": [
            ("Which crystal should I start with?", "One clear purpose. Clear quartz or amethyst are common first pieces because they are easy to live with."),
            ("Do crystals replace a reading?", "No. They are tools and gifts. Guidance still comes from the session and your decisions."),
        ],
        "keywords": "crystal shops vancouver, healing crystal shops near me, where to buy crystals near me, how to charge crystals, crystal store north vancouver",
    },
    {
        "slug": "dragonfly-butterfly-signs",
        "title": "Dragonfly, Butterfly, and Other Signs People Notice",
        "breadcrumb": "Everyday Signs",
        "date": "September 1, 2026",
        "iso": "2026-09-01",
        "category": "ANIMAL SPIRITS",
        "meta": "Dragonfly, butterfly, cardinal, or hawk showing up often? Learn a practical way to read everyday signs as prompts to pause, not fixed predictions.",
        "intro": [
            "A dragonfly, butterfly, cardinal, or hawk showing up more than usual is one of the most common searches in this category: &ldquo;spiritual meaning of a dragonfly,&rdquo; &ldquo;butterfly meaning,&rdquo; &ldquo;what does it mean when a bird visits.&rdquo; These moments are prompts to pay attention, not fixed predictions.",
            "If the sign repeats around a decision, treat it as a cue to pause and ask a clearer question &mdash; in a journal or in a session.",
        ],
        "body": [
            ("h2", "A practical way to read a sign"),
            ("ul", [
                "What were you thinking about when it appeared?",
                "What decision is already on your table?",
                "What is one honest next step?",
            ]),
            ("h2", "Common themes people bring in"),
            ("ul", [
                "<strong>Dragonfly:</strong> change, lightness after a heavy period",
                "<strong>Butterfly:</strong> transition, becoming",
                "<strong>Repeated birds at the window:</strong> a message you have been ignoring",
                "<strong>Ringing in the ear:</strong> many people ask; get a medical check if it is physical, and use a session for the symbolic side only",
            ]),
            ("p", "Utopia readers work with the context of your life, not a single symbol dictionary."),
        ],
        "faq": [
            ("Does a dragonfly always mean the same thing?", "No. Meaning follows your situation."),
            ("Should I wait for another sign before acting?", "If you already know the step, take it. Signs are not a substitute for decisions."),
        ],
        "keywords": "spiritual meaning of dragonfly, butterfly spiritual meaning, hawk meaning, what does it mean when you see a cardinal, ringing in ear spiritual",
    },
    {
        "slug": "what-to-ask-in-a-reading",
        "title": "What to Ask in a Reading (Love, Work, and Life Direction)",
        "breadcrumb": "What to Ask in a Reading",
        "date": "September 1, 2026",
        "iso": "2026-09-01",
        "category": "PSYCHIC GUIDANCE",
        "meta": "The best readings start with a real question. Example questions for love, work, and life direction, plus how to choose a trusted reader at Utopia in North Vancouver.",
        "intro": [
            "The best readings start with a real question. Searches like &ldquo;what to ask a psychic,&rdquo; &ldquo;trusted psychic,&rdquo; &ldquo;love tarot,&rdquo; and &ldquo;career reading&rdquo; all point to the same need: clarity you can use this week.",
            "At Utopia, a Clarity &amp; Guidance session can focus on relationships, work, money stress, or a single decision. Specific beats vague.",
        ],
        "body": [
            ("h2", "Useful question examples"),
            ("ul", [
                "How can I improve my current situation?",
                "What should I understand about this relationship?",
                "What is the next honest step in my work?",
                "What am I not seeing?",
                "What would help me sleep better about this choice?",
            ]),
            ("h2", "What not to cling to"),
            ("p", "The future is not a fixed script. A good session shows patterns and options. It does not replace your choices."),
            ("h2", "How to choose a trusted reader locally"),
            ("p", "Read the reader&rsquo;s specialty, notice how you feel in the first minutes, and ask one clear question. You can choose Helen, Lyne, Manti, Mystic Mic, Kim, Linda, or another scheduled reader."),
        ],
        "faq": [
            ("How long should a first session be?", "A short Glimpse is enough to test fit. Book longer if the question is large."),
            ("Can I ask about someone else&rsquo;s feelings?", "You can ask about the relationship dynamic and your part in it. Focus on what you can change."),
        ],
        "keywords": "what to ask a psychic, trusted psychic, love tarot reading, career tarot, psychic reading north vancouver",
    },
]


def render_body(blocks):
    out = []
    for kind, val in blocks:
        if kind == "h2":
            out.append("      " + H2(val))
        elif kind == "h3":
            out.append("      " + H3(val))
        elif kind == "p":
            out.append("      " + P(val))
        elif kind == "ul":
            out.append("      " + UL(val))
    return "\n".join(out)


def render_faq(faq, keywords):
    parts = [
        "      " + H2("Frequently Asked Questions"),
    ]
    for q, a in faq:
        parts.append("      " + H3(q))
        parts.append("      " + P(a))
    # People also search line (SEO). Rendered subtle, still crawlable.
    parts.append(
        '      <p class="text-[.8rem] font-light mt-8" style="color:var(--text-muted)"><strong>People also search:</strong> '
        + keywords
        + "</p>"
    )
    return "\n".join(parts)


def faq_schema(faq):
    def esc(s):
        s = re.sub(r"<[^>]+>", "", s)
        s = (s.replace("&amp;", "&").replace("&mdash;", "-").replace("&ndash;", "-")
               .replace("&ldquo;", '"').replace("&rdquo;", '"')
               .replace("&rsquo;", "'").replace("&lsquo;", "'"))
        s = s.replace("\\", "\\\\").replace('"', '\\"')
        return s
    items = ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
        % (esc(q), esc(a))
        for q, a in faq
    )
    return ('<script type="application/ld+json">{"@context":"https://schema.org",'
            '"@type":"FAQPage","mainEntity":[' + items + "]}</script>")


def main():
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        tpl = f.read()

    # Strip the instructional "🔧" comment blocks from the template so generated
    # files are clean. Handles the boxed (═) REPLACE blocks, the single-line
    # STRUCTURED DATA hint, and the multi-line FAQ SCHEMA example comment.
    tpl = re.sub(r"<!-- ═+\s*🔧 REPLACE:.*?═+ -->\n?", "", tpl, flags=re.S)
    tpl = re.sub(r"\s*<!-- 🔧 FAQ SCHEMA.*?-->", "", tpl, flags=re.S)
    # Normalize the STRUCTURED DATA comment (keep it, but drop the 🔧 hint text)
    tpl = tpl.replace(
        '<!-- STRUCTURED DATA — 🔧 REPLACE: {{TITLE}}, {{SLUG}}, {{DATE_ISO}} (YYYY-MM-DD) -->',
        '<!-- STRUCTURED DATA -->',
    )
    # Remove any leftover inline 🔧 comment lines
    tpl = re.sub(r"[ \t]*<!--[^\n]*🔧[^\n]*-->\n?", "", tpl)

    for post in POSTS:
        html = tpl
        html = html.replace("{{TITLE}}", post["title"])
        html = html.replace("{{META_DESCRIPTION}}", post["meta"])
        html = html.replace("{{SLUG}}", post["slug"])
        html = html.replace("{{BREADCRUMB}}", post["breadcrumb"])
        html = html.replace("{{DATE_ISO}}", post["iso"])
        html = html.replace("{{DATE}}", post["date"])

        intro_html = "\n".join("      " + P(p) for p in post["intro"])
        html = html.replace("{{CONTENT_INTRO}}", intro_html)

        body_html = render_body(post["body"]) + "\n\n" + render_faq(post["faq"], post["keywords"])
        html = html.replace("{{CONTENT_BODY}}", body_html)

        # Inject FAQ schema before </body>
        html = html.replace("</body>", faq_schema(post["faq"]) + "\n</body>")

        out_path = os.path.join(BLOG_DIR, post["slug"] + ".html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"wrote {post['slug']}.html")

    try:
        from gen_blogdata import regenerate
        regenerate()
    except Exception as e:
        print(f"(gen_blogdata skipped: {e})")


if __name__ == "__main__":
    main()
