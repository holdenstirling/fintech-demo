# Applied AI Architect — Interview Prep
## Anthropic Virtual Onsite · FinTechCo Mock Presentation

---

## The Interview Format

**50 minutes total:**
- 0:00–0:05 — Real introductions (not role play yet)
- 0:05–0:45 — Mock presentation (40 minutes, full role play)
- 0:45–0:50 — Your questions about Anthropic

**The 40-minute presentation must cover (from the brief):**
1. **Slides** — UVP, competitive differentiators, team-specific value, metrics/ROI framework, evaluation plan with specific use cases
2. **Live demo** — technical demonstration connected to FinTechCo's actual use cases
3. **Wrap-up** — clear next steps, don't run long

**What they're specifically evaluating:**
| What they're watching | What "great" looks like |
|---|---|
| Discovery instinct | You ask before you pitch. You surface the CTO's real fear before slide 3. |
| Executive range | You land the same message with a skeptical CTO and an eager Head of DT — at the same time. |
| Demo confidence | You narrate value while the screen shows work. You don't narrate the screen. |
| Enterprise pattern recognition | Financial services sells to Legal, Security, and Compliance before Engineering. |
| Handling objections live | Data residency question from the CTO doesn't rattle you. You were waiting for it. |
| Clear next steps | You leave with a name, a date, and an action — not "let's stay in touch." |
| Claude Code depth | "How is this different from Copilot?" — you answer without a slide and without hedging. |

---

## Know FinTechCo Cold

**Company:**
- Digital payment services + traditional banking divisions
- Infrastructure: AWS and GCP, US customers
- Priorities: team productivity + shipping new products
- Budget posture: **cost-conscious but not cost-driven** — frame ROI as productivity and quality, not just headcount savings
- Goal: **single agentic coding tool company-wide within the next few months** — this creates urgency and means they want a decision framework, not a pilot that drags on

**The three teams:**
| Team | Size | Focus | Stack | Their pain |
|---|---|---|---|---|
| Software Engineers | 120 | Digital payments, mobile, banking infra | Python, TypeScript, Java | Onboarding to unfamiliar services, PR review bottlenecks, debugging distributed systems |
| Data Scientists | 40 | Fraud detection, credit scoring, customer behavior ML | Python, Jupyter, pandas, scikit-learn, TensorFlow | Blocked on boilerplate and frontend glue work; great at models, slow on everything around them |
| SREs | 20 | Incident response, reliability | Python, shell, Go | Cold incident triage at 2am in systems they didn't write; MTTR is their KPI |

**The two personas in the room:**
- **CTO** — 20+ years fintech. Technical depth, highly skeptical, PCI-DSS and FFIEC are not abstractions to him. His real question isn't "does it work" — it's *"who is responsible when something goes wrong, and how do I know before I need to answer that question."*
- **Head of Digital Transformation** — your champion. Has been fighting for tools like this. His real question isn't "is it safe" — it's *"what metric do I put in the board deck, and will engineers actually adopt it."*

**How to read the room:** If the CTO is asking security questions, slow down and give depth. If the Head of DT is leaning forward, give him a number he can repeat. Never sacrifice one for the other — the CTO sinks the deal, the Head of DT makes it happen.

---

## Competitive Differentiators — Know These Cold

They are evaluating Claude Code **alongside other AI coding assistants**. This will come up.

### vs. GitHub Copilot
| Copilot | Claude Code |
|---|---|
| Autocomplete in your IDE | Multi-step agentic tasks in your terminal |
| Suggests the next line | Reads a Jira ticket, edits 7 files, writes tests, runs them |
| File-scoped | Entire codebase, git history, dependencies |
| Can't run tests | Runs tests, sees failures, fixes them in the same session |
| No governance layer | CLAUDE.md + hooks enforce your team's rules on every change |
| IDE plugin = shadow IT risk | Terminal-based, works with your existing audit trail |

**Say:** "Copilot makes writing code faster. Claude Code makes *shipping* faster — that's a different category."

### vs. Cursor / Windsurf
| Cursor | Claude Code |
|---|---|
| IDE-based | Terminal-based (works with any IDE, including none) |
| Good at single-file tasks | Multi-file, multi-service, full repo awareness |
| No enterprise governance | CLAUDE.md + hooks, SOC 2 Type II |
| No headless/CI mode | Runs non-interactively in pipelines (`claude -p`) |

### vs. ChatGPT / Copilot Chat
| Chat tools | Claude Code |
|---|---|
| You paste code, you get a suggestion, you implement it | Claude reads your actual repo and implements directly |
| Context window = what you paste | Context = your entire codebase, git history, docs |
| No connection to your actual system | Reads files, runs tests, makes commits, opens PRs |

