from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score

iris = load_iris()
iris_data=iris.data
print(iris_data)
X_train, X_test, y_train, y_test = train_test_split(iris_data, iris.target, test_size=0.33);

knn_clf = KNeighborsClassifier(n_neighbors=5)
classifier = knn_clf.fit(X=X_train, y=y_train)

y_prediction = classifier.predict(X=X_test)

print("Classification Report: ", '\n', classification_report(y_true=y_test, y_pred=y_prediction))
print("Accuracy: ", accuracy_score(y_true=y_test, y_pred=y_prediction))

scores = cross_val_score(estimator=knn_clf, X=X_train, y=y_train, scoring='accuracy', cv=10)
print("The accuracy is: ", scores)

print("Scores: ", scores)
print("Mean Scores: ", scores.mean())

y_prediction2 = knn_clf.predict(X=X_train)

print("Classification Report after K-fold cross validation", '\n',
      classification_report(y_true=y_train, y_pred=y_prediction2))
print("Accuracy: ", accuracy_score(y_true=y_train, y_pred=y_prediction2))
