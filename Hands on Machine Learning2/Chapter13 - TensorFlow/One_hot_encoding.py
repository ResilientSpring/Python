import pandas as pd

url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

dataset = pd.read_csv(filepath_or_buffer=url, header=0)

print(dataset.head())

print(dataset["ocean_proximity"].unique())

print(dataset["ocean_proximity"].value_counts())
