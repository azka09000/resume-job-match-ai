import pandas as pd

skills_df = pd.read_csv("data/skills.csv")
SKILLS = set(skills_df["skill"].str.lower())

# Different phrases that should map to the same skill
SKILL_ALIASES = {
    "team collaboration": "teamwork",
    "collaborative": "teamwork",
    "coordination": "teamwork",

    "artificial intelligence": "machine learning",
    "ai": "machine learning",
    "ai/ml": "machine learning",

    "object oriented programming": "software development",
    "oop": "software development",

    "web application": "web development",
    "web applications": "web development",

    "mobile application": "mobile development",
    "mobile applications": "mobile development",

    "server-side": "backend",
    "server side": "backend",

    "user interface": "frontend",
    "ui": "frontend",

    "database architecture": "databases"
}


def extract_skills(text):
    text = text.lower()

    found_skills = set()

    # Extract skills directly from skills.csv
    for skill in SKILLS:
        if skill in text:
            found_skills.add(skill)

    # Extract skills using aliases/synonyms
    for phrase, normalized_skill in SKILL_ALIASES.items():
        if phrase in text:
            found_skills.add(normalized_skill)

    return sorted(found_skills)