# Demo Cheat Sheet — Thursday 4/16
## Keep this open in a second window during the call

---

## START (30 min before)
```bash
pkill -f uvicorn
rm -f ~/fintech-demo/payments.db
cd ~/fintech-demo && git checkout feat/duplicate-charge-fix
python3 -m uvicorn app.main:app --port 8000
```
Open http://localhost:8000 — verify:
- Customer Impact card is **red** (P1 ACTIVE, $198/$398 overcharge showing)
- "Run Security Audit" → all 5 vulns animate in
- "Demo: Show Bug" → HTTP Trace appears, DUPLICATE badge fires
- "Demo: Show Fix" → Trace updates to 200 OK, Impact card turns **green**
- "Reset Demo" → everything clears cleanly

**Verify governance hook:** Open a second terminal tab. Run `cd ~/fintech-demo && claude`. Make a trivial edit to `app/config.py`. Look for `⛔ [FinTechCo Governance Hook]` → `✅ All tests passing`. If it doesn't fire, restart Claude Code from inside the repo directory.

**Verify code review plugin:** Inside the Claude session, type `/plugin list`. If `code-review` isn't there: `/plugin install code-review`.

---

## THE 40-MINUTE MAP

| Time | What | Screen |
|------|------|--------|
| 0:00 | Agenda — frame the 40 min, confirm who's in the room | Nothing |
| 0:02 | **Discovery** — ask Q1–Q5, listen more than you talk | Nothing |
| 0:08 | Reflect back: *"What I'm hearing is X and Y…"* | Nothing |
| 0:09 | Overview — Claude Code is agentic, not autocomplete | Nothing |
| 0:12 | Security architecture — slow down here for CTO | Nothing |
| 0:14 | Switch to browser — show dashboard. Point to red Impact card. *"This is your current state. P1 open. Two customers overcharged. Let me show you what a morning with Claude Code looks like."* | Browser |
| 0:15 | **[BEAT 0]** Terminal — paste Prompt 1 slowly | Terminal |
| 0:15:30 | ⚡ **ESCAPE HATCH A** — *see below* — narrate while Claude runs | Terminal |
| 0:17 | → **HEAD OF DT CALLOUT** — ask directly: *"What's your time from new hire to first meaningful commit?"* Let them answer. *"That just happened in 90 seconds."* | Terminal |
| 0:18 | **[BEAT 1]** Browser — Click "Run Security Audit" → **stay completely quiet** | Browser |
| 0:20 | Narrate 5 findings — *"Three production secrets in git history. PCI-DSS and FFIEC non-compliant. That's your next exam finding."* | Browser |
| 0:21 | ⏸ **PAUSE 1** — *"That's what came back. What's your reaction to those findings?"* Write down what CTO says. | Browser |
| 0:22:30 | **[BEAT 2a]** Click "Demo: Show Bug" → HTTP Trace, DUPLICATE badge | Browser |
| 0:23 | Point to Impact card — *"cust_A1B2. They called your support line. Charged $99 twice. This is the P1 ticket."* | Browser |
| 0:23:30 | Terminal — show ISSUE.md for 10 seconds, then paste Prompt 3 slowly | Terminal |
| 0:24 | ⚡ **ESCAPE HATCH B** — *see below* — narrate while Claude runs | Terminal |
| 0:26 | Governance hook fires — *"That ran automatically. I didn't type a command."* | Terminal |
| 0:26:30 | **[BEAT 2b]** Browser — Click "Demo: Show Fix" → HTTP Trace updates | Browser |
| 0:27 | Point to Impact card turning green — *"cust_A1B2. $99. One charge."* Let it land. | Browser |
| 0:27:30 | ⏸ **PAUSE 2** — *"Questions before I show you the control layer?"* | Browser |
| 0:28 | Editor — CLAUDE.md — *"Your team's rules. Plain English. Every engineer, every change."* | Editor |
| 0:29 | Editor — settings.json — *"This is what fired. One file, committed to the repo."* | Editor |
| 0:30 | **[BEAT 3]** Terminal — `/code-review:code-review` on PR #1 | Terminal |
| 0:32 | Editor — DEMO_TODO.md → **CLOSE BRIDGE** — *see below* | Editor |
| 0:34 | Ask baselines: *"What's your PR cycle time today? MTTR on a P1?"* | Nothing |
| 0:36 | ROI framework — use their numbers | Nothing |
| 0:38 | Evaluation plan — 5-person pilot, 3 weeks | Nothing |
| 0:39 | **CLOSE** — *see below* | Nothing |

