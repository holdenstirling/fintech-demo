# FinTechCo Demo — Definitive Guide v4
**40-minute mock customer meeting · ~13-minute live demo**
**Audience:** CTO (skeptical, security-first, 20+ yrs fintech) · Head of Digital Transformation (champion, wants productivity wins)

---

## Key Framing — Say This, Not That

| Don't say | Say instead |
|---|---|
| "AI coding assistant" | "Agentic coding tool — it reads, reasons, acts, and validates" |
| "It writes code for you" | "It's an extension of your team — unlimited capacity, same rigor" |
| "Chat with your codebase" | "It operates across your full SDLC — build, test, review, deploy" |
| "Like Copilot but better" | "Copilot autocompletes lines. Claude Code executes multi-step workflows across your whole repo" |
| "It can help with..." | "Watch — it's about to read 7 files, edit 2, run 13 tests, create a branch, and open a PR. One prompt." |

---

## Terminal Setup — Start to Finish

### 30 Minutes Before the Call

**Terminal 1 — Server (never touch again)**
```bash
cd ~/fintech-demo
git checkout main
git restore .                    # reset any leftover changes
rm -f payments.db                # force fresh seed data
python3 -m uvicorn app.main:app --reload --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Started reloader process [...] using WatchFiles
INFO:     Application startup complete.
```

**Terminal 2 — Claude Code (this is your demo window)**
```bash
cd ~/fintech-demo
claude
```

Once inside, type `/fast` to enable fast mode (same Opus model, faster output).

You should see the Claude Code welcome prompt. **This is the only window you interact with during the entire demo.**

**Browser**
Open `http://localhost:8000` — position it so both the terminal and dashboard are visible during screen share.

### Pre-Flight Checklist

- [ ] Dashboard loads with 25 seeded transactions
- [ ] Amounts show **$9,900** (bug is active — `formatAmount` missing `/100`)
- [ ] Success rate shows **99.2%** (P1 not triggered yet)
- [ ] "Simulate P1 Incident" button is **red and enabled** (not greyed out)
- [ ] 3 failed transactions visible (red badges) among the green ones
- [ ] Claude Code is open in Terminal 2, **fresh session**, `/fast` ON
- [ ] This guide is open in a separate window (not a terminal tab)

> **If amounts show correctly at start:** The formatAmount bug was fixed from a prior run. Run `git restore .` and restart the server.
> **If the table is empty:** Old `payments.db` wasn't deleted. `rm -f payments.db` and restart.

---

## What Claude Code Actually Does During This Demo

This is what makes the demo technical. Claude Code isn't autocompleting — it's executing an agentic workflow. Call out these tool calls as they happen:

| What you'll see in terminal | What it is | Why it matters |
|---|---|---|
| `Read(file_path="app/main.py")` | File read tool | Claude is reading your actual source — not guessing from training data |
| `Grep(pattern="formatAmount")` | Code search tool | Searching across the entire repo, not just the open file |
| `Edit(file_path="...", old_string, new_string)` | Surgical file edit | Targeted diff — not rewriting the whole file |
| `Bash(command="python3 -m pytest tests/ -v")` | Shell execution | Running your test suite directly — same as a developer would |
| `Bash(command="git checkout -b fix/...")` | Git branch creation | Full git workflow — branch, commit, push, all from natural language |
| `Bash(command="gh pr create --title ...")` | GitHub CLI | Opens a real PR on GitHub — not a mock, not a simulation |
| `Bash(command="curl -s -X POST ...")` | API call to notify dashboard | Calls the app's own API to trigger the PR banner |

> **Key talking point:** "Every one of these tool calls is visible. You can see exactly what Claude is doing, approve or reject each action. Full audit trail. This is what 'human in the loop' actually looks like — not a checkbox, but a live approval workflow."

---

## The Five Prompts — Technical Breakdown

