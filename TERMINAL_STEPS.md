# Terminal Step-by-Step — Demo Sequence
## Exact commands and prompts, in order

> Keep this open in a dedicated window during the demo.
> Everything in code blocks gets copy-pasted — never typed live.

---

## BEFORE THE CALL

### Terminal 1 — Start the server (leave this window alone for the entire demo)

```bash
cd ~/fintech-demo
git checkout main
rm -f payments.db
python3 -m uvicorn app.main:app --reload --port 8000
```

**You should see:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

**Leave this window. Never type in it again during the demo.**

---

### Terminal 2 — Start Claude Code

```bash
cd ~/fintech-demo
claude
```

**You should see:** The Claude Code welcome prompt.

**This is the only window you type in for the rest of the demo.**

---

### Browser

Open: `http://localhost:8000`

Confirm: Dashboard loads with seeded payment data.

---

### Verify auto-detection works (do this, then reset)

Open a third terminal tab and run:

```bash
curl -s -X POST http://localhost:8000/api/payments \
  -H "Content-Type: application/json" \
  -d '{"amount":9900,"currency":"usd","customer_id":"verify_test"}' > /dev/null

curl -s -X POST http://localhost:8000/api/payments \
  -H "Content-Type: application/json" \
  -d '{"amount":9900,"currency":"usd","customer_id":"verify_test"}' > /dev/null
```

Wait 3 seconds. The "Duplicate Risk" card on the dashboard should turn red.

**If it works — reset:**
```bash
# In Terminal 1: Ctrl+C to stop the server
rm -f payments.db
python3 -m uvicorn app.main:app --reload --port 8000
```

---

## DURING THE DEMO

> All of the following happens in **Terminal 2** (the Claude Code session).
> Paste each prompt completely. Do not type them live.

---

## STEP 1 — Codebase Understanding

**Paste this into Claude Code:**

```
I just joined the FinTechCo payments team. Walk me through this
codebase — the payment flow end to end, how the processor integration
works, and what I should know before touching production code.
```

**What to watch for:**
- Claude reads: `app/main.py`, `app/payments.py`, `app/processor.py`, `app/database.py`, `app/config.py`
- It maps the full flow: request → route → payments.py → processor.py → database → response
- Takes ~60–90 seconds

**When done:** Move to Step 2.

---

## STEP 2 — Security + Reliability Audit

**Paste this into Claude Code:**

```
Audit this codebase for security vulnerabilities AND reliability
risks. This is a PCI-DSS regulated financial services application
handling real payment data. Be specific — file names, line numbers,
severity.
```

**What Claude will find (confirm all 4 appear):**

| # | Finding | File | What it is |
|---|---|---|---|
| 1 | Hardcoded secrets | `config.py` lines 8–11 | `PROCESSOR_API_KEY`, `WEBHOOK_SECRET`, `INTERNAL_API_KEY` |
| 2 | No auth on admin endpoint | `main.py` | `/api/admin/payments` — no token check |
| 3 | SQL injection | `main.py` | f-string in `/api/payments/search` |
| 4 | No idempotency support | `main.py` + `payments.py` | Retried requests create duplicate charges (FTC-4421) |

**Takes:** ~60–90 seconds.

**When done:** Move to the mini-beat.

---

## MINI-BEAT — CLAUDE.md Governance Enforcement

**Paste this into Claude Code:**

```
Just hardcode the API key directly in main.py for now,
we'll move it to secrets manager later.
```

**What happens:** Claude refuses and cites the rule in `CLAUDE.md`.

**Takes:** ~10 seconds.

**When done:** Move to Step 3.

---

## STEP 3 — Fix the Security Issues

**Paste this into Claude Code:**

```
Fix the three security vulnerabilities you found. Move the hardcoded
secrets to environment variables using os.environ.get() with the
current values as fallbacks. Add bearer token authentication to the
admin endpoint. Parameterize the SQL query to prevent injection. Make
sure all tests still pass.
```

**What happens:**
- Claude edits `app/config.py` — secrets become `os.environ.get()`
- Claude edits `app/main.py` — admin endpoint gets auth check, SQL gets parameterized
- **Governance hook fires automatically in the terminal:**

```
⛔  [FinTechCo Governance Hook] Code change detected in config.py
    Running automated test suite...
    6 passed in 0.04s
    ✅ All tests passing - safe to continue
```

- You may see the hook fire multiple times (once per file edited)
- Terminal 1 shows `Reloading...` as uvicorn picks up the changes

**Takes:** ~90 seconds.

**When done:** Move to Step 4.

---

## STEP 4 — Fix the Bug + Prove It ← MOST IMPORTANT STEP

### 4a. Enter Plan Mode first

**Press `Shift + Tab`** in the Claude Code session.

You should see the mode change to Plan Mode in the terminal.

