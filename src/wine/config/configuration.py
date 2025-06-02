import os
from src.wine.constants import *

ROOT_DIR = ROOT_DIR_KEY

# dataset path
DATASET_PATH = os.path.join(ROOT_DIR,DATA_DIR,DATA_NAME)
# ent to end wine quality project/data/wine_data.csv

# ****************************************************** DATA INGESTION ****************************************************
# row data folder create and the data save
ROW_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACTS_DIR,CURRENT_TIME_STAMP,DATA_INGESTION_DIR,
                             DATA_INGESTION_ROW_DATA_DIR,ROW_DATA_FILE_NAME)

# train data folder create and the data save
TRAIN_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACTS_DIR,CURRENT_TIME_STAMP,DATA_INGESTION_DIR,
                               DATA_INGESTION_INGESTED_DATA_DIR,TRAIN_DATA_FILE_NAME)

# test data folder create and the data save
TEST_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACTS_DIR,CURRENT_TIME_STAMP,DATA_INGESTION_DIR,
                              DATA_INGESTION_INGESTED_DATA_DIR,TEST_DATA_FILE_NAME)



# ****************************************************** DATA TRANSFORMATION ****************************************************
# transformed data folder create and the data save
PREPROSSESING_OBJ_FILE = os.path.join(ROOT_DIR,ARTIFACTS_DIR,CURRENT_TIME_STAMP,DATA_TRANSFORMATION_DIR,
                                      DATA_TRANSFORMATION_PROCESSOR_DIR,DATA_TRANSFORMATION_PROCESSOR_OBJ)

# transform train data folder create and the data save
TRANSFROM_TRAIN_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACTS_DIR,CURRENT_TIME_STAMP,DATA_TRANSFORMATION_DIR,
                                         DATA_TRANSFORMATION_TRANSFOMATION_DIR,DATA_TRANSFORMATION_TRAIN_FILE_NAME)

# transform test data folder create and the data save
TRANSFROM_TEST_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACTS_DIR,CURRENT_TIME_STAMP,DATA_TRANSFORMATION_DIR,
                                        DATA_TRANSFORMATION_TRANSFOMATION_DIR,DATA_TRANSFORMATION_TEST_FILE_NAME)



# ****************************************************** MODEL TRAINING ****************************************************
# model training folder create and the data save
MODEL_TRAINING_OBJ_FILE = os.path.join(ROOT_DIR,ARTIFACTS_DIR,CURRENT_TIME_STAMP,MODEL_TRAINING_DIR,
                                       MODEL_TRAINING_FILE_NAME)