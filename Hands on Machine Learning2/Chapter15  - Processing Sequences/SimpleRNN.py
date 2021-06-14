import Time_Series_Generator as time
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, SimpleRNN
import matplotlib.pyplot as plt
from tensorflow.keras.losses import mean_squared_error
import numpy as np
import tensorflow as tf
import matplotlib as mpl

number_of_steps = 50
series = time.generate_time_series(batch_size=10000, number_of_steps=number_of_steps + 1)

X_train, y_train = series[:7000, :number_of_steps], series[:7000, -1]
X_valid, y_valid = series[7000:9000, :number_of_steps], series[7000:9000, -1]
X_test, y_test = series[9000:, :number_of_steps], series[9000:, -1]

def plot_series(series, y=None, y_pred=None, x_label="$t$", y_label="$x(t)$"):
    plt.plot(series, ".-")
    if y is not None:
        plt.plot(number_of_steps, y, "bx", markersize=10)
    if y_pred is not None:
        plt.plot(number_of_steps, y_pred, "ro")
    plt.grid(True)
    if x_label:
        plt.xlabel(x_label, fontsize=16)
    if y_label:
        plt.ylabel(y_label, fontsize=16, rotation=0)
    plt.hlines(0, 0, 100, linewidth=1)
    plt.axis([0, number_of_steps + 1, -1, 1])


fig, axes = plt.subplots(nrows=1, ncols=3, sharey=True, figsize=(12, 4))

for col in range(3):
    plt.sca(axes[col])
    plot_series(X_valid[col, :, 0], y_valid[col, 0],
                y_label=("$x(t)$" if col == 0 else None))

plt.savefig("time_series_plot.jpg")
plt.show()

y_prediction = X_valid[:, -1]
y_prediction_mean = np.mean(mean_squared_error(y_true=y_valid, y_pred=y_prediction))
print(y_prediction_mean)

plot_series(X_valid[0, :, 0], y_valid[0, 0], y_prediction[0, 0])
plt.show()


np.random.seed(42)
tf.random.set_seed(42)

model = Sequential([Flatten(input_shape=[50, 1]),
                    Dense(units=1)])

model.compile(loss="mse", optimizer="adam")
history = model.fit(x=X_train, y=y_train, epochs=20, validation_data=(X_valid, y_valid))
model.evaluate(X_valid, y_valid)

def plot_learning_curves(loss, val_loss):
    plt.plot(np.arange(len(loss)) + 0.5, loss, "b.-", label="Training loss")
    plt.plot(np.arange(len(val_loss)) + 1, val_loss, "r.-", label="Validation loss")
    plt.gca().xaxis.set_major_locator(mpl.ticker.MaxNLocator(integer=True))
    plt.axis([1, 20, 0, 0.05])
    plt.legend(fontsize=14)
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.grid(True)

plot_learning_curves(history.history["loss"], history.history["val_loss"])
plt.show()


model2 = Sequential([SimpleRNN(units=1, input_shape=[None, 1])])