import numpy as np
import sigmoid as s


# Defining the function that computes the prediction y_hat(x) with the current weights.
def compute_prediction(X, weights):
    """Compute the prediction y_hat based on current weights"""

    z = np.dot(X, weights);
    predictions = s.sigmoid(z);

    return predictions;


# The function updating the weights by one step in a gradient descent manner.
def update_weights_sgd(X_train, y_train, weights, learning_rate):
    """
    One weight update iteration:
        moving weights by one step based on each individual sample.

    :arg
    X_train, y_train: numpy.ndarray
        training data sets

    weights: numpy.ndarray
    learning_rate : float

    :returns
    updated_weights: numpy.ndarray

    """

    for X_each, y_each in zip(X_train, y_train):
        prediction = compute_prediction(X=X_each, weights=weights)
        weights_delta = X_each.T * (y_each - prediction)
        weights += learning_rate * weights_delta;
    return weights;


# The function calculating the cost J(w)
def compute_cost(X, y, weights):
    """Compute the cost J(w)"""

    predictions = compute_prediction(X=X, weights=weights);
    cost = np.mean(-y * np.log(predictions) - (1 - y) * np.log(1 - predictions))

    return cost;


# Now, we connect all the functions above to the model training function:
def train_logistic_regression_sgd(X_train, y_train, max_iter, learning_rate, fit_intercept=False):
    """
    Train a logistic regression model via stochastic gradient descent

    :arg
    X_train, y_train: numpy.ndarray
        training data set
    max_iter: int
        number of iterations
    learning_rate: float

    fit_intercept: bool
        with an intercept w0 or not

    :returns
    numpy.ndarray
    learned weights

    """

    if fit_intercept:
        intercept = np.ones((X_train.shape[0], 1));
        X_train = np.hstack((intercept, X_train))

    weights = np.zeros(X_train.shape[1])

    # Updating the "weights" vector in each iteration.
    for iteration in range(max_iter):
        weights = update_weights_sgd(X_train=X_train, y_train=y_train,
                                     weights=weights, learning_rate=learning_rate)

        # Check the cost for every 2 iterations, for example.
        if iteration % 2 == 0:
            # Printing out the current cost for every 1-- iterations to ensure cost is
            # decreasing and that things are on the right track.
            print(compute_cost(X=X_train, y=y_train, weights=weights))

    return weights;


# Finally, we predict the results of new inputs using the trained model as follows:
def predict(X, weights):
    if X.shape[1] == weights.shape[0] - 1:
        intercept = np.ones((X.shape[0], 1))
        X = np.hstack((intercept, X))

    return compute_prediction(X=X, weights=weights);
