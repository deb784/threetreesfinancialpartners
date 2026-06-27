document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      const open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    links.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        links.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  document.querySelectorAll('.faq-item').forEach((item) => {
    const summary = item.querySelector('summary');
    const plus = item.querySelector('.faq-plus');
    const sync = () => { if (plus) plus.textContent = item.open ? '−' : '+'; };
    sync();
    item.addEventListener('toggle', sync);
    if (summary) summary.addEventListener('click', () => setTimeout(sync, 0));
  });
});
