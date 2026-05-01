from PIL import Image, ImageDraw, ImageFont
import os, textwrap

# ====================== CONFIG ======================
book_list = [
    "Elementary I Ching — Turner",
    "The Compleat Meadmaker — Schramm",
    "The Heart of Aromatherapy — Andrea Butje",
    "A Gathering of Brilliant Moons — Gayley & Schapiro",
    "Brightening Our Inner Skies: Yin and Yoga — Norman Blair",
    "Bloom — Bronnie Ware",
    "Reboot with Joe: Fully Charged — Joe Cross",
    "Archangels & Ascended Masters — Doreen Virtue",
    "Assertiveness for Earth Angels — Doreen Virtue",
    "Essential Oils for Childbirth — Boldy",
    "Your Altar — Kynes",
    "The Crystal Experience",
    "The Crystal Bible 3",
    "The Feng Shui Bible",
    "Wind and Water: Your Personal Feng Shui Journey",
    "The Palmistry Bible",
    "The Aromatherapy Bible",
    "The Astrology Bible",
    "The Mandala Bible",
    "The Chakra Bible",
    "The Meditation Bible",
    "The Pocket Book of Stones — Robert Simmons",
    "Visualizations for Self Empowerment",
    "Ostara: Customs",
    "Nordic Runes — Mountfort",
    "The Empath's Survival Guide — Judith Orloff MD",
    "Awakening Your Inner Shaman — Marcela Lobos",
    "A Handbook of Saxon Sorcery & Magic — Shumsky",
    "Awaken Your Divine Intuition — Shumsky",
    "The Art of Manifesting — Colette Baron-Reid",
    "The Let Them Theory — Mel Robbins",
    "Spirit Talker — Shawn Leonard",
    "Walking with Your Spirit Totem Animals — Shawn Leonard",
    "You Are the Medicine — Asha Frost",
    "Ho'oponopono: The Hawaiian Ritual of Forgiveness — Ulrich E. Dupree",
    "Perfect Just as You Are — Pema Chödrön",
    "The Book of Stones — Robert Simmons & Naisha Ahsian",
    "Animal Spirit Guides — Steven D. Farmer",
    "The Book of Awakening — Nepo",
    "Tarot for Light Seers — Chris-Anne",
    "Becoming Supernatural — Dr. Joe Dispenza",
    "Earth Frequency — Alvarez",
    "The Healing Power of Pyramids — Joseph Andrew Marcello",
    "Modern Guide to Energy Clearing — Moore",
    "All That the Rain Promises and More — Arora",
    "Step Into Your Movie — Vernon",
    "Home at Last: Happy Child Stories — Cheryvolu",
    "A Shelter of Her Own — Kumari MacGregor",
    "Option B — Sheryl Sandberg & Adam Grant",
    "Shadowscapes Companion — Stephanie Pui-Mun Law",
    "The Once Upon a Time World — Hope West",
    "An Intexact Science of the Heart — Alfred Pearce",
    "Backpacks and Bra Straps — Savannah Grace",
    "More Together Than Alone — Mark Nepo",
    "Cracking the Rich Code Vol. 16 — Jim Britt & Kevin Harrington",
    "Shero — Rebecca M",
    "Dolphins Whales and Magical Tales",
    "Redefining Success — W. Brett Wilson",
    "Make Your Own Rules Diet — Tara Stiles",
    "Naked Chocolate — David Wolfe & Shazzie",
    "The Essential Flower Essence Handbook — Lila Devi Stone",
    "The Cancer Survivor's Garden Companion — Peterson",
    "Crazy Sexy Cancer Survivor — Carr",
    "The Art of Fiction — John",
    "The Sidewalk Artist — Gina Buonaguro & Gianni",
    "Angry All the Time — Ronald Potter-Efron",
    "Glad No Matter What — Sark",
    "Reclaim Your Power — Dane Stevens",
    "The Truth About Cancer — Ty M. Bollinger",
    "Weightless — Gregg McBride",
    "Your Soul's Whispers: A Journey of Awakening — Debbie Johnson",
    "We Could Stay Here All Night — DEBBIE",
    "Law of Attraction — Michael Losier",
    "Herb Magic — Scott",
    "I Can See Clearly Now — Dr. Wayne W. Dyer",
    "Alternative Cures — Bill Gottlieb",
    "Outliers: The Story of Success — Malcolm Gladwell",
    "The Road Less Traveled — M. Scott Peck",
    "Truth or Dare — Starhawk",
    "Healing to Age of Enlightenment — Stanley",
    "Healing Emotions — Goleman",
    "The Girl on the Train — Paula Hawkins",
    "News of the World — Paulette Jiles",
    "The Infinity Years of Avalon James — M. Middleton",
    "Rhythms and Roads — Victoria Erickson",
    "Spritual Healer to New Brunswick's Leprosy Victims — Losier",
    "Alternative Medicine Guide to Women's Health 2",
    "The Gerson Therapy — Charlotte Gerson & Morton Walker",
    "The Shadow Effect — Chopra",
    "Minding the Body",
]

