#!/usr/bin/env python3
"""
Tamil Nadu NEET-UG Mastery Hub & Bilingual (Tamil + English) Gemini AI Coach Server.
- Serves the interactive NEET Mock Exam (OMR Mode) & Guided Practice SPA.
- Grades mock/practice exams server-side against verified questions_bank.json (+4 / -1 / 0).
- Tracks student scores, negative marks, subject-wise mastery, and mistake bank in SQLite
  (neet_data.db) + readable mentor summary (student_score_ledger.json).
- Powers the Multilingual (Tamil, Tanglish, English) AI NEET Coach using Google Gemini
  (Cloud Gemini REST API via GEMINI_API_KEY, local Gemini via agy CLI, + offline NCERT fallback).
"""

import http.server
import json
import os
import re
import socketserver
import sqlite3
import subprocess
import sys
import threading
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime

PORT = int(os.environ.get("PORT", "8090"))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "neet_data.db")
LEDGER_PATH = os.path.join(BASE_DIR, "student_score_ledger.json")
QUESTIONS_PATH = os.path.join(BASE_DIR, "questions_bank.json")
PAST_PAPERS_PATH = os.path.join(BASE_DIR, "past_papers_archive.json")
AGY_BIN = os.environ.get("AGY_BIN", os.path.expanduser("~/.local/bin/agy"))

DB_LOCK = threading.Lock()

# Load verified question bank + 2013-2026 official past papers archive at startup
with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
    QUESTION_BANK = json.load(f)

PAST_PAPERS_ARCHIVE = {}
if os.path.exists(PAST_PAPERS_PATH):
    with open(PAST_PAPERS_PATH, "r", encoding="utf-8") as f:
        PAST_PAPERS_ARCHIVE = json.load(f)
    QUESTION_BANK.setdefault("modules", {}).update(PAST_PAPERS_ARCHIVE.get("modules", {}))
    QUESTION_BANK.setdefault("questions", []).extend(PAST_PAPERS_ARCHIVE.get("questions", []))

QUESTIONS_BY_ID = {int(q["id"]): q for q in QUESTION_BANK.get("questions", [])}


def init_db():
    with DB_LOCK:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                district TEXT DEFAULT 'Chennai',
                board TEXT DEFAULT 'TN State Board (Samacheer Kalvi)',
                quota_category TEXT DEFAULT 'BC (85% TN State Quota)',
                language_pref TEXT DEFAULT 'bilingual',
                target_score INTEGER DEFAULT 650,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS exam_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                student_name TEXT NOT NULL,
                module_id TEXT NOT NULL,
                module_title TEXT NOT NULL,
                mode TEXT NOT NULL,
                total_questions INTEGER NOT NULL,
                attempted INTEGER NOT NULL,
                correct_count INTEGER NOT NULL,
                wrong_count INTEGER NOT NULL,
                unanswered_count INTEGER NOT NULL,
                raw_score INTEGER NOT NULL,
                max_score INTEGER NOT NULL,
                negative_marks_lost INTEGER NOT NULL,
                accuracy_pct REAL NOT NULL,
                projected_720 INTEGER NOT NULL,
                tn_college_tier TEXT NOT NULL,
                time_spent_sec INTEGER NOT NULL,
                subject_breakdown_json TEXT NOT NULL,
                answers_json TEXT NOT NULL,
                wrong_question_ids_json TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS coach_interactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                student_name TEXT NOT NULL,
                question_id INTEGER,
                subject TEXT,
                user_choice TEXT,
                language_detected TEXT NOT NULL,
                student_message TEXT NOT NULL,
                coach_reply TEXT NOT NULL,
                engine_used TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        conn.commit()
        conn.close()


