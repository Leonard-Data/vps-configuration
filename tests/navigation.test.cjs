const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const sidebars = Array.from({ length: 2 }, () => ({
  open: true,
  focused: false,
  handlers: {},
  addEventListener(name, handler) { this.handlers[name] = handler; },
  querySelector() { return { focus: () => { this.focused = true; } }; }
}));
const menus = Array.from({ length: 2 }, () => ({
  open: false,
  focused: false,
  attrs: {},
  handlers: {},
  addEventListener(name, handler) { this.handlers[name] = handler; },
  querySelector(selector) {
    return selector === 'summary' && {
      setAttribute: (name, value) => { this.attrs[name] = value; },
      focus: () => { this.focused = true; }
    };
  }
}));
const media = { matches: true, addEventListener: (_, handler) => { media.change = handler; } };
const document = {
  handlers: {},
  querySelectorAll: (selector) => selector.includes('nav-menu') ? menus : sidebars,
  addEventListener(name, handler) { this.handlers[name] = handler; }
};
vm.runInNewContext(fs.readFileSync(require.resolve('../assets/navigation.js'), 'utf8'), {
  document,
  window: { matchMedia: () => media }
});

// Two-level header menus: one open at a time, close on outside click and Escape.
menus[0].open = true;
menus[0].handlers.toggle();
assert.equal(menus[0].attrs['aria-expanded'], 'true', 'open menu reports expanded');
assert.equal(menus[1].attrs['aria-expanded'], 'false');
menus[1].open = true;
menus[1].handlers.toggle();
assert.equal(menus[0].open, false, 'opening one header menu closes the other');
assert.equal(menus[1].attrs['aria-expanded'], 'true');
document.handlers.click({ target: { closest: () => ({}) } });
assert.equal(menus[1].open, true, 'clicks inside a menu keep it open');
document.handlers.click({ target: { closest: () => null } });
assert.equal(menus[1].open, false, 'outside clicks close header menus');
menus[0].open = true;
document.handlers.keydown({ key: 'Escape' });
assert.equal(menus[0].open, false, 'Escape closes the header menu');
assert.equal(menus[0].focused, true, 'Escape returns focus to the menu summary');

for (const sidebar of sidebars) {
  assert.equal(sidebar.open, false, 'mobile starts collapsed');
  sidebar.open = true;
  sidebar.handlers.click({ target: { closest: () => null } });
  assert.equal(sidebar.open, true, 'non-link clicks do not close the panel');
  sidebar.handlers.click({ target: { closest: () => ({}) } });
  assert.equal(sidebar.open, false, 'mobile navigation closes after selection');
  sidebar.open = true;
  sidebar.handlers.keydown({ key: 'Escape' });
  assert.equal(sidebar.open, false);
  assert.equal(sidebar.focused, true, 'Escape returns focus to its own disclosure');
}
media.matches = false;
media.change();
for (const sidebar of sidebars) {
  assert.equal(sidebar.open, true, 'desktop navigation is expanded after resize');
  sidebar.handlers.click({ target: { closest: () => ({}) } });
  assert.equal(sidebar.open, true, 'desktop navigation stays expanded');
}
media.matches = true;
media.change();
assert.ok(sidebars.every(sidebar => !sidebar.open), 'returning to mobile collapses both panels');
console.log('PASS: two-level header menus and both navigation panels, link selection, Escape focus and breakpoint changes');
