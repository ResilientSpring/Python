import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import pandas as pd

dataframe = pd.read_csv('movie_data.csv', encoding = 'utf-8')
print(dataframe)

target = dataframe.pop('sentiment')
print(target)

target2 = dataframe.filter(['sentiment'], axis=1)
print(target2)

target3 = dataframe['sentiment']
print(target3)
