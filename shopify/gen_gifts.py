"""
Generate 16 GIFTS-category blog posts (1 pillar + 15 topics) from blog/TEMPLATE.html.

Run:  python shopify/gen_gifts.py
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

CAT = "GIFTS"
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


# body blocks: ('h2',t) ('h3',t) ('p',t) ('ul',[items])
POSTS = [
    {
        "slug": "best-gift-shop-north-vancouver-lonsdale",
        "title": "Best Gift Shop in North Vancouver (Lonsdale)",
        "breadcrumb": "Best Gift Shop North Vancouver",
        "meta": "The best gift shop on Lonsdale in North Vancouver for jewelry, crystals, and intention-based gifts you can see, wrap, and give the same day. 1826 Lonsdale Ave.",
        "intro": [
            "If you want a gift someone will actually remember, the best gift shop on Lonsdale in North Vancouver is one where you can see the piece in person, have it wrapped, and walk out with it the same day. Utopia Wellness &amp; Gifts, at 1826 Lonsdale Ave, North Vancouver, BC V7M 2J9, specializes in jewelry, crystals, and intention-based gifts &mdash; the kind of present that feels personal, not generic.",
            "A traditional gift shop leans on mugs, candles, and seasonal knick-knacks; an online gift site can&rsquo;t let you hold the piece, feel the weight of a stone, or ask a real person which crystal fits the moment. Utopia sits in between: a curated, walk-in store where every gift &mdash; a piece of jewelry, a crystal, a small ritual set &mdash; has a story you can explain when you hand it over.",
        ],
        "body": [
            ("h2", "Address, hours &amp; parking"),
            ("p", "We&rsquo;re located at 1826 Lonsdale Ave, North Vancouver, BC V7M 2J9, with free parking at the back of the store. Hours can shift around events and readings, so the most current hours are always listed on our Google Business Profile and utopiastore.ca &mdash; worth a quick check before a special trip."),
            ("h2", "Price ranges we carry"),
            ("p", "Utopia carries gifts across every budget: small crystals, candles, and card decks generally sit under $25; jewelry pieces, curated gift sets, and larger crystals typically run $25&ndash;$100; and statement jewelry or bundled gift + experience packages can go beyond that. There&rsquo;s a real gift here whether you&rsquo;re grabbing a hostess token or a milestone present."),
            ("h2", "How we&rsquo;re different from other North Van gift stops"),
            ("p", "If you want tourist souvenirs, try the Quay. If you want Edgemont&rsquo;s boutique staples, head up to Edgemont Village. If you want a gift with meaning &mdash; jewelry, a crystal, a small ritual set &mdash; Utopia on Lonsdale is built for exactly that. Shop gifts in-store or book a Clarity Session to pair a gift with a short reading &mdash; both are welcome reasons to walk through our door."),
        ],
        "faq": [
            ("Is Utopia a gift shop or a crystal shop?", "Both. Utopia Wellness &amp; Gifts is a metaphysical gift shop &mdash; crystals, jewelry, tarot and oracle decks, candles, and intention-based gifts all live under one roof, alongside in-store tarot and energy work sessions."),
            ("Do you wrap gifts?", "Yes &mdash; ask at the counter and we&rsquo;ll wrap your purchase before you leave, so you can go straight from browsing to giving."),
            ("Is there parking?", "Yes, free parking is available at the back of the store, in addition to street parking along Lonsdale."),
            ("Do I need an appointment to shop for a gift?", "No &mdash; walk-ins are always welcome for shopping. Appointments are only needed if you want to book a reading or energy session."),
        ],
        "keywords": "best gift shop north vancouver, gift shop lonsdale, gifts near me north vancouver, unique gifts north vancouver, local gifts north vancouver, handmade gifts north vancouver",
    },
    {
        "slug": "birthday-gifts-north-vancouver",
        "title": "Birthday Gifts North Vancouver",
        "breadcrumb": "Birthday Gifts",
        "meta": "Birthday gifts in North Vancouver that feel considered, not last-minute: birthstone crystals, statement jewelry, and ritual gift sets, wrapped same-day at Utopia on Lonsdale.",
        "intro": [
            "Looking for a birthday gift in North Vancouver that doesn&rsquo;t feel like everyone else&rsquo;s? Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave stocks birthstone-adjacent crystals, statement jewelry, and small ritual gift sets you can pick up, have wrapped, and give the same day.",
            "This page is for anyone shopping for a friend, partner, sibling, or coworker&rsquo;s birthday and wants something that feels considered rather than last-minute &mdash; most birthday gifts here land between $20 and $80, with a few standout jewelry pieces above that. Shop birthday gifts in-store or book a birthday Clarity Session as an add-on experience gift.",
        ],
        "body": [
            ("h2", "Gifts under $25"),
            ("ul", ["Tumbled crystal sets matched to the birthday month or star sign", "Mini oracle decks", "Intention candles", "Palo santo or sage bundles", "Crystal keychains or pocket stones"]),
            ("h2", "Gifts under $50"),
            ("ul", ["Beaded gemstone bracelets", "Small pendant necklaces", "Curated &ldquo;birthday ritual&rdquo; gift sets (candle + crystal + card)", "Singing bowl minis"]),
            ("h2", "If they already have everything"),
            ("p", "Pair a piece of jewelry or a crystal with a Clarity Session booking &mdash; an experience gift, not another object to store."),
        ],
        "faq": [
            ("What&rsquo;s a good birthday gift if I don&rsquo;t know their star sign?", "Choose a universally-loved option like a clear quartz (amplifying, all-purpose) or a scented intention candle &mdash; both work regardless of birth month."),
            ("Can I get a birthday gift wrapped on the spot?", "Yes, gift wrapping is available at checkout."),
            ("Do you have gifts for milestone birthdays (30th, 40th, etc.)?", "Yes &mdash; ask in-store for our jewelry and larger crystal pieces, which suit a bigger milestone moment."),
        ],
        "keywords": "birthday gifts for her north vancouver, birthday gifts north vancouver, unique gifts north vancouver, jewelry gifts north vancouver",
    },
    {
        "slug": "housewarming-host-gifts-lonsdale",
        "title": "Host &amp; Housewarming Gifts Lonsdale",
        "breadcrumb": "Housewarming Gifts",
        "meta": "The best housewarming gifts near Lonsdale: home-cleansing sets, candles, and small décor crystals that add warmth without clutter. Wrapped same-day at Utopia North Vancouver.",
        "intro": [
            "The best housewarming gift near Lonsdale is one that adds warmth to a new home without adding clutter. Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave carries home-cleansing sets, candles, and small décor crystals made for exactly this moment.",
            "This page is for anyone invited to a housewarming, dinner party, or new-home visit in North Vancouver &mdash; most host gifts here fall between $15 and $45, easy to grab on your way to the door. Shop housewarming gifts or ask about a home-blessing style bundle at the counter.",
        ],
        "body": [
            ("h2", "Gifts under $25"),
            ("ul", ["Sage or palo santo bundles", "Small selenite or amethyst clusters for the home", "Intention candles", "Mini singing bowls"]),
            ("h2", "Gifts under $50"),
            ("ul", ["Home energy-cleansing gift sets (sage + selenite + candle)", "Decorative crystal clusters", "Larger singing bowls"]),
            ("h2", "If they already have everything"),
            ("p", "A &ldquo;new home&rdquo; energy-cleansing set is genuinely useful even for someone with a fully furnished house &mdash; it&rsquo;s an experience, not a decoration."),
        ],
        "faq": [
            ("What&rsquo;s a good housewarming gift that isn&rsquo;t wine or flowers?", "A cleansing bundle (sage, palo santo, or a small crystal cluster) is a popular alternative &mdash; it welcomes a new space without needing a vase."),
            ("Is there something appropriate for a first apartment vs. a family home?", "Smaller items like sage bundles or tumbled stones suit a first apartment; larger crystal clusters or singing bowls suit a family home with more room to display them."),
            ("Can you wrap housewarming gifts?", "Yes, we wrap gifts at checkout on request."),
        ],
        "keywords": "housewarming gifts north vancouver, host gifts lonsdale, gifts near me north vancouver, local gifts north vancouver",
    },
    {
        "slug": "mothers-day-gifts-north-vancouver",
        "title": "Mother&rsquo;s Day Gifts North Vancouver",
        "breadcrumb": "Mother&rsquo;s Day Gifts",
        "meta": "Mother's Day gifts in North Vancouver your mom will actually wear or use: jewelry, rose quartz, and curated gift sets, wrapped same-day at Utopia on Lonsdale.",
        "intro": [
            "For Mother&rsquo;s Day, the best gifts in North Vancouver are ones your mom will actually wear or use &mdash; not another candle she&rsquo;ll never light. Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave carries jewelry, crystals, and gift sets built for this exact occasion, with wrapping available same-day.",
            "This page is for anyone shopping for a mother, grandmother, or mother figure &mdash; Mother&rsquo;s Day gifts here typically range from $25 to $120 depending on whether you&rsquo;re choosing jewelry or a smaller crystal gift. Shop Mother&rsquo;s Day gifts in-store or book a mother-daughter Clarity Session as a shared experience gift.",
        ],
        "body": [
            ("h2", "Gifts under $25"),
            ("ul", ["Rose quartz (the &ldquo;love&rdquo; stone) tumbled pieces", "Intention candles", "Small oracle decks", "Crystal keychains"]),
            ("h2", "Gifts under $50"),
            ("ul", ["Gemstone bracelets or pendant necklaces", "Curated &ldquo;for Mom&rdquo; gift sets", "Larger rose quartz or amethyst pieces"]),
            ("h2", "If she already has everything"),
            ("p", "Book a Clarity Session for two &mdash; a reading or energy session you can do together is a gift she can&rsquo;t buy herself."),
        ],
        "faq": [
            ("What crystal is best for a Mother&rsquo;s Day gift?", "Rose quartz is the most popular choice, traditionally associated with love, warmth, and nurturing."),
            ("Do you have jewelry specifically for moms?", "Yes &mdash; ask in-store for our current jewelry selection; pendant necklaces and bracelets are popular Mother&rsquo;s Day picks."),
            ("Can I book something to do with my mom instead of buying an object?", "Yes, a shared Clarity Session or reading is a popular alternative to a physical gift."),
        ],
        "keywords": "mother's day gifts north vancouver, gifts for mom, meaningful gifts vancouver, jewelry gifts north vancouver",
    },
    {
        "slug": "christmas-holiday-gift-guide-north-vancouver",
        "title": "Christmas &amp; Holiday Gift Guide North Vancouver",
        "breadcrumb": "Holiday Gift Guide",
        "meta": "A North Vancouver holiday gift guide: stocking stuffers through statement gifts, wrapped same-day at Utopia on Lonsdale. A walk-in alternative to online holiday shipping.",
        "intro": [
            "For holiday shopping in North Vancouver, Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave is a one-stop, walk-in alternative to online holiday shipping &mdash; pick a gift, get it wrapped, and it&rsquo;s under the tree the same day.",
            "This page is for last-minute and early holiday shoppers alike, covering stocking stuffers through statement gifts, generally $10 to $100+. Shop the holiday gift guide in-store or book a Clarity Session as a holiday gift certificate.",
        ],
        "body": [
            ("h2", "Gifts under $25"),
            ("ul", ["Stocking-stuffer crystals", "Mini oracle decks", "Holiday-scented intention candles", "Sage or palo santo bundles"]),
            ("h2", "Gifts under $50"),
            ("ul", ["Gemstone bracelets", "Curated holiday gift sets", "Singing bowls"]),
            ("h2", "If they already have everything"),
            ("p", "A Clarity Session gift certificate solves the &ldquo;impossible to shop for&rdquo; relative every year."),
        ],
        "faq": [
            ("Do you have stocking stuffers?", "Yes &mdash; small crystals, mini decks, and candles are popular stocking-stuffer picks."),
            ("Can I buy a gift certificate for a reading?", "Yes, ask in-store about gift certificates for tarot, palmistry, or energy sessions."),
            ("How late can I shop for a last-minute Christmas gift?", "Check current hours on our Google Business Profile or utopiastore.ca, especially in the days leading up to Christmas."),
        ],
        "keywords": "christmas gifts north vancouver, holiday gift guide north vancouver, last minute gifts north vancouver, unique gifts north vancouver",
    },
    {
        "slug": "last-minute-gifts-lonsdale",
        "title": "Last-Minute Gifts Near Lonsdale",
        "breadcrumb": "Last-Minute Gifts",
        "meta": "Need a gift today near Lonsdale? Utopia at 1826 Lonsdale Ave has ready-to-go jewelry, crystals, and gift sets plus wrapping, so you can shop and leave in minutes.",
        "intro": [
            "If you need a gift today, not in three business days, the fastest option near Lonsdale is a walk-in store. Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave has ready-to-go jewelry, crystals, and gift sets &mdash; plus wrapping &mdash; so you can shop and leave in minutes.",
            "This page is for anyone who forgot, ran out of time, or just prefers shopping in person &mdash; most grab-and-go gifts here are $15 to $60. Shop last-minute gifts now or grab a gift certificate for a reading if you&rsquo;re out of time entirely.",
        ],
        "body": [
            ("h2", "Gifts under $25"),
            ("ul", ["Tumbled crystals", "Candles", "Small oracle decks", "Sage bundles"]),
            ("h2", "Gifts under $50"),
            ("ul", ["Ready-made gift sets", "Jewelry pieces already on display", "Singing bowl minis"]),
            ("h2", "If they already have everything"),
            ("p", "A gift certificate takes 30 seconds to buy and solves the problem instantly."),
        ],
        "faq": [
            ("Can I buy and wrap a gift in one quick visit?", "Yes &mdash; that&rsquo;s exactly what walk-in shopping and in-store wrapping are for."),
            ("Is parking easy for a quick stop?", "Yes, free parking is available at the back of the store in addition to street parking on Lonsdale."),
            ("Do you sell gift certificates for last-minute situations?", "Yes, gift certificates are available in-store for both products and readings."),
        ],
        "keywords": "last minute gifts north vancouver, gifts near me north vancouver, gift shop lonsdale",
    },
    {
        "slug": "teacher-coworker-gifts-under-30",
        "title": "Teacher &amp; Coworker Gifts Under $30",
        "breadcrumb": "Gifts Under $30",
        "meta": "Thoughtful teacher and coworker gifts under $30 in North Vancouver: small crystals, candles, and compact gift sets, perfect for Secret Santa or end-of-year. Utopia on Lonsdale.",
        "intro": [
            "For teacher and coworker gifts, the goal is thoughtful without being over-the-top. Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave keeps a dedicated selection of gifts under $30 &mdash; small, meaningful, and appropriate for a group or an individual.",
            "This page is for end-of-year teacher gifts, Secret Santa exchanges, or a &ldquo;just because&rdquo; coworker gift &mdash; everything here is priced to stay comfortably under $30. Shop gifts under $30 in-store.",
        ],
        "body": [
            ("h2", "Gifts under $25"),
            ("ul", ["Small tumbled crystals", "Mini candles", "Pocket-sized oracle cards", "Crystal keychains"]),
            ("h2", "Gifts $25&ndash;$30"),
            ("ul", ["Small gemstone bracelets", "Compact gift sets (candle + crystal)"]),
            ("h2", "If it&rsquo;s for a group or office exchange"),
            ("p", "Small individually-wrapped crystals or candles work well as a consistent, affordable option across a whole team."),
        ],
        "faq": [
            ("What&rsquo;s an appropriate teacher gift that isn&rsquo;t food?", "A small crystal, candle, or gift set is a popular non-food alternative that still feels personal."),
            ("Do you have gifts appropriate for a Secret Santa exchange?", "Yes &mdash; our under-$30 selection is designed for exactly this kind of gift exchange."),
            ("Can these be wrapped individually for a group?", "Yes, ask at checkout for individual wrapping."),
        ],
        "keywords": "gifts under $30 north vancouver, gift shop lonsdale, unique gifts north vancouver",
    },
    {
        "slug": "sympathy-get-well-thinking-of-you-gifts",
        "title": "Sympathy, Get-Well &amp; &ldquo;Thinking of You&rdquo; Gifts",
        "breadcrumb": "Comfort Gifts",
        "meta": "Gentle sympathy, get-well, and thinking-of-you gifts in North Vancouver: calming candles and comforting crystals like rose quartz and amethyst. Utopia on Lonsdale.",
        "intro": [
            "When you&rsquo;re not sure what to say, a gift can say it for you. Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave carries gentle, comfort-focused gifts for sympathy, get-well, and &ldquo;thinking of you&rdquo; moments &mdash; priced from $15 to $60.",
            "This page is for anyone supporting someone through grief, illness, or a hard stretch, and wants a gift that feels calm rather than celebratory. Shop comfort gifts in-store.",
        ],
        "body": [
            ("h2", "Gifts under $25"),
            ("ul", ["Calming intention candles", "Rose quartz or amethyst tumbled stones", "Small comfort-themed oracle decks"]),
            ("h2", "Gifts under $50"),
            ("ul", ["Gentle gemstone bracelets", "Curated comfort gift sets (candle + crystal + card)"]),
            ("h2", "If words feel hard to find"),
            ("p", "A small, quiet gift &mdash; a stone to hold, a candle to light &mdash; often communicates care better than a card alone."),
        ],
        "faq": [
            ("What&rsquo;s an appropriate crystal for a sympathy gift?", "Rose quartz (comfort, gentleness) and amethyst (calm) are commonly chosen for sympathy or get-well gifts."),
            ("Is it appropriate to give a candle for a get-well gift?", "Yes, an unscented or lightly scented candle is a safe, comforting choice, especially for someone sensitive to strong smells."),
            ("Do you have anything specifically for grief support?", "Ask in-store &mdash; several of our stones and gift sets are commonly chosen specifically for grief and comfort."),
        ],
        "keywords": "thinking of you gifts north vancouver, sympathy gifts north vancouver, meaningful gifts vancouver",
    },
    {
        "slug": "wedding-bridal-shower-gifts-north-vancouver",
        "title": "Wedding &amp; Bridal Shower Gifts",
        "breadcrumb": "Wedding &amp; Bridal Gifts",
        "meta": "Wedding and bridal shower gifts with more meaning than a registry item: gemstone jewelry and intention-based gifts from Utopia on Lonsdale, North Vancouver.",
        "intro": [
            "For a wedding or bridal shower gift with more meaning than a registry item, Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave offers jewelry and intention-based gifts the couple or bride will actually keep &mdash; from $30 up to statement jewelry pieces.",
            "This page is for wedding guests, bridal party members, and shower hosts looking for something outside a standard registry. Shop wedding and bridal shower gifts in-store.",
        ],
        "body": [
            ("h2", "Gifts under $50"),
            ("ul", ["Gemstone jewelry (bracelets, pendants)", "Curated &ldquo;new beginnings&rdquo; gift sets", "Rose quartz pieces (love, partnership)"]),
            ("h2", "Gifts $50&ndash;$100+"),
            ("ul", ["Statement jewelry pieces", "Larger crystal gift sets for the new home"]),
            ("h2", "If they&rsquo;ve already registered for everything"),
            ("p", "A piece of jewelry or a Clarity Session for the couple stands apart from a registry list."),
        ],
        "faq": [
            ("What crystal is associated with love or partnership?", "Rose quartz is the most common choice for love and partnership-themed gifts."),
            ("Is jewelry an appropriate bridal shower gift?", "Yes &mdash; a smaller jewelry piece is a popular, personal alternative to registry items at a bridal shower."),
            ("Can you gift-wrap wedding gifts?", "Yes, wrapping is available at checkout."),
        ],
        "keywords": "wedding gifts north vancouver, bridal shower gifts north vancouver, jewelry gifts north vancouver",
    },
    {
        "slug": "gifts-for-her-north-vancouver",
        "title": "Gifts for Her &mdash; North Vancouver",
        "breadcrumb": "Gifts for Her",
        "meta": "Personal gifts for her in North Vancouver: jewelry, crystals, and intention gifts from $20 to $150+, beyond the usual candle-and-mug combo. Utopia on Lonsdale.",
        "intro": [
            "If you&rsquo;re shopping for a woman in your life and want it to feel personal, Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave is built around exactly this: jewelry, crystals, and intention gifts, from $20 to $150+.",
            "This page covers partners, friends, sisters, and daughters &mdash; any &ldquo;gifts for her&rdquo; search that wants something beyond the usual candle-and-mug combo. Shop gifts for her in-store.",
        ],
        "body": [
            ("h2", "Gifts under $25"),
            ("ul", ["Tumbled crystals", "Intention candles", "Mini oracle decks"]),
            ("h2", "Gifts under $50"),
            ("ul", ["Gemstone bracelets and pendants", "Curated gift sets"]),
            ("h2", "If she already has everything"),
            ("p", "A statement jewelry piece or a Clarity Session booking goes beyond what she&rsquo;d buy herself."),
        ],
        "faq": [
            ("What&rsquo;s a popular &ldquo;gifts for her&rdquo; pick at Utopia?", "Jewelry and crystal bracelets are consistently popular, along with curated gift sets pairing a candle and a crystal."),
            ("Do you carry gifts for different budgets in one visit?", "Yes &mdash; our range spans from under-$25 items to statement jewelry pieces in the same visit."),
            ("Can I add a reading to a gift for her?", "Yes, a Clarity Session can be booked alongside or instead of a physical gift."),
        ],
        "keywords": "gifts for her north vancouver, jewelry gifts north vancouver, meaningful gifts vancouver",
    },
    {
        "slug": "gifts-for-mom-north-vancouver",
        "title": "Gifts for Mom",
        "breadcrumb": "Gifts for Mom",
        "meta": "Year-round gifts for mom in North Vancouver: jewelry and crystal gifts for birthdays, holidays, or just because, from $20 to $120. Utopia on Lonsdale.",
        "intro": [
            "Beyond the Mother&rsquo;s Day rush, &ldquo;gifts for mom&rdquo; is a year-round search &mdash; birthdays, holidays, or just because. Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave carries jewelry and crystal gifts for moms in any season, from $20 to $120.",
            "This page is for any occasion involving a mom, grandmother, or mother figure. Shop gifts for mom in-store.",
        ],
        "body": [
            ("h2", "Gifts under $25"),
            ("ul", ["Rose quartz pieces", "Intention candles", "Small oracle decks"]),
            ("h2", "Gifts under $50"),
            ("ul", ["Gemstone jewelry", "Curated &ldquo;for Mom&rdquo; gift sets"]),
            ("h2", "If mom already has everything"),
            ("p", "Consider a shared experience &mdash; a Clarity Session for two &mdash; instead of another object."),
        ],
        "faq": [
            ("What&rsquo;s a timeless gift idea for moms, not tied to a holiday?", "Jewelry and rose quartz pieces work for nearly any occasion, not just Mother&rsquo;s Day."),
            ("Do you have gift sets specifically curated &ldquo;for Mom&rdquo;?", "Yes, ask in-store for our current curated sets."),
            ("Can gifts for mom be wrapped?", "Yes, wrapping is available at checkout."),
        ],
        "keywords": "gifts for mom, mother's day gifts north vancouver, meaningful gifts vancouver",
    },
    {
        "slug": "meaningful-gifts-for-teens",
        "title": "Meaningful Gifts for Teens",
        "breadcrumb": "Gifts for Teens",
        "meta": "Meaningful gifts for teens in North Vancouver: crystal jewelry, oracle decks, and starter tarot that read as thoughtful, not childish. From $10 to $50 at Utopia on Lonsdale.",
        "intro": [
            "Teens can be the hardest to shop for &mdash; too old for toys, not quite into &ldquo;adult&rdquo; gifts yet. Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave carries crystal jewelry, oracle decks, and small ritual items that read as thoughtful, not childish &mdash; from $10 to $50.",
            "This page is for parents, aunts/uncles, and friends shopping for a teenager who&rsquo;s curious about crystals, tarot, or self-expression. Shop meaningful teen gifts in-store.",
        ],
        "body": [
            ("h2", "Gifts under $25"),
            ("ul", ["Beginner-friendly oracle decks", "Small tumbled crystals", "Crystal keychains or jewelry"]),
            ("h2", "Gifts under $50"),
            ("ul", ["Beaded bracelets", "Starter tarot decks", "Curated &ldquo;self-care&rdquo; gift sets"]),
            ("h2", "If they&rsquo;re hard to shop for"),
            ("p", "A starter tarot or oracle deck often becomes a genuine hobby rather than a one-time gift."),
        ],
        "faq": [
            ("Is a tarot deck an appropriate gift for a teen?", "Yes &mdash; many teens enjoy tarot and oracle decks as a creative, reflective hobby; beginner-friendly decks are a good starting point."),
            ("What crystal is popular with teens right now?", "Amethyst and rose quartz are consistently popular starting crystals for teens."),
            ("Do you have anything under $15 for a teen gift exchange?", "Yes, ask in-store for our smallest crystal and keychain options."),
        ],
        "keywords": "meaningful gifts for teens, unique gifts north vancouver, gift shop lonsdale",
    },
    {
        "slug": "gifts-for-someone-who-has-everything",
        "title": "Gifts for Someone Who Has Everything",
        "breadcrumb": "Hard-to-Shop-For Gifts",
        "meta": "For the person who has everything, give an experience: Clarity Sessions, readings, and energy work as gifts, plus statement jewelry. Utopia on Lonsdale, North Vancouver.",
        "intro": [
            "When someone truly doesn&rsquo;t need another object, the answer is an experience. Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave offers Clarity Sessions, readings, and energy work as gifts &mdash; alongside statement jewelry for the rare item they&rsquo;d actually want.",
            "This page is for the hardest person on your list: the one who buys what they need before you can. Book a Clarity Session gift or shop statement jewelry in-store.",
        ],
        "body": [
            ("h2", "Experience gifts"),
            ("ul", ["Tarot or oracle reading session", "Palmistry session", "Energy work / clearing session", "Clarity Session gift certificate"]),
            ("h2", "Object gifts (if you&rsquo;d rather give something physical)"),
            ("ul", ["Statement jewelry pieces", "Rare or larger crystal specimens", "Curated, high-end gift sets"]),
        ],
        "faq": [
            ("How do I gift a reading or session?", "Ask in-store for a gift certificate for a Clarity Session, tarot reading, or energy work session &mdash; it can be booked for any date the recipient chooses."),
            ("What if they&rsquo;re skeptical about readings?", "Frame it as reflection and relaxation time rather than fortune-telling &mdash; many first-time visitors come in skeptical and leave having simply enjoyed the conversation."),
            ("Is there an expiry on gift certificates?", "Ask in-store for current gift certificate terms."),
        ],
        "keywords": "gifts for someone who has everything, meaningful gifts vancouver, unique gifts north vancouver",
    },
    {
        "slug": "crystal-gifts-and-what-they-mean",
        "title": "Crystal Gifts and What They Mean",
        "breadcrumb": "Crystal Gifts Guide",
        "meta": "A gift-giving guide to crystal meanings: rose quartz, amethyst, citrine, black tourmaline, and clear quartz. Match a stone to the moment at Utopia on Lonsdale, North Vancouver.",
        "intro": [
            "Not sure which crystal to gift? Here&rsquo;s the short version: Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave can help you match a stone to the moment &mdash; love, comfort, confidence, or a fresh start &mdash; and wrap it before you leave.",
            "This page is a gift-giving guide to crystal meanings, not a witchcraft primer &mdash; useful whether or not the recipient is &ldquo;into&rdquo; crystals. Shop crystal gifts in-store.",
        ],
        "body": [
            ("h2", "Popular crystal gifts and their meanings"),
            ("ul", [
                "<strong>Rose quartz</strong> &mdash; love, comfort, warmth (great for partners, moms, sympathy gifts)",
                "<strong>Amethyst</strong> &mdash; calm, clarity (great for stressed friends, students, teens)",
                "<strong>Citrine</strong> &mdash; confidence, positivity (great for career milestones, new jobs)",
                "<strong>Black tourmaline</strong> &mdash; protection, grounding (great for someone going through change)",
                "<strong>Clear quartz</strong> &mdash; an all-purpose, &ldquo;amplifying&rdquo; stone (safe when you&rsquo;re unsure)",
            ]),
            ("h2", "Gifts under $25"),
            ("p", "Tumbled stones, small clusters, crystal keychains."),
            ("h2", "Gifts under $50"),
            ("p", "Crystal jewelry, larger specimens, curated crystal gift sets."),
        ],
        "faq": [
            ("What crystal should I gift if I don&rsquo;t know their preferences?", "Clear quartz is considered a safe, all-purpose choice since it isn&rsquo;t tied to one specific meaning."),
            ("Are crystal gifts appropriate for someone who isn&rsquo;t spiritual?", "Yes &mdash; many people give and receive crystals simply as beautiful, meaningful objects, independent of spiritual belief."),
            ("Can I combine a crystal with jewelry as one gift?", "Yes, crystal jewelry pieces combine both in a single gift."),
        ],
        "keywords": "crystal gifts, meaningful gifts vancouver, jewelry gifts north vancouver",
    },
    {
        "slug": "jewelry-gifts-lonsdale",
        "title": "Jewelry Gifts on Lonsdale",
        "breadcrumb": "Jewelry Gifts",
        "meta": "Gemstone and crystal jewelry gifts on Lonsdale: pendants, bracelets, and statement pieces from $30 to $150+, with intention and story behind each. Utopia North Vancouver.",
        "intro": [
            "For jewelry gifts on Lonsdale, Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave carries gemstone and crystal jewelry &mdash; pendants, bracelets, and statement pieces &mdash; priced from $30 to $150+, with wrapping available same-day.",
            "This page is for anyone who wants a wearable gift with more story than a mall jewelry counter offers. Shop jewelry gifts in-store.",
        ],
        "body": [
            ("h2", "Gifts under $50"),
            ("ul", ["Gemstone bracelets", "Small pendant necklaces", "Beaded stone jewelry"]),
            ("h2", "Gifts $50&ndash;$100+"),
            ("ul", ["Statement necklaces", "Larger gemstone pieces", "Curated jewelry + crystal gift sets"]),
            ("h2", "If they already have plenty of jewelry"),
            ("p", "Look for a less common stone or a piece tied to a specific intention (protection, calm, confidence) rather than a generic style."),
        ],
        "faq": [
            ("Do you carry jewelry tied to specific meanings or intentions?", "Yes &mdash; much of our jewelry uses gemstones chosen for specific meanings like love, protection, or clarity."),
            ("Is jewelry from Utopia different from mall jewelry stores?", "Our focus is on gemstone and crystal jewelry with intention and story behind each piece, rather than mass-produced fashion jewelry."),
            ("Can jewelry gifts be wrapped for a special occasion?", "Yes, gift wrapping is available at checkout for any jewelry purchase."),
        ],
        "keywords": "jewelry gifts north vancouver, gift shop lonsdale, unique gifts north vancouver",
    },
    {
        "slug": "gift-clarity-session-packages",
        "title": "Gift + Clarity Session Packages",
        "breadcrumb": "Gift + Session Packages",
        "meta": "Bundled Gift + Clarity Session packages at Utopia on Lonsdale: a crystal or jewelry piece paired with a short tarot, palmistry, or energy reading. North Vancouver.",
        "intro": [
            "The most memorable gift isn&rsquo;t always a thing &mdash; sometimes it&rsquo;s an object paired with an experience. Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave offers bundled Gift + Clarity Session packages: a piece of jewelry or a crystal, paired with a short tarot, palmistry, or energy reading.",
            "This page is for gift-givers who want to combine something tangible with something reflective &mdash; popular for birthdays, milestones, and &ldquo;thinking of you&rdquo; moments. Shop a Gift + Clarity Session package or book just the session as a standalone gift certificate.",
        ],
        "body": [
            ("h2", "Package examples"),
            ("ul", ["Crystal + mini tarot reading", "Jewelry piece + Clarity Session", "Candle + energy clearing session", "Oracle deck + guided reading session"]),
            ("h2", "If you&rsquo;re not sure which to choose"),
            ("p", "Ask in-store &mdash; packages can be customized around the recipient&rsquo;s interests and your budget."),
        ],
        "faq": [
            ("What is a Clarity Session?", "A Clarity Session is a short, guided reading or energy session offered in-store, designed to give the recipient a moment of reflection and insight."),
            ("Can I gift just the session without a product?", "Yes, a standalone Clarity Session gift certificate is available."),
            ("How do I book a package for someone else?", "Ask in-store or through utopiastore.ca &mdash; sessions can typically be booked for a date the recipient chooses, so it isn&rsquo;t tied to your schedule."),
        ],
        "keywords": "crystal gifts, gift shop lonsdale, meaningful gifts vancouver, unique gifts north vancouver",
    },
    {
        "slug": "get-well-gifts-recovery-north-vancouver",
        "title": "Coming Home, Coming Back to Yourself: A Guide to Get-Well Gifts from Utopia Wellness &amp; Gifts",
        "breadcrumb": "Get-Well Gifts",
        "meta": "Thoughtful get-well gifts for someone recovering at home in North Vancouver: calming crystals, gentle candles, gemstone jewelry, and comfort sets from Utopia on Lonsdale.",
        "intro": [
            "Coming home after a hospital stay, a surgery, or a hard stretch of illness is its own kind of milestone. The hardest part is technically over, but the body and the mind still need time to catch up. This is where a thoughtful gift can do more than most people realize. It is not about fixing anything. It is about letting someone know they are supported while they take the slow, quiet steps back to themselves.",
            "At Utopia Wellness &amp; Gifts on Lonsdale Ave, we see this kind of gift often, and we have learned what actually helps. The best get-well gifts are not the biggest or the flashiest &mdash; they are the ones that bring a little calm into a hard day.",
        ],
        "body": [
            ("h2", "What Are the Best Get-Well Gifts for Someone Recovering at Home?"),
            ("h3", "Crystals for comfort and calm"),
            ("p", "A stone you can hold is a strange kind of comfort, but it works. Rose quartz is our most requested pick for gentleness and emotional support, while amethyst is the one people reach for when they want calm on a restless day. A tumbled stone tucked next to a bedside lamp becomes something to hold onto, literally, when a day feels heavy."),
            ("h3", "Candles and calming scents"),
            ("p", "Recovery often means a lot of time in one room, so the smell of that room matters more than people expect. A softly scented intention candle can turn a bedroom or a couch corner into a place that feels cared for rather than clinical. We keep our get-well candles gentle on purpose, since strong scents are not always welcome during recovery."),
            ("h3", "A gentle energy reset for the home"),
            ("p", "Illness and hospital stays can leave a space feeling stale, and coming home to that same stagnant energy is not always comforting. A small sage or palo santo bundle, used lightly and with the windows cracked, is a simple way to freshen a room and mark the return home as a fresh start."),
            ("h3", "Jewelry that carries a quiet message"),
            ("p", "A small piece of gemstone jewelry, a rose quartz pendant or a calming bracelet, is something someone can wear every day as a small, physical reminder that they are thought of. Unlike flowers or food, it does not fade or run out. It just stays with them."),
            ("h3", "A curated comfort gift set"),
            ("p", "If you cannot decide on just one thing, our curated comfort sets pair a candle, a crystal, and a small card together, so the gift feels complete without you having to guess. These are some of our most popular get-well and sympathy picks for exactly that reason."),
            ("h3", "A Clarity Session, when words are hard to find"),
            ("p", "Sometimes the most caring gift is not an object at all. A Clarity Session, a short, gentle tarot or energy session booked for whenever they are ready, gives someone a quiet hour of reflection during a time that can otherwise feel like it is happening to them rather than with them."),
            ("p", "Recovery is not a single moment, it is a slow return, and being present for it matters more than getting the gift exactly right. Whether you choose a stone, a candle, a small piece of jewelry, or a session booked for later, what you are really giving is the message that someone is not going through this alone. Stop by 1826 Lonsdale Ave and we will help you find the right one."),
        ],
        "faq": [
            ("What is a good get-well gift that is not flowers or food?", "A calming crystal like rose quartz or amethyst, a gentle scented candle, or a small piece of gemstone jewelry are all popular alternatives that last longer than a bouquet and do not require any care."),
            ("Are crystal gifts appropriate for someone who does not consider themselves spiritual?", "Yes. Many people give and receive crystals simply as calming, meaningful objects, no belief required. The stone still works as a physical thing to hold onto on a hard day."),
            ("Can you help me build a gift if I am not sure what to pick?", "Yes, our curated comfort sets pair a candle, a crystal, and a small card together, and we can also build a custom set in store if you want something more personal."),
            ("Is a Clarity Session an appropriate gift for someone recovering?", "Yes, many people gift a session as something to look forward to once they feel ready, rather than something to do right away. It can be booked for any date the recipient chooses."),
            ("Do you wrap get-well gifts?", "Yes, gift wrapping is available at checkout on any purchase, so you can shop and go straight to visiting or sending it off."),
        ],
        "keywords": "get well gifts north vancouver, recovery gifts, comfort gifts north vancouver, sympathy gifts vancouver, crystal gifts, gift shop lonsdale",
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


if __name__ == "__main__":
    main()
