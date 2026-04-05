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
    nav.style.background = s ? 'rgba(26,20,37,.92)' : '';
    nav.style.backdropFilter = s ? 'blur(12px)' : '';
    nav.style.borderBottom = s ? '1px solid rgba(155,127,212,.12)' : '';
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
