import os
import logging
from pathlib import Path


project_name = "wine"
list_of_file = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainning.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/pipeline/__inti__.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/exception/__init__.py",
    f"config/config.yaml",
    f"params.yaml",
    f"schema.yaml",
    f"requirements.txt",
    f"app.py",
    f"main.py",
    f"Dockerfile",
    f"dvc.yaml",
    ".dockerignore"
]

for file in list_of_file:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
        
    else:
        logging.info(f"file path is already exsits{filename}")
        