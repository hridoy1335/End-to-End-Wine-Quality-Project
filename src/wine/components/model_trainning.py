import sys
from src.wine.constants import *
from dataclasses import dataclass
from src.wine.utils import save_obj
from src.wine.logger import logging
from src.wine.config.configuration import *
from src.wine.exception import WineException
from sklearn.ensemble import RandomForestClassifier
from src.wine.components.model_evaluation import model_evaluation


@dataclass
class ModelTrainingConfig:
    model_training_file: str = MODEL_TRAINING_OBJ_FILE
    
class ModelTraining:
    def __init__(self):
        self.model_training_config = ModelTrainingConfig()
        
    def initiate_model_training(self, train_arr_path, test_arr_path):
        try:
            logging.info("model training is initiated")
            X_train,y_train,X_test,y_test = (train_arr_path[:,:-1], train_arr_path[:,-1],
                                             test_arr_path[:,:-1], test_arr_path[:,-1])
            
            model = RandomForestClassifier()
            
            model_evaluation(X_train,X_test,y_train,y_test,model)
            
            logging.info("model training successfull")
            
            save_obj(file_path=self.model_training_config.model_training_file,
                     obj=model)
            logging.info(f"model save successfull {model}")
        
        except Exception as e:
            raise WineException(e, sys)