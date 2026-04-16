# Demo Speaking Notes — Full 40-Minute Meeting
## Applied AI Architect · FinTechCo Mock Presentation

> This is your script. Not to memorize — to internalize. Read it enough times that the words feel like yours.

---

## 0:00–0:05 — INTRODUCTIONS (real, not role play)

Introduce yourself. Ask their names. Light small talk.

When they signal they're ready:

> "Great — let's jump in. I'll run this the way I'd run a real customer meeting."

---

## 0:05–0:10 — DISCOVERY

> "Before I show you anything, can I ask a few questions? I want to make sure what I show you is actually useful for your situation."

**Q1:**
> "What does your current code review process look like — and where does it slow down?"

*Listen. Write it down. Don't offer solutions yet.*

**Q2:**
> "When your SREs are on-call at 2am in a system they didn't write — what's the hardest part for them?"

*Listen. This is your setup for the SRE beat later.*

**Q3:**
> "Have any of your engineers started using AI coding tools on their own — even unofficially?"

- *If yes:* "That's actually useful context. It tells me the appetite is there. The question becomes how to do it in a way your security team is comfortable with — because shadow AI is a bigger risk than governed AI."
- *If no:* "Good to know. It means governance is probably more important than adoption speed in your evaluation."

**Q4:**
> "From a security standpoint — what's your biggest concern about a tool like this touching production code?"

*Let the CTO answer. Write it down visibly. Do not jump in. Just nod.*

**Q5:**
> "What does success look like for this evaluation in 90 days?"

*Whatever they say — write it down. You'll reference it in your close.*

**Transition:**
> "What I'm hearing is [repeat back their 2-3 key points]. That's exactly what I want to show you. Let me do 8 minutes of context and then we'll get into the terminal."

---

## 0:10–0:18 — SLIDES

---

### Slide: What is Claude Code

> "Claude Code is an agentic coding assistant that runs in your terminal. Not autocomplete — not a chat window. It reads your actual codebase, understands your file structure, git history, and dependencies, and takes multi-step actions to help engineers ship faster."

> "The distinction that matters: it doesn't just suggest — it acts. And every action is visible, reversible, and governed by rules your team controls."

---

### Slide: The Three Teams at FinTechCo

> "You have three very different engineering populations and the value story is different for each, so let me be specific."

**For the 120 Software Engineers:**
> "The tax isn't on writing code. It's on understanding code they didn't write. Onboarding to an unfamiliar service, debugging a distributed system they've never seen, prepping a PR at the end of a long sprint. That's where the time goes."

**For the 40 Data Scientists:**
> "Your data scientists are world-class at the model. They're often blocked on everything around it — the API integration, the data pipeline, the dashboard to show results. Claude Code doesn't replace their expertise. It eliminates the boilerplate so they spend their time on the part only they can do."

*(To Head of DT:)* "That's 30 to 50 percent of their week today that becomes model work."

**For the 20 SREs:**
> "2am. Alert fires. Unfamiliar service. The time between 'something is wrong' and 'I know where to look' — that is your mean time to diagnose. That's where Claude Code has the most direct ROI signal for your team."

---

### Slide: Why Not Copilot or Cursor

> "You're evaluating other tools alongside this — so let me be direct about what's different."

> "Copilot makes writing code faster. It's excellent autocomplete. Claude Code is different in kind."

> "Copilot is file-scoped — it suggests the next line in the file you have open. Claude Code reads your entire repo, reasons across services, and takes multi-step actions. The thing you're about to watch — reading a ticket, understanding seven files, implementing a fix, writing tests, validating the result — Copilot cannot do that."

> "For single-file suggestions, Copilot is great. For the kind of work your senior engineers do on complex distributed payment systems — this is a different category of tool."

---

### Slide: Security and Compliance *(slow down — CTO is listening)*

> "Before I show you the terminal, let me spend a minute on this. Because in financial services, a tool that touches production code needs to earn trust before it gets access."

*(Go through each point deliberately:)*

> "Code runs locally in your terminal. Only the prompt context goes to the API — nothing is persisted on Anthropic's side after the session ends."

> "No training on your code. This is contractual — not a settings toggle that can be changed. It's in the enterprise DPA."

> "You control what Claude can do via a file called CLAUDE.md — plain English rules committed to your repo. I'll show you this live."

> "Governance hooks run your test suite automatically every time Claude touches a production file. Not because someone remembered to run tests — because it's configured."

> "Plan Mode — before Claude writes a single line of code, it shows you the plan. You review it, you can change the scope, and then you approve. Nothing happens without that approval."

