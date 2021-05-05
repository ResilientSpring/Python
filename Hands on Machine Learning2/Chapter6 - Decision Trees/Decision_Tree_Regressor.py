from sklearn.tree import DecisionTreeRegressor
import numpy as np
from sklearn import tree
import matplotlib.pyplot as plt

# Quadratic training set + noise

np.random.seed(42)
m = 200

X = np.random.rand(m, 1)
y = 4 * (X - 0.5) ** 2

y = y + np.random.randn(m, 1) / 10

# Training a DecisionTree Regressor

tree_reg = DecisionTreeRegressor(max_depth=2)
tree_reg.fit(X=X, y=y)

tree.plot_tree(decision_tree=tree_reg)

plt.savefig("Decision_Tree_Regressor.jpg")
