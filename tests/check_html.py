"""Dependency-free structural checks for the local teaching pages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.links = path, set(), []
        self.labels, self.forms, self.form, self.label = [], [], None, None
        self.lang, self.viewport, self.main, self.h1 = False, False, 0, 0
        self.nav_labels, self.current_pages, self.sidebar = [], [], False
        self.toc_links, self.in_toc = [], False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, (self.path, 'duplicate ID', attrs['id'])
            self.ids.add(attrs['id'])
        if tag == 'nav':
            self.nav_labels.append(attrs.get('aria-label'))
            self.in_toc = attrs.get('aria-label') == 'Table of contents'
        if tag == 'a' and self.in_toc: self.toc_links.append(attrs.get('href'))
        if attrs.get('aria-current') == 'page': self.current_pages.append(attrs.get('href'))
        if tag == 'details' and attrs.get('id') == 'sidebar':
            self.sidebar = 'open' in attrs
        if tag == 'html': self.lang = bool(attrs.get('lang'))
        if tag == 'meta' and attrs.get('name') == 'viewport': self.viewport = True
        if tag == 'main': self.main += 1
        if tag == 'h1': self.h1 += 1
        for key in ('href', 'src'):
            if key in attrs: self.links.append(attrs[key])
        if tag == 'form':
            self.form = {'answer': attrs.get('data-answer'), 'values': [], 'labels': [], 'status': False}
        if self.form is not None:
            if tag == 'input': self.form['values'].append(attrs.get('value'))
            if attrs.get('role') == 'status': self.form['status'] = True
            if tag == 'label': self.label = ''

    def handle_data(self, text):
        if self.label is not None: self.label += text

    def handle_endtag(self, tag):
        if tag == 'nav': self.in_toc = False
        if tag == 'label' and self.label is not None:
            self.form['labels'].append(self.label.strip())
            self.label = None
        if tag == 'form' and self.form is not None:
            self.forms.append(self.form)
            self.form = None

pages = {}
for path in [ROOT / 'index.html', *sorted((ROOT / 'lessons').glob('*.html')), *sorted((ROOT / 'reference').glob('*.html'))]:
    page = Page(path)
    page.feed(path.read_text())
    assert page.lang and page.viewport and page.main == 1 and page.h1 == 1, path
    assert {'Primary', 'Learning path', 'Table of contents'} <= set(page.nav_labels), (path, 'missing navigation')
    assert page.sidebar and page.toc_links, (path, 'missing sidebar or TOC')
    assert len(page.current_pages) == 1, (path, 'mark exactly one current page')
    assert (path.parent / page.current_pages[0]).resolve() == path.resolve(), (path, 'incorrect current page')
    assert all(link.startswith('#') for link in page.toc_links), (path, 'TOC must link within this page')
    pages[path.resolve()] = page

for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc: continue
        dest = (path.parent / unquote(url.path)).resolve() if url.path else path
        assert dest.exists(), (path, 'missing local target', link)
        if url.fragment:
            assert dest in pages and unquote(url.fragment) in pages[dest].ids, (path, 'missing anchor', link)
    for form in page.forms:
        assert form['answer'] in form['values'] and form['status'], (path, form)
        assert len(form['values']) == len(form['labels']) == 3, (path, form)
        assert len({len(label.split()) for label in form['labels']}) == 1, ('unequal answer word counts', form)

for path, page in pages.items():
    if path.parent == ROOT / 'lessons':
        answers = [form['answer'] for form in page.forms]
        assert len(answers) == 3 and len(set(answers)) == 3, (path, 'Correct answer positions must vary')
print(f'PASS: {len(pages)} HTML pages, local links/anchors, quiz structure, equal answer word counts and varied correct positions')
