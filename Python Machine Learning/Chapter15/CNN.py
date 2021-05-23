from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dropout, Dense
from keras.optimizers import Adam
from keras.losses import SparseCategoricalCrossentropy
import tensorflow as tf

model = Sequential([Conv2D(filters=32, kernel_size=5, strides=1, padding='same',
                           data_format='channels_last', name='Conv_1', activation='relu'),
                    MaxPool2D(pool_size=2, name='pool_1'),
                    Conv2D(filters=64, kernel_size=5, strides=1, padding='same', name='conv_2',
                           activation='relu'),
                    MaxPool2D(pool_size=2, name='pool_2'),
                    Flatten(),
                    Dense(units=1024, name='fully_connected_1', activation='relu'),
                    Dropout(rate=0.5),
                    Dense(units=10, name='fully_connected_2', activation='softmax')])


tf.random.set_seed(1)

model.build(input_shape=(None, 28, 28, 1))

model.compile(optimizer=Adam(), loss=SparseCategoricalCrossentropy(), metrics=['accuracy'])

history = model.fit()