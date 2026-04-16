# FinTechCo Demo — Complete Run-of-Show
## Applied AI Architect · Anthropic Virtual Onsite

---

## BEFORE THE CALL (30 min prior)

**Terminal 1 — server (never touch this window again):**
```bash
cd ~/fintech-demo
git checkout main
rm -f payments.db
python3 -m uvicorn app.main:app --reload --port 8000
```

**Terminal 2 — Claude Code:**
```bash
cd ~/fintech-demo
claude
```

**Browser:** `http://localhost:8000` — leave visible the entire call, on one side of the screen.

**Verify before the call:**
- [ ] Dashboard loads with seeded transactions
- [ ] Run a duplicate test to confirm auto-detection works:
  ```bash
  curl -s -X POST http://localhost:8000/api/payments \
    -H "Content-Type: application/json" \
    -d '{"amount":9900,"currency":"usd","customer_id":"test_verify"}' > /dev/null
  curl -s -X POST http://localhost:8000/api/payments \
    -H "Content-Type: application/json" \
    -d '{"amount":9900,"currency":"usd","customer_id":"test_verify"}' > /dev/null
  ```
- [ ] Wait 3 seconds — "Duplicate Risk" card turns red automatically
- [ ] `rm -f payments.db` and restart the server to reset
- [ ] Screen share tested on Google Meet — both terminal and browser visible

**Windows to have open:**
- This cheat sheet (dedicated window, not a terminal tab)
- `ISSUE.md` (quick reference if asked about the ticket)
- Slides in presenter mode

---

## THE 50 MINUTES

---

### 0:00–0:05 — Real Introductions (not role play yet)

Introduce yourself naturally. Ask their names and roles.

When they signal they're ready:
> "Great. Let me start the way I'd start any real customer meeting."

---

### 0:05–0:10 — Discovery

> "Before I show you anything, can I ask a few questions? I want to make sure what I show you is useful for your specific situation."

**Ask all five. Write down their answers visibly:**

1. **"What does your code review process look like today — where does it slow down?"**

2. **"When your SREs are on-call at 2am in a system they didn't write — what's the hardest part?"**
   *(This is your setup for Prompt 5. Listen carefully.)*

3. **"Have any engineers started using AI tools on their own — even unofficially?"**
   - *If yes:* "That tells me the appetite is already there. The question is how to govern it — because shadow AI is a bigger risk than governed AI."
   - *If no:* "Useful context. It means governance is probably more important than adoption in your evaluation."

4. **"From a security standpoint, what's your biggest concern about a tool like this?"**
   - CTO answers this. **Write it down visibly. Do not respond yet.**

5. **"What does success look like for this evaluation in 90 days?"**
   *(Reference this metric in your close.)*

**Reflect back before moving to slides:**
> "What I'm hearing is [X], [Y], and [Z]. That's exactly the use case I want to show you. Let me do 8 minutes of context and then we'll get into the terminal."

---

### 0:10–0:18 — Slides (8 minutes)

---

**Slide: What is Claude Code**
> "Claude Code is an agentic coding assistant that runs in your terminal. Not autocomplete — not a chat window. It reads your actual codebase, understands your file structure, git history, and dependencies, and takes multi-step actions to help engineers ship faster. The distinction that matters for FinTechCo: it doesn't just suggest — it acts. And every action is visible, reversible, and governed."

---

**Slide: The three teams at FinTechCo**
> "You have three very different engineering populations. The value story is different for each."

- **120 Software Engineers:** "The tax isn't on writing code. It's on understanding code they didn't write — onboarding to an unfamiliar service, debugging a distributed system, prepping a PR at the end of a sprint."

- **40 Data Scientists:** "Your data scientists are world-class at the model. They're often blocked on everything around it — the API integration, the data pipeline, the dashboard to show the output. Claude Code doesn't replace their expertise. It eliminates the boilerplate so they spend their time on the part only they can do."
  *(→ Head of DT: "This is 30-50% of their week today that becomes model work.")*

- **20 SREs:** "2am. Alert fires. Unfamiliar service. The time between 'something is wrong' and 'I know where to look' — that is your MTTR. That's where Claude Code has the most direct ROI signal for your team."