def sync_mentor_ledger():
    """Exports a clean, human-readable JSON ledger of all attempts for mentor/coach tracking."""
    try:
        with DB_LOCK:
            conn = sqlite3.connect(DB_PATH)
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(
                """
                SELECT id, student_id, student_name, module_id, module_title, mode,
                       total_questions, attempted, correct_count, wrong_count, unanswered_count,
                       raw_score, max_score, negative_marks_lost, accuracy_pct, projected_720,
                       tn_college_tier, time_spent_sec, subject_breakdown_json, wrong_question_ids_json, created_at
                FROM exam_attempts
                ORDER BY id DESC
                LIMIT 200
                """
            )
            rows = [dict(r) for r in cur.fetchall()]
            for r in rows:
                r["subject_breakdown"] = json.loads(r.pop("subject_breakdown_json", "{}"))
                r["wrong_question_ids"] = json.loads(r.pop("wrong_question_ids_json", "[]"))
            conn.close()

        summary = {
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_attempts_recorded": len(rows),
            "best_projected_720": max((r["projected_720"] for r in rows), default=0),
            "average_projected_720": round(sum(r["projected_720"] for r in rows) / len(rows), 1) if rows else 0,
            "attempts": rows,
        }
        with open(LEDGER_PATH, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
    except Exception as exc:
        print(f"Ledger sync warning: {exc}", file=sys.stderr)


def evaluate_tn_college_tier(projected_720: int, quota_category: str = "") -> str:
    is_75_govt = "7.5%" in (quota_category or "")
    if is_75_govt:
        if projected_720 >= 565:
            return "On Track: Tier-1 TN Govt Medical College (MMC / Stanley Chennai — 7.5% Quota)"
        if projected_720 >= 515:
            return "On Track: Tier-2 TN Govt Medical College (Madurai / Coimbatore / Kilpauk — 7.5% Quota)"
        if projected_720 >= 465:
            return "On Track: TN District Government Medical College (7.5% Govt School Quota)"
        return "Building Foundation: Increase NCERT Biology + Chemistry accuracy to cross 470+/720"

    if projected_720 >= 665:
        return "On Track: Tier-1 TN Govt Medical College (MMC Chennai / Stanley / JIPMER)"
    if projected_720 >= 630:
        return "On Track: Tier-2 Premier TN Govt Medical College (Kilpauk / Madurai / Coimbatore GMC)"
    if projected_720 >= 595:
        return "On Track: TN State Quota Government Medical College (36+ TN GMCs)"
    if projected_720 >= 520:
        return "Borderline State Self-Financing / BDS Quota — Cut -1 Negative Marks to hit 600+"
    return "Foundation Phase — Master NCERT Biology (340+/360 target) & Eliminate Blind Guessing"


def grade_exam_submission(payload: dict) -> dict:
    student_id = str(payload.get("student_id") or "default_student").strip()
    student_name = str(payload.get("student_name") or "NEET Aspirant").strip()
    quota_category = str(payload.get("quota_category") or "BC (85% TN State Quota)").strip()
    module_id = str(payload.get("module_id") or "full_mock_1").strip()
    module_title = str(payload.get("module_title") or "NEET Mock Test").strip()
    mode = str(payload.get("mode") or "mock").strip()
    time_spent_sec = max(0, int(payload.get("time_spent_sec") or 0))
    question_ids = payload.get("question_ids") or []
    answers = payload.get("answers") or {}

    if not question_ids:
        mod = QUESTION_BANK.get("modules", {}).get(module_id)
        if mod and mod.get("questionIds"):
            question_ids = mod["questionIds"]
        else:
            question_ids = [int(k) for k in answers.keys() if str(k).isdigit()]

    subjects = {}
    for subj in ("Physics", "Chemistry", "Botany", "Zoology"):
        subjects[subj] = {
            "total": 0,
            "attempted": 0,
            "correct": 0,
            "wrong": 0,
            "unanswered": 0,
            "score": 0,
            "max_score": 0,
        }

    total_q = 0
    correct_count = 0
    wrong_count = 0
    unanswered_count = 0
    wrong_q_ids = []
    per_question_review = []

    for raw_qid in question_ids:
        qid = int(raw_qid)
        q = QUESTIONS_BY_ID.get(qid)
        if not q:
            continue
        total_q += 1
        subj = q["subject"]
        subjects[subj]["total"] += 1
        subjects[subj]["max_score"] += 4

        chosen = str(answers.get(str(qid)) or answers.get(qid) or "").strip().upper()
        truth = q["correct"]
        acc_opts = set(q.get("acceptedOptions") or [truth])
        ans_status = q.get("answerStatus") or "normal"

        if ans_status == "dropped":
            # Official NTA Rule: Dropped question awards +4 bonus to all candidates
            status = "correct"
            marks = 4
            correct_count += 1
            subjects[subj]["attempted"] += 1
            subjects[subj]["correct"] += 1
            subjects[subj]["score"] += 4
        elif not chosen:
            status = "unanswered"
            marks = 0
            unanswered_count += 1
            subjects[subj]["unanswered"] += 1
        elif chosen in acc_opts:
            status = "correct"
            marks = 4
            correct_count += 1
            subjects[subj]["attempted"] += 1
            subjects[subj]["correct"] += 1
            subjects[subj]["score"] += 4
        else:
            status = "wrong"
            marks = -1
            wrong_count += 1
            wrong_q_ids.append(qid)
            subjects[subj]["attempted"] += 1
            subjects[subj]["wrong"] += 1
            subjects[subj]["score"] -= 1

        per_question_review.append(
            {
                "question_id": qid,
                "subject": subj,
                "chapter": q["chapter"],
                "chosen": chosen or None,
                "correct": truth,
                "status": status,
                "marks": marks,
            }
        )

    attempted = correct_count + wrong_count
    raw_score = (correct_count * 4) - (wrong_count * 1)
    max_score = total_q * 4
    negative_marks_lost = wrong_count * 1
    accuracy_pct = round((correct_count / attempted) * 100.0, 1) if attempted > 0 else 0.0
    projected_720 = round((raw_score / max_score) * 720) if max_score > 0 else 0
    projected_720 = max(-180, min(720, int(projected_720)))
    tn_tier = evaluate_tn_college_tier(projected_720, quota_category)
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Remove empty subject buckets if a single-subject practice module was taken
    active_subjects = {k: v for k, v in subjects.items() if v["total"] > 0}

    with DB_LOCK:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO exam_attempts (
                student_id, student_name, module_id, module_title, mode,
                total_questions, attempted, correct_count, wrong_count, unanswered_count,
                raw_score, max_score, negative_marks_lost, accuracy_pct, projected_720,
                tn_college_tier, time_spent_sec, subject_breakdown_json, answers_json,
                wrong_question_ids_json, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                student_id,
                student_name,
                module_id,
                module_title,
                mode,
                total_q,
                attempted,
                correct_count,
                wrong_count,
                unanswered_count,
                raw_score,
                max_score,
                negative_marks_lost,
                accuracy_pct,
                projected_720,
                tn_tier,
                time_spent_sec,
                json.dumps(active_subjects, ensure_ascii=False),
                json.dumps(answers, ensure_ascii=False),
                json.dumps(wrong_q_ids),
                now_str,
            ),
        )
        attempt_id = cur.lastrowid
        conn.commit()
        conn.close()

    sync_mentor_ledger()

    return {
        "attempt_id": attempt_id,
        "student_id": student_id,
        "student_name": student_name,
        "module_id": module_id,
        "module_title": module_title,
        "mode": mode,
        "total_questions": total_q,
        "attempted": attempted,
        "correct_count": correct_count,
        "wrong_count": wrong_count,
        "unanswered_count": unanswered_count,
        "raw_score": raw_score,
        "max_score": max_score,
        "negative_marks_lost": negative_marks_lost,
        "accuracy_pct": accuracy_pct,
        "projected_720": projected_720,
        "tn_college_tier": tn_tier,
        "time_spent_sec": time_spent_sec,
        "subject_breakdown": active_subjects,
        "wrong_question_ids": wrong_q_ids,
        "per_question_review": per_question_review,
        "created_at": now_str,
    }


