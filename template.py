"""You are an expert exam preparation assistant for Indian Banking & Insurance exams (IBPS PO, SBI PO, RBI Grade B, NABARD, Insurance 2026).

I will provide you:
1. A PDF of daily current affairs class (annotated/highlighted by teacher Kapil Kathpal)
2. A transcript of the class video

Your task: Analyze BOTH completely and create a 4-page A4 exam-oriented revision PDF using Python + ReportLab.
═══════════════════════════════════════════════
TECHNICAL SETUP (use exactly):
═══════════════════════════════════════════════
- Library: ReportLab (pip install reportlab --break-system-packages)
- Fonts: NotoSans-Regular.ttf & NotoSans-Bold.ttf from /usr/share/fonts/truetype/noto/
  (run: apt-get install -y fonts-noto fonts-noto-core first)
- Page size: A4 | Margins: 12mm all sides
- Output: /mnt/user-data/outputs/[DATE]_CurrentAffairs_RevisionSheet.pdf

Color palette to use:
  NAVY    = #0D1B2A  |  SAFFRON = #FF6B35  |  GREEN  = #1DB954
  YELLOW  = #FFD700  |  SKY     = #00B4D8  |  PINK   = #FF4D6D
  PURPLE  = #7B2FBE  |  LIGHT_BG= #F0F4FF  |  CARD_BG= #FFFBF0

═══════════════════════════════════════════════
PAGE 1 — REVISION SHEET
═══════════════════════════════════════════════
STRUCTURE:
- TOP: Dark navy title banner: "📚 [DATE] Current Affairs | Revision Sheet by Kapil Kathpal"

KEEP EXACT SAME SECTION HEADINGS AND ORDER AS IN THE PDF:
  🏦 BANKING / RBI CORNER (color: NAVY)
  📰 PIB CORNER (color: dark blue #1A237E)
  🇮🇳 NATIONAL (color: SAFFRON)
  🌾 AGRICULTURE (color: GREEN)
  🌍 INTERNATIONAL (color: SKY)
  🏅 SPORTS (color: GREEN)
  🏆 AWARDS (color: PURPLE)
  ✝️ OBITUARY (color: PINK)
  ⚔️ DEFENCE (color: PINK)
  (Only include sections present in that day's PDF)

FOR EACH NEWS ITEM, create a card with:
  [SECTION TAG] | [Headline/Heading from PDF]
  • Bullet 1 — key fact (bold the most important number/name/term)
  • Bullet 2 — second key fact
  • Bullet 3 — Static GK if mentioned by teacher
  • 😂 Hinglish meme line (fun, relatable, exam motivation)
  🎯 EXAM ALERT box: 3-4 expected MCQ questions with answers

TABLE RULE (for news items only):
  - If a news item has comparative/listed data in the class PDF
    (e.g. CPI trends, rate changes, medal tallies, rankings, scheme amounts)
    AND a table exists or is implied in the PDF for it
    → add a compact color-bordered table inside that news card
  - Table style: section color border | alternate row shading
  - Font size 7-8 | compact | fits within card width
  - Do NOT create tables for simple single-fact news items

RULES for content:
  - Include ALL highlighted/underlined/circled points from PDF
  - Include Static GK tables (capitals, CMs, Governors, established year, HQ, etc.)
  - Bold every number, name, date, percentage, amount
  - Include teacher's emphasis from transcript ("yaad kar lo", "important hai", etc.)
  - Keep relevant data tables (CPI trends, medal counts, award amounts, etc.)

═══════════════════════════════════════════════
PAGE 2 — EXPECTED MCQs (Section-Wise)
═══════════════════════════════════════════════
- Title banner: dark blue "🎯 PAGE 2: EXPECTED MCQs — Section Wise"
- Motivational meme strip below title
- 20-25 MCQs covering ALL sections
- Each MCQ has: section color-tag | Q[N]. question text | (A)-(E) options in 2 columns
- Question style: mix of direct, indirect, statement-based, match-the-following
- Difficulty: 60% easy (direct recall) + 30% moderate + 10% tricky/indirect
- Sections: Banking/Economy | PIB/Schemes | National/State | Defence | International | Sports/Obituary

═══════════════════════════════════════════════
PAGE 3 — ANSWERS & DETAILED SOLUTIONS
═══════════════════════════════════════════════
- Title banner: dark green "✅ PAGE 3: ANSWERS & DETAILED SOLUTIONS"
- Quick Answer Key grid at top (all Q→Answer in a colored grid)
- Then each solution as: [SECTION TAG] | Q[N] → (X) Correct Answer
  Explanation in Kapil Sir Hinglish style — why this is correct, what to remember
- Alternate-row background for readability

═══════════════════════════════════════════════
PAGE 4 — CHEAT SHEET (2-column A4 layout)
═══════════════════════════════════════════════
- Title banner: purple "⚡ PAGE 4: QUICK CHEAT SHEET | Section-Wise"
- Meme strip: "Last minute revision ke liye BEST!"
- Layout: 2 equal columns side by side (each ~(pagewidth-26mm)/2)
- LEFT COLUMN: Banking/Economy box + National box + Agriculture box + Sports box
- RIGHT COLUMN: PIB/Schemes box + International box + Defence/Obituary box + Awards box
- FULL WIDTH (below both columns): Static GK Quick Table

Each section box format:
  [Colored header bar with section name]
  Key → Value rows (font size 7, compact, 40%/60% column split)
  Bordered box with section color

- Bottom: Static GK strip (full width, purple) with all static facts from the day
- Footer on all pages: Telegram @kkathpal | +91 8929496130

═══════════════════════════════════════════════
TONE & STYLE RULES:
═══════════════════════════════════════════════
✅ Hinglish memes — funny but relevant (e.g., "Inflation 4% pe hai, RBI tension free, aur hum bhi!")
✅ Emojis on every section header and meme line
✅ Bold all key terms: names, numbers, dates, percentages, amounts
✅ Include "Kapil Sir tip" in MCQ page meme strip
✅ Closing motivational quote in YELLOW box: "Mehnat karo, revision karo, exam crack karo!"
✅ Keep content DENSE but readable — this is a revision sheet not a textbook
✅ Every page must have the date visible at the top

IMPORTANT NOTES:
- Try to reduce banner sizes if required to make the cheat sheet fit in one page
- Do NOT skip any news item from the PDF
- Do NOT invent facts — only use what's in PDF + transcript
- If teacher says "yaad karna zaroori hai" or circles/boxes something → it goes in EXAM ALERT
- Static GK (Capitals, CMs, Governors, Est. year, HQ, DG/MD names) → always include if mentioned
- ReportLab Table-in-Table approach for colored boxes (no external CSS/HTML)
- Use &#x... HTML entities for emojis in ReportLab Paragraphs
- Build everything as story[] list → doc.build(story)

OUTPUT: Build the PDF exactly as above. Then call build_quiz_html(DATE_STR, MCQs, SOLUTIONS, QUIZ_OUTPUT) —
do NOT rewrite the quiz UI/CSS/JS, it is fixed and reused daily. Present BOTH files
(PDF + Quiz HTML) using present_files. """