**The three-word differentiator:** *Agentic. Governed. Enterprise-ready.*

### What makes Claude Code unique for FinTechCo specifically:
1. **Governance layer** (CLAUDE.md + hooks) — this is what makes it safe for a regulated environment. No other tool has this.
2. **No training on code** — contractual, not a setting. Critical for PCI-DSS data.
3. **Headless mode** — runs in CI pipelines without a human. SREs and platform teams love this.
4. **Plan Mode** — shows the plan before writing a line. Human reviews, approves, then it runs. Built-in control.
5. **Works for all three teams** — SWE, Data Scientist, and SRE workflows, not just IDE users.

---

## Slides — What to Update

You have `FinTechCo_Claude_Code_Demo_v4.pptx` as a starting point.

**Must change:**
- [ ] Replace all "Solutions Engineering" → "Applied AI"
- [ ] Add FinTechCo-specific team breakdown (120 SWEs / 40 Data Scientists / 20 SREs) with their specific pain
- [ ] Add security/compliance slide — specifically PCI-DSS and FFIEC, not generic "enterprise security"
- [ ] Add competitive differentiation slide — Claude Code vs. Copilot vs. Cursor, one slide, sharp
- [ ] Add metrics/ROI framework slide with leading + lagging indicators
- [ ] Add evaluation plan slide — 3 phases, specific use cases per team, timeline that fits their "next few months" goal

**Strong to add:**
- [ ] CLAUDE.md slide — shows one file governing 180 engineers
- [ ] Governance hook diagram — automated compliance enforcement
- [ ] "What success looks like at 12 weeks" slide with specific metrics

