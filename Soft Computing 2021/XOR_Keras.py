import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import keras
from tensorflow.keras.utils import plot_model
from mlxtend.plotting import plot_decision_regions
import tensorflow

tf.random.set_seed(1)
np.random.seed(1)

# We generate a toy dataset of 200 training examples with 2 features (x0, x1) drawn from a
# uniform distribution between [-1, 1)
x = np.random.uniform(low=-1, high=1, size=(200, 2))
print(x)

# Assign the ground truth label
y = np.ones(len(x))
print(y)

## Applying the threshold rule:
y[x[:, 0] * x[:, 1] < 0] = 0

# Use half of the data (100 training examples) for training and the remaining half for
# validation
## feature set (0 - 99)
x_train = x[:100, :]
## label set (0- 99)
y_train = y[:100]

## the feature set for validation (100 - 199)
x_valid = x[100:, :]

## the label set for validation (100 - 199)
y_valid = y[100:]

fig = plt.figure(figsize=(6, 6))
plt.plot(x[y == 0, 0], x[y == 0, 1], 'o', alpha=0.75, markersize=10)
plt.plot(x[y == 1, 0], x[y == 1, 1], '<', alpha=0.75, markersize=10)
plt.xlabel(r'$x_1$', size=15)
plt.ylabel(r'$x_2$', size=15)
plt.show()

model = tensorflow.keras.Sequential()

model.add(tensorflow.keras.layers.Dense(units=1, input_shape=(2, ), activation="sigmoid"))

print(model.summary())

plot_model(model=model, show_shapes=True, show_layer_names=True)

# After defining the model, we will compile the model and train it for 200 epochs using a
# batch size of 2:
model.compile(optimizer=(tensorflow.keras.optimizers.SGD(),
                         loss=(tensorflow.keras.losses.BinaryCrossentropy(),
              metrics=[(tensorflow.keras.metrics.BinaryAccuracy()])

hist = model.fit(x=x_train, y=y_train, validation_data=(x_valid, y_valid), epochs=200,
                 batch_size=2, verbose=0)

history = hist.history
figure = plt.figure(figsize=(16, 4))
ax = figure.add_subplot(1, 3, 1)
plt.plot(history["loss"], lw=4)
plt.plot(history["val_loss"], lw=4)
plt.legend(["Train loss", "Validation loss"], fontsize=15)

ax.set_xlabel("Epochs", size=15)

ax = figure.add_subplot(1, 3, 2)

plt.plot(history["binary_accuracy"], lw=4)

plt.plot(history["val_binary_accuracy"], lw=4)

plt.legend(["Train Acc.", "Validation Acc."], fontsize=15)

ax = figure.add_subplot(1, 3, 3)

plot_decision_regions(X=x_valid, y=y_valid.astype(np.integer), clf=model)

ax.set_xlabel(r'$x_1$', size=15)

ax.xaxis.set_label_coords(1, -0.025)

ax.set_ylabel(r'$x_2$', size=15)

ax.yaxis.set_label_coords(-0.025, 1)

plt.show()