#!/usr/bin/env python3
"""16 June 2026 Current Affairs Revision PDF by Kapil Kathpal"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, PageBreak, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
import os

# ── Register Fonts ──────────────────────────────────────────────────────────
FONT_DIR = "/usr/share/fonts/truetype/noto/"
pdfmetrics.registerFont(TTFont("Noto", os.path.join(FONT_DIR, "NotoSans-Regular.ttf")))
pdfmetrics.registerFont(TTFont("NotoBold", os.path.join(FONT_DIR, "NotoSans-Bold.ttf")))


# ── Color Palette ───────────────────────────────────────────────────────────
NAVY     = colors.HexColor("#0D1B2A")
SAFFRON  = colors.HexColor("#FF6B35")
GREEN    = colors.HexColor("#1DB954")
YELLOW   = colors.HexColor("#FFD700")
SKY      = colors.HexColor("#00B4D8")
PINK     = colors.HexColor("#FF4D6D")
PURPLE   = colors.HexColor("#7B2FBE")
LIGHT_BG = colors.HexColor("#F0F4FF")
CARD_BG  = colors.HexColor("#FFFBF0")
DARK_BLUE= colors.HexColor("#1A237E")
WHITE    = colors.white
ORANGE   = colors.HexColor("#FF6B35")
DARK_GREEN=colors.HexColor("#0A6B3A")
import re, json
# ═══════════════════════════════════════════════════════════════
# QUIZ HTML GENERATOR — fixed shell, reused every day (no rewrite)
# ═══════════════════════════════════════════════════════════════

def hexcolor(c):
    """Convert any reportlab Color object to '#RRGGBB' — works for every
    section color already used in MCQs/SOLUTIONS, no manual mapping needed."""
    return '#%02X%02X%02X' % (round(c.red*255), round(c.green*255), round(c.blue*255))

def _strip_letter(opt):
    """'(A) IndiGo (6E-2278)' -> 'IndiGo (6E-2278)'"""
    return re.sub(r'^\([A-Ea-e]\)\s*', '', opt).strip()

def _correct_index(correct_str):
    """'(B) IndiGo (6E-2278)' -> 1"""
    m = re.match(r'\s*\(([A-Ea-e])\)', correct_str)
    return (ord(m.group(1).upper()) - ord('A')) if m else 0

def build_quiz_html(date_str, mcqs, solutions, output_path):
    """Reuses the MCQs + SOLUTIONS lists already built for Page 2/3 of the
    PDF — zero new content is written, only reformatted into JSON and
    dropped into the fixed QUIZ_HTML_TEMPLATE below."""
    sol_by_id = {s[0]: s for s in solutions}
    questions = []
    for q in mcqs:
        qid, text, opts, sec, tag_color = q[0], q[1], q[2], q[3], q[4]
        sol = sol_by_id.get(qid)
        if not sol:
            continue
        questions.append({
            "id": qid, "sec": sec, "color": hexcolor(tag_color),
            "text": text, "opts": [_strip_letter(o) for o in opts],
            "correct": _correct_index(sol[3]), "sol": sol[4],
        })
    html = QUIZ_HTML_TEMPLATE
    html = html.replace("__DATE_LABEL__", date_str)
    html = html.replace("__STORAGE_PREFIX__", re.sub(r'[^A-Za-z0-9]', '', date_str).lower())
    html = html.replace("__QUESTIONS_JSON__", json.dumps(questions, ensure_ascii=False))
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Quiz HTML created: {output_path}")


QUIZ_HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__DATE_LABEL__ Current Affairs — Practice Quiz</title>
<style>
:root{--navy:#0D1B2A;--saffron:#FF6B35;--green:#1DB954;--yellow:#FFD700;--sky:#00B4D8;
--pink:#FF4D6D;--purple:#7B2FBE;--lightbg:#F0F4FF;--cardbg:#FFFBF0;--darkgreen:#0A6B3A;
--ok:#1DB954;--bad:#FF4D6D;--text:#0D1B2A;}
#quizRoot *{box-sizing:border-box;}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;margin:0;background:#fff;color:var(--text);}
#quizRoot{max-width:760px;margin:0 auto;padding:10px 8px 40px;}
.qz-header{background:linear-gradient(120deg,var(--navy) 0%,#132a44 60%,var(--saffron) 130%);color:#fff;
  border-radius:14px;padding:18px 20px;margin-bottom:14px;position:relative;overflow:hidden;}
.qz-eyebrow{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--yellow);font-weight:700;margin-bottom:4px;}
.qz-title{font-size:19px;font-weight:800;margin:0;}
.qz-tabs{display:flex;gap:8px;margin-bottom:10px;}
.qz-tab{flex:1;text-align:center;padding:9px 6px;border-radius:10px;font-weight:700;font-size:13px;
  cursor:pointer;border:2px solid var(--navy);background:#fff;color:var(--navy);}
.qz-tab.active{background:var(--navy);color:#fff;}
.mode-switch{display:flex;gap:8px;margin-bottom:14px;background:var(--lightbg);padding:5px;border-radius:12px;}
.mode-btn{flex:1;text-align:center;padding:10px 8px;border-radius:9px;font-weight:700;font-size:12.5px;
  cursor:pointer;border:none;background:transparent;color:var(--navy);}
.mode-btn .mm-sub{display:block;font-weight:500;font-size:10.5px;opacity:.75;margin-top:1px;}
.mode-btn.active{background:#fff;box-shadow:0 2px 6px rgba(13,27,42,.18);}
.mode-btn.active.mock{color:var(--pink);} .mode-btn.active.practice{color:var(--darkgreen);}
.mode-tag{display:inline-block;font-size:10px;font-weight:800;padding:2px 8px;border-radius:20px;margin-left:6px;}
.mode-tag.practice{background:#e8f9ee;color:var(--darkgreen);} .mode-tag.mock{background:#ffeef3;color:var(--pink);}
.qz-progress-wrap{background:var(--lightbg);border-radius:10px;padding:10px 14px;margin-bottom:12px;
  display:flex;align-items:center;gap:10px;font-size:12.5px;font-weight:700;color:var(--navy);flex-wrap:wrap;}
.qz-progress-bar{flex:1;min-width:80px;height:8px;border-radius:5px;background:#dfe6ff;overflow:hidden;}
.qz-progress-fill{height:100%;background:linear-gradient(90deg,var(--sky),var(--green));border-radius:5px;}
.qz-score-pill{background:var(--yellow);color:var(--navy);padding:2px 9px;border-radius:20px;font-size:11.5px;}
.qcard{background:var(--cardbg);border-radius:12px;margin-bottom:10px;overflow:hidden;
  border:1.4px solid var(--tagcolor,var(--navy));}
.qcard-hdr{display:flex;}
.qtag{background:var(--tagcolor,var(--navy));color:#fff;font-size:10px;font-weight:800;padding:9px 8px;white-space:nowrap;}
.qtext{background:var(--lightbg);flex:1;padding:9px 12px;font-size:13px;font-weight:700;color:var(--navy);}
.opts{padding:10px 12px 4px;display:grid;grid-template-columns:1fr 1fr;gap:6px 10px;}
@media(max-width:480px){.opts{grid-template-columns:1fr;}}
.opt{display:flex;align-items:center;gap:8px;padding:7px 9px;border-radius:8px;border:1.5px solid #e2e2e2;
  background:#fff;cursor:pointer;font-size:13px;}
.opt input{accent-color:var(--tagcolor,var(--navy));}
.opt.correct{background:#e8f9ee;border-color:var(--ok);font-weight:700;color:#0A6B3A;}
.opt.wrong{background:#ffeef0;border-color:var(--bad);font-weight:700;color:#a3123a;}
.qactions{padding:8px 12px 12px;display:flex;gap:8px;flex-wrap:wrap;}
.btn{border:none;border-radius:8px;padding:8px 14px;font-size:12.5px;font-weight:700;cursor:pointer;}
.btn-primary{background:var(--tagcolor,var(--navy));color:#fff;}
.btn-primary:disabled{background:#c9c9c9;}
.btn-ghost{background:#fff;color:var(--tagcolor,var(--navy));border:1.5px solid var(--tagcolor,var(--navy));}
.result-banner{margin:0 12px 12px;padding:8px 10px;border-radius:8px;font-size:12.5px;font-weight:700;}
.result-banner.ok{background:#e8f9ee;color:#0A6B3A;} .result-banner.bad{background:#ffeef0;color:#a3123a;}
.solution{margin:0 12px 12px;background:#FFF8E1;border-left:4px solid var(--saffron);border-radius:6px;
  padding:8px 10px;font-size:12.3px;line-height:1.5;color:var(--navy);}
.submit-bar{position:sticky;bottom:0;background:#fff;padding:12px 0;border-top:2px solid var(--lightbg);
  display:flex;gap:10px;justify-content:center;flex-wrap:wrap;}
.submit-btn{background:var(--darkgreen);color:#fff;} .reset-btn{background:#fff;color:var(--navy);border:1.5px solid var(--navy);}
.score-summary{background:linear-gradient(120deg,var(--purple),#1A237E);color:#fff;border-radius:14px;
  padding:18px;text-align:center;margin-bottom:14px;}
.score-summary .big{font-size:32px;font-weight:800;}
.hist-card{background:#fff;border:1.5px solid var(--lightbg);border-radius:12px;margin-bottom:10px;overflow:hidden;}
.hist-hdr{display:flex;justify-content:space-between;align-items:center;padding:12px 14px;cursor:pointer;background:var(--lightbg);}
.hist-date{font-size:12.5px;font-weight:700;color:var(--navy);}
.hist-score{font-size:13px;font-weight:800;color:var(--darkgreen);}
.hist-body{padding:8px 14px 14px;display:none;} .hist-body.open{display:block;}
.hist-q{border-bottom:1px dashed #e0e0e0;padding:9px 0;font-size:12.5px;}
.hist-q .qline{font-weight:700;color:var(--navy);margin-bottom:3px;}
.hist-q .yourans{color:var(--bad);} .hist-q .yourans.ok{color:var(--darkgreen);} .hist-q .correctans{color:var(--darkgreen);}
.hist-q .hsol{background:#FFF8E1;border-left:3px solid var(--saffron);padding:6px 8px;border-radius:5px;margin-top:4px;font-size:12px;}
.empty-hist{text-align:center;color:#888;font-size:13px;padding:30px 10px;}
.del-btn{background:none;border:none;color:#a3123a;font-size:11px;cursor:pointer;text-decoration:underline;}
.footer-note{text-align:center;font-size:11px;color:#999;margin-top:16px;}
</style></head>
<body>
<div id="quizRoot">
  <div class="qz-header">
    <div class="qz-eyebrow">Kapil Kathpal · LearningNiti</div>
    <div class="qz-title">🎯 __DATE_LABEL__ Current Affairs — Practice Quiz</div>
  </div>
  <div class="qz-tabs">
    <div class="qz-tab active" id="tabQuiz" onclick="showView('quiz')">📝 Quiz</div>
    <div class="qz-tab" id="tabHistory" onclick="showView('history')">📊 Past Attempts</div>
  </div>
  <div class="mode-switch">
    <button class="mode-btn practice active" id="modeBtnPractice" onclick="setMode('practice')">🎯 Practice Mode
      <span class="mm-sub">Instant answer &amp; solution per question</span></button>
    <button class="mode-btn mock" id="modeBtnMock" onclick="setMode('mock')">🧪 Mock Mode
      <span class="mm-sub">Revealed only after submit</span></button>
  </div>
  <div id="viewQuiz"></div>
  <div id="viewHistory" style="display:none;"></div>
</div>
<script>
const QUESTIONS = __QUESTIONS_JSON__;
const STORAGE_PREFIX = "attempt:__STORAGE_PREFIX__:";
const LS_PREFIX = "quiz__STORAGE_PREFIX__:";
const hasCloud = (typeof window!=='undefined') && window.storage && typeof window.storage.set==='function';
async function sSet(k,v){ if(hasCloud){try{const r=await window.storage.set(k,v,false); if(r) return r;}catch(e){}}
  try{localStorage.setItem(LS_PREFIX+k,v); return {key:k,value:v};}catch(e){return null;} }
async function sGet(k){ if(hasCloud){try{const r=await window.storage.get(k,false); if(r) return r;}catch(e){}}
  try{const v=localStorage.getItem(LS_PREFIX+k); return v===null?null:{key:k,value:v};}catch(e){return null;} }
async function sDelete(k){ if(hasCloud){try{await window.storage.delete(k,false);}catch(e){}}
  try{localStorage.removeItem(LS_PREFIX+k);}catch(e){} }
async function sList(p){ let keys=[]; if(hasCloud){try{const r=await window.storage.list(p,false); if(r&&r.keys) keys=keys.concat(r.keys);}catch(e){}}
  try{ for(let i=0;i<localStorage.length;i++){ const k=localStorage.key(i);
    if(k && k.indexOf(LS_PREFIX+p)===0){ const rk=k.substring(LS_PREFIX.length); if(keys.indexOf(rk)===-1) keys.push(rk); } } }catch(e){}
  return keys; }

let currentMode='practice', mockSubmitted=false, state={};
QUESTIONS.forEach(q=>state[q.id]={selected:null, checked:false});
function letters(i){return String.fromCharCode(65+i);}
function setMode(m){ if(m===currentMode) return; currentMode=m; mockSubmitted=false;
  QUESTIONS.forEach(q=>state[q.id]={selected:null,checked:false});
  document.getElementById('modeBtnPractice').classList.toggle('active', m==='practice');
  document.getElementById('modeBtnMock').classList.toggle('active', m==='mock'); renderQuiz(); }

function renderQuiz(){
  const isMock = currentMode==='mock', revealAll = isMock?mockSubmitted:false;
  const answered = isMock ? QUESTIONS.filter(q=>state[q.id].selected!==null).length
                           : QUESTIONS.filter(q=>state[q.id].checked).length;
  const correctCount = isMock ? (mockSubmitted?QUESTIONS.filter(q=>state[q.id].selected===q.correct).length:0)
                               : QUESTIONS.filter(q=>state[q.id].checked && state[q.id].selected===q.correct).length;
  let html = `<div class="qz-progress-wrap"><span>Progress <span class="mode-tag ${currentMode}">${isMock?'MOCK':'PRACTICE'}</span></span>
    <div class="qz-progress-bar"><div class="qz-progress-fill" style="width:${(answered/QUESTIONS.length*100).toFixed(0)}%"></div></div>
    <span>${answered}/${QUESTIONS.length}</span>
    ${(!isMock&&answered>0)||(isMock&&mockSubmitted)?`<span class="qz-score-pill">✅ ${correctCount}/${isMock?QUESTIONS.length:answered}</span>`:''}</div>`;
  QUESTIONS.forEach(q=>{
    const st=state[q.id], color=q.color||'#0D1B2A', showResult=isMock?revealAll:st.checked, locked=showResult;
    html += `<div class="qcard" style="--tagcolor:${color}"><div class="qcard-hdr">
      <div class="qtag">${q.sec}</div><div class="qtext">Q${q.id}. ${q.text}</div></div><div class="opts">`;
    q.opts.forEach((opt,i)=>{ let cls="opt";
      if(locked){ cls+=" disabled"; if(showResult){ if(i===q.correct) cls+=" correct"; else if(i===st.selected) cls+=" wrong"; } }
      html += `<label class="${cls}" onclick="${locked?'':`selectOpt(${q.id},${i})`}">
        <input type="radio" name="q${q.id}" ${st.selected===i?'checked':''} ${locked?'disabled':''}>
        <span><b>${letters(i)})</b> ${opt}</span></label>`; });
    html += `</div><div class="qactions">`;
    if(!isMock){ if(!st.checked){ html += `<button class="btn btn-primary" style="--tagcolor:${color}" ${st.selected===null?'disabled':''} onclick="checkAnswer(${q.id})">Check Answer</button>`; }
      else { html += `<button class="btn btn-ghost" style="--tagcolor:${color}" onclick="resetQuestion(${q.id})">🔄 Reattempt this question</button>`; } }
    html += `</div>`;
    if(showResult){ const attempted=st.selected!==null, isOk=attempted&&st.selected===q.correct;
      html += `<div class="result-banner ${isOk?'ok':'bad'}">${!attempted?'⚪ Not attempted — correct answer is '+letters(q.correct)+') '+q.opts[q.correct]
        : isOk?'✅ Correct!':`❌ Incorrect — correct answer is ${letters(q.correct)}) ${q.opts[q.correct]}`}</div>
      <div class="solution"><b>Solution:</b> ${q.sol}</div>`; }
    html += `</div>`; });
  if(!isMock){ html += `<div class="submit-bar"><button class="btn submit-btn" onclick="submitQuiz()">📤 Submit Whole Quiz</button>
    <button class="btn reset-btn" onclick="resetQuiz()">🔄 Reattempt Whole Quiz</button></div>`; }
  else if(!mockSubmitted){ html += `<div class="submit-bar"><button class="btn submit-btn" onclick="submitQuiz()">📤 Submit Mock Test &amp; Reveal Answers</button>
    <button class="btn reset-btn" onclick="resetQuiz()">🔄 Clear All Selections</button></div>`; }
  else { html += `<div class="submit-bar"><button class="btn reset-btn" onclick="resetQuiz()">🔄 Reattempt Whole Mock Test</button></div>`; }
  html += `<p class="footer-note">🌟 Mehnat karo, revision karo, exam crack karo! — Kapil Sir</p>`;
  document.getElementById('viewQuiz').innerHTML = html;
}
function selectOpt(id,i){ state[id].selected=i; renderQuiz(); }
function checkAnswer(id){ state[id].checked=true; renderQuiz(); }
function resetQuestion(id){ state[id]={selected:null,checked:false}; renderQuiz(); }
function resetQuiz(){ QUESTIONS.forEach(q=>state[q.id]={selected:null,checked:false}); mockSubmitted=false; renderQuiz(); }

async function submitQuiz(){
  const isMock = currentMode==='mock';
  if(isMock){ QUESTIONS.forEach(q=>state[q.id].checked=true); mockSubmitted=true; }
  const details = QUESTIONS.map(q=>{ const st=state[q.id], attempted=st.selected!==null, isCorrect=attempted&&st.selected===q.correct;
    return {id:q.id,sec:q.sec,text:q.text,opts:q.opts,selected:st.selected,correct:q.correct,sol:q.sol,isCorrect,attempted}; });
  const score = details.filter(d=>d.isCorrect).length, attempted = details.filter(d=>d.attempted).length;
  const attempt = {timestamp:new Date().toISOString(), mode:currentMode, score, total:QUESTIONS.length, attempted, details};
  await sSet(STORAGE_PREFIX+Date.now(), JSON.stringify(attempt));
  if(isMock) renderQuiz();
  showView('history'); await loadHistory();
  document.getElementById('viewHistory').insertAdjacentHTML('afterbegin', `<div class="score-summary">
    <div>${isMock?'Mock Test':'Practice Quiz'} Submitted <span class="mode-tag ${currentMode}">${isMock?'MOCK':'PRACTICE'}</span></div>
    <div class="big">${score} / ${QUESTIONS.length}</div>
    <div>${attempted<QUESTIONS.length?`${QUESTIONS.length-attempted} left unanswered — marked incorrect`:'All questions attempted'}</div></div>`);
}
function showView(v){ document.getElementById('viewQuiz').style.display=v==='quiz'?'block':'none';
  document.getElementById('viewHistory').style.display=v==='history'?'block':'none';
  document.getElementById('tabQuiz').classList.toggle('active', v==='quiz');
  document.getElementById('tabHistory').classList.toggle('active', v==='history');
  if(v==='history') loadHistory(); }
function toggleHist(i){ document.getElementById('hbody-'+i).classList.toggle('open'); }
async function deleteAttempt(key){ await sDelete(key); loadHistory(); }
async function loadHistory(){
  const c=document.getElementById('viewHistory'); c.innerHTML='<div class="empty-hist">Loading…</div>';
  const keys=await sList(STORAGE_PREFIX);
  if(keys.length===0){ c.innerHTML='<div class="empty-hist">📭 No quiz attempts yet.</div>'; return; }
  keys.sort().reverse(); const attempts=[];
  for(const k of keys){ const r=await sGet(k); if(r&&r.value){ try{ attempts.push({key:k,data:JSON.parse(r.value)}); }catch(e){} } }
  let html='';
  attempts.forEach((a,idx)=>{ const d=a.data, dt=new Date(d.timestamp);
    const dtStr=dt.toLocaleString('en-IN',{day:'2-digit',month:'short',year:'numeric',hour:'2-digit',minute:'2-digit'});
    const modeTag = d.mode==='mock' ? '<span class="mode-tag mock">MOCK</span>' : '<span class="mode-tag practice">PRACTICE</span>';
    html += `<div class="hist-card"><div class="hist-hdr" onclick="toggleHist(${idx})">
      <div><div class="hist-date">🗓️ ${dtStr} ${modeTag}</div><div style="font-size:11px;color:#777;">${d.attempted}/${d.total} attempted</div></div>
      <div style="text-align:right;"><div class="hist-score">${d.score} / ${d.total}</div>
      <button class="del-btn" onclick="event.stopPropagation(); deleteAttempt('${a.key}')">delete</button></div></div>
      <div class="hist-body" id="hbody-${idx}">`;
    d.details.forEach(q=>{ const okClass=q.attempted?(q.isCorrect?'ok':''):''; const yourAns=q.attempted?`${letters(q.selected)}) ${q.opts[q.selected]}`:'Not attempted';
      html += `<div class="hist-q"><div class="qline">Q${q.id}. [${q.sec}] ${q.text}</div>
        <div>Your answer: <span class="yourans ${okClass}">${yourAns}</span></div>
        <div>Correct answer: <span class="correctans">${letters(q.correct)}) ${q.opts[q.correct]}</span></div>
        <div class="hsol"><b>Solution:</b> ${q.sol}</div></div>`; });
    html += `</div></div>`; });
  c.innerHTML = html;
}
renderQuiz();
</script>
</body></html>"""



