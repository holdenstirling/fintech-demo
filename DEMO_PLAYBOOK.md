# FinTechCo Demo Playbook
## Anthropic Solutions Architect Interview — Claude Code

---

## What Anthropic Interviewers Want to See

This is a Solutions Architect interview, not a technical interview. They are evaluating:

| What they're watching | What good looks like |
|---|---|
| Discovery instinct | You ask before you pitch. You surface the CTO's real concern before slide 3. |
| Executive range | You can speak to the skeptical CTO and the excited Head of DT in the same breath. |
| Demo confidence | You don't narrate the screen. You narrate the value while the screen shows the work. |
| Enterprise pattern recognition | You understand that financial services sells to Legal, Security, and HR before it sells to Engineering. |
| Handling objections live | You don't get rattled when the CTO asks about data residency. You've prepared for it. |
| Clear next steps | Every SA call ends with who does what by when. Not "let's stay in touch." |
| Claude Code depth | You know the product well enough to answer "how is this different from Copilot?" without a slide. |

**The thing that separates good SAs from great ones:** They make the customer feel understood before they make them feel impressed.

---

## The Story You're Telling

This is not a product demo. It's a proof of value for a specific company with specific problems.

**One-sentence version:**
> "FinTechCo has 180 engineers across three very different teams. Claude Code lets all of them move faster — without your security team losing sleep."

**The emotional arc for the CTO:**
1. *I'm skeptical* → You understand their world (PCI-DSS, FFIEC, regulatory exposure)
2. *Show me it's safe* → Code runs locally, no training on customer data, governance hooks, CLAUDE.md
3. *Show me it works* → Live demo finding real security issues in their own codebase
4. *How do I roll it out?* → Clear phased plan with pilot → measure → expand

**The emotional arc for Head of DT:**
1. *I've been waiting for this* → Validate their instinct. They're right that this changes things.
2. *Give me a number I can take to the board* → PR cycle time, onboarding speed, incident MTTR
3. *What's my ask?* → Small pilot, clear metrics, 6-week readout

---

## Pre-Demo Setup Checklist

**30 minutes before the call:**

- [ ] `cd ~/fintech-demo && python3 -m uvicorn app.main:app --reload --port 8000`
- [ ] Open http://localhost:8000 — verify dashboard loads and shows seeded transactions
- [ ] Click "Simulate Network Retry" — verify red duplicate alert fires
- [ ] Run `python3 -m pytest tests/ -v` — all 8 tests pass
- [ ] Open a second terminal tab in `~/fintech-demo` (for running Claude Code)
- [ ] Have ISSUE.md open in a text editor for quick reference
- [ ] If demoing code review: push `feat/duplicate-charge-fix` to GitHub, open PR
- [ ] Test screen share on Google Meet before the call

**GitHub PR setup (for code review segment):**
```bash
# Create repo on github.com first, then:
cd ~/fintech-demo
git remote add origin https://github.com/YOUR_USERNAME/fintech-demo.git
git push -u origin main
git push origin feat/duplicate-charge-fix
# Open PR on GitHub: main ← feat/duplicate-charge-fix
```

**Fallback plan if GitHub isn't set up:**
Skip the `/code-review:code-review` step. Instead, show the diff manually:
```bash
git diff main...feat/duplicate-charge-fix
```
And say: "In a real workflow, this is where we'd run `/code-review:code-review --comment` to post a review directly on the PR."

---

## Audience Personas

### CTO — The Skeptic
- 20+ years in financial services, has seen tools come and go
- Primary fear: something goes wrong and it's his name on the incident report
- Speaks the language of: **risk, compliance, auditability, blast radius**
- Win him by: acknowledging the risk before he raises it
- His unspoken question: *"Who controls what this thing does?"*

**What to say to him:**
> "Before I show you anything, I want to address the thing that's probably in the back of your mind. In financial services, a tool that touches production code needs to earn trust before it gets access. Here's how Claude Code is designed with that in mind..."

### Head of Digital Transformation — The Champion
- Has been fighting internally to modernize tooling
- Primary fear: this doesn't get adopted, he looks bad
- Speaks the language of: **velocity, adoption, ROI, competitive advantage**
- Win him by: giving him the metrics story he can take to the board
- His unspoken question: *"Will my engineers actually use this?"*

**What to say to him:**
> "The adoption data from early enterprise rollouts is strong — teams that were skeptical in week one are among the heaviest users by week four. The reason is it doesn't replace what they do, it eliminates the tax on their time."

