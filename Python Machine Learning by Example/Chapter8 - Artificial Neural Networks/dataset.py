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