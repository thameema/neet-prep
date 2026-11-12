#!/usr/bin/env python3
"""
20 Authentic NEET-UG Physics Questions (IDs 101-120) and
20 Authentic NEET-UG Chemistry Questions (IDs 201-220)
Strictly aligned to NMC-rationalized Class 11 & 12 NCERT and NEET 2019-2025 PYQs,
with full Bilingual (English + Tamil) stems, options, explanations, trap breakdowns, and video tutorials.
"""

VIDEOS = {
    "phys_mech": {
        "title": "NEET Physics Mechanics & Laws of Motion One-Shot (Tamil + NCERT)",
        "channel": "Vedantu NEET Tamil",
        "url": "https://www.youtube.com/@Vedantu_NEET_Tamil"
    },
    "phys_elec": {
        "title": "Current Electricity & Electrostatics Complete PYQs",
        "channel": "PW English",
        "url": "https://www.youtube.com/@PW-English"
    },
    "phys_opt_mod": {
        "title": "Optics, Modern Physics & Semiconductors High-Yield Shortcuts (Tamil)",
        "channel": "Xylem NEET Tamil",
        "url": "https://www.youtube.com/@XylemNEETTamil"
    },
    "chem_phys": {
        "title": "Physical Chemistry Formulas & Numericals Masterclass",
        "channel": "PW English",
        "url": "https://www.youtube.com/@PW-English"
    },
    "chem_inorg": {
        "title": "Chemical Bonding & Coordination Compounds NCERT Line-by-Line (Tamil)",
        "channel": "Vedantu NEET Tamil",
        "url": "https://www.youtube.com/@Vedantu_NEET_Tamil"
    },
    "chem_org": {
        "title": "Organic Chemistry Named Reactions & Mechanisms (Tamil)",
        "channel": "Xylem NEET Tamil",
        "url": "https://www.youtube.com/@XylemNEETTamil"
    },
}

