# FinTechCo Demo Prep Guide
**40-minute mock customer meeting · 12-minute live demo**
**Audience:** CTO (skeptical, security-first, 20+ yrs fintech) · Head of Digital Transformation (champion, wants productivity wins)

---

## Before Every Demo — Full Reset Procedure

Run this every time before you present. Takes 60 seconds.

```bash
# 1. Delete the database so seed data regenerates fresh
rm -f payments.db

# 2. Start the server with auto-reload enabled
uvicorn app.main:app --reload
```

Then open `http://localhost:8000` and confirm:
- [ ] Amounts show **$9,900** (bug is active — formatAmount is missing /100)
- [ ] Success rate shows **99.2%** (P1 not triggered)
- [ ] Button reads **"Simulate P1 Incident"** (not greyed out)
- [ ] Transaction table has **25 rows** — mix of succeeded (green) and 3 failed (red)
- [ ] Transactions span the **last 3 days** with varied amounts, currencies, customers
- [ ] Claude Code open, **fresh session**, `/fast` ON

> If the table is empty or amounts look wrong, the old `payments.db` is still there. Delete it and restart.

---

## What's in the Dashboard (Seed Data)

25 pre-loaded transactions across 5 customers, 3 currencies, last 72 hours:

| Customer | Volume | Notable |
|---|---|---|
| cust_A1B2 | $749 + $99 + $199 | Enterprise license + subscriptions |
| cust_C3D4 | $199 + $49 + others | Mix of invoices, 1 failed |
| cust_E5F6 | $499 + $499 services | Professional services invoice |
| cust_G7H8 | EUR/GBP invoices | Multi-currency, 1 failed retry |
| cust_J9K0 | Subscriptions + add-ons | Starter plan upgrade |

**3 failed transactions** — card declined, payment retry — so the table isn't all green. Realistic.

---

## Full 40-Minute Presentation Overview

### Introductions (pre-clock, ~5 min — interviewer runs this)
Hold for them. Don't start slides until they hand it to you.

---

### Slide: Title (1 min)
> "Thanks for the time. The headline: how 180 engineers ship faster — without your auditors losing sleep. Those two things are usually in tension. I want to show you today that with Claude Code, they don't have to be."

---

### Slide: Agenda (30 sec)
> "Here's how we'll use the next 40 minutes. I want to front-load discovery — I'd rather tailor this to what you're actually dealing with than run a generic pitch. Then a live demo, and we'll close with a realistic rollout plan."

---

### Slide: Discovery (3–4 min)
Ask 1–2 of these, then listen:
- "What does your code review process look like today, and where does it slow down?"
- "When a new engineer joins, how long before they're shipping independently?"
- "What does a P1 incident response look like for your payments team?"

Listen for: compliance friction, onboarding lag, review bottlenecks, SRE toil.

---

### Slide: What I'm Hearing (1 min)
Mirror back what they told you.
> "So what I'm hearing is [X, Y, Z]. Does that capture it? That's exactly what I want to make sure we address today."

---

### Slide: What Is Claude Code (2 min)
> "Claude Code is a coding agent — not an autocomplete tool, not a chatbot. It reads your whole codebase, reasons about it, makes a plan, executes it, and checks its own work against your tests. It works in your terminal alongside your existing tools. Nothing goes to the cloud except the session prompt."

> "The analogy: pairing with a senior engineer who already read every file in your repo and knows your coding standards cold — but it always waits for you before it commits anything."

**For the CTO:**
> "The human stays in the loop at every write action. Claude proposes, you approve. That's the design."

---

### Slide: Who This Helps at FinTechCo (2 min)

| Team | Bottleneck | What Claude Code does |
|---|---|---|
| 120 Software Engineers | Review wait times, onboarding lag | Faster PRs, new engineers productive in days |
| 40 Data Scientists | Boilerplate, no frontend skills | Turns analysis into a dashboard without eng support |
| 20 SREs | Incident diagnosis under pressure | Reads the whole codebase in seconds, surfaces root cause |

> "Same tool, tuned to each context. One evaluation, one rollout, one security review."

---

### Slide: Live Demo (12 min)
→ See the detailed demo script below.

---

### Slide: What You Just Saw (1 min)
> "In 12 minutes: a junior engineer onboarded to an unfamiliar codebase, caught a formatting bug, diagnosed and resolved a P1 incident, and we saw how the standards that prevented it from being worse are encoded in a single file every engineer inherits automatically. That's the day-to-day."

---

