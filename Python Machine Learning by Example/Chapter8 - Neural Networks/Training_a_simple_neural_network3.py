import pandas as pd
import feature_generation
import numpy as np
from sklearn.preprocessing import StandardScaler
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import plot_model

data_raw = pd.read_csv('19920103_20191231.csv', index_col='Date', engine='python',
                       infer_datetime_format=True, thousands=',') # [1]
print(data_raw)
print(data_raw.info())

data = feature_generation.generate_features(df=data_raw)

start_train = '1992-01-03'
end_train = '2018-12-29'
start_test = '2019-01-01'
end_test = '2019-12-31'

data_train = data.loc[start_train:end_train]
print(data_train)

X_train = data_train.drop('close', axis=1).to_numpy()

y_train = data_train['close'].to_numpy()

data_test = data.loc[start_test:end_test]
print(data_test)

X_test = data_test.drop('close', axis=1).to_numpy()

y_test = data_test['close'].to_numpy()

scaler = StandardScaler()
X_scaled_train = scaler.fit_transform(X=X_train)
x_scaled_test = scaler.fit_transform(X=X_test)

# The network we begin with has one hidden layer with 32 nodes followed by a ReLU function.
model = Sequential([Dense(units=32, activation='relu'),
                    Dense(units=1)])

print(model.summary())

plot_model(model=model, show_shapes=True, show_layer_names=True)

# References:
# 1. https://stackoverflow.com/a/22137890/14900011
