from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = fetch_california_housing(as_frame=True)

print(dataset)

(X_data, y_data) = fetch_california_housing(return_X_y=True)

print(X_data)

print(y_data)

url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

dataset2 = pd.read_csv(filepath_or_buffer=url, header=0)

print(dataset2)

print(dataset2["ocean_proximity"].value_counts())

print(dataset2.info())

print(dataset2.head())

print(dataset2.describe())

dataset2.hist(bins=50, figsize=(20, 15))

plt.savefig('California_housing.jpg')

plt.show()
