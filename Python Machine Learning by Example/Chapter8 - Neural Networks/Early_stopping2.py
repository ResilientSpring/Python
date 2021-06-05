import pandas as pd
import feature_generation
import numpy as np
from sklearn.preprocessing import StandardScaler
from keras.layers import Dense, Flatten
from keras.models import Sequential
from tensorflow.keras.utils import plot_model
from keras.optimizers import Adam
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping

data_raw = pd.read_csv('19920103_20191231.csv', index_col='Date')

data = feature_generation.generate_features(df=data_raw)

start_train = '1992-01-03'
end_train = '2018-12-27'
start_test = '2019-01-01'
end_test = '2019-12-31'

data_train = data.loc[start_train:end_train, 'open':]
print(data_train)

X_train = data_train.drop('close', axis=1)
print(X_train.info())

y_train = data_train['close']
print(y_train)

scaler = StandardScaler()

X_scaled_train = scaler.fit_transform(X=X_train)

tf.random.set_seed(42)

model = Sequential([Flatten(),
                    Dense(units=6, activation='relu'),
                    Dense(units=1)])

model.compile(loss='mean_squared_error', optimizer=Adam(0.1))

model.fit(x=X_scaled_train, y=y_train, epochs=100, verbose=True, validation_split=0.2,
          callbacks=[EarlyStopping(monitor='val_loss',
                                   min_delta=0,
                                   patience=200, # If the MSE doesn't decrease after 200 epochs of training on validation set, it stops the training process.
                                   verbose=0,
                                   mode='auto')])

