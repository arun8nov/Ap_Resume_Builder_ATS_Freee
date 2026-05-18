<div align="center">

# 📄 Ap Resume Builder — ATS Free

**AI-powered resume builder that creates ATS-friendly LaTeX resumes from scratch**  
*Fill a form → Build your base resume → Paste any JD → Get an optimized `main.tex` → Compile in Overleaf → Apply*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![NVIDIA API](https://img.shields.io/badge/NVIDIA-Llama%203.1%208B-76B900?logo=nvidia&logoColor=white)](https://build.nvidia.com)
[![LaTeX](https://img.shields.io/badge/Output-LaTeX%20%2F%20Overleaf-008080?logo=latex&logoColor=white)](https://overleaf.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

</div>

---

## 🧠 What This Does

Most resume builders give you a generic template. This platform uses **three AI agents** to:

1. Take your raw experience → format it into a professional, ATS-safe LaTeX resume
2. Compare your resume against any job description → find missing keywords
3. Tailor your resume to that specific JD → output a ready-to-compile `main.tex`

Every output uses a **fixed LaTeX template** (Cormorant Garamond + Charter fonts, blue section headings, clean spacing) — the same format throughout, only content changes.

---

## ✨ Features

- **Zero-template-design hassle** — structured LaTeX preamble is locked in, AI fills the content
- **3-tab form** covering Personal Info, Work Experience, Education, Skills & Projects
- **Save progress** — form data persists to `user_profile.json` locally
- **Base resume** built once, reused across every JD application
- **ATS keyword analysis** with match score (0–100%), matched vs missing keywords
- **JD-optimized output** — AI weaves in missing keywords naturally, never fabricates facts
- **Download `main.tex`** — paste into Overleaf, compile, done
- **Local-first** — your data never leaves your machine except for NVIDIA API inference calls

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                    app.py (Streamlit UI)             │
│  Page 1: Build My Resume  │  Page 2: Optimize for JD │  Page 3: Saved Resume  │
└───────────────┬─────────────────────┬───────────────┘
                │                     │
                ▼                     ▼
         agents.py — 3 AI Agents (NVIDIA API → Llama 3.1 8B)
                │
      ┌─────────┴──────────────────┐
      │                            │
      ▼                            ▼
LATEX_PREAMBLE (fixed)     LLM generates body only
      │                            │
      └──────────┬─────────────────┘
                 ▼
        Assembled main.tex
                 │
                 ▼
       resumes/base.tex  (saved locally)
       main.tex           (downloaded by user)
                 │
                 ▼
        Overleaf → PDF → Apply
```

---

## 🤖 The Three Agents

| Agent | Role | Temperature |
|---|---|---|
| **Agent 1 — Base Builder** | Takes form data → generates LaTeX resume body → assembled with fixed preamble | 0.2 |
| **Agent 2 — Keyword Analyzer** | Compares JD vs resume → ATS score + matched/missing keyword report | 0.3 |
| **Agent 3 — ATS Optimizer** | Rewrites summary & bullets to weave in missing keywords → complete tailored `main.tex` | 0.2 |

**Key design decision:** Agent 1 never generates `\documentclass` or `\usepackage` lines — the Python constant `LATEX_PREAMBLE` handles that. The AI only produces the body between `\begin{document}` and `\end{document}`. This guarantees consistent formatting across every user and every run.

---

## 📁 Project Structure

```
Ap_Resume_Builder_ATS_Freee/
│
├── app.py                 ← Streamlit UI — 3-page navigation
├── agents.py              ← AI agent logic + fixed LaTeX preamble
├── main.tex               ← Template reference + latest optimized output
├── requirements.txt       ← Python dependencies
├── .gitignore             ← Excludes .env, user_profile.json, resumes/
│
├── .env                   ← YOUR API KEY (create this — never commit)
├── user_profile.json      ← Your saved form data (auto-created on save)
└── resumes/
    └── base.tex           ← Your built base resume (auto-created)
```

---

## ⚙️ Installation

### Prerequisites

- Python 3.10 or higher
- A free NVIDIA API key (see below)

### 1 — Clone the repository

```bash
git clone https://github.com/arun8nov/Ap_Resume_Builder_ATS_Freee.git
cd Ap_Resume_Builder_ATS_Freee
```

### 2 — Install dependencies

```bash
pip install -r requirements.txt
```

Or with `uv` (faster):

```bash
pip install uv
uv sync
```

### 3 — Add your NVIDIA API key

Create a `.env` file in the project root:

```bash
NVIDIA_API_KEY=nvapi-xxxxxxxxxxxxxxxxxxxxxxxx
```

> ⚠️ Never commit `.env` to GitHub. It is already in `.gitignore`.

### 4 — Run the app

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`

---

## 🔑 Getting Your Free NVIDIA API Key

This project uses NVIDIA's hosted Llama 3.1 8B model via their free API.

**Step 1** — Go to [build.nvidia.com](https://build.nvidia.com)

**Step 2** — Sign in with Google, GitHub, or create an NVIDIA account

**Step 3** — Click your profile icon → **API Keys**  
Or go directly to: [build.nvidia.com/settings/api-keys](https://build.nvidia.com/settings/api-keys)

**Step 4** — Click **Generate API Key** → copy the key (starts with `nvapi-`)

**Step 5** — Paste it into your `.env` file:

```
NVIDIA_API_KEY=nvapi-your-key-here
```

**Free tier includes:** Generous token allowance for personal use — no credit card required.

---

## 📋 How to Use

### Step 1 — Build Your Base Resume

1. Open the app → click **🏠 Build My Resume** in the sidebar
2. Fill in all tabs:
   - **👤 Personal** — name, email, phone, LinkedIn, GitHub, job title
   - **💼 Experience** — companies, roles, dates, bullet achievements
   - **🎓 Education** — degrees, universities, graduation years, CGPA
   - **🛠️ Skills** — technical skills, tools, soft skills, certifications
   - **🚀 Projects** — project names, tech stack, GitHub URLs, descriptions
3. Click **💾 Save Progress** — saves to `user_profile.json` (never lost)
4. Click **🚀 Build My Resume** — AI generates your LaTeX resume
5. Download `base.tex` or `main.tex`

> 💡 **Tip:** Use numbers everywhere — "reduced time by 40%" beats "improved efficiency"

### Step 2 — Optimize for a Job Description

1. Click **🎯 Optimize for JD** in the sidebar
2. Paste the **full job description** (including requirements, responsibilities, qualifications)
3. Click **🔍 Keyword Analysis Only** to see your ATS score first
4. Click **🚀 Analyze & Build ATS Resume** to generate the tailored resume
5. View your ATS score, matched keywords, missing keywords
6. Download the tailored `main.tex`

> 💡 **Tip:** Paste the complete JD — the more text, the better the keyword extraction

### Step 3 — Get Your PDF via Overleaf

1. Go to [overleaf.com](https://overleaf.com) → **New Project** → **Blank Project**
2. Delete the default content
3. Paste your downloaded `main.tex` content
4. Click **Compile** (green button)
5. Click **Download PDF**
6. Apply to jobs!

---

## 📄 LaTeX Template Format

Every resume generated uses this exact fixed structure — the design never changes, only the content:

```
Header (name, title, contact links)
    ↓
Summary (2–3 sentences, key terms bolded)
    ↓
Technical Skills (Languages & Databases | Tools | Core Competencies)
    ↓
Work Experience (Company → Role → Bullet achievements)
    ↓
Projects (Name | Tech stack | GitHub link | Impact)
    ↓
Education (Degree | University | Year | CGPA)
    ↓
Certifications (Name | Issuer | Year)
```

**Fonts:** Cormorant Garamond + Charter  
**Colors:** `headingblue` (#0E5484) for section headings, `airforceblue` for rules  
**ATS-safe:** No tables for critical content, no text in graphics, Unicode-mapped glyphs (`\pdfgentounicode=1`)

---

## 💡 Tips for Best ATS Score

| ❌ Don't | ✅ Do |
|---|---|
| "Improved reports" | "Reduced reporting time by 40% using Python automation" |
| "Worked on ML models" | "Built Random Forest classifier achieving 94% accuracy on 500K records" |
| Paste only the job title | Paste the complete JD including all requirements |
| Leave skills vague | List specific tools: "Power BI, DAX, Tableau, SQL Server" |
| Skip projects section | Include 2–3 projects with GitHub links and measurable outcomes |

---

## 🔒 Privacy & Data

- **All your data stays local** — `user_profile.json` and `resumes/` folder on your machine only
- **The only external call** is to the NVIDIA API for LLM inference (your resume content is sent)
- **`.env` is gitignored** — your API key is never committed
- **NVIDIA's free tier** does not train on your data (check [NVIDIA's privacy policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) for current terms)

---

## 📦 Dependencies

```
streamlit>=1.35.0       # Web UI
openai>=1.30.0          # NVIDIA API client (OpenAI-compatible)
python-dotenv>=1.0.0    # Loads .env file
```

**Model:** `meta/llama-3.1-8b-instruct` via NVIDIA's hosted inference API  
**API base URL:** `https://integrate.api.nvidia.com/v1`

---

## 🛠️ Future Improvements

- [ ] PDF export directly from the app (no Overleaf needed)
- [ ] Multi-user support with SQLite session isolation
- [ ] JD history — view and re-download past optimized resumes
- [ ] LinkedIn profile parser — auto-fill the form from a LinkedIn URL
- [ ] Multiple LaTeX templates to choose from
- [ ] AI bullet point enhancer — improve existing bullets with one click
- [ ] ATS score dashboard across multiple job applications
- [ ] Dark mode UI

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

1. Fork the repository
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push and open a PR

---

## ⭐ Support

If this project helped you land an interview:

- ⭐ **Star** the repository
- 🍴 **Fork** and adapt it for your needs
- 📣 **Share** with others who are job hunting

---

## 👤 Author

**Arunprakash B**  
GitHub: [@arun8nov](https://github.com/arun8nov)  
LinkedIn: [linkedin.com/in/arun8nov](https://linkedin.com/in/arun8nov)  
Portfolio: [arun8nov.notion.site](https://arun8nov.notion.site/Hey-there-I-am-Arunprakash-B-223fe4a17f8a80faa5abee1f246a06f1)

---

<div align="center">
Built with ❤️ in Chennai, India · Powered by NVIDIA Llama 3.1 · Compiled with Overleaf
</div>