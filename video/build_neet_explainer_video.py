#!/usr/bin/env python3
"""
Builds the Official 1080p Full HD (1920x1080, 24fps) Bilingual Explainer Video for:
  "TAMIL NADU NEET-UG 720 MASTERY HUB & BILINGUAL GEMINI AI COACH"
Features:
  - Spoken Audio: Natural Indian Tamil Studio Neural Voiceover (edge-tts ta-IN-PallaviNeural, rate=-5%)
  - Subtitles:
      1. Burned-in Cinema-Grade English Subtitles (synced sentence-by-sentence to the Tamil voiceover)
      2. External YouTube .srt (tamil_nadu_neet_explainer_en.srt) and WebVTT (.vtt) files
  - Visuals:
      - Gemini-generated 16:9 illustrations (Madras Medical College sunrise dream, Holographic AI Coach, Doctor Coat Finale)
      - 7 Real High-DPI (3840x2160 -> 1920x1080) live screenshots of all 4 tabs and interactive modes of the app
      - 3-stage progressive card highlights & UI callouts per scene synced to each sentence
  - Strict Privacy/Branding Rule: Zero mention of any personal names or unrelated domains.
"""

import asyncio
import html
import math
import os
import subprocess
import wave
from pathlib import Path
import numpy as np
import edge_tts

VIDEO_DIR = Path("/Users/thameema/git/neet-prep/video")
ASSETS_DIR = VIDEO_DIR / "assets"
BUILD_DIR = VIDEO_DIR / "build"
OUTPUT_MP4 = VIDEO_DIR / "tamil_nadu_neet_explainer.mp4"
OUTPUT_SRT = VIDEO_DIR / "tamil_nadu_neet_explainer_en.srt"
OUTPUT_VTT = VIDEO_DIR / "tamil_nadu_neet_explainer_en.vtt"

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TAMIL_VOICE = "ta-IN-PallaviNeural"
VOICE_RATE = "-5%"

