<div align="center">

# 🌿 Plant Disease Recognition System

### *AI-Powered Plant Disease Classification*

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-D00000?style=for-the-badge&logo=keras&logoColor=white)](https://keras.io/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![GitHub](https://img.shields.io/badge/GitHub-srajalthakur-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/srajalthakur)

<br/>

> **Upload a leaf. Let AI identify the disease. 🌱**
>
> A deep-learning-powered plant disease classification system built with TensorFlow, Keras and Streamlit.

<br/>

![Classes](https://img.shields.io/badge/Classes-38-22c55e?style=for-the-badge)
![Validation Accuracy](https://img.shields.io/badge/Validation%20Accuracy-93.18%25-16a34a?style=for-the-badge)
![Model](https://img.shields.io/badge/Model-Custom%20CNN-7c3aed?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-22c55e?style=for-the-badge)

</div>

---

## 🌐 Live Application

| | Link |
|---|---|
| 🚀 **Streamlit App** | Your deployed Render URL |
| 🐙 **GitHub Repository** | [github.com/srajalthakur/plant-disease-app](https://github.com/srajalthakur/plant-disease-app) |

> **Note:** The application is built with Streamlit and uses the trained CNN model `plant_disease_model.keras` for prediction.

---

## ✨ Features

### 🌿 Plant Disease Classification

- Classifies plant leaf images into **38 different categories**
- Includes both healthy and diseased plant classes
- Uses a custom Convolutional Neural Network
- Provides predicted disease/healthy class

### 🧠 Deep Learning Model

- Custom CNN architecture
- Built with TensorFlow and Keras
- Input image size: **128 × 128 × 3**
- Softmax output layer for 38 classes
- Adam optimizer
- Categorical crossentropy loss

### 📷 Image Prediction

- Upload a plant leaf image
- Automatically preprocesses the image
- Resizes image to `128 × 128`
- Passes image through trained CNN
- Displays predicted class
- Displays prediction confidence

### 📊 Model Evaluation

- Training accuracy
- Validation accuracy
- Classification report
- Precision
- Recall
- F1-score
- Confusion matrix

### 🎨 Interactive Web Application

- Built with Streamlit
- Simple image upload interface
- User-friendly prediction display
- Easy to run locally
- Deployment ready

---

## 🧠 How It Works

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
                    RESIZE 128×128
                           │
                           ▼
                    🧠 CNN MODEL
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       FEATURE EXTRACTION        CLASSIFICATION
              │                         │
              └────────────┬────────────┘
                           ▼
                    🔍 PREDICTION
                           │
                           ▼
                 🌱 DISEASE / HEALTHY
                           │
                           ▼
                    📊 CONFIDENCE
```

---

## 🏗️ CNN Architecture

```text
Input Image
128 × 128 × 3
      │
      ▼
┌─────────────────────┐
│ Conv2D - 16 Filters │
│      ReLU           │
└─────────────────────┘
      │
      ▼
┌─────────────────────┐
│    MaxPooling2D     │
└─────────────────────┘
      │
      ▼
┌─────────────────────┐
│ Conv2D - 32 Filters │
│      ReLU           │
└─────────────────────┘
      │
      ▼
┌─────────────────────┐
│    MaxPooling2D     │
└─────────────────────┘
      │
      ▼
┌─────────────────────┐
│ Conv2D - 64 Filters │
│      ReLU           │
└─────────────────────┘
      │
      ▼
┌─────────────────────┐
│    MaxPooling2D     │
└─────────────────────┘
      │
      ▼
┌──────────────────────┐
│ Conv2D - 128 Filters │
│       ReLU           │
└──────────────────────┘
      │
      ▼
┌─────────────────────┐
│    MaxPooling2D     │
└─────────────────────┘
      │
      ▼
┌────────────────────────────┐
│ Global Average Pooling     │
└────────────────────────────┘
      │
      ▼
┌─────────────────────┐
│ Dense - 128 Neurons │
│       ReLU          │
└─────────────────────┘
      │
      ▼
┌─────────────────────┐
│ Dense - 38 Classes  │
│      Softmax        │
└─────────────────────┘
      │
      ▼
🌿 FINAL PREDICTION
```

---

## 📊 Model Performance

The CNN achieved a best validation accuracy of approximately **93.18%**.

| Metric | Result |
|---|---|
| 🎯 Validation Accuracy | 93.18% |
| 🌿 Number of Classes | 38 |
| 🖼️ Input Resolution | 128 × 128 × 3 |
| 🧠 Model Type | Custom CNN |
| ⚙️ Optimizer | Adam |
| 📉 Loss Function | Categorical Crossentropy |
| 🔄 Training Epochs | 10 |

### 📈 Training Results

| Epoch | Training Accuracy | Validation Accuracy |
|---|---|---|
| 1 | 50.20% | 69.79% |
| 2 | 75.91% | 80.70% |
| 3 | 82.99% | 80.54% |
| 4 | 86.90% | 87.31% |
| 5 | 89.42% | 87.87% |
| 6 | 91.22% | 89.02% |
| 7 | 92.50% | 92.36% |
| 8 | 93.45% | 92.73% |
| 9 | 94.20% | 93.18% |
| 10 | 94.84% | 92.94% |

---

## 🔬 Model Evaluation

The trained model was evaluated using multiple machine-learning metrics.

### 📋 Classification Report

The classification report includes:

- Precision
- Recall
- F1-score
- Support

### 🔥 Confusion Matrix

A confusion matrix was generated to evaluate predictions across all 38 classes.

### 📈 Accuracy & Loss

Training and validation performance were monitored throughout the training process.

---

## 🌾 Dataset

**New Plant Diseases Dataset**

The model was trained using the New Plant Diseases Dataset available on Kaggle. The dataset contains images of healthy and diseased plant leaves across multiple plant species.

🔗 [Dataset](https://www.kaggle.com/)

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Programming Language | Python 3.11 |
| Deep Learning | TensorFlow |
| Neural Network | Keras |
| Model | Custom CNN |
| Image Processing | Pillow |
| Numerical Computing | NumPy |
| Visualization | Matplotlib |
| Evaluation | Scikit-learn |
| Web Application | Streamlit |
| Version Control | Git |
| Repository | GitHub |
| Deployment | Render |

---

## 📁 Project Structure

```text
plant-disease-app/
│
├── 🌿 main.py
├── 🧠 plant_disease_model.keras
├── 📦 requirements.txt
├── 🐍 .python-version
├── 🚫 .gitignore
├── 🖼️ home_page.jpeg
├── 📖 README.md
│
├── 📓 Train_plant_disease.ipynb
├── 📓 Test_plant_disease.ipynb
├── 📊 training_hist.json
│
└── 📁 test/
```

### 📂 Important Files

| File | Description |
|---|---|
| `main.py` | Streamlit web application |
| `plant_disease_model.keras` | Trained CNN model |
| `Train_plant_disease.ipynb` | Model training notebook |
| `Test_plant_disease.ipynb` | Individual image testing notebook |
| `training_hist.json` | Saved training history |
| `requirements.txt` | Required Python packages |
| `home_page.jpeg` | Application interface image |
| `.python-version` | Python version configuration |
| `.gitignore` | Excludes datasets and unnecessary files |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have:

- Python 3.11
- pip
- Git
- VS Code or another Python IDE

### Installation

**1. Clone the Repository**
```bash
git clone https://github.com/srajalthakur/plant-disease-app.git
```

**2. Open the Project**
```bash
cd plant-disease-app
```

**3. Create a Virtual Environment**
```bash
python -m venv venv
```

**4. Activate the Environment**

Windows:
```bash
venv\Scripts\activate
```

Linux / macOS:
```bash
source venv/bin/activate
```

**5. Install Dependencies**
```bash
pip install -r requirements.txt
```

**6. Run the Application**
```bash
streamlit run main.py
```

---

## 🖥️ Application Workflow

```text
👤 USER
  │
  ▼
📷 Upload Plant Leaf Image
  │
  ▼
🖼️ Image Preprocessing
  │
  ▼
📐 Resize to 128 × 128
  │
  ▼
🧠 CNN Prediction
  │
  ▼
🔍 Find Highest Probability
  │
  ▼
🌿 Predicted Disease / Healthy Class
  │
  ▼
📊 Confidence Score
```

---

## 🧪 Individual Image Testing

The `Test_plant_disease.ipynb` notebook can be used to test individual leaf images.

### Prediction Pipeline

```text
Leaf Image
    ↓
Load Image
    ↓
Resize to 128 × 128
    ↓
Convert Image to Array
    ↓
Add Batch Dimension
    ↓
CNN Prediction
    ↓
Find Highest Probability
    ↓
Display Predicted Class
    ↓
Display Confidence
```

---

## ☁️ Deployment

The application is designed for cloud deployment using Streamlit.

### Deployment Architecture

```text
              🐙 GitHub Repository
                       │
                       ▼
                 ☁️ Render
                       │
                       ▼
              🎨 Streamlit App
                       │
                       ▼
             🧠 CNN Model (.keras)
                       │
                       ▼
                🌿 Prediction
```

### Render Configuration

**Build Command**
```bash
pip install -r requirements.txt
```

**Start Command**
```bash
streamlit run main.py --server.address 0.0.0.0 --server.port $PORT
```

---

## 🔒 Dataset Management

The large training datasets are excluded from the GitHub repository.

The `.gitignore` file contains:

```text
train/
valid/
test/
__pycache__/
.ipynb_checkpoints/
*.pyc
```

This keeps the GitHub repository lightweight while preserving the trained model and application code.

---

## 📌 Model File

The Streamlit application loads:

```text
plant_disease_model.keras
```

The model was saved using the Keras format and loaded by the Streamlit application during prediction.

---

## 🚀 Future Improvements

### 🧠 Deep Learning
- [ ] Transfer learning
- [ ] MobileNet / EfficientNet
- [ ] Data augmentation
- [ ] Hyperparameter optimization
- [ ] Learning-rate scheduling
- [ ] Model compression

### 🌱 Agricultural Features
- [ ] Disease treatment recommendations
- [ ] Prevention recommendations
- [ ] Disease severity detection
- [ ] Crop-specific information
- [ ] Multilingual support

### 🎨 Application
- [ ] Modern dashboard
- [ ] Prediction probability charts
- [ ] Prediction history
- [ ] Drag-and-drop image upload
- [ ] Mobile-friendly interface

### ☁️ Deployment
- [ ] Docker support
- [ ] CI/CD pipeline
- [ ] Faster inference
- [ ] Production monitoring
- [ ] Automated model updates

---

## ⚠️ Disclaimer

This project is developed for educational and research purposes.

The predictions generated by the model should not be considered a replacement for professional agricultural diagnosis or expert advice.

For real agricultural decisions, consult a qualified agricultural professional.

---

## 👩‍💻 Author

<div align="center">

**🌿 Sraja Thakur**
Plant Disease Recognition System

B.Tech CSE

</div>

---

## ⭐ Support

If you found this project useful or interesting:

- ⭐ Star the repository
- 🍴 Fork the project
- 💡 Share your feedback

Your support is appreciated! 🌱

<div align="center">

### 🌿 Plant Disease Recognition System
*Turning Plant Images Into Intelligent Predictions*

<br/>

Built with ❤️ by Sraja Thakur

<br/>

🐍 Python &nbsp;•&nbsp; 🧠 TensorFlow &nbsp;•&nbsp; 🔥 Keras &nbsp;•&nbsp; 🎨 Streamlit

<br/><br/>

© 2026 Sraja Thakur

</div>
