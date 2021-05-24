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

# Change the dimensions of our input images.
# CNN in Keras expects data to be in the format Width-Height-Channel.
# Our images contain width and height but no channels.
# Since the images are greyscale, we set the image channel to 1.
training_images = np.expand_dims(training_images, -1)
test_images = np.expand_dims(test_images, -1)

print(training_images.shape)

# The next step is to find the number of output classes.
# This number will be used to define the number of neurons in the output layer.
output_classes = len(set(training_labels))

print('Number of output classes is: ', output_classes)

# Let's print the shape of a single image in the training set
print(training_images[0].shape) # This shape will be used to train our convolutional neural network

input_layer = Input(shape=training_images[0].shape)

