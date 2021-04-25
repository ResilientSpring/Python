import seaborn as sns
import pandas as pd
import numpy as np
from keras.layers import Dense, Dropout, Activation
from keras.models import Model, Sequential
from keras.optimizers import Adam
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.utils import plot_model
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/AbhiRoy96/Banknote-Authentication-UCI-Dataset/master/bank_notes.csv"

banknote_data = pd.read_csv(filepath_or_buffer=url)
print(banknote_data)

# Plot a count plot to see the distribution of data with respect to the values in the class that we want to predict
sns.countplot(x="Target", data=banknote_data)

# Divide the dataset into features and target labels.

## Feature set
X = banknote_data.drop(["Target"], axis=1)
print(X)

## Class set
y = banknote_data.filter(["Target"], axis=1)
print(y)

# Divide Data into Training and Test Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Scale the data
sc = StandardScaler()
X_train = sc.fit_transform(X=X_train)
X_test = sc.transform(X=X_test)

learning_rate = 0.001
dropout_rate = 0.1

model = Sequential()

# Adding dense layers
model.add(Dense(units=12, input_dim=X_train.shape[1], activation="relu"))
model.add(Dropout(rate=dropout_rate))
model.add(Dense(units=6, activation="relu"))
model.add(Dropout(rate=dropout_rate))
model.add(Dense(units=1, activation="sigmoid"))

# Compiling the model
adam = Adam(lr=learning_rate)
model.compile(optimizer=adam, metrics=["accuracy"], loss="binary_crossentropy")

# Plot the model's architecture via the plot_model() method from keras.utils module.
plot_model(model, to_file="model_plot1.jpg", show_shapes=True, show_layer_names=True)


# To train the model, you need to call the fit method on the model object.
model_history = model.fit(x=X_train, y=y_train, batch_size=4, epochs=20, validation_split=0.2)

# After the train, we can evaluate its performance by making predictions on the test set.
accuracies = model.evaluate(x=X_test, y=y_test)

print("Test Score(loss rate):  ", accuracies[0])
print("Test Accuracy: ", accuracies[1])

# Plot the accuracy on the training and test sets to see if our model is overfitting or not.
plt.plot(model_history.history["accuracy" ], label="accuracy")
plt.plot(model_history.history["val_accuracy" ], label="val_accuracy")
plt.legend(["train", "test"], loc="lower left")

plt.show()

# Plot the loss values for test and training sets
plt.plot(model_history.history["loss" ], label="loss")
plt.plot(model_history.history["val_loss" ], label="val_loss")
plt.legend(["train", "test"], loc="upper left")

plt.show()
