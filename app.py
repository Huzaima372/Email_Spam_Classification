import gradio as gr
import pickle

# Load trained model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_spam(email_text):
    email_text = email_text.lower().strip()
    features = vectorizer.transform([email_text])
    prediction = model.predict(features)[0]
    
    if prediction == 0:
        return "✅ HAM (Not Spam)"
    else:
        return "🚨 SPAM"

# Gradio Interface
interface = gr.Interface(
    fn=predict_spam,
    inputs=gr.Textbox(lines=5, placeholder="Enter email text here..."),
    outputs="text",
    title="📧 Email Spam Classifier",
    description="A machine learning app that classifies emails as Spam or Ham using TF-IDF and Logistic Regression."
)

interface.launch()
