import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
# Load the trained model
model = load_model('hamlet_next_word_model_GRU.h5')
# Load the tokenizer
with open('tokenizer_GRU.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

#Function to predict the next word
def predict_next_word(model, tokenizer, text, max_sequence_len):
    token_list = tokenizer.texts_to_sequences([text])[0]
    if len(token_list) >= max_sequence_len:
        token_list = token_list[-(max_sequence_len-1):]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
    predict = model.predict(token_list, verbose=0)
    predicted_index = np.argmax(predict, axis=-1)[0]
    for word, index in tokenizer.word_index.items():
        if index == predicted_index:
            return word

st.title("Next Word Prediction using GRU Model")
input_text = st.text_input("Enter a sequence of words:")
if st.button("Predict Next Word"):
    max_sequence_len = model.input_shape[1] + 1
    next_word = predict_next_word(model, tokenizer, input_text, max_sequence_len)
    st.write(f"Predicted Next Word: {next_word}")