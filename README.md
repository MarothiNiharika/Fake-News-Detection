# 📰 Fake News Detection System

## 📌 Project Overview

This is a **Final Year Machine Learning Project** that detects whether a given news article is **FAKE** or **REAL** using **Natural Language Processing (NLP)** and **XGBoost Classifier**.
The project includes a **Streamlit web application** for user-friendly prediction.

---

## 🎯 Objectives

* Detect fake news using machine learning
* Apply NLP techniques on news text
* Build an interactive web application using Streamlit
* Deploy trained ML model for real-time prediction

---

## 🛠️ Technologies Used

* **Python**
* **Pandas, NumPy**
* **NLTK** (Text preprocessing)
* **Scikit-learn** (TF-IDF)
* **XGBoost Classifier**
* **Streamlit** (Web App)
* **VS Code**
* **Google Colab** (Model Training)

---

## 📂 Project Structure

```
Fake-News-Detection/
│
├── app.py                     # Streamlit web application
├── xgb_fake_news_model.pkl    # Trained XGBoost model
├── tfidf_vectorizer.pkl       # TF-IDF vectorizer
├── requirements.txt           # Required libraries
├── README.md                  # Project documentation
```

---

## 📊 Dataset

* **Fake.csv** → Fake news articles
* **True.csv** → Real news articles

The datasets were combined and labeled:

* `0` → Real News
* `1` → Fake News

---

## ⚙️ How the Model Works

1. Load Fake and True news datasets
2. Clean and preprocess text data
3. Convert text to numerical features using **TF-IDF**
4. Train model using **XGBoost Classifier**
5. Save trained model and vectorizer
6. Use Streamlit for prediction interface

---

## 🚀 How to Run the Project (VS Code)

### 1️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

### 2️⃣ Run Streamlit App

```bash
streamlit run app.py
```

### 3️⃣ Open Browser

The app will open at:

```
http://localhost:8501
```

---

## 🧪 Sample News for Testing

**True News Example:**

> The government announced a new economic policy aimed at boosting small businesses and increasing employment opportunities across the country.

**Fake News Example:**

> Scientists confirm that drinking a special herbal tea cures cancer in just three days without any medical treatment.

---

## 📈 Results

* Accurate classification of fake and real news
* Balanced predictions using XGBoost
* User-friendly web interface

---

## 🔮 Future Enhancements

* Add deep learning models (LSTM, BERT)
* Add confidence score to predictions
* Deploy on cloud platforms (Heroku / Render)
* Multi-language news detection

---

## 👩‍🎓 Academic Use

This project is suitable for:

* Final Year B.Tech / BCA / MCA Projects
* Machine Learning & Data Science portfolios

---

## 👩‍💻 Developed By

**Marothi Niharika**
Pre-Final Year Student
GitHub: https://github.com/MarothiNiharika

---

This project is fully functional, beginner-friendly, and resume-ready.
