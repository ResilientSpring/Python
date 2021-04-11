class AdalineGD:
    """ADAptive LInear NEuron classifier

    Parameters
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