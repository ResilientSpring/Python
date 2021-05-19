from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_boston

boston = load_boston()

# The last 10 samples as testing set.
number_of_test = 10

scaler = StandardScaler()

X_train = boston.data[:-number_of_test, :]

X_train = scaler.fit_transform(X=X_train)

y_train = boston.target[:- number_of_test].reshape(-1, 1)

print(y_train)

X_test = boston.data[-number_of_test: , : ]

X_test = scaler.fit_transform(X=X_test)

y_test = boston.target[-number_of_test:]

# Model creation

## Two hidden layers with 16 and 8 nodes, respectively.
nn_scikit = MLPRegressor(hidden_layer_sizes=(16, 8), activation='relu', solver='adam',
                         learning_rate_init=0.001, random_state=42, max_iter=2000)

# Fit the created neural network model on the training set
nn_scikit.fit(X=X_train, y=y_train)

# Predict on the testing data using the fitted model
y_prediction = nn_scikit.predict(X=X_test)

print(y_prediction)

print(y_test)
