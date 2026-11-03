# Service lifecycle teaching implementation plan

**Goal:** Deliver the approved split: Lesson 5 Manual First, Lesson 6 approval-gated CI/CD, Lesson 7 Recovery, with troubleshooting during setup.

**Architecture:** Extend the existing static HTML course, shared CSS, navigation and quiz components. Three short lessons link to three printable staged playbooks; no server integration or universal updater.

**Approved design:** Shared version inventory with service-specific procedures for Hermes, Pi and n8n. User approved creation and requested troubleshooting. Maintain learner-run boundaries and do not infer installation or mastery.

## Constraints
- Reuse existing assets; no new dependencies or live VPS changes.
- Keep knowledge source-backed, commands bounded and secrets out of Git/logs.
- Service-specific recovery: database migrations may prevent binary downgrade.
- GitHub required-reviewer availability must be verified; unavailable gate means manual deployment.
- Three equal-word-count quiz options per question; vary answer positions.

## Review focus
- Existing installations may differ in owner/path/Compose project: stop and inventory first.
- Shell PATH/runtime mismatch: diagnose without sudo package installs.
- SSH/approval failures: no host-key bypass, unrestricted keys or fake gates.
- n8n migration/restore: preserve matching data/key and isolate side effects.
- Navigation and long commands must remain usable on mobile and in print.

## Tasks
- [ ] Add tests for new lesson/playbook existence, troubleshooting, navigation, safety boundaries and Bash syntax; confirm missing files fail.
- [ ] Create lessons/0005-manual-service-setup.html, 0006-service-cicd.html, 0007-service-recovery.html and matching reference/manual-service-playbook.html, service-cicd-playbook.html, service-recovery-playbook.html using shared course/quiz assets.
- [ ] Update index.html, all page navigation, README.md, RESOURCES.md and NOTES.md. Do not create a mastery record.
- [ ] Run structural/quiz/navigation/content tests, browser checks when available, and a fresh read-only safety review. Fix material findings and report verification limits.

No git commits: workspace is not a Git repository. Execution authorized by the user's “go ahead”; implement inline.
