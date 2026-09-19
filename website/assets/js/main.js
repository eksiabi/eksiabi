// Mobile-Navigation
const navToggle = document.querySelector('.nav-toggle');
const mainNav = document.querySelector('.main-nav');

if (navToggle && mainNav) {
  navToggle.addEventListener('click', () => {
    mainNav.classList.toggle('open');
    const expanded = mainNav.classList.contains('open');
    navToggle.setAttribute('aria-expanded', String(expanded));
  });

  mainNav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => mainNav.classList.remove('open'));
  });
}

// Speisekarte: Kategorien-Tabs
const menuTabs = document.querySelectorAll('.menu-tab');
const menuPanels = document.querySelectorAll('.menu-panel');

menuTabs.forEach((tab) => {
  tab.addEventListener('click', () => {
    const target = tab.dataset.target;

    menuTabs.forEach((t) => t.classList.remove('active'));
    menuPanels.forEach((p) => p.classList.remove('active'));

    tab.classList.add('active');
    document.getElementById(target)?.classList.add('active');
  });
});

// Footer-Jahr automatisch aktualisieren
document.querySelectorAll('[data-year]').forEach((el) => {
  el.textContent = new Date().getFullYear();
});
