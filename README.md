# Predictor App

This project is a Streamlit-based web application that predicts outcomes based on user input data. The application allows users to input various features, and it returns a prediction based on a pre-trained model.

## Features

- **Gender:** Select between male or female.
- **Race/Ethnicity:** Choose from groups A, B, C, D, or E.
- **Parental Level of Education:** Select the highest level of education completed by the parents.
- **Lunch:** Select the type of lunch received by the student (standard or free/reduced).
- **Test Preparation Course:** Indicate whether the test preparation course was completed.
- **Reading Score:** Input the reading score between 0.0 and 100.0.
- **Writing Score:** Input the writing score between 0.0 and 100.0.

## How It Works

1. **Input Data:** The user provides the necessary inputs via the web interface.
2. **Prediction:** The application uses a machine learning model to predict the outcome based on the input data.
3. **Display Result:** The predicted outcome is displayed on the interface.

## Project Structure

- `src/pipeline/predict_pipeline.py`: Contains the `PredictPipeline` and `CustomData` classes used to handle data and make predictions.
- `app.py`: The main Streamlit app file that contains the user interface and prediction logic.
- `models/`: This directory contains the pre-trained model saved as a pickle file.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/predictor-app.git
   cd predictor-app