# Template mapping (1=Pastel, 2=Celestial, 3=Earthy, 4=Crystal)
template_mapping = {
    "Elementary I Ching — Turner": "3",
    "The Compleat Meadmaker — Schramm": "3",
    "The Heart of Aromatherapy — Andrea Butje": "1",
    "A Gathering of Brilliant Moons — Gayley & Schapiro": "2",
    "Brightening Our Inner Skies: Yin and Yoga — Norman Blair": "1",
    "Bloom — Bronnie Ware": "1",
    "Reboot with Joe: Fully Charged — Joe Cross": "4",
    "Archangels & Ascended Masters — Doreen Virtue": "2",
    "Assertiveness for Earth Angels — Doreen Virtue": "1",
    "Essential Oils for Childbirth — Boldy": "1",
    "Your Altar — Kynes": "3",
    "The Crystal Experience": "4",
    "The Crystal Bible 3": "4",
    "The Feng Shui Bible": "3",
    "Wind and Water: Your Personal Feng Shui Journey": "3",
    "The Palmistry Bible": "2",
    "The Aromatherapy Bible": "1",
    "The Astrology Bible": "2",
    "The Mandala Bible": "2",
    "The Chakra Bible": "4",
    "The Meditation Bible": "1",
    "The Pocket Book of Stones — Robert Simmons": "4",
    "Visualizations for Self Empowerment": "1",
    "Ostara: Customs": "3",
    "Nordic Runes — Mountfort": "3",
    "The Empath's Survival Guide — Judith Orloff MD": "1",
    "Awakening Your Inner Shaman — Marcela Lobos": "3",
    "A Handbook of Saxon Sorcery & Magic — Shumsky": "3",
    "Awaken Your Divine Intuition — Shumsky": "2",
    "The Art of Manifesting — Colette Baron-Reid": "2",
    "The Let Them Theory — Mel Robbins": "1",
    "Spirit Talker — Shawn Leonard": "2",
    "Walking with Your Spirit Totem Animals — Shawn Leonard": "3",
    "You Are the Medicine — Asha Frost": "1",
    "Ho'oponopono: The Hawaiian Ritual of Forgiveness — Ulrich E. Dupree": "3",
    "Perfect Just as You Are — Pema Chödrön": "1",
    "The Book of Stones — Robert Simmons & Naisha Ahsian": "4",
    "Animal Spirit Guides — Steven D. Farmer": "3",
    "The Book of Awakening — Nepo": "1",
    "Tarot for Light Seers — Chris-Anne": "2",
    "Becoming Supernatural — Dr. Joe Dispenza": "2",
    "Earth Frequency — Alvarez": "2",
    "The Healing Power of Pyramids — Joseph Andrew Marcello": "4",
    "Modern Guide to Energy Clearing — Moore": "4",
    "All That the Rain Promises and More — Arora": "3",
    "Step Into Your Movie — Vernon": "1",
    "Home at Last: Happy Child Stories — Cheryvolu": "1",
    "A Shelter of Her Own — Kumari MacGregor": "1",
    "Option B — Sheryl Sandberg & Adam Grant": "1",
    "Shadowscapes Companion — Stephanie Pui-Mun Law": "2",
    "The Once Upon a Time World — Hope West": "2",
    "An Intexact Science of the Heart — Alfred Pearce": "2",
    "Backpacks and Bra Straps — Savannah Grace": "1",
    "More Together Than Alone — Mark Nepo": "1",
    "Cracking the Rich Code Vol. 16 — Jim Britt & Kevin Harrington": "1",
    "Shero — Rebecca M": "1",
    "Dolphins Whales and Magical Tales": "2",
    "Redefining Success — W. Brett Wilson": "1",
    "Make Your Own Rules Diet — Tara Stiles": "1",
    "Naked Chocolate — David Wolfe & Shazzie": "1",
    "The Essential Flower Essence Handbook — Lila Devi Stone": "1",
    "The Cancer Survivor's Garden Companion — Peterson": "1",
    "Crazy Sexy Cancer Survivor — Carr": "1",
    "The Art of Fiction — John": "2",
    "The Sidewalk Artist — Gina Buonaguro & Gianni": "2",
    "Angry All the Time — Ronald Potter-Efron": "1",
    "Glad No Matter What — Sark": "1",
    "Reclaim Your Power — Dane Stevens": "1",
    "The Truth About Cancer — Ty M. Bollinger": "1",
    "Weightless — Gregg McBride": "1",
    "Your Soul's Whispers: A Journey of Awakening — Debbie Johnson": "1",
    "We Could Stay Here All Night — DEBBIE": "2",
    "Law of Attraction — Michael Losier": "2",
    "Herb Magic — Scott": "3",
    "I Can See Clearly Now — Dr. Wayne W. Dyer": "2",
    "Alternative Cures — Bill Gottlieb": "1",
    "Outliers: The Story of Success — Malcolm Gladwell": "1",
    "The Road Less Traveled — M. Scott Peck": "3",
    "Truth or Dare — Starhawk": "3",
    "Healing to Age of Enlightenment — Stanley": "4",
    "Healing Emotions — Goleman": "1",
    "The Girl on the Train — Paula Hawkins": "2",
    "News of the World — Paulette Jiles": "3",
    "The Infinity Years of Avalon James — M. Middleton": "2",
    "Rhythms and Roads — Victoria Erickson": "1",
    "Spritual Healer to New Brunswick's Leprosy Victims — Losier": "3",
    "Alternative Medicine Guide to Women's Health 2": "1",
    "The Gerson Therapy — Charlotte Gerson & Morton Walker": "1",
    "The Shadow Effect — Chopra": "2",
    "Minding the Body": "4",
}

