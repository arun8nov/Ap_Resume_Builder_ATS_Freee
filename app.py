import streamlit as st
import os
import json
from agents import (
    agent_build_base_resume,
    agent_keyword_analyzer,
    agent_ats_optimizer,
    load_user_data,
    save_user_data,
    load_base_resume,
)

# ─────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Resume Builder",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.main-header {
    font-size: 2rem;
    font-weight: 700;
    background: linear-gradient(90deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.2rem;
}
.sub-header { color: #888; font-size: 0.95rem; margin-bottom: 1.5rem; }
.section-label {
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #888;
    margin-top: 1rem;
    margin-bottom: 0.3rem;
}
.step-badge {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 700;
    background: #667eea22;
    color: #667eea;
    margin-right: 6px;
}
.info-box {
    background: #1e1e2e;
    border-radius: 8px;
    padding: 0.8rem 1rem;
    border-left: 3px solid #667eea;
    font-size: 0.85rem;
    margin-bottom: 0.8rem;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# SIDEBAR — NAVIGATION
# ─────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📄 Resume Builder")
    st.markdown("---")
    page = st.radio(
        "Navigation",
        ["🏠 Build My Resume", "🎯 Optimize for JD", "📁 My Saved Resume"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    base = load_base_resume()
    if base:
        st.success("✅ Base resume saved")
        st.caption(f"{len(base):,} chars · ready to optimize")
    else:
        st.warning("⚠️ No base resume yet")
        st.caption("Complete Step 1 first")

    st.markdown("---")
    st.markdown("### How it works")
    st.markdown("""
**Step 1** — Fill in your info  
AI builds a clean LaTeX resume  
Saved as `base.tex` locally  

**Step 2** *(optional)*  
Paste any job description  
AI tailors your base resume  
Download as `main.tex` for Overleaf  
""")
    st.caption("Model: Llama 3.1 8B via NVIDIA API")

# ─────────────────────────────────────────────────────────
# PAGE 1 — BUILD MY RESUME
# ─────────────────────────────────────────────────────────
if "Build" in page:
    st.markdown('<div class="main-header">📄 Build Your Resume</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Fill in your details — AI will format everything into a clean ATS-friendly LaTeX resume</div>', unsafe_allow_html=True)

    # Pre-fill from saved data
    saved = load_user_data()

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "👤 Personal", "💼 Experience", "🎓 Education", "🛠️ Skills", "🚀 Projects"
    ])

    with tab1:
        st.markdown("### Personal Information")
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full Name *", value=saved.get("full_name", ""), placeholder="Arunprakash B")
            email = st.text_input("Email *", value=saved.get("email", ""), placeholder="you@email.com")
            phone = st.text_input("Phone", value=saved.get("phone", ""), placeholder="+91 98765 43210")
        with col2:
            location = st.text_input("Location", value=saved.get("location", ""), placeholder="Chennai, Tamil Nadu")
            linkedin = st.text_input("LinkedIn URL", value=saved.get("linkedin", ""), placeholder="linkedin.com/in/yourname")
            github = st.text_input("GitHub URL", value=saved.get("github", ""), placeholder="github.com/yourname")

        job_title = st.text_input("Target Job Title", value=saved.get("job_title", ""), placeholder="Data Scientist | ML Engineer | Data Analyst")
        summary = st.text_area(
            "Professional Summary (optional — AI will generate one if blank)",
            value=saved.get("summary", ""),
            height=90,
            placeholder="Brief 2-3 sentence overview of your profile..."
        )

    with tab2:
        st.markdown("### Work Experience")
        st.caption("Add your most recent jobs first. Use numbers in bullet points where possible.")

        num_exp = st.number_input("Number of positions", min_value=1, max_value=6, value=max(1, len(saved.get("experience", []))))
        experience = []
        for i in range(int(num_exp)):
            saved_exp = saved.get("experience", [{}] * int(num_exp))
            ex = saved_exp[i] if i < len(saved_exp) else {}
            with st.expander(f"Position {i+1}", expanded=(i == 0)):
                c1, c2 = st.columns(2)
                with c1:
                    title = st.text_input(f"Job Title", value=ex.get("title", ""), key=f"etitle_{i}", placeholder="Data Analyst")
                    company = st.text_input(f"Company", value=ex.get("company", ""), key=f"ecomp_{i}", placeholder="Tech Corp Pvt Ltd")
                with c2:
                    duration = st.text_input(f"Duration", value=ex.get("duration", ""), key=f"edur_{i}", placeholder="Jan 2022 – Present")
                    location_e = st.text_input(f"Location", value=ex.get("location", ""), key=f"eloc_{i}", placeholder="Chennai, IN")
                bullets = st.text_area(
                    "Key achievements (one per line — use numbers!)",
                    value="\n".join(ex.get("bullets", [])),
                    key=f"ebullets_{i}",
                    height=120,
                    placeholder="Built dashboard reducing report time by 40%\nAnalyzed 2M+ records using Python and SQL\nLed team of 3 analysts"
                )
                experience.append({
                    "title": title, "company": company,
                    "duration": duration, "location": location_e,
                    "bullets": [b.strip() for b in bullets.split("\n") if b.strip()]
                })

    with tab3:
        st.markdown("### Education")
        num_edu = st.number_input("Number of degrees", min_value=1, max_value=4, value=max(1, len(saved.get("education", []))))
        education = []
        for i in range(int(num_edu)):
            saved_edu = saved.get("education", [{}] * int(num_edu))
            ed = saved_edu[i] if i < len(saved_edu) else {}
            with st.expander(f"Degree {i+1}", expanded=(i == 0)):
                c1, c2 = st.columns(2)
                with c1:
                    degree = st.text_input("Degree", value=ed.get("degree", ""), key=f"deg_{i}", placeholder="B.E. Computer Science")
                    university = st.text_input("University/College", value=ed.get("university", ""), key=f"uni_{i}", placeholder="Anna University")
                with c2:
                    grad_year = st.text_input("Graduation Year", value=ed.get("grad_year", ""), key=f"gyear_{i}", placeholder="2022")
                    cgpa = st.text_input("CGPA / Percentage", value=ed.get("cgpa", ""), key=f"cgpa_{i}", placeholder="8.4 / 10")
                education.append({
                    "degree": degree, "university": university,
                    "grad_year": grad_year, "cgpa": cgpa
                })

    with tab4:
        st.markdown("### Skills")
        col1, col2 = st.columns(2)
        with col1:
            tech_skills = st.text_area(
                "Technical Skills (comma-separated)",
                value=", ".join(saved.get("tech_skills", [])),
                height=100,
                placeholder="Python, SQL, Power BI, Tableau, Excel, Machine Learning, TensorFlow"
            )
            tools = st.text_area(
                "Tools & Platforms",
                value=", ".join(saved.get("tools", [])),
                height=80,
                placeholder="Git, Docker, AWS, Jupyter, VS Code, Jira"
            )
        with col2:
            soft_skills = st.text_area(
                "Soft Skills",
                value=", ".join(saved.get("soft_skills", [])),
                height=80,
                placeholder="Team leadership, Problem solving, Communication"
            )
            certifications = st.text_area(
                "Certifications (one per line)",
                value="\n".join(saved.get("certifications", [])),
                height=100,
                placeholder="AWS Certified Data Analytics – Specialty (2024)\nGoogle Data Analytics Professional Certificate"
            )

    with tab5:
        st.markdown("### Projects")
        num_proj = st.number_input("Number of projects", min_value=0, max_value=6, value=max(1, len(saved.get("projects", []))))
        projects = []
        for i in range(int(num_proj)):
            saved_proj = saved.get("projects", [{}] * int(num_proj))
            pr = saved_proj[i] if i < len(saved_proj) else {}
            with st.expander(f"Project {i+1}", expanded=(i == 0)):
                c1, c2 = st.columns(2)
                with c1:
                    proj_name = st.text_input("Project Name", value=pr.get("name", ""), key=f"pname_{i}", placeholder="Sales Prediction Dashboard")
                    tech_used = st.text_input("Technologies Used", value=pr.get("tech", ""), key=f"ptech_{i}", placeholder="Python, Scikit-learn, Streamlit")
                with c2:
                    proj_url = st.text_input("GitHub/Live URL (optional)", value=pr.get("url", ""), key=f"purl_{i}", placeholder="github.com/you/project")
                    proj_year = st.text_input("Year", value=pr.get("year", ""), key=f"pyear_{i}", placeholder="2024")
                proj_desc = st.text_area(
                    "Description (2-3 bullets)",
                    value="\n".join(pr.get("description", [])),
                    key=f"pdesc_{i}",
                    height=90,
                    placeholder="Built ML model with 94% accuracy predicting quarterly sales\nDeployed via Streamlit with real-time CSV upload support"
                )
                projects.append({
                    "name": proj_name, "tech": tech_used,
                    "url": proj_url, "year": proj_year,
                    "description": [d.strip() for d in proj_desc.split("\n") if d.strip()]
                })

    st.markdown("---")
    col1, col2 = st.columns([3, 1])
    with col1:
        build_btn = st.button("🚀 Build My Resume", type="primary", use_container_width=True,
                              disabled=not (full_name and email))
    with col2:
        if st.button("💾 Save Progress", use_container_width=True):
            data = {
                "full_name": full_name, "email": email, "phone": phone,
                "location": location, "linkedin": linkedin, "github": github,
                "job_title": job_title, "summary": summary,
                "experience": experience, "education": education,
                "tech_skills": [s.strip() for s in tech_skills.split(",") if s.strip()],
                "tools": [s.strip() for s in tools.split(",") if s.strip()],
                "soft_skills": [s.strip() for s in soft_skills.split(",") if s.strip()],
                "certifications": [c.strip() for c in certifications.split("\n") if c.strip()],
                "projects": projects
            }
            save_user_data(data)
            st.success("✅ Progress saved!")

    if build_btn:
        user_data = {
            "full_name": full_name, "email": email, "phone": phone,
            "location": location, "linkedin": linkedin, "github": github,
            "job_title": job_title, "summary": summary,
            "experience": experience, "education": education,
            "tech_skills": [s.strip() for s in tech_skills.split(",") if s.strip()],
            "tools": [s.strip() for s in tools.split(",") if s.strip()],
            "soft_skills": [s.strip() for s in soft_skills.split(",") if s.strip()],
            "certifications": [c.strip() for c in certifications.split("\n") if c.strip()],
            "projects": projects
        }
        save_user_data(user_data)

        with st.spinner("🤖 AI is building your LaTeX resume..."):
            result = agent_build_base_resume(user_data)

        if result.get("latex"):
            # Save as base.tex
            os.makedirs("resumes", exist_ok=True)
            with open("resumes/base.tex", "w", encoding="utf-8") as f:
                f.write(result["latex"])

            st.success("✅ Base resume built and saved as `resumes/base.tex`!")
            st.markdown("### Preview")
            st.code(result["latex"], language="latex")

            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    "⬇️ Download base.tex",
                    data=result["latex"],
                    file_name="base.tex",
                    mime="text/plain",
                    type="primary",
                    use_container_width=True
                )
            with col2:
                st.download_button(
                    "⬇️ Download main.tex (Overleaf ready)",
                    data=result["latex"],
                    file_name="main.tex",
                    mime="text/plain",
                    use_container_width=True
                )
            st.info("💡 Paste this into Overleaf → Compile → Download PDF → Apply!")
        else:
            st.error(f"Build failed: {result.get('error', 'Unknown error')}")

# ─────────────────────────────────────────────────────────
# PAGE 2 — OPTIMIZE FOR JD
# ─────────────────────────────────────────────────────────
elif "Optimize" in page:
    st.markdown('<div class="main-header">🎯 Optimize for Job Description</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Paste a JD — AI tailors your base resume, adds missing keywords, and outputs an ATS-ready main.tex</div>', unsafe_allow_html=True)

    base = load_base_resume()
    if not base:
        st.error("⚠️ You need to build your base resume first. Go to **Build My Resume**.")
        st.stop()

    st.markdown(f"✅ Base resume loaded — `{len(base):,}` characters")
    st.markdown("---")

    col1, col2 = st.columns([3, 1])
    with col1:
        jd_text = st.text_area(
            "Paste the full Job Description",
            height=300,
            placeholder="Paste the complete job description here — include responsibilities, requirements, and qualifications sections for best results...",
            key="jd_input"
        )
    with col2:
        st.markdown("#### 💡 Tips")
        st.markdown("- Paste the **full** JD\n- Include all sections\n- More detail = better match")
        word_count = len(jd_text.split()) if jd_text else 0
        st.metric("Words", word_count)
        if word_count > 100:
            st.success("Great length ✅")
        elif word_count > 30:
            st.warning("Add more detail")
        elif word_count > 0:
            st.error("Too short")

    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    with col1:
        run_btn = st.button(
            "🚀 Analyze & Build ATS Resume",
            type="primary",
            use_container_width=True,
            disabled=not jd_text.strip()
        )
    with col2:
        analyze_only = st.button(
            "🔍 Keyword Analysis Only",
            use_container_width=True,
            disabled=not jd_text.strip()
        )

    if analyze_only or run_btn:
        if not jd_text.strip():
            st.warning("Please paste a job description first.")
            st.stop()

        st.markdown("---")
        st.markdown("## 🤖 Agent 1 — Keyword Analysis")

        with st.spinner("Analyzing JD vs your resume..."):
            r1 = agent_keyword_analyzer(jd_text, base)
            st.session_state["kw_analysis"] = r1["raw"]
            st.session_state["jd_snap"] = jd_text

        # Show score
        raw = r1["raw"]
        import re
        score_val = None
        for line in raw.split("\n"):
            if "MATCH SCORE" in line.upper():
                nums = re.findall(r'\d+', line)
                if nums:
                    score_val = int(nums[0])
                    break

        if score_val is not None:
            s1, s2, s3 = st.columns(3)
            with s1:
                color = "#2ecc71" if score_val >= 70 else "#f39c12" if score_val >= 40 else "#e74c3c"
                label = "Strong ✅" if score_val >= 70 else "Needs Work ⚠️" if score_val >= 40 else "Low Match ❌"
                st.markdown(f"""
<div style="text-align:center;padding:1rem;background:#1e1e2e;border-radius:12px;">
<div style="font-size:0.85rem;color:#888;">ATS Match Score</div>
<div style="font-size:3rem;font-weight:800;color:{color};">{score_val}%</div>
<div style="color:{color};font-size:0.85rem;">{label}</div>
</div>""", unsafe_allow_html=True)

        st.markdown("#### 📊 Full Analysis")
        st.markdown(raw)
        st.download_button("⬇️ Download Analysis", data=raw, file_name="ats_analysis.txt", mime="text/plain")

    if run_btn and "kw_analysis" in st.session_state:
        st.markdown("---")
        st.markdown("## 🤖 Agent 2 — Building ATS-Optimized Resume")

        with st.spinner("Tailoring your resume for this specific JD..."):
            r2 = agent_ats_optimizer(
                st.session_state["jd_snap"],
                base,
                st.session_state["kw_analysis"]
            )

        if r2.get("latex"):
            final = r2["latex"]
            st.success("✅ ATS-optimized resume ready!")

            # Auto-save as main.tex
            with open("main.tex", "w", encoding="utf-8") as f:
                f.write(final)

            st.markdown("### ✅ Your Optimized Resume")
            st.code(final, language="latex")

            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    "⬇️ Download main.tex",
                    data=final,
                    file_name="main.tex",
                    mime="text/plain",
                    type="primary",
                    use_container_width=True
                )
            with col2:
                if st.button("💾 Save as main.tex locally", use_container_width=True):
                    with open("main.tex", "w", encoding="utf-8") as f:
                        f.write(final)
                    st.success("✅ Saved as main.tex!")

            st.info("💡 **Next step:** Copy the LaTeX above → Open Overleaf → New project → Paste → Compile → Download PDF → Apply!")
        else:
            st.error(f"Optimization failed: {r2.get('error')}")

