RECOMMENDATIONS = {
    "databases":
        "Highlight SQL coursework, database projects, or experience with relational databases.",

    "software development":
        "Mention software engineering projects, OOP concepts, and development methodologies.",

    "web technologies":
        "Include projects involving HTML, CSS, JavaScript, or web frameworks.",

    "teamwork":
        "Describe collaborative university projects and mention team-based experiences.",

    "organizational skills":
        "Highlight leadership roles, event management, or experiences managing deadlines.",

    "research":
        "Mention research papers, academic projects, or independent investigations.",

    "networking":
        "Include experiences involving professional networking, events, or collaborations.",

    "lead generation":
        "Mention outreach activities, marketing projects, or experiences identifying opportunities."
}

def get_recommendation(skill):
    return RECOMMENDATIONS.get(
        skill,
        f"Consider adding experience related to {skill}."
    )