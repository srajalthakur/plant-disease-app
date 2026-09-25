import os
import numpy as np
import tensorflow as tf
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Plant AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* =========================
       MAIN BACKGROUND
       ========================= */

    .stApp {
        background:
            radial-gradient(
                circle at 85% 10%,
                rgba(184, 134, 11, 0.08),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #050a0b 0%,
                #071011 45%,
                #0b1112 100%
            );
        color: #e8e1cf;
    }

    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 4rem;
        max-width: 1200px;
    }


    /* =========================
       SIDEBAR
       ========================= */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #061313 0%,
                #07100f 50%,
                #050b0b 100%
            );
        border-right: 1px solid rgba(193, 155, 55, 0.35);
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 2rem;
    }

    .sidebar-logo {
        text-align: center;
        padding: 1rem 0 2rem 0;
    }

    .logo-circle {
        width: 82px;
        height: 82px;
        margin: auto;
        border: 1px solid #c9a227;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 38px;
        background: rgba(201, 162, 39, 0.04);
        box-shadow: 0 0 25px rgba(201, 162, 39, 0.12);
    }

    .brand-name {
        margin-top: 18px;
        color: #d9b43c;
        font-family: Georgia, serif;
        font-size: 25px;
        font-weight: bold;
        letter-spacing: 1px;
    }

    .brand-tagline {
        margin-top: 8px;
        color: #819a9a;
        font-size: 10px;
        letter-spacing: 3px;
        text-transform: uppercase;
    }

    .sidebar-divider {
        height: 1px;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(201, 162, 39, 0.25),
            transparent
        );
        margin: 0 5px 2rem 5px;
    }


    /* =========================
       NAVIGATION
       ========================= */

    .nav-title {
        color: #d8cfae;
        font-size: 12px;
        font-weight: bold;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }


    /* =========================
       MODEL STATUS
       ========================= */

    .status-card {
        margin-top: 35px;
        padding: 20px;
        border: 1px solid rgba(201, 162, 39, 0.22);
        border-radius: 16px;
        background: rgba(15, 28, 27, 0.75);
    }

    .status-title {
        color: #d5ad32;
        font-family: Georgia, serif;
        font-size: 14px;
        letter-spacing: 0.5px;
        margin-bottom: 15px;
    }

    .status-online {
        color: #81d8ad;
        font-size: 13px;
        margin-bottom: 15px;
    }

    .status-line {
        color: #9caeac;
        font-size: 13px;
        margin: 8px 0;
    }

    .status-value {
        color: #e0b52f;
        font-weight: bold;
    }


    /* =========================
       HERO
       ========================= */

    .hero-section {
        padding: 50px 0 35px 0;
    }

    .hero-eyebrow {
        color: #d4a929;
        font-size: 12px;
        font-weight: bold;
        letter-spacing: 4px;
        margin-bottom: 18px;
    }

    .hero-title {
        color: #f1e5c5;
        font-family: Georgia, serif;
        font-size: clamp(35px, 4vw, 58px);
        line-height: 1.08;
        margin: 0;
    }

    .hero-text {
        color: #91a3a4;
        font-size: 17px;
        line-height: 1.8;
        max-width: 760px;
        margin-top: 22px;
    }


    /* =========================
       STAT CARDS
       ========================= */

    .stat-card {
        min-height: 125px;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid rgba(201, 162, 39, 0.18);
        background:
            linear-gradient(
                145deg,
                rgba(18, 34, 32, 0.9),
                rgba(8, 17, 17, 0.9)
            );
        text-align: center;
    }

    .stat-number {
        color: #ddb632;
        font-family: Georgia, serif;
        font-size: 28px;
        font-weight: bold;
        margin-top: 10px;
    }

    .stat-label {
        color: #879999;
        font-size: 12px;
        margin-top: 7px;
        letter-spacing: 0.5px;
    }


    /* =========================
       CONTENT CARD
       ========================= */

    .content-card {
        margin-top: 35px;
        padding: 40px;
        border: 1px solid rgba(201, 162, 39, 0.18);
        border-radius: 20px;
        background:
            linear-gradient(
                145deg,
                rgba(16, 29, 29, 0.88),
                rgba(7, 14, 15, 0.92)
            );
    }

    .section-eyebrow {
        color: #d5aa2f;
        font-size: 11px;
        letter-spacing: 3px;
        font-weight: bold;
        margin-bottom: 12px;
    }

    .content-card h2 {
        color: #f0e4c3;
        font-family: Georgia, serif;
        font-size: 30px;
        margin-top: 5px;
    }

    .content-card p {
        color: #94a5a5;
        line-height: 1.8;
        font-size: 15px;
    }


    /* =========================
       FEATURE BOXES
       ========================= */

    .feature-box {
        padding: 22px;
        margin-top: 20px;
        border: 1px solid rgba(201, 162, 39, 0.14);
        border-radius: 15px;
        background: rgba(8, 17, 17, 0.65);
        height: 100%;
    }

    .feature-icon {
        font-size: 27px;
        margin-bottom: 10px;
    }

    .feature-box h3 {
        color: #e0c45d;
        font-family: Georgia, serif;
        font-size: 19px;
    }

    .feature-box p {
        color: #859595;
        font-size: 13px;
        line-height: 1.6;
    }


    /* =========================
       IMAGE
       ========================= */

    .image-card {
        margin-top: 35px;
        border-radius: 20px;
        overflow: hidden;
        border: 1px solid rgba(201, 162, 39, 0.2);
    }


    /* =========================
       CTA
       ========================= */

    .cta-card {
        margin-top: 35px;
        padding: 45px 25px;
        text-align: center;
        border: 1px solid rgba(201, 162, 39, 0.2);
        border-radius: 20px;
        background:
            radial-gradient(
                circle at center,
                rgba(201, 162, 39, 0.08),
                transparent 60%
            ),
            #0a1414;
    }

    .cta-icon {
        font-size: 38px;
        margin-bottom: 12px;
    }

    .cta-card h2 {
        color: #e4c65e;
        font-family: Georgia, serif;
    }

    .cta-card p {
        color: #879999;
        font-size: 14px;
        line-height: 1.7;
    }


    /* =========================
       PREDICTION CARD
       ========================= */

    .prediction-card {
        margin-top: 30px;
        padding: 35px;
        border: 1px solid rgba(201, 162, 39, 0.25);
        border-radius: 20px;
        background:
            linear-gradient(
                145deg,
                rgba(14, 28, 27, 0.95),
                rgba(7, 14, 15, 0.95)
            );
    }

    .prediction-title {
        color: #e3c35b;
        font-family: Georgia, serif;
        font-size: 28px;
        margin-bottom: 10px;
    }

    .prediction-label {
        color: #879999;
        font-size: 14px;
    }

    .result-card {
        margin-top: 25px;
        padding: 30px;
        border-radius: 18px;
        border: 1px solid rgba(201, 162, 39, 0.3);
        background: rgba(201, 162, 39, 0.045);
        text-align: center;
    }

    .result-label {
        color: #9aa9a8;
        font-size: 12px;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .result-name {
        color: #e6c75c;
        font-family: Georgia, serif;
        font-size: 30px;
        margin-top: 12px;
    }

    .confidence {
        color: #8fd5ae;
        font-size: 16px;
        margin-top: 10px;
    }


    /* =========================
       ABOUT
       ========================= */

    .about-box {
        margin-top: 25px;
        padding: 30px;
        border-radius: 18px;
        border: 1px solid rgba(201, 162, 39, 0.18);
        background: rgba(12, 24, 24, 0.75);
    }

    .about-box h3 {
        color: #e1c158;
        font-family: Georgia, serif;
        font-size: 21px;
    }

    .about-box p {
        color: #91a2a2;
        line-height: 1.8;
        font-size: 14px;
    }


    /* =========================
       FOOTER
       ========================= */

    .footer {
        text-align: center;
        padding: 45px 0 15px 0;
        color: #596c6c;
        font-size: 12px;
    }

    .footer span {
        color: #cba62e;
    }


    /* =========================
       STREAMLIT ELEMENTS
       ========================= */

    div[data-testid="stFileUploader"] {
        border: 1px solid rgba(201, 162, 39, 0.25);
        border-radius: 15px;
        padding: 10px;
        background: rgba(10, 20, 20, 0.75);
    }

    div[data-testid="stFileUploader"] section {
        background: transparent;
    }

    .stButton > button {
        background: linear-gradient(
            135deg,
            #b9901f,
            #d6b13b
        );
        color: #07100f;
        border: none;
        border-radius: 10px;
        font-weight: bold;
        padding: 10px 25px;
    }

    .stButton > button:hover {
        background: linear-gradient(
            135deg,
            #d6b13b,
            #e4c75b
        );
        color: #07100f;
    }

    /* Hide Streamlit default footer */
    footer {
        visibility: hidden;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# MODEL
# ============================================================

MODEL_PATH = "plant_disease_model.keras"


@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)


try:
    model = load_model()
    model_status = True
except Exception:
    model = None
    model_status = False


# ============================================================
# CLASS NAMES
# ============================================================

class_name = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html("""
    <div class="sidebar-logo">

        <div class="logo-circle">
            🌿
        </div>

        <div class="brand-name">
            PLANT AI
        </div>

        <div class="brand-tagline">
            Intelligent Botanical Analysis
        </div>

    </div>

    <div class="sidebar-divider"></div>
    """)

    st.markdown(
        '<div class="nav-title">NAVIGATION</div>',
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "🔬 Disease Prediction",
            "ℹ️ About"
        ],
        index=0,
        label_visibility="collapsed"
    )

    if model_status:
        status_html = """
        <div class="status-card">

            <div class="status-title">
                ✦ MODEL STATUS
            </div>

            <div class="status-online">
                ● CNN model online
            </div>

            <div class="status-line">
                <span class="status-value">38</span>
                plant classes
            </div>

            <div class="status-line">
                <span class="status-value">93.18%</span>
                validation accuracy
            </div>

            <div class="status-line">
                Input:
                <span class="status-value">128 × 128</span>
            </div>

        </div>
        """

    else:
        status_html = """
        <div class="status-card">

            <div class="status-title">
                ✦ MODEL STATUS
            </div>

            <div class="status-online">
                ● Model unavailable
            </div>

        </div>
        """

    st.html(status_html)


