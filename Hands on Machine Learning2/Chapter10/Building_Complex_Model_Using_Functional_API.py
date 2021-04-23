from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras import Sequential
import keras
from sklearn import metrics
import numpy as np

housing = fetch_california_housing()

X_train_full, X_test, y_train_full, y_test = train_test_split(housing.data, housing.target)

X_train, X_validation, y_train, y_validation = train_test_split(X_train_full, y_train_full)

scaler = StandardScaler()

# Scaling the training set
X_train_std = scaler.fit_transform(X_train)

# Scaling the validation set
X_validation_std = scaler.fit_transform(X=X_validation)

# Scaling the test set.
X_test_std = scaler.fit_transform(X=X_test)

print(X_train_std.shape[1:])

# First, we need to create an input object. (The name input_ is used to avoid overshadowing
# Python's built-in input() function.)
input_ = keras.layers.Input(shape=X_train_std.shape[1:])

# Secondly, we create a Dense layer with 30 neurons, using the ReLU activation function.
# So long as it is created, notice that we call it like a function, passing it the input.
hidden1 = keras.layers.Dense(units=30, activation="relu")(input_)

# Create the second hidden layer to be fed with the output of the first hidden layer.
hidden2 = keras.layers.Dense(units=30, activation="relu")(hidden1)

# Then we create a Concatenate layer in order to concatenate the input and the output of
# the second hidden layer.
concat = keras.layers.Concatenate()([input_, hidden2])

# Then we create the output layer to be fed with the result of the concatenation.
output = keras.layers.Dense(units=1)(concat)

# Lastly, we create a Keras Model, and specify which inputs and outputs to use.
model = keras.models.Model(inputs=[input_], outputs=[output])

# Once you have built the Keras model, everything is exactly like earlier: compile the model,
# train it, evaluate it, and use it to make predictions.

## Compile the model
model.compile(loss="mean_squared_error", optimizer=keras.optimizers.SGD(lr=1e-3))

## Train it
model.fit(x=X_train_std, y=y_train, epochs=20, validation_split=0.2)

y_prediction = model.predict(x=X_test_std)

## Evaluate it.
print("Mean absolute error: ", metrics.mean_absolute_error(y_true=y_test, y_pred=y_prediction))
print("Mean squared error: ", metrics.mean_squared_error(y_true=y_test, y_pred=y_prediction))
print("Root mean squared error: ", np.sqrt(metrics.mean_squared_error(y_true=y_test,
                                                                      y_pred=y_prediction)))

