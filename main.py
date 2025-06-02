import sys
from src.wine.logger import logging
from src.wine.exception import WineException
from src.wine.components.data_ingestion import DataIngestion
from src.wine.components.model_trainning import ModelTraining
from src.wine.components.data_transformation import DataTransfromation


data_ingestion_stage_name = "Data Ingestion Stage"

if __name__ == "__main__":
    try:
        logging.info(f"**************************************{data_ingestion_stage_name}************************************")
        data_ingestion = DataIngestion()
        train_data, test_data = data_ingestion.initiate_data_ingestion()
        logging.info(f"**********************************************{"complate"}***************************************************\n")
    except Exception as e:
        raise WineException(e, sys)
    
data_tranfrom_stage_name = "Data Transformation Stage"

if __name__ == "__main__":
    try:
        logging.info(f"**************************************{data_tranfrom_stage_name}************************************")
        data_tranformation = DataTransfromation()
        train_arr,test_arr,_ = data_tranformation.initiate_data_transfrom(train_data,
                                                                          test_data)
        logging.info(f"**********************************************{"complate"}***************************************************\n")
    except Exception as e:
        raise WineException(e, sys)
    
model_training_stage_name = "Model Training Stage"

if __name__ == "__main__":
    try:
        logging.info(f"**************************************{model_training_stage_name}************************************")
        model_training = ModelTraining()
        model_training.initiate_model_training(train_arr,
                                               test_arr)
        logging.info(f"**********************************************{"complate"}***************************************************")
    except Exception as e:
        raise WineException(e, sys)