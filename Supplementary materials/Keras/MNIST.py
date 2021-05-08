import numpy as np
import pandas as pd
from keras.utils import np_utils
from keras.datasets import mnist
import matplotlib.pyplot as plt

np.random.seed(10)

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print('train data=', len(x_train))
print('test data=', len(x_test))

print('x_train_image: ', x_train.shape)
print('y_train_label: ', y_train.shape)

def plot_image(image):
    fig = plt.gcf()
    fig.set_size_inches(2, 2)
    plt.imshow(X=image, cmap='binary')
    plt.show()


plot_image(x_train[1])
