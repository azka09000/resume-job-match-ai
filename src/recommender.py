RECOMMENDATIONS = {
    "databases":
        "Highlight SQL coursework, database projects, or experience designing and querying relational databases.",

    "software development":
        "Mention software engineering projects, Object-Oriented Programming (OOP), version control, and development methodologies.",

    "web development":
        "Include projects involving HTML, CSS, JavaScript, Flask, Django, or responsive web applications.",

    "mobile development":
        "Highlight Android or iOS projects and mention mobile frameworks or app development experience.",

    "frontend":
        "Include projects involving responsive user interfaces, HTML, CSS, JavaScript, or frontend frameworks.",

    "backend":
        "Mention APIs, server-side programming, authentication systems, or database integration projects.",

    "apis":
        "Include projects that consume or build REST APIs and explain how they integrate different systems.",

    "teamwork":
        "Describe collaborative university projects, hackathons, or team-based experiences and clearly explain your contributions.",

    "communication":
        "Highlight presentations, leadership experiences, documentation work, or projects that required effective communication.",

    "organizational skills":
        "Mention experiences managing deadlines, coordinating projects, leading teams, or balancing multiple responsibilities.",

    "research":
        "Highlight research projects, literature reviews, independent investigations, or experiments you conducted.",

    "networking":
        "Mention participation in professional events, student organizations, collaborative projects, or industry engagement activities.",

    "lead generation":
        "Include outreach activities, business initiatives, marketing projects, or experiences identifying opportunities and potential clients.",

    "machine learning":
        "Highlight machine learning projects, predictive models, datasets used, and the tools and algorithms you applied.",

    "deep learning":
        "Include projects involving neural networks, CNNs, RNNs, or frameworks such as TensorFlow and PyTorch.",

    "artificial intelligence":
        "Showcase AI projects that apply intelligent systems to solve real-world problems and emphasize practical outcomes.",

    "data analysis":
        "Include projects involving data cleaning, exploratory data analysis, visualization, and actionable insights.",

    "python":
        "Highlight Python projects and mention libraries such as Pandas, NumPy, Scikit-learn, or Streamlit.",

    "sql":
        "Mention SQL queries, database projects, schema design, and data manipulation experience.",

    "git":
        "Include collaborative projects that demonstrate version control and Git workflows.",

    "github":
        "Showcase well-documented GitHub repositories with clear README files and project demonstrations.",

    "problem solving":
        "Highlight algorithmic projects, coding challenges, optimization tasks, or situations where you solved complex problems.",

    "leadership":
        "Mention leadership positions, mentoring experiences, project management, or initiatives you led.",

    "time management":
        "Demonstrate experiences balancing coursework, projects, internships, or extracurricular activities while meeting deadlines.",

    "quick learner":
        "Highlight situations where you learned a new technology independently and applied it successfully in a project."
}


def get_recommendation(skill):
    return RECOMMENDATIONS.get(
        skill,
        f"Consider adding projects, coursework, certifications, or practical experience related to {skill}."
    )