def detect_language_intent(student_msg: str, ui_lang_pref: str = "bilingual") -> str:
    msg = (student_msg or "").strip()
    if re.search(r"[\u0B80-\u0BFF]", msg):
        return "tamil_script"
    lower = msg.lower()
    tanglish_markers = (
        "tamil", "தமிழில்", "enna", "epdi", "eppadi", "puriyala", "sollunga",
        "vilakkam", "yen ", "thavaru", "sari", "puriyavillai", "konjam",
    )
    if any(tok in lower for tok in tanglish_markers):
        return "tamil_requested"
    if ui_lang_pref in ("ta", "tamil"):
        return "tamil_preferred"
    if ui_lang_pref == "bilingual":
        return "bilingual"
    return "english"


def build_neet_gemini_prompt(
    q_data: dict,
    question_number: int,
    user_choice: str,
    student_msg: str,
    student_name: str,
    lang_intent: str,
    recent_history: list,
) -> str:
    q = q_data or {}
    qid = q.get("id")
    if qid and int(qid) in QUESTIONS_BY_ID:
        # Enrich with authoritative server-side NCERT data
        q = QUESTIONS_BY_ID[int(qid)]

    subj = q.get("subject", "NEET Science")
    chapter = q.get("chapter", "")
    ncert_ref = q.get("ncertRef", "NCERT Class 11/12")
    stem_en = q.get("stem_en", "")
    stem_ta = q.get("stem_ta", "")
    correct = q.get("correct", "")
    exp_en = q.get("explanation_en", "")
    exp_ta = q.get("explanation_ta", "")
    key_pt = q.get("ncert_key_point", "")
    traps = q.get("trap_breakdown") or {}
    choices = q.get("choices") or []
    vid = q.get("videoTutorial") or {}

    choices_block = "\n".join(
        f"  ({c.get('letter')}) {c.get('text_en')} | தமிழ்: {c.get('text_ta')}"
        for c in choices
    ) or "  (General NEET conceptual / strategy query)"

    traps_block = "\n".join(
        f"  Option {k}: {v}" for k, v in traps.items()
    ) or "  None"

    hist_lines = []
    if isinstance(recent_history, list):
        for turn in recent_history[-6:]:
            if isinstance(turn, dict) and turn.get("text"):
                role = "Student" if turn.get("sender") == "student" else "NEET Coach"
                hist_lines.append(f"{role}: {str(turn['text'])[:450]}")
    history_str = "\n".join(hist_lines) if hist_lines else "(Start of coaching thread)"

    if lang_intent in ("tamil_script", "tamil_requested", "tamil_preferred"):
        lang_rule = (
            "Respond primarily in clear, encouraging Tamil Nadu academic Tamil (தமிழ்), "
            "keeping essential NCERT English scientific terms/formulas in parentheses so she masters both!"
        )
    elif lang_intent == "bilingual":
        lang_rule = (
            "Provide a concise, sharp explanation in English FIRST, followed by a clear, natural "
            "Tamil (தமிழ் சுருக்கம்) takeaway so she understands 100% in both languages."
        )
    else:
        lang_rule = (
            "Respond in clear, crisp English. If helpful, include key Tamil scientific term equivalents briefly."
        )

    student_label = student_name or "Student"
    choice_label = user_choice or "Not selected yet"

    return f"""You are a senior Tamil Nadu NEET-UG Expert Coach (who has authored multiple 720-mark NEET mock papers and coached Tamil Nadu State Board & CBSE girls into MMC Chennai and top TN Government Medical Colleges).
You are tutoring {student_label} one-on-one.

STRICT COACHING & STYLE RULES:
- Do NOT use emojis anywhere in your response.
- Ground every scientific claim strictly in NMC-rationalized Class 11 & Class 12 NCERT textbooks.
- {lang_rule}
- Directly answer what {student_label} asked in 90-200 words (unless she asks for a full practice MCQ or detailed derivation).
- Point out how to avoid the -1 negative marking trap on this topic.
- Use **bold** for key NCERT terms and answer letters.
- Write all mathematical and chemical formulas in clean standard LaTeX ($...$ for inline formulas, $$...$$ for standalone equations). Never wrap **bold** around $...$ (use \mathbf{...} inside LaTeX if needed). On multi-step derivations, write each step on its own short line rather than chaining 4-5 '=' signs on one wide line so equations fit cleanly on mobile screens.

ACTIVE NEET QUESTION CONTEXT (Q#{question_number or q.get('id', '')}):
- Subject & Chapter: {subj} — {chapter} ({ncert_ref})
- Question (English): {stem_en}
- Question (Tamil): {stem_ta}
- Options:
{choices_block}
- Student's Current Selected Bubble: {choice_label}
- Verified Correct Option: {correct}
- Verified English Solution: {exp_en}
- Verified Tamil Solution: {exp_ta}
- NCERT High-Yield Rule: {key_pt}
- -1 Negative Mark Distractor Traps:
{traps_block}
- Recommended Video Channel: {vid.get('title', '')} ({vid.get('url', '')})

RECENT CONVERSATION:
{history_str}

STUDENT'S QUESTION:
{student_msg}

Write your NEET Coach response now:"""


