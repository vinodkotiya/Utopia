// ── Utopia Store — Shared JS ──

// ── CRITICAL ──
const nav = document.getElementById('nav');
const orbs = document.querySelectorAll('.orb');
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// Hamburger
const burger = document.getElementById('navBurger');
const overlay = document.getElementById('navOverlay');
function toggleMenu() {
  const open = overlay.classList.toggle('opacity-100');
  overlay.classList.toggle('invisible');
  overlay.classList.toggle('opacity-0');
  burger.classList.toggle('active');
  burger.setAttribute('aria-expanded', open);
  document.body.style.overflow = open ? 'hidden' : '';
}
if (burger && overlay) {
  burger.addEventListener('click', toggleMenu);
  overlay.addEventListener('click', e => {
    if (e.target === overlay || e.target.closest('a')) toggleMenu();
  });
}

// Nav scroll + parallax
window.addEventListener('scroll', () => {
  if (nav) {
    const s = window.scrollY > 60;
    nav.style.background = s ? 'rgba(26,15,46,.95)' : 'rgba(26,15,46,.85)';
    nav.style.backdropFilter = s ? 'blur(14px)' : 'blur(8px)';
    nav.style.borderBottom = s ? '1px solid rgba(91,45,142,.2)' : '1px solid rgba(91,45,142,.08)';
  }
  if (!prefersReduced && orbs.length) {
    const y = window.scrollY;
    orbs.forEach((o, i) => { o.style.transform = `translateY(${y * (.03 + i * .02)}px)`; });
  }
});

// Hero char animation
(function() {
  const t = document.querySelector('.hero-title');
  if (!t) return;
  const h = t.innerHTML, parts = h.split(/(<[^>]+>)/);
  let ci = 0, r = '';
  parts.forEach(p => {
    if (p.startsWith('<')) { r += p; }
    else { for (const c of p) { if (c === ' ') r += ' '; else { r += `<span class="char" style="animation-delay:${(.6 + ci * .04).toFixed(2)}s">${c}</span>`; } ci++; } }
  });
  t.innerHTML = r;
})();

// Newsletter
function handleSignup(e) {
  e.preventDefault();
  const msg = document.getElementById('signup-msg');
  if (msg) msg.classList.remove('hidden');
  e.target.reset();
}

// ── NON-CRITICAL ──
function initDeferred() {
  // Reveal observer
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: .12 });
  document.querySelectorAll('.reveal').forEach(el => obs.observe(el));

  // Particles
  if (!prefersReduced) {
    const f = document.getElementById('particleField');
    if (f) for (let i = 0; i < 25; i++) {
      const p = document.createElement('div');
      p.className = 'particle';
      Object.assign(p.style, { left: Math.random()*100+'%', bottom: -(Math.random()*20)+'%', animationDuration: (8+Math.random()*12)+'s', animationDelay: (Math.random()*10)+'s', width: (1.5+Math.random()*2)+'px', height: (1.5+Math.random()*2)+'px' });
      f.appendChild(p);
    }
  }

  // Proof stagger
  const m = document.getElementById('proofMasonry');
  if (m) {
    const cards = m.querySelectorAll('.proof-card');
    new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) { cards.forEach((c, i) => setTimeout(() => c.classList.add('visible'), i * 60)); } });
    }, { threshold: .1 }).observe(m);
  }

  // Intention stagger
  const g = document.querySelector('.intent-card')?.parentElement;
  if (g) {
    const cards = g.querySelectorAll('.intent-card');
    if (prefersReduced) { cards.forEach(c => c.classList.add('visible')); }
    else {
      new IntersectionObserver(entries => {
        entries.forEach(e => { if (e.isIntersecting) { cards.forEach((c, i) => setTimeout(() => c.classList.add('visible'), i * 50)); } });
      }, { threshold: .1 }).observe(g);
    }
  }

  // Particle impact glow on hero CTA
  if (!prefersReduced) {
    const btn = document.getElementById('heroShopBtn');
    if (btn) {
      function flashBtn() {
        btn.classList.add('particle-hit');
        btn.addEventListener('animationend', () => btn.classList.remove('particle-hit'), { once: true });
        setTimeout(flashBtn, 2500 + Math.random() * 4000);
      }
      setTimeout(flashBtn, 3000);
    }
  }
}

