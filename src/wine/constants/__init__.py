import os
from datetime import datetime

def get_current_time_stamp():
    return datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

CURRENT_TIME_STAMP = get_current_time_stamp()

ROOT_DIR_KEY = os.getcwd()
DATA_DIR = "data"
DATA_NAME = "wine_data.csv"

# root_dir/data_dir/data_name
# ent to end wine quality project/data/wine_data.csv


# artifacts folder name
ARTIFACTS_DIR = "artifacts"
# data ingestion folder name
DATA_INGESTION_DIR = "data_ingestion"
DATA_INGESTION_ROW_DATA_DIR = "row_data"
ROW_DATA_FILE_NAME = "wine.csv"
DATA_INGESTION_INGESTED_DATA_DIR = "ingested"
TRAIN_DATA_FILE_NAME = "train.csv"
TEST_DATA_FILE_NAME = "test.csv"