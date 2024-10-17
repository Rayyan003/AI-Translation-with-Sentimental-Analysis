import streamlit as st
from translate import Translator
from textblob import TextBlob

# Add custom CSS for enhanced UI and animations
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    .stApp {
        background: linear-gradient(135deg, #1c1c1c, #2a2a2a);
        color: #FFFFFF;
        font-family: 'Poppins', sans-serif;
        transition: background-color 0.3s, color 0.3s;
    }
    .stLightApp {
        background: linear-gradient(135deg, #f0f0f0, #e0e0e0);
        color: #000000;
        font-family: 'Poppins', sans-serif;
        transition: background-color 0.3s, color 0.3s;
    }
    .stTitle {
        text-align: center;
        color: #1E90FF;
        font-weight: 600;
        font-size: 32px;
        margin-bottom: 20px;
    }
    .stTextInput>div>div>input, .stTextArea>div>textarea {
        background-color: #444444;
        color: white;
        font-size: 18px;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #1E90FF;
    }
    .stLightTextInput>div>div>input, .stLightTextArea>div>textarea {
        background-color: #FFFFFF;
        color: black;
        font-size: 18px;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #1E90FF;
    }
    .stButton>button {
        background-color: #1E90FF;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        border: 2px solid #FFFFFF;
        transition: background-color 0.3s, transform 0.3s;
    }
    .stButton>button:hover {
        background-color: #00BFFF;
        transform: scale(1.05);
    }
    .result-card {
        background-color: #262626;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.5);
        margin: 20px 0;
        font-size: 18px;
        animation: fadeIn 1s ease-in-out;
        color: #FFFFFF;
    }
    .stLightResultCard {
        background-color: #FFFFFF;
        color: #000000;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
    }
    .stHeader {
        color: #FFFFFF;
    }
    .stLightHeader {
        color: #000000;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    footer {
        font-family: 'Poppins', sans-serif;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: #888;
    }
    </style>
""", unsafe_allow_html=True)


# Function to switch theme
def set_theme(dark_mode):
    if dark_mode:
        st.markdown("""
            <style>
            .stApp {
                background: linear-gradient(135deg, #1c1c1c, #2a2a2a);
                color: #FFFFFF;
            }
            .stHeader {
                color: #FFFFFF;
            }
            .stTextInput>div>div>input, .stTextArea>div>textarea {
                background-color: #444444;
                color: white;
            }
            .result-card {
                background-color: #262626;
                color: #FFFFFF;
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            .stApp {
                background: linear-gradient(135deg, #f0f0f0, #e0e0e0);
                color: #000000;
            }
            .stHeader {
                color: #000000;
            }
            .stTextInput>div>div>input, .stTextArea>div>textarea {
                background-color: #FFFFFF;
                color: black;
            }
            .result-card {
                background-color: #FFFFFF;
                color: #000000;
            }
            </style>
        """, unsafe_allow_html=True)


# Streamlit App
def main():
    st.markdown("<h1 class='stTitle'>AI-Based Multilingual Translation and Sentiment Analysis</h1>",
                unsafe_allow_html=True)

    # Sidebar options for dark/light mode
    dark_mode = st.sidebar.checkbox("Enable Dark Mode", value=True)
    set_theme(dark_mode)

    # Sidebar options for languages
    st.sidebar.header("Translation Settings")
    source_lang = st.sidebar.selectbox("Select Source Language", [
        "en", "es", "fr", "de", "zh", "hi", "ar", "ru", "ja", "ko", "it", "pt", "nl", "sv", "tr"
    ])
    target_lang = st.sidebar.selectbox("Select Target Language", [
        "en", "es", "fr", "de", "zh", "hi", "ar", "ru", "ja", "ko", "it", "pt", "nl", "sv", "tr"
    ])

    st.subheader("Enter Text to Translate:")
    user_input = st.text_area("")

    if st.button("Translate"):
        if user_input:
            # Perform translation using the `translate` package
            translator = Translator(from_lang=source_lang, to_lang=target_lang)
            translation = translator.translate(user_input)

            # Sentiment Analysis using TextBlob
            blob = TextBlob(user_input)
            sentiment = blob.sentiment.polarity

            # Display the results in a card with icons
            st.markdown("<div class='result-card'>", unsafe_allow_html=True)
            st.markdown("<h3 class='stHeader'>Translation</h3>", unsafe_allow_html=True)
            st.write(translation)
            st.markdown("<h3 class='stHeader'>Sentiment Analysis</h3>", unsafe_allow_html=True)

            # Load appropriate icons based on sentiment
            if sentiment > 0:
                st.image("https://img.icons8.com/color/48/000000/happy.png", width=40)
                st.write("Sentiment: Positive")
            elif sentiment < 0:
                st.image("https://img.icons8.com/color/48/000000/sad.png", width=40)
                st.write("Sentiment: Negative")
            else:
                st.image("https://img.icons8.com/color/48/000000/neutral.png", width=40)
                st.write("Sentiment: Neutral")

            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.error("Please enter text for translation.")

    # Footer
    st.markdown("<footer>Powered by Streamlit | Designed by Mohammed Rayyan Ahmed</footer>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
