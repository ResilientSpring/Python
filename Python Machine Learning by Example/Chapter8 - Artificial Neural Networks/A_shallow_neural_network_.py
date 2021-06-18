import numpy as np

# We will use sigmoid as the activation function in this example.
def sigmoid(z):
    return 1.0 / (1 + np.exp(-z))


def sigmoid_derivative(z):
    return sigmoid(z) * (1.0 - sigmoid(z))


def train(X, y, learning_rate, n_iter, n_hidden=1):
    # m is the number of samples.
    m, n_input = X.shape

    # Before training, we first randomly initialize weights and biases.

    Weight1 = np.random.randn(n_input, n_hidden)

    Bias1 = np.zeros((1, n_hidden))

    Weight2 = np.random.randn(n_hidden, 1)

    Bias2 = np.zeros((1, 1))

    # In each iteration, we feed all layers of the network with the latest weights and biases.

    for i in range(1, n_iter + 1):

        Z2 = np.matmul(X, Weight1) + Bias1

        # The output values of the hidden layer.
        A2 = sigmoid(Z2)

        Z3 = np.matmul(A2, Weight2) + Bias2

        # The output values of the output layer.
        A3 = Z3

        # Calculate the gradients using the backpropagation algorithm.

        dZ3 = A3 - y

        dWeight2 = np.matmul(A2.T, dZ3)

        dBias2 = np.sum(dZ3, axis=0, keepdims=True)

        dZ2 = np.matmul(dZ3, Weight2.T) * sigmoid_derivative(Z2)

        dWeight1 =np.matmul(X.T, dZ2)

        dBias1 = np.sum(dZ2, axis=0)

        # Update the weights and biases with the resulting gradients.

        Weight2 = Weight2 - learning_rate * dWeight2 / m

        Bias2 = Bias2 - learning_rate * dBias2 / m

        Weight1 = Weight1 - learning_rate * dWeight1 / m

        Bias1 = Bias1 - learning_rate * dBias1 / m

        # Print out the loss and the mean squared error for every 100 iterations.
        if i % 100 == 0:
            cost = np.mean((y - A3) ** 2)

            print(f"Iteration {i}, training loss: {cost}")

        model = {'Weight1': Weight1, 'Bias1': Bias1, 'Weight2': Weight2, 'Bias2': Bias2}

        return model

# Take in a model and produce the regression results.
def predict(x, model):
    Weight1 = model['Weight1']
    bias1 = model['Bias1']
    Weight2 = model['Weight2']
    bias2 = model['Bias2']
    A2 = sigmoid(np.matmul(x, Weight1) + bias1)
    A3 = np.matmul(A2, Weight2) + bias2

    return A3