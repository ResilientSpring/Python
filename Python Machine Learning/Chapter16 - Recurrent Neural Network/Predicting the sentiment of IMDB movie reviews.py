import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import pandas as pd

dataframe = pd.read_csv('movie_data.csv', encoding = 'utf-8')
print(dataframe)

target = dataframe.pop('sentiment')
print(target)

# DataFrame.pop(item)
#   Return item and drop from frame. [1]

print(dataframe)  # Column ['sentiment'] is no longer present.

target2 = dataframe.filter(['sentiment'], axis=1)
print(target2)

target3 = dataframe['sentiment']
print(target3)

# Reference:
# 1. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pop.html
