import numpy as np
import logistic_regression
import matplotlib.pyplot as plt

X_train = np.array([[6, 7], [2, 4], [3, 6], [4, 7], [1, 6],
                    [5, 2], [2, 0], [6, 3], [4, 1], [7, 2]]);

y_train = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1]);

# We train a logistic regression model for 1000 iterations, at a learning rate of 0.1
# based on intercept-included weights:
weights = logistic_regression.train_logistic_regression(X_train=X_train, y_train=y_train,
                                                        max_iter=1000, learning_rate=0.1,
                                                        fit_intercept=True);

X_test = np.array([[6, 1], [1, 3], [3, 1], [4, 5]]);
predictions = logistic_regression.predict(X=X_test, weights=weights);
print(predictions);

# To visualize this:
plt.scatter(x=X_train[:, 0], y=X_train[:, 1], c=['b']*5+['k']*5, marker='o')

## Blue dots are training samples from class 0, black dots are those from class 1
## Use 0.5 as the classification decision threshold.
colours = ['k' if prediction >= 0.5 else 'b' for prediction in predictions]
plt.scatter(x=X_test[:, 0], y=X_test[:, 1], marker='*', c=colours)

plt.xlabel("x1");
plt.ylabel("x2");

plt.savefig("Implementing_logistic_regression.jpg")

plt.show();