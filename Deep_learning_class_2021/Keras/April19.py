import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
iris_data=iris.data
print(iris_data)
X_train, X_test, y_train, y_test = train_test_split(iris_data, iris.target, test_size=0.2);

model = Sequential()
model.add(keras.Input(shape=(4, 1)));
model.add(Flatten());
model.add(Dense(units=64, activation="relu", name="layer1"))
model.add(Dropout(0.2))
model.add(Dense(units=128, activation="relu", name="layer2"))
model.add(Dropout(rate=0.2))
model.add(Dense(units=3, activation="softmax", name="layers3"));
print(model.summary());
