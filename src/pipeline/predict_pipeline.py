import sys
import os
import pandas as pd
from src.exception import CustomError
from src.utils import load_object
from src.logger import logging

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifact/model.pkl'
            preprocessor_path = 'artifact/processor.pkl'
            
            # Debugging statements
            print("Before Loading Model")
            model = load_object(file_path=model_path)
            print("Model Loaded Successfully")
            
            print("Before Loading Preprocessor")
            preprocessor = load_object(file_path=preprocessor_path)
            print("Preprocessor Loaded Successfully")
            
            # Transform the features
            data_scaled = preprocessor.transform(features)
            print("Features Transformed Successfully")
            
            # Make predictions
            preds = model.predict(data_scaled)
            print("Prediction Made Successfully")
            return preds

        except Exception as e:
            print(f"Error: {e}")
            raise CustomError(e, sys)

class CustomData:
    def __init__(self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education: str,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            logging.info('Data mapping successful')
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomError(e, sys)
