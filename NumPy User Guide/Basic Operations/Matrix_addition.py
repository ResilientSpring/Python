import numpy as np

num_samples = 4

X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([0, 1, 1, 0])

n_inputs = 2
n_hidden = 2
n_classes = 1

W1 = np.random.rand(2, 2).reshape((n_inputs, n_hidden))
print(W1)
print(W1.shape)

b1 = np.random.rand(1, 2).reshape((n_hidden,))
print(b1)
print(b1.shape)

z1 = X.dot(W1)
print(z1)

