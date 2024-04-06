import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

"""
# Chest CT Scan Image Classifier
"""

# Load the trained model
model = tf.keras.models.load_model("model.h5")

# File uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Load and preprocess the image
    image = Image.open(uploaded_file).convert("RGB")  # Convert to RGB to remove alpha channel
    image = image.resize((224, 224))  # Resize the image to match model input size
    image_array = tf.keras.preprocessing.image.img_to_array(image)  # Convert PIL image to array
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

    # Predict
    predictions = model.predict(image_array)
    prediction_label = np.argmax(predictions)

    # Display prediction result
    if prediction_label == 0:
        st.image(image, caption="Predicted: Adenocarcinoma")
    elif prediction_label == 1:
        st.image(image, caption="Predicted: Large Cell Carcinoma")
    elif prediction_label == 2:
        st.image(image, caption="Predicted: Normal")
    else:
        st.image(image, caption="Predicted: Squamous Cell Carcinoma")