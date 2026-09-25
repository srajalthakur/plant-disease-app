<div align="center">

# 🌿 Plant Disease Recognition System

### AI-Powered Plant Disease Classification Using Deep Learning

<img src="home_page.jpeg" alt="Plant Disease Recognition System" width="850"/>

<br><br>

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge&logo=tensorflow&logoColor=white"/>
<img src="https://img.shields.io/badge/Keras-Deep%20Learning-red?style=for-the-badge&logo=keras&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>

<br>

<img src="https://img.shields.io/badge/Classes-38-success?style=flat-square"/>
<img src="https://img.shields.io/badge/Validation%20Accuracy-93.18%25-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/github/stars/srajalthakur/plant-disease-app?style=flat-square"/>
<img src="https://img.shields.io/github/license/srajalthakur/plant-disease-app?style=flat-square"/>

<br><br>

<b>🌱 Upload a leaf image → 🤖 Analyze with AI → 🔍 Identify the plant condition</b>

</div>

---

# 🌱 About The Project

The **Plant Disease Recognition System** is a deep-learning-based image classification application designed to recognize plant diseases from leaf images.

A custom **Convolutional Neural Network (CNN)** was trained using the **New Plant Diseases Dataset** and can classify plant leaf images into **38 different plant disease and healthy categories**.

The trained model is integrated into an interactive **Streamlit web application**, allowing users to upload a plant leaf image and receive a predicted class along with a confidence score.

---

# ✨ Key Features

| Feature | Description |
|---|---|
| 🌿 **38 Classes** | Classifies plant leaves into 38 disease/healthy categories |
| 🧠 **Custom CNN** | Deep learning model built using TensorFlow/Keras |
| 🎯 **93.18% Validation Accuracy** | Best validation accuracy achieved during training |
| 📷 **Image Upload** | Users can upload leaf images directly |
| ⚡ **Fast Prediction** | Generates predictions using the trained model |
| 📊 **Model Evaluation** | Includes classification report and confusion matrix |
| 🎨 **Interactive UI** | User-friendly Streamlit interface |
| ☁️ **Deployment Ready** | Can be deployed as a web application |

---

# 🧠 How The System Works

```text
                    🌿 PLANT LEAF IMAGE
                            │
                            ▼
                    📷 IMAGE UPLOAD
                            │
                            ▼
                    🖼️ PREPROCESSING
                            │
                            ▼
                       128 × 128
                            │
                            ▼
                    🧠 CNN MODEL
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
       FEATURE EXTRACTION          CLASSIFICATION
              │                           │
              └─────────────┬─────────────┘
                            ▼
                     🔍 PREDICTION
                            │
                            ▼
                 🌱 DISEASE / HEALTHY
                            │
                            ▼
                    📊 CONFIDENCE