---

## Full Demo Script — 40 Minutes

### 0:00–0:02 — Open with agenda (don't pitch yet)

> "Here's what I'd like to cover. Quick discovery — a few questions from me first. Then I'll walk through what Claude Code is and why I think it's specifically relevant to FinTechCo. Live demo — about 12 minutes, focused on things your teams would actually do on day one. Then how you'd measure this and what a realistic rollout looks like. Sound good?"

---

### 0:02–0:07 — Discovery (5 questions, listen more than you talk)

> "Before I show you anything, can I ask a few questions?"

**Ask these — in this order:**

1. **"What does your current code review process look like? Where does it slow down?"**
   - Listen for: PR bottlenecks, senior engineer review bandwidth, context-switching

2. **"When your SREs are diagnosing a production incident, what's the hardest part — finding the issue or fixing it?"**
   - Listen for: unfamiliar codebases, poor documentation, time pressure

3. **"Have any of your engineers started using AI tools on their own — even unofficially?"**
   - Listen for: shadow IT, Copilot usage, ChatGPT for code
   - If yes: "That's actually useful context — it tells me appetite is there. The question becomes how to do it in a way your security team is comfortable with."

4. **"From a security perspective, what's your biggest concern about a tool like this?"**
   - Let the CTO answer. Don't jump to your response. Write it down visibly.
   - Listen for: data residency, training on proprietary code, access controls

5. **"What does success look like for this evaluation in 90 days?"**
   - Listen for: specific metrics, team size, timeline pressure

**After discovery, reflect back:**
> "What I'm hearing is [X], [Y], and [Z]. So let me make sure what I show you is specifically useful for that."

---

### 0:07–0:15 — Overview (slides, 8 minutes)

**Slide: What is Claude Code**
> "Claude Code is an agentic coding assistant that runs in your terminal. Not autocomplete, not a chat window. It reads your actual codebase, understands your file structure, git history, and dependencies — and takes multi-step actions to help your engineers ship faster."

**Slide: The three teams at FinTechCo**
> "You have three very different engineering populations. I want to talk about each one specifically."

- **Software Engineers:** Onboarding to unfamiliar services, debugging distributed systems, PR prep. "The tax isn't on writing code — it's on understanding code they didn't write."
- **Data Scientists:** FRED analysis, fraud modeling, viz work that needs a frontend dev. "They're blocked on boilerplate, not blocked on ideas."
- **SREs:** 2am incident response in code someone else wrote. "The time between 'something's wrong' and 'I know where to look' — that's where Claude Code pays off."

**Slide: Security architecture** *(slow down here for the CTO)*
> "Let me spend a minute on this because I know it matters to you."

- Code runs locally — never sent to a third party
- No training on customer data — contractual, not just policy
- You control tool permissions via CLAUDE.md — Claude follows your team's rules
- Every action is visible and reversible — you approve before anything ships
- Hooks fire automatically — your governance policy runs on every code change
- SOC 2 Type II certified

---

### 0:15–0:27 — Live Demo (12 minutes)

*Switch to terminal. Open browser at localhost:8000.*

**[SETUP — 30 seconds]**
> "Before I show you what Claude Code does, I want to show you how fast it is to set up. This is the entire installation."

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

> "That's it. No IT ticket, no VM provisioning, no license server. A developer at FinTechCo installs this in 30 seconds. Now let me show you what they can do with it."

*Switch to the fintech-demo directory. Show the running dashboard briefly.*

> "This is a simplified version of a payments API — similar architecture to what your payments team runs. Python, FastAPI, external processor integration. I'm going to use Claude Code the way one of your engineers would on their first day."

---

**[BEAT 1: Codebase Understanding — 2 min]**

*In terminal:*
```
claude "I just joined the FinTechCo payments team. Walk me through this codebase — 
the payment flow end to end, how the processor integration works, and anything 
I should know before touching this code."
```

*While Claude runs:*
> "Notice I didn't give it a file path, a class name, or a module. It's reading the entire project — understanding the structure, the dependencies, the integration points."

*After response:*
> "What just happened is what normally takes a new engineer a week of meetings and Slack messages to piece together. Two minutes."

**[Callout for Head of DT]:**
> "Your onboarding time for a new engineer to their first meaningful commit — what is that today? This changes that number."

---

**[BEAT 2: Security Audit — 2.5 min]**

```
claude "Audit this codebase for security vulnerabilities. 
This is a PCI-DSS regulated financial services application."
```

