#!/usr/bin/env python3
"""
Captures 6 high-resolution 1920x1080 screenshots of the live Tamil Nadu NEET-UG Mastery Hub
(http://localhost:8090) across all 4 tabs and interactive states for the Tamil+English Explainer Video.
Ensures zero mention of any personal/unrelated names (sets student profile to 'Ananya S. (Chennai)').
"""
import os
from playwright.sync_api import sync_playwright

OUT_DIR = "/Users/thameema/git/neet-prep/video/assets"
os.makedirs(OUT_DIR, exist_ok=True)


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
        page = context.new_page()

        page.goto("http://localhost:8090", wait_until="networkidle")
        page.wait_for_timeout(800)

        # Set clean student profile ("Ananya S.") and bilingual mode
        page.evaluate("""() => {
            const prof = {
                student_id: "tn_student_demo",
                name: "Ananya S.",
                district: "Chennai",
                board: "TN State Board (Samacheer Kalvi)",
                quota_category: "BC (85% TN State Quota)",
                language_pref: "bilingual",
                target_score: 680,
                custom_gemini_key: ""
            };
            localStorage.setItem("tn_neet_student_profile_v1", JSON.stringify(prof));
        }""")
        page.reload(wait_until="networkidle")
        page.wait_for_timeout(1000)

        # 1. Screen 1: Tab 1 — Exam & Coach Workspace (Full Mock Mode, Bilingual Question + OMR Bubble Sheet)
        page.evaluate("""() => {
            loadSelectedModule('full_mock_1');
            selectBubble('D');
            state.answers[102] = 'C';
            state.answers[103] = 'B';
            state.answers[104] = 'A';
            state.markedReview[105] = true;
            state.answers[106] = 'B';
            renderOMRPalette();
            renderCurrentQuestion();
        }""")
        page.wait_for_timeout(600)
        p1 = os.path.join(OUT_DIR, "screen_01_workspace_omr.png")
        page.screenshot(path=p1)
        print("Saved:", p1)

        # 2. Screen 2: Tab 1 — Guided Practice Mode with Instant NCERT Solution & -1 Negative Mark Trap Breakdown
        page.evaluate("""() => {
            loadSelectedModule('bio_ncert_mastery');
            selectBubble('B');
            revealPracticeSolution();
        }""")
        page.wait_for_timeout(600)
        p2 = os.path.join(OUT_DIR, "screen_02_practice_trap_box.png")
        page.screenshot(path=p2)
        print("Saved:", p2)

        # 3. Screen 3: Tab 1 — Disputed / Bonus (+4) / Supreme Court Landmark Question + Bilingual AI Coach Chat
        page.evaluate("""() => {
            loadSelectedModule('pyq_controversial_2024_2026');
            selectBubble('D');
            revealPracticeSolution();
            chatHistory = [
                {
                    sender: "coach",
                    text: "வணக்கம்! Welcome to your **Tamil Nadu NEET-UG Mastery Workspace**. Ask me in **English**, **தமிழ்**, or **Tanglish** for step-by-step NCERT derivations or -1 trap analysis."
                },
                {
                    sender: "user",
                    text: "இந்த NEET 2024 Physics Atoms வினாவில் ஏன் Statement II தவறு என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது?"
                },
                {
                    sender: "coach",
                    text: "**NCERT Class 12 Physics (Ch. 12 Atoms) — உச்ச நீதிமன்றம் மற்றும் IIT-Delhi குழு தீர்ப்பு:**\\n\\n1. **கூற்று I (சரி):** அணுக்கள் மின் நடுநிலையானவை (Electrically neutral), ஏனெனில் சம எண்ணிக்கையிலான நேர் மற்றும் எதிர் மின்னூட்டங்களைக் கொண்டுள்ளன.\\n2. **கூற்று II (தவறு):** யுரேனியம், ரேடியம் போன்ற கதிரியக்கத் தனிமங்களின் (Radioactive elements) அணுக்கள் **நிலையற்றவை (Unstable)**. புதிய NCERT புத்தகத்தில் *'Atoms of most elements are stable'* என்று திருத்தப்பட்டுள்ளது. எனவே **Option D** மட்டுமே சரியான விடை!"
                }
            ];
            renderChat();
        }""")
        page.wait_for_timeout(600)
        p3 = os.path.join(OUT_DIR, "screen_03_ai_coach_tamil.png")
        page.screenshot(path=p3)
        print("Saved:", p3)

        # 4. Screen 4: Tab 2 — Past Papers & NCERT Exemplar Hub (7,484 Questions, 40 Official Papers + 5 Exemplar/Mock Modules)
        page.evaluate("""() => {
            switchView('pyq');
        }""")
        page.wait_for_timeout(700)
        p4 = os.path.join(OUT_DIR, "screen_04_pyq_exemplar_hub.png")
        page.screenshot(path=p4)
        print("Saved:", p4)

        # 5. Screen 4B: Tab 2 Scrolled to 40 Official Papers & Disputed NTA Answer Key Dossier
        page.evaluate("""() => {
            switchView('pyq');
            const sc = document.querySelector('#view-pyq .page-scroll');
            if (sc) sc.scrollTop = 580;
        }""")
        page.wait_for_timeout(600)
        p4b = os.path.join(OUT_DIR, "screen_04b_official_papers_grid.png")
        page.screenshot(path=p4b)
        print("Saved:", p4b)

        # 6. Screen 5: Tab 3 — Score & Mentor Tracker (Projected /720 Score, -1 Negative Marks Lost, TN Medical College Tier)
        page.evaluate("""() => {
            switchView('tracker');
        }""")
        page.wait_for_timeout(800)
        p5 = os.path.join(OUT_DIR, "screen_05_score_tracker.png")
        page.screenshot(path=p5)
        print("Saved:", p5)

        # 7. Screen 6: Tab 4 — TN NEET Guide, 720/720 Topper Playbook, DMER Cutoffs & Curated YouTube Hub
        page.evaluate("""() => {
            switchView('guide');
        }""")
        page.wait_for_timeout(700)
        p6 = os.path.join(OUT_DIR, "screen_06_tn_guide_youtube.png")
        page.screenshot(path=p6)
        print("Saved:", p6)

        browser.close()


if __name__ == "__main__":
    main()
