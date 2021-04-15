import numpy as np

def loss_derivative(A, N, X, y):
    dz = (A - y);
    dW = 1 / N * np.dot(X.T, dz);

    db = 1 / N * np.sum(dz, axis=0, keepdims=True);