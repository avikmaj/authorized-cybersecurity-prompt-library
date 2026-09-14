---
id: supabase-rls-review
title: Supabase PostgreSQL and Row Level Security Review
sector: cloud-security
models: [chatgpt, claude, grok]
authorization_required: true
status: production
version: 1.0.0
---

# Purpose
Review an owned/authorized Supabase schema and RLS policies for unauthorized data exposure or modification risk.

# Inputs
- Sanitized SQL migrations and policies
- Schema and tenant model
- Auth roles and expected access rules

# Instructions
1. Summarize intended table ownership.
2. Review RLS enablement and SELECT, INSERT, UPDATE, DELETE policies.
3. Identify overly broad predicates, role confusion, and service-role misuse.
4. Provide safer policy patterns and staging test cases.

# Required Output
1. Scope and assumptions
2. Table-by-table access model
3. Policy findings
4. Recommended changes
5. Test matrix
