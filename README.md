# 📧 Email Spam Classification App

This project is a **Machine Learning–based Email Spam Classifier** that detects whether an email is **Spam** or **Ham (Not Spam)** using **TF-IDF** and **Logistic Regression**.

The model is trained on labeled email data and deployed using **Gradio** on **Hugging Face Spaces**.

---

## 🚀 Live Demo
Enter an email message and instantly get a prediction:
- **HAM** → Legitimate email
- **SPAM** → Unwanted or promotional email

---

## 🧠 Model Details
- **Algorithm:** Logistic Regression  
- **Feature Extraction:** TF-IDF Vectorization  
- **Dataset Labels:**  
  - `0` → Ham  
  - `1` → Spam  

---

## 📊 Model Performance
- **Training Accuracy:** ~96.7%
- **Testing Accuracy:** ~96.8%

**Classification Report (Test Set):**
- Precision (Spam): 1.00  
- Recall (Spam): 0.76  
- F1-score (Spam): 0.86  

---

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Pandas & NumPy
- Gradio
- Hugging Face Spaces

---

## 📥 How to Use
1. Type or paste an email message.
2. Click **Submit**.
3. The app will classify the email as **HAM** or **SPAM**.

---

## 📁 Files in This Repository

├── app.py # Gradio app

├── spam_model.sav # Trained ML model

├── vectorizer.sav # TF-IDF vectorizer

├── requirements.txt # Dependencies

└── README.md

---

## 👨‍💻 Author
**Huzaima Aneeq**  
Machine Learning Engineer
