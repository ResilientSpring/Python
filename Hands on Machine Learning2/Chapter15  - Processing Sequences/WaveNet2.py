import matplotlib.pyplot as plt
from tensorflow.keras.losses import mean_squared_error
import numpy as np
import tensorflow as tf
import matplotlib as mpl
import Time_Series_Generator as time
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, SimpleRNN, Conv1D, InputLayer

number_of_steps = 50
series = time.generate_time_series(batch_size=10000, number_of_steps=number_of_steps + 1)

X_train, y_train = series[:7000, :number_of_steps], series[:7000, -1]
X_valid, y_valid = series[7000:9000, :number_of_steps], series[7000:9000, -1]
X_test, y_test = series[9000:, :number_of_steps], series[9000:, -1]

np.random.seed(42)
tf.random.set_seed(42)

model = Sequential()
model.add(InputLayer(input_shape=[None, 1]))

for rate in (1, 2, 4, 8) * 2:
    model.add(Conv1D(filters=20, kernel_size=2, padding='causal', activation='relu',
                     dilation_rate=rate))

model.add(Conv1D(filters=10, kernel_size=1))

model.compile(optimizer='adam', loss='mse')

history = model.fit(x=X_train, y=y_train, epochs=20, validation_data=(X_valid, y_valid))