### Slide: Safety, Security, Governance (2 min)
**For the CTO:**
> "Your source code does not leave your machine. The CLI reads files locally — only the session prompt goes to the API, over HTTPS, nothing retained after the session ends. SOC 2 Type II certified. We do not train on your code — that's in the contract."

> "The CLAUDE.md file we saw — that's your enforcement layer. PCI-DSS requirements, authentication patterns, testing standards. Every engineer, every contractor, inherits those rules the moment they open Claude Code on your repo."

> "Enterprise tier: permission modes that control what Claude can do before it asks, approval workflows before code is committed, full audit logs of every action."

---

### Slide: Architecture (1 min)
> "One picture for your security team. Everything that leaves the laptop is a session prompt over HTTPS. Nothing stored, nothing trained on, every write action waits for a human."

Point, don't read. Move on.

---

### Slide: Measuring the Return (2 min)
> "I don't want to give you a number without your numbers. Here's the framework:"

- **Time to first PR** for new engineers
- **Code review cycle time** — hours from open to merge
- **Mean time to diagnose** on P1 incidents
- **Test coverage delta** over the pilot

> "We baseline these in week one. At the end of the pilot, you have real data — not a vendor case study."

---

### Slide: Pragmatic Rollout (2 min)
> "Three weeks to a signal. Three months to a decision."

- **Weeks 1–3:** One team, one use case — payments engineers, bug triage and PR review. Measure time-to-resolution.
- **Month 1–2:** Add SREs for incident response. Add data scientists for analysis workflows.
- **Month 3:** Company-wide rollout decision — based on your data.

> "The teams that see the fastest signal have the clearest bottleneck. For you, that's payments engineering."

---

### Slide: Next Steps (2 min)
Three asks — none need procurement:
1. **This week:** Security overview, DPA, SOC 2 to your legal team
2. **Next week:** 30 min with your security lead on the architecture
3. **Week 3:** Pilot kickoff with 5–10 payments engineers

---

### Close (1 min)
> "I'd rather end on a name and a date than a thank-you slide. Who on your side is the natural owner for the pilot? And what does the calendar look like for next week?"

Stop talking. Wait for an answer.

---

## Live Demo Script (12 min)

### WHEN TO SIMULATE THE P1
> Click "Simulate P1 Incident" **after** Prompt 2 (visual bug) is fixed and you've refreshed the browser.
>
> Sequence: Prompt 1 → Prompt 2 → **refresh browser** (amounts now correct) → say transition line → **click P1 button** → Prompt 3 → Prompt 4 → watch dashboard resolve.
>
> Do NOT click it before the bug fix. You want the dashboard clean and healthy right before the P1 hits. The contrast is the point.

---

### Setup (30 sec — you talk, don't touch Claude)
Switch to browser. Point at dashboard.

> "Let me set the scene. Day one for a new engineer on the FinTechCo payments team. They've just been given access to the codebase and the dashboard."

Point at the $9,900 amounts.

> "The first thing they notice: something looks off."

---

### Prompt 1: Onboarding (2 min)
```
I just joined the FinTechCo payments team. Walk me through this codebase —
what does it do, how does money actually move through it, and what should
I know before I touch anything?
```

**While Claude runs (~35 sec):**
> "No diagram. No wiki page. Described it the way a new engineer would on their first day. It's reading the actual code — routes, models, database layer, the processor integration."

**After response — point at 2–3 things it surfaced:**
> "Payment flow, processor isolation, what not to touch before going to production. That's not a script — that's it reading the code and reasoning about what matters."

> "Back to that dashboard."

---

### Prompt 2: Visual Bug (2.5 min)
Point at $9,900 amounts.

> "Every transaction is showing 100x the actual amount. Alarming in a payments dashboard."

```
Our payments dashboard is showing transaction amounts 100x too high —
a $99 charge is showing as $9,900. Find the bug and fix it.
```

**While Claude runs (~30 sec):**
> "No file name. No line number. Described it the way a user would report it."

**After response:**
> "Found `formatAmount()` in `static/index.html` — missing the cents-to-dollars conversion. One line."

**Refresh the browser. Amounts now correct.**

> "Fixed. For 120 engineers, that's the difference between a 20-minute debugging session and 45 seconds."

---

### → CLICK "SIMULATE P1 INCIDENT" NOW

> "Now let me show you the scenario your SREs actually lose sleep over."

**Click the button.** P1 banner appears. Success rate drops to 94.1%. Duplicate rows appear in the table.

---

### Prompt 3: P1 Diagnose (in the 4 min P1 segment)
> "Payment success rate just dropped from 99.2% to 94.1%. Duplicate charges hitting the same customers. This is a P1."

