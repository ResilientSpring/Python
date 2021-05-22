import pandas as pd
import feature_generation
import numpy as np
from sklearn.preprocessing import StandardScaler
from keras.layers import Dense, Flatten
from keras.models import Sequential
from keras.utils import plot_model
from keras.optimizers import Adam
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import tensorflow as tf
from tensorboard.plugins.hparams import api as hp

data_raw = pd.read_csv('19920103_20191231.csv', index_col='Date', thousands=',') # [1]
print(data_raw)
print(data_raw.info())

data = feature_generation.generate_features(df=data_raw)
print(data)
print(data.info())
data.to_csv("Data_with_generated_features_.csv")

start_train = '1992-01-03'
end_train = '2017-12-30'
start_test = '2018-01-03'
end_test = '2018-12-27'

data = data.sort_index() # [2] Empty Dataframe after slice

data_train = data.loc[start_train:end_train, 'open':]
print(data_train)

X_train = data_train.drop('close', axis=1)
print(X_train.info())

y_train = data_train['close']
print(y_train)

data_test = data.loc[start_test:end_test]
print(data_test)

X_test = data_test.drop('close', axis=1)
print(X_test)

y_test = data_test['close']
print(y_test)

scaler = StandardScaler()

X_scaled_train = scaler.fit_transform(X=X_train)
X_scaled_test = scaler.fit_transform(X=X_test)

tf.random.set_seed(42)

model = Sequential([Flatten(input_shape=(31, )), Dense(units=32, activation='relu'),
                    Dense(units=1)])

print(model.summary())

model.compile(loss='mean_squared_error', optimizer=Adam(0.1))

model.fit(x=X_scaled_train, y=y_train, epochs=100, verbose=True)

y_prediction = model.predict(x=X_scaled_test)

y_prediction_bool = np.argmax(y_prediction, axis=1)

y_prediction_bool2 = model.predict(x=X_scaled_test)[:, 0]

print(y_prediction_bool == y_prediction_bool2)

print(f'Mean Squared Error: {mean_squared_error(y_true=y_test, y_pred=y_prediction_bool):.3f}')
print(f'Mean Absolute Error: {mean_absolute_error(y_true=y_test, y_pred=y_prediction_bool):.3f}')
print(f'R^2: {r2_score(y_test, y_prediction_bool):.3f}')

print(f'Mean Squared Error: {mean_squared_error(y_true=y_test, y_pred=y_prediction_bool2):.3f}')
print(f'Mean Absolute Error: {mean_absolute_error(y_true=y_test, y_pred=y_prediction_bool2):.3f}')
print(f'R^2: {r2_score(y_test, y_prediction_bool2):.3f}')

HP_HIDDEN = hp.HParam(name='hidden_size', domain=hp.Discrete([64, 32, 16]))
HP_EPOCHS = hp.HParam(name='epochs', domain=hp.Discrete([300, 1000]))
HP_LEARNING_RATE = hp.HParam(name='learning_rate', domain=hp.RealInterval(0.01, 0.4))

def train_test_model(hparams, logdir):
    test_model = Sequential([Dense(units=hparams[HP_HIDDEN], activation='relu'),
                             Dense(units=1)])

    test_model.compile(loss='mean_squared_error', optimizer=Adam(hparams[HP_LEARNING_RATE]), metrics=['mean_squared_error'])
    test_model.fit(X_scaled_train, y_train)

# References:
# 1. https://stackoverflow.com/a/22137890/14900011
# 2. https://stackoverflow.com/a/52288027/14900011
