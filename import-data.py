# Imports housing data from ageron's github
import os
import tarfile
import urllib
import pandas as pd

# Define URL and paths to download and store datasets
ROOT_URL = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
DATASET_PATH = 'datasets/housing'
DATASET_URL = ROOT_URL + DATASET_PATH + '/housing.tgz'

# Creates local dataset folder then downloads housing dataset
def fetch_housing_data(housing_url=DATASET_URL, housing_path=DATASET_PATH):
	if not os.path.isdir(housing_path):
		os.makedirs(housing_path)
	tgz_path = os.path.join(housing_path, "housing.tgz")
	urllib.request.urlretrieve(housing_url, tgz_path)
	housing_tgz = tarfile.open(tgz_path)
	housing_tgz.extractall(path=housing_path)
	housing_tgz.close()

# Load data via pandas
def load_housing_data(housing_path=DATASET_PATH):
	csv_path = os.path.join(housing_path, 'housing.csv')
	return pd.read_csv(csv_path)

fetch_housing_data()
housing = load_housing_data()
print(housing.head())
