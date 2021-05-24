import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Input, Conv2D, Dense, Flatten, Dropout, MaxPool2D
from keras.models import Model
import keras

mnist_data = keras.datasets.fashion_mnist

# dividing data into training and test sets
(training_images, training_labels), (test_images, test_labels) = mnist_data.load_data()

# The images in our dataset are greyscale images, where each pixel value lies between 0 and 255.
# The following script normalize pixel values between 0 and 1.
training_images, test_images = training_images / 255.0, test_images / 255.0

print(training_images.shape)

# plotting image number 9 from test set
plt.figure()

plt.imshow(test_images[9])
plt.colorbar()
plt.grid(False)

plt.savefig('Fashion_MNIST.jpg')

plt.show()
