import pandas as pd
import re
import joblib

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

analyzer = SentimentIntensityAnalyzer()

MODEL_PATH = "fake_news_model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"

def load_dataset(true_path, fake_path):
    true_df = pd.read_csv(true_path)
    fake_df = pd.read_csv(fake_path)

    true_df["label"] = 1
    fake_df["label"] = 0

    df = pd.concat([true_df, fake_df], ignore_index=True)

    df["content"] = df["title"].fillna("") + " " + df["text"].fillna("")

    return df[["content", "label"]]

def clean_text(text):
    text = str(text).lower()
    text = text.encode("ascii", "ignore").decode()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def get_sentiment(text):
    score = analyzer.polarity_scores(text)
    compound = score["compound"]

    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def train_model(df):

    df["content"] = df["content"].apply(clean_text)

    X = df["content"]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # TF-IDF
    vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)

    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Logistic Regression
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    # Evaluate
    preds = model.predict(X_test_vec)
    acc = accuracy_score(y_test, preds)

    print("Model Accuracy:", acc)

    # Save model + vectorizer
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)

    print("Model saved successfully!")

    return model, vectorizer

def load_model():

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    return model, vectorizer

def predict_fake_news(text, model, vectorizer):

    clean = clean_text(text)

    sentiment = get_sentiment(clean)

    vec = vectorizer.transform([clean])
    prediction = model.predict(vec)[0]
    probability = model.predict_proba(vec)[0]

    fake_probability = round(probability[0], 2)  # class 0 = fake

    if prediction == 0:
        label = "Potential Fake News"
    else:
        label = "Likely Real News"

    return {
        "sentiment": sentiment,
        "fake_probability": fake_probability,
        "label": label
    }
