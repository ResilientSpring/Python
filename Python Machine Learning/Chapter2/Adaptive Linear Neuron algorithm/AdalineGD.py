class AdalineGD:
    """ADAptive LInear NEuron classifier

    :parameter
    ------------
    eta: float
        Learning rate (between 0.0 and 1.0)

    n_iter: int
        Passes over the training dataset.

    randome_state: int
        Random number generator seed for random weight initialization.

    Attributes
    -------------
    w_: 1d-array
        Weights after fitting.

    cost_: list
        Sum-of-squares cost function value in each epoch.

    """

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta;
        self.n_iter = n_iter;
        self.random_state = random_state;

    def fit(self, X, y):
        """Fit training data.

        :parameter
        X: {array-like}, shape = [n_examples, n_features]

            Training vectors, where n-examples is the number of examples
            and n_features is the number of features.

        y: array-like, shape = [n_examples]

            Target values.

         :return
            self: object
        """