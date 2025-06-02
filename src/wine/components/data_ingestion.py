import os
import sys
import numpy as np
import pandas as pd
from src.wine.constants import *
from dataclasses import dataclass
from src.wine.logger import logging
from src.wine.config.configuration import *
from src.wine.exception import WineException
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    raw_data_path:str = ROW_FILE_PATH
    test_data_path:str = TEST_FILE_PATH
    train_data_path:str = TRAIN_FILE_PATH
    
class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        try:
            logging.info(f"data read and ingestion started -> {DATASET_PATH}")
            df = pd.read_csv(DATASET_PATH)
            logging.info("read the data successfully")
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)
            logging.info("data ingestion completed to raw data folder")
            
            logging.info("spliting the data from train and test file")
            train, test = train_test_split(df,test_size=0.2,random_state=42)
            
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            train.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            
            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path),exist_ok=True)
            test.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)
            
            logging.info(f"split the file is traing size = {train.shape[0]} and test size = {test.shape[0]}")
            logging.info("data ingestion is complate.")
            
            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path,
            )
            
        except Exception as e:
            raise WineException(e,sys) from e