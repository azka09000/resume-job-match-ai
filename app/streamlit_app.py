import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.file_processor import extract_resume_text
from src.text_preprocessor import clean_text
from src.skill_extractor import extract_skills
from src.matcher import calculate_match

st.set_page_config(page_title="Resume AI Matcher", layout="wide")

st.title("📄 Resume Screening + Job Match AI System")

uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
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

    # 4. Match score
    score = calculate_match(clean_resume, clean_job)

    # 5. Missing skills
    missing_skills = list(set(job_skills) - set(resume_skills))

    # OUTPUT UI
    st.subheader("📊 Match Score")
    st.metric(label="Compatibility", value=f"{score}%")

    st.subheader("✅ Matching Skills")
    st.write(resume_skills)

    st.subheader("❌ Missing Skills")
    st.write(missing_skills)

    st.subheader("📄 Extracted Resume Text")
    st.write(resume_text)