*While Claude runs:*
> "We haven't pointed it at any specific file. It's doing what a security reviewer does — reading the codebase with knowledge of what financial services applications need to get right."

*After response — Claude will surface:*
1. **Hardcoded API key in config.py** (`sk_live_4f8a2b1c9d...`)
2. **Unauthenticated admin endpoint** (`/api/admin/payments` — no auth check, returns all payment records)
3. **SQL injection in search** (`f"SELECT * ... WHERE customer_id = '{customer_id}'"`)

*Narrate for the CTO:*
> "Three issues. Any one of these would be a critical finding in a security review. The hardcoded key is a credential leak waiting to happen. The admin endpoint — anyone who knows the URL can pull your entire payment history with no authentication. The SQL injection is a direct path to data exfiltration."

> "Your security team would find these in a quarterly audit. Claude found them in 45 seconds."

**[Pause for reaction. Let the CTO respond.]**

**[Callout for CTO]:**
> "This isn't replacing your security review process. It's making sure these never reach it."

---

**[BEAT 3: Governance Hook — 30 seconds]**

> "Before we fix anything, I want to show you something we set up for this team."

*Show `.claude/settings.json`:*
> "This is a governance hook. Every time Claude modifies production code, this fires automatically — it runs the test suite and reports back. Claude can see the result and adjust. This is how you maintain code quality without adding process overhead."

> "For your security team: this means every code change Claude makes is validated against your test suite before it proceeds. You can add any check here — linting, security scanning, compliance rules."

---

**[BEAT 4: Fix the Bug — 3 min]**

*Show the dashboard. Click "Simulate Network Retry" button.*

> "Watch what happens when I simulate a network timeout on a payment request."

*Two rows appear. Red alert fires. Duplicate Risk stat card turns red.*

> "Your customer was just charged twice. This is real. Two of your customers — cust_A1B2 and cust_E5F6 — were double-charged last week. It's open as a P1."

*Show ISSUE.md briefly:*
> "Here's the ticket. Let me give this to Claude."

```
claude "I've been assigned ISSUE.md. Read it and implement the fix. 
Make sure existing tests still pass and write new tests for the 
acceptance criteria."
```

*While Claude runs — narrate:*
> "It's reading the ticket, understanding the existing code, planning the implementation. This touches four files — the database schema, the route handler, the database helpers, and the test suite."

*After Claude finishes — watch the governance hook fire:*
> "Notice the hook fired automatically. Tests ran. All passing."

*Run `pytest -v` to confirm:*
> "Eight tests, all green. The duplicate charge test now asserts the same payment ID is returned on a retry — not two separate charges."

