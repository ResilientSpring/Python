import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron

iris = load_iris()
print(iris)

print('\n', 30*"=", '\n')

X = iris['data']
print(X)

print('\n', 30*"=", '\n')

X1 = iris.data[:, (2, 3)]
print(X1)
