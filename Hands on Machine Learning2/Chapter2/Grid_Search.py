import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

housing = pd.read_csv(filepath_or_buffer=url, header=0)

print(housing)
print(housing.info())
print(housing.describe())

housing.hist(bins=50, figsize=(20, 15))
plt.savefig('histogram for numeric attribute.jpg')
plt.show()
