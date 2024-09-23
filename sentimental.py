import streamlit as st
import joblib
import pickle

# Load the trained model
with open('your_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the preprocessing pipeline
preprocessing_pipeline = joblib.load('your_pipeline.joblib')

# Function to preprocess the text
def preprocess_text(text):
    preprocessed_text = preprocessing_pipeline.transform([text])
    return preprocessed_text

# Function to predict sentiment
def predict_sentiment(text):
    preprocessed_text = preprocess_text(text)
    prediction = model.predict(preprocessed_text)
    return prediction[0]

# Streamlit UI
def main():
    st.title('Sentiment Prediction App')
    st.write('Enter some text and I will predict its sentiment!')

    # Input text box
    text_input = st.text_area('Enter text:', '')

    if st.button('Predict'):
        # Make prediction
        if text_input:
            sentiment = predict_sentiment(text_input)
            st.write('Predicted Sentiment:', sentiment)
        else:
            st.write('Please enter some text.')

if __name__ == '__main__':
    main()