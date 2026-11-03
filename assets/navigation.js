const sidebars = document.querySelectorAll('.site-layout > .sidebar');
const compactNavigation = window.matchMedia('(max-width: 900px)');
const header = document.querySelector?.('.site-header');

function syncHeaderHeight() {
  if (header) document.documentElement.style.setProperty('--header-height', `${header.offsetHeight}px`);
}

syncHeaderHeight();
if (header && 'ResizeObserver' in window) new ResizeObserver(syncHeaderHeight).observe(header);
else if (header) window.addEventListener('resize', syncHeaderHeight);

function syncNavigation() {
  sidebars.forEach((sidebar) => { sidebar.open = !compactNavigation.matches; });
}

syncNavigation();
compactNavigation.addEventListener('change', syncNavigation);

const menus = document.querySelectorAll('.site-header .nav-menu');

function syncMenus(openMenu) {
  menus.forEach((menu) => {
    if (menu !== openMenu) menu.open = false;
    menu.querySelector('summary')?.setAttribute('aria-expanded', String(menu.open));
  });
}

menus.forEach((menu) => menu.addEventListener('toggle', () => syncMenus(menu)));
document.addEventListener('click', (event) => {
  if (!event.target.closest('.site-header .nav-menu')) syncMenus();
});
document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  const open = [...menus].find((menu) => menu.open);
  syncMenus();
  open?.querySelector('summary')?.focus();
});

sidebars.forEach((sidebar) => {
  sidebar.addEventListener('click', (event) => {
    const link = event.target.closest('a');
    if (compactNavigation.matches && link) sidebar.open = false;
  });

  sidebar.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && compactNavigation.matches && sidebar.open) {
      sidebar.open = false;
      sidebar.querySelector('summary').focus();
    }
  });
});
