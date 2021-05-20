from keras.models import Sequential
from keras.layers import Flatten, Dense, Dropout

# The following code applies dropout regularization before every Dense layer,
# using dropout rate of 0.2

model = Sequential(layers=[Flatten(input_shape=[28, 28]),
                           Dropout(rate=0.2),
                           Dense(units=300, activation='relu', kernel_initializer='he_normal'),
                           Dropout(rate=0.2),
                           Dense(units=100, activation='relu', kernel_initializer='he_normal'),
                           Dropout(rate=0.2),
                           Dense(units=10, activation='softmax')])
