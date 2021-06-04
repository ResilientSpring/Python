import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.datasets import cifar10
import matplotlib.pyplot as plt
import os
import time
from sklearn.metrics import classification_report
import numpy as np
import cv2
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy, categorical_crossentropy
from tensorflow.keras.layers import Conv2D, BatchNormalization, MaxPool2D, Flatten, Dense, Dropout

(x_train, train_label), (x_test, test_label) = cifar10.load_data()

CLASS_NAMES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

train_data = []
for img in x_train:
    img = cv2.resize(img, (227, 227))
    img = img / 255.0
    train_data.append(img)

test_data = []
for img in x_test:
    img = cv2.resize(img, (227, 227))
    img = img / 255.0
    test_data.append(img)


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

model = Sequential([
    Conv2D(filters=96, kernel_size=(11, 11), strides=(4, 4), activation='relu', data_format='channels_last', input_shape=(227, 227, 3)),
    BatchNormalization(),
    MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
    Conv2D(filters=256, kernel_size=(5, 5), strides=(1, 1), activation='relu', padding="same"),
    BatchNormalization(),
    MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
    Conv2D(filters=384, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding="same"),
    BatchNormalization(),
    Conv2D(filters=384, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding="same"),
    BatchNormalization(),
    Conv2D(filters=256, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding="same"),
    BatchNormalization(),
    MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
    Flatten(),
    Dense(4096, activation='relu'),
    Dropout(0.5),
    Dense(4096, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

model.compile(optimizer=Adam(), loss=categorical_crossentropy, metrics=['accuracy'])

history = model.fit(x=train_data, y=train_label, epochs=20, batch_size=128)

model.evaluate(x=test_data, y=test_label)

y_prediction = model.predict(x=test_data)

y_prediction_bool = np.argmax(y_prediction, axis=1)

print(classification_report(y_true=test_label, y_pred=y_prediction_bool, target_names=CLASS_NAMES))
