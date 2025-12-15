import streamlit as st
import pickle
import re
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = stopwords.words('english')

# Load saved model
model = pickle.load(open("xgb_fake_news_model.pkl","rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl","rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = " ".join([w for w in text.split() if w not in stop_words])
    return text

st.set_page_config(page_title="Fake News Detection", page_icon="📰")
st.title("📰 Fake News Detection (XGBoost)")

news = st.text_area("Enter News Text")

if st.button("Predict"):
    if news.strip()=="":
        st.warning("Enter news text")
    else:
        cleaned = clean_text(news)
        vector = vectorizer.transform([cleaned])
        pred = model.predict(vector)[0]
        conf = model.predict_proba(vector)[0].max()

        if pred==1:
            st.error("🚨 FAKE NEWS")
        else:
            st.success("✅ REAL NEWS")
        st.write("Confidence:", round(conf*100,2), "%")
