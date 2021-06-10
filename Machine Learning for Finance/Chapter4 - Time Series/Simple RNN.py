from tensorflow.keras.layers import SimpleRNN, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import mean_absolute_percentage_error

model = Sequential([SimpleRNN(units=16, input_shape=(max_len, number_of_features)),
                    Dense(units=1)])

model.compile(optimizer='adam', loss=mean_absolute_percentage_error)
