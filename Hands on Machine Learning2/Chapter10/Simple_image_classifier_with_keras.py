import tensorflow as tf
import keras
import pandas as pd
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()

print(y_train_full)
print(y_test)

print(X_train_full.shape)
print(X_train_full.dtype)

# Create their validation sets and scale them down to 0-1 by dividing them by 255.0
X_valid, X_train = X_train_full[:5000] / 255.0, X_train_full[5000:]

y_valid, y_train = y_train_full[:5000], y_train_full[5000:]

# List the class names to know what we are dealing with:
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Scandal", "Shirt",
               "Sneaker", "Bag", "Angle boot"]

## The first image in the training set represents a coat:
print(class_names[y_train[0]])

# Creating the model using the Sequential API
model = keras.models.Sequential()

## We build the first layer and add it to the model.
## It's a Flatten layer. Alternatively, you could add a keras.layers.InputLayer
## as the first layer
model.add(keras.layers.Flatten(input_shape=[28, 28]))

## We add a Dense hidden layer with 300 neurons. It will use ReLU activation function.
model.add(keras.layers.Dense(units=300, activation="relu"))

## Then we add a second Dense hidden layer with 100 neurons, also using the ReLU activation function.
model.add(keras.layers.Dense(units=100, activation="relu"))

## Finally, we add a Dense output layer with 10 neurons, using the softmax activation function.
model.add(keras.layers.Dense(units=10, activation="softmax"))

# Display all the model's layers
model.summary()

# Get a model's list of layers
print(model.layers)

# Fetch a layer by its index
hidden1 = model.layers[1]
print(hidden1.name)

# Fetch a layer by name
print(model.get_layer(name="dense") is hidden1)

# All the parameters of a layer can be accessed using its get_weights() and set_weights()

## For a Dense layer, this includes both the connection weights and the bias terms.
weights, biases = hidden1.get_weights()

print(weights)
print(weights.shape)

print(biases)
print(biases.shape)

# After a model is created, you must call its compile() method to specify the loss function
# and the optimizer to use.
model.compile(optimizer="sgd", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# For training and evaluating the model, we simply need to call its fit() method:
history = model.fit(x=X_train, y=y_train, epochs=30, validation_data=(X_valid, y_valid))

## You can just set validation_split to the ratio of the training set that
## you want Keras to use for validation.  For example, validation_split-0.1 tells Keras
## to use the last 10% of the data (before shuffling) for validation.
history2 = model.fit(x=X_train, y=y_train, validation_split=0.1, epochs=30)

# Use the dictionary history.history returned by the fit(), to create a pandas DataFrame
pd.DataFrame(data=history.history).plot(figsize=(8, 5))

plt.grid(True)

# Set the vertical range to [0-1]
plt.gca().set_ylim(0, 1)

plt.show()