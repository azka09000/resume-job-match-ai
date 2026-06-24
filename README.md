📄 Resume Job Match AI System

An AI-powered Resume Screening and Job Matching System that analyzes a candidate’s resume against a job description using Natural Language Processing (NLP), semantic similarity with Sentence Transformers, and skill-gap analysis. The system provides ATS-style compatibility scoring and personalized recommendations to help candidates improve their resumes.

⸻

🚀 Features

* Upload resumes in PDF or DOCX format
* Paste any job description for analysis
* Automatic text extraction and preprocessing
* Skill extraction from resumes and job descriptions
* Semantic similarity scoring using Sentence Transformers
* ATS-style overall match percentage
* Skill match and coverage analysis
* Matching and missing skill detection
* Personalized recommendations based on identified skill gaps
* View extracted resume text and detected skills
* Interactive Streamlit web application

⸻

🧠 Tech Stack

* Python
* Streamlit
* Sentence Transformers
* PyTorch
* Scikit-learn
* NLTK
* Pandas
* pdfplumber
* python-docx

⸻

📂 Project Structure

resume-job-match-ai/
│
├── app/
│   └── streamlit_app.py
│
├── src/
│   ├── file_processor.py
│   ├── text_preprocessor.py
│   ├── skill_extractor.py
│   ├── semantic_matcher.py
│   └── recommender.py
│
├── data/
│   └── skills.csv
│
├── assets/
│   ├── home_page.png
│   ├── match_analysis.png
│   └── technical_details.png
│
├── requirements.txt
└── README.md

⸻

⚙️ How to Run

1. Clone the Repository

git clone https://github.com/azka09000/resume-job-match-ai.git
cd resume-job-match-ai

2. Create a Virtual Environment

Windows

python -m venv .venv
.venv\Scripts\activate

macOS/Linux

python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Run the Application

streamlit run app/streamlit_app.py

⸻

🖥️ Application Screenshots

Home Screen

Upload a resume and paste a job description to begin the analysis.

Match Analysis

The system calculates skill overlap and semantic similarity to provide an ATS-style compatibility score.

Technical Details

View extracted resume text and inspect the detected skills from both the resume and job description.

⸻

📊 Example Output

ATS Verdict: 🟡 Good Match

Overall Match: 58.99%

Matching Skills

* Communication
* Machine Learning
* Databases
* Software Development
* Teamwork
* Quick Learner

Missing Skills

* APIs
* Backend Development
* Frontend Development
* Mobile Development
* Web Development

Recommendations

* Build projects involving REST APIs
* Develop frontend and backend applications
* Create mobile applications
* Highlight relevant coursework and practical experience

⸻

🎯 Learning Outcomes

This project demonstrates:

* Natural Language Processing (NLP)
* Semantic text similarity using transformer embeddings
* Information extraction and skill matching
* Resume screening and ATS concepts
* Data preprocessing and text cleaning
* Building interactive AI applications with Streamlit
* End-to-end Python project development
* Git and GitHub project management
* Documentation and software engineering best practices

⸻

🚀 Future Improvements

* Resume keyword optimization suggestions
* Export analysis reports as PDF
* Support for multiple resume templates
* Named Entity Recognition (NER) for improved skill extraction
* More advanced ATS scoring algorithms
* Deploy the application using Streamlit Cloud

⸻

👩‍💻 Author

Azka Nisar

Artificial Intelligence Undergraduate | Python & Data Science Enthusiast

* LinkedIn: https://www.linkedin.com/in/azkanisarofficial
* GitHub: https://github.com/azka09000