W, H = A4
M = 12*mm
CW = W - 2*M   # content width

DATE_STR = "16 June 2026"

OUTPUT = "/mnt/user-data/outputs/16June2026_CurrentAffairs_RevisionSheet.pdf"

# ── Base Styles ──────────────────────────────────────────────────────────────
def S(name, font="Noto", size=8, color=colors.black, align=TA_LEFT,
      bold=False, leading=None, space_before=0, space_after=2):
    return ParagraphStyle(
        name, fontName="NotoBold" if bold else font,
        fontSize=size, textColor=color, alignment=align,
        leading=leading or size*1.35,
        spaceBefore=space_before, spaceAfter=space_after)

# Shared styles
s_normal  = S("normal", size=8)
s_bold8   = S("bold8",  size=8,  bold=True)
s_bold9   = S("bold9",  size=9,  bold=True)
s_bold10  = S("bold10", size=10, bold=True)
s_white9  = S("white9", size=9,  bold=True, color=WHITE, align=TA_CENTER)
s_white8  = S("white8", size=8,  bold=True, color=WHITE, align=TA_CENTER)
s_center8 = S("center8", size=8, align=TA_CENTER)
s_meme    = S("meme", size=8, color=PURPLE, bold=True)
s_exam    = S("exam", size=8, color=NAVY, bold=True)
s_ans     = S("ans", size=8, color=DARK_GREEN, bold=True)

def bold(txt):
    return f'<font name="NotoBold">{txt}</font>'

def col(txt, c):
    hex_c = c.hexval() if hasattr(c,'hexval') else "#{:06x}".format(int(c.hexval()[2:],16) if hasattr(c,'hexval') else 0)
    return f'<font color="{c}">{txt}</font>'

# ── Helper: header banner ────────────────────────────────────────────────────
def banner(text, bg, text_color=WHITE, font_size=11):
    p = Paragraph(text, ParagraphStyle("bann", fontName="NotoBold",
        fontSize=font_size, textColor=text_color, alignment=TA_CENTER,
        leading=font_size*1.4))
    t = Table([[p]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("TOPPADDING",   (0,0), (-1,-1), 5),
        ("BOTTOMPADDING",(0,0), (-1,-1), 5),
        ("LEFTPADDING",  (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    return t


# ── Helper: section header ────────────────────────────────────────────────────
def sec_hdr(icon_text, bg):
    p = Paragraph(icon_text, ParagraphStyle("sh", fontName="NotoBold",
        fontSize=9.5, textColor=WHITE, alignment=TA_LEFT, leading=13))
    t = Table([[p]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("TOPPADDING",   (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0), (-1,-1), 4),
        ("LEFTPADDING",  (0,0), (-1,-1), 8),
    ]))
    return t

# ── Helper: news card ────────────────────────────────────────────────────────
def news_card(section_tag, headline, bullets, meme, exam_qs, tag_color=NAVY):
    content = []

    # Tag + headline row
    tag_p = Paragraph(f'<font name="NotoBold" color="white"> {section_tag} </font>',
        ParagraphStyle("tag", fontName="NotoBold", fontSize=7.5,
            textColor=WHITE, alignment=TA_CENTER,
            backColor=tag_color, leading=11))
    hl_p = Paragraph(f'<font name="NotoBold">{headline}</font>',
        ParagraphStyle("hl", fontName="NotoBold", fontSize=8.5,
            textColor=NAVY, leading=12))
    hdr_tbl = Table([[tag_p, hl_p]],
        colWidths=[28*mm, CW-30*mm])
    hdr_tbl.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("BACKGROUND", (0,0), (0,0), tag_color),
        ("BACKGROUND", (1,0), (1,0), LIGHT_BG),
        ("TOPPADDING",   (0,0), (-1,-1), 3),
        ("BOTTOMPADDING",(0,0), (-1,-1), 3),
        ("LEFTPADDING",  (0,0), (-1,-1), 4),
        ("RIGHTPADDING", (0,0), (-1,-1), 4),
    ]))
    content.append(hdr_tbl)

    # Bullets
    for b in bullets:
        content.append(Paragraph(f"&#8226; {b}", ParagraphStyle("bul",
            fontName="Noto", fontSize=8, textColor=colors.black,
            leading=11, leftIndent=8, spaceAfter=1)))

    # Meme
    content.append(Paragraph(f"&#128514; {meme}", ParagraphStyle("mm",
        fontName="NotoBold", fontSize=7.5, textColor=PURPLE,
        leading=11, leftIndent=8, spaceAfter=2)))

    # Exam Alert box
    ea_rows = [[ Paragraph("&#127919; EXAM ALERT",
        ParagraphStyle("ea_hdr", fontName="NotoBold", fontSize=8,
            textColor=WHITE, leading=11)) ]]
    for eq in exam_qs:
        ea_rows.append([Paragraph(eq, ParagraphStyle("eq",
            fontName="Noto", fontSize=7.5, textColor=NAVY, leading=11))])
    ea_tbl = Table(ea_rows, colWidths=[CW-4*mm])
    ea_style = [
        ("BACKGROUND", (0,0), (0,0), SAFFRON),
        ("BACKGROUND", (0,1), (0,-1), colors.HexColor("#FFF8E1")),
        ("TOPPADDING",   (0,0), (-1,-1), 2),
        ("BOTTOMPADDING",(0,0), (-1,-1), 2),
        ("LEFTPADDING",  (0,0), (-1,-1), 6),
        ("BOX", (0,0), (-1,-1), 0.5, SAFFRON),
    ]
    ea_tbl.setStyle(TableStyle(ea_style))

    # Wrap in card
    card_rows = [[c] for c in content] + [[ea_tbl]]
    card = Table(card_rows, colWidths=[CW])
    card.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), CARD_BG),
        ("BOX",        (0,0), (-1,-1), 0.8, tag_color),
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 2),
        ("LEFTPADDING",  (0,0), (-1,-1), 2),
        ("RIGHTPADDING", (0,0), (-1,-1), 2),
    ]))
    return card

