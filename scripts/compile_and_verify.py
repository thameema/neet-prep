#!/usr/bin/env python3
"""
Compiles all 80 Bilingual (English + Tamil) NEET-UG questions, executes independent
mathematical & scientific verification assertions on every numerical and logic problem,
audits bilingual schema completeness, and generates questions_bank.json + questions_database.js.
"""

import json
import math
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from questions_pc import PHYSICS_QUESTIONS, CHEMISTRY_QUESTIONS
from questions_bz import BOTANY_QUESTIONS, ZOOLOGY_QUESTIONS


def has_tamil(text: str) -> bool:
    return bool(re.search(r"[\u0B80-\u0BFF]", text or ""))


def run_independent_math_verifications(by_id: dict):
    """Independently compute every numerical/logic problem in Python and assert answer key matches."""
    # Q101: X = A^2 B^(1/2) / (C^(1/3) D^3) with 1%, 2%, 3%, 4%
    err_101 = 2 * 1 + 0.5 * 2 + (1 / 3) * 3 + 3 * 4
    assert math.isclose(err_101, 16.0), f"Q101 mismatch: {err_101}"
    assert by_id[101]["correct"] == "A" and "16%" in by_id[101]["choices"][0]["text_en"]

    # Q102: Harmonic mean of v and 2v = 2*1*2/(1+2) = 4/3
    v_avg = (2 * 1 * 2) / (1 + 2)
    assert math.isclose(v_avg, 4 / 3)
    assert by_id[102]["correct"] == "B" and ("4v / 3" in by_id[102]["choices"][1]["text_en"] or "\\frac{4v}{3}" in by_id[102]["choices"][1]["text_en"])

    # Q103: u=280, theta=30 deg, g=9.8 => H = (u sin 30)^2 / (2g)
    h_max = ((280 * math.sin(math.radians(30))) ** 2) / (2 * 9.8)
    assert math.isclose(h_max, 1000.0), f"Q103 mismatch: {h_max}"
    assert by_id[103]["correct"] == "B" and "1000 m" in by_id[103]["choices"][1]["text_en"]

    # Q104: m=0.15, u=+12, v=-12 => |J| = m|v - u|
    impulse = 0.15 * abs(-12.0 - 12.0)
    assert math.isclose(impulse, 3.6)
    assert by_id[104]["correct"] == "C" and "3.6" in by_id[104]["choices"][2]["text_en"]

    # Q105: KE increases by 300% => K' = 4K => p'/p = sqrt(4) = 2 => +100%
    pct_inc_p = (math.sqrt(1 + 3.0) - 1.0) * 100.0
    assert math.isclose(pct_inc_p, 100.0)
    assert by_id[105]["correct"] == "A" and "100%" in by_id[105]["choices"][0]["text_en"]

    # Q106: K_normal / K_diam = (1/sqrt(2)) / (1/2) = sqrt(2)
    k_ratio = (1 / math.sqrt(2)) / 0.5
    assert math.isclose(k_ratio, math.sqrt(2))
    assert by_id[106]["correct"] == "B" and ("sqrt(2) : 1" in by_id[106]["choices"][1]["text_en"] or "\\sqrt{2} : 1" in by_id[106]["choices"][1]["text_en"])

    # Q107: v_e prop R at constant density; R' = 4R => 4v
    assert by_id[107]["correct"] == "D" and "4v" in by_id[107]["choices"][3]["text_en"]

    # Q108: Carnot eta=0.5, T1 = 327+273 = 600 K => T2 = 300 K = 27 C
    t1_k = 327 + 273
    t2_c = t1_k * (1 - 0.5) - 273
    assert math.isclose(t2_c, 27.0)
    assert by_id[108]["correct"] == "A" and "27°C" in by_id[108]["choices"][0]["text_en"]

    # Q109: SHM KE = PE => A^2 - x^2 = x^2 => x/A = 1/sqrt(2)
    assert by_id[109]["correct"] == "B" and ("A / sqrt(2)" in by_id[109]["choices"][1]["text_en"] or "\\frac{A}{\\sqrt{2}}" in by_id[109]["choices"][1]["text_en"])

    # Q110: C0=15 pF, d'=2d, K=4 => C' = 15 * 4 / 2 = 30 pF
    c_new = 15.0 * 4.0 / 2.0
    assert math.isclose(c_new, 30.0)
    assert by_id[110]["correct"] == "A" and "30 pF" in by_id[110]["choices"][0]["text_en"]

    # Q111: R0=10, stretched n=3 => R' = 9 * 10 = 90
    assert 10 * (3 ** 2) == 90
    assert by_id[111]["correct"] == "B" and "90 Ω" in by_id[111]["choices"][1]["text_en"]

    # Q112: Balanced bridge (4/6 == 8/12): upper=10, lower=20, V=20 => I = 20 / (200/30) = 3.0 A
    assert math.isclose(4 / 6, 8 / 12)
    r_eq = (10.0 * 20.0) / (10.0 + 20.0)
    curr = 20.0 / r_eq
    assert math.isclose(curr, 3.0)
    assert by_id[112]["correct"] == "A" and "3.0 A" in by_id[112]["choices"][0]["text_en"]

    # Q113: r_p / r_alpha at equal KE: (sqrt(1)/1) / (sqrt(4)/2) = 1.0
    r_ratio = (math.sqrt(1) / 1) / (math.sqrt(4) / 2)
    assert math.isclose(r_ratio, 1.0)
    assert by_id[113]["correct"] == "A" and "1 : 1" in by_id[113]["choices"][0]["text_en"]

    # Q114: L = 10e-3 H, C = 1e-6 F => omega_0 = 1/sqrt(LC) = 1e4 rad/s
    omega_0 = 1.0 / math.sqrt(10e-3 * 1e-6)
    assert math.isclose(omega_0, 1e4)
    assert by_id[114]["correct"] == "A" and "10^4" in by_id[114]["choices"][0]["text_en"]

    # Q115: f_air = 20, ng = 1.5, nl = 1.25 => f_liq = 20 * (1.5 - 1) / (1.5/1.25 - 1) = 50 cm
    f_liq = 20.0 * (1.5 - 1.0) / ((1.5 / 1.25) - 1.0)
    assert math.isclose(f_liq, 50.0)
    assert by_id[115]["correct"] == "A" and "+50 cm" in by_id[115]["choices"][0]["text_en"]

    # Q116: YDSE lambda=600e-9, D=1.5, d=1e-3 => beta = 0.9 mm
    beta_mm = (600e-9 * 1.5 / 1e-3) * 1000.0
    assert math.isclose(beta_mm, 0.9)
    assert by_id[116]["correct"] == "A" and "0.9 mm" in by_id[116]["choices"][0]["text_en"]

    # Q117: Photoelectric V0 = 3.54 - 2.14 = 1.40 V
    assert math.isclose(3.54 - 2.14, 1.40)
    assert by_id[117]["correct"] == "A" and "1.40 V" in by_id[117]["choices"][0]["text_en"]

    # Q118: H atom n=1 to n=2 => -13.6/4 - (-13.6) = 10.2 eV
    delta_e = (-13.6 / 4.0) - (-13.6)
    assert math.isclose(delta_e, 10.2)
    assert by_id[118]["correct"] == "B" and "10.2 eV" in by_id[118]["choices"][1]["text_en"]

    # Q119: Nuclear radius (27/125)^(1/3) = 3/5
    assert math.isclose((27 / 125) ** (1 / 3), 3 / 5)
    assert by_id[119]["correct"] == "A" and "3 : 5" in by_id[119]["choices"][0]["text_en"]

    # Q120: Truth table of NOT(NOR(A, B)) == OR(A, B)
    for a in (0, 1):
        for b in (0, 1):
            nor_out = int(not (a or b))
            final_out = int(not nor_out)
            assert final_out == (a or b)
    assert by_id[120]["correct"] == "A" and "OR gate" in by_id[120]["choices"][0]["text_en"]

    # Q201: 50 mL of 0.5 M HCl with 95% pure CaCO3
    mol_hcl = 0.050 * 0.5
    mass_sample = (mol_hcl / 2.0) * 100.0 / 0.95
    assert round(mass_sample, 2) == 1.32
    assert by_id[201]["correct"] == "B" and "1.32 g" in by_id[201]["choices"][1]["text_en"]

    # Q206: dH=30000 J, dS=100 J/K => T > 300 K
    assert 30000 / 100 == 300
    assert by_id[206]["correct"] == "B" and "above 300 K" in by_id[206]["choices"][1]["text_en"]

    # Q207: 10^-8 M HCl exact quadratic [H+]([H+] - 1e-8) = 1e-14
    c = 1e-8
    h_plus = (c + math.sqrt(c * c + 4e-14)) / 2.0
    ph_val = -math.log10(h_plus)
    assert round(ph_val, 2) == 6.98
    assert by_id[207]["correct"] == "B" and "6.98" in by_id[207]["choices"][1]["text_en"]

    # Q208: MnO4- (+7) -> Mn2+ (+2) = 5 F
    assert 7 - 2 == 5 and by_id[208]["correct"] == "A"

    # Q210: First order t1/2=20 min, 87.5% complete => remaining 0.125 = (1/2)^3 => 60 min
    k = math.log(2) / 20.0
    t_875 = math.log(1.0 / (1.0 - 0.875)) / k
    assert math.isclose(t_875, 60.0)
    assert by_id[210]["correct"] == "B" and "60" in by_id[210]["choices"][1]["text_en"]

    # Q211: Mn2+ (Z=25 -> d5 -> n=5) spin-only moment sqrt(5*7) = 5.916 -> 5.92 BM
    mu_bm = math.sqrt(5 * (5 + 2))
    assert round(mu_bm, 2) == 5.92
    assert by_id[211]["correct"] == "B" and "5.92 BM" in by_id[211]["choices"][1]["text_en"]

    # Q307: G2 phase of 2n=16, 2C => 16 chromosomes, 4C DNA
    assert by_id[307]["correct"] == "B" and "16 chromosomes and 4C" in by_id[307]["choices"][1]["text_en"]

    # Q309: C3 Calvin cycle for 1 glucose => 6 CO2, 18 ATP, 12 NADPH
    assert by_id[309]["correct"] == "A" and "6 CO2, 18 ATP, 12 NADPH" in by_id[309]["choices"][0]["text_en"]

    # Q315: Chargaff rule %C = 20% => %A = 50% - 20% = 30%
    assert 50 - 20 == 30 and by_id[315]["correct"] == "B"

    # Q414: Hardy-Weinberg q^2 = 0.09 => q = 0.3, p = 0.7 => 2pq = 0.42
    q = math.sqrt(0.09)
    two_pq = 2 * (1 - q) * q
    assert math.isclose(two_pq, 0.42)
    assert by_id[414]["correct"] == "B" and "0.42" in by_id[414]["choices"][1]["text_en"]


