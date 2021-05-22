import pandas as pd
import feature_generation
import numpy as np
from sklearn.preprocessing import StandardScaler
from keras.layers import Dense, Flatten
from keras.models import Sequential
from keras.utils import plot_model

data_raw = pd.read_csv('19920103_20191231.csv', index_col='Date', thousands=',') # [1]
print(data_raw)
print(data_raw.info())

data = feature_generation.generate_features(df=data_raw)
print(data)
print(data.info())
data.to_csv("Data_with_generated_features.csv")

start_train = '1992-01-03'
end_train = '2018-12-27'
start_test = '2019-01-01'
end_test = '2019-12-31'

data = data.sort_index() # [2] Empty Dataframe after slice

data_train = data.loc[start_train:end_train, 'open':]
print(data_train)

X_train = data_train.drop('close', axis=1)
print(X_train.info())

y_train = data_train['close']
print(y_train)

data_raw = data_raw.sort_index()

data_test = data_raw.loc[start_test:end_test]
print(data_test)

X_test = data_test.drop('Close', axis=1)
print(X_test)

y_test = data_test['Close']
print(y_test)

scaler = StandardScaler()

X_scaled_train = scaler.fit_transform(X=X_train)
X_scaled_test = scaler.fit_transform(X=X_test)

model = Sequential([Flatten(input_shape=(31, )), Dense(units=32, activation='relu'),
                    Dense(units=1)])

print(model.summary())

# References:
# 1. https://stackoverflow.com/a/22137890/14900011
# 2. https://stackoverflow.com/a/52288027/14900011
