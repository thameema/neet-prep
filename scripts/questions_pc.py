#!/usr/bin/env python3
"""
20 Authentic NEET-UG Physics Questions (IDs 101-120) and
20 Authentic NEET-UG Chemistry Questions (IDs 201-220)
Strictly aligned to NMC-rationalized Class 11 & 12 NCERT and NEET 2019-2025 PYQs,
with full Bilingual (English + Tamil) stems, options, explanations, trap breakdowns,
and publication-grade KaTeX ($...$) mathematical & chemical typesetting.
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
        "stem_en": "In an experiment, the percentage errors in the measurement of physical quantities $A$, $B$, $C$, and $D$ are $1\\%$, $2\\%$, $3\\%$, and $4\\%$ respectively. Then the maximum percentage error in the measurement of $X$, where $X = \\frac{A^2 B^{1/2}}{C^{1/3} D^3}$, will be:",
        "stem_ta": "ஒரு சோதனையில் $A$, $B$, $C$ மற்றும் $D$ ஆகிய இயற்பியல் அளவுகளின் அளவீட்டில் ஏற்படும் சதவீதப் பிழைகள் முறையே $1\\%$, $2\\%$, $3\\%$ மற்றும் $4\\%$ ஆகும். $X = \\frac{A^2 B^{1/2}}{C^{1/3} D^3}$ எனில், $X$-இன் அளவீட்டில் ஏற்படும் பெரும சதவீதப் பிழை என்ன?",
        "choices": [
            {"letter": "A", "text_en": "$16\\%$", "text_ta": "$16\\%$"},
            {"letter": "B", "text_en": "$10\\%$", "text_ta": "$10\\%$"},
            {"letter": "C", "text_en": "$14\\%$", "text_ta": "$14\\%$"},
            {"letter": "D", "text_en": "$-10\\%$", "text_ta": "$-10\\%$"}
        ],
        "correct": "A",
        "explanation_en": "Relative errors ALWAYS ADD UP for both multiplication and division: $\\frac{\\Delta X}{X} \\times 100\\% = 2\\left(\\frac{\\Delta A}{A}\\%\\right) + \\frac{1}{2}\\left(\\frac{\\Delta B}{B}\\%\\right) + \\frac{1}{3}\\left(\\frac{\\Delta C}{C}\\%\\right) + 3\\left(\\frac{\\Delta D}{D}\\%\\right) = 2(1\\%) + \\frac{1}{2}(2\\%) + \\frac{1}{3}(3\\%) + 3(4\\%) = 2\\% + 1\\% + 1\\% + 12\\% = 16\\%$.",
        "explanation_ta": "பெருக்கல் மற்றும் வகுத்தல் ஆகிய இரண்டிற்குமே சார்புப் பிழைகளை எப்போதும் கூட்ட வேண்டும்: $\\frac{\\Delta X}{X} \\times 100\\% = 2(1\\%) + \\frac{1}{2}(2\\%) + \\frac{1}{3}(3\\%) + 3(4\\%) = 2\\% + 1\\% + 1\\% + 12\\% = 16\\%$.",
        "ncert_key_point": "Maximum percentage error adds all $|n_i| \\times (\\text{\\% error}_i)$ terms; never subtract denominator errors.",
        "trap_breakdown": {
            "B": "Obtained if you wrongly subtract denominator errors: $|(2 + 1) - (1 + 12)| = 10\\%$.",
            "C": "Arithmetic slip missing the exponent $2$ on $A^2$.",
            "D": "Maximum percentage errors are always positive magnitudes; $-10\\%$ is a classic sign trap."
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
        "stem_en": "A vehicle travels half the distance with speed $v$ and the remaining distance with speed $2v$. Its average speed is:",
        "stem_ta": "ஒரு வாகனம் மொத்தத் தொலைவில் பாதியை $v$ என்ற வேகத்திலும், மீதமுள்ள பாதித் தொலைவை $2v$ என்ற வேகத்திலும் கடக்கிறது. அதன் சராசரி வேகம் என்ன?",
        "choices": [
            {"letter": "A", "text_en": "$\\frac{3v}{2}$", "text_ta": "$\\frac{3v}{2}$"},
            {"letter": "B", "text_en": "$\\frac{4v}{3}$", "text_ta": "$\\frac{4v}{3}$"},
            {"letter": "C", "text_en": "$\\frac{2v}{3}$", "text_ta": "$\\frac{2v}{3}$"},
            {"letter": "D", "text_en": "$\\frac{3v}{4}$", "text_ta": "$\\frac{3v}{4}$"}
        ],
        "correct": "B",
        "explanation_en": "For two equal half-distances with speeds $v_1$ and $v_2$, average speed is the harmonic mean: $v_{\\text{avg}} = \\frac{2v_1 v_2}{v_1 + v_2} = \\frac{2v(2v)}{v + 2v} = \\frac{4v^2}{3v} = \\frac{4v}{3}$.",
        "explanation_ta": "சம தொலைவுகளை $v_1$ மற்றும் $v_2$ வேகங்களில் கடக்கும்போது சராசரி வேகம் $v_{\\text{avg}} = \\frac{2v_1 v_2}{v_1 + v_2} = \\frac{2v(2v)}{v + 2v} = \\frac{4v}{3}$.",
        "ncert_key_point": "Equal distances $\\Rightarrow$ Harmonic Mean $\\frac{2v_1 v_2}{v_1 + v_2}$. Equal time intervals $\\Rightarrow$ Arithmetic Mean $\\frac{v_1 + v_2}{2}$.",
        "trap_breakdown": {
            "A": "$\\frac{3v}{2} = \\frac{v + 2v}{2}$ is the average speed for equal TIME intervals, not equal distances.",
            "C": "Forgetting total distance is $2d$ instead of $d$.",
            "D": "Inverting $\\frac{\\text{total distance}}{\\text{total time}}$."
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
        "stem_en": "A bullet is fired from a gun at the speed of $280\\text{ m/s}$ in the direction $30^\\circ$ above the horizontal. The maximum height attained by the bullet is (take $g = 9.8\\text{ m/s}^2$, $\\sin 30^\\circ = 0.5$):",
        "stem_ta": "ஒரு துப்பாக்கியிலிருந்து தோட்டா ஒன்று கிடைமட்டத்திலிருந்து $30^\\circ$ கோணத்தில் $280\\text{ m/s}$ வேகத்தில் சுடப்படுகிறது. தோட்டா அடையும் பெரும உயரம் என்ன? ($g = 9.8\\text{ m/s}^2$, $\\sin 30^\\circ = 0.5$):",
        "choices": [
            {"letter": "A", "text_en": "$2000\\text{ m}$", "text_ta": "$2000\\text{ m}$"},
            {"letter": "B", "text_en": "$1000\\text{ m}$", "text_ta": "$1000\\text{ m}$"},
            {"letter": "C", "text_en": "$3000\\text{ m}$", "text_ta": "$3000\\text{ m}$"},
            {"letter": "D", "text_en": "$2800\\text{ m}$", "text_ta": "$2800\\text{ m}$"}
        ],
        "correct": "B",
        "explanation_en": "Maximum height $H = \\frac{u^2 \\sin^2\\theta}{2g}$. First compute vertical velocity $u_y = u \\sin 30^\\circ = 280 \\times 0.5 = 140\\text{ m/s}$. Then $H = \\frac{140^2}{2 \\times 9.8} = \\frac{19600}{19.6} = 1000\\text{ m}$.",
        "explanation_ta": "பெரும உயரம் $H = \\frac{u^2 \\sin^2\\theta}{2g}$. இங்கு செங்குத்து திசைவேகம் $u_y = 280 \\times 0.5 = 140\\text{ m/s}$. எனவே $H = \\frac{140 \\times 140}{19.6} = 1000\\text{ m}$.",
        "ncert_key_point": "Compute vertical component $u_y = u \\sin\\theta$ first, then $H = \\frac{u_y^2}{2g}$ for instant clean cancellation.",
        "trap_breakdown": {
            "A": "$2000\\text{ m}$ omits the factor of $2$ in $2g$.",
            "C": "$3000\\text{ m}$ uses $\\cos^2 30^\\circ = \\frac{3}{4}$ instead of $\\sin^2 30^\\circ = \\frac{1}{4}$.",
            "D": "$2800\\text{ m}$ confuses horizontal range formula with maximum height."
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
        "stem_en": "A ball of mass $0.15\\text{ kg}$ hits a vertical rigid wall horizontally at $12\\text{ m/s}$ and rebounds horizontally along the same line at $12\\text{ m/s}$. The magnitude of impulse imparted by the wall to the ball is:",
        "stem_ta": "$0.15\\text{ kg}$ நிறையுள்ள பந்து ஒன்று செங்குத்துச் சுவரின் மீது கிடைமட்டமாக $12\\text{ m/s}$ வேகத்தில் மோதி, அதே நேர்க்கோட்டில் $12\\text{ m/s}$ வேகத்தில் திரும்புகிறது. சுவர் பந்தின் மீது செலுத்திய கணத்தாக்கு விசையின் எண்மதிப்பு என்ன?",
        "choices": [
            {"letter": "A", "text_en": "$0\\text{ N}\\cdot\\text{s}$", "text_ta": "$0\\text{ N}\\cdot\\text{s}$"},
            {"letter": "B", "text_en": "$1.8\\text{ N}\\cdot\\text{s}$", "text_ta": "$1.8\\text{ N}\\cdot\\text{s}$"},
            {"letter": "C", "text_en": "$3.6\\text{ N}\\cdot\\text{s}$", "text_ta": "$3.6\\text{ N}\\cdot\\text{s}$"},
            {"letter": "D", "text_en": "$7.2\\text{ N}\\cdot\\text{s}$", "text_ta": "$7.2\\text{ N}\\cdot\\text{s}$"}
        ],
        "correct": "C",
        "explanation_en": "Momentum is a vector! Taking incident velocity $u = +12\\text{ m/s}$ and rebound velocity $v = -12\\text{ m/s}$, $|\\vec{J}| = |\\Delta \\vec{p}| = m|v - u| = 0.15 \\times |-12 - 12| = 0.15 \\times 24 = 3.6\\text{ N}\\cdot\\text{s}$.",
        "explanation_ta": "உந்தம் ஒரு வெக்டர் அளவாகும்! $u = +12\\text{ m/s}$, திரும்பும் திசைவேகம் $v = -12\\text{ m/s}$. கணத்தாக்கு $|\\vec{J}| = |\\Delta \\vec{p}| = m|v - u| = 0.15 \\times 24 = 3.6\\text{ N}\\cdot\\text{s}$.",
        "ncert_key_point": "For normal elastic rebound at speed $u$, the magnitude of momentum change is always $2mu$, never zero.",
        "trap_breakdown": {
            "A": "$0\\text{ N}\\cdot\\text{s}$ treats momentum as a scalar ($mv - mu = 0$), ignoring direction reversal.",
            "B": "$1.8\\text{ N}\\cdot\\text{s}$ computes $mu$ instead of $2mu$.",
            "D": "$7.2\\text{ N}\\cdot\\text{s}$ doubles $2mu$ a second time."
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
        "stem_en": "If the kinetic energy of a body increases by $300\\%$, the percentage increase in its linear momentum will be:",
        "stem_ta": "ஒரு பொருளின் இயக்க ஆற்றல் $300\\%$ அதிகரித்தால், அதன் நேர்க்கோட்டு உந்தத்தில் ஏற்படும் சதவீத அதிகரிப்பு என்ன?",
        "choices": [
            {"letter": "A", "text_en": "$100\\%$", "text_ta": "$100\\%$"},
            {"letter": "B", "text_en": "$150\\%$", "text_ta": "$150\\%$"},
            {"letter": "C", "text_en": "$200\\%$", "text_ta": "$200\\%$"},
            {"letter": "D", "text_en": "$300\\%$", "text_ta": "$300\\%$"}
        ],
        "correct": "A",
        "explanation_en": "Initial kinetic energy $= K$. 'Increases BY $300\\%$' means final $K' = K + 3K = 4K$. Since $p = \\sqrt{2mK}$, $\\frac{p'}{p} = \\sqrt{\\frac{K'}{K}} = \\sqrt{4} = 2$. Percentage increase $= \\frac{2p - p}{p} \\times 100\\% = 100\\%$.",
        "explanation_ta": "ஆரம்ப இயக்க ஆற்றல் $= K$. $300\\%$ அதிகரிப்பு என்றால் இறுதி $K' = K + 3K = 4K$. $p = \\sqrt{2mK}$ என்பதால் $\\frac{p'}{p} = \\sqrt{4} = 2$. எனவே சதவீத அதிகரிப்பு $= \\frac{2p - p}{p} \\times 100\\% = 100\\%$.",
        "ncert_key_point": "Never use calculus approximation $\\frac{\\Delta p}{p} = \\frac{1}{2}\\frac{\\Delta K}{K}$ when percentage change exceeds $5\\%$!",
        "trap_breakdown": {
            "B": "$150\\%$ wrongly applies the small-error formula $\\frac{1}{2}(300\\%)$.",
            "C": "$200\\%$ reports final momentum percentage ($200\\%$ of initial) without subtracting the initial $100\\%$.",
            "D": "$300\\%$ assumes $p$ is linearly proportional to $K$."
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
        "ncert_key_point": "Read carefully: Radius of Gyration $K = \\sqrt{\\frac{I}{M}}$, whereas Moment of Inertia ratio $I_1 : I_2$ is $2 : 1$.",
        "trap_breakdown": {
            "A": "$2 : 1$ is the ratio of Moments of Inertia $I_1 : I_2$, forgetting the square root for $K$.",
            "C": "Squaring instead of taking the square root.",
            "D": "Inverting the order of the two axes ($K_2 : K_1$)."
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
        "stem_en": "The escape velocity from the Earth's surface is $v$. The escape velocity from the surface of another planet having a radius four times that of Earth and the same mean mass density is:",
        "stem_ta": "பூமியின் மேற்பரப்பிலிருந்து விடுபடு திசைவேகம் $v$ ஆகும். பூமியின் அதே சராசரி அடர்த்தியும், பூமியின் ஆரத்தைப் போல $4$ மடங்கு ஆரமும் கொண்ட மற்றொரு கோளின் விடுபடு திசைவேகம் என்ன?",
        "choices": [
            {"letter": "A", "text_en": "$v$", "text_ta": "$v$"},
            {"letter": "B", "text_en": "$2v$", "text_ta": "$2v$"},
            {"letter": "C", "text_en": "$\\frac{v}{2}$", "text_ta": "$\\frac{v}{2}$"},
            {"letter": "D", "text_en": "$4v$", "text_ta": "$4v$"}
        ],
        "correct": "D",
        "explanation_en": "$v_e = \\sqrt{\\frac{2GM}{R}}$. Since mean density $\\rho$ is constant, substitute $M = \\frac{4}{3}\\pi R^3 \\rho$: $v_e = \\sqrt{\\frac{8}{3}\\pi G \\rho R^2} = R\\sqrt{\\frac{8}{3}\\pi G \\rho}$. Thus $v_e \\propto R$ at constant density. Since $R' = 4R$, $v_e' = 4v$.",
        "explanation_ta": "$v_e = \\sqrt{\\frac{2GM}{R}}$. அடர்த்தி $\\rho$ மாறிலி என்பதால் $M = \\frac{4}{3}\\pi R^3 \\rho$ எனப் பிரதியிட $v_e = R\\sqrt{\\frac{8}{3}\\pi G \\rho} \\propto R$. எனவே $R' = 4R$ எனில் $v_e' = 4v$.",
        "ncert_key_point": "Constant Mass $M \\Rightarrow v_e \\propto \\frac{1}{\\sqrt{R}}$. Constant Density $\\rho \\Rightarrow v_e \\propto R$.",
        "trap_breakdown": {
            "A": "Cancelling $R$ completely.",
            "B": "$2v$ assumes surface gravity $g$ is constant ($v_e = \\sqrt{2gR}$), whereas at constant density $\\rho$, $g' = 4g$!",
            "C": "$\\frac{v}{2}$ assumes planet mass $M$ is constant instead of density $\\rho$."
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
        "stem_en": "A Carnot engine has an efficiency of $50\\%$ when its source is at a temperature of $327^\\circ\\text{C}$. The temperature of the sink is:",
        "stem_ta": "கார்னோ (Carnot) வெப்ப இயந்திரம் ஒன்றின் வெப்ப மூலம் $327^\\circ\\text{C}$ வெப்பநிலையில் உள்ளபோது அதன் பயனுறுதிறன் $50\\%$ ஆகும். வெப்ப ஏற்பியின் (sink) வெப்பநிலை என்ன?",
        "choices": [
            {"letter": "A", "text_en": "$27^\\circ\\text{C}$", "text_ta": "$27^\\circ\\text{C}$"},
            {"letter": "B", "text_en": "$15^\\circ\\text{C}$", "text_ta": "$15^\\circ\\text{C}$"},
            {"letter": "C", "text_en": "$100^\\circ\\text{C}$", "text_ta": "$100^\\circ\\text{C}$"},
            {"letter": "D", "text_en": "$163.5^\\circ\\text{C}$", "text_ta": "$163.5^\\circ\\text{C}$"}
        ],
        "correct": "A",
        "explanation_en": "Convert source temperature to Kelvin: $T_1 = 327 + 273 = 600\\text{ K}$. Efficiency $\\eta = 1 - \\frac{T_2}{T_1} = 0.5 \\Rightarrow \\frac{T_2}{600} = 0.5 \\Rightarrow T_2 = 300\\text{ K}$. In Celsius: $t_2 = 300 - 273 = 27^\\circ\\text{C}$.",
        "explanation_ta": "வெப்பநிலையை முதலில் கெல்வினுக்கு மாற்றவும்: $T_1 = 327 + 273 = 600\\text{ K}$. $\\eta = 1 - \\frac{T_2}{T_1} = 0.5 \\Rightarrow T_2 = 300\\text{ K} = 300 - 273 = 27^\\circ\\text{C}$.",
        "ncert_key_point": "Always convert $^\\circ\\text{C}$ to Kelvin ($T\\text{ (K)} = t\\text{ }(^\\circ\\text{C}) + 273$) BEFORE using $\\eta = 1 - \\frac{T_{\\text{sink}}}{T_{\\text{source}}}$.",
        "trap_breakdown": {
            "B": "Subtraction slip when converting $300\\text{ K}$ to $^\\circ\\text{C}$.",
            "C": "Guessing round Celsius values.",
            "D": "$163.5^\\circ\\text{C}$ is half of $327^\\circ\\text{C}$ — the classic mistake of forgetting to convert to Kelvin!"
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
        "stem_en": "A particle executes linear simple harmonic motion with amplitude $A$. At what displacement from the mean position is its kinetic energy equal to its potential energy?",
        "stem_ta": "துகள் ஒன்று $A$ என்ற வீச்சுடன் நேர்க்கோட்டு தனிச்சீரான இயக்கத்தை (SHM) மேற்கொள்கிறது. மையப்புள்ளியிலிருந்து எந்த இடப்பெயர்ச்சியில் அதன் இயக்க ஆற்றலும் நிலை ஆற்றலும் சமமாக இருக்கும்?",
        "choices": [
            {"letter": "A", "text_en": "$\\frac{A}{2}$", "text_ta": "$\\frac{A}{2}$"},
            {"letter": "B", "text_en": "$\\frac{A}{\\sqrt{2}}$", "text_ta": "$\\frac{A}{\\sqrt{2}}$"},
            {"letter": "C", "text_en": "$\\frac{A}{\\sqrt{3}}$", "text_ta": "$\\frac{A}{\\sqrt{3}}$"},
            {"letter": "D", "text_en": "$\\frac{\\sqrt{3}A}{2}$", "text_ta": "$\\frac{\\sqrt{3}A}{2}$"}
        ],
        "correct": "B",
        "explanation_en": "$KE = \\frac{1}{2}m\\omega^2(A^2 - x^2)$ and $PE = \\frac{1}{2}m\\omega^2 x^2$. Equating $KE = PE$ gives $A^2 - x^2 = x^2 \\Rightarrow 2x^2 = A^2 \\Rightarrow x = \\frac{A}{\\sqrt{2}}$.",
        "explanation_ta": "$KE = \\frac{1}{2}m\\omega^2(A^2 - x^2)$ மற்றும் $PE = \\frac{1}{2}m\\omega^2 x^2$. இரண்டும் சமம் எனில் $A^2 - x^2 = x^2 \\Rightarrow x = \\frac{A}{\\sqrt{2}}$.",
        "ncert_key_point": "Since $PE \\propto x^2$, $PE$ equals $50\\%$ of total energy at $x = \\frac{A}{\\sqrt{2}} \\approx 0.707A$, not $\\frac{A}{2}$.",
        "trap_breakdown": {
            "A": "At $x = \\frac{A}{2}$, $PE$ is $25\\%$ and $KE$ is $75\\%$ of total energy.",
            "C": "At $x = \\frac{A}{\\sqrt{3}}$, $KE = 2 \\times PE$.",
            "D": "At $x = \\frac{\\sqrt{3}A}{2}$, $PE = 3 \\times KE$."
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
        "stem_en": "An air-filled parallel plate capacitor has capacitance $15\\text{ pF}$. When the separation between plates is doubled and the space is completely filled with a dielectric medium of dielectric constant $K = 4$, the new capacitance becomes:",
        "stem_ta": "காற்று நிரப்பப்பட்ட இணைத்தட்டு மின்தேக்கியின் மின்தேக்குத்திறன் $15\\text{ pF}$ ஆகும். தட்டுகளுக்கு இடையிலான தொலைவு இருமடங்காக்கப்பட்டு, $K = 4$ கொண்ட மின்காப்பு ஊடகத்தால் நிரப்பப்பட்டால் புதிய மின்தேக்குத்திறன் என்ன?",
        "choices": [
            {"letter": "A", "text_en": "$30\\text{ pF}$", "text_ta": "$30\\text{ pF}$"},
            {"letter": "B", "text_en": "$60\\text{ pF}$", "text_ta": "$60\\text{ pF}$"},
            {"letter": "C", "text_en": "$7.5\\text{ pF}$", "text_ta": "$7.5\\text{ pF}$"},
            {"letter": "D", "text_en": "$120\\text{ pF}$", "text_ta": "$120\\text{ pF}$"}
        ],
        "correct": "A",
        "explanation_en": "$C_0 = \\frac{\\varepsilon_0 A}{d} = 15\\text{ pF}$. With $d' = 2d$ and $K = 4$, $C' = \\frac{K \\varepsilon_0 A}{2d} = \\frac{4}{2} C_0 = 2 \\times 15\\text{ pF} = 30\\text{ pF}$.",
        "explanation_ta": "$C_0 = \\frac{\\varepsilon_0 A}{d} = 15\\text{ pF}$. $d' = 2d$ மற்றும் $K = 4$ எனில், $C' = \\frac{4}{2} \\times 15\\text{ pF} = 30\\text{ pF}$.",
        "ncert_key_point": "$C = \\frac{K \\varepsilon_0 A}{d}$: scale initial $C_0$ directly by $\\frac{K_{\\text{new}}}{K_{\\text{old}}} \\times \\frac{d_{\\text{old}}}{d_{\\text{new}}}$.",
        "trap_breakdown": {
            "B": "$60\\text{ pF}$ multiplies by $K = 4$ without dividing by $2$ for doubled plate separation.",
            "C": "$7.5\\text{ pF}$ divides by $K$ instead of multiplying.",
            "D": "$120\\text{ pF}$ multiplies by both $4$ and $2$."
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
        "stem_en": "A wire of resistance $10\\ \\Omega$ is uniformly stretched so that its length becomes $3$ times its original length (volume remaining constant). Its new resistance is:",
        "stem_ta": "$10\\ \\Omega$ மின்தடை கொண்ட கம்பி ஒன்று அதன் பருமன் மாறாமல் நீளம் மும்மடங்காகுமாறு சீராக இழுக்கப்படுகிறது. அதன் புதிய மின்தடை என்ன?",
        "choices": [
            {"letter": "A", "text_en": "$30\\ \\Omega$", "text_ta": "$30\\ \\Omega$"},
            {"letter": "B", "text_en": "$90\\ \\Omega$", "text_ta": "$90\\ \\Omega$"},
            {"letter": "C", "text_en": "$\\frac{10}{3}\\ \\Omega$", "text_ta": "$\\frac{10}{3}\\ \\Omega$"},
            {"letter": "D", "text_en": "$60\\ \\Omega$", "text_ta": "$60\\ \\Omega$"}
        ],
        "correct": "B",
        "explanation_en": "At constant volume $V = A L$, stretching $L' = 3L$ causes cross-sectional area to become $A' = \\frac{A}{3}$. Hence $R' = \\rho \\frac{L'}{A'} = 9\\left(\\rho \\frac{L}{A}\\right) = 3^2 \\times 10\\ \\Omega = 90\\ \\Omega$.",
        "explanation_ta": "பருமன் மாறாமல் கம்பியை $n$ மடங்கு நீட்டும்போது பரப்பு $A' = \\frac{A}{n}$ ஆகும். எனவே புதிய மின்தடை $R' = n^2 R = 3^2 \\times 10\\ \\Omega = 90\\ \\Omega$.",
        "ncert_key_point": "Stretched to $n$ times length $\\Rightarrow R' = n^2 R$. Stretched to $\\frac{1}{n}$ radius $\\Rightarrow R' = n^4 R$.",
        "trap_breakdown": {
            "A": "$30\\ \\Omega$ uses $R' = nR$, ignoring that cross-sectional area shrinks by factor $3$.",
            "C": "Dividing instead of multiplying.",
            "D": "Using $2n$ instead of $n^2$."
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
        "stem_en": "In a Wheatstone bridge, the upper branch has $4\\ \\Omega$ and $6\\ \\Omega$ resistors in series, the lower branch has $8\\ \\Omega$ and $12\\ \\Omega$ resistors in series, and a $10\\ \\Omega$ galvanometer connects their midpoints. If an ideal $20\\text{ V}$ battery is connected across the bridge ends, the total current drawn from the battery is:",
        "stem_ta": "வீட்ஸ்டோன் சமனச்சுற்றில் மேல் கிளையில் $4\\ \\Omega$, $6\\ \\Omega$ மின்தடைகள் தொடரிணைப்பிலும், கீழ் கிளையில் $8\\ \\Omega$, $12\\ \\Omega$ மின்தடைகள் தொடரிணைப்பிலும் உள்ளன. அவற்றின் நடுப்புள்ளிகளுக்கிடையே $10\\ \\Omega$ கால்வனாமீட்டரும், முனைகளில் $20\\text{ V}$ மின்கலமும் இணைக்கப்பட்டால் மின்கலத்திலிருந்து பாயும் மொத்த மின்னோட்டம்:",
        "choices": [
            {"letter": "A", "text_en": "$3.0\\text{ A}$", "text_ta": "$3.0\\text{ A}$"},
            {"letter": "B", "text_en": "$2.0\\text{ A}$", "text_ta": "$2.0\\text{ A}$"},
            {"letter": "C", "text_en": "$1.5\\text{ A}$", "text_ta": "$1.5\\text{ A}$"},
            {"letter": "D", "text_en": "$4.0\\text{ A}$", "text_ta": "$4.0\\text{ A}$"}
        ],
        "correct": "A",
        "explanation_en": "Ratio check: $\\frac{4}{6} = \\frac{2}{3}$ and $\\frac{8}{12} = \\frac{2}{3}$. Because the bridge is balanced, zero current flows through the $10\\ \\Omega$ galvanometer (remove it!). Upper series branch $= 4 + 6 = 10\\ \\Omega$; lower series branch $= 8 + 12 = 20\\ \\Omega$ in parallel. $R_{\\text{eq}} = \\frac{10 \\times 20}{10 + 20} = \\frac{20}{3}\\ \\Omega$. Total current $I = \\frac{V}{R_{\\text{eq}}} = \\frac{20}{20/3} = 3.0\\text{ A}$.",
        "explanation_ta": "$\\frac{4}{6} = \\frac{8}{12} = \\frac{2}{3}$ என்பதால் சமனச்சுற்று சமநிலையில் உள்ளது; $10\\ \\Omega$ வழியே மின்னோட்டம் பாயாது. மேல் கிளை $= 10\\ \\Omega$, கீழ் கிளை $= 20\\ \\Omega$ பக்க இணைப்பில் உள்ளன. $R_{\\text{eq}} = \\frac{20}{3}\\ \\Omega$. எனவே $I = \\frac{20}{20/3} = 3.0\\text{ A}$.",
        "ncert_key_point": "Always check $\\frac{P}{Q} = \\frac{R}{S}$ first before attempting Kirchhoff's loop equations!",
        "trap_breakdown": {
            "B": "$2.0\\text{ A}$ considers only the $10\\ \\Omega$ upper branch.",
            "C": "$1.5\\text{ A}$ miscalculates the parallel combination.",
            "D": "$4.0\\text{ A}$ includes the central $10\\ \\Omega$ resistor in parallel."
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
        "stem_en": "A proton and an alpha particle enter a uniform magnetic field perpendicular to their velocities with the same kinetic energy. The ratio of the radii of their circular paths ($r_p : r_\\alpha$) is:",
        "stem_ta": "புரோட்டான் ஒன்றும் ஆல்பா துகள் ஒன்றும் சம இயக்க ஆற்றலுடன் சீரான காந்தப்புலத்திற்குச் செங்குத்தாக நுழைகின்றன. அவற்றின் வட்டப் பாதைகளின் ஆரங்களின் விகிதம் ($r_p : r_\\alpha$):",
        "choices": [
            {"letter": "A", "text_en": "$1 : 1$", "text_ta": "$1 : 1$"},
            {"letter": "B", "text_en": "$1 : 2$", "text_ta": "$1 : 2$"},
            {"letter": "C", "text_en": "$2 : 1$", "text_ta": "$2 : 1$"},
            {"letter": "D", "text_en": "$1 : 4$", "text_ta": "$1 : 4$"}
        ],
        "correct": "A",
        "explanation_en": "Radius in a magnetic field in terms of kinetic energy $K$ is $r = \\frac{\\sqrt{2mK}}{qB}$. For an alpha particle ($^4_2\\text{He}^{2+}$), $m_\\alpha = 4m_p$ and $q_\\alpha = 2q_p$. At equal $K$ and $B$, $\\frac{r_p}{r_\\alpha} = \\frac{\\sqrt{m_p}/q_p}{\\sqrt{4m_p}/(2q_p)} = \\frac{1}{2/2} = 1 : 1$.",
        "explanation_ta": "காந்தப்புலத்தில் ஆரம் $r = \\frac{\\sqrt{2mK}}{qB}$. ஆல்பா துகளுக்கு $m_\\alpha = 4m_p$ மற்றும் $q_\\alpha = 2q_p$. $K$, $B$ சமம் எனில் $r_\\alpha = \\frac{\\sqrt{4}}{2} r_p = r_p$. எனவே விகிதம் $r_p : r_\\alpha = 1 : 1$.",
        "ncert_key_point": "Same KE $\\Rightarrow r \\propto \\frac{\\sqrt{m}}{q} \\Rightarrow r_p : r_d : r_\\alpha = 1 : \\sqrt{2} : 1$. Same velocity $\\Rightarrow r \\propto \\frac{m}{q} \\Rightarrow 1 : 2 : 2$. Same potential $V \\Rightarrow r \\propto \\sqrt{\\frac{m}{q}} \\Rightarrow 1 : \\sqrt{2} : \\sqrt{2}$.",
        "trap_breakdown": {
            "B": "$1 : 2$ is the ratio when they enter with the SAME VELOCITY ($r \\propto \\frac{m}{q}$), not same kinetic energy!",
            "C": "$2 : 1$ forgets that the alpha particle carries twice the proton charge ($q_\\alpha = 2q_p$), or inverts the equal-velocity ratio.",
            "D": "$1 : 4$ forgets both the square root on mass and the factor $2$ on charge."
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
        "stem_en": "A series LCR circuit has inductance $L = 10\\text{ mH}$, capacitance $C = 1\\ \\mu\\text{F}$, and resistance $R = 50\\ \\Omega$. The angular frequency ($\\omega_0$) at which resonance occurs is:",
        "stem_ta": "தொடர் LCR சுற்றில் மின்தூண்டல் $L = 10\\text{ mH}$, மின்தேக்குத்திறன் $C = 1\\ \\mu\\text{F}$ மற்றும் மின்தடை $R = 50\\ \\Omega$ உள்ளது. ஒத்ததிர்வு நிகழும் கோண அதிர்வெண் ($\\omega_0$) என்ன?",
        "choices": [
            {"letter": "A", "text_en": "$10^4\\text{ rad/s}$", "text_ta": "$10^4\\text{ rad/s}$"},
            {"letter": "B", "text_en": "$10^5\\text{ rad/s}$", "text_ta": "$10^5\\text{ rad/s}$"},
            {"letter": "C", "text_en": "$10^3\\text{ rad/s}$", "text_ta": "$10^3\\text{ rad/s}$"},
            {"letter": "D", "text_en": "$2 \\times 10^4\\text{ rad/s}$", "text_ta": "$2 \\times 10^4\\text{ rad/s}$"}
        ],
        "correct": "A",
        "explanation_en": "Resonant angular frequency $\\omega_0 = \\frac{1}{\\sqrt{LC}}$ is independent of $R$! Here $L = 10 \\times 10^{-3}\\text{ H} = 10^{-2}\\text{ H}$ and $C = 10^{-6}\\text{ F}$, so $LC = 10^{-8}\\text{ s}^2$. Thus $\\omega_0 = \\frac{1}{\\sqrt{10^{-8}}} = 10^4\\text{ rad/s}$.",
        "explanation_ta": "ஒத்ததிர்வு கோண அதிர்வெண் $\\omega_0 = \\frac{1}{\\sqrt{LC}}$ ($R$-ஐச் சார்ந்ததல்ல). $L = 10^{-2}\\text{ H}$, $C = 10^{-6}\\text{ F} \\Rightarrow LC = 10^{-8}\\text{ s}^2 \\Rightarrow \\omega_0 = 10^4\\text{ rad/s}$.",
        "ncert_key_point": "Watch units: $10\\text{ mH} = 10^{-2}\\text{ H}$ (not $10^{-3}\\text{ H}$!), and distinguish $\\omega_0\\text{ (rad/s)}$ from $f_0 = \\frac{\\omega_0}{2\\pi}\\text{ (Hz)}$.",
        "trap_breakdown": {
            "B": "$10^5\\text{ rad/s}$ misreads $10\\text{ mH}$ as $10^{-4}\\text{ H}$.",
            "C": "$10^3\\text{ rad/s}$ misreads $1\\ \\mu\\text{F}$ as $10^{-4}\\text{ F}$.",
            "D": "Unnecessary factor introduced from $R = 50\\ \\Omega$."
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
        "stem_en": "A biconvex lens made of glass (refractive index $n_g = 1.5$) has focal length $20\\text{ cm}$ in air. When completely immersed in a transparent liquid of refractive index $n_l = 1.25$, its focal length becomes:",
        "stem_ta": "கண்ணாடியால் (ஒளிவிலகல் எண் $n_g = 1.5$) செய்யப்பட்ட இருகுவி லென்ஸின் காற்றில் குவியத்தூரம் $20\\text{ cm}$ ஆகும். $n_l = 1.25$ ஒளிவிலகல் எண் கொண்ட திரவத்தில் முழுமையாக மூழ்கடிக்கப்படும்போது அதன் புதிய குவியத்தூரம்:",
        "choices": [
            {"letter": "A", "text_en": "$+50\\text{ cm}$", "text_ta": "$+50\\text{ cm}$"},
            {"letter": "B", "text_en": "$+25\\text{ cm}$", "text_ta": "$+25\\text{ cm}$"},
            {"letter": "C", "text_en": "$-50\\text{ cm}$", "text_ta": "$-50\\text{ cm}$"},
            {"letter": "D", "text_en": "$+40\\text{ cm}$", "text_ta": "$+40\\text{ cm}$"}
        ],
        "correct": "A",
        "explanation_en": "By Lens Maker's formula: $\\frac{f_{\\text{liq}}}{f_{\\text{air}}} = \\frac{n_g - 1}{(n_g / n_l) - 1}$. Here $n_g - 1 = 0.5$, and $\\frac{1.5}{1.25} - 1 = 1.2 - 1 = 0.2$. So $\\frac{f_{\\text{liq}}}{20} = \\frac{0.5}{0.2} = 2.5 \\Rightarrow f_{\\text{liq}} = +50\\text{ cm}$.",
        "explanation_ta": "லென்ஸ் உருவாக்குபவர் சமன்பாட்டின்படி: $\\frac{f_{\\text{liq}}}{f_{\\text{air}}} = \\frac{n_g - 1}{(n_g / n_l) - 1} = \\frac{1.5 - 1}{(1.5 / 1.25) - 1} = \\frac{0.5}{0.2} = 2.5$. எனவே திரவத்தில் குவியத்தூரம் $f_{\\text{liq}} = 2.5 \\times 20\\text{ cm} = +50\\text{ cm}$.",
        "ncert_key_point": "When $n_{\\text{liq}} < n_g$, a convex lens stays converging ($+f$) with a LARGER focal length; if $n_{\\text{liq}} > n_g$, it turns diverging ($-f$)!",
        "trap_breakdown": {
            "B": "$+25\\text{ cm}$ uses $n_g - n_l = 0.25$ instead of $\\frac{n_g}{n_l} - 1 = 0.20$!",
            "C": "$-50\\text{ cm}$ wrongly flips sign (sign flips only if $n_l > 1.5$).",
            "D": "$+40\\text{ cm}$ doubles focal length by guessing."
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
        "stem_en": "In Young's double-slit experiment, the slit separation is $1.0\\text{ mm}$ and the screen is placed $1.5\\text{ m}$ away. When monochromatic light of wavelength $600\\text{ nm}$ is used, the fringe width is:",
        "stem_ta": "யங் இரட்டைப் பிளவு சோதனையில் பிளவுகளுக்கு இடையிலான தொலைவு $1.0\\text{ mm}$ மற்றும் திரை $1.5\\text{ m}$ தொலைவில் உள்ளது. $600\\text{ nm}$ அலைநீளம் கொண்ட ஒற்றைநிற ஒளி பயன்படுத்தப்படும்போது பட்டை அகலம் (fringe width) என்ன?",
        "choices": [
            {"letter": "A", "text_en": "$0.9\\text{ mm}$", "text_ta": "$0.9\\text{ mm}$"},
            {"letter": "B", "text_en": "$0.6\\text{ mm}$", "text_ta": "$0.6\\text{ mm}$"},
            {"letter": "C", "text_en": "$1.2\\text{ mm}$", "text_ta": "$1.2\\text{ mm}$"},
            {"letter": "D", "text_en": "$0.4\\text{ mm}$", "text_ta": "$0.4\\text{ mm}$"}
        ],
        "correct": "A",
        "explanation_en": "Fringe width $\\beta = \\frac{\\lambda D}{d} = \\frac{600 \\times 10^{-9}\\text{ m} \\times 1.5\\text{ m}}{1.0 \\times 10^{-3}\\text{ m}} = 900 \\times 10^{-6}\\text{ m} = 0.9 \\times 10^{-3}\\text{ m} = 0.9\\text{ mm}$.",
        "explanation_ta": "பட்டை அகலம் $\\beta = \\frac{\\lambda D}{d} = \\frac{600 \\times 10^{-9} \\times 1.5}{1.0 \\times 10^{-3}} = 0.9 \\times 10^{-3}\\text{ m} = 0.9\\text{ mm}$.",
        "ncert_key_point": "$\\beta = \\frac{\\lambda D}{d}$: convert $\\text{nm}$ ($10^{-9}\\text{ m}$) and $\\text{mm}$ ($10^{-3}\\text{ m}$) cleanly before multiplying.",
        "trap_breakdown": {
            "B": "$0.6\\text{ mm}$ forgets to multiply by $D = 1.5\\text{ m}$.",
            "C": "$1.2\\text{ mm}$ multiplies by $2$ instead of $1.5$.",
            "D": "$0.4\\text{ mm}$ divides by $1.5$ instead of multiplying."
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
        "stem_en": "The work function of Caesium is $2.14\\text{ eV}$. If incident light has photon energy $3.54\\text{ eV}$, the stopping potential ($V_0$) of the emitted photoelectrons is:",
        "stem_ta": "சீசியத்தின் வெளியேற்று ஆற்றல் (work function) $2.14\\text{ eV}$ ஆகும். படும் ஒளியின் ஃபோட்டான் ஆற்றல் $3.54\\text{ eV}$ எனில், உமிழப்படும் ஒளி எலக்ட்ரான்களின் நிறுத்து மின்னழுத்தம் (stopping potential $V_0$) என்ன?",
        "choices": [
            {"letter": "A", "text_en": "$1.40\\text{ V}$", "text_ta": "$1.40\\text{ V}$"},
            {"letter": "B", "text_en": "$5.68\\text{ V}$", "text_ta": "$5.68\\text{ V}$"},
            {"letter": "C", "text_en": "$2.14\\text{ V}$", "text_ta": "$2.14\\text{ V}$"},
            {"letter": "D", "text_en": "$0.70\\text{ V}$", "text_ta": "$0.70\\text{ V}$"}
        ],
        "correct": "A",
        "explanation_en": "By Einstein's photoelectric equation: $K_{\\max} = eV_0 = h\\nu - \\phi_0 = 3.54\\text{ eV} - 2.14\\text{ eV} = 1.40\\text{ eV}$. Dividing by elementary charge $e$ gives $V_0 = 1.40\\text{ V}$.",
        "explanation_ta": "ஐன்ஸ்டீனின் ஒளிமின் சமன்பாட்டின்படி: $eV_0 = h\\nu - \\phi_0 = 3.54\\text{ eV} - 2.14\\text{ eV} = 1.40\\text{ eV}$. எனவே நிறுத்து மின்னழுத்தம் $V_0 = 1.40\\text{ V}$.",
        "ncert_key_point": "When $K_{\\max}$ is in electron-volts ($\\text{eV}$), stopping potential $V_0$ in Volts ($\\text{V}$) has the exact same numerical value!",
        "trap_breakdown": {
            "B": "$5.68\\text{ V}$ adds $h\\nu$ and $\\phi_0$ instead of subtracting.",
            "C": "$2.14\\text{ V}$ confuses work function $\\phi_0$ with stopping potential $V_0$.",
            "D": "$0.70\\text{ V}$ divides $K_{\\max}$ by $2$."
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
        "stem_en": "The ground state energy of a hydrogen atom is $-13.6\\text{ eV}$. The energy required to excite the electron from the ground state ($n = 1$) to the first excited state ($n = 2$) is:",
        "stem_ta": "ஹைட்ரஜன் அணுவின் அடிநிலை ஆற்றல் $-13.6\\text{ eV}$ ஆகும். எலக்ட்ரானை அடிநிலையிலிருந்து ($n = 1$) முதல் கிளர்வு நிலைக்கு ($n = 2$) கிளர்வுறச் செய்யத் தேவைப்படும் ஆற்றல்:",
        "choices": [
            {"letter": "A", "text_en": "$3.4\\text{ eV}$", "text_ta": "$3.4\\text{ eV}$"},
            {"letter": "B", "text_en": "$10.2\\text{ eV}$", "text_ta": "$10.2\\text{ eV}$"},
            {"letter": "C", "text_en": "$12.09\\text{ eV}$", "text_ta": "$12.09\\text{ eV}$"},
            {"letter": "D", "text_en": "$13.6\\text{ eV}$", "text_ta": "$13.6\\text{ eV}$"}
        ],
        "correct": "B",
        "explanation_en": "First excited state corresponds to $n = 2$ (NOT $n = 1$!). $E_2 = -\\frac{13.6}{2^2} = -3.4\\text{ eV}$. Excitation energy $\\Delta E = E_2 - E_1 = -3.4 - (-13.6) = +10.2\\text{ eV}$.",
        "explanation_ta": "முதல் கிளர்வு நிலை என்பது $n = 2$ ஆகும்! $E_2 = -\\frac{13.6}{2^2} = -3.4\\text{ eV}$. தேவைப்படும் ஆற்றல் $\\Delta E = E_2 - E_1 = -3.4 - (-13.6) = 10.2\\text{ eV}$.",
        "ncert_key_point": "First excited state $= n=2$ ($+10.2\\text{ eV}$); Second excited state $= n=3$ ($+12.09\\text{ eV}$); Ionization $= n=\\infty$ ($+13.6\\text{ eV}$).",
        "trap_breakdown": {
            "A": "$3.4\\text{ eV}$ is $|E_2|$ (binding energy of $n = 2$), not $E_2 - E_1$!",
            "C": "$12.09\\text{ eV}$ is excitation to the SECOND excited state ($n = 3$).",
            "D": "$13.6\\text{ eV}$ is the ionization energy from the ground state."
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
        "stem_en": "Two nuclei have mass numbers in the ratio $27 : 125$. What is the ratio of their nuclear radii?",
        "stem_ta": "இரண்டு அணுக்கருக்களின் நிறை எண்களின் விகிதம் $27 : 125$ எனில், அவற்றின் அணுக்கரு ஆரங்களின் விகிதம் என்ன?",
        "choices": [
            {"letter": "A", "text_en": "$3 : 5$", "text_ta": "$3 : 5$"},
            {"letter": "B", "text_en": "$9 : 25$", "text_ta": "$9 : 25$"},
            {"letter": "C", "text_en": "$27 : 125$", "text_ta": "$27 : 125$"},
            {"letter": "D", "text_en": "$1 : 1$", "text_ta": "$1 : 1$"}
        ],
        "correct": "A",
        "explanation_en": "Nuclear radius $R = R_0 A^{1/3}$. Hence $\\frac{R_1}{R_2} = \\left(\\frac{A_1}{A_2}\\right)^{1/3} = \\left(\\frac{27}{125}\\right)^{1/3} = \\frac{3}{5} = 3 : 5$.",
        "explanation_ta": "அணுக்கரு ஆரம் $R = R_0 A^{1/3}$. எனவே $\\frac{R_1}{R_2} = \\left(\\frac{27}{125}\\right)^{1/3} = 3 : 5$. (அணுக்கரு அடர்த்தி $1 : 1$ மாறிலியாக இருக்கும்!)",
        "ncert_key_point": "Nuclear radius $R \\propto A^{1/3}$, surface area $\\propto A^{2/3}$, volume $\\propto A$, and nuclear density is CONSTANT ($1 : 1$) independent of $A$!",
        "trap_breakdown": {
            "B": "$9 : 25$ is the ratio of nuclear surface areas ($A^{2/3}$).",
            "C": "$27 : 125$ is the ratio of nuclear volumes ($A$).",
            "D": "$1 : 1$ is the ratio of nuclear DENSITIES, not radii!"
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
        "explanation_en": "Output of a NOR gate is $Y_1 = \\overline{A + B}$. Passing $Y_1$ through a NOT gate inverts it again: $Y = \\overline{Y_1} = \\overline{\\overline{A + B}} = A + B$, which is the Boolean expression of an OR gate!",
        "explanation_ta": "NOR வாயிலின் வெளியீடு $Y_1 = \\overline{A + B}$. இதை NOT வாயில் வழியே செலுத்தினால் $Y = \\overline{\\overline{A + B}} = A + B$, இது OR வாயிலுக்குச் சமம்!",
        "ncert_key_point": "Always verify logic gate MCQs in 10 seconds by plugging the 4 truth-table rows ($00, 01, 10, 11$).",
        "trap_breakdown": {
            "B": "AND gate ($A \\cdot B$) comes from a NAND gate ($\\overline{A \\cdot B}$) followed by a NOT gate.",
            "C": "NAND gate has Boolean expression $Y = \\overline{A \\cdot B}$.",
            "D": "Forgetting the final NOT inversion leaves $Y_1 = \\overline{A + B}$."
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
        "stem_en": "What mass of $95\\%$ pure $\\text{CaCO}_3$ will be required to neutralize $50\\text{ mL}$ of $0.5\\text{ M}\\ \\text{HCl}$ solution according to the reaction: $\\text{CaCO}_3(s) + 2\\text{HCl}(aq) \\to \\text{CaCl}_2(aq) + \\text{CO}_2(g) + \\text{H}_2\\text{O}(l)$? [Molar mass of $\\text{CaCO}_3 = 100\\text{ g/mol}$]",
        "stem_ta": "$\\text{CaCO}_3(s) + 2\\text{HCl}(aq) \\to \\text{CaCl}_2(aq) + \\text{CO}_2(g) + \\text{H}_2\\text{O}(l)$ என்ற வினையின்படி, $50\\text{ mL}$ அளவுள்ள $0.5\\text{ M}\\ \\text{HCl}$ கரைசலை நடுநிலையாக்க $95\\%$ தூய்மையான $\\text{CaCO}_3$ எவ்வளவு நிறை தேவைப்படும்? [$\\text{CaCO}_3$ மோலார் நிறை $= 100\\text{ g/mol}$]",
        "choices": [
            {"letter": "A", "text_en": "$1.25\\text{ g}$", "text_ta": "$1.25\\text{ g}$"},
            {"letter": "B", "text_en": "$1.32\\text{ g}$", "text_ta": "$1.32\\text{ g}$"},
            {"letter": "C", "text_en": "$3.65\\text{ g}$", "text_ta": "$3.65\\text{ g}$"},
            {"letter": "D", "text_en": "$9.50\\text{ g}$", "text_ta": "$9.50\\text{ g}$"}
        ],
        "correct": "B",
        "explanation_en": "Moles of $\\text{HCl} = M \\times V(\\text{L}) = 0.5 \\times 0.050 = 0.025\\text{ mol}$. From stoichiometry, $1\\text{ mol}\\ \\text{CaCO}_3$ reacts with $2\\text{ mol}\\ \\text{HCl}$, so pure $\\text{CaCO}_3$ needed $= \\frac{0.025}{2} = 0.0125\\text{ mol} = 0.0125 \\times 100\\text{ g} = 1.25\\text{ g}$. Since the sample is $95\\%$ pure, required sample mass $= \\frac{1.25}{0.95} = 1.3158\\text{ g} \\approx 1.32\\text{ g}$.",
        "explanation_ta": "$\\text{HCl}$ மோல்கள் $= 0.5 \\times 0.050 = 0.025\\text{ mol}$. தூய $\\text{CaCO}_3$ மோல்கள் $= \\frac{0.025}{2} = 0.0125\\text{ mol} = 1.25\\text{ g}$. மாதிரி $95\\%$ தூய்மையானது என்பதால் தேவையான நிறை $= \\frac{1.25}{0.95} = 1.316\\text{ g} \\approx 1.32\\text{ g}$.",
        "ncert_key_point": "Impure sample mass is ALWAYS greater than pure reactant mass: $m_{\\text{sample}} = \\frac{m_{\\text{pure}}}{\\text{\\% purity} / 100}$.",
        "trap_breakdown": {
            "A": "$1.25\\text{ g}$ stops at pure $\\text{CaCO}_3$ mass and forgets to divide by $0.95$ for $95\\%$ purity!",
            "C": "Confuses molar mass of $\\text{HCl}$ ($36.5\\text{ g/mol}$) with $\\text{CaCO}_3$ ($100\\text{ g/mol}$).",
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
        "stem_en": "What is the maximum number of orbitals that can be identified with the following quantum numbers: $n = 3$, $l = 1$, $m_l = 0$?",
        "stem_ta": "$n = 3$, $l = 1$, $m_l = 0$ ஆகிய குவாண்டம் எண்களால் அடையாளம் காணக்கூடிய அதிகபட்ச ஆர்பிட்டால்களின் எண்ணிக்கை எவ்வளவு?",
        "choices": [
            {"letter": "A", "text_en": "$1$", "text_ta": "$1$"},
            {"letter": "B", "text_en": "$2$", "text_ta": "$2$"},
            {"letter": "C", "text_en": "$3$", "text_ta": "$3$"},
            {"letter": "D", "text_en": "$4$", "text_ta": "$4$"}
        ],
        "correct": "A",
        "explanation_en": "A specific set of three quantum numbers $(n, l, m_l)$ uniquely identifies ONE single orbital (here, the $3p_z$ orbital). That $1$ orbital can hold up to $2$ electrons ($m_s = +\\frac{1}{2}, -\\frac{1}{2}$), so the number of ORBITALS $= 1$.",
        "explanation_ta": "$(n, l, m_l)$ ஆகிய மூன்று குவாண்டம் எண்களின் குறிப்பிட்ட தொகுப்பு ஒரே ஒரு ஆர்பிட்டாலை ($3p_z$) மட்டுமே குறிக்கும். இதில் அதிகபட்சம் $2$ எலக்ட்ரான்கள் ($m_s = \\pm\\frac{1}{2}$) இருக்கலாம், ஆனால் ஆர்பிட்டாலின் எண்ணிக்கை $= 1$.",
        "ncert_key_point": "Read the noun carefully: $(n, l, m_l) \\to 1$ orbital, maximum $2$ electrons!",
        "trap_breakdown": {
            "B": "$2$ is the maximum number of ELECTRONS in that orbital, not orbitals!",
            "C": "$3$ is the total number of orbitals in the entire $3p$ subshell ($m_l = -1, 0, +1$).",
            "D": "Confusing with $l + 3$."
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
        "stem_en": "Among the isoelectronic species $\\text{N}^{3-}$, $\\text{O}^{2-}$, $\\text{F}^-$, and $\\text{Na}^+$, the correct decreasing order of ionic radius is:",
        "stem_ta": "ஒத்த எலக்ட்ரான் எண்ணிக்கை கொண்ட $\\text{N}^{3-}$, $\\text{O}^{2-}$, $\\text{F}^-$ மற்றும் $\\text{Na}^+$ அயனிகளில், அயனி ஆரத்தின் சரியான இறங்கு வரிசை எது?",
        "choices": [
            {"letter": "A", "text_en": "$\\text{Na}^+ > \\text{F}^- > \\text{O}^{2-} > \\text{N}^{3-}$", "text_ta": "$\\text{Na}^+ > \\text{F}^- > \\text{O}^{2-} > \\text{N}^{3-}$"},
            {"letter": "B", "text_en": "$\\text{N}^{3-} > \\text{O}^{2-} > \\text{F}^- > \\text{Na}^+$", "text_ta": "$\\text{N}^{3-} > \\text{O}^{2-} > \\text{F}^- > \\text{Na}^+$"},
            {"letter": "C", "text_en": "$\\text{O}^{2-} > \\text{N}^{3-} > \\text{F}^- > \\text{Na}^+$", "text_ta": "$\\text{O}^{2-} > \\text{N}^{3-} > \\text{F}^- > \\text{Na}^+$"},
            {"letter": "D", "text_en": "$\\text{N}^{3-} > \\text{F}^- > \\text{O}^{2-} > \\text{Na}^+$", "text_ta": "$\\text{N}^{3-} > \\text{F}^- > \\text{O}^{2-} > \\text{Na}^+$"}
        ],
        "correct": "B",
        "explanation_en": "All four ions have $10$ electrons. For isoelectronic species, ionic radius is inversely proportional to nuclear charge ($Z$): $\\text{N}^{3-}\\ (Z=7) > \\text{O}^{2-}\\ (Z=8) > \\text{F}^-\\ (Z=9) > \\text{Na}^+\\ (Z=11)$.",
        "explanation_ta": "நான்கு அயனிகளிலும் $10$ எலக்ட்ரான்கள் உள்ளன. ஒத்த எலக்ட்ரான் அயனிகளில் அணு எண் ($Z$) அதிகரிக்கும்போது அயனி ஆரம் குறையும்: $\\text{N}^{3-}\\ (Z=7) > \\text{O}^{2-}\\ (Z=8) > \\text{F}^-\\ (Z=9) > \\text{Na}^+\\ (Z=11)$.",
        "ncert_key_point": "Isoelectronic species ($r \\propto \\frac{1}{Z}$): More negative charge $=$ Larger size; More positive charge $=$ Smaller size.",
        "trap_breakdown": {
            "A": "Exact reverse (increasing order instead of decreasing order).",
            "C": "Swaps $\\text{N}^{3-}$ and $\\text{O}^{2-}$.",
            "D": "Swaps $\\text{O}^{2-}$ and $\\text{F}^-$."
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
        "stem_en": "According to VSEPR theory, the hybridisation of the central atom and molecular geometry of $\\text{XeF}_4$ are respectively:",
        "stem_ta": "VSEPR கொள்கையின்படி, $\\text{XeF}_4$ மூலக்கூறின் மைய அணுவின் இனக்கலப்பு மற்றும் மூலக்கூறு வடிவம் முறையே:",
        "choices": [
            {"letter": "A", "text_en": "$sp^3$, Tetrahedral", "text_ta": "$sp^3$, நான்முகி (Tetrahedral)"},
            {"letter": "B", "text_en": "$sp^3d^2$, Octahedral", "text_ta": "$sp^3d^2$, எண்முகி (Octahedral)"},
            {"letter": "C", "text_en": "$sp^3d^2$, Square planar", "text_ta": "$sp^3d^2$, தள சதுரம் (Square planar)"},
            {"letter": "D", "text_en": "$sp^3d$, See-saw", "text_ta": "$sp^3d$, சீ-சா (See-saw)"}
        ],
        "correct": "C",
        "explanation_en": "Xenon has $8$ valence electrons. In $\\text{XeF}_4$, there are $4$ bond pairs and $\\frac{8 - 4}{2} = 2$ lone pairs. Steric number $= 4 + 2 = 6 \\Rightarrow sp^3d^2$ hybridisation. Placing the $2$ lone pairs *trans* ($180^\\circ$) to minimize repulsion gives a **Square planar** molecular shape!",
        "explanation_ta": "செனானின் இணைதிறன் எலக்ட்ரான்கள் $= 8$. $\\text{XeF}_4$-இல் $4$ பிணைப்பு இணைகள் $+$ $2$ தனித்த இணைகள் $= 6 \\Rightarrow sp^3d^2$ இனக்கலப்பு. இரு தனித்த இணைகளும் எதிர் எதிரே ($180^\\circ$) அமைவதால் மூலக்கூறு வடிவம் தள சதுரம் (Square planar) ஆகும்!",
        "ncert_key_point": "Electron-pair geometry includes lone pairs (Octahedral), but Molecular geometry/shape counts ONLY atom positions (Square planar)!",
        "trap_breakdown": {
            "A": "Ignores the two lone pairs on Xenon completely.",
            "B": "Octahedral is the electron-pair arrangement, NOT the molecular shape!",
            "D": "$sp^3d$ See-saw belongs to $\\text{SF}_4$ ($4\\text{ BP} + 1\\text{ LP}$), not $\\text{XeF}_4$."
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
        "stem_en": "According to Molecular Orbital Theory, the correct decreasing order of bond order among $\\text{O}_2$, $\\text{O}_2^+$, $\\text{O}_2^-$, and $\\text{O}_2^{2-}$ is:",
        "stem_ta": "மூலக்கூறு ஆர்பிட்டால் கொள்கையின்படி (MOT), $\\text{O}_2$, $\\text{O}_2^+$, $\\text{O}_2^-$ மற்றும் $\\text{O}_2^{2-}$ ஆகியவற்றின் பிணைப்புத் தரத்தின் (bond order) சரியான இறங்கு வரிசை:",
        "choices": [
            {"letter": "A", "text_en": "$\\text{O}_2^+ > \\text{O}_2 > \\text{O}_2^- > \\text{O}_2^{2-}$", "text_ta": "$\\text{O}_2^+ > \\text{O}_2 > \\text{O}_2^- > \\text{O}_2^{2-}$"},
            {"letter": "B", "text_en": "$\\text{O}_2 > \\text{O}_2^+ > \\text{O}_2^- > \\text{O}_2^{2-}$", "text_ta": "$\\text{O}_2 > \\text{O}_2^+ > \\text{O}_2^- > \\text{O}_2^{2-}$"},
            {"letter": "C", "text_en": "$\\text{O}_2^{2-} > \\text{O}_2^- > \\text{O}_2 > \\text{O}_2^+$", "text_ta": "$\\text{O}_2^{2-} > \\text{O}_2^- > \\text{O}_2 > \\text{O}_2^+$"},
            {"letter": "D", "text_en": "$\\text{O}_2^+ > \\text{O}_2^- > \\text{O}_2 > \\text{O}_2^{2-}$", "text_ta": "$\\text{O}_2^+ > \\text{O}_2^- > \\text{O}_2 > \\text{O}_2^{2-}$"}
        ],
        "correct": "A",
        "explanation_en": "$\\text{O}_2$ ($16\\ e^-$) has $10$ bonding and $6$ antibonding electrons: $\\text{BO} = \\frac{10 - 6}{2} = 2.0$. Removing an antibonding $\\pi^*$ electron in $\\text{O}_2^+$ ($15\\ e^-$) raises $\\text{BO}$ to $2.5$. Adding electrons into $\\pi^*$ orbitals lowers $\\text{BO}$: $\\text{O}_2^-$ ($17\\ e^-$) has $\\text{BO} = 1.5$, and $\\text{O}_2^{2-}$ ($18\\ e^-$) has $\\text{BO} = 1.0$.",
        "explanation_ta": "பிணைப்புத் தரம் ($\\text{BO}$): $\\text{O}_2^+$ ($15\\ e^-$) $= 2.5$; $\\text{O}_2$ ($16\\ e^-$) $= 2.0$; $\\text{O}_2^-$ ($17\\ e^-$) $= 1.5$; $\\text{O}_2^{2-}$ ($18\\ e^-$) $= 1.0$. எனவே சரியான இறங்கு வரிசை $\\text{O}_2^+ > \\text{O}_2 > \\text{O}_2^- > \\text{O}_2^{2-}$.",
        "ncert_key_point": "14-electron shortcut: $14\\ e^- \\Rightarrow \\text{BO} = 3.0$; every $\\pm 1$ electron away from $14$ reduces $\\text{BO}$ by $0.5$ ($15 \\to 2.5,\\ 16 \\to 2.0,\\ 17 \\to 1.5,\\ 18 \\to 1.0$)!",
        "trap_breakdown": {
            "B": "Assumes neutral $\\text{O}_2$ has a higher bond order than $\\text{O}_2^+$.",
            "C": "Gives bond LENGTH order (inverse of bond order) instead of bond order!",
            "D": "Scrambles $\\text{O}_2$ and $\\text{O}_2^-$."
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
        "stem_en": "For a certain reaction, $\\Delta H = +30\\text{ kJ mol}^{-1}$ and $\\Delta S = +100\\text{ J K}^{-1}\\text{ mol}^{-1}$ (assumed independent of temperature). The reaction will be spontaneous at:",
        "stem_ta": "ஒரு வேதிவினைக்கு $\\Delta H = +30\\text{ kJ mol}^{-1}$ மற்றும் $\\Delta S = +100\\text{ J K}^{-1}\\text{ mol}^{-1}$ ஆகும். இந்த வினை எப்போது தன்னிச்சையாக (spontaneous) நிகழும்?",
        "choices": [
            {"letter": "A", "text_en": "All temperatures", "text_ta": "அனைத்து வெப்பநிலைகளிலும்"},
            {"letter": "B", "text_en": "Temperatures above $300\\text{ K}$", "text_ta": "$300\\text{ K}$-க்கு அதிகமான வெப்பநிலையில்"},
            {"letter": "C", "text_en": "Temperatures below $300\\text{ K}$", "text_ta": "$300\\text{ K}$-க்கு குறைவான வெப்பநிலையில்"},
            {"letter": "D", "text_en": "Temperatures above $0.3\\text{ K}$", "text_ta": "$0.3\\text{ K}$-க்கு அதிகமான வெப்பநிலையில்"}
        ],
        "correct": "B",
        "explanation_en": "Convert $\\Delta H$ to Joules! $\\Delta H = +30{,}000\\text{ J mol}^{-1}$, $\\Delta S = +100\\text{ J K}^{-1}\\text{ mol}^{-1}$. For spontaneity, $\\Delta G = \\Delta H - T\\Delta S < 0 \\Rightarrow T\\Delta S > \\Delta H \\Rightarrow T > \\frac{30{,}000}{100} \\Rightarrow T > 300\\text{ K}$.",
        "explanation_ta": "முதலில் $\\Delta H$-ஐ ஜூலுக்கு மாற்றவும்: $\\Delta H = 30{,}000\\text{ J mol}^{-1}$. தன்னிச்சை வினைக்கு $\\Delta G = \\Delta H - T\\Delta S < 0 \\Rightarrow T > \\frac{\\Delta H}{\\Delta S} = \\frac{30{,}000}{100} = 300\\text{ K}$.",
        "ncert_key_point": "#1 NEET Thermodynamics trap: $\\Delta H$ is given in $\\text{kJ}$ while $\\Delta S$ is given in $\\text{J}$! Always multiply $\\Delta H$ by $1000$.",
        "trap_breakdown": {
            "A": "Spontaneous at all $T$ requires $\\Delta H < 0$ and $\\Delta S > 0$.",
            "C": "Reverses the inequality sign ($\\Delta G < 0 \\Rightarrow T > \\frac{\\Delta H}{\\Delta S}$ when $\\Delta S > 0$).",
            "D": "$0.3\\text{ K}$ forgets to convert $30\\text{ kJ}$ into $30{,}000\\text{ J}$!"
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
        "stem_en": "The $\\text{pH}$ of a very dilute $10^{-8}\\text{ M}$ aqueous $\\text{HCl}$ solution at $25^\\circ\\text{C}$ is approximately:",
        "stem_ta": "$25^\\circ\\text{C}$ வெப்பநிலையில் மிக நீர்த்த $10^{-8}\\text{ M}\\ \\text{HCl}$ நீர்க்கரைசலின் $\\text{pH}$ மதிப்பு தோராயமாக:",
        "choices": [
            {"letter": "A", "text_en": "$8.00$", "text_ta": "$8.00$"},
            {"letter": "B", "text_en": "$6.98$", "text_ta": "$6.98$"},
            {"letter": "C", "text_en": "$7.02$", "text_ta": "$7.02$"},
            {"letter": "D", "text_en": "$6.00$", "text_ta": "$6.00$"}
        ],
        "correct": "B",
        "explanation_en": "An acid diluted in pure water at $25^\\circ\\text{C}$ can NEVER become basic ($\\text{pH} > 7$)! When $[\\text{HCl}] = 10^{-8}\\text{ M}$, $\\text{H}^+$ from auto-ionization of water ($\\approx 10^{-7}\\text{ M}$) must be included. Solving $[\\text{H}^+]([\\text{H}^+] - 10^{-8}) = 10^{-14}$ gives $[\\text{H}^+] \\approx 1.051 \\times 10^{-7}\\text{ M}$, so $\\text{pH} = -\\log_{10}(1.051 \\times 10^{-7}) \\approx 6.98$.",
        "explanation_ta": "அமிலக் கரைசலின் $\\text{pH}$ எப்போதும் $7$-ஐ விடக் குறைவாகவே இருக்கும் (காரமாக மாறாது)! நீரின் சுய அயனியாக்கத்திலிருந்து கிடைக்கும் $\\text{H}^+$ ($\\approx 10^{-7}\\text{ M}$) சேர்க்கப்படும்போது மொத்த $[\\text{H}^+] \\approx 1.051 \\times 10^{-7}\\text{ M} \\Rightarrow \\text{pH} \\approx 6.98$.",
        "ncert_key_point": "Very dilute strong acid ($10^{-8}\\text{ M}\\ \\text{HCl}$) $\\Rightarrow \\text{pH} \\approx 6.98$ (just below $7$). Very dilute strong base ($10^{-8}\\text{ M}\\ \\text{NaOH}$) $\\Rightarrow \\text{pH} \\approx 7.02$.",
        "trap_breakdown": {
            "A": "$8.00$ blindly applies $-\\log_{10}(10^{-8}) = 8$, absurdly claiming $\\text{HCl}$ in water is basic!",
            "C": "$7.02$ is for $10^{-8}\\text{ M}\\ \\text{NaOH}$, not $\\text{HCl}$.",
            "D": "$6.00$ overestimates $[\\text{H}^+]$ by $10\\times$."
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
        "stem_en": "How many Faradays of electricity are required for the complete reduction of $1\\text{ mole}$ of permanganate ions ($\\text{MnO}_4^-$) to $\\text{Mn}^{2+}$ ions in acidic medium?",
        "stem_ta": "அமில ஊடகத்தில் $1\\text{ மோல்}$ பெர்மாங்கனேட் அயனிகளை ($\\text{MnO}_4^-$) முழுமையாக $\\text{Mn}^{2+}$ அயனிகளாக ஒடுக்க எத்தனை பாரடே (Faraday) மின்சாரம் தேவை?",
        "choices": [
            {"letter": "A", "text_en": "$5\\text{ F}$", "text_ta": "$5\\text{ F}$"},
            {"letter": "B", "text_en": "$3\\text{ F}$", "text_ta": "$3\\text{ F}$"},
            {"letter": "C", "text_en": "$7\\text{ F}$", "text_ta": "$7\\text{ F}$"},
            {"letter": "D", "text_en": "$2\\text{ F}$", "text_ta": "$2\\text{ F}$"}
        ],
        "correct": "A",
        "explanation_en": "Half-reaction: $\\text{MnO}_4^- + 8\\text{H}^+ + 5e^- \\to \\text{Mn}^{2+} + 4\\text{H}_2\\text{O}$. Oxidation state of $\\text{Mn}$ changes from $+7$ (in $\\text{MnO}_4^-$) to $+2$ (in $\\text{Mn}^{2+}$), requiring $5\\text{ moles}$ of electrons per mole of $\\text{MnO}_4^-$, which equals $5\\text{ Faradays}$ ($5\\text{ F}$).",
        "explanation_ta": "$\\text{MnO}_4^-$-இல் $\\text{Mn}$-இன் ஆக்சிஜனேற்ற எண் $+7$. இது $\\text{Mn}^{2+}$ ($+2$) ஆக மாற $1\\text{ மோலுக்கு}$ $5\\text{ மோல்}$ எலக்ட்ரான்கள் தேவை ($\\text{MnO}_4^- + 8\\text{H}^+ + 5e^- \\to \\text{Mn}^{2+} + 4\\text{H}_2\\text{O}$). எனவே தேவையான மின்னூட்டம் $= 5\\text{ F}$.",
        "ncert_key_point": "Charge in Faradays per mole $= |\\text{Change in oxidation number per formula unit}|$.",
        "trap_breakdown": {
            "B": "$3\\text{ F}$ is for reduction of $\\text{MnO}_4^-$ to $\\text{MnO}_2$ ($+4$) in neutral/faintly alkaline medium.",
            "C": "$7\\text{ F}$ confuses initial oxidation state $+7$ with change in oxidation state ($7 - 2 = 5$).",
            "D": "$2\\text{ F}$ confuses final charge $+2$ with electrons transferred."
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
        "stem_en": "Assuming $100\\%$ dissociation of strong electrolytes, which of the following $0.1\\text{ m}$ aqueous solutions will have the HIGHEST boiling point?",
        "stem_ta": "வலிமையான மின்பகுளிகள் $100\\%$ பிரிகையடைகின்றன எனக் கொண்டால், பின்வரும் $0.1\\text{ m}$ நீர்க்கரைசல்களில் எதற்குக் கொதிநிலை மிக அதிகமாக இருக்கும்?",
        "choices": [
            {"letter": "A", "text_en": "$0.1\\text{ m}$ Glucose", "text_ta": "$0.1\\text{ m}$ குளுக்கோஸ்"},
            {"letter": "B", "text_en": "$0.1\\text{ m}\\ \\text{NaCl}$", "text_ta": "$0.1\\text{ m}\\ \\text{NaCl}$"},
            {"letter": "C", "text_en": "$0.1\\text{ m}\\ \\text{BaCl}_2$", "text_ta": "$0.1\\text{ m}\\ \\text{BaCl}_2$"},
            {"letter": "D", "text_en": "$0.1\\text{ m}\\ \\text{Al}_2(\\text{SO}_4)_3$", "text_ta": "$0.1\\text{ m}\\ \\text{Al}_2(\\text{SO}_4)_3$"}
        ],
        "correct": "D",
        "explanation_en": "Boiling point elevation $\\Delta T_b = i K_b m$. At equal molality ($0.1\\text{ m}$), a larger van 't Hoff factor $i$ gives higher $\\Delta T_b$ and the highest boiling point. Glucose: $i = 1$; $\\text{NaCl}$: $i = 2$; $\\text{BaCl}_2$: $i = 3$; $\\text{Al}_2(\\text{SO}_4)_3 \\to 2\\text{Al}^{3+} + 3\\text{SO}_4^{2-}$ gives $i = 5$ (highest!).",
        "explanation_ta": "கொதிநிலை ஏற்றம் $\\Delta T_b = i K_b m$. சம மோலாலிட்டியில் $i$ மதிப்பு அதிகமாக உள்ள கரைசலின் கொதிநிலை அதிகமாக இருக்கும். $\\text{Al}_2(\\text{SO}_4)_3 \\to 2\\text{Al}^{3+} + 3\\text{SO}_4^{2-}$ ($i = 5$), எனவே இதற்கே அதிக கொதிநிலை!",
        "ncert_key_point": "Highest $i \\Rightarrow$ Highest boiling point & osmotic pressure, BUT LOWEST freezing point & vapour pressure! Read carefully!",
        "trap_breakdown": {
            "A": "Glucose ($i = 1$) has the HIGHEST freezing point / vapour pressure, but LOWEST boiling point.",
            "B": "$\\text{NaCl}$ has $i = 2$.",
            "C": "$\\text{BaCl}_2$ has $i = 3$."
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
        "stem_en": "A first-order reaction is $50\\%$ complete in $20\\text{ minutes}$. The time required for $87.5\\%$ completion of the same reaction is:",
        "stem_ta": "முதல் வகை வினை ஒன்று $50\\%$ நிறைவடைய $20\\text{ நிமிடங்கள்}$ ஆகிறது. அதே வினை $87.5\\%$ நிறைவடைய ஆகும் நேரம் எவ்வளவு?",
        "choices": [
            {"letter": "A", "text_en": "$40\\text{ minutes}$", "text_ta": "$40\\text{ நிமிடங்கள்}$"},
            {"letter": "B", "text_en": "$60\\text{ minutes}$", "text_ta": "$60\\text{ நிமிடங்கள்}$"},
            {"letter": "C", "text_en": "$80\\text{ minutes}$", "text_ta": "$80\\text{ நிமிடங்கள்}$"},
            {"letter": "D", "text_en": "$35\\text{ minutes}$", "text_ta": "$35\\text{ நிமிடங்கள்}$"}
        ],
        "correct": "B",
        "explanation_en": "For a first-order reaction, half-life $t_{1/2} = 20\\text{ min}$ is independent of initial concentration. $87.5\\%$ completion means $12.5\\% = \\left(\\frac{1}{2}\\right)^3$ of reactant remains! $100\\% \\to 50\\%\\ (20\\text{ min}) \\to 25\\%\\ (40\\text{ min}) \\to 12.5\\%\\ (60\\text{ min})$. Thus $t_{87.5\\%} = 3 \\times t_{1/2} = 60\\text{ minutes}$.",
        "explanation_ta": "முதல் வகை வினையின் அரைவாழ்வுக் காலம் $t_{1/2} = 20\\text{ நிமிடம்}$. $87.5\\%$ நிறைவு என்றால் $12.5\\% = \\left(\\frac{1}{2}\\right)^3$ மீதமுள்ளது: $100\\% \\to 50\\% \\to 25\\% \\to 12.5\\%$ ($3$ அரைவாழ்வுக் காலங்கள்). எனவே $t_{87.5\\%} = 3 \\times 20 = 60\\text{ நிமிடங்கள்}$.",
        "ncert_key_point": "Memorize first-order ratios: $t_{75\\%} = 2\\,t_{1/2}$; $t_{87.5\\%} = 3\\,t_{1/2}$; $t_{99.9\\%} \\approx 10\\,t_{1/2}$.",
        "trap_breakdown": {
            "A": "$40\\text{ minutes}$ ($2\\,t_{1/2}$) gives $75\\%$ completion ($25\\%$ remaining).",
            "C": "$80\\text{ minutes}$ ($4\\,t_{1/2}$) gives $93.75\\%$ completion ($6.25\\%$ remaining).",
            "D": "$35\\text{ minutes}$ wrongly assumes zero-order linear proportionality ($20 \\times \\frac{87.5}{50}$)."
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
        "stem_en": "The spin-only magnetic moment of divalent $\\text{Mn}^{2+}$ ion (atomic number $Z = 25$) in aqueous solution is:",
        "stem_ta": "நீர்க்கரைசலில் ஈரிணைதிறன் கொண்ட $\\text{Mn}^{2+}$ அயனியின் (அணு எண் $Z = 25$) தற்சுழற்சி காந்தத் திருப்புத்திறன் (spin-only magnetic moment) மதிப்பு:",
        "choices": [
            {"letter": "A", "text_en": "$4.90\\text{ BM}$", "text_ta": "$4.90\\text{ BM}$"},
            {"letter": "B", "text_en": "$5.92\\text{ BM}$", "text_ta": "$5.92\\text{ BM}$"},
            {"letter": "C", "text_en": "$3.87\\text{ BM}$", "text_ta": "$3.87\\text{ BM}$"},
            {"letter": "D", "text_en": "$2.84\\text{ BM}$", "text_ta": "$2.84\\text{ BM}$"}
        ],
        "correct": "B",
        "explanation_en": "Ground state $\\text{Mn}$ ($Z = 25$) is $[\\text{Ar}]\\,3d^5 4s^2$. Losing two $4s$ electrons gives $\\text{Mn}^{2+} = [\\text{Ar}]\\,3d^5$ with $n = 5$ unpaired electrons. Spin-only magnetic moment $\\mu = \\sqrt{n(n + 2)} = \\sqrt{5 \\times 7} = \\sqrt{35} \\approx 5.92\\text{ BM}$.",
        "explanation_ta": "$\\text{Mn}$ ($Z = 25$): $[\\text{Ar}]\\,3d^5 4s^2 \\Rightarrow \\text{Mn}^{2+}$: $[\\text{Ar}]\\,3d^5$. தனித்த எலக்ட்ரான்கள் $n = 5$. காந்தத் திருப்புத்திறன் $\\mu = \\sqrt{n(n + 2)} = \\sqrt{35} \\approx 5.92\\text{ BM}$.",
        "ncert_key_point": "Integer shortcut: integer part of $\\mu = \\sqrt{n(n+2)}$ ALWAYS equals $n$! ($n=1 \\to 1.73,\\ n=2 \\to 2.84,\\ n=3 \\to 3.87,\\ n=4 \\to 4.90,\\ n=5 \\to 5.92\\text{ BM}$).",
        "trap_breakdown": {
            "A": "$4.90\\text{ BM}$ corresponds to $n = 4$ (e.g., $\\text{Fe}^{2+}$ or $\\text{Cr}^{2+}$).",
            "C": "$3.87\\text{ BM}$ corresponds to $n = 3$ (e.g., $\\text{Cr}^{3+}$ or $\\text{Co}^{2+}$).",
            "D": "$2.84\\text{ BM}$ corresponds to $n = 2$ (e.g., $\\text{Ni}^{2+}$)."
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
        "stem_en": "The hybridisation, geometry, and magnetic nature of the complex ion $[\\text{Ni(CN)}_4]^{2-}$ (atomic number of $\\text{Ni} = 28$) are respectively:",
        "stem_ta": "$[\\text{Ni(CN)}_4]^{2-}$ என்ற அணைவு அயனியின் இனக்கலப்பு, வடிவியல் மற்றும் காந்தத் தன்மை முறையே ($\\text{Ni}$ அணு எண் $= 28$):",
        "choices": [
            {"letter": "A", "text_en": "$sp^3$, Tetrahedral, Paramagnetic", "text_ta": "$sp^3$, நான்முகி, பாராகாந்தத் தன்மை"},
            {"letter": "B", "text_en": "$dsp^2$, Square planar, Diamagnetic", "text_ta": "$dsp^2$, தள சதுரம், டயாகாந்தத் தன்மை"},
            {"letter": "C", "text_en": "$sp^3$, Tetrahedral, Diamagnetic", "text_ta": "$sp^3$, நான்முகி, டயாகாந்தத் தன்மை"},
            {"letter": "D", "text_en": "$dsp^2$, Square planar, Paramagnetic", "text_ta": "$dsp^2$, தள சதுரம், பாராகாந்தத் தன்மை"}
        ],
        "correct": "B",
        "explanation_en": "In $[\\text{Ni(CN)}_4]^{2-}$, Nickel is in $+2$ state ($3d^8$). Cyanide ($\\text{CN}^-$) is a strong-field ligand, forcing the $8$ $d$-electrons to pair up in four $3d$ orbitals, leaving one $3d$ orbital vacant for $dsp^2$ hybridisation $\\to$ Square planar geometry and Diamagnetic ($0$ unpaired electrons).",
        "explanation_ta": "$[\\text{Ni(CN)}_4]^{2-}$-இல் $\\text{Ni}^{2+}$ ($3d^8$) உள்ளது. $\\text{CN}^-$ வலிமையான ஈனி (strong-field ligand) என்பதால் எலக்ட்ரான்கள் இணையாகி $dsp^2$ இனக்கலப்பு, தள சதுர வடிவம் மற்றும் டயாகாந்தத் தன்மையைப் ($0$ தனித்த எலக்ட்ரான்) பெறுகிறது.",
        "ncert_key_point": "Contrast the classic NCERT trio: $[\\text{NiCl}_4]^{2-}$ ($sp^3$, tetrahedral, paramagnetic, $2\\ e^-$), $[\\text{Ni(CN)}_4]^{2-}$ ($dsp^2$, square planar, diamagnetic), $[\\text{Ni(CO)}_4]$ ($\\text{Ni}^0\\ 3d^{10}$, $sp^3$, tetrahedral, diamagnetic)!",
        "trap_breakdown": {
            "A": "$sp^3$, Tetrahedral, Paramagnetic is for $[\\text{NiCl}_4]^{2-}$ (weak-field $\\text{Cl}^-$ ligand).",
            "C": "$sp^3$, Tetrahedral, Diamagnetic is for neutral $[\\text{Ni(CO)}_4]$ where $\\text{Ni}$ is in $0$ oxidation state!",
            "D": "$dsp^2$ $\\text{Ni(II)}$ cannot be paramagnetic because all $8$ $3d$ electrons are paired."
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
        "stem_en": "Arrange the following compounds in decreasing order of acidic strength: (I) Phenol, (II) *p*-Nitrophenol, (III) *p*-Cresol (4-methylphenol), (IV) 2,4,6-Trinitrophenol (Picric acid).",
        "stem_ta": "பின்வரும் சேர்மங்களை அவற்றின் அமில வலிமையின் இறங்கு வரிசையில் எழுதுக: (I) பீனால், (II) *p*-நைட்ரோபீனால், (III) *p*-கிரெசால் (4-மெத்தில்பீனால்), (IV) 2,4,6-டிரைநைட்ரோபீனால் (பிக்ரிக் அமிலம்).",
        "choices": [
            {"letter": "A", "text_en": "$\\text{IV} > \\text{II} > \\text{I} > \\text{III}$", "text_ta": "$\\text{IV} > \\text{II} > \\text{I} > \\text{III}$"},
            {"letter": "B", "text_en": "$\\text{II} > \\text{IV} > \\text{I} > \\text{III}$", "text_ta": "$\\text{II} > \\text{IV} > \\text{I} > \\text{III}$"},
            {"letter": "C", "text_en": "$\\text{IV} > \\text{II} > \\text{III} > \\text{I}$", "text_ta": "$\\text{IV} > \\text{II} > \\text{III} > \\text{I}$"},
            {"letter": "D", "text_en": "$\\text{III} > \\text{I} > \\text{II} > \\text{IV}$", "text_ta": "$\\text{III} > \\text{I} > \\text{II} > \\text{IV}$"}
        ],
        "correct": "A",
        "explanation_en": "Electron-withdrawing groups ($-\\text{NO}_2$ via $-M$ and $-I$ effects) disperse negative charge on the phenoxide ion and strongly INCREASE acidity; electron-donating groups ($-\\text{CH}_3$ via $+I$ and hyperconjugation) DECREASE acidity. Thus: Picric acid (IV) $>$ *p*-Nitrophenol (II) $>$ Phenol (I) $>$ *p*-Cresol (III).",
        "explanation_ta": "எலக்ட்ரான் கவரும் தொகுதிகள் ($-\\text{NO}_2$) பீனாக்சைடு அயனியை நிலைப்படுத்தி அமிலத் தன்மையை அதிகரிக்கும்; எலக்ட்ரான் தரும் தொகுதிகள் ($-\\text{CH}_3$) அமிலத் தன்மையைக் குறைக்கும். எனவே: $\\text{IV} > \\text{II} > \\text{I} > \\text{III}$.",
        "ncert_key_point": "EWG ($-\\text{NO}_2, -\\text{CN}, -\\text{X}$) increases acidity (lower $\\text{p}K_a$); EDG ($-\\text{CH}_3, -\\text{OCH}_3$) decreases acidity (higher $\\text{p}K_a$).",
        "trap_breakdown": {
            "B": "Three $-\\text{NO}_2$ groups stabilize phenoxide far more than one $-\\text{NO}_2$ group.",
            "C": "Places *p*-cresol above phenol despite its destabilizing $+I$ methyl group.",
            "D": "Gives increasing order of acidic strength (decreasing $\\text{p}K_a$ reversed) instead of decreasing acidic strength."
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
        "stem_en": "Reductive ozonolysis ((i) $\\text{O}_3$, (ii) $\\text{Zn}/\\text{H}_2\\text{O}$) of an alkene 'X' gives an equimolar mixture of ethanal ($\\text{CH}_3\\text{CHO}$) and propanone ($\\text{CH}_3\\text{COCH}_3$). The IUPAC name of alkene 'X' is:",
        "stem_ta": "ஆல்கீன் 'X' ஆனது ஒடுக்க ஓசோனேற்றம் ((i) $\\text{O}_3$, (ii) $\\text{Zn}/\\text{H}_2\\text{O}$) அடையும்போது எத்தனல் ($\\text{CH}_3\\text{CHO}$) மற்றும் புரோப்பனோன் ($\\text{CH}_3\\text{COCH}_3$) ஆகியவற்றை சம மோலார் அளவில் தருகிறது. 'X'-இன் IUPAC பெயர் என்ன?",
        "choices": [
            {"letter": "A", "text_en": "2-Methylbut-2-ene", "text_ta": "2-மெத்தில்பியூட்-2-ஈன்"},
            {"letter": "B", "text_en": "2-Methylbut-1-ene", "text_ta": "2-மெத்தில்பியூட்-1-ஈன்"},
            {"letter": "C", "text_en": "Pent-2-ene", "text_ta": "பென்ட்-2-ஈன்"},
            {"letter": "D", "text_en": "2,3-Dimethylbut-2-ene", "text_ta": "2,3-டைமெத்தில்பியூட்-2-ஈன்"}
        ],
        "correct": "A",
        "explanation_en": "Shortcut: place the carbonyl oxygens face-to-face: $(\\text{CH}_3)_2\\text{C=O} + \\text{O=CH–CH}_3$, erase both $\\text{O}$ atoms, and join with a double bond $\\Rightarrow (\\text{CH}_3)_2\\text{C=CH–CH}_3$. Numbering the 4-carbon chain from the left gives the double bond at $\\text{C}_2$ and methyl branch at $\\text{C}_2$: **2-Methylbut-2-ene**.",
        "explanation_ta": "$(\\text{CH}_3)_2\\text{C=O}$ மற்றும் $\\text{O=CH–CH}_3$ ஆகியவற்றின் ஆக்சிஜன்களை நீக்கி இரட்டைப் பிணைப்பால் இணைத்தால் $(\\text{CH}_3)_2\\text{C=CH–CH}_3$ கிடைக்கும். இதன் IUPAC பெயர் **2-மெத்தில்பியூட்-2-ஈன்**.",
        "ncert_key_point": "Reverse ozonolysis trick: point the two $\\text{C=O}$ groups at each other, delete $\\text{O} + \\text{O}$, and weld $\\text{C=C}$.",
        "trap_breakdown": {
            "B": "2-Methylbut-1-ene gives methanal ($\\text{HCHO}$) $+$ butan-2-one.",
            "C": "Pent-2-ene gives ethanal $+$ propanal (two aldehydes, no ketone).",
            "D": "2,3-Dimethylbut-2-ene gives $2\\text{ moles}$ of propanone only."
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
        "stem_en": "Which of the following alkyl bromides undergoes nucleophilic substitution by the $\\text{S}_{\\text{N}}1$ mechanism at the FASTEST rate?",
        "stem_ta": "பின்வரும் ஆல்கைல் புரோமைடுகளில் எது $\\text{S}_{\\text{N}}1$ வினைவழிமுறையின் மூலம் மிக வேகமாக கருக்கவர் பதிலீட்டு வினைக்கு உட்படும்?",
        "choices": [
            {"letter": "A", "text_en": "$\\text{CH}_3\\text{CH}_2\\text{Br}$", "text_ta": "$\\text{CH}_3\\text{CH}_2\\text{Br}$"},
            {"letter": "B", "text_en": "$(\\text{CH}_3)_2\\text{CHBr}$", "text_ta": "$(\\text{CH}_3)_2\\text{CHBr}$"},
            {"letter": "C", "text_en": "$(\\text{CH}_3)_3\\text{CBr}$", "text_ta": "$(\\text{CH}_3)_3\\text{CBr}$"},
            {"letter": "D", "text_en": "$\\text{CH}_3\\text{Br}$", "text_ta": "$\\text{CH}_3\\text{Br}$"}
        ],
        "correct": "C",
        "explanation_en": "The rate-determining step of $\\text{S}_{\\text{N}}1$ is unimolecular $\\text{C–Br}$ bond cleavage to form a carbocation intermediate. Tertiary carbocation $(\\text{CH}_3)_3\\text{C}^+$ is stabilized by $9$ $\\alpha$-$\\text{C–H}$ hyperconjugative structures $+\\ +I$ effect, so $3^\\circ$ halide $(\\text{CH}_3)_3\\text{CBr}$ reacts fastest via $\\text{S}_{\\text{N}}1$!",
        "explanation_ta": "$\\text{S}_{\\text{N}}1$ வினையின் வேகம் உருவாகும் கார்பன் நேர் அயனியின் (carbocation) நிலைப்புத்தன்மையைப் பொறுத்தது. மூவிணைய ($3^\\circ$) கார்பன் நேர் அயனி $(\\text{CH}_3)_3\\text{C}^+$ மிகவும் நிலைப்புத்தன்மை உடையதால் $(\\text{CH}_3)_3\\text{CBr}$ மிக வேகமாக வினைபுரியும்!",
        "ncert_key_point": "Alkyl halide reactivity: $\\text{S}_{\\text{N}}1 \\Rightarrow 3^\\circ > 2^\\circ > 1^\\circ > \\text{CH}_3\\text{X}$; $\\text{S}_{\\text{N}}2 \\Rightarrow \\text{CH}_3\\text{X} > 1^\\circ > 2^\\circ > 3^\\circ$.",
        "trap_breakdown": {
            "A": "$1^\\circ$ halide ($\\text{CH}_3\\text{CH}_2\\text{Br}$) prefers $\\text{S}_{\\text{N}}2$.",
            "B": "$2^\\circ$ carbocation is less stable than $3^\\circ$.",
            "D": "$\\text{CH}_3\\text{Br}$ reacts fastest via $\\text{S}_{\\text{N}}2$, and slowest via $\\text{S}_{\\text{N}}1$!"
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
        "stem_en": "When phenol is treated with chloroform ($\\text{CHCl}_3$) and aqueous $\\text{NaOH}$ followed by acidification, the major product obtained is (Reimer–Tiemann reaction):",
        "stem_ta": "பீனாலை குளோரோஃபார்ம் ($\\text{CHCl}_3$) மற்றும் நீர்த்த $\\text{NaOH}$ உடன் வினைப்படுத்தி, பின் அமிலமாக்கும்போது கிடைக்கும் முதன்மை விளைபொருள் எது (ரைமர்-டீமன் வினை)?",
        "choices": [
            {"letter": "A", "text_en": "Salicylic acid (2-Hydroxybenzoic acid)", "text_ta": "சாலிசிலிக் அமிலம் (2-ஹைட்ராக்சிபென்சாயிக் அமிலம்)"},
            {"letter": "B", "text_en": "Salicylaldehyde (2-Hydroxybenzaldehyde)", "text_ta": "சாலிசிலால்டிஹைடு (2-ஹைட்ராக்சிபென்சால்டிஹைடு)"},
            {"letter": "C", "text_en": "Benzoquinone", "text_ta": "பென்சோகுயினோன்"},
            {"letter": "D", "text_en": "Benzaldehyde", "text_ta": "பென்சால்டிஹைடு"}
        ],
        "correct": "B",
        "explanation_en": "In the Reimer–Tiemann reaction, $\\text{CHCl}_3 + \\text{NaOH}$ generates the electrophile dichlorocarbene ($:\\!\\text{CCl}_2$), which attacks the *ortho* position of phenoxide ion, hydrolyzes to $-\\text{CHO}$, and upon acidification yields **Salicylaldehyde** (2-hydroxybenzaldehyde).",
        "explanation_ta": "ரைமர்-டீமன் வினையில் $\\text{CHCl}_3 + \\text{NaOH}$ வினைபுரிந்து டைகுளோரோகார்பீன் ($:\\!\\text{CCl}_2$) எலக்ட்ரான் கவர் காரணியை உருவாக்கி, **சாலிசிலால்டிஹைடை** (2-ஹைட்ராக்சிபென்சால்டிஹைடு) முதன்மை விளைபொருளாகத் தருகிறது.",
        "ncert_key_point": "Phenol $+\\ \\text{CHCl}_3/\\text{NaOH} \\to$ Salicylaldehyde (Reimer–Tiemann); Phenol $+\\ \\text{CO}_2/\\text{NaOH} \\to$ Salicylic acid (Kolbe's reaction); Phenol $+\\ \\text{Zn}$ dust $\\to$ Benzene.",
        "trap_breakdown": {
            "A": "Salicylic acid is formed in Kolbe's reaction ($\\text{CO}_2 + \\text{NaOH}$) or if $\\text{CCl}_4$ is used instead of $\\text{CHCl}_3$!",
            "C": "Benzoquinone is formed on oxidation of phenol with $\\text{Na}_2\\text{Cr}_2\\text{O}_7 / \\text{H}_2\\text{SO}_4$.",
            "D": "Phenol's $-\\text{OH}$ group remains intact; $\\text{Zn}$ dust is not used here."
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
        "stem_en": "Which of the following aldehydes will undergo Cannizzaro disproportionation reaction on heating with concentrated $\\text{NaOH}$?",
        "stem_ta": "பின்வரும் ஆல்டிஹைடுகளில் எது அடர் $\\text{NaOH}$ உடன் வெப்பப்படுத்தும்போது கன்னிசாரோ (Cannizzaro) விகிதச்சிதைவு வினைக்கு உட்படும்?",
        "choices": [
            {"letter": "A", "text_en": "Ethanal ($\\text{CH}_3\\text{CHO}$)", "text_ta": "எத்தனல் ($\\text{CH}_3\\text{CHO}$)"},
            {"letter": "B", "text_en": "Propanal ($\\text{CH}_3\\text{CH}_2\\text{CHO}$)", "text_ta": "புரோப்பனல் ($\\text{CH}_3\\text{CH}_2\\text{CHO}$)"},
            {"letter": "C", "text_en": "Benzaldehyde ($\\text{C}_6\\text{H}_5\\text{CHO}$)", "text_ta": "பென்சால்டிஹைடு ($\\text{C}_6\\text{H}_5\\text{CHO}$)"},
            {"letter": "D", "text_en": "Phenylacetaldehyde ($\\text{C}_6\\text{H}_5\\text{CH}_2\\text{CHO}$)", "text_ta": "பினைல்அசிட்டால்டிஹைடு ($\\text{C}_6\\text{H}_5\\text{CH}_2\\text{CHO}$)"}
        ],
        "correct": "C",
        "explanation_en": "Cannizzaro reaction is given ONLY by aldehydes that have NO $\\alpha$-hydrogen atom! In Benzaldehyde ($\\text{C}_6\\text{H}_5\\text{CHO}$), the carbon attached to $-\\text{CHO}$ is a ring $sp^2$ carbon bearing zero hydrogens, so it disproportionates into Benzyl alcohol ($\\text{C}_6\\text{H}_5\\text{CH}_2\\text{OH}$) $+$ Sodium benzoate ($\\text{C}_6\\text{H}_5\\text{COONa}$).",
        "explanation_ta": "ஆல்பா-ஹைட்ரஜன் ($\\alpha$-$\\text{H}$) இல்லாத ஆல்டிஹைடுகள் மட்டுமே கன்னிசாரோ வினைக்கு உட்படும்! பென்சால்டிஹைடில் ($\\text{C}_6\\text{H}_5\\text{CHO}$) $\\alpha$-$\\text{H}$ இல்லை என்பதால் அது பென்சைல் ஆல்கஹால் மற்றும் சோடியம் பென்சோயேட்டைத் தருகிறது.",
        "ncert_key_point": "Has $\\alpha$-$\\text{H} \\Rightarrow$ Aldol condensation (dilute alkali). Zero $\\alpha$-$\\text{H}$ ($\\text{HCHO}$, $\\text{C}_6\\text{H}_5\\text{CHO}$, $(\\text{CH}_3)_3\\text{CCHO}$) $\\Rightarrow$ Cannizzaro reaction (conc. alkali).",
        "trap_breakdown": {
            "A": "Ethanal has $3$ $\\alpha$-hydrogens $\\to$ undergoes Aldol condensation.",
            "B": "Propanal has $2$ $\\alpha$-hydrogens $\\to$ undergoes Aldol condensation.",
            "D": "Phenylacetaldehyde has $2$ benzylic $\\alpha$-hydrogens ($-\\text{CH}_2-$) $\\to$ undergoes Aldol condensation!"
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
        "stem_en": "Which reagent converts Ethanamide ($\\text{CH}_3\\text{CONH}_2$) directly into Methanamine ($\\text{CH}_3\\text{NH}_2$) with one carbon atom less?",
        "stem_ta": "எத்தனமைடை ($\\text{CH}_3\\text{CONH}_2$) ஒரு கார்பன் அணு குறைவான மெத்தனமீனாக ($\\text{CH}_3\\text{NH}_2$) நேரடியாக மாற்றும் வினைக்காரணி எது?",
        "choices": [
            {"letter": "A", "text_en": "$\\text{LiAlH}_4$ followed by $\\text{H}_2\\text{O}$", "text_ta": "$\\text{LiAlH}_4$ மற்றும் $\\text{H}_2\\text{O}$"},
            {"letter": "B", "text_en": "$\\text{Br}_2$ and aqueous/ethanolic $\\text{NaOH}$", "text_ta": "$\\text{Br}_2$ மற்றும் நீர்த்த/ஆல்கஹால் கலந்த $\\text{NaOH}$"},
            {"letter": "C", "text_en": "$\\text{P}_2\\text{O}_5$ with heating", "text_ta": "$\\text{P}_2\\text{O}_5$ உடன் வெப்பப்படுத்துதல்"},
            {"letter": "D", "text_en": "$\\text{NaNO}_2 + \\text{HCl}$", "text_ta": "$\\text{NaNO}_2 + \\text{HCl}$"}
        ],
        "correct": "B",
        "explanation_en": "Hoffmann bromamide degradation: $\\text{CH}_3\\text{CONH}_2 + \\text{Br}_2 + 4\\text{NaOH} \\to \\text{CH}_3\\text{NH}_2 + \\text{Na}_2\\text{CO}_3 + 2\\text{NaBr} + 2\\text{H}_2\\text{O}$. The carbonyl carbon is lost as $\\text{Na}_2\\text{CO}_3$, producing a primary amine with ONE fewer carbon atom.",
        "explanation_ta": "ஹாஃப்மன் புரோமமைடு இறக்க வினை: $\\text{CH}_3\\text{CONH}_2 + \\text{Br}_2 + 4\\text{NaOH} \\to \\text{CH}_3\\text{NH}_2 + \\text{Na}_2\\text{CO}_3 + 2\\text{NaBr} + 2\\text{H}_2\\text{O}$. இது ஒரு கார்பன் குறைவான ஓரிணைய அமீனைத் தருகிறது.",
        "ncert_key_point": "Step-down amine ($n - 1$ carbons): $\\text{Br}_2/\\text{NaOH}$ on amide. Same-carbon amine ($n$ carbons): $\\text{LiAlH}_4$ reduction of amide.",
        "trap_breakdown": {
            "A": "$\\text{LiAlH}_4$ reduces $-\\text{CONH}_2$ to $-\\text{CH}_2\\text{NH}_2$, giving Ethanamine ($\\text{CH}_3\\text{CH}_2\\text{NH}_2$, $2$ carbons), NOT Methanamine!",
            "C": "$\\text{P}_2\\text{O}_5$ dehydrates ethanamide to ethanenitrile ($\\text{CH}_3\\text{CN}$).",
            "D": "$\\text{HNO}_2$ ($\\text{NaNO}_2 + \\text{HCl}$) converts primary amide into ethanoic acid ($\\text{CH}_3\\text{COOH}$) $+\\ \\text{N}_2$."
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
        "stem_en": "Given below are two statements:\nStatement I: Sucrose is a non-reducing sugar because the glycosidic linkage is between $\\text{C}_1$ of $\\alpha$-D-glucose and $\\text{C}_2$ of $\\beta$-D-fructose, locking both reducing groups.\nStatement II: Maltose and lactose are reducing sugars.\nChoose the correct option:",
        "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன:\nகூற்று I: சுக்ரோஸில் $\\alpha$-D-குளுக்கோஸின் $\\text{C}_1$ மற்றும் $\\beta$-D-ஃபிரக்டோஸின் $\\text{C}_2$ இடையே கிளைக்கோசிடிக் பிணைப்பு உள்ளதால் இது ஒரு ஒடுக்கா சர்க்கரை (non-reducing sugar) ஆகும்.\nகூற்று II: மால்டோஸ் மற்றும் லாக்டோஸ் ஆகியவை ஒடுக்கும் சர்க்கரைகள் (reducing sugars) ஆகும்.\nசரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        "choices": [
            {"letter": "A", "text_en": "Both Statement I and Statement II are correct", "text_ta": "கூற்று I மற்றும் கூற்று II ஆகிய இரண்டும் சரி"},
            {"letter": "B", "text_en": "Both Statement I and Statement II are incorrect", "text_ta": "கூற்று I மற்றும் கூற்று II ஆகிய இரண்டும் தவறு"},
            {"letter": "C", "text_en": "Statement I is correct but Statement II is incorrect", "text_ta": "கூற்று I சரி, ஆனால் கூற்று II தவறு"},
            {"letter": "D", "text_en": "Statement I is incorrect but Statement II is correct", "text_ta": "கூற்று I தவறு, ஆனால் கூற்று II சரி"}
        ],
        "correct": "A",
        "explanation_en": "Exact NCERT Biomolecules facts: In sucrose, both anomeric carbons ($\\text{C}_1$ of $\\alpha$-D-glucose and $\\text{C}_2$ of $\\beta$-D-fructose) participate in the glycosidic bond, so it cannot reduce Fehling's or Tollens' reagent. Maltose and lactose each retain one free hemiacetal $\\text{C}_1$ group and are reducing sugars.",
        "explanation_ta": "NCERT உயிரிமூலக்கூறுகள் பாடத்தின்படி: சுக்ரோஸில் இரு ஒடுக்கும் தொகுதிகளும் ($\\text{C}_1$ மற்றும் $\\text{C}_2$) பிணைப்பில் ஈடுபட்டுள்ளதால் அது ஒடுக்கா சர்க்கரை ஆகும். மால்டோஸ் மற்றும் லாக்டோஸ் ஒடுக்கும் சர்க்கரைகள் ஆகும். எனவே இரு கூற்றுகளும் சரி.",
        "ncert_key_point": "All monosaccharides $+$ Maltose $+$ Lactose $=$ Reducing sugars. Sucrose $=$ Non-reducing disaccharide!",
        "trap_breakdown": {
            "B": "Contradicts NCERT disaccharide classification.",
            "C": "Maltose and lactose DO reduce Tollens' and Fehling's solutions.",
            "D": "$\\text{C}_1$($\\alpha$-D-glucose)–$\\text{C}_2$($\\beta$-D-fructose) is the exact NCERT linkage of sucrose."
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
            {"letter": "A", "text_en": "$\\text{Na}_4[\\text{Fe(CN)}_6]$", "text_ta": "$\\text{Na}_4[\\text{Fe(CN)}_6]$"},
            {"letter": "B", "text_en": "$\\text{Fe}_4[\\text{Fe(CN)}_6]_3 \\cdot x\\text{H}_2\\text{O}$", "text_ta": "$\\text{Fe}_4[\\text{Fe(CN)}_6]_3 \\cdot x\\text{H}_2\\text{O}$"},
            {"letter": "C", "text_en": "$[\\text{Fe(CN)}_5\\text{NOS}]^{4-}$", "text_ta": "$[\\text{Fe(CN)}_5\\text{NOS}]^{4-}$"},
            {"letter": "D", "text_en": "$[\\text{Fe(SCN)}]^{2+}$", "text_ta": "$[\\text{Fe(SCN)}]^{2+}$"}
        ],
        "correct": "B",
        "explanation_en": "Sodium fusion extract contains $\\text{NaCN}$, which reacts with $\\text{Fe}^{2+}$ to form $\\text{Na}_4[\\text{Fe(CN)}_6]$. Upon boiling with conc. $\\text{H}_2\\text{SO}_4$/air, some $\\text{Fe}^{2+}$ oxidizes to $\\text{Fe}^{3+}$, reacting with $[\\text{Fe(CN)}_6]^{4-}$ to form Iron(III) hexacyanoferrate(II), $\\text{Fe}_4[\\text{Fe(CN)}_6]_3 \\cdot x\\text{H}_2\\text{O}$ (Prussian blue).",
        "explanation_ta": "சோடியம் சாறு $\\text{FeSO}_4$ உடன் வினைபுரிந்து $\\text{Na}_4[\\text{Fe(CN)}_6]$ உருவாக்கி, பின் $\\text{Fe}^{3+}$ அயனிகளுடன் இணைந்து $\\text{Fe}_4[\\text{Fe(CN)}_6]_3 \\cdot x\\text{H}_2\\text{O}$ (ஃபெரிக் ஃபெரோசயனைடு — புருஷியன் நீல நிறம்) தருகிறது.",
        "ncert_key_point": "Lassaigne colours (NCERT must-memorize!): $\\text{Fe}_4[\\text{Fe(CN)}_6]_3 =$ Prussian Blue ($\\text{N}$ only); $[\\text{Fe(SCN)}]^{2+} =$ Blood Red (both $\\text{N}$ & $\\text{S}$ present); $[\\text{Fe(CN)}_5\\text{NOS}]^{4-} =$ Violet ($\\text{S}$ with nitroprusside)!",
        "trap_breakdown": {
            "A": "$\\text{Na}_4[\\text{Fe(CN)}_6]$ is the intermediate sodium hexacyanoferrate(II), not Prussian blue.",
            "C": "$[\\text{Fe(CN)}_5\\text{NOS}]^{4-}$ gives Violet colour in the sodium nitroprusside test for Sulphur.",
            "D": "$[\\text{Fe(SCN)}]^{2+}$ gives Blood Red colour when BOTH $\\text{N}$ and $\\text{S}$ are present together."
        },
        "videoTutorial": VIDEOS["chem_org"]
    },
]
