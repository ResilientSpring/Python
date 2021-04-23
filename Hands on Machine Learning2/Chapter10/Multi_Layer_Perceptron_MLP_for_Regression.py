from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras import Sequential
import keras
import pandas as pd
import matplotlib.pyplot as plt

housing = fetch_california_housing()

X_train_full, X_test, y_train_full, y_test = train_test_split(housing.data, housing.target,
                                                              random_state=42)

X_train, X_validation, y_train, y_validation = train_test_split(X_train_full, y_train_full,
                                                                random_state=42)

scaler = StandardScaler()

X_train_std = scaler.fit_transform(X_train)
X_validation_std = scaler.fit_transform(X=X_validation)
X_test_std = scaler.fit_transform(X=X_test)

print(X_train_std.shape[1:])

model = Sequential()

model.add(keras.layers.Dense(units=30, activation="relu", input_shape=X_train_std.shape[1:]))

# The output layer has only a single neuron since we only want to predict a single value.
model.add(keras.layers.Dense(units=1))

model.compile(loss="mean_squared_error", optimizer=keras.optimizers.SGD(lr=1e-3))

history = model.fit(x=X_train_std, y=y_train, epochs=20,
                    validation_data=(X_validation_std, y_validation))

# Pretend these are new instances
X_new = X_test[:3]

y_prediction = model.predict(x=X_new)

print(y_prediction)

# Plot
plt.plot(pd.DataFrame(history.history))
plt.grid(True)
plt.gca().set_ylim(0, 1)

plt.savefig("Multi-layer_perceptron_using_stochastic_gradient_descent.jpg")

plt.show()