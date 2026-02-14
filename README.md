# 🎤 AI Pronunciation Evaluation System

An AI-powered pronunciation evaluation system built using Speech Recognition and NLP techniques.  
This application analyzes user speech in real-time, evaluates pronunciation accuracy at the word level, provides AI-based feedback, and tracks progress over time.

---

## 🚀 Features

### ✍ Expected Sentence Input
User enters the sentence they want to practice.

### 🎙 Live Voice Recording
Built-in audio recording using Streamlit.

### 📝 Speech-to-Text (Whisper Model)
Uses OpenAI Whisper model to transcribe spoken audio.

### 📊 Word-Level Accuracy Analysis
Compares expected text and spoken text using similarity scoring.

### 🔎 Pronunciation Highlight
- Green → Correct pronunciation
- Red → Incorrect pronunciation

### 🎯 Overall Accuracy Score
Displays average pronunciation accuracy percentage.

### 🤖 Smart AI Feedback
Automatically identifies weak words and gives improvement suggestions.

### 📈 Progress Tracking
Stores daily accuracy scores and visualizes improvement using a line graph.

---

## 🧠 Technologies Used

- Python
- Streamlit
- OpenAI Whisper
- PyTorch
- Pronouncing (Phoneme Analysis)
- Pandas
- FFmpeg
- Difflib (SequenceMatcher)

---

## 📂 Project Structure
pronunciation_project/ │ ├── app.py ├── logic.py ├── requirements.txt ├── .gitignore └── README.md
Copy code

---

## ⚙ Installation Guide

### 1️⃣ Clone Repository
git clone https://github.com/yuvaraj9753/pronunciation_project.git cd pronunciation_project
Copy code

---

### 2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
Copy code

Activate:

**Windows**
venv\Scripts\activate
Copy code

**Mac/Linux**
source venv/bin/activate
Copy code

---

### 3️⃣ Install Required Packages
pip install -r requirements.txt
Copy code

---

### 4️⃣ Install FFmpeg (Important)

Whisper requires FFmpeg.

Download FFmpeg from:
https://ffmpeg.org/download.html

After installation:
Add the FFmpeg `bin` folder to your system PATH.

Verify installation:
ffmpeg -version
Copy code

If version appears → FFmpeg is installed correctly.

---

## ▶ Run the Application
streamlit run app.py
Copy code

The application will open automatically in your browser.

---

## 📊 How It Works

1. User enters expected sentence.
2. User records voice.
3. Whisper transcribes audio.
4. Word similarity is calculated.
5. Phoneme comparison is performed.
6. Accuracy score is generated.
7. AI feedback is displayed.
8. Progress is stored and visualized.

---

## 🎓 Academic Significance

This project demonstrates:

- Applied Natural Language Processing
- Speech Recognition Systems
- Pronunciation Evaluation Algorithms
- Phoneme Matching Techniques
- Real-time Data Processing
- AI Feedback Mechanism
- Data Visualization & Progress Analytics

---

## 🔮 Future Improvements

- Accent Detection
- Phoneme-Level Heatmap Visualization
- User Authentication System
- Cloud Deployment
- Deep Learning-based Scoring Enhancement

