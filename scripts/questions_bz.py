#!/usr/bin/env python3
"""
20 Authentic NEET-UG Botany Questions (IDs 301-320) and
20 Authentic NEET-UG Zoology Questions (IDs 401-420)
Strictly aligned to NMC-rationalized Class 11 & 12 NCERT Biology and NEET 2019-2025 PYQs,
with full Bilingual (English + Tamil) stems, options, explanations, trap breakdowns, and video tutorials.
"""

BIO_VIDEOS = {
    "bot_ncert_tamil": {
        "title": "NCERT Biology Line-by-Line Botany Complete Revision (Tamil)",
        "channel": "Biology Simplified Tamil (Senthil Nathan)",
        "url": "https://www.youtube.com/@BiologySimplifiedTamil"
    },
    "bot_genetics": {
        "title": "Genetics & Molecular Basis of Inheritance NCERT Masterclass (Tamil)",
        "channel": "Biology Simplified Tamil (Senthil Nathan)",
        "url": "https://www.youtube.com/@BiologySimplifiedTamil"
    },
    "zoo_physio": {
        "title": "Human Physiology NCERT Line-by-Line & PYQs (Tamil)",
        "channel": "Biology Simplified Tamil (Senthil Nathan)",
        "url": "https://www.youtube.com/@BiologySimplifiedTamil"
    },
    "zoo_biotech": {
        "title": "Biotechnology Principles & Applications Complete NCERT (Tamil)",
        "channel": "Vedantu NEET Tamil",
        "url": "https://www.youtube.com/@Vedantu_NEET_Tamil"
    },
}