> "SOC 2 Type II certified. Enterprise DPA available. Our agreement template has been through legal review at comparable financial services firms."

*(Pause. Look at the CTO.)*

> "The thing I'm about to show you isn't a sandboxed demo environment. It's a payments API with live security issues. Let me switch to the terminal."

---

## 0:18–0:32 — LIVE DEMO

*Switch to terminal. Browser stays visible on the side.*

---

### BEAT 1: Codebase Understanding

*[Type or paste Prompt 1 into Claude Code. While it runs:]*

> "Notice I didn't give it a file path, a class name, or a module to look at. It's reading the entire project — understanding the structure, the dependencies, the integration points — on its own."

*[After response:]*

> "What normally takes a new engineer a week of meetings and Slack messages to piece together — two minutes."

*(To Head of DT:)* "Your onboarding time from start date to first meaningful PR — what is that today? That number changes."

*(To CTO:)* "And Claude didn't make up a file structure. It read the actual repo."

---

### BEAT 2: Security + Reliability Audit

*[Type or paste Prompt 2. While it runs:]*

> "We haven't pointed it at any specific file. It's doing what a security reviewer does — reading the codebase with knowledge of what financial services applications need to get right."

*[After response — point to each finding:]*

> "Finding one: three production API keys committed directly to git history. `PROCESSOR_API_KEY`, `WEBHOOK_SECRET`, `INTERNAL_API_KEY` — in `config.py`, lines 8 through 11. Every engineer who has ever cloned this repo has those credentials. That's a PCI-DSS violation and an FFIEC audit finding waiting to happen."

> "Finding two: `/api/admin/payments` — no authentication check. Anyone who knows the URL gets your full payment history."

> "Finding three: f-string SQL injection in the search endpoint. Direct path to data exfiltration."

> "Finding four — and this one is different. No idempotency key support on the payments endpoint. If a client's network times out and retries, two charges are created. That is ticket FTC-4421. Two of your customers were double-charged last week. I'm going to fix that in a few minutes."

*(To CTO:)* "Your security team would find these in a quarterly audit. Claude found all four in 45 seconds."

---

### MINI-BEAT: CLAUDE.md Governance Enforcement

*[Paste the one-liner into Claude Code. Claude refuses.]*

> "I didn't configure that refusal just now. That rule lives in CLAUDE.md, committed to this repo. Every engineer who uses Claude Code in this codebase hits the same wall. You cannot opt out of your own governance policy."

*(To CTO, say this slowly:)* "This is what control looks like in practice — not a policy document. A rule that actually runs."

---

### BEAT 3: Fix the Security Issues

*[Paste Prompt 3. Watch the terminal.]*

*(When the governance hook fires:)*

> "I didn't run those tests. The PostToolUse governance hook ran them automatically the moment Claude touched a production file. 6 tests, all passing. That is your control mechanism — it fires for every engineer, every time, whether they think to run tests or not."

---

### BEAT 4: Fix the Bug + Prove It ← THE MONEY BEAT

*[Hit Shift+Tab to enter Plan Mode. Then paste Prompt 4.]*

*(When the plan appears — pause before approving:)*

> "Nothing has changed yet. Claude is showing me what it intends to do — which files it will touch, what the schema change looks like, how it plans to prove the fix works. I can push back, change the scope, ask questions. This is Plan Mode. I review the plan first. Then I approve."

*[Approve the plan.]*

*(When Claude makes the two buggy API calls — watch the dashboard:)*

> "Two requests, two charges. Look at the dashboard — two new rows just appeared, same customer, same amount. The Duplicate Risk card just turned red. That is the live bug."

*(When Claude edits the files and the hook fires:)*

> "The hook fired automatically — 9 tests, all passing. The server just reloaded with Claude's changes. The fix is live."

*(When Claude sends two requests with the same idempotency key — watch the dashboard:)*

> "Two requests. One charge. Watch the Charges Prevented card."

*(Dashboard turns green.)*

> "One charge. The dashboard updated itself — I didn't click anything, I didn't write a test script. The server is live with Claude's fix, and it just proved it."

*(Beat. Let it land.)*

> "From ticket to implementation to passing tests to live proof — without switching tools, without a Jira comment, without a stand-up."

*(To Head of DT:)* "Think about how many tools an engineer touches between 'ticket is assigned' and 'fix is verified' in your current process. This was one."

---

### BEAT 5: SRE Incident Response

*[Paste Prompt 5. While it runs:]*

