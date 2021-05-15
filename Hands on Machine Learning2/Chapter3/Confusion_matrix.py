from sklearn.linear_model import SGDClassifier
from sklearn.datasets import fetch_openml
import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split, cross_val_predict
from sklearn.metrics import confusion_matrix

mnist = fetch_openml('mnist_784', version=1, as_frame=False)
print(mnist.keys())

X, y = mnist["data"], mnist["target"]

print(X.shape)

print(y.shape)

X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]

y_train_5 = (y_train == 5)
y_test_5 = (y_test == 5)

sgd_classifier = SGDClassifier(max_iter=1000, random_state=42)
sgd_classifier.fit(X=X_train, y=y_train_5)

y_train_prediction = cross_val_predict(estimator=sgd_classifier, X=X_train, y=y_train_5, cv=3)

result = confusion_matrix(y_true=y_train_5, y_pred=y_train_prediction)

print(result)