# ── Helper: inline data table inside a news card ────────────────────────────
def news_table(headers, rows, border_color=NAVY):
    """
    Use this when a news item has comparative/listed data that exists as a
    table in the class PDF (e.g. CPI trends, rate changes, medal tallies,
    rankings, scheme amounts). Do NOT use for simple single-fact news items.

    headers : list of column header strings  e.g. ["Category", "Rate", "Change"]
    rows    : list of lists                  e.g. [["CPI Food", "3.2%", "-0.4%"], ...]
    border_color : section color (NAVY, GREEN, SKY etc.)
    """
    col_count = len(headers)
    col_w = (CW - 6*mm) / col_count

    def cell(txt, is_hdr=False):
        return Paragraph(txt, ParagraphStyle(
            "ntc", fontName="NotoBold" if is_hdr else "Noto",
            fontSize=7, textColor=WHITE if is_hdr else NAVY,
            alignment=TA_CENTER, leading=9))

    tbl_data = [[cell(h, is_hdr=True) for h in headers]]
    for row in rows:
        tbl_data.append([cell(str(v)) for v in row])

    t = Table(tbl_data, colWidths=[col_w] * col_count)
    style = [
        ("BACKGROUND",    (0, 0), (-1,  0), border_color),
        ("BOX",           (0, 0), (-1, -1), 0.6, border_color),
        ("GRID",          (0, 0), (-1, -1), 0.3, colors.HexColor("#CCCCCC")),
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LEFTPADDING",   (0, 0), (-1, -1), 4),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]
    for i in range(1, len(tbl_data)):
        bg = colors.HexColor("#F0F4FF") if i % 2 == 1 else colors.HexColor("#FFFBF0")
        style.append(("BACKGROUND", (0, i), (-1, i), bg))
    t.setStyle(TableStyle(style))
    return t

# ── Helper: MCQ option table ─────────────────────────────────────────────────
def mcq_block(num, q_text, opts, tag, tag_color):
    tag_p = Paragraph(f'<font name="NotoBold" color="white"> {tag} </font>',
        ParagraphStyle("t2", fontName="NotoBold", fontSize=7,
            textColor=WHITE, alignment=TA_CENTER, leading=10))
    q_p = Paragraph(f'<font name="NotoBold">Q{num}.</font> {q_text}',
        ParagraphStyle("qp", fontName="Noto", fontSize=8,
            textColor=NAVY, leading=11))
    hdr = Table([[tag_p, q_p]], colWidths=[22*mm, CW-24*mm])
    hdr.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,0), tag_color),
        ("BACKGROUND", (1,0), (1,0), LIGHT_BG),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",   (0,0), (-1,-1), 3),
        ("BOTTOMPADDING",(0,0), (-1,-1), 3),
        ("LEFTPADDING",  (0,0), (-1,-1), 3),
    ]))
    # Options in 2 cols
    half = len(opts)//2 + len(opts)%2
    left_opts  = opts[:half]
    right_opts = opts[half:]
    opt_rows = []
    for i in range(half):
        lo = left_opts[i] if i < len(left_opts) else ""
        ro = right_opts[i] if i < len(right_opts) else ""
        lp = Paragraph(lo, ParagraphStyle("op", fontName="Noto", fontSize=7.5, leading=10))
        rp = Paragraph(ro, ParagraphStyle("op2", fontName="Noto", fontSize=7.5, leading=10))
        opt_rows.append([lp, rp])
    opt_tbl = Table(opt_rows, colWidths=[CW/2, CW/2])
    opt_tbl.setStyle(TableStyle([
        ("TOPPADDING",   (0,0), (-1,-1), 1),
        ("BOTTOMPADDING",(0,0), (-1,-1), 1),
        ("LEFTPADDING",  (0,0), (-1,-1), 10),
    ]))
    rows = [[hdr], [opt_tbl]]
    card = Table(rows, colWidths=[CW])
    card.setStyle(TableStyle([
        ("BOX", (0,0), (-1,-1), 0.5, tag_color),
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#FAFAFA")),
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 1),
        ("LEFTPADDING",  (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ]))
    return card

# ── Helper: solution block ───────────────────────────────────────────────────
def sol_block(num, tag, tag_color, correct, explanation, is_alt=False):
    bg = colors.HexColor("#F0FFF4") if not is_alt else colors.HexColor("#FFF8F0")
    tag_p = Paragraph(f'<font name="NotoBold" color="white"> {tag} </font>',
        ParagraphStyle("st", fontName="NotoBold", fontSize=7,
            textColor=WHITE, alignment=TA_CENTER, leading=10))
    ans_p = Paragraph(f'<font name="NotoBold">Q{num} &#8594; {correct}</font>',
        ParagraphStyle("ap", fontName="NotoBold", fontSize=8,
            textColor=DARK_GREEN, leading=11))
    exp_p = Paragraph(explanation,
        ParagraphStyle("ep", fontName="Noto", fontSize=7.5,
            textColor=colors.black, leading=10))
    hdr = Table([[tag_p, ans_p]], colWidths=[22*mm, CW-24*mm])
    hdr.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,0), tag_color),
        ("BACKGROUND", (1,0), (1,0), bg),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",   (0,0), (-1,-1), 3),
        ("BOTTOMPADDING",(0,0), (-1,-1), 3),
        ("LEFTPADDING",  (0,0), (-1,-1), 3),
    ]))
    exp_row = Table([[exp_p]], colWidths=[CW])
    exp_row.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("LEFTPADDING",  (0,0), (-1,-1), 8),
        ("TOPPADDING",   (0,0), (-1,-1), 1),
        ("BOTTOMPADDING",(0,0), (-1,-1), 2),
    ]))
    card = Table([[hdr], [exp_row]], colWidths=[CW])
    card.setStyle(TableStyle([
        ("BOX", (0,0), (-1,-1), 0.5, tag_color),
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 0),
        ("LEFTPADDING",  (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ]))
    return card

# ── Helper: footer (drawn on each page via canvas) ───────────────────────────
def footer_canvas(canvas, doc):
    canvas.saveState()
    canvas.setFont("NotoBold", 7)
    canvas.setFillColor(NAVY)
    canvas.drawString(M, 8*mm,
        "Telegram: @kkathpal  |  WhatsApp: +91 8929496130  |  www.learningniti.com")
    canvas.drawRightString(W - M, 8*mm, f"Page {doc.page}  |  {DATE_STR}")
    canvas.restoreState()

# ════════════════════════════════════════════════════════════════════════════
# BUILD STORY
# ════════════════════════════════════════════════════════════════════════════
story = []

sp = lambda h=4: Spacer(1, h)

# ╔══════════════════════════════════════════════════════════════╗
# ║  PAGE 1 — REVISION SHEET                                    ║
# ╚══════════════════════════════════════════════════════════════╝

story.append(banner(f"&#128218; {DATE_STR} Current Affairs | Revision Sheet by Kapil Kathpal", NAVY, font_size=9))
story.append(sp(3))

# ── NATIONAL ──────────────────────────────────────────────────
story.append(sec_hdr("&#127470;&#127475; NATIONAL", SAFFRON))
story.append(sp(3))

story.append(news_card(
    "NATIONAL",
    "Noida International Airport (Jewar) Begins Commercial Flights",
    [
        f"First commercial flight: {bold('IndiGo 6E-2278')} from Lucknow's Chaudhary Charan Singh Airport landed at {bold('7:55 AM')}, departed for {bold('Bengaluru')} at 8:35 AM.",
        f"First passengers: {bold('170 farmers')} (incl. 20 women) who gave land — met CM {bold('Yogi Adityanath')} in Lucknow.",
        f"Phase 1 routes: {bold('Lucknow, Bengaluru, Hyderabad, Amritsar')}. Phase 2 (16 June): {bold('Navi Mumbai & Jammu')}. Full network by {bold('1 July')}: 16-17 cities, 11 states.",
        f"Static GK: Airport also called {bold('Jewar Airport')} | Runway: {bold('3,900 metres')} | IATA planning code: DXN | Operator: {bold('Yamuna International Airport Pvt Ltd')}.",
    ],
    "Jewar airport ne udaan bhari, ab hum bhi bolunte hain - 'Madam, window seat milega?'",
    [
        "Q: Which airline operated the FIRST commercial flight at Noida International Airport? Ans: (B) IndiGo (6E-2278)",
        "Q: What is the runway length of Jewar Airport? Ans: (C) 3,900 metres",
        "Q: How many farmers were the first symbolic passengers? Ans: (D) 170",
        "Q: By when will Jewar Airport connect 16-17 cities? Ans: (A) July 1, 2026",
    ],
    tag_color=SAFFRON
))
story.append(sp(4))

story.append(news_card(
    "NATIONAL",
    "19th MIFF to Host AI Cinema Hackathon 'Mumbai Through a Thousand Eyes' — First Time",
    [
        f"The {bold('19th Mumbai International Film Festival (MIFF 2026)')} is hosting an {bold('AI Cinema Hackathon')} titled 'Mumbai Through a Thousand Eyes' — first ever.",
        f"Format: {bold('48-hour')} global filmmaking challenge; {bold('346 films')} from {bold('46 nations')} showcased.",
        f"Awards: {bold('18 awards')}, total prize money {bold('Rs 45 lakh')}. {bold('V Shantaram Lifetime Achievement Award')} to be given.",
        f"Special tribute to {bold('David Attenborough')}. Festival dates: June 15-21, 2026.",
    ],
    "AI se short film banao, award pao — abhi tak humne sirf reels banaye the!",
    [
        "Q: Which edition of MIFF 2026 is hosting the AI Hackathon for the first time? Ans: (B) 19th",
        "Q: What is the hackathon's duration? Ans: (C) 48 hours",
        "Q: Total prize money at MIFF 2026? Ans: (D) Rs 45 lakh",
        "Q: Which lifetime achievement award is given at MIFF? Ans: (A) V Shantaram Award",
    ],
    tag_color=SAFFRON
))
story.append(sp(4))

story.append(news_card(
    "NATIONAL",
    "Jagannath Temple Secures Trademarks for Nilachakra & 2 Key Terms",
    [
        f"{bold('Shree Jagannath Temple Administration (SJTA)')}, Puri, Odisha — first Indian shrine to register trademarks under the {bold('Trade Marks Act')}.",
        f"3 trademarks: (1) {bold('Nilachakra Logo')} — sacred 8-spoked disc atop temple spire; (2) {bold('Ananda Bajara')} — Mahaprasad dining area; (3) {bold('Patitapabana')} — form of Lord Jagannath near Singhadwara (Lion Gate).",
        f"Static GK: GI Registry HQ: {bold('Chennai')} | Under: Office of CGPDTM | Ministry: {bold('Commerce & Industry')} | GI Act: {bold('1999')} (active Sept 2003) | Validity: {bold('10 years')}.",
        f"Trademark governed by: {bold('Trade Marks Act, 1999')} | CGPDTM under Ministry of Commerce.",
    ],
    "Nilachakra ka trademark le liya — ab Puri ki copy koi nahi karega bhai!",
    [
        "Q: Which temple secured trademark for 'Nilachakra' logo in 2026? Ans: (B) Jagannath Temple, Puri",
        "Q: 'Ananda Bajara' trademark refers to? Ans: (C) Mahaprasad dining area",
        "Q: GI Registry is headquartered in? Ans: (A) Chennai",
        "Q: GI tag validity period? Ans: (D) 10 years",
    ],
    tag_color=SAFFRON
))
story.append(sp(4))

# ── AGRICULTURE / ENVIRONMENT ──────────────────────────────────
story.append(sec_hdr("&#127807; AGRICULTURE / ENVIRONMENT", GREEN))
story.append(sp(3))

story.append(news_card(
    "AGRI/ENV",
    "Project GIB Adds 3 Chicks — Total Captive Stock Reaches 94 Birds",
    [
        f"{bold('Project Great Indian Bustard (GIB)')}: 3 new chicks added; total captive stock now {bold('94 birds')}.",
        f"As of June 14, 2026: {bold('26 chicks')} hatched in 4th year of captive breeding. Wild population: fewer than {bold('150 individuals')}, mainly in {bold('Rajasthan Thar Desert')}.",
        f"Joint effort: {bold('MoEFCC + Rajasthan Forest Dept + Wildlife Institute of India (WII)')}.",
        f"Static GK: GIB = {bold('Godawan')} (local name) | Official State Bird of {bold('Rajasthan')} since {bold('1981')} | Status: {bold('Critically Endangered')}.",
    ],
    "94 birds captive mein hain — GIB bhi bol raha hai 'Hum bachenge, exam mein aayenge!'",
    [
        "Q: Great Indian Bustard is state bird of which state? Ans: (B) Rajasthan",
        "Q: Local name of GIB? Ans: (C) Godawan",
        "Q: Year GIB designated as Rajasthan's state bird? Ans: (A) 1981",
        "Q: Total captive GIB stock as of June 2026? Ans: (D) 94",
    ],
    tag_color=GREEN
))
story.append(sp(4))

story.append(news_card(
    "AGRI/ENV",
    "NBA Reconstitutes Expert Committee on Agrobiodiversity",
    [
        f"{bold('National Biodiversity Authority (NBA)')} reconstituted Expert Committee on Agrobiodiversity under {bold('Section 13(1) of Biological Diversity Act, 2002')}.",
        f"Chaired by {bold('Padma Shri Dr. P.L. Gautam')} for {bold('1 year')}. Includes experts from Ministry of Agriculture, ICAR, National Genetic Resource Bureaus.",
        f"Static GK: NBA est. {bold('2003')} | Under {bold('MoEFCC')} | HQ: {bold('Chennai')}.",
    ],
    "NBA — National Biodiversity Authority, na ki Basketball wali!",
    [
        "Q: NBA's Expert Committee on Agrobiodiversity chaired by? Ans: (A) Dr. P.L. Gautam",
        "Q: Under which section was this committee reconstituted? Ans: (B) Section 13(1)",
        "Q: NBA HQ is located in? Ans: (C) Chennai",
    ],
    tag_color=GREEN
))
story.append(sp(4))

# PIB CORNER
story.append(sec_hdr("&#128240; PIB CORNER", DARK_BLUE))
story.append(sp(3))

story.append(news_card(
    "PIB",
    "Drone-Based Mail Transmission Service Launched in Himachal Pradesh",
    [
        f"Launched by {bold('Jyotiraditya Scindia')} (Union Minister of Communications); Department of Posts, {bold('Himachal Pradesh')}.",
        f"Route: {bold('Mandi Head Post Office')} &#8594; {bold('Rehardhar Branch Post Office')} | Tech Partner: {bold('Skye Air Company')}.",
        f"Capacity: {bold('10 kg')} payload | {bold('30 minutes')} endurance | Range: {bold('50 km')}.",
    ],
    "Drone ne dak pahunchai pahad pe — dak babu bhi keh raha hai 'Technology zindabad!'",
    [
        "Q: Drone mail service in HP launched between which post offices? Ans: Mandi HPO & Rehardhar BPO",
        "Q: Technology partner for drone mail in HP? Ans: (B) Skye Air Company",
        "Q: Drone payload capacity? Ans: (C) 10 kg",
        "Q: Range of drone mail service? Ans: (D) 50 km",
    ],
    tag_color=DARK_BLUE
))
story.append(sp(4))

story.append(news_card(
    "PIB",
    "Ministry of Ayush Sets Guinness Record — Largest YouTube Live Yoga Stream",
    [
        f"Ministry of Ayush + {bold('MDNIY (Morarji Desai National Institute of Yoga)')} + {bold('Habuild')} set Guinness World Record: {bold('Most Viewers for a YouTube Live Yoga Stream')}.",
        f"Viewers: {bold('4,35,831')} verified (previous record: {bold('2,46,252')} in 2024). Theme: {bold('\"Yoga for Healthy Ageing\"')}.",
        f"Minister: {bold('Prataprao Jadhav')}. National IDY 2026 event: {bold('Kolkata, West Bengal')} on {bold('21 June')}.",
        f"Static GK: International Yoga Day = {bold('21 June')} | First celebrated: {bold('2015')}.",
    ],
    "4.35 lakh log yoga live dekh rahe the — hum bhi dekh rahe the... Netflix pe!",
    [
        "Q: Who set Guinness record for YouTube Live Yoga Stream? Ans: (A) Ministry of Ayush",
        "Q: Number of verified viewers in record stream? Ans: (B) 4,35,831",
        "Q: Theme of IDY 2026 yoga stream? Ans: (C) Yoga for Healthy Ageing",
        "Q: IDY 2026 national event city? Ans: (D) Kolkata, West Bengal",
    ],
    tag_color=DARK_BLUE
))
story.append(sp(4))

story.append(news_card(
    "PIB",
    "NESTS Signs MoU to Implement Amazon Future Engineer in Eklavya Schools",
    [
        f"{bold('NESTS (National Education Society for Tribal Students)')} — under {bold('Ministry of Tribal Affairs')} — signed MoU with {bold('Learning Links Foundation (LLF)')} for Amazon Future Engineer (AFE) programme.",
        f"Valid: {bold('April 1, 2026 – March 31, 2028')} | Target: {bold('2 lakh tribal students')} in {bold('EMRS (Eklavya Model Residential Schools)')}.",
        f"Focus: Computer Science Fundamentals, AI Literacy, Career Exposure, Teacher Capacity Building.",
    ],
    "Tribal students ko AI sikhao — future ka banker wahi hoga!",
    [
        "Q: Which org signed MoU with LLF for Amazon AFE in EMRS? Ans: (A) NESTS",
        "Q: Duration of AFE programme in EMRS? Ans: (B) Apr 2026 – Mar 2028",
        "Q: How many tribal students targeted? Ans: (C) 2 lakh",
        "Q: NESTS is under which Ministry? Ans: (D) Tribal Affairs",
    ],
    tag_color=DARK_BLUE
))
story.append(sp(4))

# ── INTERNATIONAL ──────────────────────────────────────────────
story.append(sec_hdr("&#127758; INTERNATIONAL", SKY))
story.append(sp(3))

story.append(news_card(
    "INTL",
    "India Participates as 'Partner Country' 13th Time in 52nd G7 Summit",
    [
        f"52nd G7 Summit held in {bold('Evian, France')}. India participates as 'partner country' for {bold('13th time')}.",
        f"PM Modi attending at invite of French President {bold('Emmanuel Macron')} — {bold('7th consecutive')} G7 participation.",
        f"Other outreach partners: {bold('Brazil, Egypt, South Korea, UAE')}.",
        f"Static GK: G7 members: {bold('Canada, France, Germany, Italy, Japan, UK, USA')} | Founded: {bold('1975')} as G6 (Canada joined later).",
    ],
    "India G7 mein partner hai, member nahi — par hum toh G7+ pe nazar rakhte hain!",
    [
        "Q: Where was the 52nd G7 Summit held? Ans: (B) Evian, France",
        "Q: India's participation count as partner country? Ans: (C) 13th time",
        "Q: G7 was founded in which year? Ans: (A) 1975",
        "Q: Which country was NOT in the original G6? Ans: (D) Canada",
    ],
    tag_color=SKY
))
story.append(sp(4))

story.append(news_card(
    "INTL",
    "Dr. Sudhir Srivastava Sets World Record for Longest-Distance Robotic Telesurgery",
    [
        f"{bold('Dr. Sudhir Srivastava')} (Chairman & CEO, SS Innovations) performed longest-distance robotic cardiac telesurgery from {bold('Georgetown, Guyana')} to patient in {bold('Indore, India')} — distance: {bold('~20,000 km')}.",
        f"Procedure: {bold('LIMA (Left Internal Mammary Artery)')} takedown | Technology: {bold('SSI Mantra')} — India's indigenous surgical robot.",
        f"Previous record: {bold('10,000 km')} (France-India, same SSI Mantra system).",
    ],
    "20,000 km se surgery ki — doctor ne prove kiya distance koi barrier nahi!",
    [
        "Q: Who performed the world's longest robotic telesurgery? Ans: (A) Dr. Sudhir Srivastava",
        "Q: Distance covered in the record surgery? Ans: (B) ~20,000 km",
        "Q: Technology used in the telesurgery? Ans: (C) SSI Mantra",
        "Q: Surgery was performed on patient in which city? Ans: (D) Indore",
    ],
    tag_color=SKY
))
story.append(sp(4))

story.append(news_card(
    "INTL",
    "Switzerland Rejects Referendum on Capping Population at 10 Million",
    [
        f"Swiss voters {bold('rejected')} 'Sustainability Initiative' to cap population at {bold('10 million')} by 2050.",
        f"Result: {bold('54.79%')} against, {bold('45.21%')} for. Current population: ~{bold('9.5 million')}.",
        f"Proposal by: {bold('Swiss People\'s Party (SVP)')}. Had passed, would restrict residency, family reunification, asylum.",
        f"Static GK: Switzerland capital: {bold('Bern')} | Currency: {bold('Swiss Franc (CHF)')} | Not EU member but part of Schengen.",
    ],
    "Switzerland ne bola NO — 10 million capping reject! Chocolate aur watches ke liye sabka swagat hai!",
    [
        "Q: Switzerland referendum on population cap — result? Ans: (B) Rejected (54.79% against)",
        "Q: Population cap proposed in Switzerland? Ans: (A) 10 million",
        "Q: Swiss People's Party (SVP) political orientation? Ans: (C) Right-wing",
        "Q: Capital of Switzerland? Ans: (D) Bern",
    ],
    tag_color=SKY
))
story.append(sp(4))

# ── DEFENCE ──────────────────────────────────────────────────
story.append(sec_hdr("&#9876;&#65039; DEFENCE", PINK))
story.append(sp(3))

story.append(news_card(
    "DEFENCE",
    "First Batch of 17 Women Cadets from NDA Commissioned into Armed Forces",
    [
        f"Landmark: {bold('17 women cadets')} trained at {bold('NDA (National Defence Academy)')} commissioned as officers — {bold('first ever')} batch.",
        f"Distribution: {bold('Indian Army: 9')}, {bold('Air Force: 5')}, {bold('Navy: 3')} officers. Via {bold('Direct Permanent Commission')} — first time for women.",
        f"NDA Journey: {bold('148th Course')}, first {bold('co-ed batch')}; joined NDA August {bold('2022')} after {bold('2021 Supreme Court')} ruling.",
        f"Historically women entered via {bold('Short Service Commission (SSC)')} — max 10 yrs extendable to 14 yrs.",
    ],
    "17 verangnaon ne NDA se commission li — ab COAS bhi ek din mahila hongi!",
    [
        "Q: How many women cadets were commissioned in NDA's first women batch? Ans: (A) 17",
        "Q: NDA batch number of this historic co-ed batch? Ans: (C) 148th Course",
        "Q: Women traditionally entered Armed Forces via? Ans: (B) Short Service Commission (SSC)",
        "Q: Supreme Court ruling allowing women in NDA was in? Ans: (D) 2021",
    ],
    tag_color=PINK
))
story.append(sp(4))

story.append(news_card(
    "DEFENCE",
    "Lt Gen Dhiraj Seth Appointed as Chief of Army Staff w.e.f. June 30, 2026",
    [
        f"{bold('Lt Gen Dhiraj Seth')} (PVSM, UYSM, AVSM) — currently Vice Chief of Army Staff — appointed {bold('31st Army Chief (COAS)')} w.e.f. {bold('June 30, 2026')}.",
        f"Succeeds: {bold('General Upendra Dwivedi')}. Tenure until: {bold('August 31, 2028')}.",
        f"Static GK: COAS = Chief of Army Staff | HQ: {bold('New Delhi')} | Indian Army founded: {bold('1 April 1895')}.",
    ],
    "Dhiraj Seth aayenge June 30 ko — Army ka naya captain ready hai!",
    [
        "Q: Who is appointed as the new Chief of Army Staff? Ans: (A) Lt Gen Dhiraj Seth",
        "Q: When does Dhiraj Seth take charge as COAS? Ans: (B) June 30, 2026",
        "Q: Dhiraj Seth will be the ___th Army Chief? Ans: (C) 31st",
        "Q: Who does Dhiraj Seth succeed as Army Chief? Ans: (D) Gen Upendra Dwivedi",
    ],
    tag_color=PINK
))
story.append(sp(4))

# ── NATIONAL — Science/Tech ─────────────────────────────────
story.append(sec_hdr("&#128640; SCIENCE & TECHNOLOGY", NAVY))
story.append(sp(3))

story.append(news_card(
    "SCI/TECH",
    "ISRO + Dept. of Atomic Energy Collaborate on Lunar Lander for 200-Day Survival",
    [
        f"{bold('ISRO')} + {bold('Department of Atomic Energy (DAE)')} partnered to develop lunar lander technology surviving {bold('200 days')} on Moon.",
        f"Challenge: Moon surface temp {bold('+121°C')} (day) to {bold('-129°C')} (night). DAE provides nuclear-based thermal (RHU) solutions — doesn't rely on solar energy.",
        f"Goals: {bold('Chandrayaan-4')} (sample return); {bold('Chandrayaan-5/LUPEX')} with {bold('Japan')}; {bold('Indian astronaut on Moon by 2040')}; permanent lunar base by {bold('2047')}.",
        f"Static GK: ISRO Chairman: {bold('V. Narayanan')} | ISRO HQ: {bold('Bengaluru')} | Chandrayaan-3 Vikram lander survived: {bold('14 days')}.",
    ],
    "200 din moon pe rehna hai — ISRO ke liye toh normal hai, hum 2 din bina AC ke nahi reh sakte!",
    [
        "Q: ISRO-DAE collaboration aims for lunar lander survival of? Ans: (A) 200 days",
        "Q: Moon daytime temperature is? Ans: (B) +121°C",
        "Q: LUPEX (Chandrayaan-5) collaboration country? Ans: (C) Japan",
        "Q: ISRO Chairman as of 2026? Ans: (D) V. Narayanan",
    ],
    tag_color=NAVY
))
story.append(sp(4))

# GI Tags
story.append(sec_hdr("&#127823; AGRICULTURE — GI TAGS", GREEN))
story.append(sp(3))

story.append(news_card(
    "GI TAGS",
    "Jharkhand Gets GI Tags for 11 Traditional Products (NABARD Role)",
    [
        f"{bold('11 traditional products')} from {bold('Jharkhand')} granted GI Tags. NABARD played key facilitation role.",
        f"Products include: {bold('Bhagaiya Silk & Fabric, Kuchai Silk Saree, Munda Jewellery, Jharkhand Bamboo Craft, Kesaria Kalakand, Dokra Craft, Dumka Chadar & Baroni Puppets, Tussar Silk, Jadopatia Painting, Panchi Saree, Jharkhand Benam Handicraft')}.",
        f"Static GK: GI Act: {bold('1999')} | Active: Sept 2003 | Registry HQ: {bold('Chennai')} | CGPDTM under {bold('Ministry of Commerce')} | Validity: {bold('10 yrs')} | First GI: {bold('Darjeeling Tea (2004)')} | Global: WTO {bold('TRIPS Agreement')}.",
    ],
    "Jharkhand ko 11 GI tags mile — Dokra Craft bhi boli 'Abhi to hum trend mein aaye hain!'",
    [
        "Q: How many products from Jharkhand got GI tags recently? Ans: (D) 11",
        "Q: Which bank facilitated GI tags for Jharkhand? Ans: (A) NABARD",
        "Q: India's first GI tag product? Ans: (B) Darjeeling Tea",
        "Q: GI tags globally governed by? Ans: (C) WTO TRIPS Agreement",
    ],
    tag_color=GREEN
))
story.append(sp(4))

# ── DAYS ──
story.append(sec_hdr("&#128197; IMPORTANT DAYS", PURPLE))
story.append(sp(3))

story.append(news_card(
    "IMP DAY",
    "Global Wind Day 2026 — 15 June | 'Our Wind, Our Community'",
    [
        f"{bold('Global Wind Day')}: Observed {bold('15 June')} annually. Organized by {bold('WindEurope')} & {bold('GWEC (Global Wind Energy Council)')}.",
        f"Theme 2026: {bold('\"Our Wind, Our Community\"')}. India event: {bold('Goa')} — theme: '{bold('Wind Energy: From Ambition to Acceleration')}'.",
        f"Ministry: {bold('Ministry of New & Renewable Energy (MNRE)')} hosting India event.",
        f"Static GK: First Wind Day observed in {bold('Europe in 2007')} by European Wind Energy Association.",
    ],
    "Wind Day pe Goa mein conference — kash hum bhi wind ki tarah free hote!",
    [
        "Q: Global Wind Day is observed on? Ans: (A) 15 June",
        "Q: Global theme for Wind Day 2026? Ans: (B) Our Wind, Our Community",
        "Q: India's Wind Day 2026 conference location? Ans: (C) Goa",
        "Q: First Wind Day was observed in? Ans: (D) 2007",
    ],
    tag_color=PURPLE
))
story.append(sp(4))

# Appointments
story.append(sec_hdr("&#128100; APPOINTMENTS", PURPLE))
story.append(sp(3))

story.append(news_card(
    "APPT",
    "Prof. Alakh N. Sharma Appointed Chairman — High-Level Technical Expert Committee on Labour Statistics",
    [
        f"Govt appointed {bold('Prof. Alakh N. Sharma')} as Chairman (non-official) of {bold('High-Level Technical Expert Committee on Labour Statistics')}.",
        f"Current roles: Director, {bold('Institute for Human Development (IHD)')}; President, {bold('Indian Society of Labour Economics (ISLE)')}.",
        f"Committee aim: Strengthen labour market indicators, improve data accuracy & international comparability.",
    ],
    "Labour Statistics committee mein Professor aa gaye — ab data bilkul sahi hoga!",
    [
        "Q: Who was appointed Chairman of Labour Statistics expert committee? Ans: (A) Prof. Alakh N. Sharma",
        "Q: Prof. Sharma is Director of which institute? Ans: (B) Institute for Human Development (IHD)",
    ],
    tag_color=PURPLE
))

story.append(PageBreak())

# ╔══════════════════════════════════════════════════════════════╗
# ║  PAGE 2 — EXPECTED MCQs                                     ║
# ╚══════════════════════════════════════════════════════════════╝

story.append(banner("&#127919; PAGE 2: EXPECTED MCQs — Section Wise", DARK_BLUE, font_size=9))
story.append(sp(3))

# Meme strip
meme_p = Paragraph(
    "&#128293; Kapil Sir Tip: '40-50% questions direct hote hain — inhe first attempt mein pakdo!' "
    "| &#128170; Yaad raho: Numbers, Names aur Dates = 3 marks guaranteed!",
    ParagraphStyle("mt", fontName="NotoBold", fontSize=8, textColor=NAVY,
        alignment=TA_CENTER, leading=12))
meme_t = Table([[meme_p]], colWidths=[CW])
meme_t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), YELLOW),
    ("TOPPADDING",   (0,0), (-1,-1), 5),
    ("BOTTOMPADDING",(0,0), (-1,-1), 5),
]))
story.append(meme_t)
story.append(sp(5))

