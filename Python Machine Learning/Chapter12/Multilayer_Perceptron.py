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

    def __init__(self, number_of_hidden_units=30, l2=0., epochs=100, eta=0.001,
                 shuffle=True, minibatch_size=1, seed=None):
        self.random = np.random.RandomState(seed)
        self.n_hidden = number_of_hidden_units
        self.l2 = l2
        self.epochs = epochs
        self.eta = eta
        self.shuffle = shuffle
        self.minibatch_size = minibatch_size

    def _sigmoid(self, z):
        """Compute logistic function (sigmoid)"""

        return 1. / (1. + np.exp(-np.clip(z, -250, 250)))

    def _forward(self, X):
        """Compute forward propagation step"""

        # step 1: net input of hidden layer
        # [n_examples, n_features] dot [n_features, n_hidden]
        # -> [n_examples, n_hidden]
        z_h = np.dot(X, self.w_h) + self.b_h

        # step 2: activation of hidden layer
        a_h = self._sigmoid(z_h)

        # step 3: net input of output layer
        # [n_examples, n_hidden] dot [n_hidden, n_classlabels]
        # -> [n_examples, n_classlabels]

        z_out = np.dot(a_h, self.w_out) + self.b_out

        # step 4: activation output layer
        a_out = self._sigmoid(z_out)

        return z_h, a_h, z_out, a_out


    def _compute_cost(self, y_enc, output):
        """Compute cost function.
        Parameters
        ----------
        y_enc : array, shape = (n_examples, n_labels)
            one-hot encoded class labels.
        output : array, shape = [n_examples, n_output_units]
            Activation of the output layer (forward propagation)
        Returns
        ---------
        cost : float
            Regularized cost
        """
        L2_term = (self.l2 *
                   (np.sum(self.w_h ** 2.) +
                    np.sum(self.w_out ** 2.)))

        term1 = -y_enc * (np.log(output))
        term2 = (1. - y_enc) * np.log(1. - output)
        cost = np.sum(term1 - term2) + L2_term