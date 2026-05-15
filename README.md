# 📄 Resume Builder Platform

An AI-powered resume builder that lets you **create a resume from scratch** via a form, saves it locally, and can tailor it to any job description — outputting an ATS-ready `main.tex` for Overleaf.

---

## 🚀 What This Does

```
Fill in your details (form)
        ↓
Agent 1 — Builds your base LaTeX resume
        ↓ saved as resumes/base.tex
        ↓
(Optional) Paste a Job Description
        ↓
Agent 2 — Keyword Analyzer
Compares JD vs your base resume
Returns ATS score, matched/missing keywords
        ↓
Agent 3 — ATS Optimizer
Tailors base.tex keywords & title to JD
        ↓
Download main.tex → Paste in Overleaf → Compile → Apply
```

---

## 📁 File Structure

```
project/
├── app.py                ← Streamlit UI (3 pages)
├── agents.py             ← AI agent logic
├── main.tex              ← Template / latest optimized output
├── user_profile.json     ← Your saved form data (auto-created)
├── resumes/
│   └── base.tex          ← Your base resume (auto-generated)
├── .env                  ← Your API key (never commit this!)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### 1. Clone / download the project

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or with `uv`:
```bash
uv sync
```

### 3. Add your API key

Create a `.env` file:
```
NVIDIA_API_KEY=your_key_here
```

Get a **free** key at: https://build.nvidia.com

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📋 How To Use

### Step 1 — Build Your Resume
1. Open the app → go to **Build My Resume**
2. Fill in your: Personal info, Work experience, Education, Skills, Projects
3. Click **Save Progress** anytime to not lose your work
4. Click **Build My Resume** → AI generates your LaTeX resume
5. Download as `base.tex` or `main.tex`

### Step 2 — Optimize for a Job (optional)
1. Go to **Optimize for JD**
2. Paste the full job description
3. Click **Analyze & Build ATS Resume**
4. View your ATS score + missing keywords
5. Download the tailored `main.tex`

### Step 3 — Get Your PDF
1. Go to [overleaf.com](https://overleaf.com)
2. New Project → Blank Project
3. Paste your `main.tex` content
4. Click **Compile** → Download PDF → Apply!

---

## 🤖 The 3 Agents

| Agent | Role |
|---|---|
| **Agent 1** — Base Builder | Takes your form data → formats into ATS-safe LaTeX |
| **Agent 2** — Keyword Analyzer | Compares JD vs resume → ATS score + gap analysis |
| **Agent 3** — ATS Optimizer | Tailors base resume → adds missing keywords naturally |

---

## 💡 Tips for Best Results

- Fill in **all sections** of the form — more data = better resume
- Use **numbers** in bullet points: "Reduced time by 40%" beats "Improved efficiency"
- Paste the **complete** JD — including responsibilities, requirements, and qualifications
- Keep your `base.tex` as your general resume; each JD creates a new `main.tex`

---

## 🔒 Privacy Notes

- All your data stays **local** — `user_profile.json` and `resumes/` folder on your machine
- `.env` is in `.gitignore` — your API key is never committed
- Nothing is sent anywhere except to the NVIDIA API for LLM inference

---

## 📦 Dependencies

- `streamlit` — Web UI
- `openai` — NVIDIA API client (OpenAI-compatible)
- `python-dotenv` — Loads `.env` file

Model: **Llama 3.1 8B Instruct** via NVIDIA's free hosted API

---

## 👤 Author

Built on top of the original [Ap_ATS_Friendly_Resume](https://github.com/arun8nov/Ap_ATS_Friendly_Resume) project.