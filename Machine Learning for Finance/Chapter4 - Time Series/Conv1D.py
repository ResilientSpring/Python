from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv1D, MaxPool1D
from tensorflow.keras.losses import mean_absolute_percentage_error

number_of_features = 29
max_length = 100

model = Sequential([Conv1D(filters=16, kernel_size=5, input_shape=(100, 29), activation='relu'),
                    MaxPool1D(pool_size=5),
                    Conv1D(filters=16, kernel_size=5, activation='relu'),
                    MaxPool1D(5),
                    Flatten(),
                    Dense(units=1)])

model.compile(optimizer='adam', loss=mean_absolute_percentage_error)