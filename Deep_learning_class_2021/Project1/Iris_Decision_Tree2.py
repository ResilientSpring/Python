import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score

iris = load_iris()

iris_data = iris.data
iris_label = iris.target

print(iris_data)
print(iris_label)

train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label,
                                                                  test_size=0.33)

tree_classifier = DecisionTreeClassifier(max_depth=2)
tree_classifier.fit(X=train_data, y=train_label)

y_prediction = tree_classifier.predict(X=test_data)

target_name = ['setosa', 'versicolor', 'virginica']

print("Classification Report:", '\n',
      classification_report(y_true=test_label, y_pred=y_prediction,
                            target_names=target_name))

print("Accuracy: ", accuracy_score(y_true=test_label, y_pred=y_prediction))

scores = cross_val_score(estimator=tree_classifier, X=train_data, y=train_label, cv=10,
                         scoring='accuracy')

print("Scores: ", scores)
print("Mean: ", scores.mean())

y_prediction2 = tree_classifier.predict(X=train_data)

print("Classification Report with K-fold cross validation:", '\n',
      classification_report(y_true=train_label, y_pred=y_prediction2,
                            target_names=target_name))
print("Accuracy: ", accuracy_score(y_true=train_label, y_pred=y_prediction2))
