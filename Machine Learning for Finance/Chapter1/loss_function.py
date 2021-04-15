import numpy as np

def bce_loss(y, y_hat):

    N = y.shape[0];
    loss = -1/N * np.sum((y*np.log(y_hat) + (1 - y)*np.log(1-y_hat)));

    return loss;