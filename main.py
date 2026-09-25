import os
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

MODEL_PATH = "plant_disease_model.keras"

CLASS_NAMES = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy',
    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot',
    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

st.set_page_config(page_title="Plant Disease Recognition", page_icon="🌿", layout="wide")


@st.cache_resource
def load_model():
    """Load the trained model once and cache it across reruns."""
    if not os.path.exists(MODEL_PATH):
        return None
    return tf.keras.models.load_model(MODEL_PATH)


def model_prediction(model, image: Image.Image):
    """Run inference on a PIL image and return (predicted_index, confidence)."""
    image = image.convert("RGB").resize((128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.expand_dims(input_arr, axis=0)  # convert single image to batch
    predictions = model.predict(input_arr, verbose=0)[0]
    predicted_index = int(np.argmax(predictions))
    confidence = float(predictions[predicted_index])
    return predicted_index, confidence


# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition"])

# Home Page
if app_mode == "Home":
    st.header("PLANT DISEASE RECOGNITION SYSTEM")
    if os.path.exists("home_page.jpeg"):
        st.image("home_page.jpeg", use_container_width=True)
    st.markdown("""
    Welcome to the Plant Disease Recognition System! 🌿🔍

    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant,
    and our system will analyze it to detect any signs of disease. Together, let's protect our
    crops and ensure a healthier harvest!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Recognition** page in the sidebar to upload an image and experience
    the power of our Plant Disease Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    """)

# About Page
elif app_mode == "About":
    st.header("About")
    st.markdown("""
    #### About Dataset
    This dataset is recreated using offline augmentation from the original dataset. The original
    dataset can be found on this [Kaggle page](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset).
    It consists of about 87K RGB images of healthy and diseased crop leaves, categorized into
    38 different classes. The dataset is split 80/20 into training and validation sets, preserving
    the directory structure. A separate directory with 33 test images is used for prediction.

    #### Content
    1. train (70,295 images)
    2. test (33 images)
    3. validation (17,572 images)
    """)

# Prediction Page
elif app_mode == "Disease Recognition":
    st.header("Disease Recognition")

    model = load_model()
    if model is None:
        st.warning(
            f"⚠️ Model file `{MODEL_PATH}` was not found. Train the model using "
            "`Train_plant_disease.ipynb` and place the resulting `.keras` file in this folder "
            "(or point `MODEL_PATH` to it) before using this page."
        )

    test_image = st.file_uploader("Choose an image:", type=["jpg", "jpeg", "png"])

    if test_image is not None:
        image = Image.open(test_image)
        st.image(image, caption="Uploaded image", use_container_width=True)

        if st.button("Predict", disabled=model is None):
            with st.spinner("Analyzing image..."):
                result_index, confidence = model_prediction(model, image)
            st.success(
                f"Prediction: **{CLASS_NAMES[result_index]}** "
                f"(confidence: {confidence * 100:.1f}%)"
            )
    else:
        st.info("Upload an image above to get a prediction.")
