from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

model = Sequential([Conv2D(filters=64, kernel_size=7, activation='relu', padding='same', input_shape=[28, 28, 1]),
                    ])