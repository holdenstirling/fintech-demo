# FinTechCo Deck — Full Audit & Recommendations

_Audit target: `FinTechCo_Claude_Code_Demo_v3.pptx` (20 slides)_
_Audience: Final-round Anthropic Solutions Architect / Applied AI Architect interview panel_
_Author: Holden Ottolini_

---

## Overall verdict

**Strong bones. The tone has swung too far toward "soft."**

The v3 deck successfully fixed the aggressive, bro-y tone of v2. But in removing dashes and softening language, we introduced a second problem: the deck now reads slightly apologetic in places ("easy," "gentle," "small asks," "friendly walk through"). That hurts you against Anthropic's SA rubric.

Based on 2026 candidate reports, the Anthropic SA/SE bar specifically looks for:

1. **Measured confidence.** You're the expert in the room on Claude Code. Sound like it.
2. **Customer problem framing before product.** You're already doing this well.
3. **Honest tradeoffs, not polished pitches.** The limitations slide is your single biggest asset — move it earlier.
4. **Systems thinking.** Talk about queues, scale, failure modes, and "what breaks at 180 engineers."
5. **Simplicity over cleverness.** Anthropic's own value: _"we don't invent a spaceship if all we need is a bicycle."_ Your deck should feel like a bicycle.
6. **Authenticity. Limited small talk. High bar for directness.**

**The fix is not to un-do the friendliness. It's to re-introduce _professional conviction_ in the titles while keeping the warm body copy.** Think "trusted advisor" not "eager vendor."

---

## Scorecard

| Dimension | Score | Notes |
|---|---|---|
| Narrative arc | 8 / 10 | Agenda → Problem → Discovery → Demo → ROI → Rollout → Close. Textbook. |
| Title clarity | 5 / 10 | Several titles are subtitles pretending to be titles. See rewrites below. |
| Tone calibration | 6 / 10 | Leaned too far toward "gentle." Should be _warm + confident_, not _apologetic_. |
| Executive scannability | 7 / 10 | If the CTO reads only the titles, do they get the story? Today: not quite. |
| Business framing | 8 / 10 | ROI and rollout are strong. Pricing math lands. |
| Technical credibility | 7 / 10 | Architecture is implicit. One slide should make the flow visible (Safety Gate, CLAUDE.md, hooks). |
| Honesty / trade-offs | 9 / 10 | Slide 19 is your secret weapon. Anthropic specifically looks for this. |
| Anthropic values alignment | 7 / 10 | Safety is mentioned but not framed as _Anthropic's identity_. |

---

## The title problem, in one sentence

**Most of your slide titles are currently the _subtitle_, and the real title is buried in small-caps above it.** On a projector, the first thing the room reads is the headline. Right now the headline is doing all the narrative lifting with zero help from the eyebrow label.

**Rule for every slide:** the room should be able to read only the main title and still know what this slide is _for_. Treat the small-caps eyebrow as _section_; treat the title as _takeaway_.

---

## Slide-by-slide audit

### Slide 1 — Cover

**Current:** Eyebrow: _"A learning session with FinTechCo"_. Title: _"Claude Code"_. Subtitle: _"A friendly walk through how your engineers, SREs, and data scientists can ship faster, together."_

**Issues:**
- _"Learning session"_ sounds like training, not a pitch. You are selling, not teaching.
- _"Friendly walk through"_ undersells you.

**Recommendation:**
- Eyebrow → `A working session with FinTechCo` (neutral, professional)
- Title → `Claude Code` (keep)
- Subtitle → `How 180 engineers ship faster, with the controls your auditors expect.`

Why: gives the CTO the two things they care about in one line — velocity and control.

---

### Slide 2 — Agenda

**Current title:** _"Here's how I'd love to spend our next 40 minutes together."_

**Issues:**
- Reads as a sentence, not a title. 11 words before the room learns this is the agenda.
- "I'd love to" is weaker than "I'll." Solutions Architects _drive_; they don't _ask_.

