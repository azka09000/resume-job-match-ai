import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.file_processor import extract_resume_text
from src.text_preprocessor import clean_text
from src.skill_extractor import extract_skills
from src.matcher import calculate_match
from src.recommender import get_recommendation

st.set_page_config(
    page_title="Resume AI Matcher",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Screening + Job Match AI System")
st.markdown(
    """
    Upload your resume and paste a job description to analyze
    your compatibility, identify skill gaps, and receive
    personalized recommendations.
    """
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF/DOCX)",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=200
)

if uploaded_file and job_description:

    # ============================
    # 1. Extract Resume Text
    # ============================
    resume_text = extract_resume_text(uploaded_file)

    # ============================
    # 2. Clean Text
    # ============================
    clean_resume = clean_text(resume_text)
    clean_job = clean_text(job_description)

    # ============================
    # 3. Extract Skills
    # ============================
    resume_skills = set(extract_skills(clean_resume))
    job_skills = set(extract_skills(clean_job))

    # ============================
    # 4. Skill Analysis
    # ============================
    matching_skills = sorted(
        resume_skills.intersection(job_skills)
    )

    missing_skills = sorted(
        job_skills - resume_skills
    )

    skill_match_score = (
        len(matching_skills) / len(job_skills) * 100
        if job_skills
        else 0
    )

    # ============================
    # 5. TF-IDF Similarity
    # ============================
    tfidf_score = calculate_match(
        clean_resume,
        clean_job
    )

    # ============================
    # 6. Overall Score
    # ============================
    overall_score = (
        skill_match_score * 0.7 +
        tfidf_score * 0.3
    )

    overall_score = min(overall_score, 100)
    skill_match_score = min(skill_match_score, 100)
    tfidf_score = min(tfidf_score, 100)

    # ============================
    # ATS Verdict
    # ============================
    if overall_score >= 80:
        verdict = "🟢 Excellent Match"
    elif overall_score >= 60:
        verdict = "🟡 Good Match"
    elif overall_score >= 40:
        verdict = "🟠 Moderate Match"
    else:
        verdict = "🔴 Low Match"

    # ============================
    # MATCH ANALYSIS
    # ============================
    st.subheader("📊 Match Analysis")
    st.info(f"ATS Verdict: **{verdict}**")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Overall Match",
            f"{overall_score:.2f}%"
        )
        st.progress(overall_score / 100)

    with col2:
        st.metric(
            "Skill Match",
            f"{skill_match_score:.2f}%"
        )
        st.progress(skill_match_score / 100)

    with col3:
        st.metric(
            "TF-IDF Similarity",
            f"{tfidf_score:.2f}%"
        )
        st.progress(tfidf_score / 100)

    # ============================
    # SKILL SUMMARY
    # ============================
    st.subheader("📌 Skill Summary")

    st.caption(
        f"Matched {len(matching_skills)} of "
        f"{len(job_skills)} detected job skills."
    )

    col4, col5 = st.columns(2)

    with col4:
        st.metric(
            "Matching Skills",
            len(matching_skills)
        )

        if matching_skills:
            for skill in matching_skills:
                st.success(f"✓ {skill}")
        else:
            st.info("No matching skills found.")

    with col5:
        st.metric(
            "Missing Skills",
            len(missing_skills)
        )

        if missing_skills:
            for skill in missing_skills:
                st.warning(f"✗ {skill}")
        else:
            st.success("No missing skills detected.")

    # ============================
    # RECOMMENDATIONS
    # ============================
    st.subheader("💡 Recommendations")

    if missing_skills:

        st.write(
            "Consider strengthening or highlighting "
            "experience in the following areas:"
        )

        for skill in missing_skills:
            st.info(get_recommendation(skill))

    else:
        st.success(
            "Excellent! Your resume covers all detected job requirements."
        )

    # ============================
    # EXTRACTED RESUME TEXT
    # ============================
    with st.expander("📄 View Extracted Resume Text"):

        if resume_text.strip():
            st.text_area(
                "Extracted Text",
                resume_text,
                height=300
            )
        else:
            st.warning(
                "No text could be extracted from the uploaded file."
            )

    # ============================
    # TECHNICAL DETAILS
    # ============================
    show_debug = st.checkbox(
        "🔍 Show Technical Details"
    )

    if show_debug:
        st.write(
            "Resume Skills:",
            sorted(resume_skills)
        )
        st.write(
            "Job Skills:",
            sorted(job_skills)
        )