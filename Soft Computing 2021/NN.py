# Import modules
import numpy as np
import matplotlib.pyplot as plt

# Import PySwarms
import pyswarms as ps

input_features = 2
neurons_per_hidden = 2
number_of_classes = 1   # Either 0, or 1.
number_of_samples = 4

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

    # step 1: net input of hidden layer
    # [n_examples, n_features] dot [n_features, n_hidden]
    # -> [n_examples, n_hidden]
    z_h = np.dot(X, w_h) + b_h

    # step 2: activation of hidden layer
    a_h = _sigmoid(z_h)

    # step 3: net input of output layer
    # [n_examples, n_hidden] dot [n_hidden, n_classlabels]
    # -> [n_examples, n_classlabels]
    z_out = np.dot(a_h, w_out) + b_out

    # step 4: activation output layer
    a_out = _sigmoid(z_out)

    # Roll-back the weights and biases
    W1 = p[0:80].reshape((n_inputs,neurons_per_hidden))
    b1 = p[80:100].reshape((n_hidden,))
    W2 = p[100:160].reshape((n_hidden,n_classes))
    b2 = p[160:163].reshape((n_classes,))

    # Perform forward propagation
    z1 = X.dot(W1) + b1  # Pre-activation in Layer 1
    a1 = np.tanh(z1)     # Activation in Layer 1
    logits = a1.dot(W2) + b2 # Pre-activation in Layer 2
    return logits          # Logits for Layer 2