SCENES = [
    # -------------------------------------------------------------------------
    # SCENE 01: INTRO — THE TAMIL NADU MEDICAL DREAM & PLATFORM OVERVIEW
    # -------------------------------------------------------------------------
    {
        "idx": 1,
        "tab_badge": "INTRO • TAMIL NADU NEET-UG 720 MASTERY HUB",
        "title_en": "Turn Your Government Medical College Dream Into Reality",
        "title_ta": "தமிழக மாணவர்களின் மருத்துவக் கனவை நனவாக்கும் முழுமையான நீட் பயிற்சித் தளம்",
        "bg_image": str(ASSETS_DIR / "bg_intro_medical_dream.jpg"),
        "layout": "hero_intro",
        "accent": "#14b8a6",
        "accent2": "#f59e0b",
        "segments": [
            {
                "step": "01 • BUILT FOR TAMIL NADU ASPIRANTS",
                "card_title": "Complete NEET-UG 720 System",
                "card_body": "Designed specifically for Tamil Nadu State Board & CBSE students targeting top Government Medical Colleges.",
                "card_badge": "Target: 650+ to 720/720",
                "vo_ta": "வணக்கம்! தமிழக மாணவர்களின் மருத்துவக் கனவை நனவாக்க உருவாக்கப்பட்ட, தமிழ்நாடு நீட் எழுநூற்றி இருபது மாஸ்டரி தளத்திற்கு உங்களை அன்புடன் வரவேற்கிறோம்.",
                "sub_en": "Welcome to the Tamil Nadu NEET 720 Mastery Hub — built to turn every Tamil Nadu student's medical dream into reality.",
            },
            {
                "step": "02 • BEYOND ROTE MEMORIZATION",
                "card_title": "NCERT Depth + OMR Precision",
                "card_body": "Cracking MMC, Stanley, or Madurai Medical College requires line-by-line NCERT clarity and zero negative-mark traps.",
                "card_badge": "+4 Correct • -1 Negative Trap Control",
                "vo_ta": "மெட்ராஸ் மருத்துவக் கல்லூரி உள்ளிட்ட அரசு மருத்துவக் கல்லூரிகளில் இடம் பிடிக்க, வெறும் மனப்பாடம் மட்டும் போதாது; என்.சி.இ.ஆர்.டி ஆழமான புரிதலும், துல்லியமான ஓ.எம்.ஆர் பயிற்சியும் அவசியம்.",
                "sub_en": "Securing a seat in top Government Medical Colleges like MMC requires more than memorization — it demands deep NCERT mastery and precision OMR practice.",
            },
            {
                "step": "03 • ALL-IN-ONE BILINGUAL PLATFORM",
                "card_title": "7,484 Verified Qs + Gemini AI Coach",
                "card_body": "Combines 40 official past papers, NCERT Exemplar banks, OMR mock exams, score tracking, and a 24/7 Tamil + English AI Coach.",
                "card_badge": "English + தமிழ் Bilingual",
                "vo_ta": "அதற்காகவே, ஏழாயிரத்து நானூற்றுக்கும் மேற்பட்ட அதிகாரப்பூர்வ வினாக்கள் மற்றும் இருமொழி ஜெமினி ஏ.ஐ ஆசிரியருடன் இந்த தளம் வடிவமைக்கப்பட்டுள்ளது.",
                "sub_en": "That is why this platform combines 7,484 verified NEET questions with a live bilingual Tamil and English Gemini AI Coach.",
            },
        ],
    },
    # -------------------------------------------------------------------------
    # SCENE 02: TAB 1A — EXAM WORKSPACE, NTA 180-Q OMR SHEET & BILINGUAL SWITCH
    # -------------------------------------------------------------------------
    {
        "idx": 2,
        "tab_badge": "TAB 1 • EXAM & COACH WORKSPACE (MOCK OMR MODE)",
        "title_en": "Authentic NTA 180-Question OMR Mock Workspace",
        "title_ta": "புதிய NTA 180-வினா முறைப்படி முழு மாதிரித் தேர்வு மற்றும் OMR பயிற்சி",
        "bg_image": str(ASSETS_DIR / "screen_01_workspace_omr.png"),
        "layout": "screen_showcase",
        "accent": "#0ea5e9",
        "accent2": "#10b981",
        "callout": {"x": 28, "y": 145, "w": 225, "h": 760, "label": "LIVE NTA OMR BUBBLE SHEET"},
        "segments": [
            {
                "step": "TAB 1 • STRICT NTA 180-IN-180 FORMAT",
                "card_title": "180 Compulsory Questions",
                "card_body": "Simulates the latest post-Section-B NTA exam pattern: 45 Physics, 45 Chemistry, 45 Botany, and 45 Zoology questions in 180 minutes.",
                "card_badge": "180 Mins Live Countdown",
                "vo_ta": "முதல் பகுதியான எக்ஸாம் ஒர்க்ஸ்பேஸில், புதிய என்.டி.ஏ விதிமுறைப்படி நூற்றி எண்பது நிமிடங்களில் நூற்றி எண்பது கட்டாய வினாக்களைக் கொண்ட முழு மாதிரித் தேர்வுகளை எழுதலாம்.",
                "sub_en": "In Tab 1 — the Exam Workspace — you can take full-length Mock Exams following NTA's strict 180-question, 180-minute compulsory pattern.",
            },
            {
                "step": "INSTANT LANGUAGE SWITCHER",
                "card_title": "English + தமிழ் Side-by-Side",
                "card_body": "Toggle between Bilingual (EN + தமிழ்), English Only, or Tamil Primary mode at any moment without losing your exam progress.",
                "card_badge": "Zero Language Barrier",
                "vo_ta": "ஒவ்வொரு வினாவையும் ஆங்கிலம் மற்றும் தமிழில் உடனடியாக மாற்றிப் படிக்கலாம்; இடதுபுறம் உள்ள ஓ.எம்.ஆர் தாளில் உங்கள் விடைகள் உடனுக்குடன் பதிவாகும்.",
                "sub_en": "Switch any question instantly between English, Tamil, or Bilingual view, while tracking every bubble on the live NTA OMR sheet on the left.",
            },
            {
                "step": "SUBJECT PILLS & REVIEW PALETTE",
                "card_title": "4-Subject Smart Navigation",
                "card_body": "Jump between Physics, Chemistry, Botany, and Zoology with 1 click, flag doubtful items for review, and master OMR speed.",
                "card_badge": "Physics • Chem • Botany • Zoology",
                "vo_ta": "இயற்பியல், வேதியியல், தாவரவியல் மற்றும் விலங்கியல் என நான்கு பாடங்களுக்கும் தனித்தனியாக வினாக்களைப் பிரித்துப் பயிற்சி செய்யலாம்.",
                "sub_en": "Filter seamlessly across Physics, Chemistry, Botany, and Zoology, mark questions for review, and master real exam time management.",
            },
        ],
    },
    # -------------------------------------------------------------------------
    # SCENE 03: TAB 1B — GUIDED PRACTICE MODE & -1 NEGATIVE MARK TRAP BOX
    # -------------------------------------------------------------------------
    {
        "idx": 3,
        "tab_badge": "TAB 1 • GUIDED PRACTICE & -1 NEGATIVE MARK TRAP ELIMINATOR",
        "title_en": "Eliminate -1 Negative Marks With Instant NCERT Trap Analysis",
        "title_ta": "நெகட்டிவ் மதிப்பெண்களைத் (-1) தவிர்க்க உதவும் உடனடி NCERT விளக்கம்",
        "bg_image": str(ASSETS_DIR / "screen_02_practice_trap_box.png"),
        "layout": "screen_showcase",
        "accent": "#f43f5e",
        "accent2": "#fbbf24",
        "callout": {"x": 280, "y": 540, "w": 860, "h": 350, "label": "VERIFIED NCERT DERIVATION & -1 TRAP BOX"},
        "segments": [
            {
                "step": "THE #1 SCORE KILLER IN NEET",
                "card_title": "+4 Correct vs -1 Wrong",
                "card_body": "Losing 15 to 20 marks to careless -1 negative bubbles can drop a student from a top Chennai college to missing the cutoff.",
                "card_badge": "Protect Every Single Mark",
                "vo_ta": "நீட் தேர்வில் சரியான விடைக்கு நான்கு மதிப்பெண்கள் கிடைக்கும்; ஆனால் தவறான விடைக்கு மைனஸ் ஒன்று என நெகட்டிவ் மதிப்பெண் குறைக்கப்படும்.",
                "sub_en": "In NEET, every correct answer awards +4 marks, while every wrong bubble costs a -1 negative mark penalty.",
            },
            {
                "step": "INSTANT BILINGUAL VERIFICATION",
                "card_title": "Exact NCERT Page & Chapter Ref",
                "card_body": "In Practice Mode, tap 'Check Answer' to see the exact Class 11/12 NCERT reference, English derivation, தமிழ் விளக்கம், and Topper Rule.",
                "card_badge": "100% NCERT Verified",
                "vo_ta": "இதைத் தவிர்க்க, பிராக்டிஸ் மோடில் உள்ள செக் ஆன்சர் பொத்தானை அழுத்தியவுடன், என்.சி.இ.ஆர்.டி புத்தக ஆதாரத்துடன் தமிழ் மற்றும் ஆங்கில விளக்கம் தோன்றும்.",
                "sub_en": "In Guided Practice Mode, clicking 'Check Answer' immediately reveals the exact NCERT textbook reference with step-by-step English and Tamil explanations.",
            },
            {
                "step": "DISTRACTOR TRAP BREAKDOWN",
                "card_title": "Why Other Bubbles Fail (-1 Trap)",
                "card_body": "Our signature red Trap Box dissects every wrong option (A/B/C/D) so you immediately spot NCERT word twists and unit conversion traps.",
                "card_badge": "Zero Repeat Mistakes",
                "vo_ta": "மற்ற மூன்று தவறான விருப்பங்கள் ஏன் தவறு என்பதையும், மாணவர்கள் எங்கே ஏமாறுவார்கள் என்பதையும் ட்ராப் பாக்ஸ் தெளிவாகக் காட்டுகிறது.",
                "sub_en": "Even better, the '-1 Negative Mark Trap Box' explains why each distractor option fails so you never fall for the same exam trap twice.",
            },
        ],
    },
    # -------------------------------------------------------------------------
    # SCENE 04: TAB 1C — LIVE 24/7 BILINGUAL GEMINI AI NEET COACH
    # -------------------------------------------------------------------------
    {
        "idx": 4,
        "tab_badge": "AI TUTOR • 24/7 BILINGUAL GEMINI AI NEET COACH (தமிழ் + ENGLISH)",
        "title_en": "Your Personal 24/7 Gemini AI NEET Coach in Tamil, English & Tanglish",
        "title_ta": "தமிழ், ஆங்கிலம் மற்றும் தங்லீஷில் சந்தேகங்களைத் தீர்க்கும் ஜெமினி ஏ.ஐ ஆசிரியர்",
        "bg_image": str(ASSETS_DIR / "screen_03_ai_coach_tamil.png"),
        "secondary_image": str(ASSETS_DIR / "bg_ai_coach_concept.jpg"),
        "layout": "screen_showcase",
        "accent": "#8b5cf6",
        "accent2": "#14b8a6",
        "callout": {"x": 1155, "y": 55, "w": 420, "h": 890, "label": "LIVE BILINGUAL GEMINI AI COACH"},
        "segments": [
            {
                "step": "ASK IN TAMIL, ENGLISH OR TANGLISH",
                "card_title": "Context-Aware AI Tutoring",
                "card_body": "The Gemini AI Coach automatically reads the active question, all 4 options, and the bubble you selected before answering your doubt.",
                "card_badge": "Live Gemini AI Engine",
                "vo_ta": "ஒரு வினாவில் சந்தேகம் வந்தால், வலதுபுறம் உள்ள ஜெமினி ஏ.ஐ நீட் பயிற்சியாளரிடம் தமிழ், ஆங்கிலம் அல்லது தங்லீஷில் நேரடியாகக் கேட்கலாம்.",
                "sub_en": "Whenever you have a doubt on any question, ask the built-in Gemini AI NEET Coach directly in Tamil, English, or Tanglish.",
            },
            {
                "step": "5 ONE-TAP SMART COACHING CHIPS",
                "card_title": "Shortcuts, Traps & New MCQs",
                "card_body": "Tap 'Step-by-Step', 'தமிழில் விளக்குக', '-1 Trap Check', 'NCERT Shortcut', or 'Similar MCQ' to generate a fresh test question on the spot.",
                "card_badge": "Instant Concept Mastery",
                "vo_ta": "ஸ்டெப்-பை-ஸ்டெப் கணக்கீடு, என்.சி.இ.ஆர்.டி குறுக்குவழி, அல்லது அதே பாடத்திலிருந்து புதிய பயிற்சி வினா என எதை வேண்டுமானாலும் ஒரு கிளிக்கில் பெறலாம்.",
                "sub_en": "Use one-tap quick chips for Step-by-Step derivations, Tamil explanations, NCERT memory shortcuts, or a brand-new similar MCQ to test yourself.",
            },
            {
                "step": "PERSONAL MENTOR AT HOME",
                "card_title": "Never Stay Stuck on Physics or Bio",
                "card_body": "Bridges the gap between Samacheer Kalvi terminology and English NCERT terms with patient, encouraging bilingual guidance.",
                "card_badge": "24/7 Personal NEET Mentor",
                "vo_ta": "இது இருபத்தி நான்கு மணி நேரமும் உங்களுடன் இருக்கும் ஒரு தனிப்பட்ட நீட் ஆசிரியரைப் போல செயல்படுகிறது.",
                "sub_en": "It acts like a personal 24/7 NEET subject expert sitting right beside you through every single practice session.",
            },
        ],
    },
    # -------------------------------------------------------------------------
    # SCENE 05: TAB 2A — 27-YEAR OFFICIAL PAST PAPERS ARCHIVE (2000–2026)
    # -------------------------------------------------------------------------
    {
        "idx": 5,
        "tab_badge": "TAB 2 • 27-YEAR OFFICIAL PAST PAPERS ARCHIVE (2000–2026)",
        "title_en": "40 Official NEET, Re-NEET, AIPMT & Tamil Medium Booklets (2000–2026)",
        "title_ta": "27 ஆண்டுகால அதிகாரப்பூர்வ நீட், AIPMT மற்றும் தமிழ் வழி வினாத்தாள்கள் (2000–2026)",
        "bg_image": str(ASSETS_DIR / "screen_04b_official_papers_grid.png"),
        "layout": "screen_showcase",
        "accent": "#10b981",
        "accent2": "#38bdf8",
        "callout": {"x": 210, "y": 120, "w": 1160, "h": 770, "label": "40 OFFICIAL EXAM PAPERS + DISPUTED KEYS DOSSIER"},
        "segments": [
            {
                "step": "5,968 OFFICIAL PAST QUESTIONS",
                "card_title": "40 Authentic Exam Booklets",
                "card_body": "Solve complete papers from NEET 2026, Re-NEET 2026, NEET 2025, NEET 2024, down to classic 2000–2012 CBSE AIPMT Prelims & Mains.",
                "card_badge": "2000–2026 Complete Archive",
                "vo_ta": "இரண்டாவது டேப் ஆன பாஸ்ட் பேப்பர்ஸ் பகுதியில், இரண்டாயிரம் முதல் இரண்டாயிரத்து இருபத்தி ஆறு வரையிலான நாற்பது அதிகாரப்பூர்வ நீட் மற்றும் ஏ.ஐ.பி.எம்.டி வினாத்தாள்கள் உள்ளன.",
                "sub_en": "Tab 2 — the Past Papers Archive — houses 40 official NEET, Re-NEET, and classic AIPMT exam papers spanning 27 years from 2000 to 2026.",
            },
            {
                "step": "OFFICIAL NTA TAMIL BOOKLETS",
                "card_title": "2018–2021 தமிழ் வழி வினாத்தாள்கள்",
                "card_body": "Includes 651 authentic questions from official NTA Tamil Medium booklets plus 45-question dynamic subject sprints.",
                "card_badge": "651 Official தமிழ் PYQs",
                "vo_ta": "இதில் இரண்டாயிரத்து பதினெட்டு முதல் இரண்டாயிரத்து இருபத்தி ஒன்று வரையிலான அதிகாரப்பூர்வ என்.டி.ஏ தமிழ் வழி வினாத்தாள்களும் முழுமையாக இணைக்கப்பட்டுள்ளன.",
                "sub_en": "It also includes official NTA Tamil Medium question booklets from 2018 to 2021 alongside 27-year subject-wise 45-question sprints.",
            },
            {
                "step": "SUPREME COURT & BONUS (+4) MODULE",
                "card_title": "Disputed & Multi-Key NTA Rulings",
                "card_body": "Master the exact 2024–2026 questions adjudicated by the Supreme Court & IIT-Delhi panel, +4 dropped bonus items, and dual-key rulings.",
                "card_badge": "SC Landmark & Multi-Key Grading",
                "vo_ta": "மேலும், உச்ச நீதிமன்றத் தீர்ப்பு பெற்ற வினாக்கள் மற்றும் போனஸ் நான்கு மதிப்பெண் வழங்கப்பட்ட சர்ச்சைக்குரிய வினாக்களுக்கும் தனிப் பயிற்சித் தொகுப்பு உள்ளது.",
                "sub_en": "A dedicated module even lets you practice landmark Supreme Court adjudicated questions, +4 bonus dropped items, and multi-key NTA questions.",
            },
        ],
    },
    # -------------------------------------------------------------------------
    # SCENE 06: TAB 2B — NCERT EXEMPLAR, LINE-BY-LINE & COACHING MOCKS
    # -------------------------------------------------------------------------
    {
        "idx": 6,
        "tab_badge": "TAB 2 • NCERT EXEMPLAR, LINE-BY-LINE & COACHING MOCK SERIES",
        "title_en": "1,436 NCERT Exemplar, Line-by-Line & NTA Abhyas Coaching Questions",
        "title_ta": "NCERT Exemplar, வரிக்கு வரி உயிரியல் மற்றும் NTA Abhyas மாதிரித் தேர்வுகள்",
        "bg_image": str(ASSETS_DIR / "screen_04_pyq_exemplar_hub.png"),
        "layout": "screen_showcase",
        "accent": "#f59e0b",
        "accent2": "#14b8a6",
        "callout": {"x": 210, "y": 340, "w": 1160, "h": 540, "label": "5 DEDICATED EXEMPLAR, LINE-BY-LINE & COACHING MODULES"},
        "segments": [
            {
                "step": "709 NCERT EXEMPLAR LEVEL-4 MCQS",
                "card_title": "Class 11 & 12 Analytical Bank",
                "card_body": "Covers all 40 Class 11 & 12 Biology chapters with Level-4 conceptual reasoning, exception analysis, and comparative NCERT traps.",
                "card_badge": "709 Level-4 Exemplar Qs",
                "vo_ta": "முந்தைய ஆண்டு வினாத்தாள்கள் மட்டுமின்றி, ஆயிரத்து நானூற்றுக்கும் மேற்பட்ட என்.சி.இ.ஆர்.டி எக்ஸம்பிளர் மற்றும் கோச்சிங் மாதிரி வினாக்களும் இதில் உள்ளன.",
                "sub_en": "Beyond past papers, the archive features over 1,430 NCERT Exemplar, Textbook Back-Exercise, and Coaching Mock Test questions.",
            },
            {
                "step": "NCERT LINE-BY-LINE PAGE MASTERY",
                "card_title": "Exact NCERT Sentence Citations",
                "card_body": "342 page-by-page Biology micro-drills that quote the exact NCERT textbook sentence so you never miss a Statement I/II twist.",
                "card_badge": "342 Line-by-Line Bio Qs",
                "vo_ta": "பதினொன்று மற்றும் பன்னிரண்டாம் வகுப்பு உயிரியலுக்கான வரிக்கு வரி என்.சி.இ.ஆர்.டி வினாக்கள், புத்தகத்தின் நேரடி மேற்கோள்களுடன் வழங்கப்பட்டுள்ளன.",
                "sub_en": "Practice Class 11 and 12 NCERT Line-by-Line Biology questions complete with exact textbook sentence citations and statement-twist checks.",
            },
            {
                "step": "NTA ABHYAS & COACHING PCB DRILLS",
                "card_title": "180-Q Full Mock + Physics Pack",
                "card_body": "Includes a full 180-question NTA Abhyas CBT simulation and a 205-question physics-heavy coaching test-series pack with full derivations.",
                "card_badge": "385 Coaching & Abhyas Qs",
                "vo_ta": "என்.டி.ஏ அப்யாஸ் நூற்றி எண்பது வினா முழு மாதிரித் தேர்வு மற்றும் இயற்பியல் சிறப்புப் பயிற்சித் தொகுப்புகள் உங்கள் வேகத்தை பல மடங்கு உயர்த்தும்.",
                "sub_en": "Full 180-question NTA Abhyas CBT mocks and physics-heavy coaching test packs build the speed needed for tough exam papers.",
            },
        ],
    },
    # -------------------------------------------------------------------------
    # SCENE 07: TAB 3 — SCORE & MENTOR TRACKER + ADAPTIVE MISTAKE BANK
    # -------------------------------------------------------------------------
    {
        "idx": 7,
        "tab_badge": "TAB 3 • SCORE & MENTOR TRACKER + ADAPTIVE MISTAKE BANK",
        "title_en": "Live /720 Score Progression, Mistake Bank & TN Medical College Predictor",
        "title_ta": "720 மதிப்பெண் கணிப்பு, தவறு வங்கி (Mistake Bank) மற்றும் அரசு மருத்துவக் கல்லூரி இலக்கு",
        "bg_image": str(ASSETS_DIR / "screen_05_score_tracker.png"),
        "layout": "screen_showcase",
        "accent": "#06b6d4",
        "accent2": "#f43f5e",
        "callout": {"x": 210, "y": 115, "w": 1160, "h": 410, "label": "PROJECTED /720 SCORE, SUBJECT ACCURACY & TN QUOTA TIER"},
        "segments": [
            {
                "step": "AUTOMATIC /720 SCORE PROJECTION",
                "card_title": "Track Every Mock & Practice Run",
                "card_body": "Computes your raw score, accuracy percentage, -1 negative marks lost, subject-wise PCB bars, and projected score out of 720.",
                "card_badge": "Real-Time Analytics Ledger",
                "vo_ta": "மூன்றாவது டேப் ஆன ஸ்கோர் டிராக்கர், நீங்கள் எழுதும் ஒவ்வொரு தேர்வின் மதிப்பெண்ணையும் எழுநூற்றி இருபதுக்கு கணக்கிட்டு துல்லியமாகப் பதிவு செய்கிறது.",
                "sub_en": "Tab 3 — the Score and Mentor Tracker — automatically logs every attempt and projects your standing on the 720-point NEET scale.",
            },
            {
                "step": "TAMIL NADU DMER CUTOFF BENCHMARK",
                "card_title": "85% State & 7.5% Govt Quota Tiers",
                "card_body": "Maps your score against verified TN DMER Round 1 cutoffs for MMC Chennai, Stanley, Kilpauk, Madurai, Coimbatore, and 7.5% Govt School Quota.",
                "card_badge": "TN Govt MBBS Seat Predictor",
                "vo_ta": "உங்கள் மதிப்பெண் அடிப்படையில், தமிழகத்தின் எண்பத்தி ஐந்து சதவீத மாநில ஒதுக்கீடு மற்றும் ஏழரை சதவீத அரசுப் பள்ளி ஒதுக்கீட்டில் எந்த மருத்துவக் கல்லூரி கிடைக்கும் என்பதை உடனே அறியலாம்.",
                "sub_en": "It benchmarks your score against Tamil Nadu's 85% State Quota and 7.5% Government School Quota cutoffs for MMC, Stanley, Madurai, and District GMCs.",
            },
            {
                "step": "ADAPTIVE MISTAKE BANK & WHATSAPP SHARE",
                "card_title": "Turn Weaknesses Into +4 Marks",
                "card_body": "Every wrong question is automatically queued in your Mistake Bank for re-testing, and you can copy a 1-click WhatsApp summary for parents or mentors.",
                "card_badge": "1-Click Mistake Re-Test",
                "vo_ta": "நீங்கள் தவறவிட்ட வினாக்கள் அனைத்தும் மிஸ்டேக் பேங்க் பகுதியில் சேமிக்கப்படுவதால், அவற்றை மீண்டும் எழுதிப் பார்த்துத் தவறுகளைத் திருத்திக் கொள்ளலாம்.",
                "sub_en": "Every wrong answer is saved into your personal Adaptive Mistake Bank so you can re-test weak spots and share a 1-click WhatsApp progress report.",
            },
        ],
    },
    # -------------------------------------------------------------------------
    # SCENE 08: TAB 4 & FINALE — TN NEET GUIDE, 720/720 PLAYBOOK & YOUTUBE HUB
    # -------------------------------------------------------------------------
    {
        "idx": 8,
        "tab_badge": "TAB 4 & FINALE • TN NEET GUIDE, 720/720 TOPPER PLAYBOOK & YOUTUBE HUB",
        "title_en": "720/720 Topper Playbook, Curated Tamil YouTube Hub & Your MBBS Future",
        "title_ta": "720/720 முதன்மை மாணவர்களின் யுக்திகள், சிறந்த YouTube சேனல்கள் மற்றும் உங்கள் மருத்துவ எதிர்காலம்",
        "bg_image": str(ASSETS_DIR / "bg_endcard_doctor.jpg"),
        "secondary_image": str(ASSETS_DIR / "screen_06_tn_guide_youtube.png"),
        "layout": "finale_endcard",
        "accent": "#14b8a6",
        "accent2": "#f59e0b",
        "segments": [
            {
                "step": "TAB 4 • 720/720 TOPPER PLAYBOOK",
                "card_title": "3-Round OMR Time Strategy",
                "card_body": "Learn how Tamil Nadu AIR-1 (720/720) and 7.5% Govt School Quota toppers finish Biology in 45 mins, Chemistry in 50 mins, and Physics in 65 mins.",
                "card_badge": "Proven 720/720 Blueprint",
                "vo_ta": "நான்காவது டேப் ஆன டி.என் நீட் கைடு பகுதியில், எழுநூற்றி இருபதுக்கு எழுநூற்றி இருபது எடுத்த தமிழக முதன்மை மாணவர்களின் நேர மேலாண்மை ரகசியங்கள் தொகுக்கப்பட்டுள்ளன.",
                "sub_en": "Finally, Tab 4 — the TN NEET Guide & YouTube Hub — shares the exact 3-Round OMR timing playbook used by 720/720 Tamil Nadu toppers.",
            },
            {
                "step": "CURATED TAMIL & ENGLISH YOUTUBE HUB",
                "card_title": "Direct Video Tutorials by Topic",
                "card_body": "One-click access to Biology Simplified Tamil, Open Your Mind With Muruga MP, PW Tamil Nadu NEET, Xylem Tamil, Ritu Rattewal, and Physics Wallah.",
                "card_badge": "Tamil + English Video Hub",
                "vo_ta": "மேலும், பயாலஜி சிம்ப்ளிஃபைடு தமிழ், முருகா எம்.பி, மற்றும் பி.டபிள்யூ தமிழ் உள்ளிட்ட சிறந்த யூடியூப் கல்விச் சேனல்களின் பாடவாரியான வீடியோ இணைப்புகளும் ஒரே இடத்தில் உள்ளன.",
                "sub_en": "It also curates the best Tamil and English YouTube tutorials — including Biology Simplified Tamil, Muruga MP, and PW Tamil — linked by subject.",
            },
            {
                "step": "BEGIN YOUR MBBS JOURNEY TODAY",
                "card_title": "Your White Coat Awaits!",
                "card_body": "7,484 Verified Questions • 40 Official Past Papers • NCERT Exemplar & Line-by-Line • 24/7 Bilingual Gemini AI Coach.",
                "card_badge": "வெற்றி நிச்சயம்! All The Best!",
                "vo_ta": "இன்றே உங்கள் பயிற்சியைத் தொடங்குங்கள்; விடாமுயற்சியும் சரியான பயிற்சியும் உங்கள் அரசு மருத்துவக் கல்லூரிக் கனவை நிச்சயம் நனவாக்கும்! வாழ்த்துகள்!",
                "sub_en": "Start practicing today — with 7,484 verified questions, smart OMR analytics, and your bilingual Gemini AI Coach, your medical college dream is within reach!",
            },
        ],
    },
]