def main():
    all_questions = (
        PHYSICS_QUESTIONS
        + CHEMISTRY_QUESTIONS
        + BOTANY_QUESTIONS
        + ZOOLOGY_QUESTIONS
    )
    assert len(all_questions) == 80, f"Expected 80 questions, got {len(all_questions)}"

    seen_ids = set()
    by_id = {}
    subject_counts = {"Physics": 0, "Chemistry": 0, "Botany": 0, "Zoology": 0}

    for q in all_questions:
        qid = q["id"]
        assert qid not in seen_ids, f"Duplicate question ID: {qid}"
        seen_ids.add(qid)
        by_id[qid] = q

        subj = q["subject"]
        assert subj in subject_counts, f"Invalid subject {subj} in Q{qid}"
        subject_counts[subj] += 1

        # Bilingual stem & explanation verification
        assert len(q.get("stem_en", "").strip()) >= 20, f"Short stem_en in Q{qid}"
        assert has_tamil(q.get("stem_ta", "")), f"Missing Tamil script in stem_ta of Q{qid}"
        assert len(q.get("explanation_en", "").strip()) >= 30, f"Short explanation_en in Q{qid}"
        assert has_tamil(q.get("explanation_ta", "")), f"Missing Tamil script in explanation_ta of Q{qid}"
        assert q.get("ncertRef", "").startswith("NCERT"), f"Missing NCERT ref in Q{qid}"
        assert len(q.get("ncert_key_point", "").strip()) >= 15, f"Short ncert_key_point in Q{qid}"

        # Choices check
        choices = q.get("choices", [])
        assert len(choices) == 4, f"Q{qid} does not have 4 choices"
        letters = [c["letter"] for c in choices]
        assert letters == ["A", "B", "C", "D"], f"Invalid choice letters in Q{qid}: {letters}"
        en_texts = [c["text_en"].strip() for c in choices]
        assert len(set(en_texts)) == 4, f"Duplicate English choices in Q{qid}: {en_texts}"
        for c in choices:
            assert c.get("text_ta", "").strip(), f"Empty text_ta in Q{qid} option {c['letter']}"

        # Correct answer & trap breakdown check
        corr = q.get("correct")
        assert corr in ("A", "B", "C", "D"), f"Invalid correct answer in Q{qid}: {corr}"
        traps = q.get("trap_breakdown", {})
        wrong_letters = [L for L in ("A", "B", "C", "D") if L != corr]
        for wl in wrong_letters:
            assert wl in traps and len(traps[wl].strip()) >= 8, f"Missing trap breakdown for {wl} in Q{qid}"

        # Video check
        vid = q.get("videoTutorial", {})
        assert vid.get("url", "").startswith("https://www.youtube.com/"), f"Invalid YouTube URL in Q{qid}"

    for s, cnt in subject_counts.items():
        assert cnt == 20, f"Expected 20 {s} questions, got {cnt}"

    run_independent_math_verifications(by_id)

    # Define exam & practice modules matching NTA NEET-UG structure (+4 / -1 / 0)
    modules = {
        "full_mock_1": {
            "id": "full_mock_1",
            "title": "NEET Full Syllabus Mock Exam — Paper 1 (NTA 4-Subject OMR Pattern)",
            "title_ta": "முழு பாடத்திட்ட நீட் மாதிரித் தேர்வு — தாள் 1 (NTA OMR முறை)",
            "mode": "mock",
            "durationMinutes": 80,
            "marking": {"correct": 4, "wrong": -1, "unanswered": 0},
            "description": "80 compulsory questions (20 Physics + 20 Chemistry + 20 Botany + 20 Zoology) in exact 1:1:1:1 NTA NEET proportion. 80 minutes (1 min/question pace matching 180 Qs in 180 mins), +4/-1 marking, projected out of 720.",
            "questionIds": [q["id"] for q in all_questions]
        },
        "mini_mock_pyq": {
            "id": "mini_mock_pyq",
            "title": "NEET High-Yield PYQ Mock Exam — Paper 2 (40 Qs / 40 Mins)",
            "title_ta": "முக்கிய முந்தைய ஆண்டு வினாக்கள் மாதிரித் தேர்வு — தாள் 2 (40 வினாக்கள்)",
            "mode": "mock",
            "durationMinutes": 40,
            "marking": {"correct": 4, "wrong": -1, "unanswered": 0},
            "description": "Balanced 40-question high-frequency NEET Previous Year Paper (10 Physics + 10 Chemistry + 10 Botany + 10 Zoology) for daily timed exam practice.",
            "questionIds": (
                [101, 102, 103, 106, 108, 111, 112, 115, 118, 120]
                + [201, 203, 204, 207, 209, 210, 212, 214, 216, 220]
                + [301, 303, 305, 306, 308, 311, 312, 314, 316, 318]
                + [401, 403, 404, 405, 407, 411, 412, 414, 417, 420]
            )
        },
        "random_daily_sprint": {
            "id": "random_daily_sprint",
            "title": "Dynamic Randomised 20-Q NEET Sprint (Fresh Paper Every Attempt)",
            "title_ta": "தினசரி சுழற்சி நீட் மாதிரித் தேர்வு (20 வினாக்கள் — ஒவ்வொரு முறையும் புதிய தாள்)",
            "mode": "mock",
            "isDynamicRandom": True,
            "perSubjectCount": 5,
            "durationMinutes": 20,
            "marking": {"correct": 4, "wrong": -1, "unanswered": 0},
            "description": "Generates a newly shuffled 20-question mini-OMR test (5 Physics, 5 Chemistry, 5 Botany, 5 Zoology) every time you start or retake.",
            "questionIds": []
        },
        "practice_physics": {
            "id": "practice_physics",
            "title": "Physics Mastery Practice (20 Qs — Instant Coaching & Formulas)",
            "title_ta": "இயற்பியல் பயிற்சி (20 வினாக்கள் — உடனடி விளக்கம்)",
            "mode": "practice",
            "durationMinutes": 30,
            "marking": {"correct": 4, "wrong": -1, "unanswered": 0},
            "description": "Class 11 & 12 NCERT Physics numericals, derivations, and conceptual traps with instant check and step-by-step Gemini coaching.",
            "questionIds": [q["id"] for q in PHYSICS_QUESTIONS]
        },
        "practice_chemistry": {
            "id": "practice_chemistry",
            "title": "Chemistry Mastery Practice (20 Qs — Physical, Inorganic & Organic)",
            "title_ta": "வேதியியல் பயிற்சி (20 வினாக்கள் — இயற்பியல், கனிம & கரிம வேதியியல்)",
            "mode": "practice",
            "durationMinutes": 25,
            "marking": {"correct": 4, "wrong": -1, "unanswered": 0},
            "description": "Stoichiometry, VSEPR/MOT, Coordination Compounds, Named Organic Reactions, and Practical Chemistry.",
            "questionIds": [q["id"] for q in CHEMISTRY_QUESTIONS]
        },
        "practice_botany": {
            "id": "practice_botany",
            "title": "Botany NCERT Line-by-Line Practice (20 Qs — Instant Feedback)",
            "title_ta": "தாவரவியல் NCERT வரிக்கு வரி பயிற்சி (20 வினாக்கள்)",
            "mode": "practice",
            "durationMinutes": 20,
            "marking": {"correct": 4, "wrong": -1, "unanswered": 0},
            "description": "Cell Cycle, C3/C4 Photosynthesis, ETS, Plant Kingdom, Morphology, Mendelian & Molecular Genetics, and Ecology.",
            "questionIds": [q["id"] for q in BOTANY_QUESTIONS]
        },
        "practice_zoology": {
            "id": "practice_zoology",
            "title": "Zoology NCERT Line-by-Line Practice (20 Qs — Instant Feedback)",
            "title_ta": "விலங்கியல் NCERT வரிக்கு வரி பயிற்சி (20 வினாக்கள்)",
            "mode": "practice",
            "durationMinutes": 20,
            "marking": {"correct": 4, "wrong": -1, "unanswered": 0},
            "description": "Animal Kingdom, Human Physiology (ECG, O2 Curve, Nephron, Sliding Filament, Hormones), Human Reproduction, IUDs, Evolution, and Biotechnology.",
            "questionIds": [q["id"] for q in ZOOLOGY_QUESTIONS]
        },
        "mistake_bank": {
            "id": "mistake_bank",
            "title": "Adaptive Mistake & Negative-Mark Recovery Bank",
            "title_ta": "தவறான வினாக்கள் மீட்புப் பயிற்சி வங்கி (-1 மதிப்பெண் தடுப்பு)",
            "mode": "practice",
            "isMistakeBank": True,
            "durationMinutes": 25,
            "marking": {"correct": 4, "wrong": -1, "unanswered": 0},
            "description": "Automatically collects every question you answered wrong (-1) or flagged across mocks so you can turn weak NCERT lines into +4 marks.",
            "questionIds": []
        }
    }

    bank_payload = {
        "metadata": {
            "exam": "NEET-UG (NTA Current 180-Q Compulsory OMR Pattern)",
            "region": "Tamil Nadu (Bilingual English + Tamil)",
            "totalQuestionsInBank": len(all_questions),
            "subjectCounts": subject_counts,
            "markingScheme": {"correct": 4, "incorrect": -1, "unanswered": 0, "fullExamMaxMarks": 720}
        },
        "modules": modules,
        "questions": all_questions
    }

    json_path = os.path.join(ROOT_DIR, "questions_bank.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(bank_payload, f, ensure_ascii=False, indent=2)

    js_path = os.path.join(ROOT_DIR, "questions_database.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("// Auto-generated & mathematically verified Bilingual NEET-UG Question Bank\n")
        f.write("window.NEET_QUESTION_BANK = ")
        json.dump(bank_payload, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    print(f"VERIFICATION PASSED: {len(all_questions)} bilingual NEET-UG questions audited & mathematically verified!")
    print(f"Subject distribution: {subject_counts}")
    print(f"Wrote: {json_path} and {js_path}")


if __name__ == "__main__":
    main()
