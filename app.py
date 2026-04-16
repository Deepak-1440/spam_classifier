import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📩 Spam vs Ham Classifier")

message = st.text_area("Enter your message")

if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter a message")
    else:
        transformed = vectorizer.transform([message])
        prediction = model.predict(transformed)

        if prediction[0] == 1:
            st.error("🚫 Spam Message")
        else:
            st.success("✅ Ham Message")