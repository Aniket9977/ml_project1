import pickle
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

# Home
st.title("Prediction App")

# Input fields
st.header("Input Data")
gender = st.selectbox("Gender", ["male", "female"])
race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parental_level_of_education = st.selectbox("Parental Level of Education", [
    "some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"
])
lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
reading_score = st.number_input("Reading Score", min_value=0.0, max_value=100.0, step=0.1)
writing_score = st.number_input("Writing Score", min_value=0.0, max_value=100.0, step=0.1)

# Button to trigger prediction
if st.button("Predict"):
    # Create an instance of CustomData with input data
    data = CustomData(
        gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

    # Convert input data to DataFrame
    pred_df = data.get_data_as_data_frame()
    st.write("Input DataFrame:")
    st.write(pred_df)

    # Load the prediction pipeline and make predictions
    predicts_pipeline = PredictPipeline()
    results = predicts_pipeline.predict(pred_df)

    # Display the prediction
    st.write(f"Prediction: {results[0]}")
