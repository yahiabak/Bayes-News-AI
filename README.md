# BayesNewsAI

An AI-powered classifier that predicts the category of BBC news articles using a Naive Bayes model.  
Built with `scikit-learn` and deployed via a live `Streamlit` web app.

## 🔍 Features

- Classifies news articles into 5 topics: `business`, `entertainment`, `politics`, `sport`, `tech`
- Cleans and vectorizes text using TF-IDF
- Trained with a Naive Bayes classifier (MultinomialNB)
- Real-time prediction via Streamlit interface
- Tracks input + prediction history


## 🚀 Run the Project

### 1. Clone the Repo

git clone https://github.com/YOUR_USERNAME/BayesNewsAI.git
cd BayesNewsAI
pip install -r requirements.txt
cd streamlit_app
streamlit run app.py
