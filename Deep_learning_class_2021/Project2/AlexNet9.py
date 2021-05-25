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