def call_gemini_rest_api(prompt_str: str, api_key: str):
    """Calls Google Gemini API (gemini-2.5-flash / gemini-2.0-flash) directly via HTTPS."""
    for model_id in ("gemini-2.5-flash", "gemini-2.0-flash"):
        url = (
            f"https://generativelanguage.googleapis.com/v1beta/models/"
            f"{model_id}:generateContent?key={urllib.parse.quote(api_key)}"
        )
        req_body = json.dumps(
            {
                "contents": [{"parts": [{"text": prompt_str}]}],
                "generationConfig": {"temperature": 0.35, "maxOutputTokens": 900},
            }
        ).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=req_body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                candidates = data.get("candidates") or []
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts") or []
                    text = "".join(p.get("text", "") for p in parts).strip()
                    if text:
                        return text, f"google_gemini_api ({model_id})"
        except Exception as exc:
            print(f"Gemini REST ({model_id}) notice: {exc}", file=sys.stderr)
    return None, None


def call_local_agy_gemini(prompt_str: str):
    """Calls authenticated Google Gemini models via local agy CLI on this laptop."""
    if not os.path.exists(AGY_BIN):
        return None, None
    env = os.environ.copy()
    scratch_dir = "/tmp/neet_gemini_scratch"
    os.makedirs(scratch_dir, exist_ok=True)
    for model_name in ("gemini-3.8-flash-low", "gemini-4-argon-low", "gemini-4-carbon-low"):
        try:
            proc = subprocess.run(
                [
                    AGY_BIN,
                    "--model",
                    model_name,
                    "--mode",
                    "plan",
                    "--disable-slash-commands",
                    f"-p={prompt_str}",
                ],
                cwd=scratch_dir,
                text=True,
                capture_output=True,
                timeout=34,
                env=env,
            )
            if proc.returncode == 0 and proc.stdout and proc.stdout.strip():
                return proc.stdout.strip(), f"gemini_agy ({model_name})"
            print(
                f"agy Gemini ({model_name}) non-zero rc={proc.returncode}: {(proc.stderr or '')[:200]}",
                file=sys.stderr,
            )
        except Exception as exc:
            print(f"agy Gemini ({model_name}) notice: {exc}", file=sys.stderr)
    return None, None


