---
id: github-actions-hardening
title: GitHub Actions CI/CD Security Hardening Review
sector: devsecops-cicd
models: [chatgpt, claude, grok]
authorization_required: true
status: production
version: 1.0.0
---

# Purpose
Review GitHub Actions workflows for least privilege, secret safety, untrusted PR risks, action pinning, artifacts, caches, and supply-chain controls.

# Inputs
- Sanitized workflow YAML
- Trigger definitions, permissions, and action versions
- Deployment environment and approval constraints

# Required Output
1. Scope and assumptions
2. Workflow inventory
3. Findings table
4. Hardened configuration recommendations
5. Validation and rollout plan
