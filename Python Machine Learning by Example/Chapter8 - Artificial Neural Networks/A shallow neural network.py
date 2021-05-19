import numpy as np

def sigmoid(z):
    return 1.0/ (1 + np.exp(-z))


def sigmoid_derivative(z):
    return sigmoid(z) * (1.0 - sigmoid(z))


def train(X, y, n_hidden, learning_rate, n_iter):
    m, n_input = X.shape

    W1 = np.random.randn(n_input, n_hidden)

    b1 = np.zeros((1, n_hidden))

    W2 = np.random.randn(n_hidden, 1)

    b2 = np.zeros((1, 1))

    for i in range(1, n_iter + 1):

        Z2 = np.matmul(X, W1) + b1

        A2 =