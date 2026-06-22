import pandas as pd

skills_df = pd.read_csv("data/skills.csv")
SKILLS = set(skills_df["skill"].str.lower())

def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return sorted(set(found_skills))