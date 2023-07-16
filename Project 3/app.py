import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import pandas as pd


# Define class labels
class_names = [
    "Corn Common Rust",
    "Corn Gray Leaf Spot",
    "Corn Healthy",
    "Corn Northern Leaf Blight",
    "Potato Early Blight",
    "Potato Healthy",
    "Potato Late Blight",
    "Rice Brown Spot",
    "Rice Healthy",
    "Rice Leaf Blast",
    "Rice Neck Blast",
    "Wheat Brown Rust",
    "Wheat Healthy",
    "Wheat Yellow Rust"
]

# Define the function for image classification
def classify_image(image):
    # Preprocess the image
    image = image.resize((224, 224))  # Resize the image to match the model's input shape
    image = np.array(image)  # Convert image to numpy array
    image = image / 255.0  # Normalize the image
    
    # Reshape the image to match the model's input shape
    image = np.reshape(image, (1, 224, 224, 3))
    
    # Load the model
    model = tf.keras.models.load_model('efficientnet.h5')
    
    # Perform prediction
    predictions = model.predict(image)
    
    # Get the top 3 predicted classes and their confidences
    top_indices = np.argsort(predictions[0])[::-1][:3]  # Get the indices of top 3 classes
    top_classes = [class_names[i] for i in top_indices]
    top_confidences = [predictions[0][i] * 100 for i in top_indices]
    
    # Filter out predictions with 0% confidence
    valid_predictions = [(cls, conf) for cls, conf in zip(top_classes, top_confidences) if conf > 0]
    top_classes, top_confidences = zip(*valid_predictions)
    
    return top_classes, top_confidences

# Set page title
st.title(":red[Agricultural Crop Disease Classification]")

# Create the file uploader and submit button
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
submit_button = st.button("Predict")

if submit_button and uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image')
    
    # Classify the image
    top_classes, top_confidences = classify_image(image)
    
    # Prepare the result in DataFrame format
    valid_predictions_df = pd.DataFrame({
        "Class": top_classes,
        "Confidence (%)": top_confidences
    })
    
    # Filter out classes with 0% confidence
    valid_predictions_df = valid_predictions_df[valid_predictions_df["Confidence (%)"] > 0]
    
    # Display the top predictions with index starting from 1
    if not valid_predictions_df.empty:
        valid_predictions_df.index = range(1, len(valid_predictions_df) + 1)
        st.write("Top Predictions:")
        st.dataframe(valid_predictions_df)
    else:
        st.write("No valid predictions with confidence greater than 0%.")