def _chrome_screenshot(html_content: str, html_path: Path, png_path: Path):
    html_path.write_text(html_content, encoding="utf-8")
    subprocess.run(
        [
            CHROME_BIN,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--window-size=1920,1080",
            "--force-device-scale-factor=1",
            f"--screenshot={png_path}",
            f"file://{html_path}",
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def _ffprobe_duration(media_path: Path) -> float:
    out = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(media_path),
        ],
        text=True,
    ).strip()
    return float(out)


async def generate_all_voiceovers():
    """Generates individual Tamil MP3 clips for each sentence segment across all 8 scenes."""
    for s in SCENES:
        s_idx = s["idx"]
        for k, seg in enumerate(s["segments"], 1):
            mp3_path = BUILD_DIR / f"vo_s{s_idx:02d}_seg{k}.mp3"
            if not mp3_path.exists() or mp3_path.stat().st_size < 1000:
                comm = edge_tts.Communicate(seg["vo_ta"], TAMIL_VOICE, rate=VOICE_RATE)
                await comm.save(str(mp3_path))
            seg["vo_path"] = mp3_path
            seg["vo_dur"] = _ffprobe_duration(mp3_path)
        print(
            f"   Scene {s_idx:02d} Tamil voiceovers ready: "
            + ", ".join(f"seg{k}={seg['vo_dur']:.2f}s" for k, seg in enumerate(s["segments"], 1))
        )


