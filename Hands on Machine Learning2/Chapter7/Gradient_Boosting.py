from sklearn.tree import DecisionTreeRegressor
import numpy as np

np.random.seed(42)
X = np.random.rand(100, 1) - 0.5
y = 3*X[:, 0]**2 + 0.05 * np.random.randn(100)

# First, let's fit a DecisionTreeRegressor to the training set.
tree_reg1 = DecisionTreeRegressor(max_depth=2, random_state=42)
tree_reg1.fit(X=X, y=y)

# Next, we will train a second DecisionTreeRegressor on the residual errors made by the first
# predictor.
y2 = y - tree_reg1.predict(X=X)

tree_reg2 = DecisionTreeRegressor(max_depth=2, random_state=42)
tree_reg2.fit(X=X, y=y2)

# Then, we train a third regressor on the residual errors made by the second predictor.
y3 = y2 - tree_reg2.predict(X=X)

tree_reg3 = DecisionTreeRegressor(max_depth=2, random_state=42)

tree_reg3.fit(X=X, y=y3)

# Now that we have an ensemble containing three trees.

## This ensemble can now make predictions on a new instance simply by adding up the predictions of
# all the trees.

X_new = np.array([[0.8]])

y_prediction = sum(tree.predict(X=X_new) for tree in (tree_reg1, tree_reg2, tree_reg3))

print(y_prediction)