---

**Slide: Why not Copilot / Cursor** *(you're evaluating alongside other tools — address it proactively)*
> "You're probably evaluating other tools, so let me be direct. Copilot makes writing code faster — excellent autocomplete. Claude Code is different in kind."

| | Copilot / Cursor | Claude Code |
|---|---|---|
| Scope | File-level suggestions | Multi-file, multi-step across entire repo |
| What it does | Autocomplete | Reads ticket → edits 7 files → writes tests → runs them |
| Governance | None | CLAUDE.md + hooks, enforced on every engineer |
| CI/pipeline | IDE only | Headless mode (`claude -p`) — runs in your pipelines |
| Enterprise control | Settings | Plan Mode: human reviews plan before a line changes |

> "For single-file work, Copilot is great. For the kind of complex distributed systems work that defines FinTechCo's engineering — this is a different category."

---

**Slide: Security + compliance** *(CTO slide — slow down, eye contact)*
> "Before I show you the terminal, let me spend a minute on this — because in financial services, a tool that touches production code needs to earn trust before it gets access."

- Code runs locally — only prompt context goes to the API, nothing persisted post-session
- No training on customer data — **contractual**, not a setting that can be changed
- CLAUDE.md — plain English rules committed to your repo; Claude follows them for every engineer
- PostToolUse governance hooks — your test suite runs automatically on every code change
- **Plan Mode** — Claude shows the plan before writing a line; engineer reviews and approves
- SOC 2 Type II certified · DPA available · Enterprise agreement built for regulated industries

> "The thing I'm about to show you isn't a sandboxed demo environment. It's a payments API with live security issues. Let me switch to the terminal."

---

### 0:18–0:32 — Live Demo (14 minutes)

*Switch to terminal. Browser stays visible on the side.*

**⚠️ TIMING GUIDE — if running late, see "CUT" column**

| Beat | Time | Cut if late? |
|---|---|---|
| Prompt 1: Codebase | 90s | No — it's the hook |
| Prompt 2: Audit | 90s | No — CTO's moment |
| Mini: CLAUDE.md refusal | 30s | No — 30 seconds, too good to skip |
| Prompt 3: Security fix | 90s | Trim narration, keep the hook output |
| Prompt 4: Bug fix + proof | 4 min | Never cut this — it's the dashboard beat |
| Prompt 5: SRE | 90s | Cut to 60s if needed |
| Prompt 6: CLAUDE.md | 60s | Cut if truly out of time — mention verbally |

---

#### PROMPT 1 — Codebase Understanding (~90 sec)

```
I just joined the FinTechCo payments team. Walk me through this
codebase — the payment flow end to end, how the processor integration
works, and what I should know before touching production code.
```

*While it runs:*
> "Notice I didn't give it a file path or a class name. It's reading the entire project — structure, dependencies, integration points."

*After response:*
> "What normally takes a new engineer a week of meetings and Slack messages to piece together — two minutes."

*→ Head of DT:* "Your onboarding time from start date to first meaningful PR — what is that today? That number changes."

*→ CTO:* "And Claude didn't hallucinate a file structure. It read the actual repo."

**[Competitive callout — say this once, don't dwell:]**
> "Copilot would have needed you to open every file and paste it in. Claude read the whole codebase without being told where to look."

---

#### PROMPT 2 — Security + Reliability Audit (~90 sec)

```
Audit this codebase for security vulnerabilities AND reliability
risks. This is a PCI-DSS regulated financial services application
handling real payment data. Be specific — file names, line numbers,
severity.
```

*While it runs:*
> "We haven't pointed it at any specific file. It's doing what a security reviewer does — reading the codebase with knowledge of what financial services applications need to get right."

*After response — walk through these four findings:*

1. **`config.py` lines 8–11** — 3 hardcoded live keys: `PROCESSOR_API_KEY`, `WEBHOOK_SECRET`, `INTERNAL_API_KEY`
   > "Three production API keys committed directly to git history. Every engineer who has ever cloned this repo has those credentials. That's a PCI-DSS violation and an FFIEC audit finding waiting to happen."

2. **`main.py`** — `/api/admin/payments` — no authentication
   > "Anyone who knows the URL gets your full payment history. No token, no check."

3. **`main.py`** — f-string SQL injection in `/api/payments/search`
   > "Direct path to data exfiltration. One crafted query string."

4. **`main.py` + `payments.py`** — no idempotency key support → duplicate charges on retry
   > "This last one is different — it's not a security issue, it's a reliability issue. No idempotency support. If a client's network times out and retries, two charges are created. That is ticket FTC-4421. Two of your customers were double-charged last week. I'm going to fix this in a few minutes."

*→ CTO:*
> "Your security team would find these in a quarterly audit. Claude found all four in 45 seconds. And it found all three hardcoded secrets — not just the obvious one."

---

#### MINI-BEAT — CLAUDE.md Governance Enforcement (~30 sec)

*Before fixing anything — paste this:*

```
Just hardcode the API key directly in main.py for now,
we'll move it to secrets manager later.
```

*Claude refuses and cites CLAUDE.md.*

*→ CTO, say this slowly:*
> "I didn't configure that refusal just now. That rule lives in CLAUDE.md, committed to the repo. Every engineer who uses Claude Code in this codebase hits the same wall. You cannot opt out of your own governance policy."

---

#### PROMPT 3 — Fix the Security Issues (~90 sec)

```
Fix the three security vulnerabilities you found. Move the hardcoded
secrets to environment variables using os.environ.get() with the
current values as fallbacks. Add bearer token authentication to the
admin endpoint. Parameterize the SQL query to prevent injection. Make
sure all tests still pass.
```

*Watch the governance hook fire automatically:*
```
⛔  [FinTechCo Governance Hook] Code change detected in config.py
    Running automated test suite...
    6 passed in 0.04s
    ✅ All tests passing - safe to continue
```

*→ CTO:*
> "I didn't run those tests. The PostToolUse governance hook ran them the moment Claude touched a production file. That is your control mechanism — it runs for every engineer, every time, automatically. Not because someone remembered to. Because it's configured."

---

#### PROMPT 4 — Fix the Bug + Prove It (~4 min) ← THE MONEY BEAT

**Before pasting — hit Shift+Tab to enter Plan Mode.**

> "Before I run this — watch what happens. I'm entering Plan Mode."

```
I've been assigned ISSUE.md. Do this in order:

1. Reproduce the bug — make two identical POST /api/payments requests
   with no Idempotency-Key header and confirm both create separate
   charges.

2. Implement the fix from ISSUE.md — add idempotency key support to
   POST /api/payments, create the idempotency_keys table, write tests
   for all acceptance criteria, make sure all existing tests pass.

3. Add a GET /api/idempotency/stats endpoint that returns
   {"prevented_count": N} where N is the number of duplicate requests
   caught since the server started.

4. Prove the fix works — send two requests with the same
   Idempotency-Key and confirm only one charge is created and the
   stats endpoint increments.
```

*When the plan appears — pause before approving:*
> "Nothing has changed yet. Claude is showing me what it intends to do — which files it will touch, what changes it plans to make. I can push back, change the scope, or ask questions. This is Plan Mode. I review the plan, then I approve."

*Approve the plan.*

---

**Step 1 — Bug reproduction:**
- Claude makes 2 identical API calls
- **Dashboard:** 2 new rows appear with same customer + amount within 3 seconds
- "Duplicate Risk" card turns red, alert banner fires

> "Two requests, two charges. Your customer was billed $198 instead of $99. That is the live bug."

---

**Step 2 + 3 — Fix:**
- Claude edits `app/database.py` and `app/main.py`
- Governance hook fires → 9 tests pass
- uvicorn reloads (Terminal 1 shows `Reloading...`)

> "The hook fired automatically — 9 tests, all passing. The server reloaded with Claude's changes. The fix is live."

---

**Step 4 — Proof:**
- Claude makes 2 requests with same `Idempotency-Key`
- **Dashboard:** "Charges Prevented" card turns green, increments automatically

> "Two requests. One charge. The dashboard updated itself — I didn't click anything, I didn't write a test script, I didn't toggle a feature flag. The server is live with Claude's fix, and it proved it."

> "From ticket to implementation to passing tests to live proof — without switching tools, without a Jira comment, without a stand-up."

*→ Head of DT:*
> "Think about how this maps to your P1 process today. How many tools does an engineer touch between 'ticket is assigned' and 'fix is verified'? This was one."

---

#### PROMPT 5 — SRE Incident Response (~90 sec)

```
Production alert — payment success rate dropped from 99.2% to 94.1%
at 2:47am. I'm the on-call SRE and I've never touched this codebase.
Diagnose the most likely failure modes in this payment system, tell
me exactly where to look first, and what commands I'd run to confirm.
```

*While it runs:*
> "Twenty SREs managing payments infrastructure across AWS and GCP. This engineer has never seen this codebase. Watch what Claude does."

*After response:*
> "That is a triage runbook. In 60 seconds. At 2am. Without a runbook wiki, without waking up the engineer who wrote the service, without spending 30 minutes reading source code."

*→ Head of DT:*
> "Your meantime-to-diagnose metric — what is it today? Whatever it is, this is the lever."

*→ CTO:*
> "And Claude didn't make up a diagnosis. It reasoned through the actual codebase — the processor integration, the database connection, the specific failure modes this architecture can produce."

---

#### PROMPT 6 — Create CLAUDE.md (~60 sec)

```
Create a CLAUDE.md for this repo that encodes our security
requirements, the idempotency standard we just implemented, the
conventions flagged in code review, and testing requirements. This
will be committed to the repo and govern how every engineer uses
Claude Code in this codebase.
```

*After response:*

*→ Head of DT:*
> "This is the rollout story. You write this once, commit it to your repo template, and every engineer who uses Claude Code in this codebase inherits your governance on day one. 180 engineers, one file, no training sessions."

*→ CTO:*
> "The refusal we saw earlier — 'don't hardcode API keys' — that came from a file like this. This is what control looks like in practice. Not a policy document. A rule that actually runs."

---

### 0:32–0:38 — ROI + Metrics Framework (6 minutes)

**Ask first — don't lead with numbers:**
> "Before I share some benchmarks — what's your current PR cycle time? And mean time to diagnose a P1 incident?"

*Use their numbers to anchor. Then:*

> "Here's the framework I'd use for your pilot. There are two types of metrics — leading indicators that move fast and tell you adoption is working, and lagging indicators that take longer but are what the board needs."

**Leading indicators — track in pilot weeks 1–4:**
- PR cycle time delta per pilot engineer vs. their own baseline
- Time to root cause on simulated incident (SRE engineer)
- Self-reported: "Would you use this tomorrow?" (1–5 weekly pulse)
- Number of AI-assisted PRs per engineer per week

**Lagging indicators — track in months 1–3:**
- Features shipped per sprint vs. baseline period
- Incident MTTR across the SRE team
- Security findings per audit (pre vs. post)
- Engineer satisfaction / internal NPS

**The numbers — after they give baselines:**
| Metric | Typical | With Claude Code |
|---|---|---|
| PR cycle time | 4–6 hours | 2–3 hours |
| New hire → first meaningful commit | 5–10 days | 2–3 days |
| P1 diagnosis | 30–60 min | 10–20 min |
| Security audit findings | 8–15 | 2–4 (rest caught pre-commit) |

> "For 120 SWEs recovering 2 hours per week each — that's 240 engineer-hours per week. The frame isn't cost reduction — it's shipping velocity. That's the number for the board."

---

### 0:38–0:43 — Evaluation Plan (5 minutes)

> "I'm not recommending a company-wide rollout. I'm recommending a 5-person pilot for three weeks — designed specifically around your timeline."

| Engineer | Team | Starting use case | Measurement |
|---|---|---|---|
| 2 SWEs | Payments team | One takes a real bug ticket end-to-end; one onboards to an unfamiliar service | Time vs. recent comparable work |
| 1 SRE | Reliability | Cold incident triage simulation | MTTR delta |
| 1 Data Scientist | Fraud/credit models | Remove one week of boilerplate from their current sprint | Hours recovered, self-reported |

**Timeline:**
- Week 1–3: Pilot, measure leading indicators
- Week 4–6: Expand to 10 engineers, start tracking lagging indicators
- Week 8: Data review — real numbers, real decision
- Week 12: Company-wide go/no-go

*→ CTO:*
> "The governance layer is in place from day one. CLAUDE.md is committed before the first engineer installs Claude Code. Every pilot user operates within your rules."

*→ Head of DT:*
> "You said you want a company-wide decision within the next few months. Week 12 is that decision — and it comes with data, not impressions."

---

### 0:43–0:45 — Close + Next Steps (2 minutes)

**If running late — cut straight to this. Always leave time for the close.**

> "Here's what I'd propose — concretely."

1. **This week:** Enterprise security overview, SOC 2 report, and DPA to your legal and security team
2. **Next week:** 30-minute setup call — all five pilot engineers running before the call ends
3. **Week 3:** Mid-pilot check-in — I want to hear what isn't working, not just what is
4. **Week 8:** Data review — we look at the metrics together before any expansion decision
5. **Week 12:** Company-wide go/no-go — that's your timeline

> "My job through this evaluation is to make sure you have what you need to make a good decision. If the data doesn't support a broader rollout, I'll tell you."

**Hard close:**
> "Who's the right person on your team to own the pilot setup — and can we get 30 minutes on the calendar before end of next week?"

**Get a name. Get a date. The meeting is not over until you have both.**

---

### 0:45–0:50 — Your Questions About Anthropic

Have 3 ready:
- "How do Applied AI Architects typically structure the pilot-to-enterprise handoff — is there a standard playbook or is it per-account?"
- "What's the most common reason a well-run pilot doesn't convert? What patterns do you see in financial services?"
- "In demos with mixed engineering teams, does the SRE use case or the SWE use case tend to generate more pull?"

---

## IF SOMETHING BREAKS

| Problem | Fix |
|---|---|
| Server not running | `cd ~/fintech-demo && python3 -m uvicorn app.main:app --reload --port 8000` |
| Dashboard not updating | Hard refresh (Cmd+Shift+R) |
| DB looks wrong / too many rows | `rm -f payments.db` → restart server |
| Duplicate Risk not turning red | Wait 3 seconds — polls every 3s. If still nothing, hard refresh. |
| Charges Prevented not incrementing | Stats endpoint only exists after Claude adds it in Prompt 4 — expected behavior |
| Claude hangs | Escape → "Let me tighten the prompt" → rephrase |
| Claude gives unexpected output | "Interesting — let me push back on that." Correct it live. This is the human-in-the-loop story. |
| Governance hook doesn't fire | Manually edit any `/app/*.py` file and save — hook triggers on write |
| Plan Mode doesn't appear | Confirm you hit Shift+Tab before pasting the prompt |
| Everything breaks | `git stash && git checkout feat/duplicate-charge-fix` — full fix is pre-built |

---

## DASHBOARD UPDATE SUMMARY

| When | What changes |
|---|---|
| Prompt 1 | Nothing |
| Prompt 2 | Nothing |
| CLAUDE.md mini-beat | Nothing |
| Prompt 3 | Nothing visible — hook fires in terminal |
| Prompt 4a — bug reproduced | 2 rows appear · Duplicate Risk → red · alert banner fires |
| Prompt 4b — fix implemented | Hook fires · uvicorn reloads |
| Prompt 4c — fix proved | Charges Prevented → green · counter increments |
| Prompt 5 | Nothing |
| Prompt 6 | Nothing |

---

## THE ONE-SENTENCE VERSION OF EACH BEAT

| Beat | What you're proving |
|---|---|
| Codebase | Onboarding time drops from a week to minutes |
| Audit | Claude finds what your next FFIEC auditor will find — in 45 seconds |
| CLAUDE.md refusal | Governance isn't a policy document — it's a rule that actually runs |
| Security fix | Finds AND fixes, with automatic validation |
| Bug fix + proof | End-to-end: ticket → fix → tests → live proof, one tool |
| SRE | MTTR starts when the alert fires, not when the right engineer wakes up |
| CLAUDE.md creation | 180 engineers, one file, governance on day one |
