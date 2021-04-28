import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.utils import plot_model
from mlxtend.plotting import plot_decision_regions

x_train = np.array([ [1, 1], [1, 0], [0, 1], [0, 0] ])
print(x_train)

y_train = np.array([0, 1, 1, 0])
print(y_train)

x_valid = np.array([[1, 0], [1, 1], [0, 0], [0, 1]])
y_valid = np.array([1, 0, 0, 1])

# Construct a feedforward NN with three hidden layers.
model = keras.Sequential()
model.add(keras.layers.Dense(units=4, input_shape=(2, ), activation="relu"))
model.add(keras.layers.Dense(units=4, activation="relu"))
model.add(keras.layers.Dense(units=4, activation="relu"))
model.add(keras.layers.Dense(units=1, activation="sigmoid"))

print(model.summary())

plot_model(model=model, show_shapes=True, show_layer_names=True)


# Compile
model.compile(optimizer=keras.optimizers.SGD(), loss=keras.losses.BinaryCrossentropy(),
              metrics=[keras.metrics.BinaryAccuracy()])

# Train
hist = model.fit(x=x_train, y=y_train, validation_data=(x_valid, y_valid), epochs=200,
                 batch_size=2)

print(hist.history)

plot_decision_regions(X=x_valid, y=y_valid, clf=model)

plt.show()