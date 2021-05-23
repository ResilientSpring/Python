from keras.datasets import fashion_mnist
import matplotlib.pyplot as plt
import tensorflow as tf
from keras import datasets, layers, models, losses
from sklearn.metrics import classification_report
import numpy as np

fashion_mnist = fashion_mnist

(X_train_full, y_train_full), (X_test_, y_test) = fashion_mnist.load_data()

# Split the full training set into a validation set and a (smaller) training set.
# We also scale the pixel intensities down to the 0-1 range and convert them to floats,
# by dividing by 255.[1]
X_valid, X_train = X_train_full[:5000] / 255.0, X_train_full[5000:] / 255.0
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]
X_test_ = X_test_ / 255.0

# Print a few samples from these four arrays, for example, the training labels as follows:
print(y_train_full)

# The label arrays do not include class names. Hence, we define them as follows and will
# use them for plotting later on:
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt',
               'Sneaker', 'Bag', 'Ankle boot']

# Take a look at the format of the image
print(X_train_full.shape)

# Similarly for the 10000 testing samples, we check the format as follows:
print(X_test_.shape)

# Let's now inspect a random training sample
plt.figure()
plt.imshow(X_train_full[42])
plt.colorbar()
plt.grid(False)
plt.title(class_names[y_train_full[42]])

plt.show()

# test_images = X_test_ / 255.0

# Now we display the first 16  training samples after the pre-processing
for i in range(16):
    plt.subplot(4, 4, i + 1) # Do not mistake subplot as subplots [1]
    plt.subplots_adjust(hspace=.3)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)

    plt.imshow(X_train_full[i], cmap=plt.cm.binary)

    plt.title(class_names[y_train_full[i]])


plt.show()

# As the convolutional layer in Keras only takes in individual samples in three dimensions,
# we need to first reshape the data into four dimensions:
X_train = X_train.reshape((X_train.shape[0], 28, 28, 1))

X_test = X_test_.reshape((X_test_.shape[0], 28, 28, 1))

print(X_train.shape)

# Before we develop the CNN model, let's specify the random speed in TensorFlow for reproducibility
tf.random.set_seed(42)

model = models.Sequential()

# For the convolutional extractor, we are going to use three convolutional layers.

## We start with the first convolutional layer with 32 small-sized 3 * 3 filters.
model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(units=64, activation='relu'))
model.add(layers.Dense(units=10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss=losses.sparse_categorical_crossentropy, metrics=['accuracy'])

print(model.summary())

# Fitting/training the CNN model we just built.
model.fit(x=X_train, y=y_train, epochs=10, validation_data=(X_valid, y_valid))

# If you want to double check the performance on the test set, you can do the following:
test_loss, test_accuracy = model.evaluate(x=X_test, y=y_test, verbose=2)

print('Accuracy on test set: ', test_accuracy)

y_prediction = model.predict(x=X_test)

y_prediction_bool = np.argmax(y_prediction, axis=1)

print(classification_report(y_true=y_test, y_pred=y_prediction_bool, target_names=class_names))

# References:
# 1. https://github.com/ageron/handson-ml2/blob/master/10_neural_nets_with_keras.ipynb
