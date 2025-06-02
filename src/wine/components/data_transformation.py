import os
import sys
import numpy as np
import pandas as pd
from src.wine.constants import *
from dataclasses import dataclass
from src.wine.utils import save_obj
from src.wine.logger import logging
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.wine.config.configuration import *
from src.wine.exception import WineException
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


@dataclass
class DataTransformationConfig:
    preprossesing_obj_file:str = PREPROSSESING_OBJ_FILE
    transfrom_train_path: str = TRANSFROM_TRAIN_FILE_PATH
    transform_test_path: str = TRANSFROM_TEST_FILE_PATH
    
class DataTransfromation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    def get_data_tranformation_obj(self):
        try:
            logging.info("data transformation object creation started.")
            numeric_features = ['fixed acidity',
                                'volatile acidity',
                                'citric acid',
                                'residual sugar',
                                'chlorides',
                                'free sulfur dioxide',
                                'total sulfur dioxide',
                                'density',
                                'pH',
                                'sulphates',
                                'alcohol']
            
            num_pipe = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])
            
            preprossesor = ColumnTransformer([
                ('num_columns',num_pipe,numeric_features)
            ],remainder='passthrough')
            
            logging.info("Pipeline steps complate")
            return preprossesor
            
        except Exception as e:
            raise WineException(e,sys)
        
        
    def initiate_data_transfrom(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info('train and test data loaded')
            
            preprocessing_obj = self.get_data_tranformation_obj()
            logging.info('preprocessing object loaded successfull.')
            
            terget_columns = ['quality']
            
            X_train = train_df.drop(columns=terget_columns,axis=1)
            y_train = train_df[terget_columns]
            
            X_test = test_df.drop(columns=terget_columns,axis=1)
            y_test = test_df[terget_columns]
            
            logging.info('train and test data split to X_train,X_test,y_train,y_test')
            
            X_train = preprocessing_obj.fit_transform(X_train)
            X_test = preprocessing_obj.transform(X_test)
            
            logging.info('X_train and X_test data transformed')
            
            train_array = np.c_[X_train, np.array(y_train)]
            test_array = np.c_[X_test, np.array(y_test)]
            
            train_data = pd.DataFrame(train_array)
            test_data = pd.DataFrame(test_array)
            
            logging.info('train_array and test_array concatinate successfull')
            
            os.makedirs(os.path.dirname(self.data_transformation_config.transfrom_train_path),exist_ok=True)
            train_data.to_csv(self.data_transformation_config.transfrom_train_path, index=False)
            logging.info(f'train_data saved to csv from : {self.data_transformation_config.transfrom_train_path}')
            
            os.makedirs(os.path.dirname(self.data_transformation_config.transform_test_path),exist_ok=True)
            test_data.to_csv(self.data_transformation_config.transform_test_path, index=False)
            logging.info(f'test_data saved to csv from : {self.data_transformation_config.transform_test_path}')

            save_obj(file_path=self.data_transformation_config.preprossesing_obj_file,
                     obj=preprocessing_obj)
            logging.info(f'preprocessing object saved to file from : {self.data_transformation_config.preprossesing_obj_file}')
            
            return(
                train_array,
                test_array,
                self.data_transformation_config.preprossesing_obj_file
            )
        except Exception as e:
            raise WineException(e,sys)