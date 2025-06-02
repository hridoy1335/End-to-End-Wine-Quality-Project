import os
import sys
import numpy as np 
import pandas as pd
from dataclasses import dataclass
from src.wine.utils import load_obj
from src.wine.logger import logging
from src.wine.exception import WineException


PREDICTION_FOLDER = "batch_prediction"
PREDICTION_DIR = "prediction_csv"
PREDICTION_FILE = "output.csv"

ROOT_DIR = os.getcwd()

BATCH_PREDICTION = os.path.join(ROOT_DIR,PREDICTION_FOLDER,PREDICTION_DIR)


@dataclass
class BatchPredictionConfig:
    def __init__(self, input_file, trnsformaer_file, model_file):
        self.inpute_file_path = input_file
        self.transformer_file_path = trnsformaer_file
        self.model_file_path = model_file
        
        
    def start_batch_prediction(self):
        try:
            logging.info('batch prediction is started')
            preprossesor = load_obj(file_path=self.transformer_file_path)
            model = load_obj(file_path=self.model_file_path)
            logging.info('preprossesor and model file loaded succesfully.')
            
            df = pd.read_csv(self.inpute_file_path)
            logging.info('input file loaded succesfully.')
            df.to_csv("wine_quality_check_prediction.csv",index=False,header=True)
            logging.info('input file saved succesfully.')
            
            data = df.drop(columns=['quality'],axis=1)
            
            transfrom_data = preprossesor.transform(data)
            
            file_path = os.path.join(BATCH_PREDICTION,"prossesor.csv")
            
            predictions = model.predict(transfrom_data)
            
            pediction_data = pd.DataFrame(predictions,columns=['prediction'])
            
            os.makedirs(BATCH_PREDICTION,exist_ok=True)
            csv_path = os.path.join(BATCH_PREDICTION,PREDICTION_FILE)
            pediction_data.to_csv(csv_path,index=False,header=True)
            
            logging.info('batch prediction done')
        
        except Exception as e:
            raise WineException(e,sys)