import pandas as pd
import random

# Load existing dataset
df_old = pd.read_csv("career_data.csv")

# Categories
interests = ["Coding", "Design", "Business", "Arts", "Healthcare", "Finance", "Teaching"]
skills = ["Low", "Medium", "High"]
personalities = ["Analytical", "Creative", "Extrovert", "Introvert"]
education_levels = ["High School", "Bachelor", "Master"]
work_types = ["Remote", "Onsite", "Hybrid"]

career_map = {
    "Coding": ["Data Scientist", "Software Developer", "AI Engineer"],
    "Design": ["UI/UX Designer", "Graphic Designer"],
    "Business": ["MBA", "Marketing Manager"],
    "Arts": ["Artist", "Content Creator"],
    "Healthcare": ["Doctor", "Nurse"],
    "Finance": ["Financial Analyst", "Chartered Accountant"],
    "Teaching": ["Teacher", "Professor"]
}

new_data = []

for i in range(500):  # 500 rows add kar rahe
    interest = random.choice(interests)
    skill = random.choice(skills)
    aptitude = random.randint(50, 100)
    personality = random.choice(personalities)
    education = random.choice(education_levels)
    work = random.choice(work_types)
    career = random.choice(career_map[interest])

    new_data.append([
        interest, skill, aptitude, personality,
        education, work, career
    ])

df_new = pd.DataFrame(new_data, columns=[
    "Interest",
    "Skill_Level",
    "Aptitude",
    "Personality",
    "Education_Level",
    "Preferred_Work_Type",
    "Career"
])

df_final = pd.concat([df_old, df_new], ignore_index=True)

df_final.to_csv("career_data.csv", index=False)

print("✅ Dataset Updated Successfully!")
