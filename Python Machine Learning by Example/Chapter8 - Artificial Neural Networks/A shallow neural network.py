import numpy as np

def sigmoid(z):
    return 1.0/ (1 + np.exp(-z))


def sigmoid_derivative(z):
    return sigmoid(z) * (1.0 - sigmoid(z))


def train(X, y, n_hidden, learning_rate, n_iter):
    m, n_input = X.shape

    W1 = np.random.randn(n_input, n_hidden)