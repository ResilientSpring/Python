from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=500, noise=0.30, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# First, let's fit a DecisionTreeRegressor to the training set.
tree_reg1 = DecisionTreeRegressor(max_depth=2)
tree_reg1.fit(X=X, y=y)

# Next, we will train a second DecisionTreeRegressor on the residual errors made by the first
# predictor.
y2 = y - tree_reg1.predict(X=X)

tree_reg2 = DecisionTreeRegressor(max_depth=2)
tree_reg2.fit(X=X, y=y2)

# Then, we train a third regressor on the residual errors made by the second predictor.
y3 = y2 - tree_reg2.predict(X=X)

tree_reg3 = DecisionTreeRegressor(max_depth=2)

tree_reg3.fit(X=X, y=y3)

# Now that we have an ensemble containing three trees.

## This ensemble can now make predictions on a new instance simply by adding up the predictions of
# all the trees.
y_prediction = sum(tree.predict(X=X_new) for tree in (tree_reg1, tree_reg2, tree_reg3))