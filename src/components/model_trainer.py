import os
import sys
from src.exception import CustomException
from src.logger import logging

from catboost import CatBoostRegressor
from dataclasses import dataclass
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self,train_arr,test_arr):#,preprocessor_path
        try:
            logging.info("Splitting trainning and testing data")
            X_train,y_train,X_test,y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            models = {
                "RandomForestRegressor":RandomForestRegressor(),
                "DecisionTreeRegressor":DecisionTreeRegressor(),
                "GradientBoostingRegressor":GradientBoostingRegressor(),
                "LinearRegression":LinearRegression(),
                "KNeighborsRegressor":KNeighborsRegressor(),
                "XGBRegressor":XGBRegressor(),
                "CatBoostRegressor":CatBoostRegressor(),
                "AdaBoostRegressor":AdaBoostRegressor(),
            }

            model_report:dict = evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)

            #print(model_report)

            best_model_score = max(sorted(model_report.values()))
            
            #print(best_model_score)

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
                
            ]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No Best model found")
            logging.info("Best model found")

            save_object(
                file_path= self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)

            r2_sq = r2_score(y_test,predicted)
            return r2_sq
        

        except Exception as e:
            raise CustomException(e,sys)
            



