# Tamil Nadu NEET-UG Mastery Hub & Bilingual Gemini AI Coach

A mobile-first **NEET-UG OMR Mock Exam Platform, Dual Score Tracker, Tamil Nadu Reference Hub, and Multilingual (Tamil + English) Gemini AI Coach** built for medical aspirants preparing in Tamil Nadu, India.

- **Live Web App (Custom Domain):** `https://neet.memnos.net`
- **GitHub Pages Mirror:** `https://thameema.github.io/neet-prep/`

## Key Capabilities

- **Mobile-First Phone & Tablet Experience (PWA Ready):**
  - Thumb-friendly 5-tab bottom navigation (`Question`, `OMR (x/y)`, `AI Coach`, `Scores`, `TN Guide`) on Android & iPhone (`<= 960px`), expanding automatically into a 3-column desktop exam workstation on laptops.
  - 50px touch-target OMR bubbles, safe-area inset support, zero horizontal scroll, 1-tap **Copy WhatsApp Score Report**, and `manifest.json` Add-to-Home-Screen installability.
- **Authentic NTA NEET-UG Exam Pattern:** Strict **+4 / -1 / 0** OMR bubble marking across all four official subjects (**Physics, Chemistry, Botany, Zoology** — aligned to NTA's current 180 compulsory questions in 180 minutes structure with optional Section B removed).
- **80 Mathematically & Scientifically Verified Bilingual Questions:** Every question, option, step-by-step NCERT derivation, key takeaway, and `-1` negative-mark distractor trap is verified (`scripts/compile_and_verify.py`) and available in **English**, **தமிழ் (Tamil)**, and side-by-side **EN + தமிழ்**.
- **8 Repeatable Mock & Practice Modules:**
  1. `full_mock_1` — 80-Question Full 4-Subject OMR Mock Exam (Projected `/720` + TN Medical College Cutoff Evaluation)
  2. `mini_mock_pyq` — 40-Question High-Yield NEET PYQ Mock Exam
  3. `random_daily_sprint` — Dynamic Randomised 20-Question Sprint (fresh `5P + 5C + 5B + 5Z` paper on every retake)
  4. `practice_physics`, `practice_chemistry`, `practice_botany`, `practice_zoology` — Instant-feedback Guided Practice Modes
  5. `mistake_bank` — Adaptive Mistake & Negative-Mark Recovery Bank
- **3-Tier Hybrid Hosting & Multilingual Gemini AI Coach (`English`, `தமிழ்`, & `Tanglish`):**
  1. **Live Server / Cloudflare HTTPS Tunnel (`neet_server.py`):** Syncs scores centrally into SQLite (`neet_data.db`) + `student_score_ledger.json` and runs live Gemini coaching (`GEMINI_API_KEY` or local `agy` Gemini CLI). Override the backend URL anytime via `?backend=https://your-tunnel.trycloudflare.com`.
  2. **Direct Browser Gemini Mode:** Optional per-device Gemini API key in the Profile modal (`localStorage` only, never committed) for serverless live Gemini on GitHub Pages.
  3. **24/7 Standalone GitHub Pages Mode:** Even if no tunnel or API key is active, all 8 mock/practice exams, local score tracking, and the built-in **Bilingual NCERT Deterministic Coach** work 100% standalone in the browser.

## Running Locally

```bash
# 1. Verify and compile the 80 bilingual NEET questions
python3 scripts/compile_and_verify.py

# 2. Launch the local server + mentor ledger on http://localhost:8090
python3 neet_server.py

# 3. Run the automated E2E self-exam & bilingual coach test suite
python3 tests/test_and_self_exam.py
```

## Optional Live Tunnel or Cloud Deployment

1. **Cloudflare HTTPS Tunnel from Mac (Connects GitHub Pages to local Gemini & Mentor DB):**
   ```bash
   cloudflared tunnel --no-autoupdate --url http://localhost:8090
   ```
2. **24/7 Cloud Backend (Render / Railway / Cloud Run / Docker):**
   Deploy using the included `Dockerfile` or `render.yaml` and set `GEMINI_API_KEY` in the cloud dashboard's secret environment variables.
