import sys
from src.wine.logger import logging
from src.wine.exception import WineException
from src.wine.components.data_ingestion import DataIngestion
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
        data_tranformation.initiate_data_transfrom(train_data,
                                                   test_data)
        logging.info(f"**********************************************{"complate"}***************************************************\n")
    except Exception as e:
        raise WineException(e, sys)
    
    
    