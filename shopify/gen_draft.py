"""
Blog posts from draft.md. Generate from blog/TEMPLATE.html.
Run:  python shopify/gen_draft.py
Same rendering approach as gen_tier1/gen_tier3.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(__file__))
TEMPLATE = os.path.join(ROOT, "blog", "TEMPLATE.html")
BLOG_DIR = os.path.join(ROOT, "blog")

P_CLS = 'text-[clamp(0.9rem,1.8vw,1.05rem)] font-light leading-[1.9] mb-6'
H2_CLS = 'text-[clamp(1.2rem,3vw,1.7rem)] leading-[1.3] mt-12 mb-5'
H3_CLS = 'text-[1.1rem] leading-[1.3] mt-8 mb-3'
UL_CLS = 'list-disc pl-6 mb-6 space-y-2 text-[clamp(0.9rem,1.8vw,1.05rem)] font-light leading-[1.9]'
DATE = "September 9, 2026"
ISO = "2026-09-09"


def P(t): return f'<p class="{P_CLS}" style="color:var(--text-body)">{t}</p>'
def H2(t): return f'<h2 class="{H2_CLS}" style="font-family:var(--font-display);color:var(--text-heading)">{t}</h2>'
def H3(t): return f'<h3 class="{H3_CLS}" style="font-family:var(--font-display);color:var(--text-heading)">{t}</h3>'
def UL(items):
    lis = "\n".join(f"        <li>{it}</li>" for it in items)
    return f'<ul class="{UL_CLS}" style="color:var(--text-body)">\n{lis}\n      </ul>'


POSTS = [
    {
        "slug": "tumbled-stones-affordable-meaningful-gift",
        "title": "Tumbled Stones: A Small, Affordable Gift That Still Feels Meaningful",
        "breadcrumb": "Tumbled Stones Gift",
        "category": "GIFTS",
        "meta": "Tumbled stones are an easy, affordable gift that still feels personal. A guide to what they are, how to care for them, and why they make a great gift, from Utopia in North Vancouver.",
        "intro": [
            "If you are looking for an easy, affordable gift in North Vancouver that still feels personal, a tumbled stone is one of the best places to start. Utopia Wellness &amp; Gifts on Lonsdale Ave keeps a wide rotating selection in store, wrapped and ready the same day.",
            "Tumbled stones are rough crystals polished smooth in a rock tumbler, which brings out their colour and pattern while making them easy to carry in a pocket, purse, or car.",
        ],
        "body": [
            ("h2", "Why Tumbled Stones Make a Good Gift"),
            ("p", "Each stone carries its own folklore and meaning, which is part of what makes them such a thoughtful small gift: amethyst for calm, rose quartz for love and emotional warmth, citrine for positivity and confidence. They are small, inexpensive, easy to personalise to the recipient, and meaningful without being a big commitment."),
            ("h2", "Everyday Uses"),
            ("p", "Beyond gifting, people use tumbled stones in jewellery, home d&eacute;cor, meditation, and even bath rituals (water-safe stones only). Many like to cleanse them regularly under running water, in moonlight, or with sage smoke to keep their energy feeling fresh."),
            ("p", "Stop by Utopia Wellness &amp; Gifts on Lonsdale Ave to pick a stone in person, since most people find they are drawn to one once they hold it."),
        ],
        "faq": [
            ("What is a tumbled stone?", "A tumbled stone is a rough crystal that has been smoothed and polished in a rock tumbler, giving it a rounded shape and glossy finish."),
            ("Are tumbled stones a good gift?", "Yes. They are affordable, easy to carry, and each stone carries its own meaning you can match to the recipient, which makes them one of the most popular small gifts."),
            ("How do I clean a tumbled stone?", "Common methods include rinsing under water if the stone is water-safe, leaving it in moonlight overnight, or passing it through sage or palo santo smoke."),
            ("Where can I buy tumbled stones in North Vancouver?", "Utopia Wellness & Gifts, 1826 Lonsdale Ave, carries a rotating selection in store, with free parking at the back and gift wrapping available."),
        ],
        "keywords": "crystal gifts, cleansing crystals, healing crystals, crystal shop North Vancouver",
    },
    {
        "slug": "black-obsidian-grounding-protective-gift",
        "title": "Black Obsidian: A Grounding, Protective Gift",
        "breadcrumb": "Black Obsidian Gift",
        "category": "CRYSTALS",
        "meta": "Black obsidian is a grounding, protective stone and a striking gift for someone going through a stressful stretch. What it means and how to cleanse it, from Utopia in North Vancouver.",
        "intro": [
            "Looking for a gift with a bit more weight to it, literally and symbolically? Black obsidian is one of the most requested protective stones at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, and it makes a striking gift for anyone going through a stressful stretch.",
            "Black obsidian is volcanic glass, formed when lava cools too quickly to crystallise, giving it a smooth, glassy, jet-black finish.",
        ],
        "body": [
            ("h2", "What Black Obsidian Is Known For"),
            ("p", "It is traditionally associated with protection and grounding, often chosen by people who feel scattered, anxious, or like they need an energetic boundary. It is also commonly used in meditation and said to help bring buried emotions to the surface for release."),
            ("h2", "Why It Makes a Good Gift"),
            ("p", "A striking, substantial-feeling stone with a clear, easy-to-explain meaning &mdash; good for someone navigating a big change or a hard season. Pick one up in store on Lonsdale Ave, or ask us about pairing it with a candle for a simple grounding gift set."),
        ],
        "faq": [
            ("What is black obsidian good for?", "It is traditionally associated with grounding, protection, and emotional release, and is a popular choice for meditation."),
            ("Is black obsidian a good gift?", "Yes, especially for someone going through stress or a major life transition, since its meaning of protection and grounding is easy to explain when giving it."),
            ("How do I cleanse black obsidian?", "Smoke cleansing with sage or palo santo, or leaving it in moonlight, are the most common methods."),
            ("Where can I buy black obsidian in North Vancouver?", "Utopia Wellness & Gifts on Lonsdale Ave carries black obsidian in store, wrapped on request."),
        ],
        "keywords": "protection crystals, black obsidian meaning, grounding stones, crystal shop Vancouver",
    },
    {
        "slug": "herkimer-diamond-gift-spiritual-seeker",
        "title": "Herkimer Diamond: A Gift for the Spiritual Seeker",
        "breadcrumb": "Herkimer Diamond Gift",
        "category": "CRYSTALS",
        "meta": "A Herkimer diamond is a special gift for someone further along in their crystal practice. What makes it different from quartz and how to use it, from Utopia in North Vancouver.",
        "intro": [
            "For the person on your list who already has a crystal collection, a Herkimer diamond is one of the more special gifts you can give. Utopia Wellness &amp; Gifts carries a small, curated selection in store on Lonsdale Ave, since this is a premium pick rather than an everyday stone.",
            "Herkimer diamonds are a naturally double-terminated, exceptionally clear form of quartz, often described by practitioners as one of the most powerful amplifiers in the quartz family.",
        ],
        "body": [
            ("h2", "What Makes It Special"),
            ("p", "They are associated with spiritual growth and deep clarity, and are said to be easy to &ldquo;program&rdquo; with a specific intention, which makes them a favourite for meditation and energy work."),
            ("h2", "Why It Makes a Good Gift"),
            ("p", "A step up from a basic tumbled stone, ideal for someone further along in their crystal or meditation practice."),
        ],
        "faq": [
            ("What makes a Herkimer diamond different from regular quartz?", "Herkimer diamonds are a naturally double-terminated, unusually clear variety of quartz, prized for their clarity and believed to carry an especially high vibrational energy."),
            ("Who is a Herkimer diamond a good gift for?", "Someone already familiar with crystals or meditation, since it is considered a more advanced stone than a basic tumbled piece."),
            ("How do I use a Herkimer diamond?", "Common uses include holding it during meditation, placing it on an altar, or programming it by holding it while focusing on a specific intention."),
            ("Where can I find one in North Vancouver?", "Utopia Wellness & Gifts on Lonsdale Ave carries a rotating selection in store."),
        ],
        "keywords": "quartz crystals, crystal gifts, metaphysical store North Vancouver",
    },
    {
        "slug": "clear-quartz-master-healer-gift",
        "title": "Clear Quartz: The Master Healer Gift That Works for Anyone",
        "breadcrumb": "Clear Quartz Gift",
        "category": "CRYSTALS",
        "meta": "Clear quartz is the safest, most versatile crystal gift. Why it is called the master healer, what forms it comes in, and where to find it, from Utopia in North Vancouver.",
        "intro": [
            "If you are not sure what crystal to give someone, clear quartz is the safest and most versatile choice in the store, which is exactly why Utopia Wellness &amp; Gifts on Lonsdale Ave keeps it stocked in nearly every form, from tumbled stones to jewellery to larger display pieces.",
            "Clear quartz is known as the master healer because it is believed to amplify the energy and intention of anything near it, including other crystals.",
        ],
        "body": [
            ("h2", "What Clear Quartz Is Associated With"),
            ("p", "It is associated with clarity, focus, and balance, and is said to work with every chakra rather than just one, which is why it suits almost any gifting occasion."),
            ("h2", "Why It Makes a Good Gift"),
            ("p", "A no-fail option when you are unsure of someone's specific taste or needs, it works well alone or paired with another stone. Come browse our clear quartz selection on Lonsdale Ave; we can help you pick a piece or shape that fits your gift budget."),
        ],
        "faq": [
            ("Why is clear quartz called the master healer?", "It is believed to amplify energy and intention, including the energy of other crystals placed near it, and is said to work with every chakra."),
            ("Is clear quartz a good gift if I don't know the person's specific interests?", "Yes, it is considered one of the safest, most universal crystal gifts for exactly that reason."),
            ("What forms does clear quartz come in?", "Tumbled stones, points, jewellery, and larger decorative pieces like towers and clusters."),
            ("Where can I buy clear quartz in North Vancouver?", "Utopia Wellness & Gifts, 1826 Lonsdale Ave, carries clear quartz in multiple forms and price points."),
        ],
        "keywords": "clear quartz meaning, crystal gifts, master healer crystal, crystal shop Vancouver",
    },
    {
        "slug": "smoky-quartz-grounding-gift",
        "title": "Smoky Quartz: A Grounding Gift for Anyone Feeling Overwhelmed",
        "breadcrumb": "Smoky Quartz Gift",
        "category": "CRYSTALS",
        "meta": "Smoky quartz is a gentle grounding gift for someone anxious or overworked. What it is good for and how it differs from clear quartz, from Utopia in North Vancouver.",
        "intro": [
            "For a friend who has been anxious, overworked, or just needs to feel steadier, smoky quartz is a gentle, grounding gift available at Utopia Wellness &amp; Gifts on Lonsdale Ave.",
            "This grey-to-brown variety of quartz is associated with grounding, emotional protection, and clarity of intention, and is often chosen by people navigating stress or a big transition.",
        ],
        "body": [
            ("h2", "Who It Suits"),
            ("p", "It is a popular choice for those working on breaking old habits or simply looking to feel more settled day to day."),
            ("h2", "Why It Makes a Good Gift"),
            ("p", "Approachable, with a calming meaning, it works well as jewellery for everyday wear."),
        ],
        "faq": [
            ("What is smoky quartz good for?", "It is traditionally associated with grounding, emotional protection, and clarity, often chosen for stressful periods or big transitions."),
            ("Is smoky quartz a good everyday jewellery gift?", "Yes, many people choose smoky quartz bracelets or pendants specifically so they can carry its grounding energy throughout the day."),
            ("How is smoky quartz different from clear quartz?", "Smoky quartz gets its grey-brown colour from natural irradiation and is associated more specifically with grounding, while clear quartz is considered a more general, all-purpose amplifier."),
            ("Where can I find smoky quartz gifts in North Vancouver?", "Utopia Wellness & Gifts on Lonsdale Ave carries smoky quartz in jewellery and loose stone form."),
        ],
        "keywords": "grounding crystals, smoky quartz meaning, crystal jewelry North Vancouver",
    },
    {
        "slug": "citrine-gift-confidence-fresh-starts",
        "title": "Citrine: A Golden Gift for Confidence and Fresh Starts",
        "breadcrumb": "Citrine Gift",
        "category": "CRYSTALS",
        "meta": "Citrine is a bright, uplifting gift for someone starting something new. What it symbolises and why it suits new jobs and milestones, from Utopia in North Vancouver.",
        "intro": [
            "Citrine is one of our most popular gifts for someone starting something new &mdash; a job, a business, a fresh chapter &mdash; available at Utopia Wellness &amp; Gifts on Lonsdale Ave in tumbled stones, jewellery, and raw points.",
            "This golden quartz is associated with confidence, creativity, and prosperity, and its sunny colour makes it an easy, upbeat gift to hand someone.",
        ],
        "body": [
            ("h2", "How People Use It"),
            ("p", "It is often placed near workspaces or carried during big decisions as a reminder of self-trust and positivity."),
            ("h2", "Why It Makes a Good Gift"),
            ("p", "Bright, optimistic meaning that suits career milestones, graduations, and new ventures particularly well."),
        ],
        "faq": [
            ("What does citrine symbolise?", "Confidence, creativity, and prosperity, which is why it is a popular gift for new jobs, businesses, and fresh starts."),
            ("Is citrine a good gift for a graduation or new job?", "Yes, its association with confidence and manifestation makes it a popular choice for exactly these occasions."),
            ("What forms does citrine come in?", "Tumbled stones, jewellery, and raw points are all available."),
            ("Where can I buy citrine in North Vancouver?", "Utopia Wellness & Gifts, 1826 Lonsdale Ave, carries citrine year-round."),
        ],
        "keywords": "citrine meaning, crystals for confidence, crystal gifts North Vancouver",
    },
    {
        "slug": "pink-tourmaline-gentle-gift-heart",
        "title": "Pink Tourmaline: A Gentle Gift for the Heart",
        "breadcrumb": "Pink Tourmaline Gift",
        "category": "CRYSTALS",
        "meta": "Pink tourmaline is a gentle, nurturing stone for emotional comfort. What it is associated with and why it suits sympathy gifts, from Utopia in North Vancouver.",
        "intro": [
            "For a gift centred on emotional comfort, pink tourmaline is one of the gentler, more nurturing stones carried at Utopia Wellness &amp; Gifts on Lonsdale Ave.",
            "Also called ruby tourmaline, this gem is associated with the heart chakra and is traditionally given as a gift for emotional healing, comfort during a hard stretch, or to mark the bond between a parent and child.",
        ],
        "body": [
            ("h2", "A Soft Choice for Jewellery"),
            ("p", "Its soft pink tones make it a popular choice for jewellery."),
            ("h2", "Why It Makes a Good Gift"),
            ("p", "Appropriate for both romantic and platonic relationships, it works well as a comfort or sympathy gift."),
        ],
        "faq": [
            ("What is pink tourmaline associated with?", "Emotional healing, comfort, and the heart chakra."),
            ("Is pink tourmaline a good gift for a difficult time?", "Yes, its gentle, comforting meaning makes it a popular choice for sympathy or thinking-of-you gifts."),
            ("Can pink tourmaline be worn as jewellery?", "Yes, it is commonly set into rings, pendants, and earrings."),
            ("Where can I buy pink tourmaline in North Vancouver?", "Utopia Wellness & Gifts on Lonsdale Ave carries pink tourmaline jewellery and loose stones."),
        ],
        "keywords": "heart chakra stones, crystals for comfort, pink tourmaline meaning",
    },
    {
        "slug": "rose-quartz-love-stone-gift",
        "title": "Rose Quartz: The Love Stone, Always a Safe Gift",
        "breadcrumb": "Rose Quartz Gift",
        "category": "CRYSTALS",
        "meta": "Rose quartz is the love stone and one of the safest crystal gifts for anyone. What it symbolises and the occasions it suits, from Utopia in North Vancouver.",
        "intro": [
            "If there is one crystal nearly everyone recognises, it is rose quartz, and Utopia Wellness &amp; Gifts on Lonsdale Ave keeps it in stock in more forms than almost any other stone in the shop.",
            "Rose quartz is known as the stone of unconditional love, associated with self-love, emotional healing, and harmonious relationships.",
        ],
        "body": [
            ("h2", "Who It Suits"),
            ("p", "It is a go-to gift for partners, friends, mothers, and anyone going through a season that calls for a little extra gentleness."),
            ("h2", "Why It Makes a Good Gift"),
            ("p", "A universally recognised meaning that suits romantic gifts, Mother's Day, sympathy gifts, and self-care gifts equally well."),
        ],
        "faq": [
            ("What does rose quartz symbolise?", "Unconditional love, self-love, and emotional healing."),
            ("Is rose quartz a good gift for a romantic partner?", "Yes, it is one of the most popular romantic gift stones for exactly this reason."),
            ("Can rose quartz be used for self-care gifts too?", "Yes, many people give it as a self-love or comfort gift, not only a romantic one."),
            ("Where can I buy rose quartz in North Vancouver?", "Utopia Wellness & Gifts, 1826 Lonsdale Ave, carries rose quartz jewellery, tumbled stones, and larger pieces."),
        ],
        "keywords": "rose quartz meaning, love stone, crystal gifts for her, jewelry gifts North Vancouver",
    },
    {
        "slug": "amazonite-calming-gift-communication",
        "title": "Amazonite: A Calming Gift for Communication and Balance",
        "breadcrumb": "Amazonite Gift",
        "category": "CRYSTALS",
        "meta": "Amazonite is a soothing green stone for communication and calm. What it is associated with and why it suits anxious or overworked people, from Utopia in North Vancouver.",
        "intro": [
            "For someone who needs a little more calm in their life, or who struggles to speak their mind, amazonite is a soothing green gift available at Utopia Wellness &amp; Gifts on Lonsdale Ave.",
            "This gemstone is linked to the heart and throat chakras, associated with open communication, emotional balance, and a calming effect on anxious thoughts.",
        ],
        "body": [
            ("h2", "How People Wear It"),
            ("p", "Many people wear it as jewellery to keep its steady, grounding energy close throughout the day."),
            ("h2", "Why It Makes a Good Gift"),
            ("p", "A good pick for someone feeling anxious, overworked, or navigating a hard conversation."),
        ],
        "faq": [
            ("What is amazonite associated with?", "Communication, calm, and emotional balance, linked to the heart and throat chakras."),
            ("Is amazonite a good gift for someone who is anxious?", "Yes, its calming associations make it a popular gift for stress or anxiety."),
            ("What forms does amazonite come in?", "Jewellery, tumbled stones, and larger palm stones or spheres."),
            ("Where can I buy amazonite in North Vancouver?", "Utopia Wellness & Gifts on Lonsdale Ave carries amazonite in jewellery and loose stone form."),
        ],
        "keywords": "calming crystals, amazonite meaning, crystals for anxiety",
    },
    {
        "slug": "labradorite-gift-dreamer-deep-thinker",
        "title": "Labradorite: A Gift for the Dreamer and the Deep Thinker",
        "breadcrumb": "Labradorite Gift",
        "category": "CRYSTALS",
        "meta": "Labradorite is a mesmerising stone of intuition and insight, with flashes of blue and green. What its colour-shift means and who it suits, from Utopia in North Vancouver.",
        "intro": [
            "For the friend who is always asking big questions, labradorite is one of the more mesmerising gifts at Utopia Wellness &amp; Gifts on Lonsdale Ave, known for its flashes of blue and green within a grey stone.",
            "Labradorite is associated with intuition, spiritual insight, and protection, often linked to the third eye chakra.",
        ],
        "body": [
            ("h2", "That Shifting Colour"),
            ("p", "Its shifting colour, called labradorescence, makes it a visually striking gift on its own, even before getting into the meaning behind it."),
            ("h2", "Why It Makes a Good Gift"),
            ("p", "A conversation piece as much as a meaningful one, suited to anyone drawn to intuition, meditation, or simply beautiful stones."),
        ],
        "faq": [
            ("What does labradorite's colour-shifting effect mean?", "The effect is called labradorescence, a natural optical phenomenon, and it is part of why the stone is so prized visually."),
            ("What is labradorite associated with?", "Intuition, spiritual insight, and protection."),
            ("Is labradorite a good beginner gift?", "Yes, its striking appearance makes it approachable even for someone new to crystals."),
            ("Where can I buy labradorite in North Vancouver?", "Utopia Wellness & Gifts on Lonsdale Ave carries labradorite jewellery and specimens."),
        ],
        "keywords": "labradorite meaning, intuition crystals, crystal shop North Vancouver",
    },
    {
        "slug": "amethyst-timeless-gift",
        "title": "Amethyst: A Timeless, Always-Right Gift",
        "breadcrumb": "Amethyst Gift",
        "category": "CRYSTALS",
        "meta": "Amethyst is a timeless crystal gift that suits almost any occasion. What it is known for and the forms it comes in, from Utopia Wellness & Gifts in North Vancouver.",
        "intro": [
            "If you want a gift that is never wrong, amethyst is likely it. Utopia Wellness &amp; Gifts on Lonsdale Ave carries amethyst in nearly every form &mdash; tumbled stones, bracelets, towers, and cathedral pieces &mdash; making it easy to find one that fits any budget.",
            "Amethyst belongs to the quartz family and has been treasured for centuries for its calming, protective qualities.",
        ],
        "body": [
            ("h2", "What Amethyst Is Known For"),
            ("p", "It is associated with stress relief, spiritual growth, and a sense of balance, and its deep purple colour makes it an easy, elegant gift for almost anyone."),
            ("h2", "Why It Makes a Good Gift"),
            ("p", "A wide range of price points means it suits nearly every occasion, from a small thank-you gift to a large statement piece."),
        ],
        "faq": [
            ("What is amethyst known for?", "Calming energy, stress relief, and spiritual growth; it belongs to the quartz family."),
            ("Is amethyst an appropriate gift for any occasion?", "Yes, it is one of the most universally appropriate crystal gifts, suiting birthdays, sympathy gifts, and housewarmings alike."),
            ("What forms does amethyst come in?", "Tumbled stones, jewellery, towers, and larger decorative clusters or cathedrals."),
            ("Where can I buy amethyst in North Vancouver?", "Utopia Wellness & Gifts, 1826 Lonsdale Ave, carries a full range of amethyst pieces."),
        ],
        "keywords": "amethyst meaning, crystal gifts North Vancouver, calming crystals",
    },
    {
        "slug": "tigers-eye-confidence-gift",
        "title": "Tiger's Eye: A Confidence-Boosting Gift",
        "breadcrumb": "Tiger's Eye Gift",
        "category": "CRYSTALS",
        "meta": "Tiger's eye is the stone of confidence, a grounding gift for new jobs and big decisions. What it is associated with and who it suits, from Utopia in North Vancouver.",
        "intro": [
            "For someone who needs a push of courage &mdash; maybe starting a new job, facing a hard decision, or simply needing to back themselves more &mdash; tiger's eye is a grounding, confidence-focused gift from Utopia Wellness &amp; Gifts on Lonsdale Ave.",
            "This golden-brown quartz is known as the stone of confidence, associated with grounding, protection, and self-empowerment.",
        ],
        "body": [
            ("h2", "Focus and Clarity"),
            ("p", "It is also linked to focus and mental clarity, making it a popular gift for students or anyone navigating a demanding stretch of work."),
            ("h2", "Why It Makes a Good Gift"),
            ("p", "A motivating, practical meaning that suits career milestones, exams, and new beginnings."),
        ],
        "faq": [
            ("Why is tiger's eye called the stone of confidence?", "It is traditionally associated with self-empowerment, courage, and overcoming self-doubt."),
            ("Is tiger's eye a good gift for a student or someone starting a new job?", "Yes, its associations with focus and confidence make it a popular choice for exactly these moments."),
            ("What forms does tiger's eye come in?", "Jewellery, tumbled stones, and palm stones."),
            ("Where can I buy tiger's eye in North Vancouver?", "Utopia Wellness & Gifts on Lonsdale Ave carries tiger's eye in store."),
        ],
        "keywords": "tiger's eye meaning, confidence crystals, crystal gifts for him",
    },
    {
        "slug": "carnelian-gift-energy-motivation",
        "title": "Carnelian: A Gift of Energy and Motivation",
        "breadcrumb": "Carnelian Gift",
        "category": "CRYSTALS",
        "meta": "Carnelian is a vibrant, energising stone for courage and creativity. What it is associated with and who it suits as a gift, from Utopia Wellness & Gifts in North Vancouver.",
        "intro": [
            "If someone in your life is low on motivation or just needs a little more fire, carnelian is a vibrant, energising gift available at Utopia Wellness &amp; Gifts on Lonsdale Ave.",
            "This orange-red stone has been treasured since ancient Egypt, associated with courage, vitality, and creative motivation.",
        ],
        "body": [
            ("h2", "Who It Suits"),
            ("p", "It is often chosen by people starting a new creative project or simply needing an extra boost of energy and confidence."),
            ("h2", "Why It Makes a Good Gift"),
            ("p", "An energising, warm-toned stone, good for creative friends, athletes, or anyone pushing toward a goal."),
        ],
        "faq": [
            ("What is carnelian associated with?", "Courage, vitality, and creative motivation."),
            ("Is carnelian a good gift for a creative friend?", "Yes, it is a popular choice specifically for stimulating creativity and motivation."),
            ("What forms does carnelian come in?", "Jewellery, tumbled stones, and raw pieces."),
            ("Where can I buy carnelian in North Vancouver?", "Utopia Wellness & Gifts, 1826 Lonsdale Ave, carries carnelian in jewellery and loose stone form."),
        ],
        "keywords": "carnelian meaning, crystals for motivation, crystal gifts North Vancouver",
    },
    {
        "slug": "sunstone-gift-warmth-vitality",
        "title": "Sunstone: A Gift of Warmth and Vitality",
        "breadcrumb": "Sunstone Gift",
        "category": "CRYSTALS",
        "meta": "Sunstone is a warm, glittering stone of optimism and vitality. What it is known for and how to care for it, from Utopia Wellness & Gifts in North Vancouver.",
        "intro": [
            "For a gift that feels like a little bit of sunshine, sunstone is a warm, glittering choice available at Utopia Wellness &amp; Gifts on Lonsdale Ave.",
            "This feldspar gem gets its sparkle from natural copper inclusions, and is associated with vitality, optimism, and self-empowerment.",
        ],
        "body": [
            ("h2", "A Mood Lift"),
            ("p", "It is often linked to the solar plexus chakra and chosen as a gift for someone who needs a mood lift or a reminder of their own inner strength."),
            ("h2", "Why It Makes a Good Gift"),
            ("p", "A bright, uplifting meaning, visually striking even as a simple pendant or tumbled stone."),
        ],
        "faq": [
            ("What is sunstone known for?", "Vitality, optimism, and self-empowerment, linked to the solar plexus chakra."),
            ("Is sunstone a good gift for someone going through a hard season?", "Yes, its associations with optimism and inner strength make it a popular mood-lifting gift."),
            ("How should I care for sunstone jewellery?", "Clean with warm soapy water and a soft cloth, and avoid harsh chemicals or prolonged sun exposure."),
            ("Where can I buy sunstone in North Vancouver?", "Utopia Wellness & Gifts on Lonsdale Ave carries sunstone jewellery and loose stones."),
        ],
        "keywords": "sunstone meaning, crystals for positivity, crystal gifts North Vancouver",
    },
    {
        "slug": "ultimate-metaphysical-gift-guide",
        "title": "The Ultimate Metaphysical Gift Guide, From Utopia Wellness &amp; Gifts",
        "breadcrumb": "Metaphysical Gift Guide",
        "category": "GIFTS",
        "meta": "A metaphysical gift guide beyond candles and gift cards: crystals, meditation essentials, tarot decks, sacred jewellery, and gift cards, from Utopia in North Vancouver.",
        "intro": [
            "Looking for a spiritual or metaphysical gift that goes beyond the usual candle or gift card? Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver, puts together exactly this kind of gift year-round, not just for the holidays.",
        ],
        "body": [
            ("h2", "Where to Start"),
            ("ul", [
                "<strong>Crystals:</strong> start with a stone matched to the person &mdash; amethyst for calm, rose quartz for love, citrine for confidence &mdash; and build from there.",
                "<strong>Meditation essentials:</strong> a comfortable cushion, a calming candle, or a small singing bowl supports a peaceful daily practice.",
                "<strong>Tarot and oracle decks:</strong> a beautifully illustrated deck, paired with a simple guidebook, is a favourite gift for anyone curious about self-reflection.",
                "<strong>Sacred jewellery:</strong> pendants, bracelets, and mala beads carrying real gemstone meaning make a gift that is worn, not just displayed.",
                "<strong>Gift cards:</strong> when you are not sure exactly what to choose, a Utopia gift card lets the recipient pick their own piece in store.",
            ]),
            ("p", "Every item above can be wrapped on the spot at Utopia Wellness &amp; Gifts, so you can shop and go the same day."),
        ],
        "faq": [
            ("What makes a good metaphysical gift?", "Something matched to the person's intentions or current season of life works best &mdash; a calming crystal for someone stressed, a confidence stone for someone starting fresh, or an oracle deck for someone curious about reflection."),
            ("Do you offer gift wrapping?", "Yes, every purchase can be wrapped at checkout."),
            ("Can I get a gift card if I'm not sure what to choose?", "Yes, Utopia gift cards are available in store and let the recipient choose their own piece."),
            ("Where is Utopia Wellness & Gifts located?", "1826 Lonsdale Ave, North Vancouver, BC V7M 2J9, with free parking at the back."),
        ],
        "keywords": "best gift shop North Vancouver, unique gifts North Vancouver, metaphysical gift guide, crystal gifts",
    },
    {
        "slug": "gemstones-to-honor-your-mom",
        "title": "5 Meaningful Gemstones to Honor Your Mom",
        "breadcrumb": "Gemstones for Mom",
        "category": "GIFTS",
        "meta": "Five meaningful gemstones for Mother's Day: moonstone, pink tourmaline, chrysoprase, ruby zoisite, and malachite. A jewellery gift guide from Utopia in North Vancouver.",
        "intro": [
            "Jewellery remains one of the most popular Mother's Day gifts, since it serves as a lasting, visible reminder of love, and Utopia Wellness &amp; Gifts on Lonsdale Ave carries each of these five gemstones in jewellery form.",
        ],
        "body": [
            ("h2", "Five Gemstones for Mom"),
            ("ul", [
                "<strong>Moonstone:</strong> a bluish-white stone connected to feminine, nurturing energy and the moon, often chosen for its calming, protective associations for mothers and children.",
                "<strong>Pink tourmaline:</strong> representing unconditional love and understanding, this gem connects to the heart chakra and suits a mom who could use a little extra comfort.",
                "<strong>Chrysoprase:</strong> sometimes called the Stone of Venus, this soothing green gem is associated with balance, kindness, and self-esteem.",
                "<strong>Ruby zoisite:</strong> a bold green-and-red combination stone, associated with growth and vitality, connecting the heart and third eye.",
                "<strong>Malachite:</strong> a deep green stone historically associated with healing and protection, said to help release old patterns and encourage courage.",
            ]),
            ("p", "Come into Utopia Wellness &amp; Gifts on Lonsdale Ave to see each of these in person. We can help you choose a piece and have it wrapped before you leave."),
        ],
        "faq": [
            ("What is the most popular Mother's Day gemstone?", "Moonstone and rose quartz are consistently among the most requested, though the best choice really depends on what feels right for your mom."),
            ("Can I get Mother's Day jewellery wrapped in store?", "Yes, gift wrapping is available at checkout."),
            ("Do you carry rings, bracelets, and necklaces for Mother's Day?", "Yes, all three are available across these gemstones in store."),
            ("Where can I buy Mother's Day jewellery in North Vancouver?", "Utopia Wellness & Gifts, 1826 Lonsdale Ave, carries gemstone jewellery suited to Mother's Day year-round."),
        ],
        "keywords": "Mother's Day gifts North Vancouver, jewelry gifts North Vancouver, gifts for mom",
    },
    {
        "slug": "crystal-healing-bracelets-gift-guide",
        "title": "Crystal Healing Bracelets: Everything to Know Before You Gift One",
        "breadcrumb": "Crystal Bracelets Gift",
        "category": "GIFTS",
        "meta": "A guide to gifting crystal healing bracelets: how to choose by meaning, how to cleanse them, and why they are a safe gift, from Utopia Wellness & Gifts in North Vancouver.",
        "intro": [
            "A crystal bracelet is one of the easiest &ldquo;sure thing&rdquo; gifts in the shop, since nearly everyone can wear one home the same day. Utopia Wellness &amp; Gifts on Lonsdale Ave keeps dozens of styles in stock, from single-stone pieces to mixed designs.",
            "Each gemstone carries its own meaning &mdash; amethyst for calm, rose quartz for love, citrine for confidence, clear quartz as an all-purpose amplifier &mdash; so choosing a bracelet is really about matching the stone to the person.",
        ],
        "body": [
            ("h2", "Why They Work So Well"),
            ("p", "Worn on the wrist, the bracelet keeps that stone's energy in regular contact with the body throughout the day. It is affordable, wearable, and easy to match to someone's personality or current season of life, without needing to know their exact style preferences."),
        ],
        "faq": [
            ("How do I choose a crystal bracelet as a gift?", "Match the stone's meaning to the person or occasion &mdash; calming stones for someone stressed, confidence stones for a new job, love stones for a partner."),
            ("Do crystal bracelets need to be cleansed regularly?", "Yes, most people cleanse them periodically with water if safe for the stone, sage smoke, or moonlight to keep their energy fresh."),
            ("Are crystal bracelets a good gift if I don't know someone's exact style?", "Yes, their simple, wearable design makes them a safe choice across most styles and ages."),
            ("Where can I buy crystal bracelets in North Vancouver?", "Utopia Wellness & Gifts on Lonsdale Ave carries a wide selection in store."),
        ],
        "keywords": "crystal bracelets, jewelry gifts North Vancouver, crystal gifts for her",
    },
    {
        "slug": "healing-crystals-for-men",
        "title": "Our Top 9 Healing Crystals for Men",
        "breadcrumb": "Crystals for Men",
        "category": "CRYSTALS",
        "meta": "Nine healing crystals that make great gifts for men: onyx, hematite, tiger's eye, quartz, pyrite, lapis, red jasper, carnelian, and selenite, from Utopia in North Vancouver.",
        "intro": [
            "Shopping for a gift for the man in your life can be tricky, but crystals are a genuinely good option once you know where to start. Utopia Wellness &amp; Gifts on Lonsdale Ave carries each of these nine stones, commonly chosen as gifts for men.",
        ],
        "body": [
            ("h2", "Nine Crystals to Consider"),
            ("ul", [
                "<strong>Black onyx:</strong> grounding and protective, helps with focus and confidence.",
                "<strong>Hematite:</strong> grounding and strengthening, good for staying balanced under pressure.",
                "<strong>Tiger's eye:</strong> courage and personal power, popular for career milestones.",
                "<strong>Clear quartz:</strong> an all-purpose amplifier, good for focus and clarity.",
                "<strong>Pyrite:</strong> associated with abundance and success, a popular good-luck gift.",
                "<strong>Lapis lazuli:</strong> wisdom and self-awareness, a favourite for deep thinkers.",
                "<strong>Red jasper:</strong> stability and endurance, popular with active or athletic men.",
                "<strong>Carnelian:</strong> motivation and vitality, good for creative or driven personalities.",
                "<strong>Selenite:</strong> clarity and calm, a gentler pick for quieting a busy mind.",
            ]),
            ("p", "Each has a clear, easy-to-explain meaning that suits common gifting occasions: a new job, a tough season, a milestone birthday."),
        ],
        "faq": [
            ("What is a good first crystal gift for a man who has never used crystals?", "Black onyx or tiger's eye are popular starting points, since both have straightforward, practical associations of grounding and confidence."),
            ("Can these crystals be worn as jewellery?", "Yes, most are available as bracelets, pendants, or rings in store."),
            ("Do you sell these as a set?", "Ask in store about building a custom set across a few of these stones for one gift."),
            ("Where can I buy these in North Vancouver?", "Utopia Wellness & Gifts, 1826 Lonsdale Ave, carries all nine in store."),
        ],
        "keywords": "crystals for men, gifts for him, crystal gifts North Vancouver",
    },
    {
        "slug": "healing-crystals-for-beginners",
        "title": "Our Top 10 Healing Crystals for Beginners",
        "breadcrumb": "Crystals for Beginners",
        "category": "CRYSTALS",
        "meta": "Ten approachable crystals for beginners: clear quartz, amethyst, rose quartz, citrine, black tourmaline, selenite, carnelian, labradorite, aventurine, and lepidolite, from Utopia.",
        "intro": [
            "If you are shopping for someone just getting curious about crystals, or starting your own collection yourself, these ten stones are the most approachable place to begin, all available at Utopia Wellness &amp; Gifts on Lonsdale Ave.",
        ],
        "body": [
            ("h2", "Ten Beginner Crystals"),
            ("ul", [
                "<strong>Clear quartz:</strong> the master healer, amplifies energy and works with any intention.",
                "<strong>Amethyst:</strong> calming, supports sleep and stress relief.",
                "<strong>Rose quartz:</strong> the stone of love, self-acceptance, and emotional healing.",
                "<strong>Citrine:</strong> abundance, confidence, and motivation.",
                "<strong>Black tourmaline:</strong> grounding and protective.",
                "<strong>Selenite:</strong> calming and purifying, also used to cleanse other crystals.",
                "<strong>Carnelian:</strong> vibrant, energising, good for creativity.",
                "<strong>Labradorite:</strong> intuitive and protective, visually striking.",
                "<strong>Aventurine:</strong> associated with luck and opportunity.",
                "<strong>Lepidolite:</strong> calming, linked to the crown chakra, good for stress relief.",
            ]),
            ("p", "A well-rounded starter set covers multiple needs, so the recipient can see which stone they are drawn to first."),
        ],
        "faq": [
            ("What is the best first crystal to buy or gift?", "Clear quartz is the most common recommendation, since it is considered a safe, all-purpose stone."),
            ("Can I build a custom beginner gift set from this list?", "Yes, ask in store and we can help you put together a few stones as one gift."),
            ("Do beginner crystals need special care?", "Basic cleansing &mdash; water if safe, sage smoke, or moonlight &mdash; every so often is enough to start."),
            ("Where can I buy beginner crystals in North Vancouver?", "Utopia Wellness & Gifts, 1826 Lonsdale Ave, carries all ten in store."),
        ],
        "keywords": "crystals for beginners, crystal starter set, crystal gifts North Vancouver",
    },
    {
        "slug": "candles-as-a-ritual-gift",
        "title": "The Power of Candles as a Ritual Gift",
        "breadcrumb": "Candles as a Gift",
        "category": "GIFTS",
        "meta": "Candles make a universally loved ritual gift. What candle colours mean and how to pair them with a crystal, from Utopia Wellness & Gifts in North Vancouver.",
        "intro": [
            "A good candle is one of the most universally appreciated gifts, and at Utopia Wellness &amp; Gifts on Lonsdale Ave, we choose ours with ritual and intention in mind, not just scent.",
            "Candles have played a role in spiritual practice for thousands of years, used in meditation, prayer, and simple at-home rituals.",
        ],
        "body": [
            ("h2", "What Candle Colours Mean"),
            ("p", "Colour carries its own meaning in many traditions: white for purity and new beginnings, green for abundance, blue for calm and intuition, purple for spiritual connection. Choosing a candle colour that matches the occasion adds a small, thoughtful layer to an easy gift."),
            ("h2", "Why It Makes a Good Gift"),
            ("p", "Affordable, low-pressure, and it pairs naturally with a crystal for a slightly bigger gift set."),
        ],
        "faq": [
            ("What do different candle colours mean?", "White is associated with purity and new beginnings, green with abundance, blue with calm, and purple with spiritual connection, though meanings vary by tradition."),
            ("Is a candle a good stand-alone gift?", "Yes, though it also pairs well with a small crystal for a slightly more complete gift set."),
            ("Do you sell candle and crystal gift sets?", "Ask in store &mdash; we can help put together a simple candle-and-crystal pairing for any occasion."),
            ("Where can I buy ritual candles in North Vancouver?", "Utopia Wellness & Gifts, 1826 Lonsdale Ave, carries a rotating candle selection in store."),
        ],
        "keywords": "ritual candles, candle gifts North Vancouver, intention candles",
    },
    {
        "slug": "best-crystals-and-gifts-for-a-leo",
        "title": "Best Crystals and Gifts for a Leo (July 23 to August 22)",
        "breadcrumb": "Crystals for a Leo",
        "category": "ASTROLOGY",
        "meta": "The best crystals for a Leo: citrine, carnelian, sunstone, ruby, and labradorite. A zodiac-matched gift guide from Utopia Wellness & Gifts in North Vancouver.",
        "intro": [
            "Shopping for the confident, warm, larger-than-life Leo in your life? Utopia Wellness &amp; Gifts on Lonsdale Ave carries each of these Leo-aligned crystals in store, a fun, easy way to choose a gift matched to someone's sign.",
            "Leo is a fire sign known for charisma, creativity, and natural leadership. A few crystals are traditionally associated with this energy.",
        ],
        "body": [
            ("h2", "Crystals for Leo"),
            ("ul", [
                "<strong>Citrine:</strong> matches Leo's radiant, confident energy, supports manifestation and joy.",
                "<strong>Carnelian:</strong> fuels Leo's passionate, creative spirit.",
                "<strong>Sunstone:</strong> a natural match since Leo is ruled by the sun, boosts warmth and self-expression.",
                "<strong>Ruby:</strong> regal and bold, associated with passion and courage.",
                "<strong>Labradorite:</strong> enhances charisma and intuition, with a layer of protection.",
            ]),
            ("p", "Zodiac-matched gifts feel personal without requiring deep crystal knowledge &mdash; just know their sign."),
        ],
        "faq": [
            ("What crystal is best for a Leo?", "Citrine and sunstone are two of the most commonly recommended, both tied to Leo's sun-ruled, confident energy."),
            ("Is a zodiac-matched crystal a good birthday gift?", "Yes, it is a popular, easy way to personalise a gift without needing to know someone's specific taste."),
            ("Do you carry zodiac crystal sets?", "Ask in store &mdash; we can help build a small set matched to any sign."),
            ("Where can I buy Leo crystals in North Vancouver?", "Utopia Wellness & Gifts, 1826 Lonsdale Ave, carries all five in store."),
        ],
        "keywords": "crystals for Leo, zodiac gifts, birthday gifts North Vancouver",
    },
    {
        "slug": "best-crystals-and-gifts-for-a-cancer",
        "title": "Best Crystals and Gifts for a Cancer (June 21 to July 22)",
        "breadcrumb": "Crystals for a Cancer",
        "category": "ASTROLOGY",
        "meta": "The best crystals for a Cancer: moonstone, rose quartz, carnelian, emerald, and aquamarine. A zodiac-matched gift guide from Utopia Wellness & Gifts in North Vancouver.",
        "intro": [
            "For the nurturing, intuitive Cancer in your life, Utopia Wellness &amp; Gifts on Lonsdale Ave carries a set of crystals traditionally matched to this water sign's emotional depth and caring nature.",
        ],
        "body": [
            ("h2", "Crystals for Cancer"),
            ("ul", [
                "<strong>Moonstone:</strong> a natural match since Cancer is ruled by the moon, supports intuition and emotional balance.",
                "<strong>Rose quartz:</strong> deepens Cancer's already tender, loving nature.",
                "<strong>Carnelian:</strong> sparks creativity and confidence.",
                "<strong>Emerald:</strong> associated with healing and abundance, supports emotional release.",
                "<strong>Aquamarine:</strong> calming, supports clear communication during emotional moments.",
            ]),
            ("p", "Like the Leo set, a zodiac-matched gift is an easy, personal choice that works well for birthdays or just-because moments."),
        ],
        "faq": [
            ("What crystal is best for a Cancer?", "Moonstone is the most commonly recommended, since Cancer is ruled by the moon."),
            ("Is a zodiac crystal gift appropriate for any age?", "Yes, it works well across ages, from a teenager curious about their sign to an adult who already follows astrology."),
            ("Can I combine a zodiac crystal with jewellery?", "Yes, many of these stones are available as bracelets or pendants in store."),
            ("Where can I buy Cancer crystals in North Vancouver?", "Utopia Wellness & Gifts, 1826 Lonsdale Ave, carries all five in store."),
        ],
        "keywords": "crystals for Cancer, zodiac gifts, crystal gifts North Vancouver",
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
        print(f"wrote {post['slug']}.html  [{post['category']}]")


if __name__ == "__main__":
    main()
