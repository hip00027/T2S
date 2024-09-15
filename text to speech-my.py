# app.py

import streamlit as st
import pyttsx3

# Initialize the TTS engine with configuration options
def initialize_tts_engine(voice_id=0, rate=150, volume=0.8):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Set voice based on user selection (male or female)
    if voice_id < len(voices):
        engine.setProperty('voice', voices[voice_id].id)
    else:
        engine.setProperty('voice', voices[0].id)  # Fallback to default
    engine.setProperty('rate', rate)  # Set speech rate
    engine.setProperty('volume', volume)  # Set volume
    return engine

# Function to convert text to speech using pyttsx3
def pyttsx3_speech(text, voice_id=0, rate=150, volume=0.8):
    engine = initialize_tts_engine(voice_id, rate, volume)
    audio_file = "output_pyttsx3.wav"
    engine.save_to_file(text, audio_file)
    engine.runAndWait()
    return audio_file

# Custom CSS for UI styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f8ff;
    }
    .stButton>button {
        background-color: #6c63ff;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        transition-duration: 0.4s;
    }
    .stButton>button:hover {
        background-color: #4c40bf;
        color: white;
        border: 2px solid #4CAF50;
    }
    .stRadio>label {
        font-size: 18px;
        color: #6c63ff;
    }
    .stTextArea>label {
        font-size: 18px;
        color: #ff6347;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a two-column layout with adjusted ratio
col1, col2 = st.columns([2, 3])  # Adjust the ratio to make the video column larger

# Left column - Video
with col1:
    st.header("Welcome to TTS App")
    # Display the video using the provided path
    st.video(r"D:\Naresh i Class\Sept 2024\13 Sep 24\invideo-ai-1080 How to Use Text-to-Speech_ Male or Femal 2024-09-14.mp4")

# Right column - Text-to-Speech Functionality
with col2:
    st.title("TEXT - TO - SPEECH APPLICATION")

    # Text input for text-to-speech conversion
    text_input = st.text_area("Enter the text you want to convert to speech:", 
                              value="", placeholder="Type your text here...")

    # Voice selection (male or female)
    voice_type = st.radio("Select Voice Type", [0, 1], format_func=lambda x: "Male" if x == 0 else "Female")

    # Speech rate slider
    rate = st.slider("Adjust Speech Rate", 100, 200, 150)

    # Volume slider
    volume = st.slider("Adjust Volume", 0.5, 1.0, 0.8)

    # Predefined text samples
    st.write("Or choose from a predefined sample:")
    sample_texts = ["Hello, welcome to our application!", 
                    "This is a sample text to demonstrate the text-to-speech capabilities.", 
                    "Enjoy experimenting with the voices!"]
    selected_sample = st.selectbox("Sample Texts", sample_texts)

    # Button to convert text to speech using pyttsx3
    if st.button("Convert Text to Speech"):
        if text_input.strip() or selected_sample:  # Check if text input or a sample is selected
            speech_text = text_input if text_input.strip() else selected_sample
            audio_file_pyttsx3 = pyttsx3_speech(speech_text, voice_id=voice_type, rate=rate, volume=volume)
            st.audio(audio_file_pyttsx3, format='audio/wav')
            with open(audio_file_pyttsx3, "rb") as file:
                st.download_button("Download Speech", file, file_name="speech_pyttsx3.wav")
        else:
            st.warning("Please enter text or select a sample to convert to speech.")

# Sidebar with additional info or branding
st.sidebar.title("📢 About This App")
st.sidebar.info(
    """
    This Text-to-Speech application allows you to convert text into spoken words using both male and female voices.
    You can adjust the speech rate and volume to suit your preferences. Enjoy experimenting with different settings!
    """
)
