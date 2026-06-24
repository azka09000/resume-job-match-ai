import re
import pandas as pd

skills_df = pd.read_csv("data/skills.csv")
SKILLS = set(skills_df["skill"].str.lower())

# Different phrases that should map to the same skill
SKILL_ALIASES = {
    # Teamwork
    "team collaboration": "teamwork",
    "collaborative": "teamwork",
    "collaboration": "teamwork",
    "coordination": "teamwork",

    # AI / ML
    "artificial intelligence": "machine learning",
    "ai": "machine learning",
    "ai/ml": "machine learning",

    # Software Development
    "object oriented programming": "software development",
    "oop": "software development",

    # Web Development
    "web application": "web development",
    "web applications": "web development",

    # Mobile Development
    "mobile application": "mobile development",
    "mobile applications": "mobile development",

    # Backend
    "server-side": "backend",
    "server side": "backend",

    # Frontend
    "user interface": "frontend",
    "responsive user interface": "frontend",
    "responsive user interfaces": "frontend",

    # Databases
    "database": "databases",
    "database architecture": "databases",
    "sql": "databases",

    # Soft Skills
    "continuous learning": "quick learner",
    "self learning": "quick learner",
    "self-learning": "quick learner"
}


def extract_skills(text):
    text = text.lower()
    found_skills = set()

    # Extract skills directly from skills.csv
    for skill in SKILLS:
        pattern = rf"\b{re.escape(skill)}\b"

        if re.search(pattern, text):
            found_skills.add(skill)

    # Extract skills using aliases/synonyms
    for phrase, normalized_skill in SKILL_ALIASES.items():
        pattern = rf"\b{re.escape(phrase)}\b"

        if re.search(pattern, text):
            found_skills.add(normalized_skill)

    # Normalize extracted skills to avoid duplicates
    normalized_skills = set()

    for skill in found_skills:
        normalized_skills.add(
            SKILL_ALIASES.get(skill, skill)
        )

    return sorted(normalized_skills)