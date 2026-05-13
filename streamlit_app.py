import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/best_model.pkl")

st.title("💼 Job Salary Prediction")

st.write("Predict employee salary using Machine Learning")

job_title = st.selectbox(
    "Job Title",
    [
        "Data Scientist",
        "AI Engineer",
        "Backend Developer",
        "Frontend Developer",
        "Business Analyst"
    ]
)

experience = st.slider(
    "Experience Years",
    0,
    20,
    5
)

education = st.selectbox(
    "Education Level",
    [
        "High School",
        "Bachelor",
        "Master",
        "PhD"
    ]
)

skills = st.slider(
    "Skills Count",
    1,
    20,
    10
)

industry = st.selectbox(
    "Industry",
    [
        "IT",
        "Healthcare",
        "Finance",
        "Education"
    ]
)

company_size = st.selectbox(
    "Company Size",
    [
        "Small",
        "Medium",
        "Large",
        "Enterprise"
    ]
)

location = st.selectbox(
    "Location",
    [
        "USA",
        "Canada",
        "India",
        "Australia"
    ]
)

remote = st.selectbox(
    "Remote Work",
    [
        "Yes",
        "No",
        "Hybrid"
    ]
)

certifications = st.slider(
    "Certifications",
    0,
    5,
    2
)

if st.button("Predict Salary"):

    sample = pd.DataFrame({

        'job_title': [job_title],
        'experience_years': [experience],
        'education_level': [education],
        'skills_count': [skills],
        'industry': [industry],
        'company_size': [company_size],
        'location': [location],
        'remote_work': [remote],
        'certifications': [certifications]
    })

    prediction = model.predict(sample)

    st.success(
        f"Predicted Salary: ${prediction[0]:,.2f}"
    )