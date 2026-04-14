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
| 0:32 | **[BEAT 4]** Browser — Rollout Plan card appears (visible after fix). Point to 3 phases. | Browser |
| 0:34 | Ask baselines: *"What's your PR cycle time today? MTTR on a P1?"* | Nothing |
| 0:36 | ROI framework — use their numbers | Nothing |
| 0:38 | Point to 3 unchecked items at bottom of Rollout card → **CLOSE** | Browser |
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

## 🌉 CLOSE BRIDGE — Rollout card → next steps (0:32)

Switch to browser. The **Evaluation Plan card** appeared the moment the fix was demonstrated. Point to the three-phase grid:

> "This is how 180 engineers get access to what you just watched. Phase 1 is 5 people. Three weeks. No procurement, no IT ticket. I'll be on a 30-minute setup call with whoever you designate — they're running before we hang up."

Walk through the phases:
- **Phase 1 (Week 1–3):** 2 SWEs, 1 SRE, 1 data scientist, 1 senior engineer who owns CLAUDE.md. These are the signal cohort.
- **Phase 2 (Week 4–6):** 15 engineers. CLAUDE.md distributed via repo template — no per-engineer config. Every team that adopts Claude Code inherits your governance automatically.
- **Phase 3 (Week 7–12):** All 180. Enterprise agreement, compliance documentation, FFIEC evidence in hand.

Point to the **three unchecked items** at the bottom of the card:

> "These three items are all I'm asking for today. They're calendar invites and an agreement to measure — not a procurement decision."

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

Point to the three unchecked items on the Rollout Plan card in the browser.

> "These three items are all I'm asking for.
> **This week:** I send you the security overview and data processing agreement for your legal team.
> **Next week:** 30-minute setup call — your pilot engineers are running before we hang up.
> **Week 6:** Pilot readout. Data. Decision.
>
> **Who on your side would own the pilot setup?**"

*Get a name. Get a date. End the call. Do not add more content after the ask.*

---

## ❓ HARD QUESTIONS — answers you say, nothing to show

**"Our code can't leave our environment."**
> "It doesn't. Claude Code runs in your terminal. Only the session prompt goes over the wire — the source files are read locally by the CLI and included in context. Nothing is persisted on Anthropic's side after the session ends. We also have private deployment configurations for air-gapped environments. What specific framework are you operating under? I want to make sure I give you the right documentation."

**"Are you training on our code?"**
> "Contractually prohibited. Not policy — it's in the agreement. I'll send you the specific clause today."
*Never say "I think" here. Be crisp.*

**"What stops it from making a wrong change?"**
> "Nothing applies without display. Every edit Claude makes is shown to the engineer before it's applied — no silent auto-apply. And the governance hook you saw fires automatically. If a test fails, Claude sees it and fixes the issue in the same session. Blast radius is always visible and always reversible before it hits version control."
→ *If they push back: show settings.json again. Point to the hook. "This is what actually runs."*

**"How do we audit what Claude Code did?"**
> "Every tool call is logged in the session transcript. CLAUDE.md becomes the policy of record — committed to git, versioned, auditable. And git history is unchanged. Every commit is still attributed to an engineer. Your auditors see a clean trail."

**"What does 'agentic' mean for our risk posture?"**
> "Agentic means Claude plans multi-step changes before acting. For you that means it reads the ticket, reads the affected files, reads the tests — then proposes an approach before touching anything. It surfaces blast radius before the change, not after. That's the opposite of a risk increase."

**"How does CLAUDE.md actually get to 180 engineers?"**
> "You commit it to a repo template — every new repo your team creates inherits it automatically. For existing repos, one PR. Every engineer who runs Claude Code in that repo gets your governance on day one. No per-engineer config, no training session required."
→ *Show CLAUDE.md in editor if you haven't yet. Point to it: "This is the file. Plain English. Any engineer can read it."*

**"We already have Copilot."**
> "Copilot makes writing new code faster. Claude Code makes understanding and changing existing systems faster. The SRE at 2am debugging a service they've never touched doesn't need autocomplete — they need to understand the blast radius before they touch anything. Copilot doesn't read a codebase, plan a multi-file change, and validate it against your test suite. That's a different category."

**"My engineers won't adopt it."**
> "The skeptics become the heaviest users by week 4 — consistently. The pitch isn't 'use AI instead of thinking.' It's 'stop spending 3 hours reading code before you can start the task you were hired for.' Once an engineer sees the codebase walkthrough run, they stop asking whether it works."

**"We need to go through procurement."**
> "Understood — we have an enterprise agreement template designed for FFIEC environments that's moved quickly at similar firms. Tell me who owns vendor security assessments and I'll get them what they need this week. The pilot itself doesn't require procurement — that's the point of starting there."

---

## 📊 ROI NUMBERS — have these ready, use their numbers first

Ask: *"What's your PR cycle time today? MTTR on a P1?"* Write down their answer. Then:

| Metric | Typical baseline | With Claude Code |
|---|---|---|
| PR cycle time | 4–6 hours | 2–3 hours (~50% reduction) |
| New hire → first meaningful commit | 5–10 days | 2–3 days (~60% faster) |
| P1 incident diagnosis | 30–60 min | 10–20 min (~60% faster) |
| Security findings at quarterly audit | 8–15 | 2–4 (rest caught pre-commit) |

**If they give you a number, use it:**
> "If your PR cycle time is 5 hours, we typically see a 2–2.5 hour reduction in the first month. For 120 engineers — 5 hours × 120 × 0.4 reduction × hourly rate — that's meaningful in the first sprint. I'd rather use your actual numbers in the readout."

**SRE story for FinTechCo specifically:**
> "Your 20 SREs managing payments infrastructure — the time between 'alert fires' and 'I know where to look' is measurable. If Claude Code cuts that from 45 minutes to 15, you have your number before week 3 of the pilot."

---

## IF THINGS GO WRONG

| Problem | What to do |
|---------|----------|
| Claude Code slow / no output | Switch to browser, show fix already working, circle back when done |
| Server not running | `pkill -f uvicorn && cd ~/fintech-demo && python3 -m uvicorn app.main:app --port 8000` |
| /code-review not working | `git diff main...feat/duplicate-charge-fix` — *"This is the diff the review covers"* |
| Tests fail during hook | *"This is exactly what the hook is for — it caught it before production"* |
| Wrong branch | `git checkout feat/duplicate-charge-fix` |
| Discovery runs long (10+ min) | Cut CLAUDE.md walk-through — go straight from governance hook to Rollout card |
| Running short at 0:35 | Ask: *"What questions haven't I answered?"* — executives always have one |
| Rollout card not showing | Click "Demo: Show Fix" — card appears when fixDemoed becomes true |