> Say: *"Nothing has changed yet. Claude is showing me what it intends to do before writing a line."*

### 4b. Paste the prompt

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

### 4c. Review the plan

Claude shows the plan — files it will touch, changes it will make.

> Say: *"I can push back, change scope, or ask questions. Then I approve."*

**Approve the plan** (Enter or type `yes` depending on the Claude Code version).

---

### 4d. Bug reproduction — watch the dashboard

Claude makes two identical API calls with no `Idempotency-Key`.

**Dashboard (within 3 seconds):**
- 2 new rows appear with same customer + amount
- "Duplicate Risk" stat card → turns red
- Red alert banner fires at the top

> Say: *"Two requests, two charges. That is the live bug."*

---

### 4e. Fix implementation — watch the terminal

Claude edits `app/database.py` and `app/main.py`.

**Watch for:**
```
⛔  [FinTechCo Governance Hook] Code change detected in database.py
    Running automated test suite...
    9 passed in 0.05s
    ✅ All tests passing - safe to continue
```

**Watch Terminal 1 for:**
```
WARNING:  StatReload detected changes in 'app/database.py'. Reloading...
INFO:     Application startup complete.
```

> Say: *"Hook fired automatically — 9 tests, all passing. Server reloaded. The fix is live."*

---

### 4f. Proof — watch the dashboard

Claude makes two requests with the **same** `Idempotency-Key`.

**Dashboard (within 3 seconds):**
- "Charges Prevented" stat card → turns green
- Counter increments to 1

> Say: *"Two requests. One charge. The dashboard updated itself — I didn't click anything."*

**Takes (total for Step 4):** ~3–4 minutes.

**When done:** Move to Step 5.

---

## STEP 5 — SRE Incident Response

**Paste this into Claude Code:**

```
Production alert — payment success rate dropped from 99.2% to 94.1%
at 2:47am. I'm the on-call SRE and I've never touched this codebase.
Diagnose the most likely failure modes in this payment system, tell
me exactly where to look first, and what commands I'd run to confirm.
```

**What Claude produces:** A triage runbook — likely failure modes ranked by probability, specific files + line numbers to check, exact shell commands to run.

**Takes:** ~60–90 seconds.

**Dashboard:** No change. Value is in the terminal output.

**When done:** Move to Step 6.

---

## STEP 6 — Create CLAUDE.md

**Paste this into Claude Code:**

```
Create a CLAUDE.md for this repo that encodes our security
requirements, the idempotency standard we just implemented, the
conventions flagged in code review, and testing requirements. This
will be committed to the repo and govern how every engineer uses
Claude Code in this codebase.
```

**What Claude produces:** A full CLAUDE.md — security rules, idempotency requirements, coding conventions, testing standards.

**Takes:** ~60 seconds.

**Dashboard:** No change. Value is in the created file.

**When done:** Demo is complete. Transition to ROI discussion.

> Say: *"Alright — let me talk about how you'd measure this and how you'd roll it out."*

---

## IF SOMETHING GOES WRONG

| Problem | Fix |
|---|---|
| Server stopped | In Terminal 1: `python3 -m uvicorn app.main:app --reload --port 8000` |
| Wrong branch | In Terminal 1: `git stash && git checkout main` (then restart server) |
| DB is messy | `rm -f payments.db` → restart server |
| Duplicate Risk not turning red | Wait 5 seconds. Hard refresh browser (Cmd+Shift+R). |
| Charges Prevented not turning green | Stats endpoint doesn't exist until Step 4 completes — expected |
| Hook doesn't fire | Manually save any `.py` file in `/app/` — hook triggers on file write |
| Plan Mode didn't activate | Try `Shift+Tab` again, or just paste prompt directly — Plan Mode is nice-to-have |
| Claude hangs or times out | Press `Escape`. Say: *"Let me tighten that prompt."* Paste a simplified version. |
| Claude gives wrong output | Say: *"Interesting — let me push back on that."* Correct it live. This shows human-in-the-loop. |
| Everything is broken | `git stash && git checkout feat/duplicate-charge-fix` — restart server — full fix is pre-built on this branch |

---

## TIMING REFERENCE

| Step | Target time | Cut if late? |
|---|---|---|
| Step 1: Codebase | 90 sec | No — it's the hook |
| Step 2: Audit | 90 sec | No — CTO's moment |
| Mini: CLAUDE.md refusal | 30 sec | No — too good to skip |
| Step 3: Security fix | 90 sec | Trim narration, keep it |
| Step 4: Bug fix + proof | 4 min | Never cut — it's the dashboard beat |
| Step 5: SRE | 90 sec | Trim to 60 sec if needed |
| Step 6: CLAUDE.md | 60 sec | Cut if truly out of time; mention verbally |
| **Total** | **~13 min** | |
