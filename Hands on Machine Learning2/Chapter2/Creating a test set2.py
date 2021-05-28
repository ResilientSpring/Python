import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

housing = pd.read_csv(filepath_or_buffer=url, header=0)

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

print(train_set)

print(test_set)
