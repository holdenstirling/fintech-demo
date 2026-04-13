# Demo Cheat Sheet — Thursday 4/16
## Keep this open in a second window during the call

---

## START (30 min before)
```bash
cd ~/fintech-demo && git checkout feat/duplicate-charge-fix
python3 -m uvicorn app.main:app --reload --port 8000
```
Open http://localhost:8000 — verify all 3 demo buttons work:
- "Run Security Audit" → all 5 vulns appear (3 CRITICAL + 2 HIGH, PCI-DSS & FFIEC labels)
- "Demo: Show Bug" → DUPLICATE badge fires
- "Demo: Show Fix" → PROTECTED badge + dollar amount on stat card
- "Reset Demo" → everything clears

**Verify governance hook fires:** In terminal, run `claude`, make a small edit to `app/config.py`.
Look for: `⛔ [FinTechCo Governance Hook]` → `✅ All tests passing` in the terminal output.

---

## THE 40-MINUTE MAP

| Time | What you're doing | Screen |
|------|-------------------|--------|
| 0:00 | Agenda + discovery questions | Nothing |
| 0:07 | Overview — Claude Code is agentic, not autocomplete | Nothing |
| 0:12 | Security architecture slide (slow down for CTO) | Nothing |
| 0:15 | Switch to browser — show dashboard | localhost:8000 |
| 0:16 | **[BEAT 1]** Click "Run Security Audit" → let it run, stay quiet | Browser |
| 0:18 | Narrate the 5 findings — "3 production secrets in git history, PCI-DSS + FFIEC non-compliant" | Browser |
| 0:20 | **[BEAT 2a]** Click "Demo: Show Bug" → DUPLICATE badge fires | Browser |
| 0:21 | Switch to terminal — show ISSUE.md, paste prompt 3 | Terminal |
| 0:22 | Claude implements fix — narrate while it runs | Terminal |
| 0:24 | Governance hook fires → tests run → 9 green | Terminal |
| 0:25 | **[BEAT 2b]** Click "Demo: Show Fix" → PROTECTED badge | Browser |
| 0:26 | Show CLAUDE.md — "your team's rules, in plain English" | Terminal/Editor |
| 0:27 | Show .claude/settings.json — "the governance hook" | Terminal/Editor |
| 0:28 | **[BEAT 3]** Run `/code-review:code-review` on PR #1 | Terminal |
| 0:30 | Show DEMO_TODO.md — "this is what the session produced" | Editor |
| 0:32 | Ask baseline questions: PR cycle time? Incident MTTR? | Nothing |
| 0:33 | ROI framework — leading vs lagging indicators | Nothing |
| 0:37 | Evaluation plan — 5-person pilot, 3 weeks | Nothing |
| 0:39 | **Hard close** — "Who owns the pilot setup on your side?" | Nothing |

---

## 5 DISCOVERY QUESTIONS (0:02–0:07)

1. "What does your code review process look like — where does it slow down?"
2. "In a production incident, what's harder — finding the issue or fixing it?"
3. "Are any engineers already using AI tools, even unofficially?"
4. "What's your biggest security concern about a tool like this?" ← *let CTO answer, write it down*
5. "What does success look like in 90 days?"

**Reflect back:** *"What I'm hearing is [X] and [Y]. Let me make sure what I show you speaks to that."*

---

## 4 CLAUDE PROMPTS (copy-paste into terminal)

**Prompt 1 — Codebase walkthrough:**
```
I just joined the FinTechCo payments team. Walk me through this codebase —
the payment flow end to end, how the processor integration works, and anything
I should know before touching production code.
```

**Prompt 2 — Security audit (or use the UI button instead):**
```
Audit this codebase for security vulnerabilities. This is a PCI-DSS
regulated financial services application handling real payment data.
```

**Prompt 3 — Fix the bug:**
```
I've been assigned ISSUE.md. Implement the fix described, write tests
proving duplicate charges no longer happen, and make sure all existing
tests still pass.
```

**Prompt 4 — CLAUDE.md:**
```
Create a CLAUDE.md for this repo that captures our security requirements,
coding conventions, and the idempotency pattern we just implemented.
```

**Code review:**
```
/code-review:code-review
```

---

## TOP 5 OBJECTIONS

| Objection | One-line answer |
|-----------|-----------------|
| "Our code can't leave our environment" | "It doesn't. Only the session prompt goes over the wire. Nothing persisted on Anthropic's side." |
| "Are you training on our code?" | "Contractually prohibited. I can send you the specific clause today." |
| "What if it makes a wrong change?" | "Every edit is shown before it's applied. The governance hook validates it. Nothing silent, nothing irreversible." |
| "We already have Copilot" | "Copilot is autocomplete. This is agentic — reads files, runs tests, implements across a whole codebase. Different category." |
| "My engineers won't adopt it" | "The skeptics become the heaviest users by week 4. The pitch is eliminating the tax on their time, not replacing how they think." |

---

## HUMANIZING LINES (say these naturally, not scripted)

- *Before audit:* "I'm curious what it finds here — let me just show you."
- *When hook fires:* "That's the governance hook. Test suite ran automatically. That's compliance without a meeting."
- *On CLAUDE.md:* "Plain English. Any engineer on your team can read it, edit it, and own it."
- *On setup:* "I installed this 20 minutes before this call. No IT ticket."
- *When code review catches the missing test:* "That was in the acceptance criteria. Implementation missed it. Review caught it. That's the loop."

---

## CLOSE (0:39–0:40)

> "Here's what I'd propose as next steps:
> This week — I send you the security overview and data processing agreement.
> Next week — 30-minute setup call, your pilot team is running before we hang up.
> Week 6 — pilot readout, data-driven decision on broader rollout.
> **Who's the right person on your team to own the pilot setup?**"

*Get a name. Get a date. End the call.*

---

## THE THREE TEAMS — one line each

**Software Engineers (120 engineers):** "They're not blocked on writing code. They're blocked on understanding code they didn't write. Onboarding to an unfamiliar service, debugging a distributed system, reviewing a 400-line PR. Claude Code eliminates that tax."

**SREs (20 engineers):** "2am, alert fires, service owned by a team that's off. The time between 'something's wrong' and 'I know where to look' — that's where you measure ROI. We've seen that go from 45 minutes to 15."

**Data Scientists (40 engineers):** "They're brilliant at fraud modeling. They're blocked on API glue, frontend components, and the boilerplate that has nothing to do with their actual work. Claude Code handles the scaffolding so they focus on the models."

---

## PRICING (when they ask)

> "Claude Code is seat-based, similar to GitHub Copilot Enterprise in structure. For a 180-engineer org we'd work through an enterprise agreement — I can get you a number and the security documentation this week. What I'd suggest is starting the 5-person pilot under a trial arrangement so you have real usage data before any commercial conversation."

*(Do not quote a number. Get them into the pilot first.)*

---

## IF THINGS GO WRONG

| Problem | Recovery |
|---------|----------|
| Server not running | `cd ~/fintech-demo && python3 -m uvicorn app.main:app --port 8000` |
| Claude Code slow/timeout | "I'll let that run. Let me show you the result of the last session." → show feat branch |
| /code-review not working | `git diff main...feat/duplicate-charge-fix` → "This is what the review covers." |
| Tests fail | "This is exactly what the governance hook is for — catching it before production." |
| Wrong branch | `git checkout feat/duplicate-charge-fix` |