Each prompt is designed to demonstrate a different phase of the SDLC. The prompts are short because that's how engineers actually work — they describe the problem, not the solution.

| # | SDLC Phase | What Claude does | Tool calls you'll see |
|---|---|---|---|
| 1 | **Understand** | Reads the entire codebase, maps the architecture | 6-8 `Read` calls, dependency analysis |
| 2 | **Build** | Finds bug across frontend/backend boundary, writes the fix | `Grep` → `Read` → `Edit` |
| 3 | **Test / Diagnose** | Traces a production incident across 3 files, identifies root cause chain | Multiple `Read` calls, cross-file reasoning |
| 4 | **Build + Test** | Implements fix across 2 files, runs full test suite | `Edit` × 2 → `Bash(pytest)` — 13 tests pass |
| 5 | **Review + Deploy** | Creates branch, commits, pushes, opens PR on GitHub | `Bash(git)` × 4 → `Bash(gh pr create)` → dashboard updates |

> **Talking point:** "That's the full software development lifecycle — understand, build, test, review, deploy — in five prompts. Same rigor your team applies manually. Same tools. Same workflow. But now one engineer can do what used to require three, and the junior engineer operates with the same guardrails as the senior."

---

## Full Demo Script

### SEQUENCE (memorize this)

```
Prompt 1 → Prompt 2 → REFRESH BROWSER → transition line → CLICK P1 BUTTON → Prompt 3 → Prompt 4 → dashboard resolves → Prompt 5 → PR banner appears → CLAUDE.md governance close
```

---

### Setup (30 sec — you talk, don't touch Claude)

Switch to browser. Point at dashboard.

> "Let me set the scene. This is a real payments service — FastAPI backend, SQLite, external processor integration. Day one for a new engineer. They've just been given access to the codebase and the dashboard."

Point at the $9,900 amounts.

> "First thing they notice: something's off."

---

### Prompt 1 — Codebase Understanding (2 min)

**SDLC phase: UNDERSTAND**

```
Walk me through this codebase — what does it do, how does money move through it, what should I know before I touch anything?
```

**While Claude runs (~35 sec) — call out tool calls:**

> "Watch the tool calls in the terminal. `Read` on `main.py`, `payments.py`, `processor.py`, `database.py`, `config.py`, `models.py`. It's reading the entire service — routes, business logic, the external processor integration, the database schema. No file paths in the prompt. It found them."

> "This is how Claude Code works as an agent. It doesn't wait for you to open files. It uses `Read`, `Grep`, `Glob` tools to explore the codebase autonomously — the same way a senior engineer would `cd` around a new repo."

**After response:**

> "Payment flow end to end. Processor isolation pattern. Security issues it flagged unprompted. What normally takes a new engineer a week of onboarding — meetings, Slack, wiki pages — took 30 seconds."

> "And this works the same way whether Claude Code is running in the terminal, in VS Code, or in JetBrains. Same agent, same capabilities. Your team picks their environment."

---

### Prompt 2 — Visual Bug Fix (2 min)

**SDLC phase: BUILD**

Point at $9,900 amounts on dashboard.

> "Every transaction is 100x the actual amount. In a payments dashboard, that's alarming."

```
Dashboard is showing amounts 100x too high — a $99 charge shows as $9,900. Find and fix it.
```

**While Claude runs (~30 sec):**

> "No file name. No line number. Described it the way a Slack message from product would read. Watch — it's about to `Grep` for the formatting function, `Read` the file, and `Edit` the exact line."

> "This is the difference between autocomplete and an agent. Copilot needs you to have the right file open. Claude Code searches the codebase, finds `formatAmount()` in `index.html`, identifies that it's passing raw cents to `Intl.NumberFormat` without dividing by 100, and writes the one-line fix."

**After response:**

> "Found it. `static/index.html`, the `formatAmount` function. Amounts stored in cents, displayed as dollars. One line — `cents / 100`."

**Refresh the browser. Amounts now correct.**

