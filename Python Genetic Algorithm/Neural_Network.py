from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([Dense(units=2, activation='sigmoid', use_bias=True, bias_initializer='ones',
                          input_shape=[2, ]),
                    Dense(units=1, activation='sigmoid', use_bias=True, bias_initializer='ones')])


