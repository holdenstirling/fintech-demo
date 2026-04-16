# FinTechCo Demo — 12-Minute Script
**Audience:** CTO (skeptical, security-first) + Head of Digital Transformation (champion, wants productivity wins)
**Goal:** Show Claude Code can fix, audit, and enforce standards in a regulated codebase — safely

---

## Pre-Demo Checklist
- [ ] Server running: `uvicorn app.main:app --reload`
- [ ] Dashboard open at `http://localhost:8000` — confirm amounts show $9,900 (not $99)
- [ ] Terminal open in `/fintech-demo`
- [ ] Claude Code open, fresh session
- [ ] `/fast` toggled ON

---

## The Arc
> "What does it look like to be an engineer at FinTechCo using Claude Code — from a user-reported bug to a full security review to enforcement?"

**Act 1 → Fix** (visual bug, fast win)
**Act 2 → Audit** (security review, regulated context)
**Act 3 → Govern** (CLAUDE.md + approval workflows)

---

## ACT 1 — Bug Fix (3 min)

### Setup (30 sec, you talk)
Point at dashboard:
> "We just got a report from our payments team — every transaction on the dashboard looks 100x too expensive. A $99 charge is showing as $9,900. Before I touch anything, I'm going to ask Claude Code to find it."

### Prompt (copy-paste exactly)
```
Our payments dashboard is showing transaction amounts 100x too high —
a $99 charge shows as $9,900. Find the bug in the frontend and fix it.
```

### While Claude is running (~30 sec) — you say:
> "I didn't tell it which file or which function. I described it the way a user would file a ticket. It's reading the HTML, the JS, tracing the data flow."

### After Claude responds — you say:
> "It found `formatAmount()` in `static/index.html` — missing the cents-to-dollars conversion, one line. Fixed, explained, done."
>
> "For your 120 engineers, that's the difference between a 20-minute debugging session and a 45-second one. Multiply that across every team."

**[Refresh dashboard to show correct amounts]**

---

## ACT 2 — Security Audit (5 min)

### Transition (20 sec, you talk)
> "That's the speed side. Now let me show you why the CTO in the room should care — not just what's broken, but what you don't know is broken yet. Especially in a PCI-DSS environment."

### Prompt (copy-paste exactly)
```
Audit this codebase for security vulnerabilities.
This is a PCI-DSS regulated payments service handling real card data.
Be specific — file names, line numbers, severity.
```

### While Claude is running (~60-90 sec) — you say:
> "This is reading every layer — config, authentication, database queries, the processor integration. The same methodology a security engineer uses for a manual review, completed in about 90 seconds."
>
> "For your SRE team specifically — imagine running this on every PR before it merges. Or after an incident, when you need to understand the blast radius."

### After Claude responds — you say:
> "It found hardcoded production credentials, three unauthenticated endpoints exposing payment records, a timing attack vulnerability on the admin token comparison, and an unparameterized SQL query. Ranked by severity, with exact file and line numbers."
>
> "This is what a security audit report looks like. Generated in 90 seconds, not 3 weeks."

**[Pause — let findings land, especially for CTO]**

> "Now watch what happens when we ask it to fix the most critical ones."

### Prompt (copy-paste exactly)
```
Fix the three most critical vulnerabilities you found.
Make sure all existing tests still pass.
```

### While Claude is running (~45 sec) — you say:
> "In a regulated environment, finding the problem is half the work. The other half is implementing a fix that doesn't break anything and meets your standards. Watch what it does with the tests."

### After Claude responds — you say:
> "13 tests, all passing. The fix is in, it's verified. And notice — it used `hmac.compare_digest` for the token comparison, not just `==`. It knows the secure implementation pattern, not just that a problem exists."

---

## ACT 3 — Governance (3 min, mostly you talking)

### Transition (10 sec)
> "The last thing I want to show you isn't a prompt."

**[Open CLAUDE.md in the editor]**

### You say:
> "This is CLAUDE.md. Every engineer, every contractor, every new hire who opens Claude Code on this repo — it reads this file first. Your PCI-DSS requirements, your authentication patterns, your testing standards, your idempotency rules — all encoded here."
>
> "Claude Code doesn't just follow the file. It references it when it makes decisions. If someone asks it to hardcode a secret, it pushes back. If someone asks it to skip tests, it pushes back. This is your enforcement layer, not a style guide nobody reads."

**[For the CTO specifically]**
> "On top of that, in the enterprise tier: you configure permission modes that control what Claude can do before asking. Approval workflows before any code is committed. Full audit logs of every action Claude took in a session. You're not handing over the keys — you're adding a junior engineer who happens to know your entire codebase and your security standards cold."

**[For the Head of Digital Transformation]**
> "And for your teams — Software Engineers, Data Scientists, SREs — the same tool, tuned to each context. Your SREs are getting incident triage in seconds. Your data scientists are getting boilerplate out of the way so they can focus on the model. Your engineers are shipping faster without your security posture getting worse."

---

## Wrap (30 sec)
> "In 12 minutes we went from a user-reported bug to a full security audit to understanding how you'd govern this across 180 engineers. That's the day-to-day for a FinTechCo team with Claude Code."
>
> "The evaluation I'd recommend: pick one team, one use case — probably your payments engineers and bug triage or PR review. Two weeks, measure time-to-resolution. You'll have the data you need to make the broader call."

---

## Timing Reference
| Segment | Time | Claude running? |
|---|---|---|
| Act 1 setup | 0:30 | No |
| Bug fix prompt + response | 1:00 | Yes (~30s) |
| Bug fix narration | 1:00 | No |
| Transition | 0:20 | No |
| Audit prompt + response | 2:00 | Yes (~90s) |
| Audit narration | 1:00 | No |
| Fix prompt + response | 1:30 | Yes (~45s) |
| Fix narration | 0:30 | No |
| CLAUDE.md + governance | 2:30 | No |
| Wrap | 0:30 | No |
| **Total** | **~11:50** | |

---

## If Claude Takes Too Long
- Keep talking — use the "while Claude is running" lines, then add:
  > "This is a complex codebase read — in practice on a faster network with a warmer context this is closer to 20 seconds."
- If a response is longer than expected, scroll to the summary section and narrate from there

## If Something Breaks
- Dashboard not showing bug: manually point at the `formatAmount` function in the editor — "Here's what the bug looks like in code"
- Server not running: pivot to showing code in editor only — "Normally we'd see this live in the browser"
- Claude gives wrong answer: "Let me tighten that prompt" — rephrase and retry once, then move on

---

## Key Lines for Each Stakeholder
**For the CTO:**
- "CLAUDE.md is your enforcement layer, not a suggestion"
- "Approval workflows, permission modes, full audit logs — you control what it can do"
- "It used `hmac.compare_digest` — it knows the secure pattern, not just that a problem exists"

**For the Head of Digital Transformation:**
- "120 engineers, 40 data scientists, 20 SREs — same tool, tuned to each context"
- "Time-to-resolution is the metric. Two weeks, one team, you'll have the data"
- "Bug triage that used to take 20 minutes, now 45 seconds"
