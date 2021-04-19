import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# load dataset
iris = load_iris()

# feature extraction
iris_data = iris.data
print(iris_data)

# label extraction
iris_label = iris.target
print(iris_label)

train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label,
                                                                  test_size=0.2, random_state=0)

# Initialize the algorithm
clf = tree.DecisionTreeClassifier(max_depth=2)

result = clf.fit(X=train_data, y=train_label)

y_prediction = clf.predict(X=test_data)

print("Prediction: ", y_prediction)
print("Answer:     ", test_label)

# Print the decision tree
tree.plot_tree(result)
