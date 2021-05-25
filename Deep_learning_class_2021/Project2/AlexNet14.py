import tensorflow as tf
import keras
from keras.datasets import cifar10
import matplotlib.pyplot as plt
import os
import time
from sklearn.metrics import classification_report
import numpy as np
import cv2
from keras.utils import to_categorical
from keras.optimizers import Adam
from keras.losses import SparseCategoricalCrossentropy

(x_train, train_label), (x_test, test_label) = cifar10.load_data()

CLASS_NAMES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

train_data = []
for img in x_train:
    resized_img = cv2.resize(img, (227, 227))
    train_data.append(resized_img)

test_data = []
for img in x_test:
    resized_img = cv2.resize(img, (227, 227))
    test_data.append(resized_img)


train_data = np.array(train_data)
test_data = np.array(test_data)
train_data = train_data.reshape(train_data.shape[0], 227, 227, 3)
test_data = test_data.reshape(test_data.shape[0], 227, 227, 3)
train_label = to_categorical(train_label, num_classes=10)
test_label = to_categorical(test_label, num_classes=10)

print(train_data.shape)
print(test_data.shape)
print(train_label.shape)
print(test_label.shape)

model = keras.models.Sequential([
    keras.layers.Conv2D(filters=96, kernel_size=(11, 11), strides=(4, 4), activation='relu', data_format='channels_last', input_shape=(227, 227, 3)),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
    keras.layers.Conv2D(filters=256, kernel_size=(5, 5), strides=(1, 1), activation='relu', padding="same"),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
    keras.layers.Conv2D(filters=384, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding="same"),
    keras.layers.BatchNormalization(),
    keras.layers.Conv2D(filters=384, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding="same"),
    keras.layers.BatchNormalization(),
    keras.layers.Conv2D(filters=256, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding="same"),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(4096, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(4096, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(x=train_data, y=train_label, epochs=20)
