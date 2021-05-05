from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

iris = load_iris()
X = iris.data[:, 2:] # petal length and width
y = iris.target

tree_clf = DecisionTreeClassifier(max_depth=2)
tree_clf.fit(X=X, y=y)

tree.plot_tree(decision_tree=tree_clf, feature_names=iris.feature_names[2:],
               class_names=iris.target_names, rounded=True, filled=True)

# A flower whose petals are 5 cm long and 1.5 cm wide.
probability = tree_clf.predict_proba([[5, 1.5]])
print(probability)

# A flower whose petals are 5 cm long and 1.5 cm wide.
prediction = tree_clf.predict([[5, 1.5]])
print(prediction)
