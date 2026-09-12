/* ============================================================
   Samuel Kofi Agyei-Tuffour — Portfolio
   ============================================================ */

/* ---------- Mobile Nav Toggle ---------- */
const navToggle = document.querySelector('.nav-toggle');
const navMenu = document.querySelector('.nav-menu');
const navLinks = document.querySelectorAll('.nav-link');

navToggle.addEventListener('click', () => {
  navMenu.classList.toggle('active');
  navToggle.textContent = navMenu.classList.contains('active') ? '[x]' : '[=]';
});

navLinks.forEach((link) => {
  link.addEventListener('click', () => {
    navMenu.classList.remove('active');
    navToggle.textContent = '[=]';
  });
});

/* ---------- Navbar scroll ---------- */
const navbar = document.querySelector('.navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) navbar.classList.add('scrolled');
  else navbar.classList.remove('scrolled');
});

/* ---------- Fade-in on scroll ---------- */
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

document.querySelectorAll('.fade-in').forEach((el) => observer.observe(el));

/* ---------- Active link highlight ---------- */
const sections = document.querySelectorAll('section[id]');
const navLinkEls = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach((s) => {
    if (window.scrollY >= s.offsetTop - 150) current = s.id;
  });
  navLinkEls.forEach((l) => {
    l.style.color = '';
    if (l.getAttribute('href') === `#${current}`) l.style.color = 'var(--green)';
  });
});

/* ---------- Animated stat counters ---------- */
const animateCounter = (el, target) => {
  const numericTarget = parseInt(target);
  const duration = 1500;
  const start = performance.now();
  const update = (now) => {
    const p = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - p, 3);
    el.textContent = `${Math.floor(eased * numericTarget)}%`;
    if (p < 1) requestAnimationFrame(update);
  };
  requestAnimationFrame(update);
};

const statObs = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (e.isIntersecting) {
      animateCounter(e.target, e.target.dataset.target);
      statObs.unobserve(e.target);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.impact-num[data-target]').forEach((el) => statObs.observe(el));

/* ---------- Console signature ---------- */
console.log(
  '%c[ skat ]',
  'background: #00ffa3; color: #05070d; font-weight: 800; padding: 8px 14px; border-radius: 4px; font-family: monospace; font-size: 13px;'
);
console.log(
  '%cAzure Security Engineer // Identity Governance (IGA)',
  'color: #00ffa3; font-family: monospace; font-size: 12px; margin-top: 4px;'
);
console.log(
  '%cHarden your Azure identity stack? → kofileumas@gmail.com',
  'color: #8b96a8; font-family: monospace; font-size: 11px;'
);
