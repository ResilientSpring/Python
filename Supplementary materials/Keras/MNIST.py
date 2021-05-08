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
print(y_train[1])

def plot_image_labels(images, labels, idx, num = 10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25: num = 25

    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap='binary')
        title = "label=" + str(labels[idx])
        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()


plot_image_labels(images=x_train, labels=y_train, idx=0, num=10)

plot_image_labels(images=x_test, labels=y_test, idx=0, num=10)

x_Train = x_train.reshape(60000, 28 * 28).astype('float32')
x_Test = x_test.reshape(10000, 28 * 28).astype('float32')

print('x_train:', x_Train.shape)
print('x_test:', x_Test.shape)

print(x_train[0])

# Scaling the data, which is also known as normalization
x_Train_normalization = x_Train / 255
x_Test_normalization = x_Test / 255

# Checking the image after normalization
print(x_Train_normalization[0])

print(y_train[:5])

y_Train_OneHot = np_utils.to_categorical(y=y_train)
y_Test_OneHot = np_utils.to_categorical(y=y_test)

print(y_Train_OneHot[:5])

# Reference:
# https://web.archive.org/web/20210508130921/https://waternotetw.blogspot.com/2018/03/keras-mnist.html
# https://archive.ph/u71f7

# Further reading:
# https://keras.io/api/datasets/mnist/