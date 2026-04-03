// ── CRITICAL (above-the-fold) ──

// Nav scroll effect + parallax orbs
const nav = document.getElementById('nav');
const orbs = document.querySelectorAll('.orb');
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// Hamburger menu
const burger = document.getElementById('navBurger');
const overlay = document.getElementById('navOverlay');
function toggleMenu() {
  const open = overlay.classList.toggle('open');
  burger.classList.toggle('active');
  burger.setAttribute('aria-expanded', open);
  document.body.style.overflow = open ? 'hidden' : '';
}
if (burger && overlay) {
  burger.addEventListener('click', toggleMenu);
  overlay.addEventListener('click', (e) => {
    if (e.target === overlay || e.target.closest('a')) toggleMenu();
  });
}

window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 60);
  if (!prefersReduced) {
    const y = window.scrollY;
    orbs.forEach((orb, i) => {
      const speed = 0.03 + i * 0.02;
      orb.style.transform = `translateY(${y * speed}px)`;
    });
  }
});

// Character-by-character hero title animation
(function () {
  const title = document.querySelector('.hero-title');
  if (!title) return;
  const html = title.innerHTML;
  const parts = html.split(/(<[^>]+>)/);
  let charIndex = 0;
  const baseDelay = 0.6;
  const perChar = 0.04;
  let result = '';
  parts.forEach(part => {
    if (part.startsWith('<')) {
      result += part;
    } else {
      for (const ch of part) {
        if (ch === ' ') {
          result += ' ';
        } else {
          const delay = baseDelay + charIndex * perChar;
          result += `<span class="char" style="animation-delay:${delay.toFixed(2)}s">${ch}</span>`;
        }
        charIndex++;
      }
    }
  });
  title.innerHTML = result;
})();

// ── NON-CRITICAL (deferred via requestIdleCallback) ──

function initNonCritical() {
  // Reveal on scroll
  const reveals = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.12 });
  reveals.forEach(el => observer.observe(el));

  // Generate particles
  if (!prefersReduced) {
    const field = document.getElementById('particleField');
    if (field) {
      const count = 25;
      for (let i = 0; i < count; i++) {
        const p = document.createElement('div');
        p.className = 'particle';
        p.style.left = Math.random() * 100 + '%';
        p.style.bottom = -(Math.random() * 20) + '%';
        p.style.animationDuration = (8 + Math.random() * 12) + 's';
        p.style.animationDelay = (Math.random() * 10) + 's';
        p.style.width = p.style.height = (1.5 + Math.random() * 2) + 'px';
        field.appendChild(p);
      }
    }
  }

  // Social proof card stagger
  const masonry = document.getElementById('proofMasonry');
  if (masonry) {
    const cards = masonry.querySelectorAll('.proof-card');
    const proofObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          cards.forEach((card, i) => {
            setTimeout(() => card.classList.add('visible'), i * 60);
          });
          proofObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    proofObserver.observe(masonry);
  }

  // Intention card stagger
  const grid = document.querySelector('.intentions-grid');
  if (grid) {
    const cards = grid.querySelectorAll('.intention-card');
    if (prefersReduced) {
      cards.forEach(c => c.classList.add('visible'));
    } else {
      const gridObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            cards.forEach((card, i) => {
              setTimeout(() => card.classList.add('visible'), i * 50);
            });
            gridObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.1 });
      gridObserver.observe(grid);
    }
  }
}

// Newsletter (kept global for inline onsubmit handler)
function handleSignup(e) {
  e.preventDefault();
  document.getElementById('signup-msg').style.display = 'block';
  e.target.reset();
}

// Schedule non-critical work
if ('requestIdleCallback' in window) {
  requestIdleCallback(initNonCritical);
} else {
  setTimeout(initNonCritical, 1);
}
