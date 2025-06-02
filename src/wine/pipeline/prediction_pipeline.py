import os
import sys
from dataclasses import dataclass
from src.wine.utils import load_obj
from src.wine.logger import logging
from src.wine.config.configuration import *
from src.wine.exception import WineException


@dataclass
class ModelPredictionPipeliene:
    def __init__(self):
        pass
    
    def predict(self, feature):
        try:
            logging.info('importing the configuration file')
            prossesor_path = PREPROSSESING_OBJ_FILE
            model_path = MODEL_TRAINING_OBJ_FILE
            
            logging.info('loaded model and transformaer successfull')
            prossesor = load_obj(file_path=prossesor_path)
            model = load_obj(file_path=model_path)
            
            logging.info('transforming the data')
            transformed_data = prossesor.transform(feature)
            
            pred = model.predict(transformed_data)
            
            return pred
            
        except Exception as e:
            raise WineException(e, sys)
        