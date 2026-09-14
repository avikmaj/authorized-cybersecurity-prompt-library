---
id: llm-rag-agent-security-review
title: LLM RAG and AI Agent Security Review
sector: ai-llm-security
models: [chatgpt, claude, grok]
authorization_required: true
status: production
version: 1.0.0
---

# Purpose
Threat-model an owned AI application for prompt injection, unsafe tool permissions, cross-user exposure, data poisoning, and inadequate monitoring.

# Inputs
- System/developer instructions
- Retrieval and ingestion design
- Tool list, permissions, approvals
- Identity and tenant model

# Required Output
1. Scope and architecture assumptions
2. Data flow and trust boundaries
3. Threat table
4. Layered controls
5. Synthetic safe test suite
6. Logging and incident-response recommendations
