import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Lamana Mulaffer | Resume",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
h1, h2, h3 { font-family: 'Playfair Display', serif; }

.hero-name {
    font-family: 'Playfair Display', serif;
    font-size: 3.2rem;
    font-weight: 700;
    letter-spacing: -1px;
    line-height: 1.1;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-title {
    font-size: 1.1rem;
    font-weight: 300;
    color: #6b7280;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 4px;
}
.section-chip {
    display: inline-block;
    background: #0f3460;
    color: white;
    padding: 4px 14px;
    border-radius: 20px;
    font-size: 0.72rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 500;
    margin-bottom: 12px;
}
.timeline-dot {
    width: 10px; height: 10px;
    background: #0f3460;
    border-radius: 50%;
    display: inline-block;
    margin-right: 8px;
}
.tag {
    display: inline-block;
    background: #f3f4f6;
    color: #374151;
    border-radius: 6px;
    padding: 2px 10px;
    font-size: 0.8rem;
    margin: 2px;
}
.sidebar-label {
    font-size: 0.7rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #9ca3af;
    font-weight: 500;
}
.award-badge {
    background: linear-gradient(135deg, #fef3c7, #fde68a);
    border-left: 3px solid #f59e0b;
    border-radius: 6px;
    padding: 10px 14px;
    margin-bottom: 10px;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

# ── Data ──────────────────────────────────────────────────────────────────────

PROFILE = {
    "name": "Lamana Mulaffer",
    "title": "AI Leader · MMA Candidate @ Rotman · Lead Data Scientist",
    "email": "lamana.mulaffer@rotman.utoronto.ca",
    "linkedin": "linkedin.com/in/lamanamulaffer",
    "phone": "(902) 471-9486",
    "location": "Toronto, ON",
    "summary": (
        "AI leader with 9+ years of experience delivering enterprise-scale and high-growth "
        "analytics and machine learning initiatives. Skilled in building and mentoring teams, "
        "shaping technical strategy, and embedding AI into business models to drive innovation "
        "and measurable impact. Currently deepening expertise in management analytics at "
        "Rotman School of Management, University of Toronto."
    ),
}

EXPERIENCE = [
    {
        "role": "Lead Data Scientist",
        "company": "IBM",
        "period": "2022 – Present",
        "start": 2022, "end": 2025,
        "location": "Toronto, Canada",
        "highlights": [
            "Directed data and AI projects for Fortune 500 energy and telecom clients, leading cross-functional teams of 5–10 members and designing technical roadmaps aligned with strategic business outcomes.",
            "Led design and implementation of scalable ETL pipelines with AWS Glue, Lambda, and Redshift, leveraging raw, silver, and gold layers to enable near-real-time ML and analytics on large datasets.",
            "Mentored and developed data science teams through collaborative workshops, fostering growth and strengthening technical skills.",
            "Improved ML model accuracy by 15–20% and maintained production systems to ensure sustained business impact.",
        ],
        "tags": ["AWS SageMaker", "Redshift", "ETL", "Team Leadership", "Python", "ML"],
    },
    {
        "role": "Senior Data Scientist",
        "company": "Octave",
        "period": "2020 – 2021",
        "start": 2020, "end": 2022,
        "location": "Colombo, Sri Lanka",
        "highlights": [
            "Led teams of 3–5 data engineers and scientists to deliver analytics solutions, driving ~$55K USD annual margin gain and a 10% increase in ad ROI through supply chain and marketing optimization.",
            "Championed AI literacy, elevating business stakeholders from foundational understanding to practical application of AI in decision-making.",
            "Directed development of scalable, production-ready models and pipelines using CI/CD, aligning technical execution with business strategy.",
        ],
        "tags": ["CI/CD", "Supply Chain Analytics", "Marketing Optimization", "AI Strategy"],
    },
    {
        "role": "Senior Consultant – Data Science",
        "company": "Stax Inc",
        "period": "2019 – 2020",
        "start": 2019, "end": 2020,
        "location": "Colombo, Sri Lanka",
        "highlights": [
            "Led development of an NLP-driven social media analytics platform, delivered as a value-added consulting service, increasing revenue per project by 20%.",
        ],
        "tags": ["NLP", "Social Media Analytics", "Consulting", "Python"],
    },
    {
        "role": "Machine Learning Research Associate",
        "company": "Carnegie Mellon University",
        "period": "2017 – 2019",
        "start": 2017, "end": 2019,
        "location": "Doha, Qatar",
        "highlights": [
            "Built deep learning models to predict event coreference, enabling automated Q&A systems using Stanford CoreNLP.",
            "Published research findings in international conferences and journals.",
        ],
        "tags": ["Deep Learning", "NLP", "CoreNLP", "Research", "Publications"],
    },
    {
        "role": "Machine Learning Research Assistant",
        "company": "Texas A&M University",
        "period": "2015 – 2017",
        "start": 2015, "end": 2017,
        "location": "Doha, Qatar",
        "highlights": [
            "Developed supervised models (SVM, Random Forest, Deep Learning) to predict insomnia from recordings.",
            "Designed longitudinal biofeedback studies and presented findings at IEEE conferences.",
        ],
        "tags": ["SVM", "Random Forest", "Deep Learning", "Biofeedback", "IEEE"],
    },
]

EDUCATION = pd.DataFrame([
    {"Degree": "Master of Management Analytics (MMA)", "Institution": "Rotman, U of T", "Year": "2024–2026", "Notes": "Vector Scholar 2025–26"},
    {"Degree": "B.Sc. Computer Science", "Institution": "Carnegie Mellon University", "Year": "2015", "Notes": "Dean's List 2011–2015"},
])

SKILLS = {
    "Python": 95,
    "SQL / PySpark": 90,
    "Machine Learning": 95,
    "Deep Learning (TF/PyTorch)": 88,
    "AWS (SageMaker, Glue, Redshift)": 85,
    "Azure ML / Databricks": 78,
    "NLP": 88,
    "A/B Testing & Metrics Design": 82,
    "Team Leadership & Mentoring": 92,
    "AI Strategy & Roadmapping": 90,
}

CERTIFICATIONS = [
    "AWS Certified Machine Learning – Specialty",
    "IBM Certified Design Thinking Practitioner",
]

AWARDS = [
    "🏆 Vector Scholarship in Artificial Intelligence Recipient, 2025–2026",
    "🏅 Sheng Yu Award for Best Research, CIAA 2016",
    "🎖️ Senior Student Leadership Award, 2015",
    "📚 Dean's List, 2011–2015",
]

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<p class="hero-name" style="font-size:1.6rem">Lamana<br>Mulaffer</p>', unsafe_allow_html=True)
    st.caption(PROFILE["title"])
    st.divider()

    # Widget 1 – Section selector
    st.markdown('<p class="sidebar-label">Navigate</p>', unsafe_allow_html=True)
    section = st.selectbox(
        "Jump to section",
        ["🏠 Overview", "💼 Experience", "🎓 Education", "📊 Skills", "🏆 Awards"],
        label_visibility="collapsed",
    )

    st.divider()

    # Widget 2 – Skill threshold slider
    st.markdown('<p class="sidebar-label">Skill threshold</p>', unsafe_allow_html=True)
    min_skill = st.slider(
        "Show skills above proficiency %",
        min_value=0, max_value=100, value=0, step=5,
        label_visibility="collapsed",
    )

    st.divider()

    # Widget 3 – Experience filter checkboxes
    st.markdown('<p class="sidebar-label">Experience filter</p>', unsafe_allow_html=True)
    show_ibm    = st.checkbox("IBM", value=True)
    show_octave = st.checkbox("Octave", value=True)
    show_stax   = st.checkbox("Stax Inc", value=True)
    show_cmu    = st.checkbox("Carnegie Mellon", value=True)
    show_tamu   = st.checkbox("Texas A&M", value=True)

    st.divider()
    st.markdown(f"📧 {PROFILE['email']}")
    st.markdown(f"📞 {PROFILE['phone']}")
    st.markdown(f"🔗 {PROFILE['linkedin']}")
    st.markdown(f"📍 {PROFILE['location']}")

# ── Active section ────────────────────────────────────────────────────────────
active = section.split(" ", 1)[1]

# ══════════════════════════════════════════════════════════════════════════════
# OVERVIEW
# ══════════════════════════════════════════════════════════════════════════════
if active == "Overview":
    st.markdown(f'<p class="hero-name">{PROFILE["name"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="hero-title">{PROFILE["title"]}</p>', unsafe_allow_html=True)
    st.write("")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown('<span class="section-chip">About</span>', unsafe_allow_html=True)
        st.write(PROFILE["summary"])
        st.write("")
        st.markdown('<span class="section-chip">Certifications</span>', unsafe_allow_html=True)
        for cert in CERTIFICATIONS:
            st.markdown(f"✅ {cert}")

    with col2:
        st.markdown('<span class="section-chip">Quick Stats</span>', unsafe_allow_html=True)
        m1, m2, m3 = st.columns(3)
        m1.metric("Years Exp.", "9+")
        m2.metric("Industries", "4+")
        m3.metric("Max Team", "10")
        st.write("")
        st.markdown('<span class="section-chip">Key Highlights</span>', unsafe_allow_html=True)
        st.markdown("📈 **15–20%** ML accuracy improvement @ IBM")
        st.markdown("💰 **~$55K** annual margin gain @ Octave")
        st.markdown("📊 **20%** revenue uplift per project @ Stax")
        st.markdown("🎓 **Vector Scholar** 2025–26")

    st.divider()

    # Skills bar chart preview
    st.markdown('<span class="section-chip">Skills Overview</span>', unsafe_allow_html=True)
    filtered = {k: v for k, v in SKILLS.items() if v >= min_skill}
    if filtered:
        fig = px.bar(
            x=list(filtered.values()),
            y=list(filtered.keys()),
            orientation="h",
            color=list(filtered.values()),
            color_continuous_scale=["#c7d2fe", "#0f3460"],
            labels={"x": "Proficiency (%)", "y": ""},
            height=370,
        )
        fig.update_layout(
            coloraxis_showscale=False,
            plot_bgcolor="white", paper_bgcolor="white",
            margin=dict(l=0, r=30, t=10, b=10),
            xaxis=dict(range=[0, 100], gridcolor="#f3f4f6"),
            yaxis=dict(tickfont=dict(size=12)),
        )
        fig.update_traces(texttemplate="%{x}%", textposition="outside")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No skills match the current threshold — lower the slider in the sidebar.")

# ══════════════════════════════════════════════════════════════════════════════
# EXPERIENCE
# ══════════════════════════════════════════════════════════════════════════════
elif active == "Experience":
    st.markdown('<span class="section-chip">Work Experience</span>', unsafe_allow_html=True)
    st.write("")

    visibility_map = {
        "IBM": show_ibm,
        "Octave": show_octave,
        "Stax Inc": show_stax,
        "Carnegie Mellon University": show_cmu,
        "Texas A&M University": show_tamu,
    }
    visible_exp = [e for e in EXPERIENCE if visibility_map.get(e["company"], True)]

    if not visible_exp:
        st.warning("All companies are unchecked. Select at least one in the sidebar.")
    else:
        for exp in visible_exp:
            c1, c2 = st.columns([5, 1])
            with c1:
                st.markdown(f"#### {exp['role']} · {exp['company']}")
                st.caption(f"📍 {exp['location']}  ·  🗓 {exp['period']}")
            with c2:
                duration = exp["end"] - exp["start"]
                st.metric("Duration", f"{duration} yr{'s' if duration != 1 else ''}")
            for h in exp["highlights"]:
                st.markdown(f"<span class='timeline-dot'></span>{h}", unsafe_allow_html=True)
            tags_html = " ".join(f"<span class='tag'>{t}</span>" for t in exp["tags"])
            st.markdown(tags_html, unsafe_allow_html=True)
            st.divider()

    # Gantt / timeline chart
    st.markdown('<span class="section-chip">Career Timeline</span>', unsafe_allow_html=True)
    if visible_exp:
        timeline_data = [
            dict(
                Task=f"{e['role']} @ {e['company']}",
                Start=f"{e['start']}-01-01",
                Finish=f"{e['end']}-12-31",
                Company=e["company"],
            )
            for e in visible_exp
        ]
        df_t = pd.DataFrame(timeline_data)
        fig2 = px.timeline(
            df_t, x_start="Start", x_end="Finish", y="Task", color="Company",
            height=320,
            color_discrete_sequence=["#0f3460", "#16213e", "#e94560", "#457b9d", "#1d3557"],
        )
        fig2.update_yaxes(autorange="reversed")
        fig2.update_layout(
            paper_bgcolor="white", plot_bgcolor="white",
            margin=dict(l=0, r=10, t=10, b=10),
            legend=dict(orientation="h", y=-0.35),
        )
        st.plotly_chart(fig2, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# EDUCATION
# ══════════════════════════════════════════════════════════════════════════════
elif active == "Education":
    st.markdown('<span class="section-chip">Education</span>', unsafe_allow_html=True)
    st.write("")
    st.dataframe(
        EDUCATION,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Degree":      st.column_config.TextColumn("Degree / Credential", width="large"),
            "Institution": st.column_config.TextColumn("Institution"),
            "Year":        st.column_config.TextColumn("Year"),
            "Notes":       st.column_config.TextColumn("Notes"),
        },
    )
    st.write("")
    st.info("📌 Available for full-time AI/Data Science leadership roles starting **2026** upon MMA graduation.")

# ══════════════════════════════════════════════════════════════════════════════
# SKILLS
# ══════════════════════════════════════════════════════════════════════════════
elif active == "Skills":
    st.markdown('<span class="section-chip">Skills & Proficiency</span>', unsafe_allow_html=True)
    st.write("")

    filtered = {k: v for k, v in SKILLS.items() if v >= min_skill}
    if not filtered:
        st.info("Adjust the sidebar slider to see skills.")
    else:
        categories = list(filtered.keys())
        values = list(filtered.values())

        fig3 = go.Figure(go.Scatterpolar(
            r=values + [values[0]],
            theta=categories + [categories[0]],
            fill='toself',
            fillcolor='rgba(15,52,96,0.15)',
            line=dict(color='#0f3460', width=2),
        ))
        fig3.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(size=9))),
            paper_bgcolor="white",
            height=420,
            margin=dict(l=60, r=60, t=20, b=20),
        )

        col1, col2 = st.columns([1, 1])
        with col1:
            st.plotly_chart(fig3, use_container_width=True)
        with col2:
            df_skills = pd.DataFrame({
                "Skill": list(filtered.keys()),
                "Proficiency (%)": list(filtered.values()),
            }).sort_values("Proficiency (%)", ascending=False)
            st.dataframe(df_skills, use_container_width=True, hide_index=True)

        st.divider()
        st.markdown('<span class="section-chip">Certifications</span>', unsafe_allow_html=True)
        for cert in CERTIFICATIONS:
            st.markdown(f"✅ **{cert}**")

# ══════════════════════════════════════════════════════════════════════════════
# AWARDS
# ══════════════════════════════════════════════════════════════════════════════
elif active == "Awards":
    st.markdown('<span class="section-chip">Awards & Recognition</span>', unsafe_allow_html=True)
    st.write("")
    for award in AWARDS:
        st.markdown(f'<div class="award-badge">{award}</div>', unsafe_allow_html=True)
    st.write("")
    st.divider()
    st.markdown('<span class="section-chip">Research & Publications</span>', unsafe_allow_html=True)
    st.write("")
    st.markdown("📄 **Event Coreference Prediction** — Deep learning model for automated Q&A systems using Stanford CoreNLP. *Published in international conferences and journals* (CMU, 2017–2019).")
    st.markdown("📄 **Insomnia Prediction from Biofeedback** — Supervised models (SVM, Random Forest, Deep Learning) on longitudinal recordings. *Presented at IEEE conferences* (Texas A&M, 2015–2017).")
