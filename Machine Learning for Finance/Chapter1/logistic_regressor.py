import numpy as np

np.random.seed(1);

X = np.array([
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1],
    [0, 1, 1] ]);

y = np.array([[0, 1, 1, 0]]).T;

def sigmoid(x):
    return 1/(1+np.exp(-x));


W = 2 * np.random.random((3, 1)) -1;

b = 0;

# Linear step
z = X.dot(W) + b;

# Non-linear step
A = sigmoid(z);

print(A);