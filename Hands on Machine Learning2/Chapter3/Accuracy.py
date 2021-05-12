from sklearn.base import BaseEstimator
from sklearn.datasets import fetch_openml
import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split

mnist = fetch_openml('mnist_784', version=1, as_frame=False)
print(mnist.keys())

X, y = mnist["data"], mnist["target"]

print(X.shape)

print(y.shape)

X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]


class Never5Classifier(BaseEstimator):
    def fit(self, X, y=None):
        pass

    def predict(self, X):
        return np.zeros((len(X), 1), dtype=bool)


never_5_classifier = Never5Classifier()

y_train_5 = (y_train == 5)
y_test_5 = (y_test == 5)

scores = cross_val_score(estimator=never_5_classifier, X=X_train, y=y_train_5, scoring="accuracy",
                         cv=3)
print(scores)
