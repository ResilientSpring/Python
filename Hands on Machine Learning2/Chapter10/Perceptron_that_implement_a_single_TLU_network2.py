import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron

iris = load_iris()
X = iris.data[:, (2, 3)] # petal length, petal width

print(X)

y = (iris.target == 0).astype(np.int)  # Iris setosa?

print(y)

per_clf = Perceptron()
per_clf.fit(X=X, y=y)

y_prediction = per_clf.predict(X=[[2, 0.5]])