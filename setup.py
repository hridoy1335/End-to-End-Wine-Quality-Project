from typing import List
from setuptools import setup, find_packages


HYPEN_E_DOT = "-e ."
PROJECT_NAME = "wine"
PROJECT_VERSION = "0.0.1"
PROJECT_DESCRIPTION = "A Python package for wine"
PROJECT_AUTHOR = "HRIDOY KHAN"
PROJECT_EMAIL = "rkhridoyinfo@gmail.com"
PROJECT_URL = "https://github.com/hridoy1335/End-to-End-Wine-Quality-Project"
PROJECT_LICENSE = "GNU GENERAL PUBLIC LICENSE"
DOWNLOAD_URI = "https://github.com/hridoy1335/End-to-End-Wine-Quality-Project"

REQUIREMENTS_TXT = "requirements.txt"

def get_install_requires() -> List[str]:
    with open(REQUIREMENTS_TXT,'r') as file:
        require_list = [line.strip() for line in file.readlines()]
        
        if HYPEN_E_DOT in require_list:
            require_list.remove(HYPEN_E_DOT)
            
            return require_list

setup(
    name=PROJECT_NAME,
    version=PROJECT_VERSION,
    description=PROJECT_DESCRIPTION,
    download_url=DOWNLOAD_URI,
    license=PROJECT_LICENSE,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    url=PROJECT_URL,
    packages=find_packages(),
    install_requires = get_install_requires()
)