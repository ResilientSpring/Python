from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score

X, y = make_moons(n_samples=500, noise=0.30, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

bag_clf = BaggingClassifier(base_estimator=DecisionTreeClassifier(), n_estimators=500,
                            max_samples=100, bootstrap=True, n_jobs=-1)

bag_clf.fit(X=X_train, y=y_train)

y_prediction = bag_clf.predict(X=X_test)

print("Accuracy score: ", accuracy_score(y_true=y_test, y_pred=y_prediction))

bagging2 = BaggingClassifier(base_estimator=DecisionTreeClassifier(), n_estimators=500,
                             max_samples=100, bootstrap=True, oob_score=True)

bagging2.fit(X=X_train, y=y_train)

y_prediction2 = bagging2.predict(X=X_test)

print(bagging2.oob_score_)
print("Accuracy score: ", accuracy_score(y_true=y_test, y_pred=y_prediction2))
