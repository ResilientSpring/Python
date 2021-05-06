import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

iris = load_iris()

iris_data = iris.data
iris_label = iris.target

print(iris_data)
print(iris_label)