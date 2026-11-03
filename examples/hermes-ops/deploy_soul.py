#!/usr/bin/env python3
"""Accept one bounded SOUL.md on stdin; install as the current user, never root."""
import os
from pathlib import Path
import shutil
import sys
import tempfile


def replace_file(target, content=None, source=None):
    fd, name = tempfile.mkstemp(dir=target.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            if source is not None:
                with source.open('rb') as original:
                    shutil.copyfileobj(original, stream)
            else:
                stream.write(content)
        os.replace(name, target)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def main():
    if sys.argv[1:] not in ([], ['--check']):
        raise ValueError('Only --check is accepted')
    payload = sys.stdin.buffer.read(16385)
    text = payload.decode('utf-8')
    if not 1 <= len(payload) <= 16384 or '\x00' in text or not text.startswith('# '):
        raise ValueError('Expected UTF-8 Markdown starting with # ; maximum 16384 bytes; no NUL')
    if sys.argv[1:] == ['--check']:
        print('PASS: SOUL.md format (not a security or behavior review)')
        return
    home = Path.home() / '.hermes'
    home.mkdir(mode=0o700, exist_ok=True)
    target = home / 'SOUL.md'
    if target.is_symlink():
        raise ValueError('Refusing a symlink at SOUL.md')
    if target.exists():
        replace_file(home / 'SOUL.md.previous', source=target)
    replace_file(target, content=payload)
    print('Installed SOUL.md; start a fresh Hermes session and test behavior')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError) as error:
        sys.exit(str(error))