BOTANY_QUESTIONS = [
    {
        "id": 301,
        "subject": "Botany",
        "classLevel": "Class 11",
        "chapter": "Biological Classification",
        "ncertRef": "NCERT Class 11 Biology, Ch 2 — Kingdom Monera (Mycoplasma)",
        "pyqTag": "NEET High-Frequency NCERT Line PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Which of the following statements about Mycoplasma is INCORRECT according to NCERT?",
        "stem_ta": "NCERT பாடப்புத்தகத்தின்படி, மைக்கோபிளாஸ்மா (Mycoplasma) பற்றிய பின்வரும் கூற்றுகளில் எது தவறானது?",
        "choices": [
            {"letter": "A", "text_en": "They completely lack a cell wall", "text_ta": "இவற்றில் செல் சுவர் முற்றிலும் கிடையாது"},
            {"letter": "B", "text_en": "They are the smallest living cells known", "text_ta": "அறியப்பட்ட மிகச்சிறிய உயிருள்ள செல்கள் இவையே ஆகும்"},
            {"letter": "C", "text_en": "They cannot survive without oxygen", "text_ta": "ஆக்சிஜன் இன்றி இவற்றால் உயிர்வாழ முடியாது"},
            {"letter": "D", "text_en": "Many mycoplasmas are pathogenic in animals and plants", "text_ta": "பல மைக்கோபிளாஸ்மாக்கள் விலங்குகள் மற்றும் தாவரங்களில் நோயை உண்டாக்குகின்றன"}
        ],
        "correct": "C",
        "explanation_en": "Exact NCERT Class 11 Ch 2 line: 'The Mycoplasma are organisms that completely lack a cell wall. They are the smallest living cells known and CAN SURVIVE WITHOUT OXYGEN.' Hence 'cannot survive without oxygen' is INCORRECT!",
        "explanation_ta": "NCERT வகுப்பு 11 அத்தியாயம் 2-இன்படி: மைக்கோபிளாஸ்மாக்களில் செல் சுவர் இல்லை, மிகச்சிறிய உயிருள்ள செல்கள், மேலும் இவற்றால் ஆக்சிஜன் இன்றியும் உயிர்வாழ முடியும்! எனவே 'ஆக்சிஜன் இன்றி உயிர்வாழ முடியாது' என்பது தவறான கூற்றாகும்.",
        "ncert_key_point": "NTA loves flipping one word ('can survive without oxygen' -> 'cannot survive without oxygen')! Always circle INCORRECT/NOT in the stem.",
        "trap_breakdown": {
            "A": "True NCERT statement (hence resistant to penicillin, which targets cell wall).",
            "B": "True NCERT statement.",
            "D": "True NCERT statement (e.g., Witches' broom in plants, pleuropneumonia)."
        },
        "videoTutorial": BIO_VIDEOS["bot_ncert_tamil"]
    },
    {
        "id": 302,
        "subject": "Botany",
        "classLevel": "Class 11",
        "chapter": "Plant Kingdom",
        "ncertRef": "NCERT Class 11 Biology, Ch 3 — Algae (Red, Brown & Green Algae Hydrocolloids)",
        "pyqTag": "NEET 2022 / 2024 Official PYQ",
        "questionType": "Match the Column",
        "difficulty": "Medium",
        "stem_en": "Match List-I (Algal group / genus) with List-II (Stored food / Commercial product):\n(a) Rhodophyceae (Red algae) — (i) Mannitol & Laminarin\n(b) Phaeophyceae (Brown algae) — (ii) Floridean starch\n(c) Gelidium & Gracilaria — (iii) Algin\n(d) Brown marine algae — (iv) Agar\nChoose the correct match:",
        "stem_ta": "பட்டியல்-I உடன் பட்டியல்-II ஐப் பொருத்துக:\n(a) ரோடோஃபைசி (சிவப்புப் பாசிகள்) — (i) மானிட்டால் & லாமினாரின்\n(b) ஃபியோஃபைசி (பழுப்புப் பாசிகள்) — (ii) புளோரிடியன் ஸ்டார்ச்\n(c) ஜெலிடியம் & கிராசிலேரியா — (iii) அல்ஜின் (Algin)\n(d) கடல் பழுப்புப் பாசிகள் — (iv) அகார் (Agar)\nசரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        "choices": [
            {"letter": "A", "text_en": "(a)-(ii), (b)-(i), (c)-(iv), (d)-(iii)", "text_ta": "(a)-(ii), (b)-(i), (c)-(iv), (d)-(iii)"},
            {"letter": "B", "text_en": "(a)-(i), (b)-(ii), (c)-(iv), (d)-(iii)", "text_ta": "(a)-(i), (b)-(ii), (c)-(iv), (d)-(iii)"},
            {"letter": "C", "text_en": "(a)-(ii), (b)-(i), (c)-(iii), (d)-(iv)", "text_ta": "(a)-(ii), (b)-(i), (c)-(iii), (d)-(iv)"},
            {"letter": "D", "text_en": "(a)-(iv), (b)-(iii), (c)-(ii), (d)-(i)", "text_ta": "(a)-(iv), (b)-(iii), (c)-(ii), (d)-(i)"}
        ],
        "correct": "A",
        "explanation_en": "Rhodophyceae store Floridean starch (structurally very similar to amylopectin and glycogen). Phaeophyceae store Laminarin and Mannitol. Agar is obtained from red algae Gelidium and Gracilaria. Hydrocolloid Algin is obtained from brown algae (Carrageen is from red algae).",
        "explanation_ta": "சிவப்புப் பாசிகள் (ரோடோஃபைசி) சேமிப்பு உணவு புளோரிடியன் ஸ்டார்ச்; பழுப்புப் பாசிகள் (ஃபியோஃபைசி) மானிட்டால் & லாமினாரின்; ஜெலிடியம் & கிராசிலேரியாவிலிருந்து அகார் கிடைக்கிறது; பழுப்புப் பாசிகளிலிருந்து அல்ஜின் கிடைக்கிறது.",
        "ncert_key_point": "Algin = Brown algae; Carrageen & Agar (Gelidium, Gracilaria) = Red algae; Chlorella = unicellular protein-rich green alga.",
        "trap_breakdown": {
            "B": "Swaps stored food of red and brown algae.",
            "C": "Swaps Agar and Algin sources.",
            "D": "Scrambles stored food with hydrocolloids."
        },
        "videoTutorial": BIO_VIDEOS["bot_ncert_tamil"]
    },
    {
        "id": 303,
        "subject": "Botany",
        "classLevel": "Class 11",
        "chapter": "Morphology of Flowering Plants",
        "ncertRef": "NCERT Class 11 Biology, Ch 5 — Placentation in Flowering Plants",
        "pyqTag": "NEET 2023 / 2024 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Axile placentation is observed in which of the following sets of plants?",
        "stem_ta": "பின்வரும் எந்தத் தாவரத் தொகுப்பில் அச்சு சூலொட்டுமுறை (Axile placentation) காணப்படுகிறது?",
        "choices": [
            {"letter": "A", "text_en": "Mustard and Argemone", "text_ta": "கடுகு மற்றும் ஆர்ஜிமோன்"},
            {"letter": "B", "text_en": "Dianthus and Primrose", "text_ta": "டையான்தஸ் மற்றும் பிரிம்ரோஸ்"},
            {"letter": "C", "text_en": "China rose, Tomato, and Lemon", "text_ta": "செம்பருத்தி (China rose), தக்காளி மற்றும் எலுமிச்சை"},
            {"letter": "D", "text_en": "Sunflower and Marigold", "text_ta": "சூரியகாந்தி மற்றும் சாமந்தி (Marigold)"}
        ],
        "correct": "C",
        "explanation_en": "NCERT Morphology examples of placentation: Marginal = Pea; Axile = China rose, Tomato, Lemon; Parietal = Mustard, Argemone; Free central = Dianthus, Primrose; Basal = Sunflower, Marigold.",
        "explanation_ta": "NCERT எடுத்துக்காட்டுகள்: விளிம்பு சூலொட்டுமுறை = பட்டாணி; அச்சு சூலொட்டுமுறை (Axile) = செம்பருத்தி, தக்காளி, எலுமிச்சை; சுவர் = கடுகு, ஆர்ஜிமோன்; தனித்த மைய = டையான்தஸ், பிரிம்ரோஸ்; அடித்தள = சூரியகாந்தி, சாமந்தி.",
        "ncert_key_point": "Every Morphology example in NCERT Class 11 Ch 5 is a guaranteed NEET question — memorize the exact NCERT trios!",
        "trap_breakdown": {
            "A": "Mustard and Argemone show Parietal placentation (with replum false septum).",
            "B": "Dianthus and Primrose show Free-central placentation.",
            "D": "Sunflower and Marigold show Basal placentation."
        },
        "videoTutorial": BIO_VIDEOS["bot_ncert_tamil"]
    },
    {
        "id": 304,
        "subject": "Botany",
        "classLevel": "Class 11",
        "chapter": "Anatomy of Flowering Plants",
        "ncertRef": "NCERT Class 11 Biology, Ch 6 — Vascular Bundles & Casparian Strips",
        "pyqTag": "NEET Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "The tangential as well as radial walls of the endodermal cells in dicot/monocot roots have a deposition of water-impermeable, waxy material in the form of Casparian strips. This waxy material is:",
        "stem_ta": "வேர்களின் அகத்தோல் (endodermis) செல்களின் ஆர மற்றும் தொடுகோட்டுச் சுவர்களில் காஸ்பேரியன் பட்டைகளாகப் படிந்துள்ள நீர் புகாத மெழுகுப் பொருள் எது?",
        "choices": [
            {"letter": "A", "text_en": "Lignin", "text_ta": "லிக்னின் (Lignin)"},
            {"letter": "B", "text_en": "Suberin", "text_ta": "சுபெரின் (Suberin)"},
            {"letter": "C", "text_en": "Pectin", "text_ta": "பெக்டின் (Pectin)"},
            {"letter": "D", "text_en": "Chitin", "text_ta": "கைட்டின் (Chitin)"}
        ],
        "correct": "B",
        "explanation_en": "Exact NCERT Class 11 Anatomy & Plant Transport fact: Casparian strips in root endodermis are made of the waxy, water-impermeable substance SUBERIN, forcing water from apoplast into the symplast pathway across plasma membranes.",
        "explanation_ta": "வேரின் அகத்தோலில் உள்ள காஸ்பேரியன் பட்டைகள் (Casparian strips) 'சுபெரின்' (Suberin) என்ற நீர் புகாத மெழுகுப் பொருளால் ஆனவை.",
        "ncert_key_point": "Casparian strips = Suberin (Root Endodermis); Sclerenchyma/Xylem = Lignin; Collenchyma = Cellulose + Hemicellulose + Pectin; Fungal wall = Chitin.",
        "trap_breakdown": {
            "A": "Lignin thickens xylem vessels and sclerenchyma fibres, though sometimes co-mentioned in older texts — NCERT explicitly specifies waxy SUBERIN!",
            "C": "Pectin is hydrophilic and found in collenchyma/middle lamella.",
            "D": "Chitin forms fungal cell walls and arthropod exoskeletons."
        },
        "videoTutorial": BIO_VIDEOS["bot_ncert_tamil"]
    },
    {
        "id": 305,
        "subject": "Botany",
        "classLevel": "Class 11",
        "chapter": "Cell: The Unit of Life",
        "ncertRef": "NCERT Class 11 Biology, Ch 8 — Endomembrane System",
        "pyqTag": "NEET 2023 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Which of the following cellular organelles are NOT considered part of the endomembrane system because their functions are not coordinated with ER, Golgi, lysosomes, and vacuoles?",
        "stem_ta": "பின்வரும் செல் நுண்ணுறுப்புகளில் எவை அகச்சவ்வு அமைப்பின் (Endomembrane system) பகுதியாகக் கருதப்படுவதில்லை?",
        "choices": [
            {"letter": "A", "text_en": "Endoplasmic reticulum and Golgi apparatus", "text_ta": "எண்டோபிளாச வலைப்பின்னல் மற்றும் கோல்கை உறுப்பு"},
            {"letter": "B", "text_en": "Lysosomes and Vacuoles", "text_ta": "லைசோசோம்கள் மற்றும் நுண்குமிழ்கள் (Vacuoles)"},
            {"letter": "C", "text_en": "Mitochondria, Chloroplasts, and Peroxisomes", "text_ta": "மைட்டோகாண்ட்ரியா, பசுங்கணிகம் மற்றும் பெராக்சிசோம்கள்"},
            {"letter": "D", "text_en": "Rough ER and Smooth ER", "text_ta": "சொரசொரப்பான ER மற்றும் வழவழப்பான ER"}
        ],
        "correct": "C",
        "explanation_en": "Exact NCERT Class 11 Ch 8 line: The endomembrane system includes ONLY Endoplasmic Reticulum (ER), Golgi complex, Lysosomes, and Vacuoles (mnemonic: GERL/EGLV). Mitochondria, Chloroplasts, and Peroxisomes are EXCLUDED because their functions are not coordinated with the above components!",
        "explanation_ta": "அகச்சவ்வு அமைப்பில் ER, கோல்கை உறுப்பு, லைசோசோம் மற்றும் நுண்குமிழ்கள் மட்டுமே அடங்கும். மைட்டோகாண்ட்ரியா, பசுங்கணிகம் மற்றும் பெராக்சிசோம்கள் இதில் அடங்காது!",
        "ncert_key_point": "Endomembrane = ER + Golgi + Lysosome + Vacuole ONLY. Peroxisome looks like a vesicle like lysosome — don't fall for the trap!",
        "trap_breakdown": {
            "A": "Core components of the endomembrane system.",
            "B": "Core components of the endomembrane system.",
            "D": "Subtypes of ER, part of the endomembrane system."
        },
        "videoTutorial": BIO_VIDEOS["bot_ncert_tamil"]
    },
    {
        "id": 306,
        "subject": "Botany",
        "classLevel": "Class 11",
        "chapter": "Cell Cycle and Cell Division",
        "ncertRef": "NCERT Class 11 Biology, Ch 10 — Prophase I of Meiosis I",
        "pyqTag": "NEET 2023 / 2024 Mandatory PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "During Meiosis I, the appearance of recombination nodules and crossing over catalyzed by the enzyme recombinase occurs during which sub-stage of Prophase I?",
        "stem_ta": "மியாசிஸ் I-இன் புரோஃபேஸ் I-இல், மறுசேர்க்கை முடிச்சுகள் தோன்றுவதும் ரீகாம்பினேஸ் நொதியால் குறுக்கே கலத்தல் (crossing over) நிகழ்வதும் எந்தத் துணை நிலையில் நடைபெறுகிறது?",
        "choices": [
            {"letter": "A", "text_en": "Zygotene", "text_ta": "சைக்கோட்டீன் (Zygotene)"},
            {"letter": "B", "text_en": "Pachytene", "text_ta": "பாக்கிட்டீன் (Pachytene)"},
            {"letter": "C", "text_en": "Diplotene", "text_ta": "டிப்ளோட்டீன் (Diplotene)"},
            {"letter": "D", "text_en": "Diakinesis", "text_ta": "டயாகைனசிஸ் (Diakinesis)"}
        ],
        "correct": "B",
        "explanation_en": "Prophase I sequence (L-Z-P-D-D): Leptotene (compaction) -> Zygotene (synapsis, synaptonemal complex, bivalent) -> Pachytene (tetrad clearly visible, recombination nodules, crossing over via recombinase!) -> Diplotene (dissolution of synaptonemal complex, X-shaped chiasmata) -> Diakinesis (terminalisation of chiasmata).",
        "explanation_ta": "புரோஃபேஸ் I வரிசையில்: சைக்கோட்டீனில் இணை சேர்தல் (synapsis); பாக்கிட்டீனில் (Pachytene) மறுசேர்க்கை முடிச்சுகள் மற்றும் ரீகாம்பினேஸ் நொதியால் குறுக்கே கலத்தல் (crossing over); டிப்ளோட்டீனில் கயாஸ்மாட்டா; டயாகைனசிஸில் கயாஸ்மா முடிவுறுதல் நடைபெறும்.",
        "ncert_key_point": "Synapsis = Zygotene; Crossing over + Recombinase = Pachytene; Chiasmata X-shape = Diplotene; Terminalisation = Diakinesis.",
        "trap_breakdown": {
            "A": "Zygotene forms synaptonemal complex and bivalents, BEFORE crossing over.",
            "C": "Diplotene shows X-shaped chiasmata AFTER crossing over has completed in Pachytene.",
            "D": "Diakinesis shows terminalisation of chiasmata."
        },
        "videoTutorial": BIO_VIDEOS["bot_ncert_tamil"]
    },
    {
        "id": 307,
        "subject": "Botany",
        "classLevel": "Class 11",
        "chapter": "Cell Cycle and Cell Division",
        "ncertRef": "NCERT Class 11 Biology, Ch 10 — S Phase (DNA Replication vs Chromosome Number)",
        "pyqTag": "NEET Classic Numerical Trap",
        "questionType": "Numerical MCQ",
        "difficulty": "Medium",
        "stem_en": "A diploid somatic cell has 2n = 16 chromosomes and DNA content = 2C at G1 phase. What will be its chromosome number and DNA content respectively at G2 phase (after S phase)?",
        "stem_ta": "இருமடிய உடல் செல் ஒன்றில் G1 நிலையில் குரோமோசோம் எண்ணிக்கை 2n = 16 மற்றும் DNA அளவு = 2C உள்ளது. S நிலைக்குப் பிறகு G2 நிலையில் அதன் குரோமோசோம் எண்ணிக்கை மற்றும் DNA அளவு முறையே என்னவாக இருக்கும்?",
        "choices": [
            {"letter": "A", "text_en": "32 chromosomes and 4C DNA", "text_ta": "32 குரோமோசோம்கள் மற்றும் 4C DNA"},
            {"letter": "B", "text_en": "16 chromosomes and 4C DNA", "text_ta": "16 குரோமோசோம்கள் மற்றும் 4C DNA"},
            {"letter": "C", "text_en": "16 chromosomes and 2C DNA", "text_ta": "16 குரோமோசோம்கள் மற்றும் 2C DNA"},
            {"letter": "D", "text_en": "32 chromosomes and 2C DNA", "text_ta": "32 குரோமோசோம்கள் மற்றும் 2C DNA"}
        ],
        "correct": "B",
        "explanation_en": "Exact NCERT Class 11 Ch 10 emphasis: During S (Synthesis) phase, DNA content DOUBLES from 2C to 4C, BUT there is NO increase in chromosome number! If the cell had 2n = 16 chromosomes at G1, it STILL has 2n = 16 chromosomes at S and G2 (each chromosome now consists of 2 sister chromatids joined at 1 centromere).",
        "explanation_ta": "NCERT-இன் மிக முக்கிய விதி: S நிலையில் DNA அளவு 2C-யிலிருந்து 4C ஆக இரட்டிப்பாகும்; ஆனால் குரோமோசோம் எண்ணிக்கை மாறாது (2n = 16 ஆகவே இருக்கும்)!",
        "ncert_key_point": "Count centromeres to count chromosomes! S phase doubles DNA (2C -> 4C), NOT chromosome number (2n stays 2n).",
        "trap_breakdown": {
            "A": "32 chromosomes falls right into the #1 NCERT trap of doubling 2n during S phase!",
            "C": "Forgets that DNA replicated in S phase.",
            "D": "Swaps chromosome number and DNA content behaviour."
        },
        "videoTutorial": BIO_VIDEOS["bot_ncert_tamil"]
    },
    {
        "id": 308,
        "subject": "Botany",
        "classLevel": "Class 11",
        "chapter": "Photosynthesis in Higher Plants",
        "ncertRef": "NCERT Class 11 Biology, Ch 11 — C4 Pathway (Hatch and Slack Pathway)",
        "pyqTag": "NEET 2023 / 2024 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "In C4 plants such as maize and sugarcane, the primary CO2 acceptor in mesophyll cells and the first stable C4 acid formed are respectively:",
        "stem_ta": "மக்காச்சோளம் மற்றும் கரும்பு போன்ற C4 தாவரங்களின் இலை நடுத்திசு (mesophyll) செல்களில் முதன்மை CO2 ஏற்பி மற்றும் உருவாகும் முதல் நிலையான C4 அமிலம் முறையே:",
        "choices": [
            {"letter": "A", "text_en": "RuBP (5C) and 3-PGA (3C)", "text_ta": "RuBP (5C) மற்றும் 3-PGA (3C)"},
            {"letter": "B", "text_en": "PEP (3C) and Oxaloacetic acid (OAA, 4C)", "text_ta": "PEP (3C) மற்றும் ஆக்சலோ அசிட்டிக் அமிலம் (OAA, 4C)"},
            {"letter": "C", "text_en": "PEP (3C) and Malic acid (4C)", "text_ta": "PEP (3C) மற்றும் மாலிக் அமிலம் (4C)"},
            {"letter": "D", "text_en": "RuBP (5C) and Oxaloacetic acid (OAA, 4C)", "text_ta": "RuBP (5C) மற்றும் ஆக்சலோ அசிட்டிக் அமிலம் (OAA, 4C)"}
        ],
        "correct": "B",
        "explanation_en": "In C4 plants (Kranz anatomy), mesophyll cells lack RuBisCO and contain PEP carboxylase (PEPcase). The primary CO2 acceptor is a 3-carbon molecule, Phosphoenolpyruvate (PEP), forming the 4-carbon Oxaloacetic acid (OAA) as the first stable product! RuBisCO is present only in bundle sheath cells.",
        "explanation_ta": "C4 தாவரங்களின் மீசோஃபில் செல்களில் முதன்மை CO2 ஏற்பி 3-கார்பன் கொண்ட பாஸ்போஈனால்பைருவேட் (PEP) ஆகும்; PEP கார்பாக்சிலேஸ் நொதியால் உருவாகும் முதல் நிலையான விளைபொருள் ஆக்சலோ அசிட்டிக் அமிலம் (OAA, 4C) ஆகும்.",
        "ncert_key_point": "C3 primary acceptor = 5-carbon RuBP; C4 primary acceptor = 3-carbon PEP (NOT 4-carbon!).",
        "trap_breakdown": {
            "A": "RuBP and 3-PGA are for the C3 (Calvin) cycle.",
            "C": "Malic/aspartic acid is formed AFTER OAA for transport to bundle sheath cells.",
            "D": "Mesophyll cells of C4 plants completely lack RuBisCO / RuBP fixation."
        },
        "videoTutorial": BIO_VIDEOS["bot_ncert_tamil"]
    },
    {
        "id": 309,
        "subject": "Botany",
        "classLevel": "Class 11",
        "chapter": "Photosynthesis in Higher Plants",
        "ncertRef": "NCERT Class 11 Biology, Ch 11 — ATP & NADPH Stoichiometry in C3 vs C4",
        "pyqTag": "NEET Official PYQ",
        "questionType": "Numerical MCQ",
        "difficulty": "Medium",
        "stem_en": "To synthesize ONE molecule of glucose (C6H12O6) via the Calvin cycle in a C3 plant, how many molecules of CO2, ATP, and NADPH are required respectively?",
        "stem_ta": "C3 தாவரத்தில் கால்வின் சுழற்சியின் வழியே ஒரு குளுக்கோஸ் (C6H12O6) மூலக்கூறை உருவாக்கத் தேவைப்படும் CO2, ATP மற்றும் NADPH மூலக்கூறுகளின் எண்ணிக்கை முறையே:",
        "choices": [
            {"letter": "A", "text_en": "6 CO2, 18 ATP, 12 NADPH", "text_ta": "6 CO2, 18 ATP, 12 NADPH"},
            {"letter": "B", "text_en": "6 CO2, 30 ATP, 12 NADPH", "text_ta": "6 CO2, 30 ATP, 12 NADPH"},
            {"letter": "C", "text_en": "6 CO2, 12 ATP, 18 NADPH", "text_ta": "6 CO2, 12 ATP, 18 NADPH"},
            {"letter": "D", "text_en": "1 CO2, 3 ATP, 2 NADPH", "text_ta": "1 CO2, 3 ATP, 2 NADPH"}
        ],
        "correct": "A",
        "explanation_en": "Per CO2 fixed in C3 Calvin cycle: 3 ATP (2 in reduction + 1 in regeneration) and 2 NADPH are used. For 1 glucose (6 carbons = 6 turns of Calvin cycle): 6 CO2, 6 * 3 = 18 ATP, and 6 * 2 = 12 NADPH! (In C4 plants, 2 extra ATP per CO2 are used for PEP regeneration -> 30 ATP + 12 NADPH).",
        "explanation_ta": "C3 சுழற்சியில் ஒரு CO2 நிலைநிறுத்த 3 ATP மற்றும் 2 NADPH தேவை. எனவே 1 குளுக்கோஸ் உருவாக்க (6 சுற்றுகள்): 6 CO2, 18 ATP மற்றும் 12 NADPH தேவை! (C4 தாவரத்தில் 30 ATP, 12 NADPH தேவை).",
        "ncert_key_point": "1 Glucose in C3 => 18 ATP, 12 NADPH. 1 Glucose in C4 => 30 ATP, 12 NADPH.",
        "trap_breakdown": {
            "B": "30 ATP, 12 NADPH is for C4 plants, not C3 plants!",
            "C": "Swaps ATP (18) and NADPH (12).",
            "D": "1 CO2, 3 ATP, 2 NADPH fixes only ONE carbon, not one 6-carbon glucose molecule!"
        },
        "videoTutorial": BIO_VIDEOS["bot_ncert_tamil"]
    },
    {
        "id": 310,
        "subject": "Botany",
        "classLevel": "Class 11",
        "chapter": "Respiration in Plants",
        "ncertRef": "NCERT Class 11 Biology, Ch 12 — Tricarboxylic Acid (Krebs) Cycle & ETS",
        "pyqTag": "NEET 2022 / 2024 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "In the mitochondrial Electron Transport System (ETS), Complex IV refers to:",
        "stem_ta": "மைட்டோகாண்ட்ரியாவின் எலக்ட்ரான் கடத்து அமைப்பில் (ETS), தொகுப்பு IV (Complex IV) எதைக் குறிக்கிறது?",
        "choices": [
            {"letter": "A", "text_en": "NADH dehydrogenase", "text_ta": "NADH டிஹைட்ரோஜினேஸ்"},
            {"letter": "B", "text_en": "Succinate dehydrogenase (FADH2)", "text_ta": "சக்சினேட் டிஹைட்ரோஜினேஸ்"},
            {"letter": "C", "text_en": "Cytochrome bc1 complex", "text_ta": "சைட்டோகுரோம் bc1 தொகுப்பு"},
            {"letter": "D", "text_en": "Cytochrome c oxidase complex (containing cytochromes a and a3, and 2 copper centres)", "text_ta": "சைட்டோகுரோம் c ஆக்சிடேஸ் தொகுப்பு (சைட்டோகுரோம் a, a3 மற்றும் 2 தாமிர மையங்கள் கொண்டது)"}
        ],
        "correct": "D",
        "explanation_en": "Exact NCERT Class 11 Ch 12 complexes: Complex I = NADH dehydrogenase; Complex II = Succinate dehydrogenase; Complex III = Cytochrome bc1; Complex IV = Cytochrome c oxidase (cytochromes a & a3 + two copper centres); Complex V = ATP synthase (F0-F1).",
        "explanation_ta": "NCERT ETS தொகுப்புகள்: Complex I = NADH டிஹைட்ரோஜினேஸ்; Complex II = சக்சினேட் டிஹைட்ரோஜினேஸ்; Complex III = சைட்டோகுரோம் bc1; Complex IV = சைட்டோகுரோம் c ஆக்சிடேஸ் (a, a3 மற்றும் 2 Cu மையங்கள்); Complex V = ATP சிந்தேஸ்.",
        "ncert_key_point": "Memorize Complex I to V in exact order + mobile electron carrier Cytochrome c (outer surface of inner membrane between III and IV)!",
        "trap_breakdown": {
            "A": "Complex I.",
            "B": "Complex II.",
            "C": "Complex III."
        },
        "videoTutorial": BIO_VIDEOS["bot_ncert_tamil"]
    },
    {
        "id": 311,
        "subject": "Botany",
        "classLevel": "Class 11",
        "chapter": "Plant Growth and Development",
        "ncertRef": "NCERT Class 11 Biology, Ch 13 — Plant Growth Regulators (Gibberellins & Ethylene)",
        "pyqTag": "NEET 2023 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Spraying sugarcane crop with which plant hormone increases the length of the stem, thus increasing sugarcane yield by as much as 20 tonnes per acre?",
        "stem_ta": "கரும்புப் பயிரின் மீது எந்தத் தாவர ஹார்மோனைத் தெளிப்பதன் மூலம் தண்டின் நீளம் அதிகரித்து, ஏக்கருக்கு 20 டன் வரை விளைச்சல் அதிகரிக்கிறது?",
        "choices": [
            {"letter": "A", "text_en": "Auxin", "text_ta": "ஆக்சின் (Auxin)"},
            {"letter": "B", "text_en": "Gibberellins", "text_ta": "ஜிப்ரல்லின்கள் (Gibberellins)"},
            {"letter": "C", "text_en": "Cytokinin", "text_ta": "சைட்டோகைனின் (Cytokinin)"},
            {"letter": "D", "text_en": "Abscisic acid (ABA)", "text_ta": "அப்சிசிக் அமிலம் (ABA)"}
        ],
        "correct": "B",
        "explanation_en": "Verbatim NCERT Class 11 Ch 13 line (asked directly in NEET 2023!): Sugarcane stores carbohydrate as sugar in stems; spraying sugarcane crop with GIBBERELLINS increases internode/stem length, increasing yield by up to 20 tonnes per acre! Gibberellins also cause bolting in beet and cabbages.",
        "explanation_ta": "NCERT வகுப்பு 11 அத்தியாயம் 13-இல் உள்ள நேரடி வரி (NEET 2023 வினா!): கரும்புப் பயிரில் ஜிப்ரல்லின்களைத் தெளிக்கும்போது தண்டின் நீளம் அதிகரித்து ஏக்கருக்கு 20 டன் வரை மகசூல் உயர்கிறது!",
        "ncert_key_point": "Gibberellin keywords: Sugarcane +20 tonnes/acre, Bolting (beet/cabbage), Malting speedup in brewing, Early seed production in juvenile conifers.",
        "trap_breakdown": {
            "A": "Auxin promotes rooting in stem cuttings, flowering in pineapples, and 2,4-D kills dicot weeds.",
            "C": "Cytokinin overcomes apical dominance and delays leaf senescence (Richmond-Lang effect).",
            "D": "ABA is the stress hormone causing stomatal closure and seed dormancy."
        },
        "videoTutorial": BIO_VIDEOS["bot_ncert_tamil"]
    },
    {
        "id": 312,
        "subject": "Botany",
        "classLevel": "Class 12",
        "chapter": "Sexual Reproduction in Flowering Plants",
        "ncertRef": "NCERT Class 12 Biology, Ch 1 — Polygonum Embryo Sac & Double Fertilisation",
        "pyqTag": "NEET Classic NCERT Line PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "A typical mature angiosperm embryo sac (Polygonum type) at maturity is:",
        "stem_ta": "முதிர்ச்சியடைந்த பூக்கும் தாவரத்தின் (ஆஞ்சியோஸ்பெர்ம்) கருப்பை (Embryo sac) எத்தனை உட்கருக்களையும் எத்தனை செல்களையும் கொண்டது?",
        "choices": [
            {"letter": "A", "text_en": "8-nucleate and 8-celled", "text_ta": "8-உட்கருக்கள் மற்றும் 8-செல்கள் கொண்டது"},
            {"letter": "B", "text_en": "8-nucleate and 7-celled", "text_ta": "8-உட்கருக்கள் மற்றும் 7-செல்கள் கொண்டது"},
            {"letter": "C", "text_en": "7-nucleate and 8-celled", "text_ta": "7-உட்கருக்கள் மற்றும் 8-செல்கள் கொண்டது"},
            {"letter": "D", "text_en": "7-nucleate and 7-celled", "text_ta": "7-உட்கருக்கள் மற்றும் 7-செல்கள் கொண்டது"}
        ],
        "correct": "B",
        "explanation_en": "Exact NCERT Class 12 Ch 1 line: Mature embryo sac has 3 antipodal cells (3 nuclei) + 2 synergids + 1 egg cell (egg apparatus, 3 nuclei) + 1 large central cell containing 2 polar nuclei = 7 cells and 8 nuclei!",
        "explanation_ta": "முதிர்ந்த கருப்பையில் 3 எதிர்த்துருவ செல்கள் + 2 சினர்ஜிட்கள் + 1 அண்ட செல் + 2 துருவ உட்கருக்களைக் கொண்ட 1 பெரிய மைய செல் என மொத்தம் 8-உட்கருக்கள் மற்றும் 7-செல்கள் (8-nucleate, 7-celled) உள்ளன!",
        "ncert_key_point": "Pay attention to word order: 8-nucleate and 7-celled (NOT 7-nucleate and 8-celled!).",
        "trap_breakdown": {
            "A": "Forgets that the two polar nuclei share a single large central cell.",
            "C": "Swaps the numbers 7 and 8 — a classic speed-reading trap!",
            "D": "Assumes polar nuclei have already fused before fertilisation."
        },
        "videoTutorial": BIO_VIDEOS["bot_ncert_tamil"]
    },
    {
        "id": 313,
        "subject": "Botany",
        "classLevel": "Class 12",
        "chapter": "Principles of Inheritance and Variation",
        "ncertRef": "NCERT Class 12 Biology, Ch 4 — Incomplete Dominance & Test Cross",
        "pyqTag": "NEET Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "In Antirrhinum (Snapdragon / Dog flower), when true-breeding red-flowered (RR) and white-flowered (rr) plants are crossed, F1 is pink (Rr). On selfing F1, the phenotypic and genotypic ratios in F2 generation are:",
        "stem_ta": "ஆன்டிரைனம் (ஸ்னாப்டிராகன்) தாவரத்தில் தூய சிவப்பு (RR) மற்றும் வெள்ளை (rr) மலர் கொண்ட தாவரங்களைக் கலப்பு செய்யும்போது F1 இளஞ்சிவப்பு (Rr) ஆகிறது. F2 சந்ததியில் புறத்தோற்ற மற்றும் மரபணு விகிதங்கள்:",
        "choices": [
            {"letter": "A", "text_en": "Phenotypic 3 : 1, Genotypic 1 : 2 : 1", "text_ta": "புறத்தோற்றம் 3 : 1, மரபணுவாக்கம் 1 : 2 : 1"},
            {"letter": "B", "text_en": "Both Phenotypic and Genotypic ratios are identical: 1 : 2 : 1", "text_ta": "புறத்தோற்ற மற்றும் மரபணு விகிதங்கள் இரண்டும் ஒன்றே: 1 : 2 : 1"},
            {"letter": "C", "text_en": "Both Phenotypic and Genotypic ratios are 3 : 1", "text_ta": "இரண்டு விகிதங்களும் 3 : 1"},
            {"letter": "D", "text_en": "Phenotypic 9 : 3 : 3 : 1, Genotypic 1 : 2 : 1", "text_ta": "புறத்தோற்றம் 9 : 3 : 3 : 1, மரபணுவாக்கம் 1 : 2 : 1"}
        ],
        "correct": "B",
        "explanation_en": "Snapdragon flower colour shows Incomplete Dominance: F2 produces 1 Red (RR) : 2 Pink (Rr) : 1 White (rr). Therefore, BOTH phenotypic ratio and genotypic ratio are 1 : 2 : 1!",
        "explanation_ta": "ஆன்டிரைனம் மலர் நிறம் முழுமையற்ற ஓங்குத்தன்மைக்கு (Incomplete dominance) எடுத்துக்காட்டு. F2-இல் 1 சிவப்பு (RR) : 2 இளஞ்சிவப்பு (Rr) : 1 வெள்ளை (rr) கிடைப்பதால் புறத்தோற்ற மற்றும் மரபணு விகிதங்கள் இரண்டும் 1 : 2 : 1 ஆகும்!",
        "ncert_key_point": "Identical 1 : 2 : 1 phenotypic & genotypic F2 ratio is the hallmark of BOTH Incomplete Dominance (Snapdragon) and Codominance (MN/ABO IAIB).",
        "trap_breakdown": {
            "A": "3 : 1 phenotypic ratio is complete Mendelian dominance (garden pea).",
            "C": "Genotypic ratio of monohybrid selfing is never 3 : 1.",
            "D": "9 : 3 : 3 : 1 is dihybrid cross."
        },
        "videoTutorial": BIO_VIDEOS["bot_genetics"]
    },
    {
        "id": 314,
        "subject": "Botany",
        "classLevel": "Class 12",
        "chapter": "Principles of Inheritance and Variation",
        "ncertRef": "NCERT Class 12 Biology, Ch 4 — Mendelian & Chromosomal Disorders",
        "pyqTag": "NEET 2023 / 2024 Official PYQ",
        "questionType": "Assertion-Reason",
        "difficulty": "Medium",
        "stem_en": "Assertion (A): Sickle-cell anaemia is an autosome-linked recessive trait caused by substitution of Glutamic acid (Glu) by Valine (Val) at the sixth position of the beta-globin chain of haemoglobin.\nReason (R): It results from a single base substitution at the sixth codon of the beta-globin gene from GAG to GUG.\nChoose the correct option:",
        "stem_ta": "கூற்று (A): கதிர்அரிவாள் இரத்த சோகை (Sickle-cell anaemia) என்பது ஹீமோகுளோபினின் பீட்டா-குளோபின் சங்கிலியின் 6-வது இடத்தில் குளுட்டாமிக் அமிலத்திற்குப் (Glu) பதிலாக வாலின் (Val) பதிலீடு செய்யப்படுவதால் ஏற்படும் உடற்குரோமோசோம் ஒடுங்குப் பண்பாகும்.\nகாரணம் (R): பீட்டா-குளோபின் மரபணுவின் 6-வது கோடானில் GAG என்பது GUG என ஒற்றை காரப் பதிலீடு அடைவதால் இது நிகழ்கிறது.\nசரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        "choices": [
            {"letter": "A", "text_en": "Both A and R are true, and R is the correct explanation of A", "text_ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A-க்கான சரியான விளக்கமாகும்"},
            {"letter": "B", "text_en": "Both A and R are true, but R is NOT the correct explanation of A", "text_ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A-க்கான சரியான விளக்கமல்ல"},
            {"letter": "C", "text_en": "A is true, but R is false", "text_ta": "A சரி, ஆனால் R தவறு"},
            {"letter": "D", "text_en": "A is false, but R is true", "text_ta": "A தவறு, ஆனால் R சரி"}
        ],
        "correct": "A",
        "explanation_en": "Exact NCERT Class 12 Ch 4 Genetics mechanism: Point mutation in the 6th codon of beta-globin mRNA from GAG (codes for Glutamic acid) to GUG (codes for Valine) directly causes the Glu -> Val substitution at position 6, leading to Hb^S polymerisation under low O2 tension. Both A and R are true and R directly explains A!",
        "explanation_ta": "பீட்டா-குளோபின் மரபணுவின் 6-வது கோடான் GAG (குளுட்டாமிக் அமிலம்) இலிருந்து GUG (வாலின்) ஆக புள்ளி சடுதிமாற்றம் அடைவதாலேயே 6-வது இடத்தில் Glu -> Val மாற்றம் ஏற்பட்டு கதிர்அரிவாள் இரத்த சோகை உண்டாகிறது. எனவே A, R இரண்டும் சரி மற்றும் R சரியான விளக்கமாகும்.",
        "ncert_key_point": "Check carefully in NEET: Glu replaced by Val (GAG -> GUG) on beta-globin 6th position (chromosome 11) — NTA often swaps Val and Glu to trap students!",
        "trap_breakdown": {
            "B": "R is the exact molecular cause of A, so it IS the correct explanation.",
            "C": "GAG -> GUG is accurate.",
            "D": "Autosomal recessive & Glu -> Val at 6th position are accurate."
        },
        "videoTutorial": BIO_VIDEOS["bot_genetics"]
    },
    {
        "id": 315,
        "subject": "Botany",
        "classLevel": "Class 12",
        "chapter": "Molecular Basis of Inheritance",
        "ncertRef": "NCERT Class 12 Biology, Ch 5 — Packaging of DNA Helix & Chargaff's Rule",
        "pyqTag": "NEET Official PYQ",
        "questionType": "Numerical MCQ",
        "difficulty": "Easy",
        "stem_en": "In a double-stranded B-DNA molecule, if Cytosine makes up 20% of the total nitrogenous bases, what is the percentage of Adenine?",
        "stem_ta": "இரட்டை இழை B-DNA மூலக்கூறு ஒன்றில் சைட்டோசின் (Cytosine) அளவு 20% எனில், அடினைனின் (Adenine) சதவீதம் என்ன?",
        "choices": [
            {"letter": "A", "text_en": "20%", "text_ta": "20%"},
            {"letter": "B", "text_en": "30%", "text_ta": "30%"},
            {"letter": "C", "text_en": "40%", "text_ta": "40%"},
            {"letter": "D", "text_en": "60%", "text_ta": "60%"}
        ],
        "correct": "B",
        "explanation_en": "By Chargaff's rule for dsDNA: %G = %C = 20%, so %G + %C = 40%. Remaining bases %A + %T = 100% - 40% = 60%. Since %A = %T, %A = 60% / 2 = 30%.",
        "explanation_ta": "சார்காஃப் விதியின்படி dsDNA-வில்: %C = %G = 20% => %C + %G = 40%. எனவே %A + %T = 100% - 40% = 60%. %A = %T என்பதால் %A = 30%.",
        "ncert_key_point": "In dsDNA, (%Purines = %Pyrimidines = 50%), so %A + %C = 50% ALWAYS! Instant 2-second math: %A = 50% - %C = 50% - 20% = 30%!",
        "trap_breakdown": {
            "A": "20% is Guanine (%G), not Adenine!",
            "C": "40% is %G + %C combined.",
            "D": "60% is %A + %T combined without dividing by 2."
        },
        "videoTutorial": BIO_VIDEOS["bot_genetics"]
    },
    {
        "id": 316,
        "subject": "Botany",
        "classLevel": "Class 12",
        "chapter": "Molecular Basis of Inheritance",
        "ncertRef": "NCERT Class 12 Biology, Ch 5 — Lac Operon (Jacob and Monod)",
        "pyqTag": "NEET 2023 / 2024 Mandatory PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "In the lac operon of E. coli, the structural genes z, y, and a code respectively for:",
        "stem_ta": "எ.கோலை (E. coli) பாக்டீரியாவின் லாக் ஓபரானில் (lac operon) உள்ள z, y மற்றும் a ஆகிய அமைப்பு மரபணுக்கள் முறையே எவற்றைக் குறியீடு செய்கின்றன?",
        "choices": [
            {"letter": "A", "text_en": "β-galactosidase, Permease, and Transacetylase", "text_ta": "β-கேலக்டோசிடேஸ், பெர்மியேஸ் மற்றும் டிரான்ஸ்அசிட்டைலேஸ்"},
            {"letter": "B", "text_en": "Permease, β-galactosidase, and Transacetylase", "text_ta": "பெர்மியேஸ், β-கேலக்டோசிடேஸ் மற்றும் டிரான்ஸ்அசிட்டைலேஸ்"},
            {"letter": "C", "text_en": "β-galactosidase, Transacetylase, and Permease", "text_ta": "β-கேலக்டோசிடேஸ், டிரான்ஸ்அசிட்டைலேஸ் மற்றும் பெர்மியேஸ்"},
            {"letter": "D", "text_en": "Repressor protein, β-galactosidase, and Permease", "text_ta": "அடக்கிப் புரதம், β-கேலக்டோசிடேஸ் மற்றும் பெர்மியேஸ்"}
        ],
        "correct": "A",
        "explanation_en": "Exact NCERT Class 12 Ch 5: lac z codes for β-galactosidase (hydrolyses lactose into galactose + glucose); lac y codes for Permease (increases cell permeability to β-galactosides); lac a codes for Transacetylase. Note: lac i codes for the constitutive Repressor protein ('i' stands for inhibitor, NOT inducer!).",
        "explanation_ta": "லாக் ஓபரானில்: z மரபணு -> β-கேலக்டோசிடேஸ்; y மரபணு -> பெர்மியேஸ் (Permease); a மரபணு -> டிரான்ஸ்அசிட்டைலேஸ் (Transacetylase). (i மரபணு அடக்கிப் புரதத்தை உருவாக்குகிறது).",
        "ncert_key_point": "z -> β-galactosidase; y -> Permease; a -> Transacetylase ('a' for acetylase!). And 'i' gene = Inhibitor (repressor), NOT inducer!",
        "trap_breakdown": {
            "B": "Swaps z and y.",
            "C": "Swaps y and a.",
            "D": "Repressor is encoded by regulatory gene 'i', not 'z'."
        },
        "videoTutorial": BIO_VIDEOS["bot_genetics"]
    },
    {
        "id": 317,
        "subject": "Botany",
        "classLevel": "Class 12",
        "chapter": "Molecular Basis of Inheritance",
        "ncertRef": "NCERT Class 12 Biology, Ch 5 — Eukaryotic RNA Polymerases",
        "pyqTag": "NEET 2024 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "In eukaryotes, RNA Polymerase III is responsible for the transcription of:",
        "stem_ta": "யூகேரியோட்டுகளில், RNA பாலிமரேஸ் III எவற்றின் படியெடுத்தலுக்குப் (transcription) பொறுப்பாகும்?",
        "choices": [
            {"letter": "A", "text_en": "rRNAs (28S, 18S, and 5.8S)", "text_ta": "rRNA-க்கள் (28S, 18S மற்றும் 5.8S)"},
            {"letter": "B", "text_en": "Precursor of mRNA (hnRNA)", "text_ta": "mRNA-வின் முன்னோடி (hnRNA)"},
            {"letter": "C", "text_en": "tRNA, 5srRNA, and snRNAs (small nuclear RNAs)", "text_ta": "tRNA, 5srRNA மற்றும் snRNA-க்கள்"},
            {"letter": "D", "text_en": "Only 18S rRNA and mRNA", "text_ta": "18S rRNA மற்றும் mRNA மட்டும்"}
        ],
        "correct": "C",
        "explanation_en": "Division of labour in eukaryotic nucleus (NCERT Class 12 Ch 5): RNA Pol I transcribes rRNAs (28S, 18S, 5.8S); RNA Pol II transcribes hnRNA (precursor of mRNA); RNA Pol III transcribes tRNA, 5srRNA, and snRNAs!",
        "explanation_ta": "யூகேரியோட்டுகளில்: RNA Pol I -> rRNA (28S, 18S, 5.8S); RNA Pol II -> hnRNA (mRNA முன்னோடி); RNA Pol III -> tRNA, 5srRNA மற்றும் snRNA-க்கள்!",
        "ncert_key_point": "Mnemonic 'R-M-T' (1-2-3): Pol I = rRNA (except 5S!); Pol II = mRNA/hnRNA; Pol III = tRNA + 5srRNA + snRNA.",
        "trap_breakdown": {
            "A": "Transcribed by RNA Polymerase I (watch the 5S vs 5.8S distinction!).",
            "B": "Transcribed by RNA Polymerase II.",
            "D": "Mixes Pol I and Pol II products."
        },
        "videoTutorial": BIO_VIDEOS["bot_genetics"]
    },
    {
        "id": 318,
        "subject": "Botany",
        "classLevel": "Class 12",
        "chapter": "Microbes in Human Welfare",
        "ncertRef": "NCERT Class 12 Biology, Ch 8 — Bioactive Molecules (Cyclosporin A & Statins)",
        "pyqTag": "NEET High-Frequency NCERT Table PYQ",
        "questionType": "Match the Column",
        "difficulty": "Easy",
        "stem_en": "Match the bioactive molecule/chemical with its microbial source and medical role:\n(a) Cyclosporin A — (i) Monascus purpureus (blood-cholesterol lowering)\n(b) Statins — (ii) Trichoderma polysporum (immunosuppressive agent)\n(c) Streptokinase — (iii) Aspergillus niger (organic acid)\n(d) Citric acid — (iv) Streptococcus (clot buster)\nChoose the correct option:",
        "stem_ta": "உயிரி-செயல்திறன் மூலக்கூறுகளை அவற்றின் நுண்ணுயிரி மூலம் மற்றும் பயனுடன் பொருத்துக:\n(a) சைக்ளோஸ்போரின் A — (i) மோனாஸ்கஸ் பர்பூரியஸ் (இரத்த கொலஸ்ட்ரால் குறைப்பு)\n(b) ஸ்டேட்டின்கள் — (ii) டிரைக்கோடெர்மா பாலிஸ்போரம் (நோய்த்தடை ஒடுக்கி)\n(c) ஸ்ட்ரெப்டோகைனேஸ் — (iii) அஸ்பெர்ஜில்லஸ் நைஜர் (கரிம அமிலம்)\n(d) சிட்ரிக் அமிலம் — (iv) ஸ்ட்ரெப்டோகாக்கஸ் (இரத்த உறைவு கரைப்பான்)\nசரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        "choices": [
            {"letter": "A", "text_en": "(a)-(ii), (b)-(i), (c)-(iv), (d)-(iii)", "text_ta": "(a)-(ii), (b)-(i), (c)-(iv), (d)-(iii)"},
            {"letter": "B", "text_en": "(a)-(i), (b)-(ii), (c)-(iv), (d)-(iii)", "text_ta": "(a)-(i), (b)-(ii), (c)-(iv), (d)-(iii)"},
            {"letter": "C", "text_en": "(a)-(ii), (b)-(i), (c)-(iii), (d)-(iv)", "text_ta": "(a)-(ii), (b)-(i), (c)-(iii), (d)-(iv)"},
            {"letter": "D", "text_en": "(a)-(iv), (b)-(i), (c)-(ii), (d)-(iii)", "text_ta": "(a)-(iv), (b)-(i), (c)-(ii), (d)-(iii)"}
        ],
        "correct": "A",
        "explanation_en": "Guaranteed +4 marks chapter! Cyclosporin A = fungus Trichoderma polysporum (immunosuppressive in organ-transplant patients); Statins = yeast Monascus purpureus (competitively inhibits cholesterol-synthesizing enzyme); Streptokinase = bacterium Streptococcus (clot buster in myocardial infarction); Citric acid = fungus Aspergillus niger.",
        "explanation_ta": "சைக்ளோஸ்போரின் A = டிரைக்கோடெர்மா பாலிஸ்போரம் (உறுப்பு மாற்று நோயாளிகளுக்கு நோய்த்தடை ஒடுக்கி); ஸ்டேட்டின்கள் = மோனாஸ்கஸ் பர்பூரியஸ் (ஈஸ்ட் — கொலஸ்ட்ரால் குறைப்பு); ஸ்ட்ரெப்டோகைனேஸ் = ஸ்ட்ரெப்டோகாக்கஸ் (கட்டிகளைக் கரைக்கும் நொதி); சிட்ரிக் அமிலம் = அஸ்பெர்ஜில்லஸ் நைஜர்.",
        "ncert_key_point": "Monascus purpureus is a YEAST; Trichoderma polysporum & Aspergillus niger are FUNGI; Streptococcus, Acetobacter aceti, Clostridium butylicum, Lactobacillus are BACTERIA.",
        "trap_breakdown": {
            "B": "Swaps Cyclosporin A and Statins.",
            "C": "Swaps Streptokinase and Citric acid.",
            "D": "Confuses Streptokinase with Cyclosporin A."
        },
        "videoTutorial": BIO_VIDEOS["bot_ncert_tamil"]
    },
    {
        "id": 319,
        "subject": "Botany",
        "classLevel": "Class 12",
        "chapter": "Ecosystem",
        "ncertRef": "NCERT Class 12 Biology, Ch 12 — Ecological Pyramids & 10% Energy Law",
        "pyqTag": "NEET Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Which ecological pyramid is ALWAYS upright in all ecosystems without any exception?",
        "stem_ta": "எந்தவொரு சூழல்மண்டலத்திலும் விதிவிலக்கின்றி எப்போதும் நேராகவே (upright) அமையும் சூழியல் பிரமிடு எது?",
        "choices": [
            {"letter": "A", "text_en": "Pyramid of Numbers", "text_ta": "எண்ணிக்கைப் பிரமிடு"},
            {"letter": "B", "text_en": "Pyramid of Biomass", "text_ta": "உயிரித்திரள் (Biomass) பிரமிடு"},
            {"letter": "C", "text_en": "Pyramid of Energy", "text_ta": "ஆற்றல் பிரமிடு (Pyramid of Energy)"},
            {"letter": "D", "text_en": "Pyramid of Biomass in a sea/ocean", "text_ta": "கடல் சூழல்மண்டல உயிரித்திரள் பிரமிடு"}
        ],
        "correct": "C",
        "explanation_en": "Exact NCERT Class 12 Ecosystem law: Pyramid of ENERGY is ALWAYS upright and can NEVER be inverted, because when energy flows from one trophic level to the next (Lindeman's 10% law), some energy is always lost as heat at each step! By contrast, Pyramid of Biomass in the sea is generally inverted (fishes > phytoplankton standing crop), and Pyramid of Numbers on a single large tree can be inverted/spindle-shaped.",
        "explanation_ta": "ஆற்றல் பிரமிடு (Pyramid of Energy) எப்போதும் நேராகவே (upright) இருக்கும்; ஒருபோதும் தலைகீழாக அமையாது! ஏனெனில் ஒரு உணவூட்ட மட்டத்திலிருந்து அடுத்த மட்டத்திற்கு ஆற்றல் செல்லும்போது வெப்பமாக ஆற்றல் இழப்பு நிகழ்கிறது (10% விதி). கடலில் உயிரித்திரள் பிரமிடு தலைகீழாக அமையும்.",
        "ncert_key_point": "Pyramid of Energy = NEVER inverted (100% always upright). Pyramid of Biomass in Sea = Inverted.",
        "trap_breakdown": {
            "A": "Inverted on a single large tree supporting thousands of insects.",
            "B": "Inverted in marine ecosystems.",
            "D": "Classic example of an INVERTED pyramid!"
        },
        "videoTutorial": BIO_VIDEOS["bot_ncert_tamil"]
    },
    {
        "id": 320,
        "subject": "Botany",
        "classLevel": "Class 12",
        "chapter": "Biodiversity and Conservation",
        "ncertRef": "NCERT Class 12 Biology, Ch 13 — In-situ vs Ex-situ Conservation & Evil Quartet",
        "pyqTag": "NEET 2023 / 2024 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Among the 'Evil Quartet' of major causes of biodiversity losses, which one is the MOST important cause driving animals and plants to extinction?",
        "stem_ta": "உயிர்ப்பன்முகத்தன்மை இழப்பிற்கான நான்கு முக்கிய காரணிகளில் ('Evil Quartet'), விலங்குகள் மற்றும் தாவரங்கள் அழிவதற்கு மிக முக்கியமான முதன்மைக் காரணி எது?",
        "choices": [
            {"letter": "A", "text_en": "Over-exploitation", "text_ta": "மிகைச் சுரண்டல் (Over-exploitation)"},
            {"letter": "B", "text_en": "Alien species invasions", "text_ta": "அயல் இனங்களின் படையெடுப்பு"},
            {"letter": "C", "text_en": "Habitat loss and fragmentation", "text_ta": "வாழிட இழப்பு மற்றும் துண்டாடப்படுதல் (Habitat loss and fragmentation)"},
            {"letter": "D", "text_en": "Co-extinctions", "text_ta": "இணை-அழிவுகள் (Co-extinctions)"}
        ],
        "correct": "C",
        "explanation_en": "Exact NCERT Class 12 Biodiversity line: 'Habitat loss and fragmentation: This is the MOST IMPORTANT cause driving animals and plants to extinction' (exemplified by tropical rain forests shrinking from 14% to no more than 6% of Earth's land surface, and Amazon rainforest clearance).",
        "explanation_ta": "NCERT உயிர்ப்பன்முகத்தன்மை பாடத்தின்படி, விலங்குகள் மற்றும் தாவர இனங்கள் அழிவதற்கு மிக முக்கியமான முதன்மைக் காரணி 'வாழிட இழப்பு மற்றும் துண்டாடப்படுதல்' (Habitat loss and fragmentation) ஆகும்.",
        "ncert_key_point": "All 4 options are members of 'The Evil Quartet', so read the superlative 'MOST important cause' -> Habitat loss and fragmentation!",
        "trap_breakdown": {
            "A": "Part of Evil Quartet (e.g., Steller's sea cow, Passenger pigeon), but not the #1 overall driver.",
            "B": "Part of Evil Quartet (e.g., Nile perch in Lake Victoria, Lantana, Eichhornia).",
            "D": "Part of Evil Quartet (e.g., plant-pollinator mutualism)."
        },
        "videoTutorial": BIO_VIDEOS["bot_ncert_tamil"]
    },
]

