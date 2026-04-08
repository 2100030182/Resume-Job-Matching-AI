import streamlit as st
import os

from src.resume_parser import extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.matcher import calculate_match
from src.recommender import recommend_learning


st.set_page_config(
    page_title="Resume–Job Matching AI",
    layout="wide"
)

st.title("🧠 Resume–Job Matching AI System")

st.markdown(
"""
Upload your resume and paste a job description  
to analyze compatibility and skill gaps.
"""
)

# Upload Resume
resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# Job Description Input
job_description = st.text_area(
    "Paste Job Description",
    height=200
)

if st.button("Analyze Resume"):

    if resume_file and job_description:

        # Save uploaded file
        resume_path = "data/temp_resume.pdf"

        with open(resume_path, "wb") as f:
            f.write(resume_file.read())

        # Extract Resume Text
        resume_text = extract_text_from_pdf(
            resume_path
        )

        # Extract Skills
        resume_skills = extract_skills(
            resume_text
        )

        job_skills = extract_skills(
            job_description
        )

        # Calculate Match
        score, matched, missing = calculate_match(
            resume_skills,
            job_skills
        )

        # Generate Recommendations
        recommendations = recommend_learning(
            list(missing)
        )

        # Display Results
        st.subheader("📊 Match Score")

        st.metric(
            "Compatibility Score",
            f"{score:.2f}%"
        )

        st.subheader("✅ Matched Skills")

        st.write(list(matched))

        st.subheader("❌ Missing Skills")

        st.write(list(missing))

        st.subheader("📚 Learning Recommendations")

        for skill, suggestion in recommendations.items():

            st.write(
                f"**{skill}** -> {suggestion}"
            )

    else:

        st.warning(
            "Please upload resume and paste job description."
        )