**Recommendation:**
- Eyebrow → `AGENDA · 40 MINUTES`
- Title → `Here's how we'll use our time together.`
- Keep the item descriptions exactly as-is — those are strong.
- Item 03 "Discovery session" body copy: change _"Five easy questions"_ → _"Five questions"_. "Easy" is unnecessary and slightly diminishing.

---

### Slide 3 — What is Claude Code

**Current title:** _"Think of it as a teammate in the terminal."_

**Issues:**
- Cute but doesn't answer the question the eyebrow asks. The room wants a definition before a metaphor.
- The three columns ("It reads your whole codebase / It plans before it acts / It checks its own work") are good. Keep.

**Recommendation:**
- Eyebrow → `WHAT IS CLAUDE CODE`
- Title → `A coding agent that works the way a senior engineer does.`
- Keep the supporting paragraph.

Why: Anthropic SA candidates are evaluated on whether they can explain AI capability to non-technical stakeholders. "Coding agent" is the accurate term; "works the way a senior engineer does" is the accessible frame.

---

### Slide 4 — Why are we here today

**Current title:** _"Before I share anything, here's what I think I'm hearing."_

**Issues:**
- Great instinct (demonstrating active listening). Bad title (too long, buries the takeaway).
- The four cards are excellent.

**Recommendation:**
- Eyebrow → `WHAT I'M HEARING`
- Title → `Four things on FinTechCo's plate, from what you've shared so far.`
- Subtitle (keep, tighten) → `Correct me where I'm wrong. This is the most valuable thirty seconds of the call.`

---

### Slide 5 — Discovery session

**Current title:** _"Five easy questions. Your answers will shape the demo."_

**Issues:**
- "Easy" is doing you no favors. Take it out.
- Q1–Q5 are well-scoped. Keep.

**Recommendation:**
- Eyebrow → `DISCOVERY`
- Title → `Five questions before I show you anything.`
- Keep the closing line about playback — that's a senior move.

---

### Slide 6 — Three teams at FinTechCo

**Current title:** _"Three teams, three very different problems."_

**Issues:** Title is fine. The "120 / 20 / 40" headcounts with TODAY / WITH CLAUDE CODE comparison is the single strongest slide in the deck. Don't touch it.

**Recommendation:**
- Eyebrow → `WHO THIS HELPS AT FINTECHCO` (keep)
- Title → `Three teams. Three different bottlenecks. One tool.` (slightly tighter)

---

### Slide 7 — Safety, security, governance

**Current title:** _"Built to feel comfortable in the environment you already work in."_

**Issues:**
- "Feel comfortable" is hedged language. For a regulated fintech audience, this is where you stand firm.
- Compliance strip is well-placed.

**Recommendation:**
- Eyebrow → `SAFETY, SECURITY, GOVERNANCE`
- Title → `Designed for a regulated environment from the start.`
- Keep all four supporting pillars.

---

### Slide 8 — Live demo opener

**Current title:** _"Let's walk through a morning with Claude Code."_

**Issues:** Good. Keep.

**Recommendation:** no change, except consider bolding slide 8 as the _center of gravity_ of the deck. Every slide before it builds toward it; every slide after it refers back to it.

---

### Slide 9 — What you just saw

**Current title:** _"Twelve minutes, four things you'd notice on Monday morning."_

**Issues:** Strong. Keep.

**Recommendation:** no change.

---

### Slide 10 — ROI framework

**Current title:** _"A framework, not a promise. We'll use your numbers."_

**Issues:**
- Excellent title. Do not change.
- "about 50% / 60% / 60% / 70%" is correct calibration — specific enough to be credible, hedged enough to be honest.
- The math callout ($1,500 savings vs $100 cost) is the single best ROI slide in the deck. Leave it alone.

---

### Slide 11 — Rollout plan

**Current title:** _"Three weeks to a signal. Three months to a decision."_

**Issues:** One of the strongest titles in the deck. Don't touch it.

**Recommendation:** no change.

---

### Slide 12 — Next steps

**Current title:** _"Three small asks. None of them require procurement today."_

