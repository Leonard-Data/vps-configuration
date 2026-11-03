# VPS learning workspace

Open `index.html` in a browser. No install, build or server is required; keep `assets/`, `lessons/`, `reference/` and `examples/` beside it.

- `lessons/0001-vps-mental-model.html`: short beginner lesson with three immediate-feedback questions.
- `reference/vps-field-guide.html`: printable concept reference, glossary and staged infrastructure playbook.
- `lessons/0002-hermes-agent-setup.html`: Windows-to-Ubuntu Hermes setup boundaries and three recall questions.
- `reference/hermes-setup-playbook.html`: staged SSH, installation, VS Code, repository and optional restricted CI/CD lab.
- `lessons/0003-pi-software-factory.html`: Pi/FirstMate/Herdr/Treehouse roles and three retrieval questions.
- `reference/pi-factory-playbook.html`: learner-run Ubuntu installation, primary-source corrections, scratch crew task and reconnect checks; no remote changes performed.
- `lessons/0004-n8n-vps.html`: install-option comparison, HTTPS/data mental model, harmless manual workflow and three recall questions.
- `reference/n8n-vps-playbook.html`: learner-run n8n/Caddy lab, guarded owner setup, optional authenticated webhook and offline backup/recovery checks.
- `lessons/0005-manual-service-setup.html`: manual setup, service inventory, version-selection boundaries and troubleshooting for Hermes, Pi and n8n.
- `lessons/0006-service-cicd.html`: CI versus approval-gated delivery; working configuration-only lab linked, service updater intentionally not supplied.
- `lessons/0007-service-recovery.html`: coherent recovery sets, migration risk, isolated rehearsal and retrieval questions.
- `reference/manual-service-playbook.html`, `reference/service-cicd-playbook.html`, `reference/service-recovery-playbook.html`: printable checkpoints, commands where safe, stop conditions and troubleshooting tables.
- `examples/n8n/`: reviewed teaching adaptation, not the full upstream Assistant stack; replace version/domain/key placeholders privately before use. No runtime deployment verified.
- `examples/hermes-ops/`: downloadable secret-free lab files; CI deploys only `SOUL.md`, not Hermes application upgrades.
- `MISSION.md`, `RESOURCES.md`, `NOTES.md`: teaching continuity and primary sources. No learning records yet: understanding has not been demonstrated.

The material covers OS choice, security, Docker Manager, DNS/TLS, provider versus application APIs, monitoring and backup/recovery. It does not connect to a VPS or implement a production configuration. Quiz answers are not saved.

Every page has a top navbar, a left learning-path sidebar and a right-hand table of contents. Both rails stay visible on desktop and become separate native disclosures above the content on smaller screens. The homepage includes a linked learning roadmap with separate Hermes, Pi factory and n8n tracks, followed by shared manual maintenance, CI/CD and recovery lessons; it does not track completion. Navigation remains available without JavaScript. Shared navigation styles and behavior live in `assets/navigation.css` and `assets/navigation.js`.

## Checks

```sh
node tests/quiz.test.cjs
node tests/navigation.test.cjs
python3 tests/check_html.py
python3 tests/deploy_soul_test.py
python3 tests/pi_factory_test.py
python3 tests/n8n_vps_test.py
python3 tests/service_lifecycle_test.py
node --check assets/quiz.js
node --check assets/navigation.js
# Optional: requires Firefox and geckodriver on PATH
python3 tests/check_browser.py
# Set FIREFOX_BINARY to the real executable if automatic detection fails.
```

Lifecycle checks cover six new teaching pages, troubleshooting/safety contracts, navigation and Bash example syntax only; they do not run upgrades, configure GitHub or prove restore success. The CI/CD YAML fragment is intentionally incomplete and fails closed, not a runnable app deployment workflow. n8n content checks cover safety checkpoints, example secret placeholders, private service topology, course navigation and Bash syntax, not a running Docker deployment or restore. Factory content checks cover safety checkpoints, course discoverability and Bash example syntax (without executing installation commands). Structural checks cover local links/anchors, navigation landmarks/current-page markers and quiz structure. Deployment-handler tests use temporary homes and cover validation, atomic replacement, permissions and previous-file preservation; they never access a VPS. Node tests cover quiz feedback and responsive menu behavior. Firefox browser checks cover all pages at 320, 768, 1024 and 1440 CSS pixels, horizontal overflow, both panels’ responsive states, right-hand TOC placement, keyboard menu opening and TOC selection/focus. A narrow iframe works around Firefox's minimum window width. Desktop and mobile screenshots were inspected. Real-device, cross-browser and print-layout testing were not performed.

Use browser Print to produce a PDF. External documentation needs an internet connection. Provider UI and backup entitlements may change; verify the current plan and docs before acting.
