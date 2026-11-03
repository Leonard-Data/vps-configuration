# Hermes Lesson 2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Teach a Windows beginner to set up Hermes on Ubuntu 24.04 without accessing their VPS.

**Architecture:** Reuse the local HTML course, stylesheet, navigation and quiz widget. Keep a short main lesson and put detailed setup and optional CI/CD in a printable reference, with downloadable example files.

**Tech Stack:** HTML, existing CSS/JavaScript, Python standard library, illustrative GitHub Actions YAML.

**Spec:** Approved conversational plan: PowerShell SSH, non-root Hermes install, VS Code Remote SSH, secret-free GitHub repo, approved automated deployment and rollback. Core setup first; CI/CD optional. No real infrastructure changes.

## Global Constraints
- Windows PowerShell client; Ubuntu 24.04 server (learner-reported, not inspected).
- No VPS access, credentials, dependencies or external runtime assets.
- Preserve existing visual system and use source-backed instructions.
- Do not record demonstrated mastery without learner evidence.

## Review Focus
- SSH lockout: test a second connection and retain recovery access.
- Key confusion: distinguish administrator, GitHub and restricted deployment keys.
- Credential leakage: never deploy/version the whole Hermes home.
- Automation compromise: forced command limits deployment to one bounded text file.
- Failed deployment: preserve prior content and explain rollback; do not claim process health from file deployment.

### Task 1: Add lesson and lab
- [ ] Verify current official installation, configuration, SSH and Actions guidance.
- [ ] Add tests for bounded deployment, backup and invalid payloads; confirm they fail before implementation.
- [ ] Create a minimal SOUL.md deployment example, validation workflow and printable instructions.
- [ ] Create Lesson 2 with three equal-word-count quizzes and links into the lab.

### Task 2: Integrate and verify
- [ ] Link Lesson 2 and lab from all existing learning navigation; update source list, notes and README.
- [ ] Update structural tests for six questions across two lessons, checking variation per lesson.
- [ ] Run Node tests, Python checks and deployment tests; inspect browser layouts if available.
- [ ] Obtain read-only safety/content review, fix material issues, report verification limits.
