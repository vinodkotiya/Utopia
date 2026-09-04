"""
Generate 12 more blog HTML files (#9-20) from blog/TEMPLATE.html.
Reuses the helpers/structure from gen_blogs.py conventions.

Run:  python shopify/gen_blogs2.py
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


def P(t):
    return f'<p class="{P_CLS}" style="color:var(--text-body)">{t}</p>'


def H2(t):
    return f'<h2 class="{H2_CLS}" style="font-family:var(--font-display);color:var(--text-heading)">{t}</h2>'


def H3(t):
    return f'<h3 class="{H3_CLS}" style="font-family:var(--font-display);color:var(--text-heading)">{t}</h3>'


def UL(items):
    lis = "\n".join(f"        <li>{it}</li>" for it in items)
    return f'<ul class="{UL_CLS}" style="color:var(--text-body)">\n{lis}\n      </ul>'


POSTS = [
    {
        "slug": "angel-numbers-000-111-1234",
        "title": "Angel Numbers 000, 111, and 1234: What Repeating Numbers Usually Point To",
        "breadcrumb": "Angel Numbers 000, 111, 1234",
        "date": "September 1, 2026", "iso": "2026-09-01", "category": "ANGEL NUMBERS",
        "meta": "What do 000, 111, and 1234 mean? A grounded look at repeating angel numbers as prompts to pause and act, not fixed predictions.",
        "intro": [
            "Repeating numbers are one of the most common searches in this category: &ldquo;what does 000 mean,&rdquo; &ldquo;111 meaning,&rdquo; &ldquo;1234 angel number,&rdquo; &ldquo;seeing the same numbers in one day.&rdquo; They usually show up when your attention is already on a decision. Treat them as a prompt to pause, not as a guaranteed prediction.",
            "000 often points to a reset or a blank page. 111 is frequently read as a &ldquo;start&rdquo; or alignment check. 1234 is sequential &mdash; step-by-step progress rather than a leap. The number only becomes useful when you attach it to the real question in your life: work, love, money, or timing.",
        ],
        "body": [
            ("h2", "How to work with a number you keep seeing"),
            ("ul", [
                "Write the number and the thought you had when you saw it.",
                "Name one decision already on the table.",
                "Take one small action within 48 hours.",
            ]),
            ("p", "If the number stops appearing after you act, the loop is usually complete. If it continues, the step has not happened yet."),
        ],
        "faq": [
            ("Does 000 mean something is ending?", "It can mean a reset. Ending and beginning often arrive together."),
            ("Is 111 a sign to make a wish?", "It is better used as a check: is this the direction I actually want?"),
            ("Can 1234 be about money?", "It can point to ordered progress &mdash; building income in stages, not one windfall."),
        ],
        "keywords": "what does 000 mean, 111 angel number, 1234 meaning, seeing repeating numbers, angel number 1212, 0000 meaning",
    },
    {
        "slug": "signs-from-angels-guardian-archangels",
        "title": "Signs From Angels, Guardian Angels, and Archangels",
        "breadcrumb": "Signs From Angels",
        "date": "September 1, 2026", "iso": "2026-09-01", "category": "ANGEL NUMBERS",
        "meta": "Signs from angels, contacting your guardian angel, and archangels explained in grounded language. A simple way to ask for guidance at Utopia in North Vancouver.",
        "intro": [
            "People search &ldquo;signs from angels,&rdquo; &ldquo;how to contact your guardian angel,&rdquo; &ldquo;archangel meaning,&rdquo; and &ldquo;what angels are trying to tell you&rdquo; when life feels noisy and they want reassurance. In a grounded reading, angel language is a way to talk about guidance, protection, and next steps &mdash; not a requirement that you already &ldquo;believe.&rdquo;",
            "Common signs people report: repeating numbers, feathers, sudden calm, a phrase that lands, or a dream that stays after you wake. Context matters more than the symbol list.",
        ],
        "body": [
            ("h2", "A simple way to &ldquo;ask&rdquo;"),
            ("p", "Sit down. Ask one question. Write the first honest answer that appears. Then take one practical step. That is more useful than waiting for a dramatic sign."),
        ],
        "faq": [
            ("How do I know it is a sign and not coincidence?", "Repetition plus a live decision is the usual pattern. One random feather is just a feather."),
            ("Do I need to know archangel names?", "No. You can book a session and speak in ordinary language."),
        ],
        "keywords": "signs from angels, guardian angel, archangel, how to contact guardian angel, angels trying to tell me",
    },
    {
        "slug": "birth-chart-rising-sign-zodiac",
        "title": "Birth Chart, Rising Sign, and Zodiac: What People Actually Use",
        "breadcrumb": "Birth Chart &amp; Rising Sign",
        "date": "September 1, 2026", "iso": "2026-09-01", "category": "ASTROLOGY",
        "meta": "Birth chart, rising sign, and zodiac explained for self-understanding, timing, and relationships. Bring your birth date to a reading at Utopia in North Vancouver.",
        "intro": [
            "Astrology searches &mdash; &ldquo;birth chart,&rdquo; &ldquo;rising sign,&rdquo; &ldquo;Scorpio characteristics,&rdquo; &ldquo;Libra,&rdquo; &ldquo;Virgo,&rdquo; &ldquo;12 houses,&rdquo; &ldquo;Chinese zodiac&rdquo; &mdash; are usually about self-understanding, timing, and relationships. A chart is a map of patterns. It is not a prison sentence.",
            "Sun sign is the headline. Rising sign is how you meet the world. The houses describe life areas (work, home, partnership). If you only know your sun sign, you have one slice.",
        ],
        "body": [
            ("h2", "When astrology helps"),
            ("ul", [
                "You keep repeating a relationship pattern",
                "You want language for a career season",
                "You want timing, not a yes/no fortune",
            ]),
            ("p", "Bring your birth date (and time if you have it). If you do not have a birth time, a session can still work with what you know."),
        ],
        "faq": [
            ("Is my sun sign enough?", "It is a start. Rising and houses add the useful detail."),
            ("Can astrology replace a tarot reading?", "They answer differently. Tarot is often better for &ldquo;this week.&rdquo; A chart is better for &ldquo;this pattern.&rdquo;"),
        ],
        "keywords": "birth chart, rising sign, scorpio characteristics, libra personality, virgo, 12 houses astrology, chinese zodiac, what is my rising sign",
    },
    {
        "slug": "common-dream-meanings-crush-pregnancy-snake-teeth",
        "title": "Dream Meanings People Search Most: Crush, Pregnancy, Snake, Teeth",
        "breadcrumb": "Common Dream Meanings",
        "date": "September 1, 2026", "iso": "2026-09-01", "category": "DREAMS",
        "meta": "What do dreams about a crush, pregnancy, snakes, or teeth falling out mean? A grounded guide to processing dreams as emotion and change, not prophecy.",
        "intro": [
            "Dream searches are specific: &ldquo;dream about a crush,&rdquo; &ldquo;dream of being pregnant,&rdquo; &ldquo;snake in a dream,&rdquo; &ldquo;teeth falling out.&rdquo; Dreams process stress, desire, and change. They are not automatic prophecies.",
            "A crush dream often flags attention you are already giving someone &mdash; or a quality you want in yourself. Pregnancy dreams can be about a project &ldquo;gestating,&rdquo; not only a baby. Snakes often point to fear, healing, or something shedding. Teeth dreams commonly track anxiety about control, image, or words left unsaid.",
        ],
        "body": [
            ("h2", "How to work with a repeating dream"),
            ("p", "Write it down the same morning. Note what is happening in waking life. Look for the feeling, not only the image."),
        ],
        "faq": [
            ("Does a pregnancy dream mean I am pregnant?", "Not by itself. Check the physical facts if that is a real question; use the dream for the emotional meaning."),
            ("Are snake dreams always bad?", "No. Many people report them during change."),
        ],
        "keywords": "dream about crush meaning, pregnant dream meaning, snake dream spiritual meaning, teeth falling out dream, what does my dream mean",
    },
    {
        "slug": "aura-cleansing-empaths-energy-clearing",
        "title": "Aura Cleansing, Empaths, and Energy Clearing",
        "breadcrumb": "Aura &amp; Energy Clearing",
        "date": "September 1, 2026", "iso": "2026-09-01", "category": "ENERGY WORK",
        "meta": "How to cleanse your aura, empath basics, and simple energy clearing in North Vancouver. Practical resets for after crowds, conflict, or a heavy week.",
        "intro": [
            "Queries like &ldquo;how to cleanse your aura,&rdquo; &ldquo;empath,&rdquo; &ldquo;energy clearing North Vancouver,&rdquo; and &ldquo;aura with salt&rdquo; come from people who feel wiped out after crowds, conflict, or a heavy week. Language varies. The practical need is the same: reset your nervous system and your space.",
            "Simple tools people use: shower, short walk, salt bath (if your skin and plumbing allow), smoke or sound if you already work that way, and less time with draining conversations. None of this replaces medical or mental-health care.",
        ],
        "body": [
            ("h2", "If you identify as an empath"),
            ("p", "Boundaries are the skill, not collecting more labels. Choose one recovery habit after social days."),
        ],
        "faq": [
            ("Can salt cleanse an aura?", "Some people use salt water or a salt bowl as a ritual reminder. Keep expectations ordinary."),
            ("Is energy clearing the same as a psychic reading?", "Not always. A reading is insight. Clearing is a reset. Some sessions include both."),
        ],
        "keywords": "how to cleanse aura, empath traits, energy clearing north vancouver, aura reading, salt cleanse aura",
    },
    {
        "slug": "palm-reading-what-palmistry-tells-you",
        "title": "Palm Reading: What Palmistry Can and Cannot Tell You",
        "breadcrumb": "Palm Reading",
        "date": "September 1, 2026", "iso": "2026-09-01", "category": "PALMISTRY",
        "meta": "What palmistry can and cannot tell you. Palm reading as a symbolic map of tendencies, not a medical diagnosis or fixed destiny. Readings at Utopia in North Vancouver.",
        "intro": [
            "&ldquo;Palmistry,&rdquo; &ldquo;palm reading near me,&rdquo; and &ldquo;child palmistry&rdquo; are searches for a visual, in-person tool. Palmistry looks at lines and hand shape as a symbolic map of tendencies &mdash; work style, relationship patterns, vitality themes. It is not a medical diagnosis and it is not destiny carved in stone.",
            "Hands change. So do habits. That is why a palm reading works best as a conversation about how you are living now.",
        ],
        "body": [],
        "faq": [
            ("Should I read a child&rsquo;s palm?", "Be gentle. Children are still forming. Focus on strengths, not scary predictions."),
            ("Which hand do I use?", "Readers differ. Many look at both."),
        ],
        "keywords": "palmistry, palm reading near me, how to read palms, child palmistry, life line meaning",
    },
    {
        "slug": "chakras-reiki-sound-sessions",
        "title": "Chakras, Reiki, and Sound: What These Sessions Are For",
        "breadcrumb": "Chakras, Reiki &amp; Sound",
        "date": "September 1, 2026", "iso": "2026-09-01", "category": "ENERGY WORK",
        "meta": "Chakra balancing, Reiki, and sound baths explained as body-based resets. What to expect and how they sit beside readings at Utopia in North Vancouver.",
        "intro": [
            "People search &ldquo;chakra balancing,&rdquo; &ldquo;reiki North Vancouver,&rdquo; &ldquo;singing bowls,&rdquo; and &ldquo;sound bath&rdquo; when they want a body-based reset, not only talk. Chakras are a map of feeling and function (grounding, voice, focus). Reiki is hands-on or near-body settling. Sound work uses bowls or voice to help the mind drop.",
            "At Utopia these sit beside readings: some visitors want insight; some want to feel different in their body; some want both.",
        ],
        "body": [],
        "faq": [
            ("Do I have to believe in chakras for Reiki to feel useful?", "No. Many people just want quiet and less tension."),
            ("Is a sound session the same as a psychic reading?", "No. Different tool, different outcome."),
        ],
        "keywords": "chakra balancing, reiki north vancouver, singing bowls, sound bath vancouver, blocked chakras",
    },
    {
        "slug": "tarot-card-meanings-death-swords",
        "title": "Tarot Card Meanings People Search: Death, 7 of Swords, and &ldquo;Bad&rdquo; Cards",
        "breadcrumb": "Tarot Card Meanings",
        "date": "September 1, 2026", "iso": "2026-09-01", "category": "TAROT",
        "meta": "What the Death card, Seven of Swords, and other feared tarot cards really mean. A card is a snapshot in a spread, not a life sentence. Readings at Utopia.",
        "intro": [
            "Besides &ldquo;how to read tarot,&rdquo; search data shows card-by-card fear: &ldquo;death card meaning,&rdquo; &ldquo;7 of swords,&rdquo; &ldquo;what does this card mean in love.&rdquo; A card is a snapshot in a spread. It is not a life sentence.",
            "The Death card means ending and transition. The Seven of Swords points to strategy, avoidance, or something not being said. A &ldquo;scary&rdquo; card next to a hopeful card changes the whole sentence.",
        ],
        "body": [
            ("h2", "Reading cards in context"),
            ("ul", [
                "<strong>Death:</strong> ending and transition",
                "<strong>Seven of Swords:</strong> strategy, avoidance, or something not being said",
                "<strong>A &ldquo;scary&rdquo; card next to a hopeful card</strong> changes the sentence",
            ]),
        ],
        "faq": [
            ("Is the Death card a warning of physical death?", "In modern tarot reading, no. It is almost always metaphorical."),
            ("What if I keep pulling the same card?", "You are still in that lesson. Change one behaviour and pull again later."),
        ],
        "keywords": "death card tarot, 7 of swords meaning, tarot card meanings love, court cards, reversed tarot meaning",
    },
    {
        "slug": "twin-flame-soulmate-love-tarot",
        "title": "Twin Flame, Soulmate, and Love Tarot &mdash; How to Ask a Useful Question",
        "breadcrumb": "Twin Flame &amp; Love Tarot",
        "date": "September 1, 2026", "iso": "2026-09-01", "category": "LOVE & RELATIONSHIPS",
        "meta": "Twin flame, soulmate, and love tarot: how to ask a question a reading can actually answer. Clarify the pattern, not force an outcome. Love readings at Utopia.",
        "intro": [
            "&ldquo;Twin flame,&rdquo; &ldquo;soulmate,&rdquo; &ldquo;love tarot,&rdquo; and &ldquo;will they come back&rdquo; are high-emotion searches. A session can clarify the pattern between two people. It cannot force an outcome.",
            "Better questions: What is this connection teaching me? What is mine to do? What would a healthy next step look like?",
        ],
        "body": [],
        "faq": [
            ("Is twin flame the same as soulmate?", "People use the words differently. In a session we use your actual relationship, not the label."),
            ("Can a reading tell me if they will return?", "It can show likelihoods and your part. It cannot override someone else&rsquo;s will."),
        ],
        "keywords": "twin flame meaning, soulmate tarot, love reading, will my ex come back, relationship tarot spread",
    },
    {
        "slug": "sage-palo-santo-cleansing-tools",
        "title": "Sage, Palo Santo, and Cleansing Tools (What Shoppers Actually Need)",
        "breadcrumb": "Sage &amp; Cleansing Tools",
        "date": "September 1, 2026", "iso": "2026-09-01", "category": "RITUALS",
        "meta": "Sage, palo santo, and smudging kits: what you actually need to reset a room after conflict or a move. Shop tools or pair a cleanse with a reading at Utopia.",
        "intro": [
            "&ldquo;Sage shops near me,&rdquo; &ldquo;palo santo,&rdquo; &ldquo;smudging kit,&rdquo; &ldquo;witch store,&rdquo; and &ldquo;occult shop near me&rdquo; are product-intent searches. People want to reset a room after conflict, a move, or a heavy season.",
            "Use ventilation. Be kind to shared buildings. One small practice done often beats a large ritual done once.",
        ],
        "body": [],
        "faq": [
            ("Do I need both sage and palo santo?", "No. One method you will actually use is enough."),
            ("Can I smudge in an apartment?", "Check building rules and use a light hand. A wet cloth and open window still count as a reset."),
        ],
        "keywords": "buy sage near me, palo santo near me, smudge kit, witch store vancouver, occult shop near me, wiccan store",
    },
    {
        "slug": "spirit-animal-hawk-ladybug-bee",
        "title": "Spirit Animal, Hawk, Ladybug, Bee, and &ldquo;Why Is This Animal Around Me?&rdquo;",
        "breadcrumb": "Spirit Animals &amp; Signs",
        "date": "September 1, 2026", "iso": "2026-09-01", "category": "ANIMAL SPIRITS",
        "meta": "Spirit animal, hawk, ladybug, and bee meanings, plus a practical method for reading repeated wildlife as prompts. Bring the sign to a session at Utopia.",
        "intro": [
            "&ldquo;Spirit animal,&rdquo; &ldquo;hawk meaning,&rdquo; &ldquo;ladybug,&rdquo; &ldquo;bee spiritual meaning,&rdquo; and &ldquo;rats around the house spiritual meaning&rdquo; sit next to the dragonfly/butterfly searches. Same method: what were you thinking about, and what decision is live?",
            "A hawk often gets read as perspective. A ladybug as relief or luck-in-small-things. Bees as work and community. Animals in the house first need a practical check (pests, gaps, food) before a spiritual story.",
        ],
        "body": [],
        "faq": [
            ("How do I find my spirit animal?", "Notice what repeats during a real life chapter. You do not need a quiz."),
            ("Does a rat always mean betrayal?", "No. Fix the physical issue first."),
        ],
        "keywords": "spirit animal, hawk spiritual meaning, ladybug meaning, bee spiritual meaning, seeing a hawk, what is my spirit animal",
    },
    {
        "slug": "ringing-ear-signs-universe",
        "title": "Ringing in the Ear, Sudden Signs, and &ldquo;What Is Happening to Me?&rdquo;",
        "breadcrumb": "Ear Ringing &amp; Signs",
        "date": "September 1, 2026", "iso": "2026-09-01", "category": "SPIRITUALITY",
        "meta": "Ringing in the ear, synchronicity, and signs from the universe explained on two tracks: check the physical first, then use a reading for meaning and clarity.",
        "intro": [
            "Searches like &ldquo;ringing in ear spiritual meaning,&rdquo; &ldquo;sudden knowing,&rdquo; &ldquo;what is the universe trying to tell me,&rdquo; and &ldquo;synchronicity&rdquo; spike when people feel marked by coincidence. Two tracks at once: if the ringing is physical, get it checked. Then, if you want meaning, look at the decision sitting in front of you.",
            "A Clarity &amp; Guidance session is for the second track &mdash; clarity, not a medical opinion.",
        ],
        "body": [],
        "faq": [
            ("Is left-ear ringing different from right?", "Lists online disagree. Use your life context, not a rigid chart."),
            ("How often should I look for signs?", "If you are hunting all day, you will invent them. Notice what repeats, then act."),
        ],
        "keywords": "ringing in left ear spiritual, ringing in right ear, synchronicity meaning, is the universe sending me signs, sudden spiritual awakening",
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
    parts = ["      " + H2("Frequently Asked Questions")]
    for q, a in faq:
        parts.append("      " + H3(q))
        parts.append("      " + P(a))
    parts.append(
        '      <p class="text-[.8rem] font-light mt-8" style="color:var(--text-muted)"><strong>People also search:</strong> '
        + keywords + "</p>"
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
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (esc(q), esc(a))
        for q, a in faq
    )
    return ('<script type="application/ld+json">{"@context":"https://schema.org",'
            '"@type":"FAQPage","mainEntity":[' + items + "]}</script>")


def main():
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = re.sub(r"<!-- ═+\s*🔧 REPLACE:.*?═+ -->\n?", "", tpl, flags=re.S)
    tpl = re.sub(r"\s*<!-- 🔧 FAQ SCHEMA.*?-->", "", tpl, flags=re.S)
    tpl = tpl.replace(
        '<!-- STRUCTURED DATA — 🔧 REPLACE: {{TITLE}}, {{SLUG}}, {{DATE_ISO}} (YYYY-MM-DD) -->',
        '<!-- STRUCTURED DATA -->',
    )
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

        body = render_body(post["body"])
        body = (body + "\n\n" if body else "") + render_faq(post["faq"], post["keywords"])
        html = html.replace("{{CONTENT_BODY}}", body)

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
