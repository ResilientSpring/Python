import tensorflow as tf
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout
from keras.optimizers import Adam
from keras.losses import SparseCategoricalCrossentropy

(x_train, train_label), (x_test, test_label) = mnist.load_data()

model = Sequential(
    [Conv2D(filters=32, kernel_size=5, strides=1, padding='same', data_format='channels_last',
            name='Conv_1', activation='relu', input_shape=(None, 28, 28, 1)),
     MaxPool2D(pool_size=2, name='Pool_1'),
     Conv2D(filters=64, kernel_size=5, strides=1, padding='same', name='Conv_2', activation='relu'),
     MaxPool2D(pool_size=2, name='Pool_2'),
     Flatten(),
     Dense(units=1024, name='fully_connected_layer1', activation='relu'),
     Dropout(rate=0.5),
     Dense(units=10, name='fully_connected_layer2', activation='softmax')])

# model.build(input_shape=(None, 28, 28, 1))

model.compile(optimizer=Adam(), loss=SparseCategoricalCrossentropy(), metrics=['accuracy'])

history = model.fit(x=x_train, y=train_label)