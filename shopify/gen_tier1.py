"""
TIER 1 pillar blog posts. Generate from blog/TEMPLATE.html.
Run:  python shopify/gen_tier1.py
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
        "slug": "what-is-a-venus-sign",
        "title": "What Is a Venus Sign? What It Says About Love and Attraction",
        "breadcrumb": "What Is a Venus Sign",
        "category": "ASTROLOGY",
        "meta": "What is a Venus sign? It shows how you love, flirt, and what you value in relationships. Learn how to find your Venus sign and what each one means at Utopia, North Vancouver.",
        "intro": [
            "Your Venus sign is the zodiac sign Venus was travelling through at the moment you were born, and it describes how you love, what you find attractive, and what makes you feel valued in a relationship. While your Sun sign is your core identity, your Venus sign is the more specific story of your romantic and aesthetic self &mdash; the way you flirt, bond, spend, and want to be treated.",
            "If you have ever felt that your Sun sign does not quite capture how you act in love, your Venus sign is usually the missing piece. It is one of the first placements our readers look at in a birth chart love reading.",
        ],
        "body": [
            ("h2", "How to Find Your Venus Sign"),
            ("p", "Venus moves quickly, so its sign is tied to your exact birth date and often your birth year. To find yours, enter your birth date into any free birth chart calculator, or bring your birth date (and time, if you have it) to a reading. Venus is usually within one or two signs of your Sun, which is why it can feel familiar yet distinct."),
            ("h2", "What Your Venus Sign Reveals"),
            ("p", "Venus governs three related things: how you give and receive affection, what you are drawn to in a partner, and how you relate to beauty, comfort, and money. Read together, these describe your love language long before the term existed."),
            ("h2", "Venus Through the Signs"),
            ("ul", [
                "<strong>Venus in Aries:</strong> direct, passionate, drawn to the chase and to confidence.",
                "<strong>Venus in Taurus:</strong> sensual and loyal, values steadiness, touch, and comfort.",
                "<strong>Venus in Gemini:</strong> loves through words, curiosity, and playful conversation.",
                "<strong>Venus in Cancer:</strong> nurturing and tender, bonds through care and emotional safety.",
                "<strong>Venus in Leo:</strong> warm and generous, wants to be adored and to adore openly.",
                "<strong>Venus in Virgo:</strong> shows love through helpful acts and quiet, thoughtful devotion.",
                "<strong>Venus in Libra:</strong> romantic and fair, drawn to harmony, partnership, and beauty.",
                "<strong>Venus in Scorpio:</strong> intense and all-in, values depth, loyalty, and emotional truth.",
                "<strong>Venus in Sagittarius:</strong> free-spirited, attracted to adventure and shared meaning.",
                "<strong>Venus in Capricorn:</strong> steady and committed, shows love through reliability and effort.",
                "<strong>Venus in Aquarius:</strong> values friendship, freedom, and unconventional connection.",
                "<strong>Venus in Pisces:</strong> dreamy and compassionate, loves gently and imaginatively.",
            ]),
            ("h2", "Venus Signs and Compatibility"),
            ("p", "Comparing two people&rsquo;s Venus signs is one of the most useful quick reads for compatibility, because it shows whether you naturally express affection in ways the other person actually receives. Two people can love each other deeply and still miss one another if their Venus styles differ &mdash; one wants words, the other wants steadiness. Knowing both makes the gap easier to bridge."),
            ("p", "Your Venus sign is only one placement. A full picture also looks at your Moon (emotional needs), Mars (drive and attraction), and the seventh house (partnership). Our readers weave these together in a birth chart love reading at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver."),
        ],
        "faq": [
            ("Is my Venus sign the same as my Sun sign?", "Not usually, though they can match. Venus is often within one or two signs of your Sun, which is why it feels related but describes something more specific &mdash; your love and attraction style rather than your core identity."),
            ("Do I need my birth time to find my Venus sign?", "Usually no. Venus sign is set by your birth date and year for most people. Birth time matters more for your rising sign and house placements."),
            ("What is more important for love, Venus or the Moon?", "Both matter. Venus shows how you express affection and what you are drawn to; the Moon shows your deeper emotional needs. A love reading looks at them together."),
        ],
        "keywords": "what is a venus sign, venus sign meaning, how to find my venus sign, venus sign compatibility, venus in love astrology, birth chart love reading",
    },
    {
        "slug": "palmistry-101-how-to-read-your-palm",
        "title": "Palmistry 101: How to Read Your Palm",
        "breadcrumb": "Palmistry 101",
        "category": "PALMISTRY",
        "meta": "Palmistry 101: how to read the heart, head, life, marriage, and health lines, which hand to read, and what a healer's mark means. A plain guide from Utopia, North Vancouver.",
        "intro": [
            "Palmistry, also called palm reading or chiromancy, reads the lines, mounts, and shape of the hand as a symbolic map of tendencies &mdash; how you think, love, and move through life. It is a reflective tool and a conversation starter, not a medical diagnosis or a fixed destiny. Hands change as habits change, which is exactly why a palm reading works best as a snapshot of how you are living now.",
            "This guide walks through the major lines one by one, explains which hand to read, and covers the &ldquo;healer&rsquo;s mark&rdquo; that so many people ask about.",
        ],
        "body": [
            ("h2", "Which Hand Do You Read?"),
            ("p", "Traditionally, your non-dominant hand shows innate traits and potential you were born with, while your dominant hand reflects the choices and changes you have made in life. In practice, many readers &mdash; including for women specifically, a common question &mdash; look at both hands together for the fullest picture."),
            ("h2", "The Heart Line"),
            ("p", "The heart line runs across the top of the palm, below the fingers, and relates to your emotional life, relationships, and how you express affection. A long, curved line often suggests warmth and openness; a straighter line can point to a more reserved or practical approach to love."),
            ("h2", "The Head Line"),
            ("p", "The head line sits below the heart line and reflects your thinking style and how you make decisions. A long line can suggest a thorough, detail-oriented mind, while a shorter line may point to quick, decisive thinking."),
            ("h2", "The Life Line"),
            ("p", "The life line curves around the base of the thumb and relates to vitality, energy, and major life changes &mdash; not, despite the myth, the length of your life. A &ldquo;broken&rdquo; life line is commonly read as a period of significant change or a turning point, rather than anything to fear."),
            ("h2", "The Marriage and Relationship Lines"),
            ("p", "Short lines on the side of the palm below the pinky are often read as significant partnerships or relationships. As with every line, readers look at the whole hand rather than drawing conclusions from one mark."),
            ("h2", "The Health Line"),
            ("p", "The health line, when present, runs down toward the base of the palm and is traditionally associated with overall constitution and energy. Many hands do not have a clear one, and its absence is not considered negative."),
            ("h2", "What Is a Healer&rsquo;s Mark?"),
            ("p", "A healer&rsquo;s mark &mdash; sometimes written &ldquo;healers mark,&rdquo; &ldquo;healer&rsquo;s mark,&rdquo; or &ldquo;healing mark&rdquo; &mdash; usually refers to a small group of vertical lines or a cross near the Mount of Mercury (below the pinky), which some traditions associate with a natural gift for helping or healing others. Not everyone has one, and its absence does not mean anything is missing."),
            ("p", "Curious what your hands say about how you are living right now? Ask whether today&rsquo;s reader offers palmistry when you book at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver."),
        ],
        "faq": [
            ("Which hand should a woman have read in palmistry?", "Readers differ, and many read both hands regardless of gender. The common approach is the non-dominant hand for innate traits and the dominant hand for choices and changes."),
            ("Does a broken life line mean a short life?", "No. A broken life line is almost always read as a period of major change or a turning point, not as anything about lifespan."),
            ("What does a healer&rsquo;s mark look like?", "It is usually a small set of vertical lines or a cross near the base of the pinky finger. Traditions vary, and not everyone has one."),
            ("Is palmistry accurate?", "Like tarot, palmistry is best understood as a reflective tool rather than a literal prediction. Many people find it a useful, grounding way to talk about their own life."),
        ],
        "keywords": "palmistry, palm reading, how to read your palm, heart line, head line, life line, broken life line, healers mark, palmistry for female, which hand palmistry",
    },
    {
        "slug": "what-does-a-dragonfly-visit-mean",
        "title": "What Does It Mean When a Dragonfly Visits You? Complete Guide",
        "breadcrumb": "Dragonfly Meaning",
        "category": "ANIMAL SPIRITS",
        "meta": "What does it mean when a dragonfly visits you? A complete guide to dragonfly symbolism: visiting your home, by day, by color, seeing them repeatedly, and dragonfly vs butterfly.",
        "intro": [
            "A dragonfly visiting you is one of the most searched signs in nature symbolism, and it is usually read as a gentle message about change, adaptability, and seeing a situation more clearly. Dragonflies begin life underwater and later take to the air, so many traditions tie them to transformation and to letting go of an illusion you have outgrown.",
            "Whether one landed near you, followed you, or keeps showing up, this guide covers what a dragonfly can mean across the situations people ask about most.",
        ],
        "body": [
            ("h2", "The General Meaning of a Dragonfly"),
            ("p", "At its simplest, a dragonfly is read as a sign of positive change and clarity &mdash; a nudge to trust a shift already underway. Because it moves so nimbly, it is also associated with adaptability and with looking at something from a lighter, freer angle."),
            ("h2", "A Dragonfly in Your Home"),
            ("p", "A dragonfly that comes indoors is often taken as a more personal version of the same message, arriving right where you live. Practically, open a window and let it find its way out; symbolically, many people treat it as a prompt to pay attention to a change close to home."),
            ("h2", "Seeing a Dragonfly During the Day"),
            ("p", "Dragonflies are naturally active in daylight, so a daytime sighting is common. When it feels meaningful &mdash; it lingers, circles, or catches your eye during a decision &mdash; that is the moment worth noticing, rather than the time of day itself."),
            ("h2", "Dragonfly Colors and Their Meanings"),
            ("ul", [
                "<strong>Blue dragonfly:</strong> often linked to calm, clarity, and emotional steadiness.",
                "<strong>Red dragonfly:</strong> associated with passion, energy, and vitality.",
                "<strong>Yellow or gold dragonfly:</strong> tied to optimism, new confidence, and lightness.",
                "<strong>Green dragonfly:</strong> connected to growth, renewal, and fresh starts.",
                "<strong>Black dragonfly:</strong> commonly read as the end of one chapter making room for another.",
            ]),
            ("h2", "Seeing Dragonflies Repeatedly"),
            ("p", "When the same sign keeps appearing, treat it less as a single omen and more as a running theme. Ask what decision is already on your mind each time you notice one. If the sightings ease after you act, the message is usually complete."),
            ("h2", "Dragonfly vs Butterfly Symbolism"),
            ("p", "Both are symbols of transformation, but the tone differs. A butterfly is often read as a full metamorphosis &mdash; becoming something new. A dragonfly leans toward clarity and adaptability in the middle of change, seeing through illusion rather than completing a transformation."),
            ("p", "If a repeating sign is showing up around a real decision, a Clarity &amp; Guidance session can help you sort the signal from the noise. Visit Utopia Wellness &amp; Gifts at 1826 Lonsdale Ave, North Vancouver."),
        ],
        "faq": [
            ("What does it mean when a dragonfly visits you?", "It is usually read as a gentle sign of positive change, adaptability, and clearer seeing. What it points to depends on what is already on your mind when it appears."),
            ("Is a dragonfly in the house good luck?", "Many traditions treat it as a positive, personal version of the dragonfly&rsquo;s change-and-clarity meaning. Practically, just help it back outside through an open window."),
            ("What does it mean to see dragonflies repeatedly?", "Repetition suggests a running theme rather than a one-time omen. Notice the decision on your mind each time; the sign often eases once you act on it."),
            ("What is the difference between a dragonfly and a butterfly sign?", "Both symbolize transformation. A butterfly leans toward becoming something new; a dragonfly leans toward clarity and adaptability within change."),
        ],
        "keywords": "dragonfly spiritual meaning, what does it mean when a dragonfly visits you, dragonfly in the house, yellow dragonfly meaning, seeing dragonflies repeatedly, dragonfly vs butterfly",
    },
    {
        "slug": "tarot-spreads-guide-3-8-monthly",
        "title": "Tarot Spreads Guide: 3, 8, and Monthly Layouts Explained",
        "breadcrumb": "Tarot Spreads Guide",
        "category": "TAROT",
        "meta": "A guide to tarot spreads: the 3-card, 8-card, monthly, and career layouts explained, with what each position means and when to use them. From Utopia in North Vancouver.",
        "intro": [
            "A tarot spread is simply the pattern you lay the cards in, and each position gives a card its job in the reading. Choosing the right spread for your question is half the skill &mdash; a small question wants a small spread, and a full-life question wants more structure.",
            "This guide covers the layouts people ask about most: the 3-card spread, the 8-card spread, monthly spreads, and career-focused layouts.",
        ],
        "body": [
            ("h2", "The 3-Card Spread (Start Here)"),
            ("p", "The 3-card spread is the most useful everyday layout. The classic version reads as past, present, future, but you can reframe the positions to fit the question."),
            ("ul", [
                "Past / Present / Future",
                "Situation / Challenge / Advice",
                "Mind / Body / Spirit",
            ]),
            ("h2", "The 8-Card Spread"),
            ("p", "An 8-card spread gives room for a fuller picture without the complexity of the Celtic Cross. It is a good middle ground for a layered question &mdash; a relationship, a decision, or a season of life &mdash; with positions for the core issue, influences, hidden factors, and likely direction."),
            ("h2", "The Monthly Tarot Spread"),
            ("p", "A monthly spread assigns cards to the weeks or themes of the month ahead, often with one central card for the overall energy. Many readers pull a fresh one at each new moon or on the first of the month to set a reflective tone for the weeks that follow."),
            ("h2", "Career and Job Spreads"),
            ("p", "A career spread focuses the same tools on work: where you are now, what is blocking progress, what strengths to lean on, and the next practical step. It is especially useful during a job change, a burnout stretch, or a decision between two paths."),
            ("h2", "Choosing the Right Spread"),
            ("p", "Match the spread to the weight of the question. A quick check-in wants three cards; a tangled situation wants eight; a forward-looking plan wants a monthly layout. Write your question down before you shuffle so it does not drift mid-reading."),
            ("p", "Want to see a focused reading in person? Ask about tarot when you book a Clarity &amp; Guidance session at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver."),
        ],
        "faq": [
            ("What is the easiest tarot spread for beginners?", "The 3-card spread. It is quick, flexible, and teaches you how position shapes meaning without overwhelming you."),
            ("How does a monthly tarot spread work?", "It assigns cards to the weeks or themes of the coming month, usually with one central card for the overall energy. Many readers pull one at the new moon."),
            ("What spread is best for a career question?", "A career or job spread with positions for your current situation, what is blocking you, your strengths, and the next step. It keeps the reading practical."),
        ],
        "keywords": "tarot spreads, 3 card tarot spread, 8 card tarot spread, monthly tarot spread, career tarot spread, job tarot spread, tarot layouts explained",
    },
    {
        "slug": "most-powerful-tarot-cards-explained",
        "title": "The Most Powerful Tarot Cards, Explained",
        "breadcrumb": "Most Powerful Tarot Cards",
        "category": "TAROT",
        "meta": "The most powerful tarot cards explained: the Death, Tower, Wheel of Fortune, Sun, and Moon cards, and why they carry the biggest turning points in a reading. From Utopia, North Vancouver.",
        "intro": [
            "People often ask which tarot cards are the most powerful, and while there is no official ranking, a handful of Major Arcana cards consistently carry the biggest turning points in a reading. Their power is not about good or bad &mdash; it is about the size of the shift they mark.",
            "Here are the cards most readers describe as the strongest, and what each one actually signals when it appears.",
        ],
        "body": [
            ("h2", "The Death Card"),
            ("p", "Despite its name, Death is almost never literal. It marks endings and transformation &mdash; a chapter closing so another can begin. It is one of the most powerful cards precisely because it points to necessary, often welcome, change."),
            ("h2", "The Tower"),
            ("p", "The Tower represents sudden, clearing upheaval &mdash; the collapse of something built on shaky ground. It can feel jarring, but it is usually read as a fast, honest reset that makes room for something more solid."),
            ("h2", "The Wheel of Fortune"),
            ("p", "The Wheel signals cycles, fate, and turning points. When it appears, it suggests that circumstances are shifting and that timing is a bigger factor than usual. It is a reminder that seasons change."),
            ("h2", "The Sun"),
            ("p", "The Sun is one of the most positive cards in the deck &mdash; clarity, warmth, success, and genuine joy. In love and career readings alike, it points to things coming into the light and going well."),
            ("h2", "The Moon"),
            ("p", "The Moon speaks to intuition, dreams, and what is not yet clear. It asks you to trust your instincts and to be honest about illusion or uncertainty before acting. Its power is in what it reveals over time."),
            ("h2", "Why Context Still Matters"),
            ("p", "Even the strongest card is read in the company of the cards around it. A &ldquo;heavy&rdquo; card beside a hopeful one tells a very different story than it would alone. That is why a reading is a sentence, not a single word."),
            ("p", "Curious how these cards land in your own spread? Ask about tarot at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver."),
        ],
        "faq": [
            ("What are the 3 most powerful tarot cards?", "Most readers point to Death (transformation), the Tower (sudden change), and the Wheel of Fortune (fate and cycles), because they mark the biggest turning points in a reading."),
            ("Is the Death card bad?", "No. It almost always signals transformation and endings that make room for something new, not literal death."),
            ("What is the most positive card in tarot?", "The Sun is widely considered the most positive card, pointing to clarity, warmth, success, and joy."),
        ],
        "keywords": "most powerful tarot cards, strongest tarot card, death tarot card, the tower tarot, wheel of fortune, sun card, moon card meaning",
    },
    {
        "slug": "best-tarot-decks-for-beginners",
        "title": "Best Tarot Decks for Beginners",
        "breadcrumb": "Best Tarot Decks",
        "category": "TAROT",
        "meta": "The best tarot decks for beginners: Rider-Waite-Smith, the Thoth deck, and how to choose a deck that speaks to you. Browse decks in person at Utopia, North Vancouver.",
        "intro": [
            "The best tarot deck for a beginner is the one you will actually pick up and use &mdash; but a few decks are especially friendly to learn on because their imagery does so much of the teaching for you. If you are just starting, imagery and feel matter more than any rulebook.",
            "Here is how the most-asked-about decks compare, and how to choose the one that suits you.",
        ],
        "body": [
            ("h2", "Rider-Waite-Smith (The Classic Starting Point)"),
            ("p", "The Rider-Waite-Smith deck is the most widely used deck in the world and the easiest to learn on, because every card &mdash; including the Minor Arcana &mdash; is fully illustrated with a scene. Almost every tarot book and course references it, so learning on it makes everything else easier."),
            ("h2", "The Thoth Tarot"),
            ("p", "Created by Aleister Crowley and Lady Frieda Harris, the Thoth deck is rich with astrological and symbolic layering. It is stunning but denser, and most readers recommend it once you already have some tarot footing rather than as a first deck."),
            ("h2", "Oracle Decks vs Tarot Decks"),
            ("p", "Oracle decks have no fixed structure &mdash; each one sets its own number of cards and themes &mdash; which makes them gentle and intuitive but harder to &ldquo;learn&rdquo; in a transferable way. Tarot&rsquo;s fixed 78-card structure is what lets skills carry from deck to deck."),
            ("h2", "How to Choose Your First Deck"),
            ("p", "Trust the art. Hold a few decks, notice which images you want to keep looking at, and choose the one that feels alive in your hands. A deck you enjoy looking at is a deck you will practice with."),
            ("p", "We carry a curated selection of tarot and oracle decks in store &mdash; come browse them in person at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver."),
        ],
        "faq": [
            ("What is the best tarot deck for a complete beginner?", "The Rider-Waite-Smith deck. Its fully illustrated cards teach you the meanings visually, and nearly every learning resource is based on it."),
            ("Is the Thoth deck good for beginners?", "It is beautiful but dense with symbolism, so most readers suggest it after you have some experience rather than as a first deck."),
            ("Where can I buy tarot decks near me in North Vancouver?", "Utopia Wellness &amp; Gifts on Lonsdale Ave carries a curated selection of tarot and oracle decks you can browse in person."),
        ],
        "keywords": "best tarot decks, best tarot decks for beginners, rider waite tarot, thoth tarot deck, oracle vs tarot, where to buy tarot cards north vancouver",
    },
    {
        "slug": "best-crystals-for-protection",
        "title": "Best Crystals for Protection",
        "breadcrumb": "Crystals for Protection",
        "category": "CRYSTALS",
        "meta": "The best crystals for protection: black tourmaline, obsidian, hematite, smoky quartz, and how to use protective stones at home or on you. Shop crystals at Utopia, North Vancouver.",
        "intro": [
            "Protective crystals are among the most requested stones we carry, and for good reason &mdash; they give people a simple, physical way to feel grounded and shielded during a hard stretch. Protection stones are tools and reminders, not a substitute for practical steps or professional care, but many people find them genuinely steadying.",
            "Here are the stones most commonly chosen for protection, and simple ways to use them.",
        ],
        "body": [
            ("h2", "The Best Protection Crystals"),
            ("ul", [
                "<strong>Black tourmaline:</strong> the most requested protection stone, used for grounding and creating a sense of an energetic boundary.",
                "<strong>Obsidian:</strong> a volcanic glass associated with cutting through negativity and staying grounded.",
                "<strong>Hematite:</strong> heavy and metallic, chosen for grounding and a feeling of steadiness.",
                "<strong>Smoky quartz:</strong> gentle and stabilizing, popular for releasing heavy moods and staying calm.",
                "<strong>Black onyx:</strong> often kept for resilience and quiet strength during stressful times.",
            ]),
            ("h2", "How to Use Protection Crystals"),
            ("p", "There is no single right way. Many people keep a stone by the front door, carry a small tumbled piece in a pocket or bag, or place one on a desk. The point is to have a physical cue you can reach for when a day feels heavy."),
            ("h2", "Cleansing Your Protection Stones"),
            ("p", "Because protection stones are often used during difficult periods, many people like to cleanse them regularly &mdash; a night in moonlight, a pass through sage or palo santo smoke, or simply resting them on a selenite plate. Keep water-sensitive stones dry."),
            ("h2", "Choosing a Stone That Fits"),
            ("p", "If you are unsure, hold two options and keep the one you do not want to put down. If you are gifting protection to someone going through change, black tourmaline and hematite are reliable, easy-to-live-with choices."),
            ("p", "Come feel the stones in person &mdash; we keep a rotating selection of protection crystals at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver."),
        ],
        "faq": [
            ("What is the best crystal for protection?", "Black tourmaline is the most commonly chosen protection stone, used for grounding and creating a sense of an energetic boundary. Obsidian, hematite, and smoky quartz are also popular."),
            ("How do I use a protection crystal?", "Keep one by the front door, carry a small piece with you, or place one on your desk &mdash; anywhere it acts as a physical cue to feel grounded."),
            ("How often should I cleanse protection crystals?", "Many people cleanse them regularly, especially during stressful periods, using moonlight, sage or palo santo smoke, or a selenite plate."),
        ],
        "keywords": "best crystals for protection, protection crystals, crystals for protection, protective stones, black tourmaline, stone for protection, gemstones for protection",
    },
    {
        "slug": "crystals-by-chakra-simple-guide",
        "title": "Crystals by Chakra: A Simple Guide",
        "breadcrumb": "Crystals by Chakra",
        "category": "CRYSTALS",
        "meta": "A simple guide to crystals by chakra: which stones pair with the root, sacral, solar plexus, heart, throat, third eye, and crown chakras. Shop crystals at Utopia, North Vancouver.",
        "intro": [
            "Matching crystals to chakras is one of the easiest ways to choose a stone with intention, because it starts from what you actually want to work on &mdash; grounding, confidence, communication, or connection. The seven main chakras run from the base of the spine to the crown, and each is traditionally paired with certain colours and stones.",
            "Here is a simple, plain guide to which crystals pair with each chakra.",
        ],
        "body": [
            ("h2", "Root Chakra (Grounding, Safety)"),
            ("p", "At the base of the spine, the root chakra is about stability and feeling secure. Grounding stones like hematite, red jasper, black tourmaline, and smoky quartz are common choices."),
            ("h2", "Sacral Chakra (Creativity, Emotion)"),
            ("p", "Just below the navel, the sacral chakra governs creativity, emotion, and pleasure. Orange-toned stones such as carnelian and orange calcite are the usual pairings."),
            ("h2", "Solar Plexus Chakra (Confidence, Willpower)"),
            ("p", "Above the navel, the solar plexus relates to confidence and personal power. Yellow stones like citrine, tiger&rsquo;s eye, and yellow jasper are traditional matches."),
            ("h2", "Heart Chakra (Love, Connection)"),
            ("p", "At the center of the chest, the heart chakra is about love and connection. Rose quartz, green aventurine, and rhodonite are the most popular heart stones."),
            ("h2", "Throat Chakra (Communication)"),
            ("p", "At the throat, this chakra governs expression and honest communication. Blue stones such as sodalite, lapis lazuli, and blue lace agate are common choices."),
            ("h2", "Third Eye Chakra (Intuition)"),
            ("p", "Between the brows, the third eye relates to intuition and insight. Amethyst and lapis lazuli are frequently paired with it."),
            ("h2", "Crown Chakra (Connection to Something Greater)"),
            ("p", "At the top of the head, the crown chakra is about spiritual connection. Clear quartz, amethyst, and selenite are the usual stones."),
            ("p", "Not sure where to start? Clear quartz is an easy, all-purpose choice. Come match a stone to your intention in person at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver."),
        ],
        "faq": [
            ("What crystal is good for the heart chakra?", "Rose quartz is the most popular heart chakra stone, along with green aventurine and rhodonite."),
            ("Which crystals are for the root chakra?", "Grounding stones like hematite, red jasper, black tourmaline, and smoky quartz are traditional root chakra choices."),
            ("What stone should I start with if I do not know my chakras?", "Clear quartz is a safe, all-purpose choice because it is not tied to a single chakra or meaning."),
        ],
        "keywords": "crystals by chakra, chakra crystals, root chakra stones, sacral chakra crystals, heart chakra crystals, throat chakra stones, third eye chakra, crown chakra crystals",
    },
    {
        "slug": "archangels-and-angel-numbers-guide",
        "title": "Archangels and Angel Numbers: A Complete Guide",
        "breadcrumb": "Archangels &amp; Angel Numbers",
        "category": "ANGEL NUMBERS",
        "meta": "A complete guide to the archangels (Michael, Gabriel, Raphael, Uriel, Azrael and more) and the meaning of angel numbers like 111, 222, 757, 888, and 1234. From Utopia, North Vancouver.",
        "intro": [
            "Archangels and angel numbers are two of the most-searched corners of spiritual life, and they are related: both are ways people describe guidance, reassurance, and a sense of not being alone with a decision. You do not need to already &ldquo;believe&rdquo; to find the language useful &mdash; it is a way to talk about attention and meaning.",
            "This guide covers the main archangels and what they are associated with, then explains the repeating number sequences people notice most.",
        ],
        "body": [
            ("h2", "Angels vs Archangels"),
            ("p", "In most traditions, angels are messengers who interact with individual people, while archangels are higher-ranking and associated with broader themes, protection, or leadership. Archangels are usually the named figures people call on for specific kinds of help."),
            ("h2", "The Main Archangels"),
            ("ul", [
                "<strong>Michael:</strong> protection and courage.",
                "<strong>Gabriel:</strong> communication and messages.",
                "<strong>Raphael:</strong> healing and restoration.",
                "<strong>Uriel:</strong> wisdom and illumination.",
                "<strong>Jophiel:</strong> beauty and clarity of thought.",
                "<strong>Chamuel:</strong> love and relationships.",
                "<strong>Azrael:</strong> comfort, transition, and support in grief.",
            ]),
            ("h2", "What Are Angel Numbers?"),
            ("p", "Angel numbers are repeating sequences some people believe carry gentle guidance. Seeing the same number often is usually read less as a literal message and more as a nudge to pay attention to your current thoughts or decisions."),
            ("h2", "Common Angel Numbers and Their Meanings"),
            ("ul", [
                "<strong>000:</strong> a reset or a blank page.",
                "<strong>111:</strong> new beginnings and alignment with your thoughts.",
                "<strong>222:</strong> balance, partnership, and trusting the process.",
                "<strong>757:</strong> often tied to change in love and personal growth.",
                "<strong>888:</strong> associated with abundance and momentum.",
                "<strong>1234:</strong> steady, step-by-step progress.",
            ]),
            ("h2", "How to Work With a Number You Keep Seeing"),
            ("p", "Write down the number and the thought you had when you saw it, name one decision already on your mind, and take one small action. If the number eases after you act, the loop is usually complete."),
            ("p", "Want to talk through what keeps showing up for you? Book a Clarity &amp; Guidance session at Utopia Wellness &amp; Gifts, 1826 Lonsdale Ave, North Vancouver."),
        ],
        "faq": [
            ("What is the difference between an angel and an archangel?", "Angels are generally described as messengers who interact with individuals, while archangels are higher-ranking and tied to broader themes like protection, healing, or wisdom."),
            ("What does the angel number 111 mean?", "It is usually read as new beginnings and alignment &mdash; a prompt to check whether your current focus is the direction you actually want."),
            ("Which archangel is associated with healing?", "Raphael is traditionally associated with healing and restoration."),
            ("Are angel numbers real messages?", "They are best understood as prompts to pay attention rather than literal messages. The value is in what you notice and choose to do next."),
        ],
        "keywords": "archangels, angel numbers, angel vs archangel, archangel uriel, archangel raphael, archangel azrael, 111 meaning, 222 meaning, 757 angel number, 888 meaning, 1234 angel number",
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
