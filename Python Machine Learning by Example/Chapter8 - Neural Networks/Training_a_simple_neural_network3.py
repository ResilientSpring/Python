import pandas as pd
import feature_generation
import numpy as np

data_raw = pd.read_csv('19920103_20191231.csv', index_col='Date', thousands=',') # [1]
print(data_raw)
print(data_raw.info())

data = feature_generation.generate_features(df=data_raw)

start_train = '3-Jan-92'
end_train = '29-Dec-18'
start_test = '1-Jan-1'
end_test = '31-Dec-19'

data_train = data.loc[start_train:end_train]
print(data_train)

X_train = data_train.drop('close', axis=1).to_numpy()

y_train = data_train['close'].to_numpy()


# References:
# 1. https://stackoverflow.com/a/22137890/14900011
