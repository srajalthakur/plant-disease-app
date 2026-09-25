---
title: Plant Disease Recognition
emoji: 🌿
colorFrom: green
colorTo: yellow
sdk: streamlit
sdk_version: "1.38.0"
app_file: main.py
pinned: false
---

# Plant Disease Recognition System

A Streamlit app that classifies plant leaf images into 38 disease/healthy categories
using a CNN trained on the [New Plant Diseases Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset).

## Running locally

```bash
pip install -r requirements.txt
streamlit run main.py
```

Place your trained model file, `trained_plant_disease_model.keras`, in this same folder
before running — see the training notebook in this repo for how to produce it.
