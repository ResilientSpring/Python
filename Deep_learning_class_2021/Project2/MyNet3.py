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
from keras.losses import sparse_categorical_crossentropy

(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship',
               'truck']

train_images_ = train_images / 255.0
test_images_ = test_images / 255.0

x_train_ = train_images_.reshape((train_images.shape[0], 227, 227, 1))
x_test_ = test_images_.reshape((test_images.shape[0], 227, 227, 1))

model = keras.models.Sequential([
    keras.layers.Conv2D(filters=96, kernel_size=(11, 11), strides=(4, 4), activation='relu', input_shape=(227, 227, 3)),
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

model.compile(optimizer='adam', loss=sparse_categorical_crossentropy, metrics=['accuracy'])

model.fit(x=x_train_, y=train_labels, epochs=4, validation_split=0.3, shuffle=True)

model.evaluate(x=x_test_, y=test_labels)

y_prediction = model.predict(x=x_test_)

y_prediction_bool = np.argmax(y_prediction, axis=1)

print(classification_report(y_true=test_labels, y_pred=y_prediction_bool, target_names=CLASS_NAMES))
