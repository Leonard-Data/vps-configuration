"""Optional Firefox checks; requires firefox and geckodriver on PATH."""
import base64
import json
import os
from pathlib import Path
import socket
import subprocess
import time
from urllib.request import Request, urlopen
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / '.impeccable' / 'review'
OUTPUT.mkdir(parents=True, exist_ok=True)
with socket.socket() as sock:
    sock.bind(('127.0.0.1', 0))
    port = sock.getsockname()[1]
base = f'http://127.0.0.1:{port}'

def call(method, route, data=None):
    payload = json.dumps(data).encode() if data is not None else None
    request = Request(base + route, payload, {'Content-Type': 'application/json'}, method=method)
    try:
        with urlopen(request, timeout=30) as response:
            result = json.load(response)['value']
    except HTTPError as error:
        raise AssertionError(error.read().decode()) from error
    assert not isinstance(result, dict) or 'error' not in result, result
    return result

with (OUTPUT / 'webdriver.log').open('w') as log:
    process = subprocess.Popen(['geckodriver', '--port', str(port)], stdout=log, stderr=log)
    session = None
    try:
        for attempt in range(50):
            try:
                call('GET', '/status')
                break
            except OSError:
                time.sleep(.1)
        session = call('POST', '/session', {'capabilities': {'alwaysMatch': {
            'browserName': 'firefox',
            'moz:firefoxOptions': {'args': ['-headless'], **(
                {'binary': os.environ['FIREFOX_BINARY']} if 'FIREFOX_BINARY' in os.environ else {}
            )}
        }}})['sessionId']
        route = '/session/' + session

        def js(script):
            return call('POST', route + '/execute/sync', {'script': script, 'args': []})

        def element(selector):
            result = call('POST', route + '/element', {'using': 'css selector', 'value': selector})
            return result['element-6066-11e4-a52e-4f735466cecf']

        def screenshot(name):
            image = call('GET', route + '/screenshot')
            (OUTPUT / name).write_bytes(base64.b64decode(image))

        for width in (320, 768, 1024, 1440):
            call('POST', route + '/window/rect', {'width': width, 'height': 1000})
            for page in ['index.html', *[str(p.relative_to(ROOT)) for folder in ('lessons', 'reference') for p in sorted((ROOT / folder).glob('*.html'))]]:
                call('POST', route + '/url', {'url': (ROOT / page).as_uri()})
                # Firefox enforces a minimum window width; use a real narrow browsing context.
                if js('return innerWidth') != width:
                    js(f'''const frame = document.createElement('iframe');
                        frame.src = location.href;
                        frame.style = 'position:fixed;inset:0;border:0;width:{width}px;height:1000px;background:white;z-index:999';
                        document.body.replaceChildren(frame);''')
                    frame_id = element('iframe')
                    call('POST', route + '/frame', {'id': {'element-6066-11e4-a52e-4f735466cecf': frame_id}})
                    for attempt in range(50):
                        if js("return document.readyState === 'complete' && !!document.getElementById('sidebar')"):
                            break
                        time.sleep(.1)
                state = js('''return {
                    width: innerWidth,
                    overflow: document.documentElement.scrollWidth > innerWidth,
                    open: document.getElementById('sidebar').open,
                    contentsOpen: document.getElementById('page-contents').open,
                    contentsRight: document.getElementById('page-contents').getBoundingClientRect().left >= document.getElementById('main').getBoundingClientRect().right,
                    compact: matchMedia('(max-width: 900px)').matches
                }''')
                assert state['width'] == width, (page, width, state)
                assert not state['overflow'], (page, width, state)
                assert state['open'] != state['compact'], (page, width, state)
                assert state['contentsOpen'] != state['compact'], (page, width, state)
                if not state['compact']:
                    assert state['contentsRight'], (page, width, 'Contents must be right of main')
                if not state['compact']:
                    clearance = js('''return (() => {
                        const link = document.querySelector('[aria-label="Table of contents"] a');
                        const target = document.getElementById(link.getAttribute('href').slice(1));
                        document.documentElement.style.scrollBehavior = 'auto';
                        location.hash = target.id;
                        const result = {
                            top: target.getBoundingClientRect().top,
                            headerBottom: document.querySelector('.site-header').getBoundingClientRect().bottom,
                            sidebarTop: parseFloat(getComputedStyle(document.getElementById('sidebar')).top)
                        };
                        history.replaceState(null, '', location.pathname);
                        if (document.activeElement) document.activeElement.blur();
                        scrollTo(0, 0);
                        return result;
                    })()''')
                    assert abs(clearance['sidebarTop'] - clearance['headerBottom']) <= 1, (page, width, clearance)
                    assert clearance['top'] >= clearance['headerBottom'], (page, width, 'heading behind sticky header', clearance)
                if width == 1440 and page == 'index.html': screenshot('navigation-desktop.png')
                for index in range(2):
                    js(f"document.querySelectorAll('.site-header .nav-menu')[{index}].open = true")
                    assert not js('return document.documentElement.scrollWidth > innerWidth'), (page, width, f'open header menu {index} overflows')
                    js(f"document.querySelectorAll('.site-header .nav-menu')[{index}].open = false")
                if width == 1440 and page == 'lessons/0002-hermes-agent-setup.html': screenshot('hermes-lesson-desktop.png')
                if width in (320, 1440) and page.startswith(('lessons/', 'reference/')):
                    screenshot(Path(page).stem + f'-{width}.png')
                if width == 320 and page.startswith('reference/'):
                    screenshot(Path(page).stem + '-mobile.png')
                    summary = element('#page-contents > summary')
                    call('POST', route + '/element/' + summary + '/value', {'text': '\ue007'})
                    assert js("return document.getElementById('page-contents').open"), 'Enter must open the contents' 
                    screenshot('navigation-mobile-open.png')
                    target = js("return document.querySelector('[aria-label=\"Table of contents\"] a').getAttribute('href')")
                    link = element('[aria-label="Table of contents"] a')
                    call('POST', route + '/element/' + link + '/click', {})
                    assert js(f"return !document.getElementById('page-contents').open && location.hash === {json.dumps(target)}"), 'TOC selection must navigate and collapse'
                    assert js(f"return document.activeElement.id === {json.dumps(target[1:])}"), 'TOC target must receive focus'
                call('POST', route + '/frame', {'id': None})
            print(f'PASS: all pages at requested width {width} (actual {state["width"]}); no horizontal overflow, correct menu state')
        print('PASS: keyboard menu toggle and real TOC click/focus; screenshots saved')
    finally:
        if session:
            call('DELETE', '/session/' + session)
        process.terminate()
        process.wait(timeout=10)