ZOOLOGY_QUESTIONS = [
    {
        "id": 401,
        "subject": "Zoology",
        "classLevel": "Class 11",
        "chapter": "Animal Kingdom",
        "ncertRef": "NCERT Class 11 Biology, Ch 4 — Phylum Features (Porifera, Ctenophora, Platyhelminthes, Echinodermata)",
        "pyqTag": "NEET 2023 / 2024 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "Water vascular system (helping in locomotion, capture/transport of food, and respiration) is the most distinctive feature of which phylum?",
        "stem_ta": "நீர் இரத்த ஓட்ட / நீர்க்குழாய் மண்டலம் (Water vascular system — இடப்பெயர்ச்சி, உணவு பிடித்தல் மற்றும் சுவாசத்திற்கு உதவுவது) எந்தத் தொகுதியின் தனிச்சிறப்புப் பண்பாகும்?",
        "choices": [
            {"letter": "A", "text_en": "Porifera (Sponges)", "text_ta": "துளையுடலிகள் (Porifera)"},
            {"letter": "B", "text_en": "Echinodermata (e.g., Asterias / Starfish)", "text_ta": "முட்தோலிகள் (Echinodermata — எ.கா. நட்சத்திர மீன்)"},
            {"letter": "C", "text_en": "Cnidaria (Coelenterata)", "text_ta": "குழியுடலிகள் (Cnidaria)"},
            {"letter": "D", "text_en": "Ctenophora (Comb jellies)", "text_ta": "டீனோஃபோரா (Ctenophora)"}
        ],
        "correct": "B",
        "explanation_en": "Crucial NCERT distinction: Porifera (Sponges) have a WATER TRANSPORT or CANAL SYSTEM (ostia -> spongocoel -> osculum), whereas Echinodermata (Asterias, Echinus, Ophiura) possess the WATER VASCULAR SYSTEM (tube feet / ambulacral system)!",
        "explanation_ta": "மிக முக்கிய NCERT வேறுபாடு: துளையுடலிகளில் (Porifera) இருப்பது 'நீர் கடத்து / கால்வாய் மண்டலம்' (Water canal system); முட்தோலிகளில் (Echinodermata) இருப்பது 'நீர்க்குழாய் மண்டலம்' (Water vascular system)!",
        "ncert_key_point": "Water CANAL system = Porifera. Water VASCULAR system = Echinodermata. Never confuse these two in NEET!",
        "trap_breakdown": {
            "A": "Porifera has a water CANAL system, NOT a water vascular system — #1 Animal Kingdom trap!",
            "C": "Cnidaria has cnidoblasts and gastrovascular cavity.",
            "D": "Ctenophora has 8 ciliated comb plates and bioluminescence."
        },
        "videoTutorial": BIO_VIDEOS["zoo_physio"]
    },
    {
        "id": 402,
        "subject": "Zoology",
        "classLevel": "Class 11",
        "chapter": "Structural Organisation in Animals",
        "ncertRef": "NCERT Class 11 Biology, Ch 7 — Epithelial & Connective Tissues",
        "pyqTag": "NEET Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Ciliated epithelium, whose function is to move particles or mucus in a specific direction over the epithelium, is mainly present on the inner surface of:",
        "stem_ta": "துகள்கள் அல்லது கோழையை ஒரு குறிப்பிட்ட திசையில் நகர்த்த உதவும் குறுஇழை எபிதீலியம் (Ciliated epithelium) முதன்மையாக எதன் உள்பரப்பில் காணப்படுகிறது?",
        "choices": [
            {"letter": "A", "text_en": "Walls of blood vessels and air sacs (alveoli) of lungs", "text_ta": "இரத்த நாளங்களின் சுவர்கள் மற்றும் நுரையீரல் காற்று நுண்ணறைகள்"},
            {"letter": "B", "text_en": "Bronchioles and Fallopian tubes", "text_ta": "மூச்சுக்கிளைக் குழாய்கள் (Bronchioles) மற்றும் ஃபெலோப்பியன் குழாய்கள்"},
            {"letter": "C", "text_en": "Ducts of salivary glands and pancreatic ducts", "text_ta": "உமிழ்நீர் சுரப்பி நாளங்கள் மற்றும் கணைய நாளங்கள்"},
            {"letter": "D", "text_en": "Dry surface of the skin", "text_ta": "தோலின் உலர்ந்த மேற்பரப்பு"}
        ],
        "correct": "B",
        "explanation_en": "Exact NCERT Class 11 Animal Tissues line: Ciliated epithelium (columnar/cuboidal cells bearing cilia) is mainly present in the inner surface of hollow organs like BRONCHIOLES and FALLOPIAN TUBES!",
        "explanation_ta": "NCERT விலங்குத் திசுக்கள் பாடத்தின்படி: குறுஇழை எபிதீலியம் (Ciliated epithelium) மூச்சுக்கிளைக் குழாய்கள் (Bronchioles) மற்றும் கருமுட்டைக் குழாய்களின் (Fallopian tubes) உள்பரப்பில் காணப்படுகிறது!",
        "ncert_key_point": "Squamous = Blood vessels + Alveoli; Cuboidal (brush border) = PCT of nephron; Ciliated = Bronchioles + Fallopian tubes; Compound = Skin, buccal cavity, salivary/pancreatic ducts.",
        "trap_breakdown": {
            "A": "Simple squamous epithelium (diffusion boundary).",
            "C": "Compound epithelium.",
            "D": "Compound keratinized epithelium."
        },
        "videoTutorial": BIO_VIDEOS["zoo_physio"]
    },
    {
        "id": 403,
        "subject": "Zoology",
        "classLevel": "Class 11",
        "chapter": "Biomolecules",
        "ncertRef": "NCERT Class 11 Biology, Ch 9 — Enzymes (Competitive Inhibition)",
        "pyqTag": "NEET 2023 / 2024 Official PYQ",
        "questionType": "Statement I & II",
        "difficulty": "Medium",
        "stem_en": "Given below are two statements regarding enzyme action:\nStatement I: Inhibition of succinic dehydrogenase by malonate, which closely resembles the substrate succinate in structure, is an example of competitive inhibition.\nStatement II: In competitive inhibition, the inhibitor decreases the apparent affinity of enzyme for substrate (K_m increases), while V_max remains unchanged at high substrate concentration.\nChoose the correct option:",
        "stem_ta": "நொதிச் செயல்பாடு குறித்த இரு கூற்றுகள்:\nகூற்று I: சக்சினேட்டை ஒத்த அமைப்புடைய மலோனேட்டால் சக்சினிக் டிஹைட்ரோஜினேஸ் நொதி தடுக்கப்படுவது போட்டித் தடுப்பிற்கு (Competitive inhibition) எடுத்துக்காட்டாகும்.\nகூற்று II: போட்டித் தடுப்பில் K_m மதிப்பு அதிகரிக்கிறது, ஆனால் அதிக வினைபடுபொருள் செறிவில் V_max மாறுவதில்லை.\nசரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        "choices": [
            {"letter": "A", "text_en": "Both Statement I and Statement II are correct", "text_ta": "கூற்று I மற்றும் கூற்று II ஆகிய இரண்டும் சரி"},
            {"letter": "B", "text_en": "Both Statement I and Statement II are incorrect", "text_ta": "கூற்று I மற்றும் கூற்று II ஆகிய இரண்டும் தவறு"},
            {"letter": "C", "text_en": "Statement I is correct but Statement II is incorrect", "text_ta": "கூற்று I சரி, ஆனால் கூற்று II தவறு"},
            {"letter": "D", "text_en": "Statement I is incorrect but Statement II is correct", "text_ta": "கூற்று I தவறு, ஆனால் கூற்று II சரி"}
        ],
        "correct": "A",
        "explanation_en": "Malonate competing with succinate for the active site of succinic dehydrogenase is NCERT's textbook example of competitive inhibition! Because flooding with excess substrate can outcompete the reversible inhibitor, V_max stays unchanged while apparent K_m increases. Both statements are correct!",
        "explanation_ta": "சக்சினேட்டுடன் மலோனேட் போட்டியிடுவது போட்டித் தடுப்பிற்கு NCERT எடுத்துக்காட்டு. அதிக வினைபடுபொருள் சேர்க்கும்போது தடுப்பை வெல்ல முடிவதால் V_max மாறாது, ஆனால் K_m அதிகரிக்கும். இரு கூற்றுகளும் சரி!",
        "ncert_key_point": "Competitive inhibition: K_m INCREASES, V_max UNCHANGED. Classic example: Malonate inhibits Succinic dehydrogenase.",
        "trap_breakdown": {
            "B": "Both are verified NCERT & NEET 2023/2024 enzyme kinetics facts.",
            "C": "Many students wrongly think competitive inhibitor lowers V_max — it raises K_m without changing V_max!",
            "D": "Malonate + succinic dehydrogenase is verbatim NCERT."
        },
        "videoTutorial": BIO_VIDEOS["zoo_physio"]
    },
    {
        "id": 404,
        "subject": "Zoology",
        "classLevel": "Class 11",
        "chapter": "Breathing and Exchange of Gases",
        "ncertRef": "NCERT Class 11 Biology, Ch 14 — Oxygen Dissociation Curve (Oxyhaemoglobin)",
        "pyqTag": "NEET 2021 / 2024 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "Which set of physiological conditions in the pulmonary alveoli FAVOURS the formation of oxyhaemoglobin?",
        "stem_ta": "நுரையீரல் காற்று நுண்ணறைகளில் (alveoli) ஆக்சிஹீமோகுளோபின் உருவாவதற்குச் சாதகமான உடலியல் நிலைகள் எவை?",
        "choices": [
            {"letter": "A", "text_en": "High pO2, low pCO2, lesser H^+ concentration (higher pH), and lower temperature", "text_ta": "அதிக pO2, குறைந்த pCO2, குறைந்த H^+ செறிவு (அதிக pH), மற்றும் குறைந்த வெப்பநிலை"},
            {"letter": "B", "text_en": "Low pO2, high pCO2, high H^+ concentration, and higher temperature", "text_ta": "குறைந்த pO2, அதிக pCO2, அதிக H^+ செறிவு, மற்றும் அதிக வெப்பநிலை"},
            {"letter": "C", "text_en": "High pO2, high pCO2, high H^+ concentration, and higher temperature", "text_ta": "அதிக pO2, அதிக pCO2, அதிக H^+ செறிவு, மற்றும் அதிக வெப்பநிலை"},
            {"letter": "D", "text_en": "High pO2, low pCO2, high H^+ concentration (low pH), and higher temperature", "text_ta": "அதிக pO2, குறைந்த pCO2, அதிக H^+ செறிவு (குறைந்த pH), மற்றும் அதிக வெப்பநிலை"}
        ],
        "correct": "A",
        "explanation_en": "Verbatim NCERT Class 11 Ch 14: In alveoli, HIGH pO2, LOW pCO2, LESSER H^+ concentration (higher pH), and LOWER temperature favour oxyhaemoglobin association (left shift). In metabolically active tissues, the exact opposite (low pO2, high pCO2, high H^+, higher T) favours O2 dissociation (right shift / Bohr effect)!",
        "explanation_ta": "காற்று நுண்ணறைகளில் அதிக pO2, குறைந்த pCO2, குறைந்த H^+ செறிவு மற்றும் குறைந்த வெப்பநிலை ஆகியவை ஆக்சிஹீமோகுளோபின் உருவாகச் சாதகமானவை. திசுக்களில் இதற்கு நேர் எதிரான நிலைகள் O2 பிரிகையடைய உதவும்!",
        "ncert_key_point": "Watch H^+ vs pH carefully! Lesser H^+ concentration = HIGHER pH (alkaline shift in lungs).",
        "trap_breakdown": {
            "B": "Conditions in active tissues causing OXYHAEMOGLOBIN DISSOCIATION, not formation!",
            "C": "High pCO2, H^+, T oppose O2 binding.",
            "D": "High H^+ (low pH) causes Bohr dissociation."
        },
        "videoTutorial": BIO_VIDEOS["zoo_physio"]
    },
    {
        "id": 405,
        "subject": "Zoology",
        "classLevel": "Class 11",
        "chapter": "Body Fluids and Circulation",
        "ncertRef": "NCERT Class 11 Biology, Ch 15 — Electrocardiograph (ECG)",
        "pyqTag": "NEET 2023 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "In a standard human Electrocardiogram (ECG), the QRS complex represents:",
        "stem_ta": "மனிதனின் தரப்படுத்தப்பட்ட மின்இதய வரைபடத்தில் (ECG), QRS அலைத்தொகுப்பு எதைக் குறிக்கிறது?",
        "choices": [
            {"letter": "A", "text_en": "Depolarisation of the atria", "text_ta": "ஆரிக்கிள்களின் (ஏட்ரியா) முனைப்பியக்க நீக்கம்"},
            {"letter": "B", "text_en": "Depolarisation of the ventricles, initiating ventricular contraction", "text_ta": "வென்ட்ரிக்கிள்களின் முனைப்பியக்க நீக்கம் (வென்ட்ரிக்கிள் சுருக்கத்தைத் தொடங்குகிறது)"},
            {"letter": "C", "text_en": "Repolarisation of the ventricles (return from excited to normal state)", "text_ta": "வென்ட்ரிக்கிள்களின் மீள்முனைப்பியக்கம் (Repolarisation)"},
            {"letter": "D", "text_en": "End of ventricular systole", "text_ta": "வென்ட்ரிக்கிள் சுருக்கத்தின் முடிவு"}
        ],
        "correct": "B",
        "explanation_en": "Exact NCERT ECG waves: P-wave = electrical excitation (depolarisation) of atria; QRS complex = depolarisation of ventricles (initiates ventricular systole shortly after Q); T-wave = repolarisation of ventricles; end of T-wave marks the end of systole!",
        "explanation_ta": "ECG அலைகள்: P அலை = ஏட்ரியா முனைப்பியக்க நீக்கம்; QRS தொகுப்பு = வென்ட்ரிக்கிள்களின் முனைப்பியக்க நீக்கம் (சுருக்கத்தைத் தொடங்கும்); T அலை = வென்ட்ரிக்கிள்களின் மீள்முனைப்பியக்கம்; T அலையின் முடிவு சிஸ்டோலின் முடிவைக் குறிக்கும்!",
        "ncert_key_point": "P = Atrial depolarisation; QRS = Ventricular depolarisation (counting QRS gives heart rate!); T = Ventricular repolarisation; End of T = End of systole.",
        "trap_breakdown": {
            "A": "Represented by the P-wave.",
            "C": "Represented by the T-wave.",
            "D": "Marked by the END of the T-wave, not QRS!"
        },
        "videoTutorial": BIO_VIDEOS["zoo_physio"]
    },
    {
        "id": 406,
        "subject": "Zoology",
        "classLevel": "Class 11",
        "chapter": "Excretory Products and their Elimination",
        "ncertRef": "NCERT Class 11 Biology, Ch 16 — Regulation of Kidney Function (RAAS vs ANF)",
        "pyqTag": "NEET Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "Which hormone acts as a natural check on the Renin-Angiotensin mechanism by causing vasodilation and thereby DECREASING blood pressure?",
        "stem_ta": "இரத்த நாளங்களை விரிவடையச் செய்து இரத்த அழுத்தத்தைக் குறைப்பதன் மூலம், ரெனின்-ஆஞ்சியோடென்சின் (RAAS) செயல்முறைக்கு எதிராகச் செயல்படும் ஹார்மோன் எது?",
        "choices": [
            {"letter": "A", "text_en": "Aldosterone", "text_ta": "ஆல்டோஸ்டிரோன் (Aldosterone)"},
            {"letter": "B", "text_en": "Antidiuretic Hormone (ADH / Vasopressin)", "text_ta": "ஆன்டிடையூரிட்டிக் ஹார்மோன் (ADH / வாசோபிரஸ்ஸின்)"},
            {"letter": "C", "text_en": "Atrial Natriuretic Factor (ANF)", "text_ta": "ஏட்ரியல் நேட்ரியூரிட்டிக் காரணி (ANF)"},
            {"letter": "D", "text_en": "Angiotensin II", "text_ta": "ஆஞ்சியோடென்சின் II"}
        ],
        "correct": "C",
        "explanation_en": "Exact NCERT Class 11 Ch 16 line: Increased blood flow to the atria of the heart causes release of Atrial Natriuretic Factor (ANF). ANF causes VASODILATION (dilation of blood vessels) and DECREASES blood pressure, acting as a physiological check on the Renin-Angiotensin-Aldosterone mechanism!",
        "explanation_ta": "இதயத்தின் ஆரிக்கிள்களிலிருந்து சுரக்கும் ஏட்ரியல் நேட்ரியூரிட்டிக் காரணி (ANF) இரத்த நாளங்களை விரிவடையச் செய்து (vasodilation) இரத்த அழுத்தத்தைக் குறைக்கிறது; இது ரெனின்-ஆஞ்சியோடென்சின் அமைப்பைக் கட்டுப்படுத்துகிறது.",
        "ncert_key_point": "ADH & Angiotensin II = powerful VASOCONSTRICTORS (raise BP & GFR). ANF = VASODILATOR (lowers BP).",
        "trap_breakdown": {
            "A": "Aldosterone increases Na^+ and water reabsorption in DCT, raising blood volume and BP.",
            "B": "ADH/Vasopressin constricts blood vessels, raising BP.",
            "D": "Angiotensin II is a powerful vasoconstrictor that raises glomerular BP."
        },
        "videoTutorial": BIO_VIDEOS["zoo_physio"]
    },
    {
        "id": 407,
        "subject": "Zoology",
        "classLevel": "Class 11",
        "chapter": "Locomotion and Movement",
        "ncertRef": "NCERT Class 11 Biology, Ch 17 — Sliding Filament Theory & Muscular Disorders",
        "pyqTag": "NEET 2022 / 2024 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "During skeletal muscle contraction according to the sliding filament theory, which of the following remains UNCHANGED in length?",
        "stem_ta": "சறுக்கும் இழைக் கொள்கையின்படி (Sliding filament theory), எலும்புத் தசைச் சுருக்கத்தின்போது கீழ்க்கண்டவற்றுள் எதன் நீளம் மாறாமல் அப்படியே இருக்கும்?",
        "choices": [
            {"letter": "A", "text_en": "I-band (Isotropic band)", "text_ta": "I-பட்டை"},
            {"letter": "B", "text_en": "H-zone", "text_ta": "H-மண்டலம்"},
            {"letter": "C", "text_en": "A-band (Anisotropic band)", "text_ta": "A-பட்டை (Anisotropic band)"},
            {"letter": "D", "text_en": "Sarcomere (distance between two successive Z-lines)", "text_ta": "சார்கோமியர் (இரு Z-கோடுகளுக்கு இடையிலான தூரம்)"}
        ],
        "correct": "C",
        "explanation_en": "During muscle contraction, thin (actin) filaments slide inward over thick (myosin) filaments pulling Z-lines closer: Sarcomere shortens, I-band shortens, and H-zone narrows/disappears — whereas the A-BAND (length of thick myosin filaments) RETAINS ITS LENGTH!",
        "explanation_ta": "தசைச் சுருக்கத்தின்போது சார்கோமியர், I-பட்டை மற்றும் H-மண்டலம் ஆகியவை சுருங்கும்; ஆனால் தடித்த மயோசின் இழைகளின் நீளமான A-பட்டை (A-band) எந்த மாற்றமும் இன்றி அதே நீளத்தில் இருக்கும்!",
        "ncert_key_point": "Mnemonic: 'A-band = Always constant' during muscle contraction!",
        "trap_breakdown": {
            "A": "I-band gets reduced.",
            "B": "H-zone narrows and disappears at maximal contraction.",
            "D": "Sarcomere shortens as Z-lines are pulled inward."
        },
        "videoTutorial": BIO_VIDEOS["zoo_physio"]
    },
    {
        "id": 408,
        "subject": "Zoology",
        "classLevel": "Class 11",
        "chapter": "Neural Control and Coordination",
        "ncertRef": "NCERT Class 11 Biology, Ch 18 — Na+-K+ Pump & Resting Potential",
        "pyqTag": "NEET Exact NCERT Numbers PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Across the resting axonal membrane, the sodium-potassium pump maintains ionic gradients by actively transporting:",
        "stem_ta": "ஓய்வுநிலையிலுள்ள நரம்பிழைச் சவ்வின் (axonal membrane) குறுக்கே சோடியம்-பொட்டாசியம் பம்ப் அயனிச் சரிவை எவ்வாறு பராமரிக்கிறது?",
        "choices": [
            {"letter": "A", "text_en": "3 Na^+ outwards for 2 K^+ into the cell", "text_ta": "3 Na^+ அயனிகளை வெளியேற்றியும், 2 K^+ அயனிகளை செல்லினுள் கடத்தியும்"},
            {"letter": "B", "text_en": "2 Na^+ outwards for 3 K^+ into the cell", "text_ta": "2 Na^+ வெளியே, 3 K^+ உள்ளே"},
            {"letter": "C", "text_en": "3 Na^+ into the cell for 2 K^+ outwards", "text_ta": "3 Na^+ உள்ளே, 2 K^+ வெளியே"},
            {"letter": "D", "text_en": "2 Na^+ into the cell for 2 K^+ outwards", "text_ta": "2 Na^+ உள்ளே, 2 K^+ வெளியே"}
        ],
        "correct": "A",
        "explanation_en": "Exact NCERT Class 11 Ch 18 line: The Na^+-K^+ ATPase pump transports 3 Na^+ OUTWARDS for 2 K^+ INTO the cell per ATP hydrolysed, keeping the outer surface positively charged and inner axoplasm negatively charged at resting state.",
        "explanation_ta": "NCERT நரம்பு மண்டலப் பாடத்தின்படி, சோடியம்-பொட்டாசியம் பம்ப் ஒரு சுழற்சியில் 3 Na^+ அயனிகளை செல்லுக்கு வெளியேயும், 2 K^+ அயனிகளை செல்லுக்கு உள்ளேயும் கடத்துகிறது!",
        "ncert_key_point": "Mnemonic '3 NO, 2 KI': 3 Na^+ Out, 2 K^+ In!",
        "trap_breakdown": {
            "B": "Swaps numbers 3 and 2.",
            "C": "Reverses directions (would depolarize instead of maintaining resting state).",
            "D": "Electroneutral 2:2 is incorrect."
        },
        "videoTutorial": BIO_VIDEOS["zoo_physio"]
    },
    {
        "id": 409,
        "subject": "Zoology",
        "classLevel": "Class 11",
        "chapter": "Chemical Coordination and Integration",
        "ncertRef": "NCERT Class 11 Biology, Ch 19 — Mechanism of Hormone Action (Membrane vs Intracellular Receptors)",
        "pyqTag": "NEET Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "Which of the following sets contains ONLY hormones that interact with intracellular (mostly nuclear) receptors and directly regulate gene expression without generating a second messenger?",
        "stem_ta": "பின்வரும் தொகுப்புகளில் எது இரண்டாம் நிலைத் தூதுவரை உருவாக்காமல், செல்லக (உட்கரு) ஏற்பிகளுடன் நேரடியாக இணைந்து மரபணு வெளிப்பாட்டைக் கட்டுப்படுத்தும் ஹார்மோன்களை மட்டுமே கொண்டுள்ளது?",
        "choices": [
            {"letter": "A", "text_en": "Insulin, Glucagon, and Epinephrine", "text_ta": "இன்சுலின், குளுக்ககான் மற்றும் எபிநெஃப்ரின்"},
            {"letter": "B", "text_en": "Cortisol, Testosterone, Estradiol, and Thyroxine (Iodothyronines)", "text_ta": "கார்டிசால், டெஸ்டோஸ்டிரோன், எஸ்ட்ராடையால் மற்றும் தைராக்சின்"},
            {"letter": "C", "text_en": "FSH, LH, and Oxytocin", "text_ta": "FSH, LH மற்றும் ஆக்சிடோசின்"},
            {"letter": "D", "text_en": "Epinephrine, Cortisol, and Insulin", "text_ta": "எபிநெஃப்ரின், கார்டிசால் மற்றும் இன்சுலின்"}
        ],
        "correct": "B",
        "explanation_en": "Lipid-soluble steroid hormones (Cortisol, Testosterone, Estradiol, Progesterone) AND Iodothyronines (Thyroxine / T3, T4) cross the lipid bilayer and bind intracellular/nuclear receptors! Peptide/protein hormones (Insulin, Glucagon, FSH, LH, Oxytocin) and amino-acid derivative Epinephrine bind membrane-bound receptors and generate second messengers (cAMP, IP3, Ca^2+).",
        "explanation_ta": "ஸ்டீராய்டு ஹார்மோன்கள் (கார்டிசால், டெஸ்டோஸ்டிரோன், எஸ்ட்ராடையால்) மற்றும் அயோடோதைரோனின்கள் (தைராக்சின்) செல் சவ்வைக் கடந்து உட்கரு ஏற்பிகளுடன் இணைகின்றன! புரத ஹார்மோன்களும் எபிநெஃப்ரினும் சவ்வு ஏற்பிகளுடன் இணைந்து இரண்டாம் நிலைத் தூதுவர்களை (cAMP, IP3, Ca^2+) உருவாக்குகின்றன.",
        "ncert_key_point": "Watch the amino-acid derivative split: Thyroxine (iodothyronine) = Intracellular nuclear receptor; Epinephrine = Membrane receptor!",
        "trap_breakdown": {
            "A": "All three use membrane-bound receptors.",
            "C": "All three are peptide/protein hormones using membrane receptors (FSH shown in NCERT diagram generating cAMP/IP3!).",
            "D": "Insulin and Epinephrine use membrane receptors."
        },
        "videoTutorial": BIO_VIDEOS["zoo_physio"]
    },
    {
        "id": 410,
        "subject": "Zoology",
        "classLevel": "Class 12",
        "chapter": "Human Reproduction",
        "ncertRef": "NCERT Class 12 Biology, Ch 2 — Gametogenesis (Spermatogenesis vs Oogenesis)",
        "pyqTag": "NEET Classic Ploidy PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "In human gametogenesis, which of the following pairs consists of BOTH HAPLOID (n = 23 chromosomes) cells?",
        "stem_ta": "மனித இனச்செல் உருவாக்கத்தில் (Gametogenesis), பின்வரும் இணைகளில் எது இரண்டுமே ஒற்றைமடிய (Haploid, n = 23) செல்களைக் கொண்டுள்ளது?",
        "choices": [
            {"letter": "A", "text_en": "Primary spermatocyte and Primary oocyte", "text_ta": "முதல்நிலை விந்து தாய்ச்செல் மற்றும் முதல்நிலை அண்ட தாய்ச்செல்"},
            {"letter": "B", "text_en": "Spermatogonium and Secondary polar body", "text_ta": "ஸ்பெர்மட்டோகோனியம் மற்றும் இரண்டாம் நிலை துருவ உறுப்பு"},
            {"letter": "C", "text_en": "Secondary spermatocyte and Secondary oocyte", "text_ta": "இரண்டாம் நிலை விந்து செல் (Secondary spermatocyte) மற்றும் இரண்டாம் நிலை அண்ட செல் (Secondary oocyte)"},
            {"letter": "D", "text_en": "Primary oocyte and Spermatid", "text_ta": "முதல்நிலை அண்ட செல் மற்றும் ஸ்பெர்மாட்டிட்"}
        ],
        "correct": "C",
        "explanation_en": "Meiosis I is the reductional division! Primary spermatocyte (2n = 46) and Primary oocyte (2n = 46) are DIPLOID. Once they complete Meiosis I, they form Secondary spermatocytes (n = 23) and Secondary oocyte + First polar body (n = 23), which are HAPLOID!",
        "explanation_ta": "மியாசிஸ் I குன்றல் பகுப்பாகும்! முதல்நிலை (Primary) விந்து மற்றும் அண்ட செல்கள் இருமடியம் (2n = 46). மியாசிஸ் I முடிந்தவுடன் உருவாகும் இரண்டாம் நிலை (Secondary) விந்து செல் மற்றும் இரண்டாம் நிலை அண்ட செல் இரண்டும் ஒற்றைமடியம் (n = 23) ஆகும்!",
        "ncert_key_point": "Rule of thumb: 'Primary' = Diploid (2n = 46); 'Secondary', 'Spermatid', 'Spermatozoa', 'Ovum', 'Polar bodies' = Haploid (n = 23)!",
        "trap_breakdown": {
            "A": "Both Primary spermatocyte and Primary oocyte are diploid (2n = 46).",
            "B": "Spermatogonium is diploid (2n = 46).",
            "D": "Primary oocyte is diploid (2n = 46)."
        },
        "videoTutorial": BIO_VIDEOS["zoo_physio"]
    },
    {
        "id": 411,
        "subject": "Zoology",
        "classLevel": "Class 12",
        "chapter": "Human Reproduction",
        "ncertRef": "NCERT Class 12 Biology, Ch 2 — Menstrual Cycle & Placental Hormones",
        "pyqTag": "NEET 2023 / 2024 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Which set of hormones is produced in women ONLY during pregnancy (secreted by placenta / ovary during gestation)?",
        "stem_ta": "பெண்களில் கர்ப்ப காலத்தில் மட்டுமே உற்பத்தி செய்யப்படும் ஹார்மோன்களின் தொகுப்பு எது?",
        "choices": [
            {"letter": "A", "text_en": "Estrogen, Progesterone, and Cortisol", "text_ta": "ஈஸ்ட்ரோஜன், புரோஜெஸ்டிரோன் மற்றும் கார்டிசால்"},
            {"letter": "B", "text_en": "hCG (human Chorionic Gonadotropin), hPL (human Placental Lactogen), and Relaxin", "text_ta": "hCG, hPL மற்றும் ரிலாக்சின் (Relaxin)"},
            {"letter": "C", "text_en": "LH, FSH, and Prolactin", "text_ta": "LH, FSH மற்றும் புரோலாக்டின்"},
            {"letter": "D", "text_en": "Oxytocin, Progesterone, and Thyroxine", "text_ta": "ஆக்சிடோசின், புரோஜெஸ்டிரோன் மற்றும் தைராக்சின்"}
        ],
        "correct": "B",
        "explanation_en": "Verbatim bold NCERT Class 12 Ch 2 line: 'hCG, hPL and relaxin are produced in women ONLY during pregnancy!' (Estrogens, progestogens, cortisol, prolactin, thyroxine ARE increased several-fold during pregnancy, but are also present in non-pregnant women).",
        "explanation_ta": "NCERT வகுப்பு 12 மனித இனப்பெருக்கப் பாடத்தின் நேரடி வரி: 'hCG, hPL மற்றும் ரிலாக்சின் ஆகிய மூன்றும் பெண்களில் கர்ப்ப காலத்தில் மட்டுமே உற்பத்தி செய்யப்படுகின்றன!'",
        "ncert_key_point": "ONLY during pregnancy = hCG, hPL, Relaxin. Increased several-fold during pregnancy = Estrogen, Progesterone, Cortisol, Prolactin, Thyroxine.",
        "trap_breakdown": {
            "A": "Present in non-pregnant state too.",
            "C": "Present throughout reproductive life.",
            "D": "Present in non-pregnant state too."
        },
        "videoTutorial": BIO_VIDEOS["zoo_physio"]
    },
    {
        "id": 412,
        "subject": "Zoology",
        "classLevel": "Class 12",
        "chapter": "Reproductive Health",
        "ncertRef": "NCERT Class 12 Biology, Ch 3 — Intra Uterine Devices (IUDs) & ART",
        "pyqTag": "NEET Annual Mandatory Question",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Which of the following is a HORMONE-RELEASING Intra-Uterine Device (IUD) that makes the uterus unsuitable for implantation and the cervix hostile to sperms?",
        "stem_ta": "கருப்பையை கருப்பதித்தலுக்குத் தகுதியற்றதாகவும், கருப்பை வாயை விந்தணுக்களுக்கு எதிரானதாகவும் மாற்றும் 'ஹார்மோன் வெளியிடும்' உள்கருப்பைச் சாதனம் (Hormone-releasing IUD) எது?",
        "choices": [
            {"letter": "A", "text_en": "Lippes loop", "text_ta": "லிப்பஸ் வளையம் (Lippes loop)"},
            {"letter": "B", "text_en": "Multiload 375", "text_ta": "மல்டிலோடு 375 (Multiload 375)"},
            {"letter": "C", "text_en": "LNG-20 (and Progestasert)", "text_ta": "LNG-20 (மற்றும் புரோஜெஸ்டாசெர்ட்)"},
            {"letter": "D", "text_en": "CuT and Cu7", "text_ta": "CuT மற்றும் Cu7"}
        ],
        "correct": "C",
        "explanation_en": "NCERT classifies IUDs into 3 strict categories asked ALMOST EVERY YEAR in NEET:\n1. Non-medicated IUDs: Lippes loop\n2. Copper-releasing IUDs: CuT, Cu7, Multiload 375 (Cu^2+ suppresses sperm motility & fertilising capacity)\n3. Hormone-releasing IUDs: Progestasert, LNG-20!",
        "explanation_ta": "NCERT-இன் 3 வகை IUD-கள் (ஒவ்வொரு ஆண்டும் NEET-இல் கேட்கப்படும் வினா!):\n1. மருந்தில்லா IUD: லிப்பஸ் வளையம்\n2. தாமிரம் வெளியிடும் IUD: CuT, Cu7, Multiload 375\n3. ஹார்மோன் வெளியிடும் IUD: Progestasert, LNG-20!",
        "ncert_key_point": "Memorize all 3 IUD groups cold: Non-medicated (Lippes loop) | Cu-releasing (CuT, Cu7, Multiload 375) | Hormone-releasing (Progestasert, LNG-20).",
        "trap_breakdown": {
            "A": "Non-medicated IUD (increases phagocytosis of sperms).",
            "B": "Multiload 375 is a COPPER-releasing IUD ('375' refers to 375 mm^2 copper surface area), NOT hormone-releasing!",
            "D": "Copper-releasing IUDs."
        },
        "videoTutorial": BIO_VIDEOS["zoo_physio"]
    },
    {
        "id": 413,
        "subject": "Zoology",
        "classLevel": "Class 12",
        "chapter": "Evolution",
        "ncertRef": "NCERT Class 12 Biology, Ch 6 — Homologous vs Analogous Organs",
        "pyqTag": "NEET 2022 / 2024 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Flippers of Penguins and Dolphins are an example of:",
        "stem_ta": "பென்குயின்கள் மற்றும் டால்பின்களின் துடுப்புகள் (Flippers) எதற்கு எடுத்துக்காட்டாகும்?",
        "choices": [
            {"letter": "A", "text_en": "Homologous structures resulting from divergent evolution", "text_ta": "விரி பரிணாமத்தினால் உருவான அமைப்பொத்த உறுப்புகள் (Homologous)"},
            {"letter": "B", "text_en": "Analogous structures resulting from convergent evolution", "text_ta": "குவி பரிணாமத்தினால் உருவான செயலொத்த உறுப்புகள் (Analogous / Convergent evolution)"},
            {"letter": "C", "text_en": "Genetic drift (Founder effect)", "text_ta": "மரபியல் நகர்வு (Genetic drift)"},
            {"letter": "D", "text_en": "Industrial melanism", "text_ta": "தொழிற்சாலை மெலானிசம்"}
        ],
        "correct": "B",
        "explanation_en": "Exact NCERT Evolution example: Penguins (birds) and Dolphins (mammals) have anatomically different origins that evolved similar streamlined flippers for swimming in the same aquatic habitat -> ANALOGOUS organs showing CONVERGENT evolution! Other NCERT analogous pairs: Eye of octopus & mammals; Wings of butterfly & birds; Sweet potato (root) & Potato (stem).",
        "explanation_ta": "பென்குயின் (பறவை) மற்றும் டால்பின் (பாலூட்டி) வெவ்வேறு வம்சாவளியைக் கொண்டிருந்தாலும் நீந்துவதற்காக ஒரே மாதிரியான துடுப்புகளைப் பெற்றுள்ளன. இவை குவி பரிணாமத்தால் (Convergent evolution) உருவான செயலொத்த உறுப்புகள் (Analogous structures) ஆகும்!",
        "ncert_key_point": "Homologous = Same anatomy, different function -> Divergent (Whale/Bat/Cheetah/Human forelimbs; Bougainvillea thorn & Cucurbita tendril). Analogous = Different anatomy, same function -> Convergent (Penguin & Dolphin flippers; Sweet potato & Potato).",
        "trap_breakdown": {
            "A": "Students confuse Whale + Bat forelimbs (homologous) with Penguin + Dolphin flippers (analogous)!",
            "C": "Random allele frequency change in small isolated populations.",
            "D": "Natural selection in Biston betularia moths."
        },
        "videoTutorial": BIO_VIDEOS["zoo_physio"]
    },
    {
        "id": 414,
        "subject": "Zoology",
        "classLevel": "Class 12",
        "chapter": "Evolution",
        "ncertRef": "NCERT Class 12 Biology, Ch 6 — Hardy-Weinberg Principle",
        "pyqTag": "NEET Official Numerical PYQ",
        "questionType": "Numerical MCQ",
        "difficulty": "Medium",
        "stem_en": "In a population in Hardy-Weinberg equilibrium, the frequency of the homozygous recessive genotype (aa) is 0.09 (9%). What is the frequency of heterozygous individuals (2pq / Aa) in this population?",
        "stem_ta": "ஹார்டி-வீன்பெர்க் சமநிலையிலுள்ள ஒரு உயிர்த்தொகையில் ஒத்த கருநிலை ஒடுங்கு மரபணுவாக்கத்தின் (aa) நிகழ்வெண் 0.09 (9%) ஆகும். இதில் மாற்றுக் கருநிலை உயிரிகளின் (Aa / 2pq) நிகழ்வெண் என்ன?",
        "choices": [
            {"letter": "A", "text_en": "0.21 (21%)", "text_ta": "0.21 (21%)"},
            {"letter": "B", "text_en": "0.42 (42%)", "text_ta": "0.42 (42%)"},
            {"letter": "C", "text_en": "0.49 (49%)", "text_ta": "0.49 (49%)"},
            {"letter": "D", "text_en": "0.70 (70%)", "text_ta": "0.70 (70%)"}
        ],
        "correct": "B",
        "explanation_en": "Given homozygous recessive genotype frequency q^2 = 0.09 => recessive allele frequency q = sqrt(0.09) = 0.3. Since p + q = 1, dominant allele frequency p = 1 - 0.3 = 0.7. Heterozygous genotype frequency = 2pq = 2 * 0.7 * 0.3 = 0.42 (42%)!",
        "explanation_ta": "கொடுக்கப்பட்டது q^2 = 0.09 => q = sqrt(0.09) = 0.3. p + q = 1 என்பதால் p = 1 - 0.3 = 0.7. மாற்றுக் கருநிலை உயிரிகள் (Aa) = 2pq = 2 * 0.7 * 0.3 = 0.42 (42%)! (சரிபார்ப்பு: 0.49 + 0.42 + 0.09 = 1.00).",
        "ncert_key_point": "Check total: p^2 (0.49) + 2pq (0.42) + q^2 (0.09) = 1.00! Never forget the '2' in 2pq.",
        "trap_breakdown": {
            "A": "0.21 computes pq instead of 2pq!",
            "C": "0.49 is p^2 (homozygous dominant AA), not heterozygotes Aa.",
            "D": "0.70 is dominant allele frequency p, not genotype frequency."
        },
        "videoTutorial": BIO_VIDEOS["zoo_physio"]
    },
    {
        "id": 415,
        "subject": "Zoology",
        "classLevel": "Class 12",
        "chapter": "Human Health and Disease",
        "ncertRef": "NCERT Class 12 Biology, Ch 7 — Immunity, Antibody Types & Malaria",
        "pyqTag": "NEET Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Colostrum, the yellowish fluid secreted by mother during the initial days of lactation, has abundant antibodies of which class to protect the infant (natural passive immunity)?",
        "stem_ta": "பாலூட்டுதலின் தொடக்க நாட்களில் தாயிடமிருந்து சுரக்கும் மஞ்சள் நிற சீம்பாலில் (Colostrum), குழந்தையைப் பாதுகாக்க எந்த வகை எதிர்ப்பொருள் (Antibody) அதிக அளவில் உள்ளது?",
        "choices": [
            {"letter": "A", "text_en": "IgG", "text_ta": "IgG"},
            {"letter": "B", "text_en": "IgA", "text_ta": "IgA"},
            {"letter": "C", "text_en": "IgE", "text_ta": "IgE"},
            {"letter": "D", "text_en": "IgM", "text_ta": "IgM"}
        ],
        "correct": "B",
        "explanation_en": "Exact NCERT Class 12 Human Health & Disease: Colostrum contains abundant IgA antibodies (natural passive immunity). By contrast, IgG crosses the placenta to the foetus during pregnancy, and IgE mediates allergic responses (histamine/serotonin release from mast cells)!",
        "explanation_ta": "சீம்பாலில் (Colostrum) IgA எதிர்ப்பொருள் மிகுதியாக உள்ளது! தாயின் நஞ்சுக்கொடி வழியே கருவிற்குச் செல்வது IgG; ஒவ்வாமை (Allergy) வினைகளில் ஈடுபடுவது IgE ஆகும்.",
        "ncert_key_point": "Colostrum = IgA; Crosses Placenta = IgG; Allergy (Mast cells: Histamine + Serotonin) = IgE.",
        "trap_breakdown": {
            "A": "IgG crosses placenta BEFORE birth, whereas colostrum after birth is rich in IgA.",
            "C": "IgE is involved in allergy.",
            "D": "IgM is the pentameric primary response antibody."
        },
        "videoTutorial": BIO_VIDEOS["zoo_physio"]
    },
    {
        "id": 416,
        "subject": "Zoology",
        "classLevel": "Class 12",
        "chapter": "Human Health and Disease",
        "ncertRef": "NCERT Class 12 Biology, Ch 7 — Drugs and Alcohol Abuse",
        "pyqTag": "NEET 2023 / 2024 High-Frequency PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "Heroin (smack), chemically diacetylmorphine, is obtained by acetylation of morphine extracted from the latex of:",
        "stem_ta": "வேதியியல் ரீதியாக டைஅசிட்டைல்மார்ஃபின் எனப்படும் ஹெராயின் (smack), எந்தத் தாவரத்தின் பாலிலிருந்து (latex) பிரித்தெடுக்கப்படும் மார்ஃபினை அசிட்டைலேற்றம் செய்வதால் கிடைக்கிறது?",
        "choices": [
            {"letter": "A", "text_en": "Cannabis sativa", "text_ta": "கன்னாபிஸ் சட்டைவா (Cannabis sativa)"},
            {"letter": "B", "text_en": "Papaver somniferum (Poppy plant)", "text_ta": "பப்பாவர் சோம்னிஃபெரம் (கசகசா தாவரம் / Poppy plant)"},
            {"letter": "C", "text_en": "Erythroxylum coca", "text_ta": "எரித்ராக்சைலம் கோகா"},
            {"letter": "D", "text_en": "Atropa belladonna", "text_ta": "அட்ரோபா பெல்லடோனா"}
        ],
        "correct": "B",
        "explanation_en": "NCERT Drug Plant Trio (asked nearly every year!): Morphine & Heroin (opioids, CNS depressants binding receptors in CNS & GIT) = latex of Papaver somniferum; Cannabinoids (marijuana, hashish, charas, ganja, affect cardiovascular system) = inflorescences of Cannabis sativa; Cocaine (coka alkaloid, interferes with dopamine transport) = Erythroxylum coca.",
        "explanation_ta": "ஹெராயின் (டைஅசிட்டைல்மார்ஃபின்) என்பது பப்பாவர் சோம்னிஃபெரம் (Papaver somniferum) தாவரத்தின் பாலிலிருந்து பெறப்படும் மார்ஃபினை அசிட்டைலேற்றம் செய்வதால் கிடைக்கிறது.",
        "ncert_key_point": "Papaver somniferum -> Opioids (CNS + GIT receptors); Cannabis sativa -> Cannabinoids (Brain + Cardiovascular); Erythroxylum coca -> Dopamine transport.",
        "trap_breakdown": {
            "A": "Source of cannabinoids.",
            "C": "Source of cocaine (crack).",
            "D": "Has hallucinogenic properties (along with Datura)."
        },
        "videoTutorial": BIO_VIDEOS["zoo_physio"]
    },
    {
        "id": 417,
        "subject": "Zoology",
        "classLevel": "Class 12",
        "chapter": "Biotechnology: Principles and Processes",
        "ncertRef": "NCERT Class 12 Biology, Ch 9 — Gel Electrophoresis & Ethidium Bromide",
        "pyqTag": "NEET 2022 / 2023 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "In agarose gel electrophoresis, separated DNA fragments can be visualised ONLY after staining the DNA with ethidium bromide followed by exposure to UV radiation, appearing as:",
        "stem_ta": "அகரோஸ் இழும மின்னற்பிரிப்பில் (Gel electrophoresis), பிரிக்கப்பட்ட DNA துண்டுகளை எத்திடியம் புரோமைடு சாயமேற்றி புறஊதாக் கதிர்களில் (UV) பார்க்கும்போது எந்த நிறப் பட்டைகளாகத் தெரியும்?",
        "choices": [
            {"letter": "A", "text_en": "Bright blue bands", "text_ta": "பிரகாசமான நீல நிறப் பட்டைகள்"},
            {"letter": "B", "text_en": "Bright orange coloured bands", "text_ta": "பிரகாசமான ஆரஞ்சு நிறப் பட்டைகள் (Bright orange bands)"},
            {"letter": "C", "text_en": "Deep purple bands", "text_ta": "அடர் ஊதா நிறப் பட்டைகள்"},
            {"letter": "D", "text_en": "Emerald green bands", "text_ta": "பச்சை நிறப் பட்டைகள்"}
        ],
        "correct": "B",
        "explanation_en": "Verbatim NCERT Class 12 Biotech Ch 9 line (repeated multiple times in NEET!): DNA stained with Ethidium Bromide (EtBr) and exposed to UV light appears as BRIGHT ORANGE coloured bands! (Cutting out and extracting the DNA bands from the agarose gel piece is called 'Elution').",
        "explanation_ta": "NCERT உயிரித்தொழில்நுட்பப் பாடத்தின் மிகப் புகழ்பெற்ற வரி: எத்திடியம் புரோமைடு சாயமேற்றப்பட்ட DNA-வை UV கதிர்களில் பார்க்கும்போது 'பிரகாசமான ஆரஞ்சு நிறப் பட்டைகளாகத்' (Bright orange bands) தெரியும்!",
        "ncert_key_point": "EtBr + UV light => Bright ORANGE bands! Chilled ethanol => precipitates purified DNA as fine threads (spooling)!",
        "trap_breakdown": {
            "A": "Blue-white screening uses chromogenic substrate with β-galactosidase, not EtBr!",
            "C": "UV light looks violet/purple to the mind's eye, trapping students who haven't memorized NCERT's 'bright orange'!",
            "D": "Incorrect colour."
        },
        "videoTutorial": BIO_VIDEOS["zoo_biotech"]
    },
    {
        "id": 418,
        "subject": "Zoology",
        "classLevel": "Class 12",
        "chapter": "Biotechnology: Principles and Processes",
        "ncertRef": "NCERT Class 12 Biology, Ch 9 — Cloning Vector pBR322 & PCR",
        "pyqTag": "NEET 2023 / 2024 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "In the Polymerase Chain Reaction (PCR), the correct sequence of the three steps in each thermal cycle and the source organism of thermostable Taq polymerase are:",
        "stem_ta": "பாலிமரேஸ் சங்கிலி வினையின் (PCR) ஒவ்வொரு சுழற்சியிலும் நடைபெறும் மூன்று படிகளின் சரியான வரிசை மற்றும் வெப்பம் தாங்கும் Taq பாலிமரேஸ் நொதியின் மூலம் முறையே:",
        "choices": [
            {"letter": "A", "text_en": "Annealing -> Denaturation -> Extension; Escherichia coli", "text_ta": "பதப்படுத்துதல் -> இயல்புதிரிதல் -> நீட்சி; எ.கோலை"},
            {"letter": "B", "text_en": "Denaturation -> Annealing -> Extension; Thermus aquaticus", "text_ta": "இயல்புதிரிதல் (Denaturation) -> இணைதல் (Annealing) -> நீட்சி (Extension); தெர்மஸ் அக்வாட்டிகஸ்"},
            {"letter": "C", "text_en": "Denaturation -> Extension -> Annealing; Thermus aquaticus", "text_ta": "இயல்புதிரிதல் -> நீட்சி -> இணைதல்; தெர்மஸ் அக்வாட்டிகஸ்"},
            {"letter": "D", "text_en": "Extension -> Denaturation -> Annealing; Bacillus thuringiensis", "text_ta": "நீட்சி -> இயல்புதிரிதல் -> இணைதல்; பேசில்லஸ் துரிஞ்சியன்சிஸ்"}
        ],
        "correct": "B",
        "explanation_en": "Each PCR cycle follows D -> A -> E: (1) Denaturation (~94°C, separates dsDNA strands), (2) Primer Annealing (~50-60°C, two sets of primers bind 3' ends), (3) Extension (~72°C, thermostable DNA polymerase isolated from bacterium Thermus aquaticus synthesizes new strands using dNTPs).",
        "explanation_ta": "PCR படிகளின் சரியான வரிசை: (1) இயல்புதிரிதல் (Denaturation), (2) முதன்மை இணைதல் (Annealing), (3) நீட்சி (Extension). இதற்கு தெர்மஸ் அக்வாட்டிகஸ் (Thermus aquaticus) பாக்டீரியத்திலிருந்து பெறப்பட்ட Taq பாலிமரேஸ் பயன்படுகிறது.",
        "ncert_key_point": "Mnemonic 'D-A-E': Denaturation -> Annealing -> Extension; 30 cycles amplify DNA ~1 billion times (2^30)!",
        "trap_breakdown": {
            "A": "Primers cannot anneal until dsDNA is denatured first; E. coli polymerase denatures at 94°C.",
            "C": "Extension cannot happen before primers anneal!",
            "D": "Bacillus thuringiensis is the source of Bt cry genes, not Taq polymerase."
        },
        "videoTutorial": BIO_VIDEOS["zoo_biotech"]
    },
    {
        "id": 419,
        "subject": "Zoology",
        "classLevel": "Class 12",
        "chapter": "Biotechnology and its Applications",
        "ncertRef": "NCERT Class 12 Biology, Ch 10 — Genetically Engineered Insulin & Bt Cotton",
        "pyqTag": "NEET 2022 / 2024 Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Easy",
        "stem_en": "During the maturation of pro-insulin into functional mature insulin in humans, which peptide segment is removed and is NOT present in mature insulin?",
        "stem_ta": "மனிதனில் புரோ-இன்சுலின் (Pro-insulin) முதிர்ந்த செயல்பாட்டு இன்சுலினாக மாறும்போது, நீக்கப்படும் (முதிர்ந்த இன்சுலினில் இல்லாத) பெப்டைடு பகுதி எது?",
        "choices": [
            {"letter": "A", "text_en": "A-peptide chain", "text_ta": "A-பெப்டைடு சங்கிலி"},
            {"letter": "B", "text_en": "B-peptide chain", "text_ta": "B-பெப்டைடு சங்கிலி"},
            {"letter": "C", "text_en": "C-peptide stretch", "text_ta": "C-பெப்டைடு பகுதி (C-peptide)"},
            {"letter": "D", "text_en": "Disulphide bridges between A and B chains", "text_ta": "A மற்றும் B சங்கிலிகளுக்கிடையேயான டைசல்பைடு பிணைப்புகள்"}
        ],
        "correct": "C",
        "explanation_en": "In mammals, insulin is synthesized as a pro-hormone containing A-peptide, B-peptide, and an extra stretch called the C-PEPTIDE. This C-peptide is removed during maturation into mature insulin, leaving only A and B chains linked together by disulphide bridges! (Eli Lilly in 1983 synthesized A and B chains separately in E. coli plasmids and joined them via disulphide bonds).",
        "explanation_ta": "புரோ-இன்சுலினில் A, B மற்றும் கூடுதலாக C-பெப்டைடு உள்ளது. முதிர்ச்சியடையும்போது இந்த C-பெப்டைடு நீக்கப்பட்டு, A மற்றும் B சங்கிலிகள் மட்டும் டைசல்பைடு பிணைப்புகளால் இணைந்த முதிர்ந்த இன்சுலின் உருவாகிறது!",
        "ncert_key_point": "Pro-insulin = A + B + C; Mature insulin = A + B linked by disulphide bridges (C-peptide absent!).",
        "trap_breakdown": {
            "A": "A-chain (21 amino acids) is essential in mature insulin.",
            "B": "B-chain (30 amino acids) is essential in mature insulin.",
            "D": "Disulphide bridges hold mature A and B chains together."
        },
        "videoTutorial": BIO_VIDEOS["zoo_biotech"]
    },
    {
        "id": 420,
        "subject": "Zoology",
        "classLevel": "Class 12",
        "chapter": "Biotechnology and its Applications",
        "ncertRef": "NCERT Class 12 Biology, Ch 10 — Bt Cotton cry Genes & Gene Therapy",
        "pyqTag": "NEET Official PYQ",
        "questionType": "Single Choice MCQ",
        "difficulty": "Medium",
        "stem_en": "In Bt cotton, which specific pair of genes codes for proteins that control COTTON BOLLWORMS, while a different gene controls CORN BORER?",
        "stem_ta": "Bt பருத்தியில், பருத்தி காய்ப்புழுக்களைக் (Cotton bollworms) கட்டுப்படுத்தும் புரதங்களை உருவாக்கும் குறிப்பிட்ட மரபணு இணை எது (மற்றொன்று சோளத் துளைப்பானைக் கட்டுப்படுத்துகிறது)?",
        "choices": [
            {"letter": "A", "text_en": "cryIAc and cryIIAb control cotton bollworms; cryIAb controls corn borer", "text_ta": "cryIAc மற்றும் cryIIAb பருத்தி காய்ப்புழுக்களையும்; cryIAb சோளத் துளைப்பானையும் கட்டுப்படுத்துகின்றன"},
            {"letter": "B", "text_en": "cryIAb and cryIIAb control cotton bollworms; cryIAc controls corn borer", "text_ta": "cryIAb மற்றும் cryIIAb பருத்தி காய்ப்புழுக்களையும்; cryIAc சோளத் துளைப்பானையும் கட்டுப்படுத்துகின்றன"},
            {"letter": "C", "text_en": "cryIAb alone controls cotton bollworms", "text_ta": "cryIAb மட்டுமே பருத்தி காய்ப்புழுக்களைக் கட்டுப்படுத்துகிறது"},
            {"letter": "D", "text_en": "meloidogyne incognitia genes control cotton bollworms", "text_ta": "மெலாய்டோகைன் இன்காக்னிஷியா மரபணுக்கள் கட்டுப்படுத்துகின்றன"}
        ],
        "correct": "A",
        "explanation_en": "Exact NCERT Class 12 Biotech Ch 10 line: 'The proteins encoded by the genes cryIAc and cryIIAb control the cotton bollworms, that of cryIAb controls corn borer.' Notice how easy it is to mix up cryIAc vs cryIAb unless memorized precisely!",
        "explanation_ta": "NCERT-இன் மிக நுணுக்கமான வரி: cryIAc மற்றும் cryIIAb ஆகிய இரண்டு மரபணுக்களும் பருத்தி காய்ப்புழுக்களைக் (Cotton bollworms) கட்டுப்படுத்துகின்றன; cryIAb என்பது சோளத் துளைப்பானைக் (Corn borer) கட்டுப்படுத்துகிறது!",
        "ncert_key_point": "Memory hook: 'c' in cryIAc -> Cotton bollworm (+ cryIIAb); Single 'b' in cryIAb -> corn Borer! And Bt protoxin is activated by ALKALINE pH of insect midgut!",
        "trap_breakdown": {
            "B": "Swaps cryIAc and cryIAb — one of the sharpest NCERT traps in NEET!",
            "C": "cryIAb controls corn borer, not cotton bollworm.",
            "D": "Meloidogyne incognita is a root-knot nematode controlled via RNA interference (RNAi) in tobacco."
        },
        "videoTutorial": BIO_VIDEOS["zoo_biotech"]
    },
]