> "Fixed. The server is running with `--reload`, so it picked up the change automatically. For 180 engineers, that's the difference between a 20-minute debugging session and 30 seconds."

---

### CLICK "SIMULATE P1 INCIDENT" NOW

> "Now let me show you what keeps your SREs up at night."

**Click the button.** Red P1 banner appears. Success rate drops 99.2% → 94.1%. Duplicate charge rows appear in the table.

> "Payment success rate just cratered. Customers are being double-charged."

---

### Prompt 3 — P1 Diagnosis (2.5 min)

**SDLC phase: TEST / DIAGNOSE**

```
P1 — success rate dropped from 99.2% to 94.1%, duplicate charges hitting same customers. Diagnose root cause.
```

**While Claude runs (~45 sec) — this is your technical depth moment:**

> "This is what your on-call SRE does at 2:47am when this alert fires. Except instead of spending 20 minutes reading files they've never seen, they have an agent that reads the entire payment path in seconds."

> "Watch the tool calls — it's reading `payments.py`, then `processor.py`, then cross-referencing with `CLAUDE.md` to understand what the architecture *should* look like versus what it actually does. That's multi-file reasoning. Not pattern matching — reasoning."

> "Think about the scale here. 180 engineers, dozens of services. Claude Code doesn't just know the file you're in — it understands the dependency chain across your whole system. That's what turns a junior engineer into someone who can triage a P1 on a service they've never seen."

**After response — walk through the root cause chain:**

> "Two bugs, one incident. First: `processor.py` line 28 — every call to the external processor generates a fresh random UUID as the idempotency key. Retries send a different key. The processor treats it as a new charge. Second: `payments.py` — no error handling around the processor call. A timeout becomes an unhandled 500, the client retries, and you get a double charge."

> "Claude didn't just find one bug. It traced the full failure chain across two files and explained how they interact. That's the difference between 'I found a bug' and 'I understand why your customers were double-charged.'"

---

### Prompt 4 — P1 Fix (2.5 min)

**SDLC phase: BUILD + TEST**

```
Fix it. Make sure all tests pass.
```

**While Claude runs (~45 sec) — call out the agentic workflow:**

> "Five words. Watch what happens. It's about to edit `processor.py` — add a stable idempotency key parameter, add error classification. Then `payments.py` — reorder the payment ID generation, wrap the processor call in error handling. Then — and this is key — it runs `pytest` itself."

> "That `Bash` tool call running `python3 -m pytest tests/ -v` — Claude decided to do that. Not a hook. Not a script. The agent knows that in a regulated codebase, the fix isn't done until the tests pass. Same engineering rigor your senior engineers apply. Same workflow. Automated."

**After response — 13 tests pass:**

> "13 tests. All green. The server reloaded with `--reload`. Watch the dashboard."

**Pause. Watch the dashboard. Stay silent.**

Within 3 seconds: P1 banner clears, success rate animates back to 99.2%.

> "P1 resolved. Dashboard picked it up. No manual refresh, no deployment script. The `--reload` flag on uvicorn detected the file change and restarted the server."

**Let it land.**

---

### Prompt 5 — PR for Review (2 min)

**SDLC phase: REVIEW + DEPLOY**

> "Fix works. Tests pass. In a regulated environment, you don't merge to main without review."

```
Push a PR for this fix so the team can review it.
```

**While Claude runs (~25 sec) — this is the agent power moment:**

> "This is where Claude Code is fundamentally different from any other AI coding tool. Watch the tool calls."

> "`Bash: git checkout -b fix/ftc-4421-duplicate-charges` — creates the branch. `Bash: git add` — stages the changed files. `Bash: git commit` — writes the commit message with the fix context. `Bash: git push -u origin` — pushes to GitHub. `Bash: gh pr create` — opens the PR with a summary, test plan, and linked issue. Then it calls the dashboard notification API so the team sees it immediately."

