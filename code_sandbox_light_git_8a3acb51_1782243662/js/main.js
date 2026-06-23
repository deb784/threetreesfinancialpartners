/* =============================================================
   THREE TREES — JAVASCRIPT MAIN
   ============================================================= */

(function () {
  'use strict';

  /* ─── Sticky Header ──────────────────────────────────────── */
  const header = document.getElementById('site-header');

  function handleScroll() {
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  /* ─── Mobile Nav Toggle ──────────────────────────────────── */
  const navToggle = document.querySelector('.nav-toggle');
  const navLinks  = document.querySelector('.nav-links');

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      const isOpen = navLinks.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen);
      // Animate hamburger → X
      navToggle.classList.toggle('active', isOpen);
    });

    // Close nav when a link is clicked
    navLinks.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        navLinks.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        navToggle.classList.remove('active');
      });
    });

    // Close nav on outside click
    document.addEventListener('click', function (e) {
      if (!header.contains(e.target)) {
        navLinks.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        navToggle.classList.remove('active');
      }
    });
  }

  /* ─── Smooth-scroll offset for fixed header ─────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (!targetId || targetId === '#') return;

      const target = document.querySelector(targetId);
      if (!target) return;

      e.preventDefault();
      const headerHeight = header ? header.offsetHeight : 80;
      const targetTop    = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;

      window.scrollTo({ top: targetTop, behavior: 'smooth' });
    });
  });

  /* ─── Scroll-reveal Animation ────────────────────────────── */
  const revealElements = document.querySelectorAll(
    '.tree-card, .shield-card, .seminar-card, .testimonial-card, ' +
    '.team-card, .faq-item, .vision-feature-item, ' +
    '.hero-content, .hero-image, .methodology-infographic, ' +
    '.shield-intro-text, .shield-intro-graphic, .identity-text, .identity-image, ' +
    '.contact-form'
  );

  revealElements.forEach(function (el) {
    el.style.opacity    = '0';
    el.style.transform  = 'translateY(30px)';
    el.style.transition = 'opacity 0.65s ease, transform 0.65s ease';
  });

  const revealObserver = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry, i) {
        if (entry.isIntersecting) {
          // Stagger children of the same parent
          const parent      = entry.target.parentElement;
          const siblings    = parent ? Array.from(parent.children) : [];
          const idx         = siblings.indexOf(entry.target);
          const delay       = idx * 80;

          setTimeout(function () {
            entry.target.style.opacity   = '1';
            entry.target.style.transform = 'translateY(0)';
          }, delay);

          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -60px 0px' }
  );

  revealElements.forEach(function (el) {
    revealObserver.observe(el);
  });

  /* ─── Contact Form ───────────────────────────────────────── */
  const contactForm   = document.getElementById('contact-form');
  const successMsg    = document.getElementById('form-success');

  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();

      // Basic validation
      const required = contactForm.querySelectorAll('[required]');
      let valid = true;

      required.forEach(function (field) {
        field.style.borderColor = '';
        if (!field.value.trim()) {
          valid = false;
          field.style.borderColor = '#e74c3c';
          field.focus();
        }
        // Email check
        if (field.type === 'email' && field.value.trim()) {
          const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailRe.test(field.value.trim())) {
            valid = false;
            field.style.borderColor = '#e74c3c';
          }
        }
      });

      if (!valid) return;

      // Show success state
      const submitBtn = contactForm.querySelector('.form-submit-btn');
      submitBtn.disabled    = true;
      submitBtn.textContent = 'Sending…';

      // Simulate async submission, then redirect to thank-you page
      setTimeout(function () {
        contactForm.reset();
        // Redirect to the dedicated thank-you confirmation page
        window.location.href = 'thank-you.html';
      }, 1200);
    });

    // Remove red border on input
    contactForm.querySelectorAll('input, select, textarea').forEach(function (field) {
      field.addEventListener('input', function () {
        field.style.borderColor = '';
      });
    });
  }

  /* ─── Active Nav Highlighting ────────────────────────────── */
  const sections = document.querySelectorAll('section[id]');
  const navItems = document.querySelectorAll('.nav-links li a[href^="#"]');

  function setActiveNav() {
    const scrollPos    = window.scrollY + 120;
    let currentSection = '';

    sections.forEach(function (section) {
      if (section.offsetTop <= scrollPos) {
        currentSection = section.id;
      }
    });

    navItems.forEach(function (link) {
      link.classList.remove('active');
      const href = link.getAttribute('href').substring(1);
      if (href === currentSection) {
        link.classList.add('active');
      }
    });
  }

  window.addEventListener('scroll', setActiveNav, { passive: true });

  /* ─── FAQ Keyboard Accessibility ────────────────────────── */
  document.querySelectorAll('.faq-question').forEach(function (summary) {
    summary.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        summary.closest('details').toggleAttribute('open');
      }
    });
  });

  /* ─── Testimonials simple auto-scroll hint (mobile) ─────── */
  // No-op: grid handles layout; pointer events sufficient on desktop/mobile

  /* ─── Hamburger icon animation CSS ──────────────────────── */
  const style = document.createElement('style');
  style.textContent = `
    .nav-links a.active {
      color: var(--forest-green) !important;
      background: var(--cream) !important;
    }
    .nav-toggle.active span:nth-child(1) {
      transform: translateY(7px) rotate(45deg);
    }
    .nav-toggle.active span:nth-child(2) {
      opacity: 0;
      transform: scaleX(0);
    }
    .nav-toggle.active span:nth-child(3) {
      transform: translateY(-7px) rotate(-45deg);
    }
    .nav-toggle span {
      transition: transform 0.28s ease, opacity 0.2s ease;
    }
  `;
  document.head.appendChild(style);

  /* ─── Scroll progress bar ────────────────────────────────── */
  const progressBar = document.createElement('div');
  progressBar.id = 'scroll-progress';
  Object.assign(progressBar.style, {
    position:        'fixed',
    top:             '0',
    left:            '0',
    height:          '3px',
    background:      'linear-gradient(90deg, #b09556, #c9ac6a)',
    width:           '0%',
    zIndex:          '9999',
    transition:      'width 0.1s linear',
    pointerEvents:   'none',
  });
  document.body.prepend(progressBar);

  window.addEventListener('scroll', function () {
    const docHeight    = document.documentElement.scrollHeight - window.innerHeight;
    const scrolled     = (window.scrollY / docHeight) * 100;
    progressBar.style.width = scrolled + '%';
  }, { passive: true });

})();
