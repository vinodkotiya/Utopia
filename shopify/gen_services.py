"""
TIER 2 service landing pages (top-level site pages, NOT blog, NOT Shopify).
Run:  python shopify/gen_services.py
Writes <slug>.html to the workspace root.

CTAs: Book (-> energy-work.html) / Call / Contact / Ask for a quote (-> contact.html).
No prices anywhere.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(__file__))

NAV = '''  <!-- NAV -->
  <nav id="nav" class="fixed top-0 left-0 right-0 z-50 flex items-center justify-between px-6 md:px-10 py-4 transition-all" style="background:var(--bg-dark);backdrop-filter:blur(12px);border-bottom:1px solid var(--border)">
    <a href="/" style="display:inline-flex;align-items:center;text-decoration:none"><img src="assets/logo with name original.png" alt="Utopia Wellness & Gifts" style="height:44px;width:auto" loading="eager"></a>
    <ul class="hidden md:flex gap-8 list-none items-center">
      <li><a href="index.html" class="nav-link" style="font-family:var(--font-body);font-size:.72rem;text-transform:uppercase;letter-spacing:.14em;color:rgba(237,232,255,.75);text-decoration:none">Home</a></li>
      <li><a href="index.html#story" class="nav-link" style="font-family:var(--font-body);font-size:.72rem;text-transform:uppercase;letter-spacing:.14em;color:rgba(237,232,255,.75);text-decoration:none">Our Story</a></li>
      <li><a href="index.html#shop" class="nav-link" style="font-family:var(--font-body);font-size:.72rem;text-transform:uppercase;letter-spacing:.14em;color:rgba(237,232,255,.75);text-decoration:none">Shop</a></li>
      <li class="relative group">
        <span class="nav-link cursor-pointer" style="font-family:var(--font-body);font-size:.72rem;text-transform:uppercase;letter-spacing:.14em;color:rgba(237,232,255,.75)">Services &#9662;</span>
        <ul class="absolute top-full left-0 mt-2 py-2 px-1 list-none opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all" style="background:var(--bg-dark);border:1px solid var(--border);border-radius:6px;min-width:200px">
          <li><a href="energy-work.html" style="display:block;padding:.5rem 1rem;font-family:var(--font-body);font-size:.72rem;color:rgba(237,232,255,.75);text-decoration:none;white-space:nowrap">Clarity &amp; Guidance</a></li>
          <li><a href="tarot-reading-vancouver.html" style="display:block;padding:.5rem 1rem;font-family:var(--font-body);font-size:.72rem;color:rgba(237,232,255,.75);text-decoration:none;white-space:nowrap">Tarot Reading</a></li>
          <li><a href="psychic-mediums-vancouver.html" style="display:block;padding:.5rem 1rem;font-family:var(--font-body);font-size:.72rem;color:rgba(237,232,255,.75);text-decoration:none;white-space:nowrap">Psychics &amp; Mediums</a></li>
          <li><a href="reiki-north-vancouver.html" style="display:block;padding:.5rem 1rem;font-family:var(--font-body);font-size:.72rem;color:rgba(237,232,255,.75);text-decoration:none;white-space:nowrap">Reiki</a></li>
          <li><a href="energy-clearing-north-vancouver.html" style="display:block;padding:.5rem 1rem;font-family:var(--font-body);font-size:.72rem;color:rgba(237,232,255,.75);text-decoration:none;white-space:nowrap">Energy Clearing</a></li>
          <li><a href="intuitive-listening-north-vancouver.html" style="display:block;padding:.5rem 1rem;font-family:var(--font-body);font-size:.72rem;color:rgba(237,232,255,.75);text-decoration:none;white-space:nowrap">Intuitive Listening</a></li>
          <li><a href="feng-shui-vancouver.html" style="display:block;padding:.5rem 1rem;font-family:var(--font-body);font-size:.72rem;color:rgba(237,232,255,.75);text-decoration:none;white-space:nowrap">Feng Shui</a></li>
          <li><a href="meditations.html" style="display:block;padding:.5rem 1rem;font-family:var(--font-body);font-size:.72rem;color:rgba(237,232,255,.75);text-decoration:none;white-space:nowrap">Wellness</a></li>
          <li><a href="gatherings.html" style="display:block;padding:.5rem 1rem;font-family:var(--font-body);font-size:.72rem;color:rgba(237,232,255,.75);text-decoration:none;white-space:nowrap">Partner with Us</a></li>
          <li><a href="corporate-gifts-vancouver.html" style="display:block;padding:.5rem 1rem;font-family:var(--font-body);font-size:.72rem;color:rgba(237,232,255,.75);text-decoration:none;white-space:nowrap">Corporate Gifts</a></li>
          <li><a href="media.html" style="display:block;padding:.5rem 1rem;font-family:var(--font-body);font-size:.72rem;color:rgba(237,232,255,.75);text-decoration:none;white-space:nowrap">Media &amp; Press</a></li>
          <li><a href="mini-guide.html" style="display:block;padding:.5rem 1rem;font-family:var(--font-body);font-size:.72rem;color:rgba(237,232,255,.75);text-decoration:none;white-space:nowrap">Mini Guide</a></li>
          <li><a href="faq.html" style="display:block;padding:.5rem 1rem;font-family:var(--font-body);font-size:.72rem;color:rgba(237,232,255,.75);text-decoration:none;white-space:nowrap">FAQ</a></li>
        </ul>
      </li>
      <li><a href="blog/index.html" class="nav-link" style="font-family:var(--font-body);font-size:.72rem;text-transform:uppercase;letter-spacing:.14em;color:rgba(237,232,255,.75);text-decoration:none">Blog</a></li>
      <li><a href="index.html#visit" class="nav-link" style="font-family:var(--font-body);font-size:.72rem;text-transform:uppercase;letter-spacing:.14em;color:rgba(237,232,255,.75);text-decoration:none">Visit</a></li>
    </ul>
    <div class="hidden md:flex items-center gap-4">
      <a href="https://www.instagram.com/utopia_wellness_gifts/" target="_blank" rel="noopener" aria-label="Instagram"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(237,232,255,.6)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="5"/><circle cx="17.5" cy="6.5" r="1.5" fill="rgba(237,232,255,.6)" stroke="none"/></svg></a>
      <a href="https://www.facebook.com/utopiastore.ca" target="_blank" rel="noopener" aria-label="Facebook"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(237,232,255,.6)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg></a>
      <a href="https://shop.utopiastore.ca" class="btn-shimmer" style="font-family:var(--font-body);font-size:.75rem;text-transform:uppercase;letter-spacing:.12em;background:var(--violet);color:#fff;padding:.6rem 1.4rem;text-decoration:none;border-radius:4px">Shop Now</a>
    </div>
    <button id="navBurger" class="burger md:hidden flex flex-col gap-[5px] p-2 bg-transparent border-none cursor-pointer z-[201]" aria-label="Open menu" aria-expanded="false"><span style="background:#EDE8FF"></span><span style="background:#EDE8FF"></span><span style="background:#EDE8FF"></span></button>
  </nav>
  <div id="navOverlay" class="fixed inset-0 z-[200] flex items-center justify-center opacity-0 invisible" style="background:rgba(26,15,46,.97);backdrop-filter:blur(16px);transition:opacity .35s,visibility .35s">
    <ul class="list-none text-center flex flex-col gap-6">
      <li><a href="index.html" style="font-family:var(--font-display);font-size:1.6rem;color:#EDE8FF;text-decoration:none">Home</a></li>
      <li><a href="energy-work.html" style="font-family:var(--font-display);font-size:1.6rem;color:#EDE8FF;text-decoration:none">Clarity &amp; Guidance</a></li>
      <li><a href="tarot-reading-vancouver.html" style="font-family:var(--font-display);font-size:1.6rem;color:#EDE8FF;text-decoration:none">Tarot Reading</a></li>
      <li><a href="psychic-mediums-vancouver.html" style="font-family:var(--font-display);font-size:1.6rem;color:#EDE8FF;text-decoration:none">Psychics &amp; Mediums</a></li>
      <li><a href="reiki-north-vancouver.html" style="font-family:var(--font-display);font-size:1.6rem;color:#EDE8FF;text-decoration:none">Reiki</a></li>
      <li><a href="blog/index.html" style="font-family:var(--font-display);font-size:1.6rem;color:#EDE8FF;text-decoration:none">Blog</a></li>
      <li><a href="index.html#visit" style="font-family:var(--font-display);font-size:1.6rem;color:#EDE8FF;text-decoration:none">Visit</a></li>
      <li><a href="https://shop.utopiastore.ca" style="font-family:var(--font-body);font-size:1rem;text-transform:uppercase;letter-spacing:.18em;color:var(--violet-light);text-decoration:none">Shop Now</a></li>
    </ul>
  </div>'''

FOOTER = '''  <!-- FOOTER (dark) -->
  <footer class="px-6 md:px-10 py-12" style="background:var(--bg-dark)">
    <div class="max-w-5xl mx-auto grid grid-cols-2 md:grid-cols-[2fr_1fr_1fr_1fr] gap-8">
      <div class="col-span-2 md:col-span-1">
        <p style="font-family:var(--font-display);font-size:1.3rem;letter-spacing:.25em;color:#EDE8FF;margin-bottom:.75rem">U T O P I A</p>
        <small style="font-size:.8rem;font-weight:300;color:rgba(237,232,255,.4);line-height:1.8;display:block">20 years of sacred space in North Vancouver.<br>1826 Lonsdale Ave &middot; hello@utopiastore.ca<br>&copy; 2026 Utopia Wellness &amp; Gifts</small>
      </div>
      <div>
        <h4 style="font-size:.6rem;font-weight:500;letter-spacing:.3em;text-transform:uppercase;color:rgba(237,232,255,.9);margin-bottom:1.25rem">Shop</h4>
        <ul class="list-none space-y-0">
          <li><a href="https://shop.utopiastore.ca/collections/shop-by-intention" style="font-size:.82rem;font-weight:300;color:rgba(237,232,255,.6);text-decoration:none;min-height:44px;display:flex;align-items:center;line-height:2.2">By Intention</a></li>
          <li><a href="https://shop.utopiastore.ca/collections/crystals-minerals" style="font-size:.82rem;font-weight:300;color:rgba(237,232,255,.6);text-decoration:none;min-height:44px;display:flex;align-items:center;line-height:2.2">Crystals</a></li>
          <li><a href="https://shop.utopiastore.ca/collections/local-artists-makers" style="font-size:.82rem;font-weight:300;color:rgba(237,232,255,.6);text-decoration:none;min-height:44px;display:flex;align-items:center;line-height:2.2">Local Artists</a></li>
        </ul>
      </div>
      <div>
        <h4 style="font-size:.6rem;font-weight:500;letter-spacing:.3em;text-transform:uppercase;color:rgba(237,232,255,.9);margin-bottom:1.25rem">Services</h4>
        <ul class="list-none space-y-0">
          <li><a href="energy-work.html" style="font-size:.82rem;font-weight:300;color:rgba(237,232,255,.6);text-decoration:none;min-height:44px;display:flex;align-items:center;line-height:2.2">Clarity &amp; Guidance</a></li>
          <li><a href="tarot-reading-vancouver.html" style="font-size:.82rem;font-weight:300;color:rgba(237,232,255,.6);text-decoration:none;min-height:44px;display:flex;align-items:center;line-height:2.2">Tarot Reading</a></li>
          <li><a href="reiki-north-vancouver.html" style="font-size:.82rem;font-weight:300;color:rgba(237,232,255,.6);text-decoration:none;min-height:44px;display:flex;align-items:center;line-height:2.2">Reiki</a></li>
          <li><a href="mini-guide.html" style="font-size:.82rem;font-weight:300;color:rgba(237,232,255,.6);text-decoration:none;min-height:44px;display:flex;align-items:center;line-height:2.2">Mini Guide</a></li>
        </ul>
      </div>
      <div>
        <h4 style="font-size:.6rem;font-weight:500;letter-spacing:.3em;text-transform:uppercase;color:rgba(237,232,255,.9);margin-bottom:1.25rem">Connect</h4>
        <ul class="list-none space-y-0">
          <li><a href="index.html#story" style="font-size:.82rem;font-weight:300;color:rgba(237,232,255,.6);text-decoration:none;min-height:44px;display:flex;align-items:center;line-height:2.2">Our Story</a></li>
          <li><a href="contact.html" style="font-size:.82rem;font-weight:300;color:rgba(237,232,255,.6);text-decoration:none;min-height:44px;display:flex;align-items:center;line-height:2.2">Contact</a></li>
          <li class="flex items-center gap-4 min-h-[44px]">
            <a href="https://www.instagram.com/utopia_wellness_gifts/" target="_blank" rel="noopener" aria-label="Instagram"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(237,232,255,.6)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="5"/><circle cx="17.5" cy="6.5" r="1.5" fill="rgba(237,232,255,.6)" stroke="none"/></svg></a>
            <a href="https://www.facebook.com/utopiastore.ca" target="_blank" rel="noopener" aria-label="Facebook"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(237,232,255,.6)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg></a>
          </li>
        </ul>
      </div>
    </div>
    <p style="font-size:.72rem;color:rgba(237,232,255,.2);line-height:1.8;max-width:700px;margin:1.5rem auto 0;text-align:center">Utopia Wellness &amp; Gifts is North Vancouver's trusted metaphysical and crystal shop, serving the spiritual community since 2004. Tarot readings, reiki and energy healing, sound baths, and sacred space at 1826 Lonsdale Avenue.</p>
    <div class="max-w-5xl mx-auto mt-8 pt-6 flex justify-between items-center flex-wrap gap-4" style="border-top:1px solid rgba(237,232,255,.1);font-size:.68rem;font-weight:300;color:rgba(237,232,255,.35)">
      <span>Utopia Wellness &amp; Gifts &middot; North Vancouver &middot; Since 2004</span>
      <span class="flex items-center gap-4 flex-wrap">
        <a href="https://ekasmin.com" target="_blank" rel="noopener" style="color:rgba(237,232,255,.35);text-decoration:none;min-height:44px;display:inline-flex;align-items:center">Powered by Ekasmin.com</a>
      </span>
    </div>
  </footer>'''

# CTA presets
CTA_BOOK = ('energy-work.html', 'Book a Session')
CTA_QUOTE = ('contact.html', 'Ask for a Quote')


def esc_json(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = (s.replace("&amp;", "&").replace("&mdash;", "-").replace("&ndash;", "-")
           .replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&rsquo;", "'")
           .replace("&lsquo;", "'").replace("&middot;", "-"))
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return s


def build_page(p):
    title = p["title"]
    hero_sections = "".join(section_block(s) for s in p["sections"])
    faq_html = faq_block(p["faq"])
    primary_url, primary_label = p.get("primary_cta", CTA_BOOK)
    faq_schema = ('{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
                  + ",".join('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
                             % (esc_json(q), esc_json(a)) for q, a in p["faq"]) + ']}')
    service_schema = ('{"@context":"https://schema.org","@type":"Service","serviceType":"%s",'
                      '"provider":{"@type":"LocalBusiness","name":"Utopia Wellness & Gifts",'
                      '"address":{"@type":"PostalAddress","streetAddress":"1826 Lonsdale Avenue",'
                      '"addressLocality":"North Vancouver","addressRegion":"BC","postalCode":"V7M 2J9","addressCountry":"CA"}},'
                      '"areaServed":{"@type":"City","name":"North Vancouver"},'
                      '"url":"https://utopiastore.ca/%s"}') % (esc_json(p["service_type"]), p["slug"])
    breadcrumb_schema = ('{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
                         '{"@type":"ListItem","position":1,"name":"Home","item":"https://utopiastore.ca/"},'
                         '{"@type":"ListItem","position":2,"name":"%s","item":"https://utopiastore.ca/%s"}]}'
                         % (esc_json(p["breadcrumb"]), p["slug"]))
    localbiz = ('{"@context":"https://schema.org","@type":"LocalBusiness","@id":"https://utopiastore.ca/#business",'
                '"name":"Utopia Wellness & Gifts","url":"https://utopiastore.ca","telephone":"+16049848782",'
                '"address":{"@type":"PostalAddress","streetAddress":"1826 Lonsdale Avenue","addressLocality":"North Vancouver",'
                '"addressRegion":"BC","postalCode":"V7M 2J9","addressCountry":"CA"},'
                '"geo":{"@type":"GeoCoordinates","latitude":49.3256251,"longitude":-123.0719743},"priceRange":"$$"}')

    return f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Utopia Wellness &amp; Gifts North Vancouver</title>
  <meta name="description" content="{p['meta']}">
  <link rel="canonical" href="https://utopiastore.ca/{p['slug']}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title} | Utopia Wellness &amp; Gifts North Vancouver">
  <meta property="og:description" content="{p['meta']}">
  <meta property="og:url" content="https://utopiastore.ca/{p['slug']}">
  <meta property="og:image" content="https://utopiastore.ca/assets/cover.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title} | Utopia Wellness &amp; Gifts North Vancouver">
  <meta name="twitter:description" content="{p['meta']}">
  <meta name="theme-color" content="#FFFFFF">
  <link rel="apple-touch-icon" sizes="180x180" href="favicon/apple-touch-icon.png">
  <link rel="icon" type="image/png" sizes="32x32" href="favicon/favicon-32x32.png">
  <link rel="icon" href="favicon/favicon.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config={{theme:{{extend:{{colors:{{void:'#FFFFFF',deep:'#F8F5FF',card:'#FFFFFF',surface:'#F0EBFF',gold:{{DEFAULT:'#5B2D8E',light:'#7B4DB8'}},amethyst:{{DEFAULT:'#5B2D8E',dim:'#E8DFFF'}},rose:'#2D2035',sage:'#1A7A6E'}},fontFamily:{{display:['Cormorant Garamond','Georgia','serif'],body:['Jost','sans-serif']}}}}}}}}
  </script>
  <link rel="stylesheet" href="assets/css/theme-warm.css">
</head>
<body style="background:var(--bg-page);color:var(--text-body)">

{NAV}

  <!-- BREADCRUMB -->
  <section class="pt-28 pb-2 px-6" style="background:var(--bg-section)">
    <nav aria-label="Breadcrumb" class="max-w-4xl mx-auto">
      <ol class="flex items-center gap-2 list-none text-[.75rem]" style="color:rgba(45,32,53,.5)">
        <li><a href="index.html" style="color:var(--violet);text-decoration:none">Home</a></li>
        <li>&rsaquo;</li>
        <li style="color:rgba(45,32,53,.7)">{p['breadcrumb']}</li>
      </ol>
    </nav>
  </section>

  <!-- HERO -->
  <section class="pt-8 pb-[clamp(2rem,5vw,4rem)] px-6" style="background:var(--bg-section)">
    <div class="max-w-4xl mx-auto text-center">
      <span class="block mb-3" style="font-size:.65rem;text-transform:uppercase;letter-spacing:.32em;color:var(--violet)">{p['eyebrow']}</span>
      <h1 style="font-family:var(--font-display);font-size:clamp(2rem,5vw,3.4rem);font-weight:300;line-height:1.1;color:var(--text-heading)">{p['h1']}</h1>
      <p class="mt-5 mx-auto text-[clamp(0.95rem,1.9vw,1.15rem)] font-light leading-[1.9]" style="color:var(--text-body);max-width:60ch">{p['lede']}</p>
      <div class="mt-8 flex gap-4 justify-center flex-wrap">
        <a href="{primary_url}" class="btn-shimmer" style="font-size:.75rem;font-weight:500;text-transform:uppercase;letter-spacing:.15em;background:var(--violet);color:#fff;padding:.9rem 2rem;text-decoration:none;border-radius:6px">{primary_label} &rarr;</a>
        <a href="tel:16049848782" style="font-size:.75rem;font-weight:500;text-transform:uppercase;letter-spacing:.15em;color:var(--violet);background:transparent;padding:.9rem 2rem;text-decoration:none;border-radius:6px;border:1px solid var(--violet)">Call 604-984-8782</a>
      </div>
      <p class="mt-4 text-[.8rem] font-light" style="color:var(--text-muted)">In person at 1826 Lonsdale Ave, North Vancouver</p>
    </div>
  </section>

  <!-- BODY -->
  <article class="py-[clamp(2rem,5vw,4rem)] px-6" style="background:var(--bg-section)">
    <div class="max-w-3xl mx-auto">
{hero_sections}

{faq_block(p['faq'])}
    </div>
  </article>

  <!-- BOTTOM CTA -->
  <section class="py-16 px-6 border-t text-center" style="background:var(--bg-section);border-color:var(--border)">
    <div class="max-w-3xl mx-auto">
      <p style="font-family:var(--font-display);font-size:clamp(1.4rem,3vw,2rem);color:var(--text-heading);margin-bottom:.75rem">{p['cta_heading']}</p>
      <p style="font-size:.95rem;font-weight:300;color:var(--text-body);line-height:1.7;max-width:52ch;margin:0 auto 1.5rem">{p['cta_body']}</p>
      <div class="flex gap-4 justify-center flex-wrap">
        <a href="{primary_url}" class="btn-shimmer" style="font-size:.75rem;font-weight:500;text-transform:uppercase;letter-spacing:.18em;background:var(--violet);color:#fff;padding:1rem 2rem;border:1px solid var(--violet);text-decoration:none;display:inline-block;border-radius:6px">{primary_label} &rarr;</a>
        <a href="contact.html" style="font-size:.75rem;font-weight:500;text-transform:uppercase;letter-spacing:.18em;color:var(--violet);background:transparent;padding:1rem 2rem;border:1px solid var(--violet);text-decoration:none;display:inline-block;border-radius:6px">Contact Us</a>
      </div>
    </div>
  </section>

{FOOTER}

  <script src="assets/js/main.js"></script>

  <script type="application/ld+json">{service_schema}</script>
  <script type="application/ld+json">{faq_schema}</script>
  <script type="application/ld+json">{breadcrumb_schema}</script>
  <script type="application/ld+json">{localbiz}</script>
</body>
</html>
'''


def section_block(s):
    kind = s[0]
    if kind == "h2p":
        _, h, paras = s
        ps = "\n".join('      <p class="text-[clamp(0.9rem,1.8vw,1.05rem)] font-light leading-[1.9] mb-6" style="color:var(--text-body)">%s</p>' % t for t in paras)
        return ('      <h2 class="text-[clamp(1.2rem,3vw,1.7rem)] leading-[1.3] mt-10 mb-5" style="font-family:var(--font-display);color:var(--text-heading)">%s</h2>\n%s\n' % (h, ps))
    if kind == "h2ul":
        _, h, lead, items = s
        lead_html = '      <p class="text-[clamp(0.9rem,1.8vw,1.05rem)] font-light leading-[1.9] mb-4" style="color:var(--text-body)">%s</p>\n' % lead if lead else ""
        lis = "\n".join("        <li>%s</li>" % it for it in items)
        return ('      <h2 class="text-[clamp(1.2rem,3vw,1.7rem)] leading-[1.3] mt-10 mb-5" style="font-family:var(--font-display);color:var(--text-heading)">%s</h2>\n%s      <ul class="list-disc pl-6 mb-6 space-y-2 text-[clamp(0.9rem,1.8vw,1.05rem)] font-light leading-[1.9]" style="color:var(--text-body)">\n%s\n      </ul>\n' % (h, lead_html, lis))
    return ""


def faq_block(faq):
    parts = ['      <h2 class="text-[clamp(1.2rem,3vw,1.7rem)] leading-[1.3] mt-12 mb-5" style="font-family:var(--font-display);color:var(--text-heading)">Frequently Asked Questions</h2>']
    for q, a in faq:
        parts.append('      <h3 class="text-[1.1rem] leading-[1.3] mt-8 mb-3" style="font-family:var(--font-display);color:var(--text-heading)">%s</h3>' % q)
        parts.append('      <p class="text-[clamp(0.9rem,1.8vw,1.05rem)] font-light leading-[1.9] mb-6" style="color:var(--text-body)">%s</p>' % a)
    return "\n".join(parts)


PAGES = [
    {
        "slug": "reiki-north-vancouver.html",
        "title": "Reiki in North Vancouver",
        "breadcrumb": "Reiki",
        "service_type": "Reiki energy healing",
        "eyebrow": "Energy Healing",
        "h1": "Reiki in <em style=\"color:var(--violet);font-style:italic\">North Vancouver</em>",
        "meta": "Reiki sessions in North Vancouver at Utopia Wellness & Gifts on Lonsdale Ave. A gentle, hands-on energy healing practice for relaxation and balance. Book a session or call.",
        "lede": "Reiki is a gentle, hands-on energy practice that many people find deeply relaxing. Our practitioners offer Reiki sessions in a calm, private space on Lonsdale Avenue.",
        "sections": [
            ("h2p", "What Is Reiki?", [
                "Reiki is a Japanese energy practice where a practitioner places their hands lightly on or just above the body to encourage relaxation and a sense of balance. You stay fully clothed and simply rest.",
                "It is best understood as a complementary practice for relaxation and wellbeing, not a medical treatment or a substitute for care from your doctor.",
            ]),
            ("h2ul", "What a Session Feels Like", "People describe a Reiki session in different ways, and there is no single right experience. Common descriptions include:", [
                "A deep sense of calm, similar to a guided meditation.",
                "Warmth or a gentle tingling where the practitioner's hands rest.",
                "Feeling lighter or more settled afterward.",
                "Simply a quiet hour to slow down and reset.",
            ]),
            ("h2p", "Who Comes for Reiki", [
                "People come to Reiki for many reasons: to unwind after a stressful stretch, to complement other wellness practices, or simply to experience it for the first time. If you are new, our practitioner will explain everything before you begin.",
            ]),
        ],
        "faq": [
            ("What happens during a Reiki session?", "You rest fully clothed while the practitioner places their hands lightly on or just above the body. Most people find it deeply relaxing, like a quiet guided rest."),
            ("Is Reiki a medical treatment?", "No. Reiki is a complementary relaxation practice for wellbeing and is not a substitute for medical care. If you have a health concern, please see your doctor."),
            ("Do I need experience to try Reiki?", "Not at all. If it is your first time, the practitioner will walk you through what to expect before the session begins."),
            ("How do I book a Reiki session in North Vancouver?", "You can book online through our sessions page, call us at 604-984-8782, or visit us in person at 1826 Lonsdale Ave, North Vancouver."),
        ],
        "cta_heading": "Ready to try Reiki?",
        "cta_body": "Sessions are available in person at 1826 Lonsdale Ave, North Vancouver. Booking ahead is recommended.",
    },
    {
        "slug": "energy-clearing-north-vancouver.html",
        "title": "Energy Clearing & Healing in North Vancouver",
        "breadcrumb": "Energy Clearing",
        "service_type": "Energy clearing and healing",
        "eyebrow": "Energy Work",
        "h1": "Energy Clearing &amp; <em style=\"color:var(--violet);font-style:italic\">Healing</em>",
        "meta": "Energy clearing and healing sessions in North Vancouver at Utopia Wellness & Gifts. Reset after a heavy stretch with a calm, grounding practice on Lonsdale Ave. Book or call.",
        "lede": "Energy clearing is a calming practice for resetting after crowds, conflict, or a heavy week. Our practitioners offer grounding, balancing sessions in a private space on Lonsdale Avenue.",
        "sections": [
            ("h2p", "What Is Energy Clearing?", [
                "Energy clearing draws on techniques like grounding, chakra balancing, and gentle energy work to help you feel more settled and centred. It is often chosen after a period of stress, a big life change, or simply when things feel heavy.",
                "Like Reiki, it is a complementary wellbeing practice rather than a medical treatment.",
            ]),
            ("h2ul", "When People Reach for It", "There is no wrong reason to come, but people often book a session when:", [
                "They feel drained after crowds, travel, or conflict.",
                "A space or a season has felt heavy and they want a reset.",
                "They are moving through a big transition and want to feel grounded.",
                "They want to pair it with a reading or Reiki for a fuller reset.",
            ]),
            ("h2p", "How We Work", [
                "Your practitioner will talk with you first about what is going on and what you are hoping for, then tailor the session. Nothing is forced, and you are always in control of the pace.",
            ]),
        ],
        "faq": [
            ("What is an energy clearing session?", "It is a calm, grounding practice that uses techniques like chakra balancing and gentle energy work to help you feel more settled. You remain fully clothed and simply rest."),
            ("Is this the same as Reiki?", "They overlap and both are relaxation-focused energy practices. Energy clearing often leans toward grounding and resetting, while Reiki is a specific hands-on Japanese method. Your practitioner can suggest what fits."),
            ("Is energy clearing a medical treatment?", "No. It is a complementary wellbeing practice and not a substitute for medical care."),
            ("How do I book?", "Book online through our sessions page, call 604-984-8782, or visit us at 1826 Lonsdale Ave, North Vancouver."),
        ],
        "cta_heading": "Ready to reset?",
        "cta_body": "Energy clearing sessions are available in person at 1826 Lonsdale Ave, North Vancouver.",
    },
    {
        "slug": "intuitive-listening-north-vancouver.html",
        "title": "Intuitive Listening Sessions in North Vancouver",
        "breadcrumb": "Intuitive Listening",
        "service_type": "Intuitive listening session",
        "eyebrow": "Clarity & Guidance",
        "h1": "Intuitive <em style=\"color:var(--violet);font-style:italic\">Listening</em>",
        "meta": "Intuitive listening sessions in North Vancouver at Utopia Wellness & Gifts. A calm, judgment-free hour to talk something through and find clarity. Book a session or call.",
        "lede": "Sometimes you just need a calm, judgment-free space to talk something through. An intuitive listening session offers exactly that, with a practitioner who listens deeply and reflects back what they hear.",
        "sections": [
            ("h2p", "What Is an Intuitive Listening Session?", [
                "This is a quiet, supportive conversation rather than a formal reading. Our practitioner listens closely, asks gentle questions, and offers intuitive reflections to help you see a situation more clearly.",
                "It is a space for perspective and reflection, not professional counselling, therapy, or medical advice.",
            ]),
            ("h2ul", "What It Can Help With", "People book this kind of session when they want to:", [
                "Untangle a decision they keep circling.",
                "Feel heard without being rushed or judged.",
                "Get a fresh perspective on a relationship or a change.",
                "Slow down and hear their own intuition more clearly.",
            ]),
            ("h2p", "A Gentle Note", [
                "If you are going through something heavy, this session can be a supportive space, but it is not a replacement for professional mental health support. If you are in crisis, please reach out for help &mdash; in Canada you can call or text 988 for the Suicide Crisis Helpline, any time.",
            ]),
        ],
        "faq": [
            ("What is an intuitive listening session?", "It is a calm, supportive conversation where a practitioner listens deeply and offers intuitive reflections to help you find clarity. It is reflective, not a formal reading."),
            ("Is this therapy?", "No. It is a space for perspective and reflection, not professional counselling, therapy, or medical advice. If you need mental health support, please reach out to a professional."),
            ("What if I do not know what to talk about?", "That is completely fine. Many people arrive unsure. The practitioner will gently help you find the thread that matters most."),
            ("How do I book?", "Book online through our sessions page, call 604-984-8782, or visit 1826 Lonsdale Ave, North Vancouver."),
        ],
        "cta_heading": "Want a space to talk it through?",
        "cta_body": "Intuitive listening sessions are available in person at 1826 Lonsdale Ave, North Vancouver.",
    },
    {
        "slug": "tarot-reading-vancouver.html",
        "title": "Tarot Reading in North Vancouver",
        "breadcrumb": "Tarot Reading",
        "service_type": "Tarot reading",
        "eyebrow": "Clarity & Guidance",
        "h1": "Tarot Reading in <em style=\"color:var(--violet);font-style:italic\">North Vancouver</em>",
        "meta": "In-person tarot reading in North Vancouver at Utopia Wellness & Gifts on Lonsdale Ave. Experienced readers, a calm space, and honest guidance. Book a reading or call.",
        "lede": "Looking for an in-person tarot reading near Vancouver? Our experienced readers offer honest, grounded tarot sessions in a calm space on Lonsdale Avenue in North Vancouver.",
        "sections": [
            ("h2p", "In-Person Tarot on Lonsdale", [
                "A tarot reading is a conversation with the cards as a mirror. Our readers use the cards to help you reflect on a question, a relationship, or a decision &mdash; not to hand you a fixed fortune.",
                "Reading in person means real presence: you can ask questions, follow a thread, and sit with the insight in a quiet, unhurried space.",
            ]),
            ("h2ul", "What People Bring to a Reading", "You do not need a perfect question, but the best readings start with something real. People often come to explore:", [
                "Love and relationships &mdash; patterns, timing, and clarity.",
                "Work and direction &mdash; a decision or a crossroads.",
                "A big transition and what to focus on next.",
                "A general check-in when they feel stuck or foggy.",
            ]),
            ("h2p", "How to Prepare", [
                "Come with an open mind and a question or two you genuinely care about. There is no need to study the cards beforehand &mdash; your reader will guide the whole session.",
            ]),
        ],
        "faq": [
            ("Where can I get a tarot reading near Vancouver?", "Utopia Wellness & Gifts offers in-person tarot readings at 1826 Lonsdale Ave in North Vancouver, a short trip from downtown Vancouver over the bridge or SeaBus."),
            ("Do I need to prepare for a tarot reading?", "Just bring an open mind and a question or two that matter to you. Your reader will guide the rest."),
            ("Can tarot predict my future?", "Tarot is best used for reflection and clarity rather than fixed prediction. It helps you see patterns and choices, not a set-in-stone outcome."),
            ("How do I book a tarot reading?", "Book online through our sessions page, call 604-984-8782, or visit us at 1826 Lonsdale Ave, North Vancouver."),
        ],
        "cta_heading": "Ready for a reading?",
        "cta_body": "In-person tarot readings are available at 1826 Lonsdale Ave, North Vancouver. Walk-ins welcome, booking ahead recommended.",
    },
    {
        "slug": "psychic-mediums-vancouver.html",
        "title": "Psychics & Mediums in North Vancouver",
        "breadcrumb": "Psychics & Mediums",
        "service_type": "Psychic and mediumship reading",
        "eyebrow": "Clarity & Guidance",
        "h1": "Psychics &amp; Mediums in <em style=\"color:var(--violet);font-style:italic\">North Vancouver</em>",
        "meta": "See a psychic or medium in North Vancouver at Utopia Wellness & Gifts on Lonsdale Ave. Understand the difference and book an in-person session with an experienced reader.",
        "lede": "Searching for a psychic or medium near Vancouver? Our experienced readers offer in-person sessions in a calm, respectful space on Lonsdale Avenue in North Vancouver.",
        "sections": [
            ("h2p", "Psychic or Medium &mdash; Which Do You Want?", [
                "A psychic works with intuitive insight about your life, energy, and direction. A medium specifically works to connect with those who have passed. Not every reader offers both, so it helps to know which you are looking for.",
                "If you are unsure, tell us what you are hoping for and we will help match you with the right reader.",
            ]),
            ("h2ul", "What to Expect", "Every reader works a little differently, but in general you can expect:", [
                "A calm, private, judgment-free space.",
                "A reader who listens and works with your questions.",
                "Honest reflection rather than dramatic promises.",
                "Time to ask follow-up questions as things come up.",
            ]),
            ("h2p", "Our Approach", [
                "We keep our readings grounded and respectful. A good reading leaves you clearer and more settled, not frightened or dependent. Readings are for insight and comfort, not fixed predictions.",
            ]),
        ],
        "faq": [
            ("What is the difference between a psychic and a medium?", "A psychic works with intuitive insight about your life and direction. A medium specifically works to connect with those who have died. Some readers offer both."),
            ("Where can I see a psychic or medium near Vancouver?", "Utopia Wellness & Gifts offers in-person sessions at 1826 Lonsdale Ave in North Vancouver, easily reached from Vancouver by bridge or SeaBus."),
            ("How accurate are readings?", "Readings are best used for reflection, comfort, and perspective rather than guaranteed prediction. An ethical reader will never promise certainty."),
            ("How do I book a session?", "Book online through our sessions page, call 604-984-8782, or visit us at 1826 Lonsdale Ave, North Vancouver."),
        ],
        "cta_heading": "Ready to book a reading?",
        "cta_body": "In-person psychic and mediumship sessions are available at 1826 Lonsdale Ave, North Vancouver.",
    },
    {
        "slug": "feng-shui-vancouver.html",
        "title": "Feng Shui Consultations in North Vancouver",
        "breadcrumb": "Feng Shui",
        "service_type": "Feng shui consultation",
        "eyebrow": "Space & Energy",
        "h1": "Feng Shui in <em style=\"color:var(--violet);font-style:italic\">North Vancouver</em>",
        "meta": "Feng shui guidance and space-clearing tools in North Vancouver at Utopia Wellness & Gifts on Lonsdale Ave. Bring more flow and calm to your home. Ask for a quote or visit.",
        "lede": "Want your home or space to feel more balanced and calm? We offer feng shui guidance and the tools to support it, from our shop on Lonsdale Avenue in North Vancouver.",
        "sections": [
            ("h2p", "What Is Feng Shui?", [
                "Feng shui is the traditional practice of arranging a space so that energy, light, and movement flow more harmoniously. At its heart it is about intention: making a room support how you want to feel and live.",
                "You do not need to redo your whole home. Small, thoughtful shifts often make the biggest difference.",
            ]),
            ("h2ul", "How We Can Help", "Depending on what you need, we can support you with:", [
                "Guidance on flow, placement, and intention for a room or home.",
                "Crystals, salt lamps, and cleansing tools chosen for your space.",
                "Simple space-clearing rituals you can do yourself.",
                "Gift ideas for someone settling into a new home.",
            ]),
            ("h2p", "Tools In Store", [
                "Our Lonsdale shop carries crystals, sage and palo santo, salt lamps, and other tools that support a calmer space. Come in and we will help you choose what fits your intention.",
            ]),
        ],
        "faq": [
            ("Do you offer feng shui consultations?", "We offer feng shui guidance and the tools to support it. For a tailored consultation, ask us for a quote and we will let you know what we can arrange."),
            ("Do I need to change my whole home?", "No. Feng shui often works best through small, intentional shifts in placement, light, and flow rather than a full redesign."),
            ("What feng shui tools do you carry?", "Our North Vancouver shop carries crystals, salt lamps, sage, palo santo, and other space-clearing tools. Staff can help you choose for your space."),
            ("How do I get started?", "Ask for a quote through our contact page, call 604-984-8782, or visit us at 1826 Lonsdale Ave, North Vancouver."),
        ],
        "cta_heading": "Want a calmer space?",
        "cta_body": "Ask us for feng shui guidance and tools, or visit us at 1826 Lonsdale Ave, North Vancouver.",
        "primary_cta": CTA_QUOTE,
    },
    {
        "slug": "corporate-gifts-vancouver.html",
        "title": "Corporate Gifts in Vancouver",
        "breadcrumb": "Corporate Gifts",
        "service_type": "Corporate and bulk gifting",
        "eyebrow": "For Teams & Clients",
        "h1": "Corporate Gifts in <em style=\"color:var(--violet);font-style:italic\">Vancouver</em>",
        "meta": "Meaningful corporate gifts in Vancouver from Utopia Wellness & Gifts, North Vancouver. Crystals, curated gift sets, and reader stations for events. Ask for a quote.",
        "lede": "Looking for corporate gifts in Vancouver that feel considered rather than generic? We put together meaningful, curated gifts for teams and clients, and can add readers to your event.",
        "sections": [
            ("h2p", "Gifts With Meaning", [
                "Instead of another logo mug, give something people actually keep. We curate crystal sets, candles, jewelry, and intention-based gifts that feel personal, wrapped and ready for your team or clients.",
                "We can match gifts to a theme, a budget, or an occasion &mdash; just tell us what you have in mind.",
            ]),
            ("h2ul", "What We Offer for Teams", "We work with Vancouver-area businesses on:", [
                "Curated crystal and wellness gift sets, in bulk.",
                "Custom gift bundles matched to your budget and theme.",
                "Same-day wrapping and local pickup on Lonsdale.",
                "Readers or a reading station for holiday parties and client events.",
            ]),
            ("h2p", "One Point of Contact", [
                "For larger orders and events, you work with one person and receive one clean invoice. We are based on the North Shore and serve teams across Metro Vancouver.",
            ]),
        ],
        "faq": [
            ("Do you do corporate gifts in Vancouver?", "Yes. From our North Vancouver shop we curate meaningful corporate gifts for teams and clients across Metro Vancouver, with bulk options and same-day wrapping."),
            ("Can you match a budget?", "Yes. Tell us your budget, theme, and quantity, and we will put together options. Ask us for a quote and we will follow up."),
            ("Can you add readers to a company event?", "Yes. We can arrange tarot or intuitive readers for holiday parties, client events, and wellness days, with one point of contact and one invoice."),
            ("How do I request a quote?", "Use our contact page, call 604-984-8782, or visit us at 1826 Lonsdale Ave, North Vancouver."),
        ],
        "cta_heading": "Planning gifts for your team?",
        "cta_body": "Tell us your theme, budget, and timing, and we will put together options. Ask for a quote to get started.",
        "primary_cta": CTA_QUOTE,
    },
]


def main():
    for p in PAGES:
        html = build_page(p)
        with open(os.path.join(ROOT, p["slug"]), "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", p["slug"])


if __name__ == "__main__":
    main()
