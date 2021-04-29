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

per_clf = Perceptron()
per_clf.fit(X=X, y=y)

y_prediction = per_clf.predict(X=[[2, 0.5]])