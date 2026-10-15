"""
40 gift-category blog posts from draft.md (second batch).
Generate from blog/TEMPLATE.html. Run: python shopify/gen_draft2.py
AEO-focused: question-style H2s, concise direct answers, FAQPage schema,
"People also search for" line. All category GIFTS.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(__file__))
TEMPLATE = os.path.join(ROOT, "blog", "TEMPLATE.html")
BLOG_DIR = os.path.join(ROOT, "blog")

P_CLS = 'text-[clamp(0.9rem,1.8vw,1.05rem)] font-light leading-[1.9] mb-6'
H2_CLS = 'text-[clamp(1.2rem,3vw,1.7rem)] leading-[1.3] mt-12 mb-5'
H3_CLS = 'text-[1.1rem] leading-[1.3] mt-8 mb-3'
UL_CLS = 'list-disc pl-6 mb-6 space-y-2 text-[clamp(0.9rem,1.8vw,1.05rem)] font-light leading-[1.9]'
DATE = "September 16, 2026"
ISO = "2026-09-16"


def P(t): return f'<p class="{P_CLS}" style="color:var(--text-body)">{t}</p>'
def H2(t): return f'<h2 class="{H2_CLS}" style="font-family:var(--font-display);color:var(--text-heading)">{t}</h2>'
def H3(t): return f'<h3 class="{H3_CLS}" style="font-family:var(--font-display);color:var(--text-heading)">{t}</h3>'
def UL(items):
    lis = "\n".join(f"        <li>{it}</li>" for it in items)
    return f'<ul class="{UL_CLS}" style="color:var(--text-body)">\n{lis}\n      </ul>'

CAT = "GIFTS"

# Each post: slug, title, breadcrumb, meta, intro[list], list_heading, list_items[list],
# closing (optional paragraph), faq[(q,a)], keywords
POSTS = [
    dict(
        slug="tarot-deck-gifts-north-vancouver-birthdays",
        title="Best Tarot Deck Gifts in North Vancouver for Meaningful Birthdays",
        breadcrumb="Tarot Deck Birthday Gifts",
        meta="A tarot deck is a personal, lasting birthday gift. Who it suits and how to choose one, with decks you can flip through in store at Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "Looking for a birthday gift that actually means something? A tarot deck is one of the most personal gifts you can give. Stop by Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave, North Vancouver, and you'll find a wall of decks ranging from classic Rider-Waite-style illustrations to modern, artist-led reinterpretations, all displayed so you can flip through the cards before you decide.",
            "A tarot deck works as a birthday gift because it isn't disposable. It's something the person opens, uses, and comes back to for years &mdash; whether for quiet reflection, journaling prompts, or simply enjoying the artwork.",
        ],
        list_heading="Who a Tarot Deck Gift Suits",
        list_items=[
            "Friends newly curious about tarot or self-reflection practices.",
            "Someone starting a new job, relationship, or chapter of life.",
            "Readers and collectors who appreciate beautiful card art.",
            "Anyone who prefers a thoughtful object over a gift card.",
        ],
        closing="Visit Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave, North Vancouver to flip through decks in person (free parking at the back), or shop the full tarot collection at utopiastore.ca.",
        faq=[
            ("Do I need to know how to read tarot to give it as a gift?", "No. Most decks come with a guidebook, and our staff can point you toward a deck with clear, approachable meanings for a beginner."),
            ("What is the most popular tarot deck for a first-time gift?", "Classic Rider-Waite-style decks remain the most popular starting point because the imagery is widely documented and easy to learn from, but we also carry decks with gentler, more modern artwork."),
            ("Is tarot just for believers?", "Not at all. Many people use tarot purely as a reflection and journaling tool, no belief system required."),
        ],
        keywords="tarot gift North Vancouver, best tarot deck for beginners, meaningful birthday gift North Van, tarot cards for self-reflection",
    ),
    dict(
        slug="crystal-jewelry-gift-ideas-north-vancouver",
        title="Crystal Jewelry Gift Ideas That Feel Personal in North Vancouver",
        breadcrumb="Crystal Jewelry Gifts",
        meta="Crystal jewelry makes a personal gift matched to a birthstone or intention. How to choose and what to look for, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "Jewelry is one of the easiest gifts to get wrong &mdash; generic, forgettable, or clearly picked in five minutes at the mall. Crystal jewelry solves that problem. At Utopia Wellness &amp; Gifts on Lonsdale Ave, our jewelry cases hold pieces built around birthstones and specific crystal properties, so the gift carries a reason behind it rather than just being a necklace.",
            "Think amethyst for calm, rose quartz for self-love and relationships, citrine for confidence, or a birthstone piece matched to the month they were born. These are things people actually wear daily.",
        ],
        list_heading="What Makes It Feel Personal",
        list_items=[
            "Matched to a birth month or zodiac sign.",
            "Chosen for a specific intention: calm, confidence, protection, love.",
            "Available in everyday pieces: studs, pendants, simple bracelets.",
            "Pairs well with a card explaining the stone's meaning.",
        ],
        closing="See our jewelry cases in person at 1826 Lonsdale Ave or browse the full collection at utopiastore.ca.",
        faq=[
            ("How do I pick the right stone for someone?", "Start with their birth month or what they could use more of right now &mdash; calm, courage, clarity &mdash; and we can help match a stone to that."),
            ("Is crystal jewelry durable enough for daily wear?", "Yes, our everyday pieces are set for regular wear; just avoid harsh chemicals and hard knocks like any fine jewelry."),
            ("Do you explain what each stone means?", "Yes, every piece comes with a plain-language explanation you can pass along, or we'll write it out for you on the spot."),
        ],
        keywords="crystal jewelry gift North Vancouver, birthstone jewelry North Van, meaningful jewelry gift, healing crystal bracelet gift",
    ),
    dict(
        slug="candle-gifts-calm-home-north-vancouver",
        title="Thoughtful Candle Gifts for Creating Calm at Home",
        breadcrumb="Candle Gifts for Calm",
        meta="Candle gifts that work for almost anyone, built around ritual and intention. Best calming scents and pairings, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "Candles are the gift that works for almost everyone &mdash; housewarmings, self-care packages, or a simple just-because. At Utopia Wellness &amp; Gifts, our candles lean into ritual and intention rather than scent alone: cleansing blends, calming blends, and candles meant to be lit as a small daily pause.",
            "A candle gift says take a breath without you having to say it out loud. It works for the friend who's stressed, the coworker moving into a new place, or anyone who already has enough stuff.",
        ],
        list_heading="Good Occasions for a Candle Gift",
        list_items=[
            "Housewarmings, paired with a small sage or incense set.",
            "Self-care or thinking-of-you gifts.",
            "Stress relief for someone going through a hard season.",
            "Pairing with a crystal for a small ritual gift set.",
        ],
        closing="Find beautiful candles and ritual tools at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop online at utopiastore.ca.",
        faq=[
            ("What scent is best for a calming gift?", "Lavender and sage-based blends are the most popular for stress relief and better sleep; citrus blends work well for energy and focus."),
            ("Can I pair a candle with something else for a gift set?", "Yes, candles pair naturally with a small crystal, a smudge stick, or incense for a simple ritual gift bundle, and we're happy to help you build one."),
            ("Are your candles good for people with scent sensitivities?", "We carry both strongly scented and lightly scented options, so let us know and we'll point you to the right one."),
        ],
        keywords="best candle gift North Vancouver, calming home gifts North Van, ritual candle gift ideas, self-care gift North Vancouver",
    ),
    dict(
        slug="oracle-card-gifts-starting-spiritual-journey",
        title="Best Oracle Card Gifts for Someone Starting Their Spiritual Journey",
        breadcrumb="Oracle Card Gifts",
        meta="Oracle cards are a beginner-friendly first gift for someone curious about tarot. How they differ and which to choose, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "Oracle cards and tarot often get lumped together, but they're different, and that difference matters when choosing a gift. Oracle decks don't follow a fixed structure of suits and numbers the way tarot does; each deck has its own theme &mdash; affirmations, animals, angels, moon phases &mdash; and tends to be more intuitive and beginner-friendly out of the box.",
            "That makes oracle cards a strong first gift for someone curious about tarot but not ready to learn a full system. At Utopia on Lonsdale Ave, we carry a range so you can match the theme to the person.",
        ],
        list_heading="Who Oracle Cards Suit",
        list_items=[
            "Beginners who find tarot intimidating.",
            "Friends exploring intuition or self-reflection for the first time.",
            "Daily affirmation or journaling habits.",
            "Gifting alongside a simple intention candle.",
        ],
        closing="See our full oracle and tarot collection in store at 1826 Lonsdale Ave, or shop online at utopiastore.ca.",
        faq=[
            ("What is the real difference between oracle and tarot?", "Tarot follows a fixed 78-card structure with established meanings; oracle decks vary deck to deck and are generally more open to interpretation, which makes them easier to start with."),
            ("Which oracle deck is best for a total beginner?", "Affirmation-based decks are usually the easiest entry point since each card has a clear, direct message."),
            ("Can oracle cards be used alongside tarot?", "Yes, many people use oracle cards for daily reflection and tarot for deeper questions; they work well together."),
        ],
        keywords="oracle card gift North Vancouver, spiritual gifts North Van, oracle deck for beginners, best first tarot or oracle deck",
    ),
    dict(
        slug="incense-gifts-new-homes-north-vancouver",
        title="Meaningful Incense Gifts for New Homes in North Vancouver",
        breadcrumb="Incense Gifts for New Homes",
        meta="Incense and smudge tools make a practical, meaningful housewarming gift. What to include and how to use it, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "A new home needs more than a houseplant and a bottle of wine. Incense, smudge sticks, and clearing tools make a practical, meaningful housewarming gift &mdash; something the recipient will actually use in those first weeks of settling in.",
            "At Utopia Wellness &amp; Gifts, we carry a range of incense styles (resin, stick, cone) alongside sage and palo santo, plus simple holders so the gift arrives ready to use.",
        ],
        list_heading="Why It Works as a Housewarming Gift",
        list_items=[
            "Practical: something they'll use right away, not display and forget.",
            "Pairs naturally with a small holder or dish.",
            "Works for any home: apartment, first house, or new rental.",
            "Easy to combine with a candle for a complete new-home set.",
        ],
        closing="Shop incense and ritual items at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or order online at utopiastore.ca.",
        faq=[
            ("What is the difference between incense and smudge sticks?", "Incense is typically burned for scent and ambiance, while smudge sticks like sage and palo santo are traditionally used for clearing a space of stagnant energy; both make thoughtful housewarming gifts."),
            ("Do I need a special holder?", "A basic heatproof dish or holder works for incense; smudge sticks are often burned over an abalone shell or dish, which we also carry."),
            ("Is this gift appropriate for someone who isn't especially spiritual?", "Yes, plenty of people enjoy incense simply for the scent and ritual of lighting it, no particular belief required."),
        ],
        keywords="incense gift North Vancouver, housewarming gifts North Van, smudge stick gift ideas, new home gift North Vancouver",
    ),
    dict(
        slug="crystal-gifts-clarity-calm-north-vancouver",
        title="Crystal Gifts for Clarity and Calm",
        breadcrumb="Crystal Gifts for Clarity & Calm",
        meta="Crystal gifts chosen by intention for someone stressed or scattered. The most reliable picks for clarity and calm, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "When someone on your list is stressed, scattered, or just needs a reset, a crystal chosen for its intention can say more than a generic gift ever could. At Utopia Wellness &amp; Gifts, our crystal section is organised around what people are actually looking for &mdash; clarity, calm, protection, confidence &mdash; so you can shop by what the person needs.",
            "A few reliable picks: amethyst for calm and better sleep, clear quartz for clarity and focus, rose quartz for emotional warmth and self-compassion.",
        ],
        list_heading="Popular Picks by Intention",
        list_items=[
            "<strong>Amethyst</strong> &mdash; calm, better sleep, easing anxiety.",
            "<strong>Clear quartz</strong> &mdash; mental clarity, focus, amplifying intention.",
            "<strong>Rose quartz</strong> &mdash; self-love, emotional healing, relationships.",
            "<strong>Black tourmaline</strong> &mdash; grounding and protection from stress.",
        ],
        closing="Visit our crystal section at 1826 Lonsdale Ave, or order online at utopiastore.ca.",
        faq=[
            ("How do I know which crystal to buy for someone?", "Think about what they need most right now &mdash; rest, focus, confidence, comfort &mdash; and we can match a stone to that in a couple of minutes."),
            ("Do crystals need to be cleansed before gifting?", "Many people like to cleanse a crystal with smoke, sound, or moonlight before giving it, though it's not required; we can walk you through it if you'd like."),
            ("What is a good budget-friendly crystal gift?", "Small tumbled stones and palm stones are an easy, affordable entry point and still carry the full meaning of the larger pieces."),
        ],
        keywords="crystal gifts North Vancouver, healing crystal gift ideas, crystals for stress and anxiety, best crystal gift for a friend",
    ),
    dict(
        slug="books-as-gifts-self-growth-north-vancouver",
        title="Best Books as Gifts for Self-Growth in North Vancouver",
        breadcrumb="Books for Self-Growth",
        meta="Books on spiritual growth, tarot, astrology, and mindfulness make lasting gifts. What to pair them with, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "A good book sticks around longer than almost any other gift. At Utopia Wellness &amp; Gifts, our book section leans into spiritual growth, self-reflection, astrology, tarot reference guides, and mindfulness &mdash; the kind of titles people actually finish and recommend.",
            "Books make an especially strong gift paired with a related item: a tarot guidebook alongside a new deck, a journaling book alongside a candle, or an astrology reference for the friend who wants to go deeper.",
        ],
        list_heading="Good Gifting Occasions",
        list_items=[
            "Graduations or new chapters, with a book on self-discovery.",
            "Someone newly interested in tarot, astrology, or crystals who wants a reference guide.",
            "Pairing with a journal or tarot deck for a complete gift set.",
            "Anyone who prefers a slower, screen-free gift.",
        ],
        closing="Browse our book section at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop online at utopiastore.ca.",
        faq=[
            ("What if I don't know their reading level or interest?", "Our staff can recommend something based on whether they're a total beginner or already fairly knowledgeable, just let us know what they're into."),
            ("Do you carry reference guides for tarot or astrology?", "Yes, we stock both beginner-friendly and more in-depth reference titles for tarot, crystals, and astrology."),
            ("Can a book be part of a larger gift bundle?", "Definitely, books pair naturally with a journal, a deck, or a candle for a more complete self-growth gift set."),
        ],
        keywords="best spiritual books gift North Vancouver, self-growth books North Van, tarot guidebook gift, mindfulness book gift ideas",
    ),
    dict(
        slug="unique-anniversary-gift-ideas-north-vancouver",
        title="Unique Gift Ideas for Anniversaries in North Vancouver",
        breadcrumb="Anniversary Gift Ideas",
        meta="Anniversary gifts that last longer than flowers: crystal jewelry, a couple's tarot ritual, or a candle set, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "Flowers wilt. Chocolate disappears in a day. If you're looking for an anniversary gift that lasts longer than the weekend, crystal jewelry, a tarot deck for a couple's ritual, or an intention candle makes a far more personal alternative &mdash; and Utopia Wellness &amp; Gifts on Lonsdale Ave carries all three under one roof.",
            "Consider a rose quartz piece for love and connection, a shared tarot or oracle practice as a couple's ritual, or a candle set paired with a small crystal for an anniversary at home.",
        ],
        list_heading="Anniversary Gift Directions",
        list_items=[
            "<strong>Rose quartz jewelry</strong> &mdash; love, connection, emotional warmth.",
            "<strong>A shared tarot or oracle deck</strong> &mdash; a ritual the two of you can return to.",
            "<strong>Candle and crystal set</strong> &mdash; a calm, intentional evening at home.",
            "A meaningful book on relationships or growth.",
        ],
        closing="Find thoughtful anniversary pieces at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop at utopiastore.ca.",
        faq=[
            ("What is a good anniversary gift under $100?", "A crystal jewelry piece paired with a candle is a strong combination that stays well within that budget and still feels considered."),
            ("Is a tarot deck a strange anniversary gift?", "Not at all, many couples use it as a shared, low-pressure ritual, something to do together rather than just another object."),
            ("Can you help me build a gift bundle on the spot?", "Yes, bring us the occasion and the budget and we'll put a set together in store."),
        ],
        keywords="unique anniversary gift North Vancouver, meaningful anniversary gifts North Van, couples ritual gift, rose quartz gift for anniversary",
    ),
    dict(
        slug="tarot-deck-gifts-new-beginnings-north-vancouver",
        title="Tarot Decks as Gifts for New Beginnings",
        breadcrumb="Tarot Gifts for New Beginnings",
        meta="A tarot deck is a thoughtful gift for a new job, move, or fresh start. How to match the deck to the moment, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "A new job, a move, a breakup, a graduation &mdash; moments like these are exactly when a tarot deck makes sense as a gift. It gives the person a tool for reflecting on the chapter ahead rather than just marking the occasion. At Utopia Wellness &amp; Gifts on Lonsdale Ave, we can help you pick a deck that fits the specific kind of beginning they're facing.",
            "For someone starting a new career, a deck with strong, grounded imagery works well. For someone recovering from a hard season, gentler, more emotionally supportive artwork tends to land better.",
        ],
        list_heading="Good New-Beginnings Matches",
        list_items=[
            "New job or career change.",
            "Moving to a new city or home.",
            "Post-breakup or fresh start.",
            "Graduation or finishing a major milestone.",
        ],
        closing="Discover the right deck at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop online at utopiastore.ca.",
        faq=[
            ("Does the deck's artwork style actually matter for a gift like this?", "Yes, a gentler, more affirming deck suits someone going through a hard transition, while a bold, classic deck suits someone starting something exciting and new."),
            ("Should I include a note explaining why I chose this deck?", "It's a nice touch; a short note about the chapter they're entering makes the gift land as intentional rather than random."),
            ("What if they've never used tarot before?", "Pair it with a simple guidebook or one of our beginner-friendly decks so they have an easy way in."),
        ],
        keywords="tarot gift for new beginning North Vancouver, tarot deck gift for graduation, new job gift ideas North Van, meaningful gift for a fresh start",
    ),
    dict(
        slug="best-small-gifts-under-50-north-vancouver",
        title="Best Small Gifts Under $50 at Utopia Wellness & Gifts",
        breadcrumb="Small Gifts Under $50",
        meta="Affordable, meaningful gifts under $50: tumbled crystals, incense, small jewelry, and candles, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "Not every gift needs a big budget to feel considered. At Utopia Wellness &amp; Gifts on Lonsdale Ave, a good chunk of our store &mdash; tumbled crystals, incense, small jewelry pieces, and candles &mdash; sits comfortably under $50 without feeling like an afterthought.",
            "This is the category we point people to for coworker gifts, teacher appreciation, last-minute invites, or stocking stuffers that still feel personal. The trick is picking something tied to an intention rather than grabbing the first thing near the register.",
        ],
        list_heading="Good Picks Under $50",
        list_items=[
            "Tumbled crystals and palm stones.",
            "Small crystal jewelry: studs, simple pendants.",
            "Incense sets with a holder.",
            "Intention candles.",
            "Oracle decks.",
        ],
        closing="Shop in store at 1826 Lonsdale Ave or online at utopiastore.ca &mdash; many options under $50.",
        faq=[
            ("What is the best under-$50 gift for someone you don't know well?", "A tumbled crystal paired with a small card explaining its meaning works for almost anyone and keeps things low-pressure."),
            ("Can I build a small gift bundle within this budget?", "Yes, a candle plus a tumbled crystal, or a small jewelry piece plus incense, both fit comfortably under $50."),
            ("Do you wrap gifts in store?", "Ask our team when you visit, we're happy to help make it gift-ready."),
        ],
        keywords="best gifts under $50 North Vancouver, affordable meaningful gifts North Van, cheap thoughtful gifts North Vancouver, coworker gift ideas under $50",
    ),
    dict(
        slug="crystal-jewelry-everyday-wear-north-vancouver",
        title="Crystal Jewelry Gift Ideas for Everyday Wear",
        breadcrumb="Everyday Crystal Jewelry",
        meta="Simple crystal jewelry for everyday wear makes a gift that gets used daily. Best stones and pieces, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "Not everyone wants statement jewelry; a lot of people want something simple enough to wear every single day without thinking about it. At Utopia Wellness &amp; Gifts, our everyday crystal jewelry &mdash; simple studs, thin pendants, stacking bracelets &mdash; is designed exactly for that: subtle enough for work, meaningful enough to matter.",
            "These pieces work well as a gift because they don't demand an occasion. A simple amethyst stud or a rose quartz pendant gets used constantly instead of saved for special occasions that never come.",
        ],
        list_heading="Good Everyday Picks",
        list_items=[
            "Simple stud earrings in a single stone.",
            "Thin pendant necklaces.",
            "Stacking bracelets in one or two stones.",
            "Small rings for subtle, daily wear.",
        ],
        closing="See our jewelry collection at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop online at utopiastore.ca.",
        faq=[
            ("What stone is best for everyday wear?", "Clear quartz and rose quartz are popular because they pair with almost any outfit and carry broadly positive meanings of clarity and warmth."),
            ("Will the jewelry hold up to daily wear?", "Yes, our everyday pieces are set for regular use; we'll let you know if a specific piece needs any extra care."),
            ("Can I get a matching set?", "We carry coordinating pieces; ask in store and we can help put together a matching set."),
        ],
        keywords="crystal jewelry North Vancouver, everyday crystal gifts, simple crystal jewelry gift, subtle crystal jewelry North Van",
    ),
    dict(
        slug="gift-for-someone-who-has-everything",
        title="How to Choose a Thoughtful Gift for Someone Who Has Everything",
        breadcrumb="Gift for Someone Who Has Everything",
        meta="How to choose a gift for someone who has everything: intention-based crystals, decks, and ritual tools, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "The person who has everything usually doesn't need more stuff &mdash; they need something that feels different from what they already own. That's where intention-based gifts stand out: a crystal chosen for what they need right now, a tarot deck for reflection, or a candle built around ritual rather than scent.",
            "At Utopia Wellness &amp; Gifts on Lonsdale Ave, this is the exact gap we help people fill &mdash; something tied to a specific intention or moment in their life, which tends to land better than anything purely material.",
        ],
        list_heading="Good Approaches",
        list_items=[
            "Pick based on what they need (calm, focus, confidence) rather than what they already own.",
            "Choose an experience-adjacent gift (tarot, journaling, ritual tools) instead of an object.",
            "Go personal: a birthstone piece or a deck matched to their current life chapter.",
            "Keep it small and meaningful rather than big and generic.",
        ],
        closing="Visit Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver for meaningful options, or shop online at utopiastore.ca.",
        faq=[
            ("What if I genuinely have no idea what they'd like?", "Tell us a bit about them &mdash; their personality, what's going on in their life right now &mdash; and we can usually narrow it down quickly."),
            ("Are intention-based gifts too out there for someone more traditional?", "Not usually. A candle, a journal, or a simple crystal reads as thoughtful rather than unusual, even to people who aren't especially spiritual."),
            ("Can you gift-wrap something on the spot?", "Yes, ask our team when you visit and we'll help make it gift-ready."),
        ],
        keywords="thoughtful gifts North Vancouver, gifts for people who have everything, unique gift ideas North Van, meaningful gift North Vancouver",
    ),
    dict(
        slug="incense-smudge-gifts-sacred-space-home",
        title="Incense and Smudge Gifts for Creating Sacred Space at Home",
        breadcrumb="Incense & Smudge Gifts",
        meta="Incense, sage, and palo santo make a practical gift for a calmer home. A simple sacred-space starter kit, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "Creating a calmer, more intentional home doesn't require a renovation &mdash; sometimes it starts with incense, sage, or palo santo and a few minutes of quiet. At Utopia Wellness &amp; Gifts, we carry a full range of clearing and ritual tools, along with simple holders, so this gift arrives ready to use.",
            "This works well both as a self-care gift and a practical one: for the friend who just moved, the person redoing a room, or anyone who wants their space to feel more settled.",
        ],
        list_heading="A Simple At-Home Sacred Space Starter Kit",
        list_items=[
            "A smudge stick or palo santo.",
            "A heatproof holder or dish.",
            "An incense set for ongoing use.",
            "A small crystal to place in the space afterward.",
        ],
        closing="Find quality incense and tools at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop at utopiastore.ca.",
        faq=[
            ("Is smudging a religious practice?", "It has roots in specific cultural and spiritual traditions; many people today use it simply as a way to mark a reset or create a calmer space, and we're happy to talk through respectful use."),
            ("What is the easiest way to start?", "A simple sage bundle and a dish is the most beginner-friendly starting point."),
            ("Can this be part of a larger gift set?", "Yes, we often pair clearing tools with a candle or small crystal for a complete sacred-space gift."),
        ],
        keywords="smudge gift North Vancouver, incense gift ideas North Van, sacred space gift set, palo santo gift North Vancouver",
    ),
    dict(
        slug="oracle-cards-vs-tarot-which-better-gift",
        title="Oracle Cards vs Tarot: Which Makes a Better Gift?",
        breadcrumb="Oracle vs Tarot Gift",
        meta="Oracle cards vs tarot as a gift: which suits a beginner and which suits deeper study. A clear comparison from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "This is one of the most common questions we get at Utopia Wellness &amp; Gifts: should you give tarot or oracle cards? The honest answer depends on the person. Tarot follows a structured 78-card system with established meanings, which suits someone who likes a learning curve and wants to go deeper over time.",
            "Oracle cards vary by deck and tend to be simpler and more intuitive out of the box &mdash; better suited to someone who wants an easy daily practice without studying a whole system.",
        ],
        list_heading="Quick Comparison",
        list_items=[
            "<strong>Structure:</strong> tarot is a fixed 78 cards; oracle varies by deck.",
            "<strong>Learning curve:</strong> tarot is moderate to steep; oracle is low.",
            "<strong>Best for:</strong> tarot suits deeper, structured reflection; oracle suits daily affirmation and intuition.",
            "<strong>Good first gift:</strong> tarot with a guidebook, yes; oracle, yes, especially for beginners.",
        ],
        closing="Both are available at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave &mdash; come see them in person, or shop online at utopiastore.ca.",
        faq=[
            ("Which should I buy if I'm not sure which they'd prefer?", "If they're a total beginner, start with oracle; if they've expressed interest in learning tarot properly, go with a tarot deck and guidebook."),
            ("Can someone own and use both?", "Absolutely, many people use oracle cards for quick daily reflection and tarot for deeper questions."),
            ("Is one more legitimate than the other?", "No, they're simply different tools; neither is more valid than the other."),
        ],
        keywords="oracle vs tarot gift, best tarot gift North Vancouver, difference between oracle and tarot cards, tarot gift for beginners",
    ),
    dict(
        slug="best-housewarming-gifts-north-vancouver",
        title="Best Housewarming Gifts in North Vancouver That Feel Personal",
        breadcrumb="Housewarming Gifts",
        meta="Housewarming gifts that help a new place feel like home: candles, incense, small crystals, and statues, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "A housewarming gift should help a new place feel like home, not just fill a shelf. At Utopia Wellness &amp; Gifts on Lonsdale Ave, our go-to housewarming picks &mdash; candles, incense, small crystals, and small statues &mdash; lean into that idea directly, chosen for comfort and intention rather than decoration.",
            "These gifts work because they're immediately useful: a candle for the first night, a crystal for the nightstand, incense for clearing the space before it's fully unpacked.",
        ],
        list_heading="Good Housewarming Picks",
        list_items=[
            "A candle in a calming scent.",
            "A small crystal for the entryway or bedroom.",
            "Incense or smudge with a simple holder.",
            "A small statue or decorative piece with meaning.",
        ],
        closing="Shop thoughtful housewarming pieces at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or online at utopiastore.ca.",
        faq=[
            ("What if I don't know their taste in decor?", "Candles, incense, and small crystals are versatile enough to suit almost any home style, which makes them safe, low-risk housewarming picks."),
            ("Is it better to give one item or a small bundle?", "A small bundle, such as a candle plus a crystal, tends to feel more complete without requiring a big budget."),
            ("Do you have gift sets ready to go?", "Ask in store, we can often put a housewarming set together on the spot."),
        ],
        keywords="best housewarming gifts North Vancouver, unique housewarming gifts North Van, new home gift ideas, housewarming candle gift",
    ),
    dict(
        slug="crystal-gifts-stress-relief-better-sleep",
        title="Crystal Gifts for Stress Relief and Better Sleep",
        breadcrumb="Crystals for Stress & Sleep",
        meta="Crystals chosen for calm and better sleep make a gentle gift for someone burned out. The most-requested picks, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "When someone you care about is burned out, wired, or just not sleeping well, a crystal chosen for calm can be a small, genuine way to say I see you. At Utopia Wellness &amp; Gifts, our stress-relief and sleep-focused picks are some of our most frequently requested gifts.",
            "Amethyst is the most reached-for stone for sleep and anxiety relief, often kept on a nightstand. Black tourmaline is a common pick for grounding during high-stress periods. None require any particular belief system to appreciate.",
        ],
        list_heading="Good Picks for Stress and Sleep",
        list_items=[
            "<strong>Amethyst</strong> &mdash; calm, better sleep.",
            "<strong>Black tourmaline</strong> &mdash; grounding, protection from stress.",
            "<strong>Lepidolite</strong> &mdash; gentle calm, easing anxiety.",
            "<strong>Rose quartz</strong> &mdash; emotional comfort.",
        ],
        closing="Explore calming crystals at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop online at utopiastore.ca.",
        faq=[
            ("Where should someone keep a sleep crystal?", "Most people keep it on a nightstand or under the pillow; there's no single correct way, so whatever feels natural works."),
            ("Is this a good gift for someone going through a genuinely hard time?", "Yes, it's a gentle, low-pressure way to show you're thinking of them without requiring anything in return."),
            ("Can I pair this with a candle for a more complete gift?", "Yes, a calming candle alongside a stress-relief crystal is one of our most popular small gift pairings."),
        ],
        keywords="crystal gifts for stress North Vancouver, calming gifts North Van, crystal for better sleep, amethyst gift for anxiety",
    ),
    dict(
        slug="meaningful-birthday-gifts-north-vancouver",
        title="Meaningful Birthday Gifts in North Vancouver (That Aren't Generic)",
        breadcrumb="Meaningful Birthday Gifts",
        meta="Birthday gifts that beat a gift card: tarot decks, crystal jewelry, books, and candles matched to the person, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "Birthdays deserve better than a generic gift card. At Utopia Wellness &amp; Gifts on Lonsdale Ave, we see a steady mix of tarot decks, crystal jewelry, books, and candles go out the door as birthday gifts, each chosen with the person in mind rather than grabbed off a shelf.",
            "The easiest way to make a birthday gift feel considered is to tie it to something specific: their birth month, their current life stage, or simply what would help them most right now.",
        ],
        list_heading="Birthday Gift Directions by Personality",
        list_items=[
            "<strong>The curious friend</strong> &mdash; a tarot or oracle deck.",
            "<strong>The jewelry lover</strong> &mdash; a birthstone crystal piece.",
            "<strong>The reader</strong> &mdash; a spiritual growth or self-help book.",
            "<strong>The homebody</strong> &mdash; a candle and incense set.",
        ],
        closing="Find the perfect birthday gift at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop at utopiastore.ca.",
        faq=[
            ("What is a good birthday gift if I only have a small budget?", "A tumbled crystal or small candle under $25 to $30 still feels thoughtful when paired with a short, specific note about why you picked it."),
            ("Can you help me pick something based on their zodiac sign?", "Yes, bring us their sign and we can suggest crystals and jewelry that are traditionally associated with it."),
            ("Do you offer gift wrapping?", "Ask in store and we'll help make the gift presentation-ready."),
        ],
        keywords="meaningful birthday gifts North Vancouver, unique birthday gifts North Van, birthday gift ideas by zodiac sign, personal birthday gift North Vancouver",
    ),
    dict(
        slug="how-to-gift-a-tarot-deck",
        title="How to Gift a Tarot Deck the Right Way",
        breadcrumb="How to Gift a Tarot Deck",
        meta="How to gift a tarot deck well: match the artwork, include a guidebook, and add a note. Plus the tradition about first decks, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "Giving a tarot deck isn't complicated, but a few small choices make the gift land better. At Utopia Wellness &amp; Gifts, we walk customers through this regularly: match the deck's artwork and tone to the person, include a simple guidebook if they're new to it, and consider adding a short note about why this deck felt right.",
            "There's an old idea that you shouldn't buy your own first tarot deck &mdash; it should be gifted to you. Whether or not someone believes that, it makes tarot a genuinely nice gift to give.",
        ],
        list_heading="A Few Tips for Gifting Tarot Well",
        list_items=[
            "Choose artwork that matches their personality: bold and classic, or soft and modern.",
            "Include a beginner guidebook if they're new to tarot.",
            "Avoid testing the deck extensively yourself before gifting; some prefer it to feel untouched.",
            "Add a short, specific note about why you chose it.",
        ],
        closing="We help you choose the right deck at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop online at utopiastore.ca.",
        faq=[
            ("Is it true you shouldn't buy your own first deck?", "That's a popular tradition, not a hard rule, but it's part of what makes tarot such a meaningful gift to give someone else."),
            ("Should I include a guidebook automatically?", "For a first-time tarot user, yes; it removes the guesswork and makes the deck immediately usable."),
            ("What if they already have a deck?", "A second deck is still a welcome gift; many tarot readers enjoy collecting decks with different art styles."),
        ],
        keywords="how to gift tarot deck, tarot gift North Vancouver, first tarot deck tradition, tarot deck for beginners gift",
    ),
    dict(
        slug="small-ritual-tools-beautiful-gifts",
        title="Small Ritual Tools That Make Beautiful Gifts",
        breadcrumb="Small Ritual Tool Gifts",
        meta="Small ritual tools make beautiful, low-pressure gifts: holders, dishes, statues, and tumbled crystals, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "Not every meaningful gift needs to be expensive or complicated. Small ritual tools &mdash; candle holders, incense dishes, small statues, tumbled crystals &mdash; make beautiful, low-pressure gifts precisely because they're simple. At Utopia Wellness &amp; Gifts on Lonsdale Ave, this is one of our favourite categories to shop.",
            "These items work well as stocking stuffers, add-ons to a bigger gift, or stand-alone presents for someone who appreciates small, intentional objects over big gestures.",
        ],
        list_heading="Good Small Ritual Gifts",
        list_items=[
            "A ceramic or stone incense holder.",
            "A small statue: Buddha, elephant, moon phases.",
            "Tumbled crystals in a small gift pouch.",
            "A mini candle set.",
        ],
        closing="Discover small but meaningful tools at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop at utopiastore.ca.",
        faq=[
            ("Are small ritual tools a good gift for someone new to this space?", "Yes, they're a gentle, low-commitment way to introduce someone to ritual practice without overwhelming them."),
            ("Can these be combined into a gift basket?", "Yes, we regularly help customers build small bundles &mdash; a holder, a crystal, and a mini candle together &mdash; for one complete gift."),
            ("What is a good price point for this kind of gift?", "Most of these items sit comfortably under $30 to $40 individually, making them easy to combine without blowing a budget."),
        ],
        keywords="ritual gift ideas North Vancouver, spiritual gifts North Van, small meaningful gifts, incense holder gift",
    ),
    dict(
        slug="why-local-gift-shopping-north-vancouver",
        title="Why Local Gift Shopping in North Vancouver Feels Better",
        breadcrumb="Why Shop Local",
        meta="Why shopping local for gifts beats ordering online sight unseen: see, touch, and smell before buying, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "There's a real difference between ordering something online sight unseen and picking it up in person at a local shop. At Utopia Wellness &amp; Gifts on Lonsdale Ave, you can actually hold the crystal, flip through the tarot deck, and smell the candle before you buy it &mdash; something no product photo fully replicates.",
            "Shopping local also means supporting an independent, community-rooted business, and it usually comes with something online shopping can't offer: a real conversation.",
        ],
        list_heading="Why Local Gift Shopping Wins",
        list_items=[
            "See, touch, and smell the product before buying.",
            "Get real recommendations based on the person and occasion.",
            "Support an independent North Vancouver business.",
            "Free parking at the back makes a quick visit easy.",
        ],
        closing="Visit Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver (free parking at the back), or shop online at utopiastore.ca.",
        faq=[
            ("Is it more expensive to shop local?", "Not necessarily; many of our pieces are comparable in price to big online retailers, with the added benefit of seeing the item first."),
            ("Can I still get help if I'm short on time?", "Yes, tell our team the occasion and budget when you arrive and we can help you move quickly."),
            ("Do you offer online shopping too, for convenience?", "Yes, everything is also available at utopiastore.ca if you'd rather shop from home."),
        ],
        keywords="best gifts North Vancouver, local gift shop North Van, independent gift shop North Vancouver, gift shop near Lonsdale",
    ),
    dict(
        slug="halloween-gifts-beyond-candy-north-vancouver",
        title="Meaningful Halloween Gifts Beyond Candy in North Vancouver",
        breadcrumb="Halloween Gifts Beyond Candy",
        meta="Halloween gifts beyond candy: tarot decks, crystals, candles, and incense that fit the season and last, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "Halloween doesn't have to mean another bag of candy that's gone by November. At Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver, we carry gifts that fit the spirit of the season without the sugar crash: tarot decks, crystals, candles, and incense all lean into that mysterious, reflective mood.",
            "This works well for teacher gifts, neighbourhood exchanges, or the friend who goes all-in on the season. A small crystal, a mini tarot deck, or a spooky-scented candle reads as considered rather than last-minute.",
        ],
        list_heading="Good Halloween Alternatives to Candy",
        list_items=[
            "A small tarot or oracle deck.",
            "Tumbled crystals; black tourmaline and obsidian suit the season well.",
            "Seasonal candles in smoky, spiced, or woodsy scents.",
            "Incense and small holders.",
        ],
        closing="Find thoughtful Halloween gifts at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop online at utopiastore.ca.",
        faq=[
            ("Is a tarot deck a weird gift for Halloween?", "Not at all; the timing actually suits it well. October is when a lot of people start getting curious about tarot for the first time."),
            ("What is a good Halloween gift for kids or teens?", "Stick to lighter items like scented candles or affordable crystal pieces rather than tarot, which suits an older teen or adult better."),
            ("Do you have Halloween-specific packaging or bundles?", "Ask in store, we can often put together a small seasonal bundle on the spot."),
        ],
        keywords="Halloween gifts North Vancouver, unique Halloween gifts North Van, non-candy Halloween gift ideas, spooky season gift North Vancouver",
    ),
    dict(
        slug="crystal-tarot-gifts-mindful-halloween",
        title="Crystal and Tarot Gifts for a Mindful Halloween",
        breadcrumb="Mindful Halloween Gifts",
        meta="A quieter Halloween gift: obsidian and smoky quartz for grounding, plus a tarot deck for seasonal reflection, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "Halloween has a quieter side too &mdash; the one about reflection, shadow work, and sitting with the turn of the season rather than just costumes and candy. At Utopia Wellness &amp; Gifts, our crystal and tarot selection fits that mindful version of the holiday nicely.",
            "Stones like obsidian and smoky quartz are popular picks this time of year for grounding and release, while a tarot deck gives someone a simple tool to reflect on the year so far as the days get shorter.",
        ],
        list_heading="Good Mindful Halloween Picks",
        list_items=[
            "Obsidian or smoky quartz for grounding and release.",
            "A tarot deck for seasonal reflection.",
            "A calming candle for a quiet night in.",
            "Incense for a simple clearing ritual.",
        ],
        closing="Shop crystals and decks at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or online at utopiastore.ca.",
        faq=[
            ("What crystal is associated with this time of year?", "Obsidian and smoky quartz are commonly associated with grounding and release, which fits the turning-of-the-season feeling many people connect with Halloween and fall."),
            ("Is this a good gift for someone who doesn't love the spooky side of Halloween?", "Yes, this angle is quieter and more reflective, better suited to someone who likes the season's mood without the horror-movie theatrics."),
            ("Can I combine a few of these into one gift?", "Yes, a crystal and a candle together make a simple, complete seasonal gift."),
        ],
        keywords="spiritual Halloween gifts North Vancouver, mindful Halloween gift ideas, grounding crystal gift fall, seasonal reflection gift North Van",
    ),
    dict(
        slug="best-christmas-gifts-north-vancouver-personal",
        title="Best Christmas Gifts in North Vancouver That Feel Personal",
        breadcrumb="Personal Christmas Gifts",
        meta="Christmas gifts that feel personal, not generic: crystal jewelry, decks, candles, and crystals matched to the person, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "Christmas shopping gets generic fast &mdash; another gift card, another box of chocolates. At Utopia Wellness &amp; Gifts on Lonsdale Ave, our Christmas selection leans the other way: tarot decks, crystal jewelry, candles, and crystals chosen with the person in mind.",
            "The easiest way to make a Christmas gift feel personal is to tie it to something specific &mdash; their birth month for a jewelry piece, their current life stage for a tarot deck, or what would help them most heading into the new year.",
        ],
        list_heading="Christmas Gift Directions",
        list_items=[
            "<strong>Crystal jewelry</strong> &mdash; a lasting, wearable gift.",
            "<strong>Tarot or oracle deck</strong> &mdash; for reflection into the new year.",
            "<strong>Candles</strong> &mdash; cosy, low-cost, almost always welcome.",
            "<strong>Crystals</strong> &mdash; matched to an intention for the year ahead.",
        ],
        closing="Visit Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver for thoughtful Christmas presents, or shop online at utopiastore.ca.",
        faq=[
            ("What is a good Christmas gift if I'm shopping for the whole family?", "Candles and small crystals are versatile enough to work across a range of ages and tastes, making them an easy pick for group gifting."),
            ("Can you help me shop for multiple people at once?", "Yes, bring us your list and budget and we can help you move through it efficiently."),
            ("Do you offer gift wrapping for the holidays?", "Ask our team in store, we're happy to help make your gifts presentation-ready."),
        ],
        keywords="best Christmas gifts North Vancouver, meaningful Christmas gifts North Van, personal Christmas gift ideas, Christmas gift shop Lonsdale",
    ),
    dict(
        slug="unique-stocking-stuffers-north-vancouver",
        title="Unique Stocking Stuffers from Utopia Wellness & Gifts",
        breadcrumb="Unique Stocking Stuffers",
        meta="Stocking stuffers that feel like real gifts: small crystals, incense, mini candles, and simple jewelry under $40, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "Stockings are for small, surprising things, not an afterthought stuffed in at the last minute. At Utopia Wellness &amp; Gifts, our stocking-stuffer range &mdash; small crystals, incense, mini candles, and simple jewelry, mostly in the $30 to $40 range and under &mdash; gives you plenty to pick from without blowing the budget.",
            "A tumbled crystal with a short note about its meaning, a mini candle, or a simple pendant all fit neatly into a stocking while still feeling like a real gift.",
        ],
        list_heading="Good Stocking Stuffer Picks",
        list_items=[
            "Tumbled crystals and palm stones.",
            "Mini candles.",
            "Small incense sets.",
            "Simple stud earrings or pendants.",
        ],
        closing="Find small meaningful stocking stuffers in store at 1826 Lonsdale Ave, or online at utopiastore.ca.",
        faq=[
            ("What is the best stocking stuffer for someone hard to shop for?", "A tumbled crystal paired with a short explanation of its meaning works for almost anyone and keeps the pressure low."),
            ("Can I buy a few stocking stuffers as a set?", "Yes, we can help you put together a small bundle across a few people in one visit."),
            ("Do these stay under $40 each?", "Yes, this category is specifically built around that lower price point while still feeling considered."),
        ],
        keywords="unique stocking stuffers North Vancouver, small Christmas gifts under $40, stocking stuffer ideas North Van, crystal stocking stuffers",
    ),
    dict(
        slug="last-minute-christmas-gifts-north-vancouver",
        title="Thoughtful Last-Minute Christmas Gifts in North Vancouver",
        breadcrumb="Last-Minute Christmas Gifts",
        meta="Last-minute Christmas gifts you can pick up same-day that still feel thoughtful: candles, crystals, and jewelry, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "Running out of time doesn't mean you have to give a rushed gift. At Utopia Wellness &amp; Gifts on Lonsdale Ave, a candle, a crystal, or a small jewelry piece can be picked up same-day and still feel like you put real thought into it &mdash; no shipping delays, no panic.",
            "Keep it simple: pick based on what you know about the person &mdash; a calming scent for someone stressed, a confidence stone for someone starting something new &mdash; and let the product do the rest.",
        ],
        list_heading="Good Last-Minute Picks",
        list_items=[
            "A candle in a universally liked scent.",
            "A tumbled crystal with a quick explanation card.",
            "Small jewelry pieces, ready to wear immediately.",
            "Incense sets, simple and self-explanatory.",
        ],
        closing="Shop last-minute meaningful gifts at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or online at utopiastore.ca.",
        faq=[
            ("How late can I shop in store before Christmas?", "Check our current holiday hours before visiting, but our in-store selection means you can walk in and walk out with something complete, no waiting on shipping."),
            ("Will a last-minute gift look like I waited too long?", "Not if you pick something specific to the person rather than something generic; a short note explaining why you chose it goes a long way."),
            ("Can I get something gift-wrapped quickly?", "Ask our team when you arrive, we'll help you move fast without the gift looking rushed."),
        ],
        keywords="last minute Christmas gifts North Vancouver, same day Christmas gift North Van, quick thoughtful gift ideas, Christmas Eve gift shopping North Vancouver",
    ),
    dict(
        slug="crystal-jewelry-christmas-gift-north-vancouver",
        title="Crystal Jewelry as a Christmas Gift",
        breadcrumb="Crystal Jewelry Christmas Gift",
        meta="Crystal jewelry makes a premium Christmas gift without sizing guesswork. Best picks and how to avoid sizing issues, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "For a Christmas gift that feels a step above the usual, crystal jewelry hits a nice middle ground: it's a genuine present, not just a stocking filler, but it doesn't require guessing clothing sizes the way other gifts do. At Utopia Wellness &amp; Gifts, our jewelry cases are stocked with pieces built around birthstones and intentions.",
            "Rose quartz for warmth and connection, amethyst for calm heading into the new year, or a birthstone piece matched to the person &mdash; all read as premium without a premium conversation about sizing or taste.",
        ],
        list_heading="Good Christmas Jewelry Picks",
        list_items=[
            "A birthstone pendant or ring.",
            "Rose quartz for connection and warmth.",
            "Amethyst for calm and reflection.",
            "A simple stacking bracelet set.",
        ],
        closing="Explore our jewelry collection before Christmas at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or online at utopiastore.ca.",
        faq=[
            ("Is crystal jewelry a good main gift for Christmas, not just a stocking stuffer?", "Yes, a well-chosen piece works well as a primary gift, especially when tied to a birthstone or specific intention for the person."),
            ("How do I avoid sizing issues with jewelry?", "Stick to adjustable pieces like pendants, simple bracelets, or stud earrings, which avoid most sizing concerns entirely."),
            ("Can you help me pick a piece based on their birth month?", "Yes, bring us their birthday and we can match a birthstone or corresponding crystal."),
        ],
        keywords="crystal jewelry Christmas gift North Vancouver, birthstone jewelry Christmas present, premium Christmas gift North Van, rose quartz Christmas gift",
    ),
    dict(
        slug="tarot-oracle-decks-christmas-gifts",
        title="Tarot and Oracle Decks as Memorable Christmas Gifts",
        breadcrumb="Decks as Christmas Gifts",
        meta="Tarot and oracle decks make Christmas gifts that last all year. Picks for beginners and collectors, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "A tarot or oracle deck tends to stick around long after Christmas morning, used throughout the year rather than set aside. At Utopia Wellness &amp; Gifts on Lonsdale Ave, decks are one of our most repeat-requested Christmas gifts: personal, lasting, and fitting people at very different stages of interest.",
            "A gentle, affirmation-style oracle deck suits someone newly curious; a classic tarot deck with a guidebook suits someone ready to learn the system.",
        ],
        list_heading="Good Christmas Deck Picks",
        list_items=[
            "A beginner-friendly oracle deck for someone new to the space.",
            "A classic tarot deck with guidebook for someone ready to learn.",
            "A beautifully illustrated deck for the collector on your list.",
            "A deck paired with a small journal for reflection through the new year.",
        ],
        closing="Choose the perfect deck at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop online at utopiastore.ca.",
        faq=[
            ("What if the person already owns a deck?", "Many tarot and oracle enthusiasts collect multiple decks for different moods or questions, so a second deck is still a welcome gift."),
            ("Is a guidebook necessary for a first deck?", "For a true beginner, yes; it makes the deck usable right away instead of sitting unopened."),
            ("What is a good deck for someone who just wants something beautiful to look at?", "We carry several decks chosen specifically for their artwork; ask in store and we'll point you to our most visually striking options."),
        ],
        keywords="tarot Christmas gift North Vancouver, oracle deck Christmas present, best tarot deck gift, Christmas gift for tarot lover",
    ),
    dict(
        slug="best-boxing-day-gift-ideas-north-vancouver",
        title="Best Boxing Day Gift Ideas in North Vancouver",
        breadcrumb="Boxing Day Gift Ideas",
        meta="Boxing Day is a good moment for a late gift or a small self-treat: crystals, candles, jewelry, and decks, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "Boxing Day doesn't have to be only about returns and big-box deals. At Utopia Wellness &amp; Gifts on Lonsdale Ave, it's a good moment to pick up a late gift for someone you missed, or to treat yourself to something you held off on through the Christmas rush.",
            "Crystals, candles, and jewelry pieces all make sense here, either as a delayed gift or as a small post-holiday treat before the new year starts.",
        ],
        list_heading="Good Boxing Day Picks",
        list_items=[
            "A crystal or candle you've been eyeing.",
            "A jewelry piece as a delayed gift.",
            "A tarot deck to start the new year with intention.",
            "Small gifts for anyone you missed over the holidays.",
        ],
        closing="Visit Utopia on Boxing Day for meaningful finds, 1826 Lonsdale Ave, or shop at utopiastore.ca.",
        faq=[
            ("Is Boxing Day a good time to shop for a late Christmas gift?", "Yes, it's a natural catch-up moment if you missed someone or want to add to what you already gave."),
            ("Do you have Boxing Day sales?", "Check in store or online for current seasonal offers around that time."),
            ("Is this a good day to shop for myself?", "Plenty of people treat Boxing Day as a small self-gifting moment after a busy holiday season, and it's a good time to do exactly that."),
        ],
        keywords="Boxing Day gifts North Vancouver, Boxing Day shopping North Van, post-Christmas gift ideas, Boxing Day deals North Vancouver",
    ),
    dict(
        slug="gifts-to-give-yourself-after-christmas",
        title="Thoughtful Gifts to Give Yourself After Christmas",
        breadcrumb="Self-Gifts After Christmas",
        meta="A small self-care reset after the holidays: a crystal, candle, book, or jewelry piece for the year ahead, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "Christmas is spent giving to everyone else &mdash; Boxing Day and the days after are a reasonable moment to give something back to yourself. At Utopia Wellness &amp; Gifts, this self-care angle shows up every year: a crystal chosen for what you need heading into January, a candle for quiet nights, or a book to sit with.",
            "There's nothing indulgent about it &mdash; it's a small reset before the new year starts, and exactly the kind of gift people forget to give themselves during the holiday rush.",
        ],
        list_heading="Good Self-Gifting Picks",
        list_items=[
            "A crystal matched to an intention for the year ahead.",
            "A candle for quiet, unwinding evenings.",
            "A book on reflection or self-growth.",
            "A small piece of jewelry you've been holding off on.",
        ],
        closing="Treat yourself at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop online at utopiastore.ca.",
        faq=[
            ("Is it strange to shop for myself after Christmas?", "Not at all, it's a common and sensible time to pause and choose something just for you after a season spent focused on everyone else."),
            ("What is a good reset crystal for the new year?", "Clear quartz for clarity or amethyst for calm are both popular picks heading into January."),
            ("Can I combine a few self-care items into one purchase?", "Yes, a candle and a crystal together make a simple, complete self-care set."),
        ],
        keywords="self-care gifts North Vancouver, Boxing Day self gifts, treat yourself gift ideas, new year reset gift North Van",
    ),
    dict(
        slug="valentines-day-gifts-north-vancouver",
        title="Meaningful Valentine's Day Gifts in North Vancouver",
        breadcrumb="Valentine's Day Gifts",
        meta="Valentine's gifts that last past February 14: rose quartz jewelry, candles, and couples' tarot, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "Flowers and chocolate are fine, but they don't last. At Utopia Wellness &amp; Gifts on Lonsdale Ave, rose quartz jewelry, candles, and tarot decks make a Valentine's Day gift that sticks around well past February 14th, and carries more meaning than something picked up last-minute from a grocery aisle.",
            "Rose quartz is the obvious pick here &mdash; it's associated with love and emotional connection, and works as jewelry, a tumbled stone, or paired with a candle for an evening at home.",
        ],
        list_heading="Good Valentine's Day Picks",
        list_items=[
            "Rose quartz jewelry.",
            "A candle for a quiet night in together.",
            "A shared tarot or oracle ritual for couples.",
            "A small crystal paired with a heartfelt note.",
        ],
        closing="Find heartfelt Valentine's gifts at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop at utopiastore.ca.",
        faq=[
            ("Is rose quartz specifically a love stone?", "It's widely associated with love, warmth, and emotional connection, which is why it's such a popular Valentine's Day pick."),
            ("What is a good Valentine's gift for a new relationship?", "Keep it lighter &mdash; a candle or a small tumbled stone rather than jewelry, which can feel like a bigger statement early on."),
            ("Can this work for a self-love Valentine's gift too?", "Yes, plenty of people buy rose quartz or a candle for themselves as a Valentine's Day gift; it's not only for couples."),
        ],
        keywords="Valentine's Day gifts North Vancouver, meaningful Valentine gifts North Van, rose quartz Valentine's gift, romantic gift ideas North Vancouver",
    ),
    dict(
        slug="mothers-day-gifts-north-vancouver-not-flowers",
        title="Best Mother's Day Gifts in North Vancouver (That Aren't Flowers)",
        breadcrumb="Mother's Day Gifts",
        meta="Mother's Day gifts that last beyond flowers: birthstone jewelry, candles, books, and crystals, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "Flowers wilt within a week. At Utopia Wellness &amp; Gifts on Lonsdale Ave, jewelry, candles, books, and crystals give Mother's Day a gift that lasts well beyond the day itself &mdash; something she'll actually keep using.",
            "A birthstone piece, a calming candle for some quiet time to herself, or a book worth sitting with all land as more considered than the standard bouquet, without requiring a big budget.",
        ],
        list_heading="Good Mother's Day Picks",
        list_items=[
            "A birthstone or rose quartz jewelry piece.",
            "A calming candle for quiet time.",
            "A spiritual growth or reflection book.",
            "A small crystal matched to what she needs right now.",
        ],
        closing="Shop thoughtful Mother's Day gifts at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or online at utopiastore.ca.",
        faq=[
            ("What is a good Mother's Day gift if she doesn't need anything?", "Focus on experience-adjacent gifts like a candle for quiet time or a book, rather than more physical clutter."),
            ("Can I combine a few smaller items for a more complete Mother's Day gift?", "Yes, a candle and a crystal, or a book and a small jewelry piece, both make a nice combined gift."),
            ("Do you have gift sets ready specifically for Mother's Day?", "Check in store around the holiday; we often put together seasonal bundles."),
        ],
        keywords="Mother's Day gifts North Vancouver, unique Mother's Day gifts North Van, Mother's Day gift ideas not flowers, meaningful gift for mom",
    ),
    dict(
        slug="fathers-day-gift-ideas-north-vancouver",
        title="Father's Day Gift Ideas from Utopia Wellness & Gifts",
        breadcrumb="Father's Day Gifts",
        meta="Father's Day gifts beyond tools and golf: grounding crystals, books, candles, and incense, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "Father's Day gifts can be tricky &mdash; tools and golf accessories only go so far. At Utopia Wellness &amp; Gifts on Lonsdale Ave, books, crystals, candles, and incense offer a different direction: practical, low-key, and still genuinely useful.",
            "A grounding stone like black tourmaline, a simple reflection book, or a low-key scented candle all work well, especially for a dad who's hard to shop for or already has everything in the usual categories.",
        ],
        list_heading="Good Father's Day Picks",
        list_items=[
            "A grounding crystal like black tourmaline or smoky quartz.",
            "A book on growth, mindfulness, or reflection.",
            "A simple, non-floral scented candle.",
            "Incense for a quiet ritual at home.",
        ],
        closing="Discover practical yet meaningful Father's Day gifts at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or online at utopiastore.ca.",
        faq=[
            ("What if my dad isn't into anything spiritual?", "A grounding stone or a simple candle reads as low-key and practical rather than overtly spiritual; it works even for dads who wouldn't call themselves into this stuff."),
            ("Is a book a safe Father's Day gift?", "Yes, especially a reflection or self-growth title that doesn't require any prior interest in the subject."),
            ("What is a good budget range for this occasion?", "Most of our Father's Day-friendly picks sit comfortably under $50."),
        ],
        keywords="Father's Day gifts North Vancouver, meaningful Father's Day gift ideas, practical gifts for dad, unique Father's Day present North Van",
    ),
    dict(
        slug="new-year-gifts-intentions-north-vancouver",
        title="Thoughtful New Year Gifts and Intentions in North Vancouver",
        breadcrumb="New Year Gifts & Intentions",
        meta="New Year gifts that nudge a fresh start: tarot decks, crystals, journals, and candles for setting intentions, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "The new year is one of the few times a gift can double as a genuine nudge toward a fresh start. At Utopia Wellness &amp; Gifts on Lonsdale Ave, tarot decks, crystals, journals, and candles all fit that moment &mdash; less happy new year and more here's something to help you follow through.",
            "A tarot deck for monthly reflection, a journal for setting intentions, or a crystal matched to a specific goal all give the new year more structure than a resolution alone usually provides.",
        ],
        list_heading="Good New Year Gift Picks",
        list_items=[
            "A tarot or oracle deck for monthly reflection.",
            "A journal for setting and tracking intentions.",
            "A crystal matched to a specific goal for the year.",
            "A candle to mark the start of something new.",
        ],
        closing="Start the year with a meaningful gift from Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop at utopiastore.ca.",
        faq=[
            ("Is this a good gift for someone who doesn't usually keep New Year's resolutions?", "Yes, pairing a gift with a simple ritual like lighting a candle or drawing a card tends to stick better than a resolution alone."),
            ("What crystal is good for new beginnings?", "Clear quartz for clarity and citrine for confidence are both popular picks for setting intentions heading into a new year."),
            ("Can I combine a journal and a deck as one gift?", "Yes, that combination is one of our most popular New Year gift pairings."),
        ],
        keywords="New Year gifts North Vancouver, intentional gifts North Van, new year reflection gift, tarot for new year intentions",
    ),
    dict(
        slug="unique-easter-gifts-north-vancouver-beyond-chocolate",
        title="Unique Easter Gifts in North Vancouver Beyond Chocolate",
        breadcrumb="Easter Gifts Beyond Chocolate",
        meta="Easter gifts beyond chocolate: small crystals, spring candles, and books for a basket, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "Easter baskets don't have to be all chocolate. At Utopia Wellness &amp; Gifts on Lonsdale Ave, small crystals, candles, and books make a nice alternative or addition to the usual Easter sweets &mdash; especially for older kids, teens, or adults who'd rather have something that lasts.",
            "A small crystal tucked into a basket, a spring-scented candle, or a short, meaningful book all fit the lighter, renewal-themed spirit of the season without defaulting to sugar.",
        ],
        list_heading="Good Easter Alternatives",
        list_items=[
            "Small tumbled crystals for a basket.",
            "Spring or floral-scented candles.",
            "A short reflection or growth-themed book.",
            "Small jewelry pieces for older kids or teens.",
        ],
        closing="Find non-traditional Easter gifts at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop online at utopiastore.ca.",
        faq=[
            ("Is a crystal an appropriate Easter basket item for a teenager?", "Yes, this is a popular option for older kids and teens who've outgrown a basket full of candy."),
            ("What is a good Easter gift that fits the renewal theme of spring?", "Crystals associated with growth and clarity, like clear quartz, along with lighter floral candle scents, both fit nicely."),
            ("Can I mix a few small items into one Easter gift?", "Yes, a small crystal plus a mini candle makes a simple, complete non-candy Easter gift."),
        ],
        keywords="unique Easter gifts North Vancouver, non-candy Easter basket ideas, Easter gifts for teens, spring gift ideas North Van",
    ),
    dict(
        slug="diwali-gift-ideas-north-vancouver",
        title="Diwali Gift Ideas in North Vancouver from Utopia",
        breadcrumb="Diwali Gift Ideas",
        meta="Diwali gifts that fit the festival of light: candles, prosperity crystals like citrine, and incense, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "Diwali centres on light, renewal, and celebration &mdash; themes that line up naturally with several things Utopia Wellness &amp; Gifts already carries on Lonsdale Ave: candles, crystals, and incense. These make a thoughtful gift for Diwali gatherings, hostess gifts, or simply marking the occasion.",
            "A beautifully scented candle, a crystal chosen for prosperity or clarity, or a quality incense set all fit the spirit of the festival, especially as a gift brought to a celebration.",
        ],
        list_heading="Good Diwali Gift Picks",
        list_items=[
            "Candles, a natural fit for a festival centred on light.",
            "Crystals associated with prosperity or clarity, such as citrine.",
            "Quality incense sets.",
            "Small jewelry pieces as a festive gift.",
        ],
        closing="Celebrate with thoughtful gifts from Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop online at utopiastore.ca.",
        faq=[
            ("Is a candle a culturally appropriate Diwali gift?", "Candles and light-based gifts fit well with the festival's themes, though we'd always encourage choosing something based on what the specific recipient or household would appreciate."),
            ("What is a good host gift to bring to a Diwali gathering?", "A candle or small incense set makes a thoughtful, low-pressure gift to bring along."),
            ("Do you carry gold or warm-toned crystal pieces that suit the occasion?", "Yes, citrine and similar warm-toned stones are popular picks this time of year."),
        ],
        keywords="Diwali gifts North Vancouver, Diwali hostess gift ideas, festival of lights gift, Diwali candle gift North Van",
    ),
    dict(
        slug="hanukkah-gift-ideas-north-vancouver",
        title="Hanukkah Gift Ideas That Feel Personal in North Vancouver",
        breadcrumb="Hanukkah Gift Ideas",
        meta="Hanukkah gifts suited to a nightly tradition: candles, small crystals, books, and jewelry, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "Hanukkah gifting often leans toward something small and meaningful rather than one big present, which suits what Utopia Wellness &amp; Gifts already does well: candles, crystals, books, and jewelry that feel personal rather than generic.",
            "A candle for one of the nights, a small crystal, or a jewelry piece chosen with the person in mind all work well, especially as part of a tradition built around giving something each night.",
        ],
        list_heading="Good Hanukkah Gift Picks",
        list_items=[
            "Candles, a natural fit for a festival centred on light.",
            "Small crystals for a nightly gift tradition.",
            "A meaningful book.",
            "A simple jewelry piece.",
        ],
        closing="Shop meaningful Hanukkah gifts at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or online at utopiastore.ca.",
        faq=[
            ("Is it common to give a small gift each night of Hanukkah?", "Many families do follow that tradition, which makes smaller items like crystals or candles especially well suited to the occasion."),
            ("What is a good budget-friendly option for multiple nights of gifting?", "Tumbled crystals and small candles both stay affordable even when you're giving something several nights in a row."),
            ("Can you help me put together a small set for the full holiday?", "Yes, bring us the number of gifts you need and your budget and we can help you build a set."),
        ],
        keywords="Hanukkah gifts North Vancouver, Hanukkah gift ideas, meaningful Hanukkah present, Hanukkah candle gift",
    ),
    dict(
        slug="lunar-new-year-gift-ideas-north-vancouver",
        title="Lunar New Year Gift Ideas in North Vancouver",
        breadcrumb="Lunar New Year Gifts",
        meta="Lunar New Year gifts in lucky red and gold: prosperity crystals like citrine, incense, and festive pieces, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "Lunar New Year favours gifts in red and gold &mdash; colours tied to luck and prosperity &mdash; along with items that mark a fresh start for the year ahead. At Utopia Wellness &amp; Gifts on Lonsdale Ave, crystals in warm, gold-toned shades, incense, and festive pieces fit naturally into that tradition.",
            "Citrine, often associated with prosperity, and other warm-toned stones make a thoughtful gift, as does a quality incense set for marking the occasion at home.",
        ],
        list_heading="Good Lunar New Year Gift Picks",
        list_items=[
            "Citrine or other gold-toned crystals, associated with prosperity.",
            "Incense for marking the occasion.",
            "Red or gold-toned jewelry pieces.",
            "Candles for a festive gathering.",
        ],
        closing="Find festive yet meaningful gifts at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop online at utopiastore.ca.",
        faq=[
            ("What crystal is traditionally associated with luck or prosperity?", "Citrine is one of the most commonly referenced stones for prosperity, which is why it's a popular Lunar New Year pick."),
            ("Is red and gold just decorative, or does it mean something?", "Red and gold both carry strong associations with luck and prosperity in Lunar New Year tradition, which is why gifts in those tones are especially popular."),
            ("What is a good hostess gift for a Lunar New Year gathering?", "A small gold-toned crystal or a quality incense set both work well as a gift to bring along."),
        ],
        keywords="Lunar New Year gifts North Vancouver, Chinese New Year gift ideas, prosperity crystal gift, red and gold gift North Van",
    ),
    dict(
        slug="canadian-thanksgiving-gifts-north-vancouver",
        title="Best Gifts for Canadian Thanksgiving in North Vancouver",
        breadcrumb="Thanksgiving Host Gifts",
        meta="Canadian Thanksgiving host gifts nicer than wine: seasonal candles, small crystals, and incense, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "Thanksgiving gifting usually comes down to one thing: a good host gift. At Utopia Wellness &amp; Gifts on Lonsdale Ave, candles and crystals make an easy, low-pressure option for whoever's hosting dinner &mdash; something nicer than a bottle of wine but just as simple to pick up on your way over.",
            "A seasonal candle in a warm, cosy scent or a small crystal for their home both read as thoughtful without requiring much planning.",
        ],
        list_heading="Good Thanksgiving Host Gift Picks",
        list_items=[
            "A seasonal candle in a warm, cosy scent.",
            "A small crystal for their home.",
            "A small incense set.",
            "A book, for a host who appreciates something quieter.",
        ],
        closing="Bring a thoughtful host gift from Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop at utopiastore.ca.",
        faq=[
            ("What is a good last-minute host gift for Thanksgiving dinner?", "A seasonal candle is one of the easiest, most universally appreciated options if you're short on time."),
            ("Is a crystal a strange hostess gift?", "Not at all, a small, tasteful crystal reads as a thoughtful home gift, especially when gifted alongside a short note."),
            ("Can I grab something quickly on my way to dinner?", "Yes, our Lonsdale Ave location makes it easy for a quick stop before heading to a Thanksgiving gathering."),
        ],
        keywords="Thanksgiving gifts North Vancouver, hostess gifts North Van, Canadian Thanksgiving host gift ideas, Thanksgiving candle gift",
    ),
    dict(
        slug="remembrance-day-thoughtful-tokens-north-vancouver",
        title="Remembrance Day Thoughtful Gifts and Tokens in North Vancouver",
        breadcrumb="Remembrance Day Tokens",
        meta="Quiet, respectful Remembrance Day tokens: a simple candle, a keepsake, or a grounding stone, from Utopia Wellness & Gifts on Lonsdale Ave, North Vancouver.",
        intro=[
            "Remembrance Day calls for something quiet and respectful rather than a typical gift. At Utopia Wellness &amp; Gifts on Lonsdale Ave, a small, understated token &mdash; a simple candle to light in remembrance, or a quiet keepsake piece &mdash; can offer a meaningful way to mark the day for someone reflecting on service and sacrifice.",
            "This isn't a holiday for bold or celebratory gifting; it calls for something small, sincere, and without a loud sales message attached.",
        ],
        list_heading="Good Remembrance Day Tokens",
        list_items=[
            "A simple candle for quiet reflection.",
            "A small, understated keepsake piece.",
            "A short, meaningful book.",
            "A grounding stone for comfort during a difficult day.",
        ],
        closing="Find quiet, meaningful pieces at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, or shop online at utopiastore.ca.",
        faq=[
            ("What is an appropriate gift for someone honouring a family member who served?", "A simple candle or a small keepsake item tends to feel more fitting than anything overtly festive or commercial."),
            ("Should this kind of gift be given on the day, or before?", "Either works &mdash; a quiet token given a day or two ahead, or on the day itself, both feel appropriate."),
            ("Is it appropriate to give this kind of gift to a veteran directly?", "Yes, a simple, sincere token is generally well received; keep the gesture understated and personal."),
        ],
        keywords="thoughtful gifts North Vancouver Remembrance Day, Remembrance Day keepsake, quiet remembrance gift ideas, Remembrance Day candle",
    ),
    dict(
        slug="holiday-gift-guide-utopia-wellness-gifts",
        title="Holiday Gift Guide: Meaningful Presents from Utopia Wellness & Gifts",
        breadcrumb="Holiday Gift Guide",
        meta="A holiday gift guide covering Christmas, Hanukkah, and the season: decks, crystal jewelry, candles, crystals, incense, and books, from Utopia Wellness & Gifts, North Vancouver.",
        intro=[
            "From Christmas to Hanukkah to the general rush of the holiday season, Utopia Wellness &amp; Gifts on Lonsdale Ave is a one-stop option for gifts that feel personal rather than generic, no matter which holiday you're shopping for. Our collection spans tarot and oracle decks, crystal jewelry, candles, crystals, incense, and books.",
            "Whether you're after a single standout gift or a handful of smaller stocking-stuffer-style items, this roundup pulls together our most popular holiday picks in one place.",
        ],
        list_heading="Holiday Season Picks by Category",
        list_items=[
            "<strong>Tarot and oracle decks</strong> &mdash; a lasting gift for reflection.",
            "<strong>Crystal jewelry</strong> &mdash; wearable, meaningful, and broadly appealing.",
            "<strong>Candles</strong> &mdash; an easy, almost universally welcome pick.",
            "<strong>Crystals</strong> &mdash; matched to an intention for the person or the year ahead.",
            "<strong>Books</strong> &mdash; for the reader who wants something to sit with.",
        ],
        closing="Explore our full collection in store at 1826 Lonsdale Ave, or online at utopiastore.ca.",
        faq=[
            ("Where should I start if I have a long holiday gift list?", "Begin with candles and small crystals &mdash; they work for almost anyone &mdash; then move to jewelry or decks for the people you know better."),
            ("Can I shop your full holiday range online?", "Yes, our full collection is available at utopiastore.ca in addition to in store at 1826 Lonsdale Ave."),
            ("Do you offer gift wrapping during the holiday season?", "Ask our team in store, we're happy to help make your gifts ready to give."),
        ],
        keywords="holiday gift guide North Vancouver, best gifts North Vancouver holiday, holiday shopping North Van, Christmas and Hanukkah gift guide",
    ),
]


def render_body(post):
    out = [ "      " + H2(post["list_heading"]), "      " + UL(post["list_items"]) ]
    if post.get("closing"):
        out.append("      " + P(post["closing"]))
    out.append("      " + H2("Frequently Asked Questions"))
    for q, a in post["faq"]:
        out.append("      " + H3(q))
        out.append("      " + P(a))
    out.append('      <p class="text-[.8rem] font-light mt-8" style="color:var(--text-muted)"><strong>People also search for:</strong> ' + post["keywords"] + "</p>")
    return "\n".join(out)


def faq_schema(faq):
    def esc(s):
        s = re.sub(r"<[^>]+>", "", s)
        s = (s.replace("&amp;", "&").replace("&mdash;", "-").replace("&ndash;", "-")
               .replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&rsquo;", "'").replace("&lsquo;", "'")
               .replace("&eacute;", "e"))
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

    seen = set()
    for post in POSTS:
        assert post["slug"] not in seen, "dup slug " + post["slug"]
        seen.add(post["slug"])
        title = post["title"].replace("&", "&amp;") if "&" in post["title"] and "&amp;" not in post["title"] else post["title"]
        html = tpl
        html = html.replace("{{TITLE}}", title)
        html = html.replace("{{META_DESCRIPTION}}", post["meta"])
        html = html.replace("{{SLUG}}", post["slug"])
        html = html.replace("{{BREADCRUMB}}", post["breadcrumb"])
        html = html.replace("{{DATE_ISO}}", ISO)
        html = html.replace("{{DATE}}", DATE)
        intro_html = "\n".join("      " + P(p) for p in post["intro"])
        html = html.replace("{{CONTENT_INTRO}}", intro_html)
        html = html.replace("{{CONTENT_BODY}}", render_body(post))
        html = html.replace("</body>", faq_schema(post["faq"]) + "\n</body>")
        with open(os.path.join(BLOG_DIR, post["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"wrote {post['slug']}.html")
    print(f"total: {len(POSTS)}")


if __name__ == "__main__":
    main()