**Slide order:**
1. Agenda (set expectations, signals you're organized)
2. What is Claude Code — 30-second version, one sentence that lands
3. The three teams at FinTechCo — personalize before they ask
4. Why not Copilot/Cursor — address the competitive question proactively
5. Security + compliance architecture — CTO slide, slow down here
6. Live demo transition
7. ROI framework — leading + lagging indicators
8. Evaluation plan — 3 phases, specific use cases, timeline
9. Next steps

---

## The Narrative Arc — One Version Per Persona

**One sentence for the room:**
> "FinTechCo has 180 engineers across three very different teams. Claude Code lets all of them move faster — without your security team losing sleep."

**CTO arc:**
1. *Skeptical* → You demonstrate you understand their regulatory world before they have to explain it
2. *Concerned about control* → CLAUDE.md + governance hooks — you control what it can do, in plain English, committed to the repo
3. *Concerned about data* → Code stays local, no training, SOC 2, DPA available
4. *Wants to see it fail safely* → Plan Mode shows the plan before changes; hook validates every change; nothing ships without engineer approval
5. *Needs an exit ramp* → "It's a CLI. Uninstall is one command."

**Head of DT arc:**
1. *Excited* → Validate their instinct, but redirect to metrics: "You're right, and here's how we'll prove it."
2. *Needs a number* → Give him leading indicators he can track in week 1, lagging indicators for the board in month 3
3. *Worried about adoption* → "The engineers who are most skeptical in week one are usually the heaviest users by week four."
4. *Needs a rollout story* → 5-person pilot → measure → expand → enterprise. Clean, low-risk, reversible.

---

## Discovery Questions — Ask These, In This Order

Before slides. Before demo. Before anything.

> "Before I show you anything, can I ask a few questions? I want to make sure what I show you is specifically useful for your situation."

1. **"What does your current code review process look like — and where does it slow down?"**
   - Listen for: PR bottleneck (senior engineer bandwidth), stale PRs, context-switching tax

2. **"When your SREs are on-call at 2am in a system they didn't write — what's the hardest part?"**
   - Listen for: unfamiliar codebase, poor docs, time pressure. This is your SRE demo setup.
   - *If they say "finding the issue":* lean into the SRE incident demo. That's your money beat for them.

3. **"Have any of your engineers started using AI tools on their own — even unofficially?"**
   - *If yes:* "That tells me the appetite is already there. The question is how to channel it in a way that your security team is comfortable with — because shadow AI is a bigger risk than governed AI."
   - *If no:* "That's useful context. It means governance is probably more important than adoption in your evaluation."

4. **"From a security standpoint, what's your biggest concern about a tool like this touching production code?"**
   - Let the CTO answer. Write it down. Do not jump in.
   - Whatever he says: write it on a notepad, visible to them. You'll address it directly before the demo ends.

5. **"What does success look like for this evaluation in 90 days?"**
   - This becomes the metric you close on. Reference it in your wrap-up.

**After all five, reflect back before moving to slides:**
> "What I'm hearing is [X], [Y], and [Z]. That's exactly the use case I want to show you. Let me do 8 minutes of context and then we'll get into the terminal."

---

## Slides Narration — Key Lines Per Slide

**What is Claude Code:**
> "Claude Code is an agentic coding assistant that runs in your terminal. Not autocomplete — not a chat window. It reads your actual codebase, understands your file structure, git history, and dependencies, and takes multi-step actions to help engineers ship faster. The distinction that matters for FinTechCo is that it doesn't just suggest — it acts. And every action is visible, reversible, and governed."

**The three teams:**
> "You have three very different engineering populations and I want to talk about each one specifically, because the value story is different for each."
- **SWEs (120):** "The tax isn't on writing code. It's on understanding code you didn't write. Onboarding, debugging a distributed system you've never seen, prepping a PR at the end of a long sprint."
- **Data Scientists (40):** "Your data scientists are blocked on everything around the model — the API integration, the data pipeline, the dashboard to show results. Claude Code doesn't replace their domain expertise; it eliminates the boilerplate tax so they can spend their time on the part only they can do."
- **SREs (20):** "2am. Alert fires. Unfamiliar service. The time between 'something is wrong' and 'I know where to look' — that's your MTTR. That's where Claude Code has the most direct ROI signal for your team."

**Why not Copilot:**
> "You're probably evaluating other tools. Let me be direct about what's different. Copilot makes writing code faster — it's excellent autocomplete. Claude Code is different in kind. It takes multi-step actions across your entire repo, reasons about systems not just files, and can do things like read a P1 ticket, understand seven files across three services, implement a fix, write tests, and validate the result — without switching tools. For single-file work, Copilot is great. For the kind of complex distributed systems work that defines FinTechCo's engineering — this is a different category."

**Security architecture (slow down, eye contact with CTO):**
> "Let me spend a minute on this because I know it's not optional for you. In financial services, a tool that touches production code needs to earn trust before it gets access."
- Code runs in your terminal — only the prompt context goes to the API, nothing is persisted
- No training on customer data — this is contractual, not a setting that can change
- You control what Claude can do via CLAUDE.md — plain English rules committed to your repo
- PostToolUse governance hooks run your test suite on every code change, automatically, for every engineer
- SOC 2 Type II certified, DPA available, enterprise agreement designed for regulated industries
- Plan Mode requires human approval before any code changes — this is the built-in control mechanism

> "The thing I'm about to show you in the demo isn't a sandboxed environment. It's your stack — a payments API with real security issues. Let me switch to the terminal."

---

## Implementation Complexity — Have Answers Ready

The brief says they want to understand "implementation complexity and timelines." Be ready.

**Installation:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```
> "That's it. 30 seconds. No IT ticket, no VM provisioning, no license server, no configuration. A developer at FinTechCo installs this before the morning standup and is using it by lunch."

**Governance setup:**
- CLAUDE.md: plain English file, committed to the repo, any engineer can read and edit it
- Hooks: one JSON file (`.claude/settings.json`), already written, committed to the repo
- Rollout: distribute via your existing repo template — every new repo inherits the governance layer

**Rollback:**
> "It's a CLI. Uninstall is one command: `rm -rf ~/.local/bin/claude`. Nothing is stored server-side. Your codebase is unchanged."

**IT/Security involvement:**
- Network: outbound HTTPS only, no inbound ports
- Data: no persistent storage on Anthropic's side post-session
- Provisioning: per-developer API key, manageable via enterprise agreement
- Audit trail: every action logged locally, git history unchanged

**Timeline to value:**
| Milestone | Time |
|---|---|
| First engineer productive | Day 1 |
| Pilot team onboarded | Week 1 |
| Pilot data ready for review | Week 3 |
| Expanded cohort measuring delta | Week 6 |
| Company-wide decision | Week 12 |

> "You said you want to make a company-wide decision within the next few months. Our typical pilot-to-enterprise path is 12 weeks. That's exactly the timeline you need, and it's designed to give you real data before you commit."

---

## ROI Framework — Metrics, Leading and Lagging

The brief says they are "particularly concerned about how to measure business impact." Give them a framework, not just numbers.

### How to set baselines (do this in pilot week 1)
- PR cycle time: average of last 30 PRs per pilot engineer (open → merge)
- Incident MTTR: last 10 P1/P2 incidents (alert → resolved)
- Onboarding time: time from start date to first meaningful commit (ask the last 3 new hires)
- Security findings per sprint: count from your last internal security review

### Leading indicators (track weekly, weeks 1–4)
These move fast and show adoption is working:
- Number of AI-assisted PRs (ask engineers to tag them)
- PR cycle time delta vs. baseline
- Test coverage change per sprint
- Subjective: "Would you use this tomorrow?" (1-5, weekly pulse)

### Lagging indicators (track monthly, months 1–3)
These take longer but are what the board wants:
- Features shipped per sprint vs. baseline period
- Incident MTTR vs. baseline
- Security findings per audit (pre vs. post Claude Code)
- Onboarding time for new hires
- Engineer satisfaction / internal NPS

### The numbers — have these ready, use theirs first
Ask their baselines first. Then reference:

| Metric | Typical baseline | With Claude Code | Delta |
|---|---|---|---|
| PR cycle time | 4–6 hours | 2–3 hours | ~50% reduction |
| New hire → first meaningful commit | 5–10 days | 2–3 days | ~60% faster |
| P1 incident diagnosis | 30–60 min | 10–20 min | ~60% faster |
| Security findings per quarterly audit | 8–15 | 2–4 | ~70% fewer (rest caught pre-commit) |
| Data scientist boilerplate hours per sprint | 30–50% of their time | 10–20% | ~30 hours/sprint recovered |

### The financial frame (for Head of DT to take to the board)
> "If your 120 SWEs recover 2 hours per week each — that's 240 engineer-hours per week. At a blended rate of $150/hour loaded cost, that's $36,000 per week in recovered capacity. That's not headcount reduction — that's shipping the next product faster. The ROI math works whether you frame it as efficiency or as competitive velocity."

---

## Data Scientist Use Case — Know This Section Cold

40 engineers, and the brief specifically calls them out. You're not demoing this directly — address it verbally.

**Their specific pain:**
- Experts in the model; blocked on everything else
- API integration, data pipeline setup, frontend dashboards — these take days to weeks
- Notebook-to-production is a whole separate skillset most DSs don't have

**Claude Code's value for them:**
- Write the FastAPI wrapper around their model in minutes, not days
- Set up the data pipeline (pandas → database → API) from a description
- Turn a Jupyter analysis into a shareable dashboard
- Debug TensorFlow/scikit-learn environment issues without Stack Overflow

**The example you can give:**
> "One of the example use cases in the brief is FRED data — Federal Reserve economic data for inflation and unemployment analysis. A data scientist at FinTechCo could tell Claude Code 'pull FRED data on unemployment and inflation for the last 10 years, build a Flask app showing the Phillips Curve, and explain any statistical anomalies.' That's a week of boilerplate work in 10 minutes. The data scientist's time goes to the part only they can do — the insight."

**Why this matters for the Head of DT:**
> "Your 40 data scientists are probably your highest-leverage people and your most bottlenecked. Claude Code doesn't replace their expertise — it removes the 40% of their time that has nothing to do with it."

---

## The Evaluation Plan — Specific Use Cases Per Team

Not a generic "5-person pilot." Specific names, specific workflows.

**Pilot composition: 5 engineers, 3 weeks**

| Engineer | Team | Specific starting use case | What they measure |
|---|---|---|---|
| Engineer 1 | SWE (payments) | Onboard to a service they've never worked in; estimate first week savings | Time to first PR with context questions answered by Claude |
| Engineer 2 | SWE (payments) | Take a real bug ticket end-to-end: ticket → fix → tests → PR | Total time vs. recent comparable tickets |
| Engineer 3 | SRE | Simulate a cold incident triage: given an unfamiliar service + alert, how long to find root cause | MTTR delta vs. last 5 incidents |
| Engineer 4 | Data Scientist | Remove one week of boilerplate work: build a data pipeline + API for a model they've already trained | Hours saved, self-reported |
| Engineer 5 | Wildcard (any team) | Highest-friction workflow that team has right now | Before/after time, qualitative |

**Phase timeline:**
| Phase | Duration | Goal |
|---|---|---|
| Pilot | Weeks 1–3 | Measure leading indicators, validate adoption |
| Expand | Weeks 4–6 | 10-person cohort, start measuring lagging indicators |
| Decision | Week 8 | Data review: proceed to enterprise or not |
| Enterprise rollout | Weeks 9–12 | All 180 engineers, CLAUDE.md distributed via repo template |

> "This is designed specifically to fit your 'next few months' timeline. Week 12 is your company-wide go/no-go. That's the decision you said you need."

---

## Objections — The Big Five

**"Our code can't leave our environment."**
> "It doesn't. Claude Code runs in your terminal. Only the prompt context is sent to the API — and nothing is persisted on Anthropic's side after the session ends. We also support private deployment for air-gapped environments. Which compliance framework are you operating under specifically? I want to make sure I give you the right documentation."

**"How do we know Anthropic isn't training on our code?"**
> "It's in the contract, not a settings toggle. Our enterprise DPA explicitly prohibits using customer API inputs for model training. I can get you the specific clause. This is what separates an enterprise agreement from a consumer product."

**"What happens when it makes a wrong change?"**
> "Two things prevent this. First, Plan Mode — before Claude writes a single line, it presents the plan. You review it, change the scope, ask questions. Nothing happens until you approve. Second, the governance hook runs your test suite on every code change, automatically. If something breaks, Claude sees the failure and fixes it in the same session. The blast radius is always visible and reversible before anything reaches version control."

**"We'd need to go through procurement."**
> "Expected, and we're ready for it. We have an enterprise agreement template that has been through legal review at comparable financial services firms — it covers data processing, security, IP ownership, and compliance documentation. Who owns vendor security assessments on your side? I can have the right documents to them this week."

**"How is this different from GitHub Copilot?"**
> "Copilot is excellent autocomplete — it makes writing code faster. Claude Code is different in kind. It takes multi-step actions across your entire repo. The thing you just watched — reading a ticket, understanding seven files, implementing a fix, writing tests, running them, and proving the result — Copilot can't do that. For single-file suggestions, Copilot is great. For the work your senior engineers do on complex distributed payment systems at 2am — this is a different category of tool."

---

## The Close — Exact Language

> "Here's what I'd propose as next steps. I want to be concrete."

1. **This week:** I send you the enterprise security overview, SOC 2 report, and DPA for your legal and security team to review in parallel with the pilot
2. **Next week:** 30-minute setup call with whoever you designate as pilot lead — I will have all five engineers running before that call ends
3. **Week 3:** Mid-pilot check-in — I want to hear what's working and what isn't before we expand
4. **Week 8:** Data review — we look at the metrics together and make the expansion decision with real numbers, not impressions
5. **Week 12:** Company-wide go/no-go — that's the timeline you said you need

> "My job through this evaluation is to make sure you have everything you need to make a good decision. If the pilot data doesn't support a broader rollout, I will tell you that."

**Then, hard close:**
> "Who's the right person on your team to own the pilot setup — and can we get 30 minutes on the calendar before end of next week?"

Get a name. Get a date. The meeting is not over until you have both.

---

## Questions to Ask Anthropic at the End

Have 3 ready. These signal you're thinking like someone who's already in the role:

1. "How do Applied AI Architects typically structure the pilot-to-enterprise handoff — is there a standard playbook, or is it customized per account?"
2. "What's the most common reason a well-run pilot doesn't convert to enterprise? What patterns have you seen in financial services specifically?"
3. "How are you thinking about the Data Scientist use case relative to the Software Engineer use case — in demos with mixed engineering teams, which tends to have more pull?"

---

## Pre-Interview Checklist

**72 hours before:**
- [ ] Update slides — replace "Solutions Engineering" → "Applied AI", add competitive slide, FinTechCo team breakdown, security/compliance slide with PCI-DSS + FFIEC language, ROI framework with leading/lagging indicators, evaluation plan with specific use cases, 12-week timeline
- [ ] Practice all 5 discovery questions out loud with varied responses
- [ ] Practice all 5 objection scripts out loud until they're fluent, not recited
- [ ] Run the full demo twice, timed — target 13 minutes for the terminal portion
- [ ] Practice the competitive differentiator section without slides

**Night before:**
- [ ] Clean server test: `cd ~/fintech-demo && rm -f payments.db && python3 -m uvicorn app.main:app --reload --port 8000`
- [ ] Run all 6 prompts end to end — confirm dashboard updates on prompt 4a and 4c
- [ ] Test screen share on Google Meet — confirm terminal AND browser are both visible and readable
- [ ] Have `DEMO_CHEATSHEET.md` open in a dedicated window
- [ ] Charge laptop, close unnecessary apps, silence phone, close Slack notifications

**30 minutes before:**
- [ ] `cd ~/fintech-demo && git checkout main && rm -f payments.db`
- [ ] `python3 -m uvicorn app.main:app --reload --port 8000` in Terminal 1
- [ ] `claude` in Terminal 2
- [ ] Browser: `http://localhost:8000` — dashboard loads with seeded data
- [ ] Slides open in presenter mode (with notes visible)
- [ ] `DEMO_CHEATSHEET.md` open in a third window
- [ ] Screen share tested — both terminal and browser visible to audience
- [ ] Water nearby