# ============================================================
# HOME PAGE
# ============================================================

if page == "🏠 Home":

    st.html("""
    <div class="hero-section">

        <div class="hero-eyebrow">
            ✦ INTELLIGENT BOTANICAL ANALYSIS
        </div>

        <h1 class="hero-title">
            Discover What Your Plant Is Telling You
        </h1>

        <p class="hero-text">
            Harness the power of deep learning to understand plant health.
            Plant AI uses a convolutional neural network to recognize
            plant diseases across 38 different classes.
        </p>

    </div>
    """)


    # ========================================================
    # STATISTICS
    # ========================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.html("""
        <div class="stat-card">
            <div class="stat-number">38</div>
            <div class="stat-label">Plant Classes</div>
        </div>
        """)

    with col2:
        st.html("""
        <div class="stat-card">
            <div class="stat-number">93.18%</div>
            <div class="stat-label">Validation Accuracy</div>
        </div>
        """)

    with col3:
        st.html("""
        <div class="stat-card">
            <div class="stat-number">CNN</div>
            <div class="stat-label">Deep Learning Model</div>
        </div>
        """)

    with col4:
        st.html("""
        <div class="stat-card">
            <div class="stat-number">128²</div>
            <div class="stat-label">Input Resolution</div>
        </div>
        """)


    # ========================================================
    # HOW IT WORKS
    # ========================================================

    st.html("""
    <div class="content-card">

        <div class="section-eyebrow">
            ✦ HOW IT WORKS
        </div>

        <h2>
            Intelligent Plant Disease Recognition
        </h2>

        <p>
            Plant AI analyzes plant leaf images using a trained
            convolutional neural network. The system identifies
            visual patterns associated with different plant diseases
            and provides a predicted class with a confidence score.
        </p>

    </div>
    """)


    # ========================================================
    # THREE FEATURES
    # ========================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.html("""
        <div class="feature-box">

            <div class="feature-icon">
                📷
            </div>

            <h3>
                Upload
            </h3>

            <p>
                Provide a clear photograph of a plant leaf
                through the Disease Prediction page.
            </p>

        </div>
        """)

    with col2:
        st.html("""
        <div class="feature-box">

            <div class="feature-icon">
                🧠
            </div>

            <h3>
                Analyze
            </h3>

            <p>
                The CNN model processes the image and extracts
                important visual features.
            </p>

        </div>
        """)

    with col3:
        st.html("""
        <div class="feature-box">

            <div class="feature-icon">
                ✦
            </div>

            <h3>
                Recognize
            </h3>

            <p>
                Receive the predicted plant disease and
                model confidence.
            </p>

        </div>
        """)


    # ========================================================
    # HOME IMAGE
    # ========================================================

    if os.path.exists("home_page.jpeg"):

        st.html("""
        <div class="image-card">
        """)

        st.image(
            "home_page.jpeg",
            width="stretch"
        )

        st.html("""
        </div>
        """)


    # ========================================================
    # CALL TO ACTION
    # ========================================================

    st.html("""
    <div class="cta-card">

        <div class="cta-icon">
            🌱
        </div>

        <h2>
            Ready to Analyze Your Plant?
        </h2>

        <p>
            Open <b>Disease Prediction</b> from the sidebar
            to upload a leaf image and begin intelligent
            disease recognition.
        </p>

    </div>
    """)


# ============================================================
# DISEASE PREDICTION PAGE
# ============================================================

elif page == "🔬 Disease Prediction":

    st.html("""
    <div class="hero-section">

        <div class="hero-eyebrow">
            ✦ INTELLIGENT ANALYSIS
        </div>

        <h1 class="hero-title">
            Plant Disease Prediction
        </h1>

        <p class="hero-text">
            Upload a clear image of a plant leaf and let the
            trained CNN model analyze it.
        </p>

    </div>
    """)


    # ========================================================
    # UPLOAD SECTION
    # ========================================================

    st.html("""
    <div class="prediction-card">

        <div class="prediction-title">
            Analyze Your Plant
        </div>

        <div class="prediction-label">
            Supported formats: JPG, JPEG, PNG
        </div>

    </div>
    """)

    uploaded_file = st.file_uploader(
        "Upload your plant leaf image",
        type=["jpg", "jpeg", "png"],
        label_visibility="visible"
    )


    # ========================================================
    # PREDICTION
    # ========================================================

    if uploaded_file is not None:

        if model is None:

            st.error(
                "The plant disease model could not be loaded."
            )

        else:

            # Display uploaded image
            st.image(
                uploaded_file,
                caption="Uploaded Plant Leaf",
                width="stretch"
            )

            # Open image
            img = tf.keras.preprocessing.image.load_img(
                uploaded_file,
                target_size=(128, 128)
            )

            input_arr = tf.keras.preprocessing.image.img_to_array(
                img
            )

            input_arr = np.expand_dims(
                input_arr,
                axis=0
            )

            # Prediction
            predictions = model.predict(
                input_arr,
                verbose=0
            )

            result_index = int(
                np.argmax(predictions[0])
            )

            confidence = float(
                np.max(predictions[0]) * 100
            )

            predicted_class = class_name[result_index]


            # =================================================
            # FORMAT DISEASE NAME
            # =================================================

            display_name = predicted_class.replace(
                "___",
                " — "
            )

            display_name = display_name.replace(
                "_",
                " "
            )


            # =================================================
            # RESULT
            # =================================================

            st.html(f"""
            <div class="result-card">

                <div class="result-label">
                    PREDICTED PLANT CONDITION
                </div>

                <div class="result-name">
                    {display_name}
                </div>

                <div class="confidence">
                    Confidence: {confidence:.2f}%
                </div>

            </div>
            """)


            # =================================================
            # HEALTH STATUS
            # =================================================

            if "healthy" in predicted_class.lower():

                st.success(
                    "🌿 The model predicts that this plant appears healthy."
                )

            else:

                st.warning(
                    "⚠️ The model detected a possible plant disease."
                )


            # =================================================
            # TOP 3 PREDICTIONS
            # =================================================

            st.write("")

            st.html("""
            <div class="section-eyebrow">
                ✦ TOP PREDICTIONS
            </div>
            """)

            top_indices = np.argsort(
                predictions[0]
            )[-3:][::-1]

            for index in top_indices:

                prediction_name = class_name[index]

                prediction_name = prediction_name.replace(
                    "___",
                    " — "
                )

                prediction_name = prediction_name.replace(
                    "_",
                    " "
                )

                prediction_confidence = (
                    predictions[0][index] * 100
                )

                st.write(
                    f"**{prediction_name}** — "
                    f"{prediction_confidence:.2f}%"
                )


# ============================================================
# ABOUT PAGE
# ============================================================

elif page == "ℹ️ About":

    st.html("""
    <div class="hero-section">

        <div class="hero-eyebrow">
            ✦ ABOUT PLANT AI
        </div>

        <h1 class="hero-title">
            Intelligent Botanical Analysis
        </h1>

        <p class="hero-text">
            Plant AI is a deep-learning based plant disease
            classification system designed to identify diseases
            from plant leaf images.
        </p>

    </div>
    """)


    # ========================================================
    # PROJECT
    # ========================================================

    st.html("""
    <div class="about-box">

        <h3>
            🌿 About the Project
        </h3>

        <p>
            This project uses a Convolutional Neural Network (CNN)
            trained on a plant disease image dataset. The trained
            model can classify plant leaf images into 38 different
            plant health categories.
        </p>

    </div>
    """)


    # ========================================================
    # MODEL
    # ========================================================

    st.html("""
    <div class="about-box">

        <h3>
            🧠 Model Architecture
        </h3>

        <p>
            The model contains multiple convolutional layers,
            max-pooling layers, a global average pooling layer,
            and fully connected layers before the final
            38-class softmax output.
        </p>

        <p>
            Input image size:
            <b>128 × 128 × 3</b>
        </p>

        <p>
            Output classes:
            <b>38</b>
        </p>

        <p>
            Validation accuracy:
            <b>93.18%</b>
        </p>

    </div>
    """)


    # ========================================================
    # TECHNOLOGIES
    # ========================================================

    st.html("""
    <div class="about-box">

        <h3>
            ⚙️ Technologies Used
        </h3>

        <p>
            <b>Python</b> — Programming language
        </p>

        <p>
            <b>TensorFlow / Keras</b> — Deep learning model
        </p>

        <p>
            <b>NumPy</b> — Numerical processing
        </p>

        <p>
            <b>Streamlit</b> — Interactive web application
        </p>

        <p>
            <b>Render</b> — Application deployment
        </p>

    </div>
    """)


    # ========================================================
    # DISCLAIMER
    # ========================================================

    st.html("""
    <div class="about-box">

        <h3>
            ⚠️ Important Note
        </h3>

        <p>
            This application is intended for educational and
            research purposes. Predictions are generated by a
            machine-learning model and should not be treated as
            professional agricultural diagnosis.
        </p>

    </div>
    """)


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="footer">

    Plant AI · Intelligent Botanical Analysis
    <br><br>
    Built with <span>♥</span> using TensorFlow & Streamlit

</div>
""")