# Claude Code for FinTechCo

**A coding agent built for regulated environments. Safety at the model level, governance in your repo, a human on every write.**

---

## The problem we're solving

FinTechCo runs 180 engineers under PCI-DSS and FFIEC oversight. Three things compound: new engineers take a week to safely touch unfamiliar code; P1 incidents lose 45 minutes between alert and root cause; and pressure to ship faster keeps rising without the controls catching up.

## What Claude Code does differently

| | |
|---|---|
| **Reads the whole codebase** | Not just the open file. Understands structure, git history, and how services talk to each other. |
| **Plans before it acts** | Every change shown as a diff, line by line, before anything is touched. No silent auto-apply. |
| **Policy as code** | CLAUDE.md is a plain-English policy file committed to the repo. Same rules for all 180 engineers. |
| **Governance hook** | Tests run automatically on every change. No passing tests, no commit. |
| **Clean audit trail** | Every tool call logged. Every commit attributed to the engineer, not the bot. |

## The numbers (conservative)

| Team | Today | With Claude Code | Typical savings |
|---|---|---|---|
| Software Engineers (120) | ~1 week to ramp on unfamiliar code | ~1 day | ~50% of onboarding time |
| SREs (20) | ~45 min to find the issue at 2am | ~15 min | ~60% of find-time |
| Data Scientists (40) | Blocked on boilerplate pipelines | Ship ML work, not plumbing | ~70% of boilerplate hours |

**Unit math:** $1,500 in saved engineer-time per engineer per month vs. $100 in software cost. 15× ratio. Assumes conservative adoption and uses FinTechCo's fully-loaded hourly rate.

## Security posture

- **SOC 2 Type II** certified. Report available on request.
- **Contractual no-training clause.** Not a policy, not a promise — a contract term your legal team will read before you sign.
- **PCI-DSS aware, FFIEC ready.** Enterprise agreements built with regulated industries in mind.
- **HIPAA eligible** under BAA. 200k-token context window. All traffic HTTPS to api.anthropic.com.
- **No source code uploaded in bulk.** Files are read locally; only the session prompt transits the network.

## A pragmatic rollout

| Phase | When | What | Cost |
|---|---|---|---|
| **1 · Signal** | Weeks 1–3 | 12 engineers across all three teams. Pick two real projects. Measure cycle time, incident MTTR, and engineer sentiment. | ~$3.6k |
| **2 · Scale** | Weeks 4–8 | Expand to 40 engineers if phase 1 signal is positive. Publish CLAUDE.md policy. Roll out review plugin. | ~$12k |
| **3 · Decide** | Weeks 9–12 | Readout with real data from your team. You decide whether to broaden or stop. | — |

## What we need from you to start

1. **This week** — security overview, DPA, and SOC 2 report to your legal team so their review can run in parallel.
2. **Next week** — a 30-minute setup call with the person you designate to own the pilot.
3. **Week 6** — a pilot readout meeting on your calendar.

_No procurement commitment required today. No bulk license purchase required to run the pilot._

## Honest limitations

Claude Code will not replace senior engineers, will not eliminate code review, and will not fix a broken engineering culture. It works best when there's a real test suite to validate against. It gets things wrong sometimes — that's exactly why the Safety Gate, governance hooks, and human approval exist.

## Who's your partner

**Anthropic** is an AI safety lab. Safety isn't a feature we bolted on; it's the training objective. That's why Claude plans before it acts, why it shows its reasoning, and why your auditors will recognize the compliance posture when they read it.

---

**Contact:** Holden Ottolini · Applied AI · Anthropic · holdenstirling@gmail.com
