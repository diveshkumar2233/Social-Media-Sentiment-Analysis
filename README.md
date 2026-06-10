# 📊 Social Media Sentiment Analysis

An **NLP-powered Sentiment Analysis Web Application** that classifies social media text into **Positive 😊** or **Negative 😞** sentiment using an **LSTM Deep Learning Model** built with **TensorFlow/Keras**.

The project includes:

* 🌐 **Interactive Web UI** using Flask
* ⚡ **FastAPI REST API** for real-time predictions
* 🧠 **LSTM-based Deep Learning Model**
* 🔍 **NLP Text Preprocessing** using NLTK
* 🎨 **Modern Responsive UI** with Bootstrap & Tailwind CSS

---

## 🚀 Features

✅ Predict sentiment from social media text

✅ Deep Learning model using **LSTM**

✅ Real-time sentiment analysis

✅ Confidence score prediction

✅ Text preprocessing:

* Lowercasing
* Stopword Removal
* Stemming
* Text Cleaning

✅ Responsive and modern UI

✅ REST API support using **FastAPI**

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* Tailwind CSS

### Backend

* Python
* Flask
* FastAPI

### Machine Learning / NLP

* TensorFlow / Keras
* LSTM
* NLTK
* NumPy
* Pickle

---

## 📂 Project Structure

```bash
Social_Media_Sentiment_Analysis/
│── app.py
│── fastapi_app.py
│── lstm_model.h5
│── tokenizer.pkl
│── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
[git clone https://github.com/your-username/Social_Media_Sentiment_Analysis.git](https://github.com/diveshkumar2233?tab=repositories)
```

### 2️⃣ Move to Project Folder

```bash
cd Social_Media_Sentiment_Analysis
```

### 3️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install flask fastapi uvicorn tensorflow nltk numpy
```

---

## ▶️ Run Flask Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## ⚡ Run FastAPI Server

```bash
uvicorn fastapi_app:app --reload
```

API URL:

```text
http://127.0.0.1:8000
```

Swagger API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🧠 Model Workflow

1. User enters social media text
2. Text preprocessing using **NLTK**
3. Convert text → sequence using tokenizer
4. Padding using `pad_sequences()`
5. LSTM model predicts sentiment
6. Display **Positive/Negative sentiment** with confidence score

---

## 🔮 Future Improvements

* Multi-class sentiment analysis (**Positive / Neutral / Negative**)
* Social media API integration
* Model deployment on cloud
* User authentication system
* Dark mode UI

---

## 👨‍💻 Author

**Divesh Kumar**

If you like this project, give it a ⭐ on GitHub!
