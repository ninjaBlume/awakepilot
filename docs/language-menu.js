(() => {
  const menus = [...document.querySelectorAll('.language-switcher')];
  for (const menu of menus) {
    menu.addEventListener('toggle', () => {
      if (menu.open) menus.forEach(other => { if (other !== menu) other.open = false; });
    });
    menu.addEventListener('keydown', event => {
      if (event.key === 'Escape' && menu.open) {
        event.preventDefault();
        menu.open = false;
        menu.querySelector('summary').focus();
      }
    });
    menu.addEventListener('focusout', event => {
      // Safari can blur the summary without focusing the pressed link.
      // Let that click activate the link before dismissing the dropdown.
      if (event.relatedTarget && !menu.contains(event.relatedTarget)) menu.open = false;
    });
    for (const link of menu.querySelectorAll('a')) {
      link.addEventListener('click', () => {
        if (location.hash && !link.hash) link.hash = location.hash;
      });
    }
  }
  document.addEventListener('click', event => {
    menus.forEach(menu => { if (!menu.contains(event.target)) menu.open = false; });
  });
})();
