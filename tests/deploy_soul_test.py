"""Exercise the downloadable deployment example without touching a real Hermes home."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'examples/hermes-ops/deploy_soul.py'

class DeploymentTests(unittest.TestCase):
    def run_deploy(self, home, content, *args):
        return subprocess.run(['python3', str(SCRIPT), *args], input=content,
                              env={**os.environ, 'HOME': str(home)}, capture_output=True)

    def test_install_backup_and_invalid_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            self.assertEqual(self.run_deploy(home, b'# First\nBe helpful.\n').returncode, 0)
            target = home / '.hermes/SOUL.md'
            self.assertEqual(target.stat().st_mode & 0o777, 0o600)
            self.assertEqual(self.run_deploy(home, b'# Second\nBe clear.\n').returncode, 0)
            self.assertEqual((target.parent / 'SOUL.md.previous').read_bytes(), b'# First\nBe helpful.\n')
            for bad in (b'', b'no heading', b'# Nul\x00', b'# Bad\xff', b'# ' + b'x' * 16384):
                self.assertNotEqual(self.run_deploy(home, bad).returncode, 0)
                self.assertEqual(target.read_bytes(), b'# Second\nBe clear.\n')

    def test_check_only_and_symlink_rejection(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            self.assertEqual(self.run_deploy(home, b'# Valid\n', '--check').returncode, 0)
            self.assertFalse((home / '.hermes').exists())
            (home / '.hermes').mkdir()
            outside = home / 'outside'
            outside.write_text('untouched')
            (home / '.hermes/SOUL.md').symlink_to(outside)
            self.assertNotEqual(self.run_deploy(home, b'# Valid\n').returncode, 0)
            self.assertEqual(outside.read_text(), 'untouched')

if __name__ == '__main__':
    unittest.main()
