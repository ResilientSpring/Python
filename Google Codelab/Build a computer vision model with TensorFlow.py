import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import SparseCategoricalCrossentropy

# Train a neural network to recognize items of clothing from a common dataset called Fashion MNIST.
# It contains 70000 items of clothing in 10 different categories.
# Each item of clothing is in 28 x 28 grayscale image.

mnist = fashion_mnist

# Calling load_data() gives you two sets of two lists: training values and testing values, which
# represent graphics that show clothing items and their labels
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

# What do those values look like? Print a training image and a training label to see.
# You can experiment with different indices in the array.
plt.imshow(training_images[0])
plt.savefig("Build a computer vision model with tf.jpg")
plt.show()

# The print of the data for item 0 looks like this:
print(training_labels[0])
print(training_images[0])

# You will notice that all the values are integers between 0 and 255.
# When training a neural network, it's easier to treat all values as between 0 and 1,
# a process called normalization.
# Fortunately, Python provides an easy way to normalize a list like that without looping.
training_images = training_images / 255.0
test_images = test_images / 255.0

# Design the model
model = Sequential([Flatten(),
                    Dense(units=128, activation=tf.nn.relu),
                    Dense(units=10, activation=tf.nn.softmax)]) # The number of neurons in the last layer should match the number of classes you are classifiying for.


model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss=SparseCategoricalCrossentropy(),
              metrics=['accuracy'])


history = model.fit(x=training_images, y=training_labels, epochs=5)

# How would the model perform on data it hasn't seen? That's why you have the test set.
# You call model.evaluate and pass in the two sets, and it reports the loss for each.
accuracy = model.evaluate(x=test_images, y=test_labels)

print(accuracy)
