import numpy as np


class Perceptron:

    def __init__(self, learning_rate=0.01, number_of_iteration=1000):
        self.lr = learning_rate;
        self.n_iters = number_of_iteration;
        self.activation_func = self._unit_step_func;
        self.weight = None;
        self.bias = None;

    def fit(self, x, y):
        pass;

    def _unit_step_function(self, x):
        if x >= 0:
            return 1;
        else:
            return 0;

    def _unit_step_func(self, x):
        return np.where(x >= 0, 1, 0);