---

## ⚡ ESCAPE HATCH A — while codebase walkthrough runs (0:15:30)

Claude will take 60-120 seconds. Say this while it runs:

> "I want to be transparent — this is running live right now, reading your actual codebase. I haven't pre-loaded anything. It's mapping the payment flow, the processor integration, the database layer, the test coverage. What would normally take an engineer their first week of meetings and Slack messages."

Then stay quiet for 20 seconds. Let the terminal scroll.

> "For your SRE team — imagine it's 2am, alert fires, service owned by a team that's off. Instead of paging someone, they ask this. Time to understand the blast radius goes from 40 minutes to 5."

If Claude is still running: *"[Head of DT], what's your current onboarding time for a new engineer to a service they've never touched?"*

---

## ⚡ ESCAPE HATCH B — while live fix runs (0:24)

Claude will take 3-6 minutes for a real implementation. **Don't wait at a terminal.**

After pasting Prompt 3, immediately say:

> "This is running now — it's reading the ticket, reading the existing code, planning the change. Four files are going to change. Let me show you what it looks like when it finishes."

**Switch to browser. Show the fix already working** (it's already implemented on this branch):
- Click "Demo: Show Fix" if not already done
- HTTP Trace shows 200 OK, same ID, PROTECTED
- Impact card is green

> "This is the result. Same request sent twice — one charge created. cust_A1B2 is correctly billed $99. The governance hook is about to fire in the terminal when Claude finishes — watch."

**When Claude finishes** (or after 90 seconds, flip back):
- The governance hook output will be in the terminal
- *"There it is. Tests ran automatically. 9 passing. That's your control mechanism."*

---

## ⏸ PAUSE 1 — after security audit (0:21)

Stop. Look up from the screen. Say:

> "That's what came back in 45 seconds. What's your reaction?"

**If CTO says "we'd have to fix those":** *"Yes. And Claude Code can fix all five. Each fix requires your review before anything commits. Want me to show you that?"*

**If CTO says "we don't have those issues":** *"You may not — this is a demo repo. But in my experience, every codebase we've scanned in financial services has at least one of these. The hardcoded secret one is the most common. Would it be worth running this on a real service as part of the pilot?"*

**If CTO stays quiet:** Write something down visibly. Say: *"I'm going to note that — I want to come back to it."* Continue.

---

## ⏸ PAUSE 2 — after fix demonstrated (0:27:30)

Stop. Look up. Say:

> "Both customers are now correctly charged. The P1 is closed. Questions before I show you the governance layer?"

**If Head of DT asks "how long did that take?":** *"Four minutes of Claude Code session. The ticket had been open three days."*

**If CTO asks "how do we know it didn't break anything?":** *"The governance hook — we'll look at it in 60 seconds. Every change is validated against your test suite automatically before it proceeds."*

**If both are quiet:** *"Let me show you the one file that makes this repeatable across all 180 of your engineers."* → CLAUDE.md.

---

## 🌉 CLOSE BRIDGE — DEMO_TODO → next steps (0:32)

Open DEMO_TODO.md on screen. Let them read it for 5 seconds. Then:

> "This is what the session produced — automatically. Security findings, bug fixed, tests written, code reviewed, deployment config generated."

Point to the **unchecked items** at the bottom:
```
- [ ] Schedule Pilot Week 1 kickoff with 5-engineer cohort
- [ ] Set up metrics baseline (PR cycle time, incidents per sprint)
- [ ] 6-week readout scheduled with Head of DT
```

> "These three items don't require a procurement decision. They're a calendar invite and an agreement to measure. That's all I'm asking for today."

**Pause.** Let it land.

> "Who on your side would own the pilot kickoff?"

---

## 👥 MANAGING TWO PERSONAS IN THE SAME BREATH

When both CTO and Head of DT are watching, use these frames:

**After security audit:**
> "For [CTO] — this is your control evidence for the FFIEC exam. For [Head of DT] — this is what your engineers catch before it becomes an incident report."

**After governance hook fires:**
> "For [CTO] — every change is tested automatically, no human required. For [Head of DT] — your engineers don't lose time running CI manually. Both things at once."

**On CLAUDE.md:**
> "For [CTO] — your policies, enforced in code, not in a document no one reads. For [Head of DT] — new engineers are inside your standards on day one. No ramp-up required."

**In the close:**
> "The pilot I'm proposing gives [CTO] the compliance evidence you'd need before a broader rollout, and gives [Head of DT] the usage data you'd take to the board. One pilot, both answers."

---

## 5 DISCOVERY QUESTIONS (0:02–0:07)

Ask in this order. Listen. Write things down visibly.

1. **"What does your code review process look like — where does it slow down?"**
   - If: *bottlenecks on senior engineers* → *"That's exactly where the leverage is. Your senior engineers stop being reviewers and start being multipliers."*
   - If: *"it works fine"* → *"That's good to hear. What about when a senior engineer is pulled into incident response — what happens to the review queue?"*

2. **"In a production incident, what's harder — finding the issue or fixing it?"**
   - Most say finding it → set up your SRE beat

3. **"Are any engineers already using AI tools, even unofficially?"**
   - If yes → *"That tells me appetite is there. The question is how to give them something that doesn't keep your security team up at night."*
   - If no → *"That's interesting. Is that a cultural thing or a policy thing?"*

4. **"From a security perspective, what's your biggest concern about a tool like this?"** ← CTO owns this answer. Stay quiet. Write it down.

5. **"What does success look like in 90 days?"**
   - Whatever they say becomes your close metric.

**Reflect back:** *"What I'm hearing is [their security concern] and [their velocity concern]. Let me show you something specifically designed for that."*

---

## 4 PROMPTS — type slowly, don't paste

**Prompt 1 — Beat 0, codebase walkthrough:**
```
I just joined the FinTechCo payments team. Walk me through
this codebase — the payment flow end to end, how the processor
integration works, and anything I should know before touching
production code.
```

**Prompt 3 — Beat 2, fix the bug:**
```
I've been assigned ISSUE.md. Implement the fix described,
write tests proving duplicate charges no longer happen, and
make sure all existing tests still pass.
```

**Prompt 2 — Security audit (if not using UI button):**
```
Audit this codebase for security vulnerabilities. This is a
PCI-DSS and FFIEC regulated financial services application.
```

**Code review — Beat 3:**
```
/code-review:code-review
```

---

## TOP 5 OBJECTIONS — mid-demo versions

| Objection | Response |
|-----------|----------|
| "Our code can't leave our environment" | "It doesn't. Only the session prompt goes over the wire. Nothing is persisted. I can get you the architecture diagram and data processing agreement today." |
| "Are you training on our code?" | "Contractually prohibited — not policy, it's in the agreement. I'll send you the specific clause." |
| "What if it makes a wrong change?" | *Point to governance hook output* "Every edit is shown before it applies. This hook validates it. Nothing silent, nothing irreversible." |
| "We already have Copilot" | "Copilot makes writing faster. This makes understanding and changing existing systems faster. For your SREs at 2am — that's the difference." |
| "My engineers won't adopt it" | "The skeptics become the heaviest users by week 4. The pitch isn't 'use AI instead of thinking' — it's 'stop spending 3 hours understanding a service before you can start the task you were hired for.'" |
| "We need to go through procurement" | "Understood — we have an enterprise agreement template designed for FFIEC environments that's moved quickly at similar firms. Tell me who owns vendor security assessments and I'll get them what they need this week." |

---

## CLOSE (0:39)

Point to DEMO_TODO.md unchecked items on screen.

> "These three items are all I'm asking for.
> **This week:** I send you the security overview and data processing agreement for your legal team.
> **Next week:** 30-minute setup call — your pilot engineers are running before we hang up.
> **Week 6:** Pilot readout. Data. Decision.
>
> **Who on your side would own the pilot setup?**"

*Get a name. Get a date. End the call. Do not add more content after the ask.*

---

## IF THINGS GO WRONG

| Problem | What to do |
|---------|----------|
| Claude Code slow / no output | Switch to browser, show fix already working, circle back when done |
| Server not running | `pkill -f uvicorn && cd ~/fintech-demo && python3 -m uvicorn app.main:app --port 8000` |
| /code-review not working | `git diff main...feat/duplicate-charge-fix` — *"This is the diff the review covers"* |
| Tests fail during hook | *"This is exactly what the hook is for — it caught it before production"* |
| Wrong branch | `git checkout feat/duplicate-charge-fix` |
| Discovery runs long (10+ min) | Cut CLAUDE.md walk-through — go straight from governance hook to DEMO_TODO close bridge |
| Running short at 0:35 | Ask: *"What questions haven't I answered?"* — executives always have one |
