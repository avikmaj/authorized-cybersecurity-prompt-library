---
id: api-authorization-review
title: API Authorization and Tenant Isolation Review
sector: web-application-security
models: [chatgpt, claude, grok]
authorization_required: true
status: production
version: 1.0.0
---

# Purpose
Review an owned or authorized API design/codebase for server-side authorization and tenant isolation weaknesses.

# Inputs
- Sanitized API specification or endpoint list
- Authentication, role, and tenant model
- Relevant server-side authorization code

# Instructions
1. Define intended authorization for every endpoint.
2. Identify object ownership and tenant boundaries.
3. Review server-side enforcement.
4. Recommend code, database, logging, and test changes.

# Required Output
1. Scope and assumptions
2. Authorization-model summary
3. Findings table
4. Remediation plan
5. Safe staging regression checklist
