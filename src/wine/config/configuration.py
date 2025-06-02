import os
from src.wine.constants import *

ROOT_DIR = ROOT_DIR_KEY

# dataset path
DATASET_PATH = os.path.join(ROOT_DIR,DATA_DIR,DATA_NAME)
# ent to end wine quality project/data/wine_data.csv


# row data folder create and the data save
ROW_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACTS_DIR,CURRENT_TIME_STAMP,DATA_INGESTION_DIR,
                             DATA_INGESTION_ROW_DATA_DIR,ROW_DATA_FILE_NAME)

# train data folder create and the data save
TRAIN_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACTS_DIR,CURRENT_TIME_STAMP,DATA_INGESTION_DIR,
                               DATA_INGESTION_INGESTED_DATA_DIR,TRAIN_DATA_FILE_NAME)

# test data folder create and the data save
TEST_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACTS_DIR,CURRENT_TIME_STAMP,DATA_INGESTION_DIR,
                              DATA_INGESTION_INGESTED_DATA_DIR,TEST_DATA_FILE_NAME)