import numpy as np

def sigmoid(z):
    return 1.0 / (1 + np.exp(-z))


def fit(X, y, number_of_units_in_the_hidden_layer, iteration, velocity):

    the_number_of_samples, features_per_sample = X.shape

    weight1 = np.random.rand(number_of_units_in_the_hidden_layer, features_per_sample)
    bias1 = np.ones(number_of_units_in_the_hidden_layer)
    weight2 = np.random.rand(number_of_units_in_the_hidden_layer, 1)
    bias2 = np.ones(1)

    for i in range(1, iteration + 1):

        a12_input = np.dot(X, weight1)