```
We have a P1. Payment success rate dropped from 99.2% to 94.1% —
duplicate charges are appearing for the same customers.
Diagnose what's causing this and where in the code the problem is.
```

**While Claude runs (~45 sec):**
> "This is what your SRE does at 2:47am when this alert fires. Except instead of spending 20 minutes reading files they've never seen, they have this."

**After response:**
> "Root cause: `POST /api/payments` has no idempotency key support. Client retries after a network timeout create a second charge. Claude found it, explained it, exact file and line."

---

### Prompt 4: P1 Fix
```
Fix it. Make sure all tests pass.
```

**While Claude runs (~45 sec):**
> "In a regulated environment, fixing isn't enough. You need to know you didn't break anything else."

**After response — tests pass:**
> "13 tests, all green."

**Pause. Watch the dashboard. Don't talk.**

Within 3 seconds: banner clears, success rate animates back to 99.2%.

> "Server reloaded with the fix. Dashboard picked it up. P1 resolved."

Let it land.

---

### Governance (2.5 min — no Claude, you talk)
Open `CLAUDE.md` in the editor.

> "The last thing I want to show you isn't a prompt."

> "This file — CLAUDE.md — is how you make sure this can't happen again. PCI-DSS requirements, authentication patterns, testing standards, the idempotency rules we just implemented. Encoded here in plain English. Every engineer who opens Claude Code on this repo reads this file first. New hire, contractor, anyone. They operate within these guardrails automatically."

**For the CTO:**
> "This is the answer to your compliance question. Your standards aren't in a wiki nobody reads. They travel with the codebase."

**For the Head of Digital Transformation:**
> "When you roll this out to 180 engineers, you don't train each of them on your security requirements. You write them once."

---

## Timing Reference

| Segment | Clock | Claude running? |
|---|---|---|
| Setup narration | 0:00–0:30 | No |
| Prompt 1: Onboarding | 0:30–2:30 | Yes (~35s) |
| Prompt 2: Visual bug | 2:30–5:00 | Yes (~30s) + browser refresh |
| Click P1 button | 5:00–5:20 | No |
| Prompt 3: Diagnose | 5:20–7:15 | Yes (~45s) |
| Prompt 4: Fix + tests | 7:15–9:00 | Yes (~45s) |
| Watch dashboard resolve | 9:00–9:30 | No — stay silent |
| Governance / CLAUDE.md | 9:30–12:00 | No |
| Buffer | 12:00–12:30 | — |

---

## If Things Go Wrong

| Problem | What to do |
|---|---|
| Claude response is very long | Scroll to the summary. "It found the issue — here's the key part." |
| Dashboard doesn't auto-reload after fix | Manually refresh. "Server reloaded — let me refresh." |
| P1 button greyed out at start | Server wasn't restarted. `ctrl+c` → `rm payments.db` → `uvicorn app.main:app --reload` |
| Amounts showing correctly at start (bug not active) | The formatAmount bug may have been fixed. Check `static/index.html` — the `/ 100` needs to be removed from `formatAmount()` |
| Table is empty | Old `payments.db` has data, `init_db()` didn't reseed. Delete it and restart. |
| Claude gives unexpected answer | Rephrase once. If still off, move on — don't spiral. |

---

## Stakeholder Cheat Sheet

**For the CTO:**
- "CLAUDE.md is your enforcement layer — not a wiki, not a style guide. It's in the tool."
- "Every write action waits for a human. That's the design, not a limitation."
- "SOC 2 Type II, no training on your code — in the contract."
- "Your standards aren't in a wiki nobody reads. They travel with the codebase."

**For the Head of Digital Transformation:**
- "One tool, three teams — payments engineers, data scientists, SREs."
- "New engineer productive in days, not weeks."
- "Time-to-resolution is the metric. Two weeks, one team, you'll have the data."
- "Write your standards once. 180 engineers inherit them automatically."

---

## The Four Prompts — Copy-Paste Ready

```
PROMPT 1 — ONBOARDING
I just joined the FinTechCo payments team. Walk me through this codebase —
what does it do, how does money actually move through it, and what should
I know before I touch anything?
```

```
PROMPT 2 — VISUAL BUG
Our payments dashboard is showing transaction amounts 100x too high —
a $99 charge is showing as $9,900. Find the bug and fix it.
```

```
PROMPT 3 — P1 DIAGNOSE
We have a P1. Payment success rate dropped from 99.2% to 94.1% —
duplicate charges are appearing for the same customers.
Diagnose what's causing this and where in the code the problem is.
```

```
PROMPT 4 — P1 FIX
Fix it. Make sure all tests pass.
```
