from tensorflow.core.protobuf import config_pb2
from tensorflow.python.client.session import InteractiveSession

config = config_pb2.ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

import pandas as pd
import Time_Series_Generator
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, LSTM, TimeDistributed, Dense

number_of_steps = 50

series = Time_Series_Generator.generate_time_series(batch_size=10000,
                                                    number_of_steps=number_of_steps + 10)

print(series)
print(series.shape)

X_train, y_train = series[:7000, :number_of_steps], series[:7000, -10, 0]

print(X_train.shape)

X_valid, Y_valid = series[7000:9000, :number_of_steps], series[7000:9000, -10:, 0]
X_test, Y_test = series[9000:, :number_of_steps], series[9000:, -10:, 0]

model = Sequential([Conv1D(filters=20, kernel_size=4, strides=2, padding='valid',
                           input_shape=[None, 1]),
                    LSTM(units=20, return_sequences=True),
                    LSTM(units=20, return_sequences=True),
                    TimeDistributed(Dense(units=10))])

model.compile(loss='mse', optimizer='adam')

history = model.fit(x=X_train, y=y_train, epochs=20, validation_data=(X_valid, Y_valid))

plt.figure()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['loss, val_loss'])
plt.title('Conv1D_with_LSTM5.jpg')
plt.show()

# Reference: https://stackoverflow.com/questions/63315046/function-call-stack-train-function