if ('requestIdleCallback' in window) requestIdleCallback(initDeferred);
else setTimeout(initDeferred, 1);


// Drag-to-scroll for .scroll-row on desktop
document.querySelectorAll('.scroll-row').forEach(row => {
  let isDown = false, startX, scrollLeft;
  row.style.cursor = 'grab';
  row.addEventListener('mousedown', e => {
    isDown = true; row.style.cursor = 'grabbing';
    startX = e.pageX - row.offsetLeft;
    scrollLeft = row.scrollLeft;
    e.preventDefault();
  });
  row.addEventListener('mouseleave', () => { isDown = false; row.style.cursor = 'grab'; });
  row.addEventListener('mouseup', () => { isDown = false; row.style.cursor = 'grab'; });
  row.addEventListener('mousemove', e => {
    if (!isDown) return;
    const x = e.pageX - row.offsetLeft;
    row.scrollLeft = scrollLeft - (x - startX) * 1.5;
  });
});

// ── Google Reviews Slider ──
(function() {
  const slider = document.getElementById('reviewsSlider');
  const dotsContainer = document.getElementById('reviewDots');
  if (!slider || !dotsContainer) return;

  const cards = slider.querySelectorAll('.review-card');
  const cardCount = cards.length;
  let currentIndex = 0;
  let autoplayTimer;

  // Calculate how many cards visible at once
  function getVisibleCount() {
    const sliderWidth = slider.offsetWidth;
    const cardWidth = cards[0].offsetWidth + 20; // 20 = gap
    return Math.floor(sliderWidth / cardWidth) || 1;
  }

  function getMaxIndex() {
    return Math.max(0, cardCount - getVisibleCount());
  }

  // Build dots
  function buildDots() {
    dotsContainer.innerHTML = '';
    const maxIdx = getMaxIndex();
    for (let i = 0; i <= maxIdx; i++) {
      const dot = document.createElement('span');
      dot.className = 'dot' + (i === currentIndex ? ' active' : '');
      dot.addEventListener('click', () => goTo(i));
      dotsContainer.appendChild(dot);
    }
  }

  function updateDots() {
    const dots = dotsContainer.querySelectorAll('.dot');
    dots.forEach((d, i) => d.classList.toggle('active', i === currentIndex));
  }

  function goTo(index) {
    const maxIdx = getMaxIndex();
    currentIndex = Math.max(0, Math.min(index, maxIdx));
    const cardWidth = cards[0].offsetWidth + 20;
    slider.scrollTo({ left: currentIndex * cardWidth, behavior: 'smooth' });
    updateDots();
    resetAutoplay();
  }

  // Expose global function for arrow buttons
  window.slideReviews = function(dir) {
    goTo(currentIndex + dir);
  };

  // Autoplay
  function resetAutoplay() {
    clearInterval(autoplayTimer);
    autoplayTimer = setInterval(() => {
      const maxIdx = getMaxIndex();
      if (currentIndex >= maxIdx) goTo(0);
      else goTo(currentIndex + 1);
    }, 5000);
  }

  // Pause on hover
  slider.addEventListener('mouseenter', () => clearInterval(autoplayTimer));
  slider.addEventListener('mouseleave', resetAutoplay);

  // Touch/drag support
  let touchStartX = 0, touchDiff = 0;
  slider.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; clearInterval(autoplayTimer); }, { passive: true });
  slider.addEventListener('touchmove', e => { touchDiff = touchStartX - e.touches[0].clientX; }, { passive: true });
  slider.addEventListener('touchend', () => {
    if (Math.abs(touchDiff) > 50) {
      goTo(currentIndex + (touchDiff > 0 ? 1 : -1));
    }
    touchDiff = 0;
    resetAutoplay();
  });

  // Init
  buildDots();
  resetAutoplay();

  // Rebuild dots on resize
  window.addEventListener('resize', () => { buildDots(); goTo(Math.min(currentIndex, getMaxIndex())); });
})();

