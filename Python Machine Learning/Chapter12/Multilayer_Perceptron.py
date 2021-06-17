import numpy as np
import sys

class NeuralNetMLP(object):
    """Feedforward neural network / Multi-layer perceptron classifier.

    :parameter

    number_of_hidden_units : int (default:30)
        Number of hidden units.

    l2 : float (default: 0.)
        Lambda value for L2-regularization.
        No regularization if l2 = 0 (default)

    epochs : int (default: 100)
        Number of passes over the training set.

    eta : float (default: 0.001)
        Learning rate.

    shuffle : bool (default: True)
        Shuffles training data every epoch if true to prevent circles.

    minibatch_size : int (default: 1)
        Number of training examples per minibatch.

    seed : int (default: None)
        Random seed for initializing weights and shuffling.

    Attributes
    --------------------
    eval_ : dict
        Dictionary collecting the cost, training accuracy,
        and validation accuracy for each epoch during training.

    """