MCQs = [
    (1, "Noida International Airport's first commercial flight was operated by?",
     ["(A) Air India", "(B) IndiGo (6E-2278)", "(C) SpiceJet", "(D) Vistara", "(E) Akasa Air"],
     "NATIONAL", SAFFRON),
    (2, "The 'Nilachakra' trademark was secured by which temple administration?",
     ["(A) Kashi Vishwanath", "(B) Tirupati Balaji", "(C) SJTA – Jagannath Puri", "(D) Somnath Temple", "(E) Shirdi Sai Baba"],
     "NATIONAL", SAFFRON),
    (3, "The 19th MIFF 2026 AI Cinema Hackathon is titled?",
     ["(A) AI Meets Cinema", "(B) Frames of Future", "(C) Mumbai Through a Thousand Eyes", "(D) Digital Bollywood", "(E) Reel India AI"],
     "NATIONAL", SAFFRON),
    (4, "Drone-Based Mail Service in Himachal Pradesh is operated with which company?",
     ["(A) Zomato Drones", "(B) Skye Air Company", "(C) Garuda Aerospace", "(D) Drone Delivery India", "(E) TechEagle"],
     "PIB", DARK_BLUE),
    (5, "Ministry of Ayush's Guinness record was for 'Most Viewers for a YouTube Live Yoga Stream' with how many viewers?",
     ["(A) 2,46,252", "(B) 5,00,000", "(C) 3,50,000", "(D) 4,35,831", "(E) 1,75,000"],
     "PIB", DARK_BLUE),
    (6, "Which organization facilitated GI Tags for 11 Jharkhand products?",
     ["(A) SIDBI", "(B) NABARD", "(C) RBI", "(D) SEBI", "(E) EXIM Bank"],
     "AGRI", GREEN),
    (7, "Great Indian Bustard (Godawan) is the official state bird of?",
     ["(A) Gujarat", "(B) MP", "(C) Rajasthan", "(D) Punjab", "(E) Haryana"],
     "AGRI/ENV", GREEN),
    (8, "LUPEX (Chandrayaan-5) is a collaboration between ISRO and which country?",
     ["(A) USA", "(B) Russia", "(C) France", "(D) Japan", "(E) Germany"],
     "SCI/TECH", NAVY),
    (9, "Lt Gen Dhiraj Seth is the ___ Chief of Army Staff?",
     ["(A) 29th", "(B) 30th", "(C) 31st", "(D) 32nd", "(E) 28th"],
     "DEFENCE", PINK),
    (10, "First batch of women cadets at NDA was part of which NDA Course?",
     ["(A) 145th", "(B) 146th", "(C) 147th", "(D) 148th", "(E) 149th"],
     "DEFENCE", PINK),
    (11, "Where was the 52nd G7 Summit held?",
     ["(A) Paris, France", "(B) Evian, France", "(C) Lyon, France", "(D) Cannes, France", "(E) Nice, France"],
     "INTL", SKY),
    (12, "Switzerland referendum rejected proposal to cap population at?",
     ["(A) 8 million", "(B) 9 million", "(C) 10 million", "(D) 11 million", "(E) 12 million"],
     "INTL", SKY),
    (13, "Dr. Sudhir Srivastava performed robotic telesurgery from Georgetown, Guyana to which Indian city?",
     ["(A) Mumbai", "(B) Delhi", "(C) Bengaluru", "(D) Indore", "(E) Chennai"],
     "INTL", SKY),
    (14, "Global Wind Day 2026 India conference was held in?",
     ["(A) Mumbai", "(B) Delhi", "(C) Goa", "(D) Chennai", "(E) Hyderabad"],
     "IMP DAY", PURPLE),
    (15, "GI Registry in India is headquartered in?",
     ["(A) Mumbai", "(B) Delhi", "(C) Chennai", "(D) Bengaluru", "(E) Kolkata"],
     "GI TAG", GREEN),
    (16, "Jewar Airport runway length is?",
     ["(A) 2,500 m", "(B) 3,000 m", "(C) 3,500 m", "(D) 3,900 m", "(E) 4,200 m"],
     "NATIONAL", SAFFRON),
    (17, "NBA Expert Committee on Agrobiodiversity chaired by?",
     ["(A) Dr. P.L. Gautam", "(B) Dr. M.S. Swaminathan", "(C) Dr. R.S. Paroda", "(D) Prof. K.V. Rao", "(E) Dr. A.K. Singh"],
     "AGRI/ENV", GREEN),
    (18, "NESTS (Eklavya Schools Amazon AFE MoU) is under which Ministry?",
     ["(A) Education", "(B) Skill Development", "(C) Rural Development", "(D) Tribal Affairs", "(E) Social Justice"],
     "PIB", DARK_BLUE),
    (19, "IDY 2026 National Event will be held in?",
     ["(A) Delhi", "(B) Mumbai", "(C) Kolkata", "(D) Chennai", "(E) Pune"],
     "PIB", DARK_BLUE),
    (20, "The SSI Mantra telesurgery system was used to set previous record between France and India covering?",
     ["(A) 5,000 km", "(B) 8,000 km", "(C) 10,000 km", "(D) 15,000 km", "(E) 20,000 km"],
     "INTL", SKY),
    (21, "GIB is listed under which IUCN category?",
     ["(A) Vulnerable", "(B) Near Threatened", "(C) Endangered", "(D) Critically Endangered", "(E) Extinct in Wild"],
     "AGRI/ENV", GREEN),
    (22, "India is participating in G7 as partner country for how many times consecutively for PM Modi?",
     ["(A) 4th", "(B) 5th", "(C) 6th", "(D) 7th", "(E) 8th"],
     "INTL", SKY),
    (23, "Which act governs Trademark registration in India?",
     ["(A) IP Act 2000", "(B) Trade Marks Act 1999", "(C) Patents Act 1970", "(D) Copyright Act 1957", "(E) GI Act 1999"],
     "NATIONAL", SAFFRON),
]