# Overlay colors per template (semi-transparent tint)
overlay_colors = {
    "1": (90, 50, 120, 140),   # violet tint
    "2": (20, 30, 80, 130),    # deep blue tint
    "3": (40, 60, 30, 130),    # earthy green tint
    "4": (60, 20, 80, 140),    # crystal purple tint
}

# Text outline color per template
outline_colors = {
    "1": (60, 20, 90),
    "2": (10, 15, 60),
    "3": (30, 45, 20),
    "4": (45, 10, 65),
}

template_folder = "assets/shopify"
output_folder = "assets/shopify"
os.makedirs(output_folder, exist_ok=True)


def get_font(size):
    """Try to load a nice font, fall back to default."""
    for name in ["arialbd.ttf", "arial.ttf", "DejaVuSans-Bold.ttf", "segoeui.ttf"]:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_outlined_text(draw, xy, text, font, fill, outline_color, outline_width=3):
    """Draw text with a colored outline/border for readability."""
    x, y = xy
    # Draw outline by offsetting in all directions
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx * dx + dy * dy <= outline_width * outline_width:
                draw.text((x + dx, y + dy), text, font=font, fill=outline_color, anchor="mm")
    # Draw main text on top
    draw.text(xy, text, font=font, fill=fill, anchor="mm")