def build_offline_bilingual_fallback(q_data: dict, question_number: int, user_choice: str, student_msg: str, lang_intent: str) -> str:
    q = q_data or {}
    qid = q.get("id")
    if qid and int(qid) in QUESTIONS_BY_ID:
        q = QUESTIONS_BY_ID[int(qid)]

    if not q.get("stem_en"):
        return (
            "**NEET-UG Coaching Guide (English & தமிழ்)**\n\n"
            "Focus on **NCERT Class 11 & 12** line-by-line: Biology carries **360/720 marks (90 Qs)**, "
            "Chemistry **180 marks (45 Qs)**, and Physics **180 marks (45 Qs)** with **+4** for correct and **-1** for wrong.\n\n"
            "**தமிழ் குறிப்பு:** நீட் தேர்வில் உயிரியலுக்கு (360 மதிப்பெண்கள்) NCERT பாடப்புத்தகத்தை வரிக்கு வரி படிக்கவும். "
            "தெரியாத வினாக்களில் யூகத்தின் அடிப்படையில் விடையளித்து -1 எதிர்மறை மதிப்பெண் இழப்பதைத் தவிர்க்கவும்."
        )

    corr = q.get("correct", "")
    subj = q.get("subject", "")
    chap = q.get("chapter", "")
    ncert = q.get("ncertRef", "")
    exp_en = q.get("explanation_en", "")
    exp_ta = q.get("explanation_ta", "")
    key_pt = q.get("ncert_key_point", "")
    traps = q.get("trap_breakdown") or {}
    lower_msg = (student_msg or "").lower()

    if "trap" in lower_msg or "wrong" in lower_msg or "தவறு" in lower_msg:
        trap_lines = [f"- **Option {k}:** {v}" for k, v in traps.items()]
        return (
            f"**-1 Negative Mark Trap Analysis — {subj} ({chap})**\n\n"
            + "\n".join(trap_lines)
            + f"\n\n**Verified Correct Option:** **{corr}**\n"
            + f"**தமிழ் விளக்கம்:** {exp_ta}"
        )

    if lang_intent in ("tamil_script", "tamil_requested", "tamil_preferred"):
        return (
            f"**{subj} — {chap} ({ncert})**\n\n"
            f"**தமிழ் விளக்கம்:** {exp_ta}\n\n"
            f"**சரியான விடை:** **விருப்பம் {corr}**\n\n"
            f"**NCERT முக்கிய விதி (English Reference):** {key_pt}"
        )

    choice_note = ""
    if user_choice:
        if user_choice == corr:
            choice_note = f"Your selection **{user_choice}** is **Correct (+4 Marks)**.\n\n"
        elif user_choice in traps:
            choice_note = f"Your selection **{user_choice}** triggers a **-1 Negative Mark Trap**: {traps[user_choice]}\n\n"

    return (
        f"**{subj} — {chap}** ({ncert})\n\n"
        f"{choice_note}"
        f"**Step-by-Step NCERT Explanation:** {exp_en}\n\n"
        f"**தமிழ் விளக்கம்:** {exp_ta}\n\n"
        f"**Topper Rule:** {key_pt} | **Correct Bubble:** **{corr}**"
    )


