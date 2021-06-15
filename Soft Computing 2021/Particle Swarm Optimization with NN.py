from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([Dense(units=3, activation='sigmoid', use_bias=True)])