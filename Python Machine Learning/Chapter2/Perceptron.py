import pandas as pd
import numpy as np

class Perceptron(object):
    """Perceptron classifier.

    :parameter
    -------------------
    eta: float
        Learning rate (between 0.0 and 1.0)
    n_iter: int
        Passes over the training dataset.
    """