"""Teaching-material contracts; no Docker, DNS, server or restore execution."""
from pathlib import Path
from html import unescape
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
lesson = (ROOT / 'lessons/0004-n8n-vps.html').read_text()
playbook = (ROOT / 'reference/n8n-vps-playbook.html').read_text()
compose = (ROOT / 'examples/n8n/compose.yml').read_text()
caddy = (ROOT / 'examples/n8n/Caddyfile').read_text()
env = (ROOT / 'examples/n8n/.env.example').read_text()
for anchor in ('preflight', 'network', 'files', 'start', 'workflow', 'webhooks',
               'backup', 'operate', 'glossary', 'report'):
    assert f'id="{anchor}"' in playbook, anchor
for phrase in ('Manual Trigger', 'Edit Fields', 'N8N_WEBHOOK_URL', '2.35.0',
               'privileged Docker-in-Docker', 'not a production'):
    assert phrase in lesson, phrase
for phrase in ('provider/network firewall', 'bypass ufw', 'owner setup',
               'off this VPS', 'Do not live-copy SQLite', 'SHA256SUMS',
               'n8n-restore', 'export:credentials --all --decrypted --output=/dev/null',
               'no credentials', 'original volume', 'network-isolated',
               'DB_TYPE', 'does not migrate', 'Never use',
               'caddy respond --listen :443', 'allowed-client success',
               'If both clients fail', 'same published Production URL',
               '404/unregistered response is inconclusive'): 
    assert phrase in playbook, phrase
# New content remains reachable from both course navigation landmarks.
for path in [ROOT / 'index.html', *sorted((ROOT / 'lessons').glob('*.html')),
             *sorted((ROOT / 'reference').glob('*.html'))]:
    text = path.read_text()
    for label in ('Primary', 'Learning path'):
        nav = re.search(r'<nav aria-label="' + label + r'">(.*?)</nav>', text, re.S)[1]
        assert '0004-n8n-vps.html' in nav, (path, label)
        assert 'n8n-vps-playbook.html' in nav, (path, label)
# Only the proxy publishes host ports; the runtime cannot access the Docker socket.
n8n, proxy = compose.split('  caddy:\n', 1)
assert not re.search(r'^    ports:', n8n, re.M)
assert "- '80:80'" in proxy and "- '443:443'" in proxy
assert 'docker.sock' not in compose and 'privileged:' not in compose
assert 'N8N_PROXY_HOPS: \'1\'' in n8n
assert 'N8N_WEBHOOK_URL: https://${N8N_HOST}/' in n8n
assert 'n8n_data:/home/node/.n8n' in n8n
assert 'reverse_proxy n8n:5678' in caddy
for key in ('N8N_VERSION', 'CADDY_VERSION', 'N8N_HOST', 'N8N_ENCRYPTION_KEY'):
    assert re.search(r'^' + key + r'=REPLACE', env, re.M), key
assert ':latest' not in compose
blocks = re.findall(r'<pre><code data-shell="bash">(.*?)</code></pre>', playbook, re.S)
assert len(blocks) >= 7
for block in blocks:
    subprocess.run(['bash', '-n'], input=unescape(block), text=True, check=True)
print(f'PASS: n8n checkpoints, navigation, private topology, placeholders and {len(blocks)} Bash syntax checks (not executed)')