for mcq in MCQs:
    story.append(mcq_block(mcq[0], mcq[1], mcq[2], mcq[3], mcq[4]))
    story.append(sp(3))

# Motivational closing
story.append(sp(5))
mot = Paragraph(
    "&#128170; Mehnat karo, revision karo, exam crack karo! — Kapil Sir",
    ParagraphStyle("mot", fontName="NotoBold", fontSize=10,
        textColor=NAVY, alignment=TA_CENTER, leading=14))
mot_t = Table([[mot]], colWidths=[CW])
mot_t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), YELLOW),
    ("TOPPADDING",   (0,0), (-1,-1), 8),
    ("BOTTOMPADDING",(0,0), (-1,-1), 8),
    ("BOX", (0,0), (-1,-1), 1, SAFFRON),
]))
story.append(mot_t)

story.append(PageBreak())

# ╔══════════════════════════════════════════════════════════════╗
# ║  PAGE 3 — ANSWERS & DETAILED SOLUTIONS                      ║
# ╚══════════════════════════════════════════════════════════════╝

story.append(banner("&#9989; PAGE 3: ANSWERS & DETAILED SOLUTIONS", DARK_GREEN, font_size=9))
story.append(sp(3))

# Quick Answer Key Grid
ANSWERS = {
    1:"B", 2:"C", 3:"C", 4:"B", 5:"D", 6:"B", 7:"C", 8:"D",
    9:"C", 10:"D", 11:"B", 12:"C", 13:"D", 14:"C", 15:"C",
    16:"D", 17:"A", 18:"D", 19:"C", 20:"C", 21:"D", 22:"D", 23:"B"
}

