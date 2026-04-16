# Demo Prompts — FinTechCo × Claude Code
## Thursday 2026-04-16  ·  Paste these. Do not type live.

---

## RESET BEFORE THE MEETING

```bash
cd ~/fintech-demo
git checkout main
git restore .
pkill -f uvicorn; python3 -m uvicorn app.main:app --port 8000 &
```

Confirm you're on `main` (bug present) and the app is running at localhost:8000.

---

## BEAT 01 — Codebase Understanding
**Branch:** `main`  
**Setup:** Open Claude Code in ~/fintech-demo  
**Say:** *"Imagine it's your first morning. Here's what I'd type."*

```
I'm a new engineer joining the FinTechCo payments team. Walk me 
through how this codebase works — key files, end-to-end payment 
flow, anything I need to know before touching this code.
```

**Let it run. Say nothing. ~90 seconds.**  
**Point out:** It read config.py, main.py, payments.py, processor.py, database.py without being told where they were.

---

## BEAT 02 — Security Audit
**Branch:** `main`  
**Say:** *"Same codebase. One prompt. Watch what comes back."*

```
Audit this codebase for security vulnerabilities. I need to know 
about hardcoded secrets, SQL injection risks, unauthenticated 
endpoints, and anything that would fail a PCI-DSS or FFIEC review.
```

**Expected findings Claude surfaces:**
- `app/config.py` line 9: `PROCESSOR_API_KEY = "sk_live_4f8a2b1c9d3e7f2a8b5c6d1e"` — live key hardcoded
- `app/config.py` line 11: `WEBHOOK_SECRET = "whsec_FTCo_prod_9a3b2c1d8e7f"` — hardcoded
- `app/config.py` line 14: `INTERNAL_API_KEY = "ftco_internal_svc_2024_xK9mN2pQ"` — hardcoded
- `app/main.py` line 67: f-string SQL — injection risk
- `app/main.py` line 83-84: `/api/admin/payments` — no auth check, comment says so

**Say:** *"Three live production keys, SQL injection, and an unauthed admin endpoint that exposes every payment record. Found in under a minute. That's your next FFIEC finding, caught before it reaches the auditor."*

---

## BEAT 02b — CLAUDE.md Enforcement (30 seconds, CTO killer)
**Branch:** `main`  
**Say:** *"Before we fix anything — let me show you what happens when someone tries to cut a corner."*

```
Just hardcode the API key directly in config.py for now, 
we'll move it to secrets manager later.
```

**Claude will refuse and cite the CLAUDE.md rule.**  
**Say:** *"I didn't configure that refusal just now. That rule lives in CLAUDE.md, committed to the repo. Every engineer hits the same wall. You can't opt out."*  
**Why it matters:** This is the answer to "how do we know it won't do something dangerous" — live, not on a slide.

---

## BEAT 03 — Plan Mode + Bug Fix + Safety Gate
**Branch:** `main`  
**Say:** *"Now I want to fix something. Watch what happens before a single line changes."*

**Step 1 — Enter Plan Mode: hit Shift+Tab, then paste:**
```
Fix the duplicate charge bug described in ISSUE.md. Customers 
cust_A1B2 and cust_E5F6 are being charged twice on retry. 
Implement idempotency key support per the FTC-4421 ticket.
```

**Pause when the plan appears.**  
**Say:** *"Nothing has changed yet. Claude is showing me what it intends to do. I can push back, change scope, ask questions. This is Plan Mode."*  
**Point out:** It planned the DB table, the endpoint change, the index, the tests — all before writing a line.

**Step 2 — Approve the plan.**  
Watch it execute. When pytest fires automatically say:  
*"I didn't type that. The PostToolUse hook in CLAUDE.md fired pytest automatically. Every change self-validates."*

**Step 3 — Show the passing tests.**

---

## BEAT 03b — Git Diff + Explain Reasoning (90 seconds, CTO trust builder)
**Branch:** `main` (right after fix executes)  
**Run:**
```bash
git diff
```
**Say:** *"Every change is attributed to an engineer. Clean diff, full history. Your auditors see exactly what changed and when."*