def generate_gemini_coach_reply(payload: dict, custom_api_key: str = ""):
    student_id = str(payload.get("student_id") or "default_student").strip()
    student_name = str(payload.get("student_name") or "Student").strip()
    q_data = payload.get("question_data") or {}
    q_num = payload.get("question_number") or q_data.get("id") or 1
    user_choice = str(payload.get("user_choice") or "").strip().upper()
    student_msg = str(payload.get("student_message") or "Explain this question step by step.").strip()
    ui_lang_pref = str(payload.get("language_pref") or "bilingual").strip()
    chat_history = payload.get("chat_history") or []

    lang_intent = detect_language_intent(student_msg, ui_lang_pref)
    prompt_str = build_neet_gemini_prompt(
        q_data=q_data,
        question_number=q_num,
        user_choice=user_choice,
        student_msg=student_msg,
        student_name=student_name,
        lang_intent=lang_intent,
        recent_history=chat_history,
    )

    api_key = (custom_api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or "").strip()
    reply_text, engine_used = (None, None)

    if api_key:
        reply_text, engine_used = call_gemini_rest_api(prompt_str, api_key)

    if not reply_text:
        reply_text, engine_used = call_local_agy_gemini(prompt_str)

    if not reply_text:
        reply_text = build_offline_bilingual_fallback(q_data, q_num, user_choice, student_msg, lang_intent)
        engine_used = "ncert_bilingual_engine"

    # Strip any accidental emoji characters to keep editorial medical formatting clean
    reply_text = re.sub(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", "", reply_text).strip()

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    qid_val = int(q_data["id"]) if isinstance(q_data, dict) and str(q_data.get("id", "")).isdigit() else None
    subj_val = q_data.get("subject", "") if isinstance(q_data, dict) else ""

    with DB_LOCK:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO coach_interactions (
                student_id, student_name, question_id, subject, user_choice,
                language_detected, student_message, coach_reply, engine_used, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                student_id,
                student_name,
                qid_val,
                subj_val,
                user_choice,
                lang_intent,
                student_msg,
                reply_text,
                engine_used,
                now_str,
            ),
        )
        conn.commit()
        conn.close()

    return {
        "reply": reply_text,
        "engine": engine_used,
        "language_detected": lang_intent,
    }