// ── Dynamic Featured Products (Shopify) ──
(function() {
  const container = document.getElementById('featuredProducts');
  if (!container) return;

  const SHOP_URL = 'https://shop.utopiastore.ca';
  const COLLECTION = 'featured-products';
  const LIMIT = 15;

  async function fetchProducts() {
    const url = `${SHOP_URL}/collections/${COLLECTION}/products.json?limit=${LIMIT}`;
    const res = await fetch(url);
    if (!res.ok) throw new Error(`${res.status}`);
    const data = await res.json();
    return data.products;
  }

  function formatPrice(variant) {
    const amount = parseFloat(variant.price);
    if (amount === 0) return 'Free';
    return amount.toLocaleString('en-CA', { style: 'currency', currency: 'CAD' });
  }

  function escapeHtml(str) {
    const d = document.createElement('div');
    d.textContent = str;
    return d.innerHTML;
  }

  function renderProducts(products) {
    if (!products.length) {
      container.innerHTML = '<p style="text-align:center;color:var(--text-muted);grid-column:1/-1;padding:2rem">No featured products available right now.</p>';
      return;
    }
    container.innerHTML = products.map((product, i) => {
      const variant = product.variants[0];
      const image = product.images[0]?.src || '';
      const productUrl = `${SHOP_URL}/products/${product.handle}`;
      return `
        <a class="featured-card" href="${productUrl}" target="_blank" rel="noopener" style="animation-delay:${i * 60}ms">
          <img src="${image}" alt="${escapeHtml(product.title)}" loading="lazy">
          <div class="fc-body">
            <p class="fc-title">${escapeHtml(product.title)}</p>
            <p class="fc-price">${formatPrice(variant)}</p>
          </div>
        </a>`;
    }).join('');
  }

  fetchProducts()
    .then(renderProducts)
    .catch(err => {
      console.warn('Featured products fetch failed:', err);
      // Keep skeletons or show subtle message
      container.innerHTML = '<p style="text-align:center;color:var(--text-muted);grid-column:1/-1;padding:2rem;font-size:.9rem">Visit our <a href="https://shop.utopiastore.ca/collections/featured-products" target="_blank" rel="noopener" style="color:var(--violet)">shop</a> to see featured products.</p>';
    });
})();

