from tensorflow.keras.layers import LSTM, SimpleRNN, Dense
from tensorflow.keras.models import Sequential

number_of_features = 29
max_length = 100

model = Sequential([LSTM(units=16, input_shape=(max_length, number_of_features)),
                    Dense(units=1)])