**Issues:**
- "Small asks" is slightly diminutive for a CTO-level conversation. You _are_ asking for real things (access to legal, a named owner, a 30-minute setup call, and a pilot readout).
- The "No procurement today" framing is excellent and should stay.

**Recommendation:**
- Eyebrow → `NEXT STEPS`
- Title → `Three asks. None of them need procurement today.`

---

### Slide 13 — Appendix divider

**Current title:** _"A few things you may want to dig into later in our conversation."_

**Issues:** Too long, too hedged.

**Recommendation:**
- Title → `Appendix: the questions your team will ask next.`
- Subtitle (list): keep as-is.

---

### Slide 14 — Why Anthropic

**Current title:** _"This is as much a company question as it is a product question."_

**Issues:**
- Abstract. The room doesn't know what claim you're making.
- Content is strong (Constitutional AI, no training, 200k context, SOC 2, Claude plans before it acts). Title should preview the point.

**Recommendation:**
- Eyebrow → `WHY ANTHROPIC, WHY CLAUDE`
- Title → `You're not just buying a tool. You're picking a partner your auditors will meet.`

Why: this is the argument that wins against Copilot, Cursor, and Devin in a regulated-industry conversation. Say it out loud.

---

### Slide 15 — How we compare

**Current title:** _"Different tools for different problems."_

**Issues:** OK, but generic. You're making a sharper point inside the slide than the title suggests.

**Recommendation:**
- Eyebrow → `COMPETITIVE LANDSCAPE`
- Title → `The question isn't which AI tool. It's which problem you're solving.`
- (That sentence is already in your body copy. Promote it to the headline.)

---

### Slide 16 — Data, security, and your auditors

**Current title:** _"Plain answers to the questions you'll hear first."_

**Issues:** Strong. Keep.

**Recommendation:** no change.

---

### Slide 17 — CLAUDE.md at scale

**Current title:** _"How 180 engineers get the same rules on day one."_

**Issues:** Strong. Keep.

**Recommendation:** no change.

---

### Slide 18 — MCP integration

**Current title:** _"Claude Code connects to the tools your team already uses."_

**Issues:** Fine. Could be sharper.

**Recommendation:**
- Title → `Claude Code plugs into Jira, Confluence, and your internal APIs.`

Why: specificity builds credibility. A CTO scanning titles wants to see Jira and Confluence called out by name.

---

### Slide 19 — Honest limitations

**Current title:** _"Being honest about this makes everything else more credible."_

**Issues:**
- This is the most important slide in the whole deck for an Anthropic interview. The candidate research is unanimous: they evaluate _"candidates who confidently present a textbook solution and resist exploring alternatives miss the point. The interviewer wants to see you reason through trade-offs."_
- Your title is meta (talking about why you're being honest) instead of framing the honesty itself.

**Recommendation:**
- Eyebrow → `HONEST LIMITATIONS`
- Title → `Five things Claude Code won't do, so you can plan around them.`

Also: consider moving this slide _earlier_ — before the ROI slide — if the panel is senior enough. It disarms skepticism and earns you the right to make the ROI claim that follows.

---

### Slide 20 — Closing

**Current:** _"Let's build the pilot together."_ with _"I'd love to end our time with a name and a date, rather than a thank you."_

**Issues:** Almost perfect. One small tune-up.

**Recommendation:**
- Title → `Let's build the pilot together.` (keep)
- Subtitle → `I'd rather end on a name and a date than a thank-you. So: who on your side is the natural owner?`

Why: compressing "I'd love to end our time with…" → "I'd rather end on…" lands harder. Ending on the question forces the room to answer you.

---

## Cross-cutting recommendations

### 1. Re-balance the tone (most important)

Audit every instance of these hedging words and decide case-by-case whether to keep them: _easy, small, gentle, friendly, I'd love to, hopefully, just, a little, kind of, sort of, feel comfortable, tends to._

Rule of thumb: keep hedges in _body copy_, remove them from _titles_. Titles should sound like a senior person saying "here's what I know." Body copy can be the warmer human voice.

### 2. Add one architecture visual

The deck has zero systems diagrams. For a fintech CTO, one clean box-and-arrow diagram showing:

```
Engineer's laptop → CLAUDE.md (policy) → Claude Code CLI → Safety Gate (approve/decline) → Tests → Git commit (attributed to engineer)
                                                                ↓
                                                     api.anthropic.com (HTTPS, no training)
```

would carry more technical credibility than any paragraph. Drop it in at slide 7 or 17.

### 3. Add a "what would break" slide (optional but high-leverage)

Anthropic's SA rubric explicitly asks: _where does this fail at scale?_ You already have slide 19 (what Claude doesn't do). Consider a companion slide covering _failure modes_: "what happens when Claude is wrong / when CLAUDE.md is wrong / when a pilot engineer disagrees with a proposed change." This is the single most common missing piece in Solutions Architect demos.

