import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

iris = load_iris()

iris_data = iris.data
iris_label = iris.target

print(iris_data)
print(iris_label)

train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label,
                                                                  test_size=0.33)

tree_classifier = DecisionTreeClassifier(max_depth=2)
tree_classifier.fit(X=train_data, y=train_label)

tree.plot_tree(tree_classifier, rounded=True, filled=True)