> "Twenty SREs managing payments infrastructure across AWS and GCP. This engineer has never seen this codebase. Watch what Claude does."

*[After response:]*

> "That is a triage runbook. In 60 seconds. At 2am. Without a runbook wiki, without waking up the engineer who wrote the service, without spending 30 minutes reading source code to figure out where to look."

*(To Head of DT:)* "Your mean time to diagnose — whatever it is today, this is the lever."

*(To CTO:)* "Claude didn't make up a diagnosis. It reasoned through the actual codebase — the processor integration, the database layer, the specific failure modes this architecture can produce."

---

### BEAT 6: Create CLAUDE.md

*[Paste Prompt 6. After response:]*

*(To Head of DT:)* "This is the rollout story. You write this once, commit it to your repo template, and every engineer who uses Claude Code in this codebase inherits your governance on day one. 180 engineers, one file, no training sessions."

*(To CTO:)* "The refusal we saw earlier — 'don't hardcode the API key' — came from a file exactly like this. This is your control layer."

> "Alright — let me talk about how you'd measure this and how you'd roll it out."

---

## 0:32–0:38 — ROI + METRICS

*(Before sharing numbers — ask first:)*

> "Quick question before I share some benchmarks — what's your current average PR cycle time? And your mean time to diagnose a P1 incident?"

*[Use their answers. Then:]*

> "Here's the framework I'd use for your pilot. Two types of metrics."

> "Leading indicators — these move in weeks 1 through 4 and tell you whether adoption is actually happening: PR cycle time per pilot engineer versus their own baseline, time to root cause on a simulated incident, a simple weekly pulse — 'would you use this tomorrow, one to five.'"

> "Lagging indicators — these take a month or two but are what the board needs: features shipped per sprint versus your baseline period, incident MTTR across the SRE team, security findings per audit pre versus post."

*(With their numbers:)*

> "If your PR cycle time is [their number] — we typically see a 50 percent reduction in month one. For 120 engineers, that's [calculate: their hours × 120 × 0.5 × weeks per sprint]. The frame isn't cost reduction — it's shipping velocity. That's the number for the board."

---

## 0:38–0:43 — EVALUATION PLAN

> "I'm not recommending a company-wide rollout. I'm recommending a 5-person pilot for three weeks — designed specifically around your timeline."

> "Two software engineers from your payments team. One takes a real bug ticket end-to-end — ticket to fix to PR. The other onboards to a service they've never worked in. We measure their time against recent comparable work."

> "One SRE. Cold incident triage simulation — given an unfamiliar service and an alert, how long to identify root cause. We measure MTTR delta."

> "One data scientist. The goal is simple: remove one week of boilerplate from their current sprint. Hours recovered, self-reported."

> "Setup for the pilot is 30 minutes. I will be on the call with whoever you designate. All five engineers are running before the call ends."

*(To CTO:)* "The governance layer is in place before the first engineer installs anything. CLAUDE.md is committed, hooks are configured. Every pilot user operates within your rules from day one."

*(To Head of DT:)* "You mentioned you want a company-wide decision within the next few months. Week 12 is that decision — with data, not impressions. That's the timeline."

---

## 0:43–0:45 — CLOSE

*(Hard stop — always leave 2 minutes for this no matter what.)*

> "Here's what I'd propose — concretely."

> "This week: I send you our enterprise security overview, SOC 2 report, and data processing agreement for your legal and security team to review in parallel with the pilot."

> "Next week: 30-minute setup call with whoever you designate as pilot lead. All five engineers running before the call ends."

> "Week 3: Mid-pilot check-in. I want to hear what isn't working, not just what is."

> "Week 8: Data review. We look at the metrics together and make the expansion decision with real numbers."

> "Week 12: Company-wide go/no-go. That's your timeline."

*(Pause.)*

> "My job through this evaluation is to make sure you have everything you need to make a good decision. If the pilot data doesn't support a broader rollout, I will tell you that."

*(Hard close:)*

> "Who's the right person on your team to own the pilot setup — and can we get 30 minutes on the calendar before end of next week?"

**Do not move on until you have a name and a date.**

---

## 0:45–0:50 — YOUR QUESTIONS ABOUT ANTHROPIC

Have 3 ready:

> "How do Applied AI Architects typically structure the handoff once a pilot starts — who owns pilot success, the AE or the AA?"

> "What's the most common reason a well-run pilot doesn't convert to enterprise? Are there patterns in financial services specifically?"

> "In demos with a mixed engineering team, does the SRE incident use case or the software engineer use case tend to generate more pull with the CTO?"