### 4. Strengthen the Anthropic-mission thread

Per 2026 candidate reports: _"Anthropic weaves its mission of AI safety into every fiber of its hiring process."_ Your deck mentions SOC 2 and Constitutional AI but doesn't explicitly connect Claude Code's behavior (plans before acting, Safety Gate, honest-about-limits) to Anthropic's identity as a safety-first lab. A single line on slide 7 or 14 —_"the Safety Gate isn't a feature we bolted on; it's how Anthropic believes agentic work should behave"_— makes that thread visible to the panel.

### 5. Run the title-only scan

Before the interview, print the deck six-up, titles only. If a non-technical stakeholder can follow the narrative from titles alone, you're ready. If they can't, the titles are still too decorative.

---

## Proposed title set (copy-paste ready)

| # | Eyebrow | Title |
|---|---|---|
| 1 | A working session with FinTechCo | **Claude Code** |
| 2 | AGENDA · 40 MINUTES | Here's how we'll use our time together. |
| 3 | WHAT IS CLAUDE CODE | A coding agent that works the way a senior engineer does. |
| 4 | WHAT I'M HEARING | Four things on FinTechCo's plate, from what you've shared so far. |
| 5 | DISCOVERY | Five questions before I show you anything. |
| 6 | WHO THIS HELPS AT FINTECHCO | Three teams. Three different bottlenecks. One tool. |
| 7 | SAFETY, SECURITY, GOVERNANCE | Designed for a regulated environment from the start. |
| 8 | LIVE DEMO | Let's walk through a morning with Claude Code. |
| 9 | WHAT YOU JUST SAW | Twelve minutes, four things you'd notice on Monday morning. |
| 10 | MEASURING THE RETURN | A framework, not a promise. We'll use your numbers. |
| 11 | A PRAGMATIC ROLLOUT | Three weeks to a signal. Three months to a decision. |
| 12 | NEXT STEPS | Three asks. None of them need procurement today. |
| 13 | APPENDIX | The questions your team will ask next. |
| 14 | WHY ANTHROPIC, WHY CLAUDE | You're picking a partner your auditors will meet. |
| 15 | COMPETITIVE LANDSCAPE | The question isn't which AI tool. It's which problem you're solving. |
| 16 | DATA, SECURITY, AUDITORS | Plain answers to the questions you'll hear first. |
| 17 | CLAUDE.MD · GOVERNANCE AT SCALE | How 180 engineers get the same rules on day one. |
| 18 | MCP · INTEGRATION | Claude Code plugs into Jira, Confluence, and your internal APIs. |
| 19 | HONEST LIMITATIONS | Five things Claude Code won't do, so you can plan around them. |
| 20 | THANK YOU | Let's build the pilot together. |

---

## Priority order, if you only have an hour

1. **Update the 9 titles flagged in bold above** (slides 1, 2, 3, 4, 5, 7, 12, 14, 15, 18, 19). Biggest signal-to-effort ratio.
2. **Sweep body copy for "easy," "small," "gentle," "I'd love to"** — keep where warm, cut where weak.
3. **Add the architecture diagram** to slide 7 or 17.
4. **Rehearse slide 19 (limitations)** as a confident moment, not an apologetic one. Anthropic panels _reward_ this specifically.

Everything else in the deck is already working.
