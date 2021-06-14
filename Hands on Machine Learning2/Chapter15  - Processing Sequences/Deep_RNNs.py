from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN

model = Sequential([SimpleRNN(units=20, return_sequences=True, input_shape=[None, 1]),
                    SimpleRNN(units=20, return_sequences=True),
                    SimpleRNN(units=1)])


