import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

iris = load_iris()
iris_data=iris.data
print(iris_data)
X_train, X_test, y_train, y_test = train_test_split(iris_data, iris.target, test_size=0.2);

# Lay the foundation of the model. / Get the model off the ground.
model = Sequential()

# Feed input's shape to the model.
model.add(keras.Input(shape=(4, 1)));

# Flatten() reshapes the input into one-dimension.
model.add(Flatten());

# Dense() means the fully-connected layers.
model.add(Dense(units=64, activation="relu", name="layer1"))

# Dropout means to drop out the specified percent of input data.
model.add(Dropout(0.2))

# Configure the second layer
model.add(Dense(units=128, activation="relu", name="layer2"))
model.add(Dropout(rate=0.2))

model.add(Dense(units=3, activation="softmax", name="layers3"));

# Printing out model information
print(model.summary());

# All set, let's compile the model! (initialization)
model.compile(optimizer='adam', loss="sparse_categorical_crossentropy", metrics=["accuracy"]);
# "sparse_categorical_crossentropy" differs from "categorical_crossentropy" in that
# it automatically attains one-hot encoding.

# Train the algorithm
history = model.fit(x=X_train, y=y_train,
    #                batch_size=5,
                    validation_split=0.1,
                    epochs=100);
## validation_split refers to spliting the dataset for validation.

plt.figure();
plt.plot(history.history["loss"]);
plt.plot(history.history["val_loss"]);
plt.ylabel("loss")
plt.xlabel("epoch")
plt.title("model loss")

plt.show();