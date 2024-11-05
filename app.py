import streamlit as st
from gtts import gTTS  # Google Text-to-Speech
import os
from translate import Translator
from textblob import TextBlob


# Streamlit App
def main():
    st.title("AI-Based Multilingual Translation and Sentiment Analysis")

    # Sidebar for Dark/Light Mode
    dark_mode = st.sidebar.checkbox("Enable Dark Mode", value=True)
    text_color = "#FFFFFF" if dark_mode else "#000000"

    # Custom CSS for light/dark mode compatibility
    st.markdown(f"""
        <style>
        body {{
            background-color: {"#1e1e1e" if dark_mode else "#f5f5f5"};
        }}
        .stTextInput, .stTextArea {{
            background-color: {"#333333" if dark_mode else "#f0f0f0"};
            color: {text_color};
        }}
        </style>
    """, unsafe_allow_html=True)

    # Language selection for translation
    source_lang = st.sidebar.selectbox("Source Language", ["en", "es", "fr", "de", "zh", "hi", "ar", "ru", "ja", "ko"])
    target_lang = st.sidebar.selectbox("Target Language", ["en", "es", "fr", "de", "zh", "hi", "ar", "ru", "ja", "ko"])

    # Text Input
    user_input = st.text_area("Enter Text to Translate:", placeholder="Type something here...")

    if st.button("Translate"):
        if user_input:
            # Perform translation
            translator = Translator(from_lang=source_lang, to_lang=target_lang)
            translation = translator.translate(user_input)

            # Sentiment Analysis
            blob = TextBlob(user_input)
            sentiment = blob.sentiment.polarity

            # Display Results
            st.subheader("Translation")
            st.write(translation)

            st.subheader("Sentiment Analysis")
            if sentiment > 0:
                st.write("Sentiment: Positive 😊")
            elif sentiment < 0:
                st.write("Sentiment: Negative 😔")
            else:
                st.write("Sentiment: Neutral 😐")

            # Text-to-Speech and Download
            tts = gTTS(translation, lang=target_lang)
            tts.save("translation_audio.mp3")
            audio_file_path = "translation_audio.mp3"
            st.audio(audio_file_path, format="audio/mp3")
            st.download_button(
                label="Download Translation Audio",
                data=open(audio_file_path, "rb").read(),
                file_name="translation_audio.mp3",
                mime="audio/mp3"
            )
        else:
            st.error("Please enter some text to translate.")


if __name__ == "__main__":
    main()
