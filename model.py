import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
# Load dataset
data = pd.read_csv("career_data.csv")

# Create encoders
le_interest = LabelEncoder()
le_skill = LabelEncoder()
le_personality = LabelEncoder()
le_education = LabelEncoder()
le_work = LabelEncoder()
le_career = LabelEncoder()

# Encode columns
data['Interest'] = le_interest.fit_transform(data['Interest'])
data['Skill_Level'] = le_skill.fit_transform(data['Skill_Level'])
data['Personality'] = le_personality.fit_transform(data['Personality'])
data['Education_Level'] = le_education.fit_transform(data['Education_Level'])
data['Preferred_Work_Type'] = le_work.fit_transform(data['Preferred_Work_Type'])
data['Career'] = le_career.fit_transform(data['Career'])

# Features and Target
X = data[['Interest','Skill_Level','Aptitude',
          'Personality','Education_Level','Preferred_Work_Type']]

y = data['Career']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

if not os.path.exists("models"):
    os.makedirs("models")
# Save model and encoders
pickle.dump(model, open("career_model.pkl", "wb"))
pickle.dump(le_interest, open("le_interest.pkl", "wb"))
pickle.dump(le_skill, open("le_skill.pkl", "wb"))
pickle.dump(le_personality, open("le_personality.pkl", "wb"))
pickle.dump(le_education, open("le_education.pkl", "wb"))
pickle.dump(le_work, open("le_work.pkl", "wb"))
pickle.dump(le_career, open("le_career.pkl", "wb"))

print("Model retrained and saved successfully!")
