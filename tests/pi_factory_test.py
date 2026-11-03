"""Content contracts for the learner-run factory setup (not a live install test)."""
from pathlib import Path
import re
import subprocess
from html import unescape

ROOT = Path(__file__).resolve().parents[1]
lesson = ROOT / 'lessons/0003-pi-software-factory.html'
playbook = ROOT / 'reference/pi-factory-playbook.html'
assert lesson.exists() and playbook.exists(), 'Lesson 3 and its playbook must exist'
text = playbook.read_text()
for anchor in ('preflight', 'account', 'prerequisites', 'node', 'tools', 'workspace',
               'verify', 'launch', 'project', 'reconnect', 'troubleshoot'):
    assert f'id="{anchor}"' in text, anchor
for phrase in ('local-only', 'no sudo', 'not a sandbox', 'reboot', 'protocol',
               '22.19', 'No Mistakes ≥1.46.0', 'at least 0.8.0',
               'integration version 2 or newer', 'get --lease', 'MISSING:', 'OUTDATED:',
               'Leave the result unmerged', 'vps_learning.pub',
               'ssh -o ForwardAgent=no -i', 'scp -o ForwardAgent=no -i',
               'Do not', 'pi -c', 'Ctrl-b', 'headless', 'recovery'):
    assert phrase in text, phrase
assert 'curl -fsSL https://' in text
assert '| sh' not in unescape(text), 'Installers must be reviewed before execution'
assert 'npm config set prefix' not in text, 'nvm cannot share a custom npm prefix'
for path in [ROOT / 'index.html', *sorted((ROOT / 'lessons').glob('*.html')), *sorted((ROOT / 'reference').glob('*.html'))]:
    assert '0003-pi-software-factory.html' in path.read_text(), (path, 'missing lesson navigation')
blocks = re.findall(r'<pre><code data-shell="bash">(.*?)</code></pre>', text, re.S)
assert len(blocks) >= 10, 'Shell examples must be syntax-checked'
for block in blocks:
    subprocess.run(['bash', '-n'], input=unescape(block), text=True, check=True)
print(f'PASS: factory content checkpoints, navigation and {len(blocks)} Bash syntax checks (not executed)')