> "Six shell commands. Branch, stage, commit, push, open PR, notify. All from 'push a PR.' That's what agentic means — Claude Code doesn't just write code. It operates across your entire toolchain. Git, GitHub CLI, shell commands, API calls. It's an extension of your engineering team with unlimited capacity."

**Green PR banner appears on dashboard within 3 seconds.**

> "The dashboard picked it up. Your team can see there's an open PR before anyone checks Slack or email. Click the link — that's a real PR on GitHub."

---

### Governance Close (2 min — no Claude, you talk)

> "The last thing I want to show you isn't a prompt."

Open `CLAUDE.md` in the terminal:
```
cat CLAUDE.md
```

> "This file — `CLAUDE.md` — is committed to the repo. It encodes your PCI-DSS requirements, authentication patterns, the idempotency standard we just fixed, testing rules, SQL injection prevention. Plain English. Every engineer who opens Claude Code on this repo reads this file automatically. New hire, contractor, offshore team — same guardrails. Day one."

**For the CTO:**
> "This is the answer to your compliance question. Your engineering standards aren't in a Confluence page nobody reads. They travel with the codebase, and they're enforced automatically."

**For the Head of Digital Transformation:**
> "When you roll this out to 180 engineers, you don't train each of them on your security requirements. You write them once. The tool enforces them."

---

## Timing Reference

| Segment | Clock | Claude? | Tool calls to watch |
|---|---|---|---|
| Setup narration | 0:00–0:30 | No | — |
| Prompt 1: Understand | 0:30–2:30 | Yes (~35s) | `Read` × 6-8, `Grep` |
| Prompt 2: Build (bug fix) | 2:30–5:00 | Yes (~30s) | `Grep` → `Read` → `Edit` |
| Click P1 | 5:00–5:15 | No | — |
| Prompt 3: Diagnose | 5:15–7:45 | Yes (~45s) | `Read` × 3, cross-file analysis |
| Prompt 4: Build + Test | 7:45–10:00 | Yes (~45s) | `Edit` × 2 → `Bash(pytest)` |
| Dashboard resolves | 10:00–10:15 | No | Stay silent |
| Prompt 5: Review + Deploy | 10:15–12:15 | Yes (~25s) | `Bash(git)` × 4, `Bash(gh pr)`, API call |
| Governance / `CLAUDE.md` | 12:15–13:30 | No | `cat CLAUDE.md` |

---

## What to Say During Downtime (While Claude Runs)

These are your 30–45 second windows. Don't fill every second — silence while the tool calls scroll is powerful. But have these ready.

### Technical depth (for the CTO)

- "Every tool call you see in the terminal is logged. Enterprise tier gives you full audit trails — what Claude read, what it edited, what commands it ran. Your compliance team can review any session."

- "Claude Code runs in the terminal, but it also runs as a VS Code extension and a JetBrains plugin. Same underlying agent. Your engineers pick their environment — the governance layer is the same."

- "The `Edit` tool does a targeted string replacement — it's not rewriting the whole file. That means cleaner diffs, easier code review, and fewer merge conflicts."

- "Notice Claude is using parameterized SQL queries in the fix. It read the CLAUDE.md rule about SQL injection and applied it. That's not a coincidence — that's the governance layer in action."

### Scale framing (for Head of DT)

- "Think about this at scale. 180 engineers, each saving 30 minutes a day on code comprehension and debugging. That's 90 engineer-hours per day back into shipping features."

- "The PR Claude just created — a human reviews it. But the human is reviewing a well-structured diff with test coverage, not spending an hour writing it. That's the multiplier."

- "Your junior engineers operate at the level of your seniors. Your seniors operate at the level of a team. That's what 'unlimited capacity' means — not replacing engineers, extending them."

- "Every new hire inherits the CLAUDE.md guardrails on day one. No onboarding lag for your engineering standards. The tool teaches them your conventions as they work."