def render_scene_stage_frame(scene: dict, active_seg_idx: int) -> Path:
    """
    Renders a full 1920x1080 frame for `scene` during `active_seg_idx` (0, 1, or 2):
    - Left/Center (1220px):
        - If layout == 'hero_intro': Full-bleed Gemini Madras Medical College sunrise art with glassmorphic hero banner
        - If layout == 'screen_showcase': Crisp 3D-framed live screenshot of the NEET app with animated highlight ring
        - If layout == 'finale_endcard': Split showcase of Gemini Doctor Finale art + Tab 4 TN Guide screenshot preview
    - Right Column (580px):
        - 3 Progressive Feature Cards (Cards 0..active_seg_idx are lit & active; upcoming cards are dimmed)
    - Bottom Cinema Subtitle Bar (Full-width):
        - Prominent English Subtitle (for YouTube/universal viewers) + synchronized Tamil narration line
    """
    s_idx = scene["idx"]
    seg = scene["segments"][active_seg_idx]
    accent = scene["accent"]
    accent2 = scene["accent2"]
    progress_pct = round(((s_idx - 1 + (active_seg_idx + 1) / 3.0) / len(SCENES)) * 100, 1)

    cards_html = ""
    for i, c in enumerate(scene["segments"]):
        is_current = i == active_seg_idx
        is_past = i < active_seg_idx
        opacity = "1.0" if is_current else ("0.82" if is_past else "0.28")
        border_col = accent if is_current else ("rgba(255,255,255,0.22)" if is_past else "rgba(255,255,255,0.08)")
        bg_col = "rgba(13, 23, 42, 0.95)" if is_current else "rgba(10, 16, 30, 0.78)"
        glow = f"0 14px 36px rgba(0,0,0,0.75), 0 0 24px {accent}44" if is_current else "0 8px 20px rgba(0,0,0,0.5)"
        scale_tf = "scale(1.015)" if is_current else "scale(1.0)"
        cards_html += f"""
        <div class="f-card" style="opacity:{opacity};border-color:{border_col};background:{bg_col};box-shadow:{glow};transform:{scale_tf};">
          <div class="f-card-top">
            <span class="f-step" style="color:{accent2 if is_current else '#94a3b8'};">{html.escape(c['step'])}</span>
            <span class="f-pill" style="border-color:{accent}88;color:{accent};background:{accent}1f;">{html.escape(c['card_badge'])}</span>
          </div>
          <div class="f-card-title">{html.escape(c['card_title'])}</div>
          <div class="f-card-body">{html.escape(c['card_body'])}</div>
        </div>
        """

    # Build left visual area depending on layout
    bg_uri = f"file://{scene['bg_image']}"
    sec_uri = f"file://{scene.get('secondary_image', '')}" if scene.get("secondary_image") else ""

    if scene["layout"] == "hero_intro":
        left_visual_html = f"""
        <div class="hero-visual" style="background-image:url('{bg_uri}');">
          <div class="hero-gradient"></div>
          <div class="hero-floating-badge">
            <div class="hfb-kicker">TAMIL NADU NEET-UG 720 MASTERY HUB</div>
            <div class="hfb-main">7,484 Verified Questions • 40 Past Papers • Bilingual Gemini AI Coach</div>
            <div class="hfb-sub">Physics • Chemistry • Botany • Zoology &nbsp;|&nbsp; English + தமிழ் + Tanglish</div>
          </div>
        </div>
        """
    elif scene["layout"] == "finale_endcard":
        left_visual_html = f"""
        <div class="hero-visual" style="background-image:url('{bg_uri}');">
          <div class="hero-gradient"></div>
          <div class="inset-screen-card">
            <div class="isc-label">TAB 4 • TN NEET GUIDE, 720/720 TOPPER PLAYBOOK &amp; YOUTUBE HUB</div>
            <img src="{sec_uri}" class="isc-img" />
          </div>
          <div class="hero-floating-badge" style="bottom:20px;left:24px;right:24px;">
            <div class="hfb-kicker">READY FOR EVERY TAMIL NADU NEET ASPIRANT</div>
            <div class="hfb-main">100% NCERT Aligned • +4 / -1 OMR Precision • 85% State &amp; 7.5% Govt Quota Tracker</div>
          </div>
        </div>
        """
    else:
        co = scene.get("callout")
        callout_html = ""
        if co:
            callout_html = f"""
            <div class="callout-box" style="left:{co['x']*0.61:.0f}px;top:{co['y']*0.61:.0f}px;width:{co['w']*0.61:.0f}px;height:{co['h']*0.61:.0f}px;border-color:{accent2};">
              <span class="callout-tag" style="background:{accent2};color:#090d16;">{html.escape(co['label'])}</span>
            </div>
            """
        inset_ai_html = ""
        if sec_uri and active_seg_idx == 2:
            inset_ai_html = f"""
            <div class="ai-inset-badge">
              <img src="{sec_uri}" />
              <span>24/7 Bilingual AI Concept Visualizer</span>
            </div>
            """
        left_visual_html = f"""
        <div class="browser-frame">
          <div class="browser-bar">
            <div class="b-dots"><i></i><i></i><i></i></div>
            <div class="b-title">Tamil Nadu NEET-UG 720 Mastery Hub — Interactive Workspace (EN + தமிழ்)</div>
            <div class="b-pill" style="color:{accent};border-color:{accent}66;">LIVE APP VIEW</div>
          </div>
          <div class="browser-screen-wrap">
            <img src="{bg_uri}" class="browser-img" />
            {callout_html}
            {inset_ai_html}
          </div>
        </div>
        """

    html_doc = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px; height: 1080px;
    background: radial-gradient(circle at 20% 15%, #0f2942 0%, #070d19 65%, #04070f 100%);
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", "Noto Sans Tamil", sans-serif;
    color: #f8fafc;
    overflow: hidden;
    position: relative;
  }}
  /* Top Header Strip */
  .top-header {{
    position: absolute;
    top: 22px; left: 42px; right: 42px;
    height: 88px;
    background: rgba(10, 17, 32, 0.90);
    border: 1.5px solid rgba(255, 255, 255, 0.14);
    border-left: 7px solid {accent};
    border-radius: 16px;
    padding: 12px 26px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 12px 32px rgba(0,0,0,0.65);
  }}
  .th-left {{
    display: flex;
    flex-direction: column;
    gap: 3px;
  }}
  .th-badge {{
    font-family: "SF Mono", "Menlo", monospace;
    font-size: 12.5px;
    font-weight: 800;
    letter-spacing: 2px;
    color: {accent};
  }}
  .th-title-en {{
    font-size: 25px;
    font-weight: 900;
    color: #ffffff;
    letter-spacing: -0.3px;
  }}
  .th-title-ta {{
    font-size: 15px;
    font-weight: 600;
    color: #cbd5e1;
  }}
  .th-right {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .scene-counter {{
    background: rgba(20, 184, 166, 0.15);
    border: 1.5px solid {accent};
    border-radius: 12px;
    padding: 8px 16px;
    text-align: center;
  }}
  .sc-lbl {{
    font-size: 10.5px;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: #94a3b8;
  }}
  .sc-val {{
    font-size: 19px;
    font-weight: 900;
    color: #ffffff;
  }}

  /* Main Content Area */
  .main-stage {{
    position: absolute;
    top: 126px;
    left: 42px;
    right: 42px;
    height: 734px;
    display: flex;
    gap: 26px;
  }}
  .left-col {{
    width: 1180px;
    height: 100%;
    position: relative;
  }}
  .right-col {{
    flex: 1;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 14px;
  }}

  /* Hero Intro & Finale Visual */
  .hero-visual {{
    width: 100%;
    height: 100%;
    border-radius: 20px;
    background-size: cover;
    background-position: center;
    border: 2px solid {accent}88;
    box-shadow: 0 20px 50px rgba(0,0,0,0.85);
    position: relative;
    overflow: hidden;
  }}
  .hero-gradient {{
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(5,10,20,0.10) 0%, rgba(5,10,20,0.30) 60%, rgba(5,10,20,0.92) 100%);
  }}
  .hero-floating-badge {{
    position: absolute;
    bottom: 24px; left: 24px; right: 24px;
    background: rgba(8, 14, 28, 0.90);
    border: 1.5px solid {accent}aa;
    border-left: 6px solid {accent2};
    border-radius: 16px;
    padding: 18px 24px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.8);
  }}
  .hfb-kicker {{
    font-family: "SF Mono", monospace;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
    color: {accent2};
    margin-bottom: 4px;
  }}
  .hfb-main {{
    font-size: 23px;
    font-weight: 900;
    color: #ffffff;
  }}
  .hfb-sub {{
    font-size: 15px;
    color: #cbd5e1;
    margin-top: 4px;
  }}

  .inset-screen-card {{
    position: absolute;
    top: 22px; right: 22px;
    width: 560px;
    background: rgba(8, 14, 28, 0.94);
    border: 2px solid {accent2};
    border-radius: 14px;
    padding: 10px;
    box-shadow: 0 18px 40px rgba(0,0,0,0.9);
  }}
  .isc-label {{
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.2px;
    color: {accent2};
    margin-bottom: 6px;
    padding: 0 4px;
  }}
  .isc-img {{
    width: 100%;
    border-radius: 8px;
    display: block;
  }}

  /* Browser Showcase Frame */
  .browser-frame {{
    width: 100%;
    height: 100%;
    background: #0b1324;
    border: 2px solid rgba(255, 255, 255, 0.18);
    border-radius: 18px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    box-shadow: 0 22px 55px rgba(0,0,0,0.85);
  }}
  .browser-bar {{
    height: 42px;
    background: #111c33;
    border-bottom: 1px solid rgba(255,255,255,0.12);
    padding: 0 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .b-dots {{
    display: flex;
    gap: 7px;
  }}
  .b-dots i {{
    width: 11px; height: 11px;
    border-radius: 50%;
    display: inline-block;
  }}
  .b-dots i:nth-child(1) {{ background: #f43f5e; }}
  .b-dots i:nth-child(2) {{ background: #f59e0b; }}
  .b-dots i:nth-child(3) {{ background: #10b981; }}
  .b-title {{
    font-size: 13px;
    font-weight: 700;
    color: #cbd5e1;
  }}
  .b-pill {{
    font-family: "SF Mono", monospace;
    font-size: 11px;
    font-weight: 800;
    border: 1px solid;
    padding: 3px 10px;
    border-radius: 99px;
  }}
  .browser-screen-wrap {{
    flex: 1;
    position: relative;
    background: #f8fafc;
    overflow: hidden;
  }}
  .browser-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
    display: block;
  }}
  .callout-box {{
    position: absolute;
    border: 3.5px solid;
    border-radius: 12px;
    box-shadow: 0 0 0 9999px rgba(4, 9, 20, 0.28), 0 0 25px rgba(245, 158, 11, 0.75);
    pointer-events: none;
  }}
  .callout-tag {{
    position: absolute;
    top: -26px;
    left: 0;
    font-family: "SF Mono", monospace;
    font-size: 11.5px;
    font-weight: 900;
    letter-spacing: 1px;
    padding: 4px 10px;
    border-radius: 6px;
    white-space: nowrap;
  }}
  .ai-inset-badge {{
    position: absolute;
    bottom: 14px;
    left: 14px;
    width: 310px;
    background: rgba(8, 14, 28, 0.94);
    border: 2px solid {accent};
    border-radius: 12px;
    padding: 8px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.85);
    text-align: center;
  }}
  .ai-inset-badge img {{
    width: 100%;
    height: 145px;
    object-fit: cover;
    border-radius: 8px;
    display: block;
    margin-bottom: 5px;
  }}
  .ai-inset-badge span {{
    font-size: 12px;
    font-weight: 800;
    color: #f8fafc;
  }}

  /* Right Column Progressive Cards */
  .f-card {{
    flex: 1;
    border: 2px solid;
    border-radius: 16px;
    padding: 18px 22px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }}
  .f-card-top {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
  }}
  .f-step {{
    font-family: "SF Mono", monospace;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.2px;
  }}
  .f-pill {{
    font-size: 11.5px;
    font-weight: 800;
    padding: 3px 10px;
    border-radius: 99px;
    border: 1px solid;
  }}
  .f-card-title {{
    font-size: 22px;
    font-weight: 900;
    color: #ffffff;
    margin-bottom: 6px;
  }}
  .f-card-body {{
    font-size: 15.5px;
    line-height: 1.45;
    color: #cbd5e1;
  }}

  /* Bottom Cinema Dual Subtitle Bar (English Subtitles + Tamil Voiceover Text) */
  .subtitle-bar {{
    position: absolute;
    bottom: 20px;
    left: 42px;
    right: 42px;
    height: 178px;
    background: rgba(6, 10, 22, 0.95);
    border: 2px solid {accent}aa;
    border-radius: 18px;
    padding: 16px 32px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    box-shadow: 0 18px 45px rgba(0,0,0,0.92), 0 0 28px {accent}33;
  }}
  .sub-ta-row {{
    font-size: 18.5px;
    font-weight: 700;
    color: #5eead4;
    margin-bottom: 8px;
    line-height: 1.35;
    max-width: 1720px;
  }}
  .sub-en-row {{
    font-size: 25.5px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.32;
    max-width: 1740px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.9);
  }}
  .sub-en-tag {{
    display: inline-block;
    background: {accent2};
    color: #090d16;
    font-family: "SF Mono", monospace;
    font-size: 12px;
    font-weight: 900;
    padding: 3px 9px;
    border-radius: 6px;
    margin-right: 10px;
    vertical-align: middle;
    letter-spacing: 1px;
  }}
  .progress-bar {{
    position: absolute;
    bottom: 0;
    left: 0;
    height: 6px;
    width: {progress_pct}%;
    background: linear-gradient(90deg, #14b8a6, #0ea5e9, #f59e0b);
  }}
</style>
</head>
<body>
  <div class="top-header">
    <div class="th-left">
      <div class="th-badge">{html.escape(scene['tab_badge'])}</div>
      <div class="th-title-en">{html.escape(scene['title_en'])}</div>
      <div class="th-title-ta">{html.escape(scene['title_ta'])}</div>
    </div>
    <div class="th-right">
      <div class="scene-counter">
        <div class="sc-lbl">MODULE</div>
        <div class="sc-val">{s_idx:02d} / {len(SCENES):02d}</div>
      </div>
    </div>
  </div>

  <div class="main-stage">
    <div class="left-col">
      {left_visual_html}
    </div>
    <div class="right-col">
      {cards_html}
    </div>
  </div>

  <div class="subtitle-bar">
    <div class="sub-ta-row"><span class="sub-en-tag" style="background:{accent};color:#041019;">தமிழ் AUDIO</span>{html.escape(seg['vo_ta'])}</div>
    <div class="sub-en-row"><span class="sub-en-tag">EN SUBTITLE</span>{html.escape(seg['sub_en'])}</div>
  </div>

  <div class="progress-bar"></div>
</body>
</html>
"""
    html_path = BUILD_DIR / f"s{s_idx:02d}_seg{active_seg_idx+1}.html"
    png_path = BUILD_DIR / f"s{s_idx:02d}_seg{active_seg_idx+1}.png"
    _chrome_screenshot(html_doc, html_path, png_path)
    return png_path


def synthesize_uplifting_bgm(out_wav: Path, duration_sec: float):
    """Synthesizes a warm, inspiring, royalty-free 108 BPM ambient motivational score."""
    sr = 44100
    n_samples = int(duration_sec * sr)
    t = np.linspace(0, duration_sec, n_samples, endpoint=False)

    bpm = 108.0
    beat_sec = 60.0 / bpm
    beat_phase = (t % beat_sec) / beat_sec
    beat_idx = (t / beat_sec).astype(int)
    bar_idx = (t / (beat_sec * 4)).astype(int) % 4

    # Warm C-major / A-minor / F-major / G-major inspirational chord progression
    chords = [
        (261.63, 329.63, 392.00, 523.25),  # C maj
        (220.00, 261.63, 329.63, 440.00),  # A min
        (174.61, 261.63, 349.23, 440.00),  # F maj
        (196.00, 246.94, 392.00, 493.88),  # G maj
    ]
    pad_L = np.zeros_like(t)
    pad_R = np.zeros_like(t)
    for c_i, (f1, f2, f3, f4) in enumerate(chords):
        mask = (bar_idx == c_i).astype(float)
        sig_L = (
            0.35 * np.sin(2 * np.pi * f1 * t)
            + 0.28 * np.sin(2 * np.pi * f2 * t)
            + 0.25 * np.sin(2 * np.pi * f3 * t)
            + 0.18 * np.sin(2 * np.pi * (f4 * 1.002) * t)
        )
        sig_R = (
            0.35 * np.sin(2 * np.pi * (f1 * 0.999) * t)
            + 0.28 * np.sin(2 * np.pi * f2 * t)
            + 0.25 * np.sin(2 * np.pi * (f3 * 1.001) * t)
            + 0.18 * np.sin(2 * np.pi * f4 * t)
        )
        pad_L += mask * sig_L
        pad_R += mask * sig_R

    # Gentle piano-like arpeggio bell notes
    arp_notes = [523.25, 659.25, 783.99, 1046.50, 783.99, 659.25, 587.33, 659.25]
    step_sec = beat_sec / 2.0
    step_phase = (t % step_sec) / step_sec
    step_idx = (t / step_sec).astype(int)
    arp_f = np.take(arp_notes, step_idx % len(arp_notes))
    arp_env = np.exp(-5.5 * step_phase)
    arp = 0.14 * np.sin(2 * np.pi * arp_f * t) * arp_env

    # Soft heartbeat pulse kick
    kick_f = 95.0 * np.exp(-18.0 * beat_phase) + 42.0
    kick = 0.22 * np.sin(2 * np.pi * kick_f * beat_phase * beat_sec) * np.exp(-7.5 * beat_phase)

    mix_L = 0.45 * pad_L + 0.30 * arp + 0.25 * kick
    mix_R = 0.45 * pad_R + 0.30 * np.roll(arp, 350) + 0.25 * kick

    fade_in = np.clip(t / 1.2, 0.0, 1.0)
    fade_out = np.clip((duration_sec - t) / 2.5, 0.0, 1.0)
    env = fade_in * fade_out

    stereo = np.stack([mix_L * env, mix_R * env], axis=-1)
    stereo = np.tanh(stereo * 0.9) * 0.75
    pcm16 = (stereo * 32767).astype(np.int16)

    with wave.open(str(out_wav), "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(pcm16.tobytes())


def _fmt_srt_time(seconds: float) -> str:
    ms = int(round((seconds - int(seconds)) * 1000))
    s = int(seconds) % 60
    m = (int(seconds) // 60) % 60
    h = int(seconds) // 3600
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def _fmt_vtt_time(seconds: float) -> str:
    return _fmt_srt_time(seconds).replace(",", ".")


def build_subsegment_clip(png_path: Path, vo_path: Path, vo_dur: float, out_mp4: Path, is_first_in_scene: bool, is_last_in_scene: bool) -> float:
    """Builds a 1920x1080 24fps MP4 clip for a single sentence segment with smooth transitions."""
    pad_before = 0.30 if is_first_in_scene else 0.15
    pad_after = 0.55 if is_last_in_scene else 0.25
    clip_dur = round(vo_dur + pad_before + pad_after, 3)
    delay_ms = int(pad_before * 1000)

    fade_filters = []
    if is_first_in_scene:
        fade_filters.append("fade=t=in:st=0:d=0.35")
    if is_last_in_scene:
        fade_filters.append(f"fade=t=out:st={max(0.1, clip_dur - 0.35):.3f}:d=0.35")
    v_filter = ",".join(["format=yuv420p"] + fade_filters)

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-loop",
            "1",
            "-t",
            f"{clip_dur:.3f}",
            "-i",
            str(png_path),
            "-i",
            str(vo_path),
            "-filter_complex",
            f"[0:v]{v_filter}[vout];[1:a]adelay={delay_ms}|{delay_ms},apad=whole_dur={clip_dur:.3f},volume=1.45[aout]",
            "-map",
            "[vout]",
            "-map",
            "[aout]",
            "-t",
            f"{clip_dur:.3f}",
            "-r",
            "24",
            "-c:v",
            "libx264",
            "-preset",
            "fast",
            "-crf",
            "18",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-ar",
            "44100",
            "-ac",
            "2",
            str(out_mp4),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return clip_dur


def main():
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    print("1. Generating Tamil Studio Neural Voiceovers (ta-IN-PallaviNeural) for all 24 segments...")
    asyncio.run(generate_all_voiceovers())

    print("2. Rendering 24 1080p Full HD Stage Frames (with burned-in English Subtitles + Tamil Captions)...")
    clip_paths = []
    srt_entries = []
    vtt_entries = ["WEBVTT\n"]
    cur_time = 0.0
    sub_counter = 1

    for s in SCENES:
        s_idx = s["idx"]
        for k, seg in enumerate(s["segments"]):
            png_path = render_scene_stage_frame(s, k)
            seg_mp4 = BUILD_DIR / f"clip_s{s_idx:02d}_seg{k+1}.mp4"
            dur = build_subsegment_clip(
                png_path=png_path,
                vo_path=seg["vo_path"],
                vo_dur=seg["vo_dur"],
                out_mp4=seg_mp4,
                is_first_in_scene=(k == 0),
                is_last_in_scene=(k == len(s["segments"]) - 1),
            )
            clip_paths.append(seg_mp4)

            start_t = cur_time + 0.15
            end_t = cur_time + dur - 0.10
            srt_entries.append(
                f"{sub_counter}\n{_fmt_srt_time(start_t)} --> {_fmt_srt_time(end_t)}\n{seg['sub_en']}\n"
            )
            vtt_entries.append(
                f"{sub_counter}\n{_fmt_vtt_time(start_t)} --> {_fmt_vtt_time(end_t)}\n{seg['sub_en']}\n"
            )
            cur_time += dur
            sub_counter += 1
        print(f"   Built Scene {s_idx:02d}/08 ({s['tab_badge']}) -> cumulative duration: {cur_time:.1f}s")

    OUTPUT_SRT.write_text("\n".join(srt_entries), encoding="utf-8")
    OUTPUT_VTT.write_text("\n".join(vtt_entries), encoding="utf-8")
    print(f"3. Wrote English subtitle tracks: {OUTPUT_SRT.name} & {OUTPUT_VTT.name}")

    concat_list = BUILD_DIR / "concat_list.txt"
    concat_list.write_text("\n".join(f"file '{p}'" for p in clip_paths) + "\n", encoding="utf-8")

    concat_raw = BUILD_DIR / "concat_raw.mp4"
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_list),
            "-c",
            "copy",
            str(concat_raw),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    print(f"4. Synthesizing Uplifting Motivational Background Score ({cur_time:.1f}s)...")
    bgm_wav = BUILD_DIR / "bgm_motivational.wav"
    synthesize_uplifting_bgm(bgm_wav, duration_sec=cur_time + 1.5)

    print("5. Mastering Final 1080p Full HD MP4 (Tamil Voiceover + Burned-In English Subtitles + Soft BGM + Soft-Sub Track)...")
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(concat_raw),
            "-i",
            str(bgm_wav),
            "-i",
            str(OUTPUT_SRT),
            "-filter_complex",
            "[0:a]volume=1.05[vo];[1:a]volume=0.14[bgm];[vo][bgm]amix=inputs=2:duration=first:dropout_transition=0,alimiter=limit=0.95[aout]",
            "-map",
            "0:v",
            "-map",
            "[aout]",
            "-map",
            "2:s",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "256k",
            "-c:s",
            "mov_text",
            "-metadata:s:a:0",
            "language=tam",
            "-metadata:s:s:0",
            "language=eng",
            "-movflags",
            "+faststart",
            str(OUTPUT_MP4),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    size_mb = OUTPUT_MP4.stat().st_size / (1024 * 1024)
    print(f"\nSUCCESS! Built Tamil+English NEET Explainer Video:")
    print(f"  MP4 Video: {OUTPUT_MP4} ({size_mb:.2f} MB, {cur_time:.1f}s, 1920x1080 24fps)")
    print(f"  English SRT: {OUTPUT_SRT}")
    print(f"  English VTT: {OUTPUT_VTT}")


if __name__ == "__main__":
    main()