def fit_title(title, img_width, max_width_ratio=0.85):
    """Split title into lines and find the best font size to fit centered."""
    max_w = int(img_width * max_width_ratio)

    # Try font sizes from large to small
    for font_size in range(100, 28, -2):
        font = get_font(font_size)
        # Wrap text to fit width
        words = title.split()
        lines = []
        current = ""
        for word in words:
            test = f"{current} {word}".strip()
            bbox = font.getbbox(test)
            if bbox[2] - bbox[0] > max_w and current:
                lines.append(current)
                current = word
            else:
                current = test
        if current:
            lines.append(current)

        # Check all lines fit
        all_fit = all(
            (font.getbbox(line)[2] - font.getbbox(line)[0]) <= max_w
            for line in lines
        )
        if all_fit and len(lines) <= 4:
            return lines, font, font_size

    # Fallback
    font = get_font(32)
    return [title], font, 32


print("Generating book thumbnails...\n")

for title in book_list:
    tmpl_num = template_mapping.get(title, "1")
    template_path = os.path.join(template_folder, f"temp{tmpl_num}.png")

    if not os.path.exists(template_path):
        print(f"  ⚠ Template {template_path} not found — skipping: {title}")
        continue

    # Load template as RGBA
    img = Image.open(template_path).convert("RGBA")
    w, h = img.size

    # Apply semi-transparent overlay
    ov_color = overlay_colors.get(tmpl_num, (60, 30, 80, 130))
    overlay = Image.new("RGBA", (w, h), ov_color)
    img = Image.alpha_composite(img, overlay)

    # Create draw on the composited image
    draw = ImageDraw.Draw(img)

    # ── Top: "Utopia Sacred Space" ──
   # top_font = get_font(42)
   # draw_outlined_text(draw, (w // 2, 80), "Utopia Sacred Space", top_font,
    #                   fill="#F5E8C7", outline_color=(30, 15, 50), outline_width=2)

    # Split title and author
    if " — " in title:
        book_name, author = title.split(" — ", 1)
    else:
        book_name = title
        author = None

    # ── Center: Book Title ──
    lines, title_font, fsize = fit_title(book_name, w)
    line_height = int(fsize * 1.3)
    total_text_h = line_height * len(lines)
    # If author exists, shift title up a bit to make room
    author_space = 60 if author else 0
    start_y = (h // 2) - (total_text_h // 2) + (line_height // 2) - (author_space // 2)

    ol_color = outline_colors.get(tmpl_num, (40, 20, 60))
    for i, line in enumerate(lines):
        y = start_y + i * line_height
        draw_outlined_text(draw, (w // 2, y), line, title_font,
                           fill="#FFFFFF", outline_color=ol_color, outline_width=3)

    # ── Author name (smaller, below title) ──
    if author:
        author_font = get_font(36)
        author_y = start_y + len(lines) * line_height + 20
        draw_outlined_text(draw, (w // 2, author_y), author, author_font,
                           fill="#F5E8C7", outline_color=ol_color, outline_width=2)

    # ── Bottom: "utopiastore.ca" ──
    #bot_font = get_font(32)
    #draw_outlined_text(draw, (w // 2, h - 70), "utopiastore.ca", bot_font,
     #                  fill="#F5E8C7", outline_color=(30, 15, 50), outline_width=2)

    # Save as JPG
    clean = (title.lower()
             .replace(" — ", "-").replace(":", "").replace("&", "and")
             .replace("'", "").replace("'", "").replace(" ", "-").replace(".", ""))
    filename = f"{clean}-utopia-sacred-space.jpg"
    save_path = os.path.join(output_folder, filename)
    img.convert("RGB").save(save_path, quality=95)
    print(f"  ✅ {filename}  (template {tmpl_num}, font {fsize}px, {len(lines)} lines)")

print(f"\n🎉 Done! {len(book_list)} thumbnails in ./{output_folder}/")
