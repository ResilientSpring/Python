import numpy as np

def sigmoid(z):
    return 1.0 / (1 + np.exp(-z))


def fit(X, y, number_of_units_in_the_hidden_layer, iteration, velocity):
    X0 = 1
    X1 = X[0]
    X2 = X[1]

    weight_X0_a12 = np.random.rand()
    weight_X0_a22 = np.random.rand()
    weight_X1_a12 = np.random.rand()
    weight_X1_a22 = np.random.rand()
    weight_X2_a12 = np.random.rand()
    weight_X2_a22 = np.random.rand()

    a02 = 1
    weight_a02_a13 = np.random.rand()
    weight_a12_a13 = np.random.rand()
    weight_a22_a13 = np.random.rand()

    for i in range(1, iteration + 1):
        input_a12  = (X1 * weight_X1_a12) + (X2 * weight_X2_a12) + (X0 * weight_X0_a12)
        output_a12 = sigmoid(input_a12)

        input_a22  = (X1 * weight_X1_a22) + (X2 * weight_X2_a22) + (X0 * weight_X0_a22)
        output_a22 = sigmoid(input_a22)

        input_a13  = (a02 * weight_a02_a13) + (output_a12 * weight_a12_a13) + (output_a22 * weight_a22_a13)
        output_a13 = input_a13
