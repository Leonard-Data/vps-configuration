# VPS Resources

## Knowledge

Sources reviewed 2026-11-02. Provider features and entitlements can change; check the current dashboard before acting.

- [Hostinger VPS support](https://www.hostinger.com/support/vps/). Provider navigation and task-specific guides; starting point requested by the learner.
- [Hostinger: OS choices](https://www.hostinger.com/support/8999382-what-vps-operating-system-to-choose-at-hostinger/). Compare supported distributions and templates against application requirements.
- [Hostinger: change or reinstall the OS](https://www.hostinger.com/support/4965922-how-to-change-the-operating-system-of-your-vps-at-hostinger/). Destructive reinstall behavior; read before changing templates.
- [Ubuntu Server: OpenSSH](https://documentation.ubuntu.com/server/how-to/security/openssh-server/). Keys, configuration snippets, syntax checks and lockout warnings; commands are Ubuntu-specific.
- [Docker: containers](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/). Images, isolated processes and the shared host kernel.
- [Hostinger: Docker Manager](https://www.hostinger.com/support/12040815-how-to-deploy-your-first-container-with-hostinger-docker-manager/). Compose deployment UI and prerequisites. Review catalog YAML rather than trusting defaults.
- [Docker: packet filtering and firewalls](https://docs.docker.com/engine/network/packet-filtering-firewalls/). Published ports can bypass ufw rules; essential security caveat.
- [Docker: volumes](https://docs.docker.com/engine/storage/volumes/). Persistence, lifecycle, backup and restore operations. Persistence is not a second copy.
- [Hostinger: backups and snapshots](https://www.hostinger.com/support/1583232-how-to-back-up-or-restore-a-hostinger-vps/). Whole-server restore consequences, retention and snapshot limitations. Current article says one manual snapshot, expiring after one day; verify your actual plan. Direct provider-backup downloads are not supported by this guide.
- [Hostinger: point a domain to a VPS](https://www.hostinger.com/support/1583227-how-to-point-a-domain-to-your-vps-at-hostinger/). A records and nameserver choices; preserve unrelated records, particularly mail routing.
- [RFC 1035, sections 3–4](https://www.rfc-editor.org/rfc/rfc1035). Primary definitions of A, CNAME and TTL; use the lesson for an approachable summary.
- [RFC 3596, section 2](https://www.rfc-editor.org/rfc/rfc3596#section-2). AAAA records store IPv6 addresses.
- [Hostinger: server usage](https://www.hostinger.com/support/4725768-how-to-check-vps-resources-usage-at-hostinger/). Provider CPU, memory, disk and traffic graphs; these are not proof of application health.
- [Hostinger API reference](https://developers.hostinger.com/). Bearer-token authentication, resource operations and real-account effects. Use read-only requests first; never embed credentials in a lesson or browser code.

### Lesson 2: Hermes setup and restricted delivery

- [Hermes installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation/). Official installer, managed runtime, headless flags, setup and diagnostics; do not substitute Ubuntu system Python.
- [Hermes configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/). Private home, configuration and SOUL identity. Repository examples are not a full agent backup.
- [Hermes messaging](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/). Gateway setup and Linux service lifecycle; user-service linger and allowed-user controls.
- [Hermes updates](https://hermes-agent.nousresearch.com/docs/getting-started/updating/). Supported manual update workflow; separate from the lab’s SOUL.md deployment.
- [GitHub SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent). Ed25519 key generation and passphrases. VPS user keys and GitHub repository deploy keys are different concepts.
- [VS Code Remote SSH](https://code.visualstudio.com/docs/remote/ssh). Remote editor and SSH config; remote terminals execute on the VPS.
- [Win32-OpenSSH file security](https://github.com/PowerShell/Win32-OpenSSH/wiki/Security-protection-of-various-files-in-Win32-OpenSSH), [Microsoft icacls](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls) and [VS Code troubleshooting](https://code.visualstudio.com/docs/remote/troubleshooting). Local config ownership/access restrictions, ACL backup, inheritance copying and numeric-SID removal; source-checked Windows repair, not a live-tested fix. Follow-on Remote-SSH parsing errors do not by themselves diagnose a server fault.
- [GitHub environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments). Deployment secrets/protection rules; private-repository reviewer availability depends on plan. No available gate means manual deployment for this lab.
- [OpenSSH authorized_keys](https://man.openbsd.org/sshd.8#AUTHORIZED_KEYS_FILE_FORMAT). Forced command and restrict options used to constrain the CI user key.
- [GitHub secure Actions use](https://docs.github.com/en/actions/reference/security/secure-use). Least privilege, trusted workflows and full-SHA action pinning for production.
- The lab’s resource budget, account separation, staged checks and bounded Python handler are teaching design recommendations, not official production guarantees. Sources checked 2026-11-02; no live-server validation performed.

### Lesson 3: Pi software factory (learner-run)

- [MSP orchestration harness guide](https://leonard-data.github.io/msp/docs/orches-harness/). Requested end-to-end recipe for Pi, FirstMate, Herdr, Treehouse and AXI helpers. Treat as an entry point, not the authority when current product requirements disagree.
- [Pi quickstart](https://pi.dev/docs/latest/quickstart/) and [security model](https://pi.dev/docs/latest/security/). Node ≥22.19, npm `--ignore-scripts`, provider login, session continuation and the OS-permission boundary; trust approval is not a sandbox. Complemented by complete local Pi 1.4.0 README, quickstart and security documentation.
- [nvm README, v0.40.8](https://github.com/nvm-sh/nvm/blob/v0.40.8/README.md). Reviewed installer, LTS selection and custom-prefix incompatibility. The playbook uses nvm instead of the guide’s ~/.local npm prefix; do not combine them.
- [Ubuntu user management](https://documentation.ubuntu.com/server/how-to/security/user-management/). Dedicated accounts and administrative group boundaries; account creation is administrator work, agent runtime is not.
- [GitHub CLI Linux installation](https://github.com/cli/cli/blob/trunk/docs/install_linux.md) and [gh auth login](https://cli.github.com/manual/gh_auth_login). Supported installation, headless authentication and plaintext credential-store fallback warning.
- [FirstMate README](https://github.com/kunchenguid/firstmate), [current dependency requirements](https://github.com/kunchenguid/firstmate/blob/main/docs/configuration.md#toolchain) and [Herdr backend](https://github.com/kunchenguid/firstmate/blob/main/docs/herdr-backend.md). Source snapshot a4bf5f867bae63e0a44b72ab4a8a7c83c0dea2f8: no-mistakes ≥1.46.0 is a universal dependency despite the guide calling it optional; Lavish is presentation-only. Bootstrap owns AXI floors and Treehouse lease capability checks; detect → consent → install. Local-only can still allow approved local landing; our first task separately forbids merges.
- [Herdr official repository](https://github.com/herdrdev/herdr), [Pi integrations](https://github.com/herdrdev/herdr/blob/master/docs/versions/0.9.5/website/src/content/docs/integrations.mdx) and [saved sessions](https://github.com/herdrdev/herdr/blob/master/docs/versions/0.9.5/website/src/content/docs/session-state.mdx). Stable v0.9.5 at review, base protocol ≥14 per FirstMate, presentation spaces need ≥0.8.0, Pi native restoration needs integration ≥2. Detach preserves running processes; reboot restoration starts new ones and needs reconciliation.
- [Treehouse](https://github.com/kunchenguid/treehouse) and [installer](https://github.com/kunchenguid/treehouse/blob/main/docs/install.sh). Stable v3.1.8 at review; worktrees and leases, not security isolation. Installer may fall back to privileged /usr/local/bin when ~/.local/bin is not on PATH; current installer lacks explicit archive checksum verification.
- [No Mistakes](https://github.com/kunchenguid/no-mistakes). Install required dependency; defer PR/CI exercises. Its gates do not guarantee safety or correctness.
- [Chrome DevTools AXI](https://github.com/kunchenguid/chrome-devtools-axi) and [Chrome DevTools MCP requirements](https://github.com/ChromeDevTools/chrome-devtools-mcp#requirements). Installing an AXI CLI does not provision/validate a Linux browser; documented setup hooks do not target Pi. Shell scratch exercise needs no browser. Never expose debug endpoints or disable browser sandboxing to bypass a failed check.
- Dedicated account, installation stop points and one unmerged scratch task are teaching safety choices, not upstream production guarantees. Source review only; no installer executed or live VPS tested.

### Lesson 4: n8n VPS learning lab

- [n8n install options](https://docs.n8n.io/deploy/host-n8n/install-options). Requested primary reading: one-line, Compose, Docker, npm and provider routes are alternatives.
- [Current n8n Compose guide](https://docs.n8n.io/deploy/host-n8n/install-options/install-using-docker-compose). Full Assistant stack includes privileged Docker-in-Docker and a 4 GB / 2 vCPU prerequisite; not copied as a beginner production recipe. Our smaller SQLite + Caddy lab deliberately omits the AI sandbox. Postgres recommended for important round-the-clock use; changing DB_TYPE alone does not migrate data. Older hosting Docker guide is marked outdated.
- [Webhook proxy configuration](https://docs.n8n.io/hosting/configuration/configuration-examples/webhook-url/). N8N_WEBHOOK_URL supersedes deprecated WEBHOOK_URL since 2.35.0; one trusted proxy hop in our direct-DNS topology, with forwarded host/protocol/client headers.
- [Encryption key](https://docs.n8n.io/hosting/configuration/configuration-examples/encryption-key/). Automatic key persistence and explicit first-run key; retain matching database and key. [CLI](https://docs.n8n.io/hosting/cli-commands/) documents workflow/credential export and warns that decrypted exports expose secrets. The lesson’s rehearsal sends decrypted output only to /dev/null.
- [Manual Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger/) and [Edit Fields](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/). Two-node dummy workflow; no external accounts or side effects.
- [Webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/) and [Schedule Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/). Test versus production registration, publishing, endpoint authentication and timezone.
- [n8n security](https://docs.n8n.io/hosting/securing/overview/), [error handling](https://docs.n8n.io/flow-logic/error-handling/), [official releases](https://github.com/n8n-io/n8n/releases). Operational checklist; choose a reviewed supported exact stable tag at use, not an evergreen claim about a hard-coded version.
- [Caddy Docker Compose](https://caddyserver.com/docs/running#docker-compose), [automatic HTTPS](https://caddyserver.com/docs/automatic-https) and [reverse proxy](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy). Internal service forwarding and default forwarded headers; persist certificate state. [Caddy releases](https://github.com/caddyserver/caddy/releases) for tag selection.
- [Docker Ubuntu installation](https://docs.docker.com/engine/install/ubuntu/), plus volume/firewall sources above. First-owner provider-firewall restriction and offline recovery rehearsal are teaching adaptations, not upstream guarantees. All live DNS, TLS, image compatibility, firewall, decryption and service restoration remain unverified.

### Lessons 5–7: manual maintenance, approved delivery and recovery

- [Hermes updates](https://hermes-agent.nousresearch.com/docs/getting-started/updating/) and [backup versus profile export](https://hermes-agent.nousresearch.com/docs/reference/faq/#hermes-backup-vs-hermes-profile-export). Managed updater preview/check behavior, source/runtime maintenance, restart receipts and older-code/newer-data incompatibility. A full backup includes credentials but excludes source/runtime images and other documented paths; profile export excludes credentials. Match flags to installed help.
- [Pi CLI](https://pi.dev/docs/latest/cli/) and [release notes](https://github.com/earendil-works/pi/releases). Runtime update versus customization-package update; exact npm version selection only for existing npm installations, not a migration between install routes. Complete local Pi 1.4.0 README, quickstart and CLI docs inspected; Node and integration versions remain separate maintenance boundaries.
- [n8n updating](https://docs.n8n.io/hosting/installation/updating/), [Docker Compose config](https://docs.docker.com/reference/cli/docker/compose/config/), [Compose up](https://docs.docker.com/reference/cli/docker/compose/up/) and [immutable image digests](https://docs.docker.com/reference/cli/docker/image/pull/#pull-an-image-by-digest-immutable-identifier). Review release notes and rehearse migrations; validate without printing expanded secrets, replace one service without replacing the original project/volume, record actual runtime identity. Volume preservation is not backup or migration reversal.
- [GitHub deployment environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments). Required-reviewer availability is distinct from environment availability; on Free/Pro/Team reviewers are public-repository-only. Referencing an absent environment can create it unprotected. Prove rejection/approval before adding secrets; unavailable gate means manual deployment, not making the repository public.
- [GitHub workflow concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency). With default pending behavior, cancel-in-progress false preserves a running deploy but not every pending run; it is not a server lock or a full FIFO queue. Secure-use and OpenSSH primary references above support the restricted-key design.
- Recovery vocabulary (RPO/RTO), staged evidence, per-service adapter requirements and the intentionally non-runnable CI/CD fragment are teaching design choices. The existing guarded SQLite backup/offline restore recipe is reused, not replaced by an unverified production restoration script. Neither live upgrades nor restore/cutover safety were tested.

## Wisdom (Communities)

- [n8n Community](https://community.n8n.io/). Optional practitioner feedback on sanitized workflow and hosting questions; never post keys, credentials or sensitive execution data.
- [Docker Community Forums](https://forums.docker.com/). Product-focused troubleshooting; useful for discussing a sanitized Compose file. Never post tokens, passwords or private keys. Joining is optional; no preference established.
- [Ubuntu Discourse: Server](https://discourse.ubuntu.com/c/server/17). Distribution-specific operational discussions; useful after reproducing an issue and collecting redacted logs.

## Gaps

- User reports Ubuntu 24.04 LTS and uses Windows; actual OS, template, plan entitlements, domain and installed applications remain unverified.
- Before an executable setup lesson, verify the selected OS version, recovery access, SSH port, firewall backend and application/database backup procedure.
- Cloudflare's DNS overview returned HTTP 403; DNS definitions are instead grounded in the RFCs.
- Herdr website docs/installer returned HTTP 403 during research; verified its official repository and checked-in 0.9.5 documentation instead. If the learner gets a download error, stop rather than use an arbitrary mirror.
- Pi factory runtime, provider/GitHub authentication, browser provisioning, Windows key transfer and reboot recovery are unverified on the learner’s host. No install/security-audit claim is implied by documentation review.