**[Go back to dashboard. Click "Simulate Network Retry" again — now it should... still show the bug since the dashboard doesn't send an idempotency key.]*

Actually narrate:
> "The API now supports idempotency keys. When a client sends the same key twice, it gets back the original response — no second charge. The Simulate Retry button in the dashboard is still sending requests without a key, which is the raw bug. The fix is in the API — clients need to adopt the key."

---

**[BEAT 5: Code Review — 2 min]**

> "Before anything ships to production, it goes through review. We have a PR open."

*Switch to terminal. On the feat/duplicate-charge-fix branch:*
```
/code-review:code-review
```

*While it runs:*
> "This is running four agents in parallel — two checking for CLAUDE.md compliance, one scanning for bugs, one analyzing git history for context. Each finding gets a confidence score. Only issues above 80 confidence surface."

*After review — it will flag:*
- Missing test for expired idempotency key behaviour (acceptance criterion from ISSUE.md)
- Missing database index on `idempotency_keys.created_at` (performance issue at scale)

> "Two findings. The expired key test is actually in the acceptance criteria on the ticket — it was missed. The missing index is a performance issue that would only show up at FinTechCo's transaction volume. A code reviewer might catch it. Claude caught it automatically."

**[Callout for CTO]:**
> "This is the control mechanism. Nothing ships without review. Claude Code implements, code review validates, you decide what merges."

> "Your engineers are in control of what goes to production. Claude is doing the work. The human approves the result."

---

**[BEAT 6: Rollout Artifacts — 1 min]**

*Show CLAUDE.md:*
> "This is a CLAUDE.md file — it's a set of rules Claude reads every time it touches this repo. No hardcoded secrets. Parameterized queries only. All endpoints need auth. Idempotency required for state-mutating endpoints."

> "This is how you scale governance across 120 engineers. You write the rules once, in plain English. Claude follows them on every change, for every engineer, automatically."

> "When you onboard a new engineer, they get Claude Code and this file. Day one, they're operating within your team's standards."

---

### 0:27–0:32 — ROI & Metrics (5 min)

**Don't present numbers. Ask first:**
> "Quick question — what's your average PR cycle time today? And what's your mean time to diagnose a P1 incident?"

*(Write down their answers.)*

> "Those are your baselines. Here's the framework I'd use to measure this."

**Leading indicators (weeks 1–4):**
- PR cycle time (open → merge)
- Time to first commit for new engineers
- Test coverage delta

**Lagging indicators (months 1–3):**
- Features shipped per sprint
- Incident MTTR
- Engineer satisfaction (internal NPS)

**FinTechCo-specific:**
> "The SRE story is where I'd focus first for you. Twenty engineers managing incidents across payments infrastructure — the time between 'alert fires' and 'I know where to look' is measurable and it's where Claude Code has the strongest ROI signal."

---

### 0:32–0:37 — Evaluation Plan (5 min)

> "I'm not recommending a company-wide rollout. I'm recommending a 5-person pilot for three weeks."

| Phase | Who | What | Success Signal |
|---|---|---|---|
| Week 1–3 | 2 engineers, 1 data scientist, 1 SRE, 1 PM | Install, use on real work, track time | "Would I use this daily?" |
| Week 4–6 | Broader team | Expand based on pilot signal | Baseline vs. post metrics |
| Week 7–12 | Company-wide | Enterprise agreement, CLAUDE.md rollout | ROI readout |

> "Setup for the pilot is 30 minutes total. I'll be on a call with whoever owns this from your side. No IT involvement required, no procurement — this is a trial."

**On legal/compliance:**
> "I know that in financial services, 'no procurement required' sometimes isn't true. We have an enterprise agreement template designed for regulated industries — it covers data processing, security, IP ownership, and compliance documentation. Happy to get that to your legal team this week."

**On rollout to all 180 engineers:**
> "The way enterprises roll this out fastest is a CLAUDE.md-first approach. You define your standards in that file, distribute it with a repo template, and every team that adopts Claude Code inherits your governance on day one."

---

### 0:37–0:40 — Close (3 min)

> "Here's what I'd propose as next steps."

1. **This week:** I send you the enterprise security overview and data processing agreement for your legal team
2. **Next week:** 30-minute setup call with whoever you designate for the pilot — we have them up and running before the call ends
3. **Week 3:** Mid-pilot check-in — I want to hear what's working and what isn't
4. **Week 6:** Pilot readout — data, decision on broader rollout

> "My job through this evaluation is to make sure you have everything you need to make a good decision. That means if the pilot data doesn't support a broader rollout, I'll tell you that."

**Hard close:**
> "Who's the right person on your team to own the pilot setup?"

*(Get a name. Get a date.)*

---

## Potential Issues & How to Handle Them

### Demo Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| Server not running | High if not checked | Pre-start server, bookmark localhost:8000, have `uvicorn` command ready |
| Claude Code slow / times out | Medium | Have a recorded backup of each beat. Say: "I'll let this run and come back to it." |
| GitHub PR not set up for code review | Medium | Demo the diff with `git diff main...feat/duplicate-charge-fix` instead |
| Security audit doesn't find all 3 vulns | Low | They're real vulns — Claude will find them. If it only finds 2, pivot: "Let me show you the third one directly" |
| Governance hook doesn't fire visually | Medium | Demo it separately: edit a file, show the hook output |
| Idempotency fix breaks an existing test | Low | All 8 pass on feature branch. If something breaks during live impl, say: "This is exactly what the governance hook is for — catching it before it ships." |
| Internet drops mid-demo | Low | Claude Code still works locally. Only GitHub PR step needs internet. |

### Objections by Persona

**CTO — "Our code can't leave our environment"**
> "It doesn't. Claude Code runs in your terminal and communicates with the Claude API — only the prompt and relevant code context goes over the wire, nothing is persisted on Anthropic's side after the session ends. We also support private deployment configurations for air-gapped environments. What specific compliance framework are you operating under? I want to make sure I give you the right documentation."

**CTO — "How do we know Anthropic isn't training on our code?"**
> "Our enterprise terms explicitly prohibit using customer API inputs for model training. This isn't a policy that can be quietly changed — it's in the contract. I can get you the specific clause. The architecture also reinforces this — Claude Code sends a session context to the API and gets a response; there's no persistent storage of that context on our end."

**CTO — "What happens when it makes a wrong change?"**
> "Every edit Claude makes is shown to the engineer before it's applied. There's no silent auto-apply. And with the governance hook we showed — your test suite validates every change automatically. If Claude breaks something, the tests tell it immediately and it fixes the issue in the same session. The blast radius is always visible and always reversible before it hits version control."

**CTO — "We'd need to go through procurement"**
> "Understood — that's true for any tool in a regulated environment. We have an enterprise agreement template built for financial services that's been through legal review at similar firms. If you can tell me who owns vendor security assessments on your side, I can make sure they have what they need to move quickly."

**Head of DT — "My engineers won't adopt it"**
> "That's the most common concern and the one that disappears fastest. The engineers who are most skeptical are usually the ones who've tried worse AI tools and got burned. The pitch isn't 'use AI instead of thinking' — it's 'stop spending 2 hours understanding a microservice you didn't write before you can start the task you were actually hired to do.' That lands differently."

**Both — "GitHub Copilot already does this"**
> "Copilot is excellent autocomplete — it makes writing code faster. Claude Code is different in kind: it takes multi-step actions across your entire repo, reasons about systems not just files, and can do things like what you just saw — reading a ticket, understanding 7 files, implementing a fix, writing tests, and validating the result. For simple single-file edits, Copilot is great. For the kind of work your senior engineers do on complex distributed systems — this is a different category of tool."

---

## The Humanizing Moments

These are small things that make the demo feel real instead of rehearsed:

- **Before the security audit:** "I'm genuinely curious what it finds here — this codebase has some issues I put in intentionally, but Claude doesn't know that."
- **When the governance hook fires:** "That hook just ran your test suite automatically. That's governance without a meeting."
- **When code review catches the missing test:** "That acceptance criterion was in the original ticket. It was missed in the implementation. Code review caught it. This is the loop."
- **On CLAUDE.md:** "This is plain English. Any engineer on your team can read it, edit it, and understand it. No configuration files, no YAML."
- **On setup time:** "I installed this 20 minutes before this call. I didn't need anyone's permission."

---

## What Financial Services Customers Care About

In order of actual priority (not what they say out loud):

1. **"Who's responsible when something goes wrong?"** → Clear audit trail, human-in-the-loop approval before ship
2. **"Is our IP protected?"** → No training on code, contractual data processing agreement
3. **"Can we turn it off?"** → Yes. It's a CLI. `rm -rf ~/.local/bin/claude` is the uninstall.
4. **"What does our regulator think?"** → Honest answer: AI coding tools are not yet regulated directly. CLAUDE.md + governance hooks are your control evidence.
5. **"Will this work with our stack?"** → Python, TypeScript, Java, Go — all first-class. Show the stack matrix.
6. **"How do we train 180 people on this?"** → You don't. You give them 30 minutes and CLAUDE.md. The ramp is days, not weeks.

---

## Demo Commands — Copy/Paste Ready

**Start server:**
```bash
cd ~/fintech-demo && python3 -m uvicorn app.main:app --reload --port 8000
```

**Run tests:**
```bash
cd ~/fintech-demo && python3 -m pytest tests/ -v
```

**Start Claude Code:**
```bash
cd ~/fintech-demo && claude
```

**The 4 demo prompts (in order):**
```
1. I just joined the FinTechCo payments team. Walk me through this codebase —
   the payment flow end to end, how the processor integration works, and what
   I should know before touching production code.

2. Audit this codebase for security vulnerabilities. This is a PCI-DSS
   regulated financial services application handling real payment data.

3. I've been assigned ISSUE.md. Implement the fix described, write tests
   proving duplicate charges no longer happen, and make sure all existing
   tests still pass.

4. Create a CLAUDE.md for this repo that captures our security requirements,
   coding conventions, and the idempotency pattern we just implemented.
```

**Code review (run inside Claude Code session on feat branch):**
```
/code-review:code-review
```

**Show git diff if GitHub PR isn't set up:**
```bash
git diff main...feat/duplicate-charge-fix
```

---

## Git Branch Reference

| Branch | State | Purpose |
|---|---|---|
| `main` | No idempotency, 3 security vulns | Starting point for live "implement from scratch" demo |
| `feat/duplicate-charge-fix` | Idempotency implemented, 2 known gaps | Pre-built for code review demo |

**Switch to main for live implementation demo:**
```bash
git checkout main
```

**Switch to feature branch for code review demo:**
```bash
git checkout feat/duplicate-charge-fix
```
