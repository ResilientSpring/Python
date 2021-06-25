from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, InputLayer
import pygad.kerasga
import numpy as np
from tensorflow.keras.losses import mean_squared_error, MeanAbsoluteError

model = Sequential([InputLayer(input_shape=[2, ]),
                    Dense(units=2, activation='sigmoid', use_bias=True, bias_initializer='ones'),
                    Dense(units=1, activation='sigmoid', use_bias=True, bias_initializer='ones')])

keras_genetic_algorithm = pygad.kerasga.KerasGA(model=model, num_solutions=9)

training_data = np.array([[1, 1],
                          [1, 0],
                          [0, 1],
                          [0, 0]])

labels = np.array([[0],
                   [1],
                   [1],
                   [0]])

history =

mean_absolute_error = MeanAbsoluteError()
loss = mean_absolute_error(y_true=labels, y_pred=)