# Grid header
gh = Paragraph("&#128204; QUICK ANSWER KEY",
    ParagraphStyle("gh", fontName="NotoBold", fontSize=9,
        textColor=WHITE, alignment=TA_CENTER, leading=13))
gh_t = Table([[gh]], colWidths=[CW])
gh_t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), NAVY),
    ("TOPPADDING",   (0,0), (-1,-1), 4),
    ("BOTTOMPADDING",(0,0), (-1,-1), 4),
]))
story.append(gh_t)

# Build answer key grid (6 cols)
ans_data = []
row = []
for i, (q, a) in enumerate(ANSWERS.items(), 1):
    cell = Paragraph(f'<font name="NotoBold">Q{q}</font><br/>{a}',
        ParagraphStyle("ak", fontName="Noto", fontSize=8,
            textColor=NAVY, alignment=TA_CENTER, leading=11))
    row.append(cell)
    if len(row) == 6:
        ans_data.append(row)
        row = []
if row:
    while len(row) < 6:
        row.append(Paragraph("", s_normal))
    ans_data.append(row)

col_w = CW / 6
ak_tbl = Table(ans_data, colWidths=[col_w]*6)
ak_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#E8F5E9")),
    ("GRID", (0,0), (-1,-1), 0.5, GREEN),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING",   (0,0), (-1,-1), 3),
    ("BOTTOMPADDING",(0,0), (-1,-1), 3),
]))
story.append(ak_tbl)
story.append(sp(6))

# Solutions
SOLUTIONS = [
    (1, "NATIONAL", SAFFRON, "(B) IndiGo (6E-2278)",
     "IndiGo's flight 6E-2278 from Lucknow's Chaudhary Charan Singh Airport was the first commercial flight at Jewar Airport. '6E' is IndiGo's IATA airline code. Landed at 7:55 AM, departed for Bengaluru at 8:35 AM."),
    (2, "NATIONAL", SAFFRON, "(C) SJTA – Jagannath Puri",
     "Shree Jagannath Temple Administration (SJTA), Puri, Odisha secured trademarks for Nilachakra logo, 'Ananda Bajara' & 'Patitapabana'. Historic first for any Indian shrine under Trade Marks Act."),
    (3, "NATIONAL", SAFFRON, "(C) Mumbai Through a Thousand Eyes",
     "19th MIFF 2026 is hosting the AI Cinema Hackathon titled 'Mumbai Through a Thousand Eyes' — a 48-hour filmmaking challenge. First ever such AI hackathon at MIFF."),
    (4, "PIB", DARK_BLUE, "(B) Skye Air Company",
     "Drone mail service in HP launched by Jyotiraditya Scindia via Dept. of Posts. Tech partner is Skye Air Company. Route: Mandi HPO to Rehardhar BPO. Capacity: 10 kg, 30 min, 50 km range."),
    (5, "PIB", DARK_BLUE, "(D) 4,35,831",
     "Ministry of Ayush set Guinness record with 4,35,831 verified viewers on YouTube Live Yoga Stream. Previous record: 2,46,252 (2024). Organized with MDNIY & Habuild. Theme: 'Yoga for Healthy Ageing'."),
    (6, "AGRI", GREEN, "(B) NABARD",
     "NABARD facilitated GI Tag applications for 11 Jharkhand products along with local producer groups & govt depts. Products include Munda Jewellery, Tussar Silk, Dokra Craft, Jadopatia Painting etc."),
    (7, "AGRI/ENV", GREEN, "(C) Rajasthan",
     "Great Indian Bustard (GIB) — locally called 'Godawan' — is the official state bird of Rajasthan since 1981. Critically Endangered; wild population ~150 in Thar Desert. Captive stock now: 94 birds."),
    (8, "SCI/TECH", NAVY, "(D) Japan",
     "LUPEX = Lunar Polar Exploration Mission (Chandrayaan-5), collaboration between ISRO and JAXA (Japan). Chandrayaan-4 is sample return mission. Target: Indian astronaut on Moon by 2040."),
    (9, "DEFENCE", PINK, "(C) 31st",
     "Lt Gen Dhiraj Seth will be the 31st Chief of Army Staff, effective June 30, 2026. He succeeds Gen Upendra Dwivedi. Currently serving as Vice Chief of Army Staff. Tenure: till Aug 31, 2028."),
    (10, "DEFENCE", PINK, "(D) 148th Course",
     "17 women cadets were part of the 148th NDA Course — the first ever co-ed batch — which joined NDA in August 2022 following the 2021 Supreme Court ruling. They received Direct Permanent Commission."),
    (11, "INTL", SKY, "(B) Evian, France",
     "52nd G7 Summit was held in Evian, France. India participated as 'partner country' for the 13th time. PM Modi attended at invitation of French President Emmanuel Macron — his 7th consecutive G7."),
    (12, "INTL", SKY, "(C) 10 million",
     "Switzerland's 'Sustainability Initiative' (championed by SVP) proposed to cap population at 10 million by 2050. Rejected by 54.79% voters. Current population ~9.5 million. Proposal would have restricted EU free movement."),
    (13, "INTL", SKY, "(D) Indore",
     "Dr. Sudhir Srivastava (Chairman-CEO, SS Innovations) performed robotic cardiac telesurgery from Georgetown, Guyana to a patient in Indore, India. Distance: ~20,000 km. Used SSI Mantra — India's indigenous robot."),
    (14, "IMP DAY", PURPLE, "(C) Goa",
     "Global Wind Day 2026 (June 15): India hosted a major conference in Goa with theme 'Wind Energy: From Ambition to Acceleration'. Organized by Ministry of New & Renewable Energy (MNRE)."),
    (15, "GI TAG", GREEN, "(C) Chennai",
     "GI Registry (Geographical Indications Registry) is HQ'd in Chennai, operating under CGPDTM (Office of Controller General of Patents, Designs & Trademarks) under Ministry of Commerce & Industry."),
    (16, "NATIONAL", SAFFRON, "(D) 3,900 m",
     "Noida International Airport (Jewar) has a 3,900-metre runway with all-weather, round-the-clock operations capability. Phase 1: Lucknow, Bengaluru, Hyderabad, Amritsar. Full network by July 1."),
    (17, "AGRI/ENV", GREEN, "(A) Dr. P.L. Gautam",
     "Padma Shri Dr. P.L. Gautam was appointed to chair the reconstituted NBA Expert Committee on Agrobiodiversity for 1 year. Under Section 13(1) of Biological Diversity Act, 2002."),
    (18, "PIB", DARK_BLUE, "(D) Tribal Affairs",
     "NESTS = National Education Society for Tribal Students, an autonomous org under Ministry of Tribal Affairs. Signed MoU with Learning Links Foundation (LLF) to implement Amazon Future Engineer in EMRS."),
    (19, "PIB", DARK_BLUE, "(C) Kolkata",
     "IDY 2026 main national event scheduled in Kolkata, West Bengal on 21 June. The YouTube Yoga stream recorded 4,35,831 viewers; led by Minister Prataprao Jadhav (MoS Ayush, Ind. Charge)."),
    (20, "INTL", SKY, "(C) 10,000 km",
     "Previous world record for longest robotic telesurgery was 10,000 km (France-India), also using SSI Mantra. Dr. Sudhir Srivastava's new record of ~20,000 km more than doubled the previous record."),
    (21, "AGRI/ENV", GREEN, "(D) Critically Endangered",
     "Great Indian Bustard (GIB/Godawan) is listed as Critically Endangered by IUCN. Wild population: fewer than 150. Mainly in Rajasthan's Thar Desert. State bird of Rajasthan since 1981."),
    (22, "INTL", SKY, "(D) 7th",
     "PM Modi's participation in 52nd G7 Summit in Evian, France marks his 7th consecutive G7 summit participation. India is participating as 'partner country' for the 13th time overall."),
    (23, "NATIONAL", SAFFRON, "(B) Trade Marks Act 1999",
     "Trademarks in India are registered under the Trade Marks Act, 1999. SJTA used this Act to trademark Nilachakra, Ananda Bajara & Patitapabana. Governed by CGPDTM under Ministry of Commerce & Industry."),
]

for i, sol in enumerate(SOLUTIONS):
    story.append(sol_block(sol[0], sol[1], sol[2], sol[3], sol[4], is_alt=(i%2==1)))
    story.append(sp(2))

story.append(PageBreak())

# ╔══════════════════════════════════════════════════════════════╗
# ║  PAGE 4 — CHEAT SHEET                                       ║
# ╚══════════════════════════════════════════════════════════════╝

story.append(banner("&#9889; PAGE 4: QUICK CHEAT SHEET | Section-Wise", PURPLE, font_size=9))
story.append(sp(2))

last_meme = Paragraph(
    "&#128293; Last minute revision ke liye BEST! | Kapil Sir ke notes = Exam crack guaranteed!",
    ParagraphStyle("lm", fontName="NotoBold", fontSize=8,
        textColor=NAVY, alignment=TA_CENTER, leading=12))
lm_t = Table([[last_meme]], colWidths=[CW])
lm_t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), YELLOW),
    ("TOPPADDING",   (0,0), (-1,-1), 2),
    ("BOTTOMPADDING",(0,0), (-1,-1), 2),
]))
story.append(lm_t)
story.append(sp(2))

