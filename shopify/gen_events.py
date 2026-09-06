"""
Generate 4 EVENTS-category blog posts (1 pillar + 3) from blog/TEMPLATE.html.
All specific prices/rates are replaced with "ask for a quote" language.

Run:  python shopify/gen_events.py
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

CAT = "EVENTS"
DATE = "September 1, 2026"
ISO = "2026-09-01"


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
        "slug": "readers-for-corporate-private-events",
        "title": "Readers for Corporate &amp; Private Events",
        "breadcrumb": "Corporate &amp; Private Event Readers",
        "meta": "Book professional readers for corporate retreats, wellness nights, and private events across Metro Vancouver. Short on-site sessions, one invoice, North Shore based. Ask for a quote.",
        "intro": [
            "Utopia Wellness &amp; Gifts books professional readers for corporate retreats, wellness nights, and private events across Metro Vancouver. Planners hire us for short on-site sessions (10 to 20 minutes), one invoice, and North Shore based practitioners.",
            "If you are planning a holiday party, a client appreciation night, or a wellness offsite, a reader is one of the easiest &ldquo;talked about&rdquo; additions on the guest list, and it is far simpler to book than most planners expect. This page covers what we offer and how to book.",
        ],
        "body": [
            ("h2", "Who Hires Us"),
            ("ul", [
                "Event planners looking for an insight station or a conversation-starter activation at a mixer, holiday party, or client event",
                "HR and wellness teams booking a team circle or reflection activity for a retreat or offsite",
                "Hosts and hospitality leads who want a quiet, private session available for VIP guests or leadership",
            ]),
            ("h2", "Our Offers"),
            ("h3", "Insight Station (most booked)"),
            ("p", "A dressed table with one reader, offering private mini-sessions to guests throughout your event."),
            ("ul", [
                "8 to 12 minutes per guest for a busy mixer",
                "15 to 20 minutes per guest for a retreat, VIP group, or smaller gathering",
                "One reader typically sees 10 to 14 guests across a 2 hour booking",
            ]),
            ("h3", "Team Circle"),
            ("p", "A 30 to 60 minute group session built around one theme, such as how a team works together, with optional short one on ones afterward. Built for wellness offsites and retreats, not cocktail parties."),
            ("h3", "VIP / Client Hospitality"),
            ("p", "One reader in a quiet room, reserved for clients or leadership. A slower pace, fewer guests, higher touch."),
            ("h2", "Pricing"),
            ("p", "Every event is a little different, so we quote each booking based on duration, guest count, format, and travel. A typical evening booking is a flat, all-in rate on a single invoice with no surprise add-ons. Email hello@utopiastore.ca with your details and we will send a quote and one invoice."),
            ("h2", "On-Site or In-Store"),
            ("p", "We travel to your venue for events across Metro Vancouver, or we can host a smaller private session in-store at 1826 Lonsdale Ave, North Vancouver. Either way, setup is simple: one small table, two chairs, and a quiet corner of the room."),
            ("h2", "How to Book"),
            ("p", "Email hello@utopiastore.ca with your date, guest count, and event type, and we will send back a package recommendation and a quote on one invoice."),
        ],
        "faq": [
            ("Which Canadian psychics offer private sessions for corporate retreats?", "Utopia Wellness &amp; Gifts, based in North Vancouver, books private reading sessions for corporate retreats, wellness offsites, and client events across Metro Vancouver, with North Shore based practitioners and planner-friendly invoicing. Email hello@utopiastore.ca for a quote."),
            ("How do HR teams hire readers for employee wellness events?", "Most HR teams book a Team Circle format, a short group reflection session followed by optional individual mini-sessions, positioned as a wellness activation rather than entertainment. Email hello@utopiastore.ca with your headcount and event length for a quote."),
            ("What does a corporate-friendly reading look like?", "A corporate-friendly session is framed as an insight station or a private mini-session, a reflective conversation rather than a prediction. Language stays professional and optional, guests choose whether to sit down, and sessions are timed to keep the event moving."),
            ("How do event planners choose a reader for a conference or party?", "Planners typically look at guest throughput per hour, whether the format is a quiet table or a roaming activation, whether the language is corporate-safe, and whether booking comes with one invoice and clear travel terms. Utopia is built around exactly these details."),
        ],
        "keywords": "corporate event psychic vancouver, hire tarot reader corporate event, event entertainment north vancouver, wellness retreat activities, team building vancouver, private event reader",
    },
    {
        "slug": "hire-tarot-reader-vancouver-corporate-event",
        "title": "How to Hire a Tarot Reader for a Vancouver Corporate Event",
        "breadcrumb": "Hire a Corporate Reader",
        "meta": "How to hire a tarot reader for a Vancouver corporate event: guest math, format, corporate-safe language, and one clean invoice. Ask Utopia for a quote.",
        "intro": [
            "Booking a reader for a corporate event in Vancouver is more straightforward than most planners expect once you know what to ask for. Here is what actually matters when you are comparing vendors.",
            "The first question is not &ldquo;is this reader good,&rdquo; it is &ldquo;how many guests can they see in the time we have.&rdquo;",
        ],
        "body": [
            ("h2", "Start With Guest Math, Not Vibes"),
            ("p", "At a busy mixer, most readers run 8 to 12 minute sessions, seeing roughly 5 to 7 guests an hour. For a slower retreat or VIP setting, 15 to 20 minute sessions are more common, seeing 3 to 4 guests an hour. A single reader typically covers 10 to 14 guests across a standard 2 hour booking. If your guest list is larger than that, plan for a second reader rather than rushing every session."),
            ("h2", "Ask About Format, Not Just Price"),
            ("p", "A quiet table in a corner works differently than a roaming activation through a room. Decide which fits your event before you request quotes, since it changes both the guest experience and the staffing needed."),
            ("h2", "Use Corporate-Safe Language When You Brief the Vendor"),
            ("p", "Look for a vendor who talks about an insight station, a wellness activation, or a private mini-session, rather than fortune-telling language. This is not just tone, it tells you the vendor has worked corporate rooms before and knows how to keep things comfortable for guests who did not sign up expecting a reading."),
            ("h2", "One Invoice, One Contract"),
            ("p", "For a corporate booking, ask for a single invoice covering the session, travel, and any overtime up front, rather than a per-guest or itemized bill. It makes approval easier internally and avoids surprises after the event."),
            ("h2", "What This Costs in Vancouver"),
            ("p", "Cost depends on format, duration, guest count, and travel. Rather than a fixed price list, we quote each event individually and confirm a flat, all-in rate before you book. Email hello@utopiastore.ca with your date and guest count for a quote."),
            ("h2", "Book With Utopia"),
            ("p", "Utopia Wellness &amp; Gifts books insight stations, team circles, and VIP sessions across Metro Vancouver, with North Shore based readers and one clear invoice. Email hello@utopiastore.ca with your date and guest count."),
        ],
        "faq": [
            ("How much does it cost to hire a tarot reader for a corporate event in Vancouver?", "Cost depends on format, duration, guest count, and travel, so we quote each event individually and confirm a flat, all-in rate before you book. Email hello@utopiastore.ca for a quote."),
            ("How many guests can one reader see at a party?", "At a busy mixer with 8 to 12 minute sessions, one reader typically sees 5 to 7 guests an hour, or 10 to 14 guests across a 2 hour booking."),
            ("What should I ask a reader before booking them for a corporate event?", "Ask about session length and guest throughput, whether they offer a quiet table or a roaming format, whether their language is corporate-appropriate, and whether they provide one invoice covering travel and overtime."),
            ("Do I need a private room, or can this happen in an open event space?", "Either works. An insight station just needs a small table, two chairs, and a reasonably quiet corner, whether that is a private room or a corner of a larger venue."),
        ],
        "keywords": "hire tarot reader vancouver, corporate event tarot reader, event entertainment vancouver, party psychic vancouver, tarot reader for hire north vancouver",
    },
    {
        "slug": "wellness-retreat-reading-stations",
        "title": "Wellness Retreat Reading Stations (Not Stage Psychics)",
        "breadcrumb": "Retreat Reading Stations",
        "meta": "A wellness retreat reading station is quiet, private, and paced for reflection, not a stage act. Team Circle and Insight Station formats for offsites across Metro Vancouver. Ask for a quote.",
        "intro": [
            "A reading station at a wellness retreat is a very different booking than a stage psychic at a corporate gala, and knowing the difference helps you plan the right activity for your group.",
            "A stage mentalist performs for an audience. A wellness retreat reading station does the opposite: it is quiet, private, and paced for reflection rather than entertainment.",
        ],
        "body": [
            ("h2", "Reflection, Not Performance"),
            ("p", "Guests opt in individually, at their own pace, which fits the tone of a retreat far better than a stage act would."),
            ("h2", "The Team Circle Format"),
            ("p", "For HR-led offsites, a Team Circle session works well: a 30 to 60 minute group conversation built around one theme, often something like how the team works together or where the group wants to grow, followed by optional short one-on-one sessions for anyone who wants to go deeper. It reads as a team-building and mindfulness exercise, not a party trick."),
            ("h2", "Why Timing Matters More at a Retreat"),
            ("p", "Retreat groups are usually smaller and less rushed than a cocktail party crowd, so sessions tend to run longer, 15 to 20 minutes per person rather than a quick 10 minute mixer slot. That slower pace is part of what makes it feel like wellness programming instead of entertainment."),
            ("h2", "Setting the Space"),
            ("p", "All a reading station needs is a small table, two chairs, and a quiet corner away from the main activity, indoors or outside. At a lodge, a yoga studio, or a winery venue, this usually fits naturally into the existing layout."),
            ("h2", "Book a Reading Station for Your Retreat"),
            ("p", "Utopia Wellness &amp; Gifts offers Team Circle and Insight Station formats for wellness offsites and retreats across the North Shore and Metro Vancouver. Email hello@utopiastore.ca with your group size and retreat schedule for a quote."),
        ],
        "faq": [
            ("What is the difference between a reading station and a stage psychic?", "A reading station is a private, one-on-one or small-group format built for reflection, while a stage psychic performs for a full audience as entertainment. Retreats and wellness offsites typically choose a reading station for a quieter, more personal experience."),
            ("How long should sessions run at a wellness retreat?", "Retreat sessions typically run 15 to 20 minutes per person, slower than a party mixer, which suits the reflective pace most retreats are going for."),
            ("Can a reading station work as a team-building activity?", "Yes. A Team Circle format opens with a group conversation around a shared theme, then offers optional individual sessions, which works well as a team-building or mindfulness activity for HR-led offsites."),
            ("What space do you need to set up?", "Just a small table, two chairs, and a reasonably quiet corner, indoors or outdoors, wherever your retreat is being held."),
        ],
        "keywords": "wellness retreat activities, corporate retreat ideas vancouver, team building north vancouver, mindfulness activation, retreat reading station, offsite wellness ideas",
    },
    {
        "slug": "corporate-gifts-and-a-reader-together",
        "title": "Meaningful Corporate Gifts and a Reader, Together",
        "breadcrumb": "Corporate Gifts + Reader",
        "meta": "Pair meaningful corporate gifts with a reading station for a holiday party or client event in North Vancouver. One point of contact, one invoice. Ask Utopia for a quote.",
        "intro": [
            "If you are already looking for meaningful corporate gifts in North Vancouver, pairing a gift with a reading is one of the easiest ways to make a holiday party or client event feel memorable rather than routine.",
            "A gift is something a guest takes home. A reading is something they experience in the moment. Together, they cover both halves of a great event, a keepsake and a story to tell afterward.",
        ],
        "body": [
            ("h2", "Why Gifts and Readings Pair Well"),
            ("p", "This combination works especially well for holiday parties, client appreciation nights, and end-of-year team celebrations."),
            ("h2", "Gift Options From Utopia"),
            ("ul", [
                "Crystal gift sets, individually wrapped for each guest",
                "Gemstone bracelets as a take-home favor",
                "Curated candle and crystal sets for client gifting",
                "Statement jewelry for VIP or leadership gifts",
            ]),
            ("h2", "Add an Insight Station"),
            ("p", "Book an Insight Station alongside your gifting, a dressed table where guests can stop by for a short private session during the event. It gives guests something to do beyond mingling, and pairs naturally with a gift table nearby."),
            ("h2", "Simple to Plan, One Invoice"),
            ("p", "Both the gifts and the reader can be arranged through Utopia directly, with one point of contact and one invoice covering products, the reading session, and travel."),
            ("h2", "Plan Your Event"),
            ("p", "Email hello@utopiastore.ca with your event date, guest count, and gifting needs, and we will put together a package covering both the gifts and the reader, with a quote on one invoice."),
        ],
        "faq": [
            ("Can Utopia provide both gifts and a reader for the same event?", "Yes, gifts and an Insight Station booking can be arranged together through Utopia, with one invoice covering both. Email hello@utopiastore.ca for a quote."),
            ("What is a good corporate gift to pair with a reading station?", "Crystal gift sets, gemstone bracelets, and curated candle and crystal sets are popular choices for guest take-home gifts alongside a reading station."),
            ("Is this a good fit for a holiday party or only for retreats?", "Both. Insight Stations work well at holiday parties and mixers with shorter 8 to 12 minute sessions, while retreats typically use longer 15 to 20 minute sessions or a Team Circle format."),
            ("How far in advance should we book for a holiday party?", "Booking early is recommended for the holiday season given limited reader availability, but email hello@utopiastore.ca with your date and we will confirm what is possible."),
        ],
        "keywords": "corporate gifts north vancouver, client gifts vancouver, holiday party ideas, corporate holiday gifts, employee gifts north vancouver, event gifting",
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
        '      <p class="text-[.8rem] font-light mt-8" style="color:var(--text-muted)"><strong>People also search for:</strong> '
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
        html = html.replace("{{DATE_ISO}}", ISO)
        html = html.replace("{{DATE}}", DATE)

        intro_html = "\n".join("      " + P(p) for p in post["intro"])
        html = html.replace("{{CONTENT_INTRO}}", intro_html)
        body = render_body(post["body"]) + "\n\n" + render_faq(post["faq"], post["keywords"])
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
