# Pi Software Factory Lesson Implementation Plan

**Goal:** Deliver approved lesson 3 and a learner-run Ubuntu VPS installation playbook; never connect to or modify the VPS.

**Architecture:** Extend the existing static course with one short lesson and one detailed printable reference. Reuse the shared CSS, navigation and quiz components, then link the addition throughout the course.

**Tech Stack:** HTML, existing CSS/JavaScript, Python and Node checks; no new runtime dependencies.

**Spec:** User-approved scope in conversation: Pi + FirstMate + Herdr + Treehouse; safe preparation, reviewed installers, model/GitHub authentication, local-only first project, detach/reconnect and retrieval practice. The user runs commands and receives guidance.

## Global Constraints
- Ubuntu 24.04 LTS and Windows client are reported, not verified.
- No live server changes, credentials, automatic pushes/merges or inferred mastery.
- Keep the short conceptual lesson separate from the longer installation procedure.
- Cite current primary documentation; distinguish upstream requirements from teaching choices.
- Keep existing visual system and equal-word-count quiz choices.

## Review Focus
- Wrong terminal/account: label Windows, VPS administrator, VPS factory user and inside-Pi prompts explicitly.
- Existing installations: inspect before editing shell/npm/account configuration or overwriting directories.
- Installer trust: download and inspect before execution; never run user tooling with sudo.
- Headless/persistence: no public browser/debug ports; terminal persistence is not reboot recovery or a sandbox.
- False success: binary availability is not a working crew; require a bounded scratch task and report unverified pieces.

### Task 1: Verify sources
- [x] Read primary Pi, FirstMate, Herdr, Treehouse and prerequisite installation documentation.
- [x] Record source discrepancies and limitations in RESOURCES.md and the playbook.

### Task 2: Extend the course
Files: lessons/0003-pi-software-factory.html, reference/pi-factory-playbook.html; existing HTML navigation, index.html, RESOURCES.md, NOTES.md, README.md; tests/pi_factory_test.py.
- [x] Write a failing check for the new pages, critical safety checkpoints and course discoverability; run it.
- [x] Create lesson and reference using existing assets. Add three retrieval quizzes and a local-only scratch-task verification gate.
- [x] Link the lesson from existing pages/home; update resources and teaching notes without a learning record.

### Task 3: Validate
- [x] Run Python HTML/content checks, existing Python/Node tests and shell syntax checks for new shell blocks.
- [x] Run available browser checks at desktop/mobile widths and inspect new-page captures; run the design detector once.
- [x] Obtain a read-only safety/correctness review and address material findings.
- [x] Attempt to open lesson locally: xdg-open exited 4, so provide file links instead. Report paths and the first learner checkpoint, with explicit unverified VPS status.

No Git repository is present here, so no worktree, commit, push or PR is part of execution.

## Verification and Review Record
- Red: tests/pi_factory_test.py failed because the new pages did not exist. Green: HTML/content checks pass, including 21 Bash syntax blocks (none executed).
- Existing deployment-handler, quiz, navigation and JavaScript syntax checks pass.
- Firefox: all 7 pages pass at 320, 768, 1024 and 1440px; inspected lesson/playbook desktop and narrow screenshots. Static design detector returned no findings.
- Fresh reviewer found missing explicit Windows identity selection for Lesson 2’s nondefault vps_learning key; verified the existing key instructions and fixed both scp and ssh examples. Added regression assertions for identity selection and the required toolchain/capability floors, plus no-merge scratch handling.
- Source review corrected the MSP guide: No Mistakes is now a required dependency, Lavish is presentation-only, and local-only does not itself prohibit local landing. Current Herdr website access returned 403 during research; used official checked-in documentation. No insecure mirror suggested.
- Live VPS, credential flows, installer runtime, Windows key transfer, real-device/cross-browser and print layouts remain unverified. No mission change or assessed learning record.