### If Claude is taking longer than expected

- "Complex reasoning takes a moment. The same way a senior engineer pauses to think through a multi-file change before writing code."

- Point at the tool calls scrolling: "You can see it working — reading the processor integration, cross-referencing with the payment flow. This isn't a timeout. It's doing the work."

---

## If Things Go Wrong

| Problem | Fix | What to say |
|---|---|---|
| Claude response is very long | Scroll to the summary | "It found the issue — here's the key part." |
| Dashboard doesn't update after fix | Manual refresh (Cmd+R) | "Server reloaded — let me refresh." |
| P1 button greyed out | Server wasn't restarted. `Ctrl+C` → `rm -f payments.db` → restart | "Let me reset the environment." |
| Amounts showing correctly at start | `git restore .` and restart server | — |
| Table is empty | `rm -f payments.db` → restart server | — |
| PR banner doesn't appear | Wait 3 seconds (poll cycle) | "Dashboard polls every 3 seconds — there it is." |
| Claude gives wrong answer | Rephrase once | "Let me tighten that prompt." Shows human-in-the-loop. |
| Claude hangs | Press `Escape`, rephrase | "Let me be more specific." |
| Server died | In Terminal 1: `cd ~/fintech-demo && python3 -m uvicorn app.main:app --reload --port 8000` | "Let me restart the server." |
| Port 8000 in use | `lsof -ti :8000 \| xargs kill` then restart | — |

---

## Stakeholder Cheat Sheet

### For the CTO (security, control, compliance)
- "Every tool call is visible and auditable. Full session logs in enterprise tier."
- "CLAUDE.md is your enforcement layer — committed to the repo, not a wiki page."
- "Human approves every write action. That's the design, not a limitation."
- "SOC 2 Type II. No training on your code — contractual, not a setting."
- "Same agent runs in CLI, VS Code, JetBrains. Governance is environment-agnostic."

### For the Head of DT (scale, velocity, team extension)
- "One tool across the full SDLC — understand, build, test, review, deploy."
- "Extension of your team with unlimited capacity. Junior engineers ship like seniors."
- "180 engineers, one CLAUDE.md file. Governance scales without training sessions."
- "Time-to-first-PR for new hires drops from weeks to days."
- "It doesn't just write code — it runs git, opens PRs, executes tests, calls APIs. Full agent."

---

## The Five Prompts — Copy-Paste Ready

```
PROMPT 1 — UNDERSTAND
Walk me through this codebase — what does it do, how does money move through it, what should I know before I touch anything?
```

```
PROMPT 2 — BUILD (bug fix)
Dashboard is showing amounts 100x too high — a $99 charge shows as $9,900. Find and fix it.
```

```
PROMPT 3 — DIAGNOSE
P1 — success rate dropped from 99.2% to 94.1%, duplicate charges hitting same customers. Diagnose root cause.
```

```
PROMPT 4 — BUILD + TEST
Fix it. Make sure all tests pass.
```

```
PROMPT 5 — REVIEW + DEPLOY
Push a PR for this fix so the team can review it.
```

---

## Quick Reset Between Runs

If you need to reset for another demo run:

```bash
# In Terminal 2 (Claude Code) — exit the session
/exit

# In a terminal:
cd ~/fintech-demo
# Close any open PRs and delete fix branches
gh pr close $(gh pr list --json number -q '.[0].number') 2>/dev/null
git checkout main
git restore .
git push origin --delete fix/ftc-4421-duplicate-charges 2>/dev/null
git branch -D fix/ftc-4421-duplicate-charges 2>/dev/null
rm -f payments.db
# Kill and restart server
lsof -ti :8000 | xargs kill 2>/dev/null
python3 -m uvicorn app.main:app --reload --port 8000 &

# Start fresh Claude Code session
claude
# Then type /fast inside Claude Code
```

Verify the checklist at the top of this doc, then you're good to go.