// ── Dynamic Readers Grid (Shopify) ──
(function() {
  const container = document.getElementById('readersGrid');
  if (!container) return;

  const SHOP_URL = 'https://shop.utopiastore.ca';
  const COLLECTION = 'readers';
  const BOOKING_URL = SHOP_URL + '/products/readings-energy-work-sessions-booking-fee';

  async function fetchReaders() {
    const url = `${SHOP_URL}/collections/${COLLECTION}/products.json?limit=10`;
    const res = await fetch(url);
    if (!res.ok) throw new Error(`${res.status}`);
    const data = await res.json();
    return data.products;
  }

  function getFirstLine(bodyHtml) {
    if (!bodyHtml) return '';
    const div = document.createElement('div');
    div.innerHTML = bodyHtml;
    const text = (div.textContent || '').trim().replace(/\s+/g, ' ');
    const match = text.match(/^.*?[.!?](\s|$)/);
    let line = match ? match[0].trim() : text;
    if (line.length > 100) line = line.slice(0, 97).trim() + '…';
    return line;
  }

  function escapeHtml(str) {
    const d = document.createElement('div');
    d.textContent = str;
    return d.innerHTML;
  }

  function slugify(str) {
    return str.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
  }

  function renderReaders(products) {
    if (!products.length) {
      container.innerHTML = '<p style="text-align:center;color:var(--text-muted);grid-column:1/-1;padding:2rem">No readers available right now.</p>';
      return;
    }
    container.innerHTML = products.map((product, i) => {
      const image = product.images[0]?.src || '';
      const desc = getFirstLine(product.body_html);
      const slug = slugify(product.title);
      return `
        <div class="reader-card" style="animation-delay:${i * 80}ms">
          <img class="rc-img" src="${image}" alt="${escapeHtml(product.title)}" loading="lazy">
          <div class="rc-body">
            <p class="rc-name">${escapeHtml(product.title)}</p>
            <p class="rc-desc">${escapeHtml(desc)}</p>
            <div class="rc-btns">
              <a class="rc-btn rc-btn-outline" href="energy-work.html#bio-${slug}">Read Bio</a>
              <a class="rc-btn" href="${BOOKING_URL}" target="_blank" rel="noopener">Book Now</a>
            </div>
          </div>
        </div>`;
    }).join('');
  }

  fetchReaders()
    .then(renderReaders)
    .catch(err => {
      console.warn('Readers fetch failed:', err);
      container.innerHTML = '<p style="text-align:center;color:var(--text-muted);grid-column:1/-1;padding:2rem;font-size:.9rem">Visit our <a href="' + BOOKING_URL + '" target="_blank" rel="noopener" style="color:var(--violet)">booking page</a> to see available readers.</p>';
    });
})();

// ── Dynamic Wellness Grid (Shopify) ──
(function() {
  const container = document.getElementById('wellnessGrid');
  if (!container) return;

  const SHOP_URL = 'https://shop.utopiastore.ca';
  const COLLECTION = 'wellness';

  async function fetchWellness() {
    const url = `${SHOP_URL}/collections/${COLLECTION}/products.json?limit=10`;
    const res = await fetch(url);
    if (!res.ok) throw new Error(`${res.status}`);
    const data = await res.json();
    return data.products;
  }

  function getFirstLine(bodyHtml) {
    if (!bodyHtml) return '';
    const div = document.createElement('div');
    div.innerHTML = bodyHtml;
    const text = (div.textContent || '').trim().replace(/\s+/g, ' ');
    const match = text.match(/^.*?[.!?](\s|$)/);
    let line = match ? match[0].trim() : text;
    if (line.length > 90) line = line.slice(0, 87).trim() + '\u2026';
    return line;
  }

  function escapeHtml(str) {
    const d = document.createElement('div');
    d.textContent = str;
    return d.innerHTML;
  }

  function renderWellness(products) {
    if (!products.length) {
      container.innerHTML = '<p style="text-align:center;color:var(--text-muted);grid-column:1/-1;padding:2rem">No wellness services available right now.</p>';
      return;
    }
    container.innerHTML = products.map((product, i) => {
      const image = product.images[0]?.src || '';
      const desc = getFirstLine(product.body_html);
      const productUrl = `${SHOP_URL}/products/${product.handle}`;
      return `
        <div class="wellness-card" style="animation-delay:${i * 80}ms">
          <img class="wc-img" src="${image}" alt="${escapeHtml(product.title)}" loading="lazy">
          <div class="wc-body">
            <p class="wc-name">${escapeHtml(product.title)}</p>
            <p class="wc-desc">${escapeHtml(desc)}</p>
            <a class="wc-btn" href="${productUrl}" target="_blank" rel="noopener">Book Now ✦</a>
          </div>
        </div>`;
    }).join('');
  }

  fetchWellness()
    .then(renderWellness)
    .catch(err => {
      console.warn('Wellness fetch failed:', err);
      container.innerHTML = '<p style="text-align:center;color:var(--text-muted);grid-column:1/-1;padding:2rem;font-size:.9rem">Visit our <a href="https://shop.utopiastore.ca/collections/wellness" target="_blank" rel="noopener" style="color:var(--teal,#1A7A6E)">wellness page</a> to see available services.</p>';
    });
})();
