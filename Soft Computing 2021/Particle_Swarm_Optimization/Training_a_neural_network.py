# Import modules
import numpy as np
import matplotlib.pyplot as plt

# Import PySwarms
import pyswarms as ps

data_inputs = np.array([[0, 0],
                        [0, 1],
                        [1, 0],
                        [1, 1]])

# XOR problem outputs
data_outputs = np.array([[0],
                         [1],
                         [1],
                         [0]])

n_inputs = 2
n_hidden = 2
n_classes = 2

num_samples = 150


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
    W1 = p[0:80].reshape((n_inputs, n_hidden))
    b1 = p[80:100].reshape((n_hidden,))
    W2 = p[100:160].reshape((n_hidden, n_classes))
    b2 = p[160:163].reshape((n_classes,))

    # Perform forward propagation
    z1 = X.dot(W1) + b1  # Pre-activation in Layer 1
    a1 = np.tanh(z1)  # Activation in Layer 1
    logits = a1.dot(W2) + b2  # Pre-activation in Layer 2
    return logits  # Logits for Layer 2


# Forward propagation
def forward_prop(params):
    """Forward propagation as objective function

    This computes for the forward propagation of the neural network, as
    well as the loss.

    Inputs
    ------
    params: np.ndarray
        The dimensions should include an unrolled version of the
        weights and biases.

    Returns
    -------
    float
        The computed negative log-likelihood loss given the parameters
    """

    logits = logits_function(params)

    # Compute for the softmax of the logits
    exp_scores = np.exp(logits)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

    # Compute for the negative log likelihood

    corect_logprobs = -np.log(probs[range(num_samples), y])
    loss = np.sum(corect_logprobs) / num_samples

    return loss
