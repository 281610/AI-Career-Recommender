"""import streamlit as st
import pickle
import pandas as pd
from salary_data import salary_dict

# Load model and encoders
model = pickle.load(open("career_model.pkl", "rb"))
le_interest = pickle.load(open("le_interest.pkl", "rb"))
le_skill = pickle.load(open("le_skill.pkl", "rb"))
le_personality = pickle.load(open("le_personality.pkl", "rb"))
le_career = pickle.load(open("le_career.pkl", "rb"))

st.title("AI Career Path Recommender")

interest = st.selectbox("Select Interest", le_interest.classes_)
skill = st.selectbox("Skill Level", le_skill.classes_)
aptitude = st.slider("Aptitude Score", 0, 100)
personality = st.selectbox("Personality Type", le_personality.classes_)

if st.button("Predict Career"):
    
    # Encode user input
    input_data = pd.DataFrame([[
        le_interest.transform([interest])[0],
        le_skill.transform([skill])[0],
        aptitude,
        le_personality.transform([personality])[0]
    ]], columns=['Interest', 'Skill_Level', 'Aptitude', 'Personality'])
    
    prediction = model.predict(input_data)
    career = le_career.inverse_transform(prediction)[0]

    st.success(f"Suggested Career: {career}")
    st.info(f"Expected Salary: {salary_dict.get(career, 'Not Available')}")
"""
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from chatbot import get_chatbot_response

app = Flask(__name__)

# Load model & encoders
model = pickle.load(open("career_model.pkl", "rb"))
le_interest = pickle.load(open("le_interest.pkl", "rb"))
le_skill = pickle.load(open("le_skill.pkl", "rb"))
le_personality = pickle.load(open("le_personality.pkl", "rb"))
le_education = pickle.load(open("le_education.pkl", "rb"))
le_work = pickle.load(open("le_work.pkl", "rb"))
le_career = pickle.load(open("le_career.pkl", "rb"))
career_roadmaps = {


    "Data Scientist": {
        "steps": [
            "Learn Python programming",
            "Master Statistics & Probability",
            "Learn Data Analysis (Pandas, NumPy)",
            "Study Machine Learning algorithms",
            "Build real-world ML projects",
            "Learn SQL & Data Visualization",
            "Apply for internships or junior roles"
        ]
    },

    "Software Developer": {
        "steps": [
            "Learn a programming language (Python/Java/C++)",
            "Understand Data Structures & Algorithms",
            "Practice coding daily (LeetCode/HackerRank)",
            "Build web or app projects",
            "Learn Git & GitHub",
            "Prepare for technical interviews"
        ]
    },

    "Graphic Designer": {
        "steps": [
            "Learn design principles (color, typography, layout)",
            "Master tools like Photoshop & Illustrator",
            "Practice logo & poster design",
            "Build a strong portfolio",
            "Freelance or apply for internships",
            "Grow personal brand on social media"
        ]
    },

    "Mechanical Engineer": {
        "steps": [
            "Strong understanding of Physics & Mathematics",
            "Learn CAD tools (AutoCAD/SolidWorks)",
            "Understand thermodynamics & mechanics",
            "Work on industrial projects",
            "Intern in manufacturing companies",
            "Prepare for technical interviews"
        ]
    },

    "Chartered Accountant": {
        "steps": [
            "Register for CA Foundation",
            "Clear Intermediate level exams",
            "Complete Articleship training",
            "Prepare for Final exams",
            "Gain practical accounting experience",
            "Apply in finance firms or start practice"
        ]
    },

    "Professor": {
        "steps": [
            "Complete Master's degree",
            "Clear NET/PhD entrance",
            "Pursue PhD in your field",
            "Publish research papers",
            "Gain teaching experience",
            "Apply in colleges/universities"
        ]
    },

    "Digital Marketer": {
        "steps": [
            "Learn SEO & SEM",
            "Understand Social Media Marketing",
            "Learn Google Ads & Analytics",
            "Practice content marketing",
            "Run ad campaigns",
            "Work with startups or agencies"
        ]
    },

    "Architect": {
        "steps": [
            "Complete B.Arch degree",
            "Learn AutoCAD & 3D modeling tools",
            "Understand building design principles",
            "Work on real construction projects",
            "Intern under senior architects",
            "Start independent practice"
        ]
    },

    "Entrepreneur": {
        "steps": [
            "Identify a business problem",
            "Research market demand",
            "Create business plan",
            "Develop MVP (Minimum Viable Product)",
            "Secure funding or bootstrap",
            "Scale the business"
        ]
    },

    "Psychologist": {
        "steps": [
            "Complete Bachelor's in Psychology",
            "Pursue Master's specialization",
            "Gain clinical training",
            "Get licensed certification",
            "Work in hospitals or private clinics",
            "Build client base"
        ]
    },

    "Business Analyst": {
        "steps": [
            "Learn Excel & SQL",
            "Understand Business processes",
            "Learn Data Visualization (Power BI/Tableau)",
            "Practice real case studies",
            "Learn requirement gathering",
            "Apply for analyst roles"
        ]
    },

    "Content Creator": {
        "steps": [
            "Choose a niche (Tech, Fitness, Education)",
            "Learn video editing tools",
            "Start posting consistently",
            "Build audience engagement",
            "Collaborate with brands",
            "Monetize through ads & sponsorships"
        ]
    },

    "Content Creator": {
        "steps": [
            "Choose a niche (Tech, Fitness, Education, etc.)",
            "Learn video editing tools (CapCut, Premiere Pro)",
            "Start posting consistently on YouTube/Instagram",
            "Build audience engagement",
            "Monetize via ads & brand deals"
        ]
    },

    "Business Analyst": {
        "steps": [
            "Learn Excel & SQL",
            "Understand Business Fundamentals",
            "Learn Data Visualization (Power BI / Tableau)",
            "Practice case studies",
            "Apply for internships"
        ]
    },

    "Data Scientist": {
        "steps": [
            "Learn Python",
            "Master Statistics & Probability",
            "Learn Machine Learning",
            "Build projects",
            "Apply for Data roles"
        ]
    }

}

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():

    response = ""
    user_message = ""

    if request.method == "POST":
        user_message = request.form["message"]
        response = get_chatbot_response(user_message)

    return render_template(
        "chatbot.html",
        response=response,
        user_message=user_message
    )

