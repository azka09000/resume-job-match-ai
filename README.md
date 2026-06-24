# 📄 Resume Job Match AI System

An AI-powered resume screening and job matching system that analyzes a candidate’s resume against a job description using Natural Language Processing (NLP) and TF-IDF similarity scoring.

---

## 🚀 Features

- Upload Resume (PDF / DOCX)
- Paste Job Description
- Extract text from documents
- NLP-based text preprocessing
- Skill extraction from resume and job description
- AI-powered match score using TF-IDF
- Missing skill detection

---

## 🧠 Tech Stack

- Python
- Streamlit
- Scikit-learn
- NLTK
- Pandas
- pdfplumber
- python-docx

---

## 📂 Project Structure
resume-job-match-ai/
│
├── app/
├── src/
├── data/
├── assets/
├── requirements.txt
---

## ⚙️ How to Run

### 1. Clone repo
git clone https://github.com/azka09000/resume-job-match-ai.git
cd resume-job-match-ai

### 2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run app
streamlit run app/streamlit_app.py

---

## 📊 Example Output

- Match Score: 78%
- Matching Skills: Python, SQL
- Missing Skills: TensorFlow, Power BI

---

## 🎯 Future Improvements

- Sentence-BERT embeddings
- ATS scoring system
- Resume improvement suggestions
- PDF report generation

---

## 👩‍💻 Author

Azka Nisar  
AI Student | Python & Data Science Enthusiast