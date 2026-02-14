
import os
import tempfile
import csv
import datetime
import pandas as pd
import streamlit as st

from logic import speech_to_text, word_level_analysis, generate_feedback

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
    page_title="AI Pronunciation Evaluation System",
    page_icon="🎤",
    layout="wide"
)

st.markdown(
    "<h1 style='text-align: center;'>🎤 AI Pronunciation Evaluation System</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# ------------------------------
# INPUT SECTION
# ------------------------------
expected_text = st.text_input("✍ Enter Expected Sentence")

audio_file = st.audio_input("🎙 Record Your Voice")

if audio_file is not None:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(audio_file.read())
        temp_audio_path = tmp_file.name

    st.info("🔄 Transcribing... Please wait")

    spoken_text = speech_to_text(temp_audio_path)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📝 Spoken Text")
        st.info(spoken_text)

    if expected_text:

        df = word_level_analysis(expected_text, spoken_text)

        overall_accuracy = round(df["Score (%)"].mean(), 2)

        with col2:
            st.subheader("🎯 Overall Accuracy")
            st.metric(label="Accuracy", value=f"{overall_accuracy}%")

        st.markdown("---")

        # ------------------------------
        # WORD LEVEL TABLE
        # ------------------------------
        st.subheader("📊 Word-Level Analysis")
        st.dataframe(df)

        # ------------------------------
        # HIGHLIGHT INCORRECT WORDS
        # ------------------------------
        st.subheader("🔎 Pronunciation Highlight")

        words = expected_text.split()
        highlighted_text = ""

        for i, row in df.iterrows():
            if row["Score (%)"] > 80:
                highlighted_text += f"<span style='color:green; font-size:18px;'>{words[i]}</span> "
            else:
                highlighted_text += f"<span style='color:red; font-size:18px;'>{words[i]}</span> "

        st.markdown(highlighted_text, unsafe_allow_html=True)

        # ------------------------------
        # AI FEEDBACK
        # ------------------------------
        st.subheader("🤖 Smart AI Feedback")
        st.info(generate_feedback(df))

        # ------------------------------
        # SAVE PROGRESS
        # ------------------------------
        if not os.path.exists("progress.csv"):
            with open("progress.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Score"])

        with open("progress.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.datetime.now(), overall_accuracy])

        # ------------------------------
        # PROGRESS GRAPH
        # ------------------------------
        st.markdown("---")
        st.subheader("📈 Progress Tracking")

        progress_df = pd.read_csv("progress.csv")
        st.line_chart(progress_df["Score"])