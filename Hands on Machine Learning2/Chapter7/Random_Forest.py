from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score
import numpy as np

X, y = make_moons(n_samples=500, noise=0.30, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

rnd_clf = RandomForestRegressor(n_estimators=500, max_leaf_nodes=16, n_jobs=-1)

rnd_clf.fit(X=X_train, y=y_train)

y_prediction = rnd_clf.predict(X=X_test)

Accuracy = np.sum(y_test == y_prediction) / len(y_test)

print(Accuracy)

print(accuracy_score(y_true=y_test, y_pred=y_prediction))
