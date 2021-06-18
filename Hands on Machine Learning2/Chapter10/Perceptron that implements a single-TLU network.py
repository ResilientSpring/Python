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

print('\n', 30*'=', '\n')

y = iris.target
print(y)

print('\n', 30*'=', '\n')

per_clf = Perceptron()

per_clf.fit(X=X1, y=y)

y_prediction = per_clf.predict(X=[[2, 0.5]])
print(y_prediction)
