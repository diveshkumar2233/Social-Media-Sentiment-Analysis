import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import pickle
import re
import nltk
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download stopwords
nltk.download("stopwords")

# Initialize Flask app
app = Flask(__name__)

# Load model and tokenizer
model = load_model("lstm_model.h5", compile=False)

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)


# Text preprocessing
def clean_text(text):
    ps = PorterStemmer()
    stop_words = set(stopwords.words("english"))

    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)

    words = text.split()
    words = [ps.stem(word) for word in words if word not in stop_words]

    return " ".join(words)


# Prediction function
def predict_sentiment(text):
    text = clean_text(text)

    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=100)

    prediction = model.predict(padded_sequence)[0][0]

    sentiment = "Positive 😊" if prediction > 0.5 else "Negative 😞"

    return sentiment, float(prediction)


# Home route
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    confidence = None
    text = ""

    if request.method == "POST":
        text = request.form.get("text")

        if text:
            result, confidence = predict_sentiment(text)

    return render_template(
        "index.html",
        result=result,
        confidence=round(confidence * 100, 2) if confidence is not None else None,
        text=text
    )


# Run app
if __name__ == "__main__":
    app.run(debug=True)