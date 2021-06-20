# Import modules
import numpy as np
import matplotlib.pyplot as plt

# Import PySwarms
import pyswarms as ps

n_inputs = 4
n_hidden = 20
n_classes = 3

num_samples = 150

X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([0, 1, 1, 0])


def logits_function(p):
    """ Calculate roll-back the weights and biases

    Inputs
    ------
    p: np.ndarray
        The dimensions should include an unrolled version of the
        weights and biases.

    Returns
    -------
    numpy.ndarray of logits for layer 2

    """
    # Roll-back the weights and biases
    W1 = np.random.rand(2, 2).reshape((n_inputs, n_hidden))
    b1 = np.random.rand(1, 2).reshape((n_hidden,))
    W2 = p[100:160].reshape((n_hidden, n_classes))
    b2 = p[160:163].reshape((n_classes,))

    # Perform forward propagation
    z1 = X.dot(W1) + b1  # Pre-activation in Layer 1
    a1 = np.tanh(z1)  # Activation in Layer 1
    logits = a1.dot(W2) + b2  # Pre-activation in Layer 2

    return logits  # Logits for Layer 2
