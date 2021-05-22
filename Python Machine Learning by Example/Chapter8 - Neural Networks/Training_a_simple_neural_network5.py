import pandas as pd
import feature_generation
import numpy as np
from sklearn.preprocessing import StandardScaler
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import plot_model

data_raw = pd.read_csv('19920103_20191231.csv', index_col='Date', thousands=',') # [1]
print(data_raw)
print(data_raw.info())

data = feature_generation.generate_features(df=data_raw)
print(data)
print(data.info())

start_train = '1992-01-03'
end_train = '2018-12-27'
start_test = '2019-01-01'
end_test = '2019-12-31'

data = data.sort_index() # [2] Empty Dataframe after slice

data_train = data.loc[start_train:end_train, 'open':]
print(data_train)




# References:
# 1. https://stackoverflow.com/a/22137890/14900011
# 2. https://stackoverflow.com/a/52288027/14900011