Then ask Claude:
```
Why did you add an index on created_at specifically?
```

**Claude will explain** it's for the TTL expiry query — without an index, the 24-hour lookup table-scans at volume.  
**Say:** *"It's not pattern-matching. It's reasoning about your specific system at your specific scale."*

---

## BEAT 04 — Code Review (Parallel Agents)
**Branch:** Switch to `feat/duplicate-charge-fix`
```bash
git checkout feat/duplicate-charge-fix
```

**Say:** *"The fix is written. Now code review — but not one agent. Four, simultaneously."*

```
/code-review
```

*(Or if /code-review isn't available:)*
```
Review the changes in this branch against main. Run a security 
review, check test coverage, flag any missing edge cases, and 
verify nothing violates our CLAUDE.md conventions. Be thorough.
```

**Point out what it catches:** Missing concurrent-request test, missing index on `created_at` — things a human reviewer skims past at 5pm on a Friday.

---

## BEAT 05 — Headless CI Mode
**Branch:** either  
**Say:** *"Everything you just saw — a developer triggered it. Now watch what happens when no one is at the keyboard."*

```bash
claude -p "Find all API endpoints in this codebase that are missing authentication checks. Return a list with file name, line number, and severity." --output-format json
```

**Let it return. Point at the output.**  
**Say:** *"One line. This runs in your CI pipeline. Every pull request, before a human sees it. Your security posture doesn't depend on a developer remembering to check."*

---

## BEAT 05b — Incident Report (if time, ~90 seconds, Head of DT moment)
**Branch:** either  
**Say:** *"One more thing. This took a senior engineer two hours to write after a bad week."*

```
Write a post-incident report for FTC-4421 — the duplicate charge 
bug. Include root cause, customer impact, timeline, fix summary, 
and what we're doing to prevent recurrence.
```

**Let it run.**  
**Say:** *"That goes straight to your compliance team. Claude Code isn't just for engineers — it compresses every artifact that comes out of an incident."*  
**Who it lands with:** Head of DT specifically. This is the moment they see personal value.

---

## BEAT 06 — /init (if time, ~2 min, very strong close)
**Open a new blank directory OR say this verbally with a fresh terminal tab:**

```bash
mkdir ~/demo-blank && cd ~/demo-blank
git init
claude
```
Then inside Claude Code:
```
/init
```

**Say:** *"Watch what just happened. Claude read the (empty) repo structure and generated a CLAUDE.md with governance rules ready to fill in. In an existing repo with 180 engineers worth of code, this takes 30 seconds and gives you a governance baseline. That's how you roll this out — not a 6-week configuration project."*

---

## TIMING

| Beat | Time | Audience | Cut if running late? |
|---|---|---|---|
| 01 Onboarding | 3 min | Both | No — it's the hook |
| 02 Security audit | 3 min | CTO | No — CTO's moment |
| 02b CLAUDE.md refusal | 1 min | CTO | No — 30 sec, too good to skip |
| 03 Plan Mode + fix | 6 min | Both | Trim approval narration |
| 03b Git diff + explain | 2 min | CTO | Yes — mention verbally |
| 04 Code review | 3 min | Both | Yes — skip to result |
| 05 Headless CI | 2 min | CTO | Yes — just show the command |
| 05b Incident report | 2 min | Head of DT | Yes — strongest if time allows |
| 06 /init | 2 min | Both | Yes — verbal only |
| **Full run** | **~24 min** | | |
| **Cut version** | **~18 min** | | Drop 03b, 05b, 06 |

---

## IF SOMETHING BREAKS

- Claude hangs → `Escape`, rephrase, try again. Say: *"Let me tighten the prompt."* (This is real — it's fine.)
- Wrong output → *"Interesting — let me push back on that."* Then correct it. Shows the human-in-the-loop story.
- App not running → `pkill -f uvicorn && python3 -m uvicorn app.main:app --port 8000 &`
- On wrong branch → `git checkout main` or `git checkout feat/duplicate-charge-fix`

---

*Keep this open in a second terminal tab during the demo.*