def cheat_box(title, color, rows_data):
    """rows_data: list of (key, value) tuples"""
    hdr = Paragraph(title, ParagraphStyle("chdr", fontName="NotoBold",
        fontSize=7, textColor=WHITE, alignment=TA_CENTER, leading=10))
    tbl_rows = [[hdr]]
    for k, v in rows_data:
        kp = Paragraph(f'<font name="NotoBold">{k}</font>',
            ParagraphStyle("ck", fontName="NotoBold", fontSize=7, leading=10, textColor=NAVY))
        vp = Paragraph(v, ParagraphStyle("cv", fontName="Noto", fontSize=7, leading=10))
        tbl_rows.append([Table([[kp, vp]],
            colWidths=[None],
            style=TableStyle([("TOPPADDING",(0,0),(-1,-1),0),
                              ("BOTTOMPADDING",(0,0),(-1,-1),0)]))])

    # Simple table
    data = [[hdr]]
    for k, v in rows_data:
        kp = Paragraph(f'<font name="NotoBold">{k}:</font>',
            ParagraphStyle("ck2", fontName="NotoBold", fontSize=7, textColor=NAVY, leading=10))
        vp = Paragraph(v, ParagraphStyle("cv2", fontName="Noto", fontSize=7, leading=10))
        data.append([kp, vp])

    cw1 = 28*mm
    col_w = (CW/2) - 4*mm
    cw2 = col_w - cw1 - 2*mm

    inner_data = []
    for k, v in rows_data:
        kp = Paragraph(f'<font name="NotoBold">{k}:</font>',
            ParagraphStyle("ck3", fontName="NotoBold", fontSize=6, textColor=NAVY, leading=8.5))
        vp = Paragraph(v, ParagraphStyle("cv3", fontName="Noto", fontSize=6, leading=8.5))
        inner_data.append([kp, vp])

    inner_tbl = Table(inner_data, colWidths=[cw1, cw2])
    inner_tbl.setStyle(TableStyle([
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 0),
        ("LEFTPADDING",  (0,0), (-1,-1), 3),
        ("RIGHTPADDING", (0,0), (-1,-1), 2),
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [colors.HexColor("#FFFFFF"), colors.HexColor("#F5F5FF")]),
    ]))

    hdr_tbl = Table([[hdr]], colWidths=[col_w])
    hdr_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), color),
        ("TOPPADDING",   (0,0), (-1,-1), 2),
        ("BOTTOMPADDING",(0,0), (-1,-1), 2),
    ]))
    box = Table([[hdr_tbl], [inner_tbl]], colWidths=[col_w])
    box.setStyle(TableStyle([
        ("BOX", (0,0), (-1,-1), 0.8, color),
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 0),
        ("LEFTPADDING",  (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ]))
    return box

# LEFT COLUMN boxes
national_box = cheat_box("&#127470;&#127475; NATIONAL", SAFFRON, [
    ("Jewar Airport", "Noida Intl Airport; 3900m runway; IndiGo 6E-2278 first flight"),
    ("First Passengers", "170 farmers (20 women); met CM Yogi Adityanath"),
    ("Initial Destinations", "Lucknow, Bengaluru, Hyderabad, Amritsar"),
    ("July 1", "Full network: 16-17 cities, 11 states"),
    ("MIFF 2026", "19th edition; AI Cinema Hackathon — first time; 48 hrs"),
    ("MIFF Scale", "346 films, 46 nations; 18 awards; Rs 45 lakh prize"),
    ("V Shantaram Award", "Lifetime Achievement at MIFF 2026"),
    ("Jagannath TM", "SJTA Puri: Nilachakra, Ananda Bajara, Patitapabana"),
])

sci_box = cheat_box("&#128640; SCIENCE & TECH", NAVY, [
    ("ISRO+DAE", "Lunar lander for 200 days on Moon"),
    ("Moon Temps", "+121°C (day) / -129°C (night)"),
    ("ISRO Chairman", "V. Narayanan | HQ: Bengaluru"),
    ("Chandrayaan-4", "Sample return mission"),
    ("LUPEX/CY-5", "Collaboration with Japan"),
    ("India Moon Goal", "Astronaut by 2040; base by 2047"),
    ("Telesurgery", "Dr. Sudhir Srivastava; Guyana to Indore; 20,000 km"),
    ("SSI Mantra", "India's indigenous surgical robot; CEO: SS Innovations"),
])

agri_box = cheat_box("&#127807; AGRI / GI TAG", GREEN, [
    ("Jharkhand GI", "11 products; NABARD facilitated"),
    ("GI Products", "Munda Jewellery, Tussar Silk, Dokra, Jadopatia, Kuchai Silk etc."),
    ("GI Act", "1999; Active Sept 2003; Validity 10 yrs"),
    ("GI Registry", "Chennai; Under CGPDTM; Min of Commerce"),
    ("First GI", "Darjeeling Tea (2004)"),
    ("GIB/Godawan", "Rajasthan state bird since 1981; Critically Endangered"),
    ("GIB Captive", "94 birds; 26 chicks hatched; ~150 wild"),
    ("GIB Partners", "MoEFCC + Rajasthan FD + WII"),
])

sports_box = cheat_box("&#128197; IMPORTANT DAYS", PURPLE, [
    ("Global Wind Day", "15 June | 'Our Wind, Our Community'"),
    ("India Wind Conf", "Goa; 'Wind Energy: From Ambition to Acceleration'"),
    ("Wind Day Origin", "Europe, 2007 by European Wind Energy Assoc"),
    ("MNRE", "Hosting India Wind Day flagship event"),
    ("Int'l Yoga Day", "21 June | IDY 2026 theme: Yoga for Healthy Ageing"),
    ("IDY 2026 City", "Kolkata, West Bengal"),
    ("Yoga GWR", "4,35,831 viewers; Min Ayush + MDNIY + Habuild"),
])

# RIGHT COLUMN boxes
pib_box = cheat_box("&#128240; PIB / SCHEMES", DARK_BLUE, [
    ("Drone Mail HP", "Dept of Posts; Mandi HPO to Rehardhar BPO"),
    ("Drone Partner", "Skye Air Co | Cap: 10kg, 30 min, 50 km"),
    ("Drone Launch", "By Jyotiraditya Scindia (Min. Communications)"),
    ("NESTS-LLF MoU", "Amazon Future Engineer in EMRS"),
    ("AFE Duration", "Apr 2026 – Mar 2028; 2 lakh tribal students"),
    ("NESTS Ministry", "Ministry of Tribal Affairs"),
    ("AFE Focus", "CS Fundamentals, AI Literacy, Career Expo, Teacher Training"),
    ("NBA Committee", "Agrobiodiversity; Chair: Dr. P.L. Gautam; 1 year"),
])

intl_box = cheat_box("&#127758; INTERNATIONAL", SKY, [
    ("52nd G7", "Evian, France | India: 13th time as partner country"),
    ("G7 Members", "Canada, France, Germany, Italy, Japan, UK, USA"),
    ("G7 Founded", "1975 as G6 (Canada added later)"),
    ("Modi at G7", "7th consecutive participation; invited by Macron"),
    ("Other Partners", "Brazil, Egypt, South Korea, UAE"),
    ("Switzerland", "Rejected pop. cap at 10 million (54.79% against)"),
    ("Swiss Party", "Swiss People's Party (SVP) championed proposal"),
    ("Telesurgery WR", "20,000 km (Guyana-Indore); prev record: 10,000 km"),
])

def_box = cheat_box("&#9876; DEFENCE / APPOINTMENTS", PINK, [
    ("NDA Women", "17 women cadets; 148th Course; joined Aug 2022"),
    ("SC Ruling", "2021 SC opened NDA to women"),
    ("Army: 9", "Air Force: 5 | Navy: 3 officers commissioned"),
    ("DPC First", "First Direct Permanent Commission for women"),
    ("Old Route", "Short Service Commission (SSC): max 10-14 yrs"),
    ("New COAS", "Lt Gen Dhiraj Seth; w.e.f. June 30, 2026"),
    ("31st COAS", "Succeeds Gen Upendra Dwivedi; till Aug 31, 2028"),
    ("Alakh Sharma", "Chairman, High-Level Technical Expert Committee on Labour Statistics"),
])

# Combine in 2-column layout
half_w = (CW - 4*mm) / 2

left_blocks  = [national_box, sci_box, agri_box, sports_box]
right_blocks = [pib_box, intl_box, def_box]

# Pad right to same count
while len(right_blocks) < len(left_blocks):
    right_blocks.append(None)

dual_rows = []
for lb, rb in zip(left_blocks, right_blocks):
    left_cell  = lb if lb else Paragraph("", s_normal)
    right_cell = rb if rb else Paragraph("", s_normal)
    dual_rows.append([left_cell, right_cell])
    dual_rows.append([Spacer(1,1), Spacer(1,1)])

dual_tbl = Table(dual_rows, colWidths=[half_w, half_w])
dual_tbl.setStyle(TableStyle([
    ("TOPPADDING",   (0,0), (-1,-1), 0),
    ("BOTTOMPADDING",(0,0), (-1,-1), 0),
    ("LEFTPADDING",  (0,0), (-1,-1), 2),
    ("RIGHTPADDING", (0,0), (-1,-1), 2),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
]))
story.append(dual_tbl)
story.append(sp(2))

# Full-width Static GK Table
sg_hdr = Paragraph("&#9889; STATIC GK QUICK REFERENCE TABLE",
    ParagraphStyle("sg", fontName="NotoBold", fontSize=8,
        textColor=WHITE, alignment=TA_CENTER, leading=11))
sg_hdr_t = Table([[sg_hdr]], colWidths=[CW])
sg_hdr_t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), PURPLE),
    ("TOPPADDING",   (0,0), (-1,-1), 3),
    ("BOTTOMPADDING",(0,0), (-1,-1), 3),
]))
story.append(sg_hdr_t)

sg_data = [
    ["Topic", "Key Fact", "Static Detail"],
    ["GIB/Godawan", "Rajasthan State Bird since 1981", "Critically Endangered | Thar Desert | WII conservation"],
    ["GI Registry", "HQ: Chennai", "Under CGPDTM | Min Commerce | GI Act 1999 | Validity 10 yrs"],
    ["First GI Tag India", "Darjeeling Tea (2004)", "GI Globally: WTO TRIPS Agreement"],
    ["NDA Women Batch", "148th Course | 2022 joined", "SC 2021 ruling | 17 officers | Army-9, AF-5, Navy-3"],
    ["G7", "Founded 1975 as G6", "Canada, France, Germany, Italy, Japan, UK, USA"],
    ["ISRO Chairman", "V. Narayanan", "HQ: Bengaluru | Chandrayaan-5/LUPEX: Japan collab"],
    ["Jagannath Temple", "SJTA, Puri, Odisha", "Trademarks: Nilachakra, Ananda Bajara, Patitapabana"],
    ["MIFF 2026", "19th Edition | Mumbai", "346 films, 46 nations | Rs 45 lakh | V. Shantaram Award"],
    ["Jewar Airport", "Noida Intl Airport, UP", "3900m runway | IndiGo 6E-2278 | CM: Yogi Adityanath"],
    ["NBA", "National Biodiversity Authority", "Est. 2003 | HQ: Chennai | MoEFCC | Bio Diversity Act 2002"],
    ["Global Wind Day", "15 June annually", "Organized by WindEurope & GWEC | First: Europe 2007"],
    ["IDY", "International Yoga Day: 21 June", "First IDY: 2015 | IDY 2026: Kolkata, West Bengal"],
    ["SSI Mantra", "India's surgical robot", "CEO Dr. Sudhir Srivastava | 20,000 km telesurgery WR"],
    ["NESTS", "National Edu Soc for Tribal Students", "Under Min Tribal Affairs | EMRS schools"],
    ["Dhiraj Seth", "31st COAS from June 30, 2026", "Succeeds Gen Upendra Dwivedi | Tenure till Aug 2028"],
]

def sg_cell(txt, bold_flag=False, align=TA_LEFT):
    return Paragraph(txt, ParagraphStyle("sgc", fontName="NotoBold" if bold_flag else "Noto",
        fontSize=6.5, textColor=NAVY if not bold_flag else WHITE,
        alignment=align, leading=9))

sg_rows = []
for i, row in enumerate(sg_data):
    if i == 0:
        sg_rows.append([sg_cell(c, bold_flag=True, align=TA_CENTER) for c in row])
    else:
        sg_rows.append([sg_cell(c) for c in row])

cw3 = [32*mm, 50*mm, CW-82*mm]
sg_tbl = Table(sg_rows, colWidths=cw3)
sg_style = [
    ("BACKGROUND", (0,0), (-1,0), PURPLE),
    ("TEXTCOLOR",  (0,0), (-1,0), WHITE),
    ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#CCCCCC")),
    ("TOPPADDING",   (0,0), (-1,-1), 1),
    ("BOTTOMPADDING",(0,0), (-1,-1), 1),
    ("LEFTPADDING",  (0,0), (-1,-1), 4),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
]
for i in range(1, len(sg_data)):
    bg = colors.HexColor("#F3E5F5") if i % 2 == 1 else colors.HexColor("#EDE7F6")
    sg_style.append(("BACKGROUND", (0,i), (-1,i), bg))
sg_tbl.setStyle(TableStyle(sg_style))
story.append(sg_tbl)
story.append(sp(2))

# Final motivational
final_p = Paragraph(
    "&#127775; Mehnat karo, revision karo, exam crack karo! — Kapil Sir | "
    "Telegram: @kkathpal | +91 8929496130 | www.learningniti.com",
    ParagraphStyle("final", fontName="NotoBold", fontSize=8,
        textColor=NAVY, alignment=TA_CENTER, leading=12))
final_t = Table([[final_p]], colWidths=[CW])
final_t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), YELLOW),
    ("TOPPADDING",   (0,0), (-1,-1), 6),
    ("BOTTOMPADDING",(0,0), (-1,-1), 6),
    ("BOX", (0,0), (-1,-1), 1, SAFFRON),
]))
story.append(final_t)

# ── Build Doc ────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=M, rightMargin=M,
    topMargin=M, bottomMargin=14*mm,
    title=f"{DATE_STR} Current Affairs Revision — Kapil Kathpal",
    author="Kapil Kathpal | LearningNiti"
)

QUIZ_OUTPUT = OUTPUT.replace("_RevisionSheet.pdf", "_Quiz.html")
build_quiz_html(DATE_STR, MCQs, SOLUTIONS, QUIZ_OUTPUT)

doc.build(story, onFirstPage=footer_canvas, onLaterPages=footer_canvas)
print(f"PDF created: {OUTPUT}")


