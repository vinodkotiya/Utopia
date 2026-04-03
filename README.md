# Utopia Store — Static Landing Page

## Files
- `index.html` — complete single-file landing page (HTML + CSS + JS)

## Deploy to GitHub Pages (free)
1. Create a new GitHub repo named `utopiastore.ca` (or `utopia-landing`)
2. Upload `index.html` to the repo root
3. Go to Settings → Pages → Source: Deploy from branch → main → / (root)
4. Your site will be live at `https://yourusername.github.io/utopia-landing`
5. Add a custom domain: in Pages settings add `utopiastore.ca`, then update your DNS CNAME

## DNS Setup (point utopiastore.ca to GitHub Pages)
Add these DNS records at your domain registrar:
```
A     @     185.199.108.153
A     @     185.199.109.153
A     @     185.199.110.153
A     @     185.199.111.153
CNAME www   yourusername.github.io
```
Then in GitHub Pages settings, set custom domain to `utopiastore.ca` and enable HTTPS.

## TODO before launch — swap these placeholders:

### Images (4 placeholders)
Replace the placeholder divs with real `<img>` tags:
```html
<!-- Hero: replace hero-bg radial gradients with -->
<img src="images/hero-store.jpg" alt="..." style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0.35;">

<!-- Story section: replace .story-frame placeholder div with -->
<img src="images/store-interior.jpg" alt="Utopia Sacred Space interior, North Vancouver" style="width:100%;height:100%;object-fit:cover;">

<!-- Artist slots: replace each .artist-slot with -->
<div class="artist-slot" style="background-image:url('images/artist-name.jpg');background-size:cover;background-position:center;">
  <div style="position:absolute;bottom:0;left:0;right:0;background:rgba(44,31,20,0.75);padding:0.75rem;text-align:center;">
    <span class="artist-slot-label" style="color:var(--gold-light);">Artist Name</span>
  </div>
</div>
```

### Google Maps embed
Replace the `.map-placeholder` div with your actual embed:
```html
<iframe 
  src="https://www.google.com/maps/embed?pb=YOUR_EMBED_ID" 
  width="100%" height="400" style="border:0;filter:grayscale(1)brightness(0.6);" 
  allowfullscreen="" loading="lazy">
</iframe>
```
Get your embed URL: Google Maps → search your address → Share → Embed a map → Copy HTML

### Newsletter form
Replace the form action with your actual endpoint:
- **Formspree** (free): sign up at formspree.io, get your form ID, use `action="https://formspree.io/f/YOUR_ID"`
- **Klaviyo**: use Klaviyo's embedded form script instead of the HTML form
- **ConvertKit**: same, use their embed code

### Social media links (footer)
Update Instagram and Facebook URLs to your actual handles.

### Shop URLs
All shop links point to `https://shop.utopiastore.ca/collections/...`
Once Shopify is live in June, update collection handles to match your actual Shopify collection slugs.

## SEO Notes
- Page title and meta description are pre-filled with target keywords
- All image placeholders include alt text guidance — fill these in
- Add Google Analytics: paste your GA4 `gtag` snippet before `</head>`
- Add Meta Pixel: paste your pixel code before `</head>` once set up

## Fonts
Uses Google Fonts (Cormorant Garamond + Jost) — loads from CDN, no download needed.
For fully offline/fast: download fonts and host locally in `fonts/` folder.
