"""
TIER 3 blog posts. Generate from blog/TEMPLATE.html.
Run:  python shopify/gen_tier3.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(__file__))
TEMPLATE = os.path.join(ROOT, "blog", "TEMPLATE.html")
BLOG_DIR = os.path.join(ROOT, "blog")

P_CLS = 'text-[clamp(0.9rem,1.8vw,1.05rem)] font-light leading-[1.9] mb-6'
H2_CLS = 'text-[clamp(1.2rem,3vw,1.7rem)] leading-[1.3] mt-12 mb-5'
H3_CLS = 'text-[1.1rem] leading-[1.3] mt-8 mb-3'
UL_CLS = 'list-disc pl-6 mb-6 space-y-2 text-[clamp(0.9rem,1.8vw,1.05rem)] font-light leading-[1.9]'
DATE = "September 2, 2026"
ISO = "2026-09-02"


def P(t): return f'<p class="{P_CLS}" style="color:var(--text-body)">{t}</p>'
def H2(t): return f'<h2 class="{H2_CLS}" style="font-family:var(--font-display);color:var(--text-heading)">{t}</h2>'
def H3(t): return f'<h3 class="{H3_CLS}" style="font-family:var(--font-display);color:var(--text-heading)">{t}</h3>'
def UL(items):
    lis = "\n".join(f"        <li>{it}</li>" for it in items)
    return f'<ul class="{UL_CLS}" style="color:var(--text-body)">\n{lis}\n      </ul>'


POSTS = [
    {
        "slug": "why-do-bad-things-keep-happening-to-me",
        "title": "Why Do Bad Things Keep Happening to Me? A Gentle Perspective",
        "breadcrumb": "Why Bad Things Keep Happening",
        "category": "SPIRITUALITY",
        "meta": "Feeling like bad things keep happening to you? A gentle spiritual perspective on hard seasons, patterns, and finding clarity, from Utopia Wellness & Gifts in North Vancouver.",
        "intro": [
            "If it feels like one hard thing keeps following another, you are not imagining the weight of it, and you are not being punished. Difficult seasons are real, and when several land close together, the mind naturally starts looking for a reason. This piece offers a gentler way to hold that question &mdash; not a formula, just a softer perspective.",
            "Sometimes what looks like a run of bad luck is a stretch of change that has not finished arranging itself yet. Clarity tends to come slowly, and usually after the hardest part has passed.",
        ],
        "body": [
            ("h2", "Hard Seasons Are Not a Verdict"),
            ("p", "A run of difficulty does not mean you did something wrong or that you are unlucky by nature. Life moves in seasons, and some are heavier than others. Naming a stretch as a season, rather than a permanent state, can make it a little easier to carry."),
            ("h2", "Looking for the Pattern, Gently"),
            ("p", "Sometimes repeated struggles share a quiet thread &mdash; a boundary that keeps getting crossed, a decision postponed, a relationship pattern that repeats. Noticing the thread is not about blame. It is about finding the one small thing that is actually yours to change."),
            ("h2", "What a Reflective Practice Can Offer"),
            ("p", "Journaling, a quiet walk, or a conversation with someone outside the situation can help you separate what is happening to you from what is yours to act on. A Clarity &amp; Guidance session offers the same &mdash; a calm hour to step back and see the shape of things, not a prediction."),
            ("h2", "One Small Step"),
            ("p", "When everything feels heavy, the goal is not to fix it all at once. Choose one honest, doable step and take it. Momentum, even tiny, tends to shift the feeling of being stuck more than any single answer does."),
            ("p", "If you would like a calm space to talk it through, our readers offer Clarity &amp; Guidance sessions at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver."),
        ],
        "faq": [
            ("Does a run of bad luck mean something is wrong with me?", "No. Difficult seasons happen to everyone and are not a verdict on your worth or a punishment. Naming it as a season rather than a permanent state can make it easier to move through."),
            ("Can a reading tell me why bad things keep happening?", "A reading will not give a single cause, but it can offer a calmer perspective and help you notice one pattern or step that is actually yours to change."),
            ("What if I am really struggling right now?", "If you are struggling, please reach out for support. In Canada you can call or text 988 to reach the Suicide Crisis Helpline, free and confidential, 24 hours a day."),
        ],
        "keywords": "why do bad things keep happening to me, hard season spiritual meaning, feeling stuck in life, why does everything go wrong, spiritual perspective on suffering",
    },
    {
        "slug": "common-dreams-explained-teeth-crush-nightmares",
        "title": "Common Dreams Explained: Teeth Falling Out, a Crush, and Nightmares",
        "breadcrumb": "Common Dreams Explained",
        "category": "DREAMS",
        "meta": "What common dreams mean: teeth falling out, dreaming about a crush, dreaming of the same person, and recurring nightmares. A grounded guide from Utopia in North Vancouver.",
        "intro": [
            "Dreams process the stress, desire, and change we carry through the day, which is why the same few themes come up again and again. They are not automatic prophecies, but they are worth listening to &mdash; the feeling in a dream usually matters more than the literal image.",
            "Here are the dreams people ask us about most, and a grounded way to read each one.",
        ],
        "body": [
            ("h2", "Teeth Falling Out"),
            ("p", "Dreams of teeth falling out are among the most common of all. They usually track anxiety about control, appearance, or words left unsaid &mdash; something you feel is slipping or that you are afraid to voice. They rarely have anything to do with your actual teeth."),
            ("h2", "Dreaming About a Crush"),
            ("p", "A crush dream often reflects attention you are already giving someone, or a quality in them you want more of in yourself. It says more about your own longing or focus than about what the other person feels."),
            ("h2", "Dreaming About the Same Person Repeatedly"),
            ("p", "When the same person keeps appearing, your mind is usually processing an unresolved feeling or a pattern that person represents &mdash; not necessarily a sign about them. Ask what they symbolize for you: safety, regret, excitement, closure."),
            ("h2", "Recurring Nightmares"),
            ("p", "Frequent nightmares are most often linked to stress, disrupted sleep, or difficult emotions being processed at night. Spiritually, they can flag something in waking life asking for attention. Practically, if they are affecting your sleep, it is worth mentioning to a doctor."),
            ("h2", "How to Work With a Dream"),
            ("p", "Write it down the same morning, before it fades. Note what was happening in your waking life, and look for the feeling rather than only the image. Over time, patterns become easier to read."),
            ("p", "Bring a dream that keeps returning to a Clarity &amp; Guidance session at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver."),
        ],
        "faq": [
            ("What does it mean to dream about teeth falling out?", "It usually reflects anxiety about control, appearance, or something you feel unable to say &mdash; not your actual teeth."),
            ("Why do I keep dreaming about the same person?", "Your mind is often processing an unresolved feeling or a pattern that person represents, rather than sending a literal message about them."),
            ("Why do I keep having nightmares?", "Frequent nightmares are usually tied to stress, sleep disruption, or emotions being processed at night. If they affect your sleep, mention them to a doctor."),
        ],
        "keywords": "dream meanings, teeth falling out dream, dreaming about a crush, dreaming about the same person, recurring nightmares, bad dreams meaning",
    },
    {
        "slug": "moon-retrograde-and-new-moon-rituals",
        "title": "Can the Moon Be in Retrograde? Plus Simple New Moon Rituals",
        "breadcrumb": "Moon &amp; New Moon Rituals",
        "category": "RITUALS",
        "meta": "Can the moon be in retrograde? A clear answer, plus simple new moon rituals and what to do on a new moon. Join a New Moon Circle at Utopia in North Vancouver.",
        "intro": [
            "One of the most common moon questions is whether the moon can be in retrograde &mdash; and the short answer is no. The moon never goes retrograde; it always moves in the same direction relative to Earth. What people usually mean is a planet in retrograde (like Mercury) or simply the moon&rsquo;s phases, which are a lovely, low-pressure way to keep a rhythm.",
            "Here is the plain version, plus simple new moon rituals you can actually finish in one evening.",
        ],
        "body": [
            ("h2", "Does the Moon Go Retrograde?"),
            ("p", "No. Retrograde describes the apparent backward motion of planets from our view on Earth. The moon does not do this. If someone mentions the moon and retrograde together, they usually mean a planet is retrograde during a particular moon phase, or they are thinking of the moon&rsquo;s changing phases."),
            ("h2", "Working With the New Moon"),
            ("p", "The new moon is traditionally a time for setting one clear intention &mdash; a fresh page. It pairs naturally with beginnings, which is why so many people use it to start something small and specific."),
            ("h2", "A Simple New Moon Ritual"),
            ("ul", [
                "Write one intention in the present tense &mdash; just one, not ten.",
                "Sit quietly with it for a few minutes.",
                "Keep it somewhere you will see it over the coming weeks.",
                "Take one small matching action within a day or two.",
            ]),
            ("h2", "What to Do on a New Moon (and What Not To)"),
            ("p", "Keep it simple and kind to yourself. One candle, one page, one honest sentence is plenty. There is no need for elaborate tools, and there is no wrong way to do it if the intention is sincere."),
            ("p", "We host New Moon Circles and carry simple ritual supplies in store. Dates are on our site &mdash; Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver."),
        ],
        "faq": [
            ("Can the moon be in retrograde?", "No. The moon never goes retrograde. Retrograde describes the apparent backward motion of planets like Mercury. People often mean a planet is retrograde during a moon phase, or simply the moon&rsquo;s phases."),
            ("What should I do on a new moon?", "The new moon suits setting one clear intention. Write it down, keep it visible, and take one small matching action within a day or two."),
            ("Do I have to follow the exact new moon date?", "The night of the new moon or the closest evening you can keep is fine. Consistency matters more than perfect timing."),
        ],
        "keywords": "can the moon be in retrograde, does the moon go retrograde, new moon ritual, what to do on a new moon, new moon intentions, moon phases meaning",
    },
    {
        "slug": "psychic-abilities-and-clairvoyance-explained",
        "title": "Psychic Abilities and Clairvoyance, Explained",
        "breadcrumb": "Psychic Abilities &amp; Clairvoyance",
        "category": "PSYCHIC GUIDANCE",
        "meta": "Psychic abilities and clairvoyance explained: what clairvoyance means, the difference between a psychic and a medium, and the types of intuitive ability. From Utopia, North Vancouver.",
        "intro": [
            "Psychic ability is an umbrella term for intuitive or extrasensory insight, and clairvoyance is one specific kind of it. If you have searched for what a clairvoyant is, or the difference between a psychic and a medium, this is the plain-language version without the mystique.",
            "None of this is about certainty or performance &mdash; at its best, it is a way of paying close attention and putting words to it.",
        ],
        "body": [
            ("h2", "What Is Clairvoyance?"),
            ("p", "Clairvoyance means &ldquo;clear seeing&rdquo; &mdash; receiving intuitive information as images, symbols, or inner pictures. It rarely looks like a dramatic vision; more often it is a quick mental image or impression that carries meaning."),
            ("h2", "The Types of Intuitive Ability"),
            ("ul", [
                "<strong>Clairvoyance:</strong> clear seeing &mdash; images and symbols.",
                "<strong>Clairaudience:</strong> clear hearing &mdash; words, phrases, inner sound.",
                "<strong>Clairsentience:</strong> clear feeling &mdash; sensing emotion or energy.",
                "<strong>Claircognizance:</strong> clear knowing &mdash; a sudden certainty without a picture.",
            ]),
            ("h2", "Psychic vs Medium"),
            ("p", "A psychic works with intuitive insight about a person&rsquo;s life, energy, or direction. A medium specifically works to connect with those who have passed. Not every psychic is a medium, though some practitioners offer both."),
            ("h2", "Can Anyone Develop These Abilities?"),
            ("p", "Intuition sits on a spectrum, and most people can strengthen their own perceptiveness with practice and attention &mdash; the same way any skill of noticing improves. Approaching it with curiosity rather than pressure tends to work best."),
            ("h2", "How Accurate Are Readings?"),
            ("p", "Accuracy varies by practitioner, and there is no scientific consensus that readings are literally predictive. Many people find real value in them as a space for reflection, validation, and perspective. Coming with curiosity rather than expecting a fixed forecast leads to the most useful experience."),
            ("p", "Curious to experience a session? Our readers offer Clarity &amp; Guidance sessions at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver."),
        ],
        "faq": [
            ("What is a clairvoyant?", "A clairvoyant reports the ability to receive intuitive information through &ldquo;clear seeing&rdquo; &mdash; images, symbols, or inner pictures &mdash; rather than through the ordinary five senses."),
            ("What is the difference between a psychic and a medium?", "A psychic works with intuitive insight about your life, energy, or direction. A medium specifically works to connect with those who have died. Some practitioners do both."),
            ("Can anyone develop psychic abilities?", "Intuition exists on a spectrum, and most people can strengthen their own perceptiveness with practice and attention. Curiosity works better than pressure."),
        ],
        "keywords": "clairvoyance, psychic abilities, psychic vs medium, types of psychic ability, what is a clairvoyant, clairsentience meaning, intuitive abilities",
    },
    {
        "slug": "signs-someone-is-manifesting-you-karmic-relationships",
        "title": "Signs Someone Is Manifesting You &amp; What a Karmic Relationship Is",
        "breadcrumb": "Manifesting You &amp; Karmic Bonds",
        "category": "LOVE & RELATIONSHIPS",
        "meta": "Signs someone may be manifesting you and what a karmic relationship really means. A grounded look at intense connections, from Utopia Wellness & Gifts in North Vancouver.",
        "intro": [
            "&ldquo;Signs someone is manifesting you&rdquo; and &ldquo;karmic relationship&rdquo; are two of the most emotionally charged searches in this space, and they often come from the same place: a connection that feels bigger than it can be explained. This is a grounded look at both &mdash; holding them loosely rather than as proof of anything.",
            "The honest starting point: these are subjective experiences, impossible to verify, and best used for self-reflection rather than as certainty about another person.",
        ],
        "body": [
            ("h2", "Signs People Associate With Being Manifested"),
            ("ul", [
                "Sudden, vivid dreams about a specific person.",
                "A strong, unexplained sense that they are thinking of you.",
                "Their name or a shared memory surfacing repeatedly out of nowhere.",
                "Repeating numbers or a song tied to them appearing often.",
            ]),
            ("p", "Hold these loosely. They are meaningful to notice, but they are not evidence of what someone else is doing or feeling. Used well, they are a mirror for your own attention."),
            ("h2", "What Is a Karmic Relationship?"),
            ("p", "A karmic relationship is usually described as an intense, often turbulent connection that teaches you something &mdash; a bond that feels fated but is not always peaceful. Many people use the term for relationships that repeat a familiar pattern until the lesson lands."),
            ("h2", "Karmic vs Soulmate vs Twin Flame"),
            ("p", "People use these words differently. Broadly, a karmic bond is framed as a lesson, a soulmate as an easeful fit, and a twin flame as an intense mirror. In a session, we work with your actual relationship rather than which label fits."),
            ("h2", "A Healthier Question to Ask"),
            ("p", "Instead of &ldquo;are they manifesting me,&rdquo; a more useful question is &ldquo;what is this connection teaching me, and what is mine to do?&rdquo; That keeps the focus on the part you can actually act on."),
            ("p", "For a calm space to make sense of an intense connection, book a Clarity &amp; Guidance session at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver."),
        ],
        "faq": [
            ("What are signs someone is manifesting you?", "People commonly describe vivid dreams, an unexplained sense of being thought about, or a name and memories resurfacing. These are subjective, impossible to verify, and best held loosely as self-reflection."),
            ("What is a karmic relationship?", "It is usually described as an intense, often turbulent connection that teaches a lesson &mdash; a bond that feels fated but is not always peaceful."),
            ("What is the difference between a karmic relationship and a soulmate?", "People use the words differently, but broadly a karmic bond is framed as a lesson and a soulmate as an easeful fit. A reading works with your actual relationship rather than the label."),
        ],
        "keywords": "signs someone is manifesting you, karmic relationship meaning, karmic vs soulmate, twin flame vs karmic, intense connection meaning, is someone thinking of me",
    },
    {
        "slug": "year-of-the-snake-chinese-zodiac",
        "title": "Year of the Snake: What the Chinese Zodiac Sign Means",
        "breadcrumb": "Year of the Snake",
        "category": "ASTROLOGY",
        "meta": "What the Year of the Snake means in the Chinese zodiac: Snake traits, compatibility, and how zodiac years work. A clear guide from Utopia Wellness & Gifts, North Vancouver.",
        "intro": [
            "The Snake is one of the twelve animals of the Chinese zodiac, and people born in a Snake year are traditionally described as wise, intuitive, and quietly determined. Interest in Snake-year meanings stays steady year-round, whether or not the current year is a Snake year, because people look up their own birth-year sign.",
            "Here is a clear guide to the Snake sign, its traits, and how Chinese zodiac years actually work.",
        ],
        "body": [
            ("h2", "How Chinese Zodiac Years Work"),
            ("p", "The Chinese zodiac runs on a twelve-year cycle, assigning one of twelve animals to each year. Your sign is set by your birth year (with a note that the Chinese New Year falls in late January or February, so people born in early year need to check the exact date)."),
            ("h2", "Traits of the Snake"),
            ("p", "Snakes are traditionally seen as wise, perceptive, and elegant, with strong intuition and a private nature. They are often described as thoughtful planners who prefer to observe before acting, and who value depth over noise."),
            ("h2", "Snake Compatibility"),
            ("p", "In popular Chinese astrology, the Snake is often paired well with the Ox and the Rooster, who share its steadiness and focus. As with any zodiac system, compatibility is a starting point for reflection rather than a rule."),
            ("h2", "Using Your Zodiac Year"),
            ("p", "Your Chinese zodiac sign is best used the way any sign is &mdash; as language for tendencies and self-understanding, not a fixed script. It pairs interestingly with Western astrology, since the two systems describe different layers."),
            ("p", "Curious how your signs fit together across systems? Ask about an astrology-focused Clarity &amp; Guidance session at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver."),
        ],
        "faq": [
            ("What are people born in the Year of the Snake like?", "They are traditionally described as wise, intuitive, private, and quietly determined &mdash; thoughtful planners who prefer to observe before acting."),
            ("How do I know my Chinese zodiac sign?", "It is set by your birth year on a twelve-year cycle. Because the Chinese New Year falls in late January or February, people born early in the year should check the exact date."),
            ("Which signs are most compatible with the Snake?", "In popular Chinese astrology, the Snake is often paired well with the Ox and the Rooster, though compatibility is best used as a starting point for reflection."),
        ],
        "keywords": "year of the snake, chinese zodiac snake, snake zodiac traits, chinese zodiac years, snake compatibility, what is my chinese zodiac sign",
    },
]


def render_body(blocks):
    out = []
    for kind, val in blocks:
        if kind == "h2": out.append("      " + H2(val))
        elif kind == "h3": out.append("      " + H3(val))
        elif kind == "p": out.append("      " + P(val))
        elif kind == "ul": out.append("      " + UL(val))
    return "\n".join(out)


def render_faq(faq, keywords):
    parts = ["      " + H2("Frequently Asked Questions")]
    for q, a in faq:
        parts.append("      " + H3(q))
        parts.append("      " + P(a))
    parts.append('      <p class="text-[.8rem] font-light mt-8" style="color:var(--text-muted)"><strong>People also search for:</strong> ' + keywords + "</p>")
    return "\n".join(parts)


def faq_schema(faq):
    def esc(s):
        s = re.sub(r"<[^>]+>", "", s)
        s = (s.replace("&amp;", "&").replace("&mdash;", "-").replace("&ndash;", "-")
               .replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&rsquo;", "'").replace("&lsquo;", "'"))
        s = s.replace("\\", "\\\\").replace('"', '\\"')
        return s
    items = ",".join('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (esc(q), esc(a)) for q, a in faq)
    return '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + items + ']}</script>'


def main():
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        tpl = f.read()
    tpl = re.sub(r"<!-- ═+\s*🔧 REPLACE:.*?═+ -->\n?", "", tpl, flags=re.S)
    tpl = re.sub(r"\s*<!-- 🔧 FAQ SCHEMA.*?-->", "", tpl, flags=re.S)
    tpl = tpl.replace('<!-- STRUCTURED DATA — 🔧 REPLACE: {{TITLE}}, {{SLUG}}, {{DATE_ISO}} (YYYY-MM-DD) -->', '<!-- STRUCTURED DATA -->')
    tpl = re.sub(r"[ \t]*<!--[^\n]*🔧[^\n]*-->\n?", "", tpl)

    for post in POSTS:
        html = tpl
        html = html.replace("{{TITLE}}", post["title"])
        html = html.replace("{{META_DESCRIPTION}}", post["meta"])
        html = html.replace("{{SLUG}}", post["slug"])
        html = html.replace("{{BREADCRUMB}}", post["breadcrumb"])
        html = html.replace("{{DATE_ISO}}", ISO)
        html = html.replace("{{DATE}}", DATE)
        intro_html = "\n".join("      " + P(p) for p in post["intro"])
        html = html.replace("{{CONTENT_INTRO}}", intro_html)
        body = render_body(post["body"]) + "\n\n" + render_faq(post["faq"], post["keywords"])
        html = html.replace("{{CONTENT_BODY}}", body)
        html = html.replace("</body>", faq_schema(post["faq"]) + "\n</body>")
        with open(os.path.join(BLOG_DIR, post["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"wrote {post['slug']}.html")


if __name__ == "__main__":
    main()
