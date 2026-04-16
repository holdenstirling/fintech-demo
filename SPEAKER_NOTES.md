# Speaker Notes · FinTechCo Final-Round Demo

_22 slides · 40 minutes total · ~90 seconds per slide average, with the demo holding the biggest budget_

**Pacing guardrails**
- Slides 1–7: 8 minutes (setup)
- Slides 8 architecture: 2 minutes (security team's favorite)
- Slide 9 demo opener + demo itself: 12 minutes
- Slides 10 recap → 13 next steps: 10 minutes
- Appendix (14–22): only if asked — treat as a Q&A reservoir, not a monologue

---

## Slide 1 · Cover

**Entry:** "Thanks for having me. Before I open anything, I want to say I'm genuinely excited to walk through this with you."

**Body (30s):** "What I want to do today is keep this conversational. I'll share what I think I'm hearing, ask you five questions, and then show you Claude Code on a real codebase. The goal isn't to convince you of anything in the next forty minutes; it's to help you decide whether a two-week pilot makes sense."

**Exit:** "So, with that, let me share my screen."

---

## Slide 2 · Agenda

**Entry:** "Here's the shape of our time together."

**Body (45s):** Walk the five blocks at a steady pace. Don't read the descriptions verbatim — summarize. Point out that block 4 (the demo) is the biggest piece of real estate, and block 3 (discovery) is short but important because it shapes the demo. Acknowledge timing: "If we run long, the appendix has the six most common follow-up questions — we'll go there together if we have time or offline if we don't."

**Exit:** "Any objections to this flow before I start?" _Pause — let them respond._

---

## Slide 3 · What is Claude Code

**Entry:** "Before the demo, a plain-English definition. Because you have non-technical folks in the room and I want everyone on the same footing."

**Body (60s):** "Claude Code is a coding agent. Three things matter. One: it reads the whole codebase, not just the file you're in. Two: it plans before it acts — you see what it's going to do before it does anything. Three: it checks its own work by running your tests. The reason I describe it as 'a senior engineer' is because those are the habits a senior engineer has. It's less like using a tool, more like pairing."

**Exit:** "That's the what. Now let me check I understand the why."

---

## Slide 4 · What I'm hearing

**Entry:** "Before I share anything, let me play back what I think I'm hearing. Correct me where I'm wrong. This is the most valuable thirty seconds of the call."

**Body (60s):** Walk the four items briefly. _Pause_ after each one to invite a nod or a correction. "A regulated environment — PCI-DSS and FFIEC. Three very different teams — engineers, SREs, data scientists. An active P1 that shouldn't have happened. And pressure to go faster without loosening the controls."

**Exit:** "Anywhere I've got that wrong? Or anything missing?" _Wait. Take notes on what they add._

**Critical move:** if they correct you, _thank them and show you wrote it down_. That's what separates SA candidates who pass from ones who don't.

---

## Slide 5 · Discovery

**Entry:** "Five questions. I'll listen more than I talk."

**Body (6–7 min total):** Walk Q1 through Q5. Rules:
- Don't interrupt. Let silence sit.
- For every answer, repeat back one sentence: "So what I'm hearing is X."
- If Q3 (are engineers already using AI unofficially) gets a "no" — don't challenge it. If it's a "yes," ask which tools and what's working.
- End with: "Before we move on, let me play back the five things I took away from that."

**Exit:** "All that said, let me show you Claude Code on a real codebase — one that looks a lot like yours."

---

## Slide 6 · Three teams

**Entry:** "Quick orientation. Three teams inside FinTechCo. Three different bottlenecks. One tool that addresses each of them for different reasons."

**Body (90s):** For each column, speak the TODAY → WITH CLAUDE CODE delta. The SRE column is your strongest story ("45 minutes to 15 minutes to find the issue at 2am"). Linger there longest. The data scientist column is often the surprise — "these folks are your ML hires and you don't want them writing boilerplate pipelines."

**Exit:** "So: different flavors of value for different teams. Which brings us to how it behaves in a regulated environment."

---

## Slide 7 · Safety, security, governance

**Entry:** "This is the slide your security team will ask about. Four pillars."

**Body (60s):** Walk the four quadrants. Don't just read them — reframe each as a risk the CTO has likely worried about:
- "Code stays on machine" → "We're not a SaaS that pulls your repo."
- "Nothing ships without approval" → "No silent auto-commit. Ever."
- "Your rules automatically" → "CLAUDE.md is policy as code."
- "Clean audit trail" → "Your auditors see an engineer's name on every commit."

**Exit:** "And because your security lead will want to see this flow visually, let me show you one picture."

---

## Slide 8 · Architecture at a glance

**Entry:** "This is the whole picture on one slide. If your security team only reads one thing, it should be this."

**Body (90s):** Walk the flow left to right. "Laptop — local. CLAUDE.md — your policy file, version controlled. CLI — reads and plans. Safety Gate — human approval. Tests — governance hook. Commit — attributed to the engineer." Then point to the black box: "The one network call is to api.anthropic.com, over HTTPS, and that traffic is covered by our contractual no-training clause." Finish on the four guarantees at the bottom.

**Exit:** "OK — enough slides. Let me show you this in action."

---

## Slide 9 · Live demo opener

**Entry:** "We're going to spend the next twelve minutes on a real codebase. It's a payments service, intentionally similar to what you run. Three scenarios: a new engineer getting up to speed, an SRE in the middle of a P1, and a data scientist who's blocked on boilerplate. Watch for the Safety Gate — I'll point it out when it shows up."

**Demo structure (from DEMO_PLAYBOOK):**
- Beat 1 (3 min): Codebase onboarding
- Beat 2 (5 min): P1 incident — the double-charge bug
- Beat 3 (3 min): Data-scientist pipeline
- Beat 4 (1 min): Review plugin / CLAUDE.md showcase

**Key narration moments:**
- When Safety Gate appears: "Watch this — this is the moment that matters."
- When tests run green: "That's the governance hook."
- When you accept a change: "Notice my name on the commit, not Claude's."

---

## Slide 10 · What you just saw

**Entry:** "Twelve minutes. Four things your engineers would actually notice on Monday morning."

**Body (60s):** Walk the four recap cards briefly. Don't repeat the demo — compress it to one-sentence takeaways each.

**Exit:** "Now the question on everyone's mind: does this actually pay for itself? Let's do the math."

---

## Slide 11 · ROI framework

**Entry:** "A framework, not a promise. We'll use your numbers, not mine."

**Body (90s):** Walk the framework line by line, then land the math callout: "$1,500 in saved engineer-time per engineer per month, against $100 in software cost. That's a 15× ratio, and it assumes conservative adoption." Make eye contact with the CFO-equivalent in the room.

**Exit:** "That's the 'why.' Here's the 'how we get there.'"

---

## Slide 12 · Rollout plan

**Entry:** "Three weeks to a signal. Three months to a decision."

**Body (60s):** Walk phase 1 → 2 → 3. Key phrasing: "Phase 1 is twelve engineers, not one hundred and eighty, because I'd rather learn something small than oversell something big." Land on phase 3: "You decide, based on real data from your team, not my benchmarks."

**Exit:** "And that leads into what I'd like to agree on before we end."

---

## Slide 13 · Next steps

**Entry:** "Three asks. None of them need procurement today."

**Body (60s):** Walk the three rows. Emphasize "in parallel, not in sequence" — that's the compression story. Land on the closing quote: "Who on your side would feel best owning the pilot setup?"

**Exit:** Wait for an answer. If they name someone, say: "Great. I'll make sure they're copied on everything I send. Anything else you need from me to make that easy?"

_This is the close. Don't rush past it. Silence is fine._

---

## Appendix (slides 14–22)

Treat these as a reservoir. Don't walk through them unless asked or unless there's genuinely time left. Each has one job.

- **14 Appendix divider** — "A few places we can go if there's time or questions."
- **15 Why Anthropic** — use if the conversation turns to vendor selection. Key line: "You're picking a partner your auditors will meet."
- **16 Competitive** — use if they mention Copilot, Cursor, Devin, or ChatGPT by name. Don't volunteer this.
- **17 Data & security** — use if legal joins late or asks for specifics. The "contractual, not just policy" line is the one they'll quote.
- **18 CLAUDE.md at scale** — use if they ask "how do you keep 180 engineers consistent?"
- **19 MCP** — use if they ask about Jira, Confluence, or internal APIs.
- **20 Honest limitations** — use _proactively_ if the room feels skeptical. It disarms. Read it as a confident statement, not an apology. Key line: "Being specific about the edges is how I earn the right to be specific about the value."
- **21 Failure modes** — use if a security engineer gets technical. This is your "we designed for, not around, failure" moment.
- **22 Closing** — if you get to it organically. Otherwise slide 13 is your natural close.
