import tensorflow as tf
import keras
from keras.datasets import cifar10
import matplotlib.pyplot as plt
import os
import time

(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

# References:
# 1. https://megalodon.jp/2021-0523-1837-57/https://towardsdatascience.com:443/implementing-alexnet-cnn-architecture-using-tensorflow-2-0-and-keras-2113e090ad98
# 2. https://archive.ph/P1DiU