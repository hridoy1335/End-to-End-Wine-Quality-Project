from src.wine.components.data_ingestion import DataIngestion
from src.wine.components.model_trainning import ModelTraining
from src.wine.components.data_transformation import DataTransfromation


class ModelTrainingPipeline:
    def __init__(self):
        self.c = 0
        print(f"---------------------{self.c}----------------------")
        
    def main(self):
        data_ingestion = DataIngestion()
        train_data, test_data = data_ingestion.initiate_data_ingestion()
        
        data_transfromation = DataTransfromation()
        train_arr, test_arr, _ = data_transfromation.initiate_data_transfrom(train_data,test_data)
        
        model_trainner = ModelTraining()
        model_trainner.initiate_model_trainning(train_arr, test_arr)