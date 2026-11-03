"""Static teaching contracts only; never runs a VPS command."""
from pathlib import Path
from html import unescape
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
lessons = ['0005-manual-service-setup.html', '0006-service-cicd.html', '0007-service-recovery.html']
references = ['manual-service-playbook.html', 'service-cicd-playbook.html', 'service-recovery-playbook.html']
for name in lessons + references:
    path = ROOT / ('lessons' if name in lessons else 'reference') / name
    text = path.read_text()
    for phrase in ('Hermes', 'Pi', 'n8n', 'troubleshoot', 'follow-up'):
        assert phrase.lower() in text.lower(), (name, phrase)
    for block in re.findall(r'<pre><code data-shell="bash">(.*?)</code></pre>', text, re.S):
        subprocess.run(['bash', '-n'], input=unescape(block), text=True, check=True)
manual = (ROOT / 'reference' / references[0]).read_text()
for phrase in ('npm install -g', '--ignore-scripts', 'hermes update', 'docker compose config -q', 'original project', 'Do not', 'backup'):
    assert phrase in manual, phrase
ci = (ROOT / 'reference' / references[1]).read_text()
for phrase in ('workflow_dispatch', 'required reviewers', 'StrictHostKeyChecking=yes', 'cancel-in-progress: false', 'manual deployment', 'forced command', 'not a ready-to-run'):
    assert phrase in ci, phrase
recovery = (ROOT / 'reference' / references[2]).read_text()
for phrase in ('migration', 'encryption key', 'isolated', 'RPO', 'RTO', 'original volume', 'Do not', 'off-server'):
    assert phrase in recovery, phrase
for path in [ROOT / 'index.html', *sorted((ROOT / 'lessons').glob('*.html')), *sorted((ROOT / 'reference').glob('*.html'))]:
    text = path.read_text()
    for label in ('Primary', 'Learning path'):
        nav = re.search(r'<nav aria-label="' + label + r'">(.*?)</nav>', text, re.S)[1]
        for lesson in lessons:
            assert lesson in nav, (path, label, lesson)
print('PASS: three lifecycle lessons/references, troubleshooting, safety contracts, navigation and Bash syntax (not executed)')
