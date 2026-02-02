import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.datasets import imdb

# Load the IMDB dataset word index 
word_index = imdb.get_word_index()
reversed_word_index = {value: key for (key, value) in word_index.items()}

#load the trained model
model = load_model('imdb_rnn_model.h5')

#function to decode review from indices to words
def decode_review(text_indices):
    return ' '.join([reversed_word_index.get(i - 3, '?') for i in text_indices])

#Function to preprocess input text
def preprocess_text(text):
    tokens = text.lower().split()
    sequence_indices = [word_index.get(word, 2) + 3 for word in tokens]
    padded_sequence = sequence.pad_sequences([sequence_indices], maxlen=400)
    return padded_sequence

#prediction function
def predict_review(review):
    # Preprocess the review
    review_seq = [word_index.get(word, 2) + 3 for word in review.lower().split()]
    review_seq = sequence.pad_sequences([review_seq], maxlen=400)
    
    # Predict sentiment
    prediction = model.predict(review_seq)
    sentiment = "Positive" if prediction[0][0] >= 0.5 else "Negative"
    confidence = prediction[0][0] if sentiment == "Positive" else 1 - prediction[0][0]
    
    return sentiment, confidence

#Streamlit app
import streamlit as st

st.title("IMDB Movie Review Sentiment Analysis")
st.write("Enter a movie review below to predict its sentiment.")

#user input
user_review = st.text_area("Movie Review")

if st.button("Predict Sentiment"):
    preprocess_text=preprocess_text(user_review)
    if user_review.strip() == "":
        st.write("Please enter a valid review.")
    else:
        sentiment, confidence = predict_review(user_review)
        st.write(f"Predicted Sentiment: **{sentiment}** (Confidence: {confidence:.4f})")
    #make prediction
    prediction = model.predict(preprocess_text)
    sentiment = "Positive" if prediction[0][0] >= 0.5 else "Negative"
    confidence = prediction[0][0] if sentiment == "Positive" else 1 - prediction[0][0]
    #display result
    st.write(f"Predicted Sentiment: **{sentiment}** (Confidence: {confidence:.4f})")