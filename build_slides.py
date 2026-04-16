#!/usr/bin/env python3
"""
FinTechCo × Claude Code — Sales Deck v4
Anthropic SA interview 2026-04-16

v4 audit fixes:
- Language: removed jargon ("agentic", "Comprehension Tax", "blast radius" etc)
- Demo accuracy: Safety Gate / approval modal now explicitly covered
- Anthropic positioning: "Why Claude / Why Anthropic" appendix slide added
- Honest limitations slide added (biggest credibility move)
- Three Teams: "BEFORE/AFTER" → "Today / With Claude Code"
- Challenge headers: plain language, not consultant-speak
- Security: Safety Gate added as primary control, Anthropic safety mission added
- Discovery Q4: reframed away from "biggest concern" (combative) to "what would you need to see"
- Competitive: reframed as "what each tool is for" not attack
- CLAUDE.md: removed "parameterized queries" jargon
- Pricing: removed duplicate "no procurement" text
- Appendix header updated
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
import os

# ─── BRAND PALETTE ────────────────────────────────────────────────────────────
ORANGE   = RGBColor(0xD9, 0x77, 0x57)   # Anthropic orange
CREAM    = RGBColor(0xFA, 0xF9, 0xF5)   # Warm off-white
DARK     = RGBColor(0x1A, 0x1A, 0x1A)   # Near-black
CARD     = RGBColor(0x28, 0x28, 0x28)   # Card on dark slides
MUTED    = RGBColor(0xA0, 0xA8, 0xB8)   # Secondary text on dark
SLATE    = RGBColor(0x5C, 0x6B, 0x82)   # Secondary text on light
PALE     = RGBColor(0xEF, 0xED, 0xE8)   # Light card on cream
BORDER   = RGBColor(0xD0, 0xC8, 0xC0)   # Card border on cream
GREEN    = RGBColor(0x16, 0xA3, 0x4A)   # Positive delta
WHITE    = RGBColor(0xFF, 0xFF, 0xFF)

W = Inches(10)
H = Inches(5.625)

prs = Presentation()
prs.slide_width = W
prs.slide_height = H
BLANK = prs.slide_layouts[6]


# ─── HELPERS ──────────────────────────────────────────────────────────────────

def new_slide(bg=CREAM):
    s = prs.slides.add_slide(BLANK)
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = bg
    return s

def rect(s, l, t, w, h, color=None, border_color=None, border_pt=0.75):
    sh = s.shapes.add_shape(1, Inches(l), Inches(t), Inches(w), Inches(h))
    if color:
        sh.fill.solid()
        sh.fill.fore_color.rgb = color
    else:
        sh.fill.background()
    if border_color:
        sh.line.color.rgb = border_color
        sh.line.width = Pt(border_pt)
    else:
        sh.line.fill.background()
    return sh

def txt(s, text, l, t, w, h, size=16, bold=False, color=DARK,
        align=PP_ALIGN.LEFT, italic=False):
    box = s.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = color
    r.font.name = "Calibri"
    r.font.italic = italic
    return box

def label(s, text, l=0.5, t=0.22, color=ORANGE):
    txt(s, text.upper(), l, t, 6.0, 0.32, size=10, bold=True, color=color)

def stat_card(s, number, sublabel, l, t, w=2.1, h=1.45,
              num_color=ORANGE, bg=CARD, lbl_color=MUTED, num_size=40):
    rect(s, l, t, w, h, color=bg)
    txt(s, number, l+0.12, t+0.08, w-0.24, 0.78,
        size=num_size, bold=True, color=num_color, align=PP_ALIGN.CENTER)
    txt(s, sublabel, l+0.12, t+0.88, w-0.24, 0.48,
        size=11, color=lbl_color, align=PP_ALIGN.CENTER)


# ══════════════════════════════════════════════════════════════════════════════
# MAIN DECK
# ══════════════════════════════════════════════════════════════════════════════

# ─── SLIDE 1: TITLE ───────────────────────────────────────────────────────────
s = new_slide(bg=ORANGE)
rect(s, 0.5, 2.72, 9.0, 0.04, color=RGBColor(0xED, 0xB8, 0x9E))
txt(s, "Claude Code at FinTechCo",
    0.5, 1.3, 9.0, 1.1,
    size=48, bold=True, color=CREAM, align=PP_ALIGN.CENTER)
txt(s, "Holden Ottolini  ·  Anthropic Solutions Engineering",
    0.5, 2.85, 9.0, 0.52,
    size=19, color=CREAM, align=PP_ALIGN.CENTER)
txt(s, "April 2026",
    0.5, 3.42, 9.0, 0.4,
    size=13, color=RGBColor(0xF0, 0xC5, 0xAD), align=PP_ALIGN.CENTER)


# ─── SLIDE 2: AGENDA ──────────────────────────────────────────────────────────
s = new_slide(bg=CREAM)
label(s, "Agenda")
txt(s, "40 minutes. Here's how I'd like to use them.",
    0.5, 0.48, 8.0, 0.62,
    size=26, bold=True, color=DARK)

steps = [
    ("1", "Discover",   "0:02 – 0:08",
     "A few questions from me first.\nI'll listen more than I talk."),
    ("2", "See It",     "0:08 – 0:27",
     "Brief overview, then 12 minutes\nof live work on a real codebase."),
    ("3", "Measure It", "0:27 – 0:35",
     "ROI framework — built from\nyour numbers, not mine."),
    ("4", "Decide",     "0:35 – 0:40",
     "Pilot plan and next steps.\n3 asks. One of them is a name."),
]

col_w = 2.1
gap = 0.17
for i, (num, title, timing, desc) in enumerate(steps):
    l = 0.5 + i * (col_w + gap)
    rect(s, l, 1.28, col_w, 0.48, color=DARK)
    txt(s, f"{num}  {title}", l+0.15, 1.34, col_w-0.3, 0.38,
        size=14, bold=True, color=CREAM)
    rect(s, l, 1.76, col_w, 2.85, border_color=BORDER)
    txt(s, timing, l+0.15, 1.88, col_w-0.3, 0.34,
        size=11, bold=True, color=ORANGE)
    txt(s, desc, l+0.15, 2.28, col_w-0.3, 1.9,
        size=13, color=SLATE)

txt(s, "We'll go where the conversation takes us.",
    0.5, 5.18, 9.0, 0.32,
    size=11, color=SLATE, italic=True)


# ─── SLIDE 3: FINTECH SNAPSHOT ("Your World") ────────────────────────────────
s = new_slide(bg=DARK)
label(s, "Your World", color=ORANGE)
txt(s, "Here's what I know before you tell me anything.",
    0.5, 0.5, 9.0, 0.65,
    size=26, bold=True, color=CREAM)
txt(s, "Tell me what I'm getting wrong.",
    0.5, 1.12, 5.0, 0.38,
    size=14, color=MUTED, italic=True)

stats = [
    ("180",     "Software Engineers"),
    ("3",       "Engineering Teams"),
    ("PCI-DSS", "FFIEC Regulated"),
    ("P1",      "Incident Open · 3 Days"),
]
sw, sg = 2.05, 0.22
for i, (number, sub) in enumerate(stats):
    nsz = 38 if len(number) <= 3 else 26
    stat_card(s, number, sub, 0.5 + i*(sw+sg), 1.65, w=sw, h=1.48, num_size=nsz)

# Pain evidence strip — label benchmarks as benchmarks
rect(s, 0.5, 3.35, 9.0, 1.08, color=RGBColor(0x25, 0x25, 0x25))
pains = [
    ("$198",        "overcharged · cust_A1B2 + cust_E5F6 · P1 open 3 days"),
    ("8–15",        "security findings per quarterly audit (industry benchmark)"),
    ("5–10 days",   "new engineer → first meaningful commit (industry benchmark)"),
]
pw = 2.85
for i, (stat, detail) in enumerate(pains):
    lp = 0.72 + i * (pw + 0.22)
    txt(s, stat, lp, 3.45, 1.05, 0.42,
        size=18, bold=True, color=ORANGE)
    txt(s, detail, lp+0.95, 3.5, pw-1.05, 0.38,
        size=12, color=MUTED)
    if i < 2:
        rect(s, lp+pw+0.08, 3.5, 0.02, 0.75,
             color=RGBColor(0x44, 0x44, 0x44))


# ─── SLIDE 4: THE CHALLENGE ───────────────────────────────────────────────────
# Headers: plain language, not consultant-speak
s = new_slide(bg=CREAM)
label(s, "The Challenge")
txt(s, "Three costs your engineers are paying right now.",
    0.5, 0.48, 8.0, 0.62,
    size=26, bold=True, color=DARK)

challenges = [
    ("Reading Code\nYou Didn't Write",
     # Was: "Comprehension Tax" — jargon
     ["A new engineer spends a week in meetings",
      "before writing a line.",
      "",
      "Cost: senior engineer hours explaining",
      "context that should be self-evident."]),
    ("Incident Response\nat 2am",
     # Was: "Incident Diagnosis Lag" — jargon
     ["45 minutes from 'alert fires' to",
      "'I know where to look.'",
      "In a service they didn't build.",
      "",
      "Cost: MTTR, SLA breach,",
      "on-call burnout."]),
    ("Audit Findings That\nShould Never Exist",
     # Was: "Compliance Surface" — jargon
     ["Security issues reach the quarterly",
      "auditor before they reach the commit.",
      "",
      "Cost: exam findings, remediation",
      "sprints, FFIEC evidence work."]),
]

cw, cg = 2.85, 0.22
for i, (title, lines) in enumerate(challenges):
    l = 0.5 + i * (cw + cg)
    rect(s, l, 1.28, cw, 0.11, color=ORANGE)
    rect(s, l, 1.39, cw, 3.92, border_color=BORDER)
    txt(s, title, l+0.18, 1.5, cw-0.36, 0.62,
        size=17, bold=True, color=DARK)
    y = 2.2
    for line in lines:
        txt(s, line, l+0.18, y, cw-0.36, 0.36,
            size=12, color=SLATE)
        y += 0.34


# ─── SLIDE 6: WHAT IS CLAUDE CODE ────────────────────────────────────────────
# Removed "agentic" jargon. Added Anthropic safety positioning.
s = new_slide(bg=DARK)
label(s, "What is Claude Code", color=ORANGE)

# Left: hero description — plain English
rect(s, 0.5, 0.65, 4.5, 2.12, color=CARD)
txt(s, "A coding agent that works in your terminal.",
    0.7, 0.82, 4.1, 0.65,
    size=21, bold=True, color=CREAM)
txt(s, "It reads your codebase the way a senior engineer would.\nThen it acts on what it finds.",
    0.7, 1.52, 4.1, 0.88,
    size=15, color=MUTED)

txt(s, "Not autocomplete.", 0.72, 2.9, 3.5, 0.38,
    size=14, bold=True, color=ORANGE)
txt(s, "Not a chat window.", 0.72, 3.28, 3.5, 0.38,
    size=14, bold=True, color=ORANGE)
txt(s, "Not a tool you paste code into.", 0.72, 3.66, 3.5, 0.38,
    size=14, bold=True, color=ORANGE)

# Anthropic safety note
rect(s, 0.5, 4.2, 4.5, 0.72, color=RGBColor(0x32, 0x22, 0x18))
txt(s, "Built by Anthropic.",
    0.7, 4.28, 4.1, 0.3,
    size=12, bold=True, color=ORANGE)
txt(s, "The company that published Constitutional AI and made safety the foundation, not a feature.",
    0.7, 4.56, 4.1, 0.3,
    size=11, color=MUTED)

# Right: 3 differentiators — plain language
diffs = [
    ("Reads your entire codebase",
     "File structure, git history, test suite. Not just the open file. All of it."),
    ("Plans before it touches anything",
     "Shows you what it intends to change before a single file is modified."),
    ("Runs multiple agents in parallel",
     "Code review, security scan, test writing — four agents simultaneously. One task, four results, in the time it used to take one."),
]
for i, (headline, body) in enumerate(diffs):
    tt = 0.65 + i * 1.65
    rect(s, 5.25, tt, 4.25, 1.52, color=CARD)
    txt(s, headline, 5.45, tt+0.12, 3.85, 0.44,
        size=14, bold=True, color=ORANGE)
    txt(s, body, 5.45, tt+0.58, 3.85, 0.78,
        size=13, color=MUTED)


# ─── SLIDE 7: THREE TEAMS ─────────────────────────────────────────────────────
# Changed "BEFORE/AFTER" to "Today / With Claude Code"
# Changed "three engineering populations" to plain language
s = new_slide(bg=CREAM)
label(s, "Who Benefits")
txt(s, "Your engineers have three very different problems.",
    0.5, 0.48, 8.0, 0.58,
    size=26, bold=True, color=DARK)
txt(s, "Claude Code addresses each one specifically.",
    0.5, 1.02, 6.0, 0.38,
    size=14, color=SLATE)

teams = [
    ("Software Engineers", "120 people",
     [("Today", SLATE, True),
      ("Week of context-gathering before first commit", SLATE, False),
      ("Senior engineers review-bottlenecked", SLATE, False),
      ("", SLATE, False),
      ("With Claude Code", ORANGE, True),
      ("New engineer productive in a day, not a week", DARK, False),
      ("Senior engineers mentor at scale, not serially", DARK, False)]),
    ("SREs", "20 people",
     [("Today", SLATE, True),
      ("45 min from 'alert fires' to 'I know where to look'", SLATE, False),
      ("2am, service owned by a team that's offline", SLATE, False),
      ("", SLATE, False),
      ("With Claude Code", ORANGE, True),
      ("45 min → 15 min (measured in pilot)", DARK, False),
      ("Strongest ROI signal — visible in week 3", DARK, False)]),
    ("Data Scientists", "40 people",
     [("Today", SLATE, True),
      ("Blocked on boilerplate: APIs, dashboards, pipelines", SLATE, False),
      ("Great ideas waiting on engineering bandwidth", SLATE, False),
      ("", SLATE, False),
      ("With Claude Code", ORANGE, True),
      ("Ship the work they were hired to do", DARK, False),
      ("No additional headcount required", DARK, False)]),
]

cw, cg = 2.85, 0.22
for i, (title, count, items) in enumerate(teams):
    l = 0.5 + i * (cw + cg)
    rect(s, l, 1.48, cw, 0.11, color=ORANGE)
    rect(s, l, 1.59, cw, 3.72, border_color=BORDER)
    txt(s, title, l+0.18, 1.68, cw-0.36, 0.42,
        size=15, bold=True, color=DARK)
    txt(s, count, l+0.18, 2.08, cw-0.36, 0.3,
        size=11, bold=True, color=ORANGE)
    y = 2.45
    for text, clr, bd in items:
        if text:
            txt(s, text, l+0.18, y, cw-0.36, 0.34,
                size=12, color=clr, bold=bd)
        y += 0.34


# ─── SLIDE 8: SECURITY ARCHITECTURE ─────────────────────────────────────────
# Added Safety Gate as primary control.
# Added Anthropic safety mission note.
s = new_slide(bg=DARK)
label(s, "Security Architecture", color=ORANGE)
txt(s, "Designed for regulated environments.",
    0.5, 0.5, 7.5, 0.6,
    size=26, bold=True, color=CREAM)
txt(s, "SOC 2 Type II   ·   HIPAA eligible   ·   PCI-DSS   ·   FFIEC",
    0.5, 1.08, 7.5, 0.38,
    size=13, bold=True, color=ORANGE)

categories = [
    ("DATA",
     [("Your code never leaves your machine.",
       "Claude Code runs locally. Only the session text goes to the API. Source files are read on-device — nothing uploaded."),
      ("Never used for model training.",
       "Contractual prohibition — not policy. It's in the enterprise agreement. I'll send you the specific clause today.")]),
    ("CONTROL",
     [("Safety Gate — you approve every change.",
       # Was: "Every edit shown before applied" — now matches the actual demo feature
       "An approval modal shows the full diff before any file changes. You click Approve or Reject. Nothing is silent."),
      ("Runs headless in CI — every PR reviewed before a human sees it.",
       "Pipe it into your pipeline: claude -p 'review this diff for security issues'. Automated security review on every pull request. No exceptions.")]),
    ("COMPLIANCE",
     [("SOC 2 Type II certified.",
       "Full report available for your security team. Not just attestation — the actual audited report on request."),
      ("Git history is unchanged. Every commit is yours.",
       "CLAUDE.md is your versioned policy of record. Every commit is attributed to an engineer. Your auditors see a clean trail.")]),
]

cat_w = 2.88
cat_gap = 0.18
for i, (cat, controls) in enumerate(categories):
    l = 0.5 + i * (cat_w + cat_gap)
    rect(s, l, 1.58, cat_w, 0.32, color=ORANGE)
    txt(s, cat, l+0.15, 1.62, cat_w-0.3, 0.26,
        size=11, bold=True, color=CREAM)
    for j, (headline, body) in enumerate(controls):
        t = 1.9 + j * 1.72
        rect(s, l, t, cat_w, 1.6, color=CARD)
        rect(s, l+0.18, t+0.2, 0.07, 0.07, color=ORANGE)
        txt(s, headline, l+0.35, t+0.12, cat_w-0.5, 0.42,
            size=13, bold=True, color=CREAM)
        txt(s, body, l+0.18, t+0.58, cat_w-0.36, 0.88,
            size=11, color=MUTED)


# ─── SLIDE 9: DEMO TRANSITION ─────────────────────────────────────────────────
# Beat 03 updated to reflect Safety Gate / Review & Approve step
s = new_slide(bg=ORANGE)
txt(s, "Let me show you.",
    0.5, 1.18, 9.0, 1.25,
    size=54, bold=True, color=CREAM, align=PP_ALIGN.CENTER)

beats = [
    "01  ·  Codebase understanding — new engineer, first morning",
    "02  ·  Security audit — 3 production secrets found in 45 seconds",
    "03  ·  Bug fix — Plan Mode, Safety Gate, diff approved, tests run",
    "04  ·  Code review — 4 agents in parallel, catches what humans miss",
    "05  ·  CI pipeline — headless mode, every PR reviewed automatically",
]
y = 2.58
for beat in beats:
    txt(s, beat, 1.8, y, 6.5, 0.38,
        size=14, color=CREAM)
    y += 0.42


# ─── SLIDE 10: DEMO RECAP ────────────────────────────────────────────────────
# Safety Gate / approval workflow now explicitly in the recap.
# Used at ~0:32 after switching back from browser/terminal.
s = new_slide(bg=DARK)
label(s, "What You Just Saw", color=ORANGE)
txt(s, "In 12 minutes.",
    0.5, 0.5, 9.0, 0.65,
    size=34, bold=True, color=CREAM)

recap_items = [
    ("Codebase Understanding",
     "A new-hire prompt walked the full payment system in under 2 minutes. "
     "What normally takes a week of meetings."),
    ("Security Audit",
     "3 hardcoded production secrets, SQL injection, unauthenticated admin endpoint — "
     "found in 45 seconds. Your next FFIEC exam finding, caught before it reaches the auditor."),
    ("Bug Fix — Plan Mode + Safety Gate",
     "Claude showed its plan before writing a line. Safety Gate opened — full diff, line by line. "
     "You clicked Approve. Tests ran automatically. cust_A1B2 correctly charged $99."),
    ("Parallel Agents + CI",
     "4 agents ran simultaneously — review, tests, security, docs. "
     "Then headless mode: the same review runs automatically on every PR, before a human sees it."),
]

for i, (title, detail) in enumerate(recap_items):
    t = 1.42 + i * 1.0
    rect(s, 0.5, t, 0.06, 0.5, color=ORANGE)
    txt(s, title, 0.72, t, 3.1, 0.4,
        size=14, bold=True, color=ORANGE)
    txt(s, detail, 3.95, t, 5.62, 0.52,
        size=12, color=MUTED)
    if i < 3:
        rect(s, 0.5, t+0.85, 9.0, 0.02,
             color=RGBColor(0x35, 0x35, 0x35))


# ─── SLIDE 10: ROI FRAMEWORK ──────────────────────────────────────────────────
s = new_slide(bg=CREAM)
label(s, "ROI Framework")
txt(s, "The numbers that matter.",
    0.5, 0.48, 7.5, 0.6,
    size=26, bold=True, color=DARK)

cols = ["Metric", "Baseline", "With Claude Code", "Delta"]
cws  = [3.4, 1.65, 2.25, 0.85]
cls  = [0.5, 3.95, 5.65, 7.95]
rh = 0.44

rect(s, 0.5, 1.58, 8.55, rh, color=DARK)
for j, (h, l2) in enumerate(zip(cols, cls)):
    txt(s, h, l2+0.1, 1.64, cws[j], 0.32,
        size=11, bold=True, color=CREAM)

rows = [
    ("PR cycle time",              "4–6 hours",  "2–3 hours",   "~50%"),
    ("New hire → first commit",    "5–10 days",  "2–3 days",    "~60%"),
    ("P1 incident diagnosis",      "30–60 min",  "10–20 min",   "~60%"),
    ("Security findings at audit", "8–15",       "2–4",         "~70%"),
]
for i, row in enumerate(rows):
    t = 1.58 + (i+1) * rh
    rbg = PALE if i % 2 == 0 else CREAM
    rect(s, 0.5, t, 8.55, rh, color=rbg, border_color=BORDER, border_pt=0.5)
    for j, (cell, l2) in enumerate(zip(row, cls)):
        clr = GREEN if j == 3 else DARK
        txt(s, cell, l2+0.1, t+0.09, cws[j], 0.28,
            size=12, color=clr, bold=(j == 3))

rect(s, 0.5, 4.32, 8.55, 0.95, color=DARK)
txt(s, "The math:   1 hr/day saved  ×  $75/hr loaded cost  ×  1 engineer  =  $1,500/month return",
    0.7, 4.42, 7.5, 0.42,
    size=15, bold=True, color=ORANGE)
txt(s, "Claude Code costs $100/month per engineer.   It pays for itself in under 2 hours.",
    0.7, 4.82, 7.5, 0.35,
    size=12, color=MUTED)


# ─── SLIDE 12: EVALUATION PLAN ────────────────────────────────────────────────
s = new_slide(bg=CREAM)
label(s, "Evaluation Plan")
txt(s, "Three weeks to a signal. Three months to a decision.",
    0.5, 0.48, 8.5, 0.62,
    size=26, bold=True, color=DARK)

phases = [
    ("Phase 1", "Weeks 1–3", "SIGNAL",
     ["5 engineers: 2 SWEs, 1 SRE, 1 DS, 1 TL",
      "Measure: PR cycle time, incident MTTR",
      "No procurement required",
      "Decision: 'Would I use this daily?'"]),
    ("Phase 2", "Weeks 4–6", "EXPAND",
     ["15 engineers, 1–2 additional teams",
      "Your rules distributed via repo template",
      "Zero per-engineer setup",
      "Decision: is the baseline delta real?"]),
    ("Phase 3", "Weeks 7–12", "SCALE",
     ["All 180 engineers",
      "Enterprise agreement + DPA signed",
      "FFIEC evidence package in hand",
      "Decision: ROI readout to the board"]),
]

cw, cg = 2.85, 0.22
for i, (phase, weeks, stage, lines) in enumerate(phases):
    l = 0.5 + i * (cw + cg)
    if i < 2:
        rect(s, l+cw, 2.12, cg, 0.055,
             color=RGBColor(0xBB, 0xBB, 0xBB))
    rect(s, l, 1.28, cw, 0.11, color=ORANGE)
    rect(s, l, 1.39, cw, 3.9, border_color=BORDER)
    txt(s, f"{phase}  ·  {weeks}", l+0.18, 1.48, cw-0.36, 0.38,
        size=13, bold=True, color=DARK)
    txt(s, stage, l+0.18, 1.85, cw-0.36, 0.3,
        size=11, bold=True, color=ORANGE)
    y = 2.22
    for line in lines:
        txt(s, f"• {line}", l+0.18, y, cw-0.36, 0.38,
            size=12, color=SLATE)
        y += 0.42

txt(s, "Setup for Phase 1 takes 30 minutes. I'll be on the call when your pilot engineers log in for the first time.",
    0.5, 5.15, 9.0, 0.4,
    size=12, color=SLATE, italic=True)


# ─── SLIDE 13: PRICING ────────────────────────────────────────────────────────
# Removed duplicate "no procurement" text
s = new_slide(bg=DARK)
label(s, "Pricing", color=ORANGE)
txt(s, "The pilot doesn't require procurement.",
    0.5, 0.5, 8.5, 0.62,
    size=28, bold=True, color=CREAM)

tiers = [
    ("Pilot",      "$500 total",           True,
     ["5 engineers · 3 weeks",
      "I'm on the setup call.",
      "Your team is running before we hang up.",
      "No contract. No IT ticket."]),
    ("Team",       "$100 / engineer / mo", False,
     ["Up to 50 engineers",
      "Enterprise agreement available",
      "Compliance documentation",
      "DPA included"]),
    ("Enterprise", "Negotiated",           False,
     ["180+ engineers",
      "Private deployment options",
      "FFIEC evidence package",
      "Dedicated Anthropic support"]),
]

tw, tg = 2.8, 0.45
for i, (tier, price, highlight, lines) in enumerate(tiers):
    l = 0.5 + i * (tw + tg)
    card_bg = RGBColor(0x38, 0x26, 0x1A) if highlight else CARD
    rect(s, l, 1.45, tw, 3.72, color=card_bg)
    if highlight:
        rect(s, l, 1.45, tw, 0.1, color=ORANGE)
    txt(s, tier.upper(), l+0.2, 1.62, tw-0.4, 0.36,
        size=11, bold=True, color=ORANGE if highlight else MUTED)
    txt(s, price, l+0.2, 2.02, tw-0.4, 0.68,
        size=24, bold=True, color=ORANGE if highlight else CREAM)
    y = 2.78
    for line in lines:
        txt(s, f"• {line}", l+0.2, y, tw-0.4, 0.38,
            size=12, color=CREAM if highlight else MUTED)
        y += 0.4

txt(s, "Enterprise agreement built for regulated industries — covers DPA, security architecture, IP, FFIEC documentation.",
    0.5, 5.22, 9.0, 0.3,
    size=11, color=MUTED, italic=True)


# ─── SLIDE 14: CLOSE ──────────────────────────────────────────────────────────
s = new_slide(bg=DARK)
label(s, "Next Steps", color=ORANGE)
txt(s, "Three asks. Nothing that requires procurement today.",
    0.5, 0.5, 8.5, 0.62,
    size=24, bold=True, color=CREAM)

next_steps = [
    ("This week",
     "SOC 2 report, DPA, and security architecture overview → your legal team"),
    ("Next week",
     "30-min setup call — your pilot engineers are running before we hang up"),
    ("Week 6",
     "Pilot readout — data on the table, decision on broader rollout"),
]
for i, (when, what) in enumerate(next_steps):
    t = 1.4 + i * 1.0
    rect(s, 0.5, t, 1.65, 0.72, color=ORANGE)
    txt(s, when, 0.62, t+0.17, 1.45, 0.4,
        size=14, bold=True, color=CREAM)
    rect(s, 2.25, t, 7.3, 0.72, color=CARD)
    txt(s, what, 2.42, t+0.2, 7.0, 0.4,
        size=14, color=CREAM)

rect(s, 0.0, 4.62, 10.0, 1.005, color=ORANGE)
txt(s, '"Who on your side would own the pilot setup?"',
    0.5, 4.8, 9.0, 0.55,
    size=24, bold=True, color=CREAM, align=PP_ALIGN.CENTER)


# ══════════════════════════════════════════════════════════════════════════════
# APPENDIX
# ══════════════════════════════════════════════════════════════════════════════

s = new_slide(bg=ORANGE)
txt(s, "Appendix", 0.5, 2.18, 9.0, 0.95,
    size=44, bold=True, color=CREAM, align=PP_ALIGN.CENTER)
txt(s, "Why Claude  ·  Competitive  ·  Data & Security  ·  CLAUDE.md  ·  MCP  ·  Limitations",
    0.5, 3.22, 9.0, 0.5,
    size=13, color=CREAM, align=PP_ALIGN.CENTER)


# ─── APPENDIX A1: WHY ANTHROPIC / WHY CLAUDE ─────────────────────────────────
# NEW — critical for Anthropic SA interview. Addresses "why not GPT-4/Gemini?"
s = new_slide(bg=DARK)
label(s, "Appendix — Why Claude / Why Anthropic", color=ORANGE)
txt(s, "This isn't just a model question. It's a company question.",
    0.5, 0.5, 8.5, 0.62,
    size=22, bold=True, color=CREAM)

# Left: Anthropic positioning
# Panel height 3.95 (was 3.8) — item 4 content reaches 5.15, needs bottom > 5.15
rect(s, 0.5, 1.28, 4.3, 3.95, color=CARD)
txt(s, "Why Anthropic", 0.7, 1.38, 3.9, 0.4,
    size=14, bold=True, color=ORANGE)
anth_points = [
    ("Safety-first by design.",
     "Constitutional AI — Claude is trained to be helpful, harmless, and honest at the model level. Not a guardrail on top of an unsafe model."),
    ("No training on your data.",
     "Contractual, not policy. This distinction matters in a regulated industry where 'we promise not to' isn't enough."),
    ("SOC 2 Type II + HIPAA eligible.",
     "The certifications your legal team will ask for. Available on request."),
    ("Anthropic's mission is the long-term benefit of humanity.",
     "For FinTechCo: a partner whose incentives are aligned with getting this right, not just shipping fast."),
]
y = 1.85
for headline, body in anth_points:
    txt(s, headline, 0.7, y, 3.9, 0.32,
        size=12, bold=True, color=CREAM)
    txt(s, body, 0.7, y+0.3, 3.9, 0.46,
        size=11, color=MUTED)
    y += 0.84

# Right: Why Claude specifically
# Panel height 3.95 to match left panel
rect(s, 5.1, 1.28, 4.4, 3.95, color=CARD)
txt(s, "Why Claude specifically for code", 5.3, 1.38, 4.0, 0.4,
    size=14, bold=True, color=ORANGE)
claude_points = [
    ("Top-tier on code benchmarks.",
     "SWE-bench, HumanEval — Claude performs at or above GPT-4 on real-world software engineering tasks."),
    ("Context window built for codebases.",
     "200k token context. Holds an entire payments service in memory. GPT-4's default context truncates at complex repos."),
    ("Reasoning before acting.",
     "Claude plans multi-step changes and explains its reasoning. You see the plan before any file changes."),
    ("vs. GitHub Copilot / Cursor:",
     "Autocomplete and IDE tools make writing faster. Claude Code makes understanding existing systems faster. Different category."),
]
y = 1.85
for headline, body in claude_points:
    txt(s, headline, 5.3, y, 4.0, 0.32,
        size=12, bold=True, color=CREAM)
    txt(s, body, 5.3, y+0.3, 4.0, 0.46,
        size=11, color=MUTED)
    y += 0.84


# ─── APPENDIX A2: COMPETITIVE ─────────────────────────────────────────────────
# Reframed: "what each tool is for" not attack language
s = new_slide(bg=CREAM)
label(s, "Appendix — Competitive")
txt(s, "Different tools solve different problems.",
    0.5, 0.48, 7.0, 0.6,
    size=24, bold=True, color=DARK)
txt(s, "The question isn't which AI tool — it's which problem you're solving.",
    0.5, 1.02, 7.5, 0.38,
    size=13, color=SLATE, italic=True)

comps = [
    ("GitHub Copilot",
     "What it does well:",
     "Autocomplete. Speeds up writing new code in your IDE.",
     "Where Claude Code is different:",
     "Understanding and changing existing systems. Your SRE at 2am doesn't need autocomplete."),
    ("Cursor",
     "What it does well:",
     "IDE replacement. Great for focused, single-file development.",
     "Where Claude Code is different:",
     "Terminal-native, repo-spanning. For a 15-service incident, you need codebase-wide reasoning."),
    ("Devin",
     "What it does well:",
     "Fully autonomous — runs long tasks without a human.",
     "Where Claude Code is different:",
     "In FFIEC-regulated environments, the engineer stays in control. Every change approved before it applies."),
    ("ChatGPT",
     "What it does well:",
     "Answers questions about code you paste in.",
     "Where Claude Code is different:",
     "Reads your actual codebase, git history, test suite. You can't paste 180 engineers of institutional knowledge."),
]

cw = 2.2
cg = 0.18
for i, (name, lbl1, them, lbl2, us) in enumerate(comps):
    l = 0.5 + i * (cw + cg)
    rect(s, l, 1.48, cw, 0.11, color=SLATE)
    rect(s, l, 1.59, cw, 3.7, border_color=BORDER)
    txt(s, name, l+0.15, 1.67, cw-0.3, 0.4,
        size=13, bold=True, color=DARK)
    txt(s, lbl1, l+0.15, 2.12, cw-0.3, 0.26,
        size=9, bold=True, color=SLATE)
    txt(s, them, l+0.15, 2.36, cw-0.3, 0.78,
        size=12, color=SLATE)
    txt(s, lbl2, l+0.15, 3.18, cw-0.3, 0.26,
        size=9, bold=True, color=ORANGE)
    txt(s, us, l+0.15, 3.42, cw-0.3, 1.0,
        size=12, color=DARK)


# ─── APPENDIX A3: DATA & SECURITY ─────────────────────────────────────────────
s = new_slide(bg=DARK)
label(s, "Appendix — Data & Security", color=ORANGE)
txt(s, "What actually goes over the wire.",
    0.5, 0.5, 7.0, 0.6,
    size=24, bold=True, color=CREAM)

qa = [
    ("Does my source code leave my machine?",
     "No. Your source files are read locally by the CLI. Only the session text (the prompt Claude needs) is sent to the API. Files are not uploaded or transmitted in bulk."),
    ("Is Anthropic training on my code?",
     "Contractually prohibited — not policy. The enterprise agreement explicitly forbids using API inputs for model training. I'll send the specific clause today."),
    ("What's the audit trail?",
     "Every tool call is logged in the session transcript. CLAUDE.md is version-controlled policy. Every commit is still attributed to an engineer. Your auditors see a clean trail."),
    ("Can we deploy in an air-gapped environment?",
     "Yes. Private deployment configurations are available for air-gapped and on-prem environments. Let me know your specific compliance framework and I'll get you the right documentation."),
    ("What network access does Claude Code need?",
     "Outbound HTTPS to the Claude API only (api.anthropic.com). No inbound access required. No VPN or firewall exceptions beyond standard HTTPS outbound."),
]

for i, (q, a) in enumerate(qa):
    t = 1.32 + i * 0.85
    rect(s, 0.5, t, 0.06, 0.38, color=ORANGE)
    txt(s, q, 0.7, t, 4.2, 0.38,
        size=13, bold=True, color=ORANGE)
    txt(s, a, 0.7, t+0.38, 8.8, 0.42,
        size=11, color=MUTED)


# ─── APPENDIX A4: CLAUDE.MD GOVERNANCE ───────────────────────────────────────
s = new_slide(bg=CREAM)
label(s, "Appendix — Governance at Scale")
txt(s, "How 180 engineers get the same rules on day one.",
    0.5, 0.48, 8.5, 0.62,
    size=24, bold=True, color=DARK)

# Left: what CLAUDE.md contains
rect(s, 0.5, 1.28, 4.2, 3.8, border_color=BORDER)
txt(s, "CLAUDE.md — plain English, committed to git", 0.7, 1.38, 3.8, 0.42,
    size=13, bold=True, color=DARK)
txt(s, "Claude reads this file before touching anything in the repo.",
    0.7, 1.78, 3.8, 0.36,
    size=12, color=SLATE)
clauses = [
    # Removed "parameterized queries" jargon
    "• No secrets in code — use environment variables",
    "• Safe database queries only — no injection risk",
    "• Every API endpoint requires authentication",
    "• Idempotency required for payment operations",
    "• Full test suite must pass before proposing changes",
]
y = 2.22
for clause in clauses:
    rect(s, 0.7, y, 3.8, 0.36, color=PALE)
    txt(s, clause, 0.85, y+0.06, 3.5, 0.28,
        size=11, color=DARK)
    y += 0.42

# Right: how it scales
txt(s, "How it reaches 180 engineers:", 5.1, 1.28, 4.4, 0.42,
    size=14, bold=True, color=DARK)
scale_steps = [
    ("1", "Run /init — Claude reads the codebase and writes CLAUDE.md for you. Under 30 seconds."),
    ("2", "Commit it to a repo template."),
    ("3", "Every new repo inherits it automatically."),
    ("4", "Existing repos: one PR."),
    ("5", "Every engineer who runs Claude Code\ngets your governance on day one."),
]
y = 1.78
for num, step in scale_steps:
    rect(s, 5.1, y, 0.38, 0.38, color=ORANGE)
    txt(s, num, 5.1, y+0.04, 0.38, 0.3,
        size=12, bold=True, color=CREAM, align=PP_ALIGN.CENTER)
    txt(s, step, 5.6, y+0.04, 3.9, 0.5,
        size=12, color=DARK)
    y += 0.52

rect(s, 5.1, 4.52, 4.4, 0.82, color=PALE, border_color=BORDER)
txt(s, "Custom slash commands",
    5.28, 4.58, 4.0, 0.32,
    size=12, bold=True, color=DARK)
txt(s, "Save any prompt as /security-check or /fintech-review.\nEvery engineer runs your team's playbook, not their own.",
    5.28, 4.88, 4.0, 0.4,
    size=11, color=SLATE)


# ─── APPENDIX A5: MCP / INTERNAL TOOLS ───────────────────────────────────────
s = new_slide(bg=DARK)
label(s, "Appendix — MCP / Internal Tools", color=ORANGE)
txt(s, "Claude Code connects to your internal tools.",
    0.5, 0.5, 8.5, 0.62,
    size=26, bold=True, color=CREAM)
txt(s, "One config file per tool. Pre-built servers for the common ones.",
    0.5, 1.08, 7.0, 0.38,
    size=14, color=ORANGE)

rect(s, 0.5, 1.58, 4.4, 3.72, color=CARD)  # was 3.62 — last item detail reached 5.38 > 5.20
txt(s, "What your engineers get:", 0.7, 1.68, 4.0, 0.4,
    size=13, bold=True, color=CREAM)
mcp_capabilities = [
    ("Jira / Linear",
     "Pull ticket context into the session. No copy-paste."),
    ("Confluence / Notion",
     "Read runbooks and architecture docs without leaving the terminal."),
    ("Internal APIs / monitoring",
     "Query your metrics, alert history, service health — in context."),
    ("Custom internal tools",
     "Any HTTP API becomes a tool. One engineer, a few hours, team-wide."),
]
y = 2.18
for tool, detail in mcp_capabilities:
    rect(s, 0.7, y, 0.06, 0.36, color=ORANGE)
    txt(s, tool, 0.88, y, 3.8, 0.36,
        size=12, bold=True, color=ORANGE)
    txt(s, detail, 0.88, y+0.38, 3.82, 0.38,
        size=11, color=MUTED)
    y += 0.70  # was 0.82 — reduced so 4 items fit inside container (bottom 2.18+3*0.70+0.74=5.02 < 5.30)

rect(s, 5.2, 1.58, 4.3, 3.62, color=CARD)
txt(s, "How hard is setup?", 5.4, 1.68, 3.9, 0.4,
    size=13, bold=True, color=CREAM)

rect(s, 5.4, 2.18, 3.9, 1.55, color=RGBColor(0x14, 0x14, 0x14))
code_lines = [
    '# .claude/mcp.json',
    '{',
    '  "jira": {',
    '    "command": "npx",',
    '    "args": ["@mcp/jira"],',
    '    "env": { "JIRA_URL": "..." }',
    '  }',
    '}',
]
cy = 2.25
for line in code_lines:
    txt(s, line, 5.52, cy, 3.65, 0.22,
        size=10, color=RGBColor(0xA8, 0xD8, 0xA8))
    cy += 0.18

txt(s, "Pre-built servers for Jira, GitHub,\nSlack, Confluence, Linear, PagerDuty.",
    5.4, 3.85, 3.9, 0.52,
    size=12, color=MUTED)
txt(s, "Custom APIs: 1 engineer, a few hours,\nrolls out to the whole team.",
    5.4, 4.45, 3.9, 0.52,
    size=12, color=MUTED)

txt(s, '"Can it connect to our systems?" — Yes. Here\'s exactly what that looks like.',
    0.5, 5.3, 9.0, 0.3,
    size=11, color=ORANGE, italic=True)


# ─── APPENDIX A6: WHAT CLAUDE CODE DOESN'T DO ────────────────────────────────
# NEW — honest limitations. Counterintuitive, but most credibility-building slide in the deck.
s = new_slide(bg=CREAM)
label(s, "Appendix — What Claude Code Doesn't Do")
txt(s, "Being honest about this makes everything else more credible.",
    0.5, 0.48, 8.5, 0.62,
    size=22, bold=True, color=DARK)

limitations = [
    ("It doesn't replace senior engineers.",
     "It surfaces options and writes code. Your senior engineers still make architecture decisions, judge tradeoffs, and own the outcome. It makes them faster, not redundant."),
    ("It doesn't eliminate code review.",
     "The code review plugin we showed is Claude reviewing Claude's own work — and still flagging issues. Human review still matters. Claude makes it faster and more thorough."),
    ("It gets things wrong sometimes.",
     "That's why the Safety Gate, governance hooks, and human approval exist. The workflow is designed for a world where the tool is very good but not infallible."),
    ("It doesn't fix a broken engineering culture.",
     "It amplifies what's already there. Teams with good practices get more leverage. Teams with poor practices get faster poor practices. CLAUDE.md helps — it codifies the good practices."),
    ("It won't work well without a test suite.",
     "The governance hook that validates changes — it runs your tests. No tests means no automated safety net. The pilot is a good moment to improve test coverage if needed."),
]

cw = 4.15
cg = 0.2
for i, (headline, body) in enumerate(limitations[:4]):  # was limitations — item 5 was rendered twice (loop + manual below)
    col = i % 2
    row = i // 2
    l = 0.5 + col * (cw + cg)
    t = 1.28 + row * 1.38
    rect(s, l, t, cw, 1.25, border_color=BORDER)
    txt(s, headline, l+0.18, t+0.1, cw-0.36, 0.38,
        size=13, bold=True, color=DARK)
    txt(s, body, l+0.18, t+0.5, cw-0.36, 0.68,
        size=11, color=SLATE)

# 5th item spans full width
rect(s, 0.5, 4.04, 9.0 - 0.0, 0.88, border_color=BORDER)
txt(s, limitations[4][0], 0.7, 4.12, 8.6, 0.36,
    size=13, bold=True, color=DARK)
txt(s, limitations[4][1], 0.7, 4.5, 8.6, 0.36,
    size=11, color=SLATE)



# ─── SAVE ─────────────────────────────────────────────────────────────────────
out = os.path.expanduser("~/Downloads/FinTechCo_Claude_Code_Demo_v2.pptx")
prs.save(out)
print(f"Saved: {out}")
print(f"Slides: {len(prs.slides)}")
slide_names = [
    "Title", "Agenda", "Your World", "The Challenge",
    "What is Claude Code", "Three Teams", "Security Architecture",
    "Demo Transition", "Demo Recap", "ROI Framework", "Evaluation Plan",
    "Pricing", "Close",
    "Appendix Header", "A1: Why Anthropic/Claude", "A2: Competitive",
    "A3: Data & Security", "A4: CLAUDE.md", "A5: MCP", "A6: Limitations",
]
for i, (slide, name) in enumerate(zip(prs.slides, slide_names), 1):
    print(f"  {i:02d}. {name} ({len(slide.shapes)} shapes)")
