import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

# Load the custom model
model = tf.keras.models.load_model('severity_mnv2.keras')

# Function to preprocess the image
def preprocess_image(image):
    # Adjust as per your model's input size
    image = image.resize((224, 224))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = image / 255.0  # Assuming your model expects values in [0, 1]
    image = np.expand_dims(image, axis=0)
    return image

# Function to make predictions
def predict(image):
    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image)
    return predictions

# Streamlit app
def main():
    st.title("Accident Severity Classification")
    st.write("Upload an image")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Classify the image on button click
        if st.button("Classify"):
            predictions = predict(image)
            classes = ["fire", "minor", "moderate", "no_acc", "severe"]  # Adjust as per your classes
            class_index = np.argmax(predictions)
            st.write(f"Predicted Class: {classes[class_index]}")

if __name__ == "__main__":
    main()