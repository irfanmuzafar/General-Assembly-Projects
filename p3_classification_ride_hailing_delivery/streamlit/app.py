import streamlit as st
from joblib import load
import pandas as pd

# Load your trained pipeline
pipeline = load('pipe_cvnb_gridsearch.joblib')

# App title
st.image('logo.png', width=150)
st.title('Ride Hailing vs Delivery Review Classifier')

# Create tabs for different input methods
tab1, tab2 = st.tabs(["⌨️ Manual Text Input", "📤 Upload CSV File"])

# Function to predict and display the outcome
def predict_and_display_outcome(input_text):
    prediction = pipeline.predict([input_text])
    if prediction == 0:
        st.write("The text is more likely related to Ride Hailing.")
    else:
        st.write("The text is more likely related to Delivery.")

# Manual Text Input Tab
with tab1:
    user_input = st.text_input("Enter your text here:")
    # If user manually inputs text, make a prediction
    if user_input:
        predict_and_display_outcome(user_input)

# Upload CSV File Tab
with tab2:
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        # Read the uploaded CSV file
        data = pd.read_csv(uploaded_file)
        if 'content' in data.columns:
            predictions = pipeline.predict(data['content'])
            data['Prediction'] = ['Ride Hailing' if pred == 0 else 'Delivery' for pred in predictions]
            # Display the DataFrame with predictions in the app
            st.write(data)
            
            # Optional: Allow users to download the CSV file with predictions
            def convert_df_to_csv(df):
                return df.to_csv().encode('utf-8')
            
            csv = convert_df_to_csv(data)
            st.download_button(
                label="Download data with predictions",
                data=csv,
                file_name='predictions.csv',
                mime='text/csv',
            )
        else:
            st.error("Please make sure the CSV file has a 'content' column.")
