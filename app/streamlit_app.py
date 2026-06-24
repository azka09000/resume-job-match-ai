import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.file_processor import extract_resume_text
from src.text_preprocessor import clean_text
from src.skill_extractor import extract_skills
from src.matcher import calculate_match
from src.recommender import get_recommendation

st.set_page_config(page_title="Resume AI Matcher", layout="wide")

st.title("📄 Resume Screening + Job Match AI System")
st.markdown(
    "Upload your resume and paste a job description to analyze your compatibility."
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF/DOCX)",
    type=["pdf", "docx"]
)

job_description = st.text_area("Paste Job Description")

if uploaded_file and job_description:

    # 1. Extract text
    resume_text = extract_resume_text(uploaded_file)

    # 2. Clean text
    clean_resume = clean_text(resume_text)
    clean_job = clean_text(job_description)

    # 3. Extract skills
    resume_skills = extract_skills(clean_resume)
    job_skills = extract_skills(clean_job)

    # 4. Skill overlap analysis
    matching_skills = set(resume_skills).intersection(job_skills)
    missing_skills = set(job_skills) - set(resume_skills)

    skill_match_score = (
        len(matching_skills) / len(job_skills) * 100
        if job_skills
        else 0
    )

    # 5. TF-IDF similarity score
    tfidf_score = calculate_match(clean_resume, clean_job)

    # 6. Overall score
    overall_score = (
        skill_match_score * 0.7 +
        tfidf_score * 0.3
    )

    # ----------------------------
    # SCORE SECTION
    # ----------------------------
    st.subheader("📊 Match Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Overall Match",
            value=f"{overall_score:.2f}%"
        )

    with col2:
        st.metric(
            label="Skill Match",
            value=f"{skill_match_score:.2f}%"
        )

    with col3:
        st.metric(
            label="TF-IDF Similarity",
            value=f"{tfidf_score:.2f}%"
        )

    # ----------------------------
    # SKILLS SECTION
    # ----------------------------
    col4, col5 = st.columns(2)

    with col4:
        st.subheader("✅ Matching Skills")

        if matching_skills:
            for skill in sorted(matching_skills):
                st.success(f"✓ {skill}")
        else:
            st.info("No matching skills found.")

    with col5:
        st.subheader("❌ Missing Skills")

        if missing_skills:
            for skill in sorted(missing_skills):
                st.warning(f"✗ {skill}")
        else:
            st.success("No missing skills detected.")

    # ----------------------------
    # RECOMMENDATIONS SECTION
    # ----------------------------
    st.subheader("💡 Recommendations")

    if missing_skills:
        st.write(
            "Consider highlighting or developing experience in the following areas:"
        )

        for skill in sorted(missing_skills):
            st.info(get_recommendation(skill))
    else:
        st.success(
            "Great! Your resume covers all detected job requirements."
        )

    # ----------------------------
    # EXTRACTED RESUME TEXT
    # ----------------------------
    with st.expander("📄 View Extracted Resume Text"):
        st.text_area(
            "Extracted Text",
            resume_text,
            height=300
        )