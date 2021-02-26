## Downloads the dataset from raw.githubusercontent.com/ageron/handson-ml2/master/
## and places it in the data/raw/folder

import os, tarfile
import urllib.request as urllib
DOWNLOAD_PATH = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/"
DATASET_NAME = "housing.tgz"

SAVE_LOCATION = "../../data/raw/"

def fetch_housing_data(DOWNLOAD_PATH, DATASET_NAME, SAVE_LOCATION):
    download_location = DOWNLOAD_PATH + DATASET_NAME
    saved_file = SAVE_LOCATION + DATASET_NAME
    
    urllib.urlretrieve(download_location, saved_file)
    
    housing_tgz = tarfile.open(saved_file)
    housing_tgz.extractall(path="../../data/interim/")
    housing_tgz.close()
    
if __name__ == '__main__':
    fetch_housing_data(DOWNLOAD_PATH, DATASET_NAME, SAVE_LOCATION)
