"""
Generate the comprehensive FAQ mega-guide blog from blog/TEMPLATE.html.

Run:  python shopify/gen_blog3.py
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


SLUG = "utopia-north-vancouver-complete-faq-guide"
TITLE = "Utopia Wellness &amp; Gifts, North Vancouver: The Complete Spiritual, Tarot &amp; Metaphysical FAQ Guide"
BREADCRUMB = "Complete FAQ Guide"
DATE = "September 1, 2026"
ISO = "2026-09-01"
CATEGORY = "SPIRITUALITY"
META = "The complete FAQ guide from Utopia Wellness & Gifts, North Vancouver: tarot, crystals, moon water, chakras, astrology, angel numbers, dreams, and energy clearing answered."

INTRO = [
    "Your neighborhood metaphysical store on Lonsdale Avenue &mdash; tarot, crystals, moon water, energy clearing, and answers to the spiritual questions you keep searching for.",
    "If you&rsquo;ve searched for &ldquo;metaphysical store near me,&rdquo; &ldquo;crystal shop North Vancouver,&rdquo; or &ldquo;what does it mean when a dragonfly visits me,&rdquo; you&rsquo;ve probably landed on Utopia Wellness &amp; Gifts. We put together this FAQ guide to answer the questions our community asks us most &mdash; in the shop, over the phone, and online. Bookmark it, come back to it, and stop by in person when you want to go deeper.",
]

# List of (section_heading, [(question, answer), ...])
SECTIONS = [
    ("About Utopia Wellness &amp; Gifts", [
        ("What is Utopia Wellness &amp; Gifts?", "Utopia Wellness &amp; Gifts (also known as Utopia Sacred Space, Utopia Store, or simply &ldquo;Utopia&rdquo;) is a metaphysical and spiritual wellness shop in North Vancouver. We carry tarot and oracle decks, crystals and healing stones, sage and palo santo, singing bowls, jewelry, and gifts for anyone on a spiritual path &mdash; plus in-store tarot card reading, palmistry, and energy work sessions with local practitioners."),
        ("Where is Utopia located?", "Utopia Wellness &amp; Gifts is located at 1826 Lonsdale Ave, North Vancouver, British Columbia, V7M 2J9, Canada &mdash; right on the main Lonsdale strip, an easy walk from the SeaBus and North Vancouver&rsquo;s shops, cafés, and the North Vancouver bookstore and jewelry stores nearby."),
        ("What are Utopia&rsquo;s hours?", "Because our hours can shift around events, private readings, and holidays, the most accurate and up-to-date hours are always listed on our Google Business Profile and at utopiastore.ca. As a general rule, we&rsquo;re open daily during regular North Vancouver retail hours &mdash; we recommend a quick check online or a phone call before a special trip."),
        ("Is Utopia a mall, an outlet, or a single storefront?", "Utopia is a single, dedicated storefront on Lonsdale Avenue &mdash; not a mall or outlet. Some people search &ldquo;Utopia mall&rdquo; or &ldquo;Utopia outlet&rdquo; expecting a larger complex, but we&rsquo;re a focused, curated metaphysical shop rather than a multi-store centre."),
        ("Is there an Utopia in Toronto, Montreal, or elsewhere in Canada?", "The Utopia Wellness &amp; Gifts you&rsquo;re reading about is our North Vancouver location on Lonsdale Ave. If you&rsquo;ve searched &ldquo;Utopia Toronto&rdquo; or &ldquo;Utopia Montreal,&rdquo; you may be thinking of a different, unrelated business &mdash; for BC and Metro Vancouver metaphysical shopping, our North Vancouver store is the one to visit."),
        ("Does Utopia offer tarot readings, palmistry, or psychic sessions?", "Yes. Utopia hosts in-store tarot card readings, palmistry, and energy work with visiting readers and practitioners. Availability rotates, so check our website or call ahead if you want a specific type of reading (tarot, palm, or medium/clairvoyant session) on a particular day."),
        ("Does Utopia sell gift cards?", "Many metaphysical and wellness shops, including boutique stores like ours, offer gift cards for readings, workshops, or in-store credit &mdash; the best way to confirm current gift card options is to ask in person or check our site directly, since offerings change seasonally."),
    ]),
    ("Tarot &amp; Oracle Card FAQ", [
        ("What is tarot reading?", "Tarot reading is the practice of using a 78-card deck &mdash; split into the Major and Minor Arcana &mdash; to reflect on a question, situation, or period of life. A reader (or you, reading for yourself) draws cards in a specific layout, or &ldquo;spread,&rdquo; and interprets the symbolism in relation to what&rsquo;s going on in your life right now."),
        ("Do tarot cards actually work?", "Whether tarot &ldquo;works&rdquo; depends on how you use it. Skeptics see it as a structured way to organize your own thoughts and intuition; many regular tarot users describe it as a tool for reflection, pattern recognition, and clarity rather than literal fortune-telling. Either way, a good reading should leave you with more self-awareness, not less agency."),
        ("What&rsquo;s the difference between the Rider-Waite deck and the Thoth deck?", "The Rider-Waite (or Rider-Waite-Smith) tarot deck is the most widely used deck worldwide, known for its fully illustrated Minor Arcana and beginner-friendly imagery. The Thoth tarot deck, created by Aleister Crowley and Lady Frieda Harris, uses more esoteric, astrologically and Kabbalistically layered artwork and is generally recommended for readers who already have some tarot experience."),
        ("What is the Celtic Cross spread, and what other spreads should I know?", "The Celtic Cross is an 11-card spread that maps out a situation&rsquo;s present influences, obstacles, past, future, and outcome &mdash; one of the most popular layouts for in-depth questions. Simpler options include the 3-card spread (past/present/future or situation/action/outcome), the 5-card spread, and the 8-card spread, which are great for quicker daily or weekly pulls."),
        ("What do the Wheel of Fortune, Death, High Priestess, Star, Hermit, Temperance, Magician, Empress, and World cards mean?", "Broadly: the Wheel of Fortune signals cycles, fate, and turning points; Death represents transformation and endings that make way for something new (rarely literal death); the High Priestess points to intuition and hidden knowledge; the Star brings hope and healing after a hard chapter; the Hermit calls for introspection and solitude; Temperance speaks to balance and patience; the Magician signals resourcefulness and manifestation; the Empress relates to abundance and nurturing; and the World marks completion and fulfillment. Every card should be read in context with the cards around it."),
        ("What are the 3 most powerful or important tarot cards?", "There&rsquo;s no single official ranking, but the cards most readers describe as the most &ldquo;powerful&rdquo; in the Major Arcana are usually the Death card (transformation), the Tower (sudden, necessary upheaval), and the Wheel of Fortune (fate and change) &mdash; because they mark the biggest turning points in a reading."),
        ("How do I cleanse tarot cards, including after someone else has touched them?", "Common ways to cleanse a tarot deck include knocking on the deck three times, passing it through sage or palo santo smoke, leaving it in moonlight overnight, or shuffling with a clear, stated intention. If someone else has handled your deck (a friend, a shop customer, or a reader), a quick smoke cleanse or moonlight reset is the most common way to clear their energy before your next reading."),
        ("What can I do with old tarot cards I no longer use?", "You can cleanse and pass them on to a friend who&rsquo;s curious about tarot, donate them to a metaphysical or charity shop, repurpose the art in a journal or altar collage, or simply retire them to a box with intention. There&rsquo;s no requirement to destroy a deck &mdash; many readers keep old decks as keepsakes even after switching to a new one."),
        ("Where can I buy tarot cards near me in North Vancouver or Metro Vancouver?", "Utopia Wellness &amp; Gifts on Lonsdale Ave carries a curated selection of tarot and oracle decks in-store, making us one of the go-to tarot shops in North Vancouver and the wider Metro Vancouver area if you&rsquo;d rather browse decks in person than order online."),
    ]),
    ("Crystals &amp; Healing Stones FAQ", [
        ("How do I cleanse crystals?", "The most common crystal-cleansing methods are: smoke cleansing with sage or palo santo, resting the stones in moonlight (especially a full moon), briefly running them under water (only for water-safe stones), or placing them on a selenite charging plate or near a singing bowl&rsquo;s sound vibrations."),
        ("What crystals are best for protection?", "Popular protection stones include black tourmaline, obsidian, hematite, and smoky quartz, which are widely used to help ground energy and create a sense of energetic boundary. Many people also keep a protection stone by the front door or carry one for daily use."),
        ("What crystals are good for the throat chakra or solar plexus chakra?", "Blue-toned stones like sodalite, lapis lazuli, aquamarine, and blue lace agate are traditionally associated with the throat chakra (communication and self-expression). For the solar plexus chakra (confidence, personal power), yellow stones such as citrine, tiger&rsquo;s eye, and yellow jasper are common choices."),
        ("Where can I buy crystals and stones near me in North Vancouver?", "Utopia Wellness &amp; Gifts stocks a rotating selection of crystals, healing stones, and crystal jewelry in our North Vancouver storefront on Lonsdale Ave &mdash; come in to feel the stones in person, since many people find that part of choosing a crystal."),
    ]),
    ("Moon Water FAQ", [
        ("How do you make moon water?", "To make moon water, fill a clean glass jar or bowl with water and set it outside (or on a windowsill) where it can be bathed in moonlight overnight, ideally during a full moon. Many people set an intention over the water before placing it out, and bring it back inside before sunrise."),
        ("How do you charge moon water, and how long should it charge?", "&ldquo;Charging&rdquo; moon water simply means leaving it under moonlight long enough to soak up the energy of that lunar phase &mdash; typically from moonrise to just before sunrise, so roughly 6&ndash;10 hours overnight. A full moon is the most popular time to charge water, though some people also charge water during new moons for a different intention (release vs. new beginnings)."),
        ("Can you drink moon water, and how much should you drink?", "Many people do drink moon water in small amounts, treating it similarly to how they&rsquo;d use any other intention-set water &mdash; there&rsquo;s no fixed &ldquo;dose,&rdquo; and people typically add a small amount to a glass of drinking water rather than drinking it straight from the charging vessel. If you have any health concerns, treat moon water as a ritual practice rather than a medical remedy, and use a clean vessel meant for drinking water."),
        ("How do I set intentions for moon water before making it?", "Before you set the water out, hold the jar, take a few breaths, and speak or think a clear, present-tense intention &mdash; for example, &ldquo;this water carries clarity and calm.&rdquo; Some people also add a corresponding crystal near (not necessarily in) the jar to reinforce the intention."),
    ]),
    ("Palmistry FAQ", [
        ("What is palmistry, and how accurate is it?", "Palmistry (also called palm reading or chiromancy) is the practice of reading the lines, mounts, and shape of the hand to reflect on personality traits and life patterns. Like tarot, its accuracy is debated &mdash; many people find value in it as a reflective tool and a conversation starter about their own life rather than a literal prediction."),
        ("Which hand do you read for palmistry &mdash; left or right?", "Traditionally, your non-dominant hand is read for innate traits and potential you were &ldquo;born with,&rdquo; while your dominant hand reflects choices and changes you&rsquo;ve made in life. In practice, many readers look at both hands together for the fullest picture."),
        ("What do the main lines on your palm mean?", "The heart line relates to emotional life and relationships; the head line relates to thinking style and decision-making; the life line relates to vitality and major life changes (not literal lifespan); and the marriage or relationship line(s), near the pinky, are said to reflect significant partnerships. A &ldquo;broken&rdquo; life line is commonly interpreted as a period of significant change rather than a bad omen."),
        ("What is a &ldquo;healer&rsquo;s mark&rdquo; in palmistry?", "A healer&rsquo;s mark usually refers to a specific cross or star-shaped marking, often near the Mount of Jupiter (below the index finger) or on the Mount of Mercury, that some palmistry traditions associate with natural healing or intuitive ability. Not everyone has one, and its absence doesn&rsquo;t mean anything negative."),
    ]),
    ("Chakras FAQ", [
        ("What are the main chakras and what do they relate to?", "The seven main chakras are: root (safety, stability), sacral (creativity, emotion, and intimacy), solar plexus (confidence, willpower), heart (love, connection), throat (communication), third eye (intuition), and crown (spiritual connection)."),
        ("Which chakra relates to creative intimacy?", "The sacral chakra (located just below the navel) is the chakra most associated with creativity, emotional flow, pleasure, and intimacy. It&rsquo;s often the focus of healing work when someone feels creatively blocked or disconnected from their emotions."),
        ("How do I balance my root chakra, and what activities help the sacral chakra?", "Root chakra balancing often involves grounding activities like walking barefoot outside, using grounding stones (hematite, red jasper), and slow, steady breathing exercises. Sacral chakra healing activities include creative expression (art, dance, journaling), hip-opening movement or yoga, and using orange-toned crystals like carnelian."),
        ("What are good crown chakra affirmations?", "Simple crown chakra affirmations focus on connection and openness &mdash; phrases like &ldquo;I am connected to something greater than myself&rdquo; or &ldquo;I am open to wisdom and guidance&rdquo; are commonly used during crown chakra meditation."),
    ]),
    ("Astrology &amp; Zodiac Signs FAQ", [
        ("What are the fire, water, air, and earth signs?", "Fire signs: Aries, Leo, Sagittarius. Water signs: Cancer, Scorpio, Pisces. Air signs: Gemini, Libra, Aquarius. Earth signs: Taurus, Virgo, Capricorn. So yes &mdash; Aries is a fire sign, Cancer and Scorpio and Pisces are water signs, and Libra and Gemini are air signs."),
        ("What does the 1st house and 9th house mean in astrology?", "The first house represents self-image, appearance, and how you present yourself to the world &mdash; it&rsquo;s ruled by your rising sign. In mundane astrology (astrology applied to world events rather than individuals), the ninth house relates to long-distance travel, foreign relations, higher education, philosophy, and the legal system of a country."),
        ("What does my birth chart say about my love life?", "Your birth chart&rsquo;s Venus sign shows how you express affection and what you value in relationships, your Mars sign reflects attraction and drive, and your seventh house describes your approach to committed partnership. A full natal chart love-life reading typically looks at all three together rather than any single placement alone."),
        ("What are common traits of a Scorpio woman?", "Scorpio women are frequently described as intense, loyal, emotionally deep, intuitive, and fiercely protective of the people they love. Traits often associated with Scorpio women in popular astrology include strong intuition, a magnetic or striking presence, determination, a private nature, and a low tolerance for dishonesty &mdash; though, as with any sun sign, a full chart (moon, rising, Venus) gives a much fuller personality picture than the sun sign alone."),
    ]),
    ("Angel Numbers &amp; Archangels FAQ", [
        ("What do repeating numbers like 111, 222, 444, 1212, and 1234 mean?", "These are commonly called &ldquo;angel numbers,&rdquo; repeating sequences some people believe carry guidance: 111 &mdash; new beginnings, alignment with your thoughts; 222 &mdash; balance, partnership, trust the process; 444 &mdash; stability, support, &ldquo;you&rsquo;re on the right path&rdquo;; 1212 &mdash; growth and manifestation, including career growth; 1234 &mdash; forward momentum and steady progress. Seeing the same number repeatedly is often interpreted less as a literal message and more as a nudge to pay attention to your current thoughts or decisions."),
        ("What is the difference between an angel and an archangel?", "In most angelology traditions, angels are considered messengers who interact directly with individual people, while archangels are higher-ranking angels associated with broader themes, protection, or leadership roles. Archangels like Michael, Gabriel, Raphael, Uriel, Jophiel, and Azrael are each linked to specific areas of guidance."),
        ("What are the names and meanings of the 7 archangels?", "Traditions vary, but a commonly cited list includes Michael (protection, courage), Gabriel (communication, messages), Raphael (healing), Uriel (wisdom, illumination), Jophiel (beauty, clarity of thought), Chamuel (love, relationships), and Azrael (comfort, transition and grief support)."),
        ("What color eyes do earth angels have, and what does &ldquo;angel eyes&rdquo; mean?", "In popular spiritual folklore, &ldquo;earth angels&rdquo; &mdash; people said to have an unusually calming or healing presence &mdash; are sometimes described as having striking blue, green, or light-colored eyes, though this is folklore rather than any established rule, and plenty of people who fit the description have brown eyes too."),
    ]),
    ("Animal &amp; Insect Spiritual Signs FAQ", [
        ("Is there a sign if a praying mantis appears?", "A praying mantis sighting is commonly interpreted as a call to slow down, stay still, and observe before acting &mdash; mantises are patient, deliberate hunters, and their symbolism often centers on mindfulness, patience, and trusting your intuition rather than rushing a decision."),
        ("What is the spiritual meaning of a dragonfly, and what does it mean when one visits or follows you?", "Dragonflies are widely associated with transformation, self-realization, and letting go of illusions, largely because of their own life cycle from water-bound nymph to flying adult. A dragonfly that visits, lingers near, or seems to follow you is often interpreted as a sign of positive change, adaptability, or a reminder to see a situation more clearly."),
        ("What is the spiritual meaning of seeing a butterfly, and does the same butterfly returning mean anything?", "Butterflies are a near-universal symbol of transformation, rebirth, and the soul &mdash; many cultures associate them with personal growth or with visits from a loved one who has passed. A specific butterfly that repeatedly returns to the same spot is often taken as a comforting sign, especially by those who are grieving."),
        ("What does it mean when a ladybug (or ladybird) visits you?", "Ladybugs are broadly seen as a sign of good luck, protection, and positive change on the way &mdash; in many folk traditions, letting one land on you (rather than shooing it away) is considered especially lucky."),
        ("What does it mean spiritually when you see 2 rabbits or bunnies together?", "Two rabbits or bunnies appearing together is often interpreted as a sign of fertility, abundance, partnership, and rapid, positive growth in an area of your life &mdash; rabbits&rsquo; association with fertility across folklore makes a pair especially symbolic of new beginnings or a flourishing relationship."),
        ("What bird represents grief, and what do ravens, crows, owls, blue jays, and red cardinals symbolize?", "Ravens/crows are often tied to grief, transformation, and messages from beyond, especially in Norse and Celtic mythology. Owls symbolize wisdom, intuition, and the ability to see what others miss, sometimes also endings or change. Blue jays represent courage, communication, and standing your ground. Red cardinals are widely believed, in North American folklore, to represent a visit from a loved one who has passed, especially around anniversaries or hard days."),
        ("What does a bee landing on or &ldquo;visiting&rdquo; you mean spiritually?", "Bees are generally seen as symbols of productivity, community, and abundance &mdash; a bee landing on you (or even an unusual encounter with one) is often interpreted as a sign that hard work is about to pay off, or that a joyful message is on its way."),
        ("What does it mean to see a fox, spiritually?", "Foxes are commonly associated with cleverness, adaptability, and the need to trust your instincts in a tricky situation &mdash; seeing one is sometimes taken as a nudge to be more strategic or observant before making a move."),
    ]),
    ("Smudging, Sage &amp; Energy Cleansing FAQ", [
        ("What do you say when smudging or saging yourself or your house?", "There&rsquo;s no single required phrase &mdash; the words matter less than the intention behind them. A simple, common approach is to state what you want to release (&ldquo;I release any negative or stagnant energy from this space&rdquo;) and what you want to invite in (&ldquo;I welcome peace, clarity, and positive energy&rdquo;), repeating a version of this as you move the smoke around yourself or each room."),
        ("What are the benefits of burning sage, and why sage your house?", "Burning sage (smudging) is traditionally used to clear stagnant or negative energy from a person or space, mark a fresh start (after an argument, illness, or big life change), and create a sense of calm or reset. People often sage a home after moving in, after conflict, or simply as a regular energetic &ldquo;reset.&rdquo;"),
        ("How do I cleanse my home of negative energy, and what are signs my house needs energy clearing?", "Common signs a space may need clearing include a &ldquo;heavy&rdquo; or stagnant feeling, unusually frequent arguments in the home, or ongoing bad luck after a specific event. To clear a home, many people combine smoke cleansing (sage or palo santo), opening windows to circulate air, playing a singing bowl through each room, and setting a clear verbal intention."),
        ("How do I cleanse myself with an egg (egg cleansing ritual)?", "An egg cleanse (a folk practice found in several cultures) typically involves rolling a raw, unbroken egg gently over your body &mdash; often starting at the head and moving down &mdash; while stating an intention to absorb and remove negative energy, then cracking the egg into a glass of water afterward to &ldquo;read&rdquo; the result. It&rsquo;s considered a low-risk ritual, though as with any folk practice, treat the interpretation as reflective rather than diagnostic."),
        ("What do I say over a container of salt I want to cleanse with sage smoke?", "A simple approach is to hold the container in the sage smoke and state your intention directly and specifically &mdash; for example, &ldquo;I cleanse this salt of any negative or unwanted energy, and charge it with protection and clarity&rdquo; &mdash; repeating it slowly as the smoke surrounds the container."),
        ("What&rsquo;s a cord-cutting ritual?", "Cord-cutting (sometimes misspelled &ldquo;chord-cutting&rdquo;) is a visualization or ritual practice for symbolically releasing an unhealthy energetic attachment to a person, situation, or past relationship &mdash; often done by visualizing a cord between you and the other person or situation, and imagining it being gently cut or dissolved, followed by a grounding or cleansing step."),
    ]),
    ("Dreams &amp; Dream Meaning FAQ", [
        ("Why do I keep having nightmares or bad dreams every night?", "Frequent nightmares are most often linked to stress, anxiety, disrupted sleep schedules, certain medications, or processing difficult emotions during the day &mdash; many people notice a spike in bad dreams during high-stress periods. Spiritually, recurring nightmares are sometimes interpreted as a sign that something in waking life needs attention or release; practically, persistent nightmares are also worth mentioning to a doctor if they&rsquo;re affecting your sleep quality."),
        ("What does it mean to dream about being pregnant?", "Dreaming about being pregnant is very common and is usually interpreted symbolically rather than literally &mdash; often linked to new ideas, projects, or a phase of personal growth &ldquo;developing&rdquo; in your life, rather than to an actual pregnancy."),
        ("What does it mean when you dream about someone dying?", "Dreams about death &mdash; your own or someone else&rsquo;s &mdash; are typically interpreted as symbolic of endings and transformation rather than a literal warning, often reflecting the end of a life phase, relationship dynamic, or habit rather than anything to fear."),
        ("Why do I keep dreaming about my ex?", "Recurring dreams about an ex are commonly linked to unresolved feelings, unfinished emotional processing, or simply your subconscious revisiting a familiar emotional pattern &mdash; it doesn&rsquo;t necessarily mean you should reconnect, and is often more about closure than about the person themselves."),
        ("Why can&rsquo;t I remember my dreams, or why am I dreaming more than usual lately?", "Dream recall is affected by sleep quality, stress levels, alcohol, and how abruptly you wake up &mdash; waking naturally, rather than to an alarm, tends to improve recall. An increase in dreaming (or noticing dreams more) is often linked to a change in sleep patterns, stress, or simply paying more attention to your sleep lately."),
    ]),
    ("Psychic Readings, Mediums &amp; Clairvoyance FAQ", [
        ("What is a clairvoyant, and what does &ldquo;psychic ability&rdquo; mean?", "A clairvoyant is someone who reports the ability to gain information through means beyond the five ordinary senses &mdash; often described as &ldquo;clear seeing.&rdquo; &ldquo;Psychic ability&rdquo; is a broader umbrella term covering intuitive or extrasensory insight in general, of which clairvoyance is one specific type."),
        ("What&rsquo;s the difference between a psychic and a medium?", "A psychic generally works with intuitive insight about a person&rsquo;s life, energy, or future. A medium specifically claims to communicate with spirits of those who have died, acting as a bridge between the living and the deceased. Not every psychic is a medium, though some practitioners offer both."),
        ("What is clairsentience, and how is it different from being an empath?", "Clairsentience (&ldquo;clear feeling&rdquo;) is a reported psychic ability to sense information as physical or emotional feelings, sometimes about people, places, or events beyond someone&rsquo;s own direct experience. An empath, by contrast, deeply feels and absorbs the emotions of people around them &mdash; the overlap is real, but clairsentience is generally framed as an intuitive &ldquo;sensing&rdquo; ability, while empathy is about emotional attunement to others."),
        ("How accurate are psychic readings?", "Accuracy varies enormously by practitioner, and there&rsquo;s no scientific consensus validating psychic readings as literally predictive. Many people find value in readings as a structured space for reflection, validation, and perspective &mdash; approaching a reading with curiosity rather than as a guaranteed forecast tends to lead to the most useful experience."),
    ]),
    ("Ex-Relationship Spiritual Signs FAQ", [
        ("Are there spiritual signs your ex is thinking about you during no contact?", "People commonly describe things like sudden, vivid dreams about the ex, unexplained &ldquo;gut feelings,&rdquo; repeating angel numbers, or a specific song or memory surfacing out of nowhere as informal &ldquo;signs.&rdquo; These are subjective and impossible to verify, so it&rsquo;s worth holding them loosely rather than using them to justify breaking no-contact."),
        ("What does left eye twitching or ringing in the left ear mean spiritually?", "In several folk traditions, a twitching left eye or ringing left ear is associated with someone thinking or talking about you &mdash; interpretations sometimes differ slightly by gender in these traditions. Physically, eye twitching is far more often linked to fatigue, caffeine, or eye strain than anything spiritual."),
    ]),
    ("Sacred Space &amp; Home Energy FAQ", [
        ("What does &ldquo;sacred space&rdquo; mean, and how do I create one at home?", "A sacred space is any area &mdash; a corner of a room, a full room, or an outdoor spot &mdash; that&rsquo;s intentionally set aside for reflection, ritual, meditation, or spiritual practice. To create one: choose a consistent spot, clear the clutter, add meaningful objects (crystals, candles, a small altar), and return to it regularly so the space builds its own sense of calm over time."),
        ("How do I create a personal altar for ritual work?", "A simple personal altar usually includes a representative object for each of the four elements (a candle for fire, a bowl of water, a stone or plant for earth, incense or a feather for air), plus any personally meaningful items &mdash; photos, crystals, cards. Keep it somewhere you&rsquo;ll see it daily, and refresh or cleanse it periodically."),
    ]),
]

CLOSING = "Whether you came here searching for &ldquo;tarot shop near me,&rdquo; &ldquo;crystal store North Vancouver,&rdquo; &ldquo;metaphysical store near me,&rdquo; or &ldquo;what does it mean when I see a dragonfly,&rdquo; we hope this answered what you came for &mdash; and gave you a few new questions to explore. Utopia Wellness &amp; Gifts is located at 1826 Lonsdale Ave, North Vancouver, BC V7M 2J9, with tarot decks, crystals, sage, singing bowls, jewelry, and in-store readings waiting for you. Stop by, browse, and let us know what you&rsquo;re looking for."

PEOPLE_ALSO = ("utopia shop &middot; utopia store north vancouver &middot; utopia sacred space &middot; utopia north van &middot; utopia near me &middot; utopia bc &middot; utopia website &middot; utopia booking &middot; utopia lonsdale &middot; card reading north vancouver &middot; reiki north vancouver &middot; sound bath north vancouver &middot; meditation north vancouver &middot; yoga north vancouver &middot; intuitive listening vancouver &middot; energy clearing vancouver &middot; home energy clearing north vancouver &middot; curse removal vancouver &middot; negative energy removal vancouver &middot; psychic vancouver &middot; tarot reader vancouver &middot; witch store vancouver &middot; witchcraft store near me &middot; occult shop near me &middot; new age stores near me &middot; esoteric store near me &middot; spiritualist shop near me &middot; magic store vancouver &middot; gem and crystal store near me &middot; crystal singing bowls &middot; singing bowl meditation near me &middot; pendulum shop near me &middot; dream catcher near me &middot; palo santo sticks &middot; incense store near me &middot; sage and crystals near me &middot; protection stones &middot; sacral chakra healing activities &middot; third eye chakra &middot; fifth chakra stones &middot; rising sign &middot; natal chart love reading &middot; capricorn compatibility &middot; scorpio and taurus compatibility &middot; year of the snake meaning &middot; year of the dragon chinese zodiac &middot; what is zazen meditation &middot; moonology oracle cards &middot; starseed oracle cards &middot; thoth tarot deck &middot; rider waite tarot deck &middot; knocking on tarot deck &middot; lost item tarot spread &middot; monthly tarot spread &middot; past life reading &middot; medium reading near me &middot; psychic medium definition &middot; clairvoyance vs clairsentience &middot; spirit animal meaning &middot; how to find your spirit animal &middot; what color is my aura &middot; how to cleanse your aura &middot; green aura meaning &middot; attachment style quiz &middot; karmic connection meaning &middot; dream analysis &middot; visitation dreams grief &middot; why do bad things keep happening to me &middot; how to attract luck &middot; setting intentions ritual &middot; solstice ceremony &middot; full moon ceremony near me &middot; new moon 2026 dates &middot; does the moon go retrograde &middot; spider symbolism &middot; owl sighting spiritual meaning &middot; raven symbolism &middot; crow bird meaning &middot; rat in house spiritual meaning &middot; significance of a cat &middot; what does seeing a rainbow mean &middot; spiritual meaning of the color red &middot; flowers associated with angels &middot; agua de florida &middot; feng shui items &middot; wish lanterns &middot; meditation cushion &middot; sacred stones &middot; sound bowls &middot; gong meditation &middot; north vancouver bookstore &middot; jewelry stores north vancouver &middot; art supply stores near me &middot; north vancouver florist")


def build_body():
    parts = []
    for heading, qas in SECTIONS:
        parts.append("      " + H2(heading))
        for q, a in qas:
            parts.append("      " + H3(q))
            parts.append("      " + P(a))
    # Closing section
    parts.append("      " + H2("Visit Utopia Wellness &amp; Gifts in North Vancouver"))
    parts.append("      " + P(CLOSING))
    # People also search line
    parts.append(
        '      <p class="text-[.8rem] font-light mt-8" style="color:var(--text-muted)"><strong>People also search for:</strong> '
        + PEOPLE_ALSO + "</p>"
    )
    return "\n".join(parts)


def faq_schema():
    def esc(s):
        s = re.sub(r"<[^>]+>", "", s)
        # normalize entities to plain characters first
        s = (s.replace("&amp;", "&").replace("&mdash;", "-").replace("&ndash;", "-")
               .replace("&ldquo;", '"').replace("&rdquo;", '"')
               .replace("&rsquo;", "'").replace("&lsquo;", "'").replace("&middot;", "-"))
        # then escape for JSON (backslash first, then quote)
        s = s.replace("\\", "\\\\").replace('"', '\\"')
        return s
    qas = []
    for _, section_qas in SECTIONS:
        qas.extend(section_qas)
    items = ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (esc(q), esc(a))
        for q, a in qas
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

    html = tpl
    html = html.replace("{{TITLE}}", TITLE)
    html = html.replace("{{META_DESCRIPTION}}", META)
    html = html.replace("{{SLUG}}", SLUG)
    html = html.replace("{{BREADCRUMB}}", BREADCRUMB)
    html = html.replace("{{DATE_ISO}}", ISO)
    html = html.replace("{{DATE}}", DATE)

    intro_html = "\n".join("      " + P(p) for p in INTRO)
    html = html.replace("{{CONTENT_INTRO}}", intro_html)
    html = html.replace("{{CONTENT_BODY}}", build_body())
    html = html.replace("</body>", faq_schema() + "\n</body>")

    out_path = os.path.join(BLOG_DIR, SLUG + ".html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {SLUG}.html")

    try:
        from gen_blogdata import regenerate
        regenerate()
    except Exception as e:
        print(f"(gen_blogdata skipped: {e})")


if __name__ == "__main__":
    main()
