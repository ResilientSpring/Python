import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
import pandas as pd

iris = load_iris()
X = pd.DataFrame(data=iris.data)
print(X)

y = pd.DataFrame(data=iris.target)
print(y)

y_numpy = y.to_numpy()
print(y_numpy)
print(y_numpy.shape)
y_numpy = np.squeeze(a=y_numpy, axis=1)
print(y_numpy)

y = y_numpy

X1 = X.iloc[:, [2, 3]]
print(X1)

per_clf = Perceptron()
per_clf.fit(X=X1, y=y)

y_prediction = per_clf.predict(X=[[2, 0.5]])

print(y_prediction)
