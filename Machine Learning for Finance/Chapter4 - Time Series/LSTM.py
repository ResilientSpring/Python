from tensorflow.keras.layers import LSTM
from tensorflow.keras.models import Sequential

number_of_features = 29
max_length = 100

model = Sequential([LSTM(units=16, input_shape=)])