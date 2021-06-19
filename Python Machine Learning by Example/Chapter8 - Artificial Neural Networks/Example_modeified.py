'''
Source codes for Python Machine Learning By Example 3rd Edition (Packt Publishing)
Chapter 8  Predicting Stock Price with Artificial Neural Networks
Author: Yuxi (Hayden) Liu (yuxi.liu.ece@gmail.com)
'''

import numpy as np


def sigmoid(z):
    return 1.0 / (1 + np.exp(-z))


def sigmoid_derivative(z):
    return sigmoid(z) * (1.0 - sigmoid(z))



def train(X, y, the_number_of_units_in_a_hidden_layer, learning_rate, n_iter):
    # m is the number of samples.
    m, n_input = X.shape

    # Before training, we first randomly initialize weights and biases.
    W1 = np.random.randn(n_input, the_number_of_units_in_a_hidden_layer)
    b1 = np.zeros((1, the_number_of_units_in_a_hidden_layer))
    W2 = np.random.randn(the_number_of_units_in_a_hidden_layer, 1)
    b2 = np.zeros((1, 1))

    # In each iteration, we feed all layers of the network with the latest weights and biases.
    for i in range(1, n_iter+1):
        Z2 = np.matmul(X, W1) + b1

        # The output values of the hidden layer.
        A2 = sigmoid(Z2)

        Z3 = np.matmul(A2, W2) + b2

        # The output values of the output layer.
        A3 = Z3

        # Calculate the gradients using the backpropagation algorithm.
        dZ3 = A3 - y
        dW2 = np.matmul(A2.T, dZ3)
        db2 = np.sum(dZ3, axis=0, keepdims=True)

        dZ2 = np.matmul(dZ3, W2.T) * sigmoid_derivative(Z2)
        dW1 = np.matmul(X.T, dZ2)
        db1 = np.sum(dZ2, axis=0)

        # Update the weights and biases with the resulting gradients.
        W2 = W2 - learning_rate * dW2 / m
        b2 = b2 - learning_rate * db2 / m
        W1 = W1 - learning_rate * dW1 / m
        b1 = b1 - learning_rate * db1 / m

        # Print out the loss and the mean squared error for every 100 iterations.
        if i % 1 == 0:
            cost = np.mean((y - A3) ** 2)
            print('Iteration %i, training loss: %f' % (i, cost))

    model = {'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2}
    return model


# Take in a model and produce the regression results.
def predict(x, model):
    W1 = model['W1']
    b1 = model['b1']
    W2 = model['W2']
    b2 = model['b2']
    A2 = sigmoid(np.matmul(x, W1) + b1)
    A3 = np.matmul(A2, W2) + b2
    return A3


from sklearn import datasets
boston = datasets.load_boston()
num_test = 10  # the last 10 samples as testing set

from sklearn import preprocessing
scaler = preprocessing.StandardScaler()

X_train = boston.data[:-num_test, :]
X_train = scaler.fit_transform(X_train)
y_train = boston.target[:-num_test].reshape(-1, 1)
X_test = boston.data[-num_test:, :]
X_test = scaler.transform(X_test)
y_test = boston.target[-num_test:]


n_hidden = 20
learning_rate = 0.1
n_iter = 2000

model = train(X_train, y_train, n_hidden, learning_rate, n_iter)
predictions = predict(X_test, model)
print(predictions)
print(y_test)