PHYSICS_QUESTIONS = [
    {
        "id": 101,
        "subject": "Physics",
        "classLevel": "Class 11",
        "chapter": "Units and Measurements",
        "ncertRef": "NCERT Class 11 Physics, Ch 1 — Error Analysis in Measurements",
        "pyqTag": "NEET PYQ (2022/2024 Pattern)",
        "questionType": "Numerical MCQ",
        "difficulty": "Medium",
        "stem_en": "In an experiment, the percentage errors in the measurement of physical quantities A, B, C, and D are 1%, 2%, 3%, and 4% respectively. Then the maximum percentage error in the measurement of $X$, where $X = \\frac{A^2 B^{1/2}}{C^{1/3} D^3}$, will be:",
        "stem_ta": "ஒரு சோதனையில் A, B, C மற்றும் D ஆகிய இயற்பியல் அளவுகளின் அளவீட்டில் ஏற்படும் சதவீதப் பிழைகள் முறையே 1%, 2%, 3% மற்றும் 4% ஆகும். $X = \\frac{A^2 B^{1/2}}{C^{1/3} D^3}$ எனில், $X$-இன் அளவீட்டில் ஏற்படும் பெரும சதவீதப் பிழை என்ன?",
        "choices": [
            {"letter": "A", "text_en": "16%", "text_ta": "16%"},
            {"letter": "B", "text_en": "10%", "text_ta": "10%"},
            {"letter": "C", "text_en": "14%", "text_ta": "14%"},
            {"letter": "D", "text_en": "-10%", "text_ta": "-10%"}
        ],
        "correct": "A",
        "explanation_en": "Relative errors ALWAYS ADD UP for both multiplication and division: $\\frac{\\Delta X}{X}\\% = 2\\left(\\frac{\\Delta A}{A}\\right) + \\frac{1}{2}\\left(\\frac{\\Delta B}{B}\\right) + \\frac{1}{3}\\left(\\frac{\\Delta C}{C}\\right) + 3\\left(\\frac{\\Delta D}{D}\\right) = 2(1\\%) + 0.5(2\\%) + \\frac{1}{3}(3\\%) + 3(4\\%) = 2\\% + 1\\% + 1\\% + 12\\% = 16\\%$.",
        "explanation_ta": "பெருக்கல் மற்றும் வகுத்தல் ஆகிய இரண்டிற்குமே சார்புப் பிழைகளை எப்போதும் கூட்ட வேண்டும்: $\\frac{\\Delta X}{X}\\% = 2(1\\%) + \\frac{1}{2}(2\\%) + \\frac{1}{3}(3\\%) + 3(4\\%) = 2\\% + 1\\% + 1\\% + 12\\% = 16\\%$.",
        "ncert_key_point": "Maximum fractional error adds all |power * percentage error| terms; never subtract denominator errors.",
        "trap_breakdown": {
            "B": "Obtained if you wrongly subtract denominator errors: |(2 + 1) - (1 + 12)| = 10%.",
            "C": "Arithmetic slip missing the factor of 2 on A^2.",
            "D": "Maximum percentage errors are always positive magnitudes; -10% is a classic sign trap."
        },
        "videoTutorial": VIDEOS["phys_mech"]
    },
    {
        "id": 102,
        "subject": "Physics",
        "classLevel": "Class 11",
        "chapter": "Motion in a Straight Line",
        "ncertRef": "NCERT Class 11 Physics, Ch 2 — Average Speed",
        "pyqTag": "NEET 2023 Official PYQ",
        "questionType": "Numerical MCQ",
        "difficulty": "Easy",
        "stem_en": "A vehicle travels half the distance with speed v and the remaining distance with speed 2v. Its average speed is:",
        "stem_ta": "ஒரு வாகனம் மொத்தத் தொலைவில் பாதியை v என்ற வேகத்திலும், மீதமுள்ள பாதித் தொலைவை 2v என்ற வேகத்திலும் கடக்கிறது. அதன் சராசரி வேகம் என்ன?",
        "choices": [
            {"letter": "A", "text_en": "$\\frac{3v}{2}$", "text_ta": "$\\frac{3v}{2}$"},
            {"letter": "B", "text_en": "$\\frac{4v}{3}$", "text_ta": "$\\frac{4v}{3}$"},
            {"letter": "C", "text_en": "$\\frac{2v}{3}$", "text_ta": "$\\frac{2v}{3}$"},
            {"letter": "D", "text_en": "$\\frac{3v}{4}$", "text_ta": "$\\frac{3v}{4}$"}
        ],
        "correct": "B",
        "explanation_en": "For two equal half-distances with speeds v1 and v2, average speed is the harmonic mean: v_avg = 2*v1*v2 / (v1 + v2) = 2*v*(2v) / (v + 2v) = 4v^2 / 3v = 4v/3.",
        "explanation_ta": "சம தொலைவுகளை v1 மற்றும் v2 வேகங்களில் கடக்கும்போது சராசரி வேகம் = 2*v1*v2 / (v1 + v2) = 2*v*(2v) / (v + 2v) = 4v/3.",
        "ncert_key_point": "Equal distances -> Harmonic Mean 2v1v2/(v1+v2). Equal time intervals -> Arithmetic Mean (v1+v2)/2.",
        "trap_breakdown": {
            "A": "3v/2 = (v + 2v)/2 is the average speed for equal TIME intervals, not equal distances.",
            "C": "Forgetting total distance is 2d instead of d.",
            "D": "Inverting total distance / total time."
        },
        "videoTutorial": VIDEOS["phys_mech"]
    },
    {
        "id": 103,
        "subject": "Physics",
        "classLevel": "Class 11",
        "chapter": "Motion in a Plane",
        "ncertRef": "NCERT Class 11 Physics, Ch 3 — Projectile Motion",
        "pyqTag": "NEET 2023 Official PYQ",
        "questionType": "Numerical MCQ",
        "difficulty": "Medium",
        "stem_en": "A bullet is fired from a gun at the speed of 280 m/s in the direction 30° above the horizontal. The maximum height attained by the bullet is (take g = 9.8 m/s^2, sin 30° = 0.5):",
        "stem_ta": "ஒரு துப்பாக்கியிலிருந்து தோட்டா ஒன்று கிடைமட்டத்திலிருந்து 30° கோணத்தில் 280 m/s வேகத்தில் சுடப்படுகிறது. தோட்டா அடையும் பெரும உயரம் என்ன? (g = 9.8 m/s^2, sin 30° = 0.5):",
        "choices": [
            {"letter": "A", "text_en": "2000 m", "text_ta": "2000 m"},
            {"letter": "B", "text_en": "1000 m", "text_ta": "1000 m"},
            {"letter": "C", "text_en": "3000 m", "text_ta": "3000 m"},
            {"letter": "D", "text_en": "2800 m", "text_ta": "2800 m"}
        ],
        "correct": "B",
        "explanation_en": "Maximum height H = (u^2 * sin^2 θ) / (2g). First compute u_y = u * sin 30° = 280 * 0.5 = 140 m/s. Then H = 140^2 / (2 * 9.8) = 19600 / 19.6 = 1000 m.",
        "explanation_ta": "பெரும உயரம் H = (u^2 * sin^2 θ) / (2g). இங்கு செங்குத்து திசைவேகம் u_y = 280 * 0.5 = 140 m/s. எனவே H = (140 * 140) / 19.6 = 1000 m.",
        "ncert_key_point": "Compute vertical component u_y = u sin θ first, then H = u_y^2 / (2g) for instant clean cancellation.",
        "trap_breakdown": {
            "A": "2000 m omits the factor of 2 in 2g.",
            "C": "3000 m uses cos^2 30° = 3/4 instead of sin^2 30° = 1/4.",
            "D": "2800 m confuses range formula with height."
        },
        "videoTutorial": VIDEOS["phys_mech"]
    },
    {
        "id": 104,
        "subject": "Physics",
        "classLevel": "Class 11",
        "chapter": "Laws of Motion",
        "ncertRef": "NCERT Class 11 Physics, Ch 4 — Impulse and Momentum",
        "pyqTag": "NEET NCERT Exemplar / PYQ",
        "questionType": "Numerical MCQ",
        "difficulty": "Medium",
        "stem_en": "A ball of mass 0.15 kg hits a vertical rigid wall horizontally at 12 m/s and rebounds horizontally along the same line at 12 m/s. The magnitude of impulse imparted by the wall to the ball is:",
        "stem_ta": "0.15 kg நிறையுள்ள பந்து ஒன்று செங்குத்துச் சுவரின் மீது கிடைமட்டமாக 12 m/s வேகத்தில் மோதி, அதே நேர்க்கோட்டில் 12 m/s வேகத்தில் திரும்புகிறது. சுவர் பந்தின் மீது செலுத்திய கணத்தாக்கு விசையின் எண்மதிப்பு என்ன?",
        "choices": [
            {"letter": "A", "text_en": "0 N·s", "text_ta": "0 N·s"},
            {"letter": "B", "text_en": "1.8 N·s", "text_ta": "1.8 N·s"},
            {"letter": "C", "text_en": "3.6 N·s", "text_ta": "3.6 N·s"},
            {"letter": "D", "text_en": "7.2 N·s", "text_ta": "7.2 N·s"}
        ],
        "correct": "C",
        "explanation_en": "Momentum is a vector! Taking u = +12 m/s and rebound v = -12 m/s, |Impulse| = |Δp| = m|v - u| = 0.15 * |-12 - 12| = 0.15 * 24 = 3.6 N·s.",
        "explanation_ta": "உந்தம் ஒரு வெக்டர் அளவாகும்! u = +12 m/s, திரும்பும் திசைவேகம் v = -12 m/s. கணத்தாக்கு |J| = |Δp| = m|v - u| = 0.15 * 24 = 3.6 N·s.",
        "ncert_key_point": "For normal elastic rebound at speed u, magnitude of momentum change is always 2mu, never zero.",
        "trap_breakdown": {
            "A": "0 N·s treats momentum as scalar (mv - mu = 0), ignoring direction reversal.",
            "B": "1.8 N·s computes mu instead of 2mu.",
            "D": "7.2 N·s doubles 2mu a second time."
        },
        "videoTutorial": VIDEOS["phys_mech"]
    },
    {
        "id": 105,
        "subject": "Physics",
        "classLevel": "Class 11",
        "chapter": "Work, Energy and Power",
        "ncertRef": "NCERT Class 11 Physics, Ch 5 — Kinetic Energy & Linear Momentum",
        "pyqTag": "NEET High-Frequency PYQ",
        "questionType": "Numerical MCQ",
        "difficulty": "Medium",
        "stem_en": "If the kinetic energy of a body increases by 300%, the percentage increase in its linear momentum will be:",
        "stem_ta": "ஒரு பொருளின் இயக்க ஆற்றல் 300% அதிகரித்தால், அதன் நேர்க்கோட்டு உந்தத்தில் ஏற்படும் சதவீத அதிகரிப்பு என்ன?",
        "choices": [
            {"letter": "A", "text_en": "100%", "text_ta": "100%"},
            {"letter": "B", "text_en": "150%", "text_ta": "150%"},
            {"letter": "C", "text_en": "200%", "text_ta": "200%"},
            {"letter": "D", "text_en": "300%", "text_ta": "300%"}
        ],
        "correct": "A",
        "explanation_en": "Initial KE = K. 'Increases BY 300%' means final K' = K + 3K = 4K. Since p = sqrt(2mK), p'/p = sqrt(K'/K) = sqrt(4) = 2. Percentage increase = ((2p - p)/p) * 100% = 100%.",
        "explanation_ta": "ஆரம்ப இயக்க ஆற்றல் = K. 300% அதிகரிப்பு என்றால் இறுதி K' = K + 3K = 4K. p = sqrt(2mK) என்பதால் p'/p = sqrt(4) = 2. எனவே சதவீத அதிகரிப்பு = ((2p - p)/p) * 100% = 100%.",
        "ncert_key_point": "Never use calculus approximation Δp/p = (1/2)ΔK/K when percentage change exceeds 5%!",
        "trap_breakdown": {
            "B": "150% wrongly applies small-error formula (1/2)*(300%).",
            "C": "200% reports final momentum percentage (200% of initial) without subtracting initial 100%.",
            "D": "300% assumes p is linearly proportional to K."
        },
        "videoTutorial": VIDEOS["phys_mech"]
    },
    {
        "id": 106,
        "subject": "Physics",
        "classLevel": "Class 11",
        "chapter": "System of Particles and Rotational Motion",
        "ncertRef": "NCERT Class 11 Physics, Ch 6 — Moment of Inertia & Radius of Gyration",
        "pyqTag": "NEET 2023 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "The ratio of the radius of gyration of a thin uniform disc about an axis passing through its centre and normal to its plane to the radius of gyration of the disc about its diameter is:",
        "stem_ta": "சீரான மெல்லிய வட்டு ஒன்றின் மையத்தின் வழியாகவும் தளத்திற்குச் செங்குத்தாகவும் செல்லும் அச்சைப் பற்றிய சுழற்சி ஆரத்திற்கும், விட்டத்தைப் பற்றிய சுழற்சி ஆரத்திற்கும் இடையிலான விகிதம்:",
        "choices": [
            {"letter": "A", "text_en": "$2 : 1$", "text_ta": "$2 : 1$"},
            {"letter": "B", "text_en": "$\\sqrt{2} : 1$", "text_ta": "$\\sqrt{2} : 1$"},
            {"letter": "C", "text_en": "$4 : 1$", "text_ta": "$4 : 1$"},
            {"letter": "D", "text_en": "$1 : \\sqrt{2}$", "text_ta": "$1 : \\sqrt{2}$"}
        ],
        "correct": "B",
        "explanation_en": "About central normal axis: $I_1 = \\frac{1}{2}MR^2 \\Rightarrow K_1 = \\frac{R}{\\sqrt{2}}$. About diameter (perpendicular axis theorem): $I_2 = \\frac{1}{4}MR^2 \\Rightarrow K_2 = \\frac{R}{2}$. Therefore $K_1 : K_2 = \\frac{R/\\sqrt{2}}{R/2} = \\sqrt{2} : 1$.",
        "explanation_ta": "செங்குத்து அச்சில் $I_1 = \\frac{1}{2}MR^2 \\Rightarrow K_1 = \\frac{R}{\\sqrt{2}}$. விட்டத்தைப் பற்றி $I_2 = \\frac{1}{4}MR^2 \\Rightarrow K_2 = \\frac{R}{2}$. எனவே $K_1 : K_2 = \\sqrt{2} : 1$.",
        "ncert_key_point": "Read carefully: Radius of Gyration K = sqrt(I/M), whereas Moment of Inertia ratio I_1 : I_2 is 2 : 1.",
        "trap_breakdown": {
            "A": "2 : 1 is the ratio of Moments of Inertia I_1 : I_2, forgetting the square root for K.",
            "C": "Squaring instead of taking square root.",
            "D": "Inverting the order of the two axes."
        },
        "videoTutorial": VIDEOS["phys_mech"]
    },
    {
        "id": 107,
        "subject": "Physics",
        "classLevel": "Class 11",
        "chapter": "Gravitation",
        "ncertRef": "NCERT Class 11 Physics, Ch 7 — Escape Speed",
        "pyqTag": "NEET PYQ (2021/2024 Pattern)",
        "questionType": "Numerical MCQ",
        "difficulty": "Medium",
        "stem_en": "The escape velocity from the Earth's surface is v. The escape velocity from the surface of another planet having a radius four times that of Earth and the same mean mass density is:",
        "stem_ta": "பூமியின் மேற்பரப்பிலிருந்து விடுபடு திசைவேகம் v ஆகும். பூமியின் அதே சராசரி அடர்த்தியும், பூமியின் ஆரத்தைப் போல 4 மடங்கு ஆரமும் கொண்ட மற்றொரு கோளின் விடுபடு திசைவேகம் என்ன?",
        "choices": [
            {"letter": "A", "text_en": "v", "text_ta": "v"},
            {"letter": "B", "text_en": "2v", "text_ta": "2v"},
            {"letter": "C", "text_en": "v / 2", "text_ta": "v / 2"},
            {"letter": "D", "text_en": "4v", "text_ta": "4v"}
        ],
        "correct": "D",
        "explanation_en": "v_e = sqrt(2GM/R). Since density ρ is constant, substitute M = (4/3)πR^3 ρ: v_e = sqrt((8/3)πGρR^2) = R * sqrt((8/3)πGρ). Thus v_e ∝ R at constant density. Since R' = 4R, v_e' = 4v.",
        "explanation_ta": "v_e = sqrt(2GM/R). அடர்த்தி ρ மாறிலி என்பதால் M = (4/3)πR^3 ρ எனப் பிரதியிட v_e ∝ R. எனவே R' = 4R எனில் v_e' = 4v.",
        "ncert_key_point": "Constant Mass M => v_e ∝ 1/sqrt(R). Constant Density ρ => v_e ∝ R.",
        "trap_breakdown": {
            "A": "Cancelling R completely.",
            "B": "2v assumes g is constant (v_e = sqrt(2gR)), whereas here density ρ is constant so g' = 4g!",
            "C": "v/2 assumes mass M is constant instead of density ρ."
        },
        "videoTutorial": VIDEOS["phys_mech"]
    },
    {
        "id": 108,
        "subject": "Physics",
        "classLevel": "Class 11",
        "chapter": "Thermodynamics",
        "ncertRef": "NCERT Class 11 Physics, Ch 11 — Carnot Engine Efficiency",
        "pyqTag": "NEET 2023 Official PYQ",
        "questionType": "Numerical MCQ",
        "difficulty": "Easy",
        "stem_en": "A Carnot engine has an efficiency of 50% when its source is at a temperature of 327°C. The temperature of the sink is:",
        "stem_ta": "கார்னோ (Carnot) வெப்ப இயந்திரம் ஒன்றின் வெப்ப மூலம் 327°C வெப்பநிலையில் உள்ளபோது அதன் பயனுறுதிறன் 50% ஆகும். வெப்ப ஏற்பியின் (sink) வெப்பநிலை என்ன?",
        "choices": [
            {"letter": "A", "text_en": "27°C", "text_ta": "27°C"},
            {"letter": "B", "text_en": "15°C", "text_ta": "15°C"},
            {"letter": "C", "text_en": "100°C", "text_ta": "100°C"},
            {"letter": "D", "text_en": "163.5°C", "text_ta": "163.5°C"}
        ],
        "correct": "A",
        "explanation_en": "Convert source temperature to Kelvin: T_1 = 327 + 273 = 600 K. Efficiency η = 1 - (T_2 / T_1) = 0.5 => T_2 / 600 = 0.5 => T_2 = 300 K. In Celsius: t_2 = 300 - 273 = 27°C.",
        "explanation_ta": "வெப்பநிலையை முதலில் கெல்வினுக்கு மாற்றவும்: T_1 = 327 + 273 = 600 K. η = 1 - (T_2/T_1) = 0.5 => T_2 = 300 K = 300 - 273 = 27°C.",
        "ncert_key_point": "Always convert °C to Kelvin (K = °C + 273) BEFORE using η = 1 - T_sink / T_source.",
        "trap_breakdown": {
            "B": "Subtraction slip when converting 300 K to °C.",
            "C": "Guessing round Celsius values.",
            "D": "163.5°C is half of 327°C — the classic mistake of forgetting to convert to Kelvin!"
        },
        "videoTutorial": VIDEOS["phys_mech"]
    },
    {
        "id": 109,
        "subject": "Physics",
        "classLevel": "Class 11",
        "chapter": "Oscillations",
        "ncertRef": "NCERT Class 11 Physics, Ch 13 — Energy in Simple Harmonic Motion",
        "pyqTag": "NEET PYQ Pattern",
        "questionType": "Numerical MCQ",
        "difficulty": "Medium",
        "stem_en": "A particle executes linear simple harmonic motion with amplitude A. At what displacement from the mean position is its kinetic energy equal to its potential energy?",
        "stem_ta": "துகள் ஒன்று A என்ற வீச்சுடன் நேர்க்கோட்டு தனிச்சீரான இயக்கத்தை (SHM) மேற்கொள்கிறது. மையப்புள்ளியிலிருந்து எந்த இடப்பெயர்ச்சியில் அதன் இயக்க ஆற்றலும் நிலை ஆற்றலும் சமமாக இருக்கும்?",
        "choices": [
            {"letter": "A", "text_en": "$\\frac{A}{2}$", "text_ta": "$\\frac{A}{2}$"},
            {"letter": "B", "text_en": "$\\frac{A}{\\sqrt{2}}$", "text_ta": "$\\frac{A}{\\sqrt{2}}$"},
            {"letter": "C", "text_en": "$\\frac{A}{\\sqrt{3}}$", "text_ta": "$\\frac{A}{\\sqrt{3}}$"},
            {"letter": "D", "text_en": "$\\frac{\\sqrt{3}A}{2}$", "text_ta": "$\\frac{\\sqrt{3}A}{2}$"}
        ],
        "correct": "B",
        "explanation_en": "$KE = \\frac{1}{2}m\\omega^2(A^2 - x^2)$ and $PE = \\frac{1}{2}m\\omega^2 x^2$. Equating $KE = PE$ gives $A^2 - x^2 = x^2 \\Rightarrow 2x^2 = A^2 \\Rightarrow x = \\frac{A}{\\sqrt{2}}$.",
        "explanation_ta": "$KE = \\frac{1}{2}m\\omega^2(A^2 - x^2)$ மற்றும் $PE = \\frac{1}{2}m\\omega^2 x^2$. இரண்டும் சமம் எனில் $A^2 - x^2 = x^2 \\Rightarrow x = \\frac{A}{\\sqrt{2}}$.",
        "ncert_key_point": "Since PE ∝ x^2, PE equals 50% of total energy at x = A/sqrt(2) ≈ 0.707 A, not A/2.",
        "trap_breakdown": {
            "A": "At x = A/2, PE is 25% and KE is 75% of total energy.",
            "C": "At x = A/sqrt(3), KE = 2 * PE.",
            "D": "At x = A*sqrt(3)/2, PE = 3 * KE."
        },
        "videoTutorial": VIDEOS["phys_mech"]
    },
    {
        "id": 110,
        "subject": "Physics",
        "classLevel": "Class 12",
        "chapter": "Electrostatic Potential and Capacitance",
        "ncertRef": "NCERT Class 12 Physics, Ch 2 — Parallel Plate Capacitor",
        "pyqTag": "NEET 2020 / 2024 Pattern",
        "questionType": "Numerical MCQ",
        "difficulty": "Medium",
        "stem_en": "An air-filled parallel plate capacitor has capacitance 15 pF. When the separation between plates is doubled and the space is completely filled with a dielectric medium of dielectric constant K = 4, the new capacitance becomes:",
        "stem_ta": "காற்று நிரப்பப்பட்ட இணைத்தட்டு மின்தேக்கியின் மின்தேக்குத்திறன் 15 pF ஆகும். தட்டுகளுக்கு இடையிலான தொலைவு இருமடங்காக்கப்பட்டு, K = 4 கொண்ட மின்காப்பு ஊடகத்தால் நிரப்பப்பட்டால் புதிய மின்தேக்குத்திறன் என்ன?",
        "choices": [
            {"letter": "A", "text_en": "30 pF", "text_ta": "30 pF"},
            {"letter": "B", "text_en": "60 pF", "text_ta": "60 pF"},
            {"letter": "C", "text_en": "7.5 pF", "text_ta": "7.5 pF"},
            {"letter": "D", "text_en": "120 pF", "text_ta": "120 pF"}
        ],
        "correct": "A",
        "explanation_en": "$C_0 = \\frac{\\varepsilon_0 A}{d} = 15\\text{ pF}$. With $d' = 2d$ and $K = 4$, $C' = \\frac{K \\varepsilon_0 A}{2d} = \\frac{4}{2} C_0 = 2 \\times 15\\text{ pF} = 30\\text{ pF}$.",
        "explanation_ta": "$C_0 = \\frac{\\varepsilon_0 A}{d} = 15\\text{ pF}$. $d' = 2d$ மற்றும் $K = 4$ எனில், $C' = \\frac{4}{2} \\times 15\\text{ pF} = 30\\text{ pF}$.",
        "ncert_key_point": "$C = \\frac{K \\varepsilon_0 A}{d}$: scale initial $C_0$ directly by $\\frac{K_{\\text{new}}}{K_{\\text{old}}} \\times \\frac{d_{\\text{old}}}{d_{\\text{new}}}$.",
        "trap_breakdown": {
            "B": "60 pF multiplies by K=4 without dividing by 2 for doubled plate separation.",
            "C": "7.5 pF divides by K instead of multiplying.",
            "D": "120 pF multiplies by both 4 and 2."
        },
        "videoTutorial": VIDEOS["phys_elec"]
    },
    {
        "id": 111,
        "subject": "Physics",
        "classLevel": "Class 12",
        "chapter": "Current Electricity",
        "ncertRef": "NCERT Class 12 Physics, Ch 3 — Resistivity & Wire Stretching",
        "pyqTag": "NEET High-Frequency PYQ",
        "questionType": "Numerical MCQ",
        "difficulty": "Medium",
        "stem_en": "A wire of resistance 10 Ω is uniformly stretched so that its length becomes 3 times its original length (volume remaining constant). Its new resistance is:",
        "stem_ta": "10 Ω மின்தடை கொண்ட கம்பி ஒன்று அதன் பருமன் மாறாமல் நீளம் மும்மடங்காகுமாறு சீராக இழுக்கப்படுகிறது. அதன் புதிய மின்தடை என்ன?",
        "choices": [
            {"letter": "A", "text_en": "30 Ω", "text_ta": "30 Ω"},
            {"letter": "B", "text_en": "90 Ω", "text_ta": "90 Ω"},
            {"letter": "C", "text_en": "$\\frac{10}{3}\\ \\Omega$", "text_ta": "$\\frac{10}{3}\\ \\Omega$"},
            {"letter": "D", "text_en": "60 Ω", "text_ta": "60 Ω"}
        ],
        "correct": "B",
        "explanation_en": "At constant volume V = A * L, stretching L' = 3L causes cross-sectional area to become A' = A/3. Hence R' = ρ L' / A' = 9 * (ρ L / A) = 3^2 * 10 Ω = 90 Ω.",
        "explanation_ta": "பருமன் மாறாமல் கம்பியை n மடங்கு நீட்டும்போது பரப்பு A' = A/n ஆகும். எனவே புதிய மின்தடை R' = n^2 * R = 3^2 * 10 Ω = 90 Ω.",
        "ncert_key_point": "Stretched to n times length => R' = n^2 R. Stretched to 1/n radius => R' = n^4 R.",
        "trap_breakdown": {
            "A": "30 Ω uses R' = nR, ignoring that area shrinks by factor 3.",
            "C": "Dividing instead of multiplying.",
            "D": "Using 2n instead of n^2."
        },
        "videoTutorial": VIDEOS["phys_elec"]
    },
    {
        "id": 112,
        "subject": "Physics",
        "classLevel": "Class 12",
        "chapter": "Current Electricity",
        "ncertRef": "NCERT Class 12 Physics, Ch 3 — Balanced Wheatstone Bridge",
        "pyqTag": "NEET 2024 Official Pattern",
        "questionType": "Numerical MCQ",
        "difficulty": "Medium",
        "stem_en": "In a Wheatstone bridge, the upper branch has 4 Ω and 6 Ω resistors in series, the lower branch has 8 Ω and 12 Ω resistors in series, and a 10 Ω galvanometer connects their midpoints. If an ideal 20 V battery is connected across the bridge ends, the total current drawn from the battery is:",
        "stem_ta": "வீட்ஸ்டோன் சமனச்சுற்றில் மேல் கிளையில் 4 Ω, 6 Ω மின்தடைகள் தொடரிணைப்பிலும், கீழ் கிளையில் 8 Ω, 12 Ω மின்தடைகள் தொடரிணைப்பிலும் உள்ளன. அவற்றின் நடுப்புள்ளிகளுக்கிடையே 10 Ω கால்வனாமீட்டரும், முனைகளில் 20 V மின்கலமும் இணைக்கப்பட்டால் மின்கலத்திலிருந்து பாயும் மொத்த மின்னோட்டம்:",
        "choices": [
            {"letter": "A", "text_en": "3.0 A", "text_ta": "3.0 A"},
            {"letter": "B", "text_en": "2.0 A", "text_ta": "2.0 A"},
            {"letter": "C", "text_en": "1.5 A", "text_ta": "1.5 A"},
            {"letter": "D", "text_en": "4.0 A", "text_ta": "4.0 A"}
        ],
        "correct": "A",
        "explanation_en": "Ratio check: 4 / 6 = 2/3 and 8 / 12 = 2/3. Because the bridge is balanced, zero current flows through the 10 Ω galvanometer (remove it!). Upper series branch = 4 + 6 = 10 Ω; lower series branch = 8 + 12 = 20 Ω in parallel. R_eq = (10 * 20)/(10 + 20) = 20/3 Ω. Total current I = V / R_eq = 20 / (20/3) = 3.0 A.",
        "explanation_ta": "4/6 = 8/12 = 2/3 என்பதால் சமனச்சுற்று சமநிலையில் உள்ளது; 10 Ω வழியே மின்னோட்டம் பாயாது. மேல் கிளை = 10 Ω, கீழ் கிளை = 20 Ω பக்க இணைப்பில் உள்ளன. R_eq = 20/3 Ω. எனவே I = 20 / (20/3) = 3.0 A.",
        "ncert_key_point": "Always check P/Q = R/S first before attempting Kirchhoff's loop equations!",
        "trap_breakdown": {
            "B": "2.0 A considers only the 10 Ω upper branch.",
            "C": "1.5 A miscalculates parallel combination.",
            "D": "4.0 A includes the central 10 Ω resistor in parallel."
        },
        "videoTutorial": VIDEOS["phys_elec"]
    },
    {
        "id": 113,
        "subject": "Physics",
        "classLevel": "Class 12",
        "chapter": "Moving Charges and Magnetism",
        "ncertRef": "NCERT Class 12 Physics, Ch 4 — Motion in a Magnetic Field",
        "pyqTag": "NEET Classic PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "A proton and an alpha particle enter a uniform magnetic field perpendicular to their velocities with the same kinetic energy. The ratio of the radii of their circular paths (r_proton : r_alpha) is:",
        "stem_ta": "புரோட்டான் ஒன்றும் ஆல்பா துகள் ஒன்றும் சம இயக்க ஆற்றலுடன் சீரான காந்தப்புலத்திற்குச் செங்குத்தாக நுழைகின்றன. அவற்றின் வட்டப் பாதைகளின் ஆரங்களின் விகிதம் (r_புரோட்டான் : r_ஆல்பா):",
        "choices": [
            {"letter": "A", "text_en": "1 : 1", "text_ta": "1 : 1"},
            {"letter": "B", "text_en": "1 : 2", "text_ta": "1 : 2"},
            {"letter": "C", "text_en": "2 : 1", "text_ta": "2 : 1"},
            {"letter": "D", "text_en": "1 : 4", "text_ta": "1 : 4"}
        ],
        "correct": "A",
        "explanation_en": "Radius in magnetic field in terms of kinetic energy K is r = sqrt(2mK) / (qB). For alpha particle, m_α = 4 m_p and q_α = 2 q_p. At same K and B, r_p / r_α = [sqrt(m_p) / q_p] / [sqrt(4 m_p) / (2 q_p)] = 1 / (2/2) = 1 : 1.",
        "explanation_ta": "காந்தப்புலத்தில் ஆரம் r = sqrt(2mK) / (qB). ஆல்பா துகளுக்கு m_α = 4 m_p மற்றும் q_α = 2 q_p. K, B சமம் எனில் r_α = sqrt(4)/2 * r_p = r_p. எனவே விகிதம் 1 : 1.",
        "ncert_key_point": "Same KE => r_p : r_d : r_α = 1 : sqrt(2) : 1. Same velocity => r ∝ m/q => 1 : 2 : 2.",
        "trap_breakdown": {
            "B": "1 : 2 is the ratio when they enter with the SAME VELOCITY, not same kinetic energy!",
            "C": "2 : 1 is the ratio when accelerated through the SAME POTENTIAL DIFFERENCE (r ∝ sqrt(m)/q => 1 : 1/sqrt(2), or inverted).",
            "D": "1 : 4 forgets both square root on mass and factor 2 on charge."
        },
        "videoTutorial": VIDEOS["phys_elec"]
    },
    {
        "id": 114,
        "subject": "Physics",
        "classLevel": "Class 12",
        "chapter": "Alternating Current",
        "ncertRef": "NCERT Class 12 Physics, Ch 7 — Series LCR Resonance",
        "pyqTag": "NEET 2023 / 2024 PYQ",
        "questionType": "Numerical MCQ",
        "difficulty": "Easy",
        "stem_en": "A series LCR circuit has inductance L = 10 mH, capacitance C = 1 μF, and resistance R = 50 Ω. The angular frequency (ω_0) at which resonance occurs is:",
        "stem_ta": "தொடர் LCR சுற்றில் மின்தூண்டல் L = 10 mH, மின்தேக்குத்திறன் C = 1 μF மற்றும் மின்தடை R = 50 Ω உள்ளது. ஒத்ததிர்வு நிகழும் கோண அதிர்வெண் (ω_0) என்ன?",
        "choices": [
            {"letter": "A", "text_en": "10^4 rad/s", "text_ta": "10^4 rad/s"},
            {"letter": "B", "text_en": "10^5 rad/s", "text_ta": "10^5 rad/s"},
            {"letter": "C", "text_en": "10^3 rad/s", "text_ta": "10^3 rad/s"},
            {"letter": "D", "text_en": "2 * 10^4 rad/s", "text_ta": "2 * 10^4 rad/s"}
        ],
        "correct": "A",
        "explanation_en": "Resonant angular frequency ω_0 = 1 / sqrt(LC) is independent of R! Here L = 10 * 10^-3 H = 10^-2 H and C = 10^-6 F, so LC = 10^-8 s^2. Thus ω_0 = 1 / sqrt(10^-8) = 10^4 rad/s.",
        "explanation_ta": "ஒத்ததிர்வு கோண அதிர்வெண் ω_0 = 1 / sqrt(LC) (R-ஐச் சார்ந்ததல்ல). L = 10^-2 H, C = 10^-6 F => LC = 10^-8 => ω_0 = 10^4 rad/s.",
        "ncert_key_point": "Watch units: 10 mH = 10^-2 H (not 10^-3 H!), and distinguish ω_0 (rad/s) from f_0 = ω_0 / (2π) (Hz).",
        "trap_breakdown": {
            "B": "10^5 rad/s misreads 10 mH as 10^-4 H.",
            "C": "10^3 rad/s misreads 1 μF as 10^-4 F.",
            "D": "Unnecessary factor from R = 50 Ω."
        },
        "videoTutorial": VIDEOS["phys_elec"]
    },
    {
        "id": 115,
        "subject": "Physics",
        "classLevel": "Class 12",
        "chapter": "Ray Optics and Optical Instruments",
        "ncertRef": "NCERT Class 12 Physics, Ch 9 — Lens Maker's Formula",
        "pyqTag": "NEET 2023 / 2025 Pattern",
        "questionType": "Numerical MCQ",
        "difficulty": "Medium",
        "stem_en": "A biconvex lens made of glass (refractive index n_g = 1.5) has focal length 20 cm in air. When completely immersed in a transparent liquid of refractive index n_l = 1.25, its focal length becomes:",
        "stem_ta": "கண்ணாடியால் (ஒளிவிலகல் எண் n_g = 1.5) செய்யப்பட்ட இருகுவி லென்ஸின் காற்றில் குவியத்தூரம் 20 cm ஆகும். n_l = 1.25 ஒளிவிலகல் எண் கொண்ட திரவத்தில் முழுமையாக மூழ்கடிக்கப்படும்போது அதன் புதிய குவியத்தூரம்:",
        "choices": [
            {"letter": "A", "text_en": "+50 cm", "text_ta": "+50 cm"},
            {"letter": "B", "text_en": "+25 cm", "text_ta": "+25 cm"},
            {"letter": "C", "text_en": "-50 cm", "text_ta": "-50 cm"},
            {"letter": "D", "text_en": "+40 cm", "text_ta": "+40 cm"}
        ],
        "correct": "A",
        "explanation_en": "By Lens Maker's formula: (1/f_air) / (1/f_liq) = f_liq / f_air = (n_g - 1) / ((n_g / n_l) - 1). Here n_g - 1 = 0.5, and (1.5 / 1.25) - 1 = 1.2 - 1 = 0.2. So f_liq / 20 = 0.5 / 0.2 = 2.5 => f_liq = +50 cm.",
        "explanation_ta": "லென்ஸ் உருவாக்குபவர் சமன்பாட்டின்படி: f_திரவம் / f_காற்று = (n_g - 1) / ((n_g / n_l) - 1) = (1.5 - 1) / ((1.5/1.25) - 1) = 0.5 / 0.2 = 2.5. எனவே f_திரவம் = 2.5 * 20 = +50 cm.",
        "ncert_key_point": "When n_liquid < n_glass, a convex lens stays converging (+f) with a LARGER focal length; if n_liquid > n_glass, it turns diverging (-f)!",
        "trap_breakdown": {
            "B": "25 cm uses n_g - n_l = 0.25 instead of (n_g / n_l) - 1 = 0.20!",
            "C": "-50 cm wrongly flips sign (sign flips only if n_l > 1.5).",
            "D": "40 cm doubles focal length by guessing."
        },
        "videoTutorial": VIDEOS["phys_opt_mod"]
    },
    {
        "id": 116,
        "subject": "Physics",
        "classLevel": "Class 12",
        "chapter": "Wave Optics",
        "ncertRef": "NCERT Class 12 Physics, Ch 10 — Young's Double-Slit Experiment",
        "pyqTag": "NEET 2024 Official Pattern",
        "questionType": "Numerical MCQ",
        "difficulty": "Easy",
        "stem_en": "In Young's double-slit experiment, the slit separation is 1.0 mm and the screen is placed 1.5 m away. When monochromatic light of wavelength 600 nm is used, the fringe width is:",
        "stem_ta": "யங் இரட்டைப் பிளவு சோதனையில் பிளவுகளுக்கு இடையிலான தொலைவு 1.0 mm மற்றும் திரை 1.5 m தொலைவில் உள்ளது. 600 nm அலைநீளம் கொண்ட ஒற்றைநிற ஒளி பயன்படுத்தப்படும்போது பட்டை அகலம் (fringe width) என்ன?",
        "choices": [
            {"letter": "A", "text_en": "0.9 mm", "text_ta": "0.9 mm"},
            {"letter": "B", "text_en": "0.6 mm", "text_ta": "0.6 mm"},
            {"letter": "C", "text_en": "1.2 mm", "text_ta": "1.2 mm"},
            {"letter": "D", "text_en": "0.4 mm", "text_ta": "0.4 mm"}
        ],
        "correct": "A",
        "explanation_en": "Fringe width β = λD / d = (600 * 10^-9 m * 1.5 m) / (1.0 * 10^-3 m) = 900 * 10^-6 m = 0.9 * 10^-3 m = 0.9 mm.",
        "explanation_ta": "பட்டை அகலம் β = λD / d = (600 * 10^-9 * 1.5) / (1.0 * 10^-3) = 0.9 * 10^-3 m = 0.9 mm.",
        "ncert_key_point": "β = λD / d: convert nm (10^-9 m) and mm (10^-3 m) cleanly before multiplying.",
        "trap_breakdown": {
            "B": "0.6 mm forgets to multiply by D = 1.5 m.",
            "C": "1.2 mm multiplies by 2 instead of 1.5.",
            "D": "0.4 mm divides by 1.5 instead of multiplying."
        },
        "videoTutorial": VIDEOS["phys_opt_mod"]
    },
    {
        "id": 117,
        "subject": "Physics",
        "classLevel": "Class 12",
        "chapter": "Dual Nature of Radiation and Matter",
        "ncertRef": "NCERT Class 12 Physics, Ch 11 — Photoelectric Effect & de Broglie Wavelength",
        "pyqTag": "NEET 2023 Official PYQ",
        "questionType": "Numerical MCQ",
        "difficulty": "Easy",
        "stem_en": "The work function of Caesium is 2.14 eV. If incident light has photon energy 3.54 eV, the stopping potential (V_0) of the emitted photoelectrons is:",
        "stem_ta": "சீசியத்தின் வெளியேற்று ஆற்றல் (work function) 2.14 eV ஆகும். படும் ஒளியின் ஃபோட்டான் ஆற்றல் 3.54 eV எனில், உமிழப்படும் ஒளி எலக்ட்ரான்களின் நிறுத்து மின்னழுத்தம் (stopping potential V_0) என்ன?",
        "choices": [
            {"letter": "A", "text_en": "1.40 V", "text_ta": "1.40 V"},
            {"letter": "B", "text_en": "5.68 V", "text_ta": "5.68 V"},
            {"letter": "C", "text_en": "2.14 V", "text_ta": "2.14 V"},
            {"letter": "D", "text_en": "0.70 V", "text_ta": "0.70 V"}
        ],
        "correct": "A",
        "explanation_en": "By Einstein's photoelectric equation: K_max = e * V_0 = hν - φ_0 = 3.54 eV - 2.14 eV = 1.40 eV. Dividing by elementary charge e gives V_0 = 1.40 V.",
        "explanation_ta": "ஐன்ஸ்டீனின் ஒளிமின் சமன்பாட்டின்படி: e * V_0 = hν - φ_0 = 3.54 eV - 2.14 eV = 1.40 eV. எனவே நிறுத்து மின்னழுத்தம் V_0 = 1.40 V.",
        "ncert_key_point": "When K_max is in electron-volts (eV), stopping potential V_0 in Volts has the exact same numerical value!",
        "trap_breakdown": {
            "B": "5.68 V adds hν and φ_0 instead of subtracting.",
            "C": "2.14 V confuses threshold energy with stopping potential.",
            "D": "0.70 V divides K_max by 2."
        },
        "videoTutorial": VIDEOS["phys_opt_mod"]
    },
    {
        "id": 118,
        "subject": "Physics",
        "classLevel": "Class 12",
        "chapter": "Atoms",
        "ncertRef": "NCERT Class 12 Physics, Ch 12 — Bohr Model of Hydrogen Atom",
        "pyqTag": "NEET PYQ Pattern",
        "questionType": "Numerical MCQ",
        "difficulty": "Easy",
        "stem_en": "The ground state energy of a hydrogen atom is -13.6 eV. The energy required to excite the electron from the ground state (n = 1) to the first excited state (n = 2) is:",
        "stem_ta": "ஹைட்ரஜன் அணுவின் அடிநிலை ஆற்றல் -13.6 eV ஆகும். எலக்ட்ரானை அடிநிலையிலிருந்து (n = 1) முதல் கிளர்வு நிலைக்கு (n = 2) கிளர்வுறச் செய்யத் தேவைப்படும் ஆற்றல்:",
        "choices": [
            {"letter": "A", "text_en": "3.4 eV", "text_ta": "3.4 eV"},
            {"letter": "B", "text_en": "10.2 eV", "text_ta": "10.2 eV"},
            {"letter": "C", "text_en": "12.09 eV", "text_ta": "12.09 eV"},
            {"letter": "D", "text_en": "13.6 eV", "text_ta": "13.6 eV"}
        ],
        "correct": "B",
        "explanation_en": "First excited state corresponds to n = 2 (NOT n = 1!). E_2 = -13.6 / 2^2 = -3.4 eV. Excitation energy ΔE = E_2 - E_1 = -3.4 - (-13.6) = +10.2 eV.",
        "explanation_ta": "முதல் கிளர்வு நிலை என்பது n = 2 ஆகும்! E_2 = -13.6 / 4 = -3.4 eV. தேவைப்படும் ஆற்றல் ΔE = E_2 - E_1 = -3.4 - (-13.6) = 10.2 eV.",
        "ncert_key_point": "First excited state = n=2 (+10.2 eV); Second excited state = n=3 (+12.09 eV); Ionization = n=∞ (+13.6 eV).",
        "trap_breakdown": {
            "A": "3.4 eV is |E_2| (binding energy of n=2), not E_2 - E_1!",
            "C": "12.09 eV is excitation to the SECOND excited state (n = 3).",
            "D": "13.6 eV is the ionization energy from ground state."
        },
        "videoTutorial": VIDEOS["phys_opt_mod"]
    },
    {
        "id": 119,
        "subject": "Physics",
        "classLevel": "Class 12",
        "chapter": "Nuclei",
        "ncertRef": "NCERT Class 12 Physics, Ch 13 — Nuclear Size",
        "pyqTag": "NEET 2022 Official PYQ",
        "questionType": "Numerical MCQ",
        "difficulty": "Easy",
        "stem_en": "Two nuclei have mass numbers in the ratio 27 : 125. What is the ratio of their nuclear radii?",
        "stem_ta": "இரண்டு அணுக்கருக்களின் நிறை எண்களின் விகிதம் 27 : 125 எனில், அவற்றின் அணுக்கரு ஆரங்களின் விகிதம் என்ன?",
        "choices": [
            {"letter": "A", "text_en": "3 : 5", "text_ta": "3 : 5"},
            {"letter": "B", "text_en": "9 : 25", "text_ta": "9 : 25"},
            {"letter": "C", "text_en": "27 : 125", "text_ta": "27 : 125"},
            {"letter": "D", "text_en": "1 : 1", "text_ta": "1 : 1"}
        ],
        "correct": "A",
        "explanation_en": "Nuclear radius R = R_0 * A^(1/3). Hence R_1 / R_2 = (A_1 / A_2)^(1/3) = (27 / 125)^(1/3) = 3 / 5.",
        "explanation_ta": "அணுக்கரு ஆரம் R = R_0 * A^(1/3). எனவே R_1 / R_2 = (27 / 125)^(1/3) = 3 : 5. (அணுக்கரு அடர்த்தி 1 : 1 மாறிலியாக இருக்கும்!)",
        "ncert_key_point": "Nuclear radius R ∝ A^(1/3), surface area ∝ A^(2/3), volume ∝ A, and nuclear density is CONSTANT (1 : 1) independent of A!",
        "trap_breakdown": {
            "B": "9 : 25 is the ratio of nuclear surface areas (A^(2/3)).",
            "C": "27 : 125 is the ratio of nuclear volumes (A).",
            "D": "1 : 1 is the ratio of nuclear DENSITIES, not radii!"
        },
        "videoTutorial": VIDEOS["phys_opt_mod"]
    },
    {
        "id": 120,
        "subject": "Physics",
        "classLevel": "Class 12",
        "chapter": "Semiconductor Electronics",
        "ncertRef": "NCERT Class 12 Physics, Ch 14 — Digital Electronics & Logic Gates",
        "pyqTag": "NEET Mandatory Annual Topic (2023/2024)",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "The output of a 2-input NOR gate is connected directly to the input of a NOT gate. This logic circuit is equivalent to an:",
        "stem_ta": "இரு-உள்ளீடு கொண்ட NOR வாயிலின் (gate) வெளியீடு, ஒரு NOT வாயிலின் உள்ளீட்டுடன் நேரடியாக இணைக்கப்பட்டுள்ளது. இந்த மின்சுற்று எந்த வாயிலுக்குச் சமமானது?",
        "choices": [
            {"letter": "A", "text_en": "OR gate", "text_ta": "OR வாயில்"},
            {"letter": "B", "text_en": "AND gate", "text_ta": "AND வாயில்"},
            {"letter": "C", "text_en": "NAND gate", "text_ta": "NAND வாயில்"},
            {"letter": "D", "text_en": "NOR gate", "text_ta": "NOR வாயில்"}
        ],
        "correct": "A",
        "explanation_en": "Output of NOR gate is Y_1 = NOT(A + B). Passing Y_1 through a NOT gate inverts it again: Y = NOT(NOT(A + B)) = A + B, which is the Boolean expression of an OR gate!",
        "explanation_ta": "NOR வாயிலின் வெளியீடு Y_1 = பார்(A + B). இதை NOT வாயில் வழியே செலுத்தினால் Y = இரட்டை பார்(A + B) = A + B, இது OR வாயிலுக்குச் சமம்!",
        "ncert_key_point": "Always verify logic gate MCQs in 10 seconds by plugging the 4 truth-table rows (00, 01, 10, 11).",
        "trap_breakdown": {
            "B": "AND gate comes from NAND followed by NOT.",
            "C": "NAND is NOT(A·B).",
            "D": "Forgetting the final NOT inversion."
        },
        "videoTutorial": VIDEOS["phys_opt_mod"]
    },
]

