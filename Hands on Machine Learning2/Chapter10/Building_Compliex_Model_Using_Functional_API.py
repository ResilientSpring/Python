from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras import Sequential
import keras

housing = fetch_california_housing()

X_train_full, X_test, y_train_full, y_test = train_test_split(housing.data, housing.target)

X_train, X_validation, y_train, y_validation = train_test_split(X_train_full, y_train_full)

scaler = StandardScaler()

X_train_std = scaler.fit_transform(X_train)
X_validation_std = scaler.fit_transform(X=X_validation)
X_test_std = scaler.fit_transform(X=X_test)

print(X_train_std.shape[1:])

input_ = keras.layers.Input(shape=X_train_std.shape[1:])
hidden1 = keras.layers.Dense(units=30, activation="relu")(input_)
hidden2 = keras.layers.Dense(units=30, activation="relu")(hidden1)
concat = keras.layers.Concatenate()([input_, hidden2])
output = keras.layers.Dense(units=1)(concat)

model = keras.Model(inputs=[input_], output=[output])
