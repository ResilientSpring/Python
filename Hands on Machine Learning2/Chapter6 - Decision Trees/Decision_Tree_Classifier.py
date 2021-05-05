from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

iris = load_iris()
X = iris.data[:, 2:] # petal length and width
y = iris.target

tree_clf = DecisionTreeClassifier(max_depth=2)
tree_clf.fit(X=X, y=y)

export_graphviz(decision_tree=tree_clf, feature_names=iris.feature_names[2:],
                class_names=iris.target_names, rounded=True, filled=True)
