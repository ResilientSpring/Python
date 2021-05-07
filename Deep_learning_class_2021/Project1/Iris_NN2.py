import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from keras.utils import plot_model
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions

iris = load_iris()

iris_data = iris.data
print(iris_data)

iris_label = iris.target
print(iris_label)

X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label, test_size=0.33,
                                                    random_state=42)

print(X_train)
print(X_test)
print(y_train)
print(y_test)

# Input's shape
print(X_train.shape)

model = Sequential()

# Feed input's shape to the model.
model.add(keras.Input(shape=(4, )))
model.add(Dense(units=128, activation="relu"))
model.add(Dense(units=64, activation="relu"))
model.add(Dense(units=3, activation="softmax"))

print(model.summary())

plot_model(model=model, show_shapes=True, show_layer_names=True)

# Compile
model.compile(optimizer=keras.optimizers.SGD(), loss=keras.losses.BinaryCrossentropy(),
              metrics=[keras.metrics.BinaryAccuracy()])

# Train
history = model.fit(x=X_train, y=y_train, epochs=200, batch_size=10,
                    validation_data=(X_test, y_test)) #[1]

# plot
plt.figure()
plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"])
plt.title("model loss")
plt.ylabel("loss")
plt.xlabel("epoch")
plt.show()

# References:
# 1. https://stats.stackexchange.com/a/153535/318962