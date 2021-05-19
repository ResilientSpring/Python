import numpy as np

# The matmul function implements the semantics of the @ operator introduced in Python 3.5

a = np.array([[1, 0],
              [0, 1]])

b = np.array([[4, 1],
              [2, 2]])

c = np.matmul(a, b)

print(c)

d = a @ b

print(d)

e = np.dot(a, b)

print(e)

# Source: https://numpy.org/doc/stable/reference/generated/numpy.matmul.html