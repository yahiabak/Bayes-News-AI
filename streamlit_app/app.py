import streamlit as st
import joblib
import re, string

# load model
model = joblib.load("../models/model.pkl")
vectorizer = joblib.load("../models/vectorizer.pkl")

# cleaning the text function
def clean_input(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.strip()


st.title("📰 BBC News Topic Classifier")

text_input = st.text_area("Paste a BBC news article here:")

if st.button("Classify"):
    if text_input:
        clean = clean_input(text_input)
        vect = vectorizer.transform([clean])
        pred = model.predict(vect)[0]
        st.success(f"**Predicted category:** {pred}")
    else:
        st.warning("Please enter some text above.")
