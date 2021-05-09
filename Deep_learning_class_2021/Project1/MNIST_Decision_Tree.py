import numpy as np
import pandas as pd
from keras.utils import np_utils
from keras.datasets import mnist
import matplotlib.pyplot as plt

np.random.seed(10)

(X_train, y_train), (X_test, y_test) = mnist.load_data()

print('train data=', len(X_train))
print('test data=', len(X_test))

print('X_train_image: ', X_train.shape)
print('y_train_label: ', y_train.shape)

def plot_image(image):
    fig = plt.gcf()
    fig.set_size_inches(2, 2)
    plt.imshow(X=image, cmap='binary')
    plt.show()


plot_image(X_train[0])
print(y_train[0])

# Pre-processing
