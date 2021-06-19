import numpy as np


class Particle_Swarm_Optimization(object):

    def __init__(self, number_of_units_in_the_hidden_layer=2, l2=0., iterations=100, velocity=0.001,
                 shuffle=True, minibatch_size=1, seed=None):
        self.random = np.random.RandomState(seed)
        self.number_of_hidden_units = number_of_units_in_the_hidden_layer
        self.l2 = l2
        self.iterations = iterations
        self.velocity = velocity
        self.shuffle = shuffle
        self.minibatch_size = minibatch_size

    def sigmoid(self, z):
        return 1.0 / (1 + np.exp(-z))


    def forward(self, X):
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

        for i in range(1, self.iterations + 1):
            input_a12 = (X1 * weight_X1_a12) + (X2 * weight_X2_a12) + (X0 * weight_X0_a12)
            output_a12 = self.sigmoid(input_a12)

            input_a22 = (X1 * weight_X1_a22) + (X2 * weight_X2_a22) + (X0 * weight_X0_a22)
            output_a22 = self.sigmoid(input_a22)

            input_a13 = (a02 * weight_a02_a13) + (output_a12 * weight_a12_a13) + (output_a22 * weight_a22_a13)
            output_a13 = self.sigmoid(input_a13)


    def _compute_cost(self, y_true, output):
        """Compute cost function.
        Parameters
        ----------
        y_true : array, shape = (n_examples, n_labels)
            one-hot encoded class labels.
        output : array, shape = [n_examples, n_output_units]
            Activation of the output layer (forward propagation)
        Returns
        ---------
        cost : float
            Regularized cost
        """

        L2_term = (self.l2 * (np.sum(self.w_h ** 2.) + np.sum(self.w_out ** 2.)))

        term1 = -y_true * (np.log(output))
        term2 = (1. - y_true) * np.log(1. - output)
        cost = np.sum(term1 - term2) + L2_term

        # If you are applying this cost function to other
        # datasets where activation
        # values maybe become more extreme (closer to zero or 1)
        # you may encounter "ZeroDivisionError"s due to numerical
        # instabilities in Python & NumPy for the current implementation.
        # I.e., the code tries to evaluate log(0), which is undefined.
        # To address this issue, you could add a small constant to the
        # activation values that are passed to the log function.
        #
        # For example:
        #
        # term1 = -y_enc * (np.log(output + 1e-5))
        # term2 = (1. - y_enc) * np.log(1. - output + 1e-5)

        return cost