# ─────────────────────────────────────────────────────────
# PAGE 3 — MY SAVED RESUME
# ─────────────────────────────────────────────────────────
elif "Saved" in page:
    st.markdown('<div class="main-header">📁 My Saved Resume</div>', unsafe_allow_html=True)

    base = load_base_resume()
    if base:
        st.success(f"✅ Base resume found — {len(base):,} characters")
        st.markdown("### base.tex")
        st.code(base, language="latex")
        st.download_button(
            "⬇️ Download base.tex",
            data=base,
            file_name="base.tex",
            mime="text/plain",
            type="primary"
        )
    else:
        st.warning("No base resume found. Build one first in **Build My Resume**.")

    # Show main.tex if exists
    if os.path.exists("main.tex"):
        with open("main.tex", "r", encoding="utf-8") as f:
            main_tex = f.read()
        st.markdown("---")
        st.markdown("### Latest main.tex (last optimized)")
        st.code(main_tex, language="latex")
        st.download_button(
            "⬇️ Download main.tex",
            data=main_tex,
            file_name="main.tex",
            mime="text/plain"
        )

    # Show saved user data
    saved = load_user_data()
    if saved:
        st.markdown("---")
        st.markdown("### Saved Profile Data")
        with st.expander("View raw JSON"):
            st.json(saved)