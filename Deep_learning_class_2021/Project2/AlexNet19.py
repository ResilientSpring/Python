import tensorflow as tf
import keras
from keras.datasets import cifar10
import matplotlib.pyplot as plt
import os
import time
from sklearn.metrics import classification_report
import numpy as np
import cv2
from tensorflow.keras.utils import to_categorical
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


train_data = np.array(train_data, dtype=np.uint8)
test_data = np.array(test_data, dtype=np.uint8)

print(type(train_data))

