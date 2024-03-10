import streamlit as st
from art import *
import colorama
import pytube
import os
import openai
from transformers import pipeline

class ChoiceException(Exception):
    def __init__(self, value):
        self.value = value

st.title("YouTube Transcript Translator")


input_link = st.text_input("Enter a valid YouTube Video Link: ")
target_language = st.text_input("Enter the  language  for translation (e.g. French): ")

if st.button("Generate Transcript"):
    try:
        yt = pytube.YouTube(input_link)
        st.write("⌛ We are working on generating your transcript... Please wait...")

        # Get the audio stream
        audio = yt.streams.filter(only_audio=True).first()

        # Download the audio in MP4 format
        audio_path = audio.download()

        # Convert the MP4 audio to WAV format using ffmpeg
        wav_filename = os.path.splitext(audio_path)[0] + '.wav'
        os.system(f'ffmpeg -i "{audio_path}" "{wav_filename}"')

        st.write("✅ TRANSCRIPT GENERATED SUCCESS!")

        # Display audio player
        st.audio(wav_filename, format='audio/wav')

        # Provide a button to download the audio file
        #st.markdown(f'<a href="{wav_filename}" download>Download Audio</a>', unsafe_allow_html=True)

        # Summarize the transcript
        cls = pipeline("automatic-speech-recognition")
        result = cls(wav_filename)

        # Ask the user for the target language

        # Set up OpenAI API key
        #openai.api_key = "Enter Your OpenAI API Key"

        translation_prompt = f"Translate the following English text to {target_language}: \n\n {result}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": translation_prompt},
            ]
        )

        translated_result = response["choices"][0]["message"]["content"]

        st.write("--------------------------------------------------------")
        st.write("--------------------------------------------------------")
     
        st.write("Original Summary: ")
        st.write(result)
      
        st.write(f"Translated Summary (to {target_language}): ")
        st.write(translated_result)
        st.download_button('Download  text', translated_result)

    except pytube.exceptions.RegexMatchError:
        st.error("🛑 Invalid URL! 🛑")
