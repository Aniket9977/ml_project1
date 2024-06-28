import os 
import sys

from src.utils import save_object

from sklearn.ensemble import (
    AdaBoostClassifier,
    AdaBoostRegressor,
    GradientBoostingClassifier,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
 

from src.exception import CustomError
from src.logger import logging
from dataclasses import dataclass


@dataclass

class ModelTranierConfig:
    trained_model_dile_path = os.path.join('artifacts' ,'model.pkl') 

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTranierConfig()

    def initiate_model_trainer(self , train_array , test_array , preprocessor_path):
        try:
            logging.info("Splitting the data for traning and testing")
            x_train, y_train , x_test , y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            model_report:dict = evaluate_model(x)

        except Exception as e:
            raise CustomError(e,sys)