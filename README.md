# 📄 AI Resume Builder Platform

An AI-powered ATS Resume Builder that helps you:

✅ Create a resume from scratch using a simple form  
✅ Save your resume locally  
✅ Analyze any Job Description (JD)  
✅ Generate an ATS-optimized LaTeX resume automatically  
✅ Export `main.tex` for Overleaf PDF compilation  

---

# 🚀 Features

- Build resumes using a Streamlit form
- Auto-generate ATS-friendly LaTeX resumes
- Save user data locally
- Analyze Job Descriptions using AI
- Compare resume vs JD keywords
- Get ATS score + missing keywords
- Generate optimized resumes for each job
- Download ready-to-use `main.tex`
- Uses NVIDIA hosted Llama 3.1 model

---

# 🧠 Workflow

```text
Fill Resume Form
        ↓
Agent 1 → Build Base Resume
        ↓
Saved as resumes/base.tex
        ↓
(Optional) Paste Job Description
        ↓
Agent 2 → Keyword Analyzer
        ↓
ATS Score + Missing Keywords
        ↓
Agent 3 → ATS Optimizer
        ↓
Generate Optimized main.tex
        ↓
Paste into Overleaf → Compile PDF
```

---

# 📁 Project Structure

```text
project/
├── app.py
├── agents.py
├── main.tex
├── user_profile.json
├── resumes/
│   └── base.tex
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/arun8nov/Ap_Resume_Builder_ATS_Freee.git
cd Ap_Resume_Builder_ATS_Freee
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Get NVIDIA API Key (Free)

This project uses NVIDIA hosted AI models.

## Steps to Get Free NVIDIA API Key

### 1. Open NVIDIA Build Website

Go to:

https://build.nvidia.com

---

### 2. Sign In

Login using:

- Google
- GitHub
- NVIDIA account

---

### 3. Open API Keys Section

After login:

- Click your profile icon
- Go to **API Keys**

OR directly visit:

https://build.nvidia.com/settings/api-keys

---

### 4. Generate API Key

- Click **Generate API Key**
- Copy the generated key

---

### 5. Create `.env` File

Inside your project folder create:

```env
NVIDIA_API_KEY=your_api_key_here
```

Example:

```env
NVIDIA_API_KEY=nvapi-xxxxxxxxxxxxxxxx
```

⚠️ Never share or upload your API key publicly.

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📋 How to Use

# Step 1 — Build Your Resume

1. Open the Streamlit app
2. Go to **Build My Resume**
3. Fill in:
   - Personal Information
   - Work Experience
   - Education
   - Skills
   - Projects
4. Click **Save Progress**
5. Click **Build My Resume**

The AI generates:

- `resumes/base.tex`
- `main.tex`

---

# Step 2 — Optimize for Job Description

1. Open **Optimize for JD**
2. Paste complete Job Description
3. Click:

```text
Analyze & Build ATS Resume
```

The system will:

- Compare resume vs JD
- Calculate ATS score
- Find missing keywords
- Generate optimized resume

---

# Step 3 — Generate PDF using Overleaf

1. Open https://overleaf.com
2. Create **Blank Project**
3. Replace content with generated `main.tex`
4. Click **Compile**
5. Download PDF

---

# 🤖 AI Agents

| Agent | Function |
|---|---|
| Agent 1 — Base Builder | Creates ATS-friendly LaTeX resume |
| Agent 2 — Keyword Analyzer | Analyzes JD vs Resume |
| Agent 3 — ATS Optimizer | Tailors resume for ATS matching |

---

# 💡 Tips for Better ATS Score

- Add measurable achievements
- Use action verbs
- Include tools & technologies
- Paste full job description
- Keep resume keyword rich
- Add projects with outcomes

Example:

❌ Improved reports  
✅ Reduced reporting time by 40% using Python automation

---

# 🔒 Privacy

- All data is stored locally
- Resume data saved in:
  - `user_profile.json`
  - `resumes/`
- `.env` file is ignored using `.gitignore`
- Only AI requests are sent to NVIDIA API

---

# 📦 Technologies Used

| Technology | Usage |
|---|---|
| Python | Backend |
| Streamlit | Web UI |
| OpenAI SDK | NVIDIA API Client |
| python-dotenv | Environment Variables |
| LaTeX | Resume Generation |

---

# 🧠 AI Model Used

```text
Meta Llama 3.1 8B Instruct
```

Hosted via NVIDIA API.

---

# 📸 Recommended Workflow

```text
Create Base Resume
        ↓
Save base.tex
        ↓
Paste Job Description
        ↓
Generate ATS Resume
        ↓
Download main.tex
        ↓
Compile in Overleaf
        ↓
Apply for Jobs
```

---

# 🛠 Future Improvements

- PDF export directly from app
- Multiple resume templates
- Resume scoring dashboard
- LinkedIn profile parser
- AI bullet point enhancement
- Dark mode UI
- Multi-language support

---

# ⭐ Support

If you found this project useful:

- Star the repository
- Fork the project
- Share with others

---

# 🔗 GitHub Repository

https://github.com/arun8nov/Ap_Resume_Builder_ATS_Freee

---

# 👤 Author

**Arunprakash B**

GitHub: https://github.com/arun8nov

---
