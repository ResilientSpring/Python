from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([Dense(units=2, activation='sigmoid', use_bias=True),
                    Dense(units=1, use_bias=True, bias_initializer=1.0)])