@app.route("/predict_page")
def home():
    data = pd.read_csv("career_data.csv")

    interests = sorted(data["Interest"].dropna().astype(str).unique())
    skills = sorted(data["Skill_Level"].dropna().astype(str).unique())
    personalities = sorted(data["Personality"].dropna().astype(str).unique())
    education_levels = sorted(data["Education_Level"].dropna().astype(str).unique())
    work_types = sorted(data["Preferred_Work_Type"].dropna().astype(str).unique())

    return render_template(
        "index.html",
        interests=interests,
        skills=skills,
        personalities=personalities,
        education_levels=education_levels,
        work_types=work_types
    )

@app.route("/roadmap/<career>")
def roadmap(career):
    data = career_roadmaps.get(career)

    if data:
        return render_template("roadmap.html", career=career, steps=data["steps"])
    else:
        return f"No roadmap available for {career}"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        interest = request.form["interest"]
        skill = request.form["skill"]
        aptitude = int(request.form["aptitude"])
        personality = request.form["personality"]
        education = request.form["education"]
        work = request.form["work"]

        print("Received:", interest, skill, aptitude, personality, education, work)

        interest = le_interest.transform([interest])[0]
        skill = le_skill.transform([skill])[0]
        personality = le_personality.transform([personality])[0]
        education = le_education.transform([education])[0]
        work = le_work.transform([work])[0]

        input_data = [[interest, skill, aptitude, personality, education, work]]

        prediction = model.predict(input_data)
        career = le_career.inverse_transform(prediction)[0]

        return render_template("result.html", career=career)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