CHEMISTRY_QUESTIONS = [
    {
        "id": 201,
        "subject": "Chemistry",
        "classLevel": "Class 11",
        "chapter": "Some Basic Concepts of Chemistry",
        "ncertRef": "NCERT Class 11 Chemistry, Ch 1 — Stoichiometry & Percentage Purity",
        "pyqTag": "NEET 2022 Official PYQ",
        "questionType": "Numerical MCQ",
        "difficulty": "Medium",
        "stem_en": "What mass of 95% pure CaCO3 will be required to neutralize 50 mL of 0.5 M HCl solution according to the reaction: CaCO3(s) + 2HCl(aq) -> CaCl2(aq) + CO2(g) + H2O(l)? [Molar mass of CaCO3 = 100 g/mol]",
        "stem_ta": "CaCO3(s) + 2HCl(aq) -> CaCl2(aq) + CO2(g) + H2O(l) என்ற வினையின்படி, 50 mL அளவுள்ள 0.5 M HCl கரைசலை நடுநிலையாக்க 95% தூய்மையான CaCO3 எவ்வளவு நிறை தேவைப்படும்? [CaCO3 மோலார் நிறை = 100 g/mol]",
        "choices": [
            {"letter": "A", "text_en": "1.25 g", "text_ta": "1.25 g"},
            {"letter": "B", "text_en": "1.32 g", "text_ta": "1.32 g"},
            {"letter": "C", "text_en": "3.65 g", "text_ta": "3.65 g"},
            {"letter": "D", "text_en": "9.50 g", "text_ta": "9.50 g"}
        ],
        "correct": "B",
        "explanation_en": "Moles of HCl = M * V(L) = 0.5 * 0.050 = 0.025 mol. From stoichiometry, 1 mol CaCO3 reacts with 2 mol HCl, so pure CaCO3 needed = 0.025 / 2 = 0.0125 mol = 0.0125 * 100 g = 1.25 g. Since sample is 95% pure, required sample mass = 1.25 / 0.95 = 1.3158 g ≈ 1.32 g.",
        "explanation_ta": "HCl மோல்கள் = 0.5 * 0.050 = 0.025 mol. தூய CaCO3 மோல்கள் = 0.025 / 2 = 0.0125 mol = 1.25 g. மாதிரி 95% தூய்மையானது என்பதால் தேவையான நிறை = 1.25 / 0.95 = 1.316 g ≈ 1.32 g.",
        "ncert_key_point": "Impure sample mass is ALWAYS greater than pure reactant mass: divide pure mass by (% purity / 100).",
        "trap_breakdown": {
            "A": "1.25 g stops at pure CaCO3 mass and forgets to account for 95% purity!",
            "C": "Confuses molar mass of HCl (36.5) with CaCO3.",
            "D": "Decimal shift error."
        },
        "videoTutorial": VIDEOS["chem_phys"]
    },
    {
        "id": 202,
        "subject": "Chemistry",
        "classLevel": "Class 11",
        "chapter": "Structure of Atom",
        "ncertRef": "NCERT Class 11 Chemistry, Ch 2 — Quantum Numbers & Orbitals",
        "pyqTag": "NEET Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "What is the maximum number of orbitals that can be identified with the following quantum numbers: n = 3, l = 1, m_l = 0?",
        "stem_ta": "n = 3, l = 1, m_l = 0 ஆகிய குவாண்டம் எண்களால் அடையாளம் காணக்கூடிய அதிகபட்ச ஆர்பிட்டால்களின் எண்ணிக்கை எவ்வளவு?",
        "choices": [
            {"letter": "A", "text_en": "1", "text_ta": "1"},
            {"letter": "B", "text_en": "2", "text_ta": "2"},
            {"letter": "C", "text_en": "3", "text_ta": "3"},
            {"letter": "D", "text_en": "4", "text_ta": "4"}
        ],
        "correct": "A",
        "explanation_en": "A specific set of three quantum numbers (n, l, m_l) uniquely identifies ONE single orbital (here, the 3p_z orbital). That 1 orbital can hold up to 2 electrons (m_s = +1/2, -1/2), so number of ORBITALS = 1.",
        "explanation_ta": "(n, l, m_l) ஆகிய மூன்று குவாண்டம் எண்களின் குறிப்பிட்ட தொகுப்பு ஒரே ஒரு ஆர்பிட்டாலை (3p_z) மட்டுமே குறிக்கும். இதில் அதிகபட்சம் 2 எலக்ட்ரான்கள் இருக்கலாம், ஆனால் ஆர்பிட்டாலின் எண்ணிக்கை = 1.",
        "ncert_key_point": "Read the noun carefully: (n, l, m_l) -> 1 orbital, max 2 electrons!",
        "trap_breakdown": {
            "B": "2 is the maximum number of ELECTRONS in that orbital, not orbitals!",
            "C": "3 is the total number of orbitals in the entire 3p subshell (m_l = -1, 0, +1).",
            "D": "Confusing with l + 3."
        },
        "videoTutorial": VIDEOS["chem_phys"]
    },
    {
        "id": 203,
        "subject": "Chemistry",
        "classLevel": "Class 11",
        "chapter": "Classification of Elements and Periodicity",
        "ncertRef": "NCERT Class 11 Chemistry, Ch 3 — Ionic Radii of Isoelectronic Species",
        "pyqTag": "NEET High-Frequency PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Among the isoelectronic species N^3-, O^2-, F^-, and Na^+, the correct decreasing order of ionic radius is:",
        "stem_ta": "ஒத்த எலக்ட்ரான் எண்ணிக்கை கொண்ட N^3-, O^2-, F^- மற்றும் Na^+ அயனிகளில், அயனி ஆரத்தின் சரியான இறங்கு வரிசை எது?",
        "choices": [
            {"letter": "A", "text_en": "Na^+ > F^- > O^2- > N^3-", "text_ta": "Na^+ > F^- > O^2- > N^3-"},
            {"letter": "B", "text_en": "N^3- > O^2- > F^- > Na^+", "text_ta": "N^3- > O^2- > F^- > Na^+"},
            {"letter": "C", "text_en": "O^2- > N^3- > F^- > Na^+", "text_ta": "O^2- > N^3- > F^- > Na^+"},
            {"letter": "D", "text_en": "N^3- > F^- > O^2- > Na^+", "text_ta": "N^3- > F^- > O^2- > Na^+"}
        ],
        "correct": "B",
        "explanation_en": "All four ions have 10 electrons. For isoelectronic species, ionic radius is inversely proportional to nuclear charge (Z): N^3- (Z=7) > O^2- (Z=8) > F^- (Z=9) > Na^+ (Z=11).",
        "explanation_ta": "நான்கு அயனிகளிலும் 10 எலக்ட்ரான்கள் உள்ளன. ஒத்த எலக்ட்ரான் அயனிகளில் அணு எண் (Z) அதிகரிக்கும்போது அயனி ஆரம் குறையும்: N^3- (Z=7) > O^2- (Z=8) > F^- (Z=9) > Na^+ (Z=11).",
        "ncert_key_point": "Isoelectronic species: More negative charge = Larger size; More positive charge = Smaller size.",
        "trap_breakdown": {
            "A": "Exact reverse (increasing order instead of decreasing order).",
            "C": "Swaps N^3- and O^2-.",
            "D": "Swaps O^2- and F^-."
        },
        "videoTutorial": VIDEOS["chem_inorg"]
    },
    {
        "id": 204,
        "subject": "Chemistry",
        "classLevel": "Class 11",
        "chapter": "Chemical Bonding and Molecular Structure",
        "ncertRef": "NCERT Class 11 Chemistry, Ch 4 — VSEPR Theory & Hybridisation",
        "pyqTag": "NEET 2023 / 2024 PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "According to VSEPR theory, the hybridisation of central atom and molecular geometry of XeF4 are respectively:",
        "stem_ta": "VSEPR கொள்கையின்படி, XeF4 மூலக்கூறின் மைய அணுவின் இனக்கலப்பு மற்றும் மூலக்கூறு வடிவம் முறையே:",
        "choices": [
            {"letter": "A", "text_en": "sp^3, Tetrahedral", "text_ta": "sp^3, நான்முகி (Tetrahedral)"},
            {"letter": "B", "text_en": "sp^3d^2, Octahedral", "text_ta": "sp^3d^2, எண்முகி (Octahedral)"},
            {"letter": "C", "text_en": "sp^3d^2, Square planar", "text_ta": "sp^3d^2, தள சதுரம் (Square planar)"},
            {"letter": "D", "text_en": "sp^3d, See-saw", "text_ta": "sp^3d, சீ-சா (See-saw)"}
        ],
        "correct": "C",
        "explanation_en": "Xenon has 8 valence electrons. In XeF4, there are 4 bond pairs and (8 - 4)/2 = 2 lone pairs. Steric number = 4 + 2 = 6 => sp^3d^2 hybridisation. Placing the 2 lone pairs trans (180°) to minimize repulsion gives a Square Planar molecular shape!",
        "explanation_ta": "செனானின் இணைதிறன் எலக்ட்ரான்கள் = 8. XeF4-இல் 4 பிணைப்பு இணைகள் + 2 தனித்த இணைகள் = 6 => sp^3d^2 இனக்கலப்பு. இரு தனித்த இணைகளும் எதிர் எதிரே அமைவதால் மூலக்கூறு வடிவம் தள சதுரம் (Square planar) ஆகும்!",
        "ncert_key_point": "Electron-pair geometry includes lone pairs (Octahedral), but Molecular geometry/shape counts ONLY atom positions (Square Planar)!",
        "trap_breakdown": {
            "A": "Ignores the two lone pairs on Xenon completely.",
            "B": "Octahedral is the electron-pair arrangement, NOT the molecular shape!",
            "D": "sp^3d See-saw belongs to SF4 (4 BP + 1 LP), not XeF4."
        },
        "videoTutorial": VIDEOS["chem_inorg"]
    },
    {
        "id": 205,
        "subject": "Chemistry",
        "classLevel": "Class 11",
        "chapter": "Chemical Bonding and Molecular Structure",
        "ncertRef": "NCERT Class 11 Chemistry, Ch 4 — Molecular Orbital Theory (MOT)",
        "pyqTag": "NEET Classic PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "According to Molecular Orbital Theory, the correct decreasing order of bond order among O2, O2^+, O2^-, and O2^2- is:",
        "stem_ta": "மூலக்கூறு ஆர்பிட்டால் கொள்கையின்படி (MOT), O2, O2^+, O2^- மற்றும் O2^2- ஆகியவற்றின் பிணைப்புத் தரத்தின் (bond order) சரியான இறங்கு வரிசை:",
        "choices": [
            {"letter": "A", "text_en": "O2^+ > O2 > O2^- > O2^2-", "text_ta": "O2^+ > O2 > O2^- > O2^2-"},
            {"letter": "B", "text_en": "O2 > O2^+ > O2^- > O2^2-", "text_ta": "O2 > O2^+ > O2^- > O2^2-"},
            {"letter": "C", "text_en": "O2^2- > O2^- > O2 > O2^+", "text_ta": "O2^2- > O2^- > O2 > O2^+"},
            {"letter": "D", "text_en": "O2^+ > O2^- > O2 > O2^2-", "text_ta": "O2^+ > O2^- > O2 > O2^2-"}
        ],
        "correct": "A",
        "explanation_en": "O2 (16 e^-) has 10 bonding and 6 antibonding electrons: BO = (10-6)/2 = 2.0. Removing an antibonding π* electron in O2^+ (15 e^-) raises BO to 2.5. Adding electrons into π* orbitals lowers BO: O2^- (17 e^-) has BO = 1.5, and O2^2- (18 e^-) has BO = 1.0.",
        "explanation_ta": "பிணைப்புத் தரம் (BO): O2^+ (15 e^-) = 2.5; O2 (16 e^-) = 2.0; O2^- (17 e^-) = 1.5; O2^2- (18 e^-) = 1.0. எனவே சரியான இறங்கு வரிசை O2^+ > O2 > O2^- > O2^2-.",
        "ncert_key_point": "14-electron shortcut: 14 e^- => BO = 3.0; every ±1 electron away from 14 reduces BO by 0.5 (so 15->2.5, 16->2.0, 17->1.5, 18->1.0)!",
        "trap_breakdown": {
            "B": "Assumes neutral O2 has higher bond order than O2^+.",
            "C": "Gives bond LENGTH order (inverse of bond order) instead of bond order!",
            "D": "Scrambles O2 and O2^-."
        },
        "videoTutorial": VIDEOS["chem_inorg"]
    },
    {
        "id": 206,
        "subject": "Chemistry",
        "classLevel": "Class 11",
        "chapter": "Thermodynamics",
        "ncertRef": "NCERT Class 11 Chemistry, Ch 5 — Gibbs Energy & Spontaneity",
        "pyqTag": "NEET PYQ Pattern",
        "questionType": "Numerical MCQ",
        "difficulty": "Medium",
        "stem_en": "For a certain reaction, ΔH = +30 kJ mol^-1 and ΔS = +100 J K^-1 mol^-1 (assumed independent of temperature). The reaction will be spontaneous at:",
        "stem_ta": "ஒரு வேதிவினைக்கு ΔH = +30 kJ mol^-1 மற்றும் ΔS = +100 J K^-1 mol^-1 ஆகும். இந்த வினை எப்போது தன்னிச்சையாக (spontaneous) நிகழும்?",
        "choices": [
            {"letter": "A", "text_en": "All temperatures", "text_ta": "அனைத்து வெப்பநிலைகளிலும்"},
            {"letter": "B", "text_en": "Temperatures above 300 K", "text_ta": "300 K-க்கு அதிகமான வெப்பநிலையில்"},
            {"letter": "C", "text_en": "Temperatures below 300 K", "text_ta": "300 K-க்கு குறைவான வெப்பநிலையில்"},
            {"letter": "D", "text_en": "Temperatures above 0.3 K", "text_ta": "0.3 K-க்கு அதிகமான வெப்பநிலையில்"}
        ],
        "correct": "B",
        "explanation_en": "Convert ΔH to Joules! ΔH = +30,000 J mol^-1, ΔS = +100 J K^-1 mol^-1. For spontaneity, ΔG = ΔH - TΔS < 0 => TΔS > ΔH => T > 30000 / 100 => T > 300 K.",
        "explanation_ta": "முதலில் ΔH-ஐ ஜூலுக்கு மாற்றவும்: ΔH = 30,000 J mol^-1. தன்னிச்சை வினைக்கு ΔG = ΔH - TΔS < 0 => T > ΔH / ΔS = 30000 / 100 = 300 K.",
        "ncert_key_point": "#1 NEET Thermodynamics trap: ΔH is given in kJ while ΔS is given in J! Always multiply ΔH by 1000.",
        "trap_breakdown": {
            "A": "Spontaneous at all T requires ΔH < 0 and ΔS > 0.",
            "C": "Reverses the inequality sign.",
            "D": "0.3 K forgets to convert 30 kJ into 30,000 J!"
        },
        "videoTutorial": VIDEOS["chem_phys"]
    },
    {
        "id": 207,
        "subject": "Chemistry",
        "classLevel": "Class 11",
        "chapter": "Equilibrium",
        "ncertRef": "NCERT Class 11 Chemistry, Ch 6 — Ionization of Acids & Water Contribution",
        "pyqTag": "NEET Classic NCERT Trap",
        "questionType": "Numerical MCQ",
        "difficulty": "Medium",
        "stem_en": "The pH of a very dilute 10^-8 M aqueous HCl solution at 25°C is approximately:",
        "stem_ta": "25°C வெப்பநிலையில் மிக நீர்த்த 10^-8 M HCl நீர்க்கரைசலின் pH மதிப்பு தோராயமாக:",
        "choices": [
            {"letter": "A", "text_en": "8.00", "text_ta": "8.00"},
            {"letter": "B", "text_en": "6.98", "text_ta": "6.98"},
            {"letter": "C", "text_en": "7.02", "text_ta": "7.02"},
            {"letter": "D", "text_en": "6.00", "text_ta": "6.00"}
        ],
        "correct": "B",
        "explanation_en": "An acid diluted in pure water at 25°C can NEVER become basic (pH > 7)! When [HCl] = 10^-8 M, H^+ from auto-ionization of water (~10^-7 M) must be included. Solving [H^+]([H^+] - 10^-8) = 10^-14 gives [H^+] ≈ 1.051 * 10^-7 M, so pH = -log(1.051 * 10^-7) ≈ 6.98.",
        "explanation_ta": "அமிலக் கரைசலின் pH எப்போதும் 7-ஐ விடக் குறைவாகவே இருக்கும் (காரமாக மாறாது)! நீரின் சுய அயனியாக்கத்திலிருந்து கிடைக்கும் H^+ (~10^-7 M) சேர்க்கப்படும்போது மொத்த [H^+] ≈ 1.05 * 10^-7 M => pH ≈ 6.98.",
        "ncert_key_point": "Very dilute strong acid (10^-8 M HCl) => pH just below 7 (~6.98). Very dilute strong base (10^-8 M NaOH) => pH just above 7 (~7.02).",
        "trap_breakdown": {
            "A": "8.00 blindly applies -log(10^-8) = 8, absurdly claiming HCl in water is basic!",
            "C": "7.02 is for 10^-8 M NaOH, not HCl.",
            "D": "6.00 overestimates H^+ concentration by 10x."
        },
        "videoTutorial": VIDEOS["chem_phys"]
    },
    {
        "id": 208,
        "subject": "Chemistry",
        "classLevel": "Class 12",
        "chapter": "Electrochemistry",
        "ncertRef": "NCERT Class 12 Chemistry, Ch 2 — Faraday's Laws of Electrolysis",
        "pyqTag": "NEET Official PYQ",
        "questionType": "Numerical MCQ",
        "difficulty": "Easy",
        "stem_en": "How many Faradays of electricity are required for the complete reduction of 1 mole of permanganate ions (MnO4^-) to Mn^2+ ions in acidic medium?",
        "stem_ta": "அமில ஊடகத்தில் 1 மோல் பெர்மாங்கனேட் அயனிகளை (MnO4^-) முழுமையாக Mn^2+ அயனிகளாக ஒடுக்க எத்தனை பாரடே (Faraday) மின்சாரம் தேவை?",
        "choices": [
            {"letter": "A", "text_en": "5 F", "text_ta": "5 F"},
            {"letter": "B", "text_en": "3 F", "text_ta": "3 F"},
            {"letter": "C", "text_en": "7 F", "text_ta": "7 F"},
            {"letter": "D", "text_en": "2 F", "text_ta": "2 F"}
        ],
        "correct": "A",
        "explanation_en": "Half-reaction: MnO4^- + 8H^+ + 5e^- -> Mn^2+ + 4H2O. Oxidation state of Mn changes from +7 (in MnO4^-) to +2 (in Mn^2+), requiring 5 moles of electrons per mole of MnO4^-, which equals 5 Faradays (5 F).",
        "explanation_ta": "MnO4^- இல் Mn-இன் ஆக்சிஜனேற்ற எண் +7. இது Mn^2+ (+2) ஆக மாற 1 மோலுக்கு 5 மோல் எலக்ட்ரான்கள் தேவை. எனவே தேவையான மின்னூட்டம் = 5 பாரடே (5 F).",
        "ncert_key_point": "Charge in Faradays per mole = |Change in oxidation number per formula unit|.",
        "trap_breakdown": {
            "B": "3 F is for reduction of MnO4^- to MnO2 (+4) in neutral/faintly alkaline medium.",
            "C": "7 F confuses oxidation state +7 with change in oxidation state (+7 to +2 = 5).",
            "D": "2 F confuses final charge +2 with electrons transferred."
        },
        "videoTutorial": VIDEOS["chem_phys"]
    },
    {
        "id": 209,
        "subject": "Chemistry",
        "classLevel": "Class 12",
        "chapter": "Solutions",
        "ncertRef": "NCERT Class 12 Chemistry, Ch 1 — Colligative Properties & van 't Hoff Factor",
        "pyqTag": "NEET 2023 / 2024 Pattern",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Assuming 100% dissociation of strong electrolytes, which of the following 0.1 m aqueous solutions will have the HIGHEST boiling point?",
        "stem_ta": "வலிமையான மின்பகுளிகள் 100% பிரிகையடைகின்றன எனக் கொண்டால், பின்வரும் 0.1 m நீர்க்கரைசல்களில் எதற்குக் கொதிநிலை மிக அதிகமாக இருக்கும்?",
        "choices": [
            {"letter": "A", "text_en": "0.1 m Glucose", "text_ta": "0.1 m குளுக்கோஸ்"},
            {"letter": "B", "text_en": "0.1 m NaCl", "text_ta": "0.1 m NaCl"},
            {"letter": "C", "text_en": "0.1 m BaCl2", "text_ta": "0.1 m BaCl2"},
            {"letter": "D", "text_en": "0.1 m Al2(SO4)3", "text_ta": "0.1 m Al2(SO4)3"}
        ],
        "correct": "D",
        "explanation_en": "Boiling point elevation ΔT_b = i * K_b * m. At equal molality (0.1 m), larger van 't Hoff factor i gives higher ΔT_b and highest boiling point. Glucose: i = 1; NaCl: i = 2; BaCl2: i = 3; Al2(SO4)3 -> 2 Al^3+ + 3 SO4^2- gives i = 5 (highest!).",
        "explanation_ta": "கொதிநிலை ஏற்றம் ΔT_b = i * K_b * m. சம மோலாலிட்டியில் i மதிப்பு அதிகமாக உள்ள கரைசலின் கொதிநிலை அதிகமாக இருக்கும். Al2(SO4)3 -> 2 Al^3+ + 3 SO4^2- (i = 5), எனவே இதற்கே அதிக கொதிநிலை!",
        "ncert_key_point": "Highest i => Highest boiling point & osmotic pressure, BUT LOWEST freezing point & vapour pressure! Read carefully!",
        "trap_breakdown": {
            "A": "Glucose (i=1) has the HIGHEST freezing point / vapour pressure, but LOWEST boiling point.",
            "B": "NaCl has i = 2.",
            "C": "BaCl2 has i = 3."
        },
        "videoTutorial": VIDEOS["chem_phys"]
    },
    {
        "id": 210,
        "subject": "Chemistry",
        "classLevel": "Class 12",
        "chapter": "Chemical Kinetics",
        "ncertRef": "NCERT Class 12 Chemistry, Ch 3 — First-Order Integrated Rate Law",
        "pyqTag": "NEET High-Frequency PYQ",
        "questionType": "Numerical MCQ",
        "difficulty": "Easy",
        "stem_en": "A first-order reaction is 50% complete in 20 minutes. The time required for 87.5% completion of the same reaction is:",
        "stem_ta": "முதல் வகை வினை ஒன்று 50% நிறைவடைய 20 நிமிடங்கள் ஆகிறது. அதே வினை 87.5% நிறைவடைய ஆகும் நேரம் எவ்வளவு?",
        "choices": [
            {"letter": "A", "text_en": "40 minutes", "text_ta": "40 நிமிடங்கள்"},
            {"letter": "B", "text_en": "60 minutes", "text_ta": "60 நிமிடங்கள்"},
            {"letter": "C", "text_en": "80 minutes", "text_ta": "80 நிமிடங்கள்"},
            {"letter": "D", "text_en": "35 minutes", "text_ta": "35 நிமிடங்கள்"}
        ],
        "correct": "B",
        "explanation_en": "For a first-order reaction, half-life t_1/2 = 20 min is constant. 87.5% completion means 12.5% = (1/2)^3 of reactant remains! 100% -> 50% (20 min) -> 25% (40 min) -> 12.5% (60 min). Thus t_87.5% = 3 * t_1/2 = 60 minutes.",
        "explanation_ta": "முதல் வகை வினையின் அரைவாழ்வுக் காலம் t_1/2 = 20 நிமிடம். 87.5% நிறைவு என்றால் 12.5% மீதமுள்ளது: 100% -> 50% -> 25% -> 12.5% (3 அரைவாழ்வுக் காலங்கள்). எனவே நேரம் = 3 * 20 = 60 நிமிடங்கள்.",
        "ncert_key_point": "Memorize first-order ratios: t_75% = 2 t_1/2; t_87.5% = 3 t_1/2; t_99.9% ≈ 10 t_1/2.",
        "trap_breakdown": {
            "A": "40 minutes gives 75% completion (25% remaining).",
            "C": "80 minutes gives 93.75% completion (6.25% remaining).",
            "D": "35 minutes wrongly assumes zero-order linear proportionality (20 * 87.5 / 50)."
        },
        "videoTutorial": VIDEOS["chem_phys"]
    },
    {
        "id": 211,
        "subject": "Chemistry",
        "classLevel": "Class 12",
        "chapter": "The d- and f-Block Elements",
        "ncertRef": "NCERT Class 12 Chemistry, Ch 4 — Magnetic Properties of Transition Ions",
        "pyqTag": "NEET Official PYQ",
        "questionType": "Numerical MCQ",
        "difficulty": "Easy",
        "stem_en": "The spin-only magnetic moment of divalent Mn^2+ ion (atomic number Z = 25) in aqueous solution is:",
        "stem_ta": "நீர்க்கரைசலில் ஈரிணைதிறன் கொண்ட Mn^2+ அயனியின் (அணு எண் Z = 25) தற்சுழற்சி காந்தத் திருப்புத்திறன் (spin-only magnetic moment) மதிப்பு:",
        "choices": [
            {"letter": "A", "text_en": "4.90 BM", "text_ta": "4.90 BM"},
            {"letter": "B", "text_en": "5.92 BM", "text_ta": "5.92 BM"},
            {"letter": "C", "text_en": "3.87 BM", "text_ta": "3.87 BM"},
            {"letter": "D", "text_en": "2.84 BM", "text_ta": "2.84 BM"}
        ],
        "correct": "B",
        "explanation_en": "Ground state Mn (Z=25) is [Ar] 3d^5 4s^2. Losing two 4s electrons gives Mn^2+ = [Ar] 3d^5 with n = 5 unpaired electrons. Spin-only magnetic moment μ = sqrt(n(n+2)) = sqrt(5 * 7) = sqrt(35) ≈ 5.92 BM.",
        "explanation_ta": "Mn (Z=25): [Ar] 3d^5 4s^2 => Mn^2+: [Ar] 3d^5. தனித்த எலக்ட்ரான்கள் n = 5. காந்தத் திருப்புத்திறன் μ = sqrt(n(n+2)) = sqrt(35) ≈ 5.92 BM.",
        "ncert_key_point": "Integer shortcut: integer part of μ = sqrt(n(n+2)) ALWAYS equals n! (n=1 -> 1.73, n=2 -> 2.84, n=3 -> 3.87, n=4 -> 4.90, n=5 -> 5.92 BM).",
        "trap_breakdown": {
            "A": "4.90 BM corresponds to n = 4 (e.g., Fe^2+ or Cr^2+).",
            "C": "3.87 BM corresponds to n = 3 (e.g., Cr^3+ or Co^2+).",
            "D": "2.84 BM corresponds to n = 2 (e.g., Ni^2+)."
        },
        "videoTutorial": VIDEOS["chem_inorg"]
    },
    {
        "id": 212,
        "subject": "Chemistry",
        "classLevel": "Class 12",
        "chapter": "Coordination Compounds",
        "ncertRef": "NCERT Class 12 Chemistry, Ch 5 — Valence Bond Theory & Magnetic Behaviour",
        "pyqTag": "NEET 2023 / 2024 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "The hybridisation, geometry, and magnetic nature of the complex ion [Ni(CN)4]^2- (atomic number of Ni = 28) are respectively:",
        "stem_ta": "[Ni(CN)4]^2- என்ற அணைவு அயனியின் இனக்கலப்பு, வடிவியல் மற்றும் காந்தத் தன்மை முறையே (Ni அணு எண் = 28):",
        "choices": [
            {"letter": "A", "text_en": "sp^3, Tetrahedral, Paramagnetic", "text_ta": "sp^3, நான்முகி, பாராகாந்தத் தன்மை"},
            {"letter": "B", "text_en": "dsp^2, Square planar, Diamagnetic", "text_ta": "dsp^2, தள சதுரம், டயாகாந்தத் தன்மை"},
            {"letter": "C", "text_en": "sp^3, Tetrahedral, Diamagnetic", "text_ta": "sp^3, நான்முகி, டயாகாந்தத் தன்மை"},
            {"letter": "D", "text_en": "dsp^2, Square planar, Paramagnetic", "text_ta": "dsp^2, தள சதுரம், பாராகாந்தத் தன்மை"}
        ],
        "correct": "B",
        "explanation_en": "In [Ni(CN)4]^2-, Nickel is in +2 state (3d^8). Cyanide (CN^-) is a strong-field ligand, forcing the 8 d-electrons to pair up in four 3d orbitals, leaving one 3d orbital vacant for dsp^2 hybridisation -> Square planar geometry and Diamagnetic (0 unpaired electrons).",
        "explanation_ta": "[Ni(CN)4]^2- இல் Ni^2+ (3d^8) உள்ளது. CN^- வலிமையான ஈனி (strong-field ligand) என்பதால் எலக்ட்ரான்கள் இணையாகி dsp^2 இனக்கலப்பு, தள சதுர வடிவம் மற்றும் டயாகாந்தத் தன்மையைப் (0 தனித்த எலக்ட்ரான்) பெறுகிறது.",
        "ncert_key_point": "Contrast the classic NCERT trio: [NiCl4]^2- (sp^3, tetrahedral, paramagnetic, 2 e^-), [Ni(CN)4]^2- (dsp^2, square planar, diamagnetic), [Ni(CO)4] (Ni^0 3d^10, sp^3, tetrahedral, diamagnetic)!",
        "trap_breakdown": {
            "A": "sp^3, Tetrahedral, Paramagnetic is for [NiCl4]^2- (weak-field Cl^- ligand).",
            "C": "sp^3, Tetrahedral, Diamagnetic is for neutral [Ni(CO)4] where Ni is in 0 oxidation state!",
            "D": "dsp^2 Ni(II) cannot be paramagnetic because all 8 3d electrons are paired."
        },
        "videoTutorial": VIDEOS["chem_inorg"]
    },
    {
        "id": 213,
        "subject": "Chemistry",
        "classLevel": "Class 12",
        "chapter": "Alcohols, Phenols and Ethers",
        "ncertRef": "NCERT Class 12 Chemistry, Ch 7 — Acidity of Substituted Phenols",
        "pyqTag": "NEET Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "Arrange the following compounds in decreasing order of acidic strength: (I) Phenol, (II) p-Nitrophenol, (III) p-Cresol (4-methylphenol), (IV) 2,4,6-Trinitrophenol (Picric acid).",
        "stem_ta": "பின்வரும் சேர்மங்களை அவற்றின் அமில வலிமையின் இறங்கு வரிசையில் எழுதுக: (I) பீனால், (II) p-நைட்ரோபீனால், (III) p-கிரெசால் (4-மெத்தில்பீனால்), (IV) 2,4,6-டிரைநைட்ரோபீனால் (பிக்ரிக் அமிலம்).",
        "choices": [
            {"letter": "A", "text_en": "IV > II > I > III", "text_ta": "IV > II > I > III"},
            {"letter": "B", "text_en": "II > IV > I > III", "text_ta": "II > IV > I > III"},
            {"letter": "C", "text_en": "IV > II > III > I", "text_ta": "IV > II > III > I"},
            {"letter": "D", "text_en": "III > I > II > IV", "text_ta": "III > I > II > IV"}
        ],
        "correct": "A",
        "explanation_en": "Electron-withdrawing groups (-NO2 via -M and -I effects) disperse negative charge on the phenoxide ion and strongly INCREASE acidity; electron-donating groups (-CH3 via +I/hyperconjugation) DECREASE acidity. Thus: Picric acid (IV) > p-Nitrophenol (II) > Phenol (I) > p-Cresol (III).",
        "explanation_ta": "எலக்ட்ரான் கவரும் தொகுதிகள் (-NO2) பீனாக்சைடு அயனியை நிலைப்படுத்தி அமிலத் தன்மையை அதிகரிக்கும்; எலக்ட்ரான் தரும் தொகுதிகள் (-CH3) அமிலத் தன்மையைக் குறைக்கும். எனவே: IV > II > I > III.",
        "ncert_key_point": "EWG (-NO2, -CN, -X) increases acidity (lower pKa); EDG (-CH3, -OCH3) decreases acidity (higher pKa).",
        "trap_breakdown": {
            "B": "3 nitro groups stabilize phenoxide far more than 1 nitro group.",
            "C": "Places p-cresol above phenol despite destabilizing +I methyl group.",
            "D": "Gives decreasing pKa^-1 / increasing pKa order instead of acidic strength."
        },
        "videoTutorial": VIDEOS["chem_org"]
    },
    {
        "id": 214,
        "subject": "Chemistry",
        "classLevel": "Class 11",
        "chapter": "Hydrocarbons",
        "ncertRef": "NCERT Class 11 Chemistry, Ch 9 — Ozonolysis of Alkenes",
        "pyqTag": "NEET High-Frequency PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "Reductive ozonolysis ((i) O3, (ii) Zn/H2O) of an alkene 'X' gives an equimolar mixture of ethanal (CH3CHO) and propanone (CH3COCH3). The IUPAC name of alkene 'X' is:",
        "stem_ta": "ஆல்கீன் 'X' ஆனது ஒடுக்க ஓசோனேற்றம் ((i) O3, (ii) Zn/H2O) அடையும்போது எத்தனல் (CH3CHO) மற்றும் புரோப்பனோன் (CH3COCH3) ஆகியவற்றை சம மோலார் அளவில் தருகிறது. 'X'-இன் IUPAC பெயர் என்ன?",
        "choices": [
            {"letter": "A", "text_en": "2-Methylbut-2-ene", "text_ta": "2-மெத்தில்பியூட்-2-ஈன்"},
            {"letter": "B", "text_en": "2-Methylbut-1-ene", "text_ta": "2-மெத்தில்பியூட்-1-ஈன்"},
            {"letter": "C", "text_en": "Pent-2-ene", "text_ta": "பென்ட்-2-ஈன்"},
            {"letter": "D", "text_en": "2,3-Dimethylbut-2-ene", "text_ta": "2,3-டைமெத்தில்பியூட்-2-ஈன்"}
        ],
        "correct": "A",
        "explanation_en": "Shortcut: place the carbonyl oxygens face-to-face: (CH3)2C=O + O=CH-CH3, erase both O atoms, and join with a double bond => (CH3)2C=CH-CH3. Numbering the 4-carbon chain from the left gives double bond at C2 and methyl branch at C2: 2-Methylbut-2-ene.",
        "explanation_ta": "(CH3)2C=O மற்றும் O=CH-CH3 ஆகியவற்றின் ஆக்சிஜன்களை நீக்கி இரட்டைப் பிணைப்பால் இணைத்தால் (CH3)2C=CH-CH3 கிடைக்கும். இதன் IUPAC பெயர் 2-மெத்தில்பியூட்-2-ஈன்.",
        "ncert_key_point": "Reverse ozonolysis trick: point the two C=O groups at each other, delete O + O, and weld C=C.",
        "trap_breakdown": {
            "B": "2-Methylbut-1-ene gives methanal (HCHO) + butan-2-one.",
            "C": "Pent-2-ene gives ethanal + propanal (two aldehydes, no ketone).",
            "D": "2,3-Dimethylbut-2-ene gives 2 moles of propanone only."
        },
        "videoTutorial": VIDEOS["chem_org"]
    },
    {
        "id": 215,
        "subject": "Chemistry",
        "classLevel": "Class 12",
        "chapter": "Haloalkanes and Haloarenes",
        "ncertRef": "NCERT Class 12 Chemistry, Ch 6 — SN1 & SN2 Substitution Mechanisms",
        "pyqTag": "NEET Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Which of the following alkyl bromides undergoes nucleophilic substitution by the SN1 mechanism at the FASTEST rate?",
        "stem_ta": "பின்வரும் ஆல்கைல் புரோமைடுகளில் எது SN1 வினைவழிமுறையின் மூலம் மிக வேகமாக கருக்கவர் பதிலீட்டு வினைக்கு உட்படும்?",
        "choices": [
            {"letter": "A", "text_en": "CH3CH2Br", "text_ta": "CH3CH2Br"},
            {"letter": "B", "text_en": "(CH3)2CHBr", "text_ta": "(CH3)2CHBr"},
            {"letter": "C", "text_en": "(CH3)3CBr", "text_ta": "(CH3)3CBr"},
            {"letter": "D", "text_en": "CH3Br", "text_ta": "CH3Br"}
        ],
        "correct": "C",
        "explanation_en": "The rate-determining step of SN1 is unimolecular C-Br bond cleavage to form a carbocation intermediate. Tertiary carbocation (CH3)3C^+ is stabilized by 9 α-C-H hyperconjugative structures + +I effect, so 3° halide (CH3)3CBr reacts fastest via SN1!",
        "explanation_ta": "SN1 வினையின் வேகம் உருவாகும் கார்பன் நேர் அயனியின் (carbocation) நிலைப்புத்தன்மையைப் பொறுத்தது. மூவிணைய (3°) கார்பன் நேர் அயனி (CH3)3C^+ மிகவும் நிலைப்புத்தன்மை உடையதால் (CH3)3CBr மிக வேகமாக வினைபுரியும்!",
        "ncert_key_point": "Alkyl halide reactivity: SN1 => 3° > 2° > 1° > CH3X; SN2 => CH3X > 1° > 2° > 3°.",
        "trap_breakdown": {
            "A": "1° halide prefers SN2.",
            "B": "2° carbocation is less stable than 3°.",
            "D": "CH3Br reacts fastest via SN2, and slowest via SN1!"
        },
        "videoTutorial": VIDEOS["chem_org"]
    },
    {
        "id": 216,
        "subject": "Chemistry",
        "classLevel": "Class 12",
        "chapter": "Alcohols, Phenols and Ethers",
        "ncertRef": "NCERT Class 12 Chemistry, Ch 7 — Reimer-Tiemann Reaction",
        "pyqTag": "NEET 2022 / 2024 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "When phenol is treated with chloroform (CHCl3) and aqueous NaOH followed by acidification, the major product obtained is (Reimer-Tiemann reaction):",
        "stem_ta": "பீனாலை குளோரோஃபார்ம் (CHCl3) மற்றும் நீர்த்த NaOH உடன் வினைப்படுத்தி, பின் அமிலமாக்கும்போது கிடைக்கும் முதன்மை விளைபொருள் எது (ரைமர்-டீமன் வினை)?",
        "choices": [
            {"letter": "A", "text_en": "Salicylic acid (2-Hydroxybenzoic acid)", "text_ta": "சாலிசிலிக் அமிலம் (2-ஹைட்ராக்சிபென்சாயிக் அமிலம்)"},
            {"letter": "B", "text_en": "Salicylaldehyde (2-Hydroxybenzaldehyde)", "text_ta": "சாலிசிலால்டிஹைடு (2-ஹைட்ராக்சிபென்சால்டிஹைடு)"},
            {"letter": "C", "text_en": "Benzoquinone", "text_ta": "பென்சோகுயினோன்"},
            {"letter": "D", "text_en": "Benzaldehyde", "text_ta": "பென்சால்டிஹைடு"}
        ],
        "correct": "B",
        "explanation_en": "In the Reimer-Tiemann reaction, CHCl3 + NaOH generates the electrophile dichlorocarbene (:CCl2), which attacks the ortho position of phenoxide ion, hydrolyzes to -CHO, and upon acidification yields Salicylaldehyde (2-hydroxybenzaldehyde).",
        "explanation_ta": "ரைமர்-டீமன் வினையில் CHCl3 + NaOH வினைபுரிந்து டைகுளோரோகார்பீன் (:CCl2) எலக்ட்ரான் கவர் காரணியை உருவாக்கி, சாலிசிலால்டிஹைடை (2-ஹைட்ராக்சிபென்சால்டிஹைடு) முதன்மை விளைபொருளாகத் தருகிறது.",
        "ncert_key_point": "Phenol + CHCl3/NaOH => Salicylaldehyde (Reimer-Tiemann); Phenol + CO2/NaOH => Salicylic acid (Kolbe's reaction); Phenol + Zn dust => Benzene.",
        "trap_breakdown": {
            "A": "Salicylic acid is formed in Kolbe's reaction (CO2 + NaOH) or if CCl4 is used instead of CHCl3!",
            "C": "Benzoquinone is formed on oxidation of phenol with Na2Cr2O7 / H2SO4.",
            "D": "Phenol's -OH group remains intact; Zn dust is not used here."
        },
        "videoTutorial": VIDEOS["chem_org"]
    },
    {
        "id": 217,
        "subject": "Chemistry",
        "classLevel": "Class 12",
        "chapter": "Aldehydes, Ketones and Carboxylic Acids",
        "ncertRef": "NCERT Class 12 Chemistry, Ch 8 — Cannizzaro vs Aldol Reaction",
        "pyqTag": "NEET Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Which of the following aldehydes will undergo Cannizzaro disproportionation reaction on heating with concentrated NaOH?",
        "stem_ta": "பின்வரும் ஆல்டிஹைடுகளில் எது அடர் NaOH உடன் வெப்பப்படுத்தும்போது கன்னிசாரோ (Cannizzaro) விகிதச்சிதைவு வினைக்கு உட்படும்?",
        "choices": [
            {"letter": "A", "text_en": "Ethanal (CH3CHO)", "text_ta": "எத்தனல் (CH3CHO)"},
            {"letter": "B", "text_en": "Propanal (CH3CH2CHO)", "text_ta": "புரோப்பனல் (CH3CH2CHO)"},
            {"letter": "C", "text_en": "Benzaldehyde (C6H5CHO)", "text_ta": "பென்சால்டிஹைடு (C6H5CHO)"},
            {"letter": "D", "text_en": "Phenylacetaldehyde (C6H5CH2CHO)", "text_ta": "பினைல்அசிட்டால்டிஹைடு (C6H5CH2CHO)"}
        ],
        "correct": "C",
        "explanation_en": "Cannizzaro reaction is given ONLY by aldehydes that have NO α-hydrogen atom! In Benzaldehyde (C6H5-CHO), the carbon attached to -CHO is a ring sp^2 carbon bearing zero hydrogens, so it disproportionates into Benzyl alcohol + Sodium benzoate.",
        "explanation_ta": "ஆல்பா-ஹைட்ரஜன் (α-H) இல்லாத ஆல்டிஹைடுகள் மட்டுமே கன்னிசாரோ வினைக்கு உட்படும்! பென்சால்டிஹைடில் (C6H5CHO) α-ஹைட்ரஜன் இல்லை என்பதால் அது பென்சைல் ஆல்கஹால் மற்றும் சோடியம் பென்சோயேட்டைத் தருகிறது.",
        "ncert_key_point": "Has α-H => Aldol condensation (dilute alkali). Zero α-H (HCHO, C6H5CHO, (CH3)3CCHO) => Cannizzaro reaction (conc. alkali).",
        "trap_breakdown": {
            "A": "Ethanal has 3 α-hydrogens -> undergoes Aldol.",
            "B": "Propanal has 2 α-hydrogens -> undergoes Aldol.",
            "D": "Phenylacetaldehyde has 2 benzylic α-hydrogens (-CH2-) -> undergoes Aldol!"
        },
        "videoTutorial": VIDEOS["chem_org"]
    },
    {
        "id": 218,
        "subject": "Chemistry",
        "classLevel": "Class 12",
        "chapter": "Amines",
        "ncertRef": "NCERT Class 12 Chemistry, Ch 9 — Hoffmann Bromamide Degradation",
        "pyqTag": "NEET 2023 / 2024 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Which reagent converts Ethanamide (CH3CONH2) directly into Methanamine (CH3NH2) with one carbon atom less?",
        "stem_ta": "எத்தனமைடை (CH3CONH2) ஒரு கார்பன் அணு குறைவான மெத்தனமீனாக (CH3NH2) நேரடியாக மாற்றும் வினைக்காரணி எது?",
        "choices": [
            {"letter": "A", "text_en": "LiAlH4 followed by H2O", "text_ta": "LiAlH4 மற்றும் H2O"},
            {"letter": "B", "text_en": "Br2 and aqueous/ethanolic NaOH", "text_ta": "Br2 மற்றும் நீர்த்த/ஆல்கஹால் கலந்த NaOH"},
            {"letter": "C", "text_en": "P2O5 with heating", "text_ta": "P2O5 உடன் வெப்பப்படுத்துதல்"},
            {"letter": "D", "text_en": "NaNO2 + HCl", "text_ta": "NaNO2 + HCl"}
        ],
        "correct": "B",
        "explanation_en": "Hoffmann bromamide degradation: CH3CONH2 + Br2 + 4NaOH -> CH3NH2 + Na2CO3 + 2NaBr + 2H2O. The carbonyl carbon is lost as Na2CO3, producing a primary amine with ONE fewer carbon atom.",
        "explanation_ta": "ஹாஃப்மன் புரோமமைடு இறக்க வினை: CH3CONH2 + Br2 + 4NaOH -> CH3NH2 + Na2CO3 + 2NaBr + 2H2O. இது ஒரு கார்பன் குறைவான ஓரிணைய அமீனைத் தருகிறது.",
        "ncert_key_point": "Step-down amine (n-1 carbons): Br2/NaOH on amide. Same-carbon amine (n carbons): LiAlH4 reduction of amide.",
        "trap_breakdown": {
            "A": "LiAlH4 reduces -CONH2 to -CH2NH2, giving Ethanamine (CH3CH2NH2, 2 carbons), NOT Methanamine!",
            "C": "P2O5 dehydrates ethanamide to ethanenitrile (CH3CN).",
            "D": "HNO2 converts amide into ethanoic acid + N2."
        },
        "videoTutorial": VIDEOS["chem_org"]
    },
    {
        "id": 219,
        "subject": "Chemistry",
        "classLevel": "Class 12",
        "chapter": "Biomolecules",
        "ncertRef": "NCERT Class 12 Chemistry, Ch 10 — Disaccharides (Sucrose, Maltose, Lactose)",
        "pyqTag": "NEET Statement-Based PYQ",
        "questionType": "Statement I & II",
        "difficulty": "Medium",
        "stem_en": "Given below are two statements:\nStatement I: Sucrose is a non-reducing sugar because the glycosidic linkage is between C1 of α-D-glucose and C2 of β-D-fructose, locking both reducing groups.\nStatement II: Maltose and lactose are reducing sugars.\nChoose the correct option:",
        "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன:\nகூற்று I: சுக்ரோஸில் α-D-குளுக்கோஸின் C1 மற்றும் β-D-ஃபிரக்டோஸின் C2 இடையே கிளைக்கோசிடிக் பிணைப்பு உள்ளதால் இது ஒரு ஒடுக்கா சர்க்கரை (non-reducing sugar) ஆகும்.\nகூற்று II: மால்டோஸ் மற்றும் லாக்டோஸ் ஆகியவை ஒடுக்கும் சர்க்கரைகள் (reducing sugars) ஆகும்.\nசரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        "choices": [
            {"letter": "A", "text_en": "Both Statement I and Statement II are correct", "text_ta": "கூற்று I மற்றும் கூற்று II ஆகிய இரண்டும் சரி"},
            {"letter": "B", "text_en": "Both Statement I and Statement II are incorrect", "text_ta": "கூற்று I மற்றும் கூற்று II ஆகிய இரண்டும் தவறு"},
            {"letter": "C", "text_en": "Statement I is correct but Statement II is incorrect", "text_ta": "கூற்று I சரி, ஆனால் கூற்று II தவறு"},
            {"letter": "D", "text_en": "Statement I is incorrect but Statement II is correct", "text_ta": "கூற்று I தவறு, ஆனால் கூற்று II சரி"}
        ],
        "correct": "A",
        "explanation_en": "Exact NCERT Biomolecules facts: In sucrose, both anomeric carbons (C1 of α-D-glucose and C2 of β-D-fructose) participate in the glycosidic bond, so it cannot reduce Fehling's or Tollens' reagent. Maltose and lactose each retain one free hemiacetal C1 group and are reducing sugars.",
        "explanation_ta": "NCERT உயிரிமூலக்கூறுகள் பாடத்தின்படி: சுக்ரோஸில் இரு ஒடுக்கும் தொகுதிகளும் (C1 மற்றும் C2) பிணைப்பில் ஈடுபட்டுள்ளதால் அது ஒடுக்கா சர்க்கரை ஆகும். மால்டோஸ் மற்றும் லாக்டோஸ் ஒடுக்கும் சர்க்கரைகள் ஆகும். எனவே இரு கூற்றுகளும் சரி.",
        "ncert_key_point": "All monosaccharides + Maltose + Lactose = Reducing sugars. Sucrose = Non-reducing disaccharide!",
        "trap_breakdown": {
            "B": "Contradicts NCERT disaccharide classification.",
            "C": "Maltose and lactose DO reduce Tollens'/Fehling's solution.",
            "D": "C1(α-glucose)–C2(β-fructose) is the exact NCERT linkage of sucrose."
        },
        "videoTutorial": VIDEOS["chem_org"]
    },
    {
        "id": 220,
        "subject": "Chemistry",
        "classLevel": "Class 11",
        "chapter": "Organic Chemistry: Basic Principles & Practical Chemistry",
        "ncertRef": "NCERT Class 11 Chemistry, Ch 8 — Qualitative Analysis (Lassaigne's Test)",
        "pyqTag": "NEET 2023 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "In Lassaigne's test for the detection of nitrogen in an organic compound, the Prussian blue colour is due to the formation of:",
        "stem_ta": "கரிமச் சேர்மத்தில் நைட்ரஜனைக் கண்டறியும் லாசைன் சோதனையில் (Lassaigne's test) உருவாகும் புருஷியன் நீல நிறத்திற்குக் காரணமான சேர்மம் எது?",
        "choices": [
            {"letter": "A", "text_en": "Na4[Fe(CN)6]", "text_ta": "Na4[Fe(CN)6]"},
            {"letter": "B", "text_en": "Fe4[Fe(CN)6]3 · xH2O", "text_ta": "Fe4[Fe(CN)6]3 · xH2O"},
            {"letter": "C", "text_en": "[Fe(CN)5NOS]^4-", "text_ta": "[Fe(CN)5NOS]^4-"},
            {"letter": "D", "text_en": "[Fe(SCN)]^2+", "text_ta": "[Fe(SCN)]^2+"}
        ],
        "correct": "B",
        "explanation_en": "Sodium fusion extract contains NaCN, which reacts with Fe^2+ to form Na4[Fe(CN)6]. Upon boiling with conc. H2SO4/air, some Fe^2+ oxidizes to Fe^3+, reacting with [Fe(CN)6]^4- to form Iron(III) hexacyanoferrate(II), Fe4[Fe(CN)6]3 · xH2O (Prussian blue).",
        "explanation_ta": "சோடியம் சாறு FeSO4 உடன் வினைபுரிந்து Na4[Fe(CN)6] உருவாக்கி, பின் Fe^3+ அயனிகளுடன் இணைந்து Fe4[Fe(CN)6]3 · xH2O (ஃபெரிக் ஃபெரோசயனைடு — புருஷியன் நீல நிறம்) தருகிறது.",
        "ncert_key_point": "Lassaigne colours (NCERT must-memorize!): Fe4[Fe(CN)6]3 = Prussian Blue (N only); [Fe(SCN)]^2+ = Blood Red (both N & S present); [Fe(CN)5NOS]^4- = Violet (S with nitroprusside)!",
        "trap_breakdown": {
            "A": "Na4[Fe(CN)6] is the intermediate sodium hexacyanoferrate(II), not Prussian blue.",
            "C": "[Fe(CN)5NOS]^4- gives Violet colour in sodium nitroprusside test for Sulphur.",
            "D": "[Fe(SCN)]^2+ gives Blood Red colour when BOTH N and S are present together."
        },
        "videoTutorial": VIDEOS["chem_org"]
    },
]
