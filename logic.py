'''
import whisper
import pronouncing

# Load model once
model = whisper.load_model("base")

def speech_to_text(audio_path):
    """
    Converts speech audio to text using Whisper
    """
    result = model.transcribe(audio_path)
    return result["text"]

def get_phonemes(word):
    """
    Returns phonemes for a given word
    """
    phones = pronouncing.phones_for_word(word.lower())
    if phones:
        return phones[0].split()
    return []

def detect_pronunciation(expected_text, audio_path):
    """
    Main function:
    - speech to text
    - compare pronunciation
    """
    spoken_text = speech_to_text(audio_path)

    expected_words = expected_text.lower().split()
    spoken_words = spoken_text.lower().split()

    mistakes = []

    for ew, sw in zip(expected_words, spoken_words):
        e_ph = get_phonemes(ew)
        s_ph = get_phonemes(sw)

        if e_ph != s_ph:
            mistakes.append({
                "word": ew,
                "expected_phonemes": e_ph,
                "spoken_phonemes": s_ph
            })

    return spoken_text, mistakes '''

import whisper
import pronouncing
from difflib import SequenceMatcher
import pandas as pd

# 🔥 Model ko yaha load mat karo
model = None

def load_model():
    global model
    if model is None:
        model = whisper.load_model("base")
    return model


def speech_to_text(audio_path):
    model = load_model()
    result = model.transcribe(audio_path)
    return result["text"]


def get_phonemes(word):
    phones = pronouncing.phones_for_word(word.lower())
    if phones:
        return phones[0].split()
    return []


def word_level_analysis(expected_text, spoken_text):
    expected_words = expected_text.lower().split()
    spoken_words = spoken_text.lower().split()

    results = []

    for i in range(len(expected_words)):
        if i < len(spoken_words):
            similarity = SequenceMatcher(
                None, expected_words[i], spoken_words[i]
            ).ratio()
            score = round(similarity * 100, 2)
        else:
            score = 0

        expected_ph = get_phonemes(expected_words[i])
        spoken_ph = (
            get_phonemes(spoken_words[i])
            if i < len(spoken_words)
            else []
        )

        phoneme_match = expected_ph == spoken_ph

        results.append({
            "Word": expected_words[i],
            "Score (%)": score,
            "Phoneme Match": phoneme_match,
            "Status": "Correct" if score > 80 else "Incorrect"
        })

    df = pd.DataFrame(results)
    return df


def generate_feedback(df):
    weak_words = df[df["Score (%)"] < 80]["Word"].tolist()

    if not weak_words:
        return "Excellent pronunciation! Your articulation is clear and accurate."

    feedback = "You should improve pronunciation of: "
    feedback += ", ".join(weak_words)
    feedback += ". Try speaking slowly, clearly, and stress vowel sounds properly."

    return feedback
