from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_boston
import A_shallow_neural_network_ as artificial_neural_network

boston = load_boston()

# The last 10 samples as testing set.
number_of_test = 10

scaler = StandardScaler()

X_train = boston.data[:-number_of_test, :]

X_train = scaler.fit_transform(X=X_train)

y_train = boston.target[:- number_of_test].reshape(-1, 1)

# print(y_train)

X_test = boston.data[-number_of_test: , : ]

X_test = scaler.fit_transform(X=X_test)

y_test = boston.target[-number_of_test:]

# With the scaled dataset, we can now train a one-layer neural network with 20 hidden units,
# a 0.1 learning rate, and 2000 iterations.
model = artificial_neural_network.train(X=X_train, y=y_train, learning_rate=0.1, n_hidden=20,
                                        n_iter=2000)


# Finally, we apply the trained model on the testing set.
predictions = artificial_neural_network.predict(x=X_test, model=model)

# Print out the predictions and their ground truths to compare them.
# print(predictions)

# print(predictions.mean())

# print(y_test)

# print(y_test.mean())
