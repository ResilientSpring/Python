from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_moons
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
import numpy as np

X, y = make_moons(n_samples=500, noise=0.30, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

rnd_clf = RandomForestClassifier(n_estimators=500, max_leaf_nodes=16, n_jobs=-1)

rnd_clf.fit(X=X_train, y=y_train)

y_prediction = rnd_clf.predict(X=X_test)
print(y_prediction)

# The BaggingClassifier equivalent.
bagging_classifier = BaggingClassifier(base_estimator=
                                       DecisionTreeClassifier(splitter="random", max_leaf_nodes=16),
                                       n_estimators=500, max_samples=1.0, bootstrap=True, n_jobs=-1)

bagging_classifier.fit(X=X_train, y=y_train)

y_prediction2 = bagging_classifier.predict(X=X_test)

print(y_prediction2)

comparison = np.sum(y_prediction2 == y_prediction) / len(y_prediction2)

print(comparison)  # very similar predictions

sum_1 = np.sum(y_prediction)
sum_2 = np.sum(y_prediction2)

print(sum_1, "\n", sum_2)  # very similar predictions