class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


class NEETMasteryHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def log_message(self, fmt, *args):
        # Clean concise server log
        sys.stderr.write(f"[NEET-Server] {self.address_string()} - {fmt % args}\n")

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Gemini-Key")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

    def _send_json(self, status_code: int, data: dict):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json_body(self) -> dict:
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length) if length > 0 else b"{}"
        return json.loads(raw.decode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_HEAD(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path.startswith("/api/"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            return
        if parsed.path == "/":
            self.path = "/index.html"
        return super().do_HEAD()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        qs = urllib.parse.parse_qs(parsed.query)

        if path == "/api/health":
            has_env_key = bool(os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"))
            has_agy = os.path.exists(AGY_BIN)
            with DB_LOCK:
                conn = sqlite3.connect(DB_PATH)
                cur = conn.cursor()
                cur.execute("SELECT COUNT(*) FROM exam_attempts")
                attempts_cnt = cur.fetchone()[0]
                cur.execute("SELECT COUNT(*) FROM coach_interactions")
                chats_cnt = cur.fetchone()[0]
                conn.close()
            self._send_json(
                200,
                {
                    "status": "ok",
                    "exam": "NEET-UG Tamil Nadu Mastery Hub",
                    "verified_questions": len(QUESTIONS_BY_ID),
                    "gemini_engine": (
                        "google_gemini_api"
                        if has_env_key
                        else ("gemini_agy_cli" if has_agy else "ncert_bilingual_fallback")
                    ),
                    "total_attempts_logged": attempts_cnt,
                    "total_coach_chats_logged": chats_cnt,
                },
            )
            return

        if path == "/api/profile":
            student_id = (qs.get("student_id") or ["default_student"])[0]
            with DB_LOCK:
                conn = sqlite3.connect(DB_PATH)
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()
                cur.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
                row = cur.fetchone()
                conn.close()
            self._send_json(200, {"profile": dict(row) if row else None})
            return

        if path == "/api/scores":
            student_id = (qs.get("student_id") or [""])[0].strip()
            fetch_all = (qs.get("all") or ["0"])[0] == "1"
            with DB_LOCK:
                conn = sqlite3.connect(DB_PATH)
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()
                if fetch_all or not student_id:
                    cur.execute("SELECT * FROM exam_attempts ORDER BY id DESC LIMIT 100")
                else:
                    cur.execute(
                        "SELECT * FROM exam_attempts WHERE student_id = ? ORDER BY id DESC LIMIT 100",
                        (student_id,),
                    )
                rows = [dict(r) for r in cur.fetchall()]

                cur.execute("SELECT COUNT(*) FROM coach_interactions")
                total_chats = cur.fetchone()[0]
                conn.close()

            mistake_set = set()
            subject_Rollup = {
                s: {"correct": 0, "wrong": 0, "unanswered": 0, "total": 0}
                for s in ("Physics", "Chemistry", "Botany", "Zoology")
            }
            for r in rows:
                sb = json.loads(r.pop("subject_breakdown_json", "{}"))
                r["subject_breakdown"] = sb
                r.pop("answers_json", None)
                wids = json.loads(r.pop("wrong_question_ids_json", "[]"))
                r["wrong_question_ids"] = wids
                for wid in wids:
                    mistake_set.add(int(wid))
                for s_name, s_stats in sb.items():
                    if s_name in subject_Rollup:
                        subject_Rollup[s_name]["correct"] += s_stats.get("correct", 0)
                        subject_Rollup[s_name]["wrong"] += s_stats.get("wrong", 0)
                        subject_Rollup[s_name]["unanswered"] += s_stats.get("unanswered", 0)
                        subject_Rollup[s_name]["total"] += s_stats.get("total", 0)

            summary = {
                "total_attempts": len(rows),
                "best_projected_720": max((r["projected_720"] for r in rows), default=0),
                "latest_projected_720": rows[0]["projected_720"] if rows else 0,
                "average_projected_720": round(sum(r["projected_720"] for r in rows) / len(rows), 1) if rows else 0,
                "total_negative_marks_lost": sum(r["negative_marks_lost"] for r in rows),
                "total_coach_interactions": total_chats,
                "subject_rollup": subject_Rollup,
                "mistake_question_ids": sorted(mistake_set),
            }
            self._send_json(200, {"summary": summary, "attempts": rows})
            return

        if path == "/":
            self.path = "/index.html"
        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/profile":
            try:
                body = self._read_json_body()
                student_id = str(body.get("student_id") or "default_student").strip()
                name = str(body.get("name") or "NEET Aspirant").strip()
                district = str(body.get("district") or "Chennai").strip()
                board = str(body.get("board") or "TN State Board (Samacheer Kalvi)").strip()
                quota_category = str(body.get("quota_category") or "BC (85% TN State Quota)").strip()
                language_pref = str(body.get("language_pref") or "bilingual").strip()
                target_score = max(300, min(720, int(body.get("target_score") or 650)))
                now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                with DB_LOCK:
                    conn = sqlite3.connect(DB_PATH)
                    cur = conn.cursor()
                    cur.execute(
                        """
                        INSERT INTO students (
                            student_id, name, district, board, quota_category,
                            language_pref, target_score, created_at, updated_at
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ON CONFLICT(student_id) DO UPDATE SET
                            name=excluded.name,
                            district=excluded.district,
                            board=excluded.board,
                            quota_category=excluded.quota_category,
                            language_pref=excluded.language_pref,
                            target_score=excluded.target_score,
                            updated_at=excluded.updated_at
                        """,
                        (
                            student_id,
                            name,
                            district,
                            board,
                            quota_category,
                            language_pref,
                            target_score,
                            now_str,
                            now_str,
                        ),
                    )
                    conn.commit()
                    conn.close()
                self._send_json(200, {"status": "saved", "student_id": student_id, "name": name})
            except Exception as exc:
                self._send_json(400, {"error": str(exc)})
            return

        if path == "/api/submit_attempt":
            try:
                body = self._read_json_body()
                graded = grade_exam_submission(body)
                self._send_json(200, graded)
            except Exception as exc:
                self._send_json(400, {"error": str(exc)})
            return

        if path == "/api/chat":
            try:
                body = self._read_json_body()
                custom_key = self.headers.get("X-Gemini-Key", "").strip()
                result = generate_gemini_coach_reply(body, custom_api_key=custom_key)
                self._send_json(200, result)
            except Exception as exc:
                self._send_json(500, {"error": str(exc)})
            return

        self._send_json(404, {"error": "Endpoint not found"})


if __name__ == "__main__":
    init_db()
    sync_mentor_ledger()
    with ThreadedHTTPServer(("", PORT), NEETMasteryHandler) as httpd:
        print(f"Tamil Nadu NEET Mastery Hub & Gemini Coach running at http://localhost:{PORT}")
        sys.stdout.flush()
        httpd.serve_forever()
