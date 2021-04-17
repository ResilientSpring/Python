import numpy as np
import sigmoid as s

def compute_prediction(X, weights):
    """Compute the prediction y_hat based on current weights"""

    z = np.dot(X, weights);
    predictions = s.sigmoid(z);

    